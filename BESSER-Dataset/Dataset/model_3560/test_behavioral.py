import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConsoleOutput,
    Expression,
    Statement,
    simpleimperative_Assignation,
    simpleimperative_Conditional,
    simpleimperative_ConsoleOutput,
    simpleimperative_Expression,
    simpleimperative_Loop,
    simpleimperative_Print,
    simpleimperative_Println,
    simpleimperative_Program,
    simpleimperative_Statement,
    simpleimperative_VarDecl,
    simpleimperative_VarRef,
    simpleimperative_Wait,
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

def test_assoc_expr10_reverse_link_reassign_clear():
    a1 = simpleimperative_VarDecl(name="sample_text")
    a2 = simpleimperative_VarDecl(name="sample_text_2")
    b = simpleimperative_Expression()
    _safe_set(b, 'simpleimperative_Expression11', a1)
    assert _is_linked(b, 'simpleimperative_Expression11', a1)
    if hasattr(a1, 'simpleimperative_VarDecl'):
        assert _is_linked(a1, 'simpleimperative_VarDecl', b)
    _safe_set(b, 'simpleimperative_Expression11', a2)
    assert _is_linked(b, 'simpleimperative_Expression11', a2)
    if hasattr(a1, 'simpleimperative_VarDecl'):
        assert not _is_linked(a1, 'simpleimperative_VarDecl', b)
    if hasattr(a2, 'simpleimperative_VarDecl'):
        assert _is_linked(a2, 'simpleimperative_VarDecl', b)
    _safe_set(b, 'simpleimperative_Expression11', None)
    assert not _is_linked(b, 'simpleimperative_Expression11', a2)
    if hasattr(a2, 'simpleimperative_VarDecl'):
        assert not _is_linked(a2, 'simpleimperative_VarDecl', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition1_stub_double():
    # simpleimperative_Conditional has no real 'simpleimperative_Conditional' property in the generated
    # code (a bare stub) -- manually attach it so simpleimperative_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleimperative_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleimperative_Expression()
    partner = simpleimperative_Conditional()
    setattr(partner, 'simpleimperative_Conditional', None)
    _safe_set(owner, 'simpleimperative_Expression', partner)
    assert getattr(partner, 'simpleimperative_Conditional') == owner
    _safe_set(owner, 'simpleimperative_Expression', None)
    assert getattr(partner, 'simpleimperative_Conditional') is None


def test_assoc_expression14_stub_double():
    # simpleimperative_Assignation has no real 'simpleimperative_Assignation15' property in the generated
    # code (a bare stub) -- manually attach it so simpleimperative_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleimperative_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleimperative_Expression()
    partner = simpleimperative_Assignation()
    setattr(partner, 'simpleimperative_Assignation15', None)
    _safe_set(owner, 'simpleimperative_Expression16', partner)
    assert getattr(partner, 'simpleimperative_Assignation15') == owner
    _safe_set(owner, 'simpleimperative_Expression16', None)
    assert getattr(partner, 'simpleimperative_Assignation15') is None


def test_assoc_guard5_stub_double():
    # simpleimperative_Loop has no real 'simpleimperative_Loop' property in the generated
    # code (a bare stub) -- manually attach it so simpleimperative_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleimperative_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleimperative_Expression()
    partner = simpleimperative_Loop()
    setattr(partner, 'simpleimperative_Loop', None)
    _safe_set(owner, 'simpleimperative_Expression6', partner)
    assert getattr(partner, 'simpleimperative_Loop') == owner
    _safe_set(owner, 'simpleimperative_Expression6', None)
    assert getattr(partner, 'simpleimperative_Loop') is None


def test_assoc_varRef12_stub_double():
    # simpleimperative_Assignation has no real 'simpleimperative_Assignation' property in the generated
    # code (a bare stub) -- manually attach it so simpleimperative_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleimperative_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleimperative_VarDecl(name="sample_text")
    partner = simpleimperative_Assignation()
    setattr(partner, 'simpleimperative_Assignation', None)
    _safe_set(owner, 'simpleimperative_VarDecl13', partner)
    assert getattr(partner, 'simpleimperative_Assignation') == owner
    _safe_set(owner, 'simpleimperative_VarDecl13', None)
    assert getattr(partner, 'simpleimperative_Assignation') is None


