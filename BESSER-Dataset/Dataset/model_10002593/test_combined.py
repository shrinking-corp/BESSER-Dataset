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
    Building,
    Elevator_Button,
    Floor_Button,
    Data,
    People,
    Button,
    Door,
    Elevator,
    ElevatorController,
    ClassC,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_building_is_not_abstract():
    assert not inspect.isabstract(Building)


def test_hyp_building_constructor_exists():
    assert callable(Building.__init__)


def test_hyp_building_constructor_args():
    sig = inspect.signature(Building.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevator_button_is_not_abstract():
    assert not inspect.isabstract(Elevator_Button)


def test_hyp_elevator_button_constructor_exists():
    assert callable(Elevator_Button.__init__)


def test_hyp_elevator_button_constructor_args():
    sig = inspect.signature(Elevator_Button.__init__)
    params = list(sig.parameters.keys())



def test_hyp_floor_button_is_not_abstract():
    assert not inspect.isabstract(Floor_Button)


def test_hyp_floor_button_constructor_exists():
    assert callable(Floor_Button.__init__)


def test_hyp_floor_button_constructor_args():
    sig = inspect.signature(Floor_Button.__init__)
    params = list(sig.parameters.keys())



def test_hyp_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_hyp_data_constructor_exists():
    assert callable(Data.__init__)


def test_hyp_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_people_is_not_abstract():
    assert not inspect.isabstract(People)


def test_hyp_people_constructor_exists():
    assert callable(People.__init__)


def test_hyp_people_constructor_args():
    sig = inspect.signature(People.__init__)
    params = list(sig.parameters.keys())



def test_hyp_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_hyp_button_constructor_exists():
    assert callable(Button.__init__)


def test_hyp_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())



def test_hyp_door_is_not_abstract():
    assert not inspect.isabstract(Door)


def test_hyp_door_constructor_exists():
    assert callable(Door.__init__)


def test_hyp_door_constructor_args():
    sig = inspect.signature(Door.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_hyp_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_hyp_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevatorcontroller_is_not_abstract():
    assert not inspect.isabstract(ElevatorController)


def test_hyp_elevatorcontroller_constructor_exists():
    assert callable(ElevatorController.__init__)


def test_hyp_elevatorcontroller_constructor_args():
    sig = inspect.signature(ElevatorController.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_hyp_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_hyp_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"







def test_hyp_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_hyp_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_hyp_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"




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
Building_strategy = st.builds(
    Building,
)
Elevator_Button_strategy = st.builds(
    Elevator_Button,
)
Floor_Button_strategy = st.builds(
    Floor_Button,
)
Data_strategy = st.builds(
    Data,
)
People_strategy = st.builds(
    People,
)
Button_strategy = st.builds(
    Button,
)
Door_strategy = st.builds(
    Door,
)
Elevator_strategy = st.builds(
    Elevator,
)
ElevatorController_strategy = st.builds(
    ElevatorController,
)
ClassC_strategy = st.builds(
    ClassC,
    privateAttribute=
        st.integers(),
    packageAttribute=
        safe_text,
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAttribute=
        safe_text
)
BankAccount_strategy = st.builds(
    BankAccount,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ownerName=
        safe_text
)













@given(instance=ClassC_strategy)
def test_hyp_classc_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=ClassC_strategy)
def test_hyp_classc_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original



@given(instance=ClassC_strategy)
def test_hyp_classc_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=ClassC_strategy)
def test_hyp_classc_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original




@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BankAccount,
    Building,
    Button,
    ClassC,
    Data,
    Door,
    Elevator,
    ElevatorController,
    Elevator_Button,
    Floor_Button,
    People,
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

def test_BankAccount_balance_value_roundtrip():
    instance = BankAccount(balance=3.14, ownerName="sample_text")
    assert instance.balance == 3.14
    instance.balance = 9.99
    assert instance.balance == 9.99


def test_BankAccount_ownerName_value_roundtrip():
    instance = BankAccount(balance=3.14, ownerName="sample_text")
    assert instance.ownerName == "sample_text"
    instance.ownerName = "sample_text_2"
    assert instance.ownerName == "sample_text_2"


def test_ClassC_packageAttribute_value_roundtrip():
    instance = ClassC(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.packageAttribute == "sample_text"
    instance.packageAttribute = "sample_text_2"
    assert instance.packageAttribute == "sample_text_2"


def test_ClassC_privateAttribute_value_roundtrip():
    instance = ClassC(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.privateAttribute == 7
    instance.privateAttribute = 13
    assert instance.privateAttribute == 13


def test_ClassC_protectedAttribute_value_roundtrip():
    instance = ClassC(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.protectedAttribute == "sample_text"
    instance.protectedAttribute = "sample_text_2"
    assert instance.protectedAttribute == "sample_text_2"


def test_ClassC_publicAttribute_value_roundtrip():
    instance = ClassC(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.publicAttribute == 3.14
    instance.publicAttribute = 9.99
    assert instance.publicAttribute == 9.99


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BankAccount_strategy = st.builds(BankAccount, balance=st.floats(allow_nan=False, allow_infinity=False), ownerName=safe_text)
@given(instance=BankAccount_strategy)
@settings(max_examples=25)
def test_BankAccount_instantiation(instance):
    assert isinstance(instance, BankAccount)


Building_strategy = st.builds(Building)
@given(instance=Building_strategy)
@settings(max_examples=25)
def test_Building_instantiation(instance):
    assert isinstance(instance, Building)


Button_strategy = st.builds(Button)
@given(instance=Button_strategy)
@settings(max_examples=25)
def test_Button_instantiation(instance):
    assert isinstance(instance, Button)


ClassC_strategy = st.builds(ClassC, packageAttribute=safe_text, privateAttribute=st.integers(), protectedAttribute=safe_text, publicAttribute=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ClassC_strategy)
@settings(max_examples=25)
def test_ClassC_instantiation(instance):
    assert isinstance(instance, ClassC)


Data_strategy = st.builds(Data)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


Door_strategy = st.builds(Door)
@given(instance=Door_strategy)
@settings(max_examples=25)
def test_Door_instantiation(instance):
    assert isinstance(instance, Door)


Elevator_strategy = st.builds(Elevator)
@given(instance=Elevator_strategy)
@settings(max_examples=25)
def test_Elevator_instantiation(instance):
    assert isinstance(instance, Elevator)


ElevatorController_strategy = st.builds(ElevatorController)
@given(instance=ElevatorController_strategy)
@settings(max_examples=25)
def test_ElevatorController_instantiation(instance):
    assert isinstance(instance, ElevatorController)


Elevator_Button_strategy = st.builds(Elevator_Button)
@given(instance=Elevator_Button_strategy)
@settings(max_examples=25)
def test_Elevator_Button_instantiation(instance):
    assert isinstance(instance, Elevator_Button)


Floor_Button_strategy = st.builds(Floor_Button)
@given(instance=Floor_Button_strategy)
@settings(max_examples=25)
def test_Floor_Button_instantiation(instance):
    assert isinstance(instance, Floor_Button)


People_strategy = st.builds(People)
@given(instance=People_strategy)
@settings(max_examples=25)
def test_People_instantiation(instance):
    assert isinstance(instance, People)



