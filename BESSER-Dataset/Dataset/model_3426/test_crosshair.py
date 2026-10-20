from python_code import mongoQuery_FieldSelection
from python_code import mongoQuery_Selection

def test_mongoQuery_FieldSelection___init__():
    assert mongoQuery_FieldSelection.__init__(mongoQuery_FieldSelection('', 0, mongoQuery_FieldSelection=mongoQuery_Selection()), '', 0, mongoQuery_FieldSelection=mongoQuery_Selection()) == None

