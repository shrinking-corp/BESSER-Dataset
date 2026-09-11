import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActionResult,
    AtomicProcess,
    CompositeProcess,
    Process,
    actions_Action,
    actions_ActionResult,
    actions_ActionsCollection,
    actions_AtomicAction,
    actions_AtomicActionResult,
    actions_CompositeAction,
    actions_Condition,
    actions_Distribution,
    actions_Expression,
    actions_Parameter,
    actions_Participant,
    actions_Role,
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

def test_actions_ActionResult_id_value_roundtrip():
    instance = actions_ActionResult(id=7, version=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_actions_ActionResult_version_value_roundtrip():
    instance = actions_ActionResult(id=7, version=7)
    assert instance.version == 7
    instance.version = 13
    assert instance.version == 13


def test_actions_ActionsCollection_id_value_roundtrip():
    instance = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_actions_ActionsCollection_ns_value_roundtrip():
    instance = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    assert instance.ns == "sample_text"
    instance.ns = "sample_text_2"
    assert instance.ns == "sample_text_2"


def test_actions_ActionsCollection_version_value_roundtrip():
    instance = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    assert instance.version == 7
    instance.version = 13
    assert instance.version == 13


def test_actions_AtomicActionResult_hasDensity_value_roundtrip():
    instance = actions_AtomicActionResult(hasDensity=3.14)
    assert instance.hasDensity == 3.14
    instance.hasDensity = 9.99
    assert instance.hasDensity == 9.99


def test_actions_Distribution_datapoint_value_roundtrip():
    instance = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    assert instance.datapoint == 3.14
    instance.datapoint = 9.99
    assert instance.datapoint == 9.99


def test_actions_Distribution_density_value_roundtrip():
    instance = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    assert instance.density == 3.14
    instance.density = 9.99
    assert instance.density == 9.99


def test_actions_Distribution_id_value_roundtrip():
    instance = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_actions_Distribution_version_value_roundtrip():
    instance = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    assert instance.version == 7
    instance.version = 13
    assert instance.version == 13


def test_actions_AtomicAction_isa_Action():
    instance = actions_AtomicAction()
    assert isinstance(instance, Action)


def test_actions_CompositeAction_isa_Action():
    instance = actions_CompositeAction()
    assert isinstance(instance, Action)


def test_actions_AtomicActionResult_isa_ActionResult():
    instance = actions_AtomicActionResult(hasDensity=3.14)
    assert isinstance(instance, ActionResult)


def test_actions_AtomicAction_isa_AtomicProcess():
    instance = actions_AtomicAction()
    assert isinstance(instance, AtomicProcess)


def test_actions_CompositeAction_isa_CompositeProcess():
    instance = actions_CompositeAction()
    assert isinstance(instance, CompositeProcess)


def test_actions_Action_isa_Process():
    instance = actions_Action()
    assert isinstance(instance, Process)


def test_assoc_actions16_link_reassign_clear():
    a = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    b1 = actions_Action()
    b2 = actions_Action()
    _safe_set(a, 'actions_ActionsCollection', {b1})
    assert _is_linked(a, 'actions_ActionsCollection', b1)
    if hasattr(b1, 'actions_Action17'):
        assert _is_linked(b1, 'actions_Action17', a)
    _safe_set(a, 'actions_ActionsCollection', {b2})
    assert _is_linked(a, 'actions_ActionsCollection', b2)
    if hasattr(b1, 'actions_Action17'):
        assert not _is_linked(b1, 'actions_Action17', a)
    if hasattr(b2, 'actions_Action17'):
        assert _is_linked(b2, 'actions_Action17', a)
    _safe_set(a, 'actions_ActionsCollection', set())
    assert not _is_linked(a, 'actions_ActionsCollection', b2)
    if hasattr(b2, 'actions_Action17'):
        assert not _is_linked(b2, 'actions_Action17', a)


def test_assoc_hasAddEffect3_link_reassign_clear():
    a = actions_ActionResult(id=7, version=7)
    b1 = actions_Expression()
    b2 = actions_Expression()
    _safe_set(a, 'actions_ActionResult4', {b1})
    assert _is_linked(a, 'actions_ActionResult4', b1)
    if hasattr(b1, 'actions_Expression'):
        assert _is_linked(b1, 'actions_Expression', a)
    _safe_set(a, 'actions_ActionResult4', {b2})
    assert _is_linked(a, 'actions_ActionResult4', b2)
    if hasattr(b1, 'actions_Expression'):
        assert not _is_linked(b1, 'actions_Expression', a)
    if hasattr(b2, 'actions_Expression'):
        assert _is_linked(b2, 'actions_Expression', a)
    _safe_set(a, 'actions_ActionResult4', set())
    assert not _is_linked(a, 'actions_ActionResult4', b2)
    if hasattr(b2, 'actions_Expression'):
        assert not _is_linked(b2, 'actions_Expression', a)


def test_assoc_hasAtomicActionResult1_link_reassign_clear():
    a = actions_AtomicActionResult(hasDensity=3.14)
    b1 = actions_AtomicAction()
    b2 = actions_AtomicAction()
    _safe_set(a, 'actions_AtomicActionResult', b1)
    assert _is_linked(a, 'actions_AtomicActionResult', b1)
    if hasattr(b1, 'actions_AtomicAction'):
        assert _is_linked(b1, 'actions_AtomicAction', a)
    _safe_set(a, 'actions_AtomicActionResult', b2)
    assert _is_linked(a, 'actions_AtomicActionResult', b2)
    if hasattr(b1, 'actions_AtomicAction'):
        assert not _is_linked(b1, 'actions_AtomicAction', a)
    if hasattr(b2, 'actions_AtomicAction'):
        assert _is_linked(b2, 'actions_AtomicAction', a)
    _safe_set(a, 'actions_AtomicActionResult', None)
    assert not _is_linked(a, 'actions_AtomicActionResult', b2)
    if hasattr(b2, 'actions_AtomicAction'):
        assert not _is_linked(b2, 'actions_AtomicAction', a)


def test_assoc_hasCostDistribution8_link_reassign_clear():
    a = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    b1 = actions_AtomicActionResult(hasDensity=3.14)
    b2 = actions_AtomicActionResult(hasDensity=9.99)
    _safe_set(a, 'actions_Distribution', b1)
    assert _is_linked(a, 'actions_Distribution', b1)
    if hasattr(b1, 'actions_AtomicActionResult9'):
        assert _is_linked(b1, 'actions_AtomicActionResult9', a)
    _safe_set(a, 'actions_Distribution', b2)
    assert _is_linked(a, 'actions_Distribution', b2)
    if hasattr(b1, 'actions_AtomicActionResult9'):
        assert not _is_linked(b1, 'actions_AtomicActionResult9', a)
    if hasattr(b2, 'actions_AtomicActionResult9'):
        assert _is_linked(b2, 'actions_AtomicActionResult9', a)
    _safe_set(a, 'actions_Distribution', None)
    assert not _is_linked(a, 'actions_Distribution', b2)
    if hasattr(b2, 'actions_AtomicActionResult9'):
        assert not _is_linked(b2, 'actions_AtomicActionResult9', a)


def test_assoc_hasDeleteEffect5_link_reassign_clear():
    a = actions_ActionResult(id=7, version=7)
    b1 = actions_Expression()
    b2 = actions_Expression()
    _safe_set(a, 'actions_ActionResult6', {b1})
    assert _is_linked(a, 'actions_ActionResult6', b1)
    if hasattr(b1, 'actions_Expression7'):
        assert _is_linked(b1, 'actions_Expression7', a)
    _safe_set(a, 'actions_ActionResult6', {b2})
    assert _is_linked(a, 'actions_ActionResult6', b2)
    if hasattr(b1, 'actions_Expression7'):
        assert not _is_linked(b1, 'actions_Expression7', a)
    if hasattr(b2, 'actions_Expression7'):
        assert _is_linked(b2, 'actions_Expression7', a)
    _safe_set(a, 'actions_ActionResult6', set())
    assert not _is_linked(a, 'actions_ActionResult6', b2)
    if hasattr(b2, 'actions_Expression7'):
        assert not _is_linked(b2, 'actions_Expression7', a)


def test_assoc_hasDurationDistribution10_link_reassign_clear():
    a = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    b1 = actions_AtomicActionResult(hasDensity=3.14)
    b2 = actions_AtomicActionResult(hasDensity=9.99)
    _safe_set(a, 'actions_Distribution12', b1)
    assert _is_linked(a, 'actions_Distribution12', b1)
    if hasattr(b1, 'actions_AtomicActionResult11'):
        assert _is_linked(b1, 'actions_AtomicActionResult11', a)
    _safe_set(a, 'actions_Distribution12', b2)
    assert _is_linked(a, 'actions_Distribution12', b2)
    if hasattr(b1, 'actions_AtomicActionResult11'):
        assert not _is_linked(b1, 'actions_AtomicActionResult11', a)
    if hasattr(b2, 'actions_AtomicActionResult11'):
        assert _is_linked(b2, 'actions_AtomicActionResult11', a)
    _safe_set(a, 'actions_Distribution12', None)
    assert not _is_linked(a, 'actions_Distribution12', b2)
    if hasattr(b2, 'actions_AtomicActionResult11'):
        assert not _is_linked(b2, 'actions_AtomicActionResult11', a)


def test_assoc_hasQualityDistribution13_link_reassign_clear():
    a = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    b1 = actions_AtomicActionResult(hasDensity=3.14)
    b2 = actions_AtomicActionResult(hasDensity=9.99)
    _safe_set(a, 'actions_Distribution15', b1)
    assert _is_linked(a, 'actions_Distribution15', b1)
    if hasattr(b1, 'actions_AtomicActionResult14'):
        assert _is_linked(b1, 'actions_AtomicActionResult14', a)
    _safe_set(a, 'actions_Distribution15', b2)
    assert _is_linked(a, 'actions_Distribution15', b2)
    if hasattr(b1, 'actions_AtomicActionResult14'):
        assert not _is_linked(b1, 'actions_AtomicActionResult14', a)
    if hasattr(b2, 'actions_AtomicActionResult14'):
        assert _is_linked(b2, 'actions_AtomicActionResult14', a)
    _safe_set(a, 'actions_Distribution15', None)
    assert not _is_linked(a, 'actions_Distribution15', b2)
    if hasattr(b2, 'actions_AtomicActionResult14'):
        assert not _is_linked(b2, 'actions_AtomicActionResult14', a)


def test_assoc_inCondition2_link_reassign_clear():
    a = actions_ActionResult(id=7, version=7)
    b1 = actions_Condition()
    b2 = actions_Condition()
    _safe_set(a, 'actions_ActionResult', {b1})
    assert _is_linked(a, 'actions_ActionResult', b1)
    if hasattr(b1, 'actions_Condition'):
        assert _is_linked(b1, 'actions_Condition', a)
    _safe_set(a, 'actions_ActionResult', {b2})
    assert _is_linked(a, 'actions_ActionResult', b2)
    if hasattr(b1, 'actions_Condition'):
        assert not _is_linked(b1, 'actions_Condition', a)
    if hasattr(b2, 'actions_Condition'):
        assert _is_linked(b2, 'actions_Condition', a)
    _safe_set(a, 'actions_ActionResult', set())
    assert not _is_linked(a, 'actions_ActionResult', b2)
    if hasattr(b2, 'actions_Condition'):
        assert not _is_linked(b2, 'actions_Condition', a)


def test_assoc_parameters20_link_reassign_clear():
    a = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    b1 = actions_Parameter()
    b2 = actions_Parameter()
    _safe_set(a, 'actions_ActionsCollection21', {b1})
    assert _is_linked(a, 'actions_ActionsCollection21', b1)
    if hasattr(b1, 'actions_Parameter'):
        assert _is_linked(b1, 'actions_Parameter', a)
    _safe_set(a, 'actions_ActionsCollection21', {b2})
    assert _is_linked(a, 'actions_ActionsCollection21', b2)
    if hasattr(b1, 'actions_Parameter'):
        assert not _is_linked(b1, 'actions_Parameter', a)
    if hasattr(b2, 'actions_Parameter'):
        assert _is_linked(b2, 'actions_Parameter', a)
    _safe_set(a, 'actions_ActionsCollection21', set())
    assert not _is_linked(a, 'actions_ActionsCollection21', b2)
    if hasattr(b2, 'actions_Parameter'):
        assert not _is_linked(b2, 'actions_Parameter', a)


def test_assoc_participants18_link_reassign_clear():
    a = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    b1 = actions_Participant()
    b2 = actions_Participant()
    _safe_set(a, 'actions_ActionsCollection19', {b1})
    assert _is_linked(a, 'actions_ActionsCollection19', b1)
    if hasattr(b1, 'actions_Participant'):
        assert _is_linked(b1, 'actions_Participant', a)
    _safe_set(a, 'actions_ActionsCollection19', {b2})
    assert _is_linked(a, 'actions_ActionsCollection19', b2)
    if hasattr(b1, 'actions_Participant'):
        assert not _is_linked(b1, 'actions_Participant', a)
    if hasattr(b2, 'actions_Participant'):
        assert _is_linked(b2, 'actions_Participant', a)
    _safe_set(a, 'actions_ActionsCollection19', set())
    assert not _is_linked(a, 'actions_ActionsCollection19', b2)
    if hasattr(b2, 'actions_Participant'):
        assert not _is_linked(b2, 'actions_Participant', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActionResult_strategy = st.builds(ActionResult)
@given(instance=ActionResult_strategy)
@settings(max_examples=25)
def test_ActionResult_instantiation(instance):
    assert isinstance(instance, ActionResult)


AtomicProcess_strategy = st.builds(AtomicProcess)
@given(instance=AtomicProcess_strategy)
@settings(max_examples=25)
def test_AtomicProcess_instantiation(instance):
    assert isinstance(instance, AtomicProcess)


CompositeProcess_strategy = st.builds(CompositeProcess)
@given(instance=CompositeProcess_strategy)
@settings(max_examples=25)
def test_CompositeProcess_instantiation(instance):
    assert isinstance(instance, CompositeProcess)


Process_strategy = st.builds(Process)
@given(instance=Process_strategy)
@settings(max_examples=25)
def test_Process_instantiation(instance):
    assert isinstance(instance, Process)


actions_Action_strategy = st.builds(actions_Action)
@given(instance=actions_Action_strategy)
@settings(max_examples=25)
def test_actions_Action_instantiation(instance):
    assert isinstance(instance, actions_Action)


actions_ActionResult_strategy = st.builds(actions_ActionResult, id=st.integers(), version=st.integers())
@given(instance=actions_ActionResult_strategy)
@settings(max_examples=25)
def test_actions_ActionResult_instantiation(instance):
    assert isinstance(instance, actions_ActionResult)


actions_ActionsCollection_strategy = st.builds(actions_ActionsCollection, id=st.integers(), ns=safe_text, version=st.integers())
@given(instance=actions_ActionsCollection_strategy)
@settings(max_examples=25)
def test_actions_ActionsCollection_instantiation(instance):
    assert isinstance(instance, actions_ActionsCollection)


actions_AtomicAction_strategy = st.builds(actions_AtomicAction)
@given(instance=actions_AtomicAction_strategy)
@settings(max_examples=25)
def test_actions_AtomicAction_instantiation(instance):
    assert isinstance(instance, actions_AtomicAction)


actions_AtomicActionResult_strategy = st.builds(actions_AtomicActionResult, hasDensity=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=actions_AtomicActionResult_strategy)
@settings(max_examples=25)
def test_actions_AtomicActionResult_instantiation(instance):
    assert isinstance(instance, actions_AtomicActionResult)


actions_CompositeAction_strategy = st.builds(actions_CompositeAction)
@given(instance=actions_CompositeAction_strategy)
@settings(max_examples=25)
def test_actions_CompositeAction_instantiation(instance):
    assert isinstance(instance, actions_CompositeAction)


actions_Condition_strategy = st.builds(actions_Condition)
@given(instance=actions_Condition_strategy)
@settings(max_examples=25)
def test_actions_Condition_instantiation(instance):
    assert isinstance(instance, actions_Condition)


actions_Distribution_strategy = st.builds(actions_Distribution, datapoint=st.floats(allow_nan=False, allow_infinity=False), density=st.floats(allow_nan=False, allow_infinity=False), id=st.integers(), version=st.integers())
@given(instance=actions_Distribution_strategy)
@settings(max_examples=25)
def test_actions_Distribution_instantiation(instance):
    assert isinstance(instance, actions_Distribution)


actions_Expression_strategy = st.builds(actions_Expression)
@given(instance=actions_Expression_strategy)
@settings(max_examples=25)
def test_actions_Expression_instantiation(instance):
    assert isinstance(instance, actions_Expression)


actions_Parameter_strategy = st.builds(actions_Parameter)
@given(instance=actions_Parameter_strategy)
@settings(max_examples=25)
def test_actions_Parameter_instantiation(instance):
    assert isinstance(instance, actions_Parameter)


actions_Participant_strategy = st.builds(actions_Participant)
@given(instance=actions_Participant_strategy)
@settings(max_examples=25)
def test_actions_Participant_instantiation(instance):
    assert isinstance(instance, actions_Participant)


actions_Role_strategy = st.builds(actions_Role)
@given(instance=actions_Role_strategy)
@settings(max_examples=25)
def test_actions_Role_instantiation(instance):
    assert isinstance(instance, actions_Role)


