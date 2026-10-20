from python_code import mongodb_Database

def test_mongodb_Database___init__():
    assert mongodb_Database.__init__(mongodb_Database('', mongodb_Database=set()), '', mongodb_Database=set()) == None


from python_code import mongodb_Value

def test_mongodb_Value___init__():
    assert mongodb_Value.__init__(mongodb_Value('', '\x00'), '\x00\x00', '') == None

