from python_code import myDsl_Import
from python_code import myDsl_Model

def test_myDsl_Import___init__():
    assert myDsl_Import.__init__(myDsl_Import('', myDsl_Import=myDsl_Model()), '', myDsl_Import=myDsl_Model()) == None

