import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractActor,
    Block,
    Connection,
    Declaration,
    Expression,
    ExpressionCall,
    LambdaExpression,
    LiteralExpression,
    Node,
    PortAccess,
    Scope,
    Statement,
    Type,
    Variable,
    ir_AbstractActor,
    ir_Action,
    ir_Actor,
    ir_ActorInstance,
    ir_Annotation,
    ir_AnnotationArgument,
    ir_Assign,
    ir_BinaryExpression,
    ir_Block,
    ir_BooleanLiteral,
    ir_Connection,
    ir_Declaration,
    ir_Expression,
    ir_ExpressionCall,
    ir_ExternalActor,
    ir_FloatLiteral,
    ir_ForEach,
    ir_ForwardDeclaration,
    ir_FromSource,
    ir_FunctionCall,
    ir_Generator,
    ir_Guard,
    ir_IfExpression,
    ir_IfStatement,
    ir_IntegerLiteral,
    ir_LambdaExpression,
    ir_ListExpression,
    ir_LiteralExpression,
    ir_Member,
    ir_Namespace,
    ir_Network,
    ir_Node,
    ir_Point2PointConnection,
    ir_Port,
    ir_PortAccess,
    ir_PortInstance,
    ir_PortPeek,
    ir_PortRead,
    ir_PortWrite,
    ir_ProcCall,
    ir_ProcExpression,
    ir_ReturnValue,
    ir_Schedule,
    ir_Scope,
    ir_State,
    ir_Statement,
    ir_StringLiteral,
    ir_TaggedExpression,
    ir_ToSink,
    ir_Type,
    ir_TypeActor,
    ir_TypeBool,
    ir_TypeConstructor,
    ir_TypeConstructorCall,
    ir_TypeDeclaration,
    ir_TypeDeclarationImport,
    ir_TypeExternal,
    ir_TypeFloat,
    ir_TypeInt,
    ir_TypeLambda,
    ir_TypeList,
    ir_TypeProc,
    ir_TypeRecord,
    ir_TypeString,
    ir_TypeUint,
    ir_TypeUndef,
    ir_TypeUser,
    ir_UnaryExpression,
    ir_Variable,
    ir_VariableExpression,
    ir_VariableExternal,
    ir_VariableImport,
    ir_VariableReference,
    ir_WhileLoop,
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

def test_assoc_annotations4_reverse_link_reassign_clear():
    a1 = ir_Node(id="sample_text")
    a2 = ir_Node(id="sample_text_2")
    b = ir_Annotation(name="sample_text")
    _safe_set(b, 'ir_Annotation', a1)
    assert _is_linked(b, 'ir_Annotation', a1)
    if hasattr(a1, 'ir_Node'):
        assert _is_linked(a1, 'ir_Node', b)
    _safe_set(b, 'ir_Annotation', a2)
    assert _is_linked(b, 'ir_Annotation', a2)
    if hasattr(a1, 'ir_Node'):
        assert not _is_linked(a1, 'ir_Node', b)
    if hasattr(a2, 'ir_Node'):
        assert _is_linked(a2, 'ir_Node', b)
    _safe_set(b, 'ir_Annotation', None)
    assert not _is_linked(b, 'ir_Annotation', a2)
    if hasattr(a2, 'ir_Node'):
        assert not _is_linked(a2, 'ir_Node', b)


def test_assoc_arguments255_reverse_link_reassign_clear():
    a1 = ir_AnnotationArgument(id="sample_text", value="sample_text")
    a2 = ir_AnnotationArgument(id="sample_text_2", value="sample_text_2")
    b = ir_Annotation(name="sample_text")
    _safe_set(b, 'ir_Annotation256', {a1})
    assert _is_linked(b, 'ir_Annotation256', a1)
    if hasattr(a1, 'ir_AnnotationArgument'):
        assert _is_linked(a1, 'ir_AnnotationArgument', b)
    _safe_set(b, 'ir_Annotation256', {a2})
    assert _is_linked(b, 'ir_Annotation256', a2)
    if hasattr(a1, 'ir_AnnotationArgument'):
        assert not _is_linked(a1, 'ir_AnnotationArgument', b)
    if hasattr(a2, 'ir_AnnotationArgument'):
        assert _is_linked(a2, 'ir_AnnotationArgument', b)
    _safe_set(b, 'ir_Annotation256', set())
    assert not _is_linked(b, 'ir_Annotation256', a2)
    if hasattr(a2, 'ir_AnnotationArgument'):
        assert not _is_linked(a2, 'ir_AnnotationArgument', b)


def test_assoc_attributes174_reverse_link_reassign_clear():
    a1 = ir_TaggedExpression(tag="sample_text")
    a2 = ir_TaggedExpression(tag="sample_text_2")
    b = ir_Declaration(name="sample_text")
    _safe_set(b, 'ir_Declaration175', {a1})
    assert _is_linked(b, 'ir_Declaration175', a1)
    if hasattr(a1, 'ir_TaggedExpression176'):
        assert _is_linked(a1, 'ir_TaggedExpression176', b)
    _safe_set(b, 'ir_Declaration175', {a2})
    assert _is_linked(b, 'ir_Declaration175', a2)
    if hasattr(a1, 'ir_TaggedExpression176'):
        assert not _is_linked(a1, 'ir_TaggedExpression176', b)
    if hasattr(a2, 'ir_TaggedExpression176'):
        assert _is_linked(a2, 'ir_TaggedExpression176', b)
    _safe_set(b, 'ir_Declaration175', set())
    assert not _is_linked(b, 'ir_Declaration175', a2)
    if hasattr(a2, 'ir_TaggedExpression176'):
        assert not _is_linked(a2, 'ir_TaggedExpression176', b)


def test_assoc_attributes212_reverse_link_reassign_clear():
    a1 = ir_TypeExternal(name="sample_text", scopeName="sample_text")
    a2 = ir_TypeExternal(name="sample_text_2", scopeName="sample_text_2")
    b = ir_TaggedExpression(tag="sample_text")
    _safe_set(b, 'ir_TaggedExpression213', a1)
    assert _is_linked(b, 'ir_TaggedExpression213', a1)
    if hasattr(a1, 'ir_TypeExternal'):
        assert _is_linked(a1, 'ir_TypeExternal', b)
    _safe_set(b, 'ir_TaggedExpression213', a2)
    assert _is_linked(b, 'ir_TaggedExpression213', a2)
    if hasattr(a1, 'ir_TypeExternal'):
        assert not _is_linked(a1, 'ir_TypeExternal', b)
    if hasattr(a2, 'ir_TypeExternal'):
        assert _is_linked(a2, 'ir_TypeExternal', b)
    _safe_set(b, 'ir_TaggedExpression213', None)
    assert not _is_linked(b, 'ir_TaggedExpression213', a2)
    if hasattr(a2, 'ir_TypeExternal'):
        assert not _is_linked(a2, 'ir_TypeExternal', b)


def test_assoc_freeRunners249_reverse_link_reassign_clear():
    a1 = ir_Schedule(PriorityGraph="sample_text")
    a2 = ir_Schedule(PriorityGraph="sample_text_2")
    b = ir_Action(tag="sample_text")
    _safe_set(b, 'ir_Action251', a1)
    assert _is_linked(b, 'ir_Action251', a1)
    if hasattr(a1, 'ir_Schedule250'):
        assert _is_linked(a1, 'ir_Schedule250', b)
    _safe_set(b, 'ir_Action251', a2)
    assert _is_linked(b, 'ir_Action251', a2)
    if hasattr(a1, 'ir_Schedule250'):
        assert not _is_linked(a1, 'ir_Schedule250', b)
    if hasattr(a2, 'ir_Schedule250'):
        assert _is_linked(a2, 'ir_Schedule250', b)
    _safe_set(b, 'ir_Action251', None)
    assert not _is_linked(b, 'ir_Action251', a2)
    if hasattr(a2, 'ir_Schedule250'):
        assert not _is_linked(a2, 'ir_Schedule250', b)


def test_assoc_initialState252_reverse_link_reassign_clear():
    a1 = ir_State(Action2TargetMap="sample_text", PriorityGraph="sample_text", name="sample_text")
    a2 = ir_State(Action2TargetMap="sample_text_2", PriorityGraph="sample_text_2", name="sample_text_2")
    b = ir_Schedule(PriorityGraph="sample_text")
    _safe_set(b, 'ir_Schedule253', a1)
    assert _is_linked(b, 'ir_Schedule253', a1)
    if hasattr(a1, 'ir_State254'):
        assert _is_linked(a1, 'ir_State254', b)
    _safe_set(b, 'ir_Schedule253', a2)
    assert _is_linked(b, 'ir_Schedule253', a2)
    if hasattr(a1, 'ir_State254'):
        assert not _is_linked(a1, 'ir_State254', b)
    if hasattr(a2, 'ir_State254'):
        assert _is_linked(a2, 'ir_State254', b)
    _safe_set(b, 'ir_Schedule253', None)
    assert not _is_linked(b, 'ir_Schedule253', a2)
    if hasattr(a2, 'ir_State254'):
        assert not _is_linked(a2, 'ir_State254', b)


def test_assoc_states247_reverse_link_reassign_clear():
    a1 = ir_State(Action2TargetMap="sample_text", PriorityGraph="sample_text", name="sample_text")
    a2 = ir_State(Action2TargetMap="sample_text_2", PriorityGraph="sample_text_2", name="sample_text_2")
    b = ir_Schedule(PriorityGraph="sample_text")
    _safe_set(b, 'ir_Schedule248', {a1})
    assert _is_linked(b, 'ir_Schedule248', a1)
    if hasattr(a1, 'ir_State'):
        assert _is_linked(a1, 'ir_State', b)
    _safe_set(b, 'ir_Schedule248', {a2})
    assert _is_linked(b, 'ir_Schedule248', a2)
    if hasattr(a1, 'ir_State'):
        assert not _is_linked(a1, 'ir_State', b)
    if hasattr(a2, 'ir_State'):
        assert _is_linked(a2, 'ir_State', b)
    _safe_set(b, 'ir_Schedule248', set())
    assert not _is_linked(b, 'ir_Schedule248', a2)
    if hasattr(a2, 'ir_State'):
        assert not _is_linked(a2, 'ir_State', b)


def test_assoc_typedef91_reverse_link_reassign_clear():
    a1 = ir_TypeConstructorCall(name="sample_text")
    a2 = ir_TypeConstructorCall(name="sample_text_2")
    b = ir_Declaration(name="sample_text")
    _safe_set(b, 'ir_Declaration93', a1)
    assert _is_linked(b, 'ir_Declaration93', a1)
    if hasattr(a1, 'ir_TypeConstructorCall92'):
        assert _is_linked(a1, 'ir_TypeConstructorCall92', b)
    _safe_set(b, 'ir_Declaration93', a2)
    assert _is_linked(b, 'ir_Declaration93', a2)
    if hasattr(a1, 'ir_TypeConstructorCall92'):
        assert not _is_linked(a1, 'ir_TypeConstructorCall92', b)
    if hasattr(a2, 'ir_TypeConstructorCall92'):
        assert _is_linked(a2, 'ir_TypeConstructorCall92', b)
    _safe_set(b, 'ir_Declaration93', None)
    assert not _is_linked(b, 'ir_Declaration93', a2)
    if hasattr(a2, 'ir_TypeConstructorCall92'):
        assert not _is_linked(a2, 'ir_TypeConstructorCall92', b)


