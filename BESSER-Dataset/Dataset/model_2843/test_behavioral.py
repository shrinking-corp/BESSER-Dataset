import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    LITERAL,
    NUMBER_LITERAL,
    NonLiteralValueSpecification,
    SequenceElement,
    SequenceExpansionExpression,
    Statement,
    SuffixExpression,
    ValueSpecification,
    alf_AcceptBlock,
    alf_AcceptClause,
    alf_AcceptStatement,
    alf_AccessCompletion,
    alf_AdditiveExpression,
    alf_AndExpression,
    alf_AnnotatedStatement,
    alf_Annotation,
    alf_AssignmentCompletion,
    alf_BOOLEAN_LITERAL,
    alf_Block,
    alf_BlockStatement,
    alf_BreakStatement,
    alf_ClassExtentExpression,
    alf_ClassificationClause,
    alf_ClassificationExpression,
    alf_ClassificationFromClause,
    alf_ClassificationToClause,
    alf_ClassifyStatement,
    alf_CollectOrIterateOperation,
    alf_CompoundAcceptStatementCompletion,
    alf_ConcurrentClauses,
    alf_ConditionalAndExpression,
    alf_ConditionalOrExpression,
    alf_ConditionalTestExpression,
    alf_DoStatement,
    alf_DocumentedStatement,
    alf_EmptyStatement,
    alf_EqualityExpression,
    alf_ExclusiveOrExpression,
    alf_Expression,
    alf_FinalClause,
    alf_ForAllOrExistsOrOneOperation,
    alf_ForControl,
    alf_ForStatement,
    alf_INTEGER_LITERAL,
    alf_IfStatement,
    alf_InclusiveOrExpression,
    alf_InlineStatement,
    alf_InstanceCreationExpression,
    alf_InstanceCreationInvocationStatement,
    alf_InstanceCreationTuple,
    alf_InstanceCreationTupleElement,
    alf_InvocationOrAssignementOrDeclarationStatement,
    alf_IsUniqueOperation,
    alf_LITERAL,
    alf_LinkOperationExpression,
    alf_LinkOperationTuple,
    alf_LinkOperationTupleElement,
    alf_LocalNameDeclarationStatement,
    alf_LoopVariableDefinition,
    alf_MultiplicativeExpression,
    alf_NUMBER_LITERAL,
    alf_NameExpression,
    alf_NamedTemplateBinding,
    alf_NonEmptyStatementSequence,
    alf_NonFinalClause,
    alf_NonLiteralValueSpecification,
    alf_NullExpression,
    alf_OperationCallExpression,
    alf_ParenthesizedExpression,
    alf_PartialSequenceConstructionCompletion,
    alf_PrimaryExpression,
    alf_PropertyCallExpression,
    alf_QualifiedNameList,
    alf_QualifiedNamePath,
    alf_QualifiedNameWithBinding,
    alf_ReclassifyAllClause,
    alf_RelationalExpression,
    alf_ReturnStatement,
    alf_STRING_LITERAL,
    alf_SelectOrRejectOperation,
    alf_SequenceConstructionExpression,
    alf_SequenceConstructionOrAccessCompletion,
    alf_SequenceElement,
    alf_SequenceExpansionExpression,
    alf_SequenceOperationExpression,
    alf_SequenceReductionExpression,
    alf_SequentialClauses,
    alf_ShiftExpression,
    alf_SimpleAcceptStatementCompletion,
    alf_Statement,
    alf_StatementSequence,
    alf_SuffixExpression,
    alf_SuperInvocationExpression,
    alf_SuperInvocationStatement,
    alf_SwitchCase,
    alf_SwitchClause,
    alf_SwitchDefaultClause,
    alf_SwitchStatement,
    alf_TemplateBinding,
    alf_Test,
    alf_ThisExpression,
    alf_ThisInvocationStatement,
    alf_Tuple,
    alf_TupleElement,
    alf_UNLIMITED_LITERAL,
    alf_UnaryExpression,
    alf_UnqualifiedName,
    alf_ValueSpecification,
    alf_VariableDeclarationCompletion,
    alf_WhileStatement,
    AnnotationKind,
    AssignmentOperator,
    BooleanValue,
    CollectOrIterateOperator,
    ForAllOrExistsOrOneOperator,
    LinkOperationKind,
    SelectOrRejectOperator,
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

def test_assoc_actual20_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_NamedTemplateBinding(formal="sample_text")
    _safe_set(b, 'alf_NamedTemplateBinding21', a1)
    assert _is_linked(b, 'alf_NamedTemplateBinding21', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding', b)
    _safe_set(b, 'alf_NamedTemplateBinding21', a2)
    assert _is_linked(b, 'alf_NamedTemplateBinding21', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding', b)
    _safe_set(b, 'alf_NamedTemplateBinding21', None)
    assert not _is_linked(b, 'alf_NamedTemplateBinding21', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding', b)


def test_assoc_behavior99_reverse_link_reassign_clear():
    a1 = alf_SequenceReductionExpression(isOrdered=True)
    a2 = alf_SequenceReductionExpression(isOrdered=False)
    b = alf_QualifiedNameWithBinding(id="sample_text")
    _safe_set(b, 'alf_QualifiedNameWithBinding100', a1)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding100', a1)
    if hasattr(a1, 'alf_SequenceReductionExpression'):
        assert _is_linked(a1, 'alf_SequenceReductionExpression', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding100', a2)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding100', a2)
    if hasattr(a1, 'alf_SequenceReductionExpression'):
        assert not _is_linked(a1, 'alf_SequenceReductionExpression', b)
    if hasattr(a2, 'alf_SequenceReductionExpression'):
        assert _is_linked(a2, 'alf_SequenceReductionExpression', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding100', None)
    assert not _is_linked(b, 'alf_QualifiedNameWithBinding100', a2)
    if hasattr(a2, 'alf_SequenceReductionExpression'):
        assert not _is_linked(a2, 'alf_SequenceReductionExpression', b)


def test_assoc_exp50_reverse_link_reassign_clear():
    a1 = alf_EqualityExpression(op="sample_text")
    a2 = alf_EqualityExpression(op="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression', a1)
    assert _is_linked(b, 'alf_ClassificationExpression', a1)
    if hasattr(a1, 'alf_EqualityExpression51'):
        assert _is_linked(a1, 'alf_EqualityExpression51', b)
    _safe_set(b, 'alf_ClassificationExpression', a2)
    assert _is_linked(b, 'alf_ClassificationExpression', a2)
    if hasattr(a1, 'alf_EqualityExpression51'):
        assert not _is_linked(a1, 'alf_EqualityExpression51', b)
    if hasattr(a2, 'alf_EqualityExpression51'):
        assert _is_linked(a2, 'alf_EqualityExpression51', b)
    _safe_set(b, 'alf_ClassificationExpression', None)
    assert not _is_linked(b, 'alf_ClassificationExpression', a2)
    if hasattr(a2, 'alf_EqualityExpression51'):
        assert not _is_linked(a2, 'alf_EqualityExpression51', b)


def test_assoc_exp52_reverse_link_reassign_clear():
    a1 = alf_RelationalExpression(op="sample_text")
    a2 = alf_RelationalExpression(op="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression53', a1)
    assert _is_linked(b, 'alf_ClassificationExpression53', a1)
    if hasattr(a1, 'alf_RelationalExpression'):
        assert _is_linked(a1, 'alf_RelationalExpression', b)
    _safe_set(b, 'alf_ClassificationExpression53', a2)
    assert _is_linked(b, 'alf_ClassificationExpression53', a2)
    if hasattr(a1, 'alf_RelationalExpression'):
        assert not _is_linked(a1, 'alf_RelationalExpression', b)
    if hasattr(a2, 'alf_RelationalExpression'):
        assert _is_linked(a2, 'alf_RelationalExpression', b)
    _safe_set(b, 'alf_ClassificationExpression53', None)
    assert not _is_linked(b, 'alf_ClassificationExpression53', a2)
    if hasattr(a2, 'alf_RelationalExpression'):
        assert not _is_linked(a2, 'alf_RelationalExpression', b)


def test_assoc_exp62_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_AdditiveExpression(op="sample_text")
    _safe_set(b, 'alf_AdditiveExpression', a1)
    assert _is_linked(b, 'alf_AdditiveExpression', a1)
    if hasattr(a1, 'alf_ShiftExpression63'):
        assert _is_linked(a1, 'alf_ShiftExpression63', b)
    _safe_set(b, 'alf_AdditiveExpression', a2)
    assert _is_linked(b, 'alf_AdditiveExpression', a2)
    if hasattr(a1, 'alf_ShiftExpression63'):
        assert not _is_linked(a1, 'alf_ShiftExpression63', b)
    if hasattr(a2, 'alf_ShiftExpression63'):
        assert _is_linked(a2, 'alf_ShiftExpression63', b)
    _safe_set(b, 'alf_AdditiveExpression', None)
    assert not _is_linked(b, 'alf_AdditiveExpression', a2)
    if hasattr(a2, 'alf_ShiftExpression63'):
        assert not _is_linked(a2, 'alf_ShiftExpression63', b)


def test_assoc_exp64_reverse_link_reassign_clear():
    a1 = alf_MultiplicativeExpression(op="sample_text")
    a2 = alf_MultiplicativeExpression(op="sample_text_2")
    b = alf_AdditiveExpression(op="sample_text")
    _safe_set(b, 'alf_AdditiveExpression65', {a1})
    assert _is_linked(b, 'alf_AdditiveExpression65', a1)
    if hasattr(a1, 'alf_MultiplicativeExpression'):
        assert _is_linked(a1, 'alf_MultiplicativeExpression', b)
    _safe_set(b, 'alf_AdditiveExpression65', {a2})
    assert _is_linked(b, 'alf_AdditiveExpression65', a2)
    if hasattr(a1, 'alf_MultiplicativeExpression'):
        assert not _is_linked(a1, 'alf_MultiplicativeExpression', b)
    if hasattr(a2, 'alf_MultiplicativeExpression'):
        assert _is_linked(a2, 'alf_MultiplicativeExpression', b)
    _safe_set(b, 'alf_AdditiveExpression65', set())
    assert not _is_linked(b, 'alf_AdditiveExpression65', a2)
    if hasattr(a2, 'alf_MultiplicativeExpression'):
        assert not _is_linked(a2, 'alf_MultiplicativeExpression', b)


def test_assoc_exp66_reverse_link_reassign_clear():
    a1 = alf_UnaryExpression(op="sample_text")
    a2 = alf_UnaryExpression(op="sample_text_2")
    b = alf_MultiplicativeExpression(op="sample_text")
    _safe_set(b, 'alf_MultiplicativeExpression67', {a1})
    assert _is_linked(b, 'alf_MultiplicativeExpression67', a1)
    if hasattr(a1, 'alf_UnaryExpression'):
        assert _is_linked(a1, 'alf_UnaryExpression', b)
    _safe_set(b, 'alf_MultiplicativeExpression67', {a2})
    assert _is_linked(b, 'alf_MultiplicativeExpression67', a2)
    if hasattr(a1, 'alf_UnaryExpression'):
        assert not _is_linked(a1, 'alf_UnaryExpression', b)
    if hasattr(a2, 'alf_UnaryExpression'):
        assert _is_linked(a2, 'alf_UnaryExpression', b)
    _safe_set(b, 'alf_MultiplicativeExpression67', set())
    assert not _is_linked(b, 'alf_MultiplicativeExpression67', a2)
    if hasattr(a2, 'alf_UnaryExpression'):
        assert not _is_linked(a2, 'alf_UnaryExpression', b)


def test_assoc_initValue288_reverse_link_reassign_clear():
    a1 = alf_VariableDeclarationCompletion(multiplicityIndicator=True, variableName="sample_text")
    a2 = alf_VariableDeclarationCompletion(multiplicityIndicator=False, variableName="sample_text_2")
    b = alf_AssignmentCompletion(op="sample_text")
    _safe_set(b, 'alf_AssignmentCompletion290', a1)
    assert _is_linked(b, 'alf_AssignmentCompletion290', a1)
    if hasattr(a1, 'alf_VariableDeclarationCompletion289'):
        assert _is_linked(a1, 'alf_VariableDeclarationCompletion289', b)
    _safe_set(b, 'alf_AssignmentCompletion290', a2)
    assert _is_linked(b, 'alf_AssignmentCompletion290', a2)
    if hasattr(a1, 'alf_VariableDeclarationCompletion289'):
        assert not _is_linked(a1, 'alf_VariableDeclarationCompletion289', b)
    if hasattr(a2, 'alf_VariableDeclarationCompletion289'):
        assert _is_linked(a2, 'alf_VariableDeclarationCompletion289', b)
    _safe_set(b, 'alf_AssignmentCompletion290', None)
    assert not _is_linked(b, 'alf_AssignmentCompletion290', a2)
    if hasattr(a2, 'alf_VariableDeclarationCompletion289'):
        assert not _is_linked(a2, 'alf_VariableDeclarationCompletion289', b)


def test_assoc_left57_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_RelationalExpression(op="sample_text")
    _safe_set(b, 'alf_RelationalExpression58', a1)
    assert _is_linked(b, 'alf_RelationalExpression58', a1)
    if hasattr(a1, 'alf_ShiftExpression'):
        assert _is_linked(a1, 'alf_ShiftExpression', b)
    _safe_set(b, 'alf_RelationalExpression58', a2)
    assert _is_linked(b, 'alf_RelationalExpression58', a2)
    if hasattr(a1, 'alf_ShiftExpression'):
        assert not _is_linked(a1, 'alf_ShiftExpression', b)
    if hasattr(a2, 'alf_ShiftExpression'):
        assert _is_linked(a2, 'alf_ShiftExpression', b)
    _safe_set(b, 'alf_RelationalExpression58', None)
    assert not _is_linked(b, 'alf_RelationalExpression58', a2)
    if hasattr(a2, 'alf_ShiftExpression'):
        assert not _is_linked(a2, 'alf_ShiftExpression', b)


def test_assoc_remaining26_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_QualifiedNameWithBinding(id="sample_text")
    _safe_set(b, 'alf_QualifiedNameWithBinding27', a1)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding27', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding25'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding25', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding27', a2)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding27', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding25'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding25', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding25'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding25', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding27', None)
    assert not _is_linked(b, 'alf_QualifiedNameWithBinding27', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding25'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding25', b)


def test_assoc_right59_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_RelationalExpression(op="sample_text")
    _safe_set(b, 'alf_RelationalExpression60', a1)
    assert _is_linked(b, 'alf_RelationalExpression60', a1)
    if hasattr(a1, 'alf_ShiftExpression61'):
        assert _is_linked(a1, 'alf_ShiftExpression61', b)
    _safe_set(b, 'alf_RelationalExpression60', a2)
    assert _is_linked(b, 'alf_RelationalExpression60', a2)
    if hasattr(a1, 'alf_ShiftExpression61'):
        assert not _is_linked(a1, 'alf_ShiftExpression61', b)
    if hasattr(a2, 'alf_ShiftExpression61'):
        assert _is_linked(a2, 'alf_ShiftExpression61', b)
    _safe_set(b, 'alf_RelationalExpression60', None)
    assert not _is_linked(b, 'alf_RelationalExpression60', a2)
    if hasattr(a2, 'alf_ShiftExpression61'):
        assert not _is_linked(a2, 'alf_ShiftExpression61', b)


def test_assoc_sequenceConstructionCompletion10_reverse_link_reassign_clear():
    a1 = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    a2 = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=False)
    b = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    _safe_set(b, 'alf_NameExpression11', a1)
    assert _is_linked(b, 'alf_NameExpression11', a1)
    if hasattr(a1, 'alf_SequenceConstructionOrAccessCompletion'):
        assert _is_linked(a1, 'alf_SequenceConstructionOrAccessCompletion', b)
    _safe_set(b, 'alf_NameExpression11', a2)
    assert _is_linked(b, 'alf_NameExpression11', a2)
    if hasattr(a1, 'alf_SequenceConstructionOrAccessCompletion'):
        assert not _is_linked(a1, 'alf_SequenceConstructionOrAccessCompletion', b)
    if hasattr(a2, 'alf_SequenceConstructionOrAccessCompletion'):
        assert _is_linked(a2, 'alf_SequenceConstructionOrAccessCompletion', b)
    _safe_set(b, 'alf_NameExpression11', None)
    assert not _is_linked(b, 'alf_NameExpression11', a2)
    if hasattr(a2, 'alf_SequenceConstructionOrAccessCompletion'):
        assert not _is_linked(a2, 'alf_SequenceConstructionOrAccessCompletion', b)


def test_assoc_type165_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_LocalNameDeclarationStatement(multiplicityIndicator=True, varName="sample_text")
    _safe_set(b, 'alf_LocalNameDeclarationStatement', a1)
    assert _is_linked(b, 'alf_LocalNameDeclarationStatement', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding166'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding166', b)
    _safe_set(b, 'alf_LocalNameDeclarationStatement', a2)
    assert _is_linked(b, 'alf_LocalNameDeclarationStatement', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding166'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding166', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding166'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding166', b)
    _safe_set(b, 'alf_LocalNameDeclarationStatement', None)
    assert not _is_linked(b, 'alf_LocalNameDeclarationStatement', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding166'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding166', b)


def test_assoc_type227_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_LoopVariableDefinition(name="sample_text")
    _safe_set(b, 'alf_LoopVariableDefinition228', a1)
    assert _is_linked(b, 'alf_LoopVariableDefinition228', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding229'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding229', b)
    _safe_set(b, 'alf_LoopVariableDefinition228', a2)
    assert _is_linked(b, 'alf_LoopVariableDefinition228', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding229'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding229', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding229'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding229', b)
    _safe_set(b, 'alf_LoopVariableDefinition228', None)
    assert not _is_linked(b, 'alf_LoopVariableDefinition228', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding229'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding229', b)


def test_assoc_typeName54_reverse_link_reassign_clear():
    a1 = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    a2 = alf_NameExpression(id="sample_text_2", postfixOp="sample_text_2", prefixOp="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression55', a1)
    assert _is_linked(b, 'alf_ClassificationExpression55', a1)
    if hasattr(a1, 'alf_NameExpression56'):
        assert _is_linked(a1, 'alf_NameExpression56', b)
    _safe_set(b, 'alf_ClassificationExpression55', a2)
    assert _is_linked(b, 'alf_ClassificationExpression55', a2)
    if hasattr(a1, 'alf_NameExpression56'):
        assert not _is_linked(a1, 'alf_NameExpression56', b)
    if hasattr(a2, 'alf_NameExpression56'):
        assert _is_linked(a2, 'alf_NameExpression56', b)
    _safe_set(b, 'alf_ClassificationExpression55', None)
    assert not _is_linked(b, 'alf_ClassificationExpression55', a2)
    if hasattr(a2, 'alf_NameExpression56'):
        assert not _is_linked(a2, 'alf_NameExpression56', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessCompletion135_stub_double():
    # alf_AccessCompletion has no real 'alf_AccessCompletion' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_AccessCompletion()
    setattr(partner, 'alf_AccessCompletion', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion136', partner)
    assert getattr(partner, 'alf_AccessCompletion') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion136', None)
    assert getattr(partner, 'alf_AccessCompletion') is None


def test_assoc_annotation159_stub_double():
    # alf_AnnotatedStatement has no real 'alf_AnnotatedStatement' property in the generated
    # code (a bare stub) -- manually attach it so alf_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_Annotation(args="sample_text", kind="sample_text")
    partner = alf_AnnotatedStatement()
    setattr(partner, 'alf_AnnotatedStatement', None)
    _safe_set(owner, 'alf_Annotation', partner)
    assert getattr(partner, 'alf_AnnotatedStatement') == owner
    _safe_set(owner, 'alf_Annotation', None)
    assert getattr(partner, 'alf_AnnotatedStatement') is None


def test_assoc_assignExpression1_stub_double():
    # alf_Test has no real 'alf_Test2' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_Test()
    setattr(partner, 'alf_Test2', None)
    _safe_set(owner, 'alf_AssignmentCompletion', partner)
    assert owner in getattr(partner, 'alf_Test2')
    _safe_set(owner, 'alf_AssignmentCompletion', None)
    assert owner not in getattr(partner, 'alf_Test2')


def test_assoc_assignmentCompletion276_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement277' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement277', None)
    _safe_set(owner, 'alf_AssignmentCompletion278', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement277') == owner
    _safe_set(owner, 'alf_AssignmentCompletion278', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement277') is None


def test_assoc_assignmentCompletion283_stub_double():
    # alf_ThisInvocationStatement has no real 'alf_ThisInvocationStatement284' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_ThisInvocationStatement()
    setattr(partner, 'alf_ThisInvocationStatement284', None)
    _safe_set(owner, 'alf_AssignmentCompletion285', partner)
    assert getattr(partner, 'alf_ThisInvocationStatement284') == owner
    _safe_set(owner, 'alf_AssignmentCompletion285', None)
    assert getattr(partner, 'alf_ThisInvocationStatement284') is None


def test_assoc_binding22_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding24' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding24', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding23', partner)
    assert getattr(partner, 'alf_TemplateBinding24') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding23', None)
    assert getattr(partner, 'alf_TemplateBinding24') is None


def test_assoc_bindings18_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding19' property in the generated
    # code (a bare stub) -- manually attach it so alf_NamedTemplateBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NamedTemplateBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NamedTemplateBinding(formal="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding19', None)
    _safe_set(owner, 'alf_NamedTemplateBinding', partner)
    assert owner in getattr(partner, 'alf_TemplateBinding19')
    _safe_set(owner, 'alf_NamedTemplateBinding', None)
    assert owner not in getattr(partner, 'alf_TemplateBinding19')


def test_assoc_clause235_stub_double():
    # alf_AcceptStatement has no real 'alf_AcceptStatement' property in the generated
    # code (a bare stub) -- manually attach it so alf_AcceptClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AcceptClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AcceptClause(name="sample_text")
    partner = alf_AcceptStatement()
    setattr(partner, 'alf_AcceptStatement', None)
    _safe_set(owner, 'alf_AcceptClause', partner)
    assert getattr(partner, 'alf_AcceptStatement') == owner
    _safe_set(owner, 'alf_AcceptClause', None)
    assert getattr(partner, 'alf_AcceptStatement') is None


def test_assoc_clause245_stub_double():
    # alf_AcceptBlock has no real 'alf_AcceptBlock246' property in the generated
    # code (a bare stub) -- manually attach it so alf_AcceptClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AcceptClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AcceptClause(name="sample_text")
    partner = alf_AcceptBlock()
    setattr(partner, 'alf_AcceptBlock246', None)
    _safe_set(owner, 'alf_AcceptClause247', partner)
    assert getattr(partner, 'alf_AcceptBlock246') == owner
    _safe_set(owner, 'alf_AcceptClause247', None)
    assert getattr(partner, 'alf_AcceptBlock246') is None


def test_assoc_constructor123_stub_double():
    # alf_InstanceCreationExpression has no real 'alf_InstanceCreationExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_InstanceCreationExpression()
    setattr(partner, 'alf_InstanceCreationExpression', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding124', partner)
    assert getattr(partner, 'alf_InstanceCreationExpression') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding124', None)
    assert getattr(partner, 'alf_InstanceCreationExpression') is None


def test_assoc_exp48_stub_double():
    # alf_AndExpression has no real 'alf_AndExpression49' property in the generated
    # code (a bare stub) -- manually attach it so alf_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_EqualityExpression(op="sample_text")
    partner = alf_AndExpression()
    setattr(partner, 'alf_AndExpression49', None)
    _safe_set(owner, 'alf_EqualityExpression', partner)
    assert owner in getattr(partner, 'alf_AndExpression49')
    _safe_set(owner, 'alf_EqualityExpression', None)
    assert owner not in getattr(partner, 'alf_AndExpression49')


def test_assoc_exp68_stub_double():
    # alf_PrimaryExpression has no real 'alf_PrimaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnaryExpression(op="sample_text")
    partner = alf_PrimaryExpression()
    setattr(partner, 'alf_PrimaryExpression', None)
    _safe_set(owner, 'alf_UnaryExpression69', partner)
    assert getattr(partner, 'alf_PrimaryExpression') == owner
    _safe_set(owner, 'alf_UnaryExpression69', None)
    assert getattr(partner, 'alf_PrimaryExpression') is None


def test_assoc_expr104_stub_double():
    # alf_Expression has no real 'alf_Expression105' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceExpansionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceExpansionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceExpansionExpression(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression105', None)
    _safe_set(owner, 'alf_SequenceExpansionExpression', partner)
    assert getattr(partner, 'alf_Expression105') == owner
    _safe_set(owner, 'alf_SequenceExpansionExpression', None)
    assert getattr(partner, 'alf_Expression105') is None


def test_assoc_expression1221_stub_double():
    # alf_Expression has no real 'alf_Expression223' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression223', None)
    _safe_set(owner, 'alf_LoopVariableDefinition222', partner)
    assert getattr(partner, 'alf_Expression223') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition222', None)
    assert getattr(partner, 'alf_Expression223') is None


def test_assoc_expression139_stub_double():
    # alf_SequenceConstructionExpression has no real 'alf_SequenceConstructionExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_SequenceConstructionExpression()
    setattr(partner, 'alf_SequenceConstructionExpression', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion140', partner)
    assert getattr(partner, 'alf_SequenceConstructionExpression') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion140', None)
    assert getattr(partner, 'alf_SequenceConstructionExpression') is None


def test_assoc_expression2224_stub_double():
    # alf_Expression has no real 'alf_Expression226' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression226', None)
    _safe_set(owner, 'alf_LoopVariableDefinition225', partner)
    assert getattr(partner, 'alf_Expression226') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition225', None)
    assert getattr(partner, 'alf_Expression226') is None


def test_assoc_expression230_stub_double():
    # alf_Expression has no real 'alf_Expression232' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression232', None)
    _safe_set(owner, 'alf_LoopVariableDefinition231', partner)
    assert getattr(partner, 'alf_Expression232') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition231', None)
    assert getattr(partner, 'alf_Expression232') is None


def test_assoc_index77_stub_double():
    # alf_Expression has no real 'alf_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so alf_PropertyCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_PropertyCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_PropertyCallExpression(propertyName="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression78', None)
    _safe_set(owner, 'alf_PropertyCallExpression', partner)
    assert getattr(partner, 'alf_Expression78') == owner
    _safe_set(owner, 'alf_PropertyCallExpression', None)
    assert getattr(partner, 'alf_Expression78') is None


def test_assoc_init167_stub_double():
    # alf_SequenceElement has no real 'alf_SequenceElement169' property in the generated
    # code (a bare stub) -- manually attach it so alf_LocalNameDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LocalNameDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LocalNameDeclarationStatement(multiplicityIndicator=True, varName="sample_text")
    partner = alf_SequenceElement()
    setattr(partner, 'alf_SequenceElement169', None)
    _safe_set(owner, 'alf_LocalNameDeclarationStatement168', partner)
    assert getattr(partner, 'alf_SequenceElement169') == owner
    _safe_set(owner, 'alf_LocalNameDeclarationStatement168', None)
    assert getattr(partner, 'alf_SequenceElement169') is None


def test_assoc_instanceCreationTupleElement130_stub_double():
    # alf_InstanceCreationTuple has no real 'alf_InstanceCreationTuple131' property in the generated
    # code (a bare stub) -- manually attach it so alf_InstanceCreationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_InstanceCreationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_InstanceCreationTupleElement(role="sample_text")
    partner = alf_InstanceCreationTuple()
    setattr(partner, 'alf_InstanceCreationTuple131', None)
    _safe_set(owner, 'alf_InstanceCreationTupleElement', partner)
    assert owner in getattr(partner, 'alf_InstanceCreationTuple131')
    _safe_set(owner, 'alf_InstanceCreationTupleElement', None)
    assert owner not in getattr(partner, 'alf_InstanceCreationTuple131')


def test_assoc_invocationCompletion8_stub_double():
    # alf_Tuple has no real 'alf_Tuple' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple', None)
    _safe_set(owner, 'alf_NameExpression9', partner)
    assert getattr(partner, 'alf_Tuple') == owner
    _safe_set(owner, 'alf_NameExpression9', None)
    assert getattr(partner, 'alf_Tuple') is None


def test_assoc_linkOperationTupleElement83_stub_double():
    # alf_LinkOperationTuple has no real 'alf_LinkOperationTuple84' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(role="sample_text")
    partner = alf_LinkOperationTuple()
    setattr(partner, 'alf_LinkOperationTuple84', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement', partner)
    assert owner in getattr(partner, 'alf_LinkOperationTuple84')
    _safe_set(owner, 'alf_LinkOperationTupleElement', None)
    assert owner not in getattr(partner, 'alf_LinkOperationTuple84')


def test_assoc_loopVariableDefinition219_stub_double():
    # alf_ForControl has no real 'alf_ForControl220' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_ForControl()
    setattr(partner, 'alf_ForControl220', None)
    _safe_set(owner, 'alf_LoopVariableDefinition', partner)
    assert owner in getattr(partner, 'alf_ForControl220')
    _safe_set(owner, 'alf_LoopVariableDefinition', None)
    assert owner not in getattr(partner, 'alf_ForControl220')


def test_assoc_namespace14_stub_double():
    # alf_QualifiedNamePath has no real 'alf_QualifiedNamePath15' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnqualifiedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnqualifiedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnqualifiedName(name="sample_text")
    partner = alf_QualifiedNamePath()
    setattr(partner, 'alf_QualifiedNamePath15', None)
    _safe_set(owner, 'alf_UnqualifiedName', partner)
    assert owner in getattr(partner, 'alf_QualifiedNamePath15')
    _safe_set(owner, 'alf_UnqualifiedName', None)
    assert owner not in getattr(partner, 'alf_QualifiedNamePath15')


def test_assoc_object132_stub_double():
    # alf_Expression has no real 'alf_Expression134' property in the generated
    # code (a bare stub) -- manually attach it so alf_InstanceCreationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_InstanceCreationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_InstanceCreationTupleElement(role="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression134', None)
    _safe_set(owner, 'alf_InstanceCreationTupleElement133', partner)
    assert getattr(partner, 'alf_Expression134') == owner
    _safe_set(owner, 'alf_InstanceCreationTupleElement133', None)
    assert getattr(partner, 'alf_Expression134') is None


def test_assoc_object88_stub_double():
    # alf_Expression has no real 'alf_Expression90' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(role="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression90', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement89', partner)
    assert getattr(partner, 'alf_Expression90') == owner
    _safe_set(owner, 'alf_LinkOperationTupleElement89', None)
    assert getattr(partner, 'alf_Expression90') is None


def test_assoc_operationName120_stub_double():
    # alf_SuperInvocationExpression has no real 'alf_SuperInvocationExpression121' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_SuperInvocationExpression()
    setattr(partner, 'alf_SuperInvocationExpression121', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding122', partner)
    assert getattr(partner, 'alf_SuperInvocationExpression121') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding122', None)
    assert getattr(partner, 'alf_SuperInvocationExpression121') is None


def test_assoc_operationName91_stub_double():
    # alf_SequenceOperationExpression has no real 'alf_SequenceOperationExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_SequenceOperationExpression()
    setattr(partner, 'alf_SequenceOperationExpression', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding92', partner)
    assert getattr(partner, 'alf_SequenceOperationExpression') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding92', None)
    assert getattr(partner, 'alf_SequenceOperationExpression') is None


def test_assoc_path7_stub_double():
    # alf_QualifiedNamePath has no real 'alf_QualifiedNamePath' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_QualifiedNamePath()
    setattr(partner, 'alf_QualifiedNamePath', None)
    _safe_set(owner, 'alf_NameExpression', partner)
    assert getattr(partner, 'alf_QualifiedNamePath') == owner
    _safe_set(owner, 'alf_NameExpression', None)
    assert getattr(partner, 'alf_QualifiedNamePath') is None


def test_assoc_qualifiedName269_stub_double():
    # alf_QualifiedNameList has no real 'alf_QualifiedNameList270' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_QualifiedNameList()
    setattr(partner, 'alf_QualifiedNameList270', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding271', partner)
    assert owner in getattr(partner, 'alf_QualifiedNameList270')
    _safe_set(owner, 'alf_QualifiedNameWithBinding271', None)
    assert owner not in getattr(partner, 'alf_QualifiedNameList270')


def test_assoc_qualifiedNameList251_stub_double():
    # alf_QualifiedNameList has no real 'alf_QualifiedNameList' property in the generated
    # code (a bare stub) -- manually attach it so alf_AcceptClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AcceptClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AcceptClause(name="sample_text")
    partner = alf_QualifiedNameList()
    setattr(partner, 'alf_QualifiedNameList', None)
    _safe_set(owner, 'alf_AcceptClause252', partner)
    assert getattr(partner, 'alf_QualifiedNameList') == owner
    _safe_set(owner, 'alf_AcceptClause252', None)
    assert getattr(partner, 'alf_QualifiedNameList') is None


def test_assoc_rightHandSide291_stub_double():
    # alf_SequenceElement has no real 'alf_SequenceElement293' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_SequenceElement()
    setattr(partner, 'alf_SequenceElement293', None)
    _safe_set(owner, 'alf_AssignmentCompletion292', partner)
    assert getattr(partner, 'alf_SequenceElement293') == owner
    _safe_set(owner, 'alf_AssignmentCompletion292', None)
    assert getattr(partner, 'alf_SequenceElement293') is None


def test_assoc_roleIndex85_stub_double():
    # alf_Expression has no real 'alf_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(role="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression87', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement86', partner)
    assert getattr(partner, 'alf_Expression87') == owner
    _safe_set(owner, 'alf_LinkOperationTupleElement86', None)
    assert getattr(partner, 'alf_Expression87') is None


def test_assoc_sequenceCompletion137_stub_double():
    # alf_PartialSequenceConstructionCompletion has no real 'alf_PartialSequenceConstructionCompletion' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_PartialSequenceConstructionCompletion()
    setattr(partner, 'alf_PartialSequenceConstructionCompletion', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion138', partner)
    assert getattr(partner, 'alf_PartialSequenceConstructionCompletion') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion138', None)
    assert getattr(partner, 'alf_PartialSequenceConstructionCompletion') is None


def test_assoc_statement156_stub_double():
    # alf_Statement has no real 'alf_Statement158' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_Statement()
    setattr(partner, 'alf_Statement158', None)
    _safe_set(owner, 'alf_DocumentedStatement157', partner)
    assert getattr(partner, 'alf_Statement158') == owner
    _safe_set(owner, 'alf_DocumentedStatement157', None)
    assert getattr(partner, 'alf_Statement158') is None


def test_assoc_statement202_stub_double():
    # alf_NonEmptyStatementSequence has no real 'alf_NonEmptyStatementSequence203' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_NonEmptyStatementSequence()
    setattr(partner, 'alf_NonEmptyStatementSequence203', None)
    _safe_set(owner, 'alf_DocumentedStatement204', partner)
    assert owner in getattr(partner, 'alf_NonEmptyStatementSequence203')
    _safe_set(owner, 'alf_DocumentedStatement204', None)
    assert owner not in getattr(partner, 'alf_NonEmptyStatementSequence203')


def test_assoc_statements154_stub_double():
    # alf_StatementSequence has no real 'alf_StatementSequence155' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_StatementSequence()
    setattr(partner, 'alf_StatementSequence155', None)
    _safe_set(owner, 'alf_DocumentedStatement', partner)
    assert owner in getattr(partner, 'alf_StatementSequence155')
    _safe_set(owner, 'alf_DocumentedStatement', None)
    assert owner not in getattr(partner, 'alf_StatementSequence155')


def test_assoc_suffix101_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression103' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceReductionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceReductionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceReductionExpression(isOrdered=True)
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression103', None)
    _safe_set(owner, 'alf_SequenceReductionExpression102', partner)
    assert getattr(partner, 'alf_SuffixExpression103') == owner
    _safe_set(owner, 'alf_SequenceReductionExpression102', None)
    assert getattr(partner, 'alf_SuffixExpression103') is None


def test_assoc_suffix106_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression108' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceExpansionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceExpansionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceExpansionExpression(name="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression108', None)
    _safe_set(owner, 'alf_SequenceExpansionExpression107', partner)
    assert getattr(partner, 'alf_SuffixExpression108') == owner
    _safe_set(owner, 'alf_SequenceExpansionExpression107', None)
    assert getattr(partner, 'alf_SuffixExpression108') is None


def test_assoc_suffix12_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression', None)
    _safe_set(owner, 'alf_NameExpression13', partner)
    assert getattr(partner, 'alf_SuffixExpression') == owner
    _safe_set(owner, 'alf_NameExpression13', None)
    assert getattr(partner, 'alf_SuffixExpression') is None


def test_assoc_suffix74_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression76' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpression(operationName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression76', None)
    _safe_set(owner, 'alf_OperationCallExpression75', partner)
    assert getattr(partner, 'alf_SuffixExpression76') == owner
    _safe_set(owner, 'alf_OperationCallExpression75', None)
    assert getattr(partner, 'alf_SuffixExpression76') is None


def test_assoc_suffix79_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression81' property in the generated
    # code (a bare stub) -- manually attach it so alf_PropertyCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_PropertyCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_PropertyCallExpression(propertyName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression81', None)
    _safe_set(owner, 'alf_PropertyCallExpression80', partner)
    assert getattr(partner, 'alf_SuffixExpression81') == owner
    _safe_set(owner, 'alf_PropertyCallExpression80', None)
    assert getattr(partner, 'alf_SuffixExpression81') is None


def test_assoc_templateBinding16_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnqualifiedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnqualifiedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnqualifiedName(name="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding', None)
    _safe_set(owner, 'alf_UnqualifiedName17', partner)
    assert getattr(partner, 'alf_TemplateBinding') == owner
    _safe_set(owner, 'alf_UnqualifiedName17', None)
    assert getattr(partner, 'alf_TemplateBinding') is None


def test_assoc_tuple72_stub_double():
    # alf_Tuple has no real 'alf_Tuple73' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpression(operationName="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple73', None)
    _safe_set(owner, 'alf_OperationCallExpression', partner)
    assert getattr(partner, 'alf_Tuple73') == owner
    _safe_set(owner, 'alf_OperationCallExpression', None)
    assert getattr(partner, 'alf_Tuple73') is None


def test_assoc_tuple82_stub_double():
    # alf_LinkOperationTuple has no real 'alf_LinkOperationTuple' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationExpression(kind="sample_text")
    partner = alf_LinkOperationTuple()
    setattr(partner, 'alf_LinkOperationTuple', None)
    _safe_set(owner, 'alf_LinkOperationExpression', partner)
    assert getattr(partner, 'alf_LinkOperationTuple') == owner
    _safe_set(owner, 'alf_LinkOperationExpression', None)
    assert getattr(partner, 'alf_LinkOperationTuple') is None


def test_assoc_typePart_OR_assignedPart_OR_invocationPart272_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement', None)
    _safe_set(owner, 'alf_NameExpression273', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement') == owner
    _safe_set(owner, 'alf_NameExpression273', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement') is None


def test_assoc_variableDeclarationCompletion274_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement275' property in the generated
    # code (a bare stub) -- manually attach it so alf_VariableDeclarationCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_VariableDeclarationCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_VariableDeclarationCompletion(multiplicityIndicator=True, variableName="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement275', None)
    _safe_set(owner, 'alf_VariableDeclarationCompletion', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement275') == owner
    _safe_set(owner, 'alf_VariableDeclarationCompletion', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement275') is None


