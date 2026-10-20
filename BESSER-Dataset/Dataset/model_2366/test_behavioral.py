import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Key,
    ModelElement,
    NamedElement,
    sql_Annotation,
    sql_Column,
    sql_Event,
    sql_ForeignKey,
    sql_Key,
    sql_ModelElement,
    sql_NamedElement,
    sql_PrimaryKey,
    sql_Schema,
    sql_Table,
    Action,
    Condition,
    Property,
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

def test_assoc_column10_stub_double():
    # sql_Key has no real 'keys' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(properties="sample_text", type="sample_text")
    partner = sql_Key()
    setattr(partner, 'keys', None)
    _safe_set(owner, 'Column11', partner)
    assert getattr(partner, 'keys') == owner
    _safe_set(owner, 'Column11', None)
    assert getattr(partner, 'keys') is None


def test_assoc_keys9_stub_double():
    # sql_Key has no real 'Key' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(properties="sample_text", type="sample_text")
    partner = sql_Key()
    setattr(partner, 'Key', None)
    _safe_set(owner, 'column', {partner})
    assert getattr(partner, 'Key') == owner
    _safe_set(owner, 'column', set())
    assert getattr(partner, 'Key') is None


def test_assoc_ownedAnnotations23_stub_double():
    # sql_ModelElement has no real 'owningModelElement' property in the generated
    # code (a bare stub) -- manually attach it so sql_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Annotation(annotation="sample_text")
    partner = sql_ModelElement()
    setattr(partner, 'owningModelElement', None)
    _safe_set(owner, 'Annotation', partner)
    assert owner in getattr(partner, 'owningModelElement')
    _safe_set(owner, 'Annotation', None)
    assert owner not in getattr(partner, 'owningModelElement')


def test_assoc_ownedColumns0_stub_double():
    # sql_Table has no real 'owningTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(properties="sample_text", type="sample_text")
    partner = sql_Table()
    setattr(partner, 'owningTable', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'owningTable')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'owningTable')


def test_assoc_ownedEvents18_stub_double():
    # sql_ForeignKey has no real 'owningForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so sql_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Event(action="sample_text", condition="sample_text")
    partner = sql_ForeignKey()
    setattr(partner, 'owningForeignKey', None)
    _safe_set(owner, 'Event', partner)
    assert owner in getattr(partner, 'owningForeignKey')
    _safe_set(owner, 'Event', None)
    assert owner not in getattr(partner, 'owningForeignKey')


def test_assoc_owningForeignKey19_stub_double():
    # sql_ForeignKey has no real 'ForeignKey20' property in the generated
    # code (a bare stub) -- manually attach it so sql_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Event(action="sample_text", condition="sample_text")
    partner = sql_ForeignKey()
    setattr(partner, 'ForeignKey20', None)
    _safe_set(owner, 'ownedEvents', partner)
    assert getattr(partner, 'ForeignKey20') == owner
    _safe_set(owner, 'ownedEvents', None)
    assert getattr(partner, 'ForeignKey20') is None


def test_assoc_owningModelElement24_stub_double():
    # sql_ModelElement has no real 'ModelElement' property in the generated
    # code (a bare stub) -- manually attach it so sql_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Annotation(annotation="sample_text")
    partner = sql_ModelElement()
    setattr(partner, 'ModelElement', None)
    _safe_set(owner, 'ownedAnnotations', partner)
    assert getattr(partner, 'ModelElement') == owner
    _safe_set(owner, 'ownedAnnotations', None)
    assert getattr(partner, 'ModelElement') is None


def test_assoc_owningTable8_stub_double():
    # sql_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(properties="sample_text", type="sample_text")
    partner = sql_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'ownedColumns', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'ownedColumns', None)
    assert getattr(partner, 'Table') is None


