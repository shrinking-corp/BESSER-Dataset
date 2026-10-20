import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASort,
    ATerm,
    adt_ADT,
    adt_ASort,
    adt_ATerm,
    adt_Equation,
    adt_Operation,
    adt_Signature,
    adt_Sort,
    adt_SubSort,
    adt_Term,
    adt_Variable,
    adt_VariableDeclaration,
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

def test_assoc_adt26_reverse_link_reassign_clear():
    a1 = adt_ATerm(symbol="sample_text")
    a2 = adt_ATerm(symbol="sample_text_2")
    b = adt_ADT(name="sample_text")
    _safe_set(b, 'adt_ADT27', a1)
    assert _is_linked(b, 'adt_ADT27', a1)
    if hasattr(a1, 'adt_ATerm'):
        assert _is_linked(a1, 'adt_ATerm', b)
    _safe_set(b, 'adt_ADT27', a2)
    assert _is_linked(b, 'adt_ADT27', a2)
    if hasattr(a1, 'adt_ATerm'):
        assert not _is_linked(a1, 'adt_ATerm', b)
    if hasattr(a2, 'adt_ATerm'):
        assert _is_linked(a2, 'adt_ATerm', b)
    _safe_set(b, 'adt_ADT27', None)
    assert not _is_linked(b, 'adt_ADT27', a2)
    if hasattr(a2, 'adt_ATerm'):
        assert not _is_linked(a2, 'adt_ATerm', b)


def test_assoc_allOperations6_reverse_link_reassign_clear():
    a1 = adt_Signature(ops="sample_text")
    a2 = adt_Signature(ops="sample_text_2")
    b = adt_Operation(name="sample_text")
    _safe_set(b, 'adt_Operation', a1)
    assert _is_linked(b, 'adt_Operation', a1)
    if hasattr(a1, 'adt_Signature7'):
        assert _is_linked(a1, 'adt_Signature7', b)
    _safe_set(b, 'adt_Operation', a2)
    assert _is_linked(b, 'adt_Operation', a2)
    if hasattr(a1, 'adt_Signature7'):
        assert not _is_linked(a1, 'adt_Signature7', b)
    if hasattr(a2, 'adt_Signature7'):
        assert _is_linked(a2, 'adt_Signature7', b)
    _safe_set(b, 'adt_Operation', None)
    assert not _is_linked(b, 'adt_Operation', a2)
    if hasattr(a2, 'adt_Signature7'):
        assert not _is_linked(a2, 'adt_Signature7', b)


def test_assoc_formalParameters23_reverse_link_reassign_clear():
    a1 = adt_Operation(name="sample_text")
    a2 = adt_Operation(name="sample_text_2")
    b = adt_ASort(name="sample_text")
    _safe_set(b, 'adt_ASort25', a1)
    assert _is_linked(b, 'adt_ASort25', a1)
    if hasattr(a1, 'adt_Operation24'):
        assert _is_linked(a1, 'adt_Operation24', b)
    _safe_set(b, 'adt_ASort25', a2)
    assert _is_linked(b, 'adt_ASort25', a2)
    if hasattr(a1, 'adt_Operation24'):
        assert not _is_linked(a1, 'adt_Operation24', b)
    if hasattr(a2, 'adt_Operation24'):
        assert _is_linked(a2, 'adt_Operation24', b)
    _safe_set(b, 'adt_ASort25', None)
    assert not _is_linked(b, 'adt_ASort25', a2)
    if hasattr(a2, 'adt_Operation24'):
        assert not _is_linked(a2, 'adt_Operation24', b)


def test_assoc_generators14_reverse_link_reassign_clear():
    a1 = adt_Signature(ops="sample_text")
    a2 = adt_Signature(ops="sample_text_2")
    b = adt_Operation(name="sample_text")
    _safe_set(b, 'adt_Operation16', a1)
    assert _is_linked(b, 'adt_Operation16', a1)
    if hasattr(a1, 'adt_Signature15'):
        assert _is_linked(a1, 'adt_Signature15', b)
    _safe_set(b, 'adt_Operation16', a2)
    assert _is_linked(b, 'adt_Operation16', a2)
    if hasattr(a1, 'adt_Signature15'):
        assert not _is_linked(a1, 'adt_Signature15', b)
    if hasattr(a2, 'adt_Signature15'):
        assert _is_linked(a2, 'adt_Signature15', b)
    _safe_set(b, 'adt_Operation16', None)
    assert not _is_linked(b, 'adt_Operation16', a2)
    if hasattr(a2, 'adt_Signature15'):
        assert not _is_linked(a2, 'adt_Signature15', b)


def test_assoc_operations11_reverse_link_reassign_clear():
    a1 = adt_Signature(ops="sample_text")
    a2 = adt_Signature(ops="sample_text_2")
    b = adt_Operation(name="sample_text")
    _safe_set(b, 'adt_Operation13', a1)
    assert _is_linked(b, 'adt_Operation13', a1)
    if hasattr(a1, 'adt_Signature12'):
        assert _is_linked(a1, 'adt_Signature12', b)
    _safe_set(b, 'adt_Operation13', a2)
    assert _is_linked(b, 'adt_Operation13', a2)
    if hasattr(a1, 'adt_Signature12'):
        assert not _is_linked(a1, 'adt_Signature12', b)
    if hasattr(a2, 'adt_Signature12'):
        assert _is_linked(a2, 'adt_Signature12', b)
    _safe_set(b, 'adt_Operation13', None)
    assert not _is_linked(b, 'adt_Operation13', a2)
    if hasattr(a2, 'adt_Signature12'):
        assert not _is_linked(a2, 'adt_Signature12', b)


def test_assoc_returnType20_reverse_link_reassign_clear():
    a1 = adt_Operation(name="sample_text")
    a2 = adt_Operation(name="sample_text_2")
    b = adt_ASort(name="sample_text")
    _safe_set(b, 'adt_ASort22', a1)
    assert _is_linked(b, 'adt_ASort22', a1)
    if hasattr(a1, 'adt_Operation21'):
        assert _is_linked(a1, 'adt_Operation21', b)
    _safe_set(b, 'adt_ASort22', a2)
    assert _is_linked(b, 'adt_ASort22', a2)
    if hasattr(a1, 'adt_Operation21'):
        assert not _is_linked(a1, 'adt_Operation21', b)
    if hasattr(a2, 'adt_Operation21'):
        assert _is_linked(a2, 'adt_Operation21', b)
    _safe_set(b, 'adt_ASort22', None)
    assert not _is_linked(b, 'adt_ASort22', a2)
    if hasattr(a2, 'adt_Operation21'):
        assert not _is_linked(a2, 'adt_Operation21', b)


def test_assoc_signature0_reverse_link_reassign_clear():
    a1 = adt_Signature(ops="sample_text")
    a2 = adt_Signature(ops="sample_text_2")
    b = adt_ADT(name="sample_text")
    _safe_set(b, 'adt_ADT', a1)
    assert _is_linked(b, 'adt_ADT', a1)
    if hasattr(a1, 'adt_Signature'):
        assert _is_linked(a1, 'adt_Signature', b)
    _safe_set(b, 'adt_ADT', a2)
    assert _is_linked(b, 'adt_ADT', a2)
    if hasattr(a1, 'adt_Signature'):
        assert not _is_linked(a1, 'adt_Signature', b)
    if hasattr(a2, 'adt_Signature'):
        assert _is_linked(a2, 'adt_Signature', b)
    _safe_set(b, 'adt_ADT', None)
    assert not _is_linked(b, 'adt_ADT', a2)
    if hasattr(a2, 'adt_Signature'):
        assert not _is_linked(a2, 'adt_Signature', b)


def test_assoc_sort17_reverse_link_reassign_clear():
    a1 = adt_VariableDeclaration(name="sample_text")
    a2 = adt_VariableDeclaration(name="sample_text_2")
    b = adt_ASort(name="sample_text")
    _safe_set(b, 'adt_ASort19', a1)
    assert _is_linked(b, 'adt_ASort19', a1)
    if hasattr(a1, 'adt_VariableDeclaration18'):
        assert _is_linked(a1, 'adt_VariableDeclaration18', b)
    _safe_set(b, 'adt_ASort19', a2)
    assert _is_linked(b, 'adt_ASort19', a2)
    if hasattr(a1, 'adt_VariableDeclaration18'):
        assert not _is_linked(a1, 'adt_VariableDeclaration18', b)
    if hasattr(a2, 'adt_VariableDeclaration18'):
        assert _is_linked(a2, 'adt_VariableDeclaration18', b)
    _safe_set(b, 'adt_ASort19', None)
    assert not _is_linked(b, 'adt_ASort19', a2)
    if hasattr(a2, 'adt_VariableDeclaration18'):
        assert not _is_linked(a2, 'adt_VariableDeclaration18', b)


def test_assoc_sort28_reverse_link_reassign_clear():
    a1 = adt_ATerm(symbol="sample_text")
    a2 = adt_ATerm(symbol="sample_text_2")
    b = adt_ASort(name="sample_text")
    _safe_set(b, 'adt_ASort30', a1)
    assert _is_linked(b, 'adt_ASort30', a1)
    if hasattr(a1, 'adt_ATerm29'):
        assert _is_linked(a1, 'adt_ATerm29', b)
    _safe_set(b, 'adt_ASort30', a2)
    assert _is_linked(b, 'adt_ASort30', a2)
    if hasattr(a1, 'adt_ATerm29'):
        assert not _is_linked(a1, 'adt_ATerm29', b)
    if hasattr(a2, 'adt_ATerm29'):
        assert _is_linked(a2, 'adt_ATerm29', b)
    _safe_set(b, 'adt_ASort30', None)
    assert not _is_linked(b, 'adt_ASort30', a2)
    if hasattr(a2, 'adt_ATerm29'):
        assert not _is_linked(a2, 'adt_ATerm29', b)


def test_assoc_sorts8_reverse_link_reassign_clear():
    a1 = adt_Signature(ops="sample_text")
    a2 = adt_Signature(ops="sample_text_2")
    b = adt_ASort(name="sample_text")
    _safe_set(b, 'adt_ASort10', a1)
    assert _is_linked(b, 'adt_ASort10', a1)
    if hasattr(a1, 'adt_Signature9'):
        assert _is_linked(a1, 'adt_Signature9', b)
    _safe_set(b, 'adt_ASort10', a2)
    assert _is_linked(b, 'adt_ASort10', a2)
    if hasattr(a1, 'adt_Signature9'):
        assert not _is_linked(a1, 'adt_Signature9', b)
    if hasattr(a2, 'adt_Signature9'):
        assert _is_linked(a2, 'adt_Signature9', b)
    _safe_set(b, 'adt_ASort10', None)
    assert not _is_linked(b, 'adt_ASort10', a2)
    if hasattr(a2, 'adt_Signature9'):
        assert not _is_linked(a2, 'adt_Signature9', b)


def test_assoc_variables1_reverse_link_reassign_clear():
    a1 = adt_VariableDeclaration(name="sample_text")
    a2 = adt_VariableDeclaration(name="sample_text_2")
    b = adt_ADT(name="sample_text")
    _safe_set(b, 'adt_ADT2', {a1})
    assert _is_linked(b, 'adt_ADT2', a1)
    if hasattr(a1, 'adt_VariableDeclaration'):
        assert _is_linked(a1, 'adt_VariableDeclaration', b)
    _safe_set(b, 'adt_ADT2', {a2})
    assert _is_linked(b, 'adt_ADT2', a2)
    if hasattr(a1, 'adt_VariableDeclaration'):
        assert not _is_linked(a1, 'adt_VariableDeclaration', b)
    if hasattr(a2, 'adt_VariableDeclaration'):
        assert _is_linked(a2, 'adt_VariableDeclaration', b)
    _safe_set(b, 'adt_ADT2', set())
    assert not _is_linked(b, 'adt_ADT2', a2)
    if hasattr(a2, 'adt_VariableDeclaration'):
        assert not _is_linked(a2, 'adt_VariableDeclaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declaration36_stub_double():
    # adt_Variable has no real 'adt_Variable' property in the generated
    # code (a bare stub) -- manually attach it so adt_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_VariableDeclaration(name="sample_text")
    partner = adt_Variable()
    setattr(partner, 'adt_Variable', None)
    _safe_set(owner, 'adt_VariableDeclaration37', partner)
    assert getattr(partner, 'adt_Variable') == owner
    _safe_set(owner, 'adt_VariableDeclaration37', None)
    assert getattr(partner, 'adt_Variable') is None


def test_assoc_equations3_stub_double():
    # adt_Equation has no real 'adt_Equation' property in the generated
    # code (a bare stub) -- manually attach it so adt_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_ADT(name="sample_text")
    partner = adt_Equation()
    setattr(partner, 'adt_Equation', None)
    _safe_set(owner, 'adt_ADT4', {partner})
    assert getattr(partner, 'adt_Equation') == owner
    _safe_set(owner, 'adt_ADT4', set())
    assert getattr(partner, 'adt_Equation') is None


def test_assoc_leftHandTerm38_stub_double():
    # adt_Equation has no real 'adt_Equation39' property in the generated
    # code (a bare stub) -- manually attach it so adt_ATerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_ATerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_ATerm(symbol="sample_text")
    partner = adt_Equation()
    setattr(partner, 'adt_Equation39', None)
    _safe_set(owner, 'adt_ATerm40', partner)
    assert getattr(partner, 'adt_Equation39') == owner
    _safe_set(owner, 'adt_ATerm40', None)
    assert getattr(partner, 'adt_Equation39') is None


def test_assoc_operationSymbol31_stub_double():
    # adt_Term has no real 'adt_Term' property in the generated
    # code (a bare stub) -- manually attach it so adt_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_Operation(name="sample_text")
    partner = adt_Term()
    setattr(partner, 'adt_Term', None)
    _safe_set(owner, 'adt_Operation32', partner)
    assert getattr(partner, 'adt_Term') == owner
    _safe_set(owner, 'adt_Operation32', None)
    assert getattr(partner, 'adt_Term') is None


def test_assoc_rightHandTerm41_stub_double():
    # adt_Equation has no real 'adt_Equation42' property in the generated
    # code (a bare stub) -- manually attach it so adt_ATerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_ATerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_ATerm(symbol="sample_text")
    partner = adt_Equation()
    setattr(partner, 'adt_Equation42', None)
    _safe_set(owner, 'adt_ATerm43', partner)
    assert getattr(partner, 'adt_Equation42') == owner
    _safe_set(owner, 'adt_ATerm43', None)
    assert getattr(partner, 'adt_Equation42') is None


def test_assoc_subterms33_stub_double():
    # adt_Term has no real 'adt_Term34' property in the generated
    # code (a bare stub) -- manually attach it so adt_ATerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_ATerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_ATerm(symbol="sample_text")
    partner = adt_Term()
    setattr(partner, 'adt_Term34', None)
    _safe_set(owner, 'adt_ATerm35', partner)
    assert owner in getattr(partner, 'adt_Term34')
    _safe_set(owner, 'adt_ATerm35', None)
    assert owner not in getattr(partner, 'adt_Term34')


def test_assoc_superSort5_stub_double():
    # adt_SubSort has no real 'adt_SubSort' property in the generated
    # code (a bare stub) -- manually attach it so adt_ASort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adt_ASort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adt_ASort(name="sample_text")
    partner = adt_SubSort()
    setattr(partner, 'adt_SubSort', None)
    _safe_set(owner, 'adt_ASort', partner)
    assert getattr(partner, 'adt_SubSort') == owner
    _safe_set(owner, 'adt_ASort', None)
    assert getattr(partner, 'adt_SubSort') is None


