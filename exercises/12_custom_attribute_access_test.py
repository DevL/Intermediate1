import pytest


class DynamicAttributes:
    """
    This class (once finished) simulates an object that can have any attributes set, fetched, and deleted.

    https://docs.python.org/3.9/reference/datamodel.html#customizing-attribute-access
    """

    def __init__(self):
        self._attributes = {}

    def __setattr__(self, name, value):
        """
        To allow the constructor to do its thing, we handle setting _attributes normally.
        """
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            raise NotImplementedError


@pytest.fixture
def data():
    return DynamicAttributes()


def test_getting_a_non_existant_attribute(data):
    """
    We can do this by implementing __getattr__.
    Fetching a non-existant attribute should not result in an error.

    https://docs.python.org/3.9/reference/datamodel.html#object.__getattr__
    """
    assert data.missing is None


def test_setting_a_non_existant_attribute(data):
    """
    We can do this by implementing __setattr__.
    A partial implementation is already in place. Complete it.

    https://docs.python.org/3.9/reference/datamodel.html#object.__setattr__
    """
    assert data.found is None
    data.found = "Found it!"
    assert data.found == "Found it!"


def test_deleting_a_dynamic_attribute(data):
    """
    We can do this by implementing __delattr__.

    https://docs.python.org/3.9/reference/datamodel.html#object.__delattr__
    """
    data.was_here = "It was!"
    del data.was_here
    assert data.was_here is None


def test_deleting_a_non_existant_attribute(data):
    del data.never_was_here
    assert data.never_was_here is None


def test_deleting_a_non_existant_attribute_is_idempotent(data):
    data.was_here = "It was!"
    del data.was_here
    del data.was_here
    assert data.was_here is None


def test_listing_dynamic_attributes(data):
    """
    We can customize what attributes are listed by implementing the __dir__ method.

    https://docs.python.org/3.9/reference/datamodel.html#object.__dir__
    """
    data.a = 1
    data.b = 2
    data.c = 3
    assert "a" in dir(data)
    assert "b" in dir(data)
    assert "c" in dir(data)

    del data.b
    assert not "b" in dir(data)


def test_listing_the_normal_attributes_also(data):
    """
    We don't want to hide the normal attributes though. Make sure that they're included.
    You might have to call the inherited implementation of __dir__ using super().
    """
    assert "_attributes" in dir(data)
    assert "__class__" in dir(data)
    assert "__dict__" in dir(data)
    assert "__setattr__" in dir(data)
