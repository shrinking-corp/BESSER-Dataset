from python_code import data_Variable
from python_code import data_Variables

def test_data_Variable___init__():
    assert data_Variable.__init__(data_Variable('', data_Variable=data_Variables()), '', data_Variable=data_Variables()) == None

