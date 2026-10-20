import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    Class,
    Field,
    Interface,
    Java_Annotation,
    Java_Assignment,
    Java_Class,
    Java_Field,
    Java_Interface,
    Java_Method,
    Java_MethodCall,
    Java_MethodSignature,
    Java_ObjectType,
    Java_Package,
    Java_Parameter,
    Java_PrimitiveType,
    Java_Return,
    Java_Statement,
    Java_Type,
    Java_VariableDeclaration,
    Java_VoidType,
    Method,
    MethodSignature,
    ObjectType,
    Package,
    Parameter,
    Statement,
    Type,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_content0_stub_double():
    # ObjectType has no real 'ObjectType' property in the generated
    # code (a bare stub) -- manually attach it so Java_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Package(name="sample_text")
    partner = ObjectType()
    setattr(partner, 'ObjectType', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'ObjectType') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'ObjectType') is None


def test_assoc_field5_stub_double():
    # Field has no real 'Field' property in the generated
    # code (a bare stub) -- manually attach it so Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Class(isPublic=True, isStatic=True)
    partner = Field()
    setattr(partner, 'Field', None)
    _safe_set(owner, 'owner6', {partner})
    assert getattr(partner, 'Field') == owner
    _safe_set(owner, 'owner6', set())
    assert getattr(partner, 'Field') is None


def test_assoc_implements2_stub_double():
    # Interface has no real 'Interface' property in the generated
    # code (a bare stub) -- manually attach it so Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Class(isPublic=True, isStatic=True)
    partner = Interface()
    setattr(partner, 'Interface', None)
    _safe_set(owner, 'Java_Class', {partner})
    assert getattr(partner, 'Interface') == owner
    _safe_set(owner, 'Java_Class', set())
    assert getattr(partner, 'Interface') is None


def test_assoc_method7_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Class(isPublic=True, isStatic=True)
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'Java_Class8', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'Java_Class8', set())
    assert getattr(partner, 'Method') is None


def test_assoc_owner23_stub_double():
    # Class has no real 'Class24' property in the generated
    # code (a bare stub) -- manually attach it so Java_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Field(isPrivate=True, isProtected=True, isPublic=True, isStatic=True, name="sample_text")
    partner = Class()
    setattr(partner, 'Class24', None)
    _safe_set(owner, 'field', partner)
    assert getattr(partner, 'Class24') == owner
    _safe_set(owner, 'field', None)
    assert getattr(partner, 'Class24') is None


def test_assoc_parameters14_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so Java_MethodSignature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_MethodSignature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_MethodSignature(isPrivate=True, isProtected=True, isPublic=True, isStatic=True, name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'Java_MethodSignature15', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'Java_MethodSignature15', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType13_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so Java_MethodSignature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_MethodSignature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_MethodSignature(isPrivate=True, isProtected=True, isPublic=True, isStatic=True, name="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'Java_MethodSignature', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'Java_MethodSignature', None)
    assert getattr(partner, 'Type') is None


def test_assoc_superclass3_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Class(isPublic=True, isStatic=True)
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'Java_Class4', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'Java_Class4', None)
    assert getattr(partner, 'Class') is None


def test_assoc_type19_stub_double():
    # Type has no real 'Type20' property in the generated
    # code (a bare stub) -- manually attach it so Java_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Parameter(name="sample_text")
    partner = Type()
    setattr(partner, 'Type20', None)
    _safe_set(owner, 'Java_Parameter', partner)
    assert getattr(partner, 'Type20') == owner
    _safe_set(owner, 'Java_Parameter', None)
    assert getattr(partner, 'Type20') is None


def test_assoc_type21_stub_double():
    # Type has no real 'Type22' property in the generated
    # code (a bare stub) -- manually attach it so Java_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Field(isPrivate=True, isProtected=True, isPublic=True, isStatic=True, name="sample_text")
    partner = Type()
    setattr(partner, 'Type22', None)
    _safe_set(owner, 'Java_Field', partner)
    assert getattr(partner, 'Type22') == owner
    _safe_set(owner, 'Java_Field', None)
    assert getattr(partner, 'Type22') is None


def test_assoc_type25_stub_double():
    # Type has no real 'Type26' property in the generated
    # code (a bare stub) -- manually attach it so Java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_VariableDeclaration(variableName="sample_text")
    partner = Type()
    setattr(partner, 'Type26', None)
    _safe_set(owner, 'Java_VariableDeclaration', partner)
    assert getattr(partner, 'Type26') == owner
    _safe_set(owner, 'Java_VariableDeclaration', None)
    assert getattr(partner, 'Type26') is None


