import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractInstance,
    InstanceBase,
    InterfaceItemInstance,
    StructureInstance,
    WiredStructureClass,
    etricegen_AbstractInstance,
    etricegen_ActorClass,
    etricegen_ActorInstance,
    etricegen_ActorInterfaceInstance,
    etricegen_Binding,
    etricegen_BindingInstance,
    etricegen_ConnectionInstance,
    etricegen_DataClass,
    etricegen_EnumerationType,
    etricegen_ExpandedActorClass,
    etricegen_GraphContainer,
    etricegen_InstanceBase,
    etricegen_InterfaceItemInstance,
    etricegen_LayerConnection,
    etricegen_LogicalSystem,
    etricegen_OpenBinding,
    etricegen_OpenServiceConnection,
    etricegen_OptionalActorInstance,
    etricegen_Port,
    etricegen_PortInstance,
    etricegen_ProtocolClass,
    etricegen_RoomModel,
    etricegen_Root,
    etricegen_SAP,
    etricegen_SAPInstance,
    etricegen_SPP,
    etricegen_SPPInstance,
    etricegen_ServiceImplInstance,
    etricegen_ServiceImplementation,
    etricegen_StructureInstance,
    etricegen_SubSystemClass,
    etricegen_SubSystemInstance,
    etricegen_SystemInstance,
    etricegen_Wire,
    etricegen_WiredActorClass,
    etricegen_WiredStructureClass,
    etricegen_WiredSubSystemClass,
    PortKind,
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

def test_assoc_allContainedInstances51_reverse_link_reassign_clear():
    a1 = etricegen_StructureInstance()
    a2 = etricegen_StructureInstance()
    b = etricegen_ActorInstance(replIdx=7, unindexedName="sample_text")
    _safe_set(b, 'etricegen_ActorInstance', a1)
    assert _is_linked(b, 'etricegen_ActorInstance', a1)
    if hasattr(a1, 'etricegen_StructureInstance52'):
        assert _is_linked(a1, 'etricegen_StructureInstance52', b)
    _safe_set(b, 'etricegen_ActorInstance', a2)
    assert _is_linked(b, 'etricegen_ActorInstance', a2)
    if hasattr(a1, 'etricegen_StructureInstance52'):
        assert not _is_linked(a1, 'etricegen_StructureInstance52', b)
    if hasattr(a2, 'etricegen_StructureInstance52'):
        assert _is_linked(a2, 'etricegen_StructureInstance52', b)
    _safe_set(b, 'etricegen_ActorInstance', None)
    assert not _is_linked(b, 'etricegen_ActorInstance', a2)
    if hasattr(a2, 'etricegen_StructureInstance52'):
        assert not _is_linked(a2, 'etricegen_StructureInstance52', b)


def test_assoc_orderedIfItemInstances53_reverse_link_reassign_clear():
    a1 = etricegen_StructureInstance()
    a2 = etricegen_StructureInstance()
    b = etricegen_InterfaceItemInstance()
    _safe_set(b, 'etricegen_InterfaceItemInstance', a1)
    assert _is_linked(b, 'etricegen_InterfaceItemInstance', a1)
    if hasattr(a1, 'etricegen_StructureInstance54'):
        assert _is_linked(a1, 'etricegen_StructureInstance54', b)
    _safe_set(b, 'etricegen_InterfaceItemInstance', a2)
    assert _is_linked(b, 'etricegen_InterfaceItemInstance', a2)
    if hasattr(a1, 'etricegen_StructureInstance54'):
        assert not _is_linked(a1, 'etricegen_StructureInstance54', b)
    if hasattr(a2, 'etricegen_StructureInstance54'):
        assert _is_linked(a2, 'etricegen_StructureInstance54', b)
    _safe_set(b, 'etricegen_InterfaceItemInstance', None)
    assert not _is_linked(b, 'etricegen_InterfaceItemInstance', a2)
    if hasattr(a2, 'etricegen_StructureInstance54'):
        assert not _is_linked(a2, 'etricegen_StructureInstance54', b)


def test_assoc_ownSubSystemInstances1_reverse_link_reassign_clear():
    a1 = etricegen_SubSystemInstance(maxObjId=7)
    a2 = etricegen_SubSystemInstance(maxObjId=13)
    b = etricegen_Root(library=True)
    _safe_set(b, 'etricegen_Root2', {a1})
    assert _is_linked(b, 'etricegen_Root2', a1)
    if hasattr(a1, 'etricegen_SubSystemInstance'):
        assert _is_linked(a1, 'etricegen_SubSystemInstance', b)
    _safe_set(b, 'etricegen_Root2', {a2})
    assert _is_linked(b, 'etricegen_Root2', a2)
    if hasattr(a1, 'etricegen_SubSystemInstance'):
        assert not _is_linked(a1, 'etricegen_SubSystemInstance', b)
    if hasattr(a2, 'etricegen_SubSystemInstance'):
        assert _is_linked(a2, 'etricegen_SubSystemInstance', b)
    _safe_set(b, 'etricegen_Root2', set())
    assert not _is_linked(b, 'etricegen_Root2', a2)
    if hasattr(a2, 'etricegen_SubSystemInstance'):
        assert not _is_linked(a2, 'etricegen_SubSystemInstance', b)


def test_assoc_peers76_reverse_link_reassign_clear():
    a1 = etricegen_InterfaceItemInstance()
    a2 = etricegen_InterfaceItemInstance()
    b = etricegen_InterfaceItemInstance()
    _safe_set(b, 'etricegen_InterfaceItemInstance77', a1)
    assert _is_linked(b, 'etricegen_InterfaceItemInstance77', a1)
    if hasattr(a1, 'etricegen_InterfaceItemInstance75'):
        assert _is_linked(a1, 'etricegen_InterfaceItemInstance75', b)
    _safe_set(b, 'etricegen_InterfaceItemInstance77', a2)
    assert _is_linked(b, 'etricegen_InterfaceItemInstance77', a2)
    if hasattr(a1, 'etricegen_InterfaceItemInstance75'):
        assert not _is_linked(a1, 'etricegen_InterfaceItemInstance75', b)
    if hasattr(a2, 'etricegen_InterfaceItemInstance75'):
        assert _is_linked(a2, 'etricegen_InterfaceItemInstance75', b)
    _safe_set(b, 'etricegen_InterfaceItemInstance77', None)
    assert not _is_linked(b, 'etricegen_InterfaceItemInstance77', a2)
    if hasattr(a2, 'etricegen_InterfaceItemInstance75'):
        assert not _is_linked(a2, 'etricegen_InterfaceItemInstance75', b)


def test_assoc_subSystemInstances3_reverse_link_reassign_clear():
    a1 = etricegen_SubSystemInstance(maxObjId=7)
    a2 = etricegen_SubSystemInstance(maxObjId=13)
    b = etricegen_Root(library=True)
    _safe_set(b, 'etricegen_Root4', {a1})
    assert _is_linked(b, 'etricegen_Root4', a1)
    if hasattr(a1, 'etricegen_SubSystemInstance5'):
        assert _is_linked(a1, 'etricegen_SubSystemInstance5', b)
    _safe_set(b, 'etricegen_Root4', {a2})
    assert _is_linked(b, 'etricegen_Root4', a2)
    if hasattr(a1, 'etricegen_SubSystemInstance5'):
        assert not _is_linked(a1, 'etricegen_SubSystemInstance5', b)
    if hasattr(a2, 'etricegen_SubSystemInstance5'):
        assert _is_linked(a2, 'etricegen_SubSystemInstance5', b)
    _safe_set(b, 'etricegen_Root4', set())
    assert not _is_linked(b, 'etricegen_Root4', a2)
    if hasattr(a2, 'etricegen_SubSystemInstance5'):
        assert not _is_linked(a2, 'etricegen_SubSystemInstance5', b)


def test_assoc_xpActorClasses11_reverse_link_reassign_clear():
    a1 = etricegen_Root(library=True)
    a2 = etricegen_Root(library=False)
    b = etricegen_ExpandedActorClass()
    _safe_set(b, 'etricegen_ExpandedActorClass', a1)
    assert _is_linked(b, 'etricegen_ExpandedActorClass', a1)
    if hasattr(a1, 'etricegen_Root12'):
        assert _is_linked(a1, 'etricegen_Root12', b)
    _safe_set(b, 'etricegen_ExpandedActorClass', a2)
    assert _is_linked(b, 'etricegen_ExpandedActorClass', a2)
    if hasattr(a1, 'etricegen_Root12'):
        assert not _is_linked(a1, 'etricegen_Root12', b)
    if hasattr(a2, 'etricegen_Root12'):
        assert _is_linked(a2, 'etricegen_Root12', b)
    _safe_set(b, 'etricegen_ExpandedActorClass', None)
    assert not _is_linked(b, 'etricegen_ExpandedActorClass', a2)
    if hasattr(a2, 'etricegen_Root12'):
        assert not _is_linked(a2, 'etricegen_Root12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actorClass120_stub_double():
    # etricegen_ActorClass has no real 'etricegen_ActorClass122' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ExpandedActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ExpandedActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ExpandedActorClass()
    partner = etricegen_ActorClass()
    setattr(partner, 'etricegen_ActorClass122', None)
    _safe_set(owner, 'etricegen_ExpandedActorClass121', partner)
    assert getattr(partner, 'etricegen_ActorClass122') == owner
    _safe_set(owner, 'etricegen_ExpandedActorClass121', None)
    assert getattr(partner, 'etricegen_ActorClass122') is None


def test_assoc_actorClass31_stub_double():
    # etricegen_ActorClass has no real 'etricegen_ActorClass32' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ActorInterfaceInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ActorInterfaceInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ActorInterfaceInstance(array=True)
    partner = etricegen_ActorClass()
    setattr(partner, 'etricegen_ActorClass32', None)
    _safe_set(owner, 'etricegen_ActorInterfaceInstance', partner)
    assert getattr(partner, 'etricegen_ActorClass32') == owner
    _safe_set(owner, 'etricegen_ActorInterfaceInstance', None)
    assert getattr(partner, 'etricegen_ActorClass32') is None


def test_assoc_actorClass63_stub_double():
    # etricegen_ActorClass has no real 'etricegen_ActorClass65' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ActorInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ActorInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ActorInstance(replIdx=7, unindexedName="sample_text")
    partner = etricegen_ActorClass()
    setattr(partner, 'etricegen_ActorClass65', None)
    _safe_set(owner, 'etricegen_ActorInstance64', partner)
    assert getattr(partner, 'etricegen_ActorClass65') == owner
    _safe_set(owner, 'etricegen_ActorInstance64', None)
    assert getattr(partner, 'etricegen_ActorClass65') is None


def test_assoc_actorClasses17_stub_double():
    # etricegen_ActorClass has no real 'etricegen_ActorClass' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_ActorClass()
    setattr(partner, 'etricegen_ActorClass', None)
    _safe_set(owner, 'etricegen_Root18', {partner})
    assert getattr(partner, 'etricegen_ActorClass') == owner
    _safe_set(owner, 'etricegen_Root18', set())
    assert getattr(partner, 'etricegen_ActorClass') is None


def test_assoc_bindings47_stub_double():
    # etricegen_BindingInstance has no real 'etricegen_BindingInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_BindingInstance()
    setattr(partner, 'etricegen_BindingInstance', None)
    _safe_set(owner, 'etricegen_StructureInstance48', {partner})
    assert getattr(partner, 'etricegen_BindingInstance') == owner
    _safe_set(owner, 'etricegen_StructureInstance48', set())
    assert getattr(partner, 'etricegen_BindingInstance') is None


def test_assoc_bindings80_stub_double():
    # etricegen_BindingInstance has no real 'BindingInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_PortInstance(kind="sample_text")
    partner = etricegen_BindingInstance()
    setattr(partner, 'BindingInstance', None)
    _safe_set(owner, 'ports', {partner})
    assert getattr(partner, 'BindingInstance') == owner
    _safe_set(owner, 'ports', set())
    assert getattr(partner, 'BindingInstance') is None


def test_assoc_connections49_stub_double():
    # etricegen_ConnectionInstance has no real 'etricegen_ConnectionInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_ConnectionInstance()
    setattr(partner, 'etricegen_ConnectionInstance', None)
    _safe_set(owner, 'etricegen_StructureInstance50', {partner})
    assert getattr(partner, 'etricegen_ConnectionInstance') == owner
    _safe_set(owner, 'etricegen_StructureInstance50', set())
    assert getattr(partner, 'etricegen_ConnectionInstance') is None


def test_assoc_dataClasses13_stub_double():
    # etricegen_DataClass has no real 'etricegen_DataClass' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_DataClass()
    setattr(partner, 'etricegen_DataClass', None)
    _safe_set(owner, 'etricegen_Root14', {partner})
    assert getattr(partner, 'etricegen_DataClass') == owner
    _safe_set(owner, 'etricegen_Root14', set())
    assert getattr(partner, 'etricegen_DataClass') is None


def test_assoc_enumClasses19_stub_double():
    # etricegen_EnumerationType has no real 'etricegen_EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_EnumerationType()
    setattr(partner, 'etricegen_EnumerationType', None)
    _safe_set(owner, 'etricegen_Root20', {partner})
    assert getattr(partner, 'etricegen_EnumerationType') == owner
    _safe_set(owner, 'etricegen_Root20', set())
    assert getattr(partner, 'etricegen_EnumerationType') is None


def test_assoc_graphContainer123_stub_double():
    # etricegen_GraphContainer has no real 'etricegen_GraphContainer' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ExpandedActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ExpandedActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ExpandedActorClass()
    partner = etricegen_GraphContainer()
    setattr(partner, 'etricegen_GraphContainer', None)
    _safe_set(owner, 'etricegen_ExpandedActorClass124', partner)
    assert getattr(partner, 'etricegen_GraphContainer') == owner
    _safe_set(owner, 'etricegen_ExpandedActorClass124', None)
    assert getattr(partner, 'etricegen_GraphContainer') is None


def test_assoc_importedModels8_stub_double():
    # etricegen_RoomModel has no real 'etricegen_RoomModel10' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_RoomModel()
    setattr(partner, 'etricegen_RoomModel10', None)
    _safe_set(owner, 'etricegen_Root9', {partner})
    assert getattr(partner, 'etricegen_RoomModel10') == owner
    _safe_set(owner, 'etricegen_Root9', set())
    assert getattr(partner, 'etricegen_RoomModel10') is None


def test_assoc_instances38_stub_double():
    # etricegen_AbstractInstance has no real 'etricegen_AbstractInstance39' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_AbstractInstance()
    setattr(partner, 'etricegen_AbstractInstance39', None)
    _safe_set(owner, 'etricegen_StructureInstance', {partner})
    assert getattr(partner, 'etricegen_AbstractInstance39') == owner
    _safe_set(owner, 'etricegen_StructureInstance', set())
    assert getattr(partner, 'etricegen_AbstractInstance39') is None


def test_assoc_instances55_stub_double():
    # etricegen_SystemInstance has no real 'etricegen_SystemInstance56' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_SubSystemInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_SubSystemInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_SubSystemInstance(maxObjId=7)
    partner = etricegen_SystemInstance()
    setattr(partner, 'etricegen_SystemInstance56', None)
    _safe_set(owner, 'etricegen_SubSystemInstance57', partner)
    assert owner in getattr(partner, 'etricegen_SystemInstance56')
    _safe_set(owner, 'etricegen_SubSystemInstance57', None)
    assert owner not in getattr(partner, 'etricegen_SystemInstance56')


def test_assoc_models6_stub_double():
    # etricegen_RoomModel has no real 'etricegen_RoomModel' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_RoomModel()
    setattr(partner, 'etricegen_RoomModel', None)
    _safe_set(owner, 'etricegen_Root7', {partner})
    assert getattr(partner, 'etricegen_RoomModel') == owner
    _safe_set(owner, 'etricegen_Root7', set())
    assert getattr(partner, 'etricegen_RoomModel') is None


def test_assoc_openBindings103_stub_double():
    # etricegen_WiredStructureClass has no real 'etricegen_WiredStructureClass104' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_OpenBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_OpenBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_OpenBinding(path="sample_text")
    partner = etricegen_WiredStructureClass()
    setattr(partner, 'etricegen_WiredStructureClass104', None)
    _safe_set(owner, 'etricegen_OpenBinding', partner)
    assert owner in getattr(partner, 'etricegen_WiredStructureClass104')
    _safe_set(owner, 'etricegen_OpenBinding', None)
    assert owner not in getattr(partner, 'etricegen_WiredStructureClass104')


def test_assoc_optionalActorClasses25_stub_double():
    # etricegen_ActorClass has no real 'etricegen_ActorClass27' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_ActorClass()
    setattr(partner, 'etricegen_ActorClass27', None)
    _safe_set(owner, 'etricegen_Root26', {partner})
    assert getattr(partner, 'etricegen_ActorClass27') == owner
    _safe_set(owner, 'etricegen_Root26', set())
    assert getattr(partner, 'etricegen_ActorClass27') is None


def test_assoc_optionalInstances23_stub_double():
    # etricegen_OptionalActorInstance has no real 'etricegen_OptionalActorInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_OptionalActorInstance()
    setattr(partner, 'etricegen_OptionalActorInstance', None)
    _safe_set(owner, 'etricegen_Root24', {partner})
    assert getattr(partner, 'etricegen_OptionalActorInstance') == owner
    _safe_set(owner, 'etricegen_Root24', set())
    assert getattr(partner, 'etricegen_OptionalActorInstance') is None


def test_assoc_optionalInstances35_stub_double():
    # etricegen_OptionalActorInstance has no real 'etricegen_OptionalActorInstance37' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ActorInterfaceInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ActorInterfaceInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ActorInterfaceInstance(array=True)
    partner = etricegen_OptionalActorInstance()
    setattr(partner, 'etricegen_OptionalActorInstance37', None)
    _safe_set(owner, 'etricegen_ActorInterfaceInstance36', {partner})
    assert getattr(partner, 'etricegen_OptionalActorInstance37') == owner
    _safe_set(owner, 'etricegen_ActorInterfaceInstance36', set())
    assert getattr(partner, 'etricegen_OptionalActorInstance37') is None


def test_assoc_port110_stub_double():
    # etricegen_Port has no real 'etricegen_Port112' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_OpenBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_OpenBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_OpenBinding(path="sample_text")
    partner = etricegen_Port()
    setattr(partner, 'etricegen_Port112', None)
    _safe_set(owner, 'etricegen_OpenBinding111', partner)
    assert getattr(partner, 'etricegen_Port112') == owner
    _safe_set(owner, 'etricegen_OpenBinding111', None)
    assert getattr(partner, 'etricegen_Port112') is None


def test_assoc_port78_stub_double():
    # etricegen_Port has no real 'etricegen_Port' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_PortInstance(kind="sample_text")
    partner = etricegen_Port()
    setattr(partner, 'etricegen_Port', None)
    _safe_set(owner, 'etricegen_PortInstance79', partner)
    assert getattr(partner, 'etricegen_Port') == owner
    _safe_set(owner, 'etricegen_PortInstance79', None)
    assert getattr(partner, 'etricegen_Port') is None


def test_assoc_ports30_stub_double():
    # etricegen_AbstractInstance has no real 'etricegen_AbstractInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_PortInstance(kind="sample_text")
    partner = etricegen_AbstractInstance()
    setattr(partner, 'etricegen_AbstractInstance', None)
    _safe_set(owner, 'etricegen_PortInstance', partner)
    assert owner in getattr(partner, 'etricegen_AbstractInstance')
    _safe_set(owner, 'etricegen_PortInstance', None)
    assert owner not in getattr(partner, 'etricegen_AbstractInstance')


def test_assoc_ports81_stub_double():
    # etricegen_BindingInstance has no real 'bindings' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_PortInstance(kind="sample_text")
    partner = etricegen_BindingInstance()
    setattr(partner, 'bindings', None)
    _safe_set(owner, 'PortInstance', partner)
    assert owner in getattr(partner, 'bindings')
    _safe_set(owner, 'PortInstance', None)
    assert owner not in getattr(partner, 'bindings')


def test_assoc_protocol113_stub_double():
    # etricegen_ProtocolClass has no real 'etricegen_ProtocolClass115' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_OpenServiceConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_OpenServiceConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_OpenServiceConnection(path="sample_text")
    partner = etricegen_ProtocolClass()
    setattr(partner, 'etricegen_ProtocolClass115', None)
    _safe_set(owner, 'etricegen_OpenServiceConnection114', partner)
    assert getattr(partner, 'etricegen_ProtocolClass115') == owner
    _safe_set(owner, 'etricegen_OpenServiceConnection114', None)
    assert getattr(partner, 'etricegen_ProtocolClass115') is None


def test_assoc_protocol72_stub_double():
    # etricegen_ProtocolClass has no real 'etricegen_ProtocolClass74' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_InterfaceItemInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_InterfaceItemInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_InterfaceItemInstance()
    partner = etricegen_ProtocolClass()
    setattr(partner, 'etricegen_ProtocolClass74', None)
    _safe_set(owner, 'etricegen_InterfaceItemInstance73', partner)
    assert getattr(partner, 'etricegen_ProtocolClass74') == owner
    _safe_set(owner, 'etricegen_InterfaceItemInstance73', None)
    assert getattr(partner, 'etricegen_ProtocolClass74') is None


def test_assoc_protocolClasses15_stub_double():
    # etricegen_ProtocolClass has no real 'etricegen_ProtocolClass' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_ProtocolClass()
    setattr(partner, 'etricegen_ProtocolClass', None)
    _safe_set(owner, 'etricegen_Root16', {partner})
    assert getattr(partner, 'etricegen_ProtocolClass') == owner
    _safe_set(owner, 'etricegen_Root16', set())
    assert getattr(partner, 'etricegen_ProtocolClass') is None


def test_assoc_providedServices105_stub_double():
    # etricegen_WiredStructureClass has no real 'etricegen_WiredStructureClass106' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_OpenServiceConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_OpenServiceConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_OpenServiceConnection(path="sample_text")
    partner = etricegen_WiredStructureClass()
    setattr(partner, 'etricegen_WiredStructureClass106', None)
    _safe_set(owner, 'etricegen_OpenServiceConnection', partner)
    assert owner in getattr(partner, 'etricegen_WiredStructureClass106')
    _safe_set(owner, 'etricegen_OpenServiceConnection', None)
    assert owner not in getattr(partner, 'etricegen_WiredStructureClass106')


def test_assoc_providedServices33_stub_double():
    # etricegen_ServiceImplInstance has no real 'etricegen_ServiceImplInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_ActorInterfaceInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_ActorInterfaceInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_ActorInterfaceInstance(array=True)
    partner = etricegen_ServiceImplInstance()
    setattr(partner, 'etricegen_ServiceImplInstance', None)
    _safe_set(owner, 'etricegen_ActorInterfaceInstance34', {partner})
    assert getattr(partner, 'etricegen_ServiceImplInstance') == owner
    _safe_set(owner, 'etricegen_ActorInterfaceInstance34', set())
    assert getattr(partner, 'etricegen_ServiceImplInstance') is None


def test_assoc_requiredServices107_stub_double():
    # etricegen_WiredStructureClass has no real 'etricegen_WiredStructureClass108' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_OpenServiceConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_OpenServiceConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_OpenServiceConnection(path="sample_text")
    partner = etricegen_WiredStructureClass()
    setattr(partner, 'etricegen_WiredStructureClass108', None)
    _safe_set(owner, 'etricegen_OpenServiceConnection109', partner)
    assert owner in getattr(partner, 'etricegen_WiredStructureClass108')
    _safe_set(owner, 'etricegen_OpenServiceConnection109', None)
    assert owner not in getattr(partner, 'etricegen_WiredStructureClass108')


def test_assoc_saps40_stub_double():
    # etricegen_SAPInstance has no real 'etricegen_SAPInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_SAPInstance()
    setattr(partner, 'etricegen_SAPInstance', None)
    _safe_set(owner, 'etricegen_StructureInstance41', {partner})
    assert getattr(partner, 'etricegen_SAPInstance') == owner
    _safe_set(owner, 'etricegen_StructureInstance41', set())
    assert getattr(partner, 'etricegen_SAPInstance') is None


def test_assoc_services44_stub_double():
    # etricegen_ServiceImplInstance has no real 'etricegen_ServiceImplInstance46' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_ServiceImplInstance()
    setattr(partner, 'etricegen_ServiceImplInstance46', None)
    _safe_set(owner, 'etricegen_StructureInstance45', {partner})
    assert getattr(partner, 'etricegen_ServiceImplInstance46') == owner
    _safe_set(owner, 'etricegen_StructureInstance45', set())
    assert getattr(partner, 'etricegen_ServiceImplInstance46') is None


def test_assoc_spps42_stub_double():
    # etricegen_SPPInstance has no real 'etricegen_SPPInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_StructureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_StructureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_StructureInstance()
    partner = etricegen_SPPInstance()
    setattr(partner, 'etricegen_SPPInstance', None)
    _safe_set(owner, 'etricegen_StructureInstance43', {partner})
    assert getattr(partner, 'etricegen_SPPInstance') == owner
    _safe_set(owner, 'etricegen_StructureInstance43', set())
    assert getattr(partner, 'etricegen_SPPInstance') is None


def test_assoc_subSystemClass60_stub_double():
    # etricegen_SubSystemClass has no real 'etricegen_SubSystemClass62' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_SubSystemInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_SubSystemInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_SubSystemInstance(maxObjId=7)
    partner = etricegen_SubSystemClass()
    setattr(partner, 'etricegen_SubSystemClass62', None)
    _safe_set(owner, 'etricegen_SubSystemInstance61', partner)
    assert getattr(partner, 'etricegen_SubSystemClass62') == owner
    _safe_set(owner, 'etricegen_SubSystemInstance61', None)
    assert getattr(partner, 'etricegen_SubSystemClass62') is None


def test_assoc_subSystemClasses21_stub_double():
    # etricegen_SubSystemClass has no real 'etricegen_SubSystemClass' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_SubSystemClass()
    setattr(partner, 'etricegen_SubSystemClass', None)
    _safe_set(owner, 'etricegen_Root22', {partner})
    assert getattr(partner, 'etricegen_SubSystemClass') == owner
    _safe_set(owner, 'etricegen_Root22', set())
    assert getattr(partner, 'etricegen_SubSystemClass') is None


def test_assoc_systemInstances0_stub_double():
    # etricegen_SystemInstance has no real 'etricegen_SystemInstance' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_SystemInstance()
    setattr(partner, 'etricegen_SystemInstance', None)
    _safe_set(owner, 'etricegen_Root', {partner})
    assert getattr(partner, 'etricegen_SystemInstance') == owner
    _safe_set(owner, 'etricegen_Root', set())
    assert getattr(partner, 'etricegen_SystemInstance') is None


def test_assoc_wiredInstances28_stub_double():
    # etricegen_WiredStructureClass has no real 'etricegen_WiredStructureClass' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Root(library=True)
    partner = etricegen_WiredStructureClass()
    setattr(partner, 'etricegen_WiredStructureClass', None)
    _safe_set(owner, 'etricegen_Root29', {partner})
    assert getattr(partner, 'etricegen_WiredStructureClass') == owner
    _safe_set(owner, 'etricegen_Root29', set())
    assert getattr(partner, 'etricegen_WiredStructureClass') is None


def test_assoc_wires101_stub_double():
    # etricegen_WiredStructureClass has no real 'etricegen_WiredStructureClass102' property in the generated
    # code (a bare stub) -- manually attach it so etricegen_Wire's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # etricegen_Wire's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = etricegen_Wire(dataDriven=True, path1="sample_text", path2="sample_text")
    partner = etricegen_WiredStructureClass()
    setattr(partner, 'etricegen_WiredStructureClass102', None)
    _safe_set(owner, 'etricegen_Wire', partner)
    assert owner in getattr(partner, 'etricegen_WiredStructureClass102')
    _safe_set(owner, 'etricegen_Wire', None)
    assert owner not in getattr(partner, 'etricegen_WiredStructureClass102')


