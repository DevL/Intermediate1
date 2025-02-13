import pytest

MY_NAME = "Replace this with your name"


class Human:
    species = "Homo sapiens"  # this is a class attribute

    def __init__(self, name):
        """
        This is the constructor.
        It initalizes the instance by setting attributes etc.

        https://docs.python.org/3.9/reference/datamodel.html#object.__init__
        """
        self.name = name  # this is an instance attribute

    def __str__(self):
        """
        This is used whenever the object is turned into a string.

        https://docs.python.org/3.9/reference/datamodel.html#object.__str__
        """
        return f"A human named '{self.name}'"

    def __repr__(self):
        """
        This is the "object representation". Ideally, you should be able to
        create a copy of the object by pasting the output into a REPL.

        https://docs.python.org/3.9/reference/datamodel.html#object.__repr__
        """
        return f"{self.__class__.__name__}({repr(self.name)})"


def test_naming_a_human():
    me = Human(MY_NAME)
    assert me.name == ...


def test_turning_a_human_into_a_string():
    me = Human(MY_NAME)
    assert str(me) == ...
    assert f"Look: {me}!" == ...


def test_object_representation():
    me = Human(MY_NAME)
    assert repr(me) == ...


def test_class_attributes():
    """
    Class attributes are accessible from its instances.
    """
    me = Human(MY_NAME)
    assert me.species == ...
    assert Human.species == ...


def test_mutable_class_attributes():
    """
    Changing a class attribute changes it for all instances.

    NB: Shared, mutable data is a prime source of bugs. Avoid it in real life!
    """
    me = Human(MY_NAME)
    assert me.species == ...

    Human.species = "Homo programmatis"

    assert me.species == ...
    assert Human("Someone Else").species == ...


def test_shadowing_a_class_attribute_with_an_instance_attribute():
    """
    What happens if we set the species for a single human rathar than for all humans?

    Why?
    """
    me = Human(MY_NAME)
    me.species = "Homo discipulus"

    assert Human.species == ...
    assert me.species == ...
