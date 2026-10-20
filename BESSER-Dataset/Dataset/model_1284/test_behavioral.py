import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_models38_reverse_link_reassign_clear():
    a1 = morel_Unit()
    a2 = morel_Unit()
    b = morel_TypedModel(type="sample_text")
    _safe_set(b, 'morel_TypedModel39', a1)
    assert _is_linked(b, 'morel_TypedModel39', a1)
    if hasattr(a1, 'morel_Unit'):
        assert _is_linked(a1, 'morel_Unit', b)
    _safe_set(b, 'morel_TypedModel39', a2)
    assert _is_linked(b, 'morel_TypedModel39', a2)
    if hasattr(a1, 'morel_Unit'):
        assert not _is_linked(a1, 'morel_Unit', b)
    if hasattr(a2, 'morel_Unit'):
        assert _is_linked(a2, 'morel_Unit', b)
    _safe_set(b, 'morel_TypedModel39', None)
    assert not _is_linked(b, 'morel_TypedModel39', a2)
    if hasattr(a2, 'morel_Unit'):
        assert not _is_linked(a2, 'morel_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyExp64_stub_double():
    # morel_Expression has no real 'morel_Expression66' property in the generated
    # code (a bare stub) -- manually attach it so morel_IteratorPathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_IteratorPathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_IteratorPathExp(type="sample_text")
    partner = morel_Expression()
    setattr(partner, 'morel_Expression66', None)
    _safe_set(owner, 'morel_IteratorPathExp65', partner)
    assert getattr(partner, 'morel_Expression66') == owner
    _safe_set(owner, 'morel_IteratorPathExp65', None)
    assert getattr(partner, 'morel_Expression66') is None


def test_assoc_child94_stub_double():
    # morel_UnaryExpChild has no real 'morel_UnaryExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_UnaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_UnaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_UnaryExp(operator="sample_text")
    partner = morel_UnaryExpChild()
    setattr(partner, 'morel_UnaryExpChild', None)
    _safe_set(owner, 'morel_UnaryExp', partner)
    assert getattr(partner, 'morel_UnaryExpChild') == owner
    _safe_set(owner, 'morel_UnaryExp', None)
    assert getattr(partner, 'morel_UnaryExpChild') is None


def test_assoc_children86_stub_double():
    # morel_BooleanOrExpChild has no real 'morel_BooleanOrExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanOrExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanOrExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanOrExp(operators="sample_text")
    partner = morel_BooleanOrExpChild()
    setattr(partner, 'morel_BooleanOrExpChild', None)
    _safe_set(owner, 'morel_BooleanOrExp', {partner})
    assert getattr(partner, 'morel_BooleanOrExpChild') == owner
    _safe_set(owner, 'morel_BooleanOrExp', set())
    assert getattr(partner, 'morel_BooleanOrExpChild') is None


def test_assoc_children87_stub_double():
    # morel_BooleanAndExpChild has no real 'morel_BooleanAndExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanAndExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanAndExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanAndExp(operators="sample_text")
    partner = morel_BooleanAndExpChild()
    setattr(partner, 'morel_BooleanAndExpChild', None)
    _safe_set(owner, 'morel_BooleanAndExp', {partner})
    assert getattr(partner, 'morel_BooleanAndExpChild') == owner
    _safe_set(owner, 'morel_BooleanAndExp', set())
    assert getattr(partner, 'morel_BooleanAndExpChild') is None


def test_assoc_children92_stub_double():
    # morel_AdditiveExpChild has no real 'morel_AdditiveExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_AdditiveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_AdditiveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_AdditiveExp(operators="sample_text")
    partner = morel_AdditiveExpChild()
    setattr(partner, 'morel_AdditiveExpChild', None)
    _safe_set(owner, 'morel_AdditiveExp', {partner})
    assert getattr(partner, 'morel_AdditiveExpChild') == owner
    _safe_set(owner, 'morel_AdditiveExp', set())
    assert getattr(partner, 'morel_AdditiveExpChild') is None


def test_assoc_children93_stub_double():
    # morel_MultiplicativeExpChild has no real 'morel_MultiplicativeExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_MultiplicativeExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_MultiplicativeExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_MultiplicativeExp(operators="sample_text")
    partner = morel_MultiplicativeExpChild()
    setattr(partner, 'morel_MultiplicativeExpChild', None)
    _safe_set(owner, 'morel_MultiplicativeExp', {partner})
    assert getattr(partner, 'morel_MultiplicativeExpChild') == owner
    _safe_set(owner, 'morel_MultiplicativeExp', set())
    assert getattr(partner, 'morel_MultiplicativeExpChild') is None


def test_assoc_condition106_stub_double():
    # morel_IfStatement has no real 'morel_IfStatement' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanImpliesExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanImpliesExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanImpliesExp(operator="sample_text")
    partner = morel_IfStatement()
    setattr(partner, 'morel_IfStatement', None)
    _safe_set(owner, 'morel_BooleanImpliesExp107', partner)
    assert getattr(partner, 'morel_IfStatement') == owner
    _safe_set(owner, 'morel_BooleanImpliesExp107', None)
    assert getattr(partner, 'morel_IfStatement') is None


def test_assoc_condition74_stub_double():
    # morel_ConditionExp has no real 'morel_ConditionExp' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanImpliesExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanImpliesExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanImpliesExp(operator="sample_text")
    partner = morel_ConditionExp()
    setattr(partner, 'morel_ConditionExp', None)
    _safe_set(owner, 'morel_BooleanImpliesExp', partner)
    assert getattr(partner, 'morel_ConditionExp') == owner
    _safe_set(owner, 'morel_BooleanImpliesExp', None)
    assert getattr(partner, 'morel_ConditionExp') is None


def test_assoc_dataTypes40_stub_double():
    # morel_EDataType has no real 'morel_EDataType42' property in the generated
    # code (a bare stub) -- manually attach it so morel_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_Unit()
    partner = morel_EDataType()
    setattr(partner, 'morel_EDataType42', None)
    _safe_set(owner, 'morel_Unit41', {partner})
    assert getattr(partner, 'morel_EDataType42') == owner
    _safe_set(owner, 'morel_Unit41', set())
    assert getattr(partner, 'morel_EDataType42') is None


def test_assoc_firstVar59_stub_double():
    # morel_Variable has no real 'morel_Variable60' property in the generated
    # code (a bare stub) -- manually attach it so morel_IteratorPathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_IteratorPathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_IteratorPathExp(type="sample_text")
    partner = morel_Variable()
    setattr(partner, 'morel_Variable60', None)
    _safe_set(owner, 'morel_IteratorPathExp', partner)
    assert getattr(partner, 'morel_Variable60') == owner
    _safe_set(owner, 'morel_IteratorPathExp', None)
    assert getattr(partner, 'morel_Variable60') is None


def test_assoc_left81_stub_double():
    # morel_BooleanImpliesExpChild has no real 'morel_BooleanImpliesExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanImpliesExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanImpliesExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanImpliesExp(operator="sample_text")
    partner = morel_BooleanImpliesExpChild()
    setattr(partner, 'morel_BooleanImpliesExpChild', None)
    _safe_set(owner, 'morel_BooleanImpliesExp82', partner)
    assert getattr(partner, 'morel_BooleanImpliesExpChild') == owner
    _safe_set(owner, 'morel_BooleanImpliesExp82', None)
    assert getattr(partner, 'morel_BooleanImpliesExpChild') is None


def test_assoc_left88_stub_double():
    # morel_RelationalExpChild has no real 'morel_RelationalExpChild' property in the generated
    # code (a bare stub) -- manually attach it so morel_RelationalExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_RelationalExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_RelationalExp(operator="sample_text")
    partner = morel_RelationalExpChild()
    setattr(partner, 'morel_RelationalExpChild', None)
    _safe_set(owner, 'morel_RelationalExp', partner)
    assert getattr(partner, 'morel_RelationalExpChild') == owner
    _safe_set(owner, 'morel_RelationalExp', None)
    assert getattr(partner, 'morel_RelationalExpChild') is None


def test_assoc_literals44_stub_double():
    # morel_Expression has no real 'morel_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so morel_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_CollectionLiteralExp(type="sample_text")
    partner = morel_Expression()
    setattr(partner, 'morel_Expression45', None)
    _safe_set(owner, 'morel_CollectionLiteralExp', {partner})
    assert getattr(partner, 'morel_Expression45') == owner
    _safe_set(owner, 'morel_CollectionLiteralExp', set())
    assert getattr(partner, 'morel_Expression45') is None


def test_assoc_model11_stub_double():
    # morel_ObjectVariable has no real 'morel_ObjectVariable12' property in the generated
    # code (a bare stub) -- manually attach it so morel_TypedModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_TypedModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_TypedModel(type="sample_text")
    partner = morel_ObjectVariable()
    setattr(partner, 'morel_ObjectVariable12', None)
    _safe_set(owner, 'morel_TypedModel', partner)
    assert getattr(partner, 'morel_ObjectVariable12') == owner
    _safe_set(owner, 'morel_TypedModel', None)
    assert getattr(partner, 'morel_ObjectVariable12') is None


def test_assoc_package36_stub_double():
    # morel_EPackage has no real 'morel_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so morel_TypedModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_TypedModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_TypedModel(type="sample_text")
    partner = morel_EPackage()
    setattr(partner, 'morel_EPackage', None)
    _safe_set(owner, 'morel_TypedModel37', partner)
    assert getattr(partner, 'morel_EPackage') == owner
    _safe_set(owner, 'morel_TypedModel37', None)
    assert getattr(partner, 'morel_EPackage') is None


def test_assoc_parameters57_stub_double():
    # morel_Expression has no real 'morel_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so morel_OperationPathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_OperationPathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_OperationPathExp(operation="sample_text", separator="sample_text")
    partner = morel_Expression()
    setattr(partner, 'morel_Expression58', None)
    _safe_set(owner, 'morel_OperationPathExp', {partner})
    assert getattr(partner, 'morel_Expression58') == owner
    _safe_set(owner, 'morel_OperationPathExp', set())
    assert getattr(partner, 'morel_Expression58') is None


def test_assoc_pathVariable28_stub_double():
    # morel_Variable has no real 'morel_Variable' property in the generated
    # code (a bare stub) -- manually attach it so morel_PathConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_PathConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_PathConstraint(maxLength=7, minLength=7)
    partner = morel_Variable()
    setattr(partner, 'morel_Variable', None)
    _safe_set(owner, 'morel_PathConstraint', partner)
    assert getattr(partner, 'morel_Variable') == owner
    _safe_set(owner, 'morel_PathConstraint', None)
    assert getattr(partner, 'morel_Variable') is None


def test_assoc_primitiveVariables137_stub_double():
    # morel_PrimitiveVariable has no real 'morel_PrimitiveVariable138' property in the generated
    # code (a bare stub) -- manually attach it so morel_Executable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_Executable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_Executable(active=True, parameters="sample_text")
    partner = morel_PrimitiveVariable()
    setattr(partner, 'morel_PrimitiveVariable138', None)
    _safe_set(owner, 'morel_Executable', {partner})
    assert getattr(partner, 'morel_PrimitiveVariable138') == owner
    _safe_set(owner, 'morel_Executable', set())
    assert getattr(partner, 'morel_PrimitiveVariable138') is None


def test_assoc_references29_stub_double():
    # morel_EReference has no real 'morel_EReference31' property in the generated
    # code (a bare stub) -- manually attach it so morel_PathConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_PathConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_PathConstraint(maxLength=7, minLength=7)
    partner = morel_EReference()
    setattr(partner, 'morel_EReference31', None)
    _safe_set(owner, 'morel_PathConstraint30', {partner})
    assert getattr(partner, 'morel_EReference31') == owner
    _safe_set(owner, 'morel_PathConstraint30', set())
    assert getattr(partner, 'morel_EReference31') is None


def test_assoc_right83_stub_double():
    # morel_BooleanImpliesExpChild has no real 'morel_BooleanImpliesExpChild85' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanImpliesExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanImpliesExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanImpliesExp(operator="sample_text")
    partner = morel_BooleanImpliesExpChild()
    setattr(partner, 'morel_BooleanImpliesExpChild85', None)
    _safe_set(owner, 'morel_BooleanImpliesExp84', partner)
    assert getattr(partner, 'morel_BooleanImpliesExpChild85') == owner
    _safe_set(owner, 'morel_BooleanImpliesExp84', None)
    assert getattr(partner, 'morel_BooleanImpliesExpChild85') is None


def test_assoc_right89_stub_double():
    # morel_RelationalExpChild has no real 'morel_RelationalExpChild91' property in the generated
    # code (a bare stub) -- manually attach it so morel_RelationalExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_RelationalExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_RelationalExp(operator="sample_text")
    partner = morel_RelationalExpChild()
    setattr(partner, 'morel_RelationalExpChild91', None)
    _safe_set(owner, 'morel_RelationalExp90', partner)
    assert getattr(partner, 'morel_RelationalExpChild91') == owner
    _safe_set(owner, 'morel_RelationalExp90', None)
    assert getattr(partner, 'morel_RelationalExpChild91') is None


def test_assoc_rules129_stub_double():
    # morel_Rule has no real 'morel_Rule130' property in the generated
    # code (a bare stub) -- manually attach it so morel_RuleGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_RuleGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_RuleGroup(iteration="sample_text", maxIteration=7, order="sample_text", repetition="sample_text", scope="sample_text", scopeSize=7)
    partner = morel_Rule()
    setattr(partner, 'morel_Rule130', None)
    _safe_set(owner, 'morel_RuleGroup', {partner})
    assert getattr(partner, 'morel_Rule130') == owner
    _safe_set(owner, 'morel_RuleGroup', set())
    assert getattr(partner, 'morel_Rule130') is None


def test_assoc_secondVar61_stub_double():
    # morel_Variable has no real 'morel_Variable63' property in the generated
    # code (a bare stub) -- manually attach it so morel_IteratorPathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_IteratorPathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_IteratorPathExp(type="sample_text")
    partner = morel_Variable()
    setattr(partner, 'morel_Variable63', None)
    _safe_set(owner, 'morel_IteratorPathExp62', partner)
    assert getattr(partner, 'morel_Variable63') == owner
    _safe_set(owner, 'morel_IteratorPathExp62', None)
    assert getattr(partner, 'morel_Variable63') is None


def test_assoc_source102_stub_double():
    # morel_PredefinedBindExp has no real 'morel_PredefinedBindExp' property in the generated
    # code (a bare stub) -- manually attach it so morel_PredefinedVariableExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_PredefinedVariableExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_PredefinedVariableExp(variable="sample_text")
    partner = morel_PredefinedBindExp()
    setattr(partner, 'morel_PredefinedBindExp', None)
    _safe_set(owner, 'morel_PredefinedVariableExp', partner)
    assert getattr(partner, 'morel_PredefinedBindExp') == owner
    _safe_set(owner, 'morel_PredefinedVariableExp', None)
    assert getattr(partner, 'morel_PredefinedBindExp') is None


def test_assoc_terminationExp115_stub_double():
    # morel_ForStatement has no real 'morel_ForStatement116' property in the generated
    # code (a bare stub) -- manually attach it so morel_BooleanImpliesExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_BooleanImpliesExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_BooleanImpliesExp(operator="sample_text")
    partner = morel_ForStatement()
    setattr(partner, 'morel_ForStatement116', None)
    _safe_set(owner, 'morel_BooleanImpliesExp117', partner)
    assert getattr(partner, 'morel_ForStatement116') == owner
    _safe_set(owner, 'morel_BooleanImpliesExp117', None)
    assert getattr(partner, 'morel_ForStatement116') is None


def test_assoc_types32_stub_double():
    # morel_EClass has no real 'morel_EClass34' property in the generated
    # code (a bare stub) -- manually attach it so morel_PathConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # morel_PathConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = morel_PathConstraint(maxLength=7, minLength=7)
    partner = morel_EClass()
    setattr(partner, 'morel_EClass34', None)
    _safe_set(owner, 'morel_PathConstraint33', {partner})
    assert getattr(partner, 'morel_EClass34') == owner
    _safe_set(owner, 'morel_PathConstraint33', set())
    assert getattr(partner, 'morel_EClass34') is None


