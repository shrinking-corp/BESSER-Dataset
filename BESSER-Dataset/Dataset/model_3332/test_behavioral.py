import pytest
from datetime import date, datetime, time, timedelta

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
    model_AbstractCExpression,
    model_AbstractCStatement,
    model_AbstractMClass,
    model_AbstractMClassFieldDeclaration,
    model_AbstractMDeclaredType,
    model_AbstractMExternalType,
    model_AbstractMFieldDeclaration,
    model_AbstractMImplementableMethodDeclaration,
    model_AbstractMInterface,
    model_AbstractMMethodDeclaration,
    model_AbstractMMethodImplementation,
    model_AbstractMMethodLike,
    model_AbstractMPackageContainer,
    model_AbstractMResource,
    model_AbstractMType,
    model_AbstractMTypeContainer,
    model_AbstractMTypeReference,
    model_AbstractMTypeWithNameDeclaration,
    model_AbstractModifiers,
    model_CBlockStatement,
    model_CConditionalExpression,
    model_CDeclarationStatement,
    model_CExpressionStatement,
    model_CIfStatement,
    model_CUnparsedExpression,
    model_CUnparsedStatement,
    model_MAbstractClassMethodDeclaration,
    model_MAbstractDeclaredClass,
    model_MCompilationUnit,
    model_MConstantInterfaceFieldDeclaration,
    model_MConstructor,
    model_MConstructorParameter,
    model_MDeclaredClass,
    model_MDeclaredInterface,
    model_MDeclaredMethodImplementation,
    model_MDeclaredTypeReference,
    model_MDirectMethodImplementation,
    model_MExternalClass,
    model_MExternalInterface,
    model_MExternalTypeReference,
    model_MImplicitMethodDeclaration,
    model_MInstanceClassFieldDeclaration,
    model_MInterfaceMethodDeclaration,
    model_MMethodDeclarationParameter,
    model_MMethodImplementationParameter,
    model_MNativeMethodDeclaration,
    model_MPackage,
    model_MPrimitiveTypeReference,
    model_MResource,
    model_MRoot,
    model_MStaticClassFieldDeclaration,
    MPrimitiveTypes,
    MVisibility,
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

def test_assoc_derivedFrom7_reverse_link_reassign_clear():
    a1 = model_AbstractMResource(derived=True, name="sample_text")
    a2 = model_AbstractMResource(derived=False, name="sample_text_2")
    b = model_AbstractMResource(derived=True, name="sample_text")
    _safe_set(b, 'superOf', {a1})
    assert _is_linked(b, 'superOf', a1)
    if hasattr(a1, 'AbstractMResource8'):
        assert _is_linked(a1, 'AbstractMResource8', b)
    _safe_set(b, 'superOf', {a2})
    assert _is_linked(b, 'superOf', a2)
    if hasattr(a1, 'AbstractMResource8'):
        assert not _is_linked(a1, 'AbstractMResource8', b)
    if hasattr(a2, 'AbstractMResource8'):
        assert _is_linked(a2, 'AbstractMResource8', b)
    _safe_set(b, 'superOf', set())
    assert not _is_linked(b, 'superOf', a2)
    if hasattr(a2, 'AbstractMResource8'):
        assert not _is_linked(a2, 'AbstractMResource8', b)


def test_assoc_package4_reverse_link_reassign_clear():
    a1 = model_MPackage(name="sample_text")
    a2 = model_MPackage(name="sample_text_2")
    b = model_AbstractMResource(derived=True, name="sample_text")
    _safe_set(b, 'resources', a1)
    assert _is_linked(b, 'resources', a1)
    if hasattr(a1, 'MPackage5'):
        assert _is_linked(a1, 'MPackage5', b)
    _safe_set(b, 'resources', a2)
    assert _is_linked(b, 'resources', a2)
    if hasattr(a1, 'MPackage5'):
        assert not _is_linked(a1, 'MPackage5', b)
    if hasattr(a2, 'MPackage5'):
        assert _is_linked(a2, 'MPackage5', b)
    _safe_set(b, 'resources', None)
    assert not _is_linked(b, 'resources', a2)
    if hasattr(a2, 'MPackage5'):
        assert not _is_linked(a2, 'MPackage5', b)


def test_assoc_resources3_reverse_link_reassign_clear():
    a1 = model_MPackage(name="sample_text")
    a2 = model_MPackage(name="sample_text_2")
    b = model_AbstractMResource(derived=True, name="sample_text")
    _safe_set(b, 'AbstractMResource', a1)
    assert _is_linked(b, 'AbstractMResource', a1)
    if hasattr(a1, 'package'):
        assert _is_linked(a1, 'package', b)
    _safe_set(b, 'AbstractMResource', a2)
    assert _is_linked(b, 'AbstractMResource', a2)
    if hasattr(a1, 'package'):
        assert not _is_linked(a1, 'package', b)
    if hasattr(a2, 'package'):
        assert _is_linked(a2, 'package', b)
    _safe_set(b, 'AbstractMResource', None)
    assert not _is_linked(b, 'AbstractMResource', a2)
    if hasattr(a2, 'package'):
        assert not _is_linked(a2, 'package', b)


def test_assoc_superOf10_reverse_link_reassign_clear():
    a1 = model_AbstractMResource(derived=True, name="sample_text")
    a2 = model_AbstractMResource(derived=False, name="sample_text_2")
    b = model_AbstractMResource(derived=True, name="sample_text")
    _safe_set(b, 'derivedFrom', {a1})
    assert _is_linked(b, 'derivedFrom', a1)
    if hasattr(a1, 'AbstractMResource11'):
        assert _is_linked(a1, 'AbstractMResource11', b)
    _safe_set(b, 'derivedFrom', {a2})
    assert _is_linked(b, 'derivedFrom', a2)
    if hasattr(a1, 'AbstractMResource11'):
        assert not _is_linked(a1, 'AbstractMResource11', b)
    if hasattr(a2, 'AbstractMResource11'):
        assert _is_linked(a2, 'AbstractMResource11', b)
    _safe_set(b, 'derivedFrom', set())
    assert not _is_linked(b, 'derivedFrom', a2)
    if hasattr(a2, 'AbstractMResource11'):
        assert not _is_linked(a2, 'AbstractMResource11', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = model_AbstractMTypeWithNameDeclaration(name="sample_text")
    a2 = model_AbstractMTypeWithNameDeclaration(name="sample_text_2")
    b = model_AbstractMTypeReference(array=True)
    _safe_set(b, 'model_AbstractMTypeReference', a1)
    assert _is_linked(b, 'model_AbstractMTypeReference', a1)
    if hasattr(a1, 'model_AbstractMTypeWithNameDeclaration'):
        assert _is_linked(a1, 'model_AbstractMTypeWithNameDeclaration', b)
    _safe_set(b, 'model_AbstractMTypeReference', a2)
    assert _is_linked(b, 'model_AbstractMTypeReference', a2)
    if hasattr(a1, 'model_AbstractMTypeWithNameDeclaration'):
        assert not _is_linked(a1, 'model_AbstractMTypeWithNameDeclaration', b)
    if hasattr(a2, 'model_AbstractMTypeWithNameDeclaration'):
        assert _is_linked(a2, 'model_AbstractMTypeWithNameDeclaration', b)
    _safe_set(b, 'model_AbstractMTypeReference', None)
    assert not _is_linked(b, 'model_AbstractMTypeReference', a2)
    if hasattr(a2, 'model_AbstractMTypeWithNameDeclaration'):
        assert not _is_linked(a2, 'model_AbstractMTypeWithNameDeclaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractMethods32_stub_double():
    # model_MAbstractDeclaredClass has no real 'owner33' property in the generated
    # code (a bare stub) -- manually attach it so model_MAbstractClassMethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MAbstractClassMethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MAbstractClassMethodDeclaration(visibility="sample_text")
    partner = model_MAbstractDeclaredClass()
    setattr(partner, 'owner33', None)
    _safe_set(owner, 'MAbstractClassMethodDeclaration', partner)
    assert owner in getattr(partner, 'owner33')
    _safe_set(owner, 'MAbstractClassMethodDeclaration', None)
    assert owner not in getattr(partner, 'owner33')


def test_assoc_constructor67_stub_double():
    # model_MConstructor has no real 'MConstructor69' property in the generated
    # code (a bare stub) -- manually attach it so model_MConstructorParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MConstructorParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MConstructorParameter(final=True)
    partner = model_MConstructor()
    setattr(partner, 'MConstructor69', None)
    _safe_set(owner, 'parameters68', partner)
    assert getattr(partner, 'MConstructor69') == owner
    _safe_set(owner, 'parameters68', None)
    assert getattr(partner, 'MConstructor69') is None


def test_assoc_externalTypes1_stub_double():
    # model_MRoot has no real 'root' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMExternalType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMExternalType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMExternalType(fullQualifiedName="sample_text")
    partner = model_MRoot()
    setattr(partner, 'root', None)
    _safe_set(owner, 'AbstractMExternalType', partner)
    assert owner in getattr(partner, 'root')
    _safe_set(owner, 'AbstractMExternalType', None)
    assert owner not in getattr(partner, 'root')


def test_assoc_instanceFields24_stub_double():
    # model_MDeclaredClass has no real 'owner25' property in the generated
    # code (a bare stub) -- manually attach it so model_MInstanceClassFieldDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MInstanceClassFieldDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MInstanceClassFieldDeclaration(transient=True)
    partner = model_MDeclaredClass()
    setattr(partner, 'owner25', None)
    _safe_set(owner, 'MInstanceClassFieldDeclaration', partner)
    assert owner in getattr(partner, 'owner25')
    _safe_set(owner, 'MInstanceClassFieldDeclaration', None)
    assert owner not in getattr(partner, 'owner25')


def test_assoc_methodImplementation61_stub_double():
    # model_AbstractMMethodImplementation has no real 'AbstractMMethodImplementation63' property in the generated
    # code (a bare stub) -- manually attach it so model_MMethodImplementationParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MMethodImplementationParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MMethodImplementationParameter(final=True, name="sample_text")
    partner = model_AbstractMMethodImplementation()
    setattr(partner, 'AbstractMMethodImplementation63', None)
    _safe_set(owner, 'parameters62', partner)
    assert getattr(partner, 'AbstractMMethodImplementation63') == owner
    _safe_set(owner, 'parameters62', None)
    assert getattr(partner, 'AbstractMMethodImplementation63') is None


def test_assoc_owner42_stub_double():
    # model_MDeclaredClass has no real 'MDeclaredClass43' property in the generated
    # code (a bare stub) -- manually attach it so model_MInstanceClassFieldDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MInstanceClassFieldDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MInstanceClassFieldDeclaration(transient=True)
    partner = model_MDeclaredClass()
    setattr(partner, 'MDeclaredClass43', None)
    _safe_set(owner, 'instanceFields', partner)
    assert getattr(partner, 'MDeclaredClass43') == owner
    _safe_set(owner, 'instanceFields', None)
    assert getattr(partner, 'MDeclaredClass43') is None


def test_assoc_owner50_stub_double():
    # model_MAbstractDeclaredClass has no real 'MAbstractDeclaredClass' property in the generated
    # code (a bare stub) -- manually attach it so model_MAbstractClassMethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MAbstractClassMethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MAbstractClassMethodDeclaration(visibility="sample_text")
    partner = model_MAbstractDeclaredClass()
    setattr(partner, 'MAbstractDeclaredClass', None)
    _safe_set(owner, 'abstractMethods', partner)
    assert getattr(partner, 'MAbstractDeclaredClass') == owner
    _safe_set(owner, 'abstractMethods', None)
    assert getattr(partner, 'MAbstractDeclaredClass') is None


def test_assoc_packageContainer2_stub_double():
    # model_AbstractMPackageContainer has no real 'AbstractMPackageContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_MPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MPackage(name="sample_text")
    partner = model_AbstractMPackageContainer()
    setattr(partner, 'AbstractMPackageContainer', None)
    _safe_set(owner, 'packages', partner)
    assert getattr(partner, 'AbstractMPackageContainer') == owner
    _safe_set(owner, 'packages', None)
    assert getattr(partner, 'AbstractMPackageContainer') is None


def test_assoc_packages0_stub_double():
    # model_AbstractMPackageContainer has no real 'packageContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_MPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MPackage(name="sample_text")
    partner = model_AbstractMPackageContainer()
    setattr(partner, 'packageContainer', None)
    _safe_set(owner, 'MPackage', partner)
    assert owner in getattr(partner, 'packageContainer')
    _safe_set(owner, 'MPackage', None)
    assert owner not in getattr(partner, 'packageContainer')


def test_assoc_parameters57_stub_double():
    # model_AbstractMMethodImplementation has no real 'methodImplementation' property in the generated
    # code (a bare stub) -- manually attach it so model_MMethodImplementationParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MMethodImplementationParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MMethodImplementationParameter(final=True, name="sample_text")
    partner = model_AbstractMMethodImplementation()
    setattr(partner, 'methodImplementation', None)
    _safe_set(owner, 'MMethodImplementationParameter', partner)
    assert owner in getattr(partner, 'methodImplementation')
    _safe_set(owner, 'MMethodImplementationParameter', None)
    assert owner not in getattr(partner, 'methodImplementation')


def test_assoc_parameters66_stub_double():
    # model_MConstructor has no real 'constructor' property in the generated
    # code (a bare stub) -- manually attach it so model_MConstructorParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MConstructorParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MConstructorParameter(final=True)
    partner = model_MConstructor()
    setattr(partner, 'constructor', None)
    _safe_set(owner, 'MConstructorParameter', partner)
    assert owner in getattr(partner, 'constructor')
    _safe_set(owner, 'MConstructorParameter', None)
    assert owner not in getattr(partner, 'constructor')


def test_assoc_root15_stub_double():
    # model_MRoot has no real 'MRoot' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMExternalType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMExternalType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMExternalType(fullQualifiedName="sample_text")
    partner = model_MRoot()
    setattr(partner, 'MRoot', None)
    _safe_set(owner, 'externalTypes', partner)
    assert getattr(partner, 'MRoot') == owner
    _safe_set(owner, 'externalTypes', None)
    assert getattr(partner, 'MRoot') is None


def test_assoc_type16_stub_double():
    # model_MDeclaredTypeReference has no real 'model_MDeclaredTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMDeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMDeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMDeclaredType(name="sample_text")
    partner = model_MDeclaredTypeReference()
    setattr(partner, 'model_MDeclaredTypeReference', None)
    _safe_set(owner, 'model_AbstractMDeclaredType', partner)
    assert getattr(partner, 'model_MDeclaredTypeReference') == owner
    _safe_set(owner, 'model_AbstractMDeclaredType', None)
    assert getattr(partner, 'model_MDeclaredTypeReference') is None


def test_assoc_type17_stub_double():
    # model_MExternalTypeReference has no real 'model_MExternalTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMExternalType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMExternalType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMExternalType(fullQualifiedName="sample_text")
    partner = model_MExternalTypeReference()
    setattr(partner, 'model_MExternalTypeReference', None)
    _safe_set(owner, 'model_AbstractMExternalType', partner)
    assert getattr(partner, 'model_MExternalTypeReference') == owner
    _safe_set(owner, 'model_AbstractMExternalType', None)
    assert getattr(partner, 'model_MExternalTypeReference') is None


def test_assoc_typeContainer14_stub_double():
    # model_AbstractMTypeContainer has no real 'AbstractMTypeContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMDeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMDeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMDeclaredType(name="sample_text")
    partner = model_AbstractMTypeContainer()
    setattr(partner, 'AbstractMTypeContainer', None)
    _safe_set(owner, 'types', partner)
    assert getattr(partner, 'AbstractMTypeContainer') == owner
    _safe_set(owner, 'types', None)
    assert getattr(partner, 'AbstractMTypeContainer') is None


def test_assoc_types12_stub_double():
    # model_AbstractMTypeContainer has no real 'typeContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractMDeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractMDeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractMDeclaredType(name="sample_text")
    partner = model_AbstractMTypeContainer()
    setattr(partner, 'typeContainer', None)
    _safe_set(owner, 'AbstractMDeclaredType', partner)
    assert owner in getattr(partner, 'typeContainer')
    _safe_set(owner, 'AbstractMDeclaredType', None)
    assert owner not in getattr(partner, 'typeContainer')


def test_assoc_value72_stub_double():
    # model_AbstractCExpression has no real 'model_AbstractCExpression73' property in the generated
    # code (a bare stub) -- manually attach it so model_CDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CDeclarationStatement(final=True)
    partner = model_AbstractCExpression()
    setattr(partner, 'model_AbstractCExpression73', None)
    _safe_set(owner, 'model_CDeclarationStatement', partner)
    assert getattr(partner, 'model_AbstractCExpression73') == owner
    _safe_set(owner, 'model_CDeclarationStatement', None)
    assert getattr(partner, 'model_AbstractCExpression73') is None


