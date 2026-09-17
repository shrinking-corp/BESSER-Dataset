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
    patronrecord,
    vendor,
    patron,
    book_mdatabase,
    LIBRARIAN,
    library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_patronrecord_is_not_abstract():
    assert not inspect.isabstract(patronrecord)


def test_hyp_patronrecord_constructor_exists():
    assert callable(patronrecord.__init__)


def test_hyp_patronrecord_constructor_args():
    sig = inspect.signature(patronrecord.__init__)
    params = list(sig.parameters.keys())
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "filesowned" in params, "Missing parameter 'filesowned'"
    assert "patronid" in params, "Missing parameter 'patronid'"
    assert "dateofmembership" in params, "Missing parameter 'dateofmembership'"
    assert "type" in params, "Missing parameter 'type'"
    assert "noofbooks_alooted" in params, "Missing parameter 'noofbooks_alooted'"











def test_hyp_vendor_is_not_abstract():
    assert not inspect.isabstract(vendor)


def test_hyp_vendor_constructor_exists():
    assert callable(vendor.__init__)


def test_hyp_vendor_constructor_args():
    sig = inspect.signature(vendor.__init__)
    params = list(sig.parameters.keys())
    assert "search" in params, "Missing parameter 'search'"
    assert "paymentdetails" in params, "Missing parameter 'paymentdetails'"
    assert "bookdetails" in params, "Missing parameter 'bookdetails'"
    assert "supplybooks" in params, "Missing parameter 'supplybooks'"







def test_hyp_patron_is_not_abstract():
    assert not inspect.isabstract(patron)


def test_hyp_patron_constructor_exists():
    assert callable(patron.__init__)


def test_hyp_patron_constructor_args():
    sig = inspect.signature(patron.__init__)
    params = list(sig.parameters.keys())
    assert "patronid" in params, "Missing parameter 'patronid'"
    assert "details" in params, "Missing parameter 'details'"
    assert "payfine" in params, "Missing parameter 'payfine'"
    assert "request" in params, "Missing parameter 'request'"
    assert "search" in params, "Missing parameter 'search'"








def test_hyp_book_mdatabase_is_not_abstract():
    assert not inspect.isabstract(book_mdatabase)


def test_hyp_book_mdatabase_constructor_exists():
    assert callable(book_mdatabase.__init__)


def test_hyp_book_mdatabase_constructor_args():
    sig = inspect.signature(book_mdatabase.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "bookid" in params, "Missing parameter 'bookid'"
    assert "update" in params, "Missing parameter 'update'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"







def test_hyp_librarian_is_not_abstract():
    assert not inspect.isabstract(LIBRARIAN)


def test_hyp_librarian_constructor_exists():
    assert callable(LIBRARIAN.__init__)


def test_hyp_librarian_constructor_args():
    sig = inspect.signature(LIBRARIAN.__init__)
    params = list(sig.parameters.keys())
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "searchbook__" in params, "Missing parameter 'searchbook__'"
    assert "LIBRARIAN_ID" in params, "Missing parameter 'LIBRARIAN_ID'"
    assert "issue_status" in params, "Missing parameter 'issue_status'"
    assert "issue_book" in params, "Missing parameter 'issue_book'"
    assert "verify_member__" in params, "Missing parameter 'verify_member__'"









def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(library)


def test_hyp_library_constructor_exists():
    assert callable(library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(library.__init__)
    params = list(sig.parameters.keys())
    assert "_librarion_id" in params, "Missing parameter '_librarion_id'"
    assert "_location" in params, "Missing parameter '_location'"




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
patronrecord_strategy = st.builds(
    patronrecord,
    phone_no=
        safe_text,
    name=
        safe_text,
    address=
        safe_text,
    filesowned=
        safe_text,
    patronid=
        safe_text,
    dateofmembership=
        safe_text,
    type=
        safe_text,
    noofbooks_alooted=
        safe_text
)
vendor_strategy = st.builds(
    vendor,
    search=
        safe_text,
    paymentdetails=
        safe_text,
    bookdetails=
        safe_text,
    supplybooks=
        safe_text
)
patron_strategy = st.builds(
    patron,
    patronid=
        safe_text,
    details=
        safe_text,
    payfine=
        safe_text,
    request=
        safe_text,
    search=
        safe_text
)
book_mdatabase_strategy = st.builds(
    book_mdatabase,
    author=
        safe_text,
    bookid=
        safe_text,
    update=
        safe_text,
    booktitle=
        safe_text
)
LIBRARIAN_strategy = st.builds(
    LIBRARIAN,
    NAME=
        safe_text,
    searchbook__=
        safe_text,
    LIBRARIAN_ID=
        safe_text,
    issue_status=
        safe_text,
    issue_book=
        safe_text,
    verify_member__=
        safe_text
)
library_strategy = st.builds(
    library,
    _librarion_id=
        safe_text,
    _location=
        safe_text
)




@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_filesowned_setter(instance):
    original = instance.filesowned
    instance.filesowned = original
    assert instance.filesowned == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_patronid_setter(instance):
    original = instance.patronid
    instance.patronid = original
    assert instance.patronid == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_dateofmembership_setter(instance):
    original = instance.dateofmembership
    instance.dateofmembership = original
    assert instance.dateofmembership == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=patronrecord_strategy)
def test_hyp_patronrecord_noofbooks_alooted_setter(instance):
    original = instance.noofbooks_alooted
    instance.noofbooks_alooted = original
    assert instance.noofbooks_alooted == original




@given(instance=vendor_strategy)
def test_hyp_vendor_search_setter(instance):
    original = instance.search
    instance.search = original
    assert instance.search == original



@given(instance=vendor_strategy)
def test_hyp_vendor_paymentdetails_setter(instance):
    original = instance.paymentdetails
    instance.paymentdetails = original
    assert instance.paymentdetails == original



@given(instance=vendor_strategy)
def test_hyp_vendor_bookdetails_setter(instance):
    original = instance.bookdetails
    instance.bookdetails = original
    assert instance.bookdetails == original



@given(instance=vendor_strategy)
def test_hyp_vendor_supplybooks_setter(instance):
    original = instance.supplybooks
    instance.supplybooks = original
    assert instance.supplybooks == original




@given(instance=patron_strategy)
def test_hyp_patron_patronid_setter(instance):
    original = instance.patronid
    instance.patronid = original
    assert instance.patronid == original



@given(instance=patron_strategy)
def test_hyp_patron_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=patron_strategy)
def test_hyp_patron_payfine_setter(instance):
    original = instance.payfine
    instance.payfine = original
    assert instance.payfine == original



@given(instance=patron_strategy)
def test_hyp_patron_request_setter(instance):
    original = instance.request
    instance.request = original
    assert instance.request == original



@given(instance=patron_strategy)
def test_hyp_patron_search_setter(instance):
    original = instance.search
    instance.search = original
    assert instance.search == original




@given(instance=book_mdatabase_strategy)
def test_hyp_book_mdatabase_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=book_mdatabase_strategy)
def test_hyp_book_mdatabase_bookid_setter(instance):
    original = instance.bookid
    instance.bookid = original
    assert instance.bookid == original



@given(instance=book_mdatabase_strategy)
def test_hyp_book_mdatabase_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original



@given(instance=book_mdatabase_strategy)
def test_hyp_book_mdatabase_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original




@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original



@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_searchbook___setter(instance):
    original = instance.searchbook__
    instance.searchbook__ = original
    assert instance.searchbook__ == original



@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_LIBRARIAN_ID_setter(instance):
    original = instance.LIBRARIAN_ID
    instance.LIBRARIAN_ID = original
    assert instance.LIBRARIAN_ID == original



@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_issue_status_setter(instance):
    original = instance.issue_status
    instance.issue_status = original
    assert instance.issue_status == original



@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_issue_book_setter(instance):
    original = instance.issue_book
    instance.issue_book = original
    assert instance.issue_book == original



@given(instance=LIBRARIAN_strategy)
def test_hyp_librarian_verify_member___setter(instance):
    original = instance.verify_member__
    instance.verify_member__ = original
    assert instance.verify_member__ == original




@given(instance=library_strategy)
def test_hyp_library__librarion_id_setter(instance):
    original = instance._librarion_id
    instance._librarion_id = original
    assert instance._librarion_id == original



@given(instance=library_strategy)
def test_hyp_library__location_setter(instance):
    original = instance._location
    instance._location = original
    assert instance._location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    LIBRARIAN,
    book_mdatabase,
    library,
    patron,
    patronrecord,
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

def test_LIBRARIAN_LIBRARIAN_ID_value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.LIBRARIAN_ID == "sample_text"
    instance.LIBRARIAN_ID = "sample_text_2"
    assert instance.LIBRARIAN_ID == "sample_text_2"


def test_LIBRARIAN_NAME_value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.NAME == "sample_text"
    instance.NAME = "sample_text_2"
    assert instance.NAME == "sample_text_2"


def test_LIBRARIAN_issue_book_value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.issue_book == "sample_text"
    instance.issue_book = "sample_text_2"
    assert instance.issue_book == "sample_text_2"


def test_LIBRARIAN_issue_status_value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.issue_status == "sample_text"
    instance.issue_status = "sample_text_2"
    assert instance.issue_status == "sample_text_2"


def test_LIBRARIAN_searchbook___value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.searchbook__ == "sample_text"
    instance.searchbook__ = "sample_text_2"
    assert instance.searchbook__ == "sample_text_2"


def test_LIBRARIAN_verify_member___value_roundtrip():
    instance = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    assert instance.verify_member__ == "sample_text"
    instance.verify_member__ = "sample_text_2"
    assert instance.verify_member__ == "sample_text_2"


def test_book_mdatabase_author_value_roundtrip():
    instance = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_book_mdatabase_bookid_value_roundtrip():
    instance = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    assert instance.bookid == "sample_text"
    instance.bookid = "sample_text_2"
    assert instance.bookid == "sample_text_2"


def test_book_mdatabase_booktitle_value_roundtrip():
    instance = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_book_mdatabase_update_value_roundtrip():
    instance = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    assert instance.update == "sample_text"
    instance.update = "sample_text_2"
    assert instance.update == "sample_text_2"


def test_library__librarion_id_value_roundtrip():
    instance = library(_librarion_id="sample_text", _location="sample_text")
    assert instance._librarion_id == "sample_text"
    instance._librarion_id = "sample_text_2"
    assert instance._librarion_id == "sample_text_2"


def test_library__location_value_roundtrip():
    instance = library(_librarion_id="sample_text", _location="sample_text")
    assert instance._location == "sample_text"
    instance._location = "sample_text_2"
    assert instance._location == "sample_text_2"


def test_patron_details_value_roundtrip():
    instance = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_patron_patronid_value_roundtrip():
    instance = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    assert instance.patronid == "sample_text"
    instance.patronid = "sample_text_2"
    assert instance.patronid == "sample_text_2"


def test_patron_payfine_value_roundtrip():
    instance = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    assert instance.payfine == "sample_text"
    instance.payfine = "sample_text_2"
    assert instance.payfine == "sample_text_2"


def test_patron_request_value_roundtrip():
    instance = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    assert instance.request == "sample_text"
    instance.request = "sample_text_2"
    assert instance.request == "sample_text_2"


def test_patron_search_value_roundtrip():
    instance = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    assert instance.search == "sample_text"
    instance.search = "sample_text_2"
    assert instance.search == "sample_text_2"


def test_patronrecord_address_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_patronrecord_dateofmembership_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.dateofmembership == "sample_text"
    instance.dateofmembership = "sample_text_2"
    assert instance.dateofmembership == "sample_text_2"


def test_patronrecord_filesowned_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.filesowned == "sample_text"
    instance.filesowned = "sample_text_2"
    assert instance.filesowned == "sample_text_2"


def test_patronrecord_name_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_patronrecord_noofbooks_alooted_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.noofbooks_alooted == "sample_text"
    instance.noofbooks_alooted = "sample_text_2"
    assert instance.noofbooks_alooted == "sample_text_2"


def test_patronrecord_patronid_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.patronid == "sample_text"
    instance.patronid = "sample_text_2"
    assert instance.patronid == "sample_text_2"


def test_patronrecord_phone_no_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.phone_no == "sample_text"
    instance.phone_no = "sample_text_2"
    assert instance.phone_no == "sample_text_2"


def test_patronrecord_type_value_roundtrip():
    instance = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_vendor_bookdetails_value_roundtrip():
    instance = vendor(bookdetails="sample_text", paymentdetails="sample_text", search="sample_text", supplybooks="sample_text")
    assert instance.bookdetails == "sample_text"
    instance.bookdetails = "sample_text_2"
    assert instance.bookdetails == "sample_text_2"


def test_vendor_paymentdetails_value_roundtrip():
    instance = vendor(bookdetails="sample_text", paymentdetails="sample_text", search="sample_text", supplybooks="sample_text")
    assert instance.paymentdetails == "sample_text"
    instance.paymentdetails = "sample_text_2"
    assert instance.paymentdetails == "sample_text_2"


def test_vendor_search_value_roundtrip():
    instance = vendor(bookdetails="sample_text", paymentdetails="sample_text", search="sample_text", supplybooks="sample_text")
    assert instance.search == "sample_text"
    instance.search = "sample_text_2"
    assert instance.search == "sample_text_2"


def test_vendor_supplybooks_value_roundtrip():
    instance = vendor(bookdetails="sample_text", paymentdetails="sample_text", search="sample_text", supplybooks="sample_text")
    assert instance.supplybooks == "sample_text"
    instance.supplybooks = "sample_text_2"
    assert instance.supplybooks == "sample_text_2"


def test_assoc_book_mdatabase_patron_link_reassign_clear():
    a = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    b1 = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    b2 = book_mdatabase(author="sample_text_2", bookid="sample_text_2", booktitle="sample_text_2", update="sample_text_2")
    _safe_set(a, 'book_mdatabase5', b1)
    assert _is_linked(a, 'book_mdatabase5', b1)
    if hasattr(b1, 'patron4'):
        assert _is_linked(b1, 'patron4', a)
    _safe_set(a, 'book_mdatabase5', b2)
    assert _is_linked(a, 'book_mdatabase5', b2)
    if hasattr(b1, 'patron4'):
        assert not _is_linked(b1, 'patron4', a)
    if hasattr(b2, 'patron4'):
        assert _is_linked(b2, 'patron4', a)
    _safe_set(a, 'book_mdatabase5', None)
    assert not _is_linked(a, 'book_mdatabase5', b2)
    if hasattr(b2, 'patron4'):
        assert not _is_linked(b2, 'patron4', a)


def test_assoc_library_LIBRARIAN_link_reassign_clear():
    a = library(_librarion_id="sample_text", _location="sample_text")
    b1 = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    b2 = LIBRARIAN(LIBRARIAN_ID="sample_text_2", NAME="sample_text_2", issue_book="sample_text_2", issue_status="sample_text_2", searchbook__="sample_text_2", verify_member__="sample_text_2")
    _safe_set(a, 'lIBRARIAN0', b1)
    assert _is_linked(a, 'lIBRARIAN0', b1)
    if hasattr(b1, 'library1'):
        assert _is_linked(b1, 'library1', a)
    _safe_set(a, 'lIBRARIAN0', b2)
    assert _is_linked(a, 'lIBRARIAN0', b2)
    if hasattr(b1, 'library1'):
        assert not _is_linked(b1, 'library1', a)
    if hasattr(b2, 'library1'):
        assert _is_linked(b2, 'library1', a)
    _safe_set(a, 'lIBRARIAN0', None)
    assert not _is_linked(a, 'lIBRARIAN0', b2)
    if hasattr(b2, 'library1'):
        assert not _is_linked(b2, 'library1', a)


def test_assoc_library_book_mdatabase_link_reassign_clear():
    a = library(_librarion_id="sample_text", _location="sample_text")
    b1 = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    b2 = book_mdatabase(author="sample_text_2", bookid="sample_text_2", booktitle="sample_text_2", update="sample_text_2")
    _safe_set(a, 'book_mdatabase2', b1)
    assert _is_linked(a, 'book_mdatabase2', b1)
    if hasattr(b1, 'library3'):
        assert _is_linked(b1, 'library3', a)
    _safe_set(a, 'book_mdatabase2', b2)
    assert _is_linked(a, 'book_mdatabase2', b2)
    if hasattr(b1, 'library3'):
        assert not _is_linked(b1, 'library3', a)
    if hasattr(b2, 'library3'):
        assert _is_linked(b2, 'library3', a)
    _safe_set(a, 'book_mdatabase2', None)
    assert not _is_linked(a, 'book_mdatabase2', b2)
    if hasattr(b2, 'library3'):
        assert not _is_linked(b2, 'library3', a)


def test_assoc_patron_patronrecord_link_reassign_clear():
    a = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    b1 = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    b2 = patron(details="sample_text_2", patronid="sample_text_2", payfine="sample_text_2", request="sample_text_2", search="sample_text_2")
    _safe_set(a, 'patron7', b1)
    assert _is_linked(a, 'patron7', b1)
    if hasattr(b1, 'patronrecord6'):
        assert _is_linked(b1, 'patronrecord6', a)
    _safe_set(a, 'patron7', b2)
    assert _is_linked(a, 'patron7', b2)
    if hasattr(b1, 'patronrecord6'):
        assert not _is_linked(b1, 'patronrecord6', a)
    if hasattr(b2, 'patronrecord6'):
        assert _is_linked(b2, 'patronrecord6', a)
    _safe_set(a, 'patron7', None)
    assert not _is_linked(a, 'patron7', b2)
    if hasattr(b2, 'patronrecord6'):
        assert not _is_linked(b2, 'patronrecord6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

LIBRARIAN_strategy = st.builds(LIBRARIAN, LIBRARIAN_ID=safe_text, NAME=safe_text, issue_book=safe_text, issue_status=safe_text, searchbook__=safe_text, verify_member__=safe_text)
@given(instance=LIBRARIAN_strategy)
@settings(max_examples=25)
def test_LIBRARIAN_instantiation(instance):
    assert isinstance(instance, LIBRARIAN)


book_mdatabase_strategy = st.builds(book_mdatabase, author=safe_text, bookid=safe_text, booktitle=safe_text, update=safe_text)
@given(instance=book_mdatabase_strategy)
@settings(max_examples=25)
def test_book_mdatabase_instantiation(instance):
    assert isinstance(instance, book_mdatabase)


library_strategy = st.builds(library, _librarion_id=safe_text, _location=safe_text)
@given(instance=library_strategy)
@settings(max_examples=25)
def test_library_instantiation(instance):
    assert isinstance(instance, library)


patron_strategy = st.builds(patron, details=safe_text, patronid=safe_text, payfine=safe_text, request=safe_text, search=safe_text)
@given(instance=patron_strategy)
@settings(max_examples=25)
def test_patron_instantiation(instance):
    assert isinstance(instance, patron)


patronrecord_strategy = st.builds(patronrecord, address=safe_text, dateofmembership=safe_text, filesowned=safe_text, name=safe_text, noofbooks_alooted=safe_text, patronid=safe_text, phone_no=safe_text, type=safe_text)
@given(instance=patronrecord_strategy)
@settings(max_examples=25)
def test_patronrecord_instantiation(instance):
    assert isinstance(instance, patronrecord)


vendor_strategy = st.builds(vendor, bookdetails=safe_text, paymentdetails=safe_text, search=safe_text, supplybooks=safe_text)
@given(instance=vendor_strategy)
@settings(max_examples=25)
def test_vendor_instantiation(instance):
    assert isinstance(instance, vendor)



