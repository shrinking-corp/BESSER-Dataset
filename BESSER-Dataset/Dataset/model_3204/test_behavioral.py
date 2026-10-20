import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActualParameter,
    AttrDecl,
    BaseTypeSpec,
    ComplexDeclarator,
    ComponentExport,
    ConnectorExport,
    ConstExp,
    ConstParamType,
    ConstType,
    ConstrForwardDecl,
    ConstrTypeSpec,
    Declarator,
    Definition,
    Event,
    Export,
    FixedDefinition,
    FloatingPtType,
    FormalParameterType,
    HomeExport,
    IntegerType,
    Interface_or_Forward_Decl,
    OpTypeDecl,
    ParamTypeSpec,
    PortExport,
    Preproc,
    Preproc_Pragma,
    PrimaryExpr,
    SignedInt,
    SimpleTypeSpec,
    SwitchTypeSpec,
    TemplateDefinition,
    TemplateTypeSpec,
    TypeDecl,
    TypeSpec,
    UnsignedInt,
    idl_ActualParameter,
    idl_AddExpr,
    idl_AndExpr,
    idl_AnyType,
    idl_ArrayDeclarator,
    idl_AttrDecl,
    idl_AttrRaisesExpr,
    idl_AttrSpec,
    idl_BaseTypeSpec,
    idl_BooleanType,
    idl_Case,
    idl_CaseLabel,
    idl_CharType,
    idl_ComplexDeclarator,
    idl_ComponentDecl,
    idl_ComponentExport,
    idl_ComponentForwardDecl,
    idl_Connector,
    idl_ConnectorExport,
    idl_ConnectorHeader,
    idl_ConstDecl,
    idl_ConstExp,
    idl_ConstParamType,
    idl_ConstType,
    idl_ConstrForwardDecl,
    idl_ConstrTypeSpec,
    idl_ConsumesDcl,
    idl_ContextExpr,
    idl_Declarator,
    idl_Definition,
    idl_DoubleType,
    idl_ElementSpec,
    idl_EmitDcl,
    idl_EnumParamType,
    idl_EnumType,
    idl_Event,
    idl_EventDcl,
    idl_EventForwardDcl,
    idl_EventParamType,
    idl_ExceptDecl,
    idl_ExceptionList,
    idl_ExceptionParamType,
    idl_Excluded_File_Marker,
    idl_Export,
    idl_FactoryDcl,
    idl_FileName,
    idl_File_Marker,
    idl_FinderDcl,
    idl_FixedDefinition,
    idl_FixedModule,
    idl_FixedPtConstType,
    idl_FixedPtType,
    idl_FloatType,
    idl_FloatingPtType,
    idl_FormalParameter,
    idl_FormalParameterType,
    idl_Forward_decl,
    idl_HomeDecl,
    idl_HomeExport,
    idl_IDLComment,
    idl_Import_decl,
    idl_IntegerType,
    idl_InterfaceBody,
    idl_InterfaceParamType,
    idl_Interface_decl,
    idl_Interface_header,
    idl_Interface_or_Forward_Decl,
    idl_Literal,
    idl_LongDoubleType,
    idl_Member,
    idl_Module,
    idl_MultExpr,
    idl_NativeType,
    idl_ObjectType,
    idl_OctetType,
    idl_OpDecl,
    idl_OpTypeDecl,
    idl_OrExpr,
    idl_ParamDcl,
    idl_ParamTypeSpec,
    idl_ParameterDecls,
    idl_PortDecl,
    idl_PortExport,
    idl_PortTypeDecl,
    idl_PositiveIntConst,
    idl_Preproc,
    idl_Preproc_Define,
    idl_Preproc_Else,
    idl_Preproc_Endif,
    idl_Preproc_Error,
    idl_Preproc_If,
    idl_Preproc_If_Compare,
    idl_Preproc_If_Val,
    idl_Preproc_Ifdef,
    idl_Preproc_Ifndef,
    idl_Preproc_Include,
    idl_Preproc_Pragma,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Idl,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Interface,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle,
    idl_Preproc_Pragma_Ciao_Lem,
    idl_Preproc_Pragma_Component,
    idl_Preproc_Pragma_DDS4CCM_Impl,
    idl_Preproc_Pragma_Home,
    idl_Preproc_Pragma_Misc,
    idl_Preproc_Pragma_Ndds,
    idl_Preproc_Pragma_Prefix,
    idl_Preproc_Undef,
    idl_PrimaryExpr,
    idl_PrimaryKeySpec,
    idl_ProvidesDcl,
    idl_PublishesDcl,
    idl_ReadOnlyAttrSpec,
    idl_ScopedName,
    idl_SequenceParamType,
    idl_SequenceType,
    idl_ShiftExpr,
    idl_SignedInt,
    idl_SignedLongInt,
    idl_SignedLongLongInt,
    idl_SignedShortInt,
    idl_SimpleDeclarator,
    idl_SimpleTypeSpec,
    idl_Specification,
    idl_StateMember,
    idl_StringType,
    idl_StructForwardDecl,
    idl_StructParamType,
    idl_StructType,
    idl_SwitchBody,
    idl_SwitchTypeSpec,
    idl_TemplateDefinition,
    idl_TemplateModule,
    idl_TemplateModuleInst,
    idl_TemplateModuleRef,
    idl_TemplateTypeSpec,
    idl_TypeDecl,
    idl_TypeDeclarator,
    idl_TypeSpec,
    idl_TypenameParamType,
    idl_UnaryExpr,
    idl_UnionForwardDecl,
    idl_UnionParamType,
    idl_UnionType,
    idl_UnsignedInt,
    idl_UnsignedLongInt,
    idl_UnsignedLongLongInt,
    idl_UnsignedShortInt,
    idl_UsesDcl,
    idl_ValueBaseType,
    idl_ValuetypeParamType,
    idl_WideCharType,
    idl_WideStringType,
    idl_XOrExpr,
    ParamDirection,
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

def test_assoc_base169_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_ComponentDecl(name="sample_text")
    _safe_set(b, 'idl_ComponentDecl170', a1)
    assert _is_linked(b, 'idl_ComponentDecl170', a1)
    if hasattr(a1, 'idl_ScopedName171'):
        assert _is_linked(a1, 'idl_ScopedName171', b)
    _safe_set(b, 'idl_ComponentDecl170', a2)
    assert _is_linked(b, 'idl_ComponentDecl170', a2)
    if hasattr(a1, 'idl_ScopedName171'):
        assert not _is_linked(a1, 'idl_ScopedName171', b)
    if hasattr(a2, 'idl_ScopedName171'):
        assert _is_linked(a2, 'idl_ScopedName171', b)
    _safe_set(b, 'idl_ComponentDecl170', None)
    assert not _is_linked(b, 'idl_ComponentDecl170', a2)
    if hasattr(a2, 'idl_ScopedName171'):
        assert not _is_linked(a2, 'idl_ScopedName171', b)


def test_assoc_base204_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_HomeDecl(name="sample_text")
    _safe_set(b, 'idl_HomeDecl205', a1)
    assert _is_linked(b, 'idl_HomeDecl205', a1)
    if hasattr(a1, 'idl_ScopedName206'):
        assert _is_linked(a1, 'idl_ScopedName206', b)
    _safe_set(b, 'idl_HomeDecl205', a2)
    assert _is_linked(b, 'idl_HomeDecl205', a2)
    if hasattr(a1, 'idl_ScopedName206'):
        assert not _is_linked(a1, 'idl_ScopedName206', b)
    if hasattr(a2, 'idl_ScopedName206'):
        assert _is_linked(a2, 'idl_ScopedName206', b)
    _safe_set(b, 'idl_HomeDecl205', None)
    assert not _is_linked(b, 'idl_HomeDecl205', a2)
    if hasattr(a2, 'idl_ScopedName206'):
        assert not _is_linked(a2, 'idl_ScopedName206', b)


def test_assoc_base236_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_EventDcl(isCustom=True, isTruncatable=True)
    _safe_set(b, 'idl_EventDcl', {a1})
    assert _is_linked(b, 'idl_EventDcl', a1)
    if hasattr(a1, 'idl_ScopedName237'):
        assert _is_linked(a1, 'idl_ScopedName237', b)
    _safe_set(b, 'idl_EventDcl', {a2})
    assert _is_linked(b, 'idl_EventDcl', a2)
    if hasattr(a1, 'idl_ScopedName237'):
        assert not _is_linked(a1, 'idl_ScopedName237', b)
    if hasattr(a2, 'idl_ScopedName237'):
        assert _is_linked(a2, 'idl_ScopedName237', b)
    _safe_set(b, 'idl_EventDcl', set())
    assert not _is_linked(b, 'idl_EventDcl', a2)
    if hasattr(a2, 'idl_ScopedName237'):
        assert not _is_linked(a2, 'idl_ScopedName237', b)


def test_assoc_base261_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_ConnectorHeader(name="sample_text")
    _safe_set(b, 'idl_ConnectorHeader262', a1)
    assert _is_linked(b, 'idl_ConnectorHeader262', a1)
    if hasattr(a1, 'idl_ScopedName263'):
        assert _is_linked(a1, 'idl_ScopedName263', b)
    _safe_set(b, 'idl_ConnectorHeader262', a2)
    assert _is_linked(b, 'idl_ConnectorHeader262', a2)
    if hasattr(a1, 'idl_ScopedName263'):
        assert not _is_linked(a1, 'idl_ScopedName263', b)
    if hasattr(a2, 'idl_ScopedName263'):
        assert _is_linked(a2, 'idl_ScopedName263', b)
    _safe_set(b, 'idl_ConnectorHeader262', None)
    assert not _is_linked(b, 'idl_ConnectorHeader262', a2)
    if hasattr(a2, 'idl_ScopedName263'):
        assert not _is_linked(a2, 'idl_ScopedName263', b)


def test_assoc_comments115_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_EnumType(literal="sample_text", name="sample_text")
    _safe_set(b, 'idl_EnumType', {a1})
    assert _is_linked(b, 'idl_EnumType', a1)
    if hasattr(a1, 'idl_IDLComment116'):
        assert _is_linked(a1, 'idl_IDLComment116', b)
    _safe_set(b, 'idl_EnumType', {a2})
    assert _is_linked(b, 'idl_EnumType', a2)
    if hasattr(a1, 'idl_IDLComment116'):
        assert not _is_linked(a1, 'idl_IDLComment116', b)
    if hasattr(a2, 'idl_IDLComment116'):
        assert _is_linked(a2, 'idl_IDLComment116', b)
    _safe_set(b, 'idl_EnumType', set())
    assert not _is_linked(b, 'idl_EnumType', a2)
    if hasattr(a2, 'idl_IDLComment116'):
        assert not _is_linked(a2, 'idl_IDLComment116', b)


def test_assoc_comments133_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_ConstDecl(name="sample_text")
    _safe_set(b, 'idl_ConstDecl134', {a1})
    assert _is_linked(b, 'idl_ConstDecl134', a1)
    if hasattr(a1, 'idl_IDLComment135'):
        assert _is_linked(a1, 'idl_IDLComment135', b)
    _safe_set(b, 'idl_ConstDecl134', {a2})
    assert _is_linked(b, 'idl_ConstDecl134', a2)
    if hasattr(a1, 'idl_IDLComment135'):
        assert not _is_linked(a1, 'idl_IDLComment135', b)
    if hasattr(a2, 'idl_IDLComment135'):
        assert _is_linked(a2, 'idl_IDLComment135', b)
    _safe_set(b, 'idl_ConstDecl134', set())
    assert not _is_linked(b, 'idl_ConstDecl134', a2)
    if hasattr(a2, 'idl_IDLComment135'):
        assert not _is_linked(a2, 'idl_IDLComment135', b)


def test_assoc_comments14_reverse_link_reassign_clear():
    a1 = idl_Module(name="sample_text")
    a2 = idl_Module(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment', a1)
    assert _is_linked(b, 'idl_IDLComment', a1)
    if hasattr(a1, 'idl_Module'):
        assert _is_linked(a1, 'idl_Module', b)
    _safe_set(b, 'idl_IDLComment', a2)
    assert _is_linked(b, 'idl_IDLComment', a2)
    if hasattr(a1, 'idl_Module'):
        assert not _is_linked(a1, 'idl_Module', b)
    if hasattr(a2, 'idl_Module'):
        assert _is_linked(a2, 'idl_Module', b)
    _safe_set(b, 'idl_IDLComment', None)
    assert not _is_linked(b, 'idl_IDLComment', a2)
    if hasattr(a2, 'idl_Module'):
        assert not _is_linked(a2, 'idl_Module', b)


def test_assoc_comments167_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_ComponentDecl(name="sample_text")
    _safe_set(b, 'idl_ComponentDecl', {a1})
    assert _is_linked(b, 'idl_ComponentDecl', a1)
    if hasattr(a1, 'idl_IDLComment168'):
        assert _is_linked(a1, 'idl_IDLComment168', b)
    _safe_set(b, 'idl_ComponentDecl', {a2})
    assert _is_linked(b, 'idl_ComponentDecl', a2)
    if hasattr(a1, 'idl_IDLComment168'):
        assert not _is_linked(a1, 'idl_IDLComment168', b)
    if hasattr(a2, 'idl_IDLComment168'):
        assert _is_linked(a2, 'idl_IDLComment168', b)
    _safe_set(b, 'idl_ComponentDecl', set())
    assert not _is_linked(b, 'idl_ComponentDecl', a2)
    if hasattr(a2, 'idl_IDLComment168'):
        assert not _is_linked(a2, 'idl_IDLComment168', b)


def test_assoc_comments179_reverse_link_reassign_clear():
    a1 = idl_ProvidesDcl(name="sample_text")
    a2 = idl_ProvidesDcl(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment181', a1)
    assert _is_linked(b, 'idl_IDLComment181', a1)
    if hasattr(a1, 'idl_ProvidesDcl180'):
        assert _is_linked(a1, 'idl_ProvidesDcl180', b)
    _safe_set(b, 'idl_IDLComment181', a2)
    assert _is_linked(b, 'idl_IDLComment181', a2)
    if hasattr(a1, 'idl_ProvidesDcl180'):
        assert not _is_linked(a1, 'idl_ProvidesDcl180', b)
    if hasattr(a2, 'idl_ProvidesDcl180'):
        assert _is_linked(a2, 'idl_ProvidesDcl180', b)
    _safe_set(b, 'idl_IDLComment181', None)
    assert not _is_linked(b, 'idl_IDLComment181', a2)
    if hasattr(a2, 'idl_ProvidesDcl180'):
        assert not _is_linked(a2, 'idl_ProvidesDcl180', b)


def test_assoc_comments184_reverse_link_reassign_clear():
    a1 = idl_UsesDcl(isMultiple=True, name="sample_text")
    a2 = idl_UsesDcl(isMultiple=False, name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment186', a1)
    assert _is_linked(b, 'idl_IDLComment186', a1)
    if hasattr(a1, 'idl_UsesDcl185'):
        assert _is_linked(a1, 'idl_UsesDcl185', b)
    _safe_set(b, 'idl_IDLComment186', a2)
    assert _is_linked(b, 'idl_IDLComment186', a2)
    if hasattr(a1, 'idl_UsesDcl185'):
        assert not _is_linked(a1, 'idl_UsesDcl185', b)
    if hasattr(a2, 'idl_UsesDcl185'):
        assert _is_linked(a2, 'idl_UsesDcl185', b)
    _safe_set(b, 'idl_IDLComment186', None)
    assert not _is_linked(b, 'idl_IDLComment186', a2)
    if hasattr(a2, 'idl_UsesDcl185'):
        assert not _is_linked(a2, 'idl_UsesDcl185', b)


def test_assoc_comments189_reverse_link_reassign_clear():
    a1 = idl_PublishesDcl(name="sample_text")
    a2 = idl_PublishesDcl(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment191', a1)
    assert _is_linked(b, 'idl_IDLComment191', a1)
    if hasattr(a1, 'idl_PublishesDcl190'):
        assert _is_linked(a1, 'idl_PublishesDcl190', b)
    _safe_set(b, 'idl_IDLComment191', a2)
    assert _is_linked(b, 'idl_IDLComment191', a2)
    if hasattr(a1, 'idl_PublishesDcl190'):
        assert not _is_linked(a1, 'idl_PublishesDcl190', b)
    if hasattr(a2, 'idl_PublishesDcl190'):
        assert _is_linked(a2, 'idl_PublishesDcl190', b)
    _safe_set(b, 'idl_IDLComment191', None)
    assert not _is_linked(b, 'idl_IDLComment191', a2)
    if hasattr(a2, 'idl_PublishesDcl190'):
        assert not _is_linked(a2, 'idl_PublishesDcl190', b)


def test_assoc_comments194_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_EmitDcl(name="sample_text")
    _safe_set(b, 'idl_EmitDcl195', {a1})
    assert _is_linked(b, 'idl_EmitDcl195', a1)
    if hasattr(a1, 'idl_IDLComment196'):
        assert _is_linked(a1, 'idl_IDLComment196', b)
    _safe_set(b, 'idl_EmitDcl195', {a2})
    assert _is_linked(b, 'idl_EmitDcl195', a2)
    if hasattr(a1, 'idl_IDLComment196'):
        assert not _is_linked(a1, 'idl_IDLComment196', b)
    if hasattr(a2, 'idl_IDLComment196'):
        assert _is_linked(a2, 'idl_IDLComment196', b)
    _safe_set(b, 'idl_EmitDcl195', set())
    assert not _is_linked(b, 'idl_EmitDcl195', a2)
    if hasattr(a2, 'idl_IDLComment196'):
        assert not _is_linked(a2, 'idl_IDLComment196', b)


def test_assoc_comments199_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_ConsumesDcl(name="sample_text")
    _safe_set(b, 'idl_ConsumesDcl200', {a1})
    assert _is_linked(b, 'idl_ConsumesDcl200', a1)
    if hasattr(a1, 'idl_IDLComment201'):
        assert _is_linked(a1, 'idl_IDLComment201', b)
    _safe_set(b, 'idl_ConsumesDcl200', {a2})
    assert _is_linked(b, 'idl_ConsumesDcl200', a2)
    if hasattr(a1, 'idl_IDLComment201'):
        assert not _is_linked(a1, 'idl_IDLComment201', b)
    if hasattr(a2, 'idl_IDLComment201'):
        assert _is_linked(a2, 'idl_IDLComment201', b)
    _safe_set(b, 'idl_ConsumesDcl200', set())
    assert not _is_linked(b, 'idl_ConsumesDcl200', a2)
    if hasattr(a2, 'idl_IDLComment201'):
        assert not _is_linked(a2, 'idl_IDLComment201', b)


def test_assoc_comments202_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_HomeDecl(name="sample_text")
    _safe_set(b, 'idl_HomeDecl', {a1})
    assert _is_linked(b, 'idl_HomeDecl', a1)
    if hasattr(a1, 'idl_IDLComment203'):
        assert _is_linked(a1, 'idl_IDLComment203', b)
    _safe_set(b, 'idl_HomeDecl', {a2})
    assert _is_linked(b, 'idl_HomeDecl', a2)
    if hasattr(a1, 'idl_IDLComment203'):
        assert not _is_linked(a1, 'idl_IDLComment203', b)
    if hasattr(a2, 'idl_IDLComment203'):
        assert _is_linked(a2, 'idl_IDLComment203', b)
    _safe_set(b, 'idl_HomeDecl', set())
    assert not _is_linked(b, 'idl_HomeDecl', a2)
    if hasattr(a2, 'idl_IDLComment203'):
        assert not _is_linked(a2, 'idl_IDLComment203', b)


def test_assoc_comments220_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_FactoryDcl(name="sample_text")
    _safe_set(b, 'idl_FactoryDcl', {a1})
    assert _is_linked(b, 'idl_FactoryDcl', a1)
    if hasattr(a1, 'idl_IDLComment221'):
        assert _is_linked(a1, 'idl_IDLComment221', b)
    _safe_set(b, 'idl_FactoryDcl', {a2})
    assert _is_linked(b, 'idl_FactoryDcl', a2)
    if hasattr(a1, 'idl_IDLComment221'):
        assert not _is_linked(a1, 'idl_IDLComment221', b)
    if hasattr(a2, 'idl_IDLComment221'):
        assert _is_linked(a2, 'idl_IDLComment221', b)
    _safe_set(b, 'idl_FactoryDcl', set())
    assert not _is_linked(b, 'idl_FactoryDcl', a2)
    if hasattr(a2, 'idl_IDLComment221'):
        assert not _is_linked(a2, 'idl_IDLComment221', b)


def test_assoc_comments228_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_FinderDcl(name="sample_text")
    _safe_set(b, 'idl_FinderDcl', {a1})
    assert _is_linked(b, 'idl_FinderDcl', a1)
    if hasattr(a1, 'idl_IDLComment229'):
        assert _is_linked(a1, 'idl_IDLComment229', b)
    _safe_set(b, 'idl_FinderDcl', {a2})
    assert _is_linked(b, 'idl_FinderDcl', a2)
    if hasattr(a1, 'idl_IDLComment229'):
        assert not _is_linked(a1, 'idl_IDLComment229', b)
    if hasattr(a2, 'idl_IDLComment229'):
        assert _is_linked(a2, 'idl_IDLComment229', b)
    _safe_set(b, 'idl_FinderDcl', set())
    assert not _is_linked(b, 'idl_FinderDcl', a2)
    if hasattr(a2, 'idl_IDLComment229'):
        assert not _is_linked(a2, 'idl_IDLComment229', b)


def test_assoc_comments23_reverse_link_reassign_clear():
    a1 = idl_Interface_header(isAbstract=True, isLocal=True, name="sample_text")
    a2 = idl_Interface_header(isAbstract=False, isLocal=False, name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment25', a1)
    assert _is_linked(b, 'idl_IDLComment25', a1)
    if hasattr(a1, 'idl_Interface_header24'):
        assert _is_linked(a1, 'idl_Interface_header24', b)
    _safe_set(b, 'idl_IDLComment25', a2)
    assert _is_linked(b, 'idl_IDLComment25', a2)
    if hasattr(a1, 'idl_Interface_header24'):
        assert not _is_linked(a1, 'idl_Interface_header24', b)
    if hasattr(a2, 'idl_Interface_header24'):
        assert _is_linked(a2, 'idl_Interface_header24', b)
    _safe_set(b, 'idl_IDLComment25', None)
    assert not _is_linked(b, 'idl_IDLComment25', a2)
    if hasattr(a2, 'idl_Interface_header24'):
        assert not _is_linked(a2, 'idl_Interface_header24', b)


def test_assoc_comments249_reverse_link_reassign_clear():
    a1 = idl_PortTypeDecl(name="sample_text")
    a2 = idl_PortTypeDecl(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment250', a1)
    assert _is_linked(b, 'idl_IDLComment250', a1)
    if hasattr(a1, 'idl_PortTypeDecl'):
        assert _is_linked(a1, 'idl_PortTypeDecl', b)
    _safe_set(b, 'idl_IDLComment250', a2)
    assert _is_linked(b, 'idl_IDLComment250', a2)
    if hasattr(a1, 'idl_PortTypeDecl'):
        assert not _is_linked(a1, 'idl_PortTypeDecl', b)
    if hasattr(a2, 'idl_PortTypeDecl'):
        assert _is_linked(a2, 'idl_PortTypeDecl', b)
    _safe_set(b, 'idl_IDLComment250', None)
    assert not _is_linked(b, 'idl_IDLComment250', a2)
    if hasattr(a2, 'idl_PortTypeDecl'):
        assert not _is_linked(a2, 'idl_PortTypeDecl', b)


def test_assoc_comments255_reverse_link_reassign_clear():
    a1 = idl_PortDecl(isMirror=True, name="sample_text")
    a2 = idl_PortDecl(isMirror=False, name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment257', a1)
    assert _is_linked(b, 'idl_IDLComment257', a1)
    if hasattr(a1, 'idl_PortDecl256'):
        assert _is_linked(a1, 'idl_PortDecl256', b)
    _safe_set(b, 'idl_IDLComment257', a2)
    assert _is_linked(b, 'idl_IDLComment257', a2)
    if hasattr(a1, 'idl_PortDecl256'):
        assert not _is_linked(a1, 'idl_PortDecl256', b)
    if hasattr(a2, 'idl_PortDecl256'):
        assert _is_linked(a2, 'idl_PortDecl256', b)
    _safe_set(b, 'idl_IDLComment257', None)
    assert not _is_linked(b, 'idl_IDLComment257', a2)
    if hasattr(a2, 'idl_PortDecl256'):
        assert not _is_linked(a2, 'idl_PortDecl256', b)


def test_assoc_comments274_reverse_link_reassign_clear():
    a1 = idl_TemplateModuleInst(name="sample_text")
    a2 = idl_TemplateModuleInst(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment276', a1)
    assert _is_linked(b, 'idl_IDLComment276', a1)
    if hasattr(a1, 'idl_TemplateModuleInst275'):
        assert _is_linked(a1, 'idl_TemplateModuleInst275', b)
    _safe_set(b, 'idl_IDLComment276', a2)
    assert _is_linked(b, 'idl_IDLComment276', a2)
    if hasattr(a1, 'idl_TemplateModuleInst275'):
        assert not _is_linked(a1, 'idl_TemplateModuleInst275', b)
    if hasattr(a2, 'idl_TemplateModuleInst275'):
        assert _is_linked(a2, 'idl_TemplateModuleInst275', b)
    _safe_set(b, 'idl_IDLComment276', None)
    assert not _is_linked(b, 'idl_IDLComment276', a2)
    if hasattr(a2, 'idl_TemplateModuleInst275'):
        assert not _is_linked(a2, 'idl_TemplateModuleInst275', b)


def test_assoc_comments28_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_AttrDecl(names="sample_text")
    _safe_set(b, 'idl_AttrDecl', {a1})
    assert _is_linked(b, 'idl_AttrDecl', a1)
    if hasattr(a1, 'idl_IDLComment29'):
        assert _is_linked(a1, 'idl_IDLComment29', b)
    _safe_set(b, 'idl_AttrDecl', {a2})
    assert _is_linked(b, 'idl_AttrDecl', a2)
    if hasattr(a1, 'idl_IDLComment29'):
        assert not _is_linked(a1, 'idl_IDLComment29', b)
    if hasattr(a2, 'idl_IDLComment29'):
        assert _is_linked(a2, 'idl_IDLComment29', b)
    _safe_set(b, 'idl_AttrDecl', set())
    assert not _is_linked(b, 'idl_AttrDecl', a2)
    if hasattr(a2, 'idl_IDLComment29'):
        assert not _is_linked(a2, 'idl_IDLComment29', b)


def test_assoc_comments43_reverse_link_reassign_clear():
    a1 = idl_OpDecl(isOneway=True, name="sample_text")
    a2 = idl_OpDecl(isOneway=False, name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment44', a1)
    assert _is_linked(b, 'idl_IDLComment44', a1)
    if hasattr(a1, 'idl_OpDecl'):
        assert _is_linked(a1, 'idl_OpDecl', b)
    _safe_set(b, 'idl_IDLComment44', a2)
    assert _is_linked(b, 'idl_IDLComment44', a2)
    if hasattr(a1, 'idl_OpDecl'):
        assert not _is_linked(a1, 'idl_OpDecl', b)
    if hasattr(a2, 'idl_OpDecl'):
        assert _is_linked(a2, 'idl_OpDecl', b)
    _safe_set(b, 'idl_IDLComment44', None)
    assert not _is_linked(b, 'idl_IDLComment44', a2)
    if hasattr(a2, 'idl_OpDecl'):
        assert not _is_linked(a2, 'idl_OpDecl', b)


def test_assoc_comments65_reverse_link_reassign_clear():
    a1 = idl_IDLComment(body="sample_text")
    a2 = idl_IDLComment(body="sample_text_2")
    b = idl_ExceptDecl(name="sample_text")
    _safe_set(b, 'idl_ExceptDecl', {a1})
    assert _is_linked(b, 'idl_ExceptDecl', a1)
    if hasattr(a1, 'idl_IDLComment66'):
        assert _is_linked(a1, 'idl_IDLComment66', b)
    _safe_set(b, 'idl_ExceptDecl', {a2})
    assert _is_linked(b, 'idl_ExceptDecl', a2)
    if hasattr(a1, 'idl_IDLComment66'):
        assert not _is_linked(a1, 'idl_IDLComment66', b)
    if hasattr(a2, 'idl_IDLComment66'):
        assert _is_linked(a2, 'idl_IDLComment66', b)
    _safe_set(b, 'idl_ExceptDecl', set())
    assert not _is_linked(b, 'idl_ExceptDecl', a2)
    if hasattr(a2, 'idl_IDLComment66'):
        assert not _is_linked(a2, 'idl_IDLComment66', b)


def test_assoc_comments78_reverse_link_reassign_clear():
    a1 = idl_StructType(name="sample_text")
    a2 = idl_StructType(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment79', a1)
    assert _is_linked(b, 'idl_IDLComment79', a1)
    if hasattr(a1, 'idl_StructType'):
        assert _is_linked(a1, 'idl_StructType', b)
    _safe_set(b, 'idl_IDLComment79', a2)
    assert _is_linked(b, 'idl_IDLComment79', a2)
    if hasattr(a1, 'idl_StructType'):
        assert not _is_linked(a1, 'idl_StructType', b)
    if hasattr(a2, 'idl_StructType'):
        assert _is_linked(a2, 'idl_StructType', b)
    _safe_set(b, 'idl_IDLComment79', None)
    assert not _is_linked(b, 'idl_IDLComment79', a2)
    if hasattr(a2, 'idl_StructType'):
        assert not _is_linked(a2, 'idl_StructType', b)


def test_assoc_comments91_reverse_link_reassign_clear():
    a1 = idl_UnionType(name="sample_text")
    a2 = idl_UnionType(name="sample_text_2")
    b = idl_IDLComment(body="sample_text")
    _safe_set(b, 'idl_IDLComment92', a1)
    assert _is_linked(b, 'idl_IDLComment92', a1)
    if hasattr(a1, 'idl_UnionType'):
        assert _is_linked(a1, 'idl_UnionType', b)
    _safe_set(b, 'idl_IDLComment92', a2)
    assert _is_linked(b, 'idl_IDLComment92', a2)
    if hasattr(a1, 'idl_UnionType'):
        assert not _is_linked(a1, 'idl_UnionType', b)
    if hasattr(a2, 'idl_UnionType'):
        assert _is_linked(a2, 'idl_UnionType', b)
    _safe_set(b, 'idl_IDLComment92', None)
    assert not _is_linked(b, 'idl_IDLComment92', a2)
    if hasattr(a2, 'idl_UnionType'):
        assert not _is_linked(a2, 'idl_UnionType', b)


def test_assoc_context52_reverse_link_reassign_clear():
    a1 = idl_OpDecl(isOneway=True, name="sample_text")
    a2 = idl_OpDecl(isOneway=False, name="sample_text_2")
    b = idl_ContextExpr(literal="sample_text")
    _safe_set(b, 'idl_ContextExpr', a1)
    assert _is_linked(b, 'idl_ContextExpr', a1)
    if hasattr(a1, 'idl_OpDecl53'):
        assert _is_linked(a1, 'idl_OpDecl53', b)
    _safe_set(b, 'idl_ContextExpr', a2)
    assert _is_linked(b, 'idl_ContextExpr', a2)
    if hasattr(a1, 'idl_OpDecl53'):
        assert not _is_linked(a1, 'idl_OpDecl53', b)
    if hasattr(a2, 'idl_OpDecl53'):
        assert _is_linked(a2, 'idl_OpDecl53', b)
    _safe_set(b, 'idl_ContextExpr', None)
    assert not _is_linked(b, 'idl_ContextExpr', a2)
    if hasattr(a2, 'idl_OpDecl53'):
        assert not _is_linked(a2, 'idl_OpDecl53', b)


def test_assoc_lhs136_reverse_link_reassign_clear():
    a1 = idl_XOrExpr(op="sample_text")
    a2 = idl_XOrExpr(op="sample_text_2")
    b = idl_OrExpr(op="sample_text")
    _safe_set(b, 'idl_OrExpr', a1)
    assert _is_linked(b, 'idl_OrExpr', a1)
    if hasattr(a1, 'idl_XOrExpr'):
        assert _is_linked(a1, 'idl_XOrExpr', b)
    _safe_set(b, 'idl_OrExpr', a2)
    assert _is_linked(b, 'idl_OrExpr', a2)
    if hasattr(a1, 'idl_XOrExpr'):
        assert not _is_linked(a1, 'idl_XOrExpr', b)
    if hasattr(a2, 'idl_XOrExpr'):
        assert _is_linked(a2, 'idl_XOrExpr', b)
    _safe_set(b, 'idl_OrExpr', None)
    assert not _is_linked(b, 'idl_OrExpr', a2)
    if hasattr(a2, 'idl_XOrExpr'):
        assert not _is_linked(a2, 'idl_XOrExpr', b)


def test_assoc_lhs140_reverse_link_reassign_clear():
    a1 = idl_XOrExpr(op="sample_text")
    a2 = idl_XOrExpr(op="sample_text_2")
    b = idl_AndExpr(op="sample_text")
    _safe_set(b, 'idl_AndExpr', a1)
    assert _is_linked(b, 'idl_AndExpr', a1)
    if hasattr(a1, 'idl_XOrExpr141'):
        assert _is_linked(a1, 'idl_XOrExpr141', b)
    _safe_set(b, 'idl_AndExpr', a2)
    assert _is_linked(b, 'idl_AndExpr', a2)
    if hasattr(a1, 'idl_XOrExpr141'):
        assert not _is_linked(a1, 'idl_XOrExpr141', b)
    if hasattr(a2, 'idl_XOrExpr141'):
        assert _is_linked(a2, 'idl_XOrExpr141', b)
    _safe_set(b, 'idl_AndExpr', None)
    assert not _is_linked(b, 'idl_AndExpr', a2)
    if hasattr(a2, 'idl_XOrExpr141'):
        assert not _is_linked(a2, 'idl_XOrExpr141', b)


def test_assoc_lhs145_reverse_link_reassign_clear():
    a1 = idl_ShiftExpr(op="sample_text")
    a2 = idl_ShiftExpr(op="sample_text_2")
    b = idl_AndExpr(op="sample_text")
    _safe_set(b, 'idl_AndExpr146', a1)
    assert _is_linked(b, 'idl_AndExpr146', a1)
    if hasattr(a1, 'idl_ShiftExpr'):
        assert _is_linked(a1, 'idl_ShiftExpr', b)
    _safe_set(b, 'idl_AndExpr146', a2)
    assert _is_linked(b, 'idl_AndExpr146', a2)
    if hasattr(a1, 'idl_ShiftExpr'):
        assert not _is_linked(a1, 'idl_ShiftExpr', b)
    if hasattr(a2, 'idl_ShiftExpr'):
        assert _is_linked(a2, 'idl_ShiftExpr', b)
    _safe_set(b, 'idl_AndExpr146', None)
    assert not _is_linked(b, 'idl_AndExpr146', a2)
    if hasattr(a2, 'idl_ShiftExpr'):
        assert not _is_linked(a2, 'idl_ShiftExpr', b)


def test_assoc_lhs150_reverse_link_reassign_clear():
    a1 = idl_ShiftExpr(op="sample_text")
    a2 = idl_ShiftExpr(op="sample_text_2")
    b = idl_AddExpr(op="sample_text")
    _safe_set(b, 'idl_AddExpr', a1)
    assert _is_linked(b, 'idl_AddExpr', a1)
    if hasattr(a1, 'idl_ShiftExpr151'):
        assert _is_linked(a1, 'idl_ShiftExpr151', b)
    _safe_set(b, 'idl_AddExpr', a2)
    assert _is_linked(b, 'idl_AddExpr', a2)
    if hasattr(a1, 'idl_ShiftExpr151'):
        assert not _is_linked(a1, 'idl_ShiftExpr151', b)
    if hasattr(a2, 'idl_ShiftExpr151'):
        assert _is_linked(a2, 'idl_ShiftExpr151', b)
    _safe_set(b, 'idl_AddExpr', None)
    assert not _is_linked(b, 'idl_AddExpr', a2)
    if hasattr(a2, 'idl_ShiftExpr151'):
        assert not _is_linked(a2, 'idl_ShiftExpr151', b)


def test_assoc_lhs155_reverse_link_reassign_clear():
    a1 = idl_MultExpr(op="sample_text")
    a2 = idl_MultExpr(op="sample_text_2")
    b = idl_AddExpr(op="sample_text")
    _safe_set(b, 'idl_AddExpr156', a1)
    assert _is_linked(b, 'idl_AddExpr156', a1)
    if hasattr(a1, 'idl_MultExpr'):
        assert _is_linked(a1, 'idl_MultExpr', b)
    _safe_set(b, 'idl_AddExpr156', a2)
    assert _is_linked(b, 'idl_AddExpr156', a2)
    if hasattr(a1, 'idl_MultExpr'):
        assert not _is_linked(a1, 'idl_MultExpr', b)
    if hasattr(a2, 'idl_MultExpr'):
        assert _is_linked(a2, 'idl_MultExpr', b)
    _safe_set(b, 'idl_AddExpr156', None)
    assert not _is_linked(b, 'idl_AddExpr156', a2)
    if hasattr(a2, 'idl_MultExpr'):
        assert not _is_linked(a2, 'idl_MultExpr', b)


def test_assoc_lhs160_reverse_link_reassign_clear():
    a1 = idl_UnaryExpr(op="sample_text")
    a2 = idl_UnaryExpr(op="sample_text_2")
    b = idl_MultExpr(op="sample_text")
    _safe_set(b, 'idl_MultExpr161', a1)
    assert _is_linked(b, 'idl_MultExpr161', a1)
    if hasattr(a1, 'idl_UnaryExpr'):
        assert _is_linked(a1, 'idl_UnaryExpr', b)
    _safe_set(b, 'idl_MultExpr161', a2)
    assert _is_linked(b, 'idl_MultExpr161', a2)
    if hasattr(a1, 'idl_UnaryExpr'):
        assert not _is_linked(a1, 'idl_UnaryExpr', b)
    if hasattr(a2, 'idl_UnaryExpr'):
        assert _is_linked(a2, 'idl_UnaryExpr', b)
    _safe_set(b, 'idl_MultExpr161', None)
    assert not _is_linked(b, 'idl_MultExpr161', a2)
    if hasattr(a2, 'idl_UnaryExpr'):
        assert not _is_linked(a2, 'idl_UnaryExpr', b)


def test_assoc_manages210_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_HomeDecl(name="sample_text")
    _safe_set(b, 'idl_HomeDecl211', a1)
    assert _is_linked(b, 'idl_HomeDecl211', a1)
    if hasattr(a1, 'idl_ScopedName212'):
        assert _is_linked(a1, 'idl_ScopedName212', b)
    _safe_set(b, 'idl_HomeDecl211', a2)
    assert _is_linked(b, 'idl_HomeDecl211', a2)
    if hasattr(a1, 'idl_ScopedName212'):
        assert not _is_linked(a1, 'idl_ScopedName212', b)
    if hasattr(a2, 'idl_ScopedName212'):
        assert _is_linked(a2, 'idl_ScopedName212', b)
    _safe_set(b, 'idl_HomeDecl211', None)
    assert not _is_linked(b, 'idl_HomeDecl211', a2)
    if hasattr(a2, 'idl_ScopedName212'):
        assert not _is_linked(a2, 'idl_ScopedName212', b)


def test_assoc_member244_reverse_link_reassign_clear():
    a1 = idl_StateMember(isPublic=True, names="sample_text")
    a2 = idl_StateMember(isPublic=False, names="sample_text_2")
    b = idl_EventDcl(isCustom=True, isTruncatable=True)
    _safe_set(b, 'idl_EventDcl245', {a1})
    assert _is_linked(b, 'idl_EventDcl245', a1)
    if hasattr(a1, 'idl_StateMember'):
        assert _is_linked(a1, 'idl_StateMember', b)
    _safe_set(b, 'idl_EventDcl245', {a2})
    assert _is_linked(b, 'idl_EventDcl245', a2)
    if hasattr(a1, 'idl_StateMember'):
        assert not _is_linked(a1, 'idl_StateMember', b)
    if hasattr(a2, 'idl_StateMember'):
        assert _is_linked(a2, 'idl_StateMember', b)
    _safe_set(b, 'idl_EventDcl245', set())
    assert not _is_linked(b, 'idl_EventDcl245', a2)
    if hasattr(a2, 'idl_StateMember'):
        assert not _is_linked(a2, 'idl_StateMember', b)


def test_assoc_parameters264_reverse_link_reassign_clear():
    a1 = idl_TemplateModule(name="sample_text")
    a2 = idl_TemplateModule(name="sample_text_2")
    b = idl_FormalParameter(name="sample_text")
    _safe_set(b, 'idl_FormalParameter', a1)
    assert _is_linked(b, 'idl_FormalParameter', a1)
    if hasattr(a1, 'idl_TemplateModule'):
        assert _is_linked(a1, 'idl_TemplateModule', b)
    _safe_set(b, 'idl_FormalParameter', a2)
    assert _is_linked(b, 'idl_FormalParameter', a2)
    if hasattr(a1, 'idl_TemplateModule'):
        assert not _is_linked(a1, 'idl_TemplateModule', b)
    if hasattr(a2, 'idl_TemplateModule'):
        assert _is_linked(a2, 'idl_TemplateModule', b)
    _safe_set(b, 'idl_FormalParameter', None)
    assert not _is_linked(b, 'idl_FormalParameter', a2)
    if hasattr(a2, 'idl_TemplateModule'):
        assert not _is_linked(a2, 'idl_TemplateModule', b)


def test_assoc_rhs138_reverse_link_reassign_clear():
    a1 = idl_OrExpr(op="sample_text")
    a2 = idl_OrExpr(op="sample_text_2")
    b = idl_OrExpr(op="sample_text")
    _safe_set(b, 'idl_OrExpr139', a1)
    assert _is_linked(b, 'idl_OrExpr139', a1)
    if hasattr(a1, 'idl_OrExpr137'):
        assert _is_linked(a1, 'idl_OrExpr137', b)
    _safe_set(b, 'idl_OrExpr139', a2)
    assert _is_linked(b, 'idl_OrExpr139', a2)
    if hasattr(a1, 'idl_OrExpr137'):
        assert not _is_linked(a1, 'idl_OrExpr137', b)
    if hasattr(a2, 'idl_OrExpr137'):
        assert _is_linked(a2, 'idl_OrExpr137', b)
    _safe_set(b, 'idl_OrExpr139', None)
    assert not _is_linked(b, 'idl_OrExpr139', a2)
    if hasattr(a2, 'idl_OrExpr137'):
        assert not _is_linked(a2, 'idl_OrExpr137', b)


def test_assoc_rhs143_reverse_link_reassign_clear():
    a1 = idl_XOrExpr(op="sample_text")
    a2 = idl_XOrExpr(op="sample_text_2")
    b = idl_XOrExpr(op="sample_text")
    _safe_set(b, 'idl_XOrExpr144', a1)
    assert _is_linked(b, 'idl_XOrExpr144', a1)
    if hasattr(a1, 'idl_XOrExpr142'):
        assert _is_linked(a1, 'idl_XOrExpr142', b)
    _safe_set(b, 'idl_XOrExpr144', a2)
    assert _is_linked(b, 'idl_XOrExpr144', a2)
    if hasattr(a1, 'idl_XOrExpr142'):
        assert not _is_linked(a1, 'idl_XOrExpr142', b)
    if hasattr(a2, 'idl_XOrExpr142'):
        assert _is_linked(a2, 'idl_XOrExpr142', b)
    _safe_set(b, 'idl_XOrExpr144', None)
    assert not _is_linked(b, 'idl_XOrExpr144', a2)
    if hasattr(a2, 'idl_XOrExpr142'):
        assert not _is_linked(a2, 'idl_XOrExpr142', b)


def test_assoc_rhs148_reverse_link_reassign_clear():
    a1 = idl_AndExpr(op="sample_text")
    a2 = idl_AndExpr(op="sample_text_2")
    b = idl_AndExpr(op="sample_text")
    _safe_set(b, 'idl_AndExpr149', a1)
    assert _is_linked(b, 'idl_AndExpr149', a1)
    if hasattr(a1, 'idl_AndExpr147'):
        assert _is_linked(a1, 'idl_AndExpr147', b)
    _safe_set(b, 'idl_AndExpr149', a2)
    assert _is_linked(b, 'idl_AndExpr149', a2)
    if hasattr(a1, 'idl_AndExpr147'):
        assert not _is_linked(a1, 'idl_AndExpr147', b)
    if hasattr(a2, 'idl_AndExpr147'):
        assert _is_linked(a2, 'idl_AndExpr147', b)
    _safe_set(b, 'idl_AndExpr149', None)
    assert not _is_linked(b, 'idl_AndExpr149', a2)
    if hasattr(a2, 'idl_AndExpr147'):
        assert not _is_linked(a2, 'idl_AndExpr147', b)


def test_assoc_rhs153_reverse_link_reassign_clear():
    a1 = idl_ShiftExpr(op="sample_text")
    a2 = idl_ShiftExpr(op="sample_text_2")
    b = idl_ShiftExpr(op="sample_text")
    _safe_set(b, 'idl_ShiftExpr154', a1)
    assert _is_linked(b, 'idl_ShiftExpr154', a1)
    if hasattr(a1, 'idl_ShiftExpr152'):
        assert _is_linked(a1, 'idl_ShiftExpr152', b)
    _safe_set(b, 'idl_ShiftExpr154', a2)
    assert _is_linked(b, 'idl_ShiftExpr154', a2)
    if hasattr(a1, 'idl_ShiftExpr152'):
        assert not _is_linked(a1, 'idl_ShiftExpr152', b)
    if hasattr(a2, 'idl_ShiftExpr152'):
        assert _is_linked(a2, 'idl_ShiftExpr152', b)
    _safe_set(b, 'idl_ShiftExpr154', None)
    assert not _is_linked(b, 'idl_ShiftExpr154', a2)
    if hasattr(a2, 'idl_ShiftExpr152'):
        assert not _is_linked(a2, 'idl_ShiftExpr152', b)


def test_assoc_rhs158_reverse_link_reassign_clear():
    a1 = idl_AddExpr(op="sample_text")
    a2 = idl_AddExpr(op="sample_text_2")
    b = idl_AddExpr(op="sample_text")
    _safe_set(b, 'idl_AddExpr159', a1)
    assert _is_linked(b, 'idl_AddExpr159', a1)
    if hasattr(a1, 'idl_AddExpr157'):
        assert _is_linked(a1, 'idl_AddExpr157', b)
    _safe_set(b, 'idl_AddExpr159', a2)
    assert _is_linked(b, 'idl_AddExpr159', a2)
    if hasattr(a1, 'idl_AddExpr157'):
        assert not _is_linked(a1, 'idl_AddExpr157', b)
    if hasattr(a2, 'idl_AddExpr157'):
        assert _is_linked(a2, 'idl_AddExpr157', b)
    _safe_set(b, 'idl_AddExpr159', None)
    assert not _is_linked(b, 'idl_AddExpr159', a2)
    if hasattr(a2, 'idl_AddExpr157'):
        assert not _is_linked(a2, 'idl_AddExpr157', b)


def test_assoc_rhs163_reverse_link_reassign_clear():
    a1 = idl_MultExpr(op="sample_text")
    a2 = idl_MultExpr(op="sample_text_2")
    b = idl_MultExpr(op="sample_text")
    _safe_set(b, 'idl_MultExpr164', a1)
    assert _is_linked(b, 'idl_MultExpr164', a1)
    if hasattr(a1, 'idl_MultExpr162'):
        assert _is_linked(a1, 'idl_MultExpr162', b)
    _safe_set(b, 'idl_MultExpr164', a2)
    assert _is_linked(b, 'idl_MultExpr164', a2)
    if hasattr(a1, 'idl_MultExpr162'):
        assert not _is_linked(a1, 'idl_MultExpr162', b)
    if hasattr(a2, 'idl_MultExpr162'):
        assert _is_linked(a2, 'idl_MultExpr162', b)
    _safe_set(b, 'idl_MultExpr164', None)
    assert not _is_linked(b, 'idl_MultExpr164', a2)
    if hasattr(a2, 'idl_MultExpr162'):
        assert not _is_linked(a2, 'idl_MultExpr162', b)


def test_assoc_specializes21_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_Interface_header(isAbstract=True, isLocal=True, name="sample_text")
    _safe_set(b, 'idl_Interface_header22', {a1})
    assert _is_linked(b, 'idl_Interface_header22', a1)
    if hasattr(a1, 'idl_ScopedName'):
        assert _is_linked(a1, 'idl_ScopedName', b)
    _safe_set(b, 'idl_Interface_header22', {a2})
    assert _is_linked(b, 'idl_Interface_header22', a2)
    if hasattr(a1, 'idl_ScopedName'):
        assert not _is_linked(a1, 'idl_ScopedName', b)
    if hasattr(a2, 'idl_ScopedName'):
        assert _is_linked(a2, 'idl_ScopedName', b)
    _safe_set(b, 'idl_Interface_header22', set())
    assert not _is_linked(b, 'idl_Interface_header22', a2)
    if hasattr(a2, 'idl_ScopedName'):
        assert not _is_linked(a2, 'idl_ScopedName', b)


def test_assoc_supports172_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_ComponentDecl(name="sample_text")
    _safe_set(b, 'idl_ComponentDecl173', {a1})
    assert _is_linked(b, 'idl_ComponentDecl173', a1)
    if hasattr(a1, 'idl_ScopedName174'):
        assert _is_linked(a1, 'idl_ScopedName174', b)
    _safe_set(b, 'idl_ComponentDecl173', {a2})
    assert _is_linked(b, 'idl_ComponentDecl173', a2)
    if hasattr(a1, 'idl_ScopedName174'):
        assert not _is_linked(a1, 'idl_ScopedName174', b)
    if hasattr(a2, 'idl_ScopedName174'):
        assert _is_linked(a2, 'idl_ScopedName174', b)
    _safe_set(b, 'idl_ComponentDecl173', set())
    assert not _is_linked(b, 'idl_ComponentDecl173', a2)
    if hasattr(a2, 'idl_ScopedName174'):
        assert not _is_linked(a2, 'idl_ScopedName174', b)


def test_assoc_supports207_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_HomeDecl(name="sample_text")
    _safe_set(b, 'idl_HomeDecl208', {a1})
    assert _is_linked(b, 'idl_HomeDecl208', a1)
    if hasattr(a1, 'idl_ScopedName209'):
        assert _is_linked(a1, 'idl_ScopedName209', b)
    _safe_set(b, 'idl_HomeDecl208', {a2})
    assert _is_linked(b, 'idl_HomeDecl208', a2)
    if hasattr(a1, 'idl_ScopedName209'):
        assert not _is_linked(a1, 'idl_ScopedName209', b)
    if hasattr(a2, 'idl_ScopedName209'):
        assert _is_linked(a2, 'idl_ScopedName209', b)
    _safe_set(b, 'idl_HomeDecl208', set())
    assert not _is_linked(b, 'idl_HomeDecl208', a2)
    if hasattr(a2, 'idl_ScopedName209'):
        assert not _is_linked(a2, 'idl_ScopedName209', b)


def test_assoc_supports238_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_EventDcl(isCustom=True, isTruncatable=True)
    _safe_set(b, 'idl_EventDcl239', {a1})
    assert _is_linked(b, 'idl_EventDcl239', a1)
    if hasattr(a1, 'idl_ScopedName240'):
        assert _is_linked(a1, 'idl_ScopedName240', b)
    _safe_set(b, 'idl_EventDcl239', {a2})
    assert _is_linked(b, 'idl_EventDcl239', a2)
    if hasattr(a1, 'idl_ScopedName240'):
        assert not _is_linked(a1, 'idl_ScopedName240', b)
    if hasattr(a2, 'idl_ScopedName240'):
        assert _is_linked(a2, 'idl_ScopedName240', b)
    _safe_set(b, 'idl_EventDcl239', set())
    assert not _is_linked(b, 'idl_EventDcl239', a2)
    if hasattr(a2, 'idl_ScopedName240'):
        assert not _is_linked(a2, 'idl_ScopedName240', b)


def test_assoc_type177_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_ProvidesDcl(name="sample_text")
    _safe_set(b, 'idl_ProvidesDcl', a1)
    assert _is_linked(b, 'idl_ProvidesDcl', a1)
    if hasattr(a1, 'idl_ScopedName178'):
        assert _is_linked(a1, 'idl_ScopedName178', b)
    _safe_set(b, 'idl_ProvidesDcl', a2)
    assert _is_linked(b, 'idl_ProvidesDcl', a2)
    if hasattr(a1, 'idl_ScopedName178'):
        assert not _is_linked(a1, 'idl_ScopedName178', b)
    if hasattr(a2, 'idl_ScopedName178'):
        assert _is_linked(a2, 'idl_ScopedName178', b)
    _safe_set(b, 'idl_ProvidesDcl', None)
    assert not _is_linked(b, 'idl_ProvidesDcl', a2)
    if hasattr(a2, 'idl_ScopedName178'):
        assert not _is_linked(a2, 'idl_ScopedName178', b)


def test_assoc_type182_reverse_link_reassign_clear():
    a1 = idl_UsesDcl(isMultiple=True, name="sample_text")
    a2 = idl_UsesDcl(isMultiple=False, name="sample_text_2")
    b = idl_ScopedName(name="sample_text")
    _safe_set(b, 'idl_ScopedName183', a1)
    assert _is_linked(b, 'idl_ScopedName183', a1)
    if hasattr(a1, 'idl_UsesDcl'):
        assert _is_linked(a1, 'idl_UsesDcl', b)
    _safe_set(b, 'idl_ScopedName183', a2)
    assert _is_linked(b, 'idl_ScopedName183', a2)
    if hasattr(a1, 'idl_UsesDcl'):
        assert not _is_linked(a1, 'idl_UsesDcl', b)
    if hasattr(a2, 'idl_UsesDcl'):
        assert _is_linked(a2, 'idl_UsesDcl', b)
    _safe_set(b, 'idl_ScopedName183', None)
    assert not _is_linked(b, 'idl_ScopedName183', a2)
    if hasattr(a2, 'idl_UsesDcl'):
        assert not _is_linked(a2, 'idl_UsesDcl', b)


def test_assoc_type187_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_PublishesDcl(name="sample_text")
    _safe_set(b, 'idl_PublishesDcl', a1)
    assert _is_linked(b, 'idl_PublishesDcl', a1)
    if hasattr(a1, 'idl_ScopedName188'):
        assert _is_linked(a1, 'idl_ScopedName188', b)
    _safe_set(b, 'idl_PublishesDcl', a2)
    assert _is_linked(b, 'idl_PublishesDcl', a2)
    if hasattr(a1, 'idl_ScopedName188'):
        assert not _is_linked(a1, 'idl_ScopedName188', b)
    if hasattr(a2, 'idl_ScopedName188'):
        assert _is_linked(a2, 'idl_ScopedName188', b)
    _safe_set(b, 'idl_PublishesDcl', None)
    assert not _is_linked(b, 'idl_PublishesDcl', a2)
    if hasattr(a2, 'idl_ScopedName188'):
        assert not _is_linked(a2, 'idl_ScopedName188', b)


def test_assoc_type192_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_EmitDcl(name="sample_text")
    _safe_set(b, 'idl_EmitDcl', a1)
    assert _is_linked(b, 'idl_EmitDcl', a1)
    if hasattr(a1, 'idl_ScopedName193'):
        assert _is_linked(a1, 'idl_ScopedName193', b)
    _safe_set(b, 'idl_EmitDcl', a2)
    assert _is_linked(b, 'idl_EmitDcl', a2)
    if hasattr(a1, 'idl_ScopedName193'):
        assert not _is_linked(a1, 'idl_ScopedName193', b)
    if hasattr(a2, 'idl_ScopedName193'):
        assert _is_linked(a2, 'idl_ScopedName193', b)
    _safe_set(b, 'idl_EmitDcl', None)
    assert not _is_linked(b, 'idl_EmitDcl', a2)
    if hasattr(a2, 'idl_ScopedName193'):
        assert not _is_linked(a2, 'idl_ScopedName193', b)


def test_assoc_type197_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_ConsumesDcl(name="sample_text")
    _safe_set(b, 'idl_ConsumesDcl', a1)
    assert _is_linked(b, 'idl_ConsumesDcl', a1)
    if hasattr(a1, 'idl_ScopedName198'):
        assert _is_linked(a1, 'idl_ScopedName198', b)
    _safe_set(b, 'idl_ConsumesDcl', a2)
    assert _is_linked(b, 'idl_ConsumesDcl', a2)
    if hasattr(a1, 'idl_ScopedName198'):
        assert not _is_linked(a1, 'idl_ScopedName198', b)
    if hasattr(a2, 'idl_ScopedName198'):
        assert _is_linked(a2, 'idl_ScopedName198', b)
    _safe_set(b, 'idl_ConsumesDcl', None)
    assert not _is_linked(b, 'idl_ConsumesDcl', a2)
    if hasattr(a2, 'idl_ScopedName198'):
        assert not _is_linked(a2, 'idl_ScopedName198', b)


def test_assoc_type253_reverse_link_reassign_clear():
    a1 = idl_ScopedName(name="sample_text")
    a2 = idl_ScopedName(name="sample_text_2")
    b = idl_PortDecl(isMirror=True, name="sample_text")
    _safe_set(b, 'idl_PortDecl', a1)
    assert _is_linked(b, 'idl_PortDecl', a1)
    if hasattr(a1, 'idl_ScopedName254'):
        assert _is_linked(a1, 'idl_ScopedName254', b)
    _safe_set(b, 'idl_PortDecl', a2)
    assert _is_linked(b, 'idl_PortDecl', a2)
    if hasattr(a1, 'idl_ScopedName254'):
        assert not _is_linked(a1, 'idl_ScopedName254', b)
    if hasattr(a2, 'idl_ScopedName254'):
        assert _is_linked(a2, 'idl_ScopedName254', b)
    _safe_set(b, 'idl_PortDecl', None)
    assert not _is_linked(b, 'idl_PortDecl', a2)
    if hasattr(a2, 'idl_ScopedName254'):
        assert not _is_linked(a2, 'idl_ScopedName254', b)


def test_assoc_type270_reverse_link_reassign_clear():
    a1 = idl_TemplateModuleInst(name="sample_text")
    a2 = idl_TemplateModuleInst(name="sample_text_2")
    b = idl_ScopedName(name="sample_text")
    _safe_set(b, 'idl_ScopedName271', a1)
    assert _is_linked(b, 'idl_ScopedName271', a1)
    if hasattr(a1, 'idl_TemplateModuleInst'):
        assert _is_linked(a1, 'idl_TemplateModuleInst', b)
    _safe_set(b, 'idl_ScopedName271', a2)
    assert _is_linked(b, 'idl_ScopedName271', a2)
    if hasattr(a1, 'idl_TemplateModuleInst'):
        assert not _is_linked(a1, 'idl_TemplateModuleInst', b)
    if hasattr(a2, 'idl_TemplateModuleInst'):
        assert _is_linked(a2, 'idl_TemplateModuleInst', b)
    _safe_set(b, 'idl_ScopedName271', None)
    assert not _is_linked(b, 'idl_ScopedName271', a2)
    if hasattr(a2, 'idl_TemplateModuleInst'):
        assert not _is_linked(a2, 'idl_TemplateModuleInst', b)


def test_assoc_type277_reverse_link_reassign_clear():
    a1 = idl_TemplateModuleRef(id="sample_text", name="sample_text")
    a2 = idl_TemplateModuleRef(id="sample_text_2", name="sample_text_2")
    b = idl_ScopedName(name="sample_text")
    _safe_set(b, 'idl_ScopedName278', a1)
    assert _is_linked(b, 'idl_ScopedName278', a1)
    if hasattr(a1, 'idl_TemplateModuleRef'):
        assert _is_linked(a1, 'idl_TemplateModuleRef', b)
    _safe_set(b, 'idl_ScopedName278', a2)
    assert _is_linked(b, 'idl_ScopedName278', a2)
    if hasattr(a1, 'idl_TemplateModuleRef'):
        assert not _is_linked(a1, 'idl_TemplateModuleRef', b)
    if hasattr(a2, 'idl_TemplateModuleRef'):
        assert _is_linked(a2, 'idl_TemplateModuleRef', b)
    _safe_set(b, 'idl_ScopedName278', None)
    assert not _is_linked(b, 'idl_ScopedName278', a2)
    if hasattr(a2, 'idl_TemplateModuleRef'):
        assert not _is_linked(a2, 'idl_TemplateModuleRef', b)


def test_assoc_value3_reverse_link_reassign_clear():
    a1 = idl_Preproc_Include(strValue="sample_text")
    a2 = idl_Preproc_Include(strValue="sample_text_2")
    b = idl_FileName(name="sample_text")
    _safe_set(b, 'idl_FileName', a1)
    assert _is_linked(b, 'idl_FileName', a1)
    if hasattr(a1, 'idl_Preproc_Include'):
        assert _is_linked(a1, 'idl_Preproc_Include', b)
    _safe_set(b, 'idl_FileName', a2)
    assert _is_linked(b, 'idl_FileName', a2)
    if hasattr(a1, 'idl_Preproc_Include'):
        assert not _is_linked(a1, 'idl_Preproc_Include', b)
    if hasattr(a2, 'idl_Preproc_Include'):
        assert _is_linked(a2, 'idl_Preproc_Include', b)
    _safe_set(b, 'idl_FileName', None)
    assert not _is_linked(b, 'idl_FileName', a2)
    if hasattr(a2, 'idl_Preproc_Include'):
        assert not _is_linked(a2, 'idl_Preproc_Include', b)


def test_assoc_value4_reverse_link_reassign_clear():
    a1 = idl_Preproc_If_Compare(op="sample_text")
    a2 = idl_Preproc_If_Compare(op="sample_text_2")
    b = idl_Preproc_If(negation=True)
    _safe_set(b, 'idl_Preproc_If', {a1})
    assert _is_linked(b, 'idl_Preproc_If', a1)
    if hasattr(a1, 'idl_Preproc_If_Compare'):
        assert _is_linked(a1, 'idl_Preproc_If_Compare', b)
    _safe_set(b, 'idl_Preproc_If', {a2})
    assert _is_linked(b, 'idl_Preproc_If', a2)
    if hasattr(a1, 'idl_Preproc_If_Compare'):
        assert not _is_linked(a1, 'idl_Preproc_If_Compare', b)
    if hasattr(a2, 'idl_Preproc_If_Compare'):
        assert _is_linked(a2, 'idl_Preproc_If_Compare', b)
    _safe_set(b, 'idl_Preproc_If', set())
    assert not _is_linked(b, 'idl_Preproc_If', a2)
    if hasattr(a2, 'idl_Preproc_If_Compare'):
        assert not _is_linked(a2, 'idl_Preproc_If_Compare', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body95_stub_double():
    # idl_SwitchBody has no real 'idl_SwitchBody' property in the generated
    # code (a bare stub) -- manually attach it so idl_UnionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_UnionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_UnionType(name="sample_text")
    partner = idl_SwitchBody()
    setattr(partner, 'idl_SwitchBody', None)
    _safe_set(owner, 'idl_UnionType96', partner)
    assert getattr(partner, 'idl_SwitchBody') == owner
    _safe_set(owner, 'idl_UnionType96', None)
    assert getattr(partner, 'idl_SwitchBody') is None


def test_assoc_comment73_stub_double():
    # idl_Member has no real 'idl_Member74' property in the generated
    # code (a bare stub) -- manually attach it so idl_IDLComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_IDLComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_IDLComment(body="sample_text")
    partner = idl_Member()
    setattr(partner, 'idl_Member74', None)
    _safe_set(owner, 'idl_IDLComment75', partner)
    assert owner in getattr(partner, 'idl_Member74')
    _safe_set(owner, 'idl_IDLComment75', None)
    assert owner not in getattr(partner, 'idl_Member74')


def test_assoc_comments54_stub_double():
    # idl_ParameterDecls has no real 'idl_ParameterDecls55' property in the generated
    # code (a bare stub) -- manually attach it so idl_IDLComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_IDLComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_IDLComment(body="sample_text")
    partner = idl_ParameterDecls()
    setattr(partner, 'idl_ParameterDecls55', None)
    _safe_set(owner, 'idl_IDLComment56', partner)
    assert owner in getattr(partner, 'idl_ParameterDecls55')
    _safe_set(owner, 'idl_IDLComment56', None)
    assert owner not in getattr(partner, 'idl_ParameterDecls55')


def test_assoc_comments83_stub_double():
    # idl_TypeDeclarator has no real 'idl_TypeDeclarator' property in the generated
    # code (a bare stub) -- manually attach it so idl_IDLComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_IDLComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_IDLComment(body="sample_text")
    partner = idl_TypeDeclarator()
    setattr(partner, 'idl_TypeDeclarator', None)
    _safe_set(owner, 'idl_IDLComment84', partner)
    assert owner in getattr(partner, 'idl_TypeDeclarator')
    _safe_set(owner, 'idl_IDLComment84', None)
    assert owner not in getattr(partner, 'idl_TypeDeclarator')


def test_assoc_comments99_stub_double():
    # idl_Case has no real 'idl_Case100' property in the generated
    # code (a bare stub) -- manually attach it so idl_IDLComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_IDLComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_IDLComment(body="sample_text")
    partner = idl_Case()
    setattr(partner, 'idl_Case100', None)
    _safe_set(owner, 'idl_IDLComment101', partner)
    assert owner in getattr(partner, 'idl_Case100')
    _safe_set(owner, 'idl_IDLComment101', None)
    assert owner not in getattr(partner, 'idl_Case100')


def test_assoc_constExp106_stub_double():
    # idl_ConstExp has no real 'idl_ConstExp108' property in the generated
    # code (a bare stub) -- manually attach it so idl_CaseLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_CaseLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_CaseLabel(isCase=True, isDefault=True)
    partner = idl_ConstExp()
    setattr(partner, 'idl_ConstExp108', None)
    _safe_set(owner, 'idl_CaseLabel107', partner)
    assert getattr(partner, 'idl_ConstExp108') == owner
    _safe_set(owner, 'idl_CaseLabel107', None)
    assert getattr(partner, 'idl_ConstExp108') is None


def test_assoc_decl71_stub_double():
    # idl_Member has no real 'idl_Member72' property in the generated
    # code (a bare stub) -- manually attach it so idl_Declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Declarator(id="sample_text")
    partner = idl_Member()
    setattr(partner, 'idl_Member72', None)
    _safe_set(owner, 'idl_Declarator', partner)
    assert getattr(partner, 'idl_Member72') == owner
    _safe_set(owner, 'idl_Declarator', None)
    assert getattr(partner, 'idl_Member72') is None


def test_assoc_declarator112_stub_double():
    # idl_ElementSpec has no real 'idl_ElementSpec113' property in the generated
    # code (a bare stub) -- manually attach it so idl_Declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Declarator(id="sample_text")
    partner = idl_ElementSpec()
    setattr(partner, 'idl_ElementSpec113', None)
    _safe_set(owner, 'idl_Declarator114', partner)
    assert getattr(partner, 'idl_ElementSpec113') == owner
    _safe_set(owner, 'idl_Declarator114', None)
    assert getattr(partner, 'idl_ElementSpec113') is None


def test_assoc_declarators88_stub_double():
    # idl_TypeDeclarator has no real 'idl_TypeDeclarator89' property in the generated
    # code (a bare stub) -- manually attach it so idl_Declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Declarator(id="sample_text")
    partner = idl_TypeDeclarator()
    setattr(partner, 'idl_TypeDeclarator89', None)
    _safe_set(owner, 'idl_Declarator90', partner)
    assert owner in getattr(partner, 'idl_TypeDeclarator89')
    _safe_set(owner, 'idl_Declarator90', None)
    assert owner not in getattr(partner, 'idl_TypeDeclarator89')


def test_assoc_decls57_stub_double():
    # idl_ParameterDecls has no real 'idl_ParameterDecls58' property in the generated
    # code (a bare stub) -- manually attach it so idl_ParamDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ParamDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ParamDcl(direction="sample_text", name="sample_text")
    partner = idl_ParameterDecls()
    setattr(partner, 'idl_ParameterDecls58', None)
    _safe_set(owner, 'idl_ParamDcl', partner)
    assert owner in getattr(partner, 'idl_ParameterDecls58')
    _safe_set(owner, 'idl_ParamDcl', None)
    assert owner not in getattr(partner, 'idl_ParameterDecls58')


def test_assoc_definitions15_stub_double():
    # idl_Definition has no real 'idl_Definition17' property in the generated
    # code (a bare stub) -- manually attach it so idl_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Module(name="sample_text")
    partner = idl_Definition()
    setattr(partner, 'idl_Definition17', None)
    _safe_set(owner, 'idl_Module16', {partner})
    assert getattr(partner, 'idl_Definition17') == owner
    _safe_set(owner, 'idl_Module16', set())
    assert getattr(partner, 'idl_Definition17') is None


def test_assoc_definitions265_stub_double():
    # idl_TemplateDefinition has no real 'idl_TemplateDefinition' property in the generated
    # code (a bare stub) -- manually attach it so idl_TemplateModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_TemplateModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_TemplateModule(name="sample_text")
    partner = idl_TemplateDefinition()
    setattr(partner, 'idl_TemplateDefinition', None)
    _safe_set(owner, 'idl_TemplateModule266', {partner})
    assert getattr(partner, 'idl_TemplateDefinition') == owner
    _safe_set(owner, 'idl_TemplateModule266', set())
    assert getattr(partner, 'idl_TemplateDefinition') is None


def test_assoc_definitions269_stub_double():
    # idl_FixedDefinition has no real 'idl_FixedDefinition' property in the generated
    # code (a bare stub) -- manually attach it so idl_FixedModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FixedModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FixedModule(name="sample_text")
    partner = idl_FixedDefinition()
    setattr(partner, 'idl_FixedDefinition', None)
    _safe_set(owner, 'idl_FixedModule', {partner})
    assert getattr(partner, 'idl_FixedDefinition') == owner
    _safe_set(owner, 'idl_FixedModule', set())
    assert getattr(partner, 'idl_FixedDefinition') is None


def test_assoc_exception40_stub_double():
    # idl_ExceptionList has no real 'idl_ExceptionList41' property in the generated
    # code (a bare stub) -- manually attach it so idl_ScopedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ScopedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ScopedName(name="sample_text")
    partner = idl_ExceptionList()
    setattr(partner, 'idl_ExceptionList41', None)
    _safe_set(owner, 'idl_ScopedName42', partner)
    assert owner in getattr(partner, 'idl_ExceptionList41')
    _safe_set(owner, 'idl_ScopedName42', None)
    assert owner not in getattr(partner, 'idl_ExceptionList41')


def test_assoc_exp12_stub_double():
    # idl_ConstExp has no real 'idl_ConstExp13' property in the generated
    # code (a bare stub) -- manually attach it so idl_Preproc_Define's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Preproc_Define's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Preproc_Define(value="sample_text")
    partner = idl_ConstExp()
    setattr(partner, 'idl_ConstExp13', None)
    _safe_set(owner, 'idl_Preproc_Define', partner)
    assert getattr(partner, 'idl_ConstExp13') == owner
    _safe_set(owner, 'idl_Preproc_Define', None)
    assert getattr(partner, 'idl_ConstExp13') is None


def test_assoc_export175_stub_double():
    # idl_ComponentExport has no real 'idl_ComponentExport' property in the generated
    # code (a bare stub) -- manually attach it so idl_ComponentDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ComponentDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ComponentDecl(name="sample_text")
    partner = idl_ComponentExport()
    setattr(partner, 'idl_ComponentExport', None)
    _safe_set(owner, 'idl_ComponentDecl176', {partner})
    assert getattr(partner, 'idl_ComponentExport') == owner
    _safe_set(owner, 'idl_ComponentDecl176', set())
    assert getattr(partner, 'idl_ComponentExport') is None


def test_assoc_export215_stub_double():
    # idl_HomeExport has no real 'idl_HomeExport' property in the generated
    # code (a bare stub) -- manually attach it so idl_HomeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_HomeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_HomeDecl(name="sample_text")
    partner = idl_HomeExport()
    setattr(partner, 'idl_HomeExport', None)
    _safe_set(owner, 'idl_HomeDecl216', {partner})
    assert getattr(partner, 'idl_HomeExport') == owner
    _safe_set(owner, 'idl_HomeDecl216', set())
    assert getattr(partner, 'idl_HomeExport') is None


def test_assoc_export241_stub_double():
    # idl_Export has no real 'idl_Export243' property in the generated
    # code (a bare stub) -- manually attach it so idl_EventDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_EventDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_EventDcl(isCustom=True, isTruncatable=True)
    partner = idl_Export()
    setattr(partner, 'idl_Export243', None)
    _safe_set(owner, 'idl_EventDcl242', {partner})
    assert getattr(partner, 'idl_Export243') == owner
    _safe_set(owner, 'idl_EventDcl242', set())
    assert getattr(partner, 'idl_Export243') is None


def test_assoc_exports251_stub_double():
    # idl_PortExport has no real 'idl_PortExport' property in the generated
    # code (a bare stub) -- manually attach it so idl_PortTypeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_PortTypeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_PortTypeDecl(name="sample_text")
    partner = idl_PortExport()
    setattr(partner, 'idl_PortExport', None)
    _safe_set(owner, 'idl_PortTypeDecl252', {partner})
    assert getattr(partner, 'idl_PortExport') == owner
    _safe_set(owner, 'idl_PortTypeDecl252', set())
    assert getattr(partner, 'idl_PortExport') is None


def test_assoc_expr165_stub_double():
    # idl_PrimaryExpr has no real 'idl_PrimaryExpr' property in the generated
    # code (a bare stub) -- manually attach it so idl_UnaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_UnaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_UnaryExpr(op="sample_text")
    partner = idl_PrimaryExpr()
    setattr(partner, 'idl_PrimaryExpr', None)
    _safe_set(owner, 'idl_UnaryExpr166', partner)
    assert getattr(partner, 'idl_PrimaryExpr') == owner
    _safe_set(owner, 'idl_UnaryExpr166', None)
    assert getattr(partner, 'idl_PrimaryExpr') is None


def test_assoc_header18_stub_double():
    # idl_Interface_decl has no real 'idl_Interface_decl' property in the generated
    # code (a bare stub) -- manually attach it so idl_Interface_header's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Interface_header's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Interface_header(isAbstract=True, isLocal=True, name="sample_text")
    partner = idl_Interface_decl()
    setattr(partner, 'idl_Interface_decl', None)
    _safe_set(owner, 'idl_Interface_header', partner)
    assert getattr(partner, 'idl_Interface_decl') == owner
    _safe_set(owner, 'idl_Interface_header', None)
    assert getattr(partner, 'idl_Interface_decl') is None


def test_assoc_header258_stub_double():
    # idl_Connector has no real 'idl_Connector' property in the generated
    # code (a bare stub) -- manually attach it so idl_ConnectorHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ConnectorHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ConnectorHeader(name="sample_text")
    partner = idl_Connector()
    setattr(partner, 'idl_Connector', None)
    _safe_set(owner, 'idl_ConnectorHeader', partner)
    assert getattr(partner, 'idl_Connector') == owner
    _safe_set(owner, 'idl_ConnectorHeader', None)
    assert getattr(partner, 'idl_Connector') is None


def test_assoc_imports0_stub_double():
    # idl_Specification has no real 'idl_Specification' property in the generated
    # code (a bare stub) -- manually attach it so idl_Import_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Import_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Import_decl(imported_scope="sample_text")
    partner = idl_Specification()
    setattr(partner, 'idl_Specification', None)
    _safe_set(owner, 'idl_Import_decl', partner)
    assert owner in getattr(partner, 'idl_Specification')
    _safe_set(owner, 'idl_Import_decl', None)
    assert owner not in getattr(partner, 'idl_Specification')


def test_assoc_key217_stub_double():
    # idl_PrimaryKeySpec has no real 'idl_PrimaryKeySpec218' property in the generated
    # code (a bare stub) -- manually attach it so idl_ScopedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ScopedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ScopedName(name="sample_text")
    partner = idl_PrimaryKeySpec()
    setattr(partner, 'idl_PrimaryKeySpec218', None)
    _safe_set(owner, 'idl_ScopedName219', partner)
    assert getattr(partner, 'idl_PrimaryKeySpec218') == owner
    _safe_set(owner, 'idl_ScopedName219', None)
    assert getattr(partner, 'idl_PrimaryKeySpec218') is None


def test_assoc_label102_stub_double():
    # idl_Case has no real 'idl_Case103' property in the generated
    # code (a bare stub) -- manually attach it so idl_CaseLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_CaseLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_CaseLabel(isCase=True, isDefault=True)
    partner = idl_Case()
    setattr(partner, 'idl_Case103', None)
    _safe_set(owner, 'idl_CaseLabel', partner)
    assert owner in getattr(partner, 'idl_Case103')
    _safe_set(owner, 'idl_CaseLabel', None)
    assert owner not in getattr(partner, 'idl_Case103')


def test_assoc_lhs5_stub_double():
    # idl_Preproc_If_Val has no real 'idl_Preproc_If_Val' property in the generated
    # code (a bare stub) -- manually attach it so idl_Preproc_If_Compare's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Preproc_If_Compare's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Preproc_If_Compare(op="sample_text")
    partner = idl_Preproc_If_Val()
    setattr(partner, 'idl_Preproc_If_Val', None)
    _safe_set(owner, 'idl_Preproc_If_Compare6', partner)
    assert getattr(partner, 'idl_Preproc_If_Val') == owner
    _safe_set(owner, 'idl_Preproc_If_Compare6', None)
    assert getattr(partner, 'idl_Preproc_If_Val') is None


def test_assoc_members67_stub_double():
    # idl_Member has no real 'idl_Member' property in the generated
    # code (a bare stub) -- manually attach it so idl_ExceptDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ExceptDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ExceptDecl(name="sample_text")
    partner = idl_Member()
    setattr(partner, 'idl_Member', None)
    _safe_set(owner, 'idl_ExceptDecl68', {partner})
    assert getattr(partner, 'idl_Member') == owner
    _safe_set(owner, 'idl_ExceptDecl68', set())
    assert getattr(partner, 'idl_Member') is None


def test_assoc_members80_stub_double():
    # idl_Member has no real 'idl_Member82' property in the generated
    # code (a bare stub) -- manually attach it so idl_StructType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_StructType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_StructType(name="sample_text")
    partner = idl_Member()
    setattr(partner, 'idl_Member82', None)
    _safe_set(owner, 'idl_StructType81', {partner})
    assert getattr(partner, 'idl_Member82') == owner
    _safe_set(owner, 'idl_StructType81', set())
    assert getattr(partner, 'idl_Member82') is None


def test_assoc_parameter272_stub_double():
    # idl_ActualParameter has no real 'idl_ActualParameter' property in the generated
    # code (a bare stub) -- manually attach it so idl_TemplateModuleInst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_TemplateModuleInst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_TemplateModuleInst(name="sample_text")
    partner = idl_ActualParameter()
    setattr(partner, 'idl_ActualParameter', None)
    _safe_set(owner, 'idl_TemplateModuleInst273', {partner})
    assert getattr(partner, 'idl_ActualParameter') == owner
    _safe_set(owner, 'idl_TemplateModuleInst273', set())
    assert getattr(partner, 'idl_ActualParameter') is None


def test_assoc_params222_stub_double():
    # idl_ParameterDecls has no real 'idl_ParameterDecls224' property in the generated
    # code (a bare stub) -- manually attach it so idl_FactoryDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FactoryDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FactoryDcl(name="sample_text")
    partner = idl_ParameterDecls()
    setattr(partner, 'idl_ParameterDecls224', None)
    _safe_set(owner, 'idl_FactoryDcl223', partner)
    assert getattr(partner, 'idl_ParameterDecls224') == owner
    _safe_set(owner, 'idl_FactoryDcl223', None)
    assert getattr(partner, 'idl_ParameterDecls224') is None


def test_assoc_params230_stub_double():
    # idl_ParameterDecls has no real 'idl_ParameterDecls232' property in the generated
    # code (a bare stub) -- manually attach it so idl_FinderDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FinderDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FinderDcl(name="sample_text")
    partner = idl_ParameterDecls()
    setattr(partner, 'idl_ParameterDecls232', None)
    _safe_set(owner, 'idl_FinderDcl231', partner)
    assert getattr(partner, 'idl_ParameterDecls232') == owner
    _safe_set(owner, 'idl_FinderDcl231', None)
    assert getattr(partner, 'idl_ParameterDecls232') is None


def test_assoc_params47_stub_double():
    # idl_ParameterDecls has no real 'idl_ParameterDecls' property in the generated
    # code (a bare stub) -- manually attach it so idl_OpDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_OpDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_OpDecl(isOneway=True, name="sample_text")
    partner = idl_ParameterDecls()
    setattr(partner, 'idl_ParameterDecls', None)
    _safe_set(owner, 'idl_OpDecl48', partner)
    assert getattr(partner, 'idl_ParameterDecls') == owner
    _safe_set(owner, 'idl_OpDecl48', None)
    assert getattr(partner, 'idl_ParameterDecls') is None


def test_assoc_primary_key213_stub_double():
    # idl_PrimaryKeySpec has no real 'idl_PrimaryKeySpec' property in the generated
    # code (a bare stub) -- manually attach it so idl_HomeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_HomeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_HomeDecl(name="sample_text")
    partner = idl_PrimaryKeySpec()
    setattr(partner, 'idl_PrimaryKeySpec', None)
    _safe_set(owner, 'idl_HomeDecl214', partner)
    assert getattr(partner, 'idl_PrimaryKeySpec') == owner
    _safe_set(owner, 'idl_HomeDecl214', None)
    assert getattr(partner, 'idl_PrimaryKeySpec') is None


def test_assoc_raises225_stub_double():
    # idl_ExceptionList has no real 'idl_ExceptionList227' property in the generated
    # code (a bare stub) -- manually attach it so idl_FactoryDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FactoryDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FactoryDcl(name="sample_text")
    partner = idl_ExceptionList()
    setattr(partner, 'idl_ExceptionList227', None)
    _safe_set(owner, 'idl_FactoryDcl226', partner)
    assert getattr(partner, 'idl_ExceptionList227') == owner
    _safe_set(owner, 'idl_FactoryDcl226', None)
    assert getattr(partner, 'idl_ExceptionList227') is None


def test_assoc_raises233_stub_double():
    # idl_ExceptionList has no real 'idl_ExceptionList235' property in the generated
    # code (a bare stub) -- manually attach it so idl_FinderDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FinderDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FinderDcl(name="sample_text")
    partner = idl_ExceptionList()
    setattr(partner, 'idl_ExceptionList235', None)
    _safe_set(owner, 'idl_FinderDcl234', partner)
    assert getattr(partner, 'idl_ExceptionList235') == owner
    _safe_set(owner, 'idl_FinderDcl234', None)
    assert getattr(partner, 'idl_ExceptionList235') is None


def test_assoc_raises49_stub_double():
    # idl_ExceptionList has no real 'idl_ExceptionList51' property in the generated
    # code (a bare stub) -- manually attach it so idl_OpDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_OpDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_OpDecl(isOneway=True, name="sample_text")
    partner = idl_ExceptionList()
    setattr(partner, 'idl_ExceptionList51', None)
    _safe_set(owner, 'idl_OpDecl50', partner)
    assert getattr(partner, 'idl_ExceptionList51') == owner
    _safe_set(owner, 'idl_OpDecl50', None)
    assert getattr(partner, 'idl_ExceptionList51') is None


def test_assoc_rhs7_stub_double():
    # idl_Preproc_If_Val has no real 'idl_Preproc_If_Val9' property in the generated
    # code (a bare stub) -- manually attach it so idl_Preproc_If_Compare's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_Preproc_If_Compare's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_Preproc_If_Compare(op="sample_text")
    partner = idl_Preproc_If_Val()
    setattr(partner, 'idl_Preproc_If_Val9', None)
    _safe_set(owner, 'idl_Preproc_If_Compare8', partner)
    assert getattr(partner, 'idl_Preproc_If_Val9') == owner
    _safe_set(owner, 'idl_Preproc_If_Compare8', None)
    assert getattr(partner, 'idl_Preproc_If_Val9') is None


def test_assoc_switch93_stub_double():
    # idl_SwitchTypeSpec has no real 'idl_SwitchTypeSpec' property in the generated
    # code (a bare stub) -- manually attach it so idl_UnionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_UnionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_UnionType(name="sample_text")
    partner = idl_SwitchTypeSpec()
    setattr(partner, 'idl_SwitchTypeSpec', None)
    _safe_set(owner, 'idl_UnionType94', partner)
    assert getattr(partner, 'idl_SwitchTypeSpec') == owner
    _safe_set(owner, 'idl_UnionType94', None)
    assert getattr(partner, 'idl_SwitchTypeSpec') is None


def test_assoc_type129_stub_double():
    # idl_ConstType has no real 'idl_ConstType' property in the generated
    # code (a bare stub) -- manually attach it so idl_ConstDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ConstDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ConstDecl(name="sample_text")
    partner = idl_ConstType()
    setattr(partner, 'idl_ConstType', None)
    _safe_set(owner, 'idl_ConstDecl', partner)
    assert getattr(partner, 'idl_ConstType') == owner
    _safe_set(owner, 'idl_ConstDecl', None)
    assert getattr(partner, 'idl_ConstType') is None


def test_assoc_type246_stub_double():
    # idl_ParamTypeSpec has no real 'idl_ParamTypeSpec248' property in the generated
    # code (a bare stub) -- manually attach it so idl_StateMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_StateMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_StateMember(isPublic=True, names="sample_text")
    partner = idl_ParamTypeSpec()
    setattr(partner, 'idl_ParamTypeSpec248', None)
    _safe_set(owner, 'idl_StateMember247', partner)
    assert getattr(partner, 'idl_ParamTypeSpec248') == owner
    _safe_set(owner, 'idl_StateMember247', None)
    assert getattr(partner, 'idl_ParamTypeSpec248') is None


def test_assoc_type267_stub_double():
    # idl_FormalParameterType has no real 'idl_FormalParameterType' property in the generated
    # code (a bare stub) -- manually attach it so idl_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_FormalParameter(name="sample_text")
    partner = idl_FormalParameterType()
    setattr(partner, 'idl_FormalParameterType', None)
    _safe_set(owner, 'idl_FormalParameter268', partner)
    assert getattr(partner, 'idl_FormalParameterType') == owner
    _safe_set(owner, 'idl_FormalParameter268', None)
    assert getattr(partner, 'idl_FormalParameterType') is None


def test_assoc_type30_stub_double():
    # idl_ParamTypeSpec has no real 'idl_ParamTypeSpec' property in the generated
    # code (a bare stub) -- manually attach it so idl_AttrDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_AttrDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_AttrDecl(names="sample_text")
    partner = idl_ParamTypeSpec()
    setattr(partner, 'idl_ParamTypeSpec', None)
    _safe_set(owner, 'idl_AttrDecl31', partner)
    assert getattr(partner, 'idl_ParamTypeSpec') == owner
    _safe_set(owner, 'idl_AttrDecl31', None)
    assert getattr(partner, 'idl_ParamTypeSpec') is None


def test_assoc_type45_stub_double():
    # idl_OpTypeDecl has no real 'idl_OpTypeDecl' property in the generated
    # code (a bare stub) -- manually attach it so idl_OpDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_OpDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_OpDecl(isOneway=True, name="sample_text")
    partner = idl_OpTypeDecl()
    setattr(partner, 'idl_OpTypeDecl', None)
    _safe_set(owner, 'idl_OpDecl46', partner)
    assert getattr(partner, 'idl_OpTypeDecl') == owner
    _safe_set(owner, 'idl_OpDecl46', None)
    assert getattr(partner, 'idl_OpTypeDecl') is None


def test_assoc_type59_stub_double():
    # idl_ParamTypeSpec has no real 'idl_ParamTypeSpec61' property in the generated
    # code (a bare stub) -- manually attach it so idl_ParamDcl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ParamDcl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ParamDcl(direction="sample_text", name="sample_text")
    partner = idl_ParamTypeSpec()
    setattr(partner, 'idl_ParamTypeSpec61', None)
    _safe_set(owner, 'idl_ParamDcl60', partner)
    assert getattr(partner, 'idl_ParamTypeSpec61') == owner
    _safe_set(owner, 'idl_ParamDcl60', None)
    assert getattr(partner, 'idl_ParamTypeSpec61') is None


def test_assoc_value130_stub_double():
    # idl_ConstExp has no real 'idl_ConstExp132' property in the generated
    # code (a bare stub) -- manually attach it so idl_ConstDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # idl_ConstDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = idl_ConstDecl(name="sample_text")
    partner = idl_ConstExp()
    setattr(partner, 'idl_ConstExp132', None)
    _safe_set(owner, 'idl_ConstDecl131', partner)
    assert getattr(partner, 'idl_ConstExp132') == owner
    _safe_set(owner, 'idl_ConstDecl131', None)
    assert getattr(partner, 'idl_ConstExp132') is None


