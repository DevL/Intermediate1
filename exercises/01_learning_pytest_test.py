import pytest


def test_this_will_fail_and_stop_the_test_run():
    """
    You will need to change this test so that the assertion becomes true.
    """
    assert 1 == 2


def test_this_always_passes_but_not_until_the_above_has_been_fixed():
    """
    Once you've fixed the above test, this one will pass and the next one will fail.
    """
    assert True


def test_actual_and_expected():
    """
    The left side on an assertion is what we actually got, the right side what we expect.
    Manage our expectiations here to continue.
    """
    data = ["a", "c", "b"]
    actual = sorted(data)
    expected = []
    assert actual == expected


# @pytest.mark.skip(reason="test can be marked to be skipped")
def test_this_also_needs_to_be_fixed():
    """
    Before you fix this test, remove the @pytest.mark.skip line above, and run the tests.
    Notice how this test now is included in the test run? Now fix it to continue.
    """
    assert (
        2 + 2 == 5
    )  # Bonus question: why is this interpreted as (2 + 2) == 5 and not 2 + (2 == 5)?


@pytest.mark.xfail(reason="we expect this test to always fail")
def test_expected_failing_test():
    """
    When we know that a test is expected to fail, we can mark it as such.
    This is rarely used, but can come in handy when e.g. sketching a series of tests,
    perhaps based on data or knowledge we don't have yet.

    However, we should not let these kinds of tests remain for long in our code base.
    Either fix it or remove it!
    """
    assert 1 > 2
