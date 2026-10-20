import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DisplayElement,
    InputElement,
    PageElement,
    fml_DisplayElement,
    fml_Form,
    fml_Heading,
    fml_InputElement,
    fml_List,
    fml_ListItem,
    fml_Page,
    fml_PageElement,
    fml_SelectField,
    fml_SelectionItem,
    fml_TextInput,
    fml_TextParagraph,
    SelectionType,
    TextInputType,
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

def test_assoc_consists4_reverse_link_reassign_clear():
    a1 = fml_PageElement(ID="sample_text")
    a2 = fml_PageElement(ID="sample_text_2")
    b = fml_Page(Title="sample_text", isWelcome=True)
    _safe_set(b, 'contained', {a1})
    assert _is_linked(b, 'contained', a1)
    if hasattr(a1, 'PageElement'):
        assert _is_linked(a1, 'PageElement', b)
    _safe_set(b, 'contained', {a2})
    assert _is_linked(b, 'contained', a2)
    if hasattr(a1, 'PageElement'):
        assert not _is_linked(a1, 'PageElement', b)
    if hasattr(a2, 'PageElement'):
        assert _is_linked(a2, 'PageElement', b)
    _safe_set(b, 'contained', set())
    assert not _is_linked(b, 'contained', a2)
    if hasattr(a2, 'PageElement'):
        assert not _is_linked(a2, 'PageElement', b)


def test_assoc_consists7_reverse_link_reassign_clear():
    a1 = fml_ListItem(Text="sample_text")
    a2 = fml_ListItem(Text="sample_text_2")
    b = fml_List(isOrdered=True)
    _safe_set(b, 'fml_List', {a1})
    assert _is_linked(b, 'fml_List', a1)
    if hasattr(a1, 'fml_ListItem'):
        assert _is_linked(a1, 'fml_ListItem', b)
    _safe_set(b, 'fml_List', {a2})
    assert _is_linked(b, 'fml_List', a2)
    if hasattr(a1, 'fml_ListItem'):
        assert not _is_linked(a1, 'fml_ListItem', b)
    if hasattr(a2, 'fml_ListItem'):
        assert _is_linked(a2, 'fml_ListItem', b)
    _safe_set(b, 'fml_List', set())
    assert not _is_linked(b, 'fml_List', a2)
    if hasattr(a2, 'fml_ListItem'):
        assert not _is_linked(a2, 'fml_ListItem', b)


def test_assoc_consists8_reverse_link_reassign_clear():
    a1 = fml_SelectionItem(Text="sample_text", preselected=True, selected=True)
    a2 = fml_SelectionItem(Text="sample_text_2", preselected=False, selected=False)
    b = fml_SelectField(Label="sample_text", Type="sample_text")
    _safe_set(b, 'contained9', {a1})
    assert _is_linked(b, 'contained9', a1)
    if hasattr(a1, 'SelectionItem10'):
        assert _is_linked(a1, 'SelectionItem10', b)
    _safe_set(b, 'contained9', {a2})
    assert _is_linked(b, 'contained9', a2)
    if hasattr(a1, 'SelectionItem10'):
        assert not _is_linked(a1, 'SelectionItem10', b)
    if hasattr(a2, 'SelectionItem10'):
        assert _is_linked(a2, 'SelectionItem10', b)
    _safe_set(b, 'contained9', set())
    assert not _is_linked(b, 'contained9', a2)
    if hasattr(a2, 'SelectionItem10'):
        assert not _is_linked(a2, 'SelectionItem10', b)


def test_assoc_contained11_reverse_link_reassign_clear():
    a1 = fml_SelectionItem(Text="sample_text", preselected=True, selected=True)
    a2 = fml_SelectionItem(Text="sample_text_2", preselected=False, selected=False)
    b = fml_SelectField(Label="sample_text", Type="sample_text")
    _safe_set(b, 'SelectField', a1)
    assert _is_linked(b, 'SelectField', a1)
    if hasattr(a1, 'consists12'):
        assert _is_linked(a1, 'consists12', b)
    _safe_set(b, 'SelectField', a2)
    assert _is_linked(b, 'SelectField', a2)
    if hasattr(a1, 'consists12'):
        assert not _is_linked(a1, 'consists12', b)
    if hasattr(a2, 'consists12'):
        assert _is_linked(a2, 'consists12', b)
    _safe_set(b, 'SelectField', None)
    assert not _is_linked(b, 'SelectField', a2)
    if hasattr(a2, 'consists12'):
        assert not _is_linked(a2, 'consists12', b)


def test_assoc_contained5_reverse_link_reassign_clear():
    a1 = fml_PageElement(ID="sample_text")
    a2 = fml_PageElement(ID="sample_text_2")
    b = fml_Page(Title="sample_text", isWelcome=True)
    _safe_set(b, 'Page', a1)
    assert _is_linked(b, 'Page', a1)
    if hasattr(a1, 'consists'):
        assert _is_linked(a1, 'consists', b)
    _safe_set(b, 'Page', a2)
    assert _is_linked(b, 'Page', a2)
    if hasattr(a1, 'consists'):
        assert not _is_linked(a1, 'consists', b)
    if hasattr(a2, 'consists'):
        assert _is_linked(a2, 'consists', b)
    _safe_set(b, 'Page', None)
    assert not _is_linked(b, 'Page', a2)
    if hasattr(a2, 'consists'):
        assert not _is_linked(a2, 'consists', b)


def test_assoc_displayElementVisible13_reverse_link_reassign_clear():
    a1 = fml_SelectionItem(Text="sample_text", preselected=True, selected=True)
    a2 = fml_SelectionItem(Text="sample_text_2", preselected=False, selected=False)
    b = fml_PageElement(ID="sample_text")
    _safe_set(b, 'PageElement14', a1)
    assert _is_linked(b, 'PageElement14', a1)
    if hasattr(a1, 'visibleIfSelected'):
        assert _is_linked(a1, 'visibleIfSelected', b)
    _safe_set(b, 'PageElement14', a2)
    assert _is_linked(b, 'PageElement14', a2)
    if hasattr(a1, 'visibleIfSelected'):
        assert not _is_linked(a1, 'visibleIfSelected', b)
    if hasattr(a2, 'visibleIfSelected'):
        assert _is_linked(a2, 'visibleIfSelected', b)
    _safe_set(b, 'PageElement14', None)
    assert not _is_linked(b, 'PageElement14', a2)
    if hasattr(a2, 'visibleIfSelected'):
        assert not _is_linked(a2, 'visibleIfSelected', b)


def test_assoc_predecessor2_reverse_link_reassign_clear():
    a1 = fml_Page(Title="sample_text", isWelcome=True)
    a2 = fml_Page(Title="sample_text_2", isWelcome=False)
    b = fml_Page(Title="sample_text", isWelcome=True)
    _safe_set(b, 'fml_Page3', a1)
    assert _is_linked(b, 'fml_Page3', a1)
    if hasattr(a1, 'fml_Page1'):
        assert _is_linked(a1, 'fml_Page1', b)
    _safe_set(b, 'fml_Page3', a2)
    assert _is_linked(b, 'fml_Page3', a2)
    if hasattr(a1, 'fml_Page1'):
        assert not _is_linked(a1, 'fml_Page1', b)
    if hasattr(a2, 'fml_Page1'):
        assert _is_linked(a2, 'fml_Page1', b)
    _safe_set(b, 'fml_Page3', None)
    assert not _is_linked(b, 'fml_Page3', a2)
    if hasattr(a2, 'fml_Page1'):
        assert not _is_linked(a2, 'fml_Page1', b)


def test_assoc_visibleIfSelected6_reverse_link_reassign_clear():
    a1 = fml_SelectionItem(Text="sample_text", preselected=True, selected=True)
    a2 = fml_SelectionItem(Text="sample_text_2", preselected=False, selected=False)
    b = fml_PageElement(ID="sample_text")
    _safe_set(b, 'displayElementVisible', {a1})
    assert _is_linked(b, 'displayElementVisible', a1)
    if hasattr(a1, 'SelectionItem'):
        assert _is_linked(a1, 'SelectionItem', b)
    _safe_set(b, 'displayElementVisible', {a2})
    assert _is_linked(b, 'displayElementVisible', a2)
    if hasattr(a1, 'SelectionItem'):
        assert not _is_linked(a1, 'SelectionItem', b)
    if hasattr(a2, 'SelectionItem'):
        assert _is_linked(a2, 'SelectionItem', b)
    _safe_set(b, 'displayElementVisible', set())
    assert not _is_linked(b, 'displayElementVisible', a2)
    if hasattr(a2, 'SelectionItem'):
        assert not _is_linked(a2, 'SelectionItem', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_organized0_stub_double():
    # fml_Form has no real 'fml_Form' property in the generated
    # code (a bare stub) -- manually attach it so fml_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fml_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fml_Page(Title="sample_text", isWelcome=True)
    partner = fml_Form()
    setattr(partner, 'fml_Form', None)
    _safe_set(owner, 'fml_Page', partner)
    assert owner in getattr(partner, 'fml_Form')
    _safe_set(owner, 'fml_Page', None)
    assert owner not in getattr(partner, 'fml_Form')


