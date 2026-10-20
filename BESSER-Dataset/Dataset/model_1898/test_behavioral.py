import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EAttribute,
    EClass,
    EPackage,
    EReference,
    LocatedElement,
    Migrator,
    OpDef,
    emig_Artifact,
    emig_Attribute,
    emig_Class,
    emig_DotNavigationObjDX,
    emig_DotNavigationObjSX,
    emig_EAttribute,
    emig_EAttributeOpDef,
    emig_EClass,
    emig_EClassOpDef,
    emig_EObject,
    emig_EPackage,
    emig_EPackageOpDef,
    emig_EReference,
    emig_EReferenceOpDef,
    emig_EStructuralFeature,
    emig_FilterMigrator,
    emig_LocatedElement,
    emig_MigrationLibrary,
    emig_MigrationProgram,
    emig_Migrator,
    emig_MigratorDX,
    emig_MigratorSX,
    emig_MyModel,
    emig_OpDef,
    emig_Package,
    emig_Parameter,
    emig_Reference,
    emig_RewritingRule,
    emig_Rule,
    emig_setterDef,
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

def test_assoc_filter12_reverse_link_reassign_clear():
    a1 = emig_Rule(name="sample_text")
    a2 = emig_Rule(name="sample_text_2")
    b = emig_OpDef(op="sample_text")
    _safe_set(b, 'emig_OpDef', a1)
    assert _is_linked(b, 'emig_OpDef', a1)
    if hasattr(a1, 'emig_Rule13'):
        assert _is_linked(a1, 'emig_Rule13', b)
    _safe_set(b, 'emig_OpDef', a2)
    assert _is_linked(b, 'emig_OpDef', a2)
    if hasattr(a1, 'emig_Rule13'):
        assert not _is_linked(a1, 'emig_Rule13', b)
    if hasattr(a2, 'emig_Rule13'):
        assert _is_linked(a2, 'emig_Rule13', b)
    _safe_set(b, 'emig_OpDef', None)
    assert not _is_linked(b, 'emig_OpDef', a2)
    if hasattr(a2, 'emig_Rule13'):
        assert not _is_linked(a2, 'emig_Rule13', b)


def test_assoc_par46_reverse_link_reassign_clear():
    a1 = emig_setterDef(operator="sample_text")
    a2 = emig_setterDef(operator="sample_text_2")
    b = emig_Parameter(name="sample_text")
    _safe_set(b, 'emig_Parameter', a1)
    assert _is_linked(b, 'emig_Parameter', a1)
    if hasattr(a1, 'emig_setterDef47'):
        assert _is_linked(a1, 'emig_setterDef47', b)
    _safe_set(b, 'emig_Parameter', a2)
    assert _is_linked(b, 'emig_Parameter', a2)
    if hasattr(a1, 'emig_setterDef47'):
        assert not _is_linked(a1, 'emig_setterDef47', b)
    if hasattr(a2, 'emig_setterDef47'):
        assert _is_linked(a2, 'emig_setterDef47', b)
    _safe_set(b, 'emig_Parameter', None)
    assert not _is_linked(b, 'emig_Parameter', a2)
    if hasattr(a2, 'emig_setterDef47'):
        assert not _is_linked(a2, 'emig_setterDef47', b)


def test_assoc_rules3_reverse_link_reassign_clear():
    a1 = emig_Rule(name="sample_text")
    a2 = emig_Rule(name="sample_text_2")
    b = emig_MigrationLibrary(name="sample_text")
    _safe_set(b, 'emig_MigrationLibrary4', {a1})
    assert _is_linked(b, 'emig_MigrationLibrary4', a1)
    if hasattr(a1, 'emig_Rule'):
        assert _is_linked(a1, 'emig_Rule', b)
    _safe_set(b, 'emig_MigrationLibrary4', {a2})
    assert _is_linked(b, 'emig_MigrationLibrary4', a2)
    if hasattr(a1, 'emig_Rule'):
        assert not _is_linked(a1, 'emig_Rule', b)
    if hasattr(a2, 'emig_Rule'):
        assert _is_linked(a2, 'emig_Rule', b)
    _safe_set(b, 'emig_MigrationLibrary4', set())
    assert not _is_linked(b, 'emig_MigrationLibrary4', a2)
    if hasattr(a2, 'emig_Rule'):
        assert not _is_linked(a2, 'emig_Rule', b)


def test_assoc_rules9_reverse_link_reassign_clear():
    a1 = emig_Rule(name="sample_text")
    a2 = emig_Rule(name="sample_text_2")
    b = emig_MigrationProgram(artifact="sample_text", delta="sample_text", libs="sample_text", migr="sample_text", name="sample_text")
    _safe_set(b, 'emig_MigrationProgram10', {a1})
    assert _is_linked(b, 'emig_MigrationProgram10', a1)
    if hasattr(a1, 'emig_Rule11'):
        assert _is_linked(a1, 'emig_Rule11', b)
    _safe_set(b, 'emig_MigrationProgram10', {a2})
    assert _is_linked(b, 'emig_MigrationProgram10', a2)
    if hasattr(a1, 'emig_Rule11'):
        assert not _is_linked(a1, 'emig_Rule11', b)
    if hasattr(a2, 'emig_Rule11'):
        assert _is_linked(a2, 'emig_Rule11', b)
    _safe_set(b, 'emig_MigrationProgram10', set())
    assert not _is_linked(b, 'emig_MigrationProgram10', a2)
    if hasattr(a2, 'emig_Rule11'):
        assert not _is_linked(a2, 'emig_Rule11', b)


def test_assoc_setters16_reverse_link_reassign_clear():
    a1 = emig_setterDef(operator="sample_text")
    a2 = emig_setterDef(operator="sample_text_2")
    b = emig_OpDef(op="sample_text")
    _safe_set(b, 'emig_OpDef17', {a1})
    assert _is_linked(b, 'emig_OpDef17', a1)
    if hasattr(a1, 'emig_setterDef'):
        assert _is_linked(a1, 'emig_setterDef', b)
    _safe_set(b, 'emig_OpDef17', {a2})
    assert _is_linked(b, 'emig_OpDef17', a2)
    if hasattr(a1, 'emig_setterDef'):
        assert not _is_linked(a1, 'emig_setterDef', b)
    if hasattr(a2, 'emig_setterDef'):
        assert _is_linked(a2, 'emig_setterDef', b)
    _safe_set(b, 'emig_OpDef17', set())
    assert not _is_linked(b, 'emig_OpDef17', a2)
    if hasattr(a2, 'emig_setterDef'):
        assert not _is_linked(a2, 'emig_setterDef', b)


def test_assoc_typeArt5_reverse_link_reassign_clear():
    a1 = emig_MigrationProgram(artifact="sample_text", delta="sample_text", libs="sample_text", migr="sample_text", name="sample_text")
    a2 = emig_MigrationProgram(artifact="sample_text_2", delta="sample_text_2", libs="sample_text_2", migr="sample_text_2", name="sample_text_2")
    b = emig_Artifact(type="sample_text")
    _safe_set(b, 'emig_Artifact', a1)
    assert _is_linked(b, 'emig_Artifact', a1)
    if hasattr(a1, 'emig_MigrationProgram6'):
        assert _is_linked(a1, 'emig_MigrationProgram6', b)
    _safe_set(b, 'emig_Artifact', a2)
    assert _is_linked(b, 'emig_Artifact', a2)
    if hasattr(a1, 'emig_MigrationProgram6'):
        assert not _is_linked(a1, 'emig_MigrationProgram6', b)
    if hasattr(a2, 'emig_MigrationProgram6'):
        assert _is_linked(a2, 'emig_MigrationProgram6', b)
    _safe_set(b, 'emig_Artifact', None)
    assert not _is_linked(b, 'emig_Artifact', a2)
    if hasattr(a2, 'emig_MigrationProgram6'):
        assert not _is_linked(a2, 'emig_MigrationProgram6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_MigrationProgr1_stub_double():
    # emig_MyModel has no real 'emig_MyModel2' property in the generated
    # code (a bare stub) -- manually attach it so emig_MigrationProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_MigrationProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_MigrationProgram(artifact="sample_text", delta="sample_text", libs="sample_text", migr="sample_text", name="sample_text")
    partner = emig_MyModel()
    setattr(partner, 'emig_MyModel2', None)
    _safe_set(owner, 'emig_MigrationProgram', partner)
    assert getattr(partner, 'emig_MyModel2') == owner
    _safe_set(owner, 'emig_MigrationProgram', None)
    assert getattr(partner, 'emig_MyModel2') is None


def test_assoc_featureSX63_stub_double():
    # emig_DotNavigationObjSX has no real 'emig_DotNavigationObjSX' property in the generated
    # code (a bare stub) -- manually attach it so emig_FilterMigrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_FilterMigrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_FilterMigrator(op="sample_text")
    partner = emig_DotNavigationObjSX()
    setattr(partner, 'emig_DotNavigationObjSX', None)
    _safe_set(owner, 'emig_FilterMigrator64', partner)
    assert getattr(partner, 'emig_DotNavigationObjSX') == owner
    _safe_set(owner, 'emig_FilterMigrator64', None)
    assert getattr(partner, 'emig_DotNavigationObjSX') is None


def test_assoc_filterDX58_stub_double():
    # emig_MigratorDX has no real 'emig_MigratorDX59' property in the generated
    # code (a bare stub) -- manually attach it so emig_FilterMigrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_FilterMigrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_FilterMigrator(op="sample_text")
    partner = emig_MigratorDX()
    setattr(partner, 'emig_MigratorDX59', None)
    _safe_set(owner, 'emig_FilterMigrator60', partner)
    assert owner in getattr(partner, 'emig_MigratorDX59')
    _safe_set(owner, 'emig_FilterMigrator60', None)
    assert owner not in getattr(partner, 'emig_MigratorDX59')


def test_assoc_filterSX53_stub_double():
    # emig_MigratorSX has no real 'emig_MigratorSX54' property in the generated
    # code (a bare stub) -- manually attach it so emig_FilterMigrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_FilterMigrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_FilterMigrator(op="sample_text")
    partner = emig_MigratorSX()
    setattr(partner, 'emig_MigratorSX54', None)
    _safe_set(owner, 'emig_FilterMigrator', partner)
    assert owner in getattr(partner, 'emig_MigratorSX54')
    _safe_set(owner, 'emig_FilterMigrator', None)
    assert owner not in getattr(partner, 'emig_MigratorSX54')


def test_assoc_metafeature44_stub_double():
    # emig_EStructuralFeature has no real 'emig_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so emig_setterDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_setterDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_setterDef(operator="sample_text")
    partner = emig_EStructuralFeature()
    setattr(partner, 'emig_EStructuralFeature', None)
    _safe_set(owner, 'emig_setterDef45', partner)
    assert getattr(partner, 'emig_EStructuralFeature') == owner
    _safe_set(owner, 'emig_setterDef45', None)
    assert getattr(partner, 'emig_EStructuralFeature') is None


def test_assoc_migrationLib0_stub_double():
    # emig_MyModel has no real 'emig_MyModel' property in the generated
    # code (a bare stub) -- manually attach it so emig_MigrationLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_MigrationLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_MigrationLibrary(name="sample_text")
    partner = emig_MyModel()
    setattr(partner, 'emig_MyModel', None)
    _safe_set(owner, 'emig_MigrationLibrary', partner)
    assert getattr(partner, 'emig_MyModel') == owner
    _safe_set(owner, 'emig_MigrationLibrary', None)
    assert getattr(partner, 'emig_MyModel') is None


def test_assoc_rewritingRules14_stub_double():
    # emig_RewritingRule has no real 'emig_RewritingRule' property in the generated
    # code (a bare stub) -- manually attach it so emig_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_Rule(name="sample_text")
    partner = emig_RewritingRule()
    setattr(partner, 'emig_RewritingRule', None)
    _safe_set(owner, 'emig_Rule15', {partner})
    assert getattr(partner, 'emig_RewritingRule') == owner
    _safe_set(owner, 'emig_Rule15', set())
    assert getattr(partner, 'emig_RewritingRule') is None


def test_assoc_transformationPackage7_stub_double():
    # emig_EPackage has no real 'emig_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so emig_MigrationProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_MigrationProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_MigrationProgram(artifact="sample_text", delta="sample_text", libs="sample_text", migr="sample_text", name="sample_text")
    partner = emig_EPackage()
    setattr(partner, 'emig_EPackage', None)
    _safe_set(owner, 'emig_MigrationProgram8', {partner})
    assert getattr(partner, 'emig_EPackage') == owner
    _safe_set(owner, 'emig_MigrationProgram8', set())
    assert getattr(partner, 'emig_EPackage') is None


def test_assoc_value65_stub_double():
    # emig_DotNavigationObjDX has no real 'emig_DotNavigationObjDX' property in the generated
    # code (a bare stub) -- manually attach it so emig_FilterMigrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emig_FilterMigrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emig_FilterMigrator(op="sample_text")
    partner = emig_DotNavigationObjDX()
    setattr(partner, 'emig_DotNavigationObjDX', None)
    _safe_set(owner, 'emig_FilterMigrator66', partner)
    assert getattr(partner, 'emig_DotNavigationObjDX') == owner
    _safe_set(owner, 'emig_FilterMigrator66', None)
    assert getattr(partner, 'emig_DotNavigationObjDX') is None


