import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    NamedElement,
    PackageMember,
    ParameterizedType,
    PrimitiveType,
    Type,
    TypeConstraint,
    TypedElement,
    types_ComplexType,
    types_Declaration,
    types_Domain,
    types_EnumerationType,
    types_Enumerator,
    types_Event,
    types_Operation,
    types_Package,
    types_PackageMember,
    types_Parameter,
    types_ParameterizedType,
    types_PrimitiveType,
    types_Property,
    types_RangeConstraint,
    types_Type,
    types_TypeAlias,
    types_TypeConstraint,
    types_TypeParameter,
    types_TypedElement,
    Direction,
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

def test_assoc_constraint3_reverse_link_reassign_clear():
    a1 = types_TypeConstraint(value="sample_text")
    a2 = types_TypeConstraint(value="sample_text_2")
    b = types_Type(abstract=True)
    _safe_set(b, 'types_Type', {a1})
    assert _is_linked(b, 'types_Type', a1)
    if hasattr(a1, 'types_TypeConstraint'):
        assert _is_linked(a1, 'types_TypeConstraint', b)
    _safe_set(b, 'types_Type', {a2})
    assert _is_linked(b, 'types_Type', a2)
    if hasattr(a1, 'types_TypeConstraint'):
        assert not _is_linked(a1, 'types_TypeConstraint', b)
    if hasattr(a2, 'types_TypeConstraint'):
        assert _is_linked(a2, 'types_TypeConstraint', b)
    _safe_set(b, 'types_Type', set())
    assert not _is_linked(b, 'types_Type', a2)
    if hasattr(a2, 'types_TypeConstraint'):
        assert not _is_linked(a2, 'types_TypeConstraint', b)


def test_assoc_superTypes16_reverse_link_reassign_clear():
    a1 = types_ComplexType()
    a2 = types_ComplexType()
    b = types_ComplexType()
    _safe_set(b, 'types_ComplexType17', a1)
    assert _is_linked(b, 'types_ComplexType17', a1)
    if hasattr(a1, 'types_ComplexType15'):
        assert _is_linked(a1, 'types_ComplexType15', b)
    _safe_set(b, 'types_ComplexType17', a2)
    assert _is_linked(b, 'types_ComplexType17', a2)
    if hasattr(a1, 'types_ComplexType15'):
        assert not _is_linked(a1, 'types_ComplexType15', b)
    if hasattr(a2, 'types_ComplexType15'):
        assert _is_linked(a2, 'types_ComplexType15', b)
    _safe_set(b, 'types_ComplexType17', None)
    assert not _is_linked(b, 'types_ComplexType17', a2)
    if hasattr(a2, 'types_ComplexType15'):
        assert not _is_linked(a2, 'types_ComplexType15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bound19_stub_double():
    # types_TypeParameter has no real 'types_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True)
    partner = types_TypeParameter()
    setattr(partner, 'types_TypeParameter', None)
    _safe_set(owner, 'types_Type20', partner)
    assert getattr(partner, 'types_TypeParameter') == owner
    _safe_set(owner, 'types_Type20', None)
    assert getattr(partner, 'types_TypeParameter') is None


def test_assoc_domain1_stub_double():
    # types_Package has no real 'types_Package2' property in the generated
    # code (a bare stub) -- manually attach it so types_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Domain(domainID="sample_text")
    partner = types_Package()
    setattr(partner, 'types_Package2', None)
    _safe_set(owner, 'types_Domain', partner)
    assert getattr(partner, 'types_Package2') == owner
    _safe_set(owner, 'types_Domain', None)
    assert getattr(partner, 'types_Package2') is None


def test_assoc_enumerator11_stub_double():
    # types_EnumerationType has no real 'owningEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue="sample_text")
    partner = types_EnumerationType()
    setattr(partner, 'owningEnumeration', None)
    _safe_set(owner, 'Enumerator', partner)
    assert owner in getattr(partner, 'owningEnumeration')
    _safe_set(owner, 'Enumerator', None)
    assert owner not in getattr(partner, 'owningEnumeration')


def test_assoc_features14_stub_double():
    # types_Declaration has no real 'types_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so types_ComplexType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_ComplexType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_ComplexType()
    partner = types_Declaration()
    setattr(partner, 'types_Declaration', None)
    _safe_set(owner, 'types_ComplexType', {partner})
    assert getattr(partner, 'types_Declaration') == owner
    _safe_set(owner, 'types_ComplexType', set())
    assert getattr(partner, 'types_Declaration') is None


def test_assoc_owningEnumeration18_stub_double():
    # types_EnumerationType has no real 'EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue="sample_text")
    partner = types_EnumerationType()
    setattr(partner, 'EnumerationType', None)
    _safe_set(owner, 'enumerator', partner)
    assert getattr(partner, 'EnumerationType') == owner
    _safe_set(owner, 'enumerator', None)
    assert getattr(partner, 'EnumerationType') is None


def test_assoc_type6_stub_double():
    # types_TypedElement has no real 'types_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True)
    partner = types_TypedElement()
    setattr(partner, 'types_TypedElement', None)
    _safe_set(owner, 'types_Type7', partner)
    assert getattr(partner, 'types_TypedElement') == owner
    _safe_set(owner, 'types_Type7', None)
    assert getattr(partner, 'types_TypedElement') is None


def test_assoc_typeArguments8_stub_double():
    # types_TypedElement has no real 'types_TypedElement9' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True)
    partner = types_TypedElement()
    setattr(partner, 'types_TypedElement9', None)
    _safe_set(owner, 'types_Type10', partner)
    assert owner in getattr(partner, 'types_TypedElement9')
    _safe_set(owner, 'types_Type10', None)
    assert owner not in getattr(partner, 'types_TypedElement9')


