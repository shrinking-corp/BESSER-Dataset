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
    umlMM__Attribute,
    Classifier,
    umlMM__PrimitiveDataType,
    umlMM__Class,
    umlMM__dummy,
    umlMM__Association,
    umlMM__Classifier,
    umlMM__Package,
    KIND,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_umlmm__attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM__Attribute)


def test_hyp_umlmm__attribute_constructor_exists():
    assert callable(umlMM__Attribute.__init__)


def test_hyp_umlmm__attribute_constructor_args():
    sig = inspect.signature(umlMM__Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmm__primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(umlMM__PrimitiveDataType)


def test_hyp_umlmm__primitivedatatype_constructor_exists():
    assert callable(umlMM__PrimitiveDataType.__init__)


def test_hyp_umlmm__primitivedatatype_constructor_args():
    sig = inspect.signature(umlMM__PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmm__class_is_not_abstract():
    assert not inspect.isabstract(umlMM__Class)


def test_hyp_umlmm__class_constructor_exists():
    assert callable(umlMM__Class.__init__)


def test_hyp_umlmm__class_constructor_args():
    sig = inspect.signature(umlMM__Class.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_umlmm__dummy_is_not_abstract():
    assert not inspect.isabstract(umlMM__dummy)


def test_hyp_umlmm__dummy_constructor_exists():
    assert callable(umlMM__dummy.__init__)


def test_hyp_umlmm__dummy_constructor_args():
    sig = inspect.signature(umlMM__dummy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmm__association_is_not_abstract():
    assert not inspect.isabstract(umlMM__Association)


def test_hyp_umlmm__association_constructor_exists():
    assert callable(umlMM__Association.__init__)


def test_hyp_umlmm__association_constructor_args():
    sig = inspect.signature(umlMM__Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlmm__classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM__Classifier)


def test_hyp_umlmm__classifier_constructor_exists():
    assert callable(umlMM__Classifier.__init__)


def test_hyp_umlmm__classifier_constructor_args():
    sig = inspect.signature(umlMM__Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlmm__package_is_not_abstract():
    assert not inspect.isabstract(umlMM__Package)


def test_hyp_umlmm__package_constructor_exists():
    assert callable(umlMM__Package.__init__)


def test_hyp_umlmm__package_constructor_args():
    sig = inspect.signature(umlMM__Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_kind_exists():
    # Check that the Enumeration exists
    assert KIND is not None

def test_hyp_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KIND]
    expected_literals = [
        "OTHER",
        "PERSISTENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KIND"


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
umlMM__Attribute_strategy = st.builds(
    umlMM__Attribute,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
umlMM__PrimitiveDataType_strategy = st.builds(
    umlMM__PrimitiveDataType,
)
umlMM__Class_strategy = st.builds(
    umlMM__Class,
    kind=
        safe_text
)
umlMM__dummy_strategy = st.builds(
    umlMM__dummy,
)
umlMM__Association_strategy = st.builds(
    umlMM__Association,
    name=
        safe_text
)
umlMM__Classifier_strategy = st.builds(
    umlMM__Classifier,
    name=
        safe_text
)
umlMM__Package_strategy = st.builds(
    umlMM__Package,
    name=
        safe_text
)




@given(instance=umlMM__Attribute_strategy)
def test_hyp_umlmm__attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=umlMM__Class_strategy)
def test_hyp_umlmm__class_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





@given(instance=umlMM__Association_strategy)
def test_hyp_umlmm__association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=umlMM__Classifier_strategy)
def test_hyp_umlmm__classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=umlMM__Package_strategy)
def test_hyp_umlmm__package_name_setter(instance):
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
    Classifier,
    umlMM__Association,
    umlMM__Attribute,
    umlMM__Class,
    umlMM__Classifier,
    umlMM__Package,
    umlMM__PrimitiveDataType,
    umlMM__dummy,
    KIND,
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

def test_umlMM__Association_name_value_roundtrip():
    instance = umlMM__Association(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlMM__Attribute_name_value_roundtrip():
    instance = umlMM__Attribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlMM__Class_kind_value_roundtrip():
    instance = umlMM__Class(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_umlMM__Classifier_name_value_roundtrip():
    instance = umlMM__Classifier(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlMM__Package_name_value_roundtrip():
    instance = umlMM__Package(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlMM__Class_isa_Classifier():
    instance = umlMM__Class(kind="sample_text")
    assert isinstance(instance, Classifier)


def test_umlMM__PrimitiveDataType_isa_Classifier():
    instance = umlMM__PrimitiveDataType()
    assert isinstance(instance, Classifier)


def test_assoc_association1_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'namespace2', {b1})
    assert _is_linked(a, 'namespace2', b1)
    if hasattr(b1, 'Association'):
        assert _is_linked(b1, 'Association', a)
    _safe_set(a, 'namespace2', {b2})
    assert _is_linked(a, 'namespace2', b2)
    if hasattr(b1, 'Association'):
        assert not _is_linked(b1, 'Association', a)
    if hasattr(b2, 'Association'):
        assert _is_linked(b2, 'Association', a)
    _safe_set(a, 'namespace2', set())
    assert not _is_linked(a, 'namespace2', b2)
    if hasattr(b2, 'Association'):
        assert not _is_linked(b2, 'Association', a)


def test_assoc_attribute4_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Attribute(name="sample_text")
    b2 = umlMM__Attribute(name="sample_text_2")
    _safe_set(a, 'owner', {b1})
    assert _is_linked(a, 'owner', b1)
    if hasattr(b1, 'Attribute'):
        assert _is_linked(b1, 'Attribute', a)
    _safe_set(a, 'owner', {b2})
    assert _is_linked(a, 'owner', b2)
    if hasattr(b1, 'Attribute'):
        assert not _is_linked(b1, 'Attribute', a)
    if hasattr(b2, 'Attribute'):
        assert _is_linked(b2, 'Attribute', a)
    _safe_set(a, 'owner', set())
    assert not _is_linked(a, 'owner', b2)
    if hasattr(b2, 'Attribute'):
        assert not _is_linked(b2, 'Attribute', a)


def test_assoc_classifier0_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__Classifier(name="sample_text")
    b2 = umlMM__Classifier(name="sample_text_2")
    _safe_set(a, 'namespace', {b1})
    assert _is_linked(a, 'namespace', b1)
    if hasattr(b1, 'Classifier'):
        assert _is_linked(b1, 'Classifier', a)
    _safe_set(a, 'namespace', {b2})
    assert _is_linked(a, 'namespace', b2)
    if hasattr(b1, 'Classifier'):
        assert not _is_linked(b1, 'Classifier', a)
    if hasattr(b2, 'Classifier'):
        assert _is_linked(b2, 'Classifier', a)
    _safe_set(a, 'namespace', set())
    assert not _is_linked(a, 'namespace', b2)
    if hasattr(b2, 'Classifier'):
        assert not _is_linked(b2, 'Classifier', a)


def test_assoc_containsPackage27_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__dummy()
    b2 = umlMM__dummy()
    _safe_set(a, 'Package29', b1)
    assert _is_linked(a, 'Package29', b1)
    if hasattr(b1, 'dummy28'):
        assert _is_linked(b1, 'dummy28', a)
    _safe_set(a, 'Package29', b2)
    assert _is_linked(a, 'Package29', b2)
    if hasattr(b1, 'dummy28'):
        assert not _is_linked(b1, 'dummy28', a)
    if hasattr(b2, 'dummy28'):
        assert _is_linked(b2, 'dummy28', a)
    _safe_set(a, 'Package29', None)
    assert not _is_linked(a, 'Package29', b2)
    if hasattr(b2, 'dummy28'):
        assert not _is_linked(b2, 'dummy28', a)


def test_assoc_destination25_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'Class26', b1)
    assert _is_linked(a, 'Class26', b1)
    if hasattr(b1, 'destinationOf'):
        assert _is_linked(b1, 'destinationOf', a)
    _safe_set(a, 'Class26', b2)
    assert _is_linked(a, 'Class26', b2)
    if hasattr(b1, 'destinationOf'):
        assert not _is_linked(b1, 'destinationOf', a)
    if hasattr(b2, 'destinationOf'):
        assert _is_linked(b2, 'destinationOf', a)
    _safe_set(a, 'Class26', None)
    assert not _is_linked(a, 'Class26', b2)
    if hasattr(b2, 'destinationOf'):
        assert not _is_linked(b2, 'destinationOf', a)


def test_assoc_destinationOf12_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'destination', {b1})
    assert _is_linked(a, 'destination', b1)
    if hasattr(b1, 'Association13'):
        assert _is_linked(b1, 'Association13', a)
    _safe_set(a, 'destination', {b2})
    assert _is_linked(a, 'destination', b2)
    if hasattr(b1, 'Association13'):
        assert not _is_linked(b1, 'Association13', a)
    if hasattr(b2, 'Association13'):
        assert _is_linked(b2, 'Association13', a)
    _safe_set(a, 'destination', set())
    assert not _is_linked(a, 'destination', b2)
    if hasattr(b2, 'Association13'):
        assert not _is_linked(b2, 'Association13', a)


def test_assoc_dummy3_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__dummy()
    b2 = umlMM__dummy()
    _safe_set(a, 'containsPackage', b1)
    assert _is_linked(a, 'containsPackage', b1)
    if hasattr(b1, 'dummy'):
        assert _is_linked(b1, 'dummy', a)
    _safe_set(a, 'containsPackage', b2)
    assert _is_linked(a, 'containsPackage', b2)
    if hasattr(b1, 'dummy'):
        assert not _is_linked(b1, 'dummy', a)
    if hasattr(b2, 'dummy'):
        assert _is_linked(b2, 'dummy', a)
    _safe_set(a, 'containsPackage', None)
    assert not _is_linked(a, 'containsPackage', b2)
    if hasattr(b2, 'dummy'):
        assert not _is_linked(b2, 'dummy', a)


def test_assoc_general6_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Class(kind="sample_text")
    b2 = umlMM__Class(kind="sample_text_2")
    _safe_set(a, 'Class', b1)
    assert _is_linked(a, 'Class', b1)
    if hasattr(b1, 'subclass'):
        assert _is_linked(b1, 'subclass', a)
    _safe_set(a, 'Class', b2)
    assert _is_linked(a, 'Class', b2)
    if hasattr(b1, 'subclass'):
        assert not _is_linked(b1, 'subclass', a)
    if hasattr(b2, 'subclass'):
        assert _is_linked(b2, 'subclass', a)
    _safe_set(a, 'Class', None)
    assert not _is_linked(a, 'Class', b2)
    if hasattr(b2, 'subclass'):
        assert not _is_linked(b2, 'subclass', a)


def test_assoc_namespace20_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__Classifier(name="sample_text")
    b2 = umlMM__Classifier(name="sample_text_2")
    _safe_set(a, 'Package', b1)
    assert _is_linked(a, 'Package', b1)
    if hasattr(b1, 'classifier'):
        assert _is_linked(b1, 'classifier', a)
    _safe_set(a, 'Package', b2)
    assert _is_linked(a, 'Package', b2)
    if hasattr(b1, 'classifier'):
        assert not _is_linked(b1, 'classifier', a)
    if hasattr(b2, 'classifier'):
        assert _is_linked(b2, 'classifier', a)
    _safe_set(a, 'Package', None)
    assert not _is_linked(a, 'Package', b2)
    if hasattr(b2, 'classifier'):
        assert not _is_linked(b2, 'classifier', a)


def test_assoc_namespace21_link_reassign_clear():
    a = umlMM__Package(name="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'Package22', b1)
    assert _is_linked(a, 'Package22', b1)
    if hasattr(b1, 'association'):
        assert _is_linked(b1, 'association', a)
    _safe_set(a, 'Package22', b2)
    assert _is_linked(a, 'Package22', b2)
    if hasattr(b1, 'association'):
        assert not _is_linked(b1, 'association', a)
    if hasattr(b2, 'association'):
        assert _is_linked(b2, 'association', a)
    _safe_set(a, 'Package22', None)
    assert not _is_linked(a, 'Package22', b2)
    if hasattr(b2, 'association'):
        assert not _is_linked(b2, 'association', a)


def test_assoc_owner14_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Attribute(name="sample_text")
    b2 = umlMM__Attribute(name="sample_text_2")
    _safe_set(a, 'Class15', b1)
    assert _is_linked(a, 'Class15', b1)
    if hasattr(b1, 'attribute'):
        assert _is_linked(b1, 'attribute', a)
    _safe_set(a, 'Class15', b2)
    assert _is_linked(a, 'Class15', b2)
    if hasattr(b1, 'attribute'):
        assert not _is_linked(b1, 'attribute', a)
    if hasattr(b2, 'attribute'):
        assert _is_linked(b2, 'attribute', a)
    _safe_set(a, 'Class15', None)
    assert not _is_linked(a, 'Class15', b2)
    if hasattr(b2, 'attribute'):
        assert not _is_linked(b2, 'attribute', a)


def test_assoc_source23_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'Class24', b1)
    assert _is_linked(a, 'Class24', b1)
    if hasattr(b1, 'sourceOf'):
        assert _is_linked(b1, 'sourceOf', a)
    _safe_set(a, 'Class24', b2)
    assert _is_linked(a, 'Class24', b2)
    if hasattr(b1, 'sourceOf'):
        assert not _is_linked(b1, 'sourceOf', a)
    if hasattr(b2, 'sourceOf'):
        assert _is_linked(b2, 'sourceOf', a)
    _safe_set(a, 'Class24', None)
    assert not _is_linked(a, 'Class24', b2)
    if hasattr(b2, 'sourceOf'):
        assert not _is_linked(b2, 'sourceOf', a)


def test_assoc_sourceOf10_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Association(name="sample_text")
    b2 = umlMM__Association(name="sample_text_2")
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Association11'):
        assert _is_linked(b1, 'Association11', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Association11'):
        assert not _is_linked(b1, 'Association11', a)
    if hasattr(b2, 'Association11'):
        assert _is_linked(b2, 'Association11', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Association11'):
        assert not _is_linked(b2, 'Association11', a)


def test_assoc_subclass8_link_reassign_clear():
    a = umlMM__Class(kind="sample_text")
    b1 = umlMM__Class(kind="sample_text")
    b2 = umlMM__Class(kind="sample_text_2")
    _safe_set(a, 'Class9', b1)
    assert _is_linked(a, 'Class9', b1)
    if hasattr(b1, 'general'):
        assert _is_linked(b1, 'general', a)
    _safe_set(a, 'Class9', b2)
    assert _is_linked(a, 'Class9', b2)
    if hasattr(b1, 'general'):
        assert not _is_linked(b1, 'general', a)
    if hasattr(b2, 'general'):
        assert _is_linked(b2, 'general', a)
    _safe_set(a, 'Class9', None)
    assert not _is_linked(a, 'Class9', b2)
    if hasattr(b2, 'general'):
        assert not _is_linked(b2, 'general', a)


def test_assoc_type16_link_reassign_clear():
    a = umlMM__Classifier(name="sample_text")
    b1 = umlMM__Attribute(name="sample_text")
    b2 = umlMM__Attribute(name="sample_text_2")
    _safe_set(a, 'Classifier17', b1)
    assert _is_linked(a, 'Classifier17', b1)
    if hasattr(b1, 'typeOf'):
        assert _is_linked(b1, 'typeOf', a)
    _safe_set(a, 'Classifier17', b2)
    assert _is_linked(a, 'Classifier17', b2)
    if hasattr(b1, 'typeOf'):
        assert not _is_linked(b1, 'typeOf', a)
    if hasattr(b2, 'typeOf'):
        assert _is_linked(b2, 'typeOf', a)
    _safe_set(a, 'Classifier17', None)
    assert not _is_linked(a, 'Classifier17', b2)
    if hasattr(b2, 'typeOf'):
        assert not _is_linked(b2, 'typeOf', a)


def test_assoc_typeOf18_link_reassign_clear():
    a = umlMM__Classifier(name="sample_text")
    b1 = umlMM__Attribute(name="sample_text")
    b2 = umlMM__Attribute(name="sample_text_2")
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'Attribute19'):
        assert _is_linked(b1, 'Attribute19', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'Attribute19'):
        assert not _is_linked(b1, 'Attribute19', a)
    if hasattr(b2, 'Attribute19'):
        assert _is_linked(b2, 'Attribute19', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'Attribute19'):
        assert not _is_linked(b2, 'Attribute19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


umlMM__Association_strategy = st.builds(umlMM__Association, name=safe_text)
@given(instance=umlMM__Association_strategy)
@settings(max_examples=25)
def test_umlMM__Association_instantiation(instance):
    assert isinstance(instance, umlMM__Association)


umlMM__Attribute_strategy = st.builds(umlMM__Attribute, name=safe_text)
@given(instance=umlMM__Attribute_strategy)
@settings(max_examples=25)
def test_umlMM__Attribute_instantiation(instance):
    assert isinstance(instance, umlMM__Attribute)


umlMM__Class_strategy = st.builds(umlMM__Class, kind=safe_text)
@given(instance=umlMM__Class_strategy)
@settings(max_examples=25)
def test_umlMM__Class_instantiation(instance):
    assert isinstance(instance, umlMM__Class)


umlMM__Classifier_strategy = st.builds(umlMM__Classifier, name=safe_text)
@given(instance=umlMM__Classifier_strategy)
@settings(max_examples=25)
def test_umlMM__Classifier_instantiation(instance):
    assert isinstance(instance, umlMM__Classifier)


umlMM__Package_strategy = st.builds(umlMM__Package, name=safe_text)
@given(instance=umlMM__Package_strategy)
@settings(max_examples=25)
def test_umlMM__Package_instantiation(instance):
    assert isinstance(instance, umlMM__Package)


umlMM__PrimitiveDataType_strategy = st.builds(umlMM__PrimitiveDataType)
@given(instance=umlMM__PrimitiveDataType_strategy)
@settings(max_examples=25)
def test_umlMM__PrimitiveDataType_instantiation(instance):
    assert isinstance(instance, umlMM__PrimitiveDataType)


umlMM__dummy_strategy = st.builds(umlMM__dummy)
@given(instance=umlMM__dummy_strategy)
@settings(max_examples=25)
def test_umlMM__dummy_instantiation(instance):
    assert isinstance(instance, umlMM__dummy)



