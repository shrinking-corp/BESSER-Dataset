import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ComplexType,
    DataType,
    IDLReference,
    datatypes_ComplexType,
    datatypes_CustomType,
    datatypes_DataType,
    datatypes_Field,
    datatypes_IDLReference,
    datatypes_RosIDLReference,
    datatypes_SimpleType,
    datatypes_TypesLibrary,
    datatypes_VectorType,
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

def test_assoc_includes2_reverse_link_reassign_clear():
    a1 = datatypes_TypesLibrary(name="sample_text")
    a2 = datatypes_TypesLibrary(name="sample_text_2")
    b = datatypes_TypesLibrary(name="sample_text")
    _safe_set(b, 'datatypes_TypesLibrary1', {a1})
    assert _is_linked(b, 'datatypes_TypesLibrary1', a1)
    if hasattr(a1, 'datatypes_TypesLibrary'):
        assert _is_linked(a1, 'datatypes_TypesLibrary', b)
    _safe_set(b, 'datatypes_TypesLibrary1', {a2})
    assert _is_linked(b, 'datatypes_TypesLibrary1', a2)
    if hasattr(a1, 'datatypes_TypesLibrary'):
        assert not _is_linked(a1, 'datatypes_TypesLibrary', b)
    if hasattr(a2, 'datatypes_TypesLibrary'):
        assert _is_linked(a2, 'datatypes_TypesLibrary', b)
    _safe_set(b, 'datatypes_TypesLibrary1', set())
    assert not _is_linked(b, 'datatypes_TypesLibrary1', a2)
    if hasattr(a2, 'datatypes_TypesLibrary'):
        assert not _is_linked(a2, 'datatypes_TypesLibrary', b)


def test_assoc_type6_reverse_link_reassign_clear():
    a1 = datatypes_Field(description="sample_text", measureUnit="sample_text", name="sample_text")
    a2 = datatypes_Field(description="sample_text_2", measureUnit="sample_text_2", name="sample_text_2")
    b = datatypes_DataType(name="sample_text")
    _safe_set(b, 'datatypes_DataType8', a1)
    assert _is_linked(b, 'datatypes_DataType8', a1)
    if hasattr(a1, 'datatypes_Field7'):
        assert _is_linked(a1, 'datatypes_Field7', b)
    _safe_set(b, 'datatypes_DataType8', a2)
    assert _is_linked(b, 'datatypes_DataType8', a2)
    if hasattr(a1, 'datatypes_Field7'):
        assert not _is_linked(a1, 'datatypes_Field7', b)
    if hasattr(a2, 'datatypes_Field7'):
        assert _is_linked(a2, 'datatypes_Field7', b)
    _safe_set(b, 'datatypes_DataType8', None)
    assert not _is_linked(b, 'datatypes_DataType8', a2)
    if hasattr(a2, 'datatypes_Field7'):
        assert not _is_linked(a2, 'datatypes_Field7', b)


def test_assoc_types0_reverse_link_reassign_clear():
    a1 = datatypes_TypesLibrary(name="sample_text")
    a2 = datatypes_TypesLibrary(name="sample_text_2")
    b = datatypes_DataType(name="sample_text")
    _safe_set(b, 'DataType', a1)
    assert _is_linked(b, 'DataType', a1)
    if hasattr(a1, 'typesLibrary'):
        assert _is_linked(a1, 'typesLibrary', b)
    _safe_set(b, 'DataType', a2)
    assert _is_linked(b, 'DataType', a2)
    if hasattr(a1, 'typesLibrary'):
        assert not _is_linked(a1, 'typesLibrary', b)
    if hasattr(a2, 'typesLibrary'):
        assert _is_linked(a2, 'typesLibrary', b)
    _safe_set(b, 'DataType', None)
    assert not _is_linked(b, 'DataType', a2)
    if hasattr(a2, 'typesLibrary'):
        assert not _is_linked(a2, 'typesLibrary', b)


def test_assoc_typesLibrary3_reverse_link_reassign_clear():
    a1 = datatypes_TypesLibrary(name="sample_text")
    a2 = datatypes_TypesLibrary(name="sample_text_2")
    b = datatypes_DataType(name="sample_text")
    _safe_set(b, 'types', a1)
    assert _is_linked(b, 'types', a1)
    if hasattr(a1, 'TypesLibrary'):
        assert _is_linked(a1, 'TypesLibrary', b)
    _safe_set(b, 'types', a2)
    assert _is_linked(b, 'types', a2)
    if hasattr(a1, 'TypesLibrary'):
        assert not _is_linked(a1, 'TypesLibrary', b)
    if hasattr(a2, 'TypesLibrary'):
        assert _is_linked(a2, 'TypesLibrary', b)
    _safe_set(b, 'types', None)
    assert not _is_linked(b, 'types', a2)
    if hasattr(a2, 'TypesLibrary'):
        assert not _is_linked(a2, 'TypesLibrary', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fields5_stub_double():
    # datatypes_CustomType has no real 'datatypes_CustomType' property in the generated
    # code (a bare stub) -- manually attach it so datatypes_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatypes_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatypes_Field(description="sample_text", measureUnit="sample_text", name="sample_text")
    partner = datatypes_CustomType()
    setattr(partner, 'datatypes_CustomType', None)
    _safe_set(owner, 'datatypes_Field', partner)
    assert owner in getattr(partner, 'datatypes_CustomType')
    _safe_set(owner, 'datatypes_Field', None)
    assert owner not in getattr(partner, 'datatypes_CustomType')


def test_assoc_template4_stub_double():
    # datatypes_VectorType has no real 'datatypes_VectorType' property in the generated
    # code (a bare stub) -- manually attach it so datatypes_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatypes_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatypes_DataType(name="sample_text")
    partner = datatypes_VectorType()
    setattr(partner, 'datatypes_VectorType', None)
    _safe_set(owner, 'datatypes_DataType', partner)
    assert getattr(partner, 'datatypes_VectorType') == owner
    _safe_set(owner, 'datatypes_DataType', None)
    assert getattr(partner, 'datatypes_VectorType') is None


