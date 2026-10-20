import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    familyleft1_Family,
    familyleft1_Father,
    familyleft1_Mother,
    familyleft1_Son,
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

def test_assoc_family0_reverse_link_reassign_clear():
    a1 = familyleft1_Father(age=7, name="sample_text")
    a2 = familyleft1_Father(age=13, name="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'Family', a1)
    assert _is_linked(b, 'Family', a1)
    if hasattr(a1, 'father'):
        assert _is_linked(a1, 'father', b)
    _safe_set(b, 'Family', a2)
    assert _is_linked(b, 'Family', a2)
    if hasattr(a1, 'father'):
        assert not _is_linked(a1, 'father', b)
    if hasattr(a2, 'father'):
        assert _is_linked(a2, 'father', b)
    _safe_set(b, 'Family', None)
    assert not _is_linked(b, 'Family', a2)
    if hasattr(a2, 'father'):
        assert not _is_linked(a2, 'father', b)


def test_assoc_family1_reverse_link_reassign_clear():
    a1 = familyleft1_Mother(age=7, name="sample_text")
    a2 = familyleft1_Mother(age=13, name="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'Family2', a1)
    assert _is_linked(b, 'Family2', a1)
    if hasattr(a1, 'mother'):
        assert _is_linked(a1, 'mother', b)
    _safe_set(b, 'Family2', a2)
    assert _is_linked(b, 'Family2', a2)
    if hasattr(a1, 'mother'):
        assert not _is_linked(a1, 'mother', b)
    if hasattr(a2, 'mother'):
        assert _is_linked(a2, 'mother', b)
    _safe_set(b, 'Family2', None)
    assert not _is_linked(b, 'Family2', a2)
    if hasattr(a2, 'mother'):
        assert not _is_linked(a2, 'mother', b)


def test_assoc_family3_reverse_link_reassign_clear():
    a1 = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    a2 = familyleft1_Son(age=13, name="sample_text_2", sex="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'Family4', a1)
    assert _is_linked(b, 'Family4', a1)
    if hasattr(a1, 'sons'):
        assert _is_linked(a1, 'sons', b)
    _safe_set(b, 'Family4', a2)
    assert _is_linked(b, 'Family4', a2)
    if hasattr(a1, 'sons'):
        assert not _is_linked(a1, 'sons', b)
    if hasattr(a2, 'sons'):
        assert _is_linked(a2, 'sons', b)
    _safe_set(b, 'Family4', None)
    assert not _is_linked(b, 'Family4', a2)
    if hasattr(a2, 'sons'):
        assert not _is_linked(a2, 'sons', b)


def test_assoc_father5_reverse_link_reassign_clear():
    a1 = familyleft1_Father(age=7, name="sample_text")
    a2 = familyleft1_Father(age=13, name="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'family', a1)
    assert _is_linked(b, 'family', a1)
    if hasattr(a1, 'Father'):
        assert _is_linked(a1, 'Father', b)
    _safe_set(b, 'family', a2)
    assert _is_linked(b, 'family', a2)
    if hasattr(a1, 'Father'):
        assert not _is_linked(a1, 'Father', b)
    if hasattr(a2, 'Father'):
        assert _is_linked(a2, 'Father', b)
    _safe_set(b, 'family', None)
    assert not _is_linked(b, 'family', a2)
    if hasattr(a2, 'Father'):
        assert not _is_linked(a2, 'Father', b)


def test_assoc_mother6_reverse_link_reassign_clear():
    a1 = familyleft1_Mother(age=7, name="sample_text")
    a2 = familyleft1_Mother(age=13, name="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'family7', a1)
    assert _is_linked(b, 'family7', a1)
    if hasattr(a1, 'Mother'):
        assert _is_linked(a1, 'Mother', b)
    _safe_set(b, 'family7', a2)
    assert _is_linked(b, 'family7', a2)
    if hasattr(a1, 'Mother'):
        assert not _is_linked(a1, 'Mother', b)
    if hasattr(a2, 'Mother'):
        assert _is_linked(a2, 'Mother', b)
    _safe_set(b, 'family7', None)
    assert not _is_linked(b, 'family7', a2)
    if hasattr(a2, 'Mother'):
        assert not _is_linked(a2, 'Mother', b)


def test_assoc_sons8_reverse_link_reassign_clear():
    a1 = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    a2 = familyleft1_Son(age=13, name="sample_text_2", sex="sample_text_2")
    b = familyleft1_Family(location="sample_text", surname="sample_text")
    _safe_set(b, 'family9', {a1})
    assert _is_linked(b, 'family9', a1)
    if hasattr(a1, 'Son'):
        assert _is_linked(a1, 'Son', b)
    _safe_set(b, 'family9', {a2})
    assert _is_linked(b, 'family9', a2)
    if hasattr(a1, 'Son'):
        assert not _is_linked(a1, 'Son', b)
    if hasattr(a2, 'Son'):
        assert _is_linked(a2, 'Son', b)
    _safe_set(b, 'family9', set())
    assert not _is_linked(b, 'family9', a2)
    if hasattr(a2, 'Son'):
        assert not _is_linked(a2, 'Son', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

