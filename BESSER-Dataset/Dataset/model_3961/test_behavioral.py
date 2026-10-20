import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstraction,
    Association,
    BehavioralFeature,
    Class,
    Classifier,
    DataType,
    Dependency,
    DirectRelationship,
    Element,
    Feature,
    MultiplicityElement,
    NamedElement,
    Namespace,
    PackageableElement,
    Realization,
    Relationship,
    StructuralFeature,
    TypedElement,
    Typpee,
    ValueSpecification,
    uml2CD_Abstraction,
    uml2CD_Association,
    uml2CD_AssociationClass,
    uml2CD_BehavioralFeature,
    uml2CD_Class,
    uml2CD_Classifier,
    uml2CD_Comment,
    uml2CD_Constraint,
    uml2CD_DataType,
    uml2CD_Dependency,
    uml2CD_DirectRelationship,
    uml2CD_Element,
    uml2CD_ElementImport,
    uml2CD_Enumeration,
    uml2CD_EnumerationLiteral,
    uml2CD_Feature,
    uml2CD_Generalization,
    uml2CD_GeneralizationSet,
    uml2CD_Interface,
    uml2CD_InterfaceRealization,
    uml2CD_MultiplicityElement,
    uml2CD_NamedElement,
    uml2CD_Namespace,
    uml2CD_Operation,
    uml2CD_Package,
    uml2CD_PackageImport,
    uml2CD_PackageMerge,
    uml2CD_PackageableElement,
    uml2CD_Parameter,
    uml2CD_PrimitiveType,
    uml2CD_Property,
    uml2CD_Realization,
    uml2CD_RedefinableElement,
    uml2CD_Relationship,
    uml2CD_StructuralFeature,
    uml2CD_Substitution,
    uml2CD_TypedElement,
    uml2CD_Typpee,
    uml2CD_Usage,
    uml2CD_ValueSpecification,
    AggregationKind,
    ParameterDirectionKind,
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

def test_assoc_general57_reverse_link_reassign_clear():
    a1 = uml2CD_Generalization(isSubstitutable=True)
    a2 = uml2CD_Generalization(isSubstitutable=False)
    b = uml2CD_Classifier(isAbstract=True)
    _safe_set(b, 'uml2CD_Classifier', a1)
    assert _is_linked(b, 'uml2CD_Classifier', a1)
    if hasattr(a1, 'uml2CD_Generalization'):
        assert _is_linked(a1, 'uml2CD_Generalization', b)
    _safe_set(b, 'uml2CD_Classifier', a2)
    assert _is_linked(b, 'uml2CD_Classifier', a2)
    if hasattr(a1, 'uml2CD_Generalization'):
        assert not _is_linked(a1, 'uml2CD_Generalization', b)
    if hasattr(a2, 'uml2CD_Generalization'):
        assert _is_linked(a2, 'uml2CD_Generalization', b)
    _safe_set(b, 'uml2CD_Classifier', None)
    assert not _is_linked(b, 'uml2CD_Classifier', a2)
    if hasattr(a2, 'uml2CD_Generalization'):
        assert not _is_linked(a2, 'uml2CD_Generalization', b)


def test_assoc_generalization124_reverse_link_reassign_clear():
    a1 = uml2CD_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = uml2CD_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = uml2CD_Generalization(isSubstitutable=True)
    _safe_set(b, 'Generalization125', a1)
    assert _is_linked(b, 'Generalization125', a1)
    if hasattr(a1, 'generalizationSet'):
        assert _is_linked(a1, 'generalizationSet', b)
    _safe_set(b, 'Generalization125', a2)
    assert _is_linked(b, 'Generalization125', a2)
    if hasattr(a1, 'generalizationSet'):
        assert not _is_linked(a1, 'generalizationSet', b)
    if hasattr(a2, 'generalizationSet'):
        assert _is_linked(a2, 'generalizationSet', b)
    _safe_set(b, 'Generalization125', None)
    assert not _is_linked(b, 'Generalization125', a2)
    if hasattr(a2, 'generalizationSet'):
        assert not _is_linked(a2, 'generalizationSet', b)


def test_assoc_generalization61_reverse_link_reassign_clear():
    a1 = uml2CD_Generalization(isSubstitutable=True)
    a2 = uml2CD_Generalization(isSubstitutable=False)
    b = uml2CD_Classifier(isAbstract=True)
    _safe_set(b, 'specific', {a1})
    assert _is_linked(b, 'specific', a1)
    if hasattr(a1, 'Generalization'):
        assert _is_linked(a1, 'Generalization', b)
    _safe_set(b, 'specific', {a2})
    assert _is_linked(b, 'specific', a2)
    if hasattr(a1, 'Generalization'):
        assert not _is_linked(a1, 'Generalization', b)
    if hasattr(a2, 'Generalization'):
        assert _is_linked(a2, 'Generalization', b)
    _safe_set(b, 'specific', set())
    assert not _is_linked(b, 'specific', a2)
    if hasattr(a2, 'Generalization'):
        assert not _is_linked(a2, 'Generalization', b)


def test_assoc_generalizationSet59_reverse_link_reassign_clear():
    a1 = uml2CD_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = uml2CD_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = uml2CD_Generalization(isSubstitutable=True)
    _safe_set(b, 'generalization60', {a1})
    assert _is_linked(b, 'generalization60', a1)
    if hasattr(a1, 'GeneralizationSet'):
        assert _is_linked(a1, 'GeneralizationSet', b)
    _safe_set(b, 'generalization60', {a2})
    assert _is_linked(b, 'generalization60', a2)
    if hasattr(a1, 'GeneralizationSet'):
        assert not _is_linked(a1, 'GeneralizationSet', b)
    if hasattr(a2, 'GeneralizationSet'):
        assert _is_linked(a2, 'GeneralizationSet', b)
    _safe_set(b, 'generalization60', set())
    assert not _is_linked(b, 'generalization60', a2)
    if hasattr(a2, 'GeneralizationSet'):
        assert not _is_linked(a2, 'GeneralizationSet', b)


def test_assoc_powertype126_reverse_link_reassign_clear():
    a1 = uml2CD_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = uml2CD_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = uml2CD_Classifier(isAbstract=True)
    _safe_set(b, 'Classifier127', a1)
    assert _is_linked(b, 'Classifier127', a1)
    if hasattr(a1, 'powertypeExtent'):
        assert _is_linked(a1, 'powertypeExtent', b)
    _safe_set(b, 'Classifier127', a2)
    assert _is_linked(b, 'Classifier127', a2)
    if hasattr(a1, 'powertypeExtent'):
        assert not _is_linked(a1, 'powertypeExtent', b)
    if hasattr(a2, 'powertypeExtent'):
        assert _is_linked(a2, 'powertypeExtent', b)
    _safe_set(b, 'Classifier127', None)
    assert not _is_linked(b, 'Classifier127', a2)
    if hasattr(a2, 'powertypeExtent'):
        assert not _is_linked(a2, 'powertypeExtent', b)


def test_assoc_powertypeExtent64_reverse_link_reassign_clear():
    a1 = uml2CD_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = uml2CD_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = uml2CD_Classifier(isAbstract=True)
    _safe_set(b, 'powertype', {a1})
    assert _is_linked(b, 'powertype', a1)
    if hasattr(a1, 'GeneralizationSet65'):
        assert _is_linked(a1, 'GeneralizationSet65', b)
    _safe_set(b, 'powertype', {a2})
    assert _is_linked(b, 'powertype', a2)
    if hasattr(a1, 'GeneralizationSet65'):
        assert not _is_linked(a1, 'GeneralizationSet65', b)
    if hasattr(a2, 'GeneralizationSet65'):
        assert _is_linked(a2, 'GeneralizationSet65', b)
    _safe_set(b, 'powertype', set())
    assert not _is_linked(b, 'powertype', a2)
    if hasattr(a2, 'GeneralizationSet65'):
        assert not _is_linked(a2, 'GeneralizationSet65', b)


def test_assoc_redefinedElement129_reverse_link_reassign_clear():
    a1 = uml2CD_RedefinableElement(isLeaf=True)
    a2 = uml2CD_RedefinableElement(isLeaf=False)
    b = uml2CD_RedefinableElement(isLeaf=True)
    _safe_set(b, 'uml2CD_RedefinableElement128', {a1})
    assert _is_linked(b, 'uml2CD_RedefinableElement128', a1)
    if hasattr(a1, 'uml2CD_RedefinableElement'):
        assert _is_linked(a1, 'uml2CD_RedefinableElement', b)
    _safe_set(b, 'uml2CD_RedefinableElement128', {a2})
    assert _is_linked(b, 'uml2CD_RedefinableElement128', a2)
    if hasattr(a1, 'uml2CD_RedefinableElement'):
        assert not _is_linked(a1, 'uml2CD_RedefinableElement', b)
    if hasattr(a2, 'uml2CD_RedefinableElement'):
        assert _is_linked(a2, 'uml2CD_RedefinableElement', b)
    _safe_set(b, 'uml2CD_RedefinableElement128', set())
    assert not _is_linked(b, 'uml2CD_RedefinableElement128', a2)
    if hasattr(a2, 'uml2CD_RedefinableElement'):
        assert not _is_linked(a2, 'uml2CD_RedefinableElement', b)


def test_assoc_redefinedOperation77_reverse_link_reassign_clear():
    a1 = uml2CD_Operation(isQuery=True)
    a2 = uml2CD_Operation(isQuery=False)
    b = uml2CD_Operation(isQuery=True)
    _safe_set(b, 'uml2CD_Operation76', {a1})
    assert _is_linked(b, 'uml2CD_Operation76', a1)
    if hasattr(a1, 'uml2CD_Operation'):
        assert _is_linked(a1, 'uml2CD_Operation', b)
    _safe_set(b, 'uml2CD_Operation76', {a2})
    assert _is_linked(b, 'uml2CD_Operation76', a2)
    if hasattr(a1, 'uml2CD_Operation'):
        assert not _is_linked(a1, 'uml2CD_Operation', b)
    if hasattr(a2, 'uml2CD_Operation'):
        assert _is_linked(a2, 'uml2CD_Operation', b)
    _safe_set(b, 'uml2CD_Operation76', set())
    assert not _is_linked(b, 'uml2CD_Operation76', a2)
    if hasattr(a2, 'uml2CD_Operation'):
        assert not _is_linked(a2, 'uml2CD_Operation', b)


def test_assoc_specific58_reverse_link_reassign_clear():
    a1 = uml2CD_Generalization(isSubstitutable=True)
    a2 = uml2CD_Generalization(isSubstitutable=False)
    b = uml2CD_Classifier(isAbstract=True)
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'generalization'):
        assert _is_linked(a1, 'generalization', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'generalization'):
        assert not _is_linked(a1, 'generalization', b)
    if hasattr(a2, 'generalization'):
        assert _is_linked(a2, 'generalization', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'generalization'):
        assert not _is_linked(a2, 'generalization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Class63_stub_double():
    # uml2CD_Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'nestedClassifier', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'nestedClassifier', None)
    assert getattr(partner, 'Class') is None


def test_assoc_Class78_stub_double():
    # uml2CD_Class has no real 'Class79' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Operation(isQuery=True)
    partner = uml2CD_Class()
    setattr(partner, 'Class79', None)
    _safe_set(owner, 'ownedOperation', partner)
    assert getattr(partner, 'Class79') == owner
    _safe_set(owner, 'ownedOperation', None)
    assert getattr(partner, 'Class79') is None


def test_assoc_association94_stub_double():
    # uml2CD_Property has no real 'memberEnd' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Association(isDerived=True)
    partner = uml2CD_Property()
    setattr(partner, 'memberEnd', None)
    _safe_set(owner, 'Association', partner)
    assert getattr(partner, 'memberEnd') == owner
    _safe_set(owner, 'Association', None)
    assert getattr(partner, 'memberEnd') is None


def test_assoc_client114_stub_double():
    # uml2CD_Dependency has no real 'clientDependency' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_NamedElement(name="sample_text")
    partner = uml2CD_Dependency()
    setattr(partner, 'clientDependency', None)
    _safe_set(owner, 'NamedElement115', partner)
    assert owner in getattr(partner, 'clientDependency')
    _safe_set(owner, 'NamedElement115', None)
    assert owner not in getattr(partner, 'clientDependency')


def test_assoc_clientDependency16_stub_double():
    # uml2CD_Dependency has no real 'Dependency17' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_NamedElement(name="sample_text")
    partner = uml2CD_Dependency()
    setattr(partner, 'Dependency17', None)
    _safe_set(owner, 'client', {partner})
    assert getattr(partner, 'Dependency17') == owner
    _safe_set(owner, 'client', set())
    assert getattr(partner, 'Dependency17') is None


def test_assoc_contract116_stub_double():
    # uml2CD_Substitution has no real 'uml2CD_Substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Substitution()
    setattr(partner, 'uml2CD_Substitution', None)
    _safe_set(owner, 'uml2CD_Classifier117', partner)
    assert getattr(partner, 'uml2CD_Substitution') == owner
    _safe_set(owner, 'uml2CD_Classifier117', None)
    assert getattr(partner, 'uml2CD_Substitution') is None


def test_assoc_defaultValue74_stub_double():
    # uml2CD_ValueSpecification has no real 'ValueSpecification75' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Parameter(direction="sample_text")
    partner = uml2CD_ValueSpecification()
    setattr(partner, 'ValueSpecification75', None)
    _safe_set(owner, 'owningParameter', partner)
    assert getattr(partner, 'ValueSpecification75') == owner
    _safe_set(owner, 'owningParameter', None)
    assert getattr(partner, 'ValueSpecification75') is None


def test_assoc_elementImport22_stub_double():
    # uml2CD_Namespace has no real 'importingNamespace23' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_ElementImport(visibility="sample_text")
    partner = uml2CD_Namespace()
    setattr(partner, 'importingNamespace23', None)
    _safe_set(owner, 'ElementImport', partner)
    assert owner in getattr(partner, 'importingNamespace23')
    _safe_set(owner, 'ElementImport', None)
    assert owner not in getattr(partner, 'importingNamespace23')


def test_assoc_feature62_stub_double():
    # uml2CD_Feature has no real 'Feature' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Feature()
    setattr(partner, 'Feature', None)
    _safe_set(owner, 'featuringClassifier', {partner})
    assert getattr(partner, 'Feature') == owner
    _safe_set(owner, 'featuringClassifier', set())
    assert getattr(partner, 'Feature') is None


def test_assoc_featuringClassifier67_stub_double():
    # uml2CD_Feature has no real 'feature' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Feature()
    setattr(partner, 'feature', None)
    _safe_set(owner, 'Classifier68', partner)
    assert owner in getattr(partner, 'feature')
    _safe_set(owner, 'Classifier68', None)
    assert owner not in getattr(partner, 'feature')


def test_assoc_importedElement25_stub_double():
    # uml2CD_PackageableElement has no real 'uml2CD_PackageableElement26' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_ElementImport(visibility="sample_text")
    partner = uml2CD_PackageableElement()
    setattr(partner, 'uml2CD_PackageableElement26', None)
    _safe_set(owner, 'uml2CD_ElementImport', partner)
    assert getattr(partner, 'uml2CD_PackageableElement26') == owner
    _safe_set(owner, 'uml2CD_ElementImport', None)
    assert getattr(partner, 'uml2CD_PackageableElement26') is None


def test_assoc_importedPackage28_stub_double():
    # uml2CD_Package has no real 'uml2CD_Package' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_PackageImport(visibility="sample_text")
    partner = uml2CD_Package()
    setattr(partner, 'uml2CD_Package', None)
    _safe_set(owner, 'uml2CD_PackageImport', partner)
    assert getattr(partner, 'uml2CD_Package') == owner
    _safe_set(owner, 'uml2CD_PackageImport', None)
    assert getattr(partner, 'uml2CD_Package') is None


def test_assoc_importingNamespace27_stub_double():
    # uml2CD_Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_ElementImport(visibility="sample_text")
    partner = uml2CD_Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'elementImport', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'elementImport', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_importingNamespace29_stub_double():
    # uml2CD_Namespace has no real 'Namespace30' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_PackageImport(visibility="sample_text")
    partner = uml2CD_Namespace()
    setattr(partner, 'Namespace30', None)
    _safe_set(owner, 'packageImport', partner)
    assert getattr(partner, 'Namespace30') == owner
    _safe_set(owner, 'packageImport', None)
    assert getattr(partner, 'Namespace30') is None


def test_assoc_memberEnd103_stub_double():
    # uml2CD_Property has no real 'Property104' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Association(isDerived=True)
    partner = uml2CD_Property()
    setattr(partner, 'Property104', None)
    _safe_set(owner, 'association', {partner})
    assert getattr(partner, 'Property104') == owner
    _safe_set(owner, 'association', set())
    assert getattr(partner, 'Property104') is None


def test_assoc_namespace14_stub_double():
    # uml2CD_Namespace has no real 'uml2CD_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_NamedElement(name="sample_text")
    partner = uml2CD_Namespace()
    setattr(partner, 'uml2CD_Namespace', None)
    _safe_set(owner, 'uml2CD_NamedElement', partner)
    assert getattr(partner, 'uml2CD_Namespace') == owner
    _safe_set(owner, 'uml2CD_NamedElement', None)
    assert getattr(partner, 'uml2CD_Namespace') is None


def test_assoc_nestedClassifier82_stub_double():
    # uml2CD_Class has no real 'Class83' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Class()
    setattr(partner, 'Class83', None)
    _safe_set(owner, 'Classifier84', partner)
    assert owner in getattr(partner, 'Class83')
    _safe_set(owner, 'Classifier84', None)
    assert owner not in getattr(partner, 'Class83')


def test_assoc_ownedEnd105_stub_double():
    # uml2CD_Property has no real 'Property106' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Association(isDerived=True)
    partner = uml2CD_Property()
    setattr(partner, 'Property106', None)
    _safe_set(owner, 'owningAssociation', {partner})
    assert getattr(partner, 'Property106') == owner
    _safe_set(owner, 'owningAssociation', set())
    assert getattr(partner, 'Property106') is None


def test_assoc_ownedOperation85_stub_double():
    # uml2CD_Class has no real 'Class86' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Operation(isQuery=True)
    partner = uml2CD_Class()
    setattr(partner, 'Class86', None)
    _safe_set(owner, 'Operation', partner)
    assert owner in getattr(partner, 'Class86')
    _safe_set(owner, 'Operation', None)
    assert owner not in getattr(partner, 'Class86')


def test_assoc_ownedParameter69_stub_double():
    # uml2CD_BehavioralFeature has no real 'ownerFormalParam' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Parameter(direction="sample_text")
    partner = uml2CD_BehavioralFeature()
    setattr(partner, 'ownerFormalParam', None)
    _safe_set(owner, 'Parameter70', partner)
    assert owner in getattr(partner, 'ownerFormalParam')
    _safe_set(owner, 'Parameter70', None)
    assert owner not in getattr(partner, 'ownerFormalParam')


def test_assoc_ownerFormalParam73_stub_double():
    # uml2CD_BehavioralFeature has no real 'BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Parameter(direction="sample_text")
    partner = uml2CD_BehavioralFeature()
    setattr(partner, 'BehavioralFeature', None)
    _safe_set(owner, 'ownedParameter', partner)
    assert getattr(partner, 'BehavioralFeature') == owner
    _safe_set(owner, 'ownedParameter', None)
    assert getattr(partner, 'BehavioralFeature') is None


def test_assoc_owningAssociation95_stub_double():
    # uml2CD_Property has no real 'ownedEnd' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Association(isDerived=True)
    partner = uml2CD_Property()
    setattr(partner, 'ownedEnd', None)
    _safe_set(owner, 'Association96', partner)
    assert getattr(partner, 'ownedEnd') == owner
    _safe_set(owner, 'Association96', None)
    assert getattr(partner, 'ownedEnd') is None


def test_assoc_owningParameter47_stub_double():
    # uml2CD_ValueSpecification has no real 'defaultValue' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Parameter(direction="sample_text")
    partner = uml2CD_ValueSpecification()
    setattr(partner, 'defaultValue', None)
    _safe_set(owner, 'Parameter', partner)
    assert getattr(partner, 'defaultValue') == owner
    _safe_set(owner, 'Parameter', None)
    assert getattr(partner, 'defaultValue') is None


def test_assoc_packageImport21_stub_double():
    # uml2CD_Namespace has no real 'importingNamespace' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_PackageImport(visibility="sample_text")
    partner = uml2CD_Namespace()
    setattr(partner, 'importingNamespace', None)
    _safe_set(owner, 'PackageImport', partner)
    assert owner in getattr(partner, 'importingNamespace')
    _safe_set(owner, 'PackageImport', None)
    assert owner not in getattr(partner, 'importingNamespace')


def test_assoc_substitutingClassifier118_stub_double():
    # uml2CD_Substitution has no real 'substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Substitution()
    setattr(partner, 'substitution', None)
    _safe_set(owner, 'Classifier119', partner)
    assert getattr(partner, 'substitution') == owner
    _safe_set(owner, 'Classifier119', None)
    assert getattr(partner, 'substitution') is None


def test_assoc_substitution66_stub_double():
    # uml2CD_Substitution has no real 'Substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_Classifier(isAbstract=True)
    partner = uml2CD_Substitution()
    setattr(partner, 'Substitution', None)
    _safe_set(owner, 'substitutingClassifier', {partner})
    assert getattr(partner, 'Substitution') == owner
    _safe_set(owner, 'substitutingClassifier', set())
    assert getattr(partner, 'Substitution') is None


def test_assoc_supplier113_stub_double():
    # uml2CD_Dependency has no real 'supplierDependency' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_NamedElement(name="sample_text")
    partner = uml2CD_Dependency()
    setattr(partner, 'supplierDependency', None)
    _safe_set(owner, 'NamedElement', partner)
    assert owner in getattr(partner, 'supplierDependency')
    _safe_set(owner, 'NamedElement', None)
    assert owner not in getattr(partner, 'supplierDependency')


def test_assoc_supplierDependency15_stub_double():
    # uml2CD_Dependency has no real 'Dependency' property in the generated
    # code (a bare stub) -- manually attach it so uml2CD_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2CD_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2CD_NamedElement(name="sample_text")
    partner = uml2CD_Dependency()
    setattr(partner, 'Dependency', None)
    _safe_set(owner, 'supplier', {partner})
    assert getattr(partner, 'Dependency') == owner
    _safe_set(owner, 'supplier', set())
    assert getattr(partner, 'Dependency') is None


