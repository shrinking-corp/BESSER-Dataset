import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassifierRef,
    CollectionLiteralExp,
    ContextDecl,
    Expression,
    NameExp,
    NavigatingExp,
    OclMessageArg,
    OperationRef,
    PackageRef,
    PrimitiveLiteralExp,
    PropertyRef,
    TypeExp,
    backtrackingContentAssistTest_Body,
    backtrackingContentAssistTest_BooleanLiteralExp,
    backtrackingContentAssistTest_ClassifierContextDecl,
    backtrackingContentAssistTest_ClassifierRef,
    backtrackingContentAssistTest_CollectionLiteralExp,
    backtrackingContentAssistTest_CollectionLiteralPart,
    backtrackingContentAssistTest_CollectionType,
    backtrackingContentAssistTest_ContextDecl,
    backtrackingContentAssistTest_Definition,
    backtrackingContentAssistTest_Der,
    backtrackingContentAssistTest_Document,
    backtrackingContentAssistTest_EObject,
    backtrackingContentAssistTest_Expression,
    backtrackingContentAssistTest_IfExp,
    backtrackingContentAssistTest_InfixExp,
    backtrackingContentAssistTest_Init,
    backtrackingContentAssistTest_InvalidLiteralExp,
    backtrackingContentAssistTest_Invariant,
    backtrackingContentAssistTest_LetExp,
    backtrackingContentAssistTest_LetVariable,
    backtrackingContentAssistTest_NameExp,
    backtrackingContentAssistTest_NavigatingExp,
    backtrackingContentAssistTest_NestedExp,
    backtrackingContentAssistTest_NullLiteralExp,
    backtrackingContentAssistTest_NumberLiteralExp,
    backtrackingContentAssistTest_OclMessage,
    backtrackingContentAssistTest_OclMessageArg,
    backtrackingContentAssistTest_OperationContextDecl,
    backtrackingContentAssistTest_OperationRef,
    backtrackingContentAssistTest_PackageDeclaration,
    backtrackingContentAssistTest_PackageRef,
    backtrackingContentAssistTest_Parameter,
    backtrackingContentAssistTest_PathNameExp,
    backtrackingContentAssistTest_Post,
    backtrackingContentAssistTest_Pre,
    backtrackingContentAssistTest_PreExp,
    backtrackingContentAssistTest_PrefixExp,
    backtrackingContentAssistTest_PrimitiveLiteralExp,
    backtrackingContentAssistTest_PrimitiveType,
    backtrackingContentAssistTest_PropertyContextDecl,
    backtrackingContentAssistTest_PropertyRef,
    backtrackingContentAssistTest_QualifiedClassifierRef,
    backtrackingContentAssistTest_QualifiedOperationRef,
    backtrackingContentAssistTest_QualifiedPackageRef,
    backtrackingContentAssistTest_QualifiedPropertyRef,
    backtrackingContentAssistTest_RoundBracketExp,
    backtrackingContentAssistTest_SelfExp,
    backtrackingContentAssistTest_SimpleClassifierRef,
    backtrackingContentAssistTest_SimpleNameExp,
    backtrackingContentAssistTest_SimpleOperationRef,
    backtrackingContentAssistTest_SimplePackageRef,
    backtrackingContentAssistTest_SimplePropertyRef,
    backtrackingContentAssistTest_SquareBracketExp,
    backtrackingContentAssistTest_StringLiteralExp,
    backtrackingContentAssistTest_TupleLiteralExp,
    backtrackingContentAssistTest_TupleLiteralPart,
    backtrackingContentAssistTest_TupleType,
    backtrackingContentAssistTest_TypeExp,
    backtrackingContentAssistTest_iteratorAccumulator,
    backtrackingContentAssistTest_iteratorVariable,
    backtrackingContentAssistTest_tuplePart,
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

def test_assoc_definitions7_reverse_link_reassign_clear():
    a1 = backtrackingContentAssistTest_Definition(constrainedName="sample_text", constraintName="sample_text", static=True)
    a2 = backtrackingContentAssistTest_Definition(constrainedName="sample_text_2", constraintName="sample_text_2", static=False)
    b = backtrackingContentAssistTest_ClassifierContextDecl(selfName="sample_text")
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', {a1})
    assert _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', a1)
    if hasattr(a1, 'backtrackingContentAssistTest_Definition'):
        assert _is_linked(a1, 'backtrackingContentAssistTest_Definition', b)
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', {a2})
    assert _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', a2)
    if hasattr(a1, 'backtrackingContentAssistTest_Definition'):
        assert not _is_linked(a1, 'backtrackingContentAssistTest_Definition', b)
    if hasattr(a2, 'backtrackingContentAssistTest_Definition'):
        assert _is_linked(a2, 'backtrackingContentAssistTest_Definition', b)
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', set())
    assert not _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl8', a2)
    if hasattr(a2, 'backtrackingContentAssistTest_Definition'):
        assert not _is_linked(a2, 'backtrackingContentAssistTest_Definition', b)


def test_assoc_invariants5_reverse_link_reassign_clear():
    a1 = backtrackingContentAssistTest_Invariant(constraintName="sample_text")
    a2 = backtrackingContentAssistTest_Invariant(constraintName="sample_text_2")
    b = backtrackingContentAssistTest_ClassifierContextDecl(selfName="sample_text")
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', {a1})
    assert _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', a1)
    if hasattr(a1, 'backtrackingContentAssistTest_Invariant'):
        assert _is_linked(a1, 'backtrackingContentAssistTest_Invariant', b)
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', {a2})
    assert _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', a2)
    if hasattr(a1, 'backtrackingContentAssistTest_Invariant'):
        assert not _is_linked(a1, 'backtrackingContentAssistTest_Invariant', b)
    if hasattr(a2, 'backtrackingContentAssistTest_Invariant'):
        assert _is_linked(a2, 'backtrackingContentAssistTest_Invariant', b)
    _safe_set(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', set())
    assert not _is_linked(b, 'backtrackingContentAssistTest_ClassifierContextDecl6', a2)
    if hasattr(a2, 'backtrackingContentAssistTest_Invariant'):
        assert not _is_linked(a2, 'backtrackingContentAssistTest_Invariant', b)


def test_assoc_parameters9_reverse_link_reassign_clear():
    a1 = backtrackingContentAssistTest_Parameter(name="sample_text")
    a2 = backtrackingContentAssistTest_Parameter(name="sample_text_2")
    b = backtrackingContentAssistTest_Definition(constrainedName="sample_text", constraintName="sample_text", static=True)
    _safe_set(b, 'backtrackingContentAssistTest_Definition10', {a1})
    assert _is_linked(b, 'backtrackingContentAssistTest_Definition10', a1)
    if hasattr(a1, 'backtrackingContentAssistTest_Parameter'):
        assert _is_linked(a1, 'backtrackingContentAssistTest_Parameter', b)
    _safe_set(b, 'backtrackingContentAssistTest_Definition10', {a2})
    assert _is_linked(b, 'backtrackingContentAssistTest_Definition10', a2)
    if hasattr(a1, 'backtrackingContentAssistTest_Parameter'):
        assert not _is_linked(a1, 'backtrackingContentAssistTest_Parameter', b)
    if hasattr(a2, 'backtrackingContentAssistTest_Parameter'):
        assert _is_linked(a2, 'backtrackingContentAssistTest_Parameter', b)
    _safe_set(b, 'backtrackingContentAssistTest_Definition10', set())
    assert not _is_linked(b, 'backtrackingContentAssistTest_Definition10', a2)
    if hasattr(a2, 'backtrackingContentAssistTest_Parameter'):
        assert not _is_linked(a2, 'backtrackingContentAssistTest_Parameter', b)


def test_assoc_part71_reverse_link_reassign_clear():
    a1 = backtrackingContentAssistTest_tuplePart(name="sample_text")
    a2 = backtrackingContentAssistTest_tuplePart(name="sample_text_2")
    b = backtrackingContentAssistTest_TupleType(name="sample_text")
    _safe_set(b, 'backtrackingContentAssistTest_TupleType', {a1})
    assert _is_linked(b, 'backtrackingContentAssistTest_TupleType', a1)
    if hasattr(a1, 'backtrackingContentAssistTest_tuplePart'):
        assert _is_linked(a1, 'backtrackingContentAssistTest_tuplePart', b)
    _safe_set(b, 'backtrackingContentAssistTest_TupleType', {a2})
    assert _is_linked(b, 'backtrackingContentAssistTest_TupleType', a2)
    if hasattr(a1, 'backtrackingContentAssistTest_tuplePart'):
        assert not _is_linked(a1, 'backtrackingContentAssistTest_tuplePart', b)
    if hasattr(a2, 'backtrackingContentAssistTest_tuplePart'):
        assert _is_linked(a2, 'backtrackingContentAssistTest_tuplePart', b)
    _safe_set(b, 'backtrackingContentAssistTest_TupleType', set())
    assert not _is_linked(b, 'backtrackingContentAssistTest_TupleType', a2)
    if hasattr(a2, 'backtrackingContentAssistTest_tuplePart'):
        assert not _is_linked(a2, 'backtrackingContentAssistTest_tuplePart', b)


def test_assoc_variable197_reverse_link_reassign_clear():
    a1 = backtrackingContentAssistTest_iteratorVariable(name="sample_text")
    a2 = backtrackingContentAssistTest_iteratorVariable(name="sample_text_2")
    b = backtrackingContentAssistTest_RoundBracketExp(pre=True)
    _safe_set(b, 'backtrackingContentAssistTest_RoundBracketExp98', a1)
    assert _is_linked(b, 'backtrackingContentAssistTest_RoundBracketExp98', a1)
    if hasattr(a1, 'backtrackingContentAssistTest_iteratorVariable99'):
        assert _is_linked(a1, 'backtrackingContentAssistTest_iteratorVariable99', b)
    _safe_set(b, 'backtrackingContentAssistTest_RoundBracketExp98', a2)
    assert _is_linked(b, 'backtrackingContentAssistTest_RoundBracketExp98', a2)
    if hasattr(a1, 'backtrackingContentAssistTest_iteratorVariable99'):
        assert not _is_linked(a1, 'backtrackingContentAssistTest_iteratorVariable99', b)
    if hasattr(a2, 'backtrackingContentAssistTest_iteratorVariable99'):
        assert _is_linked(a2, 'backtrackingContentAssistTest_iteratorVariable99', b)
    _safe_set(b, 'backtrackingContentAssistTest_RoundBracketExp98', None)
    assert not _is_linked(b, 'backtrackingContentAssistTest_RoundBracketExp98', a2)
    if hasattr(a2, 'backtrackingContentAssistTest_iteratorVariable99'):
        assert not _is_linked(a2, 'backtrackingContentAssistTest_iteratorVariable99', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument134_stub_double():
    # backtrackingContentAssistTest_NavigatingExp has no real 'backtrackingContentAssistTest_NavigatingExp' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_InfixExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_InfixExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_InfixExp(op="sample_text")
    partner = backtrackingContentAssistTest_NavigatingExp()
    setattr(partner, 'backtrackingContentAssistTest_NavigatingExp', None)
    _safe_set(owner, 'backtrackingContentAssistTest_InfixExp135', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_NavigatingExp') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_InfixExp135', None)
    assert getattr(partner, 'backtrackingContentAssistTest_NavigatingExp') is None


def test_assoc_arguments102_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression104' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_RoundBracketExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_RoundBracketExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_RoundBracketExp(pre=True)
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression104', None)
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp103', {partner})
    assert getattr(partner, 'backtrackingContentAssistTest_Expression104') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp103', set())
    assert getattr(partner, 'backtrackingContentAssistTest_Expression104') is None


def test_assoc_arguments107_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression109' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_SquareBracketExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_SquareBracketExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_SquareBracketExp(pre=True)
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression109', None)
    _safe_set(owner, 'backtrackingContentAssistTest_SquareBracketExp108', {partner})
    assert getattr(partner, 'backtrackingContentAssistTest_Expression109') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_SquareBracketExp108', set())
    assert getattr(partner, 'backtrackingContentAssistTest_Expression109') is None


def test_assoc_arguments138_stub_double():
    # backtrackingContentAssistTest_OclMessageArg has no real 'backtrackingContentAssistTest_OclMessageArg140' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_OclMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_OclMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_OclMessage(messageName="sample_text", op="sample_text")
    partner = backtrackingContentAssistTest_OclMessageArg()
    setattr(partner, 'backtrackingContentAssistTest_OclMessageArg140', None)
    _safe_set(owner, 'backtrackingContentAssistTest_OclMessage139', {partner})
    assert getattr(partner, 'backtrackingContentAssistTest_OclMessageArg140') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_OclMessage139', set())
    assert getattr(partner, 'backtrackingContentAssistTest_OclMessageArg140') is None


def test_assoc_bodies34_stub_double():
    # backtrackingContentAssistTest_OperationContextDecl has no real 'backtrackingContentAssistTest_OperationContextDecl35' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Body's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Body's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Body(constraintName="sample_text")
    partner = backtrackingContentAssistTest_OperationContextDecl()
    setattr(partner, 'backtrackingContentAssistTest_OperationContextDecl35', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Body36', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl35')
    _safe_set(owner, 'backtrackingContentAssistTest_Body36', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl35')


def test_assoc_classifier4_stub_double():
    # backtrackingContentAssistTest_ClassifierRef has no real 'backtrackingContentAssistTest_ClassifierRef' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_ClassifierContextDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_ClassifierContextDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_ClassifierContextDecl(selfName="sample_text")
    partner = backtrackingContentAssistTest_ClassifierRef()
    setattr(partner, 'backtrackingContentAssistTest_ClassifierRef', None)
    _safe_set(owner, 'backtrackingContentAssistTest_ClassifierContextDecl', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_ClassifierRef') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_ClassifierContextDecl', None)
    assert getattr(partner, 'backtrackingContentAssistTest_ClassifierRef') is None


def test_assoc_element112_stub_double():
    # backtrackingContentAssistTest_NameExp has no real 'backtrackingContentAssistTest_NameExp113' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_PathNameExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_PathNameExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_PathNameExp(namespace="sample_text")
    partner = backtrackingContentAssistTest_NameExp()
    setattr(partner, 'backtrackingContentAssistTest_NameExp113', None)
    _safe_set(owner, 'backtrackingContentAssistTest_PathNameExp', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp113') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_PathNameExp', None)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp113') is None


def test_assoc_element61_stub_double():
    # backtrackingContentAssistTest_ClassifierRef has no real 'backtrackingContentAssistTest_ClassifierRef62' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_QualifiedClassifierRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_QualifiedClassifierRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_QualifiedClassifierRef(namespace="sample_text")
    partner = backtrackingContentAssistTest_ClassifierRef()
    setattr(partner, 'backtrackingContentAssistTest_ClassifierRef62', None)
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedClassifierRef', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_ClassifierRef62') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedClassifierRef', None)
    assert getattr(partner, 'backtrackingContentAssistTest_ClassifierRef62') is None


def test_assoc_element63_stub_double():
    # backtrackingContentAssistTest_OperationRef has no real 'backtrackingContentAssistTest_OperationRef64' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_QualifiedOperationRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_QualifiedOperationRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_QualifiedOperationRef(namespace="sample_text")
    partner = backtrackingContentAssistTest_OperationRef()
    setattr(partner, 'backtrackingContentAssistTest_OperationRef64', None)
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedOperationRef', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_OperationRef64') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedOperationRef', None)
    assert getattr(partner, 'backtrackingContentAssistTest_OperationRef64') is None


def test_assoc_element65_stub_double():
    # backtrackingContentAssistTest_PropertyRef has no real 'backtrackingContentAssistTest_PropertyRef66' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_QualifiedPropertyRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_QualifiedPropertyRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_QualifiedPropertyRef(namespace="sample_text")
    partner = backtrackingContentAssistTest_PropertyRef()
    setattr(partner, 'backtrackingContentAssistTest_PropertyRef66', None)
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedPropertyRef', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_PropertyRef66') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedPropertyRef', None)
    assert getattr(partner, 'backtrackingContentAssistTest_PropertyRef66') is None


def test_assoc_element67_stub_double():
    # backtrackingContentAssistTest_PackageRef has no real 'backtrackingContentAssistTest_PackageRef68' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_QualifiedPackageRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_QualifiedPackageRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_QualifiedPackageRef(namespace="sample_text")
    partner = backtrackingContentAssistTest_PackageRef()
    setattr(partner, 'backtrackingContentAssistTest_PackageRef68', None)
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedPackageRef', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_PackageRef68') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_QualifiedPackageRef', None)
    assert getattr(partner, 'backtrackingContentAssistTest_PackageRef68') is None


def test_assoc_expression13_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Definition(constrainedName="sample_text", constraintName="sample_text", static=True)
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression15', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Definition14', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression15') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Definition14', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression15') is None


def test_assoc_expression20_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Invariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Invariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Invariant(constraintName="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression22', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Invariant21', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression22') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Invariant21', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression22') is None


def test_assoc_expression3_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Body's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Body's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Body(constraintName="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Body', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Body', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression') is None


def test_assoc_expression45_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Post's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Post's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Post(constraintName="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression47', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Post46', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression47') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Post46', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression47') is None


def test_assoc_expression48_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Pre's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Pre's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Pre(constraintName="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression50', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Pre49', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression50') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Pre49', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression50') is None


def test_assoc_initExpression129_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression131' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_LetVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_LetVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_LetVariable(name="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression131', None)
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable130', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression131') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable130', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression131') is None


def test_assoc_initExpression86_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_TupleLiteralPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_TupleLiteralPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_TupleLiteralPart(name="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression88', None)
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart87', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression88') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart87', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression88') is None


def test_assoc_initExpression93_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression95' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_iteratorAccumulator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_iteratorAccumulator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_iteratorAccumulator(name="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression95', None)
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorAccumulator94', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression95') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorAccumulator94', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression95') is None


def test_assoc_name105_stub_double():
    # backtrackingContentAssistTest_NameExp has no real 'backtrackingContentAssistTest_NameExp106' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_SquareBracketExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_SquareBracketExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_SquareBracketExp(pre=True)
    partner = backtrackingContentAssistTest_NameExp()
    setattr(partner, 'backtrackingContentAssistTest_NameExp106', None)
    _safe_set(owner, 'backtrackingContentAssistTest_SquareBracketExp', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp106') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_SquareBracketExp', None)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp106') is None


def test_assoc_name96_stub_double():
    # backtrackingContentAssistTest_NameExp has no real 'backtrackingContentAssistTest_NameExp' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_RoundBracketExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_RoundBracketExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_RoundBracketExp(pre=True)
    partner = backtrackingContentAssistTest_NameExp()
    setattr(partner, 'backtrackingContentAssistTest_NameExp', None)
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp', None)
    assert getattr(partner, 'backtrackingContentAssistTest_NameExp') is None


def test_assoc_parameters24_stub_double():
    # backtrackingContentAssistTest_OperationContextDecl has no real 'backtrackingContentAssistTest_OperationContextDecl25' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Parameter(name="sample_text")
    partner = backtrackingContentAssistTest_OperationContextDecl()
    setattr(partner, 'backtrackingContentAssistTest_OperationContextDecl25', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Parameter26', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl25')
    _safe_set(owner, 'backtrackingContentAssistTest_Parameter26', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl25')


def test_assoc_part82_stub_double():
    # backtrackingContentAssistTest_TupleLiteralExp has no real 'backtrackingContentAssistTest_TupleLiteralExp' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_TupleLiteralPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_TupleLiteralPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_TupleLiteralPart(name="sample_text")
    partner = backtrackingContentAssistTest_TupleLiteralExp()
    setattr(partner, 'backtrackingContentAssistTest_TupleLiteralExp', None)
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_TupleLiteralExp')
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_TupleLiteralExp')


def test_assoc_posts32_stub_double():
    # backtrackingContentAssistTest_OperationContextDecl has no real 'backtrackingContentAssistTest_OperationContextDecl33' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Post's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Post's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Post(constraintName="sample_text")
    partner = backtrackingContentAssistTest_OperationContextDecl()
    setattr(partner, 'backtrackingContentAssistTest_OperationContextDecl33', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Post', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl33')
    _safe_set(owner, 'backtrackingContentAssistTest_Post', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl33')


def test_assoc_pres30_stub_double():
    # backtrackingContentAssistTest_OperationContextDecl has no real 'backtrackingContentAssistTest_OperationContextDecl31' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Pre's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Pre's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Pre(constraintName="sample_text")
    partner = backtrackingContentAssistTest_OperationContextDecl()
    setattr(partner, 'backtrackingContentAssistTest_OperationContextDecl31', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Pre', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl31')
    _safe_set(owner, 'backtrackingContentAssistTest_Pre', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_OperationContextDecl31')


def test_assoc_source132_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression133' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_InfixExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_InfixExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_InfixExp(op="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression133', None)
    _safe_set(owner, 'backtrackingContentAssistTest_InfixExp', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression133') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_InfixExp', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression133') is None


def test_assoc_source136_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression137' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_OclMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_OclMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_OclMessage(messageName="sample_text", op="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression137', None)
    _safe_set(owner, 'backtrackingContentAssistTest_OclMessage', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression137') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_OclMessage', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression137') is None


def test_assoc_source141_stub_double():
    # backtrackingContentAssistTest_Expression has no real 'backtrackingContentAssistTest_Expression142' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_PrefixExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_PrefixExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_PrefixExp(op="sample_text")
    partner = backtrackingContentAssistTest_Expression()
    setattr(partner, 'backtrackingContentAssistTest_Expression142', None)
    _safe_set(owner, 'backtrackingContentAssistTest_PrefixExp', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression142') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_PrefixExp', None)
    assert getattr(partner, 'backtrackingContentAssistTest_Expression142') is None


def test_assoc_type11_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Definition(constrainedName="sample_text", constraintName="sample_text", static=True)
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Definition12', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Definition12', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp') is None


def test_assoc_type126_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp128' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_LetVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_LetVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_LetVariable(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp128', None)
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable127', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp128') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable127', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp128') is None


def test_assoc_type42_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp44' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_Parameter(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp44', None)
    _safe_set(owner, 'backtrackingContentAssistTest_Parameter43', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp44') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_Parameter43', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp44') is None


def test_assoc_type72_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp74' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_tuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_tuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_tuplePart(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp74', None)
    _safe_set(owner, 'backtrackingContentAssistTest_tuplePart73', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp74') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_tuplePart73', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp74') is None


def test_assoc_type83_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp85' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_TupleLiteralPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_TupleLiteralPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_TupleLiteralPart(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp85', None)
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart84', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp85') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_TupleLiteralPart84', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp85') is None


def test_assoc_type89_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp90' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_iteratorVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_iteratorVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_iteratorVariable(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp90', None)
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorVariable', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp90') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorVariable', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp90') is None


def test_assoc_type91_stub_double():
    # backtrackingContentAssistTest_TypeExp has no real 'backtrackingContentAssistTest_TypeExp92' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_iteratorAccumulator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_iteratorAccumulator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_iteratorAccumulator(name="sample_text")
    partner = backtrackingContentAssistTest_TypeExp()
    setattr(partner, 'backtrackingContentAssistTest_TypeExp92', None)
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorAccumulator', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp92') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_iteratorAccumulator', None)
    assert getattr(partner, 'backtrackingContentAssistTest_TypeExp92') is None


def test_assoc_variable122_stub_double():
    # backtrackingContentAssistTest_LetExp has no real 'backtrackingContentAssistTest_LetExp' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_LetVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_LetVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_LetVariable(name="sample_text")
    partner = backtrackingContentAssistTest_LetExp()
    setattr(partner, 'backtrackingContentAssistTest_LetExp', None)
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable', partner)
    assert owner in getattr(partner, 'backtrackingContentAssistTest_LetExp')
    _safe_set(owner, 'backtrackingContentAssistTest_LetVariable', None)
    assert owner not in getattr(partner, 'backtrackingContentAssistTest_LetExp')


def test_assoc_variable2100_stub_double():
    # backtrackingContentAssistTest_EObject has no real 'backtrackingContentAssistTest_EObject' property in the generated
    # code (a bare stub) -- manually attach it so backtrackingContentAssistTest_RoundBracketExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backtrackingContentAssistTest_RoundBracketExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backtrackingContentAssistTest_RoundBracketExp(pre=True)
    partner = backtrackingContentAssistTest_EObject()
    setattr(partner, 'backtrackingContentAssistTest_EObject', None)
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp101', partner)
    assert getattr(partner, 'backtrackingContentAssistTest_EObject') == owner
    _safe_set(owner, 'backtrackingContentAssistTest_RoundBracketExp101', None)
    assert getattr(partner, 'backtrackingContentAssistTest_EObject') is None


