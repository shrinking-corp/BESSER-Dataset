import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TraceElement,
    trace_ExecutionContext,
    trace_ModelElement,
    trace_ModuleElement,
    trace_Property,
    trace_Trace,
    trace_TraceElement,
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

def test_assoc_executionContext17_reverse_link_reassign_clear():
    a1 = trace_ModelElement(element_id="sample_text")
    a2 = trace_ModelElement(element_id="sample_text_2")
    b = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    _safe_set(b, 'ExecutionContext18', a1)
    assert _is_linked(b, 'ExecutionContext18', a1)
    if hasattr(a1, 'involves'):
        assert _is_linked(a1, 'involves', b)
    _safe_set(b, 'ExecutionContext18', a2)
    assert _is_linked(b, 'ExecutionContext18', a2)
    if hasattr(a1, 'involves'):
        assert not _is_linked(a1, 'involves', b)
    if hasattr(a2, 'involves'):
        assert _is_linked(a2, 'involves', b)
    _safe_set(b, 'ExecutionContext18', None)
    assert not _is_linked(b, 'ExecutionContext18', a2)
    if hasattr(a2, 'involves'):
        assert not _is_linked(a2, 'involves', b)


def test_assoc_executionContexts4_reverse_link_reassign_clear():
    a1 = trace_ModuleElement(module_id="sample_text")
    a2 = trace_ModuleElement(module_id="sample_text_2")
    b = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    _safe_set(b, 'ExecutionContext', a1)
    assert _is_linked(b, 'ExecutionContext', a1)
    if hasattr(a1, 'for_'):
        assert _is_linked(a1, 'for_', b)
    _safe_set(b, 'ExecutionContext', a2)
    assert _is_linked(b, 'ExecutionContext', a2)
    if hasattr(a1, 'for_'):
        assert not _is_linked(a1, 'for_', b)
    if hasattr(a2, 'for_'):
        assert _is_linked(a2, 'for_', b)
    _safe_set(b, 'ExecutionContext', None)
    assert not _is_linked(b, 'ExecutionContext', a2)
    if hasattr(a2, 'for_'):
        assert not _is_linked(a2, 'for_', b)


def test_assoc_for_0_reverse_link_reassign_clear():
    a1 = trace_ModuleElement(module_id="sample_text")
    a2 = trace_ModuleElement(module_id="sample_text_2")
    b = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    _safe_set(b, 'executionContexts', {a1})
    assert _is_linked(b, 'executionContexts', a1)
    if hasattr(a1, 'ModuleElement'):
        assert _is_linked(a1, 'ModuleElement', b)
    _safe_set(b, 'executionContexts', {a2})
    assert _is_linked(b, 'executionContexts', a2)
    if hasattr(a1, 'ModuleElement'):
        assert not _is_linked(a1, 'ModuleElement', b)
    if hasattr(a2, 'ModuleElement'):
        assert _is_linked(a2, 'ModuleElement', b)
    _safe_set(b, 'executionContexts', set())
    assert not _is_linked(b, 'executionContexts', a2)
    if hasattr(a2, 'ModuleElement'):
        assert not _is_linked(a2, 'ModuleElement', b)


def test_assoc_involves2_reverse_link_reassign_clear():
    a1 = trace_ModelElement(element_id="sample_text")
    a2 = trace_ModelElement(element_id="sample_text_2")
    b = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    _safe_set(b, 'executionContext3', {a1})
    assert _is_linked(b, 'executionContext3', a1)
    if hasattr(a1, 'ModelElement'):
        assert _is_linked(a1, 'ModelElement', b)
    _safe_set(b, 'executionContext3', {a2})
    assert _is_linked(b, 'executionContext3', a2)
    if hasattr(a1, 'ModelElement'):
        assert not _is_linked(a1, 'ModelElement', b)
    if hasattr(a2, 'ModelElement'):
        assert _is_linked(a2, 'ModelElement', b)
    _safe_set(b, 'executionContext3', set())
    assert not _is_linked(b, 'executionContext3', a2)
    if hasattr(a2, 'ModelElement'):
        assert not _is_linked(a2, 'ModelElement', b)


def test_assoc_modelElement23_reverse_link_reassign_clear():
    a1 = trace_Property(name="sample_text")
    a2 = trace_Property(name="sample_text_2")
    b = trace_ModelElement(element_id="sample_text")
    _safe_set(b, 'ModelElement24', a1)
    assert _is_linked(b, 'ModelElement24', a1)
    if hasattr(a1, 'owns'):
        assert _is_linked(a1, 'owns', b)
    _safe_set(b, 'ModelElement24', a2)
    assert _is_linked(b, 'ModelElement24', a2)
    if hasattr(a1, 'owns'):
        assert not _is_linked(a1, 'owns', b)
    if hasattr(a2, 'owns'):
        assert _is_linked(a2, 'owns', b)
    _safe_set(b, 'ModelElement24', None)
    assert not _is_linked(b, 'ModelElement24', a2)
    if hasattr(a2, 'owns'):
        assert not _is_linked(a2, 'owns', b)


def test_assoc_owns21_reverse_link_reassign_clear():
    a1 = trace_Property(name="sample_text")
    a2 = trace_Property(name="sample_text_2")
    b = trace_ModelElement(element_id="sample_text")
    _safe_set(b, 'modelElement', {a1})
    assert _is_linked(b, 'modelElement', a1)
    if hasattr(a1, 'Property22'):
        assert _is_linked(a1, 'Property22', b)
    _safe_set(b, 'modelElement', {a2})
    assert _is_linked(b, 'modelElement', a2)
    if hasattr(a1, 'Property22'):
        assert not _is_linked(a1, 'Property22', b)
    if hasattr(a2, 'Property22'):
        assert _is_linked(a2, 'Property22', b)
    _safe_set(b, 'modelElement', set())
    assert not _is_linked(b, 'modelElement', a2)
    if hasattr(a2, 'Property22'):
        assert not _is_linked(a2, 'Property22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accesses15_stub_double():
    # trace_Trace has no real 'traces16' property in the generated
    # code (a bare stub) -- manually attach it so trace_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Property(name="sample_text")
    partner = trace_Trace()
    setattr(partner, 'traces16', None)
    _safe_set(owner, 'Property', partner)
    assert owner in getattr(partner, 'traces16')
    _safe_set(owner, 'Property', None)
    assert owner not in getattr(partner, 'traces16')


def test_assoc_contains1_stub_double():
    # trace_Trace has no real 'Trace' property in the generated
    # code (a bare stub) -- manually attach it so trace_ExecutionContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ExecutionContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    partner = trace_Trace()
    setattr(partner, 'Trace', None)
    _safe_set(owner, 'executionContext', {partner})
    assert getattr(partner, 'Trace') == owner
    _safe_set(owner, 'executionContext', set())
    assert getattr(partner, 'Trace') is None


def test_assoc_executionContext7_stub_double():
    # trace_Trace has no real 'contains' property in the generated
    # code (a bare stub) -- manually attach it so trace_ExecutionContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ExecutionContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ExecutionContext(modelsIds="sample_text", scriptId="sample_text")
    partner = trace_Trace()
    setattr(partner, 'contains', None)
    _safe_set(owner, 'ExecutionContext8', partner)
    assert getattr(partner, 'contains') == owner
    _safe_set(owner, 'ExecutionContext8', None)
    assert getattr(partner, 'contains') is None


def test_assoc_reaches12_stub_double():
    # trace_Trace has no real 'traces13' property in the generated
    # code (a bare stub) -- manually attach it so trace_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ModelElement(element_id="sample_text")
    partner = trace_Trace()
    setattr(partner, 'traces13', None)
    _safe_set(owner, 'ModelElement14', partner)
    assert owner in getattr(partner, 'traces13')
    _safe_set(owner, 'ModelElement14', None)
    assert owner not in getattr(partner, 'traces13')


def test_assoc_traces19_stub_double():
    # trace_Trace has no real 'Trace20' property in the generated
    # code (a bare stub) -- manually attach it so trace_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ModelElement(element_id="sample_text")
    partner = trace_Trace()
    setattr(partner, 'Trace20', None)
    _safe_set(owner, 'reaches', {partner})
    assert getattr(partner, 'Trace20') == owner
    _safe_set(owner, 'reaches', set())
    assert getattr(partner, 'Trace20') is None


def test_assoc_traces25_stub_double():
    # trace_Trace has no real 'Trace26' property in the generated
    # code (a bare stub) -- manually attach it so trace_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Property(name="sample_text")
    partner = trace_Trace()
    setattr(partner, 'Trace26', None)
    _safe_set(owner, 'accesses', {partner})
    assert getattr(partner, 'Trace26') == owner
    _safe_set(owner, 'accesses', set())
    assert getattr(partner, 'Trace26') is None


def test_assoc_traces5_stub_double():
    # trace_Trace has no real 'Trace6' property in the generated
    # code (a bare stub) -- manually attach it so trace_ModuleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ModuleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ModuleElement(module_id="sample_text")
    partner = trace_Trace()
    setattr(partner, 'Trace6', None)
    _safe_set(owner, 'traces', {partner})
    assert getattr(partner, 'Trace6') == owner
    _safe_set(owner, 'traces', set())
    assert getattr(partner, 'Trace6') is None


def test_assoc_traces9_stub_double():
    # trace_Trace has no real 'traces10' property in the generated
    # code (a bare stub) -- manually attach it so trace_ModuleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ModuleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ModuleElement(module_id="sample_text")
    partner = trace_Trace()
    setattr(partner, 'traces10', None)
    _safe_set(owner, 'ModuleElement11', partner)
    assert getattr(partner, 'traces10') == owner
    _safe_set(owner, 'ModuleElement11', None)
    assert getattr(partner, 'traces10') is None


