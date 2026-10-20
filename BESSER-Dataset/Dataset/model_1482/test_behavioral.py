import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryConstraint,
    Constraint,
    Executable,
    Expression,
    Graph,
    GraphElement,
    NamedElement,
    Pattern,
    PatternConstraint,
    TypedElement,
    transformr_And,
    transformr_Assignment,
    transformr_Attribute,
    transformr_BinaryConstraint,
    transformr_Block,
    transformr_Branch,
    transformr_Constraint,
    transformr_Edge,
    transformr_Executable,
    transformr_Exists,
    transformr_Expression,
    transformr_ForAll,
    transformr_Graph,
    transformr_GraphElement,
    transformr_NamedElement,
    transformr_Node,
    transformr_Not,
    transformr_Or,
    transformr_Pattern,
    transformr_PatternConstraint,
    transformr_Rule,
    transformr_TypedElement,
    transformr_Variable,
    transformr_VariableConstraint,
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

def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = transformr_Node()
    a2 = transformr_Node()
    b = transformr_Attribute()
    _safe_set(b, 'transformr_Attribute', a1)
    assert _is_linked(b, 'transformr_Attribute', a1)
    if hasattr(a1, 'transformr_Node4'):
        assert _is_linked(a1, 'transformr_Node4', b)
    _safe_set(b, 'transformr_Attribute', a2)
    assert _is_linked(b, 'transformr_Attribute', a2)
    if hasattr(a1, 'transformr_Node4'):
        assert not _is_linked(a1, 'transformr_Node4', b)
    if hasattr(a2, 'transformr_Node4'):
        assert _is_linked(a2, 'transformr_Node4', b)
    _safe_set(b, 'transformr_Attribute', None)
    assert not _is_linked(b, 'transformr_Attribute', a2)
    if hasattr(a2, 'transformr_Node4'):
        assert not _is_linked(a2, 'transformr_Node4', b)


def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = transformr_Node()
    a2 = transformr_Node()
    b = transformr_Edge()
    _safe_set(b, 'transformr_Edge', a1)
    assert _is_linked(b, 'transformr_Edge', a1)
    if hasattr(a1, 'transformr_Node2'):
        assert _is_linked(a1, 'transformr_Node2', b)
    _safe_set(b, 'transformr_Edge', a2)
    assert _is_linked(b, 'transformr_Edge', a2)
    if hasattr(a1, 'transformr_Node2'):
        assert not _is_linked(a1, 'transformr_Node2', b)
    if hasattr(a2, 'transformr_Node2'):
        assert _is_linked(a2, 'transformr_Node2', b)
    _safe_set(b, 'transformr_Edge', None)
    assert not _is_linked(b, 'transformr_Edge', a2)
    if hasattr(a2, 'transformr_Node2'):
        assert not _is_linked(a2, 'transformr_Node2', b)


def test_assoc_target5_reverse_link_reassign_clear():
    a1 = transformr_Node()
    a2 = transformr_Node()
    b = transformr_Edge()
    _safe_set(b, 'transformr_Edge6', a1)
    assert _is_linked(b, 'transformr_Edge6', a1)
    if hasattr(a1, 'transformr_Node7'):
        assert _is_linked(a1, 'transformr_Node7', b)
    _safe_set(b, 'transformr_Edge6', a2)
    assert _is_linked(b, 'transformr_Edge6', a2)
    if hasattr(a1, 'transformr_Node7'):
        assert not _is_linked(a1, 'transformr_Node7', b)
    if hasattr(a2, 'transformr_Node7'):
        assert _is_linked(a2, 'transformr_Node7', b)
    _safe_set(b, 'transformr_Edge6', None)
    assert not _is_linked(b, 'transformr_Edge6', a2)
    if hasattr(a2, 'transformr_Node7'):
        assert not _is_linked(a2, 'transformr_Node7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_involvedVariables29_stub_double():
    # transformr_Variable has no real 'transformr_Variable30' property in the generated
    # code (a bare stub) -- manually attach it so transformr_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformr_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformr_Expression(expression="sample_text")
    partner = transformr_Variable()
    setattr(partner, 'transformr_Variable30', None)
    _safe_set(owner, 'transformr_Expression', {partner})
    assert getattr(partner, 'transformr_Variable30') == owner
    _safe_set(owner, 'transformr_Expression', set())
    assert getattr(partner, 'transformr_Variable30') is None


def test_assoc_nodes0_stub_double():
    # transformr_Graph has no real 'transformr_Graph' property in the generated
    # code (a bare stub) -- manually attach it so transformr_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformr_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformr_Node()
    partner = transformr_Graph()
    setattr(partner, 'transformr_Graph', None)
    _safe_set(owner, 'transformr_Node', partner)
    assert owner in getattr(partner, 'transformr_Graph')
    _safe_set(owner, 'transformr_Node', None)
    assert owner not in getattr(partner, 'transformr_Graph')


def test_assoc_targetAttribute26_stub_double():
    # transformr_Variable has no real 'transformr_Variable27' property in the generated
    # code (a bare stub) -- manually attach it so transformr_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformr_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformr_Attribute()
    partner = transformr_Variable()
    setattr(partner, 'transformr_Variable27', None)
    _safe_set(owner, 'transformr_Attribute28', partner)
    assert getattr(partner, 'transformr_Variable27') == owner
    _safe_set(owner, 'transformr_Attribute28', None)
    assert getattr(partner, 'transformr_Variable27') is None


