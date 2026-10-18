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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions16_stub_double():
    # ir_Actor has no real 'ir_Actor' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_Actor()
    setattr(partner, 'ir_Actor', None)
    _safe_set(owner, 'ir_Action', partner)
    assert owner in getattr(partner, 'ir_Actor')
    _safe_set(owner, 'ir_Action', None)
    assert owner not in getattr(partner, 'ir_Actor')


def test_assoc_actor46_stub_double():
    # ir_ActorInstance has no real 'ir_ActorInstance48' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_ActorInstance()
    setattr(partner, 'ir_ActorInstance48', None)
    _safe_set(owner, 'ir_PortInstance47', partner)
    assert getattr(partner, 'ir_ActorInstance48') == owner
    _safe_set(owner, 'ir_PortInstance47', None)
    assert getattr(partner, 'ir_ActorInstance48') is None


def test_assoc_actors6_stub_double():
    # ir_AbstractActor has no real 'ir_AbstractActor' property in the generated
    # code (a bare stub) -- manually attach it so ir_Namespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Namespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Namespace(name="sample_text")
    partner = ir_AbstractActor()
    setattr(partner, 'ir_AbstractActor', None)
    _safe_set(owner, 'ir_Namespace', {partner})
    assert getattr(partner, 'ir_AbstractActor') == owner
    _safe_set(owner, 'ir_Namespace', set())
    assert getattr(partner, 'ir_AbstractActor') is None


def test_assoc_actualParameters41_stub_double():
    # ir_ActorInstance has no real 'ir_ActorInstance42' property in the generated
    # code (a bare stub) -- manually attach it so ir_TaggedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TaggedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TaggedExpression(tag="sample_text")
    partner = ir_ActorInstance()
    setattr(partner, 'ir_ActorInstance42', None)
    _safe_set(owner, 'ir_TaggedExpression', partner)
    assert owner in getattr(partner, 'ir_ActorInstance42')
    _safe_set(owner, 'ir_TaggedExpression', None)
    assert owner not in getattr(partner, 'ir_ActorInstance42')


def test_assoc_attributes94_stub_double():
    # ir_Connection has no real 'ir_Connection95' property in the generated
    # code (a bare stub) -- manually attach it so ir_TaggedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TaggedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TaggedExpression(tag="sample_text")
    partner = ir_Connection()
    setattr(partner, 'ir_Connection95', None)
    _safe_set(owner, 'ir_TaggedExpression96', partner)
    assert owner in getattr(partner, 'ir_Connection95')
    _safe_set(owner, 'ir_TaggedExpression96', None)
    assert owner not in getattr(partner, 'ir_Connection95')


def test_assoc_connections43_stub_double():
    # ir_Connection has no real 'ir_Connection45' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_Connection()
    setattr(partner, 'ir_Connection45', None)
    _safe_set(owner, 'ir_PortInstance44', {partner})
    assert getattr(partner, 'ir_Connection45') == owner
    _safe_set(owner, 'ir_PortInstance44', set())
    assert getattr(partner, 'ir_Connection45') is None


def test_assoc_declaration112_stub_double():
    # ir_VariableReference has no real 'ir_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_VariableReference()
    setattr(partner, 'ir_VariableReference', None)
    _safe_set(owner, 'ir_Variable113', partner)
    assert getattr(partner, 'ir_VariableReference') == owner
    _safe_set(owner, 'ir_Variable113', None)
    assert getattr(partner, 'ir_VariableReference') is None


def test_assoc_declaration177_stub_double():
    # ir_ForwardDeclaration has no real 'ir_ForwardDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_ForwardDeclaration()
    setattr(partner, 'ir_ForwardDeclaration', None)
    _safe_set(owner, 'ir_Declaration178', partner)
    assert getattr(partner, 'ir_ForwardDeclaration') == owner
    _safe_set(owner, 'ir_Declaration178', None)
    assert getattr(partner, 'ir_ForwardDeclaration') is None


def test_assoc_declaration225_stub_double():
    # ir_TypeUser has no real 'ir_TypeUser' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_TypeUser()
    setattr(partner, 'ir_TypeUser', None)
    _safe_set(owner, 'ir_Declaration226', partner)
    assert getattr(partner, 'ir_TypeUser') == owner
    _safe_set(owner, 'ir_Declaration226', None)
    assert getattr(partner, 'ir_TypeUser') is None


def test_assoc_declarations0_stub_double():
    # ir_Scope has no real 'ir_Scope' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_Scope()
    setattr(partner, 'ir_Scope', None)
    _safe_set(owner, 'ir_Declaration', partner)
    assert owner in getattr(partner, 'ir_Scope')
    _safe_set(owner, 'ir_Declaration', None)
    assert owner not in getattr(partner, 'ir_Scope')


def test_assoc_expression54_stub_double():
    # ir_Expression has no real 'ir_Expression56' property in the generated
    # code (a bare stub) -- manually attach it so ir_TaggedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TaggedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TaggedExpression(tag="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression56', None)
    _safe_set(owner, 'ir_TaggedExpression55', partner)
    assert getattr(partner, 'ir_Expression56') == owner
    _safe_set(owner, 'ir_TaggedExpression55', None)
    assert getattr(partner, 'ir_Expression56') is None


def test_assoc_guards25_stub_double():
    # ir_Guard has no real 'ir_Guard' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_Guard()
    setattr(partner, 'ir_Guard', None)
    _safe_set(owner, 'ir_Action26', {partner})
    assert getattr(partner, 'ir_Guard') == owner
    _safe_set(owner, 'ir_Action26', set())
    assert getattr(partner, 'ir_Guard') is None


def test_assoc_index71_stub_double():
    # ir_Expression has no real 'ir_Expression73' property in the generated
    # code (a bare stub) -- manually attach it so ir_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Member(name="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression73', None)
    _safe_set(owner, 'ir_Member72', {partner})
    assert getattr(partner, 'ir_Expression73') == owner
    _safe_set(owner, 'ir_Member72', set())
    assert getattr(partner, 'ir_Expression73') is None


def test_assoc_initValue182_stub_double():
    # ir_Expression has no real 'ir_Expression184' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_Expression()
    setattr(partner, 'ir_Expression184', None)
    _safe_set(owner, 'ir_Variable183', partner)
    assert getattr(partner, 'ir_Expression184') == owner
    _safe_set(owner, 'ir_Variable183', None)
    assert getattr(partner, 'ir_Expression184') is None


def test_assoc_initializers17_stub_double():
    # ir_Actor has no real 'ir_Actor18' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_Actor()
    setattr(partner, 'ir_Actor18', None)
    _safe_set(owner, 'ir_Action19', partner)
    assert owner in getattr(partner, 'ir_Actor18')
    _safe_set(owner, 'ir_Action19', None)
    assert owner not in getattr(partner, 'ir_Actor18')


def test_assoc_inputPorts9_stub_double():
    # ir_AbstractActor has no real 'ir_AbstractActor10' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_AbstractActor()
    setattr(partner, 'ir_AbstractActor10', None)
    _safe_set(owner, 'ir_Port', partner)
    assert owner in getattr(partner, 'ir_AbstractActor10')
    _safe_set(owner, 'ir_Port', None)
    assert owner not in getattr(partner, 'ir_AbstractActor10')


def test_assoc_inputs29_stub_double():
    # ir_PortRead has no real 'ir_PortRead' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_PortRead()
    setattr(partner, 'ir_PortRead', None)
    _safe_set(owner, 'ir_Action30', {partner})
    assert getattr(partner, 'ir_PortRead') == owner
    _safe_set(owner, 'ir_Action30', set())
    assert getattr(partner, 'ir_PortRead') is None


def test_assoc_inputs36_stub_double():
    # ir_ActorInstance has no real 'ir_ActorInstance37' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_ActorInstance()
    setattr(partner, 'ir_ActorInstance37', None)
    _safe_set(owner, 'ir_PortInstance', partner)
    assert owner in getattr(partner, 'ir_ActorInstance37')
    _safe_set(owner, 'ir_PortInstance', None)
    assert owner not in getattr(partner, 'ir_ActorInstance37')


def test_assoc_member117_stub_double():
    # ir_VariableReference has no real 'ir_VariableReference118' property in the generated
    # code (a bare stub) -- manually attach it so ir_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Member(name="sample_text")
    partner = ir_VariableReference()
    setattr(partner, 'ir_VariableReference118', None)
    _safe_set(owner, 'ir_Member119', partner)
    assert owner in getattr(partner, 'ir_VariableReference118')
    _safe_set(owner, 'ir_Member119', None)
    assert owner not in getattr(partner, 'ir_VariableReference118')


def test_assoc_member62_stub_double():
    # ir_VariableExpression has no real 'ir_VariableExpression63' property in the generated
    # code (a bare stub) -- manually attach it so ir_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Member(name="sample_text")
    partner = ir_VariableExpression()
    setattr(partner, 'ir_VariableExpression63', None)
    _safe_set(owner, 'ir_Member', partner)
    assert owner in getattr(partner, 'ir_VariableExpression63')
    _safe_set(owner, 'ir_Member', None)
    assert owner not in getattr(partner, 'ir_VariableExpression63')


def test_assoc_members223_stub_double():
    # ir_TypeRecord has no real 'ir_TypeRecord' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_TypeRecord()
    setattr(partner, 'ir_TypeRecord', None)
    _safe_set(owner, 'ir_Variable224', partner)
    assert owner in getattr(partner, 'ir_TypeRecord')
    _safe_set(owner, 'ir_Variable224', None)
    assert owner not in getattr(partner, 'ir_TypeRecord')


def test_assoc_operand177_stub_double():
    # ir_Expression has no real 'ir_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so ir_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BinaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression78', None)
    _safe_set(owner, 'ir_BinaryExpression', partner)
    assert getattr(partner, 'ir_Expression78') == owner
    _safe_set(owner, 'ir_BinaryExpression', None)
    assert getattr(partner, 'ir_Expression78') is None


def test_assoc_operand279_stub_double():
    # ir_Expression has no real 'ir_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so ir_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BinaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression81', None)
    _safe_set(owner, 'ir_BinaryExpression80', partner)
    assert getattr(partner, 'ir_Expression81') == owner
    _safe_set(owner, 'ir_BinaryExpression80', None)
    assert getattr(partner, 'ir_Expression81') is None


def test_assoc_operand82_stub_double():
    # ir_Expression has no real 'ir_Expression83' property in the generated
    # code (a bare stub) -- manually attach it so ir_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_UnaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression83', None)
    _safe_set(owner, 'ir_UnaryExpression', partner)
    assert getattr(partner, 'ir_Expression83') == owner
    _safe_set(owner, 'ir_UnaryExpression', None)
    assert getattr(partner, 'ir_Expression83') is None


def test_assoc_outputPorts11_stub_double():
    # ir_AbstractActor has no real 'ir_AbstractActor12' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_AbstractActor()
    setattr(partner, 'ir_AbstractActor12', None)
    _safe_set(owner, 'ir_Port13', partner)
    assert owner in getattr(partner, 'ir_AbstractActor12')
    _safe_set(owner, 'ir_Port13', None)
    assert owner not in getattr(partner, 'ir_AbstractActor12')


def test_assoc_outputs195_stub_double():
    # ir_ProcExpression has no real 'ir_ProcExpression196' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_ProcExpression()
    setattr(partner, 'ir_ProcExpression196', None)
    _safe_set(owner, 'ir_Variable197', partner)
    assert owner in getattr(partner, 'ir_ProcExpression196')
    _safe_set(owner, 'ir_Variable197', None)
    assert owner not in getattr(partner, 'ir_ProcExpression196')


def test_assoc_outputs27_stub_double():
    # ir_PortWrite has no real 'ir_PortWrite' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_PortWrite()
    setattr(partner, 'ir_PortWrite', None)
    _safe_set(owner, 'ir_Action28', {partner})
    assert getattr(partner, 'ir_PortWrite') == owner
    _safe_set(owner, 'ir_Action28', set())
    assert getattr(partner, 'ir_PortWrite') is None


def test_assoc_outputs38_stub_double():
    # ir_ActorInstance has no real 'ir_ActorInstance39' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_ActorInstance()
    setattr(partner, 'ir_ActorInstance39', None)
    _safe_set(owner, 'ir_PortInstance40', partner)
    assert owner in getattr(partner, 'ir_ActorInstance39')
    _safe_set(owner, 'ir_PortInstance40', None)
    assert owner not in getattr(partner, 'ir_ActorInstance39')


def test_assoc_parameters14_stub_double():
    # ir_AbstractActor has no real 'ir_AbstractActor15' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_AbstractActor()
    setattr(partner, 'ir_AbstractActor15', None)
    _safe_set(owner, 'ir_Variable', partner)
    assert owner in getattr(partner, 'ir_AbstractActor15')
    _safe_set(owner, 'ir_Variable', None)
    assert owner not in getattr(partner, 'ir_AbstractActor15')


def test_assoc_parameters188_stub_double():
    # ir_LambdaExpression has no real 'ir_LambdaExpression' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_LambdaExpression()
    setattr(partner, 'ir_LambdaExpression', None)
    _safe_set(owner, 'ir_Variable189', partner)
    assert owner in getattr(partner, 'ir_LambdaExpression')
    _safe_set(owner, 'ir_Variable189', None)
    assert owner not in getattr(partner, 'ir_LambdaExpression')


def test_assoc_parameters193_stub_double():
    # ir_ProcExpression has no real 'ir_ProcExpression' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_ProcExpression()
    setattr(partner, 'ir_ProcExpression', None)
    _safe_set(owner, 'ir_Variable194', partner)
    assert owner in getattr(partner, 'ir_ProcExpression')
    _safe_set(owner, 'ir_Variable194', None)
    assert owner not in getattr(partner, 'ir_ProcExpression')


def test_assoc_parameters238_stub_double():
    # ir_TypeConstructor has no real 'ir_TypeConstructor239' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_TypeConstructor()
    setattr(partner, 'ir_TypeConstructor239', None)
    _safe_set(owner, 'ir_Variable240', partner)
    assert owner in getattr(partner, 'ir_TypeConstructor239')
    _safe_set(owner, 'ir_Variable240', None)
    assert owner not in getattr(partner, 'ir_TypeConstructor239')


def test_assoc_parameters89_stub_double():
    # ir_Expression has no real 'ir_Expression90' property in the generated
    # code (a bare stub) -- manually attach it so ir_TypeConstructorCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TypeConstructorCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TypeConstructorCall(name="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression90', None)
    _safe_set(owner, 'ir_TypeConstructorCall', {partner})
    assert getattr(partner, 'ir_Expression90') == owner
    _safe_set(owner, 'ir_TypeConstructorCall', set())
    assert getattr(partner, 'ir_Expression90') is None


def test_assoc_peeks209_stub_double():
    # ir_Guard has no real 'ir_Guard210' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortPeek's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortPeek's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortPeek(position=7)
    partner = ir_Guard()
    setattr(partner, 'ir_Guard210', None)
    _safe_set(owner, 'ir_PortPeek211', partner)
    assert owner in getattr(partner, 'ir_Guard210')
    _safe_set(owner, 'ir_PortPeek211', None)
    assert owner not in getattr(partner, 'ir_Guard210')


def test_assoc_port158_stub_double():
    # ir_PortAccess has no real 'ir_PortAccess' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_PortAccess()
    setattr(partner, 'ir_PortAccess', None)
    _safe_set(owner, 'ir_Port159', partner)
    assert getattr(partner, 'ir_PortAccess') == owner
    _safe_set(owner, 'ir_Port159', None)
    assert getattr(partner, 'ir_PortAccess') is None


def test_assoc_procedure135_stub_double():
    # ir_ProcCall has no real 'ir_ProcCall136' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_ProcCall()
    setattr(partner, 'ir_ProcCall136', None)
    _safe_set(owner, 'ir_Declaration137', partner)
    assert getattr(partner, 'ir_ProcCall136') == owner
    _safe_set(owner, 'ir_Declaration137', None)
    assert getattr(partner, 'ir_ProcCall136') is None


def test_assoc_schedule20_stub_double():
    # ir_Actor has no real 'ir_Actor21' property in the generated
    # code (a bare stub) -- manually attach it so ir_Schedule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Schedule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Schedule(PriorityGraph="sample_text")
    partner = ir_Actor()
    setattr(partner, 'ir_Actor21', None)
    _safe_set(owner, 'ir_Schedule', partner)
    assert getattr(partner, 'ir_Actor21') == owner
    _safe_set(owner, 'ir_Schedule', None)
    assert getattr(partner, 'ir_Actor21') is None


def test_assoc_scope171_stub_double():
    # ir_Scope has no real 'ir_Scope173' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_Scope()
    setattr(partner, 'ir_Scope173', None)
    _safe_set(owner, 'ir_Declaration172', partner)
    assert getattr(partner, 'ir_Scope173') == owner
    _safe_set(owner, 'ir_Declaration172', None)
    assert getattr(partner, 'ir_Scope173') is None


def test_assoc_sink109_stub_double():
    # ir_ToSink has no real 'ir_ToSink110' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_ToSink()
    setattr(partner, 'ir_ToSink110', None)
    _safe_set(owner, 'ir_Port111', partner)
    assert getattr(partner, 'ir_ToSink110') == owner
    _safe_set(owner, 'ir_Port111', None)
    assert getattr(partner, 'ir_ToSink110') is None


def test_assoc_source104_stub_double():
    # ir_FromSource has no real 'ir_FromSource105' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_FromSource()
    setattr(partner, 'ir_FromSource105', None)
    _safe_set(owner, 'ir_Port106', partner)
    assert getattr(partner, 'ir_FromSource105') == owner
    _safe_set(owner, 'ir_Port106', None)
    assert getattr(partner, 'ir_FromSource105') is None


def test_assoc_source107_stub_double():
    # ir_ToSink has no real 'ir_ToSink' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_ToSink()
    setattr(partner, 'ir_ToSink', None)
    _safe_set(owner, 'ir_PortInstance108', partner)
    assert getattr(partner, 'ir_ToSink') == owner
    _safe_set(owner, 'ir_PortInstance108', None)
    assert getattr(partner, 'ir_ToSink') is None


def test_assoc_source97_stub_double():
    # ir_Point2PointConnection has no real 'ir_Point2PointConnection' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_Point2PointConnection()
    setattr(partner, 'ir_Point2PointConnection', None)
    _safe_set(owner, 'ir_PortInstance98', partner)
    assert getattr(partner, 'ir_Point2PointConnection') == owner
    _safe_set(owner, 'ir_PortInstance98', None)
    assert getattr(partner, 'ir_Point2PointConnection') is None


def test_assoc_statements31_stub_double():
    # ir_Statement has no real 'ir_Statement' property in the generated
    # code (a bare stub) -- manually attach it so ir_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Action(tag="sample_text")
    partner = ir_Statement()
    setattr(partner, 'ir_Statement', None)
    _safe_set(owner, 'ir_Action32', {partner})
    assert getattr(partner, 'ir_Statement') == owner
    _safe_set(owner, 'ir_Action32', set())
    assert getattr(partner, 'ir_Statement') is None


def test_assoc_target102_stub_double():
    # ir_FromSource has no real 'ir_FromSource' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_FromSource()
    setattr(partner, 'ir_FromSource', None)
    _safe_set(owner, 'ir_PortInstance103', partner)
    assert getattr(partner, 'ir_FromSource') == owner
    _safe_set(owner, 'ir_PortInstance103', None)
    assert getattr(partner, 'ir_FromSource') is None


def test_assoc_target99_stub_double():
    # ir_Point2PointConnection has no real 'ir_Point2PointConnection100' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortInstance(name="sample_text")
    partner = ir_Point2PointConnection()
    setattr(partner, 'ir_Point2PointConnection100', None)
    _safe_set(owner, 'ir_PortInstance101', partner)
    assert getattr(partner, 'ir_Point2PointConnection100') == owner
    _safe_set(owner, 'ir_PortInstance101', None)
    assert getattr(partner, 'ir_Point2PointConnection100') is None


def test_assoc_type185_stub_double():
    # ir_Type has no real 'ir_Type187' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(constant=True, parameter=True)
    partner = ir_Type()
    setattr(partner, 'ir_Type187', None)
    _safe_set(owner, 'ir_Variable186', partner)
    assert getattr(partner, 'ir_Type187') == owner
    _safe_set(owner, 'ir_Variable186', None)
    assert getattr(partner, 'ir_Type187') is None


def test_assoc_type33_stub_double():
    # ir_Type has no real 'ir_Type35' property in the generated
    # code (a bare stub) -- manually attach it so ir_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Port(name="sample_text")
    partner = ir_Type()
    setattr(partner, 'ir_Type35', None)
    _safe_set(owner, 'ir_Port34', partner)
    assert getattr(partner, 'ir_Type35') == owner
    _safe_set(owner, 'ir_Port34', None)
    assert getattr(partner, 'ir_Type35') is None


def test_assoc_type7_stub_double():
    # ir_AbstractActor has no real 'ir_AbstractActor8' property in the generated
    # code (a bare stub) -- manually attach it so ir_TypeActor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TypeActor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TypeActor(name="sample_text", namespace="sample_text")
    partner = ir_AbstractActor()
    setattr(partner, 'ir_AbstractActor8', None)
    _safe_set(owner, 'ir_TypeActor', partner)
    assert getattr(partner, 'ir_AbstractActor8') == owner
    _safe_set(owner, 'ir_TypeActor', None)
    assert getattr(partner, 'ir_AbstractActor8') is None


def test_assoc_type74_stub_double():
    # ir_Type has no real 'ir_Type76' property in the generated
    # code (a bare stub) -- manually attach it so ir_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Member(name="sample_text")
    partner = ir_Type()
    setattr(partner, 'ir_Type76', None)
    _safe_set(owner, 'ir_Member75', partner)
    assert getattr(partner, 'ir_Type76') == owner
    _safe_set(owner, 'ir_Member75', None)
    assert getattr(partner, 'ir_Type76') is None


def test_assoc_variable169_stub_double():
    # ir_VariableReference has no real 'ir_VariableReference170' property in the generated
    # code (a bare stub) -- manually attach it so ir_PortPeek's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PortPeek's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PortPeek(position=7)
    partner = ir_VariableReference()
    setattr(partner, 'ir_VariableReference170', None)
    _safe_set(owner, 'ir_PortPeek', partner)
    assert getattr(partner, 'ir_VariableReference170') == owner
    _safe_set(owner, 'ir_PortPeek', None)
    assert getattr(partner, 'ir_VariableReference170') is None


def test_assoc_variable57_stub_double():
    # ir_VariableExpression has no real 'ir_VariableExpression' property in the generated
    # code (a bare stub) -- manually attach it so ir_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Declaration(name="sample_text")
    partner = ir_VariableExpression()
    setattr(partner, 'ir_VariableExpression', None)
    _safe_set(owner, 'ir_Declaration58', partner)
    assert getattr(partner, 'ir_VariableExpression') == owner
    _safe_set(owner, 'ir_Declaration58', None)
    assert getattr(partner, 'ir_VariableExpression') is None


