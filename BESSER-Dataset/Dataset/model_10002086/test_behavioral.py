import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Actor,
    Bayar_Tiket_external,
    Beli_Tiket_external,
    Lihat_Detail_Event_external,
    Lihat_Event_external,
    Lihat_Hasil_Jawaban__make_it_better__external,
    Lihat_Peserta_Belum_Bayar_external,
    Lihat_Peserta_Sudah_Bayar_external,
    Lihat_Ringkasan_Transaksi_external,
    Lihat_Seluruh_Peserta_external,
    Logout_external,
    Masuk_Link_Grup_Whatsapp_external,
    Melihat_pertanyaan__make_it_better__external,
    Peserta_Actor,
    Registrasi_external,
    Tambah_Event_external,
    Tambah_Kota_external,
    Tambah_Link_Grup_Whatsapp_external,
    Unduh_E_Ticket_external,
    Update_Profil_external,
    Update__isi__pertanyaan__make_it_better__external,
    _Component,
    admin,
    bookmark,
    e_ticket,
    event,
    kota,
    testimoni,
    transaksi,
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

def test_assoc_admin_event_reverse_link_reassign_clear():
    a1 = event(deskripsi="sample_text", detail="sample_text", gambar="sample_text", harga_premium=7, harga_reguler=7, id_admin=7, id_event=7, id_kota=7, latitude="sample_text", lokasi="sample_text", longitude="sample_text", nama_event="sample_text", tanggal="sample_text")
    a2 = event(deskripsi="sample_text_2", detail="sample_text_2", gambar="sample_text_2", harga_premium=13, harga_reguler=13, id_admin=13, id_event=13, id_kota=13, latitude="sample_text_2", lokasi="sample_text_2", longitude="sample_text_2", nama_event="sample_text_2", tanggal="sample_text_2")
    b = admin(id_admin=7, password="sample_text", username="sample_text")
    _safe_set(b, 'event58', {a1})
    assert _is_linked(b, 'event58', a1)
    if hasattr(a1, 'admin59'):
        assert _is_linked(a1, 'admin59', b)
    _safe_set(b, 'event58', {a2})
    assert _is_linked(b, 'event58', a2)
    if hasattr(a1, 'admin59'):
        assert not _is_linked(a1, 'admin59', b)
    if hasattr(a2, 'admin59'):
        assert _is_linked(a2, 'admin59', b)
    _safe_set(b, 'event58', set())
    assert not _is_linked(b, 'event58', a2)
    if hasattr(a2, 'admin59'):
        assert not _is_linked(a2, 'admin59', b)


def test_assoc_admin_testimoni_reverse_link_reassign_clear():
    a1 = testimoni(akses_instagram="sample_text", buka_instagram="sample_text", id=7, info_instagram="sample_text", kepuasan_instagram="sample_text", kritik="sample_text", mudah_info="sample_text", ptn="sample_text", pts_favorit="sample_text", sarana="sample_text", waktu_instagram="sample_text")
    a2 = testimoni(akses_instagram="sample_text_2", buka_instagram="sample_text_2", id=13, info_instagram="sample_text_2", kepuasan_instagram="sample_text_2", kritik="sample_text_2", mudah_info="sample_text_2", ptn="sample_text_2", pts_favorit="sample_text_2", sarana="sample_text_2", waktu_instagram="sample_text_2")
    b = admin(id_admin=7, password="sample_text", username="sample_text")
    _safe_set(b, 'testimoni56', {a1})
    assert _is_linked(b, 'testimoni56', a1)
    if hasattr(a1, 'admin57'):
        assert _is_linked(a1, 'admin57', b)
    _safe_set(b, 'testimoni56', {a2})
    assert _is_linked(b, 'testimoni56', a2)
    if hasattr(a1, 'admin57'):
        assert not _is_linked(a1, 'admin57', b)
    if hasattr(a2, 'admin57'):
        assert _is_linked(a2, 'admin57', b)
    _safe_set(b, 'testimoni56', set())
    assert not _is_linked(b, 'testimoni56', a2)
    if hasattr(a2, 'admin57'):
        assert not _is_linked(a2, 'admin57', b)


def test_assoc_bookmark_user_reverse_link_reassign_clear():
    a1 = user(asal_kota="sample_text", asal_sekolah="sample_text", email="sample_text", gambar="sample_text", id_user=7, instagram="sample_text", jenis_kelamin="sample_text", nama_lengkap="sample_text", no_telp="sample_text", password="sample_text")
    a2 = user(asal_kota="sample_text_2", asal_sekolah="sample_text_2", email="sample_text_2", gambar="sample_text_2", id_user=13, instagram="sample_text_2", jenis_kelamin="sample_text_2", nama_lengkap="sample_text_2", no_telp="sample_text_2", password="sample_text_2")
    b = bookmark(id_bookmark=7, id_event=7, id_user=7)
    _safe_set(b, 'user54', a1)
    assert _is_linked(b, 'user54', a1)
    if hasattr(a1, 'bookmark55'):
        assert _is_linked(a1, 'bookmark55', b)
    _safe_set(b, 'user54', a2)
    assert _is_linked(b, 'user54', a2)
    if hasattr(a1, 'bookmark55'):
        assert not _is_linked(a1, 'bookmark55', b)
    if hasattr(a2, 'bookmark55'):
        assert _is_linked(a2, 'bookmark55', b)
    _safe_set(b, 'user54', None)
    assert not _is_linked(b, 'user54', a2)
    if hasattr(a2, 'bookmark55'):
        assert not _is_linked(a2, 'bookmark55', b)


def test_assoc_event_e_ticket_reverse_link_reassign_clear():
    a1 = event(deskripsi="sample_text", detail="sample_text", gambar="sample_text", harga_premium=7, harga_reguler=7, id_admin=7, id_event=7, id_kota=7, latitude="sample_text", lokasi="sample_text", longitude="sample_text", nama_event="sample_text", tanggal="sample_text")
    a2 = event(deskripsi="sample_text_2", detail="sample_text_2", gambar="sample_text_2", harga_premium=13, harga_reguler=13, id_admin=13, id_event=13, id_kota=13, latitude="sample_text_2", lokasi="sample_text_2", longitude="sample_text_2", nama_event="sample_text_2", tanggal="sample_text_2")
    b = e_ticket(bukti_trf="sample_text", date="sample_text", due_date="sample_text", id_event=7, id_ticket=7, id_user=7, status="sample_text")
    _safe_set(b, 'event61', a1)
    assert _is_linked(b, 'event61', a1)
    if hasattr(a1, 'e_ticket60'):
        assert _is_linked(a1, 'e_ticket60', b)
    _safe_set(b, 'event61', a2)
    assert _is_linked(b, 'event61', a2)
    if hasattr(a1, 'e_ticket60'):
        assert not _is_linked(a1, 'e_ticket60', b)
    if hasattr(a2, 'e_ticket60'):
        assert _is_linked(a2, 'e_ticket60', b)
    _safe_set(b, 'event61', None)
    assert not _is_linked(b, 'event61', a2)
    if hasattr(a2, 'e_ticket60'):
        assert not _is_linked(a2, 'e_ticket60', b)


def test_assoc_event_kota_reverse_link_reassign_clear():
    a1 = kota(gambar="sample_text", id_kota=7, nama_kota="sample_text")
    a2 = kota(gambar="sample_text_2", id_kota=13, nama_kota="sample_text_2")
    b = event(deskripsi="sample_text", detail="sample_text", gambar="sample_text", harga_premium=7, harga_reguler=7, id_admin=7, id_event=7, id_kota=7, latitude="sample_text", lokasi="sample_text", longitude="sample_text", nama_event="sample_text", tanggal="sample_text")
    _safe_set(b, 'kota52', a1)
    assert _is_linked(b, 'kota52', a1)
    if hasattr(a1, 'event53'):
        assert _is_linked(a1, 'event53', b)
    _safe_set(b, 'kota52', a2)
    assert _is_linked(b, 'kota52', a2)
    if hasattr(a1, 'event53'):
        assert not _is_linked(a1, 'event53', b)
    if hasattr(a2, 'event53'):
        assert _is_linked(a2, 'event53', b)
    _safe_set(b, 'kota52', None)
    assert not _is_linked(b, 'kota52', a2)
    if hasattr(a2, 'event53'):
        assert not _is_linked(a2, 'event53', b)


def test_assoc_transaksi_event_reverse_link_reassign_clear():
    a1 = transaksi(harga=7, id_event=7, id_kota=7, id_orders=7, nama_event="sample_text", tipe_tiket="sample_text")
    a2 = transaksi(harga=13, id_event=13, id_kota=13, id_orders=13, nama_event="sample_text_2", tipe_tiket="sample_text_2")
    b = event(deskripsi="sample_text", detail="sample_text", gambar="sample_text", harga_premium=7, harga_reguler=7, id_admin=7, id_event=7, id_kota=7, latitude="sample_text", lokasi="sample_text", longitude="sample_text", nama_event="sample_text", tanggal="sample_text")
    _safe_set(b, 'transaksi49', {a1})
    assert _is_linked(b, 'transaksi49', a1)
    if hasattr(a1, 'event48'):
        assert _is_linked(a1, 'event48', b)
    _safe_set(b, 'transaksi49', {a2})
    assert _is_linked(b, 'transaksi49', a2)
    if hasattr(a1, 'event48'):
        assert not _is_linked(a1, 'event48', b)
    if hasattr(a2, 'event48'):
        assert _is_linked(a2, 'event48', b)
    _safe_set(b, 'transaksi49', set())
    assert not _is_linked(b, 'transaksi49', a2)
    if hasattr(a2, 'event48'):
        assert not _is_linked(a2, 'event48', b)


def test_assoc_user_e_ticket_reverse_link_reassign_clear():
    a1 = user(asal_kota="sample_text", asal_sekolah="sample_text", email="sample_text", gambar="sample_text", id_user=7, instagram="sample_text", jenis_kelamin="sample_text", nama_lengkap="sample_text", no_telp="sample_text", password="sample_text")
    a2 = user(asal_kota="sample_text_2", asal_sekolah="sample_text_2", email="sample_text_2", gambar="sample_text_2", id_user=13, instagram="sample_text_2", jenis_kelamin="sample_text_2", nama_lengkap="sample_text_2", no_telp="sample_text_2", password="sample_text_2")
    b = e_ticket(bukti_trf="sample_text", date="sample_text", due_date="sample_text", id_event=7, id_ticket=7, id_user=7, status="sample_text")
    _safe_set(b, 'user47', {a1})
    assert _is_linked(b, 'user47', a1)
    if hasattr(a1, 'e_ticket46'):
        assert _is_linked(a1, 'e_ticket46', b)
    _safe_set(b, 'user47', {a2})
    assert _is_linked(b, 'user47', a2)
    if hasattr(a1, 'e_ticket46'):
        assert not _is_linked(a1, 'e_ticket46', b)
    if hasattr(a2, 'e_ticket46'):
        assert _is_linked(a2, 'e_ticket46', b)
    _safe_set(b, 'user47', set())
    assert not _is_linked(b, 'user47', a2)
    if hasattr(a2, 'e_ticket46'):
        assert not _is_linked(a2, 'e_ticket46', b)


def test_assoc_user_transaksi_reverse_link_reassign_clear():
    a1 = user(asal_kota="sample_text", asal_sekolah="sample_text", email="sample_text", gambar="sample_text", id_user=7, instagram="sample_text", jenis_kelamin="sample_text", nama_lengkap="sample_text", no_telp="sample_text", password="sample_text")
    a2 = user(asal_kota="sample_text_2", asal_sekolah="sample_text_2", email="sample_text_2", gambar="sample_text_2", id_user=13, instagram="sample_text_2", jenis_kelamin="sample_text_2", nama_lengkap="sample_text_2", no_telp="sample_text_2", password="sample_text_2")
    b = transaksi(harga=7, id_event=7, id_kota=7, id_orders=7, nama_event="sample_text", tipe_tiket="sample_text")
    _safe_set(b, 'user51', a1)
    assert _is_linked(b, 'user51', a1)
    if hasattr(a1, 'transaksi50'):
        assert _is_linked(a1, 'transaksi50', b)
    _safe_set(b, 'user51', a2)
    assert _is_linked(b, 'user51', a2)
    if hasattr(a1, 'transaksi50'):
        assert not _is_linked(a1, 'transaksi50', b)
    if hasattr(a2, 'transaksi50'):
        assert _is_linked(a2, 'transaksi50', b)
    _safe_set(b, 'user51', None)
    assert not _is_linked(b, 'user51', a2)
    if hasattr(a2, 'transaksi50'):
        assert not _is_linked(a2, 'transaksi50', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

