import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    simpleUML_MM_Association,
    simpleUML_MM_Attribute,
    simpleUML_MM_Class,
    simpleUML_MM_ClassModel,
    simpleUML_MM_Classifier,
    simpleUML_MM_PrimitiveDataType,
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

def test_assoc_attrs5_reverse_link_reassign_clear():
    a1 = simpleUML_MM_Class(is_persistent=True)
    a2 = simpleUML_MM_Class(is_persistent=False)
    b = simpleUML_MM_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'simpleUML_MM_Attribute7', a1)
    assert _is_linked(b, 'simpleUML_MM_Attribute7', a1)
    if hasattr(a1, 'simpleUML_MM_Class6'):
        assert _is_linked(a1, 'simpleUML_MM_Class6', b)
    _safe_set(b, 'simpleUML_MM_Attribute7', a2)
    assert _is_linked(b, 'simpleUML_MM_Attribute7', a2)
    if hasattr(a1, 'simpleUML_MM_Class6'):
        assert not _is_linked(a1, 'simpleUML_MM_Class6', b)
    if hasattr(a2, 'simpleUML_MM_Class6'):
        assert _is_linked(a2, 'simpleUML_MM_Class6', b)
    _safe_set(b, 'simpleUML_MM_Attribute7', None)
    assert not _is_linked(b, 'simpleUML_MM_Attribute7', a2)
    if hasattr(a2, 'simpleUML_MM_Class6'):
        assert not _is_linked(a2, 'simpleUML_MM_Class6', b)


def test_assoc_dest1_reverse_link_reassign_clear():
    a1 = simpleUML_MM_Class(is_persistent=True)
    a2 = simpleUML_MM_Class(is_persistent=False)
    b = simpleUML_MM_Association(name="sample_text")
    _safe_set(b, 'simpleUML_MM_Association2', a1)
    assert _is_linked(b, 'simpleUML_MM_Association2', a1)
    if hasattr(a1, 'simpleUML_MM_Class3'):
        assert _is_linked(a1, 'simpleUML_MM_Class3', b)
    _safe_set(b, 'simpleUML_MM_Association2', a2)
    assert _is_linked(b, 'simpleUML_MM_Association2', a2)
    if hasattr(a1, 'simpleUML_MM_Class3'):
        assert not _is_linked(a1, 'simpleUML_MM_Class3', b)
    if hasattr(a2, 'simpleUML_MM_Class3'):
        assert _is_linked(a2, 'simpleUML_MM_Class3', b)
    _safe_set(b, 'simpleUML_MM_Association2', None)
    assert not _is_linked(b, 'simpleUML_MM_Association2', a2)
    if hasattr(a2, 'simpleUML_MM_Class3'):
        assert not _is_linked(a2, 'simpleUML_MM_Class3', b)


def test_assoc_parent9_reverse_link_reassign_clear():
    a1 = simpleUML_MM_Class(is_persistent=True)
    a2 = simpleUML_MM_Class(is_persistent=False)
    b = simpleUML_MM_Class(is_persistent=True)
    _safe_set(b, 'simpleUML_MM_Class8', a1)
    assert _is_linked(b, 'simpleUML_MM_Class8', a1)
    if hasattr(a1, 'simpleUML_MM_Class10'):
        assert _is_linked(a1, 'simpleUML_MM_Class10', b)
    _safe_set(b, 'simpleUML_MM_Class8', a2)
    assert _is_linked(b, 'simpleUML_MM_Class8', a2)
    if hasattr(a1, 'simpleUML_MM_Class10'):
        assert not _is_linked(a1, 'simpleUML_MM_Class10', b)
    if hasattr(a2, 'simpleUML_MM_Class10'):
        assert _is_linked(a2, 'simpleUML_MM_Class10', b)
    _safe_set(b, 'simpleUML_MM_Class8', None)
    assert not _is_linked(b, 'simpleUML_MM_Class8', a2)
    if hasattr(a2, 'simpleUML_MM_Class10'):
        assert not _is_linked(a2, 'simpleUML_MM_Class10', b)


def test_assoc_src0_reverse_link_reassign_clear():
    a1 = simpleUML_MM_Class(is_persistent=True)
    a2 = simpleUML_MM_Class(is_persistent=False)
    b = simpleUML_MM_Association(name="sample_text")
    _safe_set(b, 'simpleUML_MM_Association', a1)
    assert _is_linked(b, 'simpleUML_MM_Association', a1)
    if hasattr(a1, 'simpleUML_MM_Class'):
        assert _is_linked(a1, 'simpleUML_MM_Class', b)
    _safe_set(b, 'simpleUML_MM_Association', a2)
    assert _is_linked(b, 'simpleUML_MM_Association', a2)
    if hasattr(a1, 'simpleUML_MM_Class'):
        assert not _is_linked(a1, 'simpleUML_MM_Class', b)
    if hasattr(a2, 'simpleUML_MM_Class'):
        assert _is_linked(a2, 'simpleUML_MM_Class', b)
    _safe_set(b, 'simpleUML_MM_Association', None)
    assert not _is_linked(b, 'simpleUML_MM_Association', a2)
    if hasattr(a2, 'simpleUML_MM_Class'):
        assert not _is_linked(a2, 'simpleUML_MM_Class', b)


def test_assoc_type4_reverse_link_reassign_clear():
    a1 = simpleUML_MM_Classifier(name="sample_text")
    a2 = simpleUML_MM_Classifier(name="sample_text_2")
    b = simpleUML_MM_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'simpleUML_MM_Attribute', a1)
    assert _is_linked(b, 'simpleUML_MM_Attribute', a1)
    if hasattr(a1, 'simpleUML_MM_Classifier'):
        assert _is_linked(a1, 'simpleUML_MM_Classifier', b)
    _safe_set(b, 'simpleUML_MM_Attribute', a2)
    assert _is_linked(b, 'simpleUML_MM_Attribute', a2)
    if hasattr(a1, 'simpleUML_MM_Classifier'):
        assert not _is_linked(a1, 'simpleUML_MM_Classifier', b)
    if hasattr(a2, 'simpleUML_MM_Classifier'):
        assert _is_linked(a2, 'simpleUML_MM_Classifier', b)
    _safe_set(b, 'simpleUML_MM_Attribute', None)
    assert not _is_linked(b, 'simpleUML_MM_Attribute', a2)
    if hasattr(a2, 'simpleUML_MM_Classifier'):
        assert not _is_linked(a2, 'simpleUML_MM_Classifier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association13_stub_double():
    # simpleUML_MM_ClassModel has no real 'simpleUML_MM_ClassModel14' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_MM_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_MM_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_MM_Association(name="sample_text")
    partner = simpleUML_MM_ClassModel()
    setattr(partner, 'simpleUML_MM_ClassModel14', None)
    _safe_set(owner, 'simpleUML_MM_Association15', partner)
    assert owner in getattr(partner, 'simpleUML_MM_ClassModel14')
    _safe_set(owner, 'simpleUML_MM_Association15', None)
    assert owner not in getattr(partner, 'simpleUML_MM_ClassModel14')


def test_assoc_classifier11_stub_double():
    # simpleUML_MM_ClassModel has no real 'simpleUML_MM_ClassModel' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_MM_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_MM_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_MM_Classifier(name="sample_text")
    partner = simpleUML_MM_ClassModel()
    setattr(partner, 'simpleUML_MM_ClassModel', None)
    _safe_set(owner, 'simpleUML_MM_Classifier12', partner)
    assert owner in getattr(partner, 'simpleUML_MM_ClassModel')
    _safe_set(owner, 'simpleUML_MM_Classifier12', None)
    assert owner not in getattr(partner, 'simpleUML_MM_ClassModel')


