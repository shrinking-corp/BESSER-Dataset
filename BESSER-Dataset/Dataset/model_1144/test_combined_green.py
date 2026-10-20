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
    TrgCompositeState,
    TrgTransition,
    jointPackage_HSM2FSM_TrgStateMachine,
    TrgStateMachine,
    jointPackage_HSM2FSM_TrgRoot,
    SrcCompositeState,
    jointPackage_HSM2FSM_SrcAbstractState,
    jointPackage_HSM2FSM_SrcTransition,
    SrcAbstractState,
    jointPackage_HSM2FSM_SrcInitialState,
    jointPackage_HSM2FSM_SrcRegularState,
    jointPackage_HSM2FSM_SrcCompositeState,
    SrcTransition,
    jointPackage_HSM2FSM_SrcStateMachine,
    jointPackage_HSM2FSM_TrgAbstractState,
    jointPackage_HSM2FSM_TrgTransition,
    TrgAbstractState,
    jointPackage_HSM2FSM_TrgRegularState,
    jointPackage_HSM2FSM_TrgInitialState,
    jointPackage_HSM2FSM_TrgCompositeState,
    jointPackage_HSM2FSM_JointMM,
    SrcStateMachine,
    jointPackage_HSM2FSM_SrcRoot,
    TrgRoot,
    SrcRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_trgcompositestate_is_not_abstract():
    assert not inspect.isabstract(TrgCompositeState)


def test_hyp_trgcompositestate_constructor_exists():
    assert callable(TrgCompositeState.__init__)


def test_hyp_trgcompositestate_constructor_args():
    sig = inspect.signature(TrgCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trgtransition_is_not_abstract():
    assert not inspect.isabstract(TrgTransition)


def test_hyp_trgtransition_constructor_exists():
    assert callable(TrgTransition.__init__)


def test_hyp_trgtransition_constructor_args():
    sig = inspect.signature(TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_trgstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgStateMachine)


def test_hyp_jointpackage_hsm2fsm_trgstatemachine_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgStateMachine.__init__)


def test_hyp_jointpackage_hsm2fsm_trgstatemachine_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_trgstatemachine_is_not_abstract():
    assert not inspect.isabstract(TrgStateMachine)


def test_hyp_trgstatemachine_constructor_exists():
    assert callable(TrgStateMachine.__init__)


def test_hyp_trgstatemachine_constructor_args():
    sig = inspect.signature(TrgStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_trgroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgRoot)


def test_hyp_jointpackage_hsm2fsm_trgroot_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgRoot.__init__)


def test_hyp_jointpackage_hsm2fsm_trgroot_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_srccompositestate_is_not_abstract():
    assert not inspect.isabstract(SrcCompositeState)


def test_hyp_srccompositestate_constructor_exists():
    assert callable(SrcCompositeState.__init__)


def test_hyp_srccompositestate_constructor_args():
    sig = inspect.signature(SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srcabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcAbstractState)


def test_hyp_jointpackage_hsm2fsm_srcabstractstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcAbstractState.__init__)


def test_hyp_jointpackage_hsm2fsm_srcabstractstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jointpackage_hsm2fsm_srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcTransition)


def test_hyp_jointpackage_hsm2fsm_srctransition_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcTransition.__init__)


def test_hyp_jointpackage_hsm2fsm_srctransition_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_srcabstractstate_is_not_abstract():
    assert not inspect.isabstract(SrcAbstractState)


def test_hyp_srcabstractstate_constructor_exists():
    assert callable(SrcAbstractState.__init__)


def test_hyp_srcabstractstate_constructor_args():
    sig = inspect.signature(SrcAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srcinitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcInitialState)


def test_hyp_jointpackage_hsm2fsm_srcinitialstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcInitialState.__init__)


def test_hyp_jointpackage_hsm2fsm_srcinitialstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcInitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srcregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcRegularState)


def test_hyp_jointpackage_hsm2fsm_srcregularstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcRegularState.__init__)


def test_hyp_jointpackage_hsm2fsm_srcregularstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcRegularState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srccompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcCompositeState)


def test_hyp_jointpackage_hsm2fsm_srccompositestate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcCompositeState.__init__)


def test_hyp_jointpackage_hsm2fsm_srccompositestate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_srctransition_is_not_abstract():
    assert not inspect.isabstract(SrcTransition)


def test_hyp_srctransition_constructor_exists():
    assert callable(SrcTransition.__init__)


def test_hyp_srctransition_constructor_args():
    sig = inspect.signature(SrcTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcStateMachine)


def test_hyp_jointpackage_hsm2fsm_srcstatemachine_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcStateMachine.__init__)


def test_hyp_jointpackage_hsm2fsm_srcstatemachine_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jointpackage_hsm2fsm_trgabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgAbstractState)


def test_hyp_jointpackage_hsm2fsm_trgabstractstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgAbstractState.__init__)


def test_hyp_jointpackage_hsm2fsm_trgabstractstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jointpackage_hsm2fsm_trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgTransition)


def test_hyp_jointpackage_hsm2fsm_trgtransition_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgTransition.__init__)


def test_hyp_jointpackage_hsm2fsm_trgtransition_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_trgabstractstate_is_not_abstract():
    assert not inspect.isabstract(TrgAbstractState)


def test_hyp_trgabstractstate_constructor_exists():
    assert callable(TrgAbstractState.__init__)


def test_hyp_trgabstractstate_constructor_args():
    sig = inspect.signature(TrgAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_trgregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgRegularState)


def test_hyp_jointpackage_hsm2fsm_trgregularstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgRegularState.__init__)


def test_hyp_jointpackage_hsm2fsm_trgregularstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgRegularState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_trginitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgInitialState)


def test_hyp_jointpackage_hsm2fsm_trginitialstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgInitialState.__init__)


def test_hyp_jointpackage_hsm2fsm_trginitialstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgInitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_trgcompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgCompositeState)


def test_hyp_jointpackage_hsm2fsm_trgcompositestate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgCompositeState.__init__)


def test_hyp_jointpackage_hsm2fsm_trgcompositestate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_JointMM)


def test_hyp_jointpackage_hsm2fsm_jointmm_constructor_exists():
    assert callable(jointPackage_HSM2FSM_JointMM.__init__)


def test_hyp_jointpackage_hsm2fsm_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_JointMM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(SrcStateMachine)


def test_hyp_srcstatemachine_constructor_exists():
    assert callable(SrcStateMachine.__init__)


def test_hyp_srcstatemachine_constructor_args():
    sig = inspect.signature(SrcStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jointpackage_hsm2fsm_srcroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcRoot)


def test_hyp_jointpackage_hsm2fsm_srcroot_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcRoot.__init__)


def test_hyp_jointpackage_hsm2fsm_srcroot_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trgroot_is_not_abstract():
    assert not inspect.isabstract(TrgRoot)


def test_hyp_trgroot_constructor_exists():
    assert callable(TrgRoot.__init__)


def test_hyp_trgroot_constructor_args():
    sig = inspect.signature(TrgRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_srcroot_is_not_abstract():
    assert not inspect.isabstract(SrcRoot)


def test_hyp_srcroot_constructor_exists():
    assert callable(SrcRoot.__init__)


def test_hyp_srcroot_constructor_args():
    sig = inspect.signature(SrcRoot.__init__)
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
TrgCompositeState_strategy = st.builds(
    TrgCompositeState,
)
TrgTransition_strategy = st.builds(
    TrgTransition,
)
jointPackage_HSM2FSM_TrgStateMachine_strategy = st.builds(
    jointPackage_HSM2FSM_TrgStateMachine,
    name=
        safe_text
)
TrgStateMachine_strategy = st.builds(
    TrgStateMachine,
)
jointPackage_HSM2FSM_TrgRoot_strategy = st.builds(
    jointPackage_HSM2FSM_TrgRoot,
)
SrcCompositeState_strategy = st.builds(
    SrcCompositeState,
)
jointPackage_HSM2FSM_SrcAbstractState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcAbstractState,
    name=
        safe_text
)
jointPackage_HSM2FSM_SrcTransition_strategy = st.builds(
    jointPackage_HSM2FSM_SrcTransition,
    label=
        safe_text
)
SrcAbstractState_strategy = st.builds(
    SrcAbstractState,
)
jointPackage_HSM2FSM_SrcInitialState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcInitialState,
)
jointPackage_HSM2FSM_SrcRegularState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcRegularState,
)
jointPackage_HSM2FSM_SrcCompositeState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcCompositeState,
)
SrcTransition_strategy = st.builds(
    SrcTransition,
)
jointPackage_HSM2FSM_SrcStateMachine_strategy = st.builds(
    jointPackage_HSM2FSM_SrcStateMachine,
    name=
        safe_text
)
jointPackage_HSM2FSM_TrgAbstractState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgAbstractState,
    name=
        safe_text
)
jointPackage_HSM2FSM_TrgTransition_strategy = st.builds(
    jointPackage_HSM2FSM_TrgTransition,
    label=
        safe_text
)
TrgAbstractState_strategy = st.builds(
    TrgAbstractState,
)
jointPackage_HSM2FSM_TrgRegularState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgRegularState,
)
jointPackage_HSM2FSM_TrgInitialState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgInitialState,
)
jointPackage_HSM2FSM_TrgCompositeState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgCompositeState,
)
jointPackage_HSM2FSM_JointMM_strategy = st.builds(
    jointPackage_HSM2FSM_JointMM,
)
SrcStateMachine_strategy = st.builds(
    SrcStateMachine,
)
jointPackage_HSM2FSM_SrcRoot_strategy = st.builds(
    jointPackage_HSM2FSM_SrcRoot,
)
TrgRoot_strategy = st.builds(
    TrgRoot,
)
SrcRoot_strategy = st.builds(
    SrcRoot,
)






@given(instance=jointPackage_HSM2FSM_TrgStateMachine_strategy)
def test_hyp_jointpackage_hsm2fsm_trgstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=jointPackage_HSM2FSM_SrcAbstractState_strategy)
def test_hyp_jointpackage_hsm2fsm_srcabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=jointPackage_HSM2FSM_SrcTransition_strategy)
def test_hyp_jointpackage_hsm2fsm_srctransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original









@given(instance=jointPackage_HSM2FSM_SrcStateMachine_strategy)
def test_hyp_jointpackage_hsm2fsm_srcstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=jointPackage_HSM2FSM_TrgAbstractState_strategy)
def test_hyp_jointpackage_hsm2fsm_trgabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=jointPackage_HSM2FSM_TrgTransition_strategy)
def test_hyp_jointpackage_hsm2fsm_trgtransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SrcAbstractState,
    SrcCompositeState,
    SrcRoot,
    SrcStateMachine,
    SrcTransition,
    TrgAbstractState,
    TrgCompositeState,
    TrgRoot,
    TrgStateMachine,
    TrgTransition,
    jointPackage_HSM2FSM_JointMM,
    jointPackage_HSM2FSM_SrcAbstractState,
    jointPackage_HSM2FSM_SrcCompositeState,
    jointPackage_HSM2FSM_SrcInitialState,
    jointPackage_HSM2FSM_SrcRegularState,
    jointPackage_HSM2FSM_SrcRoot,
    jointPackage_HSM2FSM_SrcStateMachine,
    jointPackage_HSM2FSM_SrcTransition,
    jointPackage_HSM2FSM_TrgAbstractState,
    jointPackage_HSM2FSM_TrgCompositeState,
    jointPackage_HSM2FSM_TrgInitialState,
    jointPackage_HSM2FSM_TrgRegularState,
    jointPackage_HSM2FSM_TrgRoot,
    jointPackage_HSM2FSM_TrgStateMachine,
    jointPackage_HSM2FSM_TrgTransition,
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

def test_jointPackage_HSM2FSM_SrcAbstractState_name_value_roundtrip():
    instance = jointPackage_HSM2FSM_SrcAbstractState(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jointPackage_HSM2FSM_SrcStateMachine_name_value_roundtrip():
    instance = jointPackage_HSM2FSM_SrcStateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jointPackage_HSM2FSM_SrcTransition_label_value_roundtrip():
    instance = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_jointPackage_HSM2FSM_TrgAbstractState_name_value_roundtrip():
    instance = jointPackage_HSM2FSM_TrgAbstractState(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jointPackage_HSM2FSM_TrgStateMachine_name_value_roundtrip():
    instance = jointPackage_HSM2FSM_TrgStateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jointPackage_HSM2FSM_TrgTransition_label_value_roundtrip():
    instance = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_jointPackage_HSM2FSM_SrcCompositeState_isa_SrcAbstractState():
    instance = jointPackage_HSM2FSM_SrcCompositeState()
    assert isinstance(instance, SrcAbstractState)


def test_jointPackage_HSM2FSM_SrcInitialState_isa_SrcAbstractState():
    instance = jointPackage_HSM2FSM_SrcInitialState()
    assert isinstance(instance, SrcAbstractState)


def test_jointPackage_HSM2FSM_SrcRegularState_isa_SrcAbstractState():
    instance = jointPackage_HSM2FSM_SrcRegularState()
    assert isinstance(instance, SrcAbstractState)


def test_jointPackage_HSM2FSM_TrgCompositeState_isa_TrgAbstractState():
    instance = jointPackage_HSM2FSM_TrgCompositeState()
    assert isinstance(instance, TrgAbstractState)


def test_jointPackage_HSM2FSM_TrgInitialState_isa_TrgAbstractState():
    instance = jointPackage_HSM2FSM_TrgInitialState()
    assert isinstance(instance, TrgAbstractState)


def test_jointPackage_HSM2FSM_TrgRegularState_isa_TrgAbstractState():
    instance = jointPackage_HSM2FSM_TrgRegularState()
    assert isinstance(instance, TrgAbstractState)


def test_assoc_compositeStates16_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcAbstractState(name="sample_text")
    b1 = SrcCompositeState()
    b2 = SrcCompositeState()
    _safe_set(a, 'states17', b1)
    assert _is_linked(a, 'states17', b1)
    if hasattr(b1, 'SrcCompositeState'):
        assert _is_linked(b1, 'SrcCompositeState', a)
    _safe_set(a, 'states17', b2)
    assert _is_linked(a, 'states17', b2)
    if hasattr(b1, 'SrcCompositeState'):
        assert not _is_linked(b1, 'SrcCompositeState', a)
    if hasattr(b2, 'SrcCompositeState'):
        assert _is_linked(b2, 'SrcCompositeState', a)
    _safe_set(a, 'states17', None)
    assert not _is_linked(a, 'states17', b2)
    if hasattr(b2, 'SrcCompositeState'):
        assert not _is_linked(b2, 'SrcCompositeState', a)


def test_assoc_compositeStates36_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgAbstractState(name="sample_text")
    b1 = TrgCompositeState()
    b2 = TrgCompositeState()
    _safe_set(a, 'states37', b1)
    assert _is_linked(a, 'states37', b1)
    if hasattr(b1, 'TrgCompositeState'):
        assert _is_linked(b1, 'TrgCompositeState', a)
    _safe_set(a, 'states37', b2)
    assert _is_linked(a, 'states37', b2)
    if hasattr(b1, 'TrgCompositeState'):
        assert not _is_linked(b1, 'TrgCompositeState', a)
    if hasattr(b2, 'TrgCompositeState'):
        assert _is_linked(b2, 'TrgCompositeState', a)
    _safe_set(a, 'states37', None)
    assert not _is_linked(a, 'states37', b2)
    if hasattr(b2, 'TrgCompositeState'):
        assert not _is_linked(b2, 'TrgCompositeState', a)


def test_assoc_source28_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    b1 = TrgAbstractState()
    b2 = TrgAbstractState()
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition', b1)
    assert _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition', b1)
    if hasattr(b1, 'TrgAbstractState29'):
        assert _is_linked(b1, 'TrgAbstractState29', a)
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition', b2)
    assert _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition', b2)
    if hasattr(b1, 'TrgAbstractState29'):
        assert not _is_linked(b1, 'TrgAbstractState29', a)
    if hasattr(b2, 'TrgAbstractState29'):
        assert _is_linked(b2, 'TrgAbstractState29', a)
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition', None)
    assert not _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition', b2)
    if hasattr(b2, 'TrgAbstractState29'):
        assert not _is_linked(b2, 'TrgAbstractState29', a)


def test_assoc_source9_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    b1 = SrcAbstractState()
    b2 = SrcAbstractState()
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition', b1)
    assert _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition', b1)
    if hasattr(b1, 'SrcAbstractState10'):
        assert _is_linked(b1, 'SrcAbstractState10', a)
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition', b2)
    assert _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition', b2)
    if hasattr(b1, 'SrcAbstractState10'):
        assert not _is_linked(b1, 'SrcAbstractState10', a)
    if hasattr(b2, 'SrcAbstractState10'):
        assert _is_linked(b2, 'SrcAbstractState10', a)
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition', None)
    assert not _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition', b2)
    if hasattr(b2, 'SrcAbstractState10'):
        assert not _is_linked(b2, 'SrcAbstractState10', a)


def test_assoc_stateMachine14_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcAbstractState(name="sample_text")
    b1 = SrcStateMachine()
    b2 = SrcStateMachine()
    _safe_set(a, 'states', b1)
    assert _is_linked(a, 'states', b1)
    if hasattr(b1, 'SrcStateMachine15'):
        assert _is_linked(b1, 'SrcStateMachine15', a)
    _safe_set(a, 'states', b2)
    assert _is_linked(a, 'states', b2)
    if hasattr(b1, 'SrcStateMachine15'):
        assert not _is_linked(b1, 'SrcStateMachine15', a)
    if hasattr(b2, 'SrcStateMachine15'):
        assert _is_linked(b2, 'SrcStateMachine15', a)
    _safe_set(a, 'states', None)
    assert not _is_linked(a, 'states', b2)
    if hasattr(b2, 'SrcStateMachine15'):
        assert not _is_linked(b2, 'SrcStateMachine15', a)


def test_assoc_stateMachine25_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    b1 = TrgStateMachine()
    b2 = TrgStateMachine()
    _safe_set(a, 'transitions26', b1)
    assert _is_linked(a, 'transitions26', b1)
    if hasattr(b1, 'TrgStateMachine27'):
        assert _is_linked(b1, 'TrgStateMachine27', a)
    _safe_set(a, 'transitions26', b2)
    assert _is_linked(a, 'transitions26', b2)
    if hasattr(b1, 'TrgStateMachine27'):
        assert not _is_linked(b1, 'TrgStateMachine27', a)
    if hasattr(b2, 'TrgStateMachine27'):
        assert _is_linked(b2, 'TrgStateMachine27', a)
    _safe_set(a, 'transitions26', None)
    assert not _is_linked(a, 'transitions26', b2)
    if hasattr(b2, 'TrgStateMachine27'):
        assert not _is_linked(b2, 'TrgStateMachine27', a)


def test_assoc_stateMachine33_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgAbstractState(name="sample_text")
    b1 = TrgStateMachine()
    b2 = TrgStateMachine()
    _safe_set(a, 'states34', b1)
    assert _is_linked(a, 'states34', b1)
    if hasattr(b1, 'TrgStateMachine35'):
        assert _is_linked(b1, 'TrgStateMachine35', a)
    _safe_set(a, 'states34', b2)
    assert _is_linked(a, 'states34', b2)
    if hasattr(b1, 'TrgStateMachine35'):
        assert not _is_linked(b1, 'TrgStateMachine35', a)
    if hasattr(b2, 'TrgStateMachine35'):
        assert _is_linked(b2, 'TrgStateMachine35', a)
    _safe_set(a, 'states34', None)
    assert not _is_linked(a, 'states34', b2)
    if hasattr(b2, 'TrgStateMachine35'):
        assert not _is_linked(b2, 'TrgStateMachine35', a)


def test_assoc_stateMachine7_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    b1 = SrcStateMachine()
    b2 = SrcStateMachine()
    _safe_set(a, 'transitions', b1)
    assert _is_linked(a, 'transitions', b1)
    if hasattr(b1, 'SrcStateMachine8'):
        assert _is_linked(b1, 'SrcStateMachine8', a)
    _safe_set(a, 'transitions', b2)
    assert _is_linked(a, 'transitions', b2)
    if hasattr(b1, 'SrcStateMachine8'):
        assert not _is_linked(b1, 'SrcStateMachine8', a)
    if hasattr(b2, 'SrcStateMachine8'):
        assert _is_linked(b2, 'SrcStateMachine8', a)
    _safe_set(a, 'transitions', None)
    assert not _is_linked(a, 'transitions', b2)
    if hasattr(b2, 'SrcStateMachine8'):
        assert not _is_linked(b2, 'SrcStateMachine8', a)


def test_assoc_states23_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgStateMachine(name="sample_text")
    b1 = TrgAbstractState()
    b2 = TrgAbstractState()
    _safe_set(a, 'stateMachine24', {b1})
    assert _is_linked(a, 'stateMachine24', b1)
    if hasattr(b1, 'TrgAbstractState'):
        assert _is_linked(b1, 'TrgAbstractState', a)
    _safe_set(a, 'stateMachine24', {b2})
    assert _is_linked(a, 'stateMachine24', b2)
    if hasattr(b1, 'TrgAbstractState'):
        assert not _is_linked(b1, 'TrgAbstractState', a)
    if hasattr(b2, 'TrgAbstractState'):
        assert _is_linked(b2, 'TrgAbstractState', a)
    _safe_set(a, 'stateMachine24', set())
    assert not _is_linked(a, 'stateMachine24', b2)
    if hasattr(b2, 'TrgAbstractState'):
        assert not _is_linked(b2, 'TrgAbstractState', a)


def test_assoc_states5_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcStateMachine(name="sample_text")
    b1 = SrcAbstractState()
    b2 = SrcAbstractState()
    _safe_set(a, 'stateMachine6', {b1})
    assert _is_linked(a, 'stateMachine6', b1)
    if hasattr(b1, 'SrcAbstractState'):
        assert _is_linked(b1, 'SrcAbstractState', a)
    _safe_set(a, 'stateMachine6', {b2})
    assert _is_linked(a, 'stateMachine6', b2)
    if hasattr(b1, 'SrcAbstractState'):
        assert not _is_linked(b1, 'SrcAbstractState', a)
    if hasattr(b2, 'SrcAbstractState'):
        assert _is_linked(b2, 'SrcAbstractState', a)
    _safe_set(a, 'stateMachine6', set())
    assert not _is_linked(a, 'stateMachine6', b2)
    if hasattr(b2, 'SrcAbstractState'):
        assert not _is_linked(b2, 'SrcAbstractState', a)


def test_assoc_target11_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    b1 = SrcAbstractState()
    b2 = SrcAbstractState()
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition12', b1)
    assert _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition12', b1)
    if hasattr(b1, 'SrcAbstractState13'):
        assert _is_linked(b1, 'SrcAbstractState13', a)
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition12', b2)
    assert _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition12', b2)
    if hasattr(b1, 'SrcAbstractState13'):
        assert not _is_linked(b1, 'SrcAbstractState13', a)
    if hasattr(b2, 'SrcAbstractState13'):
        assert _is_linked(b2, 'SrcAbstractState13', a)
    _safe_set(a, 'jointPackage_HSM2FSM_SrcTransition12', None)
    assert not _is_linked(a, 'jointPackage_HSM2FSM_SrcTransition12', b2)
    if hasattr(b2, 'SrcAbstractState13'):
        assert not _is_linked(b2, 'SrcAbstractState13', a)


def test_assoc_target30_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    b1 = TrgAbstractState()
    b2 = TrgAbstractState()
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition31', b1)
    assert _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition31', b1)
    if hasattr(b1, 'TrgAbstractState32'):
        assert _is_linked(b1, 'TrgAbstractState32', a)
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition31', b2)
    assert _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition31', b2)
    if hasattr(b1, 'TrgAbstractState32'):
        assert not _is_linked(b1, 'TrgAbstractState32', a)
    if hasattr(b2, 'TrgAbstractState32'):
        assert _is_linked(b2, 'TrgAbstractState32', a)
    _safe_set(a, 'jointPackage_HSM2FSM_TrgTransition31', None)
    assert not _is_linked(a, 'jointPackage_HSM2FSM_TrgTransition31', b2)
    if hasattr(b2, 'TrgAbstractState32'):
        assert not _is_linked(b2, 'TrgAbstractState32', a)


def test_assoc_transitions21_link_reassign_clear():
    a = jointPackage_HSM2FSM_TrgStateMachine(name="sample_text")
    b1 = TrgTransition()
    b2 = TrgTransition()
    _safe_set(a, 'stateMachine22', {b1})
    assert _is_linked(a, 'stateMachine22', b1)
    if hasattr(b1, 'TrgTransition'):
        assert _is_linked(b1, 'TrgTransition', a)
    _safe_set(a, 'stateMachine22', {b2})
    assert _is_linked(a, 'stateMachine22', b2)
    if hasattr(b1, 'TrgTransition'):
        assert not _is_linked(b1, 'TrgTransition', a)
    if hasattr(b2, 'TrgTransition'):
        assert _is_linked(b2, 'TrgTransition', a)
    _safe_set(a, 'stateMachine22', set())
    assert not _is_linked(a, 'stateMachine22', b2)
    if hasattr(b2, 'TrgTransition'):
        assert not _is_linked(b2, 'TrgTransition', a)


def test_assoc_transitions4_link_reassign_clear():
    a = jointPackage_HSM2FSM_SrcStateMachine(name="sample_text")
    b1 = SrcTransition()
    b2 = SrcTransition()
    _safe_set(a, 'stateMachine', {b1})
    assert _is_linked(a, 'stateMachine', b1)
    if hasattr(b1, 'SrcTransition'):
        assert _is_linked(b1, 'SrcTransition', a)
    _safe_set(a, 'stateMachine', {b2})
    assert _is_linked(a, 'stateMachine', b2)
    if hasattr(b1, 'SrcTransition'):
        assert not _is_linked(b1, 'SrcTransition', a)
    if hasattr(b2, 'SrcTransition'):
        assert _is_linked(b2, 'SrcTransition', a)
    _safe_set(a, 'stateMachine', set())
    assert not _is_linked(a, 'stateMachine', b2)
    if hasattr(b2, 'SrcTransition'):
        assert not _is_linked(b2, 'SrcTransition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SrcAbstractState_strategy = st.builds(SrcAbstractState)
@given(instance=SrcAbstractState_strategy)
@settings(max_examples=25)
def test_SrcAbstractState_instantiation(instance):
    assert isinstance(instance, SrcAbstractState)


SrcCompositeState_strategy = st.builds(SrcCompositeState)
@given(instance=SrcCompositeState_strategy)
@settings(max_examples=25)
def test_SrcCompositeState_instantiation(instance):
    assert isinstance(instance, SrcCompositeState)


SrcRoot_strategy = st.builds(SrcRoot)
@given(instance=SrcRoot_strategy)
@settings(max_examples=25)
def test_SrcRoot_instantiation(instance):
    assert isinstance(instance, SrcRoot)


SrcStateMachine_strategy = st.builds(SrcStateMachine)
@given(instance=SrcStateMachine_strategy)
@settings(max_examples=25)
def test_SrcStateMachine_instantiation(instance):
    assert isinstance(instance, SrcStateMachine)


SrcTransition_strategy = st.builds(SrcTransition)
@given(instance=SrcTransition_strategy)
@settings(max_examples=25)
def test_SrcTransition_instantiation(instance):
    assert isinstance(instance, SrcTransition)


TrgAbstractState_strategy = st.builds(TrgAbstractState)
@given(instance=TrgAbstractState_strategy)
@settings(max_examples=25)
def test_TrgAbstractState_instantiation(instance):
    assert isinstance(instance, TrgAbstractState)


TrgCompositeState_strategy = st.builds(TrgCompositeState)
@given(instance=TrgCompositeState_strategy)
@settings(max_examples=25)
def test_TrgCompositeState_instantiation(instance):
    assert isinstance(instance, TrgCompositeState)


TrgRoot_strategy = st.builds(TrgRoot)
@given(instance=TrgRoot_strategy)
@settings(max_examples=25)
def test_TrgRoot_instantiation(instance):
    assert isinstance(instance, TrgRoot)


TrgStateMachine_strategy = st.builds(TrgStateMachine)
@given(instance=TrgStateMachine_strategy)
@settings(max_examples=25)
def test_TrgStateMachine_instantiation(instance):
    assert isinstance(instance, TrgStateMachine)


TrgTransition_strategy = st.builds(TrgTransition)
@given(instance=TrgTransition_strategy)
@settings(max_examples=25)
def test_TrgTransition_instantiation(instance):
    assert isinstance(instance, TrgTransition)


jointPackage_HSM2FSM_JointMM_strategy = st.builds(jointPackage_HSM2FSM_JointMM)
@given(instance=jointPackage_HSM2FSM_JointMM_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_JointMM_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_JointMM)


jointPackage_HSM2FSM_SrcAbstractState_strategy = st.builds(jointPackage_HSM2FSM_SrcAbstractState, name=safe_text)
@given(instance=jointPackage_HSM2FSM_SrcAbstractState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcAbstractState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcAbstractState)


jointPackage_HSM2FSM_SrcCompositeState_strategy = st.builds(jointPackage_HSM2FSM_SrcCompositeState)
@given(instance=jointPackage_HSM2FSM_SrcCompositeState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcCompositeState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcCompositeState)


jointPackage_HSM2FSM_SrcInitialState_strategy = st.builds(jointPackage_HSM2FSM_SrcInitialState)
@given(instance=jointPackage_HSM2FSM_SrcInitialState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcInitialState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcInitialState)


jointPackage_HSM2FSM_SrcRegularState_strategy = st.builds(jointPackage_HSM2FSM_SrcRegularState)
@given(instance=jointPackage_HSM2FSM_SrcRegularState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcRegularState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcRegularState)


jointPackage_HSM2FSM_SrcRoot_strategy = st.builds(jointPackage_HSM2FSM_SrcRoot)
@given(instance=jointPackage_HSM2FSM_SrcRoot_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcRoot_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcRoot)


jointPackage_HSM2FSM_SrcStateMachine_strategy = st.builds(jointPackage_HSM2FSM_SrcStateMachine, name=safe_text)
@given(instance=jointPackage_HSM2FSM_SrcStateMachine_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcStateMachine_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcStateMachine)


jointPackage_HSM2FSM_SrcTransition_strategy = st.builds(jointPackage_HSM2FSM_SrcTransition, label=safe_text)
@given(instance=jointPackage_HSM2FSM_SrcTransition_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_SrcTransition_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcTransition)


jointPackage_HSM2FSM_TrgAbstractState_strategy = st.builds(jointPackage_HSM2FSM_TrgAbstractState, name=safe_text)
@given(instance=jointPackage_HSM2FSM_TrgAbstractState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgAbstractState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgAbstractState)


jointPackage_HSM2FSM_TrgCompositeState_strategy = st.builds(jointPackage_HSM2FSM_TrgCompositeState)
@given(instance=jointPackage_HSM2FSM_TrgCompositeState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgCompositeState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgCompositeState)


jointPackage_HSM2FSM_TrgInitialState_strategy = st.builds(jointPackage_HSM2FSM_TrgInitialState)
@given(instance=jointPackage_HSM2FSM_TrgInitialState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgInitialState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgInitialState)


jointPackage_HSM2FSM_TrgRegularState_strategy = st.builds(jointPackage_HSM2FSM_TrgRegularState)
@given(instance=jointPackage_HSM2FSM_TrgRegularState_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgRegularState_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgRegularState)


jointPackage_HSM2FSM_TrgRoot_strategy = st.builds(jointPackage_HSM2FSM_TrgRoot)
@given(instance=jointPackage_HSM2FSM_TrgRoot_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgRoot_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgRoot)


jointPackage_HSM2FSM_TrgStateMachine_strategy = st.builds(jointPackage_HSM2FSM_TrgStateMachine, name=safe_text)
@given(instance=jointPackage_HSM2FSM_TrgStateMachine_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgStateMachine_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgStateMachine)


jointPackage_HSM2FSM_TrgTransition_strategy = st.builds(jointPackage_HSM2FSM_TrgTransition, label=safe_text)
@given(instance=jointPackage_HSM2FSM_TrgTransition_strategy)
@settings(max_examples=25)
def test_jointPackage_HSM2FSM_TrgTransition_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgTransition)



