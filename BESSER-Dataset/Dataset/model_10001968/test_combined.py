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
    Setting,
    masterBiaya,
    Menu_Utama,
    masterKategori,
    Login,
    Prodis,
    Jurusans,
    Mahasiswas,
    Tata_Usaha_Actor,
    Administrator_Actor,
    Sistem_Pembayaran_Add_User_UseCase,
    Sistem_Pembayaran_Add_Role_UseCase,
    Sistem_Pembayaran_Setting_UseCase,
    Sistem_Pembayaran_Pembayaran_UseCase,
    Sistem_Pembayaran_Mahasiswa_UseCase,
    Sistem_Pembayaran_Jurusan_UseCase,
    Sistem_Pembayaran_Prodi_UseCase,
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
    Sistem_Pembayaran_Masukkan_Password_UseCase,
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
    Sistem_Pembayaran_Login_UseCase,
    Mahasiswa_Actor,
    Sistem_Mahasiswa_Ganti_Password_UseCase,
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
    Sistem_Mahasiswa_Login_UseCase,
    Pembayarans,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_setting_is_not_abstract():
    assert not inspect.isabstract(Setting)


def test_hyp_setting_constructor_exists():
    assert callable(Setting.__init__)


def test_hyp_setting_constructor_args():
    sig = inspect.signature(Setting.__init__)
    params = list(sig.parameters.keys())
    assert "logo_kampus" in params, "Missing parameter 'logo_kampus'"
    assert "nama" in params, "Missing parameter 'nama'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "email" in params, "Missing parameter 'email'"
    assert "no_telepon" in params, "Missing parameter 'no_telepon'"
    assert "no_faximile" in params, "Missing parameter 'no_faximile'"











def test_hyp_masterbiaya_is_not_abstract():
    assert not inspect.isabstract(masterBiaya)


def test_hyp_masterbiaya_constructor_exists():
    assert callable(masterBiaya.__init__)


def test_hyp_masterbiaya_constructor_args():
    sig = inspect.signature(masterBiaya.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nama_biaya" in params, "Missing parameter 'nama_biaya'"
    assert "id" in params, "Missing parameter 'id'"
    assert "jumlah_biaya" in params, "Missing parameter 'jumlah_biaya'"
    assert "kategori_id" in params, "Missing parameter 'kategori_id'"
    assert "jml_bayar" in params, "Missing parameter 'jml_bayar'"
    assert "user_id" in params, "Missing parameter 'user_id'"










def test_hyp_menu_utama_is_not_abstract():
    assert not inspect.isabstract(Menu_Utama)


def test_hyp_menu_utama_constructor_exists():
    assert callable(Menu_Utama.__init__)


def test_hyp_menu_utama_constructor_args():
    sig = inspect.signature(Menu_Utama.__init__)
    params = list(sig.parameters.keys())



def test_hyp_masterkategori_is_not_abstract():
    assert not inspect.isabstract(masterKategori)


def test_hyp_masterkategori_constructor_exists():
    assert callable(masterKategori.__init__)


def test_hyp_masterkategori_constructor_args():
    sig = inspect.signature(masterKategori.__init__)
    params = list(sig.parameters.keys())
    assert "nama_kategori" in params, "Missing parameter 'nama_kategori'"
    assert "status" in params, "Missing parameter 'status'"
    assert "id" in params, "Missing parameter 'id'"
    assert "user_id" in params, "Missing parameter 'user_id'"







def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"





def test_hyp_prodis_is_not_abstract():
    assert not inspect.isabstract(Prodis)


def test_hyp_prodis_constructor_exists():
    assert callable(Prodis.__init__)


def test_hyp_prodis_constructor_args():
    sig = inspect.signature(Prodis.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "prodi_name" in params, "Missing parameter 'prodi_name'"
    assert "kapasitas_max" in params, "Missing parameter 'kapasitas_max'"
    assert "status" in params, "Missing parameter 'status'"
    assert "user_id" in params, "Missing parameter 'user_id'"








def test_hyp_jurusans_is_not_abstract():
    assert not inspect.isabstract(Jurusans)


def test_hyp_jurusans_constructor_exists():
    assert callable(Jurusans.__init__)


def test_hyp_jurusans_constructor_args():
    sig = inspect.signature(Jurusans.__init__)
    params = list(sig.parameters.keys())
    assert "jurusan_name" in params, "Missing parameter 'jurusan_name'"
    assert "prodi_id" in params, "Missing parameter 'prodi_id'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_mahasiswas_is_not_abstract():
    assert not inspect.isabstract(Mahasiswas)


def test_hyp_mahasiswas_constructor_exists():
    assert callable(Mahasiswas.__init__)


def test_hyp_mahasiswas_constructor_args():
    sig = inspect.signature(Mahasiswas.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_tata_usaha_actor_is_not_abstract():
    assert not inspect.isabstract(Tata_Usaha_Actor)


def test_hyp_tata_usaha_actor_constructor_exists():
    assert callable(Tata_Usaha_Actor.__init__)


def test_hyp_tata_usaha_actor_constructor_args():
    sig = inspect.signature(Tata_Usaha_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_hyp_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_hyp_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_add_user_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Add_User_UseCase)


def test_hyp_sistem_pembayaran_add_user_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Add_User_UseCase.__init__)


def test_hyp_sistem_pembayaran_add_user_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Add_User_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_add_role_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Add_Role_UseCase)


def test_hyp_sistem_pembayaran_add_role_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Add_Role_UseCase.__init__)


def test_hyp_sistem_pembayaran_add_role_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Add_Role_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_setting_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Setting_UseCase)


def test_hyp_sistem_pembayaran_setting_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Setting_UseCase.__init__)


def test_hyp_sistem_pembayaran_setting_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Setting_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_pembayaran_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Pembayaran_UseCase)


def test_hyp_sistem_pembayaran_pembayaran_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Pembayaran_UseCase.__init__)


def test_hyp_sistem_pembayaran_pembayaran_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Pembayaran_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_mahasiswa_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Mahasiswa_UseCase)


def test_hyp_sistem_pembayaran_mahasiswa_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Mahasiswa_UseCase.__init__)


def test_hyp_sistem_pembayaran_mahasiswa_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Mahasiswa_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_jurusan_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Jurusan_UseCase)


def test_hyp_sistem_pembayaran_jurusan_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Jurusan_UseCase.__init__)


def test_hyp_sistem_pembayaran_jurusan_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Jurusan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_prodi_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Prodi_UseCase)


def test_hyp_sistem_pembayaran_prodi_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Prodi_UseCase.__init__)


def test_hyp_sistem_pembayaran_prodi_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Prodi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_biaya_kuliah_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Biaya_Kuliah_UseCase)


def test_hyp_sistem_pembayaran_biaya_kuliah_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Biaya_Kuliah_UseCase.__init__)


def test_hyp_sistem_pembayaran_biaya_kuliah_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Biaya_Kuliah_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_kategori_biaya_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Kategori_Biaya_UseCase)


def test_hyp_sistem_pembayaran_kategori_biaya_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Kategori_Biaya_UseCase.__init__)


def test_hyp_sistem_pembayaran_kategori_biaya_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Kategori_Biaya_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_masukkan_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Masukkan_Password_UseCase)


def test_hyp_sistem_pembayaran_masukkan_password_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Masukkan_Password_UseCase.__init__)


def test_hyp_sistem_pembayaran_masukkan_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Masukkan_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_masukkan_username_email_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Masukkan_Username_Email_UseCase)


def test_hyp_sistem_pembayaran_masukkan_username_email_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Masukkan_Username_Email_UseCase.__init__)


def test_hyp_sistem_pembayaran_masukkan_username_email_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Masukkan_Username_Email_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_pembayaran_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Login_UseCase)


def test_hyp_sistem_pembayaran_login_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Login_UseCase.__init__)


def test_hyp_sistem_pembayaran_login_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mahasiswa_actor_is_not_abstract():
    assert not inspect.isabstract(Mahasiswa_Actor)


def test_hyp_mahasiswa_actor_constructor_exists():
    assert callable(Mahasiswa_Actor.__init__)


def test_hyp_mahasiswa_actor_constructor_args():
    sig = inspect.signature(Mahasiswa_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_ganti_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Ganti_Password_UseCase)


def test_hyp_sistem_mahasiswa_ganti_password_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Ganti_Password_UseCase.__init__)


def test_hyp_sistem_mahasiswa_ganti_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Ganti_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_update_data_mahasiswa_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase)


def test_hyp_sistem_mahasiswa_update_data_mahasiswa_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase.__init__)


def test_hyp_sistem_mahasiswa_update_data_mahasiswa_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_melihat_informasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Melihat_Informasi_UseCase)


def test_hyp_sistem_mahasiswa_melihat_informasi_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Melihat_Informasi_UseCase.__init__)


def test_hyp_sistem_mahasiswa_melihat_informasi_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Melihat_Informasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_masukkan_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Masukkan_Password_UseCase)


def test_hyp_sistem_mahasiswa_masukkan_password_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Masukkan_Password_UseCase.__init__)


def test_hyp_sistem_mahasiswa_masukkan_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Masukkan_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_masukkan_nim_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Masukkan_NIM_UseCase)


def test_hyp_sistem_mahasiswa_masukkan_nim_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Masukkan_NIM_UseCase.__init__)


def test_hyp_sistem_mahasiswa_masukkan_nim_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Masukkan_NIM_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistem_mahasiswa_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Login_UseCase)


def test_hyp_sistem_mahasiswa_login_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Login_UseCase.__init__)


def test_hyp_sistem_mahasiswa_login_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pembayarans_is_not_abstract():
    assert not inspect.isabstract(Pembayarans)


def test_hyp_pembayarans_constructor_exists():
    assert callable(Pembayarans.__init__)


def test_hyp_pembayarans_constructor_args():
    sig = inspect.signature(Pembayarans.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "mahasiswa_id" in params, "Missing parameter 'mahasiswa_id'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "status" in params, "Missing parameter 'status'"
    assert "pembayaran_tipe" in params, "Missing parameter 'pembayaran_tipe'"
    assert "no_pembayaran" in params, "Missing parameter 'no_pembayaran'"
    assert "id" in params, "Missing parameter 'id'"
    assert "tanggal_pembayaran" in params, "Missing parameter 'tanggal_pembayaran'"
    assert "semester_id" in params, "Missing parameter 'semester_id'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "biaya_kuliah_id" in params, "Missing parameter 'biaya_kuliah_id'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"














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
Setting_strategy = st.builds(
    Setting,
    logo_kampus=
        safe_text,
    nama=
        safe_text,
    user_id=
        st.integers(),
    id=
        st.integers(),
    alamat=
        safe_text,
    email=
        safe_text,
    no_telepon=
        safe_text,
    no_faximile=
        safe_text
)
masterBiaya_strategy = st.builds(
    masterBiaya,
    status=
        st.integers(),
    nama_biaya=
        safe_text,
    id=
        st.integers(),
    jumlah_biaya=
        st.integers(),
    kategori_id=
        st.integers(),
    jml_bayar=
        st.integers(),
    user_id=
        st.integers()
)
Menu_Utama_strategy = st.builds(
    Menu_Utama,
)
masterKategori_strategy = st.builds(
    masterKategori,
    nama_kategori=
        safe_text,
    status=
        st.integers(),
    id=
        st.integers(),
    user_id=
        st.integers()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Prodis_strategy = st.builds(
    Prodis,
    id=
        st.integers(),
    prodi_name=
        safe_text,
    kapasitas_max=
        st.integers(),
    status=
        st.integers(),
    user_id=
        st.integers()
)
Jurusans_strategy = st.builds(
    Jurusans,
    jurusan_name=
        safe_text,
    prodi_id=
        st.integers(),
    id=
        st.integers()
)
Mahasiswas_strategy = st.builds(
    Mahasiswas,
    id=
        st.integers()
)
Tata_Usaha_Actor_strategy = st.builds(
    Tata_Usaha_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Sistem_Pembayaran_Add_User_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Add_User_UseCase,
)
Sistem_Pembayaran_Add_Role_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Add_Role_UseCase,
)
Sistem_Pembayaran_Setting_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Setting_UseCase,
)
Sistem_Pembayaran_Pembayaran_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Pembayaran_UseCase,
)
Sistem_Pembayaran_Mahasiswa_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Mahasiswa_UseCase,
)
Sistem_Pembayaran_Jurusan_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Jurusan_UseCase,
)
Sistem_Pembayaran_Prodi_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Prodi_UseCase,
)
Sistem_Pembayaran_Biaya_Kuliah_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
)
Sistem_Pembayaran_Kategori_Biaya_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
)
Sistem_Pembayaran_Masukkan_Password_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Masukkan_Password_UseCase,
)
Sistem_Pembayaran_Masukkan_Username_Email_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
)
Sistem_Pembayaran_Login_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Login_UseCase,
)
Mahasiswa_Actor_strategy = st.builds(
    Mahasiswa_Actor,
)
Sistem_Mahasiswa_Ganti_Password_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Ganti_Password_UseCase,
)
Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
)
Sistem_Mahasiswa_Melihat_Informasi_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
)
Sistem_Mahasiswa_Masukkan_Password_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
)
Sistem_Mahasiswa_Masukkan_NIM_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
)
Sistem_Mahasiswa_Login_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Login_UseCase,
)
Pembayarans_strategy = st.builds(
    Pembayarans,
    user_id=
        st.integers(),
    mahasiswa_id=
        st.integers(),
    keterangan=
        safe_text,
    status=
        st.integers(),
    pembayaran_tipe=
        st.integers(),
    no_pembayaran=
        safe_text,
    id=
        st.integers(),
    tanggal_pembayaran=
        safe_text,
    semester_id=
        st.integers(),
    prefix=
        safe_text,
    biaya_kuliah_id=
        st.integers(),
    jumlah=
        st.integers()
)




@given(instance=Setting_strategy)
def test_hyp_setting_logo_kampus_setter(instance):
    original = instance.logo_kampus
    instance.logo_kampus = original
    assert instance.logo_kampus == original



@given(instance=Setting_strategy)
def test_hyp_setting_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=Setting_strategy)
def test_hyp_setting_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Setting_strategy)
def test_hyp_setting_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Setting_strategy)
def test_hyp_setting_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original



@given(instance=Setting_strategy)
def test_hyp_setting_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Setting_strategy)
def test_hyp_setting_no_telepon_setter(instance):
    original = instance.no_telepon
    instance.no_telepon = original
    assert instance.no_telepon == original



@given(instance=Setting_strategy)
def test_hyp_setting_no_faximile_setter(instance):
    original = instance.no_faximile
    instance.no_faximile = original
    assert instance.no_faximile == original




@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_nama_biaya_setter(instance):
    original = instance.nama_biaya
    instance.nama_biaya = original
    assert instance.nama_biaya == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_jumlah_biaya_setter(instance):
    original = instance.jumlah_biaya
    instance.jumlah_biaya = original
    assert instance.jumlah_biaya == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_kategori_id_setter(instance):
    original = instance.kategori_id
    instance.kategori_id = original
    assert instance.kategori_id == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_jml_bayar_setter(instance):
    original = instance.jml_bayar
    instance.jml_bayar = original
    assert instance.jml_bayar == original



@given(instance=masterBiaya_strategy)
def test_hyp_masterbiaya_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original





@given(instance=masterKategori_strategy)
def test_hyp_masterkategori_nama_kategori_setter(instance):
    original = instance.nama_kategori
    instance.nama_kategori = original
    assert instance.nama_kategori == original



@given(instance=masterKategori_strategy)
def test_hyp_masterkategori_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=masterKategori_strategy)
def test_hyp_masterkategori_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=masterKategori_strategy)
def test_hyp_masterkategori_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original




@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original




@given(instance=Prodis_strategy)
def test_hyp_prodis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Prodis_strategy)
def test_hyp_prodis_prodi_name_setter(instance):
    original = instance.prodi_name
    instance.prodi_name = original
    assert instance.prodi_name == original



@given(instance=Prodis_strategy)
def test_hyp_prodis_kapasitas_max_setter(instance):
    original = instance.kapasitas_max
    instance.kapasitas_max = original
    assert instance.kapasitas_max == original



@given(instance=Prodis_strategy)
def test_hyp_prodis_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Prodis_strategy)
def test_hyp_prodis_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original




@given(instance=Jurusans_strategy)
def test_hyp_jurusans_jurusan_name_setter(instance):
    original = instance.jurusan_name
    instance.jurusan_name = original
    assert instance.jurusan_name == original



@given(instance=Jurusans_strategy)
def test_hyp_jurusans_prodi_id_setter(instance):
    original = instance.prodi_id
    instance.prodi_id = original
    assert instance.prodi_id == original



@given(instance=Jurusans_strategy)
def test_hyp_jurusans_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Mahasiswas_strategy)
def test_hyp_mahasiswas_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

























@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_mahasiswa_id_setter(instance):
    original = instance.mahasiswa_id
    instance.mahasiswa_id = original
    assert instance.mahasiswa_id == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_pembayaran_tipe_setter(instance):
    original = instance.pembayaran_tipe
    instance.pembayaran_tipe = original
    assert instance.pembayaran_tipe == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_no_pembayaran_setter(instance):
    original = instance.no_pembayaran
    instance.no_pembayaran = original
    assert instance.no_pembayaran == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_tanggal_pembayaran_setter(instance):
    original = instance.tanggal_pembayaran
    instance.tanggal_pembayaran = original
    assert instance.tanggal_pembayaran == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_semester_id_setter(instance):
    original = instance.semester_id
    instance.semester_id = original
    assert instance.semester_id == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_biaya_kuliah_id_setter(instance):
    original = instance.biaya_kuliah_id
    instance.biaya_kuliah_id = original
    assert instance.biaya_kuliah_id == original



@given(instance=Pembayarans_strategy)
def test_hyp_pembayarans_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



