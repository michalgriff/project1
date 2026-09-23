import threading
import time


def download_file(name):
    print(f"Starting download of {name}")
    
    time.sleep(2)

    print(f"Finished downloading {name}")

if __name__ == "__main__":
    start_time = time.perf_counter()

    thread1 = threading.Thread(target=download_file, args=("File 1",))
    thread2 = threading.Thread(target=download_file, args=("File 2",))
    thread3 = threading.Thread(target=download_file, args=("File 3",))
    thread4 = threading.Thread(target=download_file, args=("File 4",))
    thread5 = threading.Thread(target=download_file, args=("File 5",))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
