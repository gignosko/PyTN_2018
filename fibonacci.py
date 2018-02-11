from hypothesis import given, settings
from hypothesis import strategies as st

def fibonacci(n):
    """
    Creates a list of n Fibonacci numbers
    """
    next = 1
    current = 0
    fib = 0
    sequence = []
    for ctr in range(0, n + 1):
        fib = next + current
        sequence.append(fib)
        next = current
        current = fib
    return sequence

@given(st.integers(max_value=10))
@settings(max_examples=5)
def test_fibonacci(s):
    """
    Tests the property that a Fibonacci is the sum of the previou two numbers
    """
    res = fibonacci(s)
    for i in range(len(res) - 2):
        assert res[i] + res[i + 1] == res[i + 2]
