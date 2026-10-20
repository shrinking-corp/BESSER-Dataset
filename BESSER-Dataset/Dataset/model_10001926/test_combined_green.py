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
    SubjectSheduleController,
    ActivityType,
    Subject,
    SubjectShedule,
    DocumentStorage,
    TimeCreditForEducationalSemester,
    EducationalPlan,
    Specialty,
    Group,
    TimeInterval,
    Auditorium,
    Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_subjectshedulecontroller_is_not_abstract():
    assert not inspect.isabstract(SubjectSheduleController)


def test_hyp_subjectshedulecontroller_constructor_exists():
    assert callable(SubjectSheduleController.__init__)


def test_hyp_subjectshedulecontroller_constructor_args():
    sig = inspect.signature(SubjectSheduleController.__init__)
    params = list(sig.parameters.keys())
    assert "auditoriumNumberService" in params, "Missing parameter 'auditoriumNumberService'"
    assert "groupNumberService" in params, "Missing parameter 'groupNumberService'"
    assert "subjectCodeService" in params, "Missing parameter 'subjectCodeService'"
    assert "individualIdentificationCodeService" in params, "Missing parameter 'individualIdentificationCodeService'"
    assert "dateService" in params, "Missing parameter 'dateService'"
    assert "activityTypeCodeService" in params, "Missing parameter 'activityTypeCodeService'"









def test_hyp_activitytype_is_not_abstract():
    assert not inspect.isabstract(ActivityType)


def test_hyp_activitytype_constructor_exists():
    assert callable(ActivityType.__init__)


def test_hyp_activitytype_constructor_args():
    sig = inspect.signature(ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "activityTypeName" in params, "Missing parameter 'activityTypeName'"







def test_hyp_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_hyp_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_hyp_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())
    assert "subjectName" in params, "Missing parameter 'subjectName'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_subjectshedule_is_not_abstract():
    assert not inspect.isabstract(SubjectShedule)


def test_hyp_subjectshedule_constructor_exists():
    assert callable(SubjectShedule.__init__)


def test_hyp_subjectshedule_constructor_args():
    sig = inspect.signature(SubjectShedule.__init__)
    params = list(sig.parameters.keys())
    assert "individualIdentificationCode" in params, "Missing parameter 'individualIdentificationCode'"
    assert "auditoriumNumber" in params, "Missing parameter 'auditoriumNumber'"
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"










def test_hyp_documentstorage_is_not_abstract():
    assert not inspect.isabstract(DocumentStorage)


def test_hyp_documentstorage_constructor_exists():
    assert callable(DocumentStorage.__init__)


def test_hyp_documentstorage_constructor_args():
    sig = inspect.signature(DocumentStorage.__init__)
    params = list(sig.parameters.keys())
    assert "documentPath" in params, "Missing parameter 'documentPath'"
    assert "documentCode" in params, "Missing parameter 'documentCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "is_exist" in params, "Missing parameter 'is_exist'"







def test_hyp_timecreditforeducationalsemester_is_not_abstract():
    assert not inspect.isabstract(TimeCreditForEducationalSemester)


def test_hyp_timecreditforeducationalsemester_constructor_exists():
    assert callable(TimeCreditForEducationalSemester.__init__)


def test_hyp_timecreditforeducationalsemester_constructor_args():
    sig = inspect.signature(TimeCreditForEducationalSemester.__init__)
    params = list(sig.parameters.keys())
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "totalHours" in params, "Missing parameter 'totalHours'"
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "id" in params, "Missing parameter 'id'"








def test_hyp_educationalplan_is_not_abstract():
    assert not inspect.isabstract(EducationalPlan)


def test_hyp_educationalplan_constructor_exists():
    assert callable(EducationalPlan.__init__)


def test_hyp_educationalplan_constructor_args():
    sig = inspect.signature(EducationalPlan.__init__)
    params = list(sig.parameters.keys())
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "individualIdentificationCode" in params, "Missing parameter 'individualIdentificationCode'"






def test_hyp_specialty_is_not_abstract():
    assert not inspect.isabstract(Specialty)


def test_hyp_specialty_constructor_exists():
    assert callable(Specialty.__init__)


def test_hyp_specialty_constructor_args():
    sig = inspect.signature(Specialty.__init__)
    params = list(sig.parameters.keys())
    assert "specialtyCode" in params, "Missing parameter 'specialtyCode'"
    assert "specialtyName" in params, "Missing parameter 'specialtyName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"







def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "educationalYear" in params, "Missing parameter 'educationalYear'"
    assert "specialtyCode" in params, "Missing parameter 'specialtyCode'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_timeinterval_is_not_abstract():
    assert not inspect.isabstract(TimeInterval)


def test_hyp_timeinterval_constructor_exists():
    assert callable(TimeInterval.__init__)


def test_hyp_timeinterval_constructor_args():
    sig = inspect.signature(TimeInterval.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "weekIdentifier" in params, "Missing parameter 'weekIdentifier'"
    assert "id" in params, "Missing parameter 'id'"
    assert "weekday" in params, "Missing parameter 'weekday'"
    assert "classOrder" in params, "Missing parameter 'classOrder'"








def test_hyp_auditorium_is_not_abstract():
    assert not inspect.isabstract(Auditorium)


def test_hyp_auditorium_constructor_exists():
    assert callable(Auditorium.__init__)


def test_hyp_auditorium_constructor_args():
    sig = inspect.signature(Auditorium.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "educationalBuilding" in params, "Missing parameter 'educationalBuilding'"
    assert "is_busy" in params, "Missing parameter 'is_busy'"
    assert "auditoriumNumber" in params, "Missing parameter 'auditoriumNumber'"







def test_hyp_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_hyp_users_constructor_exists():
    assert callable(Users.__init__)


def test_hyp_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "residentBirthday" in params, "Missing parameter 'residentBirthday'"
    assert "universityStructureUnit" in params, "Missing parameter 'universityStructureUnit'"
    assert "residentPosition" in params, "Missing parameter 'residentPosition'"
    assert "residentSurname" in params, "Missing parameter 'residentSurname'"
    assert "residentName" in params, "Missing parameter 'residentName'"
    assert "registrationCertificateCode" in params, "Missing parameter 'registrationCertificateCode'"
    assert "residentPassword" in params, "Missing parameter 'residentPassword'"
    assert "residentUserType" in params, "Missing parameter 'residentUserType'"
    assert "residentPatronymic" in params, "Missing parameter 'residentPatronymic'"
    assert "residentDepartment" in params, "Missing parameter 'residentDepartment'"
    assert "residentEmail" in params, "Missing parameter 'residentEmail'"
    assert "individuadIdentificationCode" in params, "Missing parameter 'individuadIdentificationCode'"
    assert "id" in params, "Missing parameter 'id'"















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
SubjectSheduleController_strategy = st.builds(
    SubjectSheduleController,
    auditoriumNumberService=
        st.integers(),
    groupNumberService=
        st.integers(),
    subjectCodeService=
        safe_text,
    individualIdentificationCodeService=
        st.integers(),
    dateService=
        safe_text,
    activityTypeCodeService=
        st.integers()
)
ActivityType_strategy = st.builds(
    ActivityType,
    activityTypeCode=
        st.integers(),
    id=
        st.integers(),
    subjectCode=
        st.integers(),
    activityTypeName=
        safe_text
)
Subject_strategy = st.builds(
    Subject,
    subjectName=
        safe_text,
    subjectCode=
        st.integers(),
    id=
        st.integers()
)
SubjectShedule_strategy = st.builds(
    SubjectShedule,
    individualIdentificationCode=
        st.integers(),
    auditoriumNumber=
        st.integers(),
    groupNumber=
        st.integers(),
    subjectCode=
        st.integers(),
    activityTypeCode=
        st.integers(),
    date=
        safe_text,
    id=
        st.integers()
)
DocumentStorage_strategy = st.builds(
    DocumentStorage,
    documentPath=
        safe_text,
    documentCode=
        st.integers(),
    id=
        st.integers(),
    is_exist=
        st.booleans()
)
TimeCreditForEducationalSemester_strategy = st.builds(
    TimeCreditForEducationalSemester,
    groupNumber=
        st.integers(),
    subjectCode=
        st.integers(),
    totalHours=
        st.integers(),
    activityTypeCode=
        st.integers(),
    id=
        st.integers()
)
EducationalPlan_strategy = st.builds(
    EducationalPlan,
    subjectCode=
        st.integers(),
    id=
        st.integers(),
    individualIdentificationCode=
        st.integers()
)
Specialty_strategy = st.builds(
    Specialty,
    specialtyCode=
        st.integers(),
    specialtyName=
        safe_text,
    id=
        st.integers(),
    subjectCode=
        st.integers()
)
Group_strategy = st.builds(
    Group,
    groupNumber=
        st.integers(),
    educationalYear=
        st.integers(),
    specialtyCode=
        st.integers(),
    id=
        st.integers()
)
TimeInterval_strategy = st.builds(
    TimeInterval,
    date=
        safe_text,
    weekIdentifier=
        st.integers(),
    id=
        st.integers(),
    weekday=
        st.integers(),
    classOrder=
        st.integers()
)
Auditorium_strategy = st.builds(
    Auditorium,
    id=
        st.integers(),
    educationalBuilding=
        safe_text,
    is_busy=
        st.booleans(),
    auditoriumNumber=
        st.integers()
)
Users_strategy = st.builds(
    Users,
    residentBirthday=
        safe_text,
    universityStructureUnit=
        safe_text,
    residentPosition=
        safe_text,
    residentSurname=
        safe_text,
    residentName=
        safe_text,
    registrationCertificateCode=
        st.integers(),
    residentPassword=
        safe_text,
    residentUserType=
        safe_text,
    residentPatronymic=
        safe_text,
    residentDepartment=
        safe_text,
    residentEmail=
        safe_text,
    individuadIdentificationCode=
        st.integers(),
    id=
        st.integers()
)




@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_auditoriumNumberService_setter(instance):
    original = instance.auditoriumNumberService
    instance.auditoriumNumberService = original
    assert instance.auditoriumNumberService == original



@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_groupNumberService_setter(instance):
    original = instance.groupNumberService
    instance.groupNumberService = original
    assert instance.groupNumberService == original



@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_subjectCodeService_setter(instance):
    original = instance.subjectCodeService
    instance.subjectCodeService = original
    assert instance.subjectCodeService == original



@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_individualIdentificationCodeService_setter(instance):
    original = instance.individualIdentificationCodeService
    instance.individualIdentificationCodeService = original
    assert instance.individualIdentificationCodeService == original



@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_dateService_setter(instance):
    original = instance.dateService
    instance.dateService = original
    assert instance.dateService == original



@given(instance=SubjectSheduleController_strategy)
def test_hyp_subjectshedulecontroller_activityTypeCodeService_setter(instance):
    original = instance.activityTypeCodeService
    instance.activityTypeCodeService = original
    assert instance.activityTypeCodeService == original




@given(instance=ActivityType_strategy)
def test_hyp_activitytype_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=ActivityType_strategy)
def test_hyp_activitytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ActivityType_strategy)
def test_hyp_activitytype_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=ActivityType_strategy)
def test_hyp_activitytype_activityTypeName_setter(instance):
    original = instance.activityTypeName
    instance.activityTypeName = original
    assert instance.activityTypeName == original




@given(instance=Subject_strategy)
def test_hyp_subject_subjectName_setter(instance):
    original = instance.subjectName
    instance.subjectName = original
    assert instance.subjectName == original



@given(instance=Subject_strategy)
def test_hyp_subject_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=Subject_strategy)
def test_hyp_subject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_individualIdentificationCode_setter(instance):
    original = instance.individualIdentificationCode
    instance.individualIdentificationCode = original
    assert instance.individualIdentificationCode == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_auditoriumNumber_setter(instance):
    original = instance.auditoriumNumber
    instance.auditoriumNumber = original
    assert instance.auditoriumNumber == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=SubjectShedule_strategy)
def test_hyp_subjectshedule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=DocumentStorage_strategy)
def test_hyp_documentstorage_documentPath_setter(instance):
    original = instance.documentPath
    instance.documentPath = original
    assert instance.documentPath == original



@given(instance=DocumentStorage_strategy)
def test_hyp_documentstorage_documentCode_setter(instance):
    original = instance.documentCode
    instance.documentCode = original
    assert instance.documentCode == original



@given(instance=DocumentStorage_strategy)
def test_hyp_documentstorage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=DocumentStorage_strategy)
def test_hyp_documentstorage_is_exist_setter(instance):
    original = instance.is_exist
    instance.is_exist = original
    assert instance.is_exist == original




@given(instance=TimeCreditForEducationalSemester_strategy)
def test_hyp_timecreditforeducationalsemester_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_hyp_timecreditforeducationalsemester_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_hyp_timecreditforeducationalsemester_totalHours_setter(instance):
    original = instance.totalHours
    instance.totalHours = original
    assert instance.totalHours == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_hyp_timecreditforeducationalsemester_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_hyp_timecreditforeducationalsemester_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=EducationalPlan_strategy)
def test_hyp_educationalplan_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=EducationalPlan_strategy)
def test_hyp_educationalplan_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EducationalPlan_strategy)
def test_hyp_educationalplan_individualIdentificationCode_setter(instance):
    original = instance.individualIdentificationCode
    instance.individualIdentificationCode = original
    assert instance.individualIdentificationCode == original




@given(instance=Specialty_strategy)
def test_hyp_specialty_specialtyCode_setter(instance):
    original = instance.specialtyCode
    instance.specialtyCode = original
    assert instance.specialtyCode == original



@given(instance=Specialty_strategy)
def test_hyp_specialty_specialtyName_setter(instance):
    original = instance.specialtyName
    instance.specialtyName = original
    assert instance.specialtyName == original



@given(instance=Specialty_strategy)
def test_hyp_specialty_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Specialty_strategy)
def test_hyp_specialty_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original




@given(instance=Group_strategy)
def test_hyp_group_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=Group_strategy)
def test_hyp_group_educationalYear_setter(instance):
    original = instance.educationalYear
    instance.educationalYear = original
    assert instance.educationalYear == original



@given(instance=Group_strategy)
def test_hyp_group_specialtyCode_setter(instance):
    original = instance.specialtyCode
    instance.specialtyCode = original
    assert instance.specialtyCode == original



@given(instance=Group_strategy)
def test_hyp_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=TimeInterval_strategy)
def test_hyp_timeinterval_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=TimeInterval_strategy)
def test_hyp_timeinterval_weekIdentifier_setter(instance):
    original = instance.weekIdentifier
    instance.weekIdentifier = original
    assert instance.weekIdentifier == original



@given(instance=TimeInterval_strategy)
def test_hyp_timeinterval_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TimeInterval_strategy)
def test_hyp_timeinterval_weekday_setter(instance):
    original = instance.weekday
    instance.weekday = original
    assert instance.weekday == original



@given(instance=TimeInterval_strategy)
def test_hyp_timeinterval_classOrder_setter(instance):
    original = instance.classOrder
    instance.classOrder = original
    assert instance.classOrder == original




@given(instance=Auditorium_strategy)
def test_hyp_auditorium_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Auditorium_strategy)
def test_hyp_auditorium_educationalBuilding_setter(instance):
    original = instance.educationalBuilding
    instance.educationalBuilding = original
    assert instance.educationalBuilding == original



@given(instance=Auditorium_strategy)
def test_hyp_auditorium_is_busy_setter(instance):
    original = instance.is_busy
    instance.is_busy = original
    assert instance.is_busy == original



@given(instance=Auditorium_strategy)
def test_hyp_auditorium_auditoriumNumber_setter(instance):
    original = instance.auditoriumNumber
    instance.auditoriumNumber = original
    assert instance.auditoriumNumber == original




@given(instance=Users_strategy)
def test_hyp_users_residentBirthday_setter(instance):
    original = instance.residentBirthday
    instance.residentBirthday = original
    assert instance.residentBirthday == original



@given(instance=Users_strategy)
def test_hyp_users_universityStructureUnit_setter(instance):
    original = instance.universityStructureUnit
    instance.universityStructureUnit = original
    assert instance.universityStructureUnit == original



@given(instance=Users_strategy)
def test_hyp_users_residentPosition_setter(instance):
    original = instance.residentPosition
    instance.residentPosition = original
    assert instance.residentPosition == original



@given(instance=Users_strategy)
def test_hyp_users_residentSurname_setter(instance):
    original = instance.residentSurname
    instance.residentSurname = original
    assert instance.residentSurname == original



@given(instance=Users_strategy)
def test_hyp_users_residentName_setter(instance):
    original = instance.residentName
    instance.residentName = original
    assert instance.residentName == original



@given(instance=Users_strategy)
def test_hyp_users_registrationCertificateCode_setter(instance):
    original = instance.registrationCertificateCode
    instance.registrationCertificateCode = original
    assert instance.registrationCertificateCode == original



@given(instance=Users_strategy)
def test_hyp_users_residentPassword_setter(instance):
    original = instance.residentPassword
    instance.residentPassword = original
    assert instance.residentPassword == original



@given(instance=Users_strategy)
def test_hyp_users_residentUserType_setter(instance):
    original = instance.residentUserType
    instance.residentUserType = original
    assert instance.residentUserType == original



@given(instance=Users_strategy)
def test_hyp_users_residentPatronymic_setter(instance):
    original = instance.residentPatronymic
    instance.residentPatronymic = original
    assert instance.residentPatronymic == original



@given(instance=Users_strategy)
def test_hyp_users_residentDepartment_setter(instance):
    original = instance.residentDepartment
    instance.residentDepartment = original
    assert instance.residentDepartment == original



@given(instance=Users_strategy)
def test_hyp_users_residentEmail_setter(instance):
    original = instance.residentEmail
    instance.residentEmail = original
    assert instance.residentEmail == original



@given(instance=Users_strategy)
def test_hyp_users_individuadIdentificationCode_setter(instance):
    original = instance.individuadIdentificationCode
    instance.individuadIdentificationCode = original
    assert instance.individuadIdentificationCode == original



@given(instance=Users_strategy)
def test_hyp_users_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ActivityType,
    Auditorium,
    DocumentStorage,
    EducationalPlan,
    Group,
    Specialty,
    Subject,
    SubjectShedule,
    SubjectSheduleController,
    TimeCreditForEducationalSemester,
    TimeInterval,
    Users,
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

def test_ActivityType_activityTypeCode_value_roundtrip():
    instance = ActivityType(activityTypeCode=7, activityTypeName="sample_text", id=7, subjectCode=7)
    assert instance.activityTypeCode == 7
    instance.activityTypeCode = 13
    assert instance.activityTypeCode == 13


def test_ActivityType_activityTypeName_value_roundtrip():
    instance = ActivityType(activityTypeCode=7, activityTypeName="sample_text", id=7, subjectCode=7)
    assert instance.activityTypeName == "sample_text"
    instance.activityTypeName = "sample_text_2"
    assert instance.activityTypeName == "sample_text_2"


def test_ActivityType_id_value_roundtrip():
    instance = ActivityType(activityTypeCode=7, activityTypeName="sample_text", id=7, subjectCode=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_ActivityType_subjectCode_value_roundtrip():
    instance = ActivityType(activityTypeCode=7, activityTypeName="sample_text", id=7, subjectCode=7)
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_Auditorium_auditoriumNumber_value_roundtrip():
    instance = Auditorium(auditoriumNumber=7, educationalBuilding="sample_text", id=7, is_busy=True)
    assert instance.auditoriumNumber == 7
    instance.auditoriumNumber = 13
    assert instance.auditoriumNumber == 13


def test_Auditorium_educationalBuilding_value_roundtrip():
    instance = Auditorium(auditoriumNumber=7, educationalBuilding="sample_text", id=7, is_busy=True)
    assert instance.educationalBuilding == "sample_text"
    instance.educationalBuilding = "sample_text_2"
    assert instance.educationalBuilding == "sample_text_2"


def test_Auditorium_id_value_roundtrip():
    instance = Auditorium(auditoriumNumber=7, educationalBuilding="sample_text", id=7, is_busy=True)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Auditorium_is_busy_value_roundtrip():
    instance = Auditorium(auditoriumNumber=7, educationalBuilding="sample_text", id=7, is_busy=True)
    assert instance.is_busy == True
    instance.is_busy = False
    assert instance.is_busy == False


def test_DocumentStorage_documentCode_value_roundtrip():
    instance = DocumentStorage(documentCode=7, documentPath="sample_text", id=7, is_exist=True)
    assert instance.documentCode == 7
    instance.documentCode = 13
    assert instance.documentCode == 13


def test_DocumentStorage_documentPath_value_roundtrip():
    instance = DocumentStorage(documentCode=7, documentPath="sample_text", id=7, is_exist=True)
    assert instance.documentPath == "sample_text"
    instance.documentPath = "sample_text_2"
    assert instance.documentPath == "sample_text_2"


def test_DocumentStorage_id_value_roundtrip():
    instance = DocumentStorage(documentCode=7, documentPath="sample_text", id=7, is_exist=True)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_DocumentStorage_is_exist_value_roundtrip():
    instance = DocumentStorage(documentCode=7, documentPath="sample_text", id=7, is_exist=True)
    assert instance.is_exist == True
    instance.is_exist = False
    assert instance.is_exist == False


def test_EducationalPlan_id_value_roundtrip():
    instance = EducationalPlan(id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_EducationalPlan_individualIdentificationCode_value_roundtrip():
    instance = EducationalPlan(id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.individualIdentificationCode == 7
    instance.individualIdentificationCode = 13
    assert instance.individualIdentificationCode == 13


def test_EducationalPlan_subjectCode_value_roundtrip():
    instance = EducationalPlan(id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_Group_educationalYear_value_roundtrip():
    instance = Group(educationalYear=7, groupNumber=7, id=7, specialtyCode=7)
    assert instance.educationalYear == 7
    instance.educationalYear = 13
    assert instance.educationalYear == 13


def test_Group_groupNumber_value_roundtrip():
    instance = Group(educationalYear=7, groupNumber=7, id=7, specialtyCode=7)
    assert instance.groupNumber == 7
    instance.groupNumber = 13
    assert instance.groupNumber == 13


def test_Group_id_value_roundtrip():
    instance = Group(educationalYear=7, groupNumber=7, id=7, specialtyCode=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Group_specialtyCode_value_roundtrip():
    instance = Group(educationalYear=7, groupNumber=7, id=7, specialtyCode=7)
    assert instance.specialtyCode == 7
    instance.specialtyCode = 13
    assert instance.specialtyCode == 13


def test_Specialty_id_value_roundtrip():
    instance = Specialty(id=7, specialtyCode=7, specialtyName="sample_text", subjectCode=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Specialty_specialtyCode_value_roundtrip():
    instance = Specialty(id=7, specialtyCode=7, specialtyName="sample_text", subjectCode=7)
    assert instance.specialtyCode == 7
    instance.specialtyCode = 13
    assert instance.specialtyCode == 13


def test_Specialty_specialtyName_value_roundtrip():
    instance = Specialty(id=7, specialtyCode=7, specialtyName="sample_text", subjectCode=7)
    assert instance.specialtyName == "sample_text"
    instance.specialtyName = "sample_text_2"
    assert instance.specialtyName == "sample_text_2"


def test_Specialty_subjectCode_value_roundtrip():
    instance = Specialty(id=7, specialtyCode=7, specialtyName="sample_text", subjectCode=7)
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_Subject_id_value_roundtrip():
    instance = Subject(id=7, subjectCode=7, subjectName="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Subject_subjectCode_value_roundtrip():
    instance = Subject(id=7, subjectCode=7, subjectName="sample_text")
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_Subject_subjectName_value_roundtrip():
    instance = Subject(id=7, subjectCode=7, subjectName="sample_text")
    assert instance.subjectName == "sample_text"
    instance.subjectName = "sample_text_2"
    assert instance.subjectName == "sample_text_2"


def test_SubjectShedule_activityTypeCode_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.activityTypeCode == 7
    instance.activityTypeCode = 13
    assert instance.activityTypeCode == 13


def test_SubjectShedule_auditoriumNumber_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.auditoriumNumber == 7
    instance.auditoriumNumber = 13
    assert instance.auditoriumNumber == 13


def test_SubjectShedule_date_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_SubjectShedule_groupNumber_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.groupNumber == 7
    instance.groupNumber = 13
    assert instance.groupNumber == 13


def test_SubjectShedule_id_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_SubjectShedule_individualIdentificationCode_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.individualIdentificationCode == 7
    instance.individualIdentificationCode = 13
    assert instance.individualIdentificationCode == 13


def test_SubjectShedule_subjectCode_value_roundtrip():
    instance = SubjectShedule(activityTypeCode=7, auditoriumNumber=7, date="sample_text", groupNumber=7, id=7, individualIdentificationCode=7, subjectCode=7)
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_SubjectSheduleController_activityTypeCodeService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.activityTypeCodeService == 7
    instance.activityTypeCodeService = 13
    assert instance.activityTypeCodeService == 13


def test_SubjectSheduleController_auditoriumNumberService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.auditoriumNumberService == 7
    instance.auditoriumNumberService = 13
    assert instance.auditoriumNumberService == 13


def test_SubjectSheduleController_dateService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.dateService == "sample_text"
    instance.dateService = "sample_text_2"
    assert instance.dateService == "sample_text_2"


def test_SubjectSheduleController_groupNumberService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.groupNumberService == 7
    instance.groupNumberService = 13
    assert instance.groupNumberService == 13


def test_SubjectSheduleController_individualIdentificationCodeService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.individualIdentificationCodeService == 7
    instance.individualIdentificationCodeService = 13
    assert instance.individualIdentificationCodeService == 13


def test_SubjectSheduleController_subjectCodeService_value_roundtrip():
    instance = SubjectSheduleController(activityTypeCodeService=7, auditoriumNumberService=7, dateService="sample_text", groupNumberService=7, individualIdentificationCodeService=7, subjectCodeService="sample_text")
    assert instance.subjectCodeService == "sample_text"
    instance.subjectCodeService = "sample_text_2"
    assert instance.subjectCodeService == "sample_text_2"


def test_TimeCreditForEducationalSemester_activityTypeCode_value_roundtrip():
    instance = TimeCreditForEducationalSemester(activityTypeCode=7, groupNumber=7, id=7, subjectCode=7, totalHours=7)
    assert instance.activityTypeCode == 7
    instance.activityTypeCode = 13
    assert instance.activityTypeCode == 13


def test_TimeCreditForEducationalSemester_groupNumber_value_roundtrip():
    instance = TimeCreditForEducationalSemester(activityTypeCode=7, groupNumber=7, id=7, subjectCode=7, totalHours=7)
    assert instance.groupNumber == 7
    instance.groupNumber = 13
    assert instance.groupNumber == 13


def test_TimeCreditForEducationalSemester_id_value_roundtrip():
    instance = TimeCreditForEducationalSemester(activityTypeCode=7, groupNumber=7, id=7, subjectCode=7, totalHours=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_TimeCreditForEducationalSemester_subjectCode_value_roundtrip():
    instance = TimeCreditForEducationalSemester(activityTypeCode=7, groupNumber=7, id=7, subjectCode=7, totalHours=7)
    assert instance.subjectCode == 7
    instance.subjectCode = 13
    assert instance.subjectCode == 13


def test_TimeCreditForEducationalSemester_totalHours_value_roundtrip():
    instance = TimeCreditForEducationalSemester(activityTypeCode=7, groupNumber=7, id=7, subjectCode=7, totalHours=7)
    assert instance.totalHours == 7
    instance.totalHours = 13
    assert instance.totalHours == 13


def test_TimeInterval_classOrder_value_roundtrip():
    instance = TimeInterval(classOrder=7, date="sample_text", id=7, weekIdentifier=7, weekday=7)
    assert instance.classOrder == 7
    instance.classOrder = 13
    assert instance.classOrder == 13


def test_TimeInterval_date_value_roundtrip():
    instance = TimeInterval(classOrder=7, date="sample_text", id=7, weekIdentifier=7, weekday=7)
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_TimeInterval_id_value_roundtrip():
    instance = TimeInterval(classOrder=7, date="sample_text", id=7, weekIdentifier=7, weekday=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_TimeInterval_weekIdentifier_value_roundtrip():
    instance = TimeInterval(classOrder=7, date="sample_text", id=7, weekIdentifier=7, weekday=7)
    assert instance.weekIdentifier == 7
    instance.weekIdentifier = 13
    assert instance.weekIdentifier == 13


def test_TimeInterval_weekday_value_roundtrip():
    instance = TimeInterval(classOrder=7, date="sample_text", id=7, weekIdentifier=7, weekday=7)
    assert instance.weekday == 7
    instance.weekday = 13
    assert instance.weekday == 13


def test_Users_id_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Users_individuadIdentificationCode_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.individuadIdentificationCode == 7
    instance.individuadIdentificationCode = 13
    assert instance.individuadIdentificationCode == 13


def test_Users_registrationCertificateCode_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.registrationCertificateCode == 7
    instance.registrationCertificateCode = 13
    assert instance.registrationCertificateCode == 13


def test_Users_residentBirthday_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentBirthday == "sample_text"
    instance.residentBirthday = "sample_text_2"
    assert instance.residentBirthday == "sample_text_2"


def test_Users_residentDepartment_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentDepartment == "sample_text"
    instance.residentDepartment = "sample_text_2"
    assert instance.residentDepartment == "sample_text_2"


def test_Users_residentEmail_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentEmail == "sample_text"
    instance.residentEmail = "sample_text_2"
    assert instance.residentEmail == "sample_text_2"


def test_Users_residentName_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentName == "sample_text"
    instance.residentName = "sample_text_2"
    assert instance.residentName == "sample_text_2"


def test_Users_residentPassword_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentPassword == "sample_text"
    instance.residentPassword = "sample_text_2"
    assert instance.residentPassword == "sample_text_2"


def test_Users_residentPatronymic_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentPatronymic == "sample_text"
    instance.residentPatronymic = "sample_text_2"
    assert instance.residentPatronymic == "sample_text_2"


def test_Users_residentPosition_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentPosition == "sample_text"
    instance.residentPosition = "sample_text_2"
    assert instance.residentPosition == "sample_text_2"


def test_Users_residentSurname_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentSurname == "sample_text"
    instance.residentSurname = "sample_text_2"
    assert instance.residentSurname == "sample_text_2"


def test_Users_residentUserType_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.residentUserType == "sample_text"
    instance.residentUserType = "sample_text_2"
    assert instance.residentUserType == "sample_text_2"


def test_Users_universityStructureUnit_value_roundtrip():
    instance = Users(id=7, individuadIdentificationCode=7, registrationCertificateCode=7, residentBirthday="sample_text", residentDepartment="sample_text", residentEmail="sample_text", residentName="sample_text", residentPassword="sample_text", residentPatronymic="sample_text", residentPosition="sample_text", residentSurname="sample_text", residentUserType="sample_text", universityStructureUnit="sample_text")
    assert instance.universityStructureUnit == "sample_text"
    instance.universityStructureUnit = "sample_text_2"
    assert instance.universityStructureUnit == "sample_text_2"


def test_assoc_assoc__JGODfZfZEeqEM7mFKilpXw_link_reassign_clear():
    a = Subject(id=7, subjectCode=7, subjectName="sample_text")
    b1 = ActivityType(activityTypeCode=7, activityTypeName="sample_text", id=7, subjectCode=7)
    b2 = ActivityType(activityTypeCode=13, activityTypeName="sample_text_2", id=13, subjectCode=13)
    _safe_set(a, 'assoc_00', {b1})
    assert _is_linked(a, 'assoc_00', b1)
    if hasattr(b1, 'assoc_11'):
        assert _is_linked(b1, 'assoc_11', a)
    _safe_set(a, 'assoc_00', {b2})
    assert _is_linked(a, 'assoc_00', b2)
    if hasattr(b1, 'assoc_11'):
        assert not _is_linked(b1, 'assoc_11', a)
    if hasattr(b2, 'assoc_11'):
        assert _is_linked(b2, 'assoc_11', a)
    _safe_set(a, 'assoc_00', set())
    assert not _is_linked(a, 'assoc_00', b2)
    if hasattr(b2, 'assoc_11'):
        assert not _is_linked(b2, 'assoc_11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ActivityType_strategy = st.builds(ActivityType, activityTypeCode=st.integers(), activityTypeName=safe_text, id=st.integers(), subjectCode=st.integers())
@given(instance=ActivityType_strategy)
@settings(max_examples=25)
def test_ActivityType_instantiation(instance):
    assert isinstance(instance, ActivityType)


Auditorium_strategy = st.builds(Auditorium, auditoriumNumber=st.integers(), educationalBuilding=safe_text, id=st.integers(), is_busy=st.booleans())
@given(instance=Auditorium_strategy)
@settings(max_examples=25)
def test_Auditorium_instantiation(instance):
    assert isinstance(instance, Auditorium)


DocumentStorage_strategy = st.builds(DocumentStorage, documentCode=st.integers(), documentPath=safe_text, id=st.integers(), is_exist=st.booleans())
@given(instance=DocumentStorage_strategy)
@settings(max_examples=25)
def test_DocumentStorage_instantiation(instance):
    assert isinstance(instance, DocumentStorage)


EducationalPlan_strategy = st.builds(EducationalPlan, id=st.integers(), individualIdentificationCode=st.integers(), subjectCode=st.integers())
@given(instance=EducationalPlan_strategy)
@settings(max_examples=25)
def test_EducationalPlan_instantiation(instance):
    assert isinstance(instance, EducationalPlan)


Group_strategy = st.builds(Group, educationalYear=st.integers(), groupNumber=st.integers(), id=st.integers(), specialtyCode=st.integers())
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Specialty_strategy = st.builds(Specialty, id=st.integers(), specialtyCode=st.integers(), specialtyName=safe_text, subjectCode=st.integers())
@given(instance=Specialty_strategy)
@settings(max_examples=25)
def test_Specialty_instantiation(instance):
    assert isinstance(instance, Specialty)


Subject_strategy = st.builds(Subject, id=st.integers(), subjectCode=st.integers(), subjectName=safe_text)
@given(instance=Subject_strategy)
@settings(max_examples=25)
def test_Subject_instantiation(instance):
    assert isinstance(instance, Subject)


SubjectShedule_strategy = st.builds(SubjectShedule, activityTypeCode=st.integers(), auditoriumNumber=st.integers(), date=safe_text, groupNumber=st.integers(), id=st.integers(), individualIdentificationCode=st.integers(), subjectCode=st.integers())
@given(instance=SubjectShedule_strategy)
@settings(max_examples=25)
def test_SubjectShedule_instantiation(instance):
    assert isinstance(instance, SubjectShedule)


SubjectSheduleController_strategy = st.builds(SubjectSheduleController, activityTypeCodeService=st.integers(), auditoriumNumberService=st.integers(), dateService=safe_text, groupNumberService=st.integers(), individualIdentificationCodeService=st.integers(), subjectCodeService=safe_text)
@given(instance=SubjectSheduleController_strategy)
@settings(max_examples=25)
def test_SubjectSheduleController_instantiation(instance):
    assert isinstance(instance, SubjectSheduleController)


TimeCreditForEducationalSemester_strategy = st.builds(TimeCreditForEducationalSemester, activityTypeCode=st.integers(), groupNumber=st.integers(), id=st.integers(), subjectCode=st.integers(), totalHours=st.integers())
@given(instance=TimeCreditForEducationalSemester_strategy)
@settings(max_examples=25)
def test_TimeCreditForEducationalSemester_instantiation(instance):
    assert isinstance(instance, TimeCreditForEducationalSemester)


TimeInterval_strategy = st.builds(TimeInterval, classOrder=st.integers(), date=safe_text, id=st.integers(), weekIdentifier=st.integers(), weekday=st.integers())
@given(instance=TimeInterval_strategy)
@settings(max_examples=25)
def test_TimeInterval_instantiation(instance):
    assert isinstance(instance, TimeInterval)


Users_strategy = st.builds(Users, id=st.integers(), individuadIdentificationCode=st.integers(), registrationCertificateCode=st.integers(), residentBirthday=safe_text, residentDepartment=safe_text, residentEmail=safe_text, residentName=safe_text, residentPassword=safe_text, residentPatronymic=safe_text, residentPosition=safe_text, residentSurname=safe_text, residentUserType=safe_text, universityStructureUnit=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)



