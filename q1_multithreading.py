import threading
import time


def download_file(name):
    """The function each thread will run."""
    print(f"Starting download of {name}")

    # Simulate a download taking 2 seconds
    time.sleep(2)

    print(f"Finished downloading {name}")


if __name__ == "__main__":
    # Start the timer
    start_time = time.perf_counter()

    # Create five threads
    thread1 = threading.Thread(target=download_file, args=("File 1",))
    thread2 = threading.Thread(target=download_file, args=("File 2",))
    thread3 = threading.Thread(target=download_file, args=("File 3",))
    thread4 = threading.Thread(target=download_file, args=("File 4",))
    thread5 = threading.Thread(target=download_file, args=("File 5",))

    # Start five threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Wait for five threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    # Stop the timer
    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
