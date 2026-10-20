from python_code import Food
from python_code import Items
from python_code import app

def test_Food___init__():
    assert Food.__init__(Food('', '', 0.0, False, False, items10=Items(), app13=app()), '', '', 0.0, False, True, items10=Items(), app13=app()) == None

