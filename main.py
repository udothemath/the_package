# from src.the_value import ValueList
from tests.test_the_value import test_something


def hello():
    print("hello")


if __name__ == "__main__":
    import os
    print(os.getcwd())
    hello()
    test_something()
    # a = ValueList()
    # print(a.Blue)
    # # assert a.Blue == 1
    # b = mod_value(a.Yellow)
    # print(b)
