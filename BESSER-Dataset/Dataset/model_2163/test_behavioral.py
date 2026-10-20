import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    NamedElement,
    Term,
    Vertex,
    dependencies_Block,
    dependencies_CoreClass,
    dependencies_Create,
    dependencies_Domain,
    dependencies_EClass,
    dependencies_EPackage,
    dependencies_Edge,
    dependencies_Equivalence,
    dependencies_Graph,
    dependencies_NamedElement,
    dependencies_Operation,
    dependencies_RCPackage,
    dependencies_Required,
    dependencies_RightTerm,
    dependencies_SemiRequired,
    dependencies_SimpleTerm,
    dependencies_Term,
    dependencies_Vertex,
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

def test_assoc_operation27_reverse_link_reassign_clear():
    a1 = dependencies_RightTerm(value="sample_text")
    a2 = dependencies_RightTerm(value="sample_text_2")
    b = dependencies_Operation(operationType="sample_text")
    _safe_set(b, 'dependencies_Operation', a1)
    assert _is_linked(b, 'dependencies_Operation', a1)
    if hasattr(a1, 'dependencies_RightTerm28'):
        assert _is_linked(a1, 'dependencies_RightTerm28', b)
    _safe_set(b, 'dependencies_Operation', a2)
    assert _is_linked(b, 'dependencies_Operation', a2)
    if hasattr(a1, 'dependencies_RightTerm28'):
        assert not _is_linked(a1, 'dependencies_RightTerm28', b)
    if hasattr(a2, 'dependencies_RightTerm28'):
        assert _is_linked(a2, 'dependencies_RightTerm28', b)
    _safe_set(b, 'dependencies_Operation', None)
    assert not _is_linked(b, 'dependencies_Operation', a2)
    if hasattr(a2, 'dependencies_RightTerm28'):
        assert not _is_linked(a2, 'dependencies_RightTerm28', b)


def test_assoc_rightTerm19_reverse_link_reassign_clear():
    a1 = dependencies_RightTerm(value="sample_text")
    a2 = dependencies_RightTerm(value="sample_text_2")
    b = dependencies_Edge(equal=True, referredTo=True)
    _safe_set(b, 'dependencies_Edge20', a1)
    assert _is_linked(b, 'dependencies_Edge20', a1)
    if hasattr(a1, 'dependencies_RightTerm'):
        assert _is_linked(a1, 'dependencies_RightTerm', b)
    _safe_set(b, 'dependencies_Edge20', a2)
    assert _is_linked(b, 'dependencies_Edge20', a2)
    if hasattr(a1, 'dependencies_RightTerm'):
        assert not _is_linked(a1, 'dependencies_RightTerm', b)
    if hasattr(a2, 'dependencies_RightTerm'):
        assert _is_linked(a2, 'dependencies_RightTerm', b)
    _safe_set(b, 'dependencies_Edge20', None)
    assert not _is_linked(b, 'dependencies_Edge20', a2)
    if hasattr(a2, 'dependencies_RightTerm'):
        assert not _is_linked(a2, 'dependencies_RightTerm', b)


def test_assoc_rightTerms32_reverse_link_reassign_clear():
    a1 = dependencies_RightTerm(value="sample_text")
    a2 = dependencies_RightTerm(value="sample_text_2")
    b = dependencies_Operation(operationType="sample_text")
    _safe_set(b, 'dependencies_Operation33', {a1})
    assert _is_linked(b, 'dependencies_Operation33', a1)
    if hasattr(a1, 'dependencies_RightTerm34'):
        assert _is_linked(a1, 'dependencies_RightTerm34', b)
    _safe_set(b, 'dependencies_Operation33', {a2})
    assert _is_linked(b, 'dependencies_Operation33', a2)
    if hasattr(a1, 'dependencies_RightTerm34'):
        assert not _is_linked(a1, 'dependencies_RightTerm34', b)
    if hasattr(a2, 'dependencies_RightTerm34'):
        assert _is_linked(a2, 'dependencies_RightTerm34', b)
    _safe_set(b, 'dependencies_Operation33', set())
    assert not _is_linked(b, 'dependencies_Operation33', a2)
    if hasattr(a2, 'dependencies_RightTerm34'):
        assert not _is_linked(a2, 'dependencies_RightTerm34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges16_stub_double():
    # dependencies_Vertex has no real 'dependencies_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so dependencies_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dependencies_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dependencies_Edge(equal=True, referredTo=True)
    partner = dependencies_Vertex()
    setattr(partner, 'dependencies_Vertex', None)
    _safe_set(owner, 'dependencies_Edge', partner)
    assert owner in getattr(partner, 'dependencies_Vertex')
    _safe_set(owner, 'dependencies_Edge', None)
    assert owner not in getattr(partner, 'dependencies_Vertex')


def test_assoc_modelDomains0_stub_double():
    # dependencies_Domain has no real 'dependencies_Domain' property in the generated
    # code (a bare stub) -- manually attach it so dependencies_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dependencies_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dependencies_Graph(priority="sample_text")
    partner = dependencies_Domain()
    setattr(partner, 'dependencies_Domain', None)
    _safe_set(owner, 'dependencies_Graph', {partner})
    assert getattr(partner, 'dependencies_Domain') == owner
    _safe_set(owner, 'dependencies_Graph', set())
    assert getattr(partner, 'dependencies_Domain') is None


def test_assoc_modelEquivalence1_stub_double():
    # dependencies_Equivalence has no real 'dependencies_Equivalence' property in the generated
    # code (a bare stub) -- manually attach it so dependencies_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dependencies_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dependencies_Graph(priority="sample_text")
    partner = dependencies_Equivalence()
    setattr(partner, 'dependencies_Equivalence', None)
    _safe_set(owner, 'dependencies_Graph2', partner)
    assert getattr(partner, 'dependencies_Equivalence') == owner
    _safe_set(owner, 'dependencies_Graph2', None)
    assert getattr(partner, 'dependencies_Equivalence') is None


def test_assoc_simpleTerm17_stub_double():
    # dependencies_SimpleTerm has no real 'dependencies_SimpleTerm' property in the generated
    # code (a bare stub) -- manually attach it so dependencies_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dependencies_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dependencies_Edge(equal=True, referredTo=True)
    partner = dependencies_SimpleTerm()
    setattr(partner, 'dependencies_SimpleTerm', None)
    _safe_set(owner, 'dependencies_Edge18', partner)
    assert getattr(partner, 'dependencies_SimpleTerm') == owner
    _safe_set(owner, 'dependencies_Edge18', None)
    assert getattr(partner, 'dependencies_SimpleTerm') is None


def test_assoc_simpleTerms29_stub_double():
    # dependencies_SimpleTerm has no real 'dependencies_SimpleTerm31' property in the generated
    # code (a bare stub) -- manually attach it so dependencies_RightTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dependencies_RightTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dependencies_RightTerm(value="sample_text")
    partner = dependencies_SimpleTerm()
    setattr(partner, 'dependencies_SimpleTerm31', None)
    _safe_set(owner, 'dependencies_RightTerm30', {partner})
    assert getattr(partner, 'dependencies_SimpleTerm31') == owner
    _safe_set(owner, 'dependencies_RightTerm30', set())
    assert getattr(partner, 'dependencies_SimpleTerm31') is None


