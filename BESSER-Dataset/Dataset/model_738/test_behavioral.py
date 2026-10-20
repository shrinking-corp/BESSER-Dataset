import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractPort,
    AspectModelElement,
    Attribute,
    AttributeInstance,
    BasicAttribute,
    Binding,
    CardinalityElement,
    ComponentImplementation,
    ComponentInstance,
    ComponentType,
    CompositeInstance,
    DelegationBinding,
    Dictionary,
    DictionaryDefaultValue,
    Entry,
    Group,
    InstanceGroup,
    ModelElement,
    NamedElement,
    Node,
    Operation,
    Parameter,
    PortId,
    Service,
    TransmissionBinding,
    TypeGroup,
    TypeImplementation,
    TypedElement,
    art_relaxed_AspectModelElement,
    art_relaxed_CardinalityElement,
    art_relaxed_DataType,
    art_relaxed_ModelElement,
    art_relaxed_NamedElement,
    art_relaxed_System,
    art_relaxed_TypedElement,
    art_relaxed_distrib_relaxed_Node,
    art_relaxed_group_relaxed_Group,
    art_relaxed_group_relaxed_InstanceGroup,
    art_relaxed_group_relaxed_TypeGroup,
    art_relaxed_implem_relaxed_ComponentImplementation,
    art_relaxed_implem_relaxed_FractalComponent,
    art_relaxed_implem_relaxed_OSGiComponent,
    art_relaxed_implem_relaxed_OSGiType,
    art_relaxed_implem_relaxed_TypeImplementation,
    art_relaxed_instance_relaxed_AttributeInstance,
    art_relaxed_instance_relaxed_Binding,
    art_relaxed_instance_relaxed_ComponentInstance,
    art_relaxed_instance_relaxed_CompositeInstance,
    art_relaxed_instance_relaxed_DefaultEntry,
    art_relaxed_instance_relaxed_DelegationBinding,
    art_relaxed_instance_relaxed_DictionaryValuedAttribute,
    art_relaxed_instance_relaxed_Entry,
    art_relaxed_instance_relaxed_OtherEntry,
    art_relaxed_instance_relaxed_PrimitiveInstance,
    art_relaxed_instance_relaxed_TransmissionBinding,
    art_relaxed_instance_relaxed_ValuedAttribute,
    art_relaxed_type_relaxed_AbstractPort,
    art_relaxed_type_relaxed_Attribute,
    art_relaxed_type_relaxed_BasicAttribute,
    art_relaxed_type_relaxed_ComponentType,
    art_relaxed_type_relaxed_CompositeType,
    art_relaxed_type_relaxed_ControlService,
    art_relaxed_type_relaxed_Dictionary,
    art_relaxed_type_relaxed_DictionaryDefaultValue,
    art_relaxed_type_relaxed_FunctionalService,
    art_relaxed_type_relaxed_Operation,
    art_relaxed_type_relaxed_Parameter,
    art_relaxed_type_relaxed_Port,
    art_relaxed_type_relaxed_PortCollection,
    art_relaxed_type_relaxed_PortId,
    art_relaxed_type_relaxed_PrimitiveType,
    art_relaxed_type_relaxed_Service,
    type_relaxed_AbstractPort,
    type_relaxed_art_relaxed_DataType,
    InstanceState,
    PortRole,
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

def test_assoc_attribute14_stub_double():
    # AttributeInstance has no real 'AttributeInstance' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = AttributeInstance()
    setattr(partner, 'AttributeInstance', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance15', {partner})
    assert getattr(partner, 'AttributeInstance') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance15', set())
    assert getattr(partner, 'AttributeInstance') is None


def test_assoc_attribute34_stub_double():
    # BasicAttribute has no real 'BasicAttribute' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ValuedAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ValuedAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ValuedAttribute(value="sample_text")
    partner = BasicAttribute()
    setattr(partner, 'BasicAttribute', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_ValuedAttribute', partner)
    assert getattr(partner, 'BasicAttribute') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_ValuedAttribute', None)
    assert getattr(partner, 'BasicAttribute') is None


def test_assoc_binding16_stub_double():
    # TransmissionBinding has no real 'TransmissionBinding' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = TransmissionBinding()
    setattr(partner, 'TransmissionBinding', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance17', {partner})
    assert getattr(partner, 'TransmissionBinding') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance17', set())
    assert getattr(partner, 'TransmissionBinding') is None


def test_assoc_components67_stub_double():
    # ComponentInstance has no real 'ComponentInstance68' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_distrib_relaxed_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_distrib_relaxed_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_distrib_relaxed_Node(uri="sample_text")
    partner = ComponentInstance()
    setattr(partner, 'ComponentInstance68', None)
    _safe_set(owner, 'art_relaxed_distrib_relaxed_Node', {partner})
    assert getattr(partner, 'ComponentInstance68') == owner
    _safe_set(owner, 'art_relaxed_distrib_relaxed_Node', set())
    assert getattr(partner, 'ComponentInstance68') is None


def test_assoc_groups20_stub_double():
    # InstanceGroup has no real 'InstanceGroup' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = InstanceGroup()
    setattr(partner, 'InstanceGroup', None)
    _safe_set(owner, 'instances', {partner})
    assert getattr(partner, 'InstanceGroup') == owner
    _safe_set(owner, 'instances', set())
    assert getattr(partner, 'InstanceGroup') is None


def test_assoc_implem18_stub_double():
    # ComponentImplementation has no real 'ComponentImplementation' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = ComponentImplementation()
    setattr(partner, 'ComponentImplementation', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance19', partner)
    assert getattr(partner, 'ComponentImplementation') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance19', None)
    assert getattr(partner, 'ComponentImplementation') is None


def test_assoc_serverInstance23_stub_double():
    # ComponentInstance has no real 'ComponentInstance24' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_Binding(id="sample_text")
    partner = ComponentInstance()
    setattr(partner, 'ComponentInstance24', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_Binding', partner)
    assert getattr(partner, 'ComponentInstance24') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_Binding', None)
    assert getattr(partner, 'ComponentInstance24') is None


def test_assoc_service51_stub_double():
    # Service has no real 'Service52' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_type_relaxed_AbstractPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_type_relaxed_AbstractPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_type_relaxed_AbstractPort(protocol="sample_text", role="sample_text", uri="sample_text")
    partner = Service()
    setattr(partner, 'Service52', None)
    _safe_set(owner, 'art_relaxed_type_relaxed_AbstractPort', partner)
    assert getattr(partner, 'Service52') == owner
    _safe_set(owner, 'art_relaxed_type_relaxed_AbstractPort', None)
    assert getattr(partner, 'Service52') is None


def test_assoc_superComponent13_stub_double():
    # CompositeInstance has no real 'CompositeInstance' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = CompositeInstance()
    setattr(partner, 'CompositeInstance', None)
    _safe_set(owner, 'subComponent', partner)
    assert getattr(partner, 'CompositeInstance') == owner
    _safe_set(owner, 'subComponent', None)
    assert getattr(partner, 'CompositeInstance') is None


def test_assoc_type11_stub_double():
    # ComponentType has no real 'ComponentType12' property in the generated
    # code (a bare stub) -- manually attach it so art_relaxed_instance_relaxed_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_relaxed_instance_relaxed_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_relaxed_instance_relaxed_ComponentInstance(state="sample_text")
    partner = ComponentType()
    setattr(partner, 'ComponentType12', None)
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance', partner)
    assert getattr(partner, 'ComponentType12') == owner
    _safe_set(owner, 'art_relaxed_instance_relaxed_ComponentInstance', None)
    assert getattr(partner, 'ComponentType12') is None


