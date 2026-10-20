from python_code import customerDsl_POBox

def test_customerDsl_POBox___init__():
    assert customerDsl_POBox.__init__(customerDsl_POBox(0), 0) == None


from python_code import customerDsl_CustomerDb
from python_code import customerDsl_Product

def test_customerDsl_Product___init__():
    assert customerDsl_Product.__init__(customerDsl_Product('', 0, customerDsl_Product=customerDsl_CustomerDb()), '', 0, customerDsl_Product=customerDsl_CustomerDb()) == None


from python_code import customerDsl_StreetAddress

def test_customerDsl_StreetAddress___init__():
    assert customerDsl_StreetAddress.__init__(customerDsl_StreetAddress('', '\x00'), '\x00\x00', '') == None

