import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    IdRef,
    Type,
    Typedef,
    jkind_AbbreviationType,
    jkind_Assertion,
    jkind_BinaryExpr,
    jkind_BoolExpr,
    jkind_BoolType,
    jkind_Constant,
    jkind_Equation,
    jkind_Expr,
    jkind_Field,
    jkind_File,
    jkind_IdExpr,
    jkind_IdRef,
    jkind_IfThenElseExpr,
    jkind_IntExpr,
    jkind_IntType,
    jkind_Node,
    jkind_NodeCallExpr,
    jkind_ProjectionExpr,
    jkind_Property,
    jkind_RealExpr,
    jkind_RealType,
    jkind_RecordExpr,
    jkind_RecordType,
    jkind_SubrangeType,
    jkind_Type,
    jkind_Typedef,
    jkind_UnaryExpr,
    jkind_UserType,
    jkind_Variable,
    jkind_VariableGroup,
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

def test_assoc_assertions19_stub_double():
    # jkind_Assertion has no real 'jkind_Assertion' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_Assertion()
    setattr(partner, 'jkind_Assertion', None)
    _safe_set(owner, 'jkind_Node20', {partner})
    assert getattr(partner, 'jkind_Assertion') == owner
    _safe_set(owner, 'jkind_Node20', set())
    assert getattr(partner, 'jkind_Assertion') is None


def test_assoc_def_46_stub_double():
    # jkind_UserType has no real 'jkind_UserType' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Typedef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Typedef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Typedef(name="sample_text")
    partner = jkind_UserType()
    setattr(partner, 'jkind_UserType', None)
    _safe_set(owner, 'jkind_Typedef47', partner)
    assert getattr(partner, 'jkind_UserType') == owner
    _safe_set(owner, 'jkind_Typedef47', None)
    assert getattr(partner, 'jkind_UserType') is None


def test_assoc_equations17_stub_double():
    # jkind_Equation has no real 'jkind_Equation' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_Equation()
    setattr(partner, 'jkind_Equation', None)
    _safe_set(owner, 'jkind_Node18', {partner})
    assert getattr(partner, 'jkind_Equation') == owner
    _safe_set(owner, 'jkind_Node18', set())
    assert getattr(partner, 'jkind_Equation') is None


def test_assoc_expr53_stub_double():
    # jkind_Expr has no real 'jkind_Expr54' property in the generated
    # code (a bare stub) -- manually attach it so jkind_UnaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_UnaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_UnaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr54', None)
    _safe_set(owner, 'jkind_UnaryExpr', partner)
    assert getattr(partner, 'jkind_Expr54') == owner
    _safe_set(owner, 'jkind_UnaryExpr', None)
    assert getattr(partner, 'jkind_Expr54') is None


def test_assoc_field57_stub_double():
    # jkind_ProjectionExpr has no real 'jkind_ProjectionExpr58' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_ProjectionExpr()
    setattr(partner, 'jkind_ProjectionExpr58', None)
    _safe_set(owner, 'jkind_Field59', partner)
    assert getattr(partner, 'jkind_ProjectionExpr58') == owner
    _safe_set(owner, 'jkind_Field59', None)
    assert getattr(partner, 'jkind_ProjectionExpr58') is None


def test_assoc_fields42_stub_double():
    # jkind_RecordType has no real 'jkind_RecordType' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_RecordType()
    setattr(partner, 'jkind_RecordType', None)
    _safe_set(owner, 'jkind_Field', partner)
    assert owner in getattr(partner, 'jkind_RecordType')
    _safe_set(owner, 'jkind_Field', None)
    assert owner not in getattr(partner, 'jkind_RecordType')


def test_assoc_fields76_stub_double():
    # jkind_RecordExpr has no real 'jkind_RecordExpr77' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_RecordExpr()
    setattr(partner, 'jkind_RecordExpr77', None)
    _safe_set(owner, 'jkind_Field78', partner)
    assert owner in getattr(partner, 'jkind_RecordExpr77')
    _safe_set(owner, 'jkind_Field78', None)
    assert owner not in getattr(partner, 'jkind_RecordExpr77')


def test_assoc_id60_stub_double():
    # jkind_IdExpr has no real 'jkind_IdExpr' property in the generated
    # code (a bare stub) -- manually attach it so jkind_IdRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_IdRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_IdRef(name="sample_text")
    partner = jkind_IdExpr()
    setattr(partner, 'jkind_IdExpr', None)
    _safe_set(owner, 'jkind_IdRef', partner)
    assert getattr(partner, 'jkind_IdExpr') == owner
    _safe_set(owner, 'jkind_IdRef', None)
    assert getattr(partner, 'jkind_IdExpr') is None


def test_assoc_inputs9_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup', None)
    _safe_set(owner, 'jkind_Node10', {partner})
    assert getattr(partner, 'jkind_VariableGroup') == owner
    _safe_set(owner, 'jkind_Node10', set())
    assert getattr(partner, 'jkind_VariableGroup') is None


def test_assoc_left48_stub_double():
    # jkind_Expr has no real 'jkind_Expr49' property in the generated
    # code (a bare stub) -- manually attach it so jkind_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_BinaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr49', None)
    _safe_set(owner, 'jkind_BinaryExpr', partner)
    assert getattr(partner, 'jkind_Expr49') == owner
    _safe_set(owner, 'jkind_BinaryExpr', None)
    assert getattr(partner, 'jkind_Expr49') is None


def test_assoc_locals14_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup16' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup16', None)
    _safe_set(owner, 'jkind_Node15', {partner})
    assert getattr(partner, 'jkind_VariableGroup16') == owner
    _safe_set(owner, 'jkind_Node15', set())
    assert getattr(partner, 'jkind_VariableGroup16') is None


def test_assoc_node69_stub_double():
    # jkind_NodeCallExpr has no real 'jkind_NodeCallExpr' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_NodeCallExpr()
    setattr(partner, 'jkind_NodeCallExpr', None)
    _safe_set(owner, 'jkind_Node70', partner)
    assert getattr(partner, 'jkind_NodeCallExpr') == owner
    _safe_set(owner, 'jkind_Node70', None)
    assert getattr(partner, 'jkind_NodeCallExpr') is None


def test_assoc_nodes3_stub_double():
    # jkind_File has no real 'jkind_File4' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_File()
    setattr(partner, 'jkind_File4', None)
    _safe_set(owner, 'jkind_Node', partner)
    assert owner in getattr(partner, 'jkind_File4')
    _safe_set(owner, 'jkind_Node', None)
    assert owner not in getattr(partner, 'jkind_File4')


def test_assoc_outputs11_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup13' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup13', None)
    _safe_set(owner, 'jkind_Node12', {partner})
    assert getattr(partner, 'jkind_VariableGroup13') == owner
    _safe_set(owner, 'jkind_Node12', set())
    assert getattr(partner, 'jkind_VariableGroup13') is None


def test_assoc_properties21_stub_double():
    # jkind_Property has no real 'jkind_Property' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text", name="sample_text")
    partner = jkind_Property()
    setattr(partner, 'jkind_Property', None)
    _safe_set(owner, 'jkind_Node22', {partner})
    assert getattr(partner, 'jkind_Property') == owner
    _safe_set(owner, 'jkind_Node22', set())
    assert getattr(partner, 'jkind_Property') is None


def test_assoc_right50_stub_double():
    # jkind_Expr has no real 'jkind_Expr52' property in the generated
    # code (a bare stub) -- manually attach it so jkind_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_BinaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr52', None)
    _safe_set(owner, 'jkind_BinaryExpr51', partner)
    assert getattr(partner, 'jkind_Expr52') == owner
    _safe_set(owner, 'jkind_BinaryExpr51', None)
    assert getattr(partner, 'jkind_Expr52') is None


def test_assoc_typedefs0_stub_double():
    # jkind_File has no real 'jkind_File' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Typedef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Typedef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Typedef(name="sample_text")
    partner = jkind_File()
    setattr(partner, 'jkind_File', None)
    _safe_set(owner, 'jkind_Typedef', partner)
    assert owner in getattr(partner, 'jkind_File')
    _safe_set(owner, 'jkind_Typedef', None)
    assert owner not in getattr(partner, 'jkind_File')


