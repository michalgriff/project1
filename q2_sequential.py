import time

def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number * number

    return total


if __name__ == "__main__":
    N = 8_765_324

    start_time = time.perf_counter()

    for i in range(10):
        calculate_sum(N)

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
