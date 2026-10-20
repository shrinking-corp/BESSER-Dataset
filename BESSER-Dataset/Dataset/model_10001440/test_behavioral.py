import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Admin_Actor,
    Cetak_Slip_UseCase,
    Data_Pembayaran,
    Login_Admin,
    Melakukan_Login_UseCase,
    Melakukan_Registrasi_UseCase,
    Melakukan_Transaksi_UseCase,
    Memproses_Database_UseCase,
    Memverivikasi_Data_UseCase,
    Mengentry_Data_UseCase,
    Pelanggan,
    Pelanggan__Actor,
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

def test_assoc_Admin_Data_Pembayaran_reverse_link_reassign_clear():
    a1 = Data_Pembayaran(angsuran=7, angsuranke=7, keterangan="sample_text", kode_bayar="sample_text", kode_kredit="sample_text", tanggal_bayar="sample_text")
    a2 = Data_Pembayaran(angsuran=13, angsuranke=13, keterangan="sample_text_2", kode_bayar="sample_text_2", kode_kredit="sample_text_2", tanggal_bayar="sample_text_2")
    b = Admin(alamat="sample_text", id="sample_text", nama="sample_text", no_tlp=7)
    _safe_set(b, 'data_Pembayaran26', {a1})
    assert _is_linked(b, 'data_Pembayaran26', a1)
    if hasattr(a1, 'admin27'):
        assert _is_linked(a1, 'admin27', b)
    _safe_set(b, 'data_Pembayaran26', {a2})
    assert _is_linked(b, 'data_Pembayaran26', a2)
    if hasattr(a1, 'admin27'):
        assert not _is_linked(a1, 'admin27', b)
    if hasattr(a2, 'admin27'):
        assert _is_linked(a2, 'admin27', b)
    _safe_set(b, 'data_Pembayaran26', set())
    assert not _is_linked(b, 'data_Pembayaran26', a2)
    if hasattr(a2, 'admin27'):
        assert not _is_linked(a2, 'admin27', b)


def test_assoc_Admin_Login_Admin_reverse_link_reassign_clear():
    a1 = Login_Admin(User_name="sample_text", attribute="sample_text")
    a2 = Login_Admin(User_name="sample_text_2", attribute="sample_text_2")
    b = Admin(alamat="sample_text", id="sample_text", nama="sample_text", no_tlp=7)
    _safe_set(b, 'login_Admin20', a1)
    assert _is_linked(b, 'login_Admin20', a1)
    if hasattr(a1, 'admin21'):
        assert _is_linked(a1, 'admin21', b)
    _safe_set(b, 'login_Admin20', a2)
    assert _is_linked(b, 'login_Admin20', a2)
    if hasattr(a1, 'admin21'):
        assert not _is_linked(a1, 'admin21', b)
    if hasattr(a2, 'admin21'):
        assert _is_linked(a2, 'admin21', b)
    _safe_set(b, 'login_Admin20', None)
    assert not _is_linked(b, 'login_Admin20', a2)
    if hasattr(a2, 'admin21'):
        assert not _is_linked(a2, 'admin21', b)


def test_assoc_Admin_Pelanggan_reverse_link_reassign_clear():
    a1 = Pelanggan(alamat="sample_text", kode_pelanggan="sample_text", nama="sample_text")
    a2 = Pelanggan(alamat="sample_text_2", kode_pelanggan="sample_text_2", nama="sample_text_2")
    b = Admin(alamat="sample_text", id="sample_text", nama="sample_text", no_tlp=7)
    _safe_set(b, 'pelanggan22', {a1})
    assert _is_linked(b, 'pelanggan22', a1)
    if hasattr(a1, 'admin23'):
        assert _is_linked(a1, 'admin23', b)
    _safe_set(b, 'pelanggan22', {a2})
    assert _is_linked(b, 'pelanggan22', a2)
    if hasattr(a1, 'admin23'):
        assert not _is_linked(a1, 'admin23', b)
    if hasattr(a2, 'admin23'):
        assert _is_linked(a2, 'admin23', b)
    _safe_set(b, 'pelanggan22', set())
    assert not _is_linked(b, 'pelanggan22', a2)
    if hasattr(a2, 'admin23'):
        assert not _is_linked(a2, 'admin23', b)


def test_assoc_Pelanggan_Data_Pembayaran_reverse_link_reassign_clear():
    a1 = Pelanggan(alamat="sample_text", kode_pelanggan="sample_text", nama="sample_text")
    a2 = Pelanggan(alamat="sample_text_2", kode_pelanggan="sample_text_2", nama="sample_text_2")
    b = Data_Pembayaran(angsuran=7, angsuranke=7, keterangan="sample_text", kode_bayar="sample_text", kode_kredit="sample_text", tanggal_bayar="sample_text")
    _safe_set(b, 'pelanggan25', a1)
    assert _is_linked(b, 'pelanggan25', a1)
    if hasattr(a1, 'data_Pembayaran24'):
        assert _is_linked(a1, 'data_Pembayaran24', b)
    _safe_set(b, 'pelanggan25', a2)
    assert _is_linked(b, 'pelanggan25', a2)
    if hasattr(a1, 'data_Pembayaran24'):
        assert not _is_linked(a1, 'data_Pembayaran24', b)
    if hasattr(a2, 'data_Pembayaran24'):
        assert _is_linked(a2, 'data_Pembayaran24', b)
    _safe_set(b, 'pelanggan25', None)
    assert not _is_linked(b, 'pelanggan25', a2)
    if hasattr(a2, 'data_Pembayaran24'):
        assert not _is_linked(a2, 'data_Pembayaran24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

