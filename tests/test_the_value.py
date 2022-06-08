import pytest
from src.checking.the_value import ValueList


def mod_value(input_value: int):
    print(f"Input: {input_value}")
    print("Modifying ...")
    if input_value > 999:
        return 999
    else:
        return -1000


@pytest.mark.parametrize("test_input,expected",
                         [(1, -1000),
                          (10, -1000),
                          (12345, 999)])
def test_multi_input(test_input, expected):
    assert mod_value(test_input) == int(expected)


def test_something():
    print("test")


def test_enum1():
    a = ValueList()
    a_value = a.Blue
    print(f"Value: {a_value}")
    assert mod_value(a_value) == -1000


def test_enum2():
    a = ValueList()
    a_value = a.Yellow
    print(f"Value: {a_value}")
    assert mod_value(a_value) == 999


def test_print(capture_stdout):
    print("hello")

    assert capture_stdout["stdout"] == "hello\n"
