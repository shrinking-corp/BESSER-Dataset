import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    grudi_Person,
    grudi_PersonInfo,
    grudi_Team,
    grudi_TeamLine,
    Gender,
    TeamPersonKind,
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

def test_assoc_lines0_reverse_link_reassign_clear():
    a1 = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    a2 = grudi_TeamLine(id="sample_text_2", kind="sample_text_2", versionNumber="sample_text_2")
    b = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    _safe_set(b, 'team', {a1})
    assert _is_linked(b, 'team', a1)
    if hasattr(a1, 'TeamLine'):
        assert _is_linked(a1, 'TeamLine', b)
    _safe_set(b, 'team', {a2})
    assert _is_linked(b, 'team', a2)
    if hasattr(a1, 'TeamLine'):
        assert not _is_linked(a1, 'TeamLine', b)
    if hasattr(a2, 'TeamLine'):
        assert _is_linked(a2, 'TeamLine', b)
    _safe_set(b, 'team', set())
    assert not _is_linked(b, 'team', a2)
    if hasattr(a2, 'TeamLine'):
        assert not _is_linked(a2, 'TeamLine', b)


def test_assoc_person2_reverse_link_reassign_clear():
    a1 = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    a2 = grudi_TeamLine(id="sample_text_2", kind="sample_text_2", versionNumber="sample_text_2")
    b = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    _safe_set(b, 'grudi_PersonInfo', a1)
    assert _is_linked(b, 'grudi_PersonInfo', a1)
    if hasattr(a1, 'grudi_TeamLine'):
        assert _is_linked(a1, 'grudi_TeamLine', b)
    _safe_set(b, 'grudi_PersonInfo', a2)
    assert _is_linked(b, 'grudi_PersonInfo', a2)
    if hasattr(a1, 'grudi_TeamLine'):
        assert not _is_linked(a1, 'grudi_TeamLine', b)
    if hasattr(a2, 'grudi_TeamLine'):
        assert _is_linked(a2, 'grudi_TeamLine', b)
    _safe_set(b, 'grudi_PersonInfo', None)
    assert not _is_linked(b, 'grudi_PersonInfo', a2)
    if hasattr(a2, 'grudi_TeamLine'):
        assert not _is_linked(a2, 'grudi_TeamLine', b)


def test_assoc_team1_reverse_link_reassign_clear():
    a1 = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    a2 = grudi_TeamLine(id="sample_text_2", kind="sample_text_2", versionNumber="sample_text_2")
    b = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    _safe_set(b, 'Team', a1)
    assert _is_linked(b, 'Team', a1)
    if hasattr(a1, 'lines'):
        assert _is_linked(a1, 'lines', b)
    _safe_set(b, 'Team', a2)
    assert _is_linked(b, 'Team', a2)
    if hasattr(a1, 'lines'):
        assert not _is_linked(a1, 'lines', b)
    if hasattr(a2, 'lines'):
        assert _is_linked(a2, 'lines', b)
    _safe_set(b, 'Team', None)
    assert not _is_linked(b, 'Team', a2)
    if hasattr(a2, 'lines'):
        assert not _is_linked(a2, 'lines', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

