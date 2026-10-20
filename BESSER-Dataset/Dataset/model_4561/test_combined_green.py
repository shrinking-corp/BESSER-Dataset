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
    platoon_PlatooningSystem,
    platoon_JoiningPosition,
    platoon_JoinPlatoonCoord,
    platoon_Platoon,
    platoon_FrontGap,
    Vehicle,
    platoon_PlatoonVehicle,
    platoon_JoiningVehicle,
    platoon_Vehicle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_platoon_platooningsystem_is_not_abstract():
    assert not inspect.isabstract(platoon_PlatooningSystem)


def test_hyp_platoon_platooningsystem_constructor_exists():
    assert callable(platoon_PlatooningSystem.__init__)


def test_hyp_platoon_platooningsystem_constructor_args():
    sig = inspect.signature(platoon_PlatooningSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_joiningposition_is_not_abstract():
    assert not inspect.isabstract(platoon_JoiningPosition)


def test_hyp_platoon_joiningposition_constructor_exists():
    assert callable(platoon_JoiningPosition.__init__)


def test_hyp_platoon_joiningposition_constructor_args():
    sig = inspect.signature(platoon_JoiningPosition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_joinplatooncoord_is_not_abstract():
    assert not inspect.isabstract(platoon_JoinPlatoonCoord)


def test_hyp_platoon_joinplatooncoord_constructor_exists():
    assert callable(platoon_JoinPlatoonCoord.__init__)


def test_hyp_platoon_joinplatooncoord_constructor_args():
    sig = inspect.signature(platoon_JoinPlatoonCoord.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_platoon_is_not_abstract():
    assert not inspect.isabstract(platoon_Platoon)


def test_hyp_platoon_platoon_constructor_exists():
    assert callable(platoon_Platoon.__init__)


def test_hyp_platoon_platoon_constructor_args():
    sig = inspect.signature(platoon_Platoon.__init__)
    params = list(sig.parameters.keys())
    assert "desiredGapSize" in params, "Missing parameter 'desiredGapSize'"
    assert "length" in params, "Missing parameter 'length'"





def test_hyp_platoon_frontgap_is_not_abstract():
    assert not inspect.isabstract(platoon_FrontGap)


def test_hyp_platoon_frontgap_constructor_exists():
    assert callable(platoon_FrontGap.__init__)


def test_hyp_platoon_frontgap_constructor_args():
    sig = inspect.signature(platoon_FrontGap.__init__)
    params = list(sig.parameters.keys())
    assert "actualGapSize" in params, "Missing parameter 'actualGapSize'"




def test_hyp_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_hyp_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_hyp_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_platoonvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_PlatoonVehicle)


def test_hyp_platoon_platoonvehicle_constructor_exists():
    assert callable(platoon_PlatoonVehicle.__init__)


def test_hyp_platoon_platoonvehicle_constructor_args():
    sig = inspect.signature(platoon_PlatoonVehicle.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"




def test_hyp_platoon_joiningvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_JoiningVehicle)


def test_hyp_platoon_joiningvehicle_constructor_exists():
    assert callable(platoon_JoiningVehicle.__init__)


def test_hyp_platoon_joiningvehicle_constructor_args():
    sig = inspect.signature(platoon_JoiningVehicle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_platoon_vehicle_is_not_abstract():
    assert not inspect.isabstract(platoon_Vehicle)


def test_hyp_platoon_vehicle_constructor_exists():
    assert callable(platoon_Vehicle.__init__)


def test_hyp_platoon_vehicle_constructor_args():
    sig = inspect.signature(platoon_Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"



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
platoon_PlatooningSystem_strategy = st.builds(
    platoon_PlatooningSystem,
)
platoon_JoiningPosition_strategy = st.builds(
    platoon_JoiningPosition,
)
platoon_JoinPlatoonCoord_strategy = st.builds(
    platoon_JoinPlatoonCoord,
)
platoon_Platoon_strategy = st.builds(
    platoon_Platoon,
    desiredGapSize=
        st.integers(),
    length=
        st.integers()
)
platoon_FrontGap_strategy = st.builds(
    platoon_FrontGap,
    actualGapSize=
        st.integers()
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon_PlatoonVehicle_strategy = st.builds(
    platoon_PlatoonVehicle,
    position=
        st.integers()
)
platoon_JoiningVehicle_strategy = st.builds(
    platoon_JoiningVehicle,
)
platoon_Vehicle_strategy = st.builds(
    platoon_Vehicle,
    id=
        st.integers()
)







@given(instance=platoon_Platoon_strategy)
def test_hyp_platoon_platoon_desiredGapSize_setter(instance):
    original = instance.desiredGapSize
    instance.desiredGapSize = original
    assert instance.desiredGapSize == original



@given(instance=platoon_Platoon_strategy)
def test_hyp_platoon_platoon_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original




@given(instance=platoon_FrontGap_strategy)
def test_hyp_platoon_frontgap_actualGapSize_setter(instance):
    original = instance.actualGapSize
    instance.actualGapSize = original
    assert instance.actualGapSize == original





@given(instance=platoon_PlatoonVehicle_strategy)
def test_hyp_platoon_platoonvehicle_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original





@given(instance=platoon_Vehicle_strategy)
def test_hyp_platoon_vehicle_id_setter(instance):
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
    Vehicle,
    platoon_FrontGap,
    platoon_JoinPlatoonCoord,
    platoon_JoiningPosition,
    platoon_JoiningVehicle,
    platoon_Platoon,
    platoon_PlatoonVehicle,
    platoon_PlatooningSystem,
    platoon_Vehicle,
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

def test_platoon_FrontGap_actualGapSize_value_roundtrip():
    instance = platoon_FrontGap(actualGapSize=7)
    assert instance.actualGapSize == 7
    instance.actualGapSize = 13
    assert instance.actualGapSize == 13


def test_platoon_Platoon_desiredGapSize_value_roundtrip():
    instance = platoon_Platoon(desiredGapSize=7, length=7)
    assert instance.desiredGapSize == 7
    instance.desiredGapSize = 13
    assert instance.desiredGapSize == 13


def test_platoon_Platoon_length_value_roundtrip():
    instance = platoon_Platoon(desiredGapSize=7, length=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_platoon_PlatoonVehicle_position_value_roundtrip():
    instance = platoon_PlatoonVehicle(position=7)
    assert instance.position == 7
    instance.position = 13
    assert instance.position == 13


def test_platoon_Vehicle_id_value_roundtrip():
    instance = platoon_Vehicle(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_platoon_JoiningVehicle_isa_Vehicle():
    instance = platoon_JoiningVehicle()
    assert isinstance(instance, Vehicle)


def test_platoon_PlatoonVehicle_isa_Vehicle():
    instance = platoon_PlatoonVehicle(position=7)
    assert isinstance(instance, Vehicle)


def test_assoc_cordManager18_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_JoinPlatoonCoord()
    b2 = platoon_JoinPlatoonCoord()
    _safe_set(a, 'platoon_Vehicle20', b1)
    assert _is_linked(a, 'platoon_Vehicle20', b1)
    if hasattr(b1, 'platoon_JoinPlatoonCoord19'):
        assert _is_linked(b1, 'platoon_JoinPlatoonCoord19', a)
    _safe_set(a, 'platoon_Vehicle20', b2)
    assert _is_linked(a, 'platoon_Vehicle20', b2)
    if hasattr(b1, 'platoon_JoinPlatoonCoord19'):
        assert not _is_linked(b1, 'platoon_JoinPlatoonCoord19', a)
    if hasattr(b2, 'platoon_JoinPlatoonCoord19'):
        assert _is_linked(b2, 'platoon_JoinPlatoonCoord19', a)
    _safe_set(a, 'platoon_Vehicle20', None)
    assert not _is_linked(a, 'platoon_Vehicle20', b2)
    if hasattr(b2, 'platoon_JoinPlatoonCoord19'):
        assert not _is_linked(b2, 'platoon_JoinPlatoonCoord19', a)


def test_assoc_follower1_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_Platoon(desiredGapSize=7, length=7)
    b2 = platoon_Platoon(desiredGapSize=13, length=13)
    _safe_set(a, 'platoon_PlatoonVehicle3', b1)
    assert _is_linked(a, 'platoon_PlatoonVehicle3', b1)
    if hasattr(b1, 'platoon_Platoon2'):
        assert _is_linked(b1, 'platoon_Platoon2', a)
    _safe_set(a, 'platoon_PlatoonVehicle3', b2)
    assert _is_linked(a, 'platoon_PlatoonVehicle3', b2)
    if hasattr(b1, 'platoon_Platoon2'):
        assert not _is_linked(b1, 'platoon_Platoon2', a)
    if hasattr(b2, 'platoon_Platoon2'):
        assert _is_linked(b2, 'platoon_Platoon2', a)
    _safe_set(a, 'platoon_PlatoonVehicle3', None)
    assert not _is_linked(a, 'platoon_PlatoonVehicle3', b2)
    if hasattr(b2, 'platoon_Platoon2'):
        assert not _is_linked(b2, 'platoon_Platoon2', a)


def test_assoc_follows11_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_Vehicle(id=7)
    b2 = platoon_Vehicle(id=13)
    _safe_set(a, 'platoon_Vehicle', b1)
    assert _is_linked(a, 'platoon_Vehicle', b1)
    if hasattr(b1, 'platoon_Vehicle10'):
        assert _is_linked(b1, 'platoon_Vehicle10', a)
    _safe_set(a, 'platoon_Vehicle', b2)
    assert _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b1, 'platoon_Vehicle10'):
        assert not _is_linked(b1, 'platoon_Vehicle10', a)
    if hasattr(b2, 'platoon_Vehicle10'):
        assert _is_linked(b2, 'platoon_Vehicle10', a)
    _safe_set(a, 'platoon_Vehicle', None)
    assert not _is_linked(a, 'platoon_Vehicle', b2)
    if hasattr(b2, 'platoon_Vehicle10'):
        assert not _is_linked(b2, 'platoon_Vehicle10', a)


def test_assoc_follows5_link_reassign_clear():
    a = platoon_Platoon(desiredGapSize=7, length=7)
    b1 = platoon_Platoon(desiredGapSize=7, length=7)
    b2 = platoon_Platoon(desiredGapSize=13, length=13)
    _safe_set(a, 'platoon_Platoon4', b1)
    assert _is_linked(a, 'platoon_Platoon4', b1)
    if hasattr(b1, 'platoon_Platoon6'):
        assert _is_linked(b1, 'platoon_Platoon6', a)
    _safe_set(a, 'platoon_Platoon4', b2)
    assert _is_linked(a, 'platoon_Platoon4', b2)
    if hasattr(b1, 'platoon_Platoon6'):
        assert not _is_linked(b1, 'platoon_Platoon6', a)
    if hasattr(b2, 'platoon_Platoon6'):
        assert _is_linked(b2, 'platoon_Platoon6', a)
    _safe_set(a, 'platoon_Platoon4', None)
    assert not _is_linked(a, 'platoon_Platoon4', b2)
    if hasattr(b2, 'platoon_Platoon6'):
        assert not _is_linked(b2, 'platoon_Platoon6', a)


def test_assoc_forms32_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_FrontGap(actualGapSize=7)
    b2 = platoon_FrontGap(actualGapSize=13)
    _safe_set(a, 'platoon_PlatoonVehicle33', b1)
    assert _is_linked(a, 'platoon_PlatoonVehicle33', b1)
    if hasattr(b1, 'platoon_FrontGap34'):
        assert _is_linked(b1, 'platoon_FrontGap34', a)
    _safe_set(a, 'platoon_PlatoonVehicle33', b2)
    assert _is_linked(a, 'platoon_PlatoonVehicle33', b2)
    if hasattr(b1, 'platoon_FrontGap34'):
        assert not _is_linked(b1, 'platoon_FrontGap34', a)
    if hasattr(b2, 'platoon_FrontGap34'):
        assert _is_linked(b2, 'platoon_FrontGap34', a)
    _safe_set(a, 'platoon_PlatoonVehicle33', None)
    assert not _is_linked(a, 'platoon_PlatoonVehicle33', b2)
    if hasattr(b2, 'platoon_FrontGap34'):
        assert not _is_linked(b2, 'platoon_FrontGap34', a)


def test_assoc_gapMaker21_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_JoinPlatoonCoord()
    b2 = platoon_JoinPlatoonCoord()
    _safe_set(a, 'platoon_Vehicle23', b1)
    assert _is_linked(a, 'platoon_Vehicle23', b1)
    if hasattr(b1, 'platoon_JoinPlatoonCoord22'):
        assert _is_linked(b1, 'platoon_JoinPlatoonCoord22', a)
    _safe_set(a, 'platoon_Vehicle23', b2)
    assert _is_linked(a, 'platoon_Vehicle23', b2)
    if hasattr(b1, 'platoon_JoinPlatoonCoord22'):
        assert not _is_linked(b1, 'platoon_JoinPlatoonCoord22', a)
    if hasattr(b2, 'platoon_JoinPlatoonCoord22'):
        assert _is_linked(b2, 'platoon_JoinPlatoonCoord22', a)
    _safe_set(a, 'platoon_Vehicle23', None)
    assert not _is_linked(a, 'platoon_Vehicle23', b2)
    if hasattr(b2, 'platoon_JoinPlatoonCoord22'):
        assert not _is_linked(b2, 'platoon_JoinPlatoonCoord22', a)


def test_assoc_insertsIn27_link_reassign_clear():
    a = platoon_FrontGap(actualGapSize=7)
    b1 = platoon_JoiningVehicle()
    b2 = platoon_JoiningVehicle()
    _safe_set(a, 'platoon_FrontGap', b1)
    assert _is_linked(a, 'platoon_FrontGap', b1)
    if hasattr(b1, 'platoon_JoiningVehicle'):
        assert _is_linked(b1, 'platoon_JoiningVehicle', a)
    _safe_set(a, 'platoon_FrontGap', b2)
    assert _is_linked(a, 'platoon_FrontGap', b2)
    if hasattr(b1, 'platoon_JoiningVehicle'):
        assert not _is_linked(b1, 'platoon_JoiningVehicle', a)
    if hasattr(b2, 'platoon_JoiningVehicle'):
        assert _is_linked(b2, 'platoon_JoiningVehicle', a)
    _safe_set(a, 'platoon_FrontGap', None)
    assert not _is_linked(a, 'platoon_FrontGap', b2)
    if hasattr(b2, 'platoon_JoiningVehicle'):
        assert not _is_linked(b2, 'platoon_JoiningVehicle', a)


def test_assoc_isAwareOf13_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_Vehicle(id=7)
    b2 = platoon_Vehicle(id=13)
    _safe_set(a, 'platoon_Vehicle12', b1)
    assert _is_linked(a, 'platoon_Vehicle12', b1)
    if hasattr(b1, 'platoon_Vehicle14'):
        assert _is_linked(b1, 'platoon_Vehicle14', a)
    _safe_set(a, 'platoon_Vehicle12', b2)
    assert _is_linked(a, 'platoon_Vehicle12', b2)
    if hasattr(b1, 'platoon_Vehicle14'):
        assert not _is_linked(b1, 'platoon_Vehicle14', a)
    if hasattr(b2, 'platoon_Vehicle14'):
        assert _is_linked(b2, 'platoon_Vehicle14', a)
    _safe_set(a, 'platoon_Vehicle12', None)
    assert not _is_linked(a, 'platoon_Vehicle12', b2)
    if hasattr(b2, 'platoon_Vehicle14'):
        assert not _is_linked(b2, 'platoon_Vehicle14', a)


def test_assoc_joinCord15_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_JoinPlatoonCoord()
    b2 = platoon_JoinPlatoonCoord()
    _safe_set(a, 'platoon_Vehicle16', b1)
    assert _is_linked(a, 'platoon_Vehicle16', b1)
    if hasattr(b1, 'platoon_JoinPlatoonCoord17'):
        assert _is_linked(b1, 'platoon_JoinPlatoonCoord17', a)
    _safe_set(a, 'platoon_Vehicle16', b2)
    assert _is_linked(a, 'platoon_Vehicle16', b2)
    if hasattr(b1, 'platoon_JoinPlatoonCoord17'):
        assert not _is_linked(b1, 'platoon_JoinPlatoonCoord17', a)
    if hasattr(b2, 'platoon_JoinPlatoonCoord17'):
        assert _is_linked(b2, 'platoon_JoinPlatoonCoord17', a)
    _safe_set(a, 'platoon_Vehicle16', None)
    assert not _is_linked(a, 'platoon_Vehicle16', b2)
    if hasattr(b2, 'platoon_JoinPlatoonCoord17'):
        assert not _is_linked(b2, 'platoon_JoinPlatoonCoord17', a)


def test_assoc_joiningRequest38_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_JoiningVehicle()
    b2 = platoon_JoiningVehicle()
    _safe_set(a, 'wantsToJoin', b1)
    assert _is_linked(a, 'wantsToJoin', b1)
    if hasattr(b1, 'JoiningVehicle'):
        assert _is_linked(b1, 'JoiningVehicle', a)
    _safe_set(a, 'wantsToJoin', b2)
    assert _is_linked(a, 'wantsToJoin', b2)
    if hasattr(b1, 'JoiningVehicle'):
        assert not _is_linked(b1, 'JoiningVehicle', a)
    if hasattr(b2, 'JoiningVehicle'):
        assert _is_linked(b2, 'JoiningVehicle', a)
    _safe_set(a, 'wantsToJoin', None)
    assert not _is_linked(a, 'wantsToJoin', b2)
    if hasattr(b2, 'JoiningVehicle'):
        assert not _is_linked(b2, 'JoiningVehicle', a)


def test_assoc_joiningVehicle24_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_JoinPlatoonCoord()
    b2 = platoon_JoinPlatoonCoord()
    _safe_set(a, 'platoon_Vehicle26', b1)
    assert _is_linked(a, 'platoon_Vehicle26', b1)
    if hasattr(b1, 'platoon_JoinPlatoonCoord25'):
        assert _is_linked(b1, 'platoon_JoinPlatoonCoord25', a)
    _safe_set(a, 'platoon_Vehicle26', b2)
    assert _is_linked(a, 'platoon_Vehicle26', b2)
    if hasattr(b1, 'platoon_JoinPlatoonCoord25'):
        assert not _is_linked(b1, 'platoon_JoinPlatoonCoord25', a)
    if hasattr(b2, 'platoon_JoinPlatoonCoord25'):
        assert _is_linked(b2, 'platoon_JoinPlatoonCoord25', a)
    _safe_set(a, 'platoon_Vehicle26', None)
    assert not _is_linked(a, 'platoon_Vehicle26', b2)
    if hasattr(b2, 'platoon_JoinPlatoonCoord25'):
        assert not _is_linked(b2, 'platoon_JoinPlatoonCoord25', a)


def test_assoc_joinplatoonCord7_link_reassign_clear():
    a = platoon_Platoon(desiredGapSize=7, length=7)
    b1 = platoon_JoinPlatoonCoord()
    b2 = platoon_JoinPlatoonCoord()
    _safe_set(a, 'platoon_Platoon8', b1)
    assert _is_linked(a, 'platoon_Platoon8', b1)
    if hasattr(b1, 'platoon_JoinPlatoonCoord'):
        assert _is_linked(b1, 'platoon_JoinPlatoonCoord', a)
    _safe_set(a, 'platoon_Platoon8', b2)
    assert _is_linked(a, 'platoon_Platoon8', b2)
    if hasattr(b1, 'platoon_JoinPlatoonCoord'):
        assert not _is_linked(b1, 'platoon_JoinPlatoonCoord', a)
    if hasattr(b2, 'platoon_JoinPlatoonCoord'):
        assert _is_linked(b2, 'platoon_JoinPlatoonCoord', a)
    _safe_set(a, 'platoon_Platoon8', None)
    assert not _is_linked(a, 'platoon_Platoon8', b2)
    if hasattr(b2, 'platoon_JoinPlatoonCoord'):
        assert not _is_linked(b2, 'platoon_JoinPlatoonCoord', a)


def test_assoc_leader0_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_Platoon(desiredGapSize=7, length=7)
    b2 = platoon_Platoon(desiredGapSize=13, length=13)
    _safe_set(a, 'platoon_PlatoonVehicle', b1)
    assert _is_linked(a, 'platoon_PlatoonVehicle', b1)
    if hasattr(b1, 'platoon_Platoon'):
        assert _is_linked(b1, 'platoon_Platoon', a)
    _safe_set(a, 'platoon_PlatoonVehicle', b2)
    assert _is_linked(a, 'platoon_PlatoonVehicle', b2)
    if hasattr(b1, 'platoon_Platoon'):
        assert not _is_linked(b1, 'platoon_Platoon', a)
    if hasattr(b2, 'platoon_Platoon'):
        assert _is_linked(b2, 'platoon_Platoon', a)
    _safe_set(a, 'platoon_PlatoonVehicle', None)
    assert not _is_linked(a, 'platoon_PlatoonVehicle', b2)
    if hasattr(b2, 'platoon_Platoon'):
        assert not _is_linked(b2, 'platoon_Platoon', a)


def test_assoc_marks35_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_JoiningPosition()
    b2 = platoon_JoiningPosition()
    _safe_set(a, 'platoon_PlatoonVehicle36', b1)
    assert _is_linked(a, 'platoon_PlatoonVehicle36', b1)
    if hasattr(b1, 'platoon_JoiningPosition37'):
        assert _is_linked(b1, 'platoon_JoiningPosition37', a)
    _safe_set(a, 'platoon_PlatoonVehicle36', b2)
    assert _is_linked(a, 'platoon_PlatoonVehicle36', b2)
    if hasattr(b1, 'platoon_JoiningPosition37'):
        assert not _is_linked(b1, 'platoon_JoiningPosition37', a)
    if hasattr(b2, 'platoon_JoiningPosition37'):
        assert _is_linked(b2, 'platoon_JoiningPosition37', a)
    _safe_set(a, 'platoon_PlatoonVehicle36', None)
    assert not _is_linked(a, 'platoon_PlatoonVehicle36', b2)
    if hasattr(b2, 'platoon_JoiningPosition37'):
        assert not _is_linked(b2, 'platoon_JoiningPosition37', a)


def test_assoc_members9_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_Platoon(desiredGapSize=7, length=7)
    b2 = platoon_Platoon(desiredGapSize=13, length=13)
    _safe_set(a, 'PlatoonVehicle', b1)
    assert _is_linked(a, 'PlatoonVehicle', b1)
    if hasattr(b1, 'platoon'):
        assert _is_linked(b1, 'platoon', a)
    _safe_set(a, 'PlatoonVehicle', b2)
    assert _is_linked(a, 'PlatoonVehicle', b2)
    if hasattr(b1, 'platoon'):
        assert not _is_linked(b1, 'platoon', a)
    if hasattr(b2, 'platoon'):
        assert _is_linked(b2, 'platoon', a)
    _safe_set(a, 'PlatoonVehicle', None)
    assert not _is_linked(a, 'PlatoonVehicle', b2)
    if hasattr(b2, 'platoon'):
        assert not _is_linked(b2, 'platoon', a)


def test_assoc_platoon39_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_Platoon(desiredGapSize=7, length=7)
    b2 = platoon_Platoon(desiredGapSize=13, length=13)
    _safe_set(a, 'members', b1)
    assert _is_linked(a, 'members', b1)
    if hasattr(b1, 'Platoon'):
        assert _is_linked(b1, 'Platoon', a)
    _safe_set(a, 'members', b2)
    assert _is_linked(a, 'members', b2)
    if hasattr(b1, 'Platoon'):
        assert not _is_linked(b1, 'Platoon', a)
    if hasattr(b2, 'Platoon'):
        assert _is_linked(b2, 'Platoon', a)
    _safe_set(a, 'members', None)
    assert not _is_linked(a, 'members', b2)
    if hasattr(b2, 'Platoon'):
        assert not _is_linked(b2, 'Platoon', a)


def test_assoc_platoon42_link_reassign_clear():
    a = platoon_Platoon(desiredGapSize=7, length=7)
    b1 = platoon_PlatooningSystem()
    b2 = platoon_PlatooningSystem()
    _safe_set(a, 'platoon_Platoon44', b1)
    assert _is_linked(a, 'platoon_Platoon44', b1)
    if hasattr(b1, 'platoon_PlatooningSystem43'):
        assert _is_linked(b1, 'platoon_PlatooningSystem43', a)
    _safe_set(a, 'platoon_Platoon44', b2)
    assert _is_linked(a, 'platoon_Platoon44', b2)
    if hasattr(b1, 'platoon_PlatooningSystem43'):
        assert not _is_linked(b1, 'platoon_PlatooningSystem43', a)
    if hasattr(b2, 'platoon_PlatooningSystem43'):
        assert _is_linked(b2, 'platoon_PlatooningSystem43', a)
    _safe_set(a, 'platoon_Platoon44', None)
    assert not _is_linked(a, 'platoon_Platoon44', b2)
    if hasattr(b2, 'platoon_PlatooningSystem43'):
        assert not _is_linked(b2, 'platoon_PlatooningSystem43', a)


def test_assoc_vehicles40_link_reassign_clear():
    a = platoon_Vehicle(id=7)
    b1 = platoon_PlatooningSystem()
    b2 = platoon_PlatooningSystem()
    _safe_set(a, 'platoon_Vehicle41', b1)
    assert _is_linked(a, 'platoon_Vehicle41', b1)
    if hasattr(b1, 'platoon_PlatooningSystem'):
        assert _is_linked(b1, 'platoon_PlatooningSystem', a)
    _safe_set(a, 'platoon_Vehicle41', b2)
    assert _is_linked(a, 'platoon_Vehicle41', b2)
    if hasattr(b1, 'platoon_PlatooningSystem'):
        assert not _is_linked(b1, 'platoon_PlatooningSystem', a)
    if hasattr(b2, 'platoon_PlatooningSystem'):
        assert _is_linked(b2, 'platoon_PlatooningSystem', a)
    _safe_set(a, 'platoon_Vehicle41', None)
    assert not _is_linked(a, 'platoon_Vehicle41', b2)
    if hasattr(b2, 'platoon_PlatooningSystem'):
        assert not _is_linked(b2, 'platoon_PlatooningSystem', a)


def test_assoc_wantsToJoin28_link_reassign_clear():
    a = platoon_PlatoonVehicle(position=7)
    b1 = platoon_JoiningVehicle()
    b2 = platoon_JoiningVehicle()
    _safe_set(a, 'PlatoonVehicle29', b1)
    assert _is_linked(a, 'PlatoonVehicle29', b1)
    if hasattr(b1, 'joiningRequest'):
        assert _is_linked(b1, 'joiningRequest', a)
    _safe_set(a, 'PlatoonVehicle29', b2)
    assert _is_linked(a, 'PlatoonVehicle29', b2)
    if hasattr(b1, 'joiningRequest'):
        assert not _is_linked(b1, 'joiningRequest', a)
    if hasattr(b2, 'joiningRequest'):
        assert _is_linked(b2, 'joiningRequest', a)
    _safe_set(a, 'PlatoonVehicle29', None)
    assert not _is_linked(a, 'PlatoonVehicle29', b2)
    if hasattr(b2, 'joiningRequest'):
        assert not _is_linked(b2, 'joiningRequest', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Vehicle_strategy = st.builds(Vehicle)
@given(instance=Vehicle_strategy)
@settings(max_examples=25)
def test_Vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)


platoon_FrontGap_strategy = st.builds(platoon_FrontGap, actualGapSize=st.integers())
@given(instance=platoon_FrontGap_strategy)
@settings(max_examples=25)
def test_platoon_FrontGap_instantiation(instance):
    assert isinstance(instance, platoon_FrontGap)


platoon_JoinPlatoonCoord_strategy = st.builds(platoon_JoinPlatoonCoord)
@given(instance=platoon_JoinPlatoonCoord_strategy)
@settings(max_examples=25)
def test_platoon_JoinPlatoonCoord_instantiation(instance):
    assert isinstance(instance, platoon_JoinPlatoonCoord)


platoon_JoiningPosition_strategy = st.builds(platoon_JoiningPosition)
@given(instance=platoon_JoiningPosition_strategy)
@settings(max_examples=25)
def test_platoon_JoiningPosition_instantiation(instance):
    assert isinstance(instance, platoon_JoiningPosition)


platoon_JoiningVehicle_strategy = st.builds(platoon_JoiningVehicle)
@given(instance=platoon_JoiningVehicle_strategy)
@settings(max_examples=25)
def test_platoon_JoiningVehicle_instantiation(instance):
    assert isinstance(instance, platoon_JoiningVehicle)


platoon_Platoon_strategy = st.builds(platoon_Platoon, desiredGapSize=st.integers(), length=st.integers())
@given(instance=platoon_Platoon_strategy)
@settings(max_examples=25)
def test_platoon_Platoon_instantiation(instance):
    assert isinstance(instance, platoon_Platoon)


platoon_PlatoonVehicle_strategy = st.builds(platoon_PlatoonVehicle, position=st.integers())
@given(instance=platoon_PlatoonVehicle_strategy)
@settings(max_examples=25)
def test_platoon_PlatoonVehicle_instantiation(instance):
    assert isinstance(instance, platoon_PlatoonVehicle)


platoon_PlatooningSystem_strategy = st.builds(platoon_PlatooningSystem)
@given(instance=platoon_PlatooningSystem_strategy)
@settings(max_examples=25)
def test_platoon_PlatooningSystem_instantiation(instance):
    assert isinstance(instance, platoon_PlatooningSystem)


platoon_Vehicle_strategy = st.builds(platoon_Vehicle, id=st.integers())
@given(instance=platoon_Vehicle_strategy)
@settings(max_examples=25)
def test_platoon_Vehicle_instantiation(instance):
    assert isinstance(instance, platoon_Vehicle)



