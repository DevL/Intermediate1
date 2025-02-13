class QualifiedStatement:
    def __init__(self, statement, is_true=True):
        self.statement = statement
        self.is_true = is_true

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.statement)}, is_true={self.is_true})"

    def __bool__(self):
        """
        If we expect more things to factor into whether this is true or not, we can
        use all instead of adding "and"s.

        https://docs.python.org/3.9/library/functions.html#all
        """
        # return all([self.statement, self.is_true])
        return bool(self.statement) and self.is_true


def test_making_an_object_determine_its_truthiness():
    """
    By default, all custom objects are considered to be truthy. This behaviour can be
    overridden by implementing the __bool__ method.

    https://docs.python.org/3.9/reference/datamodel.html#object.__bool__
    """
    assert QualifiedStatement("Python is fun!")
    assert not QualifiedStatement("Generative AI is real AI!", False)


def test_an_empty_claim_is_always_false():
    """
    Let's make our definition of truth a little more involved, shall we?
    """
    assert not QualifiedStatement("", is_true=True)
    assert not QualifiedStatement(None, is_true=True)
