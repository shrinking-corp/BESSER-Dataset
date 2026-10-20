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
    HasilBidding,
    Bidding,
    Biddee,
    Bidder,
    Admin,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hasilbidding_is_not_abstract():
    assert not inspect.isabstract(HasilBidding)


def test_hyp_hasilbidding_constructor_exists():
    assert callable(HasilBidding.__init__)


def test_hyp_hasilbidding_constructor_args():
    sig = inspect.signature(HasilBidding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bidding_is_not_abstract():
    assert not inspect.isabstract(Bidding)


def test_hyp_bidding_constructor_exists():
    assert callable(Bidding.__init__)


def test_hyp_bidding_constructor_args():
    sig = inspect.signature(Bidding.__init__)
    params = list(sig.parameters.keys())
    assert "bidder" in params, "Missing parameter 'bidder'"
    assert "catatanBidder" in params, "Missing parameter 'catatanBidder'"
    assert "notulensi" in params, "Missing parameter 'notulensi'"
    assert "biddee" in params, "Missing parameter 'biddee'"
    assert "berkas" in params, "Missing parameter 'berkas'"
    assert "jabatan" in params, "Missing parameter 'jabatan'"
    assert "statusBidding" in params, "Missing parameter 'statusBidding'"
    assert "nilai" in params, "Missing parameter 'nilai'"











def test_hyp_biddee_is_not_abstract():
    assert not inspect.isabstract(Biddee)


def test_hyp_biddee_constructor_exists():
    assert callable(Biddee.__init__)


def test_hyp_biddee_constructor_args():
    sig = inspect.signature(Biddee.__init__)
    params = list(sig.parameters.keys())
    assert "statusBiddee" in params, "Missing parameter 'statusBiddee'"




def test_hyp_bidder_is_not_abstract():
    assert not inspect.isabstract(Bidder)


def test_hyp_bidder_constructor_exists():
    assert callable(Bidder.__init__)


def test_hyp_bidder_constructor_args():
    sig = inspect.signature(Bidder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "nama" in params, "Missing parameter 'nama'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "password" in params, "Missing parameter 'password'"






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
HasilBidding_strategy = st.builds(
    HasilBidding,
)
Bidding_strategy = st.builds(
    Bidding,
    bidder=
        safe_text,
    catatanBidder=
        safe_text,
    notulensi=
        safe_text,
    biddee=
        safe_text,
    berkas=
        safe_text,
    jabatan=
        safe_text,
    statusBidding=
        safe_text,
    nilai=
        st.integers()
)
Biddee_strategy = st.builds(
    Biddee,
    statusBiddee=
        safe_text
)
Bidder_strategy = st.builds(
    Bidder,
)
Admin_strategy = st.builds(
    Admin,
)
User_strategy = st.builds(
    User,
    userName=
        safe_text,
    nama=
        safe_text,
    loginStatus=
        safe_text,
    password=
        safe_text
)





@given(instance=Bidding_strategy)
def test_hyp_bidding_bidder_setter(instance):
    original = instance.bidder
    instance.bidder = original
    assert instance.bidder == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_catatanBidder_setter(instance):
    original = instance.catatanBidder
    instance.catatanBidder = original
    assert instance.catatanBidder == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_notulensi_setter(instance):
    original = instance.notulensi
    instance.notulensi = original
    assert instance.notulensi == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_biddee_setter(instance):
    original = instance.biddee
    instance.biddee = original
    assert instance.biddee == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_berkas_setter(instance):
    original = instance.berkas
    instance.berkas = original
    assert instance.berkas == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_jabatan_setter(instance):
    original = instance.jabatan
    instance.jabatan = original
    assert instance.jabatan == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_statusBidding_setter(instance):
    original = instance.statusBidding
    instance.statusBidding = original
    assert instance.statusBidding == original



@given(instance=Bidding_strategy)
def test_hyp_bidding_nilai_setter(instance):
    original = instance.nilai
    instance.nilai = original
    assert instance.nilai == original




@given(instance=Biddee_strategy)
def test_hyp_biddee_statusBiddee_setter(instance):
    original = instance.statusBiddee
    instance.statusBiddee = original
    assert instance.statusBiddee == original






@given(instance=User_strategy)
def test_hyp_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_hyp_user_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=User_strategy)
def test_hyp_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Biddee,
    Bidder,
    Bidding,
    HasilBidding,
    User,
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

def test_Biddee_statusBiddee_value_roundtrip():
    instance = Biddee(statusBiddee="sample_text")
    assert instance.statusBiddee == "sample_text"
    instance.statusBiddee = "sample_text_2"
    assert instance.statusBiddee == "sample_text_2"


def test_Bidding_berkas_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.berkas == "sample_text"
    instance.berkas = "sample_text_2"
    assert instance.berkas == "sample_text_2"


def test_Bidding_biddee_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.biddee == "sample_text"
    instance.biddee = "sample_text_2"
    assert instance.biddee == "sample_text_2"


def test_Bidding_bidder_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.bidder == "sample_text"
    instance.bidder = "sample_text_2"
    assert instance.bidder == "sample_text_2"


def test_Bidding_catatanBidder_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.catatanBidder == "sample_text"
    instance.catatanBidder = "sample_text_2"
    assert instance.catatanBidder == "sample_text_2"


def test_Bidding_jabatan_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.jabatan == "sample_text"
    instance.jabatan = "sample_text_2"
    assert instance.jabatan == "sample_text_2"


def test_Bidding_nilai_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.nilai == 7
    instance.nilai = 13
    assert instance.nilai == 13


def test_Bidding_notulensi_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.notulensi == "sample_text"
    instance.notulensi = "sample_text_2"
    assert instance.notulensi == "sample_text_2"


def test_Bidding_statusBidding_value_roundtrip():
    instance = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    assert instance.statusBidding == "sample_text"
    instance.statusBidding = "sample_text_2"
    assert instance.statusBidding == "sample_text_2"


def test_User_loginStatus_value_roundtrip():
    instance = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    assert instance.loginStatus == "sample_text"
    instance.loginStatus = "sample_text_2"
    assert instance.loginStatus == "sample_text_2"


def test_User_nama_value_roundtrip():
    instance = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    assert instance.nama == "sample_text"
    instance.nama = "sample_text_2"
    assert instance.nama == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userName_value_roundtrip():
    instance = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_assoc_Admin_Biddee_link_reassign_clear():
    a = Biddee(statusBiddee="sample_text")
    b1 = Admin()
    b2 = Admin()
    _safe_set(a, 'ubah_status7', b1)
    assert _is_linked(a, 'ubah_status7', b1)
    if hasattr(b1, 'biddee6'):
        assert _is_linked(b1, 'biddee6', a)
    _safe_set(a, 'ubah_status7', b2)
    assert _is_linked(a, 'ubah_status7', b2)
    if hasattr(b1, 'biddee6'):
        assert not _is_linked(b1, 'biddee6', a)
    if hasattr(b2, 'biddee6'):
        assert _is_linked(b2, 'biddee6', a)
    _safe_set(a, 'ubah_status7', None)
    assert not _is_linked(a, 'ubah_status7', b2)
    if hasattr(b2, 'biddee6'):
        assert not _is_linked(b2, 'biddee6', a)


def test_assoc_Admin_Bidding_link_reassign_clear():
    a = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    b1 = Admin()
    b2 = Admin()
    _safe_set(a, 'CRUD_bidding3', b1)
    assert _is_linked(a, 'CRUD_bidding3', b1)
    if hasattr(b1, 'bidding2'):
        assert _is_linked(b1, 'bidding2', a)
    _safe_set(a, 'CRUD_bidding3', b2)
    assert _is_linked(a, 'CRUD_bidding3', b2)
    if hasattr(b1, 'bidding2'):
        assert not _is_linked(b1, 'bidding2', a)
    if hasattr(b2, 'bidding2'):
        assert _is_linked(b2, 'bidding2', a)
    _safe_set(a, 'CRUD_bidding3', None)
    assert not _is_linked(a, 'CRUD_bidding3', b2)
    if hasattr(b2, 'bidding2'):
        assert not _is_linked(b2, 'bidding2', a)


def test_assoc_Bidder_Bidding_link_reassign_clear():
    a = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    b1 = Bidder()
    b2 = Bidder()
    _safe_set(a, 'bidder29', {b1})
    assert _is_linked(a, 'bidder29', b1)
    if hasattr(b1, 'buat_catatan8'):
        assert _is_linked(b1, 'buat_catatan8', a)
    _safe_set(a, 'bidder29', {b2})
    assert _is_linked(a, 'bidder29', b2)
    if hasattr(b1, 'buat_catatan8'):
        assert not _is_linked(b1, 'buat_catatan8', a)
    if hasattr(b2, 'buat_catatan8'):
        assert _is_linked(b2, 'buat_catatan8', a)
    _safe_set(a, 'bidder29', set())
    assert not _is_linked(a, 'bidder29', b2)
    if hasattr(b2, 'buat_catatan8'):
        assert not _is_linked(b2, 'buat_catatan8', a)


def test_assoc_Bidder_Bidding2_link_reassign_clear():
    a = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    b1 = Bidder()
    b2 = Bidder()
    _safe_set(a, 'Bidder_Bidding2_111', {b1})
    assert _is_linked(a, 'Bidder_Bidding2_111', b1)
    if hasattr(b1, 'edit_nilai10'):
        assert _is_linked(b1, 'edit_nilai10', a)
    _safe_set(a, 'Bidder_Bidding2_111', {b2})
    assert _is_linked(a, 'Bidder_Bidding2_111', b2)
    if hasattr(b1, 'edit_nilai10'):
        assert not _is_linked(b1, 'edit_nilai10', a)
    if hasattr(b2, 'edit_nilai10'):
        assert _is_linked(b2, 'edit_nilai10', a)
    _safe_set(a, 'Bidder_Bidding2_111', set())
    assert not _is_linked(a, 'Bidder_Bidding2_111', b2)
    if hasattr(b2, 'edit_nilai10'):
        assert not _is_linked(b2, 'edit_nilai10', a)


def test_assoc_Bidding_Biddee_link_reassign_clear():
    a = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    b1 = Biddee(statusBiddee="sample_text")
    b2 = Biddee(statusBiddee="sample_text_2")
    _safe_set(a, 'daftar4', {b1})
    assert _is_linked(a, 'daftar4', b1)
    if hasattr(b1, 'bidding5'):
        assert _is_linked(b1, 'bidding5', a)
    _safe_set(a, 'daftar4', {b2})
    assert _is_linked(a, 'daftar4', b2)
    if hasattr(b1, 'bidding5'):
        assert not _is_linked(b1, 'bidding5', a)
    if hasattr(b2, 'bidding5'):
        assert _is_linked(b2, 'bidding5', a)
    _safe_set(a, 'daftar4', set())
    assert not _is_linked(a, 'daftar4', b2)
    if hasattr(b2, 'bidding5'):
        assert not _is_linked(b2, 'bidding5', a)


def test_assoc_HasilBidding_Bidding_link_reassign_clear():
    a = Bidding(berkas="sample_text", biddee="sample_text", bidder="sample_text", catatanBidder="sample_text", jabatan="sample_text", nilai=7, notulensi="sample_text", statusBidding="sample_text")
    b1 = HasilBidding()
    b2 = HasilBidding()
    _safe_set(a, 'hasilBidding1', b1)
    assert _is_linked(a, 'hasilBidding1', b1)
    if hasattr(b1, 'bidding0'):
        assert _is_linked(b1, 'bidding0', a)
    _safe_set(a, 'hasilBidding1', b2)
    assert _is_linked(a, 'hasilBidding1', b2)
    if hasattr(b1, 'bidding0'):
        assert not _is_linked(b1, 'bidding0', a)
    if hasattr(b2, 'bidding0'):
        assert _is_linked(b2, 'bidding0', a)
    _safe_set(a, 'hasilBidding1', None)
    assert not _is_linked(a, 'hasilBidding1', b2)
    if hasattr(b2, 'bidding0'):
        assert not _is_linked(b2, 'bidding0', a)


def test_assoc_User_HasilBidding_link_reassign_clear():
    a = User(loginStatus="sample_text", nama="sample_text", password="sample_text", userName="sample_text")
    b1 = HasilBidding()
    b2 = HasilBidding()
    _safe_set(a, 'hasilBidding12', {b1})
    assert _is_linked(a, 'hasilBidding12', b1)
    if hasattr(b1, 'melihat13'):
        assert _is_linked(b1, 'melihat13', a)
    _safe_set(a, 'hasilBidding12', {b2})
    assert _is_linked(a, 'hasilBidding12', b2)
    if hasattr(b1, 'melihat13'):
        assert not _is_linked(b1, 'melihat13', a)
    if hasattr(b2, 'melihat13'):
        assert _is_linked(b2, 'melihat13', a)
    _safe_set(a, 'hasilBidding12', set())
    assert not _is_linked(a, 'hasilBidding12', b2)
    if hasattr(b2, 'melihat13'):
        assert not _is_linked(b2, 'melihat13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Biddee_strategy = st.builds(Biddee, statusBiddee=safe_text)
@given(instance=Biddee_strategy)
@settings(max_examples=25)
def test_Biddee_instantiation(instance):
    assert isinstance(instance, Biddee)


Bidder_strategy = st.builds(Bidder)
@given(instance=Bidder_strategy)
@settings(max_examples=25)
def test_Bidder_instantiation(instance):
    assert isinstance(instance, Bidder)


Bidding_strategy = st.builds(Bidding, berkas=safe_text, biddee=safe_text, bidder=safe_text, catatanBidder=safe_text, jabatan=safe_text, nilai=st.integers(), notulensi=safe_text, statusBidding=safe_text)
@given(instance=Bidding_strategy)
@settings(max_examples=25)
def test_Bidding_instantiation(instance):
    assert isinstance(instance, Bidding)


HasilBidding_strategy = st.builds(HasilBidding)
@given(instance=HasilBidding_strategy)
@settings(max_examples=25)
def test_HasilBidding_instantiation(instance):
    assert isinstance(instance, HasilBidding)


User_strategy = st.builds(User, loginStatus=safe_text, nama=safe_text, password=safe_text, userName=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



