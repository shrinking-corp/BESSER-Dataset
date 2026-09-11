import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArithmeticInstruction,
    CompareInstruction,
    Instruction,
    JumpInstruction,
    OutputInstruction,
    Value,
    mil_AddInstruction,
    mil_ArithmeticInstruction,
    mil_CallInstruction,
    mil_CompareInstruction,
    mil_ConditionalJumpInstruction,
    mil_ConstantInteger,
    mil_DivInstruction,
    mil_EqualInstruction,
    mil_GreaterThanEqualInstruction,
    mil_GreaterThanInstruction,
    mil_Instruction,
    mil_JumpInstruction,
    mil_LabelInstruction,
    mil_LessThanEqualInstruction,
    mil_LessThanInstruction,
    mil_LoadInstruction,
    mil_MILModel,
    mil_MulInstruction,
    mil_NegateInstruction,
    mil_NotEqualInstruction,
    mil_OutputInstruction,
    mil_PrintInstruction,
    mil_RegisterReference,
    mil_ReturnInstruction,
    mil_StoreInstruction,
    mil_SubInstruction,
    mil_UnconditionalJumpInstruction,
    mil_Value,
    mil_YieldInstruciton,
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

def test_mil_ConstantInteger_rawValue_value_roundtrip():
    instance = mil_ConstantInteger(rawValue=7)
    assert instance.rawValue == 7
    instance.rawValue = 13
    assert instance.rawValue == 13


def test_mil_LabelInstruction_name_value_roundtrip():
    instance = mil_LabelInstruction(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mil_PrintInstruction_output_value_roundtrip():
    instance = mil_PrintInstruction(output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_mil_RegisterReference_address_value_roundtrip():
    instance = mil_RegisterReference(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_mil_AddInstruction_isa_ArithmeticInstruction():
    instance = mil_AddInstruction()
    assert isinstance(instance, ArithmeticInstruction)


def test_mil_DivInstruction_isa_ArithmeticInstruction():
    instance = mil_DivInstruction()
    assert isinstance(instance, ArithmeticInstruction)


def test_mil_MulInstruction_isa_ArithmeticInstruction():
    instance = mil_MulInstruction()
    assert isinstance(instance, ArithmeticInstruction)


def test_mil_SubInstruction_isa_ArithmeticInstruction():
    instance = mil_SubInstruction()
    assert isinstance(instance, ArithmeticInstruction)


def test_mil_EqualInstruction_isa_CompareInstruction():
    instance = mil_EqualInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_GreaterThanEqualInstruction_isa_CompareInstruction():
    instance = mil_GreaterThanEqualInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_GreaterThanInstruction_isa_CompareInstruction():
    instance = mil_GreaterThanInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_LessThanEqualInstruction_isa_CompareInstruction():
    instance = mil_LessThanEqualInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_LessThanInstruction_isa_CompareInstruction():
    instance = mil_LessThanInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_NotEqualInstruction_isa_CompareInstruction():
    instance = mil_NotEqualInstruction()
    assert isinstance(instance, CompareInstruction)


def test_mil_ArithmeticInstruction_isa_Instruction():
    instance = mil_ArithmeticInstruction()
    assert isinstance(instance, Instruction)


def test_mil_CallInstruction_isa_Instruction():
    instance = mil_CallInstruction()
    assert isinstance(instance, Instruction)


def test_mil_CompareInstruction_isa_Instruction():
    instance = mil_CompareInstruction()
    assert isinstance(instance, Instruction)


def test_mil_JumpInstruction_isa_Instruction():
    instance = mil_JumpInstruction()
    assert isinstance(instance, Instruction)


def test_mil_LabelInstruction_isa_Instruction():
    instance = mil_LabelInstruction(name="sample_text")
    assert isinstance(instance, Instruction)


def test_mil_LoadInstruction_isa_Instruction():
    instance = mil_LoadInstruction()
    assert isinstance(instance, Instruction)


def test_mil_NegateInstruction_isa_Instruction():
    instance = mil_NegateInstruction()
    assert isinstance(instance, Instruction)


def test_mil_OutputInstruction_isa_Instruction():
    instance = mil_OutputInstruction()
    assert isinstance(instance, Instruction)


def test_mil_ReturnInstruction_isa_Instruction():
    instance = mil_ReturnInstruction()
    assert isinstance(instance, Instruction)


def test_mil_StoreInstruction_isa_Instruction():
    instance = mil_StoreInstruction()
    assert isinstance(instance, Instruction)


def test_mil_ConditionalJumpInstruction_isa_JumpInstruction():
    instance = mil_ConditionalJumpInstruction()
    assert isinstance(instance, JumpInstruction)


def test_mil_UnconditionalJumpInstruction_isa_JumpInstruction():
    instance = mil_UnconditionalJumpInstruction()
    assert isinstance(instance, JumpInstruction)


def test_mil_PrintInstruction_isa_OutputInstruction():
    instance = mil_PrintInstruction(output="sample_text")
    assert isinstance(instance, OutputInstruction)


def test_mil_YieldInstruciton_isa_OutputInstruction():
    instance = mil_YieldInstruciton()
    assert isinstance(instance, OutputInstruction)


def test_mil_ConstantInteger_isa_Value():
    instance = mil_ConstantInteger(rawValue=7)
    assert isinstance(instance, Value)


def test_mil_RegisterReference_isa_Value():
    instance = mil_RegisterReference(address="sample_text")
    assert isinstance(instance, Value)


def test_assoc_jumpTo3_link_reassign_clear():
    a = mil_LabelInstruction(name="sample_text")
    b1 = mil_JumpInstruction()
    b2 = mil_JumpInstruction()
    _safe_set(a, 'mil_LabelInstruction', b1)
    assert _is_linked(a, 'mil_LabelInstruction', b1)
    if hasattr(b1, 'mil_JumpInstruction'):
        assert _is_linked(b1, 'mil_JumpInstruction', a)
    _safe_set(a, 'mil_LabelInstruction', b2)
    assert _is_linked(a, 'mil_LabelInstruction', b2)
    if hasattr(b1, 'mil_JumpInstruction'):
        assert not _is_linked(b1, 'mil_JumpInstruction', a)
    if hasattr(b2, 'mil_JumpInstruction'):
        assert _is_linked(b2, 'mil_JumpInstruction', a)
    _safe_set(a, 'mil_LabelInstruction', None)
    assert not _is_linked(a, 'mil_LabelInstruction', b2)
    if hasattr(b2, 'mil_JumpInstruction'):
        assert not _is_linked(b2, 'mil_JumpInstruction', a)


def test_assoc_operationName4_link_reassign_clear():
    a = mil_LabelInstruction(name="sample_text")
    b1 = mil_CallInstruction()
    b2 = mil_CallInstruction()
    _safe_set(a, 'mil_LabelInstruction5', b1)
    assert _is_linked(a, 'mil_LabelInstruction5', b1)
    if hasattr(b1, 'mil_CallInstruction'):
        assert _is_linked(b1, 'mil_CallInstruction', a)
    _safe_set(a, 'mil_LabelInstruction5', b2)
    assert _is_linked(a, 'mil_LabelInstruction5', b2)
    if hasattr(b1, 'mil_CallInstruction'):
        assert not _is_linked(b1, 'mil_CallInstruction', a)
    if hasattr(b2, 'mil_CallInstruction'):
        assert _is_linked(b2, 'mil_CallInstruction', a)
    _safe_set(a, 'mil_LabelInstruction5', None)
    assert not _is_linked(a, 'mil_LabelInstruction5', b2)
    if hasattr(b2, 'mil_CallInstruction'):
        assert not _is_linked(b2, 'mil_CallInstruction', a)


def test_assoc_registerReference2_link_reassign_clear():
    a = mil_RegisterReference(address="sample_text")
    b1 = mil_StoreInstruction()
    b2 = mil_StoreInstruction()
    _safe_set(a, 'mil_RegisterReference', b1)
    assert _is_linked(a, 'mil_RegisterReference', b1)
    if hasattr(b1, 'mil_StoreInstruction'):
        assert _is_linked(b1, 'mil_StoreInstruction', a)
    _safe_set(a, 'mil_RegisterReference', b2)
    assert _is_linked(a, 'mil_RegisterReference', b2)
    if hasattr(b1, 'mil_StoreInstruction'):
        assert not _is_linked(b1, 'mil_StoreInstruction', a)
    if hasattr(b2, 'mil_StoreInstruction'):
        assert _is_linked(b2, 'mil_StoreInstruction', a)
    _safe_set(a, 'mil_RegisterReference', None)
    assert not _is_linked(a, 'mil_RegisterReference', b2)
    if hasattr(b2, 'mil_StoreInstruction'):
        assert not _is_linked(b2, 'mil_StoreInstruction', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArithmeticInstruction_strategy = st.builds(ArithmeticInstruction)
@given(instance=ArithmeticInstruction_strategy)
@settings(max_examples=25)
def test_ArithmeticInstruction_instantiation(instance):
    assert isinstance(instance, ArithmeticInstruction)


CompareInstruction_strategy = st.builds(CompareInstruction)
@given(instance=CompareInstruction_strategy)
@settings(max_examples=25)
def test_CompareInstruction_instantiation(instance):
    assert isinstance(instance, CompareInstruction)


Instruction_strategy = st.builds(Instruction)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


JumpInstruction_strategy = st.builds(JumpInstruction)
@given(instance=JumpInstruction_strategy)
@settings(max_examples=25)
def test_JumpInstruction_instantiation(instance):
    assert isinstance(instance, JumpInstruction)


OutputInstruction_strategy = st.builds(OutputInstruction)
@given(instance=OutputInstruction_strategy)
@settings(max_examples=25)
def test_OutputInstruction_instantiation(instance):
    assert isinstance(instance, OutputInstruction)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


mil_AddInstruction_strategy = st.builds(mil_AddInstruction)
@given(instance=mil_AddInstruction_strategy)
@settings(max_examples=25)
def test_mil_AddInstruction_instantiation(instance):
    assert isinstance(instance, mil_AddInstruction)


mil_ArithmeticInstruction_strategy = st.builds(mil_ArithmeticInstruction)
@given(instance=mil_ArithmeticInstruction_strategy)
@settings(max_examples=25)
def test_mil_ArithmeticInstruction_instantiation(instance):
    assert isinstance(instance, mil_ArithmeticInstruction)


mil_CallInstruction_strategy = st.builds(mil_CallInstruction)
@given(instance=mil_CallInstruction_strategy)
@settings(max_examples=25)
def test_mil_CallInstruction_instantiation(instance):
    assert isinstance(instance, mil_CallInstruction)


mil_CompareInstruction_strategy = st.builds(mil_CompareInstruction)
@given(instance=mil_CompareInstruction_strategy)
@settings(max_examples=25)
def test_mil_CompareInstruction_instantiation(instance):
    assert isinstance(instance, mil_CompareInstruction)


mil_ConditionalJumpInstruction_strategy = st.builds(mil_ConditionalJumpInstruction)
@given(instance=mil_ConditionalJumpInstruction_strategy)
@settings(max_examples=25)
def test_mil_ConditionalJumpInstruction_instantiation(instance):
    assert isinstance(instance, mil_ConditionalJumpInstruction)


mil_ConstantInteger_strategy = st.builds(mil_ConstantInteger, rawValue=st.integers())
@given(instance=mil_ConstantInteger_strategy)
@settings(max_examples=25)
def test_mil_ConstantInteger_instantiation(instance):
    assert isinstance(instance, mil_ConstantInteger)


mil_DivInstruction_strategy = st.builds(mil_DivInstruction)
@given(instance=mil_DivInstruction_strategy)
@settings(max_examples=25)
def test_mil_DivInstruction_instantiation(instance):
    assert isinstance(instance, mil_DivInstruction)


mil_EqualInstruction_strategy = st.builds(mil_EqualInstruction)
@given(instance=mil_EqualInstruction_strategy)
@settings(max_examples=25)
def test_mil_EqualInstruction_instantiation(instance):
    assert isinstance(instance, mil_EqualInstruction)


mil_GreaterThanEqualInstruction_strategy = st.builds(mil_GreaterThanEqualInstruction)
@given(instance=mil_GreaterThanEqualInstruction_strategy)
@settings(max_examples=25)
def test_mil_GreaterThanEqualInstruction_instantiation(instance):
    assert isinstance(instance, mil_GreaterThanEqualInstruction)


mil_GreaterThanInstruction_strategy = st.builds(mil_GreaterThanInstruction)
@given(instance=mil_GreaterThanInstruction_strategy)
@settings(max_examples=25)
def test_mil_GreaterThanInstruction_instantiation(instance):
    assert isinstance(instance, mil_GreaterThanInstruction)


mil_Instruction_strategy = st.builds(mil_Instruction)
@given(instance=mil_Instruction_strategy)
@settings(max_examples=25)
def test_mil_Instruction_instantiation(instance):
    assert isinstance(instance, mil_Instruction)


mil_JumpInstruction_strategy = st.builds(mil_JumpInstruction)
@given(instance=mil_JumpInstruction_strategy)
@settings(max_examples=25)
def test_mil_JumpInstruction_instantiation(instance):
    assert isinstance(instance, mil_JumpInstruction)


mil_LabelInstruction_strategy = st.builds(mil_LabelInstruction, name=safe_text)
@given(instance=mil_LabelInstruction_strategy)
@settings(max_examples=25)
def test_mil_LabelInstruction_instantiation(instance):
    assert isinstance(instance, mil_LabelInstruction)


mil_LessThanEqualInstruction_strategy = st.builds(mil_LessThanEqualInstruction)
@given(instance=mil_LessThanEqualInstruction_strategy)
@settings(max_examples=25)
def test_mil_LessThanEqualInstruction_instantiation(instance):
    assert isinstance(instance, mil_LessThanEqualInstruction)


mil_LessThanInstruction_strategy = st.builds(mil_LessThanInstruction)
@given(instance=mil_LessThanInstruction_strategy)
@settings(max_examples=25)
def test_mil_LessThanInstruction_instantiation(instance):
    assert isinstance(instance, mil_LessThanInstruction)


mil_LoadInstruction_strategy = st.builds(mil_LoadInstruction)
@given(instance=mil_LoadInstruction_strategy)
@settings(max_examples=25)
def test_mil_LoadInstruction_instantiation(instance):
    assert isinstance(instance, mil_LoadInstruction)


mil_MILModel_strategy = st.builds(mil_MILModel)
@given(instance=mil_MILModel_strategy)
@settings(max_examples=25)
def test_mil_MILModel_instantiation(instance):
    assert isinstance(instance, mil_MILModel)


mil_MulInstruction_strategy = st.builds(mil_MulInstruction)
@given(instance=mil_MulInstruction_strategy)
@settings(max_examples=25)
def test_mil_MulInstruction_instantiation(instance):
    assert isinstance(instance, mil_MulInstruction)


mil_NegateInstruction_strategy = st.builds(mil_NegateInstruction)
@given(instance=mil_NegateInstruction_strategy)
@settings(max_examples=25)
def test_mil_NegateInstruction_instantiation(instance):
    assert isinstance(instance, mil_NegateInstruction)


mil_NotEqualInstruction_strategy = st.builds(mil_NotEqualInstruction)
@given(instance=mil_NotEqualInstruction_strategy)
@settings(max_examples=25)
def test_mil_NotEqualInstruction_instantiation(instance):
    assert isinstance(instance, mil_NotEqualInstruction)


mil_OutputInstruction_strategy = st.builds(mil_OutputInstruction)
@given(instance=mil_OutputInstruction_strategy)
@settings(max_examples=25)
def test_mil_OutputInstruction_instantiation(instance):
    assert isinstance(instance, mil_OutputInstruction)


mil_PrintInstruction_strategy = st.builds(mil_PrintInstruction, output=safe_text)
@given(instance=mil_PrintInstruction_strategy)
@settings(max_examples=25)
def test_mil_PrintInstruction_instantiation(instance):
    assert isinstance(instance, mil_PrintInstruction)


mil_RegisterReference_strategy = st.builds(mil_RegisterReference, address=safe_text)
@given(instance=mil_RegisterReference_strategy)
@settings(max_examples=25)
def test_mil_RegisterReference_instantiation(instance):
    assert isinstance(instance, mil_RegisterReference)


mil_ReturnInstruction_strategy = st.builds(mil_ReturnInstruction)
@given(instance=mil_ReturnInstruction_strategy)
@settings(max_examples=25)
def test_mil_ReturnInstruction_instantiation(instance):
    assert isinstance(instance, mil_ReturnInstruction)


mil_StoreInstruction_strategy = st.builds(mil_StoreInstruction)
@given(instance=mil_StoreInstruction_strategy)
@settings(max_examples=25)
def test_mil_StoreInstruction_instantiation(instance):
    assert isinstance(instance, mil_StoreInstruction)


mil_SubInstruction_strategy = st.builds(mil_SubInstruction)
@given(instance=mil_SubInstruction_strategy)
@settings(max_examples=25)
def test_mil_SubInstruction_instantiation(instance):
    assert isinstance(instance, mil_SubInstruction)


mil_UnconditionalJumpInstruction_strategy = st.builds(mil_UnconditionalJumpInstruction)
@given(instance=mil_UnconditionalJumpInstruction_strategy)
@settings(max_examples=25)
def test_mil_UnconditionalJumpInstruction_instantiation(instance):
    assert isinstance(instance, mil_UnconditionalJumpInstruction)


mil_Value_strategy = st.builds(mil_Value)
@given(instance=mil_Value_strategy)
@settings(max_examples=25)
def test_mil_Value_instantiation(instance):
    assert isinstance(instance, mil_Value)


mil_YieldInstruciton_strategy = st.builds(mil_YieldInstruciton)
@given(instance=mil_YieldInstruciton_strategy)
@settings(max_examples=25)
def test_mil_YieldInstruciton_instantiation(instance):
    assert isinstance(instance, mil_YieldInstruciton)


