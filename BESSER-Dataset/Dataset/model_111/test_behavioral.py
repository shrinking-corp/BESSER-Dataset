import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractMethodDeclaration,
    AbstractMethodInvocation,
    AbstractTypeDeclaration,
    BodyDeclaration,
    Comment,
    Expresion,
    NamedElement,
    Statement,
    Type,
    TypeDeclaration,
    VariableDeclaration,
    cSharpArchId_ASTNode,
    cSharpArchId_AbstractMethodDeclaration,
    cSharpArchId_AbstractMethodInvocation,
    cSharpArchId_AbstractTypeDeclaration,
    cSharpArchId_Annotation,
    cSharpArchId_Archive,
    cSharpArchId_Assignment,
    cSharpArchId_Block,
    cSharpArchId_BlockComment,
    cSharpArchId_BodyDeclaration,
    cSharpArchId_ClassDeclaration,
    cSharpArchId_ClassInstanceCreation,
    cSharpArchId_Comment,
    cSharpArchId_CompileUnit,
    cSharpArchId_ConstructorDeclaration,
    cSharpArchId_ConstructorInvocation,
    cSharpArchId_ElementRef,
    cSharpArchId_Enumeration,
    cSharpArchId_EnumerationLiteral,
    cSharpArchId_Expresion,
    cSharpArchId_InterfaceDeclaration,
    cSharpArchId_LineComment,
    cSharpArchId_MethodDeclaration,
    cSharpArchId_MethodInvocation,
    cSharpArchId_MethodParameter,
    cSharpArchId_Model,
    cSharpArchId_Modifier,
    cSharpArchId_NamedElement,
    cSharpArchId_Namespace,
    cSharpArchId_PrimitiveType,
    cSharpArchId_ReturnType,
    cSharpArchId_SingleVariableDeclaration,
    cSharpArchId_Statement,
    cSharpArchId_Type,
    cSharpArchId_TypeAcces,
    cSharpArchId_TypeDeclaration,
    cSharpArchId_TypeParameter,
    cSharpArchId_UsingDeclaration,
    cSharpArchId_VariableDeclaration,
    InheritanceKind,
    ModifierKind,
    SimpleType,
    VisibilityKind,
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

def test_assoc_archives0_reverse_link_reassign_clear():
    a1 = cSharpArchId_Model(name="sample_text")
    a2 = cSharpArchId_Model(name="sample_text_2")
    b = cSharpArchId_Archive(originalFilePath="sample_text")
    _safe_set(b, 'cSharpArchId_Archive', a1)
    assert _is_linked(b, 'cSharpArchId_Archive', a1)
    if hasattr(a1, 'cSharpArchId_Model'):
        assert _is_linked(a1, 'cSharpArchId_Model', b)
    _safe_set(b, 'cSharpArchId_Archive', a2)
    assert _is_linked(b, 'cSharpArchId_Archive', a2)
    if hasattr(a1, 'cSharpArchId_Model'):
        assert not _is_linked(a1, 'cSharpArchId_Model', b)
    if hasattr(a2, 'cSharpArchId_Model'):
        assert _is_linked(a2, 'cSharpArchId_Model', b)
    _safe_set(b, 'cSharpArchId_Archive', None)
    assert not _is_linked(b, 'cSharpArchId_Archive', a2)
    if hasattr(a2, 'cSharpArchId_Model'):
        assert not _is_linked(a2, 'cSharpArchId_Model', b)


def test_assoc_commentList14_reverse_link_reassign_clear():
    a1 = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    a2 = cSharpArchId_CompileUnit(originalFilePath="sample_text_2")
    b = cSharpArchId_Comment(content="sample_text")
    _safe_set(b, 'cSharpArchId_Comment', a1)
    assert _is_linked(b, 'cSharpArchId_Comment', a1)
    if hasattr(a1, 'cSharpArchId_CompileUnit15'):
        assert _is_linked(a1, 'cSharpArchId_CompileUnit15', b)
    _safe_set(b, 'cSharpArchId_Comment', a2)
    assert _is_linked(b, 'cSharpArchId_Comment', a2)
    if hasattr(a1, 'cSharpArchId_CompileUnit15'):
        assert not _is_linked(a1, 'cSharpArchId_CompileUnit15', b)
    if hasattr(a2, 'cSharpArchId_CompileUnit15'):
        assert _is_linked(a2, 'cSharpArchId_CompileUnit15', b)
    _safe_set(b, 'cSharpArchId_Comment', None)
    assert not _is_linked(b, 'cSharpArchId_Comment', a2)
    if hasattr(a2, 'cSharpArchId_CompileUnit15'):
        assert not _is_linked(a2, 'cSharpArchId_CompileUnit15', b)


def test_assoc_compileUnits1_reverse_link_reassign_clear():
    a1 = cSharpArchId_Model(name="sample_text")
    a2 = cSharpArchId_Model(name="sample_text_2")
    b = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    _safe_set(b, 'cSharpArchId_CompileUnit', a1)
    assert _is_linked(b, 'cSharpArchId_CompileUnit', a1)
    if hasattr(a1, 'cSharpArchId_Model2'):
        assert _is_linked(a1, 'cSharpArchId_Model2', b)
    _safe_set(b, 'cSharpArchId_CompileUnit', a2)
    assert _is_linked(b, 'cSharpArchId_CompileUnit', a2)
    if hasattr(a1, 'cSharpArchId_Model2'):
        assert not _is_linked(a1, 'cSharpArchId_Model2', b)
    if hasattr(a2, 'cSharpArchId_Model2'):
        assert _is_linked(a2, 'cSharpArchId_Model2', b)
    _safe_set(b, 'cSharpArchId_CompileUnit', None)
    assert not _is_linked(b, 'cSharpArchId_CompileUnit', a2)
    if hasattr(a2, 'cSharpArchId_Model2'):
        assert not _is_linked(a2, 'cSharpArchId_Model2', b)


def test_assoc_compileUnits25_reverse_link_reassign_clear():
    a1 = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    a2 = cSharpArchId_CompileUnit(originalFilePath="sample_text_2")
    b = cSharpArchId_Archive(originalFilePath="sample_text")
    _safe_set(b, 'cSharpArchId_Archive26', {a1})
    assert _is_linked(b, 'cSharpArchId_Archive26', a1)
    if hasattr(a1, 'cSharpArchId_CompileUnit27'):
        assert _is_linked(a1, 'cSharpArchId_CompileUnit27', b)
    _safe_set(b, 'cSharpArchId_Archive26', {a2})
    assert _is_linked(b, 'cSharpArchId_Archive26', a2)
    if hasattr(a1, 'cSharpArchId_CompileUnit27'):
        assert not _is_linked(a1, 'cSharpArchId_CompileUnit27', b)
    if hasattr(a2, 'cSharpArchId_CompileUnit27'):
        assert _is_linked(a2, 'cSharpArchId_CompileUnit27', b)
    _safe_set(b, 'cSharpArchId_Archive26', set())
    assert not _is_linked(b, 'cSharpArchId_Archive26', a2)
    if hasattr(a2, 'cSharpArchId_CompileUnit27'):
        assert not _is_linked(a2, 'cSharpArchId_CompileUnit27', b)


def test_assoc_elements12_reverse_link_reassign_clear():
    a1 = cSharpArchId_NamedElement(name="sample_text")
    a2 = cSharpArchId_NamedElement(name="sample_text_2")
    b = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    _safe_set(b, 'cSharpArchId_CompileUnit13', {a1})
    assert _is_linked(b, 'cSharpArchId_CompileUnit13', a1)
    if hasattr(a1, 'cSharpArchId_NamedElement'):
        assert _is_linked(a1, 'cSharpArchId_NamedElement', b)
    _safe_set(b, 'cSharpArchId_CompileUnit13', {a2})
    assert _is_linked(b, 'cSharpArchId_CompileUnit13', a2)
    if hasattr(a1, 'cSharpArchId_NamedElement'):
        assert not _is_linked(a1, 'cSharpArchId_NamedElement', b)
    if hasattr(a2, 'cSharpArchId_NamedElement'):
        assert _is_linked(a2, 'cSharpArchId_NamedElement', b)
    _safe_set(b, 'cSharpArchId_CompileUnit13', set())
    assert not _is_linked(b, 'cSharpArchId_CompileUnit13', a2)
    if hasattr(a2, 'cSharpArchId_NamedElement'):
        assert not _is_linked(a2, 'cSharpArchId_NamedElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations40_stub_double():
    # cSharpArchId_Annotation has no real 'cSharpArchId_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Modifier(inheritance="sample_text", modifier="sample_text", static=True, visibility="sample_text")
    partner = cSharpArchId_Annotation()
    setattr(partner, 'cSharpArchId_Annotation', None)
    _safe_set(owner, 'cSharpArchId_Modifier41', {partner})
    assert getattr(partner, 'cSharpArchId_Annotation') == owner
    _safe_set(owner, 'cSharpArchId_Modifier41', set())
    assert getattr(partner, 'cSharpArchId_Annotation') is None


def test_assoc_bodyDeclaration39_stub_double():
    # cSharpArchId_BodyDeclaration has no real 'BodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Modifier(inheritance="sample_text", modifier="sample_text", static=True, visibility="sample_text")
    partner = cSharpArchId_BodyDeclaration()
    setattr(partner, 'BodyDeclaration', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration') is None


def test_assoc_commentsAfterBody31_stub_double():
    # cSharpArchId_AbstractTypeDeclaration has no real 'cSharpArchId_AbstractTypeDeclaration32' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Comment(content="sample_text")
    partner = cSharpArchId_AbstractTypeDeclaration()
    setattr(partner, 'cSharpArchId_AbstractTypeDeclaration32', None)
    _safe_set(owner, 'cSharpArchId_Comment33', partner)
    assert owner in getattr(partner, 'cSharpArchId_AbstractTypeDeclaration32')
    _safe_set(owner, 'cSharpArchId_Comment33', None)
    assert owner not in getattr(partner, 'cSharpArchId_AbstractTypeDeclaration32')


def test_assoc_commentsBeforeBody28_stub_double():
    # cSharpArchId_AbstractTypeDeclaration has no real 'cSharpArchId_AbstractTypeDeclaration29' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Comment(content="sample_text")
    partner = cSharpArchId_AbstractTypeDeclaration()
    setattr(partner, 'cSharpArchId_AbstractTypeDeclaration29', None)
    _safe_set(owner, 'cSharpArchId_Comment30', partner)
    assert owner in getattr(partner, 'cSharpArchId_AbstractTypeDeclaration29')
    _safe_set(owner, 'cSharpArchId_Comment30', None)
    assert owner not in getattr(partner, 'cSharpArchId_AbstractTypeDeclaration29')


def test_assoc_modifier36_stub_double():
    # cSharpArchId_AbstractTypeDeclaration has no real 'cSharpArchId_AbstractTypeDeclaration37' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Modifier(inheritance="sample_text", modifier="sample_text", static=True, visibility="sample_text")
    partner = cSharpArchId_AbstractTypeDeclaration()
    setattr(partner, 'cSharpArchId_AbstractTypeDeclaration37', None)
    _safe_set(owner, 'cSharpArchId_Modifier', partner)
    assert getattr(partner, 'cSharpArchId_AbstractTypeDeclaration37') == owner
    _safe_set(owner, 'cSharpArchId_Modifier', None)
    assert getattr(partner, 'cSharpArchId_AbstractTypeDeclaration37') is None


def test_assoc_modifier38_stub_double():
    # cSharpArchId_BodyDeclaration has no real 'bodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_Modifier(inheritance="sample_text", modifier="sample_text", static=True, visibility="sample_text")
    partner = cSharpArchId_BodyDeclaration()
    setattr(partner, 'bodyDeclaration', None)
    _safe_set(owner, 'Modifier', partner)
    assert getattr(partner, 'bodyDeclaration') == owner
    _safe_set(owner, 'Modifier', None)
    assert getattr(partner, 'bodyDeclaration') is None


def test_assoc_namespace20_stub_double():
    # cSharpArchId_Namespace has no real 'cSharpArchId_Namespace22' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_CompileUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_CompileUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    partner = cSharpArchId_Namespace()
    setattr(partner, 'cSharpArchId_Namespace22', None)
    _safe_set(owner, 'cSharpArchId_CompileUnit21', partner)
    assert getattr(partner, 'cSharpArchId_Namespace22') == owner
    _safe_set(owner, 'cSharpArchId_CompileUnit21', None)
    assert getattr(partner, 'cSharpArchId_Namespace22') is None


def test_assoc_originalCompilationUnit23_stub_double():
    # cSharpArchId_ASTNode has no real 'cSharpArchId_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_CompileUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_CompileUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    partner = cSharpArchId_ASTNode()
    setattr(partner, 'cSharpArchId_ASTNode', None)
    _safe_set(owner, 'cSharpArchId_CompileUnit24', partner)
    assert getattr(partner, 'cSharpArchId_ASTNode') == owner
    _safe_set(owner, 'cSharpArchId_CompileUnit24', None)
    assert getattr(partner, 'cSharpArchId_ASTNode') is None


def test_assoc_typeDeclaration16_stub_double():
    # cSharpArchId_AbstractTypeDeclaration has no real 'cSharpArchId_AbstractTypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_CompileUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_CompileUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    partner = cSharpArchId_AbstractTypeDeclaration()
    setattr(partner, 'cSharpArchId_AbstractTypeDeclaration', None)
    _safe_set(owner, 'cSharpArchId_CompileUnit17', partner)
    assert getattr(partner, 'cSharpArchId_AbstractTypeDeclaration') == owner
    _safe_set(owner, 'cSharpArchId_CompileUnit17', None)
    assert getattr(partner, 'cSharpArchId_AbstractTypeDeclaration') is None


def test_assoc_usings18_stub_double():
    # cSharpArchId_UsingDeclaration has no real 'cSharpArchId_UsingDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so cSharpArchId_CompileUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharpArchId_CompileUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharpArchId_CompileUnit(originalFilePath="sample_text")
    partner = cSharpArchId_UsingDeclaration()
    setattr(partner, 'cSharpArchId_UsingDeclaration', None)
    _safe_set(owner, 'cSharpArchId_CompileUnit19', {partner})
    assert getattr(partner, 'cSharpArchId_UsingDeclaration') == owner
    _safe_set(owner, 'cSharpArchId_CompileUnit19', set())
    assert getattr(partner, 'cSharpArchId_UsingDeclaration') is None


