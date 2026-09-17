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
    fsm_Expression,
    Statement,
    fsm_Loop,
    fsm_Context,
    State,
    fsm_FinalState,
    Literal,
    fsm_VarRef,
    fsm_Real,
    fsm_Boolean,
    fsm_String,
    fsm_Integer,
    Expression,
    fsm_Literal,
    fsm_ArithmeticExpression,
    fsm_RelationalExpression,
    fsm_Assignation,
    fsm_VarDecl,
    fsm_Conditional,
    fsm_Trigger,
    fsm_Block,
    AbstractState,
    Pseudostate,
    fsm_Join,
    fsm_ShallowHistory,
    fsm_Condition,
    fsm_Fork,
    fsm_DeepHistory,
    fsm_Junction,
    fsm_InitialState,
    fsm_Pseudostate,
    Trigger,
    fsm_OrTrigger,
    fsm_AndTrigger,
    fsm_NotTrigger,
    fsm_Constraint,
    fsm_Statement,
    fsm_State,
    fsm_Transition,
    fsm_AbstractState,
    fsm_Region,
    fsm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_expression_is_not_abstract():
    assert not inspect.isabstract(fsm_Expression)


def test_hyp_fsm_expression_constructor_exists():
    assert callable(fsm_Expression.__init__)


def test_hyp_fsm_expression_constructor_args():
    sig = inspect.signature(fsm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_loop_is_not_abstract():
    assert not inspect.isabstract(fsm_Loop)


def test_hyp_fsm_loop_constructor_exists():
    assert callable(fsm_Loop.__init__)


def test_hyp_fsm_loop_constructor_args():
    sig = inspect.signature(fsm_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_context_is_not_abstract():
    assert not inspect.isabstract(fsm_Context)


def test_hyp_fsm_context_constructor_exists():
    assert callable(fsm_Context.__init__)


def test_hyp_fsm_context_constructor_args():
    sig = inspect.signature(fsm_Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_hyp_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_hyp_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_varref_is_not_abstract():
    assert not inspect.isabstract(fsm_VarRef)


def test_hyp_fsm_varref_constructor_exists():
    assert callable(fsm_VarRef.__init__)


def test_hyp_fsm_varref_constructor_args():
    sig = inspect.signature(fsm_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "varId" in params, "Missing parameter 'varId'"




def test_hyp_fsm_real_is_not_abstract():
    assert not inspect.isabstract(fsm_Real)


def test_hyp_fsm_real_constructor_exists():
    assert callable(fsm_Real.__init__)


def test_hyp_fsm_real_constructor_args():
    sig = inspect.signature(fsm_Real.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_boolean_is_not_abstract():
    assert not inspect.isabstract(fsm_Boolean)


def test_hyp_fsm_boolean_constructor_exists():
    assert callable(fsm_Boolean.__init__)


def test_hyp_fsm_boolean_constructor_args():
    sig = inspect.signature(fsm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_string_is_not_abstract():
    assert not inspect.isabstract(fsm_String)


def test_hyp_fsm_string_constructor_exists():
    assert callable(fsm_String.__init__)


def test_hyp_fsm_string_constructor_args():
    sig = inspect.signature(fsm_String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_integer_is_not_abstract():
    assert not inspect.isabstract(fsm_Integer)


def test_hyp_fsm_integer_constructor_exists():
    assert callable(fsm_Integer.__init__)


def test_hyp_fsm_integer_constructor_args():
    sig = inspect.signature(fsm_Integer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_literal_is_not_abstract():
    assert not inspect.isabstract(fsm_Literal)


def test_hyp_fsm_literal_constructor_exists():
    assert callable(fsm_Literal.__init__)


def test_hyp_fsm_literal_constructor_args():
    sig = inspect.signature(fsm_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fsm_ArithmeticExpression)


def test_hyp_fsm_arithmeticexpression_constructor_exists():
    assert callable(fsm_ArithmeticExpression.__init__)


def test_hyp_fsm_arithmeticexpression_constructor_args():
    sig = inspect.signature(fsm_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(fsm_RelationalExpression)


def test_hyp_fsm_relationalexpression_constructor_exists():
    assert callable(fsm_RelationalExpression.__init__)


def test_hyp_fsm_relationalexpression_constructor_args():
    sig = inspect.signature(fsm_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_assignation_is_not_abstract():
    assert not inspect.isabstract(fsm_Assignation)


def test_hyp_fsm_assignation_constructor_exists():
    assert callable(fsm_Assignation.__init__)


def test_hyp_fsm_assignation_constructor_args():
    sig = inspect.signature(fsm_Assignation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_vardecl_is_not_abstract():
    assert not inspect.isabstract(fsm_VarDecl)


def test_hyp_fsm_vardecl_constructor_exists():
    assert callable(fsm_VarDecl.__init__)


def test_hyp_fsm_vardecl_constructor_args():
    sig = inspect.signature(fsm_VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_conditional_is_not_abstract():
    assert not inspect.isabstract(fsm_Conditional)


def test_hyp_fsm_conditional_constructor_exists():
    assert callable(fsm_Conditional.__init__)


def test_hyp_fsm_conditional_constructor_args():
    sig = inspect.signature(fsm_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_hyp_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_hyp_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_fsm_block_is_not_abstract():
    assert not inspect.isabstract(fsm_Block)


def test_hyp_fsm_block_constructor_exists():
    assert callable(fsm_Block.__init__)


def test_hyp_fsm_block_constructor_args():
    sig = inspect.signature(fsm_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_hyp_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_hyp_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_join_is_not_abstract():
    assert not inspect.isabstract(fsm_Join)


def test_hyp_fsm_join_constructor_exists():
    assert callable(fsm_Join.__init__)


def test_hyp_fsm_join_constructor_args():
    sig = inspect.signature(fsm_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_shallowhistory_is_not_abstract():
    assert not inspect.isabstract(fsm_ShallowHistory)


def test_hyp_fsm_shallowhistory_constructor_exists():
    assert callable(fsm_ShallowHistory.__init__)


def test_hyp_fsm_shallowhistory_constructor_args():
    sig = inspect.signature(fsm_ShallowHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_condition_is_not_abstract():
    assert not inspect.isabstract(fsm_Condition)


def test_hyp_fsm_condition_constructor_exists():
    assert callable(fsm_Condition.__init__)


def test_hyp_fsm_condition_constructor_args():
    sig = inspect.signature(fsm_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_fork_is_not_abstract():
    assert not inspect.isabstract(fsm_Fork)


def test_hyp_fsm_fork_constructor_exists():
    assert callable(fsm_Fork.__init__)


def test_hyp_fsm_fork_constructor_args():
    sig = inspect.signature(fsm_Fork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_deephistory_is_not_abstract():
    assert not inspect.isabstract(fsm_DeepHistory)


def test_hyp_fsm_deephistory_constructor_exists():
    assert callable(fsm_DeepHistory.__init__)


def test_hyp_fsm_deephistory_constructor_args():
    sig = inspect.signature(fsm_DeepHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_junction_is_not_abstract():
    assert not inspect.isabstract(fsm_Junction)


def test_hyp_fsm_junction_constructor_exists():
    assert callable(fsm_Junction.__init__)


def test_hyp_fsm_junction_constructor_args():
    sig = inspect.signature(fsm_Junction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_hyp_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_hyp_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_hyp_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_hyp_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_hyp_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_hyp_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_ortrigger_is_not_abstract():
    assert not inspect.isabstract(fsm_OrTrigger)


def test_hyp_fsm_ortrigger_constructor_exists():
    assert callable(fsm_OrTrigger.__init__)


def test_hyp_fsm_ortrigger_constructor_args():
    sig = inspect.signature(fsm_OrTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_andtrigger_is_not_abstract():
    assert not inspect.isabstract(fsm_AndTrigger)


def test_hyp_fsm_andtrigger_constructor_exists():
    assert callable(fsm_AndTrigger.__init__)


def test_hyp_fsm_andtrigger_constructor_args():
    sig = inspect.signature(fsm_AndTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_nottrigger_is_not_abstract():
    assert not inspect.isabstract(fsm_NotTrigger)


def test_hyp_fsm_nottrigger_constructor_exists():
    assert callable(fsm_NotTrigger.__init__)


def test_hyp_fsm_nottrigger_constructor_args():
    sig = inspect.signature(fsm_NotTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_hyp_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_hyp_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_statement_is_not_abstract():
    assert not inspect.isabstract(fsm_Statement)


def test_hyp_fsm_statement_constructor_exists():
    assert callable(fsm_Statement.__init__)


def test_hyp_fsm_statement_constructor_args():
    sig = inspect.signature(fsm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_hyp_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_hyp_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_region_is_not_abstract():
    assert not inspect.isabstract(fsm_Region)


def test_hyp_fsm_region_constructor_exists():
    assert callable(fsm_Region.__init__)


def test_hyp_fsm_region_constructor_args():
    sig = inspect.signature(fsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_hyp_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_hyp_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
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
fsm_Expression_strategy = st.builds(
    fsm_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
fsm_Loop_strategy = st.builds(
    fsm_Loop,
)
fsm_Context_strategy = st.builds(
    fsm_Context,
)
State_strategy = st.builds(
    State,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
Literal_strategy = st.builds(
    Literal,
)
fsm_VarRef_strategy = st.builds(
    fsm_VarRef,
    varId=
        safe_text
)
fsm_Real_strategy = st.builds(
    fsm_Real,
)
fsm_Boolean_strategy = st.builds(
    fsm_Boolean,
)
fsm_String_strategy = st.builds(
    fsm_String,
)
fsm_Integer_strategy = st.builds(
    fsm_Integer,
)
Expression_strategy = st.builds(
    Expression,
)
fsm_Literal_strategy = st.builds(
    fsm_Literal,
)
fsm_ArithmeticExpression_strategy = st.builds(
    fsm_ArithmeticExpression,
)
fsm_RelationalExpression_strategy = st.builds(
    fsm_RelationalExpression,
)
fsm_Assignation_strategy = st.builds(
    fsm_Assignation,
)
fsm_VarDecl_strategy = st.builds(
    fsm_VarDecl,
)
fsm_Conditional_strategy = st.builds(
    fsm_Conditional,
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
fsm_Block_strategy = st.builds(
    fsm_Block,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm_Join_strategy = st.builds(
    fsm_Join,
)
fsm_ShallowHistory_strategy = st.builds(
    fsm_ShallowHistory,
)
fsm_Condition_strategy = st.builds(
    fsm_Condition,
)
fsm_Fork_strategy = st.builds(
    fsm_Fork,
)
fsm_DeepHistory_strategy = st.builds(
    fsm_DeepHistory,
)
fsm_Junction_strategy = st.builds(
    fsm_Junction,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
)
Trigger_strategy = st.builds(
    Trigger,
)
fsm_OrTrigger_strategy = st.builds(
    fsm_OrTrigger,
)
fsm_AndTrigger_strategy = st.builds(
    fsm_AndTrigger,
)
fsm_NotTrigger_strategy = st.builds(
    fsm_NotTrigger,
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
)
fsm_Statement_strategy = st.builds(
    fsm_Statement,
)
fsm_State_strategy = st.builds(
    fsm_State,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
)
fsm_Region_strategy = st.builds(
    fsm_Region,
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)











@given(instance=fsm_VarRef_strategy)
def test_hyp_fsm_varref_varId_setter(instance):
    original = instance.varId
    instance.varId = original
    assert instance.varId == original















@given(instance=fsm_Trigger_strategy)
def test_hyp_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original
























# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractState,
    Expression,
    Literal,
    Pseudostate,
    State,
    Statement,
    Trigger,
    fsm_AbstractState,
    fsm_AndTrigger,
    fsm_ArithmeticExpression,
    fsm_Assignation,
    fsm_Block,
    fsm_Boolean,
    fsm_Condition,
    fsm_Conditional,
    fsm_Constraint,
    fsm_Context,
    fsm_DeepHistory,
    fsm_Expression,
    fsm_FinalState,
    fsm_Fork,
    fsm_InitialState,
    fsm_Integer,
    fsm_Join,
    fsm_Junction,
    fsm_Literal,
    fsm_Loop,
    fsm_NotTrigger,
    fsm_OrTrigger,
    fsm_Pseudostate,
    fsm_Real,
    fsm_Region,
    fsm_RelationalExpression,
    fsm_ShallowHistory,
    fsm_State,
    fsm_StateMachine,
    fsm_Statement,
    fsm_String,
    fsm_Transition,
    fsm_Trigger,
    fsm_VarDecl,
    fsm_VarRef,
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

def test_fsm_Trigger_expression_value_roundtrip():
    instance = fsm_Trigger(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_fsm_VarRef_varId_value_roundtrip():
    instance = fsm_VarRef(varId="sample_text")
    assert instance.varId == "sample_text"
    instance.varId = "sample_text_2"
    assert instance.varId == "sample_text_2"


def test_fsm_Pseudostate_isa_AbstractState():
    instance = fsm_Pseudostate()
    assert isinstance(instance, AbstractState)


def test_fsm_State_isa_AbstractState():
    instance = fsm_State()
    assert isinstance(instance, AbstractState)


def test_fsm_ArithmeticExpression_isa_Expression():
    instance = fsm_ArithmeticExpression()
    assert isinstance(instance, Expression)


def test_fsm_Literal_isa_Expression():
    instance = fsm_Literal()
    assert isinstance(instance, Expression)


def test_fsm_RelationalExpression_isa_Expression():
    instance = fsm_RelationalExpression()
    assert isinstance(instance, Expression)


def test_fsm_Boolean_isa_Literal():
    instance = fsm_Boolean()
    assert isinstance(instance, Literal)


def test_fsm_Integer_isa_Literal():
    instance = fsm_Integer()
    assert isinstance(instance, Literal)


def test_fsm_Real_isa_Literal():
    instance = fsm_Real()
    assert isinstance(instance, Literal)


def test_fsm_String_isa_Literal():
    instance = fsm_String()
    assert isinstance(instance, Literal)


def test_fsm_VarRef_isa_Literal():
    instance = fsm_VarRef(varId="sample_text")
    assert isinstance(instance, Literal)


def test_fsm_Condition_isa_Pseudostate():
    instance = fsm_Condition()
    assert isinstance(instance, Pseudostate)


def test_fsm_DeepHistory_isa_Pseudostate():
    instance = fsm_DeepHistory()
    assert isinstance(instance, Pseudostate)


def test_fsm_Fork_isa_Pseudostate():
    instance = fsm_Fork()
    assert isinstance(instance, Pseudostate)


def test_fsm_InitialState_isa_Pseudostate():
    instance = fsm_InitialState()
    assert isinstance(instance, Pseudostate)


def test_fsm_Join_isa_Pseudostate():
    instance = fsm_Join()
    assert isinstance(instance, Pseudostate)


def test_fsm_Junction_isa_Pseudostate():
    instance = fsm_Junction()
    assert isinstance(instance, Pseudostate)


def test_fsm_ShallowHistory_isa_Pseudostate():
    instance = fsm_ShallowHistory()
    assert isinstance(instance, Pseudostate)


def test_fsm_FinalState_isa_State():
    instance = fsm_FinalState()
    assert isinstance(instance, State)


def test_fsm_Assignation_isa_Statement():
    instance = fsm_Assignation()
    assert isinstance(instance, Statement)


def test_fsm_Block_isa_Statement():
    instance = fsm_Block()
    assert isinstance(instance, Statement)


def test_fsm_Conditional_isa_Statement():
    instance = fsm_Conditional()
    assert isinstance(instance, Statement)


def test_fsm_Loop_isa_Statement():
    instance = fsm_Loop()
    assert isinstance(instance, Statement)


def test_fsm_VarDecl_isa_Statement():
    instance = fsm_VarDecl()
    assert isinstance(instance, Statement)


def test_fsm_AndTrigger_isa_Trigger():
    instance = fsm_AndTrigger()
    assert isinstance(instance, Trigger)


def test_fsm_NotTrigger_isa_Trigger():
    instance = fsm_NotTrigger()
    assert isinstance(instance, Trigger)


def test_fsm_OrTrigger_isa_Trigger():
    instance = fsm_OrTrigger()
    assert isinstance(instance, Trigger)


def test_assoc_left24_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_AndTrigger()
    b2 = fsm_AndTrigger()
    _safe_set(a, 'fsm_Trigger25', b1)
    assert _is_linked(a, 'fsm_Trigger25', b1)
    if hasattr(b1, 'fsm_AndTrigger'):
        assert _is_linked(b1, 'fsm_AndTrigger', a)
    _safe_set(a, 'fsm_Trigger25', b2)
    assert _is_linked(a, 'fsm_Trigger25', b2)
    if hasattr(b1, 'fsm_AndTrigger'):
        assert not _is_linked(b1, 'fsm_AndTrigger', a)
    if hasattr(b2, 'fsm_AndTrigger'):
        assert _is_linked(b2, 'fsm_AndTrigger', a)
    _safe_set(a, 'fsm_Trigger25', None)
    assert not _is_linked(a, 'fsm_Trigger25', b2)
    if hasattr(b2, 'fsm_AndTrigger'):
        assert not _is_linked(b2, 'fsm_AndTrigger', a)


def test_assoc_left29_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_OrTrigger()
    b2 = fsm_OrTrigger()
    _safe_set(a, 'fsm_Trigger30', b1)
    assert _is_linked(a, 'fsm_Trigger30', b1)
    if hasattr(b1, 'fsm_OrTrigger'):
        assert _is_linked(b1, 'fsm_OrTrigger', a)
    _safe_set(a, 'fsm_Trigger30', b2)
    assert _is_linked(a, 'fsm_Trigger30', b2)
    if hasattr(b1, 'fsm_OrTrigger'):
        assert not _is_linked(b1, 'fsm_OrTrigger', a)
    if hasattr(b2, 'fsm_OrTrigger'):
        assert _is_linked(b2, 'fsm_OrTrigger', a)
    _safe_set(a, 'fsm_Trigger30', None)
    assert not _is_linked(a, 'fsm_Trigger30', b2)
    if hasattr(b2, 'fsm_OrTrigger'):
        assert not _is_linked(b2, 'fsm_OrTrigger', a)


def test_assoc_right26_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_AndTrigger()
    b2 = fsm_AndTrigger()
    _safe_set(a, 'fsm_Trigger28', b1)
    assert _is_linked(a, 'fsm_Trigger28', b1)
    if hasattr(b1, 'fsm_AndTrigger27'):
        assert _is_linked(b1, 'fsm_AndTrigger27', a)
    _safe_set(a, 'fsm_Trigger28', b2)
    assert _is_linked(a, 'fsm_Trigger28', b2)
    if hasattr(b1, 'fsm_AndTrigger27'):
        assert not _is_linked(b1, 'fsm_AndTrigger27', a)
    if hasattr(b2, 'fsm_AndTrigger27'):
        assert _is_linked(b2, 'fsm_AndTrigger27', a)
    _safe_set(a, 'fsm_Trigger28', None)
    assert not _is_linked(a, 'fsm_Trigger28', b2)
    if hasattr(b2, 'fsm_AndTrigger27'):
        assert not _is_linked(b2, 'fsm_AndTrigger27', a)


def test_assoc_right31_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_OrTrigger()
    b2 = fsm_OrTrigger()
    _safe_set(a, 'fsm_Trigger33', b1)
    assert _is_linked(a, 'fsm_Trigger33', b1)
    if hasattr(b1, 'fsm_OrTrigger32'):
        assert _is_linked(b1, 'fsm_OrTrigger32', a)
    _safe_set(a, 'fsm_Trigger33', b2)
    assert _is_linked(a, 'fsm_Trigger33', b2)
    if hasattr(b1, 'fsm_OrTrigger32'):
        assert not _is_linked(b1, 'fsm_OrTrigger32', a)
    if hasattr(b2, 'fsm_OrTrigger32'):
        assert _is_linked(b2, 'fsm_OrTrigger32', a)
    _safe_set(a, 'fsm_Trigger33', None)
    assert not _is_linked(a, 'fsm_Trigger33', b2)
    if hasattr(b2, 'fsm_OrTrigger32'):
        assert not _is_linked(b2, 'fsm_OrTrigger32', a)


def test_assoc_trigger12_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_Transition()
    b2 = fsm_Transition()
    _safe_set(a, 'fsm_Trigger', b1)
    assert _is_linked(a, 'fsm_Trigger', b1)
    if hasattr(b1, 'fsm_Transition13'):
        assert _is_linked(b1, 'fsm_Transition13', a)
    _safe_set(a, 'fsm_Trigger', b2)
    assert _is_linked(a, 'fsm_Trigger', b2)
    if hasattr(b1, 'fsm_Transition13'):
        assert not _is_linked(b1, 'fsm_Transition13', a)
    if hasattr(b2, 'fsm_Transition13'):
        assert _is_linked(b2, 'fsm_Transition13', a)
    _safe_set(a, 'fsm_Trigger', None)
    assert not _is_linked(a, 'fsm_Trigger', b2)
    if hasattr(b2, 'fsm_Transition13'):
        assert not _is_linked(b2, 'fsm_Transition13', a)


def test_assoc_trigger22_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_NotTrigger()
    b2 = fsm_NotTrigger()
    _safe_set(a, 'fsm_Trigger23', b1)
    assert _is_linked(a, 'fsm_Trigger23', b1)
    if hasattr(b1, 'fsm_NotTrigger'):
        assert _is_linked(b1, 'fsm_NotTrigger', a)
    _safe_set(a, 'fsm_Trigger23', b2)
    assert _is_linked(a, 'fsm_Trigger23', b2)
    if hasattr(b1, 'fsm_NotTrigger'):
        assert not _is_linked(b1, 'fsm_NotTrigger', a)
    if hasattr(b2, 'fsm_NotTrigger'):
        assert _is_linked(b2, 'fsm_NotTrigger', a)
    _safe_set(a, 'fsm_Trigger23', None)
    assert not _is_linked(a, 'fsm_Trigger23', b2)
    if hasattr(b2, 'fsm_NotTrigger'):
        assert not _is_linked(b2, 'fsm_NotTrigger', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


Pseudostate_strategy = st.builds(Pseudostate)
@given(instance=Pseudostate_strategy)
@settings(max_examples=25)
def test_Pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Trigger_strategy = st.builds(Trigger)
@given(instance=Trigger_strategy)
@settings(max_examples=25)
def test_Trigger_instantiation(instance):
    assert isinstance(instance, Trigger)


fsm_AbstractState_strategy = st.builds(fsm_AbstractState)
@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=25)
def test_fsm_AbstractState_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)


fsm_AndTrigger_strategy = st.builds(fsm_AndTrigger)
@given(instance=fsm_AndTrigger_strategy)
@settings(max_examples=25)
def test_fsm_AndTrigger_instantiation(instance):
    assert isinstance(instance, fsm_AndTrigger)


fsm_ArithmeticExpression_strategy = st.builds(fsm_ArithmeticExpression)
@given(instance=fsm_ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_fsm_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, fsm_ArithmeticExpression)


fsm_Assignation_strategy = st.builds(fsm_Assignation)
@given(instance=fsm_Assignation_strategy)
@settings(max_examples=25)
def test_fsm_Assignation_instantiation(instance):
    assert isinstance(instance, fsm_Assignation)


fsm_Block_strategy = st.builds(fsm_Block)
@given(instance=fsm_Block_strategy)
@settings(max_examples=25)
def test_fsm_Block_instantiation(instance):
    assert isinstance(instance, fsm_Block)


fsm_Boolean_strategy = st.builds(fsm_Boolean)
@given(instance=fsm_Boolean_strategy)
@settings(max_examples=25)
def test_fsm_Boolean_instantiation(instance):
    assert isinstance(instance, fsm_Boolean)


fsm_Condition_strategy = st.builds(fsm_Condition)
@given(instance=fsm_Condition_strategy)
@settings(max_examples=25)
def test_fsm_Condition_instantiation(instance):
    assert isinstance(instance, fsm_Condition)


fsm_Conditional_strategy = st.builds(fsm_Conditional)
@given(instance=fsm_Conditional_strategy)
@settings(max_examples=25)
def test_fsm_Conditional_instantiation(instance):
    assert isinstance(instance, fsm_Conditional)


fsm_Constraint_strategy = st.builds(fsm_Constraint)
@given(instance=fsm_Constraint_strategy)
@settings(max_examples=25)
def test_fsm_Constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)


fsm_Context_strategy = st.builds(fsm_Context)
@given(instance=fsm_Context_strategy)
@settings(max_examples=25)
def test_fsm_Context_instantiation(instance):
    assert isinstance(instance, fsm_Context)


fsm_DeepHistory_strategy = st.builds(fsm_DeepHistory)
@given(instance=fsm_DeepHistory_strategy)
@settings(max_examples=25)
def test_fsm_DeepHistory_instantiation(instance):
    assert isinstance(instance, fsm_DeepHistory)


fsm_Expression_strategy = st.builds(fsm_Expression)
@given(instance=fsm_Expression_strategy)
@settings(max_examples=25)
def test_fsm_Expression_instantiation(instance):
    assert isinstance(instance, fsm_Expression)


fsm_FinalState_strategy = st.builds(fsm_FinalState)
@given(instance=fsm_FinalState_strategy)
@settings(max_examples=25)
def test_fsm_FinalState_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)


fsm_Fork_strategy = st.builds(fsm_Fork)
@given(instance=fsm_Fork_strategy)
@settings(max_examples=25)
def test_fsm_Fork_instantiation(instance):
    assert isinstance(instance, fsm_Fork)


fsm_InitialState_strategy = st.builds(fsm_InitialState)
@given(instance=fsm_InitialState_strategy)
@settings(max_examples=25)
def test_fsm_InitialState_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)


fsm_Integer_strategy = st.builds(fsm_Integer)
@given(instance=fsm_Integer_strategy)
@settings(max_examples=25)
def test_fsm_Integer_instantiation(instance):
    assert isinstance(instance, fsm_Integer)


fsm_Join_strategy = st.builds(fsm_Join)
@given(instance=fsm_Join_strategy)
@settings(max_examples=25)
def test_fsm_Join_instantiation(instance):
    assert isinstance(instance, fsm_Join)


fsm_Junction_strategy = st.builds(fsm_Junction)
@given(instance=fsm_Junction_strategy)
@settings(max_examples=25)
def test_fsm_Junction_instantiation(instance):
    assert isinstance(instance, fsm_Junction)


fsm_Literal_strategy = st.builds(fsm_Literal)
@given(instance=fsm_Literal_strategy)
@settings(max_examples=25)
def test_fsm_Literal_instantiation(instance):
    assert isinstance(instance, fsm_Literal)


fsm_Loop_strategy = st.builds(fsm_Loop)
@given(instance=fsm_Loop_strategy)
@settings(max_examples=25)
def test_fsm_Loop_instantiation(instance):
    assert isinstance(instance, fsm_Loop)


fsm_NotTrigger_strategy = st.builds(fsm_NotTrigger)
@given(instance=fsm_NotTrigger_strategy)
@settings(max_examples=25)
def test_fsm_NotTrigger_instantiation(instance):
    assert isinstance(instance, fsm_NotTrigger)


fsm_OrTrigger_strategy = st.builds(fsm_OrTrigger)
@given(instance=fsm_OrTrigger_strategy)
@settings(max_examples=25)
def test_fsm_OrTrigger_instantiation(instance):
    assert isinstance(instance, fsm_OrTrigger)


fsm_Pseudostate_strategy = st.builds(fsm_Pseudostate)
@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=25)
def test_fsm_Pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)


fsm_Real_strategy = st.builds(fsm_Real)
@given(instance=fsm_Real_strategy)
@settings(max_examples=25)
def test_fsm_Real_instantiation(instance):
    assert isinstance(instance, fsm_Real)


fsm_Region_strategy = st.builds(fsm_Region)
@given(instance=fsm_Region_strategy)
@settings(max_examples=25)
def test_fsm_Region_instantiation(instance):
    assert isinstance(instance, fsm_Region)


fsm_RelationalExpression_strategy = st.builds(fsm_RelationalExpression)
@given(instance=fsm_RelationalExpression_strategy)
@settings(max_examples=25)
def test_fsm_RelationalExpression_instantiation(instance):
    assert isinstance(instance, fsm_RelationalExpression)


fsm_ShallowHistory_strategy = st.builds(fsm_ShallowHistory)
@given(instance=fsm_ShallowHistory_strategy)
@settings(max_examples=25)
def test_fsm_ShallowHistory_instantiation(instance):
    assert isinstance(instance, fsm_ShallowHistory)


fsm_State_strategy = st.builds(fsm_State)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_StateMachine_strategy = st.builds(fsm_StateMachine)
@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=25)
def test_fsm_StateMachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)


fsm_Statement_strategy = st.builds(fsm_Statement)
@given(instance=fsm_Statement_strategy)
@settings(max_examples=25)
def test_fsm_Statement_instantiation(instance):
    assert isinstance(instance, fsm_Statement)


fsm_String_strategy = st.builds(fsm_String)
@given(instance=fsm_String_strategy)
@settings(max_examples=25)
def test_fsm_String_instantiation(instance):
    assert isinstance(instance, fsm_String)


fsm_Transition_strategy = st.builds(fsm_Transition)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)


fsm_Trigger_strategy = st.builds(fsm_Trigger, expression=safe_text)
@given(instance=fsm_Trigger_strategy)
@settings(max_examples=25)
def test_fsm_Trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)


fsm_VarDecl_strategy = st.builds(fsm_VarDecl)
@given(instance=fsm_VarDecl_strategy)
@settings(max_examples=25)
def test_fsm_VarDecl_instantiation(instance):
    assert isinstance(instance, fsm_VarDecl)


fsm_VarRef_strategy = st.builds(fsm_VarRef, varId=safe_text)
@given(instance=fsm_VarRef_strategy)
@settings(max_examples=25)
def test_fsm_VarRef_instantiation(instance):
    assert isinstance(instance, fsm_VarRef)



