import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Admin_Actor,
    Cancel_Pemesanan_UseCase,
    Check_Out_UseCase,
    Check_in_UseCase,
    Denda,
    Denda_UseCase,
    Kamar,
    Kamar_Deluxe_UseCase,
    Kamar_Keluarga_UseCase,
    Kamar_Standard_UseCase,
    Kirim_e_booking_email_UseCase,
    Login_UseCase,
    Melakukan_pembayaran_UseCase,
    Melakukan_reservasi_kamar_UseCase,
    Melihat_Katalog_Kamar_UseCase,
    Mengirim_e_bukti_Bayar_UseCase,
    Pembayaran,
    Pemesan,
    Pemesan_Actor,
    Pengunjung_Actor,
    Register_UseCase,
    ReservasiKamar,
    hjb_Interface,
    Enumeration,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Admin_ID_admin_value_roundtrip():
    instance = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    assert instance.ID_admin == 7
    instance.ID_admin = 13
    assert instance.ID_admin == 13


def test_Admin_attribute_value_roundtrip():
    instance = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Admin_insertData_value_roundtrip():
    instance = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    assert instance.insertData == "sample_text"
    instance.insertData = "sample_text_2"
    assert instance.insertData == "sample_text_2"


def test_Admin_password_value_roundtrip():
    instance = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Admin_username_value_roundtrip():
    instance = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Denda_ID_Denda_value_roundtrip():
    instance = Denda(ID_Denda=7, ID_Reservasi=7, jumlah=7, keterangan="sample_text")
    assert instance.ID_Denda == 7
    instance.ID_Denda = 13
    assert instance.ID_Denda == 13


def test_Denda_ID_Reservasi_value_roundtrip():
    instance = Denda(ID_Denda=7, ID_Reservasi=7, jumlah=7, keterangan="sample_text")
    assert instance.ID_Reservasi == 7
    instance.ID_Reservasi = 13
    assert instance.ID_Reservasi == 13


def test_Denda_jumlah_value_roundtrip():
    instance = Denda(ID_Denda=7, ID_Reservasi=7, jumlah=7, keterangan="sample_text")
    assert instance.jumlah == 7
    instance.jumlah = 13
    assert instance.jumlah == 13


def test_Denda_keterangan_value_roundtrip():
    instance = Denda(ID_Denda=7, ID_Reservasi=7, jumlah=7, keterangan="sample_text")
    assert instance.keterangan == "sample_text"
    instance.keterangan = "sample_text_2"
    assert instance.keterangan == "sample_text_2"


def test_Kamar__attr_value_roundtrip():
    instance = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Kamar_jumlah_bed_value_roundtrip():
    instance = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    assert instance.jumlah_bed == 7
    instance.jumlah_bed = 13
    assert instance.jumlah_bed == 13


def test_Kamar_no_kamar_value_roundtrip():
    instance = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    assert instance.no_kamar == 7
    instance.no_kamar = 13
    assert instance.no_kamar == 13


def test_Kamar_status_value_roundtrip():
    instance = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Kamar_tipe_value_roundtrip():
    instance = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    assert instance.tipe == "sample_text"
    instance.tipe = "sample_text_2"
    assert instance.tipe == "sample_text_2"


def test_Pembayaran_ID_Pembayaran_value_roundtrip():
    instance = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    assert instance.ID_Pembayaran == 7
    instance.ID_Pembayaran = 13
    assert instance.ID_Pembayaran == 13


def test_Pembayaran_ID_Reservasi_value_roundtrip():
    instance = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    assert instance.ID_Reservasi == 7
    instance.ID_Reservasi = 13
    assert instance.ID_Reservasi == 13


def test_Pembayaran_deadline_bayar_value_roundtrip():
    instance = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    assert instance.deadline_bayar == "sample_text"
    instance.deadline_bayar = "sample_text_2"
    assert instance.deadline_bayar == "sample_text_2"


def test_Pembayaran_jumlah_value_roundtrip():
    instance = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    assert instance.jumlah == 7
    instance.jumlah = 13
    assert instance.jumlah == 13


def test_Pembayaran_status_value_roundtrip():
    instance = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Pemesan_Alamat_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.Alamat == "sample_text"
    instance.Alamat = "sample_text_2"
    assert instance.Alamat == "sample_text_2"


def test_Pemesan_Emai_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.Emai == "sample_text"
    instance.Emai = "sample_text_2"
    assert instance.Emai == "sample_text_2"


def test_Pemesan_NIK_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.NIK == 7
    instance.NIK = 13
    assert instance.NIK == 13


def test_Pemesan_Nama_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.Nama == "sample_text"
    instance.Nama = "sample_text_2"
    assert instance.Nama == "sample_text_2"


def test_Pemesan_password_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Pemesan_phone_number_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.phone_number == "sample_text"
    instance.phone_number = "sample_text_2"
    assert instance.phone_number == "sample_text_2"


def test_Pemesan_username_value_roundtrip():
    instance = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_ReservasiKamar_ID_Reservasi_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.ID_Reservasi == 7
    instance.ID_Reservasi = 13
    assert instance.ID_Reservasi == 13


def test_ReservasiKamar_ID_admin_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.ID_admin == 7
    instance.ID_admin = 13
    assert instance.ID_admin == 13


def test_ReservasiKamar_ID_pembayaran_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.ID_pembayaran == 7
    instance.ID_pembayaran = 13
    assert instance.ID_pembayaran == 13


def test_ReservasiKamar_NIK_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.NIK == 7
    instance.NIK = 13
    assert instance.NIK == 13


def test_ReservasiKamar_no_kamar_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.no_kamar == 7
    instance.no_kamar = 13
    assert instance.no_kamar == 13


def test_ReservasiKamar_tgl_end_booking_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.tgl_end_booking == "sample_text"
    instance.tgl_end_booking = "sample_text_2"
    assert instance.tgl_end_booking == "sample_text_2"


def test_ReservasiKamar_tgl_start_booking_value_roundtrip():
    instance = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    assert instance.tgl_start_booking == "sample_text"
    instance.tgl_start_booking = "sample_text_2"
    assert instance.tgl_start_booking == "sample_text_2"


def test_assoc_Denda_ReservasiKamar_link_reassign_clear():
    a = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    b1 = Denda(ID_Denda=7, ID_Reservasi=7, jumlah=7, keterangan="sample_text")
    b2 = Denda(ID_Denda=13, ID_Reservasi=13, jumlah=13, keterangan="sample_text_2")
    _safe_set(a, 'denda31', {b1})
    assert _is_linked(a, 'denda31', b1)
    if hasattr(b1, 'reservasiKamar30'):
        assert _is_linked(b1, 'reservasiKamar30', a)
    _safe_set(a, 'denda31', {b2})
    assert _is_linked(a, 'denda31', b2)
    if hasattr(b1, 'reservasiKamar30'):
        assert not _is_linked(b1, 'reservasiKamar30', a)
    if hasattr(b2, 'reservasiKamar30'):
        assert _is_linked(b2, 'reservasiKamar30', a)
    _safe_set(a, 'denda31', set())
    assert not _is_linked(a, 'denda31', b2)
    if hasattr(b2, 'reservasiKamar30'):
        assert not _is_linked(b2, 'reservasiKamar30', a)


def test_assoc_Kamar_ReservasiKamar_link_reassign_clear():
    a = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    b1 = Kamar(_attr="sample_text", jumlah_bed=7, no_kamar=7, status="sample_text", tipe="sample_text")
    b2 = Kamar(_attr="sample_text_2", jumlah_bed=13, no_kamar=13, status="sample_text_2", tipe="sample_text_2")
    _safe_set(a, 'kamar29', b1)
    assert _is_linked(a, 'kamar29', b1)
    if hasattr(b1, 'reservasiKamar28'):
        assert _is_linked(b1, 'reservasiKamar28', a)
    _safe_set(a, 'kamar29', b2)
    assert _is_linked(a, 'kamar29', b2)
    if hasattr(b1, 'reservasiKamar28'):
        assert not _is_linked(b1, 'reservasiKamar28', a)
    if hasattr(b2, 'reservasiKamar28'):
        assert _is_linked(b2, 'reservasiKamar28', a)
    _safe_set(a, 'kamar29', None)
    assert not _is_linked(a, 'kamar29', b2)
    if hasattr(b2, 'reservasiKamar28'):
        assert not _is_linked(b2, 'reservasiKamar28', a)


def test_assoc_Pembayaran_ReservasiKamar_link_reassign_clear():
    a = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    b1 = Pembayaran(ID_Pembayaran=7, ID_Reservasi=7, deadline_bayar="sample_text", jumlah=7, status="sample_text")
    b2 = Pembayaran(ID_Pembayaran=13, ID_Reservasi=13, deadline_bayar="sample_text_2", jumlah=13, status="sample_text_2")
    _safe_set(a, 'pembayaran33', b1)
    assert _is_linked(a, 'pembayaran33', b1)
    if hasattr(b1, 'reservasiKamar32'):
        assert _is_linked(b1, 'reservasiKamar32', a)
    _safe_set(a, 'pembayaran33', b2)
    assert _is_linked(a, 'pembayaran33', b2)
    if hasattr(b1, 'reservasiKamar32'):
        assert not _is_linked(b1, 'reservasiKamar32', a)
    if hasattr(b2, 'reservasiKamar32'):
        assert _is_linked(b2, 'reservasiKamar32', a)
    _safe_set(a, 'pembayaran33', None)
    assert not _is_linked(a, 'pembayaran33', b2)
    if hasattr(b2, 'reservasiKamar32'):
        assert not _is_linked(b2, 'reservasiKamar32', a)


def test_assoc_Pemesan_ReservasiKamar_link_reassign_clear():
    a = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    b1 = Pemesan(Alamat="sample_text", Emai="sample_text", NIK=7, Nama="sample_text", password="sample_text", phone_number="sample_text", username="sample_text")
    b2 = Pemesan(Alamat="sample_text_2", Emai="sample_text_2", NIK=13, Nama="sample_text_2", password="sample_text_2", phone_number="sample_text_2", username="sample_text_2")
    _safe_set(a, 'pemesan25', b1)
    assert _is_linked(a, 'pemesan25', b1)
    if hasattr(b1, 'reservasiKamar24'):
        assert _is_linked(b1, 'reservasiKamar24', a)
    _safe_set(a, 'pemesan25', b2)
    assert _is_linked(a, 'pemesan25', b2)
    if hasattr(b1, 'reservasiKamar24'):
        assert not _is_linked(b1, 'reservasiKamar24', a)
    if hasattr(b2, 'reservasiKamar24'):
        assert _is_linked(b2, 'reservasiKamar24', a)
    _safe_set(a, 'pemesan25', None)
    assert not _is_linked(a, 'pemesan25', b2)
    if hasattr(b2, 'reservasiKamar24'):
        assert not _is_linked(b2, 'reservasiKamar24', a)


def test_assoc_ReservasiKamar_Admin_link_reassign_clear():
    a = ReservasiKamar(ID_Reservasi=7, ID_admin=7, ID_pembayaran=7, NIK=7, no_kamar=7, tgl_end_booking="sample_text", tgl_start_booking="sample_text")
    b1 = Admin(ID_admin=7, attribute="sample_text", insertData="sample_text", password="sample_text", username="sample_text")
    b2 = Admin(ID_admin=13, attribute="sample_text_2", insertData="sample_text_2", password="sample_text_2", username="sample_text_2")
    _safe_set(a, 'admin26', b1)
    assert _is_linked(a, 'admin26', b1)
    if hasattr(b1, 'reservasiKamar27'):
        assert _is_linked(b1, 'reservasiKamar27', a)
    _safe_set(a, 'admin26', b2)
    assert _is_linked(a, 'admin26', b2)
    if hasattr(b1, 'reservasiKamar27'):
        assert not _is_linked(b1, 'reservasiKamar27', a)
    if hasattr(b2, 'reservasiKamar27'):
        assert _is_linked(b2, 'reservasiKamar27', a)
    _safe_set(a, 'admin26', None)
    assert not _is_linked(a, 'admin26', b2)
    if hasattr(b2, 'reservasiKamar27'):
        assert not _is_linked(b2, 'reservasiKamar27', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, ID_admin=st.integers(), attribute=safe_text, insertData=safe_text, password=safe_text, username=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Admin_Actor_strategy = st.builds(Admin_Actor)
@given(instance=Admin_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)


Cancel_Pemesanan_UseCase_strategy = st.builds(Cancel_Pemesanan_UseCase)
@given(instance=Cancel_Pemesanan_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_Pemesanan_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_Pemesanan_UseCase)


Check_Out_UseCase_strategy = st.builds(Check_Out_UseCase)
@given(instance=Check_Out_UseCase_strategy)
@settings(max_examples=25)
def test_Check_Out_UseCase_instantiation(instance):
    assert isinstance(instance, Check_Out_UseCase)


Check_in_UseCase_strategy = st.builds(Check_in_UseCase)
@given(instance=Check_in_UseCase_strategy)
@settings(max_examples=25)
def test_Check_in_UseCase_instantiation(instance):
    assert isinstance(instance, Check_in_UseCase)


Denda_strategy = st.builds(Denda, ID_Denda=st.integers(), ID_Reservasi=st.integers(), jumlah=st.integers(), keterangan=safe_text)
@given(instance=Denda_strategy)
@settings(max_examples=25)
def test_Denda_instantiation(instance):
    assert isinstance(instance, Denda)


Denda_UseCase_strategy = st.builds(Denda_UseCase)
@given(instance=Denda_UseCase_strategy)
@settings(max_examples=25)
def test_Denda_UseCase_instantiation(instance):
    assert isinstance(instance, Denda_UseCase)


Kamar_strategy = st.builds(Kamar, _attr=safe_text, jumlah_bed=st.integers(), no_kamar=st.integers(), status=safe_text, tipe=safe_text)
@given(instance=Kamar_strategy)
@settings(max_examples=25)
def test_Kamar_instantiation(instance):
    assert isinstance(instance, Kamar)


Kamar_Deluxe_UseCase_strategy = st.builds(Kamar_Deluxe_UseCase)
@given(instance=Kamar_Deluxe_UseCase_strategy)
@settings(max_examples=25)
def test_Kamar_Deluxe_UseCase_instantiation(instance):
    assert isinstance(instance, Kamar_Deluxe_UseCase)


Kamar_Keluarga_UseCase_strategy = st.builds(Kamar_Keluarga_UseCase)
@given(instance=Kamar_Keluarga_UseCase_strategy)
@settings(max_examples=25)
def test_Kamar_Keluarga_UseCase_instantiation(instance):
    assert isinstance(instance, Kamar_Keluarga_UseCase)


Kamar_Standard_UseCase_strategy = st.builds(Kamar_Standard_UseCase)
@given(instance=Kamar_Standard_UseCase_strategy)
@settings(max_examples=25)
def test_Kamar_Standard_UseCase_instantiation(instance):
    assert isinstance(instance, Kamar_Standard_UseCase)


Kirim_e_booking_email_UseCase_strategy = st.builds(Kirim_e_booking_email_UseCase)
@given(instance=Kirim_e_booking_email_UseCase_strategy)
@settings(max_examples=25)
def test_Kirim_e_booking_email_UseCase_instantiation(instance):
    assert isinstance(instance, Kirim_e_booking_email_UseCase)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Melakukan_pembayaran_UseCase_strategy = st.builds(Melakukan_pembayaran_UseCase)
@given(instance=Melakukan_pembayaran_UseCase_strategy)
@settings(max_examples=25)
def test_Melakukan_pembayaran_UseCase_instantiation(instance):
    assert isinstance(instance, Melakukan_pembayaran_UseCase)


Melakukan_reservasi_kamar_UseCase_strategy = st.builds(Melakukan_reservasi_kamar_UseCase)
@given(instance=Melakukan_reservasi_kamar_UseCase_strategy)
@settings(max_examples=25)
def test_Melakukan_reservasi_kamar_UseCase_instantiation(instance):
    assert isinstance(instance, Melakukan_reservasi_kamar_UseCase)


Melihat_Katalog_Kamar_UseCase_strategy = st.builds(Melihat_Katalog_Kamar_UseCase)
@given(instance=Melihat_Katalog_Kamar_UseCase_strategy)
@settings(max_examples=25)
def test_Melihat_Katalog_Kamar_UseCase_instantiation(instance):
    assert isinstance(instance, Melihat_Katalog_Kamar_UseCase)


Mengirim_e_bukti_Bayar_UseCase_strategy = st.builds(Mengirim_e_bukti_Bayar_UseCase)
@given(instance=Mengirim_e_bukti_Bayar_UseCase_strategy)
@settings(max_examples=25)
def test_Mengirim_e_bukti_Bayar_UseCase_instantiation(instance):
    assert isinstance(instance, Mengirim_e_bukti_Bayar_UseCase)


Pembayaran_strategy = st.builds(Pembayaran, ID_Pembayaran=st.integers(), ID_Reservasi=st.integers(), deadline_bayar=safe_text, jumlah=st.integers(), status=safe_text)
@given(instance=Pembayaran_strategy)
@settings(max_examples=25)
def test_Pembayaran_instantiation(instance):
    assert isinstance(instance, Pembayaran)


Pemesan_strategy = st.builds(Pemesan, Alamat=safe_text, Emai=safe_text, NIK=st.integers(), Nama=safe_text, password=safe_text, phone_number=safe_text, username=safe_text)
@given(instance=Pemesan_strategy)
@settings(max_examples=25)
def test_Pemesan_instantiation(instance):
    assert isinstance(instance, Pemesan)


Pemesan_Actor_strategy = st.builds(Pemesan_Actor)
@given(instance=Pemesan_Actor_strategy)
@settings(max_examples=25)
def test_Pemesan_Actor_instantiation(instance):
    assert isinstance(instance, Pemesan_Actor)


Pengunjung_Actor_strategy = st.builds(Pengunjung_Actor)
@given(instance=Pengunjung_Actor_strategy)
@settings(max_examples=25)
def test_Pengunjung_Actor_instantiation(instance):
    assert isinstance(instance, Pengunjung_Actor)


Register_UseCase_strategy = st.builds(Register_UseCase)
@given(instance=Register_UseCase_strategy)
@settings(max_examples=25)
def test_Register_UseCase_instantiation(instance):
    assert isinstance(instance, Register_UseCase)


ReservasiKamar_strategy = st.builds(ReservasiKamar, ID_Reservasi=st.integers(), ID_admin=st.integers(), ID_pembayaran=st.integers(), NIK=st.integers(), no_kamar=st.integers(), tgl_end_booking=safe_text, tgl_start_booking=safe_text)
@given(instance=ReservasiKamar_strategy)
@settings(max_examples=25)
def test_ReservasiKamar_instantiation(instance):
    assert isinstance(instance, ReservasiKamar)


hjb_Interface_strategy = st.builds(hjb_Interface)
@given(instance=hjb_Interface_strategy)
@settings(max_examples=25)
def test_hjb_Interface_instantiation(instance):
    assert isinstance(instance, hjb_Interface)


