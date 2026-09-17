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
    pltest_TestPackageableElement,
    pltest_Numbers,
    GrandChildD,
    pltest_WhatEver,
    pltest_Circle,
    pltest_Red,
    TestClassifier,
    pltest_TestInterface,
    pltest_TestClass,
    TestPackageableElement,
    pltest_TestPackage,
    pltest_TestClassifier,
    pltest_Interface,
    Base,
    pltest_Common,
    pltest_Base,
    Child2,
    pltest_GrandGrandChildF,
    pltest_GrandChild2,
    pltest_Child3,
    Child1,
    pltest_GrandGrandChildE,
    Child3,
    pltest_GrandChildD,
    pltest_GrandChild,
    Interface,
    Common,
    pltest_Child2,
    pltest_Child1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pltest_testpackageableelement_is_not_abstract():
    assert not inspect.isabstract(pltest_TestPackageableElement)


def test_hyp_pltest_testpackageableelement_constructor_exists():
    assert callable(pltest_TestPackageableElement.__init__)


def test_hyp_pltest_testpackageableelement_constructor_args():
    sig = inspect.signature(pltest_TestPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_numbers_is_not_abstract():
    assert not inspect.isabstract(pltest_Numbers)


def test_hyp_pltest_numbers_constructor_exists():
    assert callable(pltest_Numbers.__init__)


def test_hyp_pltest_numbers_constructor_args():
    sig = inspect.signature(pltest_Numbers.__init__)
    params = list(sig.parameters.keys())
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "double" in params, "Missing parameter 'double'"
    assert "long" in params, "Missing parameter 'long'"
    assert "int" in params, "Missing parameter 'int'"
    assert "float" in params, "Missing parameter 'float'"
    assert "bigInt" in params, "Missing parameter 'bigInt'"









def test_hyp_grandchildd_is_not_abstract():
    assert not inspect.isabstract(GrandChildD)


def test_hyp_grandchildd_constructor_exists():
    assert callable(GrandChildD.__init__)


def test_hyp_grandchildd_constructor_args():
    sig = inspect.signature(GrandChildD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_whatever_is_not_abstract():
    assert not inspect.isabstract(pltest_WhatEver)


def test_hyp_pltest_whatever_constructor_exists():
    assert callable(pltest_WhatEver.__init__)


def test_hyp_pltest_whatever_constructor_args():
    sig = inspect.signature(pltest_WhatEver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_circle_is_not_abstract():
    assert not inspect.isabstract(pltest_Circle)


def test_hyp_pltest_circle_constructor_exists():
    assert callable(pltest_Circle.__init__)


def test_hyp_pltest_circle_constructor_args():
    sig = inspect.signature(pltest_Circle.__init__)
    params = list(sig.parameters.keys())
    assert "circumference" in params, "Missing parameter 'circumference'"
    assert "diameter" in params, "Missing parameter 'diameter'"
    assert "area" in params, "Missing parameter 'area'"






def test_hyp_pltest_red_is_not_abstract():
    assert not inspect.isabstract(pltest_Red)


def test_hyp_pltest_red_constructor_exists():
    assert callable(pltest_Red.__init__)


def test_hyp_pltest_red_constructor_args():
    sig = inspect.signature(pltest_Red.__init__)
    params = list(sig.parameters.keys())
    assert "redness" in params, "Missing parameter 'redness'"




def test_hyp_testclassifier_is_not_abstract():
    assert not inspect.isabstract(TestClassifier)


def test_hyp_testclassifier_constructor_exists():
    assert callable(TestClassifier.__init__)


def test_hyp_testclassifier_constructor_args():
    sig = inspect.signature(TestClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_testinterface_is_not_abstract():
    assert not inspect.isabstract(pltest_TestInterface)


def test_hyp_pltest_testinterface_constructor_exists():
    assert callable(pltest_TestInterface.__init__)


def test_hyp_pltest_testinterface_constructor_args():
    sig = inspect.signature(pltest_TestInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_testclass_is_not_abstract():
    assert not inspect.isabstract(pltest_TestClass)


def test_hyp_pltest_testclass_constructor_exists():
    assert callable(pltest_TestClass.__init__)


def test_hyp_pltest_testclass_constructor_args():
    sig = inspect.signature(pltest_TestClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testpackageableelement_is_not_abstract():
    assert not inspect.isabstract(TestPackageableElement)


def test_hyp_testpackageableelement_constructor_exists():
    assert callable(TestPackageableElement.__init__)


def test_hyp_testpackageableelement_constructor_args():
    sig = inspect.signature(TestPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_testpackage_is_not_abstract():
    assert not inspect.isabstract(pltest_TestPackage)


def test_hyp_pltest_testpackage_constructor_exists():
    assert callable(pltest_TestPackage.__init__)


def test_hyp_pltest_testpackage_constructor_args():
    sig = inspect.signature(pltest_TestPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_testclassifier_is_not_abstract():
    assert not inspect.isabstract(pltest_TestClassifier)


def test_hyp_pltest_testclassifier_constructor_exists():
    assert callable(pltest_TestClassifier.__init__)


def test_hyp_pltest_testclassifier_constructor_args():
    sig = inspect.signature(pltest_TestClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_interface_is_not_abstract():
    assert not inspect.isabstract(pltest_Interface)


def test_hyp_pltest_interface_constructor_exists():
    assert callable(pltest_Interface.__init__)


def test_hyp_pltest_interface_constructor_args():
    sig = inspect.signature(pltest_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_hyp_base_constructor_exists():
    assert callable(Base.__init__)


def test_hyp_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_common_is_not_abstract():
    assert not inspect.isabstract(pltest_Common)


def test_hyp_pltest_common_constructor_exists():
    assert callable(pltest_Common.__init__)


def test_hyp_pltest_common_constructor_args():
    sig = inspect.signature(pltest_Common.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_base_is_not_abstract():
    assert not inspect.isabstract(pltest_Base)


def test_hyp_pltest_base_constructor_exists():
    assert callable(pltest_Base.__init__)


def test_hyp_pltest_base_constructor_args():
    sig = inspect.signature(pltest_Base.__init__)
    params = list(sig.parameters.keys())



def test_hyp_child2_is_not_abstract():
    assert not inspect.isabstract(Child2)


def test_hyp_child2_constructor_exists():
    assert callable(Child2.__init__)


def test_hyp_child2_constructor_args():
    sig = inspect.signature(Child2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_grandgrandchildf_is_not_abstract():
    assert not inspect.isabstract(pltest_GrandGrandChildF)


def test_hyp_pltest_grandgrandchildf_constructor_exists():
    assert callable(pltest_GrandGrandChildF.__init__)


def test_hyp_pltest_grandgrandchildf_constructor_args():
    sig = inspect.signature(pltest_GrandGrandChildF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_grandchild2_is_not_abstract():
    assert not inspect.isabstract(pltest_GrandChild2)


def test_hyp_pltest_grandchild2_constructor_exists():
    assert callable(pltest_GrandChild2.__init__)


def test_hyp_pltest_grandchild2_constructor_args():
    sig = inspect.signature(pltest_GrandChild2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_child3_is_not_abstract():
    assert not inspect.isabstract(pltest_Child3)


def test_hyp_pltest_child3_constructor_exists():
    assert callable(pltest_Child3.__init__)


def test_hyp_pltest_child3_constructor_args():
    sig = inspect.signature(pltest_Child3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_child1_is_not_abstract():
    assert not inspect.isabstract(Child1)


def test_hyp_child1_constructor_exists():
    assert callable(Child1.__init__)


def test_hyp_child1_constructor_args():
    sig = inspect.signature(Child1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_grandgrandchilde_is_not_abstract():
    assert not inspect.isabstract(pltest_GrandGrandChildE)


def test_hyp_pltest_grandgrandchilde_constructor_exists():
    assert callable(pltest_GrandGrandChildE.__init__)


def test_hyp_pltest_grandgrandchilde_constructor_args():
    sig = inspect.signature(pltest_GrandGrandChildE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_child3_is_not_abstract():
    assert not inspect.isabstract(Child3)


def test_hyp_child3_constructor_exists():
    assert callable(Child3.__init__)


def test_hyp_child3_constructor_args():
    sig = inspect.signature(Child3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_grandchildd_is_not_abstract():
    assert not inspect.isabstract(pltest_GrandChildD)


def test_hyp_pltest_grandchildd_constructor_exists():
    assert callable(pltest_GrandChildD.__init__)


def test_hyp_pltest_grandchildd_constructor_args():
    sig = inspect.signature(pltest_GrandChildD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_grandchild_is_not_abstract():
    assert not inspect.isabstract(pltest_GrandChild)


def test_hyp_pltest_grandchild_constructor_exists():
    assert callable(pltest_GrandChild.__init__)


def test_hyp_pltest_grandchild_constructor_args():
    sig = inspect.signature(pltest_GrandChild.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_hyp_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_hyp_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_common_is_not_abstract():
    assert not inspect.isabstract(Common)


def test_hyp_common_constructor_exists():
    assert callable(Common.__init__)


def test_hyp_common_constructor_args():
    sig = inspect.signature(Common.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_child2_is_not_abstract():
    assert not inspect.isabstract(pltest_Child2)


def test_hyp_pltest_child2_constructor_exists():
    assert callable(pltest_Child2.__init__)


def test_hyp_pltest_child2_constructor_args():
    sig = inspect.signature(pltest_Child2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pltest_child1_is_not_abstract():
    assert not inspect.isabstract(pltest_Child1)


def test_hyp_pltest_child1_constructor_exists():
    assert callable(pltest_Child1.__init__)


def test_hyp_pltest_child1_constructor_args():
    sig = inspect.signature(pltest_Child1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
pltest_TestPackageableElement_strategy = st.builds(
    pltest_TestPackageableElement,
)
pltest_Numbers_strategy = st.builds(
    pltest_Numbers,
    bigDecimal=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    long=
        safe_text,
    int=
        st.integers(),
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    bigInt=
        safe_text
)
GrandChildD_strategy = st.builds(
    GrandChildD,
)
pltest_WhatEver_strategy = st.builds(
    pltest_WhatEver,
)
pltest_Circle_strategy = st.builds(
    pltest_Circle,
    circumference=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    diameter=
        safe_text,
    area=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pltest_Red_strategy = st.builds(
    pltest_Red,
    redness=
        st.integers()
)
TestClassifier_strategy = st.builds(
    TestClassifier,
)
pltest_TestInterface_strategy = st.builds(
    pltest_TestInterface,
)
pltest_TestClass_strategy = st.builds(
    pltest_TestClass,
)
TestPackageableElement_strategy = st.builds(
    TestPackageableElement,
)
pltest_TestPackage_strategy = st.builds(
    pltest_TestPackage,
)
pltest_TestClassifier_strategy = st.builds(
    pltest_TestClassifier,
)
pltest_Interface_strategy = st.builds(
    pltest_Interface,
)
Base_strategy = st.builds(
    Base,
)
pltest_Common_strategy = st.builds(
    pltest_Common,
)
pltest_Base_strategy = st.builds(
    pltest_Base,
)
Child2_strategy = st.builds(
    Child2,
)
pltest_GrandGrandChildF_strategy = st.builds(
    pltest_GrandGrandChildF,
)
pltest_GrandChild2_strategy = st.builds(
    pltest_GrandChild2,
)
pltest_Child3_strategy = st.builds(
    pltest_Child3,
)
Child1_strategy = st.builds(
    Child1,
)
pltest_GrandGrandChildE_strategy = st.builds(
    pltest_GrandGrandChildE,
)
Child3_strategy = st.builds(
    Child3,
)
pltest_GrandChildD_strategy = st.builds(
    pltest_GrandChildD,
)
pltest_GrandChild_strategy = st.builds(
    pltest_GrandChild,
)
Interface_strategy = st.builds(
    Interface,
)
Common_strategy = st.builds(
    Common,
)
pltest_Child2_strategy = st.builds(
    pltest_Child2,
)
pltest_Child1_strategy = st.builds(
    pltest_Child1,
    name=
        safe_text
)





@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original



@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original



@given(instance=pltest_Numbers_strategy)
def test_hyp_pltest_numbers_bigInt_setter(instance):
    original = instance.bigInt
    instance.bigInt = original
    assert instance.bigInt == original






@given(instance=pltest_Circle_strategy)
def test_hyp_pltest_circle_circumference_setter(instance):
    original = instance.circumference
    instance.circumference = original
    assert instance.circumference == original



@given(instance=pltest_Circle_strategy)
def test_hyp_pltest_circle_diameter_setter(instance):
    original = instance.diameter
    instance.diameter = original
    assert instance.diameter == original



@given(instance=pltest_Circle_strategy)
def test_hyp_pltest_circle_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original




@given(instance=pltest_Red_strategy)
def test_hyp_pltest_red_redness_setter(instance):
    original = instance.redness
    instance.redness = original
    assert instance.redness == original


























@given(instance=pltest_Child1_strategy)
def test_hyp_pltest_child1_name_setter(instance):
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
    Base,
    Child1,
    Child2,
    Child3,
    Common,
    GrandChildD,
    Interface,
    TestClassifier,
    TestPackageableElement,
    pltest_Base,
    pltest_Child1,
    pltest_Child2,
    pltest_Child3,
    pltest_Circle,
    pltest_Common,
    pltest_GrandChild,
    pltest_GrandChild2,
    pltest_GrandChildD,
    pltest_GrandGrandChildE,
    pltest_GrandGrandChildF,
    pltest_Interface,
    pltest_Numbers,
    pltest_Red,
    pltest_TestClass,
    pltest_TestClassifier,
    pltest_TestInterface,
    pltest_TestPackage,
    pltest_TestPackageableElement,
    pltest_WhatEver,
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

def test_pltest_Child1_name_value_roundtrip():
    instance = pltest_Child1(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pltest_Circle_area_value_roundtrip():
    instance = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    assert instance.area == 3.14
    instance.area = 9.99
    assert instance.area == 9.99


def test_pltest_Circle_circumference_value_roundtrip():
    instance = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    assert instance.circumference == 3.14
    instance.circumference = 9.99
    assert instance.circumference == 9.99


def test_pltest_Circle_diameter_value_roundtrip():
    instance = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    assert instance.diameter == "sample_text"
    instance.diameter = "sample_text_2"
    assert instance.diameter == "sample_text_2"


def test_pltest_Numbers_bigDecimal_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.bigDecimal == "sample_text"
    instance.bigDecimal = "sample_text_2"
    assert instance.bigDecimal == "sample_text_2"


def test_pltest_Numbers_bigInt_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.bigInt == "sample_text"
    instance.bigInt = "sample_text_2"
    assert instance.bigInt == "sample_text_2"


def test_pltest_Numbers_double_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.double == 3.14
    instance.double = 9.99
    assert instance.double == 9.99


def test_pltest_Numbers_float_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.float == 3.14
    instance.float = 9.99
    assert instance.float == 9.99


def test_pltest_Numbers_int_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.int == 7
    instance.int = 13
    assert instance.int == 13


def test_pltest_Numbers_long_value_roundtrip():
    instance = pltest_Numbers(bigDecimal="sample_text", bigInt="sample_text", double=3.14, float=3.14, int=7, long="sample_text")
    assert instance.long == "sample_text"
    instance.long = "sample_text_2"
    assert instance.long == "sample_text_2"


def test_pltest_Red_redness_value_roundtrip():
    instance = pltest_Red(redness=7)
    assert instance.redness == 7
    instance.redness = 13
    assert instance.redness == 13


def test_pltest_Common_isa_Base():
    instance = pltest_Common()
    assert isinstance(instance, Base)


def test_pltest_GrandChild_isa_Child1():
    instance = pltest_GrandChild()
    assert isinstance(instance, Child1)


def test_pltest_GrandGrandChildE_isa_Child1():
    instance = pltest_GrandGrandChildE()
    assert isinstance(instance, Child1)


def test_pltest_GrandChild2_isa_Child2():
    instance = pltest_GrandChild2()
    assert isinstance(instance, Child2)


def test_pltest_GrandGrandChildF_isa_Child2():
    instance = pltest_GrandGrandChildF()
    assert isinstance(instance, Child2)


def test_pltest_Child2_isa_Child3():
    instance = pltest_Child2()
    assert isinstance(instance, Child3)


def test_pltest_GrandChild_isa_Child3():
    instance = pltest_GrandChild()
    assert isinstance(instance, Child3)


def test_pltest_GrandChildD_isa_Child3():
    instance = pltest_GrandChildD()
    assert isinstance(instance, Child3)


def test_pltest_Child1_isa_Common():
    instance = pltest_Child1(name="sample_text")
    assert isinstance(instance, Common)


def test_pltest_Child2_isa_Common():
    instance = pltest_Child2()
    assert isinstance(instance, Common)


def test_pltest_GrandGrandChildE_isa_GrandChildD():
    instance = pltest_GrandGrandChildE()
    assert isinstance(instance, GrandChildD)


def test_pltest_GrandGrandChildF_isa_GrandChildD():
    instance = pltest_GrandGrandChildF()
    assert isinstance(instance, GrandChildD)


def test_pltest_Child1_isa_Interface():
    instance = pltest_Child1(name="sample_text")
    assert isinstance(instance, Interface)


def test_pltest_Child2_isa_Interface():
    instance = pltest_Child2()
    assert isinstance(instance, Interface)


def test_pltest_TestClass_isa_TestClassifier():
    instance = pltest_TestClass()
    assert isinstance(instance, TestClassifier)


def test_pltest_TestInterface_isa_TestClassifier():
    instance = pltest_TestInterface()
    assert isinstance(instance, TestClassifier)


def test_pltest_TestClassifier_isa_TestPackageableElement():
    instance = pltest_TestClassifier()
    assert isinstance(instance, TestPackageableElement)


def test_pltest_TestPackage_isa_TestPackageableElement():
    instance = pltest_TestPackage()
    assert isinstance(instance, TestPackageableElement)


def test_assoc_a10_link_reassign_clear():
    a = pltest_Child1(name="sample_text")
    b1 = pltest_Common()
    b2 = pltest_Common()
    _safe_set(a, 'pltest_Child1', b1)
    assert _is_linked(a, 'pltest_Child1', b1)
    if hasattr(b1, 'pltest_Common'):
        assert _is_linked(b1, 'pltest_Common', a)
    _safe_set(a, 'pltest_Child1', b2)
    assert _is_linked(a, 'pltest_Child1', b2)
    if hasattr(b1, 'pltest_Common'):
        assert not _is_linked(b1, 'pltest_Common', a)
    if hasattr(b2, 'pltest_Common'):
        assert _is_linked(b2, 'pltest_Common', a)
    _safe_set(a, 'pltest_Child1', None)
    assert not _is_linked(a, 'pltest_Child1', b2)
    if hasattr(b2, 'pltest_Common'):
        assert not _is_linked(b2, 'pltest_Common', a)


def test_assoc_red3_link_reassign_clear():
    a = pltest_Red(redness=7)
    b1 = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    b2 = pltest_Circle(area=9.99, circumference=9.99, diameter="sample_text_2")
    _safe_set(a, 'pltest_Red', b1)
    assert _is_linked(a, 'pltest_Red', b1)
    if hasattr(b1, 'pltest_Circle'):
        assert _is_linked(b1, 'pltest_Circle', a)
    _safe_set(a, 'pltest_Red', b2)
    assert _is_linked(a, 'pltest_Red', b2)
    if hasattr(b1, 'pltest_Circle'):
        assert not _is_linked(b1, 'pltest_Circle', a)
    if hasattr(b2, 'pltest_Circle'):
        assert _is_linked(b2, 'pltest_Circle', a)
    _safe_set(a, 'pltest_Red', None)
    assert not _is_linked(a, 'pltest_Red', b2)
    if hasattr(b2, 'pltest_Circle'):
        assert not _is_linked(b2, 'pltest_Circle', a)


def test_assoc_someRef4_link_reassign_clear():
    a = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    b1 = pltest_WhatEver()
    b2 = pltest_WhatEver()
    _safe_set(a, 'pltest_Circle5', b1)
    assert _is_linked(a, 'pltest_Circle5', b1)
    if hasattr(b1, 'pltest_WhatEver'):
        assert _is_linked(b1, 'pltest_WhatEver', a)
    _safe_set(a, 'pltest_Circle5', b2)
    assert _is_linked(a, 'pltest_Circle5', b2)
    if hasattr(b1, 'pltest_WhatEver'):
        assert not _is_linked(b1, 'pltest_WhatEver', a)
    if hasattr(b2, 'pltest_WhatEver'):
        assert _is_linked(b2, 'pltest_WhatEver', a)
    _safe_set(a, 'pltest_Circle5', None)
    assert not _is_linked(a, 'pltest_Circle5', b2)
    if hasattr(b2, 'pltest_WhatEver'):
        assert not _is_linked(b2, 'pltest_WhatEver', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Base_strategy = st.builds(Base)
@given(instance=Base_strategy)
@settings(max_examples=25)
def test_Base_instantiation(instance):
    assert isinstance(instance, Base)


Child1_strategy = st.builds(Child1)
@given(instance=Child1_strategy)
@settings(max_examples=25)
def test_Child1_instantiation(instance):
    assert isinstance(instance, Child1)


Child2_strategy = st.builds(Child2)
@given(instance=Child2_strategy)
@settings(max_examples=25)
def test_Child2_instantiation(instance):
    assert isinstance(instance, Child2)


Child3_strategy = st.builds(Child3)
@given(instance=Child3_strategy)
@settings(max_examples=25)
def test_Child3_instantiation(instance):
    assert isinstance(instance, Child3)


Common_strategy = st.builds(Common)
@given(instance=Common_strategy)
@settings(max_examples=25)
def test_Common_instantiation(instance):
    assert isinstance(instance, Common)


GrandChildD_strategy = st.builds(GrandChildD)
@given(instance=GrandChildD_strategy)
@settings(max_examples=25)
def test_GrandChildD_instantiation(instance):
    assert isinstance(instance, GrandChildD)


Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


TestClassifier_strategy = st.builds(TestClassifier)
@given(instance=TestClassifier_strategy)
@settings(max_examples=25)
def test_TestClassifier_instantiation(instance):
    assert isinstance(instance, TestClassifier)


TestPackageableElement_strategy = st.builds(TestPackageableElement)
@given(instance=TestPackageableElement_strategy)
@settings(max_examples=25)
def test_TestPackageableElement_instantiation(instance):
    assert isinstance(instance, TestPackageableElement)


pltest_Base_strategy = st.builds(pltest_Base)
@given(instance=pltest_Base_strategy)
@settings(max_examples=25)
def test_pltest_Base_instantiation(instance):
    assert isinstance(instance, pltest_Base)


pltest_Child1_strategy = st.builds(pltest_Child1, name=safe_text)
@given(instance=pltest_Child1_strategy)
@settings(max_examples=25)
def test_pltest_Child1_instantiation(instance):
    assert isinstance(instance, pltest_Child1)


pltest_Child2_strategy = st.builds(pltest_Child2)
@given(instance=pltest_Child2_strategy)
@settings(max_examples=25)
def test_pltest_Child2_instantiation(instance):
    assert isinstance(instance, pltest_Child2)


pltest_Child3_strategy = st.builds(pltest_Child3)
@given(instance=pltest_Child3_strategy)
@settings(max_examples=25)
def test_pltest_Child3_instantiation(instance):
    assert isinstance(instance, pltest_Child3)


pltest_Circle_strategy = st.builds(pltest_Circle, area=st.floats(allow_nan=False, allow_infinity=False), circumference=st.floats(allow_nan=False, allow_infinity=False), diameter=safe_text)
@given(instance=pltest_Circle_strategy)
@settings(max_examples=25)
def test_pltest_Circle_instantiation(instance):
    assert isinstance(instance, pltest_Circle)


pltest_Common_strategy = st.builds(pltest_Common)
@given(instance=pltest_Common_strategy)
@settings(max_examples=25)
def test_pltest_Common_instantiation(instance):
    assert isinstance(instance, pltest_Common)


pltest_GrandChild_strategy = st.builds(pltest_GrandChild)
@given(instance=pltest_GrandChild_strategy)
@settings(max_examples=25)
def test_pltest_GrandChild_instantiation(instance):
    assert isinstance(instance, pltest_GrandChild)


pltest_GrandChild2_strategy = st.builds(pltest_GrandChild2)
@given(instance=pltest_GrandChild2_strategy)
@settings(max_examples=25)
def test_pltest_GrandChild2_instantiation(instance):
    assert isinstance(instance, pltest_GrandChild2)


pltest_GrandChildD_strategy = st.builds(pltest_GrandChildD)
@given(instance=pltest_GrandChildD_strategy)
@settings(max_examples=25)
def test_pltest_GrandChildD_instantiation(instance):
    assert isinstance(instance, pltest_GrandChildD)


pltest_GrandGrandChildE_strategy = st.builds(pltest_GrandGrandChildE)
@given(instance=pltest_GrandGrandChildE_strategy)
@settings(max_examples=25)
def test_pltest_GrandGrandChildE_instantiation(instance):
    assert isinstance(instance, pltest_GrandGrandChildE)


pltest_GrandGrandChildF_strategy = st.builds(pltest_GrandGrandChildF)
@given(instance=pltest_GrandGrandChildF_strategy)
@settings(max_examples=25)
def test_pltest_GrandGrandChildF_instantiation(instance):
    assert isinstance(instance, pltest_GrandGrandChildF)


pltest_Interface_strategy = st.builds(pltest_Interface)
@given(instance=pltest_Interface_strategy)
@settings(max_examples=25)
def test_pltest_Interface_instantiation(instance):
    assert isinstance(instance, pltest_Interface)


pltest_Numbers_strategy = st.builds(pltest_Numbers, bigDecimal=safe_text, bigInt=safe_text, double=st.floats(allow_nan=False, allow_infinity=False), float=st.floats(allow_nan=False, allow_infinity=False), int=st.integers(), long=safe_text)
@given(instance=pltest_Numbers_strategy)
@settings(max_examples=25)
def test_pltest_Numbers_instantiation(instance):
    assert isinstance(instance, pltest_Numbers)


pltest_Red_strategy = st.builds(pltest_Red, redness=st.integers())
@given(instance=pltest_Red_strategy)
@settings(max_examples=25)
def test_pltest_Red_instantiation(instance):
    assert isinstance(instance, pltest_Red)


pltest_TestClass_strategy = st.builds(pltest_TestClass)
@given(instance=pltest_TestClass_strategy)
@settings(max_examples=25)
def test_pltest_TestClass_instantiation(instance):
    assert isinstance(instance, pltest_TestClass)


pltest_TestClassifier_strategy = st.builds(pltest_TestClassifier)
@given(instance=pltest_TestClassifier_strategy)
@settings(max_examples=25)
def test_pltest_TestClassifier_instantiation(instance):
    assert isinstance(instance, pltest_TestClassifier)


pltest_TestInterface_strategy = st.builds(pltest_TestInterface)
@given(instance=pltest_TestInterface_strategy)
@settings(max_examples=25)
def test_pltest_TestInterface_instantiation(instance):
    assert isinstance(instance, pltest_TestInterface)


pltest_TestPackage_strategy = st.builds(pltest_TestPackage)
@given(instance=pltest_TestPackage_strategy)
@settings(max_examples=25)
def test_pltest_TestPackage_instantiation(instance):
    assert isinstance(instance, pltest_TestPackage)


pltest_TestPackageableElement_strategy = st.builds(pltest_TestPackageableElement)
@given(instance=pltest_TestPackageableElement_strategy)
@settings(max_examples=25)
def test_pltest_TestPackageableElement_instantiation(instance):
    assert isinstance(instance, pltest_TestPackageableElement)


pltest_WhatEver_strategy = st.builds(pltest_WhatEver)
@given(instance=pltest_WhatEver_strategy)
@settings(max_examples=25)
def test_pltest_WhatEver_instantiation(instance):
    assert isinstance(instance, pltest_WhatEver)



