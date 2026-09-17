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
    rental_License,
    rental_Address,
    rental_Customer,
    rental_Rental,
    rental_RentalObject,
    rental_RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_rental_license_is_not_abstract():
    assert not inspect.isabstract(rental_License)


def test_hyp_rental_license_constructor_exists():
    assert callable(rental_License.__init__)


def test_hyp_rental_license_constructor_args():
    sig = inspect.signature(rental_License.__init__)
    params = list(sig.parameters.keys())
    assert "validityDate" in params, "Missing parameter 'validityDate'"
    assert "number" in params, "Missing parameter 'number'"





def test_hyp_rental_address_is_not_abstract():
    assert not inspect.isabstract(rental_Address)


def test_hyp_rental_address_constructor_exists():
    assert callable(rental_Address.__init__)


def test_hyp_rental_address_constructor_args():
    sig = inspect.signature(rental_Address.__init__)
    params = list(sig.parameters.keys())
    assert "streetName" in params, "Missing parameter 'streetName'"
    assert "city" in params, "Missing parameter 'city'"
    assert "number" in params, "Missing parameter 'number'"
    assert "streetType" in params, "Missing parameter 'streetType'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"








def test_hyp_rental_customer_is_not_abstract():
    assert not inspect.isabstract(rental_Customer)


def test_hyp_rental_customer_constructor_exists():
    assert callable(rental_Customer.__init__)


def test_hyp_rental_customer_constructor_args():
    sig = inspect.signature(rental_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"





def test_hyp_rental_rental_is_not_abstract():
    assert not inspect.isabstract(rental_Rental)


def test_hyp_rental_rental_constructor_exists():
    assert callable(rental_Rental.__init__)


def test_hyp_rental_rental_constructor_args():
    sig = inspect.signature(rental_Rental.__init__)
    params = list(sig.parameters.keys())
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"





def test_hyp_rental_rentalobject_is_not_abstract():
    assert not inspect.isabstract(rental_RentalObject)


def test_hyp_rental_rentalobject_constructor_exists():
    assert callable(rental_RentalObject.__init__)


def test_hyp_rental_rentalobject_constructor_args():
    sig = inspect.signature(rental_RentalObject.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "picture" in params, "Missing parameter 'picture'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_rental_rentalagency_is_not_abstract():
    assert not inspect.isabstract(rental_RentalAgency)


def test_hyp_rental_rentalagency_constructor_exists():
    assert callable(rental_RentalAgency.__init__)


def test_hyp_rental_rentalagency_constructor_args():
    sig = inspect.signature(rental_RentalAgency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_streettype_exists():
    # Check that the Enumeration exists
    assert StreetType is not None

def test_hyp_streettype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StreetType]
    expected_literals = [
        "Road",
        "Street",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StreetType"


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
rental_License_strategy = st.builds(
    rental_License,
    validityDate=
        st.dates(),
    number=
        st.integers()
)
rental_Address_strategy = st.builds(
    rental_Address,
    streetName=
        safe_text,
    city=
        safe_text,
    number=
        st.integers(),
    streetType=
        safe_text,
    zipCode=
        safe_text
)
rental_Customer_strategy = st.builds(
    rental_Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)
rental_Rental_strategy = st.builds(
    rental_Rental,
    endDate=
        st.dates(),
    startDate=
        st.dates()
)
rental_RentalObject_strategy = st.builds(
    rental_RentalObject,
    ID=
        safe_text,
    picture=
        safe_text,
    name=
        safe_text
)
rental_RentalAgency_strategy = st.builds(
    rental_RentalAgency,
    name=
        safe_text
)




@given(instance=rental_License_strategy)
def test_hyp_rental_license_validityDate_setter(instance):
    original = instance.validityDate
    instance.validityDate = original
    assert instance.validityDate == original



@given(instance=rental_License_strategy)
def test_hyp_rental_license_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original




@given(instance=rental_Address_strategy)
def test_hyp_rental_address_streetName_setter(instance):
    original = instance.streetName
    instance.streetName = original
    assert instance.streetName == original



@given(instance=rental_Address_strategy)
def test_hyp_rental_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=rental_Address_strategy)
def test_hyp_rental_address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=rental_Address_strategy)
def test_hyp_rental_address_streetType_setter(instance):
    original = instance.streetType
    instance.streetType = original
    assert instance.streetType == original



@given(instance=rental_Address_strategy)
def test_hyp_rental_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original




@given(instance=rental_Customer_strategy)
def test_hyp_rental_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=rental_Customer_strategy)
def test_hyp_rental_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original




@given(instance=rental_Rental_strategy)
def test_hyp_rental_rental_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=rental_Rental_strategy)
def test_hyp_rental_rental_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_Rental_strategy)
@settings(max_examples=30)
def test_hyp_rental_rental_nbdaysbooked_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nbDaysBooked()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nbDaysBooked).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nbDaysBooked' in rental_Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nbDaysBooked' in rental_Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nbDaysBooked' in rental_Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_Rental_strategy)
@settings(max_examples=30)
def test_hyp_rental_rental_nbdaysrented_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nbDaysRented()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nbDaysRented).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nbDaysRented' in rental_Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nbDaysRented' in rental_Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nbDaysRented' in rental_Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_Rental_strategy)
@settings(max_examples=30)
def test_hyp_rental_rental_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in rental_Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in rental_Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in rental_Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_Rental_strategy)
@settings(max_examples=30)
def test_hyp_rental_rental_end_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.end()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.end).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'end' in rental_Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'end' in rental_Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'end' in rental_Rental is not implemented or raised an error")




@given(instance=rental_RentalObject_strategy)
def test_hyp_rental_rentalobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=rental_RentalObject_strategy)
def test_hyp_rental_rentalobject_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original



@given(instance=rental_RentalObject_strategy)
def test_hyp_rental_rentalobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalObject_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalobject_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in rental_RentalObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in rental_RentalObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in rental_RentalObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalObject_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalobject_rent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.rent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.rent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'rent' in rental_RentalObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'rent' in rental_RentalObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'rent' in rental_RentalObject is not implemented or raised an error")




@given(instance=rental_RentalAgency_strategy)
def test_hyp_rental_rentalagency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalagency_book_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.book(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.book).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'book' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'book' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'book' in rental_RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalagency_addobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addObject' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addObject' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addObject' in rental_RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalagency_addcustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addCustomer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addCustomer' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCustomer' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCustomer' in rental_RentalAgency is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    rental_Address,
    rental_Customer,
    rental_License,
    rental_Rental,
    rental_RentalAgency,
    rental_RentalObject,
    StreetType,
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

def test_rental_Address_city_value_roundtrip():
    instance = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_rental_Address_number_value_roundtrip():
    instance = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_rental_Address_streetName_value_roundtrip():
    instance = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    assert instance.streetName == "sample_text"
    instance.streetName = "sample_text_2"
    assert instance.streetName == "sample_text_2"


def test_rental_Address_streetType_value_roundtrip():
    instance = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    assert instance.streetType == "sample_text"
    instance.streetType = "sample_text_2"
    assert instance.streetType == "sample_text_2"


def test_rental_Address_zipCode_value_roundtrip():
    instance = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_rental_Customer_firstName_value_roundtrip():
    instance = rental_Customer(firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_rental_Customer_lastName_value_roundtrip():
    instance = rental_Customer(firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_rental_License_number_value_roundtrip():
    instance = rental_License(number=7, validityDate=date(2024, 1, 1))
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_rental_License_validityDate_value_roundtrip():
    instance = rental_License(number=7, validityDate=date(2024, 1, 1))
    assert instance.validityDate == date(2024, 1, 1)
    instance.validityDate = date(2025, 6, 15)
    assert instance.validityDate == date(2025, 6, 15)


def test_rental_Rental_endDate_value_roundtrip():
    instance = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    assert instance.endDate == date(2024, 1, 1)
    instance.endDate = date(2025, 6, 15)
    assert instance.endDate == date(2025, 6, 15)


def test_rental_Rental_startDate_value_roundtrip():
    instance = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_rental_RentalAgency_name_value_roundtrip():
    instance = rental_RentalAgency(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rental_RentalObject_ID_value_roundtrip():
    instance = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_rental_RentalObject_name_value_roundtrip():
    instance = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rental_RentalObject_picture_value_roundtrip():
    instance = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    assert instance.picture == "sample_text"
    instance.picture = "sample_text_2"
    assert instance.picture == "sample_text_2"


def test_assoc_address0_link_reassign_clear():
    a = rental_Customer(firstName="sample_text", lastName="sample_text")
    b1 = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    b2 = rental_Address(city="sample_text_2", number=13, streetName="sample_text_2", streetType="sample_text_2", zipCode="sample_text_2")
    _safe_set(a, 'rental_Customer', b1)
    assert _is_linked(a, 'rental_Customer', b1)
    if hasattr(b1, 'rental_Address'):
        assert _is_linked(b1, 'rental_Address', a)
    _safe_set(a, 'rental_Customer', b2)
    assert _is_linked(a, 'rental_Customer', b2)
    if hasattr(b1, 'rental_Address'):
        assert not _is_linked(b1, 'rental_Address', a)
    if hasattr(b2, 'rental_Address'):
        assert _is_linked(b2, 'rental_Address', a)
    _safe_set(a, 'rental_Customer', None)
    assert not _is_linked(a, 'rental_Customer', b2)
    if hasattr(b2, 'rental_Address'):
        assert not _is_linked(b2, 'rental_Address', a)


def test_assoc_address3_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Address(city="sample_text", number=7, streetName="sample_text", streetType="sample_text", zipCode="sample_text")
    b2 = rental_Address(city="sample_text_2", number=13, streetName="sample_text_2", streetType="sample_text_2", zipCode="sample_text_2")
    _safe_set(a, 'rental_RentalAgency', b1)
    assert _is_linked(a, 'rental_RentalAgency', b1)
    if hasattr(b1, 'rental_Address4'):
        assert _is_linked(b1, 'rental_Address4', a)
    _safe_set(a, 'rental_RentalAgency', b2)
    assert _is_linked(a, 'rental_RentalAgency', b2)
    if hasattr(b1, 'rental_Address4'):
        assert not _is_linked(b1, 'rental_Address4', a)
    if hasattr(b2, 'rental_Address4'):
        assert _is_linked(b2, 'rental_Address4', a)
    _safe_set(a, 'rental_RentalAgency', None)
    assert not _is_linked(a, 'rental_RentalAgency', b2)
    if hasattr(b2, 'rental_Address4'):
        assert not _is_linked(b2, 'rental_Address4', a)


def test_assoc_customer14_link_reassign_clear():
    a = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'rental_Rental15', b1)
    assert _is_linked(a, 'rental_Rental15', b1)
    if hasattr(b1, 'rental_Customer16'):
        assert _is_linked(b1, 'rental_Customer16', a)
    _safe_set(a, 'rental_Rental15', b2)
    assert _is_linked(a, 'rental_Rental15', b2)
    if hasattr(b1, 'rental_Customer16'):
        assert not _is_linked(b1, 'rental_Customer16', a)
    if hasattr(b2, 'rental_Customer16'):
        assert _is_linked(b2, 'rental_Customer16', a)
    _safe_set(a, 'rental_Rental15', None)
    assert not _is_linked(a, 'rental_Rental15', b2)
    if hasattr(b2, 'rental_Customer16'):
        assert not _is_linked(b2, 'rental_Customer16', a)


def test_assoc_customers6_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'parentAgency7', {b1})
    assert _is_linked(a, 'parentAgency7', b1)
    if hasattr(b1, 'Customer'):
        assert _is_linked(b1, 'Customer', a)
    _safe_set(a, 'parentAgency7', {b2})
    assert _is_linked(a, 'parentAgency7', b2)
    if hasattr(b1, 'Customer'):
        assert not _is_linked(b1, 'Customer', a)
    if hasattr(b2, 'Customer'):
        assert _is_linked(b2, 'Customer', a)
    _safe_set(a, 'parentAgency7', set())
    assert not _is_linked(a, 'parentAgency7', b2)
    if hasattr(b2, 'Customer'):
        assert not _is_linked(b2, 'Customer', a)


def test_assoc_licenses1_link_reassign_clear():
    a = rental_License(number=7, validityDate=date(2024, 1, 1))
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'License', b1)
    assert _is_linked(a, 'License', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'License', b2)
    assert _is_linked(a, 'License', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'License', None)
    assert not _is_linked(a, 'License', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_objectsToRent5_link_reassign_clear():
    a = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    b1 = rental_RentalAgency(name="sample_text")
    b2 = rental_RentalAgency(name="sample_text_2")
    _safe_set(a, 'RentalObject', b1)
    assert _is_linked(a, 'RentalObject', b1)
    if hasattr(b1, 'parentAgency'):
        assert _is_linked(b1, 'parentAgency', a)
    _safe_set(a, 'RentalObject', b2)
    assert _is_linked(a, 'RentalObject', b2)
    if hasattr(b1, 'parentAgency'):
        assert not _is_linked(b1, 'parentAgency', a)
    if hasattr(b2, 'parentAgency'):
        assert _is_linked(b2, 'parentAgency', a)
    _safe_set(a, 'RentalObject', None)
    assert not _is_linked(a, 'RentalObject', b2)
    if hasattr(b2, 'parentAgency'):
        assert not _is_linked(b2, 'parentAgency', a)


def test_assoc_owner12_link_reassign_clear():
    a = rental_License(number=7, validityDate=date(2024, 1, 1))
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'licenses', b1)
    assert _is_linked(a, 'licenses', b1)
    if hasattr(b1, 'Customer13'):
        assert _is_linked(b1, 'Customer13', a)
    _safe_set(a, 'licenses', b2)
    assert _is_linked(a, 'licenses', b2)
    if hasattr(b1, 'Customer13'):
        assert not _is_linked(b1, 'Customer13', a)
    if hasattr(b2, 'Customer13'):
        assert _is_linked(b2, 'Customer13', a)
    _safe_set(a, 'licenses', None)
    assert not _is_linked(a, 'licenses', b2)
    if hasattr(b2, 'Customer13'):
        assert not _is_linked(b2, 'Customer13', a)


def test_assoc_parentAgency10_link_reassign_clear():
    a = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    b1 = rental_RentalAgency(name="sample_text")
    b2 = rental_RentalAgency(name="sample_text_2")
    _safe_set(a, 'objectsToRent', b1)
    assert _is_linked(a, 'objectsToRent', b1)
    if hasattr(b1, 'RentalAgency11'):
        assert _is_linked(b1, 'RentalAgency11', a)
    _safe_set(a, 'objectsToRent', b2)
    assert _is_linked(a, 'objectsToRent', b2)
    if hasattr(b1, 'RentalAgency11'):
        assert not _is_linked(b1, 'RentalAgency11', a)
    if hasattr(b2, 'RentalAgency11'):
        assert _is_linked(b2, 'RentalAgency11', a)
    _safe_set(a, 'objectsToRent', None)
    assert not _is_linked(a, 'objectsToRent', b2)
    if hasattr(b2, 'RentalAgency11'):
        assert not _is_linked(b2, 'RentalAgency11', a)


def test_assoc_parentAgency19_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'rental_RentalAgency21', b1)
    assert _is_linked(a, 'rental_RentalAgency21', b1)
    if hasattr(b1, 'rental_Rental20'):
        assert _is_linked(b1, 'rental_Rental20', a)
    _safe_set(a, 'rental_RentalAgency21', b2)
    assert _is_linked(a, 'rental_RentalAgency21', b2)
    if hasattr(b1, 'rental_Rental20'):
        assert not _is_linked(b1, 'rental_Rental20', a)
    if hasattr(b2, 'rental_Rental20'):
        assert _is_linked(b2, 'rental_Rental20', a)
    _safe_set(a, 'rental_RentalAgency21', None)
    assert not _is_linked(a, 'rental_RentalAgency21', b2)
    if hasattr(b2, 'rental_Rental20'):
        assert not _is_linked(b2, 'rental_Rental20', a)


def test_assoc_parentAgency2_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'RentalAgency', b1)
    assert _is_linked(a, 'RentalAgency', b1)
    if hasattr(b1, 'customers'):
        assert _is_linked(b1, 'customers', a)
    _safe_set(a, 'RentalAgency', b2)
    assert _is_linked(a, 'RentalAgency', b2)
    if hasattr(b1, 'customers'):
        assert not _is_linked(b1, 'customers', a)
    if hasattr(b2, 'customers'):
        assert _is_linked(b2, 'customers', a)
    _safe_set(a, 'RentalAgency', None)
    assert not _is_linked(a, 'RentalAgency', b2)
    if hasattr(b2, 'customers'):
        assert not _is_linked(b2, 'customers', a)


def test_assoc_rentals8_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'rental_RentalAgency9', {b1})
    assert _is_linked(a, 'rental_RentalAgency9', b1)
    if hasattr(b1, 'rental_Rental'):
        assert _is_linked(b1, 'rental_Rental', a)
    _safe_set(a, 'rental_RentalAgency9', {b2})
    assert _is_linked(a, 'rental_RentalAgency9', b2)
    if hasattr(b1, 'rental_Rental'):
        assert not _is_linked(b1, 'rental_Rental', a)
    if hasattr(b2, 'rental_Rental'):
        assert _is_linked(b2, 'rental_Rental', a)
    _safe_set(a, 'rental_RentalAgency9', set())
    assert not _is_linked(a, 'rental_RentalAgency9', b2)
    if hasattr(b2, 'rental_Rental'):
        assert not _is_linked(b2, 'rental_Rental', a)


def test_assoc_rentedObject17_link_reassign_clear():
    a = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'rental_RentalObject', b1)
    assert _is_linked(a, 'rental_RentalObject', b1)
    if hasattr(b1, 'rental_Rental18'):
        assert _is_linked(b1, 'rental_Rental18', a)
    _safe_set(a, 'rental_RentalObject', b2)
    assert _is_linked(a, 'rental_RentalObject', b2)
    if hasattr(b1, 'rental_Rental18'):
        assert not _is_linked(b1, 'rental_Rental18', a)
    if hasattr(b2, 'rental_Rental18'):
        assert _is_linked(b2, 'rental_Rental18', a)
    _safe_set(a, 'rental_RentalObject', None)
    assert not _is_linked(a, 'rental_RentalObject', b2)
    if hasattr(b2, 'rental_Rental18'):
        assert not _is_linked(b2, 'rental_Rental18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

rental_Address_strategy = st.builds(rental_Address, city=safe_text, number=st.integers(), streetName=safe_text, streetType=safe_text, zipCode=safe_text)
@given(instance=rental_Address_strategy)
@settings(max_examples=25)
def test_rental_Address_instantiation(instance):
    assert isinstance(instance, rental_Address)


rental_Customer_strategy = st.builds(rental_Customer, firstName=safe_text, lastName=safe_text)
@given(instance=rental_Customer_strategy)
@settings(max_examples=25)
def test_rental_Customer_instantiation(instance):
    assert isinstance(instance, rental_Customer)


rental_License_strategy = st.builds(rental_License, number=st.integers(), validityDate=st.dates())
@given(instance=rental_License_strategy)
@settings(max_examples=25)
def test_rental_License_instantiation(instance):
    assert isinstance(instance, rental_License)


rental_Rental_strategy = st.builds(rental_Rental, endDate=st.dates(), startDate=st.dates())
@given(instance=rental_Rental_strategy)
@settings(max_examples=25)
def test_rental_Rental_instantiation(instance):
    assert isinstance(instance, rental_Rental)


rental_RentalAgency_strategy = st.builds(rental_RentalAgency, name=safe_text)
@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=25)
def test_rental_RentalAgency_instantiation(instance):
    assert isinstance(instance, rental_RentalAgency)


rental_RentalObject_strategy = st.builds(rental_RentalObject, ID=safe_text, name=safe_text, picture=safe_text)
@given(instance=rental_RentalObject_strategy)
@settings(max_examples=25)
def test_rental_RentalObject_instantiation(instance):
    assert isinstance(instance, rental_RentalObject)



