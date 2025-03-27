from time import perf_counter, sleep
from random import random
import functools

def timeit(n):  # Accept n as an argument
    """
    Used as a decorator. Executes the deccorated function n times and prints the average execution time.

    Parameters
    ----------
    n: int
        Number of times to execute the function.
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            total_time = 0
            return_value = None
            for i in range(n):
                start = perf_counter()
                return_value = f(*args, **kwargs)
                end = perf_counter()
                total_time += (end - start)
            avg_time = total_time / n
            print(f"@timeit Function {f.__name__}: Average execution time {avg_time:.6f} seconds over {n} iterations.")
            return return_value
        return wrapper
    return decorator

if __name__ == "__main__":

    @timeit(10)
    def example_function():
        # This is where I would do something useful
        sleep(5 * random())

    example_function()
