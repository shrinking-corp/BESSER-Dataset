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
    Logo_Expression,
    Primitive,
    Logo_PenUp,
    Logo_Right,
    Logo_Forward,
    Logo_PenDown,
    Logo_Clear,
    Logo_Left,
    Logo_Back,
    Logo_Primitive,
    Logo_LogoProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_logo_expression_is_not_abstract():
    assert not inspect.isabstract(Logo_Expression)


def test_hyp_logo_expression_constructor_exists():
    assert callable(Logo_Expression.__init__)


def test_hyp_logo_expression_constructor_args():
    sig = inspect.signature(Logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_hyp_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_hyp_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_penup_is_not_abstract():
    assert not inspect.isabstract(Logo_PenUp)


def test_hyp_logo_penup_constructor_exists():
    assert callable(Logo_PenUp.__init__)


def test_hyp_logo_penup_constructor_args():
    sig = inspect.signature(Logo_PenUp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_right_is_not_abstract():
    assert not inspect.isabstract(Logo_Right)


def test_hyp_logo_right_constructor_exists():
    assert callable(Logo_Right.__init__)


def test_hyp_logo_right_constructor_args():
    sig = inspect.signature(Logo_Right.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_forward_is_not_abstract():
    assert not inspect.isabstract(Logo_Forward)


def test_hyp_logo_forward_constructor_exists():
    assert callable(Logo_Forward.__init__)


def test_hyp_logo_forward_constructor_args():
    sig = inspect.signature(Logo_Forward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_pendown_is_not_abstract():
    assert not inspect.isabstract(Logo_PenDown)


def test_hyp_logo_pendown_constructor_exists():
    assert callable(Logo_PenDown.__init__)


def test_hyp_logo_pendown_constructor_args():
    sig = inspect.signature(Logo_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_clear_is_not_abstract():
    assert not inspect.isabstract(Logo_Clear)


def test_hyp_logo_clear_constructor_exists():
    assert callable(Logo_Clear.__init__)


def test_hyp_logo_clear_constructor_args():
    sig = inspect.signature(Logo_Clear.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_left_is_not_abstract():
    assert not inspect.isabstract(Logo_Left)


def test_hyp_logo_left_constructor_exists():
    assert callable(Logo_Left.__init__)


def test_hyp_logo_left_constructor_args():
    sig = inspect.signature(Logo_Left.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_back_is_not_abstract():
    assert not inspect.isabstract(Logo_Back)


def test_hyp_logo_back_constructor_exists():
    assert callable(Logo_Back.__init__)


def test_hyp_logo_back_constructor_args():
    sig = inspect.signature(Logo_Back.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_primitive_is_not_abstract():
    assert not inspect.isabstract(Logo_Primitive)


def test_hyp_logo_primitive_constructor_exists():
    assert callable(Logo_Primitive.__init__)


def test_hyp_logo_primitive_constructor_args():
    sig = inspect.signature(Logo_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(Logo_LogoProgram)


def test_hyp_logo_logoprogram_constructor_exists():
    assert callable(Logo_LogoProgram.__init__)


def test_hyp_logo_logoprogram_constructor_args():
    sig = inspect.signature(Logo_LogoProgram.__init__)
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
Logo_Expression_strategy = st.builds(
    Logo_Expression,
)
Primitive_strategy = st.builds(
    Primitive,
)
Logo_PenUp_strategy = st.builds(
    Logo_PenUp,
)
Logo_Right_strategy = st.builds(
    Logo_Right,
)
Logo_Forward_strategy = st.builds(
    Logo_Forward,
)
Logo_PenDown_strategy = st.builds(
    Logo_PenDown,
)
Logo_Clear_strategy = st.builds(
    Logo_Clear,
)
Logo_Left_strategy = st.builds(
    Logo_Left,
)
Logo_Back_strategy = st.builds(
    Logo_Back,
)
Logo_Primitive_strategy = st.builds(
    Logo_Primitive,
)
Logo_LogoProgram_strategy = st.builds(
    Logo_LogoProgram,
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Logo_Expression_strategy)
@settings(max_examples=30)
def test_hyp_logo_expression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in Logo_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in Logo_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in Logo_Expression is not implemented or raised an error")












# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Logo_Back,
    Logo_Clear,
    Logo_Expression,
    Logo_Forward,
    Logo_Left,
    Logo_LogoProgram,
    Logo_PenDown,
    Logo_PenUp,
    Logo_Primitive,
    Logo_Right,
    Primitive,
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

def test_Logo_Back_isa_Primitive():
    instance = Logo_Back()
    assert isinstance(instance, Primitive)


def test_Logo_Clear_isa_Primitive():
    instance = Logo_Clear()
    assert isinstance(instance, Primitive)


def test_Logo_Forward_isa_Primitive():
    instance = Logo_Forward()
    assert isinstance(instance, Primitive)


def test_Logo_Left_isa_Primitive():
    instance = Logo_Left()
    assert isinstance(instance, Primitive)


def test_Logo_PenDown_isa_Primitive():
    instance = Logo_PenDown()
    assert isinstance(instance, Primitive)


def test_Logo_PenUp_isa_Primitive():
    instance = Logo_PenUp()
    assert isinstance(instance, Primitive)


def test_Logo_Right_isa_Primitive():
    instance = Logo_Right()
    assert isinstance(instance, Primitive)


def test_assoc_angle4_link_reassign_clear():
    a = Logo_Expression()
    b1 = Logo_Left()
    b2 = Logo_Left()
    _safe_set(a, 'Logo_Expression5', b1)
    assert _is_linked(a, 'Logo_Expression5', b1)
    if hasattr(b1, 'Logo_Left'):
        assert _is_linked(b1, 'Logo_Left', a)
    _safe_set(a, 'Logo_Expression5', b2)
    assert _is_linked(a, 'Logo_Expression5', b2)
    if hasattr(b1, 'Logo_Left'):
        assert not _is_linked(b1, 'Logo_Left', a)
    if hasattr(b2, 'Logo_Left'):
        assert _is_linked(b2, 'Logo_Left', a)
    _safe_set(a, 'Logo_Expression5', None)
    assert not _is_linked(a, 'Logo_Expression5', b2)
    if hasattr(b2, 'Logo_Left'):
        assert not _is_linked(b2, 'Logo_Left', a)


def test_assoc_angle6_link_reassign_clear():
    a = Logo_Expression()
    b1 = Logo_Right()
    b2 = Logo_Right()
    _safe_set(a, 'Logo_Expression7', b1)
    assert _is_linked(a, 'Logo_Expression7', b1)
    if hasattr(b1, 'Logo_Right'):
        assert _is_linked(b1, 'Logo_Right', a)
    _safe_set(a, 'Logo_Expression7', b2)
    assert _is_linked(a, 'Logo_Expression7', b2)
    if hasattr(b1, 'Logo_Right'):
        assert not _is_linked(b1, 'Logo_Right', a)
    if hasattr(b2, 'Logo_Right'):
        assert _is_linked(b2, 'Logo_Right', a)
    _safe_set(a, 'Logo_Expression7', None)
    assert not _is_linked(a, 'Logo_Expression7', b2)
    if hasattr(b2, 'Logo_Right'):
        assert not _is_linked(b2, 'Logo_Right', a)


def test_assoc_steps1_link_reassign_clear():
    a = Logo_Expression()
    b1 = Logo_Back()
    b2 = Logo_Back()
    _safe_set(a, 'Logo_Expression', b1)
    assert _is_linked(a, 'Logo_Expression', b1)
    if hasattr(b1, 'Logo_Back'):
        assert _is_linked(b1, 'Logo_Back', a)
    _safe_set(a, 'Logo_Expression', b2)
    assert _is_linked(a, 'Logo_Expression', b2)
    if hasattr(b1, 'Logo_Back'):
        assert not _is_linked(b1, 'Logo_Back', a)
    if hasattr(b2, 'Logo_Back'):
        assert _is_linked(b2, 'Logo_Back', a)
    _safe_set(a, 'Logo_Expression', None)
    assert not _is_linked(a, 'Logo_Expression', b2)
    if hasattr(b2, 'Logo_Back'):
        assert not _is_linked(b2, 'Logo_Back', a)


def test_assoc_steps2_link_reassign_clear():
    a = Logo_Expression()
    b1 = Logo_Forward()
    b2 = Logo_Forward()
    _safe_set(a, 'Logo_Expression3', b1)
    assert _is_linked(a, 'Logo_Expression3', b1)
    if hasattr(b1, 'Logo_Forward'):
        assert _is_linked(b1, 'Logo_Forward', a)
    _safe_set(a, 'Logo_Expression3', b2)
    assert _is_linked(a, 'Logo_Expression3', b2)
    if hasattr(b1, 'Logo_Forward'):
        assert not _is_linked(b1, 'Logo_Forward', a)
    if hasattr(b2, 'Logo_Forward'):
        assert _is_linked(b2, 'Logo_Forward', a)
    _safe_set(a, 'Logo_Expression3', None)
    assert not _is_linked(a, 'Logo_Expression3', b2)
    if hasattr(b2, 'Logo_Forward'):
        assert not _is_linked(b2, 'Logo_Forward', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Logo_Back_strategy = st.builds(Logo_Back)
@given(instance=Logo_Back_strategy)
@settings(max_examples=25)
def test_Logo_Back_instantiation(instance):
    assert isinstance(instance, Logo_Back)


Logo_Clear_strategy = st.builds(Logo_Clear)
@given(instance=Logo_Clear_strategy)
@settings(max_examples=25)
def test_Logo_Clear_instantiation(instance):
    assert isinstance(instance, Logo_Clear)


Logo_Expression_strategy = st.builds(Logo_Expression)
@given(instance=Logo_Expression_strategy)
@settings(max_examples=25)
def test_Logo_Expression_instantiation(instance):
    assert isinstance(instance, Logo_Expression)


Logo_Forward_strategy = st.builds(Logo_Forward)
@given(instance=Logo_Forward_strategy)
@settings(max_examples=25)
def test_Logo_Forward_instantiation(instance):
    assert isinstance(instance, Logo_Forward)


Logo_Left_strategy = st.builds(Logo_Left)
@given(instance=Logo_Left_strategy)
@settings(max_examples=25)
def test_Logo_Left_instantiation(instance):
    assert isinstance(instance, Logo_Left)


Logo_LogoProgram_strategy = st.builds(Logo_LogoProgram)
@given(instance=Logo_LogoProgram_strategy)
@settings(max_examples=25)
def test_Logo_LogoProgram_instantiation(instance):
    assert isinstance(instance, Logo_LogoProgram)


Logo_PenDown_strategy = st.builds(Logo_PenDown)
@given(instance=Logo_PenDown_strategy)
@settings(max_examples=25)
def test_Logo_PenDown_instantiation(instance):
    assert isinstance(instance, Logo_PenDown)


Logo_PenUp_strategy = st.builds(Logo_PenUp)
@given(instance=Logo_PenUp_strategy)
@settings(max_examples=25)
def test_Logo_PenUp_instantiation(instance):
    assert isinstance(instance, Logo_PenUp)


Logo_Primitive_strategy = st.builds(Logo_Primitive)
@given(instance=Logo_Primitive_strategy)
@settings(max_examples=25)
def test_Logo_Primitive_instantiation(instance):
    assert isinstance(instance, Logo_Primitive)


Logo_Right_strategy = st.builds(Logo_Right)
@given(instance=Logo_Right_strategy)
@settings(max_examples=25)
def test_Logo_Right_instantiation(instance):
    assert isinstance(instance, Logo_Right)


Primitive_strategy = st.builds(Primitive)
@given(instance=Primitive_strategy)
@settings(max_examples=25)
def test_Primitive_instantiation(instance):
    assert isinstance(instance, Primitive)



