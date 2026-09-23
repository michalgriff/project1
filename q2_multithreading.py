import threading
import time

def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number * number

    return total


def worker(n):
    calculate_sum(n)


if __name__ == "__main__":
    N = 8_765_324

    start_time = time.perf_counter()

    threads = []

    for i in range(10):
        thread = threading.Thread(target=worker, args=(N,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
