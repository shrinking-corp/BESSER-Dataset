from python_code import art_relaxed_AspectModelElement

def test_art_relaxed_AspectModelElement___init__():
    assert art_relaxed_AspectModelElement.__init__(art_relaxed_AspectModelElement(''), '') == None


from python_code import art_relaxed_CardinalityElement

def test_art_relaxed_CardinalityElement___init__():
    assert art_relaxed_CardinalityElement.__init__(art_relaxed_CardinalityElement('', '\x00'), '\x00\x00', '') == None


from python_code import art_relaxed_NamedElement

def test_art_relaxed_NamedElement___init__():
    assert art_relaxed_NamedElement.__init__(art_relaxed_NamedElement(''), '') == None


from python_code import art_relaxed_distrib_relaxed_Node

def test_art_relaxed_distrib_relaxed_Node___init__():
    assert art_relaxed_distrib_relaxed_Node.__init__(art_relaxed_distrib_relaxed_Node('', art_relaxed_distrib_relaxed_Node=set()), '', art_relaxed_distrib_relaxed_Node=set()) == None


from python_code import ComponentImplementation
from python_code import ComponentType
from python_code import CompositeInstance
from python_code import art_relaxed_implem_relaxed_FractalComponent
from python_code import art_relaxed_instance_relaxed_ComponentInstance

def test_art_relaxed_implem_relaxed_FractalComponent___init__():
    assert art_relaxed_implem_relaxed_FractalComponent.__init__(art_relaxed_implem_relaxed_FractalComponent('\x00', '', ComponentImplementation=art_relaxed_instance_relaxed_ComponentInstance('', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set())), '', '', ComponentImplementation=art_relaxed_instance_relaxed_ComponentInstance('', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set())) == None


from python_code import art_relaxed_implem_relaxed_OSGiType
from python_code import art_relaxed_type_relaxed_ComponentType

def test_art_relaxed_implem_relaxed_OSGiType___init__():
    assert art_relaxed_implem_relaxed_OSGiType.__init__(art_relaxed_implem_relaxed_OSGiType('', TypeImplementation=art_relaxed_type_relaxed_ComponentType()), '', TypeImplementation=art_relaxed_type_relaxed_ComponentType()) == None


from python_code import ComponentInstance
from python_code import art_relaxed_instance_relaxed_Binding

def test_art_relaxed_instance_relaxed_Binding___init__():
    assert art_relaxed_instance_relaxed_Binding.__init__(art_relaxed_instance_relaxed_Binding('', art_relaxed_instance_relaxed_Binding=ComponentInstance()), '\x00', art_relaxed_instance_relaxed_Binding=ComponentInstance()) == None


from python_code import ComponentImplementation
from python_code import ComponentType
from python_code import CompositeInstance
from python_code import art_relaxed_instance_relaxed_ComponentInstance

def test_art_relaxed_instance_relaxed_ComponentInstance___init__():
    assert art_relaxed_instance_relaxed_ComponentInstance.__init__(art_relaxed_instance_relaxed_ComponentInstance('', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set()), '', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set()) == None


from python_code import art_relaxed_instance_relaxed_Entry

def test_art_relaxed_instance_relaxed_Entry___init__():
    assert art_relaxed_instance_relaxed_Entry.__init__(art_relaxed_instance_relaxed_Entry(''), '') == None


from python_code import art_relaxed_instance_relaxed_DictionaryValuedAttribute
from python_code import art_relaxed_instance_relaxed_OtherEntry

def test_art_relaxed_instance_relaxed_OtherEntry___init__():
    assert art_relaxed_instance_relaxed_OtherEntry.__init__(art_relaxed_instance_relaxed_OtherEntry('', Entry=art_relaxed_instance_relaxed_DictionaryValuedAttribute()), '', Entry=art_relaxed_instance_relaxed_DictionaryValuedAttribute()) == None


from python_code import BasicAttribute
from python_code import ComponentImplementation
from python_code import ComponentType
from python_code import CompositeInstance
from python_code import art_relaxed_instance_relaxed_ComponentInstance
from python_code import art_relaxed_instance_relaxed_ValuedAttribute

def test_art_relaxed_instance_relaxed_ValuedAttribute___init__():
    assert art_relaxed_instance_relaxed_ValuedAttribute.__init__(art_relaxed_instance_relaxed_ValuedAttribute('', art_relaxed_instance_relaxed_ValuedAttribute=BasicAttribute(), AttributeInstance=art_relaxed_instance_relaxed_ComponentInstance('', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set())), '', art_relaxed_instance_relaxed_ValuedAttribute=BasicAttribute(), AttributeInstance=art_relaxed_instance_relaxed_ComponentInstance('', art_relaxed_instance_relaxed_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_relaxed_instance_relaxed_ComponentInstance15=set(), art_relaxed_instance_relaxed_ComponentInstance17=set(), art_relaxed_instance_relaxed_ComponentInstance19=ComponentImplementation(), instances=set())) == None


from python_code import Service
from python_code import art_relaxed_type_relaxed_AbstractPort

def test_art_relaxed_type_relaxed_AbstractPort___init__():
    assert art_relaxed_type_relaxed_AbstractPort.__init__(art_relaxed_type_relaxed_AbstractPort('\x00\x00', '', '', art_relaxed_type_relaxed_AbstractPort=Service()), '', '', '', art_relaxed_type_relaxed_AbstractPort=Service()) == None


from python_code import art_relaxed_type_relaxed_BasicAttribute
from python_code import art_relaxed_type_relaxed_ComponentType

def test_art_relaxed_type_relaxed_BasicAttribute___init__():
    assert art_relaxed_type_relaxed_BasicAttribute.__init__(art_relaxed_type_relaxed_BasicAttribute('', Attribute=art_relaxed_type_relaxed_ComponentType()), '', Attribute=art_relaxed_type_relaxed_ComponentType()) == None


from python_code import art_relaxed_type_relaxed_DictionaryDefaultValue

def test_art_relaxed_type_relaxed_DictionaryDefaultValue___init__():
    assert art_relaxed_type_relaxed_DictionaryDefaultValue.__init__(art_relaxed_type_relaxed_DictionaryDefaultValue('', '\x00'), '\x00\x00', '') == None

