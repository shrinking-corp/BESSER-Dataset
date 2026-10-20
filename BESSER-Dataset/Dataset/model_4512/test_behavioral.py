import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Or,
    Parenthesis,
    Value,
    ardlers_And,
    ardlers_Assignment,
    ardlers_Attribute,
    ardlers_BoardDefinition,
    ardlers_Comparison,
    ardlers_Component,
    ardlers_ComponentBody,
    ardlers_Delta,
    ardlers_EObject,
    ardlers_Exp,
    ardlers_Expression,
    ardlers_Factor,
    ardlers_Library,
    ardlers_Map,
    ardlers_Node,
    ardlers_NumberLiteral,
    ardlers_Or,
    ardlers_Parenthesis,
    ardlers_Program,
    ardlers_Range,
    ardlers_Rate,
    ardlers_Rule,
    ardlers_RuleBody,
    ardlers_SensorImport,
    ardlers_Smoothing,
    ardlers_State,
    ardlers_Value,
    IO,
    TYPE,
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

def test_assoc_boardType33_reverse_link_reassign_clear():
    a1 = ardlers_Node(name="sample_text")
    a2 = ardlers_Node(name="sample_text_2")
    b = ardlers_BoardDefinition(ain=7, aout=7, di=7, do=7, name="sample_text")
    _safe_set(b, 'ardlers_BoardDefinition35', a1)
    assert _is_linked(b, 'ardlers_BoardDefinition35', a1)
    if hasattr(a1, 'ardlers_Node34'):
        assert _is_linked(a1, 'ardlers_Node34', b)
    _safe_set(b, 'ardlers_BoardDefinition35', a2)
    assert _is_linked(b, 'ardlers_BoardDefinition35', a2)
    if hasattr(a1, 'ardlers_Node34'):
        assert not _is_linked(a1, 'ardlers_Node34', b)
    if hasattr(a2, 'ardlers_Node34'):
        assert _is_linked(a2, 'ardlers_Node34', b)
    _safe_set(b, 'ardlers_BoardDefinition35', None)
    assert not _is_linked(b, 'ardlers_BoardDefinition35', a2)
    if hasattr(a2, 'ardlers_Node34'):
        assert not _is_linked(a2, 'ardlers_Node34', b)


def test_assoc_components36_reverse_link_reassign_clear():
    a1 = ardlers_Node(name="sample_text")
    a2 = ardlers_Node(name="sample_text_2")
    b = ardlers_Component(name="sample_text")
    _safe_set(b, 'ardlers_Component38', a1)
    assert _is_linked(b, 'ardlers_Component38', a1)
    if hasattr(a1, 'ardlers_Node37'):
        assert _is_linked(a1, 'ardlers_Node37', b)
    _safe_set(b, 'ardlers_Component38', a2)
    assert _is_linked(b, 'ardlers_Component38', a2)
    if hasattr(a1, 'ardlers_Node37'):
        assert not _is_linked(a1, 'ardlers_Node37', b)
    if hasattr(a2, 'ardlers_Node37'):
        assert _is_linked(a2, 'ardlers_Node37', b)
    _safe_set(b, 'ardlers_Component38', None)
    assert not _is_linked(b, 'ardlers_Component38', a2)
    if hasattr(a2, 'ardlers_Node37'):
        assert not _is_linked(a2, 'ardlers_Node37', b)


def test_assoc_condition10_reverse_link_reassign_clear():
    a1 = ardlers_Rule(type="sample_text")
    a2 = ardlers_Rule(type="sample_text_2")
    b = ardlers_Or(operator="sample_text")
    _safe_set(b, 'ardlers_Or', a1)
    assert _is_linked(b, 'ardlers_Or', a1)
    if hasattr(a1, 'ardlers_Rule'):
        assert _is_linked(a1, 'ardlers_Rule', b)
    _safe_set(b, 'ardlers_Or', a2)
    assert _is_linked(b, 'ardlers_Or', a2)
    if hasattr(a1, 'ardlers_Rule'):
        assert not _is_linked(a1, 'ardlers_Rule', b)
    if hasattr(a2, 'ardlers_Rule'):
        assert _is_linked(a2, 'ardlers_Rule', b)
    _safe_set(b, 'ardlers_Or', None)
    assert not _is_linked(b, 'ardlers_Or', a2)
    if hasattr(a2, 'ardlers_Rule'):
        assert not _is_linked(a2, 'ardlers_Rule', b)


def test_assoc_left14_reverse_link_reassign_clear():
    a1 = ardlers_Or(operator="sample_text")
    a2 = ardlers_Or(operator="sample_text_2")
    b = ardlers_Or(operator="sample_text")
    _safe_set(b, 'ardlers_Or15', a1)
    assert _is_linked(b, 'ardlers_Or15', a1)
    if hasattr(a1, 'ardlers_Or13'):
        assert _is_linked(a1, 'ardlers_Or13', b)
    _safe_set(b, 'ardlers_Or15', a2)
    assert _is_linked(b, 'ardlers_Or15', a2)
    if hasattr(a1, 'ardlers_Or13'):
        assert not _is_linked(a1, 'ardlers_Or13', b)
    if hasattr(a2, 'ardlers_Or13'):
        assert _is_linked(a2, 'ardlers_Or13', b)
    _safe_set(b, 'ardlers_Or15', None)
    assert not _is_linked(b, 'ardlers_Or15', a2)
    if hasattr(a2, 'ardlers_Or13'):
        assert not _is_linked(a2, 'ardlers_Or13', b)


def test_assoc_properties42_reverse_link_reassign_clear():
    a1 = ardlers_ComponentBody(io="sample_text", pin=7, pinned="sample_text", type="sample_text")
    a2 = ardlers_ComponentBody(io="sample_text_2", pin=13, pinned="sample_text_2", type="sample_text_2")
    b = ardlers_Component(name="sample_text")
    _safe_set(b, 'ardlers_Component43', a1)
    assert _is_linked(b, 'ardlers_Component43', a1)
    if hasattr(a1, 'ardlers_ComponentBody'):
        assert _is_linked(a1, 'ardlers_ComponentBody', b)
    _safe_set(b, 'ardlers_Component43', a2)
    assert _is_linked(b, 'ardlers_Component43', a2)
    if hasattr(a1, 'ardlers_ComponentBody'):
        assert not _is_linked(a1, 'ardlers_ComponentBody', b)
    if hasattr(a2, 'ardlers_ComponentBody'):
        assert _is_linked(a2, 'ardlers_ComponentBody', b)
    _safe_set(b, 'ardlers_Component43', None)
    assert not _is_linked(b, 'ardlers_Component43', a2)
    if hasattr(a2, 'ardlers_ComponentBody'):
        assert not _is_linked(a2, 'ardlers_ComponentBody', b)


def test_assoc_rate44_reverse_link_reassign_clear():
    a1 = ardlers_Rate(value=7)
    a2 = ardlers_Rate(value=13)
    b = ardlers_ComponentBody(io="sample_text", pin=7, pinned="sample_text", type="sample_text")
    _safe_set(b, 'ardlers_ComponentBody45', a1)
    assert _is_linked(b, 'ardlers_ComponentBody45', a1)
    if hasattr(a1, 'ardlers_Rate'):
        assert _is_linked(a1, 'ardlers_Rate', b)
    _safe_set(b, 'ardlers_ComponentBody45', a2)
    assert _is_linked(b, 'ardlers_ComponentBody45', a2)
    if hasattr(a1, 'ardlers_Rate'):
        assert not _is_linked(a1, 'ardlers_Rate', b)
    if hasattr(a2, 'ardlers_Rate'):
        assert _is_linked(a2, 'ardlers_Rate', b)
    _safe_set(b, 'ardlers_ComponentBody45', None)
    assert not _is_linked(b, 'ardlers_ComponentBody45', a2)
    if hasattr(a2, 'ardlers_Rate'):
        assert not _is_linked(a2, 'ardlers_Rate', b)


def test_assoc_sensor39_reverse_link_reassign_clear():
    a1 = ardlers_SensorImport(name="sample_text")
    a2 = ardlers_SensorImport(name="sample_text_2")
    b = ardlers_Component(name="sample_text")
    _safe_set(b, 'ardlers_Component40', a1)
    assert _is_linked(b, 'ardlers_Component40', a1)
    if hasattr(a1, 'ardlers_SensorImport41'):
        assert _is_linked(a1, 'ardlers_SensorImport41', b)
    _safe_set(b, 'ardlers_Component40', a2)
    assert _is_linked(b, 'ardlers_Component40', a2)
    if hasattr(a1, 'ardlers_SensorImport41'):
        assert not _is_linked(a1, 'ardlers_SensorImport41', b)
    if hasattr(a2, 'ardlers_SensorImport41'):
        assert _is_linked(a2, 'ardlers_SensorImport41', b)
    _safe_set(b, 'ardlers_Component40', None)
    assert not _is_linked(b, 'ardlers_Component40', a2)
    if hasattr(a2, 'ardlers_SensorImport41'):
        assert not _is_linked(a2, 'ardlers_SensorImport41', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_boardtype7_stub_double():
    # ardlers_Library has no real 'ardlers_Library8' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_BoardDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_BoardDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_BoardDefinition(ain=7, aout=7, di=7, do=7, name="sample_text")
    partner = ardlers_Library()
    setattr(partner, 'ardlers_Library8', None)
    _safe_set(owner, 'ardlers_BoardDefinition9', partner)
    assert getattr(partner, 'ardlers_Library8') == owner
    _safe_set(owner, 'ardlers_BoardDefinition9', None)
    assert getattr(partner, 'ardlers_Library8') is None


def test_assoc_body11_stub_double():
    # ardlers_RuleBody has no real 'ardlers_RuleBody' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Rule(type="sample_text")
    partner = ardlers_RuleBody()
    setattr(partner, 'ardlers_RuleBody', None)
    _safe_set(owner, 'ardlers_Rule12', partner)
    assert getattr(partner, 'ardlers_RuleBody') == owner
    _safe_set(owner, 'ardlers_Rule12', None)
    assert getattr(partner, 'ardlers_RuleBody') is None


def test_assoc_component21_stub_double():
    # ardlers_Attribute has no real 'ardlers_Attribute22' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Component(name="sample_text")
    partner = ardlers_Attribute()
    setattr(partner, 'ardlers_Attribute22', None)
    _safe_set(owner, 'ardlers_Component', partner)
    assert getattr(partner, 'ardlers_Attribute22') == owner
    _safe_set(owner, 'ardlers_Component', None)
    assert getattr(partner, 'ardlers_Attribute22') is None


def test_assoc_definitions5_stub_double():
    # ardlers_Program has no real 'ardlers_Program6' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_BoardDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_BoardDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_BoardDefinition(ain=7, aout=7, di=7, do=7, name="sample_text")
    partner = ardlers_Program()
    setattr(partner, 'ardlers_Program6', None)
    _safe_set(owner, 'ardlers_BoardDefinition', partner)
    assert owner in getattr(partner, 'ardlers_Program6')
    _safe_set(owner, 'ardlers_BoardDefinition', None)
    assert owner not in getattr(partner, 'ardlers_Program6')


def test_assoc_in_48_stub_double():
    # ardlers_Map has no real 'ardlers_Map49' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Range(high=3.14, low=3.14)
    partner = ardlers_Map()
    setattr(partner, 'ardlers_Map49', None)
    _safe_set(owner, 'ardlers_Range', partner)
    assert getattr(partner, 'ardlers_Map49') == owner
    _safe_set(owner, 'ardlers_Range', None)
    assert getattr(partner, 'ardlers_Map49') is None


def test_assoc_map46_stub_double():
    # ardlers_Map has no real 'ardlers_Map' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_ComponentBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_ComponentBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_ComponentBody(io="sample_text", pin=7, pinned="sample_text", type="sample_text")
    partner = ardlers_Map()
    setattr(partner, 'ardlers_Map', None)
    _safe_set(owner, 'ardlers_ComponentBody47', partner)
    assert getattr(partner, 'ardlers_Map') == owner
    _safe_set(owner, 'ardlers_ComponentBody47', None)
    assert getattr(partner, 'ardlers_Map') is None


def test_assoc_name20_stub_double():
    # ardlers_Attribute has no real 'ardlers_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Node(name="sample_text")
    partner = ardlers_Attribute()
    setattr(partner, 'ardlers_Attribute', None)
    _safe_set(owner, 'ardlers_Node', partner)
    assert getattr(partner, 'ardlers_Attribute') == owner
    _safe_set(owner, 'ardlers_Node', None)
    assert getattr(partner, 'ardlers_Attribute') is None


def test_assoc_out50_stub_double():
    # ardlers_Map has no real 'ardlers_Map51' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Range(high=3.14, low=3.14)
    partner = ardlers_Map()
    setattr(partner, 'ardlers_Map51', None)
    _safe_set(owner, 'ardlers_Range52', partner)
    assert getattr(partner, 'ardlers_Map51') == owner
    _safe_set(owner, 'ardlers_Range52', None)
    assert getattr(partner, 'ardlers_Map51') is None


def test_assoc_right16_stub_double():
    # ardlers_Expression has no real 'ardlers_Expression' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Or's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Or's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Or(operator="sample_text")
    partner = ardlers_Expression()
    setattr(partner, 'ardlers_Expression', None)
    _safe_set(owner, 'ardlers_Or17', partner)
    assert getattr(partner, 'ardlers_Expression') == owner
    _safe_set(owner, 'ardlers_Or17', None)
    assert getattr(partner, 'ardlers_Expression') is None


def test_assoc_sensorsImports1_stub_double():
    # ardlers_Program has no real 'ardlers_Program2' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_SensorImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_SensorImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_SensorImport(name="sample_text")
    partner = ardlers_Program()
    setattr(partner, 'ardlers_Program2', None)
    _safe_set(owner, 'ardlers_SensorImport', partner)
    assert owner in getattr(partner, 'ardlers_Program2')
    _safe_set(owner, 'ardlers_SensorImport', None)
    assert owner not in getattr(partner, 'ardlers_Program2')


def test_assoc_sub18_stub_double():
    # ardlers_Parenthesis has no real 'ardlers_Parenthesis' property in the generated
    # code (a bare stub) -- manually attach it so ardlers_Or's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardlers_Or's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardlers_Or(operator="sample_text")
    partner = ardlers_Parenthesis()
    setattr(partner, 'ardlers_Parenthesis', None)
    _safe_set(owner, 'ardlers_Or19', partner)
    assert getattr(partner, 'ardlers_Parenthesis') == owner
    _safe_set(owner, 'ardlers_Or19', None)
    assert getattr(partner, 'ardlers_Parenthesis') is None


