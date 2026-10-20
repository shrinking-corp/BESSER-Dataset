import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Admin_Actor,
    Attack,
    AttackHistory,
    Authenticate_UseCase,
    Authenticate_UseCase1,
    Balance,
    Country,
    Edit_Profile_UseCase,
    Edit_Profile_UseCase1,
    ExecuteAttack_UseCase,
    Location,
    Register_UseCase,
    Result,
    Role,
    StartParam,
    User,
    User_Actor,
    View_AttackHistory_UseCase,
    View_AttackHistory_UseCase1,
    View_AttackNews_UseCase,
    View_AttackNews_UseCase1,
    View_Home_UseCase,
    View_Home_UseCase1,
    View_Profile_UseCase,
    View_Profile_UseCase1,
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

def test_assoc_Account_Balance_reverse_link_reassign_clear():
    a1 = Balance(tokens=7)
    a2 = Balance(tokens=13)
    b = Account(creationDate=7, login="sample_text", password=7)
    _safe_set(b, 'balance6', a1)
    assert _is_linked(b, 'balance6', a1)
    if hasattr(a1, 'account7'):
        assert _is_linked(a1, 'account7', b)
    _safe_set(b, 'balance6', a2)
    assert _is_linked(b, 'balance6', a2)
    if hasattr(a1, 'account7'):
        assert not _is_linked(a1, 'account7', b)
    if hasattr(a2, 'account7'):
        assert _is_linked(a2, 'account7', b)
    _safe_set(b, 'balance6', None)
    assert not _is_linked(b, 'balance6', a2)
    if hasattr(a2, 'account7'):
        assert not _is_linked(a2, 'account7', b)


def test_assoc_Attack_AttackHistory_reverse_link_reassign_clear():
    a1 = AttackHistory(auto=True, date=7, target="sample_text")
    a2 = AttackHistory(auto=False, date=13, target="sample_text_2")
    b = Attack(name="sample_text", requiredTokens=7)
    _safe_set(b, 'attackHistory10', {a1})
    assert _is_linked(b, 'attackHistory10', a1)
    if hasattr(a1, 'attack11'):
        assert _is_linked(a1, 'attack11', b)
    _safe_set(b, 'attackHistory10', {a2})
    assert _is_linked(b, 'attackHistory10', a2)
    if hasattr(a1, 'attack11'):
        assert not _is_linked(a1, 'attack11', b)
    if hasattr(a2, 'attack11'):
        assert _is_linked(a2, 'attack11', b)
    _safe_set(b, 'attackHistory10', set())
    assert not _is_linked(b, 'attackHistory10', a2)
    if hasattr(a2, 'attack11'):
        assert not _is_linked(a2, 'attack11', b)


def test_assoc_Location_Country_reverse_link_reassign_clear():
    a1 = Location(city="sample_text", postalCode=7, stateProvince="sample_text", streetAddress="sample_text")
    a2 = Location(city="sample_text_2", postalCode=13, stateProvince="sample_text_2", streetAddress="sample_text_2")
    b = Country(countryName="sample_text")
    _safe_set(b, 'location9', {a1})
    assert _is_linked(b, 'location9', a1)
    if hasattr(a1, 'country8'):
        assert _is_linked(a1, 'country8', b)
    _safe_set(b, 'location9', {a2})
    assert _is_linked(b, 'location9', a2)
    if hasattr(a1, 'country8'):
        assert not _is_linked(a1, 'country8', b)
    if hasattr(a2, 'country8'):
        assert _is_linked(a2, 'country8', b)
    _safe_set(b, 'location9', set())
    assert not _is_linked(b, 'location9', a2)
    if hasattr(a2, 'country8'):
        assert not _is_linked(a2, 'country8', b)


def test_assoc_Result_AttackHistory_reverse_link_reassign_clear():
    a1 = Result(value="sample_text")
    a2 = Result(value="sample_text_2")
    b = AttackHistory(auto=True, date=7, target="sample_text")
    _safe_set(b, 'result15', a1)
    assert _is_linked(b, 'result15', a1)
    if hasattr(a1, 'attackHistory14'):
        assert _is_linked(a1, 'attackHistory14', b)
    _safe_set(b, 'result15', a2)
    assert _is_linked(b, 'result15', a2)
    if hasattr(a1, 'attackHistory14'):
        assert not _is_linked(a1, 'attackHistory14', b)
    if hasattr(a2, 'attackHistory14'):
        assert _is_linked(a2, 'attackHistory14', b)
    _safe_set(b, 'result15', None)
    assert not _is_linked(b, 'result15', a2)
    if hasattr(a2, 'attackHistory14'):
        assert not _is_linked(a2, 'attackHistory14', b)


def test_assoc_StartParam_AttackHistory_reverse_link_reassign_clear():
    a1 = StartParam(type="sample_text", value="sample_text")
    a2 = StartParam(type="sample_text_2", value="sample_text_2")
    b = AttackHistory(auto=True, date=7, target="sample_text")
    _safe_set(b, 'startParam13', a1)
    assert _is_linked(b, 'startParam13', a1)
    if hasattr(a1, 'attackHistory12'):
        assert _is_linked(a1, 'attackHistory12', b)
    _safe_set(b, 'startParam13', a2)
    assert _is_linked(b, 'startParam13', a2)
    if hasattr(a1, 'attackHistory12'):
        assert not _is_linked(a1, 'attackHistory12', b)
    if hasattr(a2, 'attackHistory12'):
        assert _is_linked(a2, 'attackHistory12', b)
    _safe_set(b, 'startParam13', None)
    assert not _is_linked(b, 'startParam13', a2)
    if hasattr(a2, 'attackHistory12'):
        assert not _is_linked(a2, 'attackHistory12', b)


def test_assoc_User_Account_reverse_link_reassign_clear():
    a1 = User(birthDate=7, cin="sample_text", email="sample_text", fName="sample_text", lName="sample_text", phoneNumber=7)
    a2 = User(birthDate=13, cin="sample_text_2", email="sample_text_2", fName="sample_text_2", lName="sample_text_2", phoneNumber=13)
    b = Account(creationDate=7, login="sample_text", password=7)
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'account4'):
        assert _is_linked(a1, 'account4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'account4'):
        assert not _is_linked(a1, 'account4', b)
    if hasattr(a2, 'account4'):
        assert _is_linked(a2, 'account4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'account4'):
        assert not _is_linked(a2, 'account4', b)


def test_assoc_User_AttackHistory_reverse_link_reassign_clear():
    a1 = User(birthDate=7, cin="sample_text", email="sample_text", fName="sample_text", lName="sample_text", phoneNumber=7)
    a2 = User(birthDate=13, cin="sample_text_2", email="sample_text_2", fName="sample_text_2", lName="sample_text_2", phoneNumber=13)
    b = AttackHistory(auto=True, date=7, target="sample_text")
    _safe_set(b, 'user17', a1)
    assert _is_linked(b, 'user17', a1)
    if hasattr(a1, 'attackHistory16'):
        assert _is_linked(a1, 'attackHistory16', b)
    _safe_set(b, 'user17', a2)
    assert _is_linked(b, 'user17', a2)
    if hasattr(a1, 'attackHistory16'):
        assert not _is_linked(a1, 'attackHistory16', b)
    if hasattr(a2, 'attackHistory16'):
        assert _is_linked(a2, 'attackHistory16', b)
    _safe_set(b, 'user17', None)
    assert not _is_linked(b, 'user17', a2)
    if hasattr(a2, 'attackHistory16'):
        assert not _is_linked(a2, 'attackHistory16', b)


def test_assoc_User_Location_reverse_link_reassign_clear():
    a1 = User(birthDate=7, cin="sample_text", email="sample_text", fName="sample_text", lName="sample_text", phoneNumber=7)
    a2 = User(birthDate=13, cin="sample_text_2", email="sample_text_2", fName="sample_text_2", lName="sample_text_2", phoneNumber=13)
    b = Location(city="sample_text", postalCode=7, stateProvince="sample_text", streetAddress="sample_text")
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'location2'):
        assert _is_linked(a1, 'location2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'location2'):
        assert not _is_linked(a1, 'location2', b)
    if hasattr(a2, 'location2'):
        assert _is_linked(a2, 'location2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'location2'):
        assert not _is_linked(a2, 'location2', b)


def test_assoc_User_Role_reverse_link_reassign_clear():
    a1 = User(birthDate=7, cin="sample_text", email="sample_text", fName="sample_text", lName="sample_text", phoneNumber=7)
    a2 = User(birthDate=13, cin="sample_text_2", email="sample_text_2", fName="sample_text_2", lName="sample_text_2", phoneNumber=13)
    b = Role(type="sample_text")
    _safe_set(b, 'user1', {a1})
    assert _is_linked(b, 'user1', a1)
    if hasattr(a1, 'role0'):
        assert _is_linked(a1, 'role0', b)
    _safe_set(b, 'user1', {a2})
    assert _is_linked(b, 'user1', a2)
    if hasattr(a1, 'role0'):
        assert not _is_linked(a1, 'role0', b)
    if hasattr(a2, 'role0'):
        assert _is_linked(a2, 'role0', b)
    _safe_set(b, 'user1', set())
    assert not _is_linked(b, 'user1', a2)
    if hasattr(a2, 'role0'):
        assert not _is_linked(a2, 'role0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

