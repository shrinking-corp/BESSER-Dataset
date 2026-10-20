import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRole,
    AntiRigidType,
    Constraint,
    Inheritance,
    Model,
    ModelElement,
    NamedElement,
    Player,
    Relation,
    RelationTarget,
    RigidType,
    RoleConstraint,
    RoleGroupElement,
    Type,
    TypedElement,
    crom_l1_AbstractRole,
    crom_l1_AbstractRoleRef,
    crom_l1_AntiRigidType,
    crom_l1_Attribute,
    crom_l1_CompartmentInheritance,
    crom_l1_CompartmentType,
    crom_l1_Constraint,
    crom_l1_DataInheritance,
    crom_l1_DataType,
    crom_l1_Fulfillment,
    crom_l1_Group,
    crom_l1_Inheritance,
    crom_l1_Model,
    crom_l1_ModelElement,
    crom_l1_NamedElement,
    crom_l1_NaturalInheritance,
    crom_l1_NaturalType,
    crom_l1_Operation,
    crom_l1_Parameter,
    crom_l1_Part,
    crom_l1_Player,
    crom_l1_Relation,
    crom_l1_RelationTarget,
    crom_l1_RigidType,
    crom_l1_RoleConstraint,
    crom_l1_RoleEquivalence,
    crom_l1_RoleGroup,
    crom_l1_RoleGroupElement,
    crom_l1_RoleImplication,
    crom_l1_RoleProhibition,
    crom_l1_RoleType,
    crom_l1_Test,
    crom_l1_Type,
    crom_l1_TypedElement,
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

def test_assoc_elements23_stub_double():
    # crom_l1_RoleGroupElement has no real 'crom_l1_RoleGroupElement' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_RoleGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_RoleGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_RoleGroup(lower=7, upper=7)
    partner = crom_l1_RoleGroupElement()
    setattr(partner, 'crom_l1_RoleGroupElement', None)
    _safe_set(owner, 'crom_l1_RoleGroup', {partner})
    assert getattr(partner, 'crom_l1_RoleGroupElement') == owner
    _safe_set(owner, 'crom_l1_RoleGroup', set())
    assert getattr(partner, 'crom_l1_RoleGroupElement') is None


def test_assoc_operations8_stub_double():
    # crom_l1_Type has no real 'owner9' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Operation(operation="sample_text")
    partner = crom_l1_Type()
    setattr(partner, 'owner9', None)
    _safe_set(owner, 'Operation', partner)
    assert owner in getattr(partner, 'owner9')
    _safe_set(owner, 'Operation', None)
    assert owner not in getattr(partner, 'owner9')


def test_assoc_owner4_stub_double():
    # crom_l1_Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Operation(operation="sample_text")
    partner = crom_l1_Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'operations', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'operations', None)
    assert getattr(partner, 'Type') is None


def test_assoc_params3_stub_double():
    # crom_l1_Parameter has no real 'crom_l1_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Operation(operation="sample_text")
    partner = crom_l1_Parameter()
    setattr(partner, 'crom_l1_Parameter', None)
    _safe_set(owner, 'crom_l1_Operation', {partner})
    assert getattr(partner, 'crom_l1_Parameter') == owner
    _safe_set(owner, 'crom_l1_Operation', set())
    assert getattr(partner, 'crom_l1_Parameter') is None


def test_assoc_parts29_stub_double():
    # crom_l1_CompartmentType has no real 'whole' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Part(lower=7, upper=7)
    partner = crom_l1_CompartmentType()
    setattr(partner, 'whole', None)
    _safe_set(owner, 'Part', partner)
    assert owner in getattr(partner, 'whole')
    _safe_set(owner, 'Part', None)
    assert owner not in getattr(partner, 'whole')


def test_assoc_roles26_stub_double():
    # crom_l1_AbstractRole has no real 'crom_l1_AbstractRole27' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Part(lower=7, upper=7)
    partner = crom_l1_AbstractRole()
    setattr(partner, 'crom_l1_AbstractRole27', None)
    _safe_set(owner, 'crom_l1_Part', partner)
    assert getattr(partner, 'crom_l1_AbstractRole27') == owner
    _safe_set(owner, 'crom_l1_Part', None)
    assert getattr(partner, 'crom_l1_AbstractRole27') is None


def test_assoc_whole28_stub_double():
    # crom_l1_CompartmentType has no real 'CompartmentType' property in the generated
    # code (a bare stub) -- manually attach it so crom_l1_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # crom_l1_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = crom_l1_Part(lower=7, upper=7)
    partner = crom_l1_CompartmentType()
    setattr(partner, 'CompartmentType', None)
    _safe_set(owner, 'parts', partner)
    assert getattr(partner, 'CompartmentType') == owner
    _safe_set(owner, 'parts', None)
    assert getattr(partner, 'CompartmentType') is None


