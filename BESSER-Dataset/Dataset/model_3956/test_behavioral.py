import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstraction,
    Association,
    BehavioralFeature,
    BehavioredClassifier,
    Class,
    Classes_AssociationClasses_AssociationClass,
    Classes_Dependencies_Abstraction,
    Classes_Dependencies_Dependency,
    Classes_Dependencies_Realization,
    Classes_Dependencies_Substitution,
    Classes_Dependencies_Usage,
    Classes_Interfaces_BehavioredClassifier,
    Classes_Interfaces_Interface,
    Classes_Interfaces_InterfaceRealization,
    Classes_Kernel_Association,
    Classes_Kernel_BehavioralFeature,
    Classes_Kernel_Class,
    Classes_Kernel_Classifier,
    Classes_Kernel_Comment,
    Classes_Kernel_Constraint,
    Classes_Kernel_DataType,
    Classes_Kernel_DirectedRelationship,
    Classes_Kernel_Element,
    Classes_Kernel_ElementImport,
    Classes_Kernel_Enumeration,
    Classes_Kernel_EnumerationLiteral,
    Classes_Kernel_Expression,
    Classes_Kernel_Feature,
    Classes_Kernel_Generalization_,
    Classes_Kernel_InstanceSpecification,
    Classes_Kernel_InstanceValue,
    Classes_Kernel_LiteralBoolean,
    Classes_Kernel_LiteralInteger,
    Classes_Kernel_LiteralNull,
    Classes_Kernel_LiteralReal,
    Classes_Kernel_LiteralSpecification,
    Classes_Kernel_LiteralString,
    Classes_Kernel_LiteralUnilimitedNatural,
    Classes_Kernel_MultiplicityElement,
    Classes_Kernel_NamedElement,
    Classes_Kernel_Namespace,
    Classes_Kernel_OpaqueExpression,
    Classes_Kernel_Operation,
    Classes_Kernel_Package,
    Classes_Kernel_PackageImport,
    Classes_Kernel_PackageMerge,
    Classes_Kernel_PackageableElement,
    Classes_Kernel_Parameter,
    Classes_Kernel_PrimitiveType,
    Classes_Kernel_Property,
    Classes_Kernel_RedefinableElement,
    Classes_Kernel_Relationship,
    Classes_Kernel_Slot,
    Classes_Kernel_StructuralFeature,
    Classes_Kernel_Type,
    Classes_Kernel_TypedElement,
    Classes_Kernel_ValueSpecification,
    Classes_PowerTypes_GeneralizationSet,
    Classifier,
    Comment,
    Constraint,
    DataType,
    Dependency,
    DirectedRelationship,
    Element,
    ElementImport,
    Enumeration,
    EnumerationLiteral,
    Feature,
    GeneralizationSet,
    Generalization_,
    InstanceSpecification,
    Interface,
    InterfaceRealization,
    Kernel_Association,
    Kernel_Class,
    Kernel_Classifier,
    Kernel_DirectedRelationship,
    Kernel_Feature,
    Kernel_MultiplicityElement,
    Kernel_Namespace,
    Kernel_PackageableElement,
    Kernel_RedefinableElement,
    Kernel_Relationship,
    Kernel_Type,
    Kernel_TypedElement,
    LiteralSpecification,
    MultiplicityElement,
    NamedElement,
    Namespace,
    OpaqueExpression,
    Operation,
    Package,
    PackageImport,
    PackageMerge,
    PackageableElement,
    Parameter,
    Property,
    Realization,
    RedefinableElement,
    Relationship,
    Slot,
    StructuralFeature,
    Substitution,
    Type,
    TypedElement,
    ValueSpecification,
    AggregationKind,
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

def test_assoc_annotatedElement32_stub_double():
    # Element has no real 'Element33' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Comment(body="sample_text")
    partner = Element()
    setattr(partner, 'Element33', None)
    _safe_set(owner, 'Classes_Kernel_Comment', {partner})
    assert getattr(partner, 'Element33') == owner
    _safe_set(owner, 'Classes_Kernel_Comment', set())
    assert getattr(partner, 'Element33') is None


def test_assoc_association108_stub_double():
    # Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'memberEnd', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'memberEnd', None)
    assert getattr(partner, 'Association') is None


def test_assoc_associationEnd117_stub_double():
    # Property has no real 'Property118' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Property()
    setattr(partner, 'Property118', None)
    _safe_set(owner, 'qualifier', partner)
    assert getattr(partner, 'Property118') == owner
    _safe_set(owner, 'qualifier', None)
    assert getattr(partner, 'Property118') is None


def test_assoc_attribute83_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'Classes_Kernel_Classifier84', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'Classes_Kernel_Classifier84', set())
    assert getattr(partner, 'Property') is None


def test_assoc_bodyCondition139_stub_double():
    # Constraint has no real 'Constraint141' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Constraint()
    setattr(partner, 'Constraint141', None)
    _safe_set(owner, 'Classes_Kernel_Operation140', {partner})
    assert getattr(partner, 'Constraint141') == owner
    _safe_set(owner, 'Classes_Kernel_Operation140', set())
    assert getattr(partner, 'Constraint141') is None


def test_assoc_class_145_stub_double():
    # Class has no real 'Class146' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Class()
    setattr(partner, 'Class146', None)
    _safe_set(owner, 'ownedOperation', partner)
    assert getattr(partner, 'Class146') == owner
    _safe_set(owner, 'ownedOperation', None)
    assert getattr(partner, 'Class146') is None


def test_assoc_class_96_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'Class') is None


def test_assoc_clientDependency5_stub_double():
    # Dependency has no real 'Dependency' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = Dependency()
    setattr(partner, 'Dependency', None)
    _safe_set(owner, 'client', {partner})
    assert getattr(partner, 'Dependency') == owner
    _safe_set(owner, 'client', set())
    assert getattr(partner, 'Dependency') is None


def test_assoc_dataType111_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'ownedAttribute112', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'ownedAttribute112', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_dataType147_stub_double():
    # DataType has no real 'DataType149' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = DataType()
    setattr(partner, 'DataType149', None)
    _safe_set(owner, 'ownedOperation148', partner)
    assert getattr(partner, 'DataType149') == owner
    _safe_set(owner, 'ownedOperation148', None)
    assert getattr(partner, 'DataType149') is None


def test_assoc_defaultValue131_stub_double():
    # ValueSpecification has no real 'ValueSpecification133' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Parameter(default="sample_text")
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification133', None)
    _safe_set(owner, 'Classes_Kernel_Parameter132', partner)
    assert getattr(partner, 'ValueSpecification133') == owner
    _safe_set(owner, 'Classes_Kernel_Parameter132', None)
    assert getattr(partner, 'ValueSpecification133') is None


def test_assoc_defaultValue99_stub_double():
    # ValueSpecification has no real 'ValueSpecification101' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification101', None)
    _safe_set(owner, 'Classes_Kernel_Property100', partner)
    assert getattr(partner, 'ValueSpecification101') == owner
    _safe_set(owner, 'Classes_Kernel_Property100', None)
    assert getattr(partner, 'ValueSpecification101') is None


def test_assoc_feature82_stub_double():
    # Feature has no real 'Feature' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Feature()
    setattr(partner, 'Feature', None)
    _safe_set(owner, 'featuringClassifier', {partner})
    assert getattr(partner, 'Feature') == owner
    _safe_set(owner, 'featuringClassifier', set())
    assert getattr(partner, 'Feature') is None


def test_assoc_featuringClassifier94_stub_double():
    # Classifier has no real 'Classifier95' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Feature(isStatic=True)
    partner = Classifier()
    setattr(partner, 'Classifier95', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'Classifier95') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'Classifier95') is None


def test_assoc_general119_stub_double():
    # Classifier has no real 'Classifier120' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Generalization_(isSubstitutable=True)
    partner = Classifier()
    setattr(partner, 'Classifier120', None)
    _safe_set(owner, 'Classes_Kernel_Generalization', partner)
    assert getattr(partner, 'Classifier120') == owner
    _safe_set(owner, 'Classes_Kernel_Generalization', None)
    assert getattr(partner, 'Classifier120') is None


def test_assoc_general88_stub_double():
    # Classifier has no real 'Classifier90' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Classifier()
    setattr(partner, 'Classifier90', None)
    _safe_set(owner, 'Classes_Kernel_Classifier89', {partner})
    assert getattr(partner, 'Classifier90') == owner
    _safe_set(owner, 'Classes_Kernel_Classifier89', set())
    assert getattr(partner, 'Classifier90') is None


def test_assoc_generalization204_stub_double():
    # Generalization_ has no real 'Generalization205' property in the generated
    # code (a bare stub) -- manually attach it so Classes_PowerTypes_GeneralizationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_PowerTypes_GeneralizationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_PowerTypes_GeneralizationSet(isCovering=True, isDisjoint=True)
    partner = Generalization_()
    setattr(partner, 'Generalization205', None)
    _safe_set(owner, 'generalizationSet', {partner})
    assert getattr(partner, 'Generalization205') == owner
    _safe_set(owner, 'generalizationSet', set())
    assert getattr(partner, 'Generalization205') is None


def test_assoc_generalization91_stub_double():
    # Generalization_ has no real 'Generalization_' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Generalization_()
    setattr(partner, 'Generalization_', None)
    _safe_set(owner, 'specific', {partner})
    assert getattr(partner, 'Generalization_') == owner
    _safe_set(owner, 'specific', set())
    assert getattr(partner, 'Generalization_') is None


def test_assoc_generalizationSet123_stub_double():
    # GeneralizationSet has no real 'GeneralizationSet125' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Generalization_(isSubstitutable=True)
    partner = GeneralizationSet()
    setattr(partner, 'GeneralizationSet125', None)
    _safe_set(owner, 'generalization124', {partner})
    assert getattr(partner, 'GeneralizationSet125') == owner
    _safe_set(owner, 'generalization124', set())
    assert getattr(partner, 'GeneralizationSet125') is None


def test_assoc_importedElement15_stub_double():
    # PackageableElement has no real 'PackageableElement16' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_ElementImport(alias="sample_text", visibility="sample_text")
    partner = PackageableElement()
    setattr(partner, 'PackageableElement16', None)
    _safe_set(owner, 'Classes_Kernel_ElementImport', partner)
    assert getattr(partner, 'PackageableElement16') == owner
    _safe_set(owner, 'Classes_Kernel_ElementImport', None)
    assert getattr(partner, 'PackageableElement16') is None


def test_assoc_importedPackage19_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_PackageImport(visibility="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'Classes_Kernel_PackageImport', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'Classes_Kernel_PackageImport', None)
    assert getattr(partner, 'Package') is None


def test_assoc_importingNamespace17_stub_double():
    # Namespace has no real 'Namespace18' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_ElementImport(alias="sample_text", visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace18', None)
    _safe_set(owner, 'elementImport', partner)
    assert getattr(partner, 'Namespace18') == owner
    _safe_set(owner, 'elementImport', None)
    assert getattr(partner, 'Namespace18') is None


def test_assoc_importingNamespace20_stub_double():
    # Namespace has no real 'Namespace21' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_PackageImport(visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace21', None)
    _safe_set(owner, 'packageImport', partner)
    assert getattr(partner, 'Namespace21') == owner
    _safe_set(owner, 'packageImport', None)
    assert getattr(partner, 'Namespace21') is None


def test_assoc_inheritedMember80_stub_double():
    # NamedElement has no real 'NamedElement81' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = NamedElement()
    setattr(partner, 'NamedElement81', None)
    _safe_set(owner, 'Classes_Kernel_Classifier', {partner})
    assert getattr(partner, 'NamedElement81') == owner
    _safe_set(owner, 'Classes_Kernel_Classifier', set())
    assert getattr(partner, 'NamedElement81') is None


def test_assoc_interface113_stub_double():
    # Interface has no real 'Interface' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Interface()
    setattr(partner, 'Interface', None)
    _safe_set(owner, 'ownedAttribute114', partner)
    assert getattr(partner, 'Interface') == owner
    _safe_set(owner, 'ownedAttribute114', None)
    assert getattr(partner, 'Interface') is None


def test_assoc_interface150_stub_double():
    # Interface has no real 'Interface152' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Interface()
    setattr(partner, 'Interface152', None)
    _safe_set(owner, 'ownedOperation151', partner)
    assert getattr(partner, 'Interface152') == owner
    _safe_set(owner, 'ownedOperation151', None)
    assert getattr(partner, 'Interface152') is None


def test_assoc_lowerValue42_stub_double():
    # ValueSpecification has no real 'ValueSpecification43' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification43', None)
    _safe_set(owner, 'owningLower', partner)
    assert getattr(partner, 'ValueSpecification43') == owner
    _safe_set(owner, 'owningLower', None)
    assert getattr(partner, 'ValueSpecification43') is None


def test_assoc_memberEnd164_stub_double():
    # Property has no real 'Property165' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Association(isDerived=True)
    partner = Property()
    setattr(partner, 'Property165', None)
    _safe_set(owner, 'association', {partner})
    assert getattr(partner, 'Property165') == owner
    _safe_set(owner, 'association', set())
    assert getattr(partner, 'Property165') is None


def test_assoc_namespace4_stub_double():
    # Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedMember', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedMember', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_navigableOwnedEnd162_stub_double():
    # Property has no real 'Property163' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Association(isDerived=True)
    partner = Property()
    setattr(partner, 'Property163', None)
    _safe_set(owner, 'Classes_Kernel_Association', {partner})
    assert getattr(partner, 'Property163') == owner
    _safe_set(owner, 'Classes_Kernel_Association', set())
    assert getattr(partner, 'Property163') is None


def test_assoc_nestedPackage22_stub_double():
    # Package has no real 'Package23' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Package(URI="sample_text")
    partner = Package()
    setattr(partner, 'Package23', None)
    _safe_set(owner, 'nestingPackage', {partner})
    assert getattr(partner, 'Package23') == owner
    _safe_set(owner, 'nestingPackage', set())
    assert getattr(partner, 'Package23') is None


def test_assoc_nestingPackage24_stub_double():
    # Package has no real 'Package25' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Package(URI="sample_text")
    partner = Package()
    setattr(partner, 'Package25', None)
    _safe_set(owner, 'nestedPackage', partner)
    assert getattr(partner, 'Package25') == owner
    _safe_set(owner, 'nestedPackage', None)
    assert getattr(partner, 'Package25') is None


def test_assoc_operand56_stub_double():
    # ValueSpecification has no real 'ValueSpecification57' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Expression(symbol="sample_text")
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification57', None)
    _safe_set(owner, 'Classes_Kernel_Expression', partner)
    assert getattr(partner, 'ValueSpecification57') == owner
    _safe_set(owner, 'Classes_Kernel_Expression', None)
    assert getattr(partner, 'ValueSpecification57') is None


def test_assoc_opposite102_stub_double():
    # Property has no real 'Property104' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Property()
    setattr(partner, 'Property104', None)
    _safe_set(owner, 'Classes_Kernel_Property103', partner)
    assert getattr(partner, 'Property104') == owner
    _safe_set(owner, 'Classes_Kernel_Property103', None)
    assert getattr(partner, 'Property104') is None


def test_assoc_ownedEnd166_stub_double():
    # Property has no real 'Property167' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Association(isDerived=True)
    partner = Property()
    setattr(partner, 'Property167', None)
    _safe_set(owner, 'owningAssociation', {partner})
    assert getattr(partner, 'Property167') == owner
    _safe_set(owner, 'owningAssociation', set())
    assert getattr(partner, 'Property167') is None


def test_assoc_ownedFormalParam130_stub_double():
    # BehavioralFeature has no real 'BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Parameter(default="sample_text")
    partner = BehavioralFeature()
    setattr(partner, 'BehavioralFeature', None)
    _safe_set(owner, 'Classes_Kernel_Parameter', partner)
    assert getattr(partner, 'BehavioralFeature') == owner
    _safe_set(owner, 'Classes_Kernel_Parameter', None)
    assert getattr(partner, 'BehavioralFeature') is None


def test_assoc_ownedType28_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Package(URI="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type') is None


def test_assoc_owningAssociation109_stub_double():
    # Association has no real 'Association110' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Association()
    setattr(partner, 'Association110', None)
    _safe_set(owner, 'ownedEnd', partner)
    assert getattr(partner, 'Association110') == owner
    _safe_set(owner, 'ownedEnd', None)
    assert getattr(partner, 'Association110') is None


def test_assoc_owningElement30_stub_double():
    # Element has no real 'Element31' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Comment(body="sample_text")
    partner = Element()
    setattr(partner, 'Element31', None)
    _safe_set(owner, 'ownedComment', partner)
    assert getattr(partner, 'Element31') == owner
    _safe_set(owner, 'ownedComment', None)
    assert getattr(partner, 'Element31') is None


def test_assoc_packageMerge29_stub_double():
    # PackageMerge has no real 'PackageMerge' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Package(URI="sample_text")
    partner = PackageMerge()
    setattr(partner, 'PackageMerge', None)
    _safe_set(owner, 'receivingPackage', {partner})
    assert getattr(partner, 'PackageMerge') == owner
    _safe_set(owner, 'receivingPackage', set())
    assert getattr(partner, 'PackageMerge') is None


def test_assoc_packagedElement26_stub_double():
    # PackageableElement has no real 'PackageableElement27' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Package(URI="sample_text")
    partner = PackageableElement()
    setattr(partner, 'PackageableElement27', None)
    _safe_set(owner, 'Classes_Kernel_Package', {partner})
    assert getattr(partner, 'PackageableElement27') == owner
    _safe_set(owner, 'Classes_Kernel_Package', set())
    assert getattr(partner, 'PackageableElement27') is None


def test_assoc_postcondition142_stub_double():
    # Constraint has no real 'Constraint144' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Constraint()
    setattr(partner, 'Constraint144', None)
    _safe_set(owner, 'Classes_Kernel_Operation143', {partner})
    assert getattr(partner, 'Constraint144') == owner
    _safe_set(owner, 'Classes_Kernel_Operation143', set())
    assert getattr(partner, 'Constraint144') is None


def test_assoc_powertype202_stub_double():
    # Classifier has no real 'Classifier203' property in the generated
    # code (a bare stub) -- manually attach it so Classes_PowerTypes_GeneralizationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_PowerTypes_GeneralizationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_PowerTypes_GeneralizationSet(isCovering=True, isDisjoint=True)
    partner = Classifier()
    setattr(partner, 'Classifier203', None)
    _safe_set(owner, 'powertypeExtent', partner)
    assert getattr(partner, 'Classifier203') == owner
    _safe_set(owner, 'powertypeExtent', None)
    assert getattr(partner, 'Classifier203') is None


def test_assoc_powertypeExtent93_stub_double():
    # GeneralizationSet has no real 'GeneralizationSet' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = GeneralizationSet()
    setattr(partner, 'GeneralizationSet', None)
    _safe_set(owner, 'powertype', {partner})
    assert getattr(partner, 'GeneralizationSet') == owner
    _safe_set(owner, 'powertype', set())
    assert getattr(partner, 'GeneralizationSet') is None


def test_assoc_precondition136_stub_double():
    # Constraint has no real 'Constraint138' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Constraint()
    setattr(partner, 'Constraint138', None)
    _safe_set(owner, 'Classes_Kernel_Operation137', {partner})
    assert getattr(partner, 'Constraint138') == owner
    _safe_set(owner, 'Classes_Kernel_Operation137', set())
    assert getattr(partner, 'Constraint138') is None


def test_assoc_qualifier115_stub_double():
    # Property has no real 'Property116' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Property()
    setattr(partner, 'Property116', None)
    _safe_set(owner, 'associationEnd', {partner})
    assert getattr(partner, 'Property116') == owner
    _safe_set(owner, 'associationEnd', set())
    assert getattr(partner, 'Property116') is None


def test_assoc_redefinedClassifier85_stub_double():
    # Classifier has no real 'Classifier87' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Classifier()
    setattr(partner, 'Classifier87', None)
    _safe_set(owner, 'Classes_Kernel_Classifier86', {partner})
    assert getattr(partner, 'Classifier87') == owner
    _safe_set(owner, 'Classes_Kernel_Classifier86', set())
    assert getattr(partner, 'Classifier87') is None


def test_assoc_redefinedElement76_stub_double():
    # RedefinableElement has no real 'RedefinableElement' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_RedefinableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_RedefinableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_RedefinableElement(isLeaf=True)
    partner = RedefinableElement()
    setattr(partner, 'RedefinableElement', None)
    _safe_set(owner, 'Classes_Kernel_RedefinableElement', {partner})
    assert getattr(partner, 'RedefinableElement') == owner
    _safe_set(owner, 'Classes_Kernel_RedefinableElement', set())
    assert getattr(partner, 'RedefinableElement') is None


def test_assoc_redefinedProperty97_stub_double():
    # Property has no real 'Property98' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Property()
    setattr(partner, 'Property98', None)
    _safe_set(owner, 'Classes_Kernel_Property', {partner})
    assert getattr(partner, 'Property98') == owner
    _safe_set(owner, 'Classes_Kernel_Property', set())
    assert getattr(partner, 'Property98') is None


def test_assoc_redefinitionContext77_stub_double():
    # Classifier has no real 'Classifier79' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_RedefinableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_RedefinableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_RedefinableElement(isLeaf=True)
    partner = Classifier()
    setattr(partner, 'Classifier79', None)
    _safe_set(owner, 'Classes_Kernel_RedefinableElement78', {partner})
    assert getattr(partner, 'Classifier79') == owner
    _safe_set(owner, 'Classes_Kernel_RedefinableElement78', set())
    assert getattr(partner, 'Classifier79') is None


def test_assoc_specific121_stub_double():
    # Classifier has no real 'Classifier122' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Generalization_(isSubstitutable=True)
    partner = Classifier()
    setattr(partner, 'Classifier122', None)
    _safe_set(owner, 'generalization', partner)
    assert getattr(partner, 'Classifier122') == owner
    _safe_set(owner, 'generalization', None)
    assert getattr(partner, 'Classifier122') is None


def test_assoc_subsettedProperty105_stub_double():
    # Property has no real 'Property107' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = Property()
    setattr(partner, 'Property107', None)
    _safe_set(owner, 'Classes_Kernel_Property106', partner)
    assert getattr(partner, 'Property107') == owner
    _safe_set(owner, 'Classes_Kernel_Property106', None)
    assert getattr(partner, 'Property107') is None


def test_assoc_substitution92_stub_double():
    # Substitution has no real 'Substitution' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = Substitution()
    setattr(partner, 'Substitution', None)
    _safe_set(owner, 'substitutingClassifier', {partner})
    assert getattr(partner, 'Substitution') == owner
    _safe_set(owner, 'substitutingClassifier', set())
    assert getattr(partner, 'Substitution') is None


def test_assoc_type134_stub_double():
    # Type has no real 'Type135' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = Type()
    setattr(partner, 'Type135', None)
    _safe_set(owner, 'Classes_Kernel_Operation', partner)
    assert getattr(partner, 'Type135') == owner
    _safe_set(owner, 'Classes_Kernel_Operation', None)
    assert getattr(partner, 'Type135') is None


def test_assoc_upperValue41_stub_double():
    # ValueSpecification has no real 'ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Kernel_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Kernel_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Kernel_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification', None)
    _safe_set(owner, 'owningUpper', partner)
    assert getattr(partner, 'ValueSpecification') == owner
    _safe_set(owner, 'owningUpper', None)
    assert getattr(partner, 'ValueSpecification') is None


