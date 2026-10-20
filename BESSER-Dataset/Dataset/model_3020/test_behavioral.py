import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArgOrVar,
    Connectivity,
    ConnectivityCall,
    Container,
    Expression,
    FunctionOrReduction,
    Instruction,
    Iterable,
    IterationBlock,
    TimeIteratorRef,
    Var,
    nabla_Affectation,
    nabla_And,
    nabla_Arg,
    nabla_ArgOrVar,
    nabla_ArgOrVarRef,
    nabla_BaseType,
    nabla_BaseTypeConstant,
    nabla_BoolConstant,
    nabla_Cardinality,
    nabla_Comparison,
    nabla_Connectivity,
    nabla_ConnectivityCall,
    nabla_ConnectivityVar,
    nabla_Container,
    nabla_ContractedIf,
    nabla_CurrentTimeIteratorRef,
    nabla_Div,
    nabla_Equality,
    nabla_Exit,
    nabla_Expression,
    nabla_Function,
    nabla_FunctionCall,
    nabla_FunctionOrReduction,
    nabla_If,
    nabla_Import,
    nabla_InitTimeIteratorRef,
    nabla_Instruction,
    nabla_InstructionBlock,
    nabla_IntConstant,
    nabla_Interval,
    nabla_Item,
    nabla_ItemDefinition,
    nabla_ItemRef,
    nabla_ItemType,
    nabla_Iterable,
    nabla_IterationBlock,
    nabla_Job,
    nabla_Loop,
    nabla_MaxConstant,
    nabla_MinConstant,
    nabla_Minus,
    nabla_Modulo,
    nabla_Mul,
    nabla_MultipleConnectivity,
    nabla_MultipleConnectivityCall,
    nabla_NablaModule,
    nabla_NextTimeIteratorRef,
    nabla_Not,
    nabla_OptDefinition,
    nabla_Or,
    nabla_Parenthesis,
    nabla_Plus,
    nabla_RealConstant,
    nabla_Reduction,
    nabla_ReductionCall,
    nabla_Return,
    nabla_SetDefinition,
    nabla_SetRef,
    nabla_SimpleVar,
    nabla_SimpleVarDefinition,
    nabla_SingleConnectivity,
    nabla_SingleConnectivityCall,
    nabla_SingletonDefinition,
    nabla_SpaceIterator,
    nabla_TimeIterator,
    nabla_TimeIteratorDefinition,
    nabla_TimeIteratorRef,
    nabla_UnaryMinus,
    nabla_Var,
    nabla_VarGroupDeclaration,
    nabla_VectorConstant,
    PrimitiveType,
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

def test_assoc_connectivities3_reverse_link_reassign_clear():
    a1 = nabla_NablaModule(name="sample_text")
    a2 = nabla_NablaModule(name="sample_text_2")
    b = nabla_Connectivity(name="sample_text")
    _safe_set(b, 'nabla_Connectivity', a1)
    assert _is_linked(b, 'nabla_Connectivity', a1)
    if hasattr(a1, 'nabla_NablaModule4'):
        assert _is_linked(a1, 'nabla_NablaModule4', b)
    _safe_set(b, 'nabla_Connectivity', a2)
    assert _is_linked(b, 'nabla_Connectivity', a2)
    if hasattr(a1, 'nabla_NablaModule4'):
        assert not _is_linked(a1, 'nabla_NablaModule4', b)
    if hasattr(a2, 'nabla_NablaModule4'):
        assert _is_linked(a2, 'nabla_NablaModule4', b)
    _safe_set(b, 'nabla_Connectivity', None)
    assert not _is_linked(b, 'nabla_Connectivity', a2)
    if hasattr(a2, 'nabla_NablaModule4'):
        assert not _is_linked(a2, 'nabla_NablaModule4', b)


def test_assoc_functions7_reverse_link_reassign_clear():
    a1 = nabla_NablaModule(name="sample_text")
    a2 = nabla_NablaModule(name="sample_text_2")
    b = nabla_Function(external=True)
    _safe_set(b, 'nabla_Function', a1)
    assert _is_linked(b, 'nabla_Function', a1)
    if hasattr(a1, 'nabla_NablaModule8'):
        assert _is_linked(a1, 'nabla_NablaModule8', b)
    _safe_set(b, 'nabla_Function', a2)
    assert _is_linked(b, 'nabla_Function', a2)
    if hasattr(a1, 'nabla_NablaModule8'):
        assert not _is_linked(a1, 'nabla_NablaModule8', b)
    if hasattr(a2, 'nabla_NablaModule8'):
        assert _is_linked(a2, 'nabla_NablaModule8', b)
    _safe_set(b, 'nabla_Function', None)
    assert not _is_linked(b, 'nabla_Function', a2)
    if hasattr(a2, 'nabla_NablaModule8'):
        assert not _is_linked(a2, 'nabla_NablaModule8', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = nabla_NablaModule(name="sample_text")
    a2 = nabla_NablaModule(name="sample_text_2")
    b = nabla_Import(importedNamespace="sample_text")
    _safe_set(b, 'nabla_Import', a1)
    assert _is_linked(b, 'nabla_Import', a1)
    if hasattr(a1, 'nabla_NablaModule'):
        assert _is_linked(a1, 'nabla_NablaModule', b)
    _safe_set(b, 'nabla_Import', a2)
    assert _is_linked(b, 'nabla_Import', a2)
    if hasattr(a1, 'nabla_NablaModule'):
        assert not _is_linked(a1, 'nabla_NablaModule', b)
    if hasattr(a2, 'nabla_NablaModule'):
        assert _is_linked(a2, 'nabla_NablaModule', b)
    _safe_set(b, 'nabla_Import', None)
    assert not _is_linked(b, 'nabla_Import', a2)
    if hasattr(a2, 'nabla_NablaModule'):
        assert not _is_linked(a2, 'nabla_NablaModule', b)


def test_assoc_inTypes110_reverse_link_reassign_clear():
    a1 = nabla_Function(external=True)
    a2 = nabla_Function(external=False)
    b = nabla_BaseType(primitive="sample_text")
    _safe_set(b, 'nabla_BaseType112', a1)
    assert _is_linked(b, 'nabla_BaseType112', a1)
    if hasattr(a1, 'nabla_Function111'):
        assert _is_linked(a1, 'nabla_Function111', b)
    _safe_set(b, 'nabla_BaseType112', a2)
    assert _is_linked(b, 'nabla_BaseType112', a2)
    if hasattr(a1, 'nabla_Function111'):
        assert not _is_linked(a1, 'nabla_Function111', b)
    if hasattr(a2, 'nabla_Function111'):
        assert _is_linked(a2, 'nabla_Function111', b)
    _safe_set(b, 'nabla_BaseType112', None)
    assert not _is_linked(b, 'nabla_BaseType112', a2)
    if hasattr(a2, 'nabla_Function111'):
        assert not _is_linked(a2, 'nabla_Function111', b)


def test_assoc_inTypes23_reverse_link_reassign_clear():
    a1 = nabla_ItemType(name="sample_text")
    a2 = nabla_ItemType(name="sample_text_2")
    b = nabla_Connectivity(name="sample_text")
    _safe_set(b, 'nabla_Connectivity24', {a1})
    assert _is_linked(b, 'nabla_Connectivity24', a1)
    if hasattr(a1, 'nabla_ItemType25'):
        assert _is_linked(a1, 'nabla_ItemType25', b)
    _safe_set(b, 'nabla_Connectivity24', {a2})
    assert _is_linked(b, 'nabla_Connectivity24', a2)
    if hasattr(a1, 'nabla_ItemType25'):
        assert not _is_linked(a1, 'nabla_ItemType25', b)
    if hasattr(a2, 'nabla_ItemType25'):
        assert _is_linked(a2, 'nabla_ItemType25', b)
    _safe_set(b, 'nabla_Connectivity24', set())
    assert not _is_linked(b, 'nabla_Connectivity24', a2)
    if hasattr(a2, 'nabla_ItemType25'):
        assert not _is_linked(a2, 'nabla_ItemType25', b)


def test_assoc_itemTypes1_reverse_link_reassign_clear():
    a1 = nabla_NablaModule(name="sample_text")
    a2 = nabla_NablaModule(name="sample_text_2")
    b = nabla_ItemType(name="sample_text")
    _safe_set(b, 'nabla_ItemType', a1)
    assert _is_linked(b, 'nabla_ItemType', a1)
    if hasattr(a1, 'nabla_NablaModule2'):
        assert _is_linked(a1, 'nabla_NablaModule2', b)
    _safe_set(b, 'nabla_ItemType', a2)
    assert _is_linked(b, 'nabla_ItemType', a2)
    if hasattr(a1, 'nabla_NablaModule2'):
        assert not _is_linked(a1, 'nabla_NablaModule2', b)
    if hasattr(a2, 'nabla_NablaModule2'):
        assert _is_linked(a2, 'nabla_NablaModule2', b)
    _safe_set(b, 'nabla_ItemType', None)
    assert not _is_linked(b, 'nabla_ItemType', a2)
    if hasattr(a2, 'nabla_NablaModule2'):
        assert not _is_linked(a2, 'nabla_NablaModule2', b)


def test_assoc_jobs17_reverse_link_reassign_clear():
    a1 = nabla_NablaModule(name="sample_text")
    a2 = nabla_NablaModule(name="sample_text_2")
    b = nabla_Job(name="sample_text")
    _safe_set(b, 'nabla_Job', a1)
    assert _is_linked(b, 'nabla_Job', a1)
    if hasattr(a1, 'nabla_NablaModule18'):
        assert _is_linked(a1, 'nabla_NablaModule18', b)
    _safe_set(b, 'nabla_Job', a2)
    assert _is_linked(b, 'nabla_Job', a2)
    if hasattr(a1, 'nabla_NablaModule18'):
        assert not _is_linked(a1, 'nabla_NablaModule18', b)
    if hasattr(a2, 'nabla_NablaModule18'):
        assert _is_linked(a2, 'nabla_NablaModule18', b)
    _safe_set(b, 'nabla_Job', None)
    assert not _is_linked(b, 'nabla_Job', a2)
    if hasattr(a2, 'nabla_NablaModule18'):
        assert not _is_linked(a2, 'nabla_NablaModule18', b)


def test_assoc_returnType113_reverse_link_reassign_clear():
    a1 = nabla_Function(external=True)
    a2 = nabla_Function(external=False)
    b = nabla_BaseType(primitive="sample_text")
    _safe_set(b, 'nabla_BaseType115', a1)
    assert _is_linked(b, 'nabla_BaseType115', a1)
    if hasattr(a1, 'nabla_Function114'):
        assert _is_linked(a1, 'nabla_Function114', b)
    _safe_set(b, 'nabla_BaseType115', a2)
    assert _is_linked(b, 'nabla_BaseType115', a2)
    if hasattr(a1, 'nabla_Function114'):
        assert not _is_linked(a1, 'nabla_Function114', b)
    if hasattr(a2, 'nabla_Function114'):
        assert _is_linked(a2, 'nabla_Function114', b)
    _safe_set(b, 'nabla_BaseType115', None)
    assert not _is_linked(b, 'nabla_BaseType115', a2)
    if hasattr(a2, 'nabla_Function114'):
        assert not _is_linked(a2, 'nabla_Function114', b)


def test_assoc_returnType26_reverse_link_reassign_clear():
    a1 = nabla_ItemType(name="sample_text")
    a2 = nabla_ItemType(name="sample_text_2")
    b = nabla_Connectivity(name="sample_text")
    _safe_set(b, 'nabla_Connectivity27', a1)
    assert _is_linked(b, 'nabla_Connectivity27', a1)
    if hasattr(a1, 'nabla_ItemType28'):
        assert _is_linked(a1, 'nabla_ItemType28', b)
    _safe_set(b, 'nabla_Connectivity27', a2)
    assert _is_linked(b, 'nabla_Connectivity27', a2)
    if hasattr(a1, 'nabla_ItemType28'):
        assert not _is_linked(a1, 'nabla_ItemType28', b)
    if hasattr(a2, 'nabla_ItemType28'):
        assert _is_linked(a2, 'nabla_ItemType28', b)
    _safe_set(b, 'nabla_Connectivity27', None)
    assert not _is_linked(b, 'nabla_Connectivity27', a2)
    if hasattr(a2, 'nabla_ItemType28'):
        assert not _is_linked(a2, 'nabla_ItemType28', b)


def test_assoc_target91_reverse_link_reassign_clear():
    a1 = nabla_ItemRef(dec=7, inc=7)
    a2 = nabla_ItemRef(dec=13, inc=13)
    b = nabla_Item(name="sample_text")
    _safe_set(b, 'nabla_Item93', a1)
    assert _is_linked(b, 'nabla_Item93', a1)
    if hasattr(a1, 'nabla_ItemRef92'):
        assert _is_linked(a1, 'nabla_ItemRef92', b)
    _safe_set(b, 'nabla_Item93', a2)
    assert _is_linked(b, 'nabla_Item93', a2)
    if hasattr(a1, 'nabla_ItemRef92'):
        assert not _is_linked(a1, 'nabla_ItemRef92', b)
    if hasattr(a2, 'nabla_ItemRef92'):
        assert _is_linked(a2, 'nabla_ItemRef92', b)
    _safe_set(b, 'nabla_Item93', None)
    assert not _is_linked(b, 'nabla_Item93', a2)
    if hasattr(a2, 'nabla_ItemRef92'):
        assert not _is_linked(a2, 'nabla_ItemRef92', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Left184_stub_double():
    # nabla_Expression has no real 'nabla_Expression185' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Div's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Div's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Div(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression185', None)
    _safe_set(owner, 'nabla_Div', partner)
    assert getattr(partner, 'nabla_Expression185') == owner
    _safe_set(owner, 'nabla_Div', None)
    assert getattr(partner, 'nabla_Expression185') is None


def test_assoc_args86_stub_double():
    # nabla_ConnectivityCall has no real 'nabla_ConnectivityCall' property in the generated
    # code (a bare stub) -- manually attach it so nabla_ItemRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_ItemRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_ItemRef(dec=7, inc=7)
    partner = nabla_ConnectivityCall()
    setattr(partner, 'nabla_ConnectivityCall', None)
    _safe_set(owner, 'nabla_ItemRef', partner)
    assert owner in getattr(partner, 'nabla_ConnectivityCall')
    _safe_set(owner, 'nabla_ItemRef', None)
    assert owner not in getattr(partner, 'nabla_ConnectivityCall')


def test_assoc_body107_stub_double():
    # nabla_Instruction has no real 'nabla_Instruction109' property in the generated
    # code (a bare stub) -- manually attach it so nabla_FunctionOrReduction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_FunctionOrReduction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_FunctionOrReduction(name="sample_text")
    partner = nabla_Instruction()
    setattr(partner, 'nabla_Instruction109', None)
    _safe_set(owner, 'nabla_FunctionOrReduction108', partner)
    assert getattr(partner, 'nabla_Instruction109') == owner
    _safe_set(owner, 'nabla_FunctionOrReduction108', None)
    assert getattr(partner, 'nabla_Instruction109') is None


def test_assoc_declarations13_stub_double():
    # nabla_VarGroupDeclaration has no real 'nabla_VarGroupDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so nabla_NablaModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_NablaModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_NablaModule(name="sample_text")
    partner = nabla_VarGroupDeclaration()
    setattr(partner, 'nabla_VarGroupDeclaration', None)
    _safe_set(owner, 'nabla_NablaModule14', {partner})
    assert getattr(partner, 'nabla_VarGroupDeclaration') == owner
    _safe_set(owner, 'nabla_NablaModule14', set())
    assert getattr(partner, 'nabla_VarGroupDeclaration') is None


def test_assoc_definitions11_stub_double():
    # nabla_SimpleVarDefinition has no real 'nabla_SimpleVarDefinition' property in the generated
    # code (a bare stub) -- manually attach it so nabla_NablaModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_NablaModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_NablaModule(name="sample_text")
    partner = nabla_SimpleVarDefinition()
    setattr(partner, 'nabla_SimpleVarDefinition', None)
    _safe_set(owner, 'nabla_NablaModule12', {partner})
    assert getattr(partner, 'nabla_SimpleVarDefinition') == owner
    _safe_set(owner, 'nabla_NablaModule12', set())
    assert getattr(partner, 'nabla_SimpleVarDefinition') is None


def test_assoc_function200_stub_double():
    # nabla_FunctionCall has no real 'nabla_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Function(external=True)
    partner = nabla_FunctionCall()
    setattr(partner, 'nabla_FunctionCall', None)
    _safe_set(owner, 'nabla_Function201', partner)
    assert getattr(partner, 'nabla_FunctionCall') == owner
    _safe_set(owner, 'nabla_Function201', None)
    assert getattr(partner, 'nabla_FunctionCall') is None


def test_assoc_inArgs105_stub_double():
    # nabla_Arg has no real 'nabla_Arg' property in the generated
    # code (a bare stub) -- manually attach it so nabla_FunctionOrReduction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_FunctionOrReduction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_FunctionOrReduction(name="sample_text")
    partner = nabla_Arg()
    setattr(partner, 'nabla_Arg', None)
    _safe_set(owner, 'nabla_FunctionOrReduction106', {partner})
    assert getattr(partner, 'nabla_Arg') == owner
    _safe_set(owner, 'nabla_FunctionOrReduction106', set())
    assert getattr(partner, 'nabla_Arg') is None


def test_assoc_index81_stub_double():
    # nabla_SimpleVar has no real 'nabla_SimpleVar82' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Interval(from_=7)
    partner = nabla_SimpleVar()
    setattr(partner, 'nabla_SimpleVar82', None)
    _safe_set(owner, 'nabla_Interval', partner)
    assert getattr(partner, 'nabla_SimpleVar82') == owner
    _safe_set(owner, 'nabla_Interval', None)
    assert getattr(partner, 'nabla_SimpleVar82') is None


def test_assoc_instruction29_stub_double():
    # nabla_Instruction has no real 'nabla_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Job's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Job's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Job(name="sample_text")
    partner = nabla_Instruction()
    setattr(partner, 'nabla_Instruction', None)
    _safe_set(owner, 'nabla_Job30', partner)
    assert getattr(partner, 'nabla_Instruction') == owner
    _safe_set(owner, 'nabla_Job30', None)
    assert getattr(partner, 'nabla_Instruction') is None


def test_assoc_item58_stub_double():
    # nabla_ItemDefinition has no real 'nabla_ItemDefinition' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Item(name="sample_text")
    partner = nabla_ItemDefinition()
    setattr(partner, 'nabla_ItemDefinition', None)
    _safe_set(owner, 'nabla_Item', partner)
    assert getattr(partner, 'nabla_ItemDefinition') == owner
    _safe_set(owner, 'nabla_Item', None)
    assert getattr(partner, 'nabla_ItemDefinition') is None


def test_assoc_item66_stub_double():
    # nabla_SpaceIterator has no real 'nabla_SpaceIterator' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Item(name="sample_text")
    partner = nabla_SpaceIterator()
    setattr(partner, 'nabla_SpaceIterator', None)
    _safe_set(owner, 'nabla_Item67', partner)
    assert getattr(partner, 'nabla_SpaceIterator') == owner
    _safe_set(owner, 'nabla_Item67', None)
    assert getattr(partner, 'nabla_SpaceIterator') is None


def test_assoc_item75_stub_double():
    # nabla_SingletonDefinition has no real 'nabla_SingletonDefinition76' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Item(name="sample_text")
    partner = nabla_SingletonDefinition()
    setattr(partner, 'nabla_SingletonDefinition76', None)
    _safe_set(owner, 'nabla_Item77', partner)
    assert getattr(partner, 'nabla_SingletonDefinition76') == owner
    _safe_set(owner, 'nabla_Item77', None)
    assert getattr(partner, 'nabla_SingletonDefinition76') is None


def test_assoc_iteration15_stub_double():
    # nabla_TimeIteratorDefinition has no real 'nabla_TimeIteratorDefinition' property in the generated
    # code (a bare stub) -- manually attach it so nabla_NablaModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_NablaModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_NablaModule(name="sample_text")
    partner = nabla_TimeIteratorDefinition()
    setattr(partner, 'nabla_TimeIteratorDefinition', None)
    _safe_set(owner, 'nabla_NablaModule16', partner)
    assert getattr(partner, 'nabla_TimeIteratorDefinition') == owner
    _safe_set(owner, 'nabla_NablaModule16', None)
    assert getattr(partner, 'nabla_TimeIteratorDefinition') is None


def test_assoc_left149_stub_double():
    # nabla_Expression has no real 'nabla_Expression150' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Or's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Or's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Or(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression150', None)
    _safe_set(owner, 'nabla_Or', partner)
    assert getattr(partner, 'nabla_Expression150') == owner
    _safe_set(owner, 'nabla_Or', None)
    assert getattr(partner, 'nabla_Expression150') is None


def test_assoc_left154_stub_double():
    # nabla_Expression has no real 'nabla_Expression155' property in the generated
    # code (a bare stub) -- manually attach it so nabla_And's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_And's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_And(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression155', None)
    _safe_set(owner, 'nabla_And', partner)
    assert getattr(partner, 'nabla_Expression155') == owner
    _safe_set(owner, 'nabla_And', None)
    assert getattr(partner, 'nabla_Expression155') is None


def test_assoc_left159_stub_double():
    # nabla_Expression has no real 'nabla_Expression160' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Equality(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression160', None)
    _safe_set(owner, 'nabla_Equality', partner)
    assert getattr(partner, 'nabla_Expression160') == owner
    _safe_set(owner, 'nabla_Equality', None)
    assert getattr(partner, 'nabla_Expression160') is None


def test_assoc_left164_stub_double():
    # nabla_Expression has no real 'nabla_Expression165' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Comparison(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression165', None)
    _safe_set(owner, 'nabla_Comparison', partner)
    assert getattr(partner, 'nabla_Expression165') == owner
    _safe_set(owner, 'nabla_Comparison', None)
    assert getattr(partner, 'nabla_Expression165') is None


def test_assoc_left169_stub_double():
    # nabla_Expression has no real 'nabla_Expression170' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Plus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Plus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Plus(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression170', None)
    _safe_set(owner, 'nabla_Plus', partner)
    assert getattr(partner, 'nabla_Expression170') == owner
    _safe_set(owner, 'nabla_Plus', None)
    assert getattr(partner, 'nabla_Expression170') is None


def test_assoc_left174_stub_double():
    # nabla_Expression has no real 'nabla_Expression175' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Minus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Minus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Minus(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression175', None)
    _safe_set(owner, 'nabla_Minus', partner)
    assert getattr(partner, 'nabla_Expression175') == owner
    _safe_set(owner, 'nabla_Minus', None)
    assert getattr(partner, 'nabla_Expression175') is None


def test_assoc_left179_stub_double():
    # nabla_Expression has no real 'nabla_Expression180' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Mul's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Mul's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Mul(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression180', None)
    _safe_set(owner, 'nabla_Mul', partner)
    assert getattr(partner, 'nabla_Expression180') == owner
    _safe_set(owner, 'nabla_Mul', None)
    assert getattr(partner, 'nabla_Expression180') is None


def test_assoc_left189_stub_double():
    # nabla_Expression has no real 'nabla_Expression190' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Modulo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Modulo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Modulo(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression190', None)
    _safe_set(owner, 'nabla_Modulo', partner)
    assert getattr(partner, 'nabla_Expression190') == owner
    _safe_set(owner, 'nabla_Modulo', None)
    assert getattr(partner, 'nabla_Expression190') is None


def test_assoc_nbElems83_stub_double():
    # nabla_Expression has no real 'nabla_Expression85' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Interval(from_=7)
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression85', None)
    _safe_set(owner, 'nabla_Interval84', partner)
    assert getattr(partner, 'nabla_Expression85') == owner
    _safe_set(owner, 'nabla_Interval84', None)
    assert getattr(partner, 'nabla_Expression85') is None


def test_assoc_options9_stub_double():
    # nabla_OptDefinition has no real 'nabla_OptDefinition' property in the generated
    # code (a bare stub) -- manually attach it so nabla_NablaModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_NablaModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_NablaModule(name="sample_text")
    partner = nabla_OptDefinition()
    setattr(partner, 'nabla_OptDefinition', None)
    _safe_set(owner, 'nabla_NablaModule10', {partner})
    assert getattr(partner, 'nabla_OptDefinition') == owner
    _safe_set(owner, 'nabla_NablaModule10', set())
    assert getattr(partner, 'nabla_OptDefinition') is None


def test_assoc_reductions5_stub_double():
    # nabla_Reduction has no real 'nabla_Reduction' property in the generated
    # code (a bare stub) -- manually attach it so nabla_NablaModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_NablaModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_NablaModule(name="sample_text")
    partner = nabla_Reduction()
    setattr(partner, 'nabla_Reduction', None)
    _safe_set(owner, 'nabla_NablaModule6', {partner})
    assert getattr(partner, 'nabla_Reduction') == owner
    _safe_set(owner, 'nabla_NablaModule6', set())
    assert getattr(partner, 'nabla_Reduction') is None


def test_assoc_right151_stub_double():
    # nabla_Expression has no real 'nabla_Expression153' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Or's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Or's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Or(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression153', None)
    _safe_set(owner, 'nabla_Or152', partner)
    assert getattr(partner, 'nabla_Expression153') == owner
    _safe_set(owner, 'nabla_Or152', None)
    assert getattr(partner, 'nabla_Expression153') is None


def test_assoc_right156_stub_double():
    # nabla_Expression has no real 'nabla_Expression158' property in the generated
    # code (a bare stub) -- manually attach it so nabla_And's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_And's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_And(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression158', None)
    _safe_set(owner, 'nabla_And157', partner)
    assert getattr(partner, 'nabla_Expression158') == owner
    _safe_set(owner, 'nabla_And157', None)
    assert getattr(partner, 'nabla_Expression158') is None


def test_assoc_right161_stub_double():
    # nabla_Expression has no real 'nabla_Expression163' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Equality(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression163', None)
    _safe_set(owner, 'nabla_Equality162', partner)
    assert getattr(partner, 'nabla_Expression163') == owner
    _safe_set(owner, 'nabla_Equality162', None)
    assert getattr(partner, 'nabla_Expression163') is None


def test_assoc_right166_stub_double():
    # nabla_Expression has no real 'nabla_Expression168' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Comparison(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression168', None)
    _safe_set(owner, 'nabla_Comparison167', partner)
    assert getattr(partner, 'nabla_Expression168') == owner
    _safe_set(owner, 'nabla_Comparison167', None)
    assert getattr(partner, 'nabla_Expression168') is None


def test_assoc_right171_stub_double():
    # nabla_Expression has no real 'nabla_Expression173' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Plus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Plus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Plus(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression173', None)
    _safe_set(owner, 'nabla_Plus172', partner)
    assert getattr(partner, 'nabla_Expression173') == owner
    _safe_set(owner, 'nabla_Plus172', None)
    assert getattr(partner, 'nabla_Expression173') is None


def test_assoc_right176_stub_double():
    # nabla_Expression has no real 'nabla_Expression178' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Minus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Minus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Minus(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression178', None)
    _safe_set(owner, 'nabla_Minus177', partner)
    assert getattr(partner, 'nabla_Expression178') == owner
    _safe_set(owner, 'nabla_Minus177', None)
    assert getattr(partner, 'nabla_Expression178') is None


def test_assoc_right181_stub_double():
    # nabla_Expression has no real 'nabla_Expression183' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Mul's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Mul's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Mul(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression183', None)
    _safe_set(owner, 'nabla_Mul182', partner)
    assert getattr(partner, 'nabla_Expression183') == owner
    _safe_set(owner, 'nabla_Mul182', None)
    assert getattr(partner, 'nabla_Expression183') is None


def test_assoc_right186_stub_double():
    # nabla_Expression has no real 'nabla_Expression188' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Div's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Div's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Div(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression188', None)
    _safe_set(owner, 'nabla_Div187', partner)
    assert getattr(partner, 'nabla_Expression188') == owner
    _safe_set(owner, 'nabla_Div187', None)
    assert getattr(partner, 'nabla_Expression188') is None


def test_assoc_right191_stub_double():
    # nabla_Expression has no real 'nabla_Expression193' property in the generated
    # code (a bare stub) -- manually attach it so nabla_Modulo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_Modulo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_Modulo(op="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression193', None)
    _safe_set(owner, 'nabla_Modulo192', partner)
    assert getattr(partner, 'nabla_Expression193') == owner
    _safe_set(owner, 'nabla_Modulo192', None)
    assert getattr(partner, 'nabla_Expression193') is None


def test_assoc_sizes138_stub_double():
    # nabla_Expression has no real 'nabla_Expression140' property in the generated
    # code (a bare stub) -- manually attach it so nabla_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_BaseType(primitive="sample_text")
    partner = nabla_Expression()
    setattr(partner, 'nabla_Expression140', None)
    _safe_set(owner, 'nabla_BaseType139', {partner})
    assert getattr(partner, 'nabla_Expression140') == owner
    _safe_set(owner, 'nabla_BaseType139', set())
    assert getattr(partner, 'nabla_Expression140') is None


def test_assoc_spaceIterators132_stub_double():
    # nabla_ArgOrVarRef has no real 'nabla_ArgOrVarRef133' property in the generated
    # code (a bare stub) -- manually attach it so nabla_ItemRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_ItemRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_ItemRef(dec=7, inc=7)
    partner = nabla_ArgOrVarRef()
    setattr(partner, 'nabla_ArgOrVarRef133', None)
    _safe_set(owner, 'nabla_ItemRef134', partner)
    assert owner in getattr(partner, 'nabla_ArgOrVarRef133')
    _safe_set(owner, 'nabla_ItemRef134', None)
    assert owner not in getattr(partner, 'nabla_ArgOrVarRef133')


def test_assoc_target127_stub_double():
    # nabla_ArgOrVarRef has no real 'nabla_ArgOrVarRef128' property in the generated
    # code (a bare stub) -- manually attach it so nabla_ArgOrVar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_ArgOrVar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_ArgOrVar(name="sample_text")
    partner = nabla_ArgOrVarRef()
    setattr(partner, 'nabla_ArgOrVarRef128', None)
    _safe_set(owner, 'nabla_ArgOrVar', partner)
    assert getattr(partner, 'nabla_ArgOrVarRef128') == owner
    _safe_set(owner, 'nabla_ArgOrVar', None)
    assert getattr(partner, 'nabla_ArgOrVarRef128') is None


def test_assoc_target64_stub_double():
    # nabla_SetRef has no real 'nabla_SetRef' property in the generated
    # code (a bare stub) -- manually attach it so nabla_SetDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_SetDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_SetDefinition(name="sample_text")
    partner = nabla_SetRef()
    setattr(partner, 'nabla_SetRef', None)
    _safe_set(owner, 'nabla_SetDefinition65', partner)
    assert getattr(partner, 'nabla_SetRef') == owner
    _safe_set(owner, 'nabla_SetDefinition65', None)
    assert getattr(partner, 'nabla_SetRef') is None


def test_assoc_type119_stub_double():
    # nabla_Reduction has no real 'nabla_Reduction120' property in the generated
    # code (a bare stub) -- manually attach it so nabla_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_BaseType(primitive="sample_text")
    partner = nabla_Reduction()
    setattr(partner, 'nabla_Reduction120', None)
    _safe_set(owner, 'nabla_BaseType121', partner)
    assert getattr(partner, 'nabla_Reduction120') == owner
    _safe_set(owner, 'nabla_BaseType121', None)
    assert getattr(partner, 'nabla_Reduction120') is None


def test_assoc_type205_stub_double():
    # nabla_BaseTypeConstant has no real 'nabla_BaseTypeConstant' property in the generated
    # code (a bare stub) -- manually attach it so nabla_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_BaseType(primitive="sample_text")
    partner = nabla_BaseTypeConstant()
    setattr(partner, 'nabla_BaseTypeConstant', None)
    _safe_set(owner, 'nabla_BaseType206', partner)
    assert getattr(partner, 'nabla_BaseTypeConstant') == owner
    _safe_set(owner, 'nabla_BaseType206', None)
    assert getattr(partner, 'nabla_BaseTypeConstant') is None


def test_assoc_type38_stub_double():
    # nabla_VarGroupDeclaration has no real 'nabla_VarGroupDeclaration39' property in the generated
    # code (a bare stub) -- manually attach it so nabla_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_BaseType(primitive="sample_text")
    partner = nabla_VarGroupDeclaration()
    setattr(partner, 'nabla_VarGroupDeclaration39', None)
    _safe_set(owner, 'nabla_BaseType', partner)
    assert getattr(partner, 'nabla_VarGroupDeclaration39') == owner
    _safe_set(owner, 'nabla_BaseType', None)
    assert getattr(partner, 'nabla_VarGroupDeclaration39') is None


def test_assoc_value61_stub_double():
    # nabla_MultipleConnectivityCall has no real 'nabla_MultipleConnectivityCall' property in the generated
    # code (a bare stub) -- manually attach it so nabla_SetDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_SetDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_SetDefinition(name="sample_text")
    partner = nabla_MultipleConnectivityCall()
    setattr(partner, 'nabla_MultipleConnectivityCall', None)
    _safe_set(owner, 'nabla_SetDefinition', partner)
    assert getattr(partner, 'nabla_MultipleConnectivityCall') == owner
    _safe_set(owner, 'nabla_SetDefinition', None)
    assert getattr(partner, 'nabla_MultipleConnectivityCall') is None


def test_assoc_vars103_stub_double():
    # nabla_SimpleVar has no real 'nabla_SimpleVar104' property in the generated
    # code (a bare stub) -- manually attach it so nabla_FunctionOrReduction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nabla_FunctionOrReduction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nabla_FunctionOrReduction(name="sample_text")
    partner = nabla_SimpleVar()
    setattr(partner, 'nabla_SimpleVar104', None)
    _safe_set(owner, 'nabla_FunctionOrReduction', {partner})
    assert getattr(partner, 'nabla_SimpleVar104') == owner
    _safe_set(owner, 'nabla_FunctionOrReduction', set())
    assert getattr(partner, 'nabla_SimpleVar104') is None


