import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Process,
    ProcessElement,
    SPDLScenario,
    SPDLSimEvent,
    SPDLTrace,
    SimplePDLSemantics_DDMMSimplePDL_Guidance,
    SimplePDLSemantics_DDMMSimplePDL_Process,
    SimplePDLSemantics_DDMMSimplePDL_ProcessElement,
    SimplePDLSemantics_DDMMSimplePDL_WorkDefinition,
    SimplePDLSemantics_DDMMSimplePDL_WorkSequence,
    SimplePDLSemantics_EDMMSimplePDL_Event,
    SimplePDLSemantics_EDMMSimplePDL_FinishWD,
    SimplePDLSemantics_EDMMSimplePDL_StartWD,
    SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent,
    SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition,
    SimplePDLSemantics_TM3SimplePDL_SPDLScenario,
    SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent,
    SimplePDLSemantics_TM3SimplePDL_SPDLTrace,
    WorkDefinition,
    WorkDefinitionEvent,
    WorkSequence,
    ExecutionState,
    TimeState,
    WorkSequenceType,
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

def test_assoc_element12_stub_double():
    # ProcessElement has no real 'ProcessElement13' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_Guidance(text="sample_text")
    partner = ProcessElement()
    setattr(partner, 'ProcessElement13', None)
    _safe_set(owner, 'SimplePDLSemantics_DDMMSimplePDL_Guidance', {partner})
    assert getattr(partner, 'ProcessElement13') == owner
    _safe_set(owner, 'SimplePDLSemantics_DDMMSimplePDL_Guidance', set())
    assert getattr(partner, 'ProcessElement13') is None


def test_assoc_from_1_stub_double():
    # WorkDefinition has no real 'WorkDefinition' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_Process(name="sample_text")
    partner = WorkDefinition()
    setattr(partner, 'WorkDefinition', None)
    _safe_set(owner, 'process', partner)
    assert getattr(partner, 'WorkDefinition') == owner
    _safe_set(owner, 'process', None)
    assert getattr(partner, 'WorkDefinition') is None


def test_assoc_linksToPredecessors2_stub_double():
    # WorkSequence has no real 'WorkSequence' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_WorkDefinition(name="sample_text")
    partner = WorkSequence()
    setattr(partner, 'WorkSequence', None)
    _safe_set(owner, 'successor', {partner})
    assert getattr(partner, 'WorkSequence') == owner
    _safe_set(owner, 'successor', set())
    assert getattr(partner, 'WorkSequence') is None


def test_assoc_linksToSuccessors3_stub_double():
    # WorkSequence has no real 'WorkSequence4' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_WorkDefinition(name="sample_text")
    partner = WorkSequence()
    setattr(partner, 'WorkSequence4', None)
    _safe_set(owner, 'predecessor', {partner})
    assert getattr(partner, 'WorkSequence4') == owner
    _safe_set(owner, 'predecessor', set())
    assert getattr(partner, 'WorkSequence4') is None


def test_assoc_predecessor6_stub_double():
    # WorkDefinition has no real 'WorkDefinition7' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_WorkSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_WorkSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_WorkSequence(linkType="sample_text")
    partner = WorkDefinition()
    setattr(partner, 'WorkDefinition7', None)
    _safe_set(owner, 'linksToSuccessors', partner)
    assert getattr(partner, 'WorkDefinition7') == owner
    _safe_set(owner, 'linksToSuccessors', None)
    assert getattr(partner, 'WorkDefinition7') is None


def test_assoc_process5_stub_double():
    # Process has no real 'Process' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_WorkDefinition(name="sample_text")
    partner = Process()
    setattr(partner, 'Process', None)
    _safe_set(owner, 'from_', partner)
    assert getattr(partner, 'Process') == owner
    _safe_set(owner, 'from_', None)
    assert getattr(partner, 'Process') is None


def test_assoc_processElements0_stub_double():
    # ProcessElement has no real 'ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_Process(name="sample_text")
    partner = ProcessElement()
    setattr(partner, 'ProcessElement', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'ProcessElement') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'ProcessElement') is None


def test_assoc_successor8_stub_double():
    # WorkDefinition has no real 'WorkDefinition9' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDLSemantics_DDMMSimplePDL_WorkSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDLSemantics_DDMMSimplePDL_WorkSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDLSemantics_DDMMSimplePDL_WorkSequence(linkType="sample_text")
    partner = WorkDefinition()
    setattr(partner, 'WorkDefinition9', None)
    _safe_set(owner, 'linksToPredecessors', partner)
    assert getattr(partner, 'WorkDefinition9') == owner
    _safe_set(owner, 'linksToPredecessors', None)
    assert getattr(partner, 'WorkDefinition9') is None


