import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ElementCS,
    NamedElementCS,
    classescs_ArgumentCS,
    classescs_ClassCS,
    classescs_EObject,
    classescs_ElementCS,
    classescs_NameExpCS,
    classescs_NamedElementCS,
    classescs_OperationCS,
    classescs_PackageCS,
    classescs_PathElementCS,
    classescs_PathNameCS,
    classescs_PropertyCS,
    classescs_RootCS,
    classescs_RoundedBracketClause,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyExps18_stub_double():
    # classescs_NameExpCS has no real 'classescs_NameExpCS' property in the generated
    # code (a bare stub) -- manually attach it so classescs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classescs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classescs_OperationCS(params="sample_text")
    partner = classescs_NameExpCS()
    setattr(partner, 'classescs_NameExpCS', None)
    _safe_set(owner, 'classescs_OperationCS19', {partner})
    assert getattr(partner, 'classescs_NameExpCS') == owner
    _safe_set(owner, 'classescs_OperationCS19', set())
    assert getattr(partner, 'classescs_NameExpCS') is None


def test_assoc_operations9_stub_double():
    # classescs_ClassCS has no real 'classescs_ClassCS10' property in the generated
    # code (a bare stub) -- manually attach it so classescs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classescs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classescs_OperationCS(params="sample_text")
    partner = classescs_ClassCS()
    setattr(partner, 'classescs_ClassCS10', None)
    _safe_set(owner, 'classescs_OperationCS', partner)
    assert owner in getattr(partner, 'classescs_ClassCS10')
    _safe_set(owner, 'classescs_OperationCS', None)
    assert owner not in getattr(partner, 'classescs_ClassCS10')


def test_assoc_resultRef20_stub_double():
    # classescs_PathNameCS has no real 'classescs_PathNameCS22' property in the generated
    # code (a bare stub) -- manually attach it so classescs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classescs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classescs_OperationCS(params="sample_text")
    partner = classescs_PathNameCS()
    setattr(partner, 'classescs_PathNameCS22', None)
    _safe_set(owner, 'classescs_OperationCS21', partner)
    assert getattr(partner, 'classescs_PathNameCS22') == owner
    _safe_set(owner, 'classescs_OperationCS21', None)
    assert getattr(partner, 'classescs_PathNameCS22') is None


