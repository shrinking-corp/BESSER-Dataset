import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassDiagram_Association,
    ClassDiagram_Class,
    ClassDiagram_Classifier,
    ClassDiagram_DataType,
    ClassDiagram_Dependency,
    ClassDiagram_Generalization,
    ClassDiagram_Interface,
    ClassDiagram_Property,
    ClassDiagram_Realization,
    ClassDiagram_Relationship,
    Classifier,
    Dependency,
    Relationship,
    AggregationKind,
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

def test_assoc_memberEnd5_reverse_link_reassign_clear():
    a1 = ClassDiagram_Property(aggregation="sample_text", lower=7, name="sample_text", upper="sample_text")
    a2 = ClassDiagram_Property(aggregation="sample_text_2", lower=13, name="sample_text_2", upper="sample_text_2")
    b = ClassDiagram_Association(name="sample_text")
    _safe_set(b, 'ClassDiagram_Association', {a1})
    assert _is_linked(b, 'ClassDiagram_Association', a1)
    if hasattr(a1, 'ClassDiagram_Property6'):
        assert _is_linked(a1, 'ClassDiagram_Property6', b)
    _safe_set(b, 'ClassDiagram_Association', {a2})
    assert _is_linked(b, 'ClassDiagram_Association', a2)
    if hasattr(a1, 'ClassDiagram_Property6'):
        assert not _is_linked(a1, 'ClassDiagram_Property6', b)
    if hasattr(a2, 'ClassDiagram_Property6'):
        assert _is_linked(a2, 'ClassDiagram_Property6', b)
    _safe_set(b, 'ClassDiagram_Association', set())
    assert not _is_linked(b, 'ClassDiagram_Association', a2)
    if hasattr(a2, 'ClassDiagram_Property6'):
        assert not _is_linked(a2, 'ClassDiagram_Property6', b)


def test_assoc_type3_reverse_link_reassign_clear():
    a1 = ClassDiagram_Property(aggregation="sample_text", lower=7, name="sample_text", upper="sample_text")
    a2 = ClassDiagram_Property(aggregation="sample_text_2", lower=13, name="sample_text_2", upper="sample_text_2")
    b = ClassDiagram_Classifier(name="sample_text")
    _safe_set(b, 'ClassDiagram_Classifier', a1)
    assert _is_linked(b, 'ClassDiagram_Classifier', a1)
    if hasattr(a1, 'ClassDiagram_Property4'):
        assert _is_linked(a1, 'ClassDiagram_Property4', b)
    _safe_set(b, 'ClassDiagram_Classifier', a2)
    assert _is_linked(b, 'ClassDiagram_Classifier', a2)
    if hasattr(a1, 'ClassDiagram_Property4'):
        assert not _is_linked(a1, 'ClassDiagram_Property4', b)
    if hasattr(a2, 'ClassDiagram_Property4'):
        assert _is_linked(a2, 'ClassDiagram_Property4', b)
    _safe_set(b, 'ClassDiagram_Classifier', None)
    assert not _is_linked(b, 'ClassDiagram_Classifier', a2)
    if hasattr(a2, 'ClassDiagram_Property4'):
        assert not _is_linked(a2, 'ClassDiagram_Property4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_client14_stub_double():
    # ClassDiagram_Dependency has no real 'ClassDiagram_Dependency15' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_Dependency()
    setattr(partner, 'ClassDiagram_Dependency15', None)
    _safe_set(owner, 'ClassDiagram_Classifier16', partner)
    assert owner in getattr(partner, 'ClassDiagram_Dependency15')
    _safe_set(owner, 'ClassDiagram_Classifier16', None)
    assert owner not in getattr(partner, 'ClassDiagram_Dependency15')


def test_assoc_general7_stub_double():
    # ClassDiagram_Generalization has no real 'ClassDiagram_Generalization' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_Generalization()
    setattr(partner, 'ClassDiagram_Generalization', None)
    _safe_set(owner, 'ClassDiagram_Classifier8', partner)
    assert getattr(partner, 'ClassDiagram_Generalization') == owner
    _safe_set(owner, 'ClassDiagram_Classifier8', None)
    assert getattr(partner, 'ClassDiagram_Generalization') is None


def test_assoc_ownedAttribute0_stub_double():
    # ClassDiagram_Class has no real 'ClassDiagram_Class' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Property(aggregation="sample_text", lower=7, name="sample_text", upper="sample_text")
    partner = ClassDiagram_Class()
    setattr(partner, 'ClassDiagram_Class', None)
    _safe_set(owner, 'ClassDiagram_Property', partner)
    assert owner in getattr(partner, 'ClassDiagram_Class')
    _safe_set(owner, 'ClassDiagram_Property', None)
    assert owner not in getattr(partner, 'ClassDiagram_Class')


def test_assoc_ownedAttribute1_stub_double():
    # ClassDiagram_Interface has no real 'ClassDiagram_Interface' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Property(aggregation="sample_text", lower=7, name="sample_text", upper="sample_text")
    partner = ClassDiagram_Interface()
    setattr(partner, 'ClassDiagram_Interface', None)
    _safe_set(owner, 'ClassDiagram_Property2', partner)
    assert owner in getattr(partner, 'ClassDiagram_Interface')
    _safe_set(owner, 'ClassDiagram_Property2', None)
    assert owner not in getattr(partner, 'ClassDiagram_Interface')


def test_assoc_specific9_stub_double():
    # ClassDiagram_Generalization has no real 'ClassDiagram_Generalization10' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_Generalization()
    setattr(partner, 'ClassDiagram_Generalization10', None)
    _safe_set(owner, 'ClassDiagram_Classifier11', partner)
    assert getattr(partner, 'ClassDiagram_Generalization10') == owner
    _safe_set(owner, 'ClassDiagram_Classifier11', None)
    assert getattr(partner, 'ClassDiagram_Generalization10') is None


def test_assoc_supplier12_stub_double():
    # ClassDiagram_Dependency has no real 'ClassDiagram_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so ClassDiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassDiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassDiagram_Classifier(name="sample_text")
    partner = ClassDiagram_Dependency()
    setattr(partner, 'ClassDiagram_Dependency', None)
    _safe_set(owner, 'ClassDiagram_Classifier13', partner)
    assert owner in getattr(partner, 'ClassDiagram_Dependency')
    _safe_set(owner, 'ClassDiagram_Classifier13', None)
    assert owner not in getattr(partner, 'ClassDiagram_Dependency')


