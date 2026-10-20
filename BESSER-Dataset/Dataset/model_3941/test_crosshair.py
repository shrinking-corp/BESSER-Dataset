from python_code import UmlMM_DataType

def test_UmlMM_DataType___init__():
    assert UmlMM_DataType.__init__(UmlMM_DataType(''), '') == None


from python_code import UmlMM_Classifier
from python_code import UmlMM_UmlPackage

def test_UmlMM_UmlPackage___init__():
    assert UmlMM_UmlPackage.__init__(UmlMM_UmlPackage('', _UmlPackage=set(), UmlPackage=UmlMM_Classifier()), '', _UmlPackage=set(), UmlPackage=UmlMM_Classifier()) == None

