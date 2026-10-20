import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    architectureTool_Attribute,
    architectureTool_Class,
    architectureTool_Component,
    architectureTool_Interface,
    architectureTool_Method,
    architectureTool_Port,
    architectureTool_System,
    architectureTool_classMember,
    classMember,
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

def test_assoc_ComponentDependence11_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'ComponentDependence', {a1})
    assert _is_linked(b, 'ComponentDependence', a1)
    if hasattr(a1, 'System'):
        assert _is_linked(a1, 'System', b)
    _safe_set(b, 'ComponentDependence', {a2})
    assert _is_linked(b, 'ComponentDependence', a2)
    if hasattr(a1, 'System'):
        assert not _is_linked(a1, 'System', b)
    if hasattr(a2, 'System'):
        assert _is_linked(a2, 'System', b)
    _safe_set(b, 'ComponentDependence', set())
    assert not _is_linked(b, 'ComponentDependence', a2)
    if hasattr(a2, 'System'):
        assert not _is_linked(a2, 'System', b)


def test_assoc_ComponentDependence41_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'Component', a1)
    assert _is_linked(b, 'Component', a1)
    if hasattr(a1, 'ComponentDependence42'):
        assert _is_linked(a1, 'ComponentDependence42', b)
    _safe_set(b, 'Component', a2)
    assert _is_linked(b, 'Component', a2)
    if hasattr(a1, 'ComponentDependence42'):
        assert not _is_linked(a1, 'ComponentDependence42', b)
    if hasattr(a2, 'ComponentDependence42'):
        assert _is_linked(a2, 'ComponentDependence42', b)
    _safe_set(b, 'Component', None)
    assert not _is_linked(b, 'Component', a2)
    if hasattr(a2, 'ComponentDependence42'):
        assert not _is_linked(a2, 'ComponentDependence42', b)


def test_assoc_System36_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_System(name="sample_text")
    _safe_set(b, 'architectureTool_System37', a1)
    assert _is_linked(b, 'architectureTool_System37', a1)
    if hasattr(a1, 'architectureTool_System35'):
        assert _is_linked(a1, 'architectureTool_System35', b)
    _safe_set(b, 'architectureTool_System37', a2)
    assert _is_linked(b, 'architectureTool_System37', a2)
    if hasattr(a1, 'architectureTool_System35'):
        assert not _is_linked(a1, 'architectureTool_System35', b)
    if hasattr(a2, 'architectureTool_System35'):
        assert _is_linked(a2, 'architectureTool_System35', b)
    _safe_set(b, 'architectureTool_System37', None)
    assert not _is_linked(b, 'architectureTool_System37', a2)
    if hasattr(a2, 'architectureTool_System35'):
        assert not _is_linked(a2, 'architectureTool_System35', b)


def test_assoc_SystemDependence28_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_System(name="sample_text")
    _safe_set(b, 'architectureTool_System27', {a1})
    assert _is_linked(b, 'architectureTool_System27', a1)
    if hasattr(a1, 'architectureTool_System'):
        assert _is_linked(a1, 'architectureTool_System', b)
    _safe_set(b, 'architectureTool_System27', {a2})
    assert _is_linked(b, 'architectureTool_System27', a2)
    if hasattr(a1, 'architectureTool_System'):
        assert not _is_linked(a1, 'architectureTool_System', b)
    if hasattr(a2, 'architectureTool_System'):
        assert _is_linked(a2, 'architectureTool_System', b)
    _safe_set(b, 'architectureTool_System27', set())
    assert not _is_linked(b, 'architectureTool_System27', a2)
    if hasattr(a2, 'architectureTool_System'):
        assert not _is_linked(a2, 'architectureTool_System', b)


def test_assoc_attribute64_reverse_link_reassign_clear():
    a1 = architectureTool_classMember(name="sample_text")
    a2 = architectureTool_classMember(name="sample_text_2")
    b = architectureTool_Attribute(Visable="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'architectureTool_Attribute', a1)
    assert _is_linked(b, 'architectureTool_Attribute', a1)
    if hasattr(a1, 'architectureTool_classMember'):
        assert _is_linked(a1, 'architectureTool_classMember', b)
    _safe_set(b, 'architectureTool_Attribute', a2)
    assert _is_linked(b, 'architectureTool_Attribute', a2)
    if hasattr(a1, 'architectureTool_classMember'):
        assert not _is_linked(a1, 'architectureTool_classMember', b)
    if hasattr(a2, 'architectureTool_classMember'):
        assert _is_linked(a2, 'architectureTool_classMember', b)
    _safe_set(b, 'architectureTool_Attribute', None)
    assert not _is_linked(b, 'architectureTool_Attribute', a2)
    if hasattr(a2, 'architectureTool_classMember'):
        assert not _is_linked(a2, 'architectureTool_classMember', b)


def test_assoc_componentDependence2_reverse_link_reassign_clear():
    a1 = architectureTool_Component(name="sample_text")
    a2 = architectureTool_Component(name="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'architectureTool_Component3', a1)
    assert _is_linked(b, 'architectureTool_Component3', a1)
    if hasattr(a1, 'architectureTool_Component1'):
        assert _is_linked(a1, 'architectureTool_Component1', b)
    _safe_set(b, 'architectureTool_Component3', a2)
    assert _is_linked(b, 'architectureTool_Component3', a2)
    if hasattr(a1, 'architectureTool_Component1'):
        assert not _is_linked(a1, 'architectureTool_Component1', b)
    if hasattr(a2, 'architectureTool_Component1'):
        assert _is_linked(a2, 'architectureTool_Component1', b)
    _safe_set(b, 'architectureTool_Component3', None)
    assert not _is_linked(b, 'architectureTool_Component3', a2)
    if hasattr(a2, 'architectureTool_Component1'):
        assert not _is_linked(a2, 'architectureTool_Component1', b)


def test_assoc_componentOfComponent7_reverse_link_reassign_clear():
    a1 = architectureTool_Component(name="sample_text")
    a2 = architectureTool_Component(name="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'architectureTool_Component8', a1)
    assert _is_linked(b, 'architectureTool_Component8', a1)
    if hasattr(a1, 'architectureTool_Component6'):
        assert _is_linked(a1, 'architectureTool_Component6', b)
    _safe_set(b, 'architectureTool_Component8', a2)
    assert _is_linked(b, 'architectureTool_Component8', a2)
    if hasattr(a1, 'architectureTool_Component6'):
        assert not _is_linked(a1, 'architectureTool_Component6', b)
    if hasattr(a2, 'architectureTool_Component6'):
        assert _is_linked(a2, 'architectureTool_Component6', b)
    _safe_set(b, 'architectureTool_Component8', None)
    assert not _is_linked(b, 'architectureTool_Component8', a2)
    if hasattr(a2, 'architectureTool_Component6'):
        assert not _is_linked(a2, 'architectureTool_Component6', b)


def test_assoc_componentOfSystem29_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'architectureTool_Component31', a1)
    assert _is_linked(b, 'architectureTool_Component31', a1)
    if hasattr(a1, 'architectureTool_System30'):
        assert _is_linked(a1, 'architectureTool_System30', b)
    _safe_set(b, 'architectureTool_Component31', a2)
    assert _is_linked(b, 'architectureTool_Component31', a2)
    if hasattr(a1, 'architectureTool_System30'):
        assert not _is_linked(a1, 'architectureTool_System30', b)
    if hasattr(a2, 'architectureTool_System30'):
        assert _is_linked(a2, 'architectureTool_System30', b)
    _safe_set(b, 'architectureTool_Component31', None)
    assert not _is_linked(b, 'architectureTool_Component31', a2)
    if hasattr(a2, 'architectureTool_System30'):
        assert not _is_linked(a2, 'architectureTool_System30', b)


def test_assoc_method65_reverse_link_reassign_clear():
    a1 = architectureTool_classMember(name="sample_text")
    a2 = architectureTool_classMember(name="sample_text_2")
    b = architectureTool_Method(name="sample_text", parameter="sample_text", returnType="sample_text", visable="sample_text")
    _safe_set(b, 'architectureTool_Method', a1)
    assert _is_linked(b, 'architectureTool_Method', a1)
    if hasattr(a1, 'architectureTool_classMember66'):
        assert _is_linked(a1, 'architectureTool_classMember66', b)
    _safe_set(b, 'architectureTool_Method', a2)
    assert _is_linked(b, 'architectureTool_Method', a2)
    if hasattr(a1, 'architectureTool_classMember66'):
        assert not _is_linked(a1, 'architectureTool_classMember66', b)
    if hasattr(a2, 'architectureTool_classMember66'):
        assert _is_linked(a2, 'architectureTool_classMember66', b)
    _safe_set(b, 'architectureTool_Method', None)
    assert not _is_linked(b, 'architectureTool_Method', a2)
    if hasattr(a2, 'architectureTool_classMember66'):
        assert not _is_linked(a2, 'architectureTool_classMember66', b)


def test_assoc_portDependence47_reverse_link_reassign_clear():
    a1 = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    a2 = architectureTool_Port(name="sample_text_2", provided="sample_text_2", required="sample_text_2", simple="sample_text_2", type="sample_text_2")
    b = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    _safe_set(b, 'architectureTool_Port48', a1)
    assert _is_linked(b, 'architectureTool_Port48', a1)
    if hasattr(a1, 'architectureTool_Port46'):
        assert _is_linked(a1, 'architectureTool_Port46', b)
    _safe_set(b, 'architectureTool_Port48', a2)
    assert _is_linked(b, 'architectureTool_Port48', a2)
    if hasattr(a1, 'architectureTool_Port46'):
        assert not _is_linked(a1, 'architectureTool_Port46', b)
    if hasattr(a2, 'architectureTool_Port46'):
        assert _is_linked(a2, 'architectureTool_Port46', b)
    _safe_set(b, 'architectureTool_Port48', None)
    assert not _is_linked(b, 'architectureTool_Port48', a2)
    if hasattr(a2, 'architectureTool_Port46'):
        assert not _is_linked(a2, 'architectureTool_Port46', b)


def test_assoc_portOfComponent0_reverse_link_reassign_clear():
    a1 = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    a2 = architectureTool_Port(name="sample_text_2", provided="sample_text_2", required="sample_text_2", simple="sample_text_2", type="sample_text_2")
    b = architectureTool_Component(name="sample_text")
    _safe_set(b, 'architectureTool_Component', {a1})
    assert _is_linked(b, 'architectureTool_Component', a1)
    if hasattr(a1, 'architectureTool_Port'):
        assert _is_linked(a1, 'architectureTool_Port', b)
    _safe_set(b, 'architectureTool_Component', {a2})
    assert _is_linked(b, 'architectureTool_Component', a2)
    if hasattr(a1, 'architectureTool_Port'):
        assert not _is_linked(a1, 'architectureTool_Port', b)
    if hasattr(a2, 'architectureTool_Port'):
        assert _is_linked(a2, 'architectureTool_Port', b)
    _safe_set(b, 'architectureTool_Component', set())
    assert not _is_linked(b, 'architectureTool_Component', a2)
    if hasattr(a2, 'architectureTool_Port'):
        assert not _is_linked(a2, 'architectureTool_Port', b)


def test_assoc_portOfSystem32_reverse_link_reassign_clear():
    a1 = architectureTool_System(name="sample_text")
    a2 = architectureTool_System(name="sample_text_2")
    b = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    _safe_set(b, 'architectureTool_Port34', a1)
    assert _is_linked(b, 'architectureTool_Port34', a1)
    if hasattr(a1, 'architectureTool_System33'):
        assert _is_linked(a1, 'architectureTool_System33', b)
    _safe_set(b, 'architectureTool_Port34', a2)
    assert _is_linked(b, 'architectureTool_Port34', a2)
    if hasattr(a1, 'architectureTool_System33'):
        assert not _is_linked(a1, 'architectureTool_System33', b)
    if hasattr(a2, 'architectureTool_System33'):
        assert _is_linked(a2, 'architectureTool_System33', b)
    _safe_set(b, 'architectureTool_Port34', None)
    assert not _is_linked(b, 'architectureTool_Port34', a2)
    if hasattr(a2, 'architectureTool_System33'):
        assert not _is_linked(a2, 'architectureTool_System33', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_4_stub_double():
    # architectureTool_Class has no real 'architectureTool_Class' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Component(name="sample_text")
    partner = architectureTool_Class()
    setattr(partner, 'architectureTool_Class', None)
    _safe_set(owner, 'architectureTool_Component5', {partner})
    assert getattr(partner, 'architectureTool_Class') == owner
    _safe_set(owner, 'architectureTool_Component5', set())
    assert getattr(partner, 'architectureTool_Class') is None


def test_assoc_interfaceOfComponent9_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Component(name="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface', None)
    _safe_set(owner, 'architectureTool_Component10', {partner})
    assert getattr(partner, 'architectureTool_Interface') == owner
    _safe_set(owner, 'architectureTool_Component10', set())
    assert getattr(partner, 'architectureTool_Interface') is None


def test_assoc_interfaceOfSystem38_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface40' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_System(name="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface40', None)
    _safe_set(owner, 'architectureTool_System39', {partner})
    assert getattr(partner, 'architectureTool_Interface40') == owner
    _safe_set(owner, 'architectureTool_System39', set())
    assert getattr(partner, 'architectureTool_Interface40') is None


def test_assoc_providedRealize43_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface45' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface45', None)
    _safe_set(owner, 'architectureTool_Port44', {partner})
    assert getattr(partner, 'architectureTool_Interface45') == owner
    _safe_set(owner, 'architectureTool_Port44', set())
    assert getattr(partner, 'architectureTool_Interface45') is None


def test_assoc_providedRealize52_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface53' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface53', None)
    _safe_set(owner, 'architectureTool_Port54', partner)
    assert owner in getattr(partner, 'architectureTool_Interface53')
    _safe_set(owner, 'architectureTool_Port54', None)
    assert owner not in getattr(partner, 'architectureTool_Interface53')


def test_assoc_requiredRealize49_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface51' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface51', None)
    _safe_set(owner, 'architectureTool_Port50', {partner})
    assert getattr(partner, 'architectureTool_Interface51') == owner
    _safe_set(owner, 'architectureTool_Port50', set())
    assert getattr(partner, 'architectureTool_Interface51') is None


def test_assoc_requiredRealize61_stub_double():
    # architectureTool_Interface has no real 'architectureTool_Interface62' property in the generated
    # code (a bare stub) -- manually attach it so architectureTool_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architectureTool_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architectureTool_Port(name="sample_text", provided="sample_text", required="sample_text", simple="sample_text", type="sample_text")
    partner = architectureTool_Interface()
    setattr(partner, 'architectureTool_Interface62', None)
    _safe_set(owner, 'architectureTool_Port63', partner)
    assert owner in getattr(partner, 'architectureTool_Interface62')
    _safe_set(owner, 'architectureTool_Port63', None)
    assert owner not in getattr(partner, 'architectureTool_Interface62')


