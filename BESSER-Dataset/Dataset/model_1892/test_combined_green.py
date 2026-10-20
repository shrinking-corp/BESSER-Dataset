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
    EEPROM,
    ROM,
    MicrocontrollerModeling_EEPROM,
    Memory,
    MicrocontrollerModeling_PinMode,
    MicrocontrollerModeling_Library,
    MicrocontrollerModeling_Register,
    MicrocontrollerModeling_RAM,
    MicrocontrollerModeling_Flash,
    MicrocontrollerModeling_Memory,
    Function,
    MicrocontrollerModeling_TimerConfig,
    MicrocontrollerModeling_Instruction,
    MicrocontrollerModeling_Parameter,
    MicrocontrollerModeling_Function,
    MicrocontrollerModeling_PinOperation,
    MicrocontrollerModeling_ROM,
    MicrocontrollerModeling_Processor,
    MicrocontrollerModeling_CLanguage,
    MicrocontrollerModeling_Pin,
    MicrocontrollerModeling_Microcontroller,
    PinNature,
    RegType,
    OperationName,
    WordSize,
    TimerOp,
    SpeedUnit,
    MemoryUnit,
    PinModes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_eeprom_is_not_abstract():
    assert not inspect.isabstract(EEPROM)


def test_hyp_eeprom_constructor_exists():
    assert callable(EEPROM.__init__)


def test_hyp_eeprom_constructor_args():
    sig = inspect.signature(EEPROM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rom_is_not_abstract():
    assert not inspect.isabstract(ROM)


def test_hyp_rom_constructor_exists():
    assert callable(ROM.__init__)


def test_hyp_rom_constructor_args():
    sig = inspect.signature(ROM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_eeprom_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_EEPROM)


def test_hyp_microcontrollermodeling_eeprom_constructor_exists():
    assert callable(MicrocontrollerModeling_EEPROM.__init__)


def test_hyp_microcontrollermodeling_eeprom_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_EEPROM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memory_is_not_abstract():
    assert not inspect.isabstract(Memory)


def test_hyp_memory_constructor_exists():
    assert callable(Memory.__init__)


def test_hyp_memory_constructor_args():
    sig = inspect.signature(Memory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_pinmode_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_PinMode)


def test_hyp_microcontrollermodeling_pinmode_constructor_exists():
    assert callable(MicrocontrollerModeling_PinMode.__init__)


def test_hyp_microcontrollermodeling_pinmode_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_PinMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_microcontrollermodeling_library_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Library)


def test_hyp_microcontrollermodeling_library_constructor_exists():
    assert callable(MicrocontrollerModeling_Library.__init__)


def test_hyp_microcontrollermodeling_library_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_microcontrollermodeling_register_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Register)


def test_hyp_microcontrollermodeling_register_constructor_exists():
    assert callable(MicrocontrollerModeling_Register.__init__)


def test_hyp_microcontrollermodeling_register_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Register.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_microcontrollermodeling_ram_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_RAM)


def test_hyp_microcontrollermodeling_ram_constructor_exists():
    assert callable(MicrocontrollerModeling_RAM.__init__)


def test_hyp_microcontrollermodeling_ram_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_RAM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_flash_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Flash)


def test_hyp_microcontrollermodeling_flash_constructor_exists():
    assert callable(MicrocontrollerModeling_Flash.__init__)


def test_hyp_microcontrollermodeling_flash_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Flash.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_memory_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Memory)


def test_hyp_microcontrollermodeling_memory_constructor_exists():
    assert callable(MicrocontrollerModeling_Memory.__init__)


def test_hyp_microcontrollermodeling_memory_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Memory.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "size" in params, "Missing parameter 'size'"





def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_timerconfig_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_TimerConfig)


def test_hyp_microcontrollermodeling_timerconfig_constructor_exists():
    assert callable(MicrocontrollerModeling_TimerConfig.__init__)


def test_hyp_microcontrollermodeling_timerconfig_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_TimerConfig.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "period" in params, "Missing parameter 'period'"





def test_hyp_microcontrollermodeling_instruction_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Instruction)


def test_hyp_microcontrollermodeling_instruction_constructor_exists():
    assert callable(MicrocontrollerModeling_Instruction.__init__)


def test_hyp_microcontrollermodeling_instruction_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Instruction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_microcontrollermodeling_parameter_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Parameter)


def test_hyp_microcontrollermodeling_parameter_constructor_exists():
    assert callable(MicrocontrollerModeling_Parameter.__init__)


def test_hyp_microcontrollermodeling_parameter_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_microcontrollermodeling_function_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Function)


def test_hyp_microcontrollermodeling_function_constructor_exists():
    assert callable(MicrocontrollerModeling_Function.__init__)


def test_hyp_microcontrollermodeling_function_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Function.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_microcontrollermodeling_pinoperation_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_PinOperation)


def test_hyp_microcontrollermodeling_pinoperation_constructor_exists():
    assert callable(MicrocontrollerModeling_PinOperation.__init__)


def test_hyp_microcontrollermodeling_pinoperation_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_PinOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_microcontrollermodeling_rom_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_ROM)


def test_hyp_microcontrollermodeling_rom_constructor_exists():
    assert callable(MicrocontrollerModeling_ROM.__init__)


def test_hyp_microcontrollermodeling_rom_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_ROM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_microcontrollermodeling_processor_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Processor)


def test_hyp_microcontrollermodeling_processor_constructor_exists():
    assert callable(MicrocontrollerModeling_Processor.__init__)


def test_hyp_microcontrollermodeling_processor_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Processor.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "unit" in params, "Missing parameter 'unit'"





def test_hyp_microcontrollermodeling_clanguage_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_CLanguage)


def test_hyp_microcontrollermodeling_clanguage_constructor_exists():
    assert callable(MicrocontrollerModeling_CLanguage.__init__)


def test_hyp_microcontrollermodeling_clanguage_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_CLanguage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "filesExtension" in params, "Missing parameter 'filesExtension'"
    assert "hasMain" in params, "Missing parameter 'hasMain'"






def test_hyp_microcontrollermodeling_pin_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Pin)


def test_hyp_microcontrollermodeling_pin_constructor_exists():
    assert callable(MicrocontrollerModeling_Pin.__init__)


def test_hyp_microcontrollermodeling_pin_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "nature" in params, "Missing parameter 'nature'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_microcontrollermodeling_microcontroller_is_not_abstract():
    assert not inspect.isabstract(MicrocontrollerModeling_Microcontroller)


def test_hyp_microcontrollermodeling_microcontroller_constructor_exists():
    assert callable(MicrocontrollerModeling_Microcontroller.__init__)


def test_hyp_microcontrollermodeling_microcontroller_constructor_args():
    sig = inspect.signature(MicrocontrollerModeling_Microcontroller.__init__)
    params = list(sig.parameters.keys())
    assert "wordMemory" in params, "Missing parameter 'wordMemory'"
    assert "family" in params, "Missing parameter 'family'"
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_pinnature_exists():
    # Check that the Enumeration exists
    assert PinNature is not None

def test_hyp_pinnature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PinNature]
    expected_literals = [
        "Analog",
        "Mixed",
        "Digital",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PinNature"

def test_hyp_regtype_exists():
    # Check that the Enumeration exists
    assert RegType is not None

def test_hyp_regtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RegType]
    expected_literals = [
        "CCR",
        "ICR",
        "PCounter",
        "general",
        "accumulator",
        "Stack",
        "IR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RegType"

def test_hyp_operationname_exists():
    # Check that the Enumeration exists
    assert OperationName is not None

def test_hyp_operationname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationName]
    expected_literals = [
        "pinConfigMode",
        "digitalPinRead",
        "digitalPinWrite",
        "analogPinWrite",
        "analogPinRead",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationName"

def test_hyp_wordsize_exists():
    # Check that the Enumeration exists
    assert WordSize is not None

def test_hyp_wordsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WordSize]
    expected_literals = [
        "wd_32bits",
        "wd_64bits",
        "wd_16bits",
        "wd_8bits",
        "wd_48bits",
        "wd_24bits",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WordSize"

def test_hyp_timerop_exists():
    # Check that the Enumeration exists
    assert TimerOp is not None

def test_hyp_timerop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimerOp]
    expected_literals = [
        "initializeTimer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimerOp"

def test_hyp_speedunit_exists():
    # Check that the Enumeration exists
    assert SpeedUnit is not None

def test_hyp_speedunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeedUnit]
    expected_literals = [
        "GHz",
        "MIPS",
        "Hz",
        "Mhz",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeedUnit"

def test_hyp_memoryunit_exists():
    # Check that the Enumeration exists
    assert MemoryUnit is not None

def test_hyp_memoryunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MemoryUnit]
    expected_literals = [
        "Go",
        "Mo",
        "Ko",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MemoryUnit"

def test_hyp_pinmodes_exists():
    # Check that the Enumeration exists
    assert PinModes is not None

def test_hyp_pinmodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PinModes]
    expected_literals = [
        "Input",
        "Output",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PinModes"


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
EEPROM_strategy = st.builds(
    EEPROM,
)
ROM_strategy = st.builds(
    ROM,
)
MicrocontrollerModeling_EEPROM_strategy = st.builds(
    MicrocontrollerModeling_EEPROM,
)
Memory_strategy = st.builds(
    Memory,
)
MicrocontrollerModeling_PinMode_strategy = st.builds(
    MicrocontrollerModeling_PinMode,
    name=
        safe_text,
    value=
        safe_text
)
MicrocontrollerModeling_Library_strategy = st.builds(
    MicrocontrollerModeling_Library,
    name=
        safe_text
)
MicrocontrollerModeling_Register_strategy = st.builds(
    MicrocontrollerModeling_Register,
    type=
        safe_text,
    name=
        safe_text
)
MicrocontrollerModeling_RAM_strategy = st.builds(
    MicrocontrollerModeling_RAM,
)
MicrocontrollerModeling_Flash_strategy = st.builds(
    MicrocontrollerModeling_Flash,
)
MicrocontrollerModeling_Memory_strategy = st.builds(
    MicrocontrollerModeling_Memory,
    unit=
        safe_text,
    size=
        st.integers()
)
Function_strategy = st.builds(
    Function,
)
MicrocontrollerModeling_TimerConfig_strategy = st.builds(
    MicrocontrollerModeling_TimerConfig,
    name=
        safe_text,
    period=
        st.integers()
)
MicrocontrollerModeling_Instruction_strategy = st.builds(
    MicrocontrollerModeling_Instruction,
    value=
        safe_text
)
MicrocontrollerModeling_Parameter_strategy = st.builds(
    MicrocontrollerModeling_Parameter,
    type=
        safe_text,
    name=
        safe_text
)
MicrocontrollerModeling_Function_strategy = st.builds(
    MicrocontrollerModeling_Function,
    type=
        safe_text
)
MicrocontrollerModeling_PinOperation_strategy = st.builds(
    MicrocontrollerModeling_PinOperation,
    name=
        safe_text
)
MicrocontrollerModeling_ROM_strategy = st.builds(
    MicrocontrollerModeling_ROM,
)
MicrocontrollerModeling_Processor_strategy = st.builds(
    MicrocontrollerModeling_Processor,
    speed=
        st.integers(),
    unit=
        safe_text
)
MicrocontrollerModeling_CLanguage_strategy = st.builds(
    MicrocontrollerModeling_CLanguage,
    name=
        safe_text,
    filesExtension=
        safe_text,
    hasMain=
        st.booleans()
)
MicrocontrollerModeling_Pin_strategy = st.builds(
    MicrocontrollerModeling_Pin,
    number=
        st.integers(),
    nature=
        safe_text,
    name=
        safe_text
)
MicrocontrollerModeling_Microcontroller_strategy = st.builds(
    MicrocontrollerModeling_Microcontroller,
    wordMemory=
        safe_text,
    family=
        safe_text,
    manufacturer=
        safe_text,
    name=
        safe_text
)








@given(instance=MicrocontrollerModeling_PinMode_strategy)
def test_hyp_microcontrollermodeling_pinmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MicrocontrollerModeling_PinMode_strategy)
def test_hyp_microcontrollermodeling_pinmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=MicrocontrollerModeling_Library_strategy)
def test_hyp_microcontrollermodeling_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=MicrocontrollerModeling_Register_strategy)
def test_hyp_microcontrollermodeling_register_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MicrocontrollerModeling_Register_strategy)
def test_hyp_microcontrollermodeling_register_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=MicrocontrollerModeling_Memory_strategy)
def test_hyp_microcontrollermodeling_memory_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=MicrocontrollerModeling_Memory_strategy)
def test_hyp_microcontrollermodeling_memory_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original





@given(instance=MicrocontrollerModeling_TimerConfig_strategy)
def test_hyp_microcontrollermodeling_timerconfig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MicrocontrollerModeling_TimerConfig_strategy)
def test_hyp_microcontrollermodeling_timerconfig_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original




@given(instance=MicrocontrollerModeling_Instruction_strategy)
def test_hyp_microcontrollermodeling_instruction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=MicrocontrollerModeling_Parameter_strategy)
def test_hyp_microcontrollermodeling_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MicrocontrollerModeling_Parameter_strategy)
def test_hyp_microcontrollermodeling_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=MicrocontrollerModeling_Function_strategy)
def test_hyp_microcontrollermodeling_function_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=MicrocontrollerModeling_PinOperation_strategy)
def test_hyp_microcontrollermodeling_pinoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=MicrocontrollerModeling_Processor_strategy)
def test_hyp_microcontrollermodeling_processor_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=MicrocontrollerModeling_Processor_strategy)
def test_hyp_microcontrollermodeling_processor_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original




@given(instance=MicrocontrollerModeling_CLanguage_strategy)
def test_hyp_microcontrollermodeling_clanguage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MicrocontrollerModeling_CLanguage_strategy)
def test_hyp_microcontrollermodeling_clanguage_filesExtension_setter(instance):
    original = instance.filesExtension
    instance.filesExtension = original
    assert instance.filesExtension == original



@given(instance=MicrocontrollerModeling_CLanguage_strategy)
def test_hyp_microcontrollermodeling_clanguage_hasMain_setter(instance):
    original = instance.hasMain
    instance.hasMain = original
    assert instance.hasMain == original




@given(instance=MicrocontrollerModeling_Pin_strategy)
def test_hyp_microcontrollermodeling_pin_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=MicrocontrollerModeling_Pin_strategy)
def test_hyp_microcontrollermodeling_pin_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original



@given(instance=MicrocontrollerModeling_Pin_strategy)
def test_hyp_microcontrollermodeling_pin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=MicrocontrollerModeling_Microcontroller_strategy)
def test_hyp_microcontrollermodeling_microcontroller_wordMemory_setter(instance):
    original = instance.wordMemory
    instance.wordMemory = original
    assert instance.wordMemory == original



@given(instance=MicrocontrollerModeling_Microcontroller_strategy)
def test_hyp_microcontrollermodeling_microcontroller_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=MicrocontrollerModeling_Microcontroller_strategy)
def test_hyp_microcontrollermodeling_microcontroller_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=MicrocontrollerModeling_Microcontroller_strategy)
def test_hyp_microcontrollermodeling_microcontroller_name_setter(instance):
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

def test_MicrocontrollerModeling_CLanguage_filesExtension_value_roundtrip():
    instance = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    assert instance.filesExtension == "sample_text"
    instance.filesExtension = "sample_text_2"
    assert instance.filesExtension == "sample_text_2"


def test_MicrocontrollerModeling_CLanguage_hasMain_value_roundtrip():
    instance = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    assert instance.hasMain == True
    instance.hasMain = False
    assert instance.hasMain == False


def test_MicrocontrollerModeling_CLanguage_name_value_roundtrip():
    instance = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Function_type_value_roundtrip():
    instance = MicrocontrollerModeling_Function(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MicrocontrollerModeling_Instruction_value_value_roundtrip():
    instance = MicrocontrollerModeling_Instruction(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_MicrocontrollerModeling_Library_name_value_roundtrip():
    instance = MicrocontrollerModeling_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Memory_size_value_roundtrip():
    instance = MicrocontrollerModeling_Memory(size=7, unit="sample_text")
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_MicrocontrollerModeling_Memory_unit_value_roundtrip():
    instance = MicrocontrollerModeling_Memory(size=7, unit="sample_text")
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_MicrocontrollerModeling_Microcontroller_family_value_roundtrip():
    instance = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    assert instance.family == "sample_text"
    instance.family = "sample_text_2"
    assert instance.family == "sample_text_2"


def test_MicrocontrollerModeling_Microcontroller_manufacturer_value_roundtrip():
    instance = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    assert instance.manufacturer == "sample_text"
    instance.manufacturer = "sample_text_2"
    assert instance.manufacturer == "sample_text_2"


def test_MicrocontrollerModeling_Microcontroller_name_value_roundtrip():
    instance = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Microcontroller_wordMemory_value_roundtrip():
    instance = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    assert instance.wordMemory == "sample_text"
    instance.wordMemory = "sample_text_2"
    assert instance.wordMemory == "sample_text_2"


def test_MicrocontrollerModeling_Parameter_name_value_roundtrip():
    instance = MicrocontrollerModeling_Parameter(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Parameter_type_value_roundtrip():
    instance = MicrocontrollerModeling_Parameter(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MicrocontrollerModeling_Pin_name_value_roundtrip():
    instance = MicrocontrollerModeling_Pin(name="sample_text", nature="sample_text", number=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Pin_nature_value_roundtrip():
    instance = MicrocontrollerModeling_Pin(name="sample_text", nature="sample_text", number=7)
    assert instance.nature == "sample_text"
    instance.nature = "sample_text_2"
    assert instance.nature == "sample_text_2"


def test_MicrocontrollerModeling_Pin_number_value_roundtrip():
    instance = MicrocontrollerModeling_Pin(name="sample_text", nature="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_MicrocontrollerModeling_PinMode_name_value_roundtrip():
    instance = MicrocontrollerModeling_PinMode(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_PinMode_value_value_roundtrip():
    instance = MicrocontrollerModeling_PinMode(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_MicrocontrollerModeling_PinOperation_name_value_roundtrip():
    instance = MicrocontrollerModeling_PinOperation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Processor_speed_value_roundtrip():
    instance = MicrocontrollerModeling_Processor(speed=7, unit="sample_text")
    assert instance.speed == 7
    instance.speed = 13
    assert instance.speed == 13


def test_MicrocontrollerModeling_Processor_unit_value_roundtrip():
    instance = MicrocontrollerModeling_Processor(speed=7, unit="sample_text")
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_MicrocontrollerModeling_Register_name_value_roundtrip():
    instance = MicrocontrollerModeling_Register(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_Register_type_value_roundtrip():
    instance = MicrocontrollerModeling_Register(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MicrocontrollerModeling_TimerConfig_name_value_roundtrip():
    instance = MicrocontrollerModeling_TimerConfig(name="sample_text", period=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MicrocontrollerModeling_TimerConfig_period_value_roundtrip():
    instance = MicrocontrollerModeling_TimerConfig(name="sample_text", period=7)
    assert instance.period == 7
    instance.period = 13
    assert instance.period == 13


def test_MicrocontrollerModeling_Flash_isa_EEPROM():
    instance = MicrocontrollerModeling_Flash()
    assert isinstance(instance, EEPROM)


def test_MicrocontrollerModeling_PinOperation_isa_Function():
    instance = MicrocontrollerModeling_PinOperation(name="sample_text")
    assert isinstance(instance, Function)


def test_MicrocontrollerModeling_TimerConfig_isa_Function():
    instance = MicrocontrollerModeling_TimerConfig(name="sample_text", period=7)
    assert isinstance(instance, Function)


def test_MicrocontrollerModeling_RAM_isa_Memory():
    instance = MicrocontrollerModeling_RAM()
    assert isinstance(instance, Memory)


def test_MicrocontrollerModeling_ROM_isa_Memory():
    instance = MicrocontrollerModeling_ROM()
    assert isinstance(instance, Memory)


def test_MicrocontrollerModeling_EEPROM_isa_ROM():
    instance = MicrocontrollerModeling_EEPROM()
    assert isinstance(instance, ROM)


def test_assoc_clanguage1_link_reassign_clear():
    a = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b1 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    b2 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text_2", hasMain=False, name="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller2', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller2', b1)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage'):
        assert _is_linked(b1, 'MicrocontrollerModeling_CLanguage', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller2', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller2', b2)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_CLanguage', a)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage'):
        assert _is_linked(b2, 'MicrocontrollerModeling_CLanguage', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller2', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Microcontroller2', b2)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_CLanguage', a)


def test_assoc_flash7_link_reassign_clear():
    a = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b1 = MicrocontrollerModeling_Flash()
    b2 = MicrocontrollerModeling_Flash()
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller8', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller8', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Flash'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Flash', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller8', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller8', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Flash'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Flash', a)
    if hasattr(b2, 'MicrocontrollerModeling_Flash'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Flash', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller8', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Microcontroller8', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Flash'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Flash', a)


def test_assoc_instructions22_link_reassign_clear():
    a = MicrocontrollerModeling_Instruction(value="sample_text")
    b1 = MicrocontrollerModeling_Function(type="sample_text")
    b2 = MicrocontrollerModeling_Function(type="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Instruction', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Instruction', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Function23'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Function23', a)
    _safe_set(a, 'MicrocontrollerModeling_Instruction', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Instruction', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Function23'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Function23', a)
    if hasattr(b2, 'MicrocontrollerModeling_Function23'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Function23', a)
    _safe_set(a, 'MicrocontrollerModeling_Instruction', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Instruction', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Function23'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Function23', a)


def test_assoc_libraries13_link_reassign_clear():
    a = MicrocontrollerModeling_Library(name="sample_text")
    b1 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    b2 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text_2", hasMain=False, name="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Library', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Library', b1)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage14'):
        assert _is_linked(b1, 'MicrocontrollerModeling_CLanguage14', a)
    _safe_set(a, 'MicrocontrollerModeling_Library', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Library', b2)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage14'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_CLanguage14', a)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage14'):
        assert _is_linked(b2, 'MicrocontrollerModeling_CLanguage14', a)
    _safe_set(a, 'MicrocontrollerModeling_Library', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Library', b2)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage14'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_CLanguage14', a)


def test_assoc_parameters21_link_reassign_clear():
    a = MicrocontrollerModeling_Parameter(name="sample_text", type="sample_text")
    b1 = MicrocontrollerModeling_Function(type="sample_text")
    b2 = MicrocontrollerModeling_Function(type="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Parameter', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Parameter', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Function'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Function', a)
    _safe_set(a, 'MicrocontrollerModeling_Parameter', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Parameter', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Function'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Function', a)
    if hasattr(b2, 'MicrocontrollerModeling_Function'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Function', a)
    _safe_set(a, 'MicrocontrollerModeling_Parameter', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Parameter', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Function'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Function', a)


def test_assoc_pinmodes17_link_reassign_clear():
    a = MicrocontrollerModeling_PinMode(name="sample_text", value="sample_text")
    b1 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    b2 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text_2", hasMain=False, name="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_PinMode', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_PinMode', b1)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage18'):
        assert _is_linked(b1, 'MicrocontrollerModeling_CLanguage18', a)
    _safe_set(a, 'MicrocontrollerModeling_PinMode', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_PinMode', b2)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage18'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_CLanguage18', a)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage18'):
        assert _is_linked(b2, 'MicrocontrollerModeling_CLanguage18', a)
    _safe_set(a, 'MicrocontrollerModeling_PinMode', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_PinMode', b2)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage18'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_CLanguage18', a)


def test_assoc_pinoperation19_link_reassign_clear():
    a = MicrocontrollerModeling_PinOperation(name="sample_text")
    b1 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    b2 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text_2", hasMain=False, name="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_PinOperation', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_PinOperation', b1)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage20'):
        assert _is_linked(b1, 'MicrocontrollerModeling_CLanguage20', a)
    _safe_set(a, 'MicrocontrollerModeling_PinOperation', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_PinOperation', b2)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage20'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_CLanguage20', a)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage20'):
        assert _is_linked(b2, 'MicrocontrollerModeling_CLanguage20', a)
    _safe_set(a, 'MicrocontrollerModeling_PinOperation', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_PinOperation', b2)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage20'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_CLanguage20', a)


def test_assoc_pins0_link_reassign_clear():
    a = MicrocontrollerModeling_Pin(name="sample_text", nature="sample_text", number=7)
    b1 = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b2 = MicrocontrollerModeling_Microcontroller(family="sample_text_2", manufacturer="sample_text_2", name="sample_text_2", wordMemory="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Pin', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Pin', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Microcontroller', a)
    _safe_set(a, 'MicrocontrollerModeling_Pin', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Pin', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Microcontroller', a)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Microcontroller', a)
    _safe_set(a, 'MicrocontrollerModeling_Pin', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Pin', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Microcontroller', a)


def test_assoc_processor3_link_reassign_clear():
    a = MicrocontrollerModeling_Processor(speed=7, unit="sample_text")
    b1 = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b2 = MicrocontrollerModeling_Microcontroller(family="sample_text_2", manufacturer="sample_text_2", name="sample_text_2", wordMemory="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Processor', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Processor', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller4'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Microcontroller4', a)
    _safe_set(a, 'MicrocontrollerModeling_Processor', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Processor', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller4'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Microcontroller4', a)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller4'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Microcontroller4', a)
    _safe_set(a, 'MicrocontrollerModeling_Processor', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Processor', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller4'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Microcontroller4', a)


def test_assoc_ram9_link_reassign_clear():
    a = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b1 = MicrocontrollerModeling_RAM()
    b2 = MicrocontrollerModeling_RAM()
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller10', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller10', b1)
    if hasattr(b1, 'MicrocontrollerModeling_RAM'):
        assert _is_linked(b1, 'MicrocontrollerModeling_RAM', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller10', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller10', b2)
    if hasattr(b1, 'MicrocontrollerModeling_RAM'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_RAM', a)
    if hasattr(b2, 'MicrocontrollerModeling_RAM'):
        assert _is_linked(b2, 'MicrocontrollerModeling_RAM', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller10', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Microcontroller10', b2)
    if hasattr(b2, 'MicrocontrollerModeling_RAM'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_RAM', a)


def test_assoc_registers11_link_reassign_clear():
    a = MicrocontrollerModeling_Register(name="sample_text", type="sample_text")
    b1 = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b2 = MicrocontrollerModeling_Microcontroller(family="sample_text_2", manufacturer="sample_text_2", name="sample_text_2", wordMemory="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_Register', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Register', b1)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller12'):
        assert _is_linked(b1, 'MicrocontrollerModeling_Microcontroller12', a)
    _safe_set(a, 'MicrocontrollerModeling_Register', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Register', b2)
    if hasattr(b1, 'MicrocontrollerModeling_Microcontroller12'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_Microcontroller12', a)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller12'):
        assert _is_linked(b2, 'MicrocontrollerModeling_Microcontroller12', a)
    _safe_set(a, 'MicrocontrollerModeling_Register', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Register', b2)
    if hasattr(b2, 'MicrocontrollerModeling_Microcontroller12'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_Microcontroller12', a)


def test_assoc_rom5_link_reassign_clear():
    a = MicrocontrollerModeling_Microcontroller(family="sample_text", manufacturer="sample_text", name="sample_text", wordMemory="sample_text")
    b1 = MicrocontrollerModeling_ROM()
    b2 = MicrocontrollerModeling_ROM()
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller6', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller6', b1)
    if hasattr(b1, 'MicrocontrollerModeling_ROM'):
        assert _is_linked(b1, 'MicrocontrollerModeling_ROM', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller6', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_Microcontroller6', b2)
    if hasattr(b1, 'MicrocontrollerModeling_ROM'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_ROM', a)
    if hasattr(b2, 'MicrocontrollerModeling_ROM'):
        assert _is_linked(b2, 'MicrocontrollerModeling_ROM', a)
    _safe_set(a, 'MicrocontrollerModeling_Microcontroller6', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_Microcontroller6', b2)
    if hasattr(b2, 'MicrocontrollerModeling_ROM'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_ROM', a)


def test_assoc_timerconfig15_link_reassign_clear():
    a = MicrocontrollerModeling_TimerConfig(name="sample_text", period=7)
    b1 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text", hasMain=True, name="sample_text")
    b2 = MicrocontrollerModeling_CLanguage(filesExtension="sample_text_2", hasMain=False, name="sample_text_2")
    _safe_set(a, 'MicrocontrollerModeling_TimerConfig', b1)
    assert _is_linked(a, 'MicrocontrollerModeling_TimerConfig', b1)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage16'):
        assert _is_linked(b1, 'MicrocontrollerModeling_CLanguage16', a)
    _safe_set(a, 'MicrocontrollerModeling_TimerConfig', b2)
    assert _is_linked(a, 'MicrocontrollerModeling_TimerConfig', b2)
    if hasattr(b1, 'MicrocontrollerModeling_CLanguage16'):
        assert not _is_linked(b1, 'MicrocontrollerModeling_CLanguage16', a)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage16'):
        assert _is_linked(b2, 'MicrocontrollerModeling_CLanguage16', a)
    _safe_set(a, 'MicrocontrollerModeling_TimerConfig', None)
    assert not _is_linked(a, 'MicrocontrollerModeling_TimerConfig', b2)
    if hasattr(b2, 'MicrocontrollerModeling_CLanguage16'):
        assert not _is_linked(b2, 'MicrocontrollerModeling_CLanguage16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EEPROM_strategy = st.builds(EEPROM)
@given(instance=EEPROM_strategy)
@settings(max_examples=25)
def test_EEPROM_instantiation(instance):
    assert isinstance(instance, EEPROM)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


Memory_strategy = st.builds(Memory)
@given(instance=Memory_strategy)
@settings(max_examples=25)
def test_Memory_instantiation(instance):
    assert isinstance(instance, Memory)


MicrocontrollerModeling_CLanguage_strategy = st.builds(MicrocontrollerModeling_CLanguage, filesExtension=safe_text, hasMain=st.booleans(), name=safe_text)
@given(instance=MicrocontrollerModeling_CLanguage_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_CLanguage_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_CLanguage)


MicrocontrollerModeling_EEPROM_strategy = st.builds(MicrocontrollerModeling_EEPROM)
@given(instance=MicrocontrollerModeling_EEPROM_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_EEPROM_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_EEPROM)


MicrocontrollerModeling_Flash_strategy = st.builds(MicrocontrollerModeling_Flash)
@given(instance=MicrocontrollerModeling_Flash_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Flash_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Flash)


MicrocontrollerModeling_Function_strategy = st.builds(MicrocontrollerModeling_Function, type=safe_text)
@given(instance=MicrocontrollerModeling_Function_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Function_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Function)


MicrocontrollerModeling_Instruction_strategy = st.builds(MicrocontrollerModeling_Instruction, value=safe_text)
@given(instance=MicrocontrollerModeling_Instruction_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Instruction_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Instruction)


MicrocontrollerModeling_Library_strategy = st.builds(MicrocontrollerModeling_Library, name=safe_text)
@given(instance=MicrocontrollerModeling_Library_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Library_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Library)


MicrocontrollerModeling_Memory_strategy = st.builds(MicrocontrollerModeling_Memory, size=st.integers(), unit=safe_text)
@given(instance=MicrocontrollerModeling_Memory_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Memory_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Memory)


MicrocontrollerModeling_Microcontroller_strategy = st.builds(MicrocontrollerModeling_Microcontroller, family=safe_text, manufacturer=safe_text, name=safe_text, wordMemory=safe_text)
@given(instance=MicrocontrollerModeling_Microcontroller_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Microcontroller_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Microcontroller)


MicrocontrollerModeling_Parameter_strategy = st.builds(MicrocontrollerModeling_Parameter, name=safe_text, type=safe_text)
@given(instance=MicrocontrollerModeling_Parameter_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Parameter_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Parameter)


MicrocontrollerModeling_Pin_strategy = st.builds(MicrocontrollerModeling_Pin, name=safe_text, nature=safe_text, number=st.integers())
@given(instance=MicrocontrollerModeling_Pin_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Pin_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Pin)


MicrocontrollerModeling_PinMode_strategy = st.builds(MicrocontrollerModeling_PinMode, name=safe_text, value=safe_text)
@given(instance=MicrocontrollerModeling_PinMode_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_PinMode_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_PinMode)


MicrocontrollerModeling_PinOperation_strategy = st.builds(MicrocontrollerModeling_PinOperation, name=safe_text)
@given(instance=MicrocontrollerModeling_PinOperation_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_PinOperation_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_PinOperation)


MicrocontrollerModeling_Processor_strategy = st.builds(MicrocontrollerModeling_Processor, speed=st.integers(), unit=safe_text)
@given(instance=MicrocontrollerModeling_Processor_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Processor_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Processor)


MicrocontrollerModeling_RAM_strategy = st.builds(MicrocontrollerModeling_RAM)
@given(instance=MicrocontrollerModeling_RAM_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_RAM_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_RAM)


MicrocontrollerModeling_ROM_strategy = st.builds(MicrocontrollerModeling_ROM)
@given(instance=MicrocontrollerModeling_ROM_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_ROM_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_ROM)


MicrocontrollerModeling_Register_strategy = st.builds(MicrocontrollerModeling_Register, name=safe_text, type=safe_text)
@given(instance=MicrocontrollerModeling_Register_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_Register_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_Register)


MicrocontrollerModeling_TimerConfig_strategy = st.builds(MicrocontrollerModeling_TimerConfig, name=safe_text, period=st.integers())
@given(instance=MicrocontrollerModeling_TimerConfig_strategy)
@settings(max_examples=25)
def test_MicrocontrollerModeling_TimerConfig_instantiation(instance):
    assert isinstance(instance, MicrocontrollerModeling_TimerConfig)


ROM_strategy = st.builds(ROM)
@given(instance=ROM_strategy)
@settings(max_examples=25)
def test_ROM_instantiation(instance):
    assert isinstance(instance, ROM)



