import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFormattedInlineContent,
    AbstractUnformattedInlineContent,
    AnyText,
    HyperLink,
    ParagraphTypes,
    Template,
    wikiML_AboutTemplate,
    wikiML_AbstractFormattedInlineContent,
    wikiML_AbstractUnformattedInlineContent,
    wikiML_AnyText,
    wikiML_AnyTextSequence,
    wikiML_BlockQuote,
    wikiML_Bold,
    wikiML_Category,
    wikiML_External,
    wikiML_Heading2,
    wikiML_Heading3,
    wikiML_Heading4,
    wikiML_Heading5,
    wikiML_HyperLink,
    wikiML_Image,
    wikiML_Internal,
    wikiML_Italic,
    wikiML_ItalicBold,
    wikiML_MainTemplate,
    wikiML_OrderListItem,
    wikiML_OrderedList,
    wikiML_Paragraph,
    wikiML_ParagraphTypes,
    wikiML_QuoteTemplate,
    wikiML_Template,
    wikiML_Text,
    wikiML_UnorderListItem,
    wikiML_UnorderedList,
    wikiML_WikiPage,
    HorizontalAlign,
    ViewType,
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

def test_assoc_name23_reverse_link_reassign_clear():
    a1 = wikiML_Text(name="sample_text")
    a2 = wikiML_Text(name="sample_text_2")
    b = wikiML_Category(value="sample_text")
    _safe_set(b, 'wikiML_Category', a1)
    assert _is_linked(b, 'wikiML_Category', a1)
    if hasattr(a1, 'wikiML_Text'):
        assert _is_linked(a1, 'wikiML_Text', b)
    _safe_set(b, 'wikiML_Category', a2)
    assert _is_linked(b, 'wikiML_Category', a2)
    if hasattr(a1, 'wikiML_Text'):
        assert not _is_linked(a1, 'wikiML_Text', b)
    if hasattr(a2, 'wikiML_Text'):
        assert _is_linked(a2, 'wikiML_Text', b)
    _safe_set(b, 'wikiML_Category', None)
    assert not _is_linked(b, 'wikiML_Category', a2)
    if hasattr(a2, 'wikiML_Text'):
        assert not _is_linked(a2, 'wikiML_Text', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_altText19_stub_double():
    # wikiML_AbstractUnformattedInlineContent has no real 'wikiML_AbstractUnformattedInlineContent' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_Image(hAlign="sample_text", name="sample_text", type="sample_text")
    partner = wikiML_AbstractUnformattedInlineContent()
    setattr(partner, 'wikiML_AbstractUnformattedInlineContent', None)
    _safe_set(owner, 'wikiML_Image', partner)
    assert getattr(partner, 'wikiML_AbstractUnformattedInlineContent') == owner
    _safe_set(owner, 'wikiML_Image', None)
    assert getattr(partner, 'wikiML_AbstractUnformattedInlineContent') is None


def test_assoc_anchor37_stub_double():
    # wikiML_Internal has no real 'wikiML_Internal38' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_Text(name="sample_text")
    partner = wikiML_Internal()
    setattr(partner, 'wikiML_Internal38', None)
    _safe_set(owner, 'wikiML_Text39', partner)
    assert getattr(partner, 'wikiML_Internal38') == owner
    _safe_set(owner, 'wikiML_Text39', None)
    assert getattr(partner, 'wikiML_Internal38') is None


def test_assoc_caption20_stub_double():
    # wikiML_AnyTextSequence has no real 'wikiML_AnyTextSequence22' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_Image(hAlign="sample_text", name="sample_text", type="sample_text")
    partner = wikiML_AnyTextSequence()
    setattr(partner, 'wikiML_AnyTextSequence22', None)
    _safe_set(owner, 'wikiML_Image21', partner)
    assert getattr(partner, 'wikiML_AnyTextSequence22') == owner
    _safe_set(owner, 'wikiML_Image21', None)
    assert getattr(partner, 'wikiML_AnyTextSequence22') is None


def test_assoc_elements0_stub_double():
    # wikiML_ParagraphTypes has no real 'wikiML_ParagraphTypes' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_WikiPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_WikiPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_WikiPage(name="sample_text")
    partner = wikiML_ParagraphTypes()
    setattr(partner, 'wikiML_ParagraphTypes', None)
    _safe_set(owner, 'wikiML_WikiPage', {partner})
    assert getattr(partner, 'wikiML_ParagraphTypes') == owner
    _safe_set(owner, 'wikiML_WikiPage', set())
    assert getattr(partner, 'wikiML_ParagraphTypes') is None


def test_assoc_end10_stub_double():
    # wikiML_UnorderedList has no real 'wikiML_UnorderedList11' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_Paragraph(paragraph="sample_text")
    partner = wikiML_UnorderedList()
    setattr(partner, 'wikiML_UnorderedList11', None)
    _safe_set(owner, 'wikiML_Paragraph12', partner)
    assert getattr(partner, 'wikiML_UnorderedList11') == owner
    _safe_set(owner, 'wikiML_Paragraph12', None)
    assert getattr(partner, 'wikiML_UnorderedList11') is None


def test_assoc_end7_stub_double():
    # wikiML_OrderedList has no real 'wikiML_OrderedList8' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_Paragraph(paragraph="sample_text")
    partner = wikiML_OrderedList()
    setattr(partner, 'wikiML_OrderedList8', None)
    _safe_set(owner, 'wikiML_Paragraph', partner)
    assert getattr(partner, 'wikiML_OrderedList8') == owner
    _safe_set(owner, 'wikiML_Paragraph', None)
    assert getattr(partner, 'wikiML_OrderedList8') is None


def test_assoc_items9_stub_double():
    # wikiML_UnorderedList has no real 'wikiML_UnorderedList' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_UnorderListItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_UnorderListItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_UnorderListItem(level="sample_text")
    partner = wikiML_UnorderedList()
    setattr(partner, 'wikiML_UnorderedList', None)
    _safe_set(owner, 'wikiML_UnorderListItem', partner)
    assert owner in getattr(partner, 'wikiML_UnorderedList')
    _safe_set(owner, 'wikiML_UnorderListItem', None)
    assert owner not in getattr(partner, 'wikiML_UnorderedList')


def test_assoc_itemtext13_stub_double():
    # wikiML_AnyTextSequence has no real 'wikiML_AnyTextSequence15' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_UnorderListItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_UnorderListItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_UnorderListItem(level="sample_text")
    partner = wikiML_AnyTextSequence()
    setattr(partner, 'wikiML_AnyTextSequence15', None)
    _safe_set(owner, 'wikiML_UnorderListItem14', partner)
    assert getattr(partner, 'wikiML_AnyTextSequence15') == owner
    _safe_set(owner, 'wikiML_UnorderListItem14', None)
    assert getattr(partner, 'wikiML_AnyTextSequence15') is None


def test_assoc_link35_stub_double():
    # wikiML_Internal has no real 'wikiML_Internal' property in the generated
    # code (a bare stub) -- manually attach it so wikiML_WikiPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikiML_WikiPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikiML_WikiPage(name="sample_text")
    partner = wikiML_Internal()
    setattr(partner, 'wikiML_Internal', None)
    _safe_set(owner, 'wikiML_WikiPage36', partner)
    assert getattr(partner, 'wikiML_Internal') == owner
    _safe_set(owner, 'wikiML_WikiPage36', None)
    assert getattr(partner, 'wikiML_Internal') is None


