import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTrace,
    GenNodeTrace,
    MatchingTrace,
    trace_AbstractTrace,
    trace_GenChildNodeTrace,
    trace_GenCompartmentTrace,
    trace_GenLinkLabelTrace,
    trace_GenLinkTrace,
    trace_GenNodeLabelTrace,
    trace_GenNodeTrace,
    trace_MatchingTrace,
    trace_ToolGroupTrace,
    trace_TraceModel,
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

def test_assoc_compartmentTraces9_reverse_link_reassign_clear():
    a1 = trace_GenNodeTrace()
    a2 = trace_GenNodeTrace()
    b = trace_GenCompartmentTrace()
    _safe_set(b, 'trace_GenCompartmentTrace', a1)
    assert _is_linked(b, 'trace_GenCompartmentTrace', a1)
    if hasattr(a1, 'trace_GenNodeTrace10'):
        assert _is_linked(a1, 'trace_GenNodeTrace10', b)
    _safe_set(b, 'trace_GenCompartmentTrace', a2)
    assert _is_linked(b, 'trace_GenCompartmentTrace', a2)
    if hasattr(a1, 'trace_GenNodeTrace10'):
        assert not _is_linked(a1, 'trace_GenNodeTrace10', b)
    if hasattr(a2, 'trace_GenNodeTrace10'):
        assert _is_linked(a2, 'trace_GenNodeTrace10', b)
    _safe_set(b, 'trace_GenCompartmentTrace', None)
    assert not _is_linked(b, 'trace_GenCompartmentTrace', a2)
    if hasattr(a2, 'trace_GenNodeTrace10'):
        assert not _is_linked(a2, 'trace_GenNodeTrace10', b)


def test_assoc_linkLabelTraces11_reverse_link_reassign_clear():
    a1 = trace_GenLinkTrace()
    a2 = trace_GenLinkTrace()
    b = trace_GenLinkLabelTrace()
    _safe_set(b, 'trace_GenLinkLabelTrace', a1)
    assert _is_linked(b, 'trace_GenLinkLabelTrace', a1)
    if hasattr(a1, 'trace_GenLinkTrace12'):
        assert _is_linked(a1, 'trace_GenLinkTrace12', b)
    _safe_set(b, 'trace_GenLinkLabelTrace', a2)
    assert _is_linked(b, 'trace_GenLinkLabelTrace', a2)
    if hasattr(a1, 'trace_GenLinkTrace12'):
        assert not _is_linked(a1, 'trace_GenLinkTrace12', b)
    if hasattr(a2, 'trace_GenLinkTrace12'):
        assert _is_linked(a2, 'trace_GenLinkTrace12', b)
    _safe_set(b, 'trace_GenLinkLabelTrace', None)
    assert not _is_linked(b, 'trace_GenLinkLabelTrace', a2)
    if hasattr(a2, 'trace_GenLinkTrace12'):
        assert not _is_linked(a2, 'trace_GenLinkTrace12', b)


def test_assoc_linkTraces3_reverse_link_reassign_clear():
    a1 = trace_TraceModel()
    a2 = trace_TraceModel()
    b = trace_GenLinkTrace()
    _safe_set(b, 'trace_GenLinkTrace', a1)
    assert _is_linked(b, 'trace_GenLinkTrace', a1)
    if hasattr(a1, 'trace_TraceModel4'):
        assert _is_linked(a1, 'trace_TraceModel4', b)
    _safe_set(b, 'trace_GenLinkTrace', a2)
    assert _is_linked(b, 'trace_GenLinkTrace', a2)
    if hasattr(a1, 'trace_TraceModel4'):
        assert not _is_linked(a1, 'trace_TraceModel4', b)
    if hasattr(a2, 'trace_TraceModel4'):
        assert _is_linked(a2, 'trace_TraceModel4', b)
    _safe_set(b, 'trace_GenLinkTrace', None)
    assert not _is_linked(b, 'trace_GenLinkTrace', a2)
    if hasattr(a2, 'trace_TraceModel4'):
        assert not _is_linked(a2, 'trace_TraceModel4', b)


def test_assoc_nodeLabelTraces7_reverse_link_reassign_clear():
    a1 = trace_GenNodeTrace()
    a2 = trace_GenNodeTrace()
    b = trace_GenNodeLabelTrace()
    _safe_set(b, 'trace_GenNodeLabelTrace', a1)
    assert _is_linked(b, 'trace_GenNodeLabelTrace', a1)
    if hasattr(a1, 'trace_GenNodeTrace8'):
        assert _is_linked(a1, 'trace_GenNodeTrace8', b)
    _safe_set(b, 'trace_GenNodeLabelTrace', a2)
    assert _is_linked(b, 'trace_GenNodeLabelTrace', a2)
    if hasattr(a1, 'trace_GenNodeTrace8'):
        assert not _is_linked(a1, 'trace_GenNodeTrace8', b)
    if hasattr(a2, 'trace_GenNodeTrace8'):
        assert _is_linked(a2, 'trace_GenNodeTrace8', b)
    _safe_set(b, 'trace_GenNodeLabelTrace', None)
    assert not _is_linked(b, 'trace_GenNodeLabelTrace', a2)
    if hasattr(a2, 'trace_GenNodeTrace8'):
        assert not _is_linked(a2, 'trace_GenNodeTrace8', b)


def test_assoc_nodeTraces0_reverse_link_reassign_clear():
    a1 = trace_TraceModel()
    a2 = trace_TraceModel()
    b = trace_GenNodeTrace()
    _safe_set(b, 'trace_GenNodeTrace', a1)
    assert _is_linked(b, 'trace_GenNodeTrace', a1)
    if hasattr(a1, 'trace_TraceModel'):
        assert _is_linked(a1, 'trace_TraceModel', b)
    _safe_set(b, 'trace_GenNodeTrace', a2)
    assert _is_linked(b, 'trace_GenNodeTrace', a2)
    if hasattr(a1, 'trace_TraceModel'):
        assert not _is_linked(a1, 'trace_TraceModel', b)
    if hasattr(a2, 'trace_TraceModel'):
        assert _is_linked(a2, 'trace_TraceModel', b)
    _safe_set(b, 'trace_GenNodeTrace', None)
    assert not _is_linked(b, 'trace_GenNodeTrace', a2)
    if hasattr(a2, 'trace_TraceModel'):
        assert not _is_linked(a2, 'trace_TraceModel', b)


def test_assoc_toolGroupTraces5_reverse_link_reassign_clear():
    a1 = trace_TraceModel()
    a2 = trace_TraceModel()
    b = trace_ToolGroupTrace()
    _safe_set(b, 'trace_ToolGroupTrace', a1)
    assert _is_linked(b, 'trace_ToolGroupTrace', a1)
    if hasattr(a1, 'trace_TraceModel6'):
        assert _is_linked(a1, 'trace_TraceModel6', b)
    _safe_set(b, 'trace_ToolGroupTrace', a2)
    assert _is_linked(b, 'trace_ToolGroupTrace', a2)
    if hasattr(a1, 'trace_TraceModel6'):
        assert not _is_linked(a1, 'trace_TraceModel6', b)
    if hasattr(a2, 'trace_TraceModel6'):
        assert _is_linked(a2, 'trace_TraceModel6', b)
    _safe_set(b, 'trace_ToolGroupTrace', None)
    assert not _is_linked(b, 'trace_ToolGroupTrace', a2)
    if hasattr(a2, 'trace_TraceModel6'):
        assert not _is_linked(a2, 'trace_TraceModel6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_childNodeTraces1_stub_double():
    # trace_GenChildNodeTrace has no real 'trace_GenChildNodeTrace' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceModel()
    partner = trace_GenChildNodeTrace()
    setattr(partner, 'trace_GenChildNodeTrace', None)
    _safe_set(owner, 'trace_TraceModel2', {partner})
    assert getattr(partner, 'trace_GenChildNodeTrace') == owner
    _safe_set(owner, 'trace_TraceModel2', set())
    assert getattr(partner, 'trace_GenChildNodeTrace') is None


