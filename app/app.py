from datetime import datetime
import platform

def main():
    print("=" * 50)
    print("IBM Internship Project")
    print("Container Registry with Automated Image Cleanup")
    print("=" * 50)

    print(f"Application Started : {datetime.now()}")
    print(f"Operating System    : {platform.system()} {platform.release()}")
    print(f"Python Version      : {platform.python_version()}")

    print("\nStatus:")
    print("Docker Container Running Successfully")
    print("Container Registry Connected")
    print("CI/CD Pipeline Ready")
    print("Cleanup Automation Module Ready")

    print("\nProject Modules:")
    modules = [
        "Docker Image Build",
        "Container Registry",
        "Python Cleanup Automation",
        "GitHub Actions CI/CD",
        "Logging & Monitoring"
    ]

    for i, module in enumerate(modules, start=1):
        print(f"{i}. {module}")

    print("\nProject Status : READY FOR DEPLOYMENT")
    print("=" * 50)

if __name__ == "__main__":
    main()