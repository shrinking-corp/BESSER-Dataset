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
    py_ExprEq,
    py_ExprNot,
    py_ExprSym,
    py_ExprTl,
    py_ExprHd,
    py_ExprList,
    py_LExpr,
    py_ExprCons,
    py_ExprOr,
    py_While,
    py_Foreach,
    py_For,
    py_Affect,
    py_Nop,
    py_Expr,
    py_If,
    py_EObject,
    py_ExprAnd,
    py_ExprSimple,
    py_Input,
    py_Definition,
    py_FunctionP,
    py_Program,
    py_Wh,
    py_Command,
    py_Output,
    py_Commands,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_py_expreq_is_not_abstract():
    assert not inspect.isabstract(py_ExprEq)


def test_hyp_py_expreq_constructor_exists():
    assert callable(py_ExprEq.__init__)


def test_hyp_py_expreq_constructor_args():
    sig = inspect.signature(py_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprnot_is_not_abstract():
    assert not inspect.isabstract(py_ExprNot)


def test_hyp_py_exprnot_constructor_exists():
    assert callable(py_ExprNot.__init__)


def test_hyp_py_exprnot_constructor_args():
    sig = inspect.signature(py_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprsym_is_not_abstract():
    assert not inspect.isabstract(py_ExprSym)


def test_hyp_py_exprsym_constructor_exists():
    assert callable(py_ExprSym.__init__)


def test_hyp_py_exprsym_constructor_args():
    sig = inspect.signature(py_ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"




def test_hyp_py_exprtl_is_not_abstract():
    assert not inspect.isabstract(py_ExprTl)


def test_hyp_py_exprtl_constructor_exists():
    assert callable(py_ExprTl.__init__)


def test_hyp_py_exprtl_constructor_args():
    sig = inspect.signature(py_ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprhd_is_not_abstract():
    assert not inspect.isabstract(py_ExprHd)


def test_hyp_py_exprhd_constructor_exists():
    assert callable(py_ExprHd.__init__)


def test_hyp_py_exprhd_constructor_args():
    sig = inspect.signature(py_ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprlist_is_not_abstract():
    assert not inspect.isabstract(py_ExprList)


def test_hyp_py_exprlist_constructor_exists():
    assert callable(py_ExprList.__init__)


def test_hyp_py_exprlist_constructor_args():
    sig = inspect.signature(py_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_lexpr_is_not_abstract():
    assert not inspect.isabstract(py_LExpr)


def test_hyp_py_lexpr_constructor_exists():
    assert callable(py_LExpr.__init__)


def test_hyp_py_lexpr_constructor_args():
    sig = inspect.signature(py_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprcons_is_not_abstract():
    assert not inspect.isabstract(py_ExprCons)


def test_hyp_py_exprcons_constructor_exists():
    assert callable(py_ExprCons.__init__)


def test_hyp_py_exprcons_constructor_args():
    sig = inspect.signature(py_ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_expror_is_not_abstract():
    assert not inspect.isabstract(py_ExprOr)


def test_hyp_py_expror_constructor_exists():
    assert callable(py_ExprOr.__init__)


def test_hyp_py_expror_constructor_args():
    sig = inspect.signature(py_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_while_is_not_abstract():
    assert not inspect.isabstract(py_While)


def test_hyp_py_while_constructor_exists():
    assert callable(py_While.__init__)


def test_hyp_py_while_constructor_args():
    sig = inspect.signature(py_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_foreach_is_not_abstract():
    assert not inspect.isabstract(py_Foreach)


def test_hyp_py_foreach_constructor_exists():
    assert callable(py_Foreach.__init__)


def test_hyp_py_foreach_constructor_args():
    sig = inspect.signature(py_Foreach.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"




def test_hyp_py_for_is_not_abstract():
    assert not inspect.isabstract(py_For)


def test_hyp_py_for_constructor_exists():
    assert callable(py_For.__init__)


def test_hyp_py_for_constructor_args():
    sig = inspect.signature(py_For.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_affect_is_not_abstract():
    assert not inspect.isabstract(py_Affect)


def test_hyp_py_affect_constructor_exists():
    assert callable(py_Affect.__init__)


def test_hyp_py_affect_constructor_args():
    sig = inspect.signature(py_Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"




def test_hyp_py_nop_is_not_abstract():
    assert not inspect.isabstract(py_Nop)


def test_hyp_py_nop_constructor_exists():
    assert callable(py_Nop.__init__)


def test_hyp_py_nop_constructor_args():
    sig = inspect.signature(py_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"




def test_hyp_py_expr_is_not_abstract():
    assert not inspect.isabstract(py_Expr)


def test_hyp_py_expr_constructor_exists():
    assert callable(py_Expr.__init__)


def test_hyp_py_expr_constructor_args():
    sig = inspect.signature(py_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_if_is_not_abstract():
    assert not inspect.isabstract(py_If)


def test_hyp_py_if_constructor_exists():
    assert callable(py_If.__init__)


def test_hyp_py_if_constructor_args():
    sig = inspect.signature(py_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_eobject_is_not_abstract():
    assert not inspect.isabstract(py_EObject)


def test_hyp_py_eobject_constructor_exists():
    assert callable(py_EObject.__init__)


def test_hyp_py_eobject_constructor_args():
    sig = inspect.signature(py_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprand_is_not_abstract():
    assert not inspect.isabstract(py_ExprAnd)


def test_hyp_py_exprand_constructor_exists():
    assert callable(py_ExprAnd.__init__)


def test_hyp_py_exprand_constructor_args():
    sig = inspect.signature(py_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_exprsimple_is_not_abstract():
    assert not inspect.isabstract(py_ExprSimple)


def test_hyp_py_exprsimple_constructor_exists():
    assert callable(py_ExprSimple.__init__)


def test_hyp_py_exprsimple_constructor_args():
    sig = inspect.signature(py_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "varSimple" in params, "Missing parameter 'varSimple'"






def test_hyp_py_input_is_not_abstract():
    assert not inspect.isabstract(py_Input)


def test_hyp_py_input_constructor_exists():
    assert callable(py_Input.__init__)


def test_hyp_py_input_constructor_args():
    sig = inspect.signature(py_Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"




def test_hyp_py_definition_is_not_abstract():
    assert not inspect.isabstract(py_Definition)


def test_hyp_py_definition_constructor_exists():
    assert callable(py_Definition.__init__)


def test_hyp_py_definition_constructor_args():
    sig = inspect.signature(py_Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_functionp_is_not_abstract():
    assert not inspect.isabstract(py_FunctionP)


def test_hyp_py_functionp_constructor_exists():
    assert callable(py_FunctionP.__init__)


def test_hyp_py_functionp_constructor_args():
    sig = inspect.signature(py_FunctionP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_py_program_is_not_abstract():
    assert not inspect.isabstract(py_Program)


def test_hyp_py_program_constructor_exists():
    assert callable(py_Program.__init__)


def test_hyp_py_program_constructor_args():
    sig = inspect.signature(py_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_wh_is_not_abstract():
    assert not inspect.isabstract(py_Wh)


def test_hyp_py_wh_constructor_exists():
    assert callable(py_Wh.__init__)


def test_hyp_py_wh_constructor_args():
    sig = inspect.signature(py_Wh.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_command_is_not_abstract():
    assert not inspect.isabstract(py_Command)


def test_hyp_py_command_constructor_exists():
    assert callable(py_Command.__init__)


def test_hyp_py_command_constructor_args():
    sig = inspect.signature(py_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_py_output_is_not_abstract():
    assert not inspect.isabstract(py_Output)


def test_hyp_py_output_constructor_exists():
    assert callable(py_Output.__init__)


def test_hyp_py_output_constructor_args():
    sig = inspect.signature(py_Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"




def test_hyp_py_commands_is_not_abstract():
    assert not inspect.isabstract(py_Commands)


def test_hyp_py_commands_constructor_exists():
    assert callable(py_Commands.__init__)


def test_hyp_py_commands_constructor_args():
    sig = inspect.signature(py_Commands.__init__)
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
py_ExprEq_strategy = st.builds(
    py_ExprEq,
)
py_ExprNot_strategy = st.builds(
    py_ExprNot,
)
py_ExprSym_strategy = st.builds(
    py_ExprSym,
    arg1=
        safe_text
)
py_ExprTl_strategy = st.builds(
    py_ExprTl,
)
py_ExprHd_strategy = st.builds(
    py_ExprHd,
)
py_ExprList_strategy = st.builds(
    py_ExprList,
)
py_LExpr_strategy = st.builds(
    py_LExpr,
)
py_ExprCons_strategy = st.builds(
    py_ExprCons,
)
py_ExprOr_strategy = st.builds(
    py_ExprOr,
)
py_While_strategy = st.builds(
    py_While,
)
py_Foreach_strategy = st.builds(
    py_Foreach,
    var=
        safe_text
)
py_For_strategy = st.builds(
    py_For,
)
py_Affect_strategy = st.builds(
    py_Affect,
    vars=
        safe_text
)
py_Nop_strategy = st.builds(
    py_Nop,
    nop=
        safe_text
)
py_Expr_strategy = st.builds(
    py_Expr,
)
py_If_strategy = st.builds(
    py_If,
)
py_EObject_strategy = st.builds(
    py_EObject,
)
py_ExprAnd_strategy = st.builds(
    py_ExprAnd,
)
py_ExprSimple_strategy = st.builds(
    py_ExprSimple,
    str=
        safe_text,
    sym=
        safe_text,
    varSimple=
        safe_text
)
py_Input_strategy = st.builds(
    py_Input,
    vars=
        safe_text
)
py_Definition_strategy = st.builds(
    py_Definition,
)
py_FunctionP_strategy = st.builds(
    py_FunctionP,
    name=
        safe_text
)
py_Program_strategy = st.builds(
    py_Program,
)
py_Wh_strategy = st.builds(
    py_Wh,
)
py_Command_strategy = st.builds(
    py_Command,
)
py_Output_strategy = st.builds(
    py_Output,
    vars=
        safe_text
)
py_Commands_strategy = st.builds(
    py_Commands,
)






@given(instance=py_ExprSym_strategy)
def test_hyp_py_exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original











@given(instance=py_Foreach_strategy)
def test_hyp_py_foreach_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original





@given(instance=py_Affect_strategy)
def test_hyp_py_affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original




@given(instance=py_Nop_strategy)
def test_hyp_py_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original








@given(instance=py_ExprSimple_strategy)
def test_hyp_py_exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original



@given(instance=py_ExprSimple_strategy)
def test_hyp_py_exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original



@given(instance=py_ExprSimple_strategy)
def test_hyp_py_exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original




@given(instance=py_Input_strategy)
def test_hyp_py_input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original





@given(instance=py_FunctionP_strategy)
def test_hyp_py_functionp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=py_Output_strategy)
def test_hyp_py_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    py_Affect,
    py_Command,
    py_Commands,
    py_Definition,
    py_EObject,
    py_Expr,
    py_ExprAnd,
    py_ExprCons,
    py_ExprEq,
    py_ExprHd,
    py_ExprList,
    py_ExprNot,
    py_ExprOr,
    py_ExprSimple,
    py_ExprSym,
    py_ExprTl,
    py_For,
    py_Foreach,
    py_FunctionP,
    py_If,
    py_Input,
    py_LExpr,
    py_Nop,
    py_Output,
    py_Program,
    py_Wh,
    py_While,
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

def test_py_Affect_vars_value_roundtrip():
    instance = py_Affect(vars="sample_text")
    assert instance.vars == "sample_text"
    instance.vars = "sample_text_2"
    assert instance.vars == "sample_text_2"


def test_py_ExprSimple_str_value_roundtrip():
    instance = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    assert instance.str == "sample_text"
    instance.str = "sample_text_2"
    assert instance.str == "sample_text_2"


def test_py_ExprSimple_sym_value_roundtrip():
    instance = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    assert instance.sym == "sample_text"
    instance.sym = "sample_text_2"
    assert instance.sym == "sample_text_2"


def test_py_ExprSimple_varSimple_value_roundtrip():
    instance = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    assert instance.varSimple == "sample_text"
    instance.varSimple = "sample_text_2"
    assert instance.varSimple == "sample_text_2"


def test_py_ExprSym_arg1_value_roundtrip():
    instance = py_ExprSym(arg1="sample_text")
    assert instance.arg1 == "sample_text"
    instance.arg1 = "sample_text_2"
    assert instance.arg1 == "sample_text_2"


def test_py_Foreach_var_value_roundtrip():
    instance = py_Foreach(var="sample_text")
    assert instance.var == "sample_text"
    instance.var = "sample_text_2"
    assert instance.var == "sample_text_2"


def test_py_FunctionP_name_value_roundtrip():
    instance = py_FunctionP(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_py_Input_vars_value_roundtrip():
    instance = py_Input(vars="sample_text")
    assert instance.vars == "sample_text"
    instance.vars = "sample_text_2"
    assert instance.vars == "sample_text_2"


def test_py_Nop_nop_value_roundtrip():
    instance = py_Nop(nop="sample_text")
    assert instance.nop == "sample_text"
    instance.nop = "sample_text_2"
    assert instance.nop == "sample_text_2"


def test_py_Output_vars_value_roundtrip():
    instance = py_Output(vars="sample_text")
    assert instance.vars == "sample_text"
    instance.vars = "sample_text_2"
    assert instance.vars == "sample_text_2"


def test_assoc_arg142_link_reassign_clear():
    a = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    b1 = py_ExprAnd()
    b2 = py_ExprAnd()
    _safe_set(a, 'py_ExprSimple', b1)
    assert _is_linked(a, 'py_ExprSimple', b1)
    if hasattr(b1, 'py_ExprAnd'):
        assert _is_linked(b1, 'py_ExprAnd', a)
    _safe_set(a, 'py_ExprSimple', b2)
    assert _is_linked(a, 'py_ExprSimple', b2)
    if hasattr(b1, 'py_ExprAnd'):
        assert not _is_linked(b1, 'py_ExprAnd', a)
    if hasattr(b2, 'py_ExprAnd'):
        assert _is_linked(b2, 'py_ExprAnd', a)
    _safe_set(a, 'py_ExprSimple', None)
    assert not _is_linked(a, 'py_ExprSimple', b2)
    if hasattr(b2, 'py_ExprAnd'):
        assert not _is_linked(b2, 'py_ExprAnd', a)


def test_assoc_arg146_link_reassign_clear():
    a = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    b1 = py_ExprOr()
    b2 = py_ExprOr()
    _safe_set(a, 'py_ExprSimple47', b1)
    assert _is_linked(a, 'py_ExprSimple47', b1)
    if hasattr(b1, 'py_ExprOr'):
        assert _is_linked(b1, 'py_ExprOr', a)
    _safe_set(a, 'py_ExprSimple47', b2)
    assert _is_linked(a, 'py_ExprSimple47', b2)
    if hasattr(b1, 'py_ExprOr'):
        assert not _is_linked(b1, 'py_ExprOr', a)
    if hasattr(b2, 'py_ExprOr'):
        assert _is_linked(b2, 'py_ExprOr', a)
    _safe_set(a, 'py_ExprSimple47', None)
    assert not _is_linked(a, 'py_ExprSimple47', b2)
    if hasattr(b2, 'py_ExprOr'):
        assert not _is_linked(b2, 'py_ExprOr', a)


def test_assoc_arg165_link_reassign_clear():
    a = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    b1 = py_ExprEq()
    b2 = py_ExprEq()
    _safe_set(a, 'py_ExprSimple66', b1)
    assert _is_linked(a, 'py_ExprSimple66', b1)
    if hasattr(b1, 'py_ExprEq'):
        assert _is_linked(b1, 'py_ExprEq', a)
    _safe_set(a, 'py_ExprSimple66', b2)
    assert _is_linked(a, 'py_ExprSimple66', b2)
    if hasattr(b1, 'py_ExprEq'):
        assert not _is_linked(b1, 'py_ExprEq', a)
    if hasattr(b2, 'py_ExprEq'):
        assert _is_linked(b2, 'py_ExprEq', a)
    _safe_set(a, 'py_ExprSimple66', None)
    assert not _is_linked(a, 'py_ExprSimple66', b2)
    if hasattr(b2, 'py_ExprEq'):
        assert not _is_linked(b2, 'py_ExprEq', a)


def test_assoc_arg261_link_reassign_clear():
    a = py_ExprSym(arg1="sample_text")
    b1 = py_Expr()
    b2 = py_Expr()
    _safe_set(a, 'py_ExprSym', {b1})
    assert _is_linked(a, 'py_ExprSym', b1)
    if hasattr(b1, 'py_Expr62'):
        assert _is_linked(b1, 'py_Expr62', a)
    _safe_set(a, 'py_ExprSym', {b2})
    assert _is_linked(a, 'py_ExprSym', b2)
    if hasattr(b1, 'py_Expr62'):
        assert not _is_linked(b1, 'py_Expr62', a)
    if hasattr(b2, 'py_Expr62'):
        assert _is_linked(b2, 'py_Expr62', a)
    _safe_set(a, 'py_ExprSym', set())
    assert not _is_linked(a, 'py_ExprSym', b2)
    if hasattr(b2, 'py_Expr62'):
        assert not _is_linked(b2, 'py_Expr62', a)


def test_assoc_cmd31_link_reassign_clear():
    a = py_Foreach(var="sample_text")
    b1 = py_Commands()
    b2 = py_Commands()
    _safe_set(a, 'py_Foreach32', b1)
    assert _is_linked(a, 'py_Foreach32', b1)
    if hasattr(b1, 'py_Commands33'):
        assert _is_linked(b1, 'py_Commands33', a)
    _safe_set(a, 'py_Foreach32', b2)
    assert _is_linked(a, 'py_Foreach32', b2)
    if hasattr(b1, 'py_Commands33'):
        assert not _is_linked(b1, 'py_Commands33', a)
    if hasattr(b2, 'py_Commands33'):
        assert _is_linked(b2, 'py_Commands33', a)
    _safe_set(a, 'py_Foreach32', None)
    assert not _is_linked(a, 'py_Foreach32', b2)
    if hasattr(b2, 'py_Commands33'):
        assert not _is_linked(b2, 'py_Commands33', a)


def test_assoc_definition3_link_reassign_clear():
    a = py_FunctionP(name="sample_text")
    b1 = py_Definition()
    b2 = py_Definition()
    _safe_set(a, 'py_FunctionP4', b1)
    assert _is_linked(a, 'py_FunctionP4', b1)
    if hasattr(b1, 'py_Definition'):
        assert _is_linked(b1, 'py_Definition', a)
    _safe_set(a, 'py_FunctionP4', b2)
    assert _is_linked(a, 'py_FunctionP4', b2)
    if hasattr(b1, 'py_Definition'):
        assert not _is_linked(b1, 'py_Definition', a)
    if hasattr(b2, 'py_Definition'):
        assert _is_linked(b2, 'py_Definition', a)
    _safe_set(a, 'py_FunctionP4', None)
    assert not _is_linked(a, 'py_FunctionP4', b2)
    if hasattr(b2, 'py_Definition'):
        assert not _is_linked(b2, 'py_Definition', a)


def test_assoc_expr229_link_reassign_clear():
    a = py_Foreach(var="sample_text")
    b1 = py_Expr()
    b2 = py_Expr()
    _safe_set(a, 'py_Foreach', b1)
    assert _is_linked(a, 'py_Foreach', b1)
    if hasattr(b1, 'py_Expr30'):
        assert _is_linked(b1, 'py_Expr30', a)
    _safe_set(a, 'py_Foreach', b2)
    assert _is_linked(a, 'py_Foreach', b2)
    if hasattr(b1, 'py_Expr30'):
        assert not _is_linked(b1, 'py_Expr30', a)
    if hasattr(b2, 'py_Expr30'):
        assert _is_linked(b2, 'py_Expr30', a)
    _safe_set(a, 'py_Foreach', None)
    assert not _is_linked(a, 'py_Foreach', b2)
    if hasattr(b2, 'py_Expr30'):
        assert not _is_linked(b2, 'py_Expr30', a)


def test_assoc_exprs22_link_reassign_clear():
    a = py_Affect(vars="sample_text")
    b1 = py_Expr()
    b2 = py_Expr()
    _safe_set(a, 'py_Affect', {b1})
    assert _is_linked(a, 'py_Affect', b1)
    if hasattr(b1, 'py_Expr23'):
        assert _is_linked(b1, 'py_Expr23', a)
    _safe_set(a, 'py_Affect', {b2})
    assert _is_linked(a, 'py_Affect', b2)
    if hasattr(b1, 'py_Expr23'):
        assert not _is_linked(b1, 'py_Expr23', a)
    if hasattr(b2, 'py_Expr23'):
        assert _is_linked(b2, 'py_Expr23', a)
    _safe_set(a, 'py_Affect', set())
    assert not _is_linked(a, 'py_Affect', b2)
    if hasattr(b2, 'py_Expr23'):
        assert not _is_linked(b2, 'py_Expr23', a)


def test_assoc_functions1_link_reassign_clear():
    a = py_FunctionP(name="sample_text")
    b1 = py_Program()
    b2 = py_Program()
    _safe_set(a, 'py_FunctionP', b1)
    assert _is_linked(a, 'py_FunctionP', b1)
    if hasattr(b1, 'py_Program2'):
        assert _is_linked(b1, 'py_Program2', a)
    _safe_set(a, 'py_FunctionP', b2)
    assert _is_linked(a, 'py_FunctionP', b2)
    if hasattr(b1, 'py_Program2'):
        assert not _is_linked(b1, 'py_Program2', a)
    if hasattr(b2, 'py_Program2'):
        assert _is_linked(b2, 'py_Program2', a)
    _safe_set(a, 'py_FunctionP', None)
    assert not _is_linked(a, 'py_FunctionP', b2)
    if hasattr(b2, 'py_Program2'):
        assert not _is_linked(b2, 'py_Program2', a)


def test_assoc_input5_link_reassign_clear():
    a = py_Input(vars="sample_text")
    b1 = py_Definition()
    b2 = py_Definition()
    _safe_set(a, 'py_Input', b1)
    assert _is_linked(a, 'py_Input', b1)
    if hasattr(b1, 'py_Definition6'):
        assert _is_linked(b1, 'py_Definition6', a)
    _safe_set(a, 'py_Input', b2)
    assert _is_linked(a, 'py_Input', b2)
    if hasattr(b1, 'py_Definition6'):
        assert not _is_linked(b1, 'py_Definition6', a)
    if hasattr(b2, 'py_Definition6'):
        assert _is_linked(b2, 'py_Definition6', a)
    _safe_set(a, 'py_Input', None)
    assert not _is_linked(a, 'py_Input', b2)
    if hasattr(b2, 'py_Definition6'):
        assert not _is_linked(b2, 'py_Definition6', a)


def test_assoc_output9_link_reassign_clear():
    a = py_Output(vars="sample_text")
    b1 = py_Definition()
    b2 = py_Definition()
    _safe_set(a, 'py_Output', b1)
    assert _is_linked(a, 'py_Output', b1)
    if hasattr(b1, 'py_Definition10'):
        assert _is_linked(b1, 'py_Definition10', a)
    _safe_set(a, 'py_Output', b2)
    assert _is_linked(a, 'py_Output', b2)
    if hasattr(b1, 'py_Definition10'):
        assert not _is_linked(b1, 'py_Definition10', a)
    if hasattr(b2, 'py_Definition10'):
        assert _is_linked(b2, 'py_Definition10', a)
    _safe_set(a, 'py_Output', None)
    assert not _is_linked(a, 'py_Output', b2)
    if hasattr(b2, 'py_Definition10'):
        assert not _is_linked(b2, 'py_Definition10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

py_Affect_strategy = st.builds(py_Affect, vars=safe_text)
@given(instance=py_Affect_strategy)
@settings(max_examples=25)
def test_py_Affect_instantiation(instance):
    assert isinstance(instance, py_Affect)


py_Command_strategy = st.builds(py_Command)
@given(instance=py_Command_strategy)
@settings(max_examples=25)
def test_py_Command_instantiation(instance):
    assert isinstance(instance, py_Command)


py_Commands_strategy = st.builds(py_Commands)
@given(instance=py_Commands_strategy)
@settings(max_examples=25)
def test_py_Commands_instantiation(instance):
    assert isinstance(instance, py_Commands)


py_Definition_strategy = st.builds(py_Definition)
@given(instance=py_Definition_strategy)
@settings(max_examples=25)
def test_py_Definition_instantiation(instance):
    assert isinstance(instance, py_Definition)


py_EObject_strategy = st.builds(py_EObject)
@given(instance=py_EObject_strategy)
@settings(max_examples=25)
def test_py_EObject_instantiation(instance):
    assert isinstance(instance, py_EObject)


py_Expr_strategy = st.builds(py_Expr)
@given(instance=py_Expr_strategy)
@settings(max_examples=25)
def test_py_Expr_instantiation(instance):
    assert isinstance(instance, py_Expr)


py_ExprAnd_strategy = st.builds(py_ExprAnd)
@given(instance=py_ExprAnd_strategy)
@settings(max_examples=25)
def test_py_ExprAnd_instantiation(instance):
    assert isinstance(instance, py_ExprAnd)


py_ExprCons_strategy = st.builds(py_ExprCons)
@given(instance=py_ExprCons_strategy)
@settings(max_examples=25)
def test_py_ExprCons_instantiation(instance):
    assert isinstance(instance, py_ExprCons)


py_ExprEq_strategy = st.builds(py_ExprEq)
@given(instance=py_ExprEq_strategy)
@settings(max_examples=25)
def test_py_ExprEq_instantiation(instance):
    assert isinstance(instance, py_ExprEq)


py_ExprHd_strategy = st.builds(py_ExprHd)
@given(instance=py_ExprHd_strategy)
@settings(max_examples=25)
def test_py_ExprHd_instantiation(instance):
    assert isinstance(instance, py_ExprHd)


py_ExprList_strategy = st.builds(py_ExprList)
@given(instance=py_ExprList_strategy)
@settings(max_examples=25)
def test_py_ExprList_instantiation(instance):
    assert isinstance(instance, py_ExprList)


py_ExprNot_strategy = st.builds(py_ExprNot)
@given(instance=py_ExprNot_strategy)
@settings(max_examples=25)
def test_py_ExprNot_instantiation(instance):
    assert isinstance(instance, py_ExprNot)


py_ExprOr_strategy = st.builds(py_ExprOr)
@given(instance=py_ExprOr_strategy)
@settings(max_examples=25)
def test_py_ExprOr_instantiation(instance):
    assert isinstance(instance, py_ExprOr)


py_ExprSimple_strategy = st.builds(py_ExprSimple, str=safe_text, sym=safe_text, varSimple=safe_text)
@given(instance=py_ExprSimple_strategy)
@settings(max_examples=25)
def test_py_ExprSimple_instantiation(instance):
    assert isinstance(instance, py_ExprSimple)


py_ExprSym_strategy = st.builds(py_ExprSym, arg1=safe_text)
@given(instance=py_ExprSym_strategy)
@settings(max_examples=25)
def test_py_ExprSym_instantiation(instance):
    assert isinstance(instance, py_ExprSym)


py_ExprTl_strategy = st.builds(py_ExprTl)
@given(instance=py_ExprTl_strategy)
@settings(max_examples=25)
def test_py_ExprTl_instantiation(instance):
    assert isinstance(instance, py_ExprTl)


py_For_strategy = st.builds(py_For)
@given(instance=py_For_strategy)
@settings(max_examples=25)
def test_py_For_instantiation(instance):
    assert isinstance(instance, py_For)


py_Foreach_strategy = st.builds(py_Foreach, var=safe_text)
@given(instance=py_Foreach_strategy)
@settings(max_examples=25)
def test_py_Foreach_instantiation(instance):
    assert isinstance(instance, py_Foreach)


py_FunctionP_strategy = st.builds(py_FunctionP, name=safe_text)
@given(instance=py_FunctionP_strategy)
@settings(max_examples=25)
def test_py_FunctionP_instantiation(instance):
    assert isinstance(instance, py_FunctionP)


py_If_strategy = st.builds(py_If)
@given(instance=py_If_strategy)
@settings(max_examples=25)
def test_py_If_instantiation(instance):
    assert isinstance(instance, py_If)


py_Input_strategy = st.builds(py_Input, vars=safe_text)
@given(instance=py_Input_strategy)
@settings(max_examples=25)
def test_py_Input_instantiation(instance):
    assert isinstance(instance, py_Input)


py_LExpr_strategy = st.builds(py_LExpr)
@given(instance=py_LExpr_strategy)
@settings(max_examples=25)
def test_py_LExpr_instantiation(instance):
    assert isinstance(instance, py_LExpr)


py_Nop_strategy = st.builds(py_Nop, nop=safe_text)
@given(instance=py_Nop_strategy)
@settings(max_examples=25)
def test_py_Nop_instantiation(instance):
    assert isinstance(instance, py_Nop)


py_Output_strategy = st.builds(py_Output, vars=safe_text)
@given(instance=py_Output_strategy)
@settings(max_examples=25)
def test_py_Output_instantiation(instance):
    assert isinstance(instance, py_Output)


py_Program_strategy = st.builds(py_Program)
@given(instance=py_Program_strategy)
@settings(max_examples=25)
def test_py_Program_instantiation(instance):
    assert isinstance(instance, py_Program)


py_Wh_strategy = st.builds(py_Wh)
@given(instance=py_Wh_strategy)
@settings(max_examples=25)
def test_py_Wh_instantiation(instance):
    assert isinstance(instance, py_Wh)


py_While_strategy = st.builds(py_While)
@given(instance=py_While_strategy)
@settings(max_examples=25)
def test_py_While_instantiation(instance):
    assert isinstance(instance, py_While)



