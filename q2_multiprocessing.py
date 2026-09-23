import multiprocessing
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

    processes = []

    for i in range(10):
        process = multiprocessing.Process(target=worker, args=(N,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
