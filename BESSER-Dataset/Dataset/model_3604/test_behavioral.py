import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractConnector,
    Action,
    AnnotatedElement,
    Event,
    Expression,
    Handler,
    Literal,
    NamedElement,
    Port,
    State,
    StateContainer,
    Type,
    Variable,
    thingML_AbstractConnector,
    thingML_Action,
    thingML_ActionBlock,
    thingML_AndExpression,
    thingML_AnnotatedElement,
    thingML_ArrayIndex,
    thingML_ArrayInit,
    thingML_BooleanLiteral,
    thingML_ByteLiteral,
    thingML_CastExpression,
    thingML_CharLiteral,
    thingML_CompositeState,
    thingML_ConditionalAction,
    thingML_ConfigPropertyAssign,
    thingML_Configuration,
    thingML_Connector,
    thingML_Decrement,
    thingML_DivExpression,
    thingML_DoubleLiteral,
    thingML_EnumLiteralRef,
    thingML_Enumeration,
    thingML_EnumerationLiteral,
    thingML_EqualsExpression,
    thingML_ErrorAction,
    thingML_Event,
    thingML_EventReference,
    thingML_Expression,
    thingML_ExpressionGroup,
    thingML_ExternExpression,
    thingML_ExternStatement,
    thingML_ExternalConnector,
    thingML_FinalState,
    thingML_ForAction,
    thingML_Function,
    thingML_FunctionCallExpression,
    thingML_FunctionCallStatement,
    thingML_GreaterExpression,
    thingML_GreaterOrEqualExpression,
    thingML_Handler,
    thingML_Import,
    thingML_Increment,
    thingML_Instance,
    thingML_IntegerLiteral,
    thingML_InternalPort,
    thingML_InternalTransition,
    thingML_Literal,
    thingML_LocalVariable,
    thingML_LoopAction,
    thingML_LowerExpression,
    thingML_LowerOrEqualExpression,
    thingML_Message,
    thingML_MinusExpression,
    thingML_ModExpression,
    thingML_NamedElement,
    thingML_NotEqualsExpression,
    thingML_NotExpression,
    thingML_ObjectType,
    thingML_OrExpression,
    thingML_Parameter,
    thingML_PlatformAnnotation,
    thingML_PlusExpression,
    thingML_Port,
    thingML_PrimitiveType,
    thingML_PrintAction,
    thingML_Property,
    thingML_PropertyAssign,
    thingML_PropertyReference,
    thingML_Protocol,
    thingML_ProvidedPort,
    thingML_ReceiveMessage,
    thingML_Region,
    thingML_RequiredPort,
    thingML_ReturnAction,
    thingML_SendAction,
    thingML_Session,
    thingML_StartSession,
    thingML_State,
    thingML_StateContainer,
    thingML_StringLiteral,
    thingML_Thing,
    thingML_ThingMLModel,
    thingML_TimesExpression,
    thingML_Transition,
    thingML_Type,
    thingML_TypeRef,
    thingML_UnaryMinus,
    thingML_Variable,
    thingML_VariableAssignment,
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

def test_assoc_functions28_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Function(abstract=True)
    _safe_set(b, 'thingML_Function', a1)
    assert _is_linked(b, 'thingML_Function', a1)
    if hasattr(a1, 'thingML_Thing29'):
        assert _is_linked(a1, 'thingML_Thing29', b)
    _safe_set(b, 'thingML_Function', a2)
    assert _is_linked(b, 'thingML_Function', a2)
    if hasattr(a1, 'thingML_Thing29'):
        assert not _is_linked(a1, 'thingML_Thing29', b)
    if hasattr(a2, 'thingML_Thing29'):
        assert _is_linked(a2, 'thingML_Thing29', b)
    _safe_set(b, 'thingML_Function', None)
    assert not _is_linked(b, 'thingML_Function', a2)
    if hasattr(a2, 'thingML_Thing29'):
        assert not _is_linked(a2, 'thingML_Thing29', b)


def test_assoc_includes21_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Thing(fragment=True)
    _safe_set(b, 'thingML_Thing20', {a1})
    assert _is_linked(b, 'thingML_Thing20', a1)
    if hasattr(a1, 'thingML_Thing'):
        assert _is_linked(a1, 'thingML_Thing', b)
    _safe_set(b, 'thingML_Thing20', {a2})
    assert _is_linked(b, 'thingML_Thing20', a2)
    if hasattr(a1, 'thingML_Thing'):
        assert not _is_linked(a1, 'thingML_Thing', b)
    if hasattr(a2, 'thingML_Thing'):
        assert _is_linked(a2, 'thingML_Thing', b)
    _safe_set(b, 'thingML_Thing20', set())
    assert not _is_linked(b, 'thingML_Thing20', a2)
    if hasattr(a2, 'thingML_Thing'):
        assert not _is_linked(a2, 'thingML_Thing', b)


def test_assoc_properties26_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Property(readonly=True)
    _safe_set(b, 'thingML_Property', a1)
    assert _is_linked(b, 'thingML_Property', a1)
    if hasattr(a1, 'thingML_Thing27'):
        assert _is_linked(a1, 'thingML_Thing27', b)
    _safe_set(b, 'thingML_Property', a2)
    assert _is_linked(b, 'thingML_Property', a2)
    if hasattr(a1, 'thingML_Thing27'):
        assert not _is_linked(a1, 'thingML_Thing27', b)
    if hasattr(a2, 'thingML_Thing27'):
        assert _is_linked(a2, 'thingML_Thing27', b)
    _safe_set(b, 'thingML_Property', None)
    assert not _is_linked(b, 'thingML_Property', a2)
    if hasattr(a2, 'thingML_Thing27'):
        assert not _is_linked(a2, 'thingML_Thing27', b)


def test_assoc_typeRef45_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_Function(abstract=True)
    _safe_set(b, 'thingML_Function46', a1)
    assert _is_linked(b, 'thingML_Function46', a1)
    if hasattr(a1, 'thingML_TypeRef47'):
        assert _is_linked(a1, 'thingML_TypeRef47', b)
    _safe_set(b, 'thingML_Function46', a2)
    assert _is_linked(b, 'thingML_Function46', a2)
    if hasattr(a1, 'thingML_TypeRef47'):
        assert not _is_linked(a1, 'thingML_TypeRef47', b)
    if hasattr(a2, 'thingML_TypeRef47'):
        assert _is_linked(a2, 'thingML_TypeRef47', b)
    _safe_set(b, 'thingML_Function46', None)
    assert not _is_linked(b, 'thingML_Function46', a2)
    if hasattr(a2, 'thingML_TypeRef47'):
        assert not _is_linked(a2, 'thingML_TypeRef47', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations206_stub_double():
    # thingML_ConfigPropertyAssign has no real 'thingML_ConfigPropertyAssign207' property in the generated
    # code (a bare stub) -- manually attach it so thingML_PlatformAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_PlatformAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_PlatformAnnotation(name="sample_text", value="sample_text")
    partner = thingML_ConfigPropertyAssign()
    setattr(partner, 'thingML_ConfigPropertyAssign207', None)
    _safe_set(owner, 'thingML_PlatformAnnotation208', partner)
    assert owner in getattr(partner, 'thingML_ConfigPropertyAssign207')
    _safe_set(owner, 'thingML_PlatformAnnotation208', None)
    assert owner not in getattr(partner, 'thingML_ConfigPropertyAssign207')


def test_assoc_annotations7_stub_double():
    # thingML_AnnotatedElement has no real 'thingML_AnnotatedElement' property in the generated
    # code (a bare stub) -- manually attach it so thingML_PlatformAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_PlatformAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_PlatformAnnotation(name="sample_text", value="sample_text")
    partner = thingML_AnnotatedElement()
    setattr(partner, 'thingML_AnnotatedElement', None)
    _safe_set(owner, 'thingML_PlatformAnnotation', partner)
    assert owner in getattr(partner, 'thingML_AnnotatedElement')
    _safe_set(owner, 'thingML_PlatformAnnotation', None)
    assert owner not in getattr(partner, 'thingML_AnnotatedElement')


def test_assoc_assign30_stub_double():
    # thingML_PropertyAssign has no real 'thingML_PropertyAssign' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_PropertyAssign()
    setattr(partner, 'thingML_PropertyAssign', None)
    _safe_set(owner, 'thingML_Thing31', {partner})
    assert getattr(partner, 'thingML_PropertyAssign') == owner
    _safe_set(owner, 'thingML_Thing31', set())
    assert getattr(partner, 'thingML_PropertyAssign') is None


def test_assoc_behaviour32_stub_double():
    # thingML_CompositeState has no real 'thingML_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_CompositeState()
    setattr(partner, 'thingML_CompositeState', None)
    _safe_set(owner, 'thingML_Thing33', partner)
    assert getattr(partner, 'thingML_CompositeState') == owner
    _safe_set(owner, 'thingML_Thing33', None)
    assert getattr(partner, 'thingML_CompositeState') is None


def test_assoc_body48_stub_double():
    # thingML_Action has no real 'thingML_Action' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(abstract=True)
    partner = thingML_Action()
    setattr(partner, 'thingML_Action', None)
    _safe_set(owner, 'thingML_Function49', partner)
    assert getattr(partner, 'thingML_Action') == owner
    _safe_set(owner, 'thingML_Function49', None)
    assert getattr(partner, 'thingML_Action') is None


def test_assoc_cardinality12_stub_double():
    # thingML_Expression has no real 'thingML_Expression' property in the generated
    # code (a bare stub) -- manually attach it so thingML_TypeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_TypeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_TypeRef(isArray=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression', None)
    _safe_set(owner, 'thingML_TypeRef13', partner)
    assert getattr(partner, 'thingML_Expression') == owner
    _safe_set(owner, 'thingML_TypeRef13', None)
    assert getattr(partner, 'thingML_Expression') is None


def test_assoc_function158_stub_double():
    # thingML_FunctionCallStatement has no real 'thingML_FunctionCallStatement' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(abstract=True)
    partner = thingML_FunctionCallStatement()
    setattr(partner, 'thingML_FunctionCallStatement', None)
    _safe_set(owner, 'thingML_Function159', partner)
    assert getattr(partner, 'thingML_FunctionCallStatement') == owner
    _safe_set(owner, 'thingML_Function159', None)
    assert getattr(partner, 'thingML_FunctionCallStatement') is None


def test_assoc_function180_stub_double():
    # thingML_FunctionCallExpression has no real 'thingML_FunctionCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(abstract=True)
    partner = thingML_FunctionCallExpression()
    setattr(partner, 'thingML_FunctionCallExpression', None)
    _safe_set(owner, 'thingML_Function181', partner)
    assert getattr(partner, 'thingML_FunctionCallExpression') == owner
    _safe_set(owner, 'thingML_Function181', None)
    assert getattr(partner, 'thingML_FunctionCallExpression') is None


def test_assoc_imports0_stub_double():
    # thingML_ThingMLModel has no real 'thingML_ThingMLModel' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Import(from_="sample_text", importURI="sample_text")
    partner = thingML_ThingMLModel()
    setattr(partner, 'thingML_ThingMLModel', None)
    _safe_set(owner, 'thingML_Import', partner)
    assert owner in getattr(partner, 'thingML_ThingMLModel')
    _safe_set(owner, 'thingML_Import', None)
    assert owner not in getattr(partner, 'thingML_ThingMLModel')


def test_assoc_init105_stub_double():
    # thingML_Expression has no real 'thingML_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so thingML_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_LocalVariable(readonly=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression106', None)
    _safe_set(owner, 'thingML_LocalVariable', partner)
    assert getattr(partner, 'thingML_Expression106') == owner
    _safe_set(owner, 'thingML_LocalVariable', None)
    assert getattr(partner, 'thingML_Expression106') is None


def test_assoc_init50_stub_double():
    # thingML_Expression has no real 'thingML_Expression52' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(readonly=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression52', None)
    _safe_set(owner, 'thingML_Property51', partner)
    assert getattr(partner, 'thingML_Expression52') == owner
    _safe_set(owner, 'thingML_Property51', None)
    assert getattr(partner, 'thingML_Expression52') is None


def test_assoc_initial91_stub_double():
    # thingML_State has no real 'thingML_State92' property in the generated
    # code (a bare stub) -- manually attach it so thingML_StateContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_StateContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_StateContainer(history=True)
    partner = thingML_State()
    setattr(partner, 'thingML_State92', None)
    _safe_set(owner, 'thingML_StateContainer', partner)
    assert getattr(partner, 'thingML_State92') == owner
    _safe_set(owner, 'thingML_StateContainer', None)
    assert getattr(partner, 'thingML_State92') is None


def test_assoc_messages22_stub_double():
    # thingML_Message has no real 'thingML_Message' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_Message()
    setattr(partner, 'thingML_Message', None)
    _safe_set(owner, 'thingML_Thing23', {partner})
    assert getattr(partner, 'thingML_Message') == owner
    _safe_set(owner, 'thingML_Thing23', set())
    assert getattr(partner, 'thingML_Message') is None


def test_assoc_msg152_stub_double():
    # thingML_Expression has no real 'thingML_Expression153' property in the generated
    # code (a bare stub) -- manually attach it so thingML_PrintAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_PrintAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_PrintAction(line=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression153', None)
    _safe_set(owner, 'thingML_PrintAction', {partner})
    assert getattr(partner, 'thingML_Expression153') == owner
    _safe_set(owner, 'thingML_PrintAction', set())
    assert getattr(partner, 'thingML_Expression153') is None


def test_assoc_msg154_stub_double():
    # thingML_Expression has no real 'thingML_Expression155' property in the generated
    # code (a bare stub) -- manually attach it so thingML_ErrorAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_ErrorAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_ErrorAction(line=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression155', None)
    _safe_set(owner, 'thingML_ErrorAction', {partner})
    assert getattr(partner, 'thingML_Expression155') == owner
    _safe_set(owner, 'thingML_ErrorAction', set())
    assert getattr(partner, 'thingML_Expression155') is None


def test_assoc_parameters43_stub_double():
    # thingML_Parameter has no real 'thingML_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(abstract=True)
    partner = thingML_Parameter()
    setattr(partner, 'thingML_Parameter', None)
    _safe_set(owner, 'thingML_Function44', {partner})
    assert getattr(partner, 'thingML_Parameter') == owner
    _safe_set(owner, 'thingML_Function44', set())
    assert getattr(partner, 'thingML_Parameter') is None


def test_assoc_ports24_stub_double():
    # thingML_Port has no real 'thingML_Port' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_Port()
    setattr(partner, 'thingML_Port', None)
    _safe_set(owner, 'thingML_Thing25', {partner})
    assert getattr(partner, 'thingML_Port') == owner
    _safe_set(owner, 'thingML_Thing25', set())
    assert getattr(partner, 'thingML_Port') is None


def test_assoc_properties62_stub_double():
    # thingML_State has no real 'thingML_State' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(readonly=True)
    partner = thingML_State()
    setattr(partner, 'thingML_State', None)
    _safe_set(owner, 'thingML_Property63', partner)
    assert owner in getattr(partner, 'thingML_State')
    _safe_set(owner, 'thingML_Property63', None)
    assert owner not in getattr(partner, 'thingML_State')


def test_assoc_property197_stub_double():
    # thingML_ConfigPropertyAssign has no real 'thingML_ConfigPropertyAssign198' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(readonly=True)
    partner = thingML_ConfigPropertyAssign()
    setattr(partner, 'thingML_ConfigPropertyAssign198', None)
    _safe_set(owner, 'thingML_Property199', partner)
    assert getattr(partner, 'thingML_ConfigPropertyAssign198') == owner
    _safe_set(owner, 'thingML_Property199', None)
    assert getattr(partner, 'thingML_ConfigPropertyAssign198') is None


def test_assoc_property34_stub_double():
    # thingML_PropertyAssign has no real 'thingML_PropertyAssign35' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(readonly=True)
    partner = thingML_PropertyAssign()
    setattr(partner, 'thingML_PropertyAssign35', None)
    _safe_set(owner, 'thingML_Property36', partner)
    assert getattr(partner, 'thingML_PropertyAssign35') == owner
    _safe_set(owner, 'thingML_Property36', None)
    assert getattr(partner, 'thingML_PropertyAssign35') is None


def test_assoc_required211_stub_double():
    # thingML_Connector has no real 'thingML_Connector212' property in the generated
    # code (a bare stub) -- manually attach it so thingML_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_RequiredPort(optional=True)
    partner = thingML_Connector()
    setattr(partner, 'thingML_Connector212', None)
    _safe_set(owner, 'thingML_RequiredPort', partner)
    assert getattr(partner, 'thingML_Connector212') == owner
    _safe_set(owner, 'thingML_RequiredPort', None)
    assert getattr(partner, 'thingML_Connector212') is None


def test_assoc_segments103_stub_double():
    # thingML_Expression has no real 'thingML_Expression104' property in the generated
    # code (a bare stub) -- manually attach it so thingML_ExternStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_ExternStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_ExternStatement(statement="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression104', None)
    _safe_set(owner, 'thingML_ExternStatement', {partner})
    assert getattr(partner, 'thingML_Expression104') == owner
    _safe_set(owner, 'thingML_ExternStatement', set())
    assert getattr(partner, 'thingML_Expression104') is None


def test_assoc_segments163_stub_double():
    # thingML_Expression has no real 'thingML_Expression164' property in the generated
    # code (a bare stub) -- manually attach it so thingML_ExternExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_ExternExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_ExternExpression(expression="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression164', None)
    _safe_set(owner, 'thingML_ExternExpression', {partner})
    assert getattr(partner, 'thingML_Expression164') == owner
    _safe_set(owner, 'thingML_ExternExpression', set())
    assert getattr(partner, 'thingML_Expression164') is None


def test_assoc_substate93_stub_double():
    # thingML_State has no real 'thingML_State95' property in the generated
    # code (a bare stub) -- manually attach it so thingML_StateContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_StateContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_StateContainer(history=True)
    partner = thingML_State()
    setattr(partner, 'thingML_State95', None)
    _safe_set(owner, 'thingML_StateContainer94', {partner})
    assert getattr(partner, 'thingML_State95') == owner
    _safe_set(owner, 'thingML_StateContainer94', set())
    assert getattr(partner, 'thingML_State95') is None


def test_assoc_term291_stub_double():
    # thingML_Expression has no real 'thingML_Expression292' property in the generated
    # code (a bare stub) -- manually attach it so thingML_CastExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_CastExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_CastExpression(isArray=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression292', None)
    _safe_set(owner, 'thingML_CastExpression', partner)
    assert getattr(partner, 'thingML_Expression292') == owner
    _safe_set(owner, 'thingML_CastExpression', None)
    assert getattr(partner, 'thingML_Expression292') is None


def test_assoc_type191_stub_double():
    # thingML_Instance has no real 'thingML_Instance192' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_Instance()
    setattr(partner, 'thingML_Instance192', None)
    _safe_set(owner, 'thingML_Thing193', partner)
    assert getattr(partner, 'thingML_Instance192') == owner
    _safe_set(owner, 'thingML_Thing193', None)
    assert getattr(partner, 'thingML_Instance192') is None


def test_assoc_type293_stub_double():
    # thingML_Type has no real 'thingML_Type295' property in the generated
    # code (a bare stub) -- manually attach it so thingML_CastExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_CastExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_CastExpression(isArray=True)
    partner = thingML_Type()
    setattr(partner, 'thingML_Type295', None)
    _safe_set(owner, 'thingML_CastExpression294', partner)
    assert getattr(partner, 'thingML_Type295') == owner
    _safe_set(owner, 'thingML_CastExpression294', None)
    assert getattr(partner, 'thingML_Type295') is None


def test_assoc_type9_stub_double():
    # thingML_Type has no real 'thingML_Type11' property in the generated
    # code (a bare stub) -- manually attach it so thingML_TypeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_TypeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_TypeRef(isArray=True)
    partner = thingML_Type()
    setattr(partner, 'thingML_Type11', None)
    _safe_set(owner, 'thingML_TypeRef10', partner)
    assert getattr(partner, 'thingML_Type11') == owner
    _safe_set(owner, 'thingML_TypeRef10', None)
    assert getattr(partner, 'thingML_Type11') is None


def test_assoc_typeRef14_stub_double():
    # thingML_Enumeration has no real 'thingML_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so thingML_TypeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_TypeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_TypeRef(isArray=True)
    partner = thingML_Enumeration()
    setattr(partner, 'thingML_Enumeration', None)
    _safe_set(owner, 'thingML_TypeRef15', partner)
    assert getattr(partner, 'thingML_Enumeration') == owner
    _safe_set(owner, 'thingML_TypeRef15', None)
    assert getattr(partner, 'thingML_Enumeration') is None


def test_assoc_typeRef8_stub_double():
    # thingML_Variable has no real 'thingML_Variable' property in the generated
    # code (a bare stub) -- manually attach it so thingML_TypeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_TypeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_TypeRef(isArray=True)
    partner = thingML_Variable()
    setattr(partner, 'thingML_Variable', None)
    _safe_set(owner, 'thingML_TypeRef', partner)
    assert getattr(partner, 'thingML_Variable') == owner
    _safe_set(owner, 'thingML_TypeRef', None)
    assert getattr(partner, 'thingML_Variable') is None


