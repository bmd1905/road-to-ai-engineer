import threading
import time


def fetch_data():
    print(f"Start fetching data on thread: {threading.get_ident()}")
    time.sleep(3)
    print(f"Finished fetching data on thread: {threading.get_ident()}")


def main():
    start_time = time.perf_counter()  # Start the timer

    # Execute tasks sequentially
    for _ in range(2):
        fetch_data()

    end_time = time.perf_counter()  # End the timer
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


# Run the main function
if __name__ == "__main__":
    main()
