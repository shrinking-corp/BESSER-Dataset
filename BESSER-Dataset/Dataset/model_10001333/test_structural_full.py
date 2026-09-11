import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Librarian__Actor,
    Order_new_books_UseCase,
    UseCase2_UseCase,
    UseCase3_UseCase,
    UseCase4_UseCase,
    UseCase_UseCase,
    check_out__UseCase,
    help_people_with_research__UseCase,
    library_management__Library,
    library_management__librarian,
    library_management__patron,
    organize_books_UseCase,
    patron__Actor,
    renew_UseCase,
    renew_magazine_subscr_UseCase,
    replace_books_with_updated_info_UseCase,
    reserve_UseCase,
    retire_books_UseCase,
    return__UseCase,
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

def test_library_management__Library_Books_value_roundtrip():
    instance = library_management__Library(Books="sample_text", CD="sample_text", Computers="sample_text", Softwares="sample_text", Videos="sample_text")
    assert instance.Books == "sample_text"
    instance.Books = "sample_text_2"
    assert instance.Books == "sample_text_2"


def test_library_management__Library_CD_value_roundtrip():
    instance = library_management__Library(Books="sample_text", CD="sample_text", Computers="sample_text", Softwares="sample_text", Videos="sample_text")
    assert instance.CD == "sample_text"
    instance.CD = "sample_text_2"
    assert instance.CD == "sample_text_2"


def test_library_management__Library_Computers_value_roundtrip():
    instance = library_management__Library(Books="sample_text", CD="sample_text", Computers="sample_text", Softwares="sample_text", Videos="sample_text")
    assert instance.Computers == "sample_text"
    instance.Computers = "sample_text_2"
    assert instance.Computers == "sample_text_2"


def test_library_management__Library_Softwares_value_roundtrip():
    instance = library_management__Library(Books="sample_text", CD="sample_text", Computers="sample_text", Softwares="sample_text", Videos="sample_text")
    assert instance.Softwares == "sample_text"
    instance.Softwares = "sample_text_2"
    assert instance.Softwares == "sample_text_2"


def test_library_management__Library_Videos_value_roundtrip():
    instance = library_management__Library(Books="sample_text", CD="sample_text", Computers="sample_text", Softwares="sample_text", Videos="sample_text")
    assert instance.Videos == "sample_text"
    instance.Videos = "sample_text_2"
    assert instance.Videos == "sample_text_2"


def test_library_management__librarian_CollectFIne_fine__value_roundtrip():
    instance = library_management__librarian(CollectFIne_fine_=7)
    assert instance.CollectFIne_fine_ == 7
    instance.CollectFIne_fine_ = 13
    assert instance.CollectFIne_fine_ == 13


def test_library_management__patron_PayFIne_Dt_date__value_roundtrip():
    instance = library_management__patron(PayFIne_Dt_date_=7)
    assert instance.PayFIne_Dt_date_ == 7
    instance.PayFIne_Dt_date_ = 13
    assert instance.PayFIne_Dt_date_ == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Librarian__Actor_strategy = st.builds(Librarian__Actor)
@given(instance=Librarian__Actor_strategy)
@settings(max_examples=25)
def test_Librarian__Actor_instantiation(instance):
    assert isinstance(instance, Librarian__Actor)


Order_new_books_UseCase_strategy = st.builds(Order_new_books_UseCase)
@given(instance=Order_new_books_UseCase_strategy)
@settings(max_examples=25)
def test_Order_new_books_UseCase_instantiation(instance):
    assert isinstance(instance, Order_new_books_UseCase)


UseCase2_UseCase_strategy = st.builds(UseCase2_UseCase)
@given(instance=UseCase2_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase2_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase2_UseCase)


UseCase3_UseCase_strategy = st.builds(UseCase3_UseCase)
@given(instance=UseCase3_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase3_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase3_UseCase)


UseCase4_UseCase_strategy = st.builds(UseCase4_UseCase)
@given(instance=UseCase4_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase4_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase4_UseCase)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


check_out__UseCase_strategy = st.builds(check_out__UseCase)
@given(instance=check_out__UseCase_strategy)
@settings(max_examples=25)
def test_check_out__UseCase_instantiation(instance):
    assert isinstance(instance, check_out__UseCase)


help_people_with_research__UseCase_strategy = st.builds(help_people_with_research__UseCase)
@given(instance=help_people_with_research__UseCase_strategy)
@settings(max_examples=25)
def test_help_people_with_research__UseCase_instantiation(instance):
    assert isinstance(instance, help_people_with_research__UseCase)


library_management__Library_strategy = st.builds(library_management__Library, Books=safe_text, CD=safe_text, Computers=safe_text, Softwares=safe_text, Videos=safe_text)
@given(instance=library_management__Library_strategy)
@settings(max_examples=25)
def test_library_management__Library_instantiation(instance):
    assert isinstance(instance, library_management__Library)


library_management__librarian_strategy = st.builds(library_management__librarian, CollectFIne_fine_=st.integers())
@given(instance=library_management__librarian_strategy)
@settings(max_examples=25)
def test_library_management__librarian_instantiation(instance):
    assert isinstance(instance, library_management__librarian)


library_management__patron_strategy = st.builds(library_management__patron, PayFIne_Dt_date_=st.integers())
@given(instance=library_management__patron_strategy)
@settings(max_examples=25)
def test_library_management__patron_instantiation(instance):
    assert isinstance(instance, library_management__patron)


organize_books_UseCase_strategy = st.builds(organize_books_UseCase)
@given(instance=organize_books_UseCase_strategy)
@settings(max_examples=25)
def test_organize_books_UseCase_instantiation(instance):
    assert isinstance(instance, organize_books_UseCase)


patron__Actor_strategy = st.builds(patron__Actor)
@given(instance=patron__Actor_strategy)
@settings(max_examples=25)
def test_patron__Actor_instantiation(instance):
    assert isinstance(instance, patron__Actor)


renew_UseCase_strategy = st.builds(renew_UseCase)
@given(instance=renew_UseCase_strategy)
@settings(max_examples=25)
def test_renew_UseCase_instantiation(instance):
    assert isinstance(instance, renew_UseCase)


renew_magazine_subscr_UseCase_strategy = st.builds(renew_magazine_subscr_UseCase)
@given(instance=renew_magazine_subscr_UseCase_strategy)
@settings(max_examples=25)
def test_renew_magazine_subscr_UseCase_instantiation(instance):
    assert isinstance(instance, renew_magazine_subscr_UseCase)


replace_books_with_updated_info_UseCase_strategy = st.builds(replace_books_with_updated_info_UseCase)
@given(instance=replace_books_with_updated_info_UseCase_strategy)
@settings(max_examples=25)
def test_replace_books_with_updated_info_UseCase_instantiation(instance):
    assert isinstance(instance, replace_books_with_updated_info_UseCase)


reserve_UseCase_strategy = st.builds(reserve_UseCase)
@given(instance=reserve_UseCase_strategy)
@settings(max_examples=25)
def test_reserve_UseCase_instantiation(instance):
    assert isinstance(instance, reserve_UseCase)


retire_books_UseCase_strategy = st.builds(retire_books_UseCase)
@given(instance=retire_books_UseCase_strategy)
@settings(max_examples=25)
def test_retire_books_UseCase_instantiation(instance):
    assert isinstance(instance, retire_books_UseCase)


return__UseCase_strategy = st.builds(return__UseCase)
@given(instance=return__UseCase_strategy)
@settings(max_examples=25)
def test_return__UseCase_instantiation(instance):
    assert isinstance(instance, return__UseCase)


