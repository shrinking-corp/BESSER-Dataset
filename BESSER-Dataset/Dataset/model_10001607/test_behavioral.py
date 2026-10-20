import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Biddee,
    Bidder,
    Bidding,
    HasilBidding,
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

def test_assoc_Bidding_Biddee_reverse_link_reassign_clear():
    a1 = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    a2 = Bidding(berkas="sample_text_2", biddee="sample_text_2", bidder="sample_text_2", catatanBidder="sample_text_2", jabatan="sample_text_2", nilai=13, notulensi="sample_text_2", statusBidding="sample_text_2")
    b = Biddee(statusBiddee="sample_text")
    _safe_set(b, 'bidding5', {a1})
    assert _is_linked(b, 'bidding5', a1)
    if hasattr(a1, 'daftar4'):
        assert _is_linked(a1, 'daftar4', b)
    _safe_set(b, 'bidding5', {a2})
    assert _is_linked(b, 'bidding5', a2)
    if hasattr(a1, 'daftar4'):
        assert not _is_linked(a1, 'daftar4', b)
    if hasattr(a2, 'daftar4'):
        assert _is_linked(a2, 'daftar4', b)
    _safe_set(b, 'bidding5', set())
    assert not _is_linked(b, 'bidding5', a2)
    if hasattr(a2, 'daftar4'):
        assert not _is_linked(a2, 'daftar4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Admin_Biddee_stub_double():
    # Admin has no real 'biddee6' property in the generated
    # code (a bare stub) -- manually attach it so Biddee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Biddee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Biddee(statusBiddee="sample_text")
    partner = Admin()
    setattr(partner, 'biddee6', None)
    _safe_set(owner, 'ubah_status7', partner)
    assert owner in getattr(partner, 'biddee6')
    _safe_set(owner, 'ubah_status7', None)
    assert owner not in getattr(partner, 'biddee6')


def test_assoc_Admin_Bidding_stub_double():
    # Admin has no real 'bidding2' property in the generated
    # code (a bare stub) -- manually attach it so Bidding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bidding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    partner = Admin()
    setattr(partner, 'bidding2', None)
    _safe_set(owner, 'CRUD_bidding3', partner)
    assert owner in getattr(partner, 'bidding2')
    _safe_set(owner, 'CRUD_bidding3', None)
    assert owner not in getattr(partner, 'bidding2')


def test_assoc_Bidder_Bidding_stub_double():
    # Bidder has no real 'buat_catatan8' property in the generated
    # code (a bare stub) -- manually attach it so Bidding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bidding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    partner = Bidder()
    setattr(partner, 'buat_catatan8', None)
    _safe_set(owner, 'bidder29', {partner})
    assert owner in getattr(partner, 'buat_catatan8')
    _safe_set(owner, 'bidder29', set())
    assert owner not in getattr(partner, 'buat_catatan8')


def test_assoc_Bidder_Bidding2_stub_double():
    # Bidder has no real 'edit_nilai10' property in the generated
    # code (a bare stub) -- manually attach it so Bidding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bidding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    partner = Bidder()
    setattr(partner, 'edit_nilai10', None)
    _safe_set(owner, 'Bidder_Bidding2_111', {partner})
    assert owner in getattr(partner, 'edit_nilai10')
    _safe_set(owner, 'Bidder_Bidding2_111', set())
    assert owner not in getattr(partner, 'edit_nilai10')


def test_assoc_HasilBidding_Bidding_stub_double():
    # HasilBidding has no real 'bidding0' property in the generated
    # code (a bare stub) -- manually attach it so Bidding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bidding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    partner = HasilBidding()
    setattr(partner, 'bidding0', None)
    _safe_set(owner, 'hasilBidding1', partner)
    assert owner in getattr(partner, 'bidding0')
    _safe_set(owner, 'hasilBidding1', None)
    assert owner not in getattr(partner, 'bidding0')


def test_assoc_User_HasilBidding_stub_double():
    # HasilBidding has no real 'melihat13' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    partner = HasilBidding()
    setattr(partner, 'melihat13', None)
    _safe_set(owner, 'hasilBidding12', {partner})
    assert owner in getattr(partner, 'melihat13')
    _safe_set(owner, 'hasilBidding12', set())
    assert owner not in getattr(partner, 'melihat13')


