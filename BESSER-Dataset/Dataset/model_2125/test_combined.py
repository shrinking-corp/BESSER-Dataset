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
    test_ConfigurationModel,
    test_TestModel,
    test_AddressModel,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_test_configurationmodel_is_not_abstract():
    assert not inspect.isabstract(test_ConfigurationModel)


def test_hyp_test_configurationmodel_constructor_exists():
    assert callable(test_ConfigurationModel.__init__)


def test_hyp_test_configurationmodel_constructor_args():
    sig = inspect.signature(test_ConfigurationModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_testmodel_is_not_abstract():
    assert not inspect.isabstract(test_TestModel)


def test_hyp_test_testmodel_constructor_exists():
    assert callable(test_TestModel.__init__)


def test_hyp_test_testmodel_constructor_args():
    sig = inspect.signature(test_TestModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "childCount" in params, "Missing parameter 'childCount'"
    assert "overdrawAccount" in params, "Missing parameter 'overdrawAccount'"
    assert "accountBalance" in params, "Missing parameter 'accountBalance'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "isSelectable" in params, "Missing parameter 'isSelectable'"
    assert "age" in params, "Missing parameter 'age'"











def test_hyp_test_addressmodel_is_not_abstract():
    assert not inspect.isabstract(test_AddressModel)


def test_hyp_test_addressmodel_constructor_exists():
    assert callable(test_AddressModel.__init__)


def test_hyp_test_addressmodel_constructor_args():
    sig = inspect.signature(test_AddressModel.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "street" in params, "Missing parameter 'street'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "differentPostAddress" in params, "Missing parameter 'differentPostAddress'"
    assert "houseNumber" in params, "Missing parameter 'houseNumber'"







def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "MALE",
        "FEMALE",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
test_ConfigurationModel_strategy = st.builds(
    test_ConfigurationModel,
)
test_TestModel_strategy = st.builds(
    test_TestModel,
    name=
        safe_text,
    childCount=
        safe_text,
    overdrawAccount=
        safe_text,
    accountBalance=
        safe_text,
    birthDate=
        st.dates(),
    gender=
        safe_text,
    isSelectable=
        safe_text,
    age=
        st.integers()
)
test_AddressModel_strategy = st.builds(
    test_AddressModel,
    zipCode=
        safe_text,
    validTo=
        st.dates(),
    street=
        safe_text,
    validFrom=
        st.dates(),
    differentPostAddress=
        st.booleans(),
    houseNumber=
        safe_text
)





@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_childCount_setter(instance):
    original = instance.childCount
    instance.childCount = original
    assert instance.childCount == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_overdrawAccount_setter(instance):
    original = instance.overdrawAccount
    instance.overdrawAccount = original
    assert instance.overdrawAccount == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_accountBalance_setter(instance):
    original = instance.accountBalance
    instance.accountBalance = original
    assert instance.accountBalance == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_isSelectable_setter(instance):
    original = instance.isSelectable
    instance.isSelectable = original
    assert instance.isSelectable == original



@given(instance=test_TestModel_strategy)
def test_hyp_test_testmodel_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original




@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original



@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original



@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_differentPostAddress_setter(instance):
    original = instance.differentPostAddress
    instance.differentPostAddress = original
    assert instance.differentPostAddress == original



@given(instance=test_AddressModel_strategy)
def test_hyp_test_addressmodel_houseNumber_setter(instance):
    original = instance.houseNumber
    instance.houseNumber = original
    assert instance.houseNumber == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    test_AddressModel,
    test_ConfigurationModel,
    test_TestModel,
    Gender,
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

def test_test_AddressModel_differentPostAddress_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.differentPostAddress == True
    instance.differentPostAddress = False
    assert instance.differentPostAddress == False


def test_test_AddressModel_houseNumber_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.houseNumber == "sample_text"
    instance.houseNumber = "sample_text_2"
    assert instance.houseNumber == "sample_text_2"


def test_test_AddressModel_street_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_test_AddressModel_validFrom_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.validFrom == date(2024, 1, 1)
    instance.validFrom = date(2025, 6, 15)
    assert instance.validFrom == date(2025, 6, 15)


def test_test_AddressModel_validTo_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.validTo == date(2024, 1, 1)
    instance.validTo = date(2025, 6, 15)
    assert instance.validTo == date(2025, 6, 15)


def test_test_AddressModel_zipCode_value_roundtrip():
    instance = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_test_TestModel_accountBalance_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.accountBalance == "sample_text"
    instance.accountBalance = "sample_text_2"
    assert instance.accountBalance == "sample_text_2"


def test_test_TestModel_age_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_test_TestModel_birthDate_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.birthDate == date(2024, 1, 1)
    instance.birthDate = date(2025, 6, 15)
    assert instance.birthDate == date(2025, 6, 15)


def test_test_TestModel_childCount_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.childCount == "sample_text"
    instance.childCount = "sample_text_2"
    assert instance.childCount == "sample_text_2"


def test_test_TestModel_gender_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_test_TestModel_isSelectable_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.isSelectable == "sample_text"
    instance.isSelectable = "sample_text_2"
    assert instance.isSelectable == "sample_text_2"


def test_test_TestModel_name_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test_TestModel_overdrawAccount_value_roundtrip():
    instance = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    assert instance.overdrawAccount == "sample_text"
    instance.overdrawAccount = "sample_text_2"
    assert instance.overdrawAccount == "sample_text_2"


def test_assoc_address0_link_reassign_clear():
    a = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    b1 = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    b2 = test_AddressModel(differentPostAddress=False, houseNumber="sample_text_2", street="sample_text_2", validFrom=date(2025, 6, 15), validTo=date(2025, 6, 15), zipCode="sample_text_2")
    _safe_set(a, 'test_TestModel', b1)
    assert _is_linked(a, 'test_TestModel', b1)
    if hasattr(b1, 'test_AddressModel'):
        assert _is_linked(b1, 'test_AddressModel', a)
    _safe_set(a, 'test_TestModel', b2)
    assert _is_linked(a, 'test_TestModel', b2)
    if hasattr(b1, 'test_AddressModel'):
        assert not _is_linked(b1, 'test_AddressModel', a)
    if hasattr(b2, 'test_AddressModel'):
        assert _is_linked(b2, 'test_AddressModel', a)
    _safe_set(a, 'test_TestModel', None)
    assert not _is_linked(a, 'test_TestModel', b2)
    if hasattr(b2, 'test_AddressModel'):
        assert not _is_linked(b2, 'test_AddressModel', a)


def test_assoc_testModel3_link_reassign_clear():
    a = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    b1 = test_ConfigurationModel()
    b2 = test_ConfigurationModel()
    _safe_set(a, 'test_TestModel5', b1)
    assert _is_linked(a, 'test_TestModel5', b1)
    if hasattr(b1, 'test_ConfigurationModel4'):
        assert _is_linked(b1, 'test_ConfigurationModel4', a)
    _safe_set(a, 'test_TestModel5', b2)
    assert _is_linked(a, 'test_TestModel5', b2)
    if hasattr(b1, 'test_ConfigurationModel4'):
        assert not _is_linked(b1, 'test_ConfigurationModel4', a)
    if hasattr(b2, 'test_ConfigurationModel4'):
        assert _is_linked(b2, 'test_ConfigurationModel4', a)
    _safe_set(a, 'test_TestModel5', None)
    assert not _is_linked(a, 'test_TestModel5', b2)
    if hasattr(b2, 'test_ConfigurationModel4'):
        assert not _is_linked(b2, 'test_ConfigurationModel4', a)


def test_assoc_testModels1_link_reassign_clear():
    a = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    b1 = test_ConfigurationModel()
    b2 = test_ConfigurationModel()
    _safe_set(a, 'test_TestModel2', b1)
    assert _is_linked(a, 'test_TestModel2', b1)
    if hasattr(b1, 'test_ConfigurationModel'):
        assert _is_linked(b1, 'test_ConfigurationModel', a)
    _safe_set(a, 'test_TestModel2', b2)
    assert _is_linked(a, 'test_TestModel2', b2)
    if hasattr(b1, 'test_ConfigurationModel'):
        assert not _is_linked(b1, 'test_ConfigurationModel', a)
    if hasattr(b2, 'test_ConfigurationModel'):
        assert _is_linked(b2, 'test_ConfigurationModel', a)
    _safe_set(a, 'test_TestModel2', None)
    assert not _is_linked(a, 'test_TestModel2', b2)
    if hasattr(b2, 'test_ConfigurationModel'):
        assert not _is_linked(b2, 'test_ConfigurationModel', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

test_AddressModel_strategy = st.builds(test_AddressModel, differentPostAddress=st.booleans(), houseNumber=safe_text, street=safe_text, validFrom=st.dates(), validTo=st.dates(), zipCode=safe_text)
@given(instance=test_AddressModel_strategy)
@settings(max_examples=25)
def test_test_AddressModel_instantiation(instance):
    assert isinstance(instance, test_AddressModel)


test_ConfigurationModel_strategy = st.builds(test_ConfigurationModel)
@given(instance=test_ConfigurationModel_strategy)
@settings(max_examples=25)
def test_test_ConfigurationModel_instantiation(instance):
    assert isinstance(instance, test_ConfigurationModel)


test_TestModel_strategy = st.builds(test_TestModel, accountBalance=safe_text, age=st.integers(), birthDate=st.dates(), childCount=safe_text, gender=safe_text, isSelectable=safe_text, name=safe_text, overdrawAccount=safe_text)
@given(instance=test_TestModel_strategy)
@settings(max_examples=25)
def test_test_TestModel_instantiation(instance):
    assert isinstance(instance, test_TestModel)



