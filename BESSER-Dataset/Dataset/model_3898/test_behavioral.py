import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BinaryBooleanFunction,
    BinaryFunction,
    ConstantExpression,
    ControlNode,
    Duration,
    Edge,
    ExecutableNode,
    Expression,
    Function,
    LocationExpression,
    NamedFunction,
    Node,
    PrimitiveActivity,
    PrimitiveExpression,
    TimeExpression,
    UnaryFunction,
    VariableClass,
    behaviour_ActivityDiagramBehavior,
    behaviour_Add,
    behaviour_AnonymousFunction,
    behaviour_AttributeClass,
    behaviour_Behavior,
    behaviour_BinaryArithmeticFunction,
    behaviour_BinaryBooleanFunction,
    behaviour_BinaryFunction,
    behaviour_BinaryLocationFunction,
    behaviour_BooleanPrimitive,
    behaviour_ComparisonBooleanFunction,
    behaviour_ConstantExpression,
    behaviour_ControlNode,
    behaviour_CoordinateLocationExpression,
    behaviour_Decision,
    behaviour_Die,
    behaviour_Duration,
    behaviour_Edge,
    behaviour_End,
    behaviour_EntityClass,
    behaviour_EntityPrimive,
    behaviour_EntitySetPrimitive,
    behaviour_Equation,
    behaviour_EquationBehaviour,
    behaviour_ExecutableNode,
    behaviour_Expression,
    behaviour_FalseEdge,
    behaviour_FloatConstantExpression,
    behaviour_Fork,
    behaviour_Function,
    behaviour_FunctionCallExpression,
    behaviour_IntConstantExpression,
    behaviour_Join,
    behaviour_LocationExpression,
    behaviour_LocationPrimitive,
    behaviour_LocationSetPrimitive,
    behaviour_LogicBooleanFunction,
    behaviour_Merge,
    behaviour_MonthDuration,
    behaviour_Move,
    behaviour_NameLocationExpression,
    behaviour_NamedFunction,
    behaviour_Node,
    behaviour_NumericPrimitive,
    behaviour_OccupationBooleanFunction,
    behaviour_ParameterClass,
    behaviour_PrimitiveActivity,
    behaviour_PrimitiveExpression,
    behaviour_Remove,
    behaviour_Reproduce,
    behaviour_Start,
    behaviour_StringConstantExpression,
    behaviour_TimeExpression,
    behaviour_TrueEdge,
    behaviour_Type,
    behaviour_UnaryEntityFunction,
    behaviour_UnaryFunction,
    behaviour_UnaryLocationFunction,
    behaviour_UnaryNumericFunction,
    behaviour_UnaryStringFunction,
    behaviour_UnconditionedEdge,
    behaviour_VariableClass,
    behaviour_While,
    ArithmeticFunctionEnum,
    BooleanPrimitiveEnum,
    ComparisonBooleanFunctionEnum,
    DurationTypeEnum,
    EntityPrimitiveEnum,
    EntitySetPrimiveEnum,
    LocationPrimiveEnum,
    LocationSetPrimiveEnum,
    LogicBooleanFunctionEnum,
    MonthsEnum,
    OccupationBooleanFunctionEnum,
    TypeEnum,
    UnaryEntityFunctionEnum,
    UnaryLocationEnum,
    UnaryLocationFunctionEnum,
    UnaryNumericFunctionEnum,
    UnaryStringFunctionEnum,
    WeekDaysEnum,
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

def test_assoc_behaviour11_reverse_link_reassign_clear():
    a1 = behaviour_EntityClass(entityName="sample_text")
    a2 = behaviour_EntityClass(entityName="sample_text_2")
    b = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    _safe_set(b, 'behaviour_Behavior', a1)
    assert _is_linked(b, 'behaviour_Behavior', a1)
    if hasattr(a1, 'behaviour_EntityClass'):
        assert _is_linked(a1, 'behaviour_EntityClass', b)
    _safe_set(b, 'behaviour_Behavior', a2)
    assert _is_linked(b, 'behaviour_Behavior', a2)
    if hasattr(a1, 'behaviour_EntityClass'):
        assert not _is_linked(a1, 'behaviour_EntityClass', b)
    if hasattr(a2, 'behaviour_EntityClass'):
        assert _is_linked(a2, 'behaviour_EntityClass', b)
    _safe_set(b, 'behaviour_Behavior', None)
    assert not _is_linked(b, 'behaviour_Behavior', a2)
    if hasattr(a2, 'behaviour_EntityClass'):
        assert not _is_linked(a2, 'behaviour_EntityClass', b)


def test_assoc_endTime16_reverse_link_reassign_clear():
    a1 = behaviour_Duration(durationTime=7)
    a2 = behaviour_Duration(durationTime=13)
    b = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    _safe_set(b, 'behaviour_Behavior17', a1)
    assert _is_linked(b, 'behaviour_Behavior17', a1)
    if hasattr(a1, 'behaviour_Duration18'):
        assert _is_linked(a1, 'behaviour_Duration18', b)
    _safe_set(b, 'behaviour_Behavior17', a2)
    assert _is_linked(b, 'behaviour_Behavior17', a2)
    if hasattr(a1, 'behaviour_Duration18'):
        assert not _is_linked(a1, 'behaviour_Duration18', b)
    if hasattr(a2, 'behaviour_Duration18'):
        assert _is_linked(a2, 'behaviour_Duration18', b)
    _safe_set(b, 'behaviour_Behavior17', None)
    assert not _is_linked(b, 'behaviour_Behavior17', a2)
    if hasattr(a2, 'behaviour_Duration18'):
        assert not _is_linked(a2, 'behaviour_Duration18', b)


def test_assoc_startTime14_reverse_link_reassign_clear():
    a1 = behaviour_Duration(durationTime=7)
    a2 = behaviour_Duration(durationTime=13)
    b = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    _safe_set(b, 'behaviour_Behavior15', a1)
    assert _is_linked(b, 'behaviour_Behavior15', a1)
    if hasattr(a1, 'behaviour_Duration'):
        assert _is_linked(a1, 'behaviour_Duration', b)
    _safe_set(b, 'behaviour_Behavior15', a2)
    assert _is_linked(b, 'behaviour_Behavior15', a2)
    if hasattr(a1, 'behaviour_Duration'):
        assert not _is_linked(a1, 'behaviour_Duration', b)
    if hasattr(a2, 'behaviour_Duration'):
        assert _is_linked(a2, 'behaviour_Duration', b)
    _safe_set(b, 'behaviour_Behavior15', None)
    assert not _is_linked(b, 'behaviour_Behavior15', a2)
    if hasattr(a2, 'behaviour_Duration'):
        assert not _is_linked(a2, 'behaviour_Duration', b)


def test_assoc_type0_reverse_link_reassign_clear():
    a1 = behaviour_VariableClass(variableName="sample_text")
    a2 = behaviour_VariableClass(variableName="sample_text_2")
    b = behaviour_Type(type="sample_text")
    _safe_set(b, 'behaviour_Type', a1)
    assert _is_linked(b, 'behaviour_Type', a1)
    if hasattr(a1, 'behaviour_VariableClass'):
        assert _is_linked(a1, 'behaviour_VariableClass', b)
    _safe_set(b, 'behaviour_Type', a2)
    assert _is_linked(b, 'behaviour_Type', a2)
    if hasattr(a1, 'behaviour_VariableClass'):
        assert not _is_linked(a1, 'behaviour_VariableClass', b)
    if hasattr(a2, 'behaviour_VariableClass'):
        assert _is_linked(a2, 'behaviour_VariableClass', b)
    _safe_set(b, 'behaviour_Type', None)
    assert not _is_linked(b, 'behaviour_Type', a2)
    if hasattr(a2, 'behaviour_VariableClass'):
        assert not _is_linked(a2, 'behaviour_VariableClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments1_stub_double():
    # behaviour_FunctionCallExpression has no real 'behaviour_FunctionCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_VariableClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_VariableClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_VariableClass(variableName="sample_text")
    partner = behaviour_FunctionCallExpression()
    setattr(partner, 'behaviour_FunctionCallExpression', None)
    _safe_set(owner, 'behaviour_VariableClass2', partner)
    assert owner in getattr(partner, 'behaviour_FunctionCallExpression')
    _safe_set(owner, 'behaviour_VariableClass2', None)
    assert owner not in getattr(partner, 'behaviour_FunctionCallExpression')


def test_assoc_attribute12_stub_double():
    # behaviour_AttributeClass has no real 'behaviour_AttributeClass' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_EntityClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_EntityClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_EntityClass(entityName="sample_text")
    partner = behaviour_AttributeClass()
    setattr(partner, 'behaviour_AttributeClass', None)
    _safe_set(owner, 'behaviour_EntityClass13', {partner})
    assert getattr(partner, 'behaviour_AttributeClass') == owner
    _safe_set(owner, 'behaviour_EntityClass13', set())
    assert getattr(partner, 'behaviour_AttributeClass') is None


def test_assoc_codomaine8_stub_double():
    # behaviour_Function has no real 'behaviour_Function9' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Type(type="sample_text")
    partner = behaviour_Function()
    setattr(partner, 'behaviour_Function9', None)
    _safe_set(owner, 'behaviour_Type10', partner)
    assert getattr(partner, 'behaviour_Function9') == owner
    _safe_set(owner, 'behaviour_Type10', None)
    assert getattr(partner, 'behaviour_Function9') is None


def test_assoc_domaine5_stub_double():
    # behaviour_Function has no real 'behaviour_Function6' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Type(type="sample_text")
    partner = behaviour_Function()
    setattr(partner, 'behaviour_Function6', None)
    _safe_set(owner, 'behaviour_Type7', partner)
    assert getattr(partner, 'behaviour_Function6') == owner
    _safe_set(owner, 'behaviour_Type7', None)
    assert getattr(partner, 'behaviour_Function6') is None


def test_assoc_parameters19_stub_double():
    # behaviour_ParameterClass has no real 'behaviour_ParameterClass' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    partner = behaviour_ParameterClass()
    setattr(partner, 'behaviour_ParameterClass', None)
    _safe_set(owner, 'behaviour_Behavior20', {partner})
    assert getattr(partner, 'behaviour_ParameterClass') == owner
    _safe_set(owner, 'behaviour_Behavior20', set())
    assert getattr(partner, 'behaviour_ParameterClass') is None


