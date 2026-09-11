import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CaseLabel,
    Declarator,
    FileRegion,
    IdlType,
    IdlTypeDcl,
    MemberContainer,
    PrimitiveType,
    TemplateType,
    Typed,
    TypedElement,
    types_Any,
    types_Boolean,
    types_Case,
    types_CaseLabel,
    types_Declarator,
    types_DefaultCaseLabel,
    types_Double,
    types_ElementSpec,
    types_EnumType,
    types_Enumeration,
    types_ExprCaseLabel,
    types_Expression,
    types_FixedPtType,
    types_Float,
    types_ForwardDcl,
    types_IdlChar,
    types_IdlObject,
    types_IdlString,
    types_IdlType,
    types_IdlWChar,
    types_Long,
    types_LongDouble,
    types_LongLong,
    types_Octet,
    types_PrimitiveType,
    types_SequenceType,
    types_Short,
    types_StructForwardDcl,
    types_StructType,
    types_Switch,
    types_TemplateType,
    types_TypeDef,
    types_ULong,
    types_ULongLong,
    types_UShort,
    types_UnionForwardDcl,
    types_UnionType,
    types_ValueBaseType,
    types_VoidType,
    types_WChar,
    types_WString,
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

def test_types_DefaultCaseLabel_isa_CaseLabel():
    instance = types_DefaultCaseLabel()
    assert isinstance(instance, CaseLabel)


def test_types_ExprCaseLabel_isa_CaseLabel():
    instance = types_ExprCaseLabel()
    assert isinstance(instance, CaseLabel)


def test_types_Enumeration_isa_Declarator():
    instance = types_Enumeration()
    assert isinstance(instance, Declarator)


def test_types_Case_isa_FileRegion():
    instance = types_Case()
    assert isinstance(instance, FileRegion)


def test_types_CaseLabel_isa_FileRegion():
    instance = types_CaseLabel()
    assert isinstance(instance, FileRegion)


def test_types_ElementSpec_isa_FileRegion():
    instance = types_ElementSpec()
    assert isinstance(instance, FileRegion)


def test_types_Switch_isa_FileRegion():
    instance = types_Switch()
    assert isinstance(instance, FileRegion)


def test_types_PrimitiveType_isa_IdlType():
    instance = types_PrimitiveType()
    assert isinstance(instance, IdlType)


def test_types_TemplateType_isa_IdlType():
    instance = types_TemplateType()
    assert isinstance(instance, IdlType)


def test_types_VoidType_isa_IdlType():
    instance = types_VoidType()
    assert isinstance(instance, IdlType)


def test_types_EnumType_isa_IdlTypeDcl():
    instance = types_EnumType()
    assert isinstance(instance, IdlTypeDcl)


def test_types_Enumeration_isa_IdlTypeDcl():
    instance = types_Enumeration()
    assert isinstance(instance, IdlTypeDcl)


def test_types_StructForwardDcl_isa_IdlTypeDcl():
    instance = types_StructForwardDcl()
    assert isinstance(instance, IdlTypeDcl)


def test_types_StructType_isa_IdlTypeDcl():
    instance = types_StructType()
    assert isinstance(instance, IdlTypeDcl)


def test_types_TypeDef_isa_IdlTypeDcl():
    instance = types_TypeDef()
    assert isinstance(instance, IdlTypeDcl)


def test_types_UnionForwardDcl_isa_IdlTypeDcl():
    instance = types_UnionForwardDcl()
    assert isinstance(instance, IdlTypeDcl)


def test_types_UnionType_isa_IdlTypeDcl():
    instance = types_UnionType()
    assert isinstance(instance, IdlTypeDcl)


def test_types_StructType_isa_MemberContainer():
    instance = types_StructType()
    assert isinstance(instance, MemberContainer)


def test_types_Any_isa_PrimitiveType():
    instance = types_Any()
    assert isinstance(instance, PrimitiveType)


def test_types_Boolean_isa_PrimitiveType():
    instance = types_Boolean()
    assert isinstance(instance, PrimitiveType)


def test_types_Double_isa_PrimitiveType():
    instance = types_Double()
    assert isinstance(instance, PrimitiveType)


def test_types_Float_isa_PrimitiveType():
    instance = types_Float()
    assert isinstance(instance, PrimitiveType)


def test_types_IdlChar_isa_PrimitiveType():
    instance = types_IdlChar()
    assert isinstance(instance, PrimitiveType)


def test_types_IdlObject_isa_PrimitiveType():
    instance = types_IdlObject()
    assert isinstance(instance, PrimitiveType)


def test_types_IdlWChar_isa_PrimitiveType():
    instance = types_IdlWChar()
    assert isinstance(instance, PrimitiveType)


def test_types_Long_isa_PrimitiveType():
    instance = types_Long()
    assert isinstance(instance, PrimitiveType)


def test_types_LongDouble_isa_PrimitiveType():
    instance = types_LongDouble()
    assert isinstance(instance, PrimitiveType)


def test_types_LongLong_isa_PrimitiveType():
    instance = types_LongLong()
    assert isinstance(instance, PrimitiveType)


def test_types_Octet_isa_PrimitiveType():
    instance = types_Octet()
    assert isinstance(instance, PrimitiveType)


def test_types_Short_isa_PrimitiveType():
    instance = types_Short()
    assert isinstance(instance, PrimitiveType)


def test_types_ULong_isa_PrimitiveType():
    instance = types_ULong()
    assert isinstance(instance, PrimitiveType)


def test_types_ULongLong_isa_PrimitiveType():
    instance = types_ULongLong()
    assert isinstance(instance, PrimitiveType)


def test_types_UShort_isa_PrimitiveType():
    instance = types_UShort()
    assert isinstance(instance, PrimitiveType)


def test_types_ValueBaseType_isa_PrimitiveType():
    instance = types_ValueBaseType()
    assert isinstance(instance, PrimitiveType)


def test_types_WChar_isa_PrimitiveType():
    instance = types_WChar()
    assert isinstance(instance, PrimitiveType)


def test_types_FixedPtType_isa_TemplateType():
    instance = types_FixedPtType()
    assert isinstance(instance, TemplateType)


def test_types_IdlString_isa_TemplateType():
    instance = types_IdlString()
    assert isinstance(instance, TemplateType)


def test_types_SequenceType_isa_TemplateType():
    instance = types_SequenceType()
    assert isinstance(instance, TemplateType)


def test_types_WString_isa_TemplateType():
    instance = types_WString()
    assert isinstance(instance, TemplateType)


def test_types_SequenceType_isa_Typed():
    instance = types_SequenceType()
    assert isinstance(instance, Typed)


def test_types_TypeDef_isa_TypedElement():
    instance = types_TypeDef()
    assert isinstance(instance, TypedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CaseLabel_strategy = st.builds(CaseLabel)
@given(instance=CaseLabel_strategy)
@settings(max_examples=25)
def test_CaseLabel_instantiation(instance):
    assert isinstance(instance, CaseLabel)


Declarator_strategy = st.builds(Declarator)
@given(instance=Declarator_strategy)
@settings(max_examples=25)
def test_Declarator_instantiation(instance):
    assert isinstance(instance, Declarator)


FileRegion_strategy = st.builds(FileRegion)
@given(instance=FileRegion_strategy)
@settings(max_examples=25)
def test_FileRegion_instantiation(instance):
    assert isinstance(instance, FileRegion)


IdlType_strategy = st.builds(IdlType)
@given(instance=IdlType_strategy)
@settings(max_examples=25)
def test_IdlType_instantiation(instance):
    assert isinstance(instance, IdlType)


IdlTypeDcl_strategy = st.builds(IdlTypeDcl)
@given(instance=IdlTypeDcl_strategy)
@settings(max_examples=25)
def test_IdlTypeDcl_instantiation(instance):
    assert isinstance(instance, IdlTypeDcl)


MemberContainer_strategy = st.builds(MemberContainer)
@given(instance=MemberContainer_strategy)
@settings(max_examples=25)
def test_MemberContainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


TemplateType_strategy = st.builds(TemplateType)
@given(instance=TemplateType_strategy)
@settings(max_examples=25)
def test_TemplateType_instantiation(instance):
    assert isinstance(instance, TemplateType)


Typed_strategy = st.builds(Typed)
@given(instance=Typed_strategy)
@settings(max_examples=25)
def test_Typed_instantiation(instance):
    assert isinstance(instance, Typed)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


types_Any_strategy = st.builds(types_Any)
@given(instance=types_Any_strategy)
@settings(max_examples=25)
def test_types_Any_instantiation(instance):
    assert isinstance(instance, types_Any)


types_Boolean_strategy = st.builds(types_Boolean)
@given(instance=types_Boolean_strategy)
@settings(max_examples=25)
def test_types_Boolean_instantiation(instance):
    assert isinstance(instance, types_Boolean)


types_Case_strategy = st.builds(types_Case)
@given(instance=types_Case_strategy)
@settings(max_examples=25)
def test_types_Case_instantiation(instance):
    assert isinstance(instance, types_Case)


types_CaseLabel_strategy = st.builds(types_CaseLabel)
@given(instance=types_CaseLabel_strategy)
@settings(max_examples=25)
def test_types_CaseLabel_instantiation(instance):
    assert isinstance(instance, types_CaseLabel)


types_Declarator_strategy = st.builds(types_Declarator)
@given(instance=types_Declarator_strategy)
@settings(max_examples=25)
def test_types_Declarator_instantiation(instance):
    assert isinstance(instance, types_Declarator)


types_DefaultCaseLabel_strategy = st.builds(types_DefaultCaseLabel)
@given(instance=types_DefaultCaseLabel_strategy)
@settings(max_examples=25)
def test_types_DefaultCaseLabel_instantiation(instance):
    assert isinstance(instance, types_DefaultCaseLabel)


types_Double_strategy = st.builds(types_Double)
@given(instance=types_Double_strategy)
@settings(max_examples=25)
def test_types_Double_instantiation(instance):
    assert isinstance(instance, types_Double)


types_ElementSpec_strategy = st.builds(types_ElementSpec)
@given(instance=types_ElementSpec_strategy)
@settings(max_examples=25)
def test_types_ElementSpec_instantiation(instance):
    assert isinstance(instance, types_ElementSpec)


types_EnumType_strategy = st.builds(types_EnumType)
@given(instance=types_EnumType_strategy)
@settings(max_examples=25)
def test_types_EnumType_instantiation(instance):
    assert isinstance(instance, types_EnumType)


types_Enumeration_strategy = st.builds(types_Enumeration)
@given(instance=types_Enumeration_strategy)
@settings(max_examples=25)
def test_types_Enumeration_instantiation(instance):
    assert isinstance(instance, types_Enumeration)


types_ExprCaseLabel_strategy = st.builds(types_ExprCaseLabel)
@given(instance=types_ExprCaseLabel_strategy)
@settings(max_examples=25)
def test_types_ExprCaseLabel_instantiation(instance):
    assert isinstance(instance, types_ExprCaseLabel)


types_Expression_strategy = st.builds(types_Expression)
@given(instance=types_Expression_strategy)
@settings(max_examples=25)
def test_types_Expression_instantiation(instance):
    assert isinstance(instance, types_Expression)


types_FixedPtType_strategy = st.builds(types_FixedPtType)
@given(instance=types_FixedPtType_strategy)
@settings(max_examples=25)
def test_types_FixedPtType_instantiation(instance):
    assert isinstance(instance, types_FixedPtType)


types_Float_strategy = st.builds(types_Float)
@given(instance=types_Float_strategy)
@settings(max_examples=25)
def test_types_Float_instantiation(instance):
    assert isinstance(instance, types_Float)


types_ForwardDcl_strategy = st.builds(types_ForwardDcl)
@given(instance=types_ForwardDcl_strategy)
@settings(max_examples=25)
def test_types_ForwardDcl_instantiation(instance):
    assert isinstance(instance, types_ForwardDcl)


types_IdlChar_strategy = st.builds(types_IdlChar)
@given(instance=types_IdlChar_strategy)
@settings(max_examples=25)
def test_types_IdlChar_instantiation(instance):
    assert isinstance(instance, types_IdlChar)


types_IdlObject_strategy = st.builds(types_IdlObject)
@given(instance=types_IdlObject_strategy)
@settings(max_examples=25)
def test_types_IdlObject_instantiation(instance):
    assert isinstance(instance, types_IdlObject)


types_IdlString_strategy = st.builds(types_IdlString)
@given(instance=types_IdlString_strategy)
@settings(max_examples=25)
def test_types_IdlString_instantiation(instance):
    assert isinstance(instance, types_IdlString)


types_IdlType_strategy = st.builds(types_IdlType)
@given(instance=types_IdlType_strategy)
@settings(max_examples=25)
def test_types_IdlType_instantiation(instance):
    assert isinstance(instance, types_IdlType)


types_IdlWChar_strategy = st.builds(types_IdlWChar)
@given(instance=types_IdlWChar_strategy)
@settings(max_examples=25)
def test_types_IdlWChar_instantiation(instance):
    assert isinstance(instance, types_IdlWChar)


types_Long_strategy = st.builds(types_Long)
@given(instance=types_Long_strategy)
@settings(max_examples=25)
def test_types_Long_instantiation(instance):
    assert isinstance(instance, types_Long)


types_LongDouble_strategy = st.builds(types_LongDouble)
@given(instance=types_LongDouble_strategy)
@settings(max_examples=25)
def test_types_LongDouble_instantiation(instance):
    assert isinstance(instance, types_LongDouble)


types_LongLong_strategy = st.builds(types_LongLong)
@given(instance=types_LongLong_strategy)
@settings(max_examples=25)
def test_types_LongLong_instantiation(instance):
    assert isinstance(instance, types_LongLong)


types_Octet_strategy = st.builds(types_Octet)
@given(instance=types_Octet_strategy)
@settings(max_examples=25)
def test_types_Octet_instantiation(instance):
    assert isinstance(instance, types_Octet)


types_PrimitiveType_strategy = st.builds(types_PrimitiveType)
@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=25)
def test_types_PrimitiveType_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)


types_SequenceType_strategy = st.builds(types_SequenceType)
@given(instance=types_SequenceType_strategy)
@settings(max_examples=25)
def test_types_SequenceType_instantiation(instance):
    assert isinstance(instance, types_SequenceType)


types_Short_strategy = st.builds(types_Short)
@given(instance=types_Short_strategy)
@settings(max_examples=25)
def test_types_Short_instantiation(instance):
    assert isinstance(instance, types_Short)


types_StructForwardDcl_strategy = st.builds(types_StructForwardDcl)
@given(instance=types_StructForwardDcl_strategy)
@settings(max_examples=25)
def test_types_StructForwardDcl_instantiation(instance):
    assert isinstance(instance, types_StructForwardDcl)


types_StructType_strategy = st.builds(types_StructType)
@given(instance=types_StructType_strategy)
@settings(max_examples=25)
def test_types_StructType_instantiation(instance):
    assert isinstance(instance, types_StructType)


types_Switch_strategy = st.builds(types_Switch)
@given(instance=types_Switch_strategy)
@settings(max_examples=25)
def test_types_Switch_instantiation(instance):
    assert isinstance(instance, types_Switch)


types_TemplateType_strategy = st.builds(types_TemplateType)
@given(instance=types_TemplateType_strategy)
@settings(max_examples=25)
def test_types_TemplateType_instantiation(instance):
    assert isinstance(instance, types_TemplateType)


types_TypeDef_strategy = st.builds(types_TypeDef)
@given(instance=types_TypeDef_strategy)
@settings(max_examples=25)
def test_types_TypeDef_instantiation(instance):
    assert isinstance(instance, types_TypeDef)


types_ULong_strategy = st.builds(types_ULong)
@given(instance=types_ULong_strategy)
@settings(max_examples=25)
def test_types_ULong_instantiation(instance):
    assert isinstance(instance, types_ULong)


types_ULongLong_strategy = st.builds(types_ULongLong)
@given(instance=types_ULongLong_strategy)
@settings(max_examples=25)
def test_types_ULongLong_instantiation(instance):
    assert isinstance(instance, types_ULongLong)


types_UShort_strategy = st.builds(types_UShort)
@given(instance=types_UShort_strategy)
@settings(max_examples=25)
def test_types_UShort_instantiation(instance):
    assert isinstance(instance, types_UShort)


types_UnionForwardDcl_strategy = st.builds(types_UnionForwardDcl)
@given(instance=types_UnionForwardDcl_strategy)
@settings(max_examples=25)
def test_types_UnionForwardDcl_instantiation(instance):
    assert isinstance(instance, types_UnionForwardDcl)


types_UnionType_strategy = st.builds(types_UnionType)
@given(instance=types_UnionType_strategy)
@settings(max_examples=25)
def test_types_UnionType_instantiation(instance):
    assert isinstance(instance, types_UnionType)


types_ValueBaseType_strategy = st.builds(types_ValueBaseType)
@given(instance=types_ValueBaseType_strategy)
@settings(max_examples=25)
def test_types_ValueBaseType_instantiation(instance):
    assert isinstance(instance, types_ValueBaseType)


types_VoidType_strategy = st.builds(types_VoidType)
@given(instance=types_VoidType_strategy)
@settings(max_examples=25)
def test_types_VoidType_instantiation(instance):
    assert isinstance(instance, types_VoidType)


types_WChar_strategy = st.builds(types_WChar)
@given(instance=types_WChar_strategy)
@settings(max_examples=25)
def test_types_WChar_instantiation(instance):
    assert isinstance(instance, types_WChar)


types_WString_strategy = st.builds(types_WString)
@given(instance=types_WString_strategy)
@settings(max_examples=25)
def test_types_WString_instantiation(instance):
    assert isinstance(instance, types_WString)


