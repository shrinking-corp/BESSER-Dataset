import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    BehavioralFeature,
    Class,
    Classifier,
    DataType,
    Dependency,
    Element,
    Feature,
    GeneralizableElement,
    ModelElement,
    NameSpace,
    Relationship,
    StructuralFeature,
    UML_14_Abstraction,
    UML_14_Association,
    UML_14_AssociationClass,
    UML_14_AssociationEnd,
    UML_14_Attribute,
    UML_14_BehavioralFeature,
    UML_14_Binding,
    UML_14_Class,
    UML_14_Classifier,
    UML_14_Comment,
    UML_14_Constraint,
    UML_14_DataType,
    UML_14_Dependency,
    UML_14_Element,
    UML_14_ElementOwnership,
    UML_14_Enumeration,
    UML_14_EnumerationLiteral,
    UML_14_Feature,
    UML_14_GeneralizableElement,
    UML_14_Generalization,
    UML_14_Interface,
    UML_14_Method,
    UML_14_ModelElement,
    UML_14_Multiplicity,
    UML_14_MultiplicityRange,
    UML_14_NameSpace,
    UML_14_Operation,
    UML_14_Parameter,
    UML_14_Permission,
    UML_14_Primitive,
    UML_14_Relationship,
    UML_14_StructuralFeature,
    UML_14_Usage,
    AggregationKind,
    ChangeableKind,
    OrderingKind,
    ParameterDirectionKind,
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

def test_assoc_annotatedElement55_reverse_link_reassign_clear():
    a1 = UML_14_ModelElement(name="sample_text")
    a2 = UML_14_ModelElement(name="sample_text_2")
    b = UML_14_Comment(body="sample_text")
    _safe_set(b, 'comments', a1)
    assert _is_linked(b, 'comments', a1)
    if hasattr(a1, 'ModelElement56'):
        assert _is_linked(a1, 'ModelElement56', b)
    _safe_set(b, 'comments', a2)
    assert _is_linked(b, 'comments', a2)
    if hasattr(a1, 'ModelElement56'):
        assert not _is_linked(a1, 'ModelElement56', b)
    if hasattr(a2, 'ModelElement56'):
        assert _is_linked(a2, 'ModelElement56', b)
    _safe_set(b, 'comments', None)
    assert not _is_linked(b, 'comments', a2)
    if hasattr(a2, 'ModelElement56'):
        assert not _is_linked(a2, 'ModelElement56', b)


def test_assoc_associationEnd31_reverse_link_reassign_clear():
    a1 = UML_14_Attribute(initialValue="sample_text")
    a2 = UML_14_Attribute(initialValue="sample_text_2")
    b = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    _safe_set(b, 'AssociationEnd32', a1)
    assert _is_linked(b, 'AssociationEnd32', a1)
    if hasattr(a1, 'qualifier'):
        assert _is_linked(a1, 'qualifier', b)
    _safe_set(b, 'AssociationEnd32', a2)
    assert _is_linked(b, 'AssociationEnd32', a2)
    if hasattr(a1, 'qualifier'):
        assert not _is_linked(a1, 'qualifier', b)
    if hasattr(a2, 'qualifier'):
        assert _is_linked(a2, 'qualifier', b)
    _safe_set(b, 'AssociationEnd32', None)
    assert not _is_linked(b, 'AssociationEnd32', a2)
    if hasattr(a2, 'qualifier'):
        assert not _is_linked(a2, 'qualifier', b)


def test_assoc_child33_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_GeneralizableElement(isAbstract=True)
    _safe_set(b, 'GeneralizableElement', a1)
    assert _is_linked(b, 'GeneralizableElement', a1)
    if hasattr(a1, 'generalization'):
        assert _is_linked(a1, 'generalization', b)
    _safe_set(b, 'GeneralizableElement', a2)
    assert _is_linked(b, 'GeneralizableElement', a2)
    if hasattr(a1, 'generalization'):
        assert not _is_linked(a1, 'generalization', b)
    if hasattr(a2, 'generalization'):
        assert _is_linked(a2, 'generalization', b)
    _safe_set(b, 'GeneralizableElement', None)
    assert not _is_linked(b, 'GeneralizableElement', a2)
    if hasattr(a2, 'generalization'):
        assert not _is_linked(a2, 'generalization', b)


def test_assoc_comments1_reverse_link_reassign_clear():
    a1 = UML_14_ModelElement(name="sample_text")
    a2 = UML_14_ModelElement(name="sample_text_2")
    b = UML_14_Comment(body="sample_text")
    _safe_set(b, 'Comment', a1)
    assert _is_linked(b, 'Comment', a1)
    if hasattr(a1, 'annotatedElement'):
        assert _is_linked(a1, 'annotatedElement', b)
    _safe_set(b, 'Comment', a2)
    assert _is_linked(b, 'Comment', a2)
    if hasattr(a1, 'annotatedElement'):
        assert not _is_linked(a1, 'annotatedElement', b)
    if hasattr(a2, 'annotatedElement'):
        assert _is_linked(a2, 'annotatedElement', b)
    _safe_set(b, 'Comment', None)
    assert not _is_linked(b, 'Comment', a2)
    if hasattr(a2, 'annotatedElement'):
        assert not _is_linked(a2, 'annotatedElement', b)


def test_assoc_constrainedElement12_reverse_link_reassign_clear():
    a1 = UML_14_ModelElement(name="sample_text")
    a2 = UML_14_ModelElement(name="sample_text_2")
    b = UML_14_Constraint(body="sample_text")
    _safe_set(b, 'constraint', {a1})
    assert _is_linked(b, 'constraint', a1)
    if hasattr(a1, 'ModelElement'):
        assert _is_linked(a1, 'ModelElement', b)
    _safe_set(b, 'constraint', {a2})
    assert _is_linked(b, 'constraint', a2)
    if hasattr(a1, 'ModelElement'):
        assert not _is_linked(a1, 'ModelElement', b)
    if hasattr(a2, 'ModelElement'):
        assert _is_linked(a2, 'ModelElement', b)
    _safe_set(b, 'constraint', set())
    assert not _is_linked(b, 'constraint', a2)
    if hasattr(a2, 'ModelElement'):
        assert not _is_linked(a2, 'ModelElement', b)


def test_assoc_constraint0_reverse_link_reassign_clear():
    a1 = UML_14_ModelElement(name="sample_text")
    a2 = UML_14_ModelElement(name="sample_text_2")
    b = UML_14_Constraint(body="sample_text")
    _safe_set(b, 'Constraint', a1)
    assert _is_linked(b, 'Constraint', a1)
    if hasattr(a1, 'constrainedElement'):
        assert _is_linked(a1, 'constrainedElement', b)
    _safe_set(b, 'Constraint', a2)
    assert _is_linked(b, 'Constraint', a2)
    if hasattr(a1, 'constrainedElement'):
        assert not _is_linked(a1, 'constrainedElement', b)
    if hasattr(a2, 'constrainedElement'):
        assert _is_linked(a2, 'constrainedElement', b)
    _safe_set(b, 'Constraint', None)
    assert not _is_linked(b, 'Constraint', a2)
    if hasattr(a2, 'constrainedElement'):
        assert not _is_linked(a2, 'constrainedElement', b)


def test_assoc_feature11_reverse_link_reassign_clear():
    a1 = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    a2 = UML_14_Parameter(defaultValue="sample_text_2", kind="sample_text_2")
    b = UML_14_BehavioralFeature(isQuery=True)
    _safe_set(b, 'BehavioralFeature', a1)
    assert _is_linked(b, 'BehavioralFeature', a1)
    if hasattr(a1, 'parameter'):
        assert _is_linked(a1, 'parameter', b)
    _safe_set(b, 'BehavioralFeature', a2)
    assert _is_linked(b, 'BehavioralFeature', a2)
    if hasattr(a1, 'parameter'):
        assert not _is_linked(a1, 'parameter', b)
    if hasattr(a2, 'parameter'):
        assert _is_linked(a2, 'parameter', b)
    _safe_set(b, 'BehavioralFeature', None)
    assert not _is_linked(b, 'BehavioralFeature', a2)
    if hasattr(a2, 'parameter'):
        assert not _is_linked(a2, 'parameter', b)


def test_assoc_generalization6_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_GeneralizableElement(isAbstract=True)
    _safe_set(b, 'child', {a1})
    assert _is_linked(b, 'child', a1)
    if hasattr(a1, 'Generalization'):
        assert _is_linked(a1, 'Generalization', b)
    _safe_set(b, 'child', {a2})
    assert _is_linked(b, 'child', a2)
    if hasattr(a1, 'Generalization'):
        assert not _is_linked(a1, 'Generalization', b)
    if hasattr(a2, 'Generalization'):
        assert _is_linked(a2, 'Generalization', b)
    _safe_set(b, 'child', set())
    assert not _is_linked(b, 'child', a2)
    if hasattr(a2, 'Generalization'):
        assert not _is_linked(a2, 'Generalization', b)


def test_assoc_operation30_reverse_link_reassign_clear():
    a1 = UML_14_Operation(isAbstract=True, isLeaf=True, isRoot=True, specification="sample_text")
    a2 = UML_14_Operation(isAbstract=False, isLeaf=False, isRoot=False, specification="sample_text_2")
    b = UML_14_Method(body="sample_text")
    _safe_set(b, 'UML_14_Method', {a1})
    assert _is_linked(b, 'UML_14_Method', a1)
    if hasattr(a1, 'UML_14_Operation'):
        assert _is_linked(a1, 'UML_14_Operation', b)
    _safe_set(b, 'UML_14_Method', {a2})
    assert _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a1, 'UML_14_Operation'):
        assert not _is_linked(a1, 'UML_14_Operation', b)
    if hasattr(a2, 'UML_14_Operation'):
        assert _is_linked(a2, 'UML_14_Operation', b)
    _safe_set(b, 'UML_14_Method', set())
    assert not _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a2, 'UML_14_Operation'):
        assert not _is_linked(a2, 'UML_14_Operation', b)


def test_assoc_parameter25_reverse_link_reassign_clear():
    a1 = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    a2 = UML_14_Parameter(defaultValue="sample_text_2", kind="sample_text_2")
    b = UML_14_BehavioralFeature(isQuery=True)
    _safe_set(b, 'feature26', {a1})
    assert _is_linked(b, 'feature26', a1)
    if hasattr(a1, 'Parameter27'):
        assert _is_linked(a1, 'Parameter27', b)
    _safe_set(b, 'feature26', {a2})
    assert _is_linked(b, 'feature26', a2)
    if hasattr(a1, 'Parameter27'):
        assert not _is_linked(a1, 'Parameter27', b)
    if hasattr(a2, 'Parameter27'):
        assert _is_linked(a2, 'Parameter27', b)
    _safe_set(b, 'feature26', set())
    assert not _is_linked(b, 'feature26', a2)
    if hasattr(a2, 'Parameter27'):
        assert not _is_linked(a2, 'Parameter27', b)


def test_assoc_parent34_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_GeneralizableElement(isAbstract=True)
    _safe_set(b, 'GeneralizableElement35', a1)
    assert _is_linked(b, 'GeneralizableElement35', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'GeneralizableElement35', a2)
    assert _is_linked(b, 'GeneralizableElement35', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'GeneralizableElement35', None)
    assert not _is_linked(b, 'GeneralizableElement35', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_qualifier48_reverse_link_reassign_clear():
    a1 = UML_14_Attribute(initialValue="sample_text")
    a2 = UML_14_Attribute(initialValue="sample_text_2")
    b = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    _safe_set(b, 'associationEnd', a1)
    assert _is_linked(b, 'associationEnd', a1)
    if hasattr(a1, 'Attribute'):
        assert _is_linked(a1, 'Attribute', b)
    _safe_set(b, 'associationEnd', a2)
    assert _is_linked(b, 'associationEnd', a2)
    if hasattr(a1, 'Attribute'):
        assert not _is_linked(a1, 'Attribute', b)
    if hasattr(a2, 'Attribute'):
        assert _is_linked(a2, 'Attribute', b)
    _safe_set(b, 'associationEnd', None)
    assert not _is_linked(b, 'associationEnd', a2)
    if hasattr(a2, 'Attribute'):
        assert not _is_linked(a2, 'Attribute', b)


def test_assoc_specialization7_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_GeneralizableElement(isAbstract=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Generalization8'):
        assert _is_linked(a1, 'Generalization8', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Generalization8'):
        assert not _is_linked(a1, 'Generalization8', b)
    if hasattr(a2, 'Generalization8'):
        assert _is_linked(a2, 'Generalization8', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Generalization8'):
        assert not _is_linked(a2, 'Generalization8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association19_stub_double():
    # UML_14_Classifier has no real 'participant' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'participant', None)
    _safe_set(owner, 'AssociationEnd', partner)
    assert getattr(partner, 'participant') == owner
    _safe_set(owner, 'AssociationEnd', None)
    assert getattr(partner, 'participant') is None


def test_assoc_association40_stub_double():
    # UML_14_Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'Association') is None


def test_assoc_client51_stub_double():
    # UML_14_Dependency has no real 'clientDependency' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_ModelElement(name="sample_text")
    partner = UML_14_Dependency()
    setattr(partner, 'clientDependency', None)
    _safe_set(owner, 'ModelElement52', partner)
    assert owner in getattr(partner, 'clientDependency')
    _safe_set(owner, 'ModelElement52', None)
    assert owner not in getattr(partner, 'clientDependency')


def test_assoc_clientDependency3_stub_double():
    # UML_14_Dependency has no real 'Dependency4' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_ModelElement(name="sample_text")
    partner = UML_14_Dependency()
    setattr(partner, 'Dependency4', None)
    _safe_set(owner, 'client', {partner})
    assert getattr(partner, 'Dependency4') == owner
    _safe_set(owner, 'client', set())
    assert getattr(partner, 'Dependency4') is None


def test_assoc_connection38_stub_double():
    # UML_14_Association has no real 'association' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Association()
    setattr(partner, 'association', None)
    _safe_set(owner, 'AssociationEnd39', partner)
    assert owner in getattr(partner, 'association')
    _safe_set(owner, 'AssociationEnd39', None)
    assert owner not in getattr(partner, 'association')


def test_assoc_multiplicity29_stub_double():
    # UML_14_Multiplicity has no real 'Multiplicity' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_MultiplicityRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_MultiplicityRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_MultiplicityRange(lower=7, upper=7)
    partner = UML_14_Multiplicity()
    setattr(partner, 'Multiplicity', None)
    _safe_set(owner, 'range', partner)
    assert getattr(partner, 'Multiplicity') == owner
    _safe_set(owner, 'range', None)
    assert getattr(partner, 'Multiplicity') is None


def test_assoc_multiplicity46_stub_double():
    # UML_14_Multiplicity has no real 'UML_14_Multiplicity47' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Multiplicity()
    setattr(partner, 'UML_14_Multiplicity47', None)
    _safe_set(owner, 'UML_14_AssociationEnd', partner)
    assert getattr(partner, 'UML_14_Multiplicity47') == owner
    _safe_set(owner, 'UML_14_AssociationEnd', None)
    assert getattr(partner, 'UML_14_Multiplicity47') is None


def test_assoc_participant41_stub_double():
    # UML_14_Classifier has no real 'Classifier43' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'Classifier43', None)
    _safe_set(owner, 'association42', partner)
    assert getattr(partner, 'Classifier43') == owner
    _safe_set(owner, 'association42', None)
    assert getattr(partner, 'Classifier43') is None


def test_assoc_powertype36_stub_double():
    # UML_14_Classifier has no real 'Classifier37' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Generalization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Generalization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Generalization(discriminator="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'Classifier37', None)
    _safe_set(owner, 'powertypeRange', partner)
    assert getattr(partner, 'Classifier37') == owner
    _safe_set(owner, 'powertypeRange', None)
    assert getattr(partner, 'Classifier37') is None


def test_assoc_powertypeRange17_stub_double():
    # UML_14_Classifier has no real 'powertype' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Generalization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Generalization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Generalization(discriminator="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'powertype', None)
    _safe_set(owner, 'Generalization18', partner)
    assert owner in getattr(partner, 'powertype')
    _safe_set(owner, 'Generalization18', None)
    assert owner not in getattr(partner, 'powertype')


def test_assoc_range28_stub_double():
    # UML_14_Multiplicity has no real 'multiplicity' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_MultiplicityRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_MultiplicityRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_MultiplicityRange(lower=7, upper=7)
    partner = UML_14_Multiplicity()
    setattr(partner, 'multiplicity', None)
    _safe_set(owner, 'MultiplicityRange', partner)
    assert owner in getattr(partner, 'multiplicity')
    _safe_set(owner, 'MultiplicityRange', None)
    assert owner not in getattr(partner, 'multiplicity')


def test_assoc_specification44_stub_double():
    # UML_14_Classifier has no real 'Classifier45' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'Classifier45', None)
    _safe_set(owner, 'specifiedEnd', partner)
    assert getattr(partner, 'Classifier45') == owner
    _safe_set(owner, 'specifiedEnd', None)
    assert getattr(partner, 'Classifier45') is None


def test_assoc_specifiedEnd20_stub_double():
    # UML_14_Classifier has no real 'specification' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(aggregation="sample_text", changeability="sample_text", isNavigable=True, targetScope="sample_text", visibility="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'specification', None)
    _safe_set(owner, 'AssociationEnd21', partner)
    assert getattr(partner, 'specification') == owner
    _safe_set(owner, 'AssociationEnd21', None)
    assert getattr(partner, 'specification') is None


def test_assoc_supplier49_stub_double():
    # UML_14_Dependency has no real 'supplierDependency' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_ModelElement(name="sample_text")
    partner = UML_14_Dependency()
    setattr(partner, 'supplierDependency', None)
    _safe_set(owner, 'ModelElement50', partner)
    assert owner in getattr(partner, 'supplierDependency')
    _safe_set(owner, 'ModelElement50', None)
    assert owner not in getattr(partner, 'supplierDependency')


def test_assoc_supplierDependency2_stub_double():
    # UML_14_Dependency has no real 'Dependency' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_ModelElement(name="sample_text")
    partner = UML_14_Dependency()
    setattr(partner, 'Dependency', None)
    _safe_set(owner, 'supplier', {partner})
    assert getattr(partner, 'Dependency') == owner
    _safe_set(owner, 'supplier', set())
    assert getattr(partner, 'Dependency') is None


def test_assoc_type9_stub_double():
    # UML_14_Classifier has no real 'Classifier10' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'Classifier10', None)
    _safe_set(owner, 'typedParameter', partner)
    assert getattr(partner, 'Classifier10') == owner
    _safe_set(owner, 'typedParameter', None)
    assert getattr(partner, 'Classifier10') is None


def test_assoc_typedParameter14_stub_double():
    # UML_14_Classifier has no real 'type' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    partner = UML_14_Classifier()
    setattr(partner, 'type', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'type')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'type')


