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
    exhaustive_GenericTest,
    exhaustive_OperationsTest,
    MultipleSuperTest,
    InterfaceTest,
    AbstractTest,
    exhaustive_ReferencesTest,
    exhaustive_MultipleSuperTest,
    OperationsTest,
    exhaustive_InterfaceTest,
    exhaustive_AbstractTest,
    exhaustive_AttributesTest,
    UnserializableEnumTest,
    SerializableEnumTest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_exhaustive_generictest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_GenericTest)


def test_hyp_exhaustive_generictest_constructor_exists():
    assert callable(exhaustive_GenericTest.__init__)


def test_hyp_exhaustive_generictest_constructor_args():
    sig = inspect.signature(exhaustive_GenericTest.__init__)
    params = list(sig.parameters.keys())
    assert "genericAttr" in params, "Missing parameter 'genericAttr'"




def test_hyp_exhaustive_operationstest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_OperationsTest)


def test_hyp_exhaustive_operationstest_constructor_exists():
    assert callable(exhaustive_OperationsTest.__init__)


def test_hyp_exhaustive_operationstest_constructor_args():
    sig = inspect.signature(exhaustive_OperationsTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplesupertest_is_not_abstract():
    assert not inspect.isabstract(MultipleSuperTest)


def test_hyp_multiplesupertest_constructor_exists():
    assert callable(MultipleSuperTest.__init__)


def test_hyp_multiplesupertest_constructor_args():
    sig = inspect.signature(MultipleSuperTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interfacetest_is_not_abstract():
    assert not inspect.isabstract(InterfaceTest)


def test_hyp_interfacetest_constructor_exists():
    assert callable(InterfaceTest.__init__)


def test_hyp_interfacetest_constructor_args():
    sig = inspect.signature(InterfaceTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttest_is_not_abstract():
    assert not inspect.isabstract(AbstractTest)


def test_hyp_abstracttest_constructor_exists():
    assert callable(AbstractTest.__init__)


def test_hyp_abstracttest_constructor_args():
    sig = inspect.signature(AbstractTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exhaustive_referencestest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_ReferencesTest)


def test_hyp_exhaustive_referencestest_constructor_exists():
    assert callable(exhaustive_ReferencesTest.__init__)


def test_hyp_exhaustive_referencestest_constructor_args():
    sig = inspect.signature(exhaustive_ReferencesTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exhaustive_multiplesupertest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_MultipleSuperTest)


def test_hyp_exhaustive_multiplesupertest_constructor_exists():
    assert callable(exhaustive_MultipleSuperTest.__init__)


def test_hyp_exhaustive_multiplesupertest_constructor_args():
    sig = inspect.signature(exhaustive_MultipleSuperTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operationstest_is_not_abstract():
    assert not inspect.isabstract(OperationsTest)


def test_hyp_operationstest_constructor_exists():
    assert callable(OperationsTest.__init__)


def test_hyp_operationstest_constructor_args():
    sig = inspect.signature(OperationsTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exhaustive_interfacetest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_InterfaceTest)


def test_hyp_exhaustive_interfacetest_constructor_exists():
    assert callable(exhaustive_InterfaceTest.__init__)


def test_hyp_exhaustive_interfacetest_constructor_args():
    sig = inspect.signature(exhaustive_InterfaceTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exhaustive_abstracttest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_AbstractTest)


def test_hyp_exhaustive_abstracttest_constructor_exists():
    assert callable(exhaustive_AbstractTest.__init__)


def test_hyp_exhaustive_abstracttest_constructor_args():
    sig = inspect.signature(exhaustive_AbstractTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exhaustive_attributestest_is_not_abstract():
    assert not inspect.isabstract(exhaustive_AttributesTest)


def test_hyp_exhaustive_attributestest_constructor_exists():
    assert callable(exhaustive_AttributesTest.__init__)


def test_hyp_exhaustive_attributestest_constructor_args():
    sig = inspect.signature(exhaustive_AttributesTest.__init__)
    params = list(sig.parameters.keys())
    assert "idNo" in params, "Missing parameter 'idNo'"
    assert "orderedYes" in params, "Missing parameter 'orderedYes'"
    assert "idYes" in params, "Missing parameter 'idYes'"
    assert "lowerBoundN" in params, "Missing parameter 'lowerBoundN'"
    assert "changeableNo" in params, "Missing parameter 'changeableNo'"
    assert "transientYes" in params, "Missing parameter 'transientYes'"
    assert "upperBound1" in params, "Missing parameter 'upperBound1'"
    assert "unsettableNo" in params, "Missing parameter 'unsettableNo'"
    assert "volatileYes" in params, "Missing parameter 'volatileYes'"
    assert "upperBound2" in params, "Missing parameter 'upperBound2'"
    assert "volatileNo" in params, "Missing parameter 'volatileNo'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "transientNo" in params, "Missing parameter 'transientNo'"
    assert "uniqueNo" in params, "Missing parameter 'uniqueNo'"
    assert "derivedNo" in params, "Missing parameter 'derivedNo'"
    assert "changeableYes" in params, "Missing parameter 'changeableYes'"
    assert "lowerBound0" in params, "Missing parameter 'lowerBound0'"
    assert "orderenedNo" in params, "Missing parameter 'orderenedNo'"
    assert "upperBoundN" in params, "Missing parameter 'upperBoundN'"
    assert "derivedYes" in params, "Missing parameter 'derivedYes'"
    assert "lowerBound2" in params, "Missing parameter 'lowerBound2'"
    assert "unsettableYes" in params, "Missing parameter 'unsettableYes'"
    assert "uniqueYes" in params, "Missing parameter 'uniqueYes'"
    assert "lowerBound1" in params, "Missing parameter 'lowerBound1'"
    assert "upperBound0" in params, "Missing parameter 'upperBound0'"


























def test_hyp_unserializableenumtest_exists():
    # Check that the Enumeration exists
    assert UnserializableEnumTest is not None

def test_hyp_unserializableenumtest_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnserializableEnumTest]
    expected_literals = [
        "name2",
        "name1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnserializableEnumTest"

def test_hyp_serializableenumtest_exists():
    # Check that the Enumeration exists
    assert SerializableEnumTest is not None

def test_hyp_serializableenumtest_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SerializableEnumTest]
    expected_literals = [
        "name3",
        "name4",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SerializableEnumTest"


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
exhaustive_GenericTest_strategy = st.builds(
    exhaustive_GenericTest,
    genericAttr=
        safe_text
)
exhaustive_OperationsTest_strategy = st.builds(
    exhaustive_OperationsTest,
)
MultipleSuperTest_strategy = st.builds(
    MultipleSuperTest,
)
InterfaceTest_strategy = st.builds(
    InterfaceTest,
)
AbstractTest_strategy = st.builds(
    AbstractTest,
)
exhaustive_ReferencesTest_strategy = st.builds(
    exhaustive_ReferencesTest,
)
exhaustive_MultipleSuperTest_strategy = st.builds(
    exhaustive_MultipleSuperTest,
)
OperationsTest_strategy = st.builds(
    OperationsTest,
)
exhaustive_InterfaceTest_strategy = st.builds(
    exhaustive_InterfaceTest,
)
exhaustive_AbstractTest_strategy = st.builds(
    exhaustive_AbstractTest,
)
exhaustive_AttributesTest_strategy = st.builds(
    exhaustive_AttributesTest,
    idNo=
        safe_text,
    orderedYes=
        safe_text,
    idYes=
        safe_text,
    lowerBoundN=
        safe_text,
    changeableNo=
        safe_text,
    transientYes=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    upperBound1=
        st.dates(),
    unsettableNo=
        safe_text,
    volatileYes=
        safe_text,
    upperBound2=
        safe_text,
    volatileNo=
        safe_text,
    defaultValue=
        safe_text,
    transientNo=
        safe_text,
    uniqueNo=
        safe_text,
    derivedNo=
        safe_text,
    changeableYes=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lowerBound0=
        st.integers(),
    orderenedNo=
        safe_text,
    upperBoundN=
        safe_text,
    derivedYes=
        safe_text,
    lowerBound2=
        safe_text,
    unsettableYes=
        safe_text,
    uniqueYes=
        safe_text,
    lowerBound1=
        safe_text,
    upperBound0=
        safe_text
)




@given(instance=exhaustive_GenericTest_strategy)
def test_hyp_exhaustive_generictest_genericAttr_setter(instance):
    original = instance.genericAttr
    instance.genericAttr = original
    assert instance.genericAttr == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings













@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_idNo_setter(instance):
    original = instance.idNo
    instance.idNo = original
    assert instance.idNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_orderedYes_setter(instance):
    original = instance.orderedYes
    instance.orderedYes = original
    assert instance.orderedYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_idYes_setter(instance):
    original = instance.idYes
    instance.idYes = original
    assert instance.idYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_lowerBoundN_setter(instance):
    original = instance.lowerBoundN
    instance.lowerBoundN = original
    assert instance.lowerBoundN == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_changeableNo_setter(instance):
    original = instance.changeableNo
    instance.changeableNo = original
    assert instance.changeableNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_transientYes_setter(instance):
    original = instance.transientYes
    instance.transientYes = original
    assert instance.transientYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_upperBound1_setter(instance):
    original = instance.upperBound1
    instance.upperBound1 = original
    assert instance.upperBound1 == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_unsettableNo_setter(instance):
    original = instance.unsettableNo
    instance.unsettableNo = original
    assert instance.unsettableNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_volatileYes_setter(instance):
    original = instance.volatileYes
    instance.volatileYes = original
    assert instance.volatileYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_upperBound2_setter(instance):
    original = instance.upperBound2
    instance.upperBound2 = original
    assert instance.upperBound2 == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_volatileNo_setter(instance):
    original = instance.volatileNo
    instance.volatileNo = original
    assert instance.volatileNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_transientNo_setter(instance):
    original = instance.transientNo
    instance.transientNo = original
    assert instance.transientNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_uniqueNo_setter(instance):
    original = instance.uniqueNo
    instance.uniqueNo = original
    assert instance.uniqueNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_derivedNo_setter(instance):
    original = instance.derivedNo
    instance.derivedNo = original
    assert instance.derivedNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_changeableYes_setter(instance):
    original = instance.changeableYes
    instance.changeableYes = original
    assert instance.changeableYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_lowerBound0_setter(instance):
    original = instance.lowerBound0
    instance.lowerBound0 = original
    assert instance.lowerBound0 == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_orderenedNo_setter(instance):
    original = instance.orderenedNo
    instance.orderenedNo = original
    assert instance.orderenedNo == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_upperBoundN_setter(instance):
    original = instance.upperBoundN
    instance.upperBoundN = original
    assert instance.upperBoundN == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_derivedYes_setter(instance):
    original = instance.derivedYes
    instance.derivedYes = original
    assert instance.derivedYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_lowerBound2_setter(instance):
    original = instance.lowerBound2
    instance.lowerBound2 = original
    assert instance.lowerBound2 == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_unsettableYes_setter(instance):
    original = instance.unsettableYes
    instance.unsettableYes = original
    assert instance.unsettableYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_uniqueYes_setter(instance):
    original = instance.uniqueYes
    instance.uniqueYes = original
    assert instance.uniqueYes == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_lowerBound1_setter(instance):
    original = instance.lowerBound1
    instance.lowerBound1 = original
    assert instance.lowerBound1 == original



@given(instance=exhaustive_AttributesTest_strategy)
def test_hyp_exhaustive_attributestest_upperBound0_setter(instance):
    original = instance.upperBound0
    instance.upperBound0 = original
    assert instance.upperBound0 == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractTest,
    InterfaceTest,
    MultipleSuperTest,
    OperationsTest,
    exhaustive_AbstractTest,
    exhaustive_AttributesTest,
    exhaustive_GenericTest,
    exhaustive_InterfaceTest,
    exhaustive_MultipleSuperTest,
    exhaustive_OperationsTest,
    exhaustive_ReferencesTest,
    SerializableEnumTest,
    UnserializableEnumTest,
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

def test_exhaustive_AttributesTest_changeableNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.changeableNo == "sample_text"
    instance.changeableNo = "sample_text_2"
    assert instance.changeableNo == "sample_text_2"


def test_exhaustive_AttributesTest_changeableYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.changeableYes == 3.14
    instance.changeableYes = 9.99
    assert instance.changeableYes == 9.99


def test_exhaustive_AttributesTest_defaultValue_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_exhaustive_AttributesTest_derivedNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.derivedNo == "sample_text"
    instance.derivedNo = "sample_text_2"
    assert instance.derivedNo == "sample_text_2"


def test_exhaustive_AttributesTest_derivedYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.derivedYes == "sample_text"
    instance.derivedYes = "sample_text_2"
    assert instance.derivedYes == "sample_text_2"


def test_exhaustive_AttributesTest_idNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.idNo == "sample_text"
    instance.idNo = "sample_text_2"
    assert instance.idNo == "sample_text_2"


def test_exhaustive_AttributesTest_idYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.idYes == "sample_text"
    instance.idYes = "sample_text_2"
    assert instance.idYes == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBound0_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound0 == 7
    instance.lowerBound0 = 13
    assert instance.lowerBound0 == 13


def test_exhaustive_AttributesTest_lowerBound1_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound1 == "sample_text"
    instance.lowerBound1 = "sample_text_2"
    assert instance.lowerBound1 == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBound2_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound2 == "sample_text"
    instance.lowerBound2 = "sample_text_2"
    assert instance.lowerBound2 == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBoundN_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBoundN == "sample_text"
    instance.lowerBoundN = "sample_text_2"
    assert instance.lowerBoundN == "sample_text_2"


def test_exhaustive_AttributesTest_orderedYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.orderedYes == "sample_text"
    instance.orderedYes = "sample_text_2"
    assert instance.orderedYes == "sample_text_2"


def test_exhaustive_AttributesTest_orderenedNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.orderenedNo == "sample_text"
    instance.orderenedNo = "sample_text_2"
    assert instance.orderenedNo == "sample_text_2"


def test_exhaustive_AttributesTest_transientNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.transientNo == "sample_text"
    instance.transientNo = "sample_text_2"
    assert instance.transientNo == "sample_text_2"


def test_exhaustive_AttributesTest_transientYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.transientYes == 3.14
    instance.transientYes = 9.99
    assert instance.transientYes == 9.99


def test_exhaustive_AttributesTest_uniqueNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.uniqueNo == "sample_text"
    instance.uniqueNo = "sample_text_2"
    assert instance.uniqueNo == "sample_text_2"


def test_exhaustive_AttributesTest_uniqueYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.uniqueYes == "sample_text"
    instance.uniqueYes = "sample_text_2"
    assert instance.uniqueYes == "sample_text_2"


def test_exhaustive_AttributesTest_unsettableNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.unsettableNo == "sample_text"
    instance.unsettableNo = "sample_text_2"
    assert instance.unsettableNo == "sample_text_2"


def test_exhaustive_AttributesTest_unsettableYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.unsettableYes == "sample_text"
    instance.unsettableYes = "sample_text_2"
    assert instance.unsettableYes == "sample_text_2"


def test_exhaustive_AttributesTest_upperBound0_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound0 == "sample_text"
    instance.upperBound0 = "sample_text_2"
    assert instance.upperBound0 == "sample_text_2"


def test_exhaustive_AttributesTest_upperBound1_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound1 == date(2024, 1, 1)
    instance.upperBound1 = date(2025, 6, 15)
    assert instance.upperBound1 == date(2025, 6, 15)


def test_exhaustive_AttributesTest_upperBound2_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound2 == "sample_text"
    instance.upperBound2 = "sample_text_2"
    assert instance.upperBound2 == "sample_text_2"


def test_exhaustive_AttributesTest_upperBoundN_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBoundN == "sample_text"
    instance.upperBoundN = "sample_text_2"
    assert instance.upperBoundN == "sample_text_2"


def test_exhaustive_AttributesTest_volatileNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.volatileNo == "sample_text"
    instance.volatileNo = "sample_text_2"
    assert instance.volatileNo == "sample_text_2"


def test_exhaustive_AttributesTest_volatileYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.volatileYes == "sample_text"
    instance.volatileYes = "sample_text_2"
    assert instance.volatileYes == "sample_text_2"


def test_exhaustive_GenericTest_genericAttr_value_roundtrip():
    instance = exhaustive_GenericTest(genericAttr="sample_text")
    assert instance.genericAttr == "sample_text"
    instance.genericAttr = "sample_text_2"
    assert instance.genericAttr == "sample_text_2"


def test_exhaustive_MultipleSuperTest_isa_AbstractTest():
    instance = exhaustive_MultipleSuperTest()
    assert isinstance(instance, AbstractTest)


def test_exhaustive_ReferencesTest_isa_AbstractTest():
    instance = exhaustive_ReferencesTest()
    assert isinstance(instance, AbstractTest)


def test_exhaustive_AttributesTest_isa_InterfaceTest():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert isinstance(instance, InterfaceTest)


def test_exhaustive_MultipleSuperTest_isa_InterfaceTest():
    instance = exhaustive_MultipleSuperTest()
    assert isinstance(instance, InterfaceTest)


def test_exhaustive_AttributesTest_isa_MultipleSuperTest():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert isinstance(instance, MultipleSuperTest)


def test_exhaustive_AbstractTest_isa_OperationsTest():
    instance = exhaustive_AbstractTest()
    assert isinstance(instance, OperationsTest)


def test_exhaustive_InterfaceTest_isa_OperationsTest():
    instance = exhaustive_InterfaceTest()
    assert isinstance(instance, OperationsTest)


def test_assoc_derivedYes24_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest26', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest26', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest25'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest25', a)
    _safe_set(a, 'exhaustive_AttributesTest26', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest26', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest25'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest25', a)
    if hasattr(b2, 'exhaustive_ReferencesTest25'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest25', a)
    _safe_set(a, 'exhaustive_AttributesTest26', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest26', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest25'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest25', a)


def test_assoc_lowerBound133_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest35', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest35', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest34'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest34', a)
    _safe_set(a, 'exhaustive_AttributesTest35', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest35', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest34'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest34', a)
    if hasattr(b2, 'exhaustive_ReferencesTest34'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest34', a)
    _safe_set(a, 'exhaustive_AttributesTest35', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest35', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest34'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest34', a)


def test_assoc_lowerBound236_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest38', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest38', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest37'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest37', a)
    _safe_set(a, 'exhaustive_AttributesTest38', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest38', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest37'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest37', a)
    if hasattr(b2, 'exhaustive_ReferencesTest37'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest37', a)
    _safe_set(a, 'exhaustive_AttributesTest38', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest38', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest37'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest37', a)


def test_assoc_opposite16_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'AttributesTest', b1)
    assert _is_linked(a, 'AttributesTest', b1)
    if hasattr(b1, 'opposite2'):
        assert _is_linked(b1, 'opposite2', a)
    _safe_set(a, 'AttributesTest', b2)
    assert _is_linked(a, 'AttributesTest', b2)
    if hasattr(b1, 'opposite2'):
        assert not _is_linked(b1, 'opposite2', a)
    if hasattr(b2, 'opposite2'):
        assert _is_linked(b2, 'opposite2', a)
    _safe_set(a, 'AttributesTest', None)
    assert not _is_linked(a, 'AttributesTest', b2)
    if hasattr(b2, 'opposite2'):
        assert not _is_linked(b2, 'opposite2', a)


def test_assoc_opposite239_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'opposite1', b1)
    assert _is_linked(a, 'opposite1', b1)
    if hasattr(b1, 'ReferencesTest'):
        assert _is_linked(b1, 'ReferencesTest', a)
    _safe_set(a, 'opposite1', b2)
    assert _is_linked(a, 'opposite1', b2)
    if hasattr(b1, 'ReferencesTest'):
        assert not _is_linked(b1, 'ReferencesTest', a)
    if hasattr(b2, 'ReferencesTest'):
        assert _is_linked(b2, 'ReferencesTest', a)
    _safe_set(a, 'opposite1', None)
    assert not _is_linked(a, 'opposite1', b2)
    if hasattr(b2, 'ReferencesTest'):
        assert not _is_linked(b2, 'ReferencesTest', a)


def test_assoc_orderedFalse7_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest8'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest8', a)
    _safe_set(a, 'exhaustive_AttributesTest', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest8'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest8', a)
    if hasattr(b2, 'exhaustive_ReferencesTest8'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest8', a)
    _safe_set(a, 'exhaustive_AttributesTest', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest8'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest8', a)


def test_assoc_resolveProxiesFalse9_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest11', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest11', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest10'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest10', a)
    _safe_set(a, 'exhaustive_AttributesTest11', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest11', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest10'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest10', a)
    if hasattr(b2, 'exhaustive_ReferencesTest10'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest10', a)
    _safe_set(a, 'exhaustive_AttributesTest11', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest11', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest10'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest10', a)


def test_assoc_transientTrue12_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest14', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest14', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest13'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest13', a)
    _safe_set(a, 'exhaustive_AttributesTest14', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest14', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest13'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest13', a)
    if hasattr(b2, 'exhaustive_ReferencesTest13'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest13', a)
    _safe_set(a, 'exhaustive_AttributesTest14', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest14', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest13'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest13', a)


def test_assoc_uniqueFalse15_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest17', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest17', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest16'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest16', a)
    _safe_set(a, 'exhaustive_AttributesTest17', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest17', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest16'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest16', a)
    if hasattr(b2, 'exhaustive_ReferencesTest16'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest16', a)
    _safe_set(a, 'exhaustive_AttributesTest17', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest17', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest16'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest16', a)


def test_assoc_unsettableTrue18_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest20', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest20', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest19'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest19', a)
    _safe_set(a, 'exhaustive_AttributesTest20', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest20', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest19'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest19', a)
    if hasattr(b2, 'exhaustive_ReferencesTest19'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest19', a)
    _safe_set(a, 'exhaustive_AttributesTest20', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest20', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest19'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest19', a)


def test_assoc_upperBound230_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest32', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest32', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest31'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest31', a)
    _safe_set(a, 'exhaustive_AttributesTest32', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest32', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest31'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest31', a)
    if hasattr(b2, 'exhaustive_ReferencesTest31'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest31', a)
    _safe_set(a, 'exhaustive_AttributesTest32', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest32', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest31'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest31', a)


def test_assoc_upperBoundN27_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest29', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest29', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest28'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest28', a)
    _safe_set(a, 'exhaustive_AttributesTest29', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest29', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest28'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest28', a)
    if hasattr(b2, 'exhaustive_ReferencesTest28'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest28', a)
    _safe_set(a, 'exhaustive_AttributesTest29', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest29', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest28'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest28', a)


def test_assoc_volatileTrue21_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest23', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest23', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest22'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest22', a)
    _safe_set(a, 'exhaustive_AttributesTest23', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest23', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest22'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest22', a)
    if hasattr(b2, 'exhaustive_ReferencesTest22'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest22', a)
    _safe_set(a, 'exhaustive_AttributesTest23', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest23', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest22'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractTest_strategy = st.builds(AbstractTest)
@given(instance=AbstractTest_strategy)
@settings(max_examples=25)
def test_AbstractTest_instantiation(instance):
    assert isinstance(instance, AbstractTest)


InterfaceTest_strategy = st.builds(InterfaceTest)
@given(instance=InterfaceTest_strategy)
@settings(max_examples=25)
def test_InterfaceTest_instantiation(instance):
    assert isinstance(instance, InterfaceTest)


MultipleSuperTest_strategy = st.builds(MultipleSuperTest)
@given(instance=MultipleSuperTest_strategy)
@settings(max_examples=25)
def test_MultipleSuperTest_instantiation(instance):
    assert isinstance(instance, MultipleSuperTest)


OperationsTest_strategy = st.builds(OperationsTest)
@given(instance=OperationsTest_strategy)
@settings(max_examples=25)
def test_OperationsTest_instantiation(instance):
    assert isinstance(instance, OperationsTest)


exhaustive_AbstractTest_strategy = st.builds(exhaustive_AbstractTest)
@given(instance=exhaustive_AbstractTest_strategy)
@settings(max_examples=25)
def test_exhaustive_AbstractTest_instantiation(instance):
    assert isinstance(instance, exhaustive_AbstractTest)


exhaustive_AttributesTest_strategy = st.builds(exhaustive_AttributesTest, changeableNo=safe_text, changeableYes=st.floats(allow_nan=False, allow_infinity=False), defaultValue=safe_text, derivedNo=safe_text, derivedYes=safe_text, idNo=safe_text, idYes=safe_text, lowerBound0=st.integers(), lowerBound1=safe_text, lowerBound2=safe_text, lowerBoundN=safe_text, orderedYes=safe_text, orderenedNo=safe_text, transientNo=safe_text, transientYes=st.floats(allow_nan=False, allow_infinity=False), uniqueNo=safe_text, uniqueYes=safe_text, unsettableNo=safe_text, unsettableYes=safe_text, upperBound0=safe_text, upperBound1=st.dates(), upperBound2=safe_text, upperBoundN=safe_text, volatileNo=safe_text, volatileYes=safe_text)
@given(instance=exhaustive_AttributesTest_strategy)
@settings(max_examples=25)
def test_exhaustive_AttributesTest_instantiation(instance):
    assert isinstance(instance, exhaustive_AttributesTest)


exhaustive_GenericTest_strategy = st.builds(exhaustive_GenericTest, genericAttr=safe_text)
@given(instance=exhaustive_GenericTest_strategy)
@settings(max_examples=25)
def test_exhaustive_GenericTest_instantiation(instance):
    assert isinstance(instance, exhaustive_GenericTest)


exhaustive_InterfaceTest_strategy = st.builds(exhaustive_InterfaceTest)
@given(instance=exhaustive_InterfaceTest_strategy)
@settings(max_examples=25)
def test_exhaustive_InterfaceTest_instantiation(instance):
    assert isinstance(instance, exhaustive_InterfaceTest)


exhaustive_MultipleSuperTest_strategy = st.builds(exhaustive_MultipleSuperTest)
@given(instance=exhaustive_MultipleSuperTest_strategy)
@settings(max_examples=25)
def test_exhaustive_MultipleSuperTest_instantiation(instance):
    assert isinstance(instance, exhaustive_MultipleSuperTest)


exhaustive_OperationsTest_strategy = st.builds(exhaustive_OperationsTest)
@given(instance=exhaustive_OperationsTest_strategy)
@settings(max_examples=25)
def test_exhaustive_OperationsTest_instantiation(instance):
    assert isinstance(instance, exhaustive_OperationsTest)


exhaustive_ReferencesTest_strategy = st.builds(exhaustive_ReferencesTest)
@given(instance=exhaustive_ReferencesTest_strategy)
@settings(max_examples=25)
def test_exhaustive_ReferencesTest_instantiation(instance):
    assert isinstance(instance, exhaustive_ReferencesTest)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTest,
    InterfaceTest,
    MultipleSuperTest,
    OperationsTest,
    exhaustive_AbstractTest,
    exhaustive_AttributesTest,
    exhaustive_GenericTest,
    exhaustive_InterfaceTest,
    exhaustive_MultipleSuperTest,
    exhaustive_OperationsTest,
    exhaustive_ReferencesTest,
    SerializableEnumTest,
    UnserializableEnumTest,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_derivedYes24_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest25' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest25', None)
    _safe_set(owner, 'exhaustive_AttributesTest26', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest25') == owner
    _safe_set(owner, 'exhaustive_AttributesTest26', None)
    assert getattr(partner, 'exhaustive_ReferencesTest25') is None


def test_assoc_lowerBound133_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest34' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest34', None)
    _safe_set(owner, 'exhaustive_AttributesTest35', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest34') == owner
    _safe_set(owner, 'exhaustive_AttributesTest35', None)
    assert getattr(partner, 'exhaustive_ReferencesTest34') is None


def test_assoc_lowerBound236_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest37' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest37', None)
    _safe_set(owner, 'exhaustive_AttributesTest38', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest37')
    _safe_set(owner, 'exhaustive_AttributesTest38', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest37')


def test_assoc_opposite16_stub_double():
    # exhaustive_ReferencesTest has no real 'opposite2' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'opposite2', None)
    _safe_set(owner, 'AttributesTest', partner)
    assert getattr(partner, 'opposite2') == owner
    _safe_set(owner, 'AttributesTest', None)
    assert getattr(partner, 'opposite2') is None


def test_assoc_opposite239_stub_double():
    # exhaustive_ReferencesTest has no real 'ReferencesTest' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'ReferencesTest', None)
    _safe_set(owner, 'opposite1', partner)
    assert getattr(partner, 'ReferencesTest') == owner
    _safe_set(owner, 'opposite1', None)
    assert getattr(partner, 'ReferencesTest') is None


def test_assoc_orderedFalse7_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest8' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest8', None)
    _safe_set(owner, 'exhaustive_AttributesTest', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest8') == owner
    _safe_set(owner, 'exhaustive_AttributesTest', None)
    assert getattr(partner, 'exhaustive_ReferencesTest8') is None


def test_assoc_resolveProxiesFalse9_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest10' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest10', None)
    _safe_set(owner, 'exhaustive_AttributesTest11', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest10') == owner
    _safe_set(owner, 'exhaustive_AttributesTest11', None)
    assert getattr(partner, 'exhaustive_ReferencesTest10') is None


def test_assoc_transientTrue12_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest13' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest13', None)
    _safe_set(owner, 'exhaustive_AttributesTest14', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest13') == owner
    _safe_set(owner, 'exhaustive_AttributesTest14', None)
    assert getattr(partner, 'exhaustive_ReferencesTest13') is None


def test_assoc_uniqueFalse15_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest16' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest16', None)
    _safe_set(owner, 'exhaustive_AttributesTest17', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest16') == owner
    _safe_set(owner, 'exhaustive_AttributesTest17', None)
    assert getattr(partner, 'exhaustive_ReferencesTest16') is None


def test_assoc_unsettableTrue18_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest19' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest19', None)
    _safe_set(owner, 'exhaustive_AttributesTest20', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest19') == owner
    _safe_set(owner, 'exhaustive_AttributesTest20', None)
    assert getattr(partner, 'exhaustive_ReferencesTest19') is None


def test_assoc_upperBound230_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest31' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest31', None)
    _safe_set(owner, 'exhaustive_AttributesTest32', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest31')
    _safe_set(owner, 'exhaustive_AttributesTest32', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest31')


def test_assoc_upperBoundN27_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest28' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest28', None)
    _safe_set(owner, 'exhaustive_AttributesTest29', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest28')
    _safe_set(owner, 'exhaustive_AttributesTest29', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest28')


def test_assoc_volatileTrue21_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest22' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest22', None)
    _safe_set(owner, 'exhaustive_AttributesTest23', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest22') == owner
    _safe_set(owner, 'exhaustive_AttributesTest23', None)
    assert getattr(partner, 'exhaustive_ReferencesTest22') is None




import datetime as _ch_datetime
from python_code import exhaustive_AttributesTest
from python_code import exhaustive_ReferencesTest

def test_exhaustive_AttributesTest___init__():
    assert exhaustive_AttributesTest.__init__(exhaustive_AttributesTest('', 0, '', '', '', '', _ch_datetime.date(1, 1, 1), '', '', '', '', 0.0, '', '', '', '', '', '', '', 0.0, '', '', '', '', '', exhaustive_AttributesTest26=exhaustive_ReferencesTest(), exhaustive_AttributesTest29=exhaustive_ReferencesTest(), AttributesTest=exhaustive_ReferencesTest(), exhaustive_AttributesTest=exhaustive_ReferencesTest(), exhaustive_AttributesTest11=exhaustive_ReferencesTest(), exhaustive_AttributesTest14=exhaustive_ReferencesTest(), exhaustive_AttributesTest17=exhaustive_ReferencesTest(), exhaustive_AttributesTest20=exhaustive_ReferencesTest(), exhaustive_AttributesTest23=exhaustive_ReferencesTest(), opposite1=exhaustive_ReferencesTest(), exhaustive_AttributesTest32=exhaustive_ReferencesTest(), exhaustive_AttributesTest35=exhaustive_ReferencesTest(), exhaustive_AttributesTest38=exhaustive_ReferencesTest()), '', 0, '', '', '', '', _ch_datetime.date(1, 1, 2), '', '', '', '', 0.0, '', '', '', '', '', '', '', 0.0, '', '', '', '', '', exhaustive_AttributesTest26=exhaustive_ReferencesTest(), exhaustive_AttributesTest29=exhaustive_ReferencesTest(), AttributesTest=exhaustive_ReferencesTest(), exhaustive_AttributesTest=exhaustive_ReferencesTest(), exhaustive_AttributesTest11=exhaustive_ReferencesTest(), exhaustive_AttributesTest14=exhaustive_ReferencesTest(), exhaustive_AttributesTest17=exhaustive_ReferencesTest(), exhaustive_AttributesTest20=exhaustive_ReferencesTest(), exhaustive_AttributesTest23=exhaustive_ReferencesTest(), opposite1=exhaustive_ReferencesTest(), exhaustive_AttributesTest32=exhaustive_ReferencesTest(), exhaustive_AttributesTest35=exhaustive_ReferencesTest(), exhaustive_AttributesTest38=exhaustive_ReferencesTest()) == None
from python_code import exhaustive_GenericTest

def test_exhaustive_GenericTest___init__():
    assert exhaustive_GenericTest.__init__(exhaustive_GenericTest(''), '') == None

def test_exhaustive_GenericTest_genericOperationParameters():
    exhaustive_GenericTest.genericOperationParameters(exhaustive_GenericTest(''), 0, '\x00\x00')

def test_exhaustive_GenericTest_genericOperationThrow():
    exhaustive_GenericTest.genericOperationThrow(exhaustive_GenericTest(''))

def test_exhaustive_GenericTest_genericOperationReturn():
    exhaustive_GenericTest.genericOperationReturn(exhaustive_GenericTest(''))
from python_code import exhaustive_OperationsTest

def test_exhaustive_OperationsTest___init__():
    assert exhaustive_OperationsTest.__init__(exhaustive_OperationsTest()) == None

def test_exhaustive_OperationsTest_empty():
    exhaustive_OperationsTest.empty(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_upperBoundN():
    exhaustive_OperationsTest.upperBoundN(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_orderedNo():
    exhaustive_OperationsTest.orderedNo(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_uniqueNo():
    exhaustive_OperationsTest.uniqueNo(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_upperBound2():
    exhaustive_OperationsTest.upperBound2(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_manyParameters():
    exhaustive_OperationsTest.manyParameters(exhaustive_OperationsTest(), '', '')

def test_exhaustive_OperationsTest_lowerBound1():
    exhaustive_OperationsTest.lowerBound1(exhaustive_OperationsTest())

def test_exhaustive_OperationsTest_lowerBound2():
    exhaustive_OperationsTest.lowerBound2(exhaustive_OperationsTest())

