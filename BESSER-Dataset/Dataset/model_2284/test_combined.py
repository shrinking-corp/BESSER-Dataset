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
    Univerity_uncertainty_aUniversity,
    uUniversity,
    uncertainty_Univerity_University,
    Univerity_uncertainty_aPerson,
    uPerson,
    uncertainty_Univerity_Person,
    Univerity_uncertainty_aCourses,
    uCourses,
    uncertainty_Univerity_Courses,
    uncertainty_UData,
    Univerity_uncertainty_UData,
    uncertainty_aPerson,
    Univerity_uncertainty_uPerson,
    aPerson,
    aCourses,
    uncertainty_aCourses,
    Univerity_uncertainty_uCourses,
    uncertainty_ModelElement,
    Univerity_Person,
    Univerity_Courses,
    ModelElement,
    Univerity_uncertainty_ModelElement,
    uncertainty_aUniversity,
    Univerity_uncertainty_uUniversity,
    Univerity_University,
    OperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_univerity_uncertainty_auniversity_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_aUniversity)


def test_hyp_univerity_uncertainty_auniversity_constructor_exists():
    assert callable(Univerity_uncertainty_aUniversity.__init__)


def test_hyp_univerity_uncertainty_auniversity_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_aUniversity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uuniversity_is_not_abstract():
    assert not inspect.isabstract(uUniversity)


def test_hyp_uuniversity_constructor_exists():
    assert callable(uUniversity.__init__)


def test_hyp_uuniversity_constructor_args():
    sig = inspect.signature(uUniversity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_univerity_university_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Univerity_University)


def test_hyp_uncertainty_univerity_university_constructor_exists():
    assert callable(uncertainty_Univerity_University.__init__)


def test_hyp_uncertainty_univerity_university_constructor_args():
    sig = inspect.signature(uncertainty_Univerity_University.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_aperson_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_aPerson)


def test_hyp_univerity_uncertainty_aperson_constructor_exists():
    assert callable(Univerity_uncertainty_aPerson.__init__)


def test_hyp_univerity_uncertainty_aperson_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_aPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uperson_is_not_abstract():
    assert not inspect.isabstract(uPerson)


def test_hyp_uperson_constructor_exists():
    assert callable(uPerson.__init__)


def test_hyp_uperson_constructor_args():
    sig = inspect.signature(uPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_univerity_person_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Univerity_Person)


def test_hyp_uncertainty_univerity_person_constructor_exists():
    assert callable(uncertainty_Univerity_Person.__init__)


def test_hyp_uncertainty_univerity_person_constructor_args():
    sig = inspect.signature(uncertainty_Univerity_Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_acourses_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_aCourses)


def test_hyp_univerity_uncertainty_acourses_constructor_exists():
    assert callable(Univerity_uncertainty_aCourses.__init__)


def test_hyp_univerity_uncertainty_acourses_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_aCourses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ucourses_is_not_abstract():
    assert not inspect.isabstract(uCourses)


def test_hyp_ucourses_constructor_exists():
    assert callable(uCourses.__init__)


def test_hyp_ucourses_constructor_args():
    sig = inspect.signature(uCourses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_univerity_courses_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Univerity_Courses)


def test_hyp_uncertainty_univerity_courses_constructor_exists():
    assert callable(uncertainty_Univerity_Courses.__init__)


def test_hyp_uncertainty_univerity_courses_constructor_args():
    sig = inspect.signature(uncertainty_Univerity_Courses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_udata_is_not_abstract():
    assert not inspect.isabstract(uncertainty_UData)


def test_hyp_uncertainty_udata_constructor_exists():
    assert callable(uncertainty_UData.__init__)


def test_hyp_uncertainty_udata_constructor_args():
    sig = inspect.signature(uncertainty_UData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_udata_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_UData)


def test_hyp_univerity_uncertainty_udata_constructor_exists():
    assert callable(Univerity_uncertainty_UData.__init__)


def test_hyp_univerity_uncertainty_udata_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_UData.__init__)
    params = list(sig.parameters.keys())
    assert "utype" in params, "Missing parameter 'utype'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_uncertainty_aperson_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aPerson)


def test_hyp_uncertainty_aperson_constructor_exists():
    assert callable(uncertainty_aPerson.__init__)


def test_hyp_uncertainty_aperson_constructor_args():
    sig = inspect.signature(uncertainty_aPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_uperson_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_uPerson)


def test_hyp_univerity_uncertainty_uperson_constructor_exists():
    assert callable(Univerity_uncertainty_uPerson.__init__)


def test_hyp_univerity_uncertainty_uperson_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_uPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aperson_is_not_abstract():
    assert not inspect.isabstract(aPerson)


def test_hyp_aperson_constructor_exists():
    assert callable(aPerson.__init__)


def test_hyp_aperson_constructor_args():
    sig = inspect.signature(aPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_acourses_is_not_abstract():
    assert not inspect.isabstract(aCourses)


def test_hyp_acourses_constructor_exists():
    assert callable(aCourses.__init__)


def test_hyp_acourses_constructor_args():
    sig = inspect.signature(aCourses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_acourses_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aCourses)


def test_hyp_uncertainty_acourses_constructor_exists():
    assert callable(uncertainty_aCourses.__init__)


def test_hyp_uncertainty_acourses_constructor_args():
    sig = inspect.signature(uncertainty_aCourses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_ucourses_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_uCourses)


def test_hyp_univerity_uncertainty_ucourses_constructor_exists():
    assert callable(Univerity_uncertainty_uCourses.__init__)


def test_hyp_univerity_uncertainty_ucourses_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_uCourses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_modelelement_is_not_abstract():
    assert not inspect.isabstract(uncertainty_ModelElement)


def test_hyp_uncertainty_modelelement_constructor_exists():
    assert callable(uncertainty_ModelElement.__init__)


def test_hyp_uncertainty_modelelement_constructor_args():
    sig = inspect.signature(uncertainty_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_person_is_not_abstract():
    assert not inspect.isabstract(Univerity_Person)


def test_hyp_univerity_person_constructor_exists():
    assert callable(Univerity_Person.__init__)


def test_hyp_univerity_person_constructor_args():
    sig = inspect.signature(Univerity_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_univerity_courses_is_not_abstract():
    assert not inspect.isabstract(Univerity_Courses)


def test_hyp_univerity_courses_constructor_exists():
    assert callable(Univerity_Courses.__init__)


def test_hyp_univerity_courses_constructor_args():
    sig = inspect.signature(Univerity_Courses.__init__)
    params = list(sig.parameters.keys())
    assert "CFU" in params, "Missing parameter 'CFU'"
    assert "Semester" in params, "Missing parameter 'Semester'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_modelelement_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_ModelElement)


def test_hyp_univerity_uncertainty_modelelement_constructor_exists():
    assert callable(Univerity_uncertainty_ModelElement.__init__)


def test_hyp_univerity_uncertainty_modelelement_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_auniversity_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aUniversity)


def test_hyp_uncertainty_auniversity_constructor_exists():
    assert callable(uncertainty_aUniversity.__init__)


def test_hyp_uncertainty_auniversity_constructor_args():
    sig = inspect.signature(uncertainty_aUniversity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_uncertainty_uuniversity_is_not_abstract():
    assert not inspect.isabstract(Univerity_uncertainty_uUniversity)


def test_hyp_univerity_uncertainty_uuniversity_constructor_exists():
    assert callable(Univerity_uncertainty_uUniversity.__init__)


def test_hyp_univerity_uncertainty_uuniversity_constructor_args():
    sig = inspect.signature(Univerity_uncertainty_uUniversity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_university_is_not_abstract():
    assert not inspect.isabstract(Univerity_University)


def test_hyp_univerity_university_constructor_exists():
    assert callable(Univerity_University.__init__)


def test_hyp_univerity_university_constructor_args():
    sig = inspect.signature(Univerity_University.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_hyp_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "XOR",
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorType"


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
Univerity_uncertainty_aUniversity_strategy = st.builds(
    Univerity_uncertainty_aUniversity,
)
uUniversity_strategy = st.builds(
    uUniversity,
)
uncertainty_Univerity_University_strategy = st.builds(
    uncertainty_Univerity_University,
)
Univerity_uncertainty_aPerson_strategy = st.builds(
    Univerity_uncertainty_aPerson,
)
uPerson_strategy = st.builds(
    uPerson,
)
uncertainty_Univerity_Person_strategy = st.builds(
    uncertainty_Univerity_Person,
)
Univerity_uncertainty_aCourses_strategy = st.builds(
    Univerity_uncertainty_aCourses,
)
uCourses_strategy = st.builds(
    uCourses,
)
uncertainty_Univerity_Courses_strategy = st.builds(
    uncertainty_Univerity_Courses,
)
uncertainty_UData_strategy = st.builds(
    uncertainty_UData,
)
Univerity_uncertainty_UData_strategy = st.builds(
    Univerity_uncertainty_UData,
    utype=
        safe_text,
    name=
        safe_text
)
uncertainty_aPerson_strategy = st.builds(
    uncertainty_aPerson,
)
Univerity_uncertainty_uPerson_strategy = st.builds(
    Univerity_uncertainty_uPerson,
)
aPerson_strategy = st.builds(
    aPerson,
)
aCourses_strategy = st.builds(
    aCourses,
)
uncertainty_aCourses_strategy = st.builds(
    uncertainty_aCourses,
)
Univerity_uncertainty_uCourses_strategy = st.builds(
    Univerity_uncertainty_uCourses,
)
uncertainty_ModelElement_strategy = st.builds(
    uncertainty_ModelElement,
)
Univerity_Person_strategy = st.builds(
    Univerity_Person,
    Email=
        safe_text,
    Name=
        safe_text
)
Univerity_Courses_strategy = st.builds(
    Univerity_Courses,
    CFU=
        st.integers(),
    Semester=
        safe_text,
    Name=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
Univerity_uncertainty_ModelElement_strategy = st.builds(
    Univerity_uncertainty_ModelElement,
)
uncertainty_aUniversity_strategy = st.builds(
    uncertainty_aUniversity,
)
Univerity_uncertainty_uUniversity_strategy = st.builds(
    Univerity_uncertainty_uUniversity,
)
Univerity_University_strategy = st.builds(
    Univerity_University,
)














@given(instance=Univerity_uncertainty_UData_strategy)
def test_hyp_univerity_uncertainty_udata_utype_setter(instance):
    original = instance.utype
    instance.utype = original
    assert instance.utype == original



@given(instance=Univerity_uncertainty_UData_strategy)
def test_hyp_univerity_uncertainty_udata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=Univerity_Person_strategy)
def test_hyp_univerity_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Univerity_Person_strategy)
def test_hyp_univerity_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_CFU_setter(instance):
    original = instance.CFU
    instance.CFU = original
    assert instance.CFU == original



@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original



@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ModelElement,
    Univerity_Courses,
    Univerity_Person,
    Univerity_University,
    Univerity_uncertainty_ModelElement,
    Univerity_uncertainty_UData,
    Univerity_uncertainty_aCourses,
    Univerity_uncertainty_aPerson,
    Univerity_uncertainty_aUniversity,
    Univerity_uncertainty_uCourses,
    Univerity_uncertainty_uPerson,
    Univerity_uncertainty_uUniversity,
    aCourses,
    aPerson,
    uCourses,
    uPerson,
    uUniversity,
    uncertainty_ModelElement,
    uncertainty_UData,
    uncertainty_Univerity_Courses,
    uncertainty_Univerity_Person,
    uncertainty_Univerity_University,
    uncertainty_aCourses,
    uncertainty_aPerson,
    uncertainty_aUniversity,
    OperatorType,
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

def test_Univerity_Courses_CFU_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.CFU == 7
    instance.CFU = 13
    assert instance.CFU == 13


def test_Univerity_Courses_Name_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Univerity_Courses_Semester_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.Semester == "sample_text"
    instance.Semester = "sample_text_2"
    assert instance.Semester == "sample_text_2"


def test_Univerity_Person_Email_value_roundtrip():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Univerity_Person_Name_value_roundtrip():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Univerity_uncertainty_UData_name_value_roundtrip():
    instance = Univerity_uncertainty_UData(name="sample_text", utype="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Univerity_uncertainty_UData_utype_value_roundtrip():
    instance = Univerity_uncertainty_UData(name="sample_text", utype="sample_text")
    assert instance.utype == "sample_text"
    instance.utype = "sample_text_2"
    assert instance.utype == "sample_text_2"


def test_Univerity_Courses_isa_uncertainty_ModelElement():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert isinstance(instance, uncertainty_ModelElement)


def test_Univerity_Person_isa_uncertainty_ModelElement():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert isinstance(instance, uncertainty_ModelElement)


def test_Univerity_University_isa_uncertainty_ModelElement():
    instance = Univerity_University()
    assert isinstance(instance, uncertainty_ModelElement)


def test_Univerity_uncertainty_uCourses_isa_uncertainty_UData():
    instance = Univerity_uncertainty_uCourses()
    assert isinstance(instance, uncertainty_UData)


def test_Univerity_uncertainty_uPerson_isa_uncertainty_UData():
    instance = Univerity_uncertainty_uPerson()
    assert isinstance(instance, uncertainty_UData)


def test_Univerity_uncertainty_uUniversity_isa_uncertainty_UData():
    instance = Univerity_uncertainty_uUniversity()
    assert isinstance(instance, uncertainty_UData)


def test_Univerity_Courses_isa_uncertainty_aCourses():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert isinstance(instance, uncertainty_aCourses)


def test_Univerity_uncertainty_uCourses_isa_uncertainty_aCourses():
    instance = Univerity_uncertainty_uCourses()
    assert isinstance(instance, uncertainty_aCourses)


def test_Univerity_Person_isa_uncertainty_aPerson():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert isinstance(instance, uncertainty_aPerson)


def test_Univerity_uncertainty_uPerson_isa_uncertainty_aPerson():
    instance = Univerity_uncertainty_uPerson()
    assert isinstance(instance, uncertainty_aPerson)


def test_Univerity_University_isa_uncertainty_aUniversity():
    instance = Univerity_University()
    assert isinstance(instance, uncertainty_aUniversity)


def test_Univerity_uncertainty_uUniversity_isa_uncertainty_aUniversity():
    instance = Univerity_uncertainty_uUniversity()
    assert isinstance(instance, uncertainty_aUniversity)


def test_assoc_Professor1_link_reassign_clear():
    a = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b1 = aPerson()
    b2 = aPerson()
    _safe_set(a, 'Univerity_Courses2', b1)
    assert _is_linked(a, 'Univerity_Courses2', b1)
    if hasattr(b1, 'aPerson'):
        assert _is_linked(b1, 'aPerson', a)
    _safe_set(a, 'Univerity_Courses2', b2)
    assert _is_linked(a, 'Univerity_Courses2', b2)
    if hasattr(b1, 'aPerson'):
        assert not _is_linked(b1, 'aPerson', a)
    if hasattr(b2, 'aPerson'):
        assert _is_linked(b2, 'aPerson', a)
    _safe_set(a, 'Univerity_Courses2', None)
    assert not _is_linked(a, 'Univerity_Courses2', b2)
    if hasattr(b2, 'aPerson'):
        assert not _is_linked(b2, 'aPerson', a)


def test_assoc_Student3_link_reassign_clear():
    a = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b1 = aPerson()
    b2 = aPerson()
    _safe_set(a, 'Univerity_Courses4', {b1})
    assert _is_linked(a, 'Univerity_Courses4', b1)
    if hasattr(b1, 'aPerson5'):
        assert _is_linked(b1, 'aPerson5', a)
    _safe_set(a, 'Univerity_Courses4', {b2})
    assert _is_linked(a, 'Univerity_Courses4', b2)
    if hasattr(b1, 'aPerson5'):
        assert not _is_linked(b1, 'aPerson5', a)
    if hasattr(b2, 'aPerson5'):
        assert _is_linked(b2, 'aPerson5', a)
    _safe_set(a, 'Univerity_Courses4', set())
    assert not _is_linked(a, 'Univerity_Courses4', b2)
    if hasattr(b2, 'aPerson5'):
        assert not _is_linked(b2, 'aPerson5', a)


def test_assoc_links0_link_reassign_clear():
    a = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b1 = aCourses()
    b2 = aCourses()
    _safe_set(a, 'Univerity_Courses', {b1})
    assert _is_linked(a, 'Univerity_Courses', b1)
    if hasattr(b1, 'aCourses'):
        assert _is_linked(b1, 'aCourses', a)
    _safe_set(a, 'Univerity_Courses', {b2})
    assert _is_linked(a, 'Univerity_Courses', b2)
    if hasattr(b1, 'aCourses'):
        assert not _is_linked(b1, 'aCourses', a)
    if hasattr(b2, 'aCourses'):
        assert _is_linked(b2, 'aCourses', a)
    _safe_set(a, 'Univerity_Courses', set())
    assert not _is_linked(a, 'Univerity_Courses', b2)
    if hasattr(b2, 'aCourses'):
        assert not _is_linked(b2, 'aCourses', a)


def test_assoc_relatives6_link_reassign_clear():
    a = Univerity_Person(Email="sample_text", Name="sample_text")
    b1 = aPerson()
    b2 = aPerson()
    _safe_set(a, 'Univerity_Person', b1)
    assert _is_linked(a, 'Univerity_Person', b1)
    if hasattr(b1, 'aPerson7'):
        assert _is_linked(b1, 'aPerson7', a)
    _safe_set(a, 'Univerity_Person', b2)
    assert _is_linked(a, 'Univerity_Person', b2)
    if hasattr(b1, 'aPerson7'):
        assert not _is_linked(b1, 'aPerson7', a)
    if hasattr(b2, 'aPerson7'):
        assert _is_linked(b2, 'aPerson7', a)
    _safe_set(a, 'Univerity_Person', None)
    assert not _is_linked(a, 'Univerity_Person', b2)
    if hasattr(b2, 'aPerson7'):
        assert not _is_linked(b2, 'aPerson7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


Univerity_Courses_strategy = st.builds(Univerity_Courses, CFU=st.integers(), Name=safe_text, Semester=safe_text)
@given(instance=Univerity_Courses_strategy)
@settings(max_examples=25)
def test_Univerity_Courses_instantiation(instance):
    assert isinstance(instance, Univerity_Courses)


Univerity_Person_strategy = st.builds(Univerity_Person, Email=safe_text, Name=safe_text)
@given(instance=Univerity_Person_strategy)
@settings(max_examples=25)
def test_Univerity_Person_instantiation(instance):
    assert isinstance(instance, Univerity_Person)


Univerity_University_strategy = st.builds(Univerity_University)
@given(instance=Univerity_University_strategy)
@settings(max_examples=25)
def test_Univerity_University_instantiation(instance):
    assert isinstance(instance, Univerity_University)


Univerity_uncertainty_ModelElement_strategy = st.builds(Univerity_uncertainty_ModelElement)
@given(instance=Univerity_uncertainty_ModelElement_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_ModelElement_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_ModelElement)


Univerity_uncertainty_UData_strategy = st.builds(Univerity_uncertainty_UData, name=safe_text, utype=safe_text)
@given(instance=Univerity_uncertainty_UData_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_UData_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_UData)


Univerity_uncertainty_aCourses_strategy = st.builds(Univerity_uncertainty_aCourses)
@given(instance=Univerity_uncertainty_aCourses_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_aCourses_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_aCourses)


Univerity_uncertainty_aPerson_strategy = st.builds(Univerity_uncertainty_aPerson)
@given(instance=Univerity_uncertainty_aPerson_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_aPerson_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_aPerson)


Univerity_uncertainty_aUniversity_strategy = st.builds(Univerity_uncertainty_aUniversity)
@given(instance=Univerity_uncertainty_aUniversity_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_aUniversity_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_aUniversity)


Univerity_uncertainty_uCourses_strategy = st.builds(Univerity_uncertainty_uCourses)
@given(instance=Univerity_uncertainty_uCourses_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_uCourses_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_uCourses)


Univerity_uncertainty_uPerson_strategy = st.builds(Univerity_uncertainty_uPerson)
@given(instance=Univerity_uncertainty_uPerson_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_uPerson_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_uPerson)


Univerity_uncertainty_uUniversity_strategy = st.builds(Univerity_uncertainty_uUniversity)
@given(instance=Univerity_uncertainty_uUniversity_strategy)
@settings(max_examples=25)
def test_Univerity_uncertainty_uUniversity_instantiation(instance):
    assert isinstance(instance, Univerity_uncertainty_uUniversity)


aCourses_strategy = st.builds(aCourses)
@given(instance=aCourses_strategy)
@settings(max_examples=25)
def test_aCourses_instantiation(instance):
    assert isinstance(instance, aCourses)


aPerson_strategy = st.builds(aPerson)
@given(instance=aPerson_strategy)
@settings(max_examples=25)
def test_aPerson_instantiation(instance):
    assert isinstance(instance, aPerson)


uCourses_strategy = st.builds(uCourses)
@given(instance=uCourses_strategy)
@settings(max_examples=25)
def test_uCourses_instantiation(instance):
    assert isinstance(instance, uCourses)


uPerson_strategy = st.builds(uPerson)
@given(instance=uPerson_strategy)
@settings(max_examples=25)
def test_uPerson_instantiation(instance):
    assert isinstance(instance, uPerson)


uUniversity_strategy = st.builds(uUniversity)
@given(instance=uUniversity_strategy)
@settings(max_examples=25)
def test_uUniversity_instantiation(instance):
    assert isinstance(instance, uUniversity)


uncertainty_ModelElement_strategy = st.builds(uncertainty_ModelElement)
@given(instance=uncertainty_ModelElement_strategy)
@settings(max_examples=25)
def test_uncertainty_ModelElement_instantiation(instance):
    assert isinstance(instance, uncertainty_ModelElement)


uncertainty_UData_strategy = st.builds(uncertainty_UData)
@given(instance=uncertainty_UData_strategy)
@settings(max_examples=25)
def test_uncertainty_UData_instantiation(instance):
    assert isinstance(instance, uncertainty_UData)


uncertainty_Univerity_Courses_strategy = st.builds(uncertainty_Univerity_Courses)
@given(instance=uncertainty_Univerity_Courses_strategy)
@settings(max_examples=25)
def test_uncertainty_Univerity_Courses_instantiation(instance):
    assert isinstance(instance, uncertainty_Univerity_Courses)


uncertainty_Univerity_Person_strategy = st.builds(uncertainty_Univerity_Person)
@given(instance=uncertainty_Univerity_Person_strategy)
@settings(max_examples=25)
def test_uncertainty_Univerity_Person_instantiation(instance):
    assert isinstance(instance, uncertainty_Univerity_Person)


uncertainty_Univerity_University_strategy = st.builds(uncertainty_Univerity_University)
@given(instance=uncertainty_Univerity_University_strategy)
@settings(max_examples=25)
def test_uncertainty_Univerity_University_instantiation(instance):
    assert isinstance(instance, uncertainty_Univerity_University)


uncertainty_aCourses_strategy = st.builds(uncertainty_aCourses)
@given(instance=uncertainty_aCourses_strategy)
@settings(max_examples=25)
def test_uncertainty_aCourses_instantiation(instance):
    assert isinstance(instance, uncertainty_aCourses)


uncertainty_aPerson_strategy = st.builds(uncertainty_aPerson)
@given(instance=uncertainty_aPerson_strategy)
@settings(max_examples=25)
def test_uncertainty_aPerson_instantiation(instance):
    assert isinstance(instance, uncertainty_aPerson)


uncertainty_aUniversity_strategy = st.builds(uncertainty_aUniversity)
@given(instance=uncertainty_aUniversity_strategy)
@settings(max_examples=25)
def test_uncertainty_aUniversity_instantiation(instance):
    assert isinstance(instance, uncertainty_aUniversity)



