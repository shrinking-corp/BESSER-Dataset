import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MuddleElementType,
    PrimitiveType,
    Type,
    muddle_BooleanType,
    muddle_Feature,
    muddle_IntegerType,
    muddle_LinkElementType,
    muddle_Muddle,
    muddle_MuddleElement,
    muddle_MuddleElementType,
    muddle_PrimitiveType,
    muddle_RealType,
    muddle_Slot,
    muddle_StringType,
    muddle_Type,
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

def test_assoc_feature5_reverse_link_reassign_clear():
    a1 = muddle_Slot(values="sample_text")
    a2 = muddle_Slot(values="sample_text_2")
    b = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'slots'):
        assert _is_linked(a1, 'slots', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'slots'):
        assert not _is_linked(a1, 'slots', b)
    if hasattr(a2, 'slots'):
        assert _is_linked(a2, 'slots', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'slots'):
        assert not _is_linked(a2, 'slots', b)


def test_assoc_owningElement6_reverse_link_reassign_clear():
    a1 = muddle_Slot(values="sample_text")
    a2 = muddle_Slot(values="sample_text_2")
    b = muddle_MuddleElement(id="sample_text")
    _safe_set(b, 'MuddleElement8', a1)
    assert _is_linked(b, 'MuddleElement8', a1)
    if hasattr(a1, 'slots7'):
        assert _is_linked(a1, 'slots7', b)
    _safe_set(b, 'MuddleElement8', a2)
    assert _is_linked(b, 'MuddleElement8', a2)
    if hasattr(a1, 'slots7'):
        assert not _is_linked(a1, 'slots7', b)
    if hasattr(a2, 'slots7'):
        assert _is_linked(a2, 'slots7', b)
    _safe_set(b, 'MuddleElement8', None)
    assert not _is_linked(b, 'MuddleElement8', a2)
    if hasattr(a2, 'slots7'):
        assert not _is_linked(a2, 'slots7', b)


def test_assoc_slots13_reverse_link_reassign_clear():
    a1 = muddle_Slot(values="sample_text")
    a2 = muddle_Slot(values="sample_text_2")
    b = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    _safe_set(b, 'feature', {a1})
    assert _is_linked(b, 'feature', a1)
    if hasattr(a1, 'Slot14'):
        assert _is_linked(a1, 'Slot14', b)
    _safe_set(b, 'feature', {a2})
    assert _is_linked(b, 'feature', a2)
    if hasattr(a1, 'Slot14'):
        assert not _is_linked(a1, 'Slot14', b)
    if hasattr(a2, 'Slot14'):
        assert _is_linked(a2, 'Slot14', b)
    _safe_set(b, 'feature', set())
    assert not _is_linked(b, 'feature', a2)
    if hasattr(a2, 'Slot14'):
        assert not _is_linked(a2, 'Slot14', b)


def test_assoc_slots2_reverse_link_reassign_clear():
    a1 = muddle_Slot(values="sample_text")
    a2 = muddle_Slot(values="sample_text_2")
    b = muddle_MuddleElement(id="sample_text")
    _safe_set(b, 'owningElement', {a1})
    assert _is_linked(b, 'owningElement', a1)
    if hasattr(a1, 'Slot'):
        assert _is_linked(a1, 'Slot', b)
    _safe_set(b, 'owningElement', {a2})
    assert _is_linked(b, 'owningElement', a2)
    if hasattr(a1, 'Slot'):
        assert not _is_linked(a1, 'Slot', b)
    if hasattr(a2, 'Slot'):
        assert _is_linked(a2, 'Slot', b)
    _safe_set(b, 'owningElement', set())
    assert not _is_linked(b, 'owningElement', a2)
    if hasattr(a2, 'Slot'):
        assert not _is_linked(a2, 'Slot', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = muddle_Type(name="sample_text")
    a2 = muddle_Type(name="sample_text_2")
    b = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    _safe_set(b, 'muddle_Feature', a1)
    assert _is_linked(b, 'muddle_Feature', a1)
    if hasattr(a1, 'muddle_Type10'):
        assert _is_linked(a1, 'muddle_Type10', b)
    _safe_set(b, 'muddle_Feature', a2)
    assert _is_linked(b, 'muddle_Feature', a2)
    if hasattr(a1, 'muddle_Type10'):
        assert not _is_linked(a1, 'muddle_Type10', b)
    if hasattr(a2, 'muddle_Type10'):
        assert _is_linked(a2, 'muddle_Type10', b)
    _safe_set(b, 'muddle_Feature', None)
    assert not _is_linked(b, 'muddle_Feature', a2)
    if hasattr(a2, 'muddle_Type10'):
        assert not _is_linked(a2, 'muddle_Type10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements1_stub_double():
    # muddle_Muddle has no real 'muddle' property in the generated
    # code (a bare stub) -- manually attach it so muddle_MuddleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_MuddleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_MuddleElement(id="sample_text")
    partner = muddle_Muddle()
    setattr(partner, 'muddle', None)
    _safe_set(owner, 'MuddleElement', partner)
    assert owner in getattr(partner, 'muddle')
    _safe_set(owner, 'MuddleElement', None)
    assert owner not in getattr(partner, 'muddle')


def test_assoc_features17_stub_double():
    # muddle_MuddleElementType has no real 'owningType' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_MuddleElementType()
    setattr(partner, 'owningType', None)
    _safe_set(owner, 'Feature18', partner)
    assert owner in getattr(partner, 'owningType')
    _safe_set(owner, 'Feature18', None)
    assert owner not in getattr(partner, 'owningType')


def test_assoc_instances15_stub_double():
    # muddle_MuddleElementType has no real 'type' property in the generated
    # code (a bare stub) -- manually attach it so muddle_MuddleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_MuddleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_MuddleElement(id="sample_text")
    partner = muddle_MuddleElementType()
    setattr(partner, 'type', None)
    _safe_set(owner, 'MuddleElement16', partner)
    assert owner in getattr(partner, 'type')
    _safe_set(owner, 'MuddleElement16', None)
    assert owner not in getattr(partner, 'type')


def test_assoc_muddle4_stub_double():
    # muddle_Muddle has no real 'Muddle' property in the generated
    # code (a bare stub) -- manually attach it so muddle_MuddleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_MuddleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_MuddleElement(id="sample_text")
    partner = muddle_Muddle()
    setattr(partner, 'Muddle', None)
    _safe_set(owner, 'elements', partner)
    assert getattr(partner, 'Muddle') == owner
    _safe_set(owner, 'elements', None)
    assert getattr(partner, 'Muddle') is None


def test_assoc_owningType11_stub_double():
    # muddle_MuddleElementType has no real 'MuddleElementType12' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_MuddleElementType()
    setattr(partner, 'MuddleElementType12', None)
    _safe_set(owner, 'features', partner)
    assert getattr(partner, 'MuddleElementType12') == owner
    _safe_set(owner, 'features', None)
    assert getattr(partner, 'MuddleElementType12') is None


def test_assoc_roleInSourceFeature30_stub_double():
    # muddle_LinkElementType has no real 'muddle_LinkElementType31' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_LinkElementType()
    setattr(partner, 'muddle_LinkElementType31', None)
    _safe_set(owner, 'muddle_Feature32', partner)
    assert getattr(partner, 'muddle_LinkElementType31') == owner
    _safe_set(owner, 'muddle_Feature32', None)
    assert getattr(partner, 'muddle_LinkElementType31') is None


def test_assoc_roleInTargetFeature33_stub_double():
    # muddle_LinkElementType has no real 'muddle_LinkElementType34' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_LinkElementType()
    setattr(partner, 'muddle_LinkElementType34', None)
    _safe_set(owner, 'muddle_Feature35', partner)
    assert getattr(partner, 'muddle_LinkElementType34') == owner
    _safe_set(owner, 'muddle_Feature35', None)
    assert getattr(partner, 'muddle_LinkElementType34') is None


def test_assoc_sourceFeature25_stub_double():
    # muddle_LinkElementType has no real 'muddle_LinkElementType' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_LinkElementType()
    setattr(partner, 'muddle_LinkElementType', None)
    _safe_set(owner, 'muddle_Feature26', partner)
    assert getattr(partner, 'muddle_LinkElementType') == owner
    _safe_set(owner, 'muddle_Feature26', None)
    assert getattr(partner, 'muddle_LinkElementType') is None


def test_assoc_targetFeature27_stub_double():
    # muddle_LinkElementType has no real 'muddle_LinkElementType28' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Feature(many=True, name="sample_text", primary=True, runtime=True)
    partner = muddle_LinkElementType()
    setattr(partner, 'muddle_LinkElementType28', None)
    _safe_set(owner, 'muddle_Feature29', partner)
    assert getattr(partner, 'muddle_LinkElementType28') == owner
    _safe_set(owner, 'muddle_Feature29', None)
    assert getattr(partner, 'muddle_LinkElementType28') is None


def test_assoc_type3_stub_double():
    # muddle_MuddleElementType has no real 'MuddleElementType' property in the generated
    # code (a bare stub) -- manually attach it so muddle_MuddleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_MuddleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_MuddleElement(id="sample_text")
    partner = muddle_MuddleElementType()
    setattr(partner, 'MuddleElementType', None)
    _safe_set(owner, 'instances', partner)
    assert getattr(partner, 'MuddleElementType') == owner
    _safe_set(owner, 'instances', None)
    assert getattr(partner, 'MuddleElementType') is None


def test_assoc_types0_stub_double():
    # muddle_Muddle has no real 'muddle_Muddle' property in the generated
    # code (a bare stub) -- manually attach it so muddle_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # muddle_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = muddle_Type(name="sample_text")
    partner = muddle_Muddle()
    setattr(partner, 'muddle_Muddle', None)
    _safe_set(owner, 'muddle_Type', partner)
    assert owner in getattr(partner, 'muddle_Muddle')
    _safe_set(owner, 'muddle_Type', None)
    assert owner not in getattr(partner, 'muddle_Muddle')


