from typing import Callable, Any
from time import time
from functools import wraps
from sys import __stdout__
from datetime import datetime

def get_execution_time_print(pretty: bool = True):
    """Simple method to output to stdout the execution time for a method. The method will
    output in a reasonable unit of measure

    Args:
        func (Callable): function to be evaluated the time of
    """

    if not isinstance(pretty, bool):
        raise TypeError("pretty must be a boolean")

    def decorator(func: Callable):

        @wraps(func)
        def get_execution_time(*args, **kwargs):
            start = time() if pretty else datetime.now()
            result: Any = func(*args, **kwargs)  # save the result to a name
            compute_time = (time() if pretty else datetime.now()) - start
            if pretty:
                if compute_time < 0.1:
                    print(
                        "Computation time for %s: %.2f ms"
                        % (func.__name__, compute_time * 1000)
                    )
                elif compute_time < 60:
                    print(
                        "Computation time for %s: %.2f s" % (func.__name__, compute_time)
                    )
                elif compute_time / 60 < 60:
                    print(
                        "Computation time for %s: %.1f min"
                        % (func.__name__, (compute_time) / 60)
                    )
                else:
                    print(
                        "Computation time for %s: %.1f h"
                        % (func.__name__, (compute_time) / 3600)
                    )
            else:
                print(
                    "Computation time for %s: %s"
                    % (func.__name__, str(compute_time))
                )
            return result  # return the name

        return get_execution_time

    return decorator
