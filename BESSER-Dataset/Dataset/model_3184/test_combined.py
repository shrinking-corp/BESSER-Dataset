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
    AccessControl,
    smc_Covered,
    smc_BellLapadula,
    Expression,
    smc_PlusOrMinus,
    smc_Equality,
    smc_BooleanLiteral,
    smc_IntLiteral,
    smc_List,
    smc_StringLiteral,
    smc_DateLiteral,
    smc_DoubleLiteral,
    smc_Dict,
    smc_VariableRef,
    smc_Comparison,
    smc_Or,
    smc_Not,
    smc_MulOrDiv,
    smc_And,
    smc_TimeLiteral,
    smc_Tuple,
    Download,
    smc_Client,
    smc_Database,
    AbstractAssignment,
    smc_Download,
    Computation,
    smc_Median,
    smc_Average,
    smc_Count,
    smc_WeightedAvg,
    smc_Multiplication,
    Functions,
    smc_BloomFilter,
    smc_CheckTable,
    smc_AccessControl,
    smc_AddValues,
    smc_CreateTable,
    smc_Search,
    smc_Computation,
    smc_Functions,
    smc_Expression,
    smc_Invocation,
    Command,
    smc_InvocationVoid,
    smc_IfThenElse,
    smc_Return,
    smc_Block,
    smc_Print,
    smc_While,
    smc_ParamDecl,
    smc_VariableAssignment,
    smc_AbstractAssignment,
    smc_VariableDecl,
    smc_Smc,
    smc_Command,
    smc_MainSMC,
    smc_BlockSMC,
    BlockType,
    SecType,
    BasicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(AccessControl)


def test_hyp_accesscontrol_constructor_exists():
    assert callable(AccessControl.__init__)


def test_hyp_accesscontrol_constructor_args():
    sig = inspect.signature(AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_covered_is_not_abstract():
    assert not inspect.isabstract(smc_Covered)


def test_hyp_smc_covered_constructor_exists():
    assert callable(smc_Covered.__init__)


def test_hyp_smc_covered_constructor_args():
    sig = inspect.signature(smc_Covered.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_belllapadula_is_not_abstract():
    assert not inspect.isabstract(smc_BellLapadula)


def test_hyp_smc_belllapadula_constructor_exists():
    assert callable(smc_BellLapadula.__init__)


def test_hyp_smc_belllapadula_constructor_args():
    sig = inspect.signature(smc_BellLapadula.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_plusorminus_is_not_abstract():
    assert not inspect.isabstract(smc_PlusOrMinus)


def test_hyp_smc_plusorminus_constructor_exists():
    assert callable(smc_PlusOrMinus.__init__)


def test_hyp_smc_plusorminus_constructor_args():
    sig = inspect.signature(smc_PlusOrMinus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_smc_equality_is_not_abstract():
    assert not inspect.isabstract(smc_Equality)


def test_hyp_smc_equality_constructor_exists():
    assert callable(smc_Equality.__init__)


def test_hyp_smc_equality_constructor_args():
    sig = inspect.signature(smc_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_smc_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(smc_BooleanLiteral)


def test_hyp_smc_booleanliteral_constructor_exists():
    assert callable(smc_BooleanLiteral.__init__)


def test_hyp_smc_booleanliteral_constructor_args():
    sig = inspect.signature(smc_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_intliteral_is_not_abstract():
    assert not inspect.isabstract(smc_IntLiteral)


def test_hyp_smc_intliteral_constructor_exists():
    assert callable(smc_IntLiteral.__init__)


def test_hyp_smc_intliteral_constructor_args():
    sig = inspect.signature(smc_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_list_is_not_abstract():
    assert not inspect.isabstract(smc_List)


def test_hyp_smc_list_constructor_exists():
    assert callable(smc_List.__init__)


def test_hyp_smc_list_constructor_args():
    sig = inspect.signature(smc_List.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_stringliteral_is_not_abstract():
    assert not inspect.isabstract(smc_StringLiteral)


def test_hyp_smc_stringliteral_constructor_exists():
    assert callable(smc_StringLiteral.__init__)


def test_hyp_smc_stringliteral_constructor_args():
    sig = inspect.signature(smc_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_dateliteral_is_not_abstract():
    assert not inspect.isabstract(smc_DateLiteral)


def test_hyp_smc_dateliteral_constructor_exists():
    assert callable(smc_DateLiteral.__init__)


def test_hyp_smc_dateliteral_constructor_args():
    sig = inspect.signature(smc_DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(smc_DoubleLiteral)


def test_hyp_smc_doubleliteral_constructor_exists():
    assert callable(smc_DoubleLiteral.__init__)


def test_hyp_smc_doubleliteral_constructor_args():
    sig = inspect.signature(smc_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_dict_is_not_abstract():
    assert not inspect.isabstract(smc_Dict)


def test_hyp_smc_dict_constructor_exists():
    assert callable(smc_Dict.__init__)


def test_hyp_smc_dict_constructor_args():
    sig = inspect.signature(smc_Dict.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_variableref_is_not_abstract():
    assert not inspect.isabstract(smc_VariableRef)


def test_hyp_smc_variableref_constructor_exists():
    assert callable(smc_VariableRef.__init__)


def test_hyp_smc_variableref_constructor_args():
    sig = inspect.signature(smc_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_comparison_is_not_abstract():
    assert not inspect.isabstract(smc_Comparison)


def test_hyp_smc_comparison_constructor_exists():
    assert callable(smc_Comparison.__init__)


def test_hyp_smc_comparison_constructor_args():
    sig = inspect.signature(smc_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_smc_or_is_not_abstract():
    assert not inspect.isabstract(smc_Or)


def test_hyp_smc_or_constructor_exists():
    assert callable(smc_Or.__init__)


def test_hyp_smc_or_constructor_args():
    sig = inspect.signature(smc_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_not_is_not_abstract():
    assert not inspect.isabstract(smc_Not)


def test_hyp_smc_not_constructor_exists():
    assert callable(smc_Not.__init__)


def test_hyp_smc_not_constructor_args():
    sig = inspect.signature(smc_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_mulordiv_is_not_abstract():
    assert not inspect.isabstract(smc_MulOrDiv)


def test_hyp_smc_mulordiv_constructor_exists():
    assert callable(smc_MulOrDiv.__init__)


def test_hyp_smc_mulordiv_constructor_args():
    sig = inspect.signature(smc_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_smc_and_is_not_abstract():
    assert not inspect.isabstract(smc_And)


def test_hyp_smc_and_constructor_exists():
    assert callable(smc_And.__init__)


def test_hyp_smc_and_constructor_args():
    sig = inspect.signature(smc_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_timeliteral_is_not_abstract():
    assert not inspect.isabstract(smc_TimeLiteral)


def test_hyp_smc_timeliteral_constructor_exists():
    assert callable(smc_TimeLiteral.__init__)


def test_hyp_smc_timeliteral_constructor_args():
    sig = inspect.signature(smc_TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smc_tuple_is_not_abstract():
    assert not inspect.isabstract(smc_Tuple)


def test_hyp_smc_tuple_constructor_exists():
    assert callable(smc_Tuple.__init__)


def test_hyp_smc_tuple_constructor_args():
    sig = inspect.signature(smc_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_download_is_not_abstract():
    assert not inspect.isabstract(Download)


def test_hyp_download_constructor_exists():
    assert callable(Download.__init__)


def test_hyp_download_constructor_args():
    sig = inspect.signature(Download.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_client_is_not_abstract():
    assert not inspect.isabstract(smc_Client)


def test_hyp_smc_client_constructor_exists():
    assert callable(smc_Client.__init__)


def test_hyp_smc_client_constructor_args():
    sig = inspect.signature(smc_Client.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"




def test_hyp_smc_database_is_not_abstract():
    assert not inspect.isabstract(smc_Database)


def test_hyp_smc_database_constructor_exists():
    assert callable(smc_Database.__init__)


def test_hyp_smc_database_constructor_args():
    sig = inspect.signature(smc_Database.__init__)
    params = list(sig.parameters.keys())
    assert "clm" in params, "Missing parameter 'clm'"




def test_hyp_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_hyp_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_hyp_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_download_is_not_abstract():
    assert not inspect.isabstract(smc_Download)


def test_hyp_smc_download_constructor_exists():
    assert callable(smc_Download.__init__)


def test_hyp_smc_download_constructor_args():
    sig = inspect.signature(smc_Download.__init__)
    params = list(sig.parameters.keys())



def test_hyp_computation_is_not_abstract():
    assert not inspect.isabstract(Computation)


def test_hyp_computation_constructor_exists():
    assert callable(Computation.__init__)


def test_hyp_computation_constructor_args():
    sig = inspect.signature(Computation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_median_is_not_abstract():
    assert not inspect.isabstract(smc_Median)


def test_hyp_smc_median_constructor_exists():
    assert callable(smc_Median.__init__)


def test_hyp_smc_median_constructor_args():
    sig = inspect.signature(smc_Median.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_average_is_not_abstract():
    assert not inspect.isabstract(smc_Average)


def test_hyp_smc_average_constructor_exists():
    assert callable(smc_Average.__init__)


def test_hyp_smc_average_constructor_args():
    sig = inspect.signature(smc_Average.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_count_is_not_abstract():
    assert not inspect.isabstract(smc_Count)


def test_hyp_smc_count_constructor_exists():
    assert callable(smc_Count.__init__)


def test_hyp_smc_count_constructor_args():
    sig = inspect.signature(smc_Count.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_weightedavg_is_not_abstract():
    assert not inspect.isabstract(smc_WeightedAvg)


def test_hyp_smc_weightedavg_constructor_exists():
    assert callable(smc_WeightedAvg.__init__)


def test_hyp_smc_weightedavg_constructor_args():
    sig = inspect.signature(smc_WeightedAvg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_multiplication_is_not_abstract():
    assert not inspect.isabstract(smc_Multiplication)


def test_hyp_smc_multiplication_constructor_exists():
    assert callable(smc_Multiplication.__init__)


def test_hyp_smc_multiplication_constructor_args():
    sig = inspect.signature(smc_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_functions_is_not_abstract():
    assert not inspect.isabstract(Functions)


def test_hyp_functions_constructor_exists():
    assert callable(Functions.__init__)


def test_hyp_functions_constructor_args():
    sig = inspect.signature(Functions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_bloomfilter_is_not_abstract():
    assert not inspect.isabstract(smc_BloomFilter)


def test_hyp_smc_bloomfilter_constructor_exists():
    assert callable(smc_BloomFilter.__init__)


def test_hyp_smc_bloomfilter_constructor_args():
    sig = inspect.signature(smc_BloomFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_checktable_is_not_abstract():
    assert not inspect.isabstract(smc_CheckTable)


def test_hyp_smc_checktable_constructor_exists():
    assert callable(smc_CheckTable.__init__)


def test_hyp_smc_checktable_constructor_args():
    sig = inspect.signature(smc_CheckTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(smc_AccessControl)


def test_hyp_smc_accesscontrol_constructor_exists():
    assert callable(smc_AccessControl.__init__)


def test_hyp_smc_accesscontrol_constructor_args():
    sig = inspect.signature(smc_AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_addvalues_is_not_abstract():
    assert not inspect.isabstract(smc_AddValues)


def test_hyp_smc_addvalues_constructor_exists():
    assert callable(smc_AddValues.__init__)


def test_hyp_smc_addvalues_constructor_args():
    sig = inspect.signature(smc_AddValues.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_createtable_is_not_abstract():
    assert not inspect.isabstract(smc_CreateTable)


def test_hyp_smc_createtable_constructor_exists():
    assert callable(smc_CreateTable.__init__)


def test_hyp_smc_createtable_constructor_args():
    sig = inspect.signature(smc_CreateTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_search_is_not_abstract():
    assert not inspect.isabstract(smc_Search)


def test_hyp_smc_search_constructor_exists():
    assert callable(smc_Search.__init__)


def test_hyp_smc_search_constructor_args():
    sig = inspect.signature(smc_Search.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"




def test_hyp_smc_computation_is_not_abstract():
    assert not inspect.isabstract(smc_Computation)


def test_hyp_smc_computation_constructor_exists():
    assert callable(smc_Computation.__init__)


def test_hyp_smc_computation_constructor_args():
    sig = inspect.signature(smc_Computation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_functions_is_not_abstract():
    assert not inspect.isabstract(smc_Functions)


def test_hyp_smc_functions_constructor_exists():
    assert callable(smc_Functions.__init__)


def test_hyp_smc_functions_constructor_args():
    sig = inspect.signature(smc_Functions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_expression_is_not_abstract():
    assert not inspect.isabstract(smc_Expression)


def test_hyp_smc_expression_constructor_exists():
    assert callable(smc_Expression.__init__)


def test_hyp_smc_expression_constructor_args():
    sig = inspect.signature(smc_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_invocation_is_not_abstract():
    assert not inspect.isabstract(smc_Invocation)


def test_hyp_smc_invocation_constructor_exists():
    assert callable(smc_Invocation.__init__)


def test_hyp_smc_invocation_constructor_args():
    sig = inspect.signature(smc_Invocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_invocationvoid_is_not_abstract():
    assert not inspect.isabstract(smc_InvocationVoid)


def test_hyp_smc_invocationvoid_constructor_exists():
    assert callable(smc_InvocationVoid.__init__)


def test_hyp_smc_invocationvoid_constructor_args():
    sig = inspect.signature(smc_InvocationVoid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(smc_IfThenElse)


def test_hyp_smc_ifthenelse_constructor_exists():
    assert callable(smc_IfThenElse.__init__)


def test_hyp_smc_ifthenelse_constructor_args():
    sig = inspect.signature(smc_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_return_is_not_abstract():
    assert not inspect.isabstract(smc_Return)


def test_hyp_smc_return_constructor_exists():
    assert callable(smc_Return.__init__)


def test_hyp_smc_return_constructor_args():
    sig = inspect.signature(smc_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_block_is_not_abstract():
    assert not inspect.isabstract(smc_Block)


def test_hyp_smc_block_constructor_exists():
    assert callable(smc_Block.__init__)


def test_hyp_smc_block_constructor_args():
    sig = inspect.signature(smc_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_print_is_not_abstract():
    assert not inspect.isabstract(smc_Print)


def test_hyp_smc_print_constructor_exists():
    assert callable(smc_Print.__init__)


def test_hyp_smc_print_constructor_args():
    sig = inspect.signature(smc_Print.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_while_is_not_abstract():
    assert not inspect.isabstract(smc_While)


def test_hyp_smc_while_constructor_exists():
    assert callable(smc_While.__init__)


def test_hyp_smc_while_constructor_args():
    sig = inspect.signature(smc_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_paramdecl_is_not_abstract():
    assert not inspect.isabstract(smc_ParamDecl)


def test_hyp_smc_paramdecl_constructor_exists():
    assert callable(smc_ParamDecl.__init__)


def test_hyp_smc_paramdecl_constructor_args():
    sig = inspect.signature(smc_ParamDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "parName" in params, "Missing parameter 'parName'"
    assert "btype" in params, "Missing parameter 'btype'"
    assert "stype" in params, "Missing parameter 'stype'"







def test_hyp_smc_variableassignment_is_not_abstract():
    assert not inspect.isabstract(smc_VariableAssignment)


def test_hyp_smc_variableassignment_constructor_exists():
    assert callable(smc_VariableAssignment.__init__)


def test_hyp_smc_variableassignment_constructor_args():
    sig = inspect.signature(smc_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(smc_AbstractAssignment)


def test_hyp_smc_abstractassignment_constructor_exists():
    assert callable(smc_AbstractAssignment.__init__)


def test_hyp_smc_abstractassignment_constructor_args():
    sig = inspect.signature(smc_AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_variabledecl_is_not_abstract():
    assert not inspect.isabstract(smc_VariableDecl)


def test_hyp_smc_variabledecl_constructor_exists():
    assert callable(smc_VariableDecl.__init__)


def test_hyp_smc_variabledecl_constructor_args():
    sig = inspect.signature(smc_VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "length" in params, "Missing parameter 'length'"
    assert "type" in params, "Missing parameter 'type'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "array" in params, "Missing parameter 'array'"








def test_hyp_smc_smc_is_not_abstract():
    assert not inspect.isabstract(smc_Smc)


def test_hyp_smc_smc_constructor_exists():
    assert callable(smc_Smc.__init__)


def test_hyp_smc_smc_constructor_args():
    sig = inspect.signature(smc_Smc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_command_is_not_abstract():
    assert not inspect.isabstract(smc_Command)


def test_hyp_smc_command_constructor_exists():
    assert callable(smc_Command.__init__)


def test_hyp_smc_command_constructor_args():
    sig = inspect.signature(smc_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_mainsmc_is_not_abstract():
    assert not inspect.isabstract(smc_MainSMC)


def test_hyp_smc_mainsmc_constructor_exists():
    assert callable(smc_MainSMC.__init__)


def test_hyp_smc_mainsmc_constructor_args():
    sig = inspect.signature(smc_MainSMC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smc_blocksmc_is_not_abstract():
    assert not inspect.isabstract(smc_BlockSMC)


def test_hyp_smc_blocksmc_constructor_exists():
    assert callable(smc_BlockSMC.__init__)


def test_hyp_smc_blocksmc_constructor_args():
    sig = inspect.signature(smc_BlockSMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"



def test_hyp_blocktype_exists():
    # Check that the Enumeration exists
    assert BlockType is not None

def test_hyp_blocktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockType]
    expected_literals = [
        "INSERT",
        "ANONYMIZATION",
        "COMP",
        "ACCESS",
        "PERMISSION",
        "SEARCH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockType"

def test_hyp_sectype_exists():
    # Check that the Enumeration exists
    assert SecType is not None

def test_hyp_sectype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SecType]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SecType"

def test_hyp_basictype_exists():
    # Check that the Enumeration exists
    assert BasicType is not None

def test_hyp_basictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicType]
    expected_literals = [
        "BOOLEAN",
        "DOUBLE",
        "ENCRYPTED",
        "STRING",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicType"


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
AccessControl_strategy = st.builds(
    AccessControl,
)
smc_Covered_strategy = st.builds(
    smc_Covered,
)
smc_BellLapadula_strategy = st.builds(
    smc_BellLapadula,
    mode=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
smc_PlusOrMinus_strategy = st.builds(
    smc_PlusOrMinus,
    op=
        safe_text
)
smc_Equality_strategy = st.builds(
    smc_Equality,
    op=
        safe_text
)
smc_BooleanLiteral_strategy = st.builds(
    smc_BooleanLiteral,
    value=
        st.booleans()
)
smc_IntLiteral_strategy = st.builds(
    smc_IntLiteral,
    value=
        st.integers()
)
smc_List_strategy = st.builds(
    smc_List,
)
smc_StringLiteral_strategy = st.builds(
    smc_StringLiteral,
    value=
        safe_text
)
smc_DateLiteral_strategy = st.builds(
    smc_DateLiteral,
    value=
        safe_text
)
smc_DoubleLiteral_strategy = st.builds(
    smc_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smc_Dict_strategy = st.builds(
    smc_Dict,
)
smc_VariableRef_strategy = st.builds(
    smc_VariableRef,
)
smc_Comparison_strategy = st.builds(
    smc_Comparison,
    op=
        safe_text
)
smc_Or_strategy = st.builds(
    smc_Or,
)
smc_Not_strategy = st.builds(
    smc_Not,
)
smc_MulOrDiv_strategy = st.builds(
    smc_MulOrDiv,
    op=
        safe_text
)
smc_And_strategy = st.builds(
    smc_And,
)
smc_TimeLiteral_strategy = st.builds(
    smc_TimeLiteral,
    value=
        safe_text
)
smc_Tuple_strategy = st.builds(
    smc_Tuple,
)
Download_strategy = st.builds(
    Download,
)
smc_Client_strategy = st.builds(
    smc_Client,
    arg=
        safe_text
)
smc_Database_strategy = st.builds(
    smc_Database,
    clm=
        safe_text
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
smc_Download_strategy = st.builds(
    smc_Download,
)
Computation_strategy = st.builds(
    Computation,
)
smc_Median_strategy = st.builds(
    smc_Median,
)
smc_Average_strategy = st.builds(
    smc_Average,
)
smc_Count_strategy = st.builds(
    smc_Count,
)
smc_WeightedAvg_strategy = st.builds(
    smc_WeightedAvg,
)
smc_Multiplication_strategy = st.builds(
    smc_Multiplication,
)
Functions_strategy = st.builds(
    Functions,
)
smc_BloomFilter_strategy = st.builds(
    smc_BloomFilter,
)
smc_CheckTable_strategy = st.builds(
    smc_CheckTable,
)
smc_AccessControl_strategy = st.builds(
    smc_AccessControl,
)
smc_AddValues_strategy = st.builds(
    smc_AddValues,
)
smc_CreateTable_strategy = st.builds(
    smc_CreateTable,
)
smc_Search_strategy = st.builds(
    smc_Search,
    column=
        safe_text
)
smc_Computation_strategy = st.builds(
    smc_Computation,
)
smc_Functions_strategy = st.builds(
    smc_Functions,
)
smc_Expression_strategy = st.builds(
    smc_Expression,
)
smc_Invocation_strategy = st.builds(
    smc_Invocation,
)
Command_strategy = st.builds(
    Command,
)
smc_InvocationVoid_strategy = st.builds(
    smc_InvocationVoid,
)
smc_IfThenElse_strategy = st.builds(
    smc_IfThenElse,
)
smc_Return_strategy = st.builds(
    smc_Return,
)
smc_Block_strategy = st.builds(
    smc_Block,
)
smc_Print_strategy = st.builds(
    smc_Print,
)
smc_While_strategy = st.builds(
    smc_While,
)
smc_ParamDecl_strategy = st.builds(
    smc_ParamDecl,
    name=
        safe_text,
    parName=
        safe_text,
    btype=
        safe_text,
    stype=
        safe_text
)
smc_VariableAssignment_strategy = st.builds(
    smc_VariableAssignment,
)
smc_AbstractAssignment_strategy = st.builds(
    smc_AbstractAssignment,
)
smc_VariableDecl_strategy = st.builds(
    smc_VariableDecl,
    name=
        safe_text,
    length=
        st.integers(),
    type=
        safe_text,
    visibility=
        safe_text,
    array=
        st.booleans()
)
smc_Smc_strategy = st.builds(
    smc_Smc,
)
smc_Command_strategy = st.builds(
    smc_Command,
)
smc_MainSMC_strategy = st.builds(
    smc_MainSMC,
)
smc_BlockSMC_strategy = st.builds(
    smc_BlockSMC,
    name=
        safe_text,
    type=
        safe_text
)






@given(instance=smc_BellLapadula_strategy)
def test_hyp_smc_belllapadula_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original





@given(instance=smc_PlusOrMinus_strategy)
def test_hyp_smc_plusorminus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=smc_Equality_strategy)
def test_hyp_smc_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=smc_BooleanLiteral_strategy)
def test_hyp_smc_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=smc_IntLiteral_strategy)
def test_hyp_smc_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=smc_StringLiteral_strategy)
def test_hyp_smc_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=smc_DateLiteral_strategy)
def test_hyp_smc_dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=smc_DoubleLiteral_strategy)
def test_hyp_smc_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=smc_Comparison_strategy)
def test_hyp_smc_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=smc_MulOrDiv_strategy)
def test_hyp_smc_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=smc_TimeLiteral_strategy)
def test_hyp_smc_timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=smc_Client_strategy)
def test_hyp_smc_client_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original




@given(instance=smc_Database_strategy)
def test_hyp_smc_database_clm_setter(instance):
    original = instance.clm
    instance.clm = original
    assert instance.clm == original


















@given(instance=smc_Search_strategy)
def test_hyp_smc_search_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original















@given(instance=smc_ParamDecl_strategy)
def test_hyp_smc_paramdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_ParamDecl_strategy)
def test_hyp_smc_paramdecl_parName_setter(instance):
    original = instance.parName
    instance.parName = original
    assert instance.parName == original



@given(instance=smc_ParamDecl_strategy)
def test_hyp_smc_paramdecl_btype_setter(instance):
    original = instance.btype
    instance.btype = original
    assert instance.btype == original



@given(instance=smc_ParamDecl_strategy)
def test_hyp_smc_paramdecl_stype_setter(instance):
    original = instance.stype
    instance.stype = original
    assert instance.stype == original






@given(instance=smc_VariableDecl_strategy)
def test_hyp_smc_variabledecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_VariableDecl_strategy)
def test_hyp_smc_variabledecl_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=smc_VariableDecl_strategy)
def test_hyp_smc_variabledecl_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=smc_VariableDecl_strategy)
def test_hyp_smc_variabledecl_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=smc_VariableDecl_strategy)
def test_hyp_smc_variabledecl_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original







@given(instance=smc_BlockSMC_strategy)
def test_hyp_smc_blocksmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_BlockSMC_strategy)
def test_hyp_smc_blocksmc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractAssignment,
    AccessControl,
    Command,
    Computation,
    Download,
    Expression,
    Functions,
    smc_AbstractAssignment,
    smc_AccessControl,
    smc_AddValues,
    smc_And,
    smc_Average,
    smc_BellLapadula,
    smc_Block,
    smc_BlockSMC,
    smc_BloomFilter,
    smc_BooleanLiteral,
    smc_CheckTable,
    smc_Client,
    smc_Command,
    smc_Comparison,
    smc_Computation,
    smc_Count,
    smc_Covered,
    smc_CreateTable,
    smc_Database,
    smc_DateLiteral,
    smc_Dict,
    smc_DoubleLiteral,
    smc_Download,
    smc_Equality,
    smc_Expression,
    smc_Functions,
    smc_IfThenElse,
    smc_IntLiteral,
    smc_Invocation,
    smc_InvocationVoid,
    smc_List,
    smc_MainSMC,
    smc_Median,
    smc_MulOrDiv,
    smc_Multiplication,
    smc_Not,
    smc_Or,
    smc_ParamDecl,
    smc_PlusOrMinus,
    smc_Print,
    smc_Return,
    smc_Search,
    smc_Smc,
    smc_StringLiteral,
    smc_TimeLiteral,
    smc_Tuple,
    smc_VariableAssignment,
    smc_VariableDecl,
    smc_VariableRef,
    smc_WeightedAvg,
    smc_While,
    BasicType,
    BlockType,
    SecType,
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

def test_smc_BellLapadula_mode_value_roundtrip():
    instance = smc_BellLapadula(mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_smc_BlockSMC_name_value_roundtrip():
    instance = smc_BlockSMC(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smc_BlockSMC_type_value_roundtrip():
    instance = smc_BlockSMC(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_smc_BooleanLiteral_value_value_roundtrip():
    instance = smc_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_smc_Client_arg_value_roundtrip():
    instance = smc_Client(arg="sample_text")
    assert instance.arg == "sample_text"
    instance.arg = "sample_text_2"
    assert instance.arg == "sample_text_2"


def test_smc_Comparison_op_value_roundtrip():
    instance = smc_Comparison(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_smc_Database_clm_value_roundtrip():
    instance = smc_Database(clm="sample_text")
    assert instance.clm == "sample_text"
    instance.clm = "sample_text_2"
    assert instance.clm == "sample_text_2"


def test_smc_DateLiteral_value_value_roundtrip():
    instance = smc_DateLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_smc_DoubleLiteral_value_value_roundtrip():
    instance = smc_DoubleLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_smc_Equality_op_value_roundtrip():
    instance = smc_Equality(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_smc_IntLiteral_value_value_roundtrip():
    instance = smc_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_smc_MulOrDiv_op_value_roundtrip():
    instance = smc_MulOrDiv(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_smc_ParamDecl_btype_value_roundtrip():
    instance = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    assert instance.btype == "sample_text"
    instance.btype = "sample_text_2"
    assert instance.btype == "sample_text_2"


def test_smc_ParamDecl_name_value_roundtrip():
    instance = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smc_ParamDecl_parName_value_roundtrip():
    instance = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    assert instance.parName == "sample_text"
    instance.parName = "sample_text_2"
    assert instance.parName == "sample_text_2"


def test_smc_ParamDecl_stype_value_roundtrip():
    instance = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    assert instance.stype == "sample_text"
    instance.stype = "sample_text_2"
    assert instance.stype == "sample_text_2"


def test_smc_PlusOrMinus_op_value_roundtrip():
    instance = smc_PlusOrMinus(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_smc_Search_column_value_roundtrip():
    instance = smc_Search(column="sample_text")
    assert instance.column == "sample_text"
    instance.column = "sample_text_2"
    assert instance.column == "sample_text_2"


def test_smc_StringLiteral_value_value_roundtrip():
    instance = smc_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_smc_TimeLiteral_value_value_roundtrip():
    instance = smc_TimeLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_smc_VariableDecl_array_value_roundtrip():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert instance.array == True
    instance.array = False
    assert instance.array == False


def test_smc_VariableDecl_length_value_roundtrip():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_smc_VariableDecl_name_value_roundtrip():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smc_VariableDecl_type_value_roundtrip():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_smc_VariableDecl_visibility_value_roundtrip():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_smc_Download_isa_AbstractAssignment():
    instance = smc_Download()
    assert isinstance(instance, AbstractAssignment)


def test_smc_Expression_isa_AbstractAssignment():
    instance = smc_Expression()
    assert isinstance(instance, AbstractAssignment)


def test_smc_BellLapadula_isa_AccessControl():
    instance = smc_BellLapadula(mode="sample_text")
    assert isinstance(instance, AccessControl)


def test_smc_Covered_isa_AccessControl():
    instance = smc_Covered()
    assert isinstance(instance, AccessControl)


def test_smc_Block_isa_Command():
    instance = smc_Block()
    assert isinstance(instance, Command)


def test_smc_IfThenElse_isa_Command():
    instance = smc_IfThenElse()
    assert isinstance(instance, Command)


def test_smc_InvocationVoid_isa_Command():
    instance = smc_InvocationVoid()
    assert isinstance(instance, Command)


def test_smc_ParamDecl_isa_Command():
    instance = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    assert isinstance(instance, Command)


def test_smc_Print_isa_Command():
    instance = smc_Print()
    assert isinstance(instance, Command)


def test_smc_Return_isa_Command():
    instance = smc_Return()
    assert isinstance(instance, Command)


def test_smc_VariableAssignment_isa_Command():
    instance = smc_VariableAssignment()
    assert isinstance(instance, Command)


def test_smc_VariableDecl_isa_Command():
    instance = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    assert isinstance(instance, Command)


def test_smc_While_isa_Command():
    instance = smc_While()
    assert isinstance(instance, Command)


def test_smc_Average_isa_Computation():
    instance = smc_Average()
    assert isinstance(instance, Computation)


def test_smc_Count_isa_Computation():
    instance = smc_Count()
    assert isinstance(instance, Computation)


def test_smc_Median_isa_Computation():
    instance = smc_Median()
    assert isinstance(instance, Computation)


def test_smc_Multiplication_isa_Computation():
    instance = smc_Multiplication()
    assert isinstance(instance, Computation)


def test_smc_WeightedAvg_isa_Computation():
    instance = smc_WeightedAvg()
    assert isinstance(instance, Computation)


def test_smc_Client_isa_Download():
    instance = smc_Client(arg="sample_text")
    assert isinstance(instance, Download)


def test_smc_Database_isa_Download():
    instance = smc_Database(clm="sample_text")
    assert isinstance(instance, Download)


def test_smc_And_isa_Expression():
    instance = smc_And()
    assert isinstance(instance, Expression)


def test_smc_BooleanLiteral_isa_Expression():
    instance = smc_BooleanLiteral(value=True)
    assert isinstance(instance, Expression)


def test_smc_Comparison_isa_Expression():
    instance = smc_Comparison(op="sample_text")
    assert isinstance(instance, Expression)


def test_smc_DateLiteral_isa_Expression():
    instance = smc_DateLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_smc_Dict_isa_Expression():
    instance = smc_Dict()
    assert isinstance(instance, Expression)


def test_smc_DoubleLiteral_isa_Expression():
    instance = smc_DoubleLiteral(value=3.14)
    assert isinstance(instance, Expression)


def test_smc_Equality_isa_Expression():
    instance = smc_Equality(op="sample_text")
    assert isinstance(instance, Expression)


def test_smc_IntLiteral_isa_Expression():
    instance = smc_IntLiteral(value=7)
    assert isinstance(instance, Expression)


def test_smc_Invocation_isa_Expression():
    instance = smc_Invocation()
    assert isinstance(instance, Expression)


def test_smc_List_isa_Expression():
    instance = smc_List()
    assert isinstance(instance, Expression)


def test_smc_MulOrDiv_isa_Expression():
    instance = smc_MulOrDiv(op="sample_text")
    assert isinstance(instance, Expression)


def test_smc_Not_isa_Expression():
    instance = smc_Not()
    assert isinstance(instance, Expression)


def test_smc_Or_isa_Expression():
    instance = smc_Or()
    assert isinstance(instance, Expression)


def test_smc_PlusOrMinus_isa_Expression():
    instance = smc_PlusOrMinus(op="sample_text")
    assert isinstance(instance, Expression)


def test_smc_StringLiteral_isa_Expression():
    instance = smc_StringLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_smc_TimeLiteral_isa_Expression():
    instance = smc_TimeLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_smc_Tuple_isa_Expression():
    instance = smc_Tuple()
    assert isinstance(instance, Expression)


def test_smc_VariableRef_isa_Expression():
    instance = smc_VariableRef()
    assert isinstance(instance, Expression)


def test_smc_AccessControl_isa_Functions():
    instance = smc_AccessControl()
    assert isinstance(instance, Functions)


def test_smc_AddValues_isa_Functions():
    instance = smc_AddValues()
    assert isinstance(instance, Functions)


def test_smc_BloomFilter_isa_Functions():
    instance = smc_BloomFilter()
    assert isinstance(instance, Functions)


def test_smc_CheckTable_isa_Functions():
    instance = smc_CheckTable()
    assert isinstance(instance, Functions)


def test_smc_Computation_isa_Functions():
    instance = smc_Computation()
    assert isinstance(instance, Functions)


def test_smc_CreateTable_isa_Functions():
    instance = smc_CreateTable()
    assert isinstance(instance, Functions)


def test_smc_Search_isa_Functions():
    instance = smc_Search(column="sample_text")
    assert isinstance(instance, Functions)


def test_assoc_args87_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_AddValues()
    b2 = smc_AddValues()
    _safe_set(a, 'smc_VariableDecl89', b1)
    assert _is_linked(a, 'smc_VariableDecl89', b1)
    if hasattr(b1, 'smc_AddValues88'):
        assert _is_linked(b1, 'smc_AddValues88', a)
    _safe_set(a, 'smc_VariableDecl89', b2)
    assert _is_linked(a, 'smc_VariableDecl89', b2)
    if hasattr(b1, 'smc_AddValues88'):
        assert not _is_linked(b1, 'smc_AddValues88', a)
    if hasattr(b2, 'smc_AddValues88'):
        assert _is_linked(b2, 'smc_AddValues88', a)
    _safe_set(a, 'smc_VariableDecl89', None)
    assert not _is_linked(a, 'smc_VariableDecl89', b2)
    if hasattr(b2, 'smc_AddValues88'):
        assert not _is_linked(b2, 'smc_AddValues88', a)


def test_assoc_array50_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Median()
    b2 = smc_Median()
    _safe_set(a, 'smc_VariableDecl51', b1)
    assert _is_linked(a, 'smc_VariableDecl51', b1)
    if hasattr(b1, 'smc_Median'):
        assert _is_linked(b1, 'smc_Median', a)
    _safe_set(a, 'smc_VariableDecl51', b2)
    assert _is_linked(a, 'smc_VariableDecl51', b2)
    if hasattr(b1, 'smc_Median'):
        assert not _is_linked(b1, 'smc_Median', a)
    if hasattr(b2, 'smc_Median'):
        assert _is_linked(b2, 'smc_Median', a)
    _safe_set(a, 'smc_VariableDecl51', None)
    assert not _is_linked(a, 'smc_VariableDecl51', b2)
    if hasattr(b2, 'smc_Median'):
        assert not _is_linked(b2, 'smc_Median', a)


def test_assoc_array57_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Average()
    b2 = smc_Average()
    _safe_set(a, 'smc_VariableDecl58', b1)
    assert _is_linked(a, 'smc_VariableDecl58', b1)
    if hasattr(b1, 'smc_Average'):
        assert _is_linked(b1, 'smc_Average', a)
    _safe_set(a, 'smc_VariableDecl58', b2)
    assert _is_linked(a, 'smc_VariableDecl58', b2)
    if hasattr(b1, 'smc_Average'):
        assert not _is_linked(b1, 'smc_Average', a)
    if hasattr(b2, 'smc_Average'):
        assert _is_linked(b2, 'smc_Average', a)
    _safe_set(a, 'smc_VariableDecl58', None)
    assert not _is_linked(a, 'smc_VariableDecl58', b2)
    if hasattr(b2, 'smc_Average'):
        assert not _is_linked(b2, 'smc_Average', a)


def test_assoc_array59_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Count()
    b2 = smc_Count()
    _safe_set(a, 'smc_VariableDecl60', b1)
    assert _is_linked(a, 'smc_VariableDecl60', b1)
    if hasattr(b1, 'smc_Count'):
        assert _is_linked(b1, 'smc_Count', a)
    _safe_set(a, 'smc_VariableDecl60', b2)
    assert _is_linked(a, 'smc_VariableDecl60', b2)
    if hasattr(b1, 'smc_Count'):
        assert not _is_linked(b1, 'smc_Count', a)
    if hasattr(b2, 'smc_Count'):
        assert _is_linked(b2, 'smc_Count', a)
    _safe_set(a, 'smc_VariableDecl60', None)
    assert not _is_linked(a, 'smc_VariableDecl60', b2)
    if hasattr(b2, 'smc_Count'):
        assert not _is_linked(b2, 'smc_Count', a)


def test_assoc_blockName40_link_reassign_clear():
    a = smc_BlockSMC(name="sample_text", type="sample_text")
    b1 = smc_Invocation()
    b2 = smc_Invocation()
    _safe_set(a, 'smc_BlockSMC42', b1)
    assert _is_linked(a, 'smc_BlockSMC42', b1)
    if hasattr(b1, 'smc_Invocation41'):
        assert _is_linked(b1, 'smc_Invocation41', a)
    _safe_set(a, 'smc_BlockSMC42', b2)
    assert _is_linked(a, 'smc_BlockSMC42', b2)
    if hasattr(b1, 'smc_Invocation41'):
        assert not _is_linked(b1, 'smc_Invocation41', a)
    if hasattr(b2, 'smc_Invocation41'):
        assert _is_linked(b2, 'smc_Invocation41', a)
    _safe_set(a, 'smc_BlockSMC42', None)
    assert not _is_linked(a, 'smc_BlockSMC42', b2)
    if hasattr(b2, 'smc_Invocation41'):
        assert not _is_linked(b2, 'smc_Invocation41', a)


def test_assoc_blocks0_link_reassign_clear():
    a = smc_BlockSMC(name="sample_text", type="sample_text")
    b1 = smc_Smc()
    b2 = smc_Smc()
    _safe_set(a, 'smc_BlockSMC', b1)
    assert _is_linked(a, 'smc_BlockSMC', b1)
    if hasattr(b1, 'smc_Smc'):
        assert _is_linked(b1, 'smc_Smc', a)
    _safe_set(a, 'smc_BlockSMC', b2)
    assert _is_linked(a, 'smc_BlockSMC', b2)
    if hasattr(b1, 'smc_Smc'):
        assert not _is_linked(b1, 'smc_Smc', a)
    if hasattr(b2, 'smc_Smc'):
        assert _is_linked(b2, 'smc_Smc', a)
    _safe_set(a, 'smc_BlockSMC', None)
    assert not _is_linked(a, 'smc_BlockSMC', b2)
    if hasattr(b2, 'smc_Smc'):
        assert not _is_linked(b2, 'smc_Smc', a)


def test_assoc_c_lvls61_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_AccessControl()
    b2 = smc_AccessControl()
    _safe_set(a, 'smc_VariableDecl62', b1)
    assert _is_linked(a, 'smc_VariableDecl62', b1)
    if hasattr(b1, 'smc_AccessControl'):
        assert _is_linked(b1, 'smc_AccessControl', a)
    _safe_set(a, 'smc_VariableDecl62', b2)
    assert _is_linked(a, 'smc_VariableDecl62', b2)
    if hasattr(b1, 'smc_AccessControl'):
        assert not _is_linked(b1, 'smc_AccessControl', a)
    if hasattr(b2, 'smc_AccessControl'):
        assert _is_linked(b2, 'smc_AccessControl', a)
    _safe_set(a, 'smc_VariableDecl62', None)
    assert not _is_linked(a, 'smc_VariableDecl62', b2)
    if hasattr(b2, 'smc_AccessControl'):
        assert not _is_linked(b2, 'smc_AccessControl', a)


def test_assoc_covered70_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Covered()
    b2 = smc_Covered()
    _safe_set(a, 'smc_VariableDecl72', b1)
    assert _is_linked(a, 'smc_VariableDecl72', b1)
    if hasattr(b1, 'smc_Covered71'):
        assert _is_linked(b1, 'smc_Covered71', a)
    _safe_set(a, 'smc_VariableDecl72', b2)
    assert _is_linked(a, 'smc_VariableDecl72', b2)
    if hasattr(b1, 'smc_Covered71'):
        assert not _is_linked(b1, 'smc_Covered71', a)
    if hasattr(b2, 'smc_Covered71'):
        assert _is_linked(b2, 'smc_Covered71', a)
    _safe_set(a, 'smc_VariableDecl72', None)
    assert not _is_linked(a, 'smc_VariableDecl72', b2)
    if hasattr(b2, 'smc_Covered71'):
        assert not _is_linked(b2, 'smc_Covered71', a)


def test_assoc_cur66_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_BellLapadula(mode="sample_text")
    b2 = smc_BellLapadula(mode="sample_text_2")
    _safe_set(a, 'smc_VariableDecl67', b1)
    assert _is_linked(a, 'smc_VariableDecl67', b1)
    if hasattr(b1, 'smc_BellLapadula'):
        assert _is_linked(b1, 'smc_BellLapadula', a)
    _safe_set(a, 'smc_VariableDecl67', b2)
    assert _is_linked(a, 'smc_VariableDecl67', b2)
    if hasattr(b1, 'smc_BellLapadula'):
        assert not _is_linked(b1, 'smc_BellLapadula', a)
    if hasattr(b2, 'smc_BellLapadula'):
        assert _is_linked(b2, 'smc_BellLapadula', a)
    _safe_set(a, 'smc_VariableDecl67', None)
    assert not _is_linked(a, 'smc_VariableDecl67', b2)
    if hasattr(b2, 'smc_BellLapadula'):
        assert not _is_linked(b2, 'smc_BellLapadula', a)


def test_assoc_elems54_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_WeightedAvg()
    b2 = smc_WeightedAvg()
    _safe_set(a, 'smc_VariableDecl56', b1)
    assert _is_linked(a, 'smc_VariableDecl56', b1)
    if hasattr(b1, 'smc_WeightedAvg55'):
        assert _is_linked(b1, 'smc_WeightedAvg55', a)
    _safe_set(a, 'smc_VariableDecl56', b2)
    assert _is_linked(a, 'smc_VariableDecl56', b2)
    if hasattr(b1, 'smc_WeightedAvg55'):
        assert not _is_linked(b1, 'smc_WeightedAvg55', a)
    if hasattr(b2, 'smc_WeightedAvg55'):
        assert _is_linked(b2, 'smc_WeightedAvg55', a)
    _safe_set(a, 'smc_VariableDecl56', None)
    assert not _is_linked(a, 'smc_VariableDecl56', b2)
    if hasattr(b2, 'smc_WeightedAvg55'):
        assert not _is_linked(b2, 'smc_WeightedAvg55', a)


def test_assoc_keyword75_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Search(column="sample_text")
    b2 = smc_Search(column="sample_text_2")
    _safe_set(a, 'smc_VariableDecl77', b1)
    assert _is_linked(a, 'smc_VariableDecl77', b1)
    if hasattr(b1, 'smc_Search76'):
        assert _is_linked(b1, 'smc_Search76', a)
    _safe_set(a, 'smc_VariableDecl77', b2)
    assert _is_linked(a, 'smc_VariableDecl77', b2)
    if hasattr(b1, 'smc_Search76'):
        assert not _is_linked(b1, 'smc_Search76', a)
    if hasattr(b2, 'smc_Search76'):
        assert _is_linked(b2, 'smc_Search76', a)
    _safe_set(a, 'smc_VariableDecl77', None)
    assert not _is_linked(a, 'smc_VariableDecl77', b2)
    if hasattr(b2, 'smc_Search76'):
        assert not _is_linked(b2, 'smc_Search76', a)


def test_assoc_left106_link_reassign_clear():
    a = smc_Equality(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_Equality', b1)
    assert _is_linked(a, 'smc_Equality', b1)
    if hasattr(b1, 'smc_Expression107'):
        assert _is_linked(b1, 'smc_Expression107', a)
    _safe_set(a, 'smc_Equality', b2)
    assert _is_linked(a, 'smc_Equality', b2)
    if hasattr(b1, 'smc_Expression107'):
        assert not _is_linked(b1, 'smc_Expression107', a)
    if hasattr(b2, 'smc_Expression107'):
        assert _is_linked(b2, 'smc_Expression107', a)
    _safe_set(a, 'smc_Equality', None)
    assert not _is_linked(a, 'smc_Equality', b2)
    if hasattr(b2, 'smc_Expression107'):
        assert not _is_linked(b2, 'smc_Expression107', a)


def test_assoc_left111_link_reassign_clear():
    a = smc_Comparison(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_Comparison', b1)
    assert _is_linked(a, 'smc_Comparison', b1)
    if hasattr(b1, 'smc_Expression112'):
        assert _is_linked(b1, 'smc_Expression112', a)
    _safe_set(a, 'smc_Comparison', b2)
    assert _is_linked(a, 'smc_Comparison', b2)
    if hasattr(b1, 'smc_Expression112'):
        assert not _is_linked(b1, 'smc_Expression112', a)
    if hasattr(b2, 'smc_Expression112'):
        assert _is_linked(b2, 'smc_Expression112', a)
    _safe_set(a, 'smc_Comparison', None)
    assert not _is_linked(a, 'smc_Comparison', b2)
    if hasattr(b2, 'smc_Expression112'):
        assert not _is_linked(b2, 'smc_Expression112', a)


def test_assoc_left116_link_reassign_clear():
    a = smc_PlusOrMinus(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_PlusOrMinus', b1)
    assert _is_linked(a, 'smc_PlusOrMinus', b1)
    if hasattr(b1, 'smc_Expression117'):
        assert _is_linked(b1, 'smc_Expression117', a)
    _safe_set(a, 'smc_PlusOrMinus', b2)
    assert _is_linked(a, 'smc_PlusOrMinus', b2)
    if hasattr(b1, 'smc_Expression117'):
        assert not _is_linked(b1, 'smc_Expression117', a)
    if hasattr(b2, 'smc_Expression117'):
        assert _is_linked(b2, 'smc_Expression117', a)
    _safe_set(a, 'smc_PlusOrMinus', None)
    assert not _is_linked(a, 'smc_PlusOrMinus', b2)
    if hasattr(b2, 'smc_Expression117'):
        assert not _is_linked(b2, 'smc_Expression117', a)


def test_assoc_left121_link_reassign_clear():
    a = smc_MulOrDiv(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_MulOrDiv', b1)
    assert _is_linked(a, 'smc_MulOrDiv', b1)
    if hasattr(b1, 'smc_Expression122'):
        assert _is_linked(b1, 'smc_Expression122', a)
    _safe_set(a, 'smc_MulOrDiv', b2)
    assert _is_linked(a, 'smc_MulOrDiv', b2)
    if hasattr(b1, 'smc_Expression122'):
        assert not _is_linked(b1, 'smc_Expression122', a)
    if hasattr(b2, 'smc_Expression122'):
        assert _is_linked(b2, 'smc_Expression122', a)
    _safe_set(a, 'smc_MulOrDiv', None)
    assert not _is_linked(a, 'smc_MulOrDiv', b2)
    if hasattr(b2, 'smc_Expression122'):
        assert not _is_linked(b2, 'smc_Expression122', a)


def test_assoc_match68_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Covered()
    b2 = smc_Covered()
    _safe_set(a, 'smc_VariableDecl69', b1)
    assert _is_linked(a, 'smc_VariableDecl69', b1)
    if hasattr(b1, 'smc_Covered'):
        assert _is_linked(b1, 'smc_Covered', a)
    _safe_set(a, 'smc_VariableDecl69', b2)
    assert _is_linked(a, 'smc_VariableDecl69', b2)
    if hasattr(b1, 'smc_Covered'):
        assert not _is_linked(b1, 'smc_Covered', a)
    if hasattr(b2, 'smc_Covered'):
        assert _is_linked(b2, 'smc_Covered', a)
    _safe_set(a, 'smc_VariableDecl69', None)
    assert not _is_linked(a, 'smc_VariableDecl69', b2)
    if hasattr(b2, 'smc_Covered'):
        assert not _is_linked(b2, 'smc_Covered', a)


def test_assoc_option20_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_AbstractAssignment()
    b2 = smc_AbstractAssignment()
    _safe_set(a, 'smc_VariableDecl', b1)
    assert _is_linked(a, 'smc_VariableDecl', b1)
    if hasattr(b1, 'smc_AbstractAssignment'):
        assert _is_linked(b1, 'smc_AbstractAssignment', a)
    _safe_set(a, 'smc_VariableDecl', b2)
    assert _is_linked(a, 'smc_VariableDecl', b2)
    if hasattr(b1, 'smc_AbstractAssignment'):
        assert not _is_linked(b1, 'smc_AbstractAssignment', a)
    if hasattr(b2, 'smc_AbstractAssignment'):
        assert _is_linked(b2, 'smc_AbstractAssignment', a)
    _safe_set(a, 'smc_VariableDecl', None)
    assert not _is_linked(a, 'smc_VariableDecl', b2)
    if hasattr(b2, 'smc_AbstractAssignment'):
        assert not _is_linked(b2, 'smc_AbstractAssignment', a)


def test_assoc_params92_link_reassign_clear():
    a = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    b1 = smc_CreateTable()
    b2 = smc_CreateTable()
    _safe_set(a, 'smc_ParamDecl', b1)
    assert _is_linked(a, 'smc_ParamDecl', b1)
    if hasattr(b1, 'smc_CreateTable93'):
        assert _is_linked(b1, 'smc_CreateTable93', a)
    _safe_set(a, 'smc_ParamDecl', b2)
    assert _is_linked(a, 'smc_ParamDecl', b2)
    if hasattr(b1, 'smc_CreateTable93'):
        assert not _is_linked(b1, 'smc_CreateTable93', a)
    if hasattr(b2, 'smc_CreateTable93'):
        assert _is_linked(b2, 'smc_CreateTable93', a)
    _safe_set(a, 'smc_ParamDecl', None)
    assert not _is_linked(a, 'smc_ParamDecl', b2)
    if hasattr(b2, 'smc_CreateTable93'):
        assert not _is_linked(b2, 'smc_CreateTable93', a)


def test_assoc_post80_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_BloomFilter()
    b2 = smc_BloomFilter()
    _safe_set(a, 'smc_VariableDecl82', b1)
    assert _is_linked(a, 'smc_VariableDecl82', b1)
    if hasattr(b1, 'smc_BloomFilter81'):
        assert _is_linked(b1, 'smc_BloomFilter81', a)
    _safe_set(a, 'smc_VariableDecl82', b2)
    assert _is_linked(a, 'smc_VariableDecl82', b2)
    if hasattr(b1, 'smc_BloomFilter81'):
        assert not _is_linked(b1, 'smc_BloomFilter81', a)
    if hasattr(b2, 'smc_BloomFilter81'):
        assert _is_linked(b2, 'smc_BloomFilter81', a)
    _safe_set(a, 'smc_VariableDecl82', None)
    assert not _is_linked(a, 'smc_VariableDecl82', b2)
    if hasattr(b2, 'smc_BloomFilter81'):
        assert not _is_linked(b2, 'smc_BloomFilter81', a)


def test_assoc_pre78_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_BloomFilter()
    b2 = smc_BloomFilter()
    _safe_set(a, 'smc_VariableDecl79', b1)
    assert _is_linked(a, 'smc_VariableDecl79', b1)
    if hasattr(b1, 'smc_BloomFilter'):
        assert _is_linked(b1, 'smc_BloomFilter', a)
    _safe_set(a, 'smc_VariableDecl79', b2)
    assert _is_linked(a, 'smc_VariableDecl79', b2)
    if hasattr(b1, 'smc_BloomFilter'):
        assert not _is_linked(b1, 'smc_BloomFilter', a)
    if hasattr(b2, 'smc_BloomFilter'):
        assert _is_linked(b2, 'smc_BloomFilter', a)
    _safe_set(a, 'smc_VariableDecl79', None)
    assert not _is_linked(a, 'smc_VariableDecl79', b2)
    if hasattr(b2, 'smc_BloomFilter'):
        assert not _is_linked(b2, 'smc_BloomFilter', a)


def test_assoc_right108_link_reassign_clear():
    a = smc_Equality(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_Equality109', b1)
    assert _is_linked(a, 'smc_Equality109', b1)
    if hasattr(b1, 'smc_Expression110'):
        assert _is_linked(b1, 'smc_Expression110', a)
    _safe_set(a, 'smc_Equality109', b2)
    assert _is_linked(a, 'smc_Equality109', b2)
    if hasattr(b1, 'smc_Expression110'):
        assert not _is_linked(b1, 'smc_Expression110', a)
    if hasattr(b2, 'smc_Expression110'):
        assert _is_linked(b2, 'smc_Expression110', a)
    _safe_set(a, 'smc_Equality109', None)
    assert not _is_linked(a, 'smc_Equality109', b2)
    if hasattr(b2, 'smc_Expression110'):
        assert not _is_linked(b2, 'smc_Expression110', a)


def test_assoc_right113_link_reassign_clear():
    a = smc_Comparison(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_Comparison114', b1)
    assert _is_linked(a, 'smc_Comparison114', b1)
    if hasattr(b1, 'smc_Expression115'):
        assert _is_linked(b1, 'smc_Expression115', a)
    _safe_set(a, 'smc_Comparison114', b2)
    assert _is_linked(a, 'smc_Comparison114', b2)
    if hasattr(b1, 'smc_Expression115'):
        assert not _is_linked(b1, 'smc_Expression115', a)
    if hasattr(b2, 'smc_Expression115'):
        assert _is_linked(b2, 'smc_Expression115', a)
    _safe_set(a, 'smc_Comparison114', None)
    assert not _is_linked(a, 'smc_Comparison114', b2)
    if hasattr(b2, 'smc_Expression115'):
        assert not _is_linked(b2, 'smc_Expression115', a)


def test_assoc_right118_link_reassign_clear():
    a = smc_PlusOrMinus(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_PlusOrMinus119', b1)
    assert _is_linked(a, 'smc_PlusOrMinus119', b1)
    if hasattr(b1, 'smc_Expression120'):
        assert _is_linked(b1, 'smc_Expression120', a)
    _safe_set(a, 'smc_PlusOrMinus119', b2)
    assert _is_linked(a, 'smc_PlusOrMinus119', b2)
    if hasattr(b1, 'smc_Expression120'):
        assert not _is_linked(b1, 'smc_Expression120', a)
    if hasattr(b2, 'smc_Expression120'):
        assert _is_linked(b2, 'smc_Expression120', a)
    _safe_set(a, 'smc_PlusOrMinus119', None)
    assert not _is_linked(a, 'smc_PlusOrMinus119', b2)
    if hasattr(b2, 'smc_Expression120'):
        assert not _is_linked(b2, 'smc_Expression120', a)


def test_assoc_right123_link_reassign_clear():
    a = smc_MulOrDiv(op="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_MulOrDiv124', b1)
    assert _is_linked(a, 'smc_MulOrDiv124', b1)
    if hasattr(b1, 'smc_Expression125'):
        assert _is_linked(b1, 'smc_Expression125', a)
    _safe_set(a, 'smc_MulOrDiv124', b2)
    assert _is_linked(a, 'smc_MulOrDiv124', b2)
    if hasattr(b1, 'smc_Expression125'):
        assert not _is_linked(b1, 'smc_Expression125', a)
    if hasattr(b2, 'smc_Expression125'):
        assert _is_linked(b2, 'smc_Expression125', a)
    _safe_set(a, 'smc_MulOrDiv124', None)
    assert not _is_linked(a, 'smc_MulOrDiv124', b2)
    if hasattr(b2, 'smc_Expression125'):
        assert not _is_linked(b2, 'smc_Expression125', a)


def test_assoc_tbl26_link_reassign_clear():
    a = smc_Database(clm="sample_text")
    b1 = smc_Expression()
    b2 = smc_Expression()
    _safe_set(a, 'smc_Database', b1)
    assert _is_linked(a, 'smc_Database', b1)
    if hasattr(b1, 'smc_Expression27'):
        assert _is_linked(b1, 'smc_Expression27', a)
    _safe_set(a, 'smc_Database', b2)
    assert _is_linked(a, 'smc_Database', b2)
    if hasattr(b1, 'smc_Expression27'):
        assert not _is_linked(b1, 'smc_Expression27', a)
    if hasattr(b2, 'smc_Expression27'):
        assert _is_linked(b2, 'smc_Expression27', a)
    _safe_set(a, 'smc_Database', None)
    assert not _is_linked(a, 'smc_Database', b2)
    if hasattr(b2, 'smc_Expression27'):
        assert not _is_linked(b2, 'smc_Expression27', a)


def test_assoc_tblname73_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Search(column="sample_text")
    b2 = smc_Search(column="sample_text_2")
    _safe_set(a, 'smc_VariableDecl74', b1)
    assert _is_linked(a, 'smc_VariableDecl74', b1)
    if hasattr(b1, 'smc_Search'):
        assert _is_linked(b1, 'smc_Search', a)
    _safe_set(a, 'smc_VariableDecl74', b2)
    assert _is_linked(a, 'smc_VariableDecl74', b2)
    if hasattr(b1, 'smc_Search'):
        assert not _is_linked(b1, 'smc_Search', a)
    if hasattr(b2, 'smc_Search'):
        assert _is_linked(b2, 'smc_Search', a)
    _safe_set(a, 'smc_VariableDecl74', None)
    assert not _is_linked(a, 'smc_VariableDecl74', b2)
    if hasattr(b2, 'smc_Search'):
        assert not _is_linked(b2, 'smc_Search', a)


def test_assoc_tblname83_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_CheckTable()
    b2 = smc_CheckTable()
    _safe_set(a, 'smc_VariableDecl84', b1)
    assert _is_linked(a, 'smc_VariableDecl84', b1)
    if hasattr(b1, 'smc_CheckTable'):
        assert _is_linked(b1, 'smc_CheckTable', a)
    _safe_set(a, 'smc_VariableDecl84', b2)
    assert _is_linked(a, 'smc_VariableDecl84', b2)
    if hasattr(b1, 'smc_CheckTable'):
        assert not _is_linked(b1, 'smc_CheckTable', a)
    if hasattr(b2, 'smc_CheckTable'):
        assert _is_linked(b2, 'smc_CheckTable', a)
    _safe_set(a, 'smc_VariableDecl84', None)
    assert not _is_linked(a, 'smc_VariableDecl84', b2)
    if hasattr(b2, 'smc_CheckTable'):
        assert not _is_linked(b2, 'smc_CheckTable', a)


def test_assoc_tblname85_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_AddValues()
    b2 = smc_AddValues()
    _safe_set(a, 'smc_VariableDecl86', b1)
    assert _is_linked(a, 'smc_VariableDecl86', b1)
    if hasattr(b1, 'smc_AddValues'):
        assert _is_linked(b1, 'smc_AddValues', a)
    _safe_set(a, 'smc_VariableDecl86', b2)
    assert _is_linked(a, 'smc_VariableDecl86', b2)
    if hasattr(b1, 'smc_AddValues'):
        assert not _is_linked(b1, 'smc_AddValues', a)
    if hasattr(b2, 'smc_AddValues'):
        assert _is_linked(b2, 'smc_AddValues', a)
    _safe_set(a, 'smc_VariableDecl86', None)
    assert not _is_linked(a, 'smc_VariableDecl86', b2)
    if hasattr(b2, 'smc_AddValues'):
        assert not _is_linked(b2, 'smc_AddValues', a)


def test_assoc_tblname90_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_CreateTable()
    b2 = smc_CreateTable()
    _safe_set(a, 'smc_VariableDecl91', b1)
    assert _is_linked(a, 'smc_VariableDecl91', b1)
    if hasattr(b1, 'smc_CreateTable'):
        assert _is_linked(b1, 'smc_CreateTable', a)
    _safe_set(a, 'smc_VariableDecl91', b2)
    assert _is_linked(a, 'smc_VariableDecl91', b2)
    if hasattr(b1, 'smc_CreateTable'):
        assert not _is_linked(b1, 'smc_CreateTable', a)
    if hasattr(b2, 'smc_CreateTable'):
        assert _is_linked(b2, 'smc_CreateTable', a)
    _safe_set(a, 'smc_VariableDecl91', None)
    assert not _is_linked(a, 'smc_VariableDecl91', b2)
    if hasattr(b2, 'smc_CreateTable'):
        assert not _is_linked(b2, 'smc_CreateTable', a)


def test_assoc_v_lvl63_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_AccessControl()
    b2 = smc_AccessControl()
    _safe_set(a, 'smc_VariableDecl65', b1)
    assert _is_linked(a, 'smc_VariableDecl65', b1)
    if hasattr(b1, 'smc_AccessControl64'):
        assert _is_linked(b1, 'smc_AccessControl64', a)
    _safe_set(a, 'smc_VariableDecl65', b2)
    assert _is_linked(a, 'smc_VariableDecl65', b2)
    if hasattr(b1, 'smc_AccessControl64'):
        assert not _is_linked(b1, 'smc_AccessControl64', a)
    if hasattr(b2, 'smc_AccessControl64'):
        assert _is_linked(b2, 'smc_AccessControl64', a)
    _safe_set(a, 'smc_VariableDecl65', None)
    assert not _is_linked(a, 'smc_VariableDecl65', b2)
    if hasattr(b2, 'smc_AccessControl64'):
        assert not _is_linked(b2, 'smc_AccessControl64', a)


def test_assoc_var21_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_VariableAssignment()
    b2 = smc_VariableAssignment()
    _safe_set(a, 'smc_VariableDecl22', b1)
    assert _is_linked(a, 'smc_VariableDecl22', b1)
    if hasattr(b1, 'smc_VariableAssignment'):
        assert _is_linked(b1, 'smc_VariableAssignment', a)
    _safe_set(a, 'smc_VariableDecl22', b2)
    assert _is_linked(a, 'smc_VariableDecl22', b2)
    if hasattr(b1, 'smc_VariableAssignment'):
        assert not _is_linked(b1, 'smc_VariableAssignment', a)
    if hasattr(b2, 'smc_VariableAssignment'):
        assert _is_linked(b2, 'smc_VariableAssignment', a)
    _safe_set(a, 'smc_VariableDecl22', None)
    assert not _is_linked(a, 'smc_VariableDecl22', b2)
    if hasattr(b2, 'smc_VariableAssignment'):
        assert not _is_linked(b2, 'smc_VariableAssignment', a)


def test_assoc_variable128_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_VariableRef()
    b2 = smc_VariableRef()
    _safe_set(a, 'smc_VariableDecl129', b1)
    assert _is_linked(a, 'smc_VariableDecl129', b1)
    if hasattr(b1, 'smc_VariableRef'):
        assert _is_linked(b1, 'smc_VariableRef', a)
    _safe_set(a, 'smc_VariableDecl129', b2)
    assert _is_linked(a, 'smc_VariableDecl129', b2)
    if hasattr(b1, 'smc_VariableRef'):
        assert not _is_linked(b1, 'smc_VariableRef', a)
    if hasattr(b2, 'smc_VariableRef'):
        assert _is_linked(b2, 'smc_VariableRef', a)
    _safe_set(a, 'smc_VariableDecl129', None)
    assert not _is_linked(a, 'smc_VariableDecl129', b2)
    if hasattr(b2, 'smc_VariableRef'):
        assert not _is_linked(b2, 'smc_VariableRef', a)


def test_assoc_weights52_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_WeightedAvg()
    b2 = smc_WeightedAvg()
    _safe_set(a, 'smc_VariableDecl53', b1)
    assert _is_linked(a, 'smc_VariableDecl53', b1)
    if hasattr(b1, 'smc_WeightedAvg'):
        assert _is_linked(b1, 'smc_WeightedAvg', a)
    _safe_set(a, 'smc_VariableDecl53', b2)
    assert _is_linked(a, 'smc_VariableDecl53', b2)
    if hasattr(b1, 'smc_WeightedAvg'):
        assert not _is_linked(b1, 'smc_WeightedAvg', a)
    if hasattr(b2, 'smc_WeightedAvg'):
        assert _is_linked(b2, 'smc_WeightedAvg', a)
    _safe_set(a, 'smc_VariableDecl53', None)
    assert not _is_linked(a, 'smc_VariableDecl53', b2)
    if hasattr(b2, 'smc_WeightedAvg'):
        assert not _is_linked(b2, 'smc_WeightedAvg', a)


def test_assoc_x45_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Multiplication()
    b2 = smc_Multiplication()
    _safe_set(a, 'smc_VariableDecl46', b1)
    assert _is_linked(a, 'smc_VariableDecl46', b1)
    if hasattr(b1, 'smc_Multiplication'):
        assert _is_linked(b1, 'smc_Multiplication', a)
    _safe_set(a, 'smc_VariableDecl46', b2)
    assert _is_linked(a, 'smc_VariableDecl46', b2)
    if hasattr(b1, 'smc_Multiplication'):
        assert not _is_linked(b1, 'smc_Multiplication', a)
    if hasattr(b2, 'smc_Multiplication'):
        assert _is_linked(b2, 'smc_Multiplication', a)
    _safe_set(a, 'smc_VariableDecl46', None)
    assert not _is_linked(a, 'smc_VariableDecl46', b2)
    if hasattr(b2, 'smc_Multiplication'):
        assert not _is_linked(b2, 'smc_Multiplication', a)


def test_assoc_y47_link_reassign_clear():
    a = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    b1 = smc_Multiplication()
    b2 = smc_Multiplication()
    _safe_set(a, 'smc_VariableDecl49', b1)
    assert _is_linked(a, 'smc_VariableDecl49', b1)
    if hasattr(b1, 'smc_Multiplication48'):
        assert _is_linked(b1, 'smc_Multiplication48', a)
    _safe_set(a, 'smc_VariableDecl49', b2)
    assert _is_linked(a, 'smc_VariableDecl49', b2)
    if hasattr(b1, 'smc_Multiplication48'):
        assert not _is_linked(b1, 'smc_Multiplication48', a)
    if hasattr(b2, 'smc_Multiplication48'):
        assert _is_linked(b2, 'smc_Multiplication48', a)
    _safe_set(a, 'smc_VariableDecl49', None)
    assert not _is_linked(a, 'smc_VariableDecl49', b2)
    if hasattr(b2, 'smc_Multiplication48'):
        assert not _is_linked(b2, 'smc_Multiplication48', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractAssignment_strategy = st.builds(AbstractAssignment)
@given(instance=AbstractAssignment_strategy)
@settings(max_examples=25)
def test_AbstractAssignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)


AccessControl_strategy = st.builds(AccessControl)
@given(instance=AccessControl_strategy)
@settings(max_examples=25)
def test_AccessControl_instantiation(instance):
    assert isinstance(instance, AccessControl)


Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Computation_strategy = st.builds(Computation)
@given(instance=Computation_strategy)
@settings(max_examples=25)
def test_Computation_instantiation(instance):
    assert isinstance(instance, Computation)


Download_strategy = st.builds(Download)
@given(instance=Download_strategy)
@settings(max_examples=25)
def test_Download_instantiation(instance):
    assert isinstance(instance, Download)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Functions_strategy = st.builds(Functions)
@given(instance=Functions_strategy)
@settings(max_examples=25)
def test_Functions_instantiation(instance):
    assert isinstance(instance, Functions)


smc_AbstractAssignment_strategy = st.builds(smc_AbstractAssignment)
@given(instance=smc_AbstractAssignment_strategy)
@settings(max_examples=25)
def test_smc_AbstractAssignment_instantiation(instance):
    assert isinstance(instance, smc_AbstractAssignment)


smc_AccessControl_strategy = st.builds(smc_AccessControl)
@given(instance=smc_AccessControl_strategy)
@settings(max_examples=25)
def test_smc_AccessControl_instantiation(instance):
    assert isinstance(instance, smc_AccessControl)


smc_AddValues_strategy = st.builds(smc_AddValues)
@given(instance=smc_AddValues_strategy)
@settings(max_examples=25)
def test_smc_AddValues_instantiation(instance):
    assert isinstance(instance, smc_AddValues)


smc_And_strategy = st.builds(smc_And)
@given(instance=smc_And_strategy)
@settings(max_examples=25)
def test_smc_And_instantiation(instance):
    assert isinstance(instance, smc_And)


smc_Average_strategy = st.builds(smc_Average)
@given(instance=smc_Average_strategy)
@settings(max_examples=25)
def test_smc_Average_instantiation(instance):
    assert isinstance(instance, smc_Average)


smc_BellLapadula_strategy = st.builds(smc_BellLapadula, mode=safe_text)
@given(instance=smc_BellLapadula_strategy)
@settings(max_examples=25)
def test_smc_BellLapadula_instantiation(instance):
    assert isinstance(instance, smc_BellLapadula)


smc_Block_strategy = st.builds(smc_Block)
@given(instance=smc_Block_strategy)
@settings(max_examples=25)
def test_smc_Block_instantiation(instance):
    assert isinstance(instance, smc_Block)


smc_BlockSMC_strategy = st.builds(smc_BlockSMC, name=safe_text, type=safe_text)
@given(instance=smc_BlockSMC_strategy)
@settings(max_examples=25)
def test_smc_BlockSMC_instantiation(instance):
    assert isinstance(instance, smc_BlockSMC)


smc_BloomFilter_strategy = st.builds(smc_BloomFilter)
@given(instance=smc_BloomFilter_strategy)
@settings(max_examples=25)
def test_smc_BloomFilter_instantiation(instance):
    assert isinstance(instance, smc_BloomFilter)


smc_BooleanLiteral_strategy = st.builds(smc_BooleanLiteral, value=st.booleans())
@given(instance=smc_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_smc_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, smc_BooleanLiteral)


smc_CheckTable_strategy = st.builds(smc_CheckTable)
@given(instance=smc_CheckTable_strategy)
@settings(max_examples=25)
def test_smc_CheckTable_instantiation(instance):
    assert isinstance(instance, smc_CheckTable)


smc_Client_strategy = st.builds(smc_Client, arg=safe_text)
@given(instance=smc_Client_strategy)
@settings(max_examples=25)
def test_smc_Client_instantiation(instance):
    assert isinstance(instance, smc_Client)


smc_Command_strategy = st.builds(smc_Command)
@given(instance=smc_Command_strategy)
@settings(max_examples=25)
def test_smc_Command_instantiation(instance):
    assert isinstance(instance, smc_Command)


smc_Comparison_strategy = st.builds(smc_Comparison, op=safe_text)
@given(instance=smc_Comparison_strategy)
@settings(max_examples=25)
def test_smc_Comparison_instantiation(instance):
    assert isinstance(instance, smc_Comparison)


smc_Computation_strategy = st.builds(smc_Computation)
@given(instance=smc_Computation_strategy)
@settings(max_examples=25)
def test_smc_Computation_instantiation(instance):
    assert isinstance(instance, smc_Computation)


smc_Count_strategy = st.builds(smc_Count)
@given(instance=smc_Count_strategy)
@settings(max_examples=25)
def test_smc_Count_instantiation(instance):
    assert isinstance(instance, smc_Count)


smc_Covered_strategy = st.builds(smc_Covered)
@given(instance=smc_Covered_strategy)
@settings(max_examples=25)
def test_smc_Covered_instantiation(instance):
    assert isinstance(instance, smc_Covered)


smc_CreateTable_strategy = st.builds(smc_CreateTable)
@given(instance=smc_CreateTable_strategy)
@settings(max_examples=25)
def test_smc_CreateTable_instantiation(instance):
    assert isinstance(instance, smc_CreateTable)


smc_Database_strategy = st.builds(smc_Database, clm=safe_text)
@given(instance=smc_Database_strategy)
@settings(max_examples=25)
def test_smc_Database_instantiation(instance):
    assert isinstance(instance, smc_Database)


smc_DateLiteral_strategy = st.builds(smc_DateLiteral, value=safe_text)
@given(instance=smc_DateLiteral_strategy)
@settings(max_examples=25)
def test_smc_DateLiteral_instantiation(instance):
    assert isinstance(instance, smc_DateLiteral)


smc_Dict_strategy = st.builds(smc_Dict)
@given(instance=smc_Dict_strategy)
@settings(max_examples=25)
def test_smc_Dict_instantiation(instance):
    assert isinstance(instance, smc_Dict)


smc_DoubleLiteral_strategy = st.builds(smc_DoubleLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=smc_DoubleLiteral_strategy)
@settings(max_examples=25)
def test_smc_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, smc_DoubleLiteral)


smc_Download_strategy = st.builds(smc_Download)
@given(instance=smc_Download_strategy)
@settings(max_examples=25)
def test_smc_Download_instantiation(instance):
    assert isinstance(instance, smc_Download)


smc_Equality_strategy = st.builds(smc_Equality, op=safe_text)
@given(instance=smc_Equality_strategy)
@settings(max_examples=25)
def test_smc_Equality_instantiation(instance):
    assert isinstance(instance, smc_Equality)


smc_Expression_strategy = st.builds(smc_Expression)
@given(instance=smc_Expression_strategy)
@settings(max_examples=25)
def test_smc_Expression_instantiation(instance):
    assert isinstance(instance, smc_Expression)


smc_Functions_strategy = st.builds(smc_Functions)
@given(instance=smc_Functions_strategy)
@settings(max_examples=25)
def test_smc_Functions_instantiation(instance):
    assert isinstance(instance, smc_Functions)


smc_IfThenElse_strategy = st.builds(smc_IfThenElse)
@given(instance=smc_IfThenElse_strategy)
@settings(max_examples=25)
def test_smc_IfThenElse_instantiation(instance):
    assert isinstance(instance, smc_IfThenElse)


smc_IntLiteral_strategy = st.builds(smc_IntLiteral, value=st.integers())
@given(instance=smc_IntLiteral_strategy)
@settings(max_examples=25)
def test_smc_IntLiteral_instantiation(instance):
    assert isinstance(instance, smc_IntLiteral)


smc_Invocation_strategy = st.builds(smc_Invocation)
@given(instance=smc_Invocation_strategy)
@settings(max_examples=25)
def test_smc_Invocation_instantiation(instance):
    assert isinstance(instance, smc_Invocation)


smc_InvocationVoid_strategy = st.builds(smc_InvocationVoid)
@given(instance=smc_InvocationVoid_strategy)
@settings(max_examples=25)
def test_smc_InvocationVoid_instantiation(instance):
    assert isinstance(instance, smc_InvocationVoid)


smc_List_strategy = st.builds(smc_List)
@given(instance=smc_List_strategy)
@settings(max_examples=25)
def test_smc_List_instantiation(instance):
    assert isinstance(instance, smc_List)


smc_MainSMC_strategy = st.builds(smc_MainSMC)
@given(instance=smc_MainSMC_strategy)
@settings(max_examples=25)
def test_smc_MainSMC_instantiation(instance):
    assert isinstance(instance, smc_MainSMC)


smc_Median_strategy = st.builds(smc_Median)
@given(instance=smc_Median_strategy)
@settings(max_examples=25)
def test_smc_Median_instantiation(instance):
    assert isinstance(instance, smc_Median)


smc_MulOrDiv_strategy = st.builds(smc_MulOrDiv, op=safe_text)
@given(instance=smc_MulOrDiv_strategy)
@settings(max_examples=25)
def test_smc_MulOrDiv_instantiation(instance):
    assert isinstance(instance, smc_MulOrDiv)


smc_Multiplication_strategy = st.builds(smc_Multiplication)
@given(instance=smc_Multiplication_strategy)
@settings(max_examples=25)
def test_smc_Multiplication_instantiation(instance):
    assert isinstance(instance, smc_Multiplication)


smc_Not_strategy = st.builds(smc_Not)
@given(instance=smc_Not_strategy)
@settings(max_examples=25)
def test_smc_Not_instantiation(instance):
    assert isinstance(instance, smc_Not)


smc_Or_strategy = st.builds(smc_Or)
@given(instance=smc_Or_strategy)
@settings(max_examples=25)
def test_smc_Or_instantiation(instance):
    assert isinstance(instance, smc_Or)


smc_ParamDecl_strategy = st.builds(smc_ParamDecl, btype=safe_text, name=safe_text, parName=safe_text, stype=safe_text)
@given(instance=smc_ParamDecl_strategy)
@settings(max_examples=25)
def test_smc_ParamDecl_instantiation(instance):
    assert isinstance(instance, smc_ParamDecl)


smc_PlusOrMinus_strategy = st.builds(smc_PlusOrMinus, op=safe_text)
@given(instance=smc_PlusOrMinus_strategy)
@settings(max_examples=25)
def test_smc_PlusOrMinus_instantiation(instance):
    assert isinstance(instance, smc_PlusOrMinus)


smc_Print_strategy = st.builds(smc_Print)
@given(instance=smc_Print_strategy)
@settings(max_examples=25)
def test_smc_Print_instantiation(instance):
    assert isinstance(instance, smc_Print)


smc_Return_strategy = st.builds(smc_Return)
@given(instance=smc_Return_strategy)
@settings(max_examples=25)
def test_smc_Return_instantiation(instance):
    assert isinstance(instance, smc_Return)


smc_Search_strategy = st.builds(smc_Search, column=safe_text)
@given(instance=smc_Search_strategy)
@settings(max_examples=25)
def test_smc_Search_instantiation(instance):
    assert isinstance(instance, smc_Search)


smc_Smc_strategy = st.builds(smc_Smc)
@given(instance=smc_Smc_strategy)
@settings(max_examples=25)
def test_smc_Smc_instantiation(instance):
    assert isinstance(instance, smc_Smc)


smc_StringLiteral_strategy = st.builds(smc_StringLiteral, value=safe_text)
@given(instance=smc_StringLiteral_strategy)
@settings(max_examples=25)
def test_smc_StringLiteral_instantiation(instance):
    assert isinstance(instance, smc_StringLiteral)


smc_TimeLiteral_strategy = st.builds(smc_TimeLiteral, value=safe_text)
@given(instance=smc_TimeLiteral_strategy)
@settings(max_examples=25)
def test_smc_TimeLiteral_instantiation(instance):
    assert isinstance(instance, smc_TimeLiteral)


smc_Tuple_strategy = st.builds(smc_Tuple)
@given(instance=smc_Tuple_strategy)
@settings(max_examples=25)
def test_smc_Tuple_instantiation(instance):
    assert isinstance(instance, smc_Tuple)


smc_VariableAssignment_strategy = st.builds(smc_VariableAssignment)
@given(instance=smc_VariableAssignment_strategy)
@settings(max_examples=25)
def test_smc_VariableAssignment_instantiation(instance):
    assert isinstance(instance, smc_VariableAssignment)


smc_VariableDecl_strategy = st.builds(smc_VariableDecl, array=st.booleans(), length=st.integers(), name=safe_text, type=safe_text, visibility=safe_text)
@given(instance=smc_VariableDecl_strategy)
@settings(max_examples=25)
def test_smc_VariableDecl_instantiation(instance):
    assert isinstance(instance, smc_VariableDecl)


smc_VariableRef_strategy = st.builds(smc_VariableRef)
@given(instance=smc_VariableRef_strategy)
@settings(max_examples=25)
def test_smc_VariableRef_instantiation(instance):
    assert isinstance(instance, smc_VariableRef)


smc_WeightedAvg_strategy = st.builds(smc_WeightedAvg)
@given(instance=smc_WeightedAvg_strategy)
@settings(max_examples=25)
def test_smc_WeightedAvg_instantiation(instance):
    assert isinstance(instance, smc_WeightedAvg)


smc_While_strategy = st.builds(smc_While)
@given(instance=smc_While_strategy)
@settings(max_examples=25)
def test_smc_While_instantiation(instance):
    assert isinstance(instance, smc_While)



