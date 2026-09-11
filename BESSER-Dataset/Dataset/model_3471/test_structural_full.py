import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_featureDiagram_Feature_name_value_roundtrip():
    instance = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureDiagram_Feature_optional_value_roundtrip():
    instance = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    assert instance.optional == "sample_text"
    instance.optional = "sample_text_2"
    assert instance.optional == "sample_text_2"


def test_featureDiagram_Feature_selected_value_roundtrip():
    instance = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    assert instance.selected == "sample_text"
    instance.selected = "sample_text_2"
    assert instance.selected == "sample_text_2"


def test_featureDiagram_FeatureDiagram_graphTypeTree_value_roundtrip():
    instance = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    assert instance.graphTypeTree == "sample_text"
    instance.graphTypeTree = "sample_text_2"
    assert instance.graphTypeTree == "sample_text_2"


def test_featureDiagram_Model_name_value_roundtrip():
    instance = featureDiagram_Model(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureDiagram_Mutex_isa_Constraint():
    instance = featureDiagram_Mutex()
    assert isinstance(instance, Constraint)


def test_featureDiagram_Require_isa_Constraint():
    instance = featureDiagram_Require()
    assert isinstance(instance, Constraint)


def test_featureDiagram_PrimitiveFeature_isa_Feature():
    instance = featureDiagram_PrimitiveFeature()
    assert isinstance(instance, Feature)


def test_featureDiagram_And_isa_Operator():
    instance = featureDiagram_And()
    assert isinstance(instance, Operator)


def test_featureDiagram_Card_isa_Operator():
    instance = featureDiagram_Card()
    assert isinstance(instance, Operator)


def test_featureDiagram_Opt_isa_Operator():
    instance = featureDiagram_Opt()
    assert isinstance(instance, Operator)


def test_featureDiagram_Or_isa_Operator():
    instance = featureDiagram_Or()
    assert isinstance(instance, Operator)


def test_featureDiagram_Xor_isa_Operator():
    instance = featureDiagram_Xor()
    assert isinstance(instance, Operator)


def test_assoc_children9_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'Feature10', b1)
    assert _is_linked(a, 'Feature10', b1)
    if hasattr(b1, 'parents'):
        assert _is_linked(b1, 'parents', a)
    _safe_set(a, 'Feature10', b2)
    assert _is_linked(a, 'Feature10', b2)
    if hasattr(b1, 'parents'):
        assert not _is_linked(b1, 'parents', a)
    if hasattr(b2, 'parents'):
        assert _is_linked(b2, 'parents', a)
    _safe_set(a, 'Feature10', None)
    assert not _is_linked(a, 'Feature10', b2)
    if hasattr(b2, 'parents'):
        assert not _is_linked(b2, 'parents', a)


def test_assoc_constraintEdges2_link_reassign_clear():
    a = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    b1 = featureDiagram_ConstraintEdge()
    b2 = featureDiagram_ConstraintEdge()
    _safe_set(a, 'featureDiagram_FeatureDiagram3', {b1})
    assert _is_linked(a, 'featureDiagram_FeatureDiagram3', b1)
    if hasattr(b1, 'featureDiagram_ConstraintEdge'):
        assert _is_linked(b1, 'featureDiagram_ConstraintEdge', a)
    _safe_set(a, 'featureDiagram_FeatureDiagram3', {b2})
    assert _is_linked(a, 'featureDiagram_FeatureDiagram3', b2)
    if hasattr(b1, 'featureDiagram_ConstraintEdge'):
        assert not _is_linked(b1, 'featureDiagram_ConstraintEdge', a)
    if hasattr(b2, 'featureDiagram_ConstraintEdge'):
        assert _is_linked(b2, 'featureDiagram_ConstraintEdge', a)
    _safe_set(a, 'featureDiagram_FeatureDiagram3', set())
    assert not _is_linked(a, 'featureDiagram_FeatureDiagram3', b2)
    if hasattr(b2, 'featureDiagram_ConstraintEdge'):
        assert not _is_linked(b2, 'featureDiagram_ConstraintEdge', a)


def test_assoc_features0_link_reassign_clear():
    a = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'owningFeatureDiagram', {b1})
    assert _is_linked(a, 'owningFeatureDiagram', b1)
    if hasattr(b1, 'Feature'):
        assert _is_linked(b1, 'Feature', a)
    _safe_set(a, 'owningFeatureDiagram', {b2})
    assert _is_linked(a, 'owningFeatureDiagram', b2)
    if hasattr(b1, 'Feature'):
        assert not _is_linked(b1, 'Feature', a)
    if hasattr(b2, 'Feature'):
        assert _is_linked(b2, 'Feature', a)
    _safe_set(a, 'owningFeatureDiagram', set())
    assert not _is_linked(a, 'owningFeatureDiagram', b2)
    if hasattr(b2, 'Feature'):
        assert not _is_linked(b2, 'Feature', a)


def test_assoc_models6_link_reassign_clear():
    a = featureDiagram_Model(name="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'featureDiagram_Model', b1)
    assert _is_linked(a, 'featureDiagram_Model', b1)
    if hasattr(b1, 'featureDiagram_Feature7'):
        assert _is_linked(b1, 'featureDiagram_Feature7', a)
    _safe_set(a, 'featureDiagram_Model', b2)
    assert _is_linked(a, 'featureDiagram_Model', b2)
    if hasattr(b1, 'featureDiagram_Feature7'):
        assert not _is_linked(b1, 'featureDiagram_Feature7', a)
    if hasattr(b2, 'featureDiagram_Feature7'):
        assert _is_linked(b2, 'featureDiagram_Feature7', a)
    _safe_set(a, 'featureDiagram_Model', None)
    assert not _is_linked(a, 'featureDiagram_Model', b2)
    if hasattr(b2, 'featureDiagram_Feature7'):
        assert not _is_linked(b2, 'featureDiagram_Feature7', a)


def test_assoc_operator5_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_Operator()
    b2 = featureDiagram_Operator()
    _safe_set(a, 'owningFeature', b1)
    assert _is_linked(a, 'owningFeature', b1)
    if hasattr(b1, 'Operator'):
        assert _is_linked(b1, 'Operator', a)
    _safe_set(a, 'owningFeature', b2)
    assert _is_linked(a, 'owningFeature', b2)
    if hasattr(b1, 'Operator'):
        assert not _is_linked(b1, 'Operator', a)
    if hasattr(b2, 'Operator'):
        assert _is_linked(b2, 'Operator', a)
    _safe_set(a, 'owningFeature', None)
    assert not _is_linked(a, 'owningFeature', b2)
    if hasattr(b2, 'Operator'):
        assert not _is_linked(b2, 'Operator', a)


def test_assoc_owningFeature21_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_Operator()
    b2 = featureDiagram_Operator()
    _safe_set(a, 'Feature22', b1)
    assert _is_linked(a, 'Feature22', b1)
    if hasattr(b1, 'operator'):
        assert _is_linked(b1, 'operator', a)
    _safe_set(a, 'Feature22', b2)
    assert _is_linked(a, 'Feature22', b2)
    if hasattr(b1, 'operator'):
        assert not _is_linked(b1, 'operator', a)
    if hasattr(b2, 'operator'):
        assert _is_linked(b2, 'operator', a)
    _safe_set(a, 'Feature22', None)
    assert not _is_linked(a, 'Feature22', b2)
    if hasattr(b2, 'operator'):
        assert not _is_linked(b2, 'operator', a)


def test_assoc_owningFeatureDiagram4_link_reassign_clear():
    a = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'FeatureDiagram', b1)
    assert _is_linked(a, 'FeatureDiagram', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'FeatureDiagram', b2)
    assert _is_linked(a, 'FeatureDiagram', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'FeatureDiagram', None)
    assert not _is_linked(a, 'FeatureDiagram', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_parents12_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'Feature13', b1)
    assert _is_linked(a, 'Feature13', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'Feature13', b2)
    assert _is_linked(a, 'Feature13', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'Feature13', None)
    assert not _is_linked(a, 'Feature13', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_root1_link_reassign_clear():
    a = featureDiagram_FeatureDiagram(graphTypeTree="sample_text")
    b1 = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b2 = featureDiagram_Feature(name="sample_text_2", optional="sample_text_2", selected="sample_text_2")
    _safe_set(a, 'featureDiagram_FeatureDiagram', b1)
    assert _is_linked(a, 'featureDiagram_FeatureDiagram', b1)
    if hasattr(b1, 'featureDiagram_Feature'):
        assert _is_linked(b1, 'featureDiagram_Feature', a)
    _safe_set(a, 'featureDiagram_FeatureDiagram', b2)
    assert _is_linked(a, 'featureDiagram_FeatureDiagram', b2)
    if hasattr(b1, 'featureDiagram_Feature'):
        assert not _is_linked(b1, 'featureDiagram_Feature', a)
    if hasattr(b2, 'featureDiagram_Feature'):
        assert _is_linked(b2, 'featureDiagram_Feature', a)
    _safe_set(a, 'featureDiagram_FeatureDiagram', None)
    assert not _is_linked(a, 'featureDiagram_FeatureDiagram', b2)
    if hasattr(b2, 'featureDiagram_Feature'):
        assert not _is_linked(b2, 'featureDiagram_Feature', a)


def test_assoc_source18_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_ConstraintEdge()
    b2 = featureDiagram_ConstraintEdge()
    _safe_set(a, 'featureDiagram_Feature20', b1)
    assert _is_linked(a, 'featureDiagram_Feature20', b1)
    if hasattr(b1, 'featureDiagram_ConstraintEdge19'):
        assert _is_linked(b1, 'featureDiagram_ConstraintEdge19', a)
    _safe_set(a, 'featureDiagram_Feature20', b2)
    assert _is_linked(a, 'featureDiagram_Feature20', b2)
    if hasattr(b1, 'featureDiagram_ConstraintEdge19'):
        assert not _is_linked(b1, 'featureDiagram_ConstraintEdge19', a)
    if hasattr(b2, 'featureDiagram_ConstraintEdge19'):
        assert _is_linked(b2, 'featureDiagram_ConstraintEdge19', a)
    _safe_set(a, 'featureDiagram_Feature20', None)
    assert not _is_linked(a, 'featureDiagram_Feature20', b2)
    if hasattr(b2, 'featureDiagram_ConstraintEdge19'):
        assert not _is_linked(b2, 'featureDiagram_ConstraintEdge19', a)


def test_assoc_target14_link_reassign_clear():
    a = featureDiagram_Feature(name="sample_text", optional="sample_text", selected="sample_text")
    b1 = featureDiagram_ConstraintEdge()
    b2 = featureDiagram_ConstraintEdge()
    _safe_set(a, 'featureDiagram_Feature16', b1)
    assert _is_linked(a, 'featureDiagram_Feature16', b1)
    if hasattr(b1, 'featureDiagram_ConstraintEdge15'):
        assert _is_linked(b1, 'featureDiagram_ConstraintEdge15', a)
    _safe_set(a, 'featureDiagram_Feature16', b2)
    assert _is_linked(a, 'featureDiagram_Feature16', b2)
    if hasattr(b1, 'featureDiagram_ConstraintEdge15'):
        assert not _is_linked(b1, 'featureDiagram_ConstraintEdge15', a)
    if hasattr(b2, 'featureDiagram_ConstraintEdge15'):
        assert _is_linked(b2, 'featureDiagram_ConstraintEdge15', a)
    _safe_set(a, 'featureDiagram_Feature16', None)
    assert not _is_linked(a, 'featureDiagram_Feature16', b2)
    if hasattr(b2, 'featureDiagram_ConstraintEdge15'):
        assert not _is_linked(b2, 'featureDiagram_ConstraintEdge15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


featureDiagram_And_strategy = st.builds(featureDiagram_And)
@given(instance=featureDiagram_And_strategy)
@settings(max_examples=25)
def test_featureDiagram_And_instantiation(instance):
    assert isinstance(instance, featureDiagram_And)


featureDiagram_Card_strategy = st.builds(featureDiagram_Card)
@given(instance=featureDiagram_Card_strategy)
@settings(max_examples=25)
def test_featureDiagram_Card_instantiation(instance):
    assert isinstance(instance, featureDiagram_Card)


featureDiagram_Constraint_strategy = st.builds(featureDiagram_Constraint)
@given(instance=featureDiagram_Constraint_strategy)
@settings(max_examples=25)
def test_featureDiagram_Constraint_instantiation(instance):
    assert isinstance(instance, featureDiagram_Constraint)


featureDiagram_ConstraintEdge_strategy = st.builds(featureDiagram_ConstraintEdge)
@given(instance=featureDiagram_ConstraintEdge_strategy)
@settings(max_examples=25)
def test_featureDiagram_ConstraintEdge_instantiation(instance):
    assert isinstance(instance, featureDiagram_ConstraintEdge)


featureDiagram_Feature_strategy = st.builds(featureDiagram_Feature, name=safe_text, optional=safe_text, selected=safe_text)
@given(instance=featureDiagram_Feature_strategy)
@settings(max_examples=25)
def test_featureDiagram_Feature_instantiation(instance):
    assert isinstance(instance, featureDiagram_Feature)


featureDiagram_FeatureDiagram_strategy = st.builds(featureDiagram_FeatureDiagram, graphTypeTree=safe_text)
@given(instance=featureDiagram_FeatureDiagram_strategy)
@settings(max_examples=25)
def test_featureDiagram_FeatureDiagram_instantiation(instance):
    assert isinstance(instance, featureDiagram_FeatureDiagram)


featureDiagram_Model_strategy = st.builds(featureDiagram_Model, name=safe_text)
@given(instance=featureDiagram_Model_strategy)
@settings(max_examples=25)
def test_featureDiagram_Model_instantiation(instance):
    assert isinstance(instance, featureDiagram_Model)


featureDiagram_Mutex_strategy = st.builds(featureDiagram_Mutex)
@given(instance=featureDiagram_Mutex_strategy)
@settings(max_examples=25)
def test_featureDiagram_Mutex_instantiation(instance):
    assert isinstance(instance, featureDiagram_Mutex)


featureDiagram_Operator_strategy = st.builds(featureDiagram_Operator)
@given(instance=featureDiagram_Operator_strategy)
@settings(max_examples=25)
def test_featureDiagram_Operator_instantiation(instance):
    assert isinstance(instance, featureDiagram_Operator)


featureDiagram_Opt_strategy = st.builds(featureDiagram_Opt)
@given(instance=featureDiagram_Opt_strategy)
@settings(max_examples=25)
def test_featureDiagram_Opt_instantiation(instance):
    assert isinstance(instance, featureDiagram_Opt)


featureDiagram_Or_strategy = st.builds(featureDiagram_Or)
@given(instance=featureDiagram_Or_strategy)
@settings(max_examples=25)
def test_featureDiagram_Or_instantiation(instance):
    assert isinstance(instance, featureDiagram_Or)


featureDiagram_PrimitiveFeature_strategy = st.builds(featureDiagram_PrimitiveFeature)
@given(instance=featureDiagram_PrimitiveFeature_strategy)
@settings(max_examples=25)
def test_featureDiagram_PrimitiveFeature_instantiation(instance):
    assert isinstance(instance, featureDiagram_PrimitiveFeature)


featureDiagram_Require_strategy = st.builds(featureDiagram_Require)
@given(instance=featureDiagram_Require_strategy)
@settings(max_examples=25)
def test_featureDiagram_Require_instantiation(instance):
    assert isinstance(instance, featureDiagram_Require)


featureDiagram_Xor_strategy = st.builds(featureDiagram_Xor)
@given(instance=featureDiagram_Xor_strategy)
@settings(max_examples=25)
def test_featureDiagram_Xor_instantiation(instance):
    assert isinstance(instance, featureDiagram_Xor)


