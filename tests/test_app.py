from app import index
from app import sub
from app import mul
from app import power
from app import exp

def test_index():
    assert index() == "The sum is : " + '5'
def test_sub():
    assert sub() == "The difference is : " + '-1'
def test_mul():
    assert mul() == "The product is : " + '6'
def test_power():
    assert power() == "The power is : " + '8'
def test_exp():
    assert exp() == "The expression is : " + '14'

#from app import index


#def test_index():
#    assert index() != "Hello world!"

