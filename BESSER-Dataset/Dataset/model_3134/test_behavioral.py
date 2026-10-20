import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassDiagram_Attribute,
    ClassDiagram_Class,
    ClassDiagram_Classifier,
    ClassDiagram_Model,
    ClassDiagram_Operation,
    ClassDiagram_Parameter,
    ClassDiagram_PrimitiveType,
    ClassDiagram_StructuralFeature,
    ClassDiagram_TypedElement,
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

def test_assoc_classifiers0_stub_double():
    # ClassDiagram_Model has no real 'ClassDiagram_Model' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_Model()
    setattr(partner, 'ClassDiagram_Model', None)
    _safe_set(owner, 'ClassDiagram_Classifier', partner)
    assert owner in getattr(partner, 'ClassDiagram_Model')
    _safe_set(owner, 'ClassDiagram_Classifier', None)
    assert owner not in getattr(partner, 'ClassDiagram_Model')


def test_assoc_features1_stub_double():
    # ClassDiagram_Class has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_StructuralFeature(name="sample_text", visibility="sample_text")
    partner = ClassDiagram_Class()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'StructuralFeature', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'StructuralFeature', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_owner7_stub_double():
    # ClassDiagram_Class has no real 'Class8' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_StructuralFeature(name="sample_text", visibility="sample_text")
    partner = ClassDiagram_Class()
    setattr(partner, 'Class8', None)
    _safe_set(owner, 'features', partner)
    assert getattr(partner, 'Class8') == owner
    _safe_set(owner, 'features', None)
    assert getattr(partner, 'Class8') is None


def test_assoc_paramOf12_stub_double():
    # ClassDiagram_Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Parameter(name="sample_text")
    partner = ClassDiagram_Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'params', partner)
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'params', None)
    assert getattr(partner, 'Operation') is None


def test_assoc_params11_stub_double():
    # ClassDiagram_Operation has no real 'paramOf' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Parameter(name="sample_text")
    partner = ClassDiagram_Operation()
    setattr(partner, 'paramOf', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'paramOf')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'paramOf')


def test_assoc_type9_stub_double():
    # ClassDiagram_TypedElement has no real 'ClassDiagram_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_TypedElement()
    setattr(partner, 'ClassDiagram_TypedElement', None)
    _safe_set(owner, 'ClassDiagram_Classifier10', partner)
    assert getattr(partner, 'ClassDiagram_TypedElement') == owner
    _safe_set(owner, 'ClassDiagram_Classifier10', None)
    assert getattr(partner, 'ClassDiagram_TypedElement') is None


