from hypothesis import given, settings
from hypothesis import strategies as st

def make_agg(items):
    """
    Takes a list of tuples that repesent a Result Set and aggregates the totals by id
    """
    res = {}
    for item in items:
        if res.get(item[0]):
            res[item[0]]['total'] = res[item[0]]['total'] + item[2]
        else:
            res[item[0]] = {'name': item[1], 'total': item[2]}
    return res


@given(
        st.lists(
            st.tuples(
                st.integers(min_value = 1), st.text(), st.integers(min_value=1)
                ),
            max_size=10
            )
        )
def test_make_agg(stuff):
    """
    Hypothesis tests for make_agg
    There is a bug in the tests that I'm leaving so you can see what a failure produces
    """
    res = make_agg(stuff)
    assert type(res) is dict
    for thing in stuff:
        assert thing[0] in res
        assert res.get(thing[0]).get('name') == thing[1]

    for k,v in res.items():
        assert type(k) is int
        assert type(v['name']) is str
        assert type(v['total']) is int
