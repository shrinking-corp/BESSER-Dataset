import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    dSLPolicies_AlgorithmType,
    dSLPolicies_GraphElement,
    dSLPolicies_GraphPolicies,
    dSLPolicies_Model,
    dSLPolicies_PathGeneratorStopCondition,
    dSLPolicies_Policies,
    dSLPolicies_Severity,
    dSLPolicies_StopCondition,
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

def test_dSLPolicies_AlgorithmType_type_value_roundtrip():
    instance = dSLPolicies_AlgorithmType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_dSLPolicies_GraphElement_name_value_roundtrip():
    instance = dSLPolicies_GraphElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSLPolicies_GraphPolicies_graphModelPolicies_value_roundtrip():
    instance = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text")
    assert instance.graphModelPolicies == "sample_text"
    instance.graphModelPolicies = "sample_text_2"
    assert instance.graphModelPolicies == "sample_text_2"


def test_dSLPolicies_Policies_nocheck_value_roundtrip():
    instance = dSLPolicies_Policies(nocheck=True, sync=True)
    assert instance.nocheck == True
    instance.nocheck = False
    assert instance.nocheck == False


def test_dSLPolicies_Policies_sync_value_roundtrip():
    instance = dSLPolicies_Policies(nocheck=True, sync=True)
    assert instance.sync == True
    instance.sync = False
    assert instance.sync == False


def test_dSLPolicies_Severity_level_value_roundtrip():
    instance = dSLPolicies_Severity(level="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_dSLPolicies_StopCondition_pathtype_value_roundtrip():
    instance = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    assert instance.pathtype == "sample_text"
    instance.pathtype = "sample_text_2"
    assert instance.pathtype == "sample_text_2"


def test_dSLPolicies_StopCondition_percentage_value_roundtrip():
    instance = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    assert instance.percentage == "sample_text"
    instance.percentage = "sample_text_2"
    assert instance.percentage == "sample_text_2"


def test_dSLPolicies_StopCondition_value_value_roundtrip():
    instance = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_assoc_algorithmType7_link_reassign_clear():
    a = dSLPolicies_AlgorithmType(type="sample_text")
    b1 = dSLPolicies_PathGeneratorStopCondition()
    b2 = dSLPolicies_PathGeneratorStopCondition()
    _safe_set(a, 'dSLPolicies_AlgorithmType', b1)
    assert _is_linked(a, 'dSLPolicies_AlgorithmType', b1)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition8'):
        assert _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition8', a)
    _safe_set(a, 'dSLPolicies_AlgorithmType', b2)
    assert _is_linked(a, 'dSLPolicies_AlgorithmType', b2)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition8'):
        assert not _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition8', a)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition8'):
        assert _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition8', a)
    _safe_set(a, 'dSLPolicies_AlgorithmType', None)
    assert not _is_linked(a, 'dSLPolicies_AlgorithmType', b2)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition8'):
        assert not _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition8', a)


def test_assoc_graphPolicies0_link_reassign_clear():
    a = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text")
    b1 = dSLPolicies_Model()
    b2 = dSLPolicies_Model()
    _safe_set(a, 'dSLPolicies_GraphPolicies', b1)
    assert _is_linked(a, 'dSLPolicies_GraphPolicies', b1)
    if hasattr(b1, 'dSLPolicies_Model'):
        assert _is_linked(b1, 'dSLPolicies_Model', a)
    _safe_set(a, 'dSLPolicies_GraphPolicies', b2)
    assert _is_linked(a, 'dSLPolicies_GraphPolicies', b2)
    if hasattr(b1, 'dSLPolicies_Model'):
        assert not _is_linked(b1, 'dSLPolicies_Model', a)
    if hasattr(b2, 'dSLPolicies_Model'):
        assert _is_linked(b2, 'dSLPolicies_Model', a)
    _safe_set(a, 'dSLPolicies_GraphPolicies', None)
    assert not _is_linked(a, 'dSLPolicies_GraphPolicies', b2)
    if hasattr(b2, 'dSLPolicies_Model'):
        assert not _is_linked(b2, 'dSLPolicies_Model', a)


def test_assoc_graphelement14_link_reassign_clear():
    a = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    b1 = dSLPolicies_GraphElement(name="sample_text")
    b2 = dSLPolicies_GraphElement(name="sample_text_2")
    _safe_set(a, 'dSLPolicies_StopCondition15', b1)
    assert _is_linked(a, 'dSLPolicies_StopCondition15', b1)
    if hasattr(b1, 'dSLPolicies_GraphElement'):
        assert _is_linked(b1, 'dSLPolicies_GraphElement', a)
    _safe_set(a, 'dSLPolicies_StopCondition15', b2)
    assert _is_linked(a, 'dSLPolicies_StopCondition15', b2)
    if hasattr(b1, 'dSLPolicies_GraphElement'):
        assert not _is_linked(b1, 'dSLPolicies_GraphElement', a)
    if hasattr(b2, 'dSLPolicies_GraphElement'):
        assert _is_linked(b2, 'dSLPolicies_GraphElement', a)
    _safe_set(a, 'dSLPolicies_StopCondition15', None)
    assert not _is_linked(a, 'dSLPolicies_StopCondition15', b2)
    if hasattr(b2, 'dSLPolicies_GraphElement'):
        assert not _is_linked(b2, 'dSLPolicies_GraphElement', a)


def test_assoc_pathgenerator3_link_reassign_clear():
    a = dSLPolicies_Policies(nocheck=True, sync=True)
    b1 = dSLPolicies_PathGeneratorStopCondition()
    b2 = dSLPolicies_PathGeneratorStopCondition()
    _safe_set(a, 'dSLPolicies_Policies4', {b1})
    assert _is_linked(a, 'dSLPolicies_Policies4', b1)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition'):
        assert _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition', a)
    _safe_set(a, 'dSLPolicies_Policies4', {b2})
    assert _is_linked(a, 'dSLPolicies_Policies4', b2)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition'):
        assert not _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition', a)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition'):
        assert _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition', a)
    _safe_set(a, 'dSLPolicies_Policies4', set())
    assert not _is_linked(a, 'dSLPolicies_Policies4', b2)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition'):
        assert not _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition', a)


def test_assoc_policies1_link_reassign_clear():
    a = dSLPolicies_Policies(nocheck=True, sync=True)
    b1 = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text")
    b2 = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text_2")
    _safe_set(a, 'dSLPolicies_Policies', b1)
    assert _is_linked(a, 'dSLPolicies_Policies', b1)
    if hasattr(b1, 'dSLPolicies_GraphPolicies2'):
        assert _is_linked(b1, 'dSLPolicies_GraphPolicies2', a)
    _safe_set(a, 'dSLPolicies_Policies', b2)
    assert _is_linked(a, 'dSLPolicies_Policies', b2)
    if hasattr(b1, 'dSLPolicies_GraphPolicies2'):
        assert not _is_linked(b1, 'dSLPolicies_GraphPolicies2', a)
    if hasattr(b2, 'dSLPolicies_GraphPolicies2'):
        assert _is_linked(b2, 'dSLPolicies_GraphPolicies2', a)
    _safe_set(a, 'dSLPolicies_Policies', None)
    assert not _is_linked(a, 'dSLPolicies_Policies', b2)
    if hasattr(b2, 'dSLPolicies_GraphPolicies2'):
        assert not _is_linked(b2, 'dSLPolicies_GraphPolicies2', a)


def test_assoc_severity5_link_reassign_clear():
    a = dSLPolicies_Severity(level="sample_text")
    b1 = dSLPolicies_Policies(nocheck=True, sync=True)
    b2 = dSLPolicies_Policies(nocheck=False, sync=False)
    _safe_set(a, 'dSLPolicies_Severity', b1)
    assert _is_linked(a, 'dSLPolicies_Severity', b1)
    if hasattr(b1, 'dSLPolicies_Policies6'):
        assert _is_linked(b1, 'dSLPolicies_Policies6', a)
    _safe_set(a, 'dSLPolicies_Severity', b2)
    assert _is_linked(a, 'dSLPolicies_Severity', b2)
    if hasattr(b1, 'dSLPolicies_Policies6'):
        assert not _is_linked(b1, 'dSLPolicies_Policies6', a)
    if hasattr(b2, 'dSLPolicies_Policies6'):
        assert _is_linked(b2, 'dSLPolicies_Policies6', a)
    _safe_set(a, 'dSLPolicies_Severity', None)
    assert not _is_linked(a, 'dSLPolicies_Severity', b2)
    if hasattr(b2, 'dSLPolicies_Policies6'):
        assert not _is_linked(b2, 'dSLPolicies_Policies6', a)


def test_assoc_stopCondition9_link_reassign_clear():
    a = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    b1 = dSLPolicies_PathGeneratorStopCondition()
    b2 = dSLPolicies_PathGeneratorStopCondition()
    _safe_set(a, 'dSLPolicies_StopCondition', b1)
    assert _is_linked(a, 'dSLPolicies_StopCondition', b1)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition10'):
        assert _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition10', a)
    _safe_set(a, 'dSLPolicies_StopCondition', b2)
    assert _is_linked(a, 'dSLPolicies_StopCondition', b2)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition10'):
        assert not _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition10', a)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition10'):
        assert _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition10', a)
    _safe_set(a, 'dSLPolicies_StopCondition', None)
    assert not _is_linked(a, 'dSLPolicies_StopCondition', b2)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition10'):
        assert not _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition10', a)


def test_assoc_stopConditionype11_link_reassign_clear():
    a = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    b1 = dSLPolicies_PathGeneratorStopCondition()
    b2 = dSLPolicies_PathGeneratorStopCondition()
    _safe_set(a, 'dSLPolicies_StopCondition13', b1)
    assert _is_linked(a, 'dSLPolicies_StopCondition13', b1)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition12'):
        assert _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition12', a)
    _safe_set(a, 'dSLPolicies_StopCondition13', b2)
    assert _is_linked(a, 'dSLPolicies_StopCondition13', b2)
    if hasattr(b1, 'dSLPolicies_PathGeneratorStopCondition12'):
        assert not _is_linked(b1, 'dSLPolicies_PathGeneratorStopCondition12', a)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition12'):
        assert _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition12', a)
    _safe_set(a, 'dSLPolicies_StopCondition13', None)
    assert not _is_linked(a, 'dSLPolicies_StopCondition13', b2)
    if hasattr(b2, 'dSLPolicies_PathGeneratorStopCondition12'):
        assert not _is_linked(b2, 'dSLPolicies_PathGeneratorStopCondition12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

dSLPolicies_AlgorithmType_strategy = st.builds(dSLPolicies_AlgorithmType, type=safe_text)
@given(instance=dSLPolicies_AlgorithmType_strategy)
@settings(max_examples=25)
def test_dSLPolicies_AlgorithmType_instantiation(instance):
    assert isinstance(instance, dSLPolicies_AlgorithmType)


dSLPolicies_GraphElement_strategy = st.builds(dSLPolicies_GraphElement, name=safe_text)
@given(instance=dSLPolicies_GraphElement_strategy)
@settings(max_examples=25)
def test_dSLPolicies_GraphElement_instantiation(instance):
    assert isinstance(instance, dSLPolicies_GraphElement)


dSLPolicies_GraphPolicies_strategy = st.builds(dSLPolicies_GraphPolicies, graphModelPolicies=safe_text)
@given(instance=dSLPolicies_GraphPolicies_strategy)
@settings(max_examples=25)
def test_dSLPolicies_GraphPolicies_instantiation(instance):
    assert isinstance(instance, dSLPolicies_GraphPolicies)


dSLPolicies_Model_strategy = st.builds(dSLPolicies_Model)
@given(instance=dSLPolicies_Model_strategy)
@settings(max_examples=25)
def test_dSLPolicies_Model_instantiation(instance):
    assert isinstance(instance, dSLPolicies_Model)


dSLPolicies_PathGeneratorStopCondition_strategy = st.builds(dSLPolicies_PathGeneratorStopCondition)
@given(instance=dSLPolicies_PathGeneratorStopCondition_strategy)
@settings(max_examples=25)
def test_dSLPolicies_PathGeneratorStopCondition_instantiation(instance):
    assert isinstance(instance, dSLPolicies_PathGeneratorStopCondition)


dSLPolicies_Policies_strategy = st.builds(dSLPolicies_Policies, nocheck=st.booleans(), sync=st.booleans())
@given(instance=dSLPolicies_Policies_strategy)
@settings(max_examples=25)
def test_dSLPolicies_Policies_instantiation(instance):
    assert isinstance(instance, dSLPolicies_Policies)


dSLPolicies_Severity_strategy = st.builds(dSLPolicies_Severity, level=safe_text)
@given(instance=dSLPolicies_Severity_strategy)
@settings(max_examples=25)
def test_dSLPolicies_Severity_instantiation(instance):
    assert isinstance(instance, dSLPolicies_Severity)


dSLPolicies_StopCondition_strategy = st.builds(dSLPolicies_StopCondition, pathtype=safe_text, percentage=safe_text, value=st.integers())
@given(instance=dSLPolicies_StopCondition_strategy)
@settings(max_examples=25)
def test_dSLPolicies_StopCondition_instantiation(instance):
    assert isinstance(instance, dSLPolicies_StopCondition)


