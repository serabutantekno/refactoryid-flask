from functools import wraps


def saySomething(func):
    @wraps(func)
    def decorator():
        print("=".center(20, "="))
        print("this is middleware example")
        return func()
    return decorator
