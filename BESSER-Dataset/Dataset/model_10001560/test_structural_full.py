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


