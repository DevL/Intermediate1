import pytest


class Person:
    NO_NAME = "nameless"

    def __init__(self, name=None):
        """
        We no longer need to set self._name here as the setter does it.
        """
        self.name = name

    @property
    def name(self):
        return f"I am {self._name}."

    @name.setter
    def name(self, new_name):
        if new_name is None:
            del self.name
        else:
            self._name = new_name.upper()

    @name.deleter
    def name(self):
        self._name = self.NO_NAME


@pytest.fixture
def person():
    return Person()


def test_getting_a_property(person):
    """
    Instead of getting and setting an attribute directly, we can use properties to customize things.
    Without changing the NO_NAME class attribute, create a property for name that uses the underlying
    attribute _name.

    https://docs.python.org/3.9/library/functions.html#property
    """
    assert person.name == "I am nameless."


def test_setting_a_property(person):
    """
    A setter can customize, validate, or make inputs consistent.
    """
    person.name = "Some One"
    assert person.name == "I am SOME ONE."


def test_setting_the_name_to_None_gives_us_a_default_name(person):
    person.name = None
    assert person.name == "I am nameless."


def test_deleting_a_property(person):
    """
    Once implemented, can you reuse the deleter?
    """
    del person.name
    assert person.name == "I am nameless."


def test_using_a_setter_from_init():
    """
    When and where do you need to explicitly set self._name now?
    """
    person = Person("Some One")
    assert person.name == "I am SOME ONE."
