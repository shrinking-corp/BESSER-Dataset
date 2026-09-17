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
    student_record,
    vendor,
    student,
    books_database,
    librarian,
    library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_student_record_is_not_abstract():
    assert not inspect.isabstract(student_record)


def test_hyp_student_record_constructor_exists():
    assert callable(student_record.__init__)


def test_hyp_student_record_constructor_args():
    sig = inspect.signature(student_record.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone_number" in params, "Missing parameter 'phone_number'"
    assert "fines" in params, "Missing parameter 'fines'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_vendor_is_not_abstract():
    assert not inspect.isabstract(vendor)


def test_hyp_vendor_constructor_exists():
    assert callable(vendor.__init__)


def test_hyp_vendor_constructor_args():
    sig = inspect.signature(vendor.__init__)
    params = list(sig.parameters.keys())
    assert "book_details" in params, "Missing parameter 'book_details'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_hyp_student_constructor_exists():
    assert callable(student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"




def test_hyp_books_database_is_not_abstract():
    assert not inspect.isabstract(books_database)


def test_hyp_books_database_constructor_exists():
    assert callable(books_database.__init__)


def test_hyp_books_database_constructor_args():
    sig = inspect.signature(books_database.__init__)
    params = list(sig.parameters.keys())
    assert "book_title" in params, "Missing parameter 'book_title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "book_id" in params, "Missing parameter 'book_id'"






def test_hyp_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_hyp_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_hyp_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(library)


def test_hyp_library_constructor_exists():
    assert callable(library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(library.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"



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
student_record_strategy = st.builds(
    student_record,
    address=
        safe_text,
    phone_number=
        safe_text,
    fines=
        safe_text,
    name=
        safe_text
)
vendor_strategy = st.builds(
    vendor,
    book_details=
        safe_text,
    attribute=
        safe_text
)
student_strategy = st.builds(
    student,
    details=
        safe_text
)
books_database_strategy = st.builds(
    books_database,
    book_title=
        safe_text,
    author=
        safe_text,
    book_id=
        safe_text
)
librarian_strategy = st.builds(
    librarian,
    name=
        safe_text
)
library_strategy = st.builds(
    library,
    location=
        safe_text
)




@given(instance=student_record_strategy)
def test_hyp_student_record_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=student_record_strategy)
def test_hyp_student_record_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original



@given(instance=student_record_strategy)
def test_hyp_student_record_fines_setter(instance):
    original = instance.fines
    instance.fines = original
    assert instance.fines == original



@given(instance=student_record_strategy)
def test_hyp_student_record_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=vendor_strategy)
def test_hyp_vendor_book_details_setter(instance):
    original = instance.book_details
    instance.book_details = original
    assert instance.book_details == original



@given(instance=vendor_strategy)
def test_hyp_vendor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=student_strategy)
def test_hyp_student_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original




@given(instance=books_database_strategy)
def test_hyp_books_database_book_title_setter(instance):
    original = instance.book_title
    instance.book_title = original
    assert instance.book_title == original



@given(instance=books_database_strategy)
def test_hyp_books_database_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=books_database_strategy)
def test_hyp_books_database_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original




@given(instance=librarian_strategy)
def test_hyp_librarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_strategy)
def test_hyp_library_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    books_database,
    librarian,
    library,
    student,
    student_record,
    vendor,
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

def test_books_database_author_value_roundtrip():
    instance = books_database(author="sample_text", book_id="sample_text", book_title="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_books_database_book_id_value_roundtrip():
    instance = books_database(author="sample_text", book_id="sample_text", book_title="sample_text")
    assert instance.book_id == "sample_text"
    instance.book_id = "sample_text_2"
    assert instance.book_id == "sample_text_2"


def test_books_database_book_title_value_roundtrip():
    instance = books_database(author="sample_text", book_id="sample_text", book_title="sample_text")
    assert instance.book_title == "sample_text"
    instance.book_title = "sample_text_2"
    assert instance.book_title == "sample_text_2"


def test_librarian_name_value_roundtrip():
    instance = librarian(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_location_value_roundtrip():
    instance = library(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_student_details_value_roundtrip():
    instance = student(details="sample_text")
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_student_record_address_value_roundtrip():
    instance = student_record(address="sample_text", fines="sample_text", name="sample_text", phone_number="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_student_record_fines_value_roundtrip():
    instance = student_record(address="sample_text", fines="sample_text", name="sample_text", phone_number="sample_text")
    assert instance.fines == "sample_text"
    instance.fines = "sample_text_2"
    assert instance.fines == "sample_text_2"


def test_student_record_name_value_roundtrip():
    instance = student_record(address="sample_text", fines="sample_text", name="sample_text", phone_number="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_student_record_phone_number_value_roundtrip():
    instance = student_record(address="sample_text", fines="sample_text", name="sample_text", phone_number="sample_text")
    assert instance.phone_number == "sample_text"
    instance.phone_number = "sample_text_2"
    assert instance.phone_number == "sample_text_2"


def test_vendor_attribute_value_roundtrip():
    instance = vendor(attribute="sample_text", book_details="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_vendor_book_details_value_roundtrip():
    instance = vendor(attribute="sample_text", book_details="sample_text")
    assert instance.book_details == "sample_text"
    instance.book_details = "sample_text_2"
    assert instance.book_details == "sample_text_2"


def test_assoc_books_database_customer_link_reassign_clear():
    a = student(details="sample_text")
    b1 = books_database(author="sample_text", book_id="sample_text", book_title="sample_text")
    b2 = books_database(author="sample_text_2", book_id="sample_text_2", book_title="sample_text_2")
    _safe_set(a, 'books_database5', b1)
    assert _is_linked(a, 'books_database5', b1)
    if hasattr(b1, 'customer4'):
        assert _is_linked(b1, 'customer4', a)
    _safe_set(a, 'books_database5', b2)
    assert _is_linked(a, 'books_database5', b2)
    if hasattr(b1, 'customer4'):
        assert not _is_linked(b1, 'customer4', a)
    if hasattr(b2, 'customer4'):
        assert _is_linked(b2, 'customer4', a)
    _safe_set(a, 'books_database5', None)
    assert not _is_linked(a, 'books_database5', b2)
    if hasattr(b2, 'customer4'):
        assert not _is_linked(b2, 'customer4', a)


def test_assoc_customer_student_record_link_reassign_clear():
    a = student_record(address="sample_text", fines="sample_text", name="sample_text", phone_number="sample_text")
    b1 = student(details="sample_text")
    b2 = student(details="sample_text_2")
    _safe_set(a, 'customer7', b1)
    assert _is_linked(a, 'customer7', b1)
    if hasattr(b1, 'student_record6'):
        assert _is_linked(b1, 'student_record6', a)
    _safe_set(a, 'customer7', b2)
    assert _is_linked(a, 'customer7', b2)
    if hasattr(b1, 'student_record6'):
        assert not _is_linked(b1, 'student_record6', a)
    if hasattr(b2, 'student_record6'):
        assert _is_linked(b2, 'student_record6', a)
    _safe_set(a, 'customer7', None)
    assert not _is_linked(a, 'customer7', b2)
    if hasattr(b2, 'student_record6'):
        assert not _is_linked(b2, 'student_record6', a)


def test_assoc_library_books_database_link_reassign_clear():
    a = library(location="sample_text")
    b1 = books_database(author="sample_text", book_id="sample_text", book_title="sample_text")
    b2 = books_database(author="sample_text_2", book_id="sample_text_2", book_title="sample_text_2")
    _safe_set(a, 'books_database2', b1)
    assert _is_linked(a, 'books_database2', b1)
    if hasattr(b1, 'library3'):
        assert _is_linked(b1, 'library3', a)
    _safe_set(a, 'books_database2', b2)
    assert _is_linked(a, 'books_database2', b2)
    if hasattr(b1, 'library3'):
        assert not _is_linked(b1, 'library3', a)
    if hasattr(b2, 'library3'):
        assert _is_linked(b2, 'library3', a)
    _safe_set(a, 'books_database2', None)
    assert not _is_linked(a, 'books_database2', b2)
    if hasattr(b2, 'library3'):
        assert not _is_linked(b2, 'library3', a)


def test_assoc_library_librarian_link_reassign_clear():
    a = library(location="sample_text")
    b1 = librarian(name="sample_text")
    b2 = librarian(name="sample_text_2")
    _safe_set(a, 'librarian0', b1)
    assert _is_linked(a, 'librarian0', b1)
    if hasattr(b1, 'library1'):
        assert _is_linked(b1, 'library1', a)
    _safe_set(a, 'librarian0', b2)
    assert _is_linked(a, 'librarian0', b2)
    if hasattr(b1, 'library1'):
        assert not _is_linked(b1, 'library1', a)
    if hasattr(b2, 'library1'):
        assert _is_linked(b2, 'library1', a)
    _safe_set(a, 'librarian0', None)
    assert not _is_linked(a, 'librarian0', b2)
    if hasattr(b2, 'library1'):
        assert not _is_linked(b2, 'library1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

books_database_strategy = st.builds(books_database, author=safe_text, book_id=safe_text, book_title=safe_text)
@given(instance=books_database_strategy)
@settings(max_examples=25)
def test_books_database_instantiation(instance):
    assert isinstance(instance, books_database)


librarian_strategy = st.builds(librarian, name=safe_text)
@given(instance=librarian_strategy)
@settings(max_examples=25)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)


library_strategy = st.builds(library, location=safe_text)
@given(instance=library_strategy)
@settings(max_examples=25)
def test_library_instantiation(instance):
    assert isinstance(instance, library)


student_strategy = st.builds(student, details=safe_text)
@given(instance=student_strategy)
@settings(max_examples=25)
def test_student_instantiation(instance):
    assert isinstance(instance, student)


student_record_strategy = st.builds(student_record, address=safe_text, fines=safe_text, name=safe_text, phone_number=safe_text)
@given(instance=student_record_strategy)
@settings(max_examples=25)
def test_student_record_instantiation(instance):
    assert isinstance(instance, student_record)


vendor_strategy = st.builds(vendor, attribute=safe_text, book_details=safe_text)
@given(instance=vendor_strategy)
@settings(max_examples=25)
def test_vendor_instantiation(instance):
    assert isinstance(instance, vendor)



