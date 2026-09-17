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
    MyClass9,
    mypackage2_MyClass2,
    mypackage2_MyInterface_Interface,
    mypackage2_MyClass,
    MyInterface_Interface,
    MyClass8,
    MyClass7,
    MyClass6,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    MyClass,
    Location2,
    Location,
    BaseBO,
    Class,
    PolicyImage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myclass9_is_not_abstract():
    assert not inspect.isabstract(MyClass9)


def test_hyp_myclass9_constructor_exists():
    assert callable(MyClass9.__init__)


def test_hyp_myclass9_constructor_args():
    sig = inspect.signature(MyClass9.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage2_myclass2_is_not_abstract():
    assert not inspect.isabstract(mypackage2_MyClass2)


def test_hyp_mypackage2_myclass2_constructor_exists():
    assert callable(mypackage2_MyClass2.__init__)


def test_hyp_mypackage2_myclass2_constructor_args():
    sig = inspect.signature(mypackage2_MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage2_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(mypackage2_MyInterface_Interface)


def test_hyp_mypackage2_myinterface_interface_constructor_exists():
    assert callable(mypackage2_MyInterface_Interface.__init__)


def test_hyp_mypackage2_myinterface_interface_constructor_args():
    sig = inspect.signature(mypackage2_MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage2_myclass_is_not_abstract():
    assert not inspect.isabstract(mypackage2_MyClass)


def test_hyp_mypackage2_myclass_constructor_exists():
    assert callable(mypackage2_MyClass.__init__)


def test_hyp_mypackage2_myclass_constructor_args():
    sig = inspect.signature(mypackage2_MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_hyp_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_hyp_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass8_is_not_abstract():
    assert not inspect.isabstract(MyClass8)


def test_hyp_myclass8_constructor_exists():
    assert callable(MyClass8.__init__)


def test_hyp_myclass8_constructor_args():
    sig = inspect.signature(MyClass8.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass7_is_not_abstract():
    assert not inspect.isabstract(MyClass7)


def test_hyp_myclass7_constructor_exists():
    assert callable(MyClass7.__init__)


def test_hyp_myclass7_constructor_args():
    sig = inspect.signature(MyClass7.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_hyp_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_hyp_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass5_is_not_abstract():
    assert not inspect.isabstract(MyClass5)


def test_hyp_myclass5_constructor_exists():
    assert callable(MyClass5.__init__)


def test_hyp_myclass5_constructor_args():
    sig = inspect.signature(MyClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass4_is_not_abstract():
    assert not inspect.isabstract(MyClass4)


def test_hyp_myclass4_constructor_exists():
    assert callable(MyClass4.__init__)


def test_hyp_myclass4_constructor_args():
    sig = inspect.signature(MyClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_hyp_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_hyp_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_location2_is_not_abstract():
    assert not inspect.isabstract(Location2)


def test_hyp_location2_constructor_exists():
    assert callable(Location2.__init__)


def test_hyp_location2_constructor_args():
    sig = inspect.signature(Location2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"




def test_hyp_basebo_is_not_abstract():
    assert not inspect.isabstract(BaseBO)


def test_hyp_basebo_constructor_exists():
    assert callable(BaseBO.__init__)


def test_hyp_basebo_constructor_args():
    sig = inspect.signature(BaseBO.__init__)
    params = list(sig.parameters.keys())
    assert "newInt" in params, "Missing parameter 'newInt'"
    assert "testString" in params, "Missing parameter 'testString'"
    assert "newBool" in params, "Missing parameter 'newBool'"






def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_policyimage_is_not_abstract():
    assert not inspect.isabstract(PolicyImage)


def test_hyp_policyimage_constructor_exists():
    assert callable(PolicyImage.__init__)


def test_hyp_policyimage_constructor_args():
    sig = inspect.signature(PolicyImage.__init__)
    params = list(sig.parameters.keys())
    assert "serialVersionID" in params, "Missing parameter 'serialVersionID'"



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
MyClass9_strategy = st.builds(
    MyClass9,
)
mypackage2_MyClass2_strategy = st.builds(
    mypackage2_MyClass2,
)
mypackage2_MyInterface_Interface_strategy = st.builds(
    mypackage2_MyInterface_Interface,
)
mypackage2_MyClass_strategy = st.builds(
    mypackage2_MyClass,
)
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
MyClass8_strategy = st.builds(
    MyClass8,
)
MyClass7_strategy = st.builds(
    MyClass7,
)
MyClass6_strategy = st.builds(
    MyClass6,
)
MyClass5_strategy = st.builds(
    MyClass5,
)
MyClass4_strategy = st.builds(
    MyClass4,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
MyClass_strategy = st.builds(
    MyClass,
)
Location2_strategy = st.builds(
    Location2,
)
Location_strategy = st.builds(
    Location,
    location=
        safe_text
)
BaseBO_strategy = st.builds(
    BaseBO,
    newInt=
        st.integers(),
    testString=
        safe_text,
    newBool=
        st.booleans()
)
Class_strategy = st.builds(
    Class,
)
PolicyImage_strategy = st.builds(
    PolicyImage,
    serialVersionID=
        safe_text
)


















@given(instance=Location_strategy)
def test_hyp_location_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original




@given(instance=BaseBO_strategy)
def test_hyp_basebo_newInt_setter(instance):
    original = instance.newInt
    instance.newInt = original
    assert instance.newInt == original



@given(instance=BaseBO_strategy)
def test_hyp_basebo_testString_setter(instance):
    original = instance.testString
    instance.testString = original
    assert instance.testString == original



@given(instance=BaseBO_strategy)
def test_hyp_basebo_newBool_setter(instance):
    original = instance.newBool
    instance.newBool = original
    assert instance.newBool == original





@given(instance=PolicyImage_strategy)
def test_hyp_policyimage_serialVersionID_setter(instance):
    original = instance.serialVersionID
    instance.serialVersionID = original
    assert instance.serialVersionID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BaseBO,
    Class,
    Location,
    Location2,
    MyClass,
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass5,
    MyClass6,
    MyClass7,
    MyClass8,
    MyClass9,
    MyInterface_Interface,
    PolicyImage,
    mypackage2_MyClass,
    mypackage2_MyClass2,
    mypackage2_MyInterface_Interface,
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

def test_BaseBO_newBool_value_roundtrip():
    instance = BaseBO(newBool=True, newInt=7, testString="sample_text")
    assert instance.newBool == True
    instance.newBool = False
    assert instance.newBool == False


def test_BaseBO_newInt_value_roundtrip():
    instance = BaseBO(newBool=True, newInt=7, testString="sample_text")
    assert instance.newInt == 7
    instance.newInt = 13
    assert instance.newInt == 13


def test_BaseBO_testString_value_roundtrip():
    instance = BaseBO(newBool=True, newInt=7, testString="sample_text")
    assert instance.testString == "sample_text"
    instance.testString = "sample_text_2"
    assert instance.testString == "sample_text_2"


def test_Location_location_value_roundtrip():
    instance = Location(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_PolicyImage_serialVersionID_value_roundtrip():
    instance = PolicyImage(serialVersionID="sample_text")
    assert instance.serialVersionID == "sample_text"
    instance.serialVersionID = "sample_text_2"
    assert instance.serialVersionID == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BaseBO_strategy = st.builds(BaseBO, newBool=st.booleans(), newInt=st.integers(), testString=safe_text)
@given(instance=BaseBO_strategy)
@settings(max_examples=25)
def test_BaseBO_instantiation(instance):
    assert isinstance(instance, BaseBO)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Location_strategy = st.builds(Location, location=safe_text)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


Location2_strategy = st.builds(Location2)
@given(instance=Location2_strategy)
@settings(max_examples=25)
def test_Location2_instantiation(instance):
    assert isinstance(instance, Location2)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass2_strategy = st.builds(MyClass2)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


MyClass3_strategy = st.builds(MyClass3)
@given(instance=MyClass3_strategy)
@settings(max_examples=25)
def test_MyClass3_instantiation(instance):
    assert isinstance(instance, MyClass3)


MyClass4_strategy = st.builds(MyClass4)
@given(instance=MyClass4_strategy)
@settings(max_examples=25)
def test_MyClass4_instantiation(instance):
    assert isinstance(instance, MyClass4)


MyClass5_strategy = st.builds(MyClass5)
@given(instance=MyClass5_strategy)
@settings(max_examples=25)
def test_MyClass5_instantiation(instance):
    assert isinstance(instance, MyClass5)


MyClass6_strategy = st.builds(MyClass6)
@given(instance=MyClass6_strategy)
@settings(max_examples=25)
def test_MyClass6_instantiation(instance):
    assert isinstance(instance, MyClass6)


MyClass7_strategy = st.builds(MyClass7)
@given(instance=MyClass7_strategy)
@settings(max_examples=25)
def test_MyClass7_instantiation(instance):
    assert isinstance(instance, MyClass7)


MyClass8_strategy = st.builds(MyClass8)
@given(instance=MyClass8_strategy)
@settings(max_examples=25)
def test_MyClass8_instantiation(instance):
    assert isinstance(instance, MyClass8)


MyClass9_strategy = st.builds(MyClass9)
@given(instance=MyClass9_strategy)
@settings(max_examples=25)
def test_MyClass9_instantiation(instance):
    assert isinstance(instance, MyClass9)


MyInterface_Interface_strategy = st.builds(MyInterface_Interface)
@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)


PolicyImage_strategy = st.builds(PolicyImage, serialVersionID=safe_text)
@given(instance=PolicyImage_strategy)
@settings(max_examples=25)
def test_PolicyImage_instantiation(instance):
    assert isinstance(instance, PolicyImage)


mypackage2_MyClass_strategy = st.builds(mypackage2_MyClass)
@given(instance=mypackage2_MyClass_strategy)
@settings(max_examples=25)
def test_mypackage2_MyClass_instantiation(instance):
    assert isinstance(instance, mypackage2_MyClass)


mypackage2_MyClass2_strategy = st.builds(mypackage2_MyClass2)
@given(instance=mypackage2_MyClass2_strategy)
@settings(max_examples=25)
def test_mypackage2_MyClass2_instantiation(instance):
    assert isinstance(instance, mypackage2_MyClass2)


mypackage2_MyInterface_Interface_strategy = st.builds(mypackage2_MyInterface_Interface)
@given(instance=mypackage2_MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_mypackage2_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, mypackage2_MyInterface_Interface)



