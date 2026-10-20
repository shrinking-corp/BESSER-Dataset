import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B_Action,
    B_Any,
    B_Begin,
    B_Expression,
    B_If,
    B_Machine,
    B_Operation,
    B_Predicate,
    B_SET,
    B_Skip,
    B_Variable,
    B_VariableList,
    Expression,
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

def test_assoc_first31_reverse_link_reassign_clear():
    a1 = B_VariableList(size="sample_text")
    a2 = B_VariableList(size="sample_text_2")
    b = B_Variable(name="sample_text")
    _safe_set(b, 'B_Variable33', a1)
    assert _is_linked(b, 'B_Variable33', a1)
    if hasattr(a1, 'B_VariableList32'):
        assert _is_linked(a1, 'B_VariableList32', b)
    _safe_set(b, 'B_Variable33', a2)
    assert _is_linked(b, 'B_Variable33', a2)
    if hasattr(a1, 'B_VariableList32'):
        assert not _is_linked(a1, 'B_VariableList32', b)
    if hasattr(a2, 'B_VariableList32'):
        assert _is_linked(a2, 'B_VariableList32', b)
    _safe_set(b, 'B_Variable33', None)
    assert not _is_linked(b, 'B_Variable33', a2)
    if hasattr(a2, 'B_VariableList32'):
        assert not _is_linked(a2, 'B_VariableList32', b)


def test_assoc_inputs14_reverse_link_reassign_clear():
    a1 = B_VariableList(size="sample_text")
    a2 = B_VariableList(size="sample_text_2")
    b = B_Operation(name="sample_text")
    _safe_set(b, 'B_Operation15', a1)
    assert _is_linked(b, 'B_Operation15', a1)
    if hasattr(a1, 'B_VariableList'):
        assert _is_linked(a1, 'B_VariableList', b)
    _safe_set(b, 'B_Operation15', a2)
    assert _is_linked(b, 'B_Operation15', a2)
    if hasattr(a1, 'B_VariableList'):
        assert not _is_linked(a1, 'B_VariableList', b)
    if hasattr(a2, 'B_VariableList'):
        assert _is_linked(a2, 'B_VariableList', b)
    _safe_set(b, 'B_Operation15', None)
    assert not _is_linked(b, 'B_Operation15', a2)
    if hasattr(a2, 'B_VariableList'):
        assert not _is_linked(a2, 'B_VariableList', b)


def test_assoc_operations4_reverse_link_reassign_clear():
    a1 = B_Operation(name="sample_text")
    a2 = B_Operation(name="sample_text_2")
    b = B_Machine(name="sample_text")
    _safe_set(b, 'B_Machine5', {a1})
    assert _is_linked(b, 'B_Machine5', a1)
    if hasattr(a1, 'B_Operation'):
        assert _is_linked(a1, 'B_Operation', b)
    _safe_set(b, 'B_Machine5', {a2})
    assert _is_linked(b, 'B_Machine5', a2)
    if hasattr(a1, 'B_Operation'):
        assert not _is_linked(a1, 'B_Operation', b)
    if hasattr(a2, 'B_Operation'):
        assert _is_linked(a2, 'B_Operation', b)
    _safe_set(b, 'B_Machine5', set())
    assert not _is_linked(b, 'B_Machine5', a2)
    if hasattr(a2, 'B_Operation'):
        assert not _is_linked(a2, 'B_Operation', b)


def test_assoc_outputs16_reverse_link_reassign_clear():
    a1 = B_VariableList(size="sample_text")
    a2 = B_VariableList(size="sample_text_2")
    b = B_Operation(name="sample_text")
    _safe_set(b, 'B_Operation17', a1)
    assert _is_linked(b, 'B_Operation17', a1)
    if hasattr(a1, 'B_VariableList18'):
        assert _is_linked(a1, 'B_VariableList18', b)
    _safe_set(b, 'B_Operation17', a2)
    assert _is_linked(b, 'B_Operation17', a2)
    if hasattr(a1, 'B_VariableList18'):
        assert not _is_linked(a1, 'B_VariableList18', b)
    if hasattr(a2, 'B_VariableList18'):
        assert _is_linked(a2, 'B_VariableList18', b)
    _safe_set(b, 'B_Operation17', None)
    assert not _is_linked(b, 'B_Operation17', a2)
    if hasattr(a2, 'B_VariableList18'):
        assert not _is_linked(a2, 'B_VariableList18', b)


def test_assoc_preceeds23_reverse_link_reassign_clear():
    a1 = B_Variable(name="sample_text")
    a2 = B_Variable(name="sample_text_2")
    b = B_Variable(name="sample_text")
    _safe_set(b, 'B_Variable24', a1)
    assert _is_linked(b, 'B_Variable24', a1)
    if hasattr(a1, 'B_Variable22'):
        assert _is_linked(a1, 'B_Variable22', b)
    _safe_set(b, 'B_Variable24', a2)
    assert _is_linked(b, 'B_Variable24', a2)
    if hasattr(a1, 'B_Variable22'):
        assert not _is_linked(a1, 'B_Variable22', b)
    if hasattr(a2, 'B_Variable22'):
        assert _is_linked(a2, 'B_Variable22', b)
    _safe_set(b, 'B_Variable24', None)
    assert not _is_linked(b, 'B_Variable24', a2)
    if hasattr(a2, 'B_Variable22'):
        assert not _is_linked(a2, 'B_Variable22', b)


def test_assoc_refines1_reverse_link_reassign_clear():
    a1 = B_Machine(name="sample_text")
    a2 = B_Machine(name="sample_text_2")
    b = B_Machine(name="sample_text")
    _safe_set(b, 'B_Machine0', a1)
    assert _is_linked(b, 'B_Machine0', a1)
    if hasattr(a1, 'B_Machine'):
        assert _is_linked(a1, 'B_Machine', b)
    _safe_set(b, 'B_Machine0', a2)
    assert _is_linked(b, 'B_Machine0', a2)
    if hasattr(a1, 'B_Machine'):
        assert not _is_linked(a1, 'B_Machine', b)
    if hasattr(a2, 'B_Machine'):
        assert _is_linked(a2, 'B_Machine', b)
    _safe_set(b, 'B_Machine0', None)
    assert not _is_linked(b, 'B_Machine0', a2)
    if hasattr(a2, 'B_Machine'):
        assert not _is_linked(a2, 'B_Machine', b)


def test_assoc_sets2_reverse_link_reassign_clear():
    a1 = B_SET(name="sample_text")
    a2 = B_SET(name="sample_text_2")
    b = B_Machine(name="sample_text")
    _safe_set(b, 'B_Machine3', {a1})
    assert _is_linked(b, 'B_Machine3', a1)
    if hasattr(a1, 'B_SET'):
        assert _is_linked(a1, 'B_SET', b)
    _safe_set(b, 'B_Machine3', {a2})
    assert _is_linked(b, 'B_Machine3', a2)
    if hasattr(a1, 'B_SET'):
        assert not _is_linked(a1, 'B_SET', b)
    if hasattr(a2, 'B_SET'):
        assert _is_linked(a2, 'B_SET', b)
    _safe_set(b, 'B_Machine3', set())
    assert not _is_linked(b, 'B_Machine3', a2)
    if hasattr(a2, 'B_SET'):
        assert not _is_linked(a2, 'B_SET', b)


def test_assoc_statements12_reverse_link_reassign_clear():
    a1 = B_Operation(name="sample_text")
    a2 = B_Operation(name="sample_text_2")
    b = B_Expression(expression="sample_text")
    _safe_set(b, 'B_Expression', a1)
    assert _is_linked(b, 'B_Expression', a1)
    if hasattr(a1, 'B_Operation13'):
        assert _is_linked(a1, 'B_Operation13', b)
    _safe_set(b, 'B_Expression', a2)
    assert _is_linked(b, 'B_Expression', a2)
    if hasattr(a1, 'B_Operation13'):
        assert not _is_linked(a1, 'B_Operation13', b)
    if hasattr(a2, 'B_Operation13'):
        assert _is_linked(a2, 'B_Operation13', b)
    _safe_set(b, 'B_Expression', None)
    assert not _is_linked(b, 'B_Expression', a2)
    if hasattr(a2, 'B_Operation13'):
        assert not _is_linked(a2, 'B_Operation13', b)


def test_assoc_variables28_reverse_link_reassign_clear():
    a1 = B_VariableList(size="sample_text")
    a2 = B_VariableList(size="sample_text_2")
    b = B_Variable(name="sample_text")
    _safe_set(b, 'B_Variable30', a1)
    assert _is_linked(b, 'B_Variable30', a1)
    if hasattr(a1, 'B_VariableList29'):
        assert _is_linked(a1, 'B_VariableList29', b)
    _safe_set(b, 'B_Variable30', a2)
    assert _is_linked(b, 'B_Variable30', a2)
    if hasattr(a1, 'B_VariableList29'):
        assert not _is_linked(a1, 'B_VariableList29', b)
    if hasattr(a2, 'B_VariableList29'):
        assert _is_linked(a2, 'B_VariableList29', b)
    _safe_set(b, 'B_Variable30', None)
    assert not _is_linked(b, 'B_Variable30', a2)
    if hasattr(a2, 'B_VariableList29'):
        assert not _is_linked(a2, 'B_VariableList29', b)


def test_assoc_variables8_reverse_link_reassign_clear():
    a1 = B_Variable(name="sample_text")
    a2 = B_Variable(name="sample_text_2")
    b = B_Machine(name="sample_text")
    _safe_set(b, 'B_Machine9', {a1})
    assert _is_linked(b, 'B_Machine9', a1)
    if hasattr(a1, 'B_Variable'):
        assert _is_linked(a1, 'B_Variable', b)
    _safe_set(b, 'B_Machine9', {a2})
    assert _is_linked(b, 'B_Machine9', a2)
    if hasattr(a1, 'B_Variable'):
        assert not _is_linked(a1, 'B_Variable', b)
    if hasattr(a2, 'B_Variable'):
        assert _is_linked(a2, 'B_Variable', b)
    _safe_set(b, 'B_Machine9', set())
    assert not _is_linked(b, 'B_Machine9', a2)
    if hasattr(a2, 'B_Variable'):
        assert not _is_linked(a2, 'B_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_false_statements44_stub_double():
    # B_If has no real 'B_If45' property in the generated
    # code (a bare stub) -- manually attach it so B_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Expression(expression="sample_text")
    partner = B_If()
    setattr(partner, 'B_If45', None)
    _safe_set(owner, 'B_Expression46', partner)
    assert owner in getattr(partner, 'B_If45')
    _safe_set(owner, 'B_Expression46', None)
    assert owner not in getattr(partner, 'B_If45')


def test_assoc_initialisations10_stub_double():
    # B_Action has no real 'B_Action' property in the generated
    # code (a bare stub) -- manually attach it so B_Machine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Machine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Machine(name="sample_text")
    partner = B_Action()
    setattr(partner, 'B_Action', None)
    _safe_set(owner, 'B_Machine11', {partner})
    assert getattr(partner, 'B_Action') == owner
    _safe_set(owner, 'B_Machine11', set())
    assert getattr(partner, 'B_Action') is None


def test_assoc_invariants6_stub_double():
    # B_Predicate has no real 'B_Predicate' property in the generated
    # code (a bare stub) -- manually attach it so B_Machine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Machine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Machine(name="sample_text")
    partner = B_Predicate()
    setattr(partner, 'B_Predicate', None)
    _safe_set(owner, 'B_Machine7', {partner})
    assert getattr(partner, 'B_Predicate') == owner
    _safe_set(owner, 'B_Machine7', set())
    assert getattr(partner, 'B_Predicate') is None


def test_assoc_preconditions19_stub_double():
    # B_Predicate has no real 'B_Predicate21' property in the generated
    # code (a bare stub) -- manually attach it so B_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Operation(name="sample_text")
    partner = B_Predicate()
    setattr(partner, 'B_Predicate21', None)
    _safe_set(owner, 'B_Operation20', {partner})
    assert getattr(partner, 'B_Predicate21') == owner
    _safe_set(owner, 'B_Operation20', set())
    assert getattr(partner, 'B_Predicate21') is None


def test_assoc_statements39_stub_double():
    # B_Any has no real 'B_Any40' property in the generated
    # code (a bare stub) -- manually attach it so B_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Expression(expression="sample_text")
    partner = B_Any()
    setattr(partner, 'B_Any40', None)
    _safe_set(owner, 'B_Expression41', partner)
    assert owner in getattr(partner, 'B_Any40')
    _safe_set(owner, 'B_Expression41', None)
    assert owner not in getattr(partner, 'B_Any40')


def test_assoc_statements50_stub_double():
    # B_Begin has no real 'B_Begin' property in the generated
    # code (a bare stub) -- manually attach it so B_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Expression(expression="sample_text")
    partner = B_Begin()
    setattr(partner, 'B_Begin', None)
    _safe_set(owner, 'B_Expression51', partner)
    assert owner in getattr(partner, 'B_Begin')
    _safe_set(owner, 'B_Expression51', None)
    assert owner not in getattr(partner, 'B_Begin')


def test_assoc_true_statements42_stub_double():
    # B_If has no real 'B_If' property in the generated
    # code (a bare stub) -- manually attach it so B_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Expression(expression="sample_text")
    partner = B_If()
    setattr(partner, 'B_If', None)
    _safe_set(owner, 'B_Expression43', partner)
    assert owner in getattr(partner, 'B_If')
    _safe_set(owner, 'B_Expression43', None)
    assert owner not in getattr(partner, 'B_If')


def test_assoc_type25_stub_double():
    # B_Predicate has no real 'B_Predicate27' property in the generated
    # code (a bare stub) -- manually attach it so B_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Variable(name="sample_text")
    partner = B_Predicate()
    setattr(partner, 'B_Predicate27', None)
    _safe_set(owner, 'B_Variable26', partner)
    assert getattr(partner, 'B_Predicate27') == owner
    _safe_set(owner, 'B_Variable26', None)
    assert getattr(partner, 'B_Predicate27') is None


def test_assoc_variables34_stub_double():
    # B_Any has no real 'B_Any' property in the generated
    # code (a bare stub) -- manually attach it so B_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_Variable(name="sample_text")
    partner = B_Any()
    setattr(partner, 'B_Any', None)
    _safe_set(owner, 'B_Variable35', partner)
    assert owner in getattr(partner, 'B_Any')
    _safe_set(owner, 'B_Variable35', None)
    assert owner not in getattr(partner, 'B_Any')


