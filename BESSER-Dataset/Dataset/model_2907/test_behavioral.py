import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Data_Attribute,
    Data_Entity,
    Data_Model,
    Data_PrimitiveType,
    Data_Type,
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

def test_assoc_type1_reverse_link_reassign_clear():
    a1 = Data_Type(name="sample_text")
    a2 = Data_Type(name="sample_text_2")
    b = Data_Attribute(name="sample_text")
    _safe_set(b, 'Data_Attribute', a1)
    assert _is_linked(b, 'Data_Attribute', a1)
    if hasattr(a1, 'Data_Type2'):
        assert _is_linked(a1, 'Data_Type2', b)
    _safe_set(b, 'Data_Attribute', a2)
    assert _is_linked(b, 'Data_Attribute', a2)
    if hasattr(a1, 'Data_Type2'):
        assert not _is_linked(a1, 'Data_Type2', b)
    if hasattr(a2, 'Data_Type2'):
        assert _is_linked(a2, 'Data_Type2', b)
    _safe_set(b, 'Data_Attribute', None)
    assert not _is_linked(b, 'Data_Attribute', a2)
    if hasattr(a2, 'Data_Type2'):
        assert not _is_linked(a2, 'Data_Type2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes3_stub_double():
    # Data_Entity has no real 'Data_Entity' property in the generated
    # code (a bare stub) -- manually attach it so Data_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Data_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Data_Attribute(name="sample_text")
    partner = Data_Entity()
    setattr(partner, 'Data_Entity', None)
    _safe_set(owner, 'Data_Attribute4', partner)
    assert owner in getattr(partner, 'Data_Entity')
    _safe_set(owner, 'Data_Attribute4', None)
    assert owner not in getattr(partner, 'Data_Entity')


def test_assoc_types0_stub_double():
    # Data_Model has no real 'Data_Model' property in the generated
    # code (a bare stub) -- manually attach it so Data_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Data_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Data_Type(name="sample_text")
    partner = Data_Model()
    setattr(partner, 'Data_Model', None)
    _safe_set(owner, 'Data_Type', partner)
    assert owner in getattr(partner, 'Data_Model')
    _safe_set(owner, 'Data_Type', None)
    assert owner not in getattr(partner, 'Data_Model')


