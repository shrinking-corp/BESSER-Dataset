from python_code import RoyalAndLoyal_Container_RandL
from python_code import RoyalAndLoyal_Customer

def test_RoyalAndLoyal_Customer___init__():
    assert RoyalAndLoyal_Customer.__init__(RoyalAndLoyal_Customer('', RoyalAndLoyal_Customer=RoyalAndLoyal_Container_RandL()), '', RoyalAndLoyal_Customer=RoyalAndLoyal_Container_RandL()) == None

def test_RoyalAndLoyal_Customer_updateName():
    assert RoyalAndLoyal_Customer.updateName(RoyalAndLoyal_Customer('', RoyalAndLoyal_Customer=RoyalAndLoyal_Container_RandL()), 0) == None

