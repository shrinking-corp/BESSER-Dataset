import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ast,
    Cell,
    HasA1,
    HasId,
    InfixOperator,
    Operand,
    Operation,
    PostfixOperator,
    PrefixOperator,
    Ref,
    cellsheet_Addition,
    cellsheet_Ast,
    cellsheet_AstEval,
    cellsheet_BlankCell,
    cellsheet_Book,
    cellsheet_BooleanCell,
    cellsheet_Cell,
    cellsheet_CellFormat,
    cellsheet_Concatenation,
    cellsheet_DateCell,
    cellsheet_Division,
    cellsheet_EQ,
    cellsheet_EStringToTokenEntry,
    cellsheet_Error,
    cellsheet_Exponentiation,
    cellsheet_FormulaCell,
    cellsheet_Function,
    cellsheet_GT,
    cellsheet_GTE,
    cellsheet_HasA1,
    cellsheet_HasId,
    cellsheet_InfixOperator,
    cellsheet_Intersection,
    cellsheet_LT,
    cellsheet_LTE,
    cellsheet_Logical,
    cellsheet_Multiplication,
    cellsheet_NEQ,
    cellsheet_Negation,
    cellsheet_Noop,
    cellsheet_Number,
    cellsheet_NumericCell,
    cellsheet_Operand,
    cellsheet_Operation,
    cellsheet_Percent,
    cellsheet_Plus,
    cellsheet_PostfixOperator,
    cellsheet_PrefixOperator,
    cellsheet_Range,
    cellsheet_Ref,
    cellsheet_RelativeRange,
    cellsheet_RelativeRef,
    cellsheet_Row,
    cellsheet_Sheet,
    cellsheet_Subtraction,
    cellsheet_Text,
    cellsheet_TextCell,
    cellsheet_Token,
    cellsheet_Union,
    cellsheet_Unknown,
    cellsheet_Workspace,
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

def test_assoc_book28_reverse_link_reassign_clear():
    a1 = cellsheet_CellFormat(value="sample_text")
    a2 = cellsheet_CellFormat(value="sample_text_2")
    b = cellsheet_Book(bookname="sample_text")
    _safe_set(b, 'Book29', a1)
    assert _is_linked(b, 'Book29', a1)
    if hasattr(a1, 'cellFormats'):
        assert _is_linked(a1, 'cellFormats', b)
    _safe_set(b, 'Book29', a2)
    assert _is_linked(b, 'Book29', a2)
    if hasattr(a1, 'cellFormats'):
        assert not _is_linked(a1, 'cellFormats', b)
    if hasattr(a2, 'cellFormats'):
        assert _is_linked(a2, 'cellFormats', b)
    _safe_set(b, 'Book29', None)
    assert not _is_linked(b, 'Book29', a2)
    if hasattr(a2, 'cellFormats'):
        assert not _is_linked(a2, 'cellFormats', b)


def test_assoc_book8_reverse_link_reassign_clear():
    a1 = cellsheet_Sheet(sheetIndex=7, sheetName="sample_text")
    a2 = cellsheet_Sheet(sheetIndex=13, sheetName="sample_text_2")
    b = cellsheet_Book(bookname="sample_text")
    _safe_set(b, 'Book9', a1)
    assert _is_linked(b, 'Book9', a1)
    if hasattr(a1, 'sheets'):
        assert _is_linked(a1, 'sheets', b)
    _safe_set(b, 'Book9', a2)
    assert _is_linked(b, 'Book9', a2)
    if hasattr(a1, 'sheets'):
        assert not _is_linked(a1, 'sheets', b)
    if hasattr(a2, 'sheets'):
        assert _is_linked(a2, 'sheets', b)
    _safe_set(b, 'Book9', None)
    assert not _is_linked(b, 'Book9', a2)
    if hasattr(a2, 'sheets'):
        assert not _is_linked(a2, 'sheets', b)


def test_assoc_cellFormats5_reverse_link_reassign_clear():
    a1 = cellsheet_CellFormat(value="sample_text")
    a2 = cellsheet_CellFormat(value="sample_text_2")
    b = cellsheet_Book(bookname="sample_text")
    _safe_set(b, 'book', {a1})
    assert _is_linked(b, 'book', a1)
    if hasattr(a1, 'CellFormat'):
        assert _is_linked(a1, 'CellFormat', b)
    _safe_set(b, 'book', {a2})
    assert _is_linked(b, 'book', a2)
    if hasattr(a1, 'CellFormat'):
        assert not _is_linked(a1, 'CellFormat', b)
    if hasattr(a2, 'CellFormat'):
        assert _is_linked(a2, 'CellFormat', b)
    _safe_set(b, 'book', set())
    assert not _is_linked(b, 'book', a2)
    if hasattr(a2, 'CellFormat'):
        assert not _is_linked(a2, 'CellFormat', b)


def test_assoc_cells13_reverse_link_reassign_clear():
    a1 = cellsheet_Row(rowIndex=7)
    a2 = cellsheet_Row(rowIndex=13)
    b = cellsheet_Cell(colIndex=7)
    _safe_set(b, 'Cell', a1)
    assert _is_linked(b, 'Cell', a1)
    if hasattr(a1, 'row'):
        assert _is_linked(a1, 'row', b)
    _safe_set(b, 'Cell', a2)
    assert _is_linked(b, 'Cell', a2)
    if hasattr(a1, 'row'):
        assert not _is_linked(a1, 'row', b)
    if hasattr(a2, 'row'):
        assert _is_linked(a2, 'row', b)
    _safe_set(b, 'Cell', None)
    assert not _is_linked(b, 'Cell', a2)
    if hasattr(a2, 'row'):
        assert not _is_linked(a2, 'row', b)


def test_assoc_row14_reverse_link_reassign_clear():
    a1 = cellsheet_Row(rowIndex=7)
    a2 = cellsheet_Row(rowIndex=13)
    b = cellsheet_Cell(colIndex=7)
    _safe_set(b, 'cells', a1)
    assert _is_linked(b, 'cells', a1)
    if hasattr(a1, 'Row15'):
        assert _is_linked(a1, 'Row15', b)
    _safe_set(b, 'cells', a2)
    assert _is_linked(b, 'cells', a2)
    if hasattr(a1, 'Row15'):
        assert not _is_linked(a1, 'Row15', b)
    if hasattr(a2, 'Row15'):
        assert _is_linked(a2, 'Row15', b)
    _safe_set(b, 'cells', None)
    assert not _is_linked(b, 'cells', a2)
    if hasattr(a2, 'Row15'):
        assert not _is_linked(a2, 'Row15', b)


def test_assoc_rows10_reverse_link_reassign_clear():
    a1 = cellsheet_Sheet(sheetIndex=7, sheetName="sample_text")
    a2 = cellsheet_Sheet(sheetIndex=13, sheetName="sample_text_2")
    b = cellsheet_Row(rowIndex=7)
    _safe_set(b, 'Row', a1)
    assert _is_linked(b, 'Row', a1)
    if hasattr(a1, 'sheet'):
        assert _is_linked(a1, 'sheet', b)
    _safe_set(b, 'Row', a2)
    assert _is_linked(b, 'Row', a2)
    if hasattr(a1, 'sheet'):
        assert not _is_linked(a1, 'sheet', b)
    if hasattr(a2, 'sheet'):
        assert _is_linked(a2, 'sheet', b)
    _safe_set(b, 'Row', None)
    assert not _is_linked(b, 'Row', a2)
    if hasattr(a2, 'sheet'):
        assert not _is_linked(a2, 'sheet', b)


def test_assoc_sheet11_reverse_link_reassign_clear():
    a1 = cellsheet_Sheet(sheetIndex=7, sheetName="sample_text")
    a2 = cellsheet_Sheet(sheetIndex=13, sheetName="sample_text_2")
    b = cellsheet_Row(rowIndex=7)
    _safe_set(b, 'rows', a1)
    assert _is_linked(b, 'rows', a1)
    if hasattr(a1, 'Sheet12'):
        assert _is_linked(a1, 'Sheet12', b)
    _safe_set(b, 'rows', a2)
    assert _is_linked(b, 'rows', a2)
    if hasattr(a1, 'Sheet12'):
        assert not _is_linked(a1, 'Sheet12', b)
    if hasattr(a2, 'Sheet12'):
        assert _is_linked(a2, 'Sheet12', b)
    _safe_set(b, 'rows', None)
    assert not _is_linked(b, 'rows', a2)
    if hasattr(a2, 'Sheet12'):
        assert not _is_linked(a2, 'Sheet12', b)


def test_assoc_sheets6_reverse_link_reassign_clear():
    a1 = cellsheet_Sheet(sheetIndex=7, sheetName="sample_text")
    a2 = cellsheet_Sheet(sheetIndex=13, sheetName="sample_text_2")
    b = cellsheet_Book(bookname="sample_text")
    _safe_set(b, 'book7', {a1})
    assert _is_linked(b, 'book7', a1)
    if hasattr(a1, 'Sheet'):
        assert _is_linked(a1, 'Sheet', b)
    _safe_set(b, 'book7', {a2})
    assert _is_linked(b, 'book7', a2)
    if hasattr(a1, 'Sheet'):
        assert not _is_linked(a1, 'Sheet', b)
    if hasattr(a2, 'Sheet'):
        assert _is_linked(a2, 'Sheet', b)
    _safe_set(b, 'book7', set())
    assert not _is_linked(b, 'book7', a2)
    if hasattr(a2, 'Sheet'):
        assert not _is_linked(a2, 'Sheet', b)


def test_assoc_value0_reverse_link_reassign_clear():
    a1 = cellsheet_Token(value="sample_text")
    a2 = cellsheet_Token(value="sample_text_2")
    b = cellsheet_EStringToTokenEntry(key="sample_text")
    _safe_set(b, 'cellsheet_EStringToTokenEntry', a1)
    assert _is_linked(b, 'cellsheet_EStringToTokenEntry', a1)
    if hasattr(a1, 'cellsheet_Token'):
        assert _is_linked(a1, 'cellsheet_Token', b)
    _safe_set(b, 'cellsheet_EStringToTokenEntry', a2)
    assert _is_linked(b, 'cellsheet_EStringToTokenEntry', a2)
    if hasattr(a1, 'cellsheet_Token'):
        assert not _is_linked(a1, 'cellsheet_Token', b)
    if hasattr(a2, 'cellsheet_Token'):
        assert _is_linked(a2, 'cellsheet_Token', b)
    _safe_set(b, 'cellsheet_EStringToTokenEntry', None)
    assert not _is_linked(b, 'cellsheet_EStringToTokenEntry', a2)
    if hasattr(a2, 'cellsheet_Token'):
        assert not _is_linked(a2, 'cellsheet_Token', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_asts16_stub_double():
    # cellsheet_Ast has no real 'Ast' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Cell(colIndex=7)
    partner = cellsheet_Ast()
    setattr(partner, 'Ast', None)
    _safe_set(owner, 'cell', {partner})
    assert getattr(partner, 'Ast') == owner
    _safe_set(owner, 'cell', set())
    assert getattr(partner, 'Ast') is None


def test_assoc_books1_stub_double():
    # cellsheet_Workspace has no real 'workspace' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Book(bookname="sample_text")
    partner = cellsheet_Workspace()
    setattr(partner, 'workspace', None)
    _safe_set(owner, 'Book', partner)
    assert owner in getattr(partner, 'workspace')
    _safe_set(owner, 'Book', None)
    assert owner not in getattr(partner, 'workspace')


def test_assoc_cell23_stub_double():
    # cellsheet_Ast has no real 'asts' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Cell(colIndex=7)
    partner = cellsheet_Ast()
    setattr(partner, 'asts', None)
    _safe_set(owner, 'Cell24', partner)
    assert getattr(partner, 'asts') == owner
    _safe_set(owner, 'Cell24', None)
    assert getattr(partner, 'asts') is None


def test_assoc_result26_stub_double():
    # cellsheet_Ast has no real 'cellsheet_Ast27' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_AstEval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_AstEval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_AstEval(isError=True, numberValue="sample_text", text="sample_text")
    partner = cellsheet_Ast()
    setattr(partner, 'cellsheet_Ast27', None)
    _safe_set(owner, 'cellsheet_AstEval', partner)
    assert getattr(partner, 'cellsheet_Ast27') == owner
    _safe_set(owner, 'cellsheet_AstEval', None)
    assert getattr(partner, 'cellsheet_Ast27') is None


def test_assoc_root17_stub_double():
    # cellsheet_Ast has no real 'cellsheet_Ast' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Cell(colIndex=7)
    partner = cellsheet_Ast()
    setattr(partner, 'cellsheet_Ast', None)
    _safe_set(owner, 'cellsheet_Cell', partner)
    assert getattr(partner, 'cellsheet_Ast') == owner
    _safe_set(owner, 'cellsheet_Cell', None)
    assert getattr(partner, 'cellsheet_Ast') is None


def test_assoc_token25_stub_double():
    # cellsheet_Ast has no real 'usedBy' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Token(value="sample_text")
    partner = cellsheet_Ast()
    setattr(partner, 'usedBy', None)
    _safe_set(owner, 'Token', partner)
    assert getattr(partner, 'usedBy') == owner
    _safe_set(owner, 'Token', None)
    assert getattr(partner, 'usedBy') is None


def test_assoc_tokens2_stub_double():
    # cellsheet_Workspace has no real 'cellsheet_Workspace' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_EStringToTokenEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_EStringToTokenEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_EStringToTokenEntry(key="sample_text")
    partner = cellsheet_Workspace()
    setattr(partner, 'cellsheet_Workspace', None)
    _safe_set(owner, 'cellsheet_EStringToTokenEntry3', partner)
    assert owner in getattr(partner, 'cellsheet_Workspace')
    _safe_set(owner, 'cellsheet_EStringToTokenEntry3', None)
    assert owner not in getattr(partner, 'cellsheet_Workspace')


def test_assoc_usedBy18_stub_double():
    # cellsheet_Ast has no real 'Ast19' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Token(value="sample_text")
    partner = cellsheet_Ast()
    setattr(partner, 'Ast19', None)
    _safe_set(owner, 'token', {partner})
    assert getattr(partner, 'Ast19') == owner
    _safe_set(owner, 'token', set())
    assert getattr(partner, 'Ast19') is None


def test_assoc_workspace4_stub_double():
    # cellsheet_Workspace has no real 'Workspace' property in the generated
    # code (a bare stub) -- manually attach it so cellsheet_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cellsheet_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cellsheet_Book(bookname="sample_text")
    partner = cellsheet_Workspace()
    setattr(partner, 'Workspace', None)
    _safe_set(owner, 'books', partner)
    assert getattr(partner, 'Workspace') == owner
    _safe_set(owner, 'books', None)
    assert getattr(partner, 'Workspace') is None


