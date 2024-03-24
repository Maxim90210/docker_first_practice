import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <number_of_seconds>")
        sys.exit(1)

    try:
        seconds = int(sys.argv[1])
    except ValueError:
        print("Invalid number of seconds. Please provide an integer.")
        sys.exit(1)

    for i in range(seconds):
        print(f"Time elapsed: {i + 1} seconds")
        time.sleep(1)
