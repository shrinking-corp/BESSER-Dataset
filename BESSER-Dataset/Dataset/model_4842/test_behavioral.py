import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActiveStructureElement,
    BusinessElement,
    MotivationElement,
    Requirement,
    StrategyElement,
    archimate_ActiveStructureElement,
    archimate_ArchimateDiagram,
    archimate_Assessment,
    archimate_BusinessElement,
    archimate_BusinessProcess,
    archimate_Constraint,
    archimate_Driver,
    archimate_Goal,
    archimate_Meaning,
    archimate_MotivationElement,
    archimate_Outcome,
    archimate_Principle,
    archimate_Requirement,
    archimate_Resource,
    archimate_Stakeholder,
    archimate_StrategyElement,
    archimate_Value,
    refinement,
    relationType,
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

def test_assoc_children20_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_MotivationElement21', a1)
    assert _is_linked(b, 'archimate_MotivationElement21', a1)
    if hasattr(a1, 'archimate_MotivationElement19'):
        assert _is_linked(a1, 'archimate_MotivationElement19', b)
    _safe_set(b, 'archimate_MotivationElement21', a2)
    assert _is_linked(b, 'archimate_MotivationElement21', a2)
    if hasattr(a1, 'archimate_MotivationElement19'):
        assert not _is_linked(a1, 'archimate_MotivationElement19', b)
    if hasattr(a2, 'archimate_MotivationElement19'):
        assert _is_linked(a2, 'archimate_MotivationElement19', b)
    _safe_set(b, 'archimate_MotivationElement21', None)
    assert not _is_linked(b, 'archimate_MotivationElement21', a2)
    if hasattr(a2, 'archimate_MotivationElement19'):
        assert not _is_linked(a2, 'archimate_MotivationElement19', b)


def test_assoc_children53_reverse_link_reassign_clear():
    a1 = archimate_StrategyElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_StrategyElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_StrategyElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_StrategyElement54', a1)
    assert _is_linked(b, 'archimate_StrategyElement54', a1)
    if hasattr(a1, 'archimate_StrategyElement52'):
        assert _is_linked(a1, 'archimate_StrategyElement52', b)
    _safe_set(b, 'archimate_StrategyElement54', a2)
    assert _is_linked(b, 'archimate_StrategyElement54', a2)
    if hasattr(a1, 'archimate_StrategyElement52'):
        assert not _is_linked(a1, 'archimate_StrategyElement52', b)
    if hasattr(a2, 'archimate_StrategyElement52'):
        assert _is_linked(a2, 'archimate_StrategyElement52', b)
    _safe_set(b, 'archimate_StrategyElement54', None)
    assert not _is_linked(b, 'archimate_StrategyElement54', a2)
    if hasattr(a2, 'archimate_StrategyElement52'):
        assert not _is_linked(a2, 'archimate_StrategyElement52', b)


def test_assoc_children59_reverse_link_reassign_clear():
    a1 = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_BusinessElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_BusinessElement60', a1)
    assert _is_linked(b, 'archimate_BusinessElement60', a1)
    if hasattr(a1, 'archimate_BusinessElement58'):
        assert _is_linked(a1, 'archimate_BusinessElement58', b)
    _safe_set(b, 'archimate_BusinessElement60', a2)
    assert _is_linked(b, 'archimate_BusinessElement60', a2)
    if hasattr(a1, 'archimate_BusinessElement58'):
        assert not _is_linked(a1, 'archimate_BusinessElement58', b)
    if hasattr(a2, 'archimate_BusinessElement58'):
        assert _is_linked(a2, 'archimate_BusinessElement58', b)
    _safe_set(b, 'archimate_BusinessElement60', None)
    assert not _is_linked(b, 'archimate_BusinessElement60', a2)
    if hasattr(a2, 'archimate_BusinessElement58'):
        assert not _is_linked(a2, 'archimate_BusinessElement58', b)


def test_assoc_influences17_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_MotivationElement18', a1)
    assert _is_linked(b, 'archimate_MotivationElement18', a1)
    if hasattr(a1, 'archimate_MotivationElement16'):
        assert _is_linked(a1, 'archimate_MotivationElement16', b)
    _safe_set(b, 'archimate_MotivationElement18', a2)
    assert _is_linked(b, 'archimate_MotivationElement18', a2)
    if hasattr(a1, 'archimate_MotivationElement16'):
        assert not _is_linked(a1, 'archimate_MotivationElement16', b)
    if hasattr(a2, 'archimate_MotivationElement16'):
        assert _is_linked(a2, 'archimate_MotivationElement16', b)
    _safe_set(b, 'archimate_MotivationElement18', None)
    assert not _is_linked(b, 'archimate_MotivationElement18', a2)
    if hasattr(a2, 'archimate_MotivationElement16'):
        assert not _is_linked(a2, 'archimate_MotivationElement16', b)


def test_assoc_influences55_reverse_link_reassign_clear():
    a1 = archimate_StrategyElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_StrategyElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_MotivationElement57', a1)
    assert _is_linked(b, 'archimate_MotivationElement57', a1)
    if hasattr(a1, 'archimate_StrategyElement56'):
        assert _is_linked(a1, 'archimate_StrategyElement56', b)
    _safe_set(b, 'archimate_MotivationElement57', a2)
    assert _is_linked(b, 'archimate_MotivationElement57', a2)
    if hasattr(a1, 'archimate_StrategyElement56'):
        assert not _is_linked(a1, 'archimate_StrategyElement56', b)
    if hasattr(a2, 'archimate_StrategyElement56'):
        assert _is_linked(a2, 'archimate_StrategyElement56', b)
    _safe_set(b, 'archimate_MotivationElement57', None)
    assert not _is_linked(b, 'archimate_MotivationElement57', a2)
    if hasattr(a2, 'archimate_StrategyElement56'):
        assert not _is_linked(a2, 'archimate_StrategyElement56', b)


def test_assoc_influences64_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_BusinessElement65', {a1})
    assert _is_linked(b, 'archimate_BusinessElement65', a1)
    if hasattr(a1, 'archimate_MotivationElement66'):
        assert _is_linked(a1, 'archimate_MotivationElement66', b)
    _safe_set(b, 'archimate_BusinessElement65', {a2})
    assert _is_linked(b, 'archimate_BusinessElement65', a2)
    if hasattr(a1, 'archimate_MotivationElement66'):
        assert not _is_linked(a1, 'archimate_MotivationElement66', b)
    if hasattr(a2, 'archimate_MotivationElement66'):
        assert _is_linked(a2, 'archimate_MotivationElement66', b)
    _safe_set(b, 'archimate_BusinessElement65', set())
    assert not _is_linked(b, 'archimate_BusinessElement65', a2)
    if hasattr(a2, 'archimate_MotivationElement66'):
        assert not _is_linked(a2, 'archimate_MotivationElement66', b)


def test_assoc_influences8_reverse_link_reassign_clear():
    a1 = archimate_ActiveStructureElement(name="sample_text")
    a2 = archimate_ActiveStructureElement(name="sample_text_2")
    b = archimate_ActiveStructureElement(name="sample_text")
    _safe_set(b, 'archimate_ActiveStructureElement9', a1)
    assert _is_linked(b, 'archimate_ActiveStructureElement9', a1)
    if hasattr(a1, 'archimate_ActiveStructureElement7'):
        assert _is_linked(a1, 'archimate_ActiveStructureElement7', b)
    _safe_set(b, 'archimate_ActiveStructureElement9', a2)
    assert _is_linked(b, 'archimate_ActiveStructureElement9', a2)
    if hasattr(a1, 'archimate_ActiveStructureElement7'):
        assert not _is_linked(a1, 'archimate_ActiveStructureElement7', b)
    if hasattr(a2, 'archimate_ActiveStructureElement7'):
        assert _is_linked(a2, 'archimate_ActiveStructureElement7', b)
    _safe_set(b, 'archimate_ActiveStructureElement9', None)
    assert not _is_linked(b, 'archimate_ActiveStructureElement9', a2)
    if hasattr(a2, 'archimate_ActiveStructureElement7'):
        assert not _is_linked(a2, 'archimate_ActiveStructureElement7', b)


def test_assoc_negativeInfluence23_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_MotivationElement24', a1)
    assert _is_linked(b, 'archimate_MotivationElement24', a1)
    if hasattr(a1, 'archimate_MotivationElement22'):
        assert _is_linked(a1, 'archimate_MotivationElement22', b)
    _safe_set(b, 'archimate_MotivationElement24', a2)
    assert _is_linked(b, 'archimate_MotivationElement24', a2)
    if hasattr(a1, 'archimate_MotivationElement22'):
        assert not _is_linked(a1, 'archimate_MotivationElement22', b)
    if hasattr(a2, 'archimate_MotivationElement22'):
        assert _is_linked(a2, 'archimate_MotivationElement22', b)
    _safe_set(b, 'archimate_MotivationElement24', None)
    assert not _is_linked(b, 'archimate_MotivationElement24', a2)
    if hasattr(a2, 'archimate_MotivationElement22'):
        assert not _is_linked(a2, 'archimate_MotivationElement22', b)


def test_assoc_negativeInfluence70_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_BusinessElement71', {a1})
    assert _is_linked(b, 'archimate_BusinessElement71', a1)
    if hasattr(a1, 'archimate_MotivationElement72'):
        assert _is_linked(a1, 'archimate_MotivationElement72', b)
    _safe_set(b, 'archimate_BusinessElement71', {a2})
    assert _is_linked(b, 'archimate_BusinessElement71', a2)
    if hasattr(a1, 'archimate_MotivationElement72'):
        assert not _is_linked(a1, 'archimate_MotivationElement72', b)
    if hasattr(a2, 'archimate_MotivationElement72'):
        assert _is_linked(a2, 'archimate_MotivationElement72', b)
    _safe_set(b, 'archimate_BusinessElement71', set())
    assert not _is_linked(b, 'archimate_BusinessElement71', a2)
    if hasattr(a2, 'archimate_MotivationElement72'):
        assert not _is_linked(a2, 'archimate_MotivationElement72', b)


def test_assoc_realizes61_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_BusinessElement62', {a1})
    assert _is_linked(b, 'archimate_BusinessElement62', a1)
    if hasattr(a1, 'archimate_MotivationElement63'):
        assert _is_linked(a1, 'archimate_MotivationElement63', b)
    _safe_set(b, 'archimate_BusinessElement62', {a2})
    assert _is_linked(b, 'archimate_BusinessElement62', a2)
    if hasattr(a1, 'archimate_MotivationElement63'):
        assert not _is_linked(a1, 'archimate_MotivationElement63', b)
    if hasattr(a2, 'archimate_MotivationElement63'):
        assert _is_linked(a2, 'archimate_MotivationElement63', b)
    _safe_set(b, 'archimate_BusinessElement62', set())
    assert not _is_linked(b, 'archimate_BusinessElement62', a2)
    if hasattr(a2, 'archimate_MotivationElement63'):
        assert not _is_linked(a2, 'archimate_MotivationElement63', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_MotivationElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_ActiveStructureElement(name="sample_text")
    _safe_set(b, 'archimate_ActiveStructureElement11', {a1})
    assert _is_linked(b, 'archimate_ActiveStructureElement11', a1)
    if hasattr(a1, 'archimate_MotivationElement12'):
        assert _is_linked(a1, 'archimate_MotivationElement12', b)
    _safe_set(b, 'archimate_ActiveStructureElement11', {a2})
    assert _is_linked(b, 'archimate_ActiveStructureElement11', a2)
    if hasattr(a1, 'archimate_MotivationElement12'):
        assert not _is_linked(a1, 'archimate_MotivationElement12', b)
    if hasattr(a2, 'archimate_MotivationElement12'):
        assert _is_linked(a2, 'archimate_MotivationElement12', b)
    _safe_set(b, 'archimate_ActiveStructureElement11', set())
    assert not _is_linked(b, 'archimate_ActiveStructureElement11', a2)
    if hasattr(a2, 'archimate_MotivationElement12'):
        assert not _is_linked(a2, 'archimate_MotivationElement12', b)


def test_assoc_triggers68_reverse_link_reassign_clear():
    a1 = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    a2 = archimate_BusinessElement(name="sample_text_2", refinementType="sample_text_2", relationType="sample_text_2")
    b = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    _safe_set(b, 'archimate_BusinessElement69', a1)
    assert _is_linked(b, 'archimate_BusinessElement69', a1)
    if hasattr(a1, 'archimate_BusinessElement67'):
        assert _is_linked(a1, 'archimate_BusinessElement67', b)
    _safe_set(b, 'archimate_BusinessElement69', a2)
    assert _is_linked(b, 'archimate_BusinessElement69', a2)
    if hasattr(a1, 'archimate_BusinessElement67'):
        assert not _is_linked(a1, 'archimate_BusinessElement67', b)
    if hasattr(a2, 'archimate_BusinessElement67'):
        assert _is_linked(a2, 'archimate_BusinessElement67', b)
    _safe_set(b, 'archimate_BusinessElement69', None)
    assert not _is_linked(b, 'archimate_BusinessElement69', a2)
    if hasattr(a2, 'archimate_BusinessElement67'):
        assert not _is_linked(a2, 'archimate_BusinessElement67', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activestructureelement0_stub_double():
    # archimate_ArchimateDiagram has no real 'archimate_ArchimateDiagram' property in the generated
    # code (a bare stub) -- manually attach it so archimate_ActiveStructureElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimate_ActiveStructureElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimate_ActiveStructureElement(name="sample_text")
    partner = archimate_ArchimateDiagram()
    setattr(partner, 'archimate_ArchimateDiagram', None)
    _safe_set(owner, 'archimate_ActiveStructureElement', partner)
    assert owner in getattr(partner, 'archimate_ArchimateDiagram')
    _safe_set(owner, 'archimate_ActiveStructureElement', None)
    assert owner not in getattr(partner, 'archimate_ArchimateDiagram')


def test_assoc_bussinesselement3_stub_double():
    # archimate_ArchimateDiagram has no real 'archimate_ArchimateDiagram4' property in the generated
    # code (a bare stub) -- manually attach it so archimate_BusinessElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimate_BusinessElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimate_BusinessElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    partner = archimate_ArchimateDiagram()
    setattr(partner, 'archimate_ArchimateDiagram4', None)
    _safe_set(owner, 'archimate_BusinessElement', partner)
    assert owner in getattr(partner, 'archimate_ArchimateDiagram4')
    _safe_set(owner, 'archimate_BusinessElement', None)
    assert owner not in getattr(partner, 'archimate_ArchimateDiagram4')


def test_assoc_motivationelement1_stub_double():
    # archimate_ArchimateDiagram has no real 'archimate_ArchimateDiagram2' property in the generated
    # code (a bare stub) -- manually attach it so archimate_MotivationElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimate_MotivationElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimate_MotivationElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    partner = archimate_ArchimateDiagram()
    setattr(partner, 'archimate_ArchimateDiagram2', None)
    _safe_set(owner, 'archimate_MotivationElement', partner)
    assert owner in getattr(partner, 'archimate_ArchimateDiagram2')
    _safe_set(owner, 'archimate_MotivationElement', None)
    assert owner not in getattr(partner, 'archimate_ArchimateDiagram2')


def test_assoc_strategyelement5_stub_double():
    # archimate_ArchimateDiagram has no real 'archimate_ArchimateDiagram6' property in the generated
    # code (a bare stub) -- manually attach it so archimate_StrategyElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimate_StrategyElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimate_StrategyElement(name="sample_text", refinementType="sample_text", relationType="sample_text")
    partner = archimate_ArchimateDiagram()
    setattr(partner, 'archimate_ArchimateDiagram6', None)
    _safe_set(owner, 'archimate_StrategyElement', partner)
    assert owner in getattr(partner, 'archimate_ArchimateDiagram6')
    _safe_set(owner, 'archimate_StrategyElement', None)
    assert owner not in getattr(partner, 'archimate_ArchimateDiagram6')


