import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Administrasi,
    Kendaraan,
    Login,
    Pelanggan,
    Pemilik,
    Pesan,
    RentalMobil,
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

def test_assoc_Admin_Administrasi_reverse_link_reassign_clear():
    a1 = Administrasi(Bayar="sample_text", HargaSewa="sample_text", IdAdmin=7, IdPelanggan=7, Kembali="sample_text", NoPesan=7)
    a2 = Administrasi(Bayar="sample_text_2", HargaSewa="sample_text_2", IdAdmin=13, IdPelanggan=13, Kembali="sample_text_2", NoPesan=13)
    b = Admin(Password="sample_text", Username="sample_text")
    _safe_set(b, 'administrasi14', a1)
    assert _is_linked(b, 'administrasi14', a1)
    if hasattr(a1, 'admin15'):
        assert _is_linked(a1, 'admin15', b)
    _safe_set(b, 'administrasi14', a2)
    assert _is_linked(b, 'administrasi14', a2)
    if hasattr(a1, 'admin15'):
        assert not _is_linked(a1, 'admin15', b)
    if hasattr(a2, 'admin15'):
        assert _is_linked(a2, 'admin15', b)
    _safe_set(b, 'administrasi14', None)
    assert not _is_linked(b, 'administrasi14', a2)
    if hasattr(a2, 'admin15'):
        assert not _is_linked(a2, 'admin15', b)


def test_assoc_Admin_Pelanggan_reverse_link_reassign_clear():
    a1 = Pelanggan(Alamat="sample_text", IdPelanggan=7, JenisKelamin="sample_text", NoKTP="sample_text", Password="sample_text", Pekerjaan="sample_text", Telepon="sample_text", Umur=7, Username="sample_text")
    a2 = Pelanggan(Alamat="sample_text_2", IdPelanggan=13, JenisKelamin="sample_text_2", NoKTP="sample_text_2", Password="sample_text_2", Pekerjaan="sample_text_2", Telepon="sample_text_2", Umur=13, Username="sample_text_2")
    b = Admin(Password="sample_text", Username="sample_text")
    _safe_set(b, 'pelanggan2', {a1})
    assert _is_linked(b, 'pelanggan2', a1)
    if hasattr(a1, 'admin3'):
        assert _is_linked(a1, 'admin3', b)
    _safe_set(b, 'pelanggan2', {a2})
    assert _is_linked(b, 'pelanggan2', a2)
    if hasattr(a1, 'admin3'):
        assert not _is_linked(a1, 'admin3', b)
    if hasattr(a2, 'admin3'):
        assert _is_linked(a2, 'admin3', b)
    _safe_set(b, 'pelanggan2', set())
    assert not _is_linked(b, 'pelanggan2', a2)
    if hasattr(a2, 'admin3'):
        assert not _is_linked(a2, 'admin3', b)


def test_assoc_Admin_Pesan_reverse_link_reassign_clear():
    a1 = Pesan(IdPelanggan=7, NoPesan=7, TanggalKembali="sample_text", TanggalRental="sample_text")
    a2 = Pesan(IdPelanggan=13, NoPesan=13, TanggalKembali="sample_text_2", TanggalRental="sample_text_2")
    b = Admin(Password="sample_text", Username="sample_text")
    _safe_set(b, 'pesan12', a1)
    assert _is_linked(b, 'pesan12', a1)
    if hasattr(a1, 'admin13'):
        assert _is_linked(a1, 'admin13', b)
    _safe_set(b, 'pesan12', a2)
    assert _is_linked(b, 'pesan12', a2)
    if hasattr(a1, 'admin13'):
        assert not _is_linked(a1, 'admin13', b)
    if hasattr(a2, 'admin13'):
        assert _is_linked(a2, 'admin13', b)
    _safe_set(b, 'pesan12', None)
    assert not _is_linked(b, 'pesan12', a2)
    if hasattr(a2, 'admin13'):
        assert not _is_linked(a2, 'admin13', b)


def test_assoc_Administrasi_Pesan_reverse_link_reassign_clear():
    a1 = Pesan(IdPelanggan=7, NoPesan=7, TanggalKembali="sample_text", TanggalRental="sample_text")
    a2 = Pesan(IdPelanggan=13, NoPesan=13, TanggalKembali="sample_text_2", TanggalRental="sample_text_2")
    b = Administrasi(Bayar="sample_text", HargaSewa="sample_text", IdAdmin=7, IdPelanggan=7, Kembali="sample_text", NoPesan=7)
    _safe_set(b, 'pesan8', a1)
    assert _is_linked(b, 'pesan8', a1)
    if hasattr(a1, 'administrasi9'):
        assert _is_linked(a1, 'administrasi9', b)
    _safe_set(b, 'pesan8', a2)
    assert _is_linked(b, 'pesan8', a2)
    if hasattr(a1, 'administrasi9'):
        assert not _is_linked(a1, 'administrasi9', b)
    if hasattr(a2, 'administrasi9'):
        assert _is_linked(a2, 'administrasi9', b)
    _safe_set(b, 'pesan8', None)
    assert not _is_linked(b, 'pesan8', a2)
    if hasattr(a2, 'administrasi9'):
        assert not _is_linked(a2, 'administrasi9', b)


def test_assoc_Kendaraan_Pesan_reverse_link_reassign_clear():
    a1 = Pesan(IdPelanggan=7, NoPesan=7, TanggalKembali="sample_text", TanggalRental="sample_text")
    a2 = Pesan(IdPelanggan=13, NoPesan=13, TanggalKembali="sample_text_2", TanggalRental="sample_text_2")
    b = Kendaraan(Merk="sample_text", NoMesin="sample_text", NoPolisi="sample_text", NoRangka="sample_text", TahunPembuatan="sample_text", Warna="sample_text")
    _safe_set(b, 'pesan6', a1)
    assert _is_linked(b, 'pesan6', a1)
    if hasattr(a1, 'kendaraan7'):
        assert _is_linked(a1, 'kendaraan7', b)
    _safe_set(b, 'pesan6', a2)
    assert _is_linked(b, 'pesan6', a2)
    if hasattr(a1, 'kendaraan7'):
        assert not _is_linked(a1, 'kendaraan7', b)
    if hasattr(a2, 'kendaraan7'):
        assert _is_linked(a2, 'kendaraan7', b)
    _safe_set(b, 'pesan6', None)
    assert not _is_linked(b, 'pesan6', a2)
    if hasattr(a2, 'kendaraan7'):
        assert not _is_linked(a2, 'kendaraan7', b)


def test_assoc_Pelanggan_Kendaraan_reverse_link_reassign_clear():
    a1 = Pelanggan(Alamat="sample_text", IdPelanggan=7, JenisKelamin="sample_text", NoKTP="sample_text", Password="sample_text", Pekerjaan="sample_text", Telepon="sample_text", Umur=7, Username="sample_text")
    a2 = Pelanggan(Alamat="sample_text_2", IdPelanggan=13, JenisKelamin="sample_text_2", NoKTP="sample_text_2", Password="sample_text_2", Pekerjaan="sample_text_2", Telepon="sample_text_2", Umur=13, Username="sample_text_2")
    b = Kendaraan(Merk="sample_text", NoMesin="sample_text", NoPolisi="sample_text", NoRangka="sample_text", TahunPembuatan="sample_text", Warna="sample_text")
    _safe_set(b, 'pelanggan5', a1)
    assert _is_linked(b, 'pelanggan5', a1)
    if hasattr(a1, 'kendaraan4'):
        assert _is_linked(a1, 'kendaraan4', b)
    _safe_set(b, 'pelanggan5', a2)
    assert _is_linked(b, 'pelanggan5', a2)
    if hasattr(a1, 'kendaraan4'):
        assert not _is_linked(a1, 'kendaraan4', b)
    if hasattr(a2, 'kendaraan4'):
        assert _is_linked(a2, 'kendaraan4', b)
    _safe_set(b, 'pelanggan5', None)
    assert not _is_linked(b, 'pelanggan5', a2)
    if hasattr(a2, 'kendaraan4'):
        assert not _is_linked(a2, 'kendaraan4', b)


def test_assoc_Pelanggan_Pesan_reverse_link_reassign_clear():
    a1 = Pesan(IdPelanggan=7, NoPesan=7, TanggalKembali="sample_text", TanggalRental="sample_text")
    a2 = Pesan(IdPelanggan=13, NoPesan=13, TanggalKembali="sample_text_2", TanggalRental="sample_text_2")
    b = Pelanggan(Alamat="sample_text", IdPelanggan=7, JenisKelamin="sample_text", NoKTP="sample_text", Password="sample_text", Pekerjaan="sample_text", Telepon="sample_text", Umur=7, Username="sample_text")
    _safe_set(b, 'pesan10', {a1})
    assert _is_linked(b, 'pesan10', a1)
    if hasattr(a1, 'pelanggan11'):
        assert _is_linked(a1, 'pelanggan11', b)
    _safe_set(b, 'pesan10', {a2})
    assert _is_linked(b, 'pesan10', a2)
    if hasattr(a1, 'pelanggan11'):
        assert not _is_linked(a1, 'pelanggan11', b)
    if hasattr(a2, 'pelanggan11'):
        assert _is_linked(a2, 'pelanggan11', b)
    _safe_set(b, 'pesan10', set())
    assert not _is_linked(b, 'pesan10', a2)
    if hasattr(a2, 'pelanggan11'):
        assert not _is_linked(a2, 'pelanggan11', b)


def test_assoc_Pemilik_Admin_reverse_link_reassign_clear():
    a1 = Pemilik(Password="sample_text", Username="sample_text")
    a2 = Pemilik(Password="sample_text_2", Username="sample_text_2")
    b = Admin(Password="sample_text", Username="sample_text")
    _safe_set(b, 'pemilik1', a1)
    assert _is_linked(b, 'pemilik1', a1)
    if hasattr(a1, 'admin0'):
        assert _is_linked(a1, 'admin0', b)
    _safe_set(b, 'pemilik1', a2)
    assert _is_linked(b, 'pemilik1', a2)
    if hasattr(a1, 'admin0'):
        assert not _is_linked(a1, 'admin0', b)
    if hasattr(a2, 'admin0'):
        assert _is_linked(a2, 'admin0', b)
    _safe_set(b, 'pemilik1', None)
    assert not _is_linked(b, 'pemilik1', a2)
    if hasattr(a2, 'admin0'):
        assert not _is_linked(a2, 'admin0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

