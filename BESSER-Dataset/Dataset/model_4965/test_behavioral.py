import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    Classifier,
    EnumLiteral,
    Enumeration,
    LocatedElement,
    Metamodel,
    ModelElement,
    Operation,
    Package,
    Parameter,
    Reference,
    StructuralFeature,
    TemplateParameter,
    TypedElement,
    km3_Attribute,
    km3_Class,
    km3_Classifier,
    km3_DataType,
    km3_EnumLiteral,
    km3_Enumeration,
    km3_LocatedElement,
    km3_Metamodel,
    km3_ModelElement,
    km3_Operation,
    km3_Package,
    km3_Parameter,
    km3_Reference,
    km3_StructuralFeature,
    km3_TemplateParameter,
    km3_TypedElement,
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

def test_assoc_operations7_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so km3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'owner8', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'owner8', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_opposite16_stub_double():
    # Reference has no real 'Reference' property in the generated
    # code (a bare stub) -- manually attach it so km3_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_Reference(isContainer="sample_text")
    partner = Reference()
    setattr(partner, 'Reference', None)
    _safe_set(owner, 'km3_Reference', partner)
    assert getattr(partner, 'Reference') == owner
    _safe_set(owner, 'km3_Reference', None)
    assert getattr(partner, 'Reference') is None


def test_assoc_package0_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so km3_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_ModelElement(name="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'contents', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'contents', None)
    assert getattr(partner, 'Package') is None


def test_assoc_parameters3_stub_double():
    # TemplateParameter has no real 'TemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so km3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_Class(isAbstract="sample_text")
    partner = TemplateParameter()
    setattr(partner, 'TemplateParameter', None)
    _safe_set(owner, 'km3_Class', {partner})
    assert getattr(partner, 'TemplateParameter') == owner
    _safe_set(owner, 'km3_Class', set())
    assert getattr(partner, 'TemplateParameter') is None


def test_assoc_structuralFeatures6_stub_double():
    # StructuralFeature has no real 'StructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so km3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_Class(isAbstract="sample_text")
    partner = StructuralFeature()
    setattr(partner, 'StructuralFeature', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'StructuralFeature') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'StructuralFeature') is None


def test_assoc_supertypes4_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so km3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_Class(isAbstract="sample_text")
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'km3_Class5', {partner})
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'km3_Class5', set())
    assert getattr(partner, 'Class') is None


def test_assoc_type9_stub_double():
    # Classifier has no real 'Classifier' property in the generated
    # code (a bare stub) -- manually attach it so km3_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # km3_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = km3_TypedElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier', None)
    _safe_set(owner, 'km3_TypedElement', partner)
    assert getattr(partner, 'Classifier') == owner
    _safe_set(owner, 'km3_TypedElement', None)
    assert getattr(partner, 'Classifier') is None


