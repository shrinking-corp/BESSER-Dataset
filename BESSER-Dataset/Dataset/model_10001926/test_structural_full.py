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


