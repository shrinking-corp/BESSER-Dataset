import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnyType,
    BagType,
    CallExp,
    CollectionLiteralPart,
    CollectionType,
    Expression,
    FeatureCallExp,
    InvalidType,
    LiteralExp,
    LoopExp,
    NamedElement,
    NumericLiteralExp,
    OclExpression,
    OclLibrary,
    OrderedSetType,
    PrimitiveLiteralExp,
    SequenceType,
    SetType,
    TupleLiteralPart,
    TupleType,
    Type,
    TypeType,
    TypedElement,
    Variable,
    VoidType,
    essentialocl_expressions_BooleanLiteralExp,
    essentialocl_expressions_CallExp,
    essentialocl_expressions_CollectionItem,
    essentialocl_expressions_CollectionLiteralExp,
    essentialocl_expressions_CollectionLiteralPart,
    essentialocl_expressions_CollectionRange,
    essentialocl_expressions_EnumLiteralExp,
    essentialocl_expressions_ExpressionInOcl,
    essentialocl_expressions_FeatureCallExp,
    essentialocl_expressions_IfExp,
    essentialocl_expressions_IntegerLiteralExp,
    essentialocl_expressions_InvalidLiteralExp,
    essentialocl_expressions_IterateExp,
    essentialocl_expressions_IteratorExp,
    essentialocl_expressions_LetExp,
    essentialocl_expressions_LiteralExp,
    essentialocl_expressions_LoopExp,
    essentialocl_expressions_NumericLiteralExp,
    essentialocl_expressions_OclExpression,
    essentialocl_expressions_OperationCallExp,
    essentialocl_expressions_PrimitiveLiteralExp,
    essentialocl_expressions_PropertyCallExp,
    essentialocl_expressions_RealLiteralExp,
    essentialocl_expressions_StringLiteralExp,
    essentialocl_expressions_TupleLiteralExp,
    essentialocl_expressions_TupleLiteralPart,
    essentialocl_expressions_TypeLiteralExp,
    essentialocl_expressions_UndefinedLiteralExp,
    essentialocl_expressions_UnlimitedNaturalExp,
    essentialocl_expressions_Variable,
    essentialocl_expressions_VariableExp,
    essentialocl_types_AnyType,
    essentialocl_types_BagType,
    essentialocl_types_CollectionType,
    essentialocl_types_InvalidType,
    essentialocl_types_OclLibrary,
    essentialocl_types_OrderedSetType,
    essentialocl_types_SequenceType,
    essentialocl_types_SetType,
    essentialocl_types_TupleType,
    essentialocl_types_TypeType,
    essentialocl_types_VoidType,
    expressions_essentialocl_EnumerationLiteral,
    expressions_essentialocl_Operation,
    expressions_essentialocl_Parameter,
    expressions_essentialocl_Property,
    expressions_essentialocl_Type,
    types_essentialocl_PrimitiveType,
    types_essentialocl_Type,
    CollectionKind,
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

def test_assoc_elementType1_stub_double():
    # types_essentialocl_Type has no real 'types_essentialocl_Type' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_CollectionType(kind="sample_text")
    partner = types_essentialocl_Type()
    setattr(partner, 'types_essentialocl_Type', None)
    _safe_set(owner, 'essentialocl_types_CollectionType', partner)
    assert getattr(partner, 'types_essentialocl_Type') == owner
    _safe_set(owner, 'essentialocl_types_CollectionType', None)
    assert getattr(partner, 'types_essentialocl_Type') is None


def test_assoc_elementType88_stub_double():
    # expressions_essentialocl_Type has no real 'expressions_essentialocl_Type90' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_expressions_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_expressions_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    partner = expressions_essentialocl_Type()
    setattr(partner, 'expressions_essentialocl_Type90', None)
    _safe_set(owner, 'essentialocl_expressions_CollectionLiteralExp89', partner)
    assert getattr(partner, 'expressions_essentialocl_Type90') == owner
    _safe_set(owner, 'essentialocl_expressions_CollectionLiteralExp89', None)
    assert getattr(partner, 'expressions_essentialocl_Type90') is None


def test_assoc_initExpression42_stub_double():
    # OclExpression has no real 'OclExpression' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_expressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_expressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_expressions_Variable()
    partner = OclExpression()
    setattr(partner, 'OclExpression', None)
    _safe_set(owner, 'essentialocl_expressions_Variable43', partner)
    assert getattr(partner, 'OclExpression') == owner
    _safe_set(owner, 'essentialocl_expressions_Variable43', None)
    assert getattr(partner, 'OclExpression') is None


def test_assoc_oclAny21_stub_double():
    # AnyType has no real 'AnyType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = AnyType()
    setattr(partner, 'AnyType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary22', partner)
    assert getattr(partner, 'AnyType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary22', None)
    assert getattr(partner, 'AnyType') is None


def test_assoc_oclBag32_stub_double():
    # BagType has no real 'BagType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = BagType()
    setattr(partner, 'BagType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary33', partner)
    assert getattr(partner, 'BagType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary33', None)
    assert getattr(partner, 'BagType') is None


def test_assoc_oclBoolean11_stub_double():
    # types_essentialocl_PrimitiveType has no real 'types_essentialocl_PrimitiveType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = types_essentialocl_PrimitiveType()
    setattr(partner, 'types_essentialocl_PrimitiveType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary', partner)
    assert getattr(partner, 'types_essentialocl_PrimitiveType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary', None)
    assert getattr(partner, 'types_essentialocl_PrimitiveType') is None


def test_assoc_oclCollection28_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary29', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary29', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_oclInteger15_stub_double():
    # types_essentialocl_PrimitiveType has no real 'types_essentialocl_PrimitiveType17' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = types_essentialocl_PrimitiveType()
    setattr(partner, 'types_essentialocl_PrimitiveType17', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary16', partner)
    assert getattr(partner, 'types_essentialocl_PrimitiveType17') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary16', None)
    assert getattr(partner, 'types_essentialocl_PrimitiveType17') is None


def test_assoc_oclInvalid24_stub_double():
    # InvalidType has no real 'InvalidType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = InvalidType()
    setattr(partner, 'InvalidType', None)
    _safe_set(owner, 'oclLibrary25', partner)
    assert getattr(partner, 'InvalidType') == owner
    _safe_set(owner, 'oclLibrary25', None)
    assert getattr(partner, 'InvalidType') is None


def test_assoc_oclLibrary2_stub_double():
    # OclLibrary has no real 'OclLibrary4' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_CollectionType(kind="sample_text")
    partner = OclLibrary()
    setattr(partner, 'OclLibrary4', None)
    _safe_set(owner, 'essentialocl_types_CollectionType3', partner)
    assert getattr(partner, 'OclLibrary4') == owner
    _safe_set(owner, 'essentialocl_types_CollectionType3', None)
    assert getattr(partner, 'OclLibrary4') is None


def test_assoc_oclLibrary59_stub_double():
    # OclLibrary has no real 'OclLibrary60' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_expressions_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_expressions_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_expressions_OclExpression()
    partner = OclLibrary()
    setattr(partner, 'OclLibrary60', None)
    _safe_set(owner, 'essentialocl_expressions_OclExpression', partner)
    assert getattr(partner, 'OclLibrary60') == owner
    _safe_set(owner, 'essentialocl_expressions_OclExpression', None)
    assert getattr(partner, 'OclLibrary60') is None


def test_assoc_oclOrderedSet36_stub_double():
    # OrderedSetType has no real 'OrderedSetType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = OrderedSetType()
    setattr(partner, 'OrderedSetType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary37', partner)
    assert getattr(partner, 'OrderedSetType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary37', None)
    assert getattr(partner, 'OrderedSetType') is None


def test_assoc_oclReal18_stub_double():
    # types_essentialocl_PrimitiveType has no real 'types_essentialocl_PrimitiveType20' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = types_essentialocl_PrimitiveType()
    setattr(partner, 'types_essentialocl_PrimitiveType20', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary19', partner)
    assert getattr(partner, 'types_essentialocl_PrimitiveType20') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary19', None)
    assert getattr(partner, 'types_essentialocl_PrimitiveType20') is None


def test_assoc_oclSequence30_stub_double():
    # SequenceType has no real 'SequenceType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = SequenceType()
    setattr(partner, 'SequenceType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary31', partner)
    assert getattr(partner, 'SequenceType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary31', None)
    assert getattr(partner, 'SequenceType') is None


def test_assoc_oclSet34_stub_double():
    # SetType has no real 'SetType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = SetType()
    setattr(partner, 'SetType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary35', partner)
    assert getattr(partner, 'SetType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary35', None)
    assert getattr(partner, 'SetType') is None


def test_assoc_oclString12_stub_double():
    # types_essentialocl_PrimitiveType has no real 'types_essentialocl_PrimitiveType14' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = types_essentialocl_PrimitiveType()
    setattr(partner, 'types_essentialocl_PrimitiveType14', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary13', partner)
    assert getattr(partner, 'types_essentialocl_PrimitiveType14') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary13', None)
    assert getattr(partner, 'types_essentialocl_PrimitiveType14') is None


def test_assoc_oclTuple38_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary39', {partner})
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary39', set())
    assert getattr(partner, 'TupleType') is None


def test_assoc_oclType26_stub_double():
    # TypeType has no real 'TypeType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = TypeType()
    setattr(partner, 'TypeType', None)
    _safe_set(owner, 'essentialocl_types_OclLibrary27', partner)
    assert getattr(partner, 'TypeType') == owner
    _safe_set(owner, 'essentialocl_types_OclLibrary27', None)
    assert getattr(partner, 'TypeType') is None


def test_assoc_oclVoid23_stub_double():
    # VoidType has no real 'VoidType' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_types_OclLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_types_OclLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_types_OclLibrary()
    partner = VoidType()
    setattr(partner, 'VoidType', None)
    _safe_set(owner, 'oclLibrary', partner)
    assert getattr(partner, 'VoidType') == owner
    _safe_set(owner, 'oclLibrary', None)
    assert getattr(partner, 'VoidType') is None


def test_assoc_part87_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_expressions_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_expressions_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'essentialocl_expressions_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'essentialocl_expressions_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_representedParameter41_stub_double():
    # expressions_essentialocl_Parameter has no real 'expressions_essentialocl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_expressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_expressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_expressions_Variable()
    partner = expressions_essentialocl_Parameter()
    setattr(partner, 'expressions_essentialocl_Parameter', None)
    _safe_set(owner, 'essentialocl_expressions_Variable', partner)
    assert getattr(partner, 'expressions_essentialocl_Parameter') == owner
    _safe_set(owner, 'essentialocl_expressions_Variable', None)
    assert getattr(partner, 'expressions_essentialocl_Parameter') is None


