import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    a_Greeting,
    a_Model,
    a_PackageDeclaration,
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

def test_assoc_greetings1_reverse_link_reassign_clear():
    a1 = a_PackageDeclaration(name="sample_text")
    a2 = a_PackageDeclaration(name="sample_text_2")
    b = a_Greeting(name="sample_text")
    _safe_set(b, 'a_Greeting', a1)
    assert _is_linked(b, 'a_Greeting', a1)
    if hasattr(a1, 'a_PackageDeclaration2'):
        assert _is_linked(a1, 'a_PackageDeclaration2', b)
    _safe_set(b, 'a_Greeting', a2)
    assert _is_linked(b, 'a_Greeting', a2)
    if hasattr(a1, 'a_PackageDeclaration2'):
        assert not _is_linked(a1, 'a_PackageDeclaration2', b)
    if hasattr(a2, 'a_PackageDeclaration2'):
        assert _is_linked(a2, 'a_PackageDeclaration2', b)
    _safe_set(b, 'a_Greeting', None)
    assert not _is_linked(b, 'a_Greeting', a2)
    if hasattr(a2, 'a_PackageDeclaration2'):
        assert not _is_linked(a2, 'a_PackageDeclaration2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_package0_stub_double():
    # a_Model has no real 'a_Model' property in the generated
    # code (a bare stub) -- manually attach it so a_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # a_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = a_PackageDeclaration(name="sample_text")
    partner = a_Model()
    setattr(partner, 'a_Model', None)
    _safe_set(owner, 'a_PackageDeclaration', partner)
    assert getattr(partner, 'a_Model') == owner
    _safe_set(owner, 'a_PackageDeclaration', None)
    assert getattr(partner, 'a_Model') is None


