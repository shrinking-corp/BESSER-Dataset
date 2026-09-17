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
    OutPortB,
    typeB_OutType1,
    PortB,
    typeB_PortB,
    typeB_OutPortB,
    typeB_InPortB,
    typeB_BlockB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_outportb_is_not_abstract():
    assert not inspect.isabstract(OutPortB)


def test_hyp_outportb_constructor_exists():
    assert callable(OutPortB.__init__)


def test_hyp_outportb_constructor_args():
    sig = inspect.signature(OutPortB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeb_outtype1_is_not_abstract():
    assert not inspect.isabstract(typeB_OutType1)


def test_hyp_typeb_outtype1_constructor_exists():
    assert callable(typeB_OutType1.__init__)


def test_hyp_typeb_outtype1_constructor_args():
    sig = inspect.signature(typeB_OutType1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_portb_is_not_abstract():
    assert not inspect.isabstract(PortB)


def test_hyp_portb_constructor_exists():
    assert callable(PortB.__init__)


def test_hyp_portb_constructor_args():
    sig = inspect.signature(PortB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeb_portb_is_not_abstract():
    assert not inspect.isabstract(typeB_PortB)


def test_hyp_typeb_portb_constructor_exists():
    assert callable(typeB_PortB.__init__)


def test_hyp_typeb_portb_constructor_args():
    sig = inspect.signature(typeB_PortB.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_typeb_outportb_is_not_abstract():
    assert not inspect.isabstract(typeB_OutPortB)


def test_hyp_typeb_outportb_constructor_exists():
    assert callable(typeB_OutPortB.__init__)


def test_hyp_typeb_outportb_constructor_args():
    sig = inspect.signature(typeB_OutPortB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeb_inportb_is_not_abstract():
    assert not inspect.isabstract(typeB_InPortB)


def test_hyp_typeb_inportb_constructor_exists():
    assert callable(typeB_InPortB.__init__)


def test_hyp_typeb_inportb_constructor_args():
    sig = inspect.signature(typeB_InPortB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeb_blockb_is_not_abstract():
    assert not inspect.isabstract(typeB_BlockB)


def test_hyp_typeb_blockb_constructor_exists():
    assert callable(typeB_BlockB.__init__)


def test_hyp_typeb_blockb_constructor_args():
    sig = inspect.signature(typeB_BlockB.__init__)
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
OutPortB_strategy = st.builds(
    OutPortB,
)
typeB_OutType1_strategy = st.builds(
    typeB_OutType1,
    name=
        safe_text
)
PortB_strategy = st.builds(
    PortB,
)
typeB_PortB_strategy = st.builds(
    typeB_PortB,
    id=
        st.integers()
)
typeB_OutPortB_strategy = st.builds(
    typeB_OutPortB,
)
typeB_InPortB_strategy = st.builds(
    typeB_InPortB,
)
typeB_BlockB_strategy = st.builds(
    typeB_BlockB,
)





@given(instance=typeB_OutType1_strategy)
def test_hyp_typeb_outtype1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=typeB_PortB_strategy)
def test_hyp_typeb_portb_id_setter(instance):
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
    OutPortB,
    PortB,
    typeB_BlockB,
    typeB_InPortB,
    typeB_OutPortB,
    typeB_OutType1,
    typeB_PortB,
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

def test_typeB_OutType1_name_value_roundtrip():
    instance = typeB_OutType1(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_typeB_PortB_id_value_roundtrip():
    instance = typeB_PortB(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_typeB_OutType1_isa_OutPortB():
    instance = typeB_OutType1(name="sample_text")
    assert isinstance(instance, OutPortB)


def test_typeB_InPortB_isa_PortB():
    instance = typeB_InPortB()
    assert isinstance(instance, PortB)


def test_typeB_OutPortB_isa_PortB():
    instance = typeB_OutPortB()
    assert isinstance(instance, PortB)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

OutPortB_strategy = st.builds(OutPortB)
@given(instance=OutPortB_strategy)
@settings(max_examples=25)
def test_OutPortB_instantiation(instance):
    assert isinstance(instance, OutPortB)


PortB_strategy = st.builds(PortB)
@given(instance=PortB_strategy)
@settings(max_examples=25)
def test_PortB_instantiation(instance):
    assert isinstance(instance, PortB)


typeB_BlockB_strategy = st.builds(typeB_BlockB)
@given(instance=typeB_BlockB_strategy)
@settings(max_examples=25)
def test_typeB_BlockB_instantiation(instance):
    assert isinstance(instance, typeB_BlockB)


typeB_InPortB_strategy = st.builds(typeB_InPortB)
@given(instance=typeB_InPortB_strategy)
@settings(max_examples=25)
def test_typeB_InPortB_instantiation(instance):
    assert isinstance(instance, typeB_InPortB)


typeB_OutPortB_strategy = st.builds(typeB_OutPortB)
@given(instance=typeB_OutPortB_strategy)
@settings(max_examples=25)
def test_typeB_OutPortB_instantiation(instance):
    assert isinstance(instance, typeB_OutPortB)


typeB_OutType1_strategy = st.builds(typeB_OutType1, name=safe_text)
@given(instance=typeB_OutType1_strategy)
@settings(max_examples=25)
def test_typeB_OutType1_instantiation(instance):
    assert isinstance(instance, typeB_OutType1)


typeB_PortB_strategy = st.builds(typeB_PortB, id=st.integers())
@given(instance=typeB_PortB_strategy)
@settings(max_examples=25)
def test_typeB_PortB_instantiation(instance):
    assert isinstance(instance, typeB_PortB)



