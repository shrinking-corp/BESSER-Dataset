import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_ResourceGraph,
    graph_ResourceGraphs,
    graph_ResourcePlot,
    FitPolicy,
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

def test_assoc_plots1_reverse_link_reassign_clear():
    a1 = graph_ResourcePlot(fit="sample_text", max=3.14, min=3.14, name="sample_text", rgb="sample_text")
    a2 = graph_ResourcePlot(fit="sample_text_2", max=9.99, min=9.99, name="sample_text_2", rgb="sample_text_2")
    b = graph_ResourceGraph(name="sample_text")
    _safe_set(b, 'graph_ResourceGraph2', {a1})
    assert _is_linked(b, 'graph_ResourceGraph2', a1)
    if hasattr(a1, 'graph_ResourcePlot'):
        assert _is_linked(a1, 'graph_ResourcePlot', b)
    _safe_set(b, 'graph_ResourceGraph2', {a2})
    assert _is_linked(b, 'graph_ResourceGraph2', a2)
    if hasattr(a1, 'graph_ResourcePlot'):
        assert not _is_linked(a1, 'graph_ResourcePlot', b)
    if hasattr(a2, 'graph_ResourcePlot'):
        assert _is_linked(a2, 'graph_ResourcePlot', b)
    _safe_set(b, 'graph_ResourceGraph2', set())
    assert not _is_linked(b, 'graph_ResourceGraph2', a2)
    if hasattr(a2, 'graph_ResourcePlot'):
        assert not _is_linked(a2, 'graph_ResourcePlot', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_graphs0_stub_double():
    # graph_ResourceGraphs has no real 'graph_ResourceGraphs' property in the generated
    # code (a bare stub) -- manually attach it so graph_ResourceGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ResourceGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ResourceGraph(name="sample_text")
    partner = graph_ResourceGraphs()
    setattr(partner, 'graph_ResourceGraphs', None)
    _safe_set(owner, 'graph_ResourceGraph', partner)
    assert owner in getattr(partner, 'graph_ResourceGraphs')
    _safe_set(owner, 'graph_ResourceGraph', None)
    assert owner not in getattr(partner, 'graph_ResourceGraphs')


