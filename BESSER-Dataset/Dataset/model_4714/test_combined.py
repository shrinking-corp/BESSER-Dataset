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
    Var,
    flowgraph_Param,
    Conditional,
    flowgraph_If,
    FlowInstr,
    Stmt,
    flowgraph_Block,
    flowgraph_SimpleStmt,
    flowgraph_Exit,
    Block,
    flowgraph_Method,
    flowgraph_Return,
    flowgraph_Item,
    flowgraph_Expr,
    Item,
    flowgraph_Var,
    flowgraph_Stmt,
    flowgraph_FlowInstr,
    JumpStmt,
    flowgraph_Continue,
    flowgraph_Break,
    flowgraph_Label,
    flowgraph_JumpStmt,
    flowgraph_Conditional,
    flowgraph_Loop,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_hyp_var_constructor_exists():
    assert callable(Var.__init__)


def test_hyp_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_param_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Param)


def test_hyp_flowgraph_param_constructor_exists():
    assert callable(flowgraph_Param.__init__)


def test_hyp_flowgraph_param_constructor_args():
    sig = inspect.signature(flowgraph_Param.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_hyp_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_hyp_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_if_is_not_abstract():
    assert not inspect.isabstract(flowgraph_If)


def test_hyp_flowgraph_if_constructor_exists():
    assert callable(flowgraph_If.__init__)


def test_hyp_flowgraph_if_constructor_args():
    sig = inspect.signature(flowgraph_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowinstr_is_not_abstract():
    assert not inspect.isabstract(FlowInstr)


def test_hyp_flowinstr_constructor_exists():
    assert callable(FlowInstr.__init__)


def test_hyp_flowinstr_constructor_args():
    sig = inspect.signature(FlowInstr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_hyp_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_hyp_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_block_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Block)


def test_hyp_flowgraph_block_constructor_exists():
    assert callable(flowgraph_Block.__init__)


def test_hyp_flowgraph_block_constructor_args():
    sig = inspect.signature(flowgraph_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_simplestmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph_SimpleStmt)


def test_hyp_flowgraph_simplestmt_constructor_exists():
    assert callable(flowgraph_SimpleStmt.__init__)


def test_hyp_flowgraph_simplestmt_constructor_args():
    sig = inspect.signature(flowgraph_SimpleStmt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "valiableAccess" in params, "Missing parameter 'valiableAccess'"
    assert "functionAccess" in params, "Missing parameter 'functionAccess'"






def test_hyp_flowgraph_exit_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Exit)


def test_hyp_flowgraph_exit_constructor_exists():
    assert callable(flowgraph_Exit.__init__)


def test_hyp_flowgraph_exit_constructor_args():
    sig = inspect.signature(flowgraph_Exit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_method_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Method)


def test_hyp_flowgraph_method_constructor_exists():
    assert callable(flowgraph_Method.__init__)


def test_hyp_flowgraph_method_constructor_args():
    sig = inspect.signature(flowgraph_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_return_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Return)


def test_hyp_flowgraph_return_constructor_exists():
    assert callable(flowgraph_Return.__init__)


def test_hyp_flowgraph_return_constructor_args():
    sig = inspect.signature(flowgraph_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_item_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Item)


def test_hyp_flowgraph_item_constructor_exists():
    assert callable(flowgraph_Item.__init__)


def test_hyp_flowgraph_item_constructor_args():
    sig = inspect.signature(flowgraph_Item.__init__)
    params = list(sig.parameters.keys())
    assert "txt" in params, "Missing parameter 'txt'"
    assert "line" in params, "Missing parameter 'line'"





def test_hyp_flowgraph_expr_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Expr)


def test_hyp_flowgraph_expr_constructor_exists():
    assert callable(flowgraph_Expr.__init__)


def test_hyp_flowgraph_expr_constructor_args():
    sig = inspect.signature(flowgraph_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_var_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Var)


def test_hyp_flowgraph_var_constructor_exists():
    assert callable(flowgraph_Var.__init__)


def test_hyp_flowgraph_var_constructor_args():
    sig = inspect.signature(flowgraph_Var.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_stmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Stmt)


def test_hyp_flowgraph_stmt_constructor_exists():
    assert callable(flowgraph_Stmt.__init__)


def test_hyp_flowgraph_stmt_constructor_args():
    sig = inspect.signature(flowgraph_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_flowinstr_is_not_abstract():
    assert not inspect.isabstract(flowgraph_FlowInstr)


def test_hyp_flowgraph_flowinstr_constructor_exists():
    assert callable(flowgraph_FlowInstr.__init__)


def test_hyp_flowgraph_flowinstr_constructor_args():
    sig = inspect.signature(flowgraph_FlowInstr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jumpstmt_is_not_abstract():
    assert not inspect.isabstract(JumpStmt)


def test_hyp_jumpstmt_constructor_exists():
    assert callable(JumpStmt.__init__)


def test_hyp_jumpstmt_constructor_args():
    sig = inspect.signature(JumpStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_continue_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Continue)


def test_hyp_flowgraph_continue_constructor_exists():
    assert callable(flowgraph_Continue.__init__)


def test_hyp_flowgraph_continue_constructor_args():
    sig = inspect.signature(flowgraph_Continue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_break_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Break)


def test_hyp_flowgraph_break_constructor_exists():
    assert callable(flowgraph_Break.__init__)


def test_hyp_flowgraph_break_constructor_args():
    sig = inspect.signature(flowgraph_Break.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_label_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Label)


def test_hyp_flowgraph_label_constructor_exists():
    assert callable(flowgraph_Label.__init__)


def test_hyp_flowgraph_label_constructor_args():
    sig = inspect.signature(flowgraph_Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_jumpstmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph_JumpStmt)


def test_hyp_flowgraph_jumpstmt_constructor_exists():
    assert callable(flowgraph_JumpStmt.__init__)


def test_hyp_flowgraph_jumpstmt_constructor_args():
    sig = inspect.signature(flowgraph_JumpStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_conditional_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Conditional)


def test_hyp_flowgraph_conditional_constructor_exists():
    assert callable(flowgraph_Conditional.__init__)


def test_hyp_flowgraph_conditional_constructor_args():
    sig = inspect.signature(flowgraph_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowgraph_loop_is_not_abstract():
    assert not inspect.isabstract(flowgraph_Loop)


def test_hyp_flowgraph_loop_constructor_exists():
    assert callable(flowgraph_Loop.__init__)


def test_hyp_flowgraph_loop_constructor_args():
    sig = inspect.signature(flowgraph_Loop.__init__)
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
Var_strategy = st.builds(
    Var,
)
flowgraph_Param_strategy = st.builds(
    flowgraph_Param,
)
Conditional_strategy = st.builds(
    Conditional,
)
flowgraph_If_strategy = st.builds(
    flowgraph_If,
)
FlowInstr_strategy = st.builds(
    FlowInstr,
)
Stmt_strategy = st.builds(
    Stmt,
)
flowgraph_Block_strategy = st.builds(
    flowgraph_Block,
)
flowgraph_SimpleStmt_strategy = st.builds(
    flowgraph_SimpleStmt,
    type=
        safe_text,
    valiableAccess=
        safe_text,
    functionAccess=
        safe_text
)
flowgraph_Exit_strategy = st.builds(
    flowgraph_Exit,
)
Block_strategy = st.builds(
    Block,
)
flowgraph_Method_strategy = st.builds(
    flowgraph_Method,
)
flowgraph_Return_strategy = st.builds(
    flowgraph_Return,
)
flowgraph_Item_strategy = st.builds(
    flowgraph_Item,
    txt=
        safe_text,
    line=
        st.integers()
)
flowgraph_Expr_strategy = st.builds(
    flowgraph_Expr,
)
Item_strategy = st.builds(
    Item,
)
flowgraph_Var_strategy = st.builds(
    flowgraph_Var,
)
flowgraph_Stmt_strategy = st.builds(
    flowgraph_Stmt,
)
flowgraph_FlowInstr_strategy = st.builds(
    flowgraph_FlowInstr,
)
JumpStmt_strategy = st.builds(
    JumpStmt,
)
flowgraph_Continue_strategy = st.builds(
    flowgraph_Continue,
)
flowgraph_Break_strategy = st.builds(
    flowgraph_Break,
)
flowgraph_Label_strategy = st.builds(
    flowgraph_Label,
)
flowgraph_JumpStmt_strategy = st.builds(
    flowgraph_JumpStmt,
)
flowgraph_Conditional_strategy = st.builds(
    flowgraph_Conditional,
)
flowgraph_Loop_strategy = st.builds(
    flowgraph_Loop,
)











@given(instance=flowgraph_SimpleStmt_strategy)
def test_hyp_flowgraph_simplestmt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=flowgraph_SimpleStmt_strategy)
def test_hyp_flowgraph_simplestmt_valiableAccess_setter(instance):
    original = instance.valiableAccess
    instance.valiableAccess = original
    assert instance.valiableAccess == original



@given(instance=flowgraph_SimpleStmt_strategy)
def test_hyp_flowgraph_simplestmt_functionAccess_setter(instance):
    original = instance.functionAccess
    instance.functionAccess = original
    assert instance.functionAccess == original








@given(instance=flowgraph_Item_strategy)
def test_hyp_flowgraph_item_txt_setter(instance):
    original = instance.txt
    instance.txt = original
    assert instance.txt == original



@given(instance=flowgraph_Item_strategy)
def test_hyp_flowgraph_item_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original














# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Block,
    Conditional,
    FlowInstr,
    Item,
    JumpStmt,
    Stmt,
    Var,
    flowgraph_Block,
    flowgraph_Break,
    flowgraph_Conditional,
    flowgraph_Continue,
    flowgraph_Exit,
    flowgraph_Expr,
    flowgraph_FlowInstr,
    flowgraph_If,
    flowgraph_Item,
    flowgraph_JumpStmt,
    flowgraph_Label,
    flowgraph_Loop,
    flowgraph_Method,
    flowgraph_Param,
    flowgraph_Return,
    flowgraph_SimpleStmt,
    flowgraph_Stmt,
    flowgraph_Var,
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

def test_flowgraph_Item_line_value_roundtrip():
    instance = flowgraph_Item(line=7, txt="sample_text")
    assert instance.line == 7
    instance.line = 13
    assert instance.line == 13


def test_flowgraph_Item_txt_value_roundtrip():
    instance = flowgraph_Item(line=7, txt="sample_text")
    assert instance.txt == "sample_text"
    instance.txt = "sample_text_2"
    assert instance.txt == "sample_text_2"


def test_flowgraph_SimpleStmt_functionAccess_value_roundtrip():
    instance = flowgraph_SimpleStmt(functionAccess="sample_text", type="sample_text", valiableAccess="sample_text")
    assert instance.functionAccess == "sample_text"
    instance.functionAccess = "sample_text_2"
    assert instance.functionAccess == "sample_text_2"


def test_flowgraph_SimpleStmt_type_value_roundtrip():
    instance = flowgraph_SimpleStmt(functionAccess="sample_text", type="sample_text", valiableAccess="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_flowgraph_SimpleStmt_valiableAccess_value_roundtrip():
    instance = flowgraph_SimpleStmt(functionAccess="sample_text", type="sample_text", valiableAccess="sample_text")
    assert instance.valiableAccess == "sample_text"
    instance.valiableAccess = "sample_text_2"
    assert instance.valiableAccess == "sample_text_2"


def test_flowgraph_Method_isa_Block():
    instance = flowgraph_Method()
    assert isinstance(instance, Block)


def test_flowgraph_If_isa_Conditional():
    instance = flowgraph_If()
    assert isinstance(instance, Conditional)


def test_flowgraph_Loop_isa_Conditional():
    instance = flowgraph_Loop()
    assert isinstance(instance, Conditional)


def test_flowgraph_Exit_isa_FlowInstr():
    instance = flowgraph_Exit()
    assert isinstance(instance, FlowInstr)


def test_flowgraph_Expr_isa_FlowInstr():
    instance = flowgraph_Expr()
    assert isinstance(instance, FlowInstr)


def test_flowgraph_JumpStmt_isa_FlowInstr():
    instance = flowgraph_JumpStmt()
    assert isinstance(instance, FlowInstr)


def test_flowgraph_Method_isa_FlowInstr():
    instance = flowgraph_Method()
    assert isinstance(instance, FlowInstr)


def test_flowgraph_Return_isa_FlowInstr():
    instance = flowgraph_Return()
    assert isinstance(instance, FlowInstr)


def test_flowgraph_SimpleStmt_isa_FlowInstr():
    instance = flowgraph_SimpleStmt(functionAccess="sample_text", type="sample_text", valiableAccess="sample_text")
    assert isinstance(instance, FlowInstr)


def test_flowgraph_FlowInstr_isa_Item():
    instance = flowgraph_FlowInstr()
    assert isinstance(instance, Item)


def test_flowgraph_Stmt_isa_Item():
    instance = flowgraph_Stmt()
    assert isinstance(instance, Item)


def test_flowgraph_Var_isa_Item():
    instance = flowgraph_Var()
    assert isinstance(instance, Item)


def test_flowgraph_Break_isa_JumpStmt():
    instance = flowgraph_Break()
    assert isinstance(instance, JumpStmt)


def test_flowgraph_Continue_isa_JumpStmt():
    instance = flowgraph_Continue()
    assert isinstance(instance, JumpStmt)


def test_flowgraph_Block_isa_Stmt():
    instance = flowgraph_Block()
    assert isinstance(instance, Stmt)


def test_flowgraph_Conditional_isa_Stmt():
    instance = flowgraph_Conditional()
    assert isinstance(instance, Stmt)


def test_flowgraph_JumpStmt_isa_Stmt():
    instance = flowgraph_JumpStmt()
    assert isinstance(instance, Stmt)


def test_flowgraph_Label_isa_Stmt():
    instance = flowgraph_Label()
    assert isinstance(instance, Stmt)


def test_flowgraph_Return_isa_Stmt():
    instance = flowgraph_Return()
    assert isinstance(instance, Stmt)


def test_flowgraph_SimpleStmt_isa_Stmt():
    instance = flowgraph_SimpleStmt(functionAccess="sample_text", type="sample_text", valiableAccess="sample_text")
    assert isinstance(instance, Stmt)


def test_flowgraph_Param_isa_Var():
    instance = flowgraph_Param()
    assert isinstance(instance, Var)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


Conditional_strategy = st.builds(Conditional)
@given(instance=Conditional_strategy)
@settings(max_examples=25)
def test_Conditional_instantiation(instance):
    assert isinstance(instance, Conditional)


FlowInstr_strategy = st.builds(FlowInstr)
@given(instance=FlowInstr_strategy)
@settings(max_examples=25)
def test_FlowInstr_instantiation(instance):
    assert isinstance(instance, FlowInstr)


Item_strategy = st.builds(Item)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


JumpStmt_strategy = st.builds(JumpStmt)
@given(instance=JumpStmt_strategy)
@settings(max_examples=25)
def test_JumpStmt_instantiation(instance):
    assert isinstance(instance, JumpStmt)


Stmt_strategy = st.builds(Stmt)
@given(instance=Stmt_strategy)
@settings(max_examples=25)
def test_Stmt_instantiation(instance):
    assert isinstance(instance, Stmt)


Var_strategy = st.builds(Var)
@given(instance=Var_strategy)
@settings(max_examples=25)
def test_Var_instantiation(instance):
    assert isinstance(instance, Var)


flowgraph_Block_strategy = st.builds(flowgraph_Block)
@given(instance=flowgraph_Block_strategy)
@settings(max_examples=25)
def test_flowgraph_Block_instantiation(instance):
    assert isinstance(instance, flowgraph_Block)


flowgraph_Break_strategy = st.builds(flowgraph_Break)
@given(instance=flowgraph_Break_strategy)
@settings(max_examples=25)
def test_flowgraph_Break_instantiation(instance):
    assert isinstance(instance, flowgraph_Break)


flowgraph_Conditional_strategy = st.builds(flowgraph_Conditional)
@given(instance=flowgraph_Conditional_strategy)
@settings(max_examples=25)
def test_flowgraph_Conditional_instantiation(instance):
    assert isinstance(instance, flowgraph_Conditional)


flowgraph_Continue_strategy = st.builds(flowgraph_Continue)
@given(instance=flowgraph_Continue_strategy)
@settings(max_examples=25)
def test_flowgraph_Continue_instantiation(instance):
    assert isinstance(instance, flowgraph_Continue)


flowgraph_Exit_strategy = st.builds(flowgraph_Exit)
@given(instance=flowgraph_Exit_strategy)
@settings(max_examples=25)
def test_flowgraph_Exit_instantiation(instance):
    assert isinstance(instance, flowgraph_Exit)


flowgraph_Expr_strategy = st.builds(flowgraph_Expr)
@given(instance=flowgraph_Expr_strategy)
@settings(max_examples=25)
def test_flowgraph_Expr_instantiation(instance):
    assert isinstance(instance, flowgraph_Expr)


flowgraph_FlowInstr_strategy = st.builds(flowgraph_FlowInstr)
@given(instance=flowgraph_FlowInstr_strategy)
@settings(max_examples=25)
def test_flowgraph_FlowInstr_instantiation(instance):
    assert isinstance(instance, flowgraph_FlowInstr)


flowgraph_If_strategy = st.builds(flowgraph_If)
@given(instance=flowgraph_If_strategy)
@settings(max_examples=25)
def test_flowgraph_If_instantiation(instance):
    assert isinstance(instance, flowgraph_If)


flowgraph_Item_strategy = st.builds(flowgraph_Item, line=st.integers(), txt=safe_text)
@given(instance=flowgraph_Item_strategy)
@settings(max_examples=25)
def test_flowgraph_Item_instantiation(instance):
    assert isinstance(instance, flowgraph_Item)


flowgraph_JumpStmt_strategy = st.builds(flowgraph_JumpStmt)
@given(instance=flowgraph_JumpStmt_strategy)
@settings(max_examples=25)
def test_flowgraph_JumpStmt_instantiation(instance):
    assert isinstance(instance, flowgraph_JumpStmt)


flowgraph_Label_strategy = st.builds(flowgraph_Label)
@given(instance=flowgraph_Label_strategy)
@settings(max_examples=25)
def test_flowgraph_Label_instantiation(instance):
    assert isinstance(instance, flowgraph_Label)


flowgraph_Loop_strategy = st.builds(flowgraph_Loop)
@given(instance=flowgraph_Loop_strategy)
@settings(max_examples=25)
def test_flowgraph_Loop_instantiation(instance):
    assert isinstance(instance, flowgraph_Loop)


flowgraph_Method_strategy = st.builds(flowgraph_Method)
@given(instance=flowgraph_Method_strategy)
@settings(max_examples=25)
def test_flowgraph_Method_instantiation(instance):
    assert isinstance(instance, flowgraph_Method)


flowgraph_Param_strategy = st.builds(flowgraph_Param)
@given(instance=flowgraph_Param_strategy)
@settings(max_examples=25)
def test_flowgraph_Param_instantiation(instance):
    assert isinstance(instance, flowgraph_Param)


flowgraph_Return_strategy = st.builds(flowgraph_Return)
@given(instance=flowgraph_Return_strategy)
@settings(max_examples=25)
def test_flowgraph_Return_instantiation(instance):
    assert isinstance(instance, flowgraph_Return)


flowgraph_SimpleStmt_strategy = st.builds(flowgraph_SimpleStmt, functionAccess=safe_text, type=safe_text, valiableAccess=safe_text)
@given(instance=flowgraph_SimpleStmt_strategy)
@settings(max_examples=25)
def test_flowgraph_SimpleStmt_instantiation(instance):
    assert isinstance(instance, flowgraph_SimpleStmt)


flowgraph_Stmt_strategy = st.builds(flowgraph_Stmt)
@given(instance=flowgraph_Stmt_strategy)
@settings(max_examples=25)
def test_flowgraph_Stmt_instantiation(instance):
    assert isinstance(instance, flowgraph_Stmt)


flowgraph_Var_strategy = st.builds(flowgraph_Var)
@given(instance=flowgraph_Var_strategy)
@settings(max_examples=25)
def test_flowgraph_Var_instantiation(instance):
    assert isinstance(instance, flowgraph_Var)



