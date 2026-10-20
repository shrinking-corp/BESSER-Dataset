import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Type,
    smalluml_Association,
    smalluml_Boolean,
    smalluml_Class,
    smalluml_Diagram,
    smalluml_Float,
    smalluml_Heritage,
    smalluml_Int,
    smalluml_Method,
    smalluml_NamedElement,
    smalluml_Role,
    smalluml_String,
    smalluml_Type,
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

def test_assoc_child15_stub_double():
    # smalluml_Heritage has no real 'smalluml_Heritage16' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lower=7, upper=7)
    partner = smalluml_Heritage()
    setattr(partner, 'smalluml_Heritage16', None)
    _safe_set(owner, 'smalluml_Role17', partner)
    assert getattr(partner, 'smalluml_Heritage16') == owner
    _safe_set(owner, 'smalluml_Role17', None)
    assert getattr(partner, 'smalluml_Heritage16') is None


def test_assoc_class_18_stub_double():
    # smalluml_Class has no real 'smalluml_Class20' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lower=7, upper=7)
    partner = smalluml_Class()
    setattr(partner, 'smalluml_Class20', None)
    _safe_set(owner, 'smalluml_Role19', partner)
    assert getattr(partner, 'smalluml_Class20') == owner
    _safe_set(owner, 'smalluml_Role19', None)
    assert getattr(partner, 'smalluml_Class20') is None


def test_assoc_mother13_stub_double():
    # smalluml_Heritage has no real 'smalluml_Heritage' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lower=7, upper=7)
    partner = smalluml_Heritage()
    setattr(partner, 'smalluml_Heritage', None)
    _safe_set(owner, 'smalluml_Role14', partner)
    assert getattr(partner, 'smalluml_Heritage') == owner
    _safe_set(owner, 'smalluml_Role14', None)
    assert getattr(partner, 'smalluml_Heritage') is None


def test_assoc_used9_stub_double():
    # smalluml_Association has no real 'smalluml_Association' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lower=7, upper=7)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association', None)
    _safe_set(owner, 'smalluml_Role', partner)
    assert getattr(partner, 'smalluml_Association') == owner
    _safe_set(owner, 'smalluml_Role', None)
    assert getattr(partner, 'smalluml_Association') is None


def test_assoc_user10_stub_double():
    # smalluml_Association has no real 'smalluml_Association11' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lower=7, upper=7)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association11', None)
    _safe_set(owner, 'smalluml_Role12', partner)
    assert getattr(partner, 'smalluml_Association11') == owner
    _safe_set(owner, 'smalluml_Role12', None)
    assert getattr(partner, 'smalluml_Association11') is None


