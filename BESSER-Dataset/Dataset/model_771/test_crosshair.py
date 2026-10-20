from python_code import UML2WithID_Classifier

def test_UML2WithID_Classifier___init__():
    assert UML2WithID_Classifier.__init__(UML2WithID_Classifier(True), False) == None


from python_code import UML2WithID_Element

def test_UML2WithID_Element___init__():
    assert UML2WithID_Element.__init__(UML2WithID_Element(''), '') == None

