from python_code import Cash

def test_Cash___init__():
    assert Cash.__init__(Cash(0), 0) == None


from python_code import Credit_Card

def test_Credit_Card___init__():
    assert Credit_Card.__init__(Credit_Card(0), 0) == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '', '', order16=set()), '', '', '', order16=set()) == None

