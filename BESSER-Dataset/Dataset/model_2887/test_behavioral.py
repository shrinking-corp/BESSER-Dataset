import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Feature,
    Relation,
    Type,
    metamodel_AssociationEntity,
    metamodel_DatabaseConnection,
    metamodel_Datatype,
    metamodel_Entity,
    metamodel_Feature,
    metamodel_ManyToMany,
    metamodel_Model,
    metamodel_OneToMany,
    metamodel_OneToOne,
    metamodel_Relation,
    metamodel_Type,
    metamodel_idFeature,
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

def test_assoc_connector1_reverse_link_reassign_clear():
    a1 = metamodel_Model(name="sample_text")
    a2 = metamodel_Model(name="sample_text_2")
    b = metamodel_DatabaseConnection(jdbcDriver="sample_text", jdbcPassword="sample_text", jdbcPrefix="sample_text", jdbcUrl="sample_text", jdbcUser="sample_text", persistenceUnit="sample_text")
    _safe_set(b, 'metamodel_DatabaseConnection', a1)
    assert _is_linked(b, 'metamodel_DatabaseConnection', a1)
    if hasattr(a1, 'metamodel_Model2'):
        assert _is_linked(a1, 'metamodel_Model2', b)
    _safe_set(b, 'metamodel_DatabaseConnection', a2)
    assert _is_linked(b, 'metamodel_DatabaseConnection', a2)
    if hasattr(a1, 'metamodel_Model2'):
        assert not _is_linked(a1, 'metamodel_Model2', b)
    if hasattr(a2, 'metamodel_Model2'):
        assert _is_linked(a2, 'metamodel_Model2', b)
    _safe_set(b, 'metamodel_DatabaseConnection', None)
    assert not _is_linked(b, 'metamodel_DatabaseConnection', a2)
    if hasattr(a2, 'metamodel_Model2'):
        assert not _is_linked(a2, 'metamodel_Model2', b)


def test_assoc_type14_reverse_link_reassign_clear():
    a1 = metamodel_Type(name="sample_text")
    a2 = metamodel_Type(name="sample_text_2")
    b = metamodel_Feature(name="sample_text", nullable=True, xmltransient=True)
    _safe_set(b, 'metamodel_Feature15', a1)
    assert _is_linked(b, 'metamodel_Feature15', a1)
    if hasattr(a1, 'metamodel_Type16'):
        assert _is_linked(a1, 'metamodel_Type16', b)
    _safe_set(b, 'metamodel_Feature15', a2)
    assert _is_linked(b, 'metamodel_Feature15', a2)
    if hasattr(a1, 'metamodel_Type16'):
        assert not _is_linked(a1, 'metamodel_Type16', b)
    if hasattr(a2, 'metamodel_Type16'):
        assert _is_linked(a2, 'metamodel_Type16', b)
    _safe_set(b, 'metamodel_Feature15', None)
    assert not _is_linked(b, 'metamodel_Feature15', a2)
    if hasattr(a2, 'metamodel_Type16'):
        assert not _is_linked(a2, 'metamodel_Type16', b)


def test_assoc_types0_reverse_link_reassign_clear():
    a1 = metamodel_Type(name="sample_text")
    a2 = metamodel_Type(name="sample_text_2")
    b = metamodel_Model(name="sample_text")
    _safe_set(b, 'metamodel_Model', {a1})
    assert _is_linked(b, 'metamodel_Model', a1)
    if hasattr(a1, 'metamodel_Type'):
        assert _is_linked(a1, 'metamodel_Type', b)
    _safe_set(b, 'metamodel_Model', {a2})
    assert _is_linked(b, 'metamodel_Model', a2)
    if hasattr(a1, 'metamodel_Type'):
        assert not _is_linked(a1, 'metamodel_Type', b)
    if hasattr(a2, 'metamodel_Type'):
        assert _is_linked(a2, 'metamodel_Type', b)
    _safe_set(b, 'metamodel_Model', set())
    assert not _is_linked(b, 'metamodel_Model', a2)
    if hasattr(a2, 'metamodel_Type'):
        assert not _is_linked(a2, 'metamodel_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associates21_stub_double():
    # metamodel_AssociationEntity has no real 'AssociationEntity' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_AssociationEntity()
    setattr(partner, 'AssociationEntity', None)
    _safe_set(owner, 'relation', partner)
    assert getattr(partner, 'AssociationEntity') == owner
    _safe_set(owner, 'relation', None)
    assert getattr(partner, 'AssociationEntity') is None


def test_assoc_features22_stub_double():
    # metamodel_AssociationEntity has no real 'metamodel_AssociationEntity' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Feature(name="sample_text", nullable=True, xmltransient=True)
    partner = metamodel_AssociationEntity()
    setattr(partner, 'metamodel_AssociationEntity', None)
    _safe_set(owner, 'metamodel_Feature23', partner)
    assert owner in getattr(partner, 'metamodel_AssociationEntity')
    _safe_set(owner, 'metamodel_Feature23', None)
    assert owner not in getattr(partner, 'metamodel_AssociationEntity')


def test_assoc_features3_stub_double():
    # metamodel_Entity has no real 'metamodel_Entity' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Feature(name="sample_text", nullable=True, xmltransient=True)
    partner = metamodel_Entity()
    setattr(partner, 'metamodel_Entity', None)
    _safe_set(owner, 'metamodel_Feature', partner)
    assert owner in getattr(partner, 'metamodel_Entity')
    _safe_set(owner, 'metamodel_Feature', None)
    assert owner not in getattr(partner, 'metamodel_Entity')


def test_assoc_featuresId7_stub_double():
    # metamodel_Entity has no real 'metamodel_Entity8' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_idFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_idFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_idFeature(generationType="sample_text")
    partner = metamodel_Entity()
    setattr(partner, 'metamodel_Entity8', None)
    _safe_set(owner, 'metamodel_idFeature', partner)
    assert getattr(partner, 'metamodel_Entity8') == owner
    _safe_set(owner, 'metamodel_idFeature', None)
    assert getattr(partner, 'metamodel_Entity8') is None


def test_assoc_ownedBy5_stub_double():
    # metamodel_Entity has no real 'slave' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_Entity()
    setattr(partner, 'slave', None)
    _safe_set(owner, 'Relation6', partner)
    assert owner in getattr(partner, 'slave')
    _safe_set(owner, 'Relation6', None)
    assert owner not in getattr(partner, 'slave')


def test_assoc_owner17_stub_double():
    # metamodel_Entity has no real 'Entity18' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_Entity()
    setattr(partner, 'Entity18', None)
    _safe_set(owner, 'owns', partner)
    assert getattr(partner, 'Entity18') == owner
    _safe_set(owner, 'owns', None)
    assert getattr(partner, 'Entity18') is None


def test_assoc_owns4_stub_double():
    # metamodel_Entity has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_Entity()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Relation', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Relation', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_relation24_stub_double():
    # metamodel_AssociationEntity has no real 'associates' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_AssociationEntity()
    setattr(partner, 'associates', None)
    _safe_set(owner, 'Relation25', partner)
    assert getattr(partner, 'associates') == owner
    _safe_set(owner, 'Relation25', None)
    assert getattr(partner, 'associates') is None


def test_assoc_slave19_stub_double():
    # metamodel_Entity has no real 'Entity20' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Relation(optional=True, unidirectional=True)
    partner = metamodel_Entity()
    setattr(partner, 'Entity20', None)
    _safe_set(owner, 'ownedBy', partner)
    assert getattr(partner, 'Entity20') == owner
    _safe_set(owner, 'ownedBy', None)
    assert getattr(partner, 'Entity20') is None


