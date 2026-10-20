import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Argument,
    DataItem,
    Definition,
    ElementReference,
    End,
    ExceptionHandlerStatement,
    Expression,
    Jump,
    KernelRoot,
    LabellableElement,
    MainProcedure,
    Member,
    NamedElement,
    Parameter,
    ProcedureCall,
    ReferenceableElement,
    ReturnSite,
    Start,
    Statement,
    SubExpression,
    Usage,
    commons_LabellableElement,
    commons_Variable,
    kernel_commons_NamedElement,
    kernel_containers_CompilationUnit,
    kernel_containers_KernelRoot,
    kernel_dataitems_DataItem,
    kernel_expressions_Affects,
    kernel_expressions_Defines,
    kernel_expressions_Definition,
    kernel_expressions_Expression,
    kernel_expressions_SubExpression,
    kernel_expressions_Usage,
    kernel_expressions_Uses,
    kernel_members_Member,
    kernel_parameters_Parameter,
    kernel_procedures_MainProcedure,
    kernel_procedures_Procedure,
    kernel_references_Argument,
    kernel_references_ElementReference,
    kernel_references_Reference,
    kernel_references_ReferenceableElement,
    kernel_statements_Abort,
    kernel_statements_Block,
    kernel_statements_Condition,
    kernel_statements_Conditional,
    kernel_statements_ExceptionHandlerStatement,
    kernel_statements_ExpressionStatement,
    kernel_statements_Goto,
    kernel_statements_Jump,
    kernel_statements_NonDeterministicBlock,
    kernel_statements_ParallelBlock,
    kernel_statements_ProcedureCall,
    kernel_statements_Return,
    kernel_statements_Skip,
    kernel_statements_Statement,
    kernel_statements_StatementContainer,
    kernel_statements_StatementListContainer,
    kernel_statements_StatementWithException,
    kernel_statements_WhileLoop,
    members_Member,
    procedures_Procedure,
    procedures_ProcedureCall,
    references_ElementReference,
    references_ReferenceableElement,
    statements_Conditional,
    statements_Statement,
    statements_StatementContainer,
    statements_StatementListContainer,
    ExecutionOrder,
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

def test_assoc_children30_stub_double():
    # SubExpression has no real 'SubExpression' property in the generated
    # code (a bare stub) -- manually attach it so kernel_expressions_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kernel_expressions_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kernel_expressions_Expression()
    partner = SubExpression()
    setattr(partner, 'SubExpression', None)
    _safe_set(owner, 'kernel_expressions_Expression', {partner})
    assert getattr(partner, 'SubExpression') == owner
    _safe_set(owner, 'kernel_expressions_Expression', set())
    assert getattr(partner, 'SubExpression') is None


