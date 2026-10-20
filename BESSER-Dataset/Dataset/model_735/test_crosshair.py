from python_code import art_CardinalityElement

def test_art_CardinalityElement___init__():
    assert art_CardinalityElement.__init__(art_CardinalityElement('', '\x00'), '\x00\x00', '') == None


from python_code import art_NamedElement

def test_art_NamedElement___init__():
    assert art_NamedElement.__init__(art_NamedElement(''), '') == None


from python_code import ComponentImplementation
from python_code import ComponentType
from python_code import CompositeInstance
from python_code import art_implem_FractalComponent
from python_code import art_instance_ComponentInstance

def test_art_implem_FractalComponent___init__():
    assert art_implem_FractalComponent.__init__(art_implem_FractalComponent('\x00', '', ComponentImplementation=art_instance_ComponentInstance('', art_instance_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_instance_ComponentInstance16=set(), art_instance_ComponentInstance18=set(), art_instance_ComponentInstance20=ComponentImplementation(), instances=set())), '', '', ComponentImplementation=art_instance_ComponentInstance('', art_instance_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_instance_ComponentInstance16=set(), art_instance_ComponentInstance18=set(), art_instance_ComponentInstance20=ComponentImplementation(), instances=set())) == None


from python_code import art_implem_OSGiType
from python_code import art_type_ComponentType

def test_art_implem_OSGiType___init__():
    assert art_implem_OSGiType.__init__(art_implem_OSGiType('', TypeImplementation=art_type_ComponentType()), '', TypeImplementation=art_type_ComponentType()) == None


from python_code import ComponentInstance
from python_code import art_instance_Binding

def test_art_instance_Binding___init__():
    assert art_instance_Binding.__init__(art_instance_Binding('', art_instance_Binding=ComponentInstance()), '\x00', art_instance_Binding=ComponentInstance()) == None


from python_code import ComponentImplementation
from python_code import ComponentType
from python_code import CompositeInstance
from python_code import art_instance_ComponentInstance

def test_art_instance_ComponentInstance___init__():
    assert art_instance_ComponentInstance.__init__(art_instance_ComponentInstance('', art_instance_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_instance_ComponentInstance16=set(), art_instance_ComponentInstance18=set(), art_instance_ComponentInstance20=ComponentImplementation(), instances=set()), '', art_instance_ComponentInstance=ComponentType(), subComponent=CompositeInstance(), art_instance_ComponentInstance16=set(), art_instance_ComponentInstance18=set(), art_instance_ComponentInstance20=ComponentImplementation(), instances=set()) == None


from python_code import art_instance_Entry

def test_art_instance_Entry___init__():
    assert art_instance_Entry.__init__(art_instance_Entry(''), '') == None


from python_code import art_instance_DictionaryValuedAttribute
from python_code import art_instance_OtherEntry

def test_art_instance_OtherEntry___init__():
    assert art_instance_OtherEntry.__init__(art_instance_OtherEntry('', Entry=art_instance_DictionaryValuedAttribute()), '', Entry=art_instance_DictionaryValuedAttribute()) == None


from python_code import Service
from python_code import art_type_AbstractPort

def test_art_type_AbstractPort___init__():
    assert art_type_AbstractPort.__init__(art_type_AbstractPort('', art_type_AbstractPort=Service()), '\x00', art_type_AbstractPort=Service()) == None


from python_code import art_type_BasicAttribute
from python_code import art_type_ComponentType

def test_art_type_BasicAttribute___init__():
    assert art_type_BasicAttribute.__init__(art_type_BasicAttribute('', Attribute=art_type_ComponentType()), '', Attribute=art_type_ComponentType()) == None


from python_code import art_type_DictionaryDefaultValue

def test_art_type_DictionaryDefaultValue___init__():
    assert art_type_DictionaryDefaultValue.__init__(art_type_DictionaryDefaultValue('', '\x00'), '\x00\x00', '') == None


from python_code import art_type_Port

def test_art_type_Port___init__():
    assert art_type_Port.__init__(art_type_Port(''), '') == None

