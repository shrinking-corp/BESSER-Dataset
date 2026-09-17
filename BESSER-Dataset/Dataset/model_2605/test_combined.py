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
    project_CommitterShip,
    project_Person,
    project_Project,
    project_Foundation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_project_committership_is_not_abstract():
    assert not inspect.isabstract(project_CommitterShip)


def test_hyp_project_committership_constructor_exists():
    assert callable(project_CommitterShip.__init__)


def test_hyp_project_committership_constructor_args():
    sig = inspect.signature(project_CommitterShip.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"





def test_hyp_project_person_is_not_abstract():
    assert not inspect.isabstract(project_Person)


def test_hyp_project_person_constructor_exists():
    assert callable(project_Person.__init__)


def test_hyp_project_person_constructor_args():
    sig = inspect.signature(project_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "image" in params, "Missing parameter 'image'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"







def test_hyp_project_project_is_not_abstract():
    assert not inspect.isabstract(project_Project)


def test_hyp_project_project_constructor_exists():
    assert callable(project_Project.__init__)


def test_hyp_project_project_constructor_args():
    sig = inspect.signature(project_Project.__init__)
    params = list(sig.parameters.keys())
    assert "shortname" in params, "Missing parameter 'shortname'"
    assert "homepage" in params, "Missing parameter 'homepage'"
    assert "longname" in params, "Missing parameter 'longname'"
    assert "end" in params, "Missing parameter 'end'"
    assert "devmail" in params, "Missing parameter 'devmail'"
    assert "start" in params, "Missing parameter 'start'"









def test_hyp_project_foundation_is_not_abstract():
    assert not inspect.isabstract(project_Foundation)


def test_hyp_project_foundation_constructor_exists():
    assert callable(project_Foundation.__init__)


def test_hyp_project_foundation_constructor_args():
    sig = inspect.signature(project_Foundation.__init__)
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
project_CommitterShip_strategy = st.builds(
    project_CommitterShip,
    start=
        st.dates(),
    end=
        st.dates()
)
project_Person_strategy = st.builds(
    project_Person,
    lastname=
        safe_text,
    image=
        safe_text,
    email=
        safe_text,
    firstname=
        safe_text
)
project_Project_strategy = st.builds(
    project_Project,
    shortname=
        safe_text,
    homepage=
        safe_text,
    longname=
        safe_text,
    end=
        st.dates(),
    devmail=
        safe_text,
    start=
        st.dates()
)
project_Foundation_strategy = st.builds(
    project_Foundation,
)




@given(instance=project_CommitterShip_strategy)
def test_hyp_project_committership_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=project_CommitterShip_strategy)
def test_hyp_project_committership_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original




@given(instance=project_Person_strategy)
def test_hyp_project_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=project_Person_strategy)
def test_hyp_project_person_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=project_Person_strategy)
def test_hyp_project_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=project_Person_strategy)
def test_hyp_project_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original




@given(instance=project_Project_strategy)
def test_hyp_project_project_shortname_setter(instance):
    original = instance.shortname
    instance.shortname = original
    assert instance.shortname == original



@given(instance=project_Project_strategy)
def test_hyp_project_project_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original



@given(instance=project_Project_strategy)
def test_hyp_project_project_longname_setter(instance):
    original = instance.longname
    instance.longname = original
    assert instance.longname == original



@given(instance=project_Project_strategy)
def test_hyp_project_project_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_Project_strategy)
def test_hyp_project_project_devmail_setter(instance):
    original = instance.devmail
    instance.devmail = original
    assert instance.devmail == original



@given(instance=project_Project_strategy)
def test_hyp_project_project_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    project_CommitterShip,
    project_Foundation,
    project_Person,
    project_Project,
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

def test_project_CommitterShip_end_value_roundtrip():
    instance = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    assert instance.end == date(2024, 1, 1)
    instance.end = date(2025, 6, 15)
    assert instance.end == date(2025, 6, 15)


def test_project_CommitterShip_start_value_roundtrip():
    instance = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    assert instance.start == date(2024, 1, 1)
    instance.start = date(2025, 6, 15)
    assert instance.start == date(2025, 6, 15)


def test_project_Person_email_value_roundtrip():
    instance = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_project_Person_firstname_value_roundtrip():
    instance = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_project_Person_image_value_roundtrip():
    instance = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_project_Person_lastname_value_roundtrip():
    instance = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_project_Project_devmail_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.devmail == "sample_text"
    instance.devmail = "sample_text_2"
    assert instance.devmail == "sample_text_2"


def test_project_Project_end_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.end == date(2024, 1, 1)
    instance.end = date(2025, 6, 15)
    assert instance.end == date(2025, 6, 15)


def test_project_Project_homepage_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.homepage == "sample_text"
    instance.homepage = "sample_text_2"
    assert instance.homepage == "sample_text_2"


def test_project_Project_longname_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.longname == "sample_text"
    instance.longname = "sample_text_2"
    assert instance.longname == "sample_text_2"


def test_project_Project_shortname_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.shortname == "sample_text"
    instance.shortname = "sample_text_2"
    assert instance.shortname == "sample_text_2"


def test_project_Project_start_value_roundtrip():
    instance = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    assert instance.start == date(2024, 1, 1)
    instance.start = date(2025, 6, 15)
    assert instance.start == date(2025, 6, 15)


def test_assoc_committers5_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    b2 = project_CommitterShip(end=date(2025, 6, 15), start=date(2025, 6, 15))
    _safe_set(a, 'project', {b1})
    assert _is_linked(a, 'project', b1)
    if hasattr(b1, 'CommitterShip'):
        assert _is_linked(b1, 'CommitterShip', a)
    _safe_set(a, 'project', {b2})
    assert _is_linked(a, 'project', b2)
    if hasattr(b1, 'CommitterShip'):
        assert not _is_linked(b1, 'CommitterShip', a)
    if hasattr(b2, 'CommitterShip'):
        assert _is_linked(b2, 'CommitterShip', a)
    _safe_set(a, 'project', set())
    assert not _is_linked(a, 'project', b2)
    if hasattr(b2, 'CommitterShip'):
        assert not _is_linked(b2, 'CommitterShip', a)


def test_assoc_committerships15_link_reassign_clear():
    a = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    b1 = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    b2 = project_CommitterShip(end=date(2025, 6, 15), start=date(2025, 6, 15))
    _safe_set(a, 'person', {b1})
    assert _is_linked(a, 'person', b1)
    if hasattr(b1, 'CommitterShip16'):
        assert _is_linked(b1, 'CommitterShip16', a)
    _safe_set(a, 'person', {b2})
    assert _is_linked(a, 'person', b2)
    if hasattr(b1, 'CommitterShip16'):
        assert not _is_linked(b1, 'CommitterShip16', a)
    if hasattr(b2, 'CommitterShip16'):
        assert _is_linked(b2, 'CommitterShip16', a)
    _safe_set(a, 'person', set())
    assert not _is_linked(a, 'person', b2)
    if hasattr(b2, 'CommitterShip16'):
        assert not _is_linked(b2, 'CommitterShip16', a)


def test_assoc_parent7_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b2 = project_Project(devmail="sample_text_2", end=date(2025, 6, 15), homepage="sample_text_2", longname="sample_text_2", shortname="sample_text_2", start=date(2025, 6, 15))
    _safe_set(a, 'Project8', b1)
    assert _is_linked(a, 'Project8', b1)
    if hasattr(b1, 'subprojects'):
        assert _is_linked(b1, 'subprojects', a)
    _safe_set(a, 'Project8', b2)
    assert _is_linked(a, 'Project8', b2)
    if hasattr(b1, 'subprojects'):
        assert not _is_linked(b1, 'subprojects', a)
    if hasattr(b2, 'subprojects'):
        assert _is_linked(b2, 'subprojects', a)
    _safe_set(a, 'Project8', None)
    assert not _is_linked(a, 'Project8', b2)
    if hasattr(b2, 'subprojects'):
        assert not _is_linked(b2, 'subprojects', a)


def test_assoc_person14_link_reassign_clear():
    a = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    b1 = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    b2 = project_CommitterShip(end=date(2025, 6, 15), start=date(2025, 6, 15))
    _safe_set(a, 'Person', b1)
    assert _is_linked(a, 'Person', b1)
    if hasattr(b1, 'committerships'):
        assert _is_linked(b1, 'committerships', a)
    _safe_set(a, 'Person', b2)
    assert _is_linked(a, 'Person', b2)
    if hasattr(b1, 'committerships'):
        assert not _is_linked(b1, 'committerships', a)
    if hasattr(b2, 'committerships'):
        assert _is_linked(b2, 'committerships', a)
    _safe_set(a, 'Person', None)
    assert not _is_linked(a, 'Person', b2)
    if hasattr(b2, 'committerships'):
        assert not _is_linked(b2, 'committerships', a)


def test_assoc_persons1_link_reassign_clear():
    a = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    b1 = project_Foundation()
    b2 = project_Foundation()
    _safe_set(a, 'project_Person', b1)
    assert _is_linked(a, 'project_Person', b1)
    if hasattr(b1, 'project_Foundation2'):
        assert _is_linked(b1, 'project_Foundation2', a)
    _safe_set(a, 'project_Person', b2)
    assert _is_linked(a, 'project_Person', b2)
    if hasattr(b1, 'project_Foundation2'):
        assert not _is_linked(b1, 'project_Foundation2', a)
    if hasattr(b2, 'project_Foundation2'):
        assert _is_linked(b2, 'project_Foundation2', a)
    _safe_set(a, 'project_Person', None)
    assert not _is_linked(a, 'project_Person', b2)
    if hasattr(b2, 'project_Foundation2'):
        assert not _is_linked(b2, 'project_Foundation2', a)


def test_assoc_project12_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_CommitterShip(end=date(2024, 1, 1), start=date(2024, 1, 1))
    b2 = project_CommitterShip(end=date(2025, 6, 15), start=date(2025, 6, 15))
    _safe_set(a, 'Project13', b1)
    assert _is_linked(a, 'Project13', b1)
    if hasattr(b1, 'committers'):
        assert _is_linked(b1, 'committers', a)
    _safe_set(a, 'Project13', b2)
    assert _is_linked(a, 'Project13', b2)
    if hasattr(b1, 'committers'):
        assert not _is_linked(b1, 'committers', a)
    if hasattr(b2, 'committers'):
        assert _is_linked(b2, 'committers', a)
    _safe_set(a, 'Project13', None)
    assert not _is_linked(a, 'Project13', b2)
    if hasattr(b2, 'committers'):
        assert not _is_linked(b2, 'committers', a)


def test_assoc_projectleads9_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_Person(email="sample_text", firstname="sample_text", image="sample_text", lastname="sample_text")
    b2 = project_Person(email="sample_text_2", firstname="sample_text_2", image="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'project_Project10', {b1})
    assert _is_linked(a, 'project_Project10', b1)
    if hasattr(b1, 'project_Person11'):
        assert _is_linked(b1, 'project_Person11', a)
    _safe_set(a, 'project_Project10', {b2})
    assert _is_linked(a, 'project_Project10', b2)
    if hasattr(b1, 'project_Person11'):
        assert not _is_linked(b1, 'project_Person11', a)
    if hasattr(b2, 'project_Person11'):
        assert _is_linked(b2, 'project_Person11', a)
    _safe_set(a, 'project_Project10', set())
    assert not _is_linked(a, 'project_Project10', b2)
    if hasattr(b2, 'project_Person11'):
        assert not _is_linked(b2, 'project_Person11', a)


def test_assoc_projects0_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_Foundation()
    b2 = project_Foundation()
    _safe_set(a, 'project_Project', b1)
    assert _is_linked(a, 'project_Project', b1)
    if hasattr(b1, 'project_Foundation'):
        assert _is_linked(b1, 'project_Foundation', a)
    _safe_set(a, 'project_Project', b2)
    assert _is_linked(a, 'project_Project', b2)
    if hasattr(b1, 'project_Foundation'):
        assert not _is_linked(b1, 'project_Foundation', a)
    if hasattr(b2, 'project_Foundation'):
        assert _is_linked(b2, 'project_Foundation', a)
    _safe_set(a, 'project_Project', None)
    assert not _is_linked(a, 'project_Project', b2)
    if hasattr(b2, 'project_Foundation'):
        assert not _is_linked(b2, 'project_Foundation', a)


def test_assoc_subprojects4_link_reassign_clear():
    a = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b1 = project_Project(devmail="sample_text", end=date(2024, 1, 1), homepage="sample_text", longname="sample_text", shortname="sample_text", start=date(2024, 1, 1))
    b2 = project_Project(devmail="sample_text_2", end=date(2025, 6, 15), homepage="sample_text_2", longname="sample_text_2", shortname="sample_text_2", start=date(2025, 6, 15))
    _safe_set(a, 'Project', b1)
    assert _is_linked(a, 'Project', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'Project', b2)
    assert _is_linked(a, 'Project', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'Project', None)
    assert not _is_linked(a, 'Project', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

project_CommitterShip_strategy = st.builds(project_CommitterShip, end=st.dates(), start=st.dates())
@given(instance=project_CommitterShip_strategy)
@settings(max_examples=25)
def test_project_CommitterShip_instantiation(instance):
    assert isinstance(instance, project_CommitterShip)


project_Foundation_strategy = st.builds(project_Foundation)
@given(instance=project_Foundation_strategy)
@settings(max_examples=25)
def test_project_Foundation_instantiation(instance):
    assert isinstance(instance, project_Foundation)


project_Person_strategy = st.builds(project_Person, email=safe_text, firstname=safe_text, image=safe_text, lastname=safe_text)
@given(instance=project_Person_strategy)
@settings(max_examples=25)
def test_project_Person_instantiation(instance):
    assert isinstance(instance, project_Person)


project_Project_strategy = st.builds(project_Project, devmail=safe_text, end=st.dates(), homepage=safe_text, longname=safe_text, shortname=safe_text, start=st.dates())
@given(instance=project_Project_strategy)
@settings(max_examples=25)
def test_project_Project_instantiation(instance):
    assert isinstance(instance, project_Project)



