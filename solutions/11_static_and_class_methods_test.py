from uuid import UUID, uuid4


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_first_and_last_names(cls, first, last):
        return cls(" ".join([first, last]))

    @classmethod
    def from_comma_separated_names(cls, names):
        last, first = names.split(", ")
        return cls.from_first_and_last_names(first, last)

    @staticmethod
    def generate_id():
        return uuid4()


def test_we_are_not_changing_the_default_constructor():
    assert Person("me").name == "me"


def test_add_an_alternate_constructor():
    """
    We can add a class method that calls the normal constructor properly.

    https://docs.python.org/3.9/library/functions.html#classmethod
    """
    person = Person.from_first_and_last_names(first="Lennart", last="Fridén")
    assert person.name == "Lennart Fridén"


def test_add_another_one():
    person = Person.from_comma_separated_names("Fridén, Lennart")
    assert person.name == "Lennart Fridén"


def test_generate_a_uuid():
    """
    Doubtful why this is even in the Person class, but hey, let's give it a go!

    We have no need for the class nor an instance so we can use a static method here.

    https://docs.python.org/3.9/library/functions.html#staticmethod
    https://docs.python.org/3.9/library/uuid.html#uuid.uuid4
    """
    generated_id = Person.generate_id()
    assert isinstance(generated_id, UUID)
    assert generated_id.version == 4
