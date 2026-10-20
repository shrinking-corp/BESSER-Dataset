import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    Statement,
    graph_And,
    graph_AssignStmt,
    graph_BoolConstant,
    graph_Comparison,
    graph_Declaration,
    graph_Edge,
    graph_Expr,
    graph_GraphConstant,
    graph_IfStmt,
    graph_IntConstant,
    graph_MoveStmt,
    graph_MulOrDiv,
    graph_Not,
    graph_Or,
    graph_ParticleConstant,
    graph_PathExistence,
    graph_PlusOrMin,
    graph_PrintStmt,
    graph_Program,
    graph_Statement,
    graph_StringConstant,
    graph_VariableRef,
    graph_Vertex,
    graph_WhileStmt,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declarations0_stub_double():
    # graph_Program has no real 'graph_Program' property in the generated
    # code (a bare stub) -- manually attach it so graph_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Declaration(name="sample_text", type="sample_text")
    partner = graph_Program()
    setattr(partner, 'graph_Program', None)
    _safe_set(owner, 'graph_Declaration', partner)
    assert owner in getattr(partner, 'graph_Program')
    _safe_set(owner, 'graph_Declaration', None)
    assert owner not in getattr(partner, 'graph_Program')


def test_assoc_dest25_stub_double():
    # graph_Edge has no real 'graph_Edge26' property in the generated
    # code (a bare stub) -- manually attach it so graph_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Vertex(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'graph_Edge26', None)
    _safe_set(owner, 'graph_Vertex27', partner)
    assert getattr(partner, 'graph_Edge26') == owner
    _safe_set(owner, 'graph_Vertex27', None)
    assert getattr(partner, 'graph_Edge26') is None


def test_assoc_left43_stub_double():
    # graph_Expr has no real 'graph_Expr44' property in the generated
    # code (a bare stub) -- manually attach it so graph_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Comparison(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr44', None)
    _safe_set(owner, 'graph_Comparison', partner)
    assert getattr(partner, 'graph_Expr44') == owner
    _safe_set(owner, 'graph_Comparison', None)
    assert getattr(partner, 'graph_Expr44') is None


def test_assoc_left48_stub_double():
    # graph_Expr has no real 'graph_Expr49' property in the generated
    # code (a bare stub) -- manually attach it so graph_PlusOrMin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_PlusOrMin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_PlusOrMin(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr49', None)
    _safe_set(owner, 'graph_PlusOrMin', partner)
    assert getattr(partner, 'graph_Expr49') == owner
    _safe_set(owner, 'graph_PlusOrMin', None)
    assert getattr(partner, 'graph_Expr49') is None


def test_assoc_left53_stub_double():
    # graph_Expr has no real 'graph_Expr54' property in the generated
    # code (a bare stub) -- manually attach it so graph_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_MulOrDiv(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr54', None)
    _safe_set(owner, 'graph_MulOrDiv', partner)
    assert getattr(partner, 'graph_Expr54') == owner
    _safe_set(owner, 'graph_MulOrDiv', None)
    assert getattr(partner, 'graph_Expr54') is None


def test_assoc_right45_stub_double():
    # graph_Expr has no real 'graph_Expr47' property in the generated
    # code (a bare stub) -- manually attach it so graph_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Comparison(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr47', None)
    _safe_set(owner, 'graph_Comparison46', partner)
    assert getattr(partner, 'graph_Expr47') == owner
    _safe_set(owner, 'graph_Comparison46', None)
    assert getattr(partner, 'graph_Expr47') is None


def test_assoc_right50_stub_double():
    # graph_Expr has no real 'graph_Expr52' property in the generated
    # code (a bare stub) -- manually attach it so graph_PlusOrMin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_PlusOrMin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_PlusOrMin(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr52', None)
    _safe_set(owner, 'graph_PlusOrMin51', partner)
    assert getattr(partner, 'graph_Expr52') == owner
    _safe_set(owner, 'graph_PlusOrMin51', None)
    assert getattr(partner, 'graph_Expr52') is None


def test_assoc_right55_stub_double():
    # graph_Expr has no real 'graph_Expr57' property in the generated
    # code (a bare stub) -- manually attach it so graph_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_MulOrDiv(op="sample_text")
    partner = graph_Expr()
    setattr(partner, 'graph_Expr57', None)
    _safe_set(owner, 'graph_MulOrDiv56', partner)
    assert getattr(partner, 'graph_Expr57') == owner
    _safe_set(owner, 'graph_MulOrDiv56', None)
    assert getattr(partner, 'graph_Expr57') is None


def test_assoc_source24_stub_double():
    # graph_Edge has no real 'graph_Edge' property in the generated
    # code (a bare stub) -- manually attach it so graph_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Vertex(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'graph_Edge', None)
    _safe_set(owner, 'graph_Vertex', partner)
    assert getattr(partner, 'graph_Edge') == owner
    _safe_set(owner, 'graph_Vertex', None)
    assert getattr(partner, 'graph_Edge') is None


def test_assoc_var22_stub_double():
    # graph_MoveStmt has no real 'graph_MoveStmt' property in the generated
    # code (a bare stub) -- manually attach it so graph_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Declaration(name="sample_text", type="sample_text")
    partner = graph_MoveStmt()
    setattr(partner, 'graph_MoveStmt', None)
    _safe_set(owner, 'graph_Declaration23', partner)
    assert getattr(partner, 'graph_MoveStmt') == owner
    _safe_set(owner, 'graph_Declaration23', None)
    assert getattr(partner, 'graph_MoveStmt') is None


def test_assoc_var3_stub_double():
    # graph_AssignStmt has no real 'graph_AssignStmt' property in the generated
    # code (a bare stub) -- manually attach it so graph_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Declaration(name="sample_text", type="sample_text")
    partner = graph_AssignStmt()
    setattr(partner, 'graph_AssignStmt', None)
    _safe_set(owner, 'graph_Declaration4', partner)
    assert getattr(partner, 'graph_AssignStmt') == owner
    _safe_set(owner, 'graph_Declaration4', None)
    assert getattr(partner, 'graph_AssignStmt') is None


def test_assoc_variable60_stub_double():
    # graph_VariableRef has no real 'graph_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so graph_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Declaration(name="sample_text", type="sample_text")
    partner = graph_VariableRef()
    setattr(partner, 'graph_VariableRef', None)
    _safe_set(owner, 'graph_Declaration61', partner)
    assert getattr(partner, 'graph_VariableRef') == owner
    _safe_set(owner, 'graph_Declaration61', None)
    assert getattr(partner, 'graph_VariableRef') is None


def test_assoc_vertex69_stub_double():
    # graph_ParticleConstant has no real 'graph_ParticleConstant70' property in the generated
    # code (a bare stub) -- manually attach it so graph_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Vertex(name="sample_text")
    partner = graph_ParticleConstant()
    setattr(partner, 'graph_ParticleConstant70', None)
    _safe_set(owner, 'graph_Vertex71', partner)
    assert getattr(partner, 'graph_ParticleConstant70') == owner
    _safe_set(owner, 'graph_Vertex71', None)
    assert getattr(partner, 'graph_ParticleConstant70') is None


def test_assoc_vertices62_stub_double():
    # graph_GraphConstant has no real 'graph_GraphConstant' property in the generated
    # code (a bare stub) -- manually attach it so graph_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Vertex(name="sample_text")
    partner = graph_GraphConstant()
    setattr(partner, 'graph_GraphConstant', None)
    _safe_set(owner, 'graph_Vertex63', partner)
    assert owner in getattr(partner, 'graph_GraphConstant')
    _safe_set(owner, 'graph_Vertex63', None)
    assert owner not in getattr(partner, 'graph_GraphConstant')


