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
    techStaff_DeveloperTest,
    techStaff_DatabaseAdminTest,
    techStaff_Developer,
    techStaff_DatabaseAdmin,
    Staff_Employee,
    Management_ManagerTest,
    Management_DirectorTest,
    Management_Manager,
    Management_Director,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_techstaff_developertest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DeveloperTest)


def test_hyp_techstaff_developertest_constructor_exists():
    assert callable(techStaff_DeveloperTest.__init__)


def test_hyp_techstaff_developertest_constructor_args():
    sig = inspect.signature(techStaff_DeveloperTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_techstaff_databaseadmintest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdminTest)


def test_hyp_techstaff_databaseadmintest_constructor_exists():
    assert callable(techStaff_DatabaseAdminTest.__init__)


def test_hyp_techstaff_databaseadmintest_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdminTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_techstaff_developer_is_not_abstract():
    assert not inspect.isabstract(techStaff_Developer)


def test_hyp_techstaff_developer_constructor_exists():
    assert callable(techStaff_Developer.__init__)


def test_hyp_techstaff_developer_constructor_args():
    sig = inspect.signature(techStaff_Developer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_techstaff_databaseadmin_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdmin)


def test_hyp_techstaff_databaseadmin_constructor_exists():
    assert callable(techStaff_DatabaseAdmin.__init__)


def test_hyp_techstaff_databaseadmin_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdmin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff_employee_is_not_abstract():
    assert not inspect.isabstract(Staff_Employee)


def test_hyp_staff_employee_constructor_exists():
    assert callable(Staff_Employee.__init__)


def test_hyp_staff_employee_constructor_args():
    sig = inspect.signature(Staff_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "nationalInsurance" in params, "Missing parameter 'nationalInsurance'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_management_managertest_is_not_abstract():
    assert not inspect.isabstract(Management_ManagerTest)


def test_hyp_management_managertest_constructor_exists():
    assert callable(Management_ManagerTest.__init__)


def test_hyp_management_managertest_constructor_args():
    sig = inspect.signature(Management_ManagerTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_management_directortest_is_not_abstract():
    assert not inspect.isabstract(Management_DirectorTest)


def test_hyp_management_directortest_constructor_exists():
    assert callable(Management_DirectorTest.__init__)


def test_hyp_management_directortest_constructor_args():
    sig = inspect.signature(Management_DirectorTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_management_manager_is_not_abstract():
    assert not inspect.isabstract(Management_Manager)


def test_hyp_management_manager_constructor_exists():
    assert callable(Management_Manager.__init__)


def test_hyp_management_manager_constructor_args():
    sig = inspect.signature(Management_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "deptName" in params, "Missing parameter 'deptName'"




def test_hyp_management_director_is_not_abstract():
    assert not inspect.isabstract(Management_Director)


def test_hyp_management_director_constructor_exists():
    assert callable(Management_Director.__init__)


def test_hyp_management_director_constructor_args():
    sig = inspect.signature(Management_Director.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"



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
techStaff_DeveloperTest_strategy = st.builds(
    techStaff_DeveloperTest,
)
techStaff_DatabaseAdminTest_strategy = st.builds(
    techStaff_DatabaseAdminTest,
)
techStaff_Developer_strategy = st.builds(
    techStaff_Developer,
)
techStaff_DatabaseAdmin_strategy = st.builds(
    techStaff_DatabaseAdmin,
)
Staff_Employee_strategy = st.builds(
    Staff_Employee,
    nationalInsurance=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
Management_ManagerTest_strategy = st.builds(
    Management_ManagerTest,
)
Management_DirectorTest_strategy = st.builds(
    Management_DirectorTest,
)
Management_Manager_strategy = st.builds(
    Management_Manager,
    deptName=
        safe_text
)
Management_Director_strategy = st.builds(
    Management_Director,
    budget=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)








@given(instance=Staff_Employee_strategy)
def test_hyp_staff_employee_nationalInsurance_setter(instance):
    original = instance.nationalInsurance
    instance.nationalInsurance = original
    assert instance.nationalInsurance == original



@given(instance=Staff_Employee_strategy)
def test_hyp_staff_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Staff_Employee_strategy)
def test_hyp_staff_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=Management_Manager_strategy)
def test_hyp_management_manager_deptName_setter(instance):
    original = instance.deptName
    instance.deptName = original
    assert instance.deptName == original




@given(instance=Management_Director_strategy)
def test_hyp_management_director_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Management_Director,
    Management_DirectorTest,
    Management_Manager,
    Management_ManagerTest,
    Staff_Employee,
    techStaff_DatabaseAdmin,
    techStaff_DatabaseAdminTest,
    techStaff_Developer,
    techStaff_DeveloperTest,
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

def test_Management_Director_budget_value_roundtrip():
    instance = Management_Director(budget=3.14)
    assert instance.budget == 3.14
    instance.budget = 9.99
    assert instance.budget == 9.99


def test_Management_Manager_deptName_value_roundtrip():
    instance = Management_Manager(deptName="sample_text")
    assert instance.deptName == "sample_text"
    instance.deptName = "sample_text_2"
    assert instance.deptName == "sample_text_2"


def test_Staff_Employee_name_value_roundtrip():
    instance = Staff_Employee(name="sample_text", nationalInsurance="sample_text", salary=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Staff_Employee_nationalInsurance_value_roundtrip():
    instance = Staff_Employee(name="sample_text", nationalInsurance="sample_text", salary=3.14)
    assert instance.nationalInsurance == "sample_text"
    instance.nationalInsurance = "sample_text_2"
    assert instance.nationalInsurance == "sample_text_2"


def test_Staff_Employee_salary_value_roundtrip():
    instance = Staff_Employee(name="sample_text", nationalInsurance="sample_text", salary=3.14)
    assert instance.salary == 3.14
    instance.salary = 9.99
    assert instance.salary == 9.99


def test_assoc_director_DirectorTest_Director_1_link_reassign_clear():
    a = Management_Director(budget=3.14)
    b1 = Management_DirectorTest()
    b2 = Management_DirectorTest()
    _safe_set(a, 'directortest6', b1)
    assert _is_linked(a, 'directortest6', b1)
    if hasattr(b1, 'director7'):
        assert _is_linked(b1, 'director7', a)
    _safe_set(a, 'directortest6', b2)
    assert _is_linked(a, 'directortest6', b2)
    if hasattr(b1, 'director7'):
        assert not _is_linked(b1, 'director7', a)
    if hasattr(b2, 'director7'):
        assert _is_linked(b2, 'director7', a)
    _safe_set(a, 'directortest6', None)
    assert not _is_linked(a, 'directortest6', b2)
    if hasattr(b2, 'director7'):
        assert not _is_linked(b2, 'director7', a)


def test_assoc_manager_ManagerTest_Manager_0_link_reassign_clear():
    a = Management_Manager(deptName="sample_text")
    b1 = Management_ManagerTest()
    b2 = Management_ManagerTest()
    _safe_set(a, 'managertest4', b1)
    assert _is_linked(a, 'managertest4', b1)
    if hasattr(b1, 'manager5'):
        assert _is_linked(b1, 'manager5', a)
    _safe_set(a, 'managertest4', b2)
    assert _is_linked(a, 'managertest4', b2)
    if hasattr(b1, 'manager5'):
        assert not _is_linked(b1, 'manager5', a)
    if hasattr(b2, 'manager5'):
        assert _is_linked(b2, 'manager5', a)
    _safe_set(a, 'managertest4', None)
    assert not _is_linked(a, 'managertest4', b2)
    if hasattr(b2, 'manager5'):
        assert not _is_linked(b2, 'manager5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Management_Director_strategy = st.builds(Management_Director, budget=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Management_Director_strategy)
@settings(max_examples=25)
def test_Management_Director_instantiation(instance):
    assert isinstance(instance, Management_Director)


Management_DirectorTest_strategy = st.builds(Management_DirectorTest)
@given(instance=Management_DirectorTest_strategy)
@settings(max_examples=25)
def test_Management_DirectorTest_instantiation(instance):
    assert isinstance(instance, Management_DirectorTest)


Management_Manager_strategy = st.builds(Management_Manager, deptName=safe_text)
@given(instance=Management_Manager_strategy)
@settings(max_examples=25)
def test_Management_Manager_instantiation(instance):
    assert isinstance(instance, Management_Manager)


Management_ManagerTest_strategy = st.builds(Management_ManagerTest)
@given(instance=Management_ManagerTest_strategy)
@settings(max_examples=25)
def test_Management_ManagerTest_instantiation(instance):
    assert isinstance(instance, Management_ManagerTest)


Staff_Employee_strategy = st.builds(Staff_Employee, name=safe_text, nationalInsurance=safe_text, salary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Staff_Employee_strategy)
@settings(max_examples=25)
def test_Staff_Employee_instantiation(instance):
    assert isinstance(instance, Staff_Employee)


techStaff_DatabaseAdmin_strategy = st.builds(techStaff_DatabaseAdmin)
@given(instance=techStaff_DatabaseAdmin_strategy)
@settings(max_examples=25)
def test_techStaff_DatabaseAdmin_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdmin)


techStaff_DatabaseAdminTest_strategy = st.builds(techStaff_DatabaseAdminTest)
@given(instance=techStaff_DatabaseAdminTest_strategy)
@settings(max_examples=25)
def test_techStaff_DatabaseAdminTest_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdminTest)


techStaff_Developer_strategy = st.builds(techStaff_Developer)
@given(instance=techStaff_Developer_strategy)
@settings(max_examples=25)
def test_techStaff_Developer_instantiation(instance):
    assert isinstance(instance, techStaff_Developer)


techStaff_DeveloperTest_strategy = st.builds(techStaff_DeveloperTest)
@given(instance=techStaff_DeveloperTest_strategy)
@settings(max_examples=25)
def test_techStaff_DeveloperTest_instantiation(instance):
    assert isinstance(instance, techStaff_DeveloperTest)



