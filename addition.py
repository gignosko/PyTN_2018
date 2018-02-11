from hypothesis import given, settings
from hypothesis import strategies as st


@given(st.integers(), st.integers(), st.integers())
def test_addition(x, y, z):
    """
    Hypothesis tests that check the four properties of addition
    """
    # test commutative
    assert x + y == y + x

    #test associative
    assert x + (y + z) == (x + y) + z

    # test identity
    assert x + 0 == x

    # test distributive
    assert x * (y + z) == x * y + x * z
