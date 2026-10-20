from python_code import Regular_Members

def test_Regular_Members___init__():
    assert Regular_Members.__init__(Regular_Members(0, '\x00'), 0, '\x00') == None


from python_code import Vendor

def test_Vendor___init__():
    assert Vendor.__init__(Vendor(0, '', '', 0, '', Product_Vendor_115=set()), 0, '', '', 0, '', Product_Vendor_115=set()) == None

