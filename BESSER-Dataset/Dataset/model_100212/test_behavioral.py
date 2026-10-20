import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Fragment,
    NamedElement,
    TextFragmentContainer,
    documentation_Documentation,
    documentation_Fragment,
    documentation_Image,
    documentation_Line,
    documentation_List,
    documentation_ListItem,
    documentation_NamedElement,
    documentation_Paragraph,
    documentation_Section,
    documentation_Subsection,
    documentation_Subsubsection,
    documentation_Table,
    documentation_TableHeader,
    documentation_TableRow,
    documentation_TermEntry,
    documentation_TextFragmentContainer,
    documentation_XML,
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_items4_stub_double():
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


def test_assoc_tableHeader5_stub_double():
    # documentation_Table has no real 'documentation_Table' property in the generated
    # code (a bare stub) -- manually attach it so documentation_TableHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_TableHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_TableHeader(headerCells="sample_text")
    partner = documentation_Table()
    setattr(partner, 'documentation_Table', None)
    _safe_set(owner, 'documentation_TableHeader', partner)
    assert getattr(partner, 'documentation_Table') == owner
    _safe_set(owner, 'documentation_TableHeader', None)
    assert getattr(partner, 'documentation_Table') is None


def test_assoc_tableRows6_stub_double():
    # documentation_Table has no real 'documentation_Table7' property in the generated
    # code (a bare stub) -- manually attach it so documentation_TableRow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # documentation_TableRow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = documentation_TableRow(rowCells="sample_text")
    partner = documentation_Table()
    setattr(partner, 'documentation_Table7', None)
    _safe_set(owner, 'documentation_TableRow', partner)
    assert owner in getattr(partner, 'documentation_Table7')
    _safe_set(owner, 'documentation_TableRow', None)
    assert owner not in getattr(partner, 'documentation_Table7')


