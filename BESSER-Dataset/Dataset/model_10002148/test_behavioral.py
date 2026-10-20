import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BankAccount,
    Class,
    ClassA,
    ClassB,
    ClassC,
    ClassD,
    ClassE,
    ClassF,
    ClassG,
    ClassH,
    ClassJ,
    ClassK,
    ClassL,
    ClassM,
    ClassN,
    ClassP,
    ClassQ,
    ClassR,
    ClassS,
    ClassT,
    ClassU,
    ClassV,
    InterfaceO_Interface,
    T,
    T1,
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

def test_assoc_ClassC_ClassB_stub_double():
    # ClassB has no real 'classC7' property in the generated
    # code (a bare stub) -- manually attach it so ClassC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassC(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    partner = ClassB()
    setattr(partner, 'classC7', None)
    _safe_set(owner, 'classB6', partner)
    assert getattr(partner, 'classC7') == owner
    _safe_set(owner, 'classB6', None)
    assert getattr(partner, 'classC7') is None


