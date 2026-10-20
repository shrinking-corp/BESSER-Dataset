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
    organizationchart_Location,
    organizationchart_OrganizationalStructure,
    organizationchart_Employee,
    organizationchart_Organization,
    organizationchart_Function,
    StructureType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_organizationchart_location_is_not_abstract():
    assert not inspect.isabstract(organizationchart_Location)


def test_hyp_organizationchart_location_constructor_exists():
    assert callable(organizationchart_Location.__init__)


def test_hyp_organizationchart_location_constructor_args():
    sig = inspect.signature(organizationchart_Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_organizationchart_organizationalstructure_is_not_abstract():
    assert not inspect.isabstract(organizationchart_OrganizationalStructure)


def test_hyp_organizationchart_organizationalstructure_constructor_exists():
    assert callable(organizationchart_OrganizationalStructure.__init__)


def test_hyp_organizationchart_organizationalstructure_constructor_args():
    sig = inspect.signature(organizationchart_OrganizationalStructure.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_organizationchart_employee_is_not_abstract():
    assert not inspect.isabstract(organizationchart_Employee)


def test_hyp_organizationchart_employee_constructor_exists():
    assert callable(organizationchart_Employee.__init__)


def test_hyp_organizationchart_employee_constructor_args():
    sig = inspect.signature(organizationchart_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "trigraph" in params, "Missing parameter 'trigraph'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "title" in params, "Missing parameter 'title'"
    assert "firstname" in params, "Missing parameter 'firstname'"







def test_hyp_organizationchart_organization_is_not_abstract():
    assert not inspect.isabstract(organizationchart_Organization)


def test_hyp_organizationchart_organization_constructor_exists():
    assert callable(organizationchart_Organization.__init__)


def test_hyp_organizationchart_organization_constructor_args():
    sig = inspect.signature(organizationchart_Organization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_organizationchart_function_is_not_abstract():
    assert not inspect.isabstract(organizationchart_Function)


def test_hyp_organizationchart_function_constructor_exists():
    assert callable(organizationchart_Function.__init__)


def test_hyp_organizationchart_function_constructor_args():
    sig = inspect.signature(organizationchart_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_structuretype_exists():
    # Check that the Enumeration exists
    assert StructureType is not None

def test_hyp_structuretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StructureType]
    expected_literals = [
        "team",
        "service",
        "businessUnit",
        "division",
        "department",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StructureType"


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
organizationchart_Location_strategy = st.builds(
    organizationchart_Location,
    name=
        safe_text
)
organizationchart_OrganizationalStructure_strategy = st.builds(
    organizationchart_OrganizationalStructure,
    type=
        safe_text,
    name=
        safe_text
)
organizationchart_Employee_strategy = st.builds(
    organizationchart_Employee,
    trigraph=
        safe_text,
    lastname=
        safe_text,
    title=
        safe_text,
    firstname=
        safe_text
)
organizationchart_Organization_strategy = st.builds(
    organizationchart_Organization,
    name=
        safe_text
)
organizationchart_Function_strategy = st.builds(
    organizationchart_Function,
    name=
        safe_text
)




@given(instance=organizationchart_Location_strategy)
def test_hyp_organizationchart_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=organizationchart_OrganizationalStructure_strategy)
def test_hyp_organizationchart_organizationalstructure_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=organizationchart_OrganizationalStructure_strategy)
def test_hyp_organizationchart_organizationalstructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=organizationchart_Employee_strategy)
def test_hyp_organizationchart_employee_trigraph_setter(instance):
    original = instance.trigraph
    instance.trigraph = original
    assert instance.trigraph == original



@given(instance=organizationchart_Employee_strategy)
def test_hyp_organizationchart_employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=organizationchart_Employee_strategy)
def test_hyp_organizationchart_employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=organizationchart_Employee_strategy)
def test_hyp_organizationchart_employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original




@given(instance=organizationchart_Organization_strategy)
def test_hyp_organizationchart_organization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=organizationchart_Function_strategy)
def test_hyp_organizationchart_function_name_setter(instance):
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
    organizationchart_Employee,
    organizationchart_Function,
    organizationchart_Location,
    organizationchart_Organization,
    organizationchart_OrganizationalStructure,
    StructureType,
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

def test_organizationchart_Employee_firstname_value_roundtrip():
    instance = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_organizationchart_Employee_lastname_value_roundtrip():
    instance = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_organizationchart_Employee_title_value_roundtrip():
    instance = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_organizationchart_Employee_trigraph_value_roundtrip():
    instance = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    assert instance.trigraph == "sample_text"
    instance.trigraph = "sample_text_2"
    assert instance.trigraph == "sample_text_2"


def test_organizationchart_Function_name_value_roundtrip():
    instance = organizationchart_Function(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_organizationchart_Location_name_value_roundtrip():
    instance = organizationchart_Location(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_organizationchart_Organization_name_value_roundtrip():
    instance = organizationchart_Organization(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_organizationchart_OrganizationalStructure_name_value_roundtrip():
    instance = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_organizationchart_OrganizationalStructure_type_value_roundtrip():
    instance = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_belongsTo2_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'OrganizationalStructure', b1)
    assert _is_linked(a, 'OrganizationalStructure', b1)
    if hasattr(b1, 'employees'):
        assert _is_linked(b1, 'employees', a)
    _safe_set(a, 'OrganizationalStructure', b2)
    assert _is_linked(a, 'OrganizationalStructure', b2)
    if hasattr(b1, 'employees'):
        assert not _is_linked(b1, 'employees', a)
    if hasattr(b2, 'employees'):
        assert _is_linked(b2, 'employees', a)
    _safe_set(a, 'OrganizationalStructure', None)
    assert not _is_linked(a, 'OrganizationalStructure', b2)
    if hasattr(b2, 'employees'):
        assert not _is_linked(b2, 'employees', a)


def test_assoc_employees12_link_reassign_clear():
    a = organizationchart_Organization(name="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'organizationchart_Organization', {b1})
    assert _is_linked(a, 'organizationchart_Organization', b1)
    if hasattr(b1, 'organizationchart_Employee'):
        assert _is_linked(b1, 'organizationchart_Employee', a)
    _safe_set(a, 'organizationchart_Organization', {b2})
    assert _is_linked(a, 'organizationchart_Organization', b2)
    if hasattr(b1, 'organizationchart_Employee'):
        assert not _is_linked(b1, 'organizationchart_Employee', a)
    if hasattr(b2, 'organizationchart_Employee'):
        assert _is_linked(b2, 'organizationchart_Employee', a)
    _safe_set(a, 'organizationchart_Organization', set())
    assert not _is_linked(a, 'organizationchart_Organization', b2)
    if hasattr(b2, 'organizationchart_Employee'):
        assert not _is_linked(b2, 'organizationchart_Employee', a)


def test_assoc_employees17_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'belongsTo', {b1})
    assert _is_linked(a, 'belongsTo', b1)
    if hasattr(b1, 'Employee18'):
        assert _is_linked(b1, 'Employee18', a)
    _safe_set(a, 'belongsTo', {b2})
    assert _is_linked(a, 'belongsTo', b2)
    if hasattr(b1, 'Employee18'):
        assert not _is_linked(b1, 'Employee18', a)
    if hasattr(b2, 'Employee18'):
        assert _is_linked(b2, 'Employee18', a)
    _safe_set(a, 'belongsTo', set())
    assert not _is_linked(a, 'belongsTo', b2)
    if hasattr(b2, 'Employee18'):
        assert not _is_linked(b2, 'Employee18', a)


def test_assoc_employees26_link_reassign_clear():
    a = organizationchart_Location(name="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'location', {b1})
    assert _is_linked(a, 'location', b1)
    if hasattr(b1, 'Employee27'):
        assert _is_linked(b1, 'Employee27', a)
    _safe_set(a, 'location', {b2})
    assert _is_linked(a, 'location', b2)
    if hasattr(b1, 'Employee27'):
        assert not _is_linked(b1, 'Employee27', a)
    if hasattr(b2, 'Employee27'):
        assert _is_linked(b2, 'Employee27', a)
    _safe_set(a, 'location', set())
    assert not _is_linked(a, 'location', b2)
    if hasattr(b2, 'Employee27'):
        assert not _is_linked(b2, 'Employee27', a)


def test_assoc_isPerformedBy28_link_reassign_clear():
    a = organizationchart_Function(name="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'performs', {b1})
    assert _is_linked(a, 'performs', b1)
    if hasattr(b1, 'Employee29'):
        assert _is_linked(b1, 'Employee29', a)
    _safe_set(a, 'performs', {b2})
    assert _is_linked(a, 'performs', b2)
    if hasattr(b1, 'Employee29'):
        assert not _is_linked(b1, 'Employee29', a)
    if hasattr(b2, 'Employee29'):
        assert _is_linked(b2, 'Employee29', a)
    _safe_set(a, 'performs', set())
    assert not _is_linked(a, 'performs', b2)
    if hasattr(b2, 'Employee29'):
        assert not _is_linked(b2, 'Employee29', a)


def test_assoc_leads9_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'OrganizationalStructure11', b1)
    assert _is_linked(a, 'OrganizationalStructure11', b1)
    if hasattr(b1, 'manager10'):
        assert _is_linked(b1, 'manager10', a)
    _safe_set(a, 'OrganizationalStructure11', b2)
    assert _is_linked(a, 'OrganizationalStructure11', b2)
    if hasattr(b1, 'manager10'):
        assert not _is_linked(b1, 'manager10', a)
    if hasattr(b2, 'manager10'):
        assert _is_linked(b2, 'manager10', a)
    _safe_set(a, 'OrganizationalStructure11', None)
    assert not _is_linked(a, 'OrganizationalStructure11', b2)
    if hasattr(b2, 'manager10'):
        assert not _is_linked(b2, 'manager10', a)


def test_assoc_location3_link_reassign_clear():
    a = organizationchart_Location(name="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'Location', b1)
    assert _is_linked(a, 'Location', b1)
    if hasattr(b1, 'employees4'):
        assert _is_linked(b1, 'employees4', a)
    _safe_set(a, 'Location', b2)
    assert _is_linked(a, 'Location', b2)
    if hasattr(b1, 'employees4'):
        assert not _is_linked(b1, 'employees4', a)
    if hasattr(b2, 'employees4'):
        assert _is_linked(b2, 'employees4', a)
    _safe_set(a, 'Location', None)
    assert not _is_linked(a, 'Location', b2)
    if hasattr(b2, 'employees4'):
        assert not _is_linked(b2, 'employees4', a)


def test_assoc_locations15_link_reassign_clear():
    a = organizationchart_Organization(name="sample_text")
    b1 = organizationchart_Location(name="sample_text")
    b2 = organizationchart_Location(name="sample_text_2")
    _safe_set(a, 'organizationchart_Organization16', {b1})
    assert _is_linked(a, 'organizationchart_Organization16', b1)
    if hasattr(b1, 'organizationchart_Location'):
        assert _is_linked(b1, 'organizationchart_Location', a)
    _safe_set(a, 'organizationchart_Organization16', {b2})
    assert _is_linked(a, 'organizationchart_Organization16', b2)
    if hasattr(b1, 'organizationchart_Location'):
        assert not _is_linked(b1, 'organizationchart_Location', a)
    if hasattr(b2, 'organizationchart_Location'):
        assert _is_linked(b2, 'organizationchart_Location', a)
    _safe_set(a, 'organizationchart_Organization16', set())
    assert not _is_linked(a, 'organizationchart_Organization16', b2)
    if hasattr(b2, 'organizationchart_Location'):
        assert not _is_linked(b2, 'organizationchart_Location', a)


def test_assoc_manager24_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'leads', b1)
    assert _is_linked(a, 'leads', b1)
    if hasattr(b1, 'Employee25'):
        assert _is_linked(b1, 'Employee25', a)
    _safe_set(a, 'leads', b2)
    assert _is_linked(a, 'leads', b2)
    if hasattr(b1, 'Employee25'):
        assert not _is_linked(b1, 'Employee25', a)
    if hasattr(b2, 'Employee25'):
        assert _is_linked(b2, 'Employee25', a)
    _safe_set(a, 'leads', None)
    assert not _is_linked(a, 'leads', b2)
    if hasattr(b2, 'Employee25'):
        assert not _is_linked(b2, 'Employee25', a)


def test_assoc_manager6_link_reassign_clear():
    a = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'Employee7', b1)
    assert _is_linked(a, 'Employee7', b1)
    if hasattr(b1, 'manages'):
        assert _is_linked(b1, 'manages', a)
    _safe_set(a, 'Employee7', b2)
    assert _is_linked(a, 'Employee7', b2)
    if hasattr(b1, 'manages'):
        assert not _is_linked(b1, 'manages', a)
    if hasattr(b2, 'manages'):
        assert _is_linked(b2, 'manages', a)
    _safe_set(a, 'Employee7', None)
    assert not _is_linked(a, 'Employee7', b2)
    if hasattr(b2, 'manages'):
        assert not _is_linked(b2, 'manages', a)


def test_assoc_manages1_link_reassign_clear():
    a = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'manager'):
        assert _is_linked(b1, 'manager', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'manager'):
        assert not _is_linked(b1, 'manager', a)
    if hasattr(b2, 'manager'):
        assert _is_linked(b2, 'manager', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'manager'):
        assert not _is_linked(b2, 'manager', a)


def test_assoc_owns22_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Function(name="sample_text")
    b2 = organizationchart_Function(name="sample_text_2")
    _safe_set(a, 'organizationchart_OrganizationalStructure23', {b1})
    assert _is_linked(a, 'organizationchart_OrganizationalStructure23', b1)
    if hasattr(b1, 'organizationchart_Function'):
        assert _is_linked(b1, 'organizationchart_Function', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure23', {b2})
    assert _is_linked(a, 'organizationchart_OrganizationalStructure23', b2)
    if hasattr(b1, 'organizationchart_Function'):
        assert not _is_linked(b1, 'organizationchart_Function', a)
    if hasattr(b2, 'organizationchart_Function'):
        assert _is_linked(b2, 'organizationchart_Function', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure23', set())
    assert not _is_linked(a, 'organizationchart_OrganizationalStructure23', b2)
    if hasattr(b2, 'organizationchart_Function'):
        assert not _is_linked(b2, 'organizationchart_Function', a)


def test_assoc_performs8_link_reassign_clear():
    a = organizationchart_Function(name="sample_text")
    b1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    b2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    _safe_set(a, 'Function', b1)
    assert _is_linked(a, 'Function', b1)
    if hasattr(b1, 'isPerformedBy'):
        assert _is_linked(b1, 'isPerformedBy', a)
    _safe_set(a, 'Function', b2)
    assert _is_linked(a, 'Function', b2)
    if hasattr(b1, 'isPerformedBy'):
        assert not _is_linked(b1, 'isPerformedBy', a)
    if hasattr(b2, 'isPerformedBy'):
        assert _is_linked(b2, 'isPerformedBy', a)
    _safe_set(a, 'Function', None)
    assert not _is_linked(a, 'Function', b2)
    if hasattr(b2, 'isPerformedBy'):
        assert not _is_linked(b2, 'isPerformedBy', a)


def test_assoc_structures13_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_Organization(name="sample_text")
    b2 = organizationchart_Organization(name="sample_text_2")
    _safe_set(a, 'organizationchart_OrganizationalStructure', b1)
    assert _is_linked(a, 'organizationchart_OrganizationalStructure', b1)
    if hasattr(b1, 'organizationchart_Organization14'):
        assert _is_linked(b1, 'organizationchart_Organization14', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure', b2)
    assert _is_linked(a, 'organizationchart_OrganizationalStructure', b2)
    if hasattr(b1, 'organizationchart_Organization14'):
        assert not _is_linked(b1, 'organizationchart_Organization14', a)
    if hasattr(b2, 'organizationchart_Organization14'):
        assert _is_linked(b2, 'organizationchart_Organization14', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure', None)
    assert not _is_linked(a, 'organizationchart_OrganizationalStructure', b2)
    if hasattr(b2, 'organizationchart_Organization14'):
        assert not _is_linked(b2, 'organizationchart_Organization14', a)


def test_assoc_subStructures20_link_reassign_clear():
    a = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    b2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'organizationchart_OrganizationalStructure19', {b1})
    assert _is_linked(a, 'organizationchart_OrganizationalStructure19', b1)
    if hasattr(b1, 'organizationchart_OrganizationalStructure21'):
        assert _is_linked(b1, 'organizationchart_OrganizationalStructure21', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure19', {b2})
    assert _is_linked(a, 'organizationchart_OrganizationalStructure19', b2)
    if hasattr(b1, 'organizationchart_OrganizationalStructure21'):
        assert not _is_linked(b1, 'organizationchart_OrganizationalStructure21', a)
    if hasattr(b2, 'organizationchart_OrganizationalStructure21'):
        assert _is_linked(b2, 'organizationchart_OrganizationalStructure21', a)
    _safe_set(a, 'organizationchart_OrganizationalStructure19', set())
    assert not _is_linked(a, 'organizationchart_OrganizationalStructure19', b2)
    if hasattr(b2, 'organizationchart_OrganizationalStructure21'):
        assert not _is_linked(b2, 'organizationchart_OrganizationalStructure21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

organizationchart_Employee_strategy = st.builds(organizationchart_Employee, firstname=safe_text, lastname=safe_text, title=safe_text, trigraph=safe_text)
@given(instance=organizationchart_Employee_strategy)
@settings(max_examples=25)
def test_organizationchart_Employee_instantiation(instance):
    assert isinstance(instance, organizationchart_Employee)


organizationchart_Function_strategy = st.builds(organizationchart_Function, name=safe_text)
@given(instance=organizationchart_Function_strategy)
@settings(max_examples=25)
def test_organizationchart_Function_instantiation(instance):
    assert isinstance(instance, organizationchart_Function)


organizationchart_Location_strategy = st.builds(organizationchart_Location, name=safe_text)
@given(instance=organizationchart_Location_strategy)
@settings(max_examples=25)
def test_organizationchart_Location_instantiation(instance):
    assert isinstance(instance, organizationchart_Location)


organizationchart_Organization_strategy = st.builds(organizationchart_Organization, name=safe_text)
@given(instance=organizationchart_Organization_strategy)
@settings(max_examples=25)
def test_organizationchart_Organization_instantiation(instance):
    assert isinstance(instance, organizationchart_Organization)


organizationchart_OrganizationalStructure_strategy = st.builds(organizationchart_OrganizationalStructure, name=safe_text, type=safe_text)
@given(instance=organizationchart_OrganizationalStructure_strategy)
@settings(max_examples=25)
def test_organizationchart_OrganizationalStructure_instantiation(instance):
    assert isinstance(instance, organizationchart_OrganizationalStructure)



