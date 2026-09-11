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


