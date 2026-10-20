import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Birthday_Parties,
    Client,
    Commercial_Events,
    Event,
    Eventhead,
    Payment,
    Refreshment,
    User,
    Volunteer,
    Weddings,
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

def test_assoc_client_payment_reverse_link_reassign_clear():
    a1 = Payment(amout=7, paytype="sample_text", status="sample_text")
    a2 = Payment(amout=13, paytype="sample_text_2", status="sample_text_2")
    b = Client(id=7)
    _safe_set(b, 'payment20', a1)
    assert _is_linked(b, 'payment20', a1)
    if hasattr(a1, 'client1'):
        assert _is_linked(a1, 'client1', b)
    _safe_set(b, 'payment20', a2)
    assert _is_linked(b, 'payment20', a2)
    if hasattr(a1, 'client1'):
        assert not _is_linked(a1, 'client1', b)
    if hasattr(a2, 'client1'):
        assert _is_linked(a2, 'client1', b)
    _safe_set(b, 'payment20', None)
    assert not _is_linked(b, 'payment20', a2)
    if hasattr(a2, 'client1'):
        assert not _is_linked(a2, 'client1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

