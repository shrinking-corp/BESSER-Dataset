from python_code import ram_CombinedFragment

def test_ram_CombinedFragment___init__():
    assert ram_CombinedFragment.__init__(ram_CombinedFragment('', ram_CombinedFragment=set()), '', ram_CombinedFragment=set()) == None


from python_code import ram_ImplementationClass

def test_ram_ImplementationClass___init__():
    assert ram_ImplementationClass.__init__(ram_ImplementationClass(''), '') == None


from python_code import ram_Aspect
from python_code import ram_Instantiation

def test_ram_Instantiation___init__():
    assert ram_Instantiation.__init__(ram_Instantiation('', ram_Instantiation=ram_Aspect(), ram_Instantiation25=set(), ram_Instantiation27=ram_Aspect()), '', ram_Instantiation=ram_Aspect(), ram_Instantiation25=set(), ram_Instantiation27=ram_Aspect()) == None


from python_code import ram_ElementMap
from python_code import ram_LayoutElement

def test_ram_LayoutElement___init__():
    assert ram_LayoutElement.__init__(ram_LayoutElement(0.0, 0.0, ram_LayoutElement=ram_ElementMap()), 0.0, 0.0, ram_LayoutElement=ram_ElementMap()) == None


from python_code import ram_LiteralBoolean

def test_ram_LiteralBoolean___init__():
    assert ram_LiteralBoolean.__init__(ram_LiteralBoolean(True), False) == None


from python_code import ram_LiteralInteger

def test_ram_LiteralInteger___init__():
    assert ram_LiteralInteger.__init__(ram_LiteralInteger(0), 0) == None


from python_code import ram_LiteralString

def test_ram_LiteralString___init__():
    assert ram_LiteralString.__init__(ram_LiteralString(''), '') == None


from python_code import ram_NamedElement

def test_ram_NamedElement___init__():
    assert ram_NamedElement.__init__(ram_NamedElement(''), '') == None


from python_code import ram_OpaqueExpression

def test_ram_OpaqueExpression___init__():
    assert ram_OpaqueExpression.__init__(ram_OpaqueExpression('', '\x00'), '\x00\x00', '') == None


from python_code import ram_Property

def test_ram_Property___init__():
    assert ram_Property.__init__(ram_Property(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import ram_RAny

def test_ram_RAny___init__():
    assert ram_RAny.__init__(ram_RAny()) == None

def test_ram_RAny_getName():
    assert ram_RAny.getName(ram_RAny()) == None


from python_code import ram_RBoolean

def test_ram_RBoolean___init__():
    assert ram_RBoolean.__init__(ram_RBoolean()) == None

def test_ram_RBoolean_getInstanceClassName():
    assert ram_RBoolean.getInstanceClassName(ram_RBoolean()) == None

def test_ram_RBoolean_getName():
    assert ram_RBoolean.getName(ram_RBoolean()) == None


from python_code import ram_RChar

def test_ram_RChar___init__():
    assert ram_RChar.__init__(ram_RChar()) == None

def test_ram_RChar_getInstanceClassName():
    assert ram_RChar.getInstanceClassName(ram_RChar()) == None

def test_ram_RChar_getName():
    assert ram_RChar.getName(ram_RChar()) == None


from python_code import ram_ObjectType
from python_code import ram_RCollection

def test_ram_RCollection___init__():
    assert ram_RCollection.__init__(ram_RCollection(ram_RCollection=ram_ObjectType()), ram_RCollection=ram_ObjectType()) == None

def test_ram_RCollection_getName():
    assert ram_RCollection.getName(ram_RCollection(ram_RCollection=ram_ObjectType())) == None


from python_code import ram_RInt

def test_ram_RInt___init__():
    assert ram_RInt.__init__(ram_RInt()) == None

def test_ram_RInt_getInstanceClassName():
    assert ram_RInt.getInstanceClassName(ram_RInt()) == None

def test_ram_RInt_getName():
    assert ram_RInt.getName(ram_RInt()) == None


from python_code import ram_RString

def test_ram_RString___init__():
    assert ram_RString.__init__(ram_RString()) == None

def test_ram_RString_getInstanceClassName():
    assert ram_RString.getInstanceClassName(ram_RString()) == None

def test_ram_RString_getName():
    assert ram_RString.getName(ram_RString()) == None


from python_code import ram_RVoid

def test_ram_RVoid___init__():
    assert ram_RVoid.__init__(ram_RVoid()) == None

def test_ram_RVoid_getName():
    assert ram_RVoid.getName(ram_RVoid()) == None


from python_code import ram_Lifeline
from python_code import ram_TypedElement

def test_ram_TypedElement___init__():
    assert ram_TypedElement.__init__(ram_TypedElement(ram_TypedElement=ram_Lifeline()), ram_TypedElement=ram_Lifeline()) == None

def test_ram_TypedElement_getType():
    assert ram_TypedElement.getType(ram_TypedElement(ram_TypedElement=ram_Lifeline())) == None

