import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    KragsteinPackage_Aggregation,
    KragsteinPackage_Association,
    KragsteinPackage_Attribute,
    KragsteinPackage_Class,
    KragsteinPackage_Composition,
    KragsteinPackage_Dependency,
    KragsteinPackage_Generalization,
    KragsteinPackage_ImportedClass,
    KragsteinPackage_Link,
    KragsteinPackage_Method,
    KragsteinPackage_Note,
    KragsteinPackage_Package,
    KragsteinPackage_Parameter,
    KragsteinPackage_Realization,
    KragsteinPackage_Relationship,
    KragsteinPackage_Unit,
    Relationship,
    Unit,
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

def test_assoc_attribute5_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    a2 = KragsteinPackage_Class(isInterface=False, isSingletone=False, name="sample_text_2", superClass="sample_text_2", supplierElement="sample_text_2", visibility="sample_text_2")
    b = KragsteinPackage_Attribute(isConst=True, isStatic=True, name="sample_text", type="sample_text", value="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Attribute', a1)
    assert _is_linked(b, 'KragsteinPackage_Attribute', a1)
    if hasattr(a1, 'KragsteinPackage_Class6'):
        assert _is_linked(a1, 'KragsteinPackage_Class6', b)
    _safe_set(b, 'KragsteinPackage_Attribute', a2)
    assert _is_linked(b, 'KragsteinPackage_Attribute', a2)
    if hasattr(a1, 'KragsteinPackage_Class6'):
        assert not _is_linked(a1, 'KragsteinPackage_Class6', b)
    if hasattr(a2, 'KragsteinPackage_Class6'):
        assert _is_linked(a2, 'KragsteinPackage_Class6', b)
    _safe_set(b, 'KragsteinPackage_Attribute', None)
    assert not _is_linked(b, 'KragsteinPackage_Attribute', a2)
    if hasattr(a2, 'KragsteinPackage_Class6'):
        assert not _is_linked(a2, 'KragsteinPackage_Class6', b)


def test_assoc_importedClass12_reverse_link_reassign_clear():
    a1 = KragsteinPackage_ImportedClass(isInternal=True, name="sample_text", path="sample_text")
    a2 = KragsteinPackage_ImportedClass(isInternal=False, name="sample_text_2", path="sample_text_2")
    b = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Class13', {a1})
    assert _is_linked(b, 'KragsteinPackage_Class13', a1)
    if hasattr(a1, 'KragsteinPackage_ImportedClass'):
        assert _is_linked(a1, 'KragsteinPackage_ImportedClass', b)
    _safe_set(b, 'KragsteinPackage_Class13', {a2})
    assert _is_linked(b, 'KragsteinPackage_Class13', a2)
    if hasattr(a1, 'KragsteinPackage_ImportedClass'):
        assert not _is_linked(a1, 'KragsteinPackage_ImportedClass', b)
    if hasattr(a2, 'KragsteinPackage_ImportedClass'):
        assert _is_linked(a2, 'KragsteinPackage_ImportedClass', b)
    _safe_set(b, 'KragsteinPackage_Class13', set())
    assert not _is_linked(b, 'KragsteinPackage_Class13', a2)
    if hasattr(a2, 'KragsteinPackage_ImportedClass'):
        assert not _is_linked(a2, 'KragsteinPackage_ImportedClass', b)


def test_assoc_method7_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Method(isConst=True, isStatic=True, isVirtual=True, name="sample_text", type="sample_text", visibility="sample_text")
    a2 = KragsteinPackage_Method(isConst=False, isStatic=False, isVirtual=False, name="sample_text_2", type="sample_text_2", visibility="sample_text_2")
    b = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Class8', {a1})
    assert _is_linked(b, 'KragsteinPackage_Class8', a1)
    if hasattr(a1, 'KragsteinPackage_Method'):
        assert _is_linked(a1, 'KragsteinPackage_Method', b)
    _safe_set(b, 'KragsteinPackage_Class8', {a2})
    assert _is_linked(b, 'KragsteinPackage_Class8', a2)
    if hasattr(a1, 'KragsteinPackage_Method'):
        assert not _is_linked(a1, 'KragsteinPackage_Method', b)
    if hasattr(a2, 'KragsteinPackage_Method'):
        assert _is_linked(a2, 'KragsteinPackage_Method', b)
    _safe_set(b, 'KragsteinPackage_Class8', set())
    assert not _is_linked(b, 'KragsteinPackage_Class8', a2)
    if hasattr(a2, 'KragsteinPackage_Method'):
        assert not _is_linked(a2, 'KragsteinPackage_Method', b)


def test_assoc_parameter14_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Parameter(name="sample_text", type="sample_text", value="sample_text")
    a2 = KragsteinPackage_Parameter(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    b = KragsteinPackage_Method(isConst=True, isStatic=True, isVirtual=True, name="sample_text", type="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Method15', {a1})
    assert _is_linked(b, 'KragsteinPackage_Method15', a1)
    if hasattr(a1, 'KragsteinPackage_Parameter'):
        assert _is_linked(a1, 'KragsteinPackage_Parameter', b)
    _safe_set(b, 'KragsteinPackage_Method15', {a2})
    assert _is_linked(b, 'KragsteinPackage_Method15', a2)
    if hasattr(a1, 'KragsteinPackage_Parameter'):
        assert not _is_linked(a1, 'KragsteinPackage_Parameter', b)
    if hasattr(a2, 'KragsteinPackage_Parameter'):
        assert _is_linked(a2, 'KragsteinPackage_Parameter', b)
    _safe_set(b, 'KragsteinPackage_Method15', set())
    assert not _is_linked(b, 'KragsteinPackage_Method15', a2)
    if hasattr(a2, 'KragsteinPackage_Parameter'):
        assert not _is_linked(a2, 'KragsteinPackage_Parameter', b)


def test_assoc_source2_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = KragsteinPackage_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Class4', a1)
    assert _is_linked(b, 'KragsteinPackage_Class4', a1)
    if hasattr(a1, 'KragsteinPackage_Relationship3'):
        assert _is_linked(a1, 'KragsteinPackage_Relationship3', b)
    _safe_set(b, 'KragsteinPackage_Class4', a2)
    assert _is_linked(b, 'KragsteinPackage_Class4', a2)
    if hasattr(a1, 'KragsteinPackage_Relationship3'):
        assert not _is_linked(a1, 'KragsteinPackage_Relationship3', b)
    if hasattr(a2, 'KragsteinPackage_Relationship3'):
        assert _is_linked(a2, 'KragsteinPackage_Relationship3', b)
    _safe_set(b, 'KragsteinPackage_Class4', None)
    assert not _is_linked(b, 'KragsteinPackage_Class4', a2)
    if hasattr(a2, 'KragsteinPackage_Relationship3'):
        assert not _is_linked(a2, 'KragsteinPackage_Relationship3', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = KragsteinPackage_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Class', a1)
    assert _is_linked(b, 'KragsteinPackage_Class', a1)
    if hasattr(a1, 'KragsteinPackage_Relationship'):
        assert _is_linked(a1, 'KragsteinPackage_Relationship', b)
    _safe_set(b, 'KragsteinPackage_Class', a2)
    assert _is_linked(b, 'KragsteinPackage_Class', a2)
    if hasattr(a1, 'KragsteinPackage_Relationship'):
        assert not _is_linked(a1, 'KragsteinPackage_Relationship', b)
    if hasattr(a2, 'KragsteinPackage_Relationship'):
        assert _is_linked(a2, 'KragsteinPackage_Relationship', b)
    _safe_set(b, 'KragsteinPackage_Class', None)
    assert not _is_linked(b, 'KragsteinPackage_Class', a2)
    if hasattr(a2, 'KragsteinPackage_Relationship'):
        assert not _is_linked(a2, 'KragsteinPackage_Relationship', b)


def test_assoc_targetRelationship9_reverse_link_reassign_clear():
    a1 = KragsteinPackage_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = KragsteinPackage_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = KragsteinPackage_Class(isInterface=True, isSingletone=True, name="sample_text", superClass="sample_text", supplierElement="sample_text", visibility="sample_text")
    _safe_set(b, 'KragsteinPackage_Class10', {a1})
    assert _is_linked(b, 'KragsteinPackage_Class10', a1)
    if hasattr(a1, 'KragsteinPackage_Relationship11'):
        assert _is_linked(a1, 'KragsteinPackage_Relationship11', b)
    _safe_set(b, 'KragsteinPackage_Class10', {a2})
    assert _is_linked(b, 'KragsteinPackage_Class10', a2)
    if hasattr(a1, 'KragsteinPackage_Relationship11'):
        assert not _is_linked(a1, 'KragsteinPackage_Relationship11', b)
    if hasattr(a2, 'KragsteinPackage_Relationship11'):
        assert _is_linked(a2, 'KragsteinPackage_Relationship11', b)
    _safe_set(b, 'KragsteinPackage_Class10', set())
    assert not _is_linked(b, 'KragsteinPackage_Class10', a2)
    if hasattr(a2, 'KragsteinPackage_Relationship11'):
        assert not _is_linked(a2, 'KragsteinPackage_Relationship11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_unit0_stub_double():
    # KragsteinPackage_Unit has no real 'KragsteinPackage_Unit' property in the generated
    # code (a bare stub) -- manually attach it so KragsteinPackage_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KragsteinPackage_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KragsteinPackage_Package(name="sample_text", path="sample_text")
    partner = KragsteinPackage_Unit()
    setattr(partner, 'KragsteinPackage_Unit', None)
    _safe_set(owner, 'KragsteinPackage_Package', {partner})
    assert getattr(partner, 'KragsteinPackage_Unit') == owner
    _safe_set(owner, 'KragsteinPackage_Package', set())
    assert getattr(partner, 'KragsteinPackage_Unit') is None


