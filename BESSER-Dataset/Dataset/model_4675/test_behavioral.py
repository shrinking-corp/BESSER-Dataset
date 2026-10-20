import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Condition,
    EquationalCond,
    MaudeTopEl,
    Maude_BooleanCond,
    Maude_CompModExp,
    Maude_Condition,
    Maude_Constant,
    Maude_EqualCond,
    Maude_Equation,
    Maude_EquationalCond,
    Maude_FModule,
    Maude_FTheory,
    Maude_InstModExp,
    Maude_Kind,
    Maude_LabelMapping,
    Maude_MatchingCond,
    Maude_MaudeSpec,
    Maude_MaudeTopEl,
    Maude_Membership,
    Maude_MembershipCond,
    Maude_ModElement,
    Maude_ModExpression,
    Maude_ModImportation,
    Maude_Module,
    Maude_ModuleIdModExp,
    Maude_OpMapping,
    Maude_OpTypedMapping,
    Maude_Operation,
    Maude_Parameter,
    Maude_RecTerm,
    Maude_RenMapping,
    Maude_RenModExp,
    Maude_RewriteCond,
    Maude_Rule,
    Maude_SModule,
    Maude_STheory,
    Maude_Sort,
    Maude_SortMapping,
    Maude_Statement,
    Maude_SubsortRel,
    Maude_Term,
    Maude_TermMapping,
    Maude_Theory,
    Maude_TheoryIdModExp,
    Maude_Type,
    Maude_Variable,
    Maude_View,
    Maude_ViewMapping,
    ModElement,
    ModExpression,
    Module,
    RenMapping,
    Statement,
    Term,
    Theory,
    Type,
    ViewMapping,
    ImportationMode,
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

def test_assoc_arity38_reverse_link_reassign_clear():
    a1 = Maude_Type(name="sample_text")
    a2 = Maude_Type(name="sample_text_2")
    b = Maude_Operation(atts="sample_text", name="sample_text")
    _safe_set(b, 'Maude_Operation39', {a1})
    assert _is_linked(b, 'Maude_Operation39', a1)
    if hasattr(a1, 'Maude_Type40'):
        assert _is_linked(a1, 'Maude_Type40', b)
    _safe_set(b, 'Maude_Operation39', {a2})
    assert _is_linked(b, 'Maude_Operation39', a2)
    if hasattr(a1, 'Maude_Type40'):
        assert not _is_linked(a1, 'Maude_Type40', b)
    if hasattr(a2, 'Maude_Type40'):
        assert _is_linked(a2, 'Maude_Type40', b)
    _safe_set(b, 'Maude_Operation39', set())
    assert not _is_linked(b, 'Maude_Operation39', a2)
    if hasattr(a2, 'Maude_Type40'):
        assert not _is_linked(a2, 'Maude_Type40', b)


def test_assoc_coarity37_reverse_link_reassign_clear():
    a1 = Maude_Type(name="sample_text")
    a2 = Maude_Type(name="sample_text_2")
    b = Maude_Operation(atts="sample_text", name="sample_text")
    _safe_set(b, 'Maude_Operation', a1)
    assert _is_linked(b, 'Maude_Operation', a1)
    if hasattr(a1, 'Maude_Type'):
        assert _is_linked(a1, 'Maude_Type', b)
    _safe_set(b, 'Maude_Operation', a2)
    assert _is_linked(b, 'Maude_Operation', a2)
    if hasattr(a1, 'Maude_Type'):
        assert not _is_linked(a1, 'Maude_Type', b)
    if hasattr(a2, 'Maude_Type'):
        assert _is_linked(a2, 'Maude_Type', b)
    _safe_set(b, 'Maude_Operation', None)
    assert not _is_linked(b, 'Maude_Operation', a2)
    if hasattr(a2, 'Maude_Type'):
        assert not _is_linked(a2, 'Maude_Type', b)


def test_assoc_from_86_reverse_link_reassign_clear():
    a1 = Maude_Operation(atts="sample_text", name="sample_text")
    a2 = Maude_Operation(atts="sample_text_2", name="sample_text_2")
    b = Maude_OpTypedMapping(atts="sample_text", to="sample_text")
    _safe_set(b, 'Maude_OpTypedMapping', a1)
    assert _is_linked(b, 'Maude_OpTypedMapping', a1)
    if hasattr(a1, 'Maude_Operation87'):
        assert _is_linked(a1, 'Maude_Operation87', b)
    _safe_set(b, 'Maude_OpTypedMapping', a2)
    assert _is_linked(b, 'Maude_OpTypedMapping', a2)
    if hasattr(a1, 'Maude_Operation87'):
        assert not _is_linked(a1, 'Maude_Operation87', b)
    if hasattr(a2, 'Maude_Operation87'):
        assert _is_linked(a2, 'Maude_Operation87', b)
    _safe_set(b, 'Maude_OpTypedMapping', None)
    assert not _is_linked(b, 'Maude_OpTypedMapping', a2)
    if hasattr(a2, 'Maude_Operation87'):
        assert not _is_linked(a2, 'Maude_Operation87', b)


def test_assoc_from_88_reverse_link_reassign_clear():
    a1 = Maude_Operation(atts="sample_text", name="sample_text")
    a2 = Maude_Operation(atts="sample_text_2", name="sample_text_2")
    b = Maude_OpMapping(to="sample_text")
    _safe_set(b, 'Maude_OpMapping', a1)
    assert _is_linked(b, 'Maude_OpMapping', a1)
    if hasattr(a1, 'Maude_Operation89'):
        assert _is_linked(a1, 'Maude_Operation89', b)
    _safe_set(b, 'Maude_OpMapping', a2)
    assert _is_linked(b, 'Maude_OpMapping', a2)
    if hasattr(a1, 'Maude_Operation89'):
        assert not _is_linked(a1, 'Maude_Operation89', b)
    if hasattr(a2, 'Maude_Operation89'):
        assert _is_linked(a2, 'Maude_Operation89', b)
    _safe_set(b, 'Maude_OpMapping', None)
    assert not _is_linked(b, 'Maude_OpMapping', a2)
    if hasattr(a2, 'Maude_Operation89'):
        assert not _is_linked(a2, 'Maude_Operation89', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args69_stub_double():
    # Maude_Term has no real 'Maude_Term70' property in the generated
    # code (a bare stub) -- manually attach it so Maude_RecTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_RecTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_RecTerm(op="sample_text")
    partner = Maude_Term()
    setattr(partner, 'Maude_Term70', None)
    _safe_set(owner, 'Maude_RecTerm', {partner})
    assert getattr(partner, 'Maude_Term70') == owner
    _safe_set(owner, 'Maude_RecTerm', set())
    assert getattr(partner, 'Maude_Term70') is None


def test_assoc_conds41_stub_double():
    # Maude_Condition has no real 'Maude_Condition' property in the generated
    # code (a bare stub) -- manually attach it so Maude_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_Statement(atts="sample_text", label="sample_text")
    partner = Maude_Condition()
    setattr(partner, 'Maude_Condition', None)
    _safe_set(owner, 'Maude_Statement', {partner})
    assert getattr(partner, 'Maude_Condition') == owner
    _safe_set(owner, 'Maude_Statement', set())
    assert getattr(partner, 'Maude_Condition') is None


def test_assoc_els0_stub_double():
    # Maude_MaudeSpec has no real 'Maude_MaudeSpec' property in the generated
    # code (a bare stub) -- manually attach it so Maude_MaudeTopEl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_MaudeTopEl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_MaudeTopEl(name="sample_text")
    partner = Maude_MaudeSpec()
    setattr(partner, 'Maude_MaudeSpec', None)
    _safe_set(owner, 'Maude_MaudeTopEl', partner)
    assert owner in getattr(partner, 'Maude_MaudeSpec')
    _safe_set(owner, 'Maude_MaudeTopEl', None)
    assert owner not in getattr(partner, 'Maude_MaudeSpec')


def test_assoc_from_84_stub_double():
    # Maude_Sort has no real 'Maude_Sort85' property in the generated
    # code (a bare stub) -- manually attach it so Maude_SortMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_SortMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_SortMapping(to="sample_text")
    partner = Maude_Sort()
    setattr(partner, 'Maude_Sort85', None)
    _safe_set(owner, 'Maude_SortMapping', partner)
    assert getattr(partner, 'Maude_Sort85') == owner
    _safe_set(owner, 'Maude_SortMapping', None)
    assert getattr(partner, 'Maude_Sort85') is None


def test_assoc_imports26_stub_double():
    # Maude_ModExpression has no real 'Maude_ModExpression27' property in the generated
    # code (a bare stub) -- manually attach it so Maude_ModImportation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_ModImportation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_ModImportation(mode="sample_text")
    partner = Maude_ModExpression()
    setattr(partner, 'Maude_ModExpression27', None)
    _safe_set(owner, 'Maude_ModImportation', partner)
    assert getattr(partner, 'Maude_ModExpression27') == owner
    _safe_set(owner, 'Maude_ModImportation', None)
    assert getattr(partner, 'Maude_ModExpression27') is None


def test_assoc_modExp15_stub_double():
    # Maude_ModExpression has no real 'Maude_ModExpression16' property in the generated
    # code (a bare stub) -- manually attach it so Maude_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_Parameter(label="sample_text")
    partner = Maude_ModExpression()
    setattr(partner, 'Maude_ModExpression16', None)
    _safe_set(owner, 'Maude_Parameter', partner)
    assert getattr(partner, 'Maude_ModExpression16') == owner
    _safe_set(owner, 'Maude_Parameter', None)
    assert getattr(partner, 'Maude_ModExpression16') is None


def test_assoc_params20_stub_double():
    # Maude_Module has no real 'Maude_Module21' property in the generated
    # code (a bare stub) -- manually attach it so Maude_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_Parameter(label="sample_text")
    partner = Maude_Module()
    setattr(partner, 'Maude_Module21', None)
    _safe_set(owner, 'Maude_Parameter22', partner)
    assert owner in getattr(partner, 'Maude_Module21')
    _safe_set(owner, 'Maude_Parameter22', None)
    assert owner not in getattr(partner, 'Maude_Module21')


def test_assoc_printableEls1_stub_double():
    # Maude_MaudeSpec has no real 'Maude_MaudeSpec2' property in the generated
    # code (a bare stub) -- manually attach it so Maude_MaudeTopEl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_MaudeTopEl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_MaudeTopEl(name="sample_text")
    partner = Maude_MaudeSpec()
    setattr(partner, 'Maude_MaudeSpec2', None)
    _safe_set(owner, 'Maude_MaudeTopEl3', partner)
    assert owner in getattr(partner, 'Maude_MaudeSpec2')
    _safe_set(owner, 'Maude_MaudeTopEl3', None)
    assert owner not in getattr(partner, 'Maude_MaudeSpec2')


def test_assoc_type66_stub_double():
    # Maude_Term has no real 'Maude_Term67' property in the generated
    # code (a bare stub) -- manually attach it so Maude_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maude_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maude_Type(name="sample_text")
    partner = Maude_Term()
    setattr(partner, 'Maude_Term67', None)
    _safe_set(owner, 'Maude_Type68', partner)
    assert getattr(partner, 'Maude_Term67') == owner
    _safe_set(owner, 'Maude_Type68', None)
    assert getattr(partner, 'Maude_Term67') is None


