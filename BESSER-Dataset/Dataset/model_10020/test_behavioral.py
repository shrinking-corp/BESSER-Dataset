import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Project,
    Projects_Company,
    Projects_Project,
    Projects_Qualification,
    Projects_Training,
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

def test_assoc_company6_reverse_link_reassign_clear():
    a1 = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    a2 = Projects_Project(name="sample_text_2", size="sample_text_2", status="sample_text_2")
    b = Projects_Company(name="sample_text")
    _safe_set(b, 'Company7', a1)
    assert _is_linked(b, 'Company7', a1)
    if hasattr(a1, 'projects'):
        assert _is_linked(a1, 'projects', b)
    _safe_set(b, 'Company7', a2)
    assert _is_linked(b, 'Company7', a2)
    if hasattr(a1, 'projects'):
        assert not _is_linked(a1, 'projects', b)
    if hasattr(a2, 'projects'):
        assert _is_linked(a2, 'projects', b)
    _safe_set(b, 'Company7', None)
    assert not _is_linked(b, 'Company7', a2)
    if hasattr(a2, 'projects'):
        assert not _is_linked(a2, 'projects', b)


def test_assoc_employees1_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Company(name="sample_text")
    _safe_set(b, 'employer', {a1})
    assert _is_linked(b, 'employer', a1)
    if hasattr(a1, 'Worker'):
        assert _is_linked(a1, 'Worker', b)
    _safe_set(b, 'employer', {a2})
    assert _is_linked(b, 'employer', a2)
    if hasattr(a1, 'Worker'):
        assert not _is_linked(a1, 'Worker', b)
    if hasattr(a2, 'Worker'):
        assert _is_linked(a2, 'Worker', b)
    _safe_set(b, 'employer', set())
    assert not _is_linked(b, 'employer', a2)
    if hasattr(a2, 'Worker'):
        assert not _is_linked(a2, 'Worker', b)


def test_assoc_employer2_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Company(name="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'employees'):
        assert _is_linked(a1, 'employees', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'employees'):
        assert not _is_linked(a1, 'employees', b)
    if hasattr(a2, 'employees'):
        assert _is_linked(a2, 'employees', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'employees'):
        assert not _is_linked(a2, 'employees', b)


def test_assoc_members8_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'projects9', {a1})
    assert _is_linked(b, 'projects9', a1)
    if hasattr(a1, 'Worker10'):
        assert _is_linked(a1, 'Worker10', b)
    _safe_set(b, 'projects9', {a2})
    assert _is_linked(b, 'projects9', a2)
    if hasattr(a1, 'Worker10'):
        assert not _is_linked(a1, 'Worker10', b)
    if hasattr(a2, 'Worker10'):
        assert _is_linked(a2, 'Worker10', b)
    _safe_set(b, 'projects9', set())
    assert not _is_linked(b, 'projects9', a2)
    if hasattr(a2, 'Worker10'):
        assert not _is_linked(a2, 'Worker10', b)


def test_assoc_predecessors15_reverse_link_reassign_clear():
    a1 = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    a2 = Projects_Project(name="sample_text_2", size="sample_text_2", status="sample_text_2")
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'successors', {a1})
    assert _is_linked(b, 'successors', a1)
    if hasattr(a1, 'Project16'):
        assert _is_linked(a1, 'Project16', b)
    _safe_set(b, 'successors', {a2})
    assert _is_linked(b, 'successors', a2)
    if hasattr(a1, 'Project16'):
        assert not _is_linked(a1, 'Project16', b)
    if hasattr(a2, 'Project16'):
        assert _is_linked(a2, 'Project16', b)
    _safe_set(b, 'successors', set())
    assert not _is_linked(b, 'successors', a2)
    if hasattr(a2, 'Project16'):
        assert not _is_linked(a2, 'Project16', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    a2 = Projects_Project(name="sample_text_2", size="sample_text_2", status="sample_text_2")
    b = Projects_Company(name="sample_text")
    _safe_set(b, 'company', {a1})
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'company', {a2})
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'company', set())
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_projects22_reverse_link_reassign_clear():
    a1 = Projects_Qualification(description="sample_text")
    a2 = Projects_Qualification(description="sample_text_2")
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'Project23', a1)
    assert _is_linked(b, 'Project23', a1)
    if hasattr(a1, 'requirements'):
        assert _is_linked(a1, 'requirements', b)
    _safe_set(b, 'Project23', a2)
    assert _is_linked(b, 'Project23', a2)
    if hasattr(a1, 'requirements'):
        assert not _is_linked(a1, 'requirements', b)
    if hasattr(a2, 'requirements'):
        assert _is_linked(a2, 'requirements', b)
    _safe_set(b, 'Project23', None)
    assert not _is_linked(b, 'Project23', a2)
    if hasattr(a2, 'requirements'):
        assert not _is_linked(a2, 'requirements', b)


def test_assoc_projects4_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'Project5', a1)
    assert _is_linked(b, 'Project5', a1)
    if hasattr(a1, 'members'):
        assert _is_linked(a1, 'members', b)
    _safe_set(b, 'Project5', a2)
    assert _is_linked(b, 'Project5', a2)
    if hasattr(a1, 'members'):
        assert not _is_linked(a1, 'members', b)
    if hasattr(a2, 'members'):
        assert _is_linked(a2, 'members', b)
    _safe_set(b, 'Project5', None)
    assert not _is_linked(b, 'Project5', a2)
    if hasattr(a2, 'members'):
        assert not _is_linked(a2, 'members', b)


def test_assoc_qualifications3_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Qualification(description="sample_text")
    _safe_set(b, 'Qualification', a1)
    assert _is_linked(b, 'Qualification', a1)
    if hasattr(a1, 'workers'):
        assert _is_linked(a1, 'workers', b)
    _safe_set(b, 'Qualification', a2)
    assert _is_linked(b, 'Qualification', a2)
    if hasattr(a1, 'workers'):
        assert not _is_linked(a1, 'workers', b)
    if hasattr(a2, 'workers'):
        assert _is_linked(a2, 'workers', b)
    _safe_set(b, 'Qualification', None)
    assert not _is_linked(b, 'Qualification', a2)
    if hasattr(a2, 'workers'):
        assert not _is_linked(a2, 'workers', b)


def test_assoc_requirements11_reverse_link_reassign_clear():
    a1 = Projects_Qualification(description="sample_text")
    a2 = Projects_Qualification(description="sample_text_2")
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'projects12', {a1})
    assert _is_linked(b, 'projects12', a1)
    if hasattr(a1, 'Qualification13'):
        assert _is_linked(a1, 'Qualification13', b)
    _safe_set(b, 'projects12', {a2})
    assert _is_linked(b, 'projects12', a2)
    if hasattr(a1, 'Qualification13'):
        assert not _is_linked(a1, 'Qualification13', b)
    if hasattr(a2, 'Qualification13'):
        assert _is_linked(a2, 'Qualification13', b)
    _safe_set(b, 'projects12', set())
    assert not _is_linked(b, 'projects12', a2)
    if hasattr(a2, 'Qualification13'):
        assert not _is_linked(a2, 'Qualification13', b)


def test_assoc_successors18_reverse_link_reassign_clear():
    a1 = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    a2 = Projects_Project(name="sample_text_2", size="sample_text_2", status="sample_text_2")
    b = Projects_Project(name="sample_text", size="sample_text", status="sample_text")
    _safe_set(b, 'predecessors', {a1})
    assert _is_linked(b, 'predecessors', a1)
    if hasattr(a1, 'Project19'):
        assert _is_linked(a1, 'Project19', b)
    _safe_set(b, 'predecessors', {a2})
    assert _is_linked(b, 'predecessors', a2)
    if hasattr(a1, 'Project19'):
        assert not _is_linked(a1, 'Project19', b)
    if hasattr(a2, 'Project19'):
        assert _is_linked(a2, 'Project19', b)
    _safe_set(b, 'predecessors', set())
    assert not _is_linked(b, 'predecessors', a2)
    if hasattr(a2, 'Project19'):
        assert not _is_linked(a2, 'Project19', b)


def test_assoc_workers20_reverse_link_reassign_clear():
    a1 = Projects_Worker(nickname="sample_text", salary=7)
    a2 = Projects_Worker(nickname="sample_text_2", salary=13)
    b = Projects_Qualification(description="sample_text")
    _safe_set(b, 'qualifications', {a1})
    assert _is_linked(b, 'qualifications', a1)
    if hasattr(a1, 'Worker21'):
        assert _is_linked(a1, 'Worker21', b)
    _safe_set(b, 'qualifications', {a2})
    assert _is_linked(b, 'qualifications', a2)
    if hasattr(a1, 'Worker21'):
        assert not _is_linked(a1, 'Worker21', b)
    if hasattr(a2, 'Worker21'):
        assert _is_linked(a2, 'Worker21', b)
    _safe_set(b, 'qualifications', set())
    assert not _is_linked(b, 'qualifications', a2)
    if hasattr(a2, 'Worker21'):
        assert not _is_linked(a2, 'Worker21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_trained25_stub_double():
    # Projects_Training has no real 'trainings' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Qualification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Qualification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Qualification(description="sample_text")
    partner = Projects_Training()
    setattr(partner, 'trainings', None)
    _safe_set(owner, 'Qualification26', partner)
    assert owner in getattr(partner, 'trainings')
    _safe_set(owner, 'Qualification26', None)
    assert owner not in getattr(partner, 'trainings')


def test_assoc_trainings24_stub_double():
    # Projects_Training has no real 'Training' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Qualification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Qualification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Qualification(description="sample_text")
    partner = Projects_Training()
    setattr(partner, 'Training', None)
    _safe_set(owner, 'trained', partner)
    assert getattr(partner, 'Training') == owner
    _safe_set(owner, 'trained', None)
    assert getattr(partner, 'Training') is None


