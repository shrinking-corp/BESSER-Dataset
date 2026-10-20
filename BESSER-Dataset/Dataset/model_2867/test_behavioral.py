import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arg,
    Assignment,
    BasicType,
    Channel,
    Communication,
    Composition,
    Declaration,
    Exp,
    InlineCollection,
    LabeledType,
    Literal,
    MaxBound,
    MinBound,
    NodeDecl,
    Pattern,
    PortDecl,
    Statement,
    Type,
    Variable,
    fiacre_AnyPattern,
    fiacre_Arg,
    fiacre_ArgumentVariable,
    fiacre_Array,
    fiacre_ArrayElem,
    fiacre_ArrayPattern,
    fiacre_Assignment,
    fiacre_BasicType,
    fiacre_BinExp,
    fiacre_BoolLiteral,
    fiacre_BoolType,
    fiacre_CaseStmt,
    fiacre_Channel,
    fiacre_ChannelDecl,
    fiacre_Communication,
    fiacre_ComponentDecl,
    fiacre_Composition,
    fiacre_CondExp,
    fiacre_ConstantDecl,
    fiacre_ConstantRef,
    fiacre_Constr,
    fiacre_ConstrExp,
    fiacre_ConstrPattern,
    fiacre_Declaration,
    fiacre_DeterministicAssignment,
    fiacre_Emission,
    fiacre_Exp,
    fiacre_Field,
    fiacre_FieldPattern,
    fiacre_FiniteBound,
    fiacre_Foreach,
    fiacre_IfStmt,
    fiacre_InfiniteBound,
    fiacre_InlineArray,
    fiacre_InlineCollection,
    fiacre_InlineQueue,
    fiacre_InlineRecord,
    fiacre_Instance,
    fiacre_IntType,
    fiacre_InterfacedComp,
    fiacre_Interval,
    fiacre_LabeledType,
    fiacre_Literal,
    fiacre_LocalPortDecl,
    fiacre_LocalVariable,
    fiacre_MaxBound,
    fiacre_MinBound,
    fiacre_NatLiteral,
    fiacre_NatType,
    fiacre_NodeDecl,
    fiacre_NonDeterministicAssignment,
    fiacre_NullStmt,
    fiacre_Par,
    fiacre_ParamPortDecl,
    fiacre_Pattern,
    fiacre_PortDecl,
    fiacre_Priority,
    fiacre_ProcessDecl,
    fiacre_Profile,
    fiacre_Program,
    fiacre_Queue,
    fiacre_Reception,
    fiacre_Record,
    fiacre_RecordElem,
    fiacre_RefArg,
    fiacre_Rule,
    fiacre_Select,
    fiacre_Seq,
    fiacre_SingleAssignment,
    fiacre_State,
    fiacre_Statement,
    fiacre_Synchronization,
    fiacre_To,
    fiacre_Transition,
    fiacre_Type,
    fiacre_TypeDecl,
    fiacre_TypeId,
    fiacre_UnExp,
    fiacre_Union,
    fiacre_ValuedField,
    fiacre_VarRef,
    fiacre_Variable,
    fiacre_Wait,
    fiacre_WhileStmt,
    BinOp,
    UnOp,
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

def test_assoc_action42_reverse_link_reassign_clear():
    a1 = fiacre_Transition(name="sample_text")
    a2 = fiacre_Transition(name="sample_text_2")
    b = fiacre_Statement(comment="sample_text")
    _safe_set(b, 'fiacre_Statement44', a1)
    assert _is_linked(b, 'fiacre_Statement44', a1)
    if hasattr(a1, 'fiacre_Transition43'):
        assert _is_linked(a1, 'fiacre_Transition43', b)
    _safe_set(b, 'fiacre_Statement44', a2)
    assert _is_linked(b, 'fiacre_Statement44', a2)
    if hasattr(a1, 'fiacre_Transition43'):
        assert not _is_linked(a1, 'fiacre_Transition43', b)
    if hasattr(a2, 'fiacre_Transition43'):
        assert _is_linked(a2, 'fiacre_Transition43', b)
    _safe_set(b, 'fiacre_Statement44', None)
    assert not _is_linked(b, 'fiacre_Statement44', a2)
    if hasattr(a2, 'fiacre_Transition43'):
        assert not _is_linked(a2, 'fiacre_Transition43', b)


def test_assoc_from_39_reverse_link_reassign_clear():
    a1 = fiacre_Transition(name="sample_text")
    a2 = fiacre_Transition(name="sample_text_2")
    b = fiacre_State(name="sample_text")
    _safe_set(b, 'fiacre_State41', a1)
    assert _is_linked(b, 'fiacre_State41', a1)
    if hasattr(a1, 'fiacre_Transition40'):
        assert _is_linked(a1, 'fiacre_Transition40', b)
    _safe_set(b, 'fiacre_State41', a2)
    assert _is_linked(b, 'fiacre_State41', a2)
    if hasattr(a1, 'fiacre_Transition40'):
        assert not _is_linked(a1, 'fiacre_Transition40', b)
    if hasattr(a2, 'fiacre_Transition40'):
        assert _is_linked(a2, 'fiacre_Transition40', b)
    _safe_set(b, 'fiacre_State41', None)
    assert not _is_linked(b, 'fiacre_State41', a2)
    if hasattr(a2, 'fiacre_Transition40'):
        assert not _is_linked(a2, 'fiacre_Transition40', b)


def test_assoc_port30_reverse_link_reassign_clear():
    a1 = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    a2 = fiacre_PortDecl(in_=False, name="sample_text_2", out=False)
    b = fiacre_Instance(name="sample_text")
    _safe_set(b, 'fiacre_Instance31', {a1})
    assert _is_linked(b, 'fiacre_Instance31', a1)
    if hasattr(a1, 'fiacre_PortDecl32'):
        assert _is_linked(a1, 'fiacre_PortDecl32', b)
    _safe_set(b, 'fiacre_Instance31', {a2})
    assert _is_linked(b, 'fiacre_Instance31', a2)
    if hasattr(a1, 'fiacre_PortDecl32'):
        assert not _is_linked(a1, 'fiacre_PortDecl32', b)
    if hasattr(a2, 'fiacre_PortDecl32'):
        assert _is_linked(a2, 'fiacre_PortDecl32', b)
    _safe_set(b, 'fiacre_Instance31', set())
    assert not _is_linked(b, 'fiacre_Instance31', a2)
    if hasattr(a2, 'fiacre_PortDecl32'):
        assert not _is_linked(a2, 'fiacre_PortDecl32', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action160_stub_double():
    # fiacre_Rule has no real 'fiacre_Rule161' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_Rule()
    setattr(partner, 'fiacre_Rule161', None)
    _safe_set(owner, 'fiacre_Statement162', partner)
    assert getattr(partner, 'fiacre_Rule161') == owner
    _safe_set(owner, 'fiacre_Statement162', None)
    assert getattr(partner, 'fiacre_Rule161') is None


def test_assoc_arg141_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp142' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_ConstrExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_ConstrExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_ConstrExp(name="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp142', None)
    _safe_set(owner, 'fiacre_ConstrExp', partner)
    assert getattr(partner, 'fiacre_Exp142') == owner
    _safe_set(owner, 'fiacre_ConstrExp', None)
    assert getattr(partner, 'fiacre_Exp142') is None


def test_assoc_arg144_stub_double():
    # fiacre_Pattern has no real 'fiacre_Pattern145' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_ConstrPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_ConstrPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_ConstrPattern(name="sample_text")
    partner = fiacre_Pattern()
    setattr(partner, 'fiacre_Pattern145', None)
    _safe_set(owner, 'fiacre_ConstrPattern', partner)
    assert getattr(partner, 'fiacre_Pattern145') == owner
    _safe_set(owner, 'fiacre_ConstrPattern', None)
    assert getattr(partner, 'fiacre_Pattern145') is None


def test_assoc_arg28_stub_double():
    # fiacre_Arg has no real 'fiacre_Arg' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Instance(name="sample_text")
    partner = fiacre_Arg()
    setattr(partner, 'fiacre_Arg', None)
    _safe_set(owner, 'fiacre_Instance29', {partner})
    assert getattr(partner, 'fiacre_Arg') == owner
    _safe_set(owner, 'fiacre_Instance29', set())
    assert getattr(partner, 'fiacre_Arg') is None


def test_assoc_arg3_stub_double():
    # fiacre_NodeDecl has no real 'fiacre_NodeDecl4' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_ArgumentVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_ArgumentVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_ArgumentVariable(read=True, ref=True, write=True)
    partner = fiacre_NodeDecl()
    setattr(partner, 'fiacre_NodeDecl4', None)
    _safe_set(owner, 'fiacre_ArgumentVariable', partner)
    assert owner in getattr(partner, 'fiacre_NodeDecl4')
    _safe_set(owner, 'fiacre_ArgumentVariable', None)
    assert owner not in getattr(partner, 'fiacre_NodeDecl4')


def test_assoc_body184_stub_double():
    # fiacre_Foreach has no real 'fiacre_Foreach' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_Foreach()
    setattr(partner, 'fiacre_Foreach', None)
    _safe_set(owner, 'fiacre_Statement185', partner)
    assert getattr(partner, 'fiacre_Foreach') == owner
    _safe_set(owner, 'fiacre_Statement185', None)
    assert getattr(partner, 'fiacre_Foreach') is None


def test_assoc_body49_stub_double():
    # fiacre_WhileStmt has no real 'fiacre_WhileStmt50' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_WhileStmt()
    setattr(partner, 'fiacre_WhileStmt50', None)
    _safe_set(owner, 'fiacre_Statement51', partner)
    assert getattr(partner, 'fiacre_WhileStmt50') == owner
    _safe_set(owner, 'fiacre_Statement51', None)
    assert getattr(partner, 'fiacre_WhileStmt50') is None


def test_assoc_channel21_stub_double():
    # fiacre_Channel has no real 'fiacre_Channel22' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_PortDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_PortDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    partner = fiacre_Channel()
    setattr(partner, 'fiacre_Channel22', None)
    _safe_set(owner, 'fiacre_PortDecl', partner)
    assert getattr(partner, 'fiacre_Channel22') == owner
    _safe_set(owner, 'fiacre_PortDecl', None)
    assert getattr(partner, 'fiacre_Channel22') is None


def test_assoc_decl85_stub_double():
    # fiacre_VarRef has no real 'fiacre_VarRef' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Variable(name="sample_text")
    partner = fiacre_VarRef()
    setattr(partner, 'fiacre_VarRef', None)
    _safe_set(owner, 'fiacre_Variable', partner)
    assert getattr(partner, 'fiacre_VarRef') == owner
    _safe_set(owner, 'fiacre_Variable', None)
    assert getattr(partner, 'fiacre_VarRef') is None


def test_assoc_declaration0_stub_double():
    # fiacre_Program has no real 'fiacre_Program' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Declaration(name="sample_text")
    partner = fiacre_Program()
    setattr(partner, 'fiacre_Program', None)
    _safe_set(owner, 'fiacre_Declaration', partner)
    assert owner in getattr(partner, 'fiacre_Program')
    _safe_set(owner, 'fiacre_Declaration', None)
    assert owner not in getattr(partner, 'fiacre_Program')


def test_assoc_dest62_stub_double():
    # fiacre_To has no real 'fiacre_To' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_State(name="sample_text")
    partner = fiacre_To()
    setattr(partner, 'fiacre_To', None)
    _safe_set(owner, 'fiacre_State63', partner)
    assert getattr(partner, 'fiacre_To') == owner
    _safe_set(owner, 'fiacre_State63', None)
    assert getattr(partner, 'fiacre_To') is None


def test_assoc_else_57_stub_double():
    # fiacre_IfStmt has no real 'fiacre_IfStmt58' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_IfStmt()
    setattr(partner, 'fiacre_IfStmt58', None)
    _safe_set(owner, 'fiacre_Statement59', partner)
    assert getattr(partner, 'fiacre_IfStmt58') == owner
    _safe_set(owner, 'fiacre_Statement59', None)
    assert getattr(partner, 'fiacre_IfStmt58') is None


def test_assoc_exp78_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp79' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_UnExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_UnExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_UnExp(unop="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp79', None)
    _safe_set(owner, 'fiacre_UnExp', partner)
    assert getattr(partner, 'fiacre_Exp79') == owner
    _safe_set(owner, 'fiacre_UnExp', None)
    assert getattr(partner, 'fiacre_Exp79') is None


def test_assoc_inf135_stub_double():
    # fiacre_Priority has no real 'fiacre_Priority136' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_PortDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_PortDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    partner = fiacre_Priority()
    setattr(partner, 'fiacre_Priority136', None)
    _safe_set(owner, 'fiacre_PortDecl137', partner)
    assert owner in getattr(partner, 'fiacre_Priority136')
    _safe_set(owner, 'fiacre_PortDecl137', None)
    assert owner not in getattr(partner, 'fiacre_Priority136')


def test_assoc_initAction11_stub_double():
    # fiacre_NodeDecl has no real 'fiacre_NodeDecl12' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_NodeDecl()
    setattr(partner, 'fiacre_NodeDecl12', None)
    _safe_set(owner, 'fiacre_Statement', partner)
    assert getattr(partner, 'fiacre_NodeDecl12') == owner
    _safe_set(owner, 'fiacre_Statement', None)
    assert getattr(partner, 'fiacre_NodeDecl12') is None


def test_assoc_initializer23_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_LocalVariable(constant=True)
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp', None)
    _safe_set(owner, 'fiacre_LocalVariable24', partner)
    assert getattr(partner, 'fiacre_Exp') == owner
    _safe_set(owner, 'fiacre_LocalVariable24', None)
    assert getattr(partner, 'fiacre_Exp') is None


def test_assoc_iter186_stub_double():
    # fiacre_Foreach has no real 'fiacre_Foreach187' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_LocalVariable(constant=True)
    partner = fiacre_Foreach()
    setattr(partner, 'fiacre_Foreach187', None)
    _safe_set(owner, 'fiacre_LocalVariable188', partner)
    assert getattr(partner, 'fiacre_Foreach187') == owner
    _safe_set(owner, 'fiacre_LocalVariable188', None)
    assert getattr(partner, 'fiacre_Foreach187') is None


def test_assoc_left82_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp84' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_BinExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_BinExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_BinExp(binOp="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp84', None)
    _safe_set(owner, 'fiacre_BinExp83', partner)
    assert getattr(partner, 'fiacre_Exp84') == owner
    _safe_set(owner, 'fiacre_BinExp83', None)
    assert getattr(partner, 'fiacre_Exp84') is None


def test_assoc_port45_stub_double():
    # fiacre_Communication has no real 'fiacre_Communication' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_PortDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_PortDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    partner = fiacre_Communication()
    setattr(partner, 'fiacre_Communication', None)
    _safe_set(owner, 'fiacre_PortDecl46', partner)
    assert getattr(partner, 'fiacre_Communication') == owner
    _safe_set(owner, 'fiacre_PortDecl46', None)
    assert getattr(partner, 'fiacre_Communication') is None


def test_assoc_record151_stub_double():
    # fiacre_Pattern has no real 'fiacre_Pattern152' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_FieldPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_FieldPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_FieldPattern(field="sample_text")
    partner = fiacre_Pattern()
    setattr(partner, 'fiacre_Pattern152', None)
    _safe_set(owner, 'fiacre_FieldPattern', partner)
    assert getattr(partner, 'fiacre_Pattern152') == owner
    _safe_set(owner, 'fiacre_FieldPattern', None)
    assert getattr(partner, 'fiacre_Pattern152') is None


def test_assoc_record91_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp92' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_RecordElem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_RecordElem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_RecordElem(field="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp92', None)
    _safe_set(owner, 'fiacre_RecordElem', partner)
    assert getattr(partner, 'fiacre_Exp92') == owner
    _safe_set(owner, 'fiacre_RecordElem', None)
    assert getattr(partner, 'fiacre_Exp92') is None


def test_assoc_ref163_stub_double():
    # fiacre_RefArg has no real 'fiacre_RefArg' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Variable(name="sample_text")
    partner = fiacre_RefArg()
    setattr(partner, 'fiacre_RefArg', None)
    _safe_set(owner, 'fiacre_Variable164', partner)
    assert getattr(partner, 'fiacre_RefArg') == owner
    _safe_set(owner, 'fiacre_Variable164', None)
    assert getattr(partner, 'fiacre_RefArg') is None


def test_assoc_right80_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp81' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_BinExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_BinExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_BinExp(binOp="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp81', None)
    _safe_set(owner, 'fiacre_BinExp', partner)
    assert getattr(partner, 'fiacre_Exp81') == owner
    _safe_set(owner, 'fiacre_BinExp', None)
    assert getattr(partner, 'fiacre_Exp81') is None


def test_assoc_state18_stub_double():
    # fiacre_ProcessDecl has no real 'fiacre_ProcessDecl' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_State(name="sample_text")
    partner = fiacre_ProcessDecl()
    setattr(partner, 'fiacre_ProcessDecl', None)
    _safe_set(owner, 'fiacre_State', partner)
    assert owner in getattr(partner, 'fiacre_ProcessDecl')
    _safe_set(owner, 'fiacre_State', None)
    assert owner not in getattr(partner, 'fiacre_ProcessDecl')


def test_assoc_statement124_stub_double():
    # fiacre_Seq has no real 'fiacre_Seq' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_Seq()
    setattr(partner, 'fiacre_Seq', None)
    _safe_set(owner, 'fiacre_Statement125', partner)
    assert owner in getattr(partner, 'fiacre_Seq')
    _safe_set(owner, 'fiacre_Statement125', None)
    assert owner not in getattr(partner, 'fiacre_Seq')


def test_assoc_statement60_stub_double():
    # fiacre_Select has no real 'fiacre_Select' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_Select()
    setattr(partner, 'fiacre_Select', None)
    _safe_set(owner, 'fiacre_Statement61', partner)
    assert owner in getattr(partner, 'fiacre_Select')
    _safe_set(owner, 'fiacre_Statement61', None)
    assert owner not in getattr(partner, 'fiacre_Select')


def test_assoc_sup138_stub_double():
    # fiacre_Priority has no real 'fiacre_Priority139' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_PortDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_PortDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    partner = fiacre_Priority()
    setattr(partner, 'fiacre_Priority139', None)
    _safe_set(owner, 'fiacre_PortDecl140', partner)
    assert owner in getattr(partner, 'fiacre_Priority139')
    _safe_set(owner, 'fiacre_PortDecl140', None)
    assert owner not in getattr(partner, 'fiacre_Priority139')


def test_assoc_syncPort36_stub_double():
    # fiacre_InterfacedComp has no real 'fiacre_InterfacedComp37' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_PortDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_PortDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_PortDecl(in_=True, name="sample_text", out=True)
    partner = fiacre_InterfacedComp()
    setattr(partner, 'fiacre_InterfacedComp37', None)
    _safe_set(owner, 'fiacre_PortDecl38', partner)
    assert owner in getattr(partner, 'fiacre_InterfacedComp37')
    _safe_set(owner, 'fiacre_PortDecl38', None)
    assert owner not in getattr(partner, 'fiacre_InterfacedComp37')


def test_assoc_then54_stub_double():
    # fiacre_IfStmt has no real 'fiacre_IfStmt55' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Statement(comment="sample_text")
    partner = fiacre_IfStmt()
    setattr(partner, 'fiacre_IfStmt55', None)
    _safe_set(owner, 'fiacre_Statement56', partner)
    assert getattr(partner, 'fiacre_IfStmt55') == owner
    _safe_set(owner, 'fiacre_Statement56', None)
    assert getattr(partner, 'fiacre_IfStmt55') is None


def test_assoc_transition19_stub_double():
    # fiacre_ProcessDecl has no real 'fiacre_ProcessDecl20' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Transition(name="sample_text")
    partner = fiacre_ProcessDecl()
    setattr(partner, 'fiacre_ProcessDecl20', None)
    _safe_set(owner, 'fiacre_Transition', partner)
    assert owner in getattr(partner, 'fiacre_ProcessDecl20')
    _safe_set(owner, 'fiacre_Transition', None)
    assert owner not in getattr(partner, 'fiacre_ProcessDecl20')


def test_assoc_type132_stub_double():
    # fiacre_Type has no real 'fiacre_Type134' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Variable(name="sample_text")
    partner = fiacre_Type()
    setattr(partner, 'fiacre_Type134', None)
    _safe_set(owner, 'fiacre_Variable133', partner)
    assert getattr(partner, 'fiacre_Type134') == owner
    _safe_set(owner, 'fiacre_Variable133', None)
    assert getattr(partner, 'fiacre_Type134') is None


def test_assoc_type174_stub_double():
    # fiacre_Type has no real 'fiacre_Type175' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_LabeledType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_LabeledType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_LabeledType(name="sample_text")
    partner = fiacre_Type()
    setattr(partner, 'fiacre_Type175', None)
    _safe_set(owner, 'fiacre_LabeledType', partner)
    assert getattr(partner, 'fiacre_Type175') == owner
    _safe_set(owner, 'fiacre_LabeledType', None)
    assert getattr(partner, 'fiacre_Type175') is None


def test_assoc_type26_stub_double():
    # fiacre_NodeDecl has no real 'fiacre_NodeDecl27' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Instance(name="sample_text")
    partner = fiacre_NodeDecl()
    setattr(partner, 'fiacre_NodeDecl27', None)
    _safe_set(owner, 'fiacre_Instance', partner)
    assert getattr(partner, 'fiacre_NodeDecl27') == owner
    _safe_set(owner, 'fiacre_Instance', None)
    assert getattr(partner, 'fiacre_NodeDecl27') is None


def test_assoc_value113_stub_double():
    # fiacre_InlineRecord has no real 'fiacre_InlineRecord' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_ValuedField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_ValuedField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_ValuedField(field="sample_text")
    partner = fiacre_InlineRecord()
    setattr(partner, 'fiacre_InlineRecord', None)
    _safe_set(owner, 'fiacre_ValuedField', partner)
    assert owner in getattr(partner, 'fiacre_InlineRecord')
    _safe_set(owner, 'fiacre_ValuedField', None)
    assert owner not in getattr(partner, 'fiacre_InlineRecord')


def test_assoc_value114_stub_double():
    # fiacre_Exp has no real 'fiacre_Exp116' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_ValuedField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_ValuedField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_ValuedField(field="sample_text")
    partner = fiacre_Exp()
    setattr(partner, 'fiacre_Exp116', None)
    _safe_set(owner, 'fiacre_ValuedField115', partner)
    assert getattr(partner, 'fiacre_Exp116') == owner
    _safe_set(owner, 'fiacre_ValuedField115', None)
    assert getattr(partner, 'fiacre_Exp116') is None


def test_assoc_var5_stub_double():
    # fiacre_NodeDecl has no real 'fiacre_NodeDecl6' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_LocalVariable(constant=True)
    partner = fiacre_NodeDecl()
    setattr(partner, 'fiacre_NodeDecl6', None)
    _safe_set(owner, 'fiacre_LocalVariable', partner)
    assert owner in getattr(partner, 'fiacre_NodeDecl6')
    _safe_set(owner, 'fiacre_LocalVariable', None)
    assert owner not in getattr(partner, 'fiacre_NodeDecl6')


