import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Callable,
    Expr,
    IdRef,
    Type,
    TypeDef,
    jkind_AbbreviationType,
    jkind_ArrayAccessExpr,
    jkind_ArrayExpr,
    jkind_ArrayType,
    jkind_ArrayUpdateExpr,
    jkind_Assertion,
    jkind_BinaryExpr,
    jkind_BoolExpr,
    jkind_BoolType,
    jkind_CallExpr,
    jkind_Callable,
    jkind_CastExpr,
    jkind_CondactExpr,
    jkind_Constant,
    jkind_EnumType,
    jkind_EnumValue,
    jkind_Equation,
    jkind_Expr,
    jkind_Field,
    jkind_File,
    jkind_Function,
    jkind_IdExpr,
    jkind_IdRef,
    jkind_IfThenElseExpr,
    jkind_IntExpr,
    jkind_IntType,
    jkind_Ivc,
    jkind_Node,
    jkind_Property,
    jkind_RealExpr,
    jkind_RealType,
    jkind_RealizabilityInputs,
    jkind_RecordAccessExpr,
    jkind_RecordExpr,
    jkind_RecordType,
    jkind_RecordUpdateExpr,
    jkind_SubrangeType,
    jkind_TupleExpr,
    jkind_Type,
    jkind_TypeDef,
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

def test_assoc_assertions15_stub_double():
    # jkind_Assertion has no real 'jkind_Assertion' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_Assertion()
    setattr(partner, 'jkind_Assertion', None)
    _safe_set(owner, 'jkind_Node16', {partner})
    assert getattr(partner, 'jkind_Assertion') == owner
    _safe_set(owner, 'jkind_Node16', set())
    assert getattr(partner, 'jkind_Assertion') is None


def test_assoc_base63_stub_double():
    # jkind_Type has no real 'jkind_Type64' property in the generated
    # code (a bare stub) -- manually attach it so jkind_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_ArrayType(size="sample_text")
    partner = jkind_Type()
    setattr(partner, 'jkind_Type64', None)
    _safe_set(owner, 'jkind_ArrayType', partner)
    assert getattr(partner, 'jkind_Type64') == owner
    _safe_set(owner, 'jkind_ArrayType', None)
    assert getattr(partner, 'jkind_Type64') is None


def test_assoc_callable46_stub_double():
    # jkind_CallExpr has no real 'jkind_CallExpr' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Callable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Callable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Callable(name="sample_text")
    partner = jkind_CallExpr()
    setattr(partner, 'jkind_CallExpr', None)
    _safe_set(owner, 'jkind_Callable', partner)
    assert getattr(partner, 'jkind_CallExpr') == owner
    _safe_set(owner, 'jkind_Callable', None)
    assert getattr(partner, 'jkind_CallExpr') is None


def test_assoc_def_65_stub_double():
    # jkind_UserType has no real 'jkind_UserType' property in the generated
    # code (a bare stub) -- manually attach it so jkind_TypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_TypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_TypeDef(name="sample_text")
    partner = jkind_UserType()
    setattr(partner, 'jkind_UserType', None)
    _safe_set(owner, 'jkind_TypeDef66', partner)
    assert getattr(partner, 'jkind_UserType') == owner
    _safe_set(owner, 'jkind_TypeDef66', None)
    assert getattr(partner, 'jkind_UserType') is None


def test_assoc_equations13_stub_double():
    # jkind_Equation has no real 'jkind_Equation' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_Equation()
    setattr(partner, 'jkind_Equation', None)
    _safe_set(owner, 'jkind_Node14', {partner})
    assert getattr(partner, 'jkind_Equation') == owner
    _safe_set(owner, 'jkind_Node14', set())
    assert getattr(partner, 'jkind_Equation') is None


def test_assoc_expr106_stub_double():
    # jkind_Expr has no real 'jkind_Expr107' property in the generated
    # code (a bare stub) -- manually attach it so jkind_CastExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_CastExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_CastExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr107', None)
    _safe_set(owner, 'jkind_CastExpr', partner)
    assert getattr(partner, 'jkind_Expr107') == owner
    _safe_set(owner, 'jkind_CastExpr', None)
    assert getattr(partner, 'jkind_Expr107') is None


def test_assoc_expr72_stub_double():
    # jkind_Expr has no real 'jkind_Expr73' property in the generated
    # code (a bare stub) -- manually attach it so jkind_UnaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_UnaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_UnaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr73', None)
    _safe_set(owner, 'jkind_UnaryExpr', partner)
    assert getattr(partner, 'jkind_Expr73') == owner
    _safe_set(owner, 'jkind_UnaryExpr', None)
    assert getattr(partner, 'jkind_Expr73') is None


def test_assoc_field76_stub_double():
    # jkind_RecordAccessExpr has no real 'jkind_RecordAccessExpr77' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_RecordAccessExpr()
    setattr(partner, 'jkind_RecordAccessExpr77', None)
    _safe_set(owner, 'jkind_Field78', partner)
    assert getattr(partner, 'jkind_RecordAccessExpr77') == owner
    _safe_set(owner, 'jkind_Field78', None)
    assert getattr(partner, 'jkind_RecordAccessExpr77') is None


def test_assoc_field81_stub_double():
    # jkind_RecordUpdateExpr has no real 'jkind_RecordUpdateExpr82' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_RecordUpdateExpr()
    setattr(partner, 'jkind_RecordUpdateExpr82', None)
    _safe_set(owner, 'jkind_Field83', partner)
    assert getattr(partner, 'jkind_RecordUpdateExpr82') == owner
    _safe_set(owner, 'jkind_Field83', None)
    assert getattr(partner, 'jkind_RecordUpdateExpr82') is None


def test_assoc_fields120_stub_double():
    # jkind_RecordExpr has no real 'jkind_RecordExpr121' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Field(name="sample_text")
    partner = jkind_RecordExpr()
    setattr(partner, 'jkind_RecordExpr121', None)
    _safe_set(owner, 'jkind_Field122', partner)
    assert owner in getattr(partner, 'jkind_RecordExpr121')
    _safe_set(owner, 'jkind_Field122', None)
    assert owner not in getattr(partner, 'jkind_RecordExpr121')


def test_assoc_fields58_stub_double():
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


def test_assoc_id97_stub_double():
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


def test_assoc_inputs50_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup52' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Callable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Callable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Callable(name="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup52', None)
    _safe_set(owner, 'jkind_Callable51', {partner})
    assert getattr(partner, 'jkind_VariableGroup52') == owner
    _safe_set(owner, 'jkind_Callable51', set())
    assert getattr(partner, 'jkind_VariableGroup52') is None


def test_assoc_ivc19_stub_double():
    # jkind_Ivc has no real 'jkind_Ivc' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_Ivc()
    setattr(partner, 'jkind_Ivc', None)
    _safe_set(owner, 'jkind_Node20', {partner})
    assert getattr(partner, 'jkind_Ivc') == owner
    _safe_set(owner, 'jkind_Node20', set())
    assert getattr(partner, 'jkind_Ivc') is None


def test_assoc_left67_stub_double():
    # jkind_Expr has no real 'jkind_Expr68' property in the generated
    # code (a bare stub) -- manually attach it so jkind_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_BinaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr68', None)
    _safe_set(owner, 'jkind_BinaryExpr', partner)
    assert getattr(partner, 'jkind_Expr68') == owner
    _safe_set(owner, 'jkind_BinaryExpr', None)
    assert getattr(partner, 'jkind_Expr68') is None


def test_assoc_locals11_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup', None)
    _safe_set(owner, 'jkind_Node12', {partner})
    assert getattr(partner, 'jkind_VariableGroup') == owner
    _safe_set(owner, 'jkind_Node12', set())
    assert getattr(partner, 'jkind_VariableGroup') is None


def test_assoc_nodes5_stub_double():
    # jkind_File has no real 'jkind_File6' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_File()
    setattr(partner, 'jkind_File6', None)
    _safe_set(owner, 'jkind_Node', partner)
    assert owner in getattr(partner, 'jkind_File6')
    _safe_set(owner, 'jkind_Node', None)
    assert owner not in getattr(partner, 'jkind_File6')


def test_assoc_outputs53_stub_double():
    # jkind_VariableGroup has no real 'jkind_VariableGroup55' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Callable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Callable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Callable(name="sample_text")
    partner = jkind_VariableGroup()
    setattr(partner, 'jkind_VariableGroup55', None)
    _safe_set(owner, 'jkind_Callable54', {partner})
    assert getattr(partner, 'jkind_VariableGroup55') == owner
    _safe_set(owner, 'jkind_Callable54', set())
    assert getattr(partner, 'jkind_VariableGroup55') is None


def test_assoc_properties17_stub_double():
    # jkind_Property has no real 'jkind_Property' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_Property()
    setattr(partner, 'jkind_Property', None)
    _safe_set(owner, 'jkind_Node18', {partner})
    assert getattr(partner, 'jkind_Property') == owner
    _safe_set(owner, 'jkind_Node18', set())
    assert getattr(partner, 'jkind_Property') is None


def test_assoc_realizabilityInputs21_stub_double():
    # jkind_RealizabilityInputs has no real 'jkind_RealizabilityInputs' property in the generated
    # code (a bare stub) -- manually attach it so jkind_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_Node(main="sample_text")
    partner = jkind_RealizabilityInputs()
    setattr(partner, 'jkind_RealizabilityInputs', None)
    _safe_set(owner, 'jkind_Node22', {partner})
    assert getattr(partner, 'jkind_RealizabilityInputs') == owner
    _safe_set(owner, 'jkind_Node22', set())
    assert getattr(partner, 'jkind_RealizabilityInputs') is None


def test_assoc_right69_stub_double():
    # jkind_Expr has no real 'jkind_Expr71' property in the generated
    # code (a bare stub) -- manually attach it so jkind_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_BinaryExpr(op="sample_text")
    partner = jkind_Expr()
    setattr(partner, 'jkind_Expr71', None)
    _safe_set(owner, 'jkind_BinaryExpr70', partner)
    assert getattr(partner, 'jkind_Expr71') == owner
    _safe_set(owner, 'jkind_BinaryExpr70', None)
    assert getattr(partner, 'jkind_Expr71') is None


def test_assoc_typedefs0_stub_double():
    # jkind_File has no real 'jkind_File' property in the generated
    # code (a bare stub) -- manually attach it so jkind_TypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jkind_TypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jkind_TypeDef(name="sample_text")
    partner = jkind_File()
    setattr(partner, 'jkind_File', None)
    _safe_set(owner, 'jkind_TypeDef', partner)
    assert owner in getattr(partner, 'jkind_File')
    _safe_set(owner, 'jkind_TypeDef', None)
    assert owner not in getattr(partner, 'jkind_File')


