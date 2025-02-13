import pytest


class Human:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __lt__(self, other):
        return self.name < other.name


class Horse:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __lt__(self, other):
        return self.name < other.name


@pytest.fixture
def me():
    return Human("me")


@pytest.fixture
def you():
    return Human("you")


@pytest.fixture
def my_horse():
    return Horse("Amadeus")


def test_humans_with_the_same_name_are_the_same_person(me):
    """
    Yes, we'll address this in a later exercise.
    """
    assert me == Human("me")


def test_horses_with_the_same_name_are_the_same_horse(my_horse):
    """
    As above.
    """
    assert my_horse == Horse("Amadeus")


def test_humans_and_horses_are_not_the_same():
    """
    Maybe we shouldn't only rely on the name being equal when comparing two objects.

    We could also check if the objects are of the same type.
    https://docs.python.org/3.9/library/functions.html#isinstance
    """
    assert Human("Amadeus") != Horse("Amadeus")


def test_but_we_should_still_be_able_to_sort_humans_and_horses(me, you, my_horse):
    assert my_horse < me < you
    assert sorted([you, my_horse, me]) == [my_horse, me, you]
