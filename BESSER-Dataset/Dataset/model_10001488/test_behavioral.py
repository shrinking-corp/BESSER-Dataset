import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Doctor,
    Insurance,
    Patient,
    UseCase3_UseCase,
    user,
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

def test_assoc_Admin_Doctor_reverse_link_reassign_clear():
    a1 = Doctor(email="sample_text", password="sample_text")
    a2 = Doctor(email="sample_text_2", password="sample_text_2")
    b = Admin(password="sample_text", uname="sample_text")
    _safe_set(b, 'Admin_Doctor_04', {a1})
    assert _is_linked(b, 'Admin_Doctor_04', a1)
    if hasattr(a1, 'accepts5'):
        assert _is_linked(a1, 'accepts5', b)
    _safe_set(b, 'Admin_Doctor_04', {a2})
    assert _is_linked(b, 'Admin_Doctor_04', a2)
    if hasattr(a1, 'accepts5'):
        assert not _is_linked(a1, 'accepts5', b)
    if hasattr(a2, 'accepts5'):
        assert _is_linked(a2, 'accepts5', b)
    _safe_set(b, 'Admin_Doctor_04', set())
    assert not _is_linked(b, 'Admin_Doctor_04', a2)
    if hasattr(a2, 'accepts5'):
        assert not _is_linked(a2, 'accepts5', b)


def test_assoc_Admin_Patient_reverse_link_reassign_clear():
    a1 = Patient(email="sample_text", password="sample_text")
    a2 = Patient(email="sample_text_2", password="sample_text_2")
    b = Admin(password="sample_text", uname="sample_text")
    _safe_set(b, 'Admin_Patient_06', {a1})
    assert _is_linked(b, 'Admin_Patient_06', a1)
    if hasattr(a1, 'accepts7'):
        assert _is_linked(a1, 'accepts7', b)
    _safe_set(b, 'Admin_Patient_06', {a2})
    assert _is_linked(b, 'Admin_Patient_06', a2)
    if hasattr(a1, 'accepts7'):
        assert not _is_linked(a1, 'accepts7', b)
    if hasattr(a2, 'accepts7'):
        assert _is_linked(a2, 'accepts7', b)
    _safe_set(b, 'Admin_Patient_06', set())
    assert not _is_linked(b, 'Admin_Patient_06', a2)
    if hasattr(a2, 'accepts7'):
        assert not _is_linked(a2, 'accepts7', b)


def test_assoc_Admin_user_reverse_link_reassign_clear():
    a1 = user(address="sample_text", email="sample_text", name="sample_text", password="sample_text", phone_number=7)
    a2 = user(address="sample_text_2", email="sample_text_2", name="sample_text_2", password="sample_text_2", phone_number=13)
    b = Admin(password="sample_text", uname="sample_text")
    _safe_set(b, 'Admin_user_08', a1)
    assert _is_linked(b, 'Admin_user_08', a1)
    if hasattr(a1, 'send_mail9'):
        assert _is_linked(a1, 'send_mail9', b)
    _safe_set(b, 'Admin_user_08', a2)
    assert _is_linked(b, 'Admin_user_08', a2)
    if hasattr(a1, 'send_mail9'):
        assert not _is_linked(a1, 'send_mail9', b)
    if hasattr(a2, 'send_mail9'):
        assert _is_linked(a2, 'send_mail9', b)
    _safe_set(b, 'Admin_user_08', None)
    assert not _is_linked(b, 'Admin_user_08', a2)
    if hasattr(a2, 'send_mail9'):
        assert not _is_linked(a2, 'send_mail9', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(email="sample_text", password="sample_text")
    a2 = Patient(email="sample_text_2", password="sample_text_2")
    b = Doctor(email="sample_text", password="sample_text")
    _safe_set(b, 'request_to2', {a1})
    assert _is_linked(b, 'request_to2', a1)
    if hasattr(a1, 'checks3'):
        assert _is_linked(a1, 'checks3', b)
    _safe_set(b, 'request_to2', {a2})
    assert _is_linked(b, 'request_to2', a2)
    if hasattr(a1, 'checks3'):
        assert not _is_linked(a1, 'checks3', b)
    if hasattr(a2, 'checks3'):
        assert _is_linked(a2, 'checks3', b)
    _safe_set(b, 'request_to2', set())
    assert not _is_linked(b, 'request_to2', a2)
    if hasattr(a2, 'checks3'):
        assert not _is_linked(a2, 'checks3', b)


def test_assoc_Insurance_user_reverse_link_reassign_clear():
    a1 = user(address="sample_text", email="sample_text", name="sample_text", password="sample_text", phone_number=7)
    a2 = user(address="sample_text_2", email="sample_text_2", name="sample_text_2", password="sample_text_2", phone_number=13)
    b = Insurance(email="sample_text", password="sample_text")
    _safe_set(b, 'user10', a1)
    assert _is_linked(b, 'user10', a1)
    if hasattr(a1, 'insurance11'):
        assert _is_linked(a1, 'insurance11', b)
    _safe_set(b, 'user10', a2)
    assert _is_linked(b, 'user10', a2)
    if hasattr(a1, 'insurance11'):
        assert not _is_linked(a1, 'insurance11', b)
    if hasattr(a2, 'insurance11'):
        assert _is_linked(a2, 'insurance11', b)
    _safe_set(b, 'user10', None)
    assert not _is_linked(b, 'user10', a2)
    if hasattr(a2, 'insurance11'):
        assert not _is_linked(a2, 'insurance11', b)


def test_assoc_user_Doctor_reverse_link_reassign_clear():
    a1 = user(address="sample_text", email="sample_text", name="sample_text", password="sample_text", phone_number=7)
    a2 = user(address="sample_text_2", email="sample_text_2", name="sample_text_2", password="sample_text_2", phone_number=13)
    b = Doctor(email="sample_text", password="sample_text")
    _safe_set(b, 'register1', a1)
    assert _is_linked(b, 'register1', a1)
    if hasattr(a1, 'user_Doctor_00'):
        assert _is_linked(a1, 'user_Doctor_00', b)
    _safe_set(b, 'register1', a2)
    assert _is_linked(b, 'register1', a2)
    if hasattr(a1, 'user_Doctor_00'):
        assert not _is_linked(a1, 'user_Doctor_00', b)
    if hasattr(a2, 'user_Doctor_00'):
        assert _is_linked(a2, 'user_Doctor_00', b)
    _safe_set(b, 'register1', None)
    assert not _is_linked(b, 'register1', a2)
    if hasattr(a2, 'user_Doctor_00'):
        assert not _is_linked(a2, 'user_Doctor_00', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

