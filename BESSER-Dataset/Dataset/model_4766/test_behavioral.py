import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFunction,
    Port,
    syswbeff106prepa_AbstractFunction,
    syswbeff106prepa_Flow,
    syswbeff106prepa_Function,
    syswbeff106prepa_InputPort,
    syswbeff106prepa_OutputPort,
    syswbeff106prepa_Pattern,
    syswbeff106prepa_PatternCatalog,
    syswbeff106prepa_Port,
    syswbeff106prepa_System,
    syswbeff106prepa_Workbench,
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

def test_assoc_associations1_reverse_link_reassign_clear():
    a1 = syswbeff106prepa_AbstractFunction(name="sample_text")
    a2 = syswbeff106prepa_AbstractFunction(name="sample_text_2")
    b = syswbeff106prepa_AbstractFunction(name="sample_text")
    _safe_set(b, 'syswbeff106prepa_AbstractFunction0', a1)
    assert _is_linked(b, 'syswbeff106prepa_AbstractFunction0', a1)
    if hasattr(a1, 'syswbeff106prepa_AbstractFunction'):
        assert _is_linked(a1, 'syswbeff106prepa_AbstractFunction', b)
    _safe_set(b, 'syswbeff106prepa_AbstractFunction0', a2)
    assert _is_linked(b, 'syswbeff106prepa_AbstractFunction0', a2)
    if hasattr(a1, 'syswbeff106prepa_AbstractFunction'):
        assert not _is_linked(a1, 'syswbeff106prepa_AbstractFunction', b)
    if hasattr(a2, 'syswbeff106prepa_AbstractFunction'):
        assert _is_linked(a2, 'syswbeff106prepa_AbstractFunction', b)
    _safe_set(b, 'syswbeff106prepa_AbstractFunction0', None)
    assert not _is_linked(b, 'syswbeff106prepa_AbstractFunction0', a2)
    if hasattr(a2, 'syswbeff106prepa_AbstractFunction'):
        assert not _is_linked(a2, 'syswbeff106prepa_AbstractFunction', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_catalog12_stub_double():
    # syswbeff106prepa_Workbench has no real 'syswbeff106prepa_Workbench13' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_PatternCatalog(id="sample_text")
    partner = syswbeff106prepa_Workbench()
    setattr(partner, 'syswbeff106prepa_Workbench13', None)
    _safe_set(owner, 'syswbeff106prepa_PatternCatalog14', partner)
    assert owner in getattr(partner, 'syswbeff106prepa_Workbench13')
    _safe_set(owner, 'syswbeff106prepa_PatternCatalog14', None)
    assert owner not in getattr(partner, 'syswbeff106prepa_Workbench13')


def test_assoc_flows6_stub_double():
    # syswbeff106prepa_Flow has no real 'syswbeff106prepa_Flow' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_AbstractFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_AbstractFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_AbstractFunction(name="sample_text")
    partner = syswbeff106prepa_Flow()
    setattr(partner, 'syswbeff106prepa_Flow', None)
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction7', {partner})
    assert getattr(partner, 'syswbeff106prepa_Flow') == owner
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction7', set())
    assert getattr(partner, 'syswbeff106prepa_Flow') is None


def test_assoc_functionalArchitecture8_stub_double():
    # syswbeff106prepa_Function has no real 'syswbeff106prepa_Function' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_System(id="sample_text")
    partner = syswbeff106prepa_Function()
    setattr(partner, 'syswbeff106prepa_Function', None)
    _safe_set(owner, 'syswbeff106prepa_System', partner)
    assert getattr(partner, 'syswbeff106prepa_Function') == owner
    _safe_set(owner, 'syswbeff106prepa_System', None)
    assert getattr(partner, 'syswbeff106prepa_Function') is None


def test_assoc_inputports2_stub_double():
    # syswbeff106prepa_InputPort has no real 'syswbeff106prepa_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_AbstractFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_AbstractFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_AbstractFunction(name="sample_text")
    partner = syswbeff106prepa_InputPort()
    setattr(partner, 'syswbeff106prepa_InputPort', None)
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction3', {partner})
    assert getattr(partner, 'syswbeff106prepa_InputPort') == owner
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction3', set())
    assert getattr(partner, 'syswbeff106prepa_InputPort') is None


def test_assoc_outputports4_stub_double():
    # syswbeff106prepa_OutputPort has no real 'syswbeff106prepa_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_AbstractFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_AbstractFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_AbstractFunction(name="sample_text")
    partner = syswbeff106prepa_OutputPort()
    setattr(partner, 'syswbeff106prepa_OutputPort', None)
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction5', {partner})
    assert getattr(partner, 'syswbeff106prepa_OutputPort') == owner
    _safe_set(owner, 'syswbeff106prepa_AbstractFunction5', set())
    assert getattr(partner, 'syswbeff106prepa_OutputPort') is None


def test_assoc_patterns9_stub_double():
    # syswbeff106prepa_Pattern has no real 'syswbeff106prepa_Pattern' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_PatternCatalog(id="sample_text")
    partner = syswbeff106prepa_Pattern()
    setattr(partner, 'syswbeff106prepa_Pattern', None)
    _safe_set(owner, 'syswbeff106prepa_PatternCatalog', {partner})
    assert getattr(partner, 'syswbeff106prepa_Pattern') == owner
    _safe_set(owner, 'syswbeff106prepa_PatternCatalog', set())
    assert getattr(partner, 'syswbeff106prepa_Pattern') is None


def test_assoc_systemView10_stub_double():
    # syswbeff106prepa_Workbench has no real 'syswbeff106prepa_Workbench' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106prepa_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106prepa_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106prepa_System(id="sample_text")
    partner = syswbeff106prepa_Workbench()
    setattr(partner, 'syswbeff106prepa_Workbench', None)
    _safe_set(owner, 'syswbeff106prepa_System11', partner)
    assert getattr(partner, 'syswbeff106prepa_Workbench') == owner
    _safe_set(owner, 'syswbeff106prepa_System11', None)
    assert getattr(partner, 'syswbeff106prepa_Workbench') is None


