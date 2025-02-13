import pytest

MY_NAME = "Lennart"


class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        """
        This is the constructor.
        It initalizes the instance by setting attributes etc.

        https://docs.python.org/3.9/reference/datamodel.html#object.__init__
        """
        self.name = name

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


@pytest.fixture
def me():
    """
    If passed as an argument to a test function, the result of this function will be available
    as a local variable with the same name within the test function.

    https://docs.pytest.org/en/stable/explanation/fixtures.html
    """
    return Human(MY_NAME)


def test_refactoring_the_tests(me):
    """
    We can use a fixture to clean up and deduplicate our tests.
    Use the above fixture (me) by passing it as an argument to all the other test functions.
    Remove the local variable (me) from each of the tests.

    Do this one test at a time, but before you run the first test, make this test pass!
    Notice that all tests pass? This is when we change them one at a time.
    """
    assert me.name == MY_NAME


def test_naming_a_human(me):
    assert me.name == MY_NAME


def test_turning_a_human_into_a_string(me):
    assert str(me) == "A human named 'Lennart'"
    assert "Look: A human named 'Lennart'!"


def test_object_representation(me):
    assert repr(me) == "Human('Lennart')"


def test_class_attributes(me):
    """
    Class attributes are accessible from its instances.
    """
    assert me.species == "Homo sapiens"
    assert Human.species == "Homo sapiens"


def test_mutable_class_attributes(me):
    """
    Changing a class attribute changes it for all instances.

    NB: Shared, mutable data is a prime source of bugs. Avoid it in real life!
    """
    assert me.species == "Homo sapiens"
    Human.species = "Homo programmatis"

    assert me.species == "Homo programmatis"
    assert Human("Someone Else").species == "Homo programmatis"


def test_shadowing_a_class_attribute_with_an_instance_attribute(me):
    """
    What happens if we set the species for a single human rathar than for all humans?

    Why? The previous test mutated the Human class!
    """
    me.species = "Homo discipulus"

    assert Human.species == "Homo programmatis"
    assert me.species == "Homo discipulus"
