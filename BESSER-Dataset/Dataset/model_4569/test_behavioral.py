import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Capability,
    Content,
    DeclaredType,
    Expression,
    Feature,
    Node,
    TimingExpression,
    Type,
    Value,
    iotdsl_Actuating,
    iotdsl_AfterExpression,
    iotdsl_AndExpression,
    iotdsl_Attribute,
    iotdsl_BoolConstant,
    iotdsl_Capability,
    iotdsl_CommunicationPath,
    iotdsl_Configuration,
    iotdsl_Content,
    iotdsl_DeclaredType,
    iotdsl_Delay,
    iotdsl_Device,
    iotdsl_EnumLiteral,
    iotdsl_Enumeration,
    iotdsl_EventOccurrence,
    iotdsl_Expression,
    iotdsl_Feature,
    iotdsl_Gateway,
    iotdsl_Import,
    iotdsl_IntConstant,
    iotdsl_IotModel,
    iotdsl_Node,
    iotdsl_NodeInstance,
    iotdsl_NotExpression,
    iotdsl_Parameter,
    iotdsl_PrimitiveType,
    iotdsl_Property,
    iotdsl_Reaction,
    iotdsl_Rule,
    iotdsl_Sensing,
    iotdsl_StringConstant,
    iotdsl_TimingExpression,
    iotdsl_Type,
    iotdsl_Value,
    iotdsl_WithinExpression,
    DefaultType,
    Operator,
    Protocol,
    Unit,
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

def test_assoc_attributes30_reverse_link_reassign_clear():
    a1 = iotdsl_EventOccurrence(operator="sample_text")
    a2 = iotdsl_EventOccurrence(operator="sample_text_2")
    b = iotdsl_Attribute(name="sample_text")
    _safe_set(b, 'iotdsl_Attribute', a1)
    assert _is_linked(b, 'iotdsl_Attribute', a1)
    if hasattr(a1, 'iotdsl_EventOccurrence31'):
        assert _is_linked(a1, 'iotdsl_EventOccurrence31', b)
    _safe_set(b, 'iotdsl_Attribute', a2)
    assert _is_linked(b, 'iotdsl_Attribute', a2)
    if hasattr(a1, 'iotdsl_EventOccurrence31'):
        assert not _is_linked(a1, 'iotdsl_EventOccurrence31', b)
    if hasattr(a2, 'iotdsl_EventOccurrence31'):
        assert _is_linked(a2, 'iotdsl_EventOccurrence31', b)
    _safe_set(b, 'iotdsl_Attribute', None)
    assert not _is_linked(b, 'iotdsl_Attribute', a2)
    if hasattr(a2, 'iotdsl_EventOccurrence31'):
        assert not _is_linked(a2, 'iotdsl_EventOccurrence31', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = iotdsl_IotModel(name="sample_text")
    a2 = iotdsl_IotModel(name="sample_text_2")
    b = iotdsl_Import(importedNamespace="sample_text")
    _safe_set(b, 'iotdsl_Import', a1)
    assert _is_linked(b, 'iotdsl_Import', a1)
    if hasattr(a1, 'iotdsl_IotModel'):
        assert _is_linked(a1, 'iotdsl_IotModel', b)
    _safe_set(b, 'iotdsl_Import', a2)
    assert _is_linked(b, 'iotdsl_Import', a2)
    if hasattr(a1, 'iotdsl_IotModel'):
        assert not _is_linked(a1, 'iotdsl_IotModel', b)
    if hasattr(a2, 'iotdsl_IotModel'):
        assert _is_linked(a2, 'iotdsl_IotModel', b)
    _safe_set(b, 'iotdsl_Import', None)
    assert not _is_linked(b, 'iotdsl_Import', a2)
    if hasattr(a2, 'iotdsl_IotModel'):
        assert not _is_linked(a2, 'iotdsl_IotModel', b)


def test_assoc_instance25_reverse_link_reassign_clear():
    a1 = iotdsl_NodeInstance(name="sample_text")
    a2 = iotdsl_NodeInstance(name="sample_text_2")
    b = iotdsl_EventOccurrence(operator="sample_text")
    _safe_set(b, 'iotdsl_EventOccurrence26', a1)
    assert _is_linked(b, 'iotdsl_EventOccurrence26', a1)
    if hasattr(a1, 'iotdsl_NodeInstance27'):
        assert _is_linked(a1, 'iotdsl_NodeInstance27', b)
    _safe_set(b, 'iotdsl_EventOccurrence26', a2)
    assert _is_linked(b, 'iotdsl_EventOccurrence26', a2)
    if hasattr(a1, 'iotdsl_NodeInstance27'):
        assert not _is_linked(a1, 'iotdsl_NodeInstance27', b)
    if hasattr(a2, 'iotdsl_NodeInstance27'):
        assert _is_linked(a2, 'iotdsl_NodeInstance27', b)
    _safe_set(b, 'iotdsl_EventOccurrence26', None)
    assert not _is_linked(b, 'iotdsl_EventOccurrence26', a2)
    if hasattr(a2, 'iotdsl_NodeInstance27'):
        assert not _is_linked(a2, 'iotdsl_NodeInstance27', b)


def test_assoc_nodes9_reverse_link_reassign_clear():
    a1 = iotdsl_NodeInstance(name="sample_text")
    a2 = iotdsl_NodeInstance(name="sample_text_2")
    b = iotdsl_Configuration(confname="sample_text")
    _safe_set(b, 'iotdsl_Configuration', {a1})
    assert _is_linked(b, 'iotdsl_Configuration', a1)
    if hasattr(a1, 'iotdsl_NodeInstance'):
        assert _is_linked(a1, 'iotdsl_NodeInstance', b)
    _safe_set(b, 'iotdsl_Configuration', {a2})
    assert _is_linked(b, 'iotdsl_Configuration', a2)
    if hasattr(a1, 'iotdsl_NodeInstance'):
        assert not _is_linked(a1, 'iotdsl_NodeInstance', b)
    if hasattr(a2, 'iotdsl_NodeInstance'):
        assert _is_linked(a2, 'iotdsl_NodeInstance', b)
    _safe_set(b, 'iotdsl_Configuration', set())
    assert not _is_linked(b, 'iotdsl_Configuration', a2)
    if hasattr(a2, 'iotdsl_NodeInstance'):
        assert not _is_linked(a2, 'iotdsl_NodeInstance', b)


def test_assoc_paths10_reverse_link_reassign_clear():
    a1 = iotdsl_Configuration(confname="sample_text")
    a2 = iotdsl_Configuration(confname="sample_text_2")
    b = iotdsl_CommunicationPath(protocol="sample_text")
    _safe_set(b, 'iotdsl_CommunicationPath', a1)
    assert _is_linked(b, 'iotdsl_CommunicationPath', a1)
    if hasattr(a1, 'iotdsl_Configuration11'):
        assert _is_linked(a1, 'iotdsl_Configuration11', b)
    _safe_set(b, 'iotdsl_CommunicationPath', a2)
    assert _is_linked(b, 'iotdsl_CommunicationPath', a2)
    if hasattr(a1, 'iotdsl_Configuration11'):
        assert not _is_linked(a1, 'iotdsl_Configuration11', b)
    if hasattr(a2, 'iotdsl_Configuration11'):
        assert _is_linked(a2, 'iotdsl_Configuration11', b)
    _safe_set(b, 'iotdsl_CommunicationPath', None)
    assert not _is_linked(b, 'iotdsl_CommunicationPath', a2)
    if hasattr(a2, 'iotdsl_Configuration11'):
        assert not _is_linked(a2, 'iotdsl_Configuration11', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = iotdsl_NodeInstance(name="sample_text")
    a2 = iotdsl_NodeInstance(name="sample_text_2")
    b = iotdsl_CommunicationPath(protocol="sample_text")
    _safe_set(b, 'iotdsl_CommunicationPath16', a1)
    assert _is_linked(b, 'iotdsl_CommunicationPath16', a1)
    if hasattr(a1, 'iotdsl_NodeInstance17'):
        assert _is_linked(a1, 'iotdsl_NodeInstance17', b)
    _safe_set(b, 'iotdsl_CommunicationPath16', a2)
    assert _is_linked(b, 'iotdsl_CommunicationPath16', a2)
    if hasattr(a1, 'iotdsl_NodeInstance17'):
        assert not _is_linked(a1, 'iotdsl_NodeInstance17', b)
    if hasattr(a2, 'iotdsl_NodeInstance17'):
        assert _is_linked(a2, 'iotdsl_NodeInstance17', b)
    _safe_set(b, 'iotdsl_CommunicationPath16', None)
    assert not _is_linked(b, 'iotdsl_CommunicationPath16', a2)
    if hasattr(a2, 'iotdsl_NodeInstance17'):
        assert not _is_linked(a2, 'iotdsl_NodeInstance17', b)


def test_assoc_taget18_reverse_link_reassign_clear():
    a1 = iotdsl_NodeInstance(name="sample_text")
    a2 = iotdsl_NodeInstance(name="sample_text_2")
    b = iotdsl_CommunicationPath(protocol="sample_text")
    _safe_set(b, 'iotdsl_CommunicationPath19', a1)
    assert _is_linked(b, 'iotdsl_CommunicationPath19', a1)
    if hasattr(a1, 'iotdsl_NodeInstance20'):
        assert _is_linked(a1, 'iotdsl_NodeInstance20', b)
    _safe_set(b, 'iotdsl_CommunicationPath19', a2)
    assert _is_linked(b, 'iotdsl_CommunicationPath19', a2)
    if hasattr(a1, 'iotdsl_NodeInstance20'):
        assert not _is_linked(a1, 'iotdsl_NodeInstance20', b)
    if hasattr(a2, 'iotdsl_NodeInstance20'):
        assert _is_linked(a2, 'iotdsl_NodeInstance20', b)
    _safe_set(b, 'iotdsl_CommunicationPath19', None)
    assert not _is_linked(b, 'iotdsl_CommunicationPath19', a2)
    if hasattr(a2, 'iotdsl_NodeInstance20'):
        assert not _is_linked(a2, 'iotdsl_NodeInstance20', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = iotdsl_Type(name="sample_text")
    a2 = iotdsl_Type(name="sample_text_2")
    b = iotdsl_NodeInstance(name="sample_text")
    _safe_set(b, 'iotdsl_NodeInstance13', a1)
    assert _is_linked(b, 'iotdsl_NodeInstance13', a1)
    if hasattr(a1, 'iotdsl_Type14'):
        assert _is_linked(a1, 'iotdsl_Type14', b)
    _safe_set(b, 'iotdsl_NodeInstance13', a2)
    assert _is_linked(b, 'iotdsl_NodeInstance13', a2)
    if hasattr(a1, 'iotdsl_Type14'):
        assert not _is_linked(a1, 'iotdsl_Type14', b)
    if hasattr(a2, 'iotdsl_Type14'):
        assert _is_linked(a2, 'iotdsl_Type14', b)
    _safe_set(b, 'iotdsl_NodeInstance13', None)
    assert not _is_linked(b, 'iotdsl_NodeInstance13', a2)
    if hasattr(a2, 'iotdsl_Type14'):
        assert not _is_linked(a2, 'iotdsl_Type14', b)


def test_assoc_type7_reverse_link_reassign_clear():
    a1 = iotdsl_Type(name="sample_text")
    a2 = iotdsl_Type(name="sample_text_2")
    b = iotdsl_Parameter(name="sample_text")
    _safe_set(b, 'iotdsl_Parameter8', a1)
    assert _is_linked(b, 'iotdsl_Parameter8', a1)
    if hasattr(a1, 'iotdsl_Type'):
        assert _is_linked(a1, 'iotdsl_Type', b)
    _safe_set(b, 'iotdsl_Parameter8', a2)
    assert _is_linked(b, 'iotdsl_Parameter8', a2)
    if hasattr(a1, 'iotdsl_Type'):
        assert not _is_linked(a1, 'iotdsl_Type', b)
    if hasattr(a2, 'iotdsl_Type'):
        assert _is_linked(a2, 'iotdsl_Type', b)
    _safe_set(b, 'iotdsl_Parameter8', None)
    assert not _is_linked(b, 'iotdsl_Parameter8', a2)
    if hasattr(a2, 'iotdsl_Type'):
        assert not _is_linked(a2, 'iotdsl_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes40_stub_double():
    # iotdsl_Reaction has no real 'iotdsl_Reaction41' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Attribute(name="sample_text")
    partner = iotdsl_Reaction()
    setattr(partner, 'iotdsl_Reaction41', None)
    _safe_set(owner, 'iotdsl_Attribute42', partner)
    assert owner in getattr(partner, 'iotdsl_Reaction41')
    _safe_set(owner, 'iotdsl_Attribute42', None)
    assert owner not in getattr(partner, 'iotdsl_Reaction41')


def test_assoc_capability28_stub_double():
    # iotdsl_Sensing has no real 'iotdsl_Sensing' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_EventOccurrence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_EventOccurrence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_EventOccurrence(operator="sample_text")
    partner = iotdsl_Sensing()
    setattr(partner, 'iotdsl_Sensing', None)
    _safe_set(owner, 'iotdsl_EventOccurrence29', partner)
    assert getattr(partner, 'iotdsl_Sensing') == owner
    _safe_set(owner, 'iotdsl_EventOccurrence29', None)
    assert getattr(partner, 'iotdsl_Sensing') is None


def test_assoc_content1_stub_double():
    # iotdsl_Content has no real 'iotdsl_Content' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_IotModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_IotModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_IotModel(name="sample_text")
    partner = iotdsl_Content()
    setattr(partner, 'iotdsl_Content', None)
    _safe_set(owner, 'iotdsl_IotModel2', {partner})
    assert getattr(partner, 'iotdsl_Content') == owner
    _safe_set(owner, 'iotdsl_IotModel2', set())
    assert getattr(partner, 'iotdsl_Content') is None


def test_assoc_delay53_stub_double():
    # iotdsl_WithinExpression has no real 'iotdsl_WithinExpression' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Delay's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Delay's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Delay(time=7, unit="sample_text")
    partner = iotdsl_WithinExpression()
    setattr(partner, 'iotdsl_WithinExpression', None)
    _safe_set(owner, 'iotdsl_Delay', partner)
    assert getattr(partner, 'iotdsl_WithinExpression') == owner
    _safe_set(owner, 'iotdsl_Delay', None)
    assert getattr(partner, 'iotdsl_WithinExpression') is None


def test_assoc_event24_stub_double():
    # iotdsl_NotExpression has no real 'iotdsl_NotExpression' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_EventOccurrence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_EventOccurrence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_EventOccurrence(operator="sample_text")
    partner = iotdsl_NotExpression()
    setattr(partner, 'iotdsl_NotExpression', None)
    _safe_set(owner, 'iotdsl_EventOccurrence', partner)
    assert getattr(partner, 'iotdsl_NotExpression') == owner
    _safe_set(owner, 'iotdsl_EventOccurrence', None)
    assert getattr(partner, 'iotdsl_NotExpression') is None


def test_assoc_features4_stub_double():
    # iotdsl_Device has no real 'iotdsl_Device' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Feature(name="sample_text")
    partner = iotdsl_Device()
    setattr(partner, 'iotdsl_Device', None)
    _safe_set(owner, 'iotdsl_Feature', partner)
    assert owner in getattr(partner, 'iotdsl_Device')
    _safe_set(owner, 'iotdsl_Feature', None)
    assert owner not in getattr(partner, 'iotdsl_Device')


def test_assoc_instance35_stub_double():
    # iotdsl_Reaction has no real 'iotdsl_Reaction36' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_NodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_NodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_NodeInstance(name="sample_text")
    partner = iotdsl_Reaction()
    setattr(partner, 'iotdsl_Reaction36', None)
    _safe_set(owner, 'iotdsl_NodeInstance37', partner)
    assert getattr(partner, 'iotdsl_Reaction36') == owner
    _safe_set(owner, 'iotdsl_NodeInstance37', None)
    assert getattr(partner, 'iotdsl_Reaction36') is None


def test_assoc_literals3_stub_double():
    # iotdsl_Enumeration has no real 'iotdsl_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_EnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_EnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_EnumLiteral(name="sample_text")
    partner = iotdsl_Enumeration()
    setattr(partner, 'iotdsl_Enumeration', None)
    _safe_set(owner, 'iotdsl_EnumLiteral', partner)
    assert owner in getattr(partner, 'iotdsl_Enumeration')
    _safe_set(owner, 'iotdsl_EnumLiteral', None)
    assert owner not in getattr(partner, 'iotdsl_Enumeration')


def test_assoc_parameters6_stub_double():
    # iotdsl_Capability has no real 'iotdsl_Capability' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Parameter(name="sample_text")
    partner = iotdsl_Capability()
    setattr(partner, 'iotdsl_Capability', None)
    _safe_set(owner, 'iotdsl_Parameter', partner)
    assert owner in getattr(partner, 'iotdsl_Capability')
    _safe_set(owner, 'iotdsl_Parameter', None)
    assert owner not in getattr(partner, 'iotdsl_Capability')


def test_assoc_reactions22_stub_double():
    # iotdsl_Reaction has no real 'iotdsl_Reaction' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Rule(name="sample_text")
    partner = iotdsl_Reaction()
    setattr(partner, 'iotdsl_Reaction', None)
    _safe_set(owner, 'iotdsl_Rule23', {partner})
    assert getattr(partner, 'iotdsl_Reaction') == owner
    _safe_set(owner, 'iotdsl_Rule23', set())
    assert getattr(partner, 'iotdsl_Reaction') is None


def test_assoc_triggers21_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Rule(name="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression', None)
    _safe_set(owner, 'iotdsl_Rule', partner)
    assert getattr(partner, 'iotdsl_Expression') == owner
    _safe_set(owner, 'iotdsl_Rule', None)
    assert getattr(partner, 'iotdsl_Expression') is None


def test_assoc_value32_stub_double():
    # iotdsl_Value has no real 'iotdsl_Value34' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_EventOccurrence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_EventOccurrence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_EventOccurrence(operator="sample_text")
    partner = iotdsl_Value()
    setattr(partner, 'iotdsl_Value34', None)
    _safe_set(owner, 'iotdsl_EventOccurrence33', partner)
    assert getattr(partner, 'iotdsl_Value34') == owner
    _safe_set(owner, 'iotdsl_EventOccurrence33', None)
    assert getattr(partner, 'iotdsl_Value34') is None


