class MagicNumber:
    def __init__(self, offset):
        self._offset = offset

    def __repr__(self):
        return f"{type(self).__name__}({repr(self._offset)})"

    def __call__(self, *numbers):
        return sum(numbers, start=self._offset)


def test_making_an_object_callable():
    """
    An object can behave like a function if it implements __call__.

    https://docs.python.org/3.9/reference/datamodel.html#emulating-callable-objects
    """
    add_one = MagicNumber(1)
    assert callable(add_one)
    assert add_one(2) == 3


def test_making_the_callable_object_accept_multiple_numbers():
    """
    In case you don't recall how to accept a variable amount of parameters, see this.

    https://docs.python.org/3.9/tutorial/controlflow.html#arbitrary-argument-lists
    """
    add_two = MagicNumber(2)
    assert add_two(3, 4) == 9
    assert add_two(3, 4, 5) == 14
    assert add_two(3, 4, 5, 6) == 20
    assert add_two() == 2
