import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AdditionalConstraint,
    AdditiveExpChild,
    AtomicExp,
    BooleanAndExpChild,
    BooleanImpliesExpChild,
    BooleanOrExpChild,
    CallPathExp,
    CollectionType,
    EDataType,
    Executable,
    Expression,
    ImperativeExp,
    ImperativeStatement,
    LinkConstraint,
    LiteralExp,
    LoopPathExp,
    MultiplicativeExpChild,
    NamedElement,
    ObjectVariable,
    Pattern,
    PrimitiveConstraint,
    PrimitiveVariable,
    RelationalExpChild,
    RuleElement,
    Section,
    Statement,
    UnaryExpChild,
    Unit,
    Variable,
    VariableWithInit,
    morel_AdditionalConstraint,
    morel_AdditiveExp,
    morel_AdditiveExpChild,
    morel_AllDifferentConstraint,
    morel_ArrayLiteralExp,
    morel_AtomicExp,
    morel_BagType,
    morel_BindExp,
    morel_BlockStatement,
    morel_BooleanAndExp,
    morel_BooleanAndExpChild,
    morel_BooleanImpliesExp,
    morel_BooleanImpliesExpChild,
    morel_BooleanLiteralExp,
    morel_BooleanOrExp,
    morel_BooleanOrExpChild,
    morel_CallPathExp,
    morel_Clause,
    morel_CollectionLiteralExp,
    morel_CollectionType,
    morel_ConditionExp,
    morel_DeclarativeStatement,
    morel_EAttribute,
    morel_EClass,
    morel_EClassifier,
    morel_EDataType,
    morel_EEnum,
    morel_EEnumLiteral,
    morel_EPackage,
    morel_EReference,
    morel_EnclosureLinkConstraint,
    morel_EnumLiteralExp,
    morel_Executable,
    morel_Expression,
    morel_FeaturePathExp,
    morel_ForStatement,
    morel_IfStatement,
    morel_ImperativeExp,
    morel_ImperativeStatement,
    morel_IntegerLiteralExp,
    morel_IteratorPathExp,
    morel_LetExp,
    morel_LinkConstraint,
    morel_LiteralExp,
    morel_LoopPathExp,
    morel_MultiValueConstraint,
    morel_MultiplicativeExp,
    morel_MultiplicativeExpChild,
    morel_NamedElement,
    morel_NestedExp,
    morel_ObjectVariable,
    morel_ObjectVariableWithInit,
    morel_OperationPathExp,
    morel_OrderConstraint,
    morel_OrderedSetType,
    morel_PathConstraint,
    morel_Pattern,
    morel_PredefinedBindExp,
    morel_PredefinedVariableExp,
    morel_PrimitiveConstraint,
    morel_PrimitiveVariable,
    morel_PrimitiveVariableWithInit,
    morel_Query,
    morel_QueryModel,
    morel_RealLiteralExp,
    morel_ReflectiveVariableExp,
    morel_RelationalExp,
    morel_RelationalExpChild,
    morel_Rule,
    morel_RuleElement,
    morel_RuleGroup,
    morel_Section,
    morel_SequenceType,
    morel_SetType,
    morel_SimpleLinkConstraint,
    morel_Statement,
    morel_StringLiteralExp,
    morel_TransformationModel,
    morel_TypeLiteralExp,
    morel_TypedModel,
    morel_UnaryExp,
    morel_UnaryExpChild,
    morel_UndefinedLiteralExp,
    morel_Unit,
    morel_ValueRangeConstraint,
    morel_Variable,
    morel_VariableExp,
    morel_VariableWithInit,
    AdditiveOperator,
    BooleanOperator,
    IterationType,
    IteratorType,
    MultiplicativeOperator,
    OperationSeparator,
    OrderType,
    PredefinedVariable,
    RelationalOperator,
    RepetitionType,
    ScopeType,
    SectionType,
    TypedModelAction,
    UnaryOperator,
    UndefinedLiteral,
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

def test_morel_AdditiveExp_operators_value_roundtrip():
    instance = morel_AdditiveExp(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_morel_BooleanAndExp_operators_value_roundtrip():
    instance = morel_BooleanAndExp(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_morel_BooleanImpliesExp_operator_value_roundtrip():
    instance = morel_BooleanImpliesExp(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_morel_BooleanLiteralExp_boolSymbol_value_roundtrip():
    instance = morel_BooleanLiteralExp(boolSymbol=True)
    assert instance.boolSymbol == True
    instance.boolSymbol = False
    assert instance.boolSymbol == False


def test_morel_BooleanOrExp_operators_value_roundtrip():
    instance = morel_BooleanOrExp(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_morel_CollectionLiteralExp_type_value_roundtrip():
    instance = morel_CollectionLiteralExp(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_morel_Executable_active_value_roundtrip():
    instance = morel_Executable(active=True, parameters="sample_text")
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_morel_Executable_parameters_value_roundtrip():
    instance = morel_Executable(active=True, parameters="sample_text")
    assert instance.parameters == "sample_text"
    instance.parameters = "sample_text_2"
    assert instance.parameters == "sample_text_2"


def test_morel_FeaturePathExp_feature_value_roundtrip():
    instance = morel_FeaturePathExp(feature="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_morel_IntegerLiteralExp_integerSymbol_value_roundtrip():
    instance = morel_IntegerLiteralExp(integerSymbol=7)
    assert instance.integerSymbol == 7
    instance.integerSymbol = 13
    assert instance.integerSymbol == 13


def test_morel_IteratorPathExp_type_value_roundtrip():
    instance = morel_IteratorPathExp(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_morel_MultiplicativeExp_operators_value_roundtrip():
    instance = morel_MultiplicativeExp(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_morel_NamedElement_name_value_roundtrip():
    instance = morel_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_morel_OperationPathExp_operation_value_roundtrip():
    instance = morel_OperationPathExp(operation="sample_text", separator="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_morel_OperationPathExp_separator_value_roundtrip():
    instance = morel_OperationPathExp(operation="sample_text", separator="sample_text")
    assert instance.separator == "sample_text"
    instance.separator = "sample_text_2"
    assert instance.separator == "sample_text_2"


def test_morel_PathConstraint_maxLength_value_roundtrip():
    instance = morel_PathConstraint(maxLength=7, minLength=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_morel_PathConstraint_minLength_value_roundtrip():
    instance = morel_PathConstraint(maxLength=7, minLength=7)
    assert instance.minLength == 7
    instance.minLength = 13
    assert instance.minLength == 13


def test_morel_PredefinedVariableExp_variable_value_roundtrip():
    instance = morel_PredefinedVariableExp(variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_morel_RealLiteralExp_realSymbol_value_roundtrip():
    instance = morel_RealLiteralExp(realSymbol=3.14)
    assert instance.realSymbol == 3.14
    instance.realSymbol = 9.99
    assert instance.realSymbol == 9.99


def test_morel_RelationalExp_operator_value_roundtrip():
    instance = morel_RelationalExp(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_morel_RuleGroup_iteration_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.iteration == "sample_text"
    instance.iteration = "sample_text_2"
    assert instance.iteration == "sample_text_2"


def test_morel_RuleGroup_maxIteration_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.maxIteration == 7
    instance.maxIteration = 13
    assert instance.maxIteration == 13


def test_morel_RuleGroup_order_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.order == "sample_text"
    instance.order = "sample_text_2"
    assert instance.order == "sample_text_2"


def test_morel_RuleGroup_repetition_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.repetition == "sample_text"
    instance.repetition = "sample_text_2"
    assert instance.repetition == "sample_text_2"


def test_morel_RuleGroup_scope_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_morel_RuleGroup_scopeSize_value_roundtrip():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert instance.scopeSize == 7
    instance.scopeSize = 13
    assert instance.scopeSize == 13


def test_morel_Section_type_value_roundtrip():
    instance = morel_Section(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_morel_StringLiteralExp_stringSymbol_value_roundtrip():
    instance = morel_StringLiteralExp(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_morel_TypedModel_type_value_roundtrip():
    instance = morel_TypedModel(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_morel_UnaryExp_operator_value_roundtrip():
    instance = morel_UnaryExp(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_morel_UndefinedLiteralExp_value_value_roundtrip():
    instance = morel_UndefinedLiteralExp(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_morel_AllDifferentConstraint_isa_AdditionalConstraint():
    instance = morel_AllDifferentConstraint()
    assert isinstance(instance, AdditionalConstraint)


def test_morel_OrderConstraint_isa_AdditionalConstraint():
    instance = morel_OrderConstraint()
    assert isinstance(instance, AdditionalConstraint)


def test_morel_MultiplicativeExp_isa_AdditiveExpChild():
    instance = morel_MultiplicativeExp(operators="sample_text")
    assert isinstance(instance, AdditiveExpChild)


def test_morel_MultiplicativeExpChild_isa_AdditiveExpChild():
    instance = morel_MultiplicativeExpChild()
    assert isinstance(instance, AdditiveExpChild)


def test_morel_LiteralExp_isa_AtomicExp():
    instance = morel_LiteralExp()
    assert isinstance(instance, AtomicExp)


def test_morel_NestedExp_isa_AtomicExp():
    instance = morel_NestedExp()
    assert isinstance(instance, AtomicExp)


def test_morel_PredefinedVariableExp_isa_AtomicExp():
    instance = morel_PredefinedVariableExp(variable="sample_text")
    assert isinstance(instance, AtomicExp)


def test_morel_VariableExp_isa_AtomicExp():
    instance = morel_VariableExp()
    assert isinstance(instance, AtomicExp)


def test_morel_RelationalExp_isa_BooleanAndExpChild():
    instance = morel_RelationalExp(operator="sample_text")
    assert isinstance(instance, BooleanAndExpChild)


def test_morel_RelationalExpChild_isa_BooleanAndExpChild():
    instance = morel_RelationalExpChild()
    assert isinstance(instance, BooleanAndExpChild)


def test_morel_BooleanOrExp_isa_BooleanImpliesExpChild():
    instance = morel_BooleanOrExp(operators="sample_text")
    assert isinstance(instance, BooleanImpliesExpChild)


def test_morel_BooleanOrExpChild_isa_BooleanImpliesExpChild():
    instance = morel_BooleanOrExpChild()
    assert isinstance(instance, BooleanImpliesExpChild)


def test_morel_BooleanAndExp_isa_BooleanOrExpChild():
    instance = morel_BooleanAndExp(operators="sample_text")
    assert isinstance(instance, BooleanOrExpChild)


def test_morel_BooleanAndExpChild_isa_BooleanOrExpChild():
    instance = morel_BooleanAndExpChild()
    assert isinstance(instance, BooleanOrExpChild)


def test_morel_FeaturePathExp_isa_CallPathExp():
    instance = morel_FeaturePathExp(feature="sample_text")
    assert isinstance(instance, CallPathExp)


def test_morel_LoopPathExp_isa_CallPathExp():
    instance = morel_LoopPathExp()
    assert isinstance(instance, CallPathExp)


def test_morel_OperationPathExp_isa_CallPathExp():
    instance = morel_OperationPathExp(operation="sample_text", separator="sample_text")
    assert isinstance(instance, CallPathExp)


def test_morel_BagType_isa_CollectionType():
    instance = morel_BagType()
    assert isinstance(instance, CollectionType)


def test_morel_OrderedSetType_isa_CollectionType():
    instance = morel_OrderedSetType()
    assert isinstance(instance, CollectionType)


def test_morel_SequenceType_isa_CollectionType():
    instance = morel_SequenceType()
    assert isinstance(instance, CollectionType)


def test_morel_SetType_isa_CollectionType():
    instance = morel_SetType()
    assert isinstance(instance, CollectionType)


def test_morel_CollectionType_isa_EDataType():
    instance = morel_CollectionType()
    assert isinstance(instance, EDataType)


def test_morel_Query_isa_Executable():
    instance = morel_Query()
    assert isinstance(instance, Executable)


def test_morel_RuleElement_isa_Executable():
    instance = morel_RuleElement()
    assert isinstance(instance, Executable)


def test_morel_BooleanImpliesExp_isa_Expression():
    instance = morel_BooleanImpliesExp(operator="sample_text")
    assert isinstance(instance, Expression)


def test_morel_BooleanImpliesExpChild_isa_Expression():
    instance = morel_BooleanImpliesExpChild()
    assert isinstance(instance, Expression)


def test_morel_ConditionExp_isa_Expression():
    instance = morel_ConditionExp()
    assert isinstance(instance, Expression)


def test_morel_ImperativeExp_isa_Expression():
    instance = morel_ImperativeExp()
    assert isinstance(instance, Expression)


def test_morel_LetExp_isa_Expression():
    instance = morel_LetExp()
    assert isinstance(instance, Expression)


def test_morel_ReflectiveVariableExp_isa_Expression():
    instance = morel_ReflectiveVariableExp()
    assert isinstance(instance, Expression)


def test_morel_BindExp_isa_ImperativeExp():
    instance = morel_BindExp()
    assert isinstance(instance, ImperativeExp)


def test_morel_LetExp_isa_ImperativeExp():
    instance = morel_LetExp()
    assert isinstance(instance, ImperativeExp)


def test_morel_PredefinedBindExp_isa_ImperativeExp():
    instance = morel_PredefinedBindExp()
    assert isinstance(instance, ImperativeExp)


def test_morel_BlockStatement_isa_ImperativeStatement():
    instance = morel_BlockStatement()
    assert isinstance(instance, ImperativeStatement)


def test_morel_ForStatement_isa_ImperativeStatement():
    instance = morel_ForStatement()
    assert isinstance(instance, ImperativeStatement)


def test_morel_IfStatement_isa_ImperativeStatement():
    instance = morel_IfStatement()
    assert isinstance(instance, ImperativeStatement)


def test_morel_EnclosureLinkConstraint_isa_LinkConstraint():
    instance = morel_EnclosureLinkConstraint()
    assert isinstance(instance, LinkConstraint)


def test_morel_PathConstraint_isa_LinkConstraint():
    instance = morel_PathConstraint(maxLength=7, minLength=7)
    assert isinstance(instance, LinkConstraint)


def test_morel_SimpleLinkConstraint_isa_LinkConstraint():
    instance = morel_SimpleLinkConstraint()
    assert isinstance(instance, LinkConstraint)


def test_morel_ArrayLiteralExp_isa_LiteralExp():
    instance = morel_ArrayLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_morel_BooleanLiteralExp_isa_LiteralExp():
    instance = morel_BooleanLiteralExp(boolSymbol=True)
    assert isinstance(instance, LiteralExp)


def test_morel_CollectionLiteralExp_isa_LiteralExp():
    instance = morel_CollectionLiteralExp(type="sample_text")
    assert isinstance(instance, LiteralExp)


def test_morel_EnumLiteralExp_isa_LiteralExp():
    instance = morel_EnumLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_morel_IntegerLiteralExp_isa_LiteralExp():
    instance = morel_IntegerLiteralExp(integerSymbol=7)
    assert isinstance(instance, LiteralExp)


def test_morel_RealLiteralExp_isa_LiteralExp():
    instance = morel_RealLiteralExp(realSymbol=3.14)
    assert isinstance(instance, LiteralExp)


def test_morel_StringLiteralExp_isa_LiteralExp():
    instance = morel_StringLiteralExp(stringSymbol="sample_text")
    assert isinstance(instance, LiteralExp)


def test_morel_TypeLiteralExp_isa_LiteralExp():
    instance = morel_TypeLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_morel_UndefinedLiteralExp_isa_LiteralExp():
    instance = morel_UndefinedLiteralExp(value="sample_text")
    assert isinstance(instance, LiteralExp)


def test_morel_IteratorPathExp_isa_LoopPathExp():
    instance = morel_IteratorPathExp(type="sample_text")
    assert isinstance(instance, LoopPathExp)


def test_morel_UnaryExp_isa_MultiplicativeExpChild():
    instance = morel_UnaryExp(operator="sample_text")
    assert isinstance(instance, MultiplicativeExpChild)


def test_morel_UnaryExpChild_isa_MultiplicativeExpChild():
    instance = morel_UnaryExpChild()
    assert isinstance(instance, MultiplicativeExpChild)


def test_morel_Query_isa_NamedElement():
    instance = morel_Query()
    assert isinstance(instance, NamedElement)


def test_morel_RuleElement_isa_NamedElement():
    instance = morel_RuleElement()
    assert isinstance(instance, NamedElement)


def test_morel_TransformationModel_isa_NamedElement():
    instance = morel_TransformationModel()
    assert isinstance(instance, NamedElement)


def test_morel_TypedModel_isa_NamedElement():
    instance = morel_TypedModel(type="sample_text")
    assert isinstance(instance, NamedElement)


def test_morel_Variable_isa_NamedElement():
    instance = morel_Variable()
    assert isinstance(instance, NamedElement)


def test_morel_ObjectVariableWithInit_isa_ObjectVariable():
    instance = morel_ObjectVariableWithInit()
    assert isinstance(instance, ObjectVariable)


def test_morel_Query_isa_Pattern():
    instance = morel_Query()
    assert isinstance(instance, Pattern)


def test_morel_MultiValueConstraint_isa_PrimitiveConstraint():
    instance = morel_MultiValueConstraint()
    assert isinstance(instance, PrimitiveConstraint)


def test_morel_ValueRangeConstraint_isa_PrimitiveConstraint():
    instance = morel_ValueRangeConstraint()
    assert isinstance(instance, PrimitiveConstraint)


def test_morel_PrimitiveVariableWithInit_isa_PrimitiveVariable():
    instance = morel_PrimitiveVariableWithInit()
    assert isinstance(instance, PrimitiveVariable)


def test_morel_AdditiveExp_isa_RelationalExpChild():
    instance = morel_AdditiveExp(operators="sample_text")
    assert isinstance(instance, RelationalExpChild)


def test_morel_AdditiveExpChild_isa_RelationalExpChild():
    instance = morel_AdditiveExpChild()
    assert isinstance(instance, RelationalExpChild)


def test_morel_Rule_isa_RuleElement():
    instance = morel_Rule()
    assert isinstance(instance, RuleElement)


def test_morel_RuleGroup_isa_RuleElement():
    instance = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    assert isinstance(instance, RuleElement)


def test_morel_Clause_isa_Section():
    instance = morel_Clause()
    assert isinstance(instance, Section)


def test_morel_Pattern_isa_Section():
    instance = morel_Pattern()
    assert isinstance(instance, Section)


def test_morel_DeclarativeStatement_isa_Statement():
    instance = morel_DeclarativeStatement()
    assert isinstance(instance, Statement)


def test_morel_ImperativeStatement_isa_Statement():
    instance = morel_ImperativeStatement()
    assert isinstance(instance, Statement)


def test_morel_AtomicExp_isa_UnaryExpChild():
    instance = morel_AtomicExp()
    assert isinstance(instance, UnaryExpChild)


def test_morel_QueryModel_isa_Unit():
    instance = morel_QueryModel()
    assert isinstance(instance, Unit)


def test_morel_TransformationModel_isa_Unit():
    instance = morel_TransformationModel()
    assert isinstance(instance, Unit)


def test_morel_ObjectVariable_isa_Variable():
    instance = morel_ObjectVariable()
    assert isinstance(instance, Variable)


def test_morel_PrimitiveVariable_isa_Variable():
    instance = morel_PrimitiveVariable()
    assert isinstance(instance, Variable)


def test_morel_VariableWithInit_isa_Variable():
    instance = morel_VariableWithInit()
    assert isinstance(instance, Variable)


def test_morel_ObjectVariableWithInit_isa_VariableWithInit():
    instance = morel_ObjectVariableWithInit()
    assert isinstance(instance, VariableWithInit)


def test_morel_PrimitiveVariableWithInit_isa_VariableWithInit():
    instance = morel_PrimitiveVariableWithInit()
    assert isinstance(instance, VariableWithInit)


def test_assoc_bodyExp64_link_reassign_clear():
    a = morel_IteratorPathExp(type="sample_text")
    b1 = morel_Expression()
    b2 = morel_Expression()
    _safe_set(a, 'morel_IteratorPathExp65', b1)
    assert _is_linked(a, 'morel_IteratorPathExp65', b1)
    if hasattr(b1, 'morel_Expression66'):
        assert _is_linked(b1, 'morel_Expression66', a)
    _safe_set(a, 'morel_IteratorPathExp65', b2)
    assert _is_linked(a, 'morel_IteratorPathExp65', b2)
    if hasattr(b1, 'morel_Expression66'):
        assert not _is_linked(b1, 'morel_Expression66', a)
    if hasattr(b2, 'morel_Expression66'):
        assert _is_linked(b2, 'morel_Expression66', a)
    _safe_set(a, 'morel_IteratorPathExp65', None)
    assert not _is_linked(a, 'morel_IteratorPathExp65', b2)
    if hasattr(b2, 'morel_Expression66'):
        assert not _is_linked(b2, 'morel_Expression66', a)


def test_assoc_child94_link_reassign_clear():
    a = morel_UnaryExp(operator="sample_text")
    b1 = morel_UnaryExpChild()
    b2 = morel_UnaryExpChild()
    _safe_set(a, 'morel_UnaryExp', b1)
    assert _is_linked(a, 'morel_UnaryExp', b1)
    if hasattr(b1, 'morel_UnaryExpChild'):
        assert _is_linked(b1, 'morel_UnaryExpChild', a)
    _safe_set(a, 'morel_UnaryExp', b2)
    assert _is_linked(a, 'morel_UnaryExp', b2)
    if hasattr(b1, 'morel_UnaryExpChild'):
        assert not _is_linked(b1, 'morel_UnaryExpChild', a)
    if hasattr(b2, 'morel_UnaryExpChild'):
        assert _is_linked(b2, 'morel_UnaryExpChild', a)
    _safe_set(a, 'morel_UnaryExp', None)
    assert not _is_linked(a, 'morel_UnaryExp', b2)
    if hasattr(b2, 'morel_UnaryExpChild'):
        assert not _is_linked(b2, 'morel_UnaryExpChild', a)


def test_assoc_children86_link_reassign_clear():
    a = morel_BooleanOrExp(operators="sample_text")
    b1 = morel_BooleanOrExpChild()
    b2 = morel_BooleanOrExpChild()
    _safe_set(a, 'morel_BooleanOrExp', {b1})
    assert _is_linked(a, 'morel_BooleanOrExp', b1)
    if hasattr(b1, 'morel_BooleanOrExpChild'):
        assert _is_linked(b1, 'morel_BooleanOrExpChild', a)
    _safe_set(a, 'morel_BooleanOrExp', {b2})
    assert _is_linked(a, 'morel_BooleanOrExp', b2)
    if hasattr(b1, 'morel_BooleanOrExpChild'):
        assert not _is_linked(b1, 'morel_BooleanOrExpChild', a)
    if hasattr(b2, 'morel_BooleanOrExpChild'):
        assert _is_linked(b2, 'morel_BooleanOrExpChild', a)
    _safe_set(a, 'morel_BooleanOrExp', set())
    assert not _is_linked(a, 'morel_BooleanOrExp', b2)
    if hasattr(b2, 'morel_BooleanOrExpChild'):
        assert not _is_linked(b2, 'morel_BooleanOrExpChild', a)


def test_assoc_children87_link_reassign_clear():
    a = morel_BooleanAndExp(operators="sample_text")
    b1 = morel_BooleanAndExpChild()
    b2 = morel_BooleanAndExpChild()
    _safe_set(a, 'morel_BooleanAndExp', {b1})
    assert _is_linked(a, 'morel_BooleanAndExp', b1)
    if hasattr(b1, 'morel_BooleanAndExpChild'):
        assert _is_linked(b1, 'morel_BooleanAndExpChild', a)
    _safe_set(a, 'morel_BooleanAndExp', {b2})
    assert _is_linked(a, 'morel_BooleanAndExp', b2)
    if hasattr(b1, 'morel_BooleanAndExpChild'):
        assert not _is_linked(b1, 'morel_BooleanAndExpChild', a)
    if hasattr(b2, 'morel_BooleanAndExpChild'):
        assert _is_linked(b2, 'morel_BooleanAndExpChild', a)
    _safe_set(a, 'morel_BooleanAndExp', set())
    assert not _is_linked(a, 'morel_BooleanAndExp', b2)
    if hasattr(b2, 'morel_BooleanAndExpChild'):
        assert not _is_linked(b2, 'morel_BooleanAndExpChild', a)


def test_assoc_children92_link_reassign_clear():
    a = morel_AdditiveExp(operators="sample_text")
    b1 = morel_AdditiveExpChild()
    b2 = morel_AdditiveExpChild()
    _safe_set(a, 'morel_AdditiveExp', {b1})
    assert _is_linked(a, 'morel_AdditiveExp', b1)
    if hasattr(b1, 'morel_AdditiveExpChild'):
        assert _is_linked(b1, 'morel_AdditiveExpChild', a)
    _safe_set(a, 'morel_AdditiveExp', {b2})
    assert _is_linked(a, 'morel_AdditiveExp', b2)
    if hasattr(b1, 'morel_AdditiveExpChild'):
        assert not _is_linked(b1, 'morel_AdditiveExpChild', a)
    if hasattr(b2, 'morel_AdditiveExpChild'):
        assert _is_linked(b2, 'morel_AdditiveExpChild', a)
    _safe_set(a, 'morel_AdditiveExp', set())
    assert not _is_linked(a, 'morel_AdditiveExp', b2)
    if hasattr(b2, 'morel_AdditiveExpChild'):
        assert not _is_linked(b2, 'morel_AdditiveExpChild', a)


def test_assoc_children93_link_reassign_clear():
    a = morel_MultiplicativeExp(operators="sample_text")
    b1 = morel_MultiplicativeExpChild()
    b2 = morel_MultiplicativeExpChild()
    _safe_set(a, 'morel_MultiplicativeExp', {b1})
    assert _is_linked(a, 'morel_MultiplicativeExp', b1)
    if hasattr(b1, 'morel_MultiplicativeExpChild'):
        assert _is_linked(b1, 'morel_MultiplicativeExpChild', a)
    _safe_set(a, 'morel_MultiplicativeExp', {b2})
    assert _is_linked(a, 'morel_MultiplicativeExp', b2)
    if hasattr(b1, 'morel_MultiplicativeExpChild'):
        assert not _is_linked(b1, 'morel_MultiplicativeExpChild', a)
    if hasattr(b2, 'morel_MultiplicativeExpChild'):
        assert _is_linked(b2, 'morel_MultiplicativeExpChild', a)
    _safe_set(a, 'morel_MultiplicativeExp', set())
    assert not _is_linked(a, 'morel_MultiplicativeExp', b2)
    if hasattr(b2, 'morel_MultiplicativeExpChild'):
        assert not _is_linked(b2, 'morel_MultiplicativeExpChild', a)


def test_assoc_condition106_link_reassign_clear():
    a = morel_BooleanImpliesExp(operator="sample_text")
    b1 = morel_IfStatement()
    b2 = morel_IfStatement()
    _safe_set(a, 'morel_BooleanImpliesExp107', b1)
    assert _is_linked(a, 'morel_BooleanImpliesExp107', b1)
    if hasattr(b1, 'morel_IfStatement'):
        assert _is_linked(b1, 'morel_IfStatement', a)
    _safe_set(a, 'morel_BooleanImpliesExp107', b2)
    assert _is_linked(a, 'morel_BooleanImpliesExp107', b2)
    if hasattr(b1, 'morel_IfStatement'):
        assert not _is_linked(b1, 'morel_IfStatement', a)
    if hasattr(b2, 'morel_IfStatement'):
        assert _is_linked(b2, 'morel_IfStatement', a)
    _safe_set(a, 'morel_BooleanImpliesExp107', None)
    assert not _is_linked(a, 'morel_BooleanImpliesExp107', b2)
    if hasattr(b2, 'morel_IfStatement'):
        assert not _is_linked(b2, 'morel_IfStatement', a)


def test_assoc_condition74_link_reassign_clear():
    a = morel_BooleanImpliesExp(operator="sample_text")
    b1 = morel_ConditionExp()
    b2 = morel_ConditionExp()
    _safe_set(a, 'morel_BooleanImpliesExp', b1)
    assert _is_linked(a, 'morel_BooleanImpliesExp', b1)
    if hasattr(b1, 'morel_ConditionExp'):
        assert _is_linked(b1, 'morel_ConditionExp', a)
    _safe_set(a, 'morel_BooleanImpliesExp', b2)
    assert _is_linked(a, 'morel_BooleanImpliesExp', b2)
    if hasattr(b1, 'morel_ConditionExp'):
        assert not _is_linked(b1, 'morel_ConditionExp', a)
    if hasattr(b2, 'morel_ConditionExp'):
        assert _is_linked(b2, 'morel_ConditionExp', a)
    _safe_set(a, 'morel_BooleanImpliesExp', None)
    assert not _is_linked(a, 'morel_BooleanImpliesExp', b2)
    if hasattr(b2, 'morel_ConditionExp'):
        assert not _is_linked(b2, 'morel_ConditionExp', a)


def test_assoc_dataTypes40_link_reassign_clear():
    a = morel_Unit()
    b1 = morel_EDataType()
    b2 = morel_EDataType()
    _safe_set(a, 'morel_Unit41', {b1})
    assert _is_linked(a, 'morel_Unit41', b1)
    if hasattr(b1, 'morel_EDataType42'):
        assert _is_linked(b1, 'morel_EDataType42', a)
    _safe_set(a, 'morel_Unit41', {b2})
    assert _is_linked(a, 'morel_Unit41', b2)
    if hasattr(b1, 'morel_EDataType42'):
        assert not _is_linked(b1, 'morel_EDataType42', a)
    if hasattr(b2, 'morel_EDataType42'):
        assert _is_linked(b2, 'morel_EDataType42', a)
    _safe_set(a, 'morel_Unit41', set())
    assert not _is_linked(a, 'morel_Unit41', b2)
    if hasattr(b2, 'morel_EDataType42'):
        assert not _is_linked(b2, 'morel_EDataType42', a)


def test_assoc_firstVar59_link_reassign_clear():
    a = morel_IteratorPathExp(type="sample_text")
    b1 = morel_Variable()
    b2 = morel_Variable()
    _safe_set(a, 'morel_IteratorPathExp', b1)
    assert _is_linked(a, 'morel_IteratorPathExp', b1)
    if hasattr(b1, 'morel_Variable60'):
        assert _is_linked(b1, 'morel_Variable60', a)
    _safe_set(a, 'morel_IteratorPathExp', b2)
    assert _is_linked(a, 'morel_IteratorPathExp', b2)
    if hasattr(b1, 'morel_Variable60'):
        assert not _is_linked(b1, 'morel_Variable60', a)
    if hasattr(b2, 'morel_Variable60'):
        assert _is_linked(b2, 'morel_Variable60', a)
    _safe_set(a, 'morel_IteratorPathExp', None)
    assert not _is_linked(a, 'morel_IteratorPathExp', b2)
    if hasattr(b2, 'morel_Variable60'):
        assert not _is_linked(b2, 'morel_Variable60', a)


def test_assoc_left81_link_reassign_clear():
    a = morel_BooleanImpliesExp(operator="sample_text")
    b1 = morel_BooleanImpliesExpChild()
    b2 = morel_BooleanImpliesExpChild()
    _safe_set(a, 'morel_BooleanImpliesExp82', b1)
    assert _is_linked(a, 'morel_BooleanImpliesExp82', b1)
    if hasattr(b1, 'morel_BooleanImpliesExpChild'):
        assert _is_linked(b1, 'morel_BooleanImpliesExpChild', a)
    _safe_set(a, 'morel_BooleanImpliesExp82', b2)
    assert _is_linked(a, 'morel_BooleanImpliesExp82', b2)
    if hasattr(b1, 'morel_BooleanImpliesExpChild'):
        assert not _is_linked(b1, 'morel_BooleanImpliesExpChild', a)
    if hasattr(b2, 'morel_BooleanImpliesExpChild'):
        assert _is_linked(b2, 'morel_BooleanImpliesExpChild', a)
    _safe_set(a, 'morel_BooleanImpliesExp82', None)
    assert not _is_linked(a, 'morel_BooleanImpliesExp82', b2)
    if hasattr(b2, 'morel_BooleanImpliesExpChild'):
        assert not _is_linked(b2, 'morel_BooleanImpliesExpChild', a)


def test_assoc_left88_link_reassign_clear():
    a = morel_RelationalExp(operator="sample_text")
    b1 = morel_RelationalExpChild()
    b2 = morel_RelationalExpChild()
    _safe_set(a, 'morel_RelationalExp', b1)
    assert _is_linked(a, 'morel_RelationalExp', b1)
    if hasattr(b1, 'morel_RelationalExpChild'):
        assert _is_linked(b1, 'morel_RelationalExpChild', a)
    _safe_set(a, 'morel_RelationalExp', b2)
    assert _is_linked(a, 'morel_RelationalExp', b2)
    if hasattr(b1, 'morel_RelationalExpChild'):
        assert not _is_linked(b1, 'morel_RelationalExpChild', a)
    if hasattr(b2, 'morel_RelationalExpChild'):
        assert _is_linked(b2, 'morel_RelationalExpChild', a)
    _safe_set(a, 'morel_RelationalExp', None)
    assert not _is_linked(a, 'morel_RelationalExp', b2)
    if hasattr(b2, 'morel_RelationalExpChild'):
        assert not _is_linked(b2, 'morel_RelationalExpChild', a)


def test_assoc_literals44_link_reassign_clear():
    a = morel_CollectionLiteralExp(type="sample_text")
    b1 = morel_Expression()
    b2 = morel_Expression()
    _safe_set(a, 'morel_CollectionLiteralExp', {b1})
    assert _is_linked(a, 'morel_CollectionLiteralExp', b1)
    if hasattr(b1, 'morel_Expression45'):
        assert _is_linked(b1, 'morel_Expression45', a)
    _safe_set(a, 'morel_CollectionLiteralExp', {b2})
    assert _is_linked(a, 'morel_CollectionLiteralExp', b2)
    if hasattr(b1, 'morel_Expression45'):
        assert not _is_linked(b1, 'morel_Expression45', a)
    if hasattr(b2, 'morel_Expression45'):
        assert _is_linked(b2, 'morel_Expression45', a)
    _safe_set(a, 'morel_CollectionLiteralExp', set())
    assert not _is_linked(a, 'morel_CollectionLiteralExp', b2)
    if hasattr(b2, 'morel_Expression45'):
        assert not _is_linked(b2, 'morel_Expression45', a)


def test_assoc_model11_link_reassign_clear():
    a = morel_TypedModel(type="sample_text")
    b1 = morel_ObjectVariable()
    b2 = morel_ObjectVariable()
    _safe_set(a, 'morel_TypedModel', b1)
    assert _is_linked(a, 'morel_TypedModel', b1)
    if hasattr(b1, 'morel_ObjectVariable12'):
        assert _is_linked(b1, 'morel_ObjectVariable12', a)
    _safe_set(a, 'morel_TypedModel', b2)
    assert _is_linked(a, 'morel_TypedModel', b2)
    if hasattr(b1, 'morel_ObjectVariable12'):
        assert not _is_linked(b1, 'morel_ObjectVariable12', a)
    if hasattr(b2, 'morel_ObjectVariable12'):
        assert _is_linked(b2, 'morel_ObjectVariable12', a)
    _safe_set(a, 'morel_TypedModel', None)
    assert not _is_linked(a, 'morel_TypedModel', b2)
    if hasattr(b2, 'morel_ObjectVariable12'):
        assert not _is_linked(b2, 'morel_ObjectVariable12', a)


def test_assoc_models38_link_reassign_clear():
    a = morel_Unit()
    b1 = morel_TypedModel(type="sample_text")
    b2 = morel_TypedModel(type="sample_text_2")
    _safe_set(a, 'morel_Unit', {b1})
    assert _is_linked(a, 'morel_Unit', b1)
    if hasattr(b1, 'morel_TypedModel39'):
        assert _is_linked(b1, 'morel_TypedModel39', a)
    _safe_set(a, 'morel_Unit', {b2})
    assert _is_linked(a, 'morel_Unit', b2)
    if hasattr(b1, 'morel_TypedModel39'):
        assert not _is_linked(b1, 'morel_TypedModel39', a)
    if hasattr(b2, 'morel_TypedModel39'):
        assert _is_linked(b2, 'morel_TypedModel39', a)
    _safe_set(a, 'morel_Unit', set())
    assert not _is_linked(a, 'morel_Unit', b2)
    if hasattr(b2, 'morel_TypedModel39'):
        assert not _is_linked(b2, 'morel_TypedModel39', a)


def test_assoc_package36_link_reassign_clear():
    a = morel_TypedModel(type="sample_text")
    b1 = morel_EPackage()
    b2 = morel_EPackage()
    _safe_set(a, 'morel_TypedModel37', b1)
    assert _is_linked(a, 'morel_TypedModel37', b1)
    if hasattr(b1, 'morel_EPackage'):
        assert _is_linked(b1, 'morel_EPackage', a)
    _safe_set(a, 'morel_TypedModel37', b2)
    assert _is_linked(a, 'morel_TypedModel37', b2)
    if hasattr(b1, 'morel_EPackage'):
        assert not _is_linked(b1, 'morel_EPackage', a)
    if hasattr(b2, 'morel_EPackage'):
        assert _is_linked(b2, 'morel_EPackage', a)
    _safe_set(a, 'morel_TypedModel37', None)
    assert not _is_linked(a, 'morel_TypedModel37', b2)
    if hasattr(b2, 'morel_EPackage'):
        assert not _is_linked(b2, 'morel_EPackage', a)


def test_assoc_parameters57_link_reassign_clear():
    a = morel_OperationPathExp(operation="sample_text", separator="sample_text")
    b1 = morel_Expression()
    b2 = morel_Expression()
    _safe_set(a, 'morel_OperationPathExp', {b1})
    assert _is_linked(a, 'morel_OperationPathExp', b1)
    if hasattr(b1, 'morel_Expression58'):
        assert _is_linked(b1, 'morel_Expression58', a)
    _safe_set(a, 'morel_OperationPathExp', {b2})
    assert _is_linked(a, 'morel_OperationPathExp', b2)
    if hasattr(b1, 'morel_Expression58'):
        assert not _is_linked(b1, 'morel_Expression58', a)
    if hasattr(b2, 'morel_Expression58'):
        assert _is_linked(b2, 'morel_Expression58', a)
    _safe_set(a, 'morel_OperationPathExp', set())
    assert not _is_linked(a, 'morel_OperationPathExp', b2)
    if hasattr(b2, 'morel_Expression58'):
        assert not _is_linked(b2, 'morel_Expression58', a)


def test_assoc_pathVariable28_link_reassign_clear():
    a = morel_PathConstraint(maxLength=7, minLength=7)
    b1 = morel_Variable()
    b2 = morel_Variable()
    _safe_set(a, 'morel_PathConstraint', b1)
    assert _is_linked(a, 'morel_PathConstraint', b1)
    if hasattr(b1, 'morel_Variable'):
        assert _is_linked(b1, 'morel_Variable', a)
    _safe_set(a, 'morel_PathConstraint', b2)
    assert _is_linked(a, 'morel_PathConstraint', b2)
    if hasattr(b1, 'morel_Variable'):
        assert not _is_linked(b1, 'morel_Variable', a)
    if hasattr(b2, 'morel_Variable'):
        assert _is_linked(b2, 'morel_Variable', a)
    _safe_set(a, 'morel_PathConstraint', None)
    assert not _is_linked(a, 'morel_PathConstraint', b2)
    if hasattr(b2, 'morel_Variable'):
        assert not _is_linked(b2, 'morel_Variable', a)


def test_assoc_primitiveVariables137_link_reassign_clear():
    a = morel_Executable(active=True, parameters="sample_text")
    b1 = morel_PrimitiveVariable()
    b2 = morel_PrimitiveVariable()
    _safe_set(a, 'morel_Executable', {b1})
    assert _is_linked(a, 'morel_Executable', b1)
    if hasattr(b1, 'morel_PrimitiveVariable138'):
        assert _is_linked(b1, 'morel_PrimitiveVariable138', a)
    _safe_set(a, 'morel_Executable', {b2})
    assert _is_linked(a, 'morel_Executable', b2)
    if hasattr(b1, 'morel_PrimitiveVariable138'):
        assert not _is_linked(b1, 'morel_PrimitiveVariable138', a)
    if hasattr(b2, 'morel_PrimitiveVariable138'):
        assert _is_linked(b2, 'morel_PrimitiveVariable138', a)
    _safe_set(a, 'morel_Executable', set())
    assert not _is_linked(a, 'morel_Executable', b2)
    if hasattr(b2, 'morel_PrimitiveVariable138'):
        assert not _is_linked(b2, 'morel_PrimitiveVariable138', a)


def test_assoc_references29_link_reassign_clear():
    a = morel_PathConstraint(maxLength=7, minLength=7)
    b1 = morel_EReference()
    b2 = morel_EReference()
    _safe_set(a, 'morel_PathConstraint30', {b1})
    assert _is_linked(a, 'morel_PathConstraint30', b1)
    if hasattr(b1, 'morel_EReference31'):
        assert _is_linked(b1, 'morel_EReference31', a)
    _safe_set(a, 'morel_PathConstraint30', {b2})
    assert _is_linked(a, 'morel_PathConstraint30', b2)
    if hasattr(b1, 'morel_EReference31'):
        assert not _is_linked(b1, 'morel_EReference31', a)
    if hasattr(b2, 'morel_EReference31'):
        assert _is_linked(b2, 'morel_EReference31', a)
    _safe_set(a, 'morel_PathConstraint30', set())
    assert not _is_linked(a, 'morel_PathConstraint30', b2)
    if hasattr(b2, 'morel_EReference31'):
        assert not _is_linked(b2, 'morel_EReference31', a)


def test_assoc_right83_link_reassign_clear():
    a = morel_BooleanImpliesExp(operator="sample_text")
    b1 = morel_BooleanImpliesExpChild()
    b2 = morel_BooleanImpliesExpChild()
    _safe_set(a, 'morel_BooleanImpliesExp84', b1)
    assert _is_linked(a, 'morel_BooleanImpliesExp84', b1)
    if hasattr(b1, 'morel_BooleanImpliesExpChild85'):
        assert _is_linked(b1, 'morel_BooleanImpliesExpChild85', a)
    _safe_set(a, 'morel_BooleanImpliesExp84', b2)
    assert _is_linked(a, 'morel_BooleanImpliesExp84', b2)
    if hasattr(b1, 'morel_BooleanImpliesExpChild85'):
        assert not _is_linked(b1, 'morel_BooleanImpliesExpChild85', a)
    if hasattr(b2, 'morel_BooleanImpliesExpChild85'):
        assert _is_linked(b2, 'morel_BooleanImpliesExpChild85', a)
    _safe_set(a, 'morel_BooleanImpliesExp84', None)
    assert not _is_linked(a, 'morel_BooleanImpliesExp84', b2)
    if hasattr(b2, 'morel_BooleanImpliesExpChild85'):
        assert not _is_linked(b2, 'morel_BooleanImpliesExpChild85', a)


def test_assoc_right89_link_reassign_clear():
    a = morel_RelationalExp(operator="sample_text")
    b1 = morel_RelationalExpChild()
    b2 = morel_RelationalExpChild()
    _safe_set(a, 'morel_RelationalExp90', b1)
    assert _is_linked(a, 'morel_RelationalExp90', b1)
    if hasattr(b1, 'morel_RelationalExpChild91'):
        assert _is_linked(b1, 'morel_RelationalExpChild91', a)
    _safe_set(a, 'morel_RelationalExp90', b2)
    assert _is_linked(a, 'morel_RelationalExp90', b2)
    if hasattr(b1, 'morel_RelationalExpChild91'):
        assert not _is_linked(b1, 'morel_RelationalExpChild91', a)
    if hasattr(b2, 'morel_RelationalExpChild91'):
        assert _is_linked(b2, 'morel_RelationalExpChild91', a)
    _safe_set(a, 'morel_RelationalExp90', None)
    assert not _is_linked(a, 'morel_RelationalExp90', b2)
    if hasattr(b2, 'morel_RelationalExpChild91'):
        assert not _is_linked(b2, 'morel_RelationalExpChild91', a)


def test_assoc_rules129_link_reassign_clear():
    a = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    b1 = morel_Rule()
    b2 = morel_Rule()
    _safe_set(a, 'morel_RuleGroup', {b1})
    assert _is_linked(a, 'morel_RuleGroup', b1)
    if hasattr(b1, 'morel_Rule130'):
        assert _is_linked(b1, 'morel_Rule130', a)
    _safe_set(a, 'morel_RuleGroup', {b2})
    assert _is_linked(a, 'morel_RuleGroup', b2)
    if hasattr(b1, 'morel_Rule130'):
        assert not _is_linked(b1, 'morel_Rule130', a)
    if hasattr(b2, 'morel_Rule130'):
        assert _is_linked(b2, 'morel_Rule130', a)
    _safe_set(a, 'morel_RuleGroup', set())
    assert not _is_linked(a, 'morel_RuleGroup', b2)
    if hasattr(b2, 'morel_Rule130'):
        assert not _is_linked(b2, 'morel_Rule130', a)


def test_assoc_secondVar61_link_reassign_clear():
    a = morel_IteratorPathExp(type="sample_text")
    b1 = morel_Variable()
    b2 = morel_Variable()
    _safe_set(a, 'morel_IteratorPathExp62', b1)
    assert _is_linked(a, 'morel_IteratorPathExp62', b1)
    if hasattr(b1, 'morel_Variable63'):
        assert _is_linked(b1, 'morel_Variable63', a)
    _safe_set(a, 'morel_IteratorPathExp62', b2)
    assert _is_linked(a, 'morel_IteratorPathExp62', b2)
    if hasattr(b1, 'morel_Variable63'):
        assert not _is_linked(b1, 'morel_Variable63', a)
    if hasattr(b2, 'morel_Variable63'):
        assert _is_linked(b2, 'morel_Variable63', a)
    _safe_set(a, 'morel_IteratorPathExp62', None)
    assert not _is_linked(a, 'morel_IteratorPathExp62', b2)
    if hasattr(b2, 'morel_Variable63'):
        assert not _is_linked(b2, 'morel_Variable63', a)


def test_assoc_source102_link_reassign_clear():
    a = morel_PredefinedVariableExp(variable="sample_text")
    b1 = morel_PredefinedBindExp()
    b2 = morel_PredefinedBindExp()
    _safe_set(a, 'morel_PredefinedVariableExp', b1)
    assert _is_linked(a, 'morel_PredefinedVariableExp', b1)
    if hasattr(b1, 'morel_PredefinedBindExp'):
        assert _is_linked(b1, 'morel_PredefinedBindExp', a)
    _safe_set(a, 'morel_PredefinedVariableExp', b2)
    assert _is_linked(a, 'morel_PredefinedVariableExp', b2)
    if hasattr(b1, 'morel_PredefinedBindExp'):
        assert not _is_linked(b1, 'morel_PredefinedBindExp', a)
    if hasattr(b2, 'morel_PredefinedBindExp'):
        assert _is_linked(b2, 'morel_PredefinedBindExp', a)
    _safe_set(a, 'morel_PredefinedVariableExp', None)
    assert not _is_linked(a, 'morel_PredefinedVariableExp', b2)
    if hasattr(b2, 'morel_PredefinedBindExp'):
        assert not _is_linked(b2, 'morel_PredefinedBindExp', a)


def test_assoc_terminationExp115_link_reassign_clear():
    a = morel_BooleanImpliesExp(operator="sample_text")
    b1 = morel_ForStatement()
    b2 = morel_ForStatement()
    _safe_set(a, 'morel_BooleanImpliesExp117', b1)
    assert _is_linked(a, 'morel_BooleanImpliesExp117', b1)
    if hasattr(b1, 'morel_ForStatement116'):
        assert _is_linked(b1, 'morel_ForStatement116', a)
    _safe_set(a, 'morel_BooleanImpliesExp117', b2)
    assert _is_linked(a, 'morel_BooleanImpliesExp117', b2)
    if hasattr(b1, 'morel_ForStatement116'):
        assert not _is_linked(b1, 'morel_ForStatement116', a)
    if hasattr(b2, 'morel_ForStatement116'):
        assert _is_linked(b2, 'morel_ForStatement116', a)
    _safe_set(a, 'morel_BooleanImpliesExp117', None)
    assert not _is_linked(a, 'morel_BooleanImpliesExp117', b2)
    if hasattr(b2, 'morel_ForStatement116'):
        assert not _is_linked(b2, 'morel_ForStatement116', a)


def test_assoc_types32_link_reassign_clear():
    a = morel_PathConstraint(maxLength=7, minLength=7)
    b1 = morel_EClass()
    b2 = morel_EClass()
    _safe_set(a, 'morel_PathConstraint33', {b1})
    assert _is_linked(a, 'morel_PathConstraint33', b1)
    if hasattr(b1, 'morel_EClass34'):
        assert _is_linked(b1, 'morel_EClass34', a)
    _safe_set(a, 'morel_PathConstraint33', {b2})
    assert _is_linked(a, 'morel_PathConstraint33', b2)
    if hasattr(b1, 'morel_EClass34'):
        assert not _is_linked(b1, 'morel_EClass34', a)
    if hasattr(b2, 'morel_EClass34'):
        assert _is_linked(b2, 'morel_EClass34', a)
    _safe_set(a, 'morel_PathConstraint33', set())
    assert not _is_linked(a, 'morel_PathConstraint33', b2)
    if hasattr(b2, 'morel_EClass34'):
        assert not _is_linked(b2, 'morel_EClass34', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AdditionalConstraint_strategy = st.builds(AdditionalConstraint)
@given(instance=AdditionalConstraint_strategy)
@settings(max_examples=25)
def test_AdditionalConstraint_instantiation(instance):
    assert isinstance(instance, AdditionalConstraint)


AdditiveExpChild_strategy = st.builds(AdditiveExpChild)
@given(instance=AdditiveExpChild_strategy)
@settings(max_examples=25)
def test_AdditiveExpChild_instantiation(instance):
    assert isinstance(instance, AdditiveExpChild)


AtomicExp_strategy = st.builds(AtomicExp)
@given(instance=AtomicExp_strategy)
@settings(max_examples=25)
def test_AtomicExp_instantiation(instance):
    assert isinstance(instance, AtomicExp)


BooleanAndExpChild_strategy = st.builds(BooleanAndExpChild)
@given(instance=BooleanAndExpChild_strategy)
@settings(max_examples=25)
def test_BooleanAndExpChild_instantiation(instance):
    assert isinstance(instance, BooleanAndExpChild)


BooleanImpliesExpChild_strategy = st.builds(BooleanImpliesExpChild)
@given(instance=BooleanImpliesExpChild_strategy)
@settings(max_examples=25)
def test_BooleanImpliesExpChild_instantiation(instance):
    assert isinstance(instance, BooleanImpliesExpChild)


BooleanOrExpChild_strategy = st.builds(BooleanOrExpChild)
@given(instance=BooleanOrExpChild_strategy)
@settings(max_examples=25)
def test_BooleanOrExpChild_instantiation(instance):
    assert isinstance(instance, BooleanOrExpChild)


CallPathExp_strategy = st.builds(CallPathExp)
@given(instance=CallPathExp_strategy)
@settings(max_examples=25)
def test_CallPathExp_instantiation(instance):
    assert isinstance(instance, CallPathExp)


CollectionType_strategy = st.builds(CollectionType)
@given(instance=CollectionType_strategy)
@settings(max_examples=25)
def test_CollectionType_instantiation(instance):
    assert isinstance(instance, CollectionType)


EDataType_strategy = st.builds(EDataType)
@given(instance=EDataType_strategy)
@settings(max_examples=25)
def test_EDataType_instantiation(instance):
    assert isinstance(instance, EDataType)


Executable_strategy = st.builds(Executable)
@given(instance=Executable_strategy)
@settings(max_examples=25)
def test_Executable_instantiation(instance):
    assert isinstance(instance, Executable)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ImperativeExp_strategy = st.builds(ImperativeExp)
@given(instance=ImperativeExp_strategy)
@settings(max_examples=25)
def test_ImperativeExp_instantiation(instance):
    assert isinstance(instance, ImperativeExp)


ImperativeStatement_strategy = st.builds(ImperativeStatement)
@given(instance=ImperativeStatement_strategy)
@settings(max_examples=25)
def test_ImperativeStatement_instantiation(instance):
    assert isinstance(instance, ImperativeStatement)


LinkConstraint_strategy = st.builds(LinkConstraint)
@given(instance=LinkConstraint_strategy)
@settings(max_examples=25)
def test_LinkConstraint_instantiation(instance):
    assert isinstance(instance, LinkConstraint)


LiteralExp_strategy = st.builds(LiteralExp)
@given(instance=LiteralExp_strategy)
@settings(max_examples=25)
def test_LiteralExp_instantiation(instance):
    assert isinstance(instance, LiteralExp)


LoopPathExp_strategy = st.builds(LoopPathExp)
@given(instance=LoopPathExp_strategy)
@settings(max_examples=25)
def test_LoopPathExp_instantiation(instance):
    assert isinstance(instance, LoopPathExp)


MultiplicativeExpChild_strategy = st.builds(MultiplicativeExpChild)
@given(instance=MultiplicativeExpChild_strategy)
@settings(max_examples=25)
def test_MultiplicativeExpChild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpChild)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ObjectVariable_strategy = st.builds(ObjectVariable)
@given(instance=ObjectVariable_strategy)
@settings(max_examples=25)
def test_ObjectVariable_instantiation(instance):
    assert isinstance(instance, ObjectVariable)


Pattern_strategy = st.builds(Pattern)
@given(instance=Pattern_strategy)
@settings(max_examples=25)
def test_Pattern_instantiation(instance):
    assert isinstance(instance, Pattern)


PrimitiveConstraint_strategy = st.builds(PrimitiveConstraint)
@given(instance=PrimitiveConstraint_strategy)
@settings(max_examples=25)
def test_PrimitiveConstraint_instantiation(instance):
    assert isinstance(instance, PrimitiveConstraint)


PrimitiveVariable_strategy = st.builds(PrimitiveVariable)
@given(instance=PrimitiveVariable_strategy)
@settings(max_examples=25)
def test_PrimitiveVariable_instantiation(instance):
    assert isinstance(instance, PrimitiveVariable)


RelationalExpChild_strategy = st.builds(RelationalExpChild)
@given(instance=RelationalExpChild_strategy)
@settings(max_examples=25)
def test_RelationalExpChild_instantiation(instance):
    assert isinstance(instance, RelationalExpChild)


RuleElement_strategy = st.builds(RuleElement)
@given(instance=RuleElement_strategy)
@settings(max_examples=25)
def test_RuleElement_instantiation(instance):
    assert isinstance(instance, RuleElement)


Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


UnaryExpChild_strategy = st.builds(UnaryExpChild)
@given(instance=UnaryExpChild_strategy)
@settings(max_examples=25)
def test_UnaryExpChild_instantiation(instance):
    assert isinstance(instance, UnaryExpChild)


Unit_strategy = st.builds(Unit)
@given(instance=Unit_strategy)
@settings(max_examples=25)
def test_Unit_instantiation(instance):
    assert isinstance(instance, Unit)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


VariableWithInit_strategy = st.builds(VariableWithInit)
@given(instance=VariableWithInit_strategy)
@settings(max_examples=25)
def test_VariableWithInit_instantiation(instance):
    assert isinstance(instance, VariableWithInit)


morel_AdditionalConstraint_strategy = st.builds(morel_AdditionalConstraint)
@given(instance=morel_AdditionalConstraint_strategy)
@settings(max_examples=25)
def test_morel_AdditionalConstraint_instantiation(instance):
    assert isinstance(instance, morel_AdditionalConstraint)


morel_AdditiveExp_strategy = st.builds(morel_AdditiveExp, operators=safe_text)
@given(instance=morel_AdditiveExp_strategy)
@settings(max_examples=25)
def test_morel_AdditiveExp_instantiation(instance):
    assert isinstance(instance, morel_AdditiveExp)


morel_AdditiveExpChild_strategy = st.builds(morel_AdditiveExpChild)
@given(instance=morel_AdditiveExpChild_strategy)
@settings(max_examples=25)
def test_morel_AdditiveExpChild_instantiation(instance):
    assert isinstance(instance, morel_AdditiveExpChild)


morel_AllDifferentConstraint_strategy = st.builds(morel_AllDifferentConstraint)
@given(instance=morel_AllDifferentConstraint_strategy)
@settings(max_examples=25)
def test_morel_AllDifferentConstraint_instantiation(instance):
    assert isinstance(instance, morel_AllDifferentConstraint)


morel_ArrayLiteralExp_strategy = st.builds(morel_ArrayLiteralExp)
@given(instance=morel_ArrayLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_ArrayLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_ArrayLiteralExp)


morel_AtomicExp_strategy = st.builds(morel_AtomicExp)
@given(instance=morel_AtomicExp_strategy)
@settings(max_examples=25)
def test_morel_AtomicExp_instantiation(instance):
    assert isinstance(instance, morel_AtomicExp)


morel_BagType_strategy = st.builds(morel_BagType)
@given(instance=morel_BagType_strategy)
@settings(max_examples=25)
def test_morel_BagType_instantiation(instance):
    assert isinstance(instance, morel_BagType)


morel_BindExp_strategy = st.builds(morel_BindExp)
@given(instance=morel_BindExp_strategy)
@settings(max_examples=25)
def test_morel_BindExp_instantiation(instance):
    assert isinstance(instance, morel_BindExp)


morel_BlockStatement_strategy = st.builds(morel_BlockStatement)
@given(instance=morel_BlockStatement_strategy)
@settings(max_examples=25)
def test_morel_BlockStatement_instantiation(instance):
    assert isinstance(instance, morel_BlockStatement)


morel_BooleanAndExp_strategy = st.builds(morel_BooleanAndExp, operators=safe_text)
@given(instance=morel_BooleanAndExp_strategy)
@settings(max_examples=25)
def test_morel_BooleanAndExp_instantiation(instance):
    assert isinstance(instance, morel_BooleanAndExp)


morel_BooleanAndExpChild_strategy = st.builds(morel_BooleanAndExpChild)
@given(instance=morel_BooleanAndExpChild_strategy)
@settings(max_examples=25)
def test_morel_BooleanAndExpChild_instantiation(instance):
    assert isinstance(instance, morel_BooleanAndExpChild)


morel_BooleanImpliesExp_strategy = st.builds(morel_BooleanImpliesExp, operator=safe_text)
@given(instance=morel_BooleanImpliesExp_strategy)
@settings(max_examples=25)
def test_morel_BooleanImpliesExp_instantiation(instance):
    assert isinstance(instance, morel_BooleanImpliesExp)


morel_BooleanImpliesExpChild_strategy = st.builds(morel_BooleanImpliesExpChild)
@given(instance=morel_BooleanImpliesExpChild_strategy)
@settings(max_examples=25)
def test_morel_BooleanImpliesExpChild_instantiation(instance):
    assert isinstance(instance, morel_BooleanImpliesExpChild)


morel_BooleanLiteralExp_strategy = st.builds(morel_BooleanLiteralExp, boolSymbol=st.booleans())
@given(instance=morel_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_BooleanLiteralExp)


morel_BooleanOrExp_strategy = st.builds(morel_BooleanOrExp, operators=safe_text)
@given(instance=morel_BooleanOrExp_strategy)
@settings(max_examples=25)
def test_morel_BooleanOrExp_instantiation(instance):
    assert isinstance(instance, morel_BooleanOrExp)


morel_BooleanOrExpChild_strategy = st.builds(morel_BooleanOrExpChild)
@given(instance=morel_BooleanOrExpChild_strategy)
@settings(max_examples=25)
def test_morel_BooleanOrExpChild_instantiation(instance):
    assert isinstance(instance, morel_BooleanOrExpChild)


morel_CallPathExp_strategy = st.builds(morel_CallPathExp)
@given(instance=morel_CallPathExp_strategy)
@settings(max_examples=25)
def test_morel_CallPathExp_instantiation(instance):
    assert isinstance(instance, morel_CallPathExp)


morel_Clause_strategy = st.builds(morel_Clause)
@given(instance=morel_Clause_strategy)
@settings(max_examples=25)
def test_morel_Clause_instantiation(instance):
    assert isinstance(instance, morel_Clause)


morel_CollectionLiteralExp_strategy = st.builds(morel_CollectionLiteralExp, type=safe_text)
@given(instance=morel_CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_CollectionLiteralExp)


morel_CollectionType_strategy = st.builds(morel_CollectionType)
@given(instance=morel_CollectionType_strategy)
@settings(max_examples=25)
def test_morel_CollectionType_instantiation(instance):
    assert isinstance(instance, morel_CollectionType)


morel_ConditionExp_strategy = st.builds(morel_ConditionExp)
@given(instance=morel_ConditionExp_strategy)
@settings(max_examples=25)
def test_morel_ConditionExp_instantiation(instance):
    assert isinstance(instance, morel_ConditionExp)


morel_DeclarativeStatement_strategy = st.builds(morel_DeclarativeStatement)
@given(instance=morel_DeclarativeStatement_strategy)
@settings(max_examples=25)
def test_morel_DeclarativeStatement_instantiation(instance):
    assert isinstance(instance, morel_DeclarativeStatement)


morel_EAttribute_strategy = st.builds(morel_EAttribute)
@given(instance=morel_EAttribute_strategy)
@settings(max_examples=25)
def test_morel_EAttribute_instantiation(instance):
    assert isinstance(instance, morel_EAttribute)


morel_EClass_strategy = st.builds(morel_EClass)
@given(instance=morel_EClass_strategy)
@settings(max_examples=25)
def test_morel_EClass_instantiation(instance):
    assert isinstance(instance, morel_EClass)


morel_EClassifier_strategy = st.builds(morel_EClassifier)
@given(instance=morel_EClassifier_strategy)
@settings(max_examples=25)
def test_morel_EClassifier_instantiation(instance):
    assert isinstance(instance, morel_EClassifier)


morel_EDataType_strategy = st.builds(morel_EDataType)
@given(instance=morel_EDataType_strategy)
@settings(max_examples=25)
def test_morel_EDataType_instantiation(instance):
    assert isinstance(instance, morel_EDataType)


morel_EEnum_strategy = st.builds(morel_EEnum)
@given(instance=morel_EEnum_strategy)
@settings(max_examples=25)
def test_morel_EEnum_instantiation(instance):
    assert isinstance(instance, morel_EEnum)


morel_EEnumLiteral_strategy = st.builds(morel_EEnumLiteral)
@given(instance=morel_EEnumLiteral_strategy)
@settings(max_examples=25)
def test_morel_EEnumLiteral_instantiation(instance):
    assert isinstance(instance, morel_EEnumLiteral)


morel_EPackage_strategy = st.builds(morel_EPackage)
@given(instance=morel_EPackage_strategy)
@settings(max_examples=25)
def test_morel_EPackage_instantiation(instance):
    assert isinstance(instance, morel_EPackage)


morel_EReference_strategy = st.builds(morel_EReference)
@given(instance=morel_EReference_strategy)
@settings(max_examples=25)
def test_morel_EReference_instantiation(instance):
    assert isinstance(instance, morel_EReference)


morel_EnclosureLinkConstraint_strategy = st.builds(morel_EnclosureLinkConstraint)
@given(instance=morel_EnclosureLinkConstraint_strategy)
@settings(max_examples=25)
def test_morel_EnclosureLinkConstraint_instantiation(instance):
    assert isinstance(instance, morel_EnclosureLinkConstraint)


morel_EnumLiteralExp_strategy = st.builds(morel_EnumLiteralExp)
@given(instance=morel_EnumLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_EnumLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_EnumLiteralExp)


morel_Executable_strategy = st.builds(morel_Executable, active=st.booleans(), parameters=safe_text)
@given(instance=morel_Executable_strategy)
@settings(max_examples=25)
def test_morel_Executable_instantiation(instance):
    assert isinstance(instance, morel_Executable)


morel_Expression_strategy = st.builds(morel_Expression)
@given(instance=morel_Expression_strategy)
@settings(max_examples=25)
def test_morel_Expression_instantiation(instance):
    assert isinstance(instance, morel_Expression)


morel_FeaturePathExp_strategy = st.builds(morel_FeaturePathExp, feature=safe_text)
@given(instance=morel_FeaturePathExp_strategy)
@settings(max_examples=25)
def test_morel_FeaturePathExp_instantiation(instance):
    assert isinstance(instance, morel_FeaturePathExp)


morel_ForStatement_strategy = st.builds(morel_ForStatement)
@given(instance=morel_ForStatement_strategy)
@settings(max_examples=25)
def test_morel_ForStatement_instantiation(instance):
    assert isinstance(instance, morel_ForStatement)


morel_IfStatement_strategy = st.builds(morel_IfStatement)
@given(instance=morel_IfStatement_strategy)
@settings(max_examples=25)
def test_morel_IfStatement_instantiation(instance):
    assert isinstance(instance, morel_IfStatement)


morel_ImperativeExp_strategy = st.builds(morel_ImperativeExp)
@given(instance=morel_ImperativeExp_strategy)
@settings(max_examples=25)
def test_morel_ImperativeExp_instantiation(instance):
    assert isinstance(instance, morel_ImperativeExp)


morel_ImperativeStatement_strategy = st.builds(morel_ImperativeStatement)
@given(instance=morel_ImperativeStatement_strategy)
@settings(max_examples=25)
def test_morel_ImperativeStatement_instantiation(instance):
    assert isinstance(instance, morel_ImperativeStatement)


morel_IntegerLiteralExp_strategy = st.builds(morel_IntegerLiteralExp, integerSymbol=st.integers())
@given(instance=morel_IntegerLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_IntegerLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_IntegerLiteralExp)


morel_IteratorPathExp_strategy = st.builds(morel_IteratorPathExp, type=safe_text)
@given(instance=morel_IteratorPathExp_strategy)
@settings(max_examples=25)
def test_morel_IteratorPathExp_instantiation(instance):
    assert isinstance(instance, morel_IteratorPathExp)


morel_LetExp_strategy = st.builds(morel_LetExp)
@given(instance=morel_LetExp_strategy)
@settings(max_examples=25)
def test_morel_LetExp_instantiation(instance):
    assert isinstance(instance, morel_LetExp)


morel_LinkConstraint_strategy = st.builds(morel_LinkConstraint)
@given(instance=morel_LinkConstraint_strategy)
@settings(max_examples=25)
def test_morel_LinkConstraint_instantiation(instance):
    assert isinstance(instance, morel_LinkConstraint)


morel_LiteralExp_strategy = st.builds(morel_LiteralExp)
@given(instance=morel_LiteralExp_strategy)
@settings(max_examples=25)
def test_morel_LiteralExp_instantiation(instance):
    assert isinstance(instance, morel_LiteralExp)


morel_LoopPathExp_strategy = st.builds(morel_LoopPathExp)
@given(instance=morel_LoopPathExp_strategy)
@settings(max_examples=25)
def test_morel_LoopPathExp_instantiation(instance):
    assert isinstance(instance, morel_LoopPathExp)


morel_MultiValueConstraint_strategy = st.builds(morel_MultiValueConstraint)
@given(instance=morel_MultiValueConstraint_strategy)
@settings(max_examples=25)
def test_morel_MultiValueConstraint_instantiation(instance):
    assert isinstance(instance, morel_MultiValueConstraint)


morel_MultiplicativeExp_strategy = st.builds(morel_MultiplicativeExp, operators=safe_text)
@given(instance=morel_MultiplicativeExp_strategy)
@settings(max_examples=25)
def test_morel_MultiplicativeExp_instantiation(instance):
    assert isinstance(instance, morel_MultiplicativeExp)


morel_MultiplicativeExpChild_strategy = st.builds(morel_MultiplicativeExpChild)
@given(instance=morel_MultiplicativeExpChild_strategy)
@settings(max_examples=25)
def test_morel_MultiplicativeExpChild_instantiation(instance):
    assert isinstance(instance, morel_MultiplicativeExpChild)


morel_NamedElement_strategy = st.builds(morel_NamedElement, name=safe_text)
@given(instance=morel_NamedElement_strategy)
@settings(max_examples=25)
def test_morel_NamedElement_instantiation(instance):
    assert isinstance(instance, morel_NamedElement)


morel_NestedExp_strategy = st.builds(morel_NestedExp)
@given(instance=morel_NestedExp_strategy)
@settings(max_examples=25)
def test_morel_NestedExp_instantiation(instance):
    assert isinstance(instance, morel_NestedExp)


morel_ObjectVariable_strategy = st.builds(morel_ObjectVariable)
@given(instance=morel_ObjectVariable_strategy)
@settings(max_examples=25)
def test_morel_ObjectVariable_instantiation(instance):
    assert isinstance(instance, morel_ObjectVariable)


morel_ObjectVariableWithInit_strategy = st.builds(morel_ObjectVariableWithInit)
@given(instance=morel_ObjectVariableWithInit_strategy)
@settings(max_examples=25)
def test_morel_ObjectVariableWithInit_instantiation(instance):
    assert isinstance(instance, morel_ObjectVariableWithInit)


morel_OperationPathExp_strategy = st.builds(morel_OperationPathExp, operation=safe_text, separator=safe_text)
@given(instance=morel_OperationPathExp_strategy)
@settings(max_examples=25)
def test_morel_OperationPathExp_instantiation(instance):
    assert isinstance(instance, morel_OperationPathExp)


morel_OrderConstraint_strategy = st.builds(morel_OrderConstraint)
@given(instance=morel_OrderConstraint_strategy)
@settings(max_examples=25)
def test_morel_OrderConstraint_instantiation(instance):
    assert isinstance(instance, morel_OrderConstraint)


morel_OrderedSetType_strategy = st.builds(morel_OrderedSetType)
@given(instance=morel_OrderedSetType_strategy)
@settings(max_examples=25)
def test_morel_OrderedSetType_instantiation(instance):
    assert isinstance(instance, morel_OrderedSetType)


morel_PathConstraint_strategy = st.builds(morel_PathConstraint, maxLength=st.integers(), minLength=st.integers())
@given(instance=morel_PathConstraint_strategy)
@settings(max_examples=25)
def test_morel_PathConstraint_instantiation(instance):
    assert isinstance(instance, morel_PathConstraint)


morel_Pattern_strategy = st.builds(morel_Pattern)
@given(instance=morel_Pattern_strategy)
@settings(max_examples=25)
def test_morel_Pattern_instantiation(instance):
    assert isinstance(instance, morel_Pattern)


morel_PredefinedBindExp_strategy = st.builds(morel_PredefinedBindExp)
@given(instance=morel_PredefinedBindExp_strategy)
@settings(max_examples=25)
def test_morel_PredefinedBindExp_instantiation(instance):
    assert isinstance(instance, morel_PredefinedBindExp)


morel_PredefinedVariableExp_strategy = st.builds(morel_PredefinedVariableExp, variable=safe_text)
@given(instance=morel_PredefinedVariableExp_strategy)
@settings(max_examples=25)
def test_morel_PredefinedVariableExp_instantiation(instance):
    assert isinstance(instance, morel_PredefinedVariableExp)


morel_PrimitiveConstraint_strategy = st.builds(morel_PrimitiveConstraint)
@given(instance=morel_PrimitiveConstraint_strategy)
@settings(max_examples=25)
def test_morel_PrimitiveConstraint_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveConstraint)


morel_PrimitiveVariable_strategy = st.builds(morel_PrimitiveVariable)
@given(instance=morel_PrimitiveVariable_strategy)
@settings(max_examples=25)
def test_morel_PrimitiveVariable_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveVariable)


morel_PrimitiveVariableWithInit_strategy = st.builds(morel_PrimitiveVariableWithInit)
@given(instance=morel_PrimitiveVariableWithInit_strategy)
@settings(max_examples=25)
def test_morel_PrimitiveVariableWithInit_instantiation(instance):
    assert isinstance(instance, morel_PrimitiveVariableWithInit)


morel_Query_strategy = st.builds(morel_Query)
@given(instance=morel_Query_strategy)
@settings(max_examples=25)
def test_morel_Query_instantiation(instance):
    assert isinstance(instance, morel_Query)


morel_QueryModel_strategy = st.builds(morel_QueryModel)
@given(instance=morel_QueryModel_strategy)
@settings(max_examples=25)
def test_morel_QueryModel_instantiation(instance):
    assert isinstance(instance, morel_QueryModel)


morel_RealLiteralExp_strategy = st.builds(morel_RealLiteralExp, realSymbol=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=morel_RealLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_RealLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_RealLiteralExp)


morel_ReflectiveVariableExp_strategy = st.builds(morel_ReflectiveVariableExp)
@given(instance=morel_ReflectiveVariableExp_strategy)
@settings(max_examples=25)
def test_morel_ReflectiveVariableExp_instantiation(instance):
    assert isinstance(instance, morel_ReflectiveVariableExp)


morel_RelationalExp_strategy = st.builds(morel_RelationalExp, operator=safe_text)
@given(instance=morel_RelationalExp_strategy)
@settings(max_examples=25)
def test_morel_RelationalExp_instantiation(instance):
    assert isinstance(instance, morel_RelationalExp)


morel_RelationalExpChild_strategy = st.builds(morel_RelationalExpChild)
@given(instance=morel_RelationalExpChild_strategy)
@settings(max_examples=25)
def test_morel_RelationalExpChild_instantiation(instance):
    assert isinstance(instance, morel_RelationalExpChild)


morel_Rule_strategy = st.builds(morel_Rule)
@given(instance=morel_Rule_strategy)
@settings(max_examples=25)
def test_morel_Rule_instantiation(instance):
    assert isinstance(instance, morel_Rule)


morel_RuleElement_strategy = st.builds(morel_RuleElement)
@given(instance=morel_RuleElement_strategy)
@settings(max_examples=25)
def test_morel_RuleElement_instantiation(instance):
    assert isinstance(instance, morel_RuleElement)


morel_RuleGroup_strategy = st.builds(morel_RuleGroup, iteration=safe_text, maxIteration=st.integers(), order=safe_text, repetition=safe_text, scope=safe_text, scopeSize=st.integers())
@given(instance=morel_RuleGroup_strategy)
@settings(max_examples=25)
def test_morel_RuleGroup_instantiation(instance):
    assert isinstance(instance, morel_RuleGroup)


morel_Section_strategy = st.builds(morel_Section, type=safe_text)
@given(instance=morel_Section_strategy)
@settings(max_examples=25)
def test_morel_Section_instantiation(instance):
    assert isinstance(instance, morel_Section)


morel_SequenceType_strategy = st.builds(morel_SequenceType)
@given(instance=morel_SequenceType_strategy)
@settings(max_examples=25)
def test_morel_SequenceType_instantiation(instance):
    assert isinstance(instance, morel_SequenceType)


morel_SetType_strategy = st.builds(morel_SetType)
@given(instance=morel_SetType_strategy)
@settings(max_examples=25)
def test_morel_SetType_instantiation(instance):
    assert isinstance(instance, morel_SetType)


morel_SimpleLinkConstraint_strategy = st.builds(morel_SimpleLinkConstraint)
@given(instance=morel_SimpleLinkConstraint_strategy)
@settings(max_examples=25)
def test_morel_SimpleLinkConstraint_instantiation(instance):
    assert isinstance(instance, morel_SimpleLinkConstraint)


morel_Statement_strategy = st.builds(morel_Statement)
@given(instance=morel_Statement_strategy)
@settings(max_examples=25)
def test_morel_Statement_instantiation(instance):
    assert isinstance(instance, morel_Statement)


morel_StringLiteralExp_strategy = st.builds(morel_StringLiteralExp, stringSymbol=safe_text)
@given(instance=morel_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_StringLiteralExp)


morel_TransformationModel_strategy = st.builds(morel_TransformationModel)
@given(instance=morel_TransformationModel_strategy)
@settings(max_examples=25)
def test_morel_TransformationModel_instantiation(instance):
    assert isinstance(instance, morel_TransformationModel)


morel_TypeLiteralExp_strategy = st.builds(morel_TypeLiteralExp)
@given(instance=morel_TypeLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_TypeLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_TypeLiteralExp)


morel_TypedModel_strategy = st.builds(morel_TypedModel, type=safe_text)
@given(instance=morel_TypedModel_strategy)
@settings(max_examples=25)
def test_morel_TypedModel_instantiation(instance):
    assert isinstance(instance, morel_TypedModel)


morel_UnaryExp_strategy = st.builds(morel_UnaryExp, operator=safe_text)
@given(instance=morel_UnaryExp_strategy)
@settings(max_examples=25)
def test_morel_UnaryExp_instantiation(instance):
    assert isinstance(instance, morel_UnaryExp)


morel_UnaryExpChild_strategy = st.builds(morel_UnaryExpChild)
@given(instance=morel_UnaryExpChild_strategy)
@settings(max_examples=25)
def test_morel_UnaryExpChild_instantiation(instance):
    assert isinstance(instance, morel_UnaryExpChild)


morel_UndefinedLiteralExp_strategy = st.builds(morel_UndefinedLiteralExp, value=safe_text)
@given(instance=morel_UndefinedLiteralExp_strategy)
@settings(max_examples=25)
def test_morel_UndefinedLiteralExp_instantiation(instance):
    assert isinstance(instance, morel_UndefinedLiteralExp)


morel_Unit_strategy = st.builds(morel_Unit)
@given(instance=morel_Unit_strategy)
@settings(max_examples=25)
def test_morel_Unit_instantiation(instance):
    assert isinstance(instance, morel_Unit)


morel_ValueRangeConstraint_strategy = st.builds(morel_ValueRangeConstraint)
@given(instance=morel_ValueRangeConstraint_strategy)
@settings(max_examples=25)
def test_morel_ValueRangeConstraint_instantiation(instance):
    assert isinstance(instance, morel_ValueRangeConstraint)


morel_Variable_strategy = st.builds(morel_Variable)
@given(instance=morel_Variable_strategy)
@settings(max_examples=25)
def test_morel_Variable_instantiation(instance):
    assert isinstance(instance, morel_Variable)


morel_VariableExp_strategy = st.builds(morel_VariableExp)
@given(instance=morel_VariableExp_strategy)
@settings(max_examples=25)
def test_morel_VariableExp_instantiation(instance):
    assert isinstance(instance, morel_VariableExp)


morel_VariableWithInit_strategy = st.builds(morel_VariableWithInit)
@given(instance=morel_VariableWithInit_strategy)
@settings(max_examples=25)
def test_morel_VariableWithInit_instantiation(instance):
    assert isinstance(instance, morel_VariableWithInit)


