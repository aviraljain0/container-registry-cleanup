import requests
from datetime import datetime

# ==========================================
# Docker Hub Configuration
# ==========================================

USERNAME = "ibm1container1cleanup1team"
PASSWORD = "ibmcloud24"   # <-- your Docker Hub password
REPOSITORY = "container-registry-cleanup"

BASE_URL = f"https://hub.docker.com/v2/repositories/{USERNAME}/{REPOSITORY}/tags/"

# Tags that should be cleaned up
DELETE_TAGS = {"old", "backup", "test", "debug"}

# ==========================================
# Authenticate with Docker Hub
# ==========================================

print("Authenticating with Docker Hub...")

auth_url = "https://hub.docker.com/v2/users/login/"
auth_data = {"username": USERNAME, "password": PASSWORD}
auth_response = requests.post(auth_url, json=auth_data)

if auth_response.status_code != 200:
    print("Authentication failed:", auth_response.text)
    exit()

token = auth_response.json()["token"]
headers = {"Authorization": f"JWT {token}"}

print("Authentication successful!\n")

# ==========================================
# Fetch Tags
# ==========================================
  
print("Fetching tags from repository...")

response = requests.get(BASE_URL, headers=headers, timeout=10)
if response.status_code != 200:
    print("Failed to fetch tags:", response.text)
    exit()

data = response.json()

keep_images = []
delete_images = []

# ==========================================
# Create Log File
# ==========================================

with open("cleanup.log", "w", encoding="utf-8") as log:

    log.write("DOCKER HUB CLEANUP REPORT\n")
    log.write("=" * 60 + "\n")
    log.write(f"Repository : {REPOSITORY}\n")
    log.write(f"Generated  : {datetime.now()}\n\n")

    # ==========================================
    # Process Images
    # ==========================================

    for image in data["results"]:
        tag = image["name"]
        updated = image["last_updated"]

        print(f"[INFO] Processing tag : {tag}")
        print(f"[INFO] Last Updated   : {updated}")

        if tag.lower() in DELETE_TAGS:
            decision = "DELETE"
            reason = "Cleanup policy matched"
            delete_images.append(tag)
        else:
            decision = "KEEP"
            reason = "Active image"
            keep_images.append(tag)

        log.write(f"Tag          : {tag}\n")
        log.write(f"Last Updated : {updated}\n")
        log.write(f"Decision     : {decision}\n")
        log.write(f"Reason       : {reason}\n")
        log.write("-" * 60 + "\n")

    # ==========================================
    # Summary (Dry Run)
    # ==========================================

    print("=" * 50)
    print("Cleanup Completed (Dry Run)")
    print("=" * 50)

    print(f"Total Images              : {len(data['results'])}")
    print(f"Images Kept               : {len(keep_images)}")
    print(f"Images Marked for Cleanup : {len(delete_images)}")

    print("\nKEEP:")
    for image in keep_images:
        print(image)

    print("\nDELETE:")
    for image in delete_images:
        print(image)

    log.write("\nSUMMARY\n")
    log.write("=" * 60 + "\n")
    log.write(f"Total Images              : {len(data['results'])}\n")
    log.write(f"Images Kept               : {len(keep_images)}\n")
    log.write(f"Images Marked for Cleanup : {len(delete_images)}\n\n")

    log.write("KEEP\n")
    for image in keep_images:
        log.write(f"{image}\n")

    log.write("\nDELETE\n")
    for image in delete_images:
        log.write(f"{image}\n")

# ==========================================
# Verification before deletion
# ==========================================

choice = input("\nDo you want to delete these tags from Docker Hub? (yes/no): ").strip().lower()

if choice == "yes":
    confirm_repo = input(f"Type the repository name ({REPOSITORY}) to confirm deletion: ").strip()
    if confirm_repo == REPOSITORY:
        for tag in delete_images:
            delete_url = f"{BASE_URL}{tag}/"
            del_response = requests.delete(delete_url, headers=headers)
            if del_response.status_code == 204:
                print(f"[INFO] Deleted tag: {tag}")
            else:
                print(f"[ERROR] Failed to delete {tag}: {del_response.status_code} {del_response.text}")
        print("\nDeletion completed.")
    else:
        print("\nRepository name did not match. No tags were deleted.")
else:
    print("\nNo tags were deleted. Dry run only.")

