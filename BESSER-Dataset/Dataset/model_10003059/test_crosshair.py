from python_code import Food

def test_Food___init__():
    assert Food.__init__(Food(0, '\x00'), 0, '\x00') == None

