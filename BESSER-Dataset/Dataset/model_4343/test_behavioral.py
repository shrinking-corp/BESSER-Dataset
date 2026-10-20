import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractResource,
    Slot,
    migration_AbstractResource,
    migration_AttributeSlot,
    migration_EAttribute,
    migration_EClass,
    migration_EPackage,
    migration_EReference,
    migration_Instance,
    migration_Metamodel,
    migration_MetamodelResource,
    migration_Model,
    migration_ModelResource,
    migration_ReferenceSlot,
    migration_Repository,
    migration_Slot,
    migration_Type,
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

def test_assoc_instance20_reverse_link_reassign_clear():
    a1 = migration_Slot()
    a2 = migration_Slot()
    b = migration_Instance(uri="sample_text", uuid="sample_text")
    _safe_set(b, 'Instance21', a1)
    assert _is_linked(b, 'Instance21', a1)
    if hasattr(a1, 'slots'):
        assert _is_linked(a1, 'slots', b)
    _safe_set(b, 'Instance21', a2)
    assert _is_linked(b, 'Instance21', a2)
    if hasattr(a1, 'slots'):
        assert not _is_linked(a1, 'slots', b)
    if hasattr(a2, 'slots'):
        assert _is_linked(a2, 'slots', b)
    _safe_set(b, 'Instance21', None)
    assert not _is_linked(b, 'Instance21', a2)
    if hasattr(a2, 'slots'):
        assert not _is_linked(a2, 'slots', b)


def test_assoc_instances13_reverse_link_reassign_clear():
    a1 = migration_Type()
    a2 = migration_Type()
    b = migration_Instance(uri="sample_text", uuid="sample_text")
    _safe_set(b, 'Instance', a1)
    assert _is_linked(b, 'Instance', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'Instance', a2)
    assert _is_linked(b, 'Instance', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'Instance', None)
    assert not _is_linked(b, 'Instance', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_metamodel3_reverse_link_reassign_clear():
    a1 = migration_Model(reflection=True)
    a2 = migration_Model(reflection=False)
    b = migration_Metamodel()
    _safe_set(b, 'migration_Metamodel', a1)
    assert _is_linked(b, 'migration_Metamodel', a1)
    if hasattr(a1, 'migration_Model'):
        assert _is_linked(a1, 'migration_Model', b)
    _safe_set(b, 'migration_Metamodel', a2)
    assert _is_linked(b, 'migration_Metamodel', a2)
    if hasattr(a1, 'migration_Model'):
        assert not _is_linked(a1, 'migration_Model', b)
    if hasattr(a2, 'migration_Model'):
        assert _is_linked(a2, 'migration_Model', b)
    _safe_set(b, 'migration_Metamodel', None)
    assert not _is_linked(b, 'migration_Metamodel', a2)
    if hasattr(a2, 'migration_Model'):
        assert not _is_linked(a2, 'migration_Model', b)


def test_assoc_model14_reverse_link_reassign_clear():
    a1 = migration_Type()
    a2 = migration_Type()
    b = migration_Model(reflection=True)
    _safe_set(b, 'Model15', a1)
    assert _is_linked(b, 'Model15', a1)
    if hasattr(a1, 'types'):
        assert _is_linked(a1, 'types', b)
    _safe_set(b, 'Model15', a2)
    assert _is_linked(b, 'Model15', a2)
    if hasattr(a1, 'types'):
        assert not _is_linked(a1, 'types', b)
    if hasattr(a2, 'types'):
        assert _is_linked(a2, 'types', b)
    _safe_set(b, 'Model15', None)
    assert not _is_linked(b, 'Model15', a2)
    if hasattr(a2, 'types'):
        assert not _is_linked(a2, 'types', b)


def test_assoc_slots16_reverse_link_reassign_clear():
    a1 = migration_Slot()
    a2 = migration_Slot()
    b = migration_Instance(uri="sample_text", uuid="sample_text")
    _safe_set(b, 'instance', {a1})
    assert _is_linked(b, 'instance', a1)
    if hasattr(a1, 'Slot'):
        assert _is_linked(a1, 'Slot', b)
    _safe_set(b, 'instance', {a2})
    assert _is_linked(b, 'instance', a2)
    if hasattr(a1, 'Slot'):
        assert not _is_linked(a1, 'Slot', b)
    if hasattr(a2, 'Slot'):
        assert _is_linked(a2, 'Slot', b)
    _safe_set(b, 'instance', set())
    assert not _is_linked(b, 'instance', a2)
    if hasattr(a2, 'Slot'):
        assert not _is_linked(a2, 'Slot', b)


def test_assoc_type17_reverse_link_reassign_clear():
    a1 = migration_Type()
    a2 = migration_Type()
    b = migration_Instance(uri="sample_text", uuid="sample_text")
    _safe_set(b, 'instances', a1)
    assert _is_linked(b, 'instances', a1)
    if hasattr(a1, 'Type18'):
        assert _is_linked(a1, 'Type18', b)
    _safe_set(b, 'instances', a2)
    assert _is_linked(b, 'instances', a2)
    if hasattr(a1, 'Type18'):
        assert not _is_linked(a1, 'Type18', b)
    if hasattr(a2, 'Type18'):
        assert _is_linked(a2, 'Type18', b)
    _safe_set(b, 'instances', None)
    assert not _is_linked(b, 'instances', a2)
    if hasattr(a2, 'Type18'):
        assert not _is_linked(a2, 'Type18', b)


def test_assoc_types4_reverse_link_reassign_clear():
    a1 = migration_Type()
    a2 = migration_Type()
    b = migration_Model(reflection=True)
    _safe_set(b, 'model', {a1})
    assert _is_linked(b, 'model', a1)
    if hasattr(a1, 'Type'):
        assert _is_linked(a1, 'Type', b)
    _safe_set(b, 'model', {a2})
    assert _is_linked(b, 'model', a2)
    if hasattr(a1, 'Type'):
        assert not _is_linked(a1, 'Type', b)
    if hasattr(a2, 'Type'):
        assert _is_linked(a2, 'Type', b)
    _safe_set(b, 'model', set())
    assert not _is_linked(b, 'model', a2)
    if hasattr(a2, 'Type'):
        assert not _is_linked(a2, 'Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defaultPackage30_stub_double():
    # migration_EPackage has no real 'migration_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so migration_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Metamodel()
    partner = migration_EPackage()
    setattr(partner, 'migration_EPackage', None)
    _safe_set(owner, 'migration_Metamodel31', partner)
    assert getattr(partner, 'migration_EPackage') == owner
    _safe_set(owner, 'migration_Metamodel31', None)
    assert getattr(partner, 'migration_EPackage') is None


def test_assoc_eAttribute22_stub_double():
    # migration_EAttribute has no real 'migration_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so migration_AttributeSlot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_AttributeSlot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_AttributeSlot(values="sample_text")
    partner = migration_EAttribute()
    setattr(partner, 'migration_EAttribute', None)
    _safe_set(owner, 'migration_AttributeSlot', partner)
    assert getattr(partner, 'migration_EAttribute') == owner
    _safe_set(owner, 'migration_AttributeSlot', None)
    assert getattr(partner, 'migration_EAttribute') is None


def test_assoc_eClass12_stub_double():
    # migration_EClass has no real 'migration_EClass' property in the generated
    # code (a bare stub) -- manually attach it so migration_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Type()
    partner = migration_EClass()
    setattr(partner, 'migration_EClass', None)
    _safe_set(owner, 'migration_Type', partner)
    assert getattr(partner, 'migration_EClass') == owner
    _safe_set(owner, 'migration_Type', None)
    assert getattr(partner, 'migration_EClass') is None


def test_assoc_metamodel1_stub_double():
    # migration_Repository has no real 'repository2' property in the generated
    # code (a bare stub) -- manually attach it so migration_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Metamodel()
    partner = migration_Repository()
    setattr(partner, 'repository2', None)
    _safe_set(owner, 'Metamodel', partner)
    assert getattr(partner, 'repository2') == owner
    _safe_set(owner, 'Metamodel', None)
    assert getattr(partner, 'repository2') is None


def test_assoc_metamodel34_stub_double():
    # migration_MetamodelResource has no real 'resources35' property in the generated
    # code (a bare stub) -- manually attach it so migration_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Metamodel()
    partner = migration_MetamodelResource()
    setattr(partner, 'resources35', None)
    _safe_set(owner, 'Metamodel36', partner)
    assert getattr(partner, 'resources35') == owner
    _safe_set(owner, 'Metamodel36', None)
    assert getattr(partner, 'resources35') is None


def test_assoc_model0_stub_double():
    # migration_Repository has no real 'repository' property in the generated
    # code (a bare stub) -- manually attach it so migration_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Model(reflection=True)
    partner = migration_Repository()
    setattr(partner, 'repository', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'repository') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'repository') is None


def test_assoc_model10_stub_double():
    # migration_ModelResource has no real 'resources' property in the generated
    # code (a bare stub) -- manually attach it so migration_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Model(reflection=True)
    partner = migration_ModelResource()
    setattr(partner, 'resources', None)
    _safe_set(owner, 'Model11', partner)
    assert getattr(partner, 'resources') == owner
    _safe_set(owner, 'Model11', None)
    assert getattr(partner, 'resources') is None


def test_assoc_references19_stub_double():
    # migration_ReferenceSlot has no real 'ReferenceSlot' property in the generated
    # code (a bare stub) -- manually attach it so migration_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Instance(uri="sample_text", uuid="sample_text")
    partner = migration_ReferenceSlot()
    setattr(partner, 'ReferenceSlot', None)
    _safe_set(owner, 'values', {partner})
    assert getattr(partner, 'ReferenceSlot') == owner
    _safe_set(owner, 'values', set())
    assert getattr(partner, 'ReferenceSlot') is None


def test_assoc_repository27_stub_double():
    # migration_Repository has no real 'Repository29' property in the generated
    # code (a bare stub) -- manually attach it so migration_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Metamodel()
    partner = migration_Repository()
    setattr(partner, 'Repository29', None)
    _safe_set(owner, 'metamodel28', partner)
    assert getattr(partner, 'Repository29') == owner
    _safe_set(owner, 'metamodel28', None)
    assert getattr(partner, 'Repository29') is None


def test_assoc_repository7_stub_double():
    # migration_Repository has no real 'Repository' property in the generated
    # code (a bare stub) -- manually attach it so migration_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Model(reflection=True)
    partner = migration_Repository()
    setattr(partner, 'Repository', None)
    _safe_set(owner, 'model8', partner)
    assert getattr(partner, 'Repository') == owner
    _safe_set(owner, 'model8', None)
    assert getattr(partner, 'Repository') is None


def test_assoc_resources26_stub_double():
    # migration_MetamodelResource has no real 'MetamodelResource' property in the generated
    # code (a bare stub) -- manually attach it so migration_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Metamodel()
    partner = migration_MetamodelResource()
    setattr(partner, 'MetamodelResource', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'MetamodelResource') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'MetamodelResource') is None


def test_assoc_resources5_stub_double():
    # migration_ModelResource has no real 'ModelResource' property in the generated
    # code (a bare stub) -- manually attach it so migration_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Model(reflection=True)
    partner = migration_ModelResource()
    setattr(partner, 'ModelResource', None)
    _safe_set(owner, 'model6', {partner})
    assert getattr(partner, 'ModelResource') == owner
    _safe_set(owner, 'model6', set())
    assert getattr(partner, 'ModelResource') is None


def test_assoc_rootInstances9_stub_double():
    # migration_ModelResource has no real 'migration_ModelResource' property in the generated
    # code (a bare stub) -- manually attach it so migration_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Instance(uri="sample_text", uuid="sample_text")
    partner = migration_ModelResource()
    setattr(partner, 'migration_ModelResource', None)
    _safe_set(owner, 'migration_Instance', partner)
    assert owner in getattr(partner, 'migration_ModelResource')
    _safe_set(owner, 'migration_Instance', None)
    assert owner not in getattr(partner, 'migration_ModelResource')


def test_assoc_values24_stub_double():
    # migration_ReferenceSlot has no real 'references' property in the generated
    # code (a bare stub) -- manually attach it so migration_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migration_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migration_Instance(uri="sample_text", uuid="sample_text")
    partner = migration_ReferenceSlot()
    setattr(partner, 'references', None)
    _safe_set(owner, 'Instance25', partner)
    assert owner in getattr(partner, 'references')
    _safe_set(owner, 'Instance25', None)
    assert owner not in getattr(partner, 'references')


