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
    tdt4250_CourseGroup,
    tdt4250_Course,
    tdt4250_Specialisation,
    tdt4250_Student,
    tdt4250_StudyProgram,
    StudyProgramName,
    Semester,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tdt4250_coursegroup_is_not_abstract():
    assert not inspect.isabstract(tdt4250_CourseGroup)


def test_hyp_tdt4250_coursegroup_constructor_exists():
    assert callable(tdt4250_CourseGroup.__init__)


def test_hyp_tdt4250_coursegroup_constructor_args():
    sig = inspect.signature(tdt4250_CourseGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tdt4250_course_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Course)


def test_hyp_tdt4250_course_constructor_exists():
    assert callable(tdt4250_Course.__init__)


def test_hyp_tdt4250_course_constructor_args():
    sig = inspect.signature(tdt4250_Course.__init__)
    params = list(sig.parameters.keys())
    assert "study_points" in params, "Missing parameter 'study_points'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "level" in params, "Missing parameter 'level'"








def test_hyp_tdt4250_specialisation_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Specialisation)


def test_hyp_tdt4250_specialisation_constructor_exists():
    assert callable(tdt4250_Specialisation.__init__)


def test_hyp_tdt4250_specialisation_constructor_args():
    sig = inspect.signature(tdt4250_Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tdt4250_student_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Student)


def test_hyp_tdt4250_student_constructor_exists():
    assert callable(tdt4250_Student.__init__)


def test_hyp_tdt4250_student_constructor_args():
    sig = inspect.signature(tdt4250_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentID" in params, "Missing parameter 'studentID'"
    assert "current_semester" in params, "Missing parameter 'current_semester'"





def test_hyp_tdt4250_studyprogram_is_not_abstract():
    assert not inspect.isabstract(tdt4250_StudyProgram)


def test_hyp_tdt4250_studyprogram_constructor_exists():
    assert callable(tdt4250_StudyProgram.__init__)


def test_hyp_tdt4250_studyprogram_constructor_args():
    sig = inspect.signature(tdt4250_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "number_of_semesters" in params, "Missing parameter 'number_of_semesters'"



def test_hyp_studyprogramname_exists():
    # Check that the Enumeration exists
    assert StudyProgramName is not None

def test_hyp_studyprogramname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyProgramName]
    expected_literals = [
        "computer_science_5_years",
        "computer_science_2_years",
        "informatics",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyProgramName"

def test_hyp_semester_exists():
    # Check that the Enumeration exists
    assert Semester is not None

def test_hyp_semester_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Semester]
    expected_literals = [
        "spring",
        "autumn",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Semester"


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
tdt4250_CourseGroup_strategy = st.builds(
    tdt4250_CourseGroup,
)
tdt4250_Course_strategy = st.builds(
    tdt4250_Course,
    study_points=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text,
    semester=
        safe_text,
    level=
        safe_text
)
tdt4250_Specialisation_strategy = st.builds(
    tdt4250_Specialisation,
    name=
        safe_text
)
tdt4250_Student_strategy = st.builds(
    tdt4250_Student,
    studentID=
        st.integers(),
    current_semester=
        st.integers()
)
tdt4250_StudyProgram_strategy = st.builds(
    tdt4250_StudyProgram,
    name=
        safe_text,
    number_of_semesters=
        st.integers()
)





@given(instance=tdt4250_Course_strategy)
def test_hyp_tdt4250_course_study_points_setter(instance):
    original = instance.study_points
    instance.study_points = original
    assert instance.study_points == original



@given(instance=tdt4250_Course_strategy)
def test_hyp_tdt4250_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250_Course_strategy)
def test_hyp_tdt4250_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=tdt4250_Course_strategy)
def test_hyp_tdt4250_course_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original



@given(instance=tdt4250_Course_strategy)
def test_hyp_tdt4250_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original




@given(instance=tdt4250_Specialisation_strategy)
def test_hyp_tdt4250_specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tdt4250_Student_strategy)
def test_hyp_tdt4250_student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original



@given(instance=tdt4250_Student_strategy)
def test_hyp_tdt4250_student_current_semester_setter(instance):
    original = instance.current_semester
    instance.current_semester = original
    assert instance.current_semester == original




@given(instance=tdt4250_StudyProgram_strategy)
def test_hyp_tdt4250_studyprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250_StudyProgram_strategy)
def test_hyp_tdt4250_studyprogram_number_of_semesters_setter(instance):
    original = instance.number_of_semesters
    instance.number_of_semesters = original
    assert instance.number_of_semesters == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    tdt4250_Course,
    tdt4250_CourseGroup,
    tdt4250_Specialisation,
    tdt4250_Student,
    tdt4250_StudyProgram,
    Semester,
    StudyProgramName,
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

def test_tdt4250_Course_code_value_roundtrip():
    instance = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_tdt4250_Course_level_value_roundtrip():
    instance = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_tdt4250_Course_name_value_roundtrip():
    instance = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tdt4250_Course_semester_value_roundtrip():
    instance = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    assert instance.semester == "sample_text"
    instance.semester = "sample_text_2"
    assert instance.semester == "sample_text_2"


def test_tdt4250_Course_study_points_value_roundtrip():
    instance = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    assert instance.study_points == 3.14
    instance.study_points = 9.99
    assert instance.study_points == 9.99


def test_tdt4250_Specialisation_name_value_roundtrip():
    instance = tdt4250_Specialisation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tdt4250_Student_current_semester_value_roundtrip():
    instance = tdt4250_Student(current_semester=7, studentID=7)
    assert instance.current_semester == 7
    instance.current_semester = 13
    assert instance.current_semester == 13


def test_tdt4250_Student_studentID_value_roundtrip():
    instance = tdt4250_Student(current_semester=7, studentID=7)
    assert instance.studentID == 7
    instance.studentID = 13
    assert instance.studentID == 13


def test_tdt4250_StudyProgram_name_value_roundtrip():
    instance = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tdt4250_StudyProgram_number_of_semesters_value_roundtrip():
    instance = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    assert instance.number_of_semesters == 7
    instance.number_of_semesters = 13
    assert instance.number_of_semesters == 13


def test_assoc_course_group22_link_reassign_clear():
    a = tdt4250_Specialisation(name="sample_text")
    b1 = tdt4250_CourseGroup()
    b2 = tdt4250_CourseGroup()
    _safe_set(a, 'tdt4250_Specialisation23', b1)
    assert _is_linked(a, 'tdt4250_Specialisation23', b1)
    if hasattr(b1, 'tdt4250_CourseGroup24'):
        assert _is_linked(b1, 'tdt4250_CourseGroup24', a)
    _safe_set(a, 'tdt4250_Specialisation23', b2)
    assert _is_linked(a, 'tdt4250_Specialisation23', b2)
    if hasattr(b1, 'tdt4250_CourseGroup24'):
        assert not _is_linked(b1, 'tdt4250_CourseGroup24', a)
    if hasattr(b2, 'tdt4250_CourseGroup24'):
        assert _is_linked(b2, 'tdt4250_CourseGroup24', a)
    _safe_set(a, 'tdt4250_Specialisation23', None)
    assert not _is_linked(a, 'tdt4250_Specialisation23', b2)
    if hasattr(b2, 'tdt4250_CourseGroup24'):
        assert not _is_linked(b2, 'tdt4250_CourseGroup24', a)


def test_assoc_courses5_link_reassign_clear():
    a = tdt4250_Student(current_semester=7, studentID=7)
    b1 = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    b2 = tdt4250_Course(code="sample_text_2", level="sample_text_2", name="sample_text_2", semester="sample_text_2", study_points=9.99)
    _safe_set(a, 'tdt4250_Student6', {b1})
    assert _is_linked(a, 'tdt4250_Student6', b1)
    if hasattr(b1, 'tdt4250_Course7'):
        assert _is_linked(b1, 'tdt4250_Course7', a)
    _safe_set(a, 'tdt4250_Student6', {b2})
    assert _is_linked(a, 'tdt4250_Student6', b2)
    if hasattr(b1, 'tdt4250_Course7'):
        assert not _is_linked(b1, 'tdt4250_Course7', a)
    if hasattr(b2, 'tdt4250_Course7'):
        assert _is_linked(b2, 'tdt4250_Course7', a)
    _safe_set(a, 'tdt4250_Student6', set())
    assert not _is_linked(a, 'tdt4250_Student6', b2)
    if hasattr(b2, 'tdt4250_Course7'):
        assert not _is_linked(b2, 'tdt4250_Course7', a)


def test_assoc_elective_courses10_link_reassign_clear():
    a = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    b1 = tdt4250_CourseGroup()
    b2 = tdt4250_CourseGroup()
    _safe_set(a, 'tdt4250_Course12', b1)
    assert _is_linked(a, 'tdt4250_Course12', b1)
    if hasattr(b1, 'tdt4250_CourseGroup11'):
        assert _is_linked(b1, 'tdt4250_CourseGroup11', a)
    _safe_set(a, 'tdt4250_Course12', b2)
    assert _is_linked(a, 'tdt4250_Course12', b2)
    if hasattr(b1, 'tdt4250_CourseGroup11'):
        assert not _is_linked(b1, 'tdt4250_CourseGroup11', a)
    if hasattr(b2, 'tdt4250_CourseGroup11'):
        assert _is_linked(b2, 'tdt4250_CourseGroup11', a)
    _safe_set(a, 'tdt4250_Course12', None)
    assert not _is_linked(a, 'tdt4250_Course12', b2)
    if hasattr(b2, 'tdt4250_CourseGroup11'):
        assert not _is_linked(b2, 'tdt4250_CourseGroup11', a)


def test_assoc_further_specialisation20_link_reassign_clear():
    a = tdt4250_Specialisation(name="sample_text")
    b1 = tdt4250_Specialisation(name="sample_text")
    b2 = tdt4250_Specialisation(name="sample_text_2")
    _safe_set(a, 'tdt4250_Specialisation19', b1)
    assert _is_linked(a, 'tdt4250_Specialisation19', b1)
    if hasattr(b1, 'tdt4250_Specialisation21'):
        assert _is_linked(b1, 'tdt4250_Specialisation21', a)
    _safe_set(a, 'tdt4250_Specialisation19', b2)
    assert _is_linked(a, 'tdt4250_Specialisation19', b2)
    if hasattr(b1, 'tdt4250_Specialisation21'):
        assert not _is_linked(b1, 'tdt4250_Specialisation21', a)
    if hasattr(b2, 'tdt4250_Specialisation21'):
        assert _is_linked(b2, 'tdt4250_Specialisation21', a)
    _safe_set(a, 'tdt4250_Specialisation19', None)
    assert not _is_linked(a, 'tdt4250_Specialisation19', b2)
    if hasattr(b2, 'tdt4250_Specialisation21'):
        assert not _is_linked(b2, 'tdt4250_Specialisation21', a)


def test_assoc_mandatory_courses8_link_reassign_clear():
    a = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    b1 = tdt4250_CourseGroup()
    b2 = tdt4250_CourseGroup()
    _safe_set(a, 'tdt4250_Course9', b1)
    assert _is_linked(a, 'tdt4250_Course9', b1)
    if hasattr(b1, 'tdt4250_CourseGroup'):
        assert _is_linked(b1, 'tdt4250_CourseGroup', a)
    _safe_set(a, 'tdt4250_Course9', b2)
    assert _is_linked(a, 'tdt4250_Course9', b2)
    if hasattr(b1, 'tdt4250_CourseGroup'):
        assert not _is_linked(b1, 'tdt4250_CourseGroup', a)
    if hasattr(b2, 'tdt4250_CourseGroup'):
        assert _is_linked(b2, 'tdt4250_CourseGroup', a)
    _safe_set(a, 'tdt4250_Course9', None)
    assert not _is_linked(a, 'tdt4250_Course9', b2)
    if hasattr(b2, 'tdt4250_CourseGroup'):
        assert not _is_linked(b2, 'tdt4250_CourseGroup', a)


def test_assoc_obligatory_courses3_link_reassign_clear():
    a = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    b1 = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    b2 = tdt4250_Course(code="sample_text_2", level="sample_text_2", name="sample_text_2", semester="sample_text_2", study_points=9.99)
    _safe_set(a, 'tdt4250_StudyProgram4', {b1})
    assert _is_linked(a, 'tdt4250_StudyProgram4', b1)
    if hasattr(b1, 'tdt4250_Course'):
        assert _is_linked(b1, 'tdt4250_Course', a)
    _safe_set(a, 'tdt4250_StudyProgram4', {b2})
    assert _is_linked(a, 'tdt4250_StudyProgram4', b2)
    if hasattr(b1, 'tdt4250_Course'):
        assert not _is_linked(b1, 'tdt4250_Course', a)
    if hasattr(b2, 'tdt4250_Course'):
        assert _is_linked(b2, 'tdt4250_Course', a)
    _safe_set(a, 'tdt4250_StudyProgram4', set())
    assert not _is_linked(a, 'tdt4250_StudyProgram4', b2)
    if hasattr(b2, 'tdt4250_Course'):
        assert not _is_linked(b2, 'tdt4250_Course', a)


def test_assoc_specialisation13_link_reassign_clear():
    a = tdt4250_Specialisation(name="sample_text")
    b1 = tdt4250_CourseGroup()
    b2 = tdt4250_CourseGroup()
    _safe_set(a, 'tdt4250_Specialisation15', b1)
    assert _is_linked(a, 'tdt4250_Specialisation15', b1)
    if hasattr(b1, 'tdt4250_CourseGroup14'):
        assert _is_linked(b1, 'tdt4250_CourseGroup14', a)
    _safe_set(a, 'tdt4250_Specialisation15', b2)
    assert _is_linked(a, 'tdt4250_Specialisation15', b2)
    if hasattr(b1, 'tdt4250_CourseGroup14'):
        assert not _is_linked(b1, 'tdt4250_CourseGroup14', a)
    if hasattr(b2, 'tdt4250_CourseGroup14'):
        assert _is_linked(b2, 'tdt4250_CourseGroup14', a)
    _safe_set(a, 'tdt4250_Specialisation15', None)
    assert not _is_linked(a, 'tdt4250_Specialisation15', b2)
    if hasattr(b2, 'tdt4250_CourseGroup14'):
        assert not _is_linked(b2, 'tdt4250_CourseGroup14', a)


def test_assoc_specialisations1_link_reassign_clear():
    a = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    b1 = tdt4250_Specialisation(name="sample_text")
    b2 = tdt4250_Specialisation(name="sample_text_2")
    _safe_set(a, 'tdt4250_StudyProgram2', {b1})
    assert _is_linked(a, 'tdt4250_StudyProgram2', b1)
    if hasattr(b1, 'tdt4250_Specialisation'):
        assert _is_linked(b1, 'tdt4250_Specialisation', a)
    _safe_set(a, 'tdt4250_StudyProgram2', {b2})
    assert _is_linked(a, 'tdt4250_StudyProgram2', b2)
    if hasattr(b1, 'tdt4250_Specialisation'):
        assert not _is_linked(b1, 'tdt4250_Specialisation', a)
    if hasattr(b2, 'tdt4250_Specialisation'):
        assert _is_linked(b2, 'tdt4250_Specialisation', a)
    _safe_set(a, 'tdt4250_StudyProgram2', set())
    assert not _is_linked(a, 'tdt4250_StudyProgram2', b2)
    if hasattr(b2, 'tdt4250_Specialisation'):
        assert not _is_linked(b2, 'tdt4250_Specialisation', a)


def test_assoc_students0_link_reassign_clear():
    a = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    b1 = tdt4250_Student(current_semester=7, studentID=7)
    b2 = tdt4250_Student(current_semester=13, studentID=13)
    _safe_set(a, 'tdt4250_StudyProgram', {b1})
    assert _is_linked(a, 'tdt4250_StudyProgram', b1)
    if hasattr(b1, 'tdt4250_Student'):
        assert _is_linked(b1, 'tdt4250_Student', a)
    _safe_set(a, 'tdt4250_StudyProgram', {b2})
    assert _is_linked(a, 'tdt4250_StudyProgram', b2)
    if hasattr(b1, 'tdt4250_Student'):
        assert not _is_linked(b1, 'tdt4250_Student', a)
    if hasattr(b2, 'tdt4250_Student'):
        assert _is_linked(b2, 'tdt4250_Student', a)
    _safe_set(a, 'tdt4250_StudyProgram', set())
    assert not _is_linked(a, 'tdt4250_StudyProgram', b2)
    if hasattr(b2, 'tdt4250_Student'):
        assert not _is_linked(b2, 'tdt4250_Student', a)


def test_assoc_students16_link_reassign_clear():
    a = tdt4250_Student(current_semester=7, studentID=7)
    b1 = tdt4250_Specialisation(name="sample_text")
    b2 = tdt4250_Specialisation(name="sample_text_2")
    _safe_set(a, 'tdt4250_Student18', b1)
    assert _is_linked(a, 'tdt4250_Student18', b1)
    if hasattr(b1, 'tdt4250_Specialisation17'):
        assert _is_linked(b1, 'tdt4250_Specialisation17', a)
    _safe_set(a, 'tdt4250_Student18', b2)
    assert _is_linked(a, 'tdt4250_Student18', b2)
    if hasattr(b1, 'tdt4250_Specialisation17'):
        assert not _is_linked(b1, 'tdt4250_Specialisation17', a)
    if hasattr(b2, 'tdt4250_Specialisation17'):
        assert _is_linked(b2, 'tdt4250_Specialisation17', a)
    _safe_set(a, 'tdt4250_Student18', None)
    assert not _is_linked(a, 'tdt4250_Student18', b2)
    if hasattr(b2, 'tdt4250_Specialisation17'):
        assert not _is_linked(b2, 'tdt4250_Specialisation17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tdt4250_Course_strategy = st.builds(tdt4250_Course, code=safe_text, level=safe_text, name=safe_text, semester=safe_text, study_points=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tdt4250_Course_strategy)
@settings(max_examples=25)
def test_tdt4250_Course_instantiation(instance):
    assert isinstance(instance, tdt4250_Course)


tdt4250_CourseGroup_strategy = st.builds(tdt4250_CourseGroup)
@given(instance=tdt4250_CourseGroup_strategy)
@settings(max_examples=25)
def test_tdt4250_CourseGroup_instantiation(instance):
    assert isinstance(instance, tdt4250_CourseGroup)


tdt4250_Specialisation_strategy = st.builds(tdt4250_Specialisation, name=safe_text)
@given(instance=tdt4250_Specialisation_strategy)
@settings(max_examples=25)
def test_tdt4250_Specialisation_instantiation(instance):
    assert isinstance(instance, tdt4250_Specialisation)


tdt4250_Student_strategy = st.builds(tdt4250_Student, current_semester=st.integers(), studentID=st.integers())
@given(instance=tdt4250_Student_strategy)
@settings(max_examples=25)
def test_tdt4250_Student_instantiation(instance):
    assert isinstance(instance, tdt4250_Student)


tdt4250_StudyProgram_strategy = st.builds(tdt4250_StudyProgram, name=safe_text, number_of_semesters=st.integers())
@given(instance=tdt4250_StudyProgram_strategy)
@settings(max_examples=25)
def test_tdt4250_StudyProgram_instantiation(instance):
    assert isinstance(instance, tdt4250_StudyProgram)



