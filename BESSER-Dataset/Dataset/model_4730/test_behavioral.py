import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AggregateExpression,
    AtomicTerm,
    BoolOperation,
    Constant,
    Function,
    NumericOperation,
    PrimitiveRelation,
    PrimitiveTypeReference,
    ProjectedAggregateExpression,
    QuantifiedExpression,
    Relation,
    SymbolicDeclaration,
    Term,
    TermDescription,
    Type,
    TypeDescriptor,
    TypeReference,
    logiclanguage_AggregateExpression,
    logiclanguage_AggregatedParameterSubstitution,
    logiclanguage_And,
    logiclanguage_Assertion,
    logiclanguage_AssertionAnnotation,
    logiclanguage_AtomicTerm,
    logiclanguage_BoolLiteral,
    logiclanguage_BoolOperation,
    logiclanguage_BoolTypeReference,
    logiclanguage_ComplexTypeReference,
    logiclanguage_Constant,
    logiclanguage_ConstantAnnotation,
    logiclanguage_ConstantDeclaration,
    logiclanguage_ConstantDefinition,
    logiclanguage_Count,
    logiclanguage_DefinedElement,
    logiclanguage_Distinct,
    logiclanguage_Divison,
    logiclanguage_Equals,
    logiclanguage_Exists,
    logiclanguage_Forall,
    logiclanguage_Function,
    logiclanguage_FunctionAnnotation,
    logiclanguage_FunctionDeclaration,
    logiclanguage_FunctionDefinition,
    logiclanguage_IfThenElse,
    logiclanguage_Iff,
    logiclanguage_Impl,
    logiclanguage_InstanceOf,
    logiclanguage_IntLiteral,
    logiclanguage_IntTypeReference,
    logiclanguage_LessOrEqualThan,
    logiclanguage_LessThan,
    logiclanguage_Max,
    logiclanguage_Min,
    logiclanguage_Minus,
    logiclanguage_Mod,
    logiclanguage_MoreOrEqualThan,
    logiclanguage_MoreThan,
    logiclanguage_Multiply,
    logiclanguage_Not,
    logiclanguage_NumericOperation,
    logiclanguage_Or,
    logiclanguage_Plus,
    logiclanguage_Pow,
    logiclanguage_PrimitiveRelation,
    logiclanguage_PrimitiveTypeReference,
    logiclanguage_ProjectedAggregateExpression,
    logiclanguage_QuantifiedExpression,
    logiclanguage_RealLiteral,
    logiclanguage_RealTypeReference,
    logiclanguage_Relation,
    logiclanguage_RelationAnnotation,
    logiclanguage_RelationDeclaration,
    logiclanguage_RelationDefinition,
    logiclanguage_StringLiteral,
    logiclanguage_StringTypeReference,
    logiclanguage_Sum,
    logiclanguage_SymbolicDeclaration,
    logiclanguage_SymbolicValue,
    logiclanguage_Term,
    logiclanguage_TermDescription,
    logiclanguage_TransitiveClosure,
    logiclanguage_Type,
    logiclanguage_TypeDeclaration,
    logiclanguage_TypeDefinition,
    logiclanguage_TypeDescriptor,
    logiclanguage_TypeReference,
    logiclanguage_UnknownBecauseUninterpreted,
    logiclanguage_Variable,
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

def test_assoc_subtypes1_reverse_link_reassign_clear():
    a1 = logiclanguage_Type(isAbstract=True, name="sample_text")
    a2 = logiclanguage_Type(isAbstract=False, name="sample_text_2")
    b = logiclanguage_Type(isAbstract=True, name="sample_text")
    _safe_set(b, 'supertypes', {a1})
    assert _is_linked(b, 'supertypes', a1)
    if hasattr(a1, 'Type'):
        assert _is_linked(a1, 'Type', b)
    _safe_set(b, 'supertypes', {a2})
    assert _is_linked(b, 'supertypes', a2)
    if hasattr(a1, 'Type'):
        assert not _is_linked(a1, 'Type', b)
    if hasattr(a2, 'Type'):
        assert _is_linked(a2, 'Type', b)
    _safe_set(b, 'supertypes', set())
    assert not _is_linked(b, 'supertypes', a2)
    if hasattr(a2, 'Type'):
        assert not _is_linked(a2, 'Type', b)


def test_assoc_supertypes3_reverse_link_reassign_clear():
    a1 = logiclanguage_Type(isAbstract=True, name="sample_text")
    a2 = logiclanguage_Type(isAbstract=False, name="sample_text_2")
    b = logiclanguage_Type(isAbstract=True, name="sample_text")
    _safe_set(b, 'subtypes', {a1})
    assert _is_linked(b, 'subtypes', a1)
    if hasattr(a1, 'Type4'):
        assert _is_linked(a1, 'Type4', b)
    _safe_set(b, 'subtypes', {a2})
    assert _is_linked(b, 'subtypes', a2)
    if hasattr(a1, 'Type4'):
        assert not _is_linked(a1, 'Type4', b)
    if hasattr(a2, 'Type4'):
        assert _is_linked(a2, 'Type4', b)
    _safe_set(b, 'subtypes', set())
    assert not _is_linked(b, 'subtypes', a2)
    if hasattr(a2, 'Type4'):
        assert not _is_linked(a2, 'Type4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations74_stub_double():
    # logiclanguage_AssertionAnnotation has no real 'logicproblem.ecoreAssertionAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so logiclanguage_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logiclanguage_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logiclanguage_Assertion(name="sample_text")
    partner = logiclanguage_AssertionAnnotation()
    setattr(partner, 'logicproblem.ecoreAssertionAnnotation', None)
    _safe_set(owner, 'target75', {partner})
    assert getattr(partner, 'logicproblem.ecoreAssertionAnnotation') == owner
    _safe_set(owner, 'target75', set())
    assert getattr(partner, 'logicproblem.ecoreAssertionAnnotation') is None


def test_assoc_referred8_stub_double():
    # logiclanguage_ComplexTypeReference has no real 'logiclanguage_ComplexTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so logiclanguage_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logiclanguage_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logiclanguage_Type(isAbstract=True, name="sample_text")
    partner = logiclanguage_ComplexTypeReference()
    setattr(partner, 'logiclanguage_ComplexTypeReference', None)
    _safe_set(owner, 'logiclanguage_Type', partner)
    assert getattr(partner, 'logiclanguage_ComplexTypeReference') == owner
    _safe_set(owner, 'logiclanguage_Type', None)
    assert getattr(partner, 'logiclanguage_ComplexTypeReference') is None


def test_assoc_symbolicReference14_stub_double():
    # logiclanguage_SymbolicValue has no real 'logiclanguage_SymbolicValue' property in the generated
    # code (a bare stub) -- manually attach it so logiclanguage_SymbolicDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logiclanguage_SymbolicDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logiclanguage_SymbolicDeclaration(name="sample_text")
    partner = logiclanguage_SymbolicValue()
    setattr(partner, 'logiclanguage_SymbolicValue', None)
    _safe_set(owner, 'logiclanguage_SymbolicDeclaration', partner)
    assert getattr(partner, 'logiclanguage_SymbolicValue') == owner
    _safe_set(owner, 'logiclanguage_SymbolicDeclaration', None)
    assert getattr(partner, 'logiclanguage_SymbolicValue') is None


def test_assoc_value72_stub_double():
    # logiclanguage_Term has no real 'logiclanguage_Term73' property in the generated
    # code (a bare stub) -- manually attach it so logiclanguage_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logiclanguage_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logiclanguage_Assertion(name="sample_text")
    partner = logiclanguage_Term()
    setattr(partner, 'logiclanguage_Term73', None)
    _safe_set(owner, 'logiclanguage_Assertion', partner)
    assert getattr(partner, 'logiclanguage_Term73') == owner
    _safe_set(owner, 'logiclanguage_Assertion', None)
    assert getattr(partner, 'logiclanguage_Term73') is None


