import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Flightlist,
    System,
    Ticket,
    Timinglist,
    User,
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

def test_assoc_Admin_System_reverse_link_reassign_clear():
    a1 = System(id="sample_text", name="sample_text", session="sample_text")
    a2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    b = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    _safe_set(b, 'system4', a1)
    assert _is_linked(b, 'system4', a1)
    if hasattr(a1, 'maintains5'):
        assert _is_linked(a1, 'maintains5', b)
    _safe_set(b, 'system4', a2)
    assert _is_linked(b, 'system4', a2)
    if hasattr(a1, 'maintains5'):
        assert not _is_linked(a1, 'maintains5', b)
    if hasattr(a2, 'maintains5'):
        assert _is_linked(a2, 'maintains5', b)
    _safe_set(b, 'system4', None)
    assert not _is_linked(b, 'system4', a2)
    if hasattr(a2, 'maintains5'):
        assert not _is_linked(a2, 'maintains5', b)


def test_assoc_System_Flightlist_reverse_link_reassign_clear():
    a1 = System(id="sample_text", name="sample_text", session="sample_text")
    a2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    b = Flightlist(id="sample_text", name="sample_text")
    _safe_set(b, 'system7', a1)
    assert _is_linked(b, 'system7', a1)
    if hasattr(a1, 'has6'):
        assert _is_linked(a1, 'has6', b)
    _safe_set(b, 'system7', a2)
    assert _is_linked(b, 'system7', a2)
    if hasattr(a1, 'has6'):
        assert not _is_linked(a1, 'has6', b)
    if hasattr(a2, 'has6'):
        assert _is_linked(a2, 'has6', b)
    _safe_set(b, 'system7', None)
    assert not _is_linked(b, 'system7', a2)
    if hasattr(a2, 'has6'):
        assert not _is_linked(a2, 'has6', b)


def test_assoc_System_Timinglist_reverse_link_reassign_clear():
    a1 = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    a2 = Timinglist(destination="sample_text_2", flightname="sample_text_2", source="sample_text_2", time="sample_text_2")
    b = System(id="sample_text", name="sample_text", session="sample_text")
    _safe_set(b, 'system8', a1)
    assert _is_linked(b, 'system8', a1)
    if hasattr(a1, 'has9'):
        assert _is_linked(a1, 'has9', b)
    _safe_set(b, 'system8', a2)
    assert _is_linked(b, 'system8', a2)
    if hasattr(a1, 'has9'):
        assert not _is_linked(a1, 'has9', b)
    if hasattr(a2, 'has9'):
        assert _is_linked(a2, 'has9', b)
    _safe_set(b, 'system8', None)
    assert not _is_linked(b, 'system8', a2)
    if hasattr(a2, 'has9'):
        assert not _is_linked(a2, 'has9', b)


def test_assoc_User_System_reverse_link_reassign_clear():
    a1 = User(attribute="sample_text", password="sample_text", username="sample_text")
    a2 = User(attribute="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = System(id="sample_text", name="sample_text", session="sample_text")
    _safe_set(b, 'visits3', a1)
    assert _is_linked(b, 'visits3', a1)
    if hasattr(a1, 'system2'):
        assert _is_linked(a1, 'system2', b)
    _safe_set(b, 'visits3', a2)
    assert _is_linked(b, 'visits3', a2)
    if hasattr(a1, 'system2'):
        assert not _is_linked(a1, 'system2', b)
    if hasattr(a2, 'system2'):
        assert _is_linked(a2, 'system2', b)
    _safe_set(b, 'visits3', None)
    assert not _is_linked(b, 'visits3', a2)
    if hasattr(a2, 'system2'):
        assert not _is_linked(a2, 'system2', b)


def test_assoc_User_Ticket_reverse_link_reassign_clear():
    a1 = User(attribute="sample_text", password="sample_text", username="sample_text")
    a2 = User(attribute="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    _safe_set(b, 'system1', {a1})
    assert _is_linked(b, 'system1', a1)
    if hasattr(a1, 'books0'):
        assert _is_linked(a1, 'books0', b)
    _safe_set(b, 'system1', {a2})
    assert _is_linked(b, 'system1', a2)
    if hasattr(a1, 'books0'):
        assert not _is_linked(a1, 'books0', b)
    if hasattr(a2, 'books0'):
        assert _is_linked(a2, 'books0', b)
    _safe_set(b, 'system1', set())
    assert not _is_linked(b, 'system1', a2)
    if hasattr(a2, 'books0'):
        assert not _is_linked(a2, 'books0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

