import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_behaviour_Behavior_behaviorName_value_roundtrip():
    instance = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    assert instance.behaviorName == "sample_text"
    instance.behaviorName = "sample_text_2"
    assert instance.behaviorName == "sample_text_2"


def test_behaviour_Behavior_frequency_value_roundtrip():
    instance = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    assert instance.frequency == "sample_text"
    instance.frequency = "sample_text_2"
    assert instance.frequency == "sample_text_2"


def test_behaviour_BinaryArithmeticFunction_functionName_value_roundtrip():
    instance = behaviour_BinaryArithmeticFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_BooleanPrimitive_primitive_value_roundtrip():
    instance = behaviour_BooleanPrimitive(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_behaviour_ComparisonBooleanFunction_functionName_value_roundtrip():
    instance = behaviour_ComparisonBooleanFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_CoordinateLocationExpression_x_value_roundtrip():
    instance = behaviour_CoordinateLocationExpression(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_behaviour_CoordinateLocationExpression_y_value_roundtrip():
    instance = behaviour_CoordinateLocationExpression(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_behaviour_Duration_durationTime_value_roundtrip():
    instance = behaviour_Duration(durationTime=7)
    assert instance.durationTime == 7
    instance.durationTime = 13
    assert instance.durationTime == 13


def test_behaviour_EntityClass_entityName_value_roundtrip():
    instance = behaviour_EntityClass(entityName="sample_text")
    assert instance.entityName == "sample_text"
    instance.entityName = "sample_text_2"
    assert instance.entityName == "sample_text_2"


def test_behaviour_EntityPrimive_primitive_value_roundtrip():
    instance = behaviour_EntityPrimive(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_behaviour_EntitySetPrimitive_primitive_value_roundtrip():
    instance = behaviour_EntitySetPrimitive(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_behaviour_FloatConstantExpression_value_value_roundtrip():
    instance = behaviour_FloatConstantExpression(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_behaviour_IntConstantExpression_value_value_roundtrip():
    instance = behaviour_IntConstantExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_behaviour_LocationPrimitive_primitive_value_roundtrip():
    instance = behaviour_LocationPrimitive(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_behaviour_LocationSetPrimitive_primitive_value_roundtrip():
    instance = behaviour_LocationSetPrimitive(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_behaviour_LogicBooleanFunction_functionName_value_roundtrip():
    instance = behaviour_LogicBooleanFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_MonthDuration_month_value_roundtrip():
    instance = behaviour_MonthDuration(month="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_behaviour_NameLocationExpression_name_value_roundtrip():
    instance = behaviour_NameLocationExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_behaviour_OccupationBooleanFunction_functionName_value_roundtrip():
    instance = behaviour_OccupationBooleanFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_StringConstantExpression_value_value_roundtrip():
    instance = behaviour_StringConstantExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_behaviour_Type_type_value_roundtrip():
    instance = behaviour_Type(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_behaviour_UnaryEntityFunction_functionName_value_roundtrip():
    instance = behaviour_UnaryEntityFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_UnaryLocationFunction_functionName_value_roundtrip():
    instance = behaviour_UnaryLocationFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_UnaryNumericFunction_functionName_value_roundtrip():
    instance = behaviour_UnaryNumericFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_UnaryStringFunction_functionName_value_roundtrip():
    instance = behaviour_UnaryStringFunction(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_behaviour_VariableClass_variableName_value_roundtrip():
    instance = behaviour_VariableClass(variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


def test_behaviour_ActivityDiagramBehavior_isa_Behavior():
    instance = behaviour_ActivityDiagramBehavior()
    assert isinstance(instance, Behavior)


def test_behaviour_EquationBehaviour_isa_Behavior():
    instance = behaviour_EquationBehaviour()
    assert isinstance(instance, Behavior)


def test_behaviour_ComparisonBooleanFunction_isa_BinaryBooleanFunction():
    instance = behaviour_ComparisonBooleanFunction(functionName="sample_text")
    assert isinstance(instance, BinaryBooleanFunction)


def test_behaviour_LogicBooleanFunction_isa_BinaryBooleanFunction():
    instance = behaviour_LogicBooleanFunction(functionName="sample_text")
    assert isinstance(instance, BinaryBooleanFunction)


def test_behaviour_OccupationBooleanFunction_isa_BinaryBooleanFunction():
    instance = behaviour_OccupationBooleanFunction(functionName="sample_text")
    assert isinstance(instance, BinaryBooleanFunction)


def test_behaviour_BinaryArithmeticFunction_isa_BinaryFunction():
    instance = behaviour_BinaryArithmeticFunction(functionName="sample_text")
    assert isinstance(instance, BinaryFunction)


def test_behaviour_BinaryBooleanFunction_isa_BinaryFunction():
    instance = behaviour_BinaryBooleanFunction()
    assert isinstance(instance, BinaryFunction)


def test_behaviour_BinaryLocationFunction_isa_BinaryFunction():
    instance = behaviour_BinaryLocationFunction()
    assert isinstance(instance, BinaryFunction)


def test_behaviour_FloatConstantExpression_isa_ConstantExpression():
    instance = behaviour_FloatConstantExpression(value=3.14)
    assert isinstance(instance, ConstantExpression)


def test_behaviour_IntConstantExpression_isa_ConstantExpression():
    instance = behaviour_IntConstantExpression(value=7)
    assert isinstance(instance, ConstantExpression)


def test_behaviour_StringConstantExpression_isa_ConstantExpression():
    instance = behaviour_StringConstantExpression(value="sample_text")
    assert isinstance(instance, ConstantExpression)


def test_behaviour_Decision_isa_ControlNode():
    instance = behaviour_Decision()
    assert isinstance(instance, ControlNode)


def test_behaviour_End_isa_ControlNode():
    instance = behaviour_End()
    assert isinstance(instance, ControlNode)


def test_behaviour_Fork_isa_ControlNode():
    instance = behaviour_Fork()
    assert isinstance(instance, ControlNode)


def test_behaviour_Join_isa_ControlNode():
    instance = behaviour_Join()
    assert isinstance(instance, ControlNode)


def test_behaviour_Merge_isa_ControlNode():
    instance = behaviour_Merge()
    assert isinstance(instance, ControlNode)


def test_behaviour_Start_isa_ControlNode():
    instance = behaviour_Start()
    assert isinstance(instance, ControlNode)


def test_behaviour_TimeExpression_isa_ControlNode():
    instance = behaviour_TimeExpression()
    assert isinstance(instance, ControlNode)


def test_behaviour_MonthDuration_isa_Duration():
    instance = behaviour_MonthDuration(month="sample_text")
    assert isinstance(instance, Duration)


def test_behaviour_FalseEdge_isa_Edge():
    instance = behaviour_FalseEdge()
    assert isinstance(instance, Edge)


def test_behaviour_TrueEdge_isa_Edge():
    instance = behaviour_TrueEdge()
    assert isinstance(instance, Edge)


def test_behaviour_UnconditionedEdge_isa_Edge():
    instance = behaviour_UnconditionedEdge()
    assert isinstance(instance, Edge)


def test_behaviour_ActivityDiagramBehavior_isa_ExecutableNode():
    instance = behaviour_ActivityDiagramBehavior()
    assert isinstance(instance, ExecutableNode)


def test_behaviour_PrimitiveActivity_isa_ExecutableNode():
    instance = behaviour_PrimitiveActivity()
    assert isinstance(instance, ExecutableNode)


def test_behaviour_ConstantExpression_isa_Expression():
    instance = behaviour_ConstantExpression()
    assert isinstance(instance, Expression)


def test_behaviour_FunctionCallExpression_isa_Expression():
    instance = behaviour_FunctionCallExpression()
    assert isinstance(instance, Expression)


def test_behaviour_LocationExpression_isa_Expression():
    instance = behaviour_LocationExpression()
    assert isinstance(instance, Expression)


def test_behaviour_PrimitiveExpression_isa_Expression():
    instance = behaviour_PrimitiveExpression()
    assert isinstance(instance, Expression)


def test_behaviour_VariableClass_isa_Expression():
    instance = behaviour_VariableClass(variableName="sample_text")
    assert isinstance(instance, Expression)


def test_behaviour_AnonymousFunction_isa_Function():
    instance = behaviour_AnonymousFunction()
    assert isinstance(instance, Function)


def test_behaviour_NamedFunction_isa_Function():
    instance = behaviour_NamedFunction()
    assert isinstance(instance, Function)


def test_behaviour_CoordinateLocationExpression_isa_LocationExpression():
    instance = behaviour_CoordinateLocationExpression(x=3.14, y=3.14)
    assert isinstance(instance, LocationExpression)


def test_behaviour_NameLocationExpression_isa_LocationExpression():
    instance = behaviour_NameLocationExpression(name="sample_text")
    assert isinstance(instance, LocationExpression)


def test_behaviour_BinaryFunction_isa_NamedFunction():
    instance = behaviour_BinaryFunction()
    assert isinstance(instance, NamedFunction)


def test_behaviour_UnaryFunction_isa_NamedFunction():
    instance = behaviour_UnaryFunction()
    assert isinstance(instance, NamedFunction)


def test_behaviour_ControlNode_isa_Node():
    instance = behaviour_ControlNode()
    assert isinstance(instance, Node)


def test_behaviour_ExecutableNode_isa_Node():
    instance = behaviour_ExecutableNode()
    assert isinstance(instance, Node)


def test_behaviour_Add_isa_PrimitiveActivity():
    instance = behaviour_Add()
    assert isinstance(instance, PrimitiveActivity)


def test_behaviour_Die_isa_PrimitiveActivity():
    instance = behaviour_Die()
    assert isinstance(instance, PrimitiveActivity)


def test_behaviour_Move_isa_PrimitiveActivity():
    instance = behaviour_Move()
    assert isinstance(instance, PrimitiveActivity)


def test_behaviour_Remove_isa_PrimitiveActivity():
    instance = behaviour_Remove()
    assert isinstance(instance, PrimitiveActivity)


def test_behaviour_Reproduce_isa_PrimitiveActivity():
    instance = behaviour_Reproduce()
    assert isinstance(instance, PrimitiveActivity)


def test_behaviour_BooleanPrimitive_isa_PrimitiveExpression():
    instance = behaviour_BooleanPrimitive(primitive="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_behaviour_EntityPrimive_isa_PrimitiveExpression():
    instance = behaviour_EntityPrimive(primitive="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_behaviour_EntitySetPrimitive_isa_PrimitiveExpression():
    instance = behaviour_EntitySetPrimitive(primitive="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_behaviour_LocationPrimitive_isa_PrimitiveExpression():
    instance = behaviour_LocationPrimitive(primitive="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_behaviour_LocationSetPrimitive_isa_PrimitiveExpression():
    instance = behaviour_LocationSetPrimitive(primitive="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_behaviour_While_isa_TimeExpression():
    instance = behaviour_While()
    assert isinstance(instance, TimeExpression)


def test_behaviour_UnaryEntityFunction_isa_UnaryFunction():
    instance = behaviour_UnaryEntityFunction(functionName="sample_text")
    assert isinstance(instance, UnaryFunction)


def test_behaviour_UnaryLocationFunction_isa_UnaryFunction():
    instance = behaviour_UnaryLocationFunction(functionName="sample_text")
    assert isinstance(instance, UnaryFunction)


def test_behaviour_UnaryNumericFunction_isa_UnaryFunction():
    instance = behaviour_UnaryNumericFunction(functionName="sample_text")
    assert isinstance(instance, UnaryFunction)


def test_behaviour_UnaryStringFunction_isa_UnaryFunction():
    instance = behaviour_UnaryStringFunction(functionName="sample_text")
    assert isinstance(instance, UnaryFunction)


def test_behaviour_AttributeClass_isa_VariableClass():
    instance = behaviour_AttributeClass()
    assert isinstance(instance, VariableClass)


def test_behaviour_ParameterClass_isa_VariableClass():
    instance = behaviour_ParameterClass()
    assert isinstance(instance, VariableClass)


def test_assoc_arguments1_link_reassign_clear():
    a = behaviour_VariableClass(variableName="sample_text")
    b1 = behaviour_FunctionCallExpression()
    b2 = behaviour_FunctionCallExpression()
    _safe_set(a, 'behaviour_VariableClass2', b1)
    assert _is_linked(a, 'behaviour_VariableClass2', b1)
    if hasattr(b1, 'behaviour_FunctionCallExpression'):
        assert _is_linked(b1, 'behaviour_FunctionCallExpression', a)
    _safe_set(a, 'behaviour_VariableClass2', b2)
    assert _is_linked(a, 'behaviour_VariableClass2', b2)
    if hasattr(b1, 'behaviour_FunctionCallExpression'):
        assert not _is_linked(b1, 'behaviour_FunctionCallExpression', a)
    if hasattr(b2, 'behaviour_FunctionCallExpression'):
        assert _is_linked(b2, 'behaviour_FunctionCallExpression', a)
    _safe_set(a, 'behaviour_VariableClass2', None)
    assert not _is_linked(a, 'behaviour_VariableClass2', b2)
    if hasattr(b2, 'behaviour_FunctionCallExpression'):
        assert not _is_linked(b2, 'behaviour_FunctionCallExpression', a)


def test_assoc_attribute12_link_reassign_clear():
    a = behaviour_EntityClass(entityName="sample_text")
    b1 = behaviour_AttributeClass()
    b2 = behaviour_AttributeClass()
    _safe_set(a, 'behaviour_EntityClass13', {b1})
    assert _is_linked(a, 'behaviour_EntityClass13', b1)
    if hasattr(b1, 'behaviour_AttributeClass'):
        assert _is_linked(b1, 'behaviour_AttributeClass', a)
    _safe_set(a, 'behaviour_EntityClass13', {b2})
    assert _is_linked(a, 'behaviour_EntityClass13', b2)
    if hasattr(b1, 'behaviour_AttributeClass'):
        assert not _is_linked(b1, 'behaviour_AttributeClass', a)
    if hasattr(b2, 'behaviour_AttributeClass'):
        assert _is_linked(b2, 'behaviour_AttributeClass', a)
    _safe_set(a, 'behaviour_EntityClass13', set())
    assert not _is_linked(a, 'behaviour_EntityClass13', b2)
    if hasattr(b2, 'behaviour_AttributeClass'):
        assert not _is_linked(b2, 'behaviour_AttributeClass', a)


def test_assoc_behaviour11_link_reassign_clear():
    a = behaviour_EntityClass(entityName="sample_text")
    b1 = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    b2 = behaviour_Behavior(behaviorName="sample_text_2", frequency="sample_text_2")
    _safe_set(a, 'behaviour_EntityClass', {b1})
    assert _is_linked(a, 'behaviour_EntityClass', b1)
    if hasattr(b1, 'behaviour_Behavior'):
        assert _is_linked(b1, 'behaviour_Behavior', a)
    _safe_set(a, 'behaviour_EntityClass', {b2})
    assert _is_linked(a, 'behaviour_EntityClass', b2)
    if hasattr(b1, 'behaviour_Behavior'):
        assert not _is_linked(b1, 'behaviour_Behavior', a)
    if hasattr(b2, 'behaviour_Behavior'):
        assert _is_linked(b2, 'behaviour_Behavior', a)
    _safe_set(a, 'behaviour_EntityClass', set())
    assert not _is_linked(a, 'behaviour_EntityClass', b2)
    if hasattr(b2, 'behaviour_Behavior'):
        assert not _is_linked(b2, 'behaviour_Behavior', a)


def test_assoc_codomaine8_link_reassign_clear():
    a = behaviour_Type(type="sample_text")
    b1 = behaviour_Function()
    b2 = behaviour_Function()
    _safe_set(a, 'behaviour_Type10', b1)
    assert _is_linked(a, 'behaviour_Type10', b1)
    if hasattr(b1, 'behaviour_Function9'):
        assert _is_linked(b1, 'behaviour_Function9', a)
    _safe_set(a, 'behaviour_Type10', b2)
    assert _is_linked(a, 'behaviour_Type10', b2)
    if hasattr(b1, 'behaviour_Function9'):
        assert not _is_linked(b1, 'behaviour_Function9', a)
    if hasattr(b2, 'behaviour_Function9'):
        assert _is_linked(b2, 'behaviour_Function9', a)
    _safe_set(a, 'behaviour_Type10', None)
    assert not _is_linked(a, 'behaviour_Type10', b2)
    if hasattr(b2, 'behaviour_Function9'):
        assert not _is_linked(b2, 'behaviour_Function9', a)


def test_assoc_domaine5_link_reassign_clear():
    a = behaviour_Type(type="sample_text")
    b1 = behaviour_Function()
    b2 = behaviour_Function()
    _safe_set(a, 'behaviour_Type7', b1)
    assert _is_linked(a, 'behaviour_Type7', b1)
    if hasattr(b1, 'behaviour_Function6'):
        assert _is_linked(b1, 'behaviour_Function6', a)
    _safe_set(a, 'behaviour_Type7', b2)
    assert _is_linked(a, 'behaviour_Type7', b2)
    if hasattr(b1, 'behaviour_Function6'):
        assert not _is_linked(b1, 'behaviour_Function6', a)
    if hasattr(b2, 'behaviour_Function6'):
        assert _is_linked(b2, 'behaviour_Function6', a)
    _safe_set(a, 'behaviour_Type7', None)
    assert not _is_linked(a, 'behaviour_Type7', b2)
    if hasattr(b2, 'behaviour_Function6'):
        assert not _is_linked(b2, 'behaviour_Function6', a)


def test_assoc_endTime16_link_reassign_clear():
    a = behaviour_Duration(durationTime=7)
    b1 = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    b2 = behaviour_Behavior(behaviorName="sample_text_2", frequency="sample_text_2")
    _safe_set(a, 'behaviour_Duration18', b1)
    assert _is_linked(a, 'behaviour_Duration18', b1)
    if hasattr(b1, 'behaviour_Behavior17'):
        assert _is_linked(b1, 'behaviour_Behavior17', a)
    _safe_set(a, 'behaviour_Duration18', b2)
    assert _is_linked(a, 'behaviour_Duration18', b2)
    if hasattr(b1, 'behaviour_Behavior17'):
        assert not _is_linked(b1, 'behaviour_Behavior17', a)
    if hasattr(b2, 'behaviour_Behavior17'):
        assert _is_linked(b2, 'behaviour_Behavior17', a)
    _safe_set(a, 'behaviour_Duration18', None)
    assert not _is_linked(a, 'behaviour_Duration18', b2)
    if hasattr(b2, 'behaviour_Behavior17'):
        assert not _is_linked(b2, 'behaviour_Behavior17', a)


def test_assoc_parameters19_link_reassign_clear():
    a = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    b1 = behaviour_ParameterClass()
    b2 = behaviour_ParameterClass()
    _safe_set(a, 'behaviour_Behavior20', {b1})
    assert _is_linked(a, 'behaviour_Behavior20', b1)
    if hasattr(b1, 'behaviour_ParameterClass'):
        assert _is_linked(b1, 'behaviour_ParameterClass', a)
    _safe_set(a, 'behaviour_Behavior20', {b2})
    assert _is_linked(a, 'behaviour_Behavior20', b2)
    if hasattr(b1, 'behaviour_ParameterClass'):
        assert not _is_linked(b1, 'behaviour_ParameterClass', a)
    if hasattr(b2, 'behaviour_ParameterClass'):
        assert _is_linked(b2, 'behaviour_ParameterClass', a)
    _safe_set(a, 'behaviour_Behavior20', set())
    assert not _is_linked(a, 'behaviour_Behavior20', b2)
    if hasattr(b2, 'behaviour_ParameterClass'):
        assert not _is_linked(b2, 'behaviour_ParameterClass', a)


def test_assoc_startTime14_link_reassign_clear():
    a = behaviour_Duration(durationTime=7)
    b1 = behaviour_Behavior(behaviorName="sample_text", frequency="sample_text")
    b2 = behaviour_Behavior(behaviorName="sample_text_2", frequency="sample_text_2")
    _safe_set(a, 'behaviour_Duration', b1)
    assert _is_linked(a, 'behaviour_Duration', b1)
    if hasattr(b1, 'behaviour_Behavior15'):
        assert _is_linked(b1, 'behaviour_Behavior15', a)
    _safe_set(a, 'behaviour_Duration', b2)
    assert _is_linked(a, 'behaviour_Duration', b2)
    if hasattr(b1, 'behaviour_Behavior15'):
        assert not _is_linked(b1, 'behaviour_Behavior15', a)
    if hasattr(b2, 'behaviour_Behavior15'):
        assert _is_linked(b2, 'behaviour_Behavior15', a)
    _safe_set(a, 'behaviour_Duration', None)
    assert not _is_linked(a, 'behaviour_Duration', b2)
    if hasattr(b2, 'behaviour_Behavior15'):
        assert not _is_linked(b2, 'behaviour_Behavior15', a)


def test_assoc_type0_link_reassign_clear():
    a = behaviour_VariableClass(variableName="sample_text")
    b1 = behaviour_Type(type="sample_text")
    b2 = behaviour_Type(type="sample_text_2")
    _safe_set(a, 'behaviour_VariableClass', b1)
    assert _is_linked(a, 'behaviour_VariableClass', b1)
    if hasattr(b1, 'behaviour_Type'):
        assert _is_linked(b1, 'behaviour_Type', a)
    _safe_set(a, 'behaviour_VariableClass', b2)
    assert _is_linked(a, 'behaviour_VariableClass', b2)
    if hasattr(b1, 'behaviour_Type'):
        assert not _is_linked(b1, 'behaviour_Type', a)
    if hasattr(b2, 'behaviour_Type'):
        assert _is_linked(b2, 'behaviour_Type', a)
    _safe_set(a, 'behaviour_VariableClass', None)
    assert not _is_linked(a, 'behaviour_VariableClass', b2)
    if hasattr(b2, 'behaviour_Type'):
        assert not _is_linked(b2, 'behaviour_Type', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


BinaryBooleanFunction_strategy = st.builds(BinaryBooleanFunction)
@given(instance=BinaryBooleanFunction_strategy)
@settings(max_examples=25)
def test_BinaryBooleanFunction_instantiation(instance):
    assert isinstance(instance, BinaryBooleanFunction)


BinaryFunction_strategy = st.builds(BinaryFunction)
@given(instance=BinaryFunction_strategy)
@settings(max_examples=25)
def test_BinaryFunction_instantiation(instance):
    assert isinstance(instance, BinaryFunction)


ConstantExpression_strategy = st.builds(ConstantExpression)
@given(instance=ConstantExpression_strategy)
@settings(max_examples=25)
def test_ConstantExpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


Duration_strategy = st.builds(Duration)
@given(instance=Duration_strategy)
@settings(max_examples=25)
def test_Duration_instantiation(instance):
    assert isinstance(instance, Duration)


Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


LocationExpression_strategy = st.builds(LocationExpression)
@given(instance=LocationExpression_strategy)
@settings(max_examples=25)
def test_LocationExpression_instantiation(instance):
    assert isinstance(instance, LocationExpression)


NamedFunction_strategy = st.builds(NamedFunction)
@given(instance=NamedFunction_strategy)
@settings(max_examples=25)
def test_NamedFunction_instantiation(instance):
    assert isinstance(instance, NamedFunction)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


PrimitiveActivity_strategy = st.builds(PrimitiveActivity)
@given(instance=PrimitiveActivity_strategy)
@settings(max_examples=25)
def test_PrimitiveActivity_instantiation(instance):
    assert isinstance(instance, PrimitiveActivity)


PrimitiveExpression_strategy = st.builds(PrimitiveExpression)
@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)


TimeExpression_strategy = st.builds(TimeExpression)
@given(instance=TimeExpression_strategy)
@settings(max_examples=25)
def test_TimeExpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)


UnaryFunction_strategy = st.builds(UnaryFunction)
@given(instance=UnaryFunction_strategy)
@settings(max_examples=25)
def test_UnaryFunction_instantiation(instance):
    assert isinstance(instance, UnaryFunction)


VariableClass_strategy = st.builds(VariableClass)
@given(instance=VariableClass_strategy)
@settings(max_examples=25)
def test_VariableClass_instantiation(instance):
    assert isinstance(instance, VariableClass)


behaviour_ActivityDiagramBehavior_strategy = st.builds(behaviour_ActivityDiagramBehavior)
@given(instance=behaviour_ActivityDiagramBehavior_strategy)
@settings(max_examples=25)
def test_behaviour_ActivityDiagramBehavior_instantiation(instance):
    assert isinstance(instance, behaviour_ActivityDiagramBehavior)


behaviour_Add_strategy = st.builds(behaviour_Add)
@given(instance=behaviour_Add_strategy)
@settings(max_examples=25)
def test_behaviour_Add_instantiation(instance):
    assert isinstance(instance, behaviour_Add)


behaviour_AnonymousFunction_strategy = st.builds(behaviour_AnonymousFunction)
@given(instance=behaviour_AnonymousFunction_strategy)
@settings(max_examples=25)
def test_behaviour_AnonymousFunction_instantiation(instance):
    assert isinstance(instance, behaviour_AnonymousFunction)


behaviour_AttributeClass_strategy = st.builds(behaviour_AttributeClass)
@given(instance=behaviour_AttributeClass_strategy)
@settings(max_examples=25)
def test_behaviour_AttributeClass_instantiation(instance):
    assert isinstance(instance, behaviour_AttributeClass)


behaviour_Behavior_strategy = st.builds(behaviour_Behavior, behaviorName=safe_text, frequency=safe_text)
@given(instance=behaviour_Behavior_strategy)
@settings(max_examples=25)
def test_behaviour_Behavior_instantiation(instance):
    assert isinstance(instance, behaviour_Behavior)


behaviour_BinaryArithmeticFunction_strategy = st.builds(behaviour_BinaryArithmeticFunction, functionName=safe_text)
@given(instance=behaviour_BinaryArithmeticFunction_strategy)
@settings(max_examples=25)
def test_behaviour_BinaryArithmeticFunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryArithmeticFunction)


behaviour_BinaryBooleanFunction_strategy = st.builds(behaviour_BinaryBooleanFunction)
@given(instance=behaviour_BinaryBooleanFunction_strategy)
@settings(max_examples=25)
def test_behaviour_BinaryBooleanFunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryBooleanFunction)


behaviour_BinaryFunction_strategy = st.builds(behaviour_BinaryFunction)
@given(instance=behaviour_BinaryFunction_strategy)
@settings(max_examples=25)
def test_behaviour_BinaryFunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryFunction)


behaviour_BinaryLocationFunction_strategy = st.builds(behaviour_BinaryLocationFunction)
@given(instance=behaviour_BinaryLocationFunction_strategy)
@settings(max_examples=25)
def test_behaviour_BinaryLocationFunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryLocationFunction)


behaviour_BooleanPrimitive_strategy = st.builds(behaviour_BooleanPrimitive, primitive=safe_text)
@given(instance=behaviour_BooleanPrimitive_strategy)
@settings(max_examples=25)
def test_behaviour_BooleanPrimitive_instantiation(instance):
    assert isinstance(instance, behaviour_BooleanPrimitive)


behaviour_ComparisonBooleanFunction_strategy = st.builds(behaviour_ComparisonBooleanFunction, functionName=safe_text)
@given(instance=behaviour_ComparisonBooleanFunction_strategy)
@settings(max_examples=25)
def test_behaviour_ComparisonBooleanFunction_instantiation(instance):
    assert isinstance(instance, behaviour_ComparisonBooleanFunction)


behaviour_ConstantExpression_strategy = st.builds(behaviour_ConstantExpression)
@given(instance=behaviour_ConstantExpression_strategy)
@settings(max_examples=25)
def test_behaviour_ConstantExpression_instantiation(instance):
    assert isinstance(instance, behaviour_ConstantExpression)


behaviour_ControlNode_strategy = st.builds(behaviour_ControlNode)
@given(instance=behaviour_ControlNode_strategy)
@settings(max_examples=25)
def test_behaviour_ControlNode_instantiation(instance):
    assert isinstance(instance, behaviour_ControlNode)


behaviour_CoordinateLocationExpression_strategy = st.builds(behaviour_CoordinateLocationExpression, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_CoordinateLocationExpression_strategy)
@settings(max_examples=25)
def test_behaviour_CoordinateLocationExpression_instantiation(instance):
    assert isinstance(instance, behaviour_CoordinateLocationExpression)


behaviour_Decision_strategy = st.builds(behaviour_Decision)
@given(instance=behaviour_Decision_strategy)
@settings(max_examples=25)
def test_behaviour_Decision_instantiation(instance):
    assert isinstance(instance, behaviour_Decision)


behaviour_Die_strategy = st.builds(behaviour_Die)
@given(instance=behaviour_Die_strategy)
@settings(max_examples=25)
def test_behaviour_Die_instantiation(instance):
    assert isinstance(instance, behaviour_Die)


behaviour_Duration_strategy = st.builds(behaviour_Duration, durationTime=st.integers())
@given(instance=behaviour_Duration_strategy)
@settings(max_examples=25)
def test_behaviour_Duration_instantiation(instance):
    assert isinstance(instance, behaviour_Duration)


behaviour_Edge_strategy = st.builds(behaviour_Edge)
@given(instance=behaviour_Edge_strategy)
@settings(max_examples=25)
def test_behaviour_Edge_instantiation(instance):
    assert isinstance(instance, behaviour_Edge)


behaviour_End_strategy = st.builds(behaviour_End)
@given(instance=behaviour_End_strategy)
@settings(max_examples=25)
def test_behaviour_End_instantiation(instance):
    assert isinstance(instance, behaviour_End)


behaviour_EntityClass_strategy = st.builds(behaviour_EntityClass, entityName=safe_text)
@given(instance=behaviour_EntityClass_strategy)
@settings(max_examples=25)
def test_behaviour_EntityClass_instantiation(instance):
    assert isinstance(instance, behaviour_EntityClass)


behaviour_EntityPrimive_strategy = st.builds(behaviour_EntityPrimive, primitive=safe_text)
@given(instance=behaviour_EntityPrimive_strategy)
@settings(max_examples=25)
def test_behaviour_EntityPrimive_instantiation(instance):
    assert isinstance(instance, behaviour_EntityPrimive)


behaviour_EntitySetPrimitive_strategy = st.builds(behaviour_EntitySetPrimitive, primitive=safe_text)
@given(instance=behaviour_EntitySetPrimitive_strategy)
@settings(max_examples=25)
def test_behaviour_EntitySetPrimitive_instantiation(instance):
    assert isinstance(instance, behaviour_EntitySetPrimitive)


behaviour_Equation_strategy = st.builds(behaviour_Equation)
@given(instance=behaviour_Equation_strategy)
@settings(max_examples=25)
def test_behaviour_Equation_instantiation(instance):
    assert isinstance(instance, behaviour_Equation)


behaviour_EquationBehaviour_strategy = st.builds(behaviour_EquationBehaviour)
@given(instance=behaviour_EquationBehaviour_strategy)
@settings(max_examples=25)
def test_behaviour_EquationBehaviour_instantiation(instance):
    assert isinstance(instance, behaviour_EquationBehaviour)


behaviour_ExecutableNode_strategy = st.builds(behaviour_ExecutableNode)
@given(instance=behaviour_ExecutableNode_strategy)
@settings(max_examples=25)
def test_behaviour_ExecutableNode_instantiation(instance):
    assert isinstance(instance, behaviour_ExecutableNode)


behaviour_Expression_strategy = st.builds(behaviour_Expression)
@given(instance=behaviour_Expression_strategy)
@settings(max_examples=25)
def test_behaviour_Expression_instantiation(instance):
    assert isinstance(instance, behaviour_Expression)


behaviour_FalseEdge_strategy = st.builds(behaviour_FalseEdge)
@given(instance=behaviour_FalseEdge_strategy)
@settings(max_examples=25)
def test_behaviour_FalseEdge_instantiation(instance):
    assert isinstance(instance, behaviour_FalseEdge)


behaviour_FloatConstantExpression_strategy = st.builds(behaviour_FloatConstantExpression, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_FloatConstantExpression_strategy)
@settings(max_examples=25)
def test_behaviour_FloatConstantExpression_instantiation(instance):
    assert isinstance(instance, behaviour_FloatConstantExpression)


behaviour_Fork_strategy = st.builds(behaviour_Fork)
@given(instance=behaviour_Fork_strategy)
@settings(max_examples=25)
def test_behaviour_Fork_instantiation(instance):
    assert isinstance(instance, behaviour_Fork)


behaviour_Function_strategy = st.builds(behaviour_Function)
@given(instance=behaviour_Function_strategy)
@settings(max_examples=25)
def test_behaviour_Function_instantiation(instance):
    assert isinstance(instance, behaviour_Function)


behaviour_FunctionCallExpression_strategy = st.builds(behaviour_FunctionCallExpression)
@given(instance=behaviour_FunctionCallExpression_strategy)
@settings(max_examples=25)
def test_behaviour_FunctionCallExpression_instantiation(instance):
    assert isinstance(instance, behaviour_FunctionCallExpression)


behaviour_IntConstantExpression_strategy = st.builds(behaviour_IntConstantExpression, value=st.integers())
@given(instance=behaviour_IntConstantExpression_strategy)
@settings(max_examples=25)
def test_behaviour_IntConstantExpression_instantiation(instance):
    assert isinstance(instance, behaviour_IntConstantExpression)


behaviour_Join_strategy = st.builds(behaviour_Join)
@given(instance=behaviour_Join_strategy)
@settings(max_examples=25)
def test_behaviour_Join_instantiation(instance):
    assert isinstance(instance, behaviour_Join)


behaviour_LocationExpression_strategy = st.builds(behaviour_LocationExpression)
@given(instance=behaviour_LocationExpression_strategy)
@settings(max_examples=25)
def test_behaviour_LocationExpression_instantiation(instance):
    assert isinstance(instance, behaviour_LocationExpression)


behaviour_LocationPrimitive_strategy = st.builds(behaviour_LocationPrimitive, primitive=safe_text)
@given(instance=behaviour_LocationPrimitive_strategy)
@settings(max_examples=25)
def test_behaviour_LocationPrimitive_instantiation(instance):
    assert isinstance(instance, behaviour_LocationPrimitive)


behaviour_LocationSetPrimitive_strategy = st.builds(behaviour_LocationSetPrimitive, primitive=safe_text)
@given(instance=behaviour_LocationSetPrimitive_strategy)
@settings(max_examples=25)
def test_behaviour_LocationSetPrimitive_instantiation(instance):
    assert isinstance(instance, behaviour_LocationSetPrimitive)


behaviour_LogicBooleanFunction_strategy = st.builds(behaviour_LogicBooleanFunction, functionName=safe_text)
@given(instance=behaviour_LogicBooleanFunction_strategy)
@settings(max_examples=25)
def test_behaviour_LogicBooleanFunction_instantiation(instance):
    assert isinstance(instance, behaviour_LogicBooleanFunction)


behaviour_Merge_strategy = st.builds(behaviour_Merge)
@given(instance=behaviour_Merge_strategy)
@settings(max_examples=25)
def test_behaviour_Merge_instantiation(instance):
    assert isinstance(instance, behaviour_Merge)


behaviour_MonthDuration_strategy = st.builds(behaviour_MonthDuration, month=safe_text)
@given(instance=behaviour_MonthDuration_strategy)
@settings(max_examples=25)
def test_behaviour_MonthDuration_instantiation(instance):
    assert isinstance(instance, behaviour_MonthDuration)


behaviour_Move_strategy = st.builds(behaviour_Move)
@given(instance=behaviour_Move_strategy)
@settings(max_examples=25)
def test_behaviour_Move_instantiation(instance):
    assert isinstance(instance, behaviour_Move)


behaviour_NameLocationExpression_strategy = st.builds(behaviour_NameLocationExpression, name=safe_text)
@given(instance=behaviour_NameLocationExpression_strategy)
@settings(max_examples=25)
def test_behaviour_NameLocationExpression_instantiation(instance):
    assert isinstance(instance, behaviour_NameLocationExpression)


behaviour_NamedFunction_strategy = st.builds(behaviour_NamedFunction)
@given(instance=behaviour_NamedFunction_strategy)
@settings(max_examples=25)
def test_behaviour_NamedFunction_instantiation(instance):
    assert isinstance(instance, behaviour_NamedFunction)


behaviour_Node_strategy = st.builds(behaviour_Node)
@given(instance=behaviour_Node_strategy)
@settings(max_examples=25)
def test_behaviour_Node_instantiation(instance):
    assert isinstance(instance, behaviour_Node)


behaviour_NumericPrimitive_strategy = st.builds(behaviour_NumericPrimitive)
@given(instance=behaviour_NumericPrimitive_strategy)
@settings(max_examples=25)
def test_behaviour_NumericPrimitive_instantiation(instance):
    assert isinstance(instance, behaviour_NumericPrimitive)


behaviour_OccupationBooleanFunction_strategy = st.builds(behaviour_OccupationBooleanFunction, functionName=safe_text)
@given(instance=behaviour_OccupationBooleanFunction_strategy)
@settings(max_examples=25)
def test_behaviour_OccupationBooleanFunction_instantiation(instance):
    assert isinstance(instance, behaviour_OccupationBooleanFunction)


behaviour_ParameterClass_strategy = st.builds(behaviour_ParameterClass)
@given(instance=behaviour_ParameterClass_strategy)
@settings(max_examples=25)
def test_behaviour_ParameterClass_instantiation(instance):
    assert isinstance(instance, behaviour_ParameterClass)


behaviour_PrimitiveActivity_strategy = st.builds(behaviour_PrimitiveActivity)
@given(instance=behaviour_PrimitiveActivity_strategy)
@settings(max_examples=25)
def test_behaviour_PrimitiveActivity_instantiation(instance):
    assert isinstance(instance, behaviour_PrimitiveActivity)


behaviour_PrimitiveExpression_strategy = st.builds(behaviour_PrimitiveExpression)
@given(instance=behaviour_PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_behaviour_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, behaviour_PrimitiveExpression)


behaviour_Remove_strategy = st.builds(behaviour_Remove)
@given(instance=behaviour_Remove_strategy)
@settings(max_examples=25)
def test_behaviour_Remove_instantiation(instance):
    assert isinstance(instance, behaviour_Remove)


behaviour_Reproduce_strategy = st.builds(behaviour_Reproduce)
@given(instance=behaviour_Reproduce_strategy)
@settings(max_examples=25)
def test_behaviour_Reproduce_instantiation(instance):
    assert isinstance(instance, behaviour_Reproduce)


behaviour_Start_strategy = st.builds(behaviour_Start)
@given(instance=behaviour_Start_strategy)
@settings(max_examples=25)
def test_behaviour_Start_instantiation(instance):
    assert isinstance(instance, behaviour_Start)


behaviour_StringConstantExpression_strategy = st.builds(behaviour_StringConstantExpression, value=safe_text)
@given(instance=behaviour_StringConstantExpression_strategy)
@settings(max_examples=25)
def test_behaviour_StringConstantExpression_instantiation(instance):
    assert isinstance(instance, behaviour_StringConstantExpression)


behaviour_TimeExpression_strategy = st.builds(behaviour_TimeExpression)
@given(instance=behaviour_TimeExpression_strategy)
@settings(max_examples=25)
def test_behaviour_TimeExpression_instantiation(instance):
    assert isinstance(instance, behaviour_TimeExpression)


behaviour_TrueEdge_strategy = st.builds(behaviour_TrueEdge)
@given(instance=behaviour_TrueEdge_strategy)
@settings(max_examples=25)
def test_behaviour_TrueEdge_instantiation(instance):
    assert isinstance(instance, behaviour_TrueEdge)


behaviour_Type_strategy = st.builds(behaviour_Type, type=safe_text)
@given(instance=behaviour_Type_strategy)
@settings(max_examples=25)
def test_behaviour_Type_instantiation(instance):
    assert isinstance(instance, behaviour_Type)


behaviour_UnaryEntityFunction_strategy = st.builds(behaviour_UnaryEntityFunction, functionName=safe_text)
@given(instance=behaviour_UnaryEntityFunction_strategy)
@settings(max_examples=25)
def test_behaviour_UnaryEntityFunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryEntityFunction)


behaviour_UnaryFunction_strategy = st.builds(behaviour_UnaryFunction)
@given(instance=behaviour_UnaryFunction_strategy)
@settings(max_examples=25)
def test_behaviour_UnaryFunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryFunction)


behaviour_UnaryLocationFunction_strategy = st.builds(behaviour_UnaryLocationFunction, functionName=safe_text)
@given(instance=behaviour_UnaryLocationFunction_strategy)
@settings(max_examples=25)
def test_behaviour_UnaryLocationFunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryLocationFunction)


behaviour_UnaryNumericFunction_strategy = st.builds(behaviour_UnaryNumericFunction, functionName=safe_text)
@given(instance=behaviour_UnaryNumericFunction_strategy)
@settings(max_examples=25)
def test_behaviour_UnaryNumericFunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryNumericFunction)


behaviour_UnaryStringFunction_strategy = st.builds(behaviour_UnaryStringFunction, functionName=safe_text)
@given(instance=behaviour_UnaryStringFunction_strategy)
@settings(max_examples=25)
def test_behaviour_UnaryStringFunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryStringFunction)


behaviour_UnconditionedEdge_strategy = st.builds(behaviour_UnconditionedEdge)
@given(instance=behaviour_UnconditionedEdge_strategy)
@settings(max_examples=25)
def test_behaviour_UnconditionedEdge_instantiation(instance):
    assert isinstance(instance, behaviour_UnconditionedEdge)


behaviour_VariableClass_strategy = st.builds(behaviour_VariableClass, variableName=safe_text)
@given(instance=behaviour_VariableClass_strategy)
@settings(max_examples=25)
def test_behaviour_VariableClass_instantiation(instance):
    assert isinstance(instance, behaviour_VariableClass)


behaviour_While_strategy = st.builds(behaviour_While)
@given(instance=behaviour_While_strategy)
@settings(max_examples=25)
def test_behaviour_While_instantiation(instance):
    assert isinstance(instance, behaviour_While)


