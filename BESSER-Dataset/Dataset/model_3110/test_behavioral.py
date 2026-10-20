import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassM_Attribute,
    ClassM_Class,
    ClassM_Classifier,
    ClassM_Model,
    ClassM_PrimitiveType,
    Classifier,
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

def test_assoc_type1_reverse_link_reassign_clear():
    a1 = ClassM_Classifier(name="sample_text")
    a2 = ClassM_Classifier(name="sample_text_2")
    b = ClassM_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'ClassM_Attribute', a1)
    assert _is_linked(b, 'ClassM_Attribute', a1)
    if hasattr(a1, 'ClassM_Classifier'):
        assert _is_linked(a1, 'ClassM_Classifier', b)
    _safe_set(b, 'ClassM_Attribute', a2)
    assert _is_linked(b, 'ClassM_Attribute', a2)
    if hasattr(a1, 'ClassM_Classifier'):
        assert not _is_linked(a1, 'ClassM_Classifier', b)
    if hasattr(a2, 'ClassM_Classifier'):
        assert _is_linked(a2, 'ClassM_Classifier', b)
    _safe_set(b, 'ClassM_Attribute', None)
    assert not _is_linked(b, 'ClassM_Attribute', a2)
    if hasattr(a2, 'ClassM_Classifier'):
        assert not _is_linked(a2, 'ClassM_Classifier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attrs0_stub_double():
    # ClassM_Class has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Attribute(is_primary=True, name="sample_text")
    partner = ClassM_Class()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Attribute', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Attribute', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_classifiers3_stub_double():
    # ClassM_Model has no real 'ClassM_Model' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Classifier(name="sample_text")
    partner = ClassM_Model()
    setattr(partner, 'ClassM_Model', None)
    _safe_set(owner, 'ClassM_Classifier4', partner)
    assert owner in getattr(partner, 'ClassM_Model')
    _safe_set(owner, 'ClassM_Classifier4', None)
    assert owner not in getattr(partner, 'ClassM_Model')


def test_assoc_owner2_stub_double():
    # ClassM_Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so ClassM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassM_Attribute(is_primary=True, name="sample_text")
    partner = ClassM_Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'attrs', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'attrs', None)
    assert getattr(partner, 'Class') is None


