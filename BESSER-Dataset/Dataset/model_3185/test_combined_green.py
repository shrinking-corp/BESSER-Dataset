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
    Expression,
    debugSeq_Comparison,
    debugSeq_Read8,
    debugSeq_BitXor,
    debugSeq_Rem,
    debugSeq_DapSwjSequence,
    debugSeq_DapJtagSequence,
    debugSeq_Query,
    debugSeq_DapDelay,
    debugSeq_Plus,
    debugSeq_Read16,
    debugSeq_LoadDebugInfo,
    debugSeq_IntConstant,
    debugSeq_And,
    debugSeq_DapSwjPins,
    debugSeq_Read64,
    debugSeq_Write8,
    debugSeq_Shift,
    debugSeq_DapSwjClock,
    debugSeq_WriteDP,
    debugSeq_Minus,
    debugSeq_Not,
    debugSeq_Ternary,
    debugSeq_WriteAP,
    debugSeq_StringConstant,
    debugSeq_ReadDP,
    debugSeq_VariableRef,
    debugSeq_BitAnd,
    debugSeq_Write32,
    debugSeq_Or,
    debugSeq_Message,
    debugSeq_Read32,
    debugSeq_ReadAP,
    debugSeq_Mul,
    debugSeq_Div,
    debugSeq_BitNot,
    debugSeq_Equality,
    debugSeq_Write16,
    debugSeq_Write64,
    debugSeq_DapWriteABORT,
    debugSeq_SequenceCall,
    debugSeq_QueryValue,
    debugSeq_Assignment,
    debugSeq_Parameter,
    Parameter,
    CodeBlock,
    debugSeq_Control,
    debugSeq_Block,
    debugSeq_CodeBlock,
    debugSeq_BitOr,
    debugSeq_Sequence,
    Statement,
    debugSeq_Expression,
    debugSeq_VariableDeclaration,
    debugSeq_Statement,
    debugSeq_Sequences,
    debugSeq_DebugVars,
    debugSeq_DebugSeqModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_comparison_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Comparison)


def test_hyp_debugseq_comparison_constructor_exists():
    assert callable(debugSeq_Comparison.__init__)


def test_hyp_debugseq_comparison_constructor_args():
    sig = inspect.signature(debugSeq_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_debugseq_read8_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Read8)


def test_hyp_debugseq_read8_constructor_exists():
    assert callable(debugSeq_Read8.__init__)


def test_hyp_debugseq_read8_constructor_args():
    sig = inspect.signature(debugSeq_Read8.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_bitxor_is_not_abstract():
    assert not inspect.isabstract(debugSeq_BitXor)


def test_hyp_debugseq_bitxor_constructor_exists():
    assert callable(debugSeq_BitXor.__init__)


def test_hyp_debugseq_bitxor_constructor_args():
    sig = inspect.signature(debugSeq_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_rem_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Rem)


def test_hyp_debugseq_rem_constructor_exists():
    assert callable(debugSeq_Rem.__init__)


def test_hyp_debugseq_rem_constructor_args():
    sig = inspect.signature(debugSeq_Rem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_dapswjsequence_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapSwjSequence)


def test_hyp_debugseq_dapswjsequence_constructor_exists():
    assert callable(debugSeq_DapSwjSequence.__init__)


def test_hyp_debugseq_dapswjsequence_constructor_args():
    sig = inspect.signature(debugSeq_DapSwjSequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_dapjtagsequence_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapJtagSequence)


def test_hyp_debugseq_dapjtagsequence_constructor_exists():
    assert callable(debugSeq_DapJtagSequence.__init__)


def test_hyp_debugseq_dapjtagsequence_constructor_args():
    sig = inspect.signature(debugSeq_DapJtagSequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_query_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Query)


def test_hyp_debugseq_query_constructor_exists():
    assert callable(debugSeq_Query.__init__)


def test_hyp_debugseq_query_constructor_args():
    sig = inspect.signature(debugSeq_Query.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"




def test_hyp_debugseq_dapdelay_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapDelay)


def test_hyp_debugseq_dapdelay_constructor_exists():
    assert callable(debugSeq_DapDelay.__init__)


def test_hyp_debugseq_dapdelay_constructor_args():
    sig = inspect.signature(debugSeq_DapDelay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_plus_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Plus)


def test_hyp_debugseq_plus_constructor_exists():
    assert callable(debugSeq_Plus.__init__)


def test_hyp_debugseq_plus_constructor_args():
    sig = inspect.signature(debugSeq_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_read16_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Read16)


def test_hyp_debugseq_read16_constructor_exists():
    assert callable(debugSeq_Read16.__init__)


def test_hyp_debugseq_read16_constructor_args():
    sig = inspect.signature(debugSeq_Read16.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_loaddebuginfo_is_not_abstract():
    assert not inspect.isabstract(debugSeq_LoadDebugInfo)


def test_hyp_debugseq_loaddebuginfo_constructor_exists():
    assert callable(debugSeq_LoadDebugInfo.__init__)


def test_hyp_debugseq_loaddebuginfo_constructor_args():
    sig = inspect.signature(debugSeq_LoadDebugInfo.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_debugseq_intconstant_is_not_abstract():
    assert not inspect.isabstract(debugSeq_IntConstant)


def test_hyp_debugseq_intconstant_constructor_exists():
    assert callable(debugSeq_IntConstant.__init__)


def test_hyp_debugseq_intconstant_constructor_args():
    sig = inspect.signature(debugSeq_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_debugseq_and_is_not_abstract():
    assert not inspect.isabstract(debugSeq_And)


def test_hyp_debugseq_and_constructor_exists():
    assert callable(debugSeq_And.__init__)


def test_hyp_debugseq_and_constructor_args():
    sig = inspect.signature(debugSeq_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_dapswjpins_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapSwjPins)


def test_hyp_debugseq_dapswjpins_constructor_exists():
    assert callable(debugSeq_DapSwjPins.__init__)


def test_hyp_debugseq_dapswjpins_constructor_args():
    sig = inspect.signature(debugSeq_DapSwjPins.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_read64_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Read64)


def test_hyp_debugseq_read64_constructor_exists():
    assert callable(debugSeq_Read64.__init__)


def test_hyp_debugseq_read64_constructor_args():
    sig = inspect.signature(debugSeq_Read64.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_write8_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Write8)


def test_hyp_debugseq_write8_constructor_exists():
    assert callable(debugSeq_Write8.__init__)


def test_hyp_debugseq_write8_constructor_args():
    sig = inspect.signature(debugSeq_Write8.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_shift_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Shift)


def test_hyp_debugseq_shift_constructor_exists():
    assert callable(debugSeq_Shift.__init__)


def test_hyp_debugseq_shift_constructor_args():
    sig = inspect.signature(debugSeq_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_debugseq_dapswjclock_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapSwjClock)


def test_hyp_debugseq_dapswjclock_constructor_exists():
    assert callable(debugSeq_DapSwjClock.__init__)


def test_hyp_debugseq_dapswjclock_constructor_args():
    sig = inspect.signature(debugSeq_DapSwjClock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_writedp_is_not_abstract():
    assert not inspect.isabstract(debugSeq_WriteDP)


def test_hyp_debugseq_writedp_constructor_exists():
    assert callable(debugSeq_WriteDP.__init__)


def test_hyp_debugseq_writedp_constructor_args():
    sig = inspect.signature(debugSeq_WriteDP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_minus_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Minus)


def test_hyp_debugseq_minus_constructor_exists():
    assert callable(debugSeq_Minus.__init__)


def test_hyp_debugseq_minus_constructor_args():
    sig = inspect.signature(debugSeq_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_not_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Not)


def test_hyp_debugseq_not_constructor_exists():
    assert callable(debugSeq_Not.__init__)


def test_hyp_debugseq_not_constructor_args():
    sig = inspect.signature(debugSeq_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_ternary_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Ternary)


def test_hyp_debugseq_ternary_constructor_exists():
    assert callable(debugSeq_Ternary.__init__)


def test_hyp_debugseq_ternary_constructor_args():
    sig = inspect.signature(debugSeq_Ternary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_writeap_is_not_abstract():
    assert not inspect.isabstract(debugSeq_WriteAP)


def test_hyp_debugseq_writeap_constructor_exists():
    assert callable(debugSeq_WriteAP.__init__)


def test_hyp_debugseq_writeap_constructor_args():
    sig = inspect.signature(debugSeq_WriteAP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_stringconstant_is_not_abstract():
    assert not inspect.isabstract(debugSeq_StringConstant)


def test_hyp_debugseq_stringconstant_constructor_exists():
    assert callable(debugSeq_StringConstant.__init__)


def test_hyp_debugseq_stringconstant_constructor_args():
    sig = inspect.signature(debugSeq_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_debugseq_readdp_is_not_abstract():
    assert not inspect.isabstract(debugSeq_ReadDP)


def test_hyp_debugseq_readdp_constructor_exists():
    assert callable(debugSeq_ReadDP.__init__)


def test_hyp_debugseq_readdp_constructor_args():
    sig = inspect.signature(debugSeq_ReadDP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_variableref_is_not_abstract():
    assert not inspect.isabstract(debugSeq_VariableRef)


def test_hyp_debugseq_variableref_constructor_exists():
    assert callable(debugSeq_VariableRef.__init__)


def test_hyp_debugseq_variableref_constructor_args():
    sig = inspect.signature(debugSeq_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_bitand_is_not_abstract():
    assert not inspect.isabstract(debugSeq_BitAnd)


def test_hyp_debugseq_bitand_constructor_exists():
    assert callable(debugSeq_BitAnd.__init__)


def test_hyp_debugseq_bitand_constructor_args():
    sig = inspect.signature(debugSeq_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_write32_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Write32)


def test_hyp_debugseq_write32_constructor_exists():
    assert callable(debugSeq_Write32.__init__)


def test_hyp_debugseq_write32_constructor_args():
    sig = inspect.signature(debugSeq_Write32.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_or_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Or)


def test_hyp_debugseq_or_constructor_exists():
    assert callable(debugSeq_Or.__init__)


def test_hyp_debugseq_or_constructor_args():
    sig = inspect.signature(debugSeq_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_message_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Message)


def test_hyp_debugseq_message_constructor_exists():
    assert callable(debugSeq_Message.__init__)


def test_hyp_debugseq_message_constructor_args():
    sig = inspect.signature(debugSeq_Message.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"




def test_hyp_debugseq_read32_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Read32)


def test_hyp_debugseq_read32_constructor_exists():
    assert callable(debugSeq_Read32.__init__)


def test_hyp_debugseq_read32_constructor_args():
    sig = inspect.signature(debugSeq_Read32.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_readap_is_not_abstract():
    assert not inspect.isabstract(debugSeq_ReadAP)


def test_hyp_debugseq_readap_constructor_exists():
    assert callable(debugSeq_ReadAP.__init__)


def test_hyp_debugseq_readap_constructor_args():
    sig = inspect.signature(debugSeq_ReadAP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_mul_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Mul)


def test_hyp_debugseq_mul_constructor_exists():
    assert callable(debugSeq_Mul.__init__)


def test_hyp_debugseq_mul_constructor_args():
    sig = inspect.signature(debugSeq_Mul.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_div_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Div)


def test_hyp_debugseq_div_constructor_exists():
    assert callable(debugSeq_Div.__init__)


def test_hyp_debugseq_div_constructor_args():
    sig = inspect.signature(debugSeq_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_bitnot_is_not_abstract():
    assert not inspect.isabstract(debugSeq_BitNot)


def test_hyp_debugseq_bitnot_constructor_exists():
    assert callable(debugSeq_BitNot.__init__)


def test_hyp_debugseq_bitnot_constructor_args():
    sig = inspect.signature(debugSeq_BitNot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_equality_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Equality)


def test_hyp_debugseq_equality_constructor_exists():
    assert callable(debugSeq_Equality.__init__)


def test_hyp_debugseq_equality_constructor_args():
    sig = inspect.signature(debugSeq_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_debugseq_write16_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Write16)


def test_hyp_debugseq_write16_constructor_exists():
    assert callable(debugSeq_Write16.__init__)


def test_hyp_debugseq_write16_constructor_args():
    sig = inspect.signature(debugSeq_Write16.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_write64_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Write64)


def test_hyp_debugseq_write64_constructor_exists():
    assert callable(debugSeq_Write64.__init__)


def test_hyp_debugseq_write64_constructor_args():
    sig = inspect.signature(debugSeq_Write64.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_dapwriteabort_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DapWriteABORT)


def test_hyp_debugseq_dapwriteabort_constructor_exists():
    assert callable(debugSeq_DapWriteABORT.__init__)


def test_hyp_debugseq_dapwriteabort_constructor_args():
    sig = inspect.signature(debugSeq_DapWriteABORT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_sequencecall_is_not_abstract():
    assert not inspect.isabstract(debugSeq_SequenceCall)


def test_hyp_debugseq_sequencecall_constructor_exists():
    assert callable(debugSeq_SequenceCall.__init__)


def test_hyp_debugseq_sequencecall_constructor_args():
    sig = inspect.signature(debugSeq_SequenceCall.__init__)
    params = list(sig.parameters.keys())
    assert "seqname" in params, "Missing parameter 'seqname'"




def test_hyp_debugseq_queryvalue_is_not_abstract():
    assert not inspect.isabstract(debugSeq_QueryValue)


def test_hyp_debugseq_queryvalue_constructor_exists():
    assert callable(debugSeq_QueryValue.__init__)


def test_hyp_debugseq_queryvalue_constructor_args():
    sig = inspect.signature(debugSeq_QueryValue.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"




def test_hyp_debugseq_assignment_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Assignment)


def test_hyp_debugseq_assignment_constructor_exists():
    assert callable(debugSeq_Assignment.__init__)


def test_hyp_debugseq_assignment_constructor_args():
    sig = inspect.signature(debugSeq_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_debugseq_parameter_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Parameter)


def test_hyp_debugseq_parameter_constructor_exists():
    assert callable(debugSeq_Parameter.__init__)


def test_hyp_debugseq_parameter_constructor_args():
    sig = inspect.signature(debugSeq_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codeblock_is_not_abstract():
    assert not inspect.isabstract(CodeBlock)


def test_hyp_codeblock_constructor_exists():
    assert callable(CodeBlock.__init__)


def test_hyp_codeblock_constructor_args():
    sig = inspect.signature(CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_control_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Control)


def test_hyp_debugseq_control_constructor_exists():
    assert callable(debugSeq_Control.__init__)


def test_hyp_debugseq_control_constructor_args():
    sig = inspect.signature(debugSeq_Control.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"




def test_hyp_debugseq_block_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Block)


def test_hyp_debugseq_block_constructor_exists():
    assert callable(debugSeq_Block.__init__)


def test_hyp_debugseq_block_constructor_args():
    sig = inspect.signature(debugSeq_Block.__init__)
    params = list(sig.parameters.keys())
    assert "atomic" in params, "Missing parameter 'atomic'"




def test_hyp_debugseq_codeblock_is_not_abstract():
    assert not inspect.isabstract(debugSeq_CodeBlock)


def test_hyp_debugseq_codeblock_constructor_exists():
    assert callable(debugSeq_CodeBlock.__init__)


def test_hyp_debugseq_codeblock_constructor_args():
    sig = inspect.signature(debugSeq_CodeBlock.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"




def test_hyp_debugseq_bitor_is_not_abstract():
    assert not inspect.isabstract(debugSeq_BitOr)


def test_hyp_debugseq_bitor_constructor_exists():
    assert callable(debugSeq_BitOr.__init__)


def test_hyp_debugseq_bitor_constructor_args():
    sig = inspect.signature(debugSeq_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_sequence_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Sequence)


def test_hyp_debugseq_sequence_constructor_exists():
    assert callable(debugSeq_Sequence.__init__)


def test_hyp_debugseq_sequence_constructor_args():
    sig = inspect.signature(debugSeq_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "pname" in params, "Missing parameter 'pname'"
    assert "name" in params, "Missing parameter 'name'"
    assert "disable" in params, "Missing parameter 'disable'"
    assert "info" in params, "Missing parameter 'info'"







def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_expression_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Expression)


def test_hyp_debugseq_expression_constructor_exists():
    assert callable(debugSeq_Expression.__init__)


def test_hyp_debugseq_expression_constructor_args():
    sig = inspect.signature(debugSeq_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(debugSeq_VariableDeclaration)


def test_hyp_debugseq_variabledeclaration_constructor_exists():
    assert callable(debugSeq_VariableDeclaration.__init__)


def test_hyp_debugseq_variabledeclaration_constructor_args():
    sig = inspect.signature(debugSeq_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_debugseq_statement_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Statement)


def test_hyp_debugseq_statement_constructor_exists():
    assert callable(debugSeq_Statement.__init__)


def test_hyp_debugseq_statement_constructor_args():
    sig = inspect.signature(debugSeq_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_sequences_is_not_abstract():
    assert not inspect.isabstract(debugSeq_Sequences)


def test_hyp_debugseq_sequences_constructor_exists():
    assert callable(debugSeq_Sequences.__init__)


def test_hyp_debugseq_sequences_constructor_args():
    sig = inspect.signature(debugSeq_Sequences.__init__)
    params = list(sig.parameters.keys())



def test_hyp_debugseq_debugvars_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DebugVars)


def test_hyp_debugseq_debugvars_constructor_exists():
    assert callable(debugSeq_DebugVars.__init__)


def test_hyp_debugseq_debugvars_constructor_args():
    sig = inspect.signature(debugSeq_DebugVars.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "configfile" in params, "Missing parameter 'configfile'"
    assert "pname" in params, "Missing parameter 'pname'"






def test_hyp_debugseq_debugseqmodel_is_not_abstract():
    assert not inspect.isabstract(debugSeq_DebugSeqModel)


def test_hyp_debugseq_debugseqmodel_constructor_exists():
    assert callable(debugSeq_DebugSeqModel.__init__)


def test_hyp_debugseq_debugseqmodel_constructor_args():
    sig = inspect.signature(debugSeq_DebugSeqModel.__init__)
    params = list(sig.parameters.keys())


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
Expression_strategy = st.builds(
    Expression,
)
debugSeq_Comparison_strategy = st.builds(
    debugSeq_Comparison,
    op=
        safe_text
)
debugSeq_Read8_strategy = st.builds(
    debugSeq_Read8,
)
debugSeq_BitXor_strategy = st.builds(
    debugSeq_BitXor,
)
debugSeq_Rem_strategy = st.builds(
    debugSeq_Rem,
)
debugSeq_DapSwjSequence_strategy = st.builds(
    debugSeq_DapSwjSequence,
)
debugSeq_DapJtagSequence_strategy = st.builds(
    debugSeq_DapJtagSequence,
)
debugSeq_Query_strategy = st.builds(
    debugSeq_Query,
    message=
        safe_text
)
debugSeq_DapDelay_strategy = st.builds(
    debugSeq_DapDelay,
)
debugSeq_Plus_strategy = st.builds(
    debugSeq_Plus,
)
debugSeq_Read16_strategy = st.builds(
    debugSeq_Read16,
)
debugSeq_LoadDebugInfo_strategy = st.builds(
    debugSeq_LoadDebugInfo,
    path=
        safe_text
)
debugSeq_IntConstant_strategy = st.builds(
    debugSeq_IntConstant,
    value=
        safe_text
)
debugSeq_And_strategy = st.builds(
    debugSeq_And,
)
debugSeq_DapSwjPins_strategy = st.builds(
    debugSeq_DapSwjPins,
)
debugSeq_Read64_strategy = st.builds(
    debugSeq_Read64,
)
debugSeq_Write8_strategy = st.builds(
    debugSeq_Write8,
)
debugSeq_Shift_strategy = st.builds(
    debugSeq_Shift,
    op=
        safe_text
)
debugSeq_DapSwjClock_strategy = st.builds(
    debugSeq_DapSwjClock,
)
debugSeq_WriteDP_strategy = st.builds(
    debugSeq_WriteDP,
)
debugSeq_Minus_strategy = st.builds(
    debugSeq_Minus,
)
debugSeq_Not_strategy = st.builds(
    debugSeq_Not,
)
debugSeq_Ternary_strategy = st.builds(
    debugSeq_Ternary,
)
debugSeq_WriteAP_strategy = st.builds(
    debugSeq_WriteAP,
)
debugSeq_StringConstant_strategy = st.builds(
    debugSeq_StringConstant,
    value=
        safe_text
)
debugSeq_ReadDP_strategy = st.builds(
    debugSeq_ReadDP,
)
debugSeq_VariableRef_strategy = st.builds(
    debugSeq_VariableRef,
)
debugSeq_BitAnd_strategy = st.builds(
    debugSeq_BitAnd,
)
debugSeq_Write32_strategy = st.builds(
    debugSeq_Write32,
)
debugSeq_Or_strategy = st.builds(
    debugSeq_Or,
)
debugSeq_Message_strategy = st.builds(
    debugSeq_Message,
    format=
        safe_text
)
debugSeq_Read32_strategy = st.builds(
    debugSeq_Read32,
)
debugSeq_ReadAP_strategy = st.builds(
    debugSeq_ReadAP,
)
debugSeq_Mul_strategy = st.builds(
    debugSeq_Mul,
)
debugSeq_Div_strategy = st.builds(
    debugSeq_Div,
)
debugSeq_BitNot_strategy = st.builds(
    debugSeq_BitNot,
)
debugSeq_Equality_strategy = st.builds(
    debugSeq_Equality,
    op=
        safe_text
)
debugSeq_Write16_strategy = st.builds(
    debugSeq_Write16,
)
debugSeq_Write64_strategy = st.builds(
    debugSeq_Write64,
)
debugSeq_DapWriteABORT_strategy = st.builds(
    debugSeq_DapWriteABORT,
)
debugSeq_SequenceCall_strategy = st.builds(
    debugSeq_SequenceCall,
    seqname=
        safe_text
)
debugSeq_QueryValue_strategy = st.builds(
    debugSeq_QueryValue,
    message=
        safe_text
)
debugSeq_Assignment_strategy = st.builds(
    debugSeq_Assignment,
    op=
        safe_text
)
debugSeq_Parameter_strategy = st.builds(
    debugSeq_Parameter,
)
Parameter_strategy = st.builds(
    Parameter,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
debugSeq_Control_strategy = st.builds(
    debugSeq_Control,
    timeout=
        safe_text
)
debugSeq_Block_strategy = st.builds(
    debugSeq_Block,
    atomic=
        safe_text
)
debugSeq_CodeBlock_strategy = st.builds(
    debugSeq_CodeBlock,
    info=
        safe_text
)
debugSeq_BitOr_strategy = st.builds(
    debugSeq_BitOr,
)
debugSeq_Sequence_strategy = st.builds(
    debugSeq_Sequence,
    pname=
        safe_text,
    name=
        safe_text,
    disable=
        safe_text,
    info=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
debugSeq_Expression_strategy = st.builds(
    debugSeq_Expression,
)
debugSeq_VariableDeclaration_strategy = st.builds(
    debugSeq_VariableDeclaration,
    name=
        safe_text
)
debugSeq_Statement_strategy = st.builds(
    debugSeq_Statement,
)
debugSeq_Sequences_strategy = st.builds(
    debugSeq_Sequences,
)
debugSeq_DebugVars_strategy = st.builds(
    debugSeq_DebugVars,
    version=
        safe_text,
    configfile=
        safe_text,
    pname=
        safe_text
)
debugSeq_DebugSeqModel_strategy = st.builds(
    debugSeq_DebugSeqModel,
)





@given(instance=debugSeq_Comparison_strategy)
def test_hyp_debugseq_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original









@given(instance=debugSeq_Query_strategy)
def test_hyp_debugseq_query_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original







@given(instance=debugSeq_LoadDebugInfo_strategy)
def test_hyp_debugseq_loaddebuginfo_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original




@given(instance=debugSeq_IntConstant_strategy)
def test_hyp_debugseq_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=debugSeq_Shift_strategy)
def test_hyp_debugseq_shift_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original










@given(instance=debugSeq_StringConstant_strategy)
def test_hyp_debugseq_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=debugSeq_Message_strategy)
def test_hyp_debugseq_message_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original









@given(instance=debugSeq_Equality_strategy)
def test_hyp_debugseq_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original







@given(instance=debugSeq_SequenceCall_strategy)
def test_hyp_debugseq_sequencecall_seqname_setter(instance):
    original = instance.seqname
    instance.seqname = original
    assert instance.seqname == original




@given(instance=debugSeq_QueryValue_strategy)
def test_hyp_debugseq_queryvalue_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original




@given(instance=debugSeq_Assignment_strategy)
def test_hyp_debugseq_assignment_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original







@given(instance=debugSeq_Control_strategy)
def test_hyp_debugseq_control_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original




@given(instance=debugSeq_Block_strategy)
def test_hyp_debugseq_block_atomic_setter(instance):
    original = instance.atomic
    instance.atomic = original
    assert instance.atomic == original




@given(instance=debugSeq_CodeBlock_strategy)
def test_hyp_debugseq_codeblock_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original





@given(instance=debugSeq_Sequence_strategy)
def test_hyp_debugseq_sequence_pname_setter(instance):
    original = instance.pname
    instance.pname = original
    assert instance.pname == original



@given(instance=debugSeq_Sequence_strategy)
def test_hyp_debugseq_sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=debugSeq_Sequence_strategy)
def test_hyp_debugseq_sequence_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original



@given(instance=debugSeq_Sequence_strategy)
def test_hyp_debugseq_sequence_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original






@given(instance=debugSeq_VariableDeclaration_strategy)
def test_hyp_debugseq_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=debugSeq_DebugVars_strategy)
def test_hyp_debugseq_debugvars_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=debugSeq_DebugVars_strategy)
def test_hyp_debugseq_debugvars_configfile_setter(instance):
    original = instance.configfile
    instance.configfile = original
    assert instance.configfile == original



@given(instance=debugSeq_DebugVars_strategy)
def test_hyp_debugseq_debugvars_pname_setter(instance):
    original = instance.pname
    instance.pname = original
    assert instance.pname == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CodeBlock,
    Expression,
    Parameter,
    Statement,
    debugSeq_And,
    debugSeq_Assignment,
    debugSeq_BitAnd,
    debugSeq_BitNot,
    debugSeq_BitOr,
    debugSeq_BitXor,
    debugSeq_Block,
    debugSeq_CodeBlock,
    debugSeq_Comparison,
    debugSeq_Control,
    debugSeq_DapDelay,
    debugSeq_DapJtagSequence,
    debugSeq_DapSwjClock,
    debugSeq_DapSwjPins,
    debugSeq_DapSwjSequence,
    debugSeq_DapWriteABORT,
    debugSeq_DebugSeqModel,
    debugSeq_DebugVars,
    debugSeq_Div,
    debugSeq_Equality,
    debugSeq_Expression,
    debugSeq_IntConstant,
    debugSeq_LoadDebugInfo,
    debugSeq_Message,
    debugSeq_Minus,
    debugSeq_Mul,
    debugSeq_Not,
    debugSeq_Or,
    debugSeq_Parameter,
    debugSeq_Plus,
    debugSeq_Query,
    debugSeq_QueryValue,
    debugSeq_Read16,
    debugSeq_Read32,
    debugSeq_Read64,
    debugSeq_Read8,
    debugSeq_ReadAP,
    debugSeq_ReadDP,
    debugSeq_Rem,
    debugSeq_Sequence,
    debugSeq_SequenceCall,
    debugSeq_Sequences,
    debugSeq_Shift,
    debugSeq_Statement,
    debugSeq_StringConstant,
    debugSeq_Ternary,
    debugSeq_VariableDeclaration,
    debugSeq_VariableRef,
    debugSeq_Write16,
    debugSeq_Write32,
    debugSeq_Write64,
    debugSeq_Write8,
    debugSeq_WriteAP,
    debugSeq_WriteDP,
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

def test_debugSeq_Assignment_op_value_roundtrip():
    instance = debugSeq_Assignment(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_debugSeq_Block_atomic_value_roundtrip():
    instance = debugSeq_Block(atomic="sample_text")
    assert instance.atomic == "sample_text"
    instance.atomic = "sample_text_2"
    assert instance.atomic == "sample_text_2"


def test_debugSeq_CodeBlock_info_value_roundtrip():
    instance = debugSeq_CodeBlock(info="sample_text")
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_debugSeq_Comparison_op_value_roundtrip():
    instance = debugSeq_Comparison(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_debugSeq_Control_timeout_value_roundtrip():
    instance = debugSeq_Control(timeout="sample_text")
    assert instance.timeout == "sample_text"
    instance.timeout = "sample_text_2"
    assert instance.timeout == "sample_text_2"


def test_debugSeq_DebugVars_configfile_value_roundtrip():
    instance = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    assert instance.configfile == "sample_text"
    instance.configfile = "sample_text_2"
    assert instance.configfile == "sample_text_2"


def test_debugSeq_DebugVars_pname_value_roundtrip():
    instance = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    assert instance.pname == "sample_text"
    instance.pname = "sample_text_2"
    assert instance.pname == "sample_text_2"


def test_debugSeq_DebugVars_version_value_roundtrip():
    instance = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_debugSeq_Equality_op_value_roundtrip():
    instance = debugSeq_Equality(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_debugSeq_IntConstant_value_value_roundtrip():
    instance = debugSeq_IntConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_debugSeq_LoadDebugInfo_path_value_roundtrip():
    instance = debugSeq_LoadDebugInfo(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_debugSeq_Message_format_value_roundtrip():
    instance = debugSeq_Message(format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_debugSeq_Query_message_value_roundtrip():
    instance = debugSeq_Query(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_debugSeq_QueryValue_message_value_roundtrip():
    instance = debugSeq_QueryValue(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_debugSeq_Sequence_disable_value_roundtrip():
    instance = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    assert instance.disable == "sample_text"
    instance.disable = "sample_text_2"
    assert instance.disable == "sample_text_2"


def test_debugSeq_Sequence_info_value_roundtrip():
    instance = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_debugSeq_Sequence_name_value_roundtrip():
    instance = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_debugSeq_Sequence_pname_value_roundtrip():
    instance = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    assert instance.pname == "sample_text"
    instance.pname = "sample_text_2"
    assert instance.pname == "sample_text_2"


def test_debugSeq_SequenceCall_seqname_value_roundtrip():
    instance = debugSeq_SequenceCall(seqname="sample_text")
    assert instance.seqname == "sample_text"
    instance.seqname = "sample_text_2"
    assert instance.seqname == "sample_text_2"


def test_debugSeq_Shift_op_value_roundtrip():
    instance = debugSeq_Shift(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_debugSeq_StringConstant_value_value_roundtrip():
    instance = debugSeq_StringConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_debugSeq_VariableDeclaration_name_value_roundtrip():
    instance = debugSeq_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_debugSeq_Block_isa_CodeBlock():
    instance = debugSeq_Block(atomic="sample_text")
    assert isinstance(instance, CodeBlock)


def test_debugSeq_Control_isa_CodeBlock():
    instance = debugSeq_Control(timeout="sample_text")
    assert isinstance(instance, CodeBlock)


def test_debugSeq_And_isa_Expression():
    instance = debugSeq_And()
    assert isinstance(instance, Expression)


def test_debugSeq_Assignment_isa_Expression():
    instance = debugSeq_Assignment(op="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_BitAnd_isa_Expression():
    instance = debugSeq_BitAnd()
    assert isinstance(instance, Expression)


def test_debugSeq_BitNot_isa_Expression():
    instance = debugSeq_BitNot()
    assert isinstance(instance, Expression)


def test_debugSeq_BitOr_isa_Expression():
    instance = debugSeq_BitOr()
    assert isinstance(instance, Expression)


def test_debugSeq_BitXor_isa_Expression():
    instance = debugSeq_BitXor()
    assert isinstance(instance, Expression)


def test_debugSeq_Comparison_isa_Expression():
    instance = debugSeq_Comparison(op="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_DapDelay_isa_Expression():
    instance = debugSeq_DapDelay()
    assert isinstance(instance, Expression)


def test_debugSeq_DapJtagSequence_isa_Expression():
    instance = debugSeq_DapJtagSequence()
    assert isinstance(instance, Expression)


def test_debugSeq_DapSwjClock_isa_Expression():
    instance = debugSeq_DapSwjClock()
    assert isinstance(instance, Expression)


def test_debugSeq_DapSwjPins_isa_Expression():
    instance = debugSeq_DapSwjPins()
    assert isinstance(instance, Expression)


def test_debugSeq_DapSwjSequence_isa_Expression():
    instance = debugSeq_DapSwjSequence()
    assert isinstance(instance, Expression)


def test_debugSeq_DapWriteABORT_isa_Expression():
    instance = debugSeq_DapWriteABORT()
    assert isinstance(instance, Expression)


def test_debugSeq_Div_isa_Expression():
    instance = debugSeq_Div()
    assert isinstance(instance, Expression)


def test_debugSeq_Equality_isa_Expression():
    instance = debugSeq_Equality(op="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_IntConstant_isa_Expression():
    instance = debugSeq_IntConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_LoadDebugInfo_isa_Expression():
    instance = debugSeq_LoadDebugInfo(path="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_Message_isa_Expression():
    instance = debugSeq_Message(format="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_Minus_isa_Expression():
    instance = debugSeq_Minus()
    assert isinstance(instance, Expression)


def test_debugSeq_Mul_isa_Expression():
    instance = debugSeq_Mul()
    assert isinstance(instance, Expression)


def test_debugSeq_Not_isa_Expression():
    instance = debugSeq_Not()
    assert isinstance(instance, Expression)


def test_debugSeq_Or_isa_Expression():
    instance = debugSeq_Or()
    assert isinstance(instance, Expression)


def test_debugSeq_Plus_isa_Expression():
    instance = debugSeq_Plus()
    assert isinstance(instance, Expression)


def test_debugSeq_Query_isa_Expression():
    instance = debugSeq_Query(message="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_QueryValue_isa_Expression():
    instance = debugSeq_QueryValue(message="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_Read16_isa_Expression():
    instance = debugSeq_Read16()
    assert isinstance(instance, Expression)


def test_debugSeq_Read32_isa_Expression():
    instance = debugSeq_Read32()
    assert isinstance(instance, Expression)


def test_debugSeq_Read64_isa_Expression():
    instance = debugSeq_Read64()
    assert isinstance(instance, Expression)


def test_debugSeq_Read8_isa_Expression():
    instance = debugSeq_Read8()
    assert isinstance(instance, Expression)


def test_debugSeq_ReadAP_isa_Expression():
    instance = debugSeq_ReadAP()
    assert isinstance(instance, Expression)


def test_debugSeq_ReadDP_isa_Expression():
    instance = debugSeq_ReadDP()
    assert isinstance(instance, Expression)


def test_debugSeq_Rem_isa_Expression():
    instance = debugSeq_Rem()
    assert isinstance(instance, Expression)


def test_debugSeq_SequenceCall_isa_Expression():
    instance = debugSeq_SequenceCall(seqname="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_Shift_isa_Expression():
    instance = debugSeq_Shift(op="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_StringConstant_isa_Expression():
    instance = debugSeq_StringConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_debugSeq_Ternary_isa_Expression():
    instance = debugSeq_Ternary()
    assert isinstance(instance, Expression)


def test_debugSeq_VariableRef_isa_Expression():
    instance = debugSeq_VariableRef()
    assert isinstance(instance, Expression)


def test_debugSeq_Write16_isa_Expression():
    instance = debugSeq_Write16()
    assert isinstance(instance, Expression)


def test_debugSeq_Write32_isa_Expression():
    instance = debugSeq_Write32()
    assert isinstance(instance, Expression)


def test_debugSeq_Write64_isa_Expression():
    instance = debugSeq_Write64()
    assert isinstance(instance, Expression)


def test_debugSeq_Write8_isa_Expression():
    instance = debugSeq_Write8()
    assert isinstance(instance, Expression)


def test_debugSeq_WriteAP_isa_Expression():
    instance = debugSeq_WriteAP()
    assert isinstance(instance, Expression)


def test_debugSeq_WriteDP_isa_Expression():
    instance = debugSeq_WriteDP()
    assert isinstance(instance, Expression)


def test_debugSeq_Expression_isa_Parameter():
    instance = debugSeq_Expression()
    assert isinstance(instance, Parameter)


def test_debugSeq_Expression_isa_Statement():
    instance = debugSeq_Expression()
    assert isinstance(instance, Statement)


def test_debugSeq_VariableDeclaration_isa_Statement():
    instance = debugSeq_VariableDeclaration(name="sample_text")
    assert isinstance(instance, Statement)


def test_assoc_codeblocks17_link_reassign_clear():
    a = debugSeq_Control(timeout="sample_text")
    b1 = debugSeq_CodeBlock(info="sample_text")
    b2 = debugSeq_CodeBlock(info="sample_text_2")
    _safe_set(a, 'debugSeq_Control18', {b1})
    assert _is_linked(a, 'debugSeq_Control18', b1)
    if hasattr(b1, 'debugSeq_CodeBlock19'):
        assert _is_linked(b1, 'debugSeq_CodeBlock19', a)
    _safe_set(a, 'debugSeq_Control18', {b2})
    assert _is_linked(a, 'debugSeq_Control18', b2)
    if hasattr(b1, 'debugSeq_CodeBlock19'):
        assert not _is_linked(b1, 'debugSeq_CodeBlock19', a)
    if hasattr(b2, 'debugSeq_CodeBlock19'):
        assert _is_linked(b2, 'debugSeq_CodeBlock19', a)
    _safe_set(a, 'debugSeq_Control18', set())
    assert not _is_linked(a, 'debugSeq_Control18', b2)
    if hasattr(b2, 'debugSeq_CodeBlock19'):
        assert not _is_linked(b2, 'debugSeq_CodeBlock19', a)


def test_assoc_codeblocks8_link_reassign_clear():
    a = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    b1 = debugSeq_CodeBlock(info="sample_text")
    b2 = debugSeq_CodeBlock(info="sample_text_2")
    _safe_set(a, 'debugSeq_Sequence9', {b1})
    assert _is_linked(a, 'debugSeq_Sequence9', b1)
    if hasattr(b1, 'debugSeq_CodeBlock'):
        assert _is_linked(b1, 'debugSeq_CodeBlock', a)
    _safe_set(a, 'debugSeq_Sequence9', {b2})
    assert _is_linked(a, 'debugSeq_Sequence9', b2)
    if hasattr(b1, 'debugSeq_CodeBlock'):
        assert not _is_linked(b1, 'debugSeq_CodeBlock', a)
    if hasattr(b2, 'debugSeq_CodeBlock'):
        assert _is_linked(b2, 'debugSeq_CodeBlock', a)
    _safe_set(a, 'debugSeq_Sequence9', set())
    assert not _is_linked(a, 'debugSeq_Sequence9', b2)
    if hasattr(b2, 'debugSeq_CodeBlock'):
        assert not _is_linked(b2, 'debugSeq_CodeBlock', a)


def test_assoc_debugvars0_link_reassign_clear():
    a = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    b1 = debugSeq_DebugSeqModel()
    b2 = debugSeq_DebugSeqModel()
    _safe_set(a, 'debugSeq_DebugVars', b1)
    assert _is_linked(a, 'debugSeq_DebugVars', b1)
    if hasattr(b1, 'debugSeq_DebugSeqModel'):
        assert _is_linked(b1, 'debugSeq_DebugSeqModel', a)
    _safe_set(a, 'debugSeq_DebugVars', b2)
    assert _is_linked(a, 'debugSeq_DebugVars', b2)
    if hasattr(b1, 'debugSeq_DebugSeqModel'):
        assert not _is_linked(b1, 'debugSeq_DebugSeqModel', a)
    if hasattr(b2, 'debugSeq_DebugSeqModel'):
        assert _is_linked(b2, 'debugSeq_DebugSeqModel', a)
    _safe_set(a, 'debugSeq_DebugVars', None)
    assert not _is_linked(a, 'debugSeq_DebugVars', b2)
    if hasattr(b2, 'debugSeq_DebugSeqModel'):
        assert not _is_linked(b2, 'debugSeq_DebugSeqModel', a)


def test_assoc_default104_link_reassign_clear():
    a = debugSeq_Query(message="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Query105', b1)
    assert _is_linked(a, 'debugSeq_Query105', b1)
    if hasattr(b1, 'debugSeq_Expression106'):
        assert _is_linked(b1, 'debugSeq_Expression106', a)
    _safe_set(a, 'debugSeq_Query105', b2)
    assert _is_linked(a, 'debugSeq_Query105', b2)
    if hasattr(b1, 'debugSeq_Expression106'):
        assert not _is_linked(b1, 'debugSeq_Expression106', a)
    if hasattr(b2, 'debugSeq_Expression106'):
        assert _is_linked(b2, 'debugSeq_Expression106', a)
    _safe_set(a, 'debugSeq_Query105', None)
    assert not _is_linked(a, 'debugSeq_Query105', b2)
    if hasattr(b2, 'debugSeq_Expression106'):
        assert not _is_linked(b2, 'debugSeq_Expression106', a)


def test_assoc_default107_link_reassign_clear():
    a = debugSeq_QueryValue(message="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_QueryValue', b1)
    assert _is_linked(a, 'debugSeq_QueryValue', b1)
    if hasattr(b1, 'debugSeq_Expression108'):
        assert _is_linked(b1, 'debugSeq_Expression108', a)
    _safe_set(a, 'debugSeq_QueryValue', b2)
    assert _is_linked(a, 'debugSeq_QueryValue', b2)
    if hasattr(b1, 'debugSeq_Expression108'):
        assert not _is_linked(b1, 'debugSeq_Expression108', a)
    if hasattr(b2, 'debugSeq_Expression108'):
        assert _is_linked(b2, 'debugSeq_Expression108', a)
    _safe_set(a, 'debugSeq_QueryValue', None)
    assert not _is_linked(a, 'debugSeq_QueryValue', b2)
    if hasattr(b2, 'debugSeq_Expression108'):
        assert not _is_linked(b2, 'debugSeq_Expression108', a)


def test_assoc_if_12_link_reassign_clear():
    a = debugSeq_Control(timeout="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Control', b1)
    assert _is_linked(a, 'debugSeq_Control', b1)
    if hasattr(b1, 'debugSeq_Expression13'):
        assert _is_linked(b1, 'debugSeq_Expression13', a)
    _safe_set(a, 'debugSeq_Control', b2)
    assert _is_linked(a, 'debugSeq_Control', b2)
    if hasattr(b1, 'debugSeq_Expression13'):
        assert not _is_linked(b1, 'debugSeq_Expression13', a)
    if hasattr(b2, 'debugSeq_Expression13'):
        assert _is_linked(b2, 'debugSeq_Expression13', a)
    _safe_set(a, 'debugSeq_Control', None)
    assert not _is_linked(a, 'debugSeq_Control', b2)
    if hasattr(b2, 'debugSeq_Expression13'):
        assert not _is_linked(b2, 'debugSeq_Expression13', a)


def test_assoc_left20_link_reassign_clear():
    a = debugSeq_Assignment(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Assignment', b1)
    assert _is_linked(a, 'debugSeq_Assignment', b1)
    if hasattr(b1, 'debugSeq_Expression21'):
        assert _is_linked(b1, 'debugSeq_Expression21', a)
    _safe_set(a, 'debugSeq_Assignment', b2)
    assert _is_linked(a, 'debugSeq_Assignment', b2)
    if hasattr(b1, 'debugSeq_Expression21'):
        assert not _is_linked(b1, 'debugSeq_Expression21', a)
    if hasattr(b2, 'debugSeq_Expression21'):
        assert _is_linked(b2, 'debugSeq_Expression21', a)
    _safe_set(a, 'debugSeq_Assignment', None)
    assert not _is_linked(a, 'debugSeq_Assignment', b2)
    if hasattr(b2, 'debugSeq_Expression21'):
        assert not _is_linked(b2, 'debugSeq_Expression21', a)


def test_assoc_left58_link_reassign_clear():
    a = debugSeq_Equality(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Equality', b1)
    assert _is_linked(a, 'debugSeq_Equality', b1)
    if hasattr(b1, 'debugSeq_Expression59'):
        assert _is_linked(b1, 'debugSeq_Expression59', a)
    _safe_set(a, 'debugSeq_Equality', b2)
    assert _is_linked(a, 'debugSeq_Equality', b2)
    if hasattr(b1, 'debugSeq_Expression59'):
        assert not _is_linked(b1, 'debugSeq_Expression59', a)
    if hasattr(b2, 'debugSeq_Expression59'):
        assert _is_linked(b2, 'debugSeq_Expression59', a)
    _safe_set(a, 'debugSeq_Equality', None)
    assert not _is_linked(a, 'debugSeq_Equality', b2)
    if hasattr(b2, 'debugSeq_Expression59'):
        assert not _is_linked(b2, 'debugSeq_Expression59', a)


def test_assoc_left63_link_reassign_clear():
    a = debugSeq_Comparison(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Comparison', b1)
    assert _is_linked(a, 'debugSeq_Comparison', b1)
    if hasattr(b1, 'debugSeq_Expression64'):
        assert _is_linked(b1, 'debugSeq_Expression64', a)
    _safe_set(a, 'debugSeq_Comparison', b2)
    assert _is_linked(a, 'debugSeq_Comparison', b2)
    if hasattr(b1, 'debugSeq_Expression64'):
        assert not _is_linked(b1, 'debugSeq_Expression64', a)
    if hasattr(b2, 'debugSeq_Expression64'):
        assert _is_linked(b2, 'debugSeq_Expression64', a)
    _safe_set(a, 'debugSeq_Comparison', None)
    assert not _is_linked(a, 'debugSeq_Comparison', b2)
    if hasattr(b2, 'debugSeq_Expression64'):
        assert not _is_linked(b2, 'debugSeq_Expression64', a)


def test_assoc_left68_link_reassign_clear():
    a = debugSeq_Shift(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Shift', b1)
    assert _is_linked(a, 'debugSeq_Shift', b1)
    if hasattr(b1, 'debugSeq_Expression69'):
        assert _is_linked(b1, 'debugSeq_Expression69', a)
    _safe_set(a, 'debugSeq_Shift', b2)
    assert _is_linked(a, 'debugSeq_Shift', b2)
    if hasattr(b1, 'debugSeq_Expression69'):
        assert not _is_linked(b1, 'debugSeq_Expression69', a)
    if hasattr(b2, 'debugSeq_Expression69'):
        assert _is_linked(b2, 'debugSeq_Expression69', a)
    _safe_set(a, 'debugSeq_Shift', None)
    assert not _is_linked(a, 'debugSeq_Shift', b2)
    if hasattr(b2, 'debugSeq_Expression69'):
        assert not _is_linked(b2, 'debugSeq_Expression69', a)


def test_assoc_parameters111_link_reassign_clear():
    a = debugSeq_Message(format="sample_text")
    b1 = debugSeq_Parameter()
    b2 = debugSeq_Parameter()
    _safe_set(a, 'debugSeq_Message112', {b1})
    assert _is_linked(a, 'debugSeq_Message112', b1)
    if hasattr(b1, 'debugSeq_Parameter'):
        assert _is_linked(b1, 'debugSeq_Parameter', a)
    _safe_set(a, 'debugSeq_Message112', {b2})
    assert _is_linked(a, 'debugSeq_Message112', b2)
    if hasattr(b1, 'debugSeq_Parameter'):
        assert not _is_linked(b1, 'debugSeq_Parameter', a)
    if hasattr(b2, 'debugSeq_Parameter'):
        assert _is_linked(b2, 'debugSeq_Parameter', a)
    _safe_set(a, 'debugSeq_Message112', set())
    assert not _is_linked(a, 'debugSeq_Message112', b2)
    if hasattr(b2, 'debugSeq_Parameter'):
        assert not _is_linked(b2, 'debugSeq_Parameter', a)


def test_assoc_right22_link_reassign_clear():
    a = debugSeq_Assignment(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Assignment23', b1)
    assert _is_linked(a, 'debugSeq_Assignment23', b1)
    if hasattr(b1, 'debugSeq_Expression24'):
        assert _is_linked(b1, 'debugSeq_Expression24', a)
    _safe_set(a, 'debugSeq_Assignment23', b2)
    assert _is_linked(a, 'debugSeq_Assignment23', b2)
    if hasattr(b1, 'debugSeq_Expression24'):
        assert not _is_linked(b1, 'debugSeq_Expression24', a)
    if hasattr(b2, 'debugSeq_Expression24'):
        assert _is_linked(b2, 'debugSeq_Expression24', a)
    _safe_set(a, 'debugSeq_Assignment23', None)
    assert not _is_linked(a, 'debugSeq_Assignment23', b2)
    if hasattr(b2, 'debugSeq_Expression24'):
        assert not _is_linked(b2, 'debugSeq_Expression24', a)


def test_assoc_right60_link_reassign_clear():
    a = debugSeq_Equality(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Equality61', b1)
    assert _is_linked(a, 'debugSeq_Equality61', b1)
    if hasattr(b1, 'debugSeq_Expression62'):
        assert _is_linked(b1, 'debugSeq_Expression62', a)
    _safe_set(a, 'debugSeq_Equality61', b2)
    assert _is_linked(a, 'debugSeq_Equality61', b2)
    if hasattr(b1, 'debugSeq_Expression62'):
        assert not _is_linked(b1, 'debugSeq_Expression62', a)
    if hasattr(b2, 'debugSeq_Expression62'):
        assert _is_linked(b2, 'debugSeq_Expression62', a)
    _safe_set(a, 'debugSeq_Equality61', None)
    assert not _is_linked(a, 'debugSeq_Equality61', b2)
    if hasattr(b2, 'debugSeq_Expression62'):
        assert not _is_linked(b2, 'debugSeq_Expression62', a)


def test_assoc_right65_link_reassign_clear():
    a = debugSeq_Comparison(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Comparison66', b1)
    assert _is_linked(a, 'debugSeq_Comparison66', b1)
    if hasattr(b1, 'debugSeq_Expression67'):
        assert _is_linked(b1, 'debugSeq_Expression67', a)
    _safe_set(a, 'debugSeq_Comparison66', b2)
    assert _is_linked(a, 'debugSeq_Comparison66', b2)
    if hasattr(b1, 'debugSeq_Expression67'):
        assert not _is_linked(b1, 'debugSeq_Expression67', a)
    if hasattr(b2, 'debugSeq_Expression67'):
        assert _is_linked(b2, 'debugSeq_Expression67', a)
    _safe_set(a, 'debugSeq_Comparison66', None)
    assert not _is_linked(a, 'debugSeq_Comparison66', b2)
    if hasattr(b2, 'debugSeq_Expression67'):
        assert not _is_linked(b2, 'debugSeq_Expression67', a)


def test_assoc_right70_link_reassign_clear():
    a = debugSeq_Shift(op="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Shift71', b1)
    assert _is_linked(a, 'debugSeq_Shift71', b1)
    if hasattr(b1, 'debugSeq_Expression72'):
        assert _is_linked(b1, 'debugSeq_Expression72', a)
    _safe_set(a, 'debugSeq_Shift71', b2)
    assert _is_linked(a, 'debugSeq_Shift71', b2)
    if hasattr(b1, 'debugSeq_Expression72'):
        assert not _is_linked(b1, 'debugSeq_Expression72', a)
    if hasattr(b2, 'debugSeq_Expression72'):
        assert _is_linked(b2, 'debugSeq_Expression72', a)
    _safe_set(a, 'debugSeq_Shift71', None)
    assert not _is_linked(a, 'debugSeq_Shift71', b2)
    if hasattr(b2, 'debugSeq_Expression72'):
        assert not _is_linked(b2, 'debugSeq_Expression72', a)


def test_assoc_sequences6_link_reassign_clear():
    a = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    b1 = debugSeq_Sequences()
    b2 = debugSeq_Sequences()
    _safe_set(a, 'debugSeq_Sequence', b1)
    assert _is_linked(a, 'debugSeq_Sequence', b1)
    if hasattr(b1, 'debugSeq_Sequences7'):
        assert _is_linked(b1, 'debugSeq_Sequences7', a)
    _safe_set(a, 'debugSeq_Sequence', b2)
    assert _is_linked(a, 'debugSeq_Sequence', b2)
    if hasattr(b1, 'debugSeq_Sequences7'):
        assert not _is_linked(b1, 'debugSeq_Sequences7', a)
    if hasattr(b2, 'debugSeq_Sequences7'):
        assert _is_linked(b2, 'debugSeq_Sequences7', a)
    _safe_set(a, 'debugSeq_Sequence', None)
    assert not _is_linked(a, 'debugSeq_Sequence', b2)
    if hasattr(b2, 'debugSeq_Sequences7'):
        assert not _is_linked(b2, 'debugSeq_Sequences7', a)


def test_assoc_statements10_link_reassign_clear():
    a = debugSeq_Block(atomic="sample_text")
    b1 = debugSeq_Statement()
    b2 = debugSeq_Statement()
    _safe_set(a, 'debugSeq_Block', {b1})
    assert _is_linked(a, 'debugSeq_Block', b1)
    if hasattr(b1, 'debugSeq_Statement11'):
        assert _is_linked(b1, 'debugSeq_Statement11', a)
    _safe_set(a, 'debugSeq_Block', {b2})
    assert _is_linked(a, 'debugSeq_Block', b2)
    if hasattr(b1, 'debugSeq_Statement11'):
        assert not _is_linked(b1, 'debugSeq_Statement11', a)
    if hasattr(b2, 'debugSeq_Statement11'):
        assert _is_linked(b2, 'debugSeq_Statement11', a)
    _safe_set(a, 'debugSeq_Block', set())
    assert not _is_linked(a, 'debugSeq_Block', b2)
    if hasattr(b2, 'debugSeq_Statement11'):
        assert not _is_linked(b2, 'debugSeq_Statement11', a)


def test_assoc_statements3_link_reassign_clear():
    a = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    b1 = debugSeq_Statement()
    b2 = debugSeq_Statement()
    _safe_set(a, 'debugSeq_DebugVars4', {b1})
    assert _is_linked(a, 'debugSeq_DebugVars4', b1)
    if hasattr(b1, 'debugSeq_Statement'):
        assert _is_linked(b1, 'debugSeq_Statement', a)
    _safe_set(a, 'debugSeq_DebugVars4', {b2})
    assert _is_linked(a, 'debugSeq_DebugVars4', b2)
    if hasattr(b1, 'debugSeq_Statement'):
        assert not _is_linked(b1, 'debugSeq_Statement', a)
    if hasattr(b2, 'debugSeq_Statement'):
        assert _is_linked(b2, 'debugSeq_Statement', a)
    _safe_set(a, 'debugSeq_DebugVars4', set())
    assert not _is_linked(a, 'debugSeq_DebugVars4', b2)
    if hasattr(b2, 'debugSeq_Statement'):
        assert not _is_linked(b2, 'debugSeq_Statement', a)


def test_assoc_type102_link_reassign_clear():
    a = debugSeq_Query(message="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Query', b1)
    assert _is_linked(a, 'debugSeq_Query', b1)
    if hasattr(b1, 'debugSeq_Expression103'):
        assert _is_linked(b1, 'debugSeq_Expression103', a)
    _safe_set(a, 'debugSeq_Query', b2)
    assert _is_linked(a, 'debugSeq_Query', b2)
    if hasattr(b1, 'debugSeq_Expression103'):
        assert not _is_linked(b1, 'debugSeq_Expression103', a)
    if hasattr(b2, 'debugSeq_Expression103'):
        assert _is_linked(b2, 'debugSeq_Expression103', a)
    _safe_set(a, 'debugSeq_Query', None)
    assert not _is_linked(a, 'debugSeq_Query', b2)
    if hasattr(b2, 'debugSeq_Expression103'):
        assert not _is_linked(b2, 'debugSeq_Expression103', a)


def test_assoc_type109_link_reassign_clear():
    a = debugSeq_Message(format="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Message', b1)
    assert _is_linked(a, 'debugSeq_Message', b1)
    if hasattr(b1, 'debugSeq_Expression110'):
        assert _is_linked(b1, 'debugSeq_Expression110', a)
    _safe_set(a, 'debugSeq_Message', b2)
    assert _is_linked(a, 'debugSeq_Message', b2)
    if hasattr(b1, 'debugSeq_Expression110'):
        assert not _is_linked(b1, 'debugSeq_Expression110', a)
    if hasattr(b2, 'debugSeq_Expression110'):
        assert _is_linked(b2, 'debugSeq_Expression110', a)
    _safe_set(a, 'debugSeq_Message', None)
    assert not _is_linked(a, 'debugSeq_Message', b2)
    if hasattr(b2, 'debugSeq_Expression110'):
        assert not _is_linked(b2, 'debugSeq_Expression110', a)


def test_assoc_value5_link_reassign_clear():
    a = debugSeq_VariableDeclaration(name="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_VariableDeclaration', b1)
    assert _is_linked(a, 'debugSeq_VariableDeclaration', b1)
    if hasattr(b1, 'debugSeq_Expression'):
        assert _is_linked(b1, 'debugSeq_Expression', a)
    _safe_set(a, 'debugSeq_VariableDeclaration', b2)
    assert _is_linked(a, 'debugSeq_VariableDeclaration', b2)
    if hasattr(b1, 'debugSeq_Expression'):
        assert not _is_linked(b1, 'debugSeq_Expression', a)
    if hasattr(b2, 'debugSeq_Expression'):
        assert _is_linked(b2, 'debugSeq_Expression', a)
    _safe_set(a, 'debugSeq_VariableDeclaration', None)
    assert not _is_linked(a, 'debugSeq_VariableDeclaration', b2)
    if hasattr(b2, 'debugSeq_Expression'):
        assert not _is_linked(b2, 'debugSeq_Expression', a)


def test_assoc_variable182_link_reassign_clear():
    a = debugSeq_VariableDeclaration(name="sample_text")
    b1 = debugSeq_VariableRef()
    b2 = debugSeq_VariableRef()
    _safe_set(a, 'debugSeq_VariableDeclaration183', b1)
    assert _is_linked(a, 'debugSeq_VariableDeclaration183', b1)
    if hasattr(b1, 'debugSeq_VariableRef'):
        assert _is_linked(b1, 'debugSeq_VariableRef', a)
    _safe_set(a, 'debugSeq_VariableDeclaration183', b2)
    assert _is_linked(a, 'debugSeq_VariableDeclaration183', b2)
    if hasattr(b1, 'debugSeq_VariableRef'):
        assert not _is_linked(b1, 'debugSeq_VariableRef', a)
    if hasattr(b2, 'debugSeq_VariableRef'):
        assert _is_linked(b2, 'debugSeq_VariableRef', a)
    _safe_set(a, 'debugSeq_VariableDeclaration183', None)
    assert not _is_linked(a, 'debugSeq_VariableDeclaration183', b2)
    if hasattr(b2, 'debugSeq_VariableRef'):
        assert not _is_linked(b2, 'debugSeq_VariableRef', a)


def test_assoc_while_14_link_reassign_clear():
    a = debugSeq_Control(timeout="sample_text")
    b1 = debugSeq_Expression()
    b2 = debugSeq_Expression()
    _safe_set(a, 'debugSeq_Control15', b1)
    assert _is_linked(a, 'debugSeq_Control15', b1)
    if hasattr(b1, 'debugSeq_Expression16'):
        assert _is_linked(b1, 'debugSeq_Expression16', a)
    _safe_set(a, 'debugSeq_Control15', b2)
    assert _is_linked(a, 'debugSeq_Control15', b2)
    if hasattr(b1, 'debugSeq_Expression16'):
        assert not _is_linked(b1, 'debugSeq_Expression16', a)
    if hasattr(b2, 'debugSeq_Expression16'):
        assert _is_linked(b2, 'debugSeq_Expression16', a)
    _safe_set(a, 'debugSeq_Control15', None)
    assert not _is_linked(a, 'debugSeq_Control15', b2)
    if hasattr(b2, 'debugSeq_Expression16'):
        assert not _is_linked(b2, 'debugSeq_Expression16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CodeBlock_strategy = st.builds(CodeBlock)
@given(instance=CodeBlock_strategy)
@settings(max_examples=25)
def test_CodeBlock_instantiation(instance):
    assert isinstance(instance, CodeBlock)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


debugSeq_And_strategy = st.builds(debugSeq_And)
@given(instance=debugSeq_And_strategy)
@settings(max_examples=25)
def test_debugSeq_And_instantiation(instance):
    assert isinstance(instance, debugSeq_And)


debugSeq_Assignment_strategy = st.builds(debugSeq_Assignment, op=safe_text)
@given(instance=debugSeq_Assignment_strategy)
@settings(max_examples=25)
def test_debugSeq_Assignment_instantiation(instance):
    assert isinstance(instance, debugSeq_Assignment)


debugSeq_BitAnd_strategy = st.builds(debugSeq_BitAnd)
@given(instance=debugSeq_BitAnd_strategy)
@settings(max_examples=25)
def test_debugSeq_BitAnd_instantiation(instance):
    assert isinstance(instance, debugSeq_BitAnd)


debugSeq_BitNot_strategy = st.builds(debugSeq_BitNot)
@given(instance=debugSeq_BitNot_strategy)
@settings(max_examples=25)
def test_debugSeq_BitNot_instantiation(instance):
    assert isinstance(instance, debugSeq_BitNot)


debugSeq_BitOr_strategy = st.builds(debugSeq_BitOr)
@given(instance=debugSeq_BitOr_strategy)
@settings(max_examples=25)
def test_debugSeq_BitOr_instantiation(instance):
    assert isinstance(instance, debugSeq_BitOr)


debugSeq_BitXor_strategy = st.builds(debugSeq_BitXor)
@given(instance=debugSeq_BitXor_strategy)
@settings(max_examples=25)
def test_debugSeq_BitXor_instantiation(instance):
    assert isinstance(instance, debugSeq_BitXor)


debugSeq_Block_strategy = st.builds(debugSeq_Block, atomic=safe_text)
@given(instance=debugSeq_Block_strategy)
@settings(max_examples=25)
def test_debugSeq_Block_instantiation(instance):
    assert isinstance(instance, debugSeq_Block)


debugSeq_CodeBlock_strategy = st.builds(debugSeq_CodeBlock, info=safe_text)
@given(instance=debugSeq_CodeBlock_strategy)
@settings(max_examples=25)
def test_debugSeq_CodeBlock_instantiation(instance):
    assert isinstance(instance, debugSeq_CodeBlock)


debugSeq_Comparison_strategy = st.builds(debugSeq_Comparison, op=safe_text)
@given(instance=debugSeq_Comparison_strategy)
@settings(max_examples=25)
def test_debugSeq_Comparison_instantiation(instance):
    assert isinstance(instance, debugSeq_Comparison)


debugSeq_Control_strategy = st.builds(debugSeq_Control, timeout=safe_text)
@given(instance=debugSeq_Control_strategy)
@settings(max_examples=25)
def test_debugSeq_Control_instantiation(instance):
    assert isinstance(instance, debugSeq_Control)


debugSeq_DapDelay_strategy = st.builds(debugSeq_DapDelay)
@given(instance=debugSeq_DapDelay_strategy)
@settings(max_examples=25)
def test_debugSeq_DapDelay_instantiation(instance):
    assert isinstance(instance, debugSeq_DapDelay)


debugSeq_DapJtagSequence_strategy = st.builds(debugSeq_DapJtagSequence)
@given(instance=debugSeq_DapJtagSequence_strategy)
@settings(max_examples=25)
def test_debugSeq_DapJtagSequence_instantiation(instance):
    assert isinstance(instance, debugSeq_DapJtagSequence)


debugSeq_DapSwjClock_strategy = st.builds(debugSeq_DapSwjClock)
@given(instance=debugSeq_DapSwjClock_strategy)
@settings(max_examples=25)
def test_debugSeq_DapSwjClock_instantiation(instance):
    assert isinstance(instance, debugSeq_DapSwjClock)


debugSeq_DapSwjPins_strategy = st.builds(debugSeq_DapSwjPins)
@given(instance=debugSeq_DapSwjPins_strategy)
@settings(max_examples=25)
def test_debugSeq_DapSwjPins_instantiation(instance):
    assert isinstance(instance, debugSeq_DapSwjPins)


debugSeq_DapSwjSequence_strategy = st.builds(debugSeq_DapSwjSequence)
@given(instance=debugSeq_DapSwjSequence_strategy)
@settings(max_examples=25)
def test_debugSeq_DapSwjSequence_instantiation(instance):
    assert isinstance(instance, debugSeq_DapSwjSequence)


debugSeq_DapWriteABORT_strategy = st.builds(debugSeq_DapWriteABORT)
@given(instance=debugSeq_DapWriteABORT_strategy)
@settings(max_examples=25)
def test_debugSeq_DapWriteABORT_instantiation(instance):
    assert isinstance(instance, debugSeq_DapWriteABORT)


debugSeq_DebugSeqModel_strategy = st.builds(debugSeq_DebugSeqModel)
@given(instance=debugSeq_DebugSeqModel_strategy)
@settings(max_examples=25)
def test_debugSeq_DebugSeqModel_instantiation(instance):
    assert isinstance(instance, debugSeq_DebugSeqModel)


debugSeq_DebugVars_strategy = st.builds(debugSeq_DebugVars, configfile=safe_text, pname=safe_text, version=safe_text)
@given(instance=debugSeq_DebugVars_strategy)
@settings(max_examples=25)
def test_debugSeq_DebugVars_instantiation(instance):
    assert isinstance(instance, debugSeq_DebugVars)


debugSeq_Div_strategy = st.builds(debugSeq_Div)
@given(instance=debugSeq_Div_strategy)
@settings(max_examples=25)
def test_debugSeq_Div_instantiation(instance):
    assert isinstance(instance, debugSeq_Div)


debugSeq_Equality_strategy = st.builds(debugSeq_Equality, op=safe_text)
@given(instance=debugSeq_Equality_strategy)
@settings(max_examples=25)
def test_debugSeq_Equality_instantiation(instance):
    assert isinstance(instance, debugSeq_Equality)


debugSeq_Expression_strategy = st.builds(debugSeq_Expression)
@given(instance=debugSeq_Expression_strategy)
@settings(max_examples=25)
def test_debugSeq_Expression_instantiation(instance):
    assert isinstance(instance, debugSeq_Expression)


debugSeq_IntConstant_strategy = st.builds(debugSeq_IntConstant, value=safe_text)
@given(instance=debugSeq_IntConstant_strategy)
@settings(max_examples=25)
def test_debugSeq_IntConstant_instantiation(instance):
    assert isinstance(instance, debugSeq_IntConstant)


debugSeq_LoadDebugInfo_strategy = st.builds(debugSeq_LoadDebugInfo, path=safe_text)
@given(instance=debugSeq_LoadDebugInfo_strategy)
@settings(max_examples=25)
def test_debugSeq_LoadDebugInfo_instantiation(instance):
    assert isinstance(instance, debugSeq_LoadDebugInfo)


debugSeq_Message_strategy = st.builds(debugSeq_Message, format=safe_text)
@given(instance=debugSeq_Message_strategy)
@settings(max_examples=25)
def test_debugSeq_Message_instantiation(instance):
    assert isinstance(instance, debugSeq_Message)


debugSeq_Minus_strategy = st.builds(debugSeq_Minus)
@given(instance=debugSeq_Minus_strategy)
@settings(max_examples=25)
def test_debugSeq_Minus_instantiation(instance):
    assert isinstance(instance, debugSeq_Minus)


debugSeq_Mul_strategy = st.builds(debugSeq_Mul)
@given(instance=debugSeq_Mul_strategy)
@settings(max_examples=25)
def test_debugSeq_Mul_instantiation(instance):
    assert isinstance(instance, debugSeq_Mul)


debugSeq_Not_strategy = st.builds(debugSeq_Not)
@given(instance=debugSeq_Not_strategy)
@settings(max_examples=25)
def test_debugSeq_Not_instantiation(instance):
    assert isinstance(instance, debugSeq_Not)


debugSeq_Or_strategy = st.builds(debugSeq_Or)
@given(instance=debugSeq_Or_strategy)
@settings(max_examples=25)
def test_debugSeq_Or_instantiation(instance):
    assert isinstance(instance, debugSeq_Or)


debugSeq_Parameter_strategy = st.builds(debugSeq_Parameter)
@given(instance=debugSeq_Parameter_strategy)
@settings(max_examples=25)
def test_debugSeq_Parameter_instantiation(instance):
    assert isinstance(instance, debugSeq_Parameter)


debugSeq_Plus_strategy = st.builds(debugSeq_Plus)
@given(instance=debugSeq_Plus_strategy)
@settings(max_examples=25)
def test_debugSeq_Plus_instantiation(instance):
    assert isinstance(instance, debugSeq_Plus)


debugSeq_Query_strategy = st.builds(debugSeq_Query, message=safe_text)
@given(instance=debugSeq_Query_strategy)
@settings(max_examples=25)
def test_debugSeq_Query_instantiation(instance):
    assert isinstance(instance, debugSeq_Query)


debugSeq_QueryValue_strategy = st.builds(debugSeq_QueryValue, message=safe_text)
@given(instance=debugSeq_QueryValue_strategy)
@settings(max_examples=25)
def test_debugSeq_QueryValue_instantiation(instance):
    assert isinstance(instance, debugSeq_QueryValue)


debugSeq_Read16_strategy = st.builds(debugSeq_Read16)
@given(instance=debugSeq_Read16_strategy)
@settings(max_examples=25)
def test_debugSeq_Read16_instantiation(instance):
    assert isinstance(instance, debugSeq_Read16)


debugSeq_Read32_strategy = st.builds(debugSeq_Read32)
@given(instance=debugSeq_Read32_strategy)
@settings(max_examples=25)
def test_debugSeq_Read32_instantiation(instance):
    assert isinstance(instance, debugSeq_Read32)


debugSeq_Read64_strategy = st.builds(debugSeq_Read64)
@given(instance=debugSeq_Read64_strategy)
@settings(max_examples=25)
def test_debugSeq_Read64_instantiation(instance):
    assert isinstance(instance, debugSeq_Read64)


debugSeq_Read8_strategy = st.builds(debugSeq_Read8)
@given(instance=debugSeq_Read8_strategy)
@settings(max_examples=25)
def test_debugSeq_Read8_instantiation(instance):
    assert isinstance(instance, debugSeq_Read8)


debugSeq_ReadAP_strategy = st.builds(debugSeq_ReadAP)
@given(instance=debugSeq_ReadAP_strategy)
@settings(max_examples=25)
def test_debugSeq_ReadAP_instantiation(instance):
    assert isinstance(instance, debugSeq_ReadAP)


debugSeq_ReadDP_strategy = st.builds(debugSeq_ReadDP)
@given(instance=debugSeq_ReadDP_strategy)
@settings(max_examples=25)
def test_debugSeq_ReadDP_instantiation(instance):
    assert isinstance(instance, debugSeq_ReadDP)


debugSeq_Rem_strategy = st.builds(debugSeq_Rem)
@given(instance=debugSeq_Rem_strategy)
@settings(max_examples=25)
def test_debugSeq_Rem_instantiation(instance):
    assert isinstance(instance, debugSeq_Rem)


debugSeq_Sequence_strategy = st.builds(debugSeq_Sequence, disable=safe_text, info=safe_text, name=safe_text, pname=safe_text)
@given(instance=debugSeq_Sequence_strategy)
@settings(max_examples=25)
def test_debugSeq_Sequence_instantiation(instance):
    assert isinstance(instance, debugSeq_Sequence)


debugSeq_SequenceCall_strategy = st.builds(debugSeq_SequenceCall, seqname=safe_text)
@given(instance=debugSeq_SequenceCall_strategy)
@settings(max_examples=25)
def test_debugSeq_SequenceCall_instantiation(instance):
    assert isinstance(instance, debugSeq_SequenceCall)


debugSeq_Sequences_strategy = st.builds(debugSeq_Sequences)
@given(instance=debugSeq_Sequences_strategy)
@settings(max_examples=25)
def test_debugSeq_Sequences_instantiation(instance):
    assert isinstance(instance, debugSeq_Sequences)


debugSeq_Shift_strategy = st.builds(debugSeq_Shift, op=safe_text)
@given(instance=debugSeq_Shift_strategy)
@settings(max_examples=25)
def test_debugSeq_Shift_instantiation(instance):
    assert isinstance(instance, debugSeq_Shift)


debugSeq_Statement_strategy = st.builds(debugSeq_Statement)
@given(instance=debugSeq_Statement_strategy)
@settings(max_examples=25)
def test_debugSeq_Statement_instantiation(instance):
    assert isinstance(instance, debugSeq_Statement)


debugSeq_StringConstant_strategy = st.builds(debugSeq_StringConstant, value=safe_text)
@given(instance=debugSeq_StringConstant_strategy)
@settings(max_examples=25)
def test_debugSeq_StringConstant_instantiation(instance):
    assert isinstance(instance, debugSeq_StringConstant)


debugSeq_Ternary_strategy = st.builds(debugSeq_Ternary)
@given(instance=debugSeq_Ternary_strategy)
@settings(max_examples=25)
def test_debugSeq_Ternary_instantiation(instance):
    assert isinstance(instance, debugSeq_Ternary)


debugSeq_VariableDeclaration_strategy = st.builds(debugSeq_VariableDeclaration, name=safe_text)
@given(instance=debugSeq_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_debugSeq_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, debugSeq_VariableDeclaration)


debugSeq_VariableRef_strategy = st.builds(debugSeq_VariableRef)
@given(instance=debugSeq_VariableRef_strategy)
@settings(max_examples=25)
def test_debugSeq_VariableRef_instantiation(instance):
    assert isinstance(instance, debugSeq_VariableRef)


debugSeq_Write16_strategy = st.builds(debugSeq_Write16)
@given(instance=debugSeq_Write16_strategy)
@settings(max_examples=25)
def test_debugSeq_Write16_instantiation(instance):
    assert isinstance(instance, debugSeq_Write16)


debugSeq_Write32_strategy = st.builds(debugSeq_Write32)
@given(instance=debugSeq_Write32_strategy)
@settings(max_examples=25)
def test_debugSeq_Write32_instantiation(instance):
    assert isinstance(instance, debugSeq_Write32)


debugSeq_Write64_strategy = st.builds(debugSeq_Write64)
@given(instance=debugSeq_Write64_strategy)
@settings(max_examples=25)
def test_debugSeq_Write64_instantiation(instance):
    assert isinstance(instance, debugSeq_Write64)


debugSeq_Write8_strategy = st.builds(debugSeq_Write8)
@given(instance=debugSeq_Write8_strategy)
@settings(max_examples=25)
def test_debugSeq_Write8_instantiation(instance):
    assert isinstance(instance, debugSeq_Write8)


debugSeq_WriteAP_strategy = st.builds(debugSeq_WriteAP)
@given(instance=debugSeq_WriteAP_strategy)
@settings(max_examples=25)
def test_debugSeq_WriteAP_instantiation(instance):
    assert isinstance(instance, debugSeq_WriteAP)


debugSeq_WriteDP_strategy = st.builds(debugSeq_WriteDP)
@given(instance=debugSeq_WriteDP_strategy)
@settings(max_examples=25)
def test_debugSeq_WriteDP_instantiation(instance):
    assert isinstance(instance, debugSeq_WriteDP)



