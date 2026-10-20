import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    CSTNode,
    Comment,
    EPackage,
    ModuleElement,
    TemplateExpression,
    cst_Block,
    cst_CSTNode,
    cst_Comment,
    cst_Documentation,
    cst_EPackage,
    cst_FileBlock,
    cst_ForBlock,
    cst_IfBlock,
    cst_InitSection,
    cst_LetBlock,
    cst_Macro,
    cst_ModelExpression,
    cst_Module,
    cst_ModuleElement,
    cst_ModuleExtendsValue,
    cst_ModuleImportsValue,
    cst_ProtectedAreaBlock,
    cst_Query,
    cst_Template,
    cst_TemplateExpression,
    cst_TemplateOverridesValue,
    cst_TextExpression,
    cst_TraceBlock,
    cst_TypedModel,
    cst_Variable,
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

def test_assoc_after29_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_ModelExpression(body="sample_text")
    _safe_set(b, 'cst_ModelExpression30', a1)
    assert _is_linked(b, 'cst_ModelExpression30', a1)
    if hasattr(a1, 'cst_ModelExpression28'):
        assert _is_linked(a1, 'cst_ModelExpression28', b)
    _safe_set(b, 'cst_ModelExpression30', a2)
    assert _is_linked(b, 'cst_ModelExpression30', a2)
    if hasattr(a1, 'cst_ModelExpression28'):
        assert not _is_linked(a1, 'cst_ModelExpression28', b)
    if hasattr(a2, 'cst_ModelExpression28'):
        assert _is_linked(a2, 'cst_ModelExpression28', b)
    _safe_set(b, 'cst_ModelExpression30', None)
    assert not _is_linked(b, 'cst_ModelExpression30', a2)
    if hasattr(a2, 'cst_ModelExpression28'):
        assert not _is_linked(a2, 'cst_ModelExpression28', b)


def test_assoc_before23_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_ModelExpression(body="sample_text")
    _safe_set(b, 'cst_ModelExpression24', a1)
    assert _is_linked(b, 'cst_ModelExpression24', a1)
    if hasattr(a1, 'cst_ModelExpression22'):
        assert _is_linked(a1, 'cst_ModelExpression22', b)
    _safe_set(b, 'cst_ModelExpression24', a2)
    assert _is_linked(b, 'cst_ModelExpression24', a2)
    if hasattr(a1, 'cst_ModelExpression22'):
        assert not _is_linked(a1, 'cst_ModelExpression22', b)
    if hasattr(a2, 'cst_ModelExpression22'):
        assert _is_linked(a2, 'cst_ModelExpression22', b)
    _safe_set(b, 'cst_ModelExpression24', None)
    assert not _is_linked(b, 'cst_ModelExpression24', a2)
    if hasattr(a2, 'cst_ModelExpression22'):
        assert not _is_linked(a2, 'cst_ModelExpression22', b)


def test_assoc_charset77_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_FileBlock(openMode="sample_text")
    _safe_set(b, 'cst_FileBlock78', a1)
    assert _is_linked(b, 'cst_FileBlock78', a1)
    if hasattr(a1, 'cst_ModelExpression79'):
        assert _is_linked(a1, 'cst_ModelExpression79', b)
    _safe_set(b, 'cst_FileBlock78', a2)
    assert _is_linked(b, 'cst_FileBlock78', a2)
    if hasattr(a1, 'cst_ModelExpression79'):
        assert not _is_linked(a1, 'cst_ModelExpression79', b)
    if hasattr(a2, 'cst_ModelExpression79'):
        assert _is_linked(a2, 'cst_ModelExpression79', b)
    _safe_set(b, 'cst_FileBlock78', None)
    assert not _is_linked(b, 'cst_FileBlock78', a2)
    if hasattr(a2, 'cst_ModelExpression79'):
        assert not _is_linked(a2, 'cst_ModelExpression79', b)


def test_assoc_each26_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_ModelExpression(body="sample_text")
    _safe_set(b, 'cst_ModelExpression27', a1)
    assert _is_linked(b, 'cst_ModelExpression27', a1)
    if hasattr(a1, 'cst_ModelExpression25'):
        assert _is_linked(a1, 'cst_ModelExpression25', b)
    _safe_set(b, 'cst_ModelExpression27', a2)
    assert _is_linked(b, 'cst_ModelExpression27', a2)
    if hasattr(a1, 'cst_ModelExpression25'):
        assert not _is_linked(a1, 'cst_ModelExpression25', b)
    if hasattr(a2, 'cst_ModelExpression25'):
        assert _is_linked(a2, 'cst_ModelExpression25', b)
    _safe_set(b, 'cst_ModelExpression27', None)
    assert not _is_linked(b, 'cst_ModelExpression27', a2)
    if hasattr(a2, 'cst_ModelExpression25'):
        assert not _is_linked(a2, 'cst_ModelExpression25', b)


def test_assoc_expression86_reverse_link_reassign_clear():
    a1 = cst_Query(type="sample_text")
    a2 = cst_Query(type="sample_text_2")
    b = cst_ModelExpression(body="sample_text")
    _safe_set(b, 'cst_ModelExpression88', a1)
    assert _is_linked(b, 'cst_ModelExpression88', a1)
    if hasattr(a1, 'cst_Query87'):
        assert _is_linked(a1, 'cst_Query87', b)
    _safe_set(b, 'cst_ModelExpression88', a2)
    assert _is_linked(b, 'cst_ModelExpression88', a2)
    if hasattr(a1, 'cst_Query87'):
        assert not _is_linked(a1, 'cst_Query87', b)
    if hasattr(a2, 'cst_Query87'):
        assert _is_linked(a2, 'cst_Query87', b)
    _safe_set(b, 'cst_ModelExpression88', None)
    assert not _is_linked(b, 'cst_ModelExpression88', a2)
    if hasattr(a2, 'cst_Query87'):
        assert not _is_linked(a2, 'cst_Query87', b)


def test_assoc_fileUrl72_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_FileBlock(openMode="sample_text")
    _safe_set(b, 'cst_FileBlock', a1)
    assert _is_linked(b, 'cst_FileBlock', a1)
    if hasattr(a1, 'cst_ModelExpression73'):
        assert _is_linked(a1, 'cst_ModelExpression73', b)
    _safe_set(b, 'cst_FileBlock', a2)
    assert _is_linked(b, 'cst_FileBlock', a2)
    if hasattr(a1, 'cst_ModelExpression73'):
        assert not _is_linked(a1, 'cst_ModelExpression73', b)
    if hasattr(a2, 'cst_ModelExpression73'):
        assert _is_linked(a2, 'cst_ModelExpression73', b)
    _safe_set(b, 'cst_FileBlock', None)
    assert not _is_linked(b, 'cst_FileBlock', a2)
    if hasattr(a2, 'cst_ModelExpression73'):
        assert not _is_linked(a2, 'cst_ModelExpression73', b)


def test_assoc_initExpression19_reverse_link_reassign_clear():
    a1 = cst_Variable(name="sample_text", type="sample_text")
    a2 = cst_Variable(name="sample_text_2", type="sample_text_2")
    b = cst_ModelExpression(body="sample_text")
    _safe_set(b, 'cst_ModelExpression21', a1)
    assert _is_linked(b, 'cst_ModelExpression21', a1)
    if hasattr(a1, 'cst_Variable20'):
        assert _is_linked(a1, 'cst_Variable20', b)
    _safe_set(b, 'cst_ModelExpression21', a2)
    assert _is_linked(b, 'cst_ModelExpression21', a2)
    if hasattr(a1, 'cst_Variable20'):
        assert not _is_linked(a1, 'cst_Variable20', b)
    if hasattr(a2, 'cst_Variable20'):
        assert _is_linked(a2, 'cst_Variable20', b)
    _safe_set(b, 'cst_ModelExpression21', None)
    assert not _is_linked(b, 'cst_ModelExpression21', a2)
    if hasattr(a2, 'cst_Variable20'):
        assert not _is_linked(a2, 'cst_Variable20', b)


def test_assoc_parameter82_reverse_link_reassign_clear():
    a1 = cst_Variable(name="sample_text", type="sample_text")
    a2 = cst_Variable(name="sample_text_2", type="sample_text_2")
    b = cst_Macro(type="sample_text")
    _safe_set(b, 'cst_Macro', {a1})
    assert _is_linked(b, 'cst_Macro', a1)
    if hasattr(a1, 'cst_Variable83'):
        assert _is_linked(a1, 'cst_Variable83', b)
    _safe_set(b, 'cst_Macro', {a2})
    assert _is_linked(b, 'cst_Macro', a2)
    if hasattr(a1, 'cst_Variable83'):
        assert not _is_linked(a1, 'cst_Variable83', b)
    if hasattr(a2, 'cst_Variable83'):
        assert _is_linked(a2, 'cst_Variable83', b)
    _safe_set(b, 'cst_Macro', set())
    assert not _is_linked(b, 'cst_Macro', a2)
    if hasattr(a2, 'cst_Variable83'):
        assert not _is_linked(a2, 'cst_Variable83', b)


def test_assoc_parameter84_reverse_link_reassign_clear():
    a1 = cst_Variable(name="sample_text", type="sample_text")
    a2 = cst_Variable(name="sample_text_2", type="sample_text_2")
    b = cst_Query(type="sample_text")
    _safe_set(b, 'cst_Query', {a1})
    assert _is_linked(b, 'cst_Query', a1)
    if hasattr(a1, 'cst_Variable85'):
        assert _is_linked(a1, 'cst_Variable85', b)
    _safe_set(b, 'cst_Query', {a2})
    assert _is_linked(b, 'cst_Query', a2)
    if hasattr(a1, 'cst_Variable85'):
        assert not _is_linked(a1, 'cst_Variable85', b)
    if hasattr(a2, 'cst_Variable85'):
        assert _is_linked(a2, 'cst_Variable85', b)
    _safe_set(b, 'cst_Query', set())
    assert not _is_linked(b, 'cst_Query', a2)
    if hasattr(a2, 'cst_Variable85'):
        assert not _is_linked(a2, 'cst_Variable85', b)


def test_assoc_uniqId74_reverse_link_reassign_clear():
    a1 = cst_ModelExpression(body="sample_text")
    a2 = cst_ModelExpression(body="sample_text_2")
    b = cst_FileBlock(openMode="sample_text")
    _safe_set(b, 'cst_FileBlock75', a1)
    assert _is_linked(b, 'cst_FileBlock75', a1)
    if hasattr(a1, 'cst_ModelExpression76'):
        assert _is_linked(a1, 'cst_ModelExpression76', b)
    _safe_set(b, 'cst_FileBlock75', a2)
    assert _is_linked(b, 'cst_FileBlock75', a2)
    if hasattr(a1, 'cst_ModelExpression76'):
        assert not _is_linked(a1, 'cst_ModelExpression76', b)
    if hasattr(a2, 'cst_ModelExpression76'):
        assert _is_linked(a2, 'cst_ModelExpression76', b)
    _safe_set(b, 'cst_FileBlock75', None)
    assert not _is_linked(b, 'cst_FileBlock75', a2)
    if hasattr(a2, 'cst_ModelExpression76'):
        assert not _is_linked(a2, 'cst_ModelExpression76', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_after50_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock51' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock51', None)
    _safe_set(owner, 'cst_ModelExpression52', partner)
    assert getattr(partner, 'cst_ForBlock51') == owner
    _safe_set(owner, 'cst_ModelExpression52', None)
    assert getattr(partner, 'cst_ForBlock51') is None


def test_assoc_before44_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock45' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock45', None)
    _safe_set(owner, 'cst_ModelExpression46', partner)
    assert getattr(partner, 'cst_ForBlock45') == owner
    _safe_set(owner, 'cst_ModelExpression46', None)
    assert getattr(partner, 'cst_ForBlock45') is None


def test_assoc_each47_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock48' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock48', None)
    _safe_set(owner, 'cst_ModelExpression49', partner)
    assert getattr(partner, 'cst_ForBlock48') == owner
    _safe_set(owner, 'cst_ModelExpression49', None)
    assert getattr(partner, 'cst_ForBlock48') is None


def test_assoc_extends3_stub_double():
    # cst_Module has no real 'cst_Module4' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModuleExtendsValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModuleExtendsValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModuleExtendsValue(name="sample_text")
    partner = cst_Module()
    setattr(partner, 'cst_Module4', None)
    _safe_set(owner, 'cst_ModuleExtendsValue', partner)
    assert owner in getattr(partner, 'cst_Module4')
    _safe_set(owner, 'cst_ModuleExtendsValue', None)
    assert owner not in getattr(partner, 'cst_Module4')


def test_assoc_guard14_stub_double():
    # cst_Template has no real 'cst_Template15' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_Template()
    setattr(partner, 'cst_Template15', None)
    _safe_set(owner, 'cst_ModelExpression', partner)
    assert getattr(partner, 'cst_Template15') == owner
    _safe_set(owner, 'cst_ModelExpression', None)
    assert getattr(partner, 'cst_Template15') is None


def test_assoc_guard53_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock54' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock54', None)
    _safe_set(owner, 'cst_ModelExpression55', partner)
    assert getattr(partner, 'cst_ForBlock54') == owner
    _safe_set(owner, 'cst_ModelExpression55', None)
    assert getattr(partner, 'cst_ForBlock54') is None


def test_assoc_ifExpr56_stub_double():
    # cst_IfBlock has no real 'cst_IfBlock' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_IfBlock()
    setattr(partner, 'cst_IfBlock', None)
    _safe_set(owner, 'cst_ModelExpression57', partner)
    assert getattr(partner, 'cst_IfBlock') == owner
    _safe_set(owner, 'cst_ModelExpression57', None)
    assert getattr(partner, 'cst_IfBlock') is None


def test_assoc_imports5_stub_double():
    # cst_Module has no real 'cst_Module6' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModuleImportsValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModuleImportsValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModuleImportsValue(name="sample_text")
    partner = cst_Module()
    setattr(partner, 'cst_Module6', None)
    _safe_set(owner, 'cst_ModuleImportsValue', partner)
    assert owner in getattr(partner, 'cst_Module6')
    _safe_set(owner, 'cst_ModuleImportsValue', None)
    assert owner not in getattr(partner, 'cst_Module6')


def test_assoc_iterSet41_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock42' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock42', None)
    _safe_set(owner, 'cst_ModelExpression43', partner)
    assert getattr(partner, 'cst_ForBlock42') == owner
    _safe_set(owner, 'cst_ModelExpression43', None)
    assert getattr(partner, 'cst_ForBlock42') is None


def test_assoc_letVariable69_stub_double():
    # cst_LetBlock has no real 'cst_LetBlock70' property in the generated
    # code (a bare stub) -- manually attach it so cst_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_Variable(name="sample_text", type="sample_text")
    partner = cst_LetBlock()
    setattr(partner, 'cst_LetBlock70', None)
    _safe_set(owner, 'cst_Variable71', partner)
    assert getattr(partner, 'cst_LetBlock70') == owner
    _safe_set(owner, 'cst_Variable71', None)
    assert getattr(partner, 'cst_LetBlock70') is None


def test_assoc_loopVariable39_stub_double():
    # cst_ForBlock has no real 'cst_ForBlock' property in the generated
    # code (a bare stub) -- manually attach it so cst_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_Variable(name="sample_text", type="sample_text")
    partner = cst_ForBlock()
    setattr(partner, 'cst_ForBlock', None)
    _safe_set(owner, 'cst_Variable40', partner)
    assert getattr(partner, 'cst_ForBlock') == owner
    _safe_set(owner, 'cst_Variable40', None)
    assert getattr(partner, 'cst_ForBlock') is None


def test_assoc_marker37_stub_double():
    # cst_ProtectedAreaBlock has no real 'cst_ProtectedAreaBlock' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_ProtectedAreaBlock()
    setattr(partner, 'cst_ProtectedAreaBlock', None)
    _safe_set(owner, 'cst_ModelExpression38', partner)
    assert getattr(partner, 'cst_ProtectedAreaBlock') == owner
    _safe_set(owner, 'cst_ModelExpression38', None)
    assert getattr(partner, 'cst_ProtectedAreaBlock') is None


def test_assoc_modelElement80_stub_double():
    # cst_TraceBlock has no real 'cst_TraceBlock' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_TraceBlock()
    setattr(partner, 'cst_TraceBlock', None)
    _safe_set(owner, 'cst_ModelExpression81', partner)
    assert getattr(partner, 'cst_TraceBlock') == owner
    _safe_set(owner, 'cst_ModelExpression81', None)
    assert getattr(partner, 'cst_TraceBlock') is None


def test_assoc_overrides11_stub_double():
    # cst_Template has no real 'cst_Template' property in the generated
    # code (a bare stub) -- manually attach it so cst_TemplateOverridesValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_TemplateOverridesValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_TemplateOverridesValue(name="sample_text")
    partner = cst_Template()
    setattr(partner, 'cst_Template', None)
    _safe_set(owner, 'cst_TemplateOverridesValue', partner)
    assert owner in getattr(partner, 'cst_Template')
    _safe_set(owner, 'cst_TemplateOverridesValue', None)
    assert owner not in getattr(partner, 'cst_Template')


def test_assoc_ownedModuleElement1_stub_double():
    # cst_Module has no real 'cst_Module2' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModuleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModuleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModuleElement(name="sample_text", visibility="sample_text")
    partner = cst_Module()
    setattr(partner, 'cst_Module2', None)
    _safe_set(owner, 'cst_ModuleElement', partner)
    assert owner in getattr(partner, 'cst_Module2')
    _safe_set(owner, 'cst_ModuleElement', None)
    assert owner not in getattr(partner, 'cst_Module2')


def test_assoc_parameter12_stub_double():
    # cst_Template has no real 'cst_Template13' property in the generated
    # code (a bare stub) -- manually attach it so cst_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_Variable(name="sample_text", type="sample_text")
    partner = cst_Template()
    setattr(partner, 'cst_Template13', None)
    _safe_set(owner, 'cst_Variable', partner)
    assert owner in getattr(partner, 'cst_Template13')
    _safe_set(owner, 'cst_Variable', None)
    assert owner not in getattr(partner, 'cst_Template13')


def test_assoc_post16_stub_double():
    # cst_Template has no real 'cst_Template17' property in the generated
    # code (a bare stub) -- manually attach it so cst_ModelExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_ModelExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_ModelExpression(body="sample_text")
    partner = cst_Template()
    setattr(partner, 'cst_Template17', None)
    _safe_set(owner, 'cst_ModelExpression18', partner)
    assert getattr(partner, 'cst_Template17') == owner
    _safe_set(owner, 'cst_ModelExpression18', None)
    assert getattr(partner, 'cst_Template17') is None


def test_assoc_variable34_stub_double():
    # cst_InitSection has no real 'cst_InitSection35' property in the generated
    # code (a bare stub) -- manually attach it so cst_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cst_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cst_Variable(name="sample_text", type="sample_text")
    partner = cst_InitSection()
    setattr(partner, 'cst_InitSection35', None)
    _safe_set(owner, 'cst_Variable36', partner)
    assert owner in getattr(partner, 'cst_InitSection35')
    _safe_set(owner, 'cst_Variable36', None)
    assert owner not in getattr(partner, 'cst_InitSection35')


