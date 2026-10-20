from python_code import Products

def test_Products___init__():
    assert Products.__init__(Products(0, warehouse13=set(), customer1=set()), 0, warehouse13=set(), customer1=set()) == None


from python_code import Shopping_Cart

def test_Shopping_Cart___init__():
    assert Shopping_Cart.__init__(Shopping_Cart(0, items16=set(), customer5=set()), 0, items16=set(), customer5=set()) == None


from python_code import Warehouse

def test_Warehouse___init__():
    assert Warehouse.__init__(Warehouse('', products12=set()), '', products12=set()) == None

