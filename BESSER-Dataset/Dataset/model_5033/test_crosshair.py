from python_code import customers_CanadaAddress

def test_customers_CanadaAddress___init__():
    assert customers_CanadaAddress.__init__(customers_CanadaAddress(''), '') == None


from python_code import customers_CustomersDB

def test_customers_CustomersDB___init__():
    assert customers_CustomersDB.__init__(customers_CustomersDB('', customers_CustomersDB=set()), '', customers_CustomersDB=set()) == None


from python_code import customers_USAddress

def test_customers_USAddress___init__():
    assert customers_USAddress.__init__(customers_USAddress(''), '') == None

