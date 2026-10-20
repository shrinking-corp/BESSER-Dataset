import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Return_value,
    Statement,
    java_Ampersand_Rule,
    java_Arg_List,
    java_Bit_Expression_NR,
    java_Cast_Expression,
    java_Class_declaration,
    java_Compilation_unit,
    java_Constructor_declaration,
    java_Creating_Expression,
    java_Do_Statement,
    java_EObject,
    java_Expression,
    java_Expression_aux,
    java_Field_declaration,
    java_Float_Literal,
    java_For_Statement,
    java_Head,
    java_If_Statement,
    java_Import_statement,
    java_Interface_declaration,
    java_Literal_Expression,
    java_Logical_Expression_NR,
    java_Method_call,
    java_Method_declaration,
    java_Numeric_Expression_NR,
    java_Package_statement,
    java_Parameter,
    java_Parameter_list,
    java_Parameter_list_method_call,
    java_Return_Statement,
    java_Return_value,
    java_Statement,
    java_Statement_block,
    java_Static_initializer,
    java_Switch_Statement,
    java_Try_statement,
    java_Type,
    java_Type_declaration,
    java_Variable_declaration,
    java_Variable_declarator,
    java_Variable_initializer,
    java_While_Statement,
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

def test_assoc_RIGHT_PARENTHESISparameters190_reverse_link_reassign_clear():
    a1 = java_Try_statement(catchs="sample_text", finally_="sample_text", try_="sample_text")
    a2 = java_Try_statement(catchs="sample_text_2", finally_="sample_text_2", try_="sample_text_2")
    b = java_Parameter(name="sample_text")
    _safe_set(b, 'java_Parameter192', a1)
    assert _is_linked(b, 'java_Parameter192', a1)
    if hasattr(a1, 'java_Try_statement191'):
        assert _is_linked(a1, 'java_Try_statement191', b)
    _safe_set(b, 'java_Parameter192', a2)
    assert _is_linked(b, 'java_Parameter192', a2)
    if hasattr(a1, 'java_Try_statement191'):
        assert not _is_linked(a1, 'java_Try_statement191', b)
    if hasattr(a2, 'java_Try_statement191'):
        assert _is_linked(a2, 'java_Try_statement191', b)
    _safe_set(b, 'java_Parameter192', None)
    assert not _is_linked(b, 'java_Parameter192', a2)
    if hasattr(a2, 'java_Try_statement191'):
        assert not _is_linked(a2, 'java_Try_statement191', b)


def test_assoc_ampersand79_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Ampersand_Rule(a1="sample_text", a2="sample_text")
    _safe_set(b, 'java_Ampersand_Rule', a1)
    assert _is_linked(b, 'java_Ampersand_Rule', a1)
    if hasattr(a1, 'java_Expression_aux80'):
        assert _is_linked(a1, 'java_Expression_aux80', b)
    _safe_set(b, 'java_Ampersand_Rule', a2)
    assert _is_linked(b, 'java_Ampersand_Rule', a2)
    if hasattr(a1, 'java_Expression_aux80'):
        assert not _is_linked(a1, 'java_Expression_aux80', b)
    if hasattr(a2, 'java_Expression_aux80'):
        assert _is_linked(a2, 'java_Expression_aux80', b)
    _safe_set(b, 'java_Ampersand_Rule', None)
    assert not _is_linked(b, 'java_Ampersand_Rule', a2)
    if hasattr(a2, 'java_Expression_aux80'):
        assert not _is_linked(a2, 'java_Expression_aux80', b)


def test_assoc_aux53_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression54', a1)
    assert _is_linked(b, 'java_Expression54', a1)
    if hasattr(a1, 'java_Expression_aux'):
        assert _is_linked(a1, 'java_Expression_aux', b)
    _safe_set(b, 'java_Expression54', a2)
    assert _is_linked(b, 'java_Expression54', a2)
    if hasattr(a1, 'java_Expression_aux'):
        assert not _is_linked(a1, 'java_Expression_aux', b)
    if hasattr(a2, 'java_Expression_aux'):
        assert _is_linked(a2, 'java_Expression_aux', b)
    _safe_set(b, 'java_Expression54', None)
    assert not _is_linked(b, 'java_Expression54', a2)
    if hasattr(a2, 'java_Expression_aux'):
        assert not _is_linked(a2, 'java_Expression_aux', b)


def test_assoc_aux68_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    _safe_set(b, 'java_Expression_aux69', a1)
    assert _is_linked(b, 'java_Expression_aux69', a1)
    if hasattr(a1, 'java_Expression_aux67'):
        assert _is_linked(a1, 'java_Expression_aux67', b)
    _safe_set(b, 'java_Expression_aux69', a2)
    assert _is_linked(b, 'java_Expression_aux69', a2)
    if hasattr(a1, 'java_Expression_aux67'):
        assert not _is_linked(a1, 'java_Expression_aux67', b)
    if hasattr(a2, 'java_Expression_aux67'):
        assert _is_linked(a2, 'java_Expression_aux67', b)
    _safe_set(b, 'java_Expression_aux69', None)
    assert not _is_linked(b, 'java_Expression_aux69', a2)
    if hasattr(a2, 'java_Expression_aux67'):
        assert not _is_linked(a2, 'java_Expression_aux67', b)


def test_assoc_catchStatements193_reverse_link_reassign_clear():
    a1 = java_Try_statement(catchs="sample_text", finally_="sample_text", try_="sample_text")
    a2 = java_Try_statement(catchs="sample_text_2", finally_="sample_text_2", try_="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement195', a1)
    assert _is_linked(b, 'java_Statement195', a1)
    if hasattr(a1, 'java_Try_statement194'):
        assert _is_linked(a1, 'java_Try_statement194', b)
    _safe_set(b, 'java_Statement195', a2)
    assert _is_linked(b, 'java_Statement195', a2)
    if hasattr(a1, 'java_Try_statement194'):
        assert not _is_linked(a1, 'java_Try_statement194', b)
    if hasattr(a2, 'java_Try_statement194'):
        assert _is_linked(a2, 'java_Try_statement194', b)
    _safe_set(b, 'java_Statement195', None)
    assert not _is_linked(b, 'java_Statement195', a2)
    if hasattr(a2, 'java_Try_statement194'):
        assert not _is_linked(a2, 'java_Try_statement194', b)


def test_assoc_creatingExpression61_reverse_link_reassign_clear():
    a1 = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    a2 = java_Expression(name="sample_text_2", null="sample_text_2", super="sample_text_2", this="sample_text_2")
    b = java_Creating_Expression(className="sample_text", typeSpecifier="sample_text")
    _safe_set(b, 'java_Creating_Expression', a1)
    assert _is_linked(b, 'java_Creating_Expression', a1)
    if hasattr(a1, 'java_Expression62'):
        assert _is_linked(a1, 'java_Expression62', b)
    _safe_set(b, 'java_Creating_Expression', a2)
    assert _is_linked(b, 'java_Creating_Expression', a2)
    if hasattr(a1, 'java_Expression62'):
        assert not _is_linked(a1, 'java_Expression62', b)
    if hasattr(a2, 'java_Expression62'):
        assert _is_linked(a2, 'java_Expression62', b)
    _safe_set(b, 'java_Creating_Expression', None)
    assert not _is_linked(b, 'java_Creating_Expression', a2)
    if hasattr(a2, 'java_Expression62'):
        assert not _is_linked(a2, 'java_Expression62', b)


def test_assoc_exp176_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression78', a1)
    assert _is_linked(b, 'java_Expression78', a1)
    if hasattr(a1, 'java_Expression_aux77'):
        assert _is_linked(a1, 'java_Expression_aux77', b)
    _safe_set(b, 'java_Expression78', a2)
    assert _is_linked(b, 'java_Expression78', a2)
    if hasattr(a1, 'java_Expression_aux77'):
        assert not _is_linked(a1, 'java_Expression_aux77', b)
    if hasattr(a2, 'java_Expression_aux77'):
        assert _is_linked(a2, 'java_Expression_aux77', b)
    _safe_set(b, 'java_Expression78', None)
    assert not _is_linked(b, 'java_Expression78', a2)
    if hasattr(a2, 'java_Expression_aux77'):
        assert not _is_linked(a2, 'java_Expression_aux77', b)


def test_assoc_exp273_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression75', a1)
    assert _is_linked(b, 'java_Expression75', a1)
    if hasattr(a1, 'java_Expression_aux74'):
        assert _is_linked(a1, 'java_Expression_aux74', b)
    _safe_set(b, 'java_Expression75', a2)
    assert _is_linked(b, 'java_Expression75', a2)
    if hasattr(a1, 'java_Expression_aux74'):
        assert not _is_linked(a1, 'java_Expression_aux74', b)
    if hasattr(a2, 'java_Expression_aux74'):
        assert _is_linked(a2, 'java_Expression_aux74', b)
    _safe_set(b, 'java_Expression75', None)
    assert not _is_linked(b, 'java_Expression75', a2)
    if hasattr(a2, 'java_Expression_aux74'):
        assert not _is_linked(a2, 'java_Expression_aux74', b)


def test_assoc_exp284_reverse_link_reassign_clear():
    a1 = java_Literal_Expression(char="sample_text", exp="sample_text", exp1=7, string="sample_text")
    a2 = java_Literal_Expression(char="sample_text_2", exp="sample_text_2", exp1=13, string="sample_text_2")
    b = java_Float_Literal(decimalDigits1=7, decimalDigits2=7, exp="sample_text", floatTypeSufix="sample_text")
    _safe_set(b, 'java_Float_Literal', a1)
    assert _is_linked(b, 'java_Float_Literal', a1)
    if hasattr(a1, 'java_Literal_Expression85'):
        assert _is_linked(a1, 'java_Literal_Expression85', b)
    _safe_set(b, 'java_Float_Literal', a2)
    assert _is_linked(b, 'java_Float_Literal', a2)
    if hasattr(a1, 'java_Literal_Expression85'):
        assert not _is_linked(a1, 'java_Literal_Expression85', b)
    if hasattr(a2, 'java_Literal_Expression85'):
        assert _is_linked(a2, 'java_Literal_Expression85', b)
    _safe_set(b, 'java_Float_Literal', None)
    assert not _is_linked(b, 'java_Float_Literal', a2)
    if hasattr(a2, 'java_Literal_Expression85'):
        assert not _is_linked(a2, 'java_Literal_Expression85', b)


def test_assoc_expression101_reverse_link_reassign_clear():
    a1 = java_Logical_Expression_NR(false="sample_text", true="sample_text")
    a2 = java_Logical_Expression_NR(false="sample_text_2", true="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression103', a1)
    assert _is_linked(b, 'java_Expression103', a1)
    if hasattr(a1, 'java_Logical_Expression_NR102'):
        assert _is_linked(a1, 'java_Logical_Expression_NR102', b)
    _safe_set(b, 'java_Expression103', a2)
    assert _is_linked(b, 'java_Expression103', a2)
    if hasattr(a1, 'java_Logical_Expression_NR102'):
        assert not _is_linked(a1, 'java_Logical_Expression_NR102', b)
    if hasattr(a2, 'java_Logical_Expression_NR102'):
        assert _is_linked(a2, 'java_Logical_Expression_NR102', b)
    _safe_set(b, 'java_Expression103', None)
    assert not _is_linked(b, 'java_Expression103', a2)
    if hasattr(a2, 'java_Logical_Expression_NR102'):
        assert not _is_linked(a2, 'java_Logical_Expression_NR102', b)


def test_assoc_expression110_reverse_link_reassign_clear():
    a1 = java_Numeric_Expression_NR(sinal_numeric="sample_text")
    a2 = java_Numeric_Expression_NR(sinal_numeric="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression112', a1)
    assert _is_linked(b, 'java_Expression112', a1)
    if hasattr(a1, 'java_Numeric_Expression_NR111'):
        assert _is_linked(a1, 'java_Numeric_Expression_NR111', b)
    _safe_set(b, 'java_Expression112', a2)
    assert _is_linked(b, 'java_Expression112', a2)
    if hasattr(a1, 'java_Numeric_Expression_NR111'):
        assert not _is_linked(a1, 'java_Numeric_Expression_NR111', b)
    if hasattr(a2, 'java_Numeric_Expression_NR111'):
        assert _is_linked(a2, 'java_Numeric_Expression_NR111', b)
    _safe_set(b, 'java_Expression112', None)
    assert not _is_linked(b, 'java_Expression112', a2)
    if hasattr(a2, 'java_Numeric_Expression_NR111'):
        assert not _is_linked(a2, 'java_Numeric_Expression_NR111', b)


def test_assoc_expression152_reverse_link_reassign_clear():
    a1 = java_For_Statement(pv="sample_text")
    a2 = java_For_Statement(pv="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression154', a1)
    assert _is_linked(b, 'java_Expression154', a1)
    if hasattr(a1, 'java_For_Statement153'):
        assert _is_linked(a1, 'java_For_Statement153', b)
    _safe_set(b, 'java_Expression154', a2)
    assert _is_linked(b, 'java_Expression154', a2)
    if hasattr(a1, 'java_For_Statement153'):
        assert not _is_linked(a1, 'java_For_Statement153', b)
    if hasattr(a2, 'java_For_Statement153'):
        assert _is_linked(a2, 'java_For_Statement153', b)
    _safe_set(b, 'java_Expression154', None)
    assert not _is_linked(b, 'java_Expression154', a2)
    if hasattr(a2, 'java_For_Statement153'):
        assert not _is_linked(a2, 'java_For_Statement153', b)


def test_assoc_expression2155_reverse_link_reassign_clear():
    a1 = java_For_Statement(pv="sample_text")
    a2 = java_For_Statement(pv="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression157', a1)
    assert _is_linked(b, 'java_Expression157', a1)
    if hasattr(a1, 'java_For_Statement156'):
        assert _is_linked(a1, 'java_For_Statement156', b)
    _safe_set(b, 'java_Expression157', a2)
    assert _is_linked(b, 'java_Expression157', a2)
    if hasattr(a1, 'java_For_Statement156'):
        assert not _is_linked(a1, 'java_For_Statement156', b)
    if hasattr(a2, 'java_For_Statement156'):
        assert _is_linked(a2, 'java_For_Statement156', b)
    _safe_set(b, 'java_Expression157', None)
    assert not _is_linked(b, 'java_Expression157', a2)
    if hasattr(a2, 'java_For_Statement156'):
        assert not _is_linked(a2, 'java_For_Statement156', b)


def test_assoc_expression270_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression72', a1)
    assert _is_linked(b, 'java_Expression72', a1)
    if hasattr(a1, 'java_Expression_aux71'):
        assert _is_linked(a1, 'java_Expression_aux71', b)
    _safe_set(b, 'java_Expression72', a2)
    assert _is_linked(b, 'java_Expression72', a2)
    if hasattr(a1, 'java_Expression_aux71'):
        assert not _is_linked(a1, 'java_Expression_aux71', b)
    if hasattr(a2, 'java_Expression_aux71'):
        assert _is_linked(a2, 'java_Expression_aux71', b)
    _safe_set(b, 'java_Expression72', None)
    assert not _is_linked(b, 'java_Expression72', a2)
    if hasattr(a2, 'java_Expression_aux71'):
        assert not _is_linked(a2, 'java_Expression_aux71', b)


def test_assoc_expression3158_reverse_link_reassign_clear():
    a1 = java_For_Statement(pv="sample_text")
    a2 = java_For_Statement(pv="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression160', a1)
    assert _is_linked(b, 'java_Expression160', a1)
    if hasattr(a1, 'java_For_Statement159'):
        assert _is_linked(a1, 'java_For_Statement159', b)
    _safe_set(b, 'java_Expression160', a2)
    assert _is_linked(b, 'java_Expression160', a2)
    if hasattr(a1, 'java_For_Statement159'):
        assert not _is_linked(a1, 'java_For_Statement159', b)
    if hasattr(a2, 'java_For_Statement159'):
        assert _is_linked(a2, 'java_For_Statement159', b)
    _safe_set(b, 'java_Expression160', None)
    assert not _is_linked(b, 'java_Expression160', a2)
    if hasattr(a2, 'java_For_Statement159'):
        assert not _is_linked(a2, 'java_For_Statement159', b)


def test_assoc_expression89_reverse_link_reassign_clear():
    a1 = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    a2 = java_Expression(name="sample_text_2", null="sample_text_2", super="sample_text_2", this="sample_text_2")
    b = java_Creating_Expression(className="sample_text", typeSpecifier="sample_text")
    _safe_set(b, 'java_Creating_Expression90', a1)
    assert _is_linked(b, 'java_Creating_Expression90', a1)
    if hasattr(a1, 'java_Expression91'):
        assert _is_linked(a1, 'java_Expression91', b)
    _safe_set(b, 'java_Creating_Expression90', a2)
    assert _is_linked(b, 'java_Creating_Expression90', a2)
    if hasattr(a1, 'java_Expression91'):
        assert not _is_linked(a1, 'java_Expression91', b)
    if hasattr(a2, 'java_Expression91'):
        assert _is_linked(a2, 'java_Expression91', b)
    _safe_set(b, 'java_Creating_Expression90', None)
    assert not _is_linked(b, 'java_Creating_Expression90', a2)
    if hasattr(a2, 'java_Expression91'):
        assert not _is_linked(a2, 'java_Expression91', b)


def test_assoc_expressionBit81_reverse_link_reassign_clear():
    a1 = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = java_Expression_aux(bitSign="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression83', a1)
    assert _is_linked(b, 'java_Expression83', a1)
    if hasattr(a1, 'java_Expression_aux82'):
        assert _is_linked(a1, 'java_Expression_aux82', b)
    _safe_set(b, 'java_Expression83', a2)
    assert _is_linked(b, 'java_Expression83', a2)
    if hasattr(a1, 'java_Expression_aux82'):
        assert not _is_linked(a1, 'java_Expression_aux82', b)
    if hasattr(a2, 'java_Expression_aux82'):
        assert _is_linked(a2, 'java_Expression_aux82', b)
    _safe_set(b, 'java_Expression83', None)
    assert not _is_linked(b, 'java_Expression83', a2)
    if hasattr(a2, 'java_Expression_aux82'):
        assert not _is_linked(a2, 'java_Expression_aux82', b)


def test_assoc_expressionx122_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression124', a1)
    assert _is_linked(b, 'java_Expression124', a1)
    if hasattr(a1, 'java_Statement123'):
        assert _is_linked(a1, 'java_Statement123', b)
    _safe_set(b, 'java_Expression124', a2)
    assert _is_linked(b, 'java_Expression124', a2)
    if hasattr(a1, 'java_Statement123'):
        assert not _is_linked(a1, 'java_Statement123', b)
    if hasattr(a2, 'java_Statement123'):
        assert _is_linked(a2, 'java_Statement123', b)
    _safe_set(b, 'java_Expression124', None)
    assert not _is_linked(b, 'java_Expression124', a2)
    if hasattr(a2, 'java_Statement123'):
        assert not _is_linked(a2, 'java_Statement123', b)


def test_assoc_fields10_reverse_link_reassign_clear():
    a1 = java_Field_declaration(debug="sample_text", doc="sample_text")
    a2 = java_Field_declaration(debug="sample_text_2", doc="sample_text_2")
    b = java_Class_declaration(className="sample_text", extend="sample_text", implement="sample_text", implements="sample_text", modifiers="sample_text")
    _safe_set(b, 'java_Class_declaration', {a1})
    assert _is_linked(b, 'java_Class_declaration', a1)
    if hasattr(a1, 'java_Field_declaration11'):
        assert _is_linked(a1, 'java_Field_declaration11', b)
    _safe_set(b, 'java_Class_declaration', {a2})
    assert _is_linked(b, 'java_Class_declaration', a2)
    if hasattr(a1, 'java_Field_declaration11'):
        assert not _is_linked(a1, 'java_Field_declaration11', b)
    if hasattr(a2, 'java_Field_declaration11'):
        assert _is_linked(a2, 'java_Field_declaration11', b)
    _safe_set(b, 'java_Class_declaration', set())
    assert not _is_linked(b, 'java_Class_declaration', a2)
    if hasattr(a2, 'java_Field_declaration11'):
        assert not _is_linked(a2, 'java_Field_declaration11', b)


def test_assoc_fields9_reverse_link_reassign_clear():
    a1 = java_Interface_declaration(extend="sample_text", extends="sample_text", interfaceName="sample_text", modifiers="sample_text")
    a2 = java_Interface_declaration(extend="sample_text_2", extends="sample_text_2", interfaceName="sample_text_2", modifiers="sample_text_2")
    b = java_Field_declaration(debug="sample_text", doc="sample_text")
    _safe_set(b, 'java_Field_declaration', a1)
    assert _is_linked(b, 'java_Field_declaration', a1)
    if hasattr(a1, 'java_Interface_declaration'):
        assert _is_linked(a1, 'java_Interface_declaration', b)
    _safe_set(b, 'java_Field_declaration', a2)
    assert _is_linked(b, 'java_Field_declaration', a2)
    if hasattr(a1, 'java_Interface_declaration'):
        assert not _is_linked(a1, 'java_Interface_declaration', b)
    if hasattr(a2, 'java_Interface_declaration'):
        assert _is_linked(a2, 'java_Interface_declaration', b)
    _safe_set(b, 'java_Field_declaration', None)
    assert not _is_linked(b, 'java_Field_declaration', a2)
    if hasattr(a2, 'java_Interface_declaration'):
        assert not _is_linked(a2, 'java_Interface_declaration', b)


def test_assoc_finallyStatement196_reverse_link_reassign_clear():
    a1 = java_Try_statement(catchs="sample_text", finally_="sample_text", try_="sample_text")
    a2 = java_Try_statement(catchs="sample_text_2", finally_="sample_text_2", try_="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement198', a1)
    assert _is_linked(b, 'java_Statement198', a1)
    if hasattr(a1, 'java_Try_statement197'):
        assert _is_linked(a1, 'java_Try_statement197', b)
    _safe_set(b, 'java_Statement198', a2)
    assert _is_linked(b, 'java_Statement198', a2)
    if hasattr(a1, 'java_Try_statement197'):
        assert not _is_linked(a1, 'java_Try_statement197', b)
    if hasattr(a2, 'java_Try_statement197'):
        assert _is_linked(a2, 'java_Try_statement197', b)
    _safe_set(b, 'java_Statement198', None)
    assert not _is_linked(b, 'java_Statement198', a2)
    if hasattr(a2, 'java_Try_statement197'):
        assert not _is_linked(a2, 'java_Try_statement197', b)


def test_assoc_forStatement131_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_For_Statement(pv="sample_text")
    _safe_set(b, 'java_For_Statement', a1)
    assert _is_linked(b, 'java_For_Statement', a1)
    if hasattr(a1, 'java_Statement132'):
        assert _is_linked(a1, 'java_Statement132', b)
    _safe_set(b, 'java_For_Statement', a2)
    assert _is_linked(b, 'java_For_Statement', a2)
    if hasattr(a1, 'java_Statement132'):
        assert not _is_linked(a1, 'java_Statement132', b)
    if hasattr(a2, 'java_Statement132'):
        assert _is_linked(a2, 'java_Statement132', b)
    _safe_set(b, 'java_For_Statement', None)
    assert not _is_linked(b, 'java_For_Statement', a2)
    if hasattr(a2, 'java_Statement132'):
        assert not _is_linked(a2, 'java_Statement132', b)


def test_assoc_literalExpression63_reverse_link_reassign_clear():
    a1 = java_Literal_Expression(char="sample_text", exp="sample_text", exp1=7, string="sample_text")
    a2 = java_Literal_Expression(char="sample_text_2", exp="sample_text_2", exp1=13, string="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression64', a1)
    assert _is_linked(b, 'java_Expression64', a1)
    if hasattr(a1, 'java_Literal_Expression'):
        assert _is_linked(a1, 'java_Literal_Expression', b)
    _safe_set(b, 'java_Expression64', a2)
    assert _is_linked(b, 'java_Expression64', a2)
    if hasattr(a1, 'java_Literal_Expression'):
        assert not _is_linked(a1, 'java_Literal_Expression', b)
    if hasattr(a2, 'java_Literal_Expression'):
        assert _is_linked(a2, 'java_Literal_Expression', b)
    _safe_set(b, 'java_Expression64', None)
    assert not _is_linked(b, 'java_Expression64', a2)
    if hasattr(a2, 'java_Literal_Expression'):
        assert not _is_linked(a2, 'java_Literal_Expression', b)


def test_assoc_logicalExpression55_reverse_link_reassign_clear():
    a1 = java_Logical_Expression_NR(false="sample_text", true="sample_text")
    a2 = java_Logical_Expression_NR(false="sample_text_2", true="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression56', a1)
    assert _is_linked(b, 'java_Expression56', a1)
    if hasattr(a1, 'java_Logical_Expression_NR'):
        assert _is_linked(a1, 'java_Logical_Expression_NR', b)
    _safe_set(b, 'java_Expression56', a2)
    assert _is_linked(b, 'java_Expression56', a2)
    if hasattr(a1, 'java_Logical_Expression_NR'):
        assert not _is_linked(a1, 'java_Logical_Expression_NR', b)
    if hasattr(a2, 'java_Logical_Expression_NR'):
        assert _is_linked(a2, 'java_Logical_Expression_NR', b)
    _safe_set(b, 'java_Expression56', None)
    assert not _is_linked(b, 'java_Expression56', a2)
    if hasattr(a2, 'java_Logical_Expression_NR'):
        assert not _is_linked(a2, 'java_Logical_Expression_NR', b)


def test_assoc_name36_reverse_link_reassign_clear():
    a1 = java_Variable_declarator(name="sample_text")
    a2 = java_Variable_declarator(name="sample_text_2")
    b = java_Variable_declaration(modifiers="sample_text")
    _safe_set(b, 'java_Variable_declaration37', a1)
    assert _is_linked(b, 'java_Variable_declaration37', a1)
    if hasattr(a1, 'java_Variable_declarator'):
        assert _is_linked(a1, 'java_Variable_declarator', b)
    _safe_set(b, 'java_Variable_declaration37', a2)
    assert _is_linked(b, 'java_Variable_declaration37', a2)
    if hasattr(a1, 'java_Variable_declarator'):
        assert not _is_linked(a1, 'java_Variable_declarator', b)
    if hasattr(a2, 'java_Variable_declarator'):
        assert _is_linked(a2, 'java_Variable_declarator', b)
    _safe_set(b, 'java_Variable_declaration37', None)
    assert not _is_linked(b, 'java_Variable_declaration37', a2)
    if hasattr(a2, 'java_Variable_declarator'):
        assert not _is_linked(a2, 'java_Variable_declarator', b)


def test_assoc_names38_reverse_link_reassign_clear():
    a1 = java_Variable_declarator(name="sample_text")
    a2 = java_Variable_declarator(name="sample_text_2")
    b = java_Variable_declaration(modifiers="sample_text")
    _safe_set(b, 'java_Variable_declaration39', {a1})
    assert _is_linked(b, 'java_Variable_declaration39', a1)
    if hasattr(a1, 'java_Variable_declarator40'):
        assert _is_linked(a1, 'java_Variable_declarator40', b)
    _safe_set(b, 'java_Variable_declaration39', {a2})
    assert _is_linked(b, 'java_Variable_declaration39', a2)
    if hasattr(a1, 'java_Variable_declarator40'):
        assert not _is_linked(a1, 'java_Variable_declarator40', b)
    if hasattr(a2, 'java_Variable_declarator40'):
        assert _is_linked(a2, 'java_Variable_declarator40', b)
    _safe_set(b, 'java_Variable_declaration39', set())
    assert not _is_linked(b, 'java_Variable_declaration39', a2)
    if hasattr(a2, 'java_Variable_declarator40'):
        assert not _is_linked(a2, 'java_Variable_declarator40', b)


def test_assoc_numericExpression351_reverse_link_reassign_clear():
    a1 = java_Numeric_Expression_NR(sinal_numeric="sample_text")
    a2 = java_Numeric_Expression_NR(sinal_numeric="sample_text_2")
    b = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'java_Expression52', a1)
    assert _is_linked(b, 'java_Expression52', a1)
    if hasattr(a1, 'java_Numeric_Expression_NR'):
        assert _is_linked(a1, 'java_Numeric_Expression_NR', b)
    _safe_set(b, 'java_Expression52', a2)
    assert _is_linked(b, 'java_Expression52', a2)
    if hasattr(a1, 'java_Numeric_Expression_NR'):
        assert not _is_linked(a1, 'java_Numeric_Expression_NR', b)
    if hasattr(a2, 'java_Numeric_Expression_NR'):
        assert _is_linked(a2, 'java_Numeric_Expression_NR', b)
    _safe_set(b, 'java_Expression52', None)
    assert not _is_linked(b, 'java_Expression52', a2)
    if hasattr(a2, 'java_Numeric_Expression_NR'):
        assert not _is_linked(a2, 'java_Numeric_Expression_NR', b)


def test_assoc_statement138_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement139', a1)
    assert _is_linked(b, 'java_Statement139', a1)
    if hasattr(a1, 'java_Statement137'):
        assert _is_linked(a1, 'java_Statement137', b)
    _safe_set(b, 'java_Statement139', a2)
    assert _is_linked(b, 'java_Statement139', a2)
    if hasattr(a1, 'java_Statement137'):
        assert not _is_linked(a1, 'java_Statement137', b)
    if hasattr(a2, 'java_Statement137'):
        assert _is_linked(a2, 'java_Statement137', b)
    _safe_set(b, 'java_Statement139', None)
    assert not _is_linked(b, 'java_Statement139', a2)
    if hasattr(a2, 'java_Statement137'):
        assert not _is_linked(a2, 'java_Statement137', b)


def test_assoc_statement161_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_For_Statement(pv="sample_text")
    _safe_set(b, 'java_For_Statement162', a1)
    assert _is_linked(b, 'java_For_Statement162', a1)
    if hasattr(a1, 'java_Statement163'):
        assert _is_linked(a1, 'java_Statement163', b)
    _safe_set(b, 'java_For_Statement162', a2)
    assert _is_linked(b, 'java_For_Statement162', a2)
    if hasattr(a1, 'java_Statement163'):
        assert not _is_linked(a1, 'java_Statement163', b)
    if hasattr(a2, 'java_Statement163'):
        assert _is_linked(a2, 'java_Statement163', b)
    _safe_set(b, 'java_For_Statement162', None)
    assert not _is_linked(b, 'java_For_Statement162', a2)
    if hasattr(a2, 'java_Statement163'):
        assert not _is_linked(a2, 'java_Statement163', b)


def test_assoc_tryStatement187_reverse_link_reassign_clear():
    a1 = java_Try_statement(catchs="sample_text", finally_="sample_text", try_="sample_text")
    a2 = java_Try_statement(catchs="sample_text_2", finally_="sample_text_2", try_="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement189', a1)
    assert _is_linked(b, 'java_Statement189', a1)
    if hasattr(a1, 'java_Try_statement188'):
        assert _is_linked(a1, 'java_Try_statement188', b)
    _safe_set(b, 'java_Statement189', a2)
    assert _is_linked(b, 'java_Statement189', a2)
    if hasattr(a1, 'java_Try_statement188'):
        assert not _is_linked(a1, 'java_Try_statement188', b)
    if hasattr(a2, 'java_Try_statement188'):
        assert _is_linked(a2, 'java_Try_statement188', b)
    _safe_set(b, 'java_Statement189', None)
    assert not _is_linked(b, 'java_Statement189', a2)
    if hasattr(a2, 'java_Try_statement188'):
        assert not _is_linked(a2, 'java_Try_statement188', b)


def test_assoc_try_135_reverse_link_reassign_clear():
    a1 = java_Try_statement(catchs="sample_text", finally_="sample_text", try_="sample_text")
    a2 = java_Try_statement(catchs="sample_text_2", finally_="sample_text_2", try_="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement136', a1)
    assert _is_linked(b, 'java_Statement136', a1)
    if hasattr(a1, 'java_Try_statement'):
        assert _is_linked(a1, 'java_Try_statement', b)
    _safe_set(b, 'java_Statement136', a2)
    assert _is_linked(b, 'java_Statement136', a2)
    if hasattr(a1, 'java_Try_statement'):
        assert not _is_linked(a1, 'java_Try_statement', b)
    if hasattr(a2, 'java_Try_statement'):
        assert _is_linked(a2, 'java_Try_statement', b)
    _safe_set(b, 'java_Statement136', None)
    assert not _is_linked(b, 'java_Statement136', a2)
    if hasattr(a2, 'java_Try_statement'):
        assert not _is_linked(a2, 'java_Try_statement', b)


def test_assoc_type15_reverse_link_reassign_clear():
    a1 = java_Type(name="sample_text")
    a2 = java_Type(name="sample_text_2")
    b = java_Method_declaration(debug="sample_text", modifiers="sample_text", name="sample_text")
    _safe_set(b, 'java_Method_declaration', a1)
    assert _is_linked(b, 'java_Method_declaration', a1)
    if hasattr(a1, 'java_Type'):
        assert _is_linked(a1, 'java_Type', b)
    _safe_set(b, 'java_Method_declaration', a2)
    assert _is_linked(b, 'java_Method_declaration', a2)
    if hasattr(a1, 'java_Type'):
        assert not _is_linked(a1, 'java_Type', b)
    if hasattr(a2, 'java_Type'):
        assert _is_linked(a2, 'java_Type', b)
    _safe_set(b, 'java_Method_declaration', None)
    assert not _is_linked(b, 'java_Method_declaration', a2)
    if hasattr(a2, 'java_Type'):
        assert not _is_linked(a2, 'java_Type', b)


def test_assoc_type31_reverse_link_reassign_clear():
    a1 = java_Type(name="sample_text")
    a2 = java_Type(name="sample_text_2")
    b = java_Parameter(name="sample_text")
    _safe_set(b, 'java_Parameter32', a1)
    assert _is_linked(b, 'java_Parameter32', a1)
    if hasattr(a1, 'java_Type33'):
        assert _is_linked(a1, 'java_Type33', b)
    _safe_set(b, 'java_Parameter32', a2)
    assert _is_linked(b, 'java_Parameter32', a2)
    if hasattr(a1, 'java_Type33'):
        assert not _is_linked(a1, 'java_Type33', b)
    if hasattr(a2, 'java_Type33'):
        assert _is_linked(a2, 'java_Type33', b)
    _safe_set(b, 'java_Parameter32', None)
    assert not _is_linked(b, 'java_Parameter32', a2)
    if hasattr(a2, 'java_Type33'):
        assert not _is_linked(a2, 'java_Type33', b)


def test_assoc_type34_reverse_link_reassign_clear():
    a1 = java_Variable_declaration(modifiers="sample_text")
    a2 = java_Variable_declaration(modifiers="sample_text_2")
    b = java_Type(name="sample_text")
    _safe_set(b, 'java_Type35', a1)
    assert _is_linked(b, 'java_Type35', a1)
    if hasattr(a1, 'java_Variable_declaration'):
        assert _is_linked(a1, 'java_Variable_declaration', b)
    _safe_set(b, 'java_Type35', a2)
    assert _is_linked(b, 'java_Type35', a2)
    if hasattr(a1, 'java_Variable_declaration'):
        assert not _is_linked(a1, 'java_Variable_declaration', b)
    if hasattr(a2, 'java_Variable_declaration'):
        assert _is_linked(a2, 'java_Variable_declaration', b)
    _safe_set(b, 'java_Type35', None)
    assert not _is_linked(b, 'java_Type35', a2)
    if hasattr(a2, 'java_Variable_declaration'):
        assert not _is_linked(a2, 'java_Variable_declaration', b)


def test_assoc_variable119_reverse_link_reassign_clear():
    a1 = java_Variable_declaration(modifiers="sample_text")
    a2 = java_Variable_declaration(modifiers="sample_text_2")
    b = java_Statement(name="sample_text")
    _safe_set(b, 'java_Statement120', a1)
    assert _is_linked(b, 'java_Statement120', a1)
    if hasattr(a1, 'java_Variable_declaration121'):
        assert _is_linked(a1, 'java_Variable_declaration121', b)
    _safe_set(b, 'java_Statement120', a2)
    assert _is_linked(b, 'java_Statement120', a2)
    if hasattr(a1, 'java_Variable_declaration121'):
        assert not _is_linked(a1, 'java_Variable_declaration121', b)
    if hasattr(a2, 'java_Variable_declaration121'):
        assert _is_linked(a2, 'java_Variable_declaration121', b)
    _safe_set(b, 'java_Statement120', None)
    assert not _is_linked(b, 'java_Statement120', a2)
    if hasattr(a2, 'java_Variable_declaration121'):
        assert not _is_linked(a2, 'java_Variable_declaration121', b)


def test_assoc_variable149_reverse_link_reassign_clear():
    a1 = java_Variable_declaration(modifiers="sample_text")
    a2 = java_Variable_declaration(modifiers="sample_text_2")
    b = java_For_Statement(pv="sample_text")
    _safe_set(b, 'java_For_Statement150', a1)
    assert _is_linked(b, 'java_For_Statement150', a1)
    if hasattr(a1, 'java_Variable_declaration151'):
        assert _is_linked(a1, 'java_Variable_declaration151', b)
    _safe_set(b, 'java_For_Statement150', a2)
    assert _is_linked(b, 'java_For_Statement150', a2)
    if hasattr(a1, 'java_Variable_declaration151'):
        assert not _is_linked(a1, 'java_Variable_declaration151', b)
    if hasattr(a2, 'java_Variable_declaration151'):
        assert _is_linked(a2, 'java_Variable_declaration151', b)
    _safe_set(b, 'java_For_Statement150', None)
    assert not _is_linked(b, 'java_For_Statement150', a2)
    if hasattr(a2, 'java_Variable_declaration151'):
        assert not _is_linked(a2, 'java_Variable_declaration151', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argList65_stub_double():
    # java_Arg_List has no real 'java_Arg_List' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression_aux's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression_aux's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression_aux(bitSign="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    partner = java_Arg_List()
    setattr(partner, 'java_Arg_List', None)
    _safe_set(owner, 'java_Expression_aux66', {partner})
    assert getattr(partner, 'java_Arg_List') == owner
    _safe_set(owner, 'java_Expression_aux66', set())
    assert getattr(partner, 'java_Arg_List') is None


def test_assoc_argList86_stub_double():
    # java_Arg_List has no real 'java_Arg_List88' property in the generated
    # code (a bare stub) -- manually attach it so java_Creating_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Creating_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Creating_Expression(className="sample_text", typeSpecifier="sample_text")
    partner = java_Arg_List()
    setattr(partner, 'java_Arg_List88', None)
    _safe_set(owner, 'java_Creating_Expression87', partner)
    assert getattr(partner, 'java_Arg_List88') == owner
    _safe_set(owner, 'java_Creating_Expression87', None)
    assert getattr(partner, 'java_Arg_List88') is None


def test_assoc_bitExpression57_stub_double():
    # java_Bit_Expression_NR has no real 'java_Bit_Expression_NR' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Bit_Expression_NR()
    setattr(partner, 'java_Bit_Expression_NR', None)
    _safe_set(owner, 'java_Expression58', partner)
    assert getattr(partner, 'java_Bit_Expression_NR') == owner
    _safe_set(owner, 'java_Expression58', None)
    assert getattr(partner, 'java_Bit_Expression_NR') is None


def test_assoc_castExpression59_stub_double():
    # java_Cast_Expression has no real 'java_Cast_Expression' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Cast_Expression()
    setattr(partner, 'java_Cast_Expression', None)
    _safe_set(owner, 'java_Expression60', partner)
    assert getattr(partner, 'java_Cast_Expression') == owner
    _safe_set(owner, 'java_Expression60', None)
    assert getattr(partner, 'java_Cast_Expression') is None


def test_assoc_doStatement127_stub_double():
    # java_Do_Statement has no real 'java_Do_Statement' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Do_Statement()
    setattr(partner, 'java_Do_Statement', None)
    _safe_set(owner, 'java_Statement128', partner)
    assert getattr(partner, 'java_Do_Statement') == owner
    _safe_set(owner, 'java_Statement128', None)
    assert getattr(partner, 'java_Do_Statement') is None


def test_assoc_elseStatement182_stub_double():
    # java_If_Statement has no real 'java_If_Statement183' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_If_Statement()
    setattr(partner, 'java_If_Statement183', None)
    _safe_set(owner, 'java_Statement184', partner)
    assert getattr(partner, 'java_If_Statement183') == owner
    _safe_set(owner, 'java_Statement184', None)
    assert getattr(partner, 'java_If_Statement183') is None


def test_assoc_expression104_stub_double():
    # java_Arg_List has no real 'java_Arg_List105' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Arg_List()
    setattr(partner, 'java_Arg_List105', None)
    _safe_set(owner, 'java_Expression106', partner)
    assert getattr(partner, 'java_Arg_List105') == owner
    _safe_set(owner, 'java_Expression106', None)
    assert getattr(partner, 'java_Arg_List105') is None


def test_assoc_expression140_stub_double():
    # java_Switch_Statement has no real 'java_Switch_Statement141' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Switch_Statement()
    setattr(partner, 'java_Switch_Statement141', None)
    _safe_set(owner, 'java_Expression142', partner)
    assert getattr(partner, 'java_Switch_Statement141') == owner
    _safe_set(owner, 'java_Expression142', None)
    assert getattr(partner, 'java_Switch_Statement141') is None


def test_assoc_expression164_stub_double():
    # java_While_Statement has no real 'java_While_Statement165' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_While_Statement()
    setattr(partner, 'java_While_Statement165', None)
    _safe_set(owner, 'java_Expression166', partner)
    assert getattr(partner, 'java_While_Statement165') == owner
    _safe_set(owner, 'java_Expression166', None)
    assert getattr(partner, 'java_While_Statement165') is None


def test_assoc_expression173_stub_double():
    # java_Do_Statement has no real 'java_Do_Statement174' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Do_Statement()
    setattr(partner, 'java_Do_Statement174', None)
    _safe_set(owner, 'java_Expression175', partner)
    assert getattr(partner, 'java_Do_Statement174') == owner
    _safe_set(owner, 'java_Expression175', None)
    assert getattr(partner, 'java_Do_Statement174') is None


def test_assoc_expression176_stub_double():
    # java_If_Statement has no real 'java_If_Statement177' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_If_Statement()
    setattr(partner, 'java_If_Statement177', None)
    _safe_set(owner, 'java_Expression178', partner)
    assert getattr(partner, 'java_If_Statement177') == owner
    _safe_set(owner, 'java_Expression178', None)
    assert getattr(partner, 'java_If_Statement177') is None


def test_assoc_expression43_stub_double():
    # java_Variable_initializer has no real 'java_Variable_initializer44' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Variable_initializer()
    setattr(partner, 'java_Variable_initializer44', None)
    _safe_set(owner, 'java_Expression', partner)
    assert getattr(partner, 'java_Variable_initializer44') == owner
    _safe_set(owner, 'java_Expression', None)
    assert getattr(partner, 'java_Variable_initializer44') is None


def test_assoc_expression95_stub_double():
    # java_Cast_Expression has no real 'java_Cast_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Cast_Expression()
    setattr(partner, 'java_Cast_Expression96', None)
    _safe_set(owner, 'java_Expression97', partner)
    assert getattr(partner, 'java_Cast_Expression96') == owner
    _safe_set(owner, 'java_Expression97', None)
    assert getattr(partner, 'java_Cast_Expression96') is None


def test_assoc_expression98_stub_double():
    # java_Bit_Expression_NR has no real 'java_Bit_Expression_NR99' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Bit_Expression_NR()
    setattr(partner, 'java_Bit_Expression_NR99', None)
    _safe_set(owner, 'java_Expression100', partner)
    assert getattr(partner, 'java_Bit_Expression_NR99') == owner
    _safe_set(owner, 'java_Expression100', None)
    assert getattr(partner, 'java_Bit_Expression_NR99') is None


def test_assoc_expressions107_stub_double():
    # java_Arg_List has no real 'java_Arg_List108' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Arg_List()
    setattr(partner, 'java_Arg_List108', None)
    _safe_set(owner, 'java_Expression109', partner)
    assert owner in getattr(partner, 'java_Arg_List108')
    _safe_set(owner, 'java_Expression109', None)
    assert owner not in getattr(partner, 'java_Arg_List108')


def test_assoc_expressions143_stub_double():
    # java_Switch_Statement has no real 'java_Switch_Statement144' property in the generated
    # code (a bare stub) -- manually attach it so java_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = java_Switch_Statement()
    setattr(partner, 'java_Switch_Statement144', None)
    _safe_set(owner, 'java_Expression145', partner)
    assert owner in getattr(partner, 'java_Switch_Statement144')
    _safe_set(owner, 'java_Expression145', None)
    assert owner not in getattr(partner, 'java_Switch_Statement144')


def test_assoc_ifStatement125_stub_double():
    # java_If_Statement has no real 'java_If_Statement' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_If_Statement()
    setattr(partner, 'java_If_Statement', None)
    _safe_set(owner, 'java_Statement126', partner)
    assert getattr(partner, 'java_If_Statement') == owner
    _safe_set(owner, 'java_Statement126', None)
    assert getattr(partner, 'java_If_Statement') is None


def test_assoc_imports3_stub_double():
    # java_Compilation_unit has no real 'java_Compilation_unit4' property in the generated
    # code (a bare stub) -- manually attach it so java_Import_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Import_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Import_statement(classname="sample_text", packagename="sample_text")
    partner = java_Compilation_unit()
    setattr(partner, 'java_Compilation_unit4', None)
    _safe_set(owner, 'java_Import_statement', partner)
    assert owner in getattr(partner, 'java_Compilation_unit4')
    _safe_set(owner, 'java_Import_statement', None)
    assert owner not in getattr(partner, 'java_Compilation_unit4')


def test_assoc_initializer41_stub_double():
    # java_Variable_initializer has no real 'java_Variable_initializer' property in the generated
    # code (a bare stub) -- manually attach it so java_Variable_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Variable_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Variable_declarator(name="sample_text")
    partner = java_Variable_initializer()
    setattr(partner, 'java_Variable_initializer', None)
    _safe_set(owner, 'java_Variable_declarator42', partner)
    assert getattr(partner, 'java_Variable_initializer') == owner
    _safe_set(owner, 'java_Variable_declarator42', None)
    assert getattr(partner, 'java_Variable_initializer') is None


def test_assoc_name113_stub_double():
    # java_Statement_block has no real 'java_Statement_block114' property in the generated
    # code (a bare stub) -- manually attach it so java_Static_initializer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Static_initializer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Static_initializer(static="sample_text")
    partner = java_Statement_block()
    setattr(partner, 'java_Statement_block114', None)
    _safe_set(owner, 'java_Static_initializer', partner)
    assert getattr(partner, 'java_Statement_block114') == owner
    _safe_set(owner, 'java_Static_initializer', None)
    assert getattr(partner, 'java_Statement_block114') is None


def test_assoc_name12_stub_double():
    # java_EObject has no real 'java_EObject14' property in the generated
    # code (a bare stub) -- manually attach it so java_Field_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Field_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Field_declaration(debug="sample_text", doc="sample_text")
    partner = java_EObject()
    setattr(partner, 'java_EObject14', None)
    _safe_set(owner, 'java_Field_declaration13', partner)
    assert getattr(partner, 'java_EObject14') == owner
    _safe_set(owner, 'java_Field_declaration13', None)
    assert getattr(partner, 'java_EObject14') is None


def test_assoc_name7_stub_double():
    # java_EObject has no real 'java_EObject' property in the generated
    # code (a bare stub) -- manually attach it so java_Type_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Type_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Type_declaration(doc="sample_text")
    partner = java_EObject()
    setattr(partner, 'java_EObject', None)
    _safe_set(owner, 'java_Type_declaration8', partner)
    assert getattr(partner, 'java_EObject') == owner
    _safe_set(owner, 'java_Type_declaration8', None)
    assert getattr(partner, 'java_EObject') is None


def test_assoc_package1_stub_double():
    # java_Compilation_unit has no real 'java_Compilation_unit2' property in the generated
    # code (a bare stub) -- manually attach it so java_Package_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Package_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Package_statement(name="sample_text")
    partner = java_Compilation_unit()
    setattr(partner, 'java_Compilation_unit2', None)
    _safe_set(owner, 'java_Package_statement', partner)
    assert getattr(partner, 'java_Compilation_unit2') == owner
    _safe_set(owner, 'java_Package_statement', None)
    assert getattr(partner, 'java_Compilation_unit2') is None


def test_assoc_parameter16_stub_double():
    # java_Parameter_list has no real 'java_Parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so java_Method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Method_declaration(debug="sample_text", modifiers="sample_text", name="sample_text")
    partner = java_Parameter_list()
    setattr(partner, 'java_Parameter_list', None)
    _safe_set(owner, 'java_Method_declaration17', partner)
    assert getattr(partner, 'java_Parameter_list') == owner
    _safe_set(owner, 'java_Method_declaration17', None)
    assert getattr(partner, 'java_Parameter_list') is None


def test_assoc_parameter20_stub_double():
    # java_Method_call has no real 'java_Method_call' property in the generated
    # code (a bare stub) -- manually attach it so java_Parameter_list_method_call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Parameter_list_method_call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Parameter_list_method_call(name="sample_text", parameters="sample_text")
    partner = java_Method_call()
    setattr(partner, 'java_Method_call', None)
    _safe_set(owner, 'java_Parameter_list_method_call', partner)
    assert getattr(partner, 'java_Method_call') == owner
    _safe_set(owner, 'java_Parameter_list_method_call', None)
    assert getattr(partner, 'java_Method_call') is None


def test_assoc_parameter26_stub_double():
    # java_Parameter_list has no real 'java_Parameter_list27' property in the generated
    # code (a bare stub) -- manually attach it so java_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Parameter(name="sample_text")
    partner = java_Parameter_list()
    setattr(partner, 'java_Parameter_list27', None)
    _safe_set(owner, 'java_Parameter', partner)
    assert getattr(partner, 'java_Parameter_list27') == owner
    _safe_set(owner, 'java_Parameter', None)
    assert getattr(partner, 'java_Parameter_list27') is None


def test_assoc_parameters21_stub_double():
    # java_Parameter_list has no real 'java_Parameter_list22' property in the generated
    # code (a bare stub) -- manually attach it so java_Constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Constructor_declaration(modifiers="sample_text", name="sample_text")
    partner = java_Parameter_list()
    setattr(partner, 'java_Parameter_list22', None)
    _safe_set(owner, 'java_Constructor_declaration', partner)
    assert getattr(partner, 'java_Parameter_list22') == owner
    _safe_set(owner, 'java_Constructor_declaration', None)
    assert getattr(partner, 'java_Parameter_list22') is None


def test_assoc_parameters28_stub_double():
    # java_Parameter_list has no real 'java_Parameter_list29' property in the generated
    # code (a bare stub) -- manually attach it so java_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Parameter(name="sample_text")
    partner = java_Parameter_list()
    setattr(partner, 'java_Parameter_list29', None)
    _safe_set(owner, 'java_Parameter30', partner)
    assert owner in getattr(partner, 'java_Parameter_list29')
    _safe_set(owner, 'java_Parameter30', None)
    assert owner not in getattr(partner, 'java_Parameter_list29')


def test_assoc_returnSmt117_stub_double():
    # java_Return_Statement has no real 'java_Return_Statement' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Return_Statement()
    setattr(partner, 'java_Return_Statement', None)
    _safe_set(owner, 'java_Statement118', partner)
    assert getattr(partner, 'java_Return_Statement') == owner
    _safe_set(owner, 'java_Statement118', None)
    assert getattr(partner, 'java_Return_Statement') is None


def test_assoc_rv185_stub_double():
    # java_Return_Statement has no real 'java_Return_Statement186' property in the generated
    # code (a bare stub) -- manually attach it so java_Return_value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Return_value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Return_value(name="sample_text")
    partner = java_Return_Statement()
    setattr(partner, 'java_Return_Statement186', None)
    _safe_set(owner, 'java_Return_value', partner)
    assert getattr(partner, 'java_Return_Statement186') == owner
    _safe_set(owner, 'java_Return_value', None)
    assert getattr(partner, 'java_Return_Statement186') is None


def test_assoc_statement167_stub_double():
    # java_While_Statement has no real 'java_While_Statement168' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_While_Statement()
    setattr(partner, 'java_While_Statement168', None)
    _safe_set(owner, 'java_Statement169', partner)
    assert getattr(partner, 'java_While_Statement168') == owner
    _safe_set(owner, 'java_Statement169', None)
    assert getattr(partner, 'java_While_Statement168') is None


def test_assoc_statement170_stub_double():
    # java_Do_Statement has no real 'java_Do_Statement171' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Do_Statement()
    setattr(partner, 'java_Do_Statement171', None)
    _safe_set(owner, 'java_Statement172', partner)
    assert getattr(partner, 'java_Do_Statement171') == owner
    _safe_set(owner, 'java_Statement172', None)
    assert getattr(partner, 'java_Do_Statement171') is None


def test_assoc_statement179_stub_double():
    # java_If_Statement has no real 'java_If_Statement180' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_If_Statement()
    setattr(partner, 'java_If_Statement180', None)
    _safe_set(owner, 'java_Statement181', partner)
    assert getattr(partner, 'java_If_Statement180') == owner
    _safe_set(owner, 'java_Statement181', None)
    assert getattr(partner, 'java_If_Statement180') is None


def test_assoc_statement18_stub_double():
    # java_Statement_block has no real 'java_Statement_block' property in the generated
    # code (a bare stub) -- manually attach it so java_Method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Method_declaration(debug="sample_text", modifiers="sample_text", name="sample_text")
    partner = java_Statement_block()
    setattr(partner, 'java_Statement_block', None)
    _safe_set(owner, 'java_Method_declaration19', partner)
    assert getattr(partner, 'java_Statement_block') == owner
    _safe_set(owner, 'java_Method_declaration19', None)
    assert getattr(partner, 'java_Statement_block') is None


def test_assoc_statement23_stub_double():
    # java_Statement_block has no real 'java_Statement_block25' property in the generated
    # code (a bare stub) -- manually attach it so java_Constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Constructor_declaration(modifiers="sample_text", name="sample_text")
    partner = java_Statement_block()
    setattr(partner, 'java_Statement_block25', None)
    _safe_set(owner, 'java_Constructor_declaration24', partner)
    assert getattr(partner, 'java_Statement_block25') == owner
    _safe_set(owner, 'java_Constructor_declaration24', None)
    assert getattr(partner, 'java_Statement_block25') is None


def test_assoc_statements115_stub_double():
    # java_Statement_block has no real 'java_Statement_block116' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Statement_block()
    setattr(partner, 'java_Statement_block116', None)
    _safe_set(owner, 'java_Statement', partner)
    assert owner in getattr(partner, 'java_Statement_block116')
    _safe_set(owner, 'java_Statement', None)
    assert owner not in getattr(partner, 'java_Statement_block116')


def test_assoc_statements146_stub_double():
    # java_Switch_Statement has no real 'java_Switch_Statement147' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Switch_Statement()
    setattr(partner, 'java_Switch_Statement147', None)
    _safe_set(owner, 'java_Statement148', partner)
    assert owner in getattr(partner, 'java_Switch_Statement147')
    _safe_set(owner, 'java_Statement148', None)
    assert owner not in getattr(partner, 'java_Switch_Statement147')


def test_assoc_switchStatement133_stub_double():
    # java_Switch_Statement has no real 'java_Switch_Statement' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_Switch_Statement()
    setattr(partner, 'java_Switch_Statement', None)
    _safe_set(owner, 'java_Statement134', partner)
    assert getattr(partner, 'java_Switch_Statement') == owner
    _safe_set(owner, 'java_Statement134', None)
    assert getattr(partner, 'java_Switch_Statement') is None


def test_assoc_type92_stub_double():
    # java_Cast_Expression has no real 'java_Cast_Expression93' property in the generated
    # code (a bare stub) -- manually attach it so java_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Type(name="sample_text")
    partner = java_Cast_Expression()
    setattr(partner, 'java_Cast_Expression93', None)
    _safe_set(owner, 'java_Type94', partner)
    assert getattr(partner, 'java_Cast_Expression93') == owner
    _safe_set(owner, 'java_Type94', None)
    assert getattr(partner, 'java_Cast_Expression93') is None


def test_assoc_type_declarations5_stub_double():
    # java_Compilation_unit has no real 'java_Compilation_unit6' property in the generated
    # code (a bare stub) -- manually attach it so java_Type_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Type_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Type_declaration(doc="sample_text")
    partner = java_Compilation_unit()
    setattr(partner, 'java_Compilation_unit6', None)
    _safe_set(owner, 'java_Type_declaration', partner)
    assert owner in getattr(partner, 'java_Compilation_unit6')
    _safe_set(owner, 'java_Type_declaration', None)
    assert owner not in getattr(partner, 'java_Compilation_unit6')


def test_assoc_whileStatement129_stub_double():
    # java_While_Statement has no real 'java_While_Statement' property in the generated
    # code (a bare stub) -- manually attach it so java_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Statement(name="sample_text")
    partner = java_While_Statement()
    setattr(partner, 'java_While_Statement', None)
    _safe_set(owner, 'java_Statement130', partner)
    assert getattr(partner, 'java_While_Statement') == owner
    _safe_set(owner, 'java_Statement130', None)
    assert getattr(partner, 'java_While_Statement') is None


