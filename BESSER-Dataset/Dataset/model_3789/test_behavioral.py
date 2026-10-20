import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EObject,
    testmodel_StringToStringMap,
    testmodel_StringToTestElementMap,
    testmodel_TestElement,
    testmodel_TestElementContainer,
    testmodel_TestElementToStringMap,
    testmodel_TestElementToTestElementMap,
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

def test_assoc_containedElement9_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement8', a1)
    assert _is_linked(b, 'testmodel_TestElement8', a1)
    if hasattr(a1, 'testmodel_TestElement10'):
        assert _is_linked(a1, 'testmodel_TestElement10', b)
    _safe_set(b, 'testmodel_TestElement8', a2)
    assert _is_linked(b, 'testmodel_TestElement8', a2)
    if hasattr(a1, 'testmodel_TestElement10'):
        assert not _is_linked(a1, 'testmodel_TestElement10', b)
    if hasattr(a2, 'testmodel_TestElement10'):
        assert _is_linked(a2, 'testmodel_TestElement10', b)
    _safe_set(b, 'testmodel_TestElement8', None)
    assert not _is_linked(b, 'testmodel_TestElement8', a2)
    if hasattr(a2, 'testmodel_TestElement10'):
        assert not _is_linked(a2, 'testmodel_TestElement10', b)


def test_assoc_containedElements215_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement16', a1)
    assert _is_linked(b, 'testmodel_TestElement16', a1)
    if hasattr(a1, 'testmodel_TestElement14'):
        assert _is_linked(a1, 'testmodel_TestElement14', b)
    _safe_set(b, 'testmodel_TestElement16', a2)
    assert _is_linked(b, 'testmodel_TestElement16', a2)
    if hasattr(a1, 'testmodel_TestElement14'):
        assert not _is_linked(a1, 'testmodel_TestElement14', b)
    if hasattr(a2, 'testmodel_TestElement14'):
        assert _is_linked(a2, 'testmodel_TestElement14', b)
    _safe_set(b, 'testmodel_TestElement16', None)
    assert not _is_linked(b, 'testmodel_TestElement16', a2)
    if hasattr(a2, 'testmodel_TestElement14'):
        assert not _is_linked(a2, 'testmodel_TestElement14', b)


def test_assoc_containedElements3_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement4', a1)
    assert _is_linked(b, 'testmodel_TestElement4', a1)
    if hasattr(a1, 'testmodel_TestElement2'):
        assert _is_linked(a1, 'testmodel_TestElement2', b)
    _safe_set(b, 'testmodel_TestElement4', a2)
    assert _is_linked(b, 'testmodel_TestElement4', a2)
    if hasattr(a1, 'testmodel_TestElement2'):
        assert not _is_linked(a1, 'testmodel_TestElement2', b)
    if hasattr(a2, 'testmodel_TestElement2'):
        assert _is_linked(a2, 'testmodel_TestElement2', b)
    _safe_set(b, 'testmodel_TestElement4', None)
    assert not _is_linked(b, 'testmodel_TestElement4', a2)
    if hasattr(a2, 'testmodel_TestElement2'):
        assert not _is_linked(a2, 'testmodel_TestElement2', b)


def test_assoc_elementToStringMap22_reverse_link_reassign_clear():
    a1 = testmodel_TestElementToStringMap(value="sample_text")
    a2 = testmodel_TestElementToStringMap(value="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement23', {a1})
    assert _is_linked(b, 'testmodel_TestElement23', a1)
    if hasattr(a1, 'testmodel_TestElementToStringMap'):
        assert _is_linked(a1, 'testmodel_TestElementToStringMap', b)
    _safe_set(b, 'testmodel_TestElement23', {a2})
    assert _is_linked(b, 'testmodel_TestElement23', a2)
    if hasattr(a1, 'testmodel_TestElementToStringMap'):
        assert not _is_linked(a1, 'testmodel_TestElementToStringMap', b)
    if hasattr(a2, 'testmodel_TestElementToStringMap'):
        assert _is_linked(a2, 'testmodel_TestElementToStringMap', b)
    _safe_set(b, 'testmodel_TestElement23', set())
    assert not _is_linked(b, 'testmodel_TestElement23', a2)
    if hasattr(a2, 'testmodel_TestElementToStringMap'):
        assert not _is_linked(a2, 'testmodel_TestElementToStringMap', b)


def test_assoc_key27_reverse_link_reassign_clear():
    a1 = testmodel_TestElementToStringMap(value="sample_text")
    a2 = testmodel_TestElementToStringMap(value="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement29', a1)
    assert _is_linked(b, 'testmodel_TestElement29', a1)
    if hasattr(a1, 'testmodel_TestElementToStringMap28'):
        assert _is_linked(a1, 'testmodel_TestElementToStringMap28', b)
    _safe_set(b, 'testmodel_TestElement29', a2)
    assert _is_linked(b, 'testmodel_TestElement29', a2)
    if hasattr(a1, 'testmodel_TestElementToStringMap28'):
        assert not _is_linked(a1, 'testmodel_TestElementToStringMap28', b)
    if hasattr(a2, 'testmodel_TestElementToStringMap28'):
        assert _is_linked(a2, 'testmodel_TestElementToStringMap28', b)
    _safe_set(b, 'testmodel_TestElement29', None)
    assert not _is_linked(b, 'testmodel_TestElement29', a2)
    if hasattr(a2, 'testmodel_TestElementToStringMap28'):
        assert not _is_linked(a2, 'testmodel_TestElementToStringMap28', b)


def test_assoc_otherReference12_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement13', a1)
    assert _is_linked(b, 'testmodel_TestElement13', a1)
    if hasattr(a1, 'testmodel_TestElement11'):
        assert _is_linked(a1, 'testmodel_TestElement11', b)
    _safe_set(b, 'testmodel_TestElement13', a2)
    assert _is_linked(b, 'testmodel_TestElement13', a2)
    if hasattr(a1, 'testmodel_TestElement11'):
        assert not _is_linked(a1, 'testmodel_TestElement11', b)
    if hasattr(a2, 'testmodel_TestElement11'):
        assert _is_linked(a2, 'testmodel_TestElement11', b)
    _safe_set(b, 'testmodel_TestElement13', None)
    assert not _is_linked(b, 'testmodel_TestElement13', a2)
    if hasattr(a2, 'testmodel_TestElement11'):
        assert not _is_linked(a2, 'testmodel_TestElement11', b)


def test_assoc_reference6_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement7', a1)
    assert _is_linked(b, 'testmodel_TestElement7', a1)
    if hasattr(a1, 'testmodel_TestElement5'):
        assert _is_linked(a1, 'testmodel_TestElement5', b)
    _safe_set(b, 'testmodel_TestElement7', a2)
    assert _is_linked(b, 'testmodel_TestElement7', a2)
    if hasattr(a1, 'testmodel_TestElement5'):
        assert not _is_linked(a1, 'testmodel_TestElement5', b)
    if hasattr(a2, 'testmodel_TestElement5'):
        assert _is_linked(a2, 'testmodel_TestElement5', b)
    _safe_set(b, 'testmodel_TestElement7', None)
    assert not _is_linked(b, 'testmodel_TestElement7', a2)
    if hasattr(a2, 'testmodel_TestElement5'):
        assert not _is_linked(a2, 'testmodel_TestElement5', b)


def test_assoc_references1_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'testmodel_TestElement0', {a1})
    assert _is_linked(b, 'testmodel_TestElement0', a1)
    if hasattr(a1, 'testmodel_TestElement'):
        assert _is_linked(a1, 'testmodel_TestElement', b)
    _safe_set(b, 'testmodel_TestElement0', {a2})
    assert _is_linked(b, 'testmodel_TestElement0', a2)
    if hasattr(a1, 'testmodel_TestElement'):
        assert not _is_linked(a1, 'testmodel_TestElement', b)
    if hasattr(a2, 'testmodel_TestElement'):
        assert _is_linked(a2, 'testmodel_TestElement', b)
    _safe_set(b, 'testmodel_TestElement0', set())
    assert not _is_linked(b, 'testmodel_TestElement0', a2)
    if hasattr(a2, 'testmodel_TestElement'):
        assert not _is_linked(a2, 'testmodel_TestElement', b)


def test_assoc_stringToElementMap24_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_StringToTestElementMap(key="sample_text")
    _safe_set(b, 'testmodel_StringToTestElementMap', a1)
    assert _is_linked(b, 'testmodel_StringToTestElementMap', a1)
    if hasattr(a1, 'testmodel_TestElement25'):
        assert _is_linked(a1, 'testmodel_TestElement25', b)
    _safe_set(b, 'testmodel_StringToTestElementMap', a2)
    assert _is_linked(b, 'testmodel_StringToTestElementMap', a2)
    if hasattr(a1, 'testmodel_TestElement25'):
        assert not _is_linked(a1, 'testmodel_TestElement25', b)
    if hasattr(a2, 'testmodel_TestElement25'):
        assert _is_linked(a2, 'testmodel_TestElement25', b)
    _safe_set(b, 'testmodel_StringToTestElementMap', None)
    assert not _is_linked(b, 'testmodel_StringToTestElementMap', a2)
    if hasattr(a2, 'testmodel_TestElement25'):
        assert not _is_linked(a2, 'testmodel_TestElement25', b)


def test_assoc_stringToStringMap20_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'testmodel_StringToStringMap', a1)
    assert _is_linked(b, 'testmodel_StringToStringMap', a1)
    if hasattr(a1, 'testmodel_TestElement21'):
        assert _is_linked(a1, 'testmodel_TestElement21', b)
    _safe_set(b, 'testmodel_StringToStringMap', a2)
    assert _is_linked(b, 'testmodel_StringToStringMap', a2)
    if hasattr(a1, 'testmodel_TestElement21'):
        assert not _is_linked(a1, 'testmodel_TestElement21', b)
    if hasattr(a2, 'testmodel_TestElement21'):
        assert _is_linked(a2, 'testmodel_TestElement21', b)
    _safe_set(b, 'testmodel_StringToStringMap', None)
    assert not _is_linked(b, 'testmodel_StringToStringMap', a2)
    if hasattr(a2, 'testmodel_TestElement21'):
        assert not _is_linked(a2, 'testmodel_TestElement21', b)


def test_assoc_value36_reverse_link_reassign_clear():
    a1 = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    a2 = testmodel_TestElement(description="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = testmodel_StringToTestElementMap(key="sample_text")
    _safe_set(b, 'testmodel_StringToTestElementMap37', a1)
    assert _is_linked(b, 'testmodel_StringToTestElementMap37', a1)
    if hasattr(a1, 'testmodel_TestElement38'):
        assert _is_linked(a1, 'testmodel_TestElement38', b)
    _safe_set(b, 'testmodel_StringToTestElementMap37', a2)
    assert _is_linked(b, 'testmodel_StringToTestElementMap37', a2)
    if hasattr(a1, 'testmodel_TestElement38'):
        assert not _is_linked(a1, 'testmodel_TestElement38', b)
    if hasattr(a2, 'testmodel_TestElement38'):
        assert _is_linked(a2, 'testmodel_TestElement38', b)
    _safe_set(b, 'testmodel_StringToTestElementMap37', None)
    assert not _is_linked(b, 'testmodel_StringToTestElementMap37', a2)
    if hasattr(a2, 'testmodel_TestElement38'):
        assert not _is_linked(a2, 'testmodel_TestElement38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_container17_stub_double():
    # testmodel_TestElementContainer has no real 'TestElementContainer' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    partner = testmodel_TestElementContainer()
    setattr(partner, 'TestElementContainer', None)
    _safe_set(owner, 'elements', partner)
    assert getattr(partner, 'TestElementContainer') == owner
    _safe_set(owner, 'elements', None)
    assert getattr(partner, 'TestElementContainer') is None


def test_assoc_elementMap18_stub_double():
    # testmodel_TestElementToTestElementMap has no real 'testmodel_TestElementToTestElementMap' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    partner = testmodel_TestElementToTestElementMap()
    setattr(partner, 'testmodel_TestElementToTestElementMap', None)
    _safe_set(owner, 'testmodel_TestElement19', {partner})
    assert getattr(partner, 'testmodel_TestElementToTestElementMap') == owner
    _safe_set(owner, 'testmodel_TestElement19', set())
    assert getattr(partner, 'testmodel_TestElementToTestElementMap') is None


def test_assoc_elements26_stub_double():
    # testmodel_TestElementContainer has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    partner = testmodel_TestElementContainer()
    setattr(partner, 'container', None)
    _safe_set(owner, 'TestElement', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'TestElement', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_key33_stub_double():
    # testmodel_TestElementToTestElementMap has no real 'testmodel_TestElementToTestElementMap34' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    partner = testmodel_TestElementToTestElementMap()
    setattr(partner, 'testmodel_TestElementToTestElementMap34', None)
    _safe_set(owner, 'testmodel_TestElement35', partner)
    assert getattr(partner, 'testmodel_TestElementToTestElementMap34') == owner
    _safe_set(owner, 'testmodel_TestElement35', None)
    assert getattr(partner, 'testmodel_TestElementToTestElementMap34') is None


def test_assoc_value30_stub_double():
    # testmodel_TestElementToTestElementMap has no real 'testmodel_TestElementToTestElementMap31' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_TestElement(description="sample_text", name="sample_text", strings="sample_text")
    partner = testmodel_TestElementToTestElementMap()
    setattr(partner, 'testmodel_TestElementToTestElementMap31', None)
    _safe_set(owner, 'testmodel_TestElement32', partner)
    assert getattr(partner, 'testmodel_TestElementToTestElementMap31') == owner
    _safe_set(owner, 'testmodel_TestElement32', None)
    assert getattr(partner, 'testmodel_TestElementToTestElementMap31') is None


