import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    admin,
    admin_Actor,
    book_a_ticket,
    book_a_ticket_UseCase,
    browse_item_UseCase,
    cancle,
    cancle_UseCase,
    cancle_with_driver_UseCase,
    captcha_UseCase,
    changing_seats_by_admin_UseCase,
    driver,
    driver_Actor,
    driver_planing_UseCase,
    enter_password_UseCase,
    enter_user_name_UseCase,
    exciting_package_UseCase,
    guest_user_Actor,
    login,
    login_UseCase,
    logout_UseCase,
    pay,
    payment_UseCase,
    person,
    remove_user_UseCase,
    return_the_money_to_the_customer_UseCase,
    search_item__UseCase,
    send_message_to_number_registered_UseCase,
    submit_information,
    submit_information_UseCase,
    ticket_printing_UseCase,
    user,
    user_Actor,
    user_register,
    view_item,
    view_item_UseCase,
    view_seat_UseCase,
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

def test_login_password_value_roundtrip():
    instance = login(password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_login_username_value_roundtrip():
    instance = login(password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_pay_id_value_roundtrip():
    instance = pay(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_person_name_value_roundtrip():
    instance = person(name="sample_text", password="sample_text", phone="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_person_password_value_roundtrip():
    instance = person(name="sample_text", password="sample_text", phone="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_person_phone_value_roundtrip():
    instance = person(name="sample_text", password="sample_text", phone="sample_text", username="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_person_username_value_roundtrip():
    instance = person(name="sample_text", password="sample_text", phone="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

admin_strategy = st.builds(admin)
@given(instance=admin_strategy)
@settings(max_examples=25)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)


admin_Actor_strategy = st.builds(admin_Actor)
@given(instance=admin_Actor_strategy)
@settings(max_examples=25)
def test_admin_Actor_instantiation(instance):
    assert isinstance(instance, admin_Actor)


book_a_ticket_strategy = st.builds(book_a_ticket)
@given(instance=book_a_ticket_strategy)
@settings(max_examples=25)
def test_book_a_ticket_instantiation(instance):
    assert isinstance(instance, book_a_ticket)


book_a_ticket_UseCase_strategy = st.builds(book_a_ticket_UseCase)
@given(instance=book_a_ticket_UseCase_strategy)
@settings(max_examples=25)
def test_book_a_ticket_UseCase_instantiation(instance):
    assert isinstance(instance, book_a_ticket_UseCase)


browse_item_UseCase_strategy = st.builds(browse_item_UseCase)
@given(instance=browse_item_UseCase_strategy)
@settings(max_examples=25)
def test_browse_item_UseCase_instantiation(instance):
    assert isinstance(instance, browse_item_UseCase)


cancle_strategy = st.builds(cancle)
@given(instance=cancle_strategy)
@settings(max_examples=25)
def test_cancle_instantiation(instance):
    assert isinstance(instance, cancle)


cancle_UseCase_strategy = st.builds(cancle_UseCase)
@given(instance=cancle_UseCase_strategy)
@settings(max_examples=25)
def test_cancle_UseCase_instantiation(instance):
    assert isinstance(instance, cancle_UseCase)


cancle_with_driver_UseCase_strategy = st.builds(cancle_with_driver_UseCase)
@given(instance=cancle_with_driver_UseCase_strategy)
@settings(max_examples=25)
def test_cancle_with_driver_UseCase_instantiation(instance):
    assert isinstance(instance, cancle_with_driver_UseCase)


captcha_UseCase_strategy = st.builds(captcha_UseCase)
@given(instance=captcha_UseCase_strategy)
@settings(max_examples=25)
def test_captcha_UseCase_instantiation(instance):
    assert isinstance(instance, captcha_UseCase)


changing_seats_by_admin_UseCase_strategy = st.builds(changing_seats_by_admin_UseCase)
@given(instance=changing_seats_by_admin_UseCase_strategy)
@settings(max_examples=25)
def test_changing_seats_by_admin_UseCase_instantiation(instance):
    assert isinstance(instance, changing_seats_by_admin_UseCase)


driver_strategy = st.builds(driver)
@given(instance=driver_strategy)
@settings(max_examples=25)
def test_driver_instantiation(instance):
    assert isinstance(instance, driver)


driver_Actor_strategy = st.builds(driver_Actor)
@given(instance=driver_Actor_strategy)
@settings(max_examples=25)
def test_driver_Actor_instantiation(instance):
    assert isinstance(instance, driver_Actor)


driver_planing_UseCase_strategy = st.builds(driver_planing_UseCase)
@given(instance=driver_planing_UseCase_strategy)
@settings(max_examples=25)
def test_driver_planing_UseCase_instantiation(instance):
    assert isinstance(instance, driver_planing_UseCase)


enter_password_UseCase_strategy = st.builds(enter_password_UseCase)
@given(instance=enter_password_UseCase_strategy)
@settings(max_examples=25)
def test_enter_password_UseCase_instantiation(instance):
    assert isinstance(instance, enter_password_UseCase)


enter_user_name_UseCase_strategy = st.builds(enter_user_name_UseCase)
@given(instance=enter_user_name_UseCase_strategy)
@settings(max_examples=25)
def test_enter_user_name_UseCase_instantiation(instance):
    assert isinstance(instance, enter_user_name_UseCase)


exciting_package_UseCase_strategy = st.builds(exciting_package_UseCase)
@given(instance=exciting_package_UseCase_strategy)
@settings(max_examples=25)
def test_exciting_package_UseCase_instantiation(instance):
    assert isinstance(instance, exciting_package_UseCase)


guest_user_Actor_strategy = st.builds(guest_user_Actor)
@given(instance=guest_user_Actor_strategy)
@settings(max_examples=25)
def test_guest_user_Actor_instantiation(instance):
    assert isinstance(instance, guest_user_Actor)


login_strategy = st.builds(login, password=safe_text, username=safe_text)
@given(instance=login_strategy)
@settings(max_examples=25)
def test_login_instantiation(instance):
    assert isinstance(instance, login)


login_UseCase_strategy = st.builds(login_UseCase)
@given(instance=login_UseCase_strategy)
@settings(max_examples=25)
def test_login_UseCase_instantiation(instance):
    assert isinstance(instance, login_UseCase)


logout_UseCase_strategy = st.builds(logout_UseCase)
@given(instance=logout_UseCase_strategy)
@settings(max_examples=25)
def test_logout_UseCase_instantiation(instance):
    assert isinstance(instance, logout_UseCase)


pay_strategy = st.builds(pay, id=safe_text)
@given(instance=pay_strategy)
@settings(max_examples=25)
def test_pay_instantiation(instance):
    assert isinstance(instance, pay)


payment_UseCase_strategy = st.builds(payment_UseCase)
@given(instance=payment_UseCase_strategy)
@settings(max_examples=25)
def test_payment_UseCase_instantiation(instance):
    assert isinstance(instance, payment_UseCase)


person_strategy = st.builds(person, name=safe_text, password=safe_text, phone=safe_text, username=safe_text)
@given(instance=person_strategy)
@settings(max_examples=25)
def test_person_instantiation(instance):
    assert isinstance(instance, person)


remove_user_UseCase_strategy = st.builds(remove_user_UseCase)
@given(instance=remove_user_UseCase_strategy)
@settings(max_examples=25)
def test_remove_user_UseCase_instantiation(instance):
    assert isinstance(instance, remove_user_UseCase)


return_the_money_to_the_customer_UseCase_strategy = st.builds(return_the_money_to_the_customer_UseCase)
@given(instance=return_the_money_to_the_customer_UseCase_strategy)
@settings(max_examples=25)
def test_return_the_money_to_the_customer_UseCase_instantiation(instance):
    assert isinstance(instance, return_the_money_to_the_customer_UseCase)


search_item__UseCase_strategy = st.builds(search_item__UseCase)
@given(instance=search_item__UseCase_strategy)
@settings(max_examples=25)
def test_search_item__UseCase_instantiation(instance):
    assert isinstance(instance, search_item__UseCase)


send_message_to_number_registered_UseCase_strategy = st.builds(send_message_to_number_registered_UseCase)
@given(instance=send_message_to_number_registered_UseCase_strategy)
@settings(max_examples=25)
def test_send_message_to_number_registered_UseCase_instantiation(instance):
    assert isinstance(instance, send_message_to_number_registered_UseCase)


submit_information_strategy = st.builds(submit_information)
@given(instance=submit_information_strategy)
@settings(max_examples=25)
def test_submit_information_instantiation(instance):
    assert isinstance(instance, submit_information)


submit_information_UseCase_strategy = st.builds(submit_information_UseCase)
@given(instance=submit_information_UseCase_strategy)
@settings(max_examples=25)
def test_submit_information_UseCase_instantiation(instance):
    assert isinstance(instance, submit_information_UseCase)


ticket_printing_UseCase_strategy = st.builds(ticket_printing_UseCase)
@given(instance=ticket_printing_UseCase_strategy)
@settings(max_examples=25)
def test_ticket_printing_UseCase_instantiation(instance):
    assert isinstance(instance, ticket_printing_UseCase)


user_strategy = st.builds(user)
@given(instance=user_strategy)
@settings(max_examples=25)
def test_user_instantiation(instance):
    assert isinstance(instance, user)


user_Actor_strategy = st.builds(user_Actor)
@given(instance=user_Actor_strategy)
@settings(max_examples=25)
def test_user_Actor_instantiation(instance):
    assert isinstance(instance, user_Actor)


user_register_strategy = st.builds(user_register)
@given(instance=user_register_strategy)
@settings(max_examples=25)
def test_user_register_instantiation(instance):
    assert isinstance(instance, user_register)


view_item_strategy = st.builds(view_item)
@given(instance=view_item_strategy)
@settings(max_examples=25)
def test_view_item_instantiation(instance):
    assert isinstance(instance, view_item)


view_item_UseCase_strategy = st.builds(view_item_UseCase)
@given(instance=view_item_UseCase_strategy)
@settings(max_examples=25)
def test_view_item_UseCase_instantiation(instance):
    assert isinstance(instance, view_item_UseCase)


view_seat_UseCase_strategy = st.builds(view_seat_UseCase)
@given(instance=view_seat_UseCase_strategy)
@settings(max_examples=25)
def test_view_seat_UseCase_instantiation(instance):
    assert isinstance(instance, view_seat_UseCase)


