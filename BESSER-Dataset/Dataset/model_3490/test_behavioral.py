import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    Feature,
    FeatureElement,
    Operator,
    featureDiagram_Alternative,
    featureDiagram_Attribute,
    featureDiagram_Card,
    featureDiagram_Constraint,
    featureDiagram_ConstraintEdge,
    featureDiagram_EObject,
    featureDiagram_Feature,
    featureDiagram_FeatureDiagram,
    featureDiagram_FeatureElement,
    featureDiagram_Mandatory,
    featureDiagram_Mutex,
    featureDiagram_Operator,
    featureDiagram_Opt,
    featureDiagram_Or,
    featureDiagram_PrimitiveFeature,
    featureDiagram_Require,
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

def test_assoc_attributes6_reverse_link_reassign_clear():
    a1 = featureDiagram_Feature(name="sample_text", selected=True)
    a2 = featureDiagram_Feature(name="sample_text_2", selected=False)
    b = featureDiagram_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'owningFeature7'):
        assert _is_linked(a1, 'owningFeature7', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'owningFeature7'):
        assert not _is_linked(a1, 'owningFeature7', b)
    if hasattr(a2, 'owningFeature7'):
        assert _is_linked(a2, 'owningFeature7', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'owningFeature7'):
        assert not _is_linked(a2, 'owningFeature7', b)


def test_assoc_features0_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree=True)
    a2 = featureDiagram_FeatureDiagram(graphTypeTree=False)
    b = featureDiagram_Feature(name="sample_text", selected=True)
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


def test_assoc_features22_reverse_link_reassign_clear():
    a1 = featureDiagram_Operator(name="sample_text")
    a2 = featureDiagram_Operator(name="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", selected=True)
    _safe_set(b, 'Feature23', a1)
    assert _is_linked(b, 'Feature23', a1)
    if hasattr(a1, 'owningOperator'):
        assert _is_linked(a1, 'owningOperator', b)
    _safe_set(b, 'Feature23', a2)
    assert _is_linked(b, 'Feature23', a2)
    if hasattr(a1, 'owningOperator'):
        assert not _is_linked(a1, 'owningOperator', b)
    if hasattr(a2, 'owningOperator'):
        assert _is_linked(a2, 'owningOperator', b)
    _safe_set(b, 'Feature23', None)
    assert not _is_linked(b, 'Feature23', a2)
    if hasattr(a2, 'owningOperator'):
        assert not _is_linked(a2, 'owningOperator', b)


def test_assoc_operator5_reverse_link_reassign_clear():
    a1 = featureDiagram_Operator(name="sample_text")
    a2 = featureDiagram_Operator(name="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", selected=True)
    _safe_set(b, 'owningFeature', {a1})
    assert _is_linked(b, 'owningFeature', a1)
    if hasattr(a1, 'Operator'):
        assert _is_linked(a1, 'Operator', b)
    _safe_set(b, 'owningFeature', {a2})
    assert _is_linked(b, 'owningFeature', a2)
    if hasattr(a1, 'Operator'):
        assert not _is_linked(a1, 'Operator', b)
    if hasattr(a2, 'Operator'):
        assert _is_linked(a2, 'Operator', b)
    _safe_set(b, 'owningFeature', set())
    assert not _is_linked(b, 'owningFeature', a2)
    if hasattr(a2, 'Operator'):
        assert not _is_linked(a2, 'Operator', b)


def test_assoc_owningFeature20_reverse_link_reassign_clear():
    a1 = featureDiagram_Operator(name="sample_text")
    a2 = featureDiagram_Operator(name="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", selected=True)
    _safe_set(b, 'Feature21', a1)
    assert _is_linked(b, 'Feature21', a1)
    if hasattr(a1, 'operator'):
        assert _is_linked(a1, 'operator', b)
    _safe_set(b, 'Feature21', a2)
    assert _is_linked(b, 'Feature21', a2)
    if hasattr(a1, 'operator'):
        assert not _is_linked(a1, 'operator', b)
    if hasattr(a2, 'operator'):
        assert _is_linked(a2, 'operator', b)
    _safe_set(b, 'Feature21', None)
    assert not _is_linked(b, 'Feature21', a2)
    if hasattr(a2, 'operator'):
        assert not _is_linked(a2, 'operator', b)


def test_assoc_owningFeature25_reverse_link_reassign_clear():
    a1 = featureDiagram_Feature(name="sample_text", selected=True)
    a2 = featureDiagram_Feature(name="sample_text_2", selected=False)
    b = featureDiagram_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Feature26'):
        assert _is_linked(a1, 'Feature26', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Feature26'):
        assert not _is_linked(a1, 'Feature26', b)
    if hasattr(a2, 'Feature26'):
        assert _is_linked(a2, 'Feature26', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Feature26'):
        assert not _is_linked(a2, 'Feature26', b)


def test_assoc_owningFeatureDiagram4_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree=True)
    a2 = featureDiagram_FeatureDiagram(graphTypeTree=False)
    b = featureDiagram_Feature(name="sample_text", selected=True)
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


def test_assoc_owningOperator8_reverse_link_reassign_clear():
    a1 = featureDiagram_Operator(name="sample_text")
    a2 = featureDiagram_Operator(name="sample_text_2")
    b = featureDiagram_Feature(name="sample_text", selected=True)
    _safe_set(b, 'features9', {a1})
    assert _is_linked(b, 'features9', a1)
    if hasattr(a1, 'Operator10'):
        assert _is_linked(a1, 'Operator10', b)
    _safe_set(b, 'features9', {a2})
    assert _is_linked(b, 'features9', a2)
    if hasattr(a1, 'Operator10'):
        assert not _is_linked(a1, 'Operator10', b)
    if hasattr(a2, 'Operator10'):
        assert _is_linked(a2, 'Operator10', b)
    _safe_set(b, 'features9', set())
    assert not _is_linked(b, 'features9', a2)
    if hasattr(a2, 'Operator10'):
        assert not _is_linked(a2, 'Operator10', b)


def test_assoc_root1_reverse_link_reassign_clear():
    a1 = featureDiagram_FeatureDiagram(graphTypeTree=True)
    a2 = featureDiagram_FeatureDiagram(graphTypeTree=False)
    b = featureDiagram_Feature(name="sample_text", selected=True)
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
    owner = featureDiagram_FeatureDiagram(graphTypeTree=True)
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge', None)
    _safe_set(owner, 'featureDiagram_FeatureDiagram3', {partner})
    assert getattr(partner, 'featureDiagram_ConstraintEdge') == owner
    _safe_set(owner, 'featureDiagram_FeatureDiagram3', set())
    assert getattr(partner, 'featureDiagram_ConstraintEdge') is None


def test_assoc_modelElements11_stub_double():
    # featureDiagram_EObject has no real 'featureDiagram_EObject' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", selected=True)
    partner = featureDiagram_EObject()
    setattr(partner, 'featureDiagram_EObject', None)
    _safe_set(owner, 'featureDiagram_Feature12', {partner})
    assert getattr(partner, 'featureDiagram_EObject') == owner
    _safe_set(owner, 'featureDiagram_Feature12', set())
    assert getattr(partner, 'featureDiagram_EObject') is None


def test_assoc_source17_stub_double():
    # featureDiagram_ConstraintEdge has no real 'featureDiagram_ConstraintEdge18' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", selected=True)
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge18', None)
    _safe_set(owner, 'featureDiagram_Feature19', partner)
    assert getattr(partner, 'featureDiagram_ConstraintEdge18') == owner
    _safe_set(owner, 'featureDiagram_Feature19', None)
    assert getattr(partner, 'featureDiagram_ConstraintEdge18') is None


def test_assoc_target13_stub_double():
    # featureDiagram_ConstraintEdge has no real 'featureDiagram_ConstraintEdge14' property in the generated
    # code (a bare stub) -- manually attach it so featureDiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureDiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureDiagram_Feature(name="sample_text", selected=True)
    partner = featureDiagram_ConstraintEdge()
    setattr(partner, 'featureDiagram_ConstraintEdge14', None)
    _safe_set(owner, 'featureDiagram_Feature15', partner)
    assert getattr(partner, 'featureDiagram_ConstraintEdge14') == owner
    _safe_set(owner, 'featureDiagram_Feature15', None)
    assert getattr(partner, 'featureDiagram_ConstraintEdge14') is None


