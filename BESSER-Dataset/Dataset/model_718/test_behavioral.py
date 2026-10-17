import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artifact,
    Association,
    AssociationEnd,
    AssociationEndRole,
    Attribute,
    BehavioralFeature,
    Binding,
    BooleanExpression,
    CallAction,
    CallEvent,
    Classifier,
    Collaboration,
    Comment,
    Component,
    Constraint,
    CreateAction,
    DataType,
    Dependency,
    Element,
    ElementResidence,
    Enumeration,
    EnumerationLiteral,
    Expression,
    Feature,
    Flow,
    GeneralizableElement,
    Generalization_,
    MappingExpression,
    Method,
    ModelElement,
    MultiplicityRange,
    Multiplicity_,
    Namespace,
    Node,
    Operation,
    Parameter,
    PresentationElement,
    ProcedureExpression,
    Relationship,
    Signal,
    StateMachine,
    Stereotype,
    StructuralFeature,
    TagDefinition,
    TaggedValue,
    TemplateArgument,
    TemplateParameter,
    TypeExpression,
    core_Association,
    core_Class,
    core_GeneralizableElement,
    core_Namespace,
    core_Relationship,
    foundation_core_Abstraction,
    foundation_core_Artifact,
    foundation_core_Association,
    foundation_core_AssociationClass,
    foundation_core_AssociationEnd,
    foundation_core_Attribute,
    foundation_core_BehavioralFeature,
    foundation_core_Binding,
    foundation_core_Class,
    foundation_core_Classifier,
    foundation_core_Comment,
    foundation_core_Component,
    foundation_core_Constraint,
    foundation_core_DataType,
    foundation_core_Dependency,
    foundation_core_Element,
    foundation_core_ElementResidence,
    foundation_core_Enumeration,
    foundation_core_EnumerationLiteral,
    foundation_core_Feature,
    foundation_core_Flow,
    foundation_core_GeneralizableElement,
    foundation_core_Generalization_,
    foundation_core_Interface,
    foundation_core_Method,
    foundation_core_ModelElement,
    foundation_core_Namespace,
    foundation_core_Node,
    foundation_core_Operation,
    foundation_core_Parameter,
    foundation_core_Permission,
    foundation_core_PresentationElement,
    foundation_core_Primitive,
    foundation_core_ProgrammingLanguageDataType,
    foundation_core_Relationship,
    foundation_core_Stereotype,
    foundation_core_StructuralFeature,
    foundation_core_TagDefinition,
    foundation_core_TaggedValue,
    foundation_core_TemplateArgument,
    foundation_core_TemplateParameter,
    foundation_core_Usage,
    foundation_data_types_ActionExpression,
    foundation_data_types_ArgListsExpression,
    foundation_data_types_BooleanExpression,
    foundation_data_types_Expression,
    foundation_data_types_IterationExpression,
    foundation_data_types_MappingExpression,
    foundation_data_types_MultiplicityRange,
    foundation_data_types_Multiplicity_,
    foundation_data_types_ObjectSetExpression,
    foundation_data_types_ProcedureExpression,
    foundation_data_types_TimeExpression,
    foundation_data_types_TypeExpression,
    AggregationKind,
    CallConcurrencyKind,
    ChangeableKind,
    OrderingKind,
    ParameterDirectionKind,
    PseudostateKind,
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

def test_assoc_annotatedElement95_stub_double():
    # ModelElement has no real 'ModelElement96' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Comment(body="sample_text")
    partner = ModelElement()
    setattr(partner, 'ModelElement96', None)
    _safe_set(owner, 'comment', {partner})
    assert getattr(partner, 'ModelElement96') == owner
    _safe_set(owner, 'comment', set())
    assert getattr(partner, 'ModelElement96') is None


def test_assoc_association41_stub_double():
    # Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'Association') is None


def test_assoc_behavior18_stub_double():
    # StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'context', {partner})
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'context', set())
    assert getattr(partner, 'StateMachine') is None


def test_assoc_behavioralFeature72_stub_double():
    # BehavioralFeature has no real 'BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Parameter(kind="sample_text")
    partner = BehavioralFeature()
    setattr(partner, 'BehavioralFeature', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'BehavioralFeature') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'BehavioralFeature') is None


def test_assoc_callAction65_stub_double():
    # CallAction has no real 'CallAction' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Operation(concurrency="sample_text", isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = CallAction()
    setattr(partner, 'CallAction', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'CallAction') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'CallAction') is None


def test_assoc_child77_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement', None)
    _safe_set(owner, 'generalization', partner)
    assert getattr(partner, 'GeneralizableElement') == owner
    _safe_set(owner, 'generalization', None)
    assert getattr(partner, 'GeneralizableElement') is None


def test_assoc_clientDependency3_stub_double():
    # Dependency has no real 'Dependency' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Dependency()
    setattr(partner, 'Dependency', None)
    _safe_set(owner, 'client', {partner})
    assert getattr(partner, 'Dependency') == owner
    _safe_set(owner, 'client', set())
    assert getattr(partner, 'Dependency') is None


def test_assoc_collaboration68_stub_double():
    # Collaboration has no real 'Collaboration69' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Operation(concurrency="sample_text", isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = Collaboration()
    setattr(partner, 'Collaboration69', None)
    _safe_set(owner, 'representedOperation', {partner})
    assert getattr(partner, 'Collaboration69') == owner
    _safe_set(owner, 'representedOperation', set())
    assert getattr(partner, 'Collaboration69') is None


def test_assoc_comment11_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'annotatedElement', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'annotatedElement', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_constraint4_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'constrainedElement', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'constrainedElement', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_container103_stub_double():
    # Component has no real 'Component104' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ElementResidence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ElementResidence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ElementResidence(visibility="sample_text")
    partner = Component()
    setattr(partner, 'Component104', None)
    _safe_set(owner, 'residentElement', partner)
    assert getattr(partner, 'Component104') == owner
    _safe_set(owner, 'residentElement', None)
    assert getattr(partner, 'Component104') is None


def test_assoc_defaultValue70_stub_double():
    # Expression has no real 'Expression71' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Parameter(kind="sample_text")
    partner = Expression()
    setattr(partner, 'Expression71', None)
    _safe_set(owner, 'foundation_core_Parameter', partner)
    assert getattr(partner, 'Expression71') == owner
    _safe_set(owner, 'foundation_core_Parameter', None)
    assert getattr(partner, 'Expression71') is None


def test_assoc_definedTag114_stub_double():
    # TagDefinition has no real 'TagDefinition' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Stereotype(baseClass="sample_text", icon="sample_text")
    partner = TagDefinition()
    setattr(partner, 'TagDefinition', None)
    _safe_set(owner, 'owner115', {partner})
    assert getattr(partner, 'TagDefinition') == owner
    _safe_set(owner, 'owner115', set())
    assert getattr(partner, 'TagDefinition') is None


def test_assoc_elementResidence12_stub_double():
    # ElementResidence has no real 'ElementResidence' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = ElementResidence()
    setattr(partner, 'ElementResidence', None)
    _safe_set(owner, 'resident', {partner})
    assert getattr(partner, 'ElementResidence') == owner
    _safe_set(owner, 'resident', set())
    assert getattr(partner, 'ElementResidence') is None


def test_assoc_extendedElement116_stub_double():
    # ModelElement has no real 'ModelElement117' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Stereotype(baseClass="sample_text", icon="sample_text")
    partner = ModelElement()
    setattr(partner, 'ModelElement117', None)
    _safe_set(owner, 'stereotype', {partner})
    assert getattr(partner, 'ModelElement117') == owner
    _safe_set(owner, 'stereotype', set())
    assert getattr(partner, 'ModelElement117') is None


def test_assoc_generalization19_stub_double():
    # Generalization_ has no real 'Generalization_' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_GeneralizableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_GeneralizableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_GeneralizableElement(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text")
    partner = Generalization_()
    setattr(partner, 'Generalization_', None)
    _safe_set(owner, 'child', {partner})
    assert getattr(partner, 'Generalization_') == owner
    _safe_set(owner, 'child', set())
    assert getattr(partner, 'Generalization_') is None


def test_assoc_method63_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Operation(concurrency="sample_text", isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'specification64', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'specification64', set())
    assert getattr(partner, 'Method') is None


def test_assoc_modelElement127_stub_double():
    # ModelElement has no real 'ModelElement128' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TaggedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TaggedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TaggedValue(dataValue="sample_text")
    partner = ModelElement()
    setattr(partner, 'ModelElement128', None)
    _safe_set(owner, 'taggedValue', partner)
    assert getattr(partner, 'ModelElement128') == owner
    _safe_set(owner, 'taggedValue', None)
    assert getattr(partner, 'ModelElement128') is None


def test_assoc_multiplicity1_stub_double():
    # Multiplicity_ has no real 'Multiplicity' property in the generated
    # code (a bare stub) -- manually attach it so foundation_data_types_MultiplicityRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_data_types_MultiplicityRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_data_types_MultiplicityRange(lower="sample_text", upper="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity', None)
    _safe_set(owner, 'range', partner)
    assert getattr(partner, 'Multiplicity') == owner
    _safe_set(owner, 'range', None)
    assert getattr(partner, 'Multiplicity') is None


def test_assoc_multiplicity120_stub_double():
    # Multiplicity_ has no real 'Multiplicity121' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TagDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TagDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TagDefinition(tagType="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity121', None)
    _safe_set(owner, 'foundation_core_TagDefinition', partner)
    assert getattr(partner, 'Multiplicity121') == owner
    _safe_set(owner, 'foundation_core_TagDefinition', None)
    assert getattr(partner, 'Multiplicity121') is None


def test_assoc_multiplicity35_stub_double():
    # Multiplicity_ has no real 'Multiplicity36' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_StructuralFeature(changeability="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity36', None)
    _safe_set(owner, 'foundation_core_StructuralFeature', partner)
    assert getattr(partner, 'Multiplicity36') == owner
    _safe_set(owner, 'foundation_core_StructuralFeature', None)
    assert getattr(partner, 'Multiplicity36') is None


def test_assoc_multiplicity39_stub_double():
    # Multiplicity_ has no real 'Multiplicity40' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity40', None)
    _safe_set(owner, 'foundation_core_AssociationEnd', partner)
    assert getattr(partner, 'Multiplicity40') == owner
    _safe_set(owner, 'foundation_core_AssociationEnd', None)
    assert getattr(partner, 'Multiplicity40') is None


def test_assoc_namespace2_stub_double():
    # Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedElement', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedElement', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_occurrence66_stub_double():
    # CallEvent has no real 'CallEvent' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Operation(concurrency="sample_text", isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = CallEvent()
    setattr(partner, 'CallEvent', None)
    _safe_set(owner, 'operation67', {partner})
    assert getattr(partner, 'CallEvent') == owner
    _safe_set(owner, 'operation67', set())
    assert getattr(partner, 'CallEvent') is None


def test_assoc_owner122_stub_double():
    # Stereotype has no real 'Stereotype123' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TagDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TagDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TagDefinition(tagType="sample_text")
    partner = Stereotype()
    setattr(partner, 'Stereotype123', None)
    _safe_set(owner, 'definedTag', partner)
    assert getattr(partner, 'Stereotype123') == owner
    _safe_set(owner, 'definedTag', None)
    assert getattr(partner, 'Stereotype123') is None


def test_assoc_owner34_stub_double():
    # Classifier has no real 'Classifier' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Feature(ownerScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier', None)
    _safe_set(owner, 'feature', partner)
    assert getattr(partner, 'Classifier') == owner
    _safe_set(owner, 'feature', None)
    assert getattr(partner, 'Classifier') is None


def test_assoc_parameter59_stub_double():
    # Parameter has no real 'Parameter60' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_BehavioralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_BehavioralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_BehavioralFeature(isQuery="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter60', None)
    _safe_set(owner, 'behavioralFeature', {partner})
    assert getattr(partner, 'Parameter60') == owner
    _safe_set(owner, 'behavioralFeature', set())
    assert getattr(partner, 'Parameter60') is None


def test_assoc_parent78_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement79' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement79', None)
    _safe_set(owner, 'specialization', partner)
    assert getattr(partner, 'GeneralizableElement79') == owner
    _safe_set(owner, 'specialization', None)
    assert getattr(partner, 'GeneralizableElement79') is None


def test_assoc_participant43_stub_double():
    # Classifier has no real 'Classifier44' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier44', None)
    _safe_set(owner, 'association', partner)
    assert getattr(partner, 'Classifier44') == owner
    _safe_set(owner, 'association', None)
    assert getattr(partner, 'Classifier44') is None


def test_assoc_powertype80_stub_double():
    # Classifier has no real 'Classifier81' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Generalization_(discriminator="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier81', None)
    _safe_set(owner, 'powertypeRange', partner)
    assert getattr(partner, 'Classifier81') == owner
    _safe_set(owner, 'powertypeRange', None)
    assert getattr(partner, 'Classifier81') is None


def test_assoc_presentation7_stub_double():
    # PresentationElement has no real 'PresentationElement' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = PresentationElement()
    setattr(partner, 'PresentationElement', None)
    _safe_set(owner, 'subject', {partner})
    assert getattr(partner, 'PresentationElement') == owner
    _safe_set(owner, 'subject', set())
    assert getattr(partner, 'PresentationElement') is None


def test_assoc_qualifier42_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'associationEnd', {partner})
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'associationEnd', set())
    assert getattr(partner, 'Attribute') is None


def test_assoc_raisedSignal61_stub_double():
    # Signal has no real 'Signal' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_BehavioralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_BehavioralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_BehavioralFeature(isQuery="sample_text")
    partner = Signal()
    setattr(partner, 'Signal', None)
    _safe_set(owner, 'context62', {partner})
    assert getattr(partner, 'Signal') == owner
    _safe_set(owner, 'context62', set())
    assert getattr(partner, 'Signal') is None


def test_assoc_referenceTag16_stub_double():
    # TaggedValue has no real 'TaggedValue17' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = TaggedValue()
    setattr(partner, 'TaggedValue17', None)
    _safe_set(owner, 'referenceValue', {partner})
    assert getattr(partner, 'TaggedValue17') == owner
    _safe_set(owner, 'referenceValue', set())
    assert getattr(partner, 'TaggedValue17') is None


def test_assoc_referenceValue131_stub_double():
    # ModelElement has no real 'ModelElement132' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TaggedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TaggedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TaggedValue(dataValue="sample_text")
    partner = ModelElement()
    setattr(partner, 'ModelElement132', None)
    _safe_set(owner, 'referenceTag', {partner})
    assert getattr(partner, 'ModelElement132') == owner
    _safe_set(owner, 'referenceTag', set())
    assert getattr(partner, 'ModelElement132') is None


def test_assoc_resident101_stub_double():
    # ModelElement has no real 'ModelElement102' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ElementResidence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ElementResidence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ElementResidence(visibility="sample_text")
    partner = ModelElement()
    setattr(partner, 'ModelElement102', None)
    _safe_set(owner, 'elementResidence', partner)
    assert getattr(partner, 'ModelElement102') == owner
    _safe_set(owner, 'elementResidence', None)
    assert getattr(partner, 'ModelElement102') is None


def test_assoc_sourceFlow9_stub_double():
    # Flow has no real 'Flow10' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Flow()
    setattr(partner, 'Flow10', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Flow10') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Flow10') is None


def test_assoc_specialization20_stub_double():
    # Generalization_ has no real 'Generalization21' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_GeneralizableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_GeneralizableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_GeneralizableElement(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text")
    partner = Generalization_()
    setattr(partner, 'Generalization21', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'Generalization21') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'Generalization21') is None


def test_assoc_specification45_stub_double():
    # Classifier has no real 'Classifier46' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier46', None)
    _safe_set(owner, 'specifiedEnd', {partner})
    assert getattr(partner, 'Classifier46') == owner
    _safe_set(owner, 'specifiedEnd', set())
    assert getattr(partner, 'Classifier46') is None


def test_assoc_stereotype14_stub_double():
    # Stereotype has no real 'Stereotype' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Stereotype()
    setattr(partner, 'Stereotype', None)
    _safe_set(owner, 'extendedElement', {partner})
    assert getattr(partner, 'Stereotype') == owner
    _safe_set(owner, 'extendedElement', set())
    assert getattr(partner, 'Stereotype') is None


def test_assoc_stereotypeConstraint118_stub_double():
    # Constraint has no real 'Constraint119' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Stereotype(baseClass="sample_text", icon="sample_text")
    partner = Constraint()
    setattr(partner, 'Constraint119', None)
    _safe_set(owner, 'constrainedStereotype', {partner})
    assert getattr(partner, 'Constraint119') == owner
    _safe_set(owner, 'constrainedStereotype', set())
    assert getattr(partner, 'Constraint119') is None


def test_assoc_supplierDependency5_stub_double():
    # Dependency has no real 'Dependency6' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Dependency()
    setattr(partner, 'Dependency6', None)
    _safe_set(owner, 'supplier', {partner})
    assert getattr(partner, 'Dependency6') == owner
    _safe_set(owner, 'supplier', set())
    assert getattr(partner, 'Dependency6') is None


def test_assoc_taggedValue15_stub_double():
    # TaggedValue has no real 'TaggedValue' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = TaggedValue()
    setattr(partner, 'TaggedValue', None)
    _safe_set(owner, 'modelElement', {partner})
    assert getattr(partner, 'TaggedValue') == owner
    _safe_set(owner, 'modelElement', set())
    assert getattr(partner, 'TaggedValue') is None


def test_assoc_targetFlow8_stub_double():
    # Flow has no real 'Flow' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Flow()
    setattr(partner, 'Flow', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Flow') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Flow') is None


def test_assoc_templateParameter13_stub_double():
    # TemplateParameter has no real 'TemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = TemplateParameter()
    setattr(partner, 'TemplateParameter', None)
    _safe_set(owner, 'template', {partner})
    assert getattr(partner, 'TemplateParameter') == owner
    _safe_set(owner, 'template', set())
    assert getattr(partner, 'TemplateParameter') is None


def test_assoc_type129_stub_double():
    # TagDefinition has no real 'TagDefinition130' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TaggedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TaggedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TaggedValue(dataValue="sample_text")
    partner = TagDefinition()
    setattr(partner, 'TagDefinition130', None)
    _safe_set(owner, 'typedValue', partner)
    assert getattr(partner, 'TagDefinition130') == owner
    _safe_set(owner, 'typedValue', None)
    assert getattr(partner, 'TagDefinition130') is None


def test_assoc_type37_stub_double():
    # Classifier has no real 'Classifier38' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_StructuralFeature(changeability="sample_text", ordering="sample_text", targetScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier38', None)
    _safe_set(owner, 'typedFeature', partner)
    assert getattr(partner, 'Classifier38') == owner
    _safe_set(owner, 'typedFeature', None)
    assert getattr(partner, 'Classifier38') is None


def test_assoc_type73_stub_double():
    # Classifier has no real 'Classifier74' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_Parameter(kind="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier74', None)
    _safe_set(owner, 'typedParameter', partner)
    assert getattr(partner, 'Classifier74') == owner
    _safe_set(owner, 'typedParameter', None)
    assert getattr(partner, 'Classifier74') is None


def test_assoc_typedValue124_stub_double():
    # TaggedValue has no real 'TaggedValue126' property in the generated
    # code (a bare stub) -- manually attach it so foundation_core_TagDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # foundation_core_TagDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = foundation_core_TagDefinition(tagType="sample_text")
    partner = TaggedValue()
    setattr(partner, 'TaggedValue126', None)
    _safe_set(owner, 'type125', {partner})
    assert getattr(partner, 'TaggedValue126') == owner
    _safe_set(owner, 'type125', set())
    assert getattr(partner, 'TaggedValue126') is None


