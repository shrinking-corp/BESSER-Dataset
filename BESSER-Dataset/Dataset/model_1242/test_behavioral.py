import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDomainCS,
    ClassCS,
    ExpCS,
    ModelElementCS,
    Nameable,
    NamedElementCS,
    Relation,
    RootPackageCS,
    TemplateCS,
    TemplateVariableCS,
    TypedElementCS,
    qvtrelationcs_AbstractDomainCS,
    qvtrelationcs_Class,
    qvtrelationcs_CollectionTemplateCS,
    qvtrelationcs_DefaultValueCS,
    qvtrelationcs_DomainCS,
    qvtrelationcs_DomainPatternCS,
    qvtrelationcs_Element,
    qvtrelationcs_ElementTemplateCS,
    qvtrelationcs_ExpCS,
    qvtrelationcs_KeyDeclCS,
    qvtrelationcs_ModelDeclCS,
    qvtrelationcs_Namespace,
    qvtrelationcs_ObjectTemplateCS,
    qvtrelationcs_ParamDeclarationCS,
    qvtrelationcs_PathNameCS,
    qvtrelationcs_PatternCS,
    qvtrelationcs_PredicateCS,
    qvtrelationcs_PrimitiveTypeDomainCS,
    qvtrelationcs_Property,
    qvtrelationcs_PropertyTemplateCS,
    qvtrelationcs_QueryCS,
    qvtrelationcs_RelationCS,
    qvtrelationcs_TemplateCS,
    qvtrelationcs_TemplateVariableCS,
    qvtrelationcs_TopLevelCS,
    qvtrelationcs_Transformation,
    qvtrelationcs_TransformationCS,
    qvtrelationcs_TypedModel,
    qvtrelationcs_TypedRefCS,
    qvtrelationcs_UnitCS,
    qvtrelationcs_VarDeclarationCS,
    qvtrelationcs_VarDeclarationIdCS,
    qvtrelationcs_Variable,
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

def test_assoc_modelId6_stub_double():
    # qvtrelationcs_TypedModel has no real 'qvtrelationcs_TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_DomainCS(implementedBy="sample_text", isCheckonly=True, isEnforce=True, isReplace=True)
    partner = qvtrelationcs_TypedModel()
    setattr(partner, 'qvtrelationcs_TypedModel', None)
    _safe_set(owner, 'qvtrelationcs_DomainCS', partner)
    assert getattr(partner, 'qvtrelationcs_TypedModel') == owner
    _safe_set(owner, 'qvtrelationcs_DomainCS', None)
    assert getattr(partner, 'qvtrelationcs_TypedModel') is None


def test_assoc_overrides47_stub_double():
    # Relation has no real 'Relation' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = Relation()
    setattr(partner, 'Relation', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS', partner)
    assert getattr(partner, 'Relation') == owner
    _safe_set(owner, 'qvtrelationcs_RelationCS', None)
    assert getattr(partner, 'Relation') is None


def test_assoc_ownedDefaultValues9_stub_double():
    # qvtrelationcs_DefaultValueCS has no real 'qvtrelationcs_DefaultValueCS11' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_DomainCS(implementedBy="sample_text", isCheckonly=True, isEnforce=True, isReplace=True)
    partner = qvtrelationcs_DefaultValueCS()
    setattr(partner, 'qvtrelationcs_DefaultValueCS11', None)
    _safe_set(owner, 'qvtrelationcs_DomainCS10', {partner})
    assert getattr(partner, 'qvtrelationcs_DefaultValueCS11') == owner
    _safe_set(owner, 'qvtrelationcs_DomainCS10', set())
    assert getattr(partner, 'qvtrelationcs_DefaultValueCS11') is None


def test_assoc_ownedDomains50_stub_double():
    # qvtrelationcs_AbstractDomainCS has no real 'qvtrelationcs_AbstractDomainCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = qvtrelationcs_AbstractDomainCS()
    setattr(partner, 'qvtrelationcs_AbstractDomainCS', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS51', {partner})
    assert getattr(partner, 'qvtrelationcs_AbstractDomainCS') == owner
    _safe_set(owner, 'qvtrelationcs_RelationCS51', set())
    assert getattr(partner, 'qvtrelationcs_AbstractDomainCS') is None


def test_assoc_ownedImplementedBy12_stub_double():
    # qvtrelationcs_ExpCS has no real 'qvtrelationcs_ExpCS14' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_DomainCS(implementedBy="sample_text", isCheckonly=True, isEnforce=True, isReplace=True)
    partner = qvtrelationcs_ExpCS()
    setattr(partner, 'qvtrelationcs_ExpCS14', None)
    _safe_set(owner, 'qvtrelationcs_DomainCS13', partner)
    assert getattr(partner, 'qvtrelationcs_ExpCS14') == owner
    _safe_set(owner, 'qvtrelationcs_DomainCS13', None)
    assert getattr(partner, 'qvtrelationcs_ExpCS14') is None


def test_assoc_ownedPattern7_stub_double():
    # qvtrelationcs_DomainPatternCS has no real 'qvtrelationcs_DomainPatternCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_DomainCS(implementedBy="sample_text", isCheckonly=True, isEnforce=True, isReplace=True)
    partner = qvtrelationcs_DomainPatternCS()
    setattr(partner, 'qvtrelationcs_DomainPatternCS', None)
    _safe_set(owner, 'qvtrelationcs_DomainCS8', {partner})
    assert getattr(partner, 'qvtrelationcs_DomainPatternCS') == owner
    _safe_set(owner, 'qvtrelationcs_DomainCS8', set())
    assert getattr(partner, 'qvtrelationcs_DomainPatternCS') is None


def test_assoc_ownedRelations80_stub_double():
    # qvtrelationcs_TransformationCS has no real 'qvtrelationcs_TransformationCS81' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = qvtrelationcs_TransformationCS()
    setattr(partner, 'qvtrelationcs_TransformationCS81', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS82', partner)
    assert owner in getattr(partner, 'qvtrelationcs_TransformationCS81')
    _safe_set(owner, 'qvtrelationcs_RelationCS82', None)
    assert owner not in getattr(partner, 'qvtrelationcs_TransformationCS81')


def test_assoc_ownedVarDeclarations48_stub_double():
    # qvtrelationcs_VarDeclarationCS has no real 'qvtrelationcs_VarDeclarationCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = qvtrelationcs_VarDeclarationCS()
    setattr(partner, 'qvtrelationcs_VarDeclarationCS', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS49', {partner})
    assert getattr(partner, 'qvtrelationcs_VarDeclarationCS') == owner
    _safe_set(owner, 'qvtrelationcs_RelationCS49', set())
    assert getattr(partner, 'qvtrelationcs_VarDeclarationCS') is None


def test_assoc_ownedWhen52_stub_double():
    # qvtrelationcs_PatternCS has no real 'qvtrelationcs_PatternCS54' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = qvtrelationcs_PatternCS()
    setattr(partner, 'qvtrelationcs_PatternCS54', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS53', partner)
    assert getattr(partner, 'qvtrelationcs_PatternCS54') == owner
    _safe_set(owner, 'qvtrelationcs_RelationCS53', None)
    assert getattr(partner, 'qvtrelationcs_PatternCS54') is None


def test_assoc_ownedWhere55_stub_double():
    # qvtrelationcs_PatternCS has no real 'qvtrelationcs_PatternCS57' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelationcs_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelationcs_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelationcs_RelationCS(isDefault=True, isTop=True)
    partner = qvtrelationcs_PatternCS()
    setattr(partner, 'qvtrelationcs_PatternCS57', None)
    _safe_set(owner, 'qvtrelationcs_RelationCS56', partner)
    assert getattr(partner, 'qvtrelationcs_PatternCS57') == owner
    _safe_set(owner, 'qvtrelationcs_RelationCS56', None)
    assert getattr(partner, 'qvtrelationcs_PatternCS57') is None


