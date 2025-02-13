import pytest


class Human:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """
        This method is used to test equality with another object as in x == y.

        This particular implementation reimplements the behaviour for any class inheriting from "object".
        It does so by delegating the call to its ancestor, which happens to be "object".

        https://docs.python.org/3.9/reference/datamodel.html#object.__eq__
        """
        # return super().__eq__(other)
        return True

    def __lt__(self, other):
        """
        This method is used to test whether the object is less than another object as in x < y.

        This particular implementation reimplements the behaviour for any class inheriting from "object".
        It does so by delegating the call to its ancestor, which happens to be "object".

        https://docs.python.org/3.9/reference/datamodel.html#object.__lt__
        """
        # return super().__eq__(other)
        return self.name < other.name


@pytest.fixture
def me():
    return Human("me")


@pytest.fixture
def you():
    return Human("you")


def test_all_humans_are_equal(me, you):
    """
    Out of the box, an object is only equal to itself in Python.
    We can change this behaviour by implementing the `__eq__` method.

    Implement this in the simplest possible way.
    """
    assert me == you


def test_but_we_can_still_order_them_by_name(me, you):
    """
    Out of the box, an object cannot be determined to be less than another.
    We can change this behaviour by implementing the `__lt__` method.

    By doing so, we can make our objects sortable.

    Let's base the implementation on humans' names.
    """
    assert me < you
    assert sorted([you, me]) == [me, you]
