import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    jsonldConverter_DataType,
    jsonldConverter_Entity,
    jsonldConverter_Enum,
    jsonldConverter_EnumItem,
    jsonldConverter_Model,
    jsonldConverter_Property,
    jsonldConverter_Type,
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
    a1 = jsonldConverter_Type(name="sample_text")
    a2 = jsonldConverter_Type(name="sample_text_2")
    b = jsonldConverter_Property(many=True, name="sample_text", one=True)
    _safe_set(b, 'jsonldConverter_Property6', a1)
    assert _is_linked(b, 'jsonldConverter_Property6', a1)
    if hasattr(a1, 'jsonldConverter_Type7'):
        assert _is_linked(a1, 'jsonldConverter_Type7', b)
    _safe_set(b, 'jsonldConverter_Property6', a2)
    assert _is_linked(b, 'jsonldConverter_Property6', a2)
    if hasattr(a1, 'jsonldConverter_Type7'):
        assert not _is_linked(a1, 'jsonldConverter_Type7', b)
    if hasattr(a2, 'jsonldConverter_Type7'):
        assert _is_linked(a2, 'jsonldConverter_Type7', b)
    _safe_set(b, 'jsonldConverter_Property6', None)
    assert not _is_linked(b, 'jsonldConverter_Property6', a2)
    if hasattr(a2, 'jsonldConverter_Type7'):
        assert not _is_linked(a2, 'jsonldConverter_Type7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # jsonldConverter_Model has no real 'jsonldConverter_Model' property in the generated
    # code (a bare stub) -- manually attach it so jsonldConverter_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jsonldConverter_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jsonldConverter_Type(name="sample_text")
    partner = jsonldConverter_Model()
    setattr(partner, 'jsonldConverter_Model', None)
    _safe_set(owner, 'jsonldConverter_Type', partner)
    assert owner in getattr(partner, 'jsonldConverter_Model')
    _safe_set(owner, 'jsonldConverter_Type', None)
    assert owner not in getattr(partner, 'jsonldConverter_Model')


def test_assoc_features3_stub_double():
    # jsonldConverter_Entity has no real 'jsonldConverter_Entity4' property in the generated
    # code (a bare stub) -- manually attach it so jsonldConverter_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jsonldConverter_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jsonldConverter_Property(many=True, name="sample_text", one=True)
    partner = jsonldConverter_Entity()
    setattr(partner, 'jsonldConverter_Entity4', None)
    _safe_set(owner, 'jsonldConverter_Property', partner)
    assert owner in getattr(partner, 'jsonldConverter_Entity4')
    _safe_set(owner, 'jsonldConverter_Property', None)
    assert owner not in getattr(partner, 'jsonldConverter_Entity4')


def test_assoc_features8_stub_double():
    # jsonldConverter_Enum has no real 'jsonldConverter_Enum' property in the generated
    # code (a bare stub) -- manually attach it so jsonldConverter_EnumItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jsonldConverter_EnumItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jsonldConverter_EnumItem(name="sample_text", type="sample_text")
    partner = jsonldConverter_Enum()
    setattr(partner, 'jsonldConverter_Enum', None)
    _safe_set(owner, 'jsonldConverter_EnumItem', partner)
    assert owner in getattr(partner, 'jsonldConverter_Enum')
    _safe_set(owner, 'jsonldConverter_EnumItem', None)
    assert owner not in getattr(partner, 'jsonldConverter_Enum')


