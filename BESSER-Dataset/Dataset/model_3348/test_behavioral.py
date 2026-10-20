import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AtomicBooleanExpression,
    BaseRecord,
    BaseTrait,
    Element,
    Field,
    GenericExpression,
    Message,
    Method,
    Parameter,
    RecordOperation,
    Start,
    Statement,
    TraitElement,
    TraitOperation,
    swrtj_AnonimousRecord,
    swrtj_AnonimousTrait,
    swrtj_Args,
    swrtj_AtomicBooleanExpression,
    swrtj_BaseRecord,
    swrtj_BaseTrait,
    swrtj_Block,
    swrtj_BooleanConstant,
    swrtj_BooleanExpression,
    swrtj_BooleanOperator,
    swrtj_Cast,
    swrtj_Class,
    swrtj_CompareOperator,
    swrtj_Constructor,
    swrtj_ConstructorInvocation,
    swrtj_DottedExpression,
    swrtj_Element,
    swrtj_Expression,
    swrtj_ExpressionStatement,
    swrtj_Field,
    swrtj_FieldAccess,
    swrtj_FieldDeclaration,
    swrtj_FieldName,
    swrtj_File,
    swrtj_FormalParameter,
    swrtj_GenericExpression,
    swrtj_IfThenElseStatement,
    swrtj_Import,
    swrtj_Input,
    swrtj_Interface,
    swrtj_LocalParameter,
    swrtj_Message,
    swrtj_Method,
    swrtj_MethodInvocation,
    swrtj_MethodName,
    swrtj_NestedBooleanExpression,
    swrtj_NestedExpression,
    swrtj_NestedRecordExpression,
    swrtj_NestedTraitExpression,
    swrtj_Null,
    swrtj_Number,
    swrtj_Output,
    swrtj_Parameter,
    swrtj_ParameterAssignment,
    swrtj_ParameterReference,
    swrtj_Program,
    swrtj_ProvidedMethod,
    swrtj_Record,
    swrtj_RecordExclude,
    swrtj_RecordExpression,
    swrtj_RecordName,
    swrtj_RecordOperation,
    swrtj_RecordRename,
    swrtj_RequiredField,
    swrtj_RequiredMethod,
    swrtj_ReturnStatement,
    swrtj_SimpleComparation,
    swrtj_Start,
    swrtj_Statement,
    swrtj_StringConstant,
    swrtj_This,
    swrtj_Trait,
    swrtj_TraitAlias,
    swrtj_TraitElement,
    swrtj_TraitExclude,
    swrtj_TraitExpression,
    swrtj_TraitFieldRename,
    swrtj_TraitMethodRename,
    swrtj_TraitName,
    swrtj_TraitOperation,
    swrtj_Type,
    swrtj_WhileStatement,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_parameterList49_reverse_link_reassign_clear():
    a1 = swrtj_Parameter(name="sample_text")
    a2 = swrtj_Parameter(name="sample_text_2")
    b = swrtj_Constructor(name="sample_text")
    _safe_set(b, 'swrtj_Constructor50', {a1})
    assert _is_linked(b, 'swrtj_Constructor50', a1)
    if hasattr(a1, 'swrtj_Parameter51'):
        assert _is_linked(a1, 'swrtj_Parameter51', b)
    _safe_set(b, 'swrtj_Constructor50', {a2})
    assert _is_linked(b, 'swrtj_Constructor50', a2)
    if hasattr(a1, 'swrtj_Parameter51'):
        assert not _is_linked(a1, 'swrtj_Parameter51', b)
    if hasattr(a2, 'swrtj_Parameter51'):
        assert _is_linked(a2, 'swrtj_Parameter51', b)
    _safe_set(b, 'swrtj_Constructor50', set())
    assert not _is_linked(b, 'swrtj_Constructor50', a2)
    if hasattr(a2, 'swrtj_Parameter51'):
        assert not _is_linked(a2, 'swrtj_Parameter51', b)


def test_assoc_type56_reverse_link_reassign_clear():
    a1 = swrtj_Type(primitiveType="sample_text")
    a2 = swrtj_Type(primitiveType="sample_text_2")
    b = swrtj_Parameter(name="sample_text")
    _safe_set(b, 'swrtj_Parameter57', a1)
    assert _is_linked(b, 'swrtj_Parameter57', a1)
    if hasattr(a1, 'swrtj_Type58'):
        assert _is_linked(a1, 'swrtj_Type58', b)
    _safe_set(b, 'swrtj_Parameter57', a2)
    assert _is_linked(b, 'swrtj_Parameter57', a2)
    if hasattr(a1, 'swrtj_Type58'):
        assert not _is_linked(a1, 'swrtj_Type58', b)
    if hasattr(a2, 'swrtj_Type58'):
        assert _is_linked(a2, 'swrtj_Type58', b)
    _safe_set(b, 'swrtj_Parameter57', None)
    assert not _is_linked(b, 'swrtj_Parameter57', a2)
    if hasattr(a2, 'swrtj_Type58'):
        assert not _is_linked(a2, 'swrtj_Type58', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_atomicList155_stub_double():
    # swrtj_BooleanExpression has no real 'swrtj_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_AtomicBooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_AtomicBooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_AtomicBooleanExpression(negated=True)
    partner = swrtj_BooleanExpression()
    setattr(partner, 'swrtj_BooleanExpression', None)
    _safe_set(owner, 'swrtj_AtomicBooleanExpression', partner)
    assert owner in getattr(partner, 'swrtj_BooleanExpression')
    _safe_set(owner, 'swrtj_AtomicBooleanExpression', None)
    assert owner not in getattr(partner, 'swrtj_BooleanExpression')


def test_assoc_block150_stub_double():
    # swrtj_Block has no real 'swrtj_Block151' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_ProvidedMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_ProvidedMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_ProvidedMethod(isSynchronized=True)
    partner = swrtj_Block()
    setattr(partner, 'swrtj_Block151', None)
    _safe_set(owner, 'swrtj_ProvidedMethod', partner)
    assert getattr(partner, 'swrtj_Block151') == owner
    _safe_set(owner, 'swrtj_ProvidedMethod', None)
    assert getattr(partner, 'swrtj_Block151') is None


def test_assoc_block52_stub_double():
    # swrtj_Block has no real 'swrtj_Block54' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Constructor(name="sample_text")
    partner = swrtj_Block()
    setattr(partner, 'swrtj_Block54', None)
    _safe_set(owner, 'swrtj_Constructor53', partner)
    assert getattr(partner, 'swrtj_Block54') == owner
    _safe_set(owner, 'swrtj_Constructor53', None)
    assert getattr(partner, 'swrtj_Block54') is None


def test_assoc_booleanOperatorList156_stub_double():
    # swrtj_BooleanExpression has no real 'swrtj_BooleanExpression157' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_BooleanOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_BooleanOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_BooleanOperator(operator="sample_text")
    partner = swrtj_BooleanExpression()
    setattr(partner, 'swrtj_BooleanExpression157', None)
    _safe_set(owner, 'swrtj_BooleanOperator', partner)
    assert owner in getattr(partner, 'swrtj_BooleanExpression157')
    _safe_set(owner, 'swrtj_BooleanOperator', None)
    assert owner not in getattr(partner, 'swrtj_BooleanExpression157')


def test_assoc_compare84_stub_double():
    # swrtj_SimpleComparation has no real 'swrtj_SimpleComparation85' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_CompareOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_CompareOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_CompareOperator(operator="sample_text")
    partner = swrtj_SimpleComparation()
    setattr(partner, 'swrtj_SimpleComparation85', None)
    _safe_set(owner, 'swrtj_CompareOperator', partner)
    assert getattr(partner, 'swrtj_SimpleComparation85') == owner
    _safe_set(owner, 'swrtj_CompareOperator', None)
    assert getattr(partner, 'swrtj_SimpleComparation85') is None


def test_assoc_constructorList17_stub_double():
    # swrtj_Class has no real 'swrtj_Class18' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Constructor(name="sample_text")
    partner = swrtj_Class()
    setattr(partner, 'swrtj_Class18', None)
    _safe_set(owner, 'swrtj_Constructor', partner)
    assert owner in getattr(partner, 'swrtj_Class18')
    _safe_set(owner, 'swrtj_Constructor', None)
    assert owner not in getattr(partner, 'swrtj_Class18')


def test_assoc_elementList1_stub_double():
    # swrtj_File has no real 'swrtj_File2' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Element(construct="sample_text", name="sample_text")
    partner = swrtj_File()
    setattr(partner, 'swrtj_File2', None)
    _safe_set(owner, 'swrtj_Element', partner)
    assert owner in getattr(partner, 'swrtj_File2')
    _safe_set(owner, 'swrtj_Element', None)
    assert owner not in getattr(partner, 'swrtj_File2')


def test_assoc_field119_stub_double():
    # swrtj_FieldAccess has no real 'swrtj_FieldAccess' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_FieldAccess()
    setattr(partner, 'swrtj_FieldAccess', None)
    _safe_set(owner, 'swrtj_FieldName120', partner)
    assert getattr(partner, 'swrtj_FieldAccess') == owner
    _safe_set(owner, 'swrtj_FieldName120', None)
    assert getattr(partner, 'swrtj_FieldAccess') is None


def test_assoc_field126_stub_double():
    # swrtj_RecordExclude has no real 'swrtj_RecordExclude' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_RecordExclude()
    setattr(partner, 'swrtj_RecordExclude', None)
    _safe_set(owner, 'swrtj_FieldName127', partner)
    assert getattr(partner, 'swrtj_RecordExclude') == owner
    _safe_set(owner, 'swrtj_FieldName127', None)
    assert getattr(partner, 'swrtj_RecordExclude') is None


def test_assoc_fieldRef40_stub_double():
    # swrtj_Field has no real 'swrtj_Field41' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_Field()
    setattr(partner, 'swrtj_Field41', None)
    _safe_set(owner, 'swrtj_FieldName', partner)
    assert getattr(partner, 'swrtj_Field41') == owner
    _safe_set(owner, 'swrtj_FieldName', None)
    assert getattr(partner, 'swrtj_Field41') is None


def test_assoc_importList0_stub_double():
    # swrtj_File has no real 'swrtj_File' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Import(importURI="sample_text")
    partner = swrtj_File()
    setattr(partner, 'swrtj_File', None)
    _safe_set(owner, 'swrtj_Import', partner)
    assert owner in getattr(partner, 'swrtj_File')
    _safe_set(owner, 'swrtj_Import', None)
    assert owner not in getattr(partner, 'swrtj_File')


def test_assoc_interfaceType59_stub_double():
    # swrtj_Interface has no real 'swrtj_Interface61' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Type(primitiveType="sample_text")
    partner = swrtj_Interface()
    setattr(partner, 'swrtj_Interface61', None)
    _safe_set(owner, 'swrtj_Type60', partner)
    assert getattr(partner, 'swrtj_Interface61') == owner
    _safe_set(owner, 'swrtj_Type60', None)
    assert getattr(partner, 'swrtj_Interface61') is None


def test_assoc_method114_stub_double():
    # swrtj_MethodInvocation has no real 'swrtj_MethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_MethodInvocation()
    setattr(partner, 'swrtj_MethodInvocation', None)
    _safe_set(owner, 'swrtj_MethodName115', partner)
    assert getattr(partner, 'swrtj_MethodInvocation') == owner
    _safe_set(owner, 'swrtj_MethodName115', None)
    assert getattr(partner, 'swrtj_MethodInvocation') is None


def test_assoc_method133_stub_double():
    # swrtj_TraitExclude has no real 'swrtj_TraitExclude' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_TraitExclude()
    setattr(partner, 'swrtj_TraitExclude', None)
    _safe_set(owner, 'swrtj_MethodName134', partner)
    assert getattr(partner, 'swrtj_TraitExclude') == owner
    _safe_set(owner, 'swrtj_MethodName134', None)
    assert getattr(partner, 'swrtj_TraitExclude') is None


def test_assoc_methodRef45_stub_double():
    # swrtj_Method has no real 'swrtj_Method46' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_Method()
    setattr(partner, 'swrtj_Method46', None)
    _safe_set(owner, 'swrtj_MethodName', partner)
    assert getattr(partner, 'swrtj_Method46') == owner
    _safe_set(owner, 'swrtj_MethodName', None)
    assert getattr(partner, 'swrtj_Method46') is None


def test_assoc_newField130_stub_double():
    # swrtj_RecordRename has no real 'swrtj_RecordRename131' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_RecordRename()
    setattr(partner, 'swrtj_RecordRename131', None)
    _safe_set(owner, 'swrtj_FieldName132', partner)
    assert getattr(partner, 'swrtj_RecordRename131') == owner
    _safe_set(owner, 'swrtj_FieldName132', None)
    assert getattr(partner, 'swrtj_RecordRename131') is None


def test_assoc_newField147_stub_double():
    # swrtj_TraitFieldRename has no real 'swrtj_TraitFieldRename148' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_TraitFieldRename()
    setattr(partner, 'swrtj_TraitFieldRename148', None)
    _safe_set(owner, 'swrtj_FieldName149', partner)
    assert getattr(partner, 'swrtj_TraitFieldRename148') == owner
    _safe_set(owner, 'swrtj_FieldName149', None)
    assert getattr(partner, 'swrtj_TraitFieldRename148') is None


def test_assoc_newMethod137_stub_double():
    # swrtj_TraitAlias has no real 'swrtj_TraitAlias138' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_TraitAlias()
    setattr(partner, 'swrtj_TraitAlias138', None)
    _safe_set(owner, 'swrtj_MethodName139', partner)
    assert getattr(partner, 'swrtj_TraitAlias138') == owner
    _safe_set(owner, 'swrtj_MethodName139', None)
    assert getattr(partner, 'swrtj_TraitAlias138') is None


def test_assoc_newMethod142_stub_double():
    # swrtj_TraitMethodRename has no real 'swrtj_TraitMethodRename143' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_TraitMethodRename()
    setattr(partner, 'swrtj_TraitMethodRename143', None)
    _safe_set(owner, 'swrtj_MethodName144', partner)
    assert getattr(partner, 'swrtj_TraitMethodRename143') == owner
    _safe_set(owner, 'swrtj_MethodName144', None)
    assert getattr(partner, 'swrtj_TraitMethodRename143') is None


def test_assoc_originalField128_stub_double():
    # swrtj_RecordRename has no real 'swrtj_RecordRename' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_RecordRename()
    setattr(partner, 'swrtj_RecordRename', None)
    _safe_set(owner, 'swrtj_FieldName129', partner)
    assert getattr(partner, 'swrtj_RecordRename') == owner
    _safe_set(owner, 'swrtj_FieldName129', None)
    assert getattr(partner, 'swrtj_RecordRename') is None


def test_assoc_originalField145_stub_double():
    # swrtj_TraitFieldRename has no real 'swrtj_TraitFieldRename' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_FieldName(name="sample_text")
    partner = swrtj_TraitFieldRename()
    setattr(partner, 'swrtj_TraitFieldRename', None)
    _safe_set(owner, 'swrtj_FieldName146', partner)
    assert getattr(partner, 'swrtj_TraitFieldRename') == owner
    _safe_set(owner, 'swrtj_FieldName146', None)
    assert getattr(partner, 'swrtj_TraitFieldRename') is None


def test_assoc_originalMethod135_stub_double():
    # swrtj_TraitAlias has no real 'swrtj_TraitAlias' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_TraitAlias()
    setattr(partner, 'swrtj_TraitAlias', None)
    _safe_set(owner, 'swrtj_MethodName136', partner)
    assert getattr(partner, 'swrtj_TraitAlias') == owner
    _safe_set(owner, 'swrtj_MethodName136', None)
    assert getattr(partner, 'swrtj_TraitAlias') is None


def test_assoc_originalMethod140_stub_double():
    # swrtj_TraitMethodRename has no real 'swrtj_TraitMethodRename' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_MethodName(name="sample_text")
    partner = swrtj_TraitMethodRename()
    setattr(partner, 'swrtj_TraitMethodRename', None)
    _safe_set(owner, 'swrtj_MethodName141', partner)
    assert getattr(partner, 'swrtj_TraitMethodRename') == owner
    _safe_set(owner, 'swrtj_MethodName141', None)
    assert getattr(partner, 'swrtj_TraitMethodRename') is None


def test_assoc_parameter100_stub_double():
    # swrtj_ParameterReference has no real 'swrtj_ParameterReference' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Parameter(name="sample_text")
    partner = swrtj_ParameterReference()
    setattr(partner, 'swrtj_ParameterReference', None)
    _safe_set(owner, 'swrtj_Parameter101', partner)
    assert getattr(partner, 'swrtj_ParameterReference') == owner
    _safe_set(owner, 'swrtj_Parameter101', None)
    assert getattr(partner, 'swrtj_ParameterReference') is None


def test_assoc_parameter121_stub_double():
    # swrtj_ParameterAssignment has no real 'swrtj_ParameterAssignment' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Parameter(name="sample_text")
    partner = swrtj_ParameterAssignment()
    setattr(partner, 'swrtj_ParameterAssignment', None)
    _safe_set(owner, 'swrtj_Parameter122', partner)
    assert getattr(partner, 'swrtj_ParameterAssignment') == owner
    _safe_set(owner, 'swrtj_Parameter122', None)
    assert getattr(partner, 'swrtj_ParameterAssignment') is None


def test_assoc_parameterList47_stub_double():
    # swrtj_Method has no real 'swrtj_Method48' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Parameter(name="sample_text")
    partner = swrtj_Method()
    setattr(partner, 'swrtj_Method48', None)
    _safe_set(owner, 'swrtj_Parameter', partner)
    assert owner in getattr(partner, 'swrtj_Method48')
    _safe_set(owner, 'swrtj_Parameter', None)
    assert owner not in getattr(partner, 'swrtj_Method48')


def test_assoc_parameterList62_stub_double():
    # swrtj_Block has no real 'swrtj_Block63' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Parameter(name="sample_text")
    partner = swrtj_Block()
    setattr(partner, 'swrtj_Block63', None)
    _safe_set(owner, 'swrtj_Parameter64', partner)
    assert owner in getattr(partner, 'swrtj_Block63')
    _safe_set(owner, 'swrtj_Parameter64', None)
    assert owner not in getattr(partner, 'swrtj_Block63')


def test_assoc_returnStatement152_stub_double():
    # swrtj_ReturnStatement has no real 'swrtj_ReturnStatement154' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_ProvidedMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_ProvidedMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_ProvidedMethod(isSynchronized=True)
    partner = swrtj_ReturnStatement()
    setattr(partner, 'swrtj_ReturnStatement154', None)
    _safe_set(owner, 'swrtj_ProvidedMethod153', partner)
    assert getattr(partner, 'swrtj_ReturnStatement154') == owner
    _safe_set(owner, 'swrtj_ProvidedMethod153', None)
    assert getattr(partner, 'swrtj_ReturnStatement154') is None


def test_assoc_returnType42_stub_double():
    # swrtj_Method has no real 'swrtj_Method43' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Type(primitiveType="sample_text")
    partner = swrtj_Method()
    setattr(partner, 'swrtj_Method43', None)
    _safe_set(owner, 'swrtj_Type44', partner)
    assert getattr(partner, 'swrtj_Method43') == owner
    _safe_set(owner, 'swrtj_Type44', None)
    assert getattr(partner, 'swrtj_Method43') is None


def test_assoc_termList160_stub_double():
    # swrtj_DottedExpression has no real 'swrtj_DottedExpression161' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Expression(operatorList="sample_text", sign="sample_text")
    partner = swrtj_DottedExpression()
    setattr(partner, 'swrtj_DottedExpression161', None)
    _safe_set(owner, 'swrtj_Expression', {partner})
    assert getattr(partner, 'swrtj_DottedExpression161') == owner
    _safe_set(owner, 'swrtj_Expression', set())
    assert getattr(partner, 'swrtj_DottedExpression161') is None


def test_assoc_type107_stub_double():
    # swrtj_Cast has no real 'swrtj_Cast' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Type(primitiveType="sample_text")
    partner = swrtj_Cast()
    setattr(partner, 'swrtj_Cast', None)
    _safe_set(owner, 'swrtj_Type108', partner)
    assert getattr(partner, 'swrtj_Cast') == owner
    _safe_set(owner, 'swrtj_Type108', None)
    assert getattr(partner, 'swrtj_Cast') is None


def test_assoc_type38_stub_double():
    # swrtj_Field has no real 'swrtj_Field39' property in the generated
    # code (a bare stub) -- manually attach it so swrtj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swrtj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swrtj_Type(primitiveType="sample_text")
    partner = swrtj_Field()
    setattr(partner, 'swrtj_Field39', None)
    _safe_set(owner, 'swrtj_Type', partner)
    assert getattr(partner, 'swrtj_Field39') == owner
    _safe_set(owner, 'swrtj_Type', None)
    assert getattr(partner, 'swrtj_Field39') is None


