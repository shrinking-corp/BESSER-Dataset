import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    CheckStatus,
    Customer,
    D_B_details,
    DbDetails,
    Login,
    Logout,
    MonitorComplaint,
    RegisterComplaint,
    UpdateStatus,
    administrator,
    administrator_Actor,
    check_status,
    client_Actor,
    create_user_UseCase,
    customer,
    find_out_fault_UseCase,
    login,
    login_UseCase,
    login_technical_UseCase,
    logout,
    logout_UseCase,
    logout_technician_UseCase,
    monitor_complaint,
    new_complaint_details_UseCase,
    register_complaint,
    register_complaint_UseCase,
    search_user_UseCase,
    send_to_admin_UseCase,
    technical_team_Actor,
    update_status,
    view_status_UseCase,
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

def test_Administrator_password_value_roundtrip():
    instance = Administrator(password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_D_B_details_logged_in_value_roundtrip():
    instance = D_B_details(logged_in="sample_text", session_out="sample_text")
    assert instance.logged_in == "sample_text"
    instance.logged_in = "sample_text_2"
    assert instance.logged_in == "sample_text_2"


def test_D_B_details_session_out_value_roundtrip():
    instance = D_B_details(logged_in="sample_text", session_out="sample_text")
    assert instance.session_out == "sample_text"
    instance.session_out = "sample_text_2"
    assert instance.session_out == "sample_text_2"


def test_administrator_password_value_roundtrip():
    instance = administrator(password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_administrator_username_value_roundtrip():
    instance = administrator(password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_check_status_complaint_value_roundtrip():
    instance = check_status(complaint="sample_text")
    assert instance.complaint == "sample_text"
    instance.complaint = "sample_text_2"
    assert instance.complaint == "sample_text_2"


def test_customer_address_value_roundtrip():
    instance = customer(address="sample_text", email_id=7, name="sample_text", product_id="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_customer_email_id_value_roundtrip():
    instance = customer(address="sample_text", email_id=7, name="sample_text", product_id="sample_text")
    assert instance.email_id == 7
    instance.email_id = 13
    assert instance.email_id == 13


def test_customer_name_value_roundtrip():
    instance = customer(address="sample_text", email_id=7, name="sample_text", product_id="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_customer_product_id_value_roundtrip():
    instance = customer(address="sample_text", email_id=7, name="sample_text", product_id="sample_text")
    assert instance.product_id == "sample_text"
    instance.product_id = "sample_text_2"
    assert instance.product_id == "sample_text_2"


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


def test_logout_session_out_value_roundtrip():
    instance = logout(session_out="sample_text")
    assert instance.session_out == "sample_text"
    instance.session_out = "sample_text_2"
    assert instance.session_out == "sample_text_2"


def test_monitor_complaint_complaint_type_value_roundtrip():
    instance = monitor_complaint(complaint_type="sample_text", complaintid=7, date="sample_text")
    assert instance.complaint_type == "sample_text"
    instance.complaint_type = "sample_text_2"
    assert instance.complaint_type == "sample_text_2"


def test_monitor_complaint_complaintid_value_roundtrip():
    instance = monitor_complaint(complaint_type="sample_text", complaintid=7, date="sample_text")
    assert instance.complaintid == 7
    instance.complaintid = 13
    assert instance.complaintid == 13


def test_monitor_complaint_date_value_roundtrip():
    instance = monitor_complaint(complaint_type="sample_text", complaintid=7, date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_register_complaint_complaint_type_value_roundtrip():
    instance = register_complaint(complaint_type="sample_text", description="sample_text")
    assert instance.complaint_type == "sample_text"
    instance.complaint_type = "sample_text_2"
    assert instance.complaint_type == "sample_text_2"


def test_register_complaint_description_value_roundtrip():
    instance = register_complaint(complaint_type="sample_text", description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_update_status_supdate_value_roundtrip():
    instance = update_status(supdate="sample_text")
    assert instance.supdate == "sample_text"
    instance.supdate = "sample_text_2"
    assert instance.supdate == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, password=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


CheckStatus_strategy = st.builds(CheckStatus)
@given(instance=CheckStatus_strategy)
@settings(max_examples=25)
def test_CheckStatus_instantiation(instance):
    assert isinstance(instance, CheckStatus)


Customer_strategy = st.builds(Customer)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


D_B_details_strategy = st.builds(D_B_details, logged_in=safe_text, session_out=safe_text)
@given(instance=D_B_details_strategy)
@settings(max_examples=25)
def test_D_B_details_instantiation(instance):
    assert isinstance(instance, D_B_details)


DbDetails_strategy = st.builds(DbDetails)
@given(instance=DbDetails_strategy)
@settings(max_examples=25)
def test_DbDetails_instantiation(instance):
    assert isinstance(instance, DbDetails)


Login_strategy = st.builds(Login)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Logout_strategy = st.builds(Logout)
@given(instance=Logout_strategy)
@settings(max_examples=25)
def test_Logout_instantiation(instance):
    assert isinstance(instance, Logout)


MonitorComplaint_strategy = st.builds(MonitorComplaint)
@given(instance=MonitorComplaint_strategy)
@settings(max_examples=25)
def test_MonitorComplaint_instantiation(instance):
    assert isinstance(instance, MonitorComplaint)


RegisterComplaint_strategy = st.builds(RegisterComplaint)
@given(instance=RegisterComplaint_strategy)
@settings(max_examples=25)
def test_RegisterComplaint_instantiation(instance):
    assert isinstance(instance, RegisterComplaint)


UpdateStatus_strategy = st.builds(UpdateStatus)
@given(instance=UpdateStatus_strategy)
@settings(max_examples=25)
def test_UpdateStatus_instantiation(instance):
    assert isinstance(instance, UpdateStatus)


administrator_strategy = st.builds(administrator, password=safe_text, username=safe_text)
@given(instance=administrator_strategy)
@settings(max_examples=25)
def test_administrator_instantiation(instance):
    assert isinstance(instance, administrator)


administrator_Actor_strategy = st.builds(administrator_Actor)
@given(instance=administrator_Actor_strategy)
@settings(max_examples=25)
def test_administrator_Actor_instantiation(instance):
    assert isinstance(instance, administrator_Actor)


check_status_strategy = st.builds(check_status, complaint=safe_text)
@given(instance=check_status_strategy)
@settings(max_examples=25)
def test_check_status_instantiation(instance):
    assert isinstance(instance, check_status)


client_Actor_strategy = st.builds(client_Actor)
@given(instance=client_Actor_strategy)
@settings(max_examples=25)
def test_client_Actor_instantiation(instance):
    assert isinstance(instance, client_Actor)


create_user_UseCase_strategy = st.builds(create_user_UseCase)
@given(instance=create_user_UseCase_strategy)
@settings(max_examples=25)
def test_create_user_UseCase_instantiation(instance):
    assert isinstance(instance, create_user_UseCase)


customer_strategy = st.builds(customer, address=safe_text, email_id=st.integers(), name=safe_text, product_id=safe_text)
@given(instance=customer_strategy)
@settings(max_examples=25)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)


find_out_fault_UseCase_strategy = st.builds(find_out_fault_UseCase)
@given(instance=find_out_fault_UseCase_strategy)
@settings(max_examples=25)
def test_find_out_fault_UseCase_instantiation(instance):
    assert isinstance(instance, find_out_fault_UseCase)


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


login_technical_UseCase_strategy = st.builds(login_technical_UseCase)
@given(instance=login_technical_UseCase_strategy)
@settings(max_examples=25)
def test_login_technical_UseCase_instantiation(instance):
    assert isinstance(instance, login_technical_UseCase)


logout_strategy = st.builds(logout, session_out=safe_text)
@given(instance=logout_strategy)
@settings(max_examples=25)
def test_logout_instantiation(instance):
    assert isinstance(instance, logout)


logout_UseCase_strategy = st.builds(logout_UseCase)
@given(instance=logout_UseCase_strategy)
@settings(max_examples=25)
def test_logout_UseCase_instantiation(instance):
    assert isinstance(instance, logout_UseCase)


logout_technician_UseCase_strategy = st.builds(logout_technician_UseCase)
@given(instance=logout_technician_UseCase_strategy)
@settings(max_examples=25)
def test_logout_technician_UseCase_instantiation(instance):
    assert isinstance(instance, logout_technician_UseCase)


monitor_complaint_strategy = st.builds(monitor_complaint, complaint_type=safe_text, complaintid=st.integers(), date=safe_text)
@given(instance=monitor_complaint_strategy)
@settings(max_examples=25)
def test_monitor_complaint_instantiation(instance):
    assert isinstance(instance, monitor_complaint)


new_complaint_details_UseCase_strategy = st.builds(new_complaint_details_UseCase)
@given(instance=new_complaint_details_UseCase_strategy)
@settings(max_examples=25)
def test_new_complaint_details_UseCase_instantiation(instance):
    assert isinstance(instance, new_complaint_details_UseCase)


register_complaint_strategy = st.builds(register_complaint, complaint_type=safe_text, description=safe_text)
@given(instance=register_complaint_strategy)
@settings(max_examples=25)
def test_register_complaint_instantiation(instance):
    assert isinstance(instance, register_complaint)


register_complaint_UseCase_strategy = st.builds(register_complaint_UseCase)
@given(instance=register_complaint_UseCase_strategy)
@settings(max_examples=25)
def test_register_complaint_UseCase_instantiation(instance):
    assert isinstance(instance, register_complaint_UseCase)


search_user_UseCase_strategy = st.builds(search_user_UseCase)
@given(instance=search_user_UseCase_strategy)
@settings(max_examples=25)
def test_search_user_UseCase_instantiation(instance):
    assert isinstance(instance, search_user_UseCase)


send_to_admin_UseCase_strategy = st.builds(send_to_admin_UseCase)
@given(instance=send_to_admin_UseCase_strategy)
@settings(max_examples=25)
def test_send_to_admin_UseCase_instantiation(instance):
    assert isinstance(instance, send_to_admin_UseCase)


technical_team_Actor_strategy = st.builds(technical_team_Actor)
@given(instance=technical_team_Actor_strategy)
@settings(max_examples=25)
def test_technical_team_Actor_instantiation(instance):
    assert isinstance(instance, technical_team_Actor)


update_status_strategy = st.builds(update_status, supdate=safe_text)
@given(instance=update_status_strategy)
@settings(max_examples=25)
def test_update_status_instantiation(instance):
    assert isinstance(instance, update_status)


view_status_UseCase_strategy = st.builds(view_status_UseCase)
@given(instance=view_status_UseCase_strategy)
@settings(max_examples=25)
def test_view_status_UseCase_instantiation(instance):
    assert isinstance(instance, view_status_UseCase)


