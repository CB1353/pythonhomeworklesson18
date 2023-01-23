import numbers


def validate_numeric(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, numbers.Number):
            raise ValueError("Result must be numeric")
        return result
    return wrapper


def add(a, b):
    return a + b


print(add(1, 2))
print(add("a", "b"))
