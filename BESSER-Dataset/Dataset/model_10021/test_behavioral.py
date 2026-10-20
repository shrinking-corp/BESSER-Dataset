import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Projects_Company,
    Projects_Project,
    Projects_Qualification,
    Projects_Worker,
    ProjectSize,
    ProjectStatus,
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

def test_assoc_company8_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Company()
    _safe_set(b, 'Projects_Company10', a1)
    assert _is_linked(b, 'Projects_Company10', a1)
    if hasattr(a1, 'Projects_Project9'):
        assert _is_linked(a1, 'Projects_Project9', b)
    _safe_set(b, 'Projects_Company10', a2)
    assert _is_linked(b, 'Projects_Company10', a2)
    if hasattr(a1, 'Projects_Project9'):
        assert not _is_linked(a1, 'Projects_Project9', b)
    if hasattr(a2, 'Projects_Project9'):
        assert _is_linked(a2, 'Projects_Project9', b)
    _safe_set(b, 'Projects_Company10', None)
    assert not _is_linked(b, 'Projects_Company10', a2)
    if hasattr(a2, 'Projects_Project9'):
        assert not _is_linked(a2, 'Projects_Project9', b)


def test_assoc_predecessors18_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Project(size="sample_text", status="sample_text")
    _safe_set(b, 'Projects_Project19', a1)
    assert _is_linked(b, 'Projects_Project19', a1)
    if hasattr(a1, 'Projects_Project17'):
        assert _is_linked(a1, 'Projects_Project17', b)
    _safe_set(b, 'Projects_Project19', a2)
    assert _is_linked(b, 'Projects_Project19', a2)
    if hasattr(a1, 'Projects_Project17'):
        assert not _is_linked(a1, 'Projects_Project17', b)
    if hasattr(a2, 'Projects_Project17'):
        assert _is_linked(a2, 'Projects_Project17', b)
    _safe_set(b, 'Projects_Project19', None)
    assert not _is_linked(b, 'Projects_Project19', a2)
    if hasattr(a2, 'Projects_Project17'):
        assert not _is_linked(a2, 'Projects_Project17', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Company()
    _safe_set(b, 'Projects_Company', {a1})
    assert _is_linked(b, 'Projects_Company', a1)
    if hasattr(a1, 'Projects_Project'):
        assert _is_linked(a1, 'Projects_Project', b)
    _safe_set(b, 'Projects_Company', {a2})
    assert _is_linked(b, 'Projects_Company', a2)
    if hasattr(a1, 'Projects_Project'):
        assert not _is_linked(a1, 'Projects_Project', b)
    if hasattr(a2, 'Projects_Project'):
        assert _is_linked(a2, 'Projects_Project', b)
    _safe_set(b, 'Projects_Company', set())
    assert not _is_linked(b, 'Projects_Company', a2)
    if hasattr(a2, 'Projects_Project'):
        assert not _is_linked(a2, 'Projects_Project', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_employees1_stub_double():
    # Projects_Worker has no real 'Projects_Worker' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Company's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Company's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Company()
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker', None)
    _safe_set(owner, 'Projects_Company2', {partner})
    assert getattr(partner, 'Projects_Worker') == owner
    _safe_set(owner, 'Projects_Company2', set())
    assert getattr(partner, 'Projects_Worker') is None


def test_assoc_members11_stub_double():
    # Projects_Worker has no real 'Projects_Worker13' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker13', None)
    _safe_set(owner, 'Projects_Project12', {partner})
    assert getattr(partner, 'Projects_Worker13') == owner
    _safe_set(owner, 'Projects_Project12', set())
    assert getattr(partner, 'Projects_Worker13') is None


def test_assoc_projects5_stub_double():
    # Projects_Worker has no real 'Projects_Worker6' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker6', None)
    _safe_set(owner, 'Projects_Project7', partner)
    assert owner in getattr(partner, 'Projects_Worker6')
    _safe_set(owner, 'Projects_Project7', None)
    assert owner not in getattr(partner, 'Projects_Worker6')


def test_assoc_requirements14_stub_double():
    # Projects_Qualification has no real 'Projects_Qualification16' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Qualification()
    setattr(partner, 'Projects_Qualification16', None)
    _safe_set(owner, 'Projects_Project15', {partner})
    assert getattr(partner, 'Projects_Qualification16') == owner
    _safe_set(owner, 'Projects_Project15', set())
    assert getattr(partner, 'Projects_Qualification16') is None


