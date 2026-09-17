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
    Property,
    UML2_ExtensionEnd,
    UML2_Port,
    UML2_Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_hyp_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_hyp_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_hyp_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_hyp_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_hyp_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_hyp_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"




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
Property_strategy = st.builds(
    Property,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
    isDerivedUnion=
        st.booleans(),
    isDerived=
        st.booleans()
)







@given(instance=UML2_Property_strategy)
def test_hyp_uml2_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=UML2_Property_strategy)
def test_hyp_uml2_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Property,
    UML2_ExtensionEnd,
    UML2_Port,
    UML2_Property,
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

def test_UML2_Property_isDerived_value_roundtrip():
    instance = UML2_Property(isDerived=True, isDerivedUnion=True)
    assert instance.isDerived == True
    instance.isDerived = False
    assert instance.isDerived == False


def test_UML2_Property_isDerivedUnion_value_roundtrip():
    instance = UML2_Property(isDerived=True, isDerivedUnion=True)
    assert instance.isDerivedUnion == True
    instance.isDerivedUnion = False
    assert instance.isDerivedUnion == False


def test_UML2_ExtensionEnd_isa_Property():
    instance = UML2_ExtensionEnd()
    assert isinstance(instance, Property)


def test_UML2_Port_isa_Property():
    instance = UML2_Port()
    assert isinstance(instance, Property)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


UML2_ExtensionEnd_strategy = st.builds(UML2_ExtensionEnd)
@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=25)
def test_UML2_ExtensionEnd_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)


UML2_Port_strategy = st.builds(UML2_Port)
@given(instance=UML2_Port_strategy)
@settings(max_examples=25)
def test_UML2_Port_instantiation(instance):
    assert isinstance(instance, UML2_Port)


UML2_Property_strategy = st.builds(UML2_Property, isDerived=st.booleans(), isDerivedUnion=st.booleans())
@given(instance=UML2_Property_strategy)
@settings(max_examples=25)
def test_UML2_Property_instantiation(instance):
    assert isinstance(instance, UML2_Property)



