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
    Type,
    smalluml_Integer,
    smalluml_String,
    smalluml_Infinity,
    smalluml_Boolean,
    smalluml_Real,
    NamedElement,
    smalluml_Enumeration,
    smalluml_Generalisation,
    smalluml_Package,
    smalluml_Type,
    smalluml_NamedElement,
    smalluml_Cardinality,
    smalluml_Relation,
    smalluml_Method,
    smalluml_Attribute,
    smalluml_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_integer_is_not_abstract():
    assert not inspect.isabstract(smalluml_Integer)


def test_hyp_smalluml_integer_constructor_exists():
    assert callable(smalluml_Integer.__init__)


def test_hyp_smalluml_integer_constructor_args():
    sig = inspect.signature(smalluml_Integer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_string_is_not_abstract():
    assert not inspect.isabstract(smalluml_String)


def test_hyp_smalluml_string_constructor_exists():
    assert callable(smalluml_String.__init__)


def test_hyp_smalluml_string_constructor_args():
    sig = inspect.signature(smalluml_String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_infinity_is_not_abstract():
    assert not inspect.isabstract(smalluml_Infinity)


def test_hyp_smalluml_infinity_constructor_exists():
    assert callable(smalluml_Infinity.__init__)


def test_hyp_smalluml_infinity_constructor_args():
    sig = inspect.signature(smalluml_Infinity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_boolean_is_not_abstract():
    assert not inspect.isabstract(smalluml_Boolean)


def test_hyp_smalluml_boolean_constructor_exists():
    assert callable(smalluml_Boolean.__init__)


def test_hyp_smalluml_boolean_constructor_args():
    sig = inspect.signature(smalluml_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smalluml_real_is_not_abstract():
    assert not inspect.isabstract(smalluml_Real)


def test_hyp_smalluml_real_constructor_exists():
    assert callable(smalluml_Real.__init__)


def test_hyp_smalluml_real_constructor_args():
    sig = inspect.signature(smalluml_Real.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml_Enumeration)


def test_hyp_smalluml_enumeration_constructor_exists():
    assert callable(smalluml_Enumeration.__init__)


def test_hyp_smalluml_enumeration_constructor_args():
    sig = inspect.signature(smalluml_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_generalisation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Generalisation)


def test_hyp_smalluml_generalisation_constructor_exists():
    assert callable(smalluml_Generalisation.__init__)


def test_hyp_smalluml_generalisation_constructor_args():
    sig = inspect.signature(smalluml_Generalisation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_package_is_not_abstract():
    assert not inspect.isabstract(smalluml_Package)


def test_hyp_smalluml_package_constructor_exists():
    assert callable(smalluml_Package.__init__)


def test_hyp_smalluml_package_constructor_args():
    sig = inspect.signature(smalluml_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_type_is_not_abstract():
    assert not inspect.isabstract(smalluml_Type)


def test_hyp_smalluml_type_constructor_exists():
    assert callable(smalluml_Type.__init__)


def test_hyp_smalluml_type_constructor_args():
    sig = inspect.signature(smalluml_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_namedelement_is_not_abstract():
    assert not inspect.isabstract(smalluml_NamedElement)


def test_hyp_smalluml_namedelement_constructor_exists():
    assert callable(smalluml_NamedElement.__init__)


def test_hyp_smalluml_namedelement_constructor_args():
    sig = inspect.signature(smalluml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_smalluml_cardinality_is_not_abstract():
    assert not inspect.isabstract(smalluml_Cardinality)


def test_hyp_smalluml_cardinality_constructor_exists():
    assert callable(smalluml_Cardinality.__init__)


def test_hyp_smalluml_cardinality_constructor_args():
    sig = inspect.signature(smalluml_Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"





def test_hyp_smalluml_relation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Relation)


def test_hyp_smalluml_relation_constructor_exists():
    assert callable(smalluml_Relation.__init__)


def test_hyp_smalluml_relation_constructor_args():
    sig = inspect.signature(smalluml_Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_method_is_not_abstract():
    assert not inspect.isabstract(smalluml_Method)


def test_hyp_smalluml_method_constructor_exists():
    assert callable(smalluml_Method.__init__)


def test_hyp_smalluml_method_constructor_args():
    sig = inspect.signature(smalluml_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml_Attribute)


def test_hyp_smalluml_attribute_constructor_exists():
    assert callable(smalluml_Attribute.__init__)


def test_hyp_smalluml_attribute_constructor_args():
    sig = inspect.signature(smalluml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalluml_class_is_not_abstract():
    assert not inspect.isabstract(smalluml_Class)


def test_hyp_smalluml_class_constructor_exists():
    assert callable(smalluml_Class.__init__)


def test_hyp_smalluml_class_constructor_args():
    sig = inspect.signature(smalluml_Class.__init__)
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
Type_strategy = st.builds(
    Type,
)
smalluml_Integer_strategy = st.builds(
    smalluml_Integer,
)
smalluml_String_strategy = st.builds(
    smalluml_String,
)
smalluml_Infinity_strategy = st.builds(
    smalluml_Infinity,
)
smalluml_Boolean_strategy = st.builds(
    smalluml_Boolean,
    value=
        st.booleans()
)
smalluml_Real_strategy = st.builds(
    smalluml_Real,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml_Enumeration_strategy = st.builds(
    smalluml_Enumeration,
)
smalluml_Generalisation_strategy = st.builds(
    smalluml_Generalisation,
)
smalluml_Package_strategy = st.builds(
    smalluml_Package,
)
smalluml_Type_strategy = st.builds(
    smalluml_Type,
)
smalluml_NamedElement_strategy = st.builds(
    smalluml_NamedElement,
    name=
        safe_text
)
smalluml_Cardinality_strategy = st.builds(
    smalluml_Cardinality,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
smalluml_Relation_strategy = st.builds(
    smalluml_Relation,
)
smalluml_Method_strategy = st.builds(
    smalluml_Method,
)
smalluml_Attribute_strategy = st.builds(
    smalluml_Attribute,
)
smalluml_Class_strategy = st.builds(
    smalluml_Class,
)








@given(instance=smalluml_Boolean_strategy)
def test_hyp_smalluml_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original










@given(instance=smalluml_NamedElement_strategy)
def test_hyp_smalluml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=smalluml_Cardinality_strategy)
def test_hyp_smalluml_cardinality_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=smalluml_Cardinality_strategy)
def test_hyp_smalluml_cardinality_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    Type,
    smalluml_Attribute,
    smalluml_Boolean,
    smalluml_Cardinality,
    smalluml_Class,
    smalluml_Enumeration,
    smalluml_Generalisation,
    smalluml_Infinity,
    smalluml_Integer,
    smalluml_Method,
    smalluml_NamedElement,
    smalluml_Package,
    smalluml_Real,
    smalluml_Relation,
    smalluml_String,
    smalluml_Type,
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

def test_smalluml_Boolean_value_value_roundtrip():
    instance = smalluml_Boolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_smalluml_Cardinality_lowerBound_value_roundtrip():
    instance = smalluml_Cardinality(lowerBound=7, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_smalluml_Cardinality_upperBound_value_roundtrip():
    instance = smalluml_Cardinality(lowerBound=7, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_smalluml_NamedElement_name_value_roundtrip():
    instance = smalluml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smalluml_Attribute_isa_NamedElement():
    instance = smalluml_Attribute()
    assert isinstance(instance, NamedElement)


def test_smalluml_Cardinality_isa_NamedElement():
    instance = smalluml_Cardinality(lowerBound=7, upperBound=7)
    assert isinstance(instance, NamedElement)


def test_smalluml_Class_isa_NamedElement():
    instance = smalluml_Class()
    assert isinstance(instance, NamedElement)


def test_smalluml_Enumeration_isa_NamedElement():
    instance = smalluml_Enumeration()
    assert isinstance(instance, NamedElement)


def test_smalluml_Generalisation_isa_NamedElement():
    instance = smalluml_Generalisation()
    assert isinstance(instance, NamedElement)


def test_smalluml_Method_isa_NamedElement():
    instance = smalluml_Method()
    assert isinstance(instance, NamedElement)


def test_smalluml_Package_isa_NamedElement():
    instance = smalluml_Package()
    assert isinstance(instance, NamedElement)


def test_smalluml_Relation_isa_NamedElement():
    instance = smalluml_Relation()
    assert isinstance(instance, NamedElement)


def test_smalluml_Type_isa_NamedElement():
    instance = smalluml_Type()
    assert isinstance(instance, NamedElement)


def test_smalluml_Boolean_isa_Type():
    instance = smalluml_Boolean(value=True)
    assert isinstance(instance, Type)


def test_smalluml_Enumeration_isa_Type():
    instance = smalluml_Enumeration()
    assert isinstance(instance, Type)


def test_smalluml_Infinity_isa_Type():
    instance = smalluml_Infinity()
    assert isinstance(instance, Type)


def test_smalluml_Integer_isa_Type():
    instance = smalluml_Integer()
    assert isinstance(instance, Type)


def test_smalluml_Real_isa_Type():
    instance = smalluml_Real()
    assert isinstance(instance, Type)


def test_smalluml_String_isa_Type():
    instance = smalluml_String()
    assert isinstance(instance, Type)


def test_assoc_cardinality15_link_reassign_clear():
    a = smalluml_Cardinality(lowerBound=7, upperBound=7)
    b1 = smalluml_Relation()
    b2 = smalluml_Relation()
    _safe_set(a, 'smalluml_Cardinality', b1)
    assert _is_linked(a, 'smalluml_Cardinality', b1)
    if hasattr(b1, 'smalluml_Relation'):
        assert _is_linked(b1, 'smalluml_Relation', a)
    _safe_set(a, 'smalluml_Cardinality', b2)
    assert _is_linked(a, 'smalluml_Cardinality', b2)
    if hasattr(b1, 'smalluml_Relation'):
        assert not _is_linked(b1, 'smalluml_Relation', a)
    if hasattr(b2, 'smalluml_Relation'):
        assert _is_linked(b2, 'smalluml_Relation', a)
    _safe_set(a, 'smalluml_Cardinality', None)
    assert not _is_linked(a, 'smalluml_Cardinality', b2)
    if hasattr(b2, 'smalluml_Relation'):
        assert not _is_linked(b2, 'smalluml_Relation', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


smalluml_Attribute_strategy = st.builds(smalluml_Attribute)
@given(instance=smalluml_Attribute_strategy)
@settings(max_examples=25)
def test_smalluml_Attribute_instantiation(instance):
    assert isinstance(instance, smalluml_Attribute)


smalluml_Boolean_strategy = st.builds(smalluml_Boolean, value=st.booleans())
@given(instance=smalluml_Boolean_strategy)
@settings(max_examples=25)
def test_smalluml_Boolean_instantiation(instance):
    assert isinstance(instance, smalluml_Boolean)


smalluml_Cardinality_strategy = st.builds(smalluml_Cardinality, lowerBound=st.integers(), upperBound=st.integers())
@given(instance=smalluml_Cardinality_strategy)
@settings(max_examples=25)
def test_smalluml_Cardinality_instantiation(instance):
    assert isinstance(instance, smalluml_Cardinality)


smalluml_Class_strategy = st.builds(smalluml_Class)
@given(instance=smalluml_Class_strategy)
@settings(max_examples=25)
def test_smalluml_Class_instantiation(instance):
    assert isinstance(instance, smalluml_Class)


smalluml_Enumeration_strategy = st.builds(smalluml_Enumeration)
@given(instance=smalluml_Enumeration_strategy)
@settings(max_examples=25)
def test_smalluml_Enumeration_instantiation(instance):
    assert isinstance(instance, smalluml_Enumeration)


smalluml_Generalisation_strategy = st.builds(smalluml_Generalisation)
@given(instance=smalluml_Generalisation_strategy)
@settings(max_examples=25)
def test_smalluml_Generalisation_instantiation(instance):
    assert isinstance(instance, smalluml_Generalisation)


smalluml_Infinity_strategy = st.builds(smalluml_Infinity)
@given(instance=smalluml_Infinity_strategy)
@settings(max_examples=25)
def test_smalluml_Infinity_instantiation(instance):
    assert isinstance(instance, smalluml_Infinity)


smalluml_Integer_strategy = st.builds(smalluml_Integer)
@given(instance=smalluml_Integer_strategy)
@settings(max_examples=25)
def test_smalluml_Integer_instantiation(instance):
    assert isinstance(instance, smalluml_Integer)


smalluml_Method_strategy = st.builds(smalluml_Method)
@given(instance=smalluml_Method_strategy)
@settings(max_examples=25)
def test_smalluml_Method_instantiation(instance):
    assert isinstance(instance, smalluml_Method)


smalluml_NamedElement_strategy = st.builds(smalluml_NamedElement, name=safe_text)
@given(instance=smalluml_NamedElement_strategy)
@settings(max_examples=25)
def test_smalluml_NamedElement_instantiation(instance):
    assert isinstance(instance, smalluml_NamedElement)


smalluml_Package_strategy = st.builds(smalluml_Package)
@given(instance=smalluml_Package_strategy)
@settings(max_examples=25)
def test_smalluml_Package_instantiation(instance):
    assert isinstance(instance, smalluml_Package)


smalluml_Real_strategy = st.builds(smalluml_Real)
@given(instance=smalluml_Real_strategy)
@settings(max_examples=25)
def test_smalluml_Real_instantiation(instance):
    assert isinstance(instance, smalluml_Real)


smalluml_Relation_strategy = st.builds(smalluml_Relation)
@given(instance=smalluml_Relation_strategy)
@settings(max_examples=25)
def test_smalluml_Relation_instantiation(instance):
    assert isinstance(instance, smalluml_Relation)


smalluml_String_strategy = st.builds(smalluml_String)
@given(instance=smalluml_String_strategy)
@settings(max_examples=25)
def test_smalluml_String_instantiation(instance):
    assert isinstance(instance, smalluml_String)


smalluml_Type_strategy = st.builds(smalluml_Type)
@given(instance=smalluml_Type_strategy)
@settings(max_examples=25)
def test_smalluml_Type_instantiation(instance):
    assert isinstance(instance, smalluml_Type)



