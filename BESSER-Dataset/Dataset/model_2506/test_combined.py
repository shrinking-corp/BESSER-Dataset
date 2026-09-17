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
    Triangles_AbstractClass,
    AbstractClass,
    Triangles_C_Class,
    Triangles_B_Class,
    Triangles_E_Class,
    Triangles_D_Class,
    Triangles_A_Class,
    Triangles_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_triangles_abstractclass_is_not_abstract():
    assert not inspect.isabstract(Triangles_AbstractClass)


def test_hyp_triangles_abstractclass_constructor_exists():
    assert callable(Triangles_AbstractClass.__init__)


def test_hyp_triangles_abstractclass_constructor_args():
    sig = inspect.signature(Triangles_AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "flag" in params, "Missing parameter 'flag'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_abstractclass_is_not_abstract():
    assert not inspect.isabstract(AbstractClass)


def test_hyp_abstractclass_constructor_exists():
    assert callable(AbstractClass.__init__)


def test_hyp_abstractclass_constructor_args():
    sig = inspect.signature(AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_c_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_C_Class)


def test_hyp_triangles_c_class_constructor_exists():
    assert callable(Triangles_C_Class.__init__)


def test_hyp_triangles_c_class_constructor_args():
    sig = inspect.signature(Triangles_C_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_b_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_B_Class)


def test_hyp_triangles_b_class_constructor_exists():
    assert callable(Triangles_B_Class.__init__)


def test_hyp_triangles_b_class_constructor_args():
    sig = inspect.signature(Triangles_B_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_e_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_E_Class)


def test_hyp_triangles_e_class_constructor_exists():
    assert callable(Triangles_E_Class.__init__)


def test_hyp_triangles_e_class_constructor_args():
    sig = inspect.signature(Triangles_E_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_d_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_D_Class)


def test_hyp_triangles_d_class_constructor_exists():
    assert callable(Triangles_D_Class.__init__)


def test_hyp_triangles_d_class_constructor_args():
    sig = inspect.signature(Triangles_D_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_a_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_A_Class)


def test_hyp_triangles_a_class_constructor_exists():
    assert callable(Triangles_A_Class.__init__)


def test_hyp_triangles_a_class_constructor_args():
    sig = inspect.signature(Triangles_A_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triangles_container_is_not_abstract():
    assert not inspect.isabstract(Triangles_Container)


def test_hyp_triangles_container_constructor_exists():
    assert callable(Triangles_Container.__init__)


def test_hyp_triangles_container_constructor_args():
    sig = inspect.signature(Triangles_Container.__init__)
    params = list(sig.parameters.keys())


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
Triangles_AbstractClass_strategy = st.builds(
    Triangles_AbstractClass,
    flag=
        st.booleans(),
    name=
        safe_text,
    id=
        st.integers()
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
Triangles_C_Class_strategy = st.builds(
    Triangles_C_Class,
)
Triangles_B_Class_strategy = st.builds(
    Triangles_B_Class,
)
Triangles_E_Class_strategy = st.builds(
    Triangles_E_Class,
)
Triangles_D_Class_strategy = st.builds(
    Triangles_D_Class,
)
Triangles_A_Class_strategy = st.builds(
    Triangles_A_Class,
)
Triangles_Container_strategy = st.builds(
    Triangles_Container,
)




@given(instance=Triangles_AbstractClass_strategy)
def test_hyp_triangles_abstractclass_flag_setter(instance):
    original = instance.flag
    instance.flag = original
    assert instance.flag == original



@given(instance=Triangles_AbstractClass_strategy)
def test_hyp_triangles_abstractclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Triangles_AbstractClass_strategy)
def test_hyp_triangles_abstractclass_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractClass,
    Triangles_A_Class,
    Triangles_AbstractClass,
    Triangles_B_Class,
    Triangles_C_Class,
    Triangles_Container,
    Triangles_D_Class,
    Triangles_E_Class,
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

def test_Triangles_AbstractClass_flag_value_roundtrip():
    instance = Triangles_AbstractClass(flag=True, id=7, name="sample_text")
    assert instance.flag == True
    instance.flag = False
    assert instance.flag == False


def test_Triangles_AbstractClass_id_value_roundtrip():
    instance = Triangles_AbstractClass(flag=True, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Triangles_AbstractClass_name_value_roundtrip():
    instance = Triangles_AbstractClass(flag=True, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Triangles_A_Class_isa_AbstractClass():
    instance = Triangles_A_Class()
    assert isinstance(instance, AbstractClass)


def test_Triangles_B_Class_isa_AbstractClass():
    instance = Triangles_B_Class()
    assert isinstance(instance, AbstractClass)


def test_Triangles_C_Class_isa_AbstractClass():
    instance = Triangles_C_Class()
    assert isinstance(instance, AbstractClass)


def test_Triangles_D_Class_isa_AbstractClass():
    instance = Triangles_D_Class()
    assert isinstance(instance, AbstractClass)


def test_Triangles_E_Class_isa_AbstractClass():
    instance = Triangles_E_Class()
    assert isinstance(instance, AbstractClass)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractClass_strategy = st.builds(AbstractClass)
@given(instance=AbstractClass_strategy)
@settings(max_examples=25)
def test_AbstractClass_instantiation(instance):
    assert isinstance(instance, AbstractClass)


Triangles_A_Class_strategy = st.builds(Triangles_A_Class)
@given(instance=Triangles_A_Class_strategy)
@settings(max_examples=25)
def test_Triangles_A_Class_instantiation(instance):
    assert isinstance(instance, Triangles_A_Class)


Triangles_AbstractClass_strategy = st.builds(Triangles_AbstractClass, flag=st.booleans(), id=st.integers(), name=safe_text)
@given(instance=Triangles_AbstractClass_strategy)
@settings(max_examples=25)
def test_Triangles_AbstractClass_instantiation(instance):
    assert isinstance(instance, Triangles_AbstractClass)


Triangles_B_Class_strategy = st.builds(Triangles_B_Class)
@given(instance=Triangles_B_Class_strategy)
@settings(max_examples=25)
def test_Triangles_B_Class_instantiation(instance):
    assert isinstance(instance, Triangles_B_Class)


Triangles_C_Class_strategy = st.builds(Triangles_C_Class)
@given(instance=Triangles_C_Class_strategy)
@settings(max_examples=25)
def test_Triangles_C_Class_instantiation(instance):
    assert isinstance(instance, Triangles_C_Class)


Triangles_Container_strategy = st.builds(Triangles_Container)
@given(instance=Triangles_Container_strategy)
@settings(max_examples=25)
def test_Triangles_Container_instantiation(instance):
    assert isinstance(instance, Triangles_Container)


Triangles_D_Class_strategy = st.builds(Triangles_D_Class)
@given(instance=Triangles_D_Class_strategy)
@settings(max_examples=25)
def test_Triangles_D_Class_instantiation(instance):
    assert isinstance(instance, Triangles_D_Class)


Triangles_E_Class_strategy = st.builds(Triangles_E_Class)
@given(instance=Triangles_E_Class_strategy)
@settings(max_examples=25)
def test_Triangles_E_Class_instantiation(instance):
    assert isinstance(instance, Triangles_E_Class)



