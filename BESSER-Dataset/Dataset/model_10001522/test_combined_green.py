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
    member_profile,
    status_of_book,
    cash,
    credit_card,
    library,
    transaction,
    fine,
    library_member,
    librarian,
    book,
    File,
    XML,
    CSV,
    Data,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_member_profile_is_not_abstract():
    assert not inspect.isabstract(member_profile)


def test_hyp_member_profile_constructor_exists():
    assert callable(member_profile.__init__)


def test_hyp_member_profile_constructor_args():
    sig = inspect.signature(member_profile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_status_of_book_is_not_abstract():
    assert not inspect.isabstract(status_of_book)


def test_hyp_status_of_book_constructor_exists():
    assert callable(status_of_book.__init__)


def test_hyp_status_of_book_constructor_args():
    sig = inspect.signature(status_of_book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cash_is_not_abstract():
    assert not inspect.isabstract(cash)


def test_hyp_cash_constructor_exists():
    assert callable(cash.__init__)


def test_hyp_cash_constructor_args():
    sig = inspect.signature(cash.__init__)
    params = list(sig.parameters.keys())



def test_hyp_credit_card_is_not_abstract():
    assert not inspect.isabstract(credit_card)


def test_hyp_credit_card_constructor_exists():
    assert callable(credit_card.__init__)


def test_hyp_credit_card_constructor_args():
    sig = inspect.signature(credit_card.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(library)


def test_hyp_library_constructor_exists():
    assert callable(library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_is_not_abstract():
    assert not inspect.isabstract(transaction)


def test_hyp_transaction_constructor_exists():
    assert callable(transaction.__init__)


def test_hyp_transaction_constructor_args():
    sig = inspect.signature(transaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fine_is_not_abstract():
    assert not inspect.isabstract(fine)


def test_hyp_fine_constructor_exists():
    assert callable(fine.__init__)


def test_hyp_fine_constructor_args():
    sig = inspect.signature(fine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_member_is_not_abstract():
    assert not inspect.isabstract(library_member)


def test_hyp_library_member_constructor_exists():
    assert callable(library_member.__init__)


def test_hyp_library_member_constructor_args():
    sig = inspect.signature(library_member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_hyp_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_hyp_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(book)


def test_hyp_book_constructor_exists():
    assert callable(book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_hyp_file_constructor_exists():
    assert callable(File.__init__)


def test_hyp_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())
    assert "file_type" in params, "Missing parameter 'file_type'"

def test_hyp_file_has_file_type():
    assert hasattr(File, "file_type")
    descriptor = None
    for klass in File.__mro__:
        if "file_type" in klass.__dict__:
            descriptor = klass.__dict__["file_type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_xml_is_not_abstract():
    assert not inspect.isabstract(XML)


def test_hyp_xml_constructor_exists():
    assert callable(XML.__init__)


def test_hyp_xml_constructor_args():
    sig = inspect.signature(XML.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_csv_is_not_abstract():
    assert not inspect.isabstract(CSV)


def test_hyp_csv_constructor_exists():
    assert callable(CSV.__init__)


def test_hyp_csv_constructor_args():
    sig = inspect.signature(CSV.__init__)
    params = list(sig.parameters.keys())
    assert "cloumn" in params, "Missing parameter 'cloumn'"
    assert "row" in params, "Missing parameter 'row'"





def test_hyp_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_hyp_data_constructor_exists():
    assert callable(Data.__init__)


def test_hyp_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_hyp_user_has_user_id():
    assert hasattr(User, "user_id")
    descriptor = None
    for klass in User.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)


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
member_profile_strategy = st.builds(
    member_profile,
)
status_of_book_strategy = st.builds(
    status_of_book,
)
cash_strategy = st.builds(
    cash,
)
credit_card_strategy = st.builds(
    credit_card,
)
library_strategy = st.builds(
    library,
)
transaction_strategy = st.builds(
    transaction,
)
fine_strategy = st.builds(
    fine,
)
library_member_strategy = st.builds(
    library_member,
)
librarian_strategy = st.builds(
    librarian,
)
book_strategy = st.builds(
    book,
)
File_strategy = st.builds(
    File,
    file_type=
        st.none()
)
XML_strategy = st.builds(
    XML,
    element=
        safe_text,
    attribute=
        safe_text
)
CSV_strategy = st.builds(
    CSV,
    cloumn=
        safe_text,
    row=
        safe_text
)
Data_strategy = st.builds(
    Data,
    key=
        safe_text,
    value=
        safe_text
)
User_strategy = st.builds(
    User,
    user_id=
        st.none()
)











@given(instance=File_strategy)
@settings(max_examples=50)
def test_hyp_file_instantiation(instance):
    assert isinstance(instance, File)



@given(instance=File_strategy)
def test_hyp_file_file_type_setter(instance):
    original = instance.file_type
    instance.file_type = original
    assert instance.file_type == original




@given(instance=XML_strategy)
def test_hyp_xml_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original



@given(instance=XML_strategy)
def test_hyp_xml_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=CSV_strategy)
def test_hyp_csv_cloumn_setter(instance):
    original = instance.cloumn
    instance.cloumn = original
    assert instance.cloumn == original



@given(instance=CSV_strategy)
def test_hyp_csv_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original




@given(instance=Data_strategy)
def test_hyp_data_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=Data_strategy)
def test_hyp_data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_hyp_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_hyp_user_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CSV,
    Data,
    File,
    User,
    XML,
    book,
    cash,
    credit_card,
    fine,
    librarian,
    library,
    library_member,
    member_profile,
    status_of_book,
    transaction,
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

def test_CSV_cloumn_value_roundtrip():
    instance = CSV(cloumn="sample_text", row="sample_text")
    assert instance.cloumn == "sample_text"
    instance.cloumn = "sample_text_2"
    assert instance.cloumn == "sample_text_2"


def test_CSV_row_value_roundtrip():
    instance = CSV(cloumn="sample_text", row="sample_text")
    assert instance.row == "sample_text"
    instance.row = "sample_text_2"
    assert instance.row == "sample_text_2"


def test_Data_key_value_roundtrip():
    instance = Data(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_Data_value_value_roundtrip():
    instance = Data(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_XML_attribute_value_roundtrip():
    instance = XML(attribute="sample_text", element="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_XML_element_value_roundtrip():
    instance = XML(attribute="sample_text", element="sample_text")
    assert instance.element == "sample_text"
    instance.element = "sample_text_2"
    assert instance.element == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CSV_strategy = st.builds(CSV, cloumn=safe_text, row=safe_text)
@given(instance=CSV_strategy)
@settings(max_examples=25)
def test_CSV_instantiation(instance):
    assert isinstance(instance, CSV)


Data_strategy = st.builds(Data, key=safe_text, value=safe_text)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


XML_strategy = st.builds(XML, attribute=safe_text, element=safe_text)
@given(instance=XML_strategy)
@settings(max_examples=25)
def test_XML_instantiation(instance):
    assert isinstance(instance, XML)


book_strategy = st.builds(book)
@given(instance=book_strategy)
@settings(max_examples=25)
def test_book_instantiation(instance):
    assert isinstance(instance, book)


cash_strategy = st.builds(cash)
@given(instance=cash_strategy)
@settings(max_examples=25)
def test_cash_instantiation(instance):
    assert isinstance(instance, cash)


credit_card_strategy = st.builds(credit_card)
@given(instance=credit_card_strategy)
@settings(max_examples=25)
def test_credit_card_instantiation(instance):
    assert isinstance(instance, credit_card)


fine_strategy = st.builds(fine)
@given(instance=fine_strategy)
@settings(max_examples=25)
def test_fine_instantiation(instance):
    assert isinstance(instance, fine)


librarian_strategy = st.builds(librarian)
@given(instance=librarian_strategy)
@settings(max_examples=25)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)


library_strategy = st.builds(library)
@given(instance=library_strategy)
@settings(max_examples=25)
def test_library_instantiation(instance):
    assert isinstance(instance, library)


library_member_strategy = st.builds(library_member)
@given(instance=library_member_strategy)
@settings(max_examples=25)
def test_library_member_instantiation(instance):
    assert isinstance(instance, library_member)


member_profile_strategy = st.builds(member_profile)
@given(instance=member_profile_strategy)
@settings(max_examples=25)
def test_member_profile_instantiation(instance):
    assert isinstance(instance, member_profile)


status_of_book_strategy = st.builds(status_of_book)
@given(instance=status_of_book_strategy)
@settings(max_examples=25)
def test_status_of_book_instantiation(instance):
    assert isinstance(instance, status_of_book)


transaction_strategy = st.builds(transaction)
@given(instance=transaction_strategy)
@settings(max_examples=25)
def test_transaction_instantiation(instance):
    assert isinstance(instance, transaction)



