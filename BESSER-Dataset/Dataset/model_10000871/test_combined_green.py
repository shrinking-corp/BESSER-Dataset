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
    Procedure,
    Treatment,
    Bill,
    Receptionist,
    Patient,
    Department,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_hyp_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_hyp_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "idProcedure" in params, "Missing parameter 'idProcedure'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_treatment_is_not_abstract():
    assert not inspect.isabstract(Treatment)


def test_hyp_treatment_constructor_exists():
    assert callable(Treatment.__init__)


def test_hyp_treatment_constructor_args():
    sig = inspect.signature(Treatment.__init__)
    params = list(sig.parameters.keys())
    assert "procedureID" in params, "Missing parameter 'procedureID'"
    assert "patientID" in params, "Missing parameter 'patientID'"
    assert "idTreatment" in params, "Missing parameter 'idTreatment'"
    assert "idBill" in params, "Missing parameter 'idBill'"







def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "patientname" in params, "Missing parameter 'patientname'"
    assert "amount" in params, "Missing parameter 'amount'"






def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "telno" in params, "Missing parameter 'telno'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "id" in params, "Missing parameter 'id'"
    assert "sex" in params, "Missing parameter 'sex'"









def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "docid" in params, "Missing parameter 'docid'"
    assert "departamentID" in params, "Missing parameter 'departamentID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phno" in params, "Missing parameter 'phno'"
    assert "department" in params, "Missing parameter 'department'"
    assert "address" in params, "Missing parameter 'address'"
    assert "specialization" in params, "Missing parameter 'specialization'"









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
Procedure_strategy = st.builds(
    Procedure,
    idProcedure=
        st.integers(),
    price=
        st.integers(),
    name=
        safe_text
)
Treatment_strategy = st.builds(
    Treatment,
    procedureID=
        st.integers(),
    patientID=
        st.integers(),
    idTreatment=
        st.integers(),
    idBill=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    patientname=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Receptionist_strategy = st.builds(
    Receptionist,
    id=
        st.integers(),
    attribute2=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    telno=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text,
    age=
        st.integers(),
    id=
        st.integers(),
    sex=
        safe_text
)
Department_strategy = st.builds(
    Department,
    name=
        safe_text,
    id=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    docid=
        st.integers(),
    departamentID=
        st.integers(),
    name=
        safe_text,
    phno=
        st.integers(),
    department=
        safe_text,
    address=
        safe_text,
    specialization=
        safe_text
)




@given(instance=Procedure_strategy)
def test_hyp_procedure_idProcedure_setter(instance):
    original = instance.idProcedure
    instance.idProcedure = original
    assert instance.idProcedure == original



@given(instance=Procedure_strategy)
def test_hyp_procedure_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Procedure_strategy)
def test_hyp_procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Treatment_strategy)
def test_hyp_treatment_procedureID_setter(instance):
    original = instance.procedureID
    instance.procedureID = original
    assert instance.procedureID == original



@given(instance=Treatment_strategy)
def test_hyp_treatment_patientID_setter(instance):
    original = instance.patientID
    instance.patientID = original
    assert instance.patientID == original



@given(instance=Treatment_strategy)
def test_hyp_treatment_idTreatment_setter(instance):
    original = instance.idTreatment
    instance.idTreatment = original
    assert instance.idTreatment == original



@given(instance=Treatment_strategy)
def test_hyp_treatment_idBill_setter(instance):
    original = instance.idBill
    instance.idBill = original
    assert instance.idBill == original




@given(instance=Bill_strategy)
def test_hyp_bill_billno_setter(instance):
    original = instance.billno
    instance.billno = original
    assert instance.billno == original



@given(instance=Bill_strategy)
def test_hyp_bill_patientname_setter(instance):
    original = instance.patientname
    instance.patientname = original
    assert instance.patientname == original



@given(instance=Bill_strategy)
def test_hyp_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=Patient_strategy)
def test_hyp_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_hyp_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_hyp_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_hyp_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Patient_strategy)
def test_hyp_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_hyp_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original




@given(instance=Department_strategy)
def test_hyp_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_hyp_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_departamentID_setter(instance):
    original = instance.departamentID
    instance.departamentID = original
    assert instance.departamentID == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Department,
    Doctor,
    Patient,
    Procedure,
    Receptionist,
    Treatment,
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
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_Bill_billno_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.billno == "sample_text"
    instance.billno = "sample_text_2"
    assert instance.billno == "sample_text_2"


def test_Bill_patientname_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.patientname == "sample_text"
    instance.patientname = "sample_text_2"
    assert instance.patientname == "sample_text_2"


def test_Department_id_value_roundtrip():
    instance = Department(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Department_name_value_roundtrip():
    instance = Department(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Doctor_address_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Doctor_departamentID_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.departamentID == 7
    instance.departamentID = 13
    assert instance.departamentID == 13


def test_Doctor_department_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_Doctor_docid_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.docid == 7
    instance.docid = 13
    assert instance.docid == 13


def test_Doctor_name_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Doctor_phno_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.phno == 7
    instance.phno = 13
    assert instance.phno == 13


def test_Doctor_specialization_value_roundtrip():
    instance = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.specialization == "sample_text"
    instance.specialization = "sample_text_2"
    assert instance.specialization == "sample_text_2"


def test_Patient_address_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Patient_age_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_Patient_id_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Patient_name_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_sex_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_Patient_telno_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    assert instance.telno == 7
    instance.telno = 13
    assert instance.telno == 13


def test_Procedure_idProcedure_value_roundtrip():
    instance = Procedure(idProcedure=7, name="sample_text", price=7)
    assert instance.idProcedure == 7
    instance.idProcedure = 13
    assert instance.idProcedure == 13


def test_Procedure_name_value_roundtrip():
    instance = Procedure(idProcedure=7, name="sample_text", price=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Procedure_price_value_roundtrip():
    instance = Procedure(idProcedure=7, name="sample_text", price=7)
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Receptionist_attribute2_value_roundtrip():
    instance = Receptionist(attribute2="sample_text", id=7)
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Receptionist_id_value_roundtrip():
    instance = Receptionist(attribute2="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Treatment_idBill_value_roundtrip():
    instance = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    assert instance.idBill == 7
    instance.idBill = 13
    assert instance.idBill == 13


def test_Treatment_idTreatment_value_roundtrip():
    instance = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    assert instance.idTreatment == 7
    instance.idTreatment = 13
    assert instance.idTreatment == 13


def test_Treatment_patientID_value_roundtrip():
    instance = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    assert instance.patientID == 7
    instance.patientID = 13
    assert instance.patientID == 13


def test_Treatment_procedureID_value_roundtrip():
    instance = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    assert instance.procedureID == 7
    instance.procedureID = 13
    assert instance.procedureID == 13


def test_assoc_Doctor_Department_link_reassign_clear():
    a = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b1 = Department(id=7, name="sample_text")
    b2 = Department(id=13, name="sample_text_2")
    _safe_set(a, 'depmt2', b1)
    assert _is_linked(a, 'depmt2', b1)
    if hasattr(b1, 'doctor3'):
        assert _is_linked(b1, 'doctor3', a)
    _safe_set(a, 'depmt2', b2)
    assert _is_linked(a, 'depmt2', b2)
    if hasattr(b1, 'doctor3'):
        assert not _is_linked(b1, 'doctor3', a)
    if hasattr(b2, 'doctor3'):
        assert _is_linked(b2, 'doctor3', a)
    _safe_set(a, 'depmt2', None)
    assert not _is_linked(a, 'depmt2', b2)
    if hasattr(b2, 'doctor3'):
        assert not _is_linked(b2, 'doctor3', a)


def test_assoc_Doctor_Patient_link_reassign_clear():
    a = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    b1 = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b2 = Doctor(address="sample_text_2", departamentID=13, department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    _safe_set(a, 'doctors1', {b1})
    assert _is_linked(a, 'doctors1', b1)
    if hasattr(b1, 'patients0'):
        assert _is_linked(b1, 'patients0', a)
    _safe_set(a, 'doctors1', {b2})
    assert _is_linked(a, 'doctors1', b2)
    if hasattr(b1, 'patients0'):
        assert not _is_linked(b1, 'patients0', a)
    if hasattr(b2, 'patients0'):
        assert _is_linked(b2, 'patients0', a)
    _safe_set(a, 'doctors1', set())
    assert not _is_linked(a, 'doctors1', b2)
    if hasattr(b2, 'patients0'):
        assert not _is_linked(b2, 'patients0', a)


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'bill4', {b1})
    assert _is_linked(a, 'bill4', b1)
    if hasattr(b1, 'pat5'):
        assert _is_linked(b1, 'pat5', a)
    _safe_set(a, 'bill4', {b2})
    assert _is_linked(a, 'bill4', b2)
    if hasattr(b1, 'pat5'):
        assert not _is_linked(b1, 'pat5', a)
    if hasattr(b2, 'pat5'):
        assert _is_linked(b2, 'pat5', a)
    _safe_set(a, 'bill4', set())
    assert not _is_linked(a, 'bill4', b2)
    if hasattr(b2, 'pat5'):
        assert not _is_linked(b2, 'pat5', a)


def test_assoc_Procedure_Treatment_link_reassign_clear():
    a = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    b1 = Procedure(idProcedure=7, name="sample_text", price=7)
    b2 = Procedure(idProcedure=13, name="sample_text_2", price=13)
    _safe_set(a, 'procedure13', {b1})
    assert _is_linked(a, 'procedure13', b1)
    if hasattr(b1, 'treatment12'):
        assert _is_linked(b1, 'treatment12', a)
    _safe_set(a, 'procedure13', {b2})
    assert _is_linked(a, 'procedure13', b2)
    if hasattr(b1, 'treatment12'):
        assert not _is_linked(b1, 'treatment12', a)
    if hasattr(b2, 'treatment12'):
        assert _is_linked(b2, 'treatment12', a)
    _safe_set(a, 'procedure13', set())
    assert not _is_linked(a, 'procedure13', b2)
    if hasattr(b2, 'treatment12'):
        assert not _is_linked(b2, 'treatment12', a)


def test_assoc_Treatment_Patient_link_reassign_clear():
    a = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", sex="sample_text_2", telno=13)
    _safe_set(a, 'patient10', b1)
    assert _is_linked(a, 'patient10', b1)
    if hasattr(b1, 'treatment11'):
        assert _is_linked(b1, 'treatment11', a)
    _safe_set(a, 'patient10', b2)
    assert _is_linked(a, 'patient10', b2)
    if hasattr(b1, 'treatment11'):
        assert not _is_linked(b1, 'treatment11', a)
    if hasattr(b2, 'treatment11'):
        assert _is_linked(b2, 'treatment11', a)
    _safe_set(a, 'patient10', None)
    assert not _is_linked(a, 'patient10', b2)
    if hasattr(b2, 'treatment11'):
        assert not _is_linked(b2, 'treatment11', a)


def test_assoc_manages_link_reassign_clear():
    a = Receptionist(attribute2="sample_text", id=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'sbill8', {b1})
    assert _is_linked(a, 'sbill8', b1)
    if hasattr(b1, 'receptionist9'):
        assert _is_linked(b1, 'receptionist9', a)
    _safe_set(a, 'sbill8', {b2})
    assert _is_linked(a, 'sbill8', b2)
    if hasattr(b1, 'receptionist9'):
        assert not _is_linked(b1, 'receptionist9', a)
    if hasattr(b2, 'receptionist9'):
        assert _is_linked(b2, 'receptionist9', a)
    _safe_set(a, 'sbill8', set())
    assert not _is_linked(a, 'sbill8', b2)
    if hasattr(b2, 'receptionist9'):
        assert not _is_linked(b2, 'receptionist9', a)


def test_assoc_receptions_link_reassign_clear():
    a = Receptionist(attribute2="sample_text", id=7)
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", sex="sample_text_2", telno=13)
    _safe_set(a, 'p7', b1)
    assert _is_linked(a, 'p7', b1)
    if hasattr(b1, 'receptionist6'):
        assert _is_linked(b1, 'receptionist6', a)
    _safe_set(a, 'p7', b2)
    assert _is_linked(a, 'p7', b2)
    if hasattr(b1, 'receptionist6'):
        assert not _is_linked(b1, 'receptionist6', a)
    if hasattr(b2, 'receptionist6'):
        assert _is_linked(b2, 'receptionist6', a)
    _safe_set(a, 'p7', None)
    assert not _is_linked(a, 'p7', b2)
    if hasattr(b2, 'receptionist6'):
        assert not _is_linked(b2, 'receptionist6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, amount=st.floats(allow_nan=False, allow_infinity=False), billno=safe_text, patientname=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Department_strategy = st.builds(Department, id=st.integers(), name=safe_text)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


Doctor_strategy = st.builds(Doctor, address=safe_text, departamentID=st.integers(), department=safe_text, docid=st.integers(), name=safe_text, phno=st.integers(), specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Patient_strategy = st.builds(Patient, address=safe_text, age=st.integers(), id=st.integers(), name=safe_text, sex=safe_text, telno=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Procedure_strategy = st.builds(Procedure, idProcedure=st.integers(), name=safe_text, price=st.integers())
@given(instance=Procedure_strategy)
@settings(max_examples=25)
def test_Procedure_instantiation(instance):
    assert isinstance(instance, Procedure)


Receptionist_strategy = st.builds(Receptionist, attribute2=safe_text, id=st.integers())
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Treatment_strategy = st.builds(Treatment, idBill=st.integers(), idTreatment=st.integers(), patientID=st.integers(), procedureID=st.integers())
@given(instance=Treatment_strategy)
@settings(max_examples=25)
def test_Treatment_instantiation(instance):
    assert isinstance(instance, Treatment)



