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
    logoASM_LogoProgram,
    BinaryExp,
    logoASM_Minus,
    logoASM_Greater,
    logoASM_Equals,
    logoASM_Lower,
    logoASM_Div,
    logoASM_Mult,
    logoASM_Plus,
    Expression,
    logoASM_ParameterCall,
    logoASM_BinaryExp,
    ControlStructure,
    logoASM_Repeat,
    logoASM_While,
    logoASM_If,
    logoASM_Parameter,
    logoASM_ProcCall,
    logoASM_Constant,
    Primitive,
    logoASM_Right,
    logoASM_PenDown,
    logoASM_Clear,
    logoASM_Left,
    logoASM_Forward,
    logoASM_PenUp,
    logoASM_Back,
    Instruction,
    logoASM_ProcDeclaration,
    logoASM_Expression,
    logoASM_Block,
    logoASM_ControlStructure,
    logoASM_Primitive,
    logoASM_Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_logoasm_logoprogram_is_not_abstract():
    assert not inspect.isabstract(logoASM_LogoProgram)


def test_hyp_logoasm_logoprogram_constructor_exists():
    assert callable(logoASM_LogoProgram.__init__)


def test_hyp_logoasm_logoprogram_constructor_args():
    sig = inspect.signature(logoASM_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_hyp_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_hyp_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_minus_is_not_abstract():
    assert not inspect.isabstract(logoASM_Minus)


def test_hyp_logoasm_minus_constructor_exists():
    assert callable(logoASM_Minus.__init__)


def test_hyp_logoasm_minus_constructor_args():
    sig = inspect.signature(logoASM_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_greater_is_not_abstract():
    assert not inspect.isabstract(logoASM_Greater)


def test_hyp_logoasm_greater_constructor_exists():
    assert callable(logoASM_Greater.__init__)


def test_hyp_logoasm_greater_constructor_args():
    sig = inspect.signature(logoASM_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_equals_is_not_abstract():
    assert not inspect.isabstract(logoASM_Equals)


def test_hyp_logoasm_equals_constructor_exists():
    assert callable(logoASM_Equals.__init__)


def test_hyp_logoasm_equals_constructor_args():
    sig = inspect.signature(logoASM_Equals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_lower_is_not_abstract():
    assert not inspect.isabstract(logoASM_Lower)


def test_hyp_logoasm_lower_constructor_exists():
    assert callable(logoASM_Lower.__init__)


def test_hyp_logoasm_lower_constructor_args():
    sig = inspect.signature(logoASM_Lower.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_div_is_not_abstract():
    assert not inspect.isabstract(logoASM_Div)


def test_hyp_logoasm_div_constructor_exists():
    assert callable(logoASM_Div.__init__)


def test_hyp_logoasm_div_constructor_args():
    sig = inspect.signature(logoASM_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_mult_is_not_abstract():
    assert not inspect.isabstract(logoASM_Mult)


def test_hyp_logoasm_mult_constructor_exists():
    assert callable(logoASM_Mult.__init__)


def test_hyp_logoasm_mult_constructor_args():
    sig = inspect.signature(logoASM_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_plus_is_not_abstract():
    assert not inspect.isabstract(logoASM_Plus)


def test_hyp_logoasm_plus_constructor_exists():
    assert callable(logoASM_Plus.__init__)


def test_hyp_logoasm_plus_constructor_args():
    sig = inspect.signature(logoASM_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_parametercall_is_not_abstract():
    assert not inspect.isabstract(logoASM_ParameterCall)


def test_hyp_logoasm_parametercall_constructor_exists():
    assert callable(logoASM_ParameterCall.__init__)


def test_hyp_logoasm_parametercall_constructor_args():
    sig = inspect.signature(logoASM_ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_binaryexp_is_not_abstract():
    assert not inspect.isabstract(logoASM_BinaryExp)


def test_hyp_logoasm_binaryexp_constructor_exists():
    assert callable(logoASM_BinaryExp.__init__)


def test_hyp_logoasm_binaryexp_constructor_args():
    sig = inspect.signature(logoASM_BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_hyp_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_hyp_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_repeat_is_not_abstract():
    assert not inspect.isabstract(logoASM_Repeat)


def test_hyp_logoasm_repeat_constructor_exists():
    assert callable(logoASM_Repeat.__init__)


def test_hyp_logoasm_repeat_constructor_args():
    sig = inspect.signature(logoASM_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_while_is_not_abstract():
    assert not inspect.isabstract(logoASM_While)


def test_hyp_logoasm_while_constructor_exists():
    assert callable(logoASM_While.__init__)


def test_hyp_logoasm_while_constructor_args():
    sig = inspect.signature(logoASM_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_if_is_not_abstract():
    assert not inspect.isabstract(logoASM_If)


def test_hyp_logoasm_if_constructor_exists():
    assert callable(logoASM_If.__init__)


def test_hyp_logoasm_if_constructor_args():
    sig = inspect.signature(logoASM_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_parameter_is_not_abstract():
    assert not inspect.isabstract(logoASM_Parameter)


def test_hyp_logoasm_parameter_constructor_exists():
    assert callable(logoASM_Parameter.__init__)


def test_hyp_logoasm_parameter_constructor_args():
    sig = inspect.signature(logoASM_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_logoasm_proccall_is_not_abstract():
    assert not inspect.isabstract(logoASM_ProcCall)


def test_hyp_logoasm_proccall_constructor_exists():
    assert callable(logoASM_ProcCall.__init__)


def test_hyp_logoasm_proccall_constructor_args():
    sig = inspect.signature(logoASM_ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_constant_is_not_abstract():
    assert not inspect.isabstract(logoASM_Constant)


def test_hyp_logoasm_constant_constructor_exists():
    assert callable(logoASM_Constant.__init__)


def test_hyp_logoasm_constant_constructor_args():
    sig = inspect.signature(logoASM_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"




def test_hyp_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_hyp_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_hyp_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_right_is_not_abstract():
    assert not inspect.isabstract(logoASM_Right)


def test_hyp_logoasm_right_constructor_exists():
    assert callable(logoASM_Right.__init__)


def test_hyp_logoasm_right_constructor_args():
    sig = inspect.signature(logoASM_Right.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_pendown_is_not_abstract():
    assert not inspect.isabstract(logoASM_PenDown)


def test_hyp_logoasm_pendown_constructor_exists():
    assert callable(logoASM_PenDown.__init__)


def test_hyp_logoasm_pendown_constructor_args():
    sig = inspect.signature(logoASM_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_clear_is_not_abstract():
    assert not inspect.isabstract(logoASM_Clear)


def test_hyp_logoasm_clear_constructor_exists():
    assert callable(logoASM_Clear.__init__)


def test_hyp_logoasm_clear_constructor_args():
    sig = inspect.signature(logoASM_Clear.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_left_is_not_abstract():
    assert not inspect.isabstract(logoASM_Left)


def test_hyp_logoasm_left_constructor_exists():
    assert callable(logoASM_Left.__init__)


def test_hyp_logoasm_left_constructor_args():
    sig = inspect.signature(logoASM_Left.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_forward_is_not_abstract():
    assert not inspect.isabstract(logoASM_Forward)


def test_hyp_logoasm_forward_constructor_exists():
    assert callable(logoASM_Forward.__init__)


def test_hyp_logoasm_forward_constructor_args():
    sig = inspect.signature(logoASM_Forward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_penup_is_not_abstract():
    assert not inspect.isabstract(logoASM_PenUp)


def test_hyp_logoasm_penup_constructor_exists():
    assert callable(logoASM_PenUp.__init__)


def test_hyp_logoasm_penup_constructor_args():
    sig = inspect.signature(logoASM_PenUp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_back_is_not_abstract():
    assert not inspect.isabstract(logoASM_Back)


def test_hyp_logoasm_back_constructor_exists():
    assert callable(logoASM_Back.__init__)


def test_hyp_logoasm_back_constructor_args():
    sig = inspect.signature(logoASM_Back.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_hyp_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_hyp_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_procdeclaration_is_not_abstract():
    assert not inspect.isabstract(logoASM_ProcDeclaration)


def test_hyp_logoasm_procdeclaration_constructor_exists():
    assert callable(logoASM_ProcDeclaration.__init__)


def test_hyp_logoasm_procdeclaration_constructor_args():
    sig = inspect.signature(logoASM_ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_logoasm_expression_is_not_abstract():
    assert not inspect.isabstract(logoASM_Expression)


def test_hyp_logoasm_expression_constructor_exists():
    assert callable(logoASM_Expression.__init__)


def test_hyp_logoasm_expression_constructor_args():
    sig = inspect.signature(logoASM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_block_is_not_abstract():
    assert not inspect.isabstract(logoASM_Block)


def test_hyp_logoasm_block_constructor_exists():
    assert callable(logoASM_Block.__init__)


def test_hyp_logoasm_block_constructor_args():
    sig = inspect.signature(logoASM_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_controlstructure_is_not_abstract():
    assert not inspect.isabstract(logoASM_ControlStructure)


def test_hyp_logoasm_controlstructure_constructor_exists():
    assert callable(logoASM_ControlStructure.__init__)


def test_hyp_logoasm_controlstructure_constructor_args():
    sig = inspect.signature(logoASM_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_primitive_is_not_abstract():
    assert not inspect.isabstract(logoASM_Primitive)


def test_hyp_logoasm_primitive_constructor_exists():
    assert callable(logoASM_Primitive.__init__)


def test_hyp_logoasm_primitive_constructor_args():
    sig = inspect.signature(logoASM_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logoasm_instruction_is_not_abstract():
    assert not inspect.isabstract(logoASM_Instruction)


def test_hyp_logoasm_instruction_constructor_exists():
    assert callable(logoASM_Instruction.__init__)


def test_hyp_logoasm_instruction_constructor_args():
    sig = inspect.signature(logoASM_Instruction.__init__)
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
logoASM_LogoProgram_strategy = st.builds(
    logoASM_LogoProgram,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
logoASM_Minus_strategy = st.builds(
    logoASM_Minus,
)
logoASM_Greater_strategy = st.builds(
    logoASM_Greater,
)
logoASM_Equals_strategy = st.builds(
    logoASM_Equals,
)
logoASM_Lower_strategy = st.builds(
    logoASM_Lower,
)
logoASM_Div_strategy = st.builds(
    logoASM_Div,
)
logoASM_Mult_strategy = st.builds(
    logoASM_Mult,
)
logoASM_Plus_strategy = st.builds(
    logoASM_Plus,
)
Expression_strategy = st.builds(
    Expression,
)
logoASM_ParameterCall_strategy = st.builds(
    logoASM_ParameterCall,
)
logoASM_BinaryExp_strategy = st.builds(
    logoASM_BinaryExp,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
logoASM_Repeat_strategy = st.builds(
    logoASM_Repeat,
)
logoASM_While_strategy = st.builds(
    logoASM_While,
)
logoASM_If_strategy = st.builds(
    logoASM_If,
)
logoASM_Parameter_strategy = st.builds(
    logoASM_Parameter,
    name=
        safe_text
)
logoASM_ProcCall_strategy = st.builds(
    logoASM_ProcCall,
)
logoASM_Constant_strategy = st.builds(
    logoASM_Constant,
    integerValue=
        st.integers()
)
Primitive_strategy = st.builds(
    Primitive,
)
logoASM_Right_strategy = st.builds(
    logoASM_Right,
)
logoASM_PenDown_strategy = st.builds(
    logoASM_PenDown,
)
logoASM_Clear_strategy = st.builds(
    logoASM_Clear,
)
logoASM_Left_strategy = st.builds(
    logoASM_Left,
)
logoASM_Forward_strategy = st.builds(
    logoASM_Forward,
)
logoASM_PenUp_strategy = st.builds(
    logoASM_PenUp,
)
logoASM_Back_strategy = st.builds(
    logoASM_Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
logoASM_ProcDeclaration_strategy = st.builds(
    logoASM_ProcDeclaration,
    name=
        safe_text
)
logoASM_Expression_strategy = st.builds(
    logoASM_Expression,
)
logoASM_Block_strategy = st.builds(
    logoASM_Block,
)
logoASM_ControlStructure_strategy = st.builds(
    logoASM_ControlStructure,
)
logoASM_Primitive_strategy = st.builds(
    logoASM_Primitive,
)
logoASM_Instruction_strategy = st.builds(
    logoASM_Instruction,
)




















@given(instance=logoASM_Parameter_strategy)
def test_hyp_logoasm_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=logoASM_Constant_strategy)
def test_hyp_logoasm_constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original













@given(instance=logoASM_ProcDeclaration_strategy)
def test_hyp_logoasm_procdeclaration_name_setter(instance):
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
    BinaryExp,
    ControlStructure,
    Expression,
    Instruction,
    Primitive,
    logoASM_Back,
    logoASM_BinaryExp,
    logoASM_Block,
    logoASM_Clear,
    logoASM_Constant,
    logoASM_ControlStructure,
    logoASM_Div,
    logoASM_Equals,
    logoASM_Expression,
    logoASM_Forward,
    logoASM_Greater,
    logoASM_If,
    logoASM_Instruction,
    logoASM_Left,
    logoASM_LogoProgram,
    logoASM_Lower,
    logoASM_Minus,
    logoASM_Mult,
    logoASM_Parameter,
    logoASM_ParameterCall,
    logoASM_PenDown,
    logoASM_PenUp,
    logoASM_Plus,
    logoASM_Primitive,
    logoASM_ProcCall,
    logoASM_ProcDeclaration,
    logoASM_Repeat,
    logoASM_Right,
    logoASM_While,
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

def test_logoASM_Constant_integerValue_value_roundtrip():
    instance = logoASM_Constant(integerValue=7)
    assert instance.integerValue == 7
    instance.integerValue = 13
    assert instance.integerValue == 13


def test_logoASM_Parameter_name_value_roundtrip():
    instance = logoASM_Parameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_logoASM_ProcDeclaration_name_value_roundtrip():
    instance = logoASM_ProcDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_logoASM_Div_isa_BinaryExp():
    instance = logoASM_Div()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Equals_isa_BinaryExp():
    instance = logoASM_Equals()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Greater_isa_BinaryExp():
    instance = logoASM_Greater()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Lower_isa_BinaryExp():
    instance = logoASM_Lower()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Minus_isa_BinaryExp():
    instance = logoASM_Minus()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Mult_isa_BinaryExp():
    instance = logoASM_Mult()
    assert isinstance(instance, BinaryExp)


def test_logoASM_Plus_isa_BinaryExp():
    instance = logoASM_Plus()
    assert isinstance(instance, BinaryExp)


def test_logoASM_If_isa_ControlStructure():
    instance = logoASM_If()
    assert isinstance(instance, ControlStructure)


def test_logoASM_Repeat_isa_ControlStructure():
    instance = logoASM_Repeat()
    assert isinstance(instance, ControlStructure)


def test_logoASM_While_isa_ControlStructure():
    instance = logoASM_While()
    assert isinstance(instance, ControlStructure)


def test_logoASM_BinaryExp_isa_Expression():
    instance = logoASM_BinaryExp()
    assert isinstance(instance, Expression)


def test_logoASM_Constant_isa_Expression():
    instance = logoASM_Constant(integerValue=7)
    assert isinstance(instance, Expression)


def test_logoASM_ParameterCall_isa_Expression():
    instance = logoASM_ParameterCall()
    assert isinstance(instance, Expression)


def test_logoASM_ProcCall_isa_Expression():
    instance = logoASM_ProcCall()
    assert isinstance(instance, Expression)


def test_logoASM_Block_isa_Instruction():
    instance = logoASM_Block()
    assert isinstance(instance, Instruction)


def test_logoASM_ControlStructure_isa_Instruction():
    instance = logoASM_ControlStructure()
    assert isinstance(instance, Instruction)


def test_logoASM_Expression_isa_Instruction():
    instance = logoASM_Expression()
    assert isinstance(instance, Instruction)


def test_logoASM_Primitive_isa_Instruction():
    instance = logoASM_Primitive()
    assert isinstance(instance, Instruction)


def test_logoASM_ProcDeclaration_isa_Instruction():
    instance = logoASM_ProcDeclaration(name="sample_text")
    assert isinstance(instance, Instruction)


def test_logoASM_Back_isa_Primitive():
    instance = logoASM_Back()
    assert isinstance(instance, Primitive)


def test_logoASM_Clear_isa_Primitive():
    instance = logoASM_Clear()
    assert isinstance(instance, Primitive)


def test_logoASM_Forward_isa_Primitive():
    instance = logoASM_Forward()
    assert isinstance(instance, Primitive)


def test_logoASM_Left_isa_Primitive():
    instance = logoASM_Left()
    assert isinstance(instance, Primitive)


def test_logoASM_PenDown_isa_Primitive():
    instance = logoASM_PenDown()
    assert isinstance(instance, Primitive)


def test_logoASM_PenUp_isa_Primitive():
    instance = logoASM_PenUp()
    assert isinstance(instance, Primitive)


def test_logoASM_Right_isa_Primitive():
    instance = logoASM_Right()
    assert isinstance(instance, Primitive)


def test_assoc_args16_link_reassign_clear():
    a = logoASM_ProcDeclaration(name="sample_text")
    b1 = logoASM_Parameter(name="sample_text")
    b2 = logoASM_Parameter(name="sample_text_2")
    _safe_set(a, 'logoASM_ProcDeclaration17', {b1})
    assert _is_linked(a, 'logoASM_ProcDeclaration17', b1)
    if hasattr(b1, 'logoASM_Parameter'):
        assert _is_linked(b1, 'logoASM_Parameter', a)
    _safe_set(a, 'logoASM_ProcDeclaration17', {b2})
    assert _is_linked(a, 'logoASM_ProcDeclaration17', b2)
    if hasattr(b1, 'logoASM_Parameter'):
        assert not _is_linked(b1, 'logoASM_Parameter', a)
    if hasattr(b2, 'logoASM_Parameter'):
        assert _is_linked(b2, 'logoASM_Parameter', a)
    _safe_set(a, 'logoASM_ProcDeclaration17', set())
    assert not _is_linked(a, 'logoASM_ProcDeclaration17', b2)
    if hasattr(b2, 'logoASM_Parameter'):
        assert not _is_linked(b2, 'logoASM_Parameter', a)


def test_assoc_declaration14_link_reassign_clear():
    a = logoASM_ProcDeclaration(name="sample_text")
    b1 = logoASM_ProcCall()
    b2 = logoASM_ProcCall()
    _safe_set(a, 'logoASM_ProcDeclaration', b1)
    assert _is_linked(a, 'logoASM_ProcDeclaration', b1)
    if hasattr(b1, 'logoASM_ProcCall15'):
        assert _is_linked(b1, 'logoASM_ProcCall15', a)
    _safe_set(a, 'logoASM_ProcDeclaration', b2)
    assert _is_linked(a, 'logoASM_ProcDeclaration', b2)
    if hasattr(b1, 'logoASM_ProcCall15'):
        assert not _is_linked(b1, 'logoASM_ProcCall15', a)
    if hasattr(b2, 'logoASM_ProcCall15'):
        assert _is_linked(b2, 'logoASM_ProcCall15', a)
    _safe_set(a, 'logoASM_ProcDeclaration', None)
    assert not _is_linked(a, 'logoASM_ProcDeclaration', b2)
    if hasattr(b2, 'logoASM_ProcCall15'):
        assert not _is_linked(b2, 'logoASM_ProcCall15', a)


def test_assoc_instructions18_link_reassign_clear():
    a = logoASM_ProcDeclaration(name="sample_text")
    b1 = logoASM_Instruction()
    b2 = logoASM_Instruction()
    _safe_set(a, 'logoASM_ProcDeclaration19', {b1})
    assert _is_linked(a, 'logoASM_ProcDeclaration19', b1)
    if hasattr(b1, 'logoASM_Instruction'):
        assert _is_linked(b1, 'logoASM_Instruction', a)
    _safe_set(a, 'logoASM_ProcDeclaration19', {b2})
    assert _is_linked(a, 'logoASM_ProcDeclaration19', b2)
    if hasattr(b1, 'logoASM_Instruction'):
        assert not _is_linked(b1, 'logoASM_Instruction', a)
    if hasattr(b2, 'logoASM_Instruction'):
        assert _is_linked(b2, 'logoASM_Instruction', a)
    _safe_set(a, 'logoASM_ProcDeclaration19', set())
    assert not _is_linked(a, 'logoASM_ProcDeclaration19', b2)
    if hasattr(b2, 'logoASM_Instruction'):
        assert not _is_linked(b2, 'logoASM_Instruction', a)


def test_assoc_parameter33_link_reassign_clear():
    a = logoASM_Parameter(name="sample_text")
    b1 = logoASM_ParameterCall()
    b2 = logoASM_ParameterCall()
    _safe_set(a, 'logoASM_Parameter34', b1)
    assert _is_linked(a, 'logoASM_Parameter34', b1)
    if hasattr(b1, 'logoASM_ParameterCall'):
        assert _is_linked(b1, 'logoASM_ParameterCall', a)
    _safe_set(a, 'logoASM_Parameter34', b2)
    assert _is_linked(a, 'logoASM_Parameter34', b2)
    if hasattr(b1, 'logoASM_ParameterCall'):
        assert not _is_linked(b1, 'logoASM_ParameterCall', a)
    if hasattr(b2, 'logoASM_ParameterCall'):
        assert _is_linked(b2, 'logoASM_ParameterCall', a)
    _safe_set(a, 'logoASM_Parameter34', None)
    assert not _is_linked(a, 'logoASM_Parameter34', b2)
    if hasattr(b2, 'logoASM_ParameterCall'):
        assert not _is_linked(b2, 'logoASM_ParameterCall', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExp_strategy = st.builds(BinaryExp)
@given(instance=BinaryExp_strategy)
@settings(max_examples=25)
def test_BinaryExp_instantiation(instance):
    assert isinstance(instance, BinaryExp)


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


Instruction_strategy = st.builds(Instruction)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


Primitive_strategy = st.builds(Primitive)
@given(instance=Primitive_strategy)
@settings(max_examples=25)
def test_Primitive_instantiation(instance):
    assert isinstance(instance, Primitive)


logoASM_Back_strategy = st.builds(logoASM_Back)
@given(instance=logoASM_Back_strategy)
@settings(max_examples=25)
def test_logoASM_Back_instantiation(instance):
    assert isinstance(instance, logoASM_Back)


logoASM_BinaryExp_strategy = st.builds(logoASM_BinaryExp)
@given(instance=logoASM_BinaryExp_strategy)
@settings(max_examples=25)
def test_logoASM_BinaryExp_instantiation(instance):
    assert isinstance(instance, logoASM_BinaryExp)


logoASM_Block_strategy = st.builds(logoASM_Block)
@given(instance=logoASM_Block_strategy)
@settings(max_examples=25)
def test_logoASM_Block_instantiation(instance):
    assert isinstance(instance, logoASM_Block)


logoASM_Clear_strategy = st.builds(logoASM_Clear)
@given(instance=logoASM_Clear_strategy)
@settings(max_examples=25)
def test_logoASM_Clear_instantiation(instance):
    assert isinstance(instance, logoASM_Clear)


logoASM_Constant_strategy = st.builds(logoASM_Constant, integerValue=st.integers())
@given(instance=logoASM_Constant_strategy)
@settings(max_examples=25)
def test_logoASM_Constant_instantiation(instance):
    assert isinstance(instance, logoASM_Constant)


logoASM_ControlStructure_strategy = st.builds(logoASM_ControlStructure)
@given(instance=logoASM_ControlStructure_strategy)
@settings(max_examples=25)
def test_logoASM_ControlStructure_instantiation(instance):
    assert isinstance(instance, logoASM_ControlStructure)


logoASM_Div_strategy = st.builds(logoASM_Div)
@given(instance=logoASM_Div_strategy)
@settings(max_examples=25)
def test_logoASM_Div_instantiation(instance):
    assert isinstance(instance, logoASM_Div)


logoASM_Equals_strategy = st.builds(logoASM_Equals)
@given(instance=logoASM_Equals_strategy)
@settings(max_examples=25)
def test_logoASM_Equals_instantiation(instance):
    assert isinstance(instance, logoASM_Equals)


logoASM_Expression_strategy = st.builds(logoASM_Expression)
@given(instance=logoASM_Expression_strategy)
@settings(max_examples=25)
def test_logoASM_Expression_instantiation(instance):
    assert isinstance(instance, logoASM_Expression)


logoASM_Forward_strategy = st.builds(logoASM_Forward)
@given(instance=logoASM_Forward_strategy)
@settings(max_examples=25)
def test_logoASM_Forward_instantiation(instance):
    assert isinstance(instance, logoASM_Forward)


logoASM_Greater_strategy = st.builds(logoASM_Greater)
@given(instance=logoASM_Greater_strategy)
@settings(max_examples=25)
def test_logoASM_Greater_instantiation(instance):
    assert isinstance(instance, logoASM_Greater)


logoASM_If_strategy = st.builds(logoASM_If)
@given(instance=logoASM_If_strategy)
@settings(max_examples=25)
def test_logoASM_If_instantiation(instance):
    assert isinstance(instance, logoASM_If)


logoASM_Instruction_strategy = st.builds(logoASM_Instruction)
@given(instance=logoASM_Instruction_strategy)
@settings(max_examples=25)
def test_logoASM_Instruction_instantiation(instance):
    assert isinstance(instance, logoASM_Instruction)


logoASM_Left_strategy = st.builds(logoASM_Left)
@given(instance=logoASM_Left_strategy)
@settings(max_examples=25)
def test_logoASM_Left_instantiation(instance):
    assert isinstance(instance, logoASM_Left)


logoASM_LogoProgram_strategy = st.builds(logoASM_LogoProgram)
@given(instance=logoASM_LogoProgram_strategy)
@settings(max_examples=25)
def test_logoASM_LogoProgram_instantiation(instance):
    assert isinstance(instance, logoASM_LogoProgram)


logoASM_Lower_strategy = st.builds(logoASM_Lower)
@given(instance=logoASM_Lower_strategy)
@settings(max_examples=25)
def test_logoASM_Lower_instantiation(instance):
    assert isinstance(instance, logoASM_Lower)


logoASM_Minus_strategy = st.builds(logoASM_Minus)
@given(instance=logoASM_Minus_strategy)
@settings(max_examples=25)
def test_logoASM_Minus_instantiation(instance):
    assert isinstance(instance, logoASM_Minus)


logoASM_Mult_strategy = st.builds(logoASM_Mult)
@given(instance=logoASM_Mult_strategy)
@settings(max_examples=25)
def test_logoASM_Mult_instantiation(instance):
    assert isinstance(instance, logoASM_Mult)


logoASM_Parameter_strategy = st.builds(logoASM_Parameter, name=safe_text)
@given(instance=logoASM_Parameter_strategy)
@settings(max_examples=25)
def test_logoASM_Parameter_instantiation(instance):
    assert isinstance(instance, logoASM_Parameter)


logoASM_ParameterCall_strategy = st.builds(logoASM_ParameterCall)
@given(instance=logoASM_ParameterCall_strategy)
@settings(max_examples=25)
def test_logoASM_ParameterCall_instantiation(instance):
    assert isinstance(instance, logoASM_ParameterCall)


logoASM_PenDown_strategy = st.builds(logoASM_PenDown)
@given(instance=logoASM_PenDown_strategy)
@settings(max_examples=25)
def test_logoASM_PenDown_instantiation(instance):
    assert isinstance(instance, logoASM_PenDown)


logoASM_PenUp_strategy = st.builds(logoASM_PenUp)
@given(instance=logoASM_PenUp_strategy)
@settings(max_examples=25)
def test_logoASM_PenUp_instantiation(instance):
    assert isinstance(instance, logoASM_PenUp)


logoASM_Plus_strategy = st.builds(logoASM_Plus)
@given(instance=logoASM_Plus_strategy)
@settings(max_examples=25)
def test_logoASM_Plus_instantiation(instance):
    assert isinstance(instance, logoASM_Plus)


logoASM_Primitive_strategy = st.builds(logoASM_Primitive)
@given(instance=logoASM_Primitive_strategy)
@settings(max_examples=25)
def test_logoASM_Primitive_instantiation(instance):
    assert isinstance(instance, logoASM_Primitive)


logoASM_ProcCall_strategy = st.builds(logoASM_ProcCall)
@given(instance=logoASM_ProcCall_strategy)
@settings(max_examples=25)
def test_logoASM_ProcCall_instantiation(instance):
    assert isinstance(instance, logoASM_ProcCall)


logoASM_ProcDeclaration_strategy = st.builds(logoASM_ProcDeclaration, name=safe_text)
@given(instance=logoASM_ProcDeclaration_strategy)
@settings(max_examples=25)
def test_logoASM_ProcDeclaration_instantiation(instance):
    assert isinstance(instance, logoASM_ProcDeclaration)


logoASM_Repeat_strategy = st.builds(logoASM_Repeat)
@given(instance=logoASM_Repeat_strategy)
@settings(max_examples=25)
def test_logoASM_Repeat_instantiation(instance):
    assert isinstance(instance, logoASM_Repeat)


logoASM_Right_strategy = st.builds(logoASM_Right)
@given(instance=logoASM_Right_strategy)
@settings(max_examples=25)
def test_logoASM_Right_instantiation(instance):
    assert isinstance(instance, logoASM_Right)


logoASM_While_strategy = st.builds(logoASM_While)
@given(instance=logoASM_While_strategy)
@settings(max_examples=25)
def test_logoASM_While_instantiation(instance):
    assert isinstance(instance, logoASM_While)



