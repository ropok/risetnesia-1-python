import pytest
import my_functions as my_functions

@pytest.mark.parametrize("num1, num2, expected",[
    (5,9,14),
    (1000,100,1100),
    (-50,0,-50),
])

def test_add(num1, num2, expected):
    assert my_functions.add(num1, num2) == expected