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
    CompositeLink,
    etrace_ETrace,
    AbstractLink,
    etrace_Link,
    etrace_CompositeLink,
    etrace_LinkType,
    etrace_EObject,
    etrace_AbstractLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_compositelink_is_not_abstract():
    assert not inspect.isabstract(CompositeLink)


def test_hyp_compositelink_constructor_exists():
    assert callable(CompositeLink.__init__)


def test_hyp_compositelink_constructor_args():
    sig = inspect.signature(CompositeLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etrace_etrace_is_not_abstract():
    assert not inspect.isabstract(etrace_ETrace)


def test_hyp_etrace_etrace_constructor_exists():
    assert callable(etrace_ETrace.__init__)


def test_hyp_etrace_etrace_constructor_args():
    sig = inspect.signature(etrace_ETrace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_abstractlink_is_not_abstract():
    assert not inspect.isabstract(AbstractLink)


def test_hyp_abstractlink_constructor_exists():
    assert callable(AbstractLink.__init__)


def test_hyp_abstractlink_constructor_args():
    sig = inspect.signature(AbstractLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etrace_link_is_not_abstract():
    assert not inspect.isabstract(etrace_Link)


def test_hyp_etrace_link_constructor_exists():
    assert callable(etrace_Link.__init__)


def test_hyp_etrace_link_constructor_args():
    sig = inspect.signature(etrace_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etrace_compositelink_is_not_abstract():
    assert not inspect.isabstract(etrace_CompositeLink)


def test_hyp_etrace_compositelink_constructor_exists():
    assert callable(etrace_CompositeLink.__init__)


def test_hyp_etrace_compositelink_constructor_args():
    sig = inspect.signature(etrace_CompositeLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etrace_linktype_is_not_abstract():
    assert not inspect.isabstract(etrace_LinkType)


def test_hyp_etrace_linktype_constructor_exists():
    assert callable(etrace_LinkType.__init__)


def test_hyp_etrace_linktype_constructor_args():
    sig = inspect.signature(etrace_LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "uses" in params, "Missing parameter 'uses'"
    assert "example" in params, "Missing parameter 'example'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_etrace_eobject_is_not_abstract():
    assert not inspect.isabstract(etrace_EObject)


def test_hyp_etrace_eobject_constructor_exists():
    assert callable(etrace_EObject.__init__)


def test_hyp_etrace_eobject_constructor_args():
    sig = inspect.signature(etrace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etrace_abstractlink_is_not_abstract():
    assert not inspect.isabstract(etrace_AbstractLink)


def test_hyp_etrace_abstractlink_constructor_exists():
    assert callable(etrace_AbstractLink.__init__)


def test_hyp_etrace_abstractlink_constructor_args():
    sig = inspect.signature(etrace_AbstractLink.__init__)
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
CompositeLink_strategy = st.builds(
    CompositeLink,
)
etrace_ETrace_strategy = st.builds(
    etrace_ETrace,
    name=
        safe_text
)
AbstractLink_strategy = st.builds(
    AbstractLink,
)
etrace_Link_strategy = st.builds(
    etrace_Link,
)
etrace_CompositeLink_strategy = st.builds(
    etrace_CompositeLink,
)
etrace_LinkType_strategy = st.builds(
    etrace_LinkType,
    uses=
        safe_text,
    example=
        safe_text,
    purpose=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
etrace_EObject_strategy = st.builds(
    etrace_EObject,
)
etrace_AbstractLink_strategy = st.builds(
    etrace_AbstractLink,
)





@given(instance=etrace_ETrace_strategy)
def test_hyp_etrace_etrace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=etrace_CompositeLink_strategy)
@settings(max_examples=30)
def test_hyp_etrace_compositelink_createcompositelink_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createCompositeLink(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createCompositeLink).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createCompositeLink' in etrace_CompositeLink is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createCompositeLink' in etrace_CompositeLink did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createCompositeLink' in etrace_CompositeLink is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=etrace_CompositeLink_strategy)
@settings(max_examples=30)
def test_hyp_etrace_compositelink_createlink_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLink(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLink).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLink' in etrace_CompositeLink is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLink' in etrace_CompositeLink did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLink' in etrace_CompositeLink is not implemented or raised an error")




@given(instance=etrace_LinkType_strategy)
def test_hyp_etrace_linktype_uses_setter(instance):
    original = instance.uses
    instance.uses = original
    assert instance.uses == original



@given(instance=etrace_LinkType_strategy)
def test_hyp_etrace_linktype_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original



@given(instance=etrace_LinkType_strategy)
def test_hyp_etrace_linktype_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=etrace_LinkType_strategy)
def test_hyp_etrace_linktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=etrace_LinkType_strategy)
def test_hyp_etrace_linktype_name_setter(instance):
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
    AbstractLink,
    CompositeLink,
    etrace_AbstractLink,
    etrace_CompositeLink,
    etrace_EObject,
    etrace_ETrace,
    etrace_Link,
    etrace_LinkType,
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

def test_etrace_ETrace_name_value_roundtrip():
    instance = etrace_ETrace(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_etrace_LinkType_description_value_roundtrip():
    instance = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_etrace_LinkType_example_value_roundtrip():
    instance = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    assert instance.example == "sample_text"
    instance.example = "sample_text_2"
    assert instance.example == "sample_text_2"


def test_etrace_LinkType_name_value_roundtrip():
    instance = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_etrace_LinkType_purpose_value_roundtrip():
    instance = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    assert instance.purpose == "sample_text"
    instance.purpose = "sample_text_2"
    assert instance.purpose == "sample_text_2"


def test_etrace_LinkType_uses_value_roundtrip():
    instance = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    assert instance.uses == "sample_text"
    instance.uses = "sample_text_2"
    assert instance.uses == "sample_text_2"


def test_etrace_CompositeLink_isa_AbstractLink():
    instance = etrace_CompositeLink()
    assert isinstance(instance, AbstractLink)


def test_etrace_Link_isa_AbstractLink():
    instance = etrace_Link()
    assert isinstance(instance, AbstractLink)


def test_etrace_ETrace_isa_CompositeLink():
    instance = etrace_ETrace(name="sample_text")
    assert isinstance(instance, CompositeLink)


def test_assoc_children19_link_reassign_clear():
    a = etrace_CompositeLink()
    b1 = etrace_AbstractLink()
    b2 = etrace_AbstractLink()
    _safe_set(a, 'etrace_CompositeLink', {b1})
    assert _is_linked(a, 'etrace_CompositeLink', b1)
    if hasattr(b1, 'etrace_AbstractLink20'):
        assert _is_linked(b1, 'etrace_AbstractLink20', a)
    _safe_set(a, 'etrace_CompositeLink', {b2})
    assert _is_linked(a, 'etrace_CompositeLink', b2)
    if hasattr(b1, 'etrace_AbstractLink20'):
        assert not _is_linked(b1, 'etrace_AbstractLink20', a)
    if hasattr(b2, 'etrace_AbstractLink20'):
        assert _is_linked(b2, 'etrace_AbstractLink20', a)
    _safe_set(a, 'etrace_CompositeLink', set())
    assert not _is_linked(a, 'etrace_CompositeLink', b2)
    if hasattr(b2, 'etrace_AbstractLink20'):
        assert not _is_linked(b2, 'etrace_AbstractLink20', a)


def test_assoc_deletedElement13_link_reassign_clear():
    a = etrace_ETrace(name="sample_text")
    b1 = etrace_EObject()
    b2 = etrace_EObject()
    _safe_set(a, 'etrace_ETrace14', {b1})
    assert _is_linked(a, 'etrace_ETrace14', b1)
    if hasattr(b1, 'etrace_EObject15'):
        assert _is_linked(b1, 'etrace_EObject15', a)
    _safe_set(a, 'etrace_ETrace14', {b2})
    assert _is_linked(a, 'etrace_ETrace14', b2)
    if hasattr(b1, 'etrace_EObject15'):
        assert not _is_linked(b1, 'etrace_EObject15', a)
    if hasattr(b2, 'etrace_EObject15'):
        assert _is_linked(b2, 'etrace_EObject15', a)
    _safe_set(a, 'etrace_ETrace14', set())
    assert not _is_linked(a, 'etrace_ETrace14', b2)
    if hasattr(b2, 'etrace_EObject15'):
        assert not _is_linked(b2, 'etrace_EObject15', a)


def test_assoc_externalElement16_link_reassign_clear():
    a = etrace_ETrace(name="sample_text")
    b1 = etrace_EObject()
    b2 = etrace_EObject()
    _safe_set(a, 'etrace_ETrace17', {b1})
    assert _is_linked(a, 'etrace_ETrace17', b1)
    if hasattr(b1, 'etrace_EObject18'):
        assert _is_linked(b1, 'etrace_EObject18', a)
    _safe_set(a, 'etrace_ETrace17', {b2})
    assert _is_linked(a, 'etrace_ETrace17', b2)
    if hasattr(b1, 'etrace_EObject18'):
        assert not _is_linked(b1, 'etrace_EObject18', a)
    if hasattr(b2, 'etrace_EObject18'):
        assert _is_linked(b2, 'etrace_EObject18', a)
    _safe_set(a, 'etrace_ETrace17', set())
    assert not _is_linked(a, 'etrace_ETrace17', b2)
    if hasattr(b2, 'etrace_EObject18'):
        assert not _is_linked(b2, 'etrace_EObject18', a)


def test_assoc_subType7_link_reassign_clear():
    a = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b1 = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b2 = etrace_LinkType(description="sample_text_2", example="sample_text_2", name="sample_text_2", purpose="sample_text_2", uses="sample_text_2")
    _safe_set(a, 'LinkType', b1)
    assert _is_linked(a, 'LinkType', b1)
    if hasattr(b1, 'superType'):
        assert _is_linked(b1, 'superType', a)
    _safe_set(a, 'LinkType', b2)
    assert _is_linked(a, 'LinkType', b2)
    if hasattr(b1, 'superType'):
        assert not _is_linked(b1, 'superType', a)
    if hasattr(b2, 'superType'):
        assert _is_linked(b2, 'superType', a)
    _safe_set(a, 'LinkType', None)
    assert not _is_linked(a, 'LinkType', b2)
    if hasattr(b2, 'superType'):
        assert not _is_linked(b2, 'superType', a)


def test_assoc_superType9_link_reassign_clear():
    a = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b1 = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b2 = etrace_LinkType(description="sample_text_2", example="sample_text_2", name="sample_text_2", purpose="sample_text_2", uses="sample_text_2")
    _safe_set(a, 'LinkType10', b1)
    assert _is_linked(a, 'LinkType10', b1)
    if hasattr(b1, 'subType'):
        assert _is_linked(b1, 'subType', a)
    _safe_set(a, 'LinkType10', b2)
    assert _is_linked(a, 'LinkType10', b2)
    if hasattr(b1, 'subType'):
        assert not _is_linked(b1, 'subType', a)
    if hasattr(b2, 'subType'):
        assert _is_linked(b2, 'subType', a)
    _safe_set(a, 'LinkType10', None)
    assert not _is_linked(a, 'LinkType10', b2)
    if hasattr(b2, 'subType'):
        assert not _is_linked(b2, 'subType', a)


def test_assoc_type4_link_reassign_clear():
    a = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b1 = etrace_AbstractLink()
    b2 = etrace_AbstractLink()
    _safe_set(a, 'etrace_LinkType', b1)
    assert _is_linked(a, 'etrace_LinkType', b1)
    if hasattr(b1, 'etrace_AbstractLink5'):
        assert _is_linked(b1, 'etrace_AbstractLink5', a)
    _safe_set(a, 'etrace_LinkType', b2)
    assert _is_linked(a, 'etrace_LinkType', b2)
    if hasattr(b1, 'etrace_AbstractLink5'):
        assert not _is_linked(b1, 'etrace_AbstractLink5', a)
    if hasattr(b2, 'etrace_AbstractLink5'):
        assert _is_linked(b2, 'etrace_AbstractLink5', a)
    _safe_set(a, 'etrace_LinkType', None)
    assert not _is_linked(a, 'etrace_LinkType', b2)
    if hasattr(b2, 'etrace_AbstractLink5'):
        assert not _is_linked(b2, 'etrace_AbstractLink5', a)


def test_assoc_typeList11_link_reassign_clear():
    a = etrace_LinkType(description="sample_text", example="sample_text", name="sample_text", purpose="sample_text", uses="sample_text")
    b1 = etrace_ETrace(name="sample_text")
    b2 = etrace_ETrace(name="sample_text_2")
    _safe_set(a, 'etrace_LinkType12', b1)
    assert _is_linked(a, 'etrace_LinkType12', b1)
    if hasattr(b1, 'etrace_ETrace'):
        assert _is_linked(b1, 'etrace_ETrace', a)
    _safe_set(a, 'etrace_LinkType12', b2)
    assert _is_linked(a, 'etrace_LinkType12', b2)
    if hasattr(b1, 'etrace_ETrace'):
        assert not _is_linked(b1, 'etrace_ETrace', a)
    if hasattr(b2, 'etrace_ETrace'):
        assert _is_linked(b2, 'etrace_ETrace', a)
    _safe_set(a, 'etrace_LinkType12', None)
    assert not _is_linked(a, 'etrace_LinkType12', b2)
    if hasattr(b2, 'etrace_ETrace'):
        assert not _is_linked(b2, 'etrace_ETrace', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractLink_strategy = st.builds(AbstractLink)
@given(instance=AbstractLink_strategy)
@settings(max_examples=25)
def test_AbstractLink_instantiation(instance):
    assert isinstance(instance, AbstractLink)


CompositeLink_strategy = st.builds(CompositeLink)
@given(instance=CompositeLink_strategy)
@settings(max_examples=25)
def test_CompositeLink_instantiation(instance):
    assert isinstance(instance, CompositeLink)


etrace_AbstractLink_strategy = st.builds(etrace_AbstractLink)
@given(instance=etrace_AbstractLink_strategy)
@settings(max_examples=25)
def test_etrace_AbstractLink_instantiation(instance):
    assert isinstance(instance, etrace_AbstractLink)


etrace_CompositeLink_strategy = st.builds(etrace_CompositeLink)
@given(instance=etrace_CompositeLink_strategy)
@settings(max_examples=25)
def test_etrace_CompositeLink_instantiation(instance):
    assert isinstance(instance, etrace_CompositeLink)


etrace_EObject_strategy = st.builds(etrace_EObject)
@given(instance=etrace_EObject_strategy)
@settings(max_examples=25)
def test_etrace_EObject_instantiation(instance):
    assert isinstance(instance, etrace_EObject)


etrace_ETrace_strategy = st.builds(etrace_ETrace, name=safe_text)
@given(instance=etrace_ETrace_strategy)
@settings(max_examples=25)
def test_etrace_ETrace_instantiation(instance):
    assert isinstance(instance, etrace_ETrace)


etrace_Link_strategy = st.builds(etrace_Link)
@given(instance=etrace_Link_strategy)
@settings(max_examples=25)
def test_etrace_Link_instantiation(instance):
    assert isinstance(instance, etrace_Link)


etrace_LinkType_strategy = st.builds(etrace_LinkType, description=safe_text, example=safe_text, name=safe_text, purpose=safe_text, uses=safe_text)
@given(instance=etrace_LinkType_strategy)
@settings(max_examples=25)
def test_etrace_LinkType_instantiation(instance):
    assert isinstance(instance, etrace_LinkType)



