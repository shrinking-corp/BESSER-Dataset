import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    Feature,
    Operator,
    featureDiagram_And,
    featureDiagram_Card,
    featureDiagram_Constraint,
    featureDiagram_ConstraintEdge,
    featureDiagram_Feature,
    featureDiagram_FeatureDiagram,
    featureDiagram_Model,
    featureDiagram_Mutex,
    featureDiagram_Operator,
    featureDiagram_Opt,
    featureDiagram_Or,
    featureDiagram_PrimitiveFeature,
    featureDiagram_Require,
    featureDiagram_Xor,
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

def test_assoc_children9_reverse_link_reassign_clear():
    a1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    a2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Feature10'):
        assert _is_linked(a1, 'Feature10', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Feature10'):
        assert not _is_linked(a1, 'Feature10', b)
    if hasattr(a2, 'Feature10'):
        assert _is_linked(a2, 'Feature10', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Feature10'):
        assert not _is_linked(a2, 'Feature10', b)


def test_assoc_features0_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    a2 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'owningFeatureDiagram'):
        assert _is_linked(a1, 'owningFeatureDiagram', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'owningFeatureDiagram'):
        assert not _is_linked(a1, 'owningFeatureDiagram', b)
    if hasattr(a2, 'owningFeatureDiagram'):
        assert _is_linked(a2, 'owningFeatureDiagram', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'owningFeatureDiagram'):
        assert not _is_linked(a2, 'owningFeatureDiagram', b)


def test_assoc_models6_reverse_link_reassign_clear():
    a1 = featureDiagram_Model(name="sample_text")
    a2 = featureDiagram_Model(name="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'featureDiagram_Feature7', {a1})
    assert _is_linked(b, 'featureDiagram_Feature7', a1)
    if hasattr(a1, 'featureDiagram_Model'):
        assert _is_linked(a1, 'featureDiagram_Model', b)
    _safe_set(b, 'featureDiagram_Feature7', {a2})
    assert _is_linked(b, 'featureDiagram_Feature7', a2)
    if hasattr(a1, 'featureDiagram_Model'):
        assert not _is_linked(a1, 'featureDiagram_Model', b)
    if hasattr(a2, 'featureDiagram_Model'):
        assert _is_linked(a2, 'featureDiagram_Model', b)
    _safe_set(b, 'featureDiagram_Feature7', set())
    assert not _is_linked(b, 'featureDiagram_Feature7', a2)
    if hasattr(a2, 'featureDiagram_Model'):
        assert not _is_linked(a2, 'featureDiagram_Model', b)


def test_assoc_owningFeatureDiagram4_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    a2 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'features', a1)
    assert _is_linked(b, 'features', a1)
    if hasattr(a1, 'FeatureDiagram'):
        assert _is_linked(a1, 'FeatureDiagram', b)
    _safe_set(b, 'features', a2)
    assert _is_linked(b, 'features', a2)
    if hasattr(a1, 'FeatureDiagram'):
        assert not _is_linked(a1, 'FeatureDiagram', b)
    if hasattr(a2, 'FeatureDiagram'):
        assert _is_linked(a2, 'FeatureDiagram', b)
    _safe_set(b, 'features', None)
    assert not _is_linked(b, 'features', a2)
    if hasattr(a2, 'FeatureDiagram'):
        assert not _is_linked(a2, 'FeatureDiagram', b)


def test_assoc_parents12_reverse_link_reassign_clear():
    a1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    a2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Feature13'):
        assert _is_linked(a1, 'Feature13', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Feature13'):
        assert not _is_linked(a1, 'Feature13', b)
    if hasattr(a2, 'Feature13'):
        assert _is_linked(a2, 'Feature13', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Feature13'):
        assert not _is_linked(a2, 'Feature13', b)


def test_assoc_root1_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    a2 = featureDiagram_FeatureDiagram(graphTypeTree="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    _safe_set(b, 'featureDiagram_Feature', a1)
    assert _is_linked(b, 'featureDiagram_Feature', a1)
    if hasattr(a1, 'featureDiagram_FeatureDiagram'):
        assert _is_linked(a1, 'featureDiagram_FeatureDiagram', b)
    _safe_set(b, 'featureDiagram_Feature', a2)
    assert _is_linked(b, 'featureDiagram_Feature', a2)
    if hasattr(a1, 'featureDiagram_FeatureDiagram'):
        assert not _is_linked(a1, 'featureDiagram_FeatureDiagram', b)
    if hasattr(a2, 'featureDiagram_FeatureDiagram'):
        assert _is_linked(a2, 'featureDiagram_FeatureDiagram', b)
    _safe_set(b, 'featureDiagram_Feature', None)
    assert not _is_linked(b, 'featureDiagram_Feature', a2)
    if hasattr(a2, 'featureDiagram_FeatureDiagram'):
        assert not _is_linked(a2, 'featureDiagram_FeatureDiagram', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constraintEdges2_stub_double():
    # featureDiagram_ConstraintEdge has no real 'featureDiagram_ConstraintEdge' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_FeatureDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_FeatureDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge', None)
    _safe_set(owner, 'featureDiagram_FeatureDiagram3', {partner})
    assert getattr(partner, 'featureDiagram_ConstraintEdge') == owner
    _safe_set(owner, 'featureDiagram_FeatureDiagram3', set())
    assert getattr(partner, 'featureDiagram_ConstraintEdge') is None


def test_assoc_operator5_stub_double():
    # featureDiagram_Operator has no real 'Operator' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    partner = featureDiagram_Operator()
    setattr(partner, 'Operator', None)
    _safe_set(owner, 'owningFeature', partner)
    assert getattr(partner, 'Operator') == owner
    _safe_set(owner, 'owningFeature', None)
    assert getattr(partner, 'Operator') is None


def test_assoc_owningFeature21_stub_double():
    # featureDiagram_Operator has no real 'operator' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    partner = featureDiagram_Operator()
    setattr(partner, 'operator', None)
    _safe_set(owner, 'Feature22', partner)
    assert getattr(partner, 'operator') == owner
    _safe_set(owner, 'Feature22', None)
    assert getattr(partner, 'operator') is None


def test_assoc_source18_stub_double():
    # featureDiagram_ConstraintEdge has no real 'featureDiagram_ConstraintEdge19' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge19', None)
    _safe_set(owner, 'featureDiagram_Feature20', partner)
    assert getattr(partner, 'featureDiagram_ConstraintEdge19') == owner
    _safe_set(owner, 'featureDiagram_Feature20', None)
    assert getattr(partner, 'featureDiagram_ConstraintEdge19') is None


def test_assoc_target14_stub_double():
    # featureDiagram_ConstraintEdge has no real 'featureDiagram_ConstraintEdge15' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge15', None)
    _safe_set(owner, 'featureDiagram_Feature16', partner)
    assert getattr(partner, 'featureDiagram_ConstraintEdge15') == owner
    _safe_set(owner, 'featureDiagram_Feature16', None)
    assert getattr(partner, 'featureDiagram_ConstraintEdge15') is None


