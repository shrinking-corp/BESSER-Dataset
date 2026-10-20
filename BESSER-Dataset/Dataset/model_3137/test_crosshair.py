from python_code import UML_14_ElementOwnership

def test_UML_14_ElementOwnership___init__():
    assert UML_14_ElementOwnership.__init__(UML_14_ElementOwnership('', False), '', False) == None


from python_code import UML_14_Method

def test_UML_14_Method___init__():
    assert UML_14_Method.__init__(UML_14_Method('', UML_14_Method=set()), '', UML_14_Method=set()) == None


from python_code import UML_14_Multiplicity
from python_code import UML_14_MultiplicityRange

def test_UML_14_MultiplicityRange___init__():
    assert UML_14_MultiplicityRange.__init__(UML_14_MultiplicityRange(0, 0, MultiplicityRange=UML_14_Multiplicity(), range=UML_14_Multiplicity()), 0, 0, MultiplicityRange=UML_14_Multiplicity(), range=UML_14_Multiplicity()) == None

