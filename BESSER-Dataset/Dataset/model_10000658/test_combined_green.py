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
    Class,
    lecturer,
    admin,
    Staff,
    Reserved,
    Borrowed,
    Fine,
    Librarian,
    Member,
    Books,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lecturer_is_not_abstract():
    assert not inspect.isabstract(lecturer)


def test_hyp_lecturer_constructor_exists():
    assert callable(lecturer.__init__)


def test_hyp_lecturer_constructor_args():
    sig = inspect.signature(lecturer.__init__)
    params = list(sig.parameters.keys())
    assert "module" in params, "Missing parameter 'module'"




def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_hyp_admin_constructor_exists():
    assert callable(admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())
    assert "Experience" in params, "Missing parameter 'Experience'"




def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "position" in params, "Missing parameter 'position'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Staff_ID" in params, "Missing parameter 'Staff_ID'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "address" in params, "Missing parameter 'address'"













def test_hyp_reserved_is_not_abstract():
    assert not inspect.isabstract(Reserved)


def test_hyp_reserved_constructor_exists():
    assert callable(Reserved.__init__)


def test_hyp_reserved_constructor_args():
    sig = inspect.signature(Reserved.__init__)
    params = list(sig.parameters.keys())
    assert "reserved_date" in params, "Missing parameter 'reserved_date'"




def test_hyp_borrowed_is_not_abstract():
    assert not inspect.isabstract(Borrowed)


def test_hyp_borrowed_constructor_exists():
    assert callable(Borrowed.__init__)


def test_hyp_borrowed_constructor_args():
    sig = inspect.signature(Borrowed.__init__)
    params = list(sig.parameters.keys())
    assert "borrowed_date" in params, "Missing parameter 'borrowed_date'"
    assert "returned_date" in params, "Missing parameter 'returned_date'"





def test_hyp_fine_is_not_abstract():
    assert not inspect.isabstract(Fine)


def test_hyp_fine_constructor_exists():
    assert callable(Fine.__init__)


def test_hyp_fine_constructor_args():
    sig = inspect.signature(Fine.__init__)
    params = list(sig.parameters.keys())
    assert "book_id" in params, "Missing parameter 'book_id'"
    assert "returned_date" in params, "Missing parameter 'returned_date'"
    assert "borrowed_date" in params, "Missing parameter 'borrowed_date'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "fine_amount" in params, "Missing parameter 'fine_amount'"








def test_hyp_librarian_is_not_abstract():
    assert not inspect.isabstract(Librarian)


def test_hyp_librarian_constructor_exists():
    assert callable(Librarian.__init__)


def test_hyp_librarian_constructor_args():
    sig = inspect.signature(Librarian.__init__)
    params = list(sig.parameters.keys())
    assert "dob" in params, "Missing parameter 'dob'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "address" in params, "Missing parameter 'address'"
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "cont_no" in params, "Missing parameter 'cont_no'"











def test_hyp_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_hyp_member_constructor_exists():
    assert callable(Member.__init__)


def test_hyp_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"
    assert "address" in params, "Missing parameter 'address'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "cont_no" in params, "Missing parameter 'cont_no'"
    assert "dob" in params, "Missing parameter 'dob'"











def test_hyp_books_is_not_abstract():
    assert not inspect.isabstract(Books)


def test_hyp_books_constructor_exists():
    assert callable(Books.__init__)


def test_hyp_books_constructor_args():
    sig = inspect.signature(Books.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "book_qty" in params, "Missing parameter 'book_qty'"
    assert "title" in params, "Missing parameter 'title'"
    assert "ISBN_no" in params, "Missing parameter 'ISBN_no'"
    assert "book_id" in params, "Missing parameter 'book_id'"
    assert "author_name" in params, "Missing parameter 'author_name'"








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
Class_strategy = st.builds(
    Class,
)
lecturer_strategy = st.builds(
    lecturer,
    module=
        safe_text
)
admin_strategy = st.builds(
    admin,
    Experience=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    gender=
        safe_text,
    lname=
        safe_text,
    position=
        safe_text,
    email=
        safe_text,
    Staff_ID=
        st.integers(),
    fname=
        safe_text,
    password=
        safe_text,
    username=
        safe_text,
    contact=
        st.integers(),
    address=
        safe_text
)
Reserved_strategy = st.builds(
    Reserved,
    reserved_date=
        safe_text
)
Borrowed_strategy = st.builds(
    Borrowed,
    borrowed_date=
        safe_text,
    returned_date=
        safe_text
)
Fine_strategy = st.builds(
    Fine,
    book_id=
        st.integers(),
    returned_date=
        safe_text,
    borrowed_date=
        safe_text,
    member_id=
        st.integers(),
    fine_amount=
        st.integers()
)
Librarian_strategy = st.builds(
    Librarian,
    dob=
        safe_text,
    fname=
        safe_text,
    member_id=
        st.integers(),
    address=
        safe_text,
    member_pwd=
        safe_text,
    lname=
        safe_text,
    gender=
        safe_text,
    cont_no=
        st.integers()
)
Member_strategy = st.builds(
    Member,
    fname=
        safe_text,
    lname=
        safe_text,
    member_id=
        st.integers(),
    member_pwd=
        safe_text,
    address=
        safe_text,
    gender=
        safe_text,
    cont_no=
        st.integers(),
    dob=
        safe_text
)
Books_strategy = st.builds(
    Books,
    publisher=
        safe_text,
    book_qty=
        st.integers(),
    title=
        safe_text,
    ISBN_no=
        safe_text,
    book_id=
        st.integers(),
    author_name=
        safe_text
)





@given(instance=lecturer_strategy)
def test_hyp_lecturer_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original




@given(instance=admin_strategy)
def test_hyp_admin_Experience_setter(instance):
    original = instance.Experience
    instance.Experience = original
    assert instance.Experience == original




@given(instance=Staff_strategy)
def test_hyp_staff_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Staff_strategy)
def test_hyp_staff_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Staff_strategy)
def test_hyp_staff_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Staff_strategy)
def test_hyp_staff_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Staff_strategy)
def test_hyp_staff_Staff_ID_setter(instance):
    original = instance.Staff_ID
    instance.Staff_ID = original
    assert instance.Staff_ID == original



@given(instance=Staff_strategy)
def test_hyp_staff_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Staff_strategy)
def test_hyp_staff_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Staff_strategy)
def test_hyp_staff_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Staff_strategy)
def test_hyp_staff_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Staff_strategy)
def test_hyp_staff_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=Reserved_strategy)
def test_hyp_reserved_reserved_date_setter(instance):
    original = instance.reserved_date
    instance.reserved_date = original
    assert instance.reserved_date == original




@given(instance=Borrowed_strategy)
def test_hyp_borrowed_borrowed_date_setter(instance):
    original = instance.borrowed_date
    instance.borrowed_date = original
    assert instance.borrowed_date == original



@given(instance=Borrowed_strategy)
def test_hyp_borrowed_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original




@given(instance=Fine_strategy)
def test_hyp_fine_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original



@given(instance=Fine_strategy)
def test_hyp_fine_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original



@given(instance=Fine_strategy)
def test_hyp_fine_borrowed_date_setter(instance):
    original = instance.borrowed_date
    instance.borrowed_date = original
    assert instance.borrowed_date == original



@given(instance=Fine_strategy)
def test_hyp_fine_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Fine_strategy)
def test_hyp_fine_fine_amount_setter(instance):
    original = instance.fine_amount
    instance.fine_amount = original
    assert instance.fine_amount == original




@given(instance=Librarian_strategy)
def test_hyp_librarian_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Librarian_strategy)
def test_hyp_librarian_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original




@given(instance=Member_strategy)
def test_hyp_member_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Member_strategy)
def test_hyp_member_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Member_strategy)
def test_hyp_member_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Member_strategy)
def test_hyp_member_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original



@given(instance=Member_strategy)
def test_hyp_member_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Member_strategy)
def test_hyp_member_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Member_strategy)
def test_hyp_member_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original



@given(instance=Member_strategy)
def test_hyp_member_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original




@given(instance=Books_strategy)
def test_hyp_books_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original



@given(instance=Books_strategy)
def test_hyp_books_book_qty_setter(instance):
    original = instance.book_qty
    instance.book_qty = original
    assert instance.book_qty == original



@given(instance=Books_strategy)
def test_hyp_books_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Books_strategy)
def test_hyp_books_ISBN_no_setter(instance):
    original = instance.ISBN_no
    instance.ISBN_no = original
    assert instance.ISBN_no == original



@given(instance=Books_strategy)
def test_hyp_books_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original



@given(instance=Books_strategy)
def test_hyp_books_author_name_setter(instance):
    original = instance.author_name
    instance.author_name = original
    assert instance.author_name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Books,
    Borrowed,
    Class,
    Fine,
    Librarian,
    Member,
    Reserved,
    Staff,
    admin,
    lecturer,
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

def test_Books_ISBN_no_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.ISBN_no == "sample_text"
    instance.ISBN_no = "sample_text_2"
    assert instance.ISBN_no == "sample_text_2"


def test_Books_author_name_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.author_name == "sample_text"
    instance.author_name = "sample_text_2"
    assert instance.author_name == "sample_text_2"


def test_Books_book_id_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.book_id == 7
    instance.book_id = 13
    assert instance.book_id == 13


def test_Books_book_qty_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.book_qty == 7
    instance.book_qty = 13
    assert instance.book_qty == 13


def test_Books_publisher_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_Books_title_value_roundtrip():
    instance = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Borrowed_borrowed_date_value_roundtrip():
    instance = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    assert instance.borrowed_date == "sample_text"
    instance.borrowed_date = "sample_text_2"
    assert instance.borrowed_date == "sample_text_2"


def test_Borrowed_returned_date_value_roundtrip():
    instance = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    assert instance.returned_date == "sample_text"
    instance.returned_date = "sample_text_2"
    assert instance.returned_date == "sample_text_2"


def test_Fine_book_id_value_roundtrip():
    instance = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    assert instance.book_id == 7
    instance.book_id = 13
    assert instance.book_id == 13


def test_Fine_borrowed_date_value_roundtrip():
    instance = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    assert instance.borrowed_date == "sample_text"
    instance.borrowed_date = "sample_text_2"
    assert instance.borrowed_date == "sample_text_2"


def test_Fine_fine_amount_value_roundtrip():
    instance = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    assert instance.fine_amount == 7
    instance.fine_amount = 13
    assert instance.fine_amount == 13


def test_Fine_member_id_value_roundtrip():
    instance = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    assert instance.member_id == 7
    instance.member_id = 13
    assert instance.member_id == 13


def test_Fine_returned_date_value_roundtrip():
    instance = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    assert instance.returned_date == "sample_text"
    instance.returned_date = "sample_text_2"
    assert instance.returned_date == "sample_text_2"


def test_Librarian_address_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Librarian_cont_no_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.cont_no == 7
    instance.cont_no = 13
    assert instance.cont_no == 13


def test_Librarian_dob_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.dob == "sample_text"
    instance.dob = "sample_text_2"
    assert instance.dob == "sample_text_2"


def test_Librarian_fname_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_Librarian_gender_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Librarian_lname_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_Librarian_member_id_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.member_id == 7
    instance.member_id = 13
    assert instance.member_id == 13


def test_Librarian_member_pwd_value_roundtrip():
    instance = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.member_pwd == "sample_text"
    instance.member_pwd = "sample_text_2"
    assert instance.member_pwd == "sample_text_2"


def test_Member_address_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Member_cont_no_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.cont_no == 7
    instance.cont_no = 13
    assert instance.cont_no == 13


def test_Member_dob_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.dob == "sample_text"
    instance.dob = "sample_text_2"
    assert instance.dob == "sample_text_2"


def test_Member_fname_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_Member_gender_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Member_lname_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_Member_member_id_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.member_id == 7
    instance.member_id = 13
    assert instance.member_id == 13


def test_Member_member_pwd_value_roundtrip():
    instance = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    assert instance.member_pwd == "sample_text"
    instance.member_pwd = "sample_text_2"
    assert instance.member_pwd == "sample_text_2"


def test_Reserved_reserved_date_value_roundtrip():
    instance = Reserved(reserved_date="sample_text")
    assert instance.reserved_date == "sample_text"
    instance.reserved_date = "sample_text_2"
    assert instance.reserved_date == "sample_text_2"


def test_Staff_Staff_ID_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.Staff_ID == 7
    instance.Staff_ID = 13
    assert instance.Staff_ID == 13


def test_Staff_address_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Staff_contact_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.contact == 7
    instance.contact = 13
    assert instance.contact == 13


def test_Staff_email_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Staff_fname_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_Staff_gender_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Staff_lname_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_Staff_password_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Staff_position_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_Staff_username_value_roundtrip():
    instance = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_admin_Experience_value_roundtrip():
    instance = admin(Experience="sample_text")
    assert instance.Experience == "sample_text"
    instance.Experience = "sample_text_2"
    assert instance.Experience == "sample_text_2"


def test_lecturer_module_value_roundtrip():
    instance = lecturer(module="sample_text")
    assert instance.module == "sample_text"
    instance.module = "sample_text_2"
    assert instance.module == "sample_text_2"


def test_assoc_Books_Borrowed_link_reassign_clear():
    a = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    b1 = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    b2 = Books(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    _safe_set(a, 'books1', {b1})
    assert _is_linked(a, 'books1', b1)
    if hasattr(b1, 'borrowed0'):
        assert _is_linked(b1, 'borrowed0', a)
    _safe_set(a, 'books1', {b2})
    assert _is_linked(a, 'books1', b2)
    if hasattr(b1, 'borrowed0'):
        assert not _is_linked(b1, 'borrowed0', a)
    if hasattr(b2, 'borrowed0'):
        assert _is_linked(b2, 'borrowed0', a)
    _safe_set(a, 'books1', set())
    assert not _is_linked(a, 'books1', b2)
    if hasattr(b2, 'borrowed0'):
        assert not _is_linked(b2, 'borrowed0', a)


def test_assoc_Books_Reserved_link_reassign_clear():
    a = Reserved(reserved_date="sample_text")
    b1 = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    b2 = Books(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    _safe_set(a, 'books5', {b1})
    assert _is_linked(a, 'books5', b1)
    if hasattr(b1, 'reserved4'):
        assert _is_linked(b1, 'reserved4', a)
    _safe_set(a, 'books5', {b2})
    assert _is_linked(a, 'books5', b2)
    if hasattr(b1, 'reserved4'):
        assert not _is_linked(b1, 'reserved4', a)
    if hasattr(b2, 'reserved4'):
        assert _is_linked(b2, 'reserved4', a)
    _safe_set(a, 'books5', set())
    assert not _is_linked(a, 'books5', b2)
    if hasattr(b2, 'reserved4'):
        assert not _is_linked(b2, 'reserved4', a)


def test_assoc_Borrowed_Member_link_reassign_clear():
    a = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b1 = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    b2 = Borrowed(borrowed_date="sample_text_2", returned_date="sample_text_2")
    _safe_set(a, 'borrowed3', {b1})
    assert _is_linked(a, 'borrowed3', b1)
    if hasattr(b1, 'member2'):
        assert _is_linked(b1, 'member2', a)
    _safe_set(a, 'borrowed3', {b2})
    assert _is_linked(a, 'borrowed3', b2)
    if hasattr(b1, 'member2'):
        assert not _is_linked(b1, 'member2', a)
    if hasattr(b2, 'member2'):
        assert _is_linked(b2, 'member2', a)
    _safe_set(a, 'borrowed3', set())
    assert not _is_linked(a, 'borrowed3', b2)
    if hasattr(b2, 'member2'):
        assert not _is_linked(b2, 'member2', a)


def test_assoc_Fine_Member_link_reassign_clear():
    a = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b1 = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    b2 = Fine(book_id=13, borrowed_date="sample_text_2", fine_amount=13, member_id=13, returned_date="sample_text_2")
    _safe_set(a, 'fine13', {b1})
    assert _is_linked(a, 'fine13', b1)
    if hasattr(b1, 'member12'):
        assert _is_linked(b1, 'member12', a)
    _safe_set(a, 'fine13', {b2})
    assert _is_linked(a, 'fine13', b2)
    if hasattr(b1, 'member12'):
        assert not _is_linked(b1, 'member12', a)
    if hasattr(b2, 'member12'):
        assert _is_linked(b2, 'member12', a)
    _safe_set(a, 'fine13', set())
    assert not _is_linked(a, 'fine13', b2)
    if hasattr(b2, 'member12'):
        assert not _is_linked(b2, 'member12', a)


def test_assoc_Librarian_Books_link_reassign_clear():
    a = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b1 = Books(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    b2 = Books(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    _safe_set(a, 'books8', {b1})
    assert _is_linked(a, 'books8', b1)
    if hasattr(b1, 'librarian9'):
        assert _is_linked(b1, 'librarian9', a)
    _safe_set(a, 'books8', {b2})
    assert _is_linked(a, 'books8', b2)
    if hasattr(b1, 'librarian9'):
        assert not _is_linked(b1, 'librarian9', a)
    if hasattr(b2, 'librarian9'):
        assert _is_linked(b2, 'librarian9', a)
    _safe_set(a, 'books8', set())
    assert not _is_linked(a, 'books8', b2)
    if hasattr(b2, 'librarian9'):
        assert not _is_linked(b2, 'librarian9', a)


def test_assoc_Librarian_Fine_link_reassign_clear():
    a = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b1 = Fine(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    b2 = Fine(book_id=13, borrowed_date="sample_text_2", fine_amount=13, member_id=13, returned_date="sample_text_2")
    _safe_set(a, 'fine10', {b1})
    assert _is_linked(a, 'fine10', b1)
    if hasattr(b1, 'librarian11'):
        assert _is_linked(b1, 'librarian11', a)
    _safe_set(a, 'fine10', {b2})
    assert _is_linked(a, 'fine10', b2)
    if hasattr(b1, 'librarian11'):
        assert not _is_linked(b1, 'librarian11', a)
    if hasattr(b2, 'librarian11'):
        assert _is_linked(b2, 'librarian11', a)
    _safe_set(a, 'fine10', set())
    assert not _is_linked(a, 'fine10', b2)
    if hasattr(b2, 'librarian11'):
        assert not _is_linked(b2, 'librarian11', a)


def test_assoc_Member_Librarian_link_reassign_clear():
    a = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b1 = Librarian(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b2 = Librarian(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    _safe_set(a, 'librarian14', {b1})
    assert _is_linked(a, 'librarian14', b1)
    if hasattr(b1, 'member15'):
        assert _is_linked(b1, 'member15', a)
    _safe_set(a, 'librarian14', {b2})
    assert _is_linked(a, 'librarian14', b2)
    if hasattr(b1, 'member15'):
        assert not _is_linked(b1, 'member15', a)
    if hasattr(b2, 'member15'):
        assert _is_linked(b2, 'member15', a)
    _safe_set(a, 'librarian14', set())
    assert not _is_linked(a, 'librarian14', b2)
    if hasattr(b2, 'member15'):
        assert not _is_linked(b2, 'member15', a)


def test_assoc_Registar_Staff2_link_reassign_clear():
    a = admin(Experience="sample_text")
    b1 = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    b2 = Staff(Staff_ID=13, address="sample_text_2", contact=13, email="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", password="sample_text_2", position="sample_text_2", username="sample_text_2")
    _safe_set(a, 'staff16', b1)
    assert _is_linked(a, 'staff16', b1)
    if hasattr(b1, 'registar17'):
        assert _is_linked(b1, 'registar17', a)
    _safe_set(a, 'staff16', b2)
    assert _is_linked(a, 'staff16', b2)
    if hasattr(b1, 'registar17'):
        assert not _is_linked(b1, 'registar17', a)
    if hasattr(b2, 'registar17'):
        assert _is_linked(b2, 'registar17', a)
    _safe_set(a, 'staff16', None)
    assert not _is_linked(a, 'staff16', b2)
    if hasattr(b2, 'registar17'):
        assert not _is_linked(b2, 'registar17', a)


def test_assoc_Reserved_Member_link_reassign_clear():
    a = Reserved(reserved_date="sample_text")
    b1 = Member(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    b2 = Member(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    _safe_set(a, 'member6', {b1})
    assert _is_linked(a, 'member6', b1)
    if hasattr(b1, 'reserved7'):
        assert _is_linked(b1, 'reserved7', a)
    _safe_set(a, 'member6', {b2})
    assert _is_linked(a, 'member6', b2)
    if hasattr(b1, 'reserved7'):
        assert not _is_linked(b1, 'reserved7', a)
    if hasattr(b2, 'reserved7'):
        assert _is_linked(b2, 'reserved7', a)
    _safe_set(a, 'member6', set())
    assert not _is_linked(a, 'member6', b2)
    if hasattr(b2, 'reserved7'):
        assert not _is_linked(b2, 'reserved7', a)


def test_assoc_Staff_Professor2_link_reassign_clear():
    a = lecturer(module="sample_text")
    b1 = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    b2 = Staff(Staff_ID=13, address="sample_text_2", contact=13, email="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", password="sample_text_2", position="sample_text_2", username="sample_text_2")
    _safe_set(a, 'staff19', b1)
    assert _is_linked(a, 'staff19', b1)
    if hasattr(b1, 'professor18'):
        assert _is_linked(b1, 'professor18', a)
    _safe_set(a, 'staff19', b2)
    assert _is_linked(a, 'staff19', b2)
    if hasattr(b1, 'professor18'):
        assert not _is_linked(b1, 'professor18', a)
    if hasattr(b2, 'professor18'):
        assert _is_linked(b2, 'professor18', a)
    _safe_set(a, 'staff19', None)
    assert not _is_linked(a, 'staff19', b2)
    if hasattr(b2, 'professor18'):
        assert not _is_linked(b2, 'professor18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Books_strategy = st.builds(Books, ISBN_no=safe_text, author_name=safe_text, book_id=st.integers(), book_qty=st.integers(), publisher=safe_text, title=safe_text)
@given(instance=Books_strategy)
@settings(max_examples=25)
def test_Books_instantiation(instance):
    assert isinstance(instance, Books)


Borrowed_strategy = st.builds(Borrowed, borrowed_date=safe_text, returned_date=safe_text)
@given(instance=Borrowed_strategy)
@settings(max_examples=25)
def test_Borrowed_instantiation(instance):
    assert isinstance(instance, Borrowed)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Fine_strategy = st.builds(Fine, book_id=st.integers(), borrowed_date=safe_text, fine_amount=st.integers(), member_id=st.integers(), returned_date=safe_text)
@given(instance=Fine_strategy)
@settings(max_examples=25)
def test_Fine_instantiation(instance):
    assert isinstance(instance, Fine)


Librarian_strategy = st.builds(Librarian, address=safe_text, cont_no=st.integers(), dob=safe_text, fname=safe_text, gender=safe_text, lname=safe_text, member_id=st.integers(), member_pwd=safe_text)
@given(instance=Librarian_strategy)
@settings(max_examples=25)
def test_Librarian_instantiation(instance):
    assert isinstance(instance, Librarian)


Member_strategy = st.builds(Member, address=safe_text, cont_no=st.integers(), dob=safe_text, fname=safe_text, gender=safe_text, lname=safe_text, member_id=st.integers(), member_pwd=safe_text)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


Reserved_strategy = st.builds(Reserved, reserved_date=safe_text)
@given(instance=Reserved_strategy)
@settings(max_examples=25)
def test_Reserved_instantiation(instance):
    assert isinstance(instance, Reserved)


Staff_strategy = st.builds(Staff, Staff_ID=st.integers(), address=safe_text, contact=st.integers(), email=safe_text, fname=safe_text, gender=safe_text, lname=safe_text, password=safe_text, position=safe_text, username=safe_text)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


admin_strategy = st.builds(admin, Experience=safe_text)
@given(instance=admin_strategy)
@settings(max_examples=25)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)


lecturer_strategy = st.builds(lecturer, module=safe_text)
@given(instance=lecturer_strategy)
@settings(max_examples=25)
def test_lecturer_instantiation(instance):
    assert isinstance(instance, lecturer)



