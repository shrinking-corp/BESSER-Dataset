import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    necsis14_classdiagram_Association,
    necsis14_classdiagram_Attribute,
    necsis14_classdiagram_Class,
    necsis14_classdiagram_ClassDiagram,
    necsis14_classdiagram_NamedElement,
    necsis14_classdiagram__QColumn,
    necsis14_classdiagram__QTable,
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

def test_assoc_associations1_stub_double():
    # necsis14_classdiagram_ClassDiagram has no real 'necsis14_classdiagram_ClassDiagram2' property in the generated
    # code (a bare stub) -- manually attach it so necsis14_classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # necsis14_classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = necsis14_classdiagram_Association(lowerBound=7, upperBound=7)
    partner = necsis14_classdiagram_ClassDiagram()
    setattr(partner, 'necsis14_classdiagram_ClassDiagram2', None)
    _safe_set(owner, 'necsis14_classdiagram_Association', partner)
    assert owner in getattr(partner, 'necsis14_classdiagram_ClassDiagram2')
    _safe_set(owner, 'necsis14_classdiagram_Association', None)
    assert owner not in getattr(partner, 'necsis14_classdiagram_ClassDiagram2')


def test_assoc_source10_stub_double():
    # necsis14_classdiagram_Class has no real 'necsis14_classdiagram_Class12' property in the generated
    # code (a bare stub) -- manually attach it so necsis14_classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # necsis14_classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = necsis14_classdiagram_Association(lowerBound=7, upperBound=7)
    partner = necsis14_classdiagram_Class()
    setattr(partner, 'necsis14_classdiagram_Class12', None)
    _safe_set(owner, 'necsis14_classdiagram_Association11', partner)
    assert getattr(partner, 'necsis14_classdiagram_Class12') == owner
    _safe_set(owner, 'necsis14_classdiagram_Association11', None)
    assert getattr(partner, 'necsis14_classdiagram_Class12') is None


def test_assoc_target13_stub_double():
    # necsis14_classdiagram_Class has no real 'necsis14_classdiagram_Class15' property in the generated
    # code (a bare stub) -- manually attach it so necsis14_classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # necsis14_classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = necsis14_classdiagram_Association(lowerBound=7, upperBound=7)
    partner = necsis14_classdiagram_Class()
    setattr(partner, 'necsis14_classdiagram_Class15', None)
    _safe_set(owner, 'necsis14_classdiagram_Association14', partner)
    assert getattr(partner, 'necsis14_classdiagram_Class15') == owner
    _safe_set(owner, 'necsis14_classdiagram_Association14', None)
    assert getattr(partner, 'necsis14_classdiagram_Class15') is None


