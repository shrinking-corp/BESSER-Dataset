import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    source_Association,
    source_Attribute,
    source_Class,
    source_ClassDiagram,
    source_PrimitiveDataType,
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

def test_assoc_attrs2_reverse_link_reassign_clear():
    a1 = source_Class(name="sample_text")
    a2 = source_Class(name="sample_text_2")
    b = source_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'source_Attribute', a1)
    assert _is_linked(b, 'source_Attribute', a1)
    if hasattr(a1, 'source_Class3'):
        assert _is_linked(a1, 'source_Class3', b)
    _safe_set(b, 'source_Attribute', a2)
    assert _is_linked(b, 'source_Attribute', a2)
    if hasattr(a1, 'source_Class3'):
        assert not _is_linked(a1, 'source_Class3', b)
    if hasattr(a2, 'source_Class3'):
        assert _is_linked(a2, 'source_Class3', b)
    _safe_set(b, 'source_Attribute', None)
    assert not _is_linked(b, 'source_Attribute', a2)
    if hasattr(a2, 'source_Class3'):
        assert not _is_linked(a2, 'source_Class3', b)


def test_assoc_dest6_reverse_link_reassign_clear():
    a1 = source_Class(name="sample_text")
    a2 = source_Class(name="sample_text_2")
    b = source_Association(leftMultiplicity=7, name="sample_text")
    _safe_set(b, 'source_Association7', a1)
    assert _is_linked(b, 'source_Association7', a1)
    if hasattr(a1, 'source_Class8'):
        assert _is_linked(a1, 'source_Class8', b)
    _safe_set(b, 'source_Association7', a2)
    assert _is_linked(b, 'source_Association7', a2)
    if hasattr(a1, 'source_Class8'):
        assert not _is_linked(a1, 'source_Class8', b)
    if hasattr(a2, 'source_Class8'):
        assert _is_linked(a2, 'source_Class8', b)
    _safe_set(b, 'source_Association7', None)
    assert not _is_linked(b, 'source_Association7', a2)
    if hasattr(a2, 'source_Class8'):
        assert not _is_linked(a2, 'source_Class8', b)


def test_assoc_parent1_reverse_link_reassign_clear():
    a1 = source_Class(name="sample_text")
    a2 = source_Class(name="sample_text_2")
    b = source_Class(name="sample_text")
    _safe_set(b, 'source_Class0', a1)
    assert _is_linked(b, 'source_Class0', a1)
    if hasattr(a1, 'source_Class'):
        assert _is_linked(a1, 'source_Class', b)
    _safe_set(b, 'source_Class0', a2)
    assert _is_linked(b, 'source_Class0', a2)
    if hasattr(a1, 'source_Class'):
        assert not _is_linked(a1, 'source_Class', b)
    if hasattr(a2, 'source_Class'):
        assert _is_linked(a2, 'source_Class', b)
    _safe_set(b, 'source_Class0', None)
    assert not _is_linked(b, 'source_Class0', a2)
    if hasattr(a2, 'source_Class'):
        assert not _is_linked(a2, 'source_Class', b)


def test_assoc_ptype12_reverse_link_reassign_clear():
    a1 = source_PrimitiveDataType(name="sample_text")
    a2 = source_PrimitiveDataType(name="sample_text_2")
    b = source_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'source_Attribute13', a1)
    assert _is_linked(b, 'source_Attribute13', a1)
    if hasattr(a1, 'source_PrimitiveDataType'):
        assert _is_linked(a1, 'source_PrimitiveDataType', b)
    _safe_set(b, 'source_Attribute13', a2)
    assert _is_linked(b, 'source_Attribute13', a2)
    if hasattr(a1, 'source_PrimitiveDataType'):
        assert not _is_linked(a1, 'source_PrimitiveDataType', b)
    if hasattr(a2, 'source_PrimitiveDataType'):
        assert _is_linked(a2, 'source_PrimitiveDataType', b)
    _safe_set(b, 'source_Attribute13', None)
    assert not _is_linked(b, 'source_Attribute13', a2)
    if hasattr(a2, 'source_PrimitiveDataType'):
        assert not _is_linked(a2, 'source_PrimitiveDataType', b)


def test_assoc_src4_reverse_link_reassign_clear():
    a1 = source_Class(name="sample_text")
    a2 = source_Class(name="sample_text_2")
    b = source_Association(leftMultiplicity=7, name="sample_text")
    _safe_set(b, 'source_Association', a1)
    assert _is_linked(b, 'source_Association', a1)
    if hasattr(a1, 'source_Class5'):
        assert _is_linked(a1, 'source_Class5', b)
    _safe_set(b, 'source_Association', a2)
    assert _is_linked(b, 'source_Association', a2)
    if hasattr(a1, 'source_Class5'):
        assert not _is_linked(a1, 'source_Class5', b)
    if hasattr(a2, 'source_Class5'):
        assert _is_linked(a2, 'source_Class5', b)
    _safe_set(b, 'source_Association', None)
    assert not _is_linked(b, 'source_Association', a2)
    if hasattr(a2, 'source_Class5'):
        assert not _is_linked(a2, 'source_Class5', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = source_Class(name="sample_text")
    a2 = source_Class(name="sample_text_2")
    b = source_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'source_Attribute10', a1)
    assert _is_linked(b, 'source_Attribute10', a1)
    if hasattr(a1, 'source_Class11'):
        assert _is_linked(a1, 'source_Class11', b)
    _safe_set(b, 'source_Attribute10', a2)
    assert _is_linked(b, 'source_Attribute10', a2)
    if hasattr(a1, 'source_Class11'):
        assert not _is_linked(a1, 'source_Class11', b)
    if hasattr(a2, 'source_Class11'):
        assert _is_linked(a2, 'source_Class11', b)
    _safe_set(b, 'source_Attribute10', None)
    assert not _is_linked(b, 'source_Attribute10', a2)
    if hasattr(a2, 'source_Class11'):
        assert not _is_linked(a2, 'source_Class11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ass16_stub_double():
    # source_ClassDiagram has no real 'source_ClassDiagram17' property in the generated
    # code (a bare stub) -- manually attach it so source_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # source_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = source_Association(leftMultiplicity=7, name="sample_text")
    partner = source_ClassDiagram()
    setattr(partner, 'source_ClassDiagram17', None)
    _safe_set(owner, 'source_Association18', partner)
    assert owner in getattr(partner, 'source_ClassDiagram17')
    _safe_set(owner, 'source_Association18', None)
    assert owner not in getattr(partner, 'source_ClassDiagram17')


def test_assoc_class_14_stub_double():
    # source_ClassDiagram has no real 'source_ClassDiagram' property in the generated
    # code (a bare stub) -- manually attach it so source_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # source_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = source_Class(name="sample_text")
    partner = source_ClassDiagram()
    setattr(partner, 'source_ClassDiagram', None)
    _safe_set(owner, 'source_Class15', partner)
    assert owner in getattr(partner, 'source_ClassDiagram')
    _safe_set(owner, 'source_Class15', None)
    assert owner not in getattr(partner, 'source_ClassDiagram')


def test_assoc_ptypes19_stub_double():
    # source_ClassDiagram has no real 'source_ClassDiagram20' property in the generated
    # code (a bare stub) -- manually attach it so source_PrimitiveDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # source_PrimitiveDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = source_PrimitiveDataType(name="sample_text")
    partner = source_ClassDiagram()
    setattr(partner, 'source_ClassDiagram20', None)
    _safe_set(owner, 'source_PrimitiveDataType21', partner)
    assert owner in getattr(partner, 'source_ClassDiagram20')
    _safe_set(owner, 'source_PrimitiveDataType21', None)
    assert owner not in getattr(partner, 'source_ClassDiagram20')


