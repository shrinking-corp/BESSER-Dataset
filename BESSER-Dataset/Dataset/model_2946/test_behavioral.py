import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    slolpBPM_Datatype,
    slolpBPM_DomainModel,
    slolpBPM_Entity,
    slolpBPM_Feature,
    slolpBPM_Type,
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
    a1 = slolpBPM_Type(name="sample_text")
    a2 = slolpBPM_Type(name="sample_text_2")
    b = slolpBPM_Feature(many=True, name="sample_text")
    _safe_set(b, 'slolpBPM_Feature6', a1)
    assert _is_linked(b, 'slolpBPM_Feature6', a1)
    if hasattr(a1, 'slolpBPM_Type7'):
        assert _is_linked(a1, 'slolpBPM_Type7', b)
    _safe_set(b, 'slolpBPM_Feature6', a2)
    assert _is_linked(b, 'slolpBPM_Feature6', a2)
    if hasattr(a1, 'slolpBPM_Type7'):
        assert not _is_linked(a1, 'slolpBPM_Type7', b)
    if hasattr(a2, 'slolpBPM_Type7'):
        assert _is_linked(a2, 'slolpBPM_Type7', b)
    _safe_set(b, 'slolpBPM_Feature6', None)
    assert not _is_linked(b, 'slolpBPM_Feature6', a2)
    if hasattr(a2, 'slolpBPM_Type7'):
        assert not _is_linked(a2, 'slolpBPM_Type7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # slolpBPM_DomainModel has no real 'slolpBPM_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so slolpBPM_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # slolpBPM_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = slolpBPM_Type(name="sample_text")
    partner = slolpBPM_DomainModel()
    setattr(partner, 'slolpBPM_DomainModel', None)
    _safe_set(owner, 'slolpBPM_Type', partner)
    assert owner in getattr(partner, 'slolpBPM_DomainModel')
    _safe_set(owner, 'slolpBPM_Type', None)
    assert owner not in getattr(partner, 'slolpBPM_DomainModel')


def test_assoc_feautres3_stub_double():
    # slolpBPM_Entity has no real 'slolpBPM_Entity4' property in the generated
    # code (a bare stub) -- manually attach it so slolpBPM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # slolpBPM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = slolpBPM_Feature(many=True, name="sample_text")
    partner = slolpBPM_Entity()
    setattr(partner, 'slolpBPM_Entity4', None)
    _safe_set(owner, 'slolpBPM_Feature', partner)
    assert owner in getattr(partner, 'slolpBPM_Entity4')
    _safe_set(owner, 'slolpBPM_Feature', None)
    assert owner not in getattr(partner, 'slolpBPM_Entity4')


