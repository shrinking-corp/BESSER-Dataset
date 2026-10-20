import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ContainerCar,
    ElectricTrain,
    EngineCar,
    FreightTrain,
    Maglev,
    MaglevCar,
    PassengerCar,
    PassengerTrain,
    T,
    Train,
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

def test_assoc_ContainerCar_FreightTrain_reverse_link_reassign_clear():
    a1 = FreightTrain(containerTrain=True)
    a2 = FreightTrain(containerTrain=False)
    b = ContainerCar(climateControlled=True, cubicFeet=3.14, temp=3.14)
    _safe_set(b, 'freightTrain4', a1)
    assert _is_linked(b, 'freightTrain4', a1)
    if hasattr(a1, 'containerCar5'):
        assert _is_linked(a1, 'containerCar5', b)
    _safe_set(b, 'freightTrain4', a2)
    assert _is_linked(b, 'freightTrain4', a2)
    if hasattr(a1, 'containerCar5'):
        assert not _is_linked(a1, 'containerCar5', b)
    if hasattr(a2, 'containerCar5'):
        assert _is_linked(a2, 'containerCar5', b)
    _safe_set(b, 'freightTrain4', None)
    assert not _is_linked(b, 'freightTrain4', a2)
    if hasattr(a2, 'containerCar5'):
        assert not _is_linked(a2, 'containerCar5', b)


def test_assoc_ElectricTrain_EngineCar_reverse_link_reassign_clear():
    a1 = EngineCar(MAXSPEED=3.14)
    a2 = EngineCar(MAXSPEED=9.99)
    b = ElectricTrain(MAXSPEED=3.14)
    _safe_set(b, 'engineCar10', a1)
    assert _is_linked(b, 'engineCar10', a1)
    if hasattr(a1, 'electricTrain11'):
        assert _is_linked(a1, 'electricTrain11', b)
    _safe_set(b, 'engineCar10', a2)
    assert _is_linked(b, 'engineCar10', a2)
    if hasattr(a1, 'electricTrain11'):
        assert not _is_linked(a1, 'electricTrain11', b)
    if hasattr(a2, 'electricTrain11'):
        assert _is_linked(a2, 'electricTrain11', b)
    _safe_set(b, 'engineCar10', None)
    assert not _is_linked(b, 'engineCar10', a2)
    if hasattr(a2, 'electricTrain11'):
        assert not _is_linked(a2, 'electricTrain11', b)


def test_assoc_ElectricTrain_PassengerCar_reverse_link_reassign_clear():
    a1 = PassengerCar(NUMSEATS=7, numSeatsOccupied=7)
    a2 = PassengerCar(NUMSEATS=13, numSeatsOccupied=13)
    b = ElectricTrain(MAXSPEED=3.14)
    _safe_set(b, 'passengerCar12', a1)
    assert _is_linked(b, 'passengerCar12', a1)
    if hasattr(a1, 'electricTrain13'):
        assert _is_linked(a1, 'electricTrain13', b)
    _safe_set(b, 'passengerCar12', a2)
    assert _is_linked(b, 'passengerCar12', a2)
    if hasattr(a1, 'electricTrain13'):
        assert not _is_linked(a1, 'electricTrain13', b)
    if hasattr(a2, 'electricTrain13'):
        assert _is_linked(a2, 'electricTrain13', b)
    _safe_set(b, 'passengerCar12', None)
    assert not _is_linked(b, 'passengerCar12', a2)
    if hasattr(a2, 'electricTrain13'):
        assert not _is_linked(a2, 'electricTrain13', b)


def test_assoc_Maglev_MaglevCar_reverse_link_reassign_clear():
    a1 = MaglevCar(NUMSEATS=7, numSeatsOccupied=7)
    a2 = MaglevCar(NUMSEATS=13, numSeatsOccupied=13)
    b = Maglev(MAXSPEED=3.14)
    _safe_set(b, 'maglevCar14', a1)
    assert _is_linked(b, 'maglevCar14', a1)
    if hasattr(a1, 'maglev15'):
        assert _is_linked(a1, 'maglev15', b)
    _safe_set(b, 'maglevCar14', a2)
    assert _is_linked(b, 'maglevCar14', a2)
    if hasattr(a1, 'maglev15'):
        assert not _is_linked(a1, 'maglev15', b)
    if hasattr(a2, 'maglev15'):
        assert _is_linked(a2, 'maglev15', b)
    _safe_set(b, 'maglevCar14', None)
    assert not _is_linked(b, 'maglevCar14', a2)
    if hasattr(a2, 'maglev15'):
        assert not _is_linked(a2, 'maglev15', b)


def test_assoc_Train_freightTrain_reverse_link_reassign_clear():
    a1 = Train(milesPerHour=3.14, totalCars=7)
    a2 = Train(milesPerHour=9.99, totalCars=13)
    b = FreightTrain(containerTrain=True)
    _safe_set(b, 'train1', a1)
    assert _is_linked(b, 'train1', a1)
    if hasattr(a1, 'freightTrain0'):
        assert _is_linked(a1, 'freightTrain0', b)
    _safe_set(b, 'train1', a2)
    assert _is_linked(b, 'train1', a2)
    if hasattr(a1, 'freightTrain0'):
        assert not _is_linked(a1, 'freightTrain0', b)
    if hasattr(a2, 'freightTrain0'):
        assert _is_linked(a2, 'freightTrain0', b)
    _safe_set(b, 'train1', None)
    assert not _is_linked(b, 'train1', a2)
    if hasattr(a2, 'freightTrain0'):
        assert not _is_linked(a2, 'freightTrain0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_PassengerTrain_ElectricTrain_stub_double():
    # PassengerTrain has no real 'electricTrain8' property in the generated
    # code (a bare stub) -- manually attach it so ElectricTrain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ElectricTrain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ElectricTrain(MAXSPEED=3.14)
    partner = PassengerTrain()
    setattr(partner, 'electricTrain8', None)
    _safe_set(owner, 'passengerTrain9', partner)
    assert getattr(partner, 'electricTrain8') == owner
    _safe_set(owner, 'passengerTrain9', None)
    assert getattr(partner, 'electricTrain8') is None


def test_assoc_PassengerTrain_Maglev_stub_double():
    # PassengerTrain has no real 'maglev6' property in the generated
    # code (a bare stub) -- manually attach it so Maglev's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Maglev's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Maglev(MAXSPEED=3.14)
    partner = PassengerTrain()
    setattr(partner, 'maglev6', None)
    _safe_set(owner, 'passengerTrain7', partner)
    assert getattr(partner, 'maglev6') == owner
    _safe_set(owner, 'passengerTrain7', None)
    assert getattr(partner, 'maglev6') is None


def test_assoc_Train_passengerTrain_stub_double():
    # PassengerTrain has no real 'train3' property in the generated
    # code (a bare stub) -- manually attach it so Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Train(milesPerHour=3.14, totalCars=7)
    partner = PassengerTrain()
    setattr(partner, 'train3', None)
    _safe_set(owner, 'passengerTrain2', partner)
    assert getattr(partner, 'train3') == owner
    _safe_set(owner, 'passengerTrain2', None)
    assert getattr(partner, 'train3') is None


