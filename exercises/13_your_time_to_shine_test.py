"""
Up until now you've been given tests to run, understand, and change.
But now it's time to write your own!

Using this file, explore one or more of the concepts listed below.

* __dict__ vs __slots__
    https://docs.python.org/3.9/library/stdtypes.html#object.__dict__
    https://docs.python.org/3.9/reference/datamodel.html#slots

* turning an object into a context manager (supporting "with") 
    https://docs.python.org/3.9/reference/datamodel.html#context-managers

* supporting more comparisons than "equality" (__eq__) and "less than" (__lt__)
    https://docs.python.org/3.9/reference/expressions.html#value-comparisons
    https://docs.python.org/3.9/library/functools.html#functools.total_ordering

* Anything in the standard libraries "itertools" and "functools"
    https://docs.python.org/3.9/library/functools.html
    https://docs.python.org/3.9/library/itertools.html

    
1. Pick a concept to explore.
2. Figure out an aspect of the concept you want to test.
3. Write a test for the concept as if you already had the implementation.
4. Run the test, study the o
utput carefully, and fix one thing at a time.
    a. This very likely involves creating a class of some sort in this file next to the test.
    b. This might take a few testruns and fixes before the test is passing.
5. Go back to 2, or 1 if you feel that you've explored all aspects of the concept.

For example, if I would want to explore how __slots__ behave, I might

* create a test for a yet-to-exist class that is defined using __slots__
    * I might expect being able to create an instance of this class, and expect it not to have a __dict__ attribute.
* Running the tests reveal that I need to create the class.
* Running the tests again will reveal that I need to define the class using __slots__ as we clearly have a __dict__ in normal objects.
    
* Once this test passes, I add another one.
    * I might expect being able to create an instance of this class, assign a value to a slot, and access the slot to get the value.
    * Or I might expect some form of error to be raised if I access a slot that doesn't exist.
"""


def test_what_you_like():
    actual = "using the implementation I wish I had"
    expected = "what I want the result to be"
    assert actual == expected
