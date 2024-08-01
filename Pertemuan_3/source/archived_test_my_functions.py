import pytest
import my_functions as my_functions

@pytest.mark.parametrize("a, b, expected",[
    (1,2,3),
    (-1,1,0),
    (-1,-1,-2),
])

def test_add(a,b,expected):
    assert my_functions.add(a,b) == expected