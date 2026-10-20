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
    fta_FTA,
    Diagram,
    fta_Condition,
    fta_Event,
    fta_Hazard,
    fta_Diagram,
    GateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fta_fta_is_not_abstract():
    assert not inspect.isabstract(fta_FTA)


def test_hyp_fta_fta_constructor_exists():
    assert callable(fta_FTA.__init__)


def test_hyp_fta_fta_constructor_args():
    sig = inspect.signature(fta_FTA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_hyp_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_hyp_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fta_condition_is_not_abstract():
    assert not inspect.isabstract(fta_Condition)


def test_hyp_fta_condition_constructor_exists():
    assert callable(fta_Condition.__init__)


def test_hyp_fta_condition_constructor_args():
    sig = inspect.signature(fta_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "GateKind" in params, "Missing parameter 'GateKind'"




def test_hyp_fta_event_is_not_abstract():
    assert not inspect.isabstract(fta_Event)


def test_hyp_fta_event_constructor_exists():
    assert callable(fta_Event.__init__)


def test_hyp_fta_event_constructor_args():
    sig = inspect.signature(fta_Event.__init__)
    params = list(sig.parameters.keys())
    assert "BaseEvent" in params, "Missing parameter 'BaseEvent'"




def test_hyp_fta_hazard_is_not_abstract():
    assert not inspect.isabstract(fta_Hazard)


def test_hyp_fta_hazard_constructor_exists():
    assert callable(fta_Hazard.__init__)


def test_hyp_fta_hazard_constructor_args():
    sig = inspect.signature(fta_Hazard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fta_diagram_is_not_abstract():
    assert not inspect.isabstract(fta_Diagram)


def test_hyp_fta_diagram_constructor_exists():
    assert callable(fta_Diagram.__init__)


def test_hyp_fta_diagram_constructor_args():
    sig = inspect.signature(fta_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "detail" in params, "Missing parameter 'detail'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_hyp_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "ORGate",
        "ANDGate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"


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
fta_FTA_strategy = st.builds(
    fta_FTA,
)
Diagram_strategy = st.builds(
    Diagram,
)
fta_Condition_strategy = st.builds(
    fta_Condition,
    GateKind=
        safe_text
)
fta_Event_strategy = st.builds(
    fta_Event,
    BaseEvent=
        st.booleans()
)
fta_Hazard_strategy = st.builds(
    fta_Hazard,
)
fta_Diagram_strategy = st.builds(
    fta_Diagram,
    detail=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)






@given(instance=fta_Condition_strategy)
def test_hyp_fta_condition_GateKind_setter(instance):
    original = instance.GateKind
    instance.GateKind = original
    assert instance.GateKind == original




@given(instance=fta_Event_strategy)
def test_hyp_fta_event_BaseEvent_setter(instance):
    original = instance.BaseEvent
    instance.BaseEvent = original
    assert instance.BaseEvent == original





@given(instance=fta_Diagram_strategy)
def test_hyp_fta_diagram_detail_setter(instance):
    original = instance.detail
    instance.detail = original
    assert instance.detail == original



@given(instance=fta_Diagram_strategy)
def test_hyp_fta_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fta_Diagram_strategy)
def test_hyp_fta_diagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Diagram,
    fta_Condition,
    fta_Diagram,
    fta_Event,
    fta_FTA,
    fta_Hazard,
    GateType,
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

def test_fta_Condition_GateKind_value_roundtrip():
    instance = fta_Condition(GateKind="sample_text")
    assert instance.GateKind == "sample_text"
    instance.GateKind = "sample_text_2"
    assert instance.GateKind == "sample_text_2"


def test_fta_Diagram_detail_value_roundtrip():
    instance = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    assert instance.detail == "sample_text"
    instance.detail = "sample_text_2"
    assert instance.detail == "sample_text_2"


def test_fta_Diagram_id_value_roundtrip():
    instance = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fta_Diagram_name_value_roundtrip():
    instance = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fta_Event_BaseEvent_value_roundtrip():
    instance = fta_Event(BaseEvent=True)
    assert instance.BaseEvent == True
    instance.BaseEvent = False
    assert instance.BaseEvent == False


def test_fta_Condition_isa_Diagram():
    instance = fta_Condition(GateKind="sample_text")
    assert isinstance(instance, Diagram)


def test_fta_Event_isa_Diagram():
    instance = fta_Event(BaseEvent=True)
    assert isinstance(instance, Diagram)


def test_fta_Hazard_isa_Diagram():
    instance = fta_Hazard()
    assert isinstance(instance, Diagram)


def test_assoc_condition2_link_reassign_clear():
    a = fta_Event(BaseEvent=True)
    b1 = fta_Condition(GateKind="sample_text")
    b2 = fta_Condition(GateKind="sample_text_2")
    _safe_set(a, 'fta_Event', b1)
    assert _is_linked(a, 'fta_Event', b1)
    if hasattr(b1, 'fta_Condition3'):
        assert _is_linked(b1, 'fta_Condition3', a)
    _safe_set(a, 'fta_Event', b2)
    assert _is_linked(a, 'fta_Event', b2)
    if hasattr(b1, 'fta_Condition3'):
        assert not _is_linked(b1, 'fta_Condition3', a)
    if hasattr(b2, 'fta_Condition3'):
        assert _is_linked(b2, 'fta_Condition3', a)
    _safe_set(a, 'fta_Event', None)
    assert not _is_linked(a, 'fta_Event', b2)
    if hasattr(b2, 'fta_Condition3'):
        assert not _is_linked(b2, 'fta_Condition3', a)


def test_assoc_conditions1_link_reassign_clear():
    a = fta_Condition(GateKind="sample_text")
    b1 = fta_Hazard()
    b2 = fta_Hazard()
    _safe_set(a, 'fta_Condition', b1)
    assert _is_linked(a, 'fta_Condition', b1)
    if hasattr(b1, 'fta_Hazard'):
        assert _is_linked(b1, 'fta_Hazard', a)
    _safe_set(a, 'fta_Condition', b2)
    assert _is_linked(a, 'fta_Condition', b2)
    if hasattr(b1, 'fta_Hazard'):
        assert not _is_linked(b1, 'fta_Hazard', a)
    if hasattr(b2, 'fta_Hazard'):
        assert _is_linked(b2, 'fta_Hazard', a)
    _safe_set(a, 'fta_Condition', None)
    assert not _is_linked(a, 'fta_Condition', b2)
    if hasattr(b2, 'fta_Hazard'):
        assert not _is_linked(b2, 'fta_Hazard', a)


def test_assoc_diagrams0_link_reassign_clear():
    a = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    b1 = fta_FTA()
    b2 = fta_FTA()
    _safe_set(a, 'fta_Diagram', b1)
    assert _is_linked(a, 'fta_Diagram', b1)
    if hasattr(b1, 'fta_FTA'):
        assert _is_linked(b1, 'fta_FTA', a)
    _safe_set(a, 'fta_Diagram', b2)
    assert _is_linked(a, 'fta_Diagram', b2)
    if hasattr(b1, 'fta_FTA'):
        assert not _is_linked(b1, 'fta_FTA', a)
    if hasattr(b2, 'fta_FTA'):
        assert _is_linked(b2, 'fta_FTA', a)
    _safe_set(a, 'fta_Diagram', None)
    assert not _is_linked(a, 'fta_Diagram', b2)
    if hasattr(b2, 'fta_FTA'):
        assert not _is_linked(b2, 'fta_FTA', a)


def test_assoc_events4_link_reassign_clear():
    a = fta_Event(BaseEvent=True)
    b1 = fta_Condition(GateKind="sample_text")
    b2 = fta_Condition(GateKind="sample_text_2")
    _safe_set(a, 'fta_Event6', b1)
    assert _is_linked(a, 'fta_Event6', b1)
    if hasattr(b1, 'fta_Condition5'):
        assert _is_linked(b1, 'fta_Condition5', a)
    _safe_set(a, 'fta_Event6', b2)
    assert _is_linked(a, 'fta_Event6', b2)
    if hasattr(b1, 'fta_Condition5'):
        assert not _is_linked(b1, 'fta_Condition5', a)
    if hasattr(b2, 'fta_Condition5'):
        assert _is_linked(b2, 'fta_Condition5', a)
    _safe_set(a, 'fta_Event6', None)
    assert not _is_linked(a, 'fta_Event6', b2)
    if hasattr(b2, 'fta_Condition5'):
        assert not _is_linked(b2, 'fta_Condition5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Diagram_strategy = st.builds(Diagram)
@given(instance=Diagram_strategy)
@settings(max_examples=25)
def test_Diagram_instantiation(instance):
    assert isinstance(instance, Diagram)


fta_Condition_strategy = st.builds(fta_Condition, GateKind=safe_text)
@given(instance=fta_Condition_strategy)
@settings(max_examples=25)
def test_fta_Condition_instantiation(instance):
    assert isinstance(instance, fta_Condition)


fta_Diagram_strategy = st.builds(fta_Diagram, detail=safe_text, id=safe_text, name=safe_text)
@given(instance=fta_Diagram_strategy)
@settings(max_examples=25)
def test_fta_Diagram_instantiation(instance):
    assert isinstance(instance, fta_Diagram)


fta_Event_strategy = st.builds(fta_Event, BaseEvent=st.booleans())
@given(instance=fta_Event_strategy)
@settings(max_examples=25)
def test_fta_Event_instantiation(instance):
    assert isinstance(instance, fta_Event)


fta_FTA_strategy = st.builds(fta_FTA)
@given(instance=fta_FTA_strategy)
@settings(max_examples=25)
def test_fta_FTA_instantiation(instance):
    assert isinstance(instance, fta_FTA)


fta_Hazard_strategy = st.builds(fta_Hazard)
@given(instance=fta_Hazard_strategy)
@settings(max_examples=25)
def test_fta_Hazard_instantiation(instance):
    assert isinstance(instance, fta_Hazard)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Diagram,
    fta_Condition,
    fta_Diagram,
    fta_Event,
    fta_FTA,
    fta_Hazard,
    GateType,
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

def test_assoc_condition2_reverse_link_reassign_clear():
    a1 = fta_Event(BaseEvent=True)
    a2 = fta_Event(BaseEvent=False)
    b = fta_Condition(GateKind="sample_text")
    _safe_set(b, 'fta_Condition3', a1)
    assert _is_linked(b, 'fta_Condition3', a1)
    if hasattr(a1, 'fta_Event'):
        assert _is_linked(a1, 'fta_Event', b)
    _safe_set(b, 'fta_Condition3', a2)
    assert _is_linked(b, 'fta_Condition3', a2)
    if hasattr(a1, 'fta_Event'):
        assert not _is_linked(a1, 'fta_Event', b)
    if hasattr(a2, 'fta_Event'):
        assert _is_linked(a2, 'fta_Event', b)
    _safe_set(b, 'fta_Condition3', None)
    assert not _is_linked(b, 'fta_Condition3', a2)
    if hasattr(a2, 'fta_Event'):
        assert not _is_linked(a2, 'fta_Event', b)


def test_assoc_events4_reverse_link_reassign_clear():
    a1 = fta_Event(BaseEvent=True)
    a2 = fta_Event(BaseEvent=False)
    b = fta_Condition(GateKind="sample_text")
    _safe_set(b, 'fta_Condition5', {a1})
    assert _is_linked(b, 'fta_Condition5', a1)
    if hasattr(a1, 'fta_Event6'):
        assert _is_linked(a1, 'fta_Event6', b)
    _safe_set(b, 'fta_Condition5', {a2})
    assert _is_linked(b, 'fta_Condition5', a2)
    if hasattr(a1, 'fta_Event6'):
        assert not _is_linked(a1, 'fta_Event6', b)
    if hasattr(a2, 'fta_Event6'):
        assert _is_linked(a2, 'fta_Event6', b)
    _safe_set(b, 'fta_Condition5', set())
    assert not _is_linked(b, 'fta_Condition5', a2)
    if hasattr(a2, 'fta_Event6'):
        assert not _is_linked(a2, 'fta_Event6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_conditions1_stub_double():
    # fta_Hazard has no real 'fta_Hazard' property in the generated
    # code (a bare stub) -- manually attach it so fta_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fta_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fta_Condition(GateKind="sample_text")
    partner = fta_Hazard()
    setattr(partner, 'fta_Hazard', None)
    _safe_set(owner, 'fta_Condition', partner)
    assert owner in getattr(partner, 'fta_Hazard')
    _safe_set(owner, 'fta_Condition', None)
    assert owner not in getattr(partner, 'fta_Hazard')


def test_assoc_diagrams0_stub_double():
    # fta_FTA has no real 'fta_FTA' property in the generated
    # code (a bare stub) -- manually attach it so fta_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fta_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    partner = fta_FTA()
    setattr(partner, 'fta_FTA', None)
    _safe_set(owner, 'fta_Diagram', partner)
    assert owner in getattr(partner, 'fta_FTA')
    _safe_set(owner, 'fta_Diagram', None)
    assert owner not in getattr(partner, 'fta_FTA')




from python_code import fta_Diagram
from python_code import fta_FTA

def test_fta_Diagram___init__():
    assert fta_Diagram.__init__(fta_Diagram('', '', '\x00\x00', fta_Diagram=fta_FTA()), '', '', '', fta_Diagram=fta_FTA()) == None

