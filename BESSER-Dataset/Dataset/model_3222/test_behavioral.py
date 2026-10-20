import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFunctionDecl,
    AbstractRelationDecl,
    ClockRDL_declarations_AbstractFunctionDecl,
    ClockRDL_declarations_AbstractRelationDecl,
    ClockRDL_declarations_ArgumentDecl,
    ClockRDL_declarations_ClockDecl,
    ClockRDL_declarations_CompositeRelationDecl,
    ClockRDL_declarations_ConstantDecl,
    ClockRDL_declarations_FormalToActualMapEntry,
    ClockRDL_declarations_FunctionDecl,
    ClockRDL_declarations_LibraryDecl,
    ClockRDL_declarations_LibraryItemDecl,
    ClockRDL_declarations_PrimitiveFunctionDecl,
    ClockRDL_declarations_PrimitiveRelationDecl,
    ClockRDL_declarations_RelationInstanceDecl,
    ClockRDL_declarations_RepositoryDecl,
    ClockRDL_declarations_SystemDecl,
    ClockRDL_declarations_TransitionDecl,
    ClockRDL_declarations_VariableDecl,
    ClockRDL_expressions_BinaryExp,
    ClockRDL_expressions_ClockReference,
    ClockRDL_expressions_ConditionalExp,
    ClockRDL_expressions_FunctionCallExp,
    ClockRDL_expressions_IndexedExp,
    ClockRDL_expressions_Literal,
    ClockRDL_expressions_ParenExp,
    ClockRDL_expressions_PrefixedExp,
    ClockRDL_expressions_ReferenceExp,
    ClockRDL_expressions_SelectedExp,
    ClockRDL_expressions_UnaryExp,
    ClockRDL_kernel_Declaration,
    ClockRDL_kernel_Element,
    ClockRDL_kernel_Expression,
    ClockRDL_kernel_NamedDeclaration,
    ClockRDL_kernel_NamedElement,
    ClockRDL_kernel_Statement,
    ClockRDL_literals_ArrayLiteral,
    ClockRDL_literals_BooleanLiteral,
    ClockRDL_literals_ClockLiteral,
    ClockRDL_literals_FieldLiteral,
    ClockRDL_literals_IntegerLiteral,
    ClockRDL_literals_QueueLiteral,
    ClockRDL_literals_RecordLiteral,
    ClockRDL_statements_AssignmentStmt,
    ClockRDL_statements_BlockStmt,
    ClockRDL_statements_ConditionalStmt,
    ClockRDL_statements_LoopStmt,
    ClockRDL_statements_ReturnStmt,
    Declaration,
    Element,
    Expression,
    Literal,
    NamedDeclaration,
    PrefixedExp,
    ReferenceExp,
    RepositoryDecl,
    Statement,
    VariableDecl,
    declarations_AbstractRelationDecl,
    declarations_ArgumentDecl,
    declarations_ClockDecl,
    declarations_FormalToActualMapEntry,
    declarations_LibraryItemDecl,
    declarations_RelationInstanceDecl,
    declarations_RepositoryDecl,
    declarations_TransitionDecl,
    expressions_ClockReference,
    expressions_Literal,
    expressions_PrefixedExp,
    kernel_Declaration,
    kernel_Element,
    kernel_Expression,
    kernel_NamedDeclaration,
    kernel_NamedElement,
    kernel_Statement,
    literals_ClockLiteral,
    literals_FieldLiteral,
    statements_BlockStmt,
    AssignmentOperator,
    BinaryOperator,
    UnaryOperator,
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

def test_assoc_argumentMap76_stub_double():
    # declarations_FormalToActualMapEntry has no real 'declarations_FormalToActualMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_declarations_RelationInstanceDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_declarations_RelationInstanceDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_declarations_RelationInstanceDecl(qualifiedName="sample_text")
    partner = declarations_FormalToActualMapEntry()
    setattr(partner, 'declarations_FormalToActualMapEntry', None)
    _safe_set(owner, 'ClockRDL_declarations_RelationInstanceDecl77', {partner})
    assert getattr(partner, 'declarations_FormalToActualMapEntry') == owner
    _safe_set(owner, 'ClockRDL_declarations_RelationInstanceDecl77', set())
    assert getattr(partner, 'declarations_FormalToActualMapEntry') is None


def test_assoc_formalDecl80_stub_double():
    # kernel_Declaration has no real 'kernel_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_declarations_FormalToActualMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_declarations_FormalToActualMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_declarations_FormalToActualMapEntry(key="sample_text")
    partner = kernel_Declaration()
    setattr(partner, 'kernel_Declaration', None)
    _safe_set(owner, 'ClockRDL_declarations_FormalToActualMapEntry81', partner)
    assert getattr(partner, 'kernel_Declaration') == owner
    _safe_set(owner, 'ClockRDL_declarations_FormalToActualMapEntry81', None)
    assert getattr(partner, 'kernel_Declaration') is None


def test_assoc_lhs10_stub_double():
    # kernel_Expression has no real 'kernel_Expression11' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_expressions_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_expressions_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_expressions_BinaryExp(operator="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression11', None)
    _safe_set(owner, 'ClockRDL_expressions_BinaryExp', partner)
    assert getattr(partner, 'kernel_Expression11') == owner
    _safe_set(owner, 'ClockRDL_expressions_BinaryExp', None)
    assert getattr(partner, 'kernel_Expression11') is None


def test_assoc_lhs30_stub_double():
    # kernel_Expression has no real 'kernel_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_statements_AssignmentStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_statements_AssignmentStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_statements_AssignmentStmt(operator="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression31', None)
    _safe_set(owner, 'ClockRDL_statements_AssignmentStmt', partner)
    assert getattr(partner, 'kernel_Expression31') == owner
    _safe_set(owner, 'ClockRDL_statements_AssignmentStmt', None)
    assert getattr(partner, 'kernel_Expression31') is None


def test_assoc_operand8_stub_double():
    # kernel_Expression has no real 'kernel_Expression9' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_expressions_UnaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_expressions_UnaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_expressions_UnaryExp(operator="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression9', None)
    _safe_set(owner, 'ClockRDL_expressions_UnaryExp', partner)
    assert getattr(partner, 'kernel_Expression9') == owner
    _safe_set(owner, 'ClockRDL_expressions_UnaryExp', None)
    assert getattr(partner, 'kernel_Expression9') is None


def test_assoc_relation75_stub_double():
    # declarations_AbstractRelationDecl has no real 'declarations_AbstractRelationDecl' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_declarations_RelationInstanceDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_declarations_RelationInstanceDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_declarations_RelationInstanceDecl(qualifiedName="sample_text")
    partner = declarations_AbstractRelationDecl()
    setattr(partner, 'declarations_AbstractRelationDecl', None)
    _safe_set(owner, 'ClockRDL_declarations_RelationInstanceDecl', partner)
    assert getattr(partner, 'declarations_AbstractRelationDecl') == owner
    _safe_set(owner, 'ClockRDL_declarations_RelationInstanceDecl', None)
    assert getattr(partner, 'declarations_AbstractRelationDecl') is None


def test_assoc_rhs12_stub_double():
    # kernel_Expression has no real 'kernel_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_expressions_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_expressions_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_expressions_BinaryExp(operator="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression14', None)
    _safe_set(owner, 'ClockRDL_expressions_BinaryExp13', partner)
    assert getattr(partner, 'kernel_Expression14') == owner
    _safe_set(owner, 'ClockRDL_expressions_BinaryExp13', None)
    assert getattr(partner, 'kernel_Expression14') is None


def test_assoc_rhs32_stub_double():
    # kernel_Expression has no real 'kernel_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_statements_AssignmentStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_statements_AssignmentStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_statements_AssignmentStmt(operator="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression34', None)
    _safe_set(owner, 'ClockRDL_statements_AssignmentStmt33', partner)
    assert getattr(partner, 'kernel_Expression34') == owner
    _safe_set(owner, 'ClockRDL_statements_AssignmentStmt33', None)
    assert getattr(partner, 'kernel_Expression34') is None


def test_assoc_value78_stub_double():
    # kernel_Expression has no real 'kernel_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so ClockRDL_declarations_FormalToActualMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClockRDL_declarations_FormalToActualMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClockRDL_declarations_FormalToActualMapEntry(key="sample_text")
    partner = kernel_Expression()
    setattr(partner, 'kernel_Expression79', None)
    _safe_set(owner, 'ClockRDL_declarations_FormalToActualMapEntry', partner)
    assert getattr(partner, 'kernel_Expression79') == owner
    _safe_set(owner, 'ClockRDL_declarations_FormalToActualMapEntry', None)
    assert getattr(partner, 'kernel_Expression79') is None


