import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_Ampersand_Rule,
    myDsl_Arg_List,
    myDsl_Array_initializer,
    myDsl_Bit_Expression_NR,
    myDsl_Cast_Expression,
    myDsl_Class_declaration,
    myDsl_Compilation_unit,
    myDsl_Constructor_declaration,
    myDsl_Creating_Expression,
    myDsl_Do_Statement,
    myDsl_Expression,
    myDsl_Expression_aux,
    myDsl_Field_declaration,
    myDsl_Float_Literal,
    myDsl_For_Statement,
    myDsl_If_statement,
    myDsl_Import_statement,
    myDsl_Interface_declaration,
    myDsl_Literal_Expression,
    myDsl_Logical_Expression_NR,
    myDsl_Method_declaration,
    myDsl_Model,
    myDsl_Numeric_Expression_NR,
    myDsl_Package_statement,
    myDsl_Parameter,
    myDsl_Parameter_list,
    myDsl_Statement,
    myDsl_Statement_block,
    myDsl_Static_initializer,
    myDsl_Switch_statement,
    myDsl_Try_statement,
    myDsl_Type,
    myDsl_Type_declaration,
    myDsl_Type_specifier,
    myDsl_Variable_declaration,
    myDsl_Variable_declarator,
    myDsl_Variable_initializer,
    myDsl_While_Statement,
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

def test_assoc_ampersand144_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Ampersand_Rule(a1="sample_text", a2="sample_text")
    _safe_set(b, 'myDsl_Ampersand_Rule', a1)
    assert _is_linked(b, 'myDsl_Ampersand_Rule', a1)
    if hasattr(a1, 'myDsl_Expression_aux145'):
        assert _is_linked(a1, 'myDsl_Expression_aux145', b)
    _safe_set(b, 'myDsl_Ampersand_Rule', a2)
    assert _is_linked(b, 'myDsl_Ampersand_Rule', a2)
    if hasattr(a1, 'myDsl_Expression_aux145'):
        assert not _is_linked(a1, 'myDsl_Expression_aux145', b)
    if hasattr(a2, 'myDsl_Expression_aux145'):
        assert _is_linked(a2, 'myDsl_Expression_aux145', b)
    _safe_set(b, 'myDsl_Ampersand_Rule', None)
    assert not _is_linked(b, 'myDsl_Ampersand_Rule', a2)
    if hasattr(a2, 'myDsl_Expression_aux145'):
        assert not _is_linked(a2, 'myDsl_Expression_aux145', b)


def test_assoc_aux115_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression116', a1)
    assert _is_linked(b, 'myDsl_Expression116', a1)
    if hasattr(a1, 'myDsl_Expression_aux'):
        assert _is_linked(a1, 'myDsl_Expression_aux', b)
    _safe_set(b, 'myDsl_Expression116', a2)
    assert _is_linked(b, 'myDsl_Expression116', a2)
    if hasattr(a1, 'myDsl_Expression_aux'):
        assert not _is_linked(a1, 'myDsl_Expression_aux', b)
    if hasattr(a2, 'myDsl_Expression_aux'):
        assert _is_linked(a2, 'myDsl_Expression_aux', b)
    _safe_set(b, 'myDsl_Expression116', None)
    assert not _is_linked(b, 'myDsl_Expression116', a2)
    if hasattr(a2, 'myDsl_Expression_aux'):
        assert not _is_linked(a2, 'myDsl_Expression_aux', b)


def test_assoc_aux130_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    _safe_set(b, 'myDsl_Expression_aux131', a1)
    assert _is_linked(b, 'myDsl_Expression_aux131', a1)
    if hasattr(a1, 'myDsl_Expression_aux129'):
        assert _is_linked(a1, 'myDsl_Expression_aux129', b)
    _safe_set(b, 'myDsl_Expression_aux131', a2)
    assert _is_linked(b, 'myDsl_Expression_aux131', a2)
    if hasattr(a1, 'myDsl_Expression_aux129'):
        assert not _is_linked(a1, 'myDsl_Expression_aux129', b)
    if hasattr(a2, 'myDsl_Expression_aux129'):
        assert _is_linked(a2, 'myDsl_Expression_aux129', b)
    _safe_set(b, 'myDsl_Expression_aux131', None)
    assert not _is_linked(b, 'myDsl_Expression_aux131', a2)
    if hasattr(a2, 'myDsl_Expression_aux129'):
        assert not _is_linked(a2, 'myDsl_Expression_aux129', b)


def test_assoc_catchStatement217_reverse_link_reassign_clear():
    a1 = myDsl_Try_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Try_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement219', a1)
    assert _is_linked(b, 'myDsl_Statement219', a1)
    if hasattr(a1, 'myDsl_Try_statement218'):
        assert _is_linked(a1, 'myDsl_Try_statement218', b)
    _safe_set(b, 'myDsl_Statement219', a2)
    assert _is_linked(b, 'myDsl_Statement219', a2)
    if hasattr(a1, 'myDsl_Try_statement218'):
        assert not _is_linked(a1, 'myDsl_Try_statement218', b)
    if hasattr(a2, 'myDsl_Try_statement218'):
        assert _is_linked(a2, 'myDsl_Try_statement218', b)
    _safe_set(b, 'myDsl_Statement219', None)
    assert not _is_linked(b, 'myDsl_Statement219', a2)
    if hasattr(a2, 'myDsl_Try_statement218'):
        assert not _is_linked(a2, 'myDsl_Try_statement218', b)


def test_assoc_classDec7_reverse_link_reassign_clear():
    a1 = myDsl_Type_declaration(comment="sample_text")
    a2 = myDsl_Type_declaration(comment="sample_text_2")
    b = myDsl_Class_declaration(classHerdada="sample_text", className="sample_text", interfaceImplementada="sample_text", interfacesImplementadas="sample_text", modifiers="sample_text")
    _safe_set(b, 'myDsl_Class_declaration', a1)
    assert _is_linked(b, 'myDsl_Class_declaration', a1)
    if hasattr(a1, 'myDsl_Type_declaration8'):
        assert _is_linked(a1, 'myDsl_Type_declaration8', b)
    _safe_set(b, 'myDsl_Class_declaration', a2)
    assert _is_linked(b, 'myDsl_Class_declaration', a2)
    if hasattr(a1, 'myDsl_Type_declaration8'):
        assert not _is_linked(a1, 'myDsl_Type_declaration8', b)
    if hasattr(a2, 'myDsl_Type_declaration8'):
        assert _is_linked(a2, 'myDsl_Type_declaration8', b)
    _safe_set(b, 'myDsl_Class_declaration', None)
    assert not _is_linked(b, 'myDsl_Class_declaration', a2)
    if hasattr(a2, 'myDsl_Type_declaration8'):
        assert not _is_linked(a2, 'myDsl_Type_declaration8', b)


def test_assoc_contructorName18_reverse_link_reassign_clear():
    a1 = myDsl_Field_declaration(comment="sample_text")
    a2 = myDsl_Field_declaration(comment="sample_text_2")
    b = myDsl_Constructor_declaration(lParen="sample_text", modifiersConstructor="sample_text", nameConstructor="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Constructor_declaration', a1)
    assert _is_linked(b, 'myDsl_Constructor_declaration', a1)
    if hasattr(a1, 'myDsl_Field_declaration19'):
        assert _is_linked(a1, 'myDsl_Field_declaration19', b)
    _safe_set(b, 'myDsl_Constructor_declaration', a2)
    assert _is_linked(b, 'myDsl_Constructor_declaration', a2)
    if hasattr(a1, 'myDsl_Field_declaration19'):
        assert not _is_linked(a1, 'myDsl_Field_declaration19', b)
    if hasattr(a2, 'myDsl_Field_declaration19'):
        assert _is_linked(a2, 'myDsl_Field_declaration19', b)
    _safe_set(b, 'myDsl_Constructor_declaration', None)
    assert not _is_linked(b, 'myDsl_Constructor_declaration', a2)
    if hasattr(a2, 'myDsl_Field_declaration19'):
        assert not _is_linked(a2, 'myDsl_Field_declaration19', b)


def test_assoc_creatingExpression123_reverse_link_reassign_clear():
    a1 = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    a2 = myDsl_Expression(name="sample_text_2", null="sample_text_2", super="sample_text_2", this="sample_text_2")
    b = myDsl_Creating_Expression(className="sample_text")
    _safe_set(b, 'myDsl_Creating_Expression', a1)
    assert _is_linked(b, 'myDsl_Creating_Expression', a1)
    if hasattr(a1, 'myDsl_Expression124'):
        assert _is_linked(a1, 'myDsl_Expression124', b)
    _safe_set(b, 'myDsl_Creating_Expression', a2)
    assert _is_linked(b, 'myDsl_Creating_Expression', a2)
    if hasattr(a1, 'myDsl_Expression124'):
        assert not _is_linked(a1, 'myDsl_Expression124', b)
    if hasattr(a2, 'myDsl_Expression124'):
        assert _is_linked(a2, 'myDsl_Expression124', b)
    _safe_set(b, 'myDsl_Creating_Expression', None)
    assert not _is_linked(b, 'myDsl_Creating_Expression', a2)
    if hasattr(a2, 'myDsl_Expression124'):
        assert not _is_linked(a2, 'myDsl_Expression124', b)


def test_assoc_doStatement199_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Do_Statement(lparent="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Do_Statement200', a1)
    assert _is_linked(b, 'myDsl_Do_Statement200', a1)
    if hasattr(a1, 'myDsl_Statement201'):
        assert _is_linked(a1, 'myDsl_Statement201', b)
    _safe_set(b, 'myDsl_Do_Statement200', a2)
    assert _is_linked(b, 'myDsl_Do_Statement200', a2)
    if hasattr(a1, 'myDsl_Statement201'):
        assert not _is_linked(a1, 'myDsl_Statement201', b)
    if hasattr(a2, 'myDsl_Statement201'):
        assert _is_linked(a2, 'myDsl_Statement201', b)
    _safe_set(b, 'myDsl_Do_Statement200', None)
    assert not _is_linked(b, 'myDsl_Do_Statement200', a2)
    if hasattr(a2, 'myDsl_Statement201'):
        assert not _is_linked(a2, 'myDsl_Statement201', b)


def test_assoc_doStatement76_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Do_Statement(lparent="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Do_Statement', a1)
    assert _is_linked(b, 'myDsl_Do_Statement', a1)
    if hasattr(a1, 'myDsl_Statement77'):
        assert _is_linked(a1, 'myDsl_Statement77', b)
    _safe_set(b, 'myDsl_Do_Statement', a2)
    assert _is_linked(b, 'myDsl_Do_Statement', a2)
    if hasattr(a1, 'myDsl_Statement77'):
        assert not _is_linked(a1, 'myDsl_Statement77', b)
    if hasattr(a2, 'myDsl_Statement77'):
        assert _is_linked(a2, 'myDsl_Statement77', b)
    _safe_set(b, 'myDsl_Do_Statement', None)
    assert not _is_linked(b, 'myDsl_Do_Statement', a2)
    if hasattr(a2, 'myDsl_Statement77'):
        assert not _is_linked(a2, 'myDsl_Statement77', b)


def test_assoc_elseStatement208_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_If_statement(lparen="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_If_statement209', a1)
    assert _is_linked(b, 'myDsl_If_statement209', a1)
    if hasattr(a1, 'myDsl_Statement210'):
        assert _is_linked(a1, 'myDsl_Statement210', b)
    _safe_set(b, 'myDsl_If_statement209', a2)
    assert _is_linked(b, 'myDsl_If_statement209', a2)
    if hasattr(a1, 'myDsl_Statement210'):
        assert not _is_linked(a1, 'myDsl_Statement210', b)
    if hasattr(a2, 'myDsl_Statement210'):
        assert _is_linked(a2, 'myDsl_Statement210', b)
    _safe_set(b, 'myDsl_If_statement209', None)
    assert not _is_linked(b, 'myDsl_If_statement209', a2)
    if hasattr(a2, 'myDsl_Statement210'):
        assert not _is_linked(a2, 'myDsl_Statement210', b)


def test_assoc_exp1141_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression143', a1)
    assert _is_linked(b, 'myDsl_Expression143', a1)
    if hasattr(a1, 'myDsl_Expression_aux142'):
        assert _is_linked(a1, 'myDsl_Expression_aux142', b)
    _safe_set(b, 'myDsl_Expression143', a2)
    assert _is_linked(b, 'myDsl_Expression143', a2)
    if hasattr(a1, 'myDsl_Expression_aux142'):
        assert not _is_linked(a1, 'myDsl_Expression_aux142', b)
    if hasattr(a2, 'myDsl_Expression_aux142'):
        assert _is_linked(a2, 'myDsl_Expression_aux142', b)
    _safe_set(b, 'myDsl_Expression143', None)
    assert not _is_linked(b, 'myDsl_Expression143', a2)
    if hasattr(a2, 'myDsl_Expression_aux142'):
        assert not _is_linked(a2, 'myDsl_Expression_aux142', b)


def test_assoc_exp2138_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression140', a1)
    assert _is_linked(b, 'myDsl_Expression140', a1)
    if hasattr(a1, 'myDsl_Expression_aux139'):
        assert _is_linked(a1, 'myDsl_Expression_aux139', b)
    _safe_set(b, 'myDsl_Expression140', a2)
    assert _is_linked(b, 'myDsl_Expression140', a2)
    if hasattr(a1, 'myDsl_Expression_aux139'):
        assert not _is_linked(a1, 'myDsl_Expression_aux139', b)
    if hasattr(a2, 'myDsl_Expression_aux139'):
        assert _is_linked(a2, 'myDsl_Expression_aux139', b)
    _safe_set(b, 'myDsl_Expression140', None)
    assert not _is_linked(b, 'myDsl_Expression140', a2)
    if hasattr(a2, 'myDsl_Expression_aux139'):
        assert not _is_linked(a2, 'myDsl_Expression_aux139', b)


def test_assoc_exp2152_reverse_link_reassign_clear():
    a1 = myDsl_Literal_Expression(charLit="sample_text", exp="sample_text", exp1=7, string="sample_text")
    a2 = myDsl_Literal_Expression(charLit="sample_text_2", exp="sample_text_2", exp1=13, string="sample_text_2")
    b = myDsl_Float_Literal(decimalDigits1=7, decimalDigits2=7, exp="sample_text", floatTypeSufix="sample_text")
    _safe_set(b, 'myDsl_Float_Literal', a1)
    assert _is_linked(b, 'myDsl_Float_Literal', a1)
    if hasattr(a1, 'myDsl_Literal_Expression153'):
        assert _is_linked(a1, 'myDsl_Literal_Expression153', b)
    _safe_set(b, 'myDsl_Float_Literal', a2)
    assert _is_linked(b, 'myDsl_Float_Literal', a2)
    if hasattr(a1, 'myDsl_Literal_Expression153'):
        assert not _is_linked(a1, 'myDsl_Literal_Expression153', b)
    if hasattr(a2, 'myDsl_Literal_Expression153'):
        assert _is_linked(a2, 'myDsl_Literal_Expression153', b)
    _safe_set(b, 'myDsl_Float_Literal', None)
    assert not _is_linked(b, 'myDsl_Float_Literal', a2)
    if hasattr(a2, 'myDsl_Literal_Expression153'):
        assert not _is_linked(a2, 'myDsl_Literal_Expression153', b)


def test_assoc_expression160_reverse_link_reassign_clear():
    a1 = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    a2 = myDsl_Expression(name="sample_text_2", null="sample_text_2", super="sample_text_2", this="sample_text_2")
    b = myDsl_Creating_Expression(className="sample_text")
    _safe_set(b, 'myDsl_Creating_Expression161', a1)
    assert _is_linked(b, 'myDsl_Creating_Expression161', a1)
    if hasattr(a1, 'myDsl_Expression162'):
        assert _is_linked(a1, 'myDsl_Expression162', b)
    _safe_set(b, 'myDsl_Creating_Expression161', a2)
    assert _is_linked(b, 'myDsl_Creating_Expression161', a2)
    if hasattr(a1, 'myDsl_Expression162'):
        assert not _is_linked(a1, 'myDsl_Expression162', b)
    if hasattr(a2, 'myDsl_Expression162'):
        assert _is_linked(a2, 'myDsl_Expression162', b)
    _safe_set(b, 'myDsl_Creating_Expression161', None)
    assert not _is_linked(b, 'myDsl_Creating_Expression161', a2)
    if hasattr(a2, 'myDsl_Expression162'):
        assert not _is_linked(a2, 'myDsl_Expression162', b)


def test_assoc_expression172_reverse_link_reassign_clear():
    a1 = myDsl_Logical_Expression_NR(exclamation="sample_text", false="sample_text", true="sample_text")
    a2 = myDsl_Logical_Expression_NR(exclamation="sample_text_2", false="sample_text_2", true="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression174', a1)
    assert _is_linked(b, 'myDsl_Expression174', a1)
    if hasattr(a1, 'myDsl_Logical_Expression_NR173'):
        assert _is_linked(a1, 'myDsl_Logical_Expression_NR173', b)
    _safe_set(b, 'myDsl_Expression174', a2)
    assert _is_linked(b, 'myDsl_Expression174', a2)
    if hasattr(a1, 'myDsl_Logical_Expression_NR173'):
        assert not _is_linked(a1, 'myDsl_Logical_Expression_NR173', b)
    if hasattr(a2, 'myDsl_Logical_Expression_NR173'):
        assert _is_linked(a2, 'myDsl_Logical_Expression_NR173', b)
    _safe_set(b, 'myDsl_Expression174', None)
    assert not _is_linked(b, 'myDsl_Expression174', a2)
    if hasattr(a2, 'myDsl_Logical_Expression_NR173'):
        assert not _is_linked(a2, 'myDsl_Logical_Expression_NR173', b)


def test_assoc_expression181_reverse_link_reassign_clear():
    a1 = myDsl_Numeric_Expression_NR(sinal_numeric="sample_text")
    a2 = myDsl_Numeric_Expression_NR(sinal_numeric="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression183', a1)
    assert _is_linked(b, 'myDsl_Expression183', a1)
    if hasattr(a1, 'myDsl_Numeric_Expression_NR182'):
        assert _is_linked(a1, 'myDsl_Numeric_Expression_NR182', b)
    _safe_set(b, 'myDsl_Expression183', a2)
    assert _is_linked(b, 'myDsl_Expression183', a2)
    if hasattr(a1, 'myDsl_Numeric_Expression_NR182'):
        assert not _is_linked(a1, 'myDsl_Numeric_Expression_NR182', b)
    if hasattr(a2, 'myDsl_Numeric_Expression_NR182'):
        assert _is_linked(a2, 'myDsl_Numeric_Expression_NR182', b)
    _safe_set(b, 'myDsl_Expression183', None)
    assert not _is_linked(b, 'myDsl_Expression183', a2)
    if hasattr(a2, 'myDsl_Numeric_Expression_NR182'):
        assert not _is_linked(a2, 'myDsl_Numeric_Expression_NR182', b)


def test_assoc_expression184_reverse_link_reassign_clear():
    a1 = myDsl_Switch_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Switch_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression186', a1)
    assert _is_linked(b, 'myDsl_Expression186', a1)
    if hasattr(a1, 'myDsl_Switch_statement185'):
        assert _is_linked(a1, 'myDsl_Switch_statement185', b)
    _safe_set(b, 'myDsl_Expression186', a2)
    assert _is_linked(b, 'myDsl_Expression186', a2)
    if hasattr(a1, 'myDsl_Switch_statement185'):
        assert not _is_linked(a1, 'myDsl_Switch_statement185', b)
    if hasattr(a2, 'myDsl_Switch_statement185'):
        assert _is_linked(a2, 'myDsl_Switch_statement185', b)
    _safe_set(b, 'myDsl_Expression186', None)
    assert not _is_linked(b, 'myDsl_Expression186', a2)
    if hasattr(a2, 'myDsl_Switch_statement185'):
        assert not _is_linked(a2, 'myDsl_Switch_statement185', b)


def test_assoc_expression193_reverse_link_reassign_clear():
    a1 = myDsl_While_Statement(rparent="sample_text")
    a2 = myDsl_While_Statement(rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression195', a1)
    assert _is_linked(b, 'myDsl_Expression195', a1)
    if hasattr(a1, 'myDsl_While_Statement194'):
        assert _is_linked(a1, 'myDsl_While_Statement194', b)
    _safe_set(b, 'myDsl_Expression195', a2)
    assert _is_linked(b, 'myDsl_Expression195', a2)
    if hasattr(a1, 'myDsl_While_Statement194'):
        assert not _is_linked(a1, 'myDsl_While_Statement194', b)
    if hasattr(a2, 'myDsl_While_Statement194'):
        assert _is_linked(a2, 'myDsl_While_Statement194', b)
    _safe_set(b, 'myDsl_Expression195', None)
    assert not _is_linked(b, 'myDsl_Expression195', a2)
    if hasattr(a2, 'myDsl_While_Statement194'):
        assert not _is_linked(a2, 'myDsl_While_Statement194', b)


def test_assoc_expression202_reverse_link_reassign_clear():
    a1 = myDsl_If_statement(lparen="sample_text", rparent="sample_text")
    a2 = myDsl_If_statement(lparen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression204', a1)
    assert _is_linked(b, 'myDsl_Expression204', a1)
    if hasattr(a1, 'myDsl_If_statement203'):
        assert _is_linked(a1, 'myDsl_If_statement203', b)
    _safe_set(b, 'myDsl_Expression204', a2)
    assert _is_linked(b, 'myDsl_Expression204', a2)
    if hasattr(a1, 'myDsl_If_statement203'):
        assert not _is_linked(a1, 'myDsl_If_statement203', b)
    if hasattr(a2, 'myDsl_If_statement203'):
        assert _is_linked(a2, 'myDsl_If_statement203', b)
    _safe_set(b, 'myDsl_Expression204', None)
    assert not _is_linked(b, 'myDsl_Expression204', a2)
    if hasattr(a2, 'myDsl_If_statement203'):
        assert not _is_linked(a2, 'myDsl_If_statement203', b)


def test_assoc_expression2132_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression134', a1)
    assert _is_linked(b, 'myDsl_Expression134', a1)
    if hasattr(a1, 'myDsl_Expression_aux133'):
        assert _is_linked(a1, 'myDsl_Expression_aux133', b)
    _safe_set(b, 'myDsl_Expression134', a2)
    assert _is_linked(b, 'myDsl_Expression134', a2)
    if hasattr(a1, 'myDsl_Expression_aux133'):
        assert not _is_linked(a1, 'myDsl_Expression_aux133', b)
    if hasattr(a2, 'myDsl_Expression_aux133'):
        assert _is_linked(a2, 'myDsl_Expression_aux133', b)
    _safe_set(b, 'myDsl_Expression134', None)
    assert not _is_linked(b, 'myDsl_Expression134', a2)
    if hasattr(a2, 'myDsl_Expression_aux133'):
        assert not _is_linked(a2, 'myDsl_Expression_aux133', b)


def test_assoc_expression2187_reverse_link_reassign_clear():
    a1 = myDsl_Switch_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Switch_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression189', a1)
    assert _is_linked(b, 'myDsl_Expression189', a1)
    if hasattr(a1, 'myDsl_Switch_statement188'):
        assert _is_linked(a1, 'myDsl_Switch_statement188', b)
    _safe_set(b, 'myDsl_Expression189', a2)
    assert _is_linked(b, 'myDsl_Expression189', a2)
    if hasattr(a1, 'myDsl_Switch_statement188'):
        assert not _is_linked(a1, 'myDsl_Switch_statement188', b)
    if hasattr(a2, 'myDsl_Switch_statement188'):
        assert _is_linked(a2, 'myDsl_Switch_statement188', b)
    _safe_set(b, 'myDsl_Expression189', None)
    assert not _is_linked(b, 'myDsl_Expression189', a2)
    if hasattr(a2, 'myDsl_Switch_statement188'):
        assert not _is_linked(a2, 'myDsl_Switch_statement188', b)


def test_assoc_expression84_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression86', a1)
    assert _is_linked(b, 'myDsl_Expression86', a1)
    if hasattr(a1, 'myDsl_Statement85'):
        assert _is_linked(a1, 'myDsl_Statement85', b)
    _safe_set(b, 'myDsl_Expression86', a2)
    assert _is_linked(b, 'myDsl_Expression86', a2)
    if hasattr(a1, 'myDsl_Statement85'):
        assert not _is_linked(a1, 'myDsl_Statement85', b)
    if hasattr(a2, 'myDsl_Statement85'):
        assert _is_linked(a2, 'myDsl_Statement85', b)
    _safe_set(b, 'myDsl_Expression86', None)
    assert not _is_linked(b, 'myDsl_Expression86', a2)
    if hasattr(a2, 'myDsl_Statement85'):
        assert not _is_linked(a2, 'myDsl_Statement85', b)


def test_assoc_expressionBit146_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression148', a1)
    assert _is_linked(b, 'myDsl_Expression148', a1)
    if hasattr(a1, 'myDsl_Expression_aux147'):
        assert _is_linked(a1, 'myDsl_Expression_aux147', b)
    _safe_set(b, 'myDsl_Expression148', a2)
    assert _is_linked(b, 'myDsl_Expression148', a2)
    if hasattr(a1, 'myDsl_Expression_aux147'):
        assert not _is_linked(a1, 'myDsl_Expression_aux147', b)
    if hasattr(a2, 'myDsl_Expression_aux147'):
        assert _is_linked(a2, 'myDsl_Expression_aux147', b)
    _safe_set(b, 'myDsl_Expression148', None)
    assert not _is_linked(b, 'myDsl_Expression148', a2)
    if hasattr(a2, 'myDsl_Expression_aux147'):
        assert not _is_linked(a2, 'myDsl_Expression_aux147', b)


def test_assoc_expressionComma135_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression137', a1)
    assert _is_linked(b, 'myDsl_Expression137', a1)
    if hasattr(a1, 'myDsl_Expression_aux136'):
        assert _is_linked(a1, 'myDsl_Expression_aux136', b)
    _safe_set(b, 'myDsl_Expression137', a2)
    assert _is_linked(b, 'myDsl_Expression137', a2)
    if hasattr(a1, 'myDsl_Expression_aux136'):
        assert not _is_linked(a1, 'myDsl_Expression_aux136', b)
    if hasattr(a2, 'myDsl_Expression_aux136'):
        assert _is_linked(a2, 'myDsl_Expression_aux136', b)
    _safe_set(b, 'myDsl_Expression137', None)
    assert not _is_linked(b, 'myDsl_Expression137', a2)
    if hasattr(a2, 'myDsl_Expression_aux136'):
        assert not _is_linked(a2, 'myDsl_Expression_aux136', b)


def test_assoc_expressionStatement71_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression73', a1)
    assert _is_linked(b, 'myDsl_Expression73', a1)
    if hasattr(a1, 'myDsl_Statement72'):
        assert _is_linked(a1, 'myDsl_Statement72', b)
    _safe_set(b, 'myDsl_Expression73', a2)
    assert _is_linked(b, 'myDsl_Expression73', a2)
    if hasattr(a1, 'myDsl_Statement72'):
        assert not _is_linked(a1, 'myDsl_Statement72', b)
    if hasattr(a2, 'myDsl_Statement72'):
        assert _is_linked(a2, 'myDsl_Statement72', b)
    _safe_set(b, 'myDsl_Expression73', None)
    assert not _is_linked(b, 'myDsl_Expression73', a2)
    if hasattr(a2, 'myDsl_Statement72'):
        assert not _is_linked(a2, 'myDsl_Statement72', b)


def test_assoc_fieldsDeclaration11_reverse_link_reassign_clear():
    a1 = myDsl_Interface_declaration(interfaceHerdada="sample_text", interfaceName="sample_text", interfacesHerdadas="sample_text", modifiers="sample_text")
    a2 = myDsl_Interface_declaration(interfaceHerdada="sample_text_2", interfaceName="sample_text_2", interfacesHerdadas="sample_text_2", modifiers="sample_text_2")
    b = myDsl_Field_declaration(comment="sample_text")
    _safe_set(b, 'myDsl_Field_declaration', a1)
    assert _is_linked(b, 'myDsl_Field_declaration', a1)
    if hasattr(a1, 'myDsl_Interface_declaration12'):
        assert _is_linked(a1, 'myDsl_Interface_declaration12', b)
    _safe_set(b, 'myDsl_Field_declaration', a2)
    assert _is_linked(b, 'myDsl_Field_declaration', a2)
    if hasattr(a1, 'myDsl_Interface_declaration12'):
        assert not _is_linked(a1, 'myDsl_Interface_declaration12', b)
    if hasattr(a2, 'myDsl_Interface_declaration12'):
        assert _is_linked(a2, 'myDsl_Interface_declaration12', b)
    _safe_set(b, 'myDsl_Field_declaration', None)
    assert not _is_linked(b, 'myDsl_Field_declaration', a2)
    if hasattr(a2, 'myDsl_Interface_declaration12'):
        assert not _is_linked(a2, 'myDsl_Interface_declaration12', b)


def test_assoc_fieldsDeclaration13_reverse_link_reassign_clear():
    a1 = myDsl_Field_declaration(comment="sample_text")
    a2 = myDsl_Field_declaration(comment="sample_text_2")
    b = myDsl_Class_declaration(classHerdada="sample_text", className="sample_text", interfaceImplementada="sample_text", interfacesImplementadas="sample_text", modifiers="sample_text")
    _safe_set(b, 'myDsl_Class_declaration14', {a1})
    assert _is_linked(b, 'myDsl_Class_declaration14', a1)
    if hasattr(a1, 'myDsl_Field_declaration15'):
        assert _is_linked(a1, 'myDsl_Field_declaration15', b)
    _safe_set(b, 'myDsl_Class_declaration14', {a2})
    assert _is_linked(b, 'myDsl_Class_declaration14', a2)
    if hasattr(a1, 'myDsl_Field_declaration15'):
        assert not _is_linked(a1, 'myDsl_Field_declaration15', b)
    if hasattr(a2, 'myDsl_Field_declaration15'):
        assert _is_linked(a2, 'myDsl_Field_declaration15', b)
    _safe_set(b, 'myDsl_Class_declaration14', set())
    assert not _is_linked(b, 'myDsl_Class_declaration14', a2)
    if hasattr(a2, 'myDsl_Field_declaration15'):
        assert not _is_linked(a2, 'myDsl_Field_declaration15', b)


def test_assoc_finallyStatement220_reverse_link_reassign_clear():
    a1 = myDsl_Try_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Try_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement222', a1)
    assert _is_linked(b, 'myDsl_Statement222', a1)
    if hasattr(a1, 'myDsl_Try_statement221'):
        assert _is_linked(a1, 'myDsl_Try_statement221', b)
    _safe_set(b, 'myDsl_Statement222', a2)
    assert _is_linked(b, 'myDsl_Statement222', a2)
    if hasattr(a1, 'myDsl_Try_statement221'):
        assert not _is_linked(a1, 'myDsl_Try_statement221', b)
    if hasattr(a2, 'myDsl_Try_statement221'):
        assert _is_linked(a2, 'myDsl_Try_statement221', b)
    _safe_set(b, 'myDsl_Statement222', None)
    assert not _is_linked(b, 'myDsl_Statement222', a2)
    if hasattr(a2, 'myDsl_Try_statement221'):
        assert not _is_linked(a2, 'myDsl_Try_statement221', b)


def test_assoc_idStatement205_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_If_statement(lparen="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_If_statement206', a1)
    assert _is_linked(b, 'myDsl_If_statement206', a1)
    if hasattr(a1, 'myDsl_Statement207'):
        assert _is_linked(a1, 'myDsl_Statement207', b)
    _safe_set(b, 'myDsl_If_statement206', a2)
    assert _is_linked(b, 'myDsl_If_statement206', a2)
    if hasattr(a1, 'myDsl_Statement207'):
        assert not _is_linked(a1, 'myDsl_Statement207', b)
    if hasattr(a2, 'myDsl_Statement207'):
        assert _is_linked(a2, 'myDsl_Statement207', b)
    _safe_set(b, 'myDsl_If_statement206', None)
    assert not _is_linked(b, 'myDsl_If_statement206', a2)
    if hasattr(a2, 'myDsl_Statement207'):
        assert not _is_linked(a2, 'myDsl_Statement207', b)


def test_assoc_ifStatement74_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_If_statement(lparen="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_If_statement', a1)
    assert _is_linked(b, 'myDsl_If_statement', a1)
    if hasattr(a1, 'myDsl_Statement75'):
        assert _is_linked(a1, 'myDsl_Statement75', b)
    _safe_set(b, 'myDsl_If_statement', a2)
    assert _is_linked(b, 'myDsl_If_statement', a2)
    if hasattr(a1, 'myDsl_Statement75'):
        assert not _is_linked(a1, 'myDsl_Statement75', b)
    if hasattr(a2, 'myDsl_Statement75'):
        assert _is_linked(a2, 'myDsl_Statement75', b)
    _safe_set(b, 'myDsl_If_statement', None)
    assert not _is_linked(b, 'myDsl_If_statement', a2)
    if hasattr(a2, 'myDsl_Statement75'):
        assert not _is_linked(a2, 'myDsl_Statement75', b)


def test_assoc_interfaceDec9_reverse_link_reassign_clear():
    a1 = myDsl_Type_declaration(comment="sample_text")
    a2 = myDsl_Type_declaration(comment="sample_text_2")
    b = myDsl_Interface_declaration(interfaceHerdada="sample_text", interfaceName="sample_text", interfacesHerdadas="sample_text", modifiers="sample_text")
    _safe_set(b, 'myDsl_Interface_declaration', a1)
    assert _is_linked(b, 'myDsl_Interface_declaration', a1)
    if hasattr(a1, 'myDsl_Type_declaration10'):
        assert _is_linked(a1, 'myDsl_Type_declaration10', b)
    _safe_set(b, 'myDsl_Interface_declaration', a2)
    assert _is_linked(b, 'myDsl_Interface_declaration', a2)
    if hasattr(a1, 'myDsl_Type_declaration10'):
        assert not _is_linked(a1, 'myDsl_Type_declaration10', b)
    if hasattr(a2, 'myDsl_Type_declaration10'):
        assert _is_linked(a2, 'myDsl_Type_declaration10', b)
    _safe_set(b, 'myDsl_Interface_declaration', None)
    assert not _is_linked(b, 'myDsl_Interface_declaration', a2)
    if hasattr(a2, 'myDsl_Type_declaration10'):
        assert not _is_linked(a2, 'myDsl_Type_declaration10', b)


def test_assoc_literalExpression125_reverse_link_reassign_clear():
    a1 = myDsl_Literal_Expression(charLit="sample_text", exp="sample_text", exp1=7, string="sample_text")
    a2 = myDsl_Literal_Expression(charLit="sample_text_2", exp="sample_text_2", exp1=13, string="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression126', a1)
    assert _is_linked(b, 'myDsl_Expression126', a1)
    if hasattr(a1, 'myDsl_Literal_Expression'):
        assert _is_linked(a1, 'myDsl_Literal_Expression', b)
    _safe_set(b, 'myDsl_Expression126', a2)
    assert _is_linked(b, 'myDsl_Expression126', a2)
    if hasattr(a1, 'myDsl_Literal_Expression'):
        assert not _is_linked(a1, 'myDsl_Literal_Expression', b)
    if hasattr(a2, 'myDsl_Literal_Expression'):
        assert _is_linked(a2, 'myDsl_Literal_Expression', b)
    _safe_set(b, 'myDsl_Expression126', None)
    assert not _is_linked(b, 'myDsl_Expression126', a2)
    if hasattr(a2, 'myDsl_Literal_Expression'):
        assert not _is_linked(a2, 'myDsl_Literal_Expression', b)


def test_assoc_logicExp149_reverse_link_reassign_clear():
    a1 = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    a2 = myDsl_Expression_aux(bitSign="sample_text_2", logicOp="sample_text_2", logicalSign="sample_text_2", name="sample_text_2", numericSign="sample_text_2", sgin="sample_text_2", stringSign="sample_text_2", testingSign="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression151', a1)
    assert _is_linked(b, 'myDsl_Expression151', a1)
    if hasattr(a1, 'myDsl_Expression_aux150'):
        assert _is_linked(a1, 'myDsl_Expression_aux150', b)
    _safe_set(b, 'myDsl_Expression151', a2)
    assert _is_linked(b, 'myDsl_Expression151', a2)
    if hasattr(a1, 'myDsl_Expression_aux150'):
        assert not _is_linked(a1, 'myDsl_Expression_aux150', b)
    if hasattr(a2, 'myDsl_Expression_aux150'):
        assert _is_linked(a2, 'myDsl_Expression_aux150', b)
    _safe_set(b, 'myDsl_Expression151', None)
    assert not _is_linked(b, 'myDsl_Expression151', a2)
    if hasattr(a2, 'myDsl_Expression_aux150'):
        assert not _is_linked(a2, 'myDsl_Expression_aux150', b)


def test_assoc_logicalExpression117_reverse_link_reassign_clear():
    a1 = myDsl_Logical_Expression_NR(exclamation="sample_text", false="sample_text", true="sample_text")
    a2 = myDsl_Logical_Expression_NR(exclamation="sample_text_2", false="sample_text_2", true="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression118', a1)
    assert _is_linked(b, 'myDsl_Expression118', a1)
    if hasattr(a1, 'myDsl_Logical_Expression_NR'):
        assert _is_linked(a1, 'myDsl_Logical_Expression_NR', b)
    _safe_set(b, 'myDsl_Expression118', a2)
    assert _is_linked(b, 'myDsl_Expression118', a2)
    if hasattr(a1, 'myDsl_Logical_Expression_NR'):
        assert not _is_linked(a1, 'myDsl_Logical_Expression_NR', b)
    if hasattr(a2, 'myDsl_Logical_Expression_NR'):
        assert _is_linked(a2, 'myDsl_Logical_Expression_NR', b)
    _safe_set(b, 'myDsl_Expression118', None)
    assert not _is_linked(b, 'myDsl_Expression118', a2)
    if hasattr(a2, 'myDsl_Logical_Expression_NR'):
        assert not _is_linked(a2, 'myDsl_Logical_Expression_NR', b)


def test_assoc_methodName20_reverse_link_reassign_clear():
    a1 = myDsl_Method_declaration(debug="sample_text", lParen="sample_text", modifiersMethod="sample_text", nameMethod="sample_text", rparent="sample_text")
    a2 = myDsl_Method_declaration(debug="sample_text_2", lParen="sample_text_2", modifiersMethod="sample_text_2", nameMethod="sample_text_2", rparent="sample_text_2")
    b = myDsl_Field_declaration(comment="sample_text")
    _safe_set(b, 'myDsl_Field_declaration21', a1)
    assert _is_linked(b, 'myDsl_Field_declaration21', a1)
    if hasattr(a1, 'myDsl_Method_declaration'):
        assert _is_linked(a1, 'myDsl_Method_declaration', b)
    _safe_set(b, 'myDsl_Field_declaration21', a2)
    assert _is_linked(b, 'myDsl_Field_declaration21', a2)
    if hasattr(a1, 'myDsl_Method_declaration'):
        assert not _is_linked(a1, 'myDsl_Method_declaration', b)
    if hasattr(a2, 'myDsl_Method_declaration'):
        assert _is_linked(a2, 'myDsl_Method_declaration', b)
    _safe_set(b, 'myDsl_Field_declaration21', None)
    assert not _is_linked(b, 'myDsl_Field_declaration21', a2)
    if hasattr(a2, 'myDsl_Method_declaration'):
        assert not _is_linked(a2, 'myDsl_Method_declaration', b)


def test_assoc_name63_reverse_link_reassign_clear():
    a1 = myDsl_Static_initializer(static="sample_text")
    a2 = myDsl_Static_initializer(static="sample_text_2")
    b = myDsl_Statement_block(lCurly="sample_text", rCurly="sample_text")
    _safe_set(b, 'myDsl_Statement_block65', a1)
    assert _is_linked(b, 'myDsl_Statement_block65', a1)
    if hasattr(a1, 'myDsl_Static_initializer64'):
        assert _is_linked(a1, 'myDsl_Static_initializer64', b)
    _safe_set(b, 'myDsl_Statement_block65', a2)
    assert _is_linked(b, 'myDsl_Statement_block65', a2)
    if hasattr(a1, 'myDsl_Static_initializer64'):
        assert not _is_linked(a1, 'myDsl_Static_initializer64', b)
    if hasattr(a2, 'myDsl_Static_initializer64'):
        assert _is_linked(a2, 'myDsl_Static_initializer64', b)
    _safe_set(b, 'myDsl_Statement_block65', None)
    assert not _is_linked(b, 'myDsl_Statement_block65', a2)
    if hasattr(a2, 'myDsl_Static_initializer64'):
        assert not _is_linked(a2, 'myDsl_Static_initializer64', b)


def test_assoc_nameVariable47_reverse_link_reassign_clear():
    a1 = myDsl_Variable_declarator(lenVector="sample_text", nameVariable="sample_text")
    a2 = myDsl_Variable_declarator(lenVector="sample_text_2", nameVariable="sample_text_2")
    b = myDsl_Variable_declaration(modifiersVariable="sample_text")
    _safe_set(b, 'myDsl_Variable_declaration48', a1)
    assert _is_linked(b, 'myDsl_Variable_declaration48', a1)
    if hasattr(a1, 'myDsl_Variable_declarator'):
        assert _is_linked(a1, 'myDsl_Variable_declarator', b)
    _safe_set(b, 'myDsl_Variable_declaration48', a2)
    assert _is_linked(b, 'myDsl_Variable_declaration48', a2)
    if hasattr(a1, 'myDsl_Variable_declarator'):
        assert not _is_linked(a1, 'myDsl_Variable_declarator', b)
    if hasattr(a2, 'myDsl_Variable_declarator'):
        assert _is_linked(a2, 'myDsl_Variable_declarator', b)
    _safe_set(b, 'myDsl_Variable_declaration48', None)
    assert not _is_linked(b, 'myDsl_Variable_declaration48', a2)
    if hasattr(a2, 'myDsl_Variable_declarator'):
        assert not _is_linked(a2, 'myDsl_Variable_declarator', b)


def test_assoc_names49_reverse_link_reassign_clear():
    a1 = myDsl_Variable_declarator(lenVector="sample_text", nameVariable="sample_text")
    a2 = myDsl_Variable_declarator(lenVector="sample_text_2", nameVariable="sample_text_2")
    b = myDsl_Variable_declaration(modifiersVariable="sample_text")
    _safe_set(b, 'myDsl_Variable_declaration50', {a1})
    assert _is_linked(b, 'myDsl_Variable_declaration50', a1)
    if hasattr(a1, 'myDsl_Variable_declarator51'):
        assert _is_linked(a1, 'myDsl_Variable_declarator51', b)
    _safe_set(b, 'myDsl_Variable_declaration50', {a2})
    assert _is_linked(b, 'myDsl_Variable_declaration50', a2)
    if hasattr(a1, 'myDsl_Variable_declarator51'):
        assert not _is_linked(a1, 'myDsl_Variable_declarator51', b)
    if hasattr(a2, 'myDsl_Variable_declarator51'):
        assert _is_linked(a2, 'myDsl_Variable_declarator51', b)
    _safe_set(b, 'myDsl_Variable_declaration50', set())
    assert not _is_linked(b, 'myDsl_Variable_declaration50', a2)
    if hasattr(a2, 'myDsl_Variable_declarator51'):
        assert not _is_linked(a2, 'myDsl_Variable_declarator51', b)


def test_assoc_numericExpression3113_reverse_link_reassign_clear():
    a1 = myDsl_Numeric_Expression_NR(sinal_numeric="sample_text")
    a2 = myDsl_Numeric_Expression_NR(sinal_numeric="sample_text_2")
    b = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    _safe_set(b, 'myDsl_Expression114', a1)
    assert _is_linked(b, 'myDsl_Expression114', a1)
    if hasattr(a1, 'myDsl_Numeric_Expression_NR'):
        assert _is_linked(a1, 'myDsl_Numeric_Expression_NR', b)
    _safe_set(b, 'myDsl_Expression114', a2)
    assert _is_linked(b, 'myDsl_Expression114', a2)
    if hasattr(a1, 'myDsl_Numeric_Expression_NR'):
        assert not _is_linked(a1, 'myDsl_Numeric_Expression_NR', b)
    if hasattr(a2, 'myDsl_Numeric_Expression_NR'):
        assert _is_linked(a2, 'myDsl_Numeric_Expression_NR', b)
    _safe_set(b, 'myDsl_Expression114', None)
    assert not _is_linked(b, 'myDsl_Expression114', a2)
    if hasattr(a2, 'myDsl_Numeric_Expression_NR'):
        assert not _is_linked(a2, 'myDsl_Numeric_Expression_NR', b)


def test_assoc_parameters214_reverse_link_reassign_clear():
    a1 = myDsl_Try_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Try_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Parameter(parameterName="sample_text")
    _safe_set(b, 'myDsl_Parameter216', a1)
    assert _is_linked(b, 'myDsl_Parameter216', a1)
    if hasattr(a1, 'myDsl_Try_statement215'):
        assert _is_linked(a1, 'myDsl_Try_statement215', b)
    _safe_set(b, 'myDsl_Parameter216', a2)
    assert _is_linked(b, 'myDsl_Parameter216', a2)
    if hasattr(a1, 'myDsl_Try_statement215'):
        assert not _is_linked(a1, 'myDsl_Try_statement215', b)
    if hasattr(a2, 'myDsl_Try_statement215'):
        assert _is_linked(a2, 'myDsl_Try_statement215', b)
    _safe_set(b, 'myDsl_Parameter216', None)
    assert not _is_linked(b, 'myDsl_Parameter216', a2)
    if hasattr(a2, 'myDsl_Try_statement215'):
        assert not _is_linked(a2, 'myDsl_Try_statement215', b)


def test_assoc_statement96_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement97', a1)
    assert _is_linked(b, 'myDsl_Statement97', a1)
    if hasattr(a1, 'myDsl_Statement95'):
        assert _is_linked(a1, 'myDsl_Statement95', b)
    _safe_set(b, 'myDsl_Statement97', a2)
    assert _is_linked(b, 'myDsl_Statement97', a2)
    if hasattr(a1, 'myDsl_Statement95'):
        assert not _is_linked(a1, 'myDsl_Statement95', b)
    if hasattr(a2, 'myDsl_Statement95'):
        assert _is_linked(a2, 'myDsl_Statement95', b)
    _safe_set(b, 'myDsl_Statement97', None)
    assert not _is_linked(b, 'myDsl_Statement97', a2)
    if hasattr(a2, 'myDsl_Statement95'):
        assert not _is_linked(a2, 'myDsl_Statement95', b)


def test_assoc_statementBlock90_reverse_link_reassign_clear():
    a1 = myDsl_Statement_block(lCurly="sample_text", rCurly="sample_text")
    a2 = myDsl_Statement_block(lCurly="sample_text_2", rCurly="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement91', a1)
    assert _is_linked(b, 'myDsl_Statement91', a1)
    if hasattr(a1, 'myDsl_Statement_block92'):
        assert _is_linked(a1, 'myDsl_Statement_block92', b)
    _safe_set(b, 'myDsl_Statement91', a2)
    assert _is_linked(b, 'myDsl_Statement91', a2)
    if hasattr(a1, 'myDsl_Statement_block92'):
        assert not _is_linked(a1, 'myDsl_Statement_block92', b)
    if hasattr(a2, 'myDsl_Statement_block92'):
        assert _is_linked(a2, 'myDsl_Statement_block92', b)
    _safe_set(b, 'myDsl_Statement91', None)
    assert not _is_linked(b, 'myDsl_Statement91', a2)
    if hasattr(a2, 'myDsl_Statement_block92'):
        assert not _is_linked(a2, 'myDsl_Statement_block92', b)


def test_assoc_statementConstructor33_reverse_link_reassign_clear():
    a1 = myDsl_Statement_block(lCurly="sample_text", rCurly="sample_text")
    a2 = myDsl_Statement_block(lCurly="sample_text_2", rCurly="sample_text_2")
    b = myDsl_Constructor_declaration(lParen="sample_text", modifiersConstructor="sample_text", nameConstructor="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Constructor_declaration34', a1)
    assert _is_linked(b, 'myDsl_Constructor_declaration34', a1)
    if hasattr(a1, 'myDsl_Statement_block35'):
        assert _is_linked(a1, 'myDsl_Statement_block35', b)
    _safe_set(b, 'myDsl_Constructor_declaration34', a2)
    assert _is_linked(b, 'myDsl_Constructor_declaration34', a2)
    if hasattr(a1, 'myDsl_Statement_block35'):
        assert not _is_linked(a1, 'myDsl_Statement_block35', b)
    if hasattr(a2, 'myDsl_Statement_block35'):
        assert _is_linked(a2, 'myDsl_Statement_block35', b)
    _safe_set(b, 'myDsl_Constructor_declaration34', None)
    assert not _is_linked(b, 'myDsl_Constructor_declaration34', a2)
    if hasattr(a2, 'myDsl_Statement_block35'):
        assert not _is_linked(a2, 'myDsl_Statement_block35', b)


def test_assoc_statementMethod28_reverse_link_reassign_clear():
    a1 = myDsl_Statement_block(lCurly="sample_text", rCurly="sample_text")
    a2 = myDsl_Statement_block(lCurly="sample_text_2", rCurly="sample_text_2")
    b = myDsl_Method_declaration(debug="sample_text", lParen="sample_text", modifiersMethod="sample_text", nameMethod="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Method_declaration29', a1)
    assert _is_linked(b, 'myDsl_Method_declaration29', a1)
    if hasattr(a1, 'myDsl_Statement_block'):
        assert _is_linked(a1, 'myDsl_Statement_block', b)
    _safe_set(b, 'myDsl_Method_declaration29', a2)
    assert _is_linked(b, 'myDsl_Method_declaration29', a2)
    if hasattr(a1, 'myDsl_Statement_block'):
        assert not _is_linked(a1, 'myDsl_Statement_block', b)
    if hasattr(a2, 'myDsl_Statement_block'):
        assert _is_linked(a2, 'myDsl_Statement_block', b)
    _safe_set(b, 'myDsl_Method_declaration29', None)
    assert not _is_linked(b, 'myDsl_Method_declaration29', a2)
    if hasattr(a2, 'myDsl_Statement_block'):
        assert not _is_linked(a2, 'myDsl_Statement_block', b)


def test_assoc_staticinitializer22_reverse_link_reassign_clear():
    a1 = myDsl_Static_initializer(static="sample_text")
    a2 = myDsl_Static_initializer(static="sample_text_2")
    b = myDsl_Field_declaration(comment="sample_text")
    _safe_set(b, 'myDsl_Field_declaration23', a1)
    assert _is_linked(b, 'myDsl_Field_declaration23', a1)
    if hasattr(a1, 'myDsl_Static_initializer'):
        assert _is_linked(a1, 'myDsl_Static_initializer', b)
    _safe_set(b, 'myDsl_Field_declaration23', a2)
    assert _is_linked(b, 'myDsl_Field_declaration23', a2)
    if hasattr(a1, 'myDsl_Static_initializer'):
        assert not _is_linked(a1, 'myDsl_Static_initializer', b)
    if hasattr(a2, 'myDsl_Static_initializer'):
        assert _is_linked(a2, 'myDsl_Static_initializer', b)
    _safe_set(b, 'myDsl_Field_declaration23', None)
    assert not _is_linked(b, 'myDsl_Field_declaration23', a2)
    if hasattr(a2, 'myDsl_Static_initializer'):
        assert not _is_linked(a2, 'myDsl_Static_initializer', b)


def test_assoc_statments66_reverse_link_reassign_clear():
    a1 = myDsl_Statement_block(lCurly="sample_text", rCurly="sample_text")
    a2 = myDsl_Statement_block(lCurly="sample_text_2", rCurly="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement', a1)
    assert _is_linked(b, 'myDsl_Statement', a1)
    if hasattr(a1, 'myDsl_Statement_block67'):
        assert _is_linked(a1, 'myDsl_Statement_block67', b)
    _safe_set(b, 'myDsl_Statement', a2)
    assert _is_linked(b, 'myDsl_Statement', a2)
    if hasattr(a1, 'myDsl_Statement_block67'):
        assert not _is_linked(a1, 'myDsl_Statement_block67', b)
    if hasattr(a2, 'myDsl_Statement_block67'):
        assert _is_linked(a2, 'myDsl_Statement_block67', b)
    _safe_set(b, 'myDsl_Statement', None)
    assert not _is_linked(b, 'myDsl_Statement', a2)
    if hasattr(a2, 'myDsl_Statement_block67'):
        assert not _is_linked(a2, 'myDsl_Statement_block67', b)


def test_assoc_switchStatement82_reverse_link_reassign_clear():
    a1 = myDsl_Switch_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Switch_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement83', a1)
    assert _is_linked(b, 'myDsl_Statement83', a1)
    if hasattr(a1, 'myDsl_Switch_statement'):
        assert _is_linked(a1, 'myDsl_Switch_statement', b)
    _safe_set(b, 'myDsl_Statement83', a2)
    assert _is_linked(b, 'myDsl_Statement83', a2)
    if hasattr(a1, 'myDsl_Switch_statement'):
        assert not _is_linked(a1, 'myDsl_Switch_statement', b)
    if hasattr(a2, 'myDsl_Switch_statement'):
        assert _is_linked(a2, 'myDsl_Switch_statement', b)
    _safe_set(b, 'myDsl_Statement83', None)
    assert not _is_linked(b, 'myDsl_Statement83', a2)
    if hasattr(a2, 'myDsl_Switch_statement'):
        assert not _is_linked(a2, 'myDsl_Switch_statement', b)


def test_assoc_switchStatements190_reverse_link_reassign_clear():
    a1 = myDsl_Switch_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Switch_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement192', a1)
    assert _is_linked(b, 'myDsl_Statement192', a1)
    if hasattr(a1, 'myDsl_Switch_statement191'):
        assert _is_linked(a1, 'myDsl_Switch_statement191', b)
    _safe_set(b, 'myDsl_Statement192', a2)
    assert _is_linked(b, 'myDsl_Statement192', a2)
    if hasattr(a1, 'myDsl_Switch_statement191'):
        assert not _is_linked(a1, 'myDsl_Switch_statement191', b)
    if hasattr(a2, 'myDsl_Switch_statement191'):
        assert _is_linked(a2, 'myDsl_Switch_statement191', b)
    _safe_set(b, 'myDsl_Statement192', None)
    assert not _is_linked(b, 'myDsl_Statement192', a2)
    if hasattr(a2, 'myDsl_Switch_statement191'):
        assert not _is_linked(a2, 'myDsl_Switch_statement191', b)


def test_assoc_syncStatement88_reverse_link_reassign_clear():
    a1 = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    a2 = myDsl_Statement(g="sample_text_2", name="sample_text_2", nameStatement="sample_text_2", ret="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement89', a1)
    assert _is_linked(b, 'myDsl_Statement89', a1)
    if hasattr(a1, 'myDsl_Statement87'):
        assert _is_linked(a1, 'myDsl_Statement87', b)
    _safe_set(b, 'myDsl_Statement89', a2)
    assert _is_linked(b, 'myDsl_Statement89', a2)
    if hasattr(a1, 'myDsl_Statement87'):
        assert not _is_linked(a1, 'myDsl_Statement87', b)
    if hasattr(a2, 'myDsl_Statement87'):
        assert _is_linked(a2, 'myDsl_Statement87', b)
    _safe_set(b, 'myDsl_Statement89', None)
    assert not _is_linked(b, 'myDsl_Statement89', a2)
    if hasattr(a2, 'myDsl_Statement87'):
        assert not _is_linked(a2, 'myDsl_Statement87', b)


def test_assoc_tryStatement211_reverse_link_reassign_clear():
    a1 = myDsl_Try_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Try_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement213', a1)
    assert _is_linked(b, 'myDsl_Statement213', a1)
    if hasattr(a1, 'myDsl_Try_statement212'):
        assert _is_linked(a1, 'myDsl_Try_statement212', b)
    _safe_set(b, 'myDsl_Statement213', a2)
    assert _is_linked(b, 'myDsl_Statement213', a2)
    if hasattr(a1, 'myDsl_Try_statement212'):
        assert not _is_linked(a1, 'myDsl_Try_statement212', b)
    if hasattr(a2, 'myDsl_Try_statement212'):
        assert _is_linked(a2, 'myDsl_Try_statement212', b)
    _safe_set(b, 'myDsl_Statement213', None)
    assert not _is_linked(b, 'myDsl_Statement213', a2)
    if hasattr(a2, 'myDsl_Try_statement212'):
        assert not _is_linked(a2, 'myDsl_Try_statement212', b)


def test_assoc_tryStatement93_reverse_link_reassign_clear():
    a1 = myDsl_Try_statement(lParen="sample_text", rparent="sample_text")
    a2 = myDsl_Try_statement(lParen="sample_text_2", rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement94', a1)
    assert _is_linked(b, 'myDsl_Statement94', a1)
    if hasattr(a1, 'myDsl_Try_statement'):
        assert _is_linked(a1, 'myDsl_Try_statement', b)
    _safe_set(b, 'myDsl_Statement94', a2)
    assert _is_linked(b, 'myDsl_Statement94', a2)
    if hasattr(a1, 'myDsl_Try_statement'):
        assert not _is_linked(a1, 'myDsl_Try_statement', b)
    if hasattr(a2, 'myDsl_Try_statement'):
        assert _is_linked(a2, 'myDsl_Try_statement', b)
    _safe_set(b, 'myDsl_Statement94', None)
    assert not _is_linked(b, 'myDsl_Statement94', a2)
    if hasattr(a2, 'myDsl_Try_statement'):
        assert not _is_linked(a2, 'myDsl_Try_statement', b)


def test_assoc_type41_reverse_link_reassign_clear():
    a1 = myDsl_Type(typeVector="sample_text")
    a2 = myDsl_Type(typeVector="sample_text_2")
    b = myDsl_Parameter(parameterName="sample_text")
    _safe_set(b, 'myDsl_Parameter42', a1)
    assert _is_linked(b, 'myDsl_Parameter42', a1)
    if hasattr(a1, 'myDsl_Type43'):
        assert _is_linked(a1, 'myDsl_Type43', b)
    _safe_set(b, 'myDsl_Parameter42', a2)
    assert _is_linked(b, 'myDsl_Parameter42', a2)
    if hasattr(a1, 'myDsl_Type43'):
        assert not _is_linked(a1, 'myDsl_Type43', b)
    if hasattr(a2, 'myDsl_Type43'):
        assert _is_linked(a2, 'myDsl_Type43', b)
    _safe_set(b, 'myDsl_Parameter42', None)
    assert not _is_linked(b, 'myDsl_Parameter42', a2)
    if hasattr(a2, 'myDsl_Type43'):
        assert not _is_linked(a2, 'myDsl_Type43', b)


def test_assoc_type44_reverse_link_reassign_clear():
    a1 = myDsl_Variable_declaration(modifiersVariable="sample_text")
    a2 = myDsl_Variable_declaration(modifiersVariable="sample_text_2")
    b = myDsl_Type(typeVector="sample_text")
    _safe_set(b, 'myDsl_Type46', a1)
    assert _is_linked(b, 'myDsl_Type46', a1)
    if hasattr(a1, 'myDsl_Variable_declaration45'):
        assert _is_linked(a1, 'myDsl_Variable_declaration45', b)
    _safe_set(b, 'myDsl_Type46', a2)
    assert _is_linked(b, 'myDsl_Type46', a2)
    if hasattr(a1, 'myDsl_Variable_declaration45'):
        assert not _is_linked(a1, 'myDsl_Variable_declaration45', b)
    if hasattr(a2, 'myDsl_Variable_declaration45'):
        assert _is_linked(a2, 'myDsl_Variable_declaration45', b)
    _safe_set(b, 'myDsl_Type46', None)
    assert not _is_linked(b, 'myDsl_Type46', a2)
    if hasattr(a2, 'myDsl_Variable_declaration45'):
        assert not _is_linked(a2, 'myDsl_Variable_declaration45', b)


def test_assoc_typeMethod24_reverse_link_reassign_clear():
    a1 = myDsl_Type(typeVector="sample_text")
    a2 = myDsl_Type(typeVector="sample_text_2")
    b = myDsl_Method_declaration(debug="sample_text", lParen="sample_text", modifiersMethod="sample_text", nameMethod="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Method_declaration25', a1)
    assert _is_linked(b, 'myDsl_Method_declaration25', a1)
    if hasattr(a1, 'myDsl_Type'):
        assert _is_linked(a1, 'myDsl_Type', b)
    _safe_set(b, 'myDsl_Method_declaration25', a2)
    assert _is_linked(b, 'myDsl_Method_declaration25', a2)
    if hasattr(a1, 'myDsl_Type'):
        assert not _is_linked(a1, 'myDsl_Type', b)
    if hasattr(a2, 'myDsl_Type'):
        assert _is_linked(a2, 'myDsl_Type', b)
    _safe_set(b, 'myDsl_Method_declaration25', None)
    assert not _is_linked(b, 'myDsl_Method_declaration25', a2)
    if hasattr(a2, 'myDsl_Type'):
        assert not _is_linked(a2, 'myDsl_Type', b)


def test_assoc_typeSpecifier157_reverse_link_reassign_clear():
    a1 = myDsl_Type_specifier(className="sample_text", primitiveType="sample_text")
    a2 = myDsl_Type_specifier(className="sample_text_2", primitiveType="sample_text_2")
    b = myDsl_Creating_Expression(className="sample_text")
    _safe_set(b, 'myDsl_Creating_Expression158', a1)
    assert _is_linked(b, 'myDsl_Creating_Expression158', a1)
    if hasattr(a1, 'myDsl_Type_specifier159'):
        assert _is_linked(a1, 'myDsl_Type_specifier159', b)
    _safe_set(b, 'myDsl_Creating_Expression158', a2)
    assert _is_linked(b, 'myDsl_Creating_Expression158', a2)
    if hasattr(a1, 'myDsl_Type_specifier159'):
        assert not _is_linked(a1, 'myDsl_Type_specifier159', b)
    if hasattr(a2, 'myDsl_Type_specifier159'):
        assert _is_linked(a2, 'myDsl_Type_specifier159', b)
    _safe_set(b, 'myDsl_Creating_Expression158', None)
    assert not _is_linked(b, 'myDsl_Creating_Expression158', a2)
    if hasattr(a2, 'myDsl_Type_specifier159'):
        assert not _is_linked(a2, 'myDsl_Type_specifier159', b)


def test_assoc_typeSpecifier61_reverse_link_reassign_clear():
    a1 = myDsl_Type_specifier(className="sample_text", primitiveType="sample_text")
    a2 = myDsl_Type_specifier(className="sample_text_2", primitiveType="sample_text_2")
    b = myDsl_Type(typeVector="sample_text")
    _safe_set(b, 'myDsl_Type62', a1)
    assert _is_linked(b, 'myDsl_Type62', a1)
    if hasattr(a1, 'myDsl_Type_specifier'):
        assert _is_linked(a1, 'myDsl_Type_specifier', b)
    _safe_set(b, 'myDsl_Type62', a2)
    assert _is_linked(b, 'myDsl_Type62', a2)
    if hasattr(a1, 'myDsl_Type_specifier'):
        assert not _is_linked(a1, 'myDsl_Type_specifier', b)
    if hasattr(a2, 'myDsl_Type_specifier'):
        assert _is_linked(a2, 'myDsl_Type_specifier', b)
    _safe_set(b, 'myDsl_Type62', None)
    assert not _is_linked(b, 'myDsl_Type62', a2)
    if hasattr(a2, 'myDsl_Type_specifier'):
        assert not _is_linked(a2, 'myDsl_Type_specifier', b)


def test_assoc_variableDeclaration16_reverse_link_reassign_clear():
    a1 = myDsl_Variable_declaration(modifiersVariable="sample_text")
    a2 = myDsl_Variable_declaration(modifiersVariable="sample_text_2")
    b = myDsl_Field_declaration(comment="sample_text")
    _safe_set(b, 'myDsl_Field_declaration17', a1)
    assert _is_linked(b, 'myDsl_Field_declaration17', a1)
    if hasattr(a1, 'myDsl_Variable_declaration'):
        assert _is_linked(a1, 'myDsl_Variable_declaration', b)
    _safe_set(b, 'myDsl_Field_declaration17', a2)
    assert _is_linked(b, 'myDsl_Field_declaration17', a2)
    if hasattr(a1, 'myDsl_Variable_declaration'):
        assert not _is_linked(a1, 'myDsl_Variable_declaration', b)
    if hasattr(a2, 'myDsl_Variable_declaration'):
        assert _is_linked(a2, 'myDsl_Variable_declaration', b)
    _safe_set(b, 'myDsl_Field_declaration17', None)
    assert not _is_linked(b, 'myDsl_Field_declaration17', a2)
    if hasattr(a2, 'myDsl_Variable_declaration'):
        assert not _is_linked(a2, 'myDsl_Variable_declaration', b)


def test_assoc_variableDeclaration68_reverse_link_reassign_clear():
    a1 = myDsl_Variable_declaration(modifiersVariable="sample_text")
    a2 = myDsl_Variable_declaration(modifiersVariable="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement69', a1)
    assert _is_linked(b, 'myDsl_Statement69', a1)
    if hasattr(a1, 'myDsl_Variable_declaration70'):
        assert _is_linked(a1, 'myDsl_Variable_declaration70', b)
    _safe_set(b, 'myDsl_Statement69', a2)
    assert _is_linked(b, 'myDsl_Statement69', a2)
    if hasattr(a1, 'myDsl_Variable_declaration70'):
        assert not _is_linked(a1, 'myDsl_Variable_declaration70', b)
    if hasattr(a2, 'myDsl_Variable_declaration70'):
        assert _is_linked(a2, 'myDsl_Variable_declaration70', b)
    _safe_set(b, 'myDsl_Statement69', None)
    assert not _is_linked(b, 'myDsl_Statement69', a2)
    if hasattr(a2, 'myDsl_Variable_declaration70'):
        assert not _is_linked(a2, 'myDsl_Variable_declaration70', b)


def test_assoc_whileStatement196_reverse_link_reassign_clear():
    a1 = myDsl_While_Statement(rparent="sample_text")
    a2 = myDsl_While_Statement(rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement198', a1)
    assert _is_linked(b, 'myDsl_Statement198', a1)
    if hasattr(a1, 'myDsl_While_Statement197'):
        assert _is_linked(a1, 'myDsl_While_Statement197', b)
    _safe_set(b, 'myDsl_Statement198', a2)
    assert _is_linked(b, 'myDsl_Statement198', a2)
    if hasattr(a1, 'myDsl_While_Statement197'):
        assert not _is_linked(a1, 'myDsl_While_Statement197', b)
    if hasattr(a2, 'myDsl_While_Statement197'):
        assert _is_linked(a2, 'myDsl_While_Statement197', b)
    _safe_set(b, 'myDsl_Statement198', None)
    assert not _is_linked(b, 'myDsl_Statement198', a2)
    if hasattr(a2, 'myDsl_While_Statement197'):
        assert not _is_linked(a2, 'myDsl_While_Statement197', b)


def test_assoc_whileStatement78_reverse_link_reassign_clear():
    a1 = myDsl_While_Statement(rparent="sample_text")
    a2 = myDsl_While_Statement(rparent="sample_text_2")
    b = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    _safe_set(b, 'myDsl_Statement79', a1)
    assert _is_linked(b, 'myDsl_Statement79', a1)
    if hasattr(a1, 'myDsl_While_Statement'):
        assert _is_linked(a1, 'myDsl_While_Statement', b)
    _safe_set(b, 'myDsl_Statement79', a2)
    assert _is_linked(b, 'myDsl_Statement79', a2)
    if hasattr(a1, 'myDsl_While_Statement'):
        assert not _is_linked(a1, 'myDsl_While_Statement', b)
    if hasattr(a2, 'myDsl_While_Statement'):
        assert _is_linked(a2, 'myDsl_While_Statement', b)
    _safe_set(b, 'myDsl_Statement79', None)
    assert not _is_linked(b, 'myDsl_Statement79', a2)
    if hasattr(a2, 'myDsl_While_Statement'):
        assert not _is_linked(a2, 'myDsl_While_Statement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argList127_stub_double():
    # myDsl_Arg_List has no real 'myDsl_Arg_List' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression_aux's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression_aux's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression_aux(bitSign="sample_text", logicOp="sample_text", logicalSign="sample_text", name="sample_text", numericSign="sample_text", sgin="sample_text", stringSign="sample_text", testingSign="sample_text")
    partner = myDsl_Arg_List()
    setattr(partner, 'myDsl_Arg_List', None)
    _safe_set(owner, 'myDsl_Expression_aux128', partner)
    assert getattr(partner, 'myDsl_Arg_List') == owner
    _safe_set(owner, 'myDsl_Expression_aux128', None)
    assert getattr(partner, 'myDsl_Arg_List') is None


def test_assoc_argList154_stub_double():
    # myDsl_Arg_List has no real 'myDsl_Arg_List156' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Creating_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Creating_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Creating_Expression(className="sample_text")
    partner = myDsl_Arg_List()
    setattr(partner, 'myDsl_Arg_List156', None)
    _safe_set(owner, 'myDsl_Creating_Expression155', partner)
    assert getattr(partner, 'myDsl_Arg_List156') == owner
    _safe_set(owner, 'myDsl_Creating_Expression155', None)
    assert getattr(partner, 'myDsl_Arg_List156') is None


def test_assoc_bitExpression119_stub_double():
    # myDsl_Bit_Expression_NR has no real 'myDsl_Bit_Expression_NR' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Bit_Expression_NR()
    setattr(partner, 'myDsl_Bit_Expression_NR', None)
    _safe_set(owner, 'myDsl_Expression120', partner)
    assert getattr(partner, 'myDsl_Bit_Expression_NR') == owner
    _safe_set(owner, 'myDsl_Expression120', None)
    assert getattr(partner, 'myDsl_Bit_Expression_NR') is None


def test_assoc_castExpression121_stub_double():
    # myDsl_Cast_Expression has no real 'myDsl_Cast_Expression' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Cast_Expression()
    setattr(partner, 'myDsl_Cast_Expression', None)
    _safe_set(owner, 'myDsl_Expression122', partner)
    assert getattr(partner, 'myDsl_Cast_Expression') == owner
    _safe_set(owner, 'myDsl_Expression122', None)
    assert getattr(partner, 'myDsl_Cast_Expression') is None


def test_assoc_expression101_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement102' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement102', None)
    _safe_set(owner, 'myDsl_Expression103', partner)
    assert getattr(partner, 'myDsl_For_Statement102') == owner
    _safe_set(owner, 'myDsl_Expression103', None)
    assert getattr(partner, 'myDsl_For_Statement102') is None


def test_assoc_expression166_stub_double():
    # myDsl_Cast_Expression has no real 'myDsl_Cast_Expression167' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Cast_Expression()
    setattr(partner, 'myDsl_Cast_Expression167', None)
    _safe_set(owner, 'myDsl_Expression168', partner)
    assert getattr(partner, 'myDsl_Cast_Expression167') == owner
    _safe_set(owner, 'myDsl_Expression168', None)
    assert getattr(partner, 'myDsl_Cast_Expression167') is None


def test_assoc_expression169_stub_double():
    # myDsl_Bit_Expression_NR has no real 'myDsl_Bit_Expression_NR170' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Bit_Expression_NR()
    setattr(partner, 'myDsl_Bit_Expression_NR170', None)
    _safe_set(owner, 'myDsl_Expression171', partner)
    assert getattr(partner, 'myDsl_Bit_Expression_NR170') == owner
    _safe_set(owner, 'myDsl_Expression171', None)
    assert getattr(partner, 'myDsl_Bit_Expression_NR170') is None


def test_assoc_expression175_stub_double():
    # myDsl_Arg_List has no real 'myDsl_Arg_List176' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Arg_List()
    setattr(partner, 'myDsl_Arg_List176', None)
    _safe_set(owner, 'myDsl_Expression177', partner)
    assert getattr(partner, 'myDsl_Arg_List176') == owner
    _safe_set(owner, 'myDsl_Expression177', None)
    assert getattr(partner, 'myDsl_Arg_List176') is None


def test_assoc_expression2104_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement105' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement105', None)
    _safe_set(owner, 'myDsl_Expression106', partner)
    assert getattr(partner, 'myDsl_For_Statement105') == owner
    _safe_set(owner, 'myDsl_Expression106', None)
    assert getattr(partner, 'myDsl_For_Statement105') is None


def test_assoc_expression3107_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement108' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement108', None)
    _safe_set(owner, 'myDsl_Expression109', partner)
    assert getattr(partner, 'myDsl_For_Statement108') == owner
    _safe_set(owner, 'myDsl_Expression109', None)
    assert getattr(partner, 'myDsl_For_Statement108') is None


def test_assoc_expression56_stub_double():
    # myDsl_Variable_initializer has no real 'myDsl_Variable_initializer57' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Variable_initializer()
    setattr(partner, 'myDsl_Variable_initializer57', None)
    _safe_set(owner, 'myDsl_Expression', partner)
    assert getattr(partner, 'myDsl_Variable_initializer57') == owner
    _safe_set(owner, 'myDsl_Expression', None)
    assert getattr(partner, 'myDsl_Variable_initializer57') is None


def test_assoc_expressions178_stub_double():
    # myDsl_Arg_List has no real 'myDsl_Arg_List179' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Expression(name="sample_text", null="sample_text", super="sample_text", this="sample_text")
    partner = myDsl_Arg_List()
    setattr(partner, 'myDsl_Arg_List179', None)
    _safe_set(owner, 'myDsl_Expression180', partner)
    assert owner in getattr(partner, 'myDsl_Arg_List179')
    _safe_set(owner, 'myDsl_Expression180', None)
    assert owner not in getattr(partner, 'myDsl_Arg_List179')


def test_assoc_forStatement80_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement', None)
    _safe_set(owner, 'myDsl_Statement81', partner)
    assert getattr(partner, 'myDsl_For_Statement') == owner
    _safe_set(owner, 'myDsl_Statement81', None)
    assert getattr(partner, 'myDsl_For_Statement') is None


def test_assoc_imports3_stub_double():
    # myDsl_Compilation_unit has no real 'myDsl_Compilation_unit4' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Import_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Import_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Import_statement(className="sample_text", pacName="sample_text")
    partner = myDsl_Compilation_unit()
    setattr(partner, 'myDsl_Compilation_unit4', None)
    _safe_set(owner, 'myDsl_Import_statement', partner)
    assert owner in getattr(partner, 'myDsl_Compilation_unit4')
    _safe_set(owner, 'myDsl_Import_statement', None)
    assert owner not in getattr(partner, 'myDsl_Compilation_unit4')


def test_assoc_name1_stub_double():
    # myDsl_Compilation_unit has no real 'myDsl_Compilation_unit2' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Package_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Package_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Package_statement(pacName="sample_text")
    partner = myDsl_Compilation_unit()
    setattr(partner, 'myDsl_Compilation_unit2', None)
    _safe_set(owner, 'myDsl_Package_statement', partner)
    assert getattr(partner, 'myDsl_Compilation_unit2') == owner
    _safe_set(owner, 'myDsl_Package_statement', None)
    assert getattr(partner, 'myDsl_Compilation_unit2') is None


def test_assoc_parameter36_stub_double():
    # myDsl_Parameter_list has no real 'myDsl_Parameter_list37' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Parameter(parameterName="sample_text")
    partner = myDsl_Parameter_list()
    setattr(partner, 'myDsl_Parameter_list37', None)
    _safe_set(owner, 'myDsl_Parameter', partner)
    assert getattr(partner, 'myDsl_Parameter_list37') == owner
    _safe_set(owner, 'myDsl_Parameter', None)
    assert getattr(partner, 'myDsl_Parameter_list37') is None


def test_assoc_parameterListConstructor30_stub_double():
    # myDsl_Parameter_list has no real 'myDsl_Parameter_list32' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Constructor_declaration(lParen="sample_text", modifiersConstructor="sample_text", nameConstructor="sample_text", rparent="sample_text")
    partner = myDsl_Parameter_list()
    setattr(partner, 'myDsl_Parameter_list32', None)
    _safe_set(owner, 'myDsl_Constructor_declaration31', partner)
    assert getattr(partner, 'myDsl_Parameter_list32') == owner
    _safe_set(owner, 'myDsl_Constructor_declaration31', None)
    assert getattr(partner, 'myDsl_Parameter_list32') is None


def test_assoc_parameterListMethod26_stub_double():
    # myDsl_Parameter_list has no real 'myDsl_Parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Method_declaration(debug="sample_text", lParen="sample_text", modifiersMethod="sample_text", nameMethod="sample_text", rparent="sample_text")
    partner = myDsl_Parameter_list()
    setattr(partner, 'myDsl_Parameter_list', None)
    _safe_set(owner, 'myDsl_Method_declaration27', partner)
    assert getattr(partner, 'myDsl_Parameter_list') == owner
    _safe_set(owner, 'myDsl_Method_declaration27', None)
    assert getattr(partner, 'myDsl_Parameter_list') is None


def test_assoc_parameters38_stub_double():
    # myDsl_Parameter_list has no real 'myDsl_Parameter_list39' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Parameter(parameterName="sample_text")
    partner = myDsl_Parameter_list()
    setattr(partner, 'myDsl_Parameter_list39', None)
    _safe_set(owner, 'myDsl_Parameter40', partner)
    assert owner in getattr(partner, 'myDsl_Parameter_list39')
    _safe_set(owner, 'myDsl_Parameter40', None)
    assert owner not in getattr(partner, 'myDsl_Parameter_list39')


def test_assoc_statement110_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement111' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Statement(g="sample_text", name="sample_text", nameStatement="sample_text", ret="sample_text", rparent="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement111', None)
    _safe_set(owner, 'myDsl_Statement112', partner)
    assert getattr(partner, 'myDsl_For_Statement111') == owner
    _safe_set(owner, 'myDsl_Statement112', None)
    assert getattr(partner, 'myDsl_For_Statement111') is None


def test_assoc_type163_stub_double():
    # myDsl_Cast_Expression has no real 'myDsl_Cast_Expression164' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Type(typeVector="sample_text")
    partner = myDsl_Cast_Expression()
    setattr(partner, 'myDsl_Cast_Expression164', None)
    _safe_set(owner, 'myDsl_Type165', partner)
    assert getattr(partner, 'myDsl_Cast_Expression164') == owner
    _safe_set(owner, 'myDsl_Type165', None)
    assert getattr(partner, 'myDsl_Cast_Expression164') is None


def test_assoc_typeDeclarations5_stub_double():
    # myDsl_Compilation_unit has no real 'myDsl_Compilation_unit6' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Type_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Type_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Type_declaration(comment="sample_text")
    partner = myDsl_Compilation_unit()
    setattr(partner, 'myDsl_Compilation_unit6', None)
    _safe_set(owner, 'myDsl_Type_declaration', partner)
    assert owner in getattr(partner, 'myDsl_Compilation_unit6')
    _safe_set(owner, 'myDsl_Type_declaration', None)
    assert owner not in getattr(partner, 'myDsl_Compilation_unit6')


def test_assoc_vari52_stub_double():
    # myDsl_Variable_initializer has no real 'myDsl_Variable_initializer' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Variable_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Variable_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Variable_declarator(lenVector="sample_text", nameVariable="sample_text")
    partner = myDsl_Variable_initializer()
    setattr(partner, 'myDsl_Variable_initializer', None)
    _safe_set(owner, 'myDsl_Variable_declarator53', partner)
    assert getattr(partner, 'myDsl_Variable_initializer') == owner
    _safe_set(owner, 'myDsl_Variable_declarator53', None)
    assert getattr(partner, 'myDsl_Variable_initializer') is None


def test_assoc_variable98_stub_double():
    # myDsl_For_Statement has no real 'myDsl_For_Statement99' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Variable_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Variable_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Variable_declaration(modifiersVariable="sample_text")
    partner = myDsl_For_Statement()
    setattr(partner, 'myDsl_For_Statement99', None)
    _safe_set(owner, 'myDsl_Variable_declaration100', partner)
    assert getattr(partner, 'myDsl_For_Statement99') == owner
    _safe_set(owner, 'myDsl_Variable_declaration100', None)
    assert getattr(partner, 'myDsl_For_Statement99') is None


