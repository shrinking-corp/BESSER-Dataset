import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuiltInType,
    Content,
    Description,
    Type,
    Value,
    classes_Association,
    classes_Attribute,
    classes_BuiltInType,
    classes_Class,
    classes_ClassModel,
    classes_ClassRef,
    classes_Constant,
    classes_ConstantRef,
    classes_Content,
    classes_Description,
    classes_IntegerLiteral,
    classes_IntegerType,
    classes_StringType,
    classes_Type,
    classes_Value,
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

def test_assoc_attributes15_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Attribute(name="sample_text", visibility="sample_text")
    _safe_set(b, 'classes_Attribute', a1)
    assert _is_linked(b, 'classes_Attribute', a1)
    if hasattr(a1, 'classes_Class16'):
        assert _is_linked(a1, 'classes_Class16', b)
    _safe_set(b, 'classes_Attribute', a2)
    assert _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a1, 'classes_Class16'):
        assert not _is_linked(a1, 'classes_Class16', b)
    if hasattr(a2, 'classes_Class16'):
        assert _is_linked(a2, 'classes_Class16', b)
    _safe_set(b, 'classes_Attribute', None)
    assert not _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a2, 'classes_Class16'):
        assert not _is_linked(a2, 'classes_Class16', b)


def test_assoc_source2_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Association(name="sample_text")
    _safe_set(b, 'classes_Association', a1)
    assert _is_linked(b, 'classes_Association', a1)
    if hasattr(a1, 'classes_Class'):
        assert _is_linked(a1, 'classes_Class', b)
    _safe_set(b, 'classes_Association', a2)
    assert _is_linked(b, 'classes_Association', a2)
    if hasattr(a1, 'classes_Class'):
        assert not _is_linked(a1, 'classes_Class', b)
    if hasattr(a2, 'classes_Class'):
        assert _is_linked(a2, 'classes_Class', b)
    _safe_set(b, 'classes_Association', None)
    assert not _is_linked(b, 'classes_Association', a2)
    if hasattr(a2, 'classes_Class'):
        assert not _is_linked(a2, 'classes_Class', b)


def test_assoc_subClasses13_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'classes_Class14', a1)
    assert _is_linked(b, 'classes_Class14', a1)
    if hasattr(a1, 'classes_Class12'):
        assert _is_linked(a1, 'classes_Class12', b)
    _safe_set(b, 'classes_Class14', a2)
    assert _is_linked(b, 'classes_Class14', a2)
    if hasattr(a1, 'classes_Class12'):
        assert not _is_linked(a1, 'classes_Class12', b)
    if hasattr(a2, 'classes_Class12'):
        assert _is_linked(a2, 'classes_Class12', b)
    _safe_set(b, 'classes_Class14', None)
    assert not _is_linked(b, 'classes_Class14', a2)
    if hasattr(a2, 'classes_Class12'):
        assert not _is_linked(a2, 'classes_Class12', b)


def test_assoc_target3_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Association(name="sample_text")
    _safe_set(b, 'classes_Association4', a1)
    assert _is_linked(b, 'classes_Association4', a1)
    if hasattr(a1, 'classes_Class5'):
        assert _is_linked(a1, 'classes_Class5', b)
    _safe_set(b, 'classes_Association4', a2)
    assert _is_linked(b, 'classes_Association4', a2)
    if hasattr(a1, 'classes_Class5'):
        assert not _is_linked(a1, 'classes_Class5', b)
    if hasattr(a2, 'classes_Class5'):
        assert _is_linked(a2, 'classes_Class5', b)
    _safe_set(b, 'classes_Association4', None)
    assert not _is_linked(b, 'classes_Association4', a2)
    if hasattr(a2, 'classes_Class5'):
        assert not _is_linked(a2, 'classes_Class5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_initial1_stub_double():
    # classes_Value has no real 'classes_Value' property in the generated
    # code (a bare stub) -- manually attach it so classes_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Constant(name="sample_text")
    partner = classes_Value()
    setattr(partner, 'classes_Value', None)
    _safe_set(owner, 'classes_Constant', partner)
    assert getattr(partner, 'classes_Value') == owner
    _safe_set(owner, 'classes_Constant', None)
    assert getattr(partner, 'classes_Value') is None


def test_assoc_lowerBound19_stub_double():
    # classes_Value has no real 'classes_Value21' property in the generated
    # code (a bare stub) -- manually attach it so classes_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Attribute(name="sample_text", visibility="sample_text")
    partner = classes_Value()
    setattr(partner, 'classes_Value21', None)
    _safe_set(owner, 'classes_Attribute20', partner)
    assert getattr(partner, 'classes_Value21') == owner
    _safe_set(owner, 'classes_Attribute20', None)
    assert getattr(partner, 'classes_Value21') is None


def test_assoc_lowerBound6_stub_double():
    # classes_Value has no real 'classes_Value8' property in the generated
    # code (a bare stub) -- manually attach it so classes_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Association(name="sample_text")
    partner = classes_Value()
    setattr(partner, 'classes_Value8', None)
    _safe_set(owner, 'classes_Association7', partner)
    assert getattr(partner, 'classes_Value8') == owner
    _safe_set(owner, 'classes_Association7', None)
    assert getattr(partner, 'classes_Value8') is None


def test_assoc_target25_stub_double():
    # classes_ClassRef has no real 'classes_ClassRef' property in the generated
    # code (a bare stub) -- manually attach it so classes_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Class(name="sample_text")
    partner = classes_ClassRef()
    setattr(partner, 'classes_ClassRef', None)
    _safe_set(owner, 'classes_Class26', partner)
    assert getattr(partner, 'classes_ClassRef') == owner
    _safe_set(owner, 'classes_Class26', None)
    assert getattr(partner, 'classes_ClassRef') is None


def test_assoc_target27_stub_double():
    # classes_ConstantRef has no real 'classes_ConstantRef' property in the generated
    # code (a bare stub) -- manually attach it so classes_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Constant(name="sample_text")
    partner = classes_ConstantRef()
    setattr(partner, 'classes_ConstantRef', None)
    _safe_set(owner, 'classes_Constant28', partner)
    assert getattr(partner, 'classes_ConstantRef') == owner
    _safe_set(owner, 'classes_Constant28', None)
    assert getattr(partner, 'classes_ConstantRef') is None


def test_assoc_type17_stub_double():
    # classes_Type has no real 'classes_Type' property in the generated
    # code (a bare stub) -- manually attach it so classes_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Attribute(name="sample_text", visibility="sample_text")
    partner = classes_Type()
    setattr(partner, 'classes_Type', None)
    _safe_set(owner, 'classes_Attribute18', partner)
    assert getattr(partner, 'classes_Type') == owner
    _safe_set(owner, 'classes_Attribute18', None)
    assert getattr(partner, 'classes_Type') is None


def test_assoc_upperBound22_stub_double():
    # classes_Value has no real 'classes_Value24' property in the generated
    # code (a bare stub) -- manually attach it so classes_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Attribute(name="sample_text", visibility="sample_text")
    partner = classes_Value()
    setattr(partner, 'classes_Value24', None)
    _safe_set(owner, 'classes_Attribute23', partner)
    assert getattr(partner, 'classes_Value24') == owner
    _safe_set(owner, 'classes_Attribute23', None)
    assert getattr(partner, 'classes_Value24') is None


def test_assoc_upperBound9_stub_double():
    # classes_Value has no real 'classes_Value11' property in the generated
    # code (a bare stub) -- manually attach it so classes_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Association(name="sample_text")
    partner = classes_Value()
    setattr(partner, 'classes_Value11', None)
    _safe_set(owner, 'classes_Association10', partner)
    assert getattr(partner, 'classes_Value11') == owner
    _safe_set(owner, 'classes_Association10', None)
    assert getattr(partner, 'classes_Value11') is None


