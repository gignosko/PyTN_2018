def fibonacci(n):

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

def test_fib():
    res = fibonacci(4)
    assert res == [1, 1, 2, 3, 5]


# from hypothesis import given, settings
# from hypothesis import strategies as st

# @given(st.integers(min_value=0, max_value=10))
# @settings(max_examples=5)
# def test_fibonacci(s):
    # res = fibonacci(s)
    # for i in range(len(res) - 2):
        # assert res[i] + res[i + 1] == res[i + 2]
