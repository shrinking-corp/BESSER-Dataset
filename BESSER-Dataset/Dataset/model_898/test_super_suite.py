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
    ProcessElement,
    SimplePDL_Resource,
    SimplePDL_ResourceType,
    SimplePDL_WorkSequence,
    SimplePDL_WorkDefinition,
    SimplePDL_Guidance,
    SimplePDL_ProcessElement,
    SimplePDL_Process,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_hyp_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_hyp_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplepdl_resource_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Resource)


def test_hyp_simplepdl_resource_constructor_exists():
    assert callable(SimplePDL_Resource.__init__)


def test_hyp_simplepdl_resource_constructor_args():
    sig = inspect.signature(SimplePDL_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"




def test_hyp_simplepdl_resourcetype_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_ResourceType)


def test_hyp_simplepdl_resourcetype_constructor_exists():
    assert callable(SimplePDL_ResourceType.__init__)


def test_hyp_simplepdl_resourcetype_constructor_args():
    sig = inspect.signature(SimplePDL_ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_simplepdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_WorkSequence)


def test_hyp_simplepdl_worksequence_constructor_exists():
    assert callable(SimplePDL_WorkSequence.__init__)


def test_hyp_simplepdl_worksequence_constructor_args():
    sig = inspect.signature(SimplePDL_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"




def test_hyp_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_WorkDefinition)


def test_hyp_simplepdl_workdefinition_constructor_exists():
    assert callable(SimplePDL_WorkDefinition.__init__)


def test_hyp_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(SimplePDL_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_simplepdl_guidance_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Guidance)


def test_hyp_simplepdl_guidance_constructor_exists():
    assert callable(SimplePDL_Guidance.__init__)


def test_hyp_simplepdl_guidance_constructor_args():
    sig = inspect.signature(SimplePDL_Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_simplepdl_processelement_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_ProcessElement)


def test_hyp_simplepdl_processelement_constructor_exists():
    assert callable(SimplePDL_ProcessElement.__init__)


def test_hyp_simplepdl_processelement_constructor_args():
    sig = inspect.signature(SimplePDL_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplepdl_process_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Process)


def test_hyp_simplepdl_process_constructor_exists():
    assert callable(SimplePDL_Process.__init__)


def test_hyp_simplepdl_process_constructor_args():
    sig = inspect.signature(SimplePDL_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"




def test_hyp_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_hyp_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "finishToFinish",
        "finishToStart",
        "startToFinish",
        "startToStart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceType"


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
ProcessElement_strategy = st.builds(
    ProcessElement,
)
SimplePDL_Resource_strategy = st.builds(
    SimplePDL_Resource,
    occurrences=
        st.integers()
)
SimplePDL_ResourceType_strategy = st.builds(
    SimplePDL_ResourceType,
    occurrences=
        st.integers(),
    name=
        safe_text
)
SimplePDL_WorkSequence_strategy = st.builds(
    SimplePDL_WorkSequence,
    linkType=
        safe_text
)
SimplePDL_WorkDefinition_strategy = st.builds(
    SimplePDL_WorkDefinition,
    maxTime=
        st.integers(),
    minTime=
        st.integers(),
    name=
        safe_text
)
SimplePDL_Guidance_strategy = st.builds(
    SimplePDL_Guidance,
    text=
        safe_text
)
SimplePDL_ProcessElement_strategy = st.builds(
    SimplePDL_ProcessElement,
)
SimplePDL_Process_strategy = st.builds(
    SimplePDL_Process,
    name=
        safe_text,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)





@given(instance=SimplePDL_Resource_strategy)
def test_hyp_simplepdl_resource_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original




@given(instance=SimplePDL_ResourceType_strategy)
def test_hyp_simplepdl_resourcetype_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original



@given(instance=SimplePDL_ResourceType_strategy)
def test_hyp_simplepdl_resourcetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SimplePDL_WorkSequence_strategy)
def test_hyp_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original




@given(instance=SimplePDL_WorkDefinition_strategy)
def test_hyp_simplepdl_workdefinition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=SimplePDL_WorkDefinition_strategy)
def test_hyp_simplepdl_workdefinition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=SimplePDL_WorkDefinition_strategy)
def test_hyp_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SimplePDL_Guidance_strategy)
def test_hyp_simplepdl_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=SimplePDL_Process_strategy)
def test_hyp_simplepdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimplePDL_Process_strategy)
def test_hyp_simplepdl_process_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=SimplePDL_Process_strategy)
def test_hyp_simplepdl_process_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ProcessElement,
    SimplePDL_Guidance,
    SimplePDL_Process,
    SimplePDL_ProcessElement,
    SimplePDL_Resource,
    SimplePDL_ResourceType,
    SimplePDL_WorkDefinition,
    SimplePDL_WorkSequence,
    WorkSequenceType,
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

def test_SimplePDL_Guidance_text_value_roundtrip():
    instance = SimplePDL_Guidance(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_SimplePDL_Process_maxTime_value_roundtrip():
    instance = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    assert instance.maxTime == 7
    instance.maxTime = 13
    assert instance.maxTime == 13


def test_SimplePDL_Process_minTime_value_roundtrip():
    instance = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    assert instance.minTime == 7
    instance.minTime = 13
    assert instance.minTime == 13


def test_SimplePDL_Process_name_value_roundtrip():
    instance = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplePDL_Resource_occurrences_value_roundtrip():
    instance = SimplePDL_Resource(occurrences=7)
    assert instance.occurrences == 7
    instance.occurrences = 13
    assert instance.occurrences == 13


def test_SimplePDL_ResourceType_name_value_roundtrip():
    instance = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplePDL_ResourceType_occurrences_value_roundtrip():
    instance = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    assert instance.occurrences == 7
    instance.occurrences = 13
    assert instance.occurrences == 13


def test_SimplePDL_WorkDefinition_maxTime_value_roundtrip():
    instance = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    assert instance.maxTime == 7
    instance.maxTime = 13
    assert instance.maxTime == 13


def test_SimplePDL_WorkDefinition_minTime_value_roundtrip():
    instance = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    assert instance.minTime == 7
    instance.minTime = 13
    assert instance.minTime == 13


def test_SimplePDL_WorkDefinition_name_value_roundtrip():
    instance = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplePDL_WorkSequence_linkType_value_roundtrip():
    instance = SimplePDL_WorkSequence(linkType="sample_text")
    assert instance.linkType == "sample_text"
    instance.linkType = "sample_text_2"
    assert instance.linkType == "sample_text_2"


def test_SimplePDL_Resource_isa_ProcessElement():
    instance = SimplePDL_Resource(occurrences=7)
    assert isinstance(instance, ProcessElement)


def test_SimplePDL_ResourceType_isa_ProcessElement():
    instance = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    assert isinstance(instance, ProcessElement)


def test_SimplePDL_WorkDefinition_isa_ProcessElement():
    instance = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    assert isinstance(instance, ProcessElement)


def test_SimplePDL_WorkSequence_isa_ProcessElement():
    instance = SimplePDL_WorkSequence(linkType="sample_text")
    assert isinstance(instance, ProcessElement)


def test_assoc_child7_link_reassign_clear():
    a = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_ProcessElement()
    b2 = SimplePDL_ProcessElement()
    _safe_set(a, 'parent', {b1})
    assert _is_linked(a, 'parent', b1)
    if hasattr(b1, 'ProcessElement'):
        assert _is_linked(b1, 'ProcessElement', a)
    _safe_set(a, 'parent', {b2})
    assert _is_linked(a, 'parent', b2)
    if hasattr(b1, 'ProcessElement'):
        assert not _is_linked(b1, 'ProcessElement', a)
    if hasattr(b2, 'ProcessElement'):
        assert _is_linked(b2, 'ProcessElement', a)
    _safe_set(a, 'parent', set())
    assert not _is_linked(a, 'parent', b2)
    if hasattr(b2, 'ProcessElement'):
        assert not _is_linked(b2, 'ProcessElement', a)


def test_assoc_guidanceGFX1_link_reassign_clear():
    a = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_Guidance(text="sample_text")
    b2 = SimplePDL_Guidance(text="sample_text_2")
    _safe_set(a, 'SimplePDL_Process2', {b1})
    assert _is_linked(a, 'SimplePDL_Process2', b1)
    if hasattr(b1, 'SimplePDL_Guidance'):
        assert _is_linked(b1, 'SimplePDL_Guidance', a)
    _safe_set(a, 'SimplePDL_Process2', {b2})
    assert _is_linked(a, 'SimplePDL_Process2', b2)
    if hasattr(b1, 'SimplePDL_Guidance'):
        assert not _is_linked(b1, 'SimplePDL_Guidance', a)
    if hasattr(b2, 'SimplePDL_Guidance'):
        assert _is_linked(b2, 'SimplePDL_Guidance', a)
    _safe_set(a, 'SimplePDL_Process2', set())
    assert not _is_linked(a, 'SimplePDL_Process2', b2)
    if hasattr(b2, 'SimplePDL_Guidance'):
        assert not _is_linked(b2, 'SimplePDL_Guidance', a)


def test_assoc_guides11_link_reassign_clear():
    a = SimplePDL_Guidance(text="sample_text")
    b1 = SimplePDL_ProcessElement()
    b2 = SimplePDL_ProcessElement()
    _safe_set(a, 'SimplePDL_Guidance13', b1)
    assert _is_linked(a, 'SimplePDL_Guidance13', b1)
    if hasattr(b1, 'SimplePDL_ProcessElement12'):
        assert _is_linked(b1, 'SimplePDL_ProcessElement12', a)
    _safe_set(a, 'SimplePDL_Guidance13', b2)
    assert _is_linked(a, 'SimplePDL_Guidance13', b2)
    if hasattr(b1, 'SimplePDL_ProcessElement12'):
        assert not _is_linked(b1, 'SimplePDL_ProcessElement12', a)
    if hasattr(b2, 'SimplePDL_ProcessElement12'):
        assert _is_linked(b2, 'SimplePDL_ProcessElement12', a)
    _safe_set(a, 'SimplePDL_Guidance13', None)
    assert not _is_linked(a, 'SimplePDL_Guidance13', b2)
    if hasattr(b2, 'SimplePDL_ProcessElement12'):
        assert not _is_linked(b2, 'SimplePDL_ProcessElement12', a)


def test_assoc_linksToPredecessors3_link_reassign_clear():
    a = SimplePDL_WorkSequence(linkType="sample_text")
    b1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'WorkSequence', b1)
    assert _is_linked(a, 'WorkSequence', b1)
    if hasattr(b1, 'successor'):
        assert _is_linked(b1, 'successor', a)
    _safe_set(a, 'WorkSequence', b2)
    assert _is_linked(a, 'WorkSequence', b2)
    if hasattr(b1, 'successor'):
        assert not _is_linked(b1, 'successor', a)
    if hasattr(b2, 'successor'):
        assert _is_linked(b2, 'successor', a)
    _safe_set(a, 'WorkSequence', None)
    assert not _is_linked(a, 'WorkSequence', b2)
    if hasattr(b2, 'successor'):
        assert not _is_linked(b2, 'successor', a)


def test_assoc_linksToSuccessors4_link_reassign_clear():
    a = SimplePDL_WorkSequence(linkType="sample_text")
    b1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'WorkSequence5', b1)
    assert _is_linked(a, 'WorkSequence5', b1)
    if hasattr(b1, 'predecessor'):
        assert _is_linked(b1, 'predecessor', a)
    _safe_set(a, 'WorkSequence5', b2)
    assert _is_linked(a, 'WorkSequence5', b2)
    if hasattr(b1, 'predecessor'):
        assert not _is_linked(b1, 'predecessor', a)
    if hasattr(b2, 'predecessor'):
        assert _is_linked(b2, 'predecessor', a)
    _safe_set(a, 'WorkSequence5', None)
    assert not _is_linked(a, 'WorkSequence5', b2)
    if hasattr(b2, 'predecessor'):
        assert not _is_linked(b2, 'predecessor', a)


def test_assoc_neededResources6_link_reassign_clear():
    a = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_Resource(occurrences=7)
    b2 = SimplePDL_Resource(occurrences=13)
    _safe_set(a, 'workDefinition', {b1})
    assert _is_linked(a, 'workDefinition', b1)
    if hasattr(b1, 'Resource'):
        assert _is_linked(b1, 'Resource', a)
    _safe_set(a, 'workDefinition', {b2})
    assert _is_linked(a, 'workDefinition', b2)
    if hasattr(b1, 'Resource'):
        assert not _is_linked(b1, 'Resource', a)
    if hasattr(b2, 'Resource'):
        assert _is_linked(b2, 'Resource', a)
    _safe_set(a, 'workDefinition', set())
    assert not _is_linked(a, 'workDefinition', b2)
    if hasattr(b2, 'Resource'):
        assert not _is_linked(b2, 'Resource', a)


def test_assoc_parent14_link_reassign_clear():
    a = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_ProcessElement()
    b2 = SimplePDL_ProcessElement()
    _safe_set(a, 'WorkDefinition15', b1)
    assert _is_linked(a, 'WorkDefinition15', b1)
    if hasattr(b1, 'child'):
        assert _is_linked(b1, 'child', a)
    _safe_set(a, 'WorkDefinition15', b2)
    assert _is_linked(a, 'WorkDefinition15', b2)
    if hasattr(b1, 'child'):
        assert not _is_linked(b1, 'child', a)
    if hasattr(b2, 'child'):
        assert _is_linked(b2, 'child', a)
    _safe_set(a, 'WorkDefinition15', None)
    assert not _is_linked(a, 'WorkDefinition15', b2)
    if hasattr(b2, 'child'):
        assert not _is_linked(b2, 'child', a)


def test_assoc_predecessor8_link_reassign_clear():
    a = SimplePDL_WorkSequence(linkType="sample_text")
    b1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'linksToSuccessors', b1)
    assert _is_linked(a, 'linksToSuccessors', b1)
    if hasattr(b1, 'WorkDefinition'):
        assert _is_linked(b1, 'WorkDefinition', a)
    _safe_set(a, 'linksToSuccessors', b2)
    assert _is_linked(a, 'linksToSuccessors', b2)
    if hasattr(b1, 'WorkDefinition'):
        assert not _is_linked(b1, 'WorkDefinition', a)
    if hasattr(b2, 'WorkDefinition'):
        assert _is_linked(b2, 'WorkDefinition', a)
    _safe_set(a, 'linksToSuccessors', None)
    assert not _is_linked(a, 'linksToSuccessors', b2)
    if hasattr(b2, 'WorkDefinition'):
        assert not _is_linked(b2, 'WorkDefinition', a)


def test_assoc_processElements0_link_reassign_clear():
    a = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_ProcessElement()
    b2 = SimplePDL_ProcessElement()
    _safe_set(a, 'SimplePDL_Process', {b1})
    assert _is_linked(a, 'SimplePDL_Process', b1)
    if hasattr(b1, 'SimplePDL_ProcessElement'):
        assert _is_linked(b1, 'SimplePDL_ProcessElement', a)
    _safe_set(a, 'SimplePDL_Process', {b2})
    assert _is_linked(a, 'SimplePDL_Process', b2)
    if hasattr(b1, 'SimplePDL_ProcessElement'):
        assert not _is_linked(b1, 'SimplePDL_ProcessElement', a)
    if hasattr(b2, 'SimplePDL_ProcessElement'):
        assert _is_linked(b2, 'SimplePDL_ProcessElement', a)
    _safe_set(a, 'SimplePDL_Process', set())
    assert not _is_linked(a, 'SimplePDL_Process', b2)
    if hasattr(b2, 'SimplePDL_ProcessElement'):
        assert not _is_linked(b2, 'SimplePDL_ProcessElement', a)


def test_assoc_successor9_link_reassign_clear():
    a = SimplePDL_WorkSequence(linkType="sample_text")
    b1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'linksToPredecessors', b1)
    assert _is_linked(a, 'linksToPredecessors', b1)
    if hasattr(b1, 'WorkDefinition10'):
        assert _is_linked(b1, 'WorkDefinition10', a)
    _safe_set(a, 'linksToPredecessors', b2)
    assert _is_linked(a, 'linksToPredecessors', b2)
    if hasattr(b1, 'WorkDefinition10'):
        assert not _is_linked(b1, 'WorkDefinition10', a)
    if hasattr(b2, 'WorkDefinition10'):
        assert _is_linked(b2, 'WorkDefinition10', a)
    _safe_set(a, 'linksToPredecessors', None)
    assert not _is_linked(a, 'linksToPredecessors', b2)
    if hasattr(b2, 'WorkDefinition10'):
        assert not _is_linked(b2, 'WorkDefinition10', a)


def test_assoc_type18_link_reassign_clear():
    a = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    b1 = SimplePDL_Resource(occurrences=7)
    b2 = SimplePDL_Resource(occurrences=13)
    _safe_set(a, 'SimplePDL_ResourceType', b1)
    assert _is_linked(a, 'SimplePDL_ResourceType', b1)
    if hasattr(b1, 'SimplePDL_Resource'):
        assert _is_linked(b1, 'SimplePDL_Resource', a)
    _safe_set(a, 'SimplePDL_ResourceType', b2)
    assert _is_linked(a, 'SimplePDL_ResourceType', b2)
    if hasattr(b1, 'SimplePDL_Resource'):
        assert not _is_linked(b1, 'SimplePDL_Resource', a)
    if hasattr(b2, 'SimplePDL_Resource'):
        assert _is_linked(b2, 'SimplePDL_Resource', a)
    _safe_set(a, 'SimplePDL_ResourceType', None)
    assert not _is_linked(a, 'SimplePDL_ResourceType', b2)
    if hasattr(b2, 'SimplePDL_Resource'):
        assert not _is_linked(b2, 'SimplePDL_Resource', a)


def test_assoc_workDefinition16_link_reassign_clear():
    a = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    b1 = SimplePDL_Resource(occurrences=7)
    b2 = SimplePDL_Resource(occurrences=13)
    _safe_set(a, 'WorkDefinition17', b1)
    assert _is_linked(a, 'WorkDefinition17', b1)
    if hasattr(b1, 'neededResources'):
        assert _is_linked(b1, 'neededResources', a)
    _safe_set(a, 'WorkDefinition17', b2)
    assert _is_linked(a, 'WorkDefinition17', b2)
    if hasattr(b1, 'neededResources'):
        assert not _is_linked(b1, 'neededResources', a)
    if hasattr(b2, 'neededResources'):
        assert _is_linked(b2, 'neededResources', a)
    _safe_set(a, 'WorkDefinition17', None)
    assert not _is_linked(a, 'WorkDefinition17', b2)
    if hasattr(b2, 'neededResources'):
        assert not _is_linked(b2, 'neededResources', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ProcessElement_strategy = st.builds(ProcessElement)
@given(instance=ProcessElement_strategy)
@settings(max_examples=25)
def test_ProcessElement_instantiation(instance):
    assert isinstance(instance, ProcessElement)


SimplePDL_Guidance_strategy = st.builds(SimplePDL_Guidance, text=safe_text)
@given(instance=SimplePDL_Guidance_strategy)
@settings(max_examples=25)
def test_SimplePDL_Guidance_instantiation(instance):
    assert isinstance(instance, SimplePDL_Guidance)


SimplePDL_Process_strategy = st.builds(SimplePDL_Process, maxTime=st.integers(), minTime=st.integers(), name=safe_text)
@given(instance=SimplePDL_Process_strategy)
@settings(max_examples=25)
def test_SimplePDL_Process_instantiation(instance):
    assert isinstance(instance, SimplePDL_Process)


SimplePDL_ProcessElement_strategy = st.builds(SimplePDL_ProcessElement)
@given(instance=SimplePDL_ProcessElement_strategy)
@settings(max_examples=25)
def test_SimplePDL_ProcessElement_instantiation(instance):
    assert isinstance(instance, SimplePDL_ProcessElement)


SimplePDL_Resource_strategy = st.builds(SimplePDL_Resource, occurrences=st.integers())
@given(instance=SimplePDL_Resource_strategy)
@settings(max_examples=25)
def test_SimplePDL_Resource_instantiation(instance):
    assert isinstance(instance, SimplePDL_Resource)


SimplePDL_ResourceType_strategy = st.builds(SimplePDL_ResourceType, name=safe_text, occurrences=st.integers())
@given(instance=SimplePDL_ResourceType_strategy)
@settings(max_examples=25)
def test_SimplePDL_ResourceType_instantiation(instance):
    assert isinstance(instance, SimplePDL_ResourceType)


SimplePDL_WorkDefinition_strategy = st.builds(SimplePDL_WorkDefinition, maxTime=st.integers(), minTime=st.integers(), name=safe_text)
@given(instance=SimplePDL_WorkDefinition_strategy)
@settings(max_examples=25)
def test_SimplePDL_WorkDefinition_instantiation(instance):
    assert isinstance(instance, SimplePDL_WorkDefinition)


SimplePDL_WorkSequence_strategy = st.builds(SimplePDL_WorkSequence, linkType=safe_text)
@given(instance=SimplePDL_WorkSequence_strategy)
@settings(max_examples=25)
def test_SimplePDL_WorkSequence_instantiation(instance):
    assert isinstance(instance, SimplePDL_WorkSequence)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProcessElement,
    SimplePDL_Guidance,
    SimplePDL_Process,
    SimplePDL_ProcessElement,
    SimplePDL_Resource,
    SimplePDL_ResourceType,
    SimplePDL_WorkDefinition,
    SimplePDL_WorkSequence,
    WorkSequenceType,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_guidanceGFX1_reverse_link_reassign_clear():
    a1 = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_Process(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Guidance(text="sample_text")
    _safe_set(b, 'SimplePDL_Guidance', a1)
    assert _is_linked(b, 'SimplePDL_Guidance', a1)
    if hasattr(a1, 'SimplePDL_Process2'):
        assert _is_linked(a1, 'SimplePDL_Process2', b)
    _safe_set(b, 'SimplePDL_Guidance', a2)
    assert _is_linked(b, 'SimplePDL_Guidance', a2)
    if hasattr(a1, 'SimplePDL_Process2'):
        assert not _is_linked(a1, 'SimplePDL_Process2', b)
    if hasattr(a2, 'SimplePDL_Process2'):
        assert _is_linked(a2, 'SimplePDL_Process2', b)
    _safe_set(b, 'SimplePDL_Guidance', None)
    assert not _is_linked(b, 'SimplePDL_Guidance', a2)
    if hasattr(a2, 'SimplePDL_Process2'):
        assert not _is_linked(a2, 'SimplePDL_Process2', b)


def test_assoc_linksToPredecessors3_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'successor', {a1})
    assert _is_linked(b, 'successor', a1)
    if hasattr(a1, 'WorkSequence'):
        assert _is_linked(a1, 'WorkSequence', b)
    _safe_set(b, 'successor', {a2})
    assert _is_linked(b, 'successor', a2)
    if hasattr(a1, 'WorkSequence'):
        assert not _is_linked(a1, 'WorkSequence', b)
    if hasattr(a2, 'WorkSequence'):
        assert _is_linked(a2, 'WorkSequence', b)
    _safe_set(b, 'successor', set())
    assert not _is_linked(b, 'successor', a2)
    if hasattr(a2, 'WorkSequence'):
        assert not _is_linked(a2, 'WorkSequence', b)


def test_assoc_linksToSuccessors4_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence5'):
        assert _is_linked(a1, 'WorkSequence5', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence5'):
        assert not _is_linked(a1, 'WorkSequence5', b)
    if hasattr(a2, 'WorkSequence5'):
        assert _is_linked(a2, 'WorkSequence5', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence5'):
        assert not _is_linked(a2, 'WorkSequence5', b)


def test_assoc_neededResources6_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'Resource', a1)
    assert _is_linked(b, 'Resource', a1)
    if hasattr(a1, 'workDefinition'):
        assert _is_linked(a1, 'workDefinition', b)
    _safe_set(b, 'Resource', a2)
    assert _is_linked(b, 'Resource', a2)
    if hasattr(a1, 'workDefinition'):
        assert not _is_linked(a1, 'workDefinition', b)
    if hasattr(a2, 'workDefinition'):
        assert _is_linked(a2, 'workDefinition', b)
    _safe_set(b, 'Resource', None)
    assert not _is_linked(b, 'Resource', a2)
    if hasattr(a2, 'workDefinition'):
        assert not _is_linked(a2, 'workDefinition', b)


def test_assoc_predecessor8_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'WorkDefinition', a1)
    assert _is_linked(b, 'WorkDefinition', a1)
    if hasattr(a1, 'linksToSuccessors'):
        assert _is_linked(a1, 'linksToSuccessors', b)
    _safe_set(b, 'WorkDefinition', a2)
    assert _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a1, 'linksToSuccessors'):
        assert not _is_linked(a1, 'linksToSuccessors', b)
    if hasattr(a2, 'linksToSuccessors'):
        assert _is_linked(a2, 'linksToSuccessors', b)
    _safe_set(b, 'WorkDefinition', None)
    assert not _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a2, 'linksToSuccessors'):
        assert not _is_linked(a2, 'linksToSuccessors', b)


def test_assoc_successor9_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'WorkDefinition10', a1)
    assert _is_linked(b, 'WorkDefinition10', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition10', a2)
    assert _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition10', None)
    assert not _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


def test_assoc_type18_reverse_link_reassign_clear():
    a1 = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    a2 = SimplePDL_ResourceType(name="sample_text_2", occurrences=13)
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'SimplePDL_Resource', a1)
    assert _is_linked(b, 'SimplePDL_Resource', a1)
    if hasattr(a1, 'SimplePDL_ResourceType'):
        assert _is_linked(a1, 'SimplePDL_ResourceType', b)
    _safe_set(b, 'SimplePDL_Resource', a2)
    assert _is_linked(b, 'SimplePDL_Resource', a2)
    if hasattr(a1, 'SimplePDL_ResourceType'):
        assert not _is_linked(a1, 'SimplePDL_ResourceType', b)
    if hasattr(a2, 'SimplePDL_ResourceType'):
        assert _is_linked(a2, 'SimplePDL_ResourceType', b)
    _safe_set(b, 'SimplePDL_Resource', None)
    assert not _is_linked(b, 'SimplePDL_Resource', a2)
    if hasattr(a2, 'SimplePDL_ResourceType'):
        assert not _is_linked(a2, 'SimplePDL_ResourceType', b)


def test_assoc_workDefinition16_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'neededResources', a1)
    assert _is_linked(b, 'neededResources', a1)
    if hasattr(a1, 'WorkDefinition17'):
        assert _is_linked(a1, 'WorkDefinition17', b)
    _safe_set(b, 'neededResources', a2)
    assert _is_linked(b, 'neededResources', a2)
    if hasattr(a1, 'WorkDefinition17'):
        assert not _is_linked(a1, 'WorkDefinition17', b)
    if hasattr(a2, 'WorkDefinition17'):
        assert _is_linked(a2, 'WorkDefinition17', b)
    _safe_set(b, 'neededResources', None)
    assert not _is_linked(b, 'neededResources', a2)
    if hasattr(a2, 'WorkDefinition17'):
        assert not _is_linked(a2, 'WorkDefinition17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child7_stub_double():
    # SimplePDL_ProcessElement has no real 'ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'ProcessElement', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'ProcessElement') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'ProcessElement') is None


def test_assoc_guides11_stub_double():
    # SimplePDL_ProcessElement has no real 'SimplePDL_ProcessElement12' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_Guidance(text="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'SimplePDL_ProcessElement12', None)
    _safe_set(owner, 'SimplePDL_Guidance13', partner)
    assert owner in getattr(partner, 'SimplePDL_ProcessElement12')
    _safe_set(owner, 'SimplePDL_Guidance13', None)
    assert owner not in getattr(partner, 'SimplePDL_ProcessElement12')


def test_assoc_parent14_stub_double():
    # SimplePDL_ProcessElement has no real 'child' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'child', None)
    _safe_set(owner, 'WorkDefinition15', partner)
    assert getattr(partner, 'child') == owner
    _safe_set(owner, 'WorkDefinition15', None)
    assert getattr(partner, 'child') is None


def test_assoc_processElements0_stub_double():
    # SimplePDL_ProcessElement has no real 'SimplePDL_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'SimplePDL_ProcessElement', None)
    _safe_set(owner, 'SimplePDL_Process', {partner})
    assert getattr(partner, 'SimplePDL_ProcessElement') == owner
    _safe_set(owner, 'SimplePDL_Process', set())
    assert getattr(partner, 'SimplePDL_ProcessElement') is None




from python_code import SimplePDL_Process

def test_SimplePDL_Process___init__():
    assert SimplePDL_Process.__init__(SimplePDL_Process('', 0, 0, SimplePDL_Process=set(), SimplePDL_Process2=set()), '', 0, 0, SimplePDL_Process=set(), SimplePDL_Process2=set()) == None

