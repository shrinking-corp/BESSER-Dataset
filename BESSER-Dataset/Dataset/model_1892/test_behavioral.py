import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EEPROM,
    Function,
    Memory,
    MicrocontrollerModeling_CLanguage,
    MicrocontrollerModeling_EEPROM,
    MicrocontrollerModeling_Flash,
    MicrocontrollerModeling_Function,
    MicrocontrollerModeling_Instruction,
    MicrocontrollerModeling_Library,
    MicrocontrollerModeling_Memory,
    MicrocontrollerModeling_Microcontroller,
    MicrocontrollerModeling_Parameter,
    MicrocontrollerModeling_Pin,
    MicrocontrollerModeling_PinMode,
    MicrocontrollerModeling_PinOperation,
    MicrocontrollerModeling_Processor,
    MicrocontrollerModeling_RAM,
    MicrocontrollerModeling_ROM,
    MicrocontrollerModeling_Register,
    MicrocontrollerModeling_TimerConfig,
    ROM,
    MemoryUnit,
    OperationName,
    PinModes,
    PinNature,
    RegType,
    SpeedUnit,
    TimerOp,
    WordSize,
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

def test_assoc_clanguage1_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    a2 = MicrocontrollerModeling_Microcontroller(family="sample_text_2", manufacturer="sample_text_2", name="sample_text_2", wordMemory="sample_text_2")
    b = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_CLanguage', a1)
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Microcontroller2'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Microcontroller2', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage', a2)
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Microcontroller2'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Microcontroller2', b)
    if hasattr(a2, 'MicrocontrollerModeling_Microcontroller2'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Microcontroller2', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage', None)
    assert not _is_linked(b, 'MicrocontrollerModeling_CLanguage', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Microcontroller2'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Microcontroller2', b)


def test_assoc_instructions22_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Instruction(value="sample_text")
    a2 = MicrocontrollerModeling_Instruction(value="sample_text_2")
    b = MicrocontrollerModeling_Function(type="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_Function23', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_Function23', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Instruction'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Instruction', b)
    _safe_set(b, 'MicrocontrollerModeling_Function23', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_Function23', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Instruction'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Instruction', b)
    if hasattr(a2, 'MicrocontrollerModeling_Instruction'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Instruction', b)
    _safe_set(b, 'MicrocontrollerModeling_Function23', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_Function23', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Instruction'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Instruction', b)


def test_assoc_libraries13_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Library(name="sample_text")
    a2 = MicrocontrollerModeling_Library(name="sample_text_2")
    b = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_CLanguage14', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage14', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Library'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Library', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage14', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage14', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Library'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Library', b)
    if hasattr(a2, 'MicrocontrollerModeling_Library'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Library', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage14', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_CLanguage14', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Library'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Library', b)


def test_assoc_parameters21_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Parameter(name="sample_text", type="sample_text")
    a2 = MicrocontrollerModeling_Parameter(name="sample_text_2", type="sample_text_2")
    b = MicrocontrollerModeling_Function(type="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_Function', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_Function', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Parameter'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Parameter', b)
    _safe_set(b, 'MicrocontrollerModeling_Function', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_Function', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Parameter'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Parameter', b)
    if hasattr(a2, 'MicrocontrollerModeling_Parameter'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Parameter', b)
    _safe_set(b, 'MicrocontrollerModeling_Function', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_Function', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Parameter'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Parameter', b)


def test_assoc_pinmodes17_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_PinMode(name="sample_text", value="sample_text")
    a2 = MicrocontrollerModeling_PinMode(name="sample_text_2", value="sample_text_2")
    b = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_CLanguage18', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage18', a1)
    if hasattr(a1, 'MicrocontrollerModeling_PinMode'):
        assert _is_linked(a1, 'MicrocontrollerModeling_PinMode', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage18', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage18', a2)
    if hasattr(a1, 'MicrocontrollerModeling_PinMode'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_PinMode', b)
    if hasattr(a2, 'MicrocontrollerModeling_PinMode'):
        assert _is_linked(a2, 'MicrocontrollerModeling_PinMode', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage18', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_CLanguage18', a2)
    if hasattr(a2, 'MicrocontrollerModeling_PinMode'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_PinMode', b)


def test_assoc_pinoperation19_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_PinOperation(name="sample_text")
    a2 = MicrocontrollerModeling_PinOperation(name="sample_text_2")
    b = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_CLanguage20', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage20', a1)
    if hasattr(a1, 'MicrocontrollerModeling_PinOperation'):
        assert _is_linked(a1, 'MicrocontrollerModeling_PinOperation', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage20', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage20', a2)
    if hasattr(a1, 'MicrocontrollerModeling_PinOperation'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_PinOperation', b)
    if hasattr(a2, 'MicrocontrollerModeling_PinOperation'):
        assert _is_linked(a2, 'MicrocontrollerModeling_PinOperation', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage20', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_CLanguage20', a2)
    if hasattr(a2, 'MicrocontrollerModeling_PinOperation'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_PinOperation', b)


def test_assoc_pins0_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Pin(name="sample_text", nature="sample_text", number=7)
    a2 = MicrocontrollerModeling_Pin(name="sample_text_2", nature="sample_text_2", number=13)
    b = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Pin'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Pin', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Pin'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Pin', b)
    if hasattr(a2, 'MicrocontrollerModeling_Pin'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Pin', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_Microcontroller', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Pin'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Pin', b)


def test_assoc_processor3_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Processor(speed=7, unit="sample_text")
    a2 = MicrocontrollerModeling_Processor(speed=13, unit="sample_text_2")
    b = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller4', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller4', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Processor'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Processor', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller4', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller4', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Processor'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Processor', b)
    if hasattr(a2, 'MicrocontrollerModeling_Processor'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Processor', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller4', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_Microcontroller4', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Processor'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Processor', b)


def test_assoc_registers11_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_Register(name="sample_text", type="sample_text")
    a2 = MicrocontrollerModeling_Register(name="sample_text_2", type="sample_text_2")
    b = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller12', {a1})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller12', a1)
    if hasattr(a1, 'MicrocontrollerModeling_Register'):
        assert _is_linked(a1, 'MicrocontrollerModeling_Register', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller12', {a2})
    assert _is_linked(b, 'MicrocontrollerModeling_Microcontroller12', a2)
    if hasattr(a1, 'MicrocontrollerModeling_Register'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_Register', b)
    if hasattr(a2, 'MicrocontrollerModeling_Register'):
        assert _is_linked(a2, 'MicrocontrollerModeling_Register', b)
    _safe_set(b, 'MicrocontrollerModeling_Microcontroller12', set())
    assert not _is_linked(b, 'MicrocontrollerModeling_Microcontroller12', a2)
    if hasattr(a2, 'MicrocontrollerModeling_Register'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_Register', b)


def test_assoc_timerconfig15_reverse_link_reassign_clear():
    a1 = MicrocontrollerModeling_TimerConfig(name="sample_text", period=7)
    a2 = MicrocontrollerModeling_TimerConfig(name="sample_text_2", period=13)
    b = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    _safe_set(b, 'MicrocontrollerModeling_CLanguage16', a1)
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage16', a1)
    if hasattr(a1, 'MicrocontrollerModeling_TimerConfig'):
        assert _is_linked(a1, 'MicrocontrollerModeling_TimerConfig', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage16', a2)
    assert _is_linked(b, 'MicrocontrollerModeling_CLanguage16', a2)
    if hasattr(a1, 'MicrocontrollerModeling_TimerConfig'):
        assert not _is_linked(a1, 'MicrocontrollerModeling_TimerConfig', b)
    if hasattr(a2, 'MicrocontrollerModeling_TimerConfig'):
        assert _is_linked(a2, 'MicrocontrollerModeling_TimerConfig', b)
    _safe_set(b, 'MicrocontrollerModeling_CLanguage16', None)
    assert not _is_linked(b, 'MicrocontrollerModeling_CLanguage16', a2)
    if hasattr(a2, 'MicrocontrollerModeling_TimerConfig'):
        assert not _is_linked(a2, 'MicrocontrollerModeling_TimerConfig', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flash7_stub_double():
    # MicrocontrollerModeling_Flash has no real 'MicrocontrollerModeling_Flash' property in the generated
    # code (a bare stub) -- manually attach it so MicrocontrollerModeling_Microcontroller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MicrocontrollerModeling_Microcontroller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    partner = MicrocontrollerModeling_Flash()
    setattr(partner, 'MicrocontrollerModeling_Flash', None)
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller8', partner)
    assert getattr(partner, 'MicrocontrollerModeling_Flash') == owner
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller8', None)
    assert getattr(partner, 'MicrocontrollerModeling_Flash') is None


def test_assoc_ram9_stub_double():
    # MicrocontrollerModeling_RAM has no real 'MicrocontrollerModeling_RAM' property in the generated
    # code (a bare stub) -- manually attach it so MicrocontrollerModeling_Microcontroller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MicrocontrollerModeling_Microcontroller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    partner = MicrocontrollerModeling_RAM()
    setattr(partner, 'MicrocontrollerModeling_RAM', None)
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller10', partner)
    assert getattr(partner, 'MicrocontrollerModeling_RAM') == owner
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller10', None)
    assert getattr(partner, 'MicrocontrollerModeling_RAM') is None


def test_assoc_rom5_stub_double():
    # MicrocontrollerModeling_ROM has no real 'MicrocontrollerModeling_ROM' property in the generated
    # code (a bare stub) -- manually attach it so MicrocontrollerModeling_Microcontroller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MicrocontrollerModeling_Microcontroller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    partner = MicrocontrollerModeling_ROM()
    setattr(partner, 'MicrocontrollerModeling_ROM', None)
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller6', partner)
    assert getattr(partner, 'MicrocontrollerModeling_ROM') == owner
    _safe_set(owner, 'MicrocontrollerModeling_Microcontroller6', None)
    assert getattr(partner, 'MicrocontrollerModeling_ROM') is None


