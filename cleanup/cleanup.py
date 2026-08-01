import os
import requests
from datetime import datetime

# ==========================================
# Configuration
# ==========================================

USERNAME = os.getenv("DOCKER_USERNAME")
PASSWORD = os.getenv("DOCKER_PASSWORD")
REPOSITORY = "container-registry-cleanup"

KEEP_LAST = 3

LOGIN_URL = "https://hub.docker.com/v2/users/login/"
BASE_URL = f"https://hub.docker.com/v2/repositories/{USERNAME}/{REPOSITORY}/tags/"

# ==========================================
# Login
# ==========================================

print("Authenticating...")

login = requests.post(
    LOGIN_URL,
    json={
        "username": USERNAME,
        "password": PASSWORD
    },
    timeout=20
)

if login.status_code != 200:
    print("Authentication Failed")
    print(login.text)
    exit(1)

token = login.json()["token"]

headers = {
    "Authorization": f"JWT {token}"
}

print("Authentication Successful\n")

# ==========================================
# Fetch ALL Tags
# ==========================================

tags = []
url = BASE_URL + "?page_size=100"

while url:

    response = requests.get(url, headers=headers, timeout=20)

    if response.status_code != 200:
        print("Unable to fetch tags")
        print(response.text)
        exit(1)

    data = response.json()

    tags.extend(data["results"])

    url = data["next"]

if len(tags) == 0:
    print("Repository has no tags.")
    exit(0)

# ==========================================
# Sort Latest First
# ==========================================

tags.sort(
    key=lambda x: datetime.fromisoformat(
        x["last_updated"].replace("Z", "+00:00")
    ),
    reverse=True
)

keep_tags = tags[:KEEP_LAST]
delete_tags = tags[KEEP_LAST:]

# ==========================================
# Logging
# ==========================================

with open("cleanup.log", "w") as log:

    log.write("DOCKER HUB CLEANUP REPORT\n")
    log.write("=" * 60 + "\n\n")

    log.write(f"Repository : {REPOSITORY}\n")
    log.write(f"Generated  : {datetime.now()}\n\n")

    log.write(f"Keeping latest {KEEP_LAST} tags\n\n")

    for tag in keep_tags:
        log.write(f"KEEP : {tag['name']}\n")

    log.write("\n")

    # ==========================================
    # Delete Older Tags
    # ==========================================

    deleted = 0

    for tag in delete_tags:

        tag_name = tag["name"]

        delete_url = BASE_URL + tag_name + "/"

        print(f"Deleting {tag_name}...")

        r = requests.delete(delete_url, headers=headers, timeout=20)

        if r.status_code in (202, 204):

            print(f"Deleted {tag_name}")

            log.write(f"DELETED : {tag_name}\n")

            deleted += 1

        else:

            print(f"Failed : {tag_name}")

            print(r.text)

            log.write(f"FAILED : {tag_name}\n")

    log.write("\n")
    log.write("=" * 60 + "\n")
    log.write(f"Total Tags : {len(tags)}\n")
    log.write(f"Kept       : {len(keep_tags)}\n")
    log.write(f"Deleted    : {deleted}\n")

print("\n======================================")
print("Cleanup Completed")
print("======================================")

print(f"Total Tags : {len(tags)}")
print(f"Kept       : {len(keep_tags)}")
print(f"Deleted    : {len(delete_tags)}")

print("\nLatest Tags:")

for tag in keep_tags:
    print(" -", tag["name"])

print("\ncleanup.log generated successfully.")
