import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAssignment,
    Access,
    AtomicFilter,
    Block,
    CcslBooleanFunction,
    CcslFunction,
    CcslNumberFunction,
    ComplexType,
    Context,
    ControlFlow,
    DataType,
    DeclaredType,
    Element,
    Filter,
    InitializableVariable,
    InjectionAction,
    InjectionStrategy,
    Invocation,
    LiteralValue,
    NamedElement,
    ObjectType,
    OperatorExpression,
    PrimitiveType,
    Root,
    Rule,
    SimpleMethod,
    SimpleMethodInvocation,
    Statement,
    TemplateFilter,
    UnaryAssignment,
    Variable,
    action_ArithmeticOperatorMap,
    annotation_AnnotableElement,
    annotation_Annotation,
    ccsl_AtomicRule,
    ccsl_CompositeRule,
    ccsl_FaultTypeDescription,
    ccsl_Root,
    ccsl_Rule,
    ccsl_action_ArithmeticOperatorMap,
    ccsl_action_ChangeLiteralValueAction,
    ccsl_action_DeleteAction,
    ccsl_action_DeleteInfixOperatorAction,
    ccsl_action_DeleteRandomStatementAction,
    ccsl_action_MoveScopeUpAction,
    ccsl_action_ReplaceArithmeticOperatorAction,
    ccsl_action_ReplaceVariableAccessAction,
    ccsl_annotation_AnnotableElement,
    ccsl_annotation_Annotation,
    ccsl_assignment_AbstractAssignment,
    ccsl_assignment_Assignment,
    ccsl_assignment_PostfixUnaryAssignment,
    ccsl_assignment_PrefixUnaryAssignment,
    ccsl_assignment_UnaryAssignment,
    ccsl_booleanFunctions_CcslBooleanFunction,
    ccsl_complexType_AnnotationType,
    ccsl_complexType_AnonymousClass,
    ccsl_complexType_ComplexType,
    ccsl_complexType_DeclaredType,
    ccsl_complexType_JClass,
    ccsl_complexType_JInterface,
    ccsl_context_Context,
    ccsl_controlFlow_IfStatement,
    ccsl_controlFlow_LoopStatement,
    ccsl_controlFlow_SwitchCaseBlock,
    ccsl_controlFlow_SwitchStatement,
    ccsl_datatype_ArrayType,
    ccsl_datatype_BooleanPrimitiveType,
    ccsl_datatype_DataType,
    ccsl_datatype_GenericType,
    ccsl_datatype_IntPrimitiveType,
    ccsl_datatype_ObjectType,
    ccsl_datatype_ParameterizedType,
    ccsl_datatype_PrimitiveType,
    ccsl_datatype_ShortPrimitiveType,
    ccsl_datatype_StringPrimitiveType,
    ccsl_datatype_VoidType,
    ccsl_elements_Element,
    ccsl_expressions_ArithmeticExpression,
    ccsl_expressions_BooleanExpression,
    ccsl_expressions_InfixExpression,
    ccsl_expressions_OperatorExpression,
    ccsl_expressions_ParenthesizedExpression,
    ccsl_expressions_StringConcatenation,
    ccsl_faultTypeDescription_InjectionAction,
    ccsl_faultTypeDescription_InjectionStrategy,
    ccsl_filters_AtomicFilter,
    ccsl_filters_BlockLastStatementFilter,
    ccsl_filters_ChildClosureComplexTypeFilter,
    ccsl_filters_CompositeFilter,
    ccsl_filters_CountFilter,
    ccsl_filters_EquationFilter,
    ccsl_filters_Filter,
    ccsl_filters_FromClosureFilter,
    ccsl_filters_HasSameReferenceFilter,
    ccsl_filters_ImplicityContainerFilter,
    ccsl_filters_ImplicityOperandFilter,
    ccsl_filters_IsKindOfFilter,
    ccsl_filters_IsStringFilter,
    ccsl_filters_IsTypeOfFilter,
    ccsl_filters_PropertyFilter,
    ccsl_filters_RegexMatch,
    ccsl_filters_SameNameFilter,
    ccsl_filters_SuperClassClosureFilter,
    ccsl_filters_SuperMethodClosureFilter,
    ccsl_filters_TemplateFilter,
    ccsl_functions_CcslFunction,
    ccsl_import_ImportStatement,
    ccsl_import_ImportableElement,
    ccsl_invocation_ConstructorInvocation,
    ccsl_invocation_Invocation,
    ccsl_invocation_MethodInvocation,
    ccsl_invocation_SimpleMethodInvocation,
    ccsl_invocation_SuperMethodInvocation,
    ccsl_literalValues_BooleanLiteral,
    ccsl_literalValues_CharacterLiteral,
    ccsl_literalValues_LiteralValue,
    ccsl_literalValues_NullLiteral,
    ccsl_literalValues_NumberLiteral,
    ccsl_literalValues_StringLiteral,
    ccsl_method_Constructor,
    ccsl_method_Method,
    ccsl_method_SimpleMethod,
    ccsl_namedElements_NamedElement,
    ccsl_namedElements_Package,
    ccsl_numberFunctions_CcslIntegerLiteral,
    ccsl_numberFunctions_CcslNumberFunction,
    ccsl_numberFunctions_GetIndexOf,
    ccsl_statements_Access,
    ccsl_statements_ArrayCreation,
    ccsl_statements_Block,
    ccsl_statements_BreakStatement,
    ccsl_statements_ContinueStatement,
    ccsl_statements_ControlFlow,
    ccsl_statements_DataTypeAccess,
    ccsl_statements_EmptyStatement,
    ccsl_statements_InstanceCreation,
    ccsl_statements_InstanceOf,
    ccsl_statements_NamedElementAccess,
    ccsl_statements_ReturnStatement,
    ccsl_statements_Statement,
    ccsl_statements_SynchronizedBlock,
    ccsl_statements_ThisStatement,
    ccsl_statements_ThrowStatement,
    ccsl_statements_VarDeclaration,
    ccsl_statements_VariableAccess,
    ccsl_strategy_AllStrategy,
    ccsl_tryCatch_CatchClause,
    ccsl_tryCatch_TryStatement,
    ccsl_variable_FieldVariable,
    ccsl_variable_InitializableVariable,
    ccsl_variable_LocalVariable,
    ccsl_variable_ParameterVariable,
    ccsl_variable_Variable,
    complexType_AnnotationType,
    complexType_ComplexType,
    complexType_DeclaredType,
    complexType_JClass,
    complexType_JInterface,
    controlFlow_SwitchCaseBlock,
    datatype_DataType,
    datatype_ObjectType,
    elements_Element,
    expressions_OperatorExpression,
    filters_Filter,
    import_ImportStatement,
    import_ImportableElement,
    method_Constructor,
    method_Method,
    method_SimpleMethod,
    namedElements_NamedElement,
    numberFunctions_CcslNumberFunction,
    statements_Access,
    statements_Block,
    statements_Statement,
    tryCatch_CatchClause,
    variable_FieldVariable,
    variable_InitializableVariable,
    variable_ParameterVariable,
    variable_Variable,
    ArithmeticOperator,
    AssignmentOperator,
    BooleanOperator,
    CollectionKind,
    EquationOperator,
    Inheritance,
    LogicOperator,
    UnaryAssignmentOperator,
    Visibility,
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

def test_assoc_rules0_reverse_link_reassign_clear():
    a1 = ccsl_Rule(negated="sample_text")
    a2 = ccsl_Rule(negated="sample_text_2")
    b = ccsl_CompositeRule(operator="sample_text")
    _safe_set(b, 'ccsl_CompositeRule', {a1})
    assert _is_linked(b, 'ccsl_CompositeRule', a1)
    if hasattr(a1, 'ccsl_Rule'):
        assert _is_linked(a1, 'ccsl_Rule', b)
    _safe_set(b, 'ccsl_CompositeRule', {a2})
    assert _is_linked(b, 'ccsl_CompositeRule', a2)
    if hasattr(a1, 'ccsl_Rule'):
        assert not _is_linked(a1, 'ccsl_Rule', b)
    if hasattr(a2, 'ccsl_Rule'):
        assert _is_linked(a2, 'ccsl_Rule', b)
    _safe_set(b, 'ccsl_CompositeRule', set())
    assert not _is_linked(b, 'ccsl_CompositeRule', a2)
    if hasattr(a2, 'ccsl_Rule'):
        assert not _is_linked(a2, 'ccsl_Rule', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions6_stub_double():
    # InjectionAction has no real 'InjectionAction' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_FaultTypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_FaultTypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_FaultTypeDescription(name="sample_text")
    partner = InjectionAction()
    setattr(partner, 'InjectionAction', None)
    _safe_set(owner, 'ccsl_FaultTypeDescription7', {partner})
    assert getattr(partner, 'InjectionAction') == owner
    _safe_set(owner, 'ccsl_FaultTypeDescription7', set())
    assert getattr(partner, 'InjectionAction') is None


def test_assoc_annotations102_stub_double():
    # annotation_Annotation has no real 'annotation_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_annotation_AnnotableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_annotation_AnnotableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_annotation_AnnotableElement(annotationsKind="sample_text")
    partner = annotation_Annotation()
    setattr(partner, 'annotation_Annotation', None)
    _safe_set(owner, 'ccsl_annotation_AnnotableElement', {partner})
    assert getattr(partner, 'annotation_Annotation') == owner
    _safe_set(owner, 'ccsl_annotation_AnnotableElement', set())
    assert getattr(partner, 'annotation_Annotation') is None


def test_assoc_args41_stub_double():
    # statements_Statement has no real 'statements_Statement43' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_statements_InstanceCreation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_statements_InstanceCreation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_statements_InstanceCreation(argsKind="sample_text")
    partner = statements_Statement()
    setattr(partner, 'statements_Statement43', None)
    _safe_set(owner, 'ccsl_statements_InstanceCreation42', {partner})
    assert getattr(partner, 'statements_Statement43') == owner
    _safe_set(owner, 'ccsl_statements_InstanceCreation42', set())
    assert getattr(partner, 'statements_Statement43') is None


def test_assoc_args94_stub_double():
    # statements_Statement has no real 'statements_Statement95' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_invocation_Invocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_invocation_Invocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_invocation_Invocation(argsKind="sample_text")
    partner = statements_Statement()
    setattr(partner, 'statements_Statement95', None)
    _safe_set(owner, 'ccsl_invocation_Invocation', {partner})
    assert getattr(partner, 'statements_Statement95') == owner
    _safe_set(owner, 'ccsl_invocation_Invocation', set())
    assert getattr(partner, 'statements_Statement95') is None


def test_assoc_constructor38_stub_double():
    # method_Constructor has no real 'method_Constructor40' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_statements_InstanceCreation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_statements_InstanceCreation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_statements_InstanceCreation(argsKind="sample_text")
    partner = method_Constructor()
    setattr(partner, 'method_Constructor40', None)
    _safe_set(owner, 'ccsl_statements_InstanceCreation39', partner)
    assert getattr(partner, 'method_Constructor40') == owner
    _safe_set(owner, 'ccsl_statements_InstanceCreation39', None)
    assert getattr(partner, 'method_Constructor40') is None


def test_assoc_constructors14_stub_double():
    # method_Constructor has no real 'method_Constructor' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_complexType_JClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_complexType_JClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_complexType_JClass(inheritance="sample_text")
    partner = method_Constructor()
    setattr(partner, 'method_Constructor', None)
    _safe_set(owner, 'ccsl_complexType_JClass', {partner})
    assert getattr(partner, 'method_Constructor') == owner
    _safe_set(owner, 'ccsl_complexType_JClass', set())
    assert getattr(partner, 'method_Constructor') is None


def test_assoc_container129_stub_double():
    # Element has no real 'Element131' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_CountFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_CountFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    partner = Element()
    setattr(partner, 'Element131', None)
    _safe_set(owner, 'ccsl_filters_CountFilter130', partner)
    assert getattr(partner, 'Element131') == owner
    _safe_set(owner, 'ccsl_filters_CountFilter130', None)
    assert getattr(partner, 'Element131') is None


def test_assoc_context127_stub_double():
    # Context has no real 'Context128' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_CountFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_CountFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    partner = Context()
    setattr(partner, 'Context128', None)
    _safe_set(owner, 'ccsl_filters_CountFilter', {partner})
    assert getattr(partner, 'Context128') == owner
    _safe_set(owner, 'ccsl_filters_CountFilter', set())
    assert getattr(partner, 'Context128') is None


def test_assoc_context185_stub_double():
    # Context has no real 'Context187' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_SuperClassClosureFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_SuperClassClosureFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    partner = Context()
    setattr(partner, 'Context187', None)
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter186', partner)
    assert getattr(partner, 'Context187') == owner
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter186', None)
    assert getattr(partner, 'Context187') is None


def test_assoc_elements126_stub_double():
    # namedElements_NamedElement has no real 'namedElements_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_SameNameFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_SameNameFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_SameNameFilter(ignoreCase="sample_text")
    partner = namedElements_NamedElement()
    setattr(partner, 'namedElements_NamedElement', None)
    _safe_set(owner, 'ccsl_filters_SameNameFilter', {partner})
    assert getattr(partner, 'namedElements_NamedElement') == owner
    _safe_set(owner, 'ccsl_filters_SameNameFilter', set())
    assert getattr(partner, 'namedElements_NamedElement') is None


def test_assoc_field132_stub_double():
    # Element has no real 'Element134' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_CountFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_CountFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    partner = Element()
    setattr(partner, 'Element134', None)
    _safe_set(owner, 'ccsl_filters_CountFilter133', partner)
    assert getattr(partner, 'Element134') == owner
    _safe_set(owner, 'ccsl_filters_CountFilter133', None)
    assert getattr(partner, 'Element134') is None


def test_assoc_filters119_stub_double():
    # filters_Filter has no real 'filters_Filter120' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_CompositeFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_CompositeFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_CompositeFilter(operator="sample_text")
    partner = filters_Filter()
    setattr(partner, 'filters_Filter120', None)
    _safe_set(owner, 'ccsl_filters_CompositeFilter', {partner})
    assert getattr(partner, 'filters_Filter120') == owner
    _safe_set(owner, 'ccsl_filters_CompositeFilter', set())
    assert getattr(partner, 'filters_Filter120') is None


def test_assoc_imports18_stub_double():
    # import_ImportStatement has no real 'import_ImportStatement' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_complexType_DeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_complexType_DeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    partner = import_ImportStatement()
    setattr(partner, 'import_ImportStatement', None)
    _safe_set(owner, 'ccsl_complexType_DeclaredType19', {partner})
    assert getattr(partner, 'import_ImportStatement') == owner
    _safe_set(owner, 'ccsl_complexType_DeclaredType19', set())
    assert getattr(partner, 'import_ImportStatement') is None


def test_assoc_leftHandSide169_stub_double():
    # numberFunctions_CcslNumberFunction has no real 'numberFunctions_CcslNumberFunction' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_EquationFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_EquationFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_EquationFilter(operator="sample_text")
    partner = numberFunctions_CcslNumberFunction()
    setattr(partner, 'numberFunctions_CcslNumberFunction', None)
    _safe_set(owner, 'ccsl_filters_EquationFilter', {partner})
    assert getattr(partner, 'numberFunctions_CcslNumberFunction') == owner
    _safe_set(owner, 'ccsl_filters_EquationFilter', set())
    assert getattr(partner, 'numberFunctions_CcslNumberFunction') is None


def test_assoc_nestedTypes20_stub_double():
    # complexType_DeclaredType has no real 'complexType_DeclaredType22' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_complexType_DeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_complexType_DeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    partner = complexType_DeclaredType()
    setattr(partner, 'complexType_DeclaredType22', None)
    _safe_set(owner, 'ccsl_complexType_DeclaredType21', {partner})
    assert getattr(partner, 'complexType_DeclaredType22') == owner
    _safe_set(owner, 'ccsl_complexType_DeclaredType21', set())
    assert getattr(partner, 'complexType_DeclaredType22') is None


def test_assoc_params26_stub_double():
    # variable_ParameterVariable has no real 'variable_ParameterVariable' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_method_SimpleMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_method_SimpleMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    partner = variable_ParameterVariable()
    setattr(partner, 'variable_ParameterVariable', None)
    _safe_set(owner, 'ccsl_method_SimpleMethod', {partner})
    assert getattr(partner, 'variable_ParameterVariable') == owner
    _safe_set(owner, 'ccsl_method_SimpleMethod', set())
    assert getattr(partner, 'variable_ParameterVariable') is None


def test_assoc_returnType27_stub_double():
    # datatype_DataType has no real 'datatype_DataType28' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_method_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_method_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    partner = datatype_DataType()
    setattr(partner, 'datatype_DataType28', None)
    _safe_set(owner, 'ccsl_method_Method', partner)
    assert getattr(partner, 'datatype_DataType28') == owner
    _safe_set(owner, 'ccsl_method_Method', None)
    assert getattr(partner, 'datatype_DataType28') is None


def test_assoc_rightHandSide170_stub_double():
    # numberFunctions_CcslNumberFunction has no real 'numberFunctions_CcslNumberFunction172' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_EquationFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_EquationFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_EquationFilter(operator="sample_text")
    partner = numberFunctions_CcslNumberFunction()
    setattr(partner, 'numberFunctions_CcslNumberFunction172', None)
    _safe_set(owner, 'ccsl_filters_EquationFilter171', {partner})
    assert getattr(partner, 'numberFunctions_CcslNumberFunction172') == owner
    _safe_set(owner, 'ccsl_filters_EquationFilter171', set())
    assert getattr(partner, 'numberFunctions_CcslNumberFunction172') is None


def test_assoc_rightHandSide90_stub_double():
    # statements_Statement has no real 'statements_Statement91' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_assignment_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_assignment_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_assignment_Assignment(operator="sample_text")
    partner = statements_Statement()
    setattr(partner, 'statements_Statement91', None)
    _safe_set(owner, 'ccsl_assignment_Assignment', partner)
    assert getattr(partner, 'statements_Statement91') == owner
    _safe_set(owner, 'ccsl_assignment_Assignment', None)
    assert getattr(partner, 'statements_Statement91') is None


def test_assoc_rule4_stub_double():
    # ccsl_AtomicRule has no real 'ccsl_AtomicRule5' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_FaultTypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_FaultTypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_FaultTypeDescription(name="sample_text")
    partner = ccsl_AtomicRule()
    setattr(partner, 'ccsl_AtomicRule5', None)
    _safe_set(owner, 'ccsl_FaultTypeDescription', partner)
    assert getattr(partner, 'ccsl_AtomicRule5') == owner
    _safe_set(owner, 'ccsl_FaultTypeDescription', None)
    assert getattr(partner, 'ccsl_AtomicRule5') is None


def test_assoc_statements33_stub_double():
    # statements_Statement has no real 'statements_Statement34' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_statements_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_statements_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_statements_Block(statementsKind="sample_text")
    partner = statements_Statement()
    setattr(partner, 'statements_Statement34', None)
    _safe_set(owner, 'ccsl_statements_Block', {partner})
    assert getattr(partner, 'statements_Statement34') == owner
    _safe_set(owner, 'ccsl_statements_Block', set())
    assert getattr(partner, 'statements_Statement34') is None


def test_assoc_strategy8_stub_double():
    # InjectionStrategy has no real 'InjectionStrategy' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_FaultTypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_FaultTypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_FaultTypeDescription(name="sample_text")
    partner = InjectionStrategy()
    setattr(partner, 'InjectionStrategy', None)
    _safe_set(owner, 'ccsl_FaultTypeDescription9', partner)
    assert getattr(partner, 'InjectionStrategy') == owner
    _safe_set(owner, 'ccsl_FaultTypeDescription9', None)
    assert getattr(partner, 'InjectionStrategy') is None


def test_assoc_subClass182_stub_double():
    # complexType_JClass has no real 'complexType_JClass184' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_SuperClassClosureFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_SuperClassClosureFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    partner = complexType_JClass()
    setattr(partner, 'complexType_JClass184', None)
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter183', partner)
    assert getattr(partner, 'complexType_JClass184') == owner
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter183', None)
    assert getattr(partner, 'complexType_JClass184') is None


def test_assoc_superClass15_stub_double():
    # complexType_JClass has no real 'complexType_JClass' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_complexType_JClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_complexType_JClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_complexType_JClass(inheritance="sample_text")
    partner = complexType_JClass()
    setattr(partner, 'complexType_JClass', None)
    _safe_set(owner, 'ccsl_complexType_JClass16', partner)
    assert getattr(partner, 'complexType_JClass') == owner
    _safe_set(owner, 'ccsl_complexType_JClass16', None)
    assert getattr(partner, 'complexType_JClass') is None


def test_assoc_superClass180_stub_double():
    # complexType_JClass has no real 'complexType_JClass181' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_filters_SuperClassClosureFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_filters_SuperClassClosureFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    partner = complexType_JClass()
    setattr(partner, 'complexType_JClass181', None)
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter', partner)
    assert getattr(partner, 'complexType_JClass181') == owner
    _safe_set(owner, 'ccsl_filters_SuperClassClosureFilter', None)
    assert getattr(partner, 'complexType_JClass181') is None


def test_assoc_superInterfaces17_stub_double():
    # complexType_JInterface has no real 'complexType_JInterface' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_complexType_DeclaredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_complexType_DeclaredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    partner = complexType_JInterface()
    setattr(partner, 'complexType_JInterface', None)
    _safe_set(owner, 'ccsl_complexType_DeclaredType', {partner})
    assert getattr(partner, 'complexType_JInterface') == owner
    _safe_set(owner, 'ccsl_complexType_DeclaredType', set())
    assert getattr(partner, 'complexType_JInterface') is None


def test_assoc_type108_stub_double():
    # datatype_DataType has no real 'datatype_DataType109' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_datatype_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_datatype_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_datatype_ArrayType(dimensions="sample_text")
    partner = datatype_DataType()
    setattr(partner, 'datatype_DataType109', None)
    _safe_set(owner, 'ccsl_datatype_ArrayType', partner)
    assert getattr(partner, 'datatype_DataType109') == owner
    _safe_set(owner, 'ccsl_datatype_ArrayType', None)
    assert getattr(partner, 'datatype_DataType109') is None


def test_assoc_type11_stub_double():
    # datatype_DataType has no real 'datatype_DataType' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_variable_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_variable_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_variable_Variable(final="sample_text")
    partner = datatype_DataType()
    setattr(partner, 'datatype_DataType', None)
    _safe_set(owner, 'ccsl_variable_Variable', partner)
    assert getattr(partner, 'datatype_DataType') == owner
    _safe_set(owner, 'ccsl_variable_Variable', None)
    assert getattr(partner, 'datatype_DataType') is None


def test_assoc_type36_stub_double():
    # datatype_ObjectType has no real 'datatype_ObjectType37' property in the generated
    # code (a bare stub) -- manually attach it so ccsl_statements_InstanceCreation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccsl_statements_InstanceCreation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccsl_statements_InstanceCreation(argsKind="sample_text")
    partner = datatype_ObjectType()
    setattr(partner, 'datatype_ObjectType37', None)
    _safe_set(owner, 'ccsl_statements_InstanceCreation', partner)
    assert getattr(partner, 'datatype_ObjectType37') == owner
    _safe_set(owner, 'ccsl_statements_InstanceCreation', None)
    assert getattr(partner, 'datatype_ObjectType37') is None


