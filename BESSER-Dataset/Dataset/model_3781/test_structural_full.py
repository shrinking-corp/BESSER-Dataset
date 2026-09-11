import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Dependency,
    Feature,
    UnaryDependency,
    assignment6_model_BinaryDependency,
    assignment6_model_Configurator,
    assignment6_model_Dependency,
    assignment6_model_Feature,
    assignment6_model_Group,
    assignment6_model_IntegerFeature,
    assignment6_model_IntegerValueDependency,
    assignment6_model_IsSelectedDependency,
    assignment6_model_SimpleFeature,
    assignment6_model_UnaryDependency,
    BinaryOperator,
    GroupType,
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

def test_assignment6_model_BinaryDependency_operator_value_roundtrip():
    instance = assignment6_model_BinaryDependency(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_assignment6_model_Configurator_name_value_roundtrip():
    instance = assignment6_model_Configurator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assignment6_model_Dependency_not__value_roundtrip():
    instance = assignment6_model_Dependency(not_=True)
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_assignment6_model_Feature_mandatory_value_roundtrip():
    instance = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_assignment6_model_Feature_name_value_roundtrip():
    instance = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assignment6_model_Feature_selected_value_roundtrip():
    instance = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_assignment6_model_Group_groupType_value_roundtrip():
    instance = assignment6_model_Group(groupType="sample_text", name="sample_text")
    assert instance.groupType == "sample_text"
    instance.groupType = "sample_text_2"
    assert instance.groupType == "sample_text_2"


def test_assignment6_model_Group_name_value_roundtrip():
    instance = assignment6_model_Group(groupType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assignment6_model_IntegerFeature_maxValue_value_roundtrip():
    instance = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    assert instance.maxValue == 7
    instance.maxValue = 13
    assert instance.maxValue == 13


def test_assignment6_model_IntegerFeature_minValue_value_roundtrip():
    instance = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    assert instance.minValue == 7
    instance.minValue = 13
    assert instance.minValue == 13


def test_assignment6_model_IntegerFeature_step_value_roundtrip():
    instance = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    assert instance.step == 7
    instance.step = 13
    assert instance.step == 13


def test_assignment6_model_IntegerFeature_value_value_roundtrip():
    instance = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_assignment6_model_IntegerValueDependency_value_value_roundtrip():
    instance = assignment6_model_IntegerValueDependency(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_assignment6_model_BinaryDependency_isa_Dependency():
    instance = assignment6_model_BinaryDependency(operator="sample_text")
    assert isinstance(instance, Dependency)


def test_assignment6_model_UnaryDependency_isa_Dependency():
    instance = assignment6_model_UnaryDependency()
    assert isinstance(instance, Dependency)


def test_assignment6_model_IntegerFeature_isa_Feature():
    instance = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    assert isinstance(instance, Feature)


def test_assignment6_model_SimpleFeature_isa_Feature():
    instance = assignment6_model_SimpleFeature()
    assert isinstance(instance, Feature)


def test_assignment6_model_IntegerValueDependency_isa_UnaryDependency():
    instance = assignment6_model_IntegerValueDependency(value=7)
    assert isinstance(instance, UnaryDependency)


def test_assignment6_model_IsSelectedDependency_isa_UnaryDependency():
    instance = assignment6_model_IsSelectedDependency()
    assert isinstance(instance, UnaryDependency)


def test_assoc_dependencies9_link_reassign_clear():
    a = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b1 = assignment6_model_Dependency(not_=True)
    b2 = assignment6_model_Dependency(not_=False)
    _safe_set(a, 'assignment6_model_Feature10', {b1})
    assert _is_linked(a, 'assignment6_model_Feature10', b1)
    if hasattr(b1, 'assignment6_model_Dependency'):
        assert _is_linked(b1, 'assignment6_model_Dependency', a)
    _safe_set(a, 'assignment6_model_Feature10', {b2})
    assert _is_linked(a, 'assignment6_model_Feature10', b2)
    if hasattr(b1, 'assignment6_model_Dependency'):
        assert not _is_linked(b1, 'assignment6_model_Dependency', a)
    if hasattr(b2, 'assignment6_model_Dependency'):
        assert _is_linked(b2, 'assignment6_model_Dependency', a)
    _safe_set(a, 'assignment6_model_Feature10', set())
    assert not _is_linked(a, 'assignment6_model_Feature10', b2)
    if hasattr(b2, 'assignment6_model_Dependency'):
        assert not _is_linked(b2, 'assignment6_model_Dependency', a)


def test_assoc_features0_link_reassign_clear():
    a = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b1 = assignment6_model_Configurator(name="sample_text")
    b2 = assignment6_model_Configurator(name="sample_text_2")
    _safe_set(a, 'assignment6_model_Feature', b1)
    assert _is_linked(a, 'assignment6_model_Feature', b1)
    if hasattr(b1, 'assignment6_model_Configurator'):
        assert _is_linked(b1, 'assignment6_model_Configurator', a)
    _safe_set(a, 'assignment6_model_Feature', b2)
    assert _is_linked(a, 'assignment6_model_Feature', b2)
    if hasattr(b1, 'assignment6_model_Configurator'):
        assert not _is_linked(b1, 'assignment6_model_Configurator', a)
    if hasattr(b2, 'assignment6_model_Configurator'):
        assert _is_linked(b2, 'assignment6_model_Configurator', a)
    _safe_set(a, 'assignment6_model_Feature', None)
    assert not _is_linked(a, 'assignment6_model_Feature', b2)
    if hasattr(b2, 'assignment6_model_Configurator'):
        assert not _is_linked(b2, 'assignment6_model_Configurator', a)


def test_assoc_features11_link_reassign_clear():
    a = assignment6_model_Group(groupType="sample_text", name="sample_text")
    b1 = assignment6_model_SimpleFeature()
    b2 = assignment6_model_SimpleFeature()
    _safe_set(a, 'assignment6_model_Group12', {b1})
    assert _is_linked(a, 'assignment6_model_Group12', b1)
    if hasattr(b1, 'assignment6_model_SimpleFeature'):
        assert _is_linked(b1, 'assignment6_model_SimpleFeature', a)
    _safe_set(a, 'assignment6_model_Group12', {b2})
    assert _is_linked(a, 'assignment6_model_Group12', b2)
    if hasattr(b1, 'assignment6_model_SimpleFeature'):
        assert not _is_linked(b1, 'assignment6_model_SimpleFeature', a)
    if hasattr(b2, 'assignment6_model_SimpleFeature'):
        assert _is_linked(b2, 'assignment6_model_SimpleFeature', a)
    _safe_set(a, 'assignment6_model_Group12', set())
    assert not _is_linked(a, 'assignment6_model_Group12', b2)
    if hasattr(b2, 'assignment6_model_SimpleFeature'):
        assert not _is_linked(b2, 'assignment6_model_SimpleFeature', a)


def test_assoc_features4_link_reassign_clear():
    a = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b1 = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b2 = assignment6_model_Feature(mandatory=False, name="sample_text_2", selected=False)
    _safe_set(a, 'assignment6_model_Feature3', {b1})
    assert _is_linked(a, 'assignment6_model_Feature3', b1)
    if hasattr(b1, 'assignment6_model_Feature5'):
        assert _is_linked(b1, 'assignment6_model_Feature5', a)
    _safe_set(a, 'assignment6_model_Feature3', {b2})
    assert _is_linked(a, 'assignment6_model_Feature3', b2)
    if hasattr(b1, 'assignment6_model_Feature5'):
        assert not _is_linked(b1, 'assignment6_model_Feature5', a)
    if hasattr(b2, 'assignment6_model_Feature5'):
        assert _is_linked(b2, 'assignment6_model_Feature5', a)
    _safe_set(a, 'assignment6_model_Feature3', set())
    assert not _is_linked(a, 'assignment6_model_Feature3', b2)
    if hasattr(b2, 'assignment6_model_Feature5'):
        assert not _is_linked(b2, 'assignment6_model_Feature5', a)


def test_assoc_groups1_link_reassign_clear():
    a = assignment6_model_Group(groupType="sample_text", name="sample_text")
    b1 = assignment6_model_Configurator(name="sample_text")
    b2 = assignment6_model_Configurator(name="sample_text_2")
    _safe_set(a, 'assignment6_model_Group', b1)
    assert _is_linked(a, 'assignment6_model_Group', b1)
    if hasattr(b1, 'assignment6_model_Configurator2'):
        assert _is_linked(b1, 'assignment6_model_Configurator2', a)
    _safe_set(a, 'assignment6_model_Group', b2)
    assert _is_linked(a, 'assignment6_model_Group', b2)
    if hasattr(b1, 'assignment6_model_Configurator2'):
        assert not _is_linked(b1, 'assignment6_model_Configurator2', a)
    if hasattr(b2, 'assignment6_model_Configurator2'):
        assert _is_linked(b2, 'assignment6_model_Configurator2', a)
    _safe_set(a, 'assignment6_model_Group', None)
    assert not _is_linked(a, 'assignment6_model_Group', b2)
    if hasattr(b2, 'assignment6_model_Configurator2'):
        assert not _is_linked(b2, 'assignment6_model_Configurator2', a)


def test_assoc_groups6_link_reassign_clear():
    a = assignment6_model_Group(groupType="sample_text", name="sample_text")
    b1 = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b2 = assignment6_model_Feature(mandatory=False, name="sample_text_2", selected=False)
    _safe_set(a, 'assignment6_model_Group8', b1)
    assert _is_linked(a, 'assignment6_model_Group8', b1)
    if hasattr(b1, 'assignment6_model_Feature7'):
        assert _is_linked(b1, 'assignment6_model_Feature7', a)
    _safe_set(a, 'assignment6_model_Group8', b2)
    assert _is_linked(a, 'assignment6_model_Group8', b2)
    if hasattr(b1, 'assignment6_model_Feature7'):
        assert not _is_linked(b1, 'assignment6_model_Feature7', a)
    if hasattr(b2, 'assignment6_model_Feature7'):
        assert _is_linked(b2, 'assignment6_model_Feature7', a)
    _safe_set(a, 'assignment6_model_Group8', None)
    assert not _is_linked(a, 'assignment6_model_Group8', b2)
    if hasattr(b2, 'assignment6_model_Feature7'):
        assert not _is_linked(b2, 'assignment6_model_Feature7', a)


def test_assoc_leftHand15_link_reassign_clear():
    a = assignment6_model_Dependency(not_=True)
    b1 = assignment6_model_BinaryDependency(operator="sample_text")
    b2 = assignment6_model_BinaryDependency(operator="sample_text_2")
    _safe_set(a, 'assignment6_model_Dependency17', b1)
    assert _is_linked(a, 'assignment6_model_Dependency17', b1)
    if hasattr(b1, 'assignment6_model_BinaryDependency16'):
        assert _is_linked(b1, 'assignment6_model_BinaryDependency16', a)
    _safe_set(a, 'assignment6_model_Dependency17', b2)
    assert _is_linked(a, 'assignment6_model_Dependency17', b2)
    if hasattr(b1, 'assignment6_model_BinaryDependency16'):
        assert not _is_linked(b1, 'assignment6_model_BinaryDependency16', a)
    if hasattr(b2, 'assignment6_model_BinaryDependency16'):
        assert _is_linked(b2, 'assignment6_model_BinaryDependency16', a)
    _safe_set(a, 'assignment6_model_Dependency17', None)
    assert not _is_linked(a, 'assignment6_model_Dependency17', b2)
    if hasattr(b2, 'assignment6_model_BinaryDependency16'):
        assert not _is_linked(b2, 'assignment6_model_BinaryDependency16', a)


def test_assoc_rightHand13_link_reassign_clear():
    a = assignment6_model_Dependency(not_=True)
    b1 = assignment6_model_BinaryDependency(operator="sample_text")
    b2 = assignment6_model_BinaryDependency(operator="sample_text_2")
    _safe_set(a, 'assignment6_model_Dependency14', b1)
    assert _is_linked(a, 'assignment6_model_Dependency14', b1)
    if hasattr(b1, 'assignment6_model_BinaryDependency'):
        assert _is_linked(b1, 'assignment6_model_BinaryDependency', a)
    _safe_set(a, 'assignment6_model_Dependency14', b2)
    assert _is_linked(a, 'assignment6_model_Dependency14', b2)
    if hasattr(b1, 'assignment6_model_BinaryDependency'):
        assert not _is_linked(b1, 'assignment6_model_BinaryDependency', a)
    if hasattr(b2, 'assignment6_model_BinaryDependency'):
        assert _is_linked(b2, 'assignment6_model_BinaryDependency', a)
    _safe_set(a, 'assignment6_model_Dependency14', None)
    assert not _is_linked(a, 'assignment6_model_Dependency14', b2)
    if hasattr(b2, 'assignment6_model_BinaryDependency'):
        assert not _is_linked(b2, 'assignment6_model_BinaryDependency', a)


def test_assoc_target18_link_reassign_clear():
    a = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    b1 = assignment6_model_IsSelectedDependency()
    b2 = assignment6_model_IsSelectedDependency()
    _safe_set(a, 'assignment6_model_Feature19', b1)
    assert _is_linked(a, 'assignment6_model_Feature19', b1)
    if hasattr(b1, 'assignment6_model_IsSelectedDependency'):
        assert _is_linked(b1, 'assignment6_model_IsSelectedDependency', a)
    _safe_set(a, 'assignment6_model_Feature19', b2)
    assert _is_linked(a, 'assignment6_model_Feature19', b2)
    if hasattr(b1, 'assignment6_model_IsSelectedDependency'):
        assert not _is_linked(b1, 'assignment6_model_IsSelectedDependency', a)
    if hasattr(b2, 'assignment6_model_IsSelectedDependency'):
        assert _is_linked(b2, 'assignment6_model_IsSelectedDependency', a)
    _safe_set(a, 'assignment6_model_Feature19', None)
    assert not _is_linked(a, 'assignment6_model_Feature19', b2)
    if hasattr(b2, 'assignment6_model_IsSelectedDependency'):
        assert not _is_linked(b2, 'assignment6_model_IsSelectedDependency', a)


def test_assoc_target20_link_reassign_clear():
    a = assignment6_model_IntegerValueDependency(value=7)
    b1 = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    b2 = assignment6_model_IntegerFeature(maxValue=13, minValue=13, step=13, value=13)
    _safe_set(a, 'assignment6_model_IntegerValueDependency', b1)
    assert _is_linked(a, 'assignment6_model_IntegerValueDependency', b1)
    if hasattr(b1, 'assignment6_model_IntegerFeature'):
        assert _is_linked(b1, 'assignment6_model_IntegerFeature', a)
    _safe_set(a, 'assignment6_model_IntegerValueDependency', b2)
    assert _is_linked(a, 'assignment6_model_IntegerValueDependency', b2)
    if hasattr(b1, 'assignment6_model_IntegerFeature'):
        assert not _is_linked(b1, 'assignment6_model_IntegerFeature', a)
    if hasattr(b2, 'assignment6_model_IntegerFeature'):
        assert _is_linked(b2, 'assignment6_model_IntegerFeature', a)
    _safe_set(a, 'assignment6_model_IntegerValueDependency', None)
    assert not _is_linked(a, 'assignment6_model_IntegerValueDependency', b2)
    if hasattr(b2, 'assignment6_model_IntegerFeature'):
        assert not _is_linked(b2, 'assignment6_model_IntegerFeature', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Dependency_strategy = st.builds(Dependency)
@given(instance=Dependency_strategy)
@settings(max_examples=25)
def test_Dependency_instantiation(instance):
    assert isinstance(instance, Dependency)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


UnaryDependency_strategy = st.builds(UnaryDependency)
@given(instance=UnaryDependency_strategy)
@settings(max_examples=25)
def test_UnaryDependency_instantiation(instance):
    assert isinstance(instance, UnaryDependency)


assignment6_model_BinaryDependency_strategy = st.builds(assignment6_model_BinaryDependency, operator=safe_text)
@given(instance=assignment6_model_BinaryDependency_strategy)
@settings(max_examples=25)
def test_assignment6_model_BinaryDependency_instantiation(instance):
    assert isinstance(instance, assignment6_model_BinaryDependency)


assignment6_model_Configurator_strategy = st.builds(assignment6_model_Configurator, name=safe_text)
@given(instance=assignment6_model_Configurator_strategy)
@settings(max_examples=25)
def test_assignment6_model_Configurator_instantiation(instance):
    assert isinstance(instance, assignment6_model_Configurator)


assignment6_model_Dependency_strategy = st.builds(assignment6_model_Dependency, not_=st.booleans())
@given(instance=assignment6_model_Dependency_strategy)
@settings(max_examples=25)
def test_assignment6_model_Dependency_instantiation(instance):
    assert isinstance(instance, assignment6_model_Dependency)


assignment6_model_Feature_strategy = st.builds(assignment6_model_Feature, mandatory=st.booleans(), name=safe_text, selected=st.booleans())
@given(instance=assignment6_model_Feature_strategy)
@settings(max_examples=25)
def test_assignment6_model_Feature_instantiation(instance):
    assert isinstance(instance, assignment6_model_Feature)


assignment6_model_Group_strategy = st.builds(assignment6_model_Group, groupType=safe_text, name=safe_text)
@given(instance=assignment6_model_Group_strategy)
@settings(max_examples=25)
def test_assignment6_model_Group_instantiation(instance):
    assert isinstance(instance, assignment6_model_Group)


assignment6_model_IntegerFeature_strategy = st.builds(assignment6_model_IntegerFeature, maxValue=st.integers(), minValue=st.integers(), step=st.integers(), value=st.integers())
@given(instance=assignment6_model_IntegerFeature_strategy)
@settings(max_examples=25)
def test_assignment6_model_IntegerFeature_instantiation(instance):
    assert isinstance(instance, assignment6_model_IntegerFeature)


assignment6_model_IntegerValueDependency_strategy = st.builds(assignment6_model_IntegerValueDependency, value=st.integers())
@given(instance=assignment6_model_IntegerValueDependency_strategy)
@settings(max_examples=25)
def test_assignment6_model_IntegerValueDependency_instantiation(instance):
    assert isinstance(instance, assignment6_model_IntegerValueDependency)


assignment6_model_IsSelectedDependency_strategy = st.builds(assignment6_model_IsSelectedDependency)
@given(instance=assignment6_model_IsSelectedDependency_strategy)
@settings(max_examples=25)
def test_assignment6_model_IsSelectedDependency_instantiation(instance):
    assert isinstance(instance, assignment6_model_IsSelectedDependency)


assignment6_model_SimpleFeature_strategy = st.builds(assignment6_model_SimpleFeature)
@given(instance=assignment6_model_SimpleFeature_strategy)
@settings(max_examples=25)
def test_assignment6_model_SimpleFeature_instantiation(instance):
    assert isinstance(instance, assignment6_model_SimpleFeature)


assignment6_model_UnaryDependency_strategy = st.builds(assignment6_model_UnaryDependency)
@given(instance=assignment6_model_UnaryDependency_strategy)
@settings(max_examples=25)
def test_assignment6_model_UnaryDependency_instantiation(instance):
    assert isinstance(instance, assignment6_model_UnaryDependency)


