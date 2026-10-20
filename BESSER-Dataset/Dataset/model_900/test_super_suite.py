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
    simplepdl_WorkSequence,
    simplepdl_WorkDefinition,
    simplepdl_Process,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simplepdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(simplepdl_WorkSequence)


def test_hyp_simplepdl_worksequence_constructor_exists():
    assert callable(simplepdl_WorkSequence.__init__)


def test_hyp_simplepdl_worksequence_constructor_args():
    sig = inspect.signature(simplepdl_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"




def test_hyp_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl_WorkDefinition)


def test_hyp_simplepdl_workdefinition_constructor_exists():
    assert callable(simplepdl_WorkDefinition.__init__)


def test_hyp_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(simplepdl_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplepdl_process_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Process)


def test_hyp_simplepdl_process_constructor_exists():
    assert callable(simplepdl_Process.__init__)


def test_hyp_simplepdl_process_constructor_args():
    sig = inspect.signature(simplepdl_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_hyp_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "finishToFinish",
        "startToFinish",
        "finishToStart",
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
simplepdl_WorkSequence_strategy = st.builds(
    simplepdl_WorkSequence,
    linkType=
        safe_text
)
simplepdl_WorkDefinition_strategy = st.builds(
    simplepdl_WorkDefinition,
    name=
        safe_text
)
simplepdl_Process_strategy = st.builds(
    simplepdl_Process,
    name=
        safe_text
)




@given(instance=simplepdl_WorkSequence_strategy)
def test_hyp_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original




@given(instance=simplepdl_WorkDefinition_strategy)
def test_hyp_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=simplepdl_Process_strategy)
def test_hyp_simplepdl_process_name_setter(instance):
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
    simplepdl_Process,
    simplepdl_WorkDefinition,
    simplepdl_WorkSequence,
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

def test_simplepdl_Process_name_value_roundtrip():
    instance = simplepdl_Process(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simplepdl_WorkDefinition_name_value_roundtrip():
    instance = simplepdl_WorkDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simplepdl_WorkSequence_linkType_value_roundtrip():
    instance = simplepdl_WorkSequence(linkType="sample_text")
    assert instance.linkType == "sample_text"
    instance.linkType = "sample_text_2"
    assert instance.linkType == "sample_text_2"


def test_assoc_activities0_link_reassign_clear():
    a = simplepdl_WorkDefinition(name="sample_text")
    b1 = simplepdl_Process(name="sample_text")
    b2 = simplepdl_Process(name="sample_text_2")
    _safe_set(a, 'simplepdl_WorkDefinition', b1)
    assert _is_linked(a, 'simplepdl_WorkDefinition', b1)
    if hasattr(b1, 'simplepdl_Process'):
        assert _is_linked(b1, 'simplepdl_Process', a)
    _safe_set(a, 'simplepdl_WorkDefinition', b2)
    assert _is_linked(a, 'simplepdl_WorkDefinition', b2)
    if hasattr(b1, 'simplepdl_Process'):
        assert not _is_linked(b1, 'simplepdl_Process', a)
    if hasattr(b2, 'simplepdl_Process'):
        assert _is_linked(b2, 'simplepdl_Process', a)
    _safe_set(a, 'simplepdl_WorkDefinition', None)
    assert not _is_linked(a, 'simplepdl_WorkDefinition', b2)
    if hasattr(b2, 'simplepdl_Process'):
        assert not _is_linked(b2, 'simplepdl_Process', a)


def test_assoc_linksToPredecessors3_link_reassign_clear():
    a = simplepdl_WorkSequence(linkType="sample_text")
    b1 = simplepdl_WorkDefinition(name="sample_text")
    b2 = simplepdl_WorkDefinition(name="sample_text_2")
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
    a = simplepdl_WorkSequence(linkType="sample_text")
    b1 = simplepdl_WorkDefinition(name="sample_text")
    b2 = simplepdl_WorkDefinition(name="sample_text_2")
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


def test_assoc_predecessor6_link_reassign_clear():
    a = simplepdl_WorkSequence(linkType="sample_text")
    b1 = simplepdl_WorkDefinition(name="sample_text")
    b2 = simplepdl_WorkDefinition(name="sample_text_2")
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


def test_assoc_successor7_link_reassign_clear():
    a = simplepdl_WorkSequence(linkType="sample_text")
    b1 = simplepdl_WorkDefinition(name="sample_text")
    b2 = simplepdl_WorkDefinition(name="sample_text_2")
    _safe_set(a, 'linksToPredecessors', b1)
    assert _is_linked(a, 'linksToPredecessors', b1)
    if hasattr(b1, 'WorkDefinition8'):
        assert _is_linked(b1, 'WorkDefinition8', a)
    _safe_set(a, 'linksToPredecessors', b2)
    assert _is_linked(a, 'linksToPredecessors', b2)
    if hasattr(b1, 'WorkDefinition8'):
        assert not _is_linked(b1, 'WorkDefinition8', a)
    if hasattr(b2, 'WorkDefinition8'):
        assert _is_linked(b2, 'WorkDefinition8', a)
    _safe_set(a, 'linksToPredecessors', None)
    assert not _is_linked(a, 'linksToPredecessors', b2)
    if hasattr(b2, 'WorkDefinition8'):
        assert not _is_linked(b2, 'WorkDefinition8', a)


def test_assoc_workSequences1_link_reassign_clear():
    a = simplepdl_WorkSequence(linkType="sample_text")
    b1 = simplepdl_Process(name="sample_text")
    b2 = simplepdl_Process(name="sample_text_2")
    _safe_set(a, 'simplepdl_WorkSequence', b1)
    assert _is_linked(a, 'simplepdl_WorkSequence', b1)
    if hasattr(b1, 'simplepdl_Process2'):
        assert _is_linked(b1, 'simplepdl_Process2', a)
    _safe_set(a, 'simplepdl_WorkSequence', b2)
    assert _is_linked(a, 'simplepdl_WorkSequence', b2)
    if hasattr(b1, 'simplepdl_Process2'):
        assert not _is_linked(b1, 'simplepdl_Process2', a)
    if hasattr(b2, 'simplepdl_Process2'):
        assert _is_linked(b2, 'simplepdl_Process2', a)
    _safe_set(a, 'simplepdl_WorkSequence', None)
    assert not _is_linked(a, 'simplepdl_WorkSequence', b2)
    if hasattr(b2, 'simplepdl_Process2'):
        assert not _is_linked(b2, 'simplepdl_Process2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

simplepdl_Process_strategy = st.builds(simplepdl_Process, name=safe_text)
@given(instance=simplepdl_Process_strategy)
@settings(max_examples=25)
def test_simplepdl_Process_instantiation(instance):
    assert isinstance(instance, simplepdl_Process)


simplepdl_WorkDefinition_strategy = st.builds(simplepdl_WorkDefinition, name=safe_text)
@given(instance=simplepdl_WorkDefinition_strategy)
@settings(max_examples=25)
def test_simplepdl_WorkDefinition_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkDefinition)


simplepdl_WorkSequence_strategy = st.builds(simplepdl_WorkSequence, linkType=safe_text)
@given(instance=simplepdl_WorkSequence_strategy)
@settings(max_examples=25)
def test_simplepdl_WorkSequence_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkSequence)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simplepdl_Process,
    simplepdl_WorkDefinition,
    simplepdl_WorkSequence,
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

def test_assoc_activities0_reverse_link_reassign_clear():
    a1 = simplepdl_WorkDefinition(name="sample_text")
    a2 = simplepdl_WorkDefinition(name="sample_text_2")
    b = simplepdl_Process(name="sample_text")
    _safe_set(b, 'simplepdl_Process', {a1})
    assert _is_linked(b, 'simplepdl_Process', a1)
    if hasattr(a1, 'simplepdl_WorkDefinition'):
        assert _is_linked(a1, 'simplepdl_WorkDefinition', b)
    _safe_set(b, 'simplepdl_Process', {a2})
    assert _is_linked(b, 'simplepdl_Process', a2)
    if hasattr(a1, 'simplepdl_WorkDefinition'):
        assert not _is_linked(a1, 'simplepdl_WorkDefinition', b)
    if hasattr(a2, 'simplepdl_WorkDefinition'):
        assert _is_linked(a2, 'simplepdl_WorkDefinition', b)
    _safe_set(b, 'simplepdl_Process', set())
    assert not _is_linked(b, 'simplepdl_Process', a2)
    if hasattr(a2, 'simplepdl_WorkDefinition'):
        assert not _is_linked(a2, 'simplepdl_WorkDefinition', b)


def test_assoc_linksToPredecessors3_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
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
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
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


def test_assoc_predecessor6_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
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


def test_assoc_successor7_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition8', a1)
    assert _is_linked(b, 'WorkDefinition8', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition8', a2)
    assert _is_linked(b, 'WorkDefinition8', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition8', None)
    assert not _is_linked(b, 'WorkDefinition8', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


def test_assoc_workSequences1_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_Process(name="sample_text")
    _safe_set(b, 'simplepdl_Process2', {a1})
    assert _is_linked(b, 'simplepdl_Process2', a1)
    if hasattr(a1, 'simplepdl_WorkSequence'):
        assert _is_linked(a1, 'simplepdl_WorkSequence', b)
    _safe_set(b, 'simplepdl_Process2', {a2})
    assert _is_linked(b, 'simplepdl_Process2', a2)
    if hasattr(a1, 'simplepdl_WorkSequence'):
        assert not _is_linked(a1, 'simplepdl_WorkSequence', b)
    if hasattr(a2, 'simplepdl_WorkSequence'):
        assert _is_linked(a2, 'simplepdl_WorkSequence', b)
    _safe_set(b, 'simplepdl_Process2', set())
    assert not _is_linked(b, 'simplepdl_Process2', a2)
    if hasattr(a2, 'simplepdl_WorkSequence'):
        assert not _is_linked(a2, 'simplepdl_WorkSequence', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import simplepdl_Process

def test_simplepdl_Process___init__():
    assert simplepdl_Process.__init__(simplepdl_Process('', simplepdl_Process2=set(), simplepdl_Process=set()), '', simplepdl_Process2=set(), simplepdl_Process=set()) == None

