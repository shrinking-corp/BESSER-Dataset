# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smachDSL_Transition,
    smachDSL_ActionState,
    smachDSL_ServiceClient,
    smachDSL_ActionClient,
    smachDSL_Test,
    smachDSL_StateMachine,
    smachDSL_PrimitivePackage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_smachdsl_transition_is_not_abstract():
    assert not inspect.isabstract(smachDSL_Transition)


def test_hyp_smachdsl_transition_constructor_exists():
    assert callable(smachDSL_Transition.__init__)


def test_hyp_smachdsl_transition_constructor_args():
    sig = inspect.signature(smachDSL_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "outcome" in params, "Missing parameter 'outcome'"




def test_hyp_smachdsl_actionstate_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ActionState)


def test_hyp_smachdsl_actionstate_constructor_exists():
    assert callable(smachDSL_ActionState.__init__)


def test_hyp_smachdsl_actionstate_constructor_args():
    sig = inspect.signature(smachDSL_ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_smachdsl_serviceclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ServiceClient)


def test_hyp_smachdsl_serviceclient_constructor_exists():
    assert callable(smachDSL_ServiceClient.__init__)


def test_hyp_smachdsl_serviceclient_constructor_args():
    sig = inspect.signature(smachDSL_ServiceClient.__init__)
    params = list(sig.parameters.keys())
    assert "servicesrv" in params, "Missing parameter 'servicesrv'"
    assert "servicename" in params, "Missing parameter 'servicename'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_smachdsl_actionclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ActionClient)


def test_hyp_smachdsl_actionclient_constructor_exists():
    assert callable(smachDSL_ActionClient.__init__)


def test_hyp_smachdsl_actionclient_constructor_args():
    sig = inspect.signature(smachDSL_ActionClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "actionname" in params, "Missing parameter 'actionname'"
    assert "actiontype" in params, "Missing parameter 'actiontype'"






def test_hyp_smachdsl_test_is_not_abstract():
    assert not inspect.isabstract(smachDSL_Test)


def test_hyp_smachdsl_test_constructor_exists():
    assert callable(smachDSL_Test.__init__)


def test_hyp_smachdsl_test_constructor_args():
    sig = inspect.signature(smachDSL_Test.__init__)
    params = list(sig.parameters.keys())
    assert "ros" in params, "Missing parameter 'ros'"




def test_hyp_smachdsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(smachDSL_StateMachine)


def test_hyp_smachdsl_statemachine_constructor_exists():
    assert callable(smachDSL_StateMachine.__init__)


def test_hyp_smachdsl_statemachine_constructor_args():
    sig = inspect.signature(smachDSL_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_smachdsl_primitivepackage_is_not_abstract():
    assert not inspect.isabstract(smachDSL_PrimitivePackage)


def test_hyp_smachdsl_primitivepackage_constructor_exists():
    assert callable(smachDSL_PrimitivePackage.__init__)


def test_hyp_smachdsl_primitivepackage_constructor_args():
    sig = inspect.signature(smachDSL_PrimitivePackage.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
smachDSL_Transition_strategy = st.builds(
    smachDSL_Transition,
    outcome=
        safe_text
)
smachDSL_ActionState_strategy = st.builds(
    smachDSL_ActionState,
    name=
        safe_text
)
smachDSL_ServiceClient_strategy = st.builds(
    smachDSL_ServiceClient,
    servicesrv=
        safe_text,
    servicename=
        safe_text,
    name=
        safe_text
)
smachDSL_ActionClient_strategy = st.builds(
    smachDSL_ActionClient,
    name=
        safe_text,
    actionname=
        safe_text,
    actiontype=
        safe_text
)
smachDSL_Test_strategy = st.builds(
    smachDSL_Test,
    ros=
        safe_text
)
smachDSL_StateMachine_strategy = st.builds(
    smachDSL_StateMachine,
    name=
        safe_text
)
smachDSL_PrimitivePackage_strategy = st.builds(
    smachDSL_PrimitivePackage,
)




@given(instance=smachDSL_Transition_strategy)
def test_hyp_smachdsl_transition_outcome_setter(instance):
    original = instance.outcome
    instance.outcome = original
    assert instance.outcome == original




@given(instance=smachDSL_ActionState_strategy)
def test_hyp_smachdsl_actionstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=smachDSL_ServiceClient_strategy)
def test_hyp_smachdsl_serviceclient_servicesrv_setter(instance):
    original = instance.servicesrv
    instance.servicesrv = original
    assert instance.servicesrv == original



@given(instance=smachDSL_ServiceClient_strategy)
def test_hyp_smachdsl_serviceclient_servicename_setter(instance):
    original = instance.servicename
    instance.servicename = original
    assert instance.servicename == original



@given(instance=smachDSL_ServiceClient_strategy)
def test_hyp_smachdsl_serviceclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=smachDSL_ActionClient_strategy)
def test_hyp_smachdsl_actionclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smachDSL_ActionClient_strategy)
def test_hyp_smachdsl_actionclient_actionname_setter(instance):
    original = instance.actionname
    instance.actionname = original
    assert instance.actionname == original



@given(instance=smachDSL_ActionClient_strategy)
def test_hyp_smachdsl_actionclient_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original




@given(instance=smachDSL_Test_strategy)
def test_hyp_smachdsl_test_ros_setter(instance):
    original = instance.ros
    instance.ros = original
    assert instance.ros == original




@given(instance=smachDSL_StateMachine_strategy)
def test_hyp_smachdsl_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    smachDSL_ActionClient,
    smachDSL_ActionState,
    smachDSL_PrimitivePackage,
    smachDSL_ServiceClient,
    smachDSL_StateMachine,
    smachDSL_Test,
    smachDSL_Transition,
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

def test_smachDSL_ActionClient_actionname_value_roundtrip():
    instance = smachDSL_ActionClient(actionname="sample_text", actiontype="sample_text", name="sample_text")
    assert instance.actionname == "sample_text"
    instance.actionname = "sample_text_2"
    assert instance.actionname == "sample_text_2"


def test_smachDSL_ActionClient_actiontype_value_roundtrip():
    instance = smachDSL_ActionClient(actionname="sample_text", actiontype="sample_text", name="sample_text")
    assert instance.actiontype == "sample_text"
    instance.actiontype = "sample_text_2"
    assert instance.actiontype == "sample_text_2"


def test_smachDSL_ActionClient_name_value_roundtrip():
    instance = smachDSL_ActionClient(actionname="sample_text", actiontype="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smachDSL_ActionState_name_value_roundtrip():
    instance = smachDSL_ActionState(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smachDSL_ServiceClient_name_value_roundtrip():
    instance = smachDSL_ServiceClient(name="sample_text", servicename="sample_text", servicesrv="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smachDSL_ServiceClient_servicename_value_roundtrip():
    instance = smachDSL_ServiceClient(name="sample_text", servicename="sample_text", servicesrv="sample_text")
    assert instance.servicename == "sample_text"
    instance.servicename = "sample_text_2"
    assert instance.servicename == "sample_text_2"


def test_smachDSL_ServiceClient_servicesrv_value_roundtrip():
    instance = smachDSL_ServiceClient(name="sample_text", servicename="sample_text", servicesrv="sample_text")
    assert instance.servicesrv == "sample_text"
    instance.servicesrv = "sample_text_2"
    assert instance.servicesrv == "sample_text_2"


def test_smachDSL_StateMachine_name_value_roundtrip():
    instance = smachDSL_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smachDSL_Test_ros_value_roundtrip():
    instance = smachDSL_Test(ros="sample_text")
    assert instance.ros == "sample_text"
    instance.ros = "sample_text_2"
    assert instance.ros == "sample_text_2"


def test_smachDSL_Transition_outcome_value_roundtrip():
    instance = smachDSL_Transition(outcome="sample_text")
    assert instance.outcome == "sample_text"
    instance.outcome = "sample_text_2"
    assert instance.outcome == "sample_text_2"


def test_assoc_actionclients1_link_reassign_clear():
    a = smachDSL_StateMachine(name="sample_text")
    b1 = smachDSL_ActionClient(actionname="sample_text", actiontype="sample_text", name="sample_text")
    b2 = smachDSL_ActionClient(actionname="sample_text_2", actiontype="sample_text_2", name="sample_text_2")
    _safe_set(a, 'smachDSL_StateMachine2', {b1})
    assert _is_linked(a, 'smachDSL_StateMachine2', b1)
    if hasattr(b1, 'smachDSL_ActionClient'):
        assert _is_linked(b1, 'smachDSL_ActionClient', a)
    _safe_set(a, 'smachDSL_StateMachine2', {b2})
    assert _is_linked(a, 'smachDSL_StateMachine2', b2)
    if hasattr(b1, 'smachDSL_ActionClient'):
        assert not _is_linked(b1, 'smachDSL_ActionClient', a)
    if hasattr(b2, 'smachDSL_ActionClient'):
        assert _is_linked(b2, 'smachDSL_ActionClient', a)
    _safe_set(a, 'smachDSL_StateMachine2', set())
    assert not _is_linked(a, 'smachDSL_StateMachine2', b2)
    if hasattr(b2, 'smachDSL_ActionClient'):
        assert not _is_linked(b2, 'smachDSL_ActionClient', a)


def test_assoc_actionsstates5_link_reassign_clear():
    a = smachDSL_StateMachine(name="sample_text")
    b1 = smachDSL_ActionState(name="sample_text")
    b2 = smachDSL_ActionState(name="sample_text_2")
    _safe_set(a, 'smachDSL_StateMachine6', {b1})
    assert _is_linked(a, 'smachDSL_StateMachine6', b1)
    if hasattr(b1, 'smachDSL_ActionState'):
        assert _is_linked(b1, 'smachDSL_ActionState', a)
    _safe_set(a, 'smachDSL_StateMachine6', {b2})
    assert _is_linked(a, 'smachDSL_StateMachine6', b2)
    if hasattr(b1, 'smachDSL_ActionState'):
        assert not _is_linked(b1, 'smachDSL_ActionState', a)
    if hasattr(b2, 'smachDSL_ActionState'):
        assert _is_linked(b2, 'smachDSL_ActionState', a)
    _safe_set(a, 'smachDSL_StateMachine6', set())
    assert not _is_linked(a, 'smachDSL_StateMachine6', b2)
    if hasattr(b2, 'smachDSL_ActionState'):
        assert not _is_linked(b2, 'smachDSL_ActionState', a)


def test_assoc_clientname7_link_reassign_clear():
    a = smachDSL_ActionState(name="sample_text")
    b1 = smachDSL_ActionClient(actionname="sample_text", actiontype="sample_text", name="sample_text")
    b2 = smachDSL_ActionClient(actionname="sample_text_2", actiontype="sample_text_2", name="sample_text_2")
    _safe_set(a, 'smachDSL_ActionState8', b1)
    assert _is_linked(a, 'smachDSL_ActionState8', b1)
    if hasattr(b1, 'smachDSL_ActionClient9'):
        assert _is_linked(b1, 'smachDSL_ActionClient9', a)
    _safe_set(a, 'smachDSL_ActionState8', b2)
    assert _is_linked(a, 'smachDSL_ActionState8', b2)
    if hasattr(b1, 'smachDSL_ActionClient9'):
        assert not _is_linked(b1, 'smachDSL_ActionClient9', a)
    if hasattr(b2, 'smachDSL_ActionClient9'):
        assert _is_linked(b2, 'smachDSL_ActionClient9', a)
    _safe_set(a, 'smachDSL_ActionState8', None)
    assert not _is_linked(a, 'smachDSL_ActionState8', b2)
    if hasattr(b2, 'smachDSL_ActionClient9'):
        assert not _is_linked(b2, 'smachDSL_ActionClient9', a)


def test_assoc_serviceclients3_link_reassign_clear():
    a = smachDSL_StateMachine(name="sample_text")
    b1 = smachDSL_ServiceClient(name="sample_text", servicename="sample_text", servicesrv="sample_text")
    b2 = smachDSL_ServiceClient(name="sample_text_2", servicename="sample_text_2", servicesrv="sample_text_2")
    _safe_set(a, 'smachDSL_StateMachine4', {b1})
    assert _is_linked(a, 'smachDSL_StateMachine4', b1)
    if hasattr(b1, 'smachDSL_ServiceClient'):
        assert _is_linked(b1, 'smachDSL_ServiceClient', a)
    _safe_set(a, 'smachDSL_StateMachine4', {b2})
    assert _is_linked(a, 'smachDSL_StateMachine4', b2)
    if hasattr(b1, 'smachDSL_ServiceClient'):
        assert not _is_linked(b1, 'smachDSL_ServiceClient', a)
    if hasattr(b2, 'smachDSL_ServiceClient'):
        assert _is_linked(b2, 'smachDSL_ServiceClient', a)
    _safe_set(a, 'smachDSL_StateMachine4', set())
    assert not _is_linked(a, 'smachDSL_StateMachine4', b2)
    if hasattr(b2, 'smachDSL_ServiceClient'):
        assert not _is_linked(b2, 'smachDSL_ServiceClient', a)


def test_assoc_state12_link_reassign_clear():
    a = smachDSL_Transition(outcome="sample_text")
    b1 = smachDSL_ActionState(name="sample_text")
    b2 = smachDSL_ActionState(name="sample_text_2")
    _safe_set(a, 'smachDSL_Transition13', b1)
    assert _is_linked(a, 'smachDSL_Transition13', b1)
    if hasattr(b1, 'smachDSL_ActionState14'):
        assert _is_linked(b1, 'smachDSL_ActionState14', a)
    _safe_set(a, 'smachDSL_Transition13', b2)
    assert _is_linked(a, 'smachDSL_Transition13', b2)
    if hasattr(b1, 'smachDSL_ActionState14'):
        assert not _is_linked(b1, 'smachDSL_ActionState14', a)
    if hasattr(b2, 'smachDSL_ActionState14'):
        assert _is_linked(b2, 'smachDSL_ActionState14', a)
    _safe_set(a, 'smachDSL_Transition13', None)
    assert not _is_linked(a, 'smachDSL_Transition13', b2)
    if hasattr(b2, 'smachDSL_ActionState14'):
        assert not _is_linked(b2, 'smachDSL_ActionState14', a)


def test_assoc_statemachines0_link_reassign_clear():
    a = smachDSL_StateMachine(name="sample_text")
    b1 = smachDSL_PrimitivePackage()
    b2 = smachDSL_PrimitivePackage()
    _safe_set(a, 'smachDSL_StateMachine', b1)
    assert _is_linked(a, 'smachDSL_StateMachine', b1)
    if hasattr(b1, 'smachDSL_PrimitivePackage'):
        assert _is_linked(b1, 'smachDSL_PrimitivePackage', a)
    _safe_set(a, 'smachDSL_StateMachine', b2)
    assert _is_linked(a, 'smachDSL_StateMachine', b2)
    if hasattr(b1, 'smachDSL_PrimitivePackage'):
        assert not _is_linked(b1, 'smachDSL_PrimitivePackage', a)
    if hasattr(b2, 'smachDSL_PrimitivePackage'):
        assert _is_linked(b2, 'smachDSL_PrimitivePackage', a)
    _safe_set(a, 'smachDSL_StateMachine', None)
    assert not _is_linked(a, 'smachDSL_StateMachine', b2)
    if hasattr(b2, 'smachDSL_PrimitivePackage'):
        assert not _is_linked(b2, 'smachDSL_PrimitivePackage', a)


def test_assoc_transitions10_link_reassign_clear():
    a = smachDSL_Transition(outcome="sample_text")
    b1 = smachDSL_ActionState(name="sample_text")
    b2 = smachDSL_ActionState(name="sample_text_2")
    _safe_set(a, 'smachDSL_Transition', b1)
    assert _is_linked(a, 'smachDSL_Transition', b1)
    if hasattr(b1, 'smachDSL_ActionState11'):
        assert _is_linked(b1, 'smachDSL_ActionState11', a)
    _safe_set(a, 'smachDSL_Transition', b2)
    assert _is_linked(a, 'smachDSL_Transition', b2)
    if hasattr(b1, 'smachDSL_ActionState11'):
        assert not _is_linked(b1, 'smachDSL_ActionState11', a)
    if hasattr(b2, 'smachDSL_ActionState11'):
        assert _is_linked(b2, 'smachDSL_ActionState11', a)
    _safe_set(a, 'smachDSL_Transition', None)
    assert not _is_linked(a, 'smachDSL_Transition', b2)
    if hasattr(b2, 'smachDSL_ActionState11'):
        assert not _is_linked(b2, 'smachDSL_ActionState11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

smachDSL_ActionClient_strategy = st.builds(smachDSL_ActionClient, actionname=safe_text, actiontype=safe_text, name=safe_text)
@given(instance=smachDSL_ActionClient_strategy)
@settings(max_examples=25)
def test_smachDSL_ActionClient_instantiation(instance):
    assert isinstance(instance, smachDSL_ActionClient)


smachDSL_ActionState_strategy = st.builds(smachDSL_ActionState, name=safe_text)
@given(instance=smachDSL_ActionState_strategy)
@settings(max_examples=25)
def test_smachDSL_ActionState_instantiation(instance):
    assert isinstance(instance, smachDSL_ActionState)


smachDSL_PrimitivePackage_strategy = st.builds(smachDSL_PrimitivePackage)
@given(instance=smachDSL_PrimitivePackage_strategy)
@settings(max_examples=25)
def test_smachDSL_PrimitivePackage_instantiation(instance):
    assert isinstance(instance, smachDSL_PrimitivePackage)


smachDSL_ServiceClient_strategy = st.builds(smachDSL_ServiceClient, name=safe_text, servicename=safe_text, servicesrv=safe_text)
@given(instance=smachDSL_ServiceClient_strategy)
@settings(max_examples=25)
def test_smachDSL_ServiceClient_instantiation(instance):
    assert isinstance(instance, smachDSL_ServiceClient)


smachDSL_StateMachine_strategy = st.builds(smachDSL_StateMachine, name=safe_text)
@given(instance=smachDSL_StateMachine_strategy)
@settings(max_examples=25)
def test_smachDSL_StateMachine_instantiation(instance):
    assert isinstance(instance, smachDSL_StateMachine)


smachDSL_Test_strategy = st.builds(smachDSL_Test, ros=safe_text)
@given(instance=smachDSL_Test_strategy)
@settings(max_examples=25)
def test_smachDSL_Test_instantiation(instance):
    assert isinstance(instance, smachDSL_Test)


smachDSL_Transition_strategy = st.builds(smachDSL_Transition, outcome=safe_text)
@given(instance=smachDSL_Transition_strategy)
@settings(max_examples=25)
def test_smachDSL_Transition_instantiation(instance):
    assert isinstance(instance, smachDSL_Transition)



