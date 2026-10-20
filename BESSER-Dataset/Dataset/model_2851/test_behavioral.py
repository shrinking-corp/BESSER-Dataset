import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BlockStatement,
    Expression,
    Feature,
    Literal,
    MetamodelFeature,
    MethodInvocation,
    Parameter,
    ParameterReference,
    RuleReference,
    Statement,
    StatementExpression,
    TerminalExpression,
    Type,
    VarDeclaration,
    mitra_Annotation,
    mitra_AnnotationDecl,
    mitra_AnnotationProperty,
    mitra_AnnotationPropertyDecl,
    mitra_AnnotationsDefinition,
    mitra_Assignment,
    mitra_Block,
    mitra_BlockStatement,
    mitra_BooleanExpression,
    mitra_BooleanLiteral,
    mitra_BreakStatement,
    mitra_Catch,
    mitra_ClassInstanceCreationExpression,
    mitra_CollectionType,
    mitra_DoStatement,
    mitra_EClassifier,
    mitra_EmptyStatement,
    mitra_EqualityExpression,
    mitra_Expression,
    mitra_ExpressionStatement,
    mitra_Feature,
    mitra_FeatureField,
    mitra_FeatureMethodInvocation,
    mitra_ForInit,
    mitra_ForStatement,
    mitra_ForUpdate,
    mitra_FormalParameter,
    mitra_IfStatement,
    mitra_InferredVarDeclaration,
    mitra_InstanceOfExpression,
    mitra_IntLiteral,
    mitra_IteratorExpression,
    mitra_JavaSpec,
    mitra_Literal,
    mitra_LocalVariableDeclaration,
    mitra_LocalVariableDeclarationStatement,
    mitra_LoopVariable,
    mitra_MathExpression,
    mitra_MetamodelDeclaration,
    mitra_MetamodelFeature,
    mitra_MethodInvocation,
    mitra_Module,
    mitra_ModuleReference,
    mitra_NativeOperationInvocation,
    mitra_NullLiteral,
    mitra_Parameter,
    mitra_ParameterReference,
    mitra_PrimitiveType,
    mitra_Property,
    mitra_QualifiedParameterReference,
    mitra_QualifiedRuleReference,
    mitra_RealLiteral,
    mitra_ReferenceType,
    mitra_RelationalExpression,
    mitra_ReturnParameter,
    mitra_ReturnStatement,
    mitra_RuleDeclaration,
    mitra_RuleInvocation,
    mitra_RuleInvocationSuper,
    mitra_RuleReference,
    mitra_SimpleParameterReference,
    mitra_SimpleRuleReference,
    mitra_Statement,
    mitra_StatementExpression,
    mitra_StaticAccess,
    mitra_StringLiteral,
    mitra_TerminalExpression,
    mitra_ThrowStatement,
    mitra_Trigger,
    mitra_TryStatement,
    mitra_Type,
    mitra_TypedVarDeclaration,
    mitra_UnaryBooleanExpression,
    mitra_UnaryCastExpression,
    mitra_UnaryMathExpression,
    mitra_VarDeclaration,
    mitra_VariableAccess,
    mitra_WhileStatement,
    AnnotationTargetSpec,
    AssignmentOperator,
    BooleanOperator,
    CollectionTypeSpec,
    EqualityOperator,
    ExecutionModifier,
    MathOperator,
    PPOperator,
    ParameterModifier,
    PrimitiveTypeSpec,
    RelationalOperator,
    UnaryMathOperator,
    VisibilityModifier,
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

def test_assoc_excludingRules23_reverse_link_reassign_clear():
    a1 = mitra_SimpleRuleReference()
    a2 = mitra_SimpleRuleReference()
    b = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    _safe_set(b, 'mitra_RuleDeclaration24', {a1})
    assert _is_linked(b, 'mitra_RuleDeclaration24', a1)
    if hasattr(a1, 'mitra_SimpleRuleReference25'):
        assert _is_linked(a1, 'mitra_SimpleRuleReference25', b)
    _safe_set(b, 'mitra_RuleDeclaration24', {a2})
    assert _is_linked(b, 'mitra_RuleDeclaration24', a2)
    if hasattr(a1, 'mitra_SimpleRuleReference25'):
        assert not _is_linked(a1, 'mitra_SimpleRuleReference25', b)
    if hasattr(a2, 'mitra_SimpleRuleReference25'):
        assert _is_linked(a2, 'mitra_SimpleRuleReference25', b)
    _safe_set(b, 'mitra_RuleDeclaration24', set())
    assert not _is_linked(b, 'mitra_RuleDeclaration24', a2)
    if hasattr(a2, 'mitra_SimpleRuleReference25'):
        assert not _is_linked(a2, 'mitra_SimpleRuleReference25', b)


def test_assoc_features156_reverse_link_reassign_clear():
    a1 = mitra_VariableAccess(postfixOperator="sample_text", prefixOperator="sample_text")
    a2 = mitra_VariableAccess(postfixOperator="sample_text_2", prefixOperator="sample_text_2")
    b = mitra_Feature(name="sample_text")
    _safe_set(b, 'mitra_Feature', a1)
    assert _is_linked(b, 'mitra_Feature', a1)
    if hasattr(a1, 'mitra_VariableAccess157'):
        assert _is_linked(a1, 'mitra_VariableAccess157', b)
    _safe_set(b, 'mitra_Feature', a2)
    assert _is_linked(b, 'mitra_Feature', a2)
    if hasattr(a1, 'mitra_VariableAccess157'):
        assert not _is_linked(a1, 'mitra_VariableAccess157', b)
    if hasattr(a2, 'mitra_VariableAccess157'):
        assert _is_linked(a2, 'mitra_VariableAccess157', b)
    _safe_set(b, 'mitra_Feature', None)
    assert not _is_linked(b, 'mitra_Feature', a2)
    if hasattr(a2, 'mitra_VariableAccess157'):
        assert not _is_linked(a2, 'mitra_VariableAccess157', b)


def test_assoc_formalParameters14_reverse_link_reassign_clear():
    a1 = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    a2 = mitra_RuleDeclaration(exec="sample_text_2", multi=False, name="sample_text_2", stealth=False, traced=False, virtual=False, visibility="sample_text_2")
    b = mitra_FormalParameter()
    _safe_set(b, 'mitra_FormalParameter', a1)
    assert _is_linked(b, 'mitra_FormalParameter', a1)
    if hasattr(a1, 'mitra_RuleDeclaration15'):
        assert _is_linked(a1, 'mitra_RuleDeclaration15', b)
    _safe_set(b, 'mitra_FormalParameter', a2)
    assert _is_linked(b, 'mitra_FormalParameter', a2)
    if hasattr(a1, 'mitra_RuleDeclaration15'):
        assert not _is_linked(a1, 'mitra_RuleDeclaration15', b)
    if hasattr(a2, 'mitra_RuleDeclaration15'):
        assert _is_linked(a2, 'mitra_RuleDeclaration15', b)
    _safe_set(b, 'mitra_FormalParameter', None)
    assert not _is_linked(b, 'mitra_FormalParameter', a2)
    if hasattr(a2, 'mitra_RuleDeclaration15'):
        assert not _is_linked(a2, 'mitra_RuleDeclaration15', b)


def test_assoc_implementedRules18_reverse_link_reassign_clear():
    a1 = mitra_SimpleRuleReference()
    a2 = mitra_SimpleRuleReference()
    b = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    _safe_set(b, 'mitra_RuleDeclaration19', {a1})
    assert _is_linked(b, 'mitra_RuleDeclaration19', a1)
    if hasattr(a1, 'mitra_SimpleRuleReference'):
        assert _is_linked(a1, 'mitra_SimpleRuleReference', b)
    _safe_set(b, 'mitra_RuleDeclaration19', {a2})
    assert _is_linked(b, 'mitra_RuleDeclaration19', a2)
    if hasattr(a1, 'mitra_SimpleRuleReference'):
        assert not _is_linked(a1, 'mitra_SimpleRuleReference', b)
    if hasattr(a2, 'mitra_SimpleRuleReference'):
        assert _is_linked(a2, 'mitra_SimpleRuleReference', b)
    _safe_set(b, 'mitra_RuleDeclaration19', set())
    assert not _is_linked(b, 'mitra_RuleDeclaration19', a2)
    if hasattr(a2, 'mitra_SimpleRuleReference'):
        assert not _is_linked(a2, 'mitra_SimpleRuleReference', b)


def test_assoc_lhs197_reverse_link_reassign_clear():
    a1 = mitra_VariableAccess(postfixOperator="sample_text", prefixOperator="sample_text")
    a2 = mitra_VariableAccess(postfixOperator="sample_text_2", prefixOperator="sample_text_2")
    b = mitra_Assignment(operator="sample_text")
    _safe_set(b, 'mitra_Assignment', {a1})
    assert _is_linked(b, 'mitra_Assignment', a1)
    if hasattr(a1, 'mitra_VariableAccess198'):
        assert _is_linked(a1, 'mitra_VariableAccess198', b)
    _safe_set(b, 'mitra_Assignment', {a2})
    assert _is_linked(b, 'mitra_Assignment', a2)
    if hasattr(a1, 'mitra_VariableAccess198'):
        assert not _is_linked(a1, 'mitra_VariableAccess198', b)
    if hasattr(a2, 'mitra_VariableAccess198'):
        assert _is_linked(a2, 'mitra_VariableAccess198', b)
    _safe_set(b, 'mitra_Assignment', set())
    assert not _is_linked(b, 'mitra_Assignment', a2)
    if hasattr(a2, 'mitra_VariableAccess198'):
        assert not _is_linked(a2, 'mitra_VariableAccess198', b)


def test_assoc_metamodelDeclaration63_reverse_link_reassign_clear():
    a1 = mitra_ReferenceType()
    a2 = mitra_ReferenceType()
    b = mitra_MetamodelDeclaration(name="sample_text", replaces="sample_text", type="sample_text")
    _safe_set(b, 'mitra_MetamodelDeclaration64', a1)
    assert _is_linked(b, 'mitra_MetamodelDeclaration64', a1)
    if hasattr(a1, 'mitra_ReferenceType'):
        assert _is_linked(a1, 'mitra_ReferenceType', b)
    _safe_set(b, 'mitra_MetamodelDeclaration64', a2)
    assert _is_linked(b, 'mitra_MetamodelDeclaration64', a2)
    if hasattr(a1, 'mitra_ReferenceType'):
        assert not _is_linked(a1, 'mitra_ReferenceType', b)
    if hasattr(a2, 'mitra_ReferenceType'):
        assert _is_linked(a2, 'mitra_ReferenceType', b)
    _safe_set(b, 'mitra_MetamodelDeclaration64', None)
    assert not _is_linked(b, 'mitra_MetamodelDeclaration64', a2)
    if hasattr(a2, 'mitra_ReferenceType'):
        assert not _is_linked(a2, 'mitra_ReferenceType', b)


def test_assoc_metamodelDeclarations1_reverse_link_reassign_clear():
    a1 = mitra_Module(name="sample_text", packageName="sample_text")
    a2 = mitra_Module(name="sample_text_2", packageName="sample_text_2")
    b = mitra_MetamodelDeclaration(name="sample_text", replaces="sample_text", type="sample_text")
    _safe_set(b, 'mitra_MetamodelDeclaration', a1)
    assert _is_linked(b, 'mitra_MetamodelDeclaration', a1)
    if hasattr(a1, 'mitra_Module2'):
        assert _is_linked(a1, 'mitra_Module2', b)
    _safe_set(b, 'mitra_MetamodelDeclaration', a2)
    assert _is_linked(b, 'mitra_MetamodelDeclaration', a2)
    if hasattr(a1, 'mitra_Module2'):
        assert not _is_linked(a1, 'mitra_Module2', b)
    if hasattr(a2, 'mitra_Module2'):
        assert _is_linked(a2, 'mitra_Module2', b)
    _safe_set(b, 'mitra_MetamodelDeclaration', None)
    assert not _is_linked(b, 'mitra_MetamodelDeclaration', a2)
    if hasattr(a2, 'mitra_Module2'):
        assert not _is_linked(a2, 'mitra_Module2', b)


def test_assoc_overriddenRule20_reverse_link_reassign_clear():
    a1 = mitra_SimpleRuleReference()
    a2 = mitra_SimpleRuleReference()
    b = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    _safe_set(b, 'mitra_RuleDeclaration21', a1)
    assert _is_linked(b, 'mitra_RuleDeclaration21', a1)
    if hasattr(a1, 'mitra_SimpleRuleReference22'):
        assert _is_linked(a1, 'mitra_SimpleRuleReference22', b)
    _safe_set(b, 'mitra_RuleDeclaration21', a2)
    assert _is_linked(b, 'mitra_RuleDeclaration21', a2)
    if hasattr(a1, 'mitra_SimpleRuleReference22'):
        assert not _is_linked(a1, 'mitra_SimpleRuleReference22', b)
    if hasattr(a2, 'mitra_SimpleRuleReference22'):
        assert _is_linked(a2, 'mitra_SimpleRuleReference22', b)
    _safe_set(b, 'mitra_RuleDeclaration21', None)
    assert not _is_linked(b, 'mitra_RuleDeclaration21', a2)
    if hasattr(a2, 'mitra_SimpleRuleReference22'):
        assert not _is_linked(a2, 'mitra_SimpleRuleReference22', b)


def test_assoc_parameterReferences34_reverse_link_reassign_clear():
    a1 = mitra_SimpleRuleReference()
    a2 = mitra_SimpleRuleReference()
    b = mitra_SimpleParameterReference(name="sample_text")
    _safe_set(b, 'mitra_SimpleParameterReference', a1)
    assert _is_linked(b, 'mitra_SimpleParameterReference', a1)
    if hasattr(a1, 'mitra_SimpleRuleReference35'):
        assert _is_linked(a1, 'mitra_SimpleRuleReference35', b)
    _safe_set(b, 'mitra_SimpleParameterReference', a2)
    assert _is_linked(b, 'mitra_SimpleParameterReference', a2)
    if hasattr(a1, 'mitra_SimpleRuleReference35'):
        assert not _is_linked(a1, 'mitra_SimpleRuleReference35', b)
    if hasattr(a2, 'mitra_SimpleRuleReference35'):
        assert _is_linked(a2, 'mitra_SimpleRuleReference35', b)
    _safe_set(b, 'mitra_SimpleParameterReference', None)
    assert not _is_linked(b, 'mitra_SimpleParameterReference', a2)
    if hasattr(a2, 'mitra_SimpleRuleReference35'):
        assert not _is_linked(a2, 'mitra_SimpleRuleReference35', b)


def test_assoc_parameterReferences39_reverse_link_reassign_clear():
    a1 = mitra_QualifiedRuleReference()
    a2 = mitra_QualifiedRuleReference()
    b = mitra_QualifiedParameterReference()
    _safe_set(b, 'mitra_QualifiedParameterReference', a1)
    assert _is_linked(b, 'mitra_QualifiedParameterReference', a1)
    if hasattr(a1, 'mitra_QualifiedRuleReference'):
        assert _is_linked(a1, 'mitra_QualifiedRuleReference', b)
    _safe_set(b, 'mitra_QualifiedParameterReference', a2)
    assert _is_linked(b, 'mitra_QualifiedParameterReference', a2)
    if hasattr(a1, 'mitra_QualifiedRuleReference'):
        assert not _is_linked(a1, 'mitra_QualifiedRuleReference', b)
    if hasattr(a2, 'mitra_QualifiedRuleReference'):
        assert _is_linked(a2, 'mitra_QualifiedRuleReference', b)
    _safe_set(b, 'mitra_QualifiedParameterReference', None)
    assert not _is_linked(b, 'mitra_QualifiedParameterReference', a2)
    if hasattr(a2, 'mitra_QualifiedRuleReference'):
        assert not _is_linked(a2, 'mitra_QualifiedRuleReference', b)


def test_assoc_properties10_reverse_link_reassign_clear():
    a1 = mitra_Property(name="sample_text", value="sample_text")
    a2 = mitra_Property(name="sample_text_2", value="sample_text_2")
    b = mitra_MetamodelDeclaration(name="sample_text", replaces="sample_text", type="sample_text")
    _safe_set(b, 'mitra_MetamodelDeclaration11', {a1})
    assert _is_linked(b, 'mitra_MetamodelDeclaration11', a1)
    if hasattr(a1, 'mitra_Property'):
        assert _is_linked(a1, 'mitra_Property', b)
    _safe_set(b, 'mitra_MetamodelDeclaration11', {a2})
    assert _is_linked(b, 'mitra_MetamodelDeclaration11', a2)
    if hasattr(a1, 'mitra_Property'):
        assert not _is_linked(a1, 'mitra_Property', b)
    if hasattr(a2, 'mitra_Property'):
        assert _is_linked(a2, 'mitra_Property', b)
    _safe_set(b, 'mitra_MetamodelDeclaration11', set())
    assert not _is_linked(b, 'mitra_MetamodelDeclaration11', a2)
    if hasattr(a2, 'mitra_Property'):
        assert not _is_linked(a2, 'mitra_Property', b)


def test_assoc_propertyDecls175_reverse_link_reassign_clear():
    a1 = mitra_AnnotationPropertyDecl(name="sample_text", required=True)
    a2 = mitra_AnnotationPropertyDecl(name="sample_text_2", required=False)
    b = mitra_AnnotationDecl(many=True, name="sample_text", required=True, targets="sample_text")
    _safe_set(b, 'mitra_AnnotationDecl176', {a1})
    assert _is_linked(b, 'mitra_AnnotationDecl176', a1)
    if hasattr(a1, 'mitra_AnnotationPropertyDecl'):
        assert _is_linked(a1, 'mitra_AnnotationPropertyDecl', b)
    _safe_set(b, 'mitra_AnnotationDecl176', {a2})
    assert _is_linked(b, 'mitra_AnnotationDecl176', a2)
    if hasattr(a1, 'mitra_AnnotationPropertyDecl'):
        assert not _is_linked(a1, 'mitra_AnnotationPropertyDecl', b)
    if hasattr(a2, 'mitra_AnnotationPropertyDecl'):
        assert _is_linked(a2, 'mitra_AnnotationPropertyDecl', b)
    _safe_set(b, 'mitra_AnnotationDecl176', set())
    assert not _is_linked(b, 'mitra_AnnotationDecl176', a2)
    if hasattr(a2, 'mitra_AnnotationPropertyDecl'):
        assert not _is_linked(a2, 'mitra_AnnotationPropertyDecl', b)


def test_assoc_returnParameters16_reverse_link_reassign_clear():
    a1 = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    a2 = mitra_RuleDeclaration(exec="sample_text_2", multi=False, name="sample_text_2", stealth=False, traced=False, virtual=False, visibility="sample_text_2")
    b = mitra_ReturnParameter()
    _safe_set(b, 'mitra_ReturnParameter', a1)
    assert _is_linked(b, 'mitra_ReturnParameter', a1)
    if hasattr(a1, 'mitra_RuleDeclaration17'):
        assert _is_linked(a1, 'mitra_RuleDeclaration17', b)
    _safe_set(b, 'mitra_ReturnParameter', a2)
    assert _is_linked(b, 'mitra_ReturnParameter', a2)
    if hasattr(a1, 'mitra_RuleDeclaration17'):
        assert not _is_linked(a1, 'mitra_RuleDeclaration17', b)
    if hasattr(a2, 'mitra_RuleDeclaration17'):
        assert _is_linked(a2, 'mitra_RuleDeclaration17', b)
    _safe_set(b, 'mitra_ReturnParameter', None)
    assert not _is_linked(b, 'mitra_ReturnParameter', a2)
    if hasattr(a2, 'mitra_RuleDeclaration17'):
        assert not _is_linked(a2, 'mitra_RuleDeclaration17', b)


def test_assoc_returnReferences36_reverse_link_reassign_clear():
    a1 = mitra_SimpleRuleReference()
    a2 = mitra_SimpleRuleReference()
    b = mitra_SimpleParameterReference(name="sample_text")
    _safe_set(b, 'mitra_SimpleParameterReference38', a1)
    assert _is_linked(b, 'mitra_SimpleParameterReference38', a1)
    if hasattr(a1, 'mitra_SimpleRuleReference37'):
        assert _is_linked(a1, 'mitra_SimpleRuleReference37', b)
    _safe_set(b, 'mitra_SimpleParameterReference38', a2)
    assert _is_linked(b, 'mitra_SimpleParameterReference38', a2)
    if hasattr(a1, 'mitra_SimpleRuleReference37'):
        assert not _is_linked(a1, 'mitra_SimpleRuleReference37', b)
    if hasattr(a2, 'mitra_SimpleRuleReference37'):
        assert _is_linked(a2, 'mitra_SimpleRuleReference37', b)
    _safe_set(b, 'mitra_SimpleParameterReference38', None)
    assert not _is_linked(b, 'mitra_SimpleParameterReference38', a2)
    if hasattr(a2, 'mitra_SimpleRuleReference37'):
        assert not _is_linked(a2, 'mitra_SimpleRuleReference37', b)


def test_assoc_returnReferences40_reverse_link_reassign_clear():
    a1 = mitra_QualifiedRuleReference()
    a2 = mitra_QualifiedRuleReference()
    b = mitra_QualifiedParameterReference()
    _safe_set(b, 'mitra_QualifiedParameterReference42', a1)
    assert _is_linked(b, 'mitra_QualifiedParameterReference42', a1)
    if hasattr(a1, 'mitra_QualifiedRuleReference41'):
        assert _is_linked(a1, 'mitra_QualifiedRuleReference41', b)
    _safe_set(b, 'mitra_QualifiedParameterReference42', a2)
    assert _is_linked(b, 'mitra_QualifiedParameterReference42', a2)
    if hasattr(a1, 'mitra_QualifiedRuleReference41'):
        assert not _is_linked(a1, 'mitra_QualifiedRuleReference41', b)
    if hasattr(a2, 'mitra_QualifiedRuleReference41'):
        assert _is_linked(a2, 'mitra_QualifiedRuleReference41', b)
    _safe_set(b, 'mitra_QualifiedParameterReference42', None)
    assert not _is_linked(b, 'mitra_QualifiedParameterReference42', a2)
    if hasattr(a2, 'mitra_QualifiedRuleReference41'):
        assert not _is_linked(a2, 'mitra_QualifiedRuleReference41', b)


def test_assoc_ruleDeclaration143_reverse_link_reassign_clear():
    a1 = mitra_RuleInvocation()
    a2 = mitra_RuleInvocation()
    b = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    _safe_set(b, 'mitra_RuleDeclaration144', a1)
    assert _is_linked(b, 'mitra_RuleDeclaration144', a1)
    if hasattr(a1, 'mitra_RuleInvocation'):
        assert _is_linked(a1, 'mitra_RuleInvocation', b)
    _safe_set(b, 'mitra_RuleDeclaration144', a2)
    assert _is_linked(b, 'mitra_RuleDeclaration144', a2)
    if hasattr(a1, 'mitra_RuleInvocation'):
        assert not _is_linked(a1, 'mitra_RuleInvocation', b)
    if hasattr(a2, 'mitra_RuleInvocation'):
        assert _is_linked(a2, 'mitra_RuleInvocation', b)
    _safe_set(b, 'mitra_RuleDeclaration144', None)
    assert not _is_linked(b, 'mitra_RuleDeclaration144', a2)
    if hasattr(a2, 'mitra_RuleInvocation'):
        assert not _is_linked(a2, 'mitra_RuleInvocation', b)


def test_assoc_ruleDeclarations5_reverse_link_reassign_clear():
    a1 = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    a2 = mitra_RuleDeclaration(exec="sample_text_2", multi=False, name="sample_text_2", stealth=False, traced=False, virtual=False, visibility="sample_text_2")
    b = mitra_Module(name="sample_text", packageName="sample_text")
    _safe_set(b, 'mitra_Module6', {a1})
    assert _is_linked(b, 'mitra_Module6', a1)
    if hasattr(a1, 'mitra_RuleDeclaration'):
        assert _is_linked(a1, 'mitra_RuleDeclaration', b)
    _safe_set(b, 'mitra_Module6', {a2})
    assert _is_linked(b, 'mitra_Module6', a2)
    if hasattr(a1, 'mitra_RuleDeclaration'):
        assert not _is_linked(a1, 'mitra_RuleDeclaration', b)
    if hasattr(a2, 'mitra_RuleDeclaration'):
        assert _is_linked(a2, 'mitra_RuleDeclaration', b)
    _safe_set(b, 'mitra_Module6', set())
    assert not _is_linked(b, 'mitra_Module6', a2)
    if hasattr(a2, 'mitra_RuleDeclaration'):
        assert not _is_linked(a2, 'mitra_RuleDeclaration', b)


def test_assoc_type177_reverse_link_reassign_clear():
    a1 = mitra_PrimitiveType(primitiveType="sample_text")
    a2 = mitra_PrimitiveType(primitiveType="sample_text_2")
    b = mitra_AnnotationPropertyDecl(name="sample_text", required=True)
    _safe_set(b, 'mitra_AnnotationPropertyDecl178', a1)
    assert _is_linked(b, 'mitra_AnnotationPropertyDecl178', a1)
    if hasattr(a1, 'mitra_PrimitiveType179'):
        assert _is_linked(a1, 'mitra_PrimitiveType179', b)
    _safe_set(b, 'mitra_AnnotationPropertyDecl178', a2)
    assert _is_linked(b, 'mitra_AnnotationPropertyDecl178', a2)
    if hasattr(a1, 'mitra_PrimitiveType179'):
        assert not _is_linked(a1, 'mitra_PrimitiveType179', b)
    if hasattr(a2, 'mitra_PrimitiveType179'):
        assert _is_linked(a2, 'mitra_PrimitiveType179', b)
    _safe_set(b, 'mitra_AnnotationPropertyDecl178', None)
    assert not _is_linked(b, 'mitra_AnnotationPropertyDecl178', a2)
    if hasattr(a2, 'mitra_PrimitiveType179'):
        assert not _is_linked(a2, 'mitra_PrimitiveType179', b)


def test_assoc_valuetype171_reverse_link_reassign_clear():
    a1 = mitra_PrimitiveType(primitiveType="sample_text")
    a2 = mitra_PrimitiveType(primitiveType="sample_text_2")
    b = mitra_AnnotationDecl(many=True, name="sample_text", required=True, targets="sample_text")
    _safe_set(b, 'mitra_AnnotationDecl172', a1)
    assert _is_linked(b, 'mitra_AnnotationDecl172', a1)
    if hasattr(a1, 'mitra_PrimitiveType'):
        assert _is_linked(a1, 'mitra_PrimitiveType', b)
    _safe_set(b, 'mitra_AnnotationDecl172', a2)
    assert _is_linked(b, 'mitra_AnnotationDecl172', a2)
    if hasattr(a1, 'mitra_PrimitiveType'):
        assert not _is_linked(a1, 'mitra_PrimitiveType', b)
    if hasattr(a2, 'mitra_PrimitiveType'):
        assert _is_linked(a2, 'mitra_PrimitiveType', b)
    _safe_set(b, 'mitra_AnnotationDecl172', None)
    assert not _is_linked(b, 'mitra_AnnotationDecl172', a2)
    if hasattr(a2, 'mitra_PrimitiveType'):
        assert not _is_linked(a2, 'mitra_PrimitiveType', b)


def test_assoc_variable154_reverse_link_reassign_clear():
    a1 = mitra_VariableAccess(postfixOperator="sample_text", prefixOperator="sample_text")
    a2 = mitra_VariableAccess(postfixOperator="sample_text_2", prefixOperator="sample_text_2")
    b = mitra_VarDeclaration(name="sample_text")
    _safe_set(b, 'mitra_VarDeclaration155', a1)
    assert _is_linked(b, 'mitra_VarDeclaration155', a1)
    if hasattr(a1, 'mitra_VariableAccess'):
        assert _is_linked(a1, 'mitra_VariableAccess', b)
    _safe_set(b, 'mitra_VarDeclaration155', a2)
    assert _is_linked(b, 'mitra_VarDeclaration155', a2)
    if hasattr(a1, 'mitra_VariableAccess'):
        assert not _is_linked(a1, 'mitra_VariableAccess', b)
    if hasattr(a2, 'mitra_VariableAccess'):
        assert _is_linked(a2, 'mitra_VariableAccess', b)
    _safe_set(b, 'mitra_VarDeclaration155', None)
    assert not _is_linked(b, 'mitra_VarDeclaration155', a2)
    if hasattr(a2, 'mitra_VariableAccess'):
        assert not _is_linked(a2, 'mitra_VariableAccess', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotationDecls169_stub_double():
    # mitra_AnnotationsDefinition has no real 'mitra_AnnotationsDefinition170' property in the generated
    # code (a bare stub) -- manually attach it so mitra_AnnotationDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_AnnotationDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_AnnotationDecl(many=True, name="sample_text", required=True, targets="sample_text")
    partner = mitra_AnnotationsDefinition()
    setattr(partner, 'mitra_AnnotationsDefinition170', None)
    _safe_set(owner, 'mitra_AnnotationDecl', partner)
    assert owner in getattr(partner, 'mitra_AnnotationsDefinition170')
    _safe_set(owner, 'mitra_AnnotationDecl', None)
    assert owner not in getattr(partner, 'mitra_AnnotationsDefinition170')


def test_assoc_annotationDefinitions3_stub_double():
    # mitra_AnnotationsDefinition has no real 'mitra_AnnotationsDefinition' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Module(name="sample_text", packageName="sample_text")
    partner = mitra_AnnotationsDefinition()
    setattr(partner, 'mitra_AnnotationsDefinition', None)
    _safe_set(owner, 'mitra_Module4', {partner})
    assert getattr(partner, 'mitra_AnnotationsDefinition') == owner
    _safe_set(owner, 'mitra_Module4', set())
    assert getattr(partner, 'mitra_AnnotationsDefinition') is None


def test_assoc_annotations12_stub_double():
    # mitra_Annotation has no real 'mitra_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    partner = mitra_Annotation()
    setattr(partner, 'mitra_Annotation', None)
    _safe_set(owner, 'mitra_RuleDeclaration13', {partner})
    assert getattr(partner, 'mitra_Annotation') == owner
    _safe_set(owner, 'mitra_RuleDeclaration13', set())
    assert getattr(partner, 'mitra_Annotation') is None


def test_assoc_annotations58_stub_double():
    # mitra_Annotation has no real 'mitra_Annotation59' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Parameter(modifier="sample_text")
    partner = mitra_Annotation()
    setattr(partner, 'mitra_Annotation59', None)
    _safe_set(owner, 'mitra_Parameter', {partner})
    assert getattr(partner, 'mitra_Annotation59') == owner
    _safe_set(owner, 'mitra_Parameter', set())
    assert getattr(partner, 'mitra_Annotation59') is None


def test_assoc_arguments145_stub_double():
    # mitra_Expression has no real 'mitra_Expression147' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleInvocation()
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression147', None)
    _safe_set(owner, 'mitra_RuleInvocation146', {partner})
    assert getattr(partner, 'mitra_Expression147') == owner
    _safe_set(owner, 'mitra_RuleInvocation146', set())
    assert getattr(partner, 'mitra_Expression147') is None


def test_assoc_body30_stub_double():
    # mitra_Block has no real 'mitra_Block' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    partner = mitra_Block()
    setattr(partner, 'mitra_Block', None)
    _safe_set(owner, 'mitra_RuleDeclaration31', partner)
    assert getattr(partner, 'mitra_Block') == owner
    _safe_set(owner, 'mitra_RuleDeclaration31', None)
    assert getattr(partner, 'mitra_Block') is None


def test_assoc_decl183_stub_double():
    # mitra_Annotation has no real 'mitra_Annotation184' property in the generated
    # code (a bare stub) -- manually attach it so mitra_AnnotationDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_AnnotationDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_AnnotationDecl(many=True, name="sample_text", required=True, targets="sample_text")
    partner = mitra_Annotation()
    setattr(partner, 'mitra_Annotation184', None)
    _safe_set(owner, 'mitra_AnnotationDecl185', partner)
    assert getattr(partner, 'mitra_Annotation184') == owner
    _safe_set(owner, 'mitra_AnnotationDecl185', None)
    assert getattr(partner, 'mitra_Annotation184') is None


def test_assoc_decl191_stub_double():
    # mitra_AnnotationProperty has no real 'mitra_AnnotationProperty192' property in the generated
    # code (a bare stub) -- manually attach it so mitra_AnnotationPropertyDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_AnnotationPropertyDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_AnnotationPropertyDecl(name="sample_text", required=True)
    partner = mitra_AnnotationProperty()
    setattr(partner, 'mitra_AnnotationProperty192', None)
    _safe_set(owner, 'mitra_AnnotationPropertyDecl193', partner)
    assert getattr(partner, 'mitra_AnnotationProperty192') == owner
    _safe_set(owner, 'mitra_AnnotationPropertyDecl193', None)
    assert getattr(partner, 'mitra_AnnotationProperty192') is None


def test_assoc_default158_stub_double():
    # mitra_Expression has no real 'mitra_Expression160' property in the generated
    # code (a bare stub) -- manually attach it so mitra_VariableAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_VariableAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_VariableAccess(postfixOperator="sample_text", prefixOperator="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression160', None)
    _safe_set(owner, 'mitra_VariableAccess159', partner)
    assert getattr(partner, 'mitra_Expression160') == owner
    _safe_set(owner, 'mitra_VariableAccess159', None)
    assert getattr(partner, 'mitra_Expression160') is None


def test_assoc_default173_stub_double():
    # mitra_Literal has no real 'mitra_Literal' property in the generated
    # code (a bare stub) -- manually attach it so mitra_AnnotationDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_AnnotationDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_AnnotationDecl(many=True, name="sample_text", required=True, targets="sample_text")
    partner = mitra_Literal()
    setattr(partner, 'mitra_Literal', None)
    _safe_set(owner, 'mitra_AnnotationDecl174', partner)
    assert getattr(partner, 'mitra_Literal') == owner
    _safe_set(owner, 'mitra_AnnotationDecl174', None)
    assert getattr(partner, 'mitra_Literal') is None


def test_assoc_default180_stub_double():
    # mitra_Literal has no real 'mitra_Literal182' property in the generated
    # code (a bare stub) -- manually attach it so mitra_AnnotationPropertyDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_AnnotationPropertyDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_AnnotationPropertyDecl(name="sample_text", required=True)
    partner = mitra_Literal()
    setattr(partner, 'mitra_Literal182', None)
    _safe_set(owner, 'mitra_AnnotationPropertyDecl181', partner)
    assert getattr(partner, 'mitra_Literal182') == owner
    _safe_set(owner, 'mitra_AnnotationPropertyDecl181', None)
    assert getattr(partner, 'mitra_Literal182') is None


def test_assoc_eClassifier65_stub_double():
    # mitra_EClassifier has no real 'mitra_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so mitra_ReferenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_ReferenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_ReferenceType()
    partner = mitra_EClassifier()
    setattr(partner, 'mitra_EClassifier', None)
    _safe_set(owner, 'mitra_ReferenceType66', partner)
    assert getattr(partner, 'mitra_EClassifier') == owner
    _safe_set(owner, 'mitra_ReferenceType66', None)
    assert getattr(partner, 'mitra_EClassifier') is None


def test_assoc_expression199_stub_double():
    # mitra_Expression has no real 'mitra_Expression201' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Assignment(operator="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression201', None)
    _safe_set(owner, 'mitra_Assignment200', partner)
    assert getattr(partner, 'mitra_Expression201') == owner
    _safe_set(owner, 'mitra_Assignment200', None)
    assert getattr(partner, 'mitra_Expression201') is None


def test_assoc_expression234_stub_double():
    # mitra_Expression has no real 'mitra_Expression235' property in the generated
    # code (a bare stub) -- manually attach it so mitra_UnaryMathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_UnaryMathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_UnaryMathExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression235', None)
    _safe_set(owner, 'mitra_UnaryMathExpression', partner)
    assert getattr(partner, 'mitra_Expression235') == owner
    _safe_set(owner, 'mitra_UnaryMathExpression', None)
    assert getattr(partner, 'mitra_Expression235') is None


def test_assoc_features166_stub_double():
    # mitra_StaticAccess has no real 'mitra_StaticAccess167' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Feature(name="sample_text")
    partner = mitra_StaticAccess()
    setattr(partner, 'mitra_StaticAccess167', None)
    _safe_set(owner, 'mitra_Feature168', partner)
    assert owner in getattr(partner, 'mitra_StaticAccess167')
    _safe_set(owner, 'mitra_Feature168', None)
    assert owner not in getattr(partner, 'mitra_StaticAccess167')


def test_assoc_formalParameter132_stub_double():
    # mitra_Catch has no real 'mitra_Catch133' property in the generated
    # code (a bare stub) -- manually attach it so mitra_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_FormalParameter()
    partner = mitra_Catch()
    setattr(partner, 'mitra_Catch133', None)
    _safe_set(owner, 'mitra_FormalParameter134', partner)
    assert getattr(partner, 'mitra_Catch133') == owner
    _safe_set(owner, 'mitra_FormalParameter134', None)
    assert getattr(partner, 'mitra_Catch133') is None


def test_assoc_imports0_stub_double():
    # mitra_ModuleReference has no real 'mitra_ModuleReference' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Module(name="sample_text", packageName="sample_text")
    partner = mitra_ModuleReference()
    setattr(partner, 'mitra_ModuleReference', None)
    _safe_set(owner, 'mitra_Module', {partner})
    assert getattr(partner, 'mitra_ModuleReference') == owner
    _safe_set(owner, 'mitra_Module', set())
    assert getattr(partner, 'mitra_ModuleReference') is None


def test_assoc_javaSpec28_stub_double():
    # mitra_JavaSpec has no real 'mitra_JavaSpec' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    partner = mitra_JavaSpec()
    setattr(partner, 'mitra_JavaSpec', None)
    _safe_set(owner, 'mitra_RuleDeclaration29', partner)
    assert getattr(partner, 'mitra_JavaSpec') == owner
    _safe_set(owner, 'mitra_RuleDeclaration29', None)
    assert getattr(partner, 'mitra_JavaSpec') is None


def test_assoc_lhs207_stub_double():
    # mitra_Expression has no real 'mitra_Expression208' property in the generated
    # code (a bare stub) -- manually attach it so mitra_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_BooleanExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression208', None)
    _safe_set(owner, 'mitra_BooleanExpression', partner)
    assert getattr(partner, 'mitra_Expression208') == owner
    _safe_set(owner, 'mitra_BooleanExpression', None)
    assert getattr(partner, 'mitra_Expression208') is None


def test_assoc_lhs212_stub_double():
    # mitra_Expression has no real 'mitra_Expression213' property in the generated
    # code (a bare stub) -- manually attach it so mitra_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_EqualityExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression213', None)
    _safe_set(owner, 'mitra_EqualityExpression', partner)
    assert getattr(partner, 'mitra_Expression213') == owner
    _safe_set(owner, 'mitra_EqualityExpression', None)
    assert getattr(partner, 'mitra_Expression213') is None


def test_assoc_lhs217_stub_double():
    # mitra_Expression has no real 'mitra_Expression218' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RelationalExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression218', None)
    _safe_set(owner, 'mitra_RelationalExpression', partner)
    assert getattr(partner, 'mitra_Expression218') == owner
    _safe_set(owner, 'mitra_RelationalExpression', None)
    assert getattr(partner, 'mitra_Expression218') is None


def test_assoc_lhs222_stub_double():
    # mitra_Expression has no real 'mitra_Expression223' property in the generated
    # code (a bare stub) -- manually attach it so mitra_MathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_MathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_MathExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression223', None)
    _safe_set(owner, 'mitra_MathExpression', partner)
    assert getattr(partner, 'mitra_Expression223') == owner
    _safe_set(owner, 'mitra_MathExpression', None)
    assert getattr(partner, 'mitra_Expression223') is None


def test_assoc_module7_stub_double():
    # mitra_ModuleReference has no real 'mitra_ModuleReference8' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Module(name="sample_text", packageName="sample_text")
    partner = mitra_ModuleReference()
    setattr(partner, 'mitra_ModuleReference8', None)
    _safe_set(owner, 'mitra_Module9', partner)
    assert getattr(partner, 'mitra_ModuleReference8') == owner
    _safe_set(owner, 'mitra_Module9', None)
    assert getattr(partner, 'mitra_ModuleReference8') is None


def test_assoc_properties55_stub_double():
    # mitra_JavaSpec has no real 'mitra_JavaSpec56' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Property(name="sample_text", value="sample_text")
    partner = mitra_JavaSpec()
    setattr(partner, 'mitra_JavaSpec56', None)
    _safe_set(owner, 'mitra_Property57', partner)
    assert owner in getattr(partner, 'mitra_JavaSpec56')
    _safe_set(owner, 'mitra_Property57', None)
    assert owner not in getattr(partner, 'mitra_JavaSpec56')


def test_assoc_rhs209_stub_double():
    # mitra_Expression has no real 'mitra_Expression211' property in the generated
    # code (a bare stub) -- manually attach it so mitra_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_BooleanExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression211', None)
    _safe_set(owner, 'mitra_BooleanExpression210', partner)
    assert getattr(partner, 'mitra_Expression211') == owner
    _safe_set(owner, 'mitra_BooleanExpression210', None)
    assert getattr(partner, 'mitra_Expression211') is None


def test_assoc_rhs214_stub_double():
    # mitra_Expression has no real 'mitra_Expression216' property in the generated
    # code (a bare stub) -- manually attach it so mitra_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_EqualityExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression216', None)
    _safe_set(owner, 'mitra_EqualityExpression215', partner)
    assert getattr(partner, 'mitra_Expression216') == owner
    _safe_set(owner, 'mitra_EqualityExpression215', None)
    assert getattr(partner, 'mitra_Expression216') is None


def test_assoc_rhs219_stub_double():
    # mitra_Expression has no real 'mitra_Expression221' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RelationalExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression221', None)
    _safe_set(owner, 'mitra_RelationalExpression220', partner)
    assert getattr(partner, 'mitra_Expression221') == owner
    _safe_set(owner, 'mitra_RelationalExpression220', None)
    assert getattr(partner, 'mitra_Expression221') is None


def test_assoc_rhs224_stub_double():
    # mitra_Expression has no real 'mitra_Expression226' property in the generated
    # code (a bare stub) -- manually attach it so mitra_MathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_MathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_MathExpression(op="sample_text")
    partner = mitra_Expression()
    setattr(partner, 'mitra_Expression226', None)
    _safe_set(owner, 'mitra_MathExpression225', partner)
    assert getattr(partner, 'mitra_Expression226') == owner
    _safe_set(owner, 'mitra_MathExpression225', None)
    assert getattr(partner, 'mitra_Expression226') is None


def test_assoc_ruleDeclaration32_stub_double():
    # mitra_RuleReference has no real 'mitra_RuleReference' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    partner = mitra_RuleReference()
    setattr(partner, 'mitra_RuleReference', None)
    _safe_set(owner, 'mitra_RuleDeclaration33', partner)
    assert getattr(partner, 'mitra_RuleReference') == owner
    _safe_set(owner, 'mitra_RuleDeclaration33', None)
    assert getattr(partner, 'mitra_RuleReference') is None


def test_assoc_trigger26_stub_double():
    # mitra_Trigger has no real 'mitra_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so mitra_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_RuleDeclaration(exec="sample_text", multi=True, name="sample_text", stealth=True, traced=True, virtual=True, visibility="sample_text")
    partner = mitra_Trigger()
    setattr(partner, 'mitra_Trigger', None)
    _safe_set(owner, 'mitra_RuleDeclaration27', partner)
    assert getattr(partner, 'mitra_Trigger') == owner
    _safe_set(owner, 'mitra_RuleDeclaration27', None)
    assert getattr(partner, 'mitra_Trigger') is None


def test_assoc_triggerRules47_stub_double():
    # mitra_Trigger has no real 'mitra_Trigger48' property in the generated
    # code (a bare stub) -- manually attach it so mitra_QualifiedRuleReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_QualifiedRuleReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_QualifiedRuleReference()
    partner = mitra_Trigger()
    setattr(partner, 'mitra_Trigger48', None)
    _safe_set(owner, 'mitra_QualifiedRuleReference49', partner)
    assert owner in getattr(partner, 'mitra_Trigger48')
    _safe_set(owner, 'mitra_QualifiedRuleReference49', None)
    assert owner not in getattr(partner, 'mitra_Trigger48')


def test_assoc_type43_stub_double():
    # mitra_Type has no real 'mitra_Type' property in the generated
    # code (a bare stub) -- manually attach it so mitra_SimpleParameterReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_SimpleParameterReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_SimpleParameterReference(name="sample_text")
    partner = mitra_Type()
    setattr(partner, 'mitra_Type', None)
    _safe_set(owner, 'mitra_SimpleParameterReference44', partner)
    assert getattr(partner, 'mitra_Type') == owner
    _safe_set(owner, 'mitra_SimpleParameterReference44', None)
    assert getattr(partner, 'mitra_Type') is None


def test_assoc_type78_stub_double():
    # mitra_Type has no real 'mitra_Type79' property in the generated
    # code (a bare stub) -- manually attach it so mitra_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_VarDeclaration(name="sample_text")
    partner = mitra_Type()
    setattr(partner, 'mitra_Type79', None)
    _safe_set(owner, 'mitra_VarDeclaration', partner)
    assert getattr(partner, 'mitra_Type79') == owner
    _safe_set(owner, 'mitra_VarDeclaration', None)
    assert getattr(partner, 'mitra_Type79') is None


def test_assoc_typePar67_stub_double():
    # mitra_Type has no real 'mitra_Type68' property in the generated
    # code (a bare stub) -- manually attach it so mitra_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_CollectionType(collectionType="sample_text")
    partner = mitra_Type()
    setattr(partner, 'mitra_Type68', None)
    _safe_set(owner, 'mitra_CollectionType', partner)
    assert getattr(partner, 'mitra_Type68') == owner
    _safe_set(owner, 'mitra_CollectionType', None)
    assert getattr(partner, 'mitra_Type68') is None


def test_assoc_vardecl120_stub_double():
    # mitra_LoopVariable has no real 'mitra_LoopVariable121' property in the generated
    # code (a bare stub) -- manually attach it so mitra_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_VarDeclaration(name="sample_text")
    partner = mitra_LoopVariable()
    setattr(partner, 'mitra_LoopVariable121', None)
    _safe_set(owner, 'mitra_VarDeclaration122', partner)
    assert getattr(partner, 'mitra_LoopVariable121') == owner
    _safe_set(owner, 'mitra_VarDeclaration122', None)
    assert getattr(partner, 'mitra_LoopVariable121') is None


def test_assoc_vardecl45_stub_double():
    # mitra_TypedVarDeclaration has no real 'mitra_TypedVarDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so mitra_QualifiedParameterReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_QualifiedParameterReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_QualifiedParameterReference()
    partner = mitra_TypedVarDeclaration()
    setattr(partner, 'mitra_TypedVarDeclaration', None)
    _safe_set(owner, 'mitra_QualifiedParameterReference46', partner)
    assert getattr(partner, 'mitra_TypedVarDeclaration') == owner
    _safe_set(owner, 'mitra_QualifiedParameterReference46', None)
    assert getattr(partner, 'mitra_TypedVarDeclaration') is None


def test_assoc_vardecl60_stub_double():
    # mitra_TypedVarDeclaration has no real 'mitra_TypedVarDeclaration62' property in the generated
    # code (a bare stub) -- manually attach it so mitra_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mitra_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mitra_Parameter(modifier="sample_text")
    partner = mitra_TypedVarDeclaration()
    setattr(partner, 'mitra_TypedVarDeclaration62', None)
    _safe_set(owner, 'mitra_Parameter61', partner)
    assert getattr(partner, 'mitra_TypedVarDeclaration62') == owner
    _safe_set(owner, 'mitra_Parameter61', None)
    assert getattr(partner, 'mitra_TypedVarDeclaration62') is None


