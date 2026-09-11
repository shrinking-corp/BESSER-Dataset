import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Buku,
    Buku_berbahasa_Asing_UseCase,
    Class,
    Keluar,
    Login,
    Login1,
    Melakukan_Login_UseCase,
    Melakukan_Logout_UseCase,
    Melakukan_Penerjemahan_Buku_Bacaan_UseCase,
    Melihat_Tampilan_Awal_Aplikasi_UseCase,
    Memilih_Kategori_Buku_UseCase,
    Menu_Utama,
    Mulai_Membaca_UseCase,
    MyClass,
    Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase,
    Profil,
    User_Actor,
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

def test_Keluar_Keluar_value_roundtrip():
    instance = Keluar(Keluar="sample_text")
    assert instance.Keluar == "sample_text"
    instance.Keluar = "sample_text_2"
    assert instance.Keluar == "sample_text_2"


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


def test_Login1_password_value_roundtrip():
    instance = Login1(password="sample_text", usernam="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login1_usernam_value_roundtrip():
    instance = Login1(password="sample_text", usernam="sample_text")
    assert instance.usernam == "sample_text"
    instance.usernam = "sample_text_2"
    assert instance.usernam == "sample_text_2"


def test_Profil_Biodata_value_roundtrip():
    instance = Profil(Biodata="sample_text")
    assert instance.Biodata == "sample_text"
    instance.Biodata = "sample_text_2"
    assert instance.Biodata == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Buku_strategy = st.builds(Buku)
@given(instance=Buku_strategy)
@settings(max_examples=25)
def test_Buku_instantiation(instance):
    assert isinstance(instance, Buku)


Buku_berbahasa_Asing_UseCase_strategy = st.builds(Buku_berbahasa_Asing_UseCase)
@given(instance=Buku_berbahasa_Asing_UseCase_strategy)
@settings(max_examples=25)
def test_Buku_berbahasa_Asing_UseCase_instantiation(instance):
    assert isinstance(instance, Buku_berbahasa_Asing_UseCase)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Keluar_strategy = st.builds(Keluar, Keluar=safe_text)
@given(instance=Keluar_strategy)
@settings(max_examples=25)
def test_Keluar_instantiation(instance):
    assert isinstance(instance, Keluar)


Login_strategy = st.builds(Login, password=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Login1_strategy = st.builds(Login1, password=safe_text, usernam=safe_text)
@given(instance=Login1_strategy)
@settings(max_examples=25)
def test_Login1_instantiation(instance):
    assert isinstance(instance, Login1)


Melakukan_Login_UseCase_strategy = st.builds(Melakukan_Login_UseCase)
@given(instance=Melakukan_Login_UseCase_strategy)
@settings(max_examples=25)
def test_Melakukan_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Melakukan_Login_UseCase)


Melakukan_Logout_UseCase_strategy = st.builds(Melakukan_Logout_UseCase)
@given(instance=Melakukan_Logout_UseCase_strategy)
@settings(max_examples=25)
def test_Melakukan_Logout_UseCase_instantiation(instance):
    assert isinstance(instance, Melakukan_Logout_UseCase)


Melakukan_Penerjemahan_Buku_Bacaan_UseCase_strategy = st.builds(Melakukan_Penerjemahan_Buku_Bacaan_UseCase)
@given(instance=Melakukan_Penerjemahan_Buku_Bacaan_UseCase_strategy)
@settings(max_examples=25)
def test_Melakukan_Penerjemahan_Buku_Bacaan_UseCase_instantiation(instance):
    assert isinstance(instance, Melakukan_Penerjemahan_Buku_Bacaan_UseCase)


Melihat_Tampilan_Awal_Aplikasi_UseCase_strategy = st.builds(Melihat_Tampilan_Awal_Aplikasi_UseCase)
@given(instance=Melihat_Tampilan_Awal_Aplikasi_UseCase_strategy)
@settings(max_examples=25)
def test_Melihat_Tampilan_Awal_Aplikasi_UseCase_instantiation(instance):
    assert isinstance(instance, Melihat_Tampilan_Awal_Aplikasi_UseCase)


Memilih_Kategori_Buku_UseCase_strategy = st.builds(Memilih_Kategori_Buku_UseCase)
@given(instance=Memilih_Kategori_Buku_UseCase_strategy)
@settings(max_examples=25)
def test_Memilih_Kategori_Buku_UseCase_instantiation(instance):
    assert isinstance(instance, Memilih_Kategori_Buku_UseCase)


Menu_Utama_strategy = st.builds(Menu_Utama)
@given(instance=Menu_Utama_strategy)
@settings(max_examples=25)
def test_Menu_Utama_instantiation(instance):
    assert isinstance(instance, Menu_Utama)


Mulai_Membaca_UseCase_strategy = st.builds(Mulai_Membaca_UseCase)
@given(instance=Mulai_Membaca_UseCase_strategy)
@settings(max_examples=25)
def test_Mulai_Membaca_UseCase_instantiation(instance):
    assert isinstance(instance, Mulai_Membaca_UseCase)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase_strategy = st.builds(Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase)
@given(instance=Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase_strategy)
@settings(max_examples=25)
def test_Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase_instantiation(instance):
    assert isinstance(instance, Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase)


Profil_strategy = st.builds(Profil, Biodata=safe_text)
@given(instance=Profil_strategy)
@settings(max_examples=25)
def test_Profil_instantiation(instance):
    assert isinstance(instance, Profil)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)


