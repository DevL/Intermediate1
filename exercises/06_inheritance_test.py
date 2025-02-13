import pytest


class Animal:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __lt__(self, other):
        return self.name < other.name


class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.name)})"


class Horse:
    species = "Equus ferus caballus"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.name)})"


@pytest.fixture
def me():
    return Human("me")


@pytest.fixture
def you():
    return Human("you")


@pytest.fixture
def my_horse():
    return Horse("Amadeus")


def test_humans_and_horses_are_animals():
    """
    For this to work, we need to let Human and Horse both inherit from Animal.
    Animal is the base class that keeps the shared logic for its subclasses.

    Once you've made this test pass, you should move the methods __init__ and __repr__
    from Human and Horse into Animal. They can inherit them from Animal.
    """
    assert isinstance(Human("me"), Animal)
    assert isinstance(Horse("Amadeus"), Animal)


def test_equality_still_works_as_before(me, my_horse, you):
    assert me == Human("me")
    assert me != you
    assert me != my_horse
    assert my_horse == Horse("Amadeus")
    assert my_horse != Horse("Nemah")
    assert my_horse != you


def test_sorting_works_as_before(me, my_horse, you):
    assert sorted([me, my_horse, you]) == [my_horse, me, you]


def test_how_we_handle_things_without_names(me):
    """
    It doesn't make sense to sort things by name if we don't know for sure that they
    have a name. At that point we should declare the behaviour as not implemented.

    https://docs.python.org/3.9/library/constants.html#NotImplemented
    """
    expected_error_message = "'<' not supported between instances of 'Human' and 'int'"
    with pytest.raises(TypeError, match=expected_error_message):
        assert me < 1
