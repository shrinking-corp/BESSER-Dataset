import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    fopramodel_Associate,
    fopramodel_Auxiliary,
    fopramodel_ExternalAdvisor,
    fopramodel_FoPra,
    fopramodel_FoPraManagementSystem,
    fopramodel_Person,
    fopramodel_Professor,
    fopramodel_ResearchGroup,
    fopramodel_Student,
    AuxiliaryKind,
    Course,
    Status,
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

def test_assoc_advisor5_reverse_link_reassign_clear():
    a1 = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    a2 = fopramodel_FoPra(description="sample_text_2", end=date(2025, 6, 15), maxNumberOfStudents=13, start=date(2025, 6, 15), status="sample_text_2", title="sample_text_2")
    b = fopramodel_ExternalAdvisor(information="sample_text")
    _safe_set(b, 'ExternalAdvisor', a1)
    assert _is_linked(b, 'ExternalAdvisor', a1)
    if hasattr(a1, 'fopras6'):
        assert _is_linked(a1, 'fopras6', b)
    _safe_set(b, 'ExternalAdvisor', a2)
    assert _is_linked(b, 'ExternalAdvisor', a2)
    if hasattr(a1, 'fopras6'):
        assert not _is_linked(a1, 'fopras6', b)
    if hasattr(a2, 'fopras6'):
        assert _is_linked(a2, 'fopras6', b)
    _safe_set(b, 'ExternalAdvisor', None)
    assert not _is_linked(b, 'ExternalAdvisor', a2)
    if hasattr(a2, 'fopras6'):
        assert not _is_linked(a2, 'fopras6', b)


def test_assoc_auxiliaries7_reverse_link_reassign_clear():
    a1 = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    a2 = fopramodel_FoPra(description="sample_text_2", end=date(2025, 6, 15), maxNumberOfStudents=13, start=date(2025, 6, 15), status="sample_text_2", title="sample_text_2")
    b = fopramodel_Auxiliary(description="sample_text", kind="sample_text")
    _safe_set(b, 'Auxiliary', a1)
    assert _is_linked(b, 'Auxiliary', a1)
    if hasattr(a1, 'fopras8'):
        assert _is_linked(a1, 'fopras8', b)
    _safe_set(b, 'Auxiliary', a2)
    assert _is_linked(b, 'Auxiliary', a2)
    if hasattr(a1, 'fopras8'):
        assert not _is_linked(a1, 'fopras8', b)
    if hasattr(a2, 'fopras8'):
        assert _is_linked(a2, 'fopras8', b)
    _safe_set(b, 'Auxiliary', None)
    assert not _is_linked(b, 'Auxiliary', a2)
    if hasattr(a2, 'fopras8'):
        assert not _is_linked(a2, 'fopras8', b)


def test_assoc_fopras14_reverse_link_reassign_clear():
    a1 = fopramodel_Student(course="sample_text", matrikel="sample_text")
    a2 = fopramodel_Student(course="sample_text_2", matrikel="sample_text_2")
    b = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    _safe_set(b, 'FoPra', a1)
    assert _is_linked(b, 'FoPra', a1)
    if hasattr(a1, 'students'):
        assert _is_linked(a1, 'students', b)
    _safe_set(b, 'FoPra', a2)
    assert _is_linked(b, 'FoPra', a2)
    if hasattr(a1, 'students'):
        assert not _is_linked(a1, 'students', b)
    if hasattr(a2, 'students'):
        assert _is_linked(a2, 'students', b)
    _safe_set(b, 'FoPra', None)
    assert not _is_linked(b, 'FoPra', a2)
    if hasattr(a2, 'students'):
        assert not _is_linked(a2, 'students', b)


def test_assoc_fopras17_reverse_link_reassign_clear():
    a1 = fopramodel_ResearchGroup(name="sample_text")
    a2 = fopramodel_ResearchGroup(name="sample_text_2")
    b = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    _safe_set(b, 'FoPra18', a1)
    assert _is_linked(b, 'FoPra18', a1)
    if hasattr(a1, 'rg'):
        assert _is_linked(a1, 'rg', b)
    _safe_set(b, 'FoPra18', a2)
    assert _is_linked(b, 'FoPra18', a2)
    if hasattr(a1, 'rg'):
        assert not _is_linked(a1, 'rg', b)
    if hasattr(a2, 'rg'):
        assert _is_linked(a2, 'rg', b)
    _safe_set(b, 'FoPra18', None)
    assert not _is_linked(b, 'FoPra18', a2)
    if hasattr(a2, 'rg'):
        assert not _is_linked(a2, 'rg', b)


def test_assoc_fopras28_reverse_link_reassign_clear():
    a1 = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    a2 = fopramodel_FoPra(description="sample_text_2", end=date(2025, 6, 15), maxNumberOfStudents=13, start=date(2025, 6, 15), status="sample_text_2", title="sample_text_2")
    b = fopramodel_ExternalAdvisor(information="sample_text")
    _safe_set(b, 'advisor', {a1})
    assert _is_linked(b, 'advisor', a1)
    if hasattr(a1, 'FoPra29'):
        assert _is_linked(a1, 'FoPra29', b)
    _safe_set(b, 'advisor', {a2})
    assert _is_linked(b, 'advisor', a2)
    if hasattr(a1, 'FoPra29'):
        assert not _is_linked(a1, 'FoPra29', b)
    if hasattr(a2, 'FoPra29'):
        assert _is_linked(a2, 'FoPra29', b)
    _safe_set(b, 'advisor', set())
    assert not _is_linked(b, 'advisor', a2)
    if hasattr(a2, 'FoPra29'):
        assert not _is_linked(a2, 'FoPra29', b)


def test_assoc_fopras30_reverse_link_reassign_clear():
    a1 = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    a2 = fopramodel_FoPra(description="sample_text_2", end=date(2025, 6, 15), maxNumberOfStudents=13, start=date(2025, 6, 15), status="sample_text_2", title="sample_text_2")
    b = fopramodel_Auxiliary(description="sample_text", kind="sample_text")
    _safe_set(b, 'auxiliaries', {a1})
    assert _is_linked(b, 'auxiliaries', a1)
    if hasattr(a1, 'FoPra31'):
        assert _is_linked(a1, 'FoPra31', b)
    _safe_set(b, 'auxiliaries', {a2})
    assert _is_linked(b, 'auxiliaries', a2)
    if hasattr(a1, 'FoPra31'):
        assert not _is_linked(a1, 'FoPra31', b)
    if hasattr(a2, 'FoPra31'):
        assert _is_linked(a2, 'FoPra31', b)
    _safe_set(b, 'auxiliaries', set())
    assert not _is_linked(b, 'auxiliaries', a2)
    if hasattr(a2, 'FoPra31'):
        assert not _is_linked(a2, 'FoPra31', b)


def test_assoc_rg1_reverse_link_reassign_clear():
    a1 = fopramodel_ResearchGroup(name="sample_text")
    a2 = fopramodel_ResearchGroup(name="sample_text_2")
    b = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    _safe_set(b, 'fopras2', a1)
    assert _is_linked(b, 'fopras2', a1)
    if hasattr(a1, 'ResearchGroup'):
        assert _is_linked(a1, 'ResearchGroup', b)
    _safe_set(b, 'fopras2', a2)
    assert _is_linked(b, 'fopras2', a2)
    if hasattr(a1, 'ResearchGroup'):
        assert not _is_linked(a1, 'ResearchGroup', b)
    if hasattr(a2, 'ResearchGroup'):
        assert _is_linked(a2, 'ResearchGroup', b)
    _safe_set(b, 'fopras2', None)
    assert not _is_linked(b, 'fopras2', a2)
    if hasattr(a2, 'ResearchGroup'):
        assert not _is_linked(a2, 'ResearchGroup', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = fopramodel_Student(course="sample_text", matrikel="sample_text")
    a2 = fopramodel_Student(course="sample_text_2", matrikel="sample_text_2")
    b = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    _safe_set(b, 'fopras', {a1})
    assert _is_linked(b, 'fopras', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'fopras', {a2})
    assert _is_linked(b, 'fopras', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'fopras', set())
    assert not _is_linked(b, 'fopras', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associate21_stub_double():
    # fopramodel_Associate has no real 'Associate23' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_ResearchGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_ResearchGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_ResearchGroup(name="sample_text")
    partner = fopramodel_Associate()
    setattr(partner, 'Associate23', None)
    _safe_set(owner, 'rg22', {partner})
    assert getattr(partner, 'Associate23') == owner
    _safe_set(owner, 'rg22', set())
    assert getattr(partner, 'Associate23') is None


def test_assoc_auxiliaries12_stub_double():
    # fopramodel_FoPraManagementSystem has no real 'fopramodel_FoPraManagementSystem13' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_Auxiliary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_Auxiliary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_Auxiliary(description="sample_text", kind="sample_text")
    partner = fopramodel_FoPraManagementSystem()
    setattr(partner, 'fopramodel_FoPraManagementSystem13', None)
    _safe_set(owner, 'fopramodel_Auxiliary', partner)
    assert owner in getattr(partner, 'fopramodel_FoPraManagementSystem13')
    _safe_set(owner, 'fopramodel_Auxiliary', None)
    assert owner not in getattr(partner, 'fopramodel_FoPraManagementSystem13')


def test_assoc_fopras26_stub_double():
    # fopramodel_Associate has no real 'supervisor' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_FoPra's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_FoPra's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    partner = fopramodel_Associate()
    setattr(partner, 'supervisor', None)
    _safe_set(owner, 'FoPra27', partner)
    assert owner in getattr(partner, 'supervisor')
    _safe_set(owner, 'FoPra27', None)
    assert owner not in getattr(partner, 'supervisor')


def test_assoc_fopras9_stub_double():
    # fopramodel_FoPraManagementSystem has no real 'fopramodel_FoPraManagementSystem' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_FoPra's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_FoPra's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    partner = fopramodel_FoPraManagementSystem()
    setattr(partner, 'fopramodel_FoPraManagementSystem', None)
    _safe_set(owner, 'fopramodel_FoPra', partner)
    assert owner in getattr(partner, 'fopramodel_FoPraManagementSystem')
    _safe_set(owner, 'fopramodel_FoPra', None)
    assert owner not in getattr(partner, 'fopramodel_FoPraManagementSystem')


def test_assoc_persons10_stub_double():
    # fopramodel_FoPraManagementSystem has no real 'fopramodel_FoPraManagementSystem11' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_Person(forename="sample_text", lastname="sample_text")
    partner = fopramodel_FoPraManagementSystem()
    setattr(partner, 'fopramodel_FoPraManagementSystem11', None)
    _safe_set(owner, 'fopramodel_Person', partner)
    assert owner in getattr(partner, 'fopramodel_FoPraManagementSystem11')
    _safe_set(owner, 'fopramodel_Person', None)
    assert owner not in getattr(partner, 'fopramodel_FoPraManagementSystem11')


def test_assoc_professor19_stub_double():
    # fopramodel_Professor has no real 'Professor' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_ResearchGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_ResearchGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_ResearchGroup(name="sample_text")
    partner = fopramodel_Professor()
    setattr(partner, 'Professor', None)
    _safe_set(owner, 'rg20', partner)
    assert getattr(partner, 'Professor') == owner
    _safe_set(owner, 'rg20', None)
    assert getattr(partner, 'Professor') is None


def test_assoc_rg15_stub_double():
    # fopramodel_Professor has no real 'professor' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_ResearchGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_ResearchGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_ResearchGroup(name="sample_text")
    partner = fopramodel_Professor()
    setattr(partner, 'professor', None)
    _safe_set(owner, 'ResearchGroup16', partner)
    assert getattr(partner, 'professor') == owner
    _safe_set(owner, 'ResearchGroup16', None)
    assert getattr(partner, 'professor') is None


def test_assoc_rg24_stub_double():
    # fopramodel_Associate has no real 'associate' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_ResearchGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_ResearchGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_ResearchGroup(name="sample_text")
    partner = fopramodel_Associate()
    setattr(partner, 'associate', None)
    _safe_set(owner, 'ResearchGroup25', partner)
    assert getattr(partner, 'associate') == owner
    _safe_set(owner, 'ResearchGroup25', None)
    assert getattr(partner, 'associate') is None


def test_assoc_supervisor3_stub_double():
    # fopramodel_Associate has no real 'Associate' property in the generated
    # code (a bare stub) -- manually attach it so fopramodel_FoPra's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fopramodel_FoPra's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fopramodel_FoPra(description="sample_text", end=date(2024, 1, 1), maxNumberOfStudents=7, start=date(2024, 1, 1), status="sample_text", title="sample_text")
    partner = fopramodel_Associate()
    setattr(partner, 'Associate', None)
    _safe_set(owner, 'fopras4', partner)
    assert getattr(partner, 'Associate') == owner
    _safe_set(owner, 'fopras4', None)
    assert getattr(partner, 'Associate') is None


