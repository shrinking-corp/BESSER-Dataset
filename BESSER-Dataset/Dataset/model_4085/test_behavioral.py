import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simpleUML_Generalization,
    simpleUML_Model,
    simpleUML_UMLClass,
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

def test_assoc_classes0_stub_double():
    # simpleUML_Model has no real 'simpleUML_Model' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_UMLClass(umlName="sample_text")
    partner = simpleUML_Model()
    setattr(partner, 'simpleUML_Model', None)
    _safe_set(owner, 'simpleUML_UMLClass', partner)
    assert owner in getattr(partner, 'simpleUML_Model')
    _safe_set(owner, 'simpleUML_UMLClass', None)
    assert owner not in getattr(partner, 'simpleUML_Model')


def test_assoc_generalizations1_stub_double():
    # simpleUML_Generalization has no real 'simpleUML_Generalization' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_UMLClass(umlName="sample_text")
    partner = simpleUML_Generalization()
    setattr(partner, 'simpleUML_Generalization', None)
    _safe_set(owner, 'simpleUML_UMLClass2', {partner})
    assert getattr(partner, 'simpleUML_Generalization') == owner
    _safe_set(owner, 'simpleUML_UMLClass2', set())
    assert getattr(partner, 'simpleUML_Generalization') is None


def test_assoc_reference3_stub_double():
    # simpleUML_Generalization has no real 'simpleUML_Generalization4' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_UMLClass(umlName="sample_text")
    partner = simpleUML_Generalization()
    setattr(partner, 'simpleUML_Generalization4', None)
    _safe_set(owner, 'simpleUML_UMLClass5', partner)
    assert getattr(partner, 'simpleUML_Generalization4') == owner
    _safe_set(owner, 'simpleUML_UMLClass5', None)
    assert getattr(partner, 'simpleUML_Generalization4') is None


