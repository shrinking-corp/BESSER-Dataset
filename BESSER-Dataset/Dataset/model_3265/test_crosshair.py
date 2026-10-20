from python_code import aadl2_Access

def test_aadl2_Access___init__():
    assert aadl2_Access.__init__(aadl2_Access('', '\x00'), '\x00\x00', '') == None


from python_code import aadl2_ArrayDimension
from python_code import aadl2_ArraySize
from python_code import aadl2_ArraySizeProperty

def test_aadl2_ArraySize___init__():
    assert aadl2_ArraySize.__init__(aadl2_ArraySize('', aadl2_ArraySize82=aadl2_ArraySizeProperty(), aadl2_ArraySize=aadl2_ArrayDimension()), '', aadl2_ArraySize82=aadl2_ArraySizeProperty(), aadl2_ArraySize=aadl2_ArrayDimension()) == None


from python_code import aadl2_BehavioredImplementation

def test_aadl2_BehavioredImplementation___init__():
    assert aadl2_BehavioredImplementation.__init__(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation401=set()), aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation401=set()) == None

def test_aadl2_BehavioredImplementation_subprogramCalls():
    assert aadl2_BehavioredImplementation.subprogramCalls(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation401=set())) == None


from python_code import aadl2_BooleanLiteral

def test_aadl2_BooleanLiteral___init__():
    assert aadl2_BooleanLiteral.__init__(aadl2_BooleanLiteral(''), '') == None


from python_code import aadl2_ComponentPrototypeActual
from python_code import aadl2_ComponentPrototypeBinding
from python_code import aadl2_SubcomponentType

def test_aadl2_ComponentPrototypeActual___init__():
    assert aadl2_ComponentPrototypeActual.__init__(aadl2_ComponentPrototypeActual('', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding(), aadl2_ComponentPrototypeActual368=set(), aadl2_ComponentPrototypeActual371=aadl2_SubcomponentType()), '', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding(), aadl2_ComponentPrototypeActual368=set(), aadl2_ComponentPrototypeActual371=aadl2_SubcomponentType()) == None


from python_code import aadl2_ComputedValue

def test_aadl2_ComputedValue___init__():
    assert aadl2_ComputedValue.__init__(aadl2_ComputedValue(''), '') == None


from python_code import aadl2_AnnexLibrary
from python_code import aadl2_DefaultAnnexLibrary

def test_aadl2_DefaultAnnexLibrary___init__():
    assert aadl2_DefaultAnnexLibrary.__init__(aadl2_DefaultAnnexLibrary('', aadl2_DefaultAnnexLibrary=aadl2_AnnexLibrary()), '', aadl2_DefaultAnnexLibrary=aadl2_AnnexLibrary()) == None


from python_code import aadl2_AnnexSubclause
from python_code import aadl2_DefaultAnnexSubclause

def test_aadl2_DefaultAnnexSubclause___init__():
    assert aadl2_DefaultAnnexSubclause.__init__(aadl2_DefaultAnnexSubclause('', aadl2_DefaultAnnexSubclause=aadl2_AnnexSubclause()), '', aadl2_DefaultAnnexSubclause=aadl2_AnnexSubclause()) == None


from python_code import aadl2_DirectedFeature

def test_aadl2_DirectedFeature___init__():
    assert aadl2_DirectedFeature.__init__(aadl2_DirectedFeature(''), '') == None


from python_code import aadl2_IntegerLiteral

def test_aadl2_IntegerLiteral___init__():
    assert aadl2_IntegerLiteral.__init__(aadl2_IntegerLiteral('', '\x00'), '\x00\x00', '') == None

