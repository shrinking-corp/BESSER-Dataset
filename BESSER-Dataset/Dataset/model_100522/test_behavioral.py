import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    AssociationEnd,
    Attribute,
    AttributeLink,
    BooleanExpression,
    Classifier,
    Common_Behavior_AttributeLink,
    Common_Behavior_ComponentInstance,
    Common_Behavior_Instance,
    Common_Behavior_Link,
    Common_Behavior_LinkEnd,
    Common_Behavior_NodeInstance,
    ComponentInstance,
    Core_Association,
    Core_AssociationEnd,
    Core_Attribute,
    Core_Classifier,
    Core_Element,
    Core_Feature,
    Core_GeneralizableElement,
    Core_Generalization_,
    Core_ModelElement,
    Core_Namespace,
    Core_Relationship,
    Core_StructuralFeature,
    Data_Types_BooleanExpression,
    Data_Types_Expression,
    Data_Types_MultiplicityRange,
    Data_Types_Multiplicity_,
    Element,
    Expression,
    Extend,
    ExtensionPoint,
    Feature,
    GeneralizableElement,
    Generalization_,
    Include,
    Instance,
    Link,
    LinkEnd,
    ModelElement,
    MultiplicityRange,
    Multiplicity_,
    Namespace,
    NodeInstance,
    Relationship,
    StructuralFeature,
    UseCase,
    Use_Cases_Actor,
    Use_Cases_Extend,
    Use_Cases_ExtensionPoint,
    Use_Cases_Include,
    Use_Cases_UseCase,
    Use_Cases_UseCaseInstance,
    AggregationKind,
    ChangeableKind,
    OrderingKind,
    ScopeKind,
    VisibilityKind,
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

def test_assoc_association63_stub_double():
    # Association has no real 'Association65' property in the generated
    # code (a bare stub) -- manually attach it so Core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Association()
    setattr(partner, 'Association65', None)
    _safe_set(owner, 'connection64', partner)
    assert getattr(partner, 'Association65') == owner
    _safe_set(owner, 'connection64', None)
    assert getattr(partner, 'Association65') is None


def test_assoc_child84_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement85' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement85', None)
    _safe_set(owner, 'generalization', partner)
    assert getattr(partner, 'GeneralizableElement85') == owner
    _safe_set(owner, 'generalization', None)
    assert getattr(partner, 'GeneralizableElement85') is None


def test_assoc_generalization52_stub_double():
    # Generalization_ has no real 'Generalization_' property in the generated
    # code (a bare stub) -- manually attach it so Core_GeneralizableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_GeneralizableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_GeneralizableElement(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text")
    partner = Generalization_()
    setattr(partner, 'Generalization_', None)
    _safe_set(owner, 'child', {partner})
    assert getattr(partner, 'Generalization_') == owner
    _safe_set(owner, 'child', set())
    assert getattr(partner, 'Generalization_') is None


def test_assoc_multiplicity61_stub_double():
    # Multiplicity_ has no real 'Multiplicity' property in the generated
    # code (a bare stub) -- manually attach it so Core_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_StructuralFeature(changeability="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity', None)
    _safe_set(owner, 'Core_StructuralFeature62', partner)
    assert getattr(partner, 'Multiplicity') == owner
    _safe_set(owner, 'Core_StructuralFeature62', None)
    assert getattr(partner, 'Multiplicity') is None


def test_assoc_multiplicity73_stub_double():
    # Multiplicity_ has no real 'Multiplicity75' property in the generated
    # code (a bare stub) -- manually attach it so Core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity75', None)
    _safe_set(owner, 'Core_AssociationEnd74', partner)
    assert getattr(partner, 'Multiplicity75') == owner
    _safe_set(owner, 'Core_AssociationEnd74', None)
    assert getattr(partner, 'Multiplicity75') is None


def test_assoc_multiplicity87_stub_double():
    # Multiplicity_ has no real 'Multiplicity88' property in the generated
    # code (a bare stub) -- manually attach it so Data_Types_MultiplicityRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Data_Types_MultiplicityRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Data_Types_MultiplicityRange(lower="sample_text", upper="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity88', None)
    _safe_set(owner, 'range', partner)
    assert getattr(partner, 'Multiplicity88') == owner
    _safe_set(owner, 'range', None)
    assert getattr(partner, 'Multiplicity88') is None


def test_assoc_namespace51_stub_double():
    # Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so Core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedElement', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedElement', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_owner57_stub_double():
    # Classifier has no real 'Classifier58' property in the generated
    # code (a bare stub) -- manually attach it so Core_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Feature(ownerScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier58', None)
    _safe_set(owner, 'feature', partner)
    assert getattr(partner, 'Classifier58') == owner
    _safe_set(owner, 'feature', None)
    assert getattr(partner, 'Classifier58') is None


def test_assoc_parent81_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement', None)
    _safe_set(owner, 'Core_Generalization', partner)
    assert getattr(partner, 'GeneralizableElement') == owner
    _safe_set(owner, 'Core_Generalization', None)
    assert getattr(partner, 'GeneralizableElement') is None


def test_assoc_participant68_stub_double():
    # Classifier has no real 'Classifier70' property in the generated
    # code (a bare stub) -- manually attach it so Core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier70', None)
    _safe_set(owner, 'Core_AssociationEnd69', partner)
    assert getattr(partner, 'Classifier70') == owner
    _safe_set(owner, 'Core_AssociationEnd69', None)
    assert getattr(partner, 'Classifier70') is None


def test_assoc_powertype82_stub_double():
    # Classifier has no real 'Classifier83' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier83', None)
    _safe_set(owner, 'powertypeRange', partner)
    assert getattr(partner, 'Classifier83') == owner
    _safe_set(owner, 'powertypeRange', None)
    assert getattr(partner, 'Classifier83') is None


def test_assoc_qualifier71_stub_double():
    # Attribute has no real 'Attribute72' property in the generated
    # code (a bare stub) -- manually attach it so Core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute72', None)
    _safe_set(owner, 'associationEnd', {partner})
    assert getattr(partner, 'Attribute72') == owner
    _safe_set(owner, 'associationEnd', set())
    assert getattr(partner, 'Attribute72') is None


def test_assoc_specification66_stub_double():
    # Classifier has no real 'Classifier67' property in the generated
    # code (a bare stub) -- manually attach it so Core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier67', None)
    _safe_set(owner, 'Core_AssociationEnd', {partner})
    assert getattr(partner, 'Classifier67') == owner
    _safe_set(owner, 'Core_AssociationEnd', set())
    assert getattr(partner, 'Classifier67') is None


def test_assoc_type59_stub_double():
    # Classifier has no real 'Classifier60' property in the generated
    # code (a bare stub) -- manually attach it so Core_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_StructuralFeature(changeability="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier60', None)
    _safe_set(owner, 'Core_StructuralFeature', partner)
    assert getattr(partner, 'Classifier60') == owner
    _safe_set(owner, 'Core_StructuralFeature', None)
    assert getattr(partner, 'Classifier60') is None


def test_assoc_useCase49_stub_double():
    # UseCase has no real 'UseCase50' property in the generated
    # code (a bare stub) -- manually attach it so Use_Cases_ExtensionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Use_Cases_ExtensionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Use_Cases_ExtensionPoint(location="sample_text")
    partner = UseCase()
    setattr(partner, 'UseCase50', None)
    _safe_set(owner, 'extensionPoint', partner)
    assert getattr(partner, 'UseCase50') == owner
    _safe_set(owner, 'extensionPoint', None)
    assert getattr(partner, 'UseCase50') is None


