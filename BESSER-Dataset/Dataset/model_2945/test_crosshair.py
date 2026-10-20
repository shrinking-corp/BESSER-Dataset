from python_code import jointPackage_UML2ER_SrcNamedElement

def test_jointPackage_UML2ER_SrcNamedElement___init__():
    assert jointPackage_UML2ER_SrcNamedElement.__init__(jointPackage_UML2ER_SrcNamedElement(''), '') == None


from python_code import SrcClass
from python_code import jointPackage_UML2ER_SrcProperty

def test_jointPackage_UML2ER_SrcProperty___init__():
    assert jointPackage_UML2ER_SrcProperty.__init__(jointPackage_UML2ER_SrcProperty('', False, jointPackage_UML2ER_SrcProperty=SrcClass()), '', False, jointPackage_UML2ER_SrcProperty=SrcClass()) == None


from python_code import jointPackage_UML2ER_TrgAttribute
from python_code import jointPackage_UML2ER_TrgEntityType

def test_jointPackage_UML2ER_TrgAttribute___init__():
    assert jointPackage_UML2ER_TrgAttribute.__init__(jointPackage_UML2ER_TrgAttribute('', TrgFeature=jointPackage_UML2ER_TrgEntityType()), '', TrgFeature=jointPackage_UML2ER_TrgEntityType()) == None


from python_code import jointPackage_UML2ER_TrgElement

def test_jointPackage_UML2ER_TrgElement___init__():
    assert jointPackage_UML2ER_TrgElement.__init__(jointPackage_UML2ER_TrgElement(''), '') == None

