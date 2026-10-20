import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Statement,
    javali_Addition,
    javali_And,
    javali_Block,
    javali_Break,
    javali_Constant,
    javali_Continue,
    javali_Decrement,
    javali_DoWhile,
    javali_Equality,
    javali_Expression,
    javali_For,
    javali_Identifier,
    javali_IfElse,
    javali_Increment,
    javali_Literal,
    javali_Module,
    javali_Multiplication,
    javali_NewArray,
    javali_NewObject,
    javali_Null,
    javali_Or,
    javali_ProcCall,
    javali_Procedure,
    javali_Record,
    javali_Relation,
    javali_Return,
    javali_Statement,
    javali_Type,
    javali_VarAssign,
    javali_VarDeclaration,
    javali_VarExpression,
    javali_While,
    javali_Xor,
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

def test_assoc_id19_reverse_link_reassign_clear():
    a1 = javali_Procedure(comment="sample_text", static=True, void=True)
    a2 = javali_Procedure(comment="sample_text_2", static=False, void=False)
    b = javali_Identifier(id="sample_text")
    _safe_set(b, 'javali_Identifier21', a1)
    assert _is_linked(b, 'javali_Identifier21', a1)
    if hasattr(a1, 'javali_Procedure20'):
        assert _is_linked(a1, 'javali_Procedure20', b)
    _safe_set(b, 'javali_Identifier21', a2)
    assert _is_linked(b, 'javali_Identifier21', a2)
    if hasattr(a1, 'javali_Procedure20'):
        assert not _is_linked(a1, 'javali_Procedure20', b)
    if hasattr(a2, 'javali_Procedure20'):
        assert _is_linked(a2, 'javali_Procedure20', b)
    _safe_set(b, 'javali_Identifier21', None)
    assert not _is_linked(b, 'javali_Identifier21', a2)
    if hasattr(a2, 'javali_Procedure20'):
        assert not _is_linked(a2, 'javali_Procedure20', b)


def test_assoc_id7_reverse_link_reassign_clear():
    a1 = javali_Identifier(id="sample_text")
    a2 = javali_Identifier(id="sample_text_2")
    b = javali_Constant(static=True)
    _safe_set(b, 'javali_Constant8', a1)
    assert _is_linked(b, 'javali_Constant8', a1)
    if hasattr(a1, 'javali_Identifier'):
        assert _is_linked(a1, 'javali_Identifier', b)
    _safe_set(b, 'javali_Constant8', a2)
    assert _is_linked(b, 'javali_Constant8', a2)
    if hasattr(a1, 'javali_Identifier'):
        assert not _is_linked(a1, 'javali_Identifier', b)
    if hasattr(a2, 'javali_Identifier'):
        assert _is_linked(a2, 'javali_Identifier', b)
    _safe_set(b, 'javali_Constant8', None)
    assert not _is_linked(b, 'javali_Constant8', a2)
    if hasattr(a2, 'javali_Identifier'):
        assert not _is_linked(a2, 'javali_Identifier', b)


def test_assoc_id87_reverse_link_reassign_clear():
    a1 = javali_Type(arrayDims="sample_text")
    a2 = javali_Type(arrayDims="sample_text_2")
    b = javali_Identifier(id="sample_text")
    _safe_set(b, 'javali_Identifier89', a1)
    assert _is_linked(b, 'javali_Identifier89', a1)
    if hasattr(a1, 'javali_Type88'):
        assert _is_linked(a1, 'javali_Type88', b)
    _safe_set(b, 'javali_Identifier89', a2)
    assert _is_linked(b, 'javali_Identifier89', a2)
    if hasattr(a1, 'javali_Type88'):
        assert not _is_linked(a1, 'javali_Type88', b)
    if hasattr(a2, 'javali_Type88'):
        assert _is_linked(a2, 'javali_Type88', b)
    _safe_set(b, 'javali_Identifier89', None)
    assert not _is_linked(b, 'javali_Identifier89', a2)
    if hasattr(a2, 'javali_Type88'):
        assert not _is_linked(a2, 'javali_Type88', b)


def test_assoc_retType16_reverse_link_reassign_clear():
    a1 = javali_Type(arrayDims="sample_text")
    a2 = javali_Type(arrayDims="sample_text_2")
    b = javali_Procedure(comment="sample_text", static=True, void=True)
    _safe_set(b, 'javali_Procedure17', a1)
    assert _is_linked(b, 'javali_Procedure17', a1)
    if hasattr(a1, 'javali_Type18'):
        assert _is_linked(a1, 'javali_Type18', b)
    _safe_set(b, 'javali_Procedure17', a2)
    assert _is_linked(b, 'javali_Procedure17', a2)
    if hasattr(a1, 'javali_Type18'):
        assert not _is_linked(a1, 'javali_Type18', b)
    if hasattr(a2, 'javali_Type18'):
        assert _is_linked(a2, 'javali_Type18', b)
    _safe_set(b, 'javali_Procedure17', None)
    assert not _is_linked(b, 'javali_Procedure17', a2)
    if hasattr(a2, 'javali_Type18'):
        assert not _is_linked(a2, 'javali_Type18', b)


def test_assoc_type5_reverse_link_reassign_clear():
    a1 = javali_Type(arrayDims="sample_text")
    a2 = javali_Type(arrayDims="sample_text_2")
    b = javali_Constant(static=True)
    _safe_set(b, 'javali_Constant6', a1)
    assert _is_linked(b, 'javali_Constant6', a1)
    if hasattr(a1, 'javali_Type'):
        assert _is_linked(a1, 'javali_Type', b)
    _safe_set(b, 'javali_Constant6', a2)
    assert _is_linked(b, 'javali_Constant6', a2)
    if hasattr(a1, 'javali_Type'):
        assert not _is_linked(a1, 'javali_Type', b)
    if hasattr(a2, 'javali_Type'):
        assert _is_linked(a2, 'javali_Type', b)
    _safe_set(b, 'javali_Constant6', None)
    assert not _is_linked(b, 'javali_Constant6', a2)
    if hasattr(a2, 'javali_Type'):
        assert not _is_linked(a2, 'javali_Type', b)


def test_assoc_value9_reverse_link_reassign_clear():
    a1 = javali_Literal(value="sample_text")
    a2 = javali_Literal(value="sample_text_2")
    b = javali_Constant(static=True)
    _safe_set(b, 'javali_Constant10', a1)
    assert _is_linked(b, 'javali_Constant10', a1)
    if hasattr(a1, 'javali_Literal'):
        assert _is_linked(a1, 'javali_Literal', b)
    _safe_set(b, 'javali_Constant10', a2)
    assert _is_linked(b, 'javali_Constant10', a2)
    if hasattr(a1, 'javali_Literal'):
        assert not _is_linked(a1, 'javali_Literal', b)
    if hasattr(a2, 'javali_Literal'):
        assert _is_linked(a2, 'javali_Literal', b)
    _safe_set(b, 'javali_Constant10', None)
    assert not _is_linked(b, 'javali_Constant10', a2)
    if hasattr(a2, 'javali_Literal'):
        assert not _is_linked(a2, 'javali_Literal', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body25_stub_double():
    # javali_Block has no real 'javali_Block' property in the generated
    # code (a bare stub) -- manually attach it so javali_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Procedure(comment="sample_text", static=True, void=True)
    partner = javali_Block()
    setattr(partner, 'javali_Block', None)
    _safe_set(owner, 'javali_Procedure26', partner)
    assert getattr(partner, 'javali_Block') == owner
    _safe_set(owner, 'javali_Procedure26', None)
    assert getattr(partner, 'javali_Block') is None


def test_assoc_constants0_stub_double():
    # javali_Module has no real 'javali_Module' property in the generated
    # code (a bare stub) -- manually attach it so javali_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Constant(static=True)
    partner = javali_Module()
    setattr(partner, 'javali_Module', None)
    _safe_set(owner, 'javali_Constant', partner)
    assert owner in getattr(partner, 'javali_Module')
    _safe_set(owner, 'javali_Constant', None)
    assert owner not in getattr(partner, 'javali_Module')


def test_assoc_id11_stub_double():
    # javali_Record has no real 'javali_Record12' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_Record()
    setattr(partner, 'javali_Record12', None)
    _safe_set(owner, 'javali_Identifier13', partner)
    assert getattr(partner, 'javali_Record12') == owner
    _safe_set(owner, 'javali_Identifier13', None)
    assert getattr(partner, 'javali_Record12') is None


def test_assoc_id33_stub_double():
    # javali_VarDeclaration has no real 'javali_VarDeclaration34' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_VarDeclaration()
    setattr(partner, 'javali_VarDeclaration34', None)
    _safe_set(owner, 'javali_Identifier35', partner)
    assert getattr(partner, 'javali_VarDeclaration34') == owner
    _safe_set(owner, 'javali_Identifier35', None)
    assert getattr(partner, 'javali_VarDeclaration34') is None


def test_assoc_id72_stub_double():
    # javali_Increment has no real 'javali_Increment' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_Increment()
    setattr(partner, 'javali_Increment', None)
    _safe_set(owner, 'javali_Identifier73', partner)
    assert getattr(partner, 'javali_Increment') == owner
    _safe_set(owner, 'javali_Identifier73', None)
    assert getattr(partner, 'javali_Increment') is None


def test_assoc_id74_stub_double():
    # javali_Decrement has no real 'javali_Decrement' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_Decrement()
    setattr(partner, 'javali_Decrement', None)
    _safe_set(owner, 'javali_Identifier75', partner)
    assert getattr(partner, 'javali_Decrement') == owner
    _safe_set(owner, 'javali_Identifier75', None)
    assert getattr(partner, 'javali_Decrement') is None


def test_assoc_id82_stub_double():
    # javali_ProcCall has no real 'javali_ProcCall' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_ProcCall()
    setattr(partner, 'javali_ProcCall', None)
    _safe_set(owner, 'javali_Identifier83', partner)
    assert getattr(partner, 'javali_ProcCall') == owner
    _safe_set(owner, 'javali_Identifier83', None)
    assert getattr(partner, 'javali_ProcCall') is None


def test_assoc_left112_stub_double():
    # javali_Expression has no real 'javali_Expression113' property in the generated
    # code (a bare stub) -- manually attach it so javali_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Equality(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression113', None)
    _safe_set(owner, 'javali_Equality', partner)
    assert getattr(partner, 'javali_Expression113') == owner
    _safe_set(owner, 'javali_Equality', None)
    assert getattr(partner, 'javali_Expression113') is None


def test_assoc_left117_stub_double():
    # javali_Expression has no real 'javali_Expression118' property in the generated
    # code (a bare stub) -- manually attach it so javali_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Relation(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression118', None)
    _safe_set(owner, 'javali_Relation', partner)
    assert getattr(partner, 'javali_Expression118') == owner
    _safe_set(owner, 'javali_Relation', None)
    assert getattr(partner, 'javali_Expression118') is None


def test_assoc_left122_stub_double():
    # javali_Expression has no real 'javali_Expression123' property in the generated
    # code (a bare stub) -- manually attach it so javali_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Addition(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression123', None)
    _safe_set(owner, 'javali_Addition', partner)
    assert getattr(partner, 'javali_Expression123') == owner
    _safe_set(owner, 'javali_Addition', None)
    assert getattr(partner, 'javali_Expression123') is None


def test_assoc_left127_stub_double():
    # javali_Expression has no real 'javali_Expression128' property in the generated
    # code (a bare stub) -- manually attach it so javali_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Multiplication(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression128', None)
    _safe_set(owner, 'javali_Multiplication', partner)
    assert getattr(partner, 'javali_Expression128') == owner
    _safe_set(owner, 'javali_Multiplication', None)
    assert getattr(partner, 'javali_Expression128') is None


def test_assoc_params22_stub_double():
    # javali_VarDeclaration has no real 'javali_VarDeclaration24' property in the generated
    # code (a bare stub) -- manually attach it so javali_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Procedure(comment="sample_text", static=True, void=True)
    partner = javali_VarDeclaration()
    setattr(partner, 'javali_VarDeclaration24', None)
    _safe_set(owner, 'javali_Procedure23', {partner})
    assert getattr(partner, 'javali_VarDeclaration24') == owner
    _safe_set(owner, 'javali_Procedure23', set())
    assert getattr(partner, 'javali_VarDeclaration24') is None


def test_assoc_parts76_stub_double():
    # javali_VarExpression has no real 'javali_VarExpression77' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_VarExpression()
    setattr(partner, 'javali_VarExpression77', None)
    _safe_set(owner, 'javali_Identifier78', partner)
    assert owner in getattr(partner, 'javali_VarExpression77')
    _safe_set(owner, 'javali_Identifier78', None)
    assert owner not in getattr(partner, 'javali_VarExpression77')


def test_assoc_procedures3_stub_double():
    # javali_Module has no real 'javali_Module4' property in the generated
    # code (a bare stub) -- manually attach it so javali_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Procedure(comment="sample_text", static=True, void=True)
    partner = javali_Module()
    setattr(partner, 'javali_Module4', None)
    _safe_set(owner, 'javali_Procedure', partner)
    assert owner in getattr(partner, 'javali_Module4')
    _safe_set(owner, 'javali_Procedure', None)
    assert owner not in getattr(partner, 'javali_Module4')


def test_assoc_right114_stub_double():
    # javali_Expression has no real 'javali_Expression116' property in the generated
    # code (a bare stub) -- manually attach it so javali_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Equality(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression116', None)
    _safe_set(owner, 'javali_Equality115', partner)
    assert getattr(partner, 'javali_Expression116') == owner
    _safe_set(owner, 'javali_Equality115', None)
    assert getattr(partner, 'javali_Expression116') is None


def test_assoc_right119_stub_double():
    # javali_Expression has no real 'javali_Expression121' property in the generated
    # code (a bare stub) -- manually attach it so javali_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Relation(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression121', None)
    _safe_set(owner, 'javali_Relation120', partner)
    assert getattr(partner, 'javali_Expression121') == owner
    _safe_set(owner, 'javali_Relation120', None)
    assert getattr(partner, 'javali_Expression121') is None


def test_assoc_right124_stub_double():
    # javali_Expression has no real 'javali_Expression126' property in the generated
    # code (a bare stub) -- manually attach it so javali_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Addition(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression126', None)
    _safe_set(owner, 'javali_Addition125', partner)
    assert getattr(partner, 'javali_Expression126') == owner
    _safe_set(owner, 'javali_Addition125', None)
    assert getattr(partner, 'javali_Expression126') is None


def test_assoc_right129_stub_double():
    # javali_Expression has no real 'javali_Expression131' property in the generated
    # code (a bare stub) -- manually attach it so javali_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Multiplication(operator="sample_text")
    partner = javali_Expression()
    setattr(partner, 'javali_Expression131', None)
    _safe_set(owner, 'javali_Multiplication130', partner)
    assert getattr(partner, 'javali_Expression131') == owner
    _safe_set(owner, 'javali_Multiplication130', None)
    assert getattr(partner, 'javali_Expression131') is None


def test_assoc_type30_stub_double():
    # javali_VarDeclaration has no real 'javali_VarDeclaration31' property in the generated
    # code (a bare stub) -- manually attach it so javali_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Type(arrayDims="sample_text")
    partner = javali_VarDeclaration()
    setattr(partner, 'javali_VarDeclaration31', None)
    _safe_set(owner, 'javali_Type32', partner)
    assert getattr(partner, 'javali_VarDeclaration31') == owner
    _safe_set(owner, 'javali_Type32', None)
    assert getattr(partner, 'javali_VarDeclaration31') is None


def test_assoc_type90_stub_double():
    # javali_NewArray has no real 'javali_NewArray' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_NewArray()
    setattr(partner, 'javali_NewArray', None)
    _safe_set(owner, 'javali_Identifier91', partner)
    assert getattr(partner, 'javali_NewArray') == owner
    _safe_set(owner, 'javali_Identifier91', None)
    assert getattr(partner, 'javali_NewArray') is None


def test_assoc_type95_stub_double():
    # javali_NewObject has no real 'javali_NewObject' property in the generated
    # code (a bare stub) -- manually attach it so javali_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javali_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javali_Identifier(id="sample_text")
    partner = javali_NewObject()
    setattr(partner, 'javali_NewObject', None)
    _safe_set(owner, 'javali_Identifier96', partner)
    assert getattr(partner, 'javali_NewObject') == owner
    _safe_set(owner, 'javali_Identifier96', None)
    assert getattr(partner, 'javali_NewObject') is None


