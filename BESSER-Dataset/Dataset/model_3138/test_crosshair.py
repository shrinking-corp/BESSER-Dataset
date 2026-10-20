from python_code import UML_14_Class

def test_UML_14_Class___init__():
    assert UML_14_Class.__init__(UML_14_Class(True), False) == None


from python_code import UML_14_ElementOwnership

def test_UML_14_ElementOwnership___init__():
    assert UML_14_ElementOwnership.__init__(UML_14_ElementOwnership('', False), '', False) == None


from python_code import UML_14_Classifier
from python_code import UML_14_Feature

def test_UML_14_Feature___init__():
    assert UML_14_Feature.__init__(UML_14_Feature('', '\x00', Feature=UML_14_Classifier(), feature=UML_14_Classifier()), '\x00\x00', '', Feature=UML_14_Classifier(), feature=UML_14_Classifier()) == None


from python_code import UML_14_Method

def test_UML_14_Method___init__():
    assert UML_14_Method.__init__(UML_14_Method('', UML_14_Method=set()), '', UML_14_Method=set()) == None


from python_code import UML_14_Multiplicity
from python_code import UML_14_MultiplicityRange

def test_UML_14_MultiplicityRange___init__():
    assert UML_14_MultiplicityRange.__init__(UML_14_MultiplicityRange(0, 0, MultiplicityRange=UML_14_Multiplicity(), range=UML_14_Multiplicity()), 0, 0, MultiplicityRange=UML_14_Multiplicity(), range=UML_14_Multiplicity()) == None


from python_code import UML_14_Classifier
from python_code import UML_14_Multiplicity
from python_code import UML_14_StructuralFeature

def test_UML_14_StructuralFeature___init__():
    assert UML_14_StructuralFeature.__init__(UML_14_StructuralFeature('', '', '\x00\x00', StructuralFeature=UML_14_Classifier(), typedFeature=UML_14_Classifier(), UML_14_StructuralFeature=UML_14_Multiplicity()), '', '', '', StructuralFeature=UML_14_Classifier(), typedFeature=UML_14_Classifier(), UML_14_StructuralFeature=UML_14_Multiplicity()) == None

