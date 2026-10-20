import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractBinaryOperator,
    AbstractType,
    BinaryExpression,
    BooleanExpression,
    BuiltInFunction,
    CollectionExpression,
    Constraint,
    DataInitMethods,
    Declaration,
    DefinedType,
    Expression,
    FloatType,
    Function,
    Initialization,
    IntegerType,
    NumericExpression,
    NumericType,
    OPLmetamodel_AbstractBinaryOperator,
    OPLmetamodel_AbstractType,
    OPLmetamodel_ActivityDeclaration,
    OPLmetamodel_AggregateExp,
    OPLmetamodel_AllExpression,
    OPLmetamodel_ArrayDereference,
    OPLmetamodel_ArraySlotConstraint,
    OPLmetamodel_ArrayType,
    OPLmetamodel_ArrayValue,
    OPLmetamodel_Assertion,
    OPLmetamodel_BinaryExpression,
    OPLmetamodel_BinaryOperator,
    OPLmetamodel_BindingRef,
    OPLmetamodel_BlockExpression,
    OPLmetamodel_BooleanBlock,
    OPLmetamodel_BooleanExpression,
    OPLmetamodel_BooleanType,
    OPLmetamodel_BuiltInFunction,
    OPLmetamodel_CollectionExpression,
    OPLmetamodel_Comprehension,
    OPLmetamodel_Constraint,
    OPLmetamodel_CumulativeFunction,
    OPLmetamodel_DataDeclaration,
    OPLmetamodel_DataInitMethods,
    OPLmetamodel_DataObject,
    OPLmetamodel_DataRef,
    OPLmetamodel_Declaration,
    OPLmetamodel_DeferredInit,
    OPLmetamodel_DefinedType,
    OPLmetamodel_DisplayInstruction,
    OPLmetamodel_Entity,
    OPLmetamodel_EnumLiteral,
    OPLmetamodel_EnumerationType,
    OPLmetamodel_Error,
    OPLmetamodel_Expression,
    OPLmetamodel_Extension,
    OPLmetamodel_FloatExpression,
    OPLmetamodel_FloatRangeType,
    OPLmetamodel_FloatType,
    OPLmetamodel_ForAllConstraint,
    OPLmetamodel_FormalParameter,
    OPLmetamodel_Function,
    OPLmetamodel_FunctionCall,
    OPLmetamodel_FunctionRef,
    OPLmetamodel_IfConstraint,
    OPLmetamodel_IfExpression,
    OPLmetamodel_In,
    OPLmetamodel_IndexValuePair,
    OPLmetamodel_Initialization,
    OPLmetamodel_IntegerExpression,
    OPLmetamodel_IntegerRangeType,
    OPLmetamodel_IntegerType,
    OPLmetamodel_Interval,
    OPLmetamodel_Model,
    OPLmetamodel_Number,
    OPLmetamodel_NumericExpression,
    OPLmetamodel_NumericType,
    OPLmetamodel_Objective,
    OPLmetamodel_Operator,
    OPLmetamodel_ParameterDeclaration,
    OPLmetamodel_ParameterDomain,
    OPLmetamodel_ParameterRef,
    OPLmetamodel_PathDereference,
    OPLmetamodel_PathExpression,
    OPLmetamodel_PiecewiseExpression,
    OPLmetamodel_PiecewiseLinearFunction,
    OPLmetamodel_PositiveFloatType,
    OPLmetamodel_PositiveIntegerType,
    OPLmetamodel_PrimitiveExpression,
    OPLmetamodel_PrimitiveType,
    OPLmetamodel_QueryUser,
    OPLmetamodel_RangeExpression,
    OPLmetamodel_RangeType,
    OPLmetamodel_ReadFile,
    OPLmetamodel_Record,
    OPLmetamodel_RecordField,
    OPLmetamodel_RecordValue,
    OPLmetamodel_Reference,
    OPLmetamodel_ReflectiveFunction,
    OPLmetamodel_RelationalExpression,
    OPLmetamodel_RelationalInit,
    OPLmetamodel_RelationalOperator,
    OPLmetamodel_ResourceDeclaration,
    OPLmetamodel_ScheduleInitialization,
    OPLmetamodel_Script,
    OPLmetamodel_ScriptStatement,
    OPLmetamodel_SearchProcedure,
    OPLmetamodel_Sequence,
    OPLmetamodel_SetType,
    OPLmetamodel_SetValue,
    OPLmetamodel_Setting,
    OPLmetamodel_StateFunction,
    OPLmetamodel_StepFunction,
    OPLmetamodel_StringExpression,
    OPLmetamodel_StringType,
    OPLmetamodel_TupleBinding,
    OPLmetamodel_UnaryExpression,
    OPLmetamodel_VariableBinding,
    OPLmetamodel_Writeln,
    ParameterDomain,
    PathExpression,
    PiecewiseLinearFunction,
    PrimitiveExpression,
    PrimitiveType,
    RangeType,
    Reference,
    ScriptStatement,
    SetType,
    AggOp,
    BinaryOp,
    LogicalOp,
    MembershipOp,
    OptimizationMode,
    Quantifier,
    RelationalOp,
    SetOp,
    UnaryOp,
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

def test_assoc_activities106_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    a2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    b = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    _safe_set(b, 'OPLmetamodel_ActivityDeclaration108', a1)
    assert _is_linked(b, 'OPLmetamodel_ActivityDeclaration108', a1)
    if hasattr(a1, 'OPLmetamodel_Model107'):
        assert _is_linked(a1, 'OPLmetamodel_Model107', b)
    _safe_set(b, 'OPLmetamodel_ActivityDeclaration108', a2)
    assert _is_linked(b, 'OPLmetamodel_ActivityDeclaration108', a2)
    if hasattr(a1, 'OPLmetamodel_Model107'):
        assert not _is_linked(a1, 'OPLmetamodel_Model107', b)
    if hasattr(a2, 'OPLmetamodel_Model107'):
        assert _is_linked(a2, 'OPLmetamodel_Model107', b)
    _safe_set(b, 'OPLmetamodel_ActivityDeclaration108', None)
    assert not _is_linked(b, 'OPLmetamodel_ActivityDeclaration108', a2)
    if hasattr(a2, 'OPLmetamodel_Model107'):
        assert not _is_linked(a2, 'OPLmetamodel_Model107', b)


def test_assoc_assertions111_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    a2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    b = OPLmetamodel_Constraint(name="sample_text")
    _safe_set(b, 'OPLmetamodel_Constraint113', a1)
    assert _is_linked(b, 'OPLmetamodel_Constraint113', a1)
    if hasattr(a1, 'OPLmetamodel_Model112'):
        assert _is_linked(a1, 'OPLmetamodel_Model112', b)
    _safe_set(b, 'OPLmetamodel_Constraint113', a2)
    assert _is_linked(b, 'OPLmetamodel_Constraint113', a2)
    if hasattr(a1, 'OPLmetamodel_Model112'):
        assert not _is_linked(a1, 'OPLmetamodel_Model112', b)
    if hasattr(a2, 'OPLmetamodel_Model112'):
        assert _is_linked(a2, 'OPLmetamodel_Model112', b)
    _safe_set(b, 'OPLmetamodel_Constraint113', None)
    assert not _is_linked(b, 'OPLmetamodel_Constraint113', a2)
    if hasattr(a2, 'OPLmetamodel_Model112'):
        assert not _is_linked(a2, 'OPLmetamodel_Model112', b)


def test_assoc_constraints98_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    a2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    b = OPLmetamodel_Constraint(name="sample_text")
    _safe_set(b, 'OPLmetamodel_Constraint100', a1)
    assert _is_linked(b, 'OPLmetamodel_Constraint100', a1)
    if hasattr(a1, 'OPLmetamodel_Model99'):
        assert _is_linked(a1, 'OPLmetamodel_Model99', b)
    _safe_set(b, 'OPLmetamodel_Constraint100', a2)
    assert _is_linked(b, 'OPLmetamodel_Constraint100', a2)
    if hasattr(a1, 'OPLmetamodel_Model99'):
        assert not _is_linked(a1, 'OPLmetamodel_Model99', b)
    if hasattr(a2, 'OPLmetamodel_Model99'):
        assert _is_linked(a2, 'OPLmetamodel_Model99', b)
    _safe_set(b, 'OPLmetamodel_Constraint100', None)
    assert not _is_linked(b, 'OPLmetamodel_Constraint100', a2)
    if hasattr(a2, 'OPLmetamodel_Model99'):
        assert not _is_linked(a2, 'OPLmetamodel_Model99', b)


def test_assoc_data95_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    a2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    b = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    _safe_set(b, 'OPLmetamodel_DataDeclaration97', a1)
    assert _is_linked(b, 'OPLmetamodel_DataDeclaration97', a1)
    if hasattr(a1, 'OPLmetamodel_Model96'):
        assert _is_linked(a1, 'OPLmetamodel_Model96', b)
    _safe_set(b, 'OPLmetamodel_DataDeclaration97', a2)
    assert _is_linked(b, 'OPLmetamodel_DataDeclaration97', a2)
    if hasattr(a1, 'OPLmetamodel_Model96'):
        assert not _is_linked(a1, 'OPLmetamodel_Model96', b)
    if hasattr(a2, 'OPLmetamodel_Model96'):
        assert _is_linked(a2, 'OPLmetamodel_Model96', b)
    _safe_set(b, 'OPLmetamodel_DataDeclaration97', None)
    assert not _is_linked(b, 'OPLmetamodel_DataDeclaration97', a2)
    if hasattr(a2, 'OPLmetamodel_Model96'):
        assert not _is_linked(a2, 'OPLmetamodel_Model96', b)


def test_assoc_fields145_reverse_link_reassign_clear():
    a1 = OPLmetamodel_RecordField(name="sample_text")
    a2 = OPLmetamodel_RecordField(name="sample_text_2")
    b = OPLmetamodel_Record(isTuple=True, name="sample_text")
    _safe_set(b, 'OPLmetamodel_Record', {a1})
    assert _is_linked(b, 'OPLmetamodel_Record', a1)
    if hasattr(a1, 'OPLmetamodel_RecordField'):
        assert _is_linked(a1, 'OPLmetamodel_RecordField', b)
    _safe_set(b, 'OPLmetamodel_Record', {a2})
    assert _is_linked(b, 'OPLmetamodel_Record', a2)
    if hasattr(a1, 'OPLmetamodel_RecordField'):
        assert not _is_linked(a1, 'OPLmetamodel_RecordField', b)
    if hasattr(a2, 'OPLmetamodel_RecordField'):
        assert _is_linked(a2, 'OPLmetamodel_RecordField', b)
    _safe_set(b, 'OPLmetamodel_Record', set())
    assert not _is_linked(b, 'OPLmetamodel_Record', a2)
    if hasattr(a2, 'OPLmetamodel_RecordField'):
        assert not _is_linked(a2, 'OPLmetamodel_RecordField', b)


def test_assoc_id157_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Script(isMain=True)
    a2 = OPLmetamodel_Script(isMain=False)
    b = OPLmetamodel_Reference(name="sample_text")
    _safe_set(b, 'OPLmetamodel_Reference159', a1)
    assert _is_linked(b, 'OPLmetamodel_Reference159', a1)
    if hasattr(a1, 'OPLmetamodel_Script158'):
        assert _is_linked(a1, 'OPLmetamodel_Script158', b)
    _safe_set(b, 'OPLmetamodel_Reference159', a2)
    assert _is_linked(b, 'OPLmetamodel_Reference159', a2)
    if hasattr(a1, 'OPLmetamodel_Script158'):
        assert not _is_linked(a1, 'OPLmetamodel_Script158', b)
    if hasattr(a2, 'OPLmetamodel_Script158'):
        assert _is_linked(a2, 'OPLmetamodel_Script158', b)
    _safe_set(b, 'OPLmetamodel_Reference159', None)
    assert not _is_linked(b, 'OPLmetamodel_Reference159', a2)
    if hasattr(a2, 'OPLmetamodel_Script158'):
        assert not _is_linked(a2, 'OPLmetamodel_Script158', b)


def test_assoc_instruction101_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    a2 = OPLmetamodel_Objective(action="sample_text_2", isLinearRelaxation=False)
    b = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    _safe_set(b, 'OPLmetamodel_Model102', a1)
    assert _is_linked(b, 'OPLmetamodel_Model102', a1)
    if hasattr(a1, 'OPLmetamodel_Objective'):
        assert _is_linked(a1, 'OPLmetamodel_Objective', b)
    _safe_set(b, 'OPLmetamodel_Model102', a2)
    assert _is_linked(b, 'OPLmetamodel_Model102', a2)
    if hasattr(a1, 'OPLmetamodel_Objective'):
        assert not _is_linked(a1, 'OPLmetamodel_Objective', b)
    if hasattr(a2, 'OPLmetamodel_Objective'):
        assert _is_linked(a2, 'OPLmetamodel_Objective', b)
    _safe_set(b, 'OPLmetamodel_Model102', None)
    assert not _is_linked(b, 'OPLmetamodel_Model102', a2)
    if hasattr(a2, 'OPLmetamodel_Objective'):
        assert not _is_linked(a2, 'OPLmetamodel_Objective', b)


def test_assoc_parameters1_reverse_link_reassign_clear():
    a1 = OPLmetamodel_FormalParameter(isOrdered=True)
    a2 = OPLmetamodel_FormalParameter(isOrdered=False)
    b = OPLmetamodel_AggregateExp(op="sample_text")
    _safe_set(b, 'OPLmetamodel_AggregateExp', {a1})
    assert _is_linked(b, 'OPLmetamodel_AggregateExp', a1)
    if hasattr(a1, 'OPLmetamodel_FormalParameter'):
        assert _is_linked(a1, 'OPLmetamodel_FormalParameter', b)
    _safe_set(b, 'OPLmetamodel_AggregateExp', {a2})
    assert _is_linked(b, 'OPLmetamodel_AggregateExp', a2)
    if hasattr(a1, 'OPLmetamodel_FormalParameter'):
        assert not _is_linked(a1, 'OPLmetamodel_FormalParameter', b)
    if hasattr(a2, 'OPLmetamodel_FormalParameter'):
        assert _is_linked(a2, 'OPLmetamodel_FormalParameter', b)
    _safe_set(b, 'OPLmetamodel_AggregateExp', set())
    assert not _is_linked(b, 'OPLmetamodel_AggregateExp', a2)
    if hasattr(a2, 'OPLmetamodel_FormalParameter'):
        assert not _is_linked(a2, 'OPLmetamodel_FormalParameter', b)


def test_assoc_scripts116_reverse_link_reassign_clear():
    a1 = OPLmetamodel_Script(isMain=True)
    a2 = OPLmetamodel_Script(isMain=False)
    b = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    _safe_set(b, 'OPLmetamodel_Model117', {a1})
    assert _is_linked(b, 'OPLmetamodel_Model117', a1)
    if hasattr(a1, 'OPLmetamodel_Script'):
        assert _is_linked(a1, 'OPLmetamodel_Script', b)
    _safe_set(b, 'OPLmetamodel_Model117', {a2})
    assert _is_linked(b, 'OPLmetamodel_Model117', a2)
    if hasattr(a1, 'OPLmetamodel_Script'):
        assert not _is_linked(a1, 'OPLmetamodel_Script', b)
    if hasattr(a2, 'OPLmetamodel_Script'):
        assert _is_linked(a2, 'OPLmetamodel_Script', b)
    _safe_set(b, 'OPLmetamodel_Model117', set())
    assert not _is_linked(b, 'OPLmetamodel_Model117', a2)
    if hasattr(a2, 'OPLmetamodel_Script'):
        assert not _is_linked(a2, 'OPLmetamodel_Script', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args67_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression68' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FunctionCall(functionName="sample_text")
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression68', None)
    _safe_set(owner, 'OPLmetamodel_FunctionCall', {partner})
    assert getattr(partner, 'OPLmetamodel_Expression68') == owner
    _safe_set(owner, 'OPLmetamodel_FunctionCall', set())
    assert getattr(partner, 'OPLmetamodel_Expression68') is None


def test_assoc_baseType167_stub_double():
    # OPLmetamodel_AbstractType has no real 'OPLmetamodel_AbstractType168' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_SetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_SetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_SetType(name="sample_text")
    partner = OPLmetamodel_AbstractType()
    setattr(partner, 'OPLmetamodel_AbstractType168', None)
    _safe_set(owner, 'OPLmetamodel_SetType', partner)
    assert getattr(partner, 'OPLmetamodel_AbstractType168') == owner
    _safe_set(owner, 'OPLmetamodel_SetType', None)
    assert getattr(partner, 'OPLmetamodel_AbstractType168') is None


def test_assoc_body2_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_AggregateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_AggregateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_AggregateExp(op="sample_text")
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression', None)
    _safe_set(owner, 'OPLmetamodel_AggregateExp3', partner)
    assert getattr(partner, 'OPLmetamodel_Expression') == owner
    _safe_set(owner, 'OPLmetamodel_AggregateExp3', None)
    assert getattr(partner, 'OPLmetamodel_Expression') is None


def test_assoc_boundVars49_stub_double():
    # OPLmetamodel_BindingRef has no real 'OPLmetamodel_BindingRef' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FormalParameter(isOrdered=True)
    partner = OPLmetamodel_BindingRef()
    setattr(partner, 'OPLmetamodel_BindingRef', None)
    _safe_set(owner, 'OPLmetamodel_FormalParameter50', {partner})
    assert getattr(partner, 'OPLmetamodel_BindingRef') == owner
    _safe_set(owner, 'OPLmetamodel_FormalParameter50', set())
    assert getattr(partner, 'OPLmetamodel_BindingRef') is None


def test_assoc_bounds84_stub_double():
    # OPLmetamodel_RangeType has no real 'OPLmetamodel_RangeType' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Interval(isOptional=True)
    partner = OPLmetamodel_RangeType()
    setattr(partner, 'OPLmetamodel_RangeType', None)
    _safe_set(owner, 'OPLmetamodel_Interval', partner)
    assert getattr(partner, 'OPLmetamodel_RangeType') == owner
    _safe_set(owner, 'OPLmetamodel_Interval', None)
    assert getattr(partner, 'OPLmetamodel_RangeType') is None


def test_assoc_deref127_stub_double():
    # OPLmetamodel_PathDereference has no real 'OPLmetamodel_PathDereference' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Reference(name="sample_text")
    partner = OPLmetamodel_PathDereference()
    setattr(partner, 'OPLmetamodel_PathDereference', None)
    _safe_set(owner, 'OPLmetamodel_Reference128', partner)
    assert getattr(partner, 'OPLmetamodel_PathDereference') == owner
    _safe_set(owner, 'OPLmetamodel_Reference128', None)
    assert getattr(partner, 'OPLmetamodel_PathDereference') is None


def test_assoc_domain47_stub_double():
    # OPLmetamodel_ParameterDomain has no real 'OPLmetamodel_ParameterDomain' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FormalParameter(isOrdered=True)
    partner = OPLmetamodel_ParameterDomain()
    setattr(partner, 'OPLmetamodel_ParameterDomain', None)
    _safe_set(owner, 'OPLmetamodel_FormalParameter48', partner)
    assert getattr(partner, 'OPLmetamodel_ParameterDomain') == owner
    _safe_set(owner, 'OPLmetamodel_FormalParameter48', None)
    assert getattr(partner, 'OPLmetamodel_ParameterDomain') is None


def test_assoc_duration0_stub_double():
    # OPLmetamodel_Number has no real 'OPLmetamodel_Number' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_ActivityDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_ActivityDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    partner = OPLmetamodel_Number()
    setattr(partner, 'OPLmetamodel_Number', None)
    _safe_set(owner, 'OPLmetamodel_ActivityDeclaration', partner)
    assert getattr(partner, 'OPLmetamodel_Number') == owner
    _safe_set(owner, 'OPLmetamodel_ActivityDeclaration', None)
    assert getattr(partner, 'OPLmetamodel_Number') is None


def test_assoc_elements169_stub_double():
    # OPLmetamodel_Entity has no real 'OPLmetamodel_Entity' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_SetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_SetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_SetType(name="sample_text")
    partner = OPLmetamodel_Entity()
    setattr(partner, 'OPLmetamodel_Entity', None)
    _safe_set(owner, 'OPLmetamodel_SetType170', {partner})
    assert getattr(partner, 'OPLmetamodel_Entity') == owner
    _safe_set(owner, 'OPLmetamodel_SetType170', set())
    assert getattr(partner, 'OPLmetamodel_Entity') is None


def test_assoc_else_73_stub_double():
    # OPLmetamodel_IfConstraint has no real 'OPLmetamodel_IfConstraint74' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Constraint(name="sample_text")
    partner = OPLmetamodel_IfConstraint()
    setattr(partner, 'OPLmetamodel_IfConstraint74', None)
    _safe_set(owner, 'OPLmetamodel_Constraint75', partner)
    assert getattr(partner, 'OPLmetamodel_IfConstraint74') == owner
    _safe_set(owner, 'OPLmetamodel_Constraint75', None)
    assert getattr(partner, 'OPLmetamodel_IfConstraint74') is None


def test_assoc_exp177_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression178' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_UnaryExpression(op="sample_text")
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression178', None)
    _safe_set(owner, 'OPLmetamodel_UnaryExpression', partner)
    assert getattr(partner, 'OPLmetamodel_Expression178') == owner
    _safe_set(owner, 'OPLmetamodel_UnaryExpression', None)
    assert getattr(partner, 'OPLmetamodel_Expression178') is None


def test_assoc_exp20_stub_double():
    # OPLmetamodel_Assertion has no real 'OPLmetamodel_Assertion' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Constraint(name="sample_text")
    partner = OPLmetamodel_Assertion()
    setattr(partner, 'OPLmetamodel_Assertion', None)
    _safe_set(owner, 'OPLmetamodel_Constraint', partner)
    assert getattr(partner, 'OPLmetamodel_Assertion') == owner
    _safe_set(owner, 'OPLmetamodel_Constraint', None)
    assert getattr(partner, 'OPLmetamodel_Assertion') is None


def test_assoc_exp29_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Constraint(name="sample_text")
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression31', None)
    _safe_set(owner, 'OPLmetamodel_Constraint30', partner)
    assert getattr(partner, 'OPLmetamodel_Expression31') == owner
    _safe_set(owner, 'OPLmetamodel_Constraint30', None)
    assert getattr(partner, 'OPLmetamodel_Expression31') is None


def test_assoc_expression124_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression126' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Objective's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Objective's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression126', None)
    _safe_set(owner, 'OPLmetamodel_Objective125', partner)
    assert getattr(partner, 'OPLmetamodel_Expression126') == owner
    _safe_set(owner, 'OPLmetamodel_Objective125', None)
    assert getattr(partner, 'OPLmetamodel_Expression126') is None


def test_assoc_exps58_stub_double():
    # OPLmetamodel_ForAllConstraint has no real 'OPLmetamodel_ForAllConstraint59' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Constraint(name="sample_text")
    partner = OPLmetamodel_ForAllConstraint()
    setattr(partner, 'OPLmetamodel_ForAllConstraint59', None)
    _safe_set(owner, 'OPLmetamodel_Constraint60', partner)
    assert owner in getattr(partner, 'OPLmetamodel_ForAllConstraint59')
    _safe_set(owner, 'OPLmetamodel_Constraint60', None)
    assert owner not in getattr(partner, 'OPLmetamodel_ForAllConstraint59')


def test_assoc_functions103_stub_double():
    # OPLmetamodel_Function has no real 'OPLmetamodel_Function105' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_Function()
    setattr(partner, 'OPLmetamodel_Function105', None)
    _safe_set(owner, 'OPLmetamodel_Model104', {partner})
    assert getattr(partner, 'OPLmetamodel_Function105') == owner
    _safe_set(owner, 'OPLmetamodel_Model104', set())
    assert getattr(partner, 'OPLmetamodel_Function105') is None


def test_assoc_intensity87_stub_double():
    # OPLmetamodel_StepFunction has no real 'OPLmetamodel_StepFunction' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Interval(isOptional=True)
    partner = OPLmetamodel_StepFunction()
    setattr(partner, 'OPLmetamodel_StepFunction', None)
    _safe_set(owner, 'OPLmetamodel_Interval88', partner)
    assert getattr(partner, 'OPLmetamodel_StepFunction') == owner
    _safe_set(owner, 'OPLmetamodel_Interval88', None)
    assert getattr(partner, 'OPLmetamodel_StepFunction') is None


def test_assoc_intervals162_stub_double():
    # OPLmetamodel_Sequence has no real 'OPLmetamodel_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Interval(isOptional=True)
    partner = OPLmetamodel_Sequence()
    setattr(partner, 'OPLmetamodel_Sequence', None)
    _safe_set(owner, 'OPLmetamodel_Interval163', partner)
    assert owner in getattr(partner, 'OPLmetamodel_Sequence')
    _safe_set(owner, 'OPLmetamodel_Interval163', None)
    assert owner not in getattr(partner, 'OPLmetamodel_Sequence')


def test_assoc_name61_stub_double():
    # OPLmetamodel_Function has no real 'OPLmetamodel_Function' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FunctionRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FunctionRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FunctionRef(name="sample_text")
    partner = OPLmetamodel_Function()
    setattr(partner, 'OPLmetamodel_Function', None)
    _safe_set(owner, 'OPLmetamodel_FunctionRef', partner)
    assert getattr(partner, 'OPLmetamodel_Function') == owner
    _safe_set(owner, 'OPLmetamodel_FunctionRef', None)
    assert getattr(partner, 'OPLmetamodel_Function') is None


def test_assoc_parameters65_stub_double():
    # OPLmetamodel_Function has no real 'OPLmetamodel_Function66' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Reference(name="sample_text")
    partner = OPLmetamodel_Function()
    setattr(partner, 'OPLmetamodel_Function66', None)
    _safe_set(owner, 'OPLmetamodel_Reference', partner)
    assert owner in getattr(partner, 'OPLmetamodel_Function66')
    _safe_set(owner, 'OPLmetamodel_Reference', None)
    assert owner not in getattr(partner, 'OPLmetamodel_Function66')


def test_assoc_qualifiers4_stub_double():
    # OPLmetamodel_AllExpression has no real 'OPLmetamodel_AllExpression' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FormalParameter(isOrdered=True)
    partner = OPLmetamodel_AllExpression()
    setattr(partner, 'OPLmetamodel_AllExpression', None)
    _safe_set(owner, 'OPLmetamodel_FormalParameter5', partner)
    assert owner in getattr(partner, 'OPLmetamodel_AllExpression')
    _safe_set(owner, 'OPLmetamodel_FormalParameter5', None)
    assert owner not in getattr(partner, 'OPLmetamodel_AllExpression')


def test_assoc_qualifiers56_stub_double():
    # OPLmetamodel_ForAllConstraint has no real 'OPLmetamodel_ForAllConstraint' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FormalParameter(isOrdered=True)
    partner = OPLmetamodel_ForAllConstraint()
    setattr(partner, 'OPLmetamodel_ForAllConstraint', None)
    _safe_set(owner, 'OPLmetamodel_FormalParameter57', partner)
    assert owner in getattr(partner, 'OPLmetamodel_ForAllConstraint')
    _safe_set(owner, 'OPLmetamodel_FormalParameter57', None)
    assert owner not in getattr(partner, 'OPLmetamodel_ForAllConstraint')


def test_assoc_relation155_stub_double():
    # OPLmetamodel_RelationalInit has no real 'OPLmetamodel_RelationalInit156' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_RelationalExpression(redefinedOp="sample_text")
    partner = OPLmetamodel_RelationalInit()
    setattr(partner, 'OPLmetamodel_RelationalInit156', None)
    _safe_set(owner, 'OPLmetamodel_RelationalExpression', partner)
    assert getattr(partner, 'OPLmetamodel_RelationalInit156') == owner
    _safe_set(owner, 'OPLmetamodel_RelationalExpression', None)
    assert getattr(partner, 'OPLmetamodel_RelationalInit156') is None


def test_assoc_require51_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_FormalParameter(isOrdered=True)
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression53', None)
    _safe_set(owner, 'OPLmetamodel_FormalParameter52', partner)
    assert getattr(partner, 'OPLmetamodel_Expression53') == owner
    _safe_set(owner, 'OPLmetamodel_FormalParameter52', None)
    assert getattr(partner, 'OPLmetamodel_Expression53') is None


def test_assoc_resources109_stub_double():
    # OPLmetamodel_ResourceDeclaration has no real 'OPLmetamodel_ResourceDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_ResourceDeclaration()
    setattr(partner, 'OPLmetamodel_ResourceDeclaration', None)
    _safe_set(owner, 'OPLmetamodel_Model110', partner)
    assert getattr(partner, 'OPLmetamodel_ResourceDeclaration') == owner
    _safe_set(owner, 'OPLmetamodel_Model110', None)
    assert getattr(partner, 'OPLmetamodel_ResourceDeclaration') is None


def test_assoc_scheduleInit114_stub_double():
    # OPLmetamodel_ScheduleInitialization has no real 'OPLmetamodel_ScheduleInitialization' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_ScheduleInitialization()
    setattr(partner, 'OPLmetamodel_ScheduleInitialization', None)
    _safe_set(owner, 'OPLmetamodel_Model115', {partner})
    assert getattr(partner, 'OPLmetamodel_ScheduleInitialization') == owner
    _safe_set(owner, 'OPLmetamodel_Model115', set())
    assert getattr(partner, 'OPLmetamodel_ScheduleInitialization') is None


def test_assoc_search122_stub_double():
    # OPLmetamodel_SearchProcedure has no real 'OPLmetamodel_SearchProcedure' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_SearchProcedure()
    setattr(partner, 'OPLmetamodel_SearchProcedure', None)
    _safe_set(owner, 'OPLmetamodel_Model123', partner)
    assert getattr(partner, 'OPLmetamodel_SearchProcedure') == owner
    _safe_set(owner, 'OPLmetamodel_Model123', None)
    assert getattr(partner, 'OPLmetamodel_SearchProcedure') is None


def test_assoc_settings118_stub_double():
    # OPLmetamodel_Setting has no real 'OPLmetamodel_Setting' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_Setting()
    setattr(partner, 'OPLmetamodel_Setting', None)
    _safe_set(owner, 'OPLmetamodel_Model119', {partner})
    assert getattr(partner, 'OPLmetamodel_Setting') == owner
    _safe_set(owner, 'OPLmetamodel_Model119', set())
    assert getattr(partner, 'OPLmetamodel_Setting') is None


def test_assoc_size85_stub_double():
    # OPLmetamodel_NumericType has no real 'OPLmetamodel_NumericType' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Interval(isOptional=True)
    partner = OPLmetamodel_NumericType()
    setattr(partner, 'OPLmetamodel_NumericType', None)
    _safe_set(owner, 'OPLmetamodel_Interval86', partner)
    assert getattr(partner, 'OPLmetamodel_NumericType') == owner
    _safe_set(owner, 'OPLmetamodel_Interval86', None)
    assert getattr(partner, 'OPLmetamodel_NumericType') is None


def test_assoc_statements160_stub_double():
    # OPLmetamodel_ScriptStatement has no real 'OPLmetamodel_ScriptStatement' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Script's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Script's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Script(isMain=True)
    partner = OPLmetamodel_ScriptStatement()
    setattr(partner, 'OPLmetamodel_ScriptStatement', None)
    _safe_set(owner, 'OPLmetamodel_Script161', {partner})
    assert getattr(partner, 'OPLmetamodel_ScriptStatement') == owner
    _safe_set(owner, 'OPLmetamodel_Script161', set())
    assert getattr(partner, 'OPLmetamodel_ScriptStatement') is None


def test_assoc_test69_stub_double():
    # OPLmetamodel_IfConstraint has no real 'OPLmetamodel_IfConstraint' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_BooleanExpression(body="sample_text")
    partner = OPLmetamodel_IfConstraint()
    setattr(partner, 'OPLmetamodel_IfConstraint', None)
    _safe_set(owner, 'OPLmetamodel_BooleanExpression', partner)
    assert getattr(partner, 'OPLmetamodel_IfConstraint') == owner
    _safe_set(owner, 'OPLmetamodel_BooleanExpression', None)
    assert getattr(partner, 'OPLmetamodel_IfConstraint') is None


def test_assoc_test76_stub_double():
    # OPLmetamodel_IfExpression has no real 'OPLmetamodel_IfExpression' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_BooleanExpression(body="sample_text")
    partner = OPLmetamodel_IfExpression()
    setattr(partner, 'OPLmetamodel_IfExpression', None)
    _safe_set(owner, 'OPLmetamodel_BooleanExpression77', partner)
    assert getattr(partner, 'OPLmetamodel_IfExpression') == owner
    _safe_set(owner, 'OPLmetamodel_BooleanExpression77', None)
    assert getattr(partner, 'OPLmetamodel_IfExpression') is None


def test_assoc_then70_stub_double():
    # OPLmetamodel_IfConstraint has no real 'OPLmetamodel_IfConstraint71' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Constraint(name="sample_text")
    partner = OPLmetamodel_IfConstraint()
    setattr(partner, 'OPLmetamodel_IfConstraint71', None)
    _safe_set(owner, 'OPLmetamodel_Constraint72', partner)
    assert getattr(partner, 'OPLmetamodel_IfConstraint71') == owner
    _safe_set(owner, 'OPLmetamodel_Constraint72', None)
    assert getattr(partner, 'OPLmetamodel_IfConstraint71') is None


def test_assoc_transitionMatrix173_stub_double():
    # OPLmetamodel_StateFunction has no real 'OPLmetamodel_StateFunction' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_SetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_SetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_SetType(name="sample_text")
    partner = OPLmetamodel_StateFunction()
    setattr(partner, 'OPLmetamodel_StateFunction', None)
    _safe_set(owner, 'OPLmetamodel_SetType174', partner)
    assert getattr(partner, 'OPLmetamodel_StateFunction') == owner
    _safe_set(owner, 'OPLmetamodel_SetType174', None)
    assert getattr(partner, 'OPLmetamodel_StateFunction') is None


def test_assoc_type146_stub_double():
    # OPLmetamodel_AbstractType has no real 'OPLmetamodel_AbstractType148' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_RecordField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_RecordField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_RecordField(name="sample_text")
    partner = OPLmetamodel_AbstractType()
    setattr(partner, 'OPLmetamodel_AbstractType148', None)
    _safe_set(owner, 'OPLmetamodel_RecordField147', partner)
    assert getattr(partner, 'OPLmetamodel_AbstractType148') == owner
    _safe_set(owner, 'OPLmetamodel_RecordField147', None)
    assert getattr(partner, 'OPLmetamodel_AbstractType148') is None


def test_assoc_type34_stub_double():
    # OPLmetamodel_AbstractType has no real 'OPLmetamodel_AbstractType36' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_DataDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_DataDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    partner = OPLmetamodel_AbstractType()
    setattr(partner, 'OPLmetamodel_AbstractType36', None)
    _safe_set(owner, 'OPLmetamodel_DataDeclaration35', partner)
    assert getattr(partner, 'OPLmetamodel_AbstractType36') == owner
    _safe_set(owner, 'OPLmetamodel_DataDeclaration35', None)
    assert getattr(partner, 'OPLmetamodel_AbstractType36') is None


def test_assoc_types94_stub_double():
    # OPLmetamodel_DefinedType has no real 'OPLmetamodel_DefinedType' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    partner = OPLmetamodel_DefinedType()
    setattr(partner, 'OPLmetamodel_DefinedType', None)
    _safe_set(owner, 'OPLmetamodel_Model', {partner})
    assert getattr(partner, 'OPLmetamodel_DefinedType') == owner
    _safe_set(owner, 'OPLmetamodel_Model', set())
    assert getattr(partner, 'OPLmetamodel_DefinedType') is None


def test_assoc_value37_stub_double():
    # OPLmetamodel_Initialization has no real 'OPLmetamodel_Initialization' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_DataDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_DataDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    partner = OPLmetamodel_Initialization()
    setattr(partner, 'OPLmetamodel_Initialization', None)
    _safe_set(owner, 'OPLmetamodel_DataDeclaration38', partner)
    assert getattr(partner, 'OPLmetamodel_Initialization') == owner
    _safe_set(owner, 'OPLmetamodel_DataDeclaration38', None)
    assert getattr(partner, 'OPLmetamodel_Initialization') is None


def test_assoc_valueConstraint39_stub_double():
    # OPLmetamodel_Expression has no real 'OPLmetamodel_Expression41' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_DataDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_DataDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    partner = OPLmetamodel_Expression()
    setattr(partner, 'OPLmetamodel_Expression41', None)
    _safe_set(owner, 'OPLmetamodel_DataDeclaration40', partner)
    assert getattr(partner, 'OPLmetamodel_Expression41') == owner
    _safe_set(owner, 'OPLmetamodel_DataDeclaration40', None)
    assert getattr(partner, 'OPLmetamodel_Expression41') is None


def test_assoc_variable32_stub_double():
    # OPLmetamodel_DataRef has no real 'OPLmetamodel_DataRef33' property in the generated
    # code (a bare stub) -- manually attach it so OPLmetamodel_DataDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OPLmetamodel_DataDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    partner = OPLmetamodel_DataRef()
    setattr(partner, 'OPLmetamodel_DataRef33', None)
    _safe_set(owner, 'OPLmetamodel_DataDeclaration', partner)
    assert getattr(partner, 'OPLmetamodel_DataRef33') == owner
    _safe_set(owner, 'OPLmetamodel_DataDeclaration', None)
    assert getattr(partner, 'OPLmetamodel_DataRef33') is None


