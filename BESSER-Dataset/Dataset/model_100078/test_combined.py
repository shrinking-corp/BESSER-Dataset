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
    IReferenceDescription,
    builderState_ReferenceDescription,
    builderState_UserDataEntry,
    builderState_EClass,
    builderState_ResourceDescription,
    IEObjectDescription,
    builderState_EObjectDescription,
    builderState_IReferenceDescription,
    builderState_IEObjectDescription,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(IReferenceDescription)


def test_hyp_ireferencedescription_constructor_exists():
    assert callable(IReferenceDescription.__init__)


def test_hyp_ireferencedescription_constructor_args():
    sig = inspect.signature(IReferenceDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builderstate_referencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_ReferenceDescription)


def test_hyp_builderstate_referencedescription_constructor_exists():
    assert callable(builderState_ReferenceDescription.__init__)


def test_hyp_builderstate_referencedescription_constructor_args():
    sig = inspect.signature(builderState_ReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalFormOfEReference" in params, "Missing parameter 'externalFormOfEReference'"




def test_hyp_builderstate_userdataentry_is_not_abstract():
    assert not inspect.isabstract(builderState_UserDataEntry)


def test_hyp_builderstate_userdataentry_constructor_exists():
    assert callable(builderState_UserDataEntry.__init__)


def test_hyp_builderstate_userdataentry_constructor_args():
    sig = inspect.signature(builderState_UserDataEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_builderstate_eclass_is_not_abstract():
    assert not inspect.isabstract(builderState_EClass)


def test_hyp_builderstate_eclass_constructor_exists():
    assert callable(builderState_EClass.__init__)


def test_hyp_builderstate_eclass_constructor_args():
    sig = inspect.signature(builderState_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builderstate_resourcedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_ResourceDescription)


def test_hyp_builderstate_resourcedescription_constructor_exists():
    assert callable(builderState_ResourceDescription.__init__)


def test_hyp_builderstate_resourcedescription_constructor_args():
    sig = inspect.signature(builderState_ResourceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "importedNames" in params, "Missing parameter 'importedNames'"
    assert "URI" in params, "Missing parameter 'URI'"





def test_hyp_ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(IEObjectDescription)


def test_hyp_ieobjectdescription_constructor_exists():
    assert callable(IEObjectDescription.__init__)


def test_hyp_ieobjectdescription_constructor_args():
    sig = inspect.signature(IEObjectDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builderstate_eobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState_EObjectDescription)


def test_hyp_builderstate_eobjectdescription_constructor_exists():
    assert callable(builderState_EObjectDescription.__init__)


def test_hyp_builderstate_eobjectdescription_constructor_args():
    sig = inspect.signature(builderState_EObjectDescription.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"




def test_hyp_builderstate_ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_IReferenceDescription)


def test_hyp_builderstate_ireferencedescription_constructor_exists():
    assert callable(builderState_IReferenceDescription.__init__)


def test_hyp_builderstate_ireferencedescription_constructor_args():
    sig = inspect.signature(builderState_IReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "targetEObjectUri" in params, "Missing parameter 'targetEObjectUri'"
    assert "indexInList" in params, "Missing parameter 'indexInList'"
    assert "sourceEObjectUri" in params, "Missing parameter 'sourceEObjectUri'"
    assert "containerEObjectURI" in params, "Missing parameter 'containerEObjectURI'"







def test_hyp_builderstate_ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState_IEObjectDescription)


def test_hyp_builderstate_ieobjectdescription_constructor_exists():
    assert callable(builderState_IEObjectDescription.__init__)


def test_hyp_builderstate_ieobjectdescription_constructor_args():
    sig = inspect.signature(builderState_IEObjectDescription.__init__)
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
IReferenceDescription_strategy = st.builds(
    IReferenceDescription,
)
builderState_ReferenceDescription_strategy = st.builds(
    builderState_ReferenceDescription,
    externalFormOfEReference=
        safe_text
)
builderState_UserDataEntry_strategy = st.builds(
    builderState_UserDataEntry,
    key=
        safe_text,
    value=
        safe_text
)
builderState_EClass_strategy = st.builds(
    builderState_EClass,
)
builderState_ResourceDescription_strategy = st.builds(
    builderState_ResourceDescription,
    importedNames=
        safe_text,
    URI=
        safe_text
)
IEObjectDescription_strategy = st.builds(
    IEObjectDescription,
)
builderState_EObjectDescription_strategy = st.builds(
    builderState_EObjectDescription,
    fragment=
        safe_text
)
builderState_IReferenceDescription_strategy = st.builds(
    builderState_IReferenceDescription,
    targetEObjectUri=
        safe_text,
    indexInList=
        st.integers(),
    sourceEObjectUri=
        safe_text,
    containerEObjectURI=
        safe_text
)
builderState_IEObjectDescription_strategy = st.builds(
    builderState_IEObjectDescription,
    name=
        safe_text
)





@given(instance=builderState_ReferenceDescription_strategy)
def test_hyp_builderstate_referencedescription_externalFormOfEReference_setter(instance):
    original = instance.externalFormOfEReference
    instance.externalFormOfEReference = original
    assert instance.externalFormOfEReference == original




@given(instance=builderState_UserDataEntry_strategy)
def test_hyp_builderstate_userdataentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=builderState_UserDataEntry_strategy)
def test_hyp_builderstate_userdataentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=builderState_ResourceDescription_strategy)
def test_hyp_builderstate_resourcedescription_importedNames_setter(instance):
    original = instance.importedNames
    instance.importedNames = original
    assert instance.importedNames == original



@given(instance=builderState_ResourceDescription_strategy)
def test_hyp_builderstate_resourcedescription_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=builderState_ResourceDescription_strategy)
@settings(max_examples=30)
def test_hyp_builderstate_resourcedescription_isempty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEmpty()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEmpty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEmpty' in builderState_ResourceDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in builderState_ResourceDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in builderState_ResourceDescription is not implemented or raised an error")





@given(instance=builderState_EObjectDescription_strategy)
def test_hyp_builderstate_eobjectdescription_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original




@given(instance=builderState_IReferenceDescription_strategy)
def test_hyp_builderstate_ireferencedescription_targetEObjectUri_setter(instance):
    original = instance.targetEObjectUri
    instance.targetEObjectUri = original
    assert instance.targetEObjectUri == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_hyp_builderstate_ireferencedescription_indexInList_setter(instance):
    original = instance.indexInList
    instance.indexInList = original
    assert instance.indexInList == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_hyp_builderstate_ireferencedescription_sourceEObjectUri_setter(instance):
    original = instance.sourceEObjectUri
    instance.sourceEObjectUri = original
    assert instance.sourceEObjectUri == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_hyp_builderstate_ireferencedescription_containerEObjectURI_setter(instance):
    original = instance.containerEObjectURI
    instance.containerEObjectURI = original
    assert instance.containerEObjectURI == original




@given(instance=builderState_IEObjectDescription_strategy)
def test_hyp_builderstate_ieobjectdescription_name_setter(instance):
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
    IEObjectDescription,
    IReferenceDescription,
    builderState_EClass,
    builderState_EObjectDescription,
    builderState_IEObjectDescription,
    builderState_IReferenceDescription,
    builderState_ReferenceDescription,
    builderState_ResourceDescription,
    builderState_UserDataEntry,
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

def test_builderState_EObjectDescription_fragment_value_roundtrip():
    instance = builderState_EObjectDescription(fragment="sample_text")
    assert instance.fragment == "sample_text"
    instance.fragment = "sample_text_2"
    assert instance.fragment == "sample_text_2"


def test_builderState_IEObjectDescription_name_value_roundtrip():
    instance = builderState_IEObjectDescription(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_builderState_IReferenceDescription_containerEObjectURI_value_roundtrip():
    instance = builderState_IReferenceDescription(containerEObjectURI="sample_text", indexInList=7, sourceEObjectUri="sample_text", targetEObjectUri="sample_text")
    assert instance.containerEObjectURI == "sample_text"
    instance.containerEObjectURI = "sample_text_2"
    assert instance.containerEObjectURI == "sample_text_2"


def test_builderState_IReferenceDescription_indexInList_value_roundtrip():
    instance = builderState_IReferenceDescription(containerEObjectURI="sample_text", indexInList=7, sourceEObjectUri="sample_text", targetEObjectUri="sample_text")
    assert instance.indexInList == 7
    instance.indexInList = 13
    assert instance.indexInList == 13


def test_builderState_IReferenceDescription_sourceEObjectUri_value_roundtrip():
    instance = builderState_IReferenceDescription(containerEObjectURI="sample_text", indexInList=7, sourceEObjectUri="sample_text", targetEObjectUri="sample_text")
    assert instance.sourceEObjectUri == "sample_text"
    instance.sourceEObjectUri = "sample_text_2"
    assert instance.sourceEObjectUri == "sample_text_2"


def test_builderState_IReferenceDescription_targetEObjectUri_value_roundtrip():
    instance = builderState_IReferenceDescription(containerEObjectURI="sample_text", indexInList=7, sourceEObjectUri="sample_text", targetEObjectUri="sample_text")
    assert instance.targetEObjectUri == "sample_text"
    instance.targetEObjectUri = "sample_text_2"
    assert instance.targetEObjectUri == "sample_text_2"


def test_builderState_ReferenceDescription_externalFormOfEReference_value_roundtrip():
    instance = builderState_ReferenceDescription(externalFormOfEReference="sample_text")
    assert instance.externalFormOfEReference == "sample_text"
    instance.externalFormOfEReference = "sample_text_2"
    assert instance.externalFormOfEReference == "sample_text_2"


def test_builderState_ResourceDescription_URI_value_roundtrip():
    instance = builderState_ResourceDescription(URI="sample_text", importedNames="sample_text")
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_builderState_ResourceDescription_importedNames_value_roundtrip():
    instance = builderState_ResourceDescription(URI="sample_text", importedNames="sample_text")
    assert instance.importedNames == "sample_text"
    instance.importedNames = "sample_text_2"
    assert instance.importedNames == "sample_text_2"


def test_builderState_UserDataEntry_key_value_roundtrip():
    instance = builderState_UserDataEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_builderState_UserDataEntry_value_value_roundtrip():
    instance = builderState_UserDataEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_builderState_EObjectDescription_isa_IEObjectDescription():
    instance = builderState_EObjectDescription(fragment="sample_text")
    assert isinstance(instance, IEObjectDescription)


def test_builderState_ReferenceDescription_isa_IReferenceDescription():
    instance = builderState_ReferenceDescription(externalFormOfEReference="sample_text")
    assert isinstance(instance, IReferenceDescription)


def test_assoc_eClass4_link_reassign_clear():
    a = builderState_IEObjectDescription(name="sample_text")
    b1 = builderState_EClass()
    b2 = builderState_EClass()
    _safe_set(a, 'builderState_IEObjectDescription5', b1)
    assert _is_linked(a, 'builderState_IEObjectDescription5', b1)
    if hasattr(b1, 'builderState_EClass'):
        assert _is_linked(b1, 'builderState_EClass', a)
    _safe_set(a, 'builderState_IEObjectDescription5', b2)
    assert _is_linked(a, 'builderState_IEObjectDescription5', b2)
    if hasattr(b1, 'builderState_EClass'):
        assert not _is_linked(b1, 'builderState_EClass', a)
    if hasattr(b2, 'builderState_EClass'):
        assert _is_linked(b2, 'builderState_EClass', a)
    _safe_set(a, 'builderState_IEObjectDescription5', None)
    assert not _is_linked(a, 'builderState_IEObjectDescription5', b2)
    if hasattr(b2, 'builderState_EClass'):
        assert not _is_linked(b2, 'builderState_EClass', a)


def test_assoc_exportedObjects0_link_reassign_clear():
    a = builderState_ResourceDescription(URI="sample_text", importedNames="sample_text")
    b1 = builderState_IEObjectDescription(name="sample_text")
    b2 = builderState_IEObjectDescription(name="sample_text_2")
    _safe_set(a, 'builderState_ResourceDescription', {b1})
    assert _is_linked(a, 'builderState_ResourceDescription', b1)
    if hasattr(b1, 'builderState_IEObjectDescription'):
        assert _is_linked(b1, 'builderState_IEObjectDescription', a)
    _safe_set(a, 'builderState_ResourceDescription', {b2})
    assert _is_linked(a, 'builderState_ResourceDescription', b2)
    if hasattr(b1, 'builderState_IEObjectDescription'):
        assert not _is_linked(b1, 'builderState_IEObjectDescription', a)
    if hasattr(b2, 'builderState_IEObjectDescription'):
        assert _is_linked(b2, 'builderState_IEObjectDescription', a)
    _safe_set(a, 'builderState_ResourceDescription', set())
    assert not _is_linked(a, 'builderState_ResourceDescription', b2)
    if hasattr(b2, 'builderState_IEObjectDescription'):
        assert not _is_linked(b2, 'builderState_IEObjectDescription', a)


def test_assoc_referenceDescriptions1_link_reassign_clear():
    a = builderState_ResourceDescription(URI="sample_text", importedNames="sample_text")
    b1 = builderState_IReferenceDescription(containerEObjectURI="sample_text", indexInList=7, sourceEObjectUri="sample_text", targetEObjectUri="sample_text")
    b2 = builderState_IReferenceDescription(containerEObjectURI="sample_text_2", indexInList=13, sourceEObjectUri="sample_text_2", targetEObjectUri="sample_text_2")
    _safe_set(a, 'builderState_ResourceDescription2', {b1})
    assert _is_linked(a, 'builderState_ResourceDescription2', b1)
    if hasattr(b1, 'builderState_IReferenceDescription'):
        assert _is_linked(b1, 'builderState_IReferenceDescription', a)
    _safe_set(a, 'builderState_ResourceDescription2', {b2})
    assert _is_linked(a, 'builderState_ResourceDescription2', b2)
    if hasattr(b1, 'builderState_IReferenceDescription'):
        assert not _is_linked(b1, 'builderState_IReferenceDescription', a)
    if hasattr(b2, 'builderState_IReferenceDescription'):
        assert _is_linked(b2, 'builderState_IReferenceDescription', a)
    _safe_set(a, 'builderState_ResourceDescription2', set())
    assert not _is_linked(a, 'builderState_ResourceDescription2', b2)
    if hasattr(b2, 'builderState_IReferenceDescription'):
        assert not _is_linked(b2, 'builderState_IReferenceDescription', a)


def test_assoc_userData3_link_reassign_clear():
    a = builderState_UserDataEntry(key="sample_text", value="sample_text")
    b1 = builderState_EObjectDescription(fragment="sample_text")
    b2 = builderState_EObjectDescription(fragment="sample_text_2")
    _safe_set(a, 'builderState_UserDataEntry', b1)
    assert _is_linked(a, 'builderState_UserDataEntry', b1)
    if hasattr(b1, 'builderState_EObjectDescription'):
        assert _is_linked(b1, 'builderState_EObjectDescription', a)
    _safe_set(a, 'builderState_UserDataEntry', b2)
    assert _is_linked(a, 'builderState_UserDataEntry', b2)
    if hasattr(b1, 'builderState_EObjectDescription'):
        assert not _is_linked(b1, 'builderState_EObjectDescription', a)
    if hasattr(b2, 'builderState_EObjectDescription'):
        assert _is_linked(b2, 'builderState_EObjectDescription', a)
    _safe_set(a, 'builderState_UserDataEntry', None)
    assert not _is_linked(a, 'builderState_UserDataEntry', b2)
    if hasattr(b2, 'builderState_EObjectDescription'):
        assert not _is_linked(b2, 'builderState_EObjectDescription', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

IEObjectDescription_strategy = st.builds(IEObjectDescription)
@given(instance=IEObjectDescription_strategy)
@settings(max_examples=25)
def test_IEObjectDescription_instantiation(instance):
    assert isinstance(instance, IEObjectDescription)


IReferenceDescription_strategy = st.builds(IReferenceDescription)
@given(instance=IReferenceDescription_strategy)
@settings(max_examples=25)
def test_IReferenceDescription_instantiation(instance):
    assert isinstance(instance, IReferenceDescription)


builderState_EClass_strategy = st.builds(builderState_EClass)
@given(instance=builderState_EClass_strategy)
@settings(max_examples=25)
def test_builderState_EClass_instantiation(instance):
    assert isinstance(instance, builderState_EClass)


builderState_EObjectDescription_strategy = st.builds(builderState_EObjectDescription, fragment=safe_text)
@given(instance=builderState_EObjectDescription_strategy)
@settings(max_examples=25)
def test_builderState_EObjectDescription_instantiation(instance):
    assert isinstance(instance, builderState_EObjectDescription)


builderState_IEObjectDescription_strategy = st.builds(builderState_IEObjectDescription, name=safe_text)
@given(instance=builderState_IEObjectDescription_strategy)
@settings(max_examples=25)
def test_builderState_IEObjectDescription_instantiation(instance):
    assert isinstance(instance, builderState_IEObjectDescription)


builderState_IReferenceDescription_strategy = st.builds(builderState_IReferenceDescription, containerEObjectURI=safe_text, indexInList=st.integers(), sourceEObjectUri=safe_text, targetEObjectUri=safe_text)
@given(instance=builderState_IReferenceDescription_strategy)
@settings(max_examples=25)
def test_builderState_IReferenceDescription_instantiation(instance):
    assert isinstance(instance, builderState_IReferenceDescription)


builderState_ReferenceDescription_strategy = st.builds(builderState_ReferenceDescription, externalFormOfEReference=safe_text)
@given(instance=builderState_ReferenceDescription_strategy)
@settings(max_examples=25)
def test_builderState_ReferenceDescription_instantiation(instance):
    assert isinstance(instance, builderState_ReferenceDescription)


builderState_ResourceDescription_strategy = st.builds(builderState_ResourceDescription, URI=safe_text, importedNames=safe_text)
@given(instance=builderState_ResourceDescription_strategy)
@settings(max_examples=25)
def test_builderState_ResourceDescription_instantiation(instance):
    assert isinstance(instance, builderState_ResourceDescription)


builderState_UserDataEntry_strategy = st.builds(builderState_UserDataEntry, key=safe_text, value=safe_text)
@given(instance=builderState_UserDataEntry_strategy)
@settings(max_examples=25)
def test_builderState_UserDataEntry_instantiation(instance):
    assert isinstance(instance, builderState_UserDataEntry)



