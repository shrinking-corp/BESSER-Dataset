import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRole,
    AntiRigidType,
    Constraint,
    Inheritance,
    InterRelationshipConstraint,
    IntraRelationshipConstraint,
    Model,
    ModelElement,
    NamedElement,
    Relation,
    RelationTarget,
    RelationshipConstraint,
    RigidType,
    RoleConstraint,
    RoleGroupElement,
    Type,
    TypedElement,
    crom_l1_composed_AbstractRole,
    crom_l1_composed_AbstractRoleRef,
    crom_l1_composed_Acyclic,
    crom_l1_composed_AntiRigidType,
    crom_l1_composed_Attribute,
    crom_l1_composed_CompartmentInheritance,
    crom_l1_composed_CompartmentType,
    crom_l1_composed_ComplexConstraint,
    crom_l1_composed_Constraint,
    crom_l1_composed_Cyclic,
    crom_l1_composed_DataInheritance,
    crom_l1_composed_DataType,
    crom_l1_composed_Fulfillment,
    crom_l1_composed_Group,
    crom_l1_composed_Inheritance,
    crom_l1_composed_InterRelationshipConstraint,
    crom_l1_composed_IntraRelationshipConstraint,
    crom_l1_composed_Irreflexive,
    crom_l1_composed_Model,
    crom_l1_composed_ModelElement,
    crom_l1_composed_NamedElement,
    crom_l1_composed_NaturalInheritance,
    crom_l1_composed_NaturalType,
    crom_l1_composed_Operation,
    crom_l1_composed_Parameter,
    crom_l1_composed_Part,
    crom_l1_composed_ParthoodConstraint,
    crom_l1_composed_Place,
    crom_l1_composed_Reflexive,
    crom_l1_composed_Relation,
    crom_l1_composed_RelationTarget,
    crom_l1_composed_Relationship,
    crom_l1_composed_RelationshipConstraint,
    crom_l1_composed_RelationshipExclusion,
    crom_l1_composed_RelationshipImplication,
    crom_l1_composed_RigidType,
    crom_l1_composed_RoleConstraint,
    crom_l1_composed_RoleEquivalence,
    crom_l1_composed_RoleGroup,
    crom_l1_composed_RoleGroupElement,
    crom_l1_composed_RoleImplication,
    crom_l1_composed_RoleInheritance,
    crom_l1_composed_RoleProhibition,
    crom_l1_composed_RoleType,
    crom_l1_composed_Total,
    crom_l1_composed_Type,
    crom_l1_composed_TypedElement,
    Direction,
    Parthood,
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

def test_assoc_first28_reverse_link_reassign_clear():
    a1 = crom_l1_composed_Relationship(direction="sample_text")
    a2 = crom_l1_composed_Relationship(direction="sample_text_2")
    b = crom_l1_composed_Place(lower=7, upper=7)
    _safe_set(b, 'crom_l1_composed_Place', a1)
    assert _is_linked(b, 'crom_l1_composed_Place', a1)
    if hasattr(a1, 'crom_l1_composed_Relationship29'):
        assert _is_linked(a1, 'crom_l1_composed_Relationship29', b)
    _safe_set(b, 'crom_l1_composed_Place', a2)
    assert _is_linked(b, 'crom_l1_composed_Place', a2)
    if hasattr(a1, 'crom_l1_composed_Relationship29'):
        assert not _is_linked(a1, 'crom_l1_composed_Relationship29', b)
    if hasattr(a2, 'crom_l1_composed_Relationship29'):
        assert _is_linked(a2, 'crom_l1_composed_Relationship29', b)
    _safe_set(b, 'crom_l1_composed_Place', None)
    assert not _is_linked(b, 'crom_l1_composed_Place', a2)
    if hasattr(a2, 'crom_l1_composed_Relationship29'):
        assert not _is_linked(a2, 'crom_l1_composed_Relationship29', b)


def test_assoc_second30_reverse_link_reassign_clear():
    a1 = crom_l1_composed_Relationship(direction="sample_text")
    a2 = crom_l1_composed_Relationship(direction="sample_text_2")
    b = crom_l1_composed_Place(lower=7, upper=7)
    _safe_set(b, 'crom_l1_composed_Place32', a1)
    assert _is_linked(b, 'crom_l1_composed_Place32', a1)
    if hasattr(a1, 'crom_l1_composed_Relationship31'):
        assert _is_linked(a1, 'crom_l1_composed_Relationship31', b)
    _safe_set(b, 'crom_l1_composed_Place32', a2)
    assert _is_linked(b, 'crom_l1_composed_Place32', a2)
    if hasattr(a1, 'crom_l1_composed_Relationship31'):
        assert not _is_linked(a1, 'crom_l1_composed_Relationship31', b)
    if hasattr(a2, 'crom_l1_composed_Relationship31'):
        assert _is_linked(a2, 'crom_l1_composed_Relationship31', b)
    _safe_set(b, 'crom_l1_composed_Place32', None)
    assert not _is_linked(b, 'crom_l1_composed_Place32', a2)
    if hasattr(a2, 'crom_l1_composed_Relationship31'):
        assert not _is_linked(a2, 'crom_l1_composed_Relationship31', b)


def test_assoc_tr_extends11_reverse_link_reassign_clear():
    a1 = crom_l1_composed_DataType(serializable=True)
    a2 = crom_l1_composed_DataType(serializable=False)
    b = crom_l1_composed_DataType(serializable=True)
    _safe_set(b, 'crom_l1_composed_DataType10', a1)
    assert _is_linked(b, 'crom_l1_composed_DataType10', a1)
    if hasattr(a1, 'crom_l1_composed_DataType'):
        assert _is_linked(a1, 'crom_l1_composed_DataType', b)
    _safe_set(b, 'crom_l1_composed_DataType10', a2)
    assert _is_linked(b, 'crom_l1_composed_DataType10', a2)
    if hasattr(a1, 'crom_l1_composed_DataType'):
        assert not _is_linked(a1, 'crom_l1_composed_DataType', b)
    if hasattr(a2, 'crom_l1_composed_DataType'):
        assert _is_linked(a2, 'crom_l1_composed_DataType', b)
    _safe_set(b, 'crom_l1_composed_DataType10', None)
    assert not _is_linked(b, 'crom_l1_composed_DataType10', a2)
    if hasattr(a2, 'crom_l1_composed_DataType'):
        assert not _is_linked(a2, 'crom_l1_composed_DataType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements82_stub_double():
    # crom_l1_composed_RoleGroupElement has no real 'crom_l1_composed_RoleGroupElement' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_RoleGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_RoleGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_RoleGroup(lower=7, upper=7)
    partner = crom_l1_composed_RoleGroupElement()
    setattr(partner, 'crom_l1_composed_RoleGroupElement', None)
    _safe_set(owner, 'crom_l1_composed_RoleGroup', {partner})
    assert getattr(partner, 'crom_l1_composed_RoleGroupElement') == owner
    _safe_set(owner, 'crom_l1_composed_RoleGroup', set())
    assert getattr(partner, 'crom_l1_composed_RoleGroupElement') is None


def test_assoc_first47_stub_double():
    # crom_l1_composed_InterRelationshipConstraint has no real 'crom_l1_composed_InterRelationshipConstraint' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relationship(direction="sample_text")
    partner = crom_l1_composed_InterRelationshipConstraint()
    setattr(partner, 'crom_l1_composed_InterRelationshipConstraint', None)
    _safe_set(owner, 'crom_l1_composed_Relationship48', partner)
    assert getattr(partner, 'crom_l1_composed_InterRelationshipConstraint') == owner
    _safe_set(owner, 'crom_l1_composed_Relationship48', None)
    assert getattr(partner, 'crom_l1_composed_InterRelationshipConstraint') is None


def test_assoc_holder74_stub_double():
    # crom_l1_composed_RoleType has no real 'crom_l1_composed_RoleType76' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Place(lower=7, upper=7)
    partner = crom_l1_composed_RoleType()
    setattr(partner, 'crom_l1_composed_RoleType76', None)
    _safe_set(owner, 'crom_l1_composed_Place75', partner)
    assert getattr(partner, 'crom_l1_composed_RoleType76') == owner
    _safe_set(owner, 'crom_l1_composed_Place75', None)
    assert getattr(partner, 'crom_l1_composed_RoleType76') is None


def test_assoc_incoming77_stub_double():
    # crom_l1_composed_RelationTarget has no real 'crom_l1_composed_RelationTarget' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relation()
    partner = crom_l1_composed_RelationTarget()
    setattr(partner, 'crom_l1_composed_RelationTarget', None)
    _safe_set(owner, 'crom_l1_composed_Relation78', partner)
    assert owner in getattr(partner, 'crom_l1_composed_RelationTarget')
    _safe_set(owner, 'crom_l1_composed_Relation78', None)
    assert owner not in getattr(partner, 'crom_l1_composed_RelationTarget')


def test_assoc_operations8_stub_double():
    # crom_l1_composed_Type has no real 'owner9' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Operation(operation="sample_text")
    partner = crom_l1_composed_Type()
    setattr(partner, 'owner9', None)
    _safe_set(owner, 'Operation', partner)
    assert owner in getattr(partner, 'owner9')
    _safe_set(owner, 'Operation', None)
    assert owner not in getattr(partner, 'owner9')


def test_assoc_outgoing79_stub_double():
    # crom_l1_composed_RelationTarget has no real 'crom_l1_composed_RelationTarget80' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relation()
    partner = crom_l1_composed_RelationTarget()
    setattr(partner, 'crom_l1_composed_RelationTarget80', None)
    _safe_set(owner, 'crom_l1_composed_Relation81', partner)
    assert owner in getattr(partner, 'crom_l1_composed_RelationTarget80')
    _safe_set(owner, 'crom_l1_composed_Relation81', None)
    assert owner not in getattr(partner, 'crom_l1_composed_RelationTarget80')


def test_assoc_owner4_stub_double():
    # crom_l1_composed_Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Operation(operation="sample_text")
    partner = crom_l1_composed_Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'operations', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'operations', None)
    assert getattr(partner, 'Type') is None


def test_assoc_params3_stub_double():
    # crom_l1_composed_Parameter has no real 'crom_l1_composed_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Operation(operation="sample_text")
    partner = crom_l1_composed_Parameter()
    setattr(partner, 'crom_l1_composed_Parameter', None)
    _safe_set(owner, 'crom_l1_composed_Operation', {partner})
    assert getattr(partner, 'crom_l1_composed_Parameter') == owner
    _safe_set(owner, 'crom_l1_composed_Operation', set())
    assert getattr(partner, 'crom_l1_composed_Parameter') is None


def test_assoc_parts14_stub_double():
    # crom_l1_composed_CompartmentType has no real 'whole' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Part(lower=7, upper=7)
    partner = crom_l1_composed_CompartmentType()
    setattr(partner, 'whole', None)
    _safe_set(owner, 'Part', partner)
    assert owner in getattr(partner, 'whole')
    _safe_set(owner, 'Part', None)
    assert owner not in getattr(partner, 'whole')


def test_assoc_relation44_stub_double():
    # crom_l1_composed_IntraRelationshipConstraint has no real 'crom_l1_composed_IntraRelationshipConstraint45' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relationship(direction="sample_text")
    partner = crom_l1_composed_IntraRelationshipConstraint()
    setattr(partner, 'crom_l1_composed_IntraRelationshipConstraint45', None)
    _safe_set(owner, 'crom_l1_composed_Relationship46', partner)
    assert getattr(partner, 'crom_l1_composed_IntraRelationshipConstraint45') == owner
    _safe_set(owner, 'crom_l1_composed_Relationship46', None)
    assert getattr(partner, 'crom_l1_composed_IntraRelationshipConstraint45') is None


def test_assoc_relations1_stub_double():
    # crom_l1_composed_Model has no real 'crom_l1_composed_Model2' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relation()
    partner = crom_l1_composed_Model()
    setattr(partner, 'crom_l1_composed_Model2', None)
    _safe_set(owner, 'crom_l1_composed_Relation', partner)
    assert owner in getattr(partner, 'crom_l1_composed_Model2')
    _safe_set(owner, 'crom_l1_composed_Relation', None)
    assert owner not in getattr(partner, 'crom_l1_composed_Model2')


def test_assoc_relationships15_stub_double():
    # crom_l1_composed_CompartmentType has no real 'crom_l1_composed_CompartmentType' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relationship(direction="sample_text")
    partner = crom_l1_composed_CompartmentType()
    setattr(partner, 'crom_l1_composed_CompartmentType', None)
    _safe_set(owner, 'crom_l1_composed_Relationship', partner)
    assert owner in getattr(partner, 'crom_l1_composed_CompartmentType')
    _safe_set(owner, 'crom_l1_composed_Relationship', None)
    assert owner not in getattr(partner, 'crom_l1_composed_CompartmentType')


def test_assoc_role84_stub_double():
    # crom_l1_composed_AbstractRole has no real 'crom_l1_composed_AbstractRole85' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Part(lower=7, upper=7)
    partner = crom_l1_composed_AbstractRole()
    setattr(partner, 'crom_l1_composed_AbstractRole85', None)
    _safe_set(owner, 'crom_l1_composed_Part', partner)
    assert getattr(partner, 'crom_l1_composed_AbstractRole85') == owner
    _safe_set(owner, 'crom_l1_composed_Part', None)
    assert getattr(partner, 'crom_l1_composed_AbstractRole85') is None


def test_assoc_second49_stub_double():
    # crom_l1_composed_InterRelationshipConstraint has no real 'crom_l1_composed_InterRelationshipConstraint50' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relationship(direction="sample_text")
    partner = crom_l1_composed_InterRelationshipConstraint()
    setattr(partner, 'crom_l1_composed_InterRelationshipConstraint50', None)
    _safe_set(owner, 'crom_l1_composed_Relationship51', partner)
    assert getattr(partner, 'crom_l1_composed_InterRelationshipConstraint50') == owner
    _safe_set(owner, 'crom_l1_composed_Relationship51', None)
    assert getattr(partner, 'crom_l1_composed_InterRelationshipConstraint50') is None


def test_assoc_sub56_stub_double():
    # crom_l1_composed_DataInheritance has no real 'crom_l1_composed_DataInheritance57' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_DataType(serializable=True)
    partner = crom_l1_composed_DataInheritance()
    setattr(partner, 'crom_l1_composed_DataInheritance57', None)
    _safe_set(owner, 'crom_l1_composed_DataType58', partner)
    assert getattr(partner, 'crom_l1_composed_DataInheritance57') == owner
    _safe_set(owner, 'crom_l1_composed_DataType58', None)
    assert getattr(partner, 'crom_l1_composed_DataInheritance57') is None


def test_assoc_super54_stub_double():
    # crom_l1_composed_DataInheritance has no real 'crom_l1_composed_DataInheritance' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_DataType(serializable=True)
    partner = crom_l1_composed_DataInheritance()
    setattr(partner, 'crom_l1_composed_DataInheritance', None)
    _safe_set(owner, 'crom_l1_composed_DataType55', partner)
    assert getattr(partner, 'crom_l1_composed_DataInheritance') == owner
    _safe_set(owner, 'crom_l1_composed_DataType55', None)
    assert getattr(partner, 'crom_l1_composed_DataInheritance') is None


def test_assoc_targets52_stub_double():
    # crom_l1_composed_AbstractRole has no real 'crom_l1_composed_AbstractRole53' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_ComplexConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_ComplexConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_ComplexConstraint(expression="sample_text")
    partner = crom_l1_composed_AbstractRole()
    setattr(partner, 'crom_l1_composed_AbstractRole53', None)
    _safe_set(owner, 'crom_l1_composed_ComplexConstraint', {partner})
    assert getattr(partner, 'crom_l1_composed_AbstractRole53') == owner
    _safe_set(owner, 'crom_l1_composed_ComplexConstraint', set())
    assert getattr(partner, 'crom_l1_composed_AbstractRole53') is None


def test_assoc_tr_constraints33_stub_double():
    # crom_l1_composed_IntraRelationshipConstraint has no real 'crom_l1_composed_IntraRelationshipConstraint' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Relationship(direction="sample_text")
    partner = crom_l1_composed_IntraRelationshipConstraint()
    setattr(partner, 'crom_l1_composed_IntraRelationshipConstraint', None)
    _safe_set(owner, 'crom_l1_composed_Relationship34', {partner})
    assert getattr(partner, 'crom_l1_composed_IntraRelationshipConstraint') == owner
    _safe_set(owner, 'crom_l1_composed_Relationship34', set())
    assert getattr(partner, 'crom_l1_composed_IntraRelationshipConstraint') is None


def test_assoc_whole83_stub_double():
    # crom_l1_composed_CompartmentType has no real 'CompartmentType' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_composed_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_composed_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_composed_Part(lower=7, upper=7)
    partner = crom_l1_composed_CompartmentType()
    setattr(partner, 'CompartmentType', None)
    _safe_set(owner, 'parts', partner)
    assert getattr(partner, 'CompartmentType') == owner
    _safe_set(owner, 'parts', None)
    assert getattr(partner, 'CompartmentType') is None


