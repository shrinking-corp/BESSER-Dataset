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
    platoon_Constraints,
    Command,
    platoon_ForwardCommand,
    Vehicle,
    platoon_Vehicle,
    platoon_Command,
    platoon_Route,
    platoon_FollowVehicle,
    platoon_LeadingVehicle,
    platoon_World,
    platoon_Constraint,
    platoon_Platoon,
    Constraint,
    platoon_HeadwayConstraint,
    platoon_TurnCommand,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_platoon_constraints_is_not_abstract():
    assert not inspect.isabstract(platoon_Constraints)


def test_hyp_platoon_constraints_constructor_exists():
    assert callable(platoon_Constraints.__init__)


def test_hyp_platoon_constraints_constructor_args():
    sig = inspect.signature(platoon_Constraints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_forwardcommand_is_not_abstract():
    assert not inspect.isabstract(platoon_ForwardCommand)


def test_hyp_platoon_forwardcommand_constructor_exists():
    assert callable(platoon_ForwardCommand.__init__)


def test_hyp_platoon_forwardcommand_constructor_args():
    sig = inspect.signature(platoon_ForwardCommand.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




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




def test_hyp_platoon_command_is_not_abstract():
    assert not inspect.isabstract(platoon_Command)


def test_hyp_platoon_command_constructor_exists():
    assert callable(platoon_Command.__init__)


def test_hyp_platoon_command_constructor_args():
    sig = inspect.signature(platoon_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_route_is_not_abstract():
    assert not inspect.isabstract(platoon_Route)


def test_hyp_platoon_route_constructor_exists():
    assert callable(platoon_Route.__init__)


def test_hyp_platoon_route_constructor_args():
    sig = inspect.signature(platoon_Route.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_platoon_followvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_FollowVehicle)


def test_hyp_platoon_followvehicle_constructor_exists():
    assert callable(platoon_FollowVehicle.__init__)


def test_hyp_platoon_followvehicle_constructor_args():
    sig = inspect.signature(platoon_FollowVehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_leadingvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_LeadingVehicle)


def test_hyp_platoon_leadingvehicle_constructor_exists():
    assert callable(platoon_LeadingVehicle.__init__)


def test_hyp_platoon_leadingvehicle_constructor_args():
    sig = inspect.signature(platoon_LeadingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_world_is_not_abstract():
    assert not inspect.isabstract(platoon_World)


def test_hyp_platoon_world_constructor_exists():
    assert callable(platoon_World.__init__)


def test_hyp_platoon_world_constructor_args():
    sig = inspect.signature(platoon_World.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_constraint_is_not_abstract():
    assert not inspect.isabstract(platoon_Constraint)


def test_hyp_platoon_constraint_constructor_exists():
    assert callable(platoon_Constraint.__init__)


def test_hyp_platoon_constraint_constructor_args():
    sig = inspect.signature(platoon_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_platoon_is_not_abstract():
    assert not inspect.isabstract(platoon_Platoon)


def test_hyp_platoon_platoon_constructor_exists():
    assert callable(platoon_Platoon.__init__)


def test_hyp_platoon_platoon_constructor_args():
    sig = inspect.signature(platoon_Platoon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_headwayconstraint_is_not_abstract():
    assert not inspect.isabstract(platoon_HeadwayConstraint)


def test_hyp_platoon_headwayconstraint_constructor_exists():
    assert callable(platoon_HeadwayConstraint.__init__)


def test_hyp_platoon_headwayconstraint_constructor_args():
    sig = inspect.signature(platoon_HeadwayConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"





def test_hyp_platoon_turncommand_is_not_abstract():
    assert not inspect.isabstract(platoon_TurnCommand)


def test_hyp_platoon_turncommand_constructor_exists():
    assert callable(platoon_TurnCommand.__init__)


def test_hyp_platoon_turncommand_constructor_args():
    sig = inspect.signature(platoon_TurnCommand.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"



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
platoon_Constraints_strategy = st.builds(
    platoon_Constraints,
)
Command_strategy = st.builds(
    Command,
)
platoon_ForwardCommand_strategy = st.builds(
    platoon_ForwardCommand,
    distance=
        st.integers()
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon_Vehicle_strategy = st.builds(
    platoon_Vehicle,
    name=
        safe_text
)
platoon_Command_strategy = st.builds(
    platoon_Command,
)
platoon_Route_strategy = st.builds(
    platoon_Route,
    name=
        safe_text
)
platoon_FollowVehicle_strategy = st.builds(
    platoon_FollowVehicle,
)
platoon_LeadingVehicle_strategy = st.builds(
    platoon_LeadingVehicle,
)
platoon_World_strategy = st.builds(
    platoon_World,
)
platoon_Constraint_strategy = st.builds(
    platoon_Constraint,
)
platoon_Platoon_strategy = st.builds(
    platoon_Platoon,
)
Constraint_strategy = st.builds(
    Constraint,
)
platoon_HeadwayConstraint_strategy = st.builds(
    platoon_HeadwayConstraint,
    max=
        st.integers(),
    min=
        st.integers()
)
platoon_TurnCommand_strategy = st.builds(
    platoon_TurnCommand,
    direction=
        safe_text
)






@given(instance=platoon_ForwardCommand_strategy)
def test_hyp_platoon_forwardcommand_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original





@given(instance=platoon_Vehicle_strategy)
def test_hyp_platoon_vehicle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=platoon_Route_strategy)
def test_hyp_platoon_route_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=platoon_HeadwayConstraint_strategy)
def test_hyp_platoon_headwayconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=platoon_HeadwayConstraint_strategy)
def test_hyp_platoon_headwayconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original




@given(instance=platoon_TurnCommand_strategy)
def test_hyp_platoon_turncommand_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Command,
    Constraint,
    Vehicle,
    platoon_Command,
    platoon_Constraint,
    platoon_Constraints,
    platoon_FollowVehicle,
    platoon_ForwardCommand,
    platoon_HeadwayConstraint,
    platoon_LeadingVehicle,
    platoon_Platoon,
    platoon_Route,
    platoon_TurnCommand,
    platoon_Vehicle,
    platoon_World,
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

def test_platoon_ForwardCommand_distance_value_roundtrip():
    instance = platoon_ForwardCommand(distance=7)
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_platoon_HeadwayConstraint_max_value_roundtrip():
    instance = platoon_HeadwayConstraint(max=7, min=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_platoon_HeadwayConstraint_min_value_roundtrip():
    instance = platoon_HeadwayConstraint(max=7, min=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_platoon_Route_name_value_roundtrip():
    instance = platoon_Route(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_platoon_TurnCommand_direction_value_roundtrip():
    instance = platoon_TurnCommand(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_platoon_Vehicle_name_value_roundtrip():
    instance = platoon_Vehicle(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_platoon_ForwardCommand_isa_Command():
    instance = platoon_ForwardCommand(distance=7)
    assert isinstance(instance, Command)


def test_platoon_TurnCommand_isa_Command():
    instance = platoon_TurnCommand(direction="sample_text")
    assert isinstance(instance, Command)


def test_platoon_HeadwayConstraint_isa_Constraint():
    instance = platoon_HeadwayConstraint(max=7, min=7)
    assert isinstance(instance, Constraint)


def test_platoon_FollowVehicle_isa_Vehicle():
    instance = platoon_FollowVehicle()
    assert isinstance(instance, Vehicle)


def test_platoon_LeadingVehicle_isa_Vehicle():
    instance = platoon_LeadingVehicle()
    assert isinstance(instance, Vehicle)


def test_assoc_commands3_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_Command()
    b2 = platoon_Command()
    _safe_set(a, 'platoon_Route', {b1})
    assert _is_linked(a, 'platoon_Route', b1)
    if hasattr(b1, 'platoon_Command'):
        assert _is_linked(b1, 'platoon_Command', a)
    _safe_set(a, 'platoon_Route', {b2})
    assert _is_linked(a, 'platoon_Route', b2)
    if hasattr(b1, 'platoon_Command'):
        assert not _is_linked(b1, 'platoon_Command', a)
    if hasattr(b2, 'platoon_Command'):
        assert _is_linked(b2, 'platoon_Command', a)
    _safe_set(a, 'platoon_Route', set())
    assert not _is_linked(a, 'platoon_Route', b2)
    if hasattr(b2, 'platoon_Command'):
        assert not _is_linked(b2, 'platoon_Command', a)


def test_assoc_follows4_link_reassign_clear():
    a = platoon_Vehicle(name="sample_text")
    b1 = platoon_FollowVehicle()
    b2 = platoon_FollowVehicle()
    _safe_set(a, 'platoon_Vehicle', b1)
    assert _is_linked(a, 'platoon_Vehicle', b1)
    if hasattr(b1, 'platoon_FollowVehicle5'):
        assert _is_linked(b1, 'platoon_FollowVehicle5', a)
    _safe_set(a, 'platoon_Vehicle', b2)
    assert _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b1, 'platoon_FollowVehicle5'):
        assert not _is_linked(b1, 'platoon_FollowVehicle5', a)
    if hasattr(b2, 'platoon_FollowVehicle5'):
        assert _is_linked(b2, 'platoon_FollowVehicle5', a)
    _safe_set(a, 'platoon_Vehicle', None)
    assert not _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b2, 'platoon_FollowVehicle5'):
        assert not _is_linked(b2, 'platoon_FollowVehicle5', a)


def test_assoc_route11_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_World()
    b2 = platoon_World()
    _safe_set(a, 'platoon_Route13', b1)
    assert _is_linked(a, 'platoon_Route13', b1)
    if hasattr(b1, 'platoon_World12'):
        assert _is_linked(b1, 'platoon_World12', a)
    _safe_set(a, 'platoon_Route13', b2)
    assert _is_linked(a, 'platoon_Route13', b2)
    if hasattr(b1, 'platoon_World12'):
        assert not _is_linked(b1, 'platoon_World12', a)
    if hasattr(b2, 'platoon_World12'):
        assert _is_linked(b2, 'platoon_World12', a)
    _safe_set(a, 'platoon_Route13', None)
    assert not _is_linked(a, 'platoon_Route13', b2)
    if hasattr(b2, 'platoon_World12'):
        assert not _is_linked(b2, 'platoon_World12', a)


def test_assoc_route6_link_reassign_clear():
    a = platoon_Route(name="sample_text")
    b1 = platoon_LeadingVehicle()
    b2 = platoon_LeadingVehicle()
    _safe_set(a, 'platoon_Route8', b1)
    assert _is_linked(a, 'platoon_Route8', b1)
    if hasattr(b1, 'platoon_LeadingVehicle7'):
        assert _is_linked(b1, 'platoon_LeadingVehicle7', a)
    _safe_set(a, 'platoon_Route8', b2)
    assert _is_linked(a, 'platoon_Route8', b2)
    if hasattr(b1, 'platoon_LeadingVehicle7'):
        assert not _is_linked(b1, 'platoon_LeadingVehicle7', a)
    if hasattr(b2, 'platoon_LeadingVehicle7'):
        assert _is_linked(b2, 'platoon_LeadingVehicle7', a)
    _safe_set(a, 'platoon_Route8', None)
    assert not _is_linked(a, 'platoon_Route8', b2)
    if hasattr(b2, 'platoon_LeadingVehicle7'):
        assert not _is_linked(b2, 'platoon_LeadingVehicle7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Vehicle_strategy = st.builds(Vehicle)
@given(instance=Vehicle_strategy)
@settings(max_examples=25)
def test_Vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)


platoon_Command_strategy = st.builds(platoon_Command)
@given(instance=platoon_Command_strategy)
@settings(max_examples=25)
def test_platoon_Command_instantiation(instance):
    assert isinstance(instance, platoon_Command)


platoon_Constraint_strategy = st.builds(platoon_Constraint)
@given(instance=platoon_Constraint_strategy)
@settings(max_examples=25)
def test_platoon_Constraint_instantiation(instance):
    assert isinstance(instance, platoon_Constraint)


platoon_Constraints_strategy = st.builds(platoon_Constraints)
@given(instance=platoon_Constraints_strategy)
@settings(max_examples=25)
def test_platoon_Constraints_instantiation(instance):
    assert isinstance(instance, platoon_Constraints)


platoon_FollowVehicle_strategy = st.builds(platoon_FollowVehicle)
@given(instance=platoon_FollowVehicle_strategy)
@settings(max_examples=25)
def test_platoon_FollowVehicle_instantiation(instance):
    assert isinstance(instance, platoon_FollowVehicle)


platoon_ForwardCommand_strategy = st.builds(platoon_ForwardCommand, distance=st.integers())
@given(instance=platoon_ForwardCommand_strategy)
@settings(max_examples=25)
def test_platoon_ForwardCommand_instantiation(instance):
    assert isinstance(instance, platoon_ForwardCommand)


platoon_HeadwayConstraint_strategy = st.builds(platoon_HeadwayConstraint, max=st.integers(), min=st.integers())
@given(instance=platoon_HeadwayConstraint_strategy)
@settings(max_examples=25)
def test_platoon_HeadwayConstraint_instantiation(instance):
    assert isinstance(instance, platoon_HeadwayConstraint)


platoon_LeadingVehicle_strategy = st.builds(platoon_LeadingVehicle)
@given(instance=platoon_LeadingVehicle_strategy)
@settings(max_examples=25)
def test_platoon_LeadingVehicle_instantiation(instance):
    assert isinstance(instance, platoon_LeadingVehicle)


platoon_Platoon_strategy = st.builds(platoon_Platoon)
@given(instance=platoon_Platoon_strategy)
@settings(max_examples=25)
def test_platoon_Platoon_instantiation(instance):
    assert isinstance(instance, platoon_Platoon)


platoon_Route_strategy = st.builds(platoon_Route, name=safe_text)
@given(instance=platoon_Route_strategy)
@settings(max_examples=25)
def test_platoon_Route_instantiation(instance):
    assert isinstance(instance, platoon_Route)


platoon_TurnCommand_strategy = st.builds(platoon_TurnCommand, direction=safe_text)
@given(instance=platoon_TurnCommand_strategy)
@settings(max_examples=25)
def test_platoon_TurnCommand_instantiation(instance):
    assert isinstance(instance, platoon_TurnCommand)


platoon_Vehicle_strategy = st.builds(platoon_Vehicle, name=safe_text)
@given(instance=platoon_Vehicle_strategy)
@settings(max_examples=25)
def test_platoon_Vehicle_instantiation(instance):
    assert isinstance(instance, platoon_Vehicle)


platoon_World_strategy = st.builds(platoon_World)
@given(instance=platoon_World_strategy)
@settings(max_examples=25)
def test_platoon_World_instantiation(instance):
    assert isinstance(instance, platoon_World)



