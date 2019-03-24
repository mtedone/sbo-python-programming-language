from functools import wraps


def logged(func):
    # Idea: Give me a function, I'll put logging around it

    # Used not to lose the wrapped function name and docs, including help
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Callling', func.__name__)
        return func(*args, **kwargs)

    return wrapper
