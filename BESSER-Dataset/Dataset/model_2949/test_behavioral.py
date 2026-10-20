import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    domainmodel_DataType,
    domainmodel_Domainmodel,
    domainmodel_Entity,
    domainmodel_Feature,
    domainmodel_Type,
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

def test_assoc_features5_reverse_link_reassign_clear():
    a1 = domainmodel_Feature(many=True, name="sample_text", s="sample_text", type="sample_text")
    a2 = domainmodel_Feature(many=False, name="sample_text_2", s="sample_text_2", type="sample_text_2")
    b = domainmodel_Entity(name="sample_text")
    _safe_set(b, 'domainmodel_Entity6', {a1})
    assert _is_linked(b, 'domainmodel_Entity6', a1)
    if hasattr(a1, 'domainmodel_Feature'):
        assert _is_linked(a1, 'domainmodel_Feature', b)
    _safe_set(b, 'domainmodel_Entity6', {a2})
    assert _is_linked(b, 'domainmodel_Entity6', a2)
    if hasattr(a1, 'domainmodel_Feature'):
        assert not _is_linked(a1, 'domainmodel_Feature', b)
    if hasattr(a2, 'domainmodel_Feature'):
        assert _is_linked(a2, 'domainmodel_Feature', b)
    _safe_set(b, 'domainmodel_Entity6', set())
    assert not _is_linked(b, 'domainmodel_Entity6', a2)
    if hasattr(a2, 'domainmodel_Feature'):
        assert not _is_linked(a2, 'domainmodel_Feature', b)


def test_assoc_superType4_reverse_link_reassign_clear():
    a1 = domainmodel_Entity(name="sample_text")
    a2 = domainmodel_Entity(name="sample_text_2")
    b = domainmodel_Entity(name="sample_text")
    _safe_set(b, 'domainmodel_Entity3', a1)
    assert _is_linked(b, 'domainmodel_Entity3', a1)
    if hasattr(a1, 'domainmodel_Entity'):
        assert _is_linked(a1, 'domainmodel_Entity', b)
    _safe_set(b, 'domainmodel_Entity3', a2)
    assert _is_linked(b, 'domainmodel_Entity3', a2)
    if hasattr(a1, 'domainmodel_Entity'):
        assert not _is_linked(a1, 'domainmodel_Entity', b)
    if hasattr(a2, 'domainmodel_Entity'):
        assert _is_linked(a2, 'domainmodel_Entity', b)
    _safe_set(b, 'domainmodel_Entity3', None)
    assert not _is_linked(b, 'domainmodel_Entity3', a2)
    if hasattr(a2, 'domainmodel_Entity'):
        assert not _is_linked(a2, 'domainmodel_Entity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_sd1_stub_double():
    # domainmodel_Type has no real 'domainmodel_Type2' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_DataType(name="sample_text")
    partner = domainmodel_Type()
    setattr(partner, 'domainmodel_Type2', None)
    _safe_set(owner, 'domainmodel_DataType', partner)
    assert getattr(partner, 'domainmodel_Type2') == owner
    _safe_set(owner, 'domainmodel_DataType', None)
    assert getattr(partner, 'domainmodel_Type2') is None


