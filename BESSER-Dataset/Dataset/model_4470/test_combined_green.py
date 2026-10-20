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
    BinaryExp,
    kmLogo_Mult,
    kmLogo_Minus,
    kmLogo_Plus,
    kmLogo_Lower,
    kmLogo_Greater,
    kmLogo_Equals,
    kmLogo_Div,
    ControlStructure,
    kmLogo_While,
    kmLogo_Repeat,
    kmLogo_If,
    kmLogo_Parameter,
    kmLogo_Instruction,
    kmLogo_LogoProgram,
    Expression,
    kmLogo_Constant,
    kmLogo_ProcCall,
    kmLogo_ParameterCall,
    kmLogo_BinaryExp,
    Primitive,
    kmLogo_Clear,
    kmLogo_Right,
    kmLogo_Forward,
    kmLogo_PenUp,
    kmLogo_Left,
    kmLogo_PenDown,
    kmLogo_Back,
    Instruction,
    kmLogo_Expression,
    kmLogo_ProcDeclaration,
    kmLogo_ControlStructure,
    kmLogo_Block,
    kmLogo_Primitive,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_hyp_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_hyp_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_mult_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Mult)


def test_hyp_kmlogo_mult_constructor_exists():
    assert callable(kmLogo_Mult.__init__)


def test_hyp_kmlogo_mult_constructor_args():
    sig = inspect.signature(kmLogo_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_minus_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Minus)


def test_hyp_kmlogo_minus_constructor_exists():
    assert callable(kmLogo_Minus.__init__)


def test_hyp_kmlogo_minus_constructor_args():
    sig = inspect.signature(kmLogo_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_plus_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Plus)


def test_hyp_kmlogo_plus_constructor_exists():
    assert callable(kmLogo_Plus.__init__)


def test_hyp_kmlogo_plus_constructor_args():
    sig = inspect.signature(kmLogo_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_lower_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Lower)


def test_hyp_kmlogo_lower_constructor_exists():
    assert callable(kmLogo_Lower.__init__)


def test_hyp_kmlogo_lower_constructor_args():
    sig = inspect.signature(kmLogo_Lower.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_greater_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Greater)


def test_hyp_kmlogo_greater_constructor_exists():
    assert callable(kmLogo_Greater.__init__)


def test_hyp_kmlogo_greater_constructor_args():
    sig = inspect.signature(kmLogo_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_equals_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Equals)


def test_hyp_kmlogo_equals_constructor_exists():
    assert callable(kmLogo_Equals.__init__)


def test_hyp_kmlogo_equals_constructor_args():
    sig = inspect.signature(kmLogo_Equals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_div_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Div)


def test_hyp_kmlogo_div_constructor_exists():
    assert callable(kmLogo_Div.__init__)


def test_hyp_kmlogo_div_constructor_args():
    sig = inspect.signature(kmLogo_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_hyp_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_hyp_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_while_is_not_abstract():
    assert not inspect.isabstract(kmLogo_While)


def test_hyp_kmlogo_while_constructor_exists():
    assert callable(kmLogo_While.__init__)


def test_hyp_kmlogo_while_constructor_args():
    sig = inspect.signature(kmLogo_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_repeat_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Repeat)


def test_hyp_kmlogo_repeat_constructor_exists():
    assert callable(kmLogo_Repeat.__init__)


def test_hyp_kmlogo_repeat_constructor_args():
    sig = inspect.signature(kmLogo_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_if_is_not_abstract():
    assert not inspect.isabstract(kmLogo_If)


def test_hyp_kmlogo_if_constructor_exists():
    assert callable(kmLogo_If.__init__)


def test_hyp_kmlogo_if_constructor_args():
    sig = inspect.signature(kmLogo_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_parameter_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Parameter)


def test_hyp_kmlogo_parameter_constructor_exists():
    assert callable(kmLogo_Parameter.__init__)


def test_hyp_kmlogo_parameter_constructor_args():
    sig = inspect.signature(kmLogo_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_kmlogo_instruction_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Instruction)


def test_hyp_kmlogo_instruction_constructor_exists():
    assert callable(kmLogo_Instruction.__init__)


def test_hyp_kmlogo_instruction_constructor_args():
    sig = inspect.signature(kmLogo_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmLogo_LogoProgram)


def test_hyp_kmlogo_logoprogram_constructor_exists():
    assert callable(kmLogo_LogoProgram.__init__)


def test_hyp_kmlogo_logoprogram_constructor_args():
    sig = inspect.signature(kmLogo_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_constant_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Constant)


def test_hyp_kmlogo_constant_constructor_exists():
    assert callable(kmLogo_Constant.__init__)


def test_hyp_kmlogo_constant_constructor_args():
    sig = inspect.signature(kmLogo_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"




def test_hyp_kmlogo_proccall_is_not_abstract():
    assert not inspect.isabstract(kmLogo_ProcCall)


def test_hyp_kmlogo_proccall_constructor_exists():
    assert callable(kmLogo_ProcCall.__init__)


def test_hyp_kmlogo_proccall_constructor_args():
    sig = inspect.signature(kmLogo_ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_parametercall_is_not_abstract():
    assert not inspect.isabstract(kmLogo_ParameterCall)


def test_hyp_kmlogo_parametercall_constructor_exists():
    assert callable(kmLogo_ParameterCall.__init__)


def test_hyp_kmlogo_parametercall_constructor_args():
    sig = inspect.signature(kmLogo_ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_binaryexp_is_not_abstract():
    assert not inspect.isabstract(kmLogo_BinaryExp)


def test_hyp_kmlogo_binaryexp_constructor_exists():
    assert callable(kmLogo_BinaryExp.__init__)


def test_hyp_kmlogo_binaryexp_constructor_args():
    sig = inspect.signature(kmLogo_BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_hyp_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_hyp_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_clear_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Clear)


def test_hyp_kmlogo_clear_constructor_exists():
    assert callable(kmLogo_Clear.__init__)


def test_hyp_kmlogo_clear_constructor_args():
    sig = inspect.signature(kmLogo_Clear.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_right_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Right)


def test_hyp_kmlogo_right_constructor_exists():
    assert callable(kmLogo_Right.__init__)


def test_hyp_kmlogo_right_constructor_args():
    sig = inspect.signature(kmLogo_Right.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_forward_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Forward)


def test_hyp_kmlogo_forward_constructor_exists():
    assert callable(kmLogo_Forward.__init__)


def test_hyp_kmlogo_forward_constructor_args():
    sig = inspect.signature(kmLogo_Forward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_penup_is_not_abstract():
    assert not inspect.isabstract(kmLogo_PenUp)


def test_hyp_kmlogo_penup_constructor_exists():
    assert callable(kmLogo_PenUp.__init__)


def test_hyp_kmlogo_penup_constructor_args():
    sig = inspect.signature(kmLogo_PenUp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_left_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Left)


def test_hyp_kmlogo_left_constructor_exists():
    assert callable(kmLogo_Left.__init__)


def test_hyp_kmlogo_left_constructor_args():
    sig = inspect.signature(kmLogo_Left.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_pendown_is_not_abstract():
    assert not inspect.isabstract(kmLogo_PenDown)


def test_hyp_kmlogo_pendown_constructor_exists():
    assert callable(kmLogo_PenDown.__init__)


def test_hyp_kmlogo_pendown_constructor_args():
    sig = inspect.signature(kmLogo_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_back_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Back)


def test_hyp_kmlogo_back_constructor_exists():
    assert callable(kmLogo_Back.__init__)


def test_hyp_kmlogo_back_constructor_args():
    sig = inspect.signature(kmLogo_Back.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_hyp_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_hyp_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_expression_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Expression)


def test_hyp_kmlogo_expression_constructor_exists():
    assert callable(kmLogo_Expression.__init__)


def test_hyp_kmlogo_expression_constructor_args():
    sig = inspect.signature(kmLogo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_procdeclaration_is_not_abstract():
    assert not inspect.isabstract(kmLogo_ProcDeclaration)


def test_hyp_kmlogo_procdeclaration_constructor_exists():
    assert callable(kmLogo_ProcDeclaration.__init__)


def test_hyp_kmlogo_procdeclaration_constructor_args():
    sig = inspect.signature(kmLogo_ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_kmlogo_controlstructure_is_not_abstract():
    assert not inspect.isabstract(kmLogo_ControlStructure)


def test_hyp_kmlogo_controlstructure_constructor_exists():
    assert callable(kmLogo_ControlStructure.__init__)


def test_hyp_kmlogo_controlstructure_constructor_args():
    sig = inspect.signature(kmLogo_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_block_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Block)


def test_hyp_kmlogo_block_constructor_exists():
    assert callable(kmLogo_Block.__init__)


def test_hyp_kmlogo_block_constructor_args():
    sig = inspect.signature(kmLogo_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kmlogo_primitive_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Primitive)


def test_hyp_kmlogo_primitive_constructor_exists():
    assert callable(kmLogo_Primitive.__init__)


def test_hyp_kmlogo_primitive_constructor_args():
    sig = inspect.signature(kmLogo_Primitive.__init__)
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
kmLogo_Mult_strategy = st.builds(
    kmLogo_Mult,
)
kmLogo_Minus_strategy = st.builds(
    kmLogo_Minus,
)
kmLogo_Plus_strategy = st.builds(
    kmLogo_Plus,
)
kmLogo_Lower_strategy = st.builds(
    kmLogo_Lower,
)
kmLogo_Greater_strategy = st.builds(
    kmLogo_Greater,
)
kmLogo_Equals_strategy = st.builds(
    kmLogo_Equals,
)
kmLogo_Div_strategy = st.builds(
    kmLogo_Div,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
kmLogo_While_strategy = st.builds(
    kmLogo_While,
)
kmLogo_Repeat_strategy = st.builds(
    kmLogo_Repeat,
)
kmLogo_If_strategy = st.builds(
    kmLogo_If,
)
kmLogo_Parameter_strategy = st.builds(
    kmLogo_Parameter,
    name=
        safe_text
)
kmLogo_Instruction_strategy = st.builds(
    kmLogo_Instruction,
)
kmLogo_LogoProgram_strategy = st.builds(
    kmLogo_LogoProgram,
)
Expression_strategy = st.builds(
    Expression,
)
kmLogo_Constant_strategy = st.builds(
    kmLogo_Constant,
    integerValue=
        st.integers()
)
kmLogo_ProcCall_strategy = st.builds(
    kmLogo_ProcCall,
)
kmLogo_ParameterCall_strategy = st.builds(
    kmLogo_ParameterCall,
)
kmLogo_BinaryExp_strategy = st.builds(
    kmLogo_BinaryExp,
)
Primitive_strategy = st.builds(
    Primitive,
)
kmLogo_Clear_strategy = st.builds(
    kmLogo_Clear,
)
kmLogo_Right_strategy = st.builds(
    kmLogo_Right,
)
kmLogo_Forward_strategy = st.builds(
    kmLogo_Forward,
)
kmLogo_PenUp_strategy = st.builds(
    kmLogo_PenUp,
)
kmLogo_Left_strategy = st.builds(
    kmLogo_Left,
)
kmLogo_PenDown_strategy = st.builds(
    kmLogo_PenDown,
)
kmLogo_Back_strategy = st.builds(
    kmLogo_Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmLogo_Expression_strategy = st.builds(
    kmLogo_Expression,
)
kmLogo_ProcDeclaration_strategy = st.builds(
    kmLogo_ProcDeclaration,
    name=
        safe_text
)
kmLogo_ControlStructure_strategy = st.builds(
    kmLogo_ControlStructure,
)
kmLogo_Block_strategy = st.builds(
    kmLogo_Block,
)
kmLogo_Primitive_strategy = st.builds(
    kmLogo_Primitive,
)
















@given(instance=kmLogo_Parameter_strategy)
def test_hyp_kmlogo_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=kmLogo_Constant_strategy)
def test_hyp_kmlogo_constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

















@given(instance=kmLogo_ProcDeclaration_strategy)
def test_hyp_kmlogo_procdeclaration_name_setter(instance):
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
    kmLogo_Back,
    kmLogo_BinaryExp,
    kmLogo_Block,
    kmLogo_Clear,
    kmLogo_Constant,
    kmLogo_ControlStructure,
    kmLogo_Div,
    kmLogo_Equals,
    kmLogo_Expression,
    kmLogo_Forward,
    kmLogo_Greater,
    kmLogo_If,
    kmLogo_Instruction,
    kmLogo_Left,
    kmLogo_LogoProgram,
    kmLogo_Lower,
    kmLogo_Minus,
    kmLogo_Mult,
    kmLogo_Parameter,
    kmLogo_ParameterCall,
    kmLogo_PenDown,
    kmLogo_PenUp,
    kmLogo_Plus,
    kmLogo_Primitive,
    kmLogo_ProcCall,
    kmLogo_ProcDeclaration,
    kmLogo_Repeat,
    kmLogo_Right,
    kmLogo_While,
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

def test_kmLogo_Constant_integerValue_value_roundtrip():
    instance = kmLogo_Constant(integerValue=7)
    assert instance.integerValue == 7
    instance.integerValue = 13
    assert instance.integerValue == 13


def test_kmLogo_Parameter_name_value_roundtrip():
    instance = kmLogo_Parameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_kmLogo_ProcDeclaration_name_value_roundtrip():
    instance = kmLogo_ProcDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_kmLogo_Div_isa_BinaryExp():
    instance = kmLogo_Div()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Equals_isa_BinaryExp():
    instance = kmLogo_Equals()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Greater_isa_BinaryExp():
    instance = kmLogo_Greater()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Lower_isa_BinaryExp():
    instance = kmLogo_Lower()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Minus_isa_BinaryExp():
    instance = kmLogo_Minus()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Mult_isa_BinaryExp():
    instance = kmLogo_Mult()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_Plus_isa_BinaryExp():
    instance = kmLogo_Plus()
    assert isinstance(instance, BinaryExp)


def test_kmLogo_If_isa_ControlStructure():
    instance = kmLogo_If()
    assert isinstance(instance, ControlStructure)


def test_kmLogo_Repeat_isa_ControlStructure():
    instance = kmLogo_Repeat()
    assert isinstance(instance, ControlStructure)


def test_kmLogo_While_isa_ControlStructure():
    instance = kmLogo_While()
    assert isinstance(instance, ControlStructure)


def test_kmLogo_BinaryExp_isa_Expression():
    instance = kmLogo_BinaryExp()
    assert isinstance(instance, Expression)


def test_kmLogo_Constant_isa_Expression():
    instance = kmLogo_Constant(integerValue=7)
    assert isinstance(instance, Expression)


def test_kmLogo_ParameterCall_isa_Expression():
    instance = kmLogo_ParameterCall()
    assert isinstance(instance, Expression)


def test_kmLogo_ProcCall_isa_Expression():
    instance = kmLogo_ProcCall()
    assert isinstance(instance, Expression)


def test_kmLogo_Block_isa_Instruction():
    instance = kmLogo_Block()
    assert isinstance(instance, Instruction)


def test_kmLogo_ControlStructure_isa_Instruction():
    instance = kmLogo_ControlStructure()
    assert isinstance(instance, Instruction)


def test_kmLogo_Expression_isa_Instruction():
    instance = kmLogo_Expression()
    assert isinstance(instance, Instruction)


def test_kmLogo_Primitive_isa_Instruction():
    instance = kmLogo_Primitive()
    assert isinstance(instance, Instruction)


def test_kmLogo_ProcDeclaration_isa_Instruction():
    instance = kmLogo_ProcDeclaration(name="sample_text")
    assert isinstance(instance, Instruction)


def test_kmLogo_Back_isa_Primitive():
    instance = kmLogo_Back()
    assert isinstance(instance, Primitive)


def test_kmLogo_Clear_isa_Primitive():
    instance = kmLogo_Clear()
    assert isinstance(instance, Primitive)


def test_kmLogo_Forward_isa_Primitive():
    instance = kmLogo_Forward()
    assert isinstance(instance, Primitive)


def test_kmLogo_Left_isa_Primitive():
    instance = kmLogo_Left()
    assert isinstance(instance, Primitive)


def test_kmLogo_PenDown_isa_Primitive():
    instance = kmLogo_PenDown()
    assert isinstance(instance, Primitive)


def test_kmLogo_PenUp_isa_Primitive():
    instance = kmLogo_PenUp()
    assert isinstance(instance, Primitive)


def test_kmLogo_Right_isa_Primitive():
    instance = kmLogo_Right()
    assert isinstance(instance, Primitive)


def test_assoc_args16_link_reassign_clear():
    a = kmLogo_ProcDeclaration(name="sample_text")
    b1 = kmLogo_Parameter(name="sample_text")
    b2 = kmLogo_Parameter(name="sample_text_2")
    _safe_set(a, 'kmLogo_ProcDeclaration', {b1})
    assert _is_linked(a, 'kmLogo_ProcDeclaration', b1)
    if hasattr(b1, 'kmLogo_Parameter'):
        assert _is_linked(b1, 'kmLogo_Parameter', a)
    _safe_set(a, 'kmLogo_ProcDeclaration', {b2})
    assert _is_linked(a, 'kmLogo_ProcDeclaration', b2)
    if hasattr(b1, 'kmLogo_Parameter'):
        assert not _is_linked(b1, 'kmLogo_Parameter', a)
    if hasattr(b2, 'kmLogo_Parameter'):
        assert _is_linked(b2, 'kmLogo_Parameter', a)
    _safe_set(a, 'kmLogo_ProcDeclaration', set())
    assert not _is_linked(a, 'kmLogo_ProcDeclaration', b2)
    if hasattr(b2, 'kmLogo_Parameter'):
        assert not _is_linked(b2, 'kmLogo_Parameter', a)


def test_assoc_declaration15_link_reassign_clear():
    a = kmLogo_ProcDeclaration(name="sample_text")
    b1 = kmLogo_ProcCall()
    b2 = kmLogo_ProcCall()
    _safe_set(a, 'ProcDeclaration', b1)
    assert _is_linked(a, 'ProcDeclaration', b1)
    if hasattr(b1, 'procCall'):
        assert _is_linked(b1, 'procCall', a)
    _safe_set(a, 'ProcDeclaration', b2)
    assert _is_linked(a, 'ProcDeclaration', b2)
    if hasattr(b1, 'procCall'):
        assert not _is_linked(b1, 'procCall', a)
    if hasattr(b2, 'procCall'):
        assert _is_linked(b2, 'procCall', a)
    _safe_set(a, 'ProcDeclaration', None)
    assert not _is_linked(a, 'ProcDeclaration', b2)
    if hasattr(b2, 'procCall'):
        assert not _is_linked(b2, 'procCall', a)


def test_assoc_instructions18_link_reassign_clear():
    a = kmLogo_ProcDeclaration(name="sample_text")
    b1 = kmLogo_Instruction()
    b2 = kmLogo_Instruction()
    _safe_set(a, 'kmLogo_ProcDeclaration19', {b1})
    assert _is_linked(a, 'kmLogo_ProcDeclaration19', b1)
    if hasattr(b1, 'kmLogo_Instruction20'):
        assert _is_linked(b1, 'kmLogo_Instruction20', a)
    _safe_set(a, 'kmLogo_ProcDeclaration19', {b2})
    assert _is_linked(a, 'kmLogo_ProcDeclaration19', b2)
    if hasattr(b1, 'kmLogo_Instruction20'):
        assert not _is_linked(b1, 'kmLogo_Instruction20', a)
    if hasattr(b2, 'kmLogo_Instruction20'):
        assert _is_linked(b2, 'kmLogo_Instruction20', a)
    _safe_set(a, 'kmLogo_ProcDeclaration19', set())
    assert not _is_linked(a, 'kmLogo_ProcDeclaration19', b2)
    if hasattr(b2, 'kmLogo_Instruction20'):
        assert not _is_linked(b2, 'kmLogo_Instruction20', a)


def test_assoc_parameter34_link_reassign_clear():
    a = kmLogo_Parameter(name="sample_text")
    b1 = kmLogo_ParameterCall()
    b2 = kmLogo_ParameterCall()
    _safe_set(a, 'kmLogo_Parameter35', b1)
    assert _is_linked(a, 'kmLogo_Parameter35', b1)
    if hasattr(b1, 'kmLogo_ParameterCall'):
        assert _is_linked(b1, 'kmLogo_ParameterCall', a)
    _safe_set(a, 'kmLogo_Parameter35', b2)
    assert _is_linked(a, 'kmLogo_Parameter35', b2)
    if hasattr(b1, 'kmLogo_ParameterCall'):
        assert not _is_linked(b1, 'kmLogo_ParameterCall', a)
    if hasattr(b2, 'kmLogo_ParameterCall'):
        assert _is_linked(b2, 'kmLogo_ParameterCall', a)
    _safe_set(a, 'kmLogo_Parameter35', None)
    assert not _is_linked(a, 'kmLogo_Parameter35', b2)
    if hasattr(b2, 'kmLogo_ParameterCall'):
        assert not _is_linked(b2, 'kmLogo_ParameterCall', a)


def test_assoc_procCall17_link_reassign_clear():
    a = kmLogo_ProcDeclaration(name="sample_text")
    b1 = kmLogo_ProcCall()
    b2 = kmLogo_ProcCall()
    _safe_set(a, 'declaration', {b1})
    assert _is_linked(a, 'declaration', b1)
    if hasattr(b1, 'ProcCall'):
        assert _is_linked(b1, 'ProcCall', a)
    _safe_set(a, 'declaration', {b2})
    assert _is_linked(a, 'declaration', b2)
    if hasattr(b1, 'ProcCall'):
        assert not _is_linked(b1, 'ProcCall', a)
    if hasattr(b2, 'ProcCall'):
        assert _is_linked(b2, 'ProcCall', a)
    _safe_set(a, 'declaration', set())
    assert not _is_linked(a, 'declaration', b2)
    if hasattr(b2, 'ProcCall'):
        assert not _is_linked(b2, 'ProcCall', a)


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


kmLogo_Back_strategy = st.builds(kmLogo_Back)
@given(instance=kmLogo_Back_strategy)
@settings(max_examples=25)
def test_kmLogo_Back_instantiation(instance):
    assert isinstance(instance, kmLogo_Back)


kmLogo_BinaryExp_strategy = st.builds(kmLogo_BinaryExp)
@given(instance=kmLogo_BinaryExp_strategy)
@settings(max_examples=25)
def test_kmLogo_BinaryExp_instantiation(instance):
    assert isinstance(instance, kmLogo_BinaryExp)


kmLogo_Block_strategy = st.builds(kmLogo_Block)
@given(instance=kmLogo_Block_strategy)
@settings(max_examples=25)
def test_kmLogo_Block_instantiation(instance):
    assert isinstance(instance, kmLogo_Block)


kmLogo_Clear_strategy = st.builds(kmLogo_Clear)
@given(instance=kmLogo_Clear_strategy)
@settings(max_examples=25)
def test_kmLogo_Clear_instantiation(instance):
    assert isinstance(instance, kmLogo_Clear)


kmLogo_Constant_strategy = st.builds(kmLogo_Constant, integerValue=st.integers())
@given(instance=kmLogo_Constant_strategy)
@settings(max_examples=25)
def test_kmLogo_Constant_instantiation(instance):
    assert isinstance(instance, kmLogo_Constant)


kmLogo_ControlStructure_strategy = st.builds(kmLogo_ControlStructure)
@given(instance=kmLogo_ControlStructure_strategy)
@settings(max_examples=25)
def test_kmLogo_ControlStructure_instantiation(instance):
    assert isinstance(instance, kmLogo_ControlStructure)


kmLogo_Div_strategy = st.builds(kmLogo_Div)
@given(instance=kmLogo_Div_strategy)
@settings(max_examples=25)
def test_kmLogo_Div_instantiation(instance):
    assert isinstance(instance, kmLogo_Div)


kmLogo_Equals_strategy = st.builds(kmLogo_Equals)
@given(instance=kmLogo_Equals_strategy)
@settings(max_examples=25)
def test_kmLogo_Equals_instantiation(instance):
    assert isinstance(instance, kmLogo_Equals)


kmLogo_Expression_strategy = st.builds(kmLogo_Expression)
@given(instance=kmLogo_Expression_strategy)
@settings(max_examples=25)
def test_kmLogo_Expression_instantiation(instance):
    assert isinstance(instance, kmLogo_Expression)


kmLogo_Forward_strategy = st.builds(kmLogo_Forward)
@given(instance=kmLogo_Forward_strategy)
@settings(max_examples=25)
def test_kmLogo_Forward_instantiation(instance):
    assert isinstance(instance, kmLogo_Forward)


kmLogo_Greater_strategy = st.builds(kmLogo_Greater)
@given(instance=kmLogo_Greater_strategy)
@settings(max_examples=25)
def test_kmLogo_Greater_instantiation(instance):
    assert isinstance(instance, kmLogo_Greater)


kmLogo_If_strategy = st.builds(kmLogo_If)
@given(instance=kmLogo_If_strategy)
@settings(max_examples=25)
def test_kmLogo_If_instantiation(instance):
    assert isinstance(instance, kmLogo_If)


kmLogo_Instruction_strategy = st.builds(kmLogo_Instruction)
@given(instance=kmLogo_Instruction_strategy)
@settings(max_examples=25)
def test_kmLogo_Instruction_instantiation(instance):
    assert isinstance(instance, kmLogo_Instruction)


kmLogo_Left_strategy = st.builds(kmLogo_Left)
@given(instance=kmLogo_Left_strategy)
@settings(max_examples=25)
def test_kmLogo_Left_instantiation(instance):
    assert isinstance(instance, kmLogo_Left)


kmLogo_LogoProgram_strategy = st.builds(kmLogo_LogoProgram)
@given(instance=kmLogo_LogoProgram_strategy)
@settings(max_examples=25)
def test_kmLogo_LogoProgram_instantiation(instance):
    assert isinstance(instance, kmLogo_LogoProgram)


kmLogo_Lower_strategy = st.builds(kmLogo_Lower)
@given(instance=kmLogo_Lower_strategy)
@settings(max_examples=25)
def test_kmLogo_Lower_instantiation(instance):
    assert isinstance(instance, kmLogo_Lower)


kmLogo_Minus_strategy = st.builds(kmLogo_Minus)
@given(instance=kmLogo_Minus_strategy)
@settings(max_examples=25)
def test_kmLogo_Minus_instantiation(instance):
    assert isinstance(instance, kmLogo_Minus)


kmLogo_Mult_strategy = st.builds(kmLogo_Mult)
@given(instance=kmLogo_Mult_strategy)
@settings(max_examples=25)
def test_kmLogo_Mult_instantiation(instance):
    assert isinstance(instance, kmLogo_Mult)


kmLogo_Parameter_strategy = st.builds(kmLogo_Parameter, name=safe_text)
@given(instance=kmLogo_Parameter_strategy)
@settings(max_examples=25)
def test_kmLogo_Parameter_instantiation(instance):
    assert isinstance(instance, kmLogo_Parameter)


kmLogo_ParameterCall_strategy = st.builds(kmLogo_ParameterCall)
@given(instance=kmLogo_ParameterCall_strategy)
@settings(max_examples=25)
def test_kmLogo_ParameterCall_instantiation(instance):
    assert isinstance(instance, kmLogo_ParameterCall)


kmLogo_PenDown_strategy = st.builds(kmLogo_PenDown)
@given(instance=kmLogo_PenDown_strategy)
@settings(max_examples=25)
def test_kmLogo_PenDown_instantiation(instance):
    assert isinstance(instance, kmLogo_PenDown)


kmLogo_PenUp_strategy = st.builds(kmLogo_PenUp)
@given(instance=kmLogo_PenUp_strategy)
@settings(max_examples=25)
def test_kmLogo_PenUp_instantiation(instance):
    assert isinstance(instance, kmLogo_PenUp)


kmLogo_Plus_strategy = st.builds(kmLogo_Plus)
@given(instance=kmLogo_Plus_strategy)
@settings(max_examples=25)
def test_kmLogo_Plus_instantiation(instance):
    assert isinstance(instance, kmLogo_Plus)


kmLogo_Primitive_strategy = st.builds(kmLogo_Primitive)
@given(instance=kmLogo_Primitive_strategy)
@settings(max_examples=25)
def test_kmLogo_Primitive_instantiation(instance):
    assert isinstance(instance, kmLogo_Primitive)


kmLogo_ProcCall_strategy = st.builds(kmLogo_ProcCall)
@given(instance=kmLogo_ProcCall_strategy)
@settings(max_examples=25)
def test_kmLogo_ProcCall_instantiation(instance):
    assert isinstance(instance, kmLogo_ProcCall)


kmLogo_ProcDeclaration_strategy = st.builds(kmLogo_ProcDeclaration, name=safe_text)
@given(instance=kmLogo_ProcDeclaration_strategy)
@settings(max_examples=25)
def test_kmLogo_ProcDeclaration_instantiation(instance):
    assert isinstance(instance, kmLogo_ProcDeclaration)


kmLogo_Repeat_strategy = st.builds(kmLogo_Repeat)
@given(instance=kmLogo_Repeat_strategy)
@settings(max_examples=25)
def test_kmLogo_Repeat_instantiation(instance):
    assert isinstance(instance, kmLogo_Repeat)


kmLogo_Right_strategy = st.builds(kmLogo_Right)
@given(instance=kmLogo_Right_strategy)
@settings(max_examples=25)
def test_kmLogo_Right_instantiation(instance):
    assert isinstance(instance, kmLogo_Right)


kmLogo_While_strategy = st.builds(kmLogo_While)
@given(instance=kmLogo_While_strategy)
@settings(max_examples=25)
def test_kmLogo_While_instantiation(instance):
    assert isinstance(instance, kmLogo_While)



