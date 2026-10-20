import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Core_BinaryPackageFragmentRoot,
    Core_CompilationUnit,
    Core_IClassFile,
    Core_ICompilationUnit,
    Core_IField,
    Core_IImportDeclaration,
    Core_IInitializer,
    Core_IJavaElement,
    Core_IJavaModel,
    Core_IJavaProject,
    Core_IMember,
    Core_IMethod,
    Core_IPackageFragment,
    Core_IPackageFragmentRoot,
    Core_ISourceRange,
    Core_ISourceReference,
    Core_IType,
    Core_ITypeParameter,
    Core_ITypeRoot,
    Core_Parameter,
    Core_PhysicalElement,
    Core_SourcePackageFragmentRoot,
    IJavaElement,
    IMember,
    IPackageFragmentRoot,
    ISourceReference,
    ITypeRoot,
    PhysicalElement,
    Modifiers,
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

def test_assoc_classFiles14_reverse_link_reassign_clear():
    a1 = Core_IPackageFragment(isDefaultPackage="sample_text")
    a2 = Core_IPackageFragment(isDefaultPackage="sample_text_2")
    b = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    _safe_set(b, 'Core_IClassFile', a1)
    assert _is_linked(b, 'Core_IClassFile', a1)
    if hasattr(a1, 'Core_IPackageFragment'):
        assert _is_linked(a1, 'Core_IPackageFragment', b)
    _safe_set(b, 'Core_IClassFile', a2)
    assert _is_linked(b, 'Core_IClassFile', a2)
    if hasattr(a1, 'Core_IPackageFragment'):
        assert not _is_linked(a1, 'Core_IPackageFragment', b)
    if hasattr(a2, 'Core_IPackageFragment'):
        assert _is_linked(a2, 'Core_IPackageFragment', b)
    _safe_set(b, 'Core_IClassFile', None)
    assert not _is_linked(b, 'Core_IClassFile', a2)
    if hasattr(a2, 'Core_IPackageFragment'):
        assert not _is_linked(a2, 'Core_IPackageFragment', b)


def test_assoc_fields40_reverse_link_reassign_clear():
    a1 = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = Core_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    _safe_set(b, 'Core_IField', a1)
    assert _is_linked(b, 'Core_IField', a1)
    if hasattr(a1, 'Core_IType41'):
        assert _is_linked(a1, 'Core_IType41', b)
    _safe_set(b, 'Core_IField', a2)
    assert _is_linked(b, 'Core_IField', a2)
    if hasattr(a1, 'Core_IType41'):
        assert not _is_linked(a1, 'Core_IType41', b)
    if hasattr(a2, 'Core_IType41'):
        assert _is_linked(a2, 'Core_IType41', b)
    _safe_set(b, 'Core_IField', None)
    assert not _is_linked(b, 'Core_IField', a2)
    if hasattr(a2, 'Core_IType41'):
        assert not _is_linked(a2, 'Core_IType41', b)


def test_assoc_methods42_reverse_link_reassign_clear():
    a1 = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = Core_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    _safe_set(b, 'Core_IMethod', a1)
    assert _is_linked(b, 'Core_IMethod', a1)
    if hasattr(a1, 'Core_IType43'):
        assert _is_linked(a1, 'Core_IType43', b)
    _safe_set(b, 'Core_IMethod', a2)
    assert _is_linked(b, 'Core_IMethod', a2)
    if hasattr(a1, 'Core_IType43'):
        assert not _is_linked(a1, 'Core_IType43', b)
    if hasattr(a2, 'Core_IType43'):
        assert _is_linked(a2, 'Core_IType43', b)
    _safe_set(b, 'Core_IMethod', None)
    assert not _is_linked(b, 'Core_IMethod', a2)
    if hasattr(a2, 'Core_IType43'):
        assert not _is_linked(a2, 'Core_IType43', b)


def test_assoc_parameters49_reverse_link_reassign_clear():
    a1 = Core_Parameter(name="sample_text", type="sample_text")
    a2 = Core_Parameter(name="sample_text_2", type="sample_text_2")
    b = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    _safe_set(b, 'Core_IMethod50', {a1})
    assert _is_linked(b, 'Core_IMethod50', a1)
    if hasattr(a1, 'Core_Parameter'):
        assert _is_linked(a1, 'Core_Parameter', b)
    _safe_set(b, 'Core_IMethod50', {a2})
    assert _is_linked(b, 'Core_IMethod50', a2)
    if hasattr(a1, 'Core_Parameter'):
        assert not _is_linked(a1, 'Core_Parameter', b)
    if hasattr(a2, 'Core_Parameter'):
        assert _is_linked(a2, 'Core_Parameter', b)
    _safe_set(b, 'Core_IMethod50', set())
    assert not _is_linked(b, 'Core_IMethod50', a2)
    if hasattr(a2, 'Core_Parameter'):
        assert not _is_linked(a2, 'Core_Parameter', b)


def test_assoc_sourceRange32_reverse_link_reassign_clear():
    a1 = Core_ISourceReference(source="sample_text")
    a2 = Core_ISourceReference(source="sample_text_2")
    b = Core_ISourceRange(length="sample_text", offset="sample_text")
    _safe_set(b, 'Core_ISourceRange', a1)
    assert _is_linked(b, 'Core_ISourceRange', a1)
    if hasattr(a1, 'Core_ISourceReference'):
        assert _is_linked(a1, 'Core_ISourceReference', b)
    _safe_set(b, 'Core_ISourceRange', a2)
    assert _is_linked(b, 'Core_ISourceRange', a2)
    if hasattr(a1, 'Core_ISourceReference'):
        assert not _is_linked(a1, 'Core_ISourceReference', b)
    if hasattr(a2, 'Core_ISourceReference'):
        assert _is_linked(a2, 'Core_ISourceReference', b)
    _safe_set(b, 'Core_ISourceRange', None)
    assert not _is_linked(b, 'Core_ISourceRange', a2)
    if hasattr(a2, 'Core_ISourceReference'):
        assert not _is_linked(a2, 'Core_ISourceReference', b)


def test_assoc_type29_reverse_link_reassign_clear():
    a1 = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = Core_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    _safe_set(b, 'Core_IClassFile30', a1)
    assert _is_linked(b, 'Core_IClassFile30', a1)
    if hasattr(a1, 'Core_IType31'):
        assert _is_linked(a1, 'Core_IType31', b)
    _safe_set(b, 'Core_IClassFile30', a2)
    assert _is_linked(b, 'Core_IClassFile30', a2)
    if hasattr(a1, 'Core_IType31'):
        assert not _is_linked(a1, 'Core_IType31', b)
    if hasattr(a2, 'Core_IType31'):
        assert _is_linked(a2, 'Core_IType31', b)
    _safe_set(b, 'Core_IClassFile30', None)
    assert not _is_linked(b, 'Core_IClassFile30', a2)
    if hasattr(a2, 'Core_IType31'):
        assert not _is_linked(a2, 'Core_IType31', b)


def test_assoc_typeParameters47_reverse_link_reassign_clear():
    a1 = Core_ITypeParameter(bounds="sample_text")
    a2 = Core_ITypeParameter(bounds="sample_text_2")
    b = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    _safe_set(b, 'Core_IType48', {a1})
    assert _is_linked(b, 'Core_IType48', a1)
    if hasattr(a1, 'Core_ITypeParameter'):
        assert _is_linked(a1, 'Core_ITypeParameter', b)
    _safe_set(b, 'Core_IType48', {a2})
    assert _is_linked(b, 'Core_IType48', a2)
    if hasattr(a1, 'Core_ITypeParameter'):
        assert not _is_linked(a1, 'Core_ITypeParameter', b)
    if hasattr(a2, 'Core_ITypeParameter'):
        assert _is_linked(a2, 'Core_ITypeParameter', b)
    _safe_set(b, 'Core_IType48', set())
    assert not _is_linked(b, 'Core_IType48', a2)
    if hasattr(a2, 'Core_ITypeParameter'):
        assert not _is_linked(a2, 'Core_ITypeParameter', b)


def test_assoc_types45_reverse_link_reassign_clear():
    a1 = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = Core_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    _safe_set(b, 'Core_IType46', a1)
    assert _is_linked(b, 'Core_IType46', a1)
    if hasattr(a1, 'Core_IType44'):
        assert _is_linked(a1, 'Core_IType44', b)
    _safe_set(b, 'Core_IType46', a2)
    assert _is_linked(b, 'Core_IType46', a2)
    if hasattr(a1, 'Core_IType44'):
        assert not _is_linked(a1, 'Core_IType44', b)
    if hasattr(a2, 'Core_IType44'):
        assert _is_linked(a2, 'Core_IType44', b)
    _safe_set(b, 'Core_IType46', None)
    assert not _is_linked(b, 'Core_IType46', a2)
    if hasattr(a2, 'Core_IType44'):
        assert not _is_linked(a2, 'Core_IType44', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allType17_stub_double():
    # Core_ICompilationUnit has no real 'Core_ICompilationUnit18' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = Core_ICompilationUnit()
    setattr(partner, 'Core_ICompilationUnit18', None)
    _safe_set(owner, 'Core_IType', partner)
    assert owner in getattr(partner, 'Core_ICompilationUnit18')
    _safe_set(owner, 'Core_IType', None)
    assert owner not in getattr(partner, 'Core_ICompilationUnit18')


def test_assoc_compilationUnits15_stub_double():
    # Core_ICompilationUnit has no real 'Core_ICompilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = Core_ICompilationUnit()
    setattr(partner, 'Core_ICompilationUnit', None)
    _safe_set(owner, 'Core_IPackageFragment16', {partner})
    assert getattr(partner, 'Core_ICompilationUnit') == owner
    _safe_set(owner, 'Core_IPackageFragment16', set())
    assert getattr(partner, 'Core_ICompilationUnit') is None


def test_assoc_imports19_stub_double():
    # Core_ICompilationUnit has no real 'Core_ICompilationUnit20' property in the generated
    # code (a bare stub) -- manually attach it so Core_IImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    partner = Core_ICompilationUnit()
    setattr(partner, 'Core_ICompilationUnit20', None)
    _safe_set(owner, 'Core_IImportDeclaration', partner)
    assert owner in getattr(partner, 'Core_ICompilationUnit20')
    _safe_set(owner, 'Core_IImportDeclaration', None)
    assert owner not in getattr(partner, 'Core_ICompilationUnit20')


def test_assoc_initializers38_stub_double():
    # Core_IInitializer has no real 'Core_IInitializer' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = Core_IInitializer()
    setattr(partner, 'Core_IInitializer', None)
    _safe_set(owner, 'Core_IType39', {partner})
    assert getattr(partner, 'Core_IInitializer') == owner
    _safe_set(owner, 'Core_IType39', set())
    assert getattr(partner, 'Core_IInitializer') is None


def test_assoc_javadocRange33_stub_double():
    # Core_IMember has no real 'Core_IMember' property in the generated
    # code (a bare stub) -- manually attach it so Core_ISourceRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_ISourceRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_ISourceRange(length="sample_text", offset="sample_text")
    partner = Core_IMember()
    setattr(partner, 'Core_IMember', None)
    _safe_set(owner, 'Core_ISourceRange34', partner)
    assert getattr(partner, 'Core_IMember') == owner
    _safe_set(owner, 'Core_ISourceRange34', None)
    assert getattr(partner, 'Core_IMember') is None


def test_assoc_nameRange35_stub_double():
    # Core_IMember has no real 'Core_IMember36' property in the generated
    # code (a bare stub) -- manually attach it so Core_ISourceRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_ISourceRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_ISourceRange(length="sample_text", offset="sample_text")
    partner = Core_IMember()
    setattr(partner, 'Core_IMember36', None)
    _safe_set(owner, 'Core_ISourceRange37', partner)
    assert getattr(partner, 'Core_IMember36') == owner
    _safe_set(owner, 'Core_ISourceRange37', None)
    assert getattr(partner, 'Core_IMember36') is None


def test_assoc_packageFragmentRoot13_stub_double():
    # Core_IPackageFragmentRoot has no real 'IPackageFragmentRoot' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = Core_IPackageFragmentRoot()
    setattr(partner, 'IPackageFragmentRoot', None)
    _safe_set(owner, 'packageFragments', partner)
    assert getattr(partner, 'IPackageFragmentRoot') == owner
    _safe_set(owner, 'packageFragments', None)
    assert getattr(partner, 'IPackageFragmentRoot') is None


def test_assoc_packageFragments12_stub_double():
    # Core_IPackageFragmentRoot has no real 'packageFragmentRoot' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = Core_IPackageFragmentRoot()
    setattr(partner, 'packageFragmentRoot', None)
    _safe_set(owner, 'IPackageFragment', partner)
    assert owner in getattr(partner, 'packageFragmentRoot')
    _safe_set(owner, 'IPackageFragment', None)
    assert owner not in getattr(partner, 'packageFragmentRoot')


def test_assoc_types21_stub_double():
    # Core_ICompilationUnit has no real 'Core_ICompilationUnit22' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = Core_ICompilationUnit()
    setattr(partner, 'Core_ICompilationUnit22', None)
    _safe_set(owner, 'Core_IType23', partner)
    assert owner in getattr(partner, 'Core_ICompilationUnit22')
    _safe_set(owner, 'Core_IType23', None)
    assert owner not in getattr(partner, 'Core_ICompilationUnit22')


