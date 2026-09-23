import multiprocessing
import time

def download_file(name):
    """The function each child process will run."""
    print(f"Starting download of {name}")

    # Simulate a download that takes 2 seconds
    time.sleep(2)

    print(f"Finished downloading {name}")


if __name__ == "__main__":
    # Start the timer
    start_time = time.perf_counter()

    # Create five processes
    process1 = multiprocessing.Process(target=download_file, args=("File 1",))
    process2 = multiprocessing.Process(target=download_file, args=("File 2",))
    process3 = multiprocessing.Process(target=download_file, args=("File 3",))
    process4 = multiprocessing.Process(target=download_file, args=("File 4",))
    process5 = multiprocessing.Process(target=download_file, args=("File 5",))

    # Start five processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    # Wait for all five processes to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()

    # Stop the timer
    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
