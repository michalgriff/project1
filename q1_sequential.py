import time


def download_file(name):
    """Simulates downloading one file."""
    print(f"Starting download of {name}")

    # Simulate a download taking 2 seconds
    time.sleep(2)

    print(f"Finished downloading {name}")


if __name__ == "__main__":
    # Start the timer
    start_time = time.perf_counter()

    # Download each file one at a time
    download_file("File 1")
    download_file("File 2")
    download_file("File 3")
    download_file("File 4")
    download_file("File 5")

    # Stop the timer
    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
