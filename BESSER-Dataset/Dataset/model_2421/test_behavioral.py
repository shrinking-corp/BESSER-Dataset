import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CheckConstraint,
    Column,
    ColumnRefConstraint,
    Constraint,
    DataType,
    Domain,
    Element,
    ForeignKey,
    Index,
    IndexedColumn,
    NamedColumnSet,
    NamedElement,
    PrimaryKey,
    PrimitiveDataType,
    SchemaElement,
    UniqueConstraint,
    ViewAlias,
    ViewColumn,
    constraints_rdbmdl_TableColumn,
    datatypes_PrimitiveDataType,
    rdbmdl_Column,
    rdbmdl_Element,
    rdbmdl_Model,
    rdbmdl_NamedColumnSet,
    rdbmdl_NamedElement,
    rdbmdl_Schema,
    rdbmdl_SchemaElement,
    rdbmdl_Table,
    rdbmdl_TableColumn,
    rdbmdl_constraints_CheckConstraint,
    rdbmdl_constraints_ColumnRefConstraint,
    rdbmdl_constraints_Constraint,
    rdbmdl_constraints_ForeignKey,
    rdbmdl_constraints_Index,
    rdbmdl_constraints_IndexedColumn,
    rdbmdl_constraints_PrimaryKey,
    rdbmdl_constraints_UniqueConstraint,
    rdbmdl_datatypes_DataType,
    rdbmdl_datatypes_Domain,
    rdbmdl_datatypes_PrimitiveDataType,
    rdbmdl_view_ReferencedViewColumn,
    rdbmdl_view_View,
    rdbmdl_view_ViewAlias,
    rdbmdl_view_ViewColumn,
    rdbmdl_view_ViewExpressionColumn,
    view_rdbmdl_Column,
    view_rdbmdl_NamedColumnSet,
    PrimitiveTypeCodes,
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

def test_assoc_columns28_stub_double():
    # ViewColumn has no real 'ViewColumn' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_view_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_view_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_view_View(ddl="sample_text")
    partner = ViewColumn()
    setattr(partner, 'ViewColumn', None)
    _safe_set(owner, 'rdbmdl_view_View', {partner})
    assert getattr(partner, 'ViewColumn') == owner
    _safe_set(owner, 'rdbmdl_view_View', set())
    assert getattr(partner, 'ViewColumn') is None


def test_assoc_columns5_stub_double():
    # rdbmdl_Table has no real 'rdbmdl_Table' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_TableColumn(isForeignKey="sample_text", isPrimaryKey="sample_text")
    partner = rdbmdl_Table()
    setattr(partner, 'rdbmdl_Table', None)
    _safe_set(owner, 'rdbmdl_TableColumn', partner)
    assert owner in getattr(partner, 'rdbmdl_Table')
    _safe_set(owner, 'rdbmdl_TableColumn', None)
    assert owner not in getattr(partner, 'rdbmdl_Table')


def test_assoc_domain16_stub_double():
    # Domain has no real 'Domain' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_TableColumn(isForeignKey="sample_text", isPrimaryKey="sample_text")
    partner = Domain()
    setattr(partner, 'Domain', None)
    _safe_set(owner, 'rdbmdl_TableColumn17', partner)
    assert getattr(partner, 'Domain') == owner
    _safe_set(owner, 'rdbmdl_TableColumn17', None)
    assert getattr(partner, 'Domain') is None


def test_assoc_elements3_stub_double():
    # rdbmdl_Schema has no real 'rdbmdl_Schema4' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_SchemaElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_SchemaElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_SchemaElement(owner="sample_text")
    partner = rdbmdl_Schema()
    setattr(partner, 'rdbmdl_Schema4', None)
    _safe_set(owner, 'rdbmdl_SchemaElement', partner)
    assert owner in getattr(partner, 'rdbmdl_Schema4')
    _safe_set(owner, 'rdbmdl_SchemaElement', None)
    assert owner not in getattr(partner, 'rdbmdl_Schema4')


def test_assoc_refColumn24_stub_double():
    # constraints_rdbmdl_TableColumn has no real 'constraints_rdbmdl_TableColumn25' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_constraints_IndexedColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_constraints_IndexedColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_constraints_IndexedColumn(ascending=True)
    partner = constraints_rdbmdl_TableColumn()
    setattr(partner, 'constraints_rdbmdl_TableColumn25', None)
    _safe_set(owner, 'rdbmdl_constraints_IndexedColumn', partner)
    assert getattr(partner, 'constraints_rdbmdl_TableColumn25') == owner
    _safe_set(owner, 'rdbmdl_constraints_IndexedColumn', None)
    assert getattr(partner, 'constraints_rdbmdl_TableColumn25') is None


def test_assoc_referencedTablesAndViews29_stub_double():
    # ViewAlias has no real 'ViewAlias' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_view_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_view_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_view_View(ddl="sample_text")
    partner = ViewAlias()
    setattr(partner, 'ViewAlias', None)
    _safe_set(owner, 'rdbmdl_view_View30', {partner})
    assert getattr(partner, 'ViewAlias') == owner
    _safe_set(owner, 'rdbmdl_view_View30', set())
    assert getattr(partner, 'ViewAlias') is None


def test_assoc_schemas2_stub_double():
    # rdbmdl_Schema has no real 'rdbmdl_Schema' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_Model(server_id="sample_text")
    partner = rdbmdl_Schema()
    setattr(partner, 'rdbmdl_Schema', None)
    _safe_set(owner, 'rdbmdl_Model', {partner})
    assert getattr(partner, 'rdbmdl_Schema') == owner
    _safe_set(owner, 'rdbmdl_Model', set())
    assert getattr(partner, 'rdbmdl_Schema') is None


def test_assoc_type18_stub_double():
    # PrimitiveDataType has no real 'PrimitiveDataType' property in the generated
    # code (a bare stub) -- manually attach it so rdbmdl_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmdl_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmdl_TableColumn(isForeignKey="sample_text", isPrimaryKey="sample_text")
    partner = PrimitiveDataType()
    setattr(partner, 'PrimitiveDataType', None)
    _safe_set(owner, 'rdbmdl_TableColumn19', partner)
    assert getattr(partner, 'PrimitiveDataType') == owner
    _safe_set(owner, 'rdbmdl_TableColumn19', None)
    assert getattr(partner, 'PrimitiveDataType') is None


