from collections.abc import Hashable
import pytest


class Animal:
    def __init__(self, name, id_number=None):
        self.name = name
        self.id_number = id_number or id(self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id_number == other.id_number

    def __lt__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        return self.name < other.name

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.name)}, {repr(self.id_number)})"

    def __hash__(self):
        return hash((self.species, self.id_number))


class Human(Animal):
    species = "Homo sapiens"


class Horse(Animal):
    species = "Equus ferus caballus"


def test_animals_can_be_given_id_numbers():
    assert Human("me", 123).id_number == 123


def test_animals_by_default_get_their_object_id_as_the_id_number():
    """
    Any guaranteed unique id will do. It just happens to be convenient to use id here.

    https://docs.python.org/3.9/library/functions.html#id
    """
    my_horse = Horse("Amadeus")
    assert my_horse.id_number == id(my_horse)


def test_we_now_base_equality_on_the_id_number_instead_of_the_name():
    assert Human("me", 123) == Human("me", 123)
    assert Human("me", 123) != Human("me", 456)
    assert Human("me", 123) == Human("Also me", 123)


def test_calculating_the_hash_of_an_object():
    """
    The hash value of an object is used in place of the __eq__ method in some situations.
    For example, in order to use an object as the key in a dict, it must be hashable.

    In order to make an object hashable, implement the __hash__ method.

    https://docs.python.org/3.9/reference/datamodel.html#object.__hash__

    In our case, we base the implementation on the species and the id_number, ignoring the name.
    """
    me = Human("me", 123)
    assert isinstance(me, Hashable)

    also_me = Human("Also me", 123)
    assert hash(me) == hash(also_me)

    my_horse = Horse("Amadeus", 123)
    assert isinstance(my_horse, Hashable)
    assert hash(me) != hash(my_horse)


def test_we_should_be_able_to_use_animals_as_keys_in_dicts():
    """
    Normal strings work as dict keys because they're hashable.
    We can make our custom objects usable as dict keys too!
    """
    me = Human("me", 123)
    my_horse = Horse("Amadeus", 123)

    legs = {me: 2, my_horse: 4}

    assert legs[me] == 2
    assert legs[my_horse] == 4

    also_me = Human("me, but incognito", 123)

    assert legs[also_me] == 2

    with pytest.raises(LookupError):
        legs[Human("me")]
