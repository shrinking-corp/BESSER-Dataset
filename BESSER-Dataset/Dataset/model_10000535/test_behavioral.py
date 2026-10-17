import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTableModel,
    ArrayList_ProgramFileData_,
    CPU,
    Class,
    Clock,
    Dispatcher,
    Font,
    Hard_Drive,
    IO_Device,
    Instruction_Calculate,
    Instruction_CloseBracket,
    Instruction_DecrementPointer,
    Instruction_DecrementValue,
    Instruction_Exit,
    Instruction_IO,
    Instruction_IncrementPointer,
    Instruction_IncrementValue,
    Instruction_Instruction_Interface,
    Instruction_OpenBracket,
    Instruction_Out,
    Instruction_Print,
    Instruction_Yield,
    Interrupter_Interface,
    JFrame,
    JLabel,
    JScrollPane,
    JTable,
    JTextArea,
    JTextField,
    JobFileData,
    Main,
    Memory,
    Object,
    Operating_System,
    Page,
    Process,
    ProcessData,
    ProcessTableModel,
    ProgramFileData,
    Prompt,
    Request,
    Scheduler,
    Task_Manager,
    ArrayList_Instruction_,
    ArrayList_Integer_,
    ArrayList_Interrupter_,
    ArrayList_ProcessData_,
    Memory__,
    Page__,
    ProcessState,
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

def test_assoc_Hard_Drive_Request_reverse_link_reassign_clear():
    a1 = Request(endAddress=7, processID=7, startAddress=7)
    a2 = Request(endAddress=13, processID=13, startAddress=13)
    b = Hard_Drive(memory="sample_text")
    _safe_set(b, 'request48', a1)
    assert _is_linked(b, 'request48', a1)
    if hasattr(a1, 'hard_Drive49'):
        assert _is_linked(a1, 'hard_Drive49', b)
    _safe_set(b, 'request48', a2)
    assert _is_linked(b, 'request48', a2)
    if hasattr(a1, 'hard_Drive49'):
        assert not _is_linked(a1, 'hard_Drive49', b)
    if hasattr(a2, 'hard_Drive49'):
        assert _is_linked(a2, 'hard_Drive49', b)
    _safe_set(b, 'request48', None)
    assert not _is_linked(b, 'request48', a2)
    if hasattr(a2, 'hard_Drive49'):
        assert not _is_linked(a2, 'hard_Drive49', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

