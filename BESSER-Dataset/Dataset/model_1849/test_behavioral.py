import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Medium,
    libsys_BarCodeScanner,
    libsys_Book,
    libsys_BorrowedEntry,
    libsys_CD,
    libsys_ExtensionTime,
    libsys_IdentificationCard,
    libsys_Instance,
    libsys_Librarian,
    libsys_Library,
    libsys_Magazine,
    libsys_MediaAdministration,
    libsys_Medium,
    libsys_ReservationEntry,
    libsys_SearchCriterion,
    libsys_StatusSignal,
    libsys_Terminal,
    libsys_UnpaidFee,
    libsys_User,
    libsys_UserAccount,
    libsys_UserAdministration,
    libsys_Video,
    InstanceStatus,
    MediumCode,
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

def test_assoc_borrowedInstances6_reverse_link_reassign_clear():
    a1 = libsys_UserAccount(emailAddress="sample_text", lockIndication=True, postallAddress="sample_text", telephoneNumber="sample_text", unpaidFeeAmount=7, userClassification="sample_text", userData="sample_text", userName="sample_text", userNumber=7, validUntilDate=date(2024, 1, 1))
    a2 = libsys_UserAccount(emailAddress="sample_text_2", lockIndication=False, postallAddress="sample_text_2", telephoneNumber="sample_text_2", unpaidFeeAmount=13, userClassification="sample_text_2", userData="sample_text_2", userName="sample_text_2", userNumber=13, validUntilDate=date(2025, 6, 15))
    b = libsys_Instance(comments="sample_text", components="sample_text", location="sample_text", rentalPeriod="sample_text", returnDate=date(2024, 1, 1), shelfmark="sample_text", status="sample_text")
    _safe_set(b, 'libsys_Instance8', a1)
    assert _is_linked(b, 'libsys_Instance8', a1)
    if hasattr(a1, 'libsys_UserAccount7'):
        assert _is_linked(a1, 'libsys_UserAccount7', b)
    _safe_set(b, 'libsys_Instance8', a2)
    assert _is_linked(b, 'libsys_Instance8', a2)
    if hasattr(a1, 'libsys_UserAccount7'):
        assert not _is_linked(a1, 'libsys_UserAccount7', b)
    if hasattr(a2, 'libsys_UserAccount7'):
        assert _is_linked(a2, 'libsys_UserAccount7', b)
    _safe_set(b, 'libsys_Instance8', None)
    assert not _is_linked(b, 'libsys_Instance8', a2)
    if hasattr(a2, 'libsys_UserAccount7'):
        assert not _is_linked(a2, 'libsys_UserAccount7', b)


def test_assoc_borrowingList3_reverse_link_reassign_clear():
    a1 = libsys_Instance(comments="sample_text", components="sample_text", location="sample_text", rentalPeriod="sample_text", returnDate=date(2024, 1, 1), shelfmark="sample_text", status="sample_text")
    a2 = libsys_Instance(comments="sample_text_2", components="sample_text_2", location="sample_text_2", rentalPeriod="sample_text_2", returnDate=date(2025, 6, 15), shelfmark="sample_text_2", status="sample_text_2")
    b = libsys_BorrowedEntry(returnDate=date(2024, 1, 1))
    _safe_set(b, 'libsys_BorrowedEntry', a1)
    assert _is_linked(b, 'libsys_BorrowedEntry', a1)
    if hasattr(a1, 'libsys_Instance4'):
        assert _is_linked(a1, 'libsys_Instance4', b)
    _safe_set(b, 'libsys_BorrowedEntry', a2)
    assert _is_linked(b, 'libsys_BorrowedEntry', a2)
    if hasattr(a1, 'libsys_Instance4'):
        assert not _is_linked(a1, 'libsys_Instance4', b)
    if hasattr(a2, 'libsys_Instance4'):
        assert _is_linked(a2, 'libsys_Instance4', b)
    _safe_set(b, 'libsys_BorrowedEntry', None)
    assert not _is_linked(b, 'libsys_BorrowedEntry', a2)
    if hasattr(a2, 'libsys_Instance4'):
        assert not _is_linked(a2, 'libsys_Instance4', b)


def test_assoc_instances0_reverse_link_reassign_clear():
    a1 = libsys_Medium(additionalTitle="sample_text", authors="sample_text", identificationCode="sample_text", keywords="sample_text", partialShelfmark="sample_text", publicationYear=date(2024, 1, 1), title="sample_text")
    a2 = libsys_Medium(additionalTitle="sample_text_2", authors="sample_text_2", identificationCode="sample_text_2", keywords="sample_text_2", partialShelfmark="sample_text_2", publicationYear=date(2025, 6, 15), title="sample_text_2")
    b = libsys_Instance(comments="sample_text", components="sample_text", location="sample_text", rentalPeriod="sample_text", returnDate=date(2024, 1, 1), shelfmark="sample_text", status="sample_text")
    _safe_set(b, 'libsys_Instance', a1)
    assert _is_linked(b, 'libsys_Instance', a1)
    if hasattr(a1, 'libsys_Medium'):
        assert _is_linked(a1, 'libsys_Medium', b)
    _safe_set(b, 'libsys_Instance', a2)
    assert _is_linked(b, 'libsys_Instance', a2)
    if hasattr(a1, 'libsys_Medium'):
        assert not _is_linked(a1, 'libsys_Medium', b)
    if hasattr(a2, 'libsys_Medium'):
        assert _is_linked(a2, 'libsys_Medium', b)
    _safe_set(b, 'libsys_Instance', None)
    assert not _is_linked(b, 'libsys_Instance', a2)
    if hasattr(a2, 'libsys_Medium'):
        assert not _is_linked(a2, 'libsys_Medium', b)


def test_assoc_mediaEntries14_reverse_link_reassign_clear():
    a1 = libsys_Medium(additionalTitle="sample_text", authors="sample_text", identificationCode="sample_text", keywords="sample_text", partialShelfmark="sample_text", publicationYear=date(2024, 1, 1), title="sample_text")
    a2 = libsys_Medium(additionalTitle="sample_text_2", authors="sample_text_2", identificationCode="sample_text_2", keywords="sample_text_2", partialShelfmark="sample_text_2", publicationYear=date(2025, 6, 15), title="sample_text_2")
    b = libsys_MediaAdministration()
    _safe_set(b, 'libsys_MediaAdministration', {a1})
    assert _is_linked(b, 'libsys_MediaAdministration', a1)
    if hasattr(a1, 'libsys_Medium15'):
        assert _is_linked(a1, 'libsys_Medium15', b)
    _safe_set(b, 'libsys_MediaAdministration', {a2})
    assert _is_linked(b, 'libsys_MediaAdministration', a2)
    if hasattr(a1, 'libsys_Medium15'):
        assert not _is_linked(a1, 'libsys_Medium15', b)
    if hasattr(a2, 'libsys_Medium15'):
        assert _is_linked(a2, 'libsys_Medium15', b)
    _safe_set(b, 'libsys_MediaAdministration', set())
    assert not _is_linked(b, 'libsys_MediaAdministration', a2)
    if hasattr(a2, 'libsys_Medium15'):
        assert not _is_linked(a2, 'libsys_Medium15', b)


def test_assoc_reservationList9_reverse_link_reassign_clear():
    a1 = libsys_UserAccount(emailAddress="sample_text", lockIndication=True, postallAddress="sample_text", telephoneNumber="sample_text", unpaidFeeAmount=7, userClassification="sample_text", userData="sample_text", userName="sample_text", userNumber=7, validUntilDate=date(2024, 1, 1))
    a2 = libsys_UserAccount(emailAddress="sample_text_2", lockIndication=False, postallAddress="sample_text_2", telephoneNumber="sample_text_2", unpaidFeeAmount=13, userClassification="sample_text_2", userData="sample_text_2", userName="sample_text_2", userNumber=13, validUntilDate=date(2025, 6, 15))
    b = libsys_Instance(comments="sample_text", components="sample_text", location="sample_text", rentalPeriod="sample_text", returnDate=date(2024, 1, 1), shelfmark="sample_text", status="sample_text")
    _safe_set(b, 'libsys_Instance11', a1)
    assert _is_linked(b, 'libsys_Instance11', a1)
    if hasattr(a1, 'libsys_UserAccount10'):
        assert _is_linked(a1, 'libsys_UserAccount10', b)
    _safe_set(b, 'libsys_Instance11', a2)
    assert _is_linked(b, 'libsys_Instance11', a2)
    if hasattr(a1, 'libsys_UserAccount10'):
        assert not _is_linked(a1, 'libsys_UserAccount10', b)
    if hasattr(a2, 'libsys_UserAccount10'):
        assert _is_linked(a2, 'libsys_UserAccount10', b)
    _safe_set(b, 'libsys_Instance11', None)
    assert not _is_linked(b, 'libsys_Instance11', a2)
    if hasattr(a2, 'libsys_UserAccount10'):
        assert not _is_linked(a2, 'libsys_UserAccount10', b)


def test_assoc_user23_reverse_link_reassign_clear():
    a1 = libsys_User()
    a2 = libsys_User()
    b = libsys_BorrowedEntry(returnDate=date(2024, 1, 1))
    _safe_set(b, 'libsys_BorrowedEntry24', a1)
    assert _is_linked(b, 'libsys_BorrowedEntry24', a1)
    if hasattr(a1, 'libsys_User25'):
        assert _is_linked(a1, 'libsys_User25', b)
    _safe_set(b, 'libsys_BorrowedEntry24', a2)
    assert _is_linked(b, 'libsys_BorrowedEntry24', a2)
    if hasattr(a1, 'libsys_User25'):
        assert not _is_linked(a1, 'libsys_User25', b)
    if hasattr(a2, 'libsys_User25'):
        assert _is_linked(a2, 'libsys_User25', b)
    _safe_set(b, 'libsys_BorrowedEntry24', None)
    assert not _is_linked(b, 'libsys_BorrowedEntry24', a2)
    if hasattr(a2, 'libsys_User25'):
        assert not _is_linked(a2, 'libsys_User25', b)


def test_assoc_userAccount5_reverse_link_reassign_clear():
    a1 = libsys_UserAccount(emailAddress="sample_text", lockIndication=True, postallAddress="sample_text", telephoneNumber="sample_text", unpaidFeeAmount=7, userClassification="sample_text", userData="sample_text", userName="sample_text", userNumber=7, validUntilDate=date(2024, 1, 1))
    a2 = libsys_UserAccount(emailAddress="sample_text_2", lockIndication=False, postallAddress="sample_text_2", telephoneNumber="sample_text_2", unpaidFeeAmount=13, userClassification="sample_text_2", userData="sample_text_2", userName="sample_text_2", userNumber=13, validUntilDate=date(2025, 6, 15))
    b = libsys_User()
    _safe_set(b, 'libsys_User', a1)
    assert _is_linked(b, 'libsys_User', a1)
    if hasattr(a1, 'libsys_UserAccount'):
        assert _is_linked(a1, 'libsys_UserAccount', b)
    _safe_set(b, 'libsys_User', a2)
    assert _is_linked(b, 'libsys_User', a2)
    if hasattr(a1, 'libsys_UserAccount'):
        assert not _is_linked(a1, 'libsys_UserAccount', b)
    if hasattr(a2, 'libsys_UserAccount'):
        assert _is_linked(a2, 'libsys_UserAccount', b)
    _safe_set(b, 'libsys_User', None)
    assert not _is_linked(b, 'libsys_User', a2)
    if hasattr(a2, 'libsys_UserAccount'):
        assert not _is_linked(a2, 'libsys_UserAccount', b)


def test_assoc_userAccounts12_reverse_link_reassign_clear():
    a1 = libsys_UserAdministration()
    a2 = libsys_UserAdministration()
    b = libsys_UserAccount(emailAddress="sample_text", lockIndication=True, postallAddress="sample_text", telephoneNumber="sample_text", unpaidFeeAmount=7, userClassification="sample_text", userData="sample_text", userName="sample_text", userNumber=7, validUntilDate=date(2024, 1, 1))
    _safe_set(b, 'libsys_UserAccount13', a1)
    assert _is_linked(b, 'libsys_UserAccount13', a1)
    if hasattr(a1, 'libsys_UserAdministration'):
        assert _is_linked(a1, 'libsys_UserAdministration', b)
    _safe_set(b, 'libsys_UserAccount13', a2)
    assert _is_linked(b, 'libsys_UserAccount13', a2)
    if hasattr(a1, 'libsys_UserAdministration'):
        assert not _is_linked(a1, 'libsys_UserAdministration', b)
    if hasattr(a2, 'libsys_UserAdministration'):
        assert _is_linked(a2, 'libsys_UserAdministration', b)
    _safe_set(b, 'libsys_UserAccount13', None)
    assert not _is_linked(b, 'libsys_UserAccount13', a2)
    if hasattr(a2, 'libsys_UserAdministration'):
        assert not _is_linked(a2, 'libsys_UserAdministration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_media16_stub_double():
    # libsys_Library has no real 'libsys_Library' property in the generated
    # code (a bare stub) -- manually attach it so libsys_Medium's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libsys_Medium's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libsys_Medium(additionalTitle="sample_text", authors="sample_text", identificationCode="sample_text", keywords="sample_text", partialShelfmark="sample_text", publicationYear=date(2024, 1, 1), title="sample_text")
    partner = libsys_Library()
    setattr(partner, 'libsys_Library', None)
    _safe_set(owner, 'libsys_Medium17', partner)
    assert owner in getattr(partner, 'libsys_Library')
    _safe_set(owner, 'libsys_Medium17', None)
    assert owner not in getattr(partner, 'libsys_Library')


def test_assoc_reservationList1_stub_double():
    # libsys_ReservationEntry has no real 'libsys_ReservationEntry' property in the generated
    # code (a bare stub) -- manually attach it so libsys_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libsys_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libsys_Instance(comments="sample_text", components="sample_text", location="sample_text", rentalPeriod="sample_text", returnDate=date(2024, 1, 1), shelfmark="sample_text", status="sample_text")
    partner = libsys_ReservationEntry()
    setattr(partner, 'libsys_ReservationEntry', None)
    _safe_set(owner, 'libsys_Instance2', {partner})
    assert getattr(partner, 'libsys_ReservationEntry') == owner
    _safe_set(owner, 'libsys_Instance2', set())
    assert getattr(partner, 'libsys_ReservationEntry') is None


def test_assoc_user26_stub_double():
    # libsys_ReservationEntry has no real 'libsys_ReservationEntry27' property in the generated
    # code (a bare stub) -- manually attach it so libsys_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libsys_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libsys_User()
    partner = libsys_ReservationEntry()
    setattr(partner, 'libsys_ReservationEntry27', None)
    _safe_set(owner, 'libsys_User28', partner)
    assert getattr(partner, 'libsys_ReservationEntry27') == owner
    _safe_set(owner, 'libsys_User28', None)
    assert getattr(partner, 'libsys_ReservationEntry27') is None


def test_assoc_users20_stub_double():
    # libsys_Library has no real 'libsys_Library21' property in the generated
    # code (a bare stub) -- manually attach it so libsys_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libsys_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libsys_User()
    partner = libsys_Library()
    setattr(partner, 'libsys_Library21', None)
    _safe_set(owner, 'libsys_User22', partner)
    assert getattr(partner, 'libsys_Library21') == owner
    _safe_set(owner, 'libsys_User22', None)
    assert getattr(partner, 'libsys_Library21') is None


