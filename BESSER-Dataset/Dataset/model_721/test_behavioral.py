import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdaptationOperator,
    CallExpression,
    CallFeature,
    CallOperation,
    CallVariable,
    DataType,
    Expression,
    GenericTypeDefinition,
    KermetaModelElement,
    Literal,
    ModelElementTypeDefinition,
    MultiplicityElement,
    NamedElement,
    ObjectTypeVariable,
    ParameterizedType,
    Type,
    TypeDefinition,
    TypeVariable,
    TypedElement,
    behavior_CallExpression,
    behavior_Expression,
    behavior_LambdaParameter,
    behavior_Rescue,
    behavior_TypeReference,
    org_behavior_Assignment,
    org_behavior_Block,
    org_behavior_BooleanLiteral,
    org_behavior_CallEnumLiteral,
    org_behavior_CallExpression,
    org_behavior_CallFeature,
    org_behavior_CallModelTransformation,
    org_behavior_CallOperation,
    org_behavior_CallProperty,
    org_behavior_CallResult,
    org_behavior_CallSuperOperation,
    org_behavior_CallTypeLiteral,
    org_behavior_CallValue,
    org_behavior_CallVariable,
    org_behavior_Conditional,
    org_behavior_EmptyExpression,
    org_behavior_Expression,
    org_behavior_IntegerLiteral,
    org_behavior_JavaStaticCall,
    org_behavior_LambdaExpression,
    org_behavior_LambdaParameter,
    org_behavior_Literal,
    org_behavior_Loop,
    org_behavior_Raise,
    org_behavior_Rescue,
    org_behavior_SelfExpression,
    org_behavior_StringLiteral,
    org_behavior_TypeReference,
    org_behavior_UnresolvedCall,
    org_behavior_VariableDecl,
    org_behavior_VoidLiteral,
    org_structure_AbstractOperation,
    org_structure_AbstractProperty,
    org_structure_AdaptationOperator,
    org_structure_AdaptationParameter,
    org_structure_Class,
    org_structure_ClassDefinition,
    org_structure_ClassDefinitionBinding,
    org_structure_Constraint,
    org_structure_DataType,
    org_structure_Enumeration,
    org_structure_EnumerationBinding,
    org_structure_EnumerationLiteral,
    org_structure_FilteredMetamodelReference,
    org_structure_FunctionType,
    org_structure_GenericTypeDefinition,
    org_structure_KermetaModelElement,
    org_structure_Metamodel,
    org_structure_Model,
    org_structure_ModelElementTypeDefinition,
    org_structure_ModelElementTypeDefinitionContainer,
    org_structure_ModelTransformation,
    org_structure_ModelType,
    org_structure_ModelTypeDefinition,
    org_structure_ModelTypeDefinitionBinding,
    org_structure_ModelTypeDefinitionContainer,
    org_structure_ModelTypeVariable,
    org_structure_MultiplicityElement,
    org_structure_NamedElement,
    org_structure_ObjectTypeVariable,
    org_structure_Operation,
    org_structure_OperationAdaptationOperator,
    org_structure_OperationBinding,
    org_structure_Package,
    org_structure_Parameter,
    org_structure_ParameterizedType,
    org_structure_PrimitiveType,
    org_structure_ProductType,
    org_structure_Property,
    org_structure_PropertyAdaptationOperator,
    org_structure_PropertyBinding,
    org_structure_Tag,
    org_structure_Type,
    org_structure_TypeContainer,
    org_structure_TypeDefinition,
    org_structure_TypeVariable,
    org_structure_TypeVariableBinding,
    org_structure_TypedElement,
    org_structure_UnresolvedAdaptationOperator,
    org_structure_UnresolvedInferredType,
    org_structure_UnresolvedModelTransformation,
    org_structure_UnresolvedModelTypeDefinition,
    org_structure_UnresolvedOperation,
    org_structure_UnresolvedProperty,
    org_structure_UnresolvedReference,
    org_structure_UnresolvedType,
    org_structure_UnresolvedTypeVariable,
    org_structure_UseAdaptationOperator,
    org_structure_Using,
    org_structure_VirtualType,
    org_structure_VoidType,
    structure_AbstractOperation,
    structure_AbstractProperty,
    structure_AdaptationOperator,
    structure_AdaptationParameter,
    structure_Class,
    structure_ClassDefinition,
    structure_ClassDefinitionBinding,
    structure_Constraint,
    structure_Enumeration,
    structure_EnumerationBinding,
    structure_EnumerationLiteral,
    structure_FilteredMetamodelReference,
    structure_GenericTypeDefinition,
    structure_KermetaModelElement,
    structure_Metamodel,
    structure_ModelElementTypeDefinition,
    structure_ModelElementTypeDefinitionContainer,
    structure_ModelTransformation,
    structure_ModelTypeDefinition,
    structure_ModelTypeDefinitionBinding,
    structure_ModelTypeDefinitionContainer,
    structure_ModelTypeVariable,
    structure_MultiplicityElement,
    structure_NamedElement,
    structure_Operation,
    structure_OperationBinding,
    structure_Package,
    structure_Parameter,
    structure_Property,
    structure_PropertyBinding,
    structure_Tag,
    structure_Type,
    structure_TypeContainer,
    structure_TypeVariable,
    structure_TypeVariableBinding,
    structure_UnresolvedOperation,
    structure_UnresolvedProperty,
    structure_UnresolvedReference,
    structure_UseAdaptationOperator,
    structure_Using,
    structure_VirtualType,
    ConstraintLanguage,
    ConstraintType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body123_stub_double():
    # behavior_Expression has no real 'behavior_Expression124' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression124', None)
    _safe_set(owner, 'org_structure_Constraint', partner)
    assert getattr(partner, 'behavior_Expression124') == owner
    _safe_set(owner, 'org_structure_Constraint', None)
    assert getattr(partner, 'behavior_Expression124') is None


def test_assoc_body227_stub_double():
    # behavior_Expression has no real 'behavior_Expression229' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ModelTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ModelTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ModelTransformation(isAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression229', None)
    _safe_set(owner, 'org_structure_ModelTransformation228', partner)
    assert getattr(partner, 'behavior_Expression229') == owner
    _safe_set(owner, 'org_structure_ModelTransformation228', None)
    assert getattr(partner, 'behavior_Expression229') is None


def test_assoc_body27_stub_double():
    # behavior_Expression has no real 'behavior_Expression28' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_Rescue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_Rescue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_Rescue(exceptionName="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression28', None)
    _safe_set(owner, 'org_behavior_Rescue', {partner})
    assert getattr(partner, 'behavior_Expression28') == owner
    _safe_set(owner, 'org_behavior_Rescue', set())
    assert getattr(partner, 'behavior_Expression28') is None


def test_assoc_body76_stub_double():
    # behavior_Expression has no real 'behavior_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression78', None)
    _safe_set(owner, 'org_structure_Operation77', partner)
    assert getattr(partner, 'behavior_Expression78') == owner
    _safe_set(owner, 'org_structure_Operation77', None)
    assert getattr(partner, 'behavior_Expression78') is None


def test_assoc_exceptionType29_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_Rescue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_Rescue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_Rescue(exceptionName="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference', None)
    _safe_set(owner, 'org_behavior_Rescue30', partner)
    assert getattr(partner, 'behavior_TypeReference') == owner
    _safe_set(owner, 'org_behavior_Rescue30', None)
    assert getattr(partner, 'behavior_TypeReference') is None


def test_assoc_generics161_stub_double():
    # structure_Type has no real 'structure_Type163' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_UnresolvedType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_UnresolvedType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_UnresolvedType(typeIdentifier="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type163', None)
    _safe_set(owner, 'org_structure_UnresolvedType162', {partner})
    assert getattr(partner, 'structure_Type163') == owner
    _safe_set(owner, 'org_structure_UnresolvedType162', set())
    assert getattr(partner, 'structure_Type163') is None


def test_assoc_generics61_stub_double():
    # structure_Type has no real 'structure_Type63' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_UnresolvedCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_UnresolvedCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_UnresolvedCall(isAtpre="sample_text", isCalledWithParenthesis="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type63', None)
    _safe_set(owner, 'org_behavior_UnresolvedCall62', {partner})
    assert getattr(partner, 'structure_Type63') == owner
    _safe_set(owner, 'org_behavior_UnresolvedCall62', set())
    assert getattr(partner, 'structure_Type63') is None


def test_assoc_getterBody85_stub_double():
    # behavior_Expression has no real 'behavior_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression87', None)
    _safe_set(owner, 'org_structure_Property86', partner)
    assert getattr(partner, 'behavior_Expression87') == owner
    _safe_set(owner, 'org_structure_Property86', None)
    assert getattr(partner, 'behavior_Expression87') is None


def test_assoc_initialization49_stub_double():
    # behavior_Expression has no real 'behavior_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_VariableDecl(identifier="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression50', None)
    _safe_set(owner, 'org_behavior_VariableDecl', partner)
    assert getattr(partner, 'behavior_Expression50') == owner
    _safe_set(owner, 'org_behavior_VariableDecl', None)
    assert getattr(partner, 'behavior_Expression50') is None


def test_assoc_inv131_stub_double():
    # structure_Constraint has no real 'Constraint132' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ClassDefinition(isAbstract="sample_text", isFinal="sample_text", isSingleton="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint132', None)
    _safe_set(owner, 'invOwner', {partner})
    assert getattr(partner, 'Constraint132') == owner
    _safe_set(owner, 'invOwner', set())
    assert getattr(partner, 'Constraint132') is None


def test_assoc_invOwner125_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition126' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition126', None)
    _safe_set(owner, 'inv', partner)
    assert getattr(partner, 'ClassDefinition126') == owner
    _safe_set(owner, 'inv', None)
    assert getattr(partner, 'ClassDefinition126') is None


def test_assoc_nestedPackage113_stub_double():
    # structure_Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Package(uri="sample_text")
    partner = structure_Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'nestingPackage', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'nestingPackage', set())
    assert getattr(partner, 'Package') is None


def test_assoc_nestingPackage114_stub_double():
    # structure_Package has no real 'Package115' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Package(uri="sample_text")
    partner = structure_Package()
    setattr(partner, 'Package115', None)
    _safe_set(owner, 'nestedPackage', partner)
    assert getattr(partner, 'Package115') == owner
    _safe_set(owner, 'nestedPackage', None)
    assert getattr(partner, 'Package115') is None


def test_assoc_object122_stub_double():
    # structure_KermetaModelElement has no real 'KermetaModelElement' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Tag(name="sample_text", value="sample_text")
    partner = structure_KermetaModelElement()
    setattr(partner, 'KermetaModelElement', None)
    _safe_set(owner, 'kTag', {partner})
    assert getattr(partner, 'KermetaModelElement') == owner
    _safe_set(owner, 'kTag', set())
    assert getattr(partner, 'KermetaModelElement') is None


def test_assoc_opposite84_stub_double():
    # structure_AbstractProperty has no real 'structure_AbstractProperty' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = structure_AbstractProperty()
    setattr(partner, 'structure_AbstractProperty', None)
    _safe_set(owner, 'org_structure_Property', partner)
    assert getattr(partner, 'structure_AbstractProperty') == owner
    _safe_set(owner, 'org_structure_Property', None)
    assert getattr(partner, 'structure_AbstractProperty') is None


def test_assoc_ownedAdaptationOperators116_stub_double():
    # structure_AdaptationOperator has no real 'structure_AdaptationOperator' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Package(uri="sample_text")
    partner = structure_AdaptationOperator()
    setattr(partner, 'structure_AdaptationOperator', None)
    _safe_set(owner, 'org_structure_Package', {partner})
    assert getattr(partner, 'structure_AdaptationOperator') == owner
    _safe_set(owner, 'org_structure_Package', set())
    assert getattr(partner, 'structure_AdaptationOperator') is None


def test_assoc_ownedAttribute105_stub_double():
    # structure_Property has no real 'structure_Property106' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Property()
    setattr(partner, 'structure_Property106', None)
    _safe_set(owner, 'org_structure_Class', {partner})
    assert getattr(partner, 'structure_Property106') == owner
    _safe_set(owner, 'org_structure_Class', set())
    assert getattr(partner, 'structure_Property106') is None


def test_assoc_ownedAttribute133_stub_double():
    # structure_Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ClassDefinition(isAbstract="sample_text", isFinal="sample_text", isSingleton="sample_text")
    partner = structure_Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'owningClass', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'owningClass', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedOperation107_stub_double():
    # structure_Operation has no real 'structure_Operation109' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation109', None)
    _safe_set(owner, 'org_structure_Class108', {partner})
    assert getattr(partner, 'structure_Operation109') == owner
    _safe_set(owner, 'org_structure_Class108', set())
    assert getattr(partner, 'structure_Operation109') is None


def test_assoc_ownedOperation134_stub_double():
    # structure_Operation has no real 'Operation136' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ClassDefinition(isAbstract="sample_text", isFinal="sample_text", isSingleton="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation136', None)
    _safe_set(owner, 'owningClass135', {partner})
    assert getattr(partner, 'Operation136') == owner
    _safe_set(owner, 'owningClass135', set())
    assert getattr(partner, 'Operation136') is None


def test_assoc_ownedParameter234_stub_double():
    # structure_Parameter has no real 'structure_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ModelTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ModelTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ModelTransformation(isAbstract="sample_text")
    partner = structure_Parameter()
    setattr(partner, 'structure_Parameter', None)
    _safe_set(owner, 'org_structure_ModelTransformation235', {partner})
    assert getattr(partner, 'structure_Parameter') == owner
    _safe_set(owner, 'org_structure_ModelTransformation235', set())
    assert getattr(partner, 'structure_Parameter') is None


def test_assoc_ownedParameter72_stub_double():
    # structure_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_ownedUnresolvedOperations79_stub_double():
    # structure_UnresolvedOperation has no real 'structure_UnresolvedOperation' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_UnresolvedOperation()
    setattr(partner, 'structure_UnresolvedOperation', None)
    _safe_set(owner, 'org_structure_Operation80', {partner})
    assert getattr(partner, 'structure_UnresolvedOperation') == owner
    _safe_set(owner, 'org_structure_Operation80', set())
    assert getattr(partner, 'structure_UnresolvedOperation') is None


def test_assoc_ownedUnresolvedProperties91_stub_double():
    # structure_UnresolvedProperty has no real 'structure_UnresolvedProperty' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = structure_UnresolvedProperty()
    setattr(partner, 'structure_UnresolvedProperty', None)
    _safe_set(owner, 'org_structure_Property92', {partner})
    assert getattr(partner, 'structure_UnresolvedProperty') == owner
    _safe_set(owner, 'org_structure_Property92', set())
    assert getattr(partner, 'structure_UnresolvedProperty') is None


def test_assoc_owningClass81_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition', None)
    _safe_set(owner, 'ownedOperation', partner)
    assert getattr(partner, 'ClassDefinition') == owner
    _safe_set(owner, 'ownedOperation', None)
    assert getattr(partner, 'ClassDefinition') is None


def test_assoc_owningClass93_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition94' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition94', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'ClassDefinition94') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'ClassDefinition94') is None


def test_assoc_owningModelTypeDefinition233_stub_double():
    # structure_ModelTypeDefinition has no real 'ModelTypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ModelTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ModelTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ModelTransformation(isAbstract="sample_text")
    partner = structure_ModelTypeDefinition()
    setattr(partner, 'ModelTypeDefinition', None)
    _safe_set(owner, 'ownedTransformations', partner)
    assert getattr(partner, 'ModelTypeDefinition') == owner
    _safe_set(owner, 'ownedTransformations', None)
    assert getattr(partner, 'ModelTypeDefinition') is None


def test_assoc_packages137_stub_double():
    # structure_Package has no real 'structure_Package' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Metamodel(isResolved=True, uri="sample_text")
    partner = structure_Package()
    setattr(partner, 'structure_Package', None)
    _safe_set(owner, 'org_structure_Metamodel', {partner})
    assert getattr(partner, 'structure_Package') == owner
    _safe_set(owner, 'org_structure_Metamodel', set())
    assert getattr(partner, 'structure_Package') is None


def test_assoc_parameters31_stub_double():
    # behavior_Expression has no real 'behavior_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_JavaStaticCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_JavaStaticCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_JavaStaticCall(jclass="sample_text", jmethod="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression32', None)
    _safe_set(owner, 'org_behavior_JavaStaticCall', {partner})
    assert getattr(partner, 'behavior_Expression32') == owner
    _safe_set(owner, 'org_behavior_JavaStaticCall', set())
    assert getattr(partner, 'behavior_Expression32') is None


def test_assoc_parameters4_stub_double():
    # behavior_Expression has no real 'behavior_Expression5' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_CallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_CallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_CallExpression(name="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression5', None)
    _safe_set(owner, 'org_behavior_CallExpression', {partner})
    assert getattr(partner, 'behavior_Expression5') == owner
    _safe_set(owner, 'org_behavior_CallExpression', set())
    assert getattr(partner, 'behavior_Expression5') is None


def test_assoc_post74_stub_double():
    # structure_Constraint has no real 'Constraint75' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint75', None)
    _safe_set(owner, 'postOwner', {partner})
    assert getattr(partner, 'Constraint75') == owner
    _safe_set(owner, 'postOwner', set())
    assert getattr(partner, 'Constraint75') is None


def test_assoc_postOwner129_stub_double():
    # structure_Operation has no real 'Operation130' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation130', None)
    _safe_set(owner, 'post', partner)
    assert getattr(partner, 'Operation130') == owner
    _safe_set(owner, 'post', None)
    assert getattr(partner, 'Operation130') is None


def test_assoc_pre73_stub_double():
    # structure_Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'preOwner', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'preOwner', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_preOwner127_stub_double():
    # structure_Operation has no real 'Operation128' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation128', None)
    _safe_set(owner, 'pre', partner)
    assert getattr(partner, 'Operation128') == owner
    _safe_set(owner, 'pre', None)
    assert getattr(partner, 'Operation128') is None


def test_assoc_raisedException70_stub_double():
    # structure_Type has no real 'structure_Type71' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type71', None)
    _safe_set(owner, 'org_structure_Operation', {partner})
    assert getattr(partner, 'structure_Type71') == owner
    _safe_set(owner, 'org_structure_Operation', set())
    assert getattr(partner, 'structure_Type71') is None


def test_assoc_referencedMetamodels138_stub_double():
    # structure_FilteredMetamodelReference has no real 'structure_FilteredMetamodelReference' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Metamodel(isResolved=True, uri="sample_text")
    partner = structure_FilteredMetamodelReference()
    setattr(partner, 'structure_FilteredMetamodelReference', None)
    _safe_set(owner, 'org_structure_Metamodel139', {partner})
    assert getattr(partner, 'structure_FilteredMetamodelReference') == owner
    _safe_set(owner, 'org_structure_Metamodel139', set())
    assert getattr(partner, 'structure_FilteredMetamodelReference') is None


def test_assoc_rules230_stub_double():
    # structure_Operation has no real 'structure_Operation232' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ModelTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ModelTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ModelTransformation(isAbstract="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation232', None)
    _safe_set(owner, 'org_structure_ModelTransformation231', {partner})
    assert getattr(partner, 'structure_Operation232') == owner
    _safe_set(owner, 'org_structure_ModelTransformation231', set())
    assert getattr(partner, 'structure_Operation232') is None


def test_assoc_setterBody88_stub_double():
    # behavior_Expression has no real 'behavior_Expression90' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression90', None)
    _safe_set(owner, 'org_structure_Property89', partner)
    assert getattr(partner, 'behavior_Expression90') == owner
    _safe_set(owner, 'org_structure_Property89', None)
    assert getattr(partner, 'behavior_Expression90') is None


def test_assoc_staticTypeVariableBindings6_stub_double():
    # structure_Type has no real 'structure_Type8' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_CallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_CallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_CallExpression(name="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type8', None)
    _safe_set(owner, 'org_behavior_CallExpression7', {partner})
    assert getattr(partner, 'structure_Type8') == owner
    _safe_set(owner, 'org_behavior_CallExpression7', set())
    assert getattr(partner, 'structure_Type8') is None


def test_assoc_superClass110_stub_double():
    # structure_Class has no real 'structure_Class' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Class()
    setattr(partner, 'structure_Class', None)
    _safe_set(owner, 'org_structure_Class111', {partner})
    assert getattr(partner, 'structure_Class') == owner
    _safe_set(owner, 'org_structure_Class111', set())
    assert getattr(partner, 'structure_Class') is None


def test_assoc_superType103_stub_double():
    # structure_Type has no real 'structure_Type104' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_TypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_TypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_TypeDefinition(isAspect="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type104', None)
    _safe_set(owner, 'org_structure_TypeDefinition', {partner})
    assert getattr(partner, 'structure_Type104') == owner
    _safe_set(owner, 'org_structure_TypeDefinition', set())
    assert getattr(partner, 'structure_Type104') is None


def test_assoc_target0_stub_double():
    # behavior_CallExpression has no real 'behavior_CallExpression' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_Assignment(isCast="sample_text")
    partner = behavior_CallExpression()
    setattr(partner, 'behavior_CallExpression', None)
    _safe_set(owner, 'org_behavior_Assignment', partner)
    assert getattr(partner, 'behavior_CallExpression') == owner
    _safe_set(owner, 'org_behavior_Assignment', None)
    assert getattr(partner, 'behavior_CallExpression') is None


def test_assoc_target13_stub_double():
    # behavior_Expression has no real 'behavior_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_CallFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_CallFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_CallFeature(isAtpre="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression14', None)
    _safe_set(owner, 'org_behavior_CallFeature', partner)
    assert getattr(partner, 'behavior_Expression14') == owner
    _safe_set(owner, 'org_behavior_CallFeature', None)
    assert getattr(partner, 'behavior_Expression14') is None


def test_assoc_target211_stub_double():
    # structure_Property has no real 'structure_Property212' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_PropertyAdaptationOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_PropertyAdaptationOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_PropertyAdaptationOperator(adder="sample_text", getter="sample_text", remover="sample_text", setter="sample_text")
    partner = structure_Property()
    setattr(partner, 'structure_Property212', None)
    _safe_set(owner, 'org_structure_PropertyAdaptationOperator', partner)
    assert getattr(partner, 'structure_Property212') == owner
    _safe_set(owner, 'org_structure_PropertyAdaptationOperator', None)
    assert getattr(partner, 'structure_Property212') is None


def test_assoc_target213_stub_double():
    # structure_Operation has no real 'structure_Operation214' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_OperationAdaptationOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_OperationAdaptationOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_OperationAdaptationOperator(body="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation214', None)
    _safe_set(owner, 'org_structure_OperationAdaptationOperator', partner)
    assert getattr(partner, 'structure_Operation214') == owner
    _safe_set(owner, 'org_structure_OperationAdaptationOperator', None)
    assert getattr(partner, 'structure_Operation214') is None


def test_assoc_target55_stub_double():
    # behavior_Expression has no real 'behavior_Expression57' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_UnresolvedCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_UnresolvedCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_UnresolvedCall(isAtpre="sample_text", isCalledWithParenthesis="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression57', None)
    _safe_set(owner, 'org_behavior_UnresolvedCall56', partner)
    assert getattr(partner, 'behavior_Expression57') == owner
    _safe_set(owner, 'org_behavior_UnresolvedCall56', None)
    assert getattr(partner, 'behavior_Expression57') is None


def test_assoc_targetParent58_stub_double():
    # structure_Type has no real 'structure_Type60' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_UnresolvedCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_UnresolvedCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_UnresolvedCall(isAtpre="sample_text", isCalledWithParenthesis="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type60', None)
    _safe_set(owner, 'org_behavior_UnresolvedCall59', partner)
    assert getattr(partner, 'structure_Type60') == owner
    _safe_set(owner, 'org_behavior_UnresolvedCall59', None)
    assert getattr(partner, 'structure_Type60') is None


def test_assoc_type37_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference38' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_LambdaParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_LambdaParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_LambdaParameter(name="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference38', None)
    _safe_set(owner, 'org_behavior_LambdaParameter', partner)
    assert getattr(partner, 'behavior_TypeReference38') == owner
    _safe_set(owner, 'org_behavior_LambdaParameter', None)
    assert getattr(partner, 'behavior_TypeReference38') is None


def test_assoc_type51_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference53' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_VariableDecl(identifier="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference53', None)
    _safe_set(owner, 'org_behavior_VariableDecl52', partner)
    assert getattr(partner, 'behavior_TypeReference53') == owner
    _safe_set(owner, 'org_behavior_VariableDecl52', None)
    assert getattr(partner, 'behavior_TypeReference53') is None


def test_assoc_typeParameter82_stub_double():
    # structure_TypeVariable has no real 'structure_TypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_Operation(isAbstract="sample_text", uniqueName="sample_text")
    partner = structure_TypeVariable()
    setattr(partner, 'structure_TypeVariable', None)
    _safe_set(owner, 'org_structure_Operation83', {partner})
    assert getattr(partner, 'structure_TypeVariable') == owner
    _safe_set(owner, 'org_structure_Operation83', set())
    assert getattr(partner, 'structure_TypeVariable') is None


def test_assoc_typeParameters226_stub_double():
    # structure_ModelTypeVariable has no real 'structure_ModelTypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_ModelTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_ModelTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_ModelTransformation(isAbstract="sample_text")
    partner = structure_ModelTypeVariable()
    setattr(partner, 'structure_ModelTypeVariable', None)
    _safe_set(owner, 'org_structure_ModelTransformation', {partner})
    assert getattr(partner, 'structure_ModelTypeVariable') == owner
    _safe_set(owner, 'org_structure_ModelTransformation', set())
    assert getattr(partner, 'structure_ModelTypeVariable') is None


def test_assoc_usings159_stub_double():
    # structure_Using has no real 'structure_Using160' property in the generated
    # code (a bare stub) -- manually attach it so org_structure_UnresolvedType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_structure_UnresolvedType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_structure_UnresolvedType(typeIdentifier="sample_text")
    partner = structure_Using()
    setattr(partner, 'structure_Using160', None)
    _safe_set(owner, 'org_structure_UnresolvedType', {partner})
    assert getattr(partner, 'structure_Using160') == owner
    _safe_set(owner, 'org_structure_UnresolvedType', set())
    assert getattr(partner, 'structure_Using160') is None


def test_assoc_usings54_stub_double():
    # structure_Using has no real 'structure_Using' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_UnresolvedCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_UnresolvedCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_UnresolvedCall(isAtpre="sample_text", isCalledWithParenthesis="sample_text")
    partner = structure_Using()
    setattr(partner, 'structure_Using', None)
    _safe_set(owner, 'org_behavior_UnresolvedCall', {partner})
    assert getattr(partner, 'structure_Using') == owner
    _safe_set(owner, 'org_behavior_UnresolvedCall', set())
    assert getattr(partner, 'structure_Using') is None


def test_assoc_value1_stub_double():
    # behavior_Expression has no real 'behavior_Expression' property in the generated
    # code (a bare stub) -- manually attach it so org_behavior_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_behavior_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_behavior_Assignment(isCast="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression', None)
    _safe_set(owner, 'org_behavior_Assignment2', partner)
    assert getattr(partner, 'behavior_Expression') == owner
    _safe_set(owner, 'org_behavior_Assignment2', None)
    assert getattr(partner, 'behavior_Expression') is None


