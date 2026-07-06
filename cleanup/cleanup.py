import requests
from datetime import datetime

# Docker Hub Details
docker_user = "ibm1container1cleanup1team"
repository_name = "container-registry-cleanup"

api_endpoint = (
    f"https://hub.docker.com/v2/repositories/"
    f"{docker_user}/{repository_name}/tags/"
)

# Tags that are considered safe to remove
cleanup_tags = {"old", "backup", "test", "debug"}


def fetch_repository_tags():
    """Fetch all tags from the Docker Hub repository."""
    print("Connecting to Docker Hub...\n")

    try:
        response = requests.get(api_endpoint, timeout=10)
    except requests.RequestException as error:
        print(f"Unable to connect: {error}")
        return None

    if response.status_code != 200:
        print(f"Request failed (Status Code: {response.status_code})")
        return None

    print("Connection Successful!\n")
    return response.json()


def analyze_images(image_data):
    """Check which images should be kept or marked for cleanup."""

    keep_list = []
    cleanup_list = []

    with open("cleanup.log", "w", encoding="utf-8") as report:

        report.write("DOCKER HUB CLEANUP REPORT\n")
        report.write("=" * 60 + "\n")
        report.write(f"Repository : {repository_name}\n")
        report.write(f"Generated  : {datetime.now()}\n\n")

        for image in image_data["results"]:

            tag_name = image["name"]
            last_modified = image["last_updated"]

            print(f"Checking Image : {tag_name}")
            print(f"Last Updated   : {last_modified}")

            if tag_name.lower() in cleanup_tags:
                action = "DELETE"
                reason = "Matched cleanup policy"
                cleanup_list.append(tag_name)
            else:
                action = "KEEP"
                reason = "Currently active"
                keep_list.append(tag_name)

            print(f"Decision       : {action}")
            print(f"Reason         : {reason}\n")

            report.write(f"Tag          : {tag_name}\n")
            report.write(f"Updated On   : {last_modified}\n")
            report.write(f"Decision     : {action}\n")
            report.write(f"Reason       : {reason}\n")
            report.write("-" * 60 + "\n")

        report.write("\nSUMMARY\n")
        report.write("=" * 60 + "\n")
        report.write(f"Total Images : {len(image_data['results'])}\n")
        report.write(f"Kept         : {len(keep_list)}\n")
        report.write(f"Marked       : {len(cleanup_list)}\n\n")

        report.write("Images Kept:\n")
        for tag in keep_list:
            report.write(f"• {tag}\n")

        report.write("\nImages Marked For Cleanup:\n")
        for tag in cleanup_list:
            report.write(f"• {tag}\n")

    return keep_list, cleanup_list


def show_summary(total_images, keep_list, cleanup_list):
    """Display the cleanup summary."""

    print("=" * 55)
    print("Docker Hub Cleanup Summary")
    print("=" * 55)

    print(f"Total Images Scanned : {total_images}")
    print(f"Images Kept          : {len(keep_list)}")
    print(f"Marked For Cleanup   : {len(cleanup_list)}")

    print("\nImages to Keep:")
    for tag in keep_list:
        print(f"  - {tag}")

    print("\nImages Marked:")
    for tag in cleanup_list:
        print(f"  - {tag}")

    print("\nLog file created : cleanup.log")
    print("Dry Run Completed Successfully.")
    print("No images were deleted from Docker Hub.")


def main():

    repository_data = fetch_repository_tags()

    if repository_data is None:
        return

    keep_images, cleanup_images = analyze_images(repository_data)

    show_summary(
        len(repository_data["results"]),
        keep_images,
        cleanup_images
    )


if __name__ == "__main__":
    main()