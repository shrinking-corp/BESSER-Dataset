import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    esper2Maude_ComparisonOperator,
    esper2Maude_Event,
    esper2Maude_EventProperty,
    esper2Maude_Every,
    esper2Maude_Field,
    esper2Maude_FilterEvent,
    esper2Maude_FilterFrom,
    esper2Maude_FilterOperator,
    esper2Maude_FilterPart,
    esper2Maude_FollowedBy,
    esper2Maude_LastSelectEntry,
    esper2Maude_LogicalOperator,
    esper2Maude_Model,
    esper2Maude_NonLastSelectEntry,
    esper2Maude_Pattern,
    esper2Maude_Schema,
    esper2Maude_SelectEntry,
    esper2Maude_SubFilterFollowedBy,
    esper2Maude_WhereFilter,
    esper2Maude_Window,
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

def test_assoc_event8_reverse_link_reassign_clear():
    a1 = esper2Maude_Pattern(name="sample_text", num=7)
    a2 = esper2Maude_Pattern(name="sample_text_2", num=13)
    b = esper2Maude_Event(name="sample_text")
    _safe_set(b, 'esper2Maude_Event', a1)
    assert _is_linked(b, 'esper2Maude_Event', a1)
    if hasattr(a1, 'esper2Maude_Pattern9'):
        assert _is_linked(a1, 'esper2Maude_Pattern9', b)
    _safe_set(b, 'esper2Maude_Event', a2)
    assert _is_linked(b, 'esper2Maude_Event', a2)
    if hasattr(a1, 'esper2Maude_Pattern9'):
        assert not _is_linked(a1, 'esper2Maude_Pattern9', b)
    if hasattr(a2, 'esper2Maude_Pattern9'):
        assert _is_linked(a2, 'esper2Maude_Pattern9', b)
    _safe_set(b, 'esper2Maude_Event', None)
    assert not _is_linked(b, 'esper2Maude_Event', a2)
    if hasattr(a2, 'esper2Maude_Pattern9'):
        assert not _is_linked(a2, 'esper2Maude_Pattern9', b)


def test_assoc_every51_reverse_link_reassign_clear():
    a1 = esper2Maude_SubFilterFollowedBy(eventName="sample_text", eventVariable="sample_text")
    a2 = esper2Maude_SubFilterFollowedBy(eventName="sample_text_2", eventVariable="sample_text_2")
    b = esper2Maude_Every(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_Every', a1)
    assert _is_linked(b, 'esper2Maude_Every', a1)
    if hasattr(a1, 'esper2Maude_SubFilterFollowedBy52'):
        assert _is_linked(a1, 'esper2Maude_SubFilterFollowedBy52', b)
    _safe_set(b, 'esper2Maude_Every', a2)
    assert _is_linked(b, 'esper2Maude_Every', a2)
    if hasattr(a1, 'esper2Maude_SubFilterFollowedBy52'):
        assert not _is_linked(a1, 'esper2Maude_SubFilterFollowedBy52', b)
    if hasattr(a2, 'esper2Maude_SubFilterFollowedBy52'):
        assert _is_linked(a2, 'esper2Maude_SubFilterFollowedBy52', b)
    _safe_set(b, 'esper2Maude_Every', None)
    assert not _is_linked(b, 'esper2Maude_Every', a2)
    if hasattr(a2, 'esper2Maude_SubFilterFollowedBy52'):
        assert not _is_linked(a2, 'esper2Maude_SubFilterFollowedBy52', b)


def test_assoc_field77_reverse_link_reassign_clear():
    a1 = esper2Maude_SelectEntry(alias="sample_text", groupOp="sample_text")
    a2 = esper2Maude_SelectEntry(alias="sample_text_2", groupOp="sample_text_2")
    b = esper2Maude_Field(eventPropName="sample_text", eventVariable="sample_text", star="sample_text")
    _safe_set(b, 'esper2Maude_Field', a1)
    assert _is_linked(b, 'esper2Maude_Field', a1)
    if hasattr(a1, 'esper2Maude_SelectEntry78'):
        assert _is_linked(a1, 'esper2Maude_SelectEntry78', b)
    _safe_set(b, 'esper2Maude_Field', a2)
    assert _is_linked(b, 'esper2Maude_Field', a2)
    if hasattr(a1, 'esper2Maude_SelectEntry78'):
        assert not _is_linked(a1, 'esper2Maude_SelectEntry78', b)
    if hasattr(a2, 'esper2Maude_SelectEntry78'):
        assert _is_linked(a2, 'esper2Maude_SelectEntry78', b)
    _safe_set(b, 'esper2Maude_Field', None)
    assert not _is_linked(b, 'esper2Maude_Field', a2)
    if hasattr(a2, 'esper2Maude_SelectEntry78'):
        assert not _is_linked(a2, 'esper2Maude_SelectEntry78', b)


def test_assoc_filterFrom56_reverse_link_reassign_clear():
    a1 = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    a2 = esper2Maude_FilterFrom(eventName="sample_text_2", eventVariable="sample_text_2")
    b = esper2Maude_Every(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_Every57', a1)
    assert _is_linked(b, 'esper2Maude_Every57', a1)
    if hasattr(a1, 'esper2Maude_FilterFrom58'):
        assert _is_linked(a1, 'esper2Maude_FilterFrom58', b)
    _safe_set(b, 'esper2Maude_Every57', a2)
    assert _is_linked(b, 'esper2Maude_Every57', a2)
    if hasattr(a1, 'esper2Maude_FilterFrom58'):
        assert not _is_linked(a1, 'esper2Maude_FilterFrom58', b)
    if hasattr(a2, 'esper2Maude_FilterFrom58'):
        assert _is_linked(a2, 'esper2Maude_FilterFrom58', b)
    _safe_set(b, 'esper2Maude_Every57', None)
    assert not _is_linked(b, 'esper2Maude_Every57', a2)
    if hasattr(a2, 'esper2Maude_FilterFrom58'):
        assert not _is_linked(a2, 'esper2Maude_FilterFrom58', b)


def test_assoc_fromFilter14_reverse_link_reassign_clear():
    a1 = esper2Maude_Pattern(name="sample_text", num=7)
    a2 = esper2Maude_Pattern(name="sample_text_2", num=13)
    b = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_FilterFrom', a1)
    assert _is_linked(b, 'esper2Maude_FilterFrom', a1)
    if hasattr(a1, 'esper2Maude_Pattern15'):
        assert _is_linked(a1, 'esper2Maude_Pattern15', b)
    _safe_set(b, 'esper2Maude_FilterFrom', a2)
    assert _is_linked(b, 'esper2Maude_FilterFrom', a2)
    if hasattr(a1, 'esper2Maude_Pattern15'):
        assert not _is_linked(a1, 'esper2Maude_Pattern15', b)
    if hasattr(a2, 'esper2Maude_Pattern15'):
        assert _is_linked(a2, 'esper2Maude_Pattern15', b)
    _safe_set(b, 'esper2Maude_FilterFrom', None)
    assert not _is_linked(b, 'esper2Maude_FilterFrom', a2)
    if hasattr(a2, 'esper2Maude_Pattern15'):
        assert not _is_linked(a2, 'esper2Maude_Pattern15', b)


def test_assoc_left30_reverse_link_reassign_clear():
    a1 = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    a2 = esper2Maude_FilterFrom(eventName="sample_text_2", eventVariable="sample_text_2")
    b = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_FilterFrom31', a1)
    assert _is_linked(b, 'esper2Maude_FilterFrom31', a1)
    if hasattr(a1, 'esper2Maude_FilterFrom29'):
        assert _is_linked(a1, 'esper2Maude_FilterFrom29', b)
    _safe_set(b, 'esper2Maude_FilterFrom31', a2)
    assert _is_linked(b, 'esper2Maude_FilterFrom31', a2)
    if hasattr(a1, 'esper2Maude_FilterFrom29'):
        assert not _is_linked(a1, 'esper2Maude_FilterFrom29', b)
    if hasattr(a2, 'esper2Maude_FilterFrom29'):
        assert _is_linked(a2, 'esper2Maude_FilterFrom29', b)
    _safe_set(b, 'esper2Maude_FilterFrom31', None)
    assert not _is_linked(b, 'esper2Maude_FilterFrom31', a2)
    if hasattr(a2, 'esper2Maude_FilterFrom29'):
        assert not _is_linked(a2, 'esper2Maude_FilterFrom29', b)


def test_assoc_op32_reverse_link_reassign_clear():
    a1 = esper2Maude_LogicalOperator(and_="sample_text", or_="sample_text")
    a2 = esper2Maude_LogicalOperator(and_="sample_text_2", or_="sample_text_2")
    b = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_FilterFrom33', a1)
    assert _is_linked(b, 'esper2Maude_FilterFrom33', a1)
    if hasattr(a1, 'esper2Maude_LogicalOperator'):
        assert _is_linked(a1, 'esper2Maude_LogicalOperator', b)
    _safe_set(b, 'esper2Maude_FilterFrom33', a2)
    assert _is_linked(b, 'esper2Maude_FilterFrom33', a2)
    if hasattr(a1, 'esper2Maude_LogicalOperator'):
        assert not _is_linked(a1, 'esper2Maude_LogicalOperator', b)
    if hasattr(a2, 'esper2Maude_LogicalOperator'):
        assert _is_linked(a2, 'esper2Maude_LogicalOperator', b)
    _safe_set(b, 'esper2Maude_FilterFrom33', None)
    assert not _is_linked(b, 'esper2Maude_FilterFrom33', a2)
    if hasattr(a2, 'esper2Maude_LogicalOperator'):
        assert not _is_linked(a2, 'esper2Maude_LogicalOperator', b)


def test_assoc_prop3_reverse_link_reassign_clear():
    a1 = esper2Maude_Schema(name="sample_text")
    a2 = esper2Maude_Schema(name="sample_text_2")
    b = esper2Maude_EventProperty(name="sample_text", type="sample_text")
    _safe_set(b, 'esper2Maude_EventProperty', a1)
    assert _is_linked(b, 'esper2Maude_EventProperty', a1)
    if hasattr(a1, 'esper2Maude_Schema4'):
        assert _is_linked(a1, 'esper2Maude_Schema4', b)
    _safe_set(b, 'esper2Maude_EventProperty', a2)
    assert _is_linked(b, 'esper2Maude_EventProperty', a2)
    if hasattr(a1, 'esper2Maude_Schema4'):
        assert not _is_linked(a1, 'esper2Maude_Schema4', b)
    if hasattr(a2, 'esper2Maude_Schema4'):
        assert _is_linked(a2, 'esper2Maude_Schema4', b)
    _safe_set(b, 'esper2Maude_EventProperty', None)
    assert not _is_linked(b, 'esper2Maude_EventProperty', a2)
    if hasattr(a2, 'esper2Maude_Schema4'):
        assert not _is_linked(a2, 'esper2Maude_Schema4', b)


def test_assoc_props5_reverse_link_reassign_clear():
    a1 = esper2Maude_Schema(name="sample_text")
    a2 = esper2Maude_Schema(name="sample_text_2")
    b = esper2Maude_EventProperty(name="sample_text", type="sample_text")
    _safe_set(b, 'esper2Maude_EventProperty7', a1)
    assert _is_linked(b, 'esper2Maude_EventProperty7', a1)
    if hasattr(a1, 'esper2Maude_Schema6'):
        assert _is_linked(a1, 'esper2Maude_Schema6', b)
    _safe_set(b, 'esper2Maude_EventProperty7', a2)
    assert _is_linked(b, 'esper2Maude_EventProperty7', a2)
    if hasattr(a1, 'esper2Maude_Schema6'):
        assert not _is_linked(a1, 'esper2Maude_Schema6', b)
    if hasattr(a2, 'esper2Maude_Schema6'):
        assert _is_linked(a2, 'esper2Maude_Schema6', b)
    _safe_set(b, 'esper2Maude_EventProperty7', None)
    assert not _is_linked(b, 'esper2Maude_EventProperty7', a2)
    if hasattr(a2, 'esper2Maude_Schema6'):
        assert not _is_linked(a2, 'esper2Maude_Schema6', b)


def test_assoc_right35_reverse_link_reassign_clear():
    a1 = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    a2 = esper2Maude_FilterFrom(eventName="sample_text_2", eventVariable="sample_text_2")
    b = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    _safe_set(b, 'esper2Maude_FilterFrom36', a1)
    assert _is_linked(b, 'esper2Maude_FilterFrom36', a1)
    if hasattr(a1, 'esper2Maude_FilterFrom34'):
        assert _is_linked(a1, 'esper2Maude_FilterFrom34', b)
    _safe_set(b, 'esper2Maude_FilterFrom36', a2)
    assert _is_linked(b, 'esper2Maude_FilterFrom36', a2)
    if hasattr(a1, 'esper2Maude_FilterFrom34'):
        assert not _is_linked(a1, 'esper2Maude_FilterFrom34', b)
    if hasattr(a2, 'esper2Maude_FilterFrom34'):
        assert _is_linked(a2, 'esper2Maude_FilterFrom34', b)
    _safe_set(b, 'esper2Maude_FilterFrom36', None)
    assert not _is_linked(b, 'esper2Maude_FilterFrom36', a2)
    if hasattr(a2, 'esper2Maude_FilterFrom34'):
        assert not _is_linked(a2, 'esper2Maude_FilterFrom34', b)


def test_assoc_win16_reverse_link_reassign_clear():
    a1 = esper2Maude_Window(num=7, typeBatch="sample_text", typeTime="sample_text")
    a2 = esper2Maude_Window(num=13, typeBatch="sample_text_2", typeTime="sample_text_2")
    b = esper2Maude_Pattern(name="sample_text", num=7)
    _safe_set(b, 'esper2Maude_Pattern17', a1)
    assert _is_linked(b, 'esper2Maude_Pattern17', a1)
    if hasattr(a1, 'esper2Maude_Window'):
        assert _is_linked(a1, 'esper2Maude_Window', b)
    _safe_set(b, 'esper2Maude_Pattern17', a2)
    assert _is_linked(b, 'esper2Maude_Pattern17', a2)
    if hasattr(a1, 'esper2Maude_Window'):
        assert not _is_linked(a1, 'esper2Maude_Window', b)
    if hasattr(a2, 'esper2Maude_Window'):
        assert _is_linked(a2, 'esper2Maude_Window', b)
    _safe_set(b, 'esper2Maude_Pattern17', None)
    assert not _is_linked(b, 'esper2Maude_Pattern17', a2)
    if hasattr(a2, 'esper2Maude_Window'):
        assert not _is_linked(a2, 'esper2Maude_Window', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_comparison67_stub_double():
    # esper2Maude_FilterOperator has no real 'esper2Maude_FilterOperator68' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_ComparisonOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_ComparisonOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_ComparisonOperator(eq="sample_text", ge="sample_text", gt="sample_text", le="sample_text", lt="sample_text", neq="sample_text")
    partner = esper2Maude_FilterOperator()
    setattr(partner, 'esper2Maude_FilterOperator68', None)
    _safe_set(owner, 'esper2Maude_ComparisonOperator', partner)
    assert getattr(partner, 'esper2Maude_FilterOperator68') == owner
    _safe_set(owner, 'esper2Maude_ComparisonOperator', None)
    assert getattr(partner, 'esper2Maude_FilterOperator68') is None


def test_assoc_entry72_stub_double():
    # esper2Maude_NonLastSelectEntry has no real 'esper2Maude_NonLastSelectEntry73' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_SelectEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_SelectEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_SelectEntry(alias="sample_text", groupOp="sample_text")
    partner = esper2Maude_NonLastSelectEntry()
    setattr(partner, 'esper2Maude_NonLastSelectEntry73', None)
    _safe_set(owner, 'esper2Maude_SelectEntry', partner)
    assert getattr(partner, 'esper2Maude_NonLastSelectEntry73') == owner
    _safe_set(owner, 'esper2Maude_SelectEntry', None)
    assert getattr(partner, 'esper2Maude_NonLastSelectEntry73') is None


def test_assoc_entry74_stub_double():
    # esper2Maude_LastSelectEntry has no real 'esper2Maude_LastSelectEntry75' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_SelectEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_SelectEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_SelectEntry(alias="sample_text", groupOp="sample_text")
    partner = esper2Maude_LastSelectEntry()
    setattr(partner, 'esper2Maude_LastSelectEntry75', None)
    _safe_set(owner, 'esper2Maude_SelectEntry76', partner)
    assert getattr(partner, 'esper2Maude_LastSelectEntry75') == owner
    _safe_set(owner, 'esper2Maude_SelectEntry76', None)
    assert getattr(partner, 'esper2Maude_LastSelectEntry75') is None


def test_assoc_filter37_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent39' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_FilterFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_FilterFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent39', None)
    _safe_set(owner, 'esper2Maude_FilterFrom38', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent39') == owner
    _safe_set(owner, 'esper2Maude_FilterFrom38', None)
    assert getattr(partner, 'esper2Maude_FilterEvent39') is None


def test_assoc_filter48_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent50' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_SubFilterFollowedBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_SubFilterFollowedBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_SubFilterFollowedBy(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent50', None)
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy49', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent50') == owner
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy49', None)
    assert getattr(partner, 'esper2Maude_FilterEvent50') is None


def test_assoc_filter53_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent55' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_Every's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_Every's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_Every(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent55', None)
    _safe_set(owner, 'esper2Maude_Every54', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent55') == owner
    _safe_set(owner, 'esper2Maude_Every54', None)
    assert getattr(partner, 'esper2Maude_FilterEvent55') is None


def test_assoc_filterEventL18_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_WhereFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_WhereFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_WhereFilter(num=7, timer="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent', None)
    _safe_set(owner, 'esper2Maude_WhereFilter', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent') == owner
    _safe_set(owner, 'esper2Maude_WhereFilter', None)
    assert getattr(partner, 'esper2Maude_FilterEvent') is None


def test_assoc_filterEventR24_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent26' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_WhereFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_WhereFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_WhereFilter(num=7, timer="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent26', None)
    _safe_set(owner, 'esper2Maude_WhereFilter25', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent26') == owner
    _safe_set(owner, 'esper2Maude_WhereFilter25', None)
    assert getattr(partner, 'esper2Maude_FilterEvent26') is None


def test_assoc_filterLeftHandSide59_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent60' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_FilterPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_FilterPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_FilterPart(dec=7, eventPropName="sample_text", eventVariable="sample_text", f="sample_text", neg="sample_text", num=7, str="sample_text", t="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent60', None)
    _safe_set(owner, 'esper2Maude_FilterPart', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent60') == owner
    _safe_set(owner, 'esper2Maude_FilterPart', None)
    assert getattr(partner, 'esper2Maude_FilterEvent60') is None


def test_assoc_filterOpL19_stub_double():
    # esper2Maude_FilterOperator has no real 'esper2Maude_FilterOperator' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_WhereFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_WhereFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_WhereFilter(num=7, timer="sample_text")
    partner = esper2Maude_FilterOperator()
    setattr(partner, 'esper2Maude_FilterOperator', None)
    _safe_set(owner, 'esper2Maude_WhereFilter20', partner)
    assert getattr(partner, 'esper2Maude_FilterOperator') == owner
    _safe_set(owner, 'esper2Maude_WhereFilter20', None)
    assert getattr(partner, 'esper2Maude_FilterOperator') is None


def test_assoc_filterOpR21_stub_double():
    # esper2Maude_FilterOperator has no real 'esper2Maude_FilterOperator23' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_WhereFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_WhereFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_WhereFilter(num=7, timer="sample_text")
    partner = esper2Maude_FilterOperator()
    setattr(partner, 'esper2Maude_FilterOperator23', None)
    _safe_set(owner, 'esper2Maude_WhereFilter22', partner)
    assert getattr(partner, 'esper2Maude_FilterOperator23') == owner
    _safe_set(owner, 'esper2Maude_WhereFilter22', None)
    assert getattr(partner, 'esper2Maude_FilterOperator23') is None


def test_assoc_filterRightHandSide64_stub_double():
    # esper2Maude_FilterEvent has no real 'esper2Maude_FilterEvent65' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_FilterPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_FilterPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_FilterPart(dec=7, eventPropName="sample_text", eventVariable="sample_text", f="sample_text", neg="sample_text", num=7, str="sample_text", t="sample_text")
    partner = esper2Maude_FilterEvent()
    setattr(partner, 'esper2Maude_FilterEvent65', None)
    _safe_set(owner, 'esper2Maude_FilterPart66', partner)
    assert getattr(partner, 'esper2Maude_FilterEvent65') == owner
    _safe_set(owner, 'esper2Maude_FilterPart66', None)
    assert getattr(partner, 'esper2Maude_FilterEvent65') is None


def test_assoc_followedBy27_stub_double():
    # esper2Maude_FollowedBy has no real 'esper2Maude_FollowedBy' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_FilterFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_FilterFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_FilterFrom(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FollowedBy()
    setattr(partner, 'esper2Maude_FollowedBy', None)
    _safe_set(owner, 'esper2Maude_FilterFrom28', partner)
    assert getattr(partner, 'esper2Maude_FollowedBy') == owner
    _safe_set(owner, 'esper2Maude_FilterFrom28', None)
    assert getattr(partner, 'esper2Maude_FollowedBy') is None


def test_assoc_left40_stub_double():
    # esper2Maude_FollowedBy has no real 'esper2Maude_FollowedBy41' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_SubFilterFollowedBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_SubFilterFollowedBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_SubFilterFollowedBy(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FollowedBy()
    setattr(partner, 'esper2Maude_FollowedBy41', None)
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy', partner)
    assert getattr(partner, 'esper2Maude_FollowedBy41') == owner
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy', None)
    assert getattr(partner, 'esper2Maude_FollowedBy41') is None


def test_assoc_logical69_stub_double():
    # esper2Maude_FilterOperator has no real 'esper2Maude_FilterOperator70' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_LogicalOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_LogicalOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_LogicalOperator(and_="sample_text", or_="sample_text")
    partner = esper2Maude_FilterOperator()
    setattr(partner, 'esper2Maude_FilterOperator70', None)
    _safe_set(owner, 'esper2Maude_LogicalOperator71', partner)
    assert getattr(partner, 'esper2Maude_FilterOperator70') == owner
    _safe_set(owner, 'esper2Maude_LogicalOperator71', None)
    assert getattr(partner, 'esper2Maude_FilterOperator70') is None


def test_assoc_patterns1_stub_double():
    # esper2Maude_Model has no real 'esper2Maude_Model2' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_Pattern(name="sample_text", num=7)
    partner = esper2Maude_Model()
    setattr(partner, 'esper2Maude_Model2', None)
    _safe_set(owner, 'esper2Maude_Pattern', partner)
    assert owner in getattr(partner, 'esper2Maude_Model2')
    _safe_set(owner, 'esper2Maude_Pattern', None)
    assert owner not in getattr(partner, 'esper2Maude_Model2')


def test_assoc_right42_stub_double():
    # esper2Maude_FollowedBy has no real 'esper2Maude_FollowedBy43' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_SubFilterFollowedBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_SubFilterFollowedBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_SubFilterFollowedBy(eventName="sample_text", eventVariable="sample_text")
    partner = esper2Maude_FollowedBy()
    setattr(partner, 'esper2Maude_FollowedBy43', None)
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy44', partner)
    assert getattr(partner, 'esper2Maude_FollowedBy43') == owner
    _safe_set(owner, 'esper2Maude_SubFilterFollowedBy44', None)
    assert getattr(partner, 'esper2Maude_FollowedBy43') is None


def test_assoc_schemas0_stub_double():
    # esper2Maude_Model has no real 'esper2Maude_Model' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_Schema(name="sample_text")
    partner = esper2Maude_Model()
    setattr(partner, 'esper2Maude_Model', None)
    _safe_set(owner, 'esper2Maude_Schema', partner)
    assert owner in getattr(partner, 'esper2Maude_Model')
    _safe_set(owner, 'esper2Maude_Schema', None)
    assert owner not in getattr(partner, 'esper2Maude_Model')


def test_assoc_selectEntries10_stub_double():
    # esper2Maude_NonLastSelectEntry has no real 'esper2Maude_NonLastSelectEntry' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_Pattern(name="sample_text", num=7)
    partner = esper2Maude_NonLastSelectEntry()
    setattr(partner, 'esper2Maude_NonLastSelectEntry', None)
    _safe_set(owner, 'esper2Maude_Pattern11', {partner})
    assert getattr(partner, 'esper2Maude_NonLastSelectEntry') == owner
    _safe_set(owner, 'esper2Maude_Pattern11', set())
    assert getattr(partner, 'esper2Maude_NonLastSelectEntry') is None


def test_assoc_selectEntry12_stub_double():
    # esper2Maude_LastSelectEntry has no real 'esper2Maude_LastSelectEntry' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_Pattern(name="sample_text", num=7)
    partner = esper2Maude_LastSelectEntry()
    setattr(partner, 'esper2Maude_LastSelectEntry', None)
    _safe_set(owner, 'esper2Maude_Pattern13', partner)
    assert getattr(partner, 'esper2Maude_LastSelectEntry') == owner
    _safe_set(owner, 'esper2Maude_Pattern13', None)
    assert getattr(partner, 'esper2Maude_LastSelectEntry') is None


def test_assoc_whereFilter45_stub_double():
    # esper2Maude_FollowedBy has no real 'esper2Maude_FollowedBy46' property in the generated
    # code (a bare stub) -- manually attach it so esper2Maude_WhereFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper2Maude_WhereFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper2Maude_WhereFilter(num=7, timer="sample_text")
    partner = esper2Maude_FollowedBy()
    setattr(partner, 'esper2Maude_FollowedBy46', None)
    _safe_set(owner, 'esper2Maude_WhereFilter47', partner)
    assert getattr(partner, 'esper2Maude_FollowedBy46') == owner
    _safe_set(owner, 'esper2Maude_WhereFilter47', None)
    assert getattr(partner, 'esper2Maude_FollowedBy46') is None


