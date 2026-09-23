import time


def download_file(name):
    print(f"Starting download of {name}")

    time.sleep(2)

    print(f"Finished downloading {name}")


if __name__ == "__main__":
    start_time = time.perf_counter()

    download_file("File 1")
    download_file("File 2")
    download_file("File 3")
    download_file("File 4")
    download_file("File 5")

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
