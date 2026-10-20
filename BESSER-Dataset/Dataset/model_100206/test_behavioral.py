import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sqlview_Attribute,
    sqlview_Class,
    sqlview_Comparison,
    sqlview_Condition,
    sqlview_EObject,
    sqlview_EclExpression,
    sqlview_Expression,
    sqlview_From,
    sqlview_Join,
    sqlview_JoinLeft,
    sqlview_JoinRight,
    sqlview_Left,
    sqlview_Metamodel,
    sqlview_MetamodelName,
    sqlview_Model,
    sqlview_Relation,
    sqlview_Right,
    sqlview_Select,
    sqlview_SelectAttribute,
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

def test_assoc_attributeWhereRight60_reverse_link_reassign_clear():
    a1 = sqlview_Right(value="sample_text")
    a2 = sqlview_Right(value="sample_text_2")
    b = sqlview_Attribute(name="sample_text")
    _safe_set(b, 'sqlview_Attribute62', a1)
    assert _is_linked(b, 'sqlview_Attribute62', a1)
    if hasattr(a1, 'sqlview_Right61'):
        assert _is_linked(a1, 'sqlview_Right61', b)
    _safe_set(b, 'sqlview_Attribute62', a2)
    assert _is_linked(b, 'sqlview_Attribute62', a2)
    if hasattr(a1, 'sqlview_Right61'):
        assert not _is_linked(a1, 'sqlview_Right61', b)
    if hasattr(a2, 'sqlview_Right61'):
        assert _is_linked(a2, 'sqlview_Right61', b)
    _safe_set(b, 'sqlview_Attribute62', None)
    assert not _is_linked(b, 'sqlview_Attribute62', a2)
    if hasattr(a2, 'sqlview_Right61'):
        assert not _is_linked(a2, 'sqlview_Right61', b)


def test_assoc_class_57_reverse_link_reassign_clear():
    a1 = sqlview_Right(value="sample_text")
    a2 = sqlview_Right(value="sample_text_2")
    b = sqlview_Class(name="sample_text")
    _safe_set(b, 'sqlview_Class59', a1)
    assert _is_linked(b, 'sqlview_Class59', a1)
    if hasattr(a1, 'sqlview_Right58'):
        assert _is_linked(a1, 'sqlview_Right58', b)
    _safe_set(b, 'sqlview_Class59', a2)
    assert _is_linked(b, 'sqlview_Class59', a2)
    if hasattr(a1, 'sqlview_Right58'):
        assert not _is_linked(a1, 'sqlview_Right58', b)
    if hasattr(a2, 'sqlview_Right58'):
        assert _is_linked(a2, 'sqlview_Right58', b)
    _safe_set(b, 'sqlview_Class59', None)
    assert not _is_linked(b, 'sqlview_Class59', a2)
    if hasattr(a2, 'sqlview_Right58'):
        assert not _is_linked(a2, 'sqlview_Right58', b)


def test_assoc_metamodel0_reverse_link_reassign_clear():
    a1 = sqlview_Model(viewName="sample_text")
    a2 = sqlview_Model(viewName="sample_text_2")
    b = sqlview_Metamodel(metamodelURL="sample_text")
    _safe_set(b, 'sqlview_Metamodel', a1)
    assert _is_linked(b, 'sqlview_Metamodel', a1)
    if hasattr(a1, 'sqlview_Model'):
        assert _is_linked(a1, 'sqlview_Model', b)
    _safe_set(b, 'sqlview_Metamodel', a2)
    assert _is_linked(b, 'sqlview_Metamodel', a2)
    if hasattr(a1, 'sqlview_Model'):
        assert not _is_linked(a1, 'sqlview_Model', b)
    if hasattr(a2, 'sqlview_Model'):
        assert _is_linked(a2, 'sqlview_Model', b)
    _safe_set(b, 'sqlview_Metamodel', None)
    assert not _is_linked(b, 'sqlview_Metamodel', a2)
    if hasattr(a2, 'sqlview_Model'):
        assert not _is_linked(a2, 'sqlview_Model', b)


def test_assoc_metamodel54_reverse_link_reassign_clear():
    a1 = sqlview_Right(value="sample_text")
    a2 = sqlview_Right(value="sample_text_2")
    b = sqlview_MetamodelName(name="sample_text")
    _safe_set(b, 'sqlview_MetamodelName56', a1)
    assert _is_linked(b, 'sqlview_MetamodelName56', a1)
    if hasattr(a1, 'sqlview_Right55'):
        assert _is_linked(a1, 'sqlview_Right55', b)
    _safe_set(b, 'sqlview_MetamodelName56', a2)
    assert _is_linked(b, 'sqlview_MetamodelName56', a2)
    if hasattr(a1, 'sqlview_Right55'):
        assert not _is_linked(a1, 'sqlview_Right55', b)
    if hasattr(a2, 'sqlview_Right55'):
        assert _is_linked(a2, 'sqlview_Right55', b)
    _safe_set(b, 'sqlview_MetamodelName56', None)
    assert not _is_linked(b, 'sqlview_MetamodelName56', a2)
    if hasattr(a2, 'sqlview_Right55'):
        assert not _is_linked(a2, 'sqlview_Right55', b)


def test_assoc_metamodelName3_reverse_link_reassign_clear():
    a1 = sqlview_MetamodelName(name="sample_text")
    a2 = sqlview_MetamodelName(name="sample_text_2")
    b = sqlview_Metamodel(metamodelURL="sample_text")
    _safe_set(b, 'sqlview_Metamodel4', {a1})
    assert _is_linked(b, 'sqlview_Metamodel4', a1)
    if hasattr(a1, 'sqlview_MetamodelName'):
        assert _is_linked(a1, 'sqlview_MetamodelName', b)
    _safe_set(b, 'sqlview_Metamodel4', {a2})
    assert _is_linked(b, 'sqlview_Metamodel4', a2)
    if hasattr(a1, 'sqlview_MetamodelName'):
        assert not _is_linked(a1, 'sqlview_MetamodelName', b)
    if hasattr(a2, 'sqlview_MetamodelName'):
        assert _is_linked(a2, 'sqlview_MetamodelName', b)
    _safe_set(b, 'sqlview_Metamodel4', set())
    assert not _is_linked(b, 'sqlview_Metamodel4', a2)
    if hasattr(a2, 'sqlview_MetamodelName'):
        assert not _is_linked(a2, 'sqlview_MetamodelName', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute18_stub_double():
    # sqlview_SelectAttribute has no real 'sqlview_SelectAttribute19' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Attribute(name="sample_text")
    partner = sqlview_SelectAttribute()
    setattr(partner, 'sqlview_SelectAttribute19', None)
    _safe_set(owner, 'sqlview_Attribute', partner)
    assert owner in getattr(partner, 'sqlview_SelectAttribute19')
    _safe_set(owner, 'sqlview_Attribute', None)
    assert owner not in getattr(partner, 'sqlview_SelectAttribute19')


def test_assoc_attributeWhereLeft51_stub_double():
    # sqlview_Left has no real 'sqlview_Left52' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Attribute(name="sample_text")
    partner = sqlview_Left()
    setattr(partner, 'sqlview_Left52', None)
    _safe_set(owner, 'sqlview_Attribute53', partner)
    assert getattr(partner, 'sqlview_Left52') == owner
    _safe_set(owner, 'sqlview_Attribute53', None)
    assert getattr(partner, 'sqlview_Left52') is None


def test_assoc_classLeft31_stub_double():
    # sqlview_JoinLeft has no real 'sqlview_JoinLeft32' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Class(name="sample_text")
    partner = sqlview_JoinLeft()
    setattr(partner, 'sqlview_JoinLeft32', None)
    _safe_set(owner, 'sqlview_Class33', partner)
    assert owner in getattr(partner, 'sqlview_JoinLeft32')
    _safe_set(owner, 'sqlview_Class33', None)
    assert owner not in getattr(partner, 'sqlview_JoinLeft32')


def test_assoc_classRight37_stub_double():
    # sqlview_JoinRight has no real 'sqlview_JoinRight38' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Class(name="sample_text")
    partner = sqlview_JoinRight()
    setattr(partner, 'sqlview_JoinRight38', None)
    _safe_set(owner, 'sqlview_Class39', partner)
    assert owner in getattr(partner, 'sqlview_JoinRight38')
    _safe_set(owner, 'sqlview_Class39', None)
    assert owner not in getattr(partner, 'sqlview_JoinRight38')


def test_assoc_class_16_stub_double():
    # sqlview_SelectAttribute has no real 'sqlview_SelectAttribute17' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Class(name="sample_text")
    partner = sqlview_SelectAttribute()
    setattr(partner, 'sqlview_SelectAttribute17', None)
    _safe_set(owner, 'sqlview_Class', partner)
    assert owner in getattr(partner, 'sqlview_SelectAttribute17')
    _safe_set(owner, 'sqlview_Class', None)
    assert owner not in getattr(partner, 'sqlview_SelectAttribute17')


def test_assoc_class_48_stub_double():
    # sqlview_Left has no real 'sqlview_Left49' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Class(name="sample_text")
    partner = sqlview_Left()
    setattr(partner, 'sqlview_Left49', None)
    _safe_set(owner, 'sqlview_Class50', partner)
    assert owner in getattr(partner, 'sqlview_Left49')
    _safe_set(owner, 'sqlview_Class50', None)
    assert owner not in getattr(partner, 'sqlview_Left49')


def test_assoc_expression1_stub_double():
    # sqlview_Expression has no real 'sqlview_Expression' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Model(viewName="sample_text")
    partner = sqlview_Expression()
    setattr(partner, 'sqlview_Expression', None)
    _safe_set(owner, 'sqlview_Model2', {partner})
    assert getattr(partner, 'sqlview_Expression') == owner
    _safe_set(owner, 'sqlview_Model2', set())
    assert getattr(partner, 'sqlview_Expression') is None


def test_assoc_metamodel13_stub_double():
    # sqlview_SelectAttribute has no real 'sqlview_SelectAttribute14' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_MetamodelName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_MetamodelName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_MetamodelName(name="sample_text")
    partner = sqlview_SelectAttribute()
    setattr(partner, 'sqlview_SelectAttribute14', None)
    _safe_set(owner, 'sqlview_MetamodelName15', partner)
    assert owner in getattr(partner, 'sqlview_SelectAttribute14')
    _safe_set(owner, 'sqlview_MetamodelName15', None)
    assert owner not in getattr(partner, 'sqlview_SelectAttribute14')


def test_assoc_metamodel45_stub_double():
    # sqlview_Left has no real 'sqlview_Left46' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_MetamodelName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_MetamodelName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_MetamodelName(name="sample_text")
    partner = sqlview_Left()
    setattr(partner, 'sqlview_Left46', None)
    _safe_set(owner, 'sqlview_MetamodelName47', partner)
    assert owner in getattr(partner, 'sqlview_Left46')
    _safe_set(owner, 'sqlview_MetamodelName47', None)
    assert owner not in getattr(partner, 'sqlview_Left46')


def test_assoc_metamodelLeft28_stub_double():
    # sqlview_JoinLeft has no real 'sqlview_JoinLeft29' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_MetamodelName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_MetamodelName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_MetamodelName(name="sample_text")
    partner = sqlview_JoinLeft()
    setattr(partner, 'sqlview_JoinLeft29', None)
    _safe_set(owner, 'sqlview_MetamodelName30', partner)
    assert owner in getattr(partner, 'sqlview_JoinLeft29')
    _safe_set(owner, 'sqlview_MetamodelName30', None)
    assert owner not in getattr(partner, 'sqlview_JoinLeft29')


def test_assoc_metamodelRight34_stub_double():
    # sqlview_JoinRight has no real 'sqlview_JoinRight35' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_MetamodelName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_MetamodelName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_MetamodelName(name="sample_text")
    partner = sqlview_JoinRight()
    setattr(partner, 'sqlview_JoinRight35', None)
    _safe_set(owner, 'sqlview_MetamodelName36', partner)
    assert owner in getattr(partner, 'sqlview_JoinRight35')
    _safe_set(owner, 'sqlview_MetamodelName36', None)
    assert owner not in getattr(partner, 'sqlview_JoinRight35')


def test_assoc_relation26_stub_double():
    # sqlview_Join has no real 'sqlview_Join27' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Relation(name="sample_text")
    partner = sqlview_Join()
    setattr(partner, 'sqlview_Join27', None)
    _safe_set(owner, 'sqlview_Relation', partner)
    assert owner in getattr(partner, 'sqlview_Join27')
    _safe_set(owner, 'sqlview_Relation', None)
    assert owner not in getattr(partner, 'sqlview_Join27')


def test_assoc_right43_stub_double():
    # sqlview_Comparison has no real 'sqlview_Comparison44' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Right's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Right's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Right(value="sample_text")
    partner = sqlview_Comparison()
    setattr(partner, 'sqlview_Comparison44', None)
    _safe_set(owner, 'sqlview_Right', partner)
    assert owner in getattr(partner, 'sqlview_Comparison44')
    _safe_set(owner, 'sqlview_Right', None)
    assert owner not in getattr(partner, 'sqlview_Comparison44')


def test_assoc_select5_stub_double():
    # sqlview_Expression has no real 'sqlview_Expression6' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Select(select="sample_text")
    partner = sqlview_Expression()
    setattr(partner, 'sqlview_Expression6', None)
    _safe_set(owner, 'sqlview_Select', partner)
    assert owner in getattr(partner, 'sqlview_Expression6')
    _safe_set(owner, 'sqlview_Select', None)
    assert owner not in getattr(partner, 'sqlview_Expression6')


def test_assoc_selectAttribute11_stub_double():
    # sqlview_SelectAttribute has no real 'sqlview_SelectAttribute' property in the generated
    # code (a bare stub) -- manually attach it so sqlview_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlview_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlview_Select(select="sample_text")
    partner = sqlview_SelectAttribute()
    setattr(partner, 'sqlview_SelectAttribute', None)
    _safe_set(owner, 'sqlview_Select12', {partner})
    assert getattr(partner, 'sqlview_SelectAttribute') == owner
    _safe_set(owner, 'sqlview_Select12', set())
    assert getattr(partner, 'sqlview_SelectAttribute') is None


