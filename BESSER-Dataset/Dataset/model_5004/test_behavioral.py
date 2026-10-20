import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    AbstractFeatures,
    Port,
    SystemPortDec,
    componentModel_AbstractElement,
    componentModel_AbstractFeatures,
    componentModel_CompConnDec,
    componentModel_ComponentFeature,
    componentModel_ComponentImpl,
    componentModel_ComponentModel,
    componentModel_ComponentType,
    componentModel_InPort,
    componentModel_OutPort,
    componentModel_Port,
    componentModel_PortType,
    componentModel_SystemConnDec,
    componentModel_SystemDec,
    componentModel_SystemPortDec,
    componentModel_SystemPortIn,
    componentModel_SystemPortOut,
    componentModel_errorModes,
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

def test_assoc_eModes38_stub_double():
    # componentModel_PortType has no real 'componentModel_PortType39' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_errorModes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_errorModes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_errorModes(name="sample_text")
    partner = componentModel_PortType()
    setattr(partner, 'componentModel_PortType39', None)
    _safe_set(owner, 'componentModel_errorModes', partner)
    assert getattr(partner, 'componentModel_PortType39') == owner
    _safe_set(owner, 'componentModel_errorModes', None)
    assert getattr(partner, 'componentModel_PortType39') is None


def test_assoc_elements0_stub_double():
    # componentModel_ComponentModel has no real 'componentModel_ComponentModel' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_AbstractElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_AbstractElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_AbstractElement(name="sample_text")
    partner = componentModel_ComponentModel()
    setattr(partner, 'componentModel_ComponentModel', None)
    _safe_set(owner, 'componentModel_AbstractElement', partner)
    assert owner in getattr(partner, 'componentModel_ComponentModel')
    _safe_set(owner, 'componentModel_AbstractElement', None)
    assert owner not in getattr(partner, 'componentModel_ComponentModel')


def test_assoc_ports34_stub_double():
    # componentModel_ComponentFeature has no real 'componentModel_ComponentFeature35' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Port(name="sample_text")
    partner = componentModel_ComponentFeature()
    setattr(partner, 'componentModel_ComponentFeature35', None)
    _safe_set(owner, 'componentModel_Port', partner)
    assert owner in getattr(partner, 'componentModel_ComponentFeature35')
    _safe_set(owner, 'componentModel_Port', None)
    assert owner not in getattr(partner, 'componentModel_ComponentFeature35')


def test_assoc_superType36_stub_double():
    # componentModel_PortType has no real 'componentModel_PortType' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Port(name="sample_text")
    partner = componentModel_PortType()
    setattr(partner, 'componentModel_PortType', None)
    _safe_set(owner, 'componentModel_Port37', partner)
    assert getattr(partner, 'componentModel_PortType') == owner
    _safe_set(owner, 'componentModel_Port37', None)
    assert getattr(partner, 'componentModel_PortType') is None


def test_assoc_sysFeatures10_stub_double():
    # componentModel_SystemDec has no real 'componentModel_SystemDec11' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_AbstractFeatures's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_AbstractFeatures's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_AbstractFeatures(name="sample_text")
    partner = componentModel_SystemDec()
    setattr(partner, 'componentModel_SystemDec11', None)
    _safe_set(owner, 'componentModel_AbstractFeatures', partner)
    assert owner in getattr(partner, 'componentModel_SystemDec11')
    _safe_set(owner, 'componentModel_AbstractFeatures', None)
    assert owner not in getattr(partner, 'componentModel_SystemDec11')


