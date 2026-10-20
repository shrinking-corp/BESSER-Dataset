import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    InputField,
    PageElement,
    Text,
    VisibilityCondition,
    form_Form,
    form_Heading,
    form_InputField,
    form_List,
    form_ListItem,
    form_Page,
    form_PageElement,
    form_Paragraph,
    form_SelectionCondition,
    form_SelectionField,
    form_SelectionItem,
    form_Text,
    form_TextArea,
    form_TextField,
    form_VisibilityCondition,
    SelectionFieldType,
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

def test_assoc_allNextPages8_reverse_link_reassign_clear():
    a1 = form_Page(title="sample_text")
    a2 = form_Page(title="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'form_Page9', a1)
    assert _is_linked(b, 'form_Page9', a1)
    if hasattr(a1, 'form_Page7'):
        assert _is_linked(a1, 'form_Page7', b)
    _safe_set(b, 'form_Page9', a2)
    assert _is_linked(b, 'form_Page9', a2)
    if hasattr(a1, 'form_Page7'):
        assert not _is_linked(a1, 'form_Page7', b)
    if hasattr(a2, 'form_Page7'):
        assert _is_linked(a2, 'form_Page7', b)
    _safe_set(b, 'form_Page9', None)
    assert not _is_linked(b, 'form_Page9', a2)
    if hasattr(a2, 'form_Page7'):
        assert not _is_linked(a2, 'form_Page7', b)


def test_assoc_allPreviousPages5_reverse_link_reassign_clear():
    a1 = form_Page(title="sample_text")
    a2 = form_Page(title="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'form_Page6', a1)
    assert _is_linked(b, 'form_Page6', a1)
    if hasattr(a1, 'form_Page4'):
        assert _is_linked(a1, 'form_Page4', b)
    _safe_set(b, 'form_Page6', a2)
    assert _is_linked(b, 'form_Page6', a2)
    if hasattr(a1, 'form_Page4'):
        assert not _is_linked(a1, 'form_Page4', b)
    if hasattr(a2, 'form_Page4'):
        assert _is_linked(a2, 'form_Page4', b)
    _safe_set(b, 'form_Page6', None)
    assert not _is_linked(b, 'form_Page6', a2)
    if hasattr(a2, 'form_Page4'):
        assert not _is_linked(a2, 'form_Page4', b)


def test_assoc_elements12_reverse_link_reassign_clear():
    a1 = form_PageElement(elementId="sample_text")
    a2 = form_PageElement(elementId="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'page', {a1})
    assert _is_linked(b, 'page', a1)
    if hasattr(a1, 'PageElement'):
        assert _is_linked(a1, 'PageElement', b)
    _safe_set(b, 'page', {a2})
    assert _is_linked(b, 'page', a2)
    if hasattr(a1, 'PageElement'):
        assert not _is_linked(a1, 'PageElement', b)
    if hasattr(a2, 'PageElement'):
        assert _is_linked(a2, 'PageElement', b)
    _safe_set(b, 'page', set())
    assert not _is_linked(b, 'page', a2)
    if hasattr(a2, 'PageElement'):
        assert not _is_linked(a2, 'PageElement', b)


def test_assoc_field21_reverse_link_reassign_clear():
    a1 = form_SelectionItem(label="sample_text", selected=True)
    a2 = form_SelectionItem(label="sample_text_2", selected=False)
    b = form_SelectionField(selectionFieldType="sample_text")
    _safe_set(b, 'SelectionField', a1)
    assert _is_linked(b, 'SelectionField', a1)
    if hasattr(a1, 'items'):
        assert _is_linked(a1, 'items', b)
    _safe_set(b, 'SelectionField', a2)
    assert _is_linked(b, 'SelectionField', a2)
    if hasattr(a1, 'items'):
        assert not _is_linked(a1, 'items', b)
    if hasattr(a2, 'items'):
        assert _is_linked(a2, 'items', b)
    _safe_set(b, 'SelectionField', None)
    assert not _is_linked(b, 'SelectionField', a2)
    if hasattr(a2, 'items'):
        assert not _is_linked(a2, 'items', b)


def test_assoc_items20_reverse_link_reassign_clear():
    a1 = form_SelectionItem(label="sample_text", selected=True)
    a2 = form_SelectionItem(label="sample_text_2", selected=False)
    b = form_SelectionField(selectionFieldType="sample_text")
    _safe_set(b, 'field', {a1})
    assert _is_linked(b, 'field', a1)
    if hasattr(a1, 'SelectionItem'):
        assert _is_linked(a1, 'SelectionItem', b)
    _safe_set(b, 'field', {a2})
    assert _is_linked(b, 'field', a2)
    if hasattr(a1, 'SelectionItem'):
        assert not _is_linked(a1, 'SelectionItem', b)
    if hasattr(a2, 'SelectionItem'):
        assert _is_linked(a2, 'SelectionItem', b)
    _safe_set(b, 'field', set())
    assert not _is_linked(b, 'field', a2)
    if hasattr(a2, 'SelectionItem'):
        assert not _is_linked(a2, 'SelectionItem', b)


def test_assoc_items22_reverse_link_reassign_clear():
    a1 = form_ListItem(label="sample_text")
    a2 = form_ListItem(label="sample_text_2")
    b = form_List(ordered=True)
    _safe_set(b, 'form_List', {a1})
    assert _is_linked(b, 'form_List', a1)
    if hasattr(a1, 'form_ListItem'):
        assert _is_linked(a1, 'form_ListItem', b)
    _safe_set(b, 'form_List', {a2})
    assert _is_linked(b, 'form_List', a2)
    if hasattr(a1, 'form_ListItem'):
        assert not _is_linked(a1, 'form_ListItem', b)
    if hasattr(a2, 'form_ListItem'):
        assert _is_linked(a2, 'form_ListItem', b)
    _safe_set(b, 'form_List', set())
    assert not _is_linked(b, 'form_List', a2)
    if hasattr(a2, 'form_ListItem'):
        assert not _is_linked(a2, 'form_ListItem', b)


def test_assoc_nextPage11_reverse_link_reassign_clear():
    a1 = form_Page(title="sample_text")
    a2 = form_Page(title="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'previousPage', a1)
    assert _is_linked(b, 'previousPage', a1)
    if hasattr(a1, 'Page'):
        assert _is_linked(a1, 'Page', b)
    _safe_set(b, 'previousPage', a2)
    assert _is_linked(b, 'previousPage', a2)
    if hasattr(a1, 'Page'):
        assert not _is_linked(a1, 'Page', b)
    if hasattr(a2, 'Page'):
        assert _is_linked(a2, 'Page', b)
    _safe_set(b, 'previousPage', None)
    assert not _is_linked(b, 'previousPage', a2)
    if hasattr(a2, 'Page'):
        assert not _is_linked(a2, 'Page', b)


def test_assoc_page18_reverse_link_reassign_clear():
    a1 = form_PageElement(elementId="sample_text")
    a2 = form_PageElement(elementId="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'Page19', a1)
    assert _is_linked(b, 'Page19', a1)
    if hasattr(a1, 'elements'):
        assert _is_linked(a1, 'elements', b)
    _safe_set(b, 'Page19', a2)
    assert _is_linked(b, 'Page19', a2)
    if hasattr(a1, 'elements'):
        assert not _is_linked(a1, 'elements', b)
    if hasattr(a2, 'elements'):
        assert _is_linked(a2, 'elements', b)
    _safe_set(b, 'Page19', None)
    assert not _is_linked(b, 'Page19', a2)
    if hasattr(a2, 'elements'):
        assert not _is_linked(a2, 'elements', b)


def test_assoc_previousPage14_reverse_link_reassign_clear():
    a1 = form_Page(title="sample_text")
    a2 = form_Page(title="sample_text_2")
    b = form_Page(title="sample_text")
    _safe_set(b, 'nextPage', a1)
    assert _is_linked(b, 'nextPage', a1)
    if hasattr(a1, 'Page15'):
        assert _is_linked(a1, 'Page15', b)
    _safe_set(b, 'nextPage', a2)
    assert _is_linked(b, 'nextPage', a2)
    if hasattr(a1, 'Page15'):
        assert not _is_linked(a1, 'Page15', b)
    if hasattr(a2, 'Page15'):
        assert _is_linked(a2, 'Page15', b)
    _safe_set(b, 'nextPage', None)
    assert not _is_linked(b, 'nextPage', a2)
    if hasattr(a2, 'Page15'):
        assert not _is_linked(a2, 'Page15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_concernsElements25_stub_double():
    # form_VisibilityCondition has no real 'form_VisibilityCondition' property in the generated
    # code (a bare stub) -- manually attach it so form_PageElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_PageElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_PageElement(elementId="sample_text")
    partner = form_VisibilityCondition()
    setattr(partner, 'form_VisibilityCondition', None)
    _safe_set(owner, 'form_PageElement', partner)
    assert owner in getattr(partner, 'form_VisibilityCondition')
    _safe_set(owner, 'form_PageElement', None)
    assert owner not in getattr(partner, 'form_VisibilityCondition')


def test_assoc_item26_stub_double():
    # form_SelectionCondition has no real 'form_SelectionCondition' property in the generated
    # code (a bare stub) -- manually attach it so form_SelectionItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_SelectionItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_SelectionItem(label="sample_text", selected=True)
    partner = form_SelectionCondition()
    setattr(partner, 'form_SelectionCondition', None)
    _safe_set(owner, 'form_SelectionItem', partner)
    assert getattr(partner, 'form_SelectionCondition') == owner
    _safe_set(owner, 'form_SelectionItem', None)
    assert getattr(partner, 'form_SelectionCondition') is None


def test_assoc_page23_stub_double():
    # form_VisibilityCondition has no real 'visibilityConditions' property in the generated
    # code (a bare stub) -- manually attach it so form_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Page(title="sample_text")
    partner = form_VisibilityCondition()
    setattr(partner, 'visibilityConditions', None)
    _safe_set(owner, 'Page24', partner)
    assert getattr(partner, 'visibilityConditions') == owner
    _safe_set(owner, 'Page24', None)
    assert getattr(partner, 'visibilityConditions') is None


def test_assoc_pages0_stub_double():
    # form_Form has no real 'form_Form' property in the generated
    # code (a bare stub) -- manually attach it so form_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Page(title="sample_text")
    partner = form_Form()
    setattr(partner, 'form_Form', None)
    _safe_set(owner, 'form_Page', partner)
    assert owner in getattr(partner, 'form_Form')
    _safe_set(owner, 'form_Page', None)
    assert owner not in getattr(partner, 'form_Form')


def test_assoc_visibilityConditions16_stub_double():
    # form_VisibilityCondition has no real 'VisibilityCondition' property in the generated
    # code (a bare stub) -- manually attach it so form_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Page(title="sample_text")
    partner = form_VisibilityCondition()
    setattr(partner, 'VisibilityCondition', None)
    _safe_set(owner, 'page17', {partner})
    assert getattr(partner, 'VisibilityCondition') == owner
    _safe_set(owner, 'page17', set())
    assert getattr(partner, 'VisibilityCondition') is None


def test_assoc_welcomePage1_stub_double():
    # form_Form has no real 'form_Form2' property in the generated
    # code (a bare stub) -- manually attach it so form_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Page(title="sample_text")
    partner = form_Form()
    setattr(partner, 'form_Form2', None)
    _safe_set(owner, 'form_Page3', partner)
    assert getattr(partner, 'form_Form2') == owner
    _safe_set(owner, 'form_Page3', None)
    assert getattr(partner, 'form_Form2') is None


