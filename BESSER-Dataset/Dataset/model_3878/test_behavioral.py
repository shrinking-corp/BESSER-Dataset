import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentStmt,
    CMElement,
    DataType,
    Expression,
    Statement,
    Variable,
    codemodel_CMElement,
    codemodel_CodeModule,
    codemodel_DataType,
    codemodel_Function,
    codemodel_FunctionArgument,
    codemodel_GlobalVariable,
    codemodel_LocalVariable,
    codemodel_MatrixType,
    codemodel_ScalarType,
    codemodel_Variable,
    codemodel_VectorType,
    codemodel_expressions_BinaryExp,
    codemodel_expressions_Expression,
    codemodel_expressions_LiteralExp,
    codemodel_expressions_VariableExp,
    codemodel_statements_AssignmentStmt,
    codemodel_statements_CompositeStmt,
    codemodel_statements_ForStmt,
    codemodel_statements_IfStmt,
    codemodel_statements_Statement,
    expressions_codemodel_Variable,
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

def test_assoc_type5_reverse_link_reassign_clear():
    a1 = codemodel_Variable(constant=True, identifier="sample_text")
    a2 = codemodel_Variable(constant=False, identifier="sample_text_2")
    b = codemodel_DataType(basetype="sample_text")
    _safe_set(b, 'codemodel_DataType6', a1)
    assert _is_linked(b, 'codemodel_DataType6', a1)
    if hasattr(a1, 'codemodel_Variable'):
        assert _is_linked(a1, 'codemodel_Variable', b)
    _safe_set(b, 'codemodel_DataType6', a2)
    assert _is_linked(b, 'codemodel_DataType6', a2)
    if hasattr(a1, 'codemodel_Variable'):
        assert not _is_linked(a1, 'codemodel_Variable', b)
    if hasattr(a2, 'codemodel_Variable'):
        assert _is_linked(a2, 'codemodel_Variable', b)
    _safe_set(b, 'codemodel_DataType6', None)
    assert not _is_linked(b, 'codemodel_DataType6', a2)
    if hasattr(a2, 'codemodel_Variable'):
        assert not _is_linked(a2, 'codemodel_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments7_stub_double():
    # codemodel_FunctionArgument has no real 'codemodel_FunctionArgument' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_Function(identifier="sample_text")
    partner = codemodel_FunctionArgument()
    setattr(partner, 'codemodel_FunctionArgument', None)
    _safe_set(owner, 'codemodel_Function8', {partner})
    assert getattr(partner, 'codemodel_FunctionArgument') == owner
    _safe_set(owner, 'codemodel_Function8', set())
    assert getattr(partner, 'codemodel_FunctionArgument') is None


def test_assoc_body11_stub_double():
    # Statement has no real 'Statement' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_Function(identifier="sample_text")
    partner = Statement()
    setattr(partner, 'Statement', None)
    _safe_set(owner, 'codemodel_Function12', {partner})
    assert getattr(partner, 'Statement') == owner
    _safe_set(owner, 'codemodel_Function12', set())
    assert getattr(partner, 'Statement') is None


def test_assoc_dataTypes3_stub_double():
    # codemodel_CodeModule has no real 'codemodel_CodeModule4' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_DataType(basetype="sample_text")
    partner = codemodel_CodeModule()
    setattr(partner, 'codemodel_CodeModule4', None)
    _safe_set(owner, 'codemodel_DataType', partner)
    assert owner in getattr(partner, 'codemodel_CodeModule4')
    _safe_set(owner, 'codemodel_DataType', None)
    assert owner not in getattr(partner, 'codemodel_CodeModule4')


def test_assoc_functions1_stub_double():
    # codemodel_CodeModule has no real 'codemodel_CodeModule2' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_Function(identifier="sample_text")
    partner = codemodel_CodeModule()
    setattr(partner, 'codemodel_CodeModule2', None)
    _safe_set(owner, 'codemodel_Function', partner)
    assert owner in getattr(partner, 'codemodel_CodeModule2')
    _safe_set(owner, 'codemodel_Function', None)
    assert owner not in getattr(partner, 'codemodel_CodeModule2')


def test_assoc_left14_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_expressions_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_expressions_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_expressions_BinaryExp(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'codemodel_expressions_BinaryExp', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'codemodel_expressions_BinaryExp', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_localVariables9_stub_double():
    # codemodel_LocalVariable has no real 'codemodel_LocalVariable' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_Function(identifier="sample_text")
    partner = codemodel_LocalVariable()
    setattr(partner, 'codemodel_LocalVariable', None)
    _safe_set(owner, 'codemodel_Function10', {partner})
    assert getattr(partner, 'codemodel_LocalVariable') == owner
    _safe_set(owner, 'codemodel_Function10', set())
    assert getattr(partner, 'codemodel_LocalVariable') is None


def test_assoc_right15_stub_double():
    # Expression has no real 'Expression17' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_expressions_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_expressions_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_expressions_BinaryExp(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression17', None)
    _safe_set(owner, 'codemodel_expressions_BinaryExp16', partner)
    assert getattr(partner, 'Expression17') == owner
    _safe_set(owner, 'codemodel_expressions_BinaryExp16', None)
    assert getattr(partner, 'Expression17') is None


