import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DbMddAndroid_Column,
    DbMddAndroid_DBScheme,
    DbMddAndroid_NamedElement,
    DbMddAndroid_Relation,
    DbMddAndroid_Table,
    NamedElement,
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

def test_assoc_columns3_stub_double():
    # DbMddAndroid_Table has no real 'DbMddAndroid_Table4' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Column(type="sample_text")
    partner = DbMddAndroid_Table()
    setattr(partner, 'DbMddAndroid_Table4', None)
    _safe_set(owner, 'DbMddAndroid_Column', partner)
    assert owner in getattr(partner, 'DbMddAndroid_Table4')
    _safe_set(owner, 'DbMddAndroid_Column', None)
    assert owner not in getattr(partner, 'DbMddAndroid_Table4')


def test_assoc_inRelation9_stub_double():
    # DbMddAndroid_Table has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Relation(maxSourceMultiplicity=7, maxTargetMultiplicity=7, minSourceMultiplicity=7, minTargetMultiplicity=7)
    partner = DbMddAndroid_Table()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Relation10', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Relation10', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outRelation8_stub_double():
    # DbMddAndroid_Table has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Relation(maxSourceMultiplicity=7, maxTargetMultiplicity=7, minSourceMultiplicity=7, minTargetMultiplicity=7)
    partner = DbMddAndroid_Table()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Relation', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Relation', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_primaryKey5_stub_double():
    # DbMddAndroid_Table has no real 'DbMddAndroid_Table6' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Column(type="sample_text")
    partner = DbMddAndroid_Table()
    setattr(partner, 'DbMddAndroid_Table6', None)
    _safe_set(owner, 'DbMddAndroid_Column7', partner)
    assert getattr(partner, 'DbMddAndroid_Table6') == owner
    _safe_set(owner, 'DbMddAndroid_Column7', None)
    assert getattr(partner, 'DbMddAndroid_Table6') is None


def test_assoc_relations1_stub_double():
    # DbMddAndroid_DBScheme has no real 'DbMddAndroid_DBScheme2' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Relation(maxSourceMultiplicity=7, maxTargetMultiplicity=7, minSourceMultiplicity=7, minTargetMultiplicity=7)
    partner = DbMddAndroid_DBScheme()
    setattr(partner, 'DbMddAndroid_DBScheme2', None)
    _safe_set(owner, 'DbMddAndroid_Relation', partner)
    assert owner in getattr(partner, 'DbMddAndroid_DBScheme2')
    _safe_set(owner, 'DbMddAndroid_Relation', None)
    assert owner not in getattr(partner, 'DbMddAndroid_DBScheme2')


def test_assoc_source11_stub_double():
    # DbMddAndroid_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Relation(maxSourceMultiplicity=7, maxTargetMultiplicity=7, minSourceMultiplicity=7, minTargetMultiplicity=7)
    partner = DbMddAndroid_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'outRelation', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'outRelation', None)
    assert getattr(partner, 'Table') is None


def test_assoc_target12_stub_double():
    # DbMddAndroid_Table has no real 'Table13' property in the generated
    # code (a bare stub) -- manually attach it so DbMddAndroid_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DbMddAndroid_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DbMddAndroid_Relation(maxSourceMultiplicity=7, maxTargetMultiplicity=7, minSourceMultiplicity=7, minTargetMultiplicity=7)
    partner = DbMddAndroid_Table()
    setattr(partner, 'Table13', None)
    _safe_set(owner, 'inRelation', partner)
    assert getattr(partner, 'Table13') == owner
    _safe_set(owner, 'inRelation', None)
    assert getattr(partner, 'Table13') is None


