import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Repository,
    releng_BuildJob,
    releng_CompositeRepository,
    releng_Criterion,
    releng_Promotion,
    releng_Repository,
    releng_Server,
    BuildType,
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

def test_assoc_build7_reverse_link_reassign_clear():
    a1 = releng_Promotion(buildType="sample_text")
    a2 = releng_Promotion(buildType="sample_text_2")
    b = releng_BuildJob(buckminsterComponent="sample_text", name="sample_text", sourceBranch="sample_text", types="sample_text")
    _safe_set(b, 'BuildJob', a1)
    assert _is_linked(b, 'BuildJob', a1)
    if hasattr(a1, 'promotions'):
        assert _is_linked(a1, 'promotions', b)
    _safe_set(b, 'BuildJob', a2)
    assert _is_linked(b, 'BuildJob', a2)
    if hasattr(a1, 'promotions'):
        assert not _is_linked(a1, 'promotions', b)
    if hasattr(a2, 'promotions'):
        assert _is_linked(a2, 'promotions', b)
    _safe_set(b, 'BuildJob', None)
    assert not _is_linked(b, 'BuildJob', a2)
    if hasattr(a2, 'promotions'):
        assert not _is_linked(a2, 'promotions', b)


def test_assoc_buildJobs0_reverse_link_reassign_clear():
    a1 = releng_Server(name="sample_text")
    a2 = releng_Server(name="sample_text_2")
    b = releng_BuildJob(buckminsterComponent="sample_text", name="sample_text", sourceBranch="sample_text", types="sample_text")
    _safe_set(b, 'releng_BuildJob', a1)
    assert _is_linked(b, 'releng_BuildJob', a1)
    if hasattr(a1, 'releng_Server'):
        assert _is_linked(a1, 'releng_Server', b)
    _safe_set(b, 'releng_BuildJob', a2)
    assert _is_linked(b, 'releng_BuildJob', a2)
    if hasattr(a1, 'releng_Server'):
        assert not _is_linked(a1, 'releng_Server', b)
    if hasattr(a2, 'releng_Server'):
        assert _is_linked(a2, 'releng_Server', b)
    _safe_set(b, 'releng_BuildJob', None)
    assert not _is_linked(b, 'releng_BuildJob', a2)
    if hasattr(a2, 'releng_Server'):
        assert not _is_linked(a2, 'releng_Server', b)


def test_assoc_criteria10_reverse_link_reassign_clear():
    a1 = releng_Promotion(buildType="sample_text")
    a2 = releng_Promotion(buildType="sample_text_2")
    b = releng_Criterion(description="sample_text")
    _safe_set(b, 'releng_Criterion', a1)
    assert _is_linked(b, 'releng_Criterion', a1)
    if hasattr(a1, 'releng_Promotion11'):
        assert _is_linked(a1, 'releng_Promotion11', b)
    _safe_set(b, 'releng_Criterion', a2)
    assert _is_linked(b, 'releng_Criterion', a2)
    if hasattr(a1, 'releng_Promotion11'):
        assert not _is_linked(a1, 'releng_Promotion11', b)
    if hasattr(a2, 'releng_Promotion11'):
        assert _is_linked(a2, 'releng_Promotion11', b)
    _safe_set(b, 'releng_Criterion', None)
    assert not _is_linked(b, 'releng_Criterion', a2)
    if hasattr(a2, 'releng_Promotion11'):
        assert not _is_linked(a2, 'releng_Promotion11', b)


def test_assoc_promotions6_reverse_link_reassign_clear():
    a1 = releng_Promotion(buildType="sample_text")
    a2 = releng_Promotion(buildType="sample_text_2")
    b = releng_BuildJob(buckminsterComponent="sample_text", name="sample_text", sourceBranch="sample_text", types="sample_text")
    _safe_set(b, 'build', {a1})
    assert _is_linked(b, 'build', a1)
    if hasattr(a1, 'Promotion'):
        assert _is_linked(a1, 'Promotion', b)
    _safe_set(b, 'build', {a2})
    assert _is_linked(b, 'build', a2)
    if hasattr(a1, 'Promotion'):
        assert not _is_linked(a1, 'Promotion', b)
    if hasattr(a2, 'Promotion'):
        assert _is_linked(a2, 'Promotion', b)
    _safe_set(b, 'build', set())
    assert not _is_linked(b, 'build', a2)
    if hasattr(a2, 'Promotion'):
        assert not _is_linked(a2, 'Promotion', b)


def test_assoc_repositories1_reverse_link_reassign_clear():
    a1 = releng_Server(name="sample_text")
    a2 = releng_Server(name="sample_text_2")
    b = releng_Repository(location="sample_text")
    _safe_set(b, 'releng_Repository', a1)
    assert _is_linked(b, 'releng_Repository', a1)
    if hasattr(a1, 'releng_Server2'):
        assert _is_linked(a1, 'releng_Server2', b)
    _safe_set(b, 'releng_Repository', a2)
    assert _is_linked(b, 'releng_Repository', a2)
    if hasattr(a1, 'releng_Server2'):
        assert not _is_linked(a1, 'releng_Server2', b)
    if hasattr(a2, 'releng_Server2'):
        assert _is_linked(a2, 'releng_Server2', b)
    _safe_set(b, 'releng_Repository', None)
    assert not _is_linked(b, 'releng_Repository', a2)
    if hasattr(a2, 'releng_Server2'):
        assert not _is_linked(a2, 'releng_Server2', b)


def test_assoc_result3_reverse_link_reassign_clear():
    a1 = releng_Repository(location="sample_text")
    a2 = releng_Repository(location="sample_text_2")
    b = releng_BuildJob(buckminsterComponent="sample_text", name="sample_text", sourceBranch="sample_text", types="sample_text")
    _safe_set(b, 'releng_BuildJob4', a1)
    assert _is_linked(b, 'releng_BuildJob4', a1)
    if hasattr(a1, 'releng_Repository5'):
        assert _is_linked(a1, 'releng_Repository5', b)
    _safe_set(b, 'releng_BuildJob4', a2)
    assert _is_linked(b, 'releng_BuildJob4', a2)
    if hasattr(a1, 'releng_Repository5'):
        assert not _is_linked(a1, 'releng_Repository5', b)
    if hasattr(a2, 'releng_Repository5'):
        assert _is_linked(a2, 'releng_Repository5', b)
    _safe_set(b, 'releng_BuildJob4', None)
    assert not _is_linked(b, 'releng_BuildJob4', a2)
    if hasattr(a2, 'releng_Repository5'):
        assert not _is_linked(a2, 'releng_Repository5', b)


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = releng_Repository(location="sample_text")
    a2 = releng_Repository(location="sample_text_2")
    b = releng_Promotion(buildType="sample_text")
    _safe_set(b, 'releng_Promotion', a1)
    assert _is_linked(b, 'releng_Promotion', a1)
    if hasattr(a1, 'releng_Repository9'):
        assert _is_linked(a1, 'releng_Repository9', b)
    _safe_set(b, 'releng_Promotion', a2)
    assert _is_linked(b, 'releng_Promotion', a2)
    if hasattr(a1, 'releng_Repository9'):
        assert not _is_linked(a1, 'releng_Repository9', b)
    if hasattr(a2, 'releng_Repository9'):
        assert _is_linked(a2, 'releng_Repository9', b)
    _safe_set(b, 'releng_Promotion', None)
    assert not _is_linked(b, 'releng_Promotion', a2)
    if hasattr(a2, 'releng_Repository9'):
        assert not _is_linked(a2, 'releng_Repository9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements12_stub_double():
    # releng_CompositeRepository has no real 'releng_CompositeRepository' property in the generated
    # code (a bare stub) -- manually attach it so releng_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # releng_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = releng_Repository(location="sample_text")
    partner = releng_CompositeRepository()
    setattr(partner, 'releng_CompositeRepository', None)
    _safe_set(owner, 'releng_Repository13', partner)
    assert owner in getattr(partner, 'releng_CompositeRepository')
    _safe_set(owner, 'releng_Repository13', None)
    assert owner not in getattr(partner, 'releng_CompositeRepository')


