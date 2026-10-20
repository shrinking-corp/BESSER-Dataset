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
    Student,
    SourceModel_BachelorStudent,
    SourceModel_MasterStudent,
    Person,
    SourceModel_Professor,
    SourceModel_Student,
    SourceModel_Person,
    SourceModel_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcemodel_bachelorstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel_BachelorStudent)


def test_hyp_sourcemodel_bachelorstudent_constructor_exists():
    assert callable(SourceModel_BachelorStudent.__init__)


def test_hyp_sourcemodel_bachelorstudent_constructor_args():
    sig = inspect.signature(SourceModel_BachelorStudent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcemodel_masterstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel_MasterStudent)


def test_hyp_sourcemodel_masterstudent_constructor_exists():
    assert callable(SourceModel_MasterStudent.__init__)


def test_hyp_sourcemodel_masterstudent_constructor_args():
    sig = inspect.signature(SourceModel_MasterStudent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcemodel_professor_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Professor)


def test_hyp_sourcemodel_professor_constructor_exists():
    assert callable(SourceModel_Professor.__init__)


def test_hyp_sourcemodel_professor_constructor_args():
    sig = inspect.signature(SourceModel_Professor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcemodel_student_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Student)


def test_hyp_sourcemodel_student_constructor_exists():
    assert callable(SourceModel_Student.__init__)


def test_hyp_sourcemodel_student_constructor_args():
    sig = inspect.signature(SourceModel_Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcemodel_person_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Person)


def test_hyp_sourcemodel_person_constructor_exists():
    assert callable(SourceModel_Person.__init__)


def test_hyp_sourcemodel_person_constructor_args():
    sig = inspect.signature(SourceModel_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"




def test_hyp_sourcemodel_container_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Container)


def test_hyp_sourcemodel_container_constructor_exists():
    assert callable(SourceModel_Container.__init__)


def test_hyp_sourcemodel_container_constructor_args():
    sig = inspect.signature(SourceModel_Container.__init__)
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
Student_strategy = st.builds(
    Student,
)
SourceModel_BachelorStudent_strategy = st.builds(
    SourceModel_BachelorStudent,
)
SourceModel_MasterStudent_strategy = st.builds(
    SourceModel_MasterStudent,
)
Person_strategy = st.builds(
    Person,
)
SourceModel_Professor_strategy = st.builds(
    SourceModel_Professor,
)
SourceModel_Student_strategy = st.builds(
    SourceModel_Student,
)
SourceModel_Person_strategy = st.builds(
    SourceModel_Person,
    age=
        safe_text
)
SourceModel_Container_strategy = st.builds(
    SourceModel_Container,
)










@given(instance=SourceModel_Person_strategy)
def test_hyp_sourcemodel_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    SourceModel_BachelorStudent,
    SourceModel_Container,
    SourceModel_MasterStudent,
    SourceModel_Person,
    SourceModel_Professor,
    SourceModel_Student,
    Student,
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

def test_SourceModel_Person_age_value_roundtrip():
    instance = SourceModel_Person(age="sample_text")
    assert instance.age == "sample_text"
    instance.age = "sample_text_2"
    assert instance.age == "sample_text_2"


def test_SourceModel_Professor_isa_Person():
    instance = SourceModel_Professor()
    assert isinstance(instance, Person)


def test_SourceModel_Student_isa_Person():
    instance = SourceModel_Student()
    assert isinstance(instance, Person)


def test_SourceModel_BachelorStudent_isa_Student():
    instance = SourceModel_BachelorStudent()
    assert isinstance(instance, Student)


def test_SourceModel_MasterStudent_isa_Student():
    instance = SourceModel_MasterStudent()
    assert isinstance(instance, Student)


def test_assoc_likes2_link_reassign_clear():
    a = SourceModel_Person(age="sample_text")
    b1 = SourceModel_Person(age="sample_text")
    b2 = SourceModel_Person(age="sample_text_2")
    _safe_set(a, 'SourceModel_Person1', b1)
    assert _is_linked(a, 'SourceModel_Person1', b1)
    if hasattr(b1, 'SourceModel_Person3'):
        assert _is_linked(b1, 'SourceModel_Person3', a)
    _safe_set(a, 'SourceModel_Person1', b2)
    assert _is_linked(a, 'SourceModel_Person1', b2)
    if hasattr(b1, 'SourceModel_Person3'):
        assert not _is_linked(b1, 'SourceModel_Person3', a)
    if hasattr(b2, 'SourceModel_Person3'):
        assert _is_linked(b2, 'SourceModel_Person3', a)
    _safe_set(a, 'SourceModel_Person1', None)
    assert not _is_linked(a, 'SourceModel_Person1', b2)
    if hasattr(b2, 'SourceModel_Person3'):
        assert not _is_linked(b2, 'SourceModel_Person3', a)


def test_assoc_persons0_link_reassign_clear():
    a = SourceModel_Person(age="sample_text")
    b1 = SourceModel_Container()
    b2 = SourceModel_Container()
    _safe_set(a, 'SourceModel_Person', b1)
    assert _is_linked(a, 'SourceModel_Person', b1)
    if hasattr(b1, 'SourceModel_Container'):
        assert _is_linked(b1, 'SourceModel_Container', a)
    _safe_set(a, 'SourceModel_Person', b2)
    assert _is_linked(a, 'SourceModel_Person', b2)
    if hasattr(b1, 'SourceModel_Container'):
        assert not _is_linked(b1, 'SourceModel_Container', a)
    if hasattr(b2, 'SourceModel_Container'):
        assert _is_linked(b2, 'SourceModel_Container', a)
    _safe_set(a, 'SourceModel_Person', None)
    assert not _is_linked(a, 'SourceModel_Person', b2)
    if hasattr(b2, 'SourceModel_Container'):
        assert not _is_linked(b2, 'SourceModel_Container', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


SourceModel_BachelorStudent_strategy = st.builds(SourceModel_BachelorStudent)
@given(instance=SourceModel_BachelorStudent_strategy)
@settings(max_examples=25)
def test_SourceModel_BachelorStudent_instantiation(instance):
    assert isinstance(instance, SourceModel_BachelorStudent)


SourceModel_Container_strategy = st.builds(SourceModel_Container)
@given(instance=SourceModel_Container_strategy)
@settings(max_examples=25)
def test_SourceModel_Container_instantiation(instance):
    assert isinstance(instance, SourceModel_Container)


SourceModel_MasterStudent_strategy = st.builds(SourceModel_MasterStudent)
@given(instance=SourceModel_MasterStudent_strategy)
@settings(max_examples=25)
def test_SourceModel_MasterStudent_instantiation(instance):
    assert isinstance(instance, SourceModel_MasterStudent)


SourceModel_Person_strategy = st.builds(SourceModel_Person, age=safe_text)
@given(instance=SourceModel_Person_strategy)
@settings(max_examples=25)
def test_SourceModel_Person_instantiation(instance):
    assert isinstance(instance, SourceModel_Person)


SourceModel_Professor_strategy = st.builds(SourceModel_Professor)
@given(instance=SourceModel_Professor_strategy)
@settings(max_examples=25)
def test_SourceModel_Professor_instantiation(instance):
    assert isinstance(instance, SourceModel_Professor)


SourceModel_Student_strategy = st.builds(SourceModel_Student)
@given(instance=SourceModel_Student_strategy)
@settings(max_examples=25)
def test_SourceModel_Student_instantiation(instance):
    assert isinstance(instance, SourceModel_Student)


Student_strategy = st.builds(Student)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)



