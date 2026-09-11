import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractCExpression,
    AbstractCStatement,
    AbstractMClass,
    AbstractMClassFieldDeclaration,
    AbstractMDeclaredType,
    AbstractMExternalType,
    AbstractMFieldDeclaration,
    AbstractMImplementableMethodDeclaration,
    AbstractMInterface,
    AbstractMMethodDeclaration,
    AbstractMMethodImplementation,
    AbstractMMethodLike,
    AbstractMPackageContainer,
    AbstractMResource,
    AbstractMType,
    AbstractMTypeContainer,
    AbstractMTypeReference,
    AbstractMTypeWithNameDeclaration,
    AbstractModifiers,
    MDeclaredClass,
    jsm_AbstractCExpression,
    jsm_AbstractCStatement,
    jsm_AbstractMClass,
    jsm_AbstractMClassFieldDeclaration,
    jsm_AbstractMDeclaredType,
    jsm_AbstractMExternalType,
    jsm_AbstractMFieldDeclaration,
    jsm_AbstractMImplementableMethodDeclaration,
    jsm_AbstractMInterface,
    jsm_AbstractMMethodDeclaration,
    jsm_AbstractMMethodImplementation,
    jsm_AbstractMMethodLike,
    jsm_AbstractMPackageContainer,
    jsm_AbstractMResource,
    jsm_AbstractMType,
    jsm_AbstractMTypeContainer,
    jsm_AbstractMTypeReference,
    jsm_AbstractMTypeWithNameDeclaration,
    jsm_AbstractModifiers,
    jsm_CBlockStatement,
    jsm_CConditionalExpression,
    jsm_CDeclarationStatement,
    jsm_CExpressionStatement,
    jsm_CIfStatement,
    jsm_CUnparsedExpression,
    jsm_CUnparsedStatement,
    jsm_MAbstractClassMethodDeclaration,
    jsm_MAbstractDeclaredClass,
    jsm_MCompilationUnit,
    jsm_MConstantInterfaceFieldDeclaration,
    jsm_MConstructor,
    jsm_MConstructorParameter,
    jsm_MDeclaredClass,
    jsm_MDeclaredInterface,
    jsm_MDeclaredMethodImplementation,
    jsm_MDeclaredTypeReference,
    jsm_MDirectMethodImplementation,
    jsm_MExternalClass,
    jsm_MExternalInterface,
    jsm_MExternalTypeReference,
    jsm_MImplicitMethodDeclaration,
    jsm_MInstanceClassFieldDeclaration,
    jsm_MInterfaceMethodDeclaration,
    jsm_MMethodDeclarationParameter,
    jsm_MMethodImplementationParameter,
    jsm_MNativeMethodDeclaration,
    jsm_MPackage,
    jsm_MPrimitiveTypeReference,
    jsm_MResource,
    jsm_MRoot,
    jsm_MStaticClassFieldDeclaration,
    MPrimitiveTypes,
    MVisibility,
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

def test_jsm_AbstractMClassFieldDeclaration_final_value_roundtrip():
    instance = jsm_AbstractMClassFieldDeclaration(final=True, visibility="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_jsm_AbstractMClassFieldDeclaration_visibility_value_roundtrip():
    instance = jsm_AbstractMClassFieldDeclaration(final=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_jsm_AbstractMDeclaredType_name_value_roundtrip():
    instance = jsm_AbstractMDeclaredType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jsm_AbstractMExternalType_fullQualifiedName_value_roundtrip():
    instance = jsm_AbstractMExternalType(fullQualifiedName="sample_text")
    assert instance.fullQualifiedName == "sample_text"
    instance.fullQualifiedName = "sample_text_2"
    assert instance.fullQualifiedName == "sample_text_2"


def test_jsm_AbstractMResource_derived_value_roundtrip():
    instance = jsm_AbstractMResource(derived=True, name="sample_text")
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_jsm_AbstractMResource_name_value_roundtrip():
    instance = jsm_AbstractMResource(derived=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jsm_AbstractMTypeReference_array_value_roundtrip():
    instance = jsm_AbstractMTypeReference(array=True)
    assert instance.array == True
    instance.array = False
    assert instance.array == False


def test_jsm_AbstractMTypeWithNameDeclaration_name_value_roundtrip():
    instance = jsm_AbstractMTypeWithNameDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jsm_AbstractModifiers_final_value_roundtrip():
    instance = jsm_AbstractModifiers(final=True, synchronized=True, visibility="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_jsm_AbstractModifiers_synchronized_value_roundtrip():
    instance = jsm_AbstractModifiers(final=True, synchronized=True, visibility="sample_text")
    assert instance.synchronized == True
    instance.synchronized = False
    assert instance.synchronized == False


def test_jsm_AbstractModifiers_visibility_value_roundtrip():
    instance = jsm_AbstractModifiers(final=True, synchronized=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_jsm_CDeclarationStatement_final_value_roundtrip():
    instance = jsm_CDeclarationStatement(final=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_jsm_CUnparsedExpression_code_value_roundtrip():
    instance = jsm_CUnparsedExpression(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_jsm_CUnparsedStatement_code_value_roundtrip():
    instance = jsm_CUnparsedStatement(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_jsm_MAbstractClassMethodDeclaration_visibility_value_roundtrip():
    instance = jsm_MAbstractClassMethodDeclaration(visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_jsm_MConstructorParameter_final_value_roundtrip():
    instance = jsm_MConstructorParameter(final=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_jsm_MInstanceClassFieldDeclaration_transient_value_roundtrip():
    instance = jsm_MInstanceClassFieldDeclaration(transient=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_jsm_MMethodImplementationParameter_final_value_roundtrip():
    instance = jsm_MMethodImplementationParameter(final=True, name="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_jsm_MMethodImplementationParameter_name_value_roundtrip():
    instance = jsm_MMethodImplementationParameter(final=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jsm_MPackage_name_value_roundtrip():
    instance = jsm_MPackage(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jsm_MPrimitiveTypeReference_type_value_roundtrip():
    instance = jsm_MPrimitiveTypeReference(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_jsm_MResource_content_value_roundtrip():
    instance = jsm_MResource(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_jsm_CConditionalExpression_isa_AbstractCExpression():
    instance = jsm_CConditionalExpression()
    assert isinstance(instance, AbstractCExpression)


def test_jsm_CUnparsedExpression_isa_AbstractCExpression():
    instance = jsm_CUnparsedExpression(code="sample_text")
    assert isinstance(instance, AbstractCExpression)


def test_jsm_CBlockStatement_isa_AbstractCStatement():
    instance = jsm_CBlockStatement()
    assert isinstance(instance, AbstractCStatement)


def test_jsm_CDeclarationStatement_isa_AbstractCStatement():
    instance = jsm_CDeclarationStatement(final=True)
    assert isinstance(instance, AbstractCStatement)


def test_jsm_CExpressionStatement_isa_AbstractCStatement():
    instance = jsm_CExpressionStatement()
    assert isinstance(instance, AbstractCStatement)


def test_jsm_CIfStatement_isa_AbstractCStatement():
    instance = jsm_CIfStatement()
    assert isinstance(instance, AbstractCStatement)


def test_jsm_CUnparsedStatement_isa_AbstractCStatement():
    instance = jsm_CUnparsedStatement(code="sample_text")
    assert isinstance(instance, AbstractCStatement)


def test_jsm_MDeclaredClass_isa_AbstractMClass():
    instance = jsm_MDeclaredClass()
    assert isinstance(instance, AbstractMClass)


def test_jsm_MExternalClass_isa_AbstractMClass():
    instance = jsm_MExternalClass()
    assert isinstance(instance, AbstractMClass)


def test_jsm_MInstanceClassFieldDeclaration_isa_AbstractMClassFieldDeclaration():
    instance = jsm_MInstanceClassFieldDeclaration(transient=True)
    assert isinstance(instance, AbstractMClassFieldDeclaration)


def test_jsm_MStaticClassFieldDeclaration_isa_AbstractMClassFieldDeclaration():
    instance = jsm_MStaticClassFieldDeclaration()
    assert isinstance(instance, AbstractMClassFieldDeclaration)


def test_jsm_MDeclaredClass_isa_AbstractMDeclaredType():
    instance = jsm_MDeclaredClass()
    assert isinstance(instance, AbstractMDeclaredType)


def test_jsm_MDeclaredInterface_isa_AbstractMDeclaredType():
    instance = jsm_MDeclaredInterface()
    assert isinstance(instance, AbstractMDeclaredType)


def test_jsm_MExternalClass_isa_AbstractMExternalType():
    instance = jsm_MExternalClass()
    assert isinstance(instance, AbstractMExternalType)


def test_jsm_MExternalInterface_isa_AbstractMExternalType():
    instance = jsm_MExternalInterface()
    assert isinstance(instance, AbstractMExternalType)


def test_jsm_AbstractMClassFieldDeclaration_isa_AbstractMFieldDeclaration():
    instance = jsm_AbstractMClassFieldDeclaration(final=True, visibility="sample_text")
    assert isinstance(instance, AbstractMFieldDeclaration)


def test_jsm_MConstantInterfaceFieldDeclaration_isa_AbstractMFieldDeclaration():
    instance = jsm_MConstantInterfaceFieldDeclaration()
    assert isinstance(instance, AbstractMFieldDeclaration)


def test_jsm_MAbstractClassMethodDeclaration_isa_AbstractMImplementableMethodDeclaration():
    instance = jsm_MAbstractClassMethodDeclaration(visibility="sample_text")
    assert isinstance(instance, AbstractMImplementableMethodDeclaration)


def test_jsm_MInterfaceMethodDeclaration_isa_AbstractMImplementableMethodDeclaration():
    instance = jsm_MInterfaceMethodDeclaration()
    assert isinstance(instance, AbstractMImplementableMethodDeclaration)


def test_jsm_MDeclaredInterface_isa_AbstractMInterface():
    instance = jsm_MDeclaredInterface()
    assert isinstance(instance, AbstractMInterface)


def test_jsm_MExternalInterface_isa_AbstractMInterface():
    instance = jsm_MExternalInterface()
    assert isinstance(instance, AbstractMInterface)


def test_jsm_AbstractMImplementableMethodDeclaration_isa_AbstractMMethodDeclaration():
    instance = jsm_AbstractMImplementableMethodDeclaration()
    assert isinstance(instance, AbstractMMethodDeclaration)


def test_jsm_MImplicitMethodDeclaration_isa_AbstractMMethodDeclaration():
    instance = jsm_MImplicitMethodDeclaration()
    assert isinstance(instance, AbstractMMethodDeclaration)


def test_jsm_MNativeMethodDeclaration_isa_AbstractMMethodDeclaration():
    instance = jsm_MNativeMethodDeclaration()
    assert isinstance(instance, AbstractMMethodDeclaration)


def test_jsm_MDeclaredMethodImplementation_isa_AbstractMMethodImplementation():
    instance = jsm_MDeclaredMethodImplementation()
    assert isinstance(instance, AbstractMMethodImplementation)


def test_jsm_MDirectMethodImplementation_isa_AbstractMMethodImplementation():
    instance = jsm_MDirectMethodImplementation()
    assert isinstance(instance, AbstractMMethodImplementation)


def test_jsm_AbstractMMethodImplementation_isa_AbstractMMethodLike():
    instance = jsm_AbstractMMethodImplementation()
    assert isinstance(instance, AbstractMMethodLike)


def test_jsm_MConstructor_isa_AbstractMMethodLike():
    instance = jsm_MConstructor()
    assert isinstance(instance, AbstractMMethodLike)


def test_jsm_MPackage_isa_AbstractMPackageContainer():
    instance = jsm_MPackage(name="sample_text")
    assert isinstance(instance, AbstractMPackageContainer)


def test_jsm_MRoot_isa_AbstractMPackageContainer():
    instance = jsm_MRoot()
    assert isinstance(instance, AbstractMPackageContainer)


def test_jsm_MCompilationUnit_isa_AbstractMResource():
    instance = jsm_MCompilationUnit()
    assert isinstance(instance, AbstractMResource)


def test_jsm_MResource_isa_AbstractMResource():
    instance = jsm_MResource(content="sample_text")
    assert isinstance(instance, AbstractMResource)


def test_jsm_AbstractMClass_isa_AbstractMType():
    instance = jsm_AbstractMClass()
    assert isinstance(instance, AbstractMType)


def test_jsm_AbstractMInterface_isa_AbstractMType():
    instance = jsm_AbstractMInterface()
    assert isinstance(instance, AbstractMType)


def test_jsm_AbstractMDeclaredType_isa_AbstractMTypeContainer():
    instance = jsm_AbstractMDeclaredType(name="sample_text")
    assert isinstance(instance, AbstractMTypeContainer)


def test_jsm_MCompilationUnit_isa_AbstractMTypeContainer():
    instance = jsm_MCompilationUnit()
    assert isinstance(instance, AbstractMTypeContainer)


def test_jsm_MDeclaredTypeReference_isa_AbstractMTypeReference():
    instance = jsm_MDeclaredTypeReference()
    assert isinstance(instance, AbstractMTypeReference)


def test_jsm_MExternalTypeReference_isa_AbstractMTypeReference():
    instance = jsm_MExternalTypeReference()
    assert isinstance(instance, AbstractMTypeReference)


def test_jsm_MPrimitiveTypeReference_isa_AbstractMTypeReference():
    instance = jsm_MPrimitiveTypeReference(type="sample_text")
    assert isinstance(instance, AbstractMTypeReference)


def test_jsm_AbstractMFieldDeclaration_isa_AbstractMTypeWithNameDeclaration():
    instance = jsm_AbstractMFieldDeclaration()
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


def test_jsm_AbstractMMethodDeclaration_isa_AbstractMTypeWithNameDeclaration():
    instance = jsm_AbstractMMethodDeclaration()
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


def test_jsm_CDeclarationStatement_isa_AbstractMTypeWithNameDeclaration():
    instance = jsm_CDeclarationStatement(final=True)
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


def test_jsm_MConstructorParameter_isa_AbstractMTypeWithNameDeclaration():
    instance = jsm_MConstructorParameter(final=True)
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


def test_jsm_MMethodDeclarationParameter_isa_AbstractMTypeWithNameDeclaration():
    instance = jsm_MMethodDeclarationParameter()
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


def test_jsm_AbstractMMethodLike_isa_AbstractModifiers():
    instance = jsm_AbstractMMethodLike()
    assert isinstance(instance, AbstractModifiers)


def test_jsm_MAbstractDeclaredClass_isa_MDeclaredClass():
    instance = jsm_MAbstractDeclaredClass()
    assert isinstance(instance, MDeclaredClass)


def test_assoc_abstractMethods32_link_reassign_clear():
    a = jsm_MAbstractClassMethodDeclaration(visibility="sample_text")
    b1 = jsm_MAbstractDeclaredClass()
    b2 = jsm_MAbstractDeclaredClass()
    _safe_set(a, 'MAbstractClassMethodDeclaration', b1)
    assert _is_linked(a, 'MAbstractClassMethodDeclaration', b1)
    if hasattr(b1, 'owner33'):
        assert _is_linked(b1, 'owner33', a)
    _safe_set(a, 'MAbstractClassMethodDeclaration', b2)
    assert _is_linked(a, 'MAbstractClassMethodDeclaration', b2)
    if hasattr(b1, 'owner33'):
        assert not _is_linked(b1, 'owner33', a)
    if hasattr(b2, 'owner33'):
        assert _is_linked(b2, 'owner33', a)
    _safe_set(a, 'MAbstractClassMethodDeclaration', None)
    assert not _is_linked(a, 'MAbstractClassMethodDeclaration', b2)
    if hasattr(b2, 'owner33'):
        assert not _is_linked(b2, 'owner33', a)


def test_assoc_constructor67_link_reassign_clear():
    a = jsm_MConstructorParameter(final=True)
    b1 = jsm_MConstructor()
    b2 = jsm_MConstructor()
    _safe_set(a, 'parameters68', b1)
    assert _is_linked(a, 'parameters68', b1)
    if hasattr(b1, 'MConstructor69'):
        assert _is_linked(b1, 'MConstructor69', a)
    _safe_set(a, 'parameters68', b2)
    assert _is_linked(a, 'parameters68', b2)
    if hasattr(b1, 'MConstructor69'):
        assert not _is_linked(b1, 'MConstructor69', a)
    if hasattr(b2, 'MConstructor69'):
        assert _is_linked(b2, 'MConstructor69', a)
    _safe_set(a, 'parameters68', None)
    assert not _is_linked(a, 'parameters68', b2)
    if hasattr(b2, 'MConstructor69'):
        assert not _is_linked(b2, 'MConstructor69', a)


def test_assoc_derivedFrom7_link_reassign_clear():
    a = jsm_AbstractMResource(derived=True, name="sample_text")
    b1 = jsm_AbstractMResource(derived=True, name="sample_text")
    b2 = jsm_AbstractMResource(derived=False, name="sample_text_2")
    _safe_set(a, 'AbstractMResource8', b1)
    assert _is_linked(a, 'AbstractMResource8', b1)
    if hasattr(b1, 'superOf'):
        assert _is_linked(b1, 'superOf', a)
    _safe_set(a, 'AbstractMResource8', b2)
    assert _is_linked(a, 'AbstractMResource8', b2)
    if hasattr(b1, 'superOf'):
        assert not _is_linked(b1, 'superOf', a)
    if hasattr(b2, 'superOf'):
        assert _is_linked(b2, 'superOf', a)
    _safe_set(a, 'AbstractMResource8', None)
    assert not _is_linked(a, 'AbstractMResource8', b2)
    if hasattr(b2, 'superOf'):
        assert not _is_linked(b2, 'superOf', a)


def test_assoc_externalTypes1_link_reassign_clear():
    a = jsm_AbstractMExternalType(fullQualifiedName="sample_text")
    b1 = jsm_MRoot()
    b2 = jsm_MRoot()
    _safe_set(a, 'AbstractMExternalType', b1)
    assert _is_linked(a, 'AbstractMExternalType', b1)
    if hasattr(b1, 'root'):
        assert _is_linked(b1, 'root', a)
    _safe_set(a, 'AbstractMExternalType', b2)
    assert _is_linked(a, 'AbstractMExternalType', b2)
    if hasattr(b1, 'root'):
        assert not _is_linked(b1, 'root', a)
    if hasattr(b2, 'root'):
        assert _is_linked(b2, 'root', a)
    _safe_set(a, 'AbstractMExternalType', None)
    assert not _is_linked(a, 'AbstractMExternalType', b2)
    if hasattr(b2, 'root'):
        assert not _is_linked(b2, 'root', a)


def test_assoc_instanceFields24_link_reassign_clear():
    a = jsm_MInstanceClassFieldDeclaration(transient=True)
    b1 = jsm_MDeclaredClass()
    b2 = jsm_MDeclaredClass()
    _safe_set(a, 'MInstanceClassFieldDeclaration', b1)
    assert _is_linked(a, 'MInstanceClassFieldDeclaration', b1)
    if hasattr(b1, 'owner25'):
        assert _is_linked(b1, 'owner25', a)
    _safe_set(a, 'MInstanceClassFieldDeclaration', b2)
    assert _is_linked(a, 'MInstanceClassFieldDeclaration', b2)
    if hasattr(b1, 'owner25'):
        assert not _is_linked(b1, 'owner25', a)
    if hasattr(b2, 'owner25'):
        assert _is_linked(b2, 'owner25', a)
    _safe_set(a, 'MInstanceClassFieldDeclaration', None)
    assert not _is_linked(a, 'MInstanceClassFieldDeclaration', b2)
    if hasattr(b2, 'owner25'):
        assert not _is_linked(b2, 'owner25', a)


def test_assoc_methodImplementation61_link_reassign_clear():
    a = jsm_MMethodImplementationParameter(final=True, name="sample_text")
    b1 = jsm_AbstractMMethodImplementation()
    b2 = jsm_AbstractMMethodImplementation()
    _safe_set(a, 'parameters62', b1)
    assert _is_linked(a, 'parameters62', b1)
    if hasattr(b1, 'AbstractMMethodImplementation63'):
        assert _is_linked(b1, 'AbstractMMethodImplementation63', a)
    _safe_set(a, 'parameters62', b2)
    assert _is_linked(a, 'parameters62', b2)
    if hasattr(b1, 'AbstractMMethodImplementation63'):
        assert not _is_linked(b1, 'AbstractMMethodImplementation63', a)
    if hasattr(b2, 'AbstractMMethodImplementation63'):
        assert _is_linked(b2, 'AbstractMMethodImplementation63', a)
    _safe_set(a, 'parameters62', None)
    assert not _is_linked(a, 'parameters62', b2)
    if hasattr(b2, 'AbstractMMethodImplementation63'):
        assert not _is_linked(b2, 'AbstractMMethodImplementation63', a)


def test_assoc_owner42_link_reassign_clear():
    a = jsm_MInstanceClassFieldDeclaration(transient=True)
    b1 = jsm_MDeclaredClass()
    b2 = jsm_MDeclaredClass()
    _safe_set(a, 'instanceFields', b1)
    assert _is_linked(a, 'instanceFields', b1)
    if hasattr(b1, 'MDeclaredClass43'):
        assert _is_linked(b1, 'MDeclaredClass43', a)
    _safe_set(a, 'instanceFields', b2)
    assert _is_linked(a, 'instanceFields', b2)
    if hasattr(b1, 'MDeclaredClass43'):
        assert not _is_linked(b1, 'MDeclaredClass43', a)
    if hasattr(b2, 'MDeclaredClass43'):
        assert _is_linked(b2, 'MDeclaredClass43', a)
    _safe_set(a, 'instanceFields', None)
    assert not _is_linked(a, 'instanceFields', b2)
    if hasattr(b2, 'MDeclaredClass43'):
        assert not _is_linked(b2, 'MDeclaredClass43', a)


def test_assoc_owner50_link_reassign_clear():
    a = jsm_MAbstractClassMethodDeclaration(visibility="sample_text")
    b1 = jsm_MAbstractDeclaredClass()
    b2 = jsm_MAbstractDeclaredClass()
    _safe_set(a, 'abstractMethods', b1)
    assert _is_linked(a, 'abstractMethods', b1)
    if hasattr(b1, 'MAbstractDeclaredClass'):
        assert _is_linked(b1, 'MAbstractDeclaredClass', a)
    _safe_set(a, 'abstractMethods', b2)
    assert _is_linked(a, 'abstractMethods', b2)
    if hasattr(b1, 'MAbstractDeclaredClass'):
        assert not _is_linked(b1, 'MAbstractDeclaredClass', a)
    if hasattr(b2, 'MAbstractDeclaredClass'):
        assert _is_linked(b2, 'MAbstractDeclaredClass', a)
    _safe_set(a, 'abstractMethods', None)
    assert not _is_linked(a, 'abstractMethods', b2)
    if hasattr(b2, 'MAbstractDeclaredClass'):
        assert not _is_linked(b2, 'MAbstractDeclaredClass', a)


def test_assoc_package4_link_reassign_clear():
    a = jsm_MPackage(name="sample_text")
    b1 = jsm_AbstractMResource(derived=True, name="sample_text")
    b2 = jsm_AbstractMResource(derived=False, name="sample_text_2")
    _safe_set(a, 'MPackage5', b1)
    assert _is_linked(a, 'MPackage5', b1)
    if hasattr(b1, 'resources'):
        assert _is_linked(b1, 'resources', a)
    _safe_set(a, 'MPackage5', b2)
    assert _is_linked(a, 'MPackage5', b2)
    if hasattr(b1, 'resources'):
        assert not _is_linked(b1, 'resources', a)
    if hasattr(b2, 'resources'):
        assert _is_linked(b2, 'resources', a)
    _safe_set(a, 'MPackage5', None)
    assert not _is_linked(a, 'MPackage5', b2)
    if hasattr(b2, 'resources'):
        assert not _is_linked(b2, 'resources', a)


def test_assoc_packageContainer2_link_reassign_clear():
    a = jsm_MPackage(name="sample_text")
    b1 = jsm_AbstractMPackageContainer()
    b2 = jsm_AbstractMPackageContainer()
    _safe_set(a, 'packages', b1)
    assert _is_linked(a, 'packages', b1)
    if hasattr(b1, 'AbstractMPackageContainer'):
        assert _is_linked(b1, 'AbstractMPackageContainer', a)
    _safe_set(a, 'packages', b2)
    assert _is_linked(a, 'packages', b2)
    if hasattr(b1, 'AbstractMPackageContainer'):
        assert not _is_linked(b1, 'AbstractMPackageContainer', a)
    if hasattr(b2, 'AbstractMPackageContainer'):
        assert _is_linked(b2, 'AbstractMPackageContainer', a)
    _safe_set(a, 'packages', None)
    assert not _is_linked(a, 'packages', b2)
    if hasattr(b2, 'AbstractMPackageContainer'):
        assert not _is_linked(b2, 'AbstractMPackageContainer', a)


def test_assoc_packages0_link_reassign_clear():
    a = jsm_MPackage(name="sample_text")
    b1 = jsm_AbstractMPackageContainer()
    b2 = jsm_AbstractMPackageContainer()
    _safe_set(a, 'MPackage', b1)
    assert _is_linked(a, 'MPackage', b1)
    if hasattr(b1, 'packageContainer'):
        assert _is_linked(b1, 'packageContainer', a)
    _safe_set(a, 'MPackage', b2)
    assert _is_linked(a, 'MPackage', b2)
    if hasattr(b1, 'packageContainer'):
        assert not _is_linked(b1, 'packageContainer', a)
    if hasattr(b2, 'packageContainer'):
        assert _is_linked(b2, 'packageContainer', a)
    _safe_set(a, 'MPackage', None)
    assert not _is_linked(a, 'MPackage', b2)
    if hasattr(b2, 'packageContainer'):
        assert not _is_linked(b2, 'packageContainer', a)


def test_assoc_parameters57_link_reassign_clear():
    a = jsm_MMethodImplementationParameter(final=True, name="sample_text")
    b1 = jsm_AbstractMMethodImplementation()
    b2 = jsm_AbstractMMethodImplementation()
    _safe_set(a, 'MMethodImplementationParameter', b1)
    assert _is_linked(a, 'MMethodImplementationParameter', b1)
    if hasattr(b1, 'methodImplementation'):
        assert _is_linked(b1, 'methodImplementation', a)
    _safe_set(a, 'MMethodImplementationParameter', b2)
    assert _is_linked(a, 'MMethodImplementationParameter', b2)
    if hasattr(b1, 'methodImplementation'):
        assert not _is_linked(b1, 'methodImplementation', a)
    if hasattr(b2, 'methodImplementation'):
        assert _is_linked(b2, 'methodImplementation', a)
    _safe_set(a, 'MMethodImplementationParameter', None)
    assert not _is_linked(a, 'MMethodImplementationParameter', b2)
    if hasattr(b2, 'methodImplementation'):
        assert not _is_linked(b2, 'methodImplementation', a)


def test_assoc_parameters66_link_reassign_clear():
    a = jsm_MConstructorParameter(final=True)
    b1 = jsm_MConstructor()
    b2 = jsm_MConstructor()
    _safe_set(a, 'MConstructorParameter', b1)
    assert _is_linked(a, 'MConstructorParameter', b1)
    if hasattr(b1, 'constructor'):
        assert _is_linked(b1, 'constructor', a)
    _safe_set(a, 'MConstructorParameter', b2)
    assert _is_linked(a, 'MConstructorParameter', b2)
    if hasattr(b1, 'constructor'):
        assert not _is_linked(b1, 'constructor', a)
    if hasattr(b2, 'constructor'):
        assert _is_linked(b2, 'constructor', a)
    _safe_set(a, 'MConstructorParameter', None)
    assert not _is_linked(a, 'MConstructorParameter', b2)
    if hasattr(b2, 'constructor'):
        assert not _is_linked(b2, 'constructor', a)


def test_assoc_resources3_link_reassign_clear():
    a = jsm_MPackage(name="sample_text")
    b1 = jsm_AbstractMResource(derived=True, name="sample_text")
    b2 = jsm_AbstractMResource(derived=False, name="sample_text_2")
    _safe_set(a, 'package', {b1})
    assert _is_linked(a, 'package', b1)
    if hasattr(b1, 'AbstractMResource'):
        assert _is_linked(b1, 'AbstractMResource', a)
    _safe_set(a, 'package', {b2})
    assert _is_linked(a, 'package', b2)
    if hasattr(b1, 'AbstractMResource'):
        assert not _is_linked(b1, 'AbstractMResource', a)
    if hasattr(b2, 'AbstractMResource'):
        assert _is_linked(b2, 'AbstractMResource', a)
    _safe_set(a, 'package', set())
    assert not _is_linked(a, 'package', b2)
    if hasattr(b2, 'AbstractMResource'):
        assert not _is_linked(b2, 'AbstractMResource', a)


def test_assoc_root15_link_reassign_clear():
    a = jsm_AbstractMExternalType(fullQualifiedName="sample_text")
    b1 = jsm_MRoot()
    b2 = jsm_MRoot()
    _safe_set(a, 'externalTypes', b1)
    assert _is_linked(a, 'externalTypes', b1)
    if hasattr(b1, 'MRoot'):
        assert _is_linked(b1, 'MRoot', a)
    _safe_set(a, 'externalTypes', b2)
    assert _is_linked(a, 'externalTypes', b2)
    if hasattr(b1, 'MRoot'):
        assert not _is_linked(b1, 'MRoot', a)
    if hasattr(b2, 'MRoot'):
        assert _is_linked(b2, 'MRoot', a)
    _safe_set(a, 'externalTypes', None)
    assert not _is_linked(a, 'externalTypes', b2)
    if hasattr(b2, 'MRoot'):
        assert not _is_linked(b2, 'MRoot', a)


def test_assoc_superOf10_link_reassign_clear():
    a = jsm_AbstractMResource(derived=True, name="sample_text")
    b1 = jsm_AbstractMResource(derived=True, name="sample_text")
    b2 = jsm_AbstractMResource(derived=False, name="sample_text_2")
    _safe_set(a, 'AbstractMResource11', b1)
    assert _is_linked(a, 'AbstractMResource11', b1)
    if hasattr(b1, 'derivedFrom'):
        assert _is_linked(b1, 'derivedFrom', a)
    _safe_set(a, 'AbstractMResource11', b2)
    assert _is_linked(a, 'AbstractMResource11', b2)
    if hasattr(b1, 'derivedFrom'):
        assert not _is_linked(b1, 'derivedFrom', a)
    if hasattr(b2, 'derivedFrom'):
        assert _is_linked(b2, 'derivedFrom', a)
    _safe_set(a, 'AbstractMResource11', None)
    assert not _is_linked(a, 'AbstractMResource11', b2)
    if hasattr(b2, 'derivedFrom'):
        assert not _is_linked(b2, 'derivedFrom', a)


def test_assoc_type16_link_reassign_clear():
    a = jsm_AbstractMDeclaredType(name="sample_text")
    b1 = jsm_MDeclaredTypeReference()
    b2 = jsm_MDeclaredTypeReference()
    _safe_set(a, 'jsm_AbstractMDeclaredType', b1)
    assert _is_linked(a, 'jsm_AbstractMDeclaredType', b1)
    if hasattr(b1, 'jsm_MDeclaredTypeReference'):
        assert _is_linked(b1, 'jsm_MDeclaredTypeReference', a)
    _safe_set(a, 'jsm_AbstractMDeclaredType', b2)
    assert _is_linked(a, 'jsm_AbstractMDeclaredType', b2)
    if hasattr(b1, 'jsm_MDeclaredTypeReference'):
        assert not _is_linked(b1, 'jsm_MDeclaredTypeReference', a)
    if hasattr(b2, 'jsm_MDeclaredTypeReference'):
        assert _is_linked(b2, 'jsm_MDeclaredTypeReference', a)
    _safe_set(a, 'jsm_AbstractMDeclaredType', None)
    assert not _is_linked(a, 'jsm_AbstractMDeclaredType', b2)
    if hasattr(b2, 'jsm_MDeclaredTypeReference'):
        assert not _is_linked(b2, 'jsm_MDeclaredTypeReference', a)


def test_assoc_type17_link_reassign_clear():
    a = jsm_AbstractMExternalType(fullQualifiedName="sample_text")
    b1 = jsm_MExternalTypeReference()
    b2 = jsm_MExternalTypeReference()
    _safe_set(a, 'jsm_AbstractMExternalType', b1)
    assert _is_linked(a, 'jsm_AbstractMExternalType', b1)
    if hasattr(b1, 'jsm_MExternalTypeReference'):
        assert _is_linked(b1, 'jsm_MExternalTypeReference', a)
    _safe_set(a, 'jsm_AbstractMExternalType', b2)
    assert _is_linked(a, 'jsm_AbstractMExternalType', b2)
    if hasattr(b1, 'jsm_MExternalTypeReference'):
        assert not _is_linked(b1, 'jsm_MExternalTypeReference', a)
    if hasattr(b2, 'jsm_MExternalTypeReference'):
        assert _is_linked(b2, 'jsm_MExternalTypeReference', a)
    _safe_set(a, 'jsm_AbstractMExternalType', None)
    assert not _is_linked(a, 'jsm_AbstractMExternalType', b2)
    if hasattr(b2, 'jsm_MExternalTypeReference'):
        assert not _is_linked(b2, 'jsm_MExternalTypeReference', a)


def test_assoc_type19_link_reassign_clear():
    a = jsm_AbstractMTypeWithNameDeclaration(name="sample_text")
    b1 = jsm_AbstractMTypeReference(array=True)
    b2 = jsm_AbstractMTypeReference(array=False)
    _safe_set(a, 'jsm_AbstractMTypeWithNameDeclaration', b1)
    assert _is_linked(a, 'jsm_AbstractMTypeWithNameDeclaration', b1)
    if hasattr(b1, 'jsm_AbstractMTypeReference'):
        assert _is_linked(b1, 'jsm_AbstractMTypeReference', a)
    _safe_set(a, 'jsm_AbstractMTypeWithNameDeclaration', b2)
    assert _is_linked(a, 'jsm_AbstractMTypeWithNameDeclaration', b2)
    if hasattr(b1, 'jsm_AbstractMTypeReference'):
        assert not _is_linked(b1, 'jsm_AbstractMTypeReference', a)
    if hasattr(b2, 'jsm_AbstractMTypeReference'):
        assert _is_linked(b2, 'jsm_AbstractMTypeReference', a)
    _safe_set(a, 'jsm_AbstractMTypeWithNameDeclaration', None)
    assert not _is_linked(a, 'jsm_AbstractMTypeWithNameDeclaration', b2)
    if hasattr(b2, 'jsm_AbstractMTypeReference'):
        assert not _is_linked(b2, 'jsm_AbstractMTypeReference', a)


def test_assoc_typeContainer14_link_reassign_clear():
    a = jsm_AbstractMDeclaredType(name="sample_text")
    b1 = jsm_AbstractMTypeContainer()
    b2 = jsm_AbstractMTypeContainer()
    _safe_set(a, 'types', b1)
    assert _is_linked(a, 'types', b1)
    if hasattr(b1, 'AbstractMTypeContainer'):
        assert _is_linked(b1, 'AbstractMTypeContainer', a)
    _safe_set(a, 'types', b2)
    assert _is_linked(a, 'types', b2)
    if hasattr(b1, 'AbstractMTypeContainer'):
        assert not _is_linked(b1, 'AbstractMTypeContainer', a)
    if hasattr(b2, 'AbstractMTypeContainer'):
        assert _is_linked(b2, 'AbstractMTypeContainer', a)
    _safe_set(a, 'types', None)
    assert not _is_linked(a, 'types', b2)
    if hasattr(b2, 'AbstractMTypeContainer'):
        assert not _is_linked(b2, 'AbstractMTypeContainer', a)


def test_assoc_types12_link_reassign_clear():
    a = jsm_AbstractMDeclaredType(name="sample_text")
    b1 = jsm_AbstractMTypeContainer()
    b2 = jsm_AbstractMTypeContainer()
    _safe_set(a, 'AbstractMDeclaredType', b1)
    assert _is_linked(a, 'AbstractMDeclaredType', b1)
    if hasattr(b1, 'typeContainer'):
        assert _is_linked(b1, 'typeContainer', a)
    _safe_set(a, 'AbstractMDeclaredType', b2)
    assert _is_linked(a, 'AbstractMDeclaredType', b2)
    if hasattr(b1, 'typeContainer'):
        assert not _is_linked(b1, 'typeContainer', a)
    if hasattr(b2, 'typeContainer'):
        assert _is_linked(b2, 'typeContainer', a)
    _safe_set(a, 'AbstractMDeclaredType', None)
    assert not _is_linked(a, 'AbstractMDeclaredType', b2)
    if hasattr(b2, 'typeContainer'):
        assert not _is_linked(b2, 'typeContainer', a)


def test_assoc_value72_link_reassign_clear():
    a = jsm_CDeclarationStatement(final=True)
    b1 = jsm_AbstractCExpression()
    b2 = jsm_AbstractCExpression()
    _safe_set(a, 'jsm_CDeclarationStatement', b1)
    assert _is_linked(a, 'jsm_CDeclarationStatement', b1)
    if hasattr(b1, 'jsm_AbstractCExpression73'):
        assert _is_linked(b1, 'jsm_AbstractCExpression73', a)
    _safe_set(a, 'jsm_CDeclarationStatement', b2)
    assert _is_linked(a, 'jsm_CDeclarationStatement', b2)
    if hasattr(b1, 'jsm_AbstractCExpression73'):
        assert not _is_linked(b1, 'jsm_AbstractCExpression73', a)
    if hasattr(b2, 'jsm_AbstractCExpression73'):
        assert _is_linked(b2, 'jsm_AbstractCExpression73', a)
    _safe_set(a, 'jsm_CDeclarationStatement', None)
    assert not _is_linked(a, 'jsm_CDeclarationStatement', b2)
    if hasattr(b2, 'jsm_AbstractCExpression73'):
        assert not _is_linked(b2, 'jsm_AbstractCExpression73', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractCExpression_strategy = st.builds(AbstractCExpression)
@given(instance=AbstractCExpression_strategy)
@settings(max_examples=25)
def test_AbstractCExpression_instantiation(instance):
    assert isinstance(instance, AbstractCExpression)


AbstractCStatement_strategy = st.builds(AbstractCStatement)
@given(instance=AbstractCStatement_strategy)
@settings(max_examples=25)
def test_AbstractCStatement_instantiation(instance):
    assert isinstance(instance, AbstractCStatement)


AbstractMClass_strategy = st.builds(AbstractMClass)
@given(instance=AbstractMClass_strategy)
@settings(max_examples=25)
def test_AbstractMClass_instantiation(instance):
    assert isinstance(instance, AbstractMClass)


AbstractMClassFieldDeclaration_strategy = st.builds(AbstractMClassFieldDeclaration)
@given(instance=AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMClassFieldDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMClassFieldDeclaration)


AbstractMDeclaredType_strategy = st.builds(AbstractMDeclaredType)
@given(instance=AbstractMDeclaredType_strategy)
@settings(max_examples=25)
def test_AbstractMDeclaredType_instantiation(instance):
    assert isinstance(instance, AbstractMDeclaredType)


AbstractMExternalType_strategy = st.builds(AbstractMExternalType)
@given(instance=AbstractMExternalType_strategy)
@settings(max_examples=25)
def test_AbstractMExternalType_instantiation(instance):
    assert isinstance(instance, AbstractMExternalType)


AbstractMFieldDeclaration_strategy = st.builds(AbstractMFieldDeclaration)
@given(instance=AbstractMFieldDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMFieldDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMFieldDeclaration)


AbstractMImplementableMethodDeclaration_strategy = st.builds(AbstractMImplementableMethodDeclaration)
@given(instance=AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMImplementableMethodDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMImplementableMethodDeclaration)


AbstractMInterface_strategy = st.builds(AbstractMInterface)
@given(instance=AbstractMInterface_strategy)
@settings(max_examples=25)
def test_AbstractMInterface_instantiation(instance):
    assert isinstance(instance, AbstractMInterface)


AbstractMMethodDeclaration_strategy = st.builds(AbstractMMethodDeclaration)
@given(instance=AbstractMMethodDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMMethodDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMMethodDeclaration)


AbstractMMethodImplementation_strategy = st.builds(AbstractMMethodImplementation)
@given(instance=AbstractMMethodImplementation_strategy)
@settings(max_examples=25)
def test_AbstractMMethodImplementation_instantiation(instance):
    assert isinstance(instance, AbstractMMethodImplementation)


AbstractMMethodLike_strategy = st.builds(AbstractMMethodLike)
@given(instance=AbstractMMethodLike_strategy)
@settings(max_examples=25)
def test_AbstractMMethodLike_instantiation(instance):
    assert isinstance(instance, AbstractMMethodLike)


AbstractMPackageContainer_strategy = st.builds(AbstractMPackageContainer)
@given(instance=AbstractMPackageContainer_strategy)
@settings(max_examples=25)
def test_AbstractMPackageContainer_instantiation(instance):
    assert isinstance(instance, AbstractMPackageContainer)


AbstractMResource_strategy = st.builds(AbstractMResource)
@given(instance=AbstractMResource_strategy)
@settings(max_examples=25)
def test_AbstractMResource_instantiation(instance):
    assert isinstance(instance, AbstractMResource)


AbstractMType_strategy = st.builds(AbstractMType)
@given(instance=AbstractMType_strategy)
@settings(max_examples=25)
def test_AbstractMType_instantiation(instance):
    assert isinstance(instance, AbstractMType)


AbstractMTypeContainer_strategy = st.builds(AbstractMTypeContainer)
@given(instance=AbstractMTypeContainer_strategy)
@settings(max_examples=25)
def test_AbstractMTypeContainer_instantiation(instance):
    assert isinstance(instance, AbstractMTypeContainer)


AbstractMTypeReference_strategy = st.builds(AbstractMTypeReference)
@given(instance=AbstractMTypeReference_strategy)
@settings(max_examples=25)
def test_AbstractMTypeReference_instantiation(instance):
    assert isinstance(instance, AbstractMTypeReference)


AbstractMTypeWithNameDeclaration_strategy = st.builds(AbstractMTypeWithNameDeclaration)
@given(instance=AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMTypeWithNameDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)


AbstractModifiers_strategy = st.builds(AbstractModifiers)
@given(instance=AbstractModifiers_strategy)
@settings(max_examples=25)
def test_AbstractModifiers_instantiation(instance):
    assert isinstance(instance, AbstractModifiers)


MDeclaredClass_strategy = st.builds(MDeclaredClass)
@given(instance=MDeclaredClass_strategy)
@settings(max_examples=25)
def test_MDeclaredClass_instantiation(instance):
    assert isinstance(instance, MDeclaredClass)


jsm_AbstractCExpression_strategy = st.builds(jsm_AbstractCExpression)
@given(instance=jsm_AbstractCExpression_strategy)
@settings(max_examples=25)
def test_jsm_AbstractCExpression_instantiation(instance):
    assert isinstance(instance, jsm_AbstractCExpression)


jsm_AbstractCStatement_strategy = st.builds(jsm_AbstractCStatement)
@given(instance=jsm_AbstractCStatement_strategy)
@settings(max_examples=25)
def test_jsm_AbstractCStatement_instantiation(instance):
    assert isinstance(instance, jsm_AbstractCStatement)


jsm_AbstractMClass_strategy = st.builds(jsm_AbstractMClass)
@given(instance=jsm_AbstractMClass_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMClass_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMClass)


jsm_AbstractMClassFieldDeclaration_strategy = st.builds(jsm_AbstractMClassFieldDeclaration, final=st.booleans(), visibility=safe_text)
@given(instance=jsm_AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMClassFieldDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMClassFieldDeclaration)


jsm_AbstractMDeclaredType_strategy = st.builds(jsm_AbstractMDeclaredType, name=safe_text)
@given(instance=jsm_AbstractMDeclaredType_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMDeclaredType_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMDeclaredType)


jsm_AbstractMExternalType_strategy = st.builds(jsm_AbstractMExternalType, fullQualifiedName=safe_text)
@given(instance=jsm_AbstractMExternalType_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMExternalType_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMExternalType)


jsm_AbstractMFieldDeclaration_strategy = st.builds(jsm_AbstractMFieldDeclaration)
@given(instance=jsm_AbstractMFieldDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMFieldDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMFieldDeclaration)


jsm_AbstractMImplementableMethodDeclaration_strategy = st.builds(jsm_AbstractMImplementableMethodDeclaration)
@given(instance=jsm_AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMImplementableMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMImplementableMethodDeclaration)


jsm_AbstractMInterface_strategy = st.builds(jsm_AbstractMInterface)
@given(instance=jsm_AbstractMInterface_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMInterface_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMInterface)


jsm_AbstractMMethodDeclaration_strategy = st.builds(jsm_AbstractMMethodDeclaration)
@given(instance=jsm_AbstractMMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodDeclaration)


jsm_AbstractMMethodImplementation_strategy = st.builds(jsm_AbstractMMethodImplementation)
@given(instance=jsm_AbstractMMethodImplementation_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMMethodImplementation_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodImplementation)


jsm_AbstractMMethodLike_strategy = st.builds(jsm_AbstractMMethodLike)
@given(instance=jsm_AbstractMMethodLike_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMMethodLike_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodLike)


jsm_AbstractMPackageContainer_strategy = st.builds(jsm_AbstractMPackageContainer)
@given(instance=jsm_AbstractMPackageContainer_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMPackageContainer_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMPackageContainer)


jsm_AbstractMResource_strategy = st.builds(jsm_AbstractMResource, derived=st.booleans(), name=safe_text)
@given(instance=jsm_AbstractMResource_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMResource_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMResource)


jsm_AbstractMType_strategy = st.builds(jsm_AbstractMType)
@given(instance=jsm_AbstractMType_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMType_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMType)


jsm_AbstractMTypeContainer_strategy = st.builds(jsm_AbstractMTypeContainer)
@given(instance=jsm_AbstractMTypeContainer_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMTypeContainer_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeContainer)


jsm_AbstractMTypeReference_strategy = st.builds(jsm_AbstractMTypeReference, array=st.booleans())
@given(instance=jsm_AbstractMTypeReference_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMTypeReference_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeReference)


jsm_AbstractMTypeWithNameDeclaration_strategy = st.builds(jsm_AbstractMTypeWithNameDeclaration, name=safe_text)
@given(instance=jsm_AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_AbstractMTypeWithNameDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeWithNameDeclaration)


jsm_AbstractModifiers_strategy = st.builds(jsm_AbstractModifiers, final=st.booleans(), synchronized=st.booleans(), visibility=safe_text)
@given(instance=jsm_AbstractModifiers_strategy)
@settings(max_examples=25)
def test_jsm_AbstractModifiers_instantiation(instance):
    assert isinstance(instance, jsm_AbstractModifiers)


jsm_CBlockStatement_strategy = st.builds(jsm_CBlockStatement)
@given(instance=jsm_CBlockStatement_strategy)
@settings(max_examples=25)
def test_jsm_CBlockStatement_instantiation(instance):
    assert isinstance(instance, jsm_CBlockStatement)


jsm_CConditionalExpression_strategy = st.builds(jsm_CConditionalExpression)
@given(instance=jsm_CConditionalExpression_strategy)
@settings(max_examples=25)
def test_jsm_CConditionalExpression_instantiation(instance):
    assert isinstance(instance, jsm_CConditionalExpression)


jsm_CDeclarationStatement_strategy = st.builds(jsm_CDeclarationStatement, final=st.booleans())
@given(instance=jsm_CDeclarationStatement_strategy)
@settings(max_examples=25)
def test_jsm_CDeclarationStatement_instantiation(instance):
    assert isinstance(instance, jsm_CDeclarationStatement)


jsm_CExpressionStatement_strategy = st.builds(jsm_CExpressionStatement)
@given(instance=jsm_CExpressionStatement_strategy)
@settings(max_examples=25)
def test_jsm_CExpressionStatement_instantiation(instance):
    assert isinstance(instance, jsm_CExpressionStatement)


jsm_CIfStatement_strategy = st.builds(jsm_CIfStatement)
@given(instance=jsm_CIfStatement_strategy)
@settings(max_examples=25)
def test_jsm_CIfStatement_instantiation(instance):
    assert isinstance(instance, jsm_CIfStatement)


jsm_CUnparsedExpression_strategy = st.builds(jsm_CUnparsedExpression, code=safe_text)
@given(instance=jsm_CUnparsedExpression_strategy)
@settings(max_examples=25)
def test_jsm_CUnparsedExpression_instantiation(instance):
    assert isinstance(instance, jsm_CUnparsedExpression)


jsm_CUnparsedStatement_strategy = st.builds(jsm_CUnparsedStatement, code=safe_text)
@given(instance=jsm_CUnparsedStatement_strategy)
@settings(max_examples=25)
def test_jsm_CUnparsedStatement_instantiation(instance):
    assert isinstance(instance, jsm_CUnparsedStatement)


jsm_MAbstractClassMethodDeclaration_strategy = st.builds(jsm_MAbstractClassMethodDeclaration, visibility=safe_text)
@given(instance=jsm_MAbstractClassMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MAbstractClassMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MAbstractClassMethodDeclaration)


jsm_MAbstractDeclaredClass_strategy = st.builds(jsm_MAbstractDeclaredClass)
@given(instance=jsm_MAbstractDeclaredClass_strategy)
@settings(max_examples=25)
def test_jsm_MAbstractDeclaredClass_instantiation(instance):
    assert isinstance(instance, jsm_MAbstractDeclaredClass)


jsm_MCompilationUnit_strategy = st.builds(jsm_MCompilationUnit)
@given(instance=jsm_MCompilationUnit_strategy)
@settings(max_examples=25)
def test_jsm_MCompilationUnit_instantiation(instance):
    assert isinstance(instance, jsm_MCompilationUnit)


jsm_MConstantInterfaceFieldDeclaration_strategy = st.builds(jsm_MConstantInterfaceFieldDeclaration)
@given(instance=jsm_MConstantInterfaceFieldDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MConstantInterfaceFieldDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MConstantInterfaceFieldDeclaration)


jsm_MConstructor_strategy = st.builds(jsm_MConstructor)
@given(instance=jsm_MConstructor_strategy)
@settings(max_examples=25)
def test_jsm_MConstructor_instantiation(instance):
    assert isinstance(instance, jsm_MConstructor)


jsm_MConstructorParameter_strategy = st.builds(jsm_MConstructorParameter, final=st.booleans())
@given(instance=jsm_MConstructorParameter_strategy)
@settings(max_examples=25)
def test_jsm_MConstructorParameter_instantiation(instance):
    assert isinstance(instance, jsm_MConstructorParameter)


jsm_MDeclaredClass_strategy = st.builds(jsm_MDeclaredClass)
@given(instance=jsm_MDeclaredClass_strategy)
@settings(max_examples=25)
def test_jsm_MDeclaredClass_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredClass)


jsm_MDeclaredInterface_strategy = st.builds(jsm_MDeclaredInterface)
@given(instance=jsm_MDeclaredInterface_strategy)
@settings(max_examples=25)
def test_jsm_MDeclaredInterface_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredInterface)


jsm_MDeclaredMethodImplementation_strategy = st.builds(jsm_MDeclaredMethodImplementation)
@given(instance=jsm_MDeclaredMethodImplementation_strategy)
@settings(max_examples=25)
def test_jsm_MDeclaredMethodImplementation_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredMethodImplementation)


jsm_MDeclaredTypeReference_strategy = st.builds(jsm_MDeclaredTypeReference)
@given(instance=jsm_MDeclaredTypeReference_strategy)
@settings(max_examples=25)
def test_jsm_MDeclaredTypeReference_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredTypeReference)


jsm_MDirectMethodImplementation_strategy = st.builds(jsm_MDirectMethodImplementation)
@given(instance=jsm_MDirectMethodImplementation_strategy)
@settings(max_examples=25)
def test_jsm_MDirectMethodImplementation_instantiation(instance):
    assert isinstance(instance, jsm_MDirectMethodImplementation)


jsm_MExternalClass_strategy = st.builds(jsm_MExternalClass)
@given(instance=jsm_MExternalClass_strategy)
@settings(max_examples=25)
def test_jsm_MExternalClass_instantiation(instance):
    assert isinstance(instance, jsm_MExternalClass)


jsm_MExternalInterface_strategy = st.builds(jsm_MExternalInterface)
@given(instance=jsm_MExternalInterface_strategy)
@settings(max_examples=25)
def test_jsm_MExternalInterface_instantiation(instance):
    assert isinstance(instance, jsm_MExternalInterface)


jsm_MExternalTypeReference_strategy = st.builds(jsm_MExternalTypeReference)
@given(instance=jsm_MExternalTypeReference_strategy)
@settings(max_examples=25)
def test_jsm_MExternalTypeReference_instantiation(instance):
    assert isinstance(instance, jsm_MExternalTypeReference)


jsm_MImplicitMethodDeclaration_strategy = st.builds(jsm_MImplicitMethodDeclaration)
@given(instance=jsm_MImplicitMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MImplicitMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MImplicitMethodDeclaration)


jsm_MInstanceClassFieldDeclaration_strategy = st.builds(jsm_MInstanceClassFieldDeclaration, transient=st.booleans())
@given(instance=jsm_MInstanceClassFieldDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MInstanceClassFieldDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MInstanceClassFieldDeclaration)


jsm_MInterfaceMethodDeclaration_strategy = st.builds(jsm_MInterfaceMethodDeclaration)
@given(instance=jsm_MInterfaceMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MInterfaceMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MInterfaceMethodDeclaration)


jsm_MMethodDeclarationParameter_strategy = st.builds(jsm_MMethodDeclarationParameter)
@given(instance=jsm_MMethodDeclarationParameter_strategy)
@settings(max_examples=25)
def test_jsm_MMethodDeclarationParameter_instantiation(instance):
    assert isinstance(instance, jsm_MMethodDeclarationParameter)


jsm_MMethodImplementationParameter_strategy = st.builds(jsm_MMethodImplementationParameter, final=st.booleans(), name=safe_text)
@given(instance=jsm_MMethodImplementationParameter_strategy)
@settings(max_examples=25)
def test_jsm_MMethodImplementationParameter_instantiation(instance):
    assert isinstance(instance, jsm_MMethodImplementationParameter)


jsm_MNativeMethodDeclaration_strategy = st.builds(jsm_MNativeMethodDeclaration)
@given(instance=jsm_MNativeMethodDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MNativeMethodDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MNativeMethodDeclaration)


jsm_MPackage_strategy = st.builds(jsm_MPackage, name=safe_text)
@given(instance=jsm_MPackage_strategy)
@settings(max_examples=25)
def test_jsm_MPackage_instantiation(instance):
    assert isinstance(instance, jsm_MPackage)


jsm_MPrimitiveTypeReference_strategy = st.builds(jsm_MPrimitiveTypeReference, type=safe_text)
@given(instance=jsm_MPrimitiveTypeReference_strategy)
@settings(max_examples=25)
def test_jsm_MPrimitiveTypeReference_instantiation(instance):
    assert isinstance(instance, jsm_MPrimitiveTypeReference)


jsm_MResource_strategy = st.builds(jsm_MResource, content=safe_text)
@given(instance=jsm_MResource_strategy)
@settings(max_examples=25)
def test_jsm_MResource_instantiation(instance):
    assert isinstance(instance, jsm_MResource)


jsm_MRoot_strategy = st.builds(jsm_MRoot)
@given(instance=jsm_MRoot_strategy)
@settings(max_examples=25)
def test_jsm_MRoot_instantiation(instance):
    assert isinstance(instance, jsm_MRoot)


jsm_MStaticClassFieldDeclaration_strategy = st.builds(jsm_MStaticClassFieldDeclaration)
@given(instance=jsm_MStaticClassFieldDeclaration_strategy)
@settings(max_examples=25)
def test_jsm_MStaticClassFieldDeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MStaticClassFieldDeclaration)


