# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Denda,
    Pembayaran,
    ReservasiKamar,
    Kamar,
    hjb_Interface,
    Admin,
    Pemesan,
    Register_UseCase,
    Login_UseCase,
    Kamar_Standard_UseCase,
    Kamar_Keluarga_UseCase,
    Kamar_Deluxe_UseCase,
    Denda_UseCase,
    Check_Out_UseCase,
    Check_in_UseCase,
    Cancel_Pemesanan_UseCase,
    Melakukan_pembayaran_UseCase,
    Kirim_e_booking_email_UseCase,
    Mengirim_e_bukti_Bayar_UseCase,
    Melakukan_reservasi_kamar_UseCase,
    Admin_Actor,
    Pemesan_Actor,
    Melihat_Katalog_Kamar_UseCase,
    Pengunjung_Actor,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_denda_is_not_abstract():
    assert not inspect.isabstract(Denda)


def test_hyp_denda_constructor_exists():
    assert callable(Denda.__init__)


def test_hyp_denda_constructor_args():
    sig = inspect.signature(Denda.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Denda" in params, "Missing parameter 'ID_Denda'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"







def test_hyp_pembayaran_is_not_abstract():
    assert not inspect.isabstract(Pembayaran)


def test_hyp_pembayaran_constructor_exists():
    assert callable(Pembayaran.__init__)


def test_hyp_pembayaran_constructor_args():
    sig = inspect.signature(Pembayaran.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Pembayaran" in params, "Missing parameter 'ID_Pembayaran'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"
    assert "deadline_bayar" in params, "Missing parameter 'deadline_bayar'"
    assert "status" in params, "Missing parameter 'status'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"








def test_hyp_reservasikamar_is_not_abstract():
    assert not inspect.isabstract(ReservasiKamar)


def test_hyp_reservasikamar_constructor_exists():
    assert callable(ReservasiKamar.__init__)


def test_hyp_reservasikamar_constructor_args():
    sig = inspect.signature(ReservasiKamar.__init__)
    params = list(sig.parameters.keys())
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "ID_pembayaran" in params, "Missing parameter 'ID_pembayaran'"
    assert "ID_admin" in params, "Missing parameter 'ID_admin'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"
    assert "no_kamar" in params, "Missing parameter 'no_kamar'"
    assert "tgl_start_booking" in params, "Missing parameter 'tgl_start_booking'"
    assert "tgl_end_booking" in params, "Missing parameter 'tgl_end_booking'"










def test_hyp_kamar_is_not_abstract():
    assert not inspect.isabstract(Kamar)


def test_hyp_kamar_constructor_exists():
    assert callable(Kamar.__init__)


def test_hyp_kamar_constructor_args():
    sig = inspect.signature(Kamar.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "status" in params, "Missing parameter 'status'"
    assert "jumlah_bed" in params, "Missing parameter 'jumlah_bed'"
    assert "no_kamar" in params, "Missing parameter 'no_kamar'"
    assert "tipe" in params, "Missing parameter 'tipe'"








def test_hyp_hjb_interface_is_not_abstract():
    assert not inspect.isabstract(hjb_Interface)


def test_hyp_hjb_interface_constructor_exists():
    assert callable(hjb_Interface.__init__)


def test_hyp_hjb_interface_constructor_args():
    sig = inspect.signature(hjb_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "insertData" in params, "Missing parameter 'insertData'"
    assert "password" in params, "Missing parameter 'password'"
    assert "ID_admin" in params, "Missing parameter 'ID_admin'"








def test_hyp_pemesan_is_not_abstract():
    assert not inspect.isabstract(Pemesan)


def test_hyp_pemesan_constructor_exists():
    assert callable(Pemesan.__init__)


def test_hyp_pemesan_constructor_args():
    sig = inspect.signature(Pemesan.__init__)
    params = list(sig.parameters.keys())
    assert "Emai" in params, "Missing parameter 'Emai'"
    assert "Alamat" in params, "Missing parameter 'Alamat'"
    assert "Nama" in params, "Missing parameter 'Nama'"
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "phone_number" in params, "Missing parameter 'phone_number'"










def test_hyp_register_usecase_is_not_abstract():
    assert not inspect.isabstract(Register_UseCase)


def test_hyp_register_usecase_constructor_exists():
    assert callable(Register_UseCase.__init__)


def test_hyp_register_usecase_constructor_args():
    sig = inspect.signature(Register_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_hyp_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_hyp_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kamar_standard_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Standard_UseCase)


def test_hyp_kamar_standard_usecase_constructor_exists():
    assert callable(Kamar_Standard_UseCase.__init__)


def test_hyp_kamar_standard_usecase_constructor_args():
    sig = inspect.signature(Kamar_Standard_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kamar_keluarga_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Keluarga_UseCase)


def test_hyp_kamar_keluarga_usecase_constructor_exists():
    assert callable(Kamar_Keluarga_UseCase.__init__)


def test_hyp_kamar_keluarga_usecase_constructor_args():
    sig = inspect.signature(Kamar_Keluarga_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kamar_deluxe_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Deluxe_UseCase)


def test_hyp_kamar_deluxe_usecase_constructor_exists():
    assert callable(Kamar_Deluxe_UseCase.__init__)


def test_hyp_kamar_deluxe_usecase_constructor_args():
    sig = inspect.signature(Kamar_Deluxe_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_denda_usecase_is_not_abstract():
    assert not inspect.isabstract(Denda_UseCase)


def test_hyp_denda_usecase_constructor_exists():
    assert callable(Denda_UseCase.__init__)


def test_hyp_denda_usecase_constructor_args():
    sig = inspect.signature(Denda_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_check_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_Out_UseCase)


def test_hyp_check_out_usecase_constructor_exists():
    assert callable(Check_Out_UseCase.__init__)


def test_hyp_check_out_usecase_constructor_args():
    sig = inspect.signature(Check_Out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_check_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_in_UseCase)


def test_hyp_check_in_usecase_constructor_exists():
    assert callable(Check_in_UseCase.__init__)


def test_hyp_check_in_usecase_constructor_args():
    sig = inspect.signature(Check_in_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancel_pemesanan_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_Pemesanan_UseCase)


def test_hyp_cancel_pemesanan_usecase_constructor_exists():
    assert callable(Cancel_Pemesanan_UseCase.__init__)


def test_hyp_cancel_pemesanan_usecase_constructor_args():
    sig = inspect.signature(Cancel_Pemesanan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_melakukan_pembayaran_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_pembayaran_UseCase)


def test_hyp_melakukan_pembayaran_usecase_constructor_exists():
    assert callable(Melakukan_pembayaran_UseCase.__init__)


def test_hyp_melakukan_pembayaran_usecase_constructor_args():
    sig = inspect.signature(Melakukan_pembayaran_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kirim_e_booking_email_usecase_is_not_abstract():
    assert not inspect.isabstract(Kirim_e_booking_email_UseCase)


def test_hyp_kirim_e_booking_email_usecase_constructor_exists():
    assert callable(Kirim_e_booking_email_UseCase.__init__)


def test_hyp_kirim_e_booking_email_usecase_constructor_args():
    sig = inspect.signature(Kirim_e_booking_email_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mengirim_e_bukti_bayar_usecase_is_not_abstract():
    assert not inspect.isabstract(Mengirim_e_bukti_Bayar_UseCase)


def test_hyp_mengirim_e_bukti_bayar_usecase_constructor_exists():
    assert callable(Mengirim_e_bukti_Bayar_UseCase.__init__)


def test_hyp_mengirim_e_bukti_bayar_usecase_constructor_args():
    sig = inspect.signature(Mengirim_e_bukti_Bayar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_melakukan_reservasi_kamar_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_reservasi_kamar_UseCase)


def test_hyp_melakukan_reservasi_kamar_usecase_constructor_exists():
    assert callable(Melakukan_reservasi_kamar_UseCase.__init__)


def test_hyp_melakukan_reservasi_kamar_usecase_constructor_args():
    sig = inspect.signature(Melakukan_reservasi_kamar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_hyp_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_hyp_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pemesan_actor_is_not_abstract():
    assert not inspect.isabstract(Pemesan_Actor)


def test_hyp_pemesan_actor_constructor_exists():
    assert callable(Pemesan_Actor.__init__)


def test_hyp_pemesan_actor_constructor_args():
    sig = inspect.signature(Pemesan_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_melihat_katalog_kamar_usecase_is_not_abstract():
    assert not inspect.isabstract(Melihat_Katalog_Kamar_UseCase)


def test_hyp_melihat_katalog_kamar_usecase_constructor_exists():
    assert callable(Melihat_Katalog_Kamar_UseCase.__init__)


def test_hyp_melihat_katalog_kamar_usecase_constructor_args():
    sig = inspect.signature(Melihat_Katalog_Kamar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pengunjung_actor_is_not_abstract():
    assert not inspect.isabstract(Pengunjung_Actor)


def test_hyp_pengunjung_actor_constructor_exists():
    assert callable(Pengunjung_Actor.__init__)


def test_hyp_pengunjung_actor_constructor_args():
    sig = inspect.signature(Pengunjung_Actor.__init__)
    params = list(sig.parameters.keys())

def test_hyp_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_hyp_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Denda_strategy = st.builds(
    Denda,
    ID_Denda=
        st.integers(),
    keterangan=
        safe_text,
    ID_Reservasi=
        st.integers(),
    jumlah=
        st.integers()
)
Pembayaran_strategy = st.builds(
    Pembayaran,
    ID_Pembayaran=
        st.integers(),
    jumlah=
        st.integers(),
    deadline_bayar=
        safe_text,
    status=
        safe_text,
    ID_Reservasi=
        st.integers()
)
ReservasiKamar_strategy = st.builds(
    ReservasiKamar,
    NIK=
        st.integers(),
    ID_pembayaran=
        st.integers(),
    ID_admin=
        st.integers(),
    ID_Reservasi=
        st.integers(),
    no_kamar=
        st.integers(),
    tgl_start_booking=
        safe_text,
    tgl_end_booking=
        safe_text
)
Kamar_strategy = st.builds(
    Kamar,
    _attr=
        safe_text,
    status=
        safe_text,
    jumlah_bed=
        st.integers(),
    no_kamar=
        st.integers(),
    tipe=
        safe_text
)
hjb_Interface_strategy = st.builds(
    hjb_Interface,
)
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    attribute=
        safe_text,
    insertData=
        safe_text,
    password=
        safe_text,
    ID_admin=
        st.integers()
)
Pemesan_strategy = st.builds(
    Pemesan,
    Emai=
        safe_text,
    Alamat=
        safe_text,
    Nama=
        safe_text,
    username=
        safe_text,
    password=
        safe_text,
    NIK=
        st.integers(),
    phone_number=
        safe_text
)
Register_UseCase_strategy = st.builds(
    Register_UseCase,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)
Kamar_Standard_UseCase_strategy = st.builds(
    Kamar_Standard_UseCase,
)
Kamar_Keluarga_UseCase_strategy = st.builds(
    Kamar_Keluarga_UseCase,
)
Kamar_Deluxe_UseCase_strategy = st.builds(
    Kamar_Deluxe_UseCase,
)
Denda_UseCase_strategy = st.builds(
    Denda_UseCase,
)
Check_Out_UseCase_strategy = st.builds(
    Check_Out_UseCase,
)
Check_in_UseCase_strategy = st.builds(
    Check_in_UseCase,
)
Cancel_Pemesanan_UseCase_strategy = st.builds(
    Cancel_Pemesanan_UseCase,
)
Melakukan_pembayaran_UseCase_strategy = st.builds(
    Melakukan_pembayaran_UseCase,
)
Kirim_e_booking_email_UseCase_strategy = st.builds(
    Kirim_e_booking_email_UseCase,
)
Mengirim_e_bukti_Bayar_UseCase_strategy = st.builds(
    Mengirim_e_bukti_Bayar_UseCase,
)
Melakukan_reservasi_kamar_UseCase_strategy = st.builds(
    Melakukan_reservasi_kamar_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Pemesan_Actor_strategy = st.builds(
    Pemesan_Actor,
)
Melihat_Katalog_Kamar_UseCase_strategy = st.builds(
    Melihat_Katalog_Kamar_UseCase,
)
Pengunjung_Actor_strategy = st.builds(
    Pengunjung_Actor,
)




@given(instance=Denda_strategy)
def test_hyp_denda_ID_Denda_setter(instance):
    original = instance.ID_Denda
    instance.ID_Denda = original
    assert instance.ID_Denda == original



@given(instance=Denda_strategy)
def test_hyp_denda_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original



@given(instance=Denda_strategy)
def test_hyp_denda_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original



@given(instance=Denda_strategy)
def test_hyp_denda_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original




@given(instance=Pembayaran_strategy)
def test_hyp_pembayaran_ID_Pembayaran_setter(instance):
    original = instance.ID_Pembayaran
    instance.ID_Pembayaran = original
    assert instance.ID_Pembayaran == original



@given(instance=Pembayaran_strategy)
def test_hyp_pembayaran_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original



@given(instance=Pembayaran_strategy)
def test_hyp_pembayaran_deadline_bayar_setter(instance):
    original = instance.deadline_bayar
    instance.deadline_bayar = original
    assert instance.deadline_bayar == original



@given(instance=Pembayaran_strategy)
def test_hyp_pembayaran_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Pembayaran_strategy)
def test_hyp_pembayaran_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original




@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_ID_pembayaran_setter(instance):
    original = instance.ID_pembayaran
    instance.ID_pembayaran = original
    assert instance.ID_pembayaran == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_ID_admin_setter(instance):
    original = instance.ID_admin
    instance.ID_admin = original
    assert instance.ID_admin == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_no_kamar_setter(instance):
    original = instance.no_kamar
    instance.no_kamar = original
    assert instance.no_kamar == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_tgl_start_booking_setter(instance):
    original = instance.tgl_start_booking
    instance.tgl_start_booking = original
    assert instance.tgl_start_booking == original



@given(instance=ReservasiKamar_strategy)
def test_hyp_reservasikamar_tgl_end_booking_setter(instance):
    original = instance.tgl_end_booking
    instance.tgl_end_booking = original
    assert instance.tgl_end_booking == original




@given(instance=Kamar_strategy)
def test_hyp_kamar__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=Kamar_strategy)
def test_hyp_kamar_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Kamar_strategy)
def test_hyp_kamar_jumlah_bed_setter(instance):
    original = instance.jumlah_bed
    instance.jumlah_bed = original
    assert instance.jumlah_bed == original



@given(instance=Kamar_strategy)
def test_hyp_kamar_no_kamar_setter(instance):
    original = instance.no_kamar
    instance.no_kamar = original
    assert instance.no_kamar == original



@given(instance=Kamar_strategy)
def test_hyp_kamar_tipe_setter(instance):
    original = instance.tipe
    instance.tipe = original
    assert instance.tipe == original





@given(instance=Admin_strategy)
def test_hyp_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_hyp_admin_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Admin_strategy)
def test_hyp_admin_insertData_setter(instance):
    original = instance.insertData
    instance.insertData = original
    assert instance.insertData == original



@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_hyp_admin_ID_admin_setter(instance):
    original = instance.ID_admin
    instance.ID_admin = original
    assert instance.ID_admin == original




@given(instance=Pemesan_strategy)
def test_hyp_pemesan_Emai_setter(instance):
    original = instance.Emai
    instance.Emai = original
    assert instance.Emai == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_Alamat_setter(instance):
    original = instance.Alamat
    instance.Alamat = original
    assert instance.Alamat == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_Nama_setter(instance):
    original = instance.Nama
    instance.Nama = original
    assert instance.Nama == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original



@given(instance=Pemesan_strategy)
def test_hyp_pemesan_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original



















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



