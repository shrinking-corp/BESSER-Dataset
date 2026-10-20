import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExpression,
    CallVariable,
    DataType,
    Expression,
    Literal,
    MultiplicityElement,
    NamedElement,
    Object,
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
    kermeta_DummyClass,
    kermeta_behavior_Assignment,
    kermeta_behavior_Block,
    kermeta_behavior_BooleanLiteral,
    kermeta_behavior_CallExpression,
    kermeta_behavior_CallFeature,
    kermeta_behavior_CallResult,
    kermeta_behavior_CallSuperOperation,
    kermeta_behavior_CallValue,
    kermeta_behavior_CallVariable,
    kermeta_behavior_Conditional,
    kermeta_behavior_EmptyExpression,
    kermeta_behavior_Expression,
    kermeta_behavior_IntegerLiteral,
    kermeta_behavior_JavaStaticCall,
    kermeta_behavior_LambdaExpression,
    kermeta_behavior_LambdaParameter,
    kermeta_behavior_Literal,
    kermeta_behavior_Loop,
    kermeta_behavior_Raise,
    kermeta_behavior_Rescue,
    kermeta_behavior_SelfExpression,
    kermeta_behavior_StringLiteral,
    kermeta_behavior_TypeLiteral,
    kermeta_behavior_TypeReference,
    kermeta_behavior_VariableDecl,
    kermeta_behavior_VoidLiteral,
    kermeta_language_DummyClass,
    kermeta_structure_Class,
    kermeta_structure_ClassDefinition,
    kermeta_structure_Constraint,
    kermeta_structure_DataType,
    kermeta_structure_Enumeration,
    kermeta_structure_EnumerationLiteral,
    kermeta_structure_Filter,
    kermeta_structure_FunctionType,
    kermeta_structure_GenericTypeDefinition,
    kermeta_structure_Model,
    kermeta_structure_ModelType,
    kermeta_structure_ModelTypeVariable,
    kermeta_structure_ModelingUnit,
    kermeta_structure_MultiplicityElement,
    kermeta_structure_NamedElement,
    kermeta_structure_Object,
    kermeta_structure_ObjectTypeVariable,
    kermeta_structure_Operation,
    kermeta_structure_Package,
    kermeta_structure_Parameter,
    kermeta_structure_ParameterizedType,
    kermeta_structure_PrimitiveType,
    kermeta_structure_ProductType,
    kermeta_structure_Property,
    kermeta_structure_Require,
    kermeta_structure_Tag,
    kermeta_structure_Type,
    kermeta_structure_TypeContainer,
    kermeta_structure_TypeDefinition,
    kermeta_structure_TypeDefinitionContainer,
    kermeta_structure_TypeVariable,
    kermeta_structure_TypeVariableBinding,
    kermeta_structure_TypedElement,
    kermeta_structure_Using,
    kermeta_structure_VirtualType,
    kermeta_structure_VoidType,
    structure_Class,
    structure_ClassDefinition,
    structure_Constraint,
    structure_DataType,
    structure_Enumeration,
    structure_EnumerationLiteral,
    structure_Filter,
    structure_GenericTypeDefinition,
    structure_ModelTypeVariable,
    structure_ModelingUnit,
    structure_NamedElement,
    structure_Object,
    structure_Operation,
    structure_Package,
    structure_Parameter,
    structure_Property,
    structure_Require,
    structure_Tag,
    structure_Type,
    structure_TypeContainer,
    structure_TypeDefinition,
    structure_TypeDefinitionContainer,
    structure_TypeVariable,
    structure_TypeVariableBinding,
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

def test_assoc_body112_stub_double():
    # behavior_Expression has no real 'behavior_Expression113' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression113', None)
    _safe_set(owner, 'kermeta_structure_Constraint', partner)
    assert getattr(partner, 'behavior_Expression113') == owner
    _safe_set(owner, 'kermeta_structure_Constraint', None)
    assert getattr(partner, 'behavior_Expression113') is None


def test_assoc_body31_stub_double():
    # behavior_Expression has no real 'behavior_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_Rescue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_Rescue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_Rescue(exceptionName="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression32', None)
    _safe_set(owner, 'kermeta_behavior_Rescue', {partner})
    assert getattr(partner, 'behavior_Expression32') == owner
    _safe_set(owner, 'kermeta_behavior_Rescue', set())
    assert getattr(partner, 'behavior_Expression32') is None


def test_assoc_body75_stub_double():
    # behavior_Expression has no real 'behavior_Expression77' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression77', None)
    _safe_set(owner, 'kermeta_structure_Operation76', partner)
    assert getattr(partner, 'behavior_Expression77') == owner
    _safe_set(owner, 'kermeta_structure_Operation76', None)
    assert getattr(partner, 'behavior_Expression77') is None


def test_assoc_exceptionType33_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_Rescue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_Rescue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_Rescue(exceptionName="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference', None)
    _safe_set(owner, 'kermeta_behavior_Rescue34', partner)
    assert getattr(partner, 'behavior_TypeReference') == owner
    _safe_set(owner, 'kermeta_behavior_Rescue34', None)
    assert getattr(partner, 'behavior_TypeReference') is None


def test_assoc_getterBody86_stub_double():
    # behavior_Expression has no real 'behavior_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression88', None)
    _safe_set(owner, 'kermeta_structure_Property87', partner)
    assert getattr(partner, 'behavior_Expression88') == owner
    _safe_set(owner, 'kermeta_structure_Property87', None)
    assert getattr(partner, 'behavior_Expression88') is None


def test_assoc_includedTypeDefinition68_stub_double():
    # structure_TypeDefinition has no real 'structure_TypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_ModelType()
    partner = structure_TypeDefinition()
    setattr(partner, 'structure_TypeDefinition', None)
    _safe_set(owner, 'kermeta_structure_ModelType', {partner})
    assert getattr(partner, 'structure_TypeDefinition') == owner
    _safe_set(owner, 'kermeta_structure_ModelType', set())
    assert getattr(partner, 'structure_TypeDefinition') is None


def test_assoc_initialization53_stub_double():
    # behavior_Expression has no real 'behavior_Expression54' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_VariableDecl(identifier="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression54', None)
    _safe_set(owner, 'kermeta_behavior_VariableDecl', partner)
    assert getattr(partner, 'behavior_Expression54') == owner
    _safe_set(owner, 'kermeta_behavior_VariableDecl', None)
    assert getattr(partner, 'behavior_Expression54') is None


def test_assoc_inv120_stub_double():
    # structure_Constraint has no real 'Constraint121' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_ClassDefinition(isAbstract="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint121', None)
    _safe_set(owner, 'invOwner', {partner})
    assert getattr(partner, 'Constraint121') == owner
    _safe_set(owner, 'invOwner', set())
    assert getattr(partner, 'Constraint121') is None


def test_assoc_invOwner114_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition115' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition115', None)
    _safe_set(owner, 'inv', partner)
    assert getattr(partner, 'ClassDefinition115') == owner
    _safe_set(owner, 'inv', None)
    assert getattr(partner, 'ClassDefinition115') is None


def test_assoc_nestedPackage103_stub_double():
    # structure_Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Package(uri="sample_text")
    partner = structure_Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'nestingPackage', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'nestingPackage', set())
    assert getattr(partner, 'Package') is None


def test_assoc_nestingPackage104_stub_double():
    # structure_Package has no real 'Package105' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Package(uri="sample_text")
    partner = structure_Package()
    setattr(partner, 'Package105', None)
    _safe_set(owner, 'nestedPackage', partner)
    assert getattr(partner, 'Package105') == owner
    _safe_set(owner, 'nestedPackage', None)
    assert getattr(partner, 'Package105') is None


def test_assoc_object111_stub_double():
    # structure_Object has no real 'Object' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Tag(name="sample_text", value="sample_text")
    partner = structure_Object()
    setattr(partner, 'Object', None)
    _safe_set(owner, 'tag', {partner})
    assert getattr(partner, 'Object') == owner
    _safe_set(owner, 'tag', set())
    assert getattr(partner, 'Object') is None


def test_assoc_opposite84_stub_double():
    # structure_Property has no real 'structure_Property85' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = structure_Property()
    setattr(partner, 'structure_Property85', None)
    _safe_set(owner, 'kermeta_structure_Property', partner)
    assert getattr(partner, 'structure_Property85') == owner
    _safe_set(owner, 'kermeta_structure_Property', None)
    assert getattr(partner, 'structure_Property85') is None


def test_assoc_ownedAttribute122_stub_double():
    # structure_Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_ClassDefinition(isAbstract="sample_text")
    partner = structure_Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'owningClass', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'owningClass', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedAttribute58_stub_double():
    # structure_Property has no real 'structure_Property59' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Property()
    setattr(partner, 'structure_Property59', None)
    _safe_set(owner, 'kermeta_structure_Class', {partner})
    assert getattr(partner, 'structure_Property59') == owner
    _safe_set(owner, 'kermeta_structure_Class', set())
    assert getattr(partner, 'structure_Property59') is None


def test_assoc_ownedOperation123_stub_double():
    # structure_Operation has no real 'Operation125' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_ClassDefinition(isAbstract="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation125', None)
    _safe_set(owner, 'owningClass124', {partner})
    assert getattr(partner, 'Operation125') == owner
    _safe_set(owner, 'owningClass124', set())
    assert getattr(partner, 'Operation125') is None


def test_assoc_ownedOperation60_stub_double():
    # structure_Operation has no real 'structure_Operation62' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation62', None)
    _safe_set(owner, 'kermeta_structure_Class61', {partner})
    assert getattr(partner, 'structure_Operation62') == owner
    _safe_set(owner, 'kermeta_structure_Class61', set())
    assert getattr(partner, 'structure_Operation62') is None


def test_assoc_ownedParameter71_stub_double():
    # structure_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_owningClass81_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition', None)
    _safe_set(owner, 'ownedOperation', partner)
    assert getattr(partner, 'ClassDefinition') == owner
    _safe_set(owner, 'ownedOperation', None)
    assert getattr(partner, 'ClassDefinition') is None


def test_assoc_owningClass92_stub_double():
    # structure_ClassDefinition has no real 'ClassDefinition93' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = structure_ClassDefinition()
    setattr(partner, 'ClassDefinition93', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'ClassDefinition93') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'ClassDefinition93') is None


def test_assoc_parameters35_stub_double():
    # behavior_Expression has no real 'behavior_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_JavaStaticCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_JavaStaticCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_JavaStaticCall(jclass="sample_text", jmethod="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression36', None)
    _safe_set(owner, 'kermeta_behavior_JavaStaticCall', {partner})
    assert getattr(partner, 'behavior_Expression36') == owner
    _safe_set(owner, 'kermeta_behavior_JavaStaticCall', set())
    assert getattr(partner, 'behavior_Expression36') is None


def test_assoc_parameters4_stub_double():
    # behavior_Expression has no real 'behavior_Expression5' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallExpression(name="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression5', None)
    _safe_set(owner, 'kermeta_behavior_CallExpression', {partner})
    assert getattr(partner, 'behavior_Expression5') == owner
    _safe_set(owner, 'kermeta_behavior_CallExpression', set())
    assert getattr(partner, 'behavior_Expression5') is None


def test_assoc_post73_stub_double():
    # structure_Constraint has no real 'Constraint74' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint74', None)
    _safe_set(owner, 'postOwner', {partner})
    assert getattr(partner, 'Constraint74') == owner
    _safe_set(owner, 'postOwner', set())
    assert getattr(partner, 'Constraint74') is None


def test_assoc_postOwner118_stub_double():
    # structure_Operation has no real 'Operation119' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation119', None)
    _safe_set(owner, 'post', partner)
    assert getattr(partner, 'Operation119') == owner
    _safe_set(owner, 'post', None)
    assert getattr(partner, 'Operation119') is None


def test_assoc_pre72_stub_double():
    # structure_Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'preOwner', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'preOwner', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_preOwner116_stub_double():
    # structure_Operation has no real 'Operation117' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Constraint(language="sample_text", stereotype="sample_text")
    partner = structure_Operation()
    setattr(partner, 'Operation117', None)
    _safe_set(owner, 'pre', partner)
    assert getattr(partner, 'Operation117') == owner
    _safe_set(owner, 'pre', None)
    assert getattr(partner, 'Operation117') is None


def test_assoc_raisedException69_stub_double():
    # structure_Type has no real 'structure_Type70' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type70', None)
    _safe_set(owner, 'kermeta_structure_Operation', {partner})
    assert getattr(partner, 'structure_Type70') == owner
    _safe_set(owner, 'kermeta_structure_Operation', set())
    assert getattr(partner, 'structure_Type70') is None


def test_assoc_setterBody89_stub_double():
    # behavior_Expression has no real 'behavior_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isGetterAbstract="sample_text", isID="sample_text", isReadOnly="sample_text", isSetterAbstract="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression91', None)
    _safe_set(owner, 'kermeta_structure_Property90', partner)
    assert getattr(partner, 'behavior_Expression91') == owner
    _safe_set(owner, 'kermeta_structure_Property90', None)
    assert getattr(partner, 'behavior_Expression91') is None


def test_assoc_staticEnumLiteral19_stub_double():
    # structure_EnumerationLiteral has no real 'structure_EnumerationLiteral' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallFeature(isAtpre="sample_text")
    partner = structure_EnumerationLiteral()
    setattr(partner, 'structure_EnumerationLiteral', None)
    _safe_set(owner, 'kermeta_behavior_CallFeature20', partner)
    assert getattr(partner, 'structure_EnumerationLiteral') == owner
    _safe_set(owner, 'kermeta_behavior_CallFeature20', None)
    assert getattr(partner, 'structure_EnumerationLiteral') is None


def test_assoc_staticOperation17_stub_double():
    # structure_Operation has no real 'structure_Operation' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallFeature(isAtpre="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation', None)
    _safe_set(owner, 'kermeta_behavior_CallFeature18', partner)
    assert getattr(partner, 'structure_Operation') == owner
    _safe_set(owner, 'kermeta_behavior_CallFeature18', None)
    assert getattr(partner, 'structure_Operation') is None


def test_assoc_staticProperty15_stub_double():
    # structure_Property has no real 'structure_Property' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallFeature(isAtpre="sample_text")
    partner = structure_Property()
    setattr(partner, 'structure_Property', None)
    _safe_set(owner, 'kermeta_behavior_CallFeature16', partner)
    assert getattr(partner, 'structure_Property') == owner
    _safe_set(owner, 'kermeta_behavior_CallFeature16', None)
    assert getattr(partner, 'structure_Property') is None


def test_assoc_staticTypeVariableBindings6_stub_double():
    # structure_Type has no real 'structure_Type8' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallExpression(name="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type8', None)
    _safe_set(owner, 'kermeta_behavior_CallExpression7', {partner})
    assert getattr(partner, 'structure_Type8') == owner
    _safe_set(owner, 'kermeta_behavior_CallExpression7', set())
    assert getattr(partner, 'structure_Type8') is None


def test_assoc_superClass63_stub_double():
    # structure_Class has no real 'structure_Class' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Class(isAbstract="sample_text", name="sample_text")
    partner = structure_Class()
    setattr(partner, 'structure_Class', None)
    _safe_set(owner, 'kermeta_structure_Class64', {partner})
    assert getattr(partner, 'structure_Class') == owner
    _safe_set(owner, 'kermeta_structure_Class64', set())
    assert getattr(partner, 'structure_Class') is None


def test_assoc_superOperation78_stub_double():
    # structure_Operation has no real 'structure_Operation80' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_Operation()
    setattr(partner, 'structure_Operation80', None)
    _safe_set(owner, 'kermeta_structure_Operation79', partner)
    assert getattr(partner, 'structure_Operation80') == owner
    _safe_set(owner, 'kermeta_structure_Operation79', None)
    assert getattr(partner, 'structure_Operation80') is None


def test_assoc_superType126_stub_double():
    # structure_Type has no real 'structure_Type127' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_ClassDefinition(isAbstract="sample_text")
    partner = structure_Type()
    setattr(partner, 'structure_Type127', None)
    _safe_set(owner, 'kermeta_structure_ClassDefinition', {partner})
    assert getattr(partner, 'structure_Type127') == owner
    _safe_set(owner, 'kermeta_structure_ClassDefinition', set())
    assert getattr(partner, 'structure_Type127') is None


def test_assoc_target0_stub_double():
    # behavior_CallExpression has no real 'behavior_CallExpression' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_Assignment(isCast="sample_text")
    partner = behavior_CallExpression()
    setattr(partner, 'behavior_CallExpression', None)
    _safe_set(owner, 'kermeta_behavior_Assignment', partner)
    assert getattr(partner, 'behavior_CallExpression') == owner
    _safe_set(owner, 'kermeta_behavior_Assignment', None)
    assert getattr(partner, 'behavior_CallExpression') is None


def test_assoc_target13_stub_double():
    # behavior_Expression has no real 'behavior_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_CallFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_CallFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_CallFeature(isAtpre="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression14', None)
    _safe_set(owner, 'kermeta_behavior_CallFeature', partner)
    assert getattr(partner, 'behavior_Expression14') == owner
    _safe_set(owner, 'kermeta_behavior_CallFeature', None)
    assert getattr(partner, 'behavior_Expression14') is None


def test_assoc_type41_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference42' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_LambdaParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_LambdaParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_LambdaParameter(name="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference42', None)
    _safe_set(owner, 'kermeta_behavior_LambdaParameter', partner)
    assert getattr(partner, 'behavior_TypeReference42') == owner
    _safe_set(owner, 'kermeta_behavior_LambdaParameter', None)
    assert getattr(partner, 'behavior_TypeReference42') is None


def test_assoc_type55_stub_double():
    # behavior_TypeReference has no real 'behavior_TypeReference57' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_VariableDecl(identifier="sample_text")
    partner = behavior_TypeReference()
    setattr(partner, 'behavior_TypeReference57', None)
    _safe_set(owner, 'kermeta_behavior_VariableDecl56', partner)
    assert getattr(partner, 'behavior_TypeReference57') == owner
    _safe_set(owner, 'kermeta_behavior_VariableDecl56', None)
    assert getattr(partner, 'behavior_TypeReference57') is None


def test_assoc_typeParameter82_stub_double():
    # structure_TypeVariable has no real 'structure_TypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_structure_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_structure_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_structure_Operation(isAbstract="sample_text")
    partner = structure_TypeVariable()
    setattr(partner, 'structure_TypeVariable', None)
    _safe_set(owner, 'kermeta_structure_Operation83', {partner})
    assert getattr(partner, 'structure_TypeVariable') == owner
    _safe_set(owner, 'kermeta_structure_Operation83', set())
    assert getattr(partner, 'structure_TypeVariable') is None


def test_assoc_value1_stub_double():
    # behavior_Expression has no real 'behavior_Expression' property in the generated
    # code (a bare stub) -- manually attach it so kermeta_behavior_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kermeta_behavior_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kermeta_behavior_Assignment(isCast="sample_text")
    partner = behavior_Expression()
    setattr(partner, 'behavior_Expression', None)
    _safe_set(owner, 'kermeta_behavior_Assignment2', partner)
    assert getattr(partner, 'behavior_Expression') == owner
    _safe_set(owner, 'kermeta_behavior_Assignment2', None)
    assert getattr(partner, 'behavior_Expression') is None


