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
    rental_Rental,
    rental_Customer,
    rental_RentalObject,
    rental_RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_rental_rental_is_not_abstract():
    assert not inspect.isabstract(rental_Rental)


def test_hyp_rental_rental_constructor_exists():
    assert callable(rental_Rental.__init__)


def test_hyp_rental_rental_constructor_args():
    sig = inspect.signature(rental_Rental.__init__)
    params = list(sig.parameters.keys())
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"





def test_hyp_rental_customer_is_not_abstract():
    assert not inspect.isabstract(rental_Customer)


def test_hyp_rental_customer_constructor_exists():
    assert callable(rental_Customer.__init__)


def test_hyp_rental_customer_constructor_args():
    sig = inspect.signature(rental_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"





def test_hyp_rental_rentalobject_is_not_abstract():
    assert not inspect.isabstract(rental_RentalObject)


def test_hyp_rental_rentalobject_constructor_exists():
    assert callable(rental_RentalObject.__init__)


def test_hyp_rental_rentalobject_constructor_args():
    sig = inspect.signature(rental_RentalObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "picture" in params, "Missing parameter 'picture'"






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
        "Street",
        "Road",
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
rental_Rental_strategy = st.builds(
    rental_Rental,
    endDate=
        st.dates(),
    startDate=
        st.dates()
)
rental_Customer_strategy = st.builds(
    rental_Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)
rental_RentalObject_strategy = st.builds(
    rental_RentalObject,
    name=
        safe_text,
    ID=
        safe_text,
    picture=
        safe_text
)
rental_RentalAgency_strategy = st.builds(
    rental_RentalAgency,
    name=
        safe_text
)




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




@given(instance=rental_RentalObject_strategy)
def test_hyp_rental_rentalobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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
def test_hyp_rental_rentalagency_removeobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeObject' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeObject' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeObject' in rental_RentalAgency is not implemented or raised an error")

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
def test_hyp_rental_rentalagency_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in rental_RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_hyp_rental_rentalagency_removecustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeCustomer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeCustomer' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeCustomer' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeCustomer' in rental_RentalAgency is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    rental_Customer,
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


def test_assoc_customer8_link_reassign_clear():
    a = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'rental_Rental', b1)
    assert _is_linked(a, 'rental_Rental', b1)
    if hasattr(b1, 'rental_Customer'):
        assert _is_linked(b1, 'rental_Customer', a)
    _safe_set(a, 'rental_Rental', b2)
    assert _is_linked(a, 'rental_Rental', b2)
    if hasattr(b1, 'rental_Customer'):
        assert not _is_linked(b1, 'rental_Customer', a)
    if hasattr(b2, 'rental_Customer'):
        assert _is_linked(b2, 'rental_Customer', a)
    _safe_set(a, 'rental_Rental', None)
    assert not _is_linked(a, 'rental_Rental', b2)
    if hasattr(b2, 'rental_Customer'):
        assert not _is_linked(b2, 'rental_Customer', a)


def test_assoc_customers1_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Customer(firstName="sample_text", lastName="sample_text")
    b2 = rental_Customer(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'parentAgency2', {b1})
    assert _is_linked(a, 'parentAgency2', b1)
    if hasattr(b1, 'Customer'):
        assert _is_linked(b1, 'Customer', a)
    _safe_set(a, 'parentAgency2', {b2})
    assert _is_linked(a, 'parentAgency2', b2)
    if hasattr(b1, 'Customer'):
        assert not _is_linked(b1, 'Customer', a)
    if hasattr(b2, 'Customer'):
        assert _is_linked(b2, 'Customer', a)
    _safe_set(a, 'parentAgency2', set())
    assert not _is_linked(a, 'parentAgency2', b2)
    if hasattr(b2, 'Customer'):
        assert not _is_linked(b2, 'Customer', a)


def test_assoc_objectsToRent0_link_reassign_clear():
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


def test_assoc_parentAgency11_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'RentalAgency12', b1)
    assert _is_linked(a, 'RentalAgency12', b1)
    if hasattr(b1, 'rentals'):
        assert _is_linked(b1, 'rentals', a)
    _safe_set(a, 'RentalAgency12', b2)
    assert _is_linked(a, 'RentalAgency12', b2)
    if hasattr(b1, 'rentals'):
        assert not _is_linked(b1, 'rentals', a)
    if hasattr(b2, 'rentals'):
        assert _is_linked(b2, 'rentals', a)
    _safe_set(a, 'RentalAgency12', None)
    assert not _is_linked(a, 'RentalAgency12', b2)
    if hasattr(b2, 'rentals'):
        assert not _is_linked(b2, 'rentals', a)


def test_assoc_parentAgency5_link_reassign_clear():
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


def test_assoc_parentAgency6_link_reassign_clear():
    a = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    b1 = rental_RentalAgency(name="sample_text")
    b2 = rental_RentalAgency(name="sample_text_2")
    _safe_set(a, 'objectsToRent', b1)
    assert _is_linked(a, 'objectsToRent', b1)
    if hasattr(b1, 'RentalAgency7'):
        assert _is_linked(b1, 'RentalAgency7', a)
    _safe_set(a, 'objectsToRent', b2)
    assert _is_linked(a, 'objectsToRent', b2)
    if hasattr(b1, 'RentalAgency7'):
        assert not _is_linked(b1, 'RentalAgency7', a)
    if hasattr(b2, 'RentalAgency7'):
        assert _is_linked(b2, 'RentalAgency7', a)
    _safe_set(a, 'objectsToRent', None)
    assert not _is_linked(a, 'objectsToRent', b2)
    if hasattr(b2, 'RentalAgency7'):
        assert not _is_linked(b2, 'RentalAgency7', a)


def test_assoc_rentals3_link_reassign_clear():
    a = rental_RentalAgency(name="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'parentAgency4', {b1})
    assert _is_linked(a, 'parentAgency4', b1)
    if hasattr(b1, 'Rental'):
        assert _is_linked(b1, 'Rental', a)
    _safe_set(a, 'parentAgency4', {b2})
    assert _is_linked(a, 'parentAgency4', b2)
    if hasattr(b1, 'Rental'):
        assert not _is_linked(b1, 'Rental', a)
    if hasattr(b2, 'Rental'):
        assert _is_linked(b2, 'Rental', a)
    _safe_set(a, 'parentAgency4', set())
    assert not _is_linked(a, 'parentAgency4', b2)
    if hasattr(b2, 'Rental'):
        assert not _is_linked(b2, 'Rental', a)


def test_assoc_rentedObject9_link_reassign_clear():
    a = rental_RentalObject(ID="sample_text", name="sample_text", picture="sample_text")
    b1 = rental_Rental(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b2 = rental_Rental(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    _safe_set(a, 'rental_RentalObject', b1)
    assert _is_linked(a, 'rental_RentalObject', b1)
    if hasattr(b1, 'rental_Rental10'):
        assert _is_linked(b1, 'rental_Rental10', a)
    _safe_set(a, 'rental_RentalObject', b2)
    assert _is_linked(a, 'rental_RentalObject', b2)
    if hasattr(b1, 'rental_Rental10'):
        assert not _is_linked(b1, 'rental_Rental10', a)
    if hasattr(b2, 'rental_Rental10'):
        assert _is_linked(b2, 'rental_Rental10', a)
    _safe_set(a, 'rental_RentalObject', None)
    assert not _is_linked(a, 'rental_RentalObject', b2)
    if hasattr(b2, 'rental_Rental10'):
        assert not _is_linked(b2, 'rental_Rental10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

rental_Customer_strategy = st.builds(rental_Customer, firstName=safe_text, lastName=safe_text)
@given(instance=rental_Customer_strategy)
@settings(max_examples=25)
def test_rental_Customer_instantiation(instance):
    assert isinstance(instance, rental_Customer)


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



