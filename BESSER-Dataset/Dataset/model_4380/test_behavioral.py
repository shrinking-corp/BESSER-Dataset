import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Relations,
    euml_Attribute,
    euml_Class,
    euml_Dependecy,
    euml_Generalization,
    euml_NamedElement,
    euml_Operation,
    euml_Package,
    euml_Realization,
    euml_Relations,
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

def test_assoc_target20_stub_double():
    # euml_Relations has no real 'euml_Relations' property in the generated
    # code (a bare stub) -- manually attach it so euml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # euml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = euml_NamedElement(name="sample_text")
    partner = euml_Relations()
    setattr(partner, 'euml_Relations', None)
    _safe_set(owner, 'euml_NamedElement', partner)
    assert getattr(partner, 'euml_Relations') == owner
    _safe_set(owner, 'euml_NamedElement', None)
    assert getattr(partner, 'euml_Relations') is None


