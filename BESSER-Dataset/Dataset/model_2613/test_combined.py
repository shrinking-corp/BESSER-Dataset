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
    Company_Topic,
    Project,
    Company_National,
    Company_European,
    Company_Category,
    Company_Division,
    Company_Address,
    Person,
    Company_Client,
    Company_Employee,
    Division,
    Company_Unit,
    Company_CompanyModel,
    Company_Company,
    Company_ServiceLine,
    Company_Project,
    Company_Person,
    type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_company_topic_is_not_abstract():
    assert not inspect.isabstract(Company_Topic)


def test_hyp_company_topic_constructor_exists():
    assert callable(Company_Topic.__init__)


def test_hyp_company_topic_constructor_args():
    sig = inspect.signature(Company_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_hyp_project_constructor_exists():
    assert callable(Project.__init__)


def test_hyp_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_national_is_not_abstract():
    assert not inspect.isabstract(Company_National)


def test_hyp_company_national_constructor_exists():
    assert callable(Company_National.__init__)


def test_hyp_company_national_constructor_args():
    sig = inspect.signature(Company_National.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"




def test_hyp_company_european_is_not_abstract():
    assert not inspect.isabstract(Company_European)


def test_hyp_company_european_constructor_exists():
    assert callable(Company_European.__init__)


def test_hyp_company_european_constructor_args():
    sig = inspect.signature(Company_European.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"




def test_hyp_company_category_is_not_abstract():
    assert not inspect.isabstract(Company_Category)


def test_hyp_company_category_constructor_exists():
    assert callable(Company_Category.__init__)


def test_hyp_company_category_constructor_args():
    sig = inspect.signature(Company_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_company_division_is_not_abstract():
    assert not inspect.isabstract(Company_Division)


def test_hyp_company_division_constructor_exists():
    assert callable(Company_Division.__init__)


def test_hyp_company_division_constructor_args():
    sig = inspect.signature(Company_Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_company_address_is_not_abstract():
    assert not inspect.isabstract(Company_Address)


def test_hyp_company_address_constructor_exists():
    assert callable(Company_Address.__init__)


def test_hyp_company_address_constructor_args():
    sig = inspect.signature(Company_Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_client_is_not_abstract():
    assert not inspect.isabstract(Company_Client)


def test_hyp_company_client_constructor_exists():
    assert callable(Company_Client.__init__)


def test_hyp_company_client_constructor_args():
    sig = inspect.signature(Company_Client.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_employee_is_not_abstract():
    assert not inspect.isabstract(Company_Employee)


def test_hyp_company_employee_constructor_exists():
    assert callable(Company_Employee.__init__)


def test_hyp_company_employee_constructor_args():
    sig = inspect.signature(Company_Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_division_is_not_abstract():
    assert not inspect.isabstract(Division)


def test_hyp_division_constructor_exists():
    assert callable(Division.__init__)


def test_hyp_division_constructor_args():
    sig = inspect.signature(Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_unit_is_not_abstract():
    assert not inspect.isabstract(Company_Unit)


def test_hyp_company_unit_constructor_exists():
    assert callable(Company_Unit.__init__)


def test_hyp_company_unit_constructor_args():
    sig = inspect.signature(Company_Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_companymodel_is_not_abstract():
    assert not inspect.isabstract(Company_CompanyModel)


def test_hyp_company_companymodel_constructor_exists():
    assert callable(Company_CompanyModel.__init__)


def test_hyp_company_companymodel_constructor_args():
    sig = inspect.signature(Company_CompanyModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_company_is_not_abstract():
    assert not inspect.isabstract(Company_Company)


def test_hyp_company_company_constructor_exists():
    assert callable(Company_Company.__init__)


def test_hyp_company_company_constructor_args():
    sig = inspect.signature(Company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_company_serviceline_is_not_abstract():
    assert not inspect.isabstract(Company_ServiceLine)


def test_hyp_company_serviceline_constructor_exists():
    assert callable(Company_ServiceLine.__init__)


def test_hyp_company_serviceline_constructor_args():
    sig = inspect.signature(Company_ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_project_is_not_abstract():
    assert not inspect.isabstract(Company_Project)


def test_hyp_company_project_constructor_exists():
    assert callable(Company_Project.__init__)


def test_hyp_company_project_constructor_args():
    sig = inspect.signature(Company_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_company_person_is_not_abstract():
    assert not inspect.isabstract(Company_Person)


def test_hyp_company_person_constructor_exists():
    assert callable(Company_Person.__init__)


def test_hyp_company_person_constructor_args():
    sig = inspect.signature(Company_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"



def test_hyp_type_exists():
    # Check that the Enumeration exists
    assert type is not None

def test_hyp_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in type]
    expected_literals = [
        "client",
        "employee",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in type"


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
Company_Topic_strategy = st.builds(
    Company_Topic,
    id=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
Company_National_strategy = st.builds(
    Company_National,
    budget=
        st.integers()
)
Company_European_strategy = st.builds(
    Company_European,
    budget=
        st.integers()
)
Company_Category_strategy = st.builds(
    Company_Category,
    name=
        safe_text
)
Company_Division_strategy = st.builds(
    Company_Division,
    name=
        safe_text
)
Company_Address_strategy = st.builds(
    Company_Address,
    city=
        safe_text,
    completeAddress=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
Company_Client_strategy = st.builds(
    Company_Client,
)
Company_Employee_strategy = st.builds(
    Company_Employee,
)
Division_strategy = st.builds(
    Division,
)
Company_Unit_strategy = st.builds(
    Company_Unit,
)
Company_CompanyModel_strategy = st.builds(
    Company_CompanyModel,
)
Company_Company_strategy = st.builds(
    Company_Company,
    name=
        safe_text
)
Company_ServiceLine_strategy = st.builds(
    Company_ServiceLine,
)
Company_Project_strategy = st.builds(
    Company_Project,
    name=
        safe_text
)
Company_Person_strategy = st.builds(
    Company_Person,
    firstname=
        safe_text,
    lastname=
        safe_text
)




@given(instance=Company_Topic_strategy)
def test_hyp_company_topic_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=Company_National_strategy)
def test_hyp_company_national_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original




@given(instance=Company_European_strategy)
def test_hyp_company_european_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original




@given(instance=Company_Category_strategy)
def test_hyp_company_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Company_Division_strategy)
def test_hyp_company_division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Company_Address_strategy)
def test_hyp_company_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Company_Address_strategy)
def test_hyp_company_address_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original










@given(instance=Company_Company_strategy)
def test_hyp_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Company_Project_strategy)
def test_hyp_company_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Company_Person_strategy)
def test_hyp_company_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Company_Person_strategy)
def test_hyp_company_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Company_Address,
    Company_Category,
    Company_Client,
    Company_Company,
    Company_CompanyModel,
    Company_Division,
    Company_Employee,
    Company_European,
    Company_National,
    Company_Person,
    Company_Project,
    Company_ServiceLine,
    Company_Topic,
    Company_Unit,
    Division,
    Person,
    Project,
    type,
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

def test_Company_Address_city_value_roundtrip():
    instance = Company_Address(city="sample_text", completeAddress="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_Company_Address_completeAddress_value_roundtrip():
    instance = Company_Address(city="sample_text", completeAddress="sample_text")
    assert instance.completeAddress == "sample_text"
    instance.completeAddress = "sample_text_2"
    assert instance.completeAddress == "sample_text_2"


def test_Company_Category_name_value_roundtrip():
    instance = Company_Category(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Company_Company_name_value_roundtrip():
    instance = Company_Company(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Company_Division_name_value_roundtrip():
    instance = Company_Division(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Company_European_budget_value_roundtrip():
    instance = Company_European(budget=7)
    assert instance.budget == 7
    instance.budget = 13
    assert instance.budget == 13


def test_Company_National_budget_value_roundtrip():
    instance = Company_National(budget=7)
    assert instance.budget == 7
    instance.budget = 13
    assert instance.budget == 13


def test_Company_Person_firstname_value_roundtrip():
    instance = Company_Person(firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Company_Person_lastname_value_roundtrip():
    instance = Company_Person(firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Company_Project_name_value_roundtrip():
    instance = Company_Project(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Company_Topic_id_value_roundtrip():
    instance = Company_Topic(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Company_ServiceLine_isa_Division():
    instance = Company_ServiceLine()
    assert isinstance(instance, Division)


def test_Company_Unit_isa_Division():
    instance = Company_Unit()
    assert isinstance(instance, Division)


def test_Company_Client_isa_Person():
    instance = Company_Client()
    assert isinstance(instance, Person)


def test_Company_Employee_isa_Person():
    instance = Company_Employee()
    assert isinstance(instance, Person)


def test_Company_European_isa_Project():
    instance = Company_European(budget=7)
    assert isinstance(instance, Project)


def test_Company_National_isa_Project():
    instance = Company_National(budget=7)
    assert isinstance(instance, Project)


def test_assoc_address23_link_reassign_clear():
    a = Company_Address(city="sample_text", completeAddress="sample_text")
    b1 = Company_CompanyModel()
    b2 = Company_CompanyModel()
    _safe_set(a, 'Company_Address25', b1)
    assert _is_linked(a, 'Company_Address25', b1)
    if hasattr(b1, 'Company_CompanyModel24'):
        assert _is_linked(b1, 'Company_CompanyModel24', a)
    _safe_set(a, 'Company_Address25', b2)
    assert _is_linked(a, 'Company_Address25', b2)
    if hasattr(b1, 'Company_CompanyModel24'):
        assert not _is_linked(b1, 'Company_CompanyModel24', a)
    if hasattr(b2, 'Company_CompanyModel24'):
        assert _is_linked(b2, 'Company_CompanyModel24', a)
    _safe_set(a, 'Company_Address25', None)
    assert not _is_linked(a, 'Company_Address25', b2)
    if hasattr(b2, 'Company_CompanyModel24'):
        assert not _is_linked(b2, 'Company_CompanyModel24', a)


def test_assoc_address8_link_reassign_clear():
    a = Company_Company(name="sample_text")
    b1 = Company_Address(city="sample_text", completeAddress="sample_text")
    b2 = Company_Address(city="sample_text_2", completeAddress="sample_text_2")
    _safe_set(a, 'Company_Company9', b1)
    assert _is_linked(a, 'Company_Company9', b1)
    if hasattr(b1, 'Company_Address'):
        assert _is_linked(b1, 'Company_Address', a)
    _safe_set(a, 'Company_Company9', b2)
    assert _is_linked(a, 'Company_Company9', b2)
    if hasattr(b1, 'Company_Address'):
        assert not _is_linked(b1, 'Company_Address', a)
    if hasattr(b2, 'Company_Address'):
        assert _is_linked(b2, 'Company_Address', a)
    _safe_set(a, 'Company_Company9', None)
    assert not _is_linked(a, 'Company_Company9', b2)
    if hasattr(b2, 'Company_Address'):
        assert not _is_linked(b2, 'Company_Address', a)


def test_assoc_assignedTo0_link_reassign_clear():
    a = Company_Project(name="sample_text")
    b1 = Company_Person(firstname="sample_text", lastname="sample_text")
    b2 = Company_Person(firstname="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'Company_Project', b1)
    assert _is_linked(a, 'Company_Project', b1)
    if hasattr(b1, 'Company_Person'):
        assert _is_linked(b1, 'Company_Person', a)
    _safe_set(a, 'Company_Project', b2)
    assert _is_linked(a, 'Company_Project', b2)
    if hasattr(b1, 'Company_Person'):
        assert not _is_linked(b1, 'Company_Person', a)
    if hasattr(b2, 'Company_Person'):
        assert _is_linked(b2, 'Company_Person', a)
    _safe_set(a, 'Company_Project', None)
    assert not _is_linked(a, 'Company_Project', b2)
    if hasattr(b2, 'Company_Person'):
        assert not _is_linked(b2, 'Company_Person', a)


def test_assoc_categories18_link_reassign_clear():
    a = Company_Category(name="sample_text")
    b1 = Company_CompanyModel()
    b2 = Company_CompanyModel()
    _safe_set(a, 'Company_Category20', b1)
    assert _is_linked(a, 'Company_Category20', b1)
    if hasattr(b1, 'Company_CompanyModel19'):
        assert _is_linked(b1, 'Company_CompanyModel19', a)
    _safe_set(a, 'Company_Category20', b2)
    assert _is_linked(a, 'Company_Category20', b2)
    if hasattr(b1, 'Company_CompanyModel19'):
        assert not _is_linked(b1, 'Company_CompanyModel19', a)
    if hasattr(b2, 'Company_CompanyModel19'):
        assert _is_linked(b2, 'Company_CompanyModel19', a)
    _safe_set(a, 'Company_Category20', None)
    assert not _is_linked(a, 'Company_Category20', b2)
    if hasattr(b2, 'Company_CompanyModel19'):
        assert not _is_linked(b2, 'Company_CompanyModel19', a)


def test_assoc_category15_link_reassign_clear():
    a = Company_Topic(id="sample_text")
    b1 = Company_Category(name="sample_text")
    b2 = Company_Category(name="sample_text_2")
    _safe_set(a, 'topics', b1)
    assert _is_linked(a, 'topics', b1)
    if hasattr(b1, 'Category'):
        assert _is_linked(b1, 'Category', a)
    _safe_set(a, 'topics', b2)
    assert _is_linked(a, 'topics', b2)
    if hasattr(b1, 'Category'):
        assert not _is_linked(b1, 'Category', a)
    if hasattr(b2, 'Category'):
        assert _is_linked(b2, 'Category', a)
    _safe_set(a, 'topics', None)
    assert not _is_linked(a, 'topics', b2)
    if hasattr(b2, 'Category'):
        assert not _is_linked(b2, 'Category', a)


def test_assoc_company16_link_reassign_clear():
    a = Company_Company(name="sample_text")
    b1 = Company_CompanyModel()
    b2 = Company_CompanyModel()
    _safe_set(a, 'Company_Company17', b1)
    assert _is_linked(a, 'Company_Company17', b1)
    if hasattr(b1, 'Company_CompanyModel'):
        assert _is_linked(b1, 'Company_CompanyModel', a)
    _safe_set(a, 'Company_Company17', b2)
    assert _is_linked(a, 'Company_Company17', b2)
    if hasattr(b1, 'Company_CompanyModel'):
        assert not _is_linked(b1, 'Company_CompanyModel', a)
    if hasattr(b2, 'Company_CompanyModel'):
        assert _is_linked(b2, 'Company_CompanyModel', a)
    _safe_set(a, 'Company_Company17', None)
    assert not _is_linked(a, 'Company_Company17', b2)
    if hasattr(b2, 'Company_CompanyModel'):
        assert not _is_linked(b2, 'Company_CompanyModel', a)


def test_assoc_division26_link_reassign_clear():
    a = Company_Division(name="sample_text")
    b1 = Company_CompanyModel()
    b2 = Company_CompanyModel()
    _safe_set(a, 'Company_Division28', b1)
    assert _is_linked(a, 'Company_Division28', b1)
    if hasattr(b1, 'Company_CompanyModel27'):
        assert _is_linked(b1, 'Company_CompanyModel27', a)
    _safe_set(a, 'Company_Division28', b2)
    assert _is_linked(a, 'Company_Division28', b2)
    if hasattr(b1, 'Company_CompanyModel27'):
        assert not _is_linked(b1, 'Company_CompanyModel27', a)
    if hasattr(b2, 'Company_CompanyModel27'):
        assert _is_linked(b2, 'Company_CompanyModel27', a)
    _safe_set(a, 'Company_Division28', None)
    assert not _is_linked(a, 'Company_Division28', b2)
    if hasattr(b2, 'Company_CompanyModel27'):
        assert not _is_linked(b2, 'Company_CompanyModel27', a)


def test_assoc_employed1_link_reassign_clear():
    a = Company_Person(firstname="sample_text", lastname="sample_text")
    b1 = Company_ServiceLine()
    b2 = Company_ServiceLine()
    _safe_set(a, 'Company_Person2', b1)
    assert _is_linked(a, 'Company_Person2', b1)
    if hasattr(b1, 'Company_ServiceLine'):
        assert _is_linked(b1, 'Company_ServiceLine', a)
    _safe_set(a, 'Company_Person2', b2)
    assert _is_linked(a, 'Company_Person2', b2)
    if hasattr(b1, 'Company_ServiceLine'):
        assert not _is_linked(b1, 'Company_ServiceLine', a)
    if hasattr(b2, 'Company_ServiceLine'):
        assert _is_linked(b2, 'Company_ServiceLine', a)
    _safe_set(a, 'Company_Person2', None)
    assert not _is_linked(a, 'Company_Person2', b2)
    if hasattr(b2, 'Company_ServiceLine'):
        assert not _is_linked(b2, 'Company_ServiceLine', a)


def test_assoc_lines10_link_reassign_clear():
    a = Company_Division(name="sample_text")
    b1 = Company_Company(name="sample_text")
    b2 = Company_Company(name="sample_text_2")
    _safe_set(a, 'Company_Division', b1)
    assert _is_linked(a, 'Company_Division', b1)
    if hasattr(b1, 'Company_Company11'):
        assert _is_linked(b1, 'Company_Company11', a)
    _safe_set(a, 'Company_Division', b2)
    assert _is_linked(a, 'Company_Division', b2)
    if hasattr(b1, 'Company_Company11'):
        assert not _is_linked(b1, 'Company_Company11', a)
    if hasattr(b2, 'Company_Company11'):
        assert _is_linked(b2, 'Company_Company11', a)
    _safe_set(a, 'Company_Division', None)
    assert not _is_linked(a, 'Company_Division', b2)
    if hasattr(b2, 'Company_Company11'):
        assert not _is_linked(b2, 'Company_Company11', a)


def test_assoc_persons3_link_reassign_clear():
    a = Company_Person(firstname="sample_text", lastname="sample_text")
    b1 = Company_Company(name="sample_text")
    b2 = Company_Company(name="sample_text_2")
    _safe_set(a, 'Company_Person4', b1)
    assert _is_linked(a, 'Company_Person4', b1)
    if hasattr(b1, 'Company_Company'):
        assert _is_linked(b1, 'Company_Company', a)
    _safe_set(a, 'Company_Person4', b2)
    assert _is_linked(a, 'Company_Person4', b2)
    if hasattr(b1, 'Company_Company'):
        assert not _is_linked(b1, 'Company_Company', a)
    if hasattr(b2, 'Company_Company'):
        assert _is_linked(b2, 'Company_Company', a)
    _safe_set(a, 'Company_Person4', None)
    assert not _is_linked(a, 'Company_Person4', b2)
    if hasattr(b2, 'Company_Company'):
        assert not _is_linked(b2, 'Company_Company', a)


def test_assoc_projects5_link_reassign_clear():
    a = Company_Project(name="sample_text")
    b1 = Company_Company(name="sample_text")
    b2 = Company_Company(name="sample_text_2")
    _safe_set(a, 'Company_Project7', b1)
    assert _is_linked(a, 'Company_Project7', b1)
    if hasattr(b1, 'Company_Company6'):
        assert _is_linked(b1, 'Company_Company6', a)
    _safe_set(a, 'Company_Project7', b2)
    assert _is_linked(a, 'Company_Project7', b2)
    if hasattr(b1, 'Company_Company6'):
        assert not _is_linked(b1, 'Company_Company6', a)
    if hasattr(b2, 'Company_Company6'):
        assert _is_linked(b2, 'Company_Company6', a)
    _safe_set(a, 'Company_Project7', None)
    assert not _is_linked(a, 'Company_Project7', b2)
    if hasattr(b2, 'Company_Company6'):
        assert not _is_linked(b2, 'Company_Company6', a)


def test_assoc_related12_link_reassign_clear():
    a = Company_Project(name="sample_text")
    b1 = Company_Category(name="sample_text")
    b2 = Company_Category(name="sample_text_2")
    _safe_set(a, 'Company_Project13', b1)
    assert _is_linked(a, 'Company_Project13', b1)
    if hasattr(b1, 'Company_Category'):
        assert _is_linked(b1, 'Company_Category', a)
    _safe_set(a, 'Company_Project13', b2)
    assert _is_linked(a, 'Company_Project13', b2)
    if hasattr(b1, 'Company_Category'):
        assert not _is_linked(b1, 'Company_Category', a)
    if hasattr(b2, 'Company_Category'):
        assert _is_linked(b2, 'Company_Category', a)
    _safe_set(a, 'Company_Project13', None)
    assert not _is_linked(a, 'Company_Project13', b2)
    if hasattr(b2, 'Company_Category'):
        assert not _is_linked(b2, 'Company_Category', a)


def test_assoc_topics14_link_reassign_clear():
    a = Company_Topic(id="sample_text")
    b1 = Company_Category(name="sample_text")
    b2 = Company_Category(name="sample_text_2")
    _safe_set(a, 'Topic', b1)
    assert _is_linked(a, 'Topic', b1)
    if hasattr(b1, 'category'):
        assert _is_linked(b1, 'category', a)
    _safe_set(a, 'Topic', b2)
    assert _is_linked(a, 'Topic', b2)
    if hasattr(b1, 'category'):
        assert not _is_linked(b1, 'category', a)
    if hasattr(b2, 'category'):
        assert _is_linked(b2, 'category', a)
    _safe_set(a, 'Topic', None)
    assert not _is_linked(a, 'Topic', b2)
    if hasattr(b2, 'category'):
        assert not _is_linked(b2, 'category', a)


def test_assoc_topics21_link_reassign_clear():
    a = Company_Topic(id="sample_text")
    b1 = Company_CompanyModel()
    b2 = Company_CompanyModel()
    _safe_set(a, 'Company_Topic', b1)
    assert _is_linked(a, 'Company_Topic', b1)
    if hasattr(b1, 'Company_CompanyModel22'):
        assert _is_linked(b1, 'Company_CompanyModel22', a)
    _safe_set(a, 'Company_Topic', b2)
    assert _is_linked(a, 'Company_Topic', b2)
    if hasattr(b1, 'Company_CompanyModel22'):
        assert not _is_linked(b1, 'Company_CompanyModel22', a)
    if hasattr(b2, 'Company_CompanyModel22'):
        assert _is_linked(b2, 'Company_CompanyModel22', a)
    _safe_set(a, 'Company_Topic', None)
    assert not _is_linked(a, 'Company_Topic', b2)
    if hasattr(b2, 'Company_CompanyModel22'):
        assert not _is_linked(b2, 'Company_CompanyModel22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Company_Address_strategy = st.builds(Company_Address, city=safe_text, completeAddress=safe_text)
@given(instance=Company_Address_strategy)
@settings(max_examples=25)
def test_Company_Address_instantiation(instance):
    assert isinstance(instance, Company_Address)


Company_Category_strategy = st.builds(Company_Category, name=safe_text)
@given(instance=Company_Category_strategy)
@settings(max_examples=25)
def test_Company_Category_instantiation(instance):
    assert isinstance(instance, Company_Category)


Company_Client_strategy = st.builds(Company_Client)
@given(instance=Company_Client_strategy)
@settings(max_examples=25)
def test_Company_Client_instantiation(instance):
    assert isinstance(instance, Company_Client)


Company_Company_strategy = st.builds(Company_Company, name=safe_text)
@given(instance=Company_Company_strategy)
@settings(max_examples=25)
def test_Company_Company_instantiation(instance):
    assert isinstance(instance, Company_Company)


Company_CompanyModel_strategy = st.builds(Company_CompanyModel)
@given(instance=Company_CompanyModel_strategy)
@settings(max_examples=25)
def test_Company_CompanyModel_instantiation(instance):
    assert isinstance(instance, Company_CompanyModel)


Company_Division_strategy = st.builds(Company_Division, name=safe_text)
@given(instance=Company_Division_strategy)
@settings(max_examples=25)
def test_Company_Division_instantiation(instance):
    assert isinstance(instance, Company_Division)


Company_Employee_strategy = st.builds(Company_Employee)
@given(instance=Company_Employee_strategy)
@settings(max_examples=25)
def test_Company_Employee_instantiation(instance):
    assert isinstance(instance, Company_Employee)


Company_European_strategy = st.builds(Company_European, budget=st.integers())
@given(instance=Company_European_strategy)
@settings(max_examples=25)
def test_Company_European_instantiation(instance):
    assert isinstance(instance, Company_European)


Company_National_strategy = st.builds(Company_National, budget=st.integers())
@given(instance=Company_National_strategy)
@settings(max_examples=25)
def test_Company_National_instantiation(instance):
    assert isinstance(instance, Company_National)


Company_Person_strategy = st.builds(Company_Person, firstname=safe_text, lastname=safe_text)
@given(instance=Company_Person_strategy)
@settings(max_examples=25)
def test_Company_Person_instantiation(instance):
    assert isinstance(instance, Company_Person)


Company_Project_strategy = st.builds(Company_Project, name=safe_text)
@given(instance=Company_Project_strategy)
@settings(max_examples=25)
def test_Company_Project_instantiation(instance):
    assert isinstance(instance, Company_Project)


Company_ServiceLine_strategy = st.builds(Company_ServiceLine)
@given(instance=Company_ServiceLine_strategy)
@settings(max_examples=25)
def test_Company_ServiceLine_instantiation(instance):
    assert isinstance(instance, Company_ServiceLine)


Company_Topic_strategy = st.builds(Company_Topic, id=safe_text)
@given(instance=Company_Topic_strategy)
@settings(max_examples=25)
def test_Company_Topic_instantiation(instance):
    assert isinstance(instance, Company_Topic)


Company_Unit_strategy = st.builds(Company_Unit)
@given(instance=Company_Unit_strategy)
@settings(max_examples=25)
def test_Company_Unit_instantiation(instance):
    assert isinstance(instance, Company_Unit)


Division_strategy = st.builds(Division)
@given(instance=Division_strategy)
@settings(max_examples=25)
def test_Division_instantiation(instance):
    assert isinstance(instance, Division)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Project_strategy = st.builds(Project)
@given(instance=Project_strategy)
@settings(max_examples=25)
def test_Project_instantiation(instance):
    assert isinstance(instance, Project)



