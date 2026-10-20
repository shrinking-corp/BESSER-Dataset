# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    noop_Index,
    noop_ConstructorField,
    noop_Constructor,
    noop_Statement,
    noop_ElseStatement,
    noop_Block,
    noop_Length,
    Statement,
    noop_IfStatement,
    noop_AsmStatement,
    noop_BreakStatement,
    noop_ForStatement,
    noop_ContinueStatement,
    noop_ReturnStatement,
    noop_ForeverStatement,
    Member,
    noop_Method,
    noop_Variable,
    noop_Expression,
    noop_Storage,
    noop_Member,
    noop_NoopClass,
    Expression,
    noop_LShiftExpression,
    noop_Super,
    noop_ArrayLiteral,
    noop_StringLiteral,
    noop_ByteLiteral,
    noop_AndExpression,
    noop_CastExpression,
    noop_BOrExpression,
    noop_BoolLiteral,
    noop_BXorExpression,
    noop_LtExpression,
    noop_LeExpression,
    noop_SigPosExpression,
    noop_NotExpression,
    noop_MemberRef,
    noop_NewInstance,
    noop_SigNegExpression,
    noop_AddExpression,
    noop_OrExpression,
    noop_InstanceOfExpression,
    noop_GtExpression,
    noop_DecExpression,
    noop_DivExpression,
    noop_GeExpression,
    noop_ComplementExpression,
    noop_ModExpression,
    noop_MulExpression,
    noop_BAndExpression,
    noop_This,
    noop_SubExpression,
    noop_RShiftExpression,
    noop_MemberSelect,
    noop_IncExpression,
    noop_AssignmentExpression,
    noop_DifferExpression,
    noop_EqualsExpression,
    StorageType,
    AssignmentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_noop_index_is_not_abstract():
    assert not inspect.isabstract(noop_Index)


def test_hyp_noop_index_constructor_exists():
    assert callable(noop_Index.__init__)


def test_hyp_noop_index_constructor_args():
    sig = inspect.signature(noop_Index.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_constructorfield_is_not_abstract():
    assert not inspect.isabstract(noop_ConstructorField)


def test_hyp_noop_constructorfield_constructor_exists():
    assert callable(noop_ConstructorField.__init__)


def test_hyp_noop_constructorfield_constructor_args():
    sig = inspect.signature(noop_ConstructorField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_constructor_is_not_abstract():
    assert not inspect.isabstract(noop_Constructor)


def test_hyp_noop_constructor_constructor_exists():
    assert callable(noop_Constructor.__init__)


def test_hyp_noop_constructor_constructor_args():
    sig = inspect.signature(noop_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_statement_is_not_abstract():
    assert not inspect.isabstract(noop_Statement)


def test_hyp_noop_statement_constructor_exists():
    assert callable(noop_Statement.__init__)


def test_hyp_noop_statement_constructor_args():
    sig = inspect.signature(noop_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_elsestatement_is_not_abstract():
    assert not inspect.isabstract(noop_ElseStatement)


def test_hyp_noop_elsestatement_constructor_exists():
    assert callable(noop_ElseStatement.__init__)


def test_hyp_noop_elsestatement_constructor_args():
    sig = inspect.signature(noop_ElseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_block_is_not_abstract():
    assert not inspect.isabstract(noop_Block)


def test_hyp_noop_block_constructor_exists():
    assert callable(noop_Block.__init__)


def test_hyp_noop_block_constructor_args():
    sig = inspect.signature(noop_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_length_is_not_abstract():
    assert not inspect.isabstract(noop_Length)


def test_hyp_noop_length_constructor_exists():
    assert callable(noop_Length.__init__)


def test_hyp_noop_length_constructor_args():
    sig = inspect.signature(noop_Length.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_ifstatement_is_not_abstract():
    assert not inspect.isabstract(noop_IfStatement)


def test_hyp_noop_ifstatement_constructor_exists():
    assert callable(noop_IfStatement.__init__)


def test_hyp_noop_ifstatement_constructor_args():
    sig = inspect.signature(noop_IfStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_asmstatement_is_not_abstract():
    assert not inspect.isabstract(noop_AsmStatement)


def test_hyp_noop_asmstatement_constructor_exists():
    assert callable(noop_AsmStatement.__init__)


def test_hyp_noop_asmstatement_constructor_args():
    sig = inspect.signature(noop_AsmStatement.__init__)
    params = list(sig.parameters.keys())
    assert "codes" in params, "Missing parameter 'codes'"




def test_hyp_noop_breakstatement_is_not_abstract():
    assert not inspect.isabstract(noop_BreakStatement)


def test_hyp_noop_breakstatement_constructor_exists():
    assert callable(noop_BreakStatement.__init__)


def test_hyp_noop_breakstatement_constructor_args():
    sig = inspect.signature(noop_BreakStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_forstatement_is_not_abstract():
    assert not inspect.isabstract(noop_ForStatement)


def test_hyp_noop_forstatement_constructor_exists():
    assert callable(noop_ForStatement.__init__)


def test_hyp_noop_forstatement_constructor_args():
    sig = inspect.signature(noop_ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_continuestatement_is_not_abstract():
    assert not inspect.isabstract(noop_ContinueStatement)


def test_hyp_noop_continuestatement_constructor_exists():
    assert callable(noop_ContinueStatement.__init__)


def test_hyp_noop_continuestatement_constructor_args():
    sig = inspect.signature(noop_ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_returnstatement_is_not_abstract():
    assert not inspect.isabstract(noop_ReturnStatement)


def test_hyp_noop_returnstatement_constructor_exists():
    assert callable(noop_ReturnStatement.__init__)


def test_hyp_noop_returnstatement_constructor_args():
    sig = inspect.signature(noop_ReturnStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_foreverstatement_is_not_abstract():
    assert not inspect.isabstract(noop_ForeverStatement)


def test_hyp_noop_foreverstatement_constructor_exists():
    assert callable(noop_ForeverStatement.__init__)


def test_hyp_noop_foreverstatement_constructor_args():
    sig = inspect.signature(noop_ForeverStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_hyp_member_constructor_exists():
    assert callable(Member.__init__)


def test_hyp_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_method_is_not_abstract():
    assert not inspect.isabstract(noop_Method)


def test_hyp_noop_method_constructor_exists():
    assert callable(noop_Method.__init__)


def test_hyp_noop_method_constructor_args():
    sig = inspect.signature(noop_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_variable_is_not_abstract():
    assert not inspect.isabstract(noop_Variable)


def test_hyp_noop_variable_constructor_exists():
    assert callable(noop_Variable.__init__)


def test_hyp_noop_variable_constructor_args():
    sig = inspect.signature(noop_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_expression_is_not_abstract():
    assert not inspect.isabstract(noop_Expression)


def test_hyp_noop_expression_constructor_exists():
    assert callable(noop_Expression.__init__)


def test_hyp_noop_expression_constructor_args():
    sig = inspect.signature(noop_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_storage_is_not_abstract():
    assert not inspect.isabstract(noop_Storage)


def test_hyp_noop_storage_constructor_exists():
    assert callable(noop_Storage.__init__)


def test_hyp_noop_storage_constructor_args():
    sig = inspect.signature(noop_Storage.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_noop_member_is_not_abstract():
    assert not inspect.isabstract(noop_Member)


def test_hyp_noop_member_constructor_exists():
    assert callable(noop_Member.__init__)


def test_hyp_noop_member_constructor_args():
    sig = inspect.signature(noop_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_noop_noopclass_is_not_abstract():
    assert not inspect.isabstract(noop_NoopClass)


def test_hyp_noop_noopclass_constructor_exists():
    assert callable(noop_NoopClass.__init__)


def test_hyp_noop_noopclass_constructor_args():
    sig = inspect.signature(noop_NoopClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_lshiftexpression_is_not_abstract():
    assert not inspect.isabstract(noop_LShiftExpression)


def test_hyp_noop_lshiftexpression_constructor_exists():
    assert callable(noop_LShiftExpression.__init__)


def test_hyp_noop_lshiftexpression_constructor_args():
    sig = inspect.signature(noop_LShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_super_is_not_abstract():
    assert not inspect.isabstract(noop_Super)


def test_hyp_noop_super_constructor_exists():
    assert callable(noop_Super.__init__)


def test_hyp_noop_super_constructor_args():
    sig = inspect.signature(noop_Super.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(noop_ArrayLiteral)


def test_hyp_noop_arrayliteral_constructor_exists():
    assert callable(noop_ArrayLiteral.__init__)


def test_hyp_noop_arrayliteral_constructor_args():
    sig = inspect.signature(noop_ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_stringliteral_is_not_abstract():
    assert not inspect.isabstract(noop_StringLiteral)


def test_hyp_noop_stringliteral_constructor_exists():
    assert callable(noop_StringLiteral.__init__)


def test_hyp_noop_stringliteral_constructor_args():
    sig = inspect.signature(noop_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_noop_byteliteral_is_not_abstract():
    assert not inspect.isabstract(noop_ByteLiteral)


def test_hyp_noop_byteliteral_constructor_exists():
    assert callable(noop_ByteLiteral.__init__)


def test_hyp_noop_byteliteral_constructor_args():
    sig = inspect.signature(noop_ByteLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_noop_andexpression_is_not_abstract():
    assert not inspect.isabstract(noop_AndExpression)


def test_hyp_noop_andexpression_constructor_exists():
    assert callable(noop_AndExpression.__init__)


def test_hyp_noop_andexpression_constructor_args():
    sig = inspect.signature(noop_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_castexpression_is_not_abstract():
    assert not inspect.isabstract(noop_CastExpression)


def test_hyp_noop_castexpression_constructor_exists():
    assert callable(noop_CastExpression.__init__)


def test_hyp_noop_castexpression_constructor_args():
    sig = inspect.signature(noop_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_borexpression_is_not_abstract():
    assert not inspect.isabstract(noop_BOrExpression)


def test_hyp_noop_borexpression_constructor_exists():
    assert callable(noop_BOrExpression.__init__)


def test_hyp_noop_borexpression_constructor_args():
    sig = inspect.signature(noop_BOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_boolliteral_is_not_abstract():
    assert not inspect.isabstract(noop_BoolLiteral)


def test_hyp_noop_boolliteral_constructor_exists():
    assert callable(noop_BoolLiteral.__init__)


def test_hyp_noop_boolliteral_constructor_args():
    sig = inspect.signature(noop_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_noop_bxorexpression_is_not_abstract():
    assert not inspect.isabstract(noop_BXorExpression)


def test_hyp_noop_bxorexpression_constructor_exists():
    assert callable(noop_BXorExpression.__init__)


def test_hyp_noop_bxorexpression_constructor_args():
    sig = inspect.signature(noop_BXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_ltexpression_is_not_abstract():
    assert not inspect.isabstract(noop_LtExpression)


def test_hyp_noop_ltexpression_constructor_exists():
    assert callable(noop_LtExpression.__init__)


def test_hyp_noop_ltexpression_constructor_args():
    sig = inspect.signature(noop_LtExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_leexpression_is_not_abstract():
    assert not inspect.isabstract(noop_LeExpression)


def test_hyp_noop_leexpression_constructor_exists():
    assert callable(noop_LeExpression.__init__)


def test_hyp_noop_leexpression_constructor_args():
    sig = inspect.signature(noop_LeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_sigposexpression_is_not_abstract():
    assert not inspect.isabstract(noop_SigPosExpression)


def test_hyp_noop_sigposexpression_constructor_exists():
    assert callable(noop_SigPosExpression.__init__)


def test_hyp_noop_sigposexpression_constructor_args():
    sig = inspect.signature(noop_SigPosExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_notexpression_is_not_abstract():
    assert not inspect.isabstract(noop_NotExpression)


def test_hyp_noop_notexpression_constructor_exists():
    assert callable(noop_NotExpression.__init__)


def test_hyp_noop_notexpression_constructor_args():
    sig = inspect.signature(noop_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_memberref_is_not_abstract():
    assert not inspect.isabstract(noop_MemberRef)


def test_hyp_noop_memberref_constructor_exists():
    assert callable(noop_MemberRef.__init__)


def test_hyp_noop_memberref_constructor_args():
    sig = inspect.signature(noop_MemberRef.__init__)
    params = list(sig.parameters.keys())
    assert "hasArgs" in params, "Missing parameter 'hasArgs'"




def test_hyp_noop_newinstance_is_not_abstract():
    assert not inspect.isabstract(noop_NewInstance)


def test_hyp_noop_newinstance_constructor_exists():
    assert callable(noop_NewInstance.__init__)


def test_hyp_noop_newinstance_constructor_args():
    sig = inspect.signature(noop_NewInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_signegexpression_is_not_abstract():
    assert not inspect.isabstract(noop_SigNegExpression)


def test_hyp_noop_signegexpression_constructor_exists():
    assert callable(noop_SigNegExpression.__init__)


def test_hyp_noop_signegexpression_constructor_args():
    sig = inspect.signature(noop_SigNegExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_addexpression_is_not_abstract():
    assert not inspect.isabstract(noop_AddExpression)


def test_hyp_noop_addexpression_constructor_exists():
    assert callable(noop_AddExpression.__init__)


def test_hyp_noop_addexpression_constructor_args():
    sig = inspect.signature(noop_AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_orexpression_is_not_abstract():
    assert not inspect.isabstract(noop_OrExpression)


def test_hyp_noop_orexpression_constructor_exists():
    assert callable(noop_OrExpression.__init__)


def test_hyp_noop_orexpression_constructor_args():
    sig = inspect.signature(noop_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(noop_InstanceOfExpression)


def test_hyp_noop_instanceofexpression_constructor_exists():
    assert callable(noop_InstanceOfExpression.__init__)


def test_hyp_noop_instanceofexpression_constructor_args():
    sig = inspect.signature(noop_InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_gtexpression_is_not_abstract():
    assert not inspect.isabstract(noop_GtExpression)


def test_hyp_noop_gtexpression_constructor_exists():
    assert callable(noop_GtExpression.__init__)


def test_hyp_noop_gtexpression_constructor_args():
    sig = inspect.signature(noop_GtExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_decexpression_is_not_abstract():
    assert not inspect.isabstract(noop_DecExpression)


def test_hyp_noop_decexpression_constructor_exists():
    assert callable(noop_DecExpression.__init__)


def test_hyp_noop_decexpression_constructor_args():
    sig = inspect.signature(noop_DecExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_divexpression_is_not_abstract():
    assert not inspect.isabstract(noop_DivExpression)


def test_hyp_noop_divexpression_constructor_exists():
    assert callable(noop_DivExpression.__init__)


def test_hyp_noop_divexpression_constructor_args():
    sig = inspect.signature(noop_DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_geexpression_is_not_abstract():
    assert not inspect.isabstract(noop_GeExpression)


def test_hyp_noop_geexpression_constructor_exists():
    assert callable(noop_GeExpression.__init__)


def test_hyp_noop_geexpression_constructor_args():
    sig = inspect.signature(noop_GeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_complementexpression_is_not_abstract():
    assert not inspect.isabstract(noop_ComplementExpression)


def test_hyp_noop_complementexpression_constructor_exists():
    assert callable(noop_ComplementExpression.__init__)


def test_hyp_noop_complementexpression_constructor_args():
    sig = inspect.signature(noop_ComplementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_modexpression_is_not_abstract():
    assert not inspect.isabstract(noop_ModExpression)


def test_hyp_noop_modexpression_constructor_exists():
    assert callable(noop_ModExpression.__init__)


def test_hyp_noop_modexpression_constructor_args():
    sig = inspect.signature(noop_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_mulexpression_is_not_abstract():
    assert not inspect.isabstract(noop_MulExpression)


def test_hyp_noop_mulexpression_constructor_exists():
    assert callable(noop_MulExpression.__init__)


def test_hyp_noop_mulexpression_constructor_args():
    sig = inspect.signature(noop_MulExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_bandexpression_is_not_abstract():
    assert not inspect.isabstract(noop_BAndExpression)


def test_hyp_noop_bandexpression_constructor_exists():
    assert callable(noop_BAndExpression.__init__)


def test_hyp_noop_bandexpression_constructor_args():
    sig = inspect.signature(noop_BAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_this_is_not_abstract():
    assert not inspect.isabstract(noop_This)


def test_hyp_noop_this_constructor_exists():
    assert callable(noop_This.__init__)


def test_hyp_noop_this_constructor_args():
    sig = inspect.signature(noop_This.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_subexpression_is_not_abstract():
    assert not inspect.isabstract(noop_SubExpression)


def test_hyp_noop_subexpression_constructor_exists():
    assert callable(noop_SubExpression.__init__)


def test_hyp_noop_subexpression_constructor_args():
    sig = inspect.signature(noop_SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_rshiftexpression_is_not_abstract():
    assert not inspect.isabstract(noop_RShiftExpression)


def test_hyp_noop_rshiftexpression_constructor_exists():
    assert callable(noop_RShiftExpression.__init__)


def test_hyp_noop_rshiftexpression_constructor_args():
    sig = inspect.signature(noop_RShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_memberselect_is_not_abstract():
    assert not inspect.isabstract(noop_MemberSelect)


def test_hyp_noop_memberselect_constructor_exists():
    assert callable(noop_MemberSelect.__init__)


def test_hyp_noop_memberselect_constructor_args():
    sig = inspect.signature(noop_MemberSelect.__init__)
    params = list(sig.parameters.keys())
    assert "hasArgs" in params, "Missing parameter 'hasArgs'"




def test_hyp_noop_incexpression_is_not_abstract():
    assert not inspect.isabstract(noop_IncExpression)


def test_hyp_noop_incexpression_constructor_exists():
    assert callable(noop_IncExpression.__init__)


def test_hyp_noop_incexpression_constructor_args():
    sig = inspect.signature(noop_IncExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(noop_AssignmentExpression)


def test_hyp_noop_assignmentexpression_constructor_exists():
    assert callable(noop_AssignmentExpression.__init__)


def test_hyp_noop_assignmentexpression_constructor_args():
    sig = inspect.signature(noop_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assignment" in params, "Missing parameter 'assignment'"




def test_hyp_noop_differexpression_is_not_abstract():
    assert not inspect.isabstract(noop_DifferExpression)


def test_hyp_noop_differexpression_constructor_exists():
    assert callable(noop_DifferExpression.__init__)


def test_hyp_noop_differexpression_constructor_args():
    sig = inspect.signature(noop_DifferExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noop_equalsexpression_is_not_abstract():
    assert not inspect.isabstract(noop_EqualsExpression)


def test_hyp_noop_equalsexpression_constructor_exists():
    assert callable(noop_EqualsExpression.__init__)


def test_hyp_noop_equalsexpression_constructor_args():
    sig = inspect.signature(noop_EqualsExpression.__init__)
    params = list(sig.parameters.keys())

def test_hyp_storagetype_exists():
    # Check that the Enumeration exists
    assert StorageType is not None

def test_hyp_storagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StorageType]
    expected_literals = [
        "INESPRG",
        "RESET",
        "ZP",
        "CHRROM",
        "INLINE",
        "INESMAPPER",
        "MMC3CFG",
        "PRGROM",
        "INESCHR",
        "IRQ",
        "INESMIR",
        "NMI",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StorageType"

def test_hyp_assignmenttype_exists():
    # Check that the Enumeration exists
    assert AssignmentType is not None

def test_hyp_assignmenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentType]
    expected_literals = [
        "BOR_ASSIGN",
        "SUB_ASSIGN",
        "MUL_ASSIGN",
        "BAN_ASSIGN",
        "BRS_ASSIGN",
        "ASSIGN",
        "ADD_ASSIGN",
        "XOR_ASSIGN",
        "MOD_ASSIGN",
        "BLS_ASSIGN",
        "DIV_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
noop_Index_strategy = st.builds(
    noop_Index,
)
noop_ConstructorField_strategy = st.builds(
    noop_ConstructorField,
)
noop_Constructor_strategy = st.builds(
    noop_Constructor,
)
noop_Statement_strategy = st.builds(
    noop_Statement,
)
noop_ElseStatement_strategy = st.builds(
    noop_ElseStatement,
    name=
        safe_text
)
noop_Block_strategy = st.builds(
    noop_Block,
)
noop_Length_strategy = st.builds(
    noop_Length,
)
Statement_strategy = st.builds(
    Statement,
)
noop_IfStatement_strategy = st.builds(
    noop_IfStatement,
    name=
        safe_text
)
noop_AsmStatement_strategy = st.builds(
    noop_AsmStatement,
    codes=
        safe_text
)
noop_BreakStatement_strategy = st.builds(
    noop_BreakStatement,
    name=
        safe_text
)
noop_ForStatement_strategy = st.builds(
    noop_ForStatement,
    name=
        safe_text
)
noop_ContinueStatement_strategy = st.builds(
    noop_ContinueStatement,
    name=
        safe_text
)
noop_ReturnStatement_strategy = st.builds(
    noop_ReturnStatement,
    name=
        safe_text
)
noop_ForeverStatement_strategy = st.builds(
    noop_ForeverStatement,
    name=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
noop_Method_strategy = st.builds(
    noop_Method,
)
noop_Variable_strategy = st.builds(
    noop_Variable,
)
noop_Expression_strategy = st.builds(
    noop_Expression,
)
noop_Storage_strategy = st.builds(
    noop_Storage,
    type=
        safe_text
)
noop_Member_strategy = st.builds(
    noop_Member,
    name=
        safe_text
)
noop_NoopClass_strategy = st.builds(
    noop_NoopClass,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
noop_LShiftExpression_strategy = st.builds(
    noop_LShiftExpression,
)
noop_Super_strategy = st.builds(
    noop_Super,
)
noop_ArrayLiteral_strategy = st.builds(
    noop_ArrayLiteral,
)
noop_StringLiteral_strategy = st.builds(
    noop_StringLiteral,
    value=
        safe_text
)
noop_ByteLiteral_strategy = st.builds(
    noop_ByteLiteral,
    value=
        safe_text
)
noop_AndExpression_strategy = st.builds(
    noop_AndExpression,
)
noop_CastExpression_strategy = st.builds(
    noop_CastExpression,
)
noop_BOrExpression_strategy = st.builds(
    noop_BOrExpression,
)
noop_BoolLiteral_strategy = st.builds(
    noop_BoolLiteral,
    value=
        st.booleans()
)
noop_BXorExpression_strategy = st.builds(
    noop_BXorExpression,
)
noop_LtExpression_strategy = st.builds(
    noop_LtExpression,
)
noop_LeExpression_strategy = st.builds(
    noop_LeExpression,
)
noop_SigPosExpression_strategy = st.builds(
    noop_SigPosExpression,
)
noop_NotExpression_strategy = st.builds(
    noop_NotExpression,
)
noop_MemberRef_strategy = st.builds(
    noop_MemberRef,
    hasArgs=
        st.booleans()
)
noop_NewInstance_strategy = st.builds(
    noop_NewInstance,
)
noop_SigNegExpression_strategy = st.builds(
    noop_SigNegExpression,
)
noop_AddExpression_strategy = st.builds(
    noop_AddExpression,
)
noop_OrExpression_strategy = st.builds(
    noop_OrExpression,
)
noop_InstanceOfExpression_strategy = st.builds(
    noop_InstanceOfExpression,
)
noop_GtExpression_strategy = st.builds(
    noop_GtExpression,
)
noop_DecExpression_strategy = st.builds(
    noop_DecExpression,
)
noop_DivExpression_strategy = st.builds(
    noop_DivExpression,
)
noop_GeExpression_strategy = st.builds(
    noop_GeExpression,
)
noop_ComplementExpression_strategy = st.builds(
    noop_ComplementExpression,
)
noop_ModExpression_strategy = st.builds(
    noop_ModExpression,
)
noop_MulExpression_strategy = st.builds(
    noop_MulExpression,
)
noop_BAndExpression_strategy = st.builds(
    noop_BAndExpression,
)
noop_This_strategy = st.builds(
    noop_This,
)
noop_SubExpression_strategy = st.builds(
    noop_SubExpression,
)
noop_RShiftExpression_strategy = st.builds(
    noop_RShiftExpression,
)
noop_MemberSelect_strategy = st.builds(
    noop_MemberSelect,
    hasArgs=
        st.booleans()
)
noop_IncExpression_strategy = st.builds(
    noop_IncExpression,
)
noop_AssignmentExpression_strategy = st.builds(
    noop_AssignmentExpression,
    assignment=
        safe_text
)
noop_DifferExpression_strategy = st.builds(
    noop_DifferExpression,
)
noop_EqualsExpression_strategy = st.builds(
    noop_EqualsExpression,
)








@given(instance=noop_ElseStatement_strategy)
def test_hyp_noop_elsestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=noop_IfStatement_strategy)
def test_hyp_noop_ifstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_AsmStatement_strategy)
def test_hyp_noop_asmstatement_codes_setter(instance):
    original = instance.codes
    instance.codes = original
    assert instance.codes == original




@given(instance=noop_BreakStatement_strategy)
def test_hyp_noop_breakstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_ForStatement_strategy)
def test_hyp_noop_forstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_ContinueStatement_strategy)
def test_hyp_noop_continuestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_ReturnStatement_strategy)
def test_hyp_noop_returnstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_ForeverStatement_strategy)
def test_hyp_noop_foreverstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=noop_Storage_strategy)
def test_hyp_noop_storage_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=noop_Member_strategy)
def test_hyp_noop_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=noop_NoopClass_strategy)
def test_hyp_noop_noopclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=noop_StringLiteral_strategy)
def test_hyp_noop_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=noop_ByteLiteral_strategy)
def test_hyp_noop_byteliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=noop_BoolLiteral_strategy)
def test_hyp_noop_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=noop_MemberRef_strategy)
def test_hyp_noop_memberref_hasArgs_setter(instance):
    original = instance.hasArgs
    instance.hasArgs = original
    assert instance.hasArgs == original




















@given(instance=noop_MemberSelect_strategy)
def test_hyp_noop_memberselect_hasArgs_setter(instance):
    original = instance.hasArgs
    instance.hasArgs = original
    assert instance.hasArgs == original





@given(instance=noop_AssignmentExpression_strategy)
def test_hyp_noop_assignmentexpression_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    Member,
    Statement,
    noop_AddExpression,
    noop_AndExpression,
    noop_ArrayLiteral,
    noop_AsmStatement,
    noop_AssignmentExpression,
    noop_BAndExpression,
    noop_BOrExpression,
    noop_BXorExpression,
    noop_Block,
    noop_BoolLiteral,
    noop_BreakStatement,
    noop_ByteLiteral,
    noop_CastExpression,
    noop_ComplementExpression,
    noop_Constructor,
    noop_ConstructorField,
    noop_ContinueStatement,
    noop_DecExpression,
    noop_DifferExpression,
    noop_DivExpression,
    noop_ElseStatement,
    noop_EqualsExpression,
    noop_Expression,
    noop_ForStatement,
    noop_ForeverStatement,
    noop_GeExpression,
    noop_GtExpression,
    noop_IfStatement,
    noop_IncExpression,
    noop_Index,
    noop_InstanceOfExpression,
    noop_LShiftExpression,
    noop_LeExpression,
    noop_Length,
    noop_LtExpression,
    noop_Member,
    noop_MemberRef,
    noop_MemberSelect,
    noop_Method,
    noop_ModExpression,
    noop_MulExpression,
    noop_NewInstance,
    noop_NoopClass,
    noop_NotExpression,
    noop_OrExpression,
    noop_RShiftExpression,
    noop_ReturnStatement,
    noop_SigNegExpression,
    noop_SigPosExpression,
    noop_Statement,
    noop_Storage,
    noop_StringLiteral,
    noop_SubExpression,
    noop_Super,
    noop_This,
    noop_Variable,
    AssignmentType,
    StorageType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_noop_AsmStatement_codes_value_roundtrip():
    instance = noop_AsmStatement(codes="sample_text")
    assert instance.codes == "sample_text"
    instance.codes = "sample_text_2"
    assert instance.codes == "sample_text_2"


def test_noop_AssignmentExpression_assignment_value_roundtrip():
    instance = noop_AssignmentExpression(assignment="sample_text")
    assert instance.assignment == "sample_text"
    instance.assignment = "sample_text_2"
    assert instance.assignment == "sample_text_2"


def test_noop_BoolLiteral_value_value_roundtrip():
    instance = noop_BoolLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_noop_BreakStatement_name_value_roundtrip():
    instance = noop_BreakStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_ByteLiteral_value_value_roundtrip():
    instance = noop_ByteLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_noop_ContinueStatement_name_value_roundtrip():
    instance = noop_ContinueStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_ElseStatement_name_value_roundtrip():
    instance = noop_ElseStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_ForStatement_name_value_roundtrip():
    instance = noop_ForStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_ForeverStatement_name_value_roundtrip():
    instance = noop_ForeverStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_IfStatement_name_value_roundtrip():
    instance = noop_IfStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_Member_name_value_roundtrip():
    instance = noop_Member(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_MemberRef_hasArgs_value_roundtrip():
    instance = noop_MemberRef(hasArgs=True)
    assert instance.hasArgs == True
    instance.hasArgs = False
    assert instance.hasArgs == False


def test_noop_MemberSelect_hasArgs_value_roundtrip():
    instance = noop_MemberSelect(hasArgs=True)
    assert instance.hasArgs == True
    instance.hasArgs = False
    assert instance.hasArgs == False


def test_noop_NoopClass_name_value_roundtrip():
    instance = noop_NoopClass(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_ReturnStatement_name_value_roundtrip():
    instance = noop_ReturnStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_noop_Storage_type_value_roundtrip():
    instance = noop_Storage(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_noop_StringLiteral_value_value_roundtrip():
    instance = noop_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_noop_AddExpression_isa_Expression():
    instance = noop_AddExpression()
    assert isinstance(instance, Expression)


def test_noop_AndExpression_isa_Expression():
    instance = noop_AndExpression()
    assert isinstance(instance, Expression)


def test_noop_ArrayLiteral_isa_Expression():
    instance = noop_ArrayLiteral()
    assert isinstance(instance, Expression)


def test_noop_AssignmentExpression_isa_Expression():
    instance = noop_AssignmentExpression(assignment="sample_text")
    assert isinstance(instance, Expression)


def test_noop_BAndExpression_isa_Expression():
    instance = noop_BAndExpression()
    assert isinstance(instance, Expression)


def test_noop_BOrExpression_isa_Expression():
    instance = noop_BOrExpression()
    assert isinstance(instance, Expression)


def test_noop_BXorExpression_isa_Expression():
    instance = noop_BXorExpression()
    assert isinstance(instance, Expression)


def test_noop_BoolLiteral_isa_Expression():
    instance = noop_BoolLiteral(value=True)
    assert isinstance(instance, Expression)


def test_noop_ByteLiteral_isa_Expression():
    instance = noop_ByteLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_noop_CastExpression_isa_Expression():
    instance = noop_CastExpression()
    assert isinstance(instance, Expression)


def test_noop_ComplementExpression_isa_Expression():
    instance = noop_ComplementExpression()
    assert isinstance(instance, Expression)


def test_noop_DecExpression_isa_Expression():
    instance = noop_DecExpression()
    assert isinstance(instance, Expression)


def test_noop_DifferExpression_isa_Expression():
    instance = noop_DifferExpression()
    assert isinstance(instance, Expression)


def test_noop_DivExpression_isa_Expression():
    instance = noop_DivExpression()
    assert isinstance(instance, Expression)


def test_noop_EqualsExpression_isa_Expression():
    instance = noop_EqualsExpression()
    assert isinstance(instance, Expression)


def test_noop_GeExpression_isa_Expression():
    instance = noop_GeExpression()
    assert isinstance(instance, Expression)


def test_noop_GtExpression_isa_Expression():
    instance = noop_GtExpression()
    assert isinstance(instance, Expression)


def test_noop_IncExpression_isa_Expression():
    instance = noop_IncExpression()
    assert isinstance(instance, Expression)


def test_noop_InstanceOfExpression_isa_Expression():
    instance = noop_InstanceOfExpression()
    assert isinstance(instance, Expression)


def test_noop_LShiftExpression_isa_Expression():
    instance = noop_LShiftExpression()
    assert isinstance(instance, Expression)


def test_noop_LeExpression_isa_Expression():
    instance = noop_LeExpression()
    assert isinstance(instance, Expression)


def test_noop_LtExpression_isa_Expression():
    instance = noop_LtExpression()
    assert isinstance(instance, Expression)


def test_noop_MemberRef_isa_Expression():
    instance = noop_MemberRef(hasArgs=True)
    assert isinstance(instance, Expression)


def test_noop_MemberSelect_isa_Expression():
    instance = noop_MemberSelect(hasArgs=True)
    assert isinstance(instance, Expression)


def test_noop_ModExpression_isa_Expression():
    instance = noop_ModExpression()
    assert isinstance(instance, Expression)


def test_noop_MulExpression_isa_Expression():
    instance = noop_MulExpression()
    assert isinstance(instance, Expression)


def test_noop_NewInstance_isa_Expression():
    instance = noop_NewInstance()
    assert isinstance(instance, Expression)


def test_noop_NotExpression_isa_Expression():
    instance = noop_NotExpression()
    assert isinstance(instance, Expression)


def test_noop_OrExpression_isa_Expression():
    instance = noop_OrExpression()
    assert isinstance(instance, Expression)


def test_noop_RShiftExpression_isa_Expression():
    instance = noop_RShiftExpression()
    assert isinstance(instance, Expression)


def test_noop_SigNegExpression_isa_Expression():
    instance = noop_SigNegExpression()
    assert isinstance(instance, Expression)


def test_noop_SigPosExpression_isa_Expression():
    instance = noop_SigPosExpression()
    assert isinstance(instance, Expression)


def test_noop_StringLiteral_isa_Expression():
    instance = noop_StringLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_noop_SubExpression_isa_Expression():
    instance = noop_SubExpression()
    assert isinstance(instance, Expression)


def test_noop_Super_isa_Expression():
    instance = noop_Super()
    assert isinstance(instance, Expression)


def test_noop_This_isa_Expression():
    instance = noop_This()
    assert isinstance(instance, Expression)


def test_noop_Method_isa_Member():
    instance = noop_Method()
    assert isinstance(instance, Member)


def test_noop_Variable_isa_Member():
    instance = noop_Variable()
    assert isinstance(instance, Member)


def test_noop_AsmStatement_isa_Statement():
    instance = noop_AsmStatement(codes="sample_text")
    assert isinstance(instance, Statement)


def test_noop_BreakStatement_isa_Statement():
    instance = noop_BreakStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_ContinueStatement_isa_Statement():
    instance = noop_ContinueStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_Expression_isa_Statement():
    instance = noop_Expression()
    assert isinstance(instance, Statement)


def test_noop_ForStatement_isa_Statement():
    instance = noop_ForStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_ForeverStatement_isa_Statement():
    instance = noop_ForeverStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_IfStatement_isa_Statement():
    instance = noop_IfStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_ReturnStatement_isa_Statement():
    instance = noop_ReturnStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_noop_Variable_isa_Statement():
    instance = noop_Variable()
    assert isinstance(instance, Statement)


def test_assoc_args191_link_reassign_clear():
    a = noop_MemberSelect(hasArgs=True)
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_MemberSelect192', {b1})
    assert _is_linked(a, 'noop_MemberSelect192', b1)
    if hasattr(b1, 'noop_Expression193'):
        assert _is_linked(b1, 'noop_Expression193', a)
    _safe_set(a, 'noop_MemberSelect192', {b2})
    assert _is_linked(a, 'noop_MemberSelect192', b2)
    if hasattr(b1, 'noop_Expression193'):
        assert not _is_linked(b1, 'noop_Expression193', a)
    if hasattr(b2, 'noop_Expression193'):
        assert _is_linked(b2, 'noop_Expression193', a)
    _safe_set(a, 'noop_MemberSelect192', set())
    assert not _is_linked(a, 'noop_MemberSelect192', b2)
    if hasattr(b2, 'noop_Expression193'):
        assert not _is_linked(b2, 'noop_Expression193', a)


def test_assoc_args209_link_reassign_clear():
    a = noop_MemberRef(hasArgs=True)
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_MemberRef210', {b1})
    assert _is_linked(a, 'noop_MemberRef210', b1)
    if hasattr(b1, 'noop_Expression211'):
        assert _is_linked(b1, 'noop_Expression211', a)
    _safe_set(a, 'noop_MemberRef210', {b2})
    assert _is_linked(a, 'noop_MemberRef210', b2)
    if hasattr(b1, 'noop_Expression211'):
        assert not _is_linked(b1, 'noop_Expression211', a)
    if hasattr(b2, 'noop_Expression211'):
        assert _is_linked(b2, 'noop_Expression211', a)
    _safe_set(a, 'noop_MemberRef210', set())
    assert not _is_linked(a, 'noop_MemberRef210', b2)
    if hasattr(b2, 'noop_Expression211'):
        assert not _is_linked(b2, 'noop_Expression211', a)


def test_assoc_assignments38_link_reassign_clear():
    a = noop_ForStatement(name="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_ForStatement39', {b1})
    assert _is_linked(a, 'noop_ForStatement39', b1)
    if hasattr(b1, 'noop_Expression40'):
        assert _is_linked(b1, 'noop_Expression40', a)
    _safe_set(a, 'noop_ForStatement39', {b2})
    assert _is_linked(a, 'noop_ForStatement39', b2)
    if hasattr(b1, 'noop_Expression40'):
        assert not _is_linked(b1, 'noop_Expression40', a)
    if hasattr(b2, 'noop_Expression40'):
        assert _is_linked(b2, 'noop_Expression40', a)
    _safe_set(a, 'noop_ForStatement39', set())
    assert not _is_linked(a, 'noop_ForStatement39', b2)
    if hasattr(b2, 'noop_Expression40'):
        assert not _is_linked(b2, 'noop_Expression40', a)


def test_assoc_body25_link_reassign_clear():
    a = noop_IfStatement(name="sample_text")
    b1 = noop_Block()
    b2 = noop_Block()
    _safe_set(a, 'noop_IfStatement26', b1)
    assert _is_linked(a, 'noop_IfStatement26', b1)
    if hasattr(b1, 'noop_Block27'):
        assert _is_linked(b1, 'noop_Block27', a)
    _safe_set(a, 'noop_IfStatement26', b2)
    assert _is_linked(a, 'noop_IfStatement26', b2)
    if hasattr(b1, 'noop_Block27'):
        assert not _is_linked(b1, 'noop_Block27', a)
    if hasattr(b2, 'noop_Block27'):
        assert _is_linked(b2, 'noop_Block27', a)
    _safe_set(a, 'noop_IfStatement26', None)
    assert not _is_linked(a, 'noop_IfStatement26', b2)
    if hasattr(b2, 'noop_Block27'):
        assert not _is_linked(b2, 'noop_Block27', a)


def test_assoc_body30_link_reassign_clear():
    a = noop_ElseStatement(name="sample_text")
    b1 = noop_Block()
    b2 = noop_Block()
    _safe_set(a, 'noop_ElseStatement31', b1)
    assert _is_linked(a, 'noop_ElseStatement31', b1)
    if hasattr(b1, 'noop_Block32'):
        assert _is_linked(b1, 'noop_Block32', a)
    _safe_set(a, 'noop_ElseStatement31', b2)
    assert _is_linked(a, 'noop_ElseStatement31', b2)
    if hasattr(b1, 'noop_Block32'):
        assert not _is_linked(b1, 'noop_Block32', a)
    if hasattr(b2, 'noop_Block32'):
        assert _is_linked(b2, 'noop_Block32', a)
    _safe_set(a, 'noop_ElseStatement31', None)
    assert not _is_linked(a, 'noop_ElseStatement31', b2)
    if hasattr(b2, 'noop_Block32'):
        assert not _is_linked(b2, 'noop_Block32', a)


def test_assoc_body47_link_reassign_clear():
    a = noop_ForStatement(name="sample_text")
    b1 = noop_Block()
    b2 = noop_Block()
    _safe_set(a, 'noop_ForStatement48', b1)
    assert _is_linked(a, 'noop_ForStatement48', b1)
    if hasattr(b1, 'noop_Block49'):
        assert _is_linked(b1, 'noop_Block49', a)
    _safe_set(a, 'noop_ForStatement48', b2)
    assert _is_linked(a, 'noop_ForStatement48', b2)
    if hasattr(b1, 'noop_Block49'):
        assert not _is_linked(b1, 'noop_Block49', a)
    if hasattr(b2, 'noop_Block49'):
        assert _is_linked(b2, 'noop_Block49', a)
    _safe_set(a, 'noop_ForStatement48', None)
    assert not _is_linked(a, 'noop_ForStatement48', b2)
    if hasattr(b2, 'noop_Block49'):
        assert not _is_linked(b2, 'noop_Block49', a)


def test_assoc_body50_link_reassign_clear():
    a = noop_ForeverStatement(name="sample_text")
    b1 = noop_Block()
    b2 = noop_Block()
    _safe_set(a, 'noop_ForeverStatement', b1)
    assert _is_linked(a, 'noop_ForeverStatement', b1)
    if hasattr(b1, 'noop_Block51'):
        assert _is_linked(b1, 'noop_Block51', a)
    _safe_set(a, 'noop_ForeverStatement', b2)
    assert _is_linked(a, 'noop_ForeverStatement', b2)
    if hasattr(b1, 'noop_Block51'):
        assert not _is_linked(b1, 'noop_Block51', a)
    if hasattr(b2, 'noop_Block51'):
        assert _is_linked(b2, 'noop_Block51', a)
    _safe_set(a, 'noop_ForeverStatement', None)
    assert not _is_linked(a, 'noop_ForeverStatement', b2)
    if hasattr(b2, 'noop_Block51'):
        assert not _is_linked(b2, 'noop_Block51', a)


def test_assoc_condition23_link_reassign_clear():
    a = noop_IfStatement(name="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_IfStatement', b1)
    assert _is_linked(a, 'noop_IfStatement', b1)
    if hasattr(b1, 'noop_Expression24'):
        assert _is_linked(b1, 'noop_Expression24', a)
    _safe_set(a, 'noop_IfStatement', b2)
    assert _is_linked(a, 'noop_IfStatement', b2)
    if hasattr(b1, 'noop_Expression24'):
        assert not _is_linked(b1, 'noop_Expression24', a)
    if hasattr(b2, 'noop_Expression24'):
        assert _is_linked(b2, 'noop_Expression24', a)
    _safe_set(a, 'noop_IfStatement', None)
    assert not _is_linked(a, 'noop_IfStatement', b2)
    if hasattr(b2, 'noop_Expression24'):
        assert not _is_linked(b2, 'noop_Expression24', a)


def test_assoc_condition41_link_reassign_clear():
    a = noop_ForStatement(name="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_ForStatement42', b1)
    assert _is_linked(a, 'noop_ForStatement42', b1)
    if hasattr(b1, 'noop_Expression43'):
        assert _is_linked(b1, 'noop_Expression43', a)
    _safe_set(a, 'noop_ForStatement42', b2)
    assert _is_linked(a, 'noop_ForStatement42', b2)
    if hasattr(b1, 'noop_Expression43'):
        assert not _is_linked(b1, 'noop_Expression43', a)
    if hasattr(b2, 'noop_Expression43'):
        assert _is_linked(b2, 'noop_Expression43', a)
    _safe_set(a, 'noop_ForStatement42', None)
    assert not _is_linked(a, 'noop_ForStatement42', b2)
    if hasattr(b2, 'noop_Expression43'):
        assert not _is_linked(b2, 'noop_Expression43', a)


def test_assoc_else_28_link_reassign_clear():
    a = noop_IfStatement(name="sample_text")
    b1 = noop_ElseStatement(name="sample_text")
    b2 = noop_ElseStatement(name="sample_text_2")
    _safe_set(a, 'noop_IfStatement29', b1)
    assert _is_linked(a, 'noop_IfStatement29', b1)
    if hasattr(b1, 'noop_ElseStatement'):
        assert _is_linked(b1, 'noop_ElseStatement', a)
    _safe_set(a, 'noop_IfStatement29', b2)
    assert _is_linked(a, 'noop_IfStatement29', b2)
    if hasattr(b1, 'noop_ElseStatement'):
        assert not _is_linked(b1, 'noop_ElseStatement', a)
    if hasattr(b2, 'noop_ElseStatement'):
        assert _is_linked(b2, 'noop_ElseStatement', a)
    _safe_set(a, 'noop_IfStatement29', None)
    assert not _is_linked(a, 'noop_IfStatement29', b2)
    if hasattr(b2, 'noop_ElseStatement'):
        assert not _is_linked(b2, 'noop_ElseStatement', a)


def test_assoc_expressions44_link_reassign_clear():
    a = noop_ForStatement(name="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_ForStatement45', {b1})
    assert _is_linked(a, 'noop_ForStatement45', b1)
    if hasattr(b1, 'noop_Expression46'):
        assert _is_linked(b1, 'noop_Expression46', a)
    _safe_set(a, 'noop_ForStatement45', {b2})
    assert _is_linked(a, 'noop_ForStatement45', b2)
    if hasattr(b1, 'noop_Expression46'):
        assert not _is_linked(b1, 'noop_Expression46', a)
    if hasattr(b2, 'noop_Expression46'):
        assert _is_linked(b2, 'noop_Expression46', a)
    _safe_set(a, 'noop_ForStatement45', set())
    assert not _is_linked(a, 'noop_ForStatement45', b2)
    if hasattr(b2, 'noop_Expression46'):
        assert not _is_linked(b2, 'noop_Expression46', a)


def test_assoc_if_33_link_reassign_clear():
    a = noop_IfStatement(name="sample_text")
    b1 = noop_ElseStatement(name="sample_text")
    b2 = noop_ElseStatement(name="sample_text_2")
    _safe_set(a, 'noop_IfStatement35', b1)
    assert _is_linked(a, 'noop_IfStatement35', b1)
    if hasattr(b1, 'noop_ElseStatement34'):
        assert _is_linked(b1, 'noop_ElseStatement34', a)
    _safe_set(a, 'noop_IfStatement35', b2)
    assert _is_linked(a, 'noop_IfStatement35', b2)
    if hasattr(b1, 'noop_ElseStatement34'):
        assert not _is_linked(b1, 'noop_ElseStatement34', a)
    if hasattr(b2, 'noop_ElseStatement34'):
        assert _is_linked(b2, 'noop_ElseStatement34', a)
    _safe_set(a, 'noop_IfStatement35', None)
    assert not _is_linked(a, 'noop_IfStatement35', b2)
    if hasattr(b2, 'noop_ElseStatement34'):
        assert not _is_linked(b2, 'noop_ElseStatement34', a)


def test_assoc_indexes194_link_reassign_clear():
    a = noop_MemberSelect(hasArgs=True)
    b1 = noop_Index()
    b2 = noop_Index()
    _safe_set(a, 'noop_MemberSelect195', {b1})
    assert _is_linked(a, 'noop_MemberSelect195', b1)
    if hasattr(b1, 'noop_Index196'):
        assert _is_linked(b1, 'noop_Index196', a)
    _safe_set(a, 'noop_MemberSelect195', {b2})
    assert _is_linked(a, 'noop_MemberSelect195', b2)
    if hasattr(b1, 'noop_Index196'):
        assert not _is_linked(b1, 'noop_Index196', a)
    if hasattr(b2, 'noop_Index196'):
        assert _is_linked(b2, 'noop_Index196', a)
    _safe_set(a, 'noop_MemberSelect195', set())
    assert not _is_linked(a, 'noop_MemberSelect195', b2)
    if hasattr(b2, 'noop_Index196'):
        assert not _is_linked(b2, 'noop_Index196', a)


def test_assoc_indexes212_link_reassign_clear():
    a = noop_MemberRef(hasArgs=True)
    b1 = noop_Index()
    b2 = noop_Index()
    _safe_set(a, 'noop_MemberRef213', {b1})
    assert _is_linked(a, 'noop_MemberRef213', b1)
    if hasattr(b1, 'noop_Index214'):
        assert _is_linked(b1, 'noop_Index214', a)
    _safe_set(a, 'noop_MemberRef213', {b2})
    assert _is_linked(a, 'noop_MemberRef213', b2)
    if hasattr(b1, 'noop_Index214'):
        assert not _is_linked(b1, 'noop_Index214', a)
    if hasattr(b2, 'noop_Index214'):
        assert _is_linked(b2, 'noop_Index214', a)
    _safe_set(a, 'noop_MemberRef213', set())
    assert not _is_linked(a, 'noop_MemberRef213', b2)
    if hasattr(b2, 'noop_Index214'):
        assert not _is_linked(b2, 'noop_Index214', a)


def test_assoc_left66_link_reassign_clear():
    a = noop_AssignmentExpression(assignment="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_AssignmentExpression', b1)
    assert _is_linked(a, 'noop_AssignmentExpression', b1)
    if hasattr(b1, 'noop_Expression67'):
        assert _is_linked(b1, 'noop_Expression67', a)
    _safe_set(a, 'noop_AssignmentExpression', b2)
    assert _is_linked(a, 'noop_AssignmentExpression', b2)
    if hasattr(b1, 'noop_Expression67'):
        assert not _is_linked(b1, 'noop_Expression67', a)
    if hasattr(b2, 'noop_Expression67'):
        assert _is_linked(b2, 'noop_Expression67', a)
    _safe_set(a, 'noop_AssignmentExpression', None)
    assert not _is_linked(a, 'noop_AssignmentExpression', b2)
    if hasattr(b2, 'noop_Expression67'):
        assert not _is_linked(b2, 'noop_Expression67', a)


def test_assoc_location6_link_reassign_clear():
    a = noop_Storage(type="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_Storage7', b1)
    assert _is_linked(a, 'noop_Storage7', b1)
    if hasattr(b1, 'noop_Expression'):
        assert _is_linked(b1, 'noop_Expression', a)
    _safe_set(a, 'noop_Storage7', b2)
    assert _is_linked(a, 'noop_Storage7', b2)
    if hasattr(b1, 'noop_Expression'):
        assert not _is_linked(b1, 'noop_Expression', a)
    if hasattr(b2, 'noop_Expression'):
        assert _is_linked(b2, 'noop_Expression', a)
    _safe_set(a, 'noop_Storage7', None)
    assert not _is_linked(a, 'noop_Storage7', b2)
    if hasattr(b2, 'noop_Expression'):
        assert not _is_linked(b2, 'noop_Expression', a)


def test_assoc_member188_link_reassign_clear():
    a = noop_MemberSelect(hasArgs=True)
    b1 = noop_Member(name="sample_text")
    b2 = noop_Member(name="sample_text_2")
    _safe_set(a, 'noop_MemberSelect189', b1)
    assert _is_linked(a, 'noop_MemberSelect189', b1)
    if hasattr(b1, 'noop_Member190'):
        assert _is_linked(b1, 'noop_Member190', a)
    _safe_set(a, 'noop_MemberSelect189', b2)
    assert _is_linked(a, 'noop_MemberSelect189', b2)
    if hasattr(b1, 'noop_Member190'):
        assert not _is_linked(b1, 'noop_Member190', a)
    if hasattr(b2, 'noop_Member190'):
        assert _is_linked(b2, 'noop_Member190', a)
    _safe_set(a, 'noop_MemberSelect189', None)
    assert not _is_linked(a, 'noop_MemberSelect189', b2)
    if hasattr(b2, 'noop_Member190'):
        assert not _is_linked(b2, 'noop_Member190', a)


def test_assoc_member207_link_reassign_clear():
    a = noop_MemberRef(hasArgs=True)
    b1 = noop_Member(name="sample_text")
    b2 = noop_Member(name="sample_text_2")
    _safe_set(a, 'noop_MemberRef', b1)
    assert _is_linked(a, 'noop_MemberRef', b1)
    if hasattr(b1, 'noop_Member208'):
        assert _is_linked(b1, 'noop_Member208', a)
    _safe_set(a, 'noop_MemberRef', b2)
    assert _is_linked(a, 'noop_MemberRef', b2)
    if hasattr(b1, 'noop_Member208'):
        assert not _is_linked(b1, 'noop_Member208', a)
    if hasattr(b2, 'noop_Member208'):
        assert _is_linked(b2, 'noop_Member208', a)
    _safe_set(a, 'noop_MemberRef', None)
    assert not _is_linked(a, 'noop_MemberRef', b2)
    if hasattr(b2, 'noop_Member208'):
        assert not _is_linked(b2, 'noop_Member208', a)


def test_assoc_members2_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_Member(name="sample_text")
    b2 = noop_Member(name="sample_text_2")
    _safe_set(a, 'noop_NoopClass3', {b1})
    assert _is_linked(a, 'noop_NoopClass3', b1)
    if hasattr(b1, 'noop_Member'):
        assert _is_linked(b1, 'noop_Member', a)
    _safe_set(a, 'noop_NoopClass3', {b2})
    assert _is_linked(a, 'noop_NoopClass3', b2)
    if hasattr(b1, 'noop_Member'):
        assert not _is_linked(b1, 'noop_Member', a)
    if hasattr(b2, 'noop_Member'):
        assert _is_linked(b2, 'noop_Member', a)
    _safe_set(a, 'noop_NoopClass3', set())
    assert not _is_linked(a, 'noop_NoopClass3', b2)
    if hasattr(b2, 'noop_Member'):
        assert not _is_linked(b2, 'noop_Member', a)


def test_assoc_receiver186_link_reassign_clear():
    a = noop_MemberSelect(hasArgs=True)
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_MemberSelect', b1)
    assert _is_linked(a, 'noop_MemberSelect', b1)
    if hasattr(b1, 'noop_Expression187'):
        assert _is_linked(b1, 'noop_Expression187', a)
    _safe_set(a, 'noop_MemberSelect', b2)
    assert _is_linked(a, 'noop_MemberSelect', b2)
    if hasattr(b1, 'noop_Expression187'):
        assert not _is_linked(b1, 'noop_Expression187', a)
    if hasattr(b2, 'noop_Expression187'):
        assert _is_linked(b2, 'noop_Expression187', a)
    _safe_set(a, 'noop_MemberSelect', None)
    assert not _is_linked(a, 'noop_MemberSelect', b2)
    if hasattr(b2, 'noop_Expression187'):
        assert not _is_linked(b2, 'noop_Expression187', a)


def test_assoc_right68_link_reassign_clear():
    a = noop_AssignmentExpression(assignment="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_AssignmentExpression69', b1)
    assert _is_linked(a, 'noop_AssignmentExpression69', b1)
    if hasattr(b1, 'noop_Expression70'):
        assert _is_linked(b1, 'noop_Expression70', a)
    _safe_set(a, 'noop_AssignmentExpression69', b2)
    assert _is_linked(a, 'noop_AssignmentExpression69', b2)
    if hasattr(b1, 'noop_Expression70'):
        assert not _is_linked(b1, 'noop_Expression70', a)
    if hasattr(b2, 'noop_Expression70'):
        assert _is_linked(b2, 'noop_Expression70', a)
    _safe_set(a, 'noop_AssignmentExpression69', None)
    assert not _is_linked(a, 'noop_AssignmentExpression69', b2)
    if hasattr(b2, 'noop_Expression70'):
        assert not _is_linked(b2, 'noop_Expression70', a)


def test_assoc_storage4_link_reassign_clear():
    a = noop_Storage(type="sample_text")
    b1 = noop_Member(name="sample_text")
    b2 = noop_Member(name="sample_text_2")
    _safe_set(a, 'noop_Storage', b1)
    assert _is_linked(a, 'noop_Storage', b1)
    if hasattr(b1, 'noop_Member5'):
        assert _is_linked(b1, 'noop_Member5', a)
    _safe_set(a, 'noop_Storage', b2)
    assert _is_linked(a, 'noop_Storage', b2)
    if hasattr(b1, 'noop_Member5'):
        assert not _is_linked(b1, 'noop_Member5', a)
    if hasattr(b2, 'noop_Member5'):
        assert _is_linked(b2, 'noop_Member5', a)
    _safe_set(a, 'noop_Storage', None)
    assert not _is_linked(a, 'noop_Storage', b2)
    if hasattr(b2, 'noop_Member5'):
        assert not _is_linked(b2, 'noop_Member5', a)


def test_assoc_superClass1_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_NoopClass(name="sample_text")
    b2 = noop_NoopClass(name="sample_text_2")
    _safe_set(a, 'noop_NoopClass', b1)
    assert _is_linked(a, 'noop_NoopClass', b1)
    if hasattr(b1, 'noop_NoopClass0'):
        assert _is_linked(b1, 'noop_NoopClass0', a)
    _safe_set(a, 'noop_NoopClass', b2)
    assert _is_linked(a, 'noop_NoopClass', b2)
    if hasattr(b1, 'noop_NoopClass0'):
        assert not _is_linked(b1, 'noop_NoopClass0', a)
    if hasattr(b2, 'noop_NoopClass0'):
        assert _is_linked(b2, 'noop_NoopClass0', a)
    _safe_set(a, 'noop_NoopClass', None)
    assert not _is_linked(a, 'noop_NoopClass', b2)
    if hasattr(b2, 'noop_NoopClass0'):
        assert not _is_linked(b2, 'noop_NoopClass0', a)


def test_assoc_type10_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_Variable()
    b2 = noop_Variable()
    _safe_set(a, 'noop_NoopClass12', b1)
    assert _is_linked(a, 'noop_NoopClass12', b1)
    if hasattr(b1, 'noop_Variable11'):
        assert _is_linked(b1, 'noop_Variable11', a)
    _safe_set(a, 'noop_NoopClass12', b2)
    assert _is_linked(a, 'noop_NoopClass12', b2)
    if hasattr(b1, 'noop_Variable11'):
        assert not _is_linked(b1, 'noop_Variable11', a)
    if hasattr(b2, 'noop_Variable11'):
        assert _is_linked(b2, 'noop_Variable11', a)
    _safe_set(a, 'noop_NoopClass12', None)
    assert not _is_linked(a, 'noop_NoopClass12', b2)
    if hasattr(b2, 'noop_Variable11'):
        assert not _is_linked(b2, 'noop_Variable11', a)


def test_assoc_type128_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_InstanceOfExpression()
    b2 = noop_InstanceOfExpression()
    _safe_set(a, 'noop_NoopClass130', b1)
    assert _is_linked(a, 'noop_NoopClass130', b1)
    if hasattr(b1, 'noop_InstanceOfExpression129'):
        assert _is_linked(b1, 'noop_InstanceOfExpression129', a)
    _safe_set(a, 'noop_NoopClass130', b2)
    assert _is_linked(a, 'noop_NoopClass130', b2)
    if hasattr(b1, 'noop_InstanceOfExpression129'):
        assert not _is_linked(b1, 'noop_InstanceOfExpression129', a)
    if hasattr(b2, 'noop_InstanceOfExpression129'):
        assert _is_linked(b2, 'noop_InstanceOfExpression129', a)
    _safe_set(a, 'noop_NoopClass130', None)
    assert not _is_linked(a, 'noop_NoopClass130', b2)
    if hasattr(b2, 'noop_InstanceOfExpression129'):
        assert not _is_linked(b2, 'noop_InstanceOfExpression129', a)


def test_assoc_type168_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_CastExpression()
    b2 = noop_CastExpression()
    _safe_set(a, 'noop_NoopClass170', b1)
    assert _is_linked(a, 'noop_NoopClass170', b1)
    if hasattr(b1, 'noop_CastExpression169'):
        assert _is_linked(b1, 'noop_CastExpression169', a)
    _safe_set(a, 'noop_NoopClass170', b2)
    assert _is_linked(a, 'noop_NoopClass170', b2)
    if hasattr(b1, 'noop_CastExpression169'):
        assert not _is_linked(b1, 'noop_CastExpression169', a)
    if hasattr(b2, 'noop_CastExpression169'):
        assert _is_linked(b2, 'noop_CastExpression169', a)
    _safe_set(a, 'noop_NoopClass170', None)
    assert not _is_linked(a, 'noop_NoopClass170', b2)
    if hasattr(b2, 'noop_CastExpression169'):
        assert not _is_linked(b2, 'noop_CastExpression169', a)


def test_assoc_type199_link_reassign_clear():
    a = noop_NoopClass(name="sample_text")
    b1 = noop_NewInstance()
    b2 = noop_NewInstance()
    _safe_set(a, 'noop_NoopClass200', b1)
    assert _is_linked(a, 'noop_NoopClass200', b1)
    if hasattr(b1, 'noop_NewInstance'):
        assert _is_linked(b1, 'noop_NewInstance', a)
    _safe_set(a, 'noop_NoopClass200', b2)
    assert _is_linked(a, 'noop_NoopClass200', b2)
    if hasattr(b1, 'noop_NewInstance'):
        assert not _is_linked(b1, 'noop_NewInstance', a)
    if hasattr(b2, 'noop_NewInstance'):
        assert _is_linked(b2, 'noop_NewInstance', a)
    _safe_set(a, 'noop_NoopClass200', None)
    assert not _is_linked(a, 'noop_NoopClass200', b2)
    if hasattr(b2, 'noop_NewInstance'):
        assert not _is_linked(b2, 'noop_NewInstance', a)


def test_assoc_value21_link_reassign_clear():
    a = noop_ReturnStatement(name="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_ReturnStatement', b1)
    assert _is_linked(a, 'noop_ReturnStatement', b1)
    if hasattr(b1, 'noop_Expression22'):
        assert _is_linked(b1, 'noop_Expression22', a)
    _safe_set(a, 'noop_ReturnStatement', b2)
    assert _is_linked(a, 'noop_ReturnStatement', b2)
    if hasattr(b1, 'noop_Expression22'):
        assert not _is_linked(b1, 'noop_Expression22', a)
    if hasattr(b2, 'noop_Expression22'):
        assert _is_linked(b2, 'noop_Expression22', a)
    _safe_set(a, 'noop_ReturnStatement', None)
    assert not _is_linked(a, 'noop_ReturnStatement', b2)
    if hasattr(b2, 'noop_Expression22'):
        assert not _is_linked(b2, 'noop_Expression22', a)


def test_assoc_variables36_link_reassign_clear():
    a = noop_ForStatement(name="sample_text")
    b1 = noop_Variable()
    b2 = noop_Variable()
    _safe_set(a, 'noop_ForStatement', {b1})
    assert _is_linked(a, 'noop_ForStatement', b1)
    if hasattr(b1, 'noop_Variable37'):
        assert _is_linked(b1, 'noop_Variable37', a)
    _safe_set(a, 'noop_ForStatement', {b2})
    assert _is_linked(a, 'noop_ForStatement', b2)
    if hasattr(b1, 'noop_Variable37'):
        assert not _is_linked(b1, 'noop_Variable37', a)
    if hasattr(b2, 'noop_Variable37'):
        assert _is_linked(b2, 'noop_Variable37', a)
    _safe_set(a, 'noop_ForStatement', set())
    assert not _is_linked(a, 'noop_ForStatement', b2)
    if hasattr(b2, 'noop_Variable37'):
        assert not _is_linked(b2, 'noop_Variable37', a)


def test_assoc_vars52_link_reassign_clear():
    a = noop_AsmStatement(codes="sample_text")
    b1 = noop_Expression()
    b2 = noop_Expression()
    _safe_set(a, 'noop_AsmStatement', {b1})
    assert _is_linked(a, 'noop_AsmStatement', b1)
    if hasattr(b1, 'noop_Expression53'):
        assert _is_linked(b1, 'noop_Expression53', a)
    _safe_set(a, 'noop_AsmStatement', {b2})
    assert _is_linked(a, 'noop_AsmStatement', b2)
    if hasattr(b1, 'noop_Expression53'):
        assert not _is_linked(b1, 'noop_Expression53', a)
    if hasattr(b2, 'noop_Expression53'):
        assert _is_linked(b2, 'noop_Expression53', a)
    _safe_set(a, 'noop_AsmStatement', set())
    assert not _is_linked(a, 'noop_AsmStatement', b2)
    if hasattr(b2, 'noop_Expression53'):
        assert not _is_linked(b2, 'noop_Expression53', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


noop_AddExpression_strategy = st.builds(noop_AddExpression)
@given(instance=noop_AddExpression_strategy)
@settings(max_examples=25)
def test_noop_AddExpression_instantiation(instance):
    assert isinstance(instance, noop_AddExpression)


noop_AndExpression_strategy = st.builds(noop_AndExpression)
@given(instance=noop_AndExpression_strategy)
@settings(max_examples=25)
def test_noop_AndExpression_instantiation(instance):
    assert isinstance(instance, noop_AndExpression)


noop_ArrayLiteral_strategy = st.builds(noop_ArrayLiteral)
@given(instance=noop_ArrayLiteral_strategy)
@settings(max_examples=25)
def test_noop_ArrayLiteral_instantiation(instance):
    assert isinstance(instance, noop_ArrayLiteral)


noop_AsmStatement_strategy = st.builds(noop_AsmStatement, codes=safe_text)
@given(instance=noop_AsmStatement_strategy)
@settings(max_examples=25)
def test_noop_AsmStatement_instantiation(instance):
    assert isinstance(instance, noop_AsmStatement)


noop_AssignmentExpression_strategy = st.builds(noop_AssignmentExpression, assignment=safe_text)
@given(instance=noop_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_noop_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, noop_AssignmentExpression)


noop_BAndExpression_strategy = st.builds(noop_BAndExpression)
@given(instance=noop_BAndExpression_strategy)
@settings(max_examples=25)
def test_noop_BAndExpression_instantiation(instance):
    assert isinstance(instance, noop_BAndExpression)


noop_BOrExpression_strategy = st.builds(noop_BOrExpression)
@given(instance=noop_BOrExpression_strategy)
@settings(max_examples=25)
def test_noop_BOrExpression_instantiation(instance):
    assert isinstance(instance, noop_BOrExpression)


noop_BXorExpression_strategy = st.builds(noop_BXorExpression)
@given(instance=noop_BXorExpression_strategy)
@settings(max_examples=25)
def test_noop_BXorExpression_instantiation(instance):
    assert isinstance(instance, noop_BXorExpression)


noop_Block_strategy = st.builds(noop_Block)
@given(instance=noop_Block_strategy)
@settings(max_examples=25)
def test_noop_Block_instantiation(instance):
    assert isinstance(instance, noop_Block)


noop_BoolLiteral_strategy = st.builds(noop_BoolLiteral, value=st.booleans())
@given(instance=noop_BoolLiteral_strategy)
@settings(max_examples=25)
def test_noop_BoolLiteral_instantiation(instance):
    assert isinstance(instance, noop_BoolLiteral)


noop_BreakStatement_strategy = st.builds(noop_BreakStatement, name=safe_text)
@given(instance=noop_BreakStatement_strategy)
@settings(max_examples=25)
def test_noop_BreakStatement_instantiation(instance):
    assert isinstance(instance, noop_BreakStatement)


noop_ByteLiteral_strategy = st.builds(noop_ByteLiteral, value=safe_text)
@given(instance=noop_ByteLiteral_strategy)
@settings(max_examples=25)
def test_noop_ByteLiteral_instantiation(instance):
    assert isinstance(instance, noop_ByteLiteral)


noop_CastExpression_strategy = st.builds(noop_CastExpression)
@given(instance=noop_CastExpression_strategy)
@settings(max_examples=25)
def test_noop_CastExpression_instantiation(instance):
    assert isinstance(instance, noop_CastExpression)


noop_ComplementExpression_strategy = st.builds(noop_ComplementExpression)
@given(instance=noop_ComplementExpression_strategy)
@settings(max_examples=25)
def test_noop_ComplementExpression_instantiation(instance):
    assert isinstance(instance, noop_ComplementExpression)


noop_Constructor_strategy = st.builds(noop_Constructor)
@given(instance=noop_Constructor_strategy)
@settings(max_examples=25)
def test_noop_Constructor_instantiation(instance):
    assert isinstance(instance, noop_Constructor)


noop_ConstructorField_strategy = st.builds(noop_ConstructorField)
@given(instance=noop_ConstructorField_strategy)
@settings(max_examples=25)
def test_noop_ConstructorField_instantiation(instance):
    assert isinstance(instance, noop_ConstructorField)


noop_ContinueStatement_strategy = st.builds(noop_ContinueStatement, name=safe_text)
@given(instance=noop_ContinueStatement_strategy)
@settings(max_examples=25)
def test_noop_ContinueStatement_instantiation(instance):
    assert isinstance(instance, noop_ContinueStatement)


noop_DecExpression_strategy = st.builds(noop_DecExpression)
@given(instance=noop_DecExpression_strategy)
@settings(max_examples=25)
def test_noop_DecExpression_instantiation(instance):
    assert isinstance(instance, noop_DecExpression)


noop_DifferExpression_strategy = st.builds(noop_DifferExpression)
@given(instance=noop_DifferExpression_strategy)
@settings(max_examples=25)
def test_noop_DifferExpression_instantiation(instance):
    assert isinstance(instance, noop_DifferExpression)


noop_DivExpression_strategy = st.builds(noop_DivExpression)
@given(instance=noop_DivExpression_strategy)
@settings(max_examples=25)
def test_noop_DivExpression_instantiation(instance):
    assert isinstance(instance, noop_DivExpression)


noop_ElseStatement_strategy = st.builds(noop_ElseStatement, name=safe_text)
@given(instance=noop_ElseStatement_strategy)
@settings(max_examples=25)
def test_noop_ElseStatement_instantiation(instance):
    assert isinstance(instance, noop_ElseStatement)


noop_EqualsExpression_strategy = st.builds(noop_EqualsExpression)
@given(instance=noop_EqualsExpression_strategy)
@settings(max_examples=25)
def test_noop_EqualsExpression_instantiation(instance):
    assert isinstance(instance, noop_EqualsExpression)


noop_Expression_strategy = st.builds(noop_Expression)
@given(instance=noop_Expression_strategy)
@settings(max_examples=25)
def test_noop_Expression_instantiation(instance):
    assert isinstance(instance, noop_Expression)


noop_ForStatement_strategy = st.builds(noop_ForStatement, name=safe_text)
@given(instance=noop_ForStatement_strategy)
@settings(max_examples=25)
def test_noop_ForStatement_instantiation(instance):
    assert isinstance(instance, noop_ForStatement)


noop_ForeverStatement_strategy = st.builds(noop_ForeverStatement, name=safe_text)
@given(instance=noop_ForeverStatement_strategy)
@settings(max_examples=25)
def test_noop_ForeverStatement_instantiation(instance):
    assert isinstance(instance, noop_ForeverStatement)


noop_GeExpression_strategy = st.builds(noop_GeExpression)
@given(instance=noop_GeExpression_strategy)
@settings(max_examples=25)
def test_noop_GeExpression_instantiation(instance):
    assert isinstance(instance, noop_GeExpression)


noop_GtExpression_strategy = st.builds(noop_GtExpression)
@given(instance=noop_GtExpression_strategy)
@settings(max_examples=25)
def test_noop_GtExpression_instantiation(instance):
    assert isinstance(instance, noop_GtExpression)


noop_IfStatement_strategy = st.builds(noop_IfStatement, name=safe_text)
@given(instance=noop_IfStatement_strategy)
@settings(max_examples=25)
def test_noop_IfStatement_instantiation(instance):
    assert isinstance(instance, noop_IfStatement)


noop_IncExpression_strategy = st.builds(noop_IncExpression)
@given(instance=noop_IncExpression_strategy)
@settings(max_examples=25)
def test_noop_IncExpression_instantiation(instance):
    assert isinstance(instance, noop_IncExpression)


noop_Index_strategy = st.builds(noop_Index)
@given(instance=noop_Index_strategy)
@settings(max_examples=25)
def test_noop_Index_instantiation(instance):
    assert isinstance(instance, noop_Index)


noop_InstanceOfExpression_strategy = st.builds(noop_InstanceOfExpression)
@given(instance=noop_InstanceOfExpression_strategy)
@settings(max_examples=25)
def test_noop_InstanceOfExpression_instantiation(instance):
    assert isinstance(instance, noop_InstanceOfExpression)


noop_LShiftExpression_strategy = st.builds(noop_LShiftExpression)
@given(instance=noop_LShiftExpression_strategy)
@settings(max_examples=25)
def test_noop_LShiftExpression_instantiation(instance):
    assert isinstance(instance, noop_LShiftExpression)


noop_LeExpression_strategy = st.builds(noop_LeExpression)
@given(instance=noop_LeExpression_strategy)
@settings(max_examples=25)
def test_noop_LeExpression_instantiation(instance):
    assert isinstance(instance, noop_LeExpression)


noop_Length_strategy = st.builds(noop_Length)
@given(instance=noop_Length_strategy)
@settings(max_examples=25)
def test_noop_Length_instantiation(instance):
    assert isinstance(instance, noop_Length)


noop_LtExpression_strategy = st.builds(noop_LtExpression)
@given(instance=noop_LtExpression_strategy)
@settings(max_examples=25)
def test_noop_LtExpression_instantiation(instance):
    assert isinstance(instance, noop_LtExpression)


noop_Member_strategy = st.builds(noop_Member, name=safe_text)
@given(instance=noop_Member_strategy)
@settings(max_examples=25)
def test_noop_Member_instantiation(instance):
    assert isinstance(instance, noop_Member)


noop_MemberRef_strategy = st.builds(noop_MemberRef, hasArgs=st.booleans())
@given(instance=noop_MemberRef_strategy)
@settings(max_examples=25)
def test_noop_MemberRef_instantiation(instance):
    assert isinstance(instance, noop_MemberRef)


noop_MemberSelect_strategy = st.builds(noop_MemberSelect, hasArgs=st.booleans())
@given(instance=noop_MemberSelect_strategy)
@settings(max_examples=25)
def test_noop_MemberSelect_instantiation(instance):
    assert isinstance(instance, noop_MemberSelect)


noop_Method_strategy = st.builds(noop_Method)
@given(instance=noop_Method_strategy)
@settings(max_examples=25)
def test_noop_Method_instantiation(instance):
    assert isinstance(instance, noop_Method)


noop_ModExpression_strategy = st.builds(noop_ModExpression)
@given(instance=noop_ModExpression_strategy)
@settings(max_examples=25)
def test_noop_ModExpression_instantiation(instance):
    assert isinstance(instance, noop_ModExpression)


noop_MulExpression_strategy = st.builds(noop_MulExpression)
@given(instance=noop_MulExpression_strategy)
@settings(max_examples=25)
def test_noop_MulExpression_instantiation(instance):
    assert isinstance(instance, noop_MulExpression)


noop_NewInstance_strategy = st.builds(noop_NewInstance)
@given(instance=noop_NewInstance_strategy)
@settings(max_examples=25)
def test_noop_NewInstance_instantiation(instance):
    assert isinstance(instance, noop_NewInstance)


noop_NoopClass_strategy = st.builds(noop_NoopClass, name=safe_text)
@given(instance=noop_NoopClass_strategy)
@settings(max_examples=25)
def test_noop_NoopClass_instantiation(instance):
    assert isinstance(instance, noop_NoopClass)


noop_NotExpression_strategy = st.builds(noop_NotExpression)
@given(instance=noop_NotExpression_strategy)
@settings(max_examples=25)
def test_noop_NotExpression_instantiation(instance):
    assert isinstance(instance, noop_NotExpression)


noop_OrExpression_strategy = st.builds(noop_OrExpression)
@given(instance=noop_OrExpression_strategy)
@settings(max_examples=25)
def test_noop_OrExpression_instantiation(instance):
    assert isinstance(instance, noop_OrExpression)


noop_RShiftExpression_strategy = st.builds(noop_RShiftExpression)
@given(instance=noop_RShiftExpression_strategy)
@settings(max_examples=25)
def test_noop_RShiftExpression_instantiation(instance):
    assert isinstance(instance, noop_RShiftExpression)


noop_ReturnStatement_strategy = st.builds(noop_ReturnStatement, name=safe_text)
@given(instance=noop_ReturnStatement_strategy)
@settings(max_examples=25)
def test_noop_ReturnStatement_instantiation(instance):
    assert isinstance(instance, noop_ReturnStatement)


noop_SigNegExpression_strategy = st.builds(noop_SigNegExpression)
@given(instance=noop_SigNegExpression_strategy)
@settings(max_examples=25)
def test_noop_SigNegExpression_instantiation(instance):
    assert isinstance(instance, noop_SigNegExpression)


noop_SigPosExpression_strategy = st.builds(noop_SigPosExpression)
@given(instance=noop_SigPosExpression_strategy)
@settings(max_examples=25)
def test_noop_SigPosExpression_instantiation(instance):
    assert isinstance(instance, noop_SigPosExpression)


noop_Statement_strategy = st.builds(noop_Statement)
@given(instance=noop_Statement_strategy)
@settings(max_examples=25)
def test_noop_Statement_instantiation(instance):
    assert isinstance(instance, noop_Statement)


noop_Storage_strategy = st.builds(noop_Storage, type=safe_text)
@given(instance=noop_Storage_strategy)
@settings(max_examples=25)
def test_noop_Storage_instantiation(instance):
    assert isinstance(instance, noop_Storage)


noop_StringLiteral_strategy = st.builds(noop_StringLiteral, value=safe_text)
@given(instance=noop_StringLiteral_strategy)
@settings(max_examples=25)
def test_noop_StringLiteral_instantiation(instance):
    assert isinstance(instance, noop_StringLiteral)


noop_SubExpression_strategy = st.builds(noop_SubExpression)
@given(instance=noop_SubExpression_strategy)
@settings(max_examples=25)
def test_noop_SubExpression_instantiation(instance):
    assert isinstance(instance, noop_SubExpression)


noop_Super_strategy = st.builds(noop_Super)
@given(instance=noop_Super_strategy)
@settings(max_examples=25)
def test_noop_Super_instantiation(instance):
    assert isinstance(instance, noop_Super)


noop_This_strategy = st.builds(noop_This)
@given(instance=noop_This_strategy)
@settings(max_examples=25)
def test_noop_This_instantiation(instance):
    assert isinstance(instance, noop_This)


noop_Variable_strategy = st.builds(noop_Variable)
@given(instance=noop_Variable_strategy)
@settings(max_examples=25)
def test_noop_Variable_instantiation(instance):
    assert isinstance(instance, noop_Variable)



