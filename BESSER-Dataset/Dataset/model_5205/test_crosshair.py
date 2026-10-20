from python_code import Original_Metamodel_A
from python_code import Original_Metamodel_B

def test_Original_Metamodel_B___init__():
    assert Original_Metamodel_B.__init__(Original_Metamodel_B('', Original_Metamodel_B=Original_Metamodel_A()), '', Original_Metamodel_B=Original_Metamodel_A()) == None


from python_code import Original_Metamodel_C

def test_Original_Metamodel_C___init__():
    assert Original_Metamodel_C.__init__(Original_Metamodel_C(''), '') == None

