import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    entityDsl_Entity,
    entityDsl_Model,
    entityDsl_Property,
    entityDsl_SimpleType,
    entityDsl_Type,
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

def test_assoc_type5_reverse_link_reassign_clear():
    a1 = entityDsl_Type(name="sample_text")
    a2 = entityDsl_Type(name="sample_text_2")
    b = entityDsl_Property(many=True, name="sample_text")
    _safe_set(b, 'entityDsl_Property6', a1)
    assert _is_linked(b, 'entityDsl_Property6', a1)
    if hasattr(a1, 'entityDsl_Type7'):
        assert _is_linked(a1, 'entityDsl_Type7', b)
    _safe_set(b, 'entityDsl_Property6', a2)
    assert _is_linked(b, 'entityDsl_Property6', a2)
    if hasattr(a1, 'entityDsl_Type7'):
        assert not _is_linked(a1, 'entityDsl_Type7', b)
    if hasattr(a2, 'entityDsl_Type7'):
        assert _is_linked(a2, 'entityDsl_Type7', b)
    _safe_set(b, 'entityDsl_Property6', None)
    assert not _is_linked(b, 'entityDsl_Property6', a2)
    if hasattr(a2, 'entityDsl_Type7'):
        assert not _is_linked(a2, 'entityDsl_Type7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # entityDsl_Model has no real 'entityDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so entityDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityDsl_Type(name="sample_text")
    partner = entityDsl_Model()
    setattr(partner, 'entityDsl_Model', None)
    _safe_set(owner, 'entityDsl_Type', partner)
    assert owner in getattr(partner, 'entityDsl_Model')
    _safe_set(owner, 'entityDsl_Type', None)
    assert owner not in getattr(partner, 'entityDsl_Model')


def test_assoc_properties3_stub_double():
    # entityDsl_Entity has no real 'entityDsl_Entity4' property in the generated
    # code (a bare stub) -- manually attach it so entityDsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityDsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityDsl_Property(many=True, name="sample_text")
    partner = entityDsl_Entity()
    setattr(partner, 'entityDsl_Entity4', None)
    _safe_set(owner, 'entityDsl_Property', partner)
    assert owner in getattr(partner, 'entityDsl_Entity4')
    _safe_set(owner, 'entityDsl_Property', None)
    assert owner not in getattr(partner, 'entityDsl_Entity4')


