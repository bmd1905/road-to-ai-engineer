import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
# This decorator registers a middleware function that will be executed
# for every incoming HTTP request.
async def add_process_time_header(request: Request, call_next):
    # Record the start time of the request processing
    start_time = time.perf_counter()
    # Call the next middleware or route handler in the chain
    response = await call_next(request)
    # Calculate the time taken to process the request
    process_time = time.perf_counter() - start_time
    # Add a custom header to the response containing the process time
    response.headers["X-Process-Time"] = str(process_time)
    # Return the modified response
    return response
