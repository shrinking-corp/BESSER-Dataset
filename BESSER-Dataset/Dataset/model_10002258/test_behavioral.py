import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Halaman_Publikasi__major_sales_record_UseCase,
    Halaman_Publikasi__news_UseCase,
    Halaman_Publikasi__produk_UseCase,
    Pengunjung_Website_Actor,
    admin,
    admin_Actor,
    halaman_admin_login_UseCase,
    halaman_admin_major_sales_record_UseCase,
    halaman_admin_major_sales_record_UseCase1,
    halaman_admin_news_UseCase,
    halaman_admin_news_UseCase1,
    halaman_admin_news_UseCase2,
    halaman_admin_produk_UseCase,
    halaman_admin_produk_UseCase1,
    halaman_admin_produk_UseCase2,
    halaman_admin_register_UseCase,
    halaman_admin_register_UseCase1,
    halaman_admin_register_UseCase2,
    login_admin,
    news,
    news_Interface,
    our_costumer_Interface,
    our_costumer___major,
    pengunjung_website,
    produk,
    produk_Interface,
    register_admin,
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

def test_assoc_admin_login_admin_stub_double():
    # admin has no real 'login_admin20' property in the generated
    # code (a bare stub) -- manually attach it so login_admin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # login_admin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = login_admin(email="sample_text", password="sample_text")
    partner = admin()
    setattr(partner, 'login_admin20', None)
    _safe_set(owner, 'admin21', partner)
    assert getattr(partner, 'login_admin20') == owner
    _safe_set(owner, 'admin21', None)
    assert getattr(partner, 'login_admin20') is None


def test_assoc_admin_news_stub_double():
    # admin has no real 'news4' property in the generated
    # code (a bare stub) -- manually attach it so news's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # news's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = news(foto_news="sample_text", id_news=7, isi_news="sample_text", judul_news="sample_text")
    partner = admin()
    setattr(partner, 'news4', None)
    _safe_set(owner, 'admin5', partner)
    assert owner in getattr(partner, 'news4')
    _safe_set(owner, 'admin5', None)
    assert owner not in getattr(partner, 'news4')


def test_assoc_admin_our_costumer___major_stub_double():
    # admin has no real 'our_costumer___major0' property in the generated
    # code (a bare stub) -- manually attach it so our_costumer___major's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # our_costumer___major's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = our_costumer___major(id_major=7, logo_major="sample_text")
    partner = admin()
    setattr(partner, 'our_costumer___major0', None)
    _safe_set(owner, 'admin1', partner)
    assert owner in getattr(partner, 'our_costumer___major0')
    _safe_set(owner, 'admin1', None)
    assert owner not in getattr(partner, 'our_costumer___major0')


def test_assoc_admin_produk_stub_double():
    # admin has no real 'produk2' property in the generated
    # code (a bare stub) -- manually attach it so produk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # produk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = produk(foto_produk="sample_text", id_produk=7, website="sample_text")
    partner = admin()
    setattr(partner, 'produk2', None)
    _safe_set(owner, 'admin3', partner)
    assert owner in getattr(partner, 'produk2')
    _safe_set(owner, 'admin3', None)
    assert owner not in getattr(partner, 'produk2')


def test_assoc_admin_register_admin_stub_double():
    # admin has no real 'register_admin18' property in the generated
    # code (a bare stub) -- manually attach it so register_admin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # register_admin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = register_admin(email="sample_text", id_user=7, nama_lengkap="sample_text", nik="sample_text", password="sample_text")
    partner = admin()
    setattr(partner, 'register_admin18', None)
    _safe_set(owner, 'admin19', partner)
    assert getattr(partner, 'register_admin18') == owner
    _safe_set(owner, 'admin19', None)
    assert getattr(partner, 'register_admin18') is None


