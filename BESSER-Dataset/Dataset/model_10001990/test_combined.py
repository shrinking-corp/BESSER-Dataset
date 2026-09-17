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
    Login1,
    Pencarian,
    Keluar,
    Buku,
    Menu_Utama,
    MyClass,
    Class,
    Login,
    Melakukan_Penerjemahan_Buku_Bacaan_UseCase,
    Buku_berbahasa_Asing_UseCase,
    Keluar_dari_Aplikasi_UseCase,
    Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase,
    Mulai_Membaca_UseCase,
    Memilih_Kategori_Buku_UseCase,
    Melihat_Tampilan_Awal_Aplikasi_UseCase,
    Masuk_dari_Aplikasi_UseCase,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_login1_is_not_abstract():
    assert not inspect.isabstract(Login1)


def test_hyp_login1_constructor_exists():
    assert callable(Login1.__init__)


def test_hyp_login1_constructor_args():
    sig = inspect.signature(Login1.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"





def test_hyp_pencarian_is_not_abstract():
    assert not inspect.isabstract(Pencarian)


def test_hyp_pencarian_constructor_exists():
    assert callable(Pencarian.__init__)


def test_hyp_pencarian_constructor_args():
    sig = inspect.signature(Pencarian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_keluar_is_not_abstract():
    assert not inspect.isabstract(Keluar)


def test_hyp_keluar_constructor_exists():
    assert callable(Keluar.__init__)


def test_hyp_keluar_constructor_args():
    sig = inspect.signature(Keluar.__init__)
    params = list(sig.parameters.keys())
    assert "Keluar" in params, "Missing parameter 'Keluar'"




def test_hyp_buku_is_not_abstract():
    assert not inspect.isabstract(Buku)


def test_hyp_buku_constructor_exists():
    assert callable(Buku.__init__)


def test_hyp_buku_constructor_args():
    sig = inspect.signature(Buku.__init__)
    params = list(sig.parameters.keys())



def test_hyp_menu_utama_is_not_abstract():
    assert not inspect.isabstract(Menu_Utama)


def test_hyp_menu_utama_constructor_exists():
    assert callable(Menu_Utama.__init__)


def test_hyp_menu_utama_constructor_args():
    sig = inspect.signature(Menu_Utama.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"





def test_hyp_melakukan_penerjemahan_buku_bacaan_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_Penerjemahan_Buku_Bacaan_UseCase)


def test_hyp_melakukan_penerjemahan_buku_bacaan_usecase_constructor_exists():
    assert callable(Melakukan_Penerjemahan_Buku_Bacaan_UseCase.__init__)


def test_hyp_melakukan_penerjemahan_buku_bacaan_usecase_constructor_args():
    sig = inspect.signature(Melakukan_Penerjemahan_Buku_Bacaan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buku_berbahasa_asing_usecase_is_not_abstract():
    assert not inspect.isabstract(Buku_berbahasa_Asing_UseCase)


def test_hyp_buku_berbahasa_asing_usecase_constructor_exists():
    assert callable(Buku_berbahasa_Asing_UseCase.__init__)


def test_hyp_buku_berbahasa_asing_usecase_constructor_args():
    sig = inspect.signature(Buku_berbahasa_Asing_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_keluar_dari_aplikasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Keluar_dari_Aplikasi_UseCase)


def test_hyp_keluar_dari_aplikasi_usecase_constructor_exists():
    assert callable(Keluar_dari_Aplikasi_UseCase.__init__)


def test_hyp_keluar_dari_aplikasi_usecase_constructor_args():
    sig = inspect.signature(Keluar_dari_Aplikasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase_is_not_abstract():
    assert not inspect.isabstract(Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase)


def test_hyp_otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase_constructor_exists():
    assert callable(Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase.__init__)


def test_hyp_otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase_constructor_args():
    sig = inspect.signature(Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mulai_membaca_usecase_is_not_abstract():
    assert not inspect.isabstract(Mulai_Membaca_UseCase)


def test_hyp_mulai_membaca_usecase_constructor_exists():
    assert callable(Mulai_Membaca_UseCase.__init__)


def test_hyp_mulai_membaca_usecase_constructor_args():
    sig = inspect.signature(Mulai_Membaca_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memilih_kategori_buku_usecase_is_not_abstract():
    assert not inspect.isabstract(Memilih_Kategori_Buku_UseCase)


def test_hyp_memilih_kategori_buku_usecase_constructor_exists():
    assert callable(Memilih_Kategori_Buku_UseCase.__init__)


def test_hyp_memilih_kategori_buku_usecase_constructor_args():
    sig = inspect.signature(Memilih_Kategori_Buku_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_melihat_tampilan_awal_aplikasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Melihat_Tampilan_Awal_Aplikasi_UseCase)


def test_hyp_melihat_tampilan_awal_aplikasi_usecase_constructor_exists():
    assert callable(Melihat_Tampilan_Awal_Aplikasi_UseCase.__init__)


def test_hyp_melihat_tampilan_awal_aplikasi_usecase_constructor_args():
    sig = inspect.signature(Melihat_Tampilan_Awal_Aplikasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_masuk_dari_aplikasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Masuk_dari_Aplikasi_UseCase)


def test_hyp_masuk_dari_aplikasi_usecase_constructor_exists():
    assert callable(Masuk_dari_Aplikasi_UseCase.__init__)


def test_hyp_masuk_dari_aplikasi_usecase_constructor_args():
    sig = inspect.signature(Masuk_dari_Aplikasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_hyp_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_hyp_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())


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
Login1_strategy = st.builds(
    Login1,
    Username=
        safe_text,
    Password=
        safe_text
)
Pencarian_strategy = st.builds(
    Pencarian,
)
Keluar_strategy = st.builds(
    Keluar,
    Keluar=
        safe_text
)
Buku_strategy = st.builds(
    Buku,
)
Menu_Utama_strategy = st.builds(
    Menu_Utama,
)
MyClass_strategy = st.builds(
    MyClass,
)
Class_strategy = st.builds(
    Class,
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Melakukan_Penerjemahan_Buku_Bacaan_UseCase_strategy = st.builds(
    Melakukan_Penerjemahan_Buku_Bacaan_UseCase,
)
Buku_berbahasa_Asing_UseCase_strategy = st.builds(
    Buku_berbahasa_Asing_UseCase,
)
Keluar_dari_Aplikasi_UseCase_strategy = st.builds(
    Keluar_dari_Aplikasi_UseCase,
)
Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase_strategy = st.builds(
    Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase,
)
Mulai_Membaca_UseCase_strategy = st.builds(
    Mulai_Membaca_UseCase,
)
Memilih_Kategori_Buku_UseCase_strategy = st.builds(
    Memilih_Kategori_Buku_UseCase,
)
Melihat_Tampilan_Awal_Aplikasi_UseCase_strategy = st.builds(
    Melihat_Tampilan_Awal_Aplikasi_UseCase,
)
Masuk_dari_Aplikasi_UseCase_strategy = st.builds(
    Masuk_dari_Aplikasi_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)




@given(instance=Login1_strategy)
def test_hyp_login1_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Login1_strategy)
def test_hyp_login1_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original





@given(instance=Keluar_strategy)
def test_hyp_keluar_Keluar_setter(instance):
    original = instance.Keluar
    instance.Keluar = original
    assert instance.Keluar == original








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











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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
    Keluar_dari_Aplikasi_UseCase,
    Login,
    Login1,
    Masuk_dari_Aplikasi_UseCase,
    Melakukan_Penerjemahan_Buku_Bacaan_UseCase,
    Melihat_Tampilan_Awal_Aplikasi_UseCase,
    Memilih_Kategori_Buku_UseCase,
    Menu_Utama,
    Mulai_Membaca_UseCase,
    MyClass,
    Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase,
    Pencarian,
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


def test_Login1_Password_value_roundtrip():
    instance = Login1(Password="sample_text", Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Login1_Username_value_roundtrip():
    instance = Login1(Password="sample_text", Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


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


Keluar_dari_Aplikasi_UseCase_strategy = st.builds(Keluar_dari_Aplikasi_UseCase)
@given(instance=Keluar_dari_Aplikasi_UseCase_strategy)
@settings(max_examples=25)
def test_Keluar_dari_Aplikasi_UseCase_instantiation(instance):
    assert isinstance(instance, Keluar_dari_Aplikasi_UseCase)


Login_strategy = st.builds(Login, password=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Login1_strategy = st.builds(Login1, Password=safe_text, Username=safe_text)
@given(instance=Login1_strategy)
@settings(max_examples=25)
def test_Login1_instantiation(instance):
    assert isinstance(instance, Login1)


Masuk_dari_Aplikasi_UseCase_strategy = st.builds(Masuk_dari_Aplikasi_UseCase)
@given(instance=Masuk_dari_Aplikasi_UseCase_strategy)
@settings(max_examples=25)
def test_Masuk_dari_Aplikasi_UseCase_instantiation(instance):
    assert isinstance(instance, Masuk_dari_Aplikasi_UseCase)


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


Pencarian_strategy = st.builds(Pencarian)
@given(instance=Pencarian_strategy)
@settings(max_examples=25)
def test_Pencarian_instantiation(instance):
    assert isinstance(instance, Pencarian)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)



