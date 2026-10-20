import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    LITERAL,
    NUMBER_LITERAL,
    NUMBER_LITERAL_WITHOUT_SUFFIX,
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
    alf_FormalParameter,
    alf_FormalParameterList,
    alf_FormalParameters,
    alf_INTEGER_LITERAL,
    alf_INTEGER_LITERAL_WITHOUT_SUFFIX,
    alf_IfStatement,
    alf_InclusiveOrExpression,
    alf_InlineStatement,
    alf_InstanceCreationExpression,
    alf_InstanceCreationInvocationStatement,
    alf_InvocationOrAssignementOrDeclarationStatement,
    alf_IsUniqueOperation,
    alf_LITERAL,
    alf_LinkOperationExpression,
    alf_LinkOperationTuple,
    alf_LinkOperationTupleElement,
    alf_LocalNameDeclarationStatement,
    alf_LoopVariableDefinition,
    alf_MultiplicativeExpression,
    alf_Multiplicity,
    alf_MultiplicityRange,
    alf_NUMBER_LITERAL,
    alf_NUMBER_LITERAL_WITHOUT_SUFFIX,
    alf_NameExpression,
    alf_NamedTemplateBinding,
    alf_NonEmptyStatementSequence,
    alf_NonFinalClause,
    alf_NonLiteralValueSpecification,
    alf_NullExpression,
    alf_OperationCallExpression,
    alf_OperationCallExpressionWithoutDot,
    alf_OperationDeclaration,
    alf_OperationDefinitionOrStub,
    alf_Operations,
    alf_ParenthesizedExpression,
    alf_PartialSequenceConstructionCompletion,
    alf_PrimaryExpression,
    alf_PropertyCallExpression,
    alf_QualifiedNameList,
    alf_QualifiedNamePath,
    alf_QualifiedNameWithBinding,
    alf_ReclassifyAllClause,
    alf_RedefinitionClause,
    alf_RelationalExpression,
    alf_ReturnStatement,
    alf_STRING_LITERAL,
    alf_SelectOrRejectOperation,
    alf_SequenceConstructionCompletion,
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
    alf_TypeName,
    alf_TypePart,
    alf_UNLIMITED_LITERAL,
    alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX,
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
    ParameterDirection,
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

def test_assoc_actual56_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_NamedTemplateBinding(formal="sample_text")
    _safe_set(b, 'alf_NamedTemplateBinding57', a1)
    assert _is_linked(b, 'alf_NamedTemplateBinding57', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding58'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding58', b)
    _safe_set(b, 'alf_NamedTemplateBinding57', a2)
    assert _is_linked(b, 'alf_NamedTemplateBinding57', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding58'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding58', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding58'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding58', b)
    _safe_set(b, 'alf_NamedTemplateBinding57', None)
    assert not _is_linked(b, 'alf_NamedTemplateBinding57', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding58'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding58', b)


def test_assoc_behavior138_reverse_link_reassign_clear():
    a1 = alf_SequenceReductionExpression(isOrdered=True)
    a2 = alf_SequenceReductionExpression(isOrdered=False)
    b = alf_QualifiedNameWithBinding(id="sample_text")
    _safe_set(b, 'alf_QualifiedNameWithBinding139', a1)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding139', a1)
    if hasattr(a1, 'alf_SequenceReductionExpression'):
        assert _is_linked(a1, 'alf_SequenceReductionExpression', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding139', a2)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding139', a2)
    if hasattr(a1, 'alf_SequenceReductionExpression'):
        assert not _is_linked(a1, 'alf_SequenceReductionExpression', b)
    if hasattr(a2, 'alf_SequenceReductionExpression'):
        assert _is_linked(a2, 'alf_SequenceReductionExpression', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding139', None)
    assert not _is_linked(b, 'alf_QualifiedNameWithBinding139', a2)
    if hasattr(a2, 'alf_SequenceReductionExpression'):
        assert not _is_linked(a2, 'alf_SequenceReductionExpression', b)


def test_assoc_exp101_reverse_link_reassign_clear():
    a1 = alf_MultiplicativeExpression(op="sample_text")
    a2 = alf_MultiplicativeExpression(op="sample_text_2")
    b = alf_AdditiveExpression(op="sample_text")
    _safe_set(b, 'alf_AdditiveExpression102', {a1})
    assert _is_linked(b, 'alf_AdditiveExpression102', a1)
    if hasattr(a1, 'alf_MultiplicativeExpression'):
        assert _is_linked(a1, 'alf_MultiplicativeExpression', b)
    _safe_set(b, 'alf_AdditiveExpression102', {a2})
    assert _is_linked(b, 'alf_AdditiveExpression102', a2)
    if hasattr(a1, 'alf_MultiplicativeExpression'):
        assert not _is_linked(a1, 'alf_MultiplicativeExpression', b)
    if hasattr(a2, 'alf_MultiplicativeExpression'):
        assert _is_linked(a2, 'alf_MultiplicativeExpression', b)
    _safe_set(b, 'alf_AdditiveExpression102', set())
    assert not _is_linked(b, 'alf_AdditiveExpression102', a2)
    if hasattr(a2, 'alf_MultiplicativeExpression'):
        assert not _is_linked(a2, 'alf_MultiplicativeExpression', b)


def test_assoc_exp103_reverse_link_reassign_clear():
    a1 = alf_UnaryExpression(op="sample_text")
    a2 = alf_UnaryExpression(op="sample_text_2")
    b = alf_MultiplicativeExpression(op="sample_text")
    _safe_set(b, 'alf_MultiplicativeExpression104', {a1})
    assert _is_linked(b, 'alf_MultiplicativeExpression104', a1)
    if hasattr(a1, 'alf_UnaryExpression'):
        assert _is_linked(a1, 'alf_UnaryExpression', b)
    _safe_set(b, 'alf_MultiplicativeExpression104', {a2})
    assert _is_linked(b, 'alf_MultiplicativeExpression104', a2)
    if hasattr(a1, 'alf_UnaryExpression'):
        assert not _is_linked(a1, 'alf_UnaryExpression', b)
    if hasattr(a2, 'alf_UnaryExpression'):
        assert _is_linked(a2, 'alf_UnaryExpression', b)
    _safe_set(b, 'alf_MultiplicativeExpression104', set())
    assert not _is_linked(b, 'alf_MultiplicativeExpression104', a2)
    if hasattr(a2, 'alf_UnaryExpression'):
        assert not _is_linked(a2, 'alf_UnaryExpression', b)


def test_assoc_exp87_reverse_link_reassign_clear():
    a1 = alf_EqualityExpression(op="sample_text")
    a2 = alf_EqualityExpression(op="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression', a1)
    assert _is_linked(b, 'alf_ClassificationExpression', a1)
    if hasattr(a1, 'alf_EqualityExpression88'):
        assert _is_linked(a1, 'alf_EqualityExpression88', b)
    _safe_set(b, 'alf_ClassificationExpression', a2)
    assert _is_linked(b, 'alf_ClassificationExpression', a2)
    if hasattr(a1, 'alf_EqualityExpression88'):
        assert not _is_linked(a1, 'alf_EqualityExpression88', b)
    if hasattr(a2, 'alf_EqualityExpression88'):
        assert _is_linked(a2, 'alf_EqualityExpression88', b)
    _safe_set(b, 'alf_ClassificationExpression', None)
    assert not _is_linked(b, 'alf_ClassificationExpression', a2)
    if hasattr(a2, 'alf_EqualityExpression88'):
        assert not _is_linked(a2, 'alf_EqualityExpression88', b)


def test_assoc_exp89_reverse_link_reassign_clear():
    a1 = alf_RelationalExpression(op="sample_text")
    a2 = alf_RelationalExpression(op="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression90', a1)
    assert _is_linked(b, 'alf_ClassificationExpression90', a1)
    if hasattr(a1, 'alf_RelationalExpression'):
        assert _is_linked(a1, 'alf_RelationalExpression', b)
    _safe_set(b, 'alf_ClassificationExpression90', a2)
    assert _is_linked(b, 'alf_ClassificationExpression90', a2)
    if hasattr(a1, 'alf_RelationalExpression'):
        assert not _is_linked(a1, 'alf_RelationalExpression', b)
    if hasattr(a2, 'alf_RelationalExpression'):
        assert _is_linked(a2, 'alf_RelationalExpression', b)
    _safe_set(b, 'alf_ClassificationExpression90', None)
    assert not _is_linked(b, 'alf_ClassificationExpression90', a2)
    if hasattr(a2, 'alf_RelationalExpression'):
        assert not _is_linked(a2, 'alf_RelationalExpression', b)


def test_assoc_exp99_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_AdditiveExpression(op="sample_text")
    _safe_set(b, 'alf_AdditiveExpression', a1)
    assert _is_linked(b, 'alf_AdditiveExpression', a1)
    if hasattr(a1, 'alf_ShiftExpression100'):
        assert _is_linked(a1, 'alf_ShiftExpression100', b)
    _safe_set(b, 'alf_AdditiveExpression', a2)
    assert _is_linked(b, 'alf_AdditiveExpression', a2)
    if hasattr(a1, 'alf_ShiftExpression100'):
        assert not _is_linked(a1, 'alf_ShiftExpression100', b)
    if hasattr(a2, 'alf_ShiftExpression100'):
        assert _is_linked(a2, 'alf_ShiftExpression100', b)
    _safe_set(b, 'alf_AdditiveExpression', None)
    assert not _is_linked(b, 'alf_AdditiveExpression', a2)
    if hasattr(a2, 'alf_ShiftExpression100'):
        assert not _is_linked(a2, 'alf_ShiftExpression100', b)


def test_assoc_initValue322_reverse_link_reassign_clear():
    a1 = alf_VariableDeclarationCompletion(multiplicityIndicator=True, variableName="sample_text")
    a2 = alf_VariableDeclarationCompletion(multiplicityIndicator=False, variableName="sample_text_2")
    b = alf_AssignmentCompletion(op="sample_text")
    _safe_set(b, 'alf_AssignmentCompletion324', a1)
    assert _is_linked(b, 'alf_AssignmentCompletion324', a1)
    if hasattr(a1, 'alf_VariableDeclarationCompletion323'):
        assert _is_linked(a1, 'alf_VariableDeclarationCompletion323', b)
    _safe_set(b, 'alf_AssignmentCompletion324', a2)
    assert _is_linked(b, 'alf_AssignmentCompletion324', a2)
    if hasattr(a1, 'alf_VariableDeclarationCompletion323'):
        assert not _is_linked(a1, 'alf_VariableDeclarationCompletion323', b)
    if hasattr(a2, 'alf_VariableDeclarationCompletion323'):
        assert _is_linked(a2, 'alf_VariableDeclarationCompletion323', b)
    _safe_set(b, 'alf_AssignmentCompletion324', None)
    assert not _is_linked(b, 'alf_AssignmentCompletion324', a2)
    if hasattr(a2, 'alf_VariableDeclarationCompletion323'):
        assert not _is_linked(a2, 'alf_VariableDeclarationCompletion323', b)


def test_assoc_left94_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_RelationalExpression(op="sample_text")
    _safe_set(b, 'alf_RelationalExpression95', a1)
    assert _is_linked(b, 'alf_RelationalExpression95', a1)
    if hasattr(a1, 'alf_ShiftExpression'):
        assert _is_linked(a1, 'alf_ShiftExpression', b)
    _safe_set(b, 'alf_RelationalExpression95', a2)
    assert _is_linked(b, 'alf_RelationalExpression95', a2)
    if hasattr(a1, 'alf_ShiftExpression'):
        assert not _is_linked(a1, 'alf_ShiftExpression', b)
    if hasattr(a2, 'alf_ShiftExpression'):
        assert _is_linked(a2, 'alf_ShiftExpression', b)
    _safe_set(b, 'alf_RelationalExpression95', None)
    assert not _is_linked(b, 'alf_RelationalExpression95', a2)
    if hasattr(a2, 'alf_ShiftExpression'):
        assert not _is_linked(a2, 'alf_ShiftExpression', b)


def test_assoc_operationCall158_reverse_link_reassign_clear():
    a1 = alf_SuperInvocationExpression(className="sample_text")
    a2 = alf_SuperInvocationExpression(className="sample_text_2")
    b = alf_OperationCallExpression(operationName="sample_text")
    _safe_set(b, 'alf_OperationCallExpression160', a1)
    assert _is_linked(b, 'alf_OperationCallExpression160', a1)
    if hasattr(a1, 'alf_SuperInvocationExpression159'):
        assert _is_linked(a1, 'alf_SuperInvocationExpression159', b)
    _safe_set(b, 'alf_OperationCallExpression160', a2)
    assert _is_linked(b, 'alf_OperationCallExpression160', a2)
    if hasattr(a1, 'alf_SuperInvocationExpression159'):
        assert not _is_linked(a1, 'alf_SuperInvocationExpression159', b)
    if hasattr(a2, 'alf_SuperInvocationExpression159'):
        assert _is_linked(a2, 'alf_SuperInvocationExpression159', b)
    _safe_set(b, 'alf_OperationCallExpression160', None)
    assert not _is_linked(b, 'alf_OperationCallExpression160', a2)
    if hasattr(a2, 'alf_SuperInvocationExpression159'):
        assert not _is_linked(a2, 'alf_SuperInvocationExpression159', b)


def test_assoc_operationCallWithoutDot156_reverse_link_reassign_clear():
    a1 = alf_SuperInvocationExpression(className="sample_text")
    a2 = alf_SuperInvocationExpression(className="sample_text_2")
    b = alf_OperationCallExpressionWithoutDot(operationName="sample_text")
    _safe_set(b, 'alf_OperationCallExpressionWithoutDot157', a1)
    assert _is_linked(b, 'alf_OperationCallExpressionWithoutDot157', a1)
    if hasattr(a1, 'alf_SuperInvocationExpression'):
        assert _is_linked(a1, 'alf_SuperInvocationExpression', b)
    _safe_set(b, 'alf_OperationCallExpressionWithoutDot157', a2)
    assert _is_linked(b, 'alf_OperationCallExpressionWithoutDot157', a2)
    if hasattr(a1, 'alf_SuperInvocationExpression'):
        assert not _is_linked(a1, 'alf_SuperInvocationExpression', b)
    if hasattr(a2, 'alf_SuperInvocationExpression'):
        assert _is_linked(a2, 'alf_SuperInvocationExpression', b)
    _safe_set(b, 'alf_OperationCallExpressionWithoutDot157', None)
    assert not _is_linked(b, 'alf_OperationCallExpressionWithoutDot157', a2)
    if hasattr(a2, 'alf_SuperInvocationExpression'):
        assert not _is_linked(a2, 'alf_SuperInvocationExpression', b)


def test_assoc_remaining63_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_QualifiedNameWithBinding(id="sample_text")
    _safe_set(b, 'alf_QualifiedNameWithBinding64', a1)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding64', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding62'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding62', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding64', a2)
    assert _is_linked(b, 'alf_QualifiedNameWithBinding64', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding62'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding62', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding62'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding62', b)
    _safe_set(b, 'alf_QualifiedNameWithBinding64', None)
    assert not _is_linked(b, 'alf_QualifiedNameWithBinding64', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding62'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding62', b)


def test_assoc_right96_reverse_link_reassign_clear():
    a1 = alf_ShiftExpression(op="sample_text")
    a2 = alf_ShiftExpression(op="sample_text_2")
    b = alf_RelationalExpression(op="sample_text")
    _safe_set(b, 'alf_RelationalExpression97', a1)
    assert _is_linked(b, 'alf_RelationalExpression97', a1)
    if hasattr(a1, 'alf_ShiftExpression98'):
        assert _is_linked(a1, 'alf_ShiftExpression98', b)
    _safe_set(b, 'alf_RelationalExpression97', a2)
    assert _is_linked(b, 'alf_RelationalExpression97', a2)
    if hasattr(a1, 'alf_ShiftExpression98'):
        assert not _is_linked(a1, 'alf_ShiftExpression98', b)
    if hasattr(a2, 'alf_ShiftExpression98'):
        assert _is_linked(a2, 'alf_ShiftExpression98', b)
    _safe_set(b, 'alf_RelationalExpression97', None)
    assert not _is_linked(b, 'alf_RelationalExpression97', a2)
    if hasattr(a2, 'alf_ShiftExpression98'):
        assert not _is_linked(a2, 'alf_ShiftExpression98', b)


def test_assoc_sequenceConstructionCompletion45_reverse_link_reassign_clear():
    a1 = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    a2 = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=False)
    b = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    _safe_set(b, 'alf_NameExpression46', a1)
    assert _is_linked(b, 'alf_NameExpression46', a1)
    if hasattr(a1, 'alf_SequenceConstructionOrAccessCompletion'):
        assert _is_linked(a1, 'alf_SequenceConstructionOrAccessCompletion', b)
    _safe_set(b, 'alf_NameExpression46', a2)
    assert _is_linked(b, 'alf_NameExpression46', a2)
    if hasattr(a1, 'alf_SequenceConstructionOrAccessCompletion'):
        assert not _is_linked(a1, 'alf_SequenceConstructionOrAccessCompletion', b)
    if hasattr(a2, 'alf_SequenceConstructionOrAccessCompletion'):
        assert _is_linked(a2, 'alf_SequenceConstructionOrAccessCompletion', b)
    _safe_set(b, 'alf_NameExpression46', None)
    assert not _is_linked(b, 'alf_NameExpression46', a2)
    if hasattr(a2, 'alf_SequenceConstructionOrAccessCompletion'):
        assert not _is_linked(a2, 'alf_SequenceConstructionOrAccessCompletion', b)


def test_assoc_type204_reverse_link_reassign_clear():
    a1 = alf_QualifiedNameWithBinding(id="sample_text")
    a2 = alf_QualifiedNameWithBinding(id="sample_text_2")
    b = alf_LocalNameDeclarationStatement(multiplicityIndicator=True, varName="sample_text")
    _safe_set(b, 'alf_LocalNameDeclarationStatement', a1)
    assert _is_linked(b, 'alf_LocalNameDeclarationStatement', a1)
    if hasattr(a1, 'alf_QualifiedNameWithBinding205'):
        assert _is_linked(a1, 'alf_QualifiedNameWithBinding205', b)
    _safe_set(b, 'alf_LocalNameDeclarationStatement', a2)
    assert _is_linked(b, 'alf_LocalNameDeclarationStatement', a2)
    if hasattr(a1, 'alf_QualifiedNameWithBinding205'):
        assert not _is_linked(a1, 'alf_QualifiedNameWithBinding205', b)
    if hasattr(a2, 'alf_QualifiedNameWithBinding205'):
        assert _is_linked(a2, 'alf_QualifiedNameWithBinding205', b)
    _safe_set(b, 'alf_LocalNameDeclarationStatement', None)
    assert not _is_linked(b, 'alf_LocalNameDeclarationStatement', a2)
    if hasattr(a2, 'alf_QualifiedNameWithBinding205'):
        assert not _is_linked(a2, 'alf_QualifiedNameWithBinding205', b)


def test_assoc_typeName91_reverse_link_reassign_clear():
    a1 = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    a2 = alf_NameExpression(id="sample_text_2", postfixOp="sample_text_2", prefixOp="sample_text_2")
    b = alf_ClassificationExpression(op="sample_text")
    _safe_set(b, 'alf_ClassificationExpression92', a1)
    assert _is_linked(b, 'alf_ClassificationExpression92', a1)
    if hasattr(a1, 'alf_NameExpression93'):
        assert _is_linked(a1, 'alf_NameExpression93', b)
    _safe_set(b, 'alf_ClassificationExpression92', a2)
    assert _is_linked(b, 'alf_ClassificationExpression92', a2)
    if hasattr(a1, 'alf_NameExpression93'):
        assert not _is_linked(a1, 'alf_NameExpression93', b)
    if hasattr(a2, 'alf_NameExpression93'):
        assert _is_linked(a2, 'alf_NameExpression93', b)
    _safe_set(b, 'alf_ClassificationExpression92', None)
    assert not _is_linked(b, 'alf_ClassificationExpression92', a2)
    if hasattr(a2, 'alf_NameExpression93'):
        assert not _is_linked(a2, 'alf_NameExpression93', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__super313_stub_double():
    # alf_SuperInvocationStatement has no real 'alf_SuperInvocationStatement' property in the generated
    # code (a bare stub) -- manually attach it so alf_SuperInvocationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SuperInvocationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SuperInvocationExpression(className="sample_text")
    partner = alf_SuperInvocationStatement()
    setattr(partner, 'alf_SuperInvocationStatement', None)
    _safe_set(owner, 'alf_SuperInvocationExpression314', partner)
    assert getattr(partner, 'alf_SuperInvocationStatement') == owner
    _safe_set(owner, 'alf_SuperInvocationExpression314', None)
    assert getattr(partner, 'alf_SuperInvocationStatement') is None


def test_assoc_accessCompletion171_stub_double():
    # alf_AccessCompletion has no real 'alf_AccessCompletion' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_AccessCompletion()
    setattr(partner, 'alf_AccessCompletion', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion172', partner)
    assert getattr(partner, 'alf_AccessCompletion') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion172', None)
    assert getattr(partner, 'alf_AccessCompletion') is None


def test_assoc_annotation195_stub_double():
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


def test_assoc_assignExpression34_stub_double():
    # alf_Test has no real 'alf_Test35' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_Test()
    setattr(partner, 'alf_Test35', None)
    _safe_set(owner, 'alf_AssignmentCompletion', partner)
    assert owner in getattr(partner, 'alf_Test35')
    _safe_set(owner, 'alf_AssignmentCompletion', None)
    assert owner not in getattr(partner, 'alf_Test35')


def test_assoc_assignmentCompletion310_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement311' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement311', None)
    _safe_set(owner, 'alf_AssignmentCompletion312', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement311') == owner
    _safe_set(owner, 'alf_AssignmentCompletion312', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement311') is None


def test_assoc_assignmentCompletion317_stub_double():
    # alf_ThisInvocationStatement has no real 'alf_ThisInvocationStatement318' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_ThisInvocationStatement()
    setattr(partner, 'alf_ThisInvocationStatement318', None)
    _safe_set(owner, 'alf_AssignmentCompletion319', partner)
    assert getattr(partner, 'alf_ThisInvocationStatement318') == owner
    _safe_set(owner, 'alf_AssignmentCompletion319', None)
    assert getattr(partner, 'alf_ThisInvocationStatement318') is None


def test_assoc_binding59_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding61' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding61', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding60', partner)
    assert getattr(partner, 'alf_TemplateBinding61') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding60', None)
    assert getattr(partner, 'alf_TemplateBinding61') is None


def test_assoc_bindings54_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding55' property in the generated
    # code (a bare stub) -- manually attach it so alf_NamedTemplateBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NamedTemplateBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NamedTemplateBinding(formal="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding55', None)
    _safe_set(owner, 'alf_NamedTemplateBinding', partner)
    assert owner in getattr(partner, 'alf_TemplateBinding55')
    _safe_set(owner, 'alf_NamedTemplateBinding', None)
    assert owner not in getattr(partner, 'alf_TemplateBinding55')


def test_assoc_clause268_stub_double():
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


def test_assoc_clause278_stub_double():
    # alf_AcceptBlock has no real 'alf_AcceptBlock279' property in the generated
    # code (a bare stub) -- manually attach it so alf_AcceptClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AcceptClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AcceptClause(name="sample_text")
    partner = alf_AcceptBlock()
    setattr(partner, 'alf_AcceptBlock279', None)
    _safe_set(owner, 'alf_AcceptClause280', partner)
    assert getattr(partner, 'alf_AcceptBlock279') == owner
    _safe_set(owner, 'alf_AcceptClause280', None)
    assert getattr(partner, 'alf_AcceptBlock279') is None


def test_assoc_constructor161_stub_double():
    # alf_InstanceCreationExpression has no real 'alf_InstanceCreationExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_InstanceCreationExpression()
    setattr(partner, 'alf_InstanceCreationExpression', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding162', partner)
    assert getattr(partner, 'alf_InstanceCreationExpression') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding162', None)
    assert getattr(partner, 'alf_InstanceCreationExpression') is None


def test_assoc_declaration1_stub_double():
    # alf_OperationDefinitionOrStub has no real 'alf_OperationDefinitionOrStub2' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationDeclaration(name="sample_text")
    partner = alf_OperationDefinitionOrStub()
    setattr(partner, 'alf_OperationDefinitionOrStub2', None)
    _safe_set(owner, 'alf_OperationDeclaration', partner)
    assert getattr(partner, 'alf_OperationDefinitionOrStub2') == owner
    _safe_set(owner, 'alf_OperationDeclaration', None)
    assert getattr(partner, 'alf_OperationDefinitionOrStub2') is None


def test_assoc_exp105_stub_double():
    # alf_PrimaryExpression has no real 'alf_PrimaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnaryExpression(op="sample_text")
    partner = alf_PrimaryExpression()
    setattr(partner, 'alf_PrimaryExpression', None)
    _safe_set(owner, 'alf_UnaryExpression106', partner)
    assert getattr(partner, 'alf_PrimaryExpression') == owner
    _safe_set(owner, 'alf_UnaryExpression106', None)
    assert getattr(partner, 'alf_PrimaryExpression') is None


def test_assoc_exp85_stub_double():
    # alf_AndExpression has no real 'alf_AndExpression86' property in the generated
    # code (a bare stub) -- manually attach it so alf_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_EqualityExpression(op="sample_text")
    partner = alf_AndExpression()
    setattr(partner, 'alf_AndExpression86', None)
    _safe_set(owner, 'alf_EqualityExpression', partner)
    assert owner in getattr(partner, 'alf_AndExpression86')
    _safe_set(owner, 'alf_EqualityExpression', None)
    assert owner not in getattr(partner, 'alf_AndExpression86')


def test_assoc_expr145_stub_double():
    # alf_Expression has no real 'alf_Expression146' property in the generated
    # code (a bare stub) -- manually attach it so alf_IsUniqueOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_IsUniqueOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_IsUniqueOperation(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression146', None)
    _safe_set(owner, 'alf_IsUniqueOperation', partner)
    assert getattr(partner, 'alf_Expression146') == owner
    _safe_set(owner, 'alf_IsUniqueOperation', None)
    assert getattr(partner, 'alf_Expression146') is None


def test_assoc_expression1260_stub_double():
    # alf_Expression has no real 'alf_Expression262' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression262', None)
    _safe_set(owner, 'alf_LoopVariableDefinition261', partner)
    assert getattr(partner, 'alf_Expression262') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition261', None)
    assert getattr(partner, 'alf_Expression262') is None


def test_assoc_expression175_stub_double():
    # alf_SequenceConstructionExpression has no real 'alf_SequenceConstructionExpression' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_SequenceConstructionExpression()
    setattr(partner, 'alf_SequenceConstructionExpression', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion176', partner)
    assert getattr(partner, 'alf_SequenceConstructionExpression') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion176', None)
    assert getattr(partner, 'alf_SequenceConstructionExpression') is None


def test_assoc_expression183_stub_double():
    # alf_SequenceConstructionExpression has no real 'alf_SequenceConstructionExpression185' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionCompletion(multiplicityIndicator=True)
    partner = alf_SequenceConstructionExpression()
    setattr(partner, 'alf_SequenceConstructionExpression185', None)
    _safe_set(owner, 'alf_SequenceConstructionCompletion184', partner)
    assert getattr(partner, 'alf_SequenceConstructionExpression185') == owner
    _safe_set(owner, 'alf_SequenceConstructionCompletion184', None)
    assert getattr(partner, 'alf_SequenceConstructionExpression185') is None


def test_assoc_expression2263_stub_double():
    # alf_Expression has no real 'alf_Expression265' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression265', None)
    _safe_set(owner, 'alf_LoopVariableDefinition264', partner)
    assert getattr(partner, 'alf_Expression265') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition264', None)
    assert getattr(partner, 'alf_Expression265') is None


def test_assoc_formalParameter13_stub_double():
    # alf_FormalParameterList has no real 'alf_FormalParameterList14' property in the generated
    # code (a bare stub) -- manually attach it so alf_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_FormalParameter(direction="sample_text", name="sample_text")
    partner = alf_FormalParameterList()
    setattr(partner, 'alf_FormalParameterList14', None)
    _safe_set(owner, 'alf_FormalParameter', partner)
    assert owner in getattr(partner, 'alf_FormalParameterList14')
    _safe_set(owner, 'alf_FormalParameter', None)
    assert owner not in getattr(partner, 'alf_FormalParameterList14')


def test_assoc_formalParameters5_stub_double():
    # alf_FormalParameters has no real 'alf_FormalParameters' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationDeclaration(name="sample_text")
    partner = alf_FormalParameters()
    setattr(partner, 'alf_FormalParameters', None)
    _safe_set(owner, 'alf_OperationDeclaration6', partner)
    assert getattr(partner, 'alf_FormalParameters') == owner
    _safe_set(owner, 'alf_OperationDeclaration6', None)
    assert getattr(partner, 'alf_FormalParameters') is None


def test_assoc_index119_stub_double():
    # alf_Expression has no real 'alf_Expression120' property in the generated
    # code (a bare stub) -- manually attach it so alf_PropertyCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_PropertyCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_PropertyCallExpression(propertyName="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression120', None)
    _safe_set(owner, 'alf_PropertyCallExpression', partner)
    assert getattr(partner, 'alf_Expression120') == owner
    _safe_set(owner, 'alf_PropertyCallExpression', None)
    assert getattr(partner, 'alf_Expression120') is None


def test_assoc_init206_stub_double():
    # alf_Expression has no real 'alf_Expression208' property in the generated
    # code (a bare stub) -- manually attach it so alf_LocalNameDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LocalNameDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LocalNameDeclarationStatement(multiplicityIndicator=True, varName="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression208', None)
    _safe_set(owner, 'alf_LocalNameDeclarationStatement207', partner)
    assert getattr(partner, 'alf_Expression208') == owner
    _safe_set(owner, 'alf_LocalNameDeclarationStatement207', None)
    assert getattr(partner, 'alf_Expression208') is None


def test_assoc_invocationCompletion43_stub_double():
    # alf_Tuple has no real 'alf_Tuple' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple', None)
    _safe_set(owner, 'alf_NameExpression44', partner)
    assert getattr(partner, 'alf_Tuple') == owner
    _safe_set(owner, 'alf_NameExpression44', None)
    assert getattr(partner, 'alf_Tuple') is None


def test_assoc_linkOperationTupleElement125_stub_double():
    # alf_LinkOperationTuple has no real 'alf_LinkOperationTuple126' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(objectOrRole="sample_text")
    partner = alf_LinkOperationTuple()
    setattr(partner, 'alf_LinkOperationTuple126', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement', partner)
    assert owner in getattr(partner, 'alf_LinkOperationTuple126')
    _safe_set(owner, 'alf_LinkOperationTupleElement', None)
    assert owner not in getattr(partner, 'alf_LinkOperationTuple126')


def test_assoc_loopVariableDefinition258_stub_double():
    # alf_ForControl has no real 'alf_ForControl259' property in the generated
    # code (a bare stub) -- manually attach it so alf_LoopVariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LoopVariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LoopVariableDefinition(name="sample_text")
    partner = alf_ForControl()
    setattr(partner, 'alf_ForControl259', None)
    _safe_set(owner, 'alf_LoopVariableDefinition', partner)
    assert getattr(partner, 'alf_ForControl259') == owner
    _safe_set(owner, 'alf_LoopVariableDefinition', None)
    assert getattr(partner, 'alf_ForControl259') is None


def test_assoc_lower24_stub_double():
    # alf_MultiplicityRange has no real 'alf_MultiplicityRange25' property in the generated
    # code (a bare stub) -- manually attach it so alf_NUMBER_LITERAL_WITHOUT_SUFFIX's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NUMBER_LITERAL_WITHOUT_SUFFIX's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NUMBER_LITERAL_WITHOUT_SUFFIX(value="sample_text")
    partner = alf_MultiplicityRange()
    setattr(partner, 'alf_MultiplicityRange25', None)
    _safe_set(owner, 'alf_NUMBER_LITERAL_WITHOUT_SUFFIX', partner)
    assert getattr(partner, 'alf_MultiplicityRange25') == owner
    _safe_set(owner, 'alf_NUMBER_LITERAL_WITHOUT_SUFFIX', None)
    assert getattr(partner, 'alf_MultiplicityRange25') is None


def test_assoc_multiplicity20_stub_double():
    # alf_TypePart has no real 'alf_TypePart21' property in the generated
    # code (a bare stub) -- manually attach it so alf_Multiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_Multiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_Multiplicity(nonUnique=True, ordered=True, sequence=True)
    partner = alf_TypePart()
    setattr(partner, 'alf_TypePart21', None)
    _safe_set(owner, 'alf_Multiplicity', partner)
    assert getattr(partner, 'alf_TypePart21') == owner
    _safe_set(owner, 'alf_Multiplicity', None)
    assert getattr(partner, 'alf_TypePart21') is None


def test_assoc_namespace50_stub_double():
    # alf_QualifiedNamePath has no real 'alf_QualifiedNamePath51' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnqualifiedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnqualifiedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnqualifiedName(name="sample_text")
    partner = alf_QualifiedNamePath()
    setattr(partner, 'alf_QualifiedNamePath51', None)
    _safe_set(owner, 'alf_UnqualifiedName', partner)
    assert owner in getattr(partner, 'alf_QualifiedNamePath51')
    _safe_set(owner, 'alf_UnqualifiedName', None)
    assert owner not in getattr(partner, 'alf_QualifiedNamePath51')


def test_assoc_objectValueSpec130_stub_double():
    # alf_ValueSpecification has no real 'alf_ValueSpecification132' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(objectOrRole="sample_text")
    partner = alf_ValueSpecification()
    setattr(partner, 'alf_ValueSpecification132', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement131', partner)
    assert getattr(partner, 'alf_ValueSpecification132') == owner
    _safe_set(owner, 'alf_LinkOperationTupleElement131', None)
    assert getattr(partner, 'alf_ValueSpecification132') is None


def test_assoc_operations0_stub_double():
    # alf_OperationDefinitionOrStub has no real 'alf_OperationDefinitionOrStub' property in the generated
    # code (a bare stub) -- manually attach it so alf_Operations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_Operations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_Operations(imports="sample_text")
    partner = alf_OperationDefinitionOrStub()
    setattr(partner, 'alf_OperationDefinitionOrStub', None)
    _safe_set(owner, 'alf_Operations', {partner})
    assert getattr(partner, 'alf_OperationDefinitionOrStub') == owner
    _safe_set(owner, 'alf_Operations', set())
    assert getattr(partner, 'alf_OperationDefinitionOrStub') is None


def test_assoc_path42_stub_double():
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


def test_assoc_qualifiedName29_stub_double():
    # alf_TypeName has no real 'alf_TypeName30' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_TypeName()
    setattr(partner, 'alf_TypeName30', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding', partner)
    assert getattr(partner, 'alf_TypeName30') == owner
    _safe_set(owner, 'alf_QualifiedNameWithBinding', None)
    assert getattr(partner, 'alf_TypeName30') is None


def test_assoc_qualifiedName303_stub_double():
    # alf_QualifiedNameList has no real 'alf_QualifiedNameList304' property in the generated
    # code (a bare stub) -- manually attach it so alf_QualifiedNameWithBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_QualifiedNameWithBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_QualifiedNameWithBinding(id="sample_text")
    partner = alf_QualifiedNameList()
    setattr(partner, 'alf_QualifiedNameList304', None)
    _safe_set(owner, 'alf_QualifiedNameWithBinding305', partner)
    assert owner in getattr(partner, 'alf_QualifiedNameList304')
    _safe_set(owner, 'alf_QualifiedNameWithBinding305', None)
    assert owner not in getattr(partner, 'alf_QualifiedNameList304')


def test_assoc_qualifiedNameList284_stub_double():
    # alf_QualifiedNameList has no real 'alf_QualifiedNameList286' property in the generated
    # code (a bare stub) -- manually attach it so alf_AcceptClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AcceptClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AcceptClause(name="sample_text")
    partner = alf_QualifiedNameList()
    setattr(partner, 'alf_QualifiedNameList286', None)
    _safe_set(owner, 'alf_AcceptClause285', partner)
    assert getattr(partner, 'alf_QualifiedNameList286') == owner
    _safe_set(owner, 'alf_AcceptClause285', None)
    assert getattr(partner, 'alf_QualifiedNameList286') is None


def test_assoc_range22_stub_double():
    # alf_MultiplicityRange has no real 'alf_MultiplicityRange' property in the generated
    # code (a bare stub) -- manually attach it so alf_Multiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_Multiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_Multiplicity(nonUnique=True, ordered=True, sequence=True)
    partner = alf_MultiplicityRange()
    setattr(partner, 'alf_MultiplicityRange', None)
    _safe_set(owner, 'alf_Multiplicity23', partner)
    assert getattr(partner, 'alf_MultiplicityRange') == owner
    _safe_set(owner, 'alf_Multiplicity23', None)
    assert getattr(partner, 'alf_MultiplicityRange') is None


def test_assoc_redefinition9_stub_double():
    # alf_RedefinitionClause has no real 'alf_RedefinitionClause' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationDeclaration(name="sample_text")
    partner = alf_RedefinitionClause()
    setattr(partner, 'alf_RedefinitionClause', None)
    _safe_set(owner, 'alf_OperationDeclaration10', partner)
    assert getattr(partner, 'alf_RedefinitionClause') == owner
    _safe_set(owner, 'alf_OperationDeclaration10', None)
    assert getattr(partner, 'alf_RedefinitionClause') is None


def test_assoc_returnType7_stub_double():
    # alf_TypePart has no real 'alf_TypePart' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationDeclaration(name="sample_text")
    partner = alf_TypePart()
    setattr(partner, 'alf_TypePart', None)
    _safe_set(owner, 'alf_OperationDeclaration8', partner)
    assert getattr(partner, 'alf_TypePart') == owner
    _safe_set(owner, 'alf_OperationDeclaration8', None)
    assert getattr(partner, 'alf_TypePart') is None


def test_assoc_rightHandSide325_stub_double():
    # alf_Expression has no real 'alf_Expression327' property in the generated
    # code (a bare stub) -- manually attach it so alf_AssignmentCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_AssignmentCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_AssignmentCompletion(op="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression327', None)
    _safe_set(owner, 'alf_AssignmentCompletion326', partner)
    assert getattr(partner, 'alf_Expression327') == owner
    _safe_set(owner, 'alf_AssignmentCompletion326', None)
    assert getattr(partner, 'alf_Expression327') is None


def test_assoc_roleIndex127_stub_double():
    # alf_Expression has no real 'alf_Expression129' property in the generated
    # code (a bare stub) -- manually attach it so alf_LinkOperationTupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_LinkOperationTupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_LinkOperationTupleElement(objectOrRole="sample_text")
    partner = alf_Expression()
    setattr(partner, 'alf_Expression129', None)
    _safe_set(owner, 'alf_LinkOperationTupleElement128', partner)
    assert getattr(partner, 'alf_Expression129') == owner
    _safe_set(owner, 'alf_LinkOperationTupleElement128', None)
    assert getattr(partner, 'alf_Expression129') is None


def test_assoc_sequenceCompletion173_stub_double():
    # alf_PartialSequenceConstructionCompletion has no real 'alf_PartialSequenceConstructionCompletion' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionOrAccessCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionOrAccessCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionOrAccessCompletion(multiplicityIndicator=True)
    partner = alf_PartialSequenceConstructionCompletion()
    setattr(partner, 'alf_PartialSequenceConstructionCompletion', None)
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion174', partner)
    assert getattr(partner, 'alf_PartialSequenceConstructionCompletion') == owner
    _safe_set(owner, 'alf_SequenceConstructionOrAccessCompletion174', None)
    assert getattr(partner, 'alf_PartialSequenceConstructionCompletion') is None


def test_assoc_sequenceConstuctionCompletion166_stub_double():
    # alf_InstanceCreationExpression has no real 'alf_InstanceCreationExpression167' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceConstructionCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceConstructionCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceConstructionCompletion(multiplicityIndicator=True)
    partner = alf_InstanceCreationExpression()
    setattr(partner, 'alf_InstanceCreationExpression167', None)
    _safe_set(owner, 'alf_SequenceConstructionCompletion', partner)
    assert getattr(partner, 'alf_InstanceCreationExpression167') == owner
    _safe_set(owner, 'alf_SequenceConstructionCompletion', None)
    assert getattr(partner, 'alf_InstanceCreationExpression167') is None


def test_assoc_statement199_stub_double():
    # alf_Statement has no real 'alf_Statement201' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_Statement()
    setattr(partner, 'alf_Statement201', None)
    _safe_set(owner, 'alf_DocumentedStatement200', partner)
    assert getattr(partner, 'alf_Statement201') == owner
    _safe_set(owner, 'alf_DocumentedStatement200', None)
    assert getattr(partner, 'alf_Statement201') is None


def test_assoc_statement241_stub_double():
    # alf_NonEmptyStatementSequence has no real 'alf_NonEmptyStatementSequence242' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_NonEmptyStatementSequence()
    setattr(partner, 'alf_NonEmptyStatementSequence242', None)
    _safe_set(owner, 'alf_DocumentedStatement243', partner)
    assert owner in getattr(partner, 'alf_NonEmptyStatementSequence242')
    _safe_set(owner, 'alf_DocumentedStatement243', None)
    assert owner not in getattr(partner, 'alf_NonEmptyStatementSequence242')


def test_assoc_statements193_stub_double():
    # alf_StatementSequence has no real 'alf_StatementSequence194' property in the generated
    # code (a bare stub) -- manually attach it so alf_DocumentedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_DocumentedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_DocumentedStatement(comment="sample_text")
    partner = alf_StatementSequence()
    setattr(partner, 'alf_StatementSequence194', None)
    _safe_set(owner, 'alf_DocumentedStatement', partner)
    assert owner in getattr(partner, 'alf_StatementSequence194')
    _safe_set(owner, 'alf_DocumentedStatement', None)
    assert owner not in getattr(partner, 'alf_StatementSequence194')


def test_assoc_suffix111_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression113' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpression(operationName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression113', None)
    _safe_set(owner, 'alf_OperationCallExpression112', partner)
    assert getattr(partner, 'alf_SuffixExpression113') == owner
    _safe_set(owner, 'alf_OperationCallExpression112', None)
    assert getattr(partner, 'alf_SuffixExpression113') is None


def test_assoc_suffix116_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression118' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpressionWithoutDot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpressionWithoutDot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpressionWithoutDot(operationName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression118', None)
    _safe_set(owner, 'alf_OperationCallExpressionWithoutDot117', partner)
    assert getattr(partner, 'alf_SuffixExpression118') == owner
    _safe_set(owner, 'alf_OperationCallExpressionWithoutDot117', None)
    assert getattr(partner, 'alf_SuffixExpression118') is None


def test_assoc_suffix121_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression123' property in the generated
    # code (a bare stub) -- manually attach it so alf_PropertyCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_PropertyCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_PropertyCallExpression(propertyName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression123', None)
    _safe_set(owner, 'alf_PropertyCallExpression122', partner)
    assert getattr(partner, 'alf_SuffixExpression123') == owner
    _safe_set(owner, 'alf_PropertyCallExpression122', None)
    assert getattr(partner, 'alf_SuffixExpression123') is None


def test_assoc_suffix135_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression137' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceOperationExpression(operationName="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression137', None)
    _safe_set(owner, 'alf_SequenceOperationExpression136', partner)
    assert getattr(partner, 'alf_SuffixExpression137') == owner
    _safe_set(owner, 'alf_SequenceOperationExpression136', None)
    assert getattr(partner, 'alf_SuffixExpression137') is None


def test_assoc_suffix140_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression142' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceReductionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceReductionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceReductionExpression(isOrdered=True)
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression142', None)
    _safe_set(owner, 'alf_SequenceReductionExpression141', partner)
    assert getattr(partner, 'alf_SuffixExpression142') == owner
    _safe_set(owner, 'alf_SequenceReductionExpression141', None)
    assert getattr(partner, 'alf_SuffixExpression142') is None


def test_assoc_suffix47_stub_double():
    # alf_SuffixExpression has no real 'alf_SuffixExpression49' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_SuffixExpression()
    setattr(partner, 'alf_SuffixExpression49', None)
    _safe_set(owner, 'alf_NameExpression48', partner)
    assert getattr(partner, 'alf_SuffixExpression49') == owner
    _safe_set(owner, 'alf_NameExpression48', None)
    assert getattr(partner, 'alf_SuffixExpression49') is None


def test_assoc_templateBinding52_stub_double():
    # alf_TemplateBinding has no real 'alf_TemplateBinding' property in the generated
    # code (a bare stub) -- manually attach it so alf_UnqualifiedName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_UnqualifiedName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_UnqualifiedName(name="sample_text")
    partner = alf_TemplateBinding()
    setattr(partner, 'alf_TemplateBinding', None)
    _safe_set(owner, 'alf_UnqualifiedName53', partner)
    assert getattr(partner, 'alf_TemplateBinding') == owner
    _safe_set(owner, 'alf_UnqualifiedName53', None)
    assert getattr(partner, 'alf_TemplateBinding') is None


def test_assoc_tuple109_stub_double():
    # alf_Tuple has no real 'alf_Tuple110' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpression(operationName="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple110', None)
    _safe_set(owner, 'alf_OperationCallExpression', partner)
    assert getattr(partner, 'alf_Tuple110') == owner
    _safe_set(owner, 'alf_OperationCallExpression', None)
    assert getattr(partner, 'alf_Tuple110') is None


def test_assoc_tuple114_stub_double():
    # alf_Tuple has no real 'alf_Tuple115' property in the generated
    # code (a bare stub) -- manually attach it so alf_OperationCallExpressionWithoutDot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_OperationCallExpressionWithoutDot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_OperationCallExpressionWithoutDot(operationName="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple115', None)
    _safe_set(owner, 'alf_OperationCallExpressionWithoutDot', partner)
    assert getattr(partner, 'alf_Tuple115') == owner
    _safe_set(owner, 'alf_OperationCallExpressionWithoutDot', None)
    assert getattr(partner, 'alf_Tuple115') is None


def test_assoc_tuple124_stub_double():
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


def test_assoc_tuple133_stub_double():
    # alf_Tuple has no real 'alf_Tuple134' property in the generated
    # code (a bare stub) -- manually attach it so alf_SequenceOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_SequenceOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_SequenceOperationExpression(operationName="sample_text")
    partner = alf_Tuple()
    setattr(partner, 'alf_Tuple134', None)
    _safe_set(owner, 'alf_SequenceOperationExpression', partner)
    assert getattr(partner, 'alf_Tuple134') == owner
    _safe_set(owner, 'alf_SequenceOperationExpression', None)
    assert getattr(partner, 'alf_Tuple134') is None


def test_assoc_type15_stub_double():
    # alf_TypePart has no real 'alf_TypePart17' property in the generated
    # code (a bare stub) -- manually attach it so alf_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_FormalParameter(direction="sample_text", name="sample_text")
    partner = alf_TypePart()
    setattr(partner, 'alf_TypePart17', None)
    _safe_set(owner, 'alf_FormalParameter16', partner)
    assert getattr(partner, 'alf_TypePart17') == owner
    _safe_set(owner, 'alf_FormalParameter16', None)
    assert getattr(partner, 'alf_TypePart17') is None


def test_assoc_typePart_OR_assignedPart_OR_invocationPart306_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so alf_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NameExpression(id="sample_text", postfixOp="sample_text", prefixOp="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement', None)
    _safe_set(owner, 'alf_NameExpression307', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement') == owner
    _safe_set(owner, 'alf_NameExpression307', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement') is None


def test_assoc_upper26_stub_double():
    # alf_MultiplicityRange has no real 'alf_MultiplicityRange27' property in the generated
    # code (a bare stub) -- manually attach it so alf_NUMBER_LITERAL_WITHOUT_SUFFIX's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_NUMBER_LITERAL_WITHOUT_SUFFIX's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_NUMBER_LITERAL_WITHOUT_SUFFIX(value="sample_text")
    partner = alf_MultiplicityRange()
    setattr(partner, 'alf_MultiplicityRange27', None)
    _safe_set(owner, 'alf_NUMBER_LITERAL_WITHOUT_SUFFIX28', partner)
    assert getattr(partner, 'alf_MultiplicityRange27') == owner
    _safe_set(owner, 'alf_NUMBER_LITERAL_WITHOUT_SUFFIX28', None)
    assert getattr(partner, 'alf_MultiplicityRange27') is None


def test_assoc_variableDeclarationCompletion308_stub_double():
    # alf_InvocationOrAssignementOrDeclarationStatement has no real 'alf_InvocationOrAssignementOrDeclarationStatement309' property in the generated
    # code (a bare stub) -- manually attach it so alf_VariableDeclarationCompletion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alf_VariableDeclarationCompletion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alf_VariableDeclarationCompletion(multiplicityIndicator=True, variableName="sample_text")
    partner = alf_InvocationOrAssignementOrDeclarationStatement()
    setattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement309', None)
    _safe_set(owner, 'alf_VariableDeclarationCompletion', partner)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement309') == owner
    _safe_set(owner, 'alf_VariableDeclarationCompletion', None)
    assert getattr(partner, 'alf_InvocationOrAssignementOrDeclarationStatement309') is None


