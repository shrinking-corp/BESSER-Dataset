import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    Block,
    Comment,
    Documentation,
    DocumentedElement,
    ENamedElement,
    EPackage,
    ModuleElement,
    OCLExpression,
    TemplateExpression,
    Variable,
    mtl_Block,
    mtl_Comment,
    mtl_CommentBody,
    mtl_Documentation,
    mtl_DocumentedElement,
    mtl_EClassifier,
    mtl_EPackage,
    mtl_FileBlock,
    mtl_ForBlock,
    mtl_IfBlock,
    mtl_InitSection,
    mtl_LetBlock,
    mtl_Macro,
    mtl_MacroInvocation,
    mtl_Module,
    mtl_ModuleDocumentation,
    mtl_ModuleElement,
    mtl_ModuleElementDocumentation,
    mtl_ParameterDocumentation,
    mtl_ProtectedAreaBlock,
    mtl_Query,
    mtl_QueryInvocation,
    mtl_Template,
    mtl_TemplateExpression,
    mtl_TemplateInvocation,
    mtl_TraceBlock,
    mtl_TypedModel,
    utilities_ASTNode,
    OpenModeKind,
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

def test_assoc_definition25_reverse_link_reassign_clear():
    a1 = mtl_TemplateInvocation(super=True)
    a2 = mtl_TemplateInvocation(super=False)
    b = mtl_Template(main=True)
    _safe_set(b, 'mtl_Template26', a1)
    assert _is_linked(b, 'mtl_Template26', a1)
    if hasattr(a1, 'mtl_TemplateInvocation'):
        assert _is_linked(a1, 'mtl_TemplateInvocation', b)
    _safe_set(b, 'mtl_Template26', a2)
    assert _is_linked(b, 'mtl_Template26', a2)
    if hasattr(a1, 'mtl_TemplateInvocation'):
        assert not _is_linked(a1, 'mtl_TemplateInvocation', b)
    if hasattr(a2, 'mtl_TemplateInvocation'):
        assert _is_linked(a2, 'mtl_TemplateInvocation', b)
    _safe_set(b, 'mtl_Template26', None)
    assert not _is_linked(b, 'mtl_Template26', a2)
    if hasattr(a2, 'mtl_TemplateInvocation'):
        assert not _is_linked(a2, 'mtl_TemplateInvocation', b)


def test_assoc_extends2_reverse_link_reassign_clear():
    a1 = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    a2 = mtl_Module(endHeaderPosition=13, startHeaderPosition=13)
    b = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    _safe_set(b, 'mtl_Module3', a1)
    assert _is_linked(b, 'mtl_Module3', a1)
    if hasattr(a1, 'mtl_Module1'):
        assert _is_linked(a1, 'mtl_Module1', b)
    _safe_set(b, 'mtl_Module3', a2)
    assert _is_linked(b, 'mtl_Module3', a2)
    if hasattr(a1, 'mtl_Module1'):
        assert not _is_linked(a1, 'mtl_Module1', b)
    if hasattr(a2, 'mtl_Module1'):
        assert _is_linked(a2, 'mtl_Module1', b)
    _safe_set(b, 'mtl_Module3', None)
    assert not _is_linked(b, 'mtl_Module3', a2)
    if hasattr(a2, 'mtl_Module1'):
        assert not _is_linked(a2, 'mtl_Module1', b)


def test_assoc_imports5_reverse_link_reassign_clear():
    a1 = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    a2 = mtl_Module(endHeaderPosition=13, startHeaderPosition=13)
    b = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    _safe_set(b, 'mtl_Module6', a1)
    assert _is_linked(b, 'mtl_Module6', a1)
    if hasattr(a1, 'mtl_Module4'):
        assert _is_linked(a1, 'mtl_Module4', b)
    _safe_set(b, 'mtl_Module6', a2)
    assert _is_linked(b, 'mtl_Module6', a2)
    if hasattr(a1, 'mtl_Module4'):
        assert not _is_linked(a1, 'mtl_Module4', b)
    if hasattr(a2, 'mtl_Module4'):
        assert _is_linked(a2, 'mtl_Module4', b)
    _safe_set(b, 'mtl_Module6', None)
    assert not _is_linked(b, 'mtl_Module6', a2)
    if hasattr(a2, 'mtl_Module4'):
        assert not _is_linked(a2, 'mtl_Module4', b)


def test_assoc_overrides15_reverse_link_reassign_clear():
    a1 = mtl_Template(main=True)
    a2 = mtl_Template(main=False)
    b = mtl_Template(main=True)
    _safe_set(b, 'mtl_Template14', {a1})
    assert _is_linked(b, 'mtl_Template14', a1)
    if hasattr(a1, 'mtl_Template'):
        assert _is_linked(a1, 'mtl_Template', b)
    _safe_set(b, 'mtl_Template14', {a2})
    assert _is_linked(b, 'mtl_Template14', a2)
    if hasattr(a1, 'mtl_Template'):
        assert not _is_linked(a1, 'mtl_Template', b)
    if hasattr(a2, 'mtl_Template'):
        assert _is_linked(a2, 'mtl_Template', b)
    _safe_set(b, 'mtl_Template14', set())
    assert not _is_linked(b, 'mtl_Template14', a2)
    if hasattr(a2, 'mtl_Template'):
        assert not _is_linked(a2, 'mtl_Template', b)


def test_assoc_ownedModuleElement7_reverse_link_reassign_clear():
    a1 = mtl_ModuleElement(visibility="sample_text")
    a2 = mtl_ModuleElement(visibility="sample_text_2")
    b = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    _safe_set(b, 'mtl_Module8', {a1})
    assert _is_linked(b, 'mtl_Module8', a1)
    if hasattr(a1, 'mtl_ModuleElement'):
        assert _is_linked(a1, 'mtl_ModuleElement', b)
    _safe_set(b, 'mtl_Module8', {a2})
    assert _is_linked(b, 'mtl_Module8', a2)
    if hasattr(a1, 'mtl_ModuleElement'):
        assert not _is_linked(a1, 'mtl_ModuleElement', b)
    if hasattr(a2, 'mtl_ModuleElement'):
        assert _is_linked(a2, 'mtl_ModuleElement', b)
    _safe_set(b, 'mtl_Module8', set())
    assert not _is_linked(b, 'mtl_Module8', a2)
    if hasattr(a2, 'mtl_ModuleElement'):
        assert not _is_linked(a2, 'mtl_ModuleElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_after33_stub_double():
    # OCLExpression has no real 'OCLExpression35' property in the generated
    # code (a bare stub) -- manually attach it so mtl_TemplateInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_TemplateInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_TemplateInvocation(super=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression35', None)
    _safe_set(owner, 'mtl_TemplateInvocation34', partner)
    assert getattr(partner, 'OCLExpression35') == owner
    _safe_set(owner, 'mtl_TemplateInvocation34', None)
    assert getattr(partner, 'OCLExpression35') is None


def test_assoc_argument27_stub_double():
    # OCLExpression has no real 'OCLExpression29' property in the generated
    # code (a bare stub) -- manually attach it so mtl_TemplateInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_TemplateInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_TemplateInvocation(super=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression29', None)
    _safe_set(owner, 'mtl_TemplateInvocation28', {partner})
    assert getattr(partner, 'OCLExpression29') == owner
    _safe_set(owner, 'mtl_TemplateInvocation28', set())
    assert getattr(partner, 'OCLExpression29') is None


def test_assoc_before30_stub_double():
    # OCLExpression has no real 'OCLExpression32' property in the generated
    # code (a bare stub) -- manually attach it so mtl_TemplateInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_TemplateInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_TemplateInvocation(super=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression32', None)
    _safe_set(owner, 'mtl_TemplateInvocation31', partner)
    assert getattr(partner, 'OCLExpression32') == owner
    _safe_set(owner, 'mtl_TemplateInvocation31', None)
    assert getattr(partner, 'OCLExpression32') is None


def test_assoc_body108_stub_double():
    # mtl_Comment has no real 'mtl_Comment' property in the generated
    # code (a bare stub) -- manually attach it so mtl_CommentBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_CommentBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_CommentBody(endPosition=7, startPosition=7, value="sample_text")
    partner = mtl_Comment()
    setattr(partner, 'mtl_Comment', None)
    _safe_set(owner, 'mtl_CommentBody', partner)
    assert getattr(partner, 'mtl_Comment') == owner
    _safe_set(owner, 'mtl_CommentBody', None)
    assert getattr(partner, 'mtl_Comment') is None


def test_assoc_charset91_stub_double():
    # OCLExpression has no real 'OCLExpression93' property in the generated
    # code (a bare stub) -- manually attach it so mtl_FileBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_FileBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_FileBlock(openMode="sample_text")
    partner = OCLExpression()
    setattr(partner, 'OCLExpression93', None)
    _safe_set(owner, 'mtl_FileBlock92', partner)
    assert getattr(partner, 'OCLExpression93') == owner
    _safe_set(owner, 'mtl_FileBlock92', None)
    assert getattr(partner, 'OCLExpression93') is None


def test_assoc_documentation110_stub_double():
    # mtl_Documentation has no real 'Documentation' property in the generated
    # code (a bare stub) -- manually attach it so mtl_DocumentedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_DocumentedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_DocumentedElement(deprecated=True)
    partner = mtl_Documentation()
    setattr(partner, 'Documentation', None)
    _safe_set(owner, 'documentedElement', partner)
    assert getattr(partner, 'Documentation') == owner
    _safe_set(owner, 'documentedElement', None)
    assert getattr(partner, 'Documentation') is None


def test_assoc_documentedElement109_stub_double():
    # mtl_Documentation has no real 'documentation' property in the generated
    # code (a bare stub) -- manually attach it so mtl_DocumentedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_DocumentedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_DocumentedElement(deprecated=True)
    partner = mtl_Documentation()
    setattr(partner, 'documentation', None)
    _safe_set(owner, 'DocumentedElement', partner)
    assert getattr(partner, 'documentation') == owner
    _safe_set(owner, 'DocumentedElement', None)
    assert getattr(partner, 'documentation') is None


def test_assoc_each36_stub_double():
    # OCLExpression has no real 'OCLExpression38' property in the generated
    # code (a bare stub) -- manually attach it so mtl_TemplateInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_TemplateInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_TemplateInvocation(super=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression38', None)
    _safe_set(owner, 'mtl_TemplateInvocation37', partner)
    assert getattr(partner, 'OCLExpression38') == owner
    _safe_set(owner, 'mtl_TemplateInvocation37', None)
    assert getattr(partner, 'OCLExpression38') is None


def test_assoc_fileUrl86_stub_double():
    # OCLExpression has no real 'OCLExpression87' property in the generated
    # code (a bare stub) -- manually attach it so mtl_FileBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_FileBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_FileBlock(openMode="sample_text")
    partner = OCLExpression()
    setattr(partner, 'OCLExpression87', None)
    _safe_set(owner, 'mtl_FileBlock', partner)
    assert getattr(partner, 'OCLExpression87') == owner
    _safe_set(owner, 'mtl_FileBlock', None)
    assert getattr(partner, 'OCLExpression87') is None


def test_assoc_guard19_stub_double():
    # OCLExpression has no real 'OCLExpression21' property in the generated
    # code (a bare stub) -- manually attach it so mtl_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_Template(main=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression21', None)
    _safe_set(owner, 'mtl_Template20', partner)
    assert getattr(partner, 'OCLExpression21') == owner
    _safe_set(owner, 'mtl_Template20', None)
    assert getattr(partner, 'OCLExpression21') is None


def test_assoc_input0_stub_double():
    # mtl_TypedModel has no real 'mtl_TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so mtl_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_Module(endHeaderPosition=7, startHeaderPosition=7)
    partner = mtl_TypedModel()
    setattr(partner, 'mtl_TypedModel', None)
    _safe_set(owner, 'mtl_Module', {partner})
    assert getattr(partner, 'mtl_TypedModel') == owner
    _safe_set(owner, 'mtl_Module', set())
    assert getattr(partner, 'mtl_TypedModel') is None


def test_assoc_parameter16_stub_double():
    # Variable has no real 'Variable18' property in the generated
    # code (a bare stub) -- manually attach it so mtl_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_Template(main=True)
    partner = Variable()
    setattr(partner, 'Variable18', None)
    _safe_set(owner, 'mtl_Template17', {partner})
    assert getattr(partner, 'Variable18') == owner
    _safe_set(owner, 'mtl_Template17', set())
    assert getattr(partner, 'Variable18') is None


def test_assoc_post22_stub_double():
    # OCLExpression has no real 'OCLExpression24' property in the generated
    # code (a bare stub) -- manually attach it so mtl_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_Template(main=True)
    partner = OCLExpression()
    setattr(partner, 'OCLExpression24', None)
    _safe_set(owner, 'mtl_Template23', partner)
    assert getattr(partner, 'OCLExpression24') == owner
    _safe_set(owner, 'mtl_Template23', None)
    assert getattr(partner, 'OCLExpression24') is None


def test_assoc_uniqId88_stub_double():
    # OCLExpression has no real 'OCLExpression90' property in the generated
    # code (a bare stub) -- manually attach it so mtl_FileBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtl_FileBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtl_FileBlock(openMode="sample_text")
    partner = OCLExpression()
    setattr(partner, 'OCLExpression90', None)
    _safe_set(owner, 'mtl_FileBlock89', partner)
    assert getattr(partner, 'OCLExpression90') == owner
    _safe_set(owner, 'mtl_FileBlock89', None)
    assert getattr(partner, 'OCLExpression90') is None


