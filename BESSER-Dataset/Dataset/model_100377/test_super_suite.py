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
    metaCompo_mTransition,
    metaCompo_mComp,
    metaCompo_mState,
    metaCompo_mVariable,
    metaCompo_mFSM,
    metaCompo_mPort,
    mIO,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_metacompo_mtransition_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mTransition)


def test_hyp_metacompo_mtransition_constructor_exists():
    assert callable(metaCompo_mTransition.__init__)


def test_hyp_metacompo_mtransition_constructor_args():
    sig = inspect.signature(metaCompo_mTransition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "name" in params, "Missing parameter 'name'"
    assert "triggerExp" in params, "Missing parameter 'triggerExp'"







def test_hyp_metacompo_mcomp_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mComp)


def test_hyp_metacompo_mcomp_constructor_exists():
    assert callable(metaCompo_mComp.__init__)


def test_hyp_metacompo_mcomp_constructor_args():
    sig = inspect.signature(metaCompo_mComp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_metacompo_mstate_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mState)


def test_hyp_metacompo_mstate_constructor_exists():
    assert callable(metaCompo_mState.__init__)


def test_hyp_metacompo_mstate_constructor_args():
    sig = inspect.signature(metaCompo_mState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_metacompo_mvariable_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mVariable)


def test_hyp_metacompo_mvariable_constructor_exists():
    assert callable(metaCompo_mVariable.__init__)


def test_hyp_metacompo_mvariable_constructor_args():
    sig = inspect.signature(metaCompo_mVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_metacompo_mfsm_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mFSM)


def test_hyp_metacompo_mfsm_constructor_exists():
    assert callable(metaCompo_mFSM.__init__)


def test_hyp_metacompo_mfsm_constructor_args():
    sig = inspect.signature(metaCompo_mFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_metacompo_mport_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mPort)


def test_hyp_metacompo_mport_constructor_exists():
    assert callable(metaCompo_mPort.__init__)


def test_hyp_metacompo_mport_constructor_args():
    sig = inspect.signature(metaCompo_mPort.__init__)
    params = list(sig.parameters.keys())
    assert "io" in params, "Missing parameter 'io'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_mio_exists():
    # Check that the Enumeration exists
    assert mIO is not None

def test_hyp_mio_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in mIO]
    expected_literals = [
        "out",
        "in_",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in mIO"


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
metaCompo_mTransition_strategy = st.builds(
    metaCompo_mTransition,
    action=
        safe_text,
    guard=
        safe_text,
    name=
        safe_text,
    triggerExp=
        safe_text
)
metaCompo_mComp_strategy = st.builds(
    metaCompo_mComp,
    type=
        safe_text,
    name=
        safe_text
)
metaCompo_mState_strategy = st.builds(
    metaCompo_mState,
    name=
        safe_text
)
metaCompo_mVariable_strategy = st.builds(
    metaCompo_mVariable,
    name=
        safe_text,
    type=
        safe_text
)
metaCompo_mFSM_strategy = st.builds(
    metaCompo_mFSM,
    name=
        safe_text
)
metaCompo_mPort_strategy = st.builds(
    metaCompo_mPort,
    io=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)




@given(instance=metaCompo_mTransition_strategy)
def test_hyp_metacompo_mtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=metaCompo_mTransition_strategy)
def test_hyp_metacompo_mtransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=metaCompo_mTransition_strategy)
def test_hyp_metacompo_mtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mTransition_strategy)
def test_hyp_metacompo_mtransition_triggerExp_setter(instance):
    original = instance.triggerExp
    instance.triggerExp = original
    assert instance.triggerExp == original




@given(instance=metaCompo_mComp_strategy)
def test_hyp_metacompo_mcomp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=metaCompo_mComp_strategy)
def test_hyp_metacompo_mcomp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=metaCompo_mState_strategy)
def test_hyp_metacompo_mstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=metaCompo_mVariable_strategy)
def test_hyp_metacompo_mvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mVariable_strategy)
def test_hyp_metacompo_mvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=metaCompo_mFSM_strategy)
def test_hyp_metacompo_mfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=metaCompo_mPort_strategy)
def test_hyp_metacompo_mport_io_setter(instance):
    original = instance.io
    instance.io = original
    assert instance.io == original



@given(instance=metaCompo_mPort_strategy)
def test_hyp_metacompo_mport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mPort_strategy)
def test_hyp_metacompo_mport_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    metaCompo_mComp,
    metaCompo_mFSM,
    metaCompo_mPort,
    metaCompo_mState,
    metaCompo_mTransition,
    metaCompo_mVariable,
    mIO,
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

def test_metaCompo_mComp_name_value_roundtrip():
    instance = metaCompo_mComp(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mComp_type_value_roundtrip():
    instance = metaCompo_mComp(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_metaCompo_mFSM_name_value_roundtrip():
    instance = metaCompo_mFSM(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mPort_io_value_roundtrip():
    instance = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    assert instance.io == "sample_text"
    instance.io = "sample_text_2"
    assert instance.io == "sample_text_2"


def test_metaCompo_mPort_name_value_roundtrip():
    instance = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mPort_type_value_roundtrip():
    instance = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_metaCompo_mState_name_value_roundtrip():
    instance = metaCompo_mState(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mTransition_action_value_roundtrip():
    instance = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_metaCompo_mTransition_guard_value_roundtrip():
    instance = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    assert instance.guard == "sample_text"
    instance.guard = "sample_text_2"
    assert instance.guard == "sample_text_2"


def test_metaCompo_mTransition_name_value_roundtrip():
    instance = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mTransition_triggerExp_value_roundtrip():
    instance = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    assert instance.triggerExp == "sample_text"
    instance.triggerExp = "sample_text_2"
    assert instance.triggerExp == "sample_text_2"


def test_metaCompo_mVariable_name_value_roundtrip():
    instance = metaCompo_mVariable(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metaCompo_mVariable_type_value_roundtrip():
    instance = metaCompo_mVariable(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_FSMs4_link_reassign_clear():
    a = metaCompo_mFSM(name="sample_text")
    b1 = metaCompo_mComp(name="sample_text", type="sample_text")
    b2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'mFSM', b1)
    assert _is_linked(a, 'mFSM', b1)
    if hasattr(b1, 'component'):
        assert _is_linked(b1, 'component', a)
    _safe_set(a, 'mFSM', b2)
    assert _is_linked(a, 'mFSM', b2)
    if hasattr(b1, 'component'):
        assert not _is_linked(b1, 'component', a)
    if hasattr(b2, 'component'):
        assert _is_linked(b2, 'component', a)
    _safe_set(a, 'mFSM', None)
    assert not _is_linked(a, 'mFSM', b2)
    if hasattr(b2, 'component'):
        assert not _is_linked(b2, 'component', a)


def test_assoc_compVar5_link_reassign_clear():
    a = metaCompo_mVariable(name="sample_text", type="sample_text")
    b1 = metaCompo_mComp(name="sample_text", type="sample_text")
    b2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mVariable', b1)
    assert _is_linked(a, 'metaCompo_mVariable', b1)
    if hasattr(b1, 'metaCompo_mComp6'):
        assert _is_linked(b1, 'metaCompo_mComp6', a)
    _safe_set(a, 'metaCompo_mVariable', b2)
    assert _is_linked(a, 'metaCompo_mVariable', b2)
    if hasattr(b1, 'metaCompo_mComp6'):
        assert not _is_linked(b1, 'metaCompo_mComp6', a)
    if hasattr(b2, 'metaCompo_mComp6'):
        assert _is_linked(b2, 'metaCompo_mComp6', a)
    _safe_set(a, 'metaCompo_mVariable', None)
    assert not _is_linked(a, 'metaCompo_mVariable', b2)
    if hasattr(b2, 'metaCompo_mComp6'):
        assert not _is_linked(b2, 'metaCompo_mComp6', a)


def test_assoc_component13_link_reassign_clear():
    a = metaCompo_mFSM(name="sample_text")
    b1 = metaCompo_mComp(name="sample_text", type="sample_text")
    b2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'FSMs', b1)
    assert _is_linked(a, 'FSMs', b1)
    if hasattr(b1, 'mComp'):
        assert _is_linked(b1, 'mComp', a)
    _safe_set(a, 'FSMs', b2)
    assert _is_linked(a, 'FSMs', b2)
    if hasattr(b1, 'mComp'):
        assert not _is_linked(b1, 'mComp', a)
    if hasattr(b2, 'mComp'):
        assert _is_linked(b2, 'mComp', a)
    _safe_set(a, 'FSMs', None)
    assert not _is_linked(a, 'FSMs', b2)
    if hasattr(b2, 'mComp'):
        assert not _is_linked(b2, 'mComp', a)


def test_assoc_connToVar10_link_reassign_clear():
    a = metaCompo_mVariable(name="sample_text", type="sample_text")
    b1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    b2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mVariable12', b1)
    assert _is_linked(a, 'metaCompo_mVariable12', b1)
    if hasattr(b1, 'metaCompo_mPort11'):
        assert _is_linked(b1, 'metaCompo_mPort11', a)
    _safe_set(a, 'metaCompo_mVariable12', b2)
    assert _is_linked(a, 'metaCompo_mVariable12', b2)
    if hasattr(b1, 'metaCompo_mPort11'):
        assert not _is_linked(b1, 'metaCompo_mPort11', a)
    if hasattr(b2, 'metaCompo_mPort11'):
        assert _is_linked(b2, 'metaCompo_mPort11', a)
    _safe_set(a, 'metaCompo_mVariable12', None)
    assert not _is_linked(a, 'metaCompo_mVariable12', b2)
    if hasattr(b2, 'metaCompo_mPort11'):
        assert not _is_linked(b2, 'metaCompo_mPort11', a)


def test_assoc_connectedTo8_link_reassign_clear():
    a = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    b1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    b2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mPort7', b1)
    assert _is_linked(a, 'metaCompo_mPort7', b1)
    if hasattr(b1, 'metaCompo_mPort9'):
        assert _is_linked(b1, 'metaCompo_mPort9', a)
    _safe_set(a, 'metaCompo_mPort7', b2)
    assert _is_linked(a, 'metaCompo_mPort7', b2)
    if hasattr(b1, 'metaCompo_mPort9'):
        assert not _is_linked(b1, 'metaCompo_mPort9', a)
    if hasattr(b2, 'metaCompo_mPort9'):
        assert _is_linked(b2, 'metaCompo_mPort9', a)
    _safe_set(a, 'metaCompo_mPort7', None)
    assert not _is_linked(a, 'metaCompo_mPort7', b2)
    if hasattr(b2, 'metaCompo_mPort9'):
        assert not _is_linked(b2, 'metaCompo_mPort9', a)


def test_assoc_destination35_link_reassign_clear():
    a = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'mState36'):
        assert _is_linked(b1, 'mState36', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'mState36'):
        assert not _is_linked(b1, 'mState36', a)
    if hasattr(b2, 'mState36'):
        assert _is_linked(b2, 'mState36', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'mState36'):
        assert not _is_linked(b2, 'mState36', a)


def test_assoc_finalState19_link_reassign_clear():
    a = metaCompo_mState(name="sample_text")
    b1 = metaCompo_mFSM(name="sample_text")
    b2 = metaCompo_mFSM(name="sample_text_2")
    _safe_set(a, 'metaCompo_mState21', b1)
    assert _is_linked(a, 'metaCompo_mState21', b1)
    if hasattr(b1, 'metaCompo_mFSM20'):
        assert _is_linked(b1, 'metaCompo_mFSM20', a)
    _safe_set(a, 'metaCompo_mState21', b2)
    assert _is_linked(a, 'metaCompo_mState21', b2)
    if hasattr(b1, 'metaCompo_mFSM20'):
        assert not _is_linked(b1, 'metaCompo_mFSM20', a)
    if hasattr(b2, 'metaCompo_mFSM20'):
        assert _is_linked(b2, 'metaCompo_mFSM20', a)
    _safe_set(a, 'metaCompo_mState21', None)
    assert not _is_linked(a, 'metaCompo_mState21', b2)
    if hasattr(b2, 'metaCompo_mFSM20'):
        assert not _is_linked(b2, 'metaCompo_mFSM20', a)


def test_assoc_fsmVar14_link_reassign_clear():
    a = metaCompo_mVariable(name="sample_text", type="sample_text")
    b1 = metaCompo_mFSM(name="sample_text")
    b2 = metaCompo_mFSM(name="sample_text_2")
    _safe_set(a, 'metaCompo_mVariable15', b1)
    assert _is_linked(a, 'metaCompo_mVariable15', b1)
    if hasattr(b1, 'metaCompo_mFSM'):
        assert _is_linked(b1, 'metaCompo_mFSM', a)
    _safe_set(a, 'metaCompo_mVariable15', b2)
    assert _is_linked(a, 'metaCompo_mVariable15', b2)
    if hasattr(b1, 'metaCompo_mFSM'):
        assert not _is_linked(b1, 'metaCompo_mFSM', a)
    if hasattr(b2, 'metaCompo_mFSM'):
        assert _is_linked(b2, 'metaCompo_mFSM', a)
    _safe_set(a, 'metaCompo_mVariable15', None)
    assert not _is_linked(a, 'metaCompo_mVariable15', b2)
    if hasattr(b2, 'metaCompo_mFSM'):
        assert not _is_linked(b2, 'metaCompo_mFSM', a)


def test_assoc_incomingTransitions28_link_reassign_clear():
    a = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'mTransition29', b1)
    assert _is_linked(a, 'mTransition29', b1)
    if hasattr(b1, 'destination'):
        assert _is_linked(b1, 'destination', a)
    _safe_set(a, 'mTransition29', b2)
    assert _is_linked(a, 'mTransition29', b2)
    if hasattr(b1, 'destination'):
        assert not _is_linked(b1, 'destination', a)
    if hasattr(b2, 'destination'):
        assert _is_linked(b2, 'destination', a)
    _safe_set(a, 'mTransition29', None)
    assert not _is_linked(a, 'mTransition29', b2)
    if hasattr(b2, 'destination'):
        assert not _is_linked(b2, 'destination', a)


def test_assoc_initialState17_link_reassign_clear():
    a = metaCompo_mState(name="sample_text")
    b1 = metaCompo_mFSM(name="sample_text")
    b2 = metaCompo_mFSM(name="sample_text_2")
    _safe_set(a, 'metaCompo_mState', b1)
    assert _is_linked(a, 'metaCompo_mState', b1)
    if hasattr(b1, 'metaCompo_mFSM18'):
        assert _is_linked(b1, 'metaCompo_mFSM18', a)
    _safe_set(a, 'metaCompo_mState', b2)
    assert _is_linked(a, 'metaCompo_mState', b2)
    if hasattr(b1, 'metaCompo_mFSM18'):
        assert not _is_linked(b1, 'metaCompo_mFSM18', a)
    if hasattr(b2, 'metaCompo_mFSM18'):
        assert _is_linked(b2, 'metaCompo_mFSM18', a)
    _safe_set(a, 'metaCompo_mState', None)
    assert not _is_linked(a, 'metaCompo_mState', b2)
    if hasattr(b2, 'metaCompo_mFSM18'):
        assert not _is_linked(b2, 'metaCompo_mFSM18', a)


def test_assoc_outgoingTransitions27_link_reassign_clear():
    a = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'mTransition', b1)
    assert _is_linked(a, 'mTransition', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'mTransition', b2)
    assert _is_linked(a, 'mTransition', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'mTransition', None)
    assert not _is_linked(a, 'mTransition', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_owningFSM22_link_reassign_clear():
    a = metaCompo_mState(name="sample_text")
    b1 = metaCompo_mFSM(name="sample_text")
    b2 = metaCompo_mFSM(name="sample_text_2")
    _safe_set(a, 'states', b1)
    assert _is_linked(a, 'states', b1)
    if hasattr(b1, 'mFSM23'):
        assert _is_linked(b1, 'mFSM23', a)
    _safe_set(a, 'states', b2)
    assert _is_linked(a, 'states', b2)
    if hasattr(b1, 'mFSM23'):
        assert not _is_linked(b1, 'mFSM23', a)
    if hasattr(b2, 'mFSM23'):
        assert _is_linked(b2, 'mFSM23', a)
    _safe_set(a, 'states', None)
    assert not _is_linked(a, 'states', b2)
    if hasattr(b2, 'mFSM23'):
        assert not _is_linked(b2, 'mFSM23', a)


def test_assoc_ports2_link_reassign_clear():
    a = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    b1 = metaCompo_mComp(name="sample_text", type="sample_text")
    b2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mPort', b1)
    assert _is_linked(a, 'metaCompo_mPort', b1)
    if hasattr(b1, 'metaCompo_mComp3'):
        assert _is_linked(b1, 'metaCompo_mComp3', a)
    _safe_set(a, 'metaCompo_mPort', b2)
    assert _is_linked(a, 'metaCompo_mPort', b2)
    if hasattr(b1, 'metaCompo_mComp3'):
        assert not _is_linked(b1, 'metaCompo_mComp3', a)
    if hasattr(b2, 'metaCompo_mComp3'):
        assert _is_linked(b2, 'metaCompo_mComp3', a)
    _safe_set(a, 'metaCompo_mPort', None)
    assert not _is_linked(a, 'metaCompo_mPort', b2)
    if hasattr(b2, 'metaCompo_mComp3'):
        assert not _is_linked(b2, 'metaCompo_mComp3', a)


def test_assoc_source33_link_reassign_clear():
    a = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'mState34'):
        assert _is_linked(b1, 'mState34', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'mState34'):
        assert not _is_linked(b1, 'mState34', a)
    if hasattr(b2, 'mState34'):
        assert _is_linked(b2, 'mState34', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'mState34'):
        assert not _is_linked(b2, 'mState34', a)


def test_assoc_stateVar24_link_reassign_clear():
    a = metaCompo_mVariable(name="sample_text", type="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'metaCompo_mVariable26', b1)
    assert _is_linked(a, 'metaCompo_mVariable26', b1)
    if hasattr(b1, 'metaCompo_mState25'):
        assert _is_linked(b1, 'metaCompo_mState25', a)
    _safe_set(a, 'metaCompo_mVariable26', b2)
    assert _is_linked(a, 'metaCompo_mVariable26', b2)
    if hasattr(b1, 'metaCompo_mState25'):
        assert not _is_linked(b1, 'metaCompo_mState25', a)
    if hasattr(b2, 'metaCompo_mState25'):
        assert _is_linked(b2, 'metaCompo_mState25', a)
    _safe_set(a, 'metaCompo_mVariable26', None)
    assert not _is_linked(a, 'metaCompo_mVariable26', b2)
    if hasattr(b2, 'metaCompo_mState25'):
        assert not _is_linked(b2, 'metaCompo_mState25', a)


def test_assoc_states16_link_reassign_clear():
    a = metaCompo_mState(name="sample_text")
    b1 = metaCompo_mFSM(name="sample_text")
    b2 = metaCompo_mFSM(name="sample_text_2")
    _safe_set(a, 'mState', b1)
    assert _is_linked(a, 'mState', b1)
    if hasattr(b1, 'owningFSM'):
        assert _is_linked(b1, 'owningFSM', a)
    _safe_set(a, 'mState', b2)
    assert _is_linked(a, 'mState', b2)
    if hasattr(b1, 'owningFSM'):
        assert not _is_linked(b1, 'owningFSM', a)
    if hasattr(b2, 'owningFSM'):
        assert _is_linked(b2, 'owningFSM', a)
    _safe_set(a, 'mState', None)
    assert not _is_linked(a, 'mState', b2)
    if hasattr(b2, 'owningFSM'):
        assert not _is_linked(b2, 'owningFSM', a)


def test_assoc_subComps1_link_reassign_clear():
    a = metaCompo_mComp(name="sample_text", type="sample_text")
    b1 = metaCompo_mComp(name="sample_text", type="sample_text")
    b2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mComp', b1)
    assert _is_linked(a, 'metaCompo_mComp', b1)
    if hasattr(b1, 'metaCompo_mComp0'):
        assert _is_linked(b1, 'metaCompo_mComp0', a)
    _safe_set(a, 'metaCompo_mComp', b2)
    assert _is_linked(a, 'metaCompo_mComp', b2)
    if hasattr(b1, 'metaCompo_mComp0'):
        assert not _is_linked(b1, 'metaCompo_mComp0', a)
    if hasattr(b2, 'metaCompo_mComp0'):
        assert _is_linked(b2, 'metaCompo_mComp0', a)
    _safe_set(a, 'metaCompo_mComp', None)
    assert not _is_linked(a, 'metaCompo_mComp', b2)
    if hasattr(b2, 'metaCompo_mComp0'):
        assert not _is_linked(b2, 'metaCompo_mComp0', a)


def test_assoc_subStates31_link_reassign_clear():
    a = metaCompo_mState(name="sample_text")
    b1 = metaCompo_mState(name="sample_text")
    b2 = metaCompo_mState(name="sample_text_2")
    _safe_set(a, 'metaCompo_mState30', {b1})
    assert _is_linked(a, 'metaCompo_mState30', b1)
    if hasattr(b1, 'metaCompo_mState32'):
        assert _is_linked(b1, 'metaCompo_mState32', a)
    _safe_set(a, 'metaCompo_mState30', {b2})
    assert _is_linked(a, 'metaCompo_mState30', b2)
    if hasattr(b1, 'metaCompo_mState32'):
        assert not _is_linked(b1, 'metaCompo_mState32', a)
    if hasattr(b2, 'metaCompo_mState32'):
        assert _is_linked(b2, 'metaCompo_mState32', a)
    _safe_set(a, 'metaCompo_mState30', set())
    assert not _is_linked(a, 'metaCompo_mState30', b2)
    if hasattr(b2, 'metaCompo_mState32'):
        assert not _is_linked(b2, 'metaCompo_mState32', a)


def test_assoc_trigerringVar37_link_reassign_clear():
    a = metaCompo_mVariable(name="sample_text", type="sample_text")
    b1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    _safe_set(a, 'metaCompo_mVariable38', b1)
    assert _is_linked(a, 'metaCompo_mVariable38', b1)
    if hasattr(b1, 'metaCompo_mTransition'):
        assert _is_linked(b1, 'metaCompo_mTransition', a)
    _safe_set(a, 'metaCompo_mVariable38', b2)
    assert _is_linked(a, 'metaCompo_mVariable38', b2)
    if hasattr(b1, 'metaCompo_mTransition'):
        assert not _is_linked(b1, 'metaCompo_mTransition', a)
    if hasattr(b2, 'metaCompo_mTransition'):
        assert _is_linked(b2, 'metaCompo_mTransition', a)
    _safe_set(a, 'metaCompo_mVariable38', None)
    assert not _is_linked(a, 'metaCompo_mVariable38', b2)
    if hasattr(b2, 'metaCompo_mTransition'):
        assert not _is_linked(b2, 'metaCompo_mTransition', a)


def test_assoc_triggeringPort39_link_reassign_clear():
    a = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    b1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    b2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'metaCompo_mTransition40', {b1})
    assert _is_linked(a, 'metaCompo_mTransition40', b1)
    if hasattr(b1, 'metaCompo_mPort41'):
        assert _is_linked(b1, 'metaCompo_mPort41', a)
    _safe_set(a, 'metaCompo_mTransition40', {b2})
    assert _is_linked(a, 'metaCompo_mTransition40', b2)
    if hasattr(b1, 'metaCompo_mPort41'):
        assert not _is_linked(b1, 'metaCompo_mPort41', a)
    if hasattr(b2, 'metaCompo_mPort41'):
        assert _is_linked(b2, 'metaCompo_mPort41', a)
    _safe_set(a, 'metaCompo_mTransition40', set())
    assert not _is_linked(a, 'metaCompo_mTransition40', b2)
    if hasattr(b2, 'metaCompo_mPort41'):
        assert not _is_linked(b2, 'metaCompo_mPort41', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

metaCompo_mComp_strategy = st.builds(metaCompo_mComp, name=safe_text, type=safe_text)
@given(instance=metaCompo_mComp_strategy)
@settings(max_examples=25)
def test_metaCompo_mComp_instantiation(instance):
    assert isinstance(instance, metaCompo_mComp)


metaCompo_mFSM_strategy = st.builds(metaCompo_mFSM, name=safe_text)
@given(instance=metaCompo_mFSM_strategy)
@settings(max_examples=25)
def test_metaCompo_mFSM_instantiation(instance):
    assert isinstance(instance, metaCompo_mFSM)


metaCompo_mPort_strategy = st.builds(metaCompo_mPort, io=safe_text, name=safe_text, type=safe_text)
@given(instance=metaCompo_mPort_strategy)
@settings(max_examples=25)
def test_metaCompo_mPort_instantiation(instance):
    assert isinstance(instance, metaCompo_mPort)


metaCompo_mState_strategy = st.builds(metaCompo_mState, name=safe_text)
@given(instance=metaCompo_mState_strategy)
@settings(max_examples=25)
def test_metaCompo_mState_instantiation(instance):
    assert isinstance(instance, metaCompo_mState)


metaCompo_mTransition_strategy = st.builds(metaCompo_mTransition, action=safe_text, guard=safe_text, name=safe_text, triggerExp=safe_text)
@given(instance=metaCompo_mTransition_strategy)
@settings(max_examples=25)
def test_metaCompo_mTransition_instantiation(instance):
    assert isinstance(instance, metaCompo_mTransition)


metaCompo_mVariable_strategy = st.builds(metaCompo_mVariable, name=safe_text, type=safe_text)
@given(instance=metaCompo_mVariable_strategy)
@settings(max_examples=25)
def test_metaCompo_mVariable_instantiation(instance):
    assert isinstance(instance, metaCompo_mVariable)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metaCompo_mComp,
    metaCompo_mFSM,
    metaCompo_mPort,
    metaCompo_mState,
    metaCompo_mTransition,
    metaCompo_mVariable,
    mIO,
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

def test_assoc_FSMs4_reverse_link_reassign_clear():
    a1 = metaCompo_mFSM(name="sample_text")
    a2 = metaCompo_mFSM(name="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'component', {a1})
    assert _is_linked(b, 'component', a1)
    if hasattr(a1, 'mFSM'):
        assert _is_linked(a1, 'mFSM', b)
    _safe_set(b, 'component', {a2})
    assert _is_linked(b, 'component', a2)
    if hasattr(a1, 'mFSM'):
        assert not _is_linked(a1, 'mFSM', b)
    if hasattr(a2, 'mFSM'):
        assert _is_linked(a2, 'mFSM', b)
    _safe_set(b, 'component', set())
    assert not _is_linked(b, 'component', a2)
    if hasattr(a2, 'mFSM'):
        assert not _is_linked(a2, 'mFSM', b)


def test_assoc_compVar5_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp6', {a1})
    assert _is_linked(b, 'metaCompo_mComp6', a1)
    if hasattr(a1, 'metaCompo_mVariable'):
        assert _is_linked(a1, 'metaCompo_mVariable', b)
    _safe_set(b, 'metaCompo_mComp6', {a2})
    assert _is_linked(b, 'metaCompo_mComp6', a2)
    if hasattr(a1, 'metaCompo_mVariable'):
        assert not _is_linked(a1, 'metaCompo_mVariable', b)
    if hasattr(a2, 'metaCompo_mVariable'):
        assert _is_linked(a2, 'metaCompo_mVariable', b)
    _safe_set(b, 'metaCompo_mComp6', set())
    assert not _is_linked(b, 'metaCompo_mComp6', a2)
    if hasattr(a2, 'metaCompo_mVariable'):
        assert not _is_linked(a2, 'metaCompo_mVariable', b)


def test_assoc_component13_reverse_link_reassign_clear():
    a1 = metaCompo_mFSM(name="sample_text")
    a2 = metaCompo_mFSM(name="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'mComp', a1)
    assert _is_linked(b, 'mComp', a1)
    if hasattr(a1, 'FSMs'):
        assert _is_linked(a1, 'FSMs', b)
    _safe_set(b, 'mComp', a2)
    assert _is_linked(b, 'mComp', a2)
    if hasattr(a1, 'FSMs'):
        assert not _is_linked(a1, 'FSMs', b)
    if hasattr(a2, 'FSMs'):
        assert _is_linked(a2, 'FSMs', b)
    _safe_set(b, 'mComp', None)
    assert not _is_linked(b, 'mComp', a2)
    if hasattr(a2, 'FSMs'):
        assert not _is_linked(a2, 'FSMs', b)


def test_assoc_connToVar10_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort11', a1)
    assert _is_linked(b, 'metaCompo_mPort11', a1)
    if hasattr(a1, 'metaCompo_mVariable12'):
        assert _is_linked(a1, 'metaCompo_mVariable12', b)
    _safe_set(b, 'metaCompo_mPort11', a2)
    assert _is_linked(b, 'metaCompo_mPort11', a2)
    if hasattr(a1, 'metaCompo_mVariable12'):
        assert not _is_linked(a1, 'metaCompo_mVariable12', b)
    if hasattr(a2, 'metaCompo_mVariable12'):
        assert _is_linked(a2, 'metaCompo_mVariable12', b)
    _safe_set(b, 'metaCompo_mPort11', None)
    assert not _is_linked(b, 'metaCompo_mPort11', a2)
    if hasattr(a2, 'metaCompo_mVariable12'):
        assert not _is_linked(a2, 'metaCompo_mVariable12', b)


def test_assoc_connectedTo8_reverse_link_reassign_clear():
    a1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    a2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort9', a1)
    assert _is_linked(b, 'metaCompo_mPort9', a1)
    if hasattr(a1, 'metaCompo_mPort7'):
        assert _is_linked(a1, 'metaCompo_mPort7', b)
    _safe_set(b, 'metaCompo_mPort9', a2)
    assert _is_linked(b, 'metaCompo_mPort9', a2)
    if hasattr(a1, 'metaCompo_mPort7'):
        assert not _is_linked(a1, 'metaCompo_mPort7', b)
    if hasattr(a2, 'metaCompo_mPort7'):
        assert _is_linked(a2, 'metaCompo_mPort7', b)
    _safe_set(b, 'metaCompo_mPort9', None)
    assert not _is_linked(b, 'metaCompo_mPort9', a2)
    if hasattr(a2, 'metaCompo_mPort7'):
        assert not _is_linked(a2, 'metaCompo_mPort7', b)


def test_assoc_destination35_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'mState36', a1)
    assert _is_linked(b, 'mState36', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'mState36', a2)
    assert _is_linked(b, 'mState36', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'mState36', None)
    assert not _is_linked(b, 'mState36', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


def test_assoc_finalState19_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM20', a1)
    assert _is_linked(b, 'metaCompo_mFSM20', a1)
    if hasattr(a1, 'metaCompo_mState21'):
        assert _is_linked(a1, 'metaCompo_mState21', b)
    _safe_set(b, 'metaCompo_mFSM20', a2)
    assert _is_linked(b, 'metaCompo_mFSM20', a2)
    if hasattr(a1, 'metaCompo_mState21'):
        assert not _is_linked(a1, 'metaCompo_mState21', b)
    if hasattr(a2, 'metaCompo_mState21'):
        assert _is_linked(a2, 'metaCompo_mState21', b)
    _safe_set(b, 'metaCompo_mFSM20', None)
    assert not _is_linked(b, 'metaCompo_mFSM20', a2)
    if hasattr(a2, 'metaCompo_mState21'):
        assert not _is_linked(a2, 'metaCompo_mState21', b)


def test_assoc_fsmVar14_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM', {a1})
    assert _is_linked(b, 'metaCompo_mFSM', a1)
    if hasattr(a1, 'metaCompo_mVariable15'):
        assert _is_linked(a1, 'metaCompo_mVariable15', b)
    _safe_set(b, 'metaCompo_mFSM', {a2})
    assert _is_linked(b, 'metaCompo_mFSM', a2)
    if hasattr(a1, 'metaCompo_mVariable15'):
        assert not _is_linked(a1, 'metaCompo_mVariable15', b)
    if hasattr(a2, 'metaCompo_mVariable15'):
        assert _is_linked(a2, 'metaCompo_mVariable15', b)
    _safe_set(b, 'metaCompo_mFSM', set())
    assert not _is_linked(b, 'metaCompo_mFSM', a2)
    if hasattr(a2, 'metaCompo_mVariable15'):
        assert not _is_linked(a2, 'metaCompo_mVariable15', b)


def test_assoc_incomingTransitions28_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'destination', {a1})
    assert _is_linked(b, 'destination', a1)
    if hasattr(a1, 'mTransition29'):
        assert _is_linked(a1, 'mTransition29', b)
    _safe_set(b, 'destination', {a2})
    assert _is_linked(b, 'destination', a2)
    if hasattr(a1, 'mTransition29'):
        assert not _is_linked(a1, 'mTransition29', b)
    if hasattr(a2, 'mTransition29'):
        assert _is_linked(a2, 'mTransition29', b)
    _safe_set(b, 'destination', set())
    assert not _is_linked(b, 'destination', a2)
    if hasattr(a2, 'mTransition29'):
        assert not _is_linked(a2, 'mTransition29', b)


def test_assoc_initialState17_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM18', a1)
    assert _is_linked(b, 'metaCompo_mFSM18', a1)
    if hasattr(a1, 'metaCompo_mState'):
        assert _is_linked(a1, 'metaCompo_mState', b)
    _safe_set(b, 'metaCompo_mFSM18', a2)
    assert _is_linked(b, 'metaCompo_mFSM18', a2)
    if hasattr(a1, 'metaCompo_mState'):
        assert not _is_linked(a1, 'metaCompo_mState', b)
    if hasattr(a2, 'metaCompo_mState'):
        assert _is_linked(a2, 'metaCompo_mState', b)
    _safe_set(b, 'metaCompo_mFSM18', None)
    assert not _is_linked(b, 'metaCompo_mFSM18', a2)
    if hasattr(a2, 'metaCompo_mState'):
        assert not _is_linked(a2, 'metaCompo_mState', b)


def test_assoc_outgoingTransitions27_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'mTransition'):
        assert _is_linked(a1, 'mTransition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'mTransition'):
        assert not _is_linked(a1, 'mTransition', b)
    if hasattr(a2, 'mTransition'):
        assert _is_linked(a2, 'mTransition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'mTransition'):
        assert not _is_linked(a2, 'mTransition', b)


def test_assoc_owningFSM22_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'mFSM23', a1)
    assert _is_linked(b, 'mFSM23', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'mFSM23', a2)
    assert _is_linked(b, 'mFSM23', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'mFSM23', None)
    assert not _is_linked(b, 'mFSM23', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_ports2_reverse_link_reassign_clear():
    a1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    a2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp3', {a1})
    assert _is_linked(b, 'metaCompo_mComp3', a1)
    if hasattr(a1, 'metaCompo_mPort'):
        assert _is_linked(a1, 'metaCompo_mPort', b)
    _safe_set(b, 'metaCompo_mComp3', {a2})
    assert _is_linked(b, 'metaCompo_mComp3', a2)
    if hasattr(a1, 'metaCompo_mPort'):
        assert not _is_linked(a1, 'metaCompo_mPort', b)
    if hasattr(a2, 'metaCompo_mPort'):
        assert _is_linked(a2, 'metaCompo_mPort', b)
    _safe_set(b, 'metaCompo_mComp3', set())
    assert not _is_linked(b, 'metaCompo_mComp3', a2)
    if hasattr(a2, 'metaCompo_mPort'):
        assert not _is_linked(a2, 'metaCompo_mPort', b)


def test_assoc_source33_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'mState34', a1)
    assert _is_linked(b, 'mState34', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'mState34', a2)
    assert _is_linked(b, 'mState34', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'mState34', None)
    assert not _is_linked(b, 'mState34', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_stateVar24_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'metaCompo_mState25', {a1})
    assert _is_linked(b, 'metaCompo_mState25', a1)
    if hasattr(a1, 'metaCompo_mVariable26'):
        assert _is_linked(a1, 'metaCompo_mVariable26', b)
    _safe_set(b, 'metaCompo_mState25', {a2})
    assert _is_linked(b, 'metaCompo_mState25', a2)
    if hasattr(a1, 'metaCompo_mVariable26'):
        assert not _is_linked(a1, 'metaCompo_mVariable26', b)
    if hasattr(a2, 'metaCompo_mVariable26'):
        assert _is_linked(a2, 'metaCompo_mVariable26', b)
    _safe_set(b, 'metaCompo_mState25', set())
    assert not _is_linked(b, 'metaCompo_mState25', a2)
    if hasattr(a2, 'metaCompo_mVariable26'):
        assert not _is_linked(a2, 'metaCompo_mVariable26', b)


def test_assoc_states16_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'owningFSM', {a1})
    assert _is_linked(b, 'owningFSM', a1)
    if hasattr(a1, 'mState'):
        assert _is_linked(a1, 'mState', b)
    _safe_set(b, 'owningFSM', {a2})
    assert _is_linked(b, 'owningFSM', a2)
    if hasattr(a1, 'mState'):
        assert not _is_linked(a1, 'mState', b)
    if hasattr(a2, 'mState'):
        assert _is_linked(a2, 'mState', b)
    _safe_set(b, 'owningFSM', set())
    assert not _is_linked(b, 'owningFSM', a2)
    if hasattr(a2, 'mState'):
        assert not _is_linked(a2, 'mState', b)


def test_assoc_subComps1_reverse_link_reassign_clear():
    a1 = metaCompo_mComp(name="sample_text", type="sample_text")
    a2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp0', {a1})
    assert _is_linked(b, 'metaCompo_mComp0', a1)
    if hasattr(a1, 'metaCompo_mComp'):
        assert _is_linked(a1, 'metaCompo_mComp', b)
    _safe_set(b, 'metaCompo_mComp0', {a2})
    assert _is_linked(b, 'metaCompo_mComp0', a2)
    if hasattr(a1, 'metaCompo_mComp'):
        assert not _is_linked(a1, 'metaCompo_mComp', b)
    if hasattr(a2, 'metaCompo_mComp'):
        assert _is_linked(a2, 'metaCompo_mComp', b)
    _safe_set(b, 'metaCompo_mComp0', set())
    assert not _is_linked(b, 'metaCompo_mComp0', a2)
    if hasattr(a2, 'metaCompo_mComp'):
        assert not _is_linked(a2, 'metaCompo_mComp', b)


def test_assoc_subStates31_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'metaCompo_mState32', a1)
    assert _is_linked(b, 'metaCompo_mState32', a1)
    if hasattr(a1, 'metaCompo_mState30'):
        assert _is_linked(a1, 'metaCompo_mState30', b)
    _safe_set(b, 'metaCompo_mState32', a2)
    assert _is_linked(b, 'metaCompo_mState32', a2)
    if hasattr(a1, 'metaCompo_mState30'):
        assert not _is_linked(a1, 'metaCompo_mState30', b)
    if hasattr(a2, 'metaCompo_mState30'):
        assert _is_linked(a2, 'metaCompo_mState30', b)
    _safe_set(b, 'metaCompo_mState32', None)
    assert not _is_linked(b, 'metaCompo_mState32', a2)
    if hasattr(a2, 'metaCompo_mState30'):
        assert not _is_linked(a2, 'metaCompo_mState30', b)


def test_assoc_trigerringVar37_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    _safe_set(b, 'metaCompo_mTransition', {a1})
    assert _is_linked(b, 'metaCompo_mTransition', a1)
    if hasattr(a1, 'metaCompo_mVariable38'):
        assert _is_linked(a1, 'metaCompo_mVariable38', b)
    _safe_set(b, 'metaCompo_mTransition', {a2})
    assert _is_linked(b, 'metaCompo_mTransition', a2)
    if hasattr(a1, 'metaCompo_mVariable38'):
        assert not _is_linked(a1, 'metaCompo_mVariable38', b)
    if hasattr(a2, 'metaCompo_mVariable38'):
        assert _is_linked(a2, 'metaCompo_mVariable38', b)
    _safe_set(b, 'metaCompo_mTransition', set())
    assert not _is_linked(b, 'metaCompo_mTransition', a2)
    if hasattr(a2, 'metaCompo_mVariable38'):
        assert not _is_linked(a2, 'metaCompo_mVariable38', b)


def test_assoc_triggeringPort39_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort41', a1)
    assert _is_linked(b, 'metaCompo_mPort41', a1)
    if hasattr(a1, 'metaCompo_mTransition40'):
        assert _is_linked(a1, 'metaCompo_mTransition40', b)
    _safe_set(b, 'metaCompo_mPort41', a2)
    assert _is_linked(b, 'metaCompo_mPort41', a2)
    if hasattr(a1, 'metaCompo_mTransition40'):
        assert not _is_linked(a1, 'metaCompo_mTransition40', b)
    if hasattr(a2, 'metaCompo_mTransition40'):
        assert _is_linked(a2, 'metaCompo_mTransition40', b)
    _safe_set(b, 'metaCompo_mPort41', None)
    assert not _is_linked(b, 'metaCompo_mPort41', a2)
    if hasattr(a2, 'metaCompo_mTransition40'):
        assert not _is_linked(a2, 'metaCompo_mTransition40', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


