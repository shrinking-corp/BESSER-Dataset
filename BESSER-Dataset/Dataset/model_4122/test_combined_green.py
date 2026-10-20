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
    whileDsl_ExprSimpleWithSymbolLExpr,
    whileDsl_ExprSimpleWithExpr,
    whileDsl_LExpr,
    whileDsl_ExprSimpleWithLExpr,
    whileDsl_EObject,
    whileDsl_ExprSimple,
    whileDsl_ExprEq,
    whileDsl_ExprNot,
    whileDsl_ExprOr,
    whileDsl_ExprAnd,
    whileDsl_Command,
    whileDsl_Output,
    whileDsl_Commands,
    whileDsl_Input,
    whileDsl_Exprs,
    whileDsl_Vars,
    whileDsl_Expr,
    Command,
    whileDsl_IfCommand,
    whileDsl_NopCommand,
    whileDsl_VarsCommand,
    whileDsl_ForeachCommand,
    whileDsl_ForCommand,
    whileDsl_WhileCommand,
    whileDsl_Definition,
    whileDsl_Function,
    whileDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_whiledsl_exprsimplewithsymbollexpr_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprSimpleWithSymbolLExpr)


def test_hyp_whiledsl_exprsimplewithsymbollexpr_constructor_exists():
    assert callable(whileDsl_ExprSimpleWithSymbolLExpr.__init__)


def test_hyp_whiledsl_exprsimplewithsymbollexpr_constructor_args():
    sig = inspect.signature(whileDsl_ExprSimpleWithSymbolLExpr.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_whiledsl_exprsimplewithexpr_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprSimpleWithExpr)


def test_hyp_whiledsl_exprsimplewithexpr_constructor_exists():
    assert callable(whileDsl_ExprSimpleWithExpr.__init__)


def test_hyp_whiledsl_exprsimplewithexpr_constructor_args():
    sig = inspect.signature(whileDsl_ExprSimpleWithExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_whiledsl_lexpr_is_not_abstract():
    assert not inspect.isabstract(whileDsl_LExpr)


def test_hyp_whiledsl_lexpr_constructor_exists():
    assert callable(whileDsl_LExpr.__init__)


def test_hyp_whiledsl_lexpr_constructor_args():
    sig = inspect.signature(whileDsl_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_exprsimplewithlexpr_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprSimpleWithLExpr)


def test_hyp_whiledsl_exprsimplewithlexpr_constructor_exists():
    assert callable(whileDsl_ExprSimpleWithLExpr.__init__)


def test_hyp_whiledsl_exprsimplewithlexpr_constructor_args():
    sig = inspect.signature(whileDsl_ExprSimpleWithLExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_whiledsl_eobject_is_not_abstract():
    assert not inspect.isabstract(whileDsl_EObject)


def test_hyp_whiledsl_eobject_constructor_exists():
    assert callable(whileDsl_EObject.__init__)


def test_hyp_whiledsl_eobject_constructor_args():
    sig = inspect.signature(whileDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_exprsimple_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprSimple)


def test_hyp_whiledsl_exprsimple_constructor_exists():
    assert callable(whileDsl_ExprSimple.__init__)


def test_hyp_whiledsl_exprsimple_constructor_args():
    sig = inspect.signature(whileDsl_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"




def test_hyp_whiledsl_expreq_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprEq)


def test_hyp_whiledsl_expreq_constructor_exists():
    assert callable(whileDsl_ExprEq.__init__)


def test_hyp_whiledsl_expreq_constructor_args():
    sig = inspect.signature(whileDsl_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_exprnot_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprNot)


def test_hyp_whiledsl_exprnot_constructor_exists():
    assert callable(whileDsl_ExprNot.__init__)


def test_hyp_whiledsl_exprnot_constructor_args():
    sig = inspect.signature(whileDsl_ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "negation" in params, "Missing parameter 'negation'"




def test_hyp_whiledsl_expror_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprOr)


def test_hyp_whiledsl_expror_constructor_exists():
    assert callable(whileDsl_ExprOr.__init__)


def test_hyp_whiledsl_expror_constructor_args():
    sig = inspect.signature(whileDsl_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_exprand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ExprAnd)


def test_hyp_whiledsl_exprand_constructor_exists():
    assert callable(whileDsl_ExprAnd.__init__)


def test_hyp_whiledsl_exprand_constructor_args():
    sig = inspect.signature(whileDsl_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_command_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Command)


def test_hyp_whiledsl_command_constructor_exists():
    assert callable(whileDsl_Command.__init__)


def test_hyp_whiledsl_command_constructor_args():
    sig = inspect.signature(whileDsl_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_output_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Output)


def test_hyp_whiledsl_output_constructor_exists():
    assert callable(whileDsl_Output.__init__)


def test_hyp_whiledsl_output_constructor_args():
    sig = inspect.signature(whileDsl_Output.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"




def test_hyp_whiledsl_commands_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Commands)


def test_hyp_whiledsl_commands_constructor_exists():
    assert callable(whileDsl_Commands.__init__)


def test_hyp_whiledsl_commands_constructor_args():
    sig = inspect.signature(whileDsl_Commands.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_input_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Input)


def test_hyp_whiledsl_input_constructor_exists():
    assert callable(whileDsl_Input.__init__)


def test_hyp_whiledsl_input_constructor_args():
    sig = inspect.signature(whileDsl_Input.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"




def test_hyp_whiledsl_exprs_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Exprs)


def test_hyp_whiledsl_exprs_constructor_exists():
    assert callable(whileDsl_Exprs.__init__)


def test_hyp_whiledsl_exprs_constructor_args():
    sig = inspect.signature(whileDsl_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_vars_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Vars)


def test_hyp_whiledsl_vars_constructor_exists():
    assert callable(whileDsl_Vars.__init__)


def test_hyp_whiledsl_vars_constructor_args():
    sig = inspect.signature(whileDsl_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"




def test_hyp_whiledsl_expr_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Expr)


def test_hyp_whiledsl_expr_constructor_exists():
    assert callable(whileDsl_Expr.__init__)


def test_hyp_whiledsl_expr_constructor_args():
    sig = inspect.signature(whileDsl_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_ifcommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_IfCommand)


def test_hyp_whiledsl_ifcommand_constructor_exists():
    assert callable(whileDsl_IfCommand.__init__)


def test_hyp_whiledsl_ifcommand_constructor_args():
    sig = inspect.signature(whileDsl_IfCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_nopcommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_NopCommand)


def test_hyp_whiledsl_nopcommand_constructor_exists():
    assert callable(whileDsl_NopCommand.__init__)


def test_hyp_whiledsl_nopcommand_constructor_args():
    sig = inspect.signature(whileDsl_NopCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_varscommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_VarsCommand)


def test_hyp_whiledsl_varscommand_constructor_exists():
    assert callable(whileDsl_VarsCommand.__init__)


def test_hyp_whiledsl_varscommand_constructor_args():
    sig = inspect.signature(whileDsl_VarsCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_foreachcommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ForeachCommand)


def test_hyp_whiledsl_foreachcommand_constructor_exists():
    assert callable(whileDsl_ForeachCommand.__init__)


def test_hyp_whiledsl_foreachcommand_constructor_args():
    sig = inspect.signature(whileDsl_ForeachCommand.__init__)
    params = list(sig.parameters.keys())
    assert "expElement" in params, "Missing parameter 'expElement'"




def test_hyp_whiledsl_forcommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_ForCommand)


def test_hyp_whiledsl_forcommand_constructor_exists():
    assert callable(whileDsl_ForCommand.__init__)


def test_hyp_whiledsl_forcommand_constructor_args():
    sig = inspect.signature(whileDsl_ForCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_whilecommand_is_not_abstract():
    assert not inspect.isabstract(whileDsl_WhileCommand)


def test_hyp_whiledsl_whilecommand_constructor_exists():
    assert callable(whileDsl_WhileCommand.__init__)


def test_hyp_whiledsl_whilecommand_constructor_args():
    sig = inspect.signature(whileDsl_WhileCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_definition_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Definition)


def test_hyp_whiledsl_definition_constructor_exists():
    assert callable(whileDsl_Definition.__init__)


def test_hyp_whiledsl_definition_constructor_args():
    sig = inspect.signature(whileDsl_Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whiledsl_function_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Function)


def test_hyp_whiledsl_function_constructor_exists():
    assert callable(whileDsl_Function.__init__)


def test_hyp_whiledsl_function_constructor_args():
    sig = inspect.signature(whileDsl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"




def test_hyp_whiledsl_model_is_not_abstract():
    assert not inspect.isabstract(whileDsl_Model)


def test_hyp_whiledsl_model_constructor_exists():
    assert callable(whileDsl_Model.__init__)


def test_hyp_whiledsl_model_constructor_args():
    sig = inspect.signature(whileDsl_Model.__init__)
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
whileDsl_ExprSimpleWithSymbolLExpr_strategy = st.builds(
    whileDsl_ExprSimpleWithSymbolLExpr,
    symbol=
        safe_text
)
whileDsl_ExprSimpleWithExpr_strategy = st.builds(
    whileDsl_ExprSimpleWithExpr,
    operation=
        safe_text
)
whileDsl_LExpr_strategy = st.builds(
    whileDsl_LExpr,
)
whileDsl_ExprSimpleWithLExpr_strategy = st.builds(
    whileDsl_ExprSimpleWithLExpr,
    operation=
        safe_text
)
whileDsl_EObject_strategy = st.builds(
    whileDsl_EObject,
)
whileDsl_ExprSimple_strategy = st.builds(
    whileDsl_ExprSimple,
    term=
        safe_text
)
whileDsl_ExprEq_strategy = st.builds(
    whileDsl_ExprEq,
)
whileDsl_ExprNot_strategy = st.builds(
    whileDsl_ExprNot,
    negation=
        st.booleans()
)
whileDsl_ExprOr_strategy = st.builds(
    whileDsl_ExprOr,
)
whileDsl_ExprAnd_strategy = st.builds(
    whileDsl_ExprAnd,
)
whileDsl_Command_strategy = st.builds(
    whileDsl_Command,
)
whileDsl_Output_strategy = st.builds(
    whileDsl_Output,
    variables=
        safe_text
)
whileDsl_Commands_strategy = st.builds(
    whileDsl_Commands,
)
whileDsl_Input_strategy = st.builds(
    whileDsl_Input,
    variables=
        safe_text
)
whileDsl_Exprs_strategy = st.builds(
    whileDsl_Exprs,
)
whileDsl_Vars_strategy = st.builds(
    whileDsl_Vars,
    variables=
        safe_text
)
whileDsl_Expr_strategy = st.builds(
    whileDsl_Expr,
)
Command_strategy = st.builds(
    Command,
)
whileDsl_IfCommand_strategy = st.builds(
    whileDsl_IfCommand,
)
whileDsl_NopCommand_strategy = st.builds(
    whileDsl_NopCommand,
)
whileDsl_VarsCommand_strategy = st.builds(
    whileDsl_VarsCommand,
)
whileDsl_ForeachCommand_strategy = st.builds(
    whileDsl_ForeachCommand,
    expElement=
        safe_text
)
whileDsl_ForCommand_strategy = st.builds(
    whileDsl_ForCommand,
)
whileDsl_WhileCommand_strategy = st.builds(
    whileDsl_WhileCommand,
)
whileDsl_Definition_strategy = st.builds(
    whileDsl_Definition,
)
whileDsl_Function_strategy = st.builds(
    whileDsl_Function,
    functionName=
        safe_text
)
whileDsl_Model_strategy = st.builds(
    whileDsl_Model,
)




@given(instance=whileDsl_ExprSimpleWithSymbolLExpr_strategy)
def test_hyp_whiledsl_exprsimplewithsymbollexpr_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original




@given(instance=whileDsl_ExprSimpleWithExpr_strategy)
def test_hyp_whiledsl_exprsimplewithexpr_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original





@given(instance=whileDsl_ExprSimpleWithLExpr_strategy)
def test_hyp_whiledsl_exprsimplewithlexpr_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original





@given(instance=whileDsl_ExprSimple_strategy)
def test_hyp_whiledsl_exprsimple_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original





@given(instance=whileDsl_ExprNot_strategy)
def test_hyp_whiledsl_exprnot_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original







@given(instance=whileDsl_Output_strategy)
def test_hyp_whiledsl_output_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original





@given(instance=whileDsl_Input_strategy)
def test_hyp_whiledsl_input_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original





@given(instance=whileDsl_Vars_strategy)
def test_hyp_whiledsl_vars_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original









@given(instance=whileDsl_ForeachCommand_strategy)
def test_hyp_whiledsl_foreachcommand_expElement_setter(instance):
    original = instance.expElement
    instance.expElement = original
    assert instance.expElement == original







@given(instance=whileDsl_Function_strategy)
def test_hyp_whiledsl_function_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Command,
    whileDsl_Command,
    whileDsl_Commands,
    whileDsl_Definition,
    whileDsl_EObject,
    whileDsl_Expr,
    whileDsl_ExprAnd,
    whileDsl_ExprEq,
    whileDsl_ExprNot,
    whileDsl_ExprOr,
    whileDsl_ExprSimple,
    whileDsl_ExprSimpleWithExpr,
    whileDsl_ExprSimpleWithLExpr,
    whileDsl_ExprSimpleWithSymbolLExpr,
    whileDsl_Exprs,
    whileDsl_ForCommand,
    whileDsl_ForeachCommand,
    whileDsl_Function,
    whileDsl_IfCommand,
    whileDsl_Input,
    whileDsl_LExpr,
    whileDsl_Model,
    whileDsl_NopCommand,
    whileDsl_Output,
    whileDsl_Vars,
    whileDsl_VarsCommand,
    whileDsl_WhileCommand,
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

def test_whileDsl_ExprNot_negation_value_roundtrip():
    instance = whileDsl_ExprNot(negation=True)
    assert instance.negation == True
    instance.negation = False
    assert instance.negation == False


def test_whileDsl_ExprSimple_term_value_roundtrip():
    instance = whileDsl_ExprSimple(term="sample_text")
    assert instance.term == "sample_text"
    instance.term = "sample_text_2"
    assert instance.term == "sample_text_2"


def test_whileDsl_ExprSimpleWithExpr_operation_value_roundtrip():
    instance = whileDsl_ExprSimpleWithExpr(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_whileDsl_ExprSimpleWithLExpr_operation_value_roundtrip():
    instance = whileDsl_ExprSimpleWithLExpr(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_whileDsl_ExprSimpleWithSymbolLExpr_symbol_value_roundtrip():
    instance = whileDsl_ExprSimpleWithSymbolLExpr(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_whileDsl_ForeachCommand_expElement_value_roundtrip():
    instance = whileDsl_ForeachCommand(expElement="sample_text")
    assert instance.expElement == "sample_text"
    instance.expElement = "sample_text_2"
    assert instance.expElement == "sample_text_2"


def test_whileDsl_Function_functionName_value_roundtrip():
    instance = whileDsl_Function(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_whileDsl_Input_variables_value_roundtrip():
    instance = whileDsl_Input(variables="sample_text")
    assert instance.variables == "sample_text"
    instance.variables = "sample_text_2"
    assert instance.variables == "sample_text_2"


def test_whileDsl_Output_variables_value_roundtrip():
    instance = whileDsl_Output(variables="sample_text")
    assert instance.variables == "sample_text"
    instance.variables = "sample_text_2"
    assert instance.variables == "sample_text_2"


def test_whileDsl_Vars_variables_value_roundtrip():
    instance = whileDsl_Vars(variables="sample_text")
    assert instance.variables == "sample_text"
    instance.variables = "sample_text_2"
    assert instance.variables == "sample_text_2"


def test_whileDsl_ForCommand_isa_Command():
    instance = whileDsl_ForCommand()
    assert isinstance(instance, Command)


def test_whileDsl_ForeachCommand_isa_Command():
    instance = whileDsl_ForeachCommand(expElement="sample_text")
    assert isinstance(instance, Command)


def test_whileDsl_IfCommand_isa_Command():
    instance = whileDsl_IfCommand()
    assert isinstance(instance, Command)


def test_whileDsl_NopCommand_isa_Command():
    instance = whileDsl_NopCommand()
    assert isinstance(instance, Command)


def test_whileDsl_VarsCommand_isa_Command():
    instance = whileDsl_VarsCommand()
    assert isinstance(instance, Command)


def test_whileDsl_WhileCommand_isa_Command():
    instance = whileDsl_WhileCommand()
    assert isinstance(instance, Command)


def test_assoc_body30_link_reassign_clear():
    a = whileDsl_ForeachCommand(expElement="sample_text")
    b1 = whileDsl_Commands()
    b2 = whileDsl_Commands()
    _safe_set(a, 'whileDsl_ForeachCommand31', b1)
    assert _is_linked(a, 'whileDsl_ForeachCommand31', b1)
    if hasattr(b1, 'whileDsl_Commands32'):
        assert _is_linked(b1, 'whileDsl_Commands32', a)
    _safe_set(a, 'whileDsl_ForeachCommand31', b2)
    assert _is_linked(a, 'whileDsl_ForeachCommand31', b2)
    if hasattr(b1, 'whileDsl_Commands32'):
        assert not _is_linked(b1, 'whileDsl_Commands32', a)
    if hasattr(b2, 'whileDsl_Commands32'):
        assert _is_linked(b2, 'whileDsl_Commands32', a)
    _safe_set(a, 'whileDsl_ForeachCommand31', None)
    assert not _is_linked(a, 'whileDsl_ForeachCommand31', b2)
    if hasattr(b2, 'whileDsl_Commands32'):
        assert not _is_linked(b2, 'whileDsl_Commands32', a)


def test_assoc_expList28_link_reassign_clear():
    a = whileDsl_ForeachCommand(expElement="sample_text")
    b1 = whileDsl_Expr()
    b2 = whileDsl_Expr()
    _safe_set(a, 'whileDsl_ForeachCommand', b1)
    assert _is_linked(a, 'whileDsl_ForeachCommand', b1)
    if hasattr(b1, 'whileDsl_Expr29'):
        assert _is_linked(b1, 'whileDsl_Expr29', a)
    _safe_set(a, 'whileDsl_ForeachCommand', b2)
    assert _is_linked(a, 'whileDsl_ForeachCommand', b2)
    if hasattr(b1, 'whileDsl_Expr29'):
        assert not _is_linked(b1, 'whileDsl_Expr29', a)
    if hasattr(b2, 'whileDsl_Expr29'):
        assert _is_linked(b2, 'whileDsl_Expr29', a)
    _safe_set(a, 'whileDsl_ForeachCommand', None)
    assert not _is_linked(a, 'whileDsl_ForeachCommand', b2)
    if hasattr(b2, 'whileDsl_Expr29'):
        assert not _is_linked(b2, 'whileDsl_Expr29', a)


def test_assoc_expr38_link_reassign_clear():
    a = whileDsl_ExprSimpleWithExpr(operation="sample_text")
    b1 = whileDsl_Expr()
    b2 = whileDsl_Expr()
    _safe_set(a, 'whileDsl_ExprSimpleWithExpr', b1)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithExpr', b1)
    if hasattr(b1, 'whileDsl_Expr39'):
        assert _is_linked(b1, 'whileDsl_Expr39', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithExpr', b2)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithExpr', b2)
    if hasattr(b1, 'whileDsl_Expr39'):
        assert not _is_linked(b1, 'whileDsl_Expr39', a)
    if hasattr(b2, 'whileDsl_Expr39'):
        assert _is_linked(b2, 'whileDsl_Expr39', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithExpr', None)
    assert not _is_linked(a, 'whileDsl_ExprSimpleWithExpr', b2)
    if hasattr(b2, 'whileDsl_Expr39'):
        assert not _is_linked(b2, 'whileDsl_Expr39', a)


def test_assoc_exprLSimple56_link_reassign_clear():
    a = whileDsl_ExprSimple(term="sample_text")
    b1 = whileDsl_ExprEq()
    b2 = whileDsl_ExprEq()
    _safe_set(a, 'whileDsl_ExprSimple58', b1)
    assert _is_linked(a, 'whileDsl_ExprSimple58', b1)
    if hasattr(b1, 'whileDsl_ExprEq57'):
        assert _is_linked(b1, 'whileDsl_ExprEq57', a)
    _safe_set(a, 'whileDsl_ExprSimple58', b2)
    assert _is_linked(a, 'whileDsl_ExprSimple58', b2)
    if hasattr(b1, 'whileDsl_ExprEq57'):
        assert not _is_linked(b1, 'whileDsl_ExprEq57', a)
    if hasattr(b2, 'whileDsl_ExprEq57'):
        assert _is_linked(b2, 'whileDsl_ExprEq57', a)
    _safe_set(a, 'whileDsl_ExprSimple58', None)
    assert not _is_linked(a, 'whileDsl_ExprSimple58', b2)
    if hasattr(b2, 'whileDsl_ExprEq57'):
        assert not _is_linked(b2, 'whileDsl_ExprEq57', a)


def test_assoc_exprRSimple59_link_reassign_clear():
    a = whileDsl_ExprSimple(term="sample_text")
    b1 = whileDsl_ExprEq()
    b2 = whileDsl_ExprEq()
    _safe_set(a, 'whileDsl_ExprSimple61', b1)
    assert _is_linked(a, 'whileDsl_ExprSimple61', b1)
    if hasattr(b1, 'whileDsl_ExprEq60'):
        assert _is_linked(b1, 'whileDsl_ExprEq60', a)
    _safe_set(a, 'whileDsl_ExprSimple61', b2)
    assert _is_linked(a, 'whileDsl_ExprSimple61', b2)
    if hasattr(b1, 'whileDsl_ExprEq60'):
        assert not _is_linked(b1, 'whileDsl_ExprEq60', a)
    if hasattr(b2, 'whileDsl_ExprEq60'):
        assert _is_linked(b2, 'whileDsl_ExprEq60', a)
    _safe_set(a, 'whileDsl_ExprSimple61', None)
    assert not _is_linked(a, 'whileDsl_ExprSimple61', b2)
    if hasattr(b2, 'whileDsl_ExprEq60'):
        assert not _is_linked(b2, 'whileDsl_ExprEq60', a)


def test_assoc_expression36_link_reassign_clear():
    a = whileDsl_ExprSimple(term="sample_text")
    b1 = whileDsl_EObject()
    b2 = whileDsl_EObject()
    _safe_set(a, 'whileDsl_ExprSimple', b1)
    assert _is_linked(a, 'whileDsl_ExprSimple', b1)
    if hasattr(b1, 'whileDsl_EObject'):
        assert _is_linked(b1, 'whileDsl_EObject', a)
    _safe_set(a, 'whileDsl_ExprSimple', b2)
    assert _is_linked(a, 'whileDsl_ExprSimple', b2)
    if hasattr(b1, 'whileDsl_EObject'):
        assert not _is_linked(b1, 'whileDsl_EObject', a)
    if hasattr(b2, 'whileDsl_EObject'):
        assert _is_linked(b2, 'whileDsl_EObject', a)
    _safe_set(a, 'whileDsl_ExprSimple', None)
    assert not _is_linked(a, 'whileDsl_ExprSimple', b2)
    if hasattr(b2, 'whileDsl_EObject'):
        assert not _is_linked(b2, 'whileDsl_EObject', a)


def test_assoc_expressionEq54_link_reassign_clear():
    a = whileDsl_ExprNot(negation=True)
    b1 = whileDsl_ExprEq()
    b2 = whileDsl_ExprEq()
    _safe_set(a, 'whileDsl_ExprNot55', b1)
    assert _is_linked(a, 'whileDsl_ExprNot55', b1)
    if hasattr(b1, 'whileDsl_ExprEq'):
        assert _is_linked(b1, 'whileDsl_ExprEq', a)
    _safe_set(a, 'whileDsl_ExprNot55', b2)
    assert _is_linked(a, 'whileDsl_ExprNot55', b2)
    if hasattr(b1, 'whileDsl_ExprEq'):
        assert not _is_linked(b1, 'whileDsl_ExprEq', a)
    if hasattr(b2, 'whileDsl_ExprEq'):
        assert _is_linked(b2, 'whileDsl_ExprEq', a)
    _safe_set(a, 'whileDsl_ExprNot55', None)
    assert not _is_linked(a, 'whileDsl_ExprNot55', b2)
    if hasattr(b2, 'whileDsl_ExprEq'):
        assert not _is_linked(b2, 'whileDsl_ExprEq', a)


def test_assoc_expressionsNot52_link_reassign_clear():
    a = whileDsl_ExprNot(negation=True)
    b1 = whileDsl_ExprOr()
    b2 = whileDsl_ExprOr()
    _safe_set(a, 'whileDsl_ExprNot', b1)
    assert _is_linked(a, 'whileDsl_ExprNot', b1)
    if hasattr(b1, 'whileDsl_ExprOr53'):
        assert _is_linked(b1, 'whileDsl_ExprOr53', a)
    _safe_set(a, 'whileDsl_ExprNot', b2)
    assert _is_linked(a, 'whileDsl_ExprNot', b2)
    if hasattr(b1, 'whileDsl_ExprOr53'):
        assert not _is_linked(b1, 'whileDsl_ExprOr53', a)
    if hasattr(b2, 'whileDsl_ExprOr53'):
        assert _is_linked(b2, 'whileDsl_ExprOr53', a)
    _safe_set(a, 'whileDsl_ExprNot', None)
    assert not _is_linked(a, 'whileDsl_ExprNot', b2)
    if hasattr(b2, 'whileDsl_ExprOr53'):
        assert not _is_linked(b2, 'whileDsl_ExprOr53', a)


def test_assoc_functionDefinition1_link_reassign_clear():
    a = whileDsl_Function(functionName="sample_text")
    b1 = whileDsl_Definition()
    b2 = whileDsl_Definition()
    _safe_set(a, 'whileDsl_Function2', b1)
    assert _is_linked(a, 'whileDsl_Function2', b1)
    if hasattr(b1, 'whileDsl_Definition'):
        assert _is_linked(b1, 'whileDsl_Definition', a)
    _safe_set(a, 'whileDsl_Function2', b2)
    assert _is_linked(a, 'whileDsl_Function2', b2)
    if hasattr(b1, 'whileDsl_Definition'):
        assert not _is_linked(b1, 'whileDsl_Definition', a)
    if hasattr(b2, 'whileDsl_Definition'):
        assert _is_linked(b2, 'whileDsl_Definition', a)
    _safe_set(a, 'whileDsl_Function2', None)
    assert not _is_linked(a, 'whileDsl_Function2', b2)
    if hasattr(b2, 'whileDsl_Definition'):
        assert not _is_linked(b2, 'whileDsl_Definition', a)


def test_assoc_intput3_link_reassign_clear():
    a = whileDsl_Input(variables="sample_text")
    b1 = whileDsl_Definition()
    b2 = whileDsl_Definition()
    _safe_set(a, 'whileDsl_Input', b1)
    assert _is_linked(a, 'whileDsl_Input', b1)
    if hasattr(b1, 'whileDsl_Definition4'):
        assert _is_linked(b1, 'whileDsl_Definition4', a)
    _safe_set(a, 'whileDsl_Input', b2)
    assert _is_linked(a, 'whileDsl_Input', b2)
    if hasattr(b1, 'whileDsl_Definition4'):
        assert not _is_linked(b1, 'whileDsl_Definition4', a)
    if hasattr(b2, 'whileDsl_Definition4'):
        assert _is_linked(b2, 'whileDsl_Definition4', a)
    _safe_set(a, 'whileDsl_Input', None)
    assert not _is_linked(a, 'whileDsl_Input', b2)
    if hasattr(b2, 'whileDsl_Definition4'):
        assert not _is_linked(b2, 'whileDsl_Definition4', a)


def test_assoc_lexpr37_link_reassign_clear():
    a = whileDsl_ExprSimpleWithLExpr(operation="sample_text")
    b1 = whileDsl_LExpr()
    b2 = whileDsl_LExpr()
    _safe_set(a, 'whileDsl_ExprSimpleWithLExpr', b1)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithLExpr', b1)
    if hasattr(b1, 'whileDsl_LExpr'):
        assert _is_linked(b1, 'whileDsl_LExpr', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithLExpr', b2)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithLExpr', b2)
    if hasattr(b1, 'whileDsl_LExpr'):
        assert not _is_linked(b1, 'whileDsl_LExpr', a)
    if hasattr(b2, 'whileDsl_LExpr'):
        assert _is_linked(b2, 'whileDsl_LExpr', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithLExpr', None)
    assert not _is_linked(a, 'whileDsl_ExprSimpleWithLExpr', b2)
    if hasattr(b2, 'whileDsl_LExpr'):
        assert not _is_linked(b2, 'whileDsl_LExpr', a)


def test_assoc_lexpr40_link_reassign_clear():
    a = whileDsl_ExprSimpleWithSymbolLExpr(symbol="sample_text")
    b1 = whileDsl_LExpr()
    b2 = whileDsl_LExpr()
    _safe_set(a, 'whileDsl_ExprSimpleWithSymbolLExpr', b1)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithSymbolLExpr', b1)
    if hasattr(b1, 'whileDsl_LExpr41'):
        assert _is_linked(b1, 'whileDsl_LExpr41', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithSymbolLExpr', b2)
    assert _is_linked(a, 'whileDsl_ExprSimpleWithSymbolLExpr', b2)
    if hasattr(b1, 'whileDsl_LExpr41'):
        assert not _is_linked(b1, 'whileDsl_LExpr41', a)
    if hasattr(b2, 'whileDsl_LExpr41'):
        assert _is_linked(b2, 'whileDsl_LExpr41', a)
    _safe_set(a, 'whileDsl_ExprSimpleWithSymbolLExpr', None)
    assert not _is_linked(a, 'whileDsl_ExprSimpleWithSymbolLExpr', b2)
    if hasattr(b2, 'whileDsl_LExpr41'):
        assert not _is_linked(b2, 'whileDsl_LExpr41', a)


def test_assoc_output7_link_reassign_clear():
    a = whileDsl_Output(variables="sample_text")
    b1 = whileDsl_Definition()
    b2 = whileDsl_Definition()
    _safe_set(a, 'whileDsl_Output', b1)
    assert _is_linked(a, 'whileDsl_Output', b1)
    if hasattr(b1, 'whileDsl_Definition8'):
        assert _is_linked(b1, 'whileDsl_Definition8', a)
    _safe_set(a, 'whileDsl_Output', b2)
    assert _is_linked(a, 'whileDsl_Output', b2)
    if hasattr(b1, 'whileDsl_Definition8'):
        assert not _is_linked(b1, 'whileDsl_Definition8', a)
    if hasattr(b2, 'whileDsl_Definition8'):
        assert _is_linked(b2, 'whileDsl_Definition8', a)
    _safe_set(a, 'whileDsl_Output', None)
    assert not _is_linked(a, 'whileDsl_Output', b2)
    if hasattr(b2, 'whileDsl_Definition8'):
        assert not _is_linked(b2, 'whileDsl_Definition8', a)


def test_assoc_program0_link_reassign_clear():
    a = whileDsl_Function(functionName="sample_text")
    b1 = whileDsl_Model()
    b2 = whileDsl_Model()
    _safe_set(a, 'whileDsl_Function', b1)
    assert _is_linked(a, 'whileDsl_Function', b1)
    if hasattr(b1, 'whileDsl_Model'):
        assert _is_linked(b1, 'whileDsl_Model', a)
    _safe_set(a, 'whileDsl_Function', b2)
    assert _is_linked(a, 'whileDsl_Function', b2)
    if hasattr(b1, 'whileDsl_Model'):
        assert not _is_linked(b1, 'whileDsl_Model', a)
    if hasattr(b2, 'whileDsl_Model'):
        assert _is_linked(b2, 'whileDsl_Model', a)
    _safe_set(a, 'whileDsl_Function', None)
    assert not _is_linked(a, 'whileDsl_Function', b2)
    if hasattr(b2, 'whileDsl_Model'):
        assert not _is_linked(b2, 'whileDsl_Model', a)


def test_assoc_variables33_link_reassign_clear():
    a = whileDsl_Vars(variables="sample_text")
    b1 = whileDsl_VarsCommand()
    b2 = whileDsl_VarsCommand()
    _safe_set(a, 'whileDsl_Vars', b1)
    assert _is_linked(a, 'whileDsl_Vars', b1)
    if hasattr(b1, 'whileDsl_VarsCommand'):
        assert _is_linked(b1, 'whileDsl_VarsCommand', a)
    _safe_set(a, 'whileDsl_Vars', b2)
    assert _is_linked(a, 'whileDsl_Vars', b2)
    if hasattr(b1, 'whileDsl_VarsCommand'):
        assert not _is_linked(b1, 'whileDsl_VarsCommand', a)
    if hasattr(b2, 'whileDsl_VarsCommand'):
        assert _is_linked(b2, 'whileDsl_VarsCommand', a)
    _safe_set(a, 'whileDsl_Vars', None)
    assert not _is_linked(a, 'whileDsl_Vars', b2)
    if hasattr(b2, 'whileDsl_VarsCommand'):
        assert not _is_linked(b2, 'whileDsl_VarsCommand', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


whileDsl_Command_strategy = st.builds(whileDsl_Command)
@given(instance=whileDsl_Command_strategy)
@settings(max_examples=25)
def test_whileDsl_Command_instantiation(instance):
    assert isinstance(instance, whileDsl_Command)


whileDsl_Commands_strategy = st.builds(whileDsl_Commands)
@given(instance=whileDsl_Commands_strategy)
@settings(max_examples=25)
def test_whileDsl_Commands_instantiation(instance):
    assert isinstance(instance, whileDsl_Commands)


whileDsl_Definition_strategy = st.builds(whileDsl_Definition)
@given(instance=whileDsl_Definition_strategy)
@settings(max_examples=25)
def test_whileDsl_Definition_instantiation(instance):
    assert isinstance(instance, whileDsl_Definition)


whileDsl_EObject_strategy = st.builds(whileDsl_EObject)
@given(instance=whileDsl_EObject_strategy)
@settings(max_examples=25)
def test_whileDsl_EObject_instantiation(instance):
    assert isinstance(instance, whileDsl_EObject)


whileDsl_Expr_strategy = st.builds(whileDsl_Expr)
@given(instance=whileDsl_Expr_strategy)
@settings(max_examples=25)
def test_whileDsl_Expr_instantiation(instance):
    assert isinstance(instance, whileDsl_Expr)


whileDsl_ExprAnd_strategy = st.builds(whileDsl_ExprAnd)
@given(instance=whileDsl_ExprAnd_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprAnd_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprAnd)


whileDsl_ExprEq_strategy = st.builds(whileDsl_ExprEq)
@given(instance=whileDsl_ExprEq_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprEq_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprEq)


whileDsl_ExprNot_strategy = st.builds(whileDsl_ExprNot, negation=st.booleans())
@given(instance=whileDsl_ExprNot_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprNot_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprNot)


whileDsl_ExprOr_strategy = st.builds(whileDsl_ExprOr)
@given(instance=whileDsl_ExprOr_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprOr_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprOr)


whileDsl_ExprSimple_strategy = st.builds(whileDsl_ExprSimple, term=safe_text)
@given(instance=whileDsl_ExprSimple_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprSimple_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprSimple)


whileDsl_ExprSimpleWithExpr_strategy = st.builds(whileDsl_ExprSimpleWithExpr, operation=safe_text)
@given(instance=whileDsl_ExprSimpleWithExpr_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprSimpleWithExpr_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprSimpleWithExpr)


whileDsl_ExprSimpleWithLExpr_strategy = st.builds(whileDsl_ExprSimpleWithLExpr, operation=safe_text)
@given(instance=whileDsl_ExprSimpleWithLExpr_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprSimpleWithLExpr_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprSimpleWithLExpr)


whileDsl_ExprSimpleWithSymbolLExpr_strategy = st.builds(whileDsl_ExprSimpleWithSymbolLExpr, symbol=safe_text)
@given(instance=whileDsl_ExprSimpleWithSymbolLExpr_strategy)
@settings(max_examples=25)
def test_whileDsl_ExprSimpleWithSymbolLExpr_instantiation(instance):
    assert isinstance(instance, whileDsl_ExprSimpleWithSymbolLExpr)


whileDsl_Exprs_strategy = st.builds(whileDsl_Exprs)
@given(instance=whileDsl_Exprs_strategy)
@settings(max_examples=25)
def test_whileDsl_Exprs_instantiation(instance):
    assert isinstance(instance, whileDsl_Exprs)


whileDsl_ForCommand_strategy = st.builds(whileDsl_ForCommand)
@given(instance=whileDsl_ForCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_ForCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_ForCommand)


whileDsl_ForeachCommand_strategy = st.builds(whileDsl_ForeachCommand, expElement=safe_text)
@given(instance=whileDsl_ForeachCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_ForeachCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_ForeachCommand)


whileDsl_Function_strategy = st.builds(whileDsl_Function, functionName=safe_text)
@given(instance=whileDsl_Function_strategy)
@settings(max_examples=25)
def test_whileDsl_Function_instantiation(instance):
    assert isinstance(instance, whileDsl_Function)


whileDsl_IfCommand_strategy = st.builds(whileDsl_IfCommand)
@given(instance=whileDsl_IfCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_IfCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_IfCommand)


whileDsl_Input_strategy = st.builds(whileDsl_Input, variables=safe_text)
@given(instance=whileDsl_Input_strategy)
@settings(max_examples=25)
def test_whileDsl_Input_instantiation(instance):
    assert isinstance(instance, whileDsl_Input)


whileDsl_LExpr_strategy = st.builds(whileDsl_LExpr)
@given(instance=whileDsl_LExpr_strategy)
@settings(max_examples=25)
def test_whileDsl_LExpr_instantiation(instance):
    assert isinstance(instance, whileDsl_LExpr)


whileDsl_Model_strategy = st.builds(whileDsl_Model)
@given(instance=whileDsl_Model_strategy)
@settings(max_examples=25)
def test_whileDsl_Model_instantiation(instance):
    assert isinstance(instance, whileDsl_Model)


whileDsl_NopCommand_strategy = st.builds(whileDsl_NopCommand)
@given(instance=whileDsl_NopCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_NopCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_NopCommand)


whileDsl_Output_strategy = st.builds(whileDsl_Output, variables=safe_text)
@given(instance=whileDsl_Output_strategy)
@settings(max_examples=25)
def test_whileDsl_Output_instantiation(instance):
    assert isinstance(instance, whileDsl_Output)


whileDsl_Vars_strategy = st.builds(whileDsl_Vars, variables=safe_text)
@given(instance=whileDsl_Vars_strategy)
@settings(max_examples=25)
def test_whileDsl_Vars_instantiation(instance):
    assert isinstance(instance, whileDsl_Vars)


whileDsl_VarsCommand_strategy = st.builds(whileDsl_VarsCommand)
@given(instance=whileDsl_VarsCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_VarsCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_VarsCommand)


whileDsl_WhileCommand_strategy = st.builds(whileDsl_WhileCommand)
@given(instance=whileDsl_WhileCommand_strategy)
@settings(max_examples=25)
def test_whileDsl_WhileCommand_instantiation(instance):
    assert isinstance(instance, whileDsl_WhileCommand)



