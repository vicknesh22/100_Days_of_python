import time


def delay_decorator(function):
    time.sleep(3)
    # any thing before the function
    function()
    function()
    # any thing after this function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def bye():
    print('bye')
