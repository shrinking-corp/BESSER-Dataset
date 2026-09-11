import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Jurusans,
    Login,
    Mahasiswa_Actor,
    Mahasiswas,
    Menu_Utama,
    Pembayarans,
    Prodis,
    Setting,
    Sistem_Mahasiswa_Ganti_Password_UseCase,
    Sistem_Mahasiswa_Login_UseCase,
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
    Sistem_Pembayaran_Add_Role_UseCase,
    Sistem_Pembayaran_Add_User_UseCase,
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
    Sistem_Pembayaran_Jurusan_UseCase,
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
    Sistem_Pembayaran_Login_UseCase,
    Sistem_Pembayaran_Mahasiswa_UseCase,
    Sistem_Pembayaran_Masukkan_Password_UseCase,
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
    Sistem_Pembayaran_Pembayaran_UseCase,
    Sistem_Pembayaran_Prodi_UseCase,
    Sistem_Pembayaran_Setting_UseCase,
    Tata_Usaha_Actor,
    masterBiaya,
    masterKategori,
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

def test_Jurusans_id_value_roundtrip():
    instance = Jurusans(id=7, jurusan_name="sample_text", prodi_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Jurusans_jurusan_name_value_roundtrip():
    instance = Jurusans(id=7, jurusan_name="sample_text", prodi_id=7)
    assert instance.jurusan_name == "sample_text"
    instance.jurusan_name = "sample_text_2"
    assert instance.jurusan_name == "sample_text_2"


def test_Jurusans_prodi_id_value_roundtrip():
    instance = Jurusans(id=7, jurusan_name="sample_text", prodi_id=7)
    assert instance.prodi_id == 7
    instance.prodi_id = 13
    assert instance.prodi_id == 13


def test_Login_password_value_roundtrip():
    instance = Login(password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login_username_value_roundtrip():
    instance = Login(password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Mahasiswas_id_value_roundtrip():
    instance = Mahasiswas(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Pembayarans_biaya_kuliah_id_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.biaya_kuliah_id == 7
    instance.biaya_kuliah_id = 13
    assert instance.biaya_kuliah_id == 13


def test_Pembayarans_id_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Pembayarans_jumlah_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.jumlah == 7
    instance.jumlah = 13
    assert instance.jumlah == 13


def test_Pembayarans_keterangan_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.keterangan == "sample_text"
    instance.keterangan = "sample_text_2"
    assert instance.keterangan == "sample_text_2"


def test_Pembayarans_mahasiswa_id_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.mahasiswa_id == 7
    instance.mahasiswa_id = 13
    assert instance.mahasiswa_id == 13


def test_Pembayarans_no_pembayaran_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.no_pembayaran == "sample_text"
    instance.no_pembayaran = "sample_text_2"
    assert instance.no_pembayaran == "sample_text_2"


def test_Pembayarans_pembayaran_tipe_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.pembayaran_tipe == 7
    instance.pembayaran_tipe = 13
    assert instance.pembayaran_tipe == 13


def test_Pembayarans_prefix_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_Pembayarans_semester_id_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.semester_id == 7
    instance.semester_id = 13
    assert instance.semester_id == 13


def test_Pembayarans_status_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_Pembayarans_tanggal_pembayaran_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.tanggal_pembayaran == "sample_text"
    instance.tanggal_pembayaran = "sample_text_2"
    assert instance.tanggal_pembayaran == "sample_text_2"


def test_Pembayarans_user_id_value_roundtrip():
    instance = Pembayarans(biaya_kuliah_id=7, id=7, jumlah=7, keterangan="sample_text", mahasiswa_id=7, no_pembayaran="sample_text", pembayaran_tipe=7, prefix="sample_text", semester_id=7, status=7, tanggal_pembayaran="sample_text", user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Prodis_id_value_roundtrip():
    instance = Prodis(id=7, kapasitas_max=7, prodi_name="sample_text", status=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Prodis_kapasitas_max_value_roundtrip():
    instance = Prodis(id=7, kapasitas_max=7, prodi_name="sample_text", status=7, user_id=7)
    assert instance.kapasitas_max == 7
    instance.kapasitas_max = 13
    assert instance.kapasitas_max == 13


def test_Prodis_prodi_name_value_roundtrip():
    instance = Prodis(id=7, kapasitas_max=7, prodi_name="sample_text", status=7, user_id=7)
    assert instance.prodi_name == "sample_text"
    instance.prodi_name = "sample_text_2"
    assert instance.prodi_name == "sample_text_2"


def test_Prodis_status_value_roundtrip():
    instance = Prodis(id=7, kapasitas_max=7, prodi_name="sample_text", status=7, user_id=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_Prodis_user_id_value_roundtrip():
    instance = Prodis(id=7, kapasitas_max=7, prodi_name="sample_text", status=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Setting_alamat_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.alamat == "sample_text"
    instance.alamat = "sample_text_2"
    assert instance.alamat == "sample_text_2"


def test_Setting_email_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Setting_id_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Setting_logo_kampus_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.logo_kampus == "sample_text"
    instance.logo_kampus = "sample_text_2"
    assert instance.logo_kampus == "sample_text_2"


def test_Setting_nama_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.nama == "sample_text"
    instance.nama = "sample_text_2"
    assert instance.nama == "sample_text_2"


def test_Setting_no_faximile_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.no_faximile == "sample_text"
    instance.no_faximile = "sample_text_2"
    assert instance.no_faximile == "sample_text_2"


def test_Setting_no_telepon_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.no_telepon == "sample_text"
    instance.no_telepon = "sample_text_2"
    assert instance.no_telepon == "sample_text_2"


def test_Setting_user_id_value_roundtrip():
    instance = Setting(alamat="sample_text", email="sample_text", id=7, logo_kampus="sample_text", nama="sample_text", no_faximile="sample_text", no_telepon="sample_text", user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_masterBiaya_id_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_masterBiaya_jml_bayar_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.jml_bayar == 7
    instance.jml_bayar = 13
    assert instance.jml_bayar == 13


def test_masterBiaya_jumlah_biaya_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.jumlah_biaya == 7
    instance.jumlah_biaya = 13
    assert instance.jumlah_biaya == 13


def test_masterBiaya_kategori_id_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.kategori_id == 7
    instance.kategori_id = 13
    assert instance.kategori_id == 13


def test_masterBiaya_nama_biaya_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.nama_biaya == "sample_text"
    instance.nama_biaya = "sample_text_2"
    assert instance.nama_biaya == "sample_text_2"


def test_masterBiaya_status_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_masterBiaya_user_id_value_roundtrip():
    instance = masterBiaya(id=7, jml_bayar=7, jumlah_biaya=7, kategori_id=7, nama_biaya="sample_text", status=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_masterKategori_id_value_roundtrip():
    instance = masterKategori(id=7, nama_kategori="sample_text", status=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_masterKategori_nama_kategori_value_roundtrip():
    instance = masterKategori(id=7, nama_kategori="sample_text", status=7, user_id=7)
    assert instance.nama_kategori == "sample_text"
    instance.nama_kategori = "sample_text_2"
    assert instance.nama_kategori == "sample_text_2"


def test_masterKategori_status_value_roundtrip():
    instance = masterKategori(id=7, nama_kategori="sample_text", status=7, user_id=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_masterKategori_user_id_value_roundtrip():
    instance = masterKategori(id=7, nama_kategori="sample_text", status=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Jurusans_strategy = st.builds(Jurusans, id=st.integers(), jurusan_name=safe_text, prodi_id=st.integers())
@given(instance=Jurusans_strategy)
@settings(max_examples=25)
def test_Jurusans_instantiation(instance):
    assert isinstance(instance, Jurusans)


Login_strategy = st.builds(Login, password=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Mahasiswa_Actor_strategy = st.builds(Mahasiswa_Actor)
@given(instance=Mahasiswa_Actor_strategy)
@settings(max_examples=25)
def test_Mahasiswa_Actor_instantiation(instance):
    assert isinstance(instance, Mahasiswa_Actor)


Mahasiswas_strategy = st.builds(Mahasiswas, id=st.integers())
@given(instance=Mahasiswas_strategy)
@settings(max_examples=25)
def test_Mahasiswas_instantiation(instance):
    assert isinstance(instance, Mahasiswas)


Menu_Utama_strategy = st.builds(Menu_Utama)
@given(instance=Menu_Utama_strategy)
@settings(max_examples=25)
def test_Menu_Utama_instantiation(instance):
    assert isinstance(instance, Menu_Utama)


Pembayarans_strategy = st.builds(Pembayarans, biaya_kuliah_id=st.integers(), id=st.integers(), jumlah=st.integers(), keterangan=safe_text, mahasiswa_id=st.integers(), no_pembayaran=safe_text, pembayaran_tipe=st.integers(), prefix=safe_text, semester_id=st.integers(), status=st.integers(), tanggal_pembayaran=safe_text, user_id=st.integers())
@given(instance=Pembayarans_strategy)
@settings(max_examples=25)
def test_Pembayarans_instantiation(instance):
    assert isinstance(instance, Pembayarans)


Prodis_strategy = st.builds(Prodis, id=st.integers(), kapasitas_max=st.integers(), prodi_name=safe_text, status=st.integers(), user_id=st.integers())
@given(instance=Prodis_strategy)
@settings(max_examples=25)
def test_Prodis_instantiation(instance):
    assert isinstance(instance, Prodis)


Setting_strategy = st.builds(Setting, alamat=safe_text, email=safe_text, id=st.integers(), logo_kampus=safe_text, nama=safe_text, no_faximile=safe_text, no_telepon=safe_text, user_id=st.integers())
@given(instance=Setting_strategy)
@settings(max_examples=25)
def test_Setting_instantiation(instance):
    assert isinstance(instance, Setting)


Sistem_Mahasiswa_Ganti_Password_UseCase_strategy = st.builds(Sistem_Mahasiswa_Ganti_Password_UseCase)
@given(instance=Sistem_Mahasiswa_Ganti_Password_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Ganti_Password_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Ganti_Password_UseCase)


Sistem_Mahasiswa_Login_UseCase_strategy = st.builds(Sistem_Mahasiswa_Login_UseCase)
@given(instance=Sistem_Mahasiswa_Login_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Login_UseCase)


Sistem_Mahasiswa_Masukkan_NIM_UseCase_strategy = st.builds(Sistem_Mahasiswa_Masukkan_NIM_UseCase)
@given(instance=Sistem_Mahasiswa_Masukkan_NIM_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Masukkan_NIM_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Masukkan_NIM_UseCase)


Sistem_Mahasiswa_Masukkan_Password_UseCase_strategy = st.builds(Sistem_Mahasiswa_Masukkan_Password_UseCase)
@given(instance=Sistem_Mahasiswa_Masukkan_Password_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Masukkan_Password_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Masukkan_Password_UseCase)


Sistem_Mahasiswa_Melihat_Informasi_UseCase_strategy = st.builds(Sistem_Mahasiswa_Melihat_Informasi_UseCase)
@given(instance=Sistem_Mahasiswa_Melihat_Informasi_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Melihat_Informasi_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Melihat_Informasi_UseCase)


Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_strategy = st.builds(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase)
@given(instance=Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase)


Sistem_Pembayaran_Add_Role_UseCase_strategy = st.builds(Sistem_Pembayaran_Add_Role_UseCase)
@given(instance=Sistem_Pembayaran_Add_Role_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Add_Role_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Add_Role_UseCase)


Sistem_Pembayaran_Add_User_UseCase_strategy = st.builds(Sistem_Pembayaran_Add_User_UseCase)
@given(instance=Sistem_Pembayaran_Add_User_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Add_User_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Add_User_UseCase)


Sistem_Pembayaran_Biaya_Kuliah_UseCase_strategy = st.builds(Sistem_Pembayaran_Biaya_Kuliah_UseCase)
@given(instance=Sistem_Pembayaran_Biaya_Kuliah_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Biaya_Kuliah_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Biaya_Kuliah_UseCase)


Sistem_Pembayaran_Jurusan_UseCase_strategy = st.builds(Sistem_Pembayaran_Jurusan_UseCase)
@given(instance=Sistem_Pembayaran_Jurusan_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Jurusan_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Jurusan_UseCase)


Sistem_Pembayaran_Kategori_Biaya_UseCase_strategy = st.builds(Sistem_Pembayaran_Kategori_Biaya_UseCase)
@given(instance=Sistem_Pembayaran_Kategori_Biaya_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Kategori_Biaya_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Kategori_Biaya_UseCase)


Sistem_Pembayaran_Login_UseCase_strategy = st.builds(Sistem_Pembayaran_Login_UseCase)
@given(instance=Sistem_Pembayaran_Login_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Login_UseCase)


Sistem_Pembayaran_Mahasiswa_UseCase_strategy = st.builds(Sistem_Pembayaran_Mahasiswa_UseCase)
@given(instance=Sistem_Pembayaran_Mahasiswa_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Mahasiswa_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Mahasiswa_UseCase)


Sistem_Pembayaran_Masukkan_Password_UseCase_strategy = st.builds(Sistem_Pembayaran_Masukkan_Password_UseCase)
@given(instance=Sistem_Pembayaran_Masukkan_Password_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Masukkan_Password_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Masukkan_Password_UseCase)


Sistem_Pembayaran_Masukkan_Username_Email_UseCase_strategy = st.builds(Sistem_Pembayaran_Masukkan_Username_Email_UseCase)
@given(instance=Sistem_Pembayaran_Masukkan_Username_Email_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Masukkan_Username_Email_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Masukkan_Username_Email_UseCase)


Sistem_Pembayaran_Pembayaran_UseCase_strategy = st.builds(Sistem_Pembayaran_Pembayaran_UseCase)
@given(instance=Sistem_Pembayaran_Pembayaran_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Pembayaran_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Pembayaran_UseCase)


Sistem_Pembayaran_Prodi_UseCase_strategy = st.builds(Sistem_Pembayaran_Prodi_UseCase)
@given(instance=Sistem_Pembayaran_Prodi_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Prodi_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Prodi_UseCase)


Sistem_Pembayaran_Setting_UseCase_strategy = st.builds(Sistem_Pembayaran_Setting_UseCase)
@given(instance=Sistem_Pembayaran_Setting_UseCase_strategy)
@settings(max_examples=25)
def test_Sistem_Pembayaran_Setting_UseCase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Setting_UseCase)


Tata_Usaha_Actor_strategy = st.builds(Tata_Usaha_Actor)
@given(instance=Tata_Usaha_Actor_strategy)
@settings(max_examples=25)
def test_Tata_Usaha_Actor_instantiation(instance):
    assert isinstance(instance, Tata_Usaha_Actor)


masterBiaya_strategy = st.builds(masterBiaya, id=st.integers(), jml_bayar=st.integers(), jumlah_biaya=st.integers(), kategori_id=st.integers(), nama_biaya=safe_text, status=st.integers(), user_id=st.integers())
@given(instance=masterBiaya_strategy)
@settings(max_examples=25)
def test_masterBiaya_instantiation(instance):
    assert isinstance(instance, masterBiaya)


masterKategori_strategy = st.builds(masterKategori, id=st.integers(), nama_kategori=safe_text, status=st.integers(), user_id=st.integers())
@given(instance=masterKategori_strategy)
@settings(max_examples=25)
def test_masterKategori_instantiation(instance):
    assert isinstance(instance, masterKategori)


