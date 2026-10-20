from python_code import MMA_Element
from python_code import Root

def test_MMA_Element___init__():
    assert MMA_Element.__init__(MMA_Element('', children=Root(), sources=set(), targets=set()), '', children=Root(), sources=set(), targets=set()) == None

