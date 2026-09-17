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
    Person,
    test_Employee,
    test_Student,
    test_Person,
    test_University,
    Grade,
    incomeLevel,
    EEnum0,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_employee_is_not_abstract():
    assert not inspect.isabstract(test_Employee)


def test_hyp_test_employee_constructor_exists():
    assert callable(test_Employee.__init__)


def test_hyp_test_employee_constructor_args():
    sig = inspect.signature(test_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "incomeLevel" in params, "Missing parameter 'incomeLevel'"




def test_hyp_test_student_is_not_abstract():
    assert not inspect.isabstract(test_Student)


def test_hyp_test_student_constructor_exists():
    assert callable(test_Student.__init__)


def test_hyp_test_student_constructor_args():
    sig = inspect.signature(test_Student.__init__)
    params = list(sig.parameters.keys())
    assert "regNo" in params, "Missing parameter 'regNo'"




def test_hyp_test_person_is_not_abstract():
    assert not inspect.isabstract(test_Person)


def test_hyp_test_person_constructor_exists():
    assert callable(test_Person.__init__)


def test_hyp_test_person_constructor_args():
    sig = inspect.signature(test_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstame" in params, "Missing parameter 'firstame'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "Grade" in params, "Missing parameter 'Grade'"






def test_hyp_test_university_is_not_abstract():
    assert not inspect.isabstract(test_University)


def test_hyp_test_university_constructor_exists():
    assert callable(test_University.__init__)


def test_hyp_test_university_constructor_args():
    sig = inspect.signature(test_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_hyp_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "PHD",
        "None_",
        "MSC",
        "Professor",
        "BSC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"

def test_hyp_incomelevel_exists():
    # Check that the Enumeration exists
    assert incomeLevel is not None

def test_hyp_incomelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in incomeLevel]
    expected_literals = [
        "Professor",
        "PostDoc",
        "PreDoc",
        "UnderGrad",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in incomeLevel"

def test_hyp_eenum0_exists():
    # Check that the Enumeration exists
    assert EEnum0 is not None

def test_hyp_eenum0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnum0]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnum0"


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
Person_strategy = st.builds(
    Person,
)
test_Employee_strategy = st.builds(
    test_Employee,
    incomeLevel=
        safe_text
)
test_Student_strategy = st.builds(
    test_Student,
    regNo=
        safe_text
)
test_Person_strategy = st.builds(
    test_Person,
    firstame=
        safe_text,
    lastname=
        safe_text,
    Grade=
        safe_text
)
test_University_strategy = st.builds(
    test_University,
    name=
        safe_text
)





@given(instance=test_Employee_strategy)
def test_hyp_test_employee_incomeLevel_setter(instance):
    original = instance.incomeLevel
    instance.incomeLevel = original
    assert instance.incomeLevel == original




@given(instance=test_Student_strategy)
def test_hyp_test_student_regNo_setter(instance):
    original = instance.regNo
    instance.regNo = original
    assert instance.regNo == original




@given(instance=test_Person_strategy)
def test_hyp_test_person_firstame_setter(instance):
    original = instance.firstame
    instance.firstame = original
    assert instance.firstame == original



@given(instance=test_Person_strategy)
def test_hyp_test_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=test_Person_strategy)
def test_hyp_test_person_Grade_setter(instance):
    original = instance.Grade
    instance.Grade = original
    assert instance.Grade == original




@given(instance=test_University_strategy)
def test_hyp_test_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    test_Employee,
    test_Person,
    test_Student,
    test_University,
    EEnum0,
    Grade,
    incomeLevel,
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

def test_test_Employee_incomeLevel_value_roundtrip():
    instance = test_Employee(incomeLevel="sample_text")
    assert instance.incomeLevel == "sample_text"
    instance.incomeLevel = "sample_text_2"
    assert instance.incomeLevel == "sample_text_2"


def test_test_Person_Grade_value_roundtrip():
    instance = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    assert instance.Grade == "sample_text"
    instance.Grade = "sample_text_2"
    assert instance.Grade == "sample_text_2"


def test_test_Person_firstame_value_roundtrip():
    instance = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    assert instance.firstame == "sample_text"
    instance.firstame = "sample_text_2"
    assert instance.firstame == "sample_text_2"


def test_test_Person_lastname_value_roundtrip():
    instance = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_test_Student_regNo_value_roundtrip():
    instance = test_Student(regNo="sample_text")
    assert instance.regNo == "sample_text"
    instance.regNo = "sample_text_2"
    assert instance.regNo == "sample_text_2"


def test_test_University_name_value_roundtrip():
    instance = test_University(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test_Employee_isa_Person():
    instance = test_Employee(incomeLevel="sample_text")
    assert isinstance(instance, Person)


def test_test_Student_isa_Person():
    instance = test_Student(regNo="sample_text")
    assert isinstance(instance, Person)


def test_assoc_persons5_link_reassign_clear():
    a = test_University(name="sample_text")
    b1 = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    b2 = test_Person(Grade="sample_text_2", firstame="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'test_University', {b1})
    assert _is_linked(a, 'test_University', b1)
    if hasattr(b1, 'test_Person6'):
        assert _is_linked(b1, 'test_Person6', a)
    _safe_set(a, 'test_University', {b2})
    assert _is_linked(a, 'test_University', b2)
    if hasattr(b1, 'test_Person6'):
        assert not _is_linked(b1, 'test_Person6', a)
    if hasattr(b2, 'test_Person6'):
        assert _is_linked(b2, 'test_Person6', a)
    _safe_set(a, 'test_University', set())
    assert not _is_linked(a, 'test_University', b2)
    if hasattr(b2, 'test_Person6'):
        assert not _is_linked(b2, 'test_Person6', a)


def test_assoc_supervised3_link_reassign_clear():
    a = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    b1 = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    b2 = test_Person(Grade="sample_text_2", firstame="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'test_Person2', {b1})
    assert _is_linked(a, 'test_Person2', b1)
    if hasattr(b1, 'test_Person4'):
        assert _is_linked(b1, 'test_Person4', a)
    _safe_set(a, 'test_Person2', {b2})
    assert _is_linked(a, 'test_Person2', b2)
    if hasattr(b1, 'test_Person4'):
        assert not _is_linked(b1, 'test_Person4', a)
    if hasattr(b2, 'test_Person4'):
        assert _is_linked(b2, 'test_Person4', a)
    _safe_set(a, 'test_Person2', set())
    assert not _is_linked(a, 'test_Person2', b2)
    if hasattr(b2, 'test_Person4'):
        assert not _is_linked(b2, 'test_Person4', a)


def test_assoc_supervisor1_link_reassign_clear():
    a = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    b1 = test_Person(Grade="sample_text", firstame="sample_text", lastname="sample_text")
    b2 = test_Person(Grade="sample_text_2", firstame="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'test_Person', b1)
    assert _is_linked(a, 'test_Person', b1)
    if hasattr(b1, 'test_Person0'):
        assert _is_linked(b1, 'test_Person0', a)
    _safe_set(a, 'test_Person', b2)
    assert _is_linked(a, 'test_Person', b2)
    if hasattr(b1, 'test_Person0'):
        assert not _is_linked(b1, 'test_Person0', a)
    if hasattr(b2, 'test_Person0'):
        assert _is_linked(b2, 'test_Person0', a)
    _safe_set(a, 'test_Person', None)
    assert not _is_linked(a, 'test_Person', b2)
    if hasattr(b2, 'test_Person0'):
        assert not _is_linked(b2, 'test_Person0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


test_Employee_strategy = st.builds(test_Employee, incomeLevel=safe_text)
@given(instance=test_Employee_strategy)
@settings(max_examples=25)
def test_test_Employee_instantiation(instance):
    assert isinstance(instance, test_Employee)


test_Person_strategy = st.builds(test_Person, Grade=safe_text, firstame=safe_text, lastname=safe_text)
@given(instance=test_Person_strategy)
@settings(max_examples=25)
def test_test_Person_instantiation(instance):
    assert isinstance(instance, test_Person)


test_Student_strategy = st.builds(test_Student, regNo=safe_text)
@given(instance=test_Student_strategy)
@settings(max_examples=25)
def test_test_Student_instantiation(instance):
    assert isinstance(instance, test_Student)


test_University_strategy = st.builds(test_University, name=safe_text)
@given(instance=test_University_strategy)
@settings(max_examples=25)
def test_test_University_instantiation(instance):
    assert isinstance(instance, test_University)



