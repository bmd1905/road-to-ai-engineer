import asyncio
import threading
import time


async def fetch_data():
    print(f"Start fetching data on thread: {threading.get_ident()}")
    await asyncio.sleep(3)
    print(f"Finished fetching data on thread: {threading.get_ident()}")


def run_async_in_thread(thread_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_data())
    loop.close()
    print(f"Thread {thread_id} finished")


def main():
    start_time = time.perf_counter()  # Start the timer
    threads = []
    num_threads = 2

    # Create and start threads
    for i in range(num_threads):
        thread = threading.Thread(target=run_async_in_thread, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()  # End the timer
    print(
        f"Total time taken: {end_time - start_time:.2f} seconds"
    )  # Print the total time


if __name__ == "__main__":
    main()
