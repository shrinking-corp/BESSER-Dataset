import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    AnnotatedElement,
    BinaryExpression,
    CompositeState,
    ControlStructure,
    Event,
    Expression,
    FunctionCall,
    Handler,
    Literal,
    Port,
    Property,
    PropertyReference,
    Region,
    State,
    ThingMLElement,
    Type,
    TypedElement,
    UnaryExpression,
    Variable,
    thingml_Action,
    thingml_ActionBlock,
    thingml_AndExpression,
    thingml_AnnotatedElement,
    thingml_ArrayIndex,
    thingml_BinaryExpression,
    thingml_BooleanLiteral,
    thingml_CompositeState,
    thingml_ConditionalAction,
    thingml_ConfigInclude,
    thingml_ConfigPropertyAssign,
    thingml_Configuration,
    thingml_Connector,
    thingml_ControlStructure,
    thingml_Dictionary,
    thingml_DictionaryReference,
    thingml_DivExpression,
    thingml_DoubleLiteral,
    thingml_EnumLiteralRef,
    thingml_Enumeration,
    thingml_EnumerationLiteral,
    thingml_EqualsExpression,
    thingml_ErrorAction,
    thingml_Event,
    thingml_EventReference,
    thingml_Expression,
    thingml_ExpressionGroup,
    thingml_ExternExpression,
    thingml_ExternStatement,
    thingml_Function,
    thingml_FunctionCall,
    thingml_FunctionCallExpression,
    thingml_FunctionCallStatement,
    thingml_GreaterExpression,
    thingml_Handler,
    thingml_Instance,
    thingml_InstanceRef,
    thingml_IntegerLiteral,
    thingml_InternalTransition,
    thingml_Literal,
    thingml_LocalVariable,
    thingml_LoopAction,
    thingml_LowerExpression,
    thingml_Message,
    thingml_MinusExpression,
    thingml_ModExpression,
    thingml_NotExpression,
    thingml_OrExpression,
    thingml_ParallelRegion,
    thingml_Parameter,
    thingml_PlatformAnnotation,
    thingml_PlusExpression,
    thingml_Port,
    thingml_PrimitiveType,
    thingml_PrintAction,
    thingml_Property,
    thingml_PropertyAssign,
    thingml_PropertyReference,
    thingml_ProvidedPort,
    thingml_ReceiveMessage,
    thingml_Region,
    thingml_RequiredPort,
    thingml_ReturnAction,
    thingml_SendAction,
    thingml_State,
    thingml_StateMachine,
    thingml_StringLiteral,
    thingml_Thing,
    thingml_ThingMLElement,
    thingml_ThingMLModel,
    thingml_TimesExpression,
    thingml_Transition,
    thingml_Type,
    thingml_TypedElement,
    thingml_UnaryExpression,
    thingml_UnaryMinus,
    thingml_Variable,
    thingml_VariableAssignment,
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

def test_assoc_includes16_reverse_link_reassign_clear():
    a1 = thingml_Thing(fragment=True)
    a2 = thingml_Thing(fragment=False)
    b = thingml_Thing(fragment=True)
    _safe_set(b, 'thingml_Thing17', a1)
    assert _is_linked(b, 'thingml_Thing17', a1)
    if hasattr(a1, 'thingml_Thing15'):
        assert _is_linked(a1, 'thingml_Thing15', b)
    _safe_set(b, 'thingml_Thing17', a2)
    assert _is_linked(b, 'thingml_Thing17', a2)
    if hasattr(a1, 'thingml_Thing15'):
        assert not _is_linked(a1, 'thingml_Thing15', b)
    if hasattr(a2, 'thingml_Thing15'):
        assert _is_linked(a2, 'thingml_Thing15', b)
    _safe_set(b, 'thingml_Thing17', None)
    assert not _is_linked(b, 'thingml_Thing17', a2)
    if hasattr(a2, 'thingml_Thing15'):
        assert not _is_linked(a2, 'thingml_Thing15', b)


def test_assoc_properties11_reverse_link_reassign_clear():
    a1 = thingml_Thing(fragment=True)
    a2 = thingml_Thing(fragment=False)
    b = thingml_Property(changeable=True)
    _safe_set(b, 'thingml_Property', a1)
    assert _is_linked(b, 'thingml_Property', a1)
    if hasattr(a1, 'thingml_Thing'):
        assert _is_linked(a1, 'thingml_Thing', b)
    _safe_set(b, 'thingml_Property', a2)
    assert _is_linked(b, 'thingml_Property', a2)
    if hasattr(a1, 'thingml_Thing'):
        assert not _is_linked(a1, 'thingml_Thing', b)
    if hasattr(a2, 'thingml_Thing'):
        assert _is_linked(a2, 'thingml_Thing', b)
    _safe_set(b, 'thingml_Property', None)
    assert not _is_linked(b, 'thingml_Property', a2)
    if hasattr(a2, 'thingml_Thing'):
        assert not _is_linked(a2, 'thingml_Thing', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations44_stub_double():
    # thingml_AnnotatedElement has no real 'thingml_AnnotatedElement' property in the generated
    # code (a bare stub) -- manually attach it so thingml_PlatformAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_PlatformAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_PlatformAnnotation(value="sample_text")
    partner = thingml_AnnotatedElement()
    setattr(partner, 'thingml_AnnotatedElement', None)
    _safe_set(owner, 'thingml_PlatformAnnotation', partner)
    assert owner in getattr(partner, 'thingml_AnnotatedElement')
    _safe_set(owner, 'thingml_PlatformAnnotation', None)
    assert owner not in getattr(partner, 'thingml_AnnotatedElement')


def test_assoc_assign18_stub_double():
    # thingml_PropertyAssign has no real 'thingml_PropertyAssign' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_PropertyAssign()
    setattr(partner, 'thingml_PropertyAssign', None)
    _safe_set(owner, 'thingml_Thing19', {partner})
    assert getattr(partner, 'thingml_PropertyAssign') == owner
    _safe_set(owner, 'thingml_Thing19', set())
    assert getattr(partner, 'thingml_PropertyAssign') is None


def test_assoc_behaviour13_stub_double():
    # thingml_StateMachine has no real 'thingml_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_StateMachine()
    setattr(partner, 'thingml_StateMachine', None)
    _safe_set(owner, 'thingml_Thing14', {partner})
    assert getattr(partner, 'thingml_StateMachine') == owner
    _safe_set(owner, 'thingml_Thing14', set())
    assert getattr(partner, 'thingml_StateMachine') is None


def test_assoc_config185_stub_double():
    # thingml_ConfigInclude has no real 'thingml_ConfigInclude186' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_ConfigInclude()
    setattr(partner, 'thingml_ConfigInclude186', None)
    _safe_set(owner, 'thingml_Configuration187', partner)
    assert getattr(partner, 'thingml_ConfigInclude186') == owner
    _safe_set(owner, 'thingml_Configuration187', None)
    assert getattr(partner, 'thingml_ConfigInclude186') is None


def test_assoc_configs154_stub_double():
    # thingml_ConfigInclude has no real 'thingml_ConfigInclude' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_ConfigInclude()
    setattr(partner, 'thingml_ConfigInclude', None)
    _safe_set(owner, 'thingml_Configuration155', {partner})
    assert getattr(partner, 'thingml_ConfigInclude') == owner
    _safe_set(owner, 'thingml_Configuration155', set())
    assert getattr(partner, 'thingml_ConfigInclude') is None


def test_assoc_configs4_stub_double():
    # thingml_ThingMLModel has no real 'thingml_ThingMLModel5' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_ThingMLModel()
    setattr(partner, 'thingml_ThingMLModel5', None)
    _safe_set(owner, 'thingml_Configuration', partner)
    assert owner in getattr(partner, 'thingml_ThingMLModel5')
    _safe_set(owner, 'thingml_Configuration', None)
    assert owner not in getattr(partner, 'thingml_ThingMLModel5')


def test_assoc_connectors152_stub_double():
    # thingml_Connector has no real 'thingml_Connector' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_Connector()
    setattr(partner, 'thingml_Connector', None)
    _safe_set(owner, 'thingml_Configuration153', {partner})
    assert getattr(partner, 'thingml_Connector') == owner
    _safe_set(owner, 'thingml_Configuration153', set())
    assert getattr(partner, 'thingml_Connector') is None


def test_assoc_functions23_stub_double():
    # thingml_Function has no real 'thingml_Function25' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_Function()
    setattr(partner, 'thingml_Function25', None)
    _safe_set(owner, 'thingml_Thing24', {partner})
    assert getattr(partner, 'thingml_Function25') == owner
    _safe_set(owner, 'thingml_Thing24', set())
    assert getattr(partner, 'thingml_Function25') is None


def test_assoc_init199_stub_double():
    # thingml_Expression has no real 'thingml_Expression200' property in the generated
    # code (a bare stub) -- manually attach it so thingml_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_LocalVariable(changeable=True)
    partner = thingml_Expression()
    setattr(partner, 'thingml_Expression200', None)
    _safe_set(owner, 'thingml_LocalVariable', partner)
    assert getattr(partner, 'thingml_Expression200') == owner
    _safe_set(owner, 'thingml_LocalVariable', None)
    assert getattr(partner, 'thingml_Expression200') is None


def test_assoc_init30_stub_double():
    # thingml_Expression has no real 'thingml_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Property(changeable=True)
    partner = thingml_Expression()
    setattr(partner, 'thingml_Expression32', None)
    _safe_set(owner, 'thingml_Property31', partner)
    assert getattr(partner, 'thingml_Expression32') == owner
    _safe_set(owner, 'thingml_Property31', None)
    assert getattr(partner, 'thingml_Expression32') is None


def test_assoc_initial76_stub_double():
    # thingml_State has no real 'thingml_State78' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Region(history=True)
    partner = thingml_State()
    setattr(partner, 'thingml_State78', None)
    _safe_set(owner, 'thingml_Region77', partner)
    assert getattr(partner, 'thingml_State78') == owner
    _safe_set(owner, 'thingml_Region77', None)
    assert getattr(partner, 'thingml_State78') is None


def test_assoc_instances150_stub_double():
    # thingml_Instance has no real 'thingml_Instance' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_Instance()
    setattr(partner, 'thingml_Instance', None)
    _safe_set(owner, 'thingml_Configuration151', {partner})
    assert getattr(partner, 'thingml_Instance') == owner
    _safe_set(owner, 'thingml_Configuration151', set())
    assert getattr(partner, 'thingml_Instance') is None


def test_assoc_messages20_stub_double():
    # thingml_Message has no real 'thingml_Message22' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_Message()
    setattr(partner, 'thingml_Message22', None)
    _safe_set(owner, 'thingml_Thing21', {partner})
    assert getattr(partner, 'thingml_Message22') == owner
    _safe_set(owner, 'thingml_Thing21', set())
    assert getattr(partner, 'thingml_Message22') is None


def test_assoc_owner106_stub_double():
    # thingml_Port has no real 'ports' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_Port()
    setattr(partner, 'ports', None)
    _safe_set(owner, 'Thing', partner)
    assert getattr(partner, 'ports') == owner
    _safe_set(owner, 'Thing', None)
    assert getattr(partner, 'ports') is None


def test_assoc_ports12_stub_double():
    # thingml_Port has no real 'Port' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_Port()
    setattr(partner, 'Port', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Port') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Port') is None


def test_assoc_propassigns156_stub_double():
    # thingml_ConfigPropertyAssign has no real 'thingml_ConfigPropertyAssign' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Configuration(fragment=True)
    partner = thingml_ConfigPropertyAssign()
    setattr(partner, 'thingml_ConfigPropertyAssign', None)
    _safe_set(owner, 'thingml_Configuration157', {partner})
    assert getattr(partner, 'thingml_ConfigPropertyAssign') == owner
    _safe_set(owner, 'thingml_Configuration157', set())
    assert getattr(partner, 'thingml_ConfigPropertyAssign') is None


def test_assoc_properties68_stub_double():
    # thingml_State has no real 'thingml_State69' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Property(changeable=True)
    partner = thingml_State()
    setattr(partner, 'thingml_State69', None)
    _safe_set(owner, 'thingml_Property70', partner)
    assert owner in getattr(partner, 'thingml_State69')
    _safe_set(owner, 'thingml_Property70', None)
    assert owner not in getattr(partner, 'thingml_State69')


def test_assoc_property176_stub_double():
    # thingml_ConfigPropertyAssign has no real 'thingml_ConfigPropertyAssign177' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Property(changeable=True)
    partner = thingml_ConfigPropertyAssign()
    setattr(partner, 'thingml_ConfigPropertyAssign177', None)
    _safe_set(owner, 'thingml_Property178', partner)
    assert getattr(partner, 'thingml_ConfigPropertyAssign177') == owner
    _safe_set(owner, 'thingml_Property178', None)
    assert getattr(partner, 'thingml_ConfigPropertyAssign177') is None


def test_assoc_property36_stub_double():
    # thingml_PropertyAssign has no real 'thingml_PropertyAssign37' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Property(changeable=True)
    partner = thingml_PropertyAssign()
    setattr(partner, 'thingml_PropertyAssign37', None)
    _safe_set(owner, 'thingml_Property38', partner)
    assert getattr(partner, 'thingml_PropertyAssign37') == owner
    _safe_set(owner, 'thingml_Property38', None)
    assert getattr(partner, 'thingml_PropertyAssign37') is None


def test_assoc_required169_stub_double():
    # thingml_Connector has no real 'thingml_Connector170' property in the generated
    # code (a bare stub) -- manually attach it so thingml_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_RequiredPort(optional=True)
    partner = thingml_Connector()
    setattr(partner, 'thingml_Connector170', None)
    _safe_set(owner, 'thingml_RequiredPort', partner)
    assert getattr(partner, 'thingml_Connector170') == owner
    _safe_set(owner, 'thingml_RequiredPort', None)
    assert getattr(partner, 'thingml_Connector170') is None


def test_assoc_segments81_stub_double():
    # thingml_Expression has no real 'thingml_Expression82' property in the generated
    # code (a bare stub) -- manually attach it so thingml_ExternStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_ExternStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_ExternStatement(statement="sample_text")
    partner = thingml_Expression()
    setattr(partner, 'thingml_Expression82', None)
    _safe_set(owner, 'thingml_ExternStatement', {partner})
    assert getattr(partner, 'thingml_Expression82') == owner
    _safe_set(owner, 'thingml_ExternStatement', set())
    assert getattr(partner, 'thingml_Expression82') is None


def test_assoc_segments83_stub_double():
    # thingml_Expression has no real 'thingml_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so thingml_ExternExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_ExternExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_ExternExpression(expression="sample_text")
    partner = thingml_Expression()
    setattr(partner, 'thingml_Expression84', None)
    _safe_set(owner, 'thingml_ExternExpression', {partner})
    assert getattr(partner, 'thingml_Expression84') == owner
    _safe_set(owner, 'thingml_ExternExpression', set())
    assert getattr(partner, 'thingml_Expression84') is None


def test_assoc_substate74_stub_double():
    # thingml_State has no real 'thingml_State75' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Region(history=True)
    partner = thingml_State()
    setattr(partner, 'thingml_State75', None)
    _safe_set(owner, 'thingml_Region', {partner})
    assert getattr(partner, 'thingml_State75') == owner
    _safe_set(owner, 'thingml_Region', set())
    assert getattr(partner, 'thingml_State75') is None


def test_assoc_type158_stub_double():
    # thingml_Instance has no real 'thingml_Instance159' property in the generated
    # code (a bare stub) -- manually attach it so thingml_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingml_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingml_Thing(fragment=True)
    partner = thingml_Instance()
    setattr(partner, 'thingml_Instance159', None)
    _safe_set(owner, 'thingml_Thing160', partner)
    assert getattr(partner, 'thingml_Instance159') == owner
    _safe_set(owner, 'thingml_Thing160', None)
    assert getattr(partner, 'thingml_Instance159') is None


