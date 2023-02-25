import datetime
import functools
import random
import traceback
from time import sleep


def log_exceptions(file_name):

    def outer_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                pass
            except Exception as err:
                result = None
                with open(file_name, 'a') as log_file:
                    log_file.write(f"{datetime.datetime.now()}: {func} \n {traceback.format_exc()}")
            return result

        return wrapper

    return outer_wrapper


def check_exec_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before function call
        start = datetime.datetime.now()
        # function call
        result = func(*args, **kwargs)
        # do something after function call
        end = datetime.datetime.now()
        print(f"The function execution took {(end - start).seconds} seconds")
        return result

    return wrapper


@check_exec_time
def time_consuming_function():  # -> wrapper
    sleep(random.randint(1, 10))


@log_exceptions('specific_log_file.txt')
@check_exec_time
def another_time_cons_func(additional_time):
    sleep(random.randint(1, 10) + additional_time)
    raise ValueError


if __name__ == '__main__':
    print(another_time_cons_func)
