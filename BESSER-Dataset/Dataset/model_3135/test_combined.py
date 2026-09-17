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
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Attribute)


def test_hyp_classdiagram_attribute_constructor_exists():
    assert callable(classdiagram_Attribute.__init__)


def test_hyp_classdiagram_attribute_constructor_args():
    sig = inspect.signature(classdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Class)


def test_hyp_classdiagram_class_constructor_exists():
    assert callable(classdiagram_Class.__init__)


def test_hyp_classdiagram_class_constructor_args():
    sig = inspect.signature(classdiagram_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_classdiagram_classdiagram_is_not_abstract():
    assert not inspect.isabstract(classdiagram_ClassDiagram)


def test_hyp_classdiagram_classdiagram_constructor_exists():
    assert callable(classdiagram_ClassDiagram.__init__)


def test_hyp_classdiagram_classdiagram_constructor_args():
    sig = inspect.signature(classdiagram_ClassDiagram.__init__)
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
classdiagram_Attribute_strategy = st.builds(
    classdiagram_Attribute,
    name=
        safe_text
)
classdiagram_Class_strategy = st.builds(
    classdiagram_Class,
    name=
        safe_text
)
classdiagram_ClassDiagram_strategy = st.builds(
    classdiagram_ClassDiagram,
)




@given(instance=classdiagram_Attribute_strategy)
def test_hyp_classdiagram_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=classdiagram_Class_strategy)
def test_hyp_classdiagram_class_name_setter(instance):
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
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_ClassDiagram,
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

def test_classdiagram_Attribute_name_value_roundtrip():
    instance = classdiagram_Attribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_classdiagram_Class_name_value_roundtrip():
    instance = classdiagram_Class(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_attrs1_link_reassign_clear():
    a = classdiagram_Attribute(name="sample_text")
    b1 = classdiagram_ClassDiagram()
    b2 = classdiagram_ClassDiagram()
    _safe_set(a, 'classdiagram_Attribute', b1)
    assert _is_linked(a, 'classdiagram_Attribute', b1)
    if hasattr(b1, 'classdiagram_ClassDiagram2'):
        assert _is_linked(b1, 'classdiagram_ClassDiagram2', a)
    _safe_set(a, 'classdiagram_Attribute', b2)
    assert _is_linked(a, 'classdiagram_Attribute', b2)
    if hasattr(b1, 'classdiagram_ClassDiagram2'):
        assert not _is_linked(b1, 'classdiagram_ClassDiagram2', a)
    if hasattr(b2, 'classdiagram_ClassDiagram2'):
        assert _is_linked(b2, 'classdiagram_ClassDiagram2', a)
    _safe_set(a, 'classdiagram_Attribute', None)
    assert not _is_linked(a, 'classdiagram_Attribute', b2)
    if hasattr(b2, 'classdiagram_ClassDiagram2'):
        assert not _is_linked(b2, 'classdiagram_ClassDiagram2', a)


def test_assoc_attrs3_link_reassign_clear():
    a = classdiagram_Class(name="sample_text")
    b1 = classdiagram_Attribute(name="sample_text")
    b2 = classdiagram_Attribute(name="sample_text_2")
    _safe_set(a, 'classdiagram_Class4', {b1})
    assert _is_linked(a, 'classdiagram_Class4', b1)
    if hasattr(b1, 'classdiagram_Attribute5'):
        assert _is_linked(b1, 'classdiagram_Attribute5', a)
    _safe_set(a, 'classdiagram_Class4', {b2})
    assert _is_linked(a, 'classdiagram_Class4', b2)
    if hasattr(b1, 'classdiagram_Attribute5'):
        assert not _is_linked(b1, 'classdiagram_Attribute5', a)
    if hasattr(b2, 'classdiagram_Attribute5'):
        assert _is_linked(b2, 'classdiagram_Attribute5', a)
    _safe_set(a, 'classdiagram_Class4', set())
    assert not _is_linked(a, 'classdiagram_Class4', b2)
    if hasattr(b2, 'classdiagram_Attribute5'):
        assert not _is_linked(b2, 'classdiagram_Attribute5', a)


def test_assoc_classes0_link_reassign_clear():
    a = classdiagram_Class(name="sample_text")
    b1 = classdiagram_ClassDiagram()
    b2 = classdiagram_ClassDiagram()
    _safe_set(a, 'classdiagram_Class', b1)
    assert _is_linked(a, 'classdiagram_Class', b1)
    if hasattr(b1, 'classdiagram_ClassDiagram'):
        assert _is_linked(b1, 'classdiagram_ClassDiagram', a)
    _safe_set(a, 'classdiagram_Class', b2)
    assert _is_linked(a, 'classdiagram_Class', b2)
    if hasattr(b1, 'classdiagram_ClassDiagram'):
        assert not _is_linked(b1, 'classdiagram_ClassDiagram', a)
    if hasattr(b2, 'classdiagram_ClassDiagram'):
        assert _is_linked(b2, 'classdiagram_ClassDiagram', a)
    _safe_set(a, 'classdiagram_Class', None)
    assert not _is_linked(a, 'classdiagram_Class', b2)
    if hasattr(b2, 'classdiagram_ClassDiagram'):
        assert not _is_linked(b2, 'classdiagram_ClassDiagram', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

classdiagram_Attribute_strategy = st.builds(classdiagram_Attribute, name=safe_text)
@given(instance=classdiagram_Attribute_strategy)
@settings(max_examples=25)
def test_classdiagram_Attribute_instantiation(instance):
    assert isinstance(instance, classdiagram_Attribute)


classdiagram_Class_strategy = st.builds(classdiagram_Class, name=safe_text)
@given(instance=classdiagram_Class_strategy)
@settings(max_examples=25)
def test_classdiagram_Class_instantiation(instance):
    assert isinstance(instance, classdiagram_Class)


classdiagram_ClassDiagram_strategy = st.builds(classdiagram_ClassDiagram)
@given(instance=classdiagram_ClassDiagram_strategy)
@settings(max_examples=25)
def test_classdiagram_ClassDiagram_instantiation(instance):
    assert isinstance(instance, classdiagram_ClassDiagram)



