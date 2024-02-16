import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Scheduler")
    if "CANVAS_API_TOKEN" in os.environ:
        print("CANVAS_API_TOKEN found")
    else:
        print("CANVAS_API_TOKEN not found")


if __name__ == "__main__":
    main()
