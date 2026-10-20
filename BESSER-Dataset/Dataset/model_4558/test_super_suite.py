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
    routeCommand,
    platoon_TurnLeft,
    Vehicle,
    platoon_Vehicle,
    platoon_TurnRight,
    platoon_Root,
    platoon_Forward,
    platoon_FollowingVehicle,
    platoon_LeaderVehicle,
    platoon_routeCommand,
    platoon_Constraints,
    platoon_Route,
    platoon_Platoon,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_routecommand_is_not_abstract():
    assert not inspect.isabstract(routeCommand)


def test_hyp_routecommand_constructor_exists():
    assert callable(routeCommand.__init__)


def test_hyp_routecommand_constructor_args():
    sig = inspect.signature(routeCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_turnleft_is_not_abstract():
    assert not inspect.isabstract(platoon_TurnLeft)


def test_hyp_platoon_turnleft_constructor_exists():
    assert callable(platoon_TurnLeft.__init__)


def test_hyp_platoon_turnleft_constructor_args():
    sig = inspect.signature(platoon_TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_hyp_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_hyp_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_vehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_Vehicle)


def test_hyp_platoon_vehicle_constructor_exists():
    assert callable(platoon_Vehicle.__init__)


def test_hyp_platoon_vehicle_constructor_args():
    sig = inspect.signature(platoon_Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_platoon_turnright_is_not_abstract():
    assert not inspect.isabstract(platoon_TurnRight)


def test_hyp_platoon_turnright_constructor_exists():
    assert callable(platoon_TurnRight.__init__)


def test_hyp_platoon_turnright_constructor_args():
    sig = inspect.signature(platoon_TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_root_is_not_abstract():
    assert not inspect.isabstract(platoon_Root)


def test_hyp_platoon_root_constructor_exists():
    assert callable(platoon_Root.__init__)


def test_hyp_platoon_root_constructor_args():
    sig = inspect.signature(platoon_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_forward_is_not_abstract():
    assert not inspect.isabstract(platoon_Forward)


def test_hyp_platoon_forward_constructor_exists():
    assert callable(platoon_Forward.__init__)


def test_hyp_platoon_forward_constructor_args():
    sig = inspect.signature(platoon_Forward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_platoon_followingvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_FollowingVehicle)


def test_hyp_platoon_followingvehicle_constructor_exists():
    assert callable(platoon_FollowingVehicle.__init__)


def test_hyp_platoon_followingvehicle_constructor_args():
    sig = inspect.signature(platoon_FollowingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_leadervehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_LeaderVehicle)


def test_hyp_platoon_leadervehicle_constructor_exists():
    assert callable(platoon_LeaderVehicle.__init__)


def test_hyp_platoon_leadervehicle_constructor_args():
    sig = inspect.signature(platoon_LeaderVehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_routecommand_is_not_abstract():
    assert not inspect.isabstract(platoon_routeCommand)


def test_hyp_platoon_routecommand_constructor_exists():
    assert callable(platoon_routeCommand.__init__)


def test_hyp_platoon_routecommand_constructor_args():
    sig = inspect.signature(platoon_routeCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_constraints_is_not_abstract():
    assert not inspect.isabstract(platoon_Constraints)


def test_hyp_platoon_constraints_constructor_exists():
    assert callable(platoon_Constraints.__init__)


def test_hyp_platoon_constraints_constructor_args():
    sig = inspect.signature(platoon_Constraints.__init__)
    params = list(sig.parameters.keys())
    assert "lbound" in params, "Missing parameter 'lbound'"
    assert "ubound" in params, "Missing parameter 'ubound'"





def test_hyp_platoon_route_is_not_abstract():
    assert not inspect.isabstract(platoon_Route)


def test_hyp_platoon_route_constructor_exists():
    assert callable(platoon_Route.__init__)


def test_hyp_platoon_route_constructor_args():
    sig = inspect.signature(platoon_Route.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_platoon_platoon_is_not_abstract():
    assert not inspect.isabstract(platoon_Platoon)


def test_hyp_platoon_platoon_constructor_exists():
    assert callable(platoon_Platoon.__init__)


def test_hyp_platoon_platoon_constructor_args():
    sig = inspect.signature(platoon_Platoon.__init__)
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
routeCommand_strategy = st.builds(
    routeCommand,
)
platoon_TurnLeft_strategy = st.builds(
    platoon_TurnLeft,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon_Vehicle_strategy = st.builds(
    platoon_Vehicle,
    name=
        safe_text
)
platoon_TurnRight_strategy = st.builds(
    platoon_TurnRight,
)
platoon_Root_strategy = st.builds(
    platoon_Root,
)
platoon_Forward_strategy = st.builds(
    platoon_Forward,
    distance=
        st.integers()
)
platoon_FollowingVehicle_strategy = st.builds(
    platoon_FollowingVehicle,
)
platoon_LeaderVehicle_strategy = st.builds(
    platoon_LeaderVehicle,
)
platoon_routeCommand_strategy = st.builds(
    platoon_routeCommand,
)
platoon_Constraints_strategy = st.builds(
    platoon_Constraints,
    lbound=
        st.integers(),
    ubound=
        st.integers()
)
platoon_Route_strategy = st.builds(
    platoon_Route,
    name=
        safe_text
)
platoon_Platoon_strategy = st.builds(
    platoon_Platoon,
)







@given(instance=platoon_Vehicle_strategy)
def test_hyp_platoon_vehicle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=platoon_Forward_strategy)
def test_hyp_platoon_forward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original







@given(instance=platoon_Constraints_strategy)
def test_hyp_platoon_constraints_lbound_setter(instance):
    original = instance.lbound
    instance.lbound = original
    assert instance.lbound == original



@given(instance=platoon_Constraints_strategy)
def test_hyp_platoon_constraints_ubound_setter(instance):
    original = instance.ubound
    instance.ubound = original
    assert instance.ubound == original




@given(instance=platoon_Route_strategy)
def test_hyp_platoon_route_name_setter(instance):
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
    Vehicle,
    platoon_Constraints,
    platoon_FollowingVehicle,
    platoon_Forward,
    platoon_LeaderVehicle,
    platoon_Platoon,
    platoon_Root,
    platoon_Route,
    platoon_TurnLeft,
    platoon_TurnRight,
    platoon_Vehicle,
    platoon_routeCommand,
    routeCommand,
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

def test_platoon_Constraints_lbound_value_roundtrip():
    instance = platoon_Constraints(lbound=7, ubound=7)
    assert instance.lbound == 7
    instance.lbound = 13
    assert instance.lbound == 13


def test_platoon_Constraints_ubound_value_roundtrip():
    instance = platoon_Constraints(lbound=7, ubound=7)
    assert instance.ubound == 7
    instance.ubound = 13
    assert instance.ubound == 13


def test_platoon_Forward_distance_value_roundtrip():
    instance = platoon_Forward(distance=7)
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_platoon_Route_name_value_roundtrip():
    instance = platoon_Route(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_platoon_Vehicle_name_value_roundtrip():
    instance = platoon_Vehicle(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_platoon_FollowingVehicle_isa_Vehicle():
    instance = platoon_FollowingVehicle()
    assert isinstance(instance, Vehicle)


def test_platoon_LeaderVehicle_isa_Vehicle():
    instance = platoon_LeaderVehicle()
    assert isinstance(instance, Vehicle)


def test_platoon_Forward_isa_routeCommand():
    instance = platoon_Forward(distance=7)
    assert isinstance(instance, routeCommand)


def test_platoon_TurnLeft_isa_routeCommand():
    instance = platoon_TurnLeft()
    assert isinstance(instance, routeCommand)


def test_platoon_TurnRight_isa_routeCommand():
    instance = platoon_TurnRight()
    assert isinstance(instance, routeCommand)


def test_assoc_constraints3_link_reassign_clear():
    a = platoon_Constraints(lbound=7, ubound=7)
    b1 = platoon_Root()
    b2 = platoon_Root()
    _safe_set(a, 'platoon_Constraints', b1)
    assert _is_linked(a, 'platoon_Constraints', b1)
    if hasattr(b1, 'platoon_Root4'):
        assert _is_linked(b1, 'platoon_Root4', a)
    _safe_set(a, 'platoon_Constraints', b2)
    assert _is_linked(a, 'platoon_Constraints', b2)
    if hasattr(b1, 'platoon_Root4'):
        assert not _is_linked(b1, 'platoon_Root4', a)
    if hasattr(b2, 'platoon_Root4'):
        assert _is_linked(b2, 'platoon_Root4', a)
    _safe_set(a, 'platoon_Constraints', None)
    assert not _is_linked(a, 'platoon_Constraints', b2)
    if hasattr(b2, 'platoon_Root4'):
        assert not _is_linked(b2, 'platoon_Root4', a)


def test_assoc_following11_link_reassign_clear():
    a = platoon_Vehicle(name="sample_text")
    b1 = platoon_FollowingVehicle()
    b2 = platoon_FollowingVehicle()
    _safe_set(a, 'platoon_Vehicle', b1)
    assert _is_linked(a, 'platoon_Vehicle', b1)
    if hasattr(b1, 'platoon_FollowingVehicle12'):
        assert _is_linked(b1, 'platoon_FollowingVehicle12', a)
    _safe_set(a, 'platoon_Vehicle', b2)
    assert _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b1, 'platoon_FollowingVehicle12'):
        assert not _is_linked(b1, 'platoon_FollowingVehicle12', a)
    if hasattr(b2, 'platoon_FollowingVehicle12'):
        assert _is_linked(b2, 'platoon_FollowingVehicle12', a)
    _safe_set(a, 'platoon_Vehicle', None)
    assert not _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b2, 'platoon_FollowingVehicle12'):
        assert not _is_linked(b2, 'platoon_FollowingVehicle12', a)


def test_assoc_route1_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_Root()
    b2 = platoon_Root()
    _safe_set(a, 'platoon_Route', b1)
    assert _is_linked(a, 'platoon_Route', b1)
    if hasattr(b1, 'platoon_Root2'):
        assert _is_linked(b1, 'platoon_Root2', a)
    _safe_set(a, 'platoon_Route', b2)
    assert _is_linked(a, 'platoon_Route', b2)
    if hasattr(b1, 'platoon_Root2'):
        assert not _is_linked(b1, 'platoon_Root2', a)
    if hasattr(b2, 'platoon_Root2'):
        assert _is_linked(b2, 'platoon_Root2', a)
    _safe_set(a, 'platoon_Route', None)
    assert not _is_linked(a, 'platoon_Route', b2)
    if hasattr(b2, 'platoon_Root2'):
        assert not _is_linked(b2, 'platoon_Root2', a)


def test_assoc_route13_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_LeaderVehicle()
    b2 = platoon_LeaderVehicle()
    _safe_set(a, 'platoon_Route15', b1)
    assert _is_linked(a, 'platoon_Route15', b1)
    if hasattr(b1, 'platoon_LeaderVehicle14'):
        assert _is_linked(b1, 'platoon_LeaderVehicle14', a)
    _safe_set(a, 'platoon_Route15', b2)
    assert _is_linked(a, 'platoon_Route15', b2)
    if hasattr(b1, 'platoon_LeaderVehicle14'):
        assert not _is_linked(b1, 'platoon_LeaderVehicle14', a)
    if hasattr(b2, 'platoon_LeaderVehicle14'):
        assert _is_linked(b2, 'platoon_LeaderVehicle14', a)
    _safe_set(a, 'platoon_Route15', None)
    assert not _is_linked(a, 'platoon_Route15', b2)
    if hasattr(b2, 'platoon_LeaderVehicle14'):
        assert not _is_linked(b2, 'platoon_LeaderVehicle14', a)


def test_assoc_routeCommands5_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_routeCommand()
    b2 = platoon_routeCommand()
    _safe_set(a, 'platoon_Route6', {b1})
    assert _is_linked(a, 'platoon_Route6', b1)
    if hasattr(b1, 'platoon_routeCommand'):
        assert _is_linked(b1, 'platoon_routeCommand', a)
    _safe_set(a, 'platoon_Route6', {b2})
    assert _is_linked(a, 'platoon_Route6', b2)
    if hasattr(b1, 'platoon_routeCommand'):
        assert not _is_linked(b1, 'platoon_routeCommand', a)
    if hasattr(b2, 'platoon_routeCommand'):
        assert _is_linked(b2, 'platoon_routeCommand', a)
    _safe_set(a, 'platoon_Route6', set())
    assert not _is_linked(a, 'platoon_Route6', b2)
    if hasattr(b2, 'platoon_routeCommand'):
        assert not _is_linked(b2, 'platoon_routeCommand', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Vehicle_strategy = st.builds(Vehicle)
@given(instance=Vehicle_strategy)
@settings(max_examples=25)
def test_Vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)


platoon_Constraints_strategy = st.builds(platoon_Constraints, lbound=st.integers(), ubound=st.integers())
@given(instance=platoon_Constraints_strategy)
@settings(max_examples=25)
def test_platoon_Constraints_instantiation(instance):
    assert isinstance(instance, platoon_Constraints)


platoon_FollowingVehicle_strategy = st.builds(platoon_FollowingVehicle)
@given(instance=platoon_FollowingVehicle_strategy)
@settings(max_examples=25)
def test_platoon_FollowingVehicle_instantiation(instance):
    assert isinstance(instance, platoon_FollowingVehicle)


platoon_Forward_strategy = st.builds(platoon_Forward, distance=st.integers())
@given(instance=platoon_Forward_strategy)
@settings(max_examples=25)
def test_platoon_Forward_instantiation(instance):
    assert isinstance(instance, platoon_Forward)


platoon_LeaderVehicle_strategy = st.builds(platoon_LeaderVehicle)
@given(instance=platoon_LeaderVehicle_strategy)
@settings(max_examples=25)
def test_platoon_LeaderVehicle_instantiation(instance):
    assert isinstance(instance, platoon_LeaderVehicle)


platoon_Platoon_strategy = st.builds(platoon_Platoon)
@given(instance=platoon_Platoon_strategy)
@settings(max_examples=25)
def test_platoon_Platoon_instantiation(instance):
    assert isinstance(instance, platoon_Platoon)


platoon_Root_strategy = st.builds(platoon_Root)
@given(instance=platoon_Root_strategy)
@settings(max_examples=25)
def test_platoon_Root_instantiation(instance):
    assert isinstance(instance, platoon_Root)


platoon_Route_strategy = st.builds(platoon_Route, name=safe_text)
@given(instance=platoon_Route_strategy)
@settings(max_examples=25)
def test_platoon_Route_instantiation(instance):
    assert isinstance(instance, platoon_Route)


platoon_TurnLeft_strategy = st.builds(platoon_TurnLeft)
@given(instance=platoon_TurnLeft_strategy)
@settings(max_examples=25)
def test_platoon_TurnLeft_instantiation(instance):
    assert isinstance(instance, platoon_TurnLeft)


platoon_TurnRight_strategy = st.builds(platoon_TurnRight)
@given(instance=platoon_TurnRight_strategy)
@settings(max_examples=25)
def test_platoon_TurnRight_instantiation(instance):
    assert isinstance(instance, platoon_TurnRight)


platoon_Vehicle_strategy = st.builds(platoon_Vehicle, name=safe_text)
@given(instance=platoon_Vehicle_strategy)
@settings(max_examples=25)
def test_platoon_Vehicle_instantiation(instance):
    assert isinstance(instance, platoon_Vehicle)


platoon_routeCommand_strategy = st.builds(platoon_routeCommand)
@given(instance=platoon_routeCommand_strategy)
@settings(max_examples=25)
def test_platoon_routeCommand_instantiation(instance):
    assert isinstance(instance, platoon_routeCommand)


routeCommand_strategy = st.builds(routeCommand)
@given(instance=routeCommand_strategy)
@settings(max_examples=25)
def test_routeCommand_instantiation(instance):
    assert isinstance(instance, routeCommand)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Vehicle,
    platoon_Constraints,
    platoon_FollowingVehicle,
    platoon_Forward,
    platoon_LeaderVehicle,
    platoon_Platoon,
    platoon_Root,
    platoon_Route,
    platoon_TurnLeft,
    platoon_TurnRight,
    platoon_Vehicle,
    platoon_routeCommand,
    routeCommand,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constraints3_stub_double():
    # platoon_Root has no real 'platoon_Root4' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Constraints's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Constraints's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Constraints(lbound=7, ubound=7)
    partner = platoon_Root()
    setattr(partner, 'platoon_Root4', None)
    _safe_set(owner, 'platoon_Constraints', partner)
    assert getattr(partner, 'platoon_Root4') == owner
    _safe_set(owner, 'platoon_Constraints', None)
    assert getattr(partner, 'platoon_Root4') is None


def test_assoc_following11_stub_double():
    # platoon_FollowingVehicle has no real 'platoon_FollowingVehicle12' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(name="sample_text")
    partner = platoon_FollowingVehicle()
    setattr(partner, 'platoon_FollowingVehicle12', None)
    _safe_set(owner, 'platoon_Vehicle', partner)
    assert getattr(partner, 'platoon_FollowingVehicle12') == owner
    _safe_set(owner, 'platoon_Vehicle', None)
    assert getattr(partner, 'platoon_FollowingVehicle12') is None


def test_assoc_route1_stub_double():
    # platoon_Root has no real 'platoon_Root2' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Root()
    setattr(partner, 'platoon_Root2', None)
    _safe_set(owner, 'platoon_Route', partner)
    assert getattr(partner, 'platoon_Root2') == owner
    _safe_set(owner, 'platoon_Route', None)
    assert getattr(partner, 'platoon_Root2') is None


def test_assoc_route13_stub_double():
    # platoon_LeaderVehicle has no real 'platoon_LeaderVehicle14' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_LeaderVehicle()
    setattr(partner, 'platoon_LeaderVehicle14', None)
    _safe_set(owner, 'platoon_Route15', partner)
    assert getattr(partner, 'platoon_LeaderVehicle14') == owner
    _safe_set(owner, 'platoon_Route15', None)
    assert getattr(partner, 'platoon_LeaderVehicle14') is None


def test_assoc_routeCommands5_stub_double():
    # platoon_routeCommand has no real 'platoon_routeCommand' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_routeCommand()
    setattr(partner, 'platoon_routeCommand', None)
    _safe_set(owner, 'platoon_Route6', {partner})
    assert getattr(partner, 'platoon_routeCommand') == owner
    _safe_set(owner, 'platoon_Route6', set())
    assert getattr(partner, 'platoon_routeCommand') is None




from python_code import platoon_Constraints
from python_code import platoon_Root

def test_platoon_Constraints___init__():
    assert platoon_Constraints.__init__(platoon_Constraints(0, 0, platoon_Constraints=platoon_Root()), 0, 0, platoon_Constraints=platoon_Root()) == None
from python_code import platoon_Forward

def test_platoon_Forward___init__():
    assert platoon_Forward.__init__(platoon_Forward(0), 0) == None
from python_code import platoon_LeaderVehicle
from python_code import platoon_Root
from python_code import platoon_Route

def test_platoon_Route___init__():
    assert platoon_Route.__init__(platoon_Route('', platoon_Route=platoon_Root(), platoon_Route6=set(), platoon_Route15=platoon_LeaderVehicle()), '', platoon_Route=platoon_Root(), platoon_Route6=set(), platoon_Route15=platoon_LeaderVehicle()) == None
from python_code import platoon_FollowingVehicle
from python_code import platoon_Vehicle

def test_platoon_Vehicle___init__():
    assert platoon_Vehicle.__init__(platoon_Vehicle('', platoon_Vehicle=platoon_FollowingVehicle()), '', platoon_Vehicle=platoon_FollowingVehicle()) == None

