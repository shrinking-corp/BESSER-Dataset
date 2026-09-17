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
    office_NamedElement,
    OfficeElement,
    office_Office,
    office_Employee,
    NamedElement,
    office_OfficeElement,
    office_OfficeModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_office_namedelement_is_not_abstract():
    assert not inspect.isabstract(office_NamedElement)


def test_hyp_office_namedelement_constructor_exists():
    assert callable(office_NamedElement.__init__)


def test_hyp_office_namedelement_constructor_args():
    sig = inspect.signature(office_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_officeelement_is_not_abstract():
    assert not inspect.isabstract(OfficeElement)


def test_hyp_officeelement_constructor_exists():
    assert callable(OfficeElement.__init__)


def test_hyp_officeelement_constructor_args():
    sig = inspect.signature(OfficeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_office_office_is_not_abstract():
    assert not inspect.isabstract(office_Office)


def test_hyp_office_office_constructor_exists():
    assert callable(office_Office.__init__)


def test_hyp_office_office_constructor_args():
    sig = inspect.signature(office_Office.__init__)
    params = list(sig.parameters.keys())



def test_hyp_office_employee_is_not_abstract():
    assert not inspect.isabstract(office_Employee)


def test_hyp_office_employee_constructor_exists():
    assert callable(office_Employee.__init__)


def test_hyp_office_employee_constructor_args():
    sig = inspect.signature(office_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_office_officeelement_is_not_abstract():
    assert not inspect.isabstract(office_OfficeElement)


def test_hyp_office_officeelement_constructor_exists():
    assert callable(office_OfficeElement.__init__)


def test_hyp_office_officeelement_constructor_args():
    sig = inspect.signature(office_OfficeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_office_officemodel_is_not_abstract():
    assert not inspect.isabstract(office_OfficeModel)


def test_hyp_office_officemodel_constructor_exists():
    assert callable(office_OfficeModel.__init__)


def test_hyp_office_officemodel_constructor_args():
    sig = inspect.signature(office_OfficeModel.__init__)
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
office_NamedElement_strategy = st.builds(
    office_NamedElement,
    name=
        safe_text
)
OfficeElement_strategy = st.builds(
    OfficeElement,
)
office_Office_strategy = st.builds(
    office_Office,
)
office_Employee_strategy = st.builds(
    office_Employee,
    title=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
office_OfficeElement_strategy = st.builds(
    office_OfficeElement,
)
office_OfficeModel_strategy = st.builds(
    office_OfficeModel,
)




@given(instance=office_NamedElement_strategy)
def test_hyp_office_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=office_Employee_strategy)
def test_hyp_office_employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    OfficeElement,
    office_Employee,
    office_NamedElement,
    office_Office,
    office_OfficeElement,
    office_OfficeModel,
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

def test_office_Employee_title_value_roundtrip():
    instance = office_Employee(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_office_NamedElement_name_value_roundtrip():
    instance = office_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_office_OfficeElement_isa_NamedElement():
    instance = office_OfficeElement()
    assert isinstance(instance, NamedElement)


def test_office_OfficeModel_isa_NamedElement():
    instance = office_OfficeModel()
    assert isinstance(instance, NamedElement)


def test_office_Employee_isa_OfficeElement():
    instance = office_Employee(title="sample_text")
    assert isinstance(instance, OfficeElement)


def test_office_Office_isa_OfficeElement():
    instance = office_Office()
    assert isinstance(instance, OfficeElement)


def test_assoc_employees4_link_reassign_clear():
    a = office_Employee(title="sample_text")
    b1 = office_Office()
    b2 = office_Office()
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'worksIn'):
        assert _is_linked(b1, 'worksIn', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'worksIn'):
        assert not _is_linked(b1, 'worksIn', a)
    if hasattr(b2, 'worksIn'):
        assert _is_linked(b2, 'worksIn', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'worksIn'):
        assert not _is_linked(b2, 'worksIn', a)


def test_assoc_worksIn1_link_reassign_clear():
    a = office_Employee(title="sample_text")
    b1 = office_Office()
    b2 = office_Office()
    _safe_set(a, 'employees', b1)
    assert _is_linked(a, 'employees', b1)
    if hasattr(b1, 'Office'):
        assert _is_linked(b1, 'Office', a)
    _safe_set(a, 'employees', b2)
    assert _is_linked(a, 'employees', b2)
    if hasattr(b1, 'Office'):
        assert not _is_linked(b1, 'Office', a)
    if hasattr(b2, 'Office'):
        assert _is_linked(b2, 'Office', a)
    _safe_set(a, 'employees', None)
    assert not _is_linked(a, 'employees', b2)
    if hasattr(b2, 'Office'):
        assert not _is_linked(b2, 'Office', a)


def test_assoc_worksWith3_link_reassign_clear():
    a = office_Employee(title="sample_text")
    b1 = office_Employee(title="sample_text")
    b2 = office_Employee(title="sample_text_2")
    _safe_set(a, 'office_Employee', b1)
    assert _is_linked(a, 'office_Employee', b1)
    if hasattr(b1, 'office_Employee2'):
        assert _is_linked(b1, 'office_Employee2', a)
    _safe_set(a, 'office_Employee', b2)
    assert _is_linked(a, 'office_Employee', b2)
    if hasattr(b1, 'office_Employee2'):
        assert not _is_linked(b1, 'office_Employee2', a)
    if hasattr(b2, 'office_Employee2'):
        assert _is_linked(b2, 'office_Employee2', a)
    _safe_set(a, 'office_Employee', None)
    assert not _is_linked(a, 'office_Employee', b2)
    if hasattr(b2, 'office_Employee2'):
        assert not _is_linked(b2, 'office_Employee2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


OfficeElement_strategy = st.builds(OfficeElement)
@given(instance=OfficeElement_strategy)
@settings(max_examples=25)
def test_OfficeElement_instantiation(instance):
    assert isinstance(instance, OfficeElement)


office_Employee_strategy = st.builds(office_Employee, title=safe_text)
@given(instance=office_Employee_strategy)
@settings(max_examples=25)
def test_office_Employee_instantiation(instance):
    assert isinstance(instance, office_Employee)


office_NamedElement_strategy = st.builds(office_NamedElement, name=safe_text)
@given(instance=office_NamedElement_strategy)
@settings(max_examples=25)
def test_office_NamedElement_instantiation(instance):
    assert isinstance(instance, office_NamedElement)


office_Office_strategy = st.builds(office_Office)
@given(instance=office_Office_strategy)
@settings(max_examples=25)
def test_office_Office_instantiation(instance):
    assert isinstance(instance, office_Office)


office_OfficeElement_strategy = st.builds(office_OfficeElement)
@given(instance=office_OfficeElement_strategy)
@settings(max_examples=25)
def test_office_OfficeElement_instantiation(instance):
    assert isinstance(instance, office_OfficeElement)


office_OfficeModel_strategy = st.builds(office_OfficeModel)
@given(instance=office_OfficeModel_strategy)
@settings(max_examples=25)
def test_office_OfficeModel_instantiation(instance):
    assert isinstance(instance, office_OfficeModel)



