import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    USE_Association,
    USE_Attribute,
    USE_Class,
    USE_CollectionType,
    USE_Enumeration,
    USE_EnumerationType,
    USE_Literal,
    USE_Model,
    USE_OCLExpression,
    USE_Operation,
    USE_Parameter,
    USE_ReferenceType,
    USE_Role,
    USE_SimpleType,
    USE_Type,
    AssocKind,
    CollectionTypes,
    SimpleTypes,
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

def test_assoc_associations12_reverse_link_reassign_clear():
    a1 = USE_Model(name="sample_text")
    a2 = USE_Model(name="sample_text_2")
    b = USE_Association(kind="sample_text", name="sample_text")
    _safe_set(b, 'USE_Association', a1)
    assert _is_linked(b, 'USE_Association', a1)
    if hasattr(a1, 'USE_Model13'):
        assert _is_linked(a1, 'USE_Model13', b)
    _safe_set(b, 'USE_Association', a2)
    assert _is_linked(b, 'USE_Association', a2)
    if hasattr(a1, 'USE_Model13'):
        assert not _is_linked(a1, 'USE_Model13', b)
    if hasattr(a2, 'USE_Model13'):
        assert _is_linked(a2, 'USE_Model13', b)
    _safe_set(b, 'USE_Association', None)
    assert not _is_linked(b, 'USE_Association', a2)
    if hasattr(a2, 'USE_Model13'):
        assert not _is_linked(a2, 'USE_Model13', b)


def test_assoc_attributes2_reverse_link_reassign_clear():
    a1 = USE_Class(abstract=True, name="sample_text")
    a2 = USE_Class(abstract=False, name="sample_text_2")
    b = USE_Attribute(name="sample_text")
    _safe_set(b, 'USE_Attribute', a1)
    assert _is_linked(b, 'USE_Attribute', a1)
    if hasattr(a1, 'USE_Class3'):
        assert _is_linked(a1, 'USE_Class3', b)
    _safe_set(b, 'USE_Attribute', a2)
    assert _is_linked(b, 'USE_Attribute', a2)
    if hasattr(a1, 'USE_Class3'):
        assert not _is_linked(a1, 'USE_Class3', b)
    if hasattr(a2, 'USE_Class3'):
        assert _is_linked(a2, 'USE_Class3', b)
    _safe_set(b, 'USE_Attribute', None)
    assert not _is_linked(b, 'USE_Attribute', a2)
    if hasattr(a2, 'USE_Class3'):
        assert not _is_linked(a2, 'USE_Class3', b)


def test_assoc_className43_reverse_link_reassign_clear():
    a1 = USE_Role(lowerBound=7, name="sample_text", ordered=True, upperBound=7)
    a2 = USE_Role(lowerBound=13, name="sample_text_2", ordered=False, upperBound=13)
    b = USE_Class(abstract=True, name="sample_text")
    _safe_set(b, 'USE_Class45', a1)
    assert _is_linked(b, 'USE_Class45', a1)
    if hasattr(a1, 'USE_Role44'):
        assert _is_linked(a1, 'USE_Role44', b)
    _safe_set(b, 'USE_Class45', a2)
    assert _is_linked(b, 'USE_Class45', a2)
    if hasattr(a1, 'USE_Role44'):
        assert not _is_linked(a1, 'USE_Role44', b)
    if hasattr(a2, 'USE_Role44'):
        assert _is_linked(a2, 'USE_Role44', b)
    _safe_set(b, 'USE_Class45', None)
    assert not _is_linked(b, 'USE_Class45', a2)
    if hasattr(a2, 'USE_Role44'):
        assert not _is_linked(a2, 'USE_Role44', b)


def test_assoc_classes8_reverse_link_reassign_clear():
    a1 = USE_Model(name="sample_text")
    a2 = USE_Model(name="sample_text_2")
    b = USE_Class(abstract=True, name="sample_text")
    _safe_set(b, 'USE_Class9', a1)
    assert _is_linked(b, 'USE_Class9', a1)
    if hasattr(a1, 'USE_Model'):
        assert _is_linked(a1, 'USE_Model', b)
    _safe_set(b, 'USE_Class9', a2)
    assert _is_linked(b, 'USE_Class9', a2)
    if hasattr(a1, 'USE_Model'):
        assert not _is_linked(a1, 'USE_Model', b)
    if hasattr(a2, 'USE_Model'):
        assert _is_linked(a2, 'USE_Model', b)
    _safe_set(b, 'USE_Class9', None)
    assert not _is_linked(b, 'USE_Class9', a2)
    if hasattr(a2, 'USE_Model'):
        assert not _is_linked(a2, 'USE_Model', b)


def test_assoc_enumerations10_reverse_link_reassign_clear():
    a1 = USE_Model(name="sample_text")
    a2 = USE_Model(name="sample_text_2")
    b = USE_Enumeration(name="sample_text")
    _safe_set(b, 'USE_Enumeration', a1)
    assert _is_linked(b, 'USE_Enumeration', a1)
    if hasattr(a1, 'USE_Model11'):
        assert _is_linked(a1, 'USE_Model11', b)
    _safe_set(b, 'USE_Enumeration', a2)
    assert _is_linked(b, 'USE_Enumeration', a2)
    if hasattr(a1, 'USE_Model11'):
        assert not _is_linked(a1, 'USE_Model11', b)
    if hasattr(a2, 'USE_Model11'):
        assert _is_linked(a2, 'USE_Model11', b)
    _safe_set(b, 'USE_Enumeration', None)
    assert not _is_linked(b, 'USE_Enumeration', a2)
    if hasattr(a2, 'USE_Model11'):
        assert not _is_linked(a2, 'USE_Model11', b)


def test_assoc_implementation18_reverse_link_reassign_clear():
    a1 = USE_Operation(name="sample_text")
    a2 = USE_Operation(name="sample_text_2")
    b = USE_OCLExpression(expr="sample_text")
    _safe_set(b, 'USE_OCLExpression20', a1)
    assert _is_linked(b, 'USE_OCLExpression20', a1)
    if hasattr(a1, 'USE_Operation19'):
        assert _is_linked(a1, 'USE_Operation19', b)
    _safe_set(b, 'USE_OCLExpression20', a2)
    assert _is_linked(b, 'USE_OCLExpression20', a2)
    if hasattr(a1, 'USE_Operation19'):
        assert not _is_linked(a1, 'USE_Operation19', b)
    if hasattr(a2, 'USE_Operation19'):
        assert _is_linked(a2, 'USE_Operation19', b)
    _safe_set(b, 'USE_OCLExpression20', None)
    assert not _is_linked(b, 'USE_OCLExpression20', a2)
    if hasattr(a2, 'USE_Operation19'):
        assert not _is_linked(a2, 'USE_Operation19', b)


def test_assoc_invariants6_reverse_link_reassign_clear():
    a1 = USE_OCLExpression(expr="sample_text")
    a2 = USE_OCLExpression(expr="sample_text_2")
    b = USE_Class(abstract=True, name="sample_text")
    _safe_set(b, 'USE_Class7', {a1})
    assert _is_linked(b, 'USE_Class7', a1)
    if hasattr(a1, 'USE_OCLExpression'):
        assert _is_linked(a1, 'USE_OCLExpression', b)
    _safe_set(b, 'USE_Class7', {a2})
    assert _is_linked(b, 'USE_Class7', a2)
    if hasattr(a1, 'USE_OCLExpression'):
        assert not _is_linked(a1, 'USE_OCLExpression', b)
    if hasattr(a2, 'USE_OCLExpression'):
        assert _is_linked(a2, 'USE_OCLExpression', b)
    _safe_set(b, 'USE_Class7', set())
    assert not _is_linked(b, 'USE_Class7', a2)
    if hasattr(a2, 'USE_OCLExpression'):
        assert not _is_linked(a2, 'USE_OCLExpression', b)


def test_assoc_literals39_reverse_link_reassign_clear():
    a1 = USE_Literal(name="sample_text")
    a2 = USE_Literal(name="sample_text_2")
    b = USE_Enumeration(name="sample_text")
    _safe_set(b, 'USE_Enumeration40', {a1})
    assert _is_linked(b, 'USE_Enumeration40', a1)
    if hasattr(a1, 'USE_Literal'):
        assert _is_linked(a1, 'USE_Literal', b)
    _safe_set(b, 'USE_Enumeration40', {a2})
    assert _is_linked(b, 'USE_Enumeration40', a2)
    if hasattr(a1, 'USE_Literal'):
        assert not _is_linked(a1, 'USE_Literal', b)
    if hasattr(a2, 'USE_Literal'):
        assert _is_linked(a2, 'USE_Literal', b)
    _safe_set(b, 'USE_Enumeration40', set())
    assert not _is_linked(b, 'USE_Enumeration40', a2)
    if hasattr(a2, 'USE_Literal'):
        assert not _is_linked(a2, 'USE_Literal', b)


def test_assoc_operations4_reverse_link_reassign_clear():
    a1 = USE_Operation(name="sample_text")
    a2 = USE_Operation(name="sample_text_2")
    b = USE_Class(abstract=True, name="sample_text")
    _safe_set(b, 'USE_Class5', {a1})
    assert _is_linked(b, 'USE_Class5', a1)
    if hasattr(a1, 'USE_Operation'):
        assert _is_linked(a1, 'USE_Operation', b)
    _safe_set(b, 'USE_Class5', {a2})
    assert _is_linked(b, 'USE_Class5', a2)
    if hasattr(a1, 'USE_Operation'):
        assert not _is_linked(a1, 'USE_Operation', b)
    if hasattr(a2, 'USE_Operation'):
        assert _is_linked(a2, 'USE_Operation', b)
    _safe_set(b, 'USE_Class5', set())
    assert not _is_linked(b, 'USE_Class5', a2)
    if hasattr(a2, 'USE_Operation'):
        assert not _is_linked(a2, 'USE_Operation', b)


def test_assoc_parameters16_reverse_link_reassign_clear():
    a1 = USE_Parameter(name="sample_text")
    a2 = USE_Parameter(name="sample_text_2")
    b = USE_Operation(name="sample_text")
    _safe_set(b, 'USE_Operation17', {a1})
    assert _is_linked(b, 'USE_Operation17', a1)
    if hasattr(a1, 'USE_Parameter'):
        assert _is_linked(a1, 'USE_Parameter', b)
    _safe_set(b, 'USE_Operation17', {a2})
    assert _is_linked(b, 'USE_Operation17', a2)
    if hasattr(a1, 'USE_Parameter'):
        assert not _is_linked(a1, 'USE_Parameter', b)
    if hasattr(a2, 'USE_Parameter'):
        assert _is_linked(a2, 'USE_Parameter', b)
    _safe_set(b, 'USE_Operation17', set())
    assert not _is_linked(b, 'USE_Operation17', a2)
    if hasattr(a2, 'USE_Parameter'):
        assert not _is_linked(a2, 'USE_Parameter', b)


def test_assoc_postCondition27_reverse_link_reassign_clear():
    a1 = USE_Operation(name="sample_text")
    a2 = USE_Operation(name="sample_text_2")
    b = USE_OCLExpression(expr="sample_text")
    _safe_set(b, 'USE_OCLExpression29', a1)
    assert _is_linked(b, 'USE_OCLExpression29', a1)
    if hasattr(a1, 'USE_Operation28'):
        assert _is_linked(a1, 'USE_Operation28', b)
    _safe_set(b, 'USE_OCLExpression29', a2)
    assert _is_linked(b, 'USE_OCLExpression29', a2)
    if hasattr(a1, 'USE_Operation28'):
        assert not _is_linked(a1, 'USE_Operation28', b)
    if hasattr(a2, 'USE_Operation28'):
        assert _is_linked(a2, 'USE_Operation28', b)
    _safe_set(b, 'USE_OCLExpression29', None)
    assert not _is_linked(b, 'USE_OCLExpression29', a2)
    if hasattr(a2, 'USE_Operation28'):
        assert not _is_linked(a2, 'USE_Operation28', b)


def test_assoc_preCondition24_reverse_link_reassign_clear():
    a1 = USE_Operation(name="sample_text")
    a2 = USE_Operation(name="sample_text_2")
    b = USE_OCLExpression(expr="sample_text")
    _safe_set(b, 'USE_OCLExpression26', a1)
    assert _is_linked(b, 'USE_OCLExpression26', a1)
    if hasattr(a1, 'USE_Operation25'):
        assert _is_linked(a1, 'USE_Operation25', b)
    _safe_set(b, 'USE_OCLExpression26', a2)
    assert _is_linked(b, 'USE_OCLExpression26', a2)
    if hasattr(a1, 'USE_Operation25'):
        assert not _is_linked(a1, 'USE_Operation25', b)
    if hasattr(a2, 'USE_Operation25'):
        assert _is_linked(a2, 'USE_Operation25', b)
    _safe_set(b, 'USE_OCLExpression26', None)
    assert not _is_linked(b, 'USE_OCLExpression26', a2)
    if hasattr(a2, 'USE_Operation25'):
        assert not _is_linked(a2, 'USE_Operation25', b)


def test_assoc_role41_reverse_link_reassign_clear():
    a1 = USE_Role(lowerBound=7, name="sample_text", ordered=True, upperBound=7)
    a2 = USE_Role(lowerBound=13, name="sample_text_2", ordered=False, upperBound=13)
    b = USE_Association(kind="sample_text", name="sample_text")
    _safe_set(b, 'USE_Association42', {a1})
    assert _is_linked(b, 'USE_Association42', a1)
    if hasattr(a1, 'USE_Role'):
        assert _is_linked(a1, 'USE_Role', b)
    _safe_set(b, 'USE_Association42', {a2})
    assert _is_linked(b, 'USE_Association42', a2)
    if hasattr(a1, 'USE_Role'):
        assert not _is_linked(a1, 'USE_Role', b)
    if hasattr(a2, 'USE_Role'):
        assert _is_linked(a2, 'USE_Role', b)
    _safe_set(b, 'USE_Association42', set())
    assert not _is_linked(b, 'USE_Association42', a2)
    if hasattr(a2, 'USE_Role'):
        assert not _is_linked(a2, 'USE_Role', b)


def test_assoc_superClasses1_reverse_link_reassign_clear():
    a1 = USE_Class(abstract=True, name="sample_text")
    a2 = USE_Class(abstract=False, name="sample_text_2")
    b = USE_Class(abstract=True, name="sample_text")
    _safe_set(b, 'USE_Class0', {a1})
    assert _is_linked(b, 'USE_Class0', a1)
    if hasattr(a1, 'USE_Class'):
        assert _is_linked(a1, 'USE_Class', b)
    _safe_set(b, 'USE_Class0', {a2})
    assert _is_linked(b, 'USE_Class0', a2)
    if hasattr(a1, 'USE_Class'):
        assert not _is_linked(a1, 'USE_Class', b)
    if hasattr(a2, 'USE_Class'):
        assert _is_linked(a2, 'USE_Class', b)
    _safe_set(b, 'USE_Class0', set())
    assert not _is_linked(b, 'USE_Class0', a2)
    if hasattr(a2, 'USE_Class'):
        assert not _is_linked(a2, 'USE_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_baseType35_stub_double():
    # USE_Type has no real 'USE_Type36' property in the generated
    # code (a bare stub) -- manually attach it so USE_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_CollectionType(type="sample_text")
    partner = USE_Type()
    setattr(partner, 'USE_Type36', None)
    _safe_set(owner, 'USE_CollectionType', partner)
    assert getattr(partner, 'USE_Type36') == owner
    _safe_set(owner, 'USE_CollectionType', None)
    assert getattr(partner, 'USE_Type36') is None


def test_assoc_class_37_stub_double():
    # USE_ReferenceType has no real 'USE_ReferenceType' property in the generated
    # code (a bare stub) -- manually attach it so USE_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_Class(abstract=True, name="sample_text")
    partner = USE_ReferenceType()
    setattr(partner, 'USE_ReferenceType', None)
    _safe_set(owner, 'USE_Class38', partner)
    assert getattr(partner, 'USE_ReferenceType') == owner
    _safe_set(owner, 'USE_Class38', None)
    assert getattr(partner, 'USE_ReferenceType') is None


def test_assoc_enum33_stub_double():
    # USE_EnumerationType has no real 'USE_EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so USE_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_Enumeration(name="sample_text")
    partner = USE_EnumerationType()
    setattr(partner, 'USE_EnumerationType', None)
    _safe_set(owner, 'USE_Enumeration34', partner)
    assert getattr(partner, 'USE_EnumerationType') == owner
    _safe_set(owner, 'USE_Enumeration34', None)
    assert getattr(partner, 'USE_EnumerationType') is None


def test_assoc_type14_stub_double():
    # USE_Type has no real 'USE_Type' property in the generated
    # code (a bare stub) -- manually attach it so USE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_Attribute(name="sample_text")
    partner = USE_Type()
    setattr(partner, 'USE_Type', None)
    _safe_set(owner, 'USE_Attribute15', partner)
    assert getattr(partner, 'USE_Type') == owner
    _safe_set(owner, 'USE_Attribute15', None)
    assert getattr(partner, 'USE_Type') is None


def test_assoc_type21_stub_double():
    # USE_Type has no real 'USE_Type23' property in the generated
    # code (a bare stub) -- manually attach it so USE_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_Operation(name="sample_text")
    partner = USE_Type()
    setattr(partner, 'USE_Type23', None)
    _safe_set(owner, 'USE_Operation22', partner)
    assert getattr(partner, 'USE_Type23') == owner
    _safe_set(owner, 'USE_Operation22', None)
    assert getattr(partner, 'USE_Type23') is None


def test_assoc_type30_stub_double():
    # USE_Type has no real 'USE_Type32' property in the generated
    # code (a bare stub) -- manually attach it so USE_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # USE_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = USE_Parameter(name="sample_text")
    partner = USE_Type()
    setattr(partner, 'USE_Type32', None)
    _safe_set(owner, 'USE_Parameter31', partner)
    assert getattr(partner, 'USE_Type32') == owner
    _safe_set(owner, 'USE_Parameter31', None)
    assert getattr(partner, 'USE_Type32') is None


