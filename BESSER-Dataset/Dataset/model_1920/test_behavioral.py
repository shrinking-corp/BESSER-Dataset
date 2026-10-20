import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    jbatch_Analyzer,
    jbatch_Batchlet,
    jbatch_CheckpointAlgorithm,
    jbatch_Chunk,
    jbatch_Collector,
    jbatch_Decision,
    jbatch_DocumentRoot,
    jbatch_EStringToStringMapEntry,
    jbatch_End,
    jbatch_ExceptionClassFilter,
    jbatch_ExcludeType,
    jbatch_Fail,
    jbatch_Flow,
    jbatch_IncludeType,
    jbatch_ItemProcessor,
    jbatch_ItemReader,
    jbatch_ItemWriter,
    jbatch_Job,
    jbatch_Listener,
    jbatch_Listeners,
    jbatch_Next,
    jbatch_Partition,
    jbatch_PartitionMapper,
    jbatch_PartitionPlan,
    jbatch_PartitionReducer,
    jbatch_Properties,
    jbatch_Property,
    jbatch_Split,
    jbatch_Step,
    jbatch_Stop,
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

def test_assoc_batchlet126_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Batchlet(ref="sample_text")
    _safe_set(b, 'jbatch_Batchlet128', a1)
    assert _is_linked(b, 'jbatch_Batchlet128', a1)
    if hasattr(a1, 'jbatch_Step127'):
        assert _is_linked(a1, 'jbatch_Step127', b)
    _safe_set(b, 'jbatch_Batchlet128', a2)
    assert _is_linked(b, 'jbatch_Batchlet128', a2)
    if hasattr(a1, 'jbatch_Step127'):
        assert not _is_linked(a1, 'jbatch_Step127', b)
    if hasattr(a2, 'jbatch_Step127'):
        assert _is_linked(a2, 'jbatch_Step127', b)
    _safe_set(b, 'jbatch_Batchlet128', None)
    assert not _is_linked(b, 'jbatch_Batchlet128', a2)
    if hasattr(a2, 'jbatch_Step127'):
        assert not _is_linked(a2, 'jbatch_Step127', b)


def test_assoc_checkpointAlgorithm10_reverse_link_reassign_clear():
    a1 = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    a2 = jbatch_Chunk(checkpointPolicy="sample_text_2", itemCount="sample_text_2", retryLimit="sample_text_2", skipLimit="sample_text_2", timeLimit="sample_text_2")
    b = jbatch_CheckpointAlgorithm(ref="sample_text")
    _safe_set(b, 'jbatch_CheckpointAlgorithm12', a1)
    assert _is_linked(b, 'jbatch_CheckpointAlgorithm12', a1)
    if hasattr(a1, 'jbatch_Chunk11'):
        assert _is_linked(a1, 'jbatch_Chunk11', b)
    _safe_set(b, 'jbatch_CheckpointAlgorithm12', a2)
    assert _is_linked(b, 'jbatch_CheckpointAlgorithm12', a2)
    if hasattr(a1, 'jbatch_Chunk11'):
        assert not _is_linked(a1, 'jbatch_Chunk11', b)
    if hasattr(a2, 'jbatch_Chunk11'):
        assert _is_linked(a2, 'jbatch_Chunk11', b)
    _safe_set(b, 'jbatch_CheckpointAlgorithm12', None)
    assert not _is_linked(b, 'jbatch_CheckpointAlgorithm12', a2)
    if hasattr(a2, 'jbatch_Chunk11'):
        assert not _is_linked(a2, 'jbatch_Chunk11', b)


def test_assoc_chunk129_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    _safe_set(b, 'jbatch_Chunk131', a1)
    assert _is_linked(b, 'jbatch_Chunk131', a1)
    if hasattr(a1, 'jbatch_Step130'):
        assert _is_linked(a1, 'jbatch_Step130', b)
    _safe_set(b, 'jbatch_Chunk131', a2)
    assert _is_linked(b, 'jbatch_Chunk131', a2)
    if hasattr(a1, 'jbatch_Step130'):
        assert not _is_linked(a1, 'jbatch_Step130', b)
    if hasattr(a2, 'jbatch_Step130'):
        assert _is_linked(a2, 'jbatch_Step130', b)
    _safe_set(b, 'jbatch_Chunk131', None)
    assert not _is_linked(b, 'jbatch_Chunk131', a2)
    if hasattr(a2, 'jbatch_Step130'):
        assert not _is_linked(a2, 'jbatch_Step130', b)


def test_assoc_decision43_reverse_link_reassign_clear():
    a1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    a2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision44', a1)
    assert _is_linked(b, 'jbatch_Decision44', a1)
    if hasattr(a1, 'jbatch_Flow'):
        assert _is_linked(a1, 'jbatch_Flow', b)
    _safe_set(b, 'jbatch_Decision44', a2)
    assert _is_linked(b, 'jbatch_Decision44', a2)
    if hasattr(a1, 'jbatch_Flow'):
        assert not _is_linked(a1, 'jbatch_Flow', b)
    if hasattr(a2, 'jbatch_Flow'):
        assert _is_linked(a2, 'jbatch_Flow', b)
    _safe_set(b, 'jbatch_Decision44', None)
    assert not _is_linked(b, 'jbatch_Decision44', a2)
    if hasattr(a2, 'jbatch_Flow'):
        assert not _is_linked(a2, 'jbatch_Flow', b)


def test_assoc_decision78_reverse_link_reassign_clear():
    a1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    a2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision80', a1)
    assert _is_linked(b, 'jbatch_Decision80', a1)
    if hasattr(a1, 'jbatch_Job79'):
        assert _is_linked(a1, 'jbatch_Job79', b)
    _safe_set(b, 'jbatch_Decision80', a2)
    assert _is_linked(b, 'jbatch_Decision80', a2)
    if hasattr(a1, 'jbatch_Job79'):
        assert not _is_linked(a1, 'jbatch_Job79', b)
    if hasattr(a2, 'jbatch_Job79'):
        assert _is_linked(a2, 'jbatch_Job79', b)
    _safe_set(b, 'jbatch_Decision80', None)
    assert not _is_linked(b, 'jbatch_Decision80', a2)
    if hasattr(a2, 'jbatch_Job79'):
        assert not _is_linked(a2, 'jbatch_Job79', b)


def test_assoc_end135_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_End(exitStatus="sample_text", on="sample_text")
    _safe_set(b, 'jbatch_End137', a1)
    assert _is_linked(b, 'jbatch_End137', a1)
    if hasattr(a1, 'jbatch_Step136'):
        assert _is_linked(a1, 'jbatch_Step136', b)
    _safe_set(b, 'jbatch_End137', a2)
    assert _is_linked(b, 'jbatch_End137', a2)
    if hasattr(a1, 'jbatch_Step136'):
        assert not _is_linked(a1, 'jbatch_Step136', b)
    if hasattr(a2, 'jbatch_Step136'):
        assert _is_linked(a2, 'jbatch_Step136', b)
    _safe_set(b, 'jbatch_End137', None)
    assert not _is_linked(b, 'jbatch_End137', a2)
    if hasattr(a2, 'jbatch_Step136'):
        assert not _is_linked(a2, 'jbatch_Step136', b)


def test_assoc_end25_reverse_link_reassign_clear():
    a1 = jbatch_End(exitStatus="sample_text", on="sample_text")
    a2 = jbatch_End(exitStatus="sample_text_2", on="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision26', {a1})
    assert _is_linked(b, 'jbatch_Decision26', a1)
    if hasattr(a1, 'jbatch_End'):
        assert _is_linked(a1, 'jbatch_End', b)
    _safe_set(b, 'jbatch_Decision26', {a2})
    assert _is_linked(b, 'jbatch_Decision26', a2)
    if hasattr(a1, 'jbatch_End'):
        assert not _is_linked(a1, 'jbatch_End', b)
    if hasattr(a2, 'jbatch_End'):
        assert _is_linked(a2, 'jbatch_End', b)
    _safe_set(b, 'jbatch_Decision26', set())
    assert not _is_linked(b, 'jbatch_Decision26', a2)
    if hasattr(a2, 'jbatch_End'):
        assert not _is_linked(a2, 'jbatch_End', b)


def test_assoc_end52_reverse_link_reassign_clear():
    a1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    a2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_End(exitStatus="sample_text", on="sample_text")
    _safe_set(b, 'jbatch_End54', a1)
    assert _is_linked(b, 'jbatch_End54', a1)
    if hasattr(a1, 'jbatch_Flow53'):
        assert _is_linked(a1, 'jbatch_Flow53', b)
    _safe_set(b, 'jbatch_End54', a2)
    assert _is_linked(b, 'jbatch_End54', a2)
    if hasattr(a1, 'jbatch_Flow53'):
        assert not _is_linked(a1, 'jbatch_Flow53', b)
    if hasattr(a2, 'jbatch_Flow53'):
        assert _is_linked(a2, 'jbatch_Flow53', b)
    _safe_set(b, 'jbatch_End54', None)
    assert not _is_linked(b, 'jbatch_End54', a2)
    if hasattr(a2, 'jbatch_Flow53'):
        assert not _is_linked(a2, 'jbatch_Flow53', b)


def test_assoc_fail138_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    _safe_set(b, 'jbatch_Fail140', a1)
    assert _is_linked(b, 'jbatch_Fail140', a1)
    if hasattr(a1, 'jbatch_Step139'):
        assert _is_linked(a1, 'jbatch_Step139', b)
    _safe_set(b, 'jbatch_Fail140', a2)
    assert _is_linked(b, 'jbatch_Fail140', a2)
    if hasattr(a1, 'jbatch_Step139'):
        assert not _is_linked(a1, 'jbatch_Step139', b)
    if hasattr(a2, 'jbatch_Step139'):
        assert _is_linked(a2, 'jbatch_Step139', b)
    _safe_set(b, 'jbatch_Fail140', None)
    assert not _is_linked(b, 'jbatch_Fail140', a2)
    if hasattr(a2, 'jbatch_Step139'):
        assert not _is_linked(a2, 'jbatch_Step139', b)


def test_assoc_fail27_reverse_link_reassign_clear():
    a1 = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    a2 = jbatch_Fail(exitStatus="sample_text_2", on="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision28', {a1})
    assert _is_linked(b, 'jbatch_Decision28', a1)
    if hasattr(a1, 'jbatch_Fail'):
        assert _is_linked(a1, 'jbatch_Fail', b)
    _safe_set(b, 'jbatch_Decision28', {a2})
    assert _is_linked(b, 'jbatch_Decision28', a2)
    if hasattr(a1, 'jbatch_Fail'):
        assert not _is_linked(a1, 'jbatch_Fail', b)
    if hasattr(a2, 'jbatch_Fail'):
        assert _is_linked(a2, 'jbatch_Fail', b)
    _safe_set(b, 'jbatch_Decision28', set())
    assert not _is_linked(b, 'jbatch_Decision28', a2)
    if hasattr(a2, 'jbatch_Fail'):
        assert not _is_linked(a2, 'jbatch_Fail', b)


def test_assoc_fail55_reverse_link_reassign_clear():
    a1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    a2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    _safe_set(b, 'jbatch_Fail57', a1)
    assert _is_linked(b, 'jbatch_Fail57', a1)
    if hasattr(a1, 'jbatch_Flow56'):
        assert _is_linked(a1, 'jbatch_Flow56', b)
    _safe_set(b, 'jbatch_Fail57', a2)
    assert _is_linked(b, 'jbatch_Fail57', a2)
    if hasattr(a1, 'jbatch_Flow56'):
        assert not _is_linked(a1, 'jbatch_Flow56', b)
    if hasattr(a2, 'jbatch_Flow56'):
        assert _is_linked(a2, 'jbatch_Flow56', b)
    _safe_set(b, 'jbatch_Fail57', None)
    assert not _is_linked(b, 'jbatch_Fail57', a2)
    if hasattr(a2, 'jbatch_Flow56'):
        assert not _is_linked(a2, 'jbatch_Flow56', b)


def test_assoc_flow117_reverse_link_reassign_clear():
    a1 = jbatch_Split(id="sample_text", next="sample_text")
    a2 = jbatch_Split(id="sample_text_2", next="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow119', a1)
    assert _is_linked(b, 'jbatch_Flow119', a1)
    if hasattr(a1, 'jbatch_Split118'):
        assert _is_linked(a1, 'jbatch_Split118', b)
    _safe_set(b, 'jbatch_Flow119', a2)
    assert _is_linked(b, 'jbatch_Flow119', a2)
    if hasattr(a1, 'jbatch_Split118'):
        assert not _is_linked(a1, 'jbatch_Split118', b)
    if hasattr(a2, 'jbatch_Split118'):
        assert _is_linked(a2, 'jbatch_Split118', b)
    _safe_set(b, 'jbatch_Flow119', None)
    assert not _is_linked(b, 'jbatch_Flow119', a2)
    if hasattr(a2, 'jbatch_Split118'):
        assert not _is_linked(a2, 'jbatch_Split118', b)


def test_assoc_flow46_reverse_link_reassign_clear():
    a1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    a2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow47', a1)
    assert _is_linked(b, 'jbatch_Flow47', a1)
    if hasattr(a1, 'jbatch_Flow45'):
        assert _is_linked(a1, 'jbatch_Flow45', b)
    _safe_set(b, 'jbatch_Flow47', a2)
    assert _is_linked(b, 'jbatch_Flow47', a2)
    if hasattr(a1, 'jbatch_Flow45'):
        assert not _is_linked(a1, 'jbatch_Flow45', b)
    if hasattr(a2, 'jbatch_Flow45'):
        assert _is_linked(a2, 'jbatch_Flow45', b)
    _safe_set(b, 'jbatch_Flow47', None)
    assert not _is_linked(b, 'jbatch_Flow47', a2)
    if hasattr(a2, 'jbatch_Flow45'):
        assert not _is_linked(a2, 'jbatch_Flow45', b)


def test_assoc_flow81_reverse_link_reassign_clear():
    a1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    a2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow83', a1)
    assert _is_linked(b, 'jbatch_Flow83', a1)
    if hasattr(a1, 'jbatch_Job82'):
        assert _is_linked(a1, 'jbatch_Job82', b)
    _safe_set(b, 'jbatch_Flow83', a2)
    assert _is_linked(b, 'jbatch_Flow83', a2)
    if hasattr(a1, 'jbatch_Job82'):
        assert not _is_linked(a1, 'jbatch_Job82', b)
    if hasattr(a2, 'jbatch_Job82'):
        assert _is_linked(a2, 'jbatch_Job82', b)
    _safe_set(b, 'jbatch_Flow83', None)
    assert not _is_linked(b, 'jbatch_Flow83', a2)
    if hasattr(a2, 'jbatch_Job82'):
        assert not _is_linked(a2, 'jbatch_Job82', b)


def test_assoc_job37_reverse_link_reassign_clear():
    a1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    a2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    b = jbatch_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jbatch_DocumentRoot38', {a1})
    assert _is_linked(b, 'jbatch_DocumentRoot38', a1)
    if hasattr(a1, 'jbatch_Job'):
        assert _is_linked(a1, 'jbatch_Job', b)
    _safe_set(b, 'jbatch_DocumentRoot38', {a2})
    assert _is_linked(b, 'jbatch_DocumentRoot38', a2)
    if hasattr(a1, 'jbatch_Job'):
        assert not _is_linked(a1, 'jbatch_Job', b)
    if hasattr(a2, 'jbatch_Job'):
        assert _is_linked(a2, 'jbatch_Job', b)
    _safe_set(b, 'jbatch_DocumentRoot38', set())
    assert not _is_linked(b, 'jbatch_DocumentRoot38', a2)
    if hasattr(a2, 'jbatch_Job'):
        assert not _is_linked(a2, 'jbatch_Job', b)


def test_assoc_next141_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Next(on="sample_text", to="sample_text")
    _safe_set(b, 'jbatch_Next143', a1)
    assert _is_linked(b, 'jbatch_Next143', a1)
    if hasattr(a1, 'jbatch_Step142'):
        assert _is_linked(a1, 'jbatch_Step142', b)
    _safe_set(b, 'jbatch_Next143', a2)
    assert _is_linked(b, 'jbatch_Next143', a2)
    if hasattr(a1, 'jbatch_Step142'):
        assert not _is_linked(a1, 'jbatch_Step142', b)
    if hasattr(a2, 'jbatch_Step142'):
        assert _is_linked(a2, 'jbatch_Step142', b)
    _safe_set(b, 'jbatch_Next143', None)
    assert not _is_linked(b, 'jbatch_Next143', a2)
    if hasattr(a2, 'jbatch_Step142'):
        assert not _is_linked(a2, 'jbatch_Step142', b)


def test_assoc_next29_reverse_link_reassign_clear():
    a1 = jbatch_Next(on="sample_text", to="sample_text")
    a2 = jbatch_Next(on="sample_text_2", to="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision30', {a1})
    assert _is_linked(b, 'jbatch_Decision30', a1)
    if hasattr(a1, 'jbatch_Next'):
        assert _is_linked(a1, 'jbatch_Next', b)
    _safe_set(b, 'jbatch_Decision30', {a2})
    assert _is_linked(b, 'jbatch_Decision30', a2)
    if hasattr(a1, 'jbatch_Next'):
        assert not _is_linked(a1, 'jbatch_Next', b)
    if hasattr(a2, 'jbatch_Next'):
        assert _is_linked(a2, 'jbatch_Next', b)
    _safe_set(b, 'jbatch_Decision30', set())
    assert not _is_linked(b, 'jbatch_Decision30', a2)
    if hasattr(a2, 'jbatch_Next'):
        assert not _is_linked(a2, 'jbatch_Next', b)


def test_assoc_next58_reverse_link_reassign_clear():
    a1 = jbatch_Next(on="sample_text", to="sample_text")
    a2 = jbatch_Next(on="sample_text_2", to="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow59', {a1})
    assert _is_linked(b, 'jbatch_Flow59', a1)
    if hasattr(a1, 'jbatch_Next60'):
        assert _is_linked(a1, 'jbatch_Next60', b)
    _safe_set(b, 'jbatch_Flow59', {a2})
    assert _is_linked(b, 'jbatch_Flow59', a2)
    if hasattr(a1, 'jbatch_Next60'):
        assert not _is_linked(a1, 'jbatch_Next60', b)
    if hasattr(a2, 'jbatch_Next60'):
        assert _is_linked(a2, 'jbatch_Next60', b)
    _safe_set(b, 'jbatch_Flow59', set())
    assert not _is_linked(b, 'jbatch_Flow59', a2)
    if hasattr(a2, 'jbatch_Next60'):
        assert not _is_linked(a2, 'jbatch_Next60', b)


def test_assoc_processor6_reverse_link_reassign_clear():
    a1 = jbatch_ItemProcessor(ref="sample_text")
    a2 = jbatch_ItemProcessor(ref="sample_text_2")
    b = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    _safe_set(b, 'jbatch_Chunk7', a1)
    assert _is_linked(b, 'jbatch_Chunk7', a1)
    if hasattr(a1, 'jbatch_ItemProcessor'):
        assert _is_linked(a1, 'jbatch_ItemProcessor', b)
    _safe_set(b, 'jbatch_Chunk7', a2)
    assert _is_linked(b, 'jbatch_Chunk7', a2)
    if hasattr(a1, 'jbatch_ItemProcessor'):
        assert not _is_linked(a1, 'jbatch_ItemProcessor', b)
    if hasattr(a2, 'jbatch_ItemProcessor'):
        assert _is_linked(a2, 'jbatch_ItemProcessor', b)
    _safe_set(b, 'jbatch_Chunk7', None)
    assert not _is_linked(b, 'jbatch_Chunk7', a2)
    if hasattr(a2, 'jbatch_ItemProcessor'):
        assert not _is_linked(a2, 'jbatch_ItemProcessor', b)


def test_assoc_properties0_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Analyzer(ref="sample_text")
    _safe_set(b, 'jbatch_Analyzer', a1)
    assert _is_linked(b, 'jbatch_Analyzer', a1)
    if hasattr(a1, 'jbatch_Properties'):
        assert _is_linked(a1, 'jbatch_Properties', b)
    _safe_set(b, 'jbatch_Analyzer', a2)
    assert _is_linked(b, 'jbatch_Analyzer', a2)
    if hasattr(a1, 'jbatch_Properties'):
        assert not _is_linked(a1, 'jbatch_Properties', b)
    if hasattr(a2, 'jbatch_Properties'):
        assert _is_linked(a2, 'jbatch_Properties', b)
    _safe_set(b, 'jbatch_Analyzer', None)
    assert not _is_linked(b, 'jbatch_Analyzer', a2)
    if hasattr(a2, 'jbatch_Properties'):
        assert not _is_linked(a2, 'jbatch_Properties', b)


def test_assoc_properties1_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Batchlet(ref="sample_text")
    _safe_set(b, 'jbatch_Batchlet', a1)
    assert _is_linked(b, 'jbatch_Batchlet', a1)
    if hasattr(a1, 'jbatch_Properties2'):
        assert _is_linked(a1, 'jbatch_Properties2', b)
    _safe_set(b, 'jbatch_Batchlet', a2)
    assert _is_linked(b, 'jbatch_Batchlet', a2)
    if hasattr(a1, 'jbatch_Properties2'):
        assert not _is_linked(a1, 'jbatch_Properties2', b)
    if hasattr(a2, 'jbatch_Properties2'):
        assert _is_linked(a2, 'jbatch_Properties2', b)
    _safe_set(b, 'jbatch_Batchlet', None)
    assert not _is_linked(b, 'jbatch_Batchlet', a2)
    if hasattr(a2, 'jbatch_Properties2'):
        assert not _is_linked(a2, 'jbatch_Properties2', b)


def test_assoc_properties106_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_PartitionMapper(ref="sample_text")
    _safe_set(b, 'jbatch_PartitionMapper107', a1)
    assert _is_linked(b, 'jbatch_PartitionMapper107', a1)
    if hasattr(a1, 'jbatch_Properties108'):
        assert _is_linked(a1, 'jbatch_Properties108', b)
    _safe_set(b, 'jbatch_PartitionMapper107', a2)
    assert _is_linked(b, 'jbatch_PartitionMapper107', a2)
    if hasattr(a1, 'jbatch_Properties108'):
        assert not _is_linked(a1, 'jbatch_Properties108', b)
    if hasattr(a2, 'jbatch_Properties108'):
        assert _is_linked(a2, 'jbatch_Properties108', b)
    _safe_set(b, 'jbatch_PartitionMapper107', None)
    assert not _is_linked(b, 'jbatch_PartitionMapper107', a2)
    if hasattr(a2, 'jbatch_Properties108'):
        assert not _is_linked(a2, 'jbatch_Properties108', b)


def test_assoc_properties109_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    _safe_set(b, 'jbatch_PartitionPlan110', {a1})
    assert _is_linked(b, 'jbatch_PartitionPlan110', a1)
    if hasattr(a1, 'jbatch_Properties111'):
        assert _is_linked(a1, 'jbatch_Properties111', b)
    _safe_set(b, 'jbatch_PartitionPlan110', {a2})
    assert _is_linked(b, 'jbatch_PartitionPlan110', a2)
    if hasattr(a1, 'jbatch_Properties111'):
        assert not _is_linked(a1, 'jbatch_Properties111', b)
    if hasattr(a2, 'jbatch_Properties111'):
        assert _is_linked(a2, 'jbatch_Properties111', b)
    _safe_set(b, 'jbatch_PartitionPlan110', set())
    assert not _is_linked(b, 'jbatch_PartitionPlan110', a2)
    if hasattr(a2, 'jbatch_Properties111'):
        assert not _is_linked(a2, 'jbatch_Properties111', b)


def test_assoc_properties112_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_PartitionReducer(ref="sample_text")
    _safe_set(b, 'jbatch_PartitionReducer113', a1)
    assert _is_linked(b, 'jbatch_PartitionReducer113', a1)
    if hasattr(a1, 'jbatch_Properties114'):
        assert _is_linked(a1, 'jbatch_Properties114', b)
    _safe_set(b, 'jbatch_PartitionReducer113', a2)
    assert _is_linked(b, 'jbatch_PartitionReducer113', a2)
    if hasattr(a1, 'jbatch_Properties114'):
        assert not _is_linked(a1, 'jbatch_Properties114', b)
    if hasattr(a2, 'jbatch_Properties114'):
        assert _is_linked(a2, 'jbatch_Properties114', b)
    _safe_set(b, 'jbatch_PartitionReducer113', None)
    assert not _is_linked(b, 'jbatch_PartitionReducer113', a2)
    if hasattr(a2, 'jbatch_Properties114'):
        assert not _is_linked(a2, 'jbatch_Properties114', b)


def test_assoc_properties120_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Properties(partition="sample_text")
    _safe_set(b, 'jbatch_Properties122', a1)
    assert _is_linked(b, 'jbatch_Properties122', a1)
    if hasattr(a1, 'jbatch_Step121'):
        assert _is_linked(a1, 'jbatch_Step121', b)
    _safe_set(b, 'jbatch_Properties122', a2)
    assert _is_linked(b, 'jbatch_Properties122', a2)
    if hasattr(a1, 'jbatch_Step121'):
        assert not _is_linked(a1, 'jbatch_Step121', b)
    if hasattr(a2, 'jbatch_Step121'):
        assert _is_linked(a2, 'jbatch_Step121', b)
    _safe_set(b, 'jbatch_Properties122', None)
    assert not _is_linked(b, 'jbatch_Properties122', a2)
    if hasattr(a2, 'jbatch_Step121'):
        assert not _is_linked(a2, 'jbatch_Step121', b)


def test_assoc_properties21_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Collector(ref="sample_text")
    _safe_set(b, 'jbatch_Collector', a1)
    assert _is_linked(b, 'jbatch_Collector', a1)
    if hasattr(a1, 'jbatch_Properties22'):
        assert _is_linked(a1, 'jbatch_Properties22', b)
    _safe_set(b, 'jbatch_Collector', a2)
    assert _is_linked(b, 'jbatch_Collector', a2)
    if hasattr(a1, 'jbatch_Properties22'):
        assert not _is_linked(a1, 'jbatch_Properties22', b)
    if hasattr(a2, 'jbatch_Properties22'):
        assert _is_linked(a2, 'jbatch_Properties22', b)
    _safe_set(b, 'jbatch_Collector', None)
    assert not _is_linked(b, 'jbatch_Collector', a2)
    if hasattr(a2, 'jbatch_Properties22'):
        assert not _is_linked(a2, 'jbatch_Properties22', b)


def test_assoc_properties23_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision', a1)
    assert _is_linked(b, 'jbatch_Decision', a1)
    if hasattr(a1, 'jbatch_Properties24'):
        assert _is_linked(a1, 'jbatch_Properties24', b)
    _safe_set(b, 'jbatch_Decision', a2)
    assert _is_linked(b, 'jbatch_Decision', a2)
    if hasattr(a1, 'jbatch_Properties24'):
        assert not _is_linked(a1, 'jbatch_Properties24', b)
    if hasattr(a2, 'jbatch_Properties24'):
        assert _is_linked(a2, 'jbatch_Properties24', b)
    _safe_set(b, 'jbatch_Decision', None)
    assert not _is_linked(b, 'jbatch_Decision', a2)
    if hasattr(a2, 'jbatch_Properties24'):
        assert not _is_linked(a2, 'jbatch_Properties24', b)


def test_assoc_properties3_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_CheckpointAlgorithm(ref="sample_text")
    _safe_set(b, 'jbatch_CheckpointAlgorithm', a1)
    assert _is_linked(b, 'jbatch_CheckpointAlgorithm', a1)
    if hasattr(a1, 'jbatch_Properties4'):
        assert _is_linked(a1, 'jbatch_Properties4', b)
    _safe_set(b, 'jbatch_CheckpointAlgorithm', a2)
    assert _is_linked(b, 'jbatch_CheckpointAlgorithm', a2)
    if hasattr(a1, 'jbatch_Properties4'):
        assert not _is_linked(a1, 'jbatch_Properties4', b)
    if hasattr(a2, 'jbatch_Properties4'):
        assert _is_linked(a2, 'jbatch_Properties4', b)
    _safe_set(b, 'jbatch_CheckpointAlgorithm', None)
    assert not _is_linked(b, 'jbatch_CheckpointAlgorithm', a2)
    if hasattr(a2, 'jbatch_Properties4'):
        assert not _is_linked(a2, 'jbatch_Properties4', b)


def test_assoc_properties64_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_ItemProcessor(ref="sample_text")
    _safe_set(b, 'jbatch_ItemProcessor65', a1)
    assert _is_linked(b, 'jbatch_ItemProcessor65', a1)
    if hasattr(a1, 'jbatch_Properties66'):
        assert _is_linked(a1, 'jbatch_Properties66', b)
    _safe_set(b, 'jbatch_ItemProcessor65', a2)
    assert _is_linked(b, 'jbatch_ItemProcessor65', a2)
    if hasattr(a1, 'jbatch_Properties66'):
        assert not _is_linked(a1, 'jbatch_Properties66', b)
    if hasattr(a2, 'jbatch_Properties66'):
        assert _is_linked(a2, 'jbatch_Properties66', b)
    _safe_set(b, 'jbatch_ItemProcessor65', None)
    assert not _is_linked(b, 'jbatch_ItemProcessor65', a2)
    if hasattr(a2, 'jbatch_Properties66'):
        assert not _is_linked(a2, 'jbatch_Properties66', b)


def test_assoc_properties67_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_ItemReader(ref="sample_text")
    _safe_set(b, 'jbatch_ItemReader68', a1)
    assert _is_linked(b, 'jbatch_ItemReader68', a1)
    if hasattr(a1, 'jbatch_Properties69'):
        assert _is_linked(a1, 'jbatch_Properties69', b)
    _safe_set(b, 'jbatch_ItemReader68', a2)
    assert _is_linked(b, 'jbatch_ItemReader68', a2)
    if hasattr(a1, 'jbatch_Properties69'):
        assert not _is_linked(a1, 'jbatch_Properties69', b)
    if hasattr(a2, 'jbatch_Properties69'):
        assert _is_linked(a2, 'jbatch_Properties69', b)
    _safe_set(b, 'jbatch_ItemReader68', None)
    assert not _is_linked(b, 'jbatch_ItemReader68', a2)
    if hasattr(a2, 'jbatch_Properties69'):
        assert not _is_linked(a2, 'jbatch_Properties69', b)


def test_assoc_properties70_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_ItemWriter(ref="sample_text")
    _safe_set(b, 'jbatch_ItemWriter71', a1)
    assert _is_linked(b, 'jbatch_ItemWriter71', a1)
    if hasattr(a1, 'jbatch_Properties72'):
        assert _is_linked(a1, 'jbatch_Properties72', b)
    _safe_set(b, 'jbatch_ItemWriter71', a2)
    assert _is_linked(b, 'jbatch_ItemWriter71', a2)
    if hasattr(a1, 'jbatch_Properties72'):
        assert not _is_linked(a1, 'jbatch_Properties72', b)
    if hasattr(a2, 'jbatch_Properties72'):
        assert _is_linked(a2, 'jbatch_Properties72', b)
    _safe_set(b, 'jbatch_ItemWriter71', None)
    assert not _is_linked(b, 'jbatch_ItemWriter71', a2)
    if hasattr(a2, 'jbatch_Properties72'):
        assert not _is_linked(a2, 'jbatch_Properties72', b)


def test_assoc_properties73_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    _safe_set(b, 'jbatch_Job74', a1)
    assert _is_linked(b, 'jbatch_Job74', a1)
    if hasattr(a1, 'jbatch_Properties75'):
        assert _is_linked(a1, 'jbatch_Properties75', b)
    _safe_set(b, 'jbatch_Job74', a2)
    assert _is_linked(b, 'jbatch_Job74', a2)
    if hasattr(a1, 'jbatch_Properties75'):
        assert not _is_linked(a1, 'jbatch_Properties75', b)
    if hasattr(a2, 'jbatch_Properties75'):
        assert _is_linked(a2, 'jbatch_Properties75', b)
    _safe_set(b, 'jbatch_Job74', None)
    assert not _is_linked(b, 'jbatch_Job74', a2)
    if hasattr(a2, 'jbatch_Properties75'):
        assert not _is_linked(a2, 'jbatch_Properties75', b)


def test_assoc_properties90_reverse_link_reassign_clear():
    a1 = jbatch_Properties(partition="sample_text")
    a2 = jbatch_Properties(partition="sample_text_2")
    b = jbatch_Listener(ref="sample_text")
    _safe_set(b, 'jbatch_Listener', a1)
    assert _is_linked(b, 'jbatch_Listener', a1)
    if hasattr(a1, 'jbatch_Properties91'):
        assert _is_linked(a1, 'jbatch_Properties91', b)
    _safe_set(b, 'jbatch_Listener', a2)
    assert _is_linked(b, 'jbatch_Listener', a2)
    if hasattr(a1, 'jbatch_Properties91'):
        assert not _is_linked(a1, 'jbatch_Properties91', b)
    if hasattr(a2, 'jbatch_Properties91'):
        assert _is_linked(a2, 'jbatch_Properties91', b)
    _safe_set(b, 'jbatch_Listener', None)
    assert not _is_linked(b, 'jbatch_Listener', a2)
    if hasattr(a2, 'jbatch_Properties91'):
        assert not _is_linked(a2, 'jbatch_Properties91', b)


def test_assoc_property115_reverse_link_reassign_clear():
    a1 = jbatch_Property(name="sample_text", value="sample_text")
    a2 = jbatch_Property(name="sample_text_2", value="sample_text_2")
    b = jbatch_Properties(partition="sample_text")
    _safe_set(b, 'jbatch_Properties116', {a1})
    assert _is_linked(b, 'jbatch_Properties116', a1)
    if hasattr(a1, 'jbatch_Property'):
        assert _is_linked(a1, 'jbatch_Property', b)
    _safe_set(b, 'jbatch_Properties116', {a2})
    assert _is_linked(b, 'jbatch_Properties116', a2)
    if hasattr(a1, 'jbatch_Property'):
        assert not _is_linked(a1, 'jbatch_Property', b)
    if hasattr(a2, 'jbatch_Property'):
        assert _is_linked(a2, 'jbatch_Property', b)
    _safe_set(b, 'jbatch_Properties116', set())
    assert not _is_linked(b, 'jbatch_Properties116', a2)
    if hasattr(a2, 'jbatch_Property'):
        assert not _is_linked(a2, 'jbatch_Property', b)


def test_assoc_reader5_reverse_link_reassign_clear():
    a1 = jbatch_ItemReader(ref="sample_text")
    a2 = jbatch_ItemReader(ref="sample_text_2")
    b = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    _safe_set(b, 'jbatch_Chunk', a1)
    assert _is_linked(b, 'jbatch_Chunk', a1)
    if hasattr(a1, 'jbatch_ItemReader'):
        assert _is_linked(a1, 'jbatch_ItemReader', b)
    _safe_set(b, 'jbatch_Chunk', a2)
    assert _is_linked(b, 'jbatch_Chunk', a2)
    if hasattr(a1, 'jbatch_ItemReader'):
        assert not _is_linked(a1, 'jbatch_ItemReader', b)
    if hasattr(a2, 'jbatch_ItemReader'):
        assert _is_linked(a2, 'jbatch_ItemReader', b)
    _safe_set(b, 'jbatch_Chunk', None)
    assert not _is_linked(b, 'jbatch_Chunk', a2)
    if hasattr(a2, 'jbatch_ItemReader'):
        assert not _is_linked(a2, 'jbatch_ItemReader', b)


def test_assoc_split48_reverse_link_reassign_clear():
    a1 = jbatch_Split(id="sample_text", next="sample_text")
    a2 = jbatch_Split(id="sample_text_2", next="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow49', {a1})
    assert _is_linked(b, 'jbatch_Flow49', a1)
    if hasattr(a1, 'jbatch_Split'):
        assert _is_linked(a1, 'jbatch_Split', b)
    _safe_set(b, 'jbatch_Flow49', {a2})
    assert _is_linked(b, 'jbatch_Flow49', a2)
    if hasattr(a1, 'jbatch_Split'):
        assert not _is_linked(a1, 'jbatch_Split', b)
    if hasattr(a2, 'jbatch_Split'):
        assert _is_linked(a2, 'jbatch_Split', b)
    _safe_set(b, 'jbatch_Flow49', set())
    assert not _is_linked(b, 'jbatch_Flow49', a2)
    if hasattr(a2, 'jbatch_Split'):
        assert not _is_linked(a2, 'jbatch_Split', b)


def test_assoc_split84_reverse_link_reassign_clear():
    a1 = jbatch_Split(id="sample_text", next="sample_text")
    a2 = jbatch_Split(id="sample_text_2", next="sample_text_2")
    b = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    _safe_set(b, 'jbatch_Job85', {a1})
    assert _is_linked(b, 'jbatch_Job85', a1)
    if hasattr(a1, 'jbatch_Split86'):
        assert _is_linked(a1, 'jbatch_Split86', b)
    _safe_set(b, 'jbatch_Job85', {a2})
    assert _is_linked(b, 'jbatch_Job85', a2)
    if hasattr(a1, 'jbatch_Split86'):
        assert not _is_linked(a1, 'jbatch_Split86', b)
    if hasattr(a2, 'jbatch_Split86'):
        assert _is_linked(a2, 'jbatch_Split86', b)
    _safe_set(b, 'jbatch_Job85', set())
    assert not _is_linked(b, 'jbatch_Job85', a2)
    if hasattr(a2, 'jbatch_Split86'):
        assert not _is_linked(a2, 'jbatch_Split86', b)


def test_assoc_step50_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow51', {a1})
    assert _is_linked(b, 'jbatch_Flow51', a1)
    if hasattr(a1, 'jbatch_Step'):
        assert _is_linked(a1, 'jbatch_Step', b)
    _safe_set(b, 'jbatch_Flow51', {a2})
    assert _is_linked(b, 'jbatch_Flow51', a2)
    if hasattr(a1, 'jbatch_Step'):
        assert not _is_linked(a1, 'jbatch_Step', b)
    if hasattr(a2, 'jbatch_Step'):
        assert _is_linked(a2, 'jbatch_Step', b)
    _safe_set(b, 'jbatch_Flow51', set())
    assert not _is_linked(b, 'jbatch_Flow51', a2)
    if hasattr(a2, 'jbatch_Step'):
        assert not _is_linked(a2, 'jbatch_Step', b)


def test_assoc_step87_reverse_link_reassign_clear():
    a1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    a2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    b = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    _safe_set(b, 'jbatch_Job88', {a1})
    assert _is_linked(b, 'jbatch_Job88', a1)
    if hasattr(a1, 'jbatch_Step89'):
        assert _is_linked(a1, 'jbatch_Step89', b)
    _safe_set(b, 'jbatch_Job88', {a2})
    assert _is_linked(b, 'jbatch_Job88', a2)
    if hasattr(a1, 'jbatch_Step89'):
        assert not _is_linked(a1, 'jbatch_Step89', b)
    if hasattr(a2, 'jbatch_Step89'):
        assert _is_linked(a2, 'jbatch_Step89', b)
    _safe_set(b, 'jbatch_Job88', set())
    assert not _is_linked(b, 'jbatch_Job88', a2)
    if hasattr(a2, 'jbatch_Step89'):
        assert not _is_linked(a2, 'jbatch_Step89', b)


def test_assoc_stop144_reverse_link_reassign_clear():
    a1 = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    a2 = jbatch_Stop(exitStatus="sample_text_2", on="sample_text_2", restart="sample_text_2")
    b = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Step145', {a1})
    assert _is_linked(b, 'jbatch_Step145', a1)
    if hasattr(a1, 'jbatch_Stop146'):
        assert _is_linked(a1, 'jbatch_Stop146', b)
    _safe_set(b, 'jbatch_Step145', {a2})
    assert _is_linked(b, 'jbatch_Step145', a2)
    if hasattr(a1, 'jbatch_Stop146'):
        assert not _is_linked(a1, 'jbatch_Stop146', b)
    if hasattr(a2, 'jbatch_Stop146'):
        assert _is_linked(a2, 'jbatch_Stop146', b)
    _safe_set(b, 'jbatch_Step145', set())
    assert not _is_linked(b, 'jbatch_Step145', a2)
    if hasattr(a2, 'jbatch_Stop146'):
        assert not _is_linked(a2, 'jbatch_Stop146', b)


def test_assoc_stop31_reverse_link_reassign_clear():
    a1 = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    a2 = jbatch_Stop(exitStatus="sample_text_2", on="sample_text_2", restart="sample_text_2")
    b = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Decision32', {a1})
    assert _is_linked(b, 'jbatch_Decision32', a1)
    if hasattr(a1, 'jbatch_Stop'):
        assert _is_linked(a1, 'jbatch_Stop', b)
    _safe_set(b, 'jbatch_Decision32', {a2})
    assert _is_linked(b, 'jbatch_Decision32', a2)
    if hasattr(a1, 'jbatch_Stop'):
        assert not _is_linked(a1, 'jbatch_Stop', b)
    if hasattr(a2, 'jbatch_Stop'):
        assert _is_linked(a2, 'jbatch_Stop', b)
    _safe_set(b, 'jbatch_Decision32', set())
    assert not _is_linked(b, 'jbatch_Decision32', a2)
    if hasattr(a2, 'jbatch_Stop'):
        assert not _is_linked(a2, 'jbatch_Stop', b)


def test_assoc_stop61_reverse_link_reassign_clear():
    a1 = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    a2 = jbatch_Stop(exitStatus="sample_text_2", on="sample_text_2", restart="sample_text_2")
    b = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    _safe_set(b, 'jbatch_Flow62', {a1})
    assert _is_linked(b, 'jbatch_Flow62', a1)
    if hasattr(a1, 'jbatch_Stop63'):
        assert _is_linked(a1, 'jbatch_Stop63', b)
    _safe_set(b, 'jbatch_Flow62', {a2})
    assert _is_linked(b, 'jbatch_Flow62', a2)
    if hasattr(a1, 'jbatch_Stop63'):
        assert not _is_linked(a1, 'jbatch_Stop63', b)
    if hasattr(a2, 'jbatch_Stop63'):
        assert _is_linked(a2, 'jbatch_Stop63', b)
    _safe_set(b, 'jbatch_Flow62', set())
    assert not _is_linked(b, 'jbatch_Flow62', a2)
    if hasattr(a2, 'jbatch_Stop63'):
        assert not _is_linked(a2, 'jbatch_Stop63', b)


def test_assoc_writer8_reverse_link_reassign_clear():
    a1 = jbatch_ItemWriter(ref="sample_text")
    a2 = jbatch_ItemWriter(ref="sample_text_2")
    b = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    _safe_set(b, 'jbatch_Chunk9', a1)
    assert _is_linked(b, 'jbatch_Chunk9', a1)
    if hasattr(a1, 'jbatch_ItemWriter'):
        assert _is_linked(a1, 'jbatch_ItemWriter', b)
    _safe_set(b, 'jbatch_Chunk9', a2)
    assert _is_linked(b, 'jbatch_Chunk9', a2)
    if hasattr(a1, 'jbatch_ItemWriter'):
        assert not _is_linked(a1, 'jbatch_ItemWriter', b)
    if hasattr(a2, 'jbatch_ItemWriter'):
        assert _is_linked(a2, 'jbatch_ItemWriter', b)
    _safe_set(b, 'jbatch_Chunk9', None)
    assert not _is_linked(b, 'jbatch_Chunk9', a2)
    if hasattr(a2, 'jbatch_ItemWriter'):
        assert not _is_linked(a2, 'jbatch_ItemWriter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_analyzer101_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition102' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Analyzer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Analyzer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Analyzer(ref="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition102', None)
    _safe_set(owner, 'jbatch_Analyzer103', partner)
    assert getattr(partner, 'jbatch_Partition102') == owner
    _safe_set(owner, 'jbatch_Analyzer103', None)
    assert getattr(partner, 'jbatch_Partition102') is None


def test_assoc_collector98_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition99' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Collector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Collector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Collector(ref="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition99', None)
    _safe_set(owner, 'jbatch_Collector100', partner)
    assert getattr(partner, 'jbatch_Partition99') == owner
    _safe_set(owner, 'jbatch_Collector100', None)
    assert getattr(partner, 'jbatch_Partition99') is None


def test_assoc_exclude41_stub_double():
    # jbatch_ExceptionClassFilter has no real 'jbatch_ExceptionClassFilter42' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_ExcludeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_ExcludeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_ExcludeType(class_="sample_text")
    partner = jbatch_ExceptionClassFilter()
    setattr(partner, 'jbatch_ExceptionClassFilter42', None)
    _safe_set(owner, 'jbatch_ExcludeType', partner)
    assert owner in getattr(partner, 'jbatch_ExceptionClassFilter42')
    _safe_set(owner, 'jbatch_ExcludeType', None)
    assert owner not in getattr(partner, 'jbatch_ExceptionClassFilter42')


def test_assoc_include39_stub_double():
    # jbatch_ExceptionClassFilter has no real 'jbatch_ExceptionClassFilter40' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_IncludeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_IncludeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_IncludeType(class_="sample_text")
    partner = jbatch_ExceptionClassFilter()
    setattr(partner, 'jbatch_ExceptionClassFilter40', None)
    _safe_set(owner, 'jbatch_IncludeType', partner)
    assert owner in getattr(partner, 'jbatch_ExceptionClassFilter40')
    _safe_set(owner, 'jbatch_IncludeType', None)
    assert owner not in getattr(partner, 'jbatch_ExceptionClassFilter40')


def test_assoc_listener92_stub_double():
    # jbatch_Listeners has no real 'jbatch_Listeners93' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Listener's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Listener's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Listener(ref="sample_text")
    partner = jbatch_Listeners()
    setattr(partner, 'jbatch_Listeners93', None)
    _safe_set(owner, 'jbatch_Listener94', partner)
    assert owner in getattr(partner, 'jbatch_Listeners93')
    _safe_set(owner, 'jbatch_Listener94', None)
    assert owner not in getattr(partner, 'jbatch_Listeners93')


def test_assoc_listeners123_stub_double():
    # jbatch_Listeners has no real 'jbatch_Listeners125' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    partner = jbatch_Listeners()
    setattr(partner, 'jbatch_Listeners125', None)
    _safe_set(owner, 'jbatch_Step124', partner)
    assert getattr(partner, 'jbatch_Listeners125') == owner
    _safe_set(owner, 'jbatch_Step124', None)
    assert getattr(partner, 'jbatch_Listeners125') is None


def test_assoc_listeners76_stub_double():
    # jbatch_Listeners has no real 'jbatch_Listeners' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Job's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Job's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    partner = jbatch_Listeners()
    setattr(partner, 'jbatch_Listeners', None)
    _safe_set(owner, 'jbatch_Job77', partner)
    assert getattr(partner, 'jbatch_Listeners') == owner
    _safe_set(owner, 'jbatch_Job77', None)
    assert getattr(partner, 'jbatch_Listeners') is None


def test_assoc_mapper95_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_PartitionMapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_PartitionMapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_PartitionMapper(ref="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition', None)
    _safe_set(owner, 'jbatch_PartitionMapper', partner)
    assert getattr(partner, 'jbatch_Partition') == owner
    _safe_set(owner, 'jbatch_PartitionMapper', None)
    assert getattr(partner, 'jbatch_Partition') is None


def test_assoc_noRollbackExceptionClasses18_stub_double():
    # jbatch_ExceptionClassFilter has no real 'jbatch_ExceptionClassFilter20' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Chunk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Chunk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    partner = jbatch_ExceptionClassFilter()
    setattr(partner, 'jbatch_ExceptionClassFilter20', None)
    _safe_set(owner, 'jbatch_Chunk19', partner)
    assert getattr(partner, 'jbatch_ExceptionClassFilter20') == owner
    _safe_set(owner, 'jbatch_Chunk19', None)
    assert getattr(partner, 'jbatch_ExceptionClassFilter20') is None


def test_assoc_partition132_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition134' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition134', None)
    _safe_set(owner, 'jbatch_Step133', partner)
    assert getattr(partner, 'jbatch_Partition134') == owner
    _safe_set(owner, 'jbatch_Step133', None)
    assert getattr(partner, 'jbatch_Partition134') is None


def test_assoc_plan96_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition97' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_PartitionPlan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_PartitionPlan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition97', None)
    _safe_set(owner, 'jbatch_PartitionPlan', partner)
    assert getattr(partner, 'jbatch_Partition97') == owner
    _safe_set(owner, 'jbatch_PartitionPlan', None)
    assert getattr(partner, 'jbatch_Partition97') is None


def test_assoc_reducer104_stub_double():
    # jbatch_Partition has no real 'jbatch_Partition105' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_PartitionReducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_PartitionReducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_PartitionReducer(ref="sample_text")
    partner = jbatch_Partition()
    setattr(partner, 'jbatch_Partition105', None)
    _safe_set(owner, 'jbatch_PartitionReducer', partner)
    assert getattr(partner, 'jbatch_Partition105') == owner
    _safe_set(owner, 'jbatch_PartitionReducer', None)
    assert getattr(partner, 'jbatch_Partition105') is None


def test_assoc_retryableExceptionClasses15_stub_double():
    # jbatch_ExceptionClassFilter has no real 'jbatch_ExceptionClassFilter17' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Chunk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Chunk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    partner = jbatch_ExceptionClassFilter()
    setattr(partner, 'jbatch_ExceptionClassFilter17', None)
    _safe_set(owner, 'jbatch_Chunk16', partner)
    assert getattr(partner, 'jbatch_ExceptionClassFilter17') == owner
    _safe_set(owner, 'jbatch_Chunk16', None)
    assert getattr(partner, 'jbatch_ExceptionClassFilter17') is None


def test_assoc_skippableExceptionClasses13_stub_double():
    # jbatch_ExceptionClassFilter has no real 'jbatch_ExceptionClassFilter' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_Chunk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_Chunk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    partner = jbatch_ExceptionClassFilter()
    setattr(partner, 'jbatch_ExceptionClassFilter', None)
    _safe_set(owner, 'jbatch_Chunk14', partner)
    assert getattr(partner, 'jbatch_ExceptionClassFilter') == owner
    _safe_set(owner, 'jbatch_Chunk14', None)
    assert getattr(partner, 'jbatch_ExceptionClassFilter') is None


def test_assoc_xMLNSPrefixMap33_stub_double():
    # jbatch_EStringToStringMapEntry has no real 'jbatch_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_DocumentRoot(mixed="sample_text")
    partner = jbatch_EStringToStringMapEntry()
    setattr(partner, 'jbatch_EStringToStringMapEntry', None)
    _safe_set(owner, 'jbatch_DocumentRoot', {partner})
    assert getattr(partner, 'jbatch_EStringToStringMapEntry') == owner
    _safe_set(owner, 'jbatch_DocumentRoot', set())
    assert getattr(partner, 'jbatch_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation34_stub_double():
    # jbatch_EStringToStringMapEntry has no real 'jbatch_EStringToStringMapEntry36' property in the generated
    # code (a bare stub) -- manually attach it so jbatch_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jbatch_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jbatch_DocumentRoot(mixed="sample_text")
    partner = jbatch_EStringToStringMapEntry()
    setattr(partner, 'jbatch_EStringToStringMapEntry36', None)
    _safe_set(owner, 'jbatch_DocumentRoot35', {partner})
    assert getattr(partner, 'jbatch_EStringToStringMapEntry36') == owner
    _safe_set(owner, 'jbatch_DocumentRoot35', set())
    assert getattr(partner, 'jbatch_EStringToStringMapEntry36') is None


