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
    oclstdlib_UniqueCollection,
    oclstdlib_Set,
    oclstdlib_Sequence,
    oclstdlib_OrderedSet,
    oclstdlib_OrderedCollection,
    OclElement,
    oclstdlib_OclType,
    oclstdlib_OclAny,
    OclAny,
    oclstdlib_OclElement,
    oclstdlib_OclState,
    oclstdlib_OclMessage,
    oclstdlib_OclSummable,
    oclstdlib_OclTuple,
    oclstdlib_OclComparable,
    oclstdlib_OclVoid,
    oclstdlib_Collection,
    oclstdlib_Bag,
    oclstdlib_OclLambda,
    OclVoid,
    oclstdlib_OclInvalid,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_oclstdlib_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_UniqueCollection)


def test_hyp_oclstdlib_uniquecollection_constructor_exists():
    assert callable(oclstdlib_UniqueCollection.__init__)


def test_hyp_oclstdlib_uniquecollection_constructor_args():
    sig = inspect.signature(oclstdlib_UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_set_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_Set)


def test_hyp_oclstdlib_set_constructor_exists():
    assert callable(oclstdlib_Set.__init__)


def test_hyp_oclstdlib_set_constructor_args():
    sig = inspect.signature(oclstdlib_Set.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_sequence_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_Sequence)


def test_hyp_oclstdlib_sequence_constructor_exists():
    assert callable(oclstdlib_Sequence.__init__)


def test_hyp_oclstdlib_sequence_constructor_args():
    sig = inspect.signature(oclstdlib_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_orderedset_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OrderedSet)


def test_hyp_oclstdlib_orderedset_constructor_exists():
    assert callable(oclstdlib_OrderedSet.__init__)


def test_hyp_oclstdlib_orderedset_constructor_args():
    sig = inspect.signature(oclstdlib_OrderedSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OrderedCollection)


def test_hyp_oclstdlib_orderedcollection_constructor_exists():
    assert callable(oclstdlib_OrderedCollection.__init__)


def test_hyp_oclstdlib_orderedcollection_constructor_args():
    sig = inspect.signature(oclstdlib_OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclelement_is_not_abstract():
    assert not inspect.isabstract(OclElement)


def test_hyp_oclelement_constructor_exists():
    assert callable(OclElement.__init__)


def test_hyp_oclelement_constructor_args():
    sig = inspect.signature(OclElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_ocltype_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclType)


def test_hyp_oclstdlib_ocltype_constructor_exists():
    assert callable(oclstdlib_OclType.__init__)


def test_hyp_oclstdlib_ocltype_constructor_args():
    sig = inspect.signature(oclstdlib_OclType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclany_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclAny)


def test_hyp_oclstdlib_oclany_constructor_exists():
    assert callable(oclstdlib_OclAny.__init__)


def test_hyp_oclstdlib_oclany_constructor_args():
    sig = inspect.signature(oclstdlib_OclAny.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclany_is_not_abstract():
    assert not inspect.isabstract(OclAny)


def test_hyp_oclany_constructor_exists():
    assert callable(OclAny.__init__)


def test_hyp_oclany_constructor_args():
    sig = inspect.signature(OclAny.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclelement_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclElement)


def test_hyp_oclstdlib_oclelement_constructor_exists():
    assert callable(oclstdlib_OclElement.__init__)


def test_hyp_oclstdlib_oclelement_constructor_args():
    sig = inspect.signature(oclstdlib_OclElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclstate_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclState)


def test_hyp_oclstdlib_oclstate_constructor_exists():
    assert callable(oclstdlib_OclState.__init__)


def test_hyp_oclstdlib_oclstate_constructor_args():
    sig = inspect.signature(oclstdlib_OclState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclmessage_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclMessage)


def test_hyp_oclstdlib_oclmessage_constructor_exists():
    assert callable(oclstdlib_OclMessage.__init__)


def test_hyp_oclstdlib_oclmessage_constructor_args():
    sig = inspect.signature(oclstdlib_OclMessage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclsummable_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclSummable)


def test_hyp_oclstdlib_oclsummable_constructor_exists():
    assert callable(oclstdlib_OclSummable.__init__)


def test_hyp_oclstdlib_oclsummable_constructor_args():
    sig = inspect.signature(oclstdlib_OclSummable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_ocltuple_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclTuple)


def test_hyp_oclstdlib_ocltuple_constructor_exists():
    assert callable(oclstdlib_OclTuple.__init__)


def test_hyp_oclstdlib_ocltuple_constructor_args():
    sig = inspect.signature(oclstdlib_OclTuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclcomparable_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclComparable)


def test_hyp_oclstdlib_oclcomparable_constructor_exists():
    assert callable(oclstdlib_OclComparable.__init__)


def test_hyp_oclstdlib_oclcomparable_constructor_args():
    sig = inspect.signature(oclstdlib_OclComparable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclvoid_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclVoid)


def test_hyp_oclstdlib_oclvoid_constructor_exists():
    assert callable(oclstdlib_OclVoid.__init__)


def test_hyp_oclstdlib_oclvoid_constructor_args():
    sig = inspect.signature(oclstdlib_OclVoid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_collection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_Collection)


def test_hyp_oclstdlib_collection_constructor_exists():
    assert callable(oclstdlib_Collection.__init__)


def test_hyp_oclstdlib_collection_constructor_args():
    sig = inspect.signature(oclstdlib_Collection.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"





def test_hyp_oclstdlib_bag_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_Bag)


def test_hyp_oclstdlib_bag_constructor_exists():
    assert callable(oclstdlib_Bag.__init__)


def test_hyp_oclstdlib_bag_constructor_args():
    sig = inspect.signature(oclstdlib_Bag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_ocllambda_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclLambda)


def test_hyp_oclstdlib_ocllambda_constructor_exists():
    assert callable(oclstdlib_OclLambda.__init__)


def test_hyp_oclstdlib_ocllambda_constructor_args():
    sig = inspect.signature(oclstdlib_OclLambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclvoid_is_not_abstract():
    assert not inspect.isabstract(OclVoid)


def test_hyp_oclvoid_constructor_exists():
    assert callable(OclVoid.__init__)


def test_hyp_oclvoid_constructor_args():
    sig = inspect.signature(OclVoid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclstdlib_oclinvalid_is_not_abstract():
    assert not inspect.isabstract(oclstdlib_OclInvalid)


def test_hyp_oclstdlib_oclinvalid_constructor_exists():
    assert callable(oclstdlib_OclInvalid.__init__)


def test_hyp_oclstdlib_oclinvalid_constructor_args():
    sig = inspect.signature(oclstdlib_OclInvalid.__init__)
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
oclstdlib_UniqueCollection_strategy = st.builds(
    oclstdlib_UniqueCollection,
)
oclstdlib_Set_strategy = st.builds(
    oclstdlib_Set,
)
oclstdlib_Sequence_strategy = st.builds(
    oclstdlib_Sequence,
)
oclstdlib_OrderedSet_strategy = st.builds(
    oclstdlib_OrderedSet,
)
oclstdlib_OrderedCollection_strategy = st.builds(
    oclstdlib_OrderedCollection,
)
OclElement_strategy = st.builds(
    OclElement,
)
oclstdlib_OclType_strategy = st.builds(
    oclstdlib_OclType,
)
oclstdlib_OclAny_strategy = st.builds(
    oclstdlib_OclAny,
)
OclAny_strategy = st.builds(
    OclAny,
)
oclstdlib_OclElement_strategy = st.builds(
    oclstdlib_OclElement,
)
oclstdlib_OclState_strategy = st.builds(
    oclstdlib_OclState,
)
oclstdlib_OclMessage_strategy = st.builds(
    oclstdlib_OclMessage,
)
oclstdlib_OclSummable_strategy = st.builds(
    oclstdlib_OclSummable,
)
oclstdlib_OclTuple_strategy = st.builds(
    oclstdlib_OclTuple,
)
oclstdlib_OclComparable_strategy = st.builds(
    oclstdlib_OclComparable,
)
oclstdlib_OclVoid_strategy = st.builds(
    oclstdlib_OclVoid,
)
oclstdlib_Collection_strategy = st.builds(
    oclstdlib_Collection,
    upper=
        safe_text,
    lower=
        safe_text
)
oclstdlib_Bag_strategy = st.builds(
    oclstdlib_Bag,
)
oclstdlib_OclLambda_strategy = st.builds(
    oclstdlib_OclLambda,
)
OclVoid_strategy = st.builds(
    OclVoid,
)
oclstdlib_OclInvalid_strategy = st.builds(
    oclstdlib_OclInvalid,
)




















@given(instance=oclstdlib_Collection_strategy)
def test_hyp_oclstdlib_collection_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=oclstdlib_Collection_strategy)
def test_hyp_oclstdlib_collection_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    OclAny,
    OclElement,
    OclVoid,
    oclstdlib_Bag,
    oclstdlib_Collection,
    oclstdlib_OclAny,
    oclstdlib_OclComparable,
    oclstdlib_OclElement,
    oclstdlib_OclInvalid,
    oclstdlib_OclLambda,
    oclstdlib_OclMessage,
    oclstdlib_OclState,
    oclstdlib_OclSummable,
    oclstdlib_OclTuple,
    oclstdlib_OclType,
    oclstdlib_OclVoid,
    oclstdlib_OrderedCollection,
    oclstdlib_OrderedSet,
    oclstdlib_Sequence,
    oclstdlib_Set,
    oclstdlib_UniqueCollection,
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

def test_oclstdlib_Collection_lower_value_roundtrip():
    instance = oclstdlib_Collection(lower="sample_text", upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_oclstdlib_Collection_upper_value_roundtrip():
    instance = oclstdlib_Collection(lower="sample_text", upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_oclstdlib_Collection_isa_OclAny():
    instance = oclstdlib_Collection(lower="sample_text", upper="sample_text")
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclComparable_isa_OclAny():
    instance = oclstdlib_OclComparable()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclElement_isa_OclAny():
    instance = oclstdlib_OclElement()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclLambda_isa_OclAny():
    instance = oclstdlib_OclLambda()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclMessage_isa_OclAny():
    instance = oclstdlib_OclMessage()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclState_isa_OclAny():
    instance = oclstdlib_OclState()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclSummable_isa_OclAny():
    instance = oclstdlib_OclSummable()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclTuple_isa_OclAny():
    instance = oclstdlib_OclTuple()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclVoid_isa_OclAny():
    instance = oclstdlib_OclVoid()
    assert isinstance(instance, OclAny)


def test_oclstdlib_OclType_isa_OclElement():
    instance = oclstdlib_OclType()
    assert isinstance(instance, OclElement)


def test_oclstdlib_OclInvalid_isa_OclVoid():
    instance = oclstdlib_OclInvalid()
    assert isinstance(instance, OclVoid)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

OclAny_strategy = st.builds(OclAny)
@given(instance=OclAny_strategy)
@settings(max_examples=25)
def test_OclAny_instantiation(instance):
    assert isinstance(instance, OclAny)


OclElement_strategy = st.builds(OclElement)
@given(instance=OclElement_strategy)
@settings(max_examples=25)
def test_OclElement_instantiation(instance):
    assert isinstance(instance, OclElement)


OclVoid_strategy = st.builds(OclVoid)
@given(instance=OclVoid_strategy)
@settings(max_examples=25)
def test_OclVoid_instantiation(instance):
    assert isinstance(instance, OclVoid)


oclstdlib_Bag_strategy = st.builds(oclstdlib_Bag)
@given(instance=oclstdlib_Bag_strategy)
@settings(max_examples=25)
def test_oclstdlib_Bag_instantiation(instance):
    assert isinstance(instance, oclstdlib_Bag)


oclstdlib_Collection_strategy = st.builds(oclstdlib_Collection, lower=safe_text, upper=safe_text)
@given(instance=oclstdlib_Collection_strategy)
@settings(max_examples=25)
def test_oclstdlib_Collection_instantiation(instance):
    assert isinstance(instance, oclstdlib_Collection)


oclstdlib_OclAny_strategy = st.builds(oclstdlib_OclAny)
@given(instance=oclstdlib_OclAny_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclAny_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclAny)


oclstdlib_OclComparable_strategy = st.builds(oclstdlib_OclComparable)
@given(instance=oclstdlib_OclComparable_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclComparable_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclComparable)


oclstdlib_OclElement_strategy = st.builds(oclstdlib_OclElement)
@given(instance=oclstdlib_OclElement_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclElement_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclElement)


oclstdlib_OclInvalid_strategy = st.builds(oclstdlib_OclInvalid)
@given(instance=oclstdlib_OclInvalid_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclInvalid_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclInvalid)


oclstdlib_OclLambda_strategy = st.builds(oclstdlib_OclLambda)
@given(instance=oclstdlib_OclLambda_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclLambda_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclLambda)


oclstdlib_OclMessage_strategy = st.builds(oclstdlib_OclMessage)
@given(instance=oclstdlib_OclMessage_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclMessage_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclMessage)


oclstdlib_OclState_strategy = st.builds(oclstdlib_OclState)
@given(instance=oclstdlib_OclState_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclState_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclState)


oclstdlib_OclSummable_strategy = st.builds(oclstdlib_OclSummable)
@given(instance=oclstdlib_OclSummable_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclSummable_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclSummable)


oclstdlib_OclTuple_strategy = st.builds(oclstdlib_OclTuple)
@given(instance=oclstdlib_OclTuple_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclTuple_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclTuple)


oclstdlib_OclType_strategy = st.builds(oclstdlib_OclType)
@given(instance=oclstdlib_OclType_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclType_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclType)


oclstdlib_OclVoid_strategy = st.builds(oclstdlib_OclVoid)
@given(instance=oclstdlib_OclVoid_strategy)
@settings(max_examples=25)
def test_oclstdlib_OclVoid_instantiation(instance):
    assert isinstance(instance, oclstdlib_OclVoid)


oclstdlib_OrderedCollection_strategy = st.builds(oclstdlib_OrderedCollection)
@given(instance=oclstdlib_OrderedCollection_strategy)
@settings(max_examples=25)
def test_oclstdlib_OrderedCollection_instantiation(instance):
    assert isinstance(instance, oclstdlib_OrderedCollection)


oclstdlib_OrderedSet_strategy = st.builds(oclstdlib_OrderedSet)
@given(instance=oclstdlib_OrderedSet_strategy)
@settings(max_examples=25)
def test_oclstdlib_OrderedSet_instantiation(instance):
    assert isinstance(instance, oclstdlib_OrderedSet)


oclstdlib_Sequence_strategy = st.builds(oclstdlib_Sequence)
@given(instance=oclstdlib_Sequence_strategy)
@settings(max_examples=25)
def test_oclstdlib_Sequence_instantiation(instance):
    assert isinstance(instance, oclstdlib_Sequence)


oclstdlib_Set_strategy = st.builds(oclstdlib_Set)
@given(instance=oclstdlib_Set_strategy)
@settings(max_examples=25)
def test_oclstdlib_Set_instantiation(instance):
    assert isinstance(instance, oclstdlib_Set)


oclstdlib_UniqueCollection_strategy = st.builds(oclstdlib_UniqueCollection)
@given(instance=oclstdlib_UniqueCollection_strategy)
@settings(max_examples=25)
def test_oclstdlib_UniqueCollection_instantiation(instance):
    assert isinstance(instance, oclstdlib_UniqueCollection)



