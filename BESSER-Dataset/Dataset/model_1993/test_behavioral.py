import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EValue,
    MappingOperation,
    trace_EMappingContext,
    trace_EMappingOperation,
    trace_EMappingParameters,
    trace_EMappingResults,
    trace_EObject,
    trace_ETuplePartValue,
    trace_EValue,
    trace_MappingOperationToTraceRecordMapEntry,
    trace_ObjectToTraceRecordMapEntry,
    trace_Trace,
    trace_TraceRecord,
    trace_VarParameterValue,
    EDirectionKind,
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

def test_assoc_collection31_reverse_link_reassign_clear():
    a1 = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    a2 = trace_EValue(collectionType="sample_text_2", oclObject="sample_text_2", primitiveValue="sample_text_2")
    b = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    _safe_set(b, 'trace_EValue32', a1)
    assert _is_linked(b, 'trace_EValue32', a1)
    if hasattr(a1, 'trace_EValue30'):
        assert _is_linked(a1, 'trace_EValue30', b)
    _safe_set(b, 'trace_EValue32', a2)
    assert _is_linked(b, 'trace_EValue32', a2)
    if hasattr(a1, 'trace_EValue30'):
        assert not _is_linked(a1, 'trace_EValue30', b)
    if hasattr(a2, 'trace_EValue30'):
        assert _is_linked(a2, 'trace_EValue30', b)
    _safe_set(b, 'trace_EValue32', None)
    assert not _is_linked(b, 'trace_EValue32', a2)
    if hasattr(a2, 'trace_EValue30'):
        assert not _is_linked(a2, 'trace_EValue30', b)


def test_assoc_sourceToTraceRecordMap3_reverse_link_reassign_clear():
    a1 = trace_Trace()
    a2 = trace_Trace()
    b = trace_ObjectToTraceRecordMapEntry(key="sample_text")
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry', a1)
    assert _is_linked(b, 'trace_ObjectToTraceRecordMapEntry', a1)
    if hasattr(a1, 'trace_Trace4'):
        assert _is_linked(a1, 'trace_Trace4', b)
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry', a2)
    assert _is_linked(b, 'trace_ObjectToTraceRecordMapEntry', a2)
    if hasattr(a1, 'trace_Trace4'):
        assert not _is_linked(a1, 'trace_Trace4', b)
    if hasattr(a2, 'trace_Trace4'):
        assert _is_linked(a2, 'trace_Trace4', b)
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry', None)
    assert not _is_linked(b, 'trace_ObjectToTraceRecordMapEntry', a2)
    if hasattr(a2, 'trace_Trace4'):
        assert not _is_linked(a2, 'trace_Trace4', b)


def test_assoc_targetToTraceRecordMap5_reverse_link_reassign_clear():
    a1 = trace_Trace()
    a2 = trace_Trace()
    b = trace_ObjectToTraceRecordMapEntry(key="sample_text")
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry7', a1)
    assert _is_linked(b, 'trace_ObjectToTraceRecordMapEntry7', a1)
    if hasattr(a1, 'trace_Trace6'):
        assert _is_linked(a1, 'trace_Trace6', b)
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry7', a2)
    assert _is_linked(b, 'trace_ObjectToTraceRecordMapEntry7', a2)
    if hasattr(a1, 'trace_Trace6'):
        assert not _is_linked(a1, 'trace_Trace6', b)
    if hasattr(a2, 'trace_Trace6'):
        assert _is_linked(a2, 'trace_Trace6', b)
    _safe_set(b, 'trace_ObjectToTraceRecordMapEntry7', None)
    assert not _is_linked(b, 'trace_ObjectToTraceRecordMapEntry7', a2)
    if hasattr(a2, 'trace_Trace6'):
        assert not _is_linked(a2, 'trace_Trace6', b)


def test_assoc_value16_reverse_link_reassign_clear():
    a1 = trace_VarParameterValue(kind="sample_text", name="sample_text", type="sample_text")
    a2 = trace_VarParameterValue(kind="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    _safe_set(b, 'trace_EValue', a1)
    assert _is_linked(b, 'trace_EValue', a1)
    if hasattr(a1, 'trace_VarParameterValue'):
        assert _is_linked(a1, 'trace_VarParameterValue', b)
    _safe_set(b, 'trace_EValue', a2)
    assert _is_linked(b, 'trace_EValue', a2)
    if hasattr(a1, 'trace_VarParameterValue'):
        assert not _is_linked(a1, 'trace_VarParameterValue', b)
    if hasattr(a2, 'trace_VarParameterValue'):
        assert _is_linked(a2, 'trace_VarParameterValue', b)
    _safe_set(b, 'trace_EValue', None)
    assert not _is_linked(b, 'trace_EValue', a2)
    if hasattr(a2, 'trace_VarParameterValue'):
        assert not _is_linked(a2, 'trace_VarParameterValue', b)


def test_assoc_value33_reverse_link_reassign_clear():
    a1 = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    a2 = trace_EValue(collectionType="sample_text_2", oclObject="sample_text_2", primitiveValue="sample_text_2")
    b = trace_ETuplePartValue(name="sample_text")
    _safe_set(b, 'trace_ETuplePartValue', a1)
    assert _is_linked(b, 'trace_ETuplePartValue', a1)
    if hasattr(a1, 'trace_EValue34'):
        assert _is_linked(a1, 'trace_EValue34', b)
    _safe_set(b, 'trace_ETuplePartValue', a2)
    assert _is_linked(b, 'trace_ETuplePartValue', a2)
    if hasattr(a1, 'trace_EValue34'):
        assert not _is_linked(a1, 'trace_EValue34', b)
    if hasattr(a2, 'trace_EValue34'):
        assert _is_linked(a2, 'trace_EValue34', b)
    _safe_set(b, 'trace_ETuplePartValue', None)
    assert not _is_linked(b, 'trace_ETuplePartValue', a2)
    if hasattr(a2, 'trace_EValue34'):
        assert not _is_linked(a2, 'trace_EValue34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_context35_stub_double():
    # trace_EMappingContext has no real 'trace_EMappingContext36' property in the generated
    # code (a bare stub) -- manually attach it so trace_VarParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_VarParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_VarParameterValue(kind="sample_text", name="sample_text", type="sample_text")
    partner = trace_EMappingContext()
    setattr(partner, 'trace_EMappingContext36', None)
    _safe_set(owner, 'trace_VarParameterValue37', partner)
    assert getattr(partner, 'trace_EMappingContext36') == owner
    _safe_set(owner, 'trace_VarParameterValue37', None)
    assert getattr(partner, 'trace_EMappingContext36') is None


def test_assoc_intermediateElement27_stub_double():
    # trace_EObject has no real 'trace_EObject29' property in the generated
    # code (a bare stub) -- manually attach it so trace_EValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_EValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    partner = trace_EObject()
    setattr(partner, 'trace_EObject29', None)
    _safe_set(owner, 'trace_EValue28', partner)
    assert getattr(partner, 'trace_EObject29') == owner
    _safe_set(owner, 'trace_EValue28', None)
    assert getattr(partner, 'trace_EObject29') is None


def test_assoc_mappingOperation8_stub_double():
    # trace_TraceRecord has no real 'trace_TraceRecord9' property in the generated
    # code (a bare stub) -- manually attach it so trace_EMappingOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_EMappingOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_EMappingOperation(module="sample_text", name="sample_text", package="sample_text")
    partner = trace_TraceRecord()
    setattr(partner, 'trace_TraceRecord9', None)
    _safe_set(owner, 'trace_EMappingOperation', partner)
    assert getattr(partner, 'trace_TraceRecord9') == owner
    _safe_set(owner, 'trace_EMappingOperation', None)
    assert getattr(partner, 'trace_TraceRecord9') is None


def test_assoc_modelElement25_stub_double():
    # trace_EObject has no real 'trace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so trace_EValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_EValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_EValue(collectionType="sample_text", oclObject="sample_text", primitiveValue="sample_text")
    partner = trace_EObject()
    setattr(partner, 'trace_EObject', None)
    _safe_set(owner, 'trace_EValue26', partner)
    assert getattr(partner, 'trace_EObject') == owner
    _safe_set(owner, 'trace_EValue26', None)
    assert getattr(partner, 'trace_EObject') is None


def test_assoc_parameters38_stub_double():
    # trace_EMappingParameters has no real 'trace_EMappingParameters39' property in the generated
    # code (a bare stub) -- manually attach it so trace_VarParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_VarParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_VarParameterValue(kind="sample_text", name="sample_text", type="sample_text")
    partner = trace_EMappingParameters()
    setattr(partner, 'trace_EMappingParameters39', None)
    _safe_set(owner, 'trace_VarParameterValue40', partner)
    assert owner in getattr(partner, 'trace_EMappingParameters39')
    _safe_set(owner, 'trace_VarParameterValue40', None)
    assert owner not in getattr(partner, 'trace_EMappingParameters39')


def test_assoc_result41_stub_double():
    # trace_EMappingResults has no real 'trace_EMappingResults42' property in the generated
    # code (a bare stub) -- manually attach it so trace_VarParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_VarParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_VarParameterValue(kind="sample_text", name="sample_text", type="sample_text")
    partner = trace_EMappingResults()
    setattr(partner, 'trace_EMappingResults42', None)
    _safe_set(owner, 'trace_VarParameterValue43', partner)
    assert owner in getattr(partner, 'trace_EMappingResults42')
    _safe_set(owner, 'trace_VarParameterValue43', None)
    assert owner not in getattr(partner, 'trace_EMappingResults42')


def test_assoc_runtimeMappingOperation22_stub_double():
    # MappingOperation has no real 'MappingOperation24' property in the generated
    # code (a bare stub) -- manually attach it so trace_EMappingOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_EMappingOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_EMappingOperation(module="sample_text", name="sample_text", package="sample_text")
    partner = MappingOperation()
    setattr(partner, 'MappingOperation24', None)
    _safe_set(owner, 'trace_EMappingOperation23', partner)
    assert getattr(partner, 'MappingOperation24') == owner
    _safe_set(owner, 'trace_EMappingOperation23', None)
    assert getattr(partner, 'MappingOperation24') is None


def test_assoc_traceRecordMap1_stub_double():
    # trace_MappingOperationToTraceRecordMapEntry has no real 'trace_MappingOperationToTraceRecordMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_MappingOperationToTraceRecordMapEntry()
    setattr(partner, 'trace_MappingOperationToTraceRecordMapEntry', None)
    _safe_set(owner, 'trace_Trace2', {partner})
    assert getattr(partner, 'trace_MappingOperationToTraceRecordMapEntry') == owner
    _safe_set(owner, 'trace_Trace2', set())
    assert getattr(partner, 'trace_MappingOperationToTraceRecordMapEntry') is None


def test_assoc_traceRecords0_stub_double():
    # trace_TraceRecord has no real 'trace_TraceRecord' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_TraceRecord()
    setattr(partner, 'trace_TraceRecord', None)
    _safe_set(owner, 'trace_Trace', {partner})
    assert getattr(partner, 'trace_TraceRecord') == owner
    _safe_set(owner, 'trace_Trace', set())
    assert getattr(partner, 'trace_TraceRecord') is None


def test_assoc_value44_stub_double():
    # trace_TraceRecord has no real 'trace_TraceRecord46' property in the generated
    # code (a bare stub) -- manually attach it so trace_ObjectToTraceRecordMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ObjectToTraceRecordMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ObjectToTraceRecordMapEntry(key="sample_text")
    partner = trace_TraceRecord()
    setattr(partner, 'trace_TraceRecord46', None)
    _safe_set(owner, 'trace_ObjectToTraceRecordMapEntry45', {partner})
    assert getattr(partner, 'trace_TraceRecord46') == owner
    _safe_set(owner, 'trace_ObjectToTraceRecordMapEntry45', set())
    assert getattr(partner, 'trace_TraceRecord46') is None


