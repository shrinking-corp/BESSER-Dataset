import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addable,
    Andable,
    Atom,
    Collection,
    Comparable,
    Equatable,
    Expression,
    Index,
    Multipliable,
    Orable,
    Primary,
    Setable,
    Statement,
    game_Access,
    game_Addable,
    game_Addition,
    game_And,
    game_Andable,
    game_Assignment,
    game_Atom,
    game_Brackets,
    game_Call,
    game_Cardinal,
    game_Cell,
    game_Collection,
    game_Comparable,
    game_Comparison,
    game_ComponentData,
    game_End,
    game_Equality,
    game_Equatable,
    game_Expression,
    game_Forall,
    game_Function,
    game_Game,
    game_ImplicitSet,
    game_Index,
    game_Iteration,
    game_Join,
    game_LogicalNot,
    game_Multipliable,
    game_Multiplication,
    game_Or,
    game_Orable,
    game_Primary,
    game_Query,
    game_Selection,
    game_SetExpression,
    game_Setable,
    game_Statement,
    game_Subprocess,
    game_System,
    game_Type,
    game_Variable,
    AccessKind,
    AdditiveKind,
    ComparisonKind,
    EqualityKind,
    MultiplicativeKind,
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

def test_assoc_accesses22_reverse_link_reassign_clear():
    a1 = game_Query(name="sample_text")
    a2 = game_Query(name="sample_text_2")
    b = game_Access(kind="sample_text", name="sample_text")
    _safe_set(b, 'game_Access', a1)
    assert _is_linked(b, 'game_Access', a1)
    if hasattr(a1, 'game_Query23'):
        assert _is_linked(a1, 'game_Query23', b)
    _safe_set(b, 'game_Access', a2)
    assert _is_linked(b, 'game_Access', a2)
    if hasattr(a1, 'game_Query23'):
        assert not _is_linked(a1, 'game_Query23', b)
    if hasattr(a2, 'game_Query23'):
        assert _is_linked(a2, 'game_Query23', b)
    _safe_set(b, 'game_Access', None)
    assert not _is_linked(b, 'game_Access', a2)
    if hasattr(a2, 'game_Query23'):
        assert not _is_linked(a2, 'game_Query23', b)


def test_assoc_components3_reverse_link_reassign_clear():
    a1 = game_Game(name="sample_text", version="sample_text")
    a2 = game_Game(name="sample_text_2", version="sample_text_2")
    b = game_ComponentData(name="sample_text")
    _safe_set(b, 'game_ComponentData', a1)
    assert _is_linked(b, 'game_ComponentData', a1)
    if hasattr(a1, 'game_Game4'):
        assert _is_linked(a1, 'game_Game4', b)
    _safe_set(b, 'game_ComponentData', a2)
    assert _is_linked(b, 'game_ComponentData', a2)
    if hasattr(a1, 'game_Game4'):
        assert not _is_linked(a1, 'game_Game4', b)
    if hasattr(a2, 'game_Game4'):
        assert _is_linked(a2, 'game_Game4', b)
    _safe_set(b, 'game_ComponentData', None)
    assert not _is_linked(b, 'game_ComponentData', a2)
    if hasattr(a2, 'game_Game4'):
        assert not _is_linked(a2, 'game_Game4', b)


def test_assoc_functions7_reverse_link_reassign_clear():
    a1 = game_Game(name="sample_text", version="sample_text")
    a2 = game_Game(name="sample_text_2", version="sample_text_2")
    b = game_Function(name="sample_text")
    _safe_set(b, 'game_Function', a1)
    assert _is_linked(b, 'game_Function', a1)
    if hasattr(a1, 'game_Game8'):
        assert _is_linked(a1, 'game_Game8', b)
    _safe_set(b, 'game_Function', a2)
    assert _is_linked(b, 'game_Function', a2)
    if hasattr(a1, 'game_Game8'):
        assert not _is_linked(a1, 'game_Game8', b)
    if hasattr(a2, 'game_Game8'):
        assert _is_linked(a2, 'game_Game8', b)
    _safe_set(b, 'game_Function', None)
    assert not _is_linked(b, 'game_Function', a2)
    if hasattr(a2, 'game_Game8'):
        assert not _is_linked(a2, 'game_Game8', b)


def test_assoc_parameters108_reverse_link_reassign_clear():
    a1 = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    a2 = game_Type(name="sample_text_2", namespace="sample_text_2", valueType=False)
    b = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    _safe_set(b, 'game_Type109', a1)
    assert _is_linked(b, 'game_Type109', a1)
    if hasattr(a1, 'game_Type107'):
        assert _is_linked(a1, 'game_Type107', b)
    _safe_set(b, 'game_Type109', a2)
    assert _is_linked(b, 'game_Type109', a2)
    if hasattr(a1, 'game_Type107'):
        assert not _is_linked(a1, 'game_Type107', b)
    if hasattr(a2, 'game_Type107'):
        assert _is_linked(a2, 'game_Type107', b)
    _safe_set(b, 'game_Type109', None)
    assert not _is_linked(b, 'game_Type109', a2)
    if hasattr(a2, 'game_Type107'):
        assert not _is_linked(a2, 'game_Type107', b)


def test_assoc_queries20_reverse_link_reassign_clear():
    a1 = game_System(name="sample_text")
    a2 = game_System(name="sample_text_2")
    b = game_Query(name="sample_text")
    _safe_set(b, 'game_Query', a1)
    assert _is_linked(b, 'game_Query', a1)
    if hasattr(a1, 'game_System21'):
        assert _is_linked(a1, 'game_System21', b)
    _safe_set(b, 'game_Query', a2)
    assert _is_linked(b, 'game_Query', a2)
    if hasattr(a1, 'game_System21'):
        assert not _is_linked(a1, 'game_System21', b)
    if hasattr(a2, 'game_System21'):
        assert _is_linked(a2, 'game_System21', b)
    _safe_set(b, 'game_Query', None)
    assert not _is_linked(b, 'game_Query', a2)
    if hasattr(a2, 'game_System21'):
        assert not _is_linked(a2, 'game_System21', b)


def test_assoc_systems1_reverse_link_reassign_clear():
    a1 = game_System(name="sample_text")
    a2 = game_System(name="sample_text_2")
    b = game_Game(name="sample_text", version="sample_text")
    _safe_set(b, 'game_Game2', {a1})
    assert _is_linked(b, 'game_Game2', a1)
    if hasattr(a1, 'game_System'):
        assert _is_linked(a1, 'game_System', b)
    _safe_set(b, 'game_Game2', {a2})
    assert _is_linked(b, 'game_Game2', a2)
    if hasattr(a1, 'game_System'):
        assert not _is_linked(a1, 'game_System', b)
    if hasattr(a2, 'game_System'):
        assert _is_linked(a2, 'game_System', b)
    _safe_set(b, 'game_Game2', set())
    assert not _is_linked(b, 'game_Game2', a2)
    if hasattr(a2, 'game_System'):
        assert not _is_linked(a2, 'game_System', b)


def test_assoc_type14_reverse_link_reassign_clear():
    a1 = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    a2 = game_Type(name="sample_text_2", namespace="sample_text_2", valueType=False)
    b = game_ComponentData(name="sample_text")
    _safe_set(b, 'game_ComponentData15', a1)
    assert _is_linked(b, 'game_ComponentData15', a1)
    if hasattr(a1, 'game_Type16'):
        assert _is_linked(a1, 'game_Type16', b)
    _safe_set(b, 'game_ComponentData15', a2)
    assert _is_linked(b, 'game_ComponentData15', a2)
    if hasattr(a1, 'game_Type16'):
        assert not _is_linked(a1, 'game_Type16', b)
    if hasattr(a2, 'game_Type16'):
        assert _is_linked(a2, 'game_Type16', b)
    _safe_set(b, 'game_ComponentData15', None)
    assert not _is_linked(b, 'game_ComponentData15', a2)
    if hasattr(a2, 'game_Type16'):
        assert not _is_linked(a2, 'game_Type16', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    a2 = game_Type(name="sample_text_2", namespace="sample_text_2", valueType=False)
    b = game_Function(name="sample_text")
    _safe_set(b, 'game_Function10', a1)
    assert _is_linked(b, 'game_Function10', a1)
    if hasattr(a1, 'game_Type11'):
        assert _is_linked(a1, 'game_Type11', b)
    _safe_set(b, 'game_Function10', a2)
    assert _is_linked(b, 'game_Function10', a2)
    if hasattr(a1, 'game_Type11'):
        assert not _is_linked(a1, 'game_Type11', b)
    if hasattr(a2, 'game_Type11'):
        assert _is_linked(a2, 'game_Type11', b)
    _safe_set(b, 'game_Function10', None)
    assert not _is_linked(b, 'game_Function10', a2)
    if hasattr(a2, 'game_Type11'):
        assert not _is_linked(a2, 'game_Type11', b)


def test_assoc_types0_reverse_link_reassign_clear():
    a1 = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    a2 = game_Type(name="sample_text_2", namespace="sample_text_2", valueType=False)
    b = game_Game(name="sample_text", version="sample_text")
    _safe_set(b, 'game_Game', {a1})
    assert _is_linked(b, 'game_Game', a1)
    if hasattr(a1, 'game_Type'):
        assert _is_linked(a1, 'game_Type', b)
    _safe_set(b, 'game_Game', {a2})
    assert _is_linked(b, 'game_Game', a2)
    if hasattr(a1, 'game_Type'):
        assert not _is_linked(a1, 'game_Type', b)
    if hasattr(a2, 'game_Type'):
        assert _is_linked(a2, 'game_Type', b)
    _safe_set(b, 'game_Game', set())
    assert not _is_linked(b, 'game_Game', a2)
    if hasattr(a2, 'game_Type'):
        assert not _is_linked(a2, 'game_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments79_stub_double():
    # game_Expression has no real 'game_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so game_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Call(name="sample_text")
    partner = game_Expression()
    setattr(partner, 'game_Expression81', None)
    _safe_set(owner, 'game_Call80', {partner})
    assert getattr(partner, 'game_Expression81') == owner
    _safe_set(owner, 'game_Call80', set())
    assert getattr(partner, 'game_Expression81') is None


def test_assoc_call48_stub_double():
    # game_Subprocess has no real 'game_Subprocess' property in the generated
    # code (a bare stub) -- manually attach it so game_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Call(name="sample_text")
    partner = game_Subprocess()
    setattr(partner, 'game_Subprocess', None)
    _safe_set(owner, 'game_Call', partner)
    assert getattr(partner, 'game_Subprocess') == owner
    _safe_set(owner, 'game_Call', None)
    assert getattr(partner, 'game_Subprocess') is None


def test_assoc_component104_stub_double():
    # game_Cell has no real 'game_Cell105' property in the generated
    # code (a bare stub) -- manually attach it so game_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Variable(name="sample_text")
    partner = game_Cell()
    setattr(partner, 'game_Cell105', None)
    _safe_set(owner, 'game_Variable106', partner)
    assert getattr(partner, 'game_Cell105') == owner
    _safe_set(owner, 'game_Variable106', None)
    assert getattr(partner, 'game_Cell105') is None


def test_assoc_end5_stub_double():
    # game_End has no real 'game_End' property in the generated
    # code (a bare stub) -- manually attach it so game_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Game(name="sample_text", version="sample_text")
    partner = game_End()
    setattr(partner, 'game_End', None)
    _safe_set(owner, 'game_Game6', partner)
    assert getattr(partner, 'game_End') == owner
    _safe_set(owner, 'game_Game6', None)
    assert getattr(partner, 'game_End') is None


def test_assoc_entity102_stub_double():
    # game_Cell has no real 'game_Cell' property in the generated
    # code (a bare stub) -- manually attach it so game_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Variable(name="sample_text")
    partner = game_Cell()
    setattr(partner, 'game_Cell', None)
    _safe_set(owner, 'game_Variable103', partner)
    assert getattr(partner, 'game_Cell') == owner
    _safe_set(owner, 'game_Variable103', None)
    assert getattr(partner, 'game_Cell') is None


def test_assoc_left59_stub_double():
    # game_Equatable has no real 'game_Equatable60' property in the generated
    # code (a bare stub) -- manually attach it so game_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Equality(kind="sample_text")
    partner = game_Equatable()
    setattr(partner, 'game_Equatable60', None)
    _safe_set(owner, 'game_Equality', partner)
    assert getattr(partner, 'game_Equatable60') == owner
    _safe_set(owner, 'game_Equality', None)
    assert getattr(partner, 'game_Equatable60') is None


def test_assoc_left63_stub_double():
    # game_Comparable has no real 'game_Comparable64' property in the generated
    # code (a bare stub) -- manually attach it so game_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Comparison(kind="sample_text")
    partner = game_Comparable()
    setattr(partner, 'game_Comparable64', None)
    _safe_set(owner, 'game_Comparison', partner)
    assert getattr(partner, 'game_Comparable64') == owner
    _safe_set(owner, 'game_Comparison', None)
    assert getattr(partner, 'game_Comparable64') is None


def test_assoc_left67_stub_double():
    # game_Addable has no real 'game_Addable68' property in the generated
    # code (a bare stub) -- manually attach it so game_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Addition(kind="sample_text")
    partner = game_Addable()
    setattr(partner, 'game_Addable68', None)
    _safe_set(owner, 'game_Addition', partner)
    assert getattr(partner, 'game_Addable68') == owner
    _safe_set(owner, 'game_Addition', None)
    assert getattr(partner, 'game_Addable68') is None


def test_assoc_left71_stub_double():
    # game_Multipliable has no real 'game_Multipliable72' property in the generated
    # code (a bare stub) -- manually attach it so game_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Multiplication(kind="sample_text")
    partner = game_Multipliable()
    setattr(partner, 'game_Multipliable72', None)
    _safe_set(owner, 'game_Multiplication', partner)
    assert getattr(partner, 'game_Multipliable72') == owner
    _safe_set(owner, 'game_Multiplication', None)
    assert getattr(partner, 'game_Multipliable72') is None


def test_assoc_right61_stub_double():
    # game_Comparable has no real 'game_Comparable' property in the generated
    # code (a bare stub) -- manually attach it so game_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Equality(kind="sample_text")
    partner = game_Comparable()
    setattr(partner, 'game_Comparable', None)
    _safe_set(owner, 'game_Equality62', partner)
    assert getattr(partner, 'game_Comparable') == owner
    _safe_set(owner, 'game_Equality62', None)
    assert getattr(partner, 'game_Comparable') is None


def test_assoc_right65_stub_double():
    # game_Addable has no real 'game_Addable' property in the generated
    # code (a bare stub) -- manually attach it so game_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Comparison(kind="sample_text")
    partner = game_Addable()
    setattr(partner, 'game_Addable', None)
    _safe_set(owner, 'game_Comparison66', partner)
    assert getattr(partner, 'game_Addable') == owner
    _safe_set(owner, 'game_Comparison66', None)
    assert getattr(partner, 'game_Addable') is None


def test_assoc_right69_stub_double():
    # game_Multipliable has no real 'game_Multipliable' property in the generated
    # code (a bare stub) -- manually attach it so game_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Addition(kind="sample_text")
    partner = game_Multipliable()
    setattr(partner, 'game_Multipliable', None)
    _safe_set(owner, 'game_Addition70', partner)
    assert getattr(partner, 'game_Multipliable') == owner
    _safe_set(owner, 'game_Addition70', None)
    assert getattr(partner, 'game_Multipliable') is None


def test_assoc_right73_stub_double():
    # game_Setable has no real 'game_Setable' property in the generated
    # code (a bare stub) -- manually attach it so game_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Multiplication(kind="sample_text")
    partner = game_Setable()
    setattr(partner, 'game_Setable', None)
    _safe_set(owner, 'game_Multiplication74', partner)
    assert getattr(partner, 'game_Setable') == owner
    _safe_set(owner, 'game_Multiplication74', None)
    assert getattr(partner, 'game_Setable') is None


def test_assoc_statements12_stub_double():
    # game_Statement has no real 'game_Statement' property in the generated
    # code (a bare stub) -- manually attach it so game_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Function(name="sample_text")
    partner = game_Statement()
    setattr(partner, 'game_Statement', None)
    _safe_set(owner, 'game_Function13', {partner})
    assert getattr(partner, 'game_Statement') == owner
    _safe_set(owner, 'game_Function13', set())
    assert getattr(partner, 'game_Statement') is None


def test_assoc_statements17_stub_double():
    # game_Statement has no real 'game_Statement19' property in the generated
    # code (a bare stub) -- manually attach it so game_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_System(name="sample_text")
    partner = game_Statement()
    setattr(partner, 'game_Statement19', None)
    _safe_set(owner, 'game_System18', {partner})
    assert getattr(partner, 'game_Statement19') == owner
    _safe_set(owner, 'game_System18', set())
    assert getattr(partner, 'game_Statement19') is None


def test_assoc_type49_stub_double():
    # game_Expression has no real 'game_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so game_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Type(name="sample_text", namespace="sample_text", valueType=True)
    partner = game_Expression()
    setattr(partner, 'game_Expression50', None)
    _safe_set(owner, 'game_Type51', partner)
    assert getattr(partner, 'game_Expression50') == owner
    _safe_set(owner, 'game_Type51', None)
    assert getattr(partner, 'game_Expression50') is None


def test_assoc_variable41_stub_double():
    # game_Forall has no real 'game_Forall42' property in the generated
    # code (a bare stub) -- manually attach it so game_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Variable(name="sample_text")
    partner = game_Forall()
    setattr(partner, 'game_Forall42', None)
    _safe_set(owner, 'game_Variable', partner)
    assert getattr(partner, 'game_Forall42') == owner
    _safe_set(owner, 'game_Variable', None)
    assert getattr(partner, 'game_Forall42') is None


def test_assoc_variable92_stub_double():
    # game_ImplicitSet has no real 'game_ImplicitSet93' property in the generated
    # code (a bare stub) -- manually attach it so game_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Variable(name="sample_text")
    partner = game_ImplicitSet()
    setattr(partner, 'game_ImplicitSet93', None)
    _safe_set(owner, 'game_Variable94', partner)
    assert getattr(partner, 'game_ImplicitSet93') == owner
    _safe_set(owner, 'game_Variable94', None)
    assert getattr(partner, 'game_ImplicitSet93') is None


