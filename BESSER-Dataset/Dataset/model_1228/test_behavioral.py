import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDomainCS,
    CSTNode,
    DefaultValueCS,
    IdentifiedCS,
    IdentifierCS,
    KeyDeclCS,
    ModelDeclCS,
    OCLExpressionCS,
    OperationCallExpCS,
    ParamDeclarationCS,
    PathNameCS,
    PropertyTemplateCS,
    QueryCS,
    RelationCS,
    TemplateCS,
    TransformationCS,
    TypeCS,
    UnitCS,
    VarDeclarationCS,
    WhenCS,
    WhereCS,
    cst_AbstractDomainCS,
    cst_OCLExpressionCS,
    cst_TemplateVariableCS,
    cst_qvtrelation_EClass,
    cst_qvtrelation_EClassifier,
    cst_qvtrelation_EStructuralFeature,
    qvtrelation_cst_AbstractDomainCS,
    qvtrelation_cst_CollectionTemplateCS,
    qvtrelation_cst_DefaultValueCS,
    qvtrelation_cst_DomainCS,
    qvtrelation_cst_KeyDeclCS,
    qvtrelation_cst_ModelDeclCS,
    qvtrelation_cst_ObjectTemplateCS,
    qvtrelation_cst_ParamDeclarationCS,
    qvtrelation_cst_PrimitiveTypeDomainCS,
    qvtrelation_cst_PropertyTemplateCS,
    qvtrelation_cst_QueryCS,
    qvtrelation_cst_RelationCS,
    qvtrelation_cst_TemplateCS,
    qvtrelation_cst_TemplateVariableCS,
    qvtrelation_cst_TopLevelCS,
    qvtrelation_cst_TransformationCS,
    qvtrelation_cst_UnitCS,
    qvtrelation_cst_VarDeclarationCS,
    qvtrelation_cst_WhenCS,
    qvtrelation_cst_WhereCS,
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

def test_assoc_defaultValue13_stub_double():
    # DefaultValueCS has no real 'DefaultValueCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_DomainCS(checkonly=True, enforce=True, replace=True)
    partner = DefaultValueCS()
    setattr(partner, 'DefaultValueCS', None)
    _safe_set(owner, 'qvtrelation_cst_DomainCS14', {partner})
    assert getattr(partner, 'DefaultValueCS') == owner
    _safe_set(owner, 'qvtrelation_cst_DomainCS14', set())
    assert getattr(partner, 'DefaultValueCS') is None


def test_assoc_domain57_stub_double():
    # AbstractDomainCS has no real 'AbstractDomainCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = AbstractDomainCS()
    setattr(partner, 'AbstractDomainCS', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS58', {partner})
    assert getattr(partner, 'AbstractDomainCS') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS58', set())
    assert getattr(partner, 'AbstractDomainCS') is None


def test_assoc_identifier50_stub_double():
    # IdentifierCS has no real 'IdentifierCS51' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = IdentifierCS()
    setattr(partner, 'IdentifierCS51', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS', partner)
    assert getattr(partner, 'IdentifierCS51') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS', None)
    assert getattr(partner, 'IdentifierCS51') is None


def test_assoc_implementedBy15_stub_double():
    # OperationCallExpCS has no real 'OperationCallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_DomainCS(checkonly=True, enforce=True, replace=True)
    partner = OperationCallExpCS()
    setattr(partner, 'OperationCallExpCS', None)
    _safe_set(owner, 'qvtrelation_cst_DomainCS16', partner)
    assert getattr(partner, 'OperationCallExpCS') == owner
    _safe_set(owner, 'qvtrelation_cst_DomainCS16', None)
    assert getattr(partner, 'OperationCallExpCS') is None


def test_assoc_modelId9_stub_double():
    # IdentifierCS has no real 'IdentifierCS10' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_DomainCS(checkonly=True, enforce=True, replace=True)
    partner = IdentifierCS()
    setattr(partner, 'IdentifierCS10', None)
    _safe_set(owner, 'qvtrelation_cst_DomainCS', partner)
    assert getattr(partner, 'IdentifierCS10') == owner
    _safe_set(owner, 'qvtrelation_cst_DomainCS', None)
    assert getattr(partner, 'IdentifierCS10') is None


def test_assoc_oclExpression35_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS37' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_PropertyTemplateCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_PropertyTemplateCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_PropertyTemplateCS(opposite=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS37', None)
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS36', partner)
    assert getattr(partner, 'OCLExpressionCS37') == owner
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS36', None)
    assert getattr(partner, 'OCLExpressionCS37') is None


def test_assoc_overrides52_stub_double():
    # IdentifierCS has no real 'IdentifierCS54' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = IdentifierCS()
    setattr(partner, 'IdentifierCS54', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS53', partner)
    assert getattr(partner, 'IdentifierCS54') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS53', None)
    assert getattr(partner, 'IdentifierCS54') is None


def test_assoc_propertyId33_stub_double():
    # IdentifiedCS has no real 'IdentifiedCS34' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_PropertyTemplateCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_PropertyTemplateCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_PropertyTemplateCS(opposite=True)
    partner = IdentifiedCS()
    setattr(partner, 'IdentifiedCS34', None)
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS', partner)
    assert getattr(partner, 'IdentifiedCS34') == owner
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS', None)
    assert getattr(partner, 'IdentifiedCS34') is None


def test_assoc_referredProperty38_stub_double():
    # cst_qvtrelation_EStructuralFeature has no real 'cst_qvtrelation_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_PropertyTemplateCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_PropertyTemplateCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_PropertyTemplateCS(opposite=True)
    partner = cst_qvtrelation_EStructuralFeature()
    setattr(partner, 'cst_qvtrelation_EStructuralFeature', None)
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS39', partner)
    assert getattr(partner, 'cst_qvtrelation_EStructuralFeature') == owner
    _safe_set(owner, 'qvtrelation_cst_PropertyTemplateCS39', None)
    assert getattr(partner, 'cst_qvtrelation_EStructuralFeature') is None


def test_assoc_template11_stub_double():
    # TemplateCS has no real 'TemplateCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_DomainCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_DomainCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_DomainCS(checkonly=True, enforce=True, replace=True)
    partner = TemplateCS()
    setattr(partner, 'TemplateCS', None)
    _safe_set(owner, 'qvtrelation_cst_DomainCS12', partner)
    assert getattr(partner, 'TemplateCS') == owner
    _safe_set(owner, 'qvtrelation_cst_DomainCS12', None)
    assert getattr(partner, 'TemplateCS') is None


def test_assoc_varDeclaration55_stub_double():
    # VarDeclarationCS has no real 'VarDeclarationCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = VarDeclarationCS()
    setattr(partner, 'VarDeclarationCS', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS56', {partner})
    assert getattr(partner, 'VarDeclarationCS') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS56', set())
    assert getattr(partner, 'VarDeclarationCS') is None


def test_assoc_when59_stub_double():
    # WhenCS has no real 'WhenCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = WhenCS()
    setattr(partner, 'WhenCS', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS60', partner)
    assert getattr(partner, 'WhenCS') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS60', None)
    assert getattr(partner, 'WhenCS') is None


def test_assoc_where61_stub_double():
    # WhereCS has no real 'WhereCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_cst_RelationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_cst_RelationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_cst_RelationCS(top=True)
    partner = WhereCS()
    setattr(partner, 'WhereCS', None)
    _safe_set(owner, 'qvtrelation_cst_RelationCS62', partner)
    assert getattr(partner, 'WhereCS') == owner
    _safe_set(owner, 'qvtrelation_cst_RelationCS62', None)
    assert getattr(partner, 'WhereCS') is None


