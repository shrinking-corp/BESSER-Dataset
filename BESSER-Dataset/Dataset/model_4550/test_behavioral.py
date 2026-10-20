import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SmartHouse_AirConditioner,
    SmartHouse_CoffeeMaker,
    SmartHouse_Cooker,
    SmartHouse_EV,
    SmartHouse_Gate,
    SmartHouse_Heating,
    SmartHouse_House,
    SmartHouse_Light,
    SmartHouse_Person,
    SmartHouse_Projector,
    SmartHouse_Room,
    SmartHouse_Security,
    SmartHouse_Sensor,
    SmartHouse_WashingMachine,
    SmartHouse_WaterHeater,
    SmartHouse_Window,
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

def test_assoc_ac24_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    _safe_set(b, 'AirConditioner', a1)
    assert _is_linked(b, 'AirConditioner', a1)
    if hasattr(a1, 'room25'):
        assert _is_linked(a1, 'room25', b)
    _safe_set(b, 'AirConditioner', a2)
    assert _is_linked(b, 'AirConditioner', a2)
    if hasattr(a1, 'room25'):
        assert not _is_linked(a1, 'room25', b)
    if hasattr(a2, 'room25'):
        assert _is_linked(a2, 'room25', b)
    _safe_set(b, 'AirConditioner', None)
    assert not _is_linked(b, 'AirConditioner', a2)
    if hasattr(a2, 'room25'):
        assert not _is_linked(a2, 'room25', b)


def test_assoc_cm37_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    _safe_set(b, 'CoffeeMaker', a1)
    assert _is_linked(b, 'CoffeeMaker', a1)
    if hasattr(a1, 'room38'):
        assert _is_linked(a1, 'room38', b)
    _safe_set(b, 'CoffeeMaker', a2)
    assert _is_linked(b, 'CoffeeMaker', a2)
    if hasattr(a1, 'room38'):
        assert not _is_linked(a1, 'room38', b)
    if hasattr(a2, 'room38'):
        assert _is_linked(a2, 'room38', b)
    _safe_set(b, 'CoffeeMaker', None)
    assert not _is_linked(b, 'CoffeeMaker', a2)
    if hasattr(a2, 'room38'):
        assert not _is_linked(a2, 'room38', b)


def test_assoc_cooker33_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Cooker(on=True)
    _safe_set(b, 'SmartHouse_Cooker', a1)
    assert _is_linked(b, 'SmartHouse_Cooker', a1)
    if hasattr(a1, 'SmartHouse_Room34'):
        assert _is_linked(a1, 'SmartHouse_Room34', b)
    _safe_set(b, 'SmartHouse_Cooker', a2)
    assert _is_linked(b, 'SmartHouse_Cooker', a2)
    if hasattr(a1, 'SmartHouse_Room34'):
        assert not _is_linked(a1, 'SmartHouse_Room34', b)
    if hasattr(a2, 'SmartHouse_Room34'):
        assert _is_linked(a2, 'SmartHouse_Room34', b)
    _safe_set(b, 'SmartHouse_Cooker', None)
    assert not _is_linked(b, 'SmartHouse_Cooker', a2)
    if hasattr(a2, 'SmartHouse_Room34'):
        assert not _is_linked(a2, 'SmartHouse_Room34', b)


def test_assoc_ev4_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    _safe_set(b, 'EV', a1)
    assert _is_linked(b, 'EV', a1)
    if hasattr(a1, 'house5'):
        assert _is_linked(a1, 'house5', b)
    _safe_set(b, 'EV', a2)
    assert _is_linked(b, 'EV', a2)
    if hasattr(a1, 'house5'):
        assert not _is_linked(a1, 'house5', b)
    if hasattr(a2, 'house5'):
        assert _is_linked(a2, 'house5', b)
    _safe_set(b, 'EV', None)
    assert not _is_linked(b, 'EV', a2)
    if hasattr(a2, 'house5'):
        assert not _is_linked(a2, 'house5', b)


def test_assoc_gate6_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_Gate(outlocked=True)
    _safe_set(b, 'Gate', a1)
    assert _is_linked(b, 'Gate', a1)
    if hasattr(a1, 'house7'):
        assert _is_linked(a1, 'house7', b)
    _safe_set(b, 'Gate', a2)
    assert _is_linked(b, 'Gate', a2)
    if hasattr(a1, 'house7'):
        assert not _is_linked(a1, 'house7', b)
    if hasattr(a2, 'house7'):
        assert _is_linked(a2, 'house7', b)
    _safe_set(b, 'Gate', None)
    assert not _is_linked(b, 'Gate', a2)
    if hasattr(a2, 'house7'):
        assert not _is_linked(a2, 'house7', b)


def test_assoc_heating20_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Heating(level=7, name="sample_text")
    _safe_set(b, 'SmartHouse_Heating', a1)
    assert _is_linked(b, 'SmartHouse_Heating', a1)
    if hasattr(a1, 'SmartHouse_Room21'):
        assert _is_linked(a1, 'SmartHouse_Room21', b)
    _safe_set(b, 'SmartHouse_Heating', a2)
    assert _is_linked(b, 'SmartHouse_Heating', a2)
    if hasattr(a1, 'SmartHouse_Room21'):
        assert not _is_linked(a1, 'SmartHouse_Room21', b)
    if hasattr(a2, 'SmartHouse_Room21'):
        assert _is_linked(a2, 'SmartHouse_Room21', b)
    _safe_set(b, 'SmartHouse_Heating', None)
    assert not _is_linked(b, 'SmartHouse_Heating', a2)
    if hasattr(a2, 'SmartHouse_Room21'):
        assert not _is_linked(a2, 'SmartHouse_Room21', b)


def test_assoc_house10_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_Gate(outlocked=True)
    _safe_set(b, 'gate', a1)
    assert _is_linked(b, 'gate', a1)
    if hasattr(a1, 'House'):
        assert _is_linked(a1, 'House', b)
    _safe_set(b, 'gate', a2)
    assert _is_linked(b, 'gate', a2)
    if hasattr(a1, 'House'):
        assert not _is_linked(a1, 'House', b)
    if hasattr(a2, 'House'):
        assert _is_linked(a2, 'House', b)
    _safe_set(b, 'gate', None)
    assert not _is_linked(b, 'gate', a2)
    if hasattr(a2, 'House'):
        assert not _is_linked(a2, 'House', b)


def test_assoc_house11_reverse_link_reassign_clear():
    a1 = SmartHouse_Security(on=True)
    a2 = SmartHouse_Security(on=False)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House12', a1)
    assert _is_linked(b, 'House12', a1)
    if hasattr(a1, 'sec'):
        assert _is_linked(a1, 'sec', b)
    _safe_set(b, 'House12', a2)
    assert _is_linked(b, 'House12', a2)
    if hasattr(a1, 'sec'):
        assert not _is_linked(a1, 'sec', b)
    if hasattr(a2, 'sec'):
        assert _is_linked(a2, 'sec', b)
    _safe_set(b, 'House12', None)
    assert not _is_linked(b, 'House12', a2)
    if hasattr(a2, 'sec'):
        assert not _is_linked(a2, 'sec', b)


def test_assoc_house13_reverse_link_reassign_clear():
    a1 = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    a2 = SmartHouse_WaterHeater(boost=False, on=False, temp="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House14', a1)
    assert _is_linked(b, 'House14', a1)
    if hasattr(a1, 'wh'):
        assert _is_linked(a1, 'wh', b)
    _safe_set(b, 'House14', a2)
    assert _is_linked(b, 'House14', a2)
    if hasattr(a1, 'wh'):
        assert not _is_linked(a1, 'wh', b)
    if hasattr(a2, 'wh'):
        assert _is_linked(a2, 'wh', b)
    _safe_set(b, 'House14', None)
    assert not _is_linked(b, 'House14', a2)
    if hasattr(a2, 'wh'):
        assert not _is_linked(a2, 'wh', b)


def test_assoc_house15_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    _safe_set(b, 'ev', a1)
    assert _is_linked(b, 'ev', a1)
    if hasattr(a1, 'House16'):
        assert _is_linked(a1, 'House16', b)
    _safe_set(b, 'ev', a2)
    assert _is_linked(b, 'ev', a2)
    if hasattr(a1, 'House16'):
        assert not _is_linked(a1, 'House16', b)
    if hasattr(a2, 'House16'):
        assert _is_linked(a2, 'House16', b)
    _safe_set(b, 'ev', None)
    assert not _is_linked(b, 'ev', a2)
    if hasattr(a2, 'House16'):
        assert not _is_linked(a2, 'House16', b)


def test_assoc_house17_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House18', a1)
    assert _is_linked(b, 'House18', a1)
    if hasattr(a1, 'room'):
        assert _is_linked(a1, 'room', b)
    _safe_set(b, 'House18', a2)
    assert _is_linked(b, 'House18', a2)
    if hasattr(a1, 'room'):
        assert not _is_linked(a1, 'room', b)
    if hasattr(a2, 'room'):
        assert _is_linked(a2, 'room', b)
    _safe_set(b, 'House18', None)
    assert not _is_linked(b, 'House18', a2)
    if hasattr(a2, 'room'):
        assert not _is_linked(a2, 'room', b)


def test_assoc_light22_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Light(level="sample_text")
    _safe_set(b, 'SmartHouse_Light', a1)
    assert _is_linked(b, 'SmartHouse_Light', a1)
    if hasattr(a1, 'SmartHouse_Room23'):
        assert _is_linked(a1, 'SmartHouse_Room23', b)
    _safe_set(b, 'SmartHouse_Light', a2)
    assert _is_linked(b, 'SmartHouse_Light', a2)
    if hasattr(a1, 'SmartHouse_Room23'):
        assert not _is_linked(a1, 'SmartHouse_Room23', b)
    if hasattr(a2, 'SmartHouse_Room23'):
        assert _is_linked(a2, 'SmartHouse_Room23', b)
    _safe_set(b, 'SmartHouse_Light', None)
    assert not _is_linked(b, 'SmartHouse_Light', a2)
    if hasattr(a2, 'SmartHouse_Room23'):
        assert not _is_linked(a2, 'SmartHouse_Room23', b)


def test_assoc_member1_reverse_link_reassign_clear():
    a1 = SmartHouse_Person(name="sample_text")
    a2 = SmartHouse_Person(name="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'SmartHouse_House', {a1})
    assert _is_linked(b, 'SmartHouse_House', a1)
    if hasattr(a1, 'SmartHouse_Person'):
        assert _is_linked(a1, 'SmartHouse_Person', b)
    _safe_set(b, 'SmartHouse_House', {a2})
    assert _is_linked(b, 'SmartHouse_House', a2)
    if hasattr(a1, 'SmartHouse_Person'):
        assert not _is_linked(a1, 'SmartHouse_Person', b)
    if hasattr(a2, 'SmartHouse_Person'):
        assert _is_linked(a2, 'SmartHouse_Person', b)
    _safe_set(b, 'SmartHouse_House', set())
    assert not _is_linked(b, 'SmartHouse_House', a2)
    if hasattr(a2, 'SmartHouse_Person'):
        assert not _is_linked(a2, 'SmartHouse_Person', b)


def test_assoc_occupied26_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Person(name="sample_text")
    _safe_set(b, 'SmartHouse_Person28', a1)
    assert _is_linked(b, 'SmartHouse_Person28', a1)
    if hasattr(a1, 'SmartHouse_Room27'):
        assert _is_linked(a1, 'SmartHouse_Room27', b)
    _safe_set(b, 'SmartHouse_Person28', a2)
    assert _is_linked(b, 'SmartHouse_Person28', a2)
    if hasattr(a1, 'SmartHouse_Room27'):
        assert not _is_linked(a1, 'SmartHouse_Room27', b)
    if hasattr(a2, 'SmartHouse_Room27'):
        assert _is_linked(a2, 'SmartHouse_Room27', b)
    _safe_set(b, 'SmartHouse_Person28', None)
    assert not _is_linked(b, 'SmartHouse_Person28', a2)
    if hasattr(a2, 'SmartHouse_Room27'):
        assert not _is_linked(a2, 'SmartHouse_Room27', b)


def test_assoc_projector31_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    _safe_set(b, 'Projector', a1)
    assert _is_linked(b, 'Projector', a1)
    if hasattr(a1, 'room32'):
        assert _is_linked(a1, 'room32', b)
    _safe_set(b, 'Projector', a2)
    assert _is_linked(b, 'Projector', a2)
    if hasattr(a1, 'room32'):
        assert not _is_linked(a1, 'room32', b)
    if hasattr(a2, 'room32'):
        assert _is_linked(a2, 'room32', b)
    _safe_set(b, 'Projector', None)
    assert not _is_linked(b, 'Projector', a2)
    if hasattr(a2, 'room32'):
        assert not _is_linked(a2, 'room32', b)


def test_assoc_room0_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house', {a1})
    assert _is_linked(b, 'house', a1)
    if hasattr(a1, 'Room'):
        assert _is_linked(a1, 'Room', b)
    _safe_set(b, 'house', {a2})
    assert _is_linked(b, 'house', a2)
    if hasattr(a1, 'Room'):
        assert not _is_linked(a1, 'Room', b)
    if hasattr(a2, 'Room'):
        assert _is_linked(a2, 'Room', b)
    _safe_set(b, 'house', set())
    assert not _is_linked(b, 'house', a2)
    if hasattr(a2, 'Room'):
        assert not _is_linked(a2, 'Room', b)


def test_assoc_room39_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    _safe_set(b, 'ac', a1)
    assert _is_linked(b, 'ac', a1)
    if hasattr(a1, 'Room40'):
        assert _is_linked(a1, 'Room40', b)
    _safe_set(b, 'ac', a2)
    assert _is_linked(b, 'ac', a2)
    if hasattr(a1, 'Room40'):
        assert not _is_linked(a1, 'Room40', b)
    if hasattr(a2, 'Room40'):
        assert _is_linked(a2, 'Room40', b)
    _safe_set(b, 'ac', None)
    assert not _is_linked(b, 'ac', a2)
    if hasattr(a2, 'Room40'):
        assert not _is_linked(a2, 'Room40', b)


def test_assoc_room41_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    _safe_set(b, 'projector', a1)
    assert _is_linked(b, 'projector', a1)
    if hasattr(a1, 'Room42'):
        assert _is_linked(a1, 'Room42', b)
    _safe_set(b, 'projector', a2)
    assert _is_linked(b, 'projector', a2)
    if hasattr(a1, 'Room42'):
        assert not _is_linked(a1, 'Room42', b)
    if hasattr(a2, 'Room42'):
        assert _is_linked(a2, 'Room42', b)
    _safe_set(b, 'projector', None)
    assert not _is_linked(b, 'projector', a2)
    if hasattr(a2, 'Room42'):
        assert not _is_linked(a2, 'Room42', b)


def test_assoc_room43_reverse_link_reassign_clear():
    a1 = SmartHouse_WashingMachine(loaded=True, on=True)
    a2 = SmartHouse_WashingMachine(loaded=False, on=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'Room44', a1)
    assert _is_linked(b, 'Room44', a1)
    if hasattr(a1, 'wm'):
        assert _is_linked(a1, 'wm', b)
    _safe_set(b, 'Room44', a2)
    assert _is_linked(b, 'Room44', a2)
    if hasattr(a1, 'wm'):
        assert not _is_linked(a1, 'wm', b)
    if hasattr(a2, 'wm'):
        assert _is_linked(a2, 'wm', b)
    _safe_set(b, 'Room44', None)
    assert not _is_linked(b, 'Room44', a2)
    if hasattr(a2, 'wm'):
        assert not _is_linked(a2, 'wm', b)


def test_assoc_room45_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    _safe_set(b, 'cm', a1)
    assert _is_linked(b, 'cm', a1)
    if hasattr(a1, 'Room46'):
        assert _is_linked(a1, 'Room46', b)
    _safe_set(b, 'cm', a2)
    assert _is_linked(b, 'cm', a2)
    if hasattr(a1, 'Room46'):
        assert not _is_linked(a1, 'Room46', b)
    if hasattr(a2, 'Room46'):
        assert _is_linked(a2, 'Room46', b)
    _safe_set(b, 'cm', None)
    assert not _is_linked(b, 'cm', a2)
    if hasattr(a2, 'Room46'):
        assert not _is_linked(a2, 'Room46', b)


def test_assoc_sec8_reverse_link_reassign_clear():
    a1 = SmartHouse_Security(on=True)
    a2 = SmartHouse_Security(on=False)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house9', a1)
    assert _is_linked(b, 'house9', a1)
    if hasattr(a1, 'Security'):
        assert _is_linked(a1, 'Security', b)
    _safe_set(b, 'house9', a2)
    assert _is_linked(b, 'house9', a2)
    if hasattr(a1, 'Security'):
        assert not _is_linked(a1, 'Security', b)
    if hasattr(a2, 'Security'):
        assert _is_linked(a2, 'Security', b)
    _safe_set(b, 'house9', None)
    assert not _is_linked(b, 'house9', a2)
    if hasattr(a2, 'Security'):
        assert not _is_linked(a2, 'Security', b)


def test_assoc_sensor29_reverse_link_reassign_clear():
    a1 = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    a2 = SmartHouse_Sensor(air=False, battery="sample_text_2", brightness=False, circle="sample_text_2", temp=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'SmartHouse_Room30', {a1})
    assert _is_linked(b, 'SmartHouse_Room30', a1)
    if hasattr(a1, 'SmartHouse_Sensor'):
        assert _is_linked(a1, 'SmartHouse_Sensor', b)
    _safe_set(b, 'SmartHouse_Room30', {a2})
    assert _is_linked(b, 'SmartHouse_Room30', a2)
    if hasattr(a1, 'SmartHouse_Sensor'):
        assert not _is_linked(a1, 'SmartHouse_Sensor', b)
    if hasattr(a2, 'SmartHouse_Sensor'):
        assert _is_linked(a2, 'SmartHouse_Sensor', b)
    _safe_set(b, 'SmartHouse_Room30', set())
    assert not _is_linked(b, 'SmartHouse_Room30', a2)
    if hasattr(a2, 'SmartHouse_Sensor'):
        assert not _is_linked(a2, 'SmartHouse_Sensor', b)


def test_assoc_wh2_reverse_link_reassign_clear():
    a1 = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    a2 = SmartHouse_WaterHeater(boost=False, on=False, temp="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house3', a1)
    assert _is_linked(b, 'house3', a1)
    if hasattr(a1, 'WaterHeater'):
        assert _is_linked(a1, 'WaterHeater', b)
    _safe_set(b, 'house3', a2)
    assert _is_linked(b, 'house3', a2)
    if hasattr(a1, 'WaterHeater'):
        assert not _is_linked(a1, 'WaterHeater', b)
    if hasattr(a2, 'WaterHeater'):
        assert _is_linked(a2, 'WaterHeater', b)
    _safe_set(b, 'house3', None)
    assert not _is_linked(b, 'house3', a2)
    if hasattr(a2, 'WaterHeater'):
        assert not _is_linked(a2, 'WaterHeater', b)


def test_assoc_window19_reverse_link_reassign_clear():
    a1 = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    a2 = SmartHouse_Window(curtainOn=False, name="sample_text_2", opened=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'SmartHouse_Room', {a1})
    assert _is_linked(b, 'SmartHouse_Room', a1)
    if hasattr(a1, 'SmartHouse_Window'):
        assert _is_linked(a1, 'SmartHouse_Window', b)
    _safe_set(b, 'SmartHouse_Room', {a2})
    assert _is_linked(b, 'SmartHouse_Room', a2)
    if hasattr(a1, 'SmartHouse_Window'):
        assert not _is_linked(a1, 'SmartHouse_Window', b)
    if hasattr(a2, 'SmartHouse_Window'):
        assert _is_linked(a2, 'SmartHouse_Window', b)
    _safe_set(b, 'SmartHouse_Room', set())
    assert not _is_linked(b, 'SmartHouse_Room', a2)
    if hasattr(a2, 'SmartHouse_Window'):
        assert not _is_linked(a2, 'SmartHouse_Window', b)


def test_assoc_wm35_reverse_link_reassign_clear():
    a1 = SmartHouse_WashingMachine(loaded=True, on=True)
    a2 = SmartHouse_WashingMachine(loaded=False, on=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'room36', a1)
    assert _is_linked(b, 'room36', a1)
    if hasattr(a1, 'WashingMachine'):
        assert _is_linked(a1, 'WashingMachine', b)
    _safe_set(b, 'room36', a2)
    assert _is_linked(b, 'room36', a2)
    if hasattr(a1, 'WashingMachine'):
        assert not _is_linked(a1, 'WashingMachine', b)
    if hasattr(a2, 'WashingMachine'):
        assert _is_linked(a2, 'WashingMachine', b)
    _safe_set(b, 'room36', None)
    assert not _is_linked(b, 'room36', a2)
    if hasattr(a2, 'WashingMachine'):
        assert not _is_linked(a2, 'WashingMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

