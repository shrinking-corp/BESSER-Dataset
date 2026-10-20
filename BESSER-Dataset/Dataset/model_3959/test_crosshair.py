from python_code import classes_BehavioralFeature

def test_classes_BehavioralFeature___init__():
    assert classes_BehavioralFeature.__init__(classes_BehavioralFeature(False, classes_BehavioralFeature=set()), False, classes_BehavioralFeature=set()) == None


from python_code import classes_ElementImport
from python_code import classes_Namespace
from python_code import classes_PackageableElement

def test_classes_ElementImport___init__():
    assert classes_ElementImport.__init__(classes_ElementImport('', '\x00', ElementImport=classes_Namespace(), classes_ElementImport=classes_PackageableElement(), elementImport=classes_Namespace()), '\x00\x00', '', ElementImport=classes_Namespace(), classes_ElementImport=classes_PackageableElement(), elementImport=classes_Namespace()) == None


from python_code import classes_LiteralBoolean

def test_classes_LiteralBoolean___init__():
    assert classes_LiteralBoolean.__init__(classes_LiteralBoolean(True), False) == None

def test_classes_LiteralBoolean_booleanValue():
    assert classes_LiteralBoolean.booleanValue(classes_LiteralBoolean(False)) == None

def test_classes_LiteralBoolean_isComputable():
    assert classes_LiteralBoolean.isComputable(classes_LiteralBoolean(False)) == None


from python_code import classes_LiteralInteger

def test_classes_LiteralInteger___init__():
    assert classes_LiteralInteger.__init__(classes_LiteralInteger(0), 0) == None

def test_classes_LiteralInteger_isComputable():
    assert classes_LiteralInteger.isComputable(classes_LiteralInteger(0)) == None

def test_classes_LiteralInteger_integerValue():
    assert classes_LiteralInteger.integerValue(classes_LiteralInteger(0)) == None


from python_code import classes_LiteralNull

def test_classes_LiteralNull___init__():
    assert classes_LiteralNull.__init__(classes_LiteralNull()) == None

def test_classes_LiteralNull_isComputable():
    assert classes_LiteralNull.isComputable(classes_LiteralNull()) == None

def test_classes_LiteralNull_isNull():
    assert classes_LiteralNull.isNull(classes_LiteralNull()) == None


from python_code import classes_LiteralString

def test_classes_LiteralString___init__():
    assert classes_LiteralString.__init__(classes_LiteralString(''), '') == None

def test_classes_LiteralString_stringValue():
    assert classes_LiteralString.stringValue(classes_LiteralString('')) == None

def test_classes_LiteralString_isComputable():
    assert classes_LiteralString.isComputable(classes_LiteralString('')) == None


from python_code import classes_LiteralUnlimitedNatural

def test_classes_LiteralUnlimitedNatural___init__():
    assert classes_LiteralUnlimitedNatural.__init__(classes_LiteralUnlimitedNatural(0), 0) == None

def test_classes_LiteralUnlimitedNatural_unlimitedValue():
    assert classes_LiteralUnlimitedNatural.unlimitedValue(classes_LiteralUnlimitedNatural(0)) == None

def test_classes_LiteralUnlimitedNatural_isComputable():
    assert classes_LiteralUnlimitedNatural.isComputable(classes_LiteralUnlimitedNatural(0)) == None


from python_code import classes_Namespace
from python_code import classes_Package
from python_code import classes_PackageImport

def test_classes_PackageImport___init__():
    assert classes_PackageImport.__init__(classes_PackageImport('', PackageImport=classes_Namespace(), classes_PackageImport=classes_Package(), packageImport=classes_Namespace()), '', PackageImport=classes_Namespace(), classes_PackageImport=classes_Package(), packageImport=classes_Namespace()) == None


from python_code import classes_Slot
from python_code import classes_StructuralFeature

def test_classes_StructuralFeature___init__():
    assert classes_StructuralFeature.__init__(classes_StructuralFeature(True, classes_StructuralFeature=classes_Slot()), False, classes_StructuralFeature=classes_Slot()) == None

