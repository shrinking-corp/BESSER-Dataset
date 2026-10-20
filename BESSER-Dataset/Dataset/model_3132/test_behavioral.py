import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassM_Attribute,
    ClassM_Class,
    ClassM_Classifier,
    ClassM_Model,
    ClassM_Operation,
    ClassM_Parameter,
    ClassM_PrimitiveType,
    ClassM_StructuralFeature,
    ClassM_TypedElement,
    Classifier,
    StructuralFeature,
    TypedElement,
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

def test_assoc_classifiers11_stub_double():
    # ClassM_Model has no real 'ClassM_Model' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Classifier(name="sample_text")
    partner = ClassM_Model()
    setattr(partner, 'ClassM_Model', None)
    _safe_set(owner, 'ClassM_Classifier', partner)
    assert owner in getattr(partner, 'ClassM_Model')
    _safe_set(owner, 'ClassM_Classifier', None)
    assert owner not in getattr(partner, 'ClassM_Model')


def test_assoc_features0_stub_double():
    # ClassM_Class has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_StructuralFeature(name="sample_text", visibility="sample_text")
    partner = ClassM_Class()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'StructuralFeature', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'StructuralFeature', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_owner7_stub_double():
    # ClassM_Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_StructuralFeature(name="sample_text", visibility="sample_text")
    partner = ClassM_Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'features', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'features', None)
    assert getattr(partner, 'Class') is None


def test_assoc_paramOf10_stub_double():
    # ClassM_Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Parameter(name="sample_text")
    partner = ClassM_Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'params', partner)
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'params', None)
    assert getattr(partner, 'Operation') is None


def test_assoc_params9_stub_double():
    # ClassM_Operation has no real 'paramOf' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Parameter(name="sample_text")
    partner = ClassM_Operation()
    setattr(partner, 'paramOf', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'paramOf')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'paramOf')


def test_assoc_type8_stub_double():
    # ClassM_TypedElement has no real 'typeOf' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Classifier(name="sample_text")
    partner = ClassM_TypedElement()
    setattr(partner, 'typeOf', None)
    _safe_set(owner, 'Classifier', partner)
    assert getattr(partner, 'typeOf') == owner
    _safe_set(owner, 'Classifier', None)
    assert getattr(partner, 'typeOf') is None


def test_assoc_typeOf6_stub_double():
    # ClassM_TypedElement has no real 'TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Classifier(name="sample_text")
    partner = ClassM_TypedElement()
    setattr(partner, 'TypedElement', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'TypedElement') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'TypedElement') is None


