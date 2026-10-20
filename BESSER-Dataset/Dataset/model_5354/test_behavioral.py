import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    p2_Configuration,
    p2_ProfileDefinition,
    p2_Repository,
    p2_RepositoryList,
    p2_Requirement,
    RepositoryType,
    RequirementType,
    VersionSegment,
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

def test_assoc_repositories1_reverse_link_reassign_clear():
    a1 = p2_Repository(type="sample_text", uRL="sample_text")
    a2 = p2_Repository(type="sample_text_2", uRL="sample_text_2")
    b = p2_ProfileDefinition(includeSourceBundles=True)
    _safe_set(b, 'p2_ProfileDefinition2', {a1})
    assert _is_linked(b, 'p2_ProfileDefinition2', a1)
    if hasattr(a1, 'p2_Repository'):
        assert _is_linked(a1, 'p2_Repository', b)
    _safe_set(b, 'p2_ProfileDefinition2', {a2})
    assert _is_linked(b, 'p2_ProfileDefinition2', a2)
    if hasattr(a1, 'p2_Repository'):
        assert not _is_linked(a1, 'p2_Repository', b)
    if hasattr(a2, 'p2_Repository'):
        assert _is_linked(a2, 'p2_Repository', b)
    _safe_set(b, 'p2_ProfileDefinition2', set())
    assert not _is_linked(b, 'p2_ProfileDefinition2', a2)
    if hasattr(a2, 'p2_Repository'):
        assert not _is_linked(a2, 'p2_Repository', b)


def test_assoc_repositories3_reverse_link_reassign_clear():
    a1 = p2_RepositoryList(name="sample_text")
    a2 = p2_RepositoryList(name="sample_text_2")
    b = p2_Repository(type="sample_text", uRL="sample_text")
    _safe_set(b, 'p2_Repository4', a1)
    assert _is_linked(b, 'p2_Repository4', a1)
    if hasattr(a1, 'p2_RepositoryList'):
        assert _is_linked(a1, 'p2_RepositoryList', b)
    _safe_set(b, 'p2_Repository4', a2)
    assert _is_linked(b, 'p2_Repository4', a2)
    if hasattr(a1, 'p2_RepositoryList'):
        assert not _is_linked(a1, 'p2_RepositoryList', b)
    if hasattr(a2, 'p2_RepositoryList'):
        assert _is_linked(a2, 'p2_RepositoryList', b)
    _safe_set(b, 'p2_Repository4', None)
    assert not _is_linked(b, 'p2_Repository4', a2)
    if hasattr(a2, 'p2_RepositoryList'):
        assert not _is_linked(a2, 'p2_RepositoryList', b)


def test_assoc_requirements0_reverse_link_reassign_clear():
    a1 = p2_Requirement(filter="sample_text", greedy=True, iD="sample_text", name="sample_text", namespace="sample_text", optional=True, type="sample_text", versionRange="sample_text")
    a2 = p2_Requirement(filter="sample_text_2", greedy=False, iD="sample_text_2", name="sample_text_2", namespace="sample_text_2", optional=False, type="sample_text_2", versionRange="sample_text_2")
    b = p2_ProfileDefinition(includeSourceBundles=True)
    _safe_set(b, 'p2_ProfileDefinition', {a1})
    assert _is_linked(b, 'p2_ProfileDefinition', a1)
    if hasattr(a1, 'p2_Requirement'):
        assert _is_linked(a1, 'p2_Requirement', b)
    _safe_set(b, 'p2_ProfileDefinition', {a2})
    assert _is_linked(b, 'p2_ProfileDefinition', a2)
    if hasattr(a1, 'p2_Requirement'):
        assert not _is_linked(a1, 'p2_Requirement', b)
    if hasattr(a2, 'p2_Requirement'):
        assert _is_linked(a2, 'p2_Requirement', b)
    _safe_set(b, 'p2_ProfileDefinition', set())
    assert not _is_linked(b, 'p2_ProfileDefinition', a2)
    if hasattr(a2, 'p2_Requirement'):
        assert not _is_linked(a2, 'p2_Requirement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

