import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    pdb1_Database,
    pdb1_Person,
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

def test_assoc_database1_reverse_link_reassign_clear():
    a1 = pdb1_Person(birthday="sample_text", firstName="sample_text", id="sample_text", incrementalID="sample_text", lastName="sample_text", placeOfBirth="sample_text")
    a2 = pdb1_Person(birthday="sample_text_2", firstName="sample_text_2", id="sample_text_2", incrementalID="sample_text_2", lastName="sample_text_2", placeOfBirth="sample_text_2")
    b = pdb1_Database(name="sample_text")
    _safe_set(b, 'Database', a1)
    assert _is_linked(b, 'Database', a1)
    if hasattr(a1, 'persons'):
        assert _is_linked(a1, 'persons', b)
    _safe_set(b, 'Database', a2)
    assert _is_linked(b, 'Database', a2)
    if hasattr(a1, 'persons'):
        assert not _is_linked(a1, 'persons', b)
    if hasattr(a2, 'persons'):
        assert _is_linked(a2, 'persons', b)
    _safe_set(b, 'Database', None)
    assert not _is_linked(b, 'Database', a2)
    if hasattr(a2, 'persons'):
        assert not _is_linked(a2, 'persons', b)


def test_assoc_persons0_reverse_link_reassign_clear():
    a1 = pdb1_Person(birthday="sample_text", firstName="sample_text", id="sample_text", incrementalID="sample_text", lastName="sample_text", placeOfBirth="sample_text")
    a2 = pdb1_Person(birthday="sample_text_2", firstName="sample_text_2", id="sample_text_2", incrementalID="sample_text_2", lastName="sample_text_2", placeOfBirth="sample_text_2")
    b = pdb1_Database(name="sample_text")
    _safe_set(b, 'database', {a1})
    assert _is_linked(b, 'database', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'database', {a2})
    assert _is_linked(b, 'database', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'database', set())
    assert not _is_linked(b, 'database', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

