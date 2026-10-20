from python_code import Base

def test_Base___init__():
    assert Base.__init__(Base('\x00\x00', False, pizza1=set()), '', True, pizza1=set()) == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, '', 0, order9=set(), address12=set()), 0, '', 0, order9=set(), address12=set()) == None


from python_code import MealDeal

def test_MealDeal___init__():
    assert MealDeal.__init__(MealDeal('', '', float('inf'), False, sides14=set(), pizza16=set(), order19=set()), '', '', float('inf'), False, sides14=set(), pizza16=set(), order19=set()) == None


from python_code import Toppings

def test_Toppings___init__():
    assert Toppings.__init__(Toppings(False, '\x00', pizza7=set()), False, '', pizza7=set()) == None

