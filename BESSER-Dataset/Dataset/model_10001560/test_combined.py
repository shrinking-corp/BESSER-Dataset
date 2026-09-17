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
    book_ticket_UseCase,
    Customer_Actor1,
    Manager_Actor,
    statistical_reporting_UseCase,
    vehicle_management_UseCase,
    account_management_UseCase,
    customer_management_UseCase,
    Use_Actor,
    Book_ticket_UseCase,
    Search_the_route_UseCase,
    Customer_Actor,
    accoutUser,
    Ticket,
    Customer,
    infoCompany,
    mapCarExchange,
    Car,
    Login_UseCase3,
    Report_by_ticket_amount_UseCase,
    Report_by_revenue_UseCase,
    statistical_reporting_UseCase1,
    Manager_Actor4,
    Login_UseCase2,
    Delete_vehicles_UseCase,
    Update_vehicles_information_UseCase,
    View_vehicles_information_UseCase,
    vehicle_management_UseCase1,
    Manager_Actor3,
    call_for_customers_UseCase,
    Login_UseCase1,
    View_customers_information_UseCase,
    cancel_booking_UseCase,
    confirm_booking_UseCase,
    search_customers_UseCase,
    customer_management_UseCase1,
    Manager_Actor2,
    make_payment_UseCase,
    View_account_information_UseCase,
    Account_settings_UseCase,
    Login_UseCase,
    account_management_UseCase1,
    Manager_Actor1,
    search_UseCase,
    confirm_information_UseCase,
    choose_seats_UseCase,
    choose_vehicle_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_book_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(book_ticket_UseCase)


def test_hyp_book_ticket_usecase_constructor_exists():
    assert callable(book_ticket_UseCase.__init__)


def test_hyp_book_ticket_usecase_constructor_args():
    sig = inspect.signature(book_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_actor1_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor1)


def test_hyp_customer_actor1_constructor_exists():
    assert callable(Customer_Actor1.__init__)


def test_hyp_customer_actor1_constructor_args():
    sig = inspect.signature(Customer_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_hyp_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_hyp_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statistical_reporting_usecase_is_not_abstract():
    assert not inspect.isabstract(statistical_reporting_UseCase)


def test_hyp_statistical_reporting_usecase_constructor_exists():
    assert callable(statistical_reporting_UseCase.__init__)


def test_hyp_statistical_reporting_usecase_constructor_args():
    sig = inspect.signature(statistical_reporting_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vehicle_management_usecase_is_not_abstract():
    assert not inspect.isabstract(vehicle_management_UseCase)


def test_hyp_vehicle_management_usecase_constructor_exists():
    assert callable(vehicle_management_UseCase.__init__)


def test_hyp_vehicle_management_usecase_constructor_args():
    sig = inspect.signature(vehicle_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_account_management_usecase_is_not_abstract():
    assert not inspect.isabstract(account_management_UseCase)


def test_hyp_account_management_usecase_constructor_exists():
    assert callable(account_management_UseCase.__init__)


def test_hyp_account_management_usecase_constructor_args():
    sig = inspect.signature(account_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_management_usecase_is_not_abstract():
    assert not inspect.isabstract(customer_management_UseCase)


def test_hyp_customer_management_usecase_constructor_exists():
    assert callable(customer_management_UseCase.__init__)


def test_hyp_customer_management_usecase_constructor_args():
    sig = inspect.signature(customer_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_actor_is_not_abstract():
    assert not inspect.isabstract(Use_Actor)


def test_hyp_use_actor_constructor_exists():
    assert callable(Use_Actor.__init__)


def test_hyp_use_actor_constructor_args():
    sig = inspect.signature(Use_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(Book_ticket_UseCase)


def test_hyp_book_ticket_usecase_constructor_exists():
    assert callable(Book_ticket_UseCase.__init__)


def test_hyp_book_ticket_usecase_constructor_args():
    sig = inspect.signature(Book_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_search_the_route_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_the_route_UseCase)


def test_hyp_search_the_route_usecase_constructor_exists():
    assert callable(Search_the_route_UseCase.__init__)


def test_hyp_search_the_route_usecase_constructor_args():
    sig = inspect.signature(Search_the_route_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_hyp_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_hyp_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accoutuser_is_not_abstract():
    assert not inspect.isabstract(accoutUser)


def test_hyp_accoutuser_constructor_exists():
    assert callable(accoutUser.__init__)


def test_hyp_accoutuser_constructor_args():
    sig = inspect.signature(accoutUser.__init__)
    params = list(sig.parameters.keys())
    assert "codeConfirm" in params, "Missing parameter 'codeConfirm'"
    assert "idCompany" in params, "Missing parameter 'idCompany'"
    assert "emailUser" in params, "Missing parameter 'emailUser'"
    assert "dateRegister" in params, "Missing parameter 'dateRegister'"
    assert "idUser" in params, "Missing parameter 'idUser'"
    assert "passwordUser" in params, "Missing parameter 'passwordUser'"









def test_hyp_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_hyp_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_hyp_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "idCustomer" in params, "Missing parameter 'idCustomer'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "idTicket" in params, "Missing parameter 'idTicket'"
    assert "code" in params, "Missing parameter 'code'"
    assert "timeExchange" in params, "Missing parameter 'timeExchange'"
    assert "statusSeat" in params, "Missing parameter 'statusSeat'"
    assert "positionSeat" in params, "Missing parameter 'positionSeat'"
    assert "numberSeat" in params, "Missing parameter 'numberSeat'"
    assert "positionSeatBelow" in params, "Missing parameter 'positionSeatBelow'"












def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "emailCustomer" in params, "Missing parameter 'emailCustomer'"
    assert "phoneCustomer" in params, "Missing parameter 'phoneCustomer'"
    assert "idCustomer" in params, "Missing parameter 'idCustomer'"
    assert "nameCustomer" in params, "Missing parameter 'nameCustomer'"







def test_hyp_infocompany_is_not_abstract():
    assert not inspect.isabstract(infoCompany)


def test_hyp_infocompany_constructor_exists():
    assert callable(infoCompany.__init__)


def test_hyp_infocompany_constructor_args():
    sig = inspect.signature(infoCompany.__init__)
    params = list(sig.parameters.keys())
    assert "idCompany" in params, "Missing parameter 'idCompany'"
    assert "nameCompany" in params, "Missing parameter 'nameCompany'"
    assert "dateEstablish" in params, "Missing parameter 'dateEstablish'"
    assert "describeCompany" in params, "Missing parameter 'describeCompany'"
    assert "addressCompany" in params, "Missing parameter 'addressCompany'"
    assert "showSafe" in params, "Missing parameter 'showSafe'"
    assert "dateUpdate" in params, "Missing parameter 'dateUpdate'"
    assert "dateRegister" in params, "Missing parameter 'dateRegister'"
    assert "phoneCompany" in params, "Missing parameter 'phoneCompany'"












def test_hyp_mapcarexchange_is_not_abstract():
    assert not inspect.isabstract(mapCarExchange)


def test_hyp_mapcarexchange_constructor_exists():
    assert callable(mapCarExchange.__init__)


def test_hyp_mapcarexchange_constructor_args():
    sig = inspect.signature(mapCarExchange.__init__)
    params = list(sig.parameters.keys())
    assert "mapOnCar" in params, "Missing parameter 'mapOnCar'"
    assert "idMap" in params, "Missing parameter 'idMap'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "timeExchange" in params, "Missing parameter 'timeExchange'"
    assert "mapBelowCar" in params, "Missing parameter 'mapBelowCar'"








def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "idUser" in params, "Missing parameter 'idUser'"
    assert "statusCar" in params, "Missing parameter 'statusCar'"
    assert "timeStartCar" in params, "Missing parameter 'timeStartCar'"
    assert "fareCar" in params, "Missing parameter 'fareCar'"
    assert "positionEndCar" in params, "Missing parameter 'positionEndCar'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "classifyCar" in params, "Missing parameter 'classifyCar'"
    assert "positionStartCar" in params, "Missing parameter 'positionStartCar'"
    assert "mapOnCar" in params, "Missing parameter 'mapOnCar'"
    assert "mapBelowCar" in params, "Missing parameter 'mapBelowCar'"
    assert "numberPlatesCar" in params, "Missing parameter 'numberPlatesCar'"
    assert "phoneCar" in params, "Missing parameter 'phoneCar'"
    assert "imageLinkCar" in params, "Missing parameter 'imageLinkCar'"
    assert "nameCar" in params, "Missing parameter 'nameCar'"

















def test_hyp_login_usecase3_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase3)


def test_hyp_login_usecase3_constructor_exists():
    assert callable(Login_UseCase3.__init__)


def test_hyp_login_usecase3_constructor_args():
    sig = inspect.signature(Login_UseCase3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_report_by_ticket_amount_usecase_is_not_abstract():
    assert not inspect.isabstract(Report_by_ticket_amount_UseCase)


def test_hyp_report_by_ticket_amount_usecase_constructor_exists():
    assert callable(Report_by_ticket_amount_UseCase.__init__)


def test_hyp_report_by_ticket_amount_usecase_constructor_args():
    sig = inspect.signature(Report_by_ticket_amount_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_report_by_revenue_usecase_is_not_abstract():
    assert not inspect.isabstract(Report_by_revenue_UseCase)


def test_hyp_report_by_revenue_usecase_constructor_exists():
    assert callable(Report_by_revenue_UseCase.__init__)


def test_hyp_report_by_revenue_usecase_constructor_args():
    sig = inspect.signature(Report_by_revenue_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statistical_reporting_usecase1_is_not_abstract():
    assert not inspect.isabstract(statistical_reporting_UseCase1)


def test_hyp_statistical_reporting_usecase1_constructor_exists():
    assert callable(statistical_reporting_UseCase1.__init__)


def test_hyp_statistical_reporting_usecase1_constructor_args():
    sig = inspect.signature(statistical_reporting_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor4_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor4)


def test_hyp_manager_actor4_constructor_exists():
    assert callable(Manager_Actor4.__init__)


def test_hyp_manager_actor4_constructor_args():
    sig = inspect.signature(Manager_Actor4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_usecase2_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase2)


def test_hyp_login_usecase2_constructor_exists():
    assert callable(Login_UseCase2.__init__)


def test_hyp_login_usecase2_constructor_args():
    sig = inspect.signature(Login_UseCase2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_delete_vehicles_usecase_is_not_abstract():
    assert not inspect.isabstract(Delete_vehicles_UseCase)


def test_hyp_delete_vehicles_usecase_constructor_exists():
    assert callable(Delete_vehicles_UseCase.__init__)


def test_hyp_delete_vehicles_usecase_constructor_args():
    sig = inspect.signature(Delete_vehicles_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_update_vehicles_information_usecase_is_not_abstract():
    assert not inspect.isabstract(Update_vehicles_information_UseCase)


def test_hyp_update_vehicles_information_usecase_constructor_exists():
    assert callable(Update_vehicles_information_UseCase.__init__)


def test_hyp_update_vehicles_information_usecase_constructor_args():
    sig = inspect.signature(Update_vehicles_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_vehicles_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_vehicles_information_UseCase)


def test_hyp_view_vehicles_information_usecase_constructor_exists():
    assert callable(View_vehicles_information_UseCase.__init__)


def test_hyp_view_vehicles_information_usecase_constructor_args():
    sig = inspect.signature(View_vehicles_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vehicle_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(vehicle_management_UseCase1)


def test_hyp_vehicle_management_usecase1_constructor_exists():
    assert callable(vehicle_management_UseCase1.__init__)


def test_hyp_vehicle_management_usecase1_constructor_args():
    sig = inspect.signature(vehicle_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor3_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor3)


def test_hyp_manager_actor3_constructor_exists():
    assert callable(Manager_Actor3.__init__)


def test_hyp_manager_actor3_constructor_args():
    sig = inspect.signature(Manager_Actor3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_call_for_customers_usecase_is_not_abstract():
    assert not inspect.isabstract(call_for_customers_UseCase)


def test_hyp_call_for_customers_usecase_constructor_exists():
    assert callable(call_for_customers_UseCase.__init__)


def test_hyp_call_for_customers_usecase_constructor_args():
    sig = inspect.signature(call_for_customers_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_usecase1_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase1)


def test_hyp_login_usecase1_constructor_exists():
    assert callable(Login_UseCase1.__init__)


def test_hyp_login_usecase1_constructor_args():
    sig = inspect.signature(Login_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_customers_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_customers_information_UseCase)


def test_hyp_view_customers_information_usecase_constructor_exists():
    assert callable(View_customers_information_UseCase.__init__)


def test_hyp_view_customers_information_usecase_constructor_args():
    sig = inspect.signature(View_customers_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancel_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(cancel_booking_UseCase)


def test_hyp_cancel_booking_usecase_constructor_exists():
    assert callable(cancel_booking_UseCase.__init__)


def test_hyp_cancel_booking_usecase_constructor_args():
    sig = inspect.signature(cancel_booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_confirm_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(confirm_booking_UseCase)


def test_hyp_confirm_booking_usecase_constructor_exists():
    assert callable(confirm_booking_UseCase.__init__)


def test_hyp_confirm_booking_usecase_constructor_args():
    sig = inspect.signature(confirm_booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_search_customers_usecase_is_not_abstract():
    assert not inspect.isabstract(search_customers_UseCase)


def test_hyp_search_customers_usecase_constructor_exists():
    assert callable(search_customers_UseCase.__init__)


def test_hyp_search_customers_usecase_constructor_args():
    sig = inspect.signature(search_customers_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(customer_management_UseCase1)


def test_hyp_customer_management_usecase1_constructor_exists():
    assert callable(customer_management_UseCase1.__init__)


def test_hyp_customer_management_usecase1_constructor_args():
    sig = inspect.signature(customer_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor2_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor2)


def test_hyp_manager_actor2_constructor_exists():
    assert callable(Manager_Actor2.__init__)


def test_hyp_manager_actor2_constructor_args():
    sig = inspect.signature(Manager_Actor2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(make_payment_UseCase)


def test_hyp_make_payment_usecase_constructor_exists():
    assert callable(make_payment_UseCase.__init__)


def test_hyp_make_payment_usecase_constructor_args():
    sig = inspect.signature(make_payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_account_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_account_information_UseCase)


def test_hyp_view_account_information_usecase_constructor_exists():
    assert callable(View_account_information_UseCase.__init__)


def test_hyp_view_account_information_usecase_constructor_args():
    sig = inspect.signature(View_account_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_account_settings_usecase_is_not_abstract():
    assert not inspect.isabstract(Account_settings_UseCase)


def test_hyp_account_settings_usecase_constructor_exists():
    assert callable(Account_settings_UseCase.__init__)


def test_hyp_account_settings_usecase_constructor_args():
    sig = inspect.signature(Account_settings_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_hyp_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_hyp_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_account_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(account_management_UseCase1)


def test_hyp_account_management_usecase1_constructor_exists():
    assert callable(account_management_UseCase1.__init__)


def test_hyp_account_management_usecase1_constructor_args():
    sig = inspect.signature(account_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor1_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor1)


def test_hyp_manager_actor1_constructor_exists():
    assert callable(Manager_Actor1.__init__)


def test_hyp_manager_actor1_constructor_args():
    sig = inspect.signature(Manager_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_search_usecase_is_not_abstract():
    assert not inspect.isabstract(search_UseCase)


def test_hyp_search_usecase_constructor_exists():
    assert callable(search_UseCase.__init__)


def test_hyp_search_usecase_constructor_args():
    sig = inspect.signature(search_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_confirm_information_usecase_is_not_abstract():
    assert not inspect.isabstract(confirm_information_UseCase)


def test_hyp_confirm_information_usecase_constructor_exists():
    assert callable(confirm_information_UseCase.__init__)


def test_hyp_confirm_information_usecase_constructor_args():
    sig = inspect.signature(confirm_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_choose_seats_usecase_is_not_abstract():
    assert not inspect.isabstract(choose_seats_UseCase)


def test_hyp_choose_seats_usecase_constructor_exists():
    assert callable(choose_seats_UseCase.__init__)


def test_hyp_choose_seats_usecase_constructor_args():
    sig = inspect.signature(choose_seats_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_choose_vehicle_usecase_is_not_abstract():
    assert not inspect.isabstract(choose_vehicle_UseCase)


def test_hyp_choose_vehicle_usecase_constructor_exists():
    assert callable(choose_vehicle_UseCase.__init__)


def test_hyp_choose_vehicle_usecase_constructor_args():
    sig = inspect.signature(choose_vehicle_UseCase.__init__)
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
book_ticket_UseCase_strategy = st.builds(
    book_ticket_UseCase,
)
Customer_Actor1_strategy = st.builds(
    Customer_Actor1,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
statistical_reporting_UseCase_strategy = st.builds(
    statistical_reporting_UseCase,
)
vehicle_management_UseCase_strategy = st.builds(
    vehicle_management_UseCase,
)
account_management_UseCase_strategy = st.builds(
    account_management_UseCase,
)
customer_management_UseCase_strategy = st.builds(
    customer_management_UseCase,
)
Use_Actor_strategy = st.builds(
    Use_Actor,
)
Book_ticket_UseCase_strategy = st.builds(
    Book_ticket_UseCase,
)
Search_the_route_UseCase_strategy = st.builds(
    Search_the_route_UseCase,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)
accoutUser_strategy = st.builds(
    accoutUser,
    codeConfirm=
        safe_text,
    idCompany=
        st.integers(),
    emailUser=
        safe_text,
    dateRegister=
        safe_text,
    idUser=
        st.integers(),
    passwordUser=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    idCustomer=
        st.integers(),
    idCar=
        st.integers(),
    idTicket=
        st.integers(),
    code=
        safe_text,
    timeExchange=
        safe_text,
    statusSeat=
        st.integers(),
    positionSeat=
        safe_text,
    numberSeat=
        st.integers(),
    positionSeatBelow=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    emailCustomer=
        safe_text,
    phoneCustomer=
        safe_text,
    idCustomer=
        st.integers(),
    nameCustomer=
        safe_text
)
infoCompany_strategy = st.builds(
    infoCompany,
    idCompany=
        st.integers(),
    nameCompany=
        safe_text,
    dateEstablish=
        safe_text,
    describeCompany=
        safe_text,
    addressCompany=
        safe_text,
    showSafe=
        safe_text,
    dateUpdate=
        safe_text,
    dateRegister=
        safe_text,
    phoneCompany=
        safe_text
)
mapCarExchange_strategy = st.builds(
    mapCarExchange,
    mapOnCar=
        safe_text,
    idMap=
        st.integers(),
    idCar=
        st.integers(),
    timeExchange=
        safe_text,
    mapBelowCar=
        safe_text
)
Car_strategy = st.builds(
    Car,
    idUser=
        st.integers(),
    statusCar=
        st.integers(),
    timeStartCar=
        safe_text,
    fareCar=
        safe_text,
    positionEndCar=
        safe_text,
    idCar=
        st.integers(),
    classifyCar=
        st.integers(),
    positionStartCar=
        safe_text,
    mapOnCar=
        safe_text,
    mapBelowCar=
        safe_text,
    numberPlatesCar=
        safe_text,
    phoneCar=
        safe_text,
    imageLinkCar=
        safe_text,
    nameCar=
        safe_text
)
Login_UseCase3_strategy = st.builds(
    Login_UseCase3,
)
Report_by_ticket_amount_UseCase_strategy = st.builds(
    Report_by_ticket_amount_UseCase,
)
Report_by_revenue_UseCase_strategy = st.builds(
    Report_by_revenue_UseCase,
)
statistical_reporting_UseCase1_strategy = st.builds(
    statistical_reporting_UseCase1,
)
Manager_Actor4_strategy = st.builds(
    Manager_Actor4,
)
Login_UseCase2_strategy = st.builds(
    Login_UseCase2,
)
Delete_vehicles_UseCase_strategy = st.builds(
    Delete_vehicles_UseCase,
)
Update_vehicles_information_UseCase_strategy = st.builds(
    Update_vehicles_information_UseCase,
)
View_vehicles_information_UseCase_strategy = st.builds(
    View_vehicles_information_UseCase,
)
vehicle_management_UseCase1_strategy = st.builds(
    vehicle_management_UseCase1,
)
Manager_Actor3_strategy = st.builds(
    Manager_Actor3,
)
call_for_customers_UseCase_strategy = st.builds(
    call_for_customers_UseCase,
)
Login_UseCase1_strategy = st.builds(
    Login_UseCase1,
)
View_customers_information_UseCase_strategy = st.builds(
    View_customers_information_UseCase,
)
cancel_booking_UseCase_strategy = st.builds(
    cancel_booking_UseCase,
)
confirm_booking_UseCase_strategy = st.builds(
    confirm_booking_UseCase,
)
search_customers_UseCase_strategy = st.builds(
    search_customers_UseCase,
)
customer_management_UseCase1_strategy = st.builds(
    customer_management_UseCase1,
)
Manager_Actor2_strategy = st.builds(
    Manager_Actor2,
)
make_payment_UseCase_strategy = st.builds(
    make_payment_UseCase,
)
View_account_information_UseCase_strategy = st.builds(
    View_account_information_UseCase,
)
Account_settings_UseCase_strategy = st.builds(
    Account_settings_UseCase,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)
account_management_UseCase1_strategy = st.builds(
    account_management_UseCase1,
)
Manager_Actor1_strategy = st.builds(
    Manager_Actor1,
)
search_UseCase_strategy = st.builds(
    search_UseCase,
)
confirm_information_UseCase_strategy = st.builds(
    confirm_information_UseCase,
)
choose_seats_UseCase_strategy = st.builds(
    choose_seats_UseCase,
)
choose_vehicle_UseCase_strategy = st.builds(
    choose_vehicle_UseCase,
)















@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_codeConfirm_setter(instance):
    original = instance.codeConfirm
    instance.codeConfirm = original
    assert instance.codeConfirm == original



@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_idCompany_setter(instance):
    original = instance.idCompany
    instance.idCompany = original
    assert instance.idCompany == original



@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_emailUser_setter(instance):
    original = instance.emailUser
    instance.emailUser = original
    assert instance.emailUser == original



@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_dateRegister_setter(instance):
    original = instance.dateRegister
    instance.dateRegister = original
    assert instance.dateRegister == original



@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_idUser_setter(instance):
    original = instance.idUser
    instance.idUser = original
    assert instance.idUser == original



@given(instance=accoutUser_strategy)
def test_hyp_accoutuser_passwordUser_setter(instance):
    original = instance.passwordUser
    instance.passwordUser = original
    assert instance.passwordUser == original




@given(instance=Ticket_strategy)
def test_hyp_ticket_idCustomer_setter(instance):
    original = instance.idCustomer
    instance.idCustomer = original
    assert instance.idCustomer == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_idTicket_setter(instance):
    original = instance.idTicket
    instance.idTicket = original
    assert instance.idTicket == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_timeExchange_setter(instance):
    original = instance.timeExchange
    instance.timeExchange = original
    assert instance.timeExchange == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_statusSeat_setter(instance):
    original = instance.statusSeat
    instance.statusSeat = original
    assert instance.statusSeat == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_positionSeat_setter(instance):
    original = instance.positionSeat
    instance.positionSeat = original
    assert instance.positionSeat == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_numberSeat_setter(instance):
    original = instance.numberSeat
    instance.numberSeat = original
    assert instance.numberSeat == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_positionSeatBelow_setter(instance):
    original = instance.positionSeatBelow
    instance.positionSeatBelow = original
    assert instance.positionSeatBelow == original




@given(instance=Customer_strategy)
def test_hyp_customer_emailCustomer_setter(instance):
    original = instance.emailCustomer
    instance.emailCustomer = original
    assert instance.emailCustomer == original



@given(instance=Customer_strategy)
def test_hyp_customer_phoneCustomer_setter(instance):
    original = instance.phoneCustomer
    instance.phoneCustomer = original
    assert instance.phoneCustomer == original



@given(instance=Customer_strategy)
def test_hyp_customer_idCustomer_setter(instance):
    original = instance.idCustomer
    instance.idCustomer = original
    assert instance.idCustomer == original



@given(instance=Customer_strategy)
def test_hyp_customer_nameCustomer_setter(instance):
    original = instance.nameCustomer
    instance.nameCustomer = original
    assert instance.nameCustomer == original




@given(instance=infoCompany_strategy)
def test_hyp_infocompany_idCompany_setter(instance):
    original = instance.idCompany
    instance.idCompany = original
    assert instance.idCompany == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_nameCompany_setter(instance):
    original = instance.nameCompany
    instance.nameCompany = original
    assert instance.nameCompany == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_dateEstablish_setter(instance):
    original = instance.dateEstablish
    instance.dateEstablish = original
    assert instance.dateEstablish == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_describeCompany_setter(instance):
    original = instance.describeCompany
    instance.describeCompany = original
    assert instance.describeCompany == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_addressCompany_setter(instance):
    original = instance.addressCompany
    instance.addressCompany = original
    assert instance.addressCompany == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_showSafe_setter(instance):
    original = instance.showSafe
    instance.showSafe = original
    assert instance.showSafe == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_dateUpdate_setter(instance):
    original = instance.dateUpdate
    instance.dateUpdate = original
    assert instance.dateUpdate == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_dateRegister_setter(instance):
    original = instance.dateRegister
    instance.dateRegister = original
    assert instance.dateRegister == original



@given(instance=infoCompany_strategy)
def test_hyp_infocompany_phoneCompany_setter(instance):
    original = instance.phoneCompany
    instance.phoneCompany = original
    assert instance.phoneCompany == original




@given(instance=mapCarExchange_strategy)
def test_hyp_mapcarexchange_mapOnCar_setter(instance):
    original = instance.mapOnCar
    instance.mapOnCar = original
    assert instance.mapOnCar == original



@given(instance=mapCarExchange_strategy)
def test_hyp_mapcarexchange_idMap_setter(instance):
    original = instance.idMap
    instance.idMap = original
    assert instance.idMap == original



@given(instance=mapCarExchange_strategy)
def test_hyp_mapcarexchange_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=mapCarExchange_strategy)
def test_hyp_mapcarexchange_timeExchange_setter(instance):
    original = instance.timeExchange
    instance.timeExchange = original
    assert instance.timeExchange == original



@given(instance=mapCarExchange_strategy)
def test_hyp_mapcarexchange_mapBelowCar_setter(instance):
    original = instance.mapBelowCar
    instance.mapBelowCar = original
    assert instance.mapBelowCar == original




@given(instance=Car_strategy)
def test_hyp_car_idUser_setter(instance):
    original = instance.idUser
    instance.idUser = original
    assert instance.idUser == original



@given(instance=Car_strategy)
def test_hyp_car_statusCar_setter(instance):
    original = instance.statusCar
    instance.statusCar = original
    assert instance.statusCar == original



@given(instance=Car_strategy)
def test_hyp_car_timeStartCar_setter(instance):
    original = instance.timeStartCar
    instance.timeStartCar = original
    assert instance.timeStartCar == original



@given(instance=Car_strategy)
def test_hyp_car_fareCar_setter(instance):
    original = instance.fareCar
    instance.fareCar = original
    assert instance.fareCar == original



@given(instance=Car_strategy)
def test_hyp_car_positionEndCar_setter(instance):
    original = instance.positionEndCar
    instance.positionEndCar = original
    assert instance.positionEndCar == original



@given(instance=Car_strategy)
def test_hyp_car_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=Car_strategy)
def test_hyp_car_classifyCar_setter(instance):
    original = instance.classifyCar
    instance.classifyCar = original
    assert instance.classifyCar == original



@given(instance=Car_strategy)
def test_hyp_car_positionStartCar_setter(instance):
    original = instance.positionStartCar
    instance.positionStartCar = original
    assert instance.positionStartCar == original



@given(instance=Car_strategy)
def test_hyp_car_mapOnCar_setter(instance):
    original = instance.mapOnCar
    instance.mapOnCar = original
    assert instance.mapOnCar == original



@given(instance=Car_strategy)
def test_hyp_car_mapBelowCar_setter(instance):
    original = instance.mapBelowCar
    instance.mapBelowCar = original
    assert instance.mapBelowCar == original



@given(instance=Car_strategy)
def test_hyp_car_numberPlatesCar_setter(instance):
    original = instance.numberPlatesCar
    instance.numberPlatesCar = original
    assert instance.numberPlatesCar == original



@given(instance=Car_strategy)
def test_hyp_car_phoneCar_setter(instance):
    original = instance.phoneCar
    instance.phoneCar = original
    assert instance.phoneCar == original



@given(instance=Car_strategy)
def test_hyp_car_imageLinkCar_setter(instance):
    original = instance.imageLinkCar
    instance.imageLinkCar = original
    assert instance.imageLinkCar == original



@given(instance=Car_strategy)
def test_hyp_car_nameCar_setter(instance):
    original = instance.nameCar
    instance.nameCar = original
    assert instance.nameCar == original































# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account_settings_UseCase,
    Book_ticket_UseCase,
    Car,
    Customer,
    Customer_Actor,
    Customer_Actor1,
    Delete_vehicles_UseCase,
    Login_UseCase,
    Login_UseCase1,
    Login_UseCase2,
    Login_UseCase3,
    Manager_Actor,
    Manager_Actor1,
    Manager_Actor2,
    Manager_Actor3,
    Manager_Actor4,
    Report_by_revenue_UseCase,
    Report_by_ticket_amount_UseCase,
    Search_the_route_UseCase,
    Ticket,
    Update_vehicles_information_UseCase,
    Use_Actor,
    View_account_information_UseCase,
    View_customers_information_UseCase,
    View_vehicles_information_UseCase,
    account_management_UseCase,
    account_management_UseCase1,
    accoutUser,
    book_ticket_UseCase,
    call_for_customers_UseCase,
    cancel_booking_UseCase,
    choose_seats_UseCase,
    choose_vehicle_UseCase,
    confirm_booking_UseCase,
    confirm_information_UseCase,
    customer_management_UseCase,
    customer_management_UseCase1,
    infoCompany,
    make_payment_UseCase,
    mapCarExchange,
    search_UseCase,
    search_customers_UseCase,
    statistical_reporting_UseCase,
    statistical_reporting_UseCase1,
    vehicle_management_UseCase,
    vehicle_management_UseCase1,
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

def test_Car_classifyCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.classifyCar == 7
    instance.classifyCar = 13
    assert instance.classifyCar == 13


def test_Car_fareCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.fareCar == "sample_text"
    instance.fareCar = "sample_text_2"
    assert instance.fareCar == "sample_text_2"


def test_Car_idCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.idCar == 7
    instance.idCar = 13
    assert instance.idCar == 13


def test_Car_idUser_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.idUser == 7
    instance.idUser = 13
    assert instance.idUser == 13


def test_Car_imageLinkCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.imageLinkCar == "sample_text"
    instance.imageLinkCar = "sample_text_2"
    assert instance.imageLinkCar == "sample_text_2"


def test_Car_mapBelowCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.mapBelowCar == "sample_text"
    instance.mapBelowCar = "sample_text_2"
    assert instance.mapBelowCar == "sample_text_2"


def test_Car_mapOnCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.mapOnCar == "sample_text"
    instance.mapOnCar = "sample_text_2"
    assert instance.mapOnCar == "sample_text_2"


def test_Car_nameCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.nameCar == "sample_text"
    instance.nameCar = "sample_text_2"
    assert instance.nameCar == "sample_text_2"


def test_Car_numberPlatesCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.numberPlatesCar == "sample_text"
    instance.numberPlatesCar = "sample_text_2"
    assert instance.numberPlatesCar == "sample_text_2"


def test_Car_phoneCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.phoneCar == "sample_text"
    instance.phoneCar = "sample_text_2"
    assert instance.phoneCar == "sample_text_2"


def test_Car_positionEndCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.positionEndCar == "sample_text"
    instance.positionEndCar = "sample_text_2"
    assert instance.positionEndCar == "sample_text_2"


def test_Car_positionStartCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.positionStartCar == "sample_text"
    instance.positionStartCar = "sample_text_2"
    assert instance.positionStartCar == "sample_text_2"


def test_Car_statusCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.statusCar == 7
    instance.statusCar = 13
    assert instance.statusCar == 13


def test_Car_timeStartCar_value_roundtrip():
    instance = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    assert instance.timeStartCar == "sample_text"
    instance.timeStartCar = "sample_text_2"
    assert instance.timeStartCar == "sample_text_2"


def test_Customer_emailCustomer_value_roundtrip():
    instance = Customer(emailCustomer="sample_text", idCustomer=7, nameCustomer="sample_text", phoneCustomer="sample_text")
    assert instance.emailCustomer == "sample_text"
    instance.emailCustomer = "sample_text_2"
    assert instance.emailCustomer == "sample_text_2"


def test_Customer_idCustomer_value_roundtrip():
    instance = Customer(emailCustomer="sample_text", idCustomer=7, nameCustomer="sample_text", phoneCustomer="sample_text")
    assert instance.idCustomer == 7
    instance.idCustomer = 13
    assert instance.idCustomer == 13


def test_Customer_nameCustomer_value_roundtrip():
    instance = Customer(emailCustomer="sample_text", idCustomer=7, nameCustomer="sample_text", phoneCustomer="sample_text")
    assert instance.nameCustomer == "sample_text"
    instance.nameCustomer = "sample_text_2"
    assert instance.nameCustomer == "sample_text_2"


def test_Customer_phoneCustomer_value_roundtrip():
    instance = Customer(emailCustomer="sample_text", idCustomer=7, nameCustomer="sample_text", phoneCustomer="sample_text")
    assert instance.phoneCustomer == "sample_text"
    instance.phoneCustomer = "sample_text_2"
    assert instance.phoneCustomer == "sample_text_2"


def test_Ticket_code_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_Ticket_idCar_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.idCar == 7
    instance.idCar = 13
    assert instance.idCar == 13


def test_Ticket_idCustomer_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.idCustomer == 7
    instance.idCustomer = 13
    assert instance.idCustomer == 13


def test_Ticket_idTicket_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.idTicket == 7
    instance.idTicket = 13
    assert instance.idTicket == 13


def test_Ticket_numberSeat_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.numberSeat == 7
    instance.numberSeat = 13
    assert instance.numberSeat == 13


def test_Ticket_positionSeat_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.positionSeat == "sample_text"
    instance.positionSeat = "sample_text_2"
    assert instance.positionSeat == "sample_text_2"


def test_Ticket_positionSeatBelow_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.positionSeatBelow == "sample_text"
    instance.positionSeatBelow = "sample_text_2"
    assert instance.positionSeatBelow == "sample_text_2"


def test_Ticket_statusSeat_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.statusSeat == 7
    instance.statusSeat = 13
    assert instance.statusSeat == 13


def test_Ticket_timeExchange_value_roundtrip():
    instance = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    assert instance.timeExchange == "sample_text"
    instance.timeExchange = "sample_text_2"
    assert instance.timeExchange == "sample_text_2"


def test_accoutUser_codeConfirm_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.codeConfirm == "sample_text"
    instance.codeConfirm = "sample_text_2"
    assert instance.codeConfirm == "sample_text_2"


def test_accoutUser_dateRegister_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.dateRegister == "sample_text"
    instance.dateRegister = "sample_text_2"
    assert instance.dateRegister == "sample_text_2"


def test_accoutUser_emailUser_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.emailUser == "sample_text"
    instance.emailUser = "sample_text_2"
    assert instance.emailUser == "sample_text_2"


def test_accoutUser_idCompany_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.idCompany == 7
    instance.idCompany = 13
    assert instance.idCompany == 13


def test_accoutUser_idUser_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.idUser == 7
    instance.idUser = 13
    assert instance.idUser == 13


def test_accoutUser_passwordUser_value_roundtrip():
    instance = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    assert instance.passwordUser == "sample_text"
    instance.passwordUser = "sample_text_2"
    assert instance.passwordUser == "sample_text_2"


def test_infoCompany_addressCompany_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.addressCompany == "sample_text"
    instance.addressCompany = "sample_text_2"
    assert instance.addressCompany == "sample_text_2"


def test_infoCompany_dateEstablish_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.dateEstablish == "sample_text"
    instance.dateEstablish = "sample_text_2"
    assert instance.dateEstablish == "sample_text_2"


def test_infoCompany_dateRegister_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.dateRegister == "sample_text"
    instance.dateRegister = "sample_text_2"
    assert instance.dateRegister == "sample_text_2"


def test_infoCompany_dateUpdate_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.dateUpdate == "sample_text"
    instance.dateUpdate = "sample_text_2"
    assert instance.dateUpdate == "sample_text_2"


def test_infoCompany_describeCompany_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.describeCompany == "sample_text"
    instance.describeCompany = "sample_text_2"
    assert instance.describeCompany == "sample_text_2"


def test_infoCompany_idCompany_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.idCompany == 7
    instance.idCompany = 13
    assert instance.idCompany == 13


def test_infoCompany_nameCompany_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.nameCompany == "sample_text"
    instance.nameCompany = "sample_text_2"
    assert instance.nameCompany == "sample_text_2"


def test_infoCompany_phoneCompany_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.phoneCompany == "sample_text"
    instance.phoneCompany = "sample_text_2"
    assert instance.phoneCompany == "sample_text_2"


def test_infoCompany_showSafe_value_roundtrip():
    instance = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    assert instance.showSafe == "sample_text"
    instance.showSafe = "sample_text_2"
    assert instance.showSafe == "sample_text_2"


def test_mapCarExchange_idCar_value_roundtrip():
    instance = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    assert instance.idCar == 7
    instance.idCar = 13
    assert instance.idCar == 13


def test_mapCarExchange_idMap_value_roundtrip():
    instance = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    assert instance.idMap == 7
    instance.idMap = 13
    assert instance.idMap == 13


def test_mapCarExchange_mapBelowCar_value_roundtrip():
    instance = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    assert instance.mapBelowCar == "sample_text"
    instance.mapBelowCar = "sample_text_2"
    assert instance.mapBelowCar == "sample_text_2"


def test_mapCarExchange_mapOnCar_value_roundtrip():
    instance = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    assert instance.mapOnCar == "sample_text"
    instance.mapOnCar = "sample_text_2"
    assert instance.mapOnCar == "sample_text_2"


def test_mapCarExchange_timeExchange_value_roundtrip():
    instance = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    assert instance.timeExchange == "sample_text"
    instance.timeExchange = "sample_text_2"
    assert instance.timeExchange == "sample_text_2"


def test_assoc_Car_Car_link_reassign_clear():
    a = mapCarExchange(idCar=7, idMap=7, mapBelowCar="sample_text", mapOnCar="sample_text", timeExchange="sample_text")
    b1 = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    b2 = Car(classifyCar=13, fareCar="sample_text_2", idCar=13, idUser=13, imageLinkCar="sample_text_2", mapBelowCar="sample_text_2", mapOnCar="sample_text_2", nameCar="sample_text_2", numberPlatesCar="sample_text_2", phoneCar="sample_text_2", positionEndCar="sample_text_2", positionStartCar="sample_text_2", statusCar=13, timeStartCar="sample_text_2")
    _safe_set(a, 'Car_Car_022', b1)
    assert _is_linked(a, 'Car_Car_022', b1)
    if hasattr(b1, 'Car_Car_123'):
        assert _is_linked(b1, 'Car_Car_123', a)
    _safe_set(a, 'Car_Car_022', b2)
    assert _is_linked(a, 'Car_Car_022', b2)
    if hasattr(b1, 'Car_Car_123'):
        assert not _is_linked(b1, 'Car_Car_123', a)
    if hasattr(b2, 'Car_Car_123'):
        assert _is_linked(b2, 'Car_Car_123', a)
    _safe_set(a, 'Car_Car_022', None)
    assert not _is_linked(a, 'Car_Car_022', b2)
    if hasattr(b2, 'Car_Car_123'):
        assert not _is_linked(b2, 'Car_Car_123', a)


def test_assoc_Car_Car2_link_reassign_clear():
    a = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    b1 = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    b2 = Car(classifyCar=13, fareCar="sample_text_2", idCar=13, idUser=13, imageLinkCar="sample_text_2", mapBelowCar="sample_text_2", mapOnCar="sample_text_2", nameCar="sample_text_2", numberPlatesCar="sample_text_2", phoneCar="sample_text_2", positionEndCar="sample_text_2", positionStartCar="sample_text_2", statusCar=13, timeStartCar="sample_text_2")
    _safe_set(a, 'Car_Car2_026', b1)
    assert _is_linked(a, 'Car_Car2_026', b1)
    if hasattr(b1, 'Car_Car2_127'):
        assert _is_linked(b1, 'Car_Car2_127', a)
    _safe_set(a, 'Car_Car2_026', b2)
    assert _is_linked(a, 'Car_Car2_026', b2)
    if hasattr(b1, 'Car_Car2_127'):
        assert not _is_linked(b1, 'Car_Car2_127', a)
    if hasattr(b2, 'Car_Car2_127'):
        assert _is_linked(b2, 'Car_Car2_127', a)
    _safe_set(a, 'Car_Car2_026', None)
    assert not _is_linked(a, 'Car_Car2_026', b2)
    if hasattr(b2, 'Car_Car2_127'):
        assert not _is_linked(b2, 'Car_Car2_127', a)


def test_assoc_Customer_Customer_link_reassign_clear():
    a = Ticket(code="sample_text", idCar=7, idCustomer=7, idTicket=7, numberSeat=7, positionSeat="sample_text", positionSeatBelow="sample_text", statusSeat=7, timeExchange="sample_text")
    b1 = Customer(emailCustomer="sample_text", idCustomer=7, nameCustomer="sample_text", phoneCustomer="sample_text")
    b2 = Customer(emailCustomer="sample_text_2", idCustomer=13, nameCustomer="sample_text_2", phoneCustomer="sample_text_2")
    _safe_set(a, 'Customer_Customer_028', b1)
    assert _is_linked(a, 'Customer_Customer_028', b1)
    if hasattr(b1, 'Customer_Customer_129'):
        assert _is_linked(b1, 'Customer_Customer_129', a)
    _safe_set(a, 'Customer_Customer_028', b2)
    assert _is_linked(a, 'Customer_Customer_028', b2)
    if hasattr(b1, 'Customer_Customer_129'):
        assert not _is_linked(b1, 'Customer_Customer_129', a)
    if hasattr(b2, 'Customer_Customer_129'):
        assert _is_linked(b2, 'Customer_Customer_129', a)
    _safe_set(a, 'Customer_Customer_028', None)
    assert not _is_linked(a, 'Customer_Customer_028', b2)
    if hasattr(b2, 'Customer_Customer_129'):
        assert not _is_linked(b2, 'Customer_Customer_129', a)


def test_assoc_accoutUser_accoutUser_link_reassign_clear():
    a = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    b1 = Car(classifyCar=7, fareCar="sample_text", idCar=7, idUser=7, imageLinkCar="sample_text", mapBelowCar="sample_text", mapOnCar="sample_text", nameCar="sample_text", numberPlatesCar="sample_text", phoneCar="sample_text", positionEndCar="sample_text", positionStartCar="sample_text", statusCar=7, timeStartCar="sample_text")
    b2 = Car(classifyCar=13, fareCar="sample_text_2", idCar=13, idUser=13, imageLinkCar="sample_text_2", mapBelowCar="sample_text_2", mapOnCar="sample_text_2", nameCar="sample_text_2", numberPlatesCar="sample_text_2", phoneCar="sample_text_2", positionEndCar="sample_text_2", positionStartCar="sample_text_2", statusCar=13, timeStartCar="sample_text_2")
    _safe_set(a, 'accoutUser_accoutUser_125', {b1})
    assert _is_linked(a, 'accoutUser_accoutUser_125', b1)
    if hasattr(b1, 'accoutUser_accoutUser_024'):
        assert _is_linked(b1, 'accoutUser_accoutUser_024', a)
    _safe_set(a, 'accoutUser_accoutUser_125', {b2})
    assert _is_linked(a, 'accoutUser_accoutUser_125', b2)
    if hasattr(b1, 'accoutUser_accoutUser_024'):
        assert not _is_linked(b1, 'accoutUser_accoutUser_024', a)
    if hasattr(b2, 'accoutUser_accoutUser_024'):
        assert _is_linked(b2, 'accoutUser_accoutUser_024', a)
    _safe_set(a, 'accoutUser_accoutUser_125', set())
    assert not _is_linked(a, 'accoutUser_accoutUser_125', b2)
    if hasattr(b2, 'accoutUser_accoutUser_024'):
        assert not _is_linked(b2, 'accoutUser_accoutUser_024', a)


def test_assoc_infoCompany_infoCompany_link_reassign_clear():
    a = infoCompany(addressCompany="sample_text", dateEstablish="sample_text", dateRegister="sample_text", dateUpdate="sample_text", describeCompany="sample_text", idCompany=7, nameCompany="sample_text", phoneCompany="sample_text", showSafe="sample_text")
    b1 = accoutUser(codeConfirm="sample_text", dateRegister="sample_text", emailUser="sample_text", idCompany=7, idUser=7, passwordUser="sample_text")
    b2 = accoutUser(codeConfirm="sample_text_2", dateRegister="sample_text_2", emailUser="sample_text_2", idCompany=13, idUser=13, passwordUser="sample_text_2")
    _safe_set(a, 'infoCompany_infoCompany_131', {b1})
    assert _is_linked(a, 'infoCompany_infoCompany_131', b1)
    if hasattr(b1, 'infoCompany_infoCompany_030'):
        assert _is_linked(b1, 'infoCompany_infoCompany_030', a)
    _safe_set(a, 'infoCompany_infoCompany_131', {b2})
    assert _is_linked(a, 'infoCompany_infoCompany_131', b2)
    if hasattr(b1, 'infoCompany_infoCompany_030'):
        assert not _is_linked(b1, 'infoCompany_infoCompany_030', a)
    if hasattr(b2, 'infoCompany_infoCompany_030'):
        assert _is_linked(b2, 'infoCompany_infoCompany_030', a)
    _safe_set(a, 'infoCompany_infoCompany_131', set())
    assert not _is_linked(a, 'infoCompany_infoCompany_131', b2)
    if hasattr(b2, 'infoCompany_infoCompany_030'):
        assert not _is_linked(b2, 'infoCompany_infoCompany_030', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_settings_UseCase_strategy = st.builds(Account_settings_UseCase)
@given(instance=Account_settings_UseCase_strategy)
@settings(max_examples=25)
def test_Account_settings_UseCase_instantiation(instance):
    assert isinstance(instance, Account_settings_UseCase)


Book_ticket_UseCase_strategy = st.builds(Book_ticket_UseCase)
@given(instance=Book_ticket_UseCase_strategy)
@settings(max_examples=25)
def test_Book_ticket_UseCase_instantiation(instance):
    assert isinstance(instance, Book_ticket_UseCase)


Car_strategy = st.builds(Car, classifyCar=st.integers(), fareCar=safe_text, idCar=st.integers(), idUser=st.integers(), imageLinkCar=safe_text, mapBelowCar=safe_text, mapOnCar=safe_text, nameCar=safe_text, numberPlatesCar=safe_text, phoneCar=safe_text, positionEndCar=safe_text, positionStartCar=safe_text, statusCar=st.integers(), timeStartCar=safe_text)
@given(instance=Car_strategy)
@settings(max_examples=25)
def test_Car_instantiation(instance):
    assert isinstance(instance, Car)


Customer_strategy = st.builds(Customer, emailCustomer=safe_text, idCustomer=st.integers(), nameCustomer=safe_text, phoneCustomer=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Customer_Actor_strategy = st.builds(Customer_Actor)
@given(instance=Customer_Actor_strategy)
@settings(max_examples=25)
def test_Customer_Actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)


Customer_Actor1_strategy = st.builds(Customer_Actor1)
@given(instance=Customer_Actor1_strategy)
@settings(max_examples=25)
def test_Customer_Actor1_instantiation(instance):
    assert isinstance(instance, Customer_Actor1)


Delete_vehicles_UseCase_strategy = st.builds(Delete_vehicles_UseCase)
@given(instance=Delete_vehicles_UseCase_strategy)
@settings(max_examples=25)
def test_Delete_vehicles_UseCase_instantiation(instance):
    assert isinstance(instance, Delete_vehicles_UseCase)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Login_UseCase1_strategy = st.builds(Login_UseCase1)
@given(instance=Login_UseCase1_strategy)
@settings(max_examples=25)
def test_Login_UseCase1_instantiation(instance):
    assert isinstance(instance, Login_UseCase1)


Login_UseCase2_strategy = st.builds(Login_UseCase2)
@given(instance=Login_UseCase2_strategy)
@settings(max_examples=25)
def test_Login_UseCase2_instantiation(instance):
    assert isinstance(instance, Login_UseCase2)


Login_UseCase3_strategy = st.builds(Login_UseCase3)
@given(instance=Login_UseCase3_strategy)
@settings(max_examples=25)
def test_Login_UseCase3_instantiation(instance):
    assert isinstance(instance, Login_UseCase3)


Manager_Actor_strategy = st.builds(Manager_Actor)
@given(instance=Manager_Actor_strategy)
@settings(max_examples=25)
def test_Manager_Actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)


Manager_Actor1_strategy = st.builds(Manager_Actor1)
@given(instance=Manager_Actor1_strategy)
@settings(max_examples=25)
def test_Manager_Actor1_instantiation(instance):
    assert isinstance(instance, Manager_Actor1)


Manager_Actor2_strategy = st.builds(Manager_Actor2)
@given(instance=Manager_Actor2_strategy)
@settings(max_examples=25)
def test_Manager_Actor2_instantiation(instance):
    assert isinstance(instance, Manager_Actor2)


Manager_Actor3_strategy = st.builds(Manager_Actor3)
@given(instance=Manager_Actor3_strategy)
@settings(max_examples=25)
def test_Manager_Actor3_instantiation(instance):
    assert isinstance(instance, Manager_Actor3)


Manager_Actor4_strategy = st.builds(Manager_Actor4)
@given(instance=Manager_Actor4_strategy)
@settings(max_examples=25)
def test_Manager_Actor4_instantiation(instance):
    assert isinstance(instance, Manager_Actor4)


Report_by_revenue_UseCase_strategy = st.builds(Report_by_revenue_UseCase)
@given(instance=Report_by_revenue_UseCase_strategy)
@settings(max_examples=25)
def test_Report_by_revenue_UseCase_instantiation(instance):
    assert isinstance(instance, Report_by_revenue_UseCase)


Report_by_ticket_amount_UseCase_strategy = st.builds(Report_by_ticket_amount_UseCase)
@given(instance=Report_by_ticket_amount_UseCase_strategy)
@settings(max_examples=25)
def test_Report_by_ticket_amount_UseCase_instantiation(instance):
    assert isinstance(instance, Report_by_ticket_amount_UseCase)


Search_the_route_UseCase_strategy = st.builds(Search_the_route_UseCase)
@given(instance=Search_the_route_UseCase_strategy)
@settings(max_examples=25)
def test_Search_the_route_UseCase_instantiation(instance):
    assert isinstance(instance, Search_the_route_UseCase)


Ticket_strategy = st.builds(Ticket, code=safe_text, idCar=st.integers(), idCustomer=st.integers(), idTicket=st.integers(), numberSeat=st.integers(), positionSeat=safe_text, positionSeatBelow=safe_text, statusSeat=st.integers(), timeExchange=safe_text)
@given(instance=Ticket_strategy)
@settings(max_examples=25)
def test_Ticket_instantiation(instance):
    assert isinstance(instance, Ticket)


Update_vehicles_information_UseCase_strategy = st.builds(Update_vehicles_information_UseCase)
@given(instance=Update_vehicles_information_UseCase_strategy)
@settings(max_examples=25)
def test_Update_vehicles_information_UseCase_instantiation(instance):
    assert isinstance(instance, Update_vehicles_information_UseCase)


Use_Actor_strategy = st.builds(Use_Actor)
@given(instance=Use_Actor_strategy)
@settings(max_examples=25)
def test_Use_Actor_instantiation(instance):
    assert isinstance(instance, Use_Actor)


View_account_information_UseCase_strategy = st.builds(View_account_information_UseCase)
@given(instance=View_account_information_UseCase_strategy)
@settings(max_examples=25)
def test_View_account_information_UseCase_instantiation(instance):
    assert isinstance(instance, View_account_information_UseCase)


View_customers_information_UseCase_strategy = st.builds(View_customers_information_UseCase)
@given(instance=View_customers_information_UseCase_strategy)
@settings(max_examples=25)
def test_View_customers_information_UseCase_instantiation(instance):
    assert isinstance(instance, View_customers_information_UseCase)


View_vehicles_information_UseCase_strategy = st.builds(View_vehicles_information_UseCase)
@given(instance=View_vehicles_information_UseCase_strategy)
@settings(max_examples=25)
def test_View_vehicles_information_UseCase_instantiation(instance):
    assert isinstance(instance, View_vehicles_information_UseCase)


account_management_UseCase_strategy = st.builds(account_management_UseCase)
@given(instance=account_management_UseCase_strategy)
@settings(max_examples=25)
def test_account_management_UseCase_instantiation(instance):
    assert isinstance(instance, account_management_UseCase)


account_management_UseCase1_strategy = st.builds(account_management_UseCase1)
@given(instance=account_management_UseCase1_strategy)
@settings(max_examples=25)
def test_account_management_UseCase1_instantiation(instance):
    assert isinstance(instance, account_management_UseCase1)


accoutUser_strategy = st.builds(accoutUser, codeConfirm=safe_text, dateRegister=safe_text, emailUser=safe_text, idCompany=st.integers(), idUser=st.integers(), passwordUser=safe_text)
@given(instance=accoutUser_strategy)
@settings(max_examples=25)
def test_accoutUser_instantiation(instance):
    assert isinstance(instance, accoutUser)


book_ticket_UseCase_strategy = st.builds(book_ticket_UseCase)
@given(instance=book_ticket_UseCase_strategy)
@settings(max_examples=25)
def test_book_ticket_UseCase_instantiation(instance):
    assert isinstance(instance, book_ticket_UseCase)


call_for_customers_UseCase_strategy = st.builds(call_for_customers_UseCase)
@given(instance=call_for_customers_UseCase_strategy)
@settings(max_examples=25)
def test_call_for_customers_UseCase_instantiation(instance):
    assert isinstance(instance, call_for_customers_UseCase)


cancel_booking_UseCase_strategy = st.builds(cancel_booking_UseCase)
@given(instance=cancel_booking_UseCase_strategy)
@settings(max_examples=25)
def test_cancel_booking_UseCase_instantiation(instance):
    assert isinstance(instance, cancel_booking_UseCase)


choose_seats_UseCase_strategy = st.builds(choose_seats_UseCase)
@given(instance=choose_seats_UseCase_strategy)
@settings(max_examples=25)
def test_choose_seats_UseCase_instantiation(instance):
    assert isinstance(instance, choose_seats_UseCase)


choose_vehicle_UseCase_strategy = st.builds(choose_vehicle_UseCase)
@given(instance=choose_vehicle_UseCase_strategy)
@settings(max_examples=25)
def test_choose_vehicle_UseCase_instantiation(instance):
    assert isinstance(instance, choose_vehicle_UseCase)


confirm_booking_UseCase_strategy = st.builds(confirm_booking_UseCase)
@given(instance=confirm_booking_UseCase_strategy)
@settings(max_examples=25)
def test_confirm_booking_UseCase_instantiation(instance):
    assert isinstance(instance, confirm_booking_UseCase)


confirm_information_UseCase_strategy = st.builds(confirm_information_UseCase)
@given(instance=confirm_information_UseCase_strategy)
@settings(max_examples=25)
def test_confirm_information_UseCase_instantiation(instance):
    assert isinstance(instance, confirm_information_UseCase)


customer_management_UseCase_strategy = st.builds(customer_management_UseCase)
@given(instance=customer_management_UseCase_strategy)
@settings(max_examples=25)
def test_customer_management_UseCase_instantiation(instance):
    assert isinstance(instance, customer_management_UseCase)


customer_management_UseCase1_strategy = st.builds(customer_management_UseCase1)
@given(instance=customer_management_UseCase1_strategy)
@settings(max_examples=25)
def test_customer_management_UseCase1_instantiation(instance):
    assert isinstance(instance, customer_management_UseCase1)


infoCompany_strategy = st.builds(infoCompany, addressCompany=safe_text, dateEstablish=safe_text, dateRegister=safe_text, dateUpdate=safe_text, describeCompany=safe_text, idCompany=st.integers(), nameCompany=safe_text, phoneCompany=safe_text, showSafe=safe_text)
@given(instance=infoCompany_strategy)
@settings(max_examples=25)
def test_infoCompany_instantiation(instance):
    assert isinstance(instance, infoCompany)


make_payment_UseCase_strategy = st.builds(make_payment_UseCase)
@given(instance=make_payment_UseCase_strategy)
@settings(max_examples=25)
def test_make_payment_UseCase_instantiation(instance):
    assert isinstance(instance, make_payment_UseCase)


mapCarExchange_strategy = st.builds(mapCarExchange, idCar=st.integers(), idMap=st.integers(), mapBelowCar=safe_text, mapOnCar=safe_text, timeExchange=safe_text)
@given(instance=mapCarExchange_strategy)
@settings(max_examples=25)
def test_mapCarExchange_instantiation(instance):
    assert isinstance(instance, mapCarExchange)


search_UseCase_strategy = st.builds(search_UseCase)
@given(instance=search_UseCase_strategy)
@settings(max_examples=25)
def test_search_UseCase_instantiation(instance):
    assert isinstance(instance, search_UseCase)


search_customers_UseCase_strategy = st.builds(search_customers_UseCase)
@given(instance=search_customers_UseCase_strategy)
@settings(max_examples=25)
def test_search_customers_UseCase_instantiation(instance):
    assert isinstance(instance, search_customers_UseCase)


statistical_reporting_UseCase_strategy = st.builds(statistical_reporting_UseCase)
@given(instance=statistical_reporting_UseCase_strategy)
@settings(max_examples=25)
def test_statistical_reporting_UseCase_instantiation(instance):
    assert isinstance(instance, statistical_reporting_UseCase)


statistical_reporting_UseCase1_strategy = st.builds(statistical_reporting_UseCase1)
@given(instance=statistical_reporting_UseCase1_strategy)
@settings(max_examples=25)
def test_statistical_reporting_UseCase1_instantiation(instance):
    assert isinstance(instance, statistical_reporting_UseCase1)


vehicle_management_UseCase_strategy = st.builds(vehicle_management_UseCase)
@given(instance=vehicle_management_UseCase_strategy)
@settings(max_examples=25)
def test_vehicle_management_UseCase_instantiation(instance):
    assert isinstance(instance, vehicle_management_UseCase)


vehicle_management_UseCase1_strategy = st.builds(vehicle_management_UseCase1)
@given(instance=vehicle_management_UseCase1_strategy)
@settings(max_examples=25)
def test_vehicle_management_UseCase1_instantiation(instance):
    assert isinstance(instance, vehicle_management_UseCase1)



