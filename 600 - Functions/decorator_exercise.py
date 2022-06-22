from functools import wraps


# multiply result of function by 2
def duplicate_result_deco(f):
    @wraps(f)
    def inner_func(*args, **kwargs):
        return f(*args, **kwargs) * 2

    return inner_func


def multiply_result_deco(n):
    def multiply(f):
        @wraps(f)
        def inner_func(*args, **kwargs):
            return f(*args, **kwargs) * n

        return inner_func

    return multiply

#if implemented as class could be easier to read
class multiply_result_deco2:
    def __init__(self,n):
        self.n = n

    def __call__(self, function):
        return function * self.n


@duplicate_result_deco
def duplicated_square(x):
    return x ** 2


# @multiply_result_deco(2)
def multiply2_square(x):
    return x ** 2

multiply2_square = multiply_result_deco(2)(multiply2_square)  # alternative invocation


@multiply_result_deco(3)
def multiply3_square(x):
    return x ** 2


class CustomException(Exception):
    pass


def retry_n_times(n):
    """Decorator catches `CustomException` nad retries running function ntimes
    every time it displays `attempt=<attempt_no>.
    After n times it rerises exception."""
    def retry(f):
        @wraps(f)
        def inner_func(*args, **kwargs):
            for attempt in range(n):
                try:
                    return f(*args, **kwargs)
                except CustomException:
                    print(f"attempt no {attempt}")
            raise CustomException

        return inner_func

    return retry


@retry_n_times(3)
def raise_custom_exc():
    raise CustomException()


if __name__ == '__main__':
    assert duplicated_square(3) == 18
    assert duplicated_square.__name__ == 'duplicated_square'
    assert multiply2_square(3) == duplicated_square(3)
    assert multiply2_square.__name__ == 'multiply2_square'
    assert multiply3_square(3) == 27
    assert multiply3_square.__name__ == 'multiply3_square'

    raise_custom_exc()
