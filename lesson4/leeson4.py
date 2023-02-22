"""
Common weak spots.
description:
1. Tool receives input from user -> !weakspot -> stop execution.
2. Tool gets the data from DB based on the user input -> !weakspot -> not exists,
                                                          table locked -> timeout,
                                                          no open connections... -> stop exec
3. Tool calculates data based on the data from db -> ok
4. Tool writes the new data to db -> !writing errors -> stop execution
5. Tool send success api call to 3rd party tool. -> API is not respond,
                                                    Unauthorized, timeout... -> stop execution
"""
from lesson4.custom_exc import MyAwesomeException


def divider(a_, b_):
    if a_ == 15:
        raise MyAwesomeException("Not lucky day.")
    return a_/b_


def main():
    while 1:
        print('a', end='\r')
        print('A', end='\r')
        break

# try:
#     pass
# except Exception as err:
#     pass


if __name__ == '__main__':
    while 1:
        try:
            a = int(input('enter a:'), 10)
            b = int(input('enter b:'), 10)
            print(divider(a, b))
        except (ValueError, TypeError):
            print("You've entered incorrect values }:-|")
        except ZeroDivisionError as exc:
            print(exc)
            print("You can't divide by zero.")
        except MyAwesomeException as exc:
            print("I don't know how it happened.")
        except Exception:
            pass
        else:
            print("No error. Everything is ok. Well done!")
        finally:
            print("Code will be executed in any case.")
