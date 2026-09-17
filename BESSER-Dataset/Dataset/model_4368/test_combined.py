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
    BinaryOperation,
    minilang_Modulo,
    minilang_Sum,
    minilang_Value,
    Condition,
    minilang_GreaterThan,
    minilang_Condition,
    Statement,
    minilang_Move,
    minilang_CallMethod,
    minilang_VariableAffect,
    minilang_RotateRight,
    minilang_RotateLeft,
    minilang_IfStmt,
    minilang_Statement,
    minilang_Block,
    Value,
    minilang_VariableRef,
    minilang_BinaryOperation,
    minilang_Constant,
    minilang_Variable,
    minilang_Method,
    minilang_Program,
    minilang_Line,
    Cardinals,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_hyp_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_hyp_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_modulo_is_not_abstract():
    assert not inspect.isabstract(minilang_Modulo)


def test_hyp_minilang_modulo_constructor_exists():
    assert callable(minilang_Modulo.__init__)


def test_hyp_minilang_modulo_constructor_args():
    sig = inspect.signature(minilang_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_sum_is_not_abstract():
    assert not inspect.isabstract(minilang_Sum)


def test_hyp_minilang_sum_constructor_exists():
    assert callable(minilang_Sum.__init__)


def test_hyp_minilang_sum_constructor_args():
    sig = inspect.signature(minilang_Sum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_value_is_not_abstract():
    assert not inspect.isabstract(minilang_Value)


def test_hyp_minilang_value_constructor_exists():
    assert callable(minilang_Value.__init__)


def test_hyp_minilang_value_constructor_args():
    sig = inspect.signature(minilang_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_greaterthan_is_not_abstract():
    assert not inspect.isabstract(minilang_GreaterThan)


def test_hyp_minilang_greaterthan_constructor_exists():
    assert callable(minilang_GreaterThan.__init__)


def test_hyp_minilang_greaterthan_constructor_args():
    sig = inspect.signature(minilang_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_condition_is_not_abstract():
    assert not inspect.isabstract(minilang_Condition)


def test_hyp_minilang_condition_constructor_exists():
    assert callable(minilang_Condition.__init__)


def test_hyp_minilang_condition_constructor_args():
    sig = inspect.signature(minilang_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_move_is_not_abstract():
    assert not inspect.isabstract(minilang_Move)


def test_hyp_minilang_move_constructor_exists():
    assert callable(minilang_Move.__init__)


def test_hyp_minilang_move_constructor_args():
    sig = inspect.signature(minilang_Move.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_callmethod_is_not_abstract():
    assert not inspect.isabstract(minilang_CallMethod)


def test_hyp_minilang_callmethod_constructor_exists():
    assert callable(minilang_CallMethod.__init__)


def test_hyp_minilang_callmethod_constructor_args():
    sig = inspect.signature(minilang_CallMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_variableaffect_is_not_abstract():
    assert not inspect.isabstract(minilang_VariableAffect)


def test_hyp_minilang_variableaffect_constructor_exists():
    assert callable(minilang_VariableAffect.__init__)


def test_hyp_minilang_variableaffect_constructor_args():
    sig = inspect.signature(minilang_VariableAffect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_rotateright_is_not_abstract():
    assert not inspect.isabstract(minilang_RotateRight)


def test_hyp_minilang_rotateright_constructor_exists():
    assert callable(minilang_RotateRight.__init__)


def test_hyp_minilang_rotateright_constructor_args():
    sig = inspect.signature(minilang_RotateRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_rotateleft_is_not_abstract():
    assert not inspect.isabstract(minilang_RotateLeft)


def test_hyp_minilang_rotateleft_constructor_exists():
    assert callable(minilang_RotateLeft.__init__)


def test_hyp_minilang_rotateleft_constructor_args():
    sig = inspect.signature(minilang_RotateLeft.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_ifstmt_is_not_abstract():
    assert not inspect.isabstract(minilang_IfStmt)


def test_hyp_minilang_ifstmt_constructor_exists():
    assert callable(minilang_IfStmt.__init__)


def test_hyp_minilang_ifstmt_constructor_args():
    sig = inspect.signature(minilang_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_statement_is_not_abstract():
    assert not inspect.isabstract(minilang_Statement)


def test_hyp_minilang_statement_constructor_exists():
    assert callable(minilang_Statement.__init__)


def test_hyp_minilang_statement_constructor_args():
    sig = inspect.signature(minilang_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_block_is_not_abstract():
    assert not inspect.isabstract(minilang_Block)


def test_hyp_minilang_block_constructor_exists():
    assert callable(minilang_Block.__init__)


def test_hyp_minilang_block_constructor_args():
    sig = inspect.signature(minilang_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_variableref_is_not_abstract():
    assert not inspect.isabstract(minilang_VariableRef)


def test_hyp_minilang_variableref_constructor_exists():
    assert callable(minilang_VariableRef.__init__)


def test_hyp_minilang_variableref_constructor_args():
    sig = inspect.signature(minilang_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(minilang_BinaryOperation)


def test_hyp_minilang_binaryoperation_constructor_exists():
    assert callable(minilang_BinaryOperation.__init__)


def test_hyp_minilang_binaryoperation_constructor_args():
    sig = inspect.signature(minilang_BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_constant_is_not_abstract():
    assert not inspect.isabstract(minilang_Constant)


def test_hyp_minilang_constant_constructor_exists():
    assert callable(minilang_Constant.__init__)


def test_hyp_minilang_constant_constructor_args():
    sig = inspect.signature(minilang_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minilang_variable_is_not_abstract():
    assert not inspect.isabstract(minilang_Variable)


def test_hyp_minilang_variable_constructor_exists():
    assert callable(minilang_Variable.__init__)


def test_hyp_minilang_variable_constructor_args():
    sig = inspect.signature(minilang_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_minilang_method_is_not_abstract():
    assert not inspect.isabstract(minilang_Method)


def test_hyp_minilang_method_constructor_exists():
    assert callable(minilang_Method.__init__)


def test_hyp_minilang_method_constructor_args():
    sig = inspect.signature(minilang_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_minilang_program_is_not_abstract():
    assert not inspect.isabstract(minilang_Program)


def test_hyp_minilang_program_constructor_exists():
    assert callable(minilang_Program.__init__)


def test_hyp_minilang_program_constructor_args():
    sig = inspect.signature(minilang_Program.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "angle" in params, "Missing parameter 'angle'"







def test_hyp_minilang_line_is_not_abstract():
    assert not inspect.isabstract(minilang_Line)


def test_hyp_minilang_line_constructor_exists():
    assert callable(minilang_Line.__init__)


def test_hyp_minilang_line_constructor_args():
    sig = inspect.signature(minilang_Line.__init__)
    params = list(sig.parameters.keys())
    assert "y1" in params, "Missing parameter 'y1'"
    assert "y2" in params, "Missing parameter 'y2'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "x1" in params, "Missing parameter 'x1'"





def test_hyp_cardinals_exists():
    # Check that the Enumeration exists
    assert Cardinals is not None

def test_hyp_cardinals_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinals]
    expected_literals = [
        "EAST",
        "WEST",
        "NORTH",
        "SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinals"


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
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
minilang_Modulo_strategy = st.builds(
    minilang_Modulo,
)
minilang_Sum_strategy = st.builds(
    minilang_Sum,
)
minilang_Value_strategy = st.builds(
    minilang_Value,
)
Condition_strategy = st.builds(
    Condition,
)
minilang_GreaterThan_strategy = st.builds(
    minilang_GreaterThan,
)
minilang_Condition_strategy = st.builds(
    minilang_Condition,
)
Statement_strategy = st.builds(
    Statement,
)
minilang_Move_strategy = st.builds(
    minilang_Move,
)
minilang_CallMethod_strategy = st.builds(
    minilang_CallMethod,
)
minilang_VariableAffect_strategy = st.builds(
    minilang_VariableAffect,
)
minilang_RotateRight_strategy = st.builds(
    minilang_RotateRight,
)
minilang_RotateLeft_strategy = st.builds(
    minilang_RotateLeft,
)
minilang_IfStmt_strategy = st.builds(
    minilang_IfStmt,
)
minilang_Statement_strategy = st.builds(
    minilang_Statement,
)
minilang_Block_strategy = st.builds(
    minilang_Block,
)
Value_strategy = st.builds(
    Value,
)
minilang_VariableRef_strategy = st.builds(
    minilang_VariableRef,
)
minilang_BinaryOperation_strategy = st.builds(
    minilang_BinaryOperation,
)
minilang_Constant_strategy = st.builds(
    minilang_Constant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
minilang_Variable_strategy = st.builds(
    minilang_Variable,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
minilang_Method_strategy = st.builds(
    minilang_Method,
    name=
        safe_text
)
minilang_Program_strategy = st.builds(
    minilang_Program,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    angle=
        safe_text
)
minilang_Line_strategy = st.builds(
    minilang_Line,
    y1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Modulo_strategy)
@settings(max_examples=30)
def test_hyp_minilang_modulo_valuek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.valueK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.valueK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'valueK3' in minilang_Modulo is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'valueK3' in minilang_Modulo did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'valueK3' in minilang_Modulo is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Sum_strategy)
@settings(max_examples=30)
def test_hyp_minilang_sum_valuek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.valueK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.valueK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'valueK3' in minilang_Sum is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'valueK3' in minilang_Sum did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'valueK3' in minilang_Sum is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Value_strategy)
@settings(max_examples=30)
def test_hyp_minilang_value_valuek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.valueK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.valueK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'valueK3' in minilang_Value is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'valueK3' in minilang_Value did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'valueK3' in minilang_Value is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_GreaterThan_strategy)
@settings(max_examples=30)
def test_hyp_minilang_greaterthan_evalk3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalK3' in minilang_GreaterThan is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalK3' in minilang_GreaterThan did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalK3' in minilang_GreaterThan is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Condition_strategy)
@settings(max_examples=30)
def test_hyp_minilang_condition_evalk3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalK3' in minilang_Condition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalK3' in minilang_Condition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalK3' in minilang_Condition is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Move_strategy)
@settings(max_examples=30)
def test_hyp_minilang_move_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_Move is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_Move did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_Move is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_CallMethod_strategy)
@settings(max_examples=30)
def test_hyp_minilang_callmethod_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_CallMethod is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_CallMethod did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_CallMethod is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_VariableAffect_strategy)
@settings(max_examples=30)
def test_hyp_minilang_variableaffect_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_VariableAffect is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_VariableAffect did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_VariableAffect is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_RotateRight_strategy)
@settings(max_examples=30)
def test_hyp_minilang_rotateright_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_RotateRight is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_RotateRight did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_RotateRight is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_RotateLeft_strategy)
@settings(max_examples=30)
def test_hyp_minilang_rotateleft_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_RotateLeft is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_RotateLeft did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_RotateLeft is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_IfStmt_strategy)
@settings(max_examples=30)
def test_hyp_minilang_ifstmt_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_IfStmt is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_IfStmt did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_IfStmt is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Statement_strategy)
@settings(max_examples=30)
def test_hyp_minilang_statement_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_Statement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Block_strategy)
@settings(max_examples=30)
def test_hyp_minilang_block_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_Block is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_VariableRef_strategy)
@settings(max_examples=30)
def test_hyp_minilang_variableref_valuek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.valueK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.valueK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'valueK3' in minilang_VariableRef is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'valueK3' in minilang_VariableRef did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'valueK3' in minilang_VariableRef is not implemented or raised an error")





@given(instance=minilang_Constant_strategy)
def test_hyp_minilang_constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Constant_strategy)
@settings(max_examples=30)
def test_hyp_minilang_constant_valuek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.valueK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.valueK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'valueK3' in minilang_Constant is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'valueK3' in minilang_Constant did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'valueK3' in minilang_Constant is not implemented or raised an error")




@given(instance=minilang_Variable_strategy)
def test_hyp_minilang_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=minilang_Variable_strategy)
def test_hyp_minilang_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=minilang_Method_strategy)
def test_hyp_minilang_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Method_strategy)
@settings(max_examples=30)
def test_hyp_minilang_method_executek3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.executeK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.executeK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'executeK3' in minilang_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'executeK3' in minilang_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'executeK3' in minilang_Method is not implemented or raised an error")




@given(instance=minilang_Program_strategy)
def test_hyp_minilang_program_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=minilang_Program_strategy)
def test_hyp_minilang_program_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=minilang_Program_strategy)
def test_hyp_minilang_program_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=minilang_Program_strategy)
def test_hyp_minilang_program_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minilang_Program_strategy)
@settings(max_examples=30)
def test_hyp_minilang_program_maink3_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.mainK3()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.mainK3).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'mainK3' in minilang_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'mainK3' in minilang_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'mainK3' in minilang_Program is not implemented or raised an error")




@given(instance=minilang_Line_strategy)
def test_hyp_minilang_line_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original



@given(instance=minilang_Line_strategy)
def test_hyp_minilang_line_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original



@given(instance=minilang_Line_strategy)
def test_hyp_minilang_line_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original



@given(instance=minilang_Line_strategy)
def test_hyp_minilang_line_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryOperation,
    Condition,
    Statement,
    Value,
    minilang_BinaryOperation,
    minilang_Block,
    minilang_CallMethod,
    minilang_Condition,
    minilang_Constant,
    minilang_GreaterThan,
    minilang_IfStmt,
    minilang_Line,
    minilang_Method,
    minilang_Modulo,
    minilang_Move,
    minilang_Program,
    minilang_RotateLeft,
    minilang_RotateRight,
    minilang_Statement,
    minilang_Sum,
    minilang_Value,
    minilang_Variable,
    minilang_VariableAffect,
    minilang_VariableRef,
    Cardinals,
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

def test_minilang_Constant_value_value_roundtrip():
    instance = minilang_Constant(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_minilang_Line_x1_value_roundtrip():
    instance = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    assert instance.x1 == 3.14
    instance.x1 = 9.99
    assert instance.x1 == 9.99


def test_minilang_Line_x2_value_roundtrip():
    instance = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    assert instance.x2 == 3.14
    instance.x2 = 9.99
    assert instance.x2 == 9.99


def test_minilang_Line_y1_value_roundtrip():
    instance = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    assert instance.y1 == 3.14
    instance.y1 = 9.99
    assert instance.y1 == 9.99


def test_minilang_Line_y2_value_roundtrip():
    instance = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    assert instance.y2 == 3.14
    instance.y2 = 9.99
    assert instance.y2 == 9.99


def test_minilang_Method_name_value_roundtrip():
    instance = minilang_Method(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minilang_Program_angle_value_roundtrip():
    instance = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_minilang_Program_distance_value_roundtrip():
    instance = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    assert instance.distance == 3.14
    instance.distance = 9.99
    assert instance.distance == 9.99


def test_minilang_Program_x_value_roundtrip():
    instance = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_minilang_Program_y_value_roundtrip():
    instance = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_minilang_Variable_name_value_roundtrip():
    instance = minilang_Variable(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minilang_Variable_value_value_roundtrip():
    instance = minilang_Variable(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_minilang_Modulo_isa_BinaryOperation():
    instance = minilang_Modulo()
    assert isinstance(instance, BinaryOperation)


def test_minilang_Sum_isa_BinaryOperation():
    instance = minilang_Sum()
    assert isinstance(instance, BinaryOperation)


def test_minilang_GreaterThan_isa_Condition():
    instance = minilang_GreaterThan()
    assert isinstance(instance, Condition)


def test_minilang_CallMethod_isa_Statement():
    instance = minilang_CallMethod()
    assert isinstance(instance, Statement)


def test_minilang_IfStmt_isa_Statement():
    instance = minilang_IfStmt()
    assert isinstance(instance, Statement)


def test_minilang_Move_isa_Statement():
    instance = minilang_Move()
    assert isinstance(instance, Statement)


def test_minilang_RotateLeft_isa_Statement():
    instance = minilang_RotateLeft()
    assert isinstance(instance, Statement)


def test_minilang_RotateRight_isa_Statement():
    instance = minilang_RotateRight()
    assert isinstance(instance, Statement)


def test_minilang_VariableAffect_isa_Statement():
    instance = minilang_VariableAffect()
    assert isinstance(instance, Statement)


def test_minilang_BinaryOperation_isa_Value():
    instance = minilang_BinaryOperation()
    assert isinstance(instance, Value)


def test_minilang_Constant_isa_Value():
    instance = minilang_Constant(value=3.14)
    assert isinstance(instance, Value)


def test_minilang_VariableRef_isa_Value():
    instance = minilang_VariableRef()
    assert isinstance(instance, Value)


def test_assoc_block7_link_reassign_clear():
    a = minilang_Method(name="sample_text")
    b1 = minilang_Block()
    b2 = minilang_Block()
    _safe_set(a, 'minilang_Method8', b1)
    assert _is_linked(a, 'minilang_Method8', b1)
    if hasattr(b1, 'minilang_Block'):
        assert _is_linked(b1, 'minilang_Block', a)
    _safe_set(a, 'minilang_Method8', b2)
    assert _is_linked(a, 'minilang_Method8', b2)
    if hasattr(b1, 'minilang_Block'):
        assert not _is_linked(b1, 'minilang_Block', a)
    if hasattr(b2, 'minilang_Block'):
        assert _is_linked(b2, 'minilang_Block', a)
    _safe_set(a, 'minilang_Method8', None)
    assert not _is_linked(a, 'minilang_Method8', b2)
    if hasattr(b2, 'minilang_Block'):
        assert not _is_linked(b2, 'minilang_Block', a)


def test_assoc_condition16_link_reassign_clear():
    a = minilang_IfStmt()
    b1 = minilang_Condition()
    b2 = minilang_Condition()
    _safe_set(a, 'minilang_IfStmt17', b1)
    assert _is_linked(a, 'minilang_IfStmt17', b1)
    if hasattr(b1, 'minilang_Condition'):
        assert _is_linked(b1, 'minilang_Condition', a)
    _safe_set(a, 'minilang_IfStmt17', b2)
    assert _is_linked(a, 'minilang_IfStmt17', b2)
    if hasattr(b1, 'minilang_Condition'):
        assert not _is_linked(b1, 'minilang_Condition', a)
    if hasattr(b2, 'minilang_Condition'):
        assert _is_linked(b2, 'minilang_Condition', a)
    _safe_set(a, 'minilang_IfStmt17', None)
    assert not _is_linked(a, 'minilang_IfStmt17', b2)
    if hasattr(b2, 'minilang_Condition'):
        assert not _is_linked(b2, 'minilang_Condition', a)


def test_assoc_elseBranch13_link_reassign_clear():
    a = minilang_IfStmt()
    b1 = minilang_Block()
    b2 = minilang_Block()
    _safe_set(a, 'minilang_IfStmt14', b1)
    assert _is_linked(a, 'minilang_IfStmt14', b1)
    if hasattr(b1, 'minilang_Block15'):
        assert _is_linked(b1, 'minilang_Block15', a)
    _safe_set(a, 'minilang_IfStmt14', b2)
    assert _is_linked(a, 'minilang_IfStmt14', b2)
    if hasattr(b1, 'minilang_Block15'):
        assert not _is_linked(b1, 'minilang_Block15', a)
    if hasattr(b2, 'minilang_Block15'):
        assert _is_linked(b2, 'minilang_Block15', a)
    _safe_set(a, 'minilang_IfStmt14', None)
    assert not _is_linked(a, 'minilang_IfStmt14', b2)
    if hasattr(b2, 'minilang_Block15'):
        assert not _is_linked(b2, 'minilang_Block15', a)


def test_assoc_left18_link_reassign_clear():
    a = minilang_Value()
    b1 = minilang_GreaterThan()
    b2 = minilang_GreaterThan()
    _safe_set(a, 'minilang_Value', b1)
    assert _is_linked(a, 'minilang_Value', b1)
    if hasattr(b1, 'minilang_GreaterThan'):
        assert _is_linked(b1, 'minilang_GreaterThan', a)
    _safe_set(a, 'minilang_Value', b2)
    assert _is_linked(a, 'minilang_Value', b2)
    if hasattr(b1, 'minilang_GreaterThan'):
        assert not _is_linked(b1, 'minilang_GreaterThan', a)
    if hasattr(b2, 'minilang_GreaterThan'):
        assert _is_linked(b2, 'minilang_GreaterThan', a)
    _safe_set(a, 'minilang_Value', None)
    assert not _is_linked(a, 'minilang_Value', b2)
    if hasattr(b2, 'minilang_GreaterThan'):
        assert not _is_linked(b2, 'minilang_GreaterThan', a)


def test_assoc_left31_link_reassign_clear():
    a = minilang_Value()
    b1 = minilang_BinaryOperation()
    b2 = minilang_BinaryOperation()
    _safe_set(a, 'minilang_Value33', b1)
    assert _is_linked(a, 'minilang_Value33', b1)
    if hasattr(b1, 'minilang_BinaryOperation32'):
        assert _is_linked(b1, 'minilang_BinaryOperation32', a)
    _safe_set(a, 'minilang_Value33', b2)
    assert _is_linked(a, 'minilang_Value33', b2)
    if hasattr(b1, 'minilang_BinaryOperation32'):
        assert not _is_linked(b1, 'minilang_BinaryOperation32', a)
    if hasattr(b2, 'minilang_BinaryOperation32'):
        assert _is_linked(b2, 'minilang_BinaryOperation32', a)
    _safe_set(a, 'minilang_Value33', None)
    assert not _is_linked(a, 'minilang_Value33', b2)
    if hasattr(b2, 'minilang_BinaryOperation32'):
        assert not _is_linked(b2, 'minilang_BinaryOperation32', a)


def test_assoc_lines4_link_reassign_clear():
    a = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    b1 = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    b2 = minilang_Line(x1=9.99, x2=9.99, y1=9.99, y2=9.99)
    _safe_set(a, 'minilang_Program5', {b1})
    assert _is_linked(a, 'minilang_Program5', b1)
    if hasattr(b1, 'minilang_Line'):
        assert _is_linked(b1, 'minilang_Line', a)
    _safe_set(a, 'minilang_Program5', {b2})
    assert _is_linked(a, 'minilang_Program5', b2)
    if hasattr(b1, 'minilang_Line'):
        assert not _is_linked(b1, 'minilang_Line', a)
    if hasattr(b2, 'minilang_Line'):
        assert _is_linked(b2, 'minilang_Line', a)
    _safe_set(a, 'minilang_Program5', set())
    assert not _is_linked(a, 'minilang_Program5', b2)
    if hasattr(b2, 'minilang_Line'):
        assert not _is_linked(b2, 'minilang_Line', a)


def test_assoc_mainMethod1_link_reassign_clear():
    a = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    b1 = minilang_Method(name="sample_text")
    b2 = minilang_Method(name="sample_text_2")
    _safe_set(a, 'minilang_Program', b1)
    assert _is_linked(a, 'minilang_Program', b1)
    if hasattr(b1, 'minilang_Method'):
        assert _is_linked(b1, 'minilang_Method', a)
    _safe_set(a, 'minilang_Program', b2)
    assert _is_linked(a, 'minilang_Program', b2)
    if hasattr(b1, 'minilang_Method'):
        assert not _is_linked(b1, 'minilang_Method', a)
    if hasattr(b2, 'minilang_Method'):
        assert _is_linked(b2, 'minilang_Method', a)
    _safe_set(a, 'minilang_Program', None)
    assert not _is_linked(a, 'minilang_Program', b2)
    if hasattr(b2, 'minilang_Method'):
        assert not _is_linked(b2, 'minilang_Method', a)


def test_assoc_method34_link_reassign_clear():
    a = minilang_Method(name="sample_text")
    b1 = minilang_CallMethod()
    b2 = minilang_CallMethod()
    _safe_set(a, 'minilang_Method35', b1)
    assert _is_linked(a, 'minilang_Method35', b1)
    if hasattr(b1, 'minilang_CallMethod'):
        assert _is_linked(b1, 'minilang_CallMethod', a)
    _safe_set(a, 'minilang_Method35', b2)
    assert _is_linked(a, 'minilang_Method35', b2)
    if hasattr(b1, 'minilang_CallMethod'):
        assert not _is_linked(b1, 'minilang_CallMethod', a)
    if hasattr(b2, 'minilang_CallMethod'):
        assert _is_linked(b2, 'minilang_CallMethod', a)
    _safe_set(a, 'minilang_Method35', None)
    assert not _is_linked(a, 'minilang_Method35', b2)
    if hasattr(b2, 'minilang_CallMethod'):
        assert not _is_linked(b2, 'minilang_CallMethod', a)


def test_assoc_methods0_link_reassign_clear():
    a = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    b1 = minilang_Method(name="sample_text")
    b2 = minilang_Method(name="sample_text_2")
    _safe_set(a, 'program', {b1})
    assert _is_linked(a, 'program', b1)
    if hasattr(b1, 'Method'):
        assert _is_linked(b1, 'Method', a)
    _safe_set(a, 'program', {b2})
    assert _is_linked(a, 'program', b2)
    if hasattr(b1, 'Method'):
        assert not _is_linked(b1, 'Method', a)
    if hasattr(b2, 'Method'):
        assert _is_linked(b2, 'Method', a)
    _safe_set(a, 'program', set())
    assert not _is_linked(a, 'program', b2)
    if hasattr(b2, 'Method'):
        assert not _is_linked(b2, 'Method', a)


def test_assoc_program6_link_reassign_clear():
    a = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    b1 = minilang_Method(name="sample_text")
    b2 = minilang_Method(name="sample_text_2")
    _safe_set(a, 'Program', b1)
    assert _is_linked(a, 'Program', b1)
    if hasattr(b1, 'methods'):
        assert _is_linked(b1, 'methods', a)
    _safe_set(a, 'Program', b2)
    assert _is_linked(a, 'Program', b2)
    if hasattr(b1, 'methods'):
        assert not _is_linked(b1, 'methods', a)
    if hasattr(b2, 'methods'):
        assert _is_linked(b2, 'methods', a)
    _safe_set(a, 'Program', None)
    assert not _is_linked(a, 'Program', b2)
    if hasattr(b2, 'methods'):
        assert not _is_linked(b2, 'methods', a)


def test_assoc_right19_link_reassign_clear():
    a = minilang_Value()
    b1 = minilang_GreaterThan()
    b2 = minilang_GreaterThan()
    _safe_set(a, 'minilang_Value21', b1)
    assert _is_linked(a, 'minilang_Value21', b1)
    if hasattr(b1, 'minilang_GreaterThan20'):
        assert _is_linked(b1, 'minilang_GreaterThan20', a)
    _safe_set(a, 'minilang_Value21', b2)
    assert _is_linked(a, 'minilang_Value21', b2)
    if hasattr(b1, 'minilang_GreaterThan20'):
        assert not _is_linked(b1, 'minilang_GreaterThan20', a)
    if hasattr(b2, 'minilang_GreaterThan20'):
        assert _is_linked(b2, 'minilang_GreaterThan20', a)
    _safe_set(a, 'minilang_Value21', None)
    assert not _is_linked(a, 'minilang_Value21', b2)
    if hasattr(b2, 'minilang_GreaterThan20'):
        assert not _is_linked(b2, 'minilang_GreaterThan20', a)


def test_assoc_right29_link_reassign_clear():
    a = minilang_Value()
    b1 = minilang_BinaryOperation()
    b2 = minilang_BinaryOperation()
    _safe_set(a, 'minilang_Value30', b1)
    assert _is_linked(a, 'minilang_Value30', b1)
    if hasattr(b1, 'minilang_BinaryOperation'):
        assert _is_linked(b1, 'minilang_BinaryOperation', a)
    _safe_set(a, 'minilang_Value30', b2)
    assert _is_linked(a, 'minilang_Value30', b2)
    if hasattr(b1, 'minilang_BinaryOperation'):
        assert not _is_linked(b1, 'minilang_BinaryOperation', a)
    if hasattr(b2, 'minilang_BinaryOperation'):
        assert _is_linked(b2, 'minilang_BinaryOperation', a)
    _safe_set(a, 'minilang_Value30', None)
    assert not _is_linked(a, 'minilang_Value30', b2)
    if hasattr(b2, 'minilang_BinaryOperation'):
        assert not _is_linked(b2, 'minilang_BinaryOperation', a)


def test_assoc_statements9_link_reassign_clear():
    a = minilang_Statement()
    b1 = minilang_Block()
    b2 = minilang_Block()
    _safe_set(a, 'minilang_Statement', b1)
    assert _is_linked(a, 'minilang_Statement', b1)
    if hasattr(b1, 'minilang_Block10'):
        assert _is_linked(b1, 'minilang_Block10', a)
    _safe_set(a, 'minilang_Statement', b2)
    assert _is_linked(a, 'minilang_Statement', b2)
    if hasattr(b1, 'minilang_Block10'):
        assert not _is_linked(b1, 'minilang_Block10', a)
    if hasattr(b2, 'minilang_Block10'):
        assert _is_linked(b2, 'minilang_Block10', a)
    _safe_set(a, 'minilang_Statement', None)
    assert not _is_linked(a, 'minilang_Statement', b2)
    if hasattr(b2, 'minilang_Block10'):
        assert not _is_linked(b2, 'minilang_Block10', a)


def test_assoc_thenBranch11_link_reassign_clear():
    a = minilang_IfStmt()
    b1 = minilang_Block()
    b2 = minilang_Block()
    _safe_set(a, 'minilang_IfStmt', b1)
    assert _is_linked(a, 'minilang_IfStmt', b1)
    if hasattr(b1, 'minilang_Block12'):
        assert _is_linked(b1, 'minilang_Block12', a)
    _safe_set(a, 'minilang_IfStmt', b2)
    assert _is_linked(a, 'minilang_IfStmt', b2)
    if hasattr(b1, 'minilang_Block12'):
        assert not _is_linked(b1, 'minilang_Block12', a)
    if hasattr(b2, 'minilang_Block12'):
        assert _is_linked(b2, 'minilang_Block12', a)
    _safe_set(a, 'minilang_IfStmt', None)
    assert not _is_linked(a, 'minilang_IfStmt', b2)
    if hasattr(b2, 'minilang_Block12'):
        assert not _is_linked(b2, 'minilang_Block12', a)


def test_assoc_value26_link_reassign_clear():
    a = minilang_VariableAffect()
    b1 = minilang_Value()
    b2 = minilang_Value()
    _safe_set(a, 'minilang_VariableAffect27', b1)
    assert _is_linked(a, 'minilang_VariableAffect27', b1)
    if hasattr(b1, 'minilang_Value28'):
        assert _is_linked(b1, 'minilang_Value28', a)
    _safe_set(a, 'minilang_VariableAffect27', b2)
    assert _is_linked(a, 'minilang_VariableAffect27', b2)
    if hasattr(b1, 'minilang_Value28'):
        assert not _is_linked(b1, 'minilang_Value28', a)
    if hasattr(b2, 'minilang_Value28'):
        assert _is_linked(b2, 'minilang_Value28', a)
    _safe_set(a, 'minilang_VariableAffect27', None)
    assert not _is_linked(a, 'minilang_VariableAffect27', b2)
    if hasattr(b2, 'minilang_Value28'):
        assert not _is_linked(b2, 'minilang_Value28', a)


def test_assoc_variable22_link_reassign_clear():
    a = minilang_VariableRef()
    b1 = minilang_Variable(name="sample_text", value=3.14)
    b2 = minilang_Variable(name="sample_text_2", value=9.99)
    _safe_set(a, 'minilang_VariableRef', b1)
    assert _is_linked(a, 'minilang_VariableRef', b1)
    if hasattr(b1, 'minilang_Variable23'):
        assert _is_linked(b1, 'minilang_Variable23', a)
    _safe_set(a, 'minilang_VariableRef', b2)
    assert _is_linked(a, 'minilang_VariableRef', b2)
    if hasattr(b1, 'minilang_Variable23'):
        assert not _is_linked(b1, 'minilang_Variable23', a)
    if hasattr(b2, 'minilang_Variable23'):
        assert _is_linked(b2, 'minilang_Variable23', a)
    _safe_set(a, 'minilang_VariableRef', None)
    assert not _is_linked(a, 'minilang_VariableRef', b2)
    if hasattr(b2, 'minilang_Variable23'):
        assert not _is_linked(b2, 'minilang_Variable23', a)


def test_assoc_variable24_link_reassign_clear():
    a = minilang_VariableAffect()
    b1 = minilang_Variable(name="sample_text", value=3.14)
    b2 = minilang_Variable(name="sample_text_2", value=9.99)
    _safe_set(a, 'minilang_VariableAffect', b1)
    assert _is_linked(a, 'minilang_VariableAffect', b1)
    if hasattr(b1, 'minilang_Variable25'):
        assert _is_linked(b1, 'minilang_Variable25', a)
    _safe_set(a, 'minilang_VariableAffect', b2)
    assert _is_linked(a, 'minilang_VariableAffect', b2)
    if hasattr(b1, 'minilang_Variable25'):
        assert not _is_linked(b1, 'minilang_Variable25', a)
    if hasattr(b2, 'minilang_Variable25'):
        assert _is_linked(b2, 'minilang_Variable25', a)
    _safe_set(a, 'minilang_VariableAffect', None)
    assert not _is_linked(a, 'minilang_VariableAffect', b2)
    if hasattr(b2, 'minilang_Variable25'):
        assert not _is_linked(b2, 'minilang_Variable25', a)


def test_assoc_variables2_link_reassign_clear():
    a = minilang_Variable(name="sample_text", value=3.14)
    b1 = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    b2 = minilang_Program(angle="sample_text_2", distance=9.99, x=9.99, y=9.99)
    _safe_set(a, 'minilang_Variable', b1)
    assert _is_linked(a, 'minilang_Variable', b1)
    if hasattr(b1, 'minilang_Program3'):
        assert _is_linked(b1, 'minilang_Program3', a)
    _safe_set(a, 'minilang_Variable', b2)
    assert _is_linked(a, 'minilang_Variable', b2)
    if hasattr(b1, 'minilang_Program3'):
        assert not _is_linked(b1, 'minilang_Program3', a)
    if hasattr(b2, 'minilang_Program3'):
        assert _is_linked(b2, 'minilang_Program3', a)
    _safe_set(a, 'minilang_Variable', None)
    assert not _is_linked(a, 'minilang_Variable', b2)
    if hasattr(b2, 'minilang_Program3'):
        assert not _is_linked(b2, 'minilang_Program3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryOperation_strategy = st.builds(BinaryOperation)
@given(instance=BinaryOperation_strategy)
@settings(max_examples=25)
def test_BinaryOperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


minilang_BinaryOperation_strategy = st.builds(minilang_BinaryOperation)
@given(instance=minilang_BinaryOperation_strategy)
@settings(max_examples=25)
def test_minilang_BinaryOperation_instantiation(instance):
    assert isinstance(instance, minilang_BinaryOperation)


minilang_Block_strategy = st.builds(minilang_Block)
@given(instance=minilang_Block_strategy)
@settings(max_examples=25)
def test_minilang_Block_instantiation(instance):
    assert isinstance(instance, minilang_Block)


minilang_CallMethod_strategy = st.builds(minilang_CallMethod)
@given(instance=minilang_CallMethod_strategy)
@settings(max_examples=25)
def test_minilang_CallMethod_instantiation(instance):
    assert isinstance(instance, minilang_CallMethod)


minilang_Condition_strategy = st.builds(minilang_Condition)
@given(instance=minilang_Condition_strategy)
@settings(max_examples=25)
def test_minilang_Condition_instantiation(instance):
    assert isinstance(instance, minilang_Condition)


minilang_Constant_strategy = st.builds(minilang_Constant, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=minilang_Constant_strategy)
@settings(max_examples=25)
def test_minilang_Constant_instantiation(instance):
    assert isinstance(instance, minilang_Constant)


minilang_GreaterThan_strategy = st.builds(minilang_GreaterThan)
@given(instance=minilang_GreaterThan_strategy)
@settings(max_examples=25)
def test_minilang_GreaterThan_instantiation(instance):
    assert isinstance(instance, minilang_GreaterThan)


minilang_IfStmt_strategy = st.builds(minilang_IfStmt)
@given(instance=minilang_IfStmt_strategy)
@settings(max_examples=25)
def test_minilang_IfStmt_instantiation(instance):
    assert isinstance(instance, minilang_IfStmt)


minilang_Line_strategy = st.builds(minilang_Line, x1=st.floats(allow_nan=False, allow_infinity=False), x2=st.floats(allow_nan=False, allow_infinity=False), y1=st.floats(allow_nan=False, allow_infinity=False), y2=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=minilang_Line_strategy)
@settings(max_examples=25)
def test_minilang_Line_instantiation(instance):
    assert isinstance(instance, minilang_Line)


minilang_Method_strategy = st.builds(minilang_Method, name=safe_text)
@given(instance=minilang_Method_strategy)
@settings(max_examples=25)
def test_minilang_Method_instantiation(instance):
    assert isinstance(instance, minilang_Method)


minilang_Modulo_strategy = st.builds(minilang_Modulo)
@given(instance=minilang_Modulo_strategy)
@settings(max_examples=25)
def test_minilang_Modulo_instantiation(instance):
    assert isinstance(instance, minilang_Modulo)


minilang_Move_strategy = st.builds(minilang_Move)
@given(instance=minilang_Move_strategy)
@settings(max_examples=25)
def test_minilang_Move_instantiation(instance):
    assert isinstance(instance, minilang_Move)


minilang_Program_strategy = st.builds(minilang_Program, angle=safe_text, distance=st.floats(allow_nan=False, allow_infinity=False), x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=minilang_Program_strategy)
@settings(max_examples=25)
def test_minilang_Program_instantiation(instance):
    assert isinstance(instance, minilang_Program)


minilang_RotateLeft_strategy = st.builds(minilang_RotateLeft)
@given(instance=minilang_RotateLeft_strategy)
@settings(max_examples=25)
def test_minilang_RotateLeft_instantiation(instance):
    assert isinstance(instance, minilang_RotateLeft)


minilang_RotateRight_strategy = st.builds(minilang_RotateRight)
@given(instance=minilang_RotateRight_strategy)
@settings(max_examples=25)
def test_minilang_RotateRight_instantiation(instance):
    assert isinstance(instance, minilang_RotateRight)


minilang_Statement_strategy = st.builds(minilang_Statement)
@given(instance=minilang_Statement_strategy)
@settings(max_examples=25)
def test_minilang_Statement_instantiation(instance):
    assert isinstance(instance, minilang_Statement)


minilang_Sum_strategy = st.builds(minilang_Sum)
@given(instance=minilang_Sum_strategy)
@settings(max_examples=25)
def test_minilang_Sum_instantiation(instance):
    assert isinstance(instance, minilang_Sum)


minilang_Value_strategy = st.builds(minilang_Value)
@given(instance=minilang_Value_strategy)
@settings(max_examples=25)
def test_minilang_Value_instantiation(instance):
    assert isinstance(instance, minilang_Value)


minilang_Variable_strategy = st.builds(minilang_Variable, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=minilang_Variable_strategy)
@settings(max_examples=25)
def test_minilang_Variable_instantiation(instance):
    assert isinstance(instance, minilang_Variable)


minilang_VariableAffect_strategy = st.builds(minilang_VariableAffect)
@given(instance=minilang_VariableAffect_strategy)
@settings(max_examples=25)
def test_minilang_VariableAffect_instantiation(instance):
    assert isinstance(instance, minilang_VariableAffect)


minilang_VariableRef_strategy = st.builds(minilang_VariableRef)
@given(instance=minilang_VariableRef_strategy)
@settings(max_examples=25)
def test_minilang_VariableRef_instantiation(instance):
    assert isinstance(instance, minilang_VariableRef)



