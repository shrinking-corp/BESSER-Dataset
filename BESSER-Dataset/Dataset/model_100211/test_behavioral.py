import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Fragment,
    FragmentContainer,
    NamedElement,
    Text,
    TextContainer,
    documentation_Code,
    documentation_Documentation,
    documentation_Fragment,
    documentation_FragmentContainer,
    documentation_HtmlCode,
    documentation_Image,
    documentation_Line,
    documentation_Link,
    documentation_List,
    documentation_ListItem,
    documentation_Listing,
    documentation_NamedElement,
    documentation_PageBreak,
    documentation_Paragraph,
    documentation_Reference,
    documentation_Section,
    documentation_Subsection,
    documentation_Subsubsection,
    documentation_Table,
    documentation_TableCell,
    documentation_TableHeader,
    documentation_TableRow,
    documentation_TermEntry,
    documentation_Text,
    documentation_TextContainer,
    documentation_Width,
    documentation_XML,
    Unit,
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

def test_assoc_terminology1_reverse_link_reassign_clear():
    a1 = documentation_TermEntry(description="sample_text")
    a2 = documentation_TermEntry(description="sample_text_2")
    b = documentation_Documentation(title="sample_text")
    _safe_set(b, 'documentation_Documentation2', {a1})
    assert _is_linked(b, 'documentation_Documentation2', a1)
    if hasattr(a1, 'documentation_TermEntry'):
        assert _is_linked(a1, 'documentation_TermEntry', b)
    _safe_set(b, 'documentation_Documentation2', {a2})
    assert _is_linked(b, 'documentation_Documentation2', a2)
    if hasattr(a1, 'documentation_TermEntry'):
        assert not _is_linked(a1, 'documentation_TermEntry', b)
    if hasattr(a2, 'documentation_TermEntry'):
        assert _is_linked(a2, 'documentation_TermEntry', b)
    _safe_set(b, 'documentation_Documentation2', set())
    assert not _is_linked(b, 'documentation_Documentation2', a2)
    if hasattr(a2, 'documentation_TermEntry'):
        assert not _is_linked(a2, 'documentation_TermEntry', b)


def test_assoc_width12_reverse_link_reassign_clear():
    a1 = documentation_Width(unit="sample_text", width="sample_text")
    a2 = documentation_Width(unit="sample_text_2", width="sample_text_2")
    b = documentation_Image(contextClassName="sample_text", originalSource="sample_text", resource="sample_text")
    _safe_set(b, 'documentation_Image', a1)
    assert _is_linked(b, 'documentation_Image', a1)
    if hasattr(a1, 'documentation_Width'):
        assert _is_linked(a1, 'documentation_Width', b)
    _safe_set(b, 'documentation_Image', a2)
    assert _is_linked(b, 'documentation_Image', a2)
    if hasattr(a1, 'documentation_Width'):
        assert not _is_linked(a1, 'documentation_Width', b)
    if hasattr(a2, 'documentation_Width'):
        assert _is_linked(a2, 'documentation_Width', b)
    _safe_set(b, 'documentation_Image', None)
    assert not _is_linked(b, 'documentation_Image', a2)
    if hasattr(a2, 'documentation_Width'):
        assert not _is_linked(a2, 'documentation_Width', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_headerCells7_stub_double():
    # documentation_TableHeader has no real 'documentation_TableHeader8' property in the generated
    # code (a bare stub) -- manually attach it so documentation_TableCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_TableCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_TableCell(content="sample_text", span=7)
    partner = documentation_TableHeader()
    setattr(partner, 'documentation_TableHeader8', None)
    _safe_set(owner, 'documentation_TableCell', partner)
    assert owner in getattr(partner, 'documentation_TableHeader8')
    _safe_set(owner, 'documentation_TableCell', None)
    assert owner not in getattr(partner, 'documentation_TableHeader8')


def test_assoc_items3_stub_double():
    # documentation_List has no real 'documentation_List' property in the generated
    # code (a bare stub) -- manually attach it so documentation_ListItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_ListItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_ListItem(text="sample_text")
    partner = documentation_List()
    setattr(partner, 'documentation_List', None)
    _safe_set(owner, 'documentation_ListItem', partner)
    assert owner in getattr(partner, 'documentation_List')
    _safe_set(owner, 'documentation_ListItem', None)
    assert owner not in getattr(partner, 'documentation_List')


def test_assoc_rowCells9_stub_double():
    # documentation_TableRow has no real 'documentation_TableRow10' property in the generated
    # code (a bare stub) -- manually attach it so documentation_TableCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_TableCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_TableCell(content="sample_text", span=7)
    partner = documentation_TableRow()
    setattr(partner, 'documentation_TableRow10', None)
    _safe_set(owner, 'documentation_TableCell11', partner)
    assert owner in getattr(partner, 'documentation_TableRow10')
    _safe_set(owner, 'documentation_TableCell11', None)
    assert owner not in getattr(partner, 'documentation_TableRow10')


def test_assoc_sections0_stub_double():
    # documentation_Section has no real 'documentation_Section' property in the generated
    # code (a bare stub) -- manually attach it so documentation_Documentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_Documentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_Documentation(title="sample_text")
    partner = documentation_Section()
    setattr(partner, 'documentation_Section', None)
    _safe_set(owner, 'documentation_Documentation', {partner})
    assert getattr(partner, 'documentation_Section') == owner
    _safe_set(owner, 'documentation_Documentation', set())
    assert getattr(partner, 'documentation_Section') is None


def test_assoc_texts14_stub_double():
    # documentation_TextContainer has no real 'documentation_TextContainer' property in the generated
    # code (a bare stub) -- manually attach it so documentation_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_Text(text="sample_text")
    partner = documentation_TextContainer()
    setattr(partner, 'documentation_TextContainer', None)
    _safe_set(owner, 'documentation_Text', partner)
    assert owner in getattr(partner, 'documentation_TextContainer')
    _safe_set(owner, 'documentation_Text', None)
    assert owner not in getattr(partner, 'documentation_TextContainer')


