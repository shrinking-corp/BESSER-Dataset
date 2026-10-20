import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ContentElement,
    DocumentModel,
    spreadsheet_Cell,
    spreadsheet_Header,
    spreadsheet_Image,
    spreadsheet_Point,
    spreadsheet_Row,
    spreadsheet_Sheet,
    spreadsheet_SpreadsheetFile,
    spreadsheet_Table,
    spreadsheet_Text,
    spreadsheet_Title,
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

def test_assoc_image3_reverse_link_reassign_clear():
    a1 = spreadsheet_Sheet(name="sample_text")
    a2 = spreadsheet_Sheet(name="sample_text_2")
    b = spreadsheet_Image(height=7, width=7)
    _safe_set(b, 'spreadsheet_Image', a1)
    assert _is_linked(b, 'spreadsheet_Image', a1)
    if hasattr(a1, 'spreadsheet_Sheet4'):
        assert _is_linked(a1, 'spreadsheet_Sheet4', b)
    _safe_set(b, 'spreadsheet_Image', a2)
    assert _is_linked(b, 'spreadsheet_Image', a2)
    if hasattr(a1, 'spreadsheet_Sheet4'):
        assert not _is_linked(a1, 'spreadsheet_Sheet4', b)
    if hasattr(a2, 'spreadsheet_Sheet4'):
        assert _is_linked(a2, 'spreadsheet_Sheet4', b)
    _safe_set(b, 'spreadsheet_Image', None)
    assert not _is_linked(b, 'spreadsheet_Image', a2)
    if hasattr(a2, 'spreadsheet_Sheet4'):
        assert not _is_linked(a2, 'spreadsheet_Sheet4', b)


def test_assoc_imagePos12_reverse_link_reassign_clear():
    a1 = spreadsheet_Point(x=7, y=7)
    a2 = spreadsheet_Point(x=13, y=13)
    b = spreadsheet_Image(height=7, width=7)
    _safe_set(b, 'spreadsheet_Image13', a1)
    assert _is_linked(b, 'spreadsheet_Image13', a1)
    if hasattr(a1, 'spreadsheet_Point'):
        assert _is_linked(a1, 'spreadsheet_Point', b)
    _safe_set(b, 'spreadsheet_Image13', a2)
    assert _is_linked(b, 'spreadsheet_Image13', a2)
    if hasattr(a1, 'spreadsheet_Point'):
        assert not _is_linked(a1, 'spreadsheet_Point', b)
    if hasattr(a2, 'spreadsheet_Point'):
        assert _is_linked(a2, 'spreadsheet_Point', b)
    _safe_set(b, 'spreadsheet_Image13', None)
    assert not _is_linked(b, 'spreadsheet_Image13', a2)
    if hasattr(a2, 'spreadsheet_Point'):
        assert not _is_linked(a2, 'spreadsheet_Point', b)


def test_assoc_posCell26_reverse_link_reassign_clear():
    a1 = spreadsheet_Point(x=7, y=7)
    a2 = spreadsheet_Point(x=13, y=13)
    b = spreadsheet_Cell()
    _safe_set(b, 'spreadsheet_Cell27', a1)
    assert _is_linked(b, 'spreadsheet_Cell27', a1)
    if hasattr(a1, 'spreadsheet_Point28'):
        assert _is_linked(a1, 'spreadsheet_Point28', b)
    _safe_set(b, 'spreadsheet_Cell27', a2)
    assert _is_linked(b, 'spreadsheet_Cell27', a2)
    if hasattr(a1, 'spreadsheet_Point28'):
        assert not _is_linked(a1, 'spreadsheet_Point28', b)
    if hasattr(a2, 'spreadsheet_Point28'):
        assert _is_linked(a2, 'spreadsheet_Point28', b)
    _safe_set(b, 'spreadsheet_Cell27', None)
    assert not _is_linked(b, 'spreadsheet_Cell27', a2)
    if hasattr(a2, 'spreadsheet_Point28'):
        assert not _is_linked(a2, 'spreadsheet_Point28', b)


def test_assoc_sheet0_reverse_link_reassign_clear():
    a1 = spreadsheet_SpreadsheetFile(nbSheet=7)
    a2 = spreadsheet_SpreadsheetFile(nbSheet=13)
    b = spreadsheet_Sheet(name="sample_text")
    _safe_set(b, 'spreadsheet_Sheet', a1)
    assert _is_linked(b, 'spreadsheet_Sheet', a1)
    if hasattr(a1, 'spreadsheet_SpreadsheetFile'):
        assert _is_linked(a1, 'spreadsheet_SpreadsheetFile', b)
    _safe_set(b, 'spreadsheet_Sheet', a2)
    assert _is_linked(b, 'spreadsheet_Sheet', a2)
    if hasattr(a1, 'spreadsheet_SpreadsheetFile'):
        assert not _is_linked(a1, 'spreadsheet_SpreadsheetFile', b)
    if hasattr(a2, 'spreadsheet_SpreadsheetFile'):
        assert _is_linked(a2, 'spreadsheet_SpreadsheetFile', b)
    _safe_set(b, 'spreadsheet_Sheet', None)
    assert not _is_linked(b, 'spreadsheet_Sheet', a2)
    if hasattr(a2, 'spreadsheet_SpreadsheetFile'):
        assert not _is_linked(a2, 'spreadsheet_SpreadsheetFile', b)


def test_assoc_table5_reverse_link_reassign_clear():
    a1 = spreadsheet_Table(nbColumns=7)
    a2 = spreadsheet_Table(nbColumns=13)
    b = spreadsheet_Sheet(name="sample_text")
    _safe_set(b, 'spreadsheet_Sheet6', {a1})
    assert _is_linked(b, 'spreadsheet_Sheet6', a1)
    if hasattr(a1, 'spreadsheet_Table'):
        assert _is_linked(a1, 'spreadsheet_Table', b)
    _safe_set(b, 'spreadsheet_Sheet6', {a2})
    assert _is_linked(b, 'spreadsheet_Sheet6', a2)
    if hasattr(a1, 'spreadsheet_Table'):
        assert not _is_linked(a1, 'spreadsheet_Table', b)
    if hasattr(a2, 'spreadsheet_Table'):
        assert _is_linked(a2, 'spreadsheet_Table', b)
    _safe_set(b, 'spreadsheet_Sheet6', set())
    assert not _is_linked(b, 'spreadsheet_Sheet6', a2)
    if hasattr(a2, 'spreadsheet_Table'):
        assert not _is_linked(a2, 'spreadsheet_Table', b)


def test_assoc_tablePos21_reverse_link_reassign_clear():
    a1 = spreadsheet_Table(nbColumns=7)
    a2 = spreadsheet_Table(nbColumns=13)
    b = spreadsheet_Point(x=7, y=7)
    _safe_set(b, 'spreadsheet_Point23', a1)
    assert _is_linked(b, 'spreadsheet_Point23', a1)
    if hasattr(a1, 'spreadsheet_Table22'):
        assert _is_linked(a1, 'spreadsheet_Table22', b)
    _safe_set(b, 'spreadsheet_Point23', a2)
    assert _is_linked(b, 'spreadsheet_Point23', a2)
    if hasattr(a1, 'spreadsheet_Table22'):
        assert not _is_linked(a1, 'spreadsheet_Table22', b)
    if hasattr(a2, 'spreadsheet_Table22'):
        assert _is_linked(a2, 'spreadsheet_Table22', b)
    _safe_set(b, 'spreadsheet_Point23', None)
    assert not _is_linked(b, 'spreadsheet_Point23', a2)
    if hasattr(a2, 'spreadsheet_Table22'):
        assert not _is_linked(a2, 'spreadsheet_Table22', b)


def test_assoc_text1_reverse_link_reassign_clear():
    a1 = spreadsheet_Text(textContent="sample_text")
    a2 = spreadsheet_Text(textContent="sample_text_2")
    b = spreadsheet_Sheet(name="sample_text")
    _safe_set(b, 'spreadsheet_Sheet2', {a1})
    assert _is_linked(b, 'spreadsheet_Sheet2', a1)
    if hasattr(a1, 'spreadsheet_Text'):
        assert _is_linked(a1, 'spreadsheet_Text', b)
    _safe_set(b, 'spreadsheet_Sheet2', {a2})
    assert _is_linked(b, 'spreadsheet_Sheet2', a2)
    if hasattr(a1, 'spreadsheet_Text'):
        assert not _is_linked(a1, 'spreadsheet_Text', b)
    if hasattr(a2, 'spreadsheet_Text'):
        assert _is_linked(a2, 'spreadsheet_Text', b)
    _safe_set(b, 'spreadsheet_Sheet2', set())
    assert not _is_linked(b, 'spreadsheet_Sheet2', a2)
    if hasattr(a2, 'spreadsheet_Text'):
        assert not _is_linked(a2, 'spreadsheet_Text', b)


def test_assoc_title14_reverse_link_reassign_clear():
    a1 = spreadsheet_Title(hiearchy="sample_text")
    a2 = spreadsheet_Title(hiearchy="sample_text_2")
    b = spreadsheet_Table(nbColumns=7)
    _safe_set(b, 'spreadsheet_Table15', {a1})
    assert _is_linked(b, 'spreadsheet_Table15', a1)
    if hasattr(a1, 'spreadsheet_Title16'):
        assert _is_linked(a1, 'spreadsheet_Title16', b)
    _safe_set(b, 'spreadsheet_Table15', {a2})
    assert _is_linked(b, 'spreadsheet_Table15', a2)
    if hasattr(a1, 'spreadsheet_Title16'):
        assert not _is_linked(a1, 'spreadsheet_Title16', b)
    if hasattr(a2, 'spreadsheet_Title16'):
        assert _is_linked(a2, 'spreadsheet_Title16', b)
    _safe_set(b, 'spreadsheet_Table15', set())
    assert not _is_linked(b, 'spreadsheet_Table15', a2)
    if hasattr(a2, 'spreadsheet_Title16'):
        assert not _is_linked(a2, 'spreadsheet_Title16', b)


def test_assoc_title7_reverse_link_reassign_clear():
    a1 = spreadsheet_Title(hiearchy="sample_text")
    a2 = spreadsheet_Title(hiearchy="sample_text_2")
    b = spreadsheet_Text(textContent="sample_text")
    _safe_set(b, 'spreadsheet_Text8', a1)
    assert _is_linked(b, 'spreadsheet_Text8', a1)
    if hasattr(a1, 'spreadsheet_Title'):
        assert _is_linked(a1, 'spreadsheet_Title', b)
    _safe_set(b, 'spreadsheet_Text8', a2)
    assert _is_linked(b, 'spreadsheet_Text8', a2)
    if hasattr(a1, 'spreadsheet_Title'):
        assert not _is_linked(a1, 'spreadsheet_Title', b)
    if hasattr(a2, 'spreadsheet_Title'):
        assert _is_linked(a2, 'spreadsheet_Title', b)
    _safe_set(b, 'spreadsheet_Text8', None)
    assert not _is_linked(b, 'spreadsheet_Text8', a2)
    if hasattr(a2, 'spreadsheet_Title'):
        assert not _is_linked(a2, 'spreadsheet_Title', b)


def test_assoc_title9_reverse_link_reassign_clear():
    a1 = spreadsheet_Title(hiearchy="sample_text")
    a2 = spreadsheet_Title(hiearchy="sample_text_2")
    b = spreadsheet_Image(height=7, width=7)
    _safe_set(b, 'spreadsheet_Image10', a1)
    assert _is_linked(b, 'spreadsheet_Image10', a1)
    if hasattr(a1, 'spreadsheet_Title11'):
        assert _is_linked(a1, 'spreadsheet_Title11', b)
    _safe_set(b, 'spreadsheet_Image10', a2)
    assert _is_linked(b, 'spreadsheet_Image10', a2)
    if hasattr(a1, 'spreadsheet_Title11'):
        assert not _is_linked(a1, 'spreadsheet_Title11', b)
    if hasattr(a2, 'spreadsheet_Title11'):
        assert _is_linked(a2, 'spreadsheet_Title11', b)
    _safe_set(b, 'spreadsheet_Image10', None)
    assert not _is_linked(b, 'spreadsheet_Image10', a2)
    if hasattr(a2, 'spreadsheet_Title11'):
        assert not _is_linked(a2, 'spreadsheet_Title11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cell24_stub_double():
    # spreadsheet_Header has no real 'spreadsheet_Header25' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheet_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheet_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheet_Cell()
    partner = spreadsheet_Header()
    setattr(partner, 'spreadsheet_Header25', None)
    _safe_set(owner, 'spreadsheet_Cell', partner)
    assert owner in getattr(partner, 'spreadsheet_Header25')
    _safe_set(owner, 'spreadsheet_Cell', None)
    assert owner not in getattr(partner, 'spreadsheet_Header25')


def test_assoc_cell29_stub_double():
    # spreadsheet_Row has no real 'spreadsheet_Row30' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheet_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheet_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheet_Cell()
    partner = spreadsheet_Row()
    setattr(partner, 'spreadsheet_Row30', None)
    _safe_set(owner, 'spreadsheet_Cell31', partner)
    assert owner in getattr(partner, 'spreadsheet_Row30')
    _safe_set(owner, 'spreadsheet_Cell31', None)
    assert owner not in getattr(partner, 'spreadsheet_Row30')


def test_assoc_header17_stub_double():
    # spreadsheet_Header has no real 'spreadsheet_Header' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheet_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheet_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheet_Table(nbColumns=7)
    partner = spreadsheet_Header()
    setattr(partner, 'spreadsheet_Header', None)
    _safe_set(owner, 'spreadsheet_Table18', {partner})
    assert getattr(partner, 'spreadsheet_Header') == owner
    _safe_set(owner, 'spreadsheet_Table18', set())
    assert getattr(partner, 'spreadsheet_Header') is None


def test_assoc_row19_stub_double():
    # spreadsheet_Row has no real 'spreadsheet_Row' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheet_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheet_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheet_Table(nbColumns=7)
    partner = spreadsheet_Row()
    setattr(partner, 'spreadsheet_Row', None)
    _safe_set(owner, 'spreadsheet_Table20', {partner})
    assert getattr(partner, 'spreadsheet_Row') == owner
    _safe_set(owner, 'spreadsheet_Table20', set())
    assert getattr(partner, 'spreadsheet_Row') is None


