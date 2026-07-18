import requests
from datetime import datetime
import os

# ==========================================
# Docker Hub Configuration
# ==========================================

USERNAME = os.getenv("DOCKER_USERNAME")
PASSWORD = os.getenv("DOCKER_PASSWORD")
REPOSITORY = "container-registry-cleanup"

BASE_URL = f"https://hub.docker.com/v2/repositories/{USERNAME}/{REPOSITORY}/tags/"

# Tags that should be marked for cleanup
DELETE_TAGS = {"old", "backup", "test", "debug"}

# ==========================================
# Authenticate with Docker Hub
# ==========================================

print("Authenticating with Docker Hub...")

auth_url = "https://hub.docker.com/v2/users/login/"
auth_data = {
    "username": USERNAME,
    "password": PASSWORD
}

auth_response = requests.post(auth_url, json=auth_data)

if auth_response.status_code != 200:
    print("Authentication Failed!")
    print(auth_response.text)
    exit()

token = auth_response.json()["token"]
headers = {
    "Authorization": f"JWT {token}"
}

print("Authentication successful!\n")

# ==========================================
# Fetch Repository Tags
# ==========================================

print("Fetching tags from repository...\n")

response = requests.get(BASE_URL, headers=headers, timeout=10)

if response.status_code != 200:
    print("Failed to fetch repository tags.")
    print(response.text)
    exit()

data = response.json()

keep_images = []
delete_images = []

# ==========================================
# Create Cleanup Log
# ==========================================

with open("cleanup.log", "w", encoding="utf-8") as log:

    log.write("DOCKER HUB CLEANUP REPORT\n")
    log.write("=" * 60 + "\n")
    log.write(f"Repository : {REPOSITORY}\n")
    log.write(f"Generated  : {datetime.now()}\n\n")

    # ==========================================
    # Process Each Image
    # ==========================================

    for image in data["results"]:

        tag = image["name"]
        updated = image["last_updated"]

        print(f"[INFO] Processing tag : {tag}")
        print(f"[INFO] Last Updated   : {updated}")

        if tag.lower() in DELETE_TAGS:
            status = "MARKED FOR CLEANUP"
            reason = "Cleanup policy matched"
            delete_images.append(tag)
        else:
            status = "KEEP"
            reason = "Active image"
            keep_images.append(tag)

        print(f"[INFO] Status         : {status}")
        print(f"[INFO] Reason         : {reason}\n")

        log.write(f"Tag          : {tag}\n")
        log.write(f"Last Updated : {updated}\n")
        log.write(f"Status       : {status}\n")
        log.write(f"Reason       : {reason}\n")
        log.write("-" * 60 + "\n")

    # ==========================================
    # Summary
    # ==========================================

    total_images = len(data["results"])

    print("=" * 55)
    print("Cleanup Completed (Dry Run)")
    print("=" * 55)

    print(f"Total Images              : {total_images}")
    print(f"Images Kept               : {len(keep_images)}")
    print(f"Images Marked for Cleanup : {len(delete_images)}")

    print("\nImages Kept:")
    for image in keep_images:
        print(f"  - {image}")

    print("\nImages Marked for Cleanup:")
    for image in delete_images:
        print(f"  - {image}")

    log.write("\nSUMMARY\n")
    log.write("=" * 60 + "\n")
    log.write(f"Total Images              : {total_images}\n")
    log.write(f"Images Kept               : {len(keep_images)}\n")
    log.write(f"Images Marked for Cleanup : {len(delete_images)}\n\n")

    log.write("Images Kept\n")
    for image in keep_images:
        log.write(f"- {image}\n")

    log.write("\nImages Marked for Cleanup\n")
    for image in delete_images:
        log.write(f"- {image}\n")

# ==========================================
# Dry Run Completed
# ==========================================

print("\n" + "=" * 55)
print("DRY RUN COMPLETED SUCCESSFULLY")
print("=" * 55)
print("Cleanup analysis completed.")
print("Cleanup report saved as 'cleanup.log'.")
print("No Docker images were deleted.")
print("This project only identifies images that match the cleanup policy.")

# ==========================================
# Exit
# ==========================================

exit(0)
