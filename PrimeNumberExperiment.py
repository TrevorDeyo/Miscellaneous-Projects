import time
import math

def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

def update_progress(current, total):
    progress = (current / total) * 100
    print(f"\rProgress: [{progress:.0f}%] ", end='', flush=True)

def main():
    start_time = time.time()

    counter = 0
    total_numbers = 10000000

    for i in range(total_numbers):
        if check_prime(i):
            counter += 1

        # Update progress bar every 1% of total numbers
        if i % (total_numbers // 100) == 0:
            update_progress(i, total_numbers)

    print("\nThere are", counter, "prime numbers out of", total_numbers)

    stop_time = time.time()
    duration_ms = (stop_time - start_time) * 1000
    duration_s = stop_time - start_time

    print("Program took: {:.2f} milliseconds".format(duration_ms))
    print("Program took: {:.2f} seconds".format(duration_s))

if __name__ == "__main__":
    main()
