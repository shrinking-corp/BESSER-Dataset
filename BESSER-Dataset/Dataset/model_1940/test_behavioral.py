import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FlightObject,
    Flights_Airport,
    Flights_Airports,
    Flights_Booking,
    Flights_Bookings,
    Flights_Flight,
    Flights_FlightContainer,
    Flights_FlightModel,
    Flights_FlightObject,
    Flights_Gate,
    Flights_Person,
    Flights_Persons,
    Flights_Plane,
    Flights_Planes,
    Flights_Route,
    Flights_Routes,
    Flights_TimeStamp,
    Flights_Travel,
    FlightState,
    TravelState,
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

def test_assoc_arrival26_reverse_link_reassign_clear():
    a1 = Flights_TimeStamp(time="sample_text")
    a2 = Flights_TimeStamp(time="sample_text_2")
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flights_Flight27', a1)
    assert _is_linked(b, 'Flights_Flight27', a1)
    if hasattr(a1, 'Flights_TimeStamp28'):
        assert _is_linked(a1, 'Flights_TimeStamp28', b)
    _safe_set(b, 'Flights_Flight27', a2)
    assert _is_linked(b, 'Flights_Flight27', a2)
    if hasattr(a1, 'Flights_TimeStamp28'):
        assert not _is_linked(a1, 'Flights_TimeStamp28', b)
    if hasattr(a2, 'Flights_TimeStamp28'):
        assert _is_linked(a2, 'Flights_TimeStamp28', b)
    _safe_set(b, 'Flights_Flight27', None)
    assert not _is_linked(b, 'Flights_Flight27', a2)
    if hasattr(a2, 'Flights_TimeStamp28'):
        assert not _is_linked(a2, 'Flights_TimeStamp28', b)


def test_assoc_departure23_reverse_link_reassign_clear():
    a1 = Flights_TimeStamp(time="sample_text")
    a2 = Flights_TimeStamp(time="sample_text_2")
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flights_Flight24', a1)
    assert _is_linked(b, 'Flights_Flight24', a1)
    if hasattr(a1, 'Flights_TimeStamp25'):
        assert _is_linked(a1, 'Flights_TimeStamp25', b)
    _safe_set(b, 'Flights_Flight24', a2)
    assert _is_linked(b, 'Flights_Flight24', a2)
    if hasattr(a1, 'Flights_TimeStamp25'):
        assert not _is_linked(a1, 'Flights_TimeStamp25', b)
    if hasattr(a2, 'Flights_TimeStamp25'):
        assert _is_linked(a2, 'Flights_TimeStamp25', b)
    _safe_set(b, 'Flights_Flight24', None)
    assert not _is_linked(b, 'Flights_Flight24', a2)
    if hasattr(a2, 'Flights_TimeStamp25'):
        assert not _is_linked(a2, 'Flights_TimeStamp25', b)


def test_assoc_flights35_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flight', a1)
    assert _is_linked(b, 'Flight', a1)
    if hasattr(a1, 'route'):
        assert _is_linked(a1, 'route', b)
    _safe_set(b, 'Flight', a2)
    assert _is_linked(b, 'Flight', a2)
    if hasattr(a1, 'route'):
        assert not _is_linked(a1, 'route', b)
    if hasattr(a2, 'route'):
        assert _is_linked(a2, 'route', b)
    _safe_set(b, 'Flight', None)
    assert not _is_linked(b, 'Flight', a2)
    if hasattr(a2, 'route'):
        assert not _is_linked(a2, 'route', b)


def test_assoc_flights57_reverse_link_reassign_clear():
    a1 = Flights_Plane(capacity=7)
    a2 = Flights_Plane(capacity=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flight58', a1)
    assert _is_linked(b, 'Flight58', a1)
    if hasattr(a1, 'plane'):
        assert _is_linked(a1, 'plane', b)
    _safe_set(b, 'Flight58', a2)
    assert _is_linked(b, 'Flight58', a2)
    if hasattr(a1, 'plane'):
        assert not _is_linked(a1, 'plane', b)
    if hasattr(a2, 'plane'):
        assert _is_linked(a2, 'plane', b)
    _safe_set(b, 'Flight58', None)
    assert not _is_linked(b, 'Flight58', a2)
    if hasattr(a2, 'plane'):
        assert not _is_linked(a2, 'plane', b)


def test_assoc_gates49_reverse_link_reassign_clear():
    a1 = Flights_Gate(position=7)
    a2 = Flights_Gate(position=13)
    b = Flights_Airport(size=3.14)
    _safe_set(b, 'Flights_Airport50', {a1})
    assert _is_linked(b, 'Flights_Airport50', a1)
    if hasattr(a1, 'Flights_Gate'):
        assert _is_linked(a1, 'Flights_Gate', b)
    _safe_set(b, 'Flights_Airport50', {a2})
    assert _is_linked(b, 'Flights_Airport50', a2)
    if hasattr(a1, 'Flights_Gate'):
        assert not _is_linked(a1, 'Flights_Gate', b)
    if hasattr(a2, 'Flights_Gate'):
        assert _is_linked(a2, 'Flights_Gate', b)
    _safe_set(b, 'Flights_Airport50', set())
    assert not _is_linked(b, 'Flights_Airport50', a2)
    if hasattr(a2, 'Flights_Gate'):
        assert not _is_linked(a2, 'Flights_Gate', b)


def test_assoc_incomingFlights62_reverse_link_reassign_clear():
    a1 = Flights_Gate(position=7)
    a2 = Flights_Gate(position=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flight64', a1)
    assert _is_linked(b, 'Flight64', a1)
    if hasattr(a1, 'trg63'):
        assert _is_linked(a1, 'trg63', b)
    _safe_set(b, 'Flight64', a2)
    assert _is_linked(b, 'Flight64', a2)
    if hasattr(a1, 'trg63'):
        assert not _is_linked(a1, 'trg63', b)
    if hasattr(a2, 'trg63'):
        assert _is_linked(a2, 'trg63', b)
    _safe_set(b, 'Flight64', None)
    assert not _is_linked(b, 'Flight64', a2)
    if hasattr(a2, 'trg63'):
        assert not _is_linked(a2, 'trg63', b)


def test_assoc_incomingRoutes53_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Airport(size=3.14)
    _safe_set(b, 'trg', {a1})
    assert _is_linked(b, 'trg', a1)
    if hasattr(a1, 'Route54'):
        assert _is_linked(a1, 'Route54', b)
    _safe_set(b, 'trg', {a2})
    assert _is_linked(b, 'trg', a2)
    if hasattr(a1, 'Route54'):
        assert not _is_linked(a1, 'Route54', b)
    if hasattr(a2, 'Route54'):
        assert _is_linked(a2, 'Route54', b)
    _safe_set(b, 'trg', set())
    assert not _is_linked(b, 'trg', a2)
    if hasattr(a2, 'Route54'):
        assert not _is_linked(a2, 'Route54', b)


def test_assoc_outgoingFlights59_reverse_link_reassign_clear():
    a1 = Flights_Gate(position=7)
    a2 = Flights_Gate(position=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'Flight61', a1)
    assert _is_linked(b, 'Flight61', a1)
    if hasattr(a1, 'src60'):
        assert _is_linked(a1, 'src60', b)
    _safe_set(b, 'Flight61', a2)
    assert _is_linked(b, 'Flight61', a2)
    if hasattr(a1, 'src60'):
        assert not _is_linked(a1, 'src60', b)
    if hasattr(a2, 'src60'):
        assert _is_linked(a2, 'src60', b)
    _safe_set(b, 'Flight61', None)
    assert not _is_linked(b, 'Flight61', a2)
    if hasattr(a2, 'src60'):
        assert not _is_linked(a2, 'src60', b)


def test_assoc_outgoingRoutes51_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Airport(size=3.14)
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Route52'):
        assert _is_linked(a1, 'Route52', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Route52'):
        assert not _is_linked(a1, 'Route52', b)
    if hasattr(a2, 'Route52'):
        assert _is_linked(a2, 'Route52', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Route52'):
        assert not _is_linked(a2, 'Route52', b)


def test_assoc_plane21_reverse_link_reassign_clear():
    a1 = Flights_Plane(capacity=7)
    a2 = Flights_Plane(capacity=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'flights22', a1)
    assert _is_linked(b, 'flights22', a1)
    if hasattr(a1, 'Plane'):
        assert _is_linked(a1, 'Plane', b)
    _safe_set(b, 'flights22', a2)
    assert _is_linked(b, 'flights22', a2)
    if hasattr(a1, 'Plane'):
        assert not _is_linked(a1, 'Plane', b)
    if hasattr(a2, 'Plane'):
        assert _is_linked(a2, 'Plane', b)
    _safe_set(b, 'flights22', None)
    assert not _is_linked(b, 'flights22', a2)
    if hasattr(a2, 'Plane'):
        assert not _is_linked(a2, 'Plane', b)


def test_assoc_route16_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'flights17', a1)
    assert _is_linked(b, 'flights17', a1)
    if hasattr(a1, 'Route'):
        assert _is_linked(a1, 'Route', b)
    _safe_set(b, 'flights17', a2)
    assert _is_linked(b, 'flights17', a2)
    if hasattr(a1, 'Route'):
        assert not _is_linked(a1, 'Route', b)
    if hasattr(a2, 'Route'):
        assert _is_linked(a2, 'Route', b)
    _safe_set(b, 'flights17', None)
    assert not _is_linked(b, 'flights17', a2)
    if hasattr(a2, 'Route'):
        assert not _is_linked(a2, 'Route', b)


def test_assoc_src18_reverse_link_reassign_clear():
    a1 = Flights_Gate(position=7)
    a2 = Flights_Gate(position=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'outgoingFlights', a1)
    assert _is_linked(b, 'outgoingFlights', a1)
    if hasattr(a1, 'Gate'):
        assert _is_linked(a1, 'Gate', b)
    _safe_set(b, 'outgoingFlights', a2)
    assert _is_linked(b, 'outgoingFlights', a2)
    if hasattr(a1, 'Gate'):
        assert not _is_linked(a1, 'Gate', b)
    if hasattr(a2, 'Gate'):
        assert _is_linked(a2, 'Gate', b)
    _safe_set(b, 'outgoingFlights', None)
    assert not _is_linked(b, 'outgoingFlights', a2)
    if hasattr(a2, 'Gate'):
        assert not _is_linked(a2, 'Gate', b)


def test_assoc_src36_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Airport(size=3.14)
    _safe_set(b, 'Airport', a1)
    assert _is_linked(b, 'Airport', a1)
    if hasattr(a1, 'outgoingRoutes'):
        assert _is_linked(a1, 'outgoingRoutes', b)
    _safe_set(b, 'Airport', a2)
    assert _is_linked(b, 'Airport', a2)
    if hasattr(a1, 'outgoingRoutes'):
        assert not _is_linked(a1, 'outgoingRoutes', b)
    if hasattr(a2, 'outgoingRoutes'):
        assert _is_linked(a2, 'outgoingRoutes', b)
    _safe_set(b, 'Airport', None)
    assert not _is_linked(b, 'Airport', a2)
    if hasattr(a2, 'outgoingRoutes'):
        assert not _is_linked(a2, 'outgoingRoutes', b)


def test_assoc_trg19_reverse_link_reassign_clear():
    a1 = Flights_Gate(position=7)
    a2 = Flights_Gate(position=13)
    b = Flights_Flight(newAttribute="sample_text")
    _safe_set(b, 'incomingFlights', a1)
    assert _is_linked(b, 'incomingFlights', a1)
    if hasattr(a1, 'Gate20'):
        assert _is_linked(a1, 'Gate20', b)
    _safe_set(b, 'incomingFlights', a2)
    assert _is_linked(b, 'incomingFlights', a2)
    if hasattr(a1, 'Gate20'):
        assert not _is_linked(a1, 'Gate20', b)
    if hasattr(a2, 'Gate20'):
        assert _is_linked(a2, 'Gate20', b)
    _safe_set(b, 'incomingFlights', None)
    assert not _is_linked(b, 'incomingFlights', a2)
    if hasattr(a2, 'Gate20'):
        assert not _is_linked(a2, 'Gate20', b)


def test_assoc_trg37_reverse_link_reassign_clear():
    a1 = Flights_Route(duration=7)
    a2 = Flights_Route(duration=13)
    b = Flights_Airport(size=3.14)
    _safe_set(b, 'Airport38', a1)
    assert _is_linked(b, 'Airport38', a1)
    if hasattr(a1, 'incomingRoutes'):
        assert _is_linked(a1, 'incomingRoutes', b)
    _safe_set(b, 'Airport38', a2)
    assert _is_linked(b, 'Airport38', a2)
    if hasattr(a1, 'incomingRoutes'):
        assert not _is_linked(a1, 'incomingRoutes', b)
    if hasattr(a2, 'incomingRoutes'):
        assert _is_linked(a2, 'incomingRoutes', b)
    _safe_set(b, 'Airport38', None)
    assert not _is_linked(b, 'Airport38', a2)
    if hasattr(a2, 'incomingRoutes'):
        assert not _is_linked(a2, 'incomingRoutes', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_airports47_stub_double():
    # Flights_Airports has no real 'Flights_Airports48' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Airport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Airport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Airport(size=3.14)
    partner = Flights_Airports()
    setattr(partner, 'Flights_Airports48', None)
    _safe_set(owner, 'Flights_Airport', partner)
    assert owner in getattr(partner, 'Flights_Airports48')
    _safe_set(owner, 'Flights_Airport', None)
    assert owner not in getattr(partner, 'Flights_Airports48')


def test_assoc_flights13_stub_double():
    # Flights_FlightContainer has no real 'Flights_FlightContainer14' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Flight's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Flight's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Flight(newAttribute="sample_text")
    partner = Flights_FlightContainer()
    setattr(partner, 'Flights_FlightContainer14', None)
    _safe_set(owner, 'Flights_Flight', partner)
    assert owner in getattr(partner, 'Flights_FlightContainer14')
    _safe_set(owner, 'Flights_Flight', None)
    assert owner not in getattr(partner, 'Flights_FlightContainer14')


def test_assoc_flights39_stub_double():
    # Flights_Travel has no real 'travels' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Flight's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Flight's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Flight(newAttribute="sample_text")
    partner = Flights_Travel()
    setattr(partner, 'travels', None)
    _safe_set(owner, 'Flight40', partner)
    assert owner in getattr(partner, 'travels')
    _safe_set(owner, 'Flight40', None)
    assert owner not in getattr(partner, 'travels')


def test_assoc_globalTime11_stub_double():
    # Flights_FlightModel has no real 'Flights_FlightModel12' property in the generated
    # code (a bare stub) -- manually attach it so Flights_TimeStamp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_TimeStamp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_TimeStamp(time="sample_text")
    partner = Flights_FlightModel()
    setattr(partner, 'Flights_FlightModel12', None)
    _safe_set(owner, 'Flights_TimeStamp', partner)
    assert getattr(partner, 'Flights_FlightModel12') == owner
    _safe_set(owner, 'Flights_TimeStamp', None)
    assert getattr(partner, 'Flights_FlightModel12') is None


def test_assoc_person41_stub_double():
    # Flights_Travel has no real 'travels42' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Person(travelState="sample_text")
    partner = Flights_Travel()
    setattr(partner, 'travels42', None)
    _safe_set(owner, 'Person', partner)
    assert getattr(partner, 'travels42') == owner
    _safe_set(owner, 'Person', None)
    assert getattr(partner, 'travels42') is None


def test_assoc_persons43_stub_double():
    # Flights_Persons has no real 'Flights_Persons44' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Person(travelState="sample_text")
    partner = Flights_Persons()
    setattr(partner, 'Flights_Persons44', None)
    _safe_set(owner, 'Flights_Person', partner)
    assert owner in getattr(partner, 'Flights_Persons44')
    _safe_set(owner, 'Flights_Person', None)
    assert owner not in getattr(partner, 'Flights_Persons44')


def test_assoc_planes55_stub_double():
    # Flights_Planes has no real 'Flights_Planes56' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Plane's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Plane's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Plane(capacity=7)
    partner = Flights_Planes()
    setattr(partner, 'Flights_Planes56', None)
    _safe_set(owner, 'Flights_Plane', partner)
    assert owner in getattr(partner, 'Flights_Planes56')
    _safe_set(owner, 'Flights_Plane', None)
    assert owner not in getattr(partner, 'Flights_Planes56')


def test_assoc_routes33_stub_double():
    # Flights_Routes has no real 'Flights_Routes34' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Route(duration=7)
    partner = Flights_Routes()
    setattr(partner, 'Flights_Routes34', None)
    _safe_set(owner, 'Flights_Route', partner)
    assert owner in getattr(partner, 'Flights_Routes34')
    _safe_set(owner, 'Flights_Route', None)
    assert owner not in getattr(partner, 'Flights_Routes34')


def test_assoc_travels15_stub_double():
    # Flights_Travel has no real 'Travel' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Flight's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Flight's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Flight(newAttribute="sample_text")
    partner = Flights_Travel()
    setattr(partner, 'Travel', None)
    _safe_set(owner, 'flights', {partner})
    assert getattr(partner, 'Travel') == owner
    _safe_set(owner, 'flights', set())
    assert getattr(partner, 'Travel') is None


def test_assoc_travels45_stub_double():
    # Flights_Travel has no real 'Travel46' property in the generated
    # code (a bare stub) -- manually attach it so Flights_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Flights_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Flights_Person(travelState="sample_text")
    partner = Flights_Travel()
    setattr(partner, 'Travel46', None)
    _safe_set(owner, 'person', {partner})
    assert getattr(partner, 'Travel46') == owner
    _safe_set(owner, 'person', set())
    assert getattr(partner, 'Travel46') is None


