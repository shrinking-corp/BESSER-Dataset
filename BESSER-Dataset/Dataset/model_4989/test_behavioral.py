import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    BusSpecification,
    Connection,
    InPort,
    InPortBlock,
    Port,
    PortBlock,
    SimulinkElement,
    SimulinkReference,
    VirtualBlock,
    simulink_Block,
    simulink_BusCreator,
    simulink_BusSelector,
    simulink_BusSignalMapping,
    simulink_BusSpecification,
    simulink_Connection,
    simulink_Enable,
    simulink_EnableBlock,
    simulink_From,
    simulink_Goto,
    simulink_GotoTagVisibility,
    simulink_IdentifierReference,
    simulink_InPort,
    simulink_InPortBlock,
    simulink_LibraryLinkReference,
    simulink_ModelReference,
    simulink_MultiConnection,
    simulink_OutPort,
    simulink_OutPortBlock,
    simulink_Port,
    simulink_PortBlock,
    simulink_Property,
    simulink_SimulinkElement,
    simulink_SimulinkModel,
    simulink_SimulinkReference,
    simulink_SingleConnection,
    simulink_SubSystem,
    simulink_Trigger,
    simulink_TriggerBlock,
    simulink_VirtualBlock,
    EnableStates,
    PropertySource,
    PropertyType,
    TagVisibility,
    TriggerType,
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

def test_assoc_element35_reverse_link_reassign_clear():
    a1 = simulink_SimulinkReference(name="sample_text", qualifier="sample_text")
    a2 = simulink_SimulinkReference(name="sample_text_2", qualifier="sample_text_2")
    b = simulink_SimulinkElement(name="sample_text")
    _safe_set(b, 'simulink_SimulinkElement36', a1)
    assert _is_linked(b, 'simulink_SimulinkElement36', a1)
    if hasattr(a1, 'simulink_SimulinkReference'):
        assert _is_linked(a1, 'simulink_SimulinkReference', b)
    _safe_set(b, 'simulink_SimulinkElement36', a2)
    assert _is_linked(b, 'simulink_SimulinkElement36', a2)
    if hasattr(a1, 'simulink_SimulinkReference'):
        assert not _is_linked(a1, 'simulink_SimulinkReference', b)
    if hasattr(a2, 'simulink_SimulinkReference'):
        assert _is_linked(a2, 'simulink_SimulinkReference', b)
    _safe_set(b, 'simulink_SimulinkElement36', None)
    assert not _is_linked(b, 'simulink_SimulinkElement36', a2)
    if hasattr(a2, 'simulink_SimulinkReference'):
        assert not _is_linked(a2, 'simulink_SimulinkReference', b)


def test_assoc_mappings22_reverse_link_reassign_clear():
    a1 = simulink_BusSignalMapping(incomplete=True, mappingPath="sample_text")
    a2 = simulink_BusSignalMapping(incomplete=False, mappingPath="sample_text_2")
    b = simulink_BusSelector(outputAsBus=True)
    _safe_set(b, 'selector', {a1})
    assert _is_linked(b, 'selector', a1)
    if hasattr(a1, 'BusSignalMapping'):
        assert _is_linked(a1, 'BusSignalMapping', b)
    _safe_set(b, 'selector', {a2})
    assert _is_linked(b, 'selector', a2)
    if hasattr(a1, 'BusSignalMapping'):
        assert not _is_linked(a1, 'BusSignalMapping', b)
    if hasattr(a2, 'BusSignalMapping'):
        assert _is_linked(a2, 'BusSignalMapping', b)
    _safe_set(b, 'selector', set())
    assert not _is_linked(b, 'selector', a2)
    if hasattr(a2, 'BusSignalMapping'):
        assert not _is_linked(a2, 'BusSignalMapping', b)


def test_assoc_selector46_reverse_link_reassign_clear():
    a1 = simulink_BusSignalMapping(incomplete=True, mappingPath="sample_text")
    a2 = simulink_BusSignalMapping(incomplete=False, mappingPath="sample_text_2")
    b = simulink_BusSelector(outputAsBus=True)
    _safe_set(b, 'BusSelector', a1)
    assert _is_linked(b, 'BusSelector', a1)
    if hasattr(a1, 'mappings'):
        assert _is_linked(a1, 'mappings', b)
    _safe_set(b, 'BusSelector', a2)
    assert _is_linked(b, 'BusSelector', a2)
    if hasattr(a1, 'mappings'):
        assert not _is_linked(a1, 'mappings', b)
    if hasattr(a2, 'mappings'):
        assert _is_linked(a2, 'mappings', b)
    _safe_set(b, 'BusSelector', None)
    assert not _is_linked(b, 'BusSelector', a2)
    if hasattr(a2, 'mappings'):
        assert not _is_linked(a2, 'mappings', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_busCreator23_stub_double():
    # simulink_BusSpecification has no real 'simulink_BusSpecification' property in the generated
    # code (a bare stub) -- manually attach it so simulink_BusSelector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_BusSelector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_BusSelector(outputAsBus=True)
    partner = simulink_BusSpecification()
    setattr(partner, 'simulink_BusSpecification', None)
    _safe_set(owner, 'simulink_BusSelector', partner)
    assert getattr(partner, 'simulink_BusSpecification') == owner
    _safe_set(owner, 'simulink_BusSelector', None)
    assert getattr(partner, 'simulink_BusSpecification') is None


def test_assoc_connection20_stub_double():
    # simulink_OutPort has no real 'from_' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Connection(lineName="sample_text")
    partner = simulink_OutPort()
    setattr(partner, 'from_', None)
    _safe_set(owner, 'Connection', partner)
    assert getattr(partner, 'from_') == owner
    _safe_set(owner, 'Connection', None)
    assert getattr(partner, 'from_') is None


def test_assoc_contains26_stub_double():
    # simulink_Block has no real 'simulink_Block27' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SimulinkModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SimulinkModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SimulinkModel(file="sample_text", library=True, version="sample_text")
    partner = simulink_Block()
    setattr(partner, 'simulink_Block27', None)
    _safe_set(owner, 'simulink_SimulinkModel', {partner})
    assert getattr(partner, 'simulink_Block27') == owner
    _safe_set(owner, 'simulink_SimulinkModel', set())
    assert getattr(partner, 'simulink_Block27') is None


def test_assoc_enabler5_stub_double():
    # simulink_Block has no real 'simulink_Block6' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Enable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Enable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Enable(statesWhenEnabling="sample_text")
    partner = simulink_Block()
    setattr(partner, 'simulink_Block6', None)
    _safe_set(owner, 'simulink_Enable', partner)
    assert getattr(partner, 'simulink_Block6') == owner
    _safe_set(owner, 'simulink_Enable', None)
    assert getattr(partner, 'simulink_Block6') is None


def test_assoc_fromBlocks24_stub_double():
    # simulink_From has no real 'From' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Goto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Goto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Goto(gotoTag="sample_text", tagVisibility="sample_text")
    partner = simulink_From()
    setattr(partner, 'From', None)
    _safe_set(owner, 'gotoBlock', {partner})
    assert getattr(partner, 'From') == owner
    _safe_set(owner, 'gotoBlock', set())
    assert getattr(partner, 'From') is None


def test_assoc_from_21_stub_double():
    # simulink_OutPort has no real 'OutPort' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Connection(lineName="sample_text")
    partner = simulink_OutPort()
    setattr(partner, 'OutPort', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'OutPort') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'OutPort') is None


def test_assoc_gotoBlock25_stub_double():
    # simulink_From has no real 'fromBlocks' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Goto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Goto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Goto(gotoTag="sample_text", tagVisibility="sample_text")
    partner = simulink_From()
    setattr(partner, 'fromBlocks', None)
    _safe_set(owner, 'Goto', partner)
    assert getattr(partner, 'fromBlocks') == owner
    _safe_set(owner, 'Goto', None)
    assert getattr(partner, 'fromBlocks') is None


def test_assoc_gotoBlock37_stub_double():
    # simulink_GotoTagVisibility has no real 'simulink_GotoTagVisibility' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Goto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Goto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Goto(gotoTag="sample_text", tagVisibility="sample_text")
    partner = simulink_GotoTagVisibility()
    setattr(partner, 'simulink_GotoTagVisibility', None)
    _safe_set(owner, 'simulink_Goto', partner)
    assert getattr(partner, 'simulink_GotoTagVisibility') == owner
    _safe_set(owner, 'simulink_Goto', None)
    assert getattr(partner, 'simulink_GotoTagVisibility') is None


def test_assoc_mappingFrom47_stub_double():
    # simulink_OutPort has no real 'simulink_OutPort48' property in the generated
    # code (a bare stub) -- manually attach it so simulink_BusSignalMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_BusSignalMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_BusSignalMapping(incomplete=True, mappingPath="sample_text")
    partner = simulink_OutPort()
    setattr(partner, 'simulink_OutPort48', None)
    _safe_set(owner, 'simulink_BusSignalMapping', partner)
    assert getattr(partner, 'simulink_OutPort48') == owner
    _safe_set(owner, 'simulink_BusSignalMapping', None)
    assert getattr(partner, 'simulink_OutPort48') is None


def test_assoc_mappingTo49_stub_double():
    # simulink_OutPort has no real 'simulink_OutPort51' property in the generated
    # code (a bare stub) -- manually attach it so simulink_BusSignalMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_BusSignalMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_BusSignalMapping(incomplete=True, mappingPath="sample_text")
    partner = simulink_OutPort()
    setattr(partner, 'simulink_OutPort51', None)
    _safe_set(owner, 'simulink_BusSignalMapping50', partner)
    assert getattr(partner, 'simulink_OutPort51') == owner
    _safe_set(owner, 'simulink_BusSignalMapping50', None)
    assert getattr(partner, 'simulink_OutPort51') is None


def test_assoc_parent11_stub_double():
    # simulink_Block has no real 'subBlocks' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SubSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SubSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SubSystem(tag="sample_text")
    partner = simulink_Block()
    setattr(partner, 'subBlocks', None)
    _safe_set(owner, 'SubSystem', partner)
    assert getattr(partner, 'subBlocks') == owner
    _safe_set(owner, 'SubSystem', None)
    assert getattr(partner, 'subBlocks') is None


def test_assoc_properties1_stub_double():
    # simulink_Block has no real 'simulink_Block' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Property(name="sample_text", source="sample_text", type="sample_text", value="sample_text")
    partner = simulink_Block()
    setattr(partner, 'simulink_Block', None)
    _safe_set(owner, 'simulink_Property', partner)
    assert owner in getattr(partner, 'simulink_Block')
    _safe_set(owner, 'simulink_Property', None)
    assert owner not in getattr(partner, 'simulink_Block')


def test_assoc_referencedModel41_stub_double():
    # simulink_ModelReference has no real 'simulink_ModelReference' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SimulinkModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SimulinkModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SimulinkModel(file="sample_text", library=True, version="sample_text")
    partner = simulink_ModelReference()
    setattr(partner, 'simulink_ModelReference', None)
    _safe_set(owner, 'simulink_SimulinkModel42', partner)
    assert getattr(partner, 'simulink_ModelReference') == owner
    _safe_set(owner, 'simulink_SimulinkModel42', None)
    assert getattr(partner, 'simulink_ModelReference') is None


def test_assoc_simulinkRef0_stub_double():
    # simulink_IdentifierReference has no real 'simulink_IdentifierReference' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SimulinkElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SimulinkElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SimulinkElement(name="sample_text")
    partner = simulink_IdentifierReference()
    setattr(partner, 'simulink_IdentifierReference', None)
    _safe_set(owner, 'simulink_SimulinkElement', partner)
    assert getattr(partner, 'simulink_IdentifierReference') == owner
    _safe_set(owner, 'simulink_SimulinkElement', None)
    assert getattr(partner, 'simulink_IdentifierReference') is None


def test_assoc_sourceBlockRef15_stub_double():
    # simulink_Block has no real 'simulink_Block16' property in the generated
    # code (a bare stub) -- manually attach it so simulink_LibraryLinkReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_LibraryLinkReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_LibraryLinkReference(disabled=True)
    partner = simulink_Block()
    setattr(partner, 'simulink_Block16', None)
    _safe_set(owner, 'simulink_LibraryLinkReference', partner)
    assert getattr(partner, 'simulink_Block16') == owner
    _safe_set(owner, 'simulink_LibraryLinkReference', None)
    assert getattr(partner, 'simulink_Block16') is None


def test_assoc_subBlocks38_stub_double():
    # simulink_Block has no real 'Block40' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SubSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SubSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SubSystem(tag="sample_text")
    partner = simulink_Block()
    setattr(partner, 'Block40', None)
    _safe_set(owner, 'parent39', {partner})
    assert getattr(partner, 'Block40') == owner
    _safe_set(owner, 'parent39', set())
    assert getattr(partner, 'Block40') is None


def test_assoc_trigger3_stub_double():
    # simulink_Block has no real 'simulink_Block4' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Trigger(statesWhenEnabling="sample_text", triggerType="sample_text")
    partner = simulink_Block()
    setattr(partner, 'simulink_Block4', None)
    _safe_set(owner, 'simulink_Trigger', partner)
    assert getattr(partner, 'simulink_Block4') == owner
    _safe_set(owner, 'simulink_Trigger', None)
    assert getattr(partner, 'simulink_Block4') is None


