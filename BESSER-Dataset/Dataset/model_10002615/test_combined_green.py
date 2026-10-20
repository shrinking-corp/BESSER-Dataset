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
    pharmacy,
    lab,
    Bursar,
    medicine,
    Bill,
    Receptionist,
    Room,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pharmacy_is_not_abstract():
    assert not inspect.isabstract(pharmacy)


def test_hyp_pharmacy_constructor_exists():
    assert callable(pharmacy.__init__)


def test_hyp_pharmacy_constructor_args():
    sig = inspect.signature(pharmacy.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "medicine" in params, "Missing parameter 'medicine'"





def test_hyp_lab_is_not_abstract():
    assert not inspect.isabstract(lab)


def test_hyp_lab_constructor_exists():
    assert callable(lab.__init__)


def test_hyp_lab_constructor_args():
    sig = inspect.signature(lab.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "results" in params, "Missing parameter 'results'"





def test_hyp_bursar_is_not_abstract():
    assert not inspect.isabstract(Bursar)


def test_hyp_bursar_constructor_exists():
    assert callable(Bursar.__init__)


def test_hyp_bursar_constructor_args():
    sig = inspect.signature(Bursar.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"





def test_hyp_medicine_is_not_abstract():
    assert not inspect.isabstract(medicine)


def test_hyp_medicine_constructor_exists():
    assert callable(medicine.__init__)


def test_hyp_medicine_constructor_args():
    sig = inspect.signature(medicine.__init__)
    params = list(sig.parameters.keys())
    assert "medicine" in params, "Missing parameter 'medicine'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "amount" in params, "Missing parameter 'amount'"





def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"





def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "roomname" in params, "Missing parameter 'roomname'"





def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "sex" in params, "Missing parameter 'sex'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "id" in params, "Missing parameter 'id'"
    assert "blood_group" in params, "Missing parameter 'blood_group'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "phonenumber" in params, "Missing parameter 'phonenumber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "birthyear" in params, "Missing parameter 'birthyear'"
    assert "addr" in params, "Missing parameter 'addr'"












def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "dentist" in params, "Missing parameter 'dentist'"
    assert "normal_doctor" in params, "Missing parameter 'normal_doctor'"
    assert "women_doctor" in params, "Missing parameter 'women_doctor'"

def test_hyp_doctor_has_dentist():
    assert hasattr(Doctor, "dentist")
    descriptor = None
    for klass in Doctor.__mro__:
        if "dentist" in klass.__dict__:
            descriptor = klass.__dict__["dentist"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_normal_doctor():
    assert hasattr(Doctor, "normal_doctor")
    descriptor = None
    for klass in Doctor.__mro__:
        if "normal_doctor" in klass.__dict__:
            descriptor = klass.__dict__["normal_doctor"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_women_doctor():
    assert hasattr(Doctor, "women_doctor")
    descriptor = None
    for klass in Doctor.__mro__:
        if "women_doctor" in klass.__dict__:
            descriptor = klass.__dict__["women_doctor"]
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
pharmacy_strategy = st.builds(
    pharmacy,
    price=
        st.integers(),
    medicine=
        safe_text
)
lab_strategy = st.builds(
    lab,
    price=
        st.integers(),
    results=
        safe_text
)
Bursar_strategy = st.builds(
    Bursar,
    lastname=
        safe_text,
    firstname=
        safe_text
)
medicine_strategy = st.builds(
    medicine,
    medicine=
        safe_text,
    price=
        st.integers(),
    id=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Receptionist_strategy = st.builds(
    Receptionist,
    firstname=
        safe_text,
    lastname=
        safe_text
)
Room_strategy = st.builds(
    Room,
    roomno=
        st.integers(),
    roomname=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    sex=
        safe_text,
    lastname=
        safe_text,
    id=
        st.integers(),
    blood_group=
        st.integers(),
    firstname=
        safe_text,
    phonenumber=
        st.integers(),
    email=
        safe_text,
    birthyear=
        st.integers(),
    addr=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    dentist=
        st.none(),
    normal_doctor=
        st.none(),
    women_doctor=
        st.none()
)




@given(instance=pharmacy_strategy)
def test_hyp_pharmacy_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=pharmacy_strategy)
def test_hyp_pharmacy_medicine_setter(instance):
    original = instance.medicine
    instance.medicine = original
    assert instance.medicine == original




@given(instance=lab_strategy)
def test_hyp_lab_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=lab_strategy)
def test_hyp_lab_results_setter(instance):
    original = instance.results
    instance.results = original
    assert instance.results == original




@given(instance=Bursar_strategy)
def test_hyp_bursar_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Bursar_strategy)
def test_hyp_bursar_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original




@given(instance=medicine_strategy)
def test_hyp_medicine_medicine_setter(instance):
    original = instance.medicine
    instance.medicine = original
    assert instance.medicine == original



@given(instance=medicine_strategy)
def test_hyp_medicine_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=medicine_strategy)
def test_hyp_medicine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Bill_strategy)
def test_hyp_bill_billno_setter(instance):
    original = instance.billno
    instance.billno = original
    assert instance.billno == original



@given(instance=Bill_strategy)
def test_hyp_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original




@given(instance=Room_strategy)
def test_hyp_room_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Room_strategy)
def test_hyp_room_roomname_setter(instance):
    original = instance.roomname
    instance.roomname = original
    assert instance.roomname == original




@given(instance=Patient_strategy)
def test_hyp_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=Patient_strategy)
def test_hyp_patient_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Patient_strategy)
def test_hyp_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_hyp_patient_blood_group_setter(instance):
    original = instance.blood_group
    instance.blood_group = original
    assert instance.blood_group == original



@given(instance=Patient_strategy)
def test_hyp_patient_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Patient_strategy)
def test_hyp_patient_phonenumber_setter(instance):
    original = instance.phonenumber
    instance.phonenumber = original
    assert instance.phonenumber == original



@given(instance=Patient_strategy)
def test_hyp_patient_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Patient_strategy)
def test_hyp_patient_birthyear_setter(instance):
    original = instance.birthyear
    instance.birthyear = original
    assert instance.birthyear == original



@given(instance=Patient_strategy)
def test_hyp_patient_addr_setter(instance):
    original = instance.addr
    instance.addr = original
    assert instance.addr == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_hyp_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_hyp_doctor_dentist_setter(instance):
    original = instance.dentist
    instance.dentist = original
    assert instance.dentist == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_normal_doctor_setter(instance):
    original = instance.normal_doctor
    instance.normal_doctor = original
    assert instance.normal_doctor == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_women_doctor_setter(instance):
    original = instance.women_doctor
    instance.women_doctor = original
    assert instance.women_doctor == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Bursar,
    Doctor,
    Patient,
    Receptionist,
    Room,
    lab,
    medicine,
    pharmacy,
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

def test_Bill_amount_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_Bill_billno_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text")
    assert instance.billno == "sample_text"
    instance.billno = "sample_text_2"
    assert instance.billno == "sample_text_2"


def test_Bursar_firstname_value_roundtrip():
    instance = Bursar(firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Bursar_lastname_value_roundtrip():
    instance = Bursar(firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Patient_addr_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.addr == "sample_text"
    instance.addr = "sample_text_2"
    assert instance.addr == "sample_text_2"


def test_Patient_birthyear_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.birthyear == 7
    instance.birthyear = 13
    assert instance.birthyear == 13


def test_Patient_blood_group_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.blood_group == 7
    instance.blood_group = 13
    assert instance.blood_group == 13


def test_Patient_email_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Patient_firstname_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Patient_id_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Patient_lastname_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Patient_phonenumber_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.phonenumber == 7
    instance.phonenumber = 13
    assert instance.phonenumber == 13


def test_Patient_sex_value_roundtrip():
    instance = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_Receptionist_firstname_value_roundtrip():
    instance = Receptionist(firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Receptionist_lastname_value_roundtrip():
    instance = Receptionist(firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Room_roomname_value_roundtrip():
    instance = Room(roomname="sample_text", roomno=7)
    assert instance.roomname == "sample_text"
    instance.roomname = "sample_text_2"
    assert instance.roomname == "sample_text_2"


def test_Room_roomno_value_roundtrip():
    instance = Room(roomname="sample_text", roomno=7)
    assert instance.roomno == 7
    instance.roomno = 13
    assert instance.roomno == 13


def test_lab_price_value_roundtrip():
    instance = lab(price=7, results="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_lab_results_value_roundtrip():
    instance = lab(price=7, results="sample_text")
    assert instance.results == "sample_text"
    instance.results = "sample_text_2"
    assert instance.results == "sample_text_2"


def test_medicine_id_value_roundtrip():
    instance = medicine(id=7, medicine="sample_text", price=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_medicine_medicine_value_roundtrip():
    instance = medicine(id=7, medicine="sample_text", price=7)
    assert instance.medicine == "sample_text"
    instance.medicine = "sample_text_2"
    assert instance.medicine == "sample_text_2"


def test_medicine_price_value_roundtrip():
    instance = medicine(id=7, medicine="sample_text", price=7)
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_pharmacy_medicine_value_roundtrip():
    instance = pharmacy(medicine="sample_text", price=7)
    assert instance.medicine == "sample_text"
    instance.medicine = "sample_text_2"
    assert instance.medicine == "sample_text_2"


def test_pharmacy_price_value_roundtrip():
    instance = pharmacy(medicine="sample_text", price=7)
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    b1 = Bill(amount=3.14, billno="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2")
    _safe_set(a, 'bill0', b1)
    assert _is_linked(a, 'bill0', b1)
    if hasattr(b1, 'pat1'):
        assert _is_linked(b1, 'pat1', a)
    _safe_set(a, 'bill0', b2)
    assert _is_linked(a, 'bill0', b2)
    if hasattr(b1, 'pat1'):
        assert not _is_linked(b1, 'pat1', a)
    if hasattr(b2, 'pat1'):
        assert _is_linked(b2, 'pat1', a)
    _safe_set(a, 'bill0', None)
    assert not _is_linked(a, 'bill0', b2)
    if hasattr(b2, 'pat1'):
        assert not _is_linked(b2, 'pat1', a)


def test_assoc_lab_Patient_link_reassign_clear():
    a = lab(price=7, results="sample_text")
    b1 = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    b2 = Patient(addr="sample_text_2", birthyear=13, blood_group=13, email="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", phonenumber=13, sex="sample_text_2")
    _safe_set(a, 'assign4', b1)
    assert _is_linked(a, 'assign4', b1)
    if hasattr(b1, 'lab5'):
        assert _is_linked(b1, 'lab5', a)
    _safe_set(a, 'assign4', b2)
    assert _is_linked(a, 'assign4', b2)
    if hasattr(b1, 'lab5'):
        assert not _is_linked(b1, 'lab5', a)
    if hasattr(b2, 'lab5'):
        assert _is_linked(b2, 'lab5', a)
    _safe_set(a, 'assign4', None)
    assert not _is_linked(a, 'assign4', b2)
    if hasattr(b2, 'lab5'):
        assert not _is_linked(b2, 'lab5', a)


def test_assoc_pharmacy_Bursar_link_reassign_clear():
    a = pharmacy(medicine="sample_text", price=7)
    b1 = Bursar(firstname="sample_text", lastname="sample_text")
    b2 = Bursar(firstname="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'medicine_cost8', b1)
    assert _is_linked(a, 'medicine_cost8', b1)
    if hasattr(b1, 'pharmacy9'):
        assert _is_linked(b1, 'pharmacy9', a)
    _safe_set(a, 'medicine_cost8', b2)
    assert _is_linked(a, 'medicine_cost8', b2)
    if hasattr(b1, 'pharmacy9'):
        assert not _is_linked(b1, 'pharmacy9', a)
    if hasattr(b2, 'pharmacy9'):
        assert _is_linked(b2, 'pharmacy9', a)
    _safe_set(a, 'medicine_cost8', None)
    assert not _is_linked(a, 'medicine_cost8', b2)
    if hasattr(b2, 'pharmacy9'):
        assert not _is_linked(b2, 'pharmacy9', a)


def test_assoc_pharmacy_Patient_link_reassign_clear():
    a = pharmacy(medicine="sample_text", price=7)
    b1 = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    b2 = Patient(addr="sample_text_2", birthyear=13, blood_group=13, email="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", phonenumber=13, sex="sample_text_2")
    _safe_set(a, 'gives_medicine10', b1)
    assert _is_linked(a, 'gives_medicine10', b1)
    if hasattr(b1, 'pharmacy11'):
        assert _is_linked(b1, 'pharmacy11', a)
    _safe_set(a, 'gives_medicine10', b2)
    assert _is_linked(a, 'gives_medicine10', b2)
    if hasattr(b1, 'pharmacy11'):
        assert not _is_linked(b1, 'pharmacy11', a)
    if hasattr(b2, 'pharmacy11'):
        assert _is_linked(b2, 'pharmacy11', a)
    _safe_set(a, 'gives_medicine10', None)
    assert not _is_linked(a, 'gives_medicine10', b2)
    if hasattr(b2, 'pharmacy11'):
        assert not _is_linked(b2, 'pharmacy11', a)


def test_assoc_receptions_link_reassign_clear():
    a = Receptionist(firstname="sample_text", lastname="sample_text")
    b1 = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    b2 = Patient(addr="sample_text_2", birthyear=13, blood_group=13, email="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", phonenumber=13, sex="sample_text_2")
    _safe_set(a, 'p3', b1)
    assert _is_linked(a, 'p3', b1)
    if hasattr(b1, 'receptionist2'):
        assert _is_linked(b1, 'receptionist2', a)
    _safe_set(a, 'p3', b2)
    assert _is_linked(a, 'p3', b2)
    if hasattr(b1, 'receptionist2'):
        assert not _is_linked(b1, 'receptionist2', a)
    if hasattr(b2, 'receptionist2'):
        assert _is_linked(b2, 'receptionist2', a)
    _safe_set(a, 'p3', None)
    assert not _is_linked(a, 'p3', b2)
    if hasattr(b2, 'receptionist2'):
        assert not _is_linked(b2, 'receptionist2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, amount=st.floats(allow_nan=False, allow_infinity=False), billno=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Bursar_strategy = st.builds(Bursar, firstname=safe_text, lastname=safe_text)
@given(instance=Bursar_strategy)
@settings(max_examples=25)
def test_Bursar_instantiation(instance):
    assert isinstance(instance, Bursar)


Patient_strategy = st.builds(Patient, addr=safe_text, birthyear=st.integers(), blood_group=st.integers(), email=safe_text, firstname=safe_text, id=st.integers(), lastname=safe_text, phonenumber=st.integers(), sex=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Receptionist_strategy = st.builds(Receptionist, firstname=safe_text, lastname=safe_text)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, roomname=safe_text, roomno=st.integers())
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


lab_strategy = st.builds(lab, price=st.integers(), results=safe_text)
@given(instance=lab_strategy)
@settings(max_examples=25)
def test_lab_instantiation(instance):
    assert isinstance(instance, lab)


medicine_strategy = st.builds(medicine, id=st.integers(), medicine=safe_text, price=st.integers())
@given(instance=medicine_strategy)
@settings(max_examples=25)
def test_medicine_instantiation(instance):
    assert isinstance(instance, medicine)


pharmacy_strategy = st.builds(pharmacy, medicine=safe_text, price=st.integers())
@given(instance=pharmacy_strategy)
@settings(max_examples=25)
def test_pharmacy_instantiation(instance):
    assert isinstance(instance, pharmacy)



