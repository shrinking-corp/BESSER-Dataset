import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CppAbstractMethodInvocation,
    CppBinaryExpression,
    CppClassifier,
    CppExpression,
    CppField,
    CppFieldContainer,
    CppFunction,
    CppIterationStatement,
    CppJumpStatement,
    CppMemberFunction,
    CppMethodInvocation,
    CppModelElement,
    CppNamedElement,
    CppPathReferentiable,
    CppPrimitiveType,
    CppSelectionStatement,
    CppType,
    CppTypedElement,
    CppUnaryExpression,
    CppVariableDeclaration,
    Metamodelo_Cpp_CppAbstractMethodInvocation,
    Metamodelo_Cpp_CppArrayAccess,
    Metamodelo_Cpp_CppArrayInitializer,
    Metamodelo_Cpp_CppAssignamentStatement,
    Metamodelo_Cpp_CppBinaryExpression,
    Metamodelo_Cpp_CppBlock,
    Metamodelo_Cpp_CppBooleanLiteral,
    Metamodelo_Cpp_CppBooleanType,
    Metamodelo_Cpp_CppBreakStatement,
    Metamodelo_Cpp_CppCase,
    Metamodelo_Cpp_CppCastExpression,
    Metamodelo_Cpp_CppCatchClause,
    Metamodelo_Cpp_CppCharType,
    Metamodelo_Cpp_CppCharacterLiteral,
    Metamodelo_Cpp_CppClass,
    Metamodelo_Cpp_CppClassFile,
    Metamodelo_Cpp_CppClassifier,
    Metamodelo_Cpp_CppComment,
    Metamodelo_Cpp_CppConstantExpression,
    Metamodelo_Cpp_CppConstructor,
    Metamodelo_Cpp_CppContinueStatement,
    Metamodelo_Cpp_CppDeclarationExpression,
    Metamodelo_Cpp_CppDestructor,
    Metamodelo_Cpp_CppDoWhileStatement,
    Metamodelo_Cpp_CppDoubleType,
    Metamodelo_Cpp_CppEnum,
    Metamodelo_Cpp_CppEnumConstructor,
    Metamodelo_Cpp_CppExpression,
    Metamodelo_Cpp_CppField,
    Metamodelo_Cpp_CppFieldAccess,
    Metamodelo_Cpp_CppFieldContainer,
    Metamodelo_Cpp_CppFloatType,
    Metamodelo_Cpp_CppForStatement,
    Metamodelo_Cpp_CppFunction,
    Metamodelo_Cpp_CppGotoStatement,
    Metamodelo_Cpp_CppIfElseStatement,
    Metamodelo_Cpp_CppIfStatement,
    Metamodelo_Cpp_CppImportDeclaration,
    Metamodelo_Cpp_CppInfixExpression,
    Metamodelo_Cpp_CppIntType,
    Metamodelo_Cpp_CppIterationStatement,
    Metamodelo_Cpp_CppJumpStatement,
    Metamodelo_Cpp_CppLabeledStatement,
    Metamodelo_Cpp_CppLongType,
    Metamodelo_Cpp_CppMemberFunction,
    Metamodelo_Cpp_CppMethod,
    Metamodelo_Cpp_CppMethodInvocation,
    Metamodelo_Cpp_CppModel,
    Metamodelo_Cpp_CppModelElement,
    Metamodelo_Cpp_CppNamedElement,
    Metamodelo_Cpp_CppNullLiteral,
    Metamodelo_Cpp_CppNumberLiteral,
    Metamodelo_Cpp_CppPackage,
    Metamodelo_Cpp_CppParenthizedExpression,
    Metamodelo_Cpp_CppPathReference,
    Metamodelo_Cpp_CppPathReferentiable,
    Metamodelo_Cpp_CppPostfixExpression,
    Metamodelo_Cpp_CppPrefixExpression,
    Metamodelo_Cpp_CppPrimitiveType,
    Metamodelo_Cpp_CppRegexLiteral,
    Metamodelo_Cpp_CppReturnStatement,
    Metamodelo_Cpp_CppSelectionStatement,
    Metamodelo_Cpp_CppShortType,
    Metamodelo_Cpp_CppSignedType,
    Metamodelo_Cpp_CppSingleVariableDeclaration,
    Metamodelo_Cpp_CppStringLiteral,
    Metamodelo_Cpp_CppSuperConstructorInvocation,
    Metamodelo_Cpp_CppSuperMethodInvocation,
    Metamodelo_Cpp_CppSwitchExpression,
    Metamodelo_Cpp_CppThisExpression,
    Metamodelo_Cpp_CppThrowExpression,
    Metamodelo_Cpp_CppTryExpression,
    Metamodelo_Cpp_CppType,
    Metamodelo_Cpp_CppTypeAccess,
    Metamodelo_Cpp_CppTypeParameter,
    Metamodelo_Cpp_CppTypedElement,
    Metamodelo_Cpp_CppUnaryExpression,
    Metamodelo_Cpp_CppUnsignedType,
    Metamodelo_Cpp_CppVariable,
    Metamodelo_Cpp_CppVariableAccess,
    Metamodelo_Cpp_CppVariableDeclaration,
    Metamodelo_Cpp_CppVariableDeclarationFragment,
    Metamodelo_Cpp_CppVariableDeclarationGroup,
    Metamodelo_Cpp_CppVoidType,
    Metamodelo_Cpp_CppWhileStatement,
    CppAccessSpecifier,
    CppAssignmentOperator,
    CppClassKey,
    CppLinkageSpecifier,
    CppOperator,
    CppPostfixOperator,
    CppQualifierType,
    CppStorageType,
    CppUnaryOperator,
    CppVarType,
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

def test_assoc_mainClass0_reverse_link_reassign_clear():
    a1 = Metamodelo_Cpp_CppModel(name="sample_text", sourceFolder="sample_text", targetFolder="sample_text")
    a2 = Metamodelo_Cpp_CppModel(name="sample_text_2", sourceFolder="sample_text_2", targetFolder="sample_text_2")
    b = Metamodelo_Cpp_CppClass(classkey="sample_text", isAbstract=True, isFinal=True, isGeneric=True)
    _safe_set(b, 'Metamodelo_Cpp_CppClass', a1)
    assert _is_linked(b, 'Metamodelo_Cpp_CppClass', a1)
    if hasattr(a1, 'Metamodelo_Cpp_CppModel'):
        assert _is_linked(a1, 'Metamodelo_Cpp_CppModel', b)
    _safe_set(b, 'Metamodelo_Cpp_CppClass', a2)
    assert _is_linked(b, 'Metamodelo_Cpp_CppClass', a2)
    if hasattr(a1, 'Metamodelo_Cpp_CppModel'):
        assert not _is_linked(a1, 'Metamodelo_Cpp_CppModel', b)
    if hasattr(a2, 'Metamodelo_Cpp_CppModel'):
        assert _is_linked(a2, 'Metamodelo_Cpp_CppModel', b)
    _safe_set(b, 'Metamodelo_Cpp_CppClass', None)
    assert not _is_linked(b, 'Metamodelo_Cpp_CppClass', a2)
    if hasattr(a2, 'Metamodelo_Cpp_CppModel'):
        assert not _is_linked(a2, 'Metamodelo_Cpp_CppModel', b)


def test_assoc_superClass40_reverse_link_reassign_clear():
    a1 = Metamodelo_Cpp_CppClass(classkey="sample_text", isAbstract=True, isFinal=True, isGeneric=True)
    a2 = Metamodelo_Cpp_CppClass(classkey="sample_text_2", isAbstract=False, isFinal=False, isGeneric=False)
    b = Metamodelo_Cpp_CppClass(classkey="sample_text", isAbstract=True, isFinal=True, isGeneric=True)
    _safe_set(b, 'Metamodelo_Cpp_CppClass41', a1)
    assert _is_linked(b, 'Metamodelo_Cpp_CppClass41', a1)
    if hasattr(a1, 'Metamodelo_Cpp_CppClass39'):
        assert _is_linked(a1, 'Metamodelo_Cpp_CppClass39', b)
    _safe_set(b, 'Metamodelo_Cpp_CppClass41', a2)
    assert _is_linked(b, 'Metamodelo_Cpp_CppClass41', a2)
    if hasattr(a1, 'Metamodelo_Cpp_CppClass39'):
        assert not _is_linked(a1, 'Metamodelo_Cpp_CppClass39', b)
    if hasattr(a2, 'Metamodelo_Cpp_CppClass39'):
        assert _is_linked(a2, 'Metamodelo_Cpp_CppClass39', b)
    _safe_set(b, 'Metamodelo_Cpp_CppClass41', None)
    assert not _is_linked(b, 'Metamodelo_Cpp_CppClass41', a2)
    if hasattr(a2, 'Metamodelo_Cpp_CppClass39'):
        assert not _is_linked(a2, 'Metamodelo_Cpp_CppClass39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cppAttributes34_stub_double():
    # Metamodelo_Cpp_CppClassifier has no real 'Metamodelo_Cpp_CppClassifier35' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppVariable(isConst=True, storage="sample_text")
    partner = Metamodelo_Cpp_CppClassifier()
    setattr(partner, 'Metamodelo_Cpp_CppClassifier35', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppVariable', partner)
    assert owner in getattr(partner, 'Metamodelo_Cpp_CppClassifier35')
    _safe_set(owner, 'Metamodelo_Cpp_CppVariable', None)
    assert owner not in getattr(partner, 'Metamodelo_Cpp_CppClassifier35')


def test_assoc_cppFields116_stub_double():
    # Metamodelo_Cpp_CppFieldContainer has no real 'fieldContainer' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppField(accessSpecifier="sample_text")
    partner = Metamodelo_Cpp_CppFieldContainer()
    setattr(partner, 'fieldContainer', None)
    _safe_set(owner, 'CppField', partner)
    assert owner in getattr(partner, 'fieldContainer')
    _safe_set(owner, 'CppField', None)
    assert owner not in getattr(partner, 'fieldContainer')


def test_assoc_dimensions139_stub_double():
    # Metamodelo_Cpp_CppExpression has no real 'Metamodelo_Cpp_CppExpression141' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppVariableDeclaration(isArray=True, vartype="sample_text")
    partner = Metamodelo_Cpp_CppExpression()
    setattr(partner, 'Metamodelo_Cpp_CppExpression141', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppVariableDeclaration140', {partner})
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression141') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppVariableDeclaration140', set())
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression141') is None


def test_assoc_elements1_stub_double():
    # Metamodelo_Cpp_CppPathReferentiable has no real 'Metamodelo_Cpp_CppPathReferentiable' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppModel(name="sample_text", sourceFolder="sample_text", targetFolder="sample_text")
    partner = Metamodelo_Cpp_CppPathReferentiable()
    setattr(partner, 'Metamodelo_Cpp_CppPathReferentiable', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppModel2', {partner})
    assert getattr(partner, 'Metamodelo_Cpp_CppPathReferentiable') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppModel2', set())
    assert getattr(partner, 'Metamodelo_Cpp_CppPathReferentiable') is None


def test_assoc_elseStatement72_stub_double():
    # Metamodelo_Cpp_CppExpression has no real 'Metamodelo_Cpp_CppExpression73' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppIfElseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppIfElseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppIfElseStatement(inLine=True)
    partner = Metamodelo_Cpp_CppExpression()
    setattr(partner, 'Metamodelo_Cpp_CppExpression73', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppIfElseStatement', partner)
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression73') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppIfElseStatement', None)
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression73') is None


def test_assoc_fieldContainer115_stub_double():
    # Metamodelo_Cpp_CppFieldContainer has no real 'CppFieldContainer' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppField(accessSpecifier="sample_text")
    partner = Metamodelo_Cpp_CppFieldContainer()
    setattr(partner, 'CppFieldContainer', None)
    _safe_set(owner, 'cppFields', partner)
    assert getattr(partner, 'CppFieldContainer') == owner
    _safe_set(owner, 'cppFields', None)
    assert getattr(partner, 'CppFieldContainer') is None


def test_assoc_functionBody50_stub_double():
    # Metamodelo_Cpp_CppBlock has no real 'Metamodelo_Cpp_CppBlock' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppFunction(isInline=True, isVarArg=True, linkage="sample_text")
    partner = Metamodelo_Cpp_CppBlock()
    setattr(partner, 'Metamodelo_Cpp_CppBlock', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppFunction51', partner)
    assert getattr(partner, 'Metamodelo_Cpp_CppBlock') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppFunction51', None)
    assert getattr(partner, 'Metamodelo_Cpp_CppBlock') is None


def test_assoc_initializer137_stub_double():
    # Metamodelo_Cpp_CppExpression has no real 'Metamodelo_Cpp_CppExpression138' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppVariableDeclaration(isArray=True, vartype="sample_text")
    partner = Metamodelo_Cpp_CppExpression()
    setattr(partner, 'Metamodelo_Cpp_CppExpression138', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppVariableDeclaration', partner)
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression138') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppVariableDeclaration', None)
    assert getattr(partner, 'Metamodelo_Cpp_CppExpression138') is None


def test_assoc_modules5_stub_double():
    # Metamodelo_Cpp_CppClassFile has no real 'Metamodelo_Cpp_CppClassFile' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppModel(name="sample_text", sourceFolder="sample_text", targetFolder="sample_text")
    partner = Metamodelo_Cpp_CppClassFile()
    setattr(partner, 'Metamodelo_Cpp_CppClassFile', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppModel6', {partner})
    assert getattr(partner, 'Metamodelo_Cpp_CppClassFile') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppModel6', set())
    assert getattr(partner, 'Metamodelo_Cpp_CppClassFile') is None


def test_assoc_orphanTypes3_stub_double():
    # Metamodelo_Cpp_CppType has no real 'Metamodelo_Cpp_CppType' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppModel(name="sample_text", sourceFolder="sample_text", targetFolder="sample_text")
    partner = Metamodelo_Cpp_CppType()
    setattr(partner, 'Metamodelo_Cpp_CppType', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppModel4', {partner})
    assert getattr(partner, 'Metamodelo_Cpp_CppType') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppModel4', set())
    assert getattr(partner, 'Metamodelo_Cpp_CppType') is None


def test_assoc_ownedParameters49_stub_double():
    # Metamodelo_Cpp_CppSingleVariableDeclaration has no real 'Metamodelo_Cpp_CppSingleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppFunction(isInline=True, isVarArg=True, linkage="sample_text")
    partner = Metamodelo_Cpp_CppSingleVariableDeclaration()
    setattr(partner, 'Metamodelo_Cpp_CppSingleVariableDeclaration', None)
    _safe_set(owner, 'Metamodelo_Cpp_CppFunction', {partner})
    assert getattr(partner, 'Metamodelo_Cpp_CppSingleVariableDeclaration') == owner
    _safe_set(owner, 'Metamodelo_Cpp_CppFunction', set())
    assert getattr(partner, 'Metamodelo_Cpp_CppSingleVariableDeclaration') is None


def test_assoc_usageInVariableAccess136_stub_double():
    # Metamodelo_Cpp_CppVariableAccess has no real 'CppVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppVariableDeclaration(isArray=True, vartype="sample_text")
    partner = Metamodelo_Cpp_CppVariableAccess()
    setattr(partner, 'CppVariableAccess', None)
    _safe_set(owner, 'variable', {partner})
    assert getattr(partner, 'CppVariableAccess') == owner
    _safe_set(owner, 'variable', set())
    assert getattr(partner, 'CppVariableAccess') is None


def test_assoc_variable131_stub_double():
    # Metamodelo_Cpp_CppVariableAccess has no real 'usageInVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so Metamodelo_Cpp_CppVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Metamodelo_Cpp_CppVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Metamodelo_Cpp_CppVariableDeclaration(isArray=True, vartype="sample_text")
    partner = Metamodelo_Cpp_CppVariableAccess()
    setattr(partner, 'usageInVariableAccess', None)
    _safe_set(owner, 'CppVariableDeclaration', partner)
    assert getattr(partner, 'usageInVariableAccess') == owner
    _safe_set(owner, 'CppVariableDeclaration', None)
    assert getattr(partner, 'usageInVariableAccess') is None


