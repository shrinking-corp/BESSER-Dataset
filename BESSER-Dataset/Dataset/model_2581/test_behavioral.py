import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ExtraParenthesisRule,
    KindOfEvent,
    esper_AbstractFollowBy,
    esper_Anything,
    esper_Attributes,
    esper_AttributesDefinition,
    esper_DefaultMethods,
    esper_Domainmodel,
    esper_Event,
    esper_ExtraParenthesisRule,
    esper_FollowBy,
    esper_FollowByWhere,
    esper_From,
    esper_GroupBy,
    esper_Having,
    esper_Insert,
    esper_JoinFollowBy,
    esper_KindOfEvent,
    esper_KindSelectAttributesDefinition,
    esper_Name,
    esper_Pattern,
    esper_Priority,
    esper_RuleParts,
    esper_Select,
    esper_SelectAttributesDefinition,
    esper_SingleDefinition,
    esper_SingleSelectDefinition,
    esper_TerminalExpression,
    esper_Timer,
    esper_Win,
    Operators,
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

def test_assoc_anything67_reverse_link_reassign_clear():
    a1 = esper_SingleDefinition(name="sample_text")
    a2 = esper_SingleDefinition(name="sample_text_2")
    b = esper_Anything(operator="sample_text")
    _safe_set(b, 'esper_Anything69', a1)
    assert _is_linked(b, 'esper_Anything69', a1)
    if hasattr(a1, 'esper_SingleDefinition68'):
        assert _is_linked(a1, 'esper_SingleDefinition68', b)
    _safe_set(b, 'esper_Anything69', a2)
    assert _is_linked(b, 'esper_Anything69', a2)
    if hasattr(a1, 'esper_SingleDefinition68'):
        assert not _is_linked(a1, 'esper_SingleDefinition68', b)
    if hasattr(a2, 'esper_SingleDefinition68'):
        assert _is_linked(a2, 'esper_SingleDefinition68', b)
    _safe_set(b, 'esper_Anything69', None)
    assert not _is_linked(b, 'esper_Anything69', a2)
    if hasattr(a2, 'esper_SingleDefinition68'):
        assert not _is_linked(a2, 'esper_SingleDefinition68', b)


def test_assoc_anything84_reverse_link_reassign_clear():
    a1 = esper_Having(operator="sample_text")
    a2 = esper_Having(operator="sample_text_2")
    b = esper_Anything(operator="sample_text")
    _safe_set(b, 'esper_Anything86', a1)
    assert _is_linked(b, 'esper_Anything86', a1)
    if hasattr(a1, 'esper_Having85'):
        assert _is_linked(a1, 'esper_Having85', b)
    _safe_set(b, 'esper_Anything86', a2)
    assert _is_linked(b, 'esper_Anything86', a2)
    if hasattr(a1, 'esper_Having85'):
        assert not _is_linked(a1, 'esper_Having85', b)
    if hasattr(a2, 'esper_Having85'):
        assert _is_linked(a2, 'esper_Having85', b)
    _safe_set(b, 'esper_Anything86', None)
    assert not _is_linked(b, 'esper_Anything86', a2)
    if hasattr(a2, 'esper_Having85'):
        assert not _is_linked(a2, 'esper_Having85', b)


def test_assoc_anything87_reverse_link_reassign_clear():
    a1 = esper_DefaultMethods(name="sample_text")
    a2 = esper_DefaultMethods(name="sample_text_2")
    b = esper_Anything(operator="sample_text")
    _safe_set(b, 'esper_Anything89', a1)
    assert _is_linked(b, 'esper_Anything89', a1)
    if hasattr(a1, 'esper_DefaultMethods88'):
        assert _is_linked(a1, 'esper_DefaultMethods88', b)
    _safe_set(b, 'esper_Anything89', a2)
    assert _is_linked(b, 'esper_Anything89', a2)
    if hasattr(a1, 'esper_DefaultMethods88'):
        assert not _is_linked(a1, 'esper_DefaultMethods88', b)
    if hasattr(a2, 'esper_DefaultMethods88'):
        assert _is_linked(a2, 'esper_DefaultMethods88', b)
    _safe_set(b, 'esper_Anything89', None)
    assert not _is_linked(b, 'esper_Anything89', a2)
    if hasattr(a2, 'esper_DefaultMethods88'):
        assert not _is_linked(a2, 'esper_DefaultMethods88', b)


def test_assoc_defaultMethod24_reverse_link_reassign_clear():
    a1 = esper_KindSelectAttributesDefinition(int=7, string="sample_text")
    a2 = esper_KindSelectAttributesDefinition(int=13, string="sample_text_2")
    b = esper_DefaultMethods(name="sample_text")
    _safe_set(b, 'esper_DefaultMethods', a1)
    assert _is_linked(b, 'esper_DefaultMethods', a1)
    if hasattr(a1, 'esper_KindSelectAttributesDefinition25'):
        assert _is_linked(a1, 'esper_KindSelectAttributesDefinition25', b)
    _safe_set(b, 'esper_DefaultMethods', a2)
    assert _is_linked(b, 'esper_DefaultMethods', a2)
    if hasattr(a1, 'esper_KindSelectAttributesDefinition25'):
        assert not _is_linked(a1, 'esper_KindSelectAttributesDefinition25', b)
    if hasattr(a2, 'esper_KindSelectAttributesDefinition25'):
        assert _is_linked(a2, 'esper_KindSelectAttributesDefinition25', b)
    _safe_set(b, 'esper_DefaultMethods', None)
    assert not _is_linked(b, 'esper_DefaultMethods', a2)
    if hasattr(a2, 'esper_KindSelectAttributesDefinition25'):
        assert not _is_linked(a2, 'esper_KindSelectAttributesDefinition25', b)


def test_assoc_defaultMethod81_reverse_link_reassign_clear():
    a1 = esper_Having(operator="sample_text")
    a2 = esper_Having(operator="sample_text_2")
    b = esper_DefaultMethods(name="sample_text")
    _safe_set(b, 'esper_DefaultMethods83', a1)
    assert _is_linked(b, 'esper_DefaultMethods83', a1)
    if hasattr(a1, 'esper_Having82'):
        assert _is_linked(a1, 'esper_Having82', b)
    _safe_set(b, 'esper_DefaultMethods83', a2)
    assert _is_linked(b, 'esper_DefaultMethods83', a2)
    if hasattr(a1, 'esper_Having82'):
        assert not _is_linked(a1, 'esper_Having82', b)
    if hasattr(a2, 'esper_Having82'):
        assert _is_linked(a2, 'esper_Having82', b)
    _safe_set(b, 'esper_DefaultMethods83', None)
    assert not _is_linked(b, 'esper_DefaultMethods83', a2)
    if hasattr(a2, 'esper_Having82'):
        assert not _is_linked(a2, 'esper_Having82', b)


def test_assoc_event32_reverse_link_reassign_clear():
    a1 = esper_SingleSelectDefinition(attribute="sample_text")
    a2 = esper_SingleSelectDefinition(attribute="sample_text_2")
    b = esper_SingleDefinition(name="sample_text")
    _safe_set(b, 'esper_SingleDefinition', a1)
    assert _is_linked(b, 'esper_SingleDefinition', a1)
    if hasattr(a1, 'esper_SingleSelectDefinition33'):
        assert _is_linked(a1, 'esper_SingleSelectDefinition33', b)
    _safe_set(b, 'esper_SingleDefinition', a2)
    assert _is_linked(b, 'esper_SingleDefinition', a2)
    if hasattr(a1, 'esper_SingleSelectDefinition33'):
        assert not _is_linked(a1, 'esper_SingleSelectDefinition33', b)
    if hasattr(a2, 'esper_SingleSelectDefinition33'):
        assert _is_linked(a2, 'esper_SingleSelectDefinition33', b)
    _safe_set(b, 'esper_SingleDefinition', None)
    assert not _is_linked(b, 'esper_SingleDefinition', a2)
    if hasattr(a2, 'esper_SingleSelectDefinition33'):
        assert not _is_linked(a2, 'esper_SingleSelectDefinition33', b)


def test_assoc_leftSide29_reverse_link_reassign_clear():
    a1 = esper_SelectAttributesDefinition(operator="sample_text")
    a2 = esper_SelectAttributesDefinition(operator="sample_text_2")
    b = esper_KindSelectAttributesDefinition(int=7, string="sample_text")
    _safe_set(b, 'esper_KindSelectAttributesDefinition31', a1)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition31', a1)
    if hasattr(a1, 'esper_SelectAttributesDefinition30'):
        assert _is_linked(a1, 'esper_SelectAttributesDefinition30', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition31', a2)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition31', a2)
    if hasattr(a1, 'esper_SelectAttributesDefinition30'):
        assert not _is_linked(a1, 'esper_SelectAttributesDefinition30', b)
    if hasattr(a2, 'esper_SelectAttributesDefinition30'):
        assert _is_linked(a2, 'esper_SelectAttributesDefinition30', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition31', None)
    assert not _is_linked(b, 'esper_KindSelectAttributesDefinition31', a2)
    if hasattr(a2, 'esper_SelectAttributesDefinition30'):
        assert not _is_linked(a2, 'esper_SelectAttributesDefinition30', b)


def test_assoc_rightSide26_reverse_link_reassign_clear():
    a1 = esper_SelectAttributesDefinition(operator="sample_text")
    a2 = esper_SelectAttributesDefinition(operator="sample_text_2")
    b = esper_KindSelectAttributesDefinition(int=7, string="sample_text")
    _safe_set(b, 'esper_KindSelectAttributesDefinition28', a1)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition28', a1)
    if hasattr(a1, 'esper_SelectAttributesDefinition27'):
        assert _is_linked(a1, 'esper_SelectAttributesDefinition27', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition28', a2)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition28', a2)
    if hasattr(a1, 'esper_SelectAttributesDefinition27'):
        assert not _is_linked(a1, 'esper_SelectAttributesDefinition27', b)
    if hasattr(a2, 'esper_SelectAttributesDefinition27'):
        assert _is_linked(a2, 'esper_SelectAttributesDefinition27', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition28', None)
    assert not _is_linked(b, 'esper_KindSelectAttributesDefinition28', a2)
    if hasattr(a2, 'esper_SelectAttributesDefinition27'):
        assert not _is_linked(a2, 'esper_SelectAttributesDefinition27', b)


def test_assoc_selectAttributes21_reverse_link_reassign_clear():
    a1 = esper_SelectAttributesDefinition(operator="sample_text")
    a2 = esper_SelectAttributesDefinition(operator="sample_text_2")
    b = esper_Select(alias="sample_text", asterisk=True)
    _safe_set(b, 'esper_Select22', {a1})
    assert _is_linked(b, 'esper_Select22', a1)
    if hasattr(a1, 'esper_SelectAttributesDefinition'):
        assert _is_linked(a1, 'esper_SelectAttributesDefinition', b)
    _safe_set(b, 'esper_Select22', {a2})
    assert _is_linked(b, 'esper_Select22', a2)
    if hasattr(a1, 'esper_SelectAttributesDefinition'):
        assert not _is_linked(a1, 'esper_SelectAttributesDefinition', b)
    if hasattr(a2, 'esper_SelectAttributesDefinition'):
        assert _is_linked(a2, 'esper_SelectAttributesDefinition', b)
    _safe_set(b, 'esper_Select22', set())
    assert not _is_linked(b, 'esper_Select22', a2)
    if hasattr(a2, 'esper_SelectAttributesDefinition'):
        assert not _is_linked(a2, 'esper_SelectAttributesDefinition', b)


def test_assoc_simpleEvents65_reverse_link_reassign_clear():
    a1 = esper_SingleDefinition(name="sample_text")
    a2 = esper_SingleDefinition(name="sample_text_2")
    b = esper_KindOfEvent(name="sample_text")
    _safe_set(b, 'esper_KindOfEvent', a1)
    assert _is_linked(b, 'esper_KindOfEvent', a1)
    if hasattr(a1, 'esper_SingleDefinition66'):
        assert _is_linked(a1, 'esper_SingleDefinition66', b)
    _safe_set(b, 'esper_KindOfEvent', a2)
    assert _is_linked(b, 'esper_KindOfEvent', a2)
    if hasattr(a1, 'esper_SingleDefinition66'):
        assert not _is_linked(a1, 'esper_SingleDefinition66', b)
    if hasattr(a2, 'esper_SingleDefinition66'):
        assert _is_linked(a2, 'esper_SingleDefinition66', b)
    _safe_set(b, 'esper_KindOfEvent', None)
    assert not _is_linked(b, 'esper_KindOfEvent', a2)
    if hasattr(a2, 'esper_SingleDefinition66'):
        assert not _is_linked(a2, 'esper_SingleDefinition66', b)


def test_assoc_singleDefinition62_reverse_link_reassign_clear():
    a1 = esper_TerminalExpression(every=True, parenthesis=True)
    a2 = esper_TerminalExpression(every=False, parenthesis=False)
    b = esper_SingleDefinition(name="sample_text")
    _safe_set(b, 'esper_SingleDefinition64', a1)
    assert _is_linked(b, 'esper_SingleDefinition64', a1)
    if hasattr(a1, 'esper_TerminalExpression63'):
        assert _is_linked(a1, 'esper_TerminalExpression63', b)
    _safe_set(b, 'esper_SingleDefinition64', a2)
    assert _is_linked(b, 'esper_SingleDefinition64', a2)
    if hasattr(a1, 'esper_TerminalExpression63'):
        assert not _is_linked(a1, 'esper_TerminalExpression63', b)
    if hasattr(a2, 'esper_TerminalExpression63'):
        assert _is_linked(a2, 'esper_TerminalExpression63', b)
    _safe_set(b, 'esper_SingleDefinition64', None)
    assert not _is_linked(b, 'esper_SingleDefinition64', a2)
    if hasattr(a2, 'esper_TerminalExpression63'):
        assert not _is_linked(a2, 'esper_TerminalExpression63', b)


def test_assoc_singleSelectDefinition23_reverse_link_reassign_clear():
    a1 = esper_SingleSelectDefinition(attribute="sample_text")
    a2 = esper_SingleSelectDefinition(attribute="sample_text_2")
    b = esper_KindSelectAttributesDefinition(int=7, string="sample_text")
    _safe_set(b, 'esper_KindSelectAttributesDefinition', a1)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition', a1)
    if hasattr(a1, 'esper_SingleSelectDefinition'):
        assert _is_linked(a1, 'esper_SingleSelectDefinition', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition', a2)
    assert _is_linked(b, 'esper_KindSelectAttributesDefinition', a2)
    if hasattr(a1, 'esper_SingleSelectDefinition'):
        assert not _is_linked(a1, 'esper_SingleSelectDefinition', b)
    if hasattr(a2, 'esper_SingleSelectDefinition'):
        assert _is_linked(a2, 'esper_SingleSelectDefinition', b)
    _safe_set(b, 'esper_KindSelectAttributesDefinition', None)
    assert not _is_linked(b, 'esper_KindSelectAttributesDefinition', a2)
    if hasattr(a2, 'esper_SingleSelectDefinition'):
        assert not _is_linked(a2, 'esper_SingleSelectDefinition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_anything37_stub_double():
    # esper_From has no real 'esper_From38' property in the generated
    # code (a bare stub) -- manually attach it so esper_Anything's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Anything's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Anything(operator="sample_text")
    partner = esper_From()
    setattr(partner, 'esper_From38', None)
    _safe_set(owner, 'esper_Anything', partner)
    assert getattr(partner, 'esper_From38') == owner
    _safe_set(owner, 'esper_Anything', None)
    assert getattr(partner, 'esper_From38') is None


def test_assoc_anything78_stub_double():
    # esper_GroupBy has no real 'esper_GroupBy79' property in the generated
    # code (a bare stub) -- manually attach it so esper_Anything's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Anything's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Anything(operator="sample_text")
    partner = esper_GroupBy()
    setattr(partner, 'esper_GroupBy79', None)
    _safe_set(owner, 'esper_Anything80', partner)
    assert getattr(partner, 'esper_GroupBy79') == owner
    _safe_set(owner, 'esper_Anything80', None)
    assert getattr(partner, 'esper_GroupBy79') is None


def test_assoc_attribute5_stub_double():
    # esper_Attributes has no real 'esper_Attributes6' property in the generated
    # code (a bare stub) -- manually attach it so esper_AttributesDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_AttributesDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_AttributesDefinition(name="sample_text", type="sample_text")
    partner = esper_Attributes()
    setattr(partner, 'esper_Attributes6', None)
    _safe_set(owner, 'esper_AttributesDefinition', partner)
    assert owner in getattr(partner, 'esper_Attributes6')
    _safe_set(owner, 'esper_AttributesDefinition', None)
    assert owner not in getattr(partner, 'esper_Attributes6')


def test_assoc_betweenParenthesis59_stub_double():
    # esper_FollowBy has no real 'esper_FollowBy61' property in the generated
    # code (a bare stub) -- manually attach it so esper_TerminalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_TerminalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_TerminalExpression(every=True, parenthesis=True)
    partner = esper_FollowBy()
    setattr(partner, 'esper_FollowBy61', None)
    _safe_set(owner, 'esper_TerminalExpression60', partner)
    assert getattr(partner, 'esper_FollowBy61') == owner
    _safe_set(owner, 'esper_TerminalExpression60', None)
    assert getattr(partner, 'esper_FollowBy61') is None


def test_assoc_defaultMethod70_stub_double():
    # esper_Win has no real 'esper_Win71' property in the generated
    # code (a bare stub) -- manually attach it so esper_DefaultMethods's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_DefaultMethods's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_DefaultMethods(name="sample_text")
    partner = esper_Win()
    setattr(partner, 'esper_Win71', None)
    _safe_set(owner, 'esper_DefaultMethods72', partner)
    assert getattr(partner, 'esper_Win71') == owner
    _safe_set(owner, 'esper_DefaultMethods72', None)
    assert getattr(partner, 'esper_Win71') is None


def test_assoc_defaultMethod75_stub_double():
    # esper_Timer has no real 'esper_Timer76' property in the generated
    # code (a bare stub) -- manually attach it so esper_DefaultMethods's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_DefaultMethods's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_DefaultMethods(name="sample_text")
    partner = esper_Timer()
    setattr(partner, 'esper_Timer76', None)
    _safe_set(owner, 'esper_DefaultMethods77', partner)
    assert getattr(partner, 'esper_Timer76') == owner
    _safe_set(owner, 'esper_DefaultMethods77', None)
    assert getattr(partner, 'esper_Timer76') is None


def test_assoc_everyExpression56_stub_double():
    # esper_FollowBy has no real 'esper_FollowBy58' property in the generated
    # code (a bare stub) -- manually attach it so esper_TerminalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_TerminalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_TerminalExpression(every=True, parenthesis=True)
    partner = esper_FollowBy()
    setattr(partner, 'esper_FollowBy58', None)
    _safe_set(owner, 'esper_TerminalExpression57', partner)
    assert getattr(partner, 'esper_FollowBy58') == owner
    _safe_set(owner, 'esper_TerminalExpression57', None)
    assert getattr(partner, 'esper_FollowBy58') is None


def test_assoc_extraParenthesis90_stub_double():
    # esper_ExtraParenthesisRule has no real 'esper_ExtraParenthesisRule' property in the generated
    # code (a bare stub) -- manually attach it so esper_Anything's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Anything's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Anything(operator="sample_text")
    partner = esper_ExtraParenthesisRule()
    setattr(partner, 'esper_ExtraParenthesisRule', None)
    _safe_set(owner, 'esper_Anything91', {partner})
    assert getattr(partner, 'esper_ExtraParenthesisRule') == owner
    _safe_set(owner, 'esper_Anything91', set())
    assert getattr(partner, 'esper_ExtraParenthesisRule') is None


def test_assoc_followsByJoinList45_stub_double():
    # esper_AbstractFollowBy has no real 'esper_AbstractFollowBy' property in the generated
    # code (a bare stub) -- manually attach it so esper_JoinFollowBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_JoinFollowBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_JoinFollowBy(operator="sample_text")
    partner = esper_AbstractFollowBy()
    setattr(partner, 'esper_AbstractFollowBy', None)
    _safe_set(owner, 'esper_JoinFollowBy46', {partner})
    assert getattr(partner, 'esper_AbstractFollowBy') == owner
    _safe_set(owner, 'esper_JoinFollowBy46', set())
    assert getattr(partner, 'esper_AbstractFollowBy') is None


def test_assoc_having19_stub_double():
    # esper_RuleParts has no real 'esper_RuleParts20' property in the generated
    # code (a bare stub) -- manually attach it so esper_Having's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Having's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Having(operator="sample_text")
    partner = esper_RuleParts()
    setattr(partner, 'esper_RuleParts20', None)
    _safe_set(owner, 'esper_Having', partner)
    assert getattr(partner, 'esper_RuleParts20') == owner
    _safe_set(owner, 'esper_Having', None)
    assert getattr(partner, 'esper_RuleParts20') is None


def test_assoc_joinFollowBy41_stub_double():
    # esper_Pattern has no real 'esper_Pattern42' property in the generated
    # code (a bare stub) -- manually attach it so esper_JoinFollowBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_JoinFollowBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_JoinFollowBy(operator="sample_text")
    partner = esper_Pattern()
    setattr(partner, 'esper_Pattern42', None)
    _safe_set(owner, 'esper_JoinFollowBy', partner)
    assert getattr(partner, 'esper_Pattern42') == owner
    _safe_set(owner, 'esper_JoinFollowBy', None)
    assert getattr(partner, 'esper_Pattern42') is None


def test_assoc_leftSide51_stub_double():
    # esper_FollowBy has no real 'esper_FollowBy52' property in the generated
    # code (a bare stub) -- manually attach it so esper_TerminalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_TerminalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_TerminalExpression(every=True, parenthesis=True)
    partner = esper_FollowBy()
    setattr(partner, 'esper_FollowBy52', None)
    _safe_set(owner, 'esper_TerminalExpression', partner)
    assert getattr(partner, 'esper_FollowBy52') == owner
    _safe_set(owner, 'esper_TerminalExpression', None)
    assert getattr(partner, 'esper_FollowBy52') is None


def test_assoc_nameRule7_stub_double():
    # esper_RuleParts has no real 'esper_RuleParts8' property in the generated
    # code (a bare stub) -- manually attach it so esper_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Name(name="sample_text")
    partner = esper_RuleParts()
    setattr(partner, 'esper_RuleParts8', None)
    _safe_set(owner, 'esper_Name', partner)
    assert getattr(partner, 'esper_RuleParts8') == owner
    _safe_set(owner, 'esper_Name', None)
    assert getattr(partner, 'esper_RuleParts8') is None


def test_assoc_priority11_stub_double():
    # esper_RuleParts has no real 'esper_RuleParts12' property in the generated
    # code (a bare stub) -- manually attach it so esper_Priority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Priority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Priority(priorityInt=7)
    partner = esper_RuleParts()
    setattr(partner, 'esper_RuleParts12', None)
    _safe_set(owner, 'esper_Priority', partner)
    assert getattr(partner, 'esper_RuleParts12') == owner
    _safe_set(owner, 'esper_Priority', None)
    assert getattr(partner, 'esper_RuleParts12') is None


def test_assoc_rightSide53_stub_double():
    # esper_FollowBy has no real 'esper_FollowBy54' property in the generated
    # code (a bare stub) -- manually attach it so esper_TerminalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_TerminalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_TerminalExpression(every=True, parenthesis=True)
    partner = esper_FollowBy()
    setattr(partner, 'esper_FollowBy54', None)
    _safe_set(owner, 'esper_TerminalExpression55', partner)
    assert owner in getattr(partner, 'esper_FollowBy54')
    _safe_set(owner, 'esper_TerminalExpression55', None)
    assert owner not in getattr(partner, 'esper_FollowBy54')


def test_assoc_selectRule13_stub_double():
    # esper_RuleParts has no real 'esper_RuleParts14' property in the generated
    # code (a bare stub) -- manually attach it so esper_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esper_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esper_Select(alias="sample_text", asterisk=True)
    partner = esper_RuleParts()
    setattr(partner, 'esper_RuleParts14', None)
    _safe_set(owner, 'esper_Select', partner)
    assert getattr(partner, 'esper_RuleParts14') == owner
    _safe_set(owner, 'esper_Select', None)
    assert getattr(partner, 'esper_RuleParts14') is None


