import pytest 
from lib.high_value import *

"Make sure it initilises correctly"
"Check that it recognises value first is higher"
"Check that it recognises value second is higher"
"Check that it recognises that the values are equal"

def test_first_value_higher():
    hv = HighValue(3, 1)
    assert hv.get_highest() == "First value is higher"
    
def test_second_value_higher():
    hv = HighValue(1, 3)
    assert hv.get_highest() == "Second value is higher"

def test_initialises_correctly():
    hv = HighValue(0, 1)
    assert hv.value_first == 0
    assert hv.value_second == 1 

def test_first_functions_correctly():
    hv = HighValue(1, 2)
    hv.add(2, "first")
    assert hv.value_first == 3
    

def test_second_functions_correctly():
    hv = HighValue(1, 2)
    hv.add(3, "second")
    assert hv.value_second == 5
