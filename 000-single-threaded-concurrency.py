import asyncio
import threading
import time


async def fetch_data():
    print(f"Start fetching data on thread: {threading.get_ident()}")
    await asyncio.sleep(3)
    print(f"Finished fetching data on thread: {threading.get_ident()}")


async def main():
    start_time = time.perf_counter()  # Start the timer

    # Create a list of tasks
    tasks = [fetch_data() for _ in range(2)]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()  # End the timer
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


# Run the main function
asyncio.run(main())
