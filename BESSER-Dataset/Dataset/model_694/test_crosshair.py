from python_code import EMOF_Extent

def test_EMOF_Extent___init__():
    assert EMOF_Extent.__init__(EMOF_Extent()) == None

def test_EMOF_Extent_elements():
    assert EMOF_Extent.elements(EMOF_Extent()) == None

def test_EMOF_Extent_useContainment():
    assert EMOF_Extent.useContainment(EMOF_Extent()) == None


from python_code import EMOF_MultiplicityElement

def test_EMOF_MultiplicityElement___init__():
    assert EMOF_MultiplicityElement.__init__(EMOF_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import EMOF_ReflectiveCollection

def test_EMOF_ReflectiveCollection___init__():
    assert EMOF_ReflectiveCollection.__init__(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_remove():
    assert EMOF_ReflectiveCollection.remove(EMOF_ReflectiveCollection(), '') == None

def test_EMOF_ReflectiveCollection_clear():
    assert EMOF_ReflectiveCollection.clear(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_add():
    assert EMOF_ReflectiveCollection.add(EMOF_ReflectiveCollection(), '') == None

def test_EMOF_ReflectiveCollection_size():
    assert EMOF_ReflectiveCollection.size(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_addAll():
    assert EMOF_ReflectiveCollection.addAll(EMOF_ReflectiveCollection(), '') == None


from python_code import EMOF_ReflectiveSequence

def test_EMOF_ReflectiveSequence___init__():
    assert EMOF_ReflectiveSequence.__init__(EMOF_ReflectiveSequence()) == None

def test_EMOF_ReflectiveSequence_add():
    assert EMOF_ReflectiveSequence.add(EMOF_ReflectiveSequence(), '', '') == None

def test_EMOF_ReflectiveSequence_remove():
    assert EMOF_ReflectiveSequence.remove(EMOF_ReflectiveSequence(), '') == None

def test_EMOF_ReflectiveSequence_set():
    assert EMOF_ReflectiveSequence.set(EMOF_ReflectiveSequence(), '', '') == None

def test_EMOF_ReflectiveSequence_get():
    assert EMOF_ReflectiveSequence.get(EMOF_ReflectiveSequence(), '') == None


from python_code import EMOF_URIExtent

def test_EMOF_URIExtent___init__():
    assert EMOF_URIExtent.__init__(EMOF_URIExtent()) == None

def test_EMOF_URIExtent_uri():
    assert EMOF_URIExtent.uri(EMOF_URIExtent(), '') == None

def test_EMOF_URIExtent_element():
    assert EMOF_URIExtent.element(EMOF_URIExtent(), '') == None

def test_EMOF_URIExtent_contextURI():
    assert EMOF_URIExtent.contextURI(EMOF_URIExtent()) == None


from python_code import EssentialOCL_BooleanLiteralExp

def test_EssentialOCL_BooleanLiteralExp___init__():
    assert EssentialOCL_BooleanLiteralExp.__init__(EssentialOCL_BooleanLiteralExp(''), '') == None


from python_code import EssentialOCL_CollectionLiteralExp

def test_EssentialOCL_CollectionLiteralExp___init__():
    assert EssentialOCL_CollectionLiteralExp.__init__(EssentialOCL_CollectionLiteralExp('', collectionLiteralExp=set()), '', collectionLiteralExp=set()) == None


from python_code import EssentialOCL_IntegerLiteralExp

def test_EssentialOCL_IntegerLiteralExp___init__():
    assert EssentialOCL_IntegerLiteralExp.__init__(EssentialOCL_IntegerLiteralExp(''), '') == None


from python_code import EssentialOCL_RealLiteralExp

def test_EssentialOCL_RealLiteralExp___init__():
    assert EssentialOCL_RealLiteralExp.__init__(EssentialOCL_RealLiteralExp(''), '') == None


from python_code import EssentialOCL_StringLiteralExp

def test_EssentialOCL_StringLiteralExp___init__():
    assert EssentialOCL_StringLiteralExp.__init__(EssentialOCL_StringLiteralExp(''), '') == None


from python_code import EssentialOCL_UnlimitedNaturalExp

def test_EssentialOCL_UnlimitedNaturalExp___init__():
    assert EssentialOCL_UnlimitedNaturalExp.__init__(EssentialOCL_UnlimitedNaturalExp(''), '') == None


from python_code import ImperativeOCL_AssertExp
from python_code import LogExp
from python_code import OclExpression

def test_ImperativeOCL_AssertExp___init__():
    assert ImperativeOCL_AssertExp.__init__(ImperativeOCL_AssertExp('', ImperativeOCL_AssertExp=OclExpression(), ImperativeOCL_AssertExp244=LogExp()), '', ImperativeOCL_AssertExp=OclExpression(), ImperativeOCL_AssertExp244=LogExp()) == None


from python_code import ImperativeOCL_AssignExp
from python_code import OclExpression

def test_ImperativeOCL_AssignExp___init__():
    assert ImperativeOCL_AssignExp.__init__(ImperativeOCL_AssignExp('', ImperativeOCL_AssignExp=OclExpression(), ImperativeOCL_AssignExp248=OclExpression(), ImperativeOCL_AssignExp251=set()), '', ImperativeOCL_AssignExp=OclExpression(), ImperativeOCL_AssignExp248=OclExpression(), ImperativeOCL_AssignExp251=set()) == None


from python_code import QVTOperational_MappingCallExp

def test_QVTOperational_MappingCallExp___init__():
    assert QVTOperational_MappingCallExp.__init__(QVTOperational_MappingCallExp(''), '') == None

