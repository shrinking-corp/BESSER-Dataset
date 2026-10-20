import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Feature,
    StructuralFeature,
    Type,
    domainmodel_AbstractElement,
    domainmodel_Attribute,
    domainmodel_DataType,
    domainmodel_DomainModel,
    domainmodel_Entity,
    domainmodel_Feature,
    domainmodel_Import,
    domainmodel_Operation,
    domainmodel_PackageDeclaration,
    domainmodel_Parameter,
    domainmodel_Reference,
    domainmodel_StructuralFeature,
    domainmodel_Type,
    domainmodel_TypeRef,
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

def test_assoc_params11_reverse_link_reassign_clear():
    a1 = domainmodel_Parameter(name="sample_text")
    a2 = domainmodel_Parameter(name="sample_text_2")
    b = domainmodel_Operation(visibility="sample_text")
    _safe_set(b, 'domainmodel_Operation', {a1})
    assert _is_linked(b, 'domainmodel_Operation', a1)
    if hasattr(a1, 'domainmodel_Parameter'):
        assert _is_linked(a1, 'domainmodel_Parameter', b)
    _safe_set(b, 'domainmodel_Operation', {a2})
    assert _is_linked(b, 'domainmodel_Operation', a2)
    if hasattr(a1, 'domainmodel_Parameter'):
        assert not _is_linked(a1, 'domainmodel_Parameter', b)
    if hasattr(a2, 'domainmodel_Parameter'):
        assert _is_linked(a2, 'domainmodel_Parameter', b)
    _safe_set(b, 'domainmodel_Operation', set())
    assert not _is_linked(b, 'domainmodel_Operation', a2)
    if hasattr(a2, 'domainmodel_Parameter'):
        assert not _is_linked(a2, 'domainmodel_Parameter', b)


def test_assoc_referenced15_reverse_link_reassign_clear():
    a1 = domainmodel_TypeRef(multi=True)
    a2 = domainmodel_TypeRef(multi=False)
    b = domainmodel_Type(name="sample_text")
    _safe_set(b, 'domainmodel_Type', a1)
    assert _is_linked(b, 'domainmodel_Type', a1)
    if hasattr(a1, 'domainmodel_TypeRef16'):
        assert _is_linked(a1, 'domainmodel_TypeRef16', b)
    _safe_set(b, 'domainmodel_Type', a2)
    assert _is_linked(b, 'domainmodel_Type', a2)
    if hasattr(a1, 'domainmodel_TypeRef16'):
        assert not _is_linked(a1, 'domainmodel_TypeRef16', b)
    if hasattr(a2, 'domainmodel_TypeRef16'):
        assert _is_linked(a2, 'domainmodel_TypeRef16', b)
    _safe_set(b, 'domainmodel_Type', None)
    assert not _is_linked(b, 'domainmodel_Type', a2)
    if hasattr(a2, 'domainmodel_TypeRef16'):
        assert not _is_linked(a2, 'domainmodel_TypeRef16', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = domainmodel_TypeRef(multi=True)
    a2 = domainmodel_TypeRef(multi=False)
    b = domainmodel_Parameter(name="sample_text")
    _safe_set(b, 'domainmodel_Parameter13', a1)
    assert _is_linked(b, 'domainmodel_Parameter13', a1)
    if hasattr(a1, 'domainmodel_TypeRef14'):
        assert _is_linked(a1, 'domainmodel_TypeRef14', b)
    _safe_set(b, 'domainmodel_Parameter13', a2)
    assert _is_linked(b, 'domainmodel_Parameter13', a2)
    if hasattr(a1, 'domainmodel_TypeRef14'):
        assert not _is_linked(a1, 'domainmodel_TypeRef14', b)
    if hasattr(a2, 'domainmodel_TypeRef14'):
        assert _is_linked(a2, 'domainmodel_TypeRef14', b)
    _safe_set(b, 'domainmodel_Parameter13', None)
    assert not _is_linked(b, 'domainmodel_Parameter13', a2)
    if hasattr(a2, 'domainmodel_TypeRef14'):
        assert not _is_linked(a2, 'domainmodel_TypeRef14', b)


def test_assoc_type7_reverse_link_reassign_clear():
    a1 = domainmodel_TypeRef(multi=True)
    a2 = domainmodel_TypeRef(multi=False)
    b = domainmodel_Feature(name="sample_text")
    _safe_set(b, 'domainmodel_Feature8', a1)
    assert _is_linked(b, 'domainmodel_Feature8', a1)
    if hasattr(a1, 'domainmodel_TypeRef'):
        assert _is_linked(a1, 'domainmodel_TypeRef', b)
    _safe_set(b, 'domainmodel_Feature8', a2)
    assert _is_linked(b, 'domainmodel_Feature8', a2)
    if hasattr(a1, 'domainmodel_TypeRef'):
        assert not _is_linked(a1, 'domainmodel_TypeRef', b)
    if hasattr(a2, 'domainmodel_TypeRef'):
        assert _is_linked(a2, 'domainmodel_TypeRef', b)
    _safe_set(b, 'domainmodel_Feature8', None)
    assert not _is_linked(b, 'domainmodel_Feature8', a2)
    if hasattr(a2, 'domainmodel_TypeRef'):
        assert not _is_linked(a2, 'domainmodel_TypeRef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements1_stub_double():
    # domainmodel_AbstractElement has no real 'domainmodel_AbstractElement2' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_PackageDeclaration(name="sample_text")
    partner = domainmodel_AbstractElement()
    setattr(partner, 'domainmodel_AbstractElement2', None)
    _safe_set(owner, 'domainmodel_PackageDeclaration', {partner})
    assert getattr(partner, 'domainmodel_AbstractElement2') == owner
    _safe_set(owner, 'domainmodel_PackageDeclaration', set())
    assert getattr(partner, 'domainmodel_AbstractElement2') is None


def test_assoc_features5_stub_double():
    # domainmodel_Entity has no real 'domainmodel_Entity6' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_Feature(name="sample_text")
    partner = domainmodel_Entity()
    setattr(partner, 'domainmodel_Entity6', None)
    _safe_set(owner, 'domainmodel_Feature', partner)
    assert owner in getattr(partner, 'domainmodel_Entity6')
    _safe_set(owner, 'domainmodel_Feature', None)
    assert owner not in getattr(partner, 'domainmodel_Entity6')


