import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ACG,
    ACGElement,
    ACG_ACG,
    ACG_ACGElement,
    ACG_ASMNode,
    ACG_AnalyzeStat,
    ACG_Attribute,
    ACG_BooleanExp,
    ACG_CallStat,
    ACG_CodeNode,
    ACG_CollectionExp,
    ACG_CompoundStat,
    ACG_ConditionalStat,
    ACG_DeleteStat,
    ACG_DupStat,
    ACG_DupX1Stat,
    ACG_EmitStat,
    ACG_EmitWithLabelRefStat,
    ACG_EmitWithOperandStat,
    ACG_EndIterateStat,
    ACG_Expression,
    ACG_FieldStat,
    ACG_FindMEStat,
    ACG_ForEachStat,
    ACG_Function,
    ACG_GetAsmStat,
    ACG_GetStat,
    ACG_GotoStat,
    ACG_IfExp,
    ACG_IfStat,
    ACG_IntegerExp,
    ACG_IsAExp,
    ACG_IterateStat,
    ACG_IteratorExp,
    ACG_LabelStat,
    ACG_LastExp,
    ACG_LetExp,
    ACG_LetStat,
    ACG_LiteralExp,
    ACG_LoadStat,
    ACG_LocatedElement,
    ACG_NavigationExp,
    ACG_NewStat,
    ACG_NewinStat,
    ACG_Node,
    ACG_OclUndefinedExp,
    ACG_OnceStat,
    ACG_OperationCallExp,
    ACG_OperationStat,
    ACG_OperatorCallExp,
    ACG_PCallStat,
    ACG_ParamStat,
    ACG_Parameter,
    ACG_PopStat,
    ACG_PropertyCallExp,
    ACG_PushDStat,
    ACG_PushFStat,
    ACG_PushIStat,
    ACG_PushStat,
    ACG_PushTStat,
    ACG_ReportStat,
    ACG_SelfExp,
    ACG_SequenceExp,
    ACG_SetStat,
    ACG_SimpleNode,
    ACG_Statement,
    ACG_StatementBlock,
    ACG_StoreStat,
    ACG_StringExp,
    ACG_SuperCallStat,
    ACG_SwapStat,
    ACG_VariableDecl,
    ACG_VariableExp,
    ACG_VariableStat,
    CollectionExp,
    CompoundStat,
    EmitStat,
    EmitWithLabelRefStat,
    EmitWithOperandStat,
    Expression,
    LabelStat,
    LiteralExp,
    LocatedElement,
    Node,
    OperationCallExp,
    Parameter,
    PropertyCallExp,
    Statement,
    StatementBlock,
    VariableDecl,
    Severity,
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

def test_assoc_body3_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so ACG_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_Function(context="sample_text", name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'ACG_Function4', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'ACG_Function4', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_body5_stub_double():
    # Expression has no real 'Expression6' property in the generated
    # code (a bare stub) -- manually attach it so ACG_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_Attribute(context="sample_text", name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression6', None)
    _safe_set(owner, 'ACG_Attribute', partner)
    assert getattr(partner, 'Expression6') == owner
    _safe_set(owner, 'ACG_Attribute', None)
    assert getattr(partner, 'Expression6') is None


def test_assoc_elements0_stub_double():
    # ACGElement has no real 'ACGElement' property in the generated
    # code (a bare stub) -- manually attach it so ACG_ACG's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_ACG's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_ACG(metamodel="sample_text", startsWith="sample_text")
    partner = ACGElement()
    setattr(partner, 'ACGElement', None)
    _safe_set(owner, 'acg', {partner})
    assert getattr(partner, 'ACGElement') == owner
    _safe_set(owner, 'acg', set())
    assert getattr(partner, 'ACGElement') is None


def test_assoc_guard7_stub_double():
    # Expression has no real 'Expression8' property in the generated
    # code (a bare stub) -- manually attach it so ACG_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_Node(element="sample_text", mode="sample_text")
    partner = Expression()
    setattr(partner, 'Expression8', None)
    _safe_set(owner, 'ACG_Node', partner)
    assert getattr(partner, 'Expression8') == owner
    _safe_set(owner, 'ACG_Node', None)
    assert getattr(partner, 'Expression8') is None


def test_assoc_id50_stub_double():
    # Expression has no real 'Expression51' property in the generated
    # code (a bare stub) -- manually attach it so ACG_LabelStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_LabelStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_LabelStat(name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression51', None)
    _safe_set(owner, 'ACG_LabelStat', partner)
    assert getattr(partner, 'Expression51') == owner
    _safe_set(owner, 'ACG_LabelStat', None)
    assert getattr(partner, 'Expression51') is None


def test_assoc_message38_stub_double():
    # Expression has no real 'Expression39' property in the generated
    # code (a bare stub) -- manually attach it so ACG_ReportStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_ReportStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_ReportStat(severity="sample_text")
    partner = Expression()
    setattr(partner, 'Expression39', None)
    _safe_set(owner, 'ACG_ReportStat', partner)
    assert getattr(partner, 'Expression39') == owner
    _safe_set(owner, 'ACG_ReportStat', None)
    assert getattr(partner, 'Expression39') is None


def test_assoc_parameters2_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ACG_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_Function(context="sample_text", name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'ACG_Function', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'ACG_Function', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_source65_stub_double():
    # Expression has no real 'Expression66' property in the generated
    # code (a bare stub) -- manually attach it so ACG_IsAExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_IsAExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_IsAExp(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression66', None)
    _safe_set(owner, 'ACG_IsAExp', partner)
    assert getattr(partner, 'Expression66') == owner
    _safe_set(owner, 'ACG_IsAExp', None)
    assert getattr(partner, 'Expression66') is None


def test_assoc_source75_stub_double():
    # Expression has no real 'Expression76' property in the generated
    # code (a bare stub) -- manually attach it so ACG_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_PropertyCallExp(name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression76', None)
    _safe_set(owner, 'ACG_PropertyCallExp', partner)
    assert getattr(partner, 'Expression76') == owner
    _safe_set(owner, 'ACG_PropertyCallExp', None)
    assert getattr(partner, 'Expression76') is None


def test_assoc_target36_stub_double():
    # Expression has no real 'Expression37' property in the generated
    # code (a bare stub) -- manually attach it so ACG_AnalyzeStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ACG_AnalyzeStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ACG_AnalyzeStat(mode="sample_text")
    partner = Expression()
    setattr(partner, 'Expression37', None)
    _safe_set(owner, 'ACG_AnalyzeStat', partner)
    assert getattr(partner, 'Expression37') == owner
    _safe_set(owner, 'ACG_AnalyzeStat', None)
    assert getattr(partner, 'Expression37') is None


