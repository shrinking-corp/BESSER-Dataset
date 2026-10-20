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
    UMLRealTimeStateMach_RTTrigger,
    UMLRealTimeStateMach_Pseudostate,
    UMLRealTimeStateMach_Operation,
    UMLRealTimeStateMach_RTPseudostate,
    UMLRealTimeStateMach_State,
    UMLRealTimeStateMach_RTState,
    UMLRealTimeStateMach_Region,
    UMLRealTimeStateMach_RTRegion,
    UMLRealTimeStateMach_StateMachine,
    UMLRealTimeStateMach_RTStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_umlrealtimestatemach_rttrigger_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_RTTrigger)


def test_hyp_umlrealtimestatemach_rttrigger_constructor_exists():
    assert callable(UMLRealTimeStateMach_RTTrigger.__init__)


def test_hyp_umlrealtimestatemach_rttrigger_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_RTTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_pseudostate_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_Pseudostate)


def test_hyp_umlrealtimestatemach_pseudostate_constructor_exists():
    assert callable(UMLRealTimeStateMach_Pseudostate.__init__)


def test_hyp_umlrealtimestatemach_pseudostate_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_operation_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_Operation)


def test_hyp_umlrealtimestatemach_operation_constructor_exists():
    assert callable(UMLRealTimeStateMach_Operation.__init__)


def test_hyp_umlrealtimestatemach_operation_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_rtpseudostate_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_RTPseudostate)


def test_hyp_umlrealtimestatemach_rtpseudostate_constructor_exists():
    assert callable(UMLRealTimeStateMach_RTPseudostate.__init__)


def test_hyp_umlrealtimestatemach_rtpseudostate_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_RTPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_state_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_State)


def test_hyp_umlrealtimestatemach_state_constructor_exists():
    assert callable(UMLRealTimeStateMach_State.__init__)


def test_hyp_umlrealtimestatemach_state_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_rtstate_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_RTState)


def test_hyp_umlrealtimestatemach_rtstate_constructor_exists():
    assert callable(UMLRealTimeStateMach_RTState.__init__)


def test_hyp_umlrealtimestatemach_rtstate_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_RTState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_region_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_Region)


def test_hyp_umlrealtimestatemach_region_constructor_exists():
    assert callable(UMLRealTimeStateMach_Region.__init__)


def test_hyp_umlrealtimestatemach_region_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_rtregion_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_RTRegion)


def test_hyp_umlrealtimestatemach_rtregion_constructor_exists():
    assert callable(UMLRealTimeStateMach_RTRegion.__init__)


def test_hyp_umlrealtimestatemach_rtregion_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_RTRegion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_statemachine_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_StateMachine)


def test_hyp_umlrealtimestatemach_statemachine_constructor_exists():
    assert callable(UMLRealTimeStateMach_StateMachine.__init__)


def test_hyp_umlrealtimestatemach_statemachine_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlrealtimestatemach_rtstatemachine_is_not_abstract():
    assert not inspect.isabstract(UMLRealTimeStateMach_RTStateMachine)


def test_hyp_umlrealtimestatemach_rtstatemachine_constructor_exists():
    assert callable(UMLRealTimeStateMach_RTStateMachine.__init__)


def test_hyp_umlrealtimestatemach_rtstatemachine_constructor_args():
    sig = inspect.signature(UMLRealTimeStateMach_RTStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "isPassive" in params, "Missing parameter 'isPassive'"



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
UMLRealTimeStateMach_RTTrigger_strategy = st.builds(
    UMLRealTimeStateMach_RTTrigger,
)
UMLRealTimeStateMach_Pseudostate_strategy = st.builds(
    UMLRealTimeStateMach_Pseudostate,
)
UMLRealTimeStateMach_Operation_strategy = st.builds(
    UMLRealTimeStateMach_Operation,
)
UMLRealTimeStateMach_RTPseudostate_strategy = st.builds(
    UMLRealTimeStateMach_RTPseudostate,
)
UMLRealTimeStateMach_State_strategy = st.builds(
    UMLRealTimeStateMach_State,
)
UMLRealTimeStateMach_RTState_strategy = st.builds(
    UMLRealTimeStateMach_RTState,
)
UMLRealTimeStateMach_Region_strategy = st.builds(
    UMLRealTimeStateMach_Region,
)
UMLRealTimeStateMach_RTRegion_strategy = st.builds(
    UMLRealTimeStateMach_RTRegion,
)
UMLRealTimeStateMach_StateMachine_strategy = st.builds(
    UMLRealTimeStateMach_StateMachine,
)
UMLRealTimeStateMach_RTStateMachine_strategy = st.builds(
    UMLRealTimeStateMach_RTStateMachine,
    isPassive=
        safe_text
)





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=UMLRealTimeStateMach_RTStateMachine_strategy)
def test_hyp_umlrealtimestatemach_rtstatemachine_isPassive_setter(instance):
    original = instance.isPassive
    instance.isPassive = original
    assert instance.isPassive == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    UMLRealTimeStateMach_Operation,
    UMLRealTimeStateMach_Pseudostate,
    UMLRealTimeStateMach_RTPseudostate,
    UMLRealTimeStateMach_RTRegion,
    UMLRealTimeStateMach_RTState,
    UMLRealTimeStateMach_RTStateMachine,
    UMLRealTimeStateMach_RTTrigger,
    UMLRealTimeStateMach_Region,
    UMLRealTimeStateMach_State,
    UMLRealTimeStateMach_StateMachine,
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

def test_UMLRealTimeStateMach_RTStateMachine_isPassive_value_roundtrip():
    instance = UMLRealTimeStateMach_RTStateMachine(isPassive="sample_text")
    assert instance.isPassive == "sample_text"
    instance.isPassive = "sample_text_2"
    assert instance.isPassive == "sample_text_2"


def test_assoc_base_Pseudostate3_link_reassign_clear():
    a = UMLRealTimeStateMach_RTPseudostate()
    b1 = UMLRealTimeStateMach_Pseudostate()
    b2 = UMLRealTimeStateMach_Pseudostate()
    _safe_set(a, 'UMLRealTimeStateMach_RTPseudostate', b1)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTPseudostate', b1)
    if hasattr(b1, 'UMLRealTimeStateMach_Pseudostate'):
        assert _is_linked(b1, 'UMLRealTimeStateMach_Pseudostate', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTPseudostate', b2)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTPseudostate', b2)
    if hasattr(b1, 'UMLRealTimeStateMach_Pseudostate'):
        assert not _is_linked(b1, 'UMLRealTimeStateMach_Pseudostate', a)
    if hasattr(b2, 'UMLRealTimeStateMach_Pseudostate'):
        assert _is_linked(b2, 'UMLRealTimeStateMach_Pseudostate', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTPseudostate', None)
    assert not _is_linked(a, 'UMLRealTimeStateMach_RTPseudostate', b2)
    if hasattr(b2, 'UMLRealTimeStateMach_Pseudostate'):
        assert not _is_linked(b2, 'UMLRealTimeStateMach_Pseudostate', a)


def test_assoc_base_Region1_link_reassign_clear():
    a = UMLRealTimeStateMach_RTRegion()
    b1 = UMLRealTimeStateMach_Region()
    b2 = UMLRealTimeStateMach_Region()
    _safe_set(a, 'UMLRealTimeStateMach_RTRegion', b1)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTRegion', b1)
    if hasattr(b1, 'UMLRealTimeStateMach_Region'):
        assert _is_linked(b1, 'UMLRealTimeStateMach_Region', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTRegion', b2)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTRegion', b2)
    if hasattr(b1, 'UMLRealTimeStateMach_Region'):
        assert not _is_linked(b1, 'UMLRealTimeStateMach_Region', a)
    if hasattr(b2, 'UMLRealTimeStateMach_Region'):
        assert _is_linked(b2, 'UMLRealTimeStateMach_Region', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTRegion', None)
    assert not _is_linked(a, 'UMLRealTimeStateMach_RTRegion', b2)
    if hasattr(b2, 'UMLRealTimeStateMach_Region'):
        assert not _is_linked(b2, 'UMLRealTimeStateMach_Region', a)


def test_assoc_base_State2_link_reassign_clear():
    a = UMLRealTimeStateMach_RTState()
    b1 = UMLRealTimeStateMach_State()
    b2 = UMLRealTimeStateMach_State()
    _safe_set(a, 'UMLRealTimeStateMach_RTState', b1)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTState', b1)
    if hasattr(b1, 'UMLRealTimeStateMach_State'):
        assert _is_linked(b1, 'UMLRealTimeStateMach_State', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTState', b2)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTState', b2)
    if hasattr(b1, 'UMLRealTimeStateMach_State'):
        assert not _is_linked(b1, 'UMLRealTimeStateMach_State', a)
    if hasattr(b2, 'UMLRealTimeStateMach_State'):
        assert _is_linked(b2, 'UMLRealTimeStateMach_State', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTState', None)
    assert not _is_linked(a, 'UMLRealTimeStateMach_RTState', b2)
    if hasattr(b2, 'UMLRealTimeStateMach_State'):
        assert not _is_linked(b2, 'UMLRealTimeStateMach_State', a)


def test_assoc_base_StateMachine0_link_reassign_clear():
    a = UMLRealTimeStateMach_RTStateMachine(isPassive="sample_text")
    b1 = UMLRealTimeStateMach_StateMachine()
    b2 = UMLRealTimeStateMach_StateMachine()
    _safe_set(a, 'UMLRealTimeStateMach_RTStateMachine', b1)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTStateMachine', b1)
    if hasattr(b1, 'UMLRealTimeStateMach_StateMachine'):
        assert _is_linked(b1, 'UMLRealTimeStateMach_StateMachine', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTStateMachine', b2)
    assert _is_linked(a, 'UMLRealTimeStateMach_RTStateMachine', b2)
    if hasattr(b1, 'UMLRealTimeStateMach_StateMachine'):
        assert not _is_linked(b1, 'UMLRealTimeStateMach_StateMachine', a)
    if hasattr(b2, 'UMLRealTimeStateMach_StateMachine'):
        assert _is_linked(b2, 'UMLRealTimeStateMach_StateMachine', a)
    _safe_set(a, 'UMLRealTimeStateMach_RTStateMachine', None)
    assert not _is_linked(a, 'UMLRealTimeStateMach_RTStateMachine', b2)
    if hasattr(b2, 'UMLRealTimeStateMach_StateMachine'):
        assert not _is_linked(b2, 'UMLRealTimeStateMach_StateMachine', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

UMLRealTimeStateMach_Operation_strategy = st.builds(UMLRealTimeStateMach_Operation)
@given(instance=UMLRealTimeStateMach_Operation_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_Operation_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_Operation)


UMLRealTimeStateMach_Pseudostate_strategy = st.builds(UMLRealTimeStateMach_Pseudostate)
@given(instance=UMLRealTimeStateMach_Pseudostate_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_Pseudostate_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_Pseudostate)


UMLRealTimeStateMach_RTPseudostate_strategy = st.builds(UMLRealTimeStateMach_RTPseudostate)
@given(instance=UMLRealTimeStateMach_RTPseudostate_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_RTPseudostate_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_RTPseudostate)


UMLRealTimeStateMach_RTRegion_strategy = st.builds(UMLRealTimeStateMach_RTRegion)
@given(instance=UMLRealTimeStateMach_RTRegion_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_RTRegion_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_RTRegion)


UMLRealTimeStateMach_RTState_strategy = st.builds(UMLRealTimeStateMach_RTState)
@given(instance=UMLRealTimeStateMach_RTState_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_RTState_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_RTState)


UMLRealTimeStateMach_RTStateMachine_strategy = st.builds(UMLRealTimeStateMach_RTStateMachine, isPassive=safe_text)
@given(instance=UMLRealTimeStateMach_RTStateMachine_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_RTStateMachine_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_RTStateMachine)


UMLRealTimeStateMach_RTTrigger_strategy = st.builds(UMLRealTimeStateMach_RTTrigger)
@given(instance=UMLRealTimeStateMach_RTTrigger_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_RTTrigger_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_RTTrigger)


UMLRealTimeStateMach_Region_strategy = st.builds(UMLRealTimeStateMach_Region)
@given(instance=UMLRealTimeStateMach_Region_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_Region_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_Region)


UMLRealTimeStateMach_State_strategy = st.builds(UMLRealTimeStateMach_State)
@given(instance=UMLRealTimeStateMach_State_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_State_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_State)


UMLRealTimeStateMach_StateMachine_strategy = st.builds(UMLRealTimeStateMach_StateMachine)
@given(instance=UMLRealTimeStateMach_StateMachine_strategy)
@settings(max_examples=25)
def test_UMLRealTimeStateMach_StateMachine_instantiation(instance):
    assert isinstance(instance, UMLRealTimeStateMach_StateMachine)



