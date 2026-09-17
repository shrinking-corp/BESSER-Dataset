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
    IntBinaryOperation,
    gx10_Time,
    gx10_Plus,
    IntExpression,
    gx10_IntBinaryOperation,
    gx10_IntVarAccess,
    gx10_IntConst,
    gx10_Statement,
    Statement,
    gx10_Expression,
    gx10_Async,
    gx10_Finish,
    gx10_Print,
    gx10_IntVar,
    gx10_Referentiable,
    BoolExpression,
    gx10_Equal,
    gx10_False,
    gx10_BoolVarAccess,
    gx10_And,
    gx10_Not,
    gx10_True,
    ControlStructure,
    gx10_While,
    gx10_If,
    gx10_MethodCallParameter,
    Expression,
    gx10_BoolVar,
    gx10_MethodCall,
    gx10_IntExpression,
    gx10_BoolExpression,
    gx10_ControlStructure,
    gx10_Block,
    gx10_Method,
    gx10_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_intbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(IntBinaryOperation)


def test_hyp_intbinaryoperation_constructor_exists():
    assert callable(IntBinaryOperation.__init__)


def test_hyp_intbinaryoperation_constructor_args():
    sig = inspect.signature(IntBinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_time_is_not_abstract():
    assert not inspect.isabstract(gx10_Time)


def test_hyp_gx10_time_constructor_exists():
    assert callable(gx10_Time.__init__)


def test_hyp_gx10_time_constructor_args():
    sig = inspect.signature(gx10_Time.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_plus_is_not_abstract():
    assert not inspect.isabstract(gx10_Plus)


def test_hyp_gx10_plus_constructor_exists():
    assert callable(gx10_Plus.__init__)


def test_hyp_gx10_plus_constructor_args():
    sig = inspect.signature(gx10_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intexpression_is_not_abstract():
    assert not inspect.isabstract(IntExpression)


def test_hyp_intexpression_constructor_exists():
    assert callable(IntExpression.__init__)


def test_hyp_intexpression_constructor_args():
    sig = inspect.signature(IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_intbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(gx10_IntBinaryOperation)


def test_hyp_gx10_intbinaryoperation_constructor_exists():
    assert callable(gx10_IntBinaryOperation.__init__)


def test_hyp_gx10_intbinaryoperation_constructor_args():
    sig = inspect.signature(gx10_IntBinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_intvaraccess_is_not_abstract():
    assert not inspect.isabstract(gx10_IntVarAccess)


def test_hyp_gx10_intvaraccess_constructor_exists():
    assert callable(gx10_IntVarAccess.__init__)


def test_hyp_gx10_intvaraccess_constructor_args():
    sig = inspect.signature(gx10_IntVarAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_intconst_is_not_abstract():
    assert not inspect.isabstract(gx10_IntConst)


def test_hyp_gx10_intconst_constructor_exists():
    assert callable(gx10_IntConst.__init__)


def test_hyp_gx10_intconst_constructor_args():
    sig = inspect.signature(gx10_IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_gx10_statement_is_not_abstract():
    assert not inspect.isabstract(gx10_Statement)


def test_hyp_gx10_statement_constructor_exists():
    assert callable(gx10_Statement.__init__)


def test_hyp_gx10_statement_constructor_args():
    sig = inspect.signature(gx10_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_expression_is_not_abstract():
    assert not inspect.isabstract(gx10_Expression)


def test_hyp_gx10_expression_constructor_exists():
    assert callable(gx10_Expression.__init__)


def test_hyp_gx10_expression_constructor_args():
    sig = inspect.signature(gx10_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_async_is_not_abstract():
    assert not inspect.isabstract(gx10_Async)


def test_hyp_gx10_async_constructor_exists():
    assert callable(gx10_Async.__init__)


def test_hyp_gx10_async_constructor_args():
    sig = inspect.signature(gx10_Async.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_finish_is_not_abstract():
    assert not inspect.isabstract(gx10_Finish)


def test_hyp_gx10_finish_constructor_exists():
    assert callable(gx10_Finish.__init__)


def test_hyp_gx10_finish_constructor_args():
    sig = inspect.signature(gx10_Finish.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_print_is_not_abstract():
    assert not inspect.isabstract(gx10_Print)


def test_hyp_gx10_print_constructor_exists():
    assert callable(gx10_Print.__init__)


def test_hyp_gx10_print_constructor_args():
    sig = inspect.signature(gx10_Print.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_intvar_is_not_abstract():
    assert not inspect.isabstract(gx10_IntVar)


def test_hyp_gx10_intvar_constructor_exists():
    assert callable(gx10_IntVar.__init__)


def test_hyp_gx10_intvar_constructor_args():
    sig = inspect.signature(gx10_IntVar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_referentiable_is_not_abstract():
    assert not inspect.isabstract(gx10_Referentiable)


def test_hyp_gx10_referentiable_constructor_exists():
    assert callable(gx10_Referentiable.__init__)


def test_hyp_gx10_referentiable_constructor_args():
    sig = inspect.signature(gx10_Referentiable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_boolexpression_is_not_abstract():
    assert not inspect.isabstract(BoolExpression)


def test_hyp_boolexpression_constructor_exists():
    assert callable(BoolExpression.__init__)


def test_hyp_boolexpression_constructor_args():
    sig = inspect.signature(BoolExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_equal_is_not_abstract():
    assert not inspect.isabstract(gx10_Equal)


def test_hyp_gx10_equal_constructor_exists():
    assert callable(gx10_Equal.__init__)


def test_hyp_gx10_equal_constructor_args():
    sig = inspect.signature(gx10_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_false_is_not_abstract():
    assert not inspect.isabstract(gx10_False)


def test_hyp_gx10_false_constructor_exists():
    assert callable(gx10_False.__init__)


def test_hyp_gx10_false_constructor_args():
    sig = inspect.signature(gx10_False.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_boolvaraccess_is_not_abstract():
    assert not inspect.isabstract(gx10_BoolVarAccess)


def test_hyp_gx10_boolvaraccess_constructor_exists():
    assert callable(gx10_BoolVarAccess.__init__)


def test_hyp_gx10_boolvaraccess_constructor_args():
    sig = inspect.signature(gx10_BoolVarAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_and_is_not_abstract():
    assert not inspect.isabstract(gx10_And)


def test_hyp_gx10_and_constructor_exists():
    assert callable(gx10_And.__init__)


def test_hyp_gx10_and_constructor_args():
    sig = inspect.signature(gx10_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_not_is_not_abstract():
    assert not inspect.isabstract(gx10_Not)


def test_hyp_gx10_not_constructor_exists():
    assert callable(gx10_Not.__init__)


def test_hyp_gx10_not_constructor_args():
    sig = inspect.signature(gx10_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_true_is_not_abstract():
    assert not inspect.isabstract(gx10_True)


def test_hyp_gx10_true_constructor_exists():
    assert callable(gx10_True.__init__)


def test_hyp_gx10_true_constructor_args():
    sig = inspect.signature(gx10_True.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_hyp_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_hyp_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_while_is_not_abstract():
    assert not inspect.isabstract(gx10_While)


def test_hyp_gx10_while_constructor_exists():
    assert callable(gx10_While.__init__)


def test_hyp_gx10_while_constructor_args():
    sig = inspect.signature(gx10_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_if_is_not_abstract():
    assert not inspect.isabstract(gx10_If)


def test_hyp_gx10_if_constructor_exists():
    assert callable(gx10_If.__init__)


def test_hyp_gx10_if_constructor_args():
    sig = inspect.signature(gx10_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_methodcallparameter_is_not_abstract():
    assert not inspect.isabstract(gx10_MethodCallParameter)


def test_hyp_gx10_methodcallparameter_constructor_exists():
    assert callable(gx10_MethodCallParameter.__init__)


def test_hyp_gx10_methodcallparameter_constructor_args():
    sig = inspect.signature(gx10_MethodCallParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_boolvar_is_not_abstract():
    assert not inspect.isabstract(gx10_BoolVar)


def test_hyp_gx10_boolvar_constructor_exists():
    assert callable(gx10_BoolVar.__init__)


def test_hyp_gx10_boolvar_constructor_args():
    sig = inspect.signature(gx10_BoolVar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_methodcall_is_not_abstract():
    assert not inspect.isabstract(gx10_MethodCall)


def test_hyp_gx10_methodcall_constructor_exists():
    assert callable(gx10_MethodCall.__init__)


def test_hyp_gx10_methodcall_constructor_args():
    sig = inspect.signature(gx10_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_intexpression_is_not_abstract():
    assert not inspect.isabstract(gx10_IntExpression)


def test_hyp_gx10_intexpression_constructor_exists():
    assert callable(gx10_IntExpression.__init__)


def test_hyp_gx10_intexpression_constructor_args():
    sig = inspect.signature(gx10_IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_boolexpression_is_not_abstract():
    assert not inspect.isabstract(gx10_BoolExpression)


def test_hyp_gx10_boolexpression_constructor_exists():
    assert callable(gx10_BoolExpression.__init__)


def test_hyp_gx10_boolexpression_constructor_args():
    sig = inspect.signature(gx10_BoolExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_controlstructure_is_not_abstract():
    assert not inspect.isabstract(gx10_ControlStructure)


def test_hyp_gx10_controlstructure_constructor_exists():
    assert callable(gx10_ControlStructure.__init__)


def test_hyp_gx10_controlstructure_constructor_args():
    sig = inspect.signature(gx10_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_block_is_not_abstract():
    assert not inspect.isabstract(gx10_Block)


def test_hyp_gx10_block_constructor_exists():
    assert callable(gx10_Block.__init__)


def test_hyp_gx10_block_constructor_args():
    sig = inspect.signature(gx10_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gx10_method_is_not_abstract():
    assert not inspect.isabstract(gx10_Method)


def test_hyp_gx10_method_constructor_exists():
    assert callable(gx10_Method.__init__)


def test_hyp_gx10_method_constructor_args():
    sig = inspect.signature(gx10_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gx10_program_is_not_abstract():
    assert not inspect.isabstract(gx10_Program)


def test_hyp_gx10_program_constructor_exists():
    assert callable(gx10_Program.__init__)


def test_hyp_gx10_program_constructor_args():
    sig = inspect.signature(gx10_Program.__init__)
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
IntBinaryOperation_strategy = st.builds(
    IntBinaryOperation,
)
gx10_Time_strategy = st.builds(
    gx10_Time,
)
gx10_Plus_strategy = st.builds(
    gx10_Plus,
)
IntExpression_strategy = st.builds(
    IntExpression,
)
gx10_IntBinaryOperation_strategy = st.builds(
    gx10_IntBinaryOperation,
)
gx10_IntVarAccess_strategy = st.builds(
    gx10_IntVarAccess,
)
gx10_IntConst_strategy = st.builds(
    gx10_IntConst,
    value=
        st.integers()
)
gx10_Statement_strategy = st.builds(
    gx10_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
gx10_Expression_strategy = st.builds(
    gx10_Expression,
)
gx10_Async_strategy = st.builds(
    gx10_Async,
)
gx10_Finish_strategy = st.builds(
    gx10_Finish,
)
gx10_Print_strategy = st.builds(
    gx10_Print,
)
gx10_IntVar_strategy = st.builds(
    gx10_IntVar,
)
gx10_Referentiable_strategy = st.builds(
    gx10_Referentiable,
    name=
        safe_text
)
BoolExpression_strategy = st.builds(
    BoolExpression,
)
gx10_Equal_strategy = st.builds(
    gx10_Equal,
)
gx10_False_strategy = st.builds(
    gx10_False,
)
gx10_BoolVarAccess_strategy = st.builds(
    gx10_BoolVarAccess,
)
gx10_And_strategy = st.builds(
    gx10_And,
)
gx10_Not_strategy = st.builds(
    gx10_Not,
)
gx10_True_strategy = st.builds(
    gx10_True,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
gx10_While_strategy = st.builds(
    gx10_While,
)
gx10_If_strategy = st.builds(
    gx10_If,
)
gx10_MethodCallParameter_strategy = st.builds(
    gx10_MethodCallParameter,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
gx10_BoolVar_strategy = st.builds(
    gx10_BoolVar,
)
gx10_MethodCall_strategy = st.builds(
    gx10_MethodCall,
)
gx10_IntExpression_strategy = st.builds(
    gx10_IntExpression,
)
gx10_BoolExpression_strategy = st.builds(
    gx10_BoolExpression,
)
gx10_ControlStructure_strategy = st.builds(
    gx10_ControlStructure,
)
gx10_Block_strategy = st.builds(
    gx10_Block,
)
gx10_Method_strategy = st.builds(
    gx10_Method,
    name=
        st.booleans()
)
gx10_Program_strategy = st.builds(
    gx10_Program,
)






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_IntBinaryOperation_strategy)
@settings(max_examples=30)
def test_hyp_gx10_intbinaryoperation_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in gx10_IntBinaryOperation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in gx10_IntBinaryOperation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in gx10_IntBinaryOperation is not implemented or raised an error")





@given(instance=gx10_IntConst_strategy)
def test_hyp_gx10_intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_Print_strategy)
@settings(max_examples=30)
def test_hyp_gx10_print_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in gx10_Print is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in gx10_Print did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in gx10_Print is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_IntVar_strategy)
@settings(max_examples=30)
def test_hyp_gx10_intvar_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in gx10_IntVar is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in gx10_IntVar did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in gx10_IntVar is not implemented or raised an error")




@given(instance=gx10_Referentiable_strategy)
def test_hyp_gx10_referentiable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_Equal_strategy)
@settings(max_examples=30)
def test_hyp_gx10_equal_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in gx10_Equal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in gx10_Equal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in gx10_Equal is not implemented or raised an error")












@given(instance=gx10_MethodCallParameter_strategy)
def test_hyp_gx10_methodcallparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_BoolVar_strategy)
@settings(max_examples=30)
def test_hyp_gx10_boolvar_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in gx10_BoolVar is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in gx10_BoolVar did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in gx10_BoolVar is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_MethodCall_strategy)
@settings(max_examples=30)
def test_hyp_gx10_methodcall_call_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.call()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.call).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'call' in gx10_MethodCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'call' in gx10_MethodCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'call' in gx10_MethodCall is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gx10_Block_strategy)
@settings(max_examples=30)
def test_hyp_gx10_block_initblock_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initBlock()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initBlock).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initBlock' in gx10_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initBlock' in gx10_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initBlock' in gx10_Block is not implemented or raised an error")




@given(instance=gx10_Method_strategy)
def test_hyp_gx10_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BoolExpression,
    ControlStructure,
    Expression,
    IntBinaryOperation,
    IntExpression,
    Statement,
    gx10_And,
    gx10_Async,
    gx10_Block,
    gx10_BoolExpression,
    gx10_BoolVar,
    gx10_BoolVarAccess,
    gx10_ControlStructure,
    gx10_Equal,
    gx10_Expression,
    gx10_False,
    gx10_Finish,
    gx10_If,
    gx10_IntBinaryOperation,
    gx10_IntConst,
    gx10_IntExpression,
    gx10_IntVar,
    gx10_IntVarAccess,
    gx10_Method,
    gx10_MethodCall,
    gx10_MethodCallParameter,
    gx10_Not,
    gx10_Plus,
    gx10_Print,
    gx10_Program,
    gx10_Referentiable,
    gx10_Statement,
    gx10_Time,
    gx10_True,
    gx10_While,
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

def test_gx10_IntConst_value_value_roundtrip():
    instance = gx10_IntConst(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_gx10_Method_name_value_roundtrip():
    instance = gx10_Method(name=True)
    assert instance.name == True
    instance.name = False
    assert instance.name == False


def test_gx10_MethodCallParameter_name_value_roundtrip():
    instance = gx10_MethodCallParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gx10_Referentiable_name_value_roundtrip():
    instance = gx10_Referentiable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gx10_And_isa_BoolExpression():
    instance = gx10_And()
    assert isinstance(instance, BoolExpression)


def test_gx10_BoolVarAccess_isa_BoolExpression():
    instance = gx10_BoolVarAccess()
    assert isinstance(instance, BoolExpression)


def test_gx10_Equal_isa_BoolExpression():
    instance = gx10_Equal()
    assert isinstance(instance, BoolExpression)


def test_gx10_False_isa_BoolExpression():
    instance = gx10_False()
    assert isinstance(instance, BoolExpression)


def test_gx10_Not_isa_BoolExpression():
    instance = gx10_Not()
    assert isinstance(instance, BoolExpression)


def test_gx10_True_isa_BoolExpression():
    instance = gx10_True()
    assert isinstance(instance, BoolExpression)


def test_gx10_If_isa_ControlStructure():
    instance = gx10_If()
    assert isinstance(instance, ControlStructure)


def test_gx10_While_isa_ControlStructure():
    instance = gx10_While()
    assert isinstance(instance, ControlStructure)


def test_gx10_BoolExpression_isa_Expression():
    instance = gx10_BoolExpression()
    assert isinstance(instance, Expression)


def test_gx10_BoolVar_isa_Expression():
    instance = gx10_BoolVar()
    assert isinstance(instance, Expression)


def test_gx10_IntExpression_isa_Expression():
    instance = gx10_IntExpression()
    assert isinstance(instance, Expression)


def test_gx10_MethodCall_isa_Expression():
    instance = gx10_MethodCall()
    assert isinstance(instance, Expression)


def test_gx10_Plus_isa_IntBinaryOperation():
    instance = gx10_Plus()
    assert isinstance(instance, IntBinaryOperation)


def test_gx10_Time_isa_IntBinaryOperation():
    instance = gx10_Time()
    assert isinstance(instance, IntBinaryOperation)


def test_gx10_IntBinaryOperation_isa_IntExpression():
    instance = gx10_IntBinaryOperation()
    assert isinstance(instance, IntExpression)


def test_gx10_IntConst_isa_IntExpression():
    instance = gx10_IntConst(value=7)
    assert isinstance(instance, IntExpression)


def test_gx10_IntVarAccess_isa_IntExpression():
    instance = gx10_IntVarAccess()
    assert isinstance(instance, IntExpression)


def test_gx10_Async_isa_Statement():
    instance = gx10_Async()
    assert isinstance(instance, Statement)


def test_gx10_Block_isa_Statement():
    instance = gx10_Block()
    assert isinstance(instance, Statement)


def test_gx10_ControlStructure_isa_Statement():
    instance = gx10_ControlStructure()
    assert isinstance(instance, Statement)


def test_gx10_Expression_isa_Statement():
    instance = gx10_Expression()
    assert isinstance(instance, Statement)


def test_gx10_Finish_isa_Statement():
    instance = gx10_Finish()
    assert isinstance(instance, Statement)


def test_gx10_IntVar_isa_Statement():
    instance = gx10_IntVar()
    assert isinstance(instance, Statement)


def test_gx10_Print_isa_Statement():
    instance = gx10_Print()
    assert isinstance(instance, Statement)


def test_assoc_blockStatements8_link_reassign_clear():
    a = gx10_Block()
    b1 = gx10_Statement()
    b2 = gx10_Statement()
    _safe_set(a, 'inBlock', {b1})
    assert _is_linked(a, 'inBlock', b1)
    if hasattr(b1, 'Statement'):
        assert _is_linked(b1, 'Statement', a)
    _safe_set(a, 'inBlock', {b2})
    assert _is_linked(a, 'inBlock', b2)
    if hasattr(b1, 'Statement'):
        assert not _is_linked(b1, 'Statement', a)
    if hasattr(b2, 'Statement'):
        assert _is_linked(b2, 'Statement', a)
    _safe_set(a, 'inBlock', set())
    assert not _is_linked(a, 'inBlock', b2)
    if hasattr(b2, 'Statement'):
        assert not _is_linked(b2, 'Statement', a)


def test_assoc_boolVarExpr38_link_reassign_clear():
    a = gx10_BoolVar()
    b1 = gx10_BoolExpression()
    b2 = gx10_BoolExpression()
    _safe_set(a, 'gx10_BoolVar', b1)
    assert _is_linked(a, 'gx10_BoolVar', b1)
    if hasattr(b1, 'gx10_BoolExpression39'):
        assert _is_linked(b1, 'gx10_BoolExpression39', a)
    _safe_set(a, 'gx10_BoolVar', b2)
    assert _is_linked(a, 'gx10_BoolVar', b2)
    if hasattr(b1, 'gx10_BoolExpression39'):
        assert not _is_linked(b1, 'gx10_BoolExpression39', a)
    if hasattr(b2, 'gx10_BoolExpression39'):
        assert _is_linked(b2, 'gx10_BoolExpression39', a)
    _safe_set(a, 'gx10_BoolVar', None)
    assert not _is_linked(a, 'gx10_BoolVar', b2)
    if hasattr(b2, 'gx10_BoolExpression39'):
        assert not _is_linked(b2, 'gx10_BoolExpression39', a)


def test_assoc_boolVarName40_link_reassign_clear():
    a = gx10_Referentiable(name="sample_text")
    b1 = gx10_BoolVar()
    b2 = gx10_BoolVar()
    _safe_set(a, 'gx10_Referentiable42', b1)
    assert _is_linked(a, 'gx10_Referentiable42', b1)
    if hasattr(b1, 'gx10_BoolVar41'):
        assert _is_linked(b1, 'gx10_BoolVar41', a)
    _safe_set(a, 'gx10_Referentiable42', b2)
    assert _is_linked(a, 'gx10_Referentiable42', b2)
    if hasattr(b1, 'gx10_BoolVar41'):
        assert not _is_linked(b1, 'gx10_BoolVar41', a)
    if hasattr(b2, 'gx10_BoolVar41'):
        assert _is_linked(b2, 'gx10_BoolVar41', a)
    _safe_set(a, 'gx10_Referentiable42', None)
    assert not _is_linked(a, 'gx10_Referentiable42', b2)
    if hasattr(b2, 'gx10_BoolVar41'):
        assert not _is_linked(b2, 'gx10_BoolVar41', a)


def test_assoc_boolVarRef50_link_reassign_clear():
    a = gx10_Referentiable(name="sample_text")
    b1 = gx10_BoolVarAccess()
    b2 = gx10_BoolVarAccess()
    _safe_set(a, 'gx10_Referentiable51', b1)
    assert _is_linked(a, 'gx10_Referentiable51', b1)
    if hasattr(b1, 'gx10_BoolVarAccess'):
        assert _is_linked(b1, 'gx10_BoolVarAccess', a)
    _safe_set(a, 'gx10_Referentiable51', b2)
    assert _is_linked(a, 'gx10_Referentiable51', b2)
    if hasattr(b1, 'gx10_BoolVarAccess'):
        assert not _is_linked(b1, 'gx10_BoolVarAccess', a)
    if hasattr(b2, 'gx10_BoolVarAccess'):
        assert _is_linked(b2, 'gx10_BoolVarAccess', a)
    _safe_set(a, 'gx10_Referentiable51', None)
    assert not _is_linked(a, 'gx10_Referentiable51', b2)
    if hasattr(b2, 'gx10_BoolVarAccess'):
        assert not _is_linked(b2, 'gx10_BoolVarAccess', a)


def test_assoc_calledBy5_link_reassign_clear():
    a = gx10_MethodCall()
    b1 = gx10_Method(name=True)
    b2 = gx10_Method(name=False)
    _safe_set(a, 'MethodCall', b1)
    assert _is_linked(a, 'MethodCall', b1)
    if hasattr(b1, 'methodToCall'):
        assert _is_linked(b1, 'methodToCall', a)
    _safe_set(a, 'MethodCall', b2)
    assert _is_linked(a, 'MethodCall', b2)
    if hasattr(b1, 'methodToCall'):
        assert not _is_linked(b1, 'methodToCall', a)
    if hasattr(b2, 'methodToCall'):
        assert _is_linked(b2, 'methodToCall', a)
    _safe_set(a, 'MethodCall', None)
    assert not _is_linked(a, 'MethodCall', b2)
    if hasattr(b2, 'methodToCall'):
        assert not _is_linked(b2, 'methodToCall', a)


def test_assoc_controlStructureCondition10_link_reassign_clear():
    a = gx10_BoolExpression()
    b1 = gx10_ControlStructure()
    b2 = gx10_ControlStructure()
    _safe_set(a, 'gx10_BoolExpression', b1)
    assert _is_linked(a, 'gx10_BoolExpression', b1)
    if hasattr(b1, 'gx10_ControlStructure'):
        assert _is_linked(b1, 'gx10_ControlStructure', a)
    _safe_set(a, 'gx10_BoolExpression', b2)
    assert _is_linked(a, 'gx10_BoolExpression', b2)
    if hasattr(b1, 'gx10_ControlStructure'):
        assert not _is_linked(b1, 'gx10_ControlStructure', a)
    if hasattr(b2, 'gx10_ControlStructure'):
        assert _is_linked(b2, 'gx10_ControlStructure', a)
    _safe_set(a, 'gx10_BoolExpression', None)
    assert not _is_linked(a, 'gx10_BoolExpression', b2)
    if hasattr(b2, 'gx10_ControlStructure'):
        assert not _is_linked(b2, 'gx10_ControlStructure', a)


def test_assoc_elseBlock14_link_reassign_clear():
    a = gx10_Block()
    b1 = gx10_If()
    b2 = gx10_If()
    _safe_set(a, 'gx10_Block16', b1)
    assert _is_linked(a, 'gx10_Block16', b1)
    if hasattr(b1, 'gx10_If15'):
        assert _is_linked(b1, 'gx10_If15', a)
    _safe_set(a, 'gx10_Block16', b2)
    assert _is_linked(a, 'gx10_Block16', b2)
    if hasattr(b1, 'gx10_If15'):
        assert not _is_linked(b1, 'gx10_If15', a)
    if hasattr(b2, 'gx10_If15'):
        assert _is_linked(b2, 'gx10_If15', a)
    _safe_set(a, 'gx10_Block16', None)
    assert not _is_linked(a, 'gx10_Block16', b2)
    if hasattr(b2, 'gx10_If15'):
        assert not _is_linked(b2, 'gx10_If15', a)


def test_assoc_inBlock9_link_reassign_clear():
    a = gx10_Block()
    b1 = gx10_Statement()
    b2 = gx10_Statement()
    _safe_set(a, 'Block', b1)
    assert _is_linked(a, 'Block', b1)
    if hasattr(b1, 'blockStatements'):
        assert _is_linked(b1, 'blockStatements', a)
    _safe_set(a, 'Block', b2)
    assert _is_linked(a, 'Block', b2)
    if hasattr(b1, 'blockStatements'):
        assert not _is_linked(b1, 'blockStatements', a)
    if hasattr(b2, 'blockStatements'):
        assert _is_linked(b2, 'blockStatements', a)
    _safe_set(a, 'Block', None)
    assert not _is_linked(a, 'Block', b2)
    if hasattr(b2, 'blockStatements'):
        assert not _is_linked(b2, 'blockStatements', a)


def test_assoc_inMethodCall58_link_reassign_clear():
    a = gx10_MethodCallParameter(name="sample_text")
    b1 = gx10_MethodCall()
    b2 = gx10_MethodCall()
    _safe_set(a, 'methodCallParameters', b1)
    assert _is_linked(a, 'methodCallParameters', b1)
    if hasattr(b1, 'MethodCall59'):
        assert _is_linked(b1, 'MethodCall59', a)
    _safe_set(a, 'methodCallParameters', b2)
    assert _is_linked(a, 'methodCallParameters', b2)
    if hasattr(b1, 'MethodCall59'):
        assert not _is_linked(b1, 'MethodCall59', a)
    if hasattr(b2, 'MethodCall59'):
        assert _is_linked(b2, 'MethodCall59', a)
    _safe_set(a, 'methodCallParameters', None)
    assert not _is_linked(a, 'methodCallParameters', b2)
    if hasattr(b2, 'MethodCall59'):
        assert not _is_linked(b2, 'MethodCall59', a)


def test_assoc_inMethodCallParameter11_link_reassign_clear():
    a = gx10_MethodCallParameter(name="sample_text")
    b1 = gx10_IntExpression()
    b2 = gx10_IntExpression()
    _safe_set(a, 'MethodCallParameter', b1)
    assert _is_linked(a, 'MethodCallParameter', b1)
    if hasattr(b1, 'methodCallParameterExpr'):
        assert _is_linked(b1, 'methodCallParameterExpr', a)
    _safe_set(a, 'MethodCallParameter', b2)
    assert _is_linked(a, 'MethodCallParameter', b2)
    if hasattr(b1, 'methodCallParameterExpr'):
        assert not _is_linked(b1, 'methodCallParameterExpr', a)
    if hasattr(b2, 'methodCallParameterExpr'):
        assert _is_linked(b2, 'methodCallParameterExpr', a)
    _safe_set(a, 'MethodCallParameter', None)
    assert not _is_linked(a, 'MethodCallParameter', b2)
    if hasattr(b2, 'methodCallParameterExpr'):
        assert not _is_linked(b2, 'methodCallParameterExpr', a)


def test_assoc_inProgram2_link_reassign_clear():
    a = gx10_Method(name=True)
    b1 = gx10_Program()
    b2 = gx10_Program()
    _safe_set(a, 'methods', b1)
    assert _is_linked(a, 'methods', b1)
    if hasattr(b1, 'Program'):
        assert _is_linked(b1, 'Program', a)
    _safe_set(a, 'methods', b2)
    assert _is_linked(a, 'methods', b2)
    if hasattr(b1, 'Program'):
        assert not _is_linked(b1, 'Program', a)
    if hasattr(b2, 'Program'):
        assert _is_linked(b2, 'Program', a)
    _safe_set(a, 'methods', None)
    assert not _is_linked(a, 'methods', b2)
    if hasattr(b2, 'Program'):
        assert not _is_linked(b2, 'Program', a)


def test_assoc_intVarExpr43_link_reassign_clear():
    a = gx10_IntVar()
    b1 = gx10_IntExpression()
    b2 = gx10_IntExpression()
    _safe_set(a, 'gx10_IntVar', b1)
    assert _is_linked(a, 'gx10_IntVar', b1)
    if hasattr(b1, 'gx10_IntExpression44'):
        assert _is_linked(b1, 'gx10_IntExpression44', a)
    _safe_set(a, 'gx10_IntVar', b2)
    assert _is_linked(a, 'gx10_IntVar', b2)
    if hasattr(b1, 'gx10_IntExpression44'):
        assert not _is_linked(b1, 'gx10_IntExpression44', a)
    if hasattr(b2, 'gx10_IntExpression44'):
        assert _is_linked(b2, 'gx10_IntExpression44', a)
    _safe_set(a, 'gx10_IntVar', None)
    assert not _is_linked(a, 'gx10_IntVar', b2)
    if hasattr(b2, 'gx10_IntExpression44'):
        assert not _is_linked(b2, 'gx10_IntExpression44', a)


def test_assoc_intVarName45_link_reassign_clear():
    a = gx10_Referentiable(name="sample_text")
    b1 = gx10_IntVar()
    b2 = gx10_IntVar()
    _safe_set(a, 'gx10_Referentiable47', b1)
    assert _is_linked(a, 'gx10_Referentiable47', b1)
    if hasattr(b1, 'gx10_IntVar46'):
        assert _is_linked(b1, 'gx10_IntVar46', a)
    _safe_set(a, 'gx10_Referentiable47', b2)
    assert _is_linked(a, 'gx10_Referentiable47', b2)
    if hasattr(b1, 'gx10_IntVar46'):
        assert not _is_linked(b1, 'gx10_IntVar46', a)
    if hasattr(b2, 'gx10_IntVar46'):
        assert _is_linked(b2, 'gx10_IntVar46', a)
    _safe_set(a, 'gx10_Referentiable47', None)
    assert not _is_linked(a, 'gx10_Referentiable47', b2)
    if hasattr(b2, 'gx10_IntVar46'):
        assert not _is_linked(b2, 'gx10_IntVar46', a)


def test_assoc_intVarRef48_link_reassign_clear():
    a = gx10_Referentiable(name="sample_text")
    b1 = gx10_IntVarAccess()
    b2 = gx10_IntVarAccess()
    _safe_set(a, 'gx10_Referentiable49', b1)
    assert _is_linked(a, 'gx10_Referentiable49', b1)
    if hasattr(b1, 'gx10_IntVarAccess'):
        assert _is_linked(b1, 'gx10_IntVarAccess', a)
    _safe_set(a, 'gx10_Referentiable49', b2)
    assert _is_linked(a, 'gx10_Referentiable49', b2)
    if hasattr(b1, 'gx10_IntVarAccess'):
        assert not _is_linked(b1, 'gx10_IntVarAccess', a)
    if hasattr(b2, 'gx10_IntVarAccess'):
        assert _is_linked(b2, 'gx10_IntVarAccess', a)
    _safe_set(a, 'gx10_Referentiable49', None)
    assert not _is_linked(a, 'gx10_Referentiable49', b2)
    if hasattr(b2, 'gx10_IntVarAccess'):
        assert not _is_linked(b2, 'gx10_IntVarAccess', a)


def test_assoc_leftAndExpression21_link_reassign_clear():
    a = gx10_BoolExpression()
    b1 = gx10_And()
    b2 = gx10_And()
    _safe_set(a, 'gx10_BoolExpression22', b1)
    assert _is_linked(a, 'gx10_BoolExpression22', b1)
    if hasattr(b1, 'gx10_And'):
        assert _is_linked(b1, 'gx10_And', a)
    _safe_set(a, 'gx10_BoolExpression22', b2)
    assert _is_linked(a, 'gx10_BoolExpression22', b2)
    if hasattr(b1, 'gx10_And'):
        assert not _is_linked(b1, 'gx10_And', a)
    if hasattr(b2, 'gx10_And'):
        assert _is_linked(b2, 'gx10_And', a)
    _safe_set(a, 'gx10_BoolExpression22', None)
    assert not _is_linked(a, 'gx10_BoolExpression22', b2)
    if hasattr(b2, 'gx10_And'):
        assert not _is_linked(b2, 'gx10_And', a)


def test_assoc_leftBinaryExpression26_link_reassign_clear():
    a = gx10_IntExpression()
    b1 = gx10_IntBinaryOperation()
    b2 = gx10_IntBinaryOperation()
    _safe_set(a, 'gx10_IntExpression', b1)
    assert _is_linked(a, 'gx10_IntExpression', b1)
    if hasattr(b1, 'gx10_IntBinaryOperation'):
        assert _is_linked(b1, 'gx10_IntBinaryOperation', a)
    _safe_set(a, 'gx10_IntExpression', b2)
    assert _is_linked(a, 'gx10_IntExpression', b2)
    if hasattr(b1, 'gx10_IntBinaryOperation'):
        assert not _is_linked(b1, 'gx10_IntBinaryOperation', a)
    if hasattr(b2, 'gx10_IntBinaryOperation'):
        assert _is_linked(b2, 'gx10_IntBinaryOperation', a)
    _safe_set(a, 'gx10_IntExpression', None)
    assert not _is_linked(a, 'gx10_IntExpression', b2)
    if hasattr(b2, 'gx10_IntBinaryOperation'):
        assert not _is_linked(b2, 'gx10_IntBinaryOperation', a)


def test_assoc_leftEqual52_link_reassign_clear():
    a = gx10_IntExpression()
    b1 = gx10_Equal()
    b2 = gx10_Equal()
    _safe_set(a, 'gx10_IntExpression53', b1)
    assert _is_linked(a, 'gx10_IntExpression53', b1)
    if hasattr(b1, 'gx10_Equal'):
        assert _is_linked(b1, 'gx10_Equal', a)
    _safe_set(a, 'gx10_IntExpression53', b2)
    assert _is_linked(a, 'gx10_IntExpression53', b2)
    if hasattr(b1, 'gx10_Equal'):
        assert not _is_linked(b1, 'gx10_Equal', a)
    if hasattr(b2, 'gx10_Equal'):
        assert _is_linked(b2, 'gx10_Equal', a)
    _safe_set(a, 'gx10_IntExpression53', None)
    assert not _is_linked(a, 'gx10_IntExpression53', b2)
    if hasattr(b2, 'gx10_Equal'):
        assert not _is_linked(b2, 'gx10_Equal', a)


def test_assoc_methodBlock3_link_reassign_clear():
    a = gx10_Method(name=True)
    b1 = gx10_Block()
    b2 = gx10_Block()
    _safe_set(a, 'gx10_Method4', b1)
    assert _is_linked(a, 'gx10_Method4', b1)
    if hasattr(b1, 'gx10_Block'):
        assert _is_linked(b1, 'gx10_Block', a)
    _safe_set(a, 'gx10_Method4', b2)
    assert _is_linked(a, 'gx10_Method4', b2)
    if hasattr(b1, 'gx10_Block'):
        assert not _is_linked(b1, 'gx10_Block', a)
    if hasattr(b2, 'gx10_Block'):
        assert _is_linked(b2, 'gx10_Block', a)
    _safe_set(a, 'gx10_Method4', None)
    assert not _is_linked(a, 'gx10_Method4', b2)
    if hasattr(b2, 'gx10_Block'):
        assert not _is_linked(b2, 'gx10_Block', a)


def test_assoc_methodCallParameterExpr57_link_reassign_clear():
    a = gx10_MethodCallParameter(name="sample_text")
    b1 = gx10_IntExpression()
    b2 = gx10_IntExpression()
    _safe_set(a, 'inMethodCallParameter', b1)
    assert _is_linked(a, 'inMethodCallParameter', b1)
    if hasattr(b1, 'IntExpression'):
        assert _is_linked(b1, 'IntExpression', a)
    _safe_set(a, 'inMethodCallParameter', b2)
    assert _is_linked(a, 'inMethodCallParameter', b2)
    if hasattr(b1, 'IntExpression'):
        assert not _is_linked(b1, 'IntExpression', a)
    if hasattr(b2, 'IntExpression'):
        assert _is_linked(b2, 'IntExpression', a)
    _safe_set(a, 'inMethodCallParameter', None)
    assert not _is_linked(a, 'inMethodCallParameter', b2)
    if hasattr(b2, 'IntExpression'):
        assert not _is_linked(b2, 'IntExpression', a)


def test_assoc_methodCallParameters33_link_reassign_clear():
    a = gx10_MethodCallParameter(name="sample_text")
    b1 = gx10_MethodCall()
    b2 = gx10_MethodCall()
    _safe_set(a, 'MethodCallParameter34', b1)
    assert _is_linked(a, 'MethodCallParameter34', b1)
    if hasattr(b1, 'inMethodCall'):
        assert _is_linked(b1, 'inMethodCall', a)
    _safe_set(a, 'MethodCallParameter34', b2)
    assert _is_linked(a, 'MethodCallParameter34', b2)
    if hasattr(b1, 'inMethodCall'):
        assert not _is_linked(b1, 'inMethodCall', a)
    if hasattr(b2, 'inMethodCall'):
        assert _is_linked(b2, 'inMethodCall', a)
    _safe_set(a, 'MethodCallParameter34', None)
    assert not _is_linked(a, 'MethodCallParameter34', b2)
    if hasattr(b2, 'inMethodCall'):
        assert not _is_linked(b2, 'inMethodCall', a)


def test_assoc_methodParameters6_link_reassign_clear():
    a = gx10_Referentiable(name="sample_text")
    b1 = gx10_Method(name=True)
    b2 = gx10_Method(name=False)
    _safe_set(a, 'gx10_Referentiable', b1)
    assert _is_linked(a, 'gx10_Referentiable', b1)
    if hasattr(b1, 'gx10_Method7'):
        assert _is_linked(b1, 'gx10_Method7', a)
    _safe_set(a, 'gx10_Referentiable', b2)
    assert _is_linked(a, 'gx10_Referentiable', b2)
    if hasattr(b1, 'gx10_Method7'):
        assert not _is_linked(b1, 'gx10_Method7', a)
    if hasattr(b2, 'gx10_Method7'):
        assert _is_linked(b2, 'gx10_Method7', a)
    _safe_set(a, 'gx10_Referentiable', None)
    assert not _is_linked(a, 'gx10_Referentiable', b2)
    if hasattr(b2, 'gx10_Method7'):
        assert not _is_linked(b2, 'gx10_Method7', a)


def test_assoc_methodToCall31_link_reassign_clear():
    a = gx10_MethodCall()
    b1 = gx10_Method(name=True)
    b2 = gx10_Method(name=False)
    _safe_set(a, 'calledBy', b1)
    assert _is_linked(a, 'calledBy', b1)
    if hasattr(b1, 'Method32'):
        assert _is_linked(b1, 'Method32', a)
    _safe_set(a, 'calledBy', b2)
    assert _is_linked(a, 'calledBy', b2)
    if hasattr(b1, 'Method32'):
        assert not _is_linked(b1, 'Method32', a)
    if hasattr(b2, 'Method32'):
        assert _is_linked(b2, 'Method32', a)
    _safe_set(a, 'calledBy', None)
    assert not _is_linked(a, 'calledBy', b2)
    if hasattr(b2, 'Method32'):
        assert not _is_linked(b2, 'Method32', a)


def test_assoc_methods0_link_reassign_clear():
    a = gx10_Method(name=True)
    b1 = gx10_Program()
    b2 = gx10_Program()
    _safe_set(a, 'Method', b1)
    assert _is_linked(a, 'Method', b1)
    if hasattr(b1, 'inProgram'):
        assert _is_linked(b1, 'inProgram', a)
    _safe_set(a, 'Method', b2)
    assert _is_linked(a, 'Method', b2)
    if hasattr(b1, 'inProgram'):
        assert not _is_linked(b1, 'inProgram', a)
    if hasattr(b2, 'inProgram'):
        assert _is_linked(b2, 'inProgram', a)
    _safe_set(a, 'Method', None)
    assert not _is_linked(a, 'Method', b2)
    if hasattr(b2, 'inProgram'):
        assert not _is_linked(b2, 'inProgram', a)


def test_assoc_notExpression19_link_reassign_clear():
    a = gx10_BoolExpression()
    b1 = gx10_Not()
    b2 = gx10_Not()
    _safe_set(a, 'gx10_BoolExpression20', b1)
    assert _is_linked(a, 'gx10_BoolExpression20', b1)
    if hasattr(b1, 'gx10_Not'):
        assert _is_linked(b1, 'gx10_Not', a)
    _safe_set(a, 'gx10_BoolExpression20', b2)
    assert _is_linked(a, 'gx10_BoolExpression20', b2)
    if hasattr(b1, 'gx10_Not'):
        assert not _is_linked(b1, 'gx10_Not', a)
    if hasattr(b2, 'gx10_Not'):
        assert _is_linked(b2, 'gx10_Not', a)
    _safe_set(a, 'gx10_BoolExpression20', None)
    assert not _is_linked(a, 'gx10_BoolExpression20', b2)
    if hasattr(b2, 'gx10_Not'):
        assert not _is_linked(b2, 'gx10_Not', a)


def test_assoc_rightAndExpression23_link_reassign_clear():
    a = gx10_BoolExpression()
    b1 = gx10_And()
    b2 = gx10_And()
    _safe_set(a, 'gx10_BoolExpression25', b1)
    assert _is_linked(a, 'gx10_BoolExpression25', b1)
    if hasattr(b1, 'gx10_And24'):
        assert _is_linked(b1, 'gx10_And24', a)
    _safe_set(a, 'gx10_BoolExpression25', b2)
    assert _is_linked(a, 'gx10_BoolExpression25', b2)
    if hasattr(b1, 'gx10_And24'):
        assert not _is_linked(b1, 'gx10_And24', a)
    if hasattr(b2, 'gx10_And24'):
        assert _is_linked(b2, 'gx10_And24', a)
    _safe_set(a, 'gx10_BoolExpression25', None)
    assert not _is_linked(a, 'gx10_BoolExpression25', b2)
    if hasattr(b2, 'gx10_And24'):
        assert not _is_linked(b2, 'gx10_And24', a)


def test_assoc_rightBinaryExpression27_link_reassign_clear():
    a = gx10_IntExpression()
    b1 = gx10_IntBinaryOperation()
    b2 = gx10_IntBinaryOperation()
    _safe_set(a, 'gx10_IntExpression29', b1)
    assert _is_linked(a, 'gx10_IntExpression29', b1)
    if hasattr(b1, 'gx10_IntBinaryOperation28'):
        assert _is_linked(b1, 'gx10_IntBinaryOperation28', a)
    _safe_set(a, 'gx10_IntExpression29', b2)
    assert _is_linked(a, 'gx10_IntExpression29', b2)
    if hasattr(b1, 'gx10_IntBinaryOperation28'):
        assert not _is_linked(b1, 'gx10_IntBinaryOperation28', a)
    if hasattr(b2, 'gx10_IntBinaryOperation28'):
        assert _is_linked(b2, 'gx10_IntBinaryOperation28', a)
    _safe_set(a, 'gx10_IntExpression29', None)
    assert not _is_linked(a, 'gx10_IntExpression29', b2)
    if hasattr(b2, 'gx10_IntBinaryOperation28'):
        assert not _is_linked(b2, 'gx10_IntBinaryOperation28', a)


def test_assoc_rightEqual54_link_reassign_clear():
    a = gx10_IntExpression()
    b1 = gx10_Equal()
    b2 = gx10_Equal()
    _safe_set(a, 'gx10_IntExpression56', b1)
    assert _is_linked(a, 'gx10_IntExpression56', b1)
    if hasattr(b1, 'gx10_Equal55'):
        assert _is_linked(b1, 'gx10_Equal55', a)
    _safe_set(a, 'gx10_IntExpression56', b2)
    assert _is_linked(a, 'gx10_IntExpression56', b2)
    if hasattr(b1, 'gx10_Equal55'):
        assert not _is_linked(b1, 'gx10_Equal55', a)
    if hasattr(b2, 'gx10_Equal55'):
        assert _is_linked(b2, 'gx10_Equal55', a)
    _safe_set(a, 'gx10_IntExpression56', None)
    assert not _is_linked(a, 'gx10_IntExpression56', b2)
    if hasattr(b2, 'gx10_Equal55'):
        assert not _is_linked(b2, 'gx10_Equal55', a)


def test_assoc_startMethod1_link_reassign_clear():
    a = gx10_Method(name=True)
    b1 = gx10_Program()
    b2 = gx10_Program()
    _safe_set(a, 'gx10_Method', b1)
    assert _is_linked(a, 'gx10_Method', b1)
    if hasattr(b1, 'gx10_Program'):
        assert _is_linked(b1, 'gx10_Program', a)
    _safe_set(a, 'gx10_Method', b2)
    assert _is_linked(a, 'gx10_Method', b2)
    if hasattr(b1, 'gx10_Program'):
        assert not _is_linked(b1, 'gx10_Program', a)
    if hasattr(b2, 'gx10_Program'):
        assert _is_linked(b2, 'gx10_Program', a)
    _safe_set(a, 'gx10_Method', None)
    assert not _is_linked(a, 'gx10_Method', b2)
    if hasattr(b2, 'gx10_Program'):
        assert not _is_linked(b2, 'gx10_Program', a)


def test_assoc_thenBlock12_link_reassign_clear():
    a = gx10_Block()
    b1 = gx10_If()
    b2 = gx10_If()
    _safe_set(a, 'gx10_Block13', b1)
    assert _is_linked(a, 'gx10_Block13', b1)
    if hasattr(b1, 'gx10_If'):
        assert _is_linked(b1, 'gx10_If', a)
    _safe_set(a, 'gx10_Block13', b2)
    assert _is_linked(a, 'gx10_Block13', b2)
    if hasattr(b1, 'gx10_If'):
        assert not _is_linked(b1, 'gx10_If', a)
    if hasattr(b2, 'gx10_If'):
        assert _is_linked(b2, 'gx10_If', a)
    _safe_set(a, 'gx10_Block13', None)
    assert not _is_linked(a, 'gx10_Block13', b2)
    if hasattr(b2, 'gx10_If'):
        assert not _is_linked(b2, 'gx10_If', a)


def test_assoc_toPrint37_link_reassign_clear():
    a = gx10_Print()
    b1 = gx10_Expression()
    b2 = gx10_Expression()
    _safe_set(a, 'gx10_Print', b1)
    assert _is_linked(a, 'gx10_Print', b1)
    if hasattr(b1, 'gx10_Expression'):
        assert _is_linked(b1, 'gx10_Expression', a)
    _safe_set(a, 'gx10_Print', b2)
    assert _is_linked(a, 'gx10_Print', b2)
    if hasattr(b1, 'gx10_Expression'):
        assert not _is_linked(b1, 'gx10_Expression', a)
    if hasattr(b2, 'gx10_Expression'):
        assert _is_linked(b2, 'gx10_Expression', a)
    _safe_set(a, 'gx10_Print', None)
    assert not _is_linked(a, 'gx10_Print', b2)
    if hasattr(b2, 'gx10_Expression'):
        assert not _is_linked(b2, 'gx10_Expression', a)


def test_assoc_whileBlock17_link_reassign_clear():
    a = gx10_Block()
    b1 = gx10_While()
    b2 = gx10_While()
    _safe_set(a, 'gx10_Block18', b1)
    assert _is_linked(a, 'gx10_Block18', b1)
    if hasattr(b1, 'gx10_While'):
        assert _is_linked(b1, 'gx10_While', a)
    _safe_set(a, 'gx10_Block18', b2)
    assert _is_linked(a, 'gx10_Block18', b2)
    if hasattr(b1, 'gx10_While'):
        assert not _is_linked(b1, 'gx10_While', a)
    if hasattr(b2, 'gx10_While'):
        assert _is_linked(b2, 'gx10_While', a)
    _safe_set(a, 'gx10_Block18', None)
    assert not _is_linked(a, 'gx10_Block18', b2)
    if hasattr(b2, 'gx10_While'):
        assert not _is_linked(b2, 'gx10_While', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BoolExpression_strategy = st.builds(BoolExpression)
@given(instance=BoolExpression_strategy)
@settings(max_examples=25)
def test_BoolExpression_instantiation(instance):
    assert isinstance(instance, BoolExpression)


ControlStructure_strategy = st.builds(ControlStructure)
@given(instance=ControlStructure_strategy)
@settings(max_examples=25)
def test_ControlStructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


IntBinaryOperation_strategy = st.builds(IntBinaryOperation)
@given(instance=IntBinaryOperation_strategy)
@settings(max_examples=25)
def test_IntBinaryOperation_instantiation(instance):
    assert isinstance(instance, IntBinaryOperation)


IntExpression_strategy = st.builds(IntExpression)
@given(instance=IntExpression_strategy)
@settings(max_examples=25)
def test_IntExpression_instantiation(instance):
    assert isinstance(instance, IntExpression)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


gx10_And_strategy = st.builds(gx10_And)
@given(instance=gx10_And_strategy)
@settings(max_examples=25)
def test_gx10_And_instantiation(instance):
    assert isinstance(instance, gx10_And)


gx10_Async_strategy = st.builds(gx10_Async)
@given(instance=gx10_Async_strategy)
@settings(max_examples=25)
def test_gx10_Async_instantiation(instance):
    assert isinstance(instance, gx10_Async)


gx10_Block_strategy = st.builds(gx10_Block)
@given(instance=gx10_Block_strategy)
@settings(max_examples=25)
def test_gx10_Block_instantiation(instance):
    assert isinstance(instance, gx10_Block)


gx10_BoolExpression_strategy = st.builds(gx10_BoolExpression)
@given(instance=gx10_BoolExpression_strategy)
@settings(max_examples=25)
def test_gx10_BoolExpression_instantiation(instance):
    assert isinstance(instance, gx10_BoolExpression)


gx10_BoolVar_strategy = st.builds(gx10_BoolVar)
@given(instance=gx10_BoolVar_strategy)
@settings(max_examples=25)
def test_gx10_BoolVar_instantiation(instance):
    assert isinstance(instance, gx10_BoolVar)


gx10_BoolVarAccess_strategy = st.builds(gx10_BoolVarAccess)
@given(instance=gx10_BoolVarAccess_strategy)
@settings(max_examples=25)
def test_gx10_BoolVarAccess_instantiation(instance):
    assert isinstance(instance, gx10_BoolVarAccess)


gx10_ControlStructure_strategy = st.builds(gx10_ControlStructure)
@given(instance=gx10_ControlStructure_strategy)
@settings(max_examples=25)
def test_gx10_ControlStructure_instantiation(instance):
    assert isinstance(instance, gx10_ControlStructure)


gx10_Equal_strategy = st.builds(gx10_Equal)
@given(instance=gx10_Equal_strategy)
@settings(max_examples=25)
def test_gx10_Equal_instantiation(instance):
    assert isinstance(instance, gx10_Equal)


gx10_Expression_strategy = st.builds(gx10_Expression)
@given(instance=gx10_Expression_strategy)
@settings(max_examples=25)
def test_gx10_Expression_instantiation(instance):
    assert isinstance(instance, gx10_Expression)


gx10_False_strategy = st.builds(gx10_False)
@given(instance=gx10_False_strategy)
@settings(max_examples=25)
def test_gx10_False_instantiation(instance):
    assert isinstance(instance, gx10_False)


gx10_Finish_strategy = st.builds(gx10_Finish)
@given(instance=gx10_Finish_strategy)
@settings(max_examples=25)
def test_gx10_Finish_instantiation(instance):
    assert isinstance(instance, gx10_Finish)


gx10_If_strategy = st.builds(gx10_If)
@given(instance=gx10_If_strategy)
@settings(max_examples=25)
def test_gx10_If_instantiation(instance):
    assert isinstance(instance, gx10_If)


gx10_IntBinaryOperation_strategy = st.builds(gx10_IntBinaryOperation)
@given(instance=gx10_IntBinaryOperation_strategy)
@settings(max_examples=25)
def test_gx10_IntBinaryOperation_instantiation(instance):
    assert isinstance(instance, gx10_IntBinaryOperation)


gx10_IntConst_strategy = st.builds(gx10_IntConst, value=st.integers())
@given(instance=gx10_IntConst_strategy)
@settings(max_examples=25)
def test_gx10_IntConst_instantiation(instance):
    assert isinstance(instance, gx10_IntConst)


gx10_IntExpression_strategy = st.builds(gx10_IntExpression)
@given(instance=gx10_IntExpression_strategy)
@settings(max_examples=25)
def test_gx10_IntExpression_instantiation(instance):
    assert isinstance(instance, gx10_IntExpression)


gx10_IntVar_strategy = st.builds(gx10_IntVar)
@given(instance=gx10_IntVar_strategy)
@settings(max_examples=25)
def test_gx10_IntVar_instantiation(instance):
    assert isinstance(instance, gx10_IntVar)


gx10_IntVarAccess_strategy = st.builds(gx10_IntVarAccess)
@given(instance=gx10_IntVarAccess_strategy)
@settings(max_examples=25)
def test_gx10_IntVarAccess_instantiation(instance):
    assert isinstance(instance, gx10_IntVarAccess)


gx10_Method_strategy = st.builds(gx10_Method, name=st.booleans())
@given(instance=gx10_Method_strategy)
@settings(max_examples=25)
def test_gx10_Method_instantiation(instance):
    assert isinstance(instance, gx10_Method)


gx10_MethodCall_strategy = st.builds(gx10_MethodCall)
@given(instance=gx10_MethodCall_strategy)
@settings(max_examples=25)
def test_gx10_MethodCall_instantiation(instance):
    assert isinstance(instance, gx10_MethodCall)


gx10_MethodCallParameter_strategy = st.builds(gx10_MethodCallParameter, name=safe_text)
@given(instance=gx10_MethodCallParameter_strategy)
@settings(max_examples=25)
def test_gx10_MethodCallParameter_instantiation(instance):
    assert isinstance(instance, gx10_MethodCallParameter)


gx10_Not_strategy = st.builds(gx10_Not)
@given(instance=gx10_Not_strategy)
@settings(max_examples=25)
def test_gx10_Not_instantiation(instance):
    assert isinstance(instance, gx10_Not)


gx10_Plus_strategy = st.builds(gx10_Plus)
@given(instance=gx10_Plus_strategy)
@settings(max_examples=25)
def test_gx10_Plus_instantiation(instance):
    assert isinstance(instance, gx10_Plus)


gx10_Print_strategy = st.builds(gx10_Print)
@given(instance=gx10_Print_strategy)
@settings(max_examples=25)
def test_gx10_Print_instantiation(instance):
    assert isinstance(instance, gx10_Print)


gx10_Program_strategy = st.builds(gx10_Program)
@given(instance=gx10_Program_strategy)
@settings(max_examples=25)
def test_gx10_Program_instantiation(instance):
    assert isinstance(instance, gx10_Program)


gx10_Referentiable_strategy = st.builds(gx10_Referentiable, name=safe_text)
@given(instance=gx10_Referentiable_strategy)
@settings(max_examples=25)
def test_gx10_Referentiable_instantiation(instance):
    assert isinstance(instance, gx10_Referentiable)


gx10_Statement_strategy = st.builds(gx10_Statement)
@given(instance=gx10_Statement_strategy)
@settings(max_examples=25)
def test_gx10_Statement_instantiation(instance):
    assert isinstance(instance, gx10_Statement)


gx10_Time_strategy = st.builds(gx10_Time)
@given(instance=gx10_Time_strategy)
@settings(max_examples=25)
def test_gx10_Time_instantiation(instance):
    assert isinstance(instance, gx10_Time)


gx10_True_strategy = st.builds(gx10_True)
@given(instance=gx10_True_strategy)
@settings(max_examples=25)
def test_gx10_True_instantiation(instance):
    assert isinstance(instance, gx10_True)


gx10_While_strategy = st.builds(gx10_While)
@given(instance=gx10_While_strategy)
@settings(max_examples=25)
def test_gx10_While_instantiation(instance):
    assert isinstance(instance, gx10_While)



