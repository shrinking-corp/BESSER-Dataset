from python_code import FlatQVT_AssertExp
from python_code import LogExp
from python_code import OclExpression

def test_FlatQVT_AssertExp___init__():
    assert FlatQVT_AssertExp.__init__(FlatQVT_AssertExp('', FlatQVT_AssertExp10=LogExp(), FlatQVT_AssertExp=OclExpression()), '', FlatQVT_AssertExp10=LogExp(), FlatQVT_AssertExp=OclExpression()) == None


from python_code import FlatQVT_AssignExp
from python_code import FlatQVT_IfExp
from python_code import OclExpression

def test_FlatQVT_AssignExp___init__():
    assert FlatQVT_AssignExp.__init__(FlatQVT_AssignExp('', FlatQVT_AssignExp=OclExpression(), FlatQVT_AssignExp14=OclExpression(), FlatQVT_AssignExp17=set()), '', FlatQVT_AssignExp=FlatQVT_IfExp(), FlatQVT_AssignExp14=OclExpression(), FlatQVT_AssignExp17=set()) == None


from python_code import FlatQVT_BooleanLiteralExp

def test_FlatQVT_BooleanLiteralExp___init__():
    assert FlatQVT_BooleanLiteralExp.__init__(FlatQVT_BooleanLiteralExp(''), '') == None


from python_code import FlatQVT_CollectionLiteralExp

def test_FlatQVT_CollectionLiteralExp___init__():
    assert FlatQVT_CollectionLiteralExp.__init__(FlatQVT_CollectionLiteralExp('', FlatQVT_CollectionLiteralExp=set()), '', FlatQVT_CollectionLiteralExp=set()) == None


from python_code import FlatQVT_Extent

def test_FlatQVT_Extent___init__():
    assert FlatQVT_Extent.__init__(FlatQVT_Extent()) == None

def test_FlatQVT_Extent_elements():
    assert FlatQVT_Extent.elements(FlatQVT_Extent()) == None

def test_FlatQVT_Extent_useContainment():
    assert FlatQVT_Extent.useContainment(FlatQVT_Extent()) == None


from python_code import FlatQVT_IntegerLiteralExp

def test_FlatQVT_IntegerLiteralExp___init__():
    assert FlatQVT_IntegerLiteralExp.__init__(FlatQVT_IntegerLiteralExp(''), '') == None


from python_code import FlatQVT_MappingCallExp

def test_FlatQVT_MappingCallExp___init__():
    assert FlatQVT_MappingCallExp.__init__(FlatQVT_MappingCallExp(''), '') == None


from python_code import FlatQVT_MultiplicityElement

def test_FlatQVT_MultiplicityElement___init__():
    assert FlatQVT_MultiplicityElement.__init__(FlatQVT_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import FlatQVT_RealLiteralExp

def test_FlatQVT_RealLiteralExp___init__():
    assert FlatQVT_RealLiteralExp.__init__(FlatQVT_RealLiteralExp(''), '') == None


from python_code import FlatQVT_ReflectiveCollection

def test_FlatQVT_ReflectiveCollection___init__():
    assert FlatQVT_ReflectiveCollection.__init__(FlatQVT_ReflectiveCollection()) == None

def test_FlatQVT_ReflectiveCollection_size():
    assert FlatQVT_ReflectiveCollection.size(FlatQVT_ReflectiveCollection()) == None

def test_FlatQVT_ReflectiveCollection_remove():
    assert FlatQVT_ReflectiveCollection.remove(FlatQVT_ReflectiveCollection(), '') == None

def test_FlatQVT_ReflectiveCollection_clear():
    assert FlatQVT_ReflectiveCollection.clear(FlatQVT_ReflectiveCollection()) == None

def test_FlatQVT_ReflectiveCollection_add():
    assert FlatQVT_ReflectiveCollection.add(FlatQVT_ReflectiveCollection(), '') == None

def test_FlatQVT_ReflectiveCollection_addAll():
    assert FlatQVT_ReflectiveCollection.addAll(FlatQVT_ReflectiveCollection(), '') == None


from python_code import FlatQVT_ReflectiveSequence

def test_FlatQVT_ReflectiveSequence___init__():
    assert FlatQVT_ReflectiveSequence.__init__(FlatQVT_ReflectiveSequence()) == None

def test_FlatQVT_ReflectiveSequence_remove():
    assert FlatQVT_ReflectiveSequence.remove(FlatQVT_ReflectiveSequence(), '') == None

def test_FlatQVT_ReflectiveSequence_set():
    assert FlatQVT_ReflectiveSequence.set(FlatQVT_ReflectiveSequence(), '', '') == None

def test_FlatQVT_ReflectiveSequence_add():
    assert FlatQVT_ReflectiveSequence.add(FlatQVT_ReflectiveSequence(), '', '') == None

def test_FlatQVT_ReflectiveSequence_get():
    assert FlatQVT_ReflectiveSequence.get(FlatQVT_ReflectiveSequence(), '') == None


from python_code import FlatQVT_StringLiteralExp

def test_FlatQVT_StringLiteralExp___init__():
    assert FlatQVT_StringLiteralExp.__init__(FlatQVT_StringLiteralExp(''), '') == None


from python_code import FlatQVT_URIExtent

def test_FlatQVT_URIExtent___init__():
    assert FlatQVT_URIExtent.__init__(FlatQVT_URIExtent()) == None

def test_FlatQVT_URIExtent_uri():
    assert FlatQVT_URIExtent.uri(FlatQVT_URIExtent(), '') == None

def test_FlatQVT_URIExtent_contextURI():
    assert FlatQVT_URIExtent.contextURI(FlatQVT_URIExtent()) == None

def test_FlatQVT_URIExtent_element():
    assert FlatQVT_URIExtent.element(FlatQVT_URIExtent(), '') == None


from python_code import FlatQVT_UnlimitedNaturalExp

def test_FlatQVT_UnlimitedNaturalExp___init__():
    assert FlatQVT_UnlimitedNaturalExp.__init__(FlatQVT_UnlimitedNaturalExp(''), '') == None

