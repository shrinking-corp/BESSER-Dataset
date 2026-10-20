from python_code import EMOF_Extent

def test_EMOF_Extent___init__():
    assert EMOF_Extent.__init__(EMOF_Extent()) == None

def test_EMOF_Extent_useContainment():
    assert EMOF_Extent.useContainment(EMOF_Extent()) == None

def test_EMOF_Extent_elements():
    assert EMOF_Extent.elements(EMOF_Extent()) == None


from python_code import EMOF_MultiplicityElement

def test_EMOF_MultiplicityElement___init__():
    assert EMOF_MultiplicityElement.__init__(EMOF_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Class
from python_code import EMOF_Property
from python_code import Property

def test_EMOF_Property___init__():
    assert EMOF_Property.__init__(EMOF_Property('', '', '', '', '', EMOF_Property=Class(), EMOF_Property29=Property()), '', '', '', '', '', EMOF_Property=Class(), EMOF_Property29=Property()) == None


from python_code import EMOF_ReflectiveCollection

def test_EMOF_ReflectiveCollection___init__():
    assert EMOF_ReflectiveCollection.__init__(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_clear():
    assert EMOF_ReflectiveCollection.clear(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_addAll():
    assert EMOF_ReflectiveCollection.addAll(EMOF_ReflectiveCollection(), '') == None

def test_EMOF_ReflectiveCollection_remove():
    assert EMOF_ReflectiveCollection.remove(EMOF_ReflectiveCollection(), '') == None

def test_EMOF_ReflectiveCollection_size():
    assert EMOF_ReflectiveCollection.size(EMOF_ReflectiveCollection()) == None

def test_EMOF_ReflectiveCollection_add():
    assert EMOF_ReflectiveCollection.add(EMOF_ReflectiveCollection(), '') == None


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

