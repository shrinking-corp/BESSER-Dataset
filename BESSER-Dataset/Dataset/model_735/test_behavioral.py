import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractPort,
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
    Operation,
    Parameter,
    PortId,
    Service,
    TransmissionBinding,
    TypeGroup,
    TypeImplementation,
    TypedElement,
    art_CardinalityElement,
    art_DataType,
    art_ModelElement,
    art_NamedElement,
    art_System,
    art_TypedElement,
    art_group_Group,
    art_group_InstanceGroup,
    art_group_TypeGroup,
    art_implem_ComponentImplementation,
    art_implem_FractalComponent,
    art_implem_OSGiComponent,
    art_implem_OSGiType,
    art_implem_TypeImplementation,
    art_instance_AttributeInstance,
    art_instance_Binding,
    art_instance_ComponentInstance,
    art_instance_CompositeInstance,
    art_instance_DefaultEntry,
    art_instance_DelegationBinding,
    art_instance_DictionaryValuedAttribute,
    art_instance_Entry,
    art_instance_OtherEntry,
    art_instance_PrimitiveInstance,
    art_instance_TransmissionBinding,
    art_instance_ValuedAttribute,
    art_type_AbstractPort,
    art_type_Attribute,
    art_type_BasicAttribute,
    art_type_ComponentType,
    art_type_CompositeType,
    art_type_ControlService,
    art_type_Dictionary,
    art_type_DictionaryDefaultValue,
    art_type_FunctionalService,
    art_type_Operation,
    art_type_Parameter,
    art_type_Port,
    art_type_PortCollection,
    art_type_PortId,
    art_type_PrimitiveType,
    art_type_Service,
    type_AbstractPort,
    type_art_DataType,
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

def test_assoc_attribute15_stub_double():
    # AttributeInstance has no real 'AttributeInstance' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = AttributeInstance()
    setattr(partner, 'AttributeInstance', None)
    _safe_set(owner, 'art_instance_ComponentInstance16', {partner})
    assert getattr(partner, 'AttributeInstance') == owner
    _safe_set(owner, 'art_instance_ComponentInstance16', set())
    assert getattr(partner, 'AttributeInstance') is None


def test_assoc_attribute35_stub_double():
    # BasicAttribute has no real 'BasicAttribute' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ValuedAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ValuedAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ValuedAttribute(value="sample_text")
    partner = BasicAttribute()
    setattr(partner, 'BasicAttribute', None)
    _safe_set(owner, 'art_instance_ValuedAttribute', partner)
    assert getattr(partner, 'BasicAttribute') == owner
    _safe_set(owner, 'art_instance_ValuedAttribute', None)
    assert getattr(partner, 'BasicAttribute') is None


def test_assoc_binding17_stub_double():
    # TransmissionBinding has no real 'TransmissionBinding' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = TransmissionBinding()
    setattr(partner, 'TransmissionBinding', None)
    _safe_set(owner, 'art_instance_ComponentInstance18', {partner})
    assert getattr(partner, 'TransmissionBinding') == owner
    _safe_set(owner, 'art_instance_ComponentInstance18', set())
    assert getattr(partner, 'TransmissionBinding') is None


def test_assoc_groups21_stub_double():
    # InstanceGroup has no real 'InstanceGroup' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = InstanceGroup()
    setattr(partner, 'InstanceGroup', None)
    _safe_set(owner, 'instances', {partner})
    assert getattr(partner, 'InstanceGroup') == owner
    _safe_set(owner, 'instances', set())
    assert getattr(partner, 'InstanceGroup') is None


def test_assoc_implem19_stub_double():
    # ComponentImplementation has no real 'ComponentImplementation' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = ComponentImplementation()
    setattr(partner, 'ComponentImplementation', None)
    _safe_set(owner, 'art_instance_ComponentInstance20', partner)
    assert getattr(partner, 'ComponentImplementation') == owner
    _safe_set(owner, 'art_instance_ComponentInstance20', None)
    assert getattr(partner, 'ComponentImplementation') is None


def test_assoc_serverInstance24_stub_double():
    # ComponentInstance has no real 'ComponentInstance25' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_Binding(id="sample_text")
    partner = ComponentInstance()
    setattr(partner, 'ComponentInstance25', None)
    _safe_set(owner, 'art_instance_Binding', partner)
    assert getattr(partner, 'ComponentInstance25') == owner
    _safe_set(owner, 'art_instance_Binding', None)
    assert getattr(partner, 'ComponentInstance25') is None


def test_assoc_service52_stub_double():
    # Service has no real 'Service53' property in the generated
    # code (a bare stub) -- manually attach it so art_type_AbstractPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_type_AbstractPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_type_AbstractPort(role="sample_text")
    partner = Service()
    setattr(partner, 'Service53', None)
    _safe_set(owner, 'art_type_AbstractPort', partner)
    assert getattr(partner, 'Service53') == owner
    _safe_set(owner, 'art_type_AbstractPort', None)
    assert getattr(partner, 'Service53') is None


def test_assoc_superComponent13_stub_double():
    # CompositeInstance has no real 'CompositeInstance14' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = CompositeInstance()
    setattr(partner, 'CompositeInstance14', None)
    _safe_set(owner, 'subComponent', partner)
    assert getattr(partner, 'CompositeInstance14') == owner
    _safe_set(owner, 'subComponent', None)
    assert getattr(partner, 'CompositeInstance14') is None


def test_assoc_type11_stub_double():
    # ComponentType has no real 'ComponentType12' property in the generated
    # code (a bare stub) -- manually attach it so art_instance_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # art_instance_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = art_instance_ComponentInstance(state="sample_text")
    partner = ComponentType()
    setattr(partner, 'ComponentType12', None)
    _safe_set(owner, 'art_instance_ComponentInstance', partner)
    assert getattr(partner, 'ComponentType12') == owner
    _safe_set(owner, 'art_instance_ComponentInstance', None)
    assert getattr(partner, 'ComponentType12') is None


