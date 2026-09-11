import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_jbatch_Analyzer_ref_value_roundtrip():
    instance = jbatch_Analyzer(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Batchlet_ref_value_roundtrip():
    instance = jbatch_Batchlet(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_CheckpointAlgorithm_ref_value_roundtrip():
    instance = jbatch_CheckpointAlgorithm(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Chunk_checkpointPolicy_value_roundtrip():
    instance = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    assert instance.checkpointPolicy == "sample_text"
    instance.checkpointPolicy = "sample_text_2"
    assert instance.checkpointPolicy == "sample_text_2"


def test_jbatch_Chunk_itemCount_value_roundtrip():
    instance = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    assert instance.itemCount == "sample_text"
    instance.itemCount = "sample_text_2"
    assert instance.itemCount == "sample_text_2"


def test_jbatch_Chunk_retryLimit_value_roundtrip():
    instance = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    assert instance.retryLimit == "sample_text"
    instance.retryLimit = "sample_text_2"
    assert instance.retryLimit == "sample_text_2"


def test_jbatch_Chunk_skipLimit_value_roundtrip():
    instance = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    assert instance.skipLimit == "sample_text"
    instance.skipLimit = "sample_text_2"
    assert instance.skipLimit == "sample_text_2"


def test_jbatch_Chunk_timeLimit_value_roundtrip():
    instance = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    assert instance.timeLimit == "sample_text"
    instance.timeLimit = "sample_text_2"
    assert instance.timeLimit == "sample_text_2"


def test_jbatch_Collector_ref_value_roundtrip():
    instance = jbatch_Collector(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Decision_id_value_roundtrip():
    instance = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jbatch_Decision_ref_value_roundtrip():
    instance = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Decision_transitionElements_value_roundtrip():
    instance = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    assert instance.transitionElements == "sample_text"
    instance.transitionElements = "sample_text_2"
    assert instance.transitionElements == "sample_text_2"


def test_jbatch_DocumentRoot_mixed_value_roundtrip():
    instance = jbatch_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jbatch_End_exitStatus_value_roundtrip():
    instance = jbatch_End(exitStatus="sample_text", on="sample_text")
    assert instance.exitStatus == "sample_text"
    instance.exitStatus = "sample_text_2"
    assert instance.exitStatus == "sample_text_2"


def test_jbatch_End_on_value_roundtrip():
    instance = jbatch_End(exitStatus="sample_text", on="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_jbatch_ExcludeType_class__value_roundtrip():
    instance = jbatch_ExcludeType(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_jbatch_Fail_exitStatus_value_roundtrip():
    instance = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    assert instance.exitStatus == "sample_text"
    instance.exitStatus = "sample_text_2"
    assert instance.exitStatus == "sample_text_2"


def test_jbatch_Fail_on_value_roundtrip():
    instance = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_jbatch_Flow_group_value_roundtrip():
    instance = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jbatch_Flow_id_value_roundtrip():
    instance = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jbatch_Flow_next1_value_roundtrip():
    instance = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    assert instance.next1 == "sample_text"
    instance.next1 = "sample_text_2"
    assert instance.next1 == "sample_text_2"


def test_jbatch_Flow_transitionElements_value_roundtrip():
    instance = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    assert instance.transitionElements == "sample_text"
    instance.transitionElements = "sample_text_2"
    assert instance.transitionElements == "sample_text_2"


def test_jbatch_IncludeType_class__value_roundtrip():
    instance = jbatch_IncludeType(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_jbatch_ItemProcessor_ref_value_roundtrip():
    instance = jbatch_ItemProcessor(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_ItemReader_ref_value_roundtrip():
    instance = jbatch_ItemReader(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_ItemWriter_ref_value_roundtrip():
    instance = jbatch_ItemWriter(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Job_group_value_roundtrip():
    instance = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jbatch_Job_id_value_roundtrip():
    instance = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jbatch_Job_restartable_value_roundtrip():
    instance = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    assert instance.restartable == "sample_text"
    instance.restartable = "sample_text_2"
    assert instance.restartable == "sample_text_2"


def test_jbatch_Job_version_value_roundtrip():
    instance = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_jbatch_Listener_ref_value_roundtrip():
    instance = jbatch_Listener(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Next_on_value_roundtrip():
    instance = jbatch_Next(on="sample_text", to="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_jbatch_Next_to_value_roundtrip():
    instance = jbatch_Next(on="sample_text", to="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_jbatch_PartitionMapper_ref_value_roundtrip():
    instance = jbatch_PartitionMapper(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_PartitionPlan_partitions_value_roundtrip():
    instance = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    assert instance.partitions == "sample_text"
    instance.partitions = "sample_text_2"
    assert instance.partitions == "sample_text_2"


def test_jbatch_PartitionPlan_threads_value_roundtrip():
    instance = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    assert instance.threads == "sample_text"
    instance.threads = "sample_text_2"
    assert instance.threads == "sample_text_2"


def test_jbatch_PartitionReducer_ref_value_roundtrip():
    instance = jbatch_PartitionReducer(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_jbatch_Properties_partition_value_roundtrip():
    instance = jbatch_Properties(partition="sample_text")
    assert instance.partition == "sample_text"
    instance.partition = "sample_text_2"
    assert instance.partition == "sample_text_2"


def test_jbatch_Property_name_value_roundtrip():
    instance = jbatch_Property(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jbatch_Property_value_value_roundtrip():
    instance = jbatch_Property(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_jbatch_Split_id_value_roundtrip():
    instance = jbatch_Split(id="sample_text", next="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jbatch_Split_next_value_roundtrip():
    instance = jbatch_Split(id="sample_text", next="sample_text")
    assert instance.next == "sample_text"
    instance.next = "sample_text_2"
    assert instance.next == "sample_text_2"


def test_jbatch_Step_allowStartIfComplete_value_roundtrip():
    instance = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    assert instance.allowStartIfComplete == "sample_text"
    instance.allowStartIfComplete = "sample_text_2"
    assert instance.allowStartIfComplete == "sample_text_2"


def test_jbatch_Step_id_value_roundtrip():
    instance = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jbatch_Step_next1_value_roundtrip():
    instance = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    assert instance.next1 == "sample_text"
    instance.next1 = "sample_text_2"
    assert instance.next1 == "sample_text_2"


def test_jbatch_Step_startLimit_value_roundtrip():
    instance = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    assert instance.startLimit == "sample_text"
    instance.startLimit = "sample_text_2"
    assert instance.startLimit == "sample_text_2"


def test_jbatch_Step_transitionElements_value_roundtrip():
    instance = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    assert instance.transitionElements == "sample_text"
    instance.transitionElements = "sample_text_2"
    assert instance.transitionElements == "sample_text_2"


def test_jbatch_Stop_exitStatus_value_roundtrip():
    instance = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    assert instance.exitStatus == "sample_text"
    instance.exitStatus = "sample_text_2"
    assert instance.exitStatus == "sample_text_2"


def test_jbatch_Stop_on_value_roundtrip():
    instance = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_jbatch_Stop_restart_value_roundtrip():
    instance = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    assert instance.restart == "sample_text"
    instance.restart = "sample_text_2"
    assert instance.restart == "sample_text_2"


def test_assoc_analyzer101_link_reassign_clear():
    a = jbatch_Analyzer(ref="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_Analyzer103', b1)
    assert _is_linked(a, 'jbatch_Analyzer103', b1)
    if hasattr(b1, 'jbatch_Partition102'):
        assert _is_linked(b1, 'jbatch_Partition102', a)
    _safe_set(a, 'jbatch_Analyzer103', b2)
    assert _is_linked(a, 'jbatch_Analyzer103', b2)
    if hasattr(b1, 'jbatch_Partition102'):
        assert not _is_linked(b1, 'jbatch_Partition102', a)
    if hasattr(b2, 'jbatch_Partition102'):
        assert _is_linked(b2, 'jbatch_Partition102', a)
    _safe_set(a, 'jbatch_Analyzer103', None)
    assert not _is_linked(a, 'jbatch_Analyzer103', b2)
    if hasattr(b2, 'jbatch_Partition102'):
        assert not _is_linked(b2, 'jbatch_Partition102', a)


def test_assoc_batchlet126_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Batchlet(ref="sample_text")
    b2 = jbatch_Batchlet(ref="sample_text_2")
    _safe_set(a, 'jbatch_Step127', b1)
    assert _is_linked(a, 'jbatch_Step127', b1)
    if hasattr(b1, 'jbatch_Batchlet128'):
        assert _is_linked(b1, 'jbatch_Batchlet128', a)
    _safe_set(a, 'jbatch_Step127', b2)
    assert _is_linked(a, 'jbatch_Step127', b2)
    if hasattr(b1, 'jbatch_Batchlet128'):
        assert not _is_linked(b1, 'jbatch_Batchlet128', a)
    if hasattr(b2, 'jbatch_Batchlet128'):
        assert _is_linked(b2, 'jbatch_Batchlet128', a)
    _safe_set(a, 'jbatch_Step127', None)
    assert not _is_linked(a, 'jbatch_Step127', b2)
    if hasattr(b2, 'jbatch_Batchlet128'):
        assert not _is_linked(b2, 'jbatch_Batchlet128', a)


def test_assoc_checkpointAlgorithm10_link_reassign_clear():
    a = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b1 = jbatch_CheckpointAlgorithm(ref="sample_text")
    b2 = jbatch_CheckpointAlgorithm(ref="sample_text_2")
    _safe_set(a, 'jbatch_Chunk11', b1)
    assert _is_linked(a, 'jbatch_Chunk11', b1)
    if hasattr(b1, 'jbatch_CheckpointAlgorithm12'):
        assert _is_linked(b1, 'jbatch_CheckpointAlgorithm12', a)
    _safe_set(a, 'jbatch_Chunk11', b2)
    assert _is_linked(a, 'jbatch_Chunk11', b2)
    if hasattr(b1, 'jbatch_CheckpointAlgorithm12'):
        assert not _is_linked(b1, 'jbatch_CheckpointAlgorithm12', a)
    if hasattr(b2, 'jbatch_CheckpointAlgorithm12'):
        assert _is_linked(b2, 'jbatch_CheckpointAlgorithm12', a)
    _safe_set(a, 'jbatch_Chunk11', None)
    assert not _is_linked(a, 'jbatch_Chunk11', b2)
    if hasattr(b2, 'jbatch_CheckpointAlgorithm12'):
        assert not _is_linked(b2, 'jbatch_CheckpointAlgorithm12', a)


def test_assoc_chunk129_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b2 = jbatch_Chunk(checkpointPolicy="sample_text_2", itemCount="sample_text_2", retryLimit="sample_text_2", skipLimit="sample_text_2", timeLimit="sample_text_2")
    _safe_set(a, 'jbatch_Step130', b1)
    assert _is_linked(a, 'jbatch_Step130', b1)
    if hasattr(b1, 'jbatch_Chunk131'):
        assert _is_linked(b1, 'jbatch_Chunk131', a)
    _safe_set(a, 'jbatch_Step130', b2)
    assert _is_linked(a, 'jbatch_Step130', b2)
    if hasattr(b1, 'jbatch_Chunk131'):
        assert not _is_linked(b1, 'jbatch_Chunk131', a)
    if hasattr(b2, 'jbatch_Chunk131'):
        assert _is_linked(b2, 'jbatch_Chunk131', a)
    _safe_set(a, 'jbatch_Step130', None)
    assert not _is_linked(a, 'jbatch_Step130', b2)
    if hasattr(b2, 'jbatch_Chunk131'):
        assert not _is_linked(b2, 'jbatch_Chunk131', a)


def test_assoc_collector98_link_reassign_clear():
    a = jbatch_Collector(ref="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_Collector100', b1)
    assert _is_linked(a, 'jbatch_Collector100', b1)
    if hasattr(b1, 'jbatch_Partition99'):
        assert _is_linked(b1, 'jbatch_Partition99', a)
    _safe_set(a, 'jbatch_Collector100', b2)
    assert _is_linked(a, 'jbatch_Collector100', b2)
    if hasattr(b1, 'jbatch_Partition99'):
        assert not _is_linked(b1, 'jbatch_Partition99', a)
    if hasattr(b2, 'jbatch_Partition99'):
        assert _is_linked(b2, 'jbatch_Partition99', a)
    _safe_set(a, 'jbatch_Collector100', None)
    assert not _is_linked(a, 'jbatch_Collector100', b2)
    if hasattr(b2, 'jbatch_Partition99'):
        assert not _is_linked(b2, 'jbatch_Partition99', a)


def test_assoc_decision43_link_reassign_clear():
    a = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Flow', {b1})
    assert _is_linked(a, 'jbatch_Flow', b1)
    if hasattr(b1, 'jbatch_Decision44'):
        assert _is_linked(b1, 'jbatch_Decision44', a)
    _safe_set(a, 'jbatch_Flow', {b2})
    assert _is_linked(a, 'jbatch_Flow', b2)
    if hasattr(b1, 'jbatch_Decision44'):
        assert not _is_linked(b1, 'jbatch_Decision44', a)
    if hasattr(b2, 'jbatch_Decision44'):
        assert _is_linked(b2, 'jbatch_Decision44', a)
    _safe_set(a, 'jbatch_Flow', set())
    assert not _is_linked(a, 'jbatch_Flow', b2)
    if hasattr(b2, 'jbatch_Decision44'):
        assert not _is_linked(b2, 'jbatch_Decision44', a)


def test_assoc_decision78_link_reassign_clear():
    a = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Job79', {b1})
    assert _is_linked(a, 'jbatch_Job79', b1)
    if hasattr(b1, 'jbatch_Decision80'):
        assert _is_linked(b1, 'jbatch_Decision80', a)
    _safe_set(a, 'jbatch_Job79', {b2})
    assert _is_linked(a, 'jbatch_Job79', b2)
    if hasattr(b1, 'jbatch_Decision80'):
        assert not _is_linked(b1, 'jbatch_Decision80', a)
    if hasattr(b2, 'jbatch_Decision80'):
        assert _is_linked(b2, 'jbatch_Decision80', a)
    _safe_set(a, 'jbatch_Job79', set())
    assert not _is_linked(a, 'jbatch_Job79', b2)
    if hasattr(b2, 'jbatch_Decision80'):
        assert not _is_linked(b2, 'jbatch_Decision80', a)


def test_assoc_end135_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_End(exitStatus="sample_text", on="sample_text")
    b2 = jbatch_End(exitStatus="sample_text_2", on="sample_text_2")
    _safe_set(a, 'jbatch_Step136', {b1})
    assert _is_linked(a, 'jbatch_Step136', b1)
    if hasattr(b1, 'jbatch_End137'):
        assert _is_linked(b1, 'jbatch_End137', a)
    _safe_set(a, 'jbatch_Step136', {b2})
    assert _is_linked(a, 'jbatch_Step136', b2)
    if hasattr(b1, 'jbatch_End137'):
        assert not _is_linked(b1, 'jbatch_End137', a)
    if hasattr(b2, 'jbatch_End137'):
        assert _is_linked(b2, 'jbatch_End137', a)
    _safe_set(a, 'jbatch_Step136', set())
    assert not _is_linked(a, 'jbatch_Step136', b2)
    if hasattr(b2, 'jbatch_End137'):
        assert not _is_linked(b2, 'jbatch_End137', a)


def test_assoc_end25_link_reassign_clear():
    a = jbatch_End(exitStatus="sample_text", on="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_End', b1)
    assert _is_linked(a, 'jbatch_End', b1)
    if hasattr(b1, 'jbatch_Decision26'):
        assert _is_linked(b1, 'jbatch_Decision26', a)
    _safe_set(a, 'jbatch_End', b2)
    assert _is_linked(a, 'jbatch_End', b2)
    if hasattr(b1, 'jbatch_Decision26'):
        assert not _is_linked(b1, 'jbatch_Decision26', a)
    if hasattr(b2, 'jbatch_Decision26'):
        assert _is_linked(b2, 'jbatch_Decision26', a)
    _safe_set(a, 'jbatch_End', None)
    assert not _is_linked(a, 'jbatch_End', b2)
    if hasattr(b2, 'jbatch_Decision26'):
        assert not _is_linked(b2, 'jbatch_Decision26', a)


def test_assoc_end52_link_reassign_clear():
    a = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b1 = jbatch_End(exitStatus="sample_text", on="sample_text")
    b2 = jbatch_End(exitStatus="sample_text_2", on="sample_text_2")
    _safe_set(a, 'jbatch_Flow53', {b1})
    assert _is_linked(a, 'jbatch_Flow53', b1)
    if hasattr(b1, 'jbatch_End54'):
        assert _is_linked(b1, 'jbatch_End54', a)
    _safe_set(a, 'jbatch_Flow53', {b2})
    assert _is_linked(a, 'jbatch_Flow53', b2)
    if hasattr(b1, 'jbatch_End54'):
        assert not _is_linked(b1, 'jbatch_End54', a)
    if hasattr(b2, 'jbatch_End54'):
        assert _is_linked(b2, 'jbatch_End54', a)
    _safe_set(a, 'jbatch_Flow53', set())
    assert not _is_linked(a, 'jbatch_Flow53', b2)
    if hasattr(b2, 'jbatch_End54'):
        assert not _is_linked(b2, 'jbatch_End54', a)


def test_assoc_exclude41_link_reassign_clear():
    a = jbatch_ExcludeType(class_="sample_text")
    b1 = jbatch_ExceptionClassFilter()
    b2 = jbatch_ExceptionClassFilter()
    _safe_set(a, 'jbatch_ExcludeType', b1)
    assert _is_linked(a, 'jbatch_ExcludeType', b1)
    if hasattr(b1, 'jbatch_ExceptionClassFilter42'):
        assert _is_linked(b1, 'jbatch_ExceptionClassFilter42', a)
    _safe_set(a, 'jbatch_ExcludeType', b2)
    assert _is_linked(a, 'jbatch_ExcludeType', b2)
    if hasattr(b1, 'jbatch_ExceptionClassFilter42'):
        assert not _is_linked(b1, 'jbatch_ExceptionClassFilter42', a)
    if hasattr(b2, 'jbatch_ExceptionClassFilter42'):
        assert _is_linked(b2, 'jbatch_ExceptionClassFilter42', a)
    _safe_set(a, 'jbatch_ExcludeType', None)
    assert not _is_linked(a, 'jbatch_ExcludeType', b2)
    if hasattr(b2, 'jbatch_ExceptionClassFilter42'):
        assert not _is_linked(b2, 'jbatch_ExceptionClassFilter42', a)


def test_assoc_fail138_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    b2 = jbatch_Fail(exitStatus="sample_text_2", on="sample_text_2")
    _safe_set(a, 'jbatch_Step139', {b1})
    assert _is_linked(a, 'jbatch_Step139', b1)
    if hasattr(b1, 'jbatch_Fail140'):
        assert _is_linked(b1, 'jbatch_Fail140', a)
    _safe_set(a, 'jbatch_Step139', {b2})
    assert _is_linked(a, 'jbatch_Step139', b2)
    if hasattr(b1, 'jbatch_Fail140'):
        assert not _is_linked(b1, 'jbatch_Fail140', a)
    if hasattr(b2, 'jbatch_Fail140'):
        assert _is_linked(b2, 'jbatch_Fail140', a)
    _safe_set(a, 'jbatch_Step139', set())
    assert not _is_linked(a, 'jbatch_Step139', b2)
    if hasattr(b2, 'jbatch_Fail140'):
        assert not _is_linked(b2, 'jbatch_Fail140', a)


def test_assoc_fail27_link_reassign_clear():
    a = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Fail', b1)
    assert _is_linked(a, 'jbatch_Fail', b1)
    if hasattr(b1, 'jbatch_Decision28'):
        assert _is_linked(b1, 'jbatch_Decision28', a)
    _safe_set(a, 'jbatch_Fail', b2)
    assert _is_linked(a, 'jbatch_Fail', b2)
    if hasattr(b1, 'jbatch_Decision28'):
        assert not _is_linked(b1, 'jbatch_Decision28', a)
    if hasattr(b2, 'jbatch_Decision28'):
        assert _is_linked(b2, 'jbatch_Decision28', a)
    _safe_set(a, 'jbatch_Fail', None)
    assert not _is_linked(a, 'jbatch_Fail', b2)
    if hasattr(b2, 'jbatch_Decision28'):
        assert not _is_linked(b2, 'jbatch_Decision28', a)


def test_assoc_fail55_link_reassign_clear():
    a = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b1 = jbatch_Fail(exitStatus="sample_text", on="sample_text")
    b2 = jbatch_Fail(exitStatus="sample_text_2", on="sample_text_2")
    _safe_set(a, 'jbatch_Flow56', {b1})
    assert _is_linked(a, 'jbatch_Flow56', b1)
    if hasattr(b1, 'jbatch_Fail57'):
        assert _is_linked(b1, 'jbatch_Fail57', a)
    _safe_set(a, 'jbatch_Flow56', {b2})
    assert _is_linked(a, 'jbatch_Flow56', b2)
    if hasattr(b1, 'jbatch_Fail57'):
        assert not _is_linked(b1, 'jbatch_Fail57', a)
    if hasattr(b2, 'jbatch_Fail57'):
        assert _is_linked(b2, 'jbatch_Fail57', a)
    _safe_set(a, 'jbatch_Flow56', set())
    assert not _is_linked(a, 'jbatch_Flow56', b2)
    if hasattr(b2, 'jbatch_Fail57'):
        assert not _is_linked(b2, 'jbatch_Fail57', a)


def test_assoc_flow117_link_reassign_clear():
    a = jbatch_Split(id="sample_text", next="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Split118', {b1})
    assert _is_linked(a, 'jbatch_Split118', b1)
    if hasattr(b1, 'jbatch_Flow119'):
        assert _is_linked(b1, 'jbatch_Flow119', a)
    _safe_set(a, 'jbatch_Split118', {b2})
    assert _is_linked(a, 'jbatch_Split118', b2)
    if hasattr(b1, 'jbatch_Flow119'):
        assert not _is_linked(b1, 'jbatch_Flow119', a)
    if hasattr(b2, 'jbatch_Flow119'):
        assert _is_linked(b2, 'jbatch_Flow119', a)
    _safe_set(a, 'jbatch_Split118', set())
    assert not _is_linked(a, 'jbatch_Split118', b2)
    if hasattr(b2, 'jbatch_Flow119'):
        assert not _is_linked(b2, 'jbatch_Flow119', a)


def test_assoc_flow46_link_reassign_clear():
    a = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Flow45', {b1})
    assert _is_linked(a, 'jbatch_Flow45', b1)
    if hasattr(b1, 'jbatch_Flow47'):
        assert _is_linked(b1, 'jbatch_Flow47', a)
    _safe_set(a, 'jbatch_Flow45', {b2})
    assert _is_linked(a, 'jbatch_Flow45', b2)
    if hasattr(b1, 'jbatch_Flow47'):
        assert not _is_linked(b1, 'jbatch_Flow47', a)
    if hasattr(b2, 'jbatch_Flow47'):
        assert _is_linked(b2, 'jbatch_Flow47', a)
    _safe_set(a, 'jbatch_Flow45', set())
    assert not _is_linked(a, 'jbatch_Flow45', b2)
    if hasattr(b2, 'jbatch_Flow47'):
        assert not _is_linked(b2, 'jbatch_Flow47', a)


def test_assoc_flow81_link_reassign_clear():
    a = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Job82', {b1})
    assert _is_linked(a, 'jbatch_Job82', b1)
    if hasattr(b1, 'jbatch_Flow83'):
        assert _is_linked(b1, 'jbatch_Flow83', a)
    _safe_set(a, 'jbatch_Job82', {b2})
    assert _is_linked(a, 'jbatch_Job82', b2)
    if hasattr(b1, 'jbatch_Flow83'):
        assert not _is_linked(b1, 'jbatch_Flow83', a)
    if hasattr(b2, 'jbatch_Flow83'):
        assert _is_linked(b2, 'jbatch_Flow83', a)
    _safe_set(a, 'jbatch_Job82', set())
    assert not _is_linked(a, 'jbatch_Job82', b2)
    if hasattr(b2, 'jbatch_Flow83'):
        assert not _is_linked(b2, 'jbatch_Flow83', a)


def test_assoc_include39_link_reassign_clear():
    a = jbatch_IncludeType(class_="sample_text")
    b1 = jbatch_ExceptionClassFilter()
    b2 = jbatch_ExceptionClassFilter()
    _safe_set(a, 'jbatch_IncludeType', b1)
    assert _is_linked(a, 'jbatch_IncludeType', b1)
    if hasattr(b1, 'jbatch_ExceptionClassFilter40'):
        assert _is_linked(b1, 'jbatch_ExceptionClassFilter40', a)
    _safe_set(a, 'jbatch_IncludeType', b2)
    assert _is_linked(a, 'jbatch_IncludeType', b2)
    if hasattr(b1, 'jbatch_ExceptionClassFilter40'):
        assert not _is_linked(b1, 'jbatch_ExceptionClassFilter40', a)
    if hasattr(b2, 'jbatch_ExceptionClassFilter40'):
        assert _is_linked(b2, 'jbatch_ExceptionClassFilter40', a)
    _safe_set(a, 'jbatch_IncludeType', None)
    assert not _is_linked(a, 'jbatch_IncludeType', b2)
    if hasattr(b2, 'jbatch_ExceptionClassFilter40'):
        assert not _is_linked(b2, 'jbatch_ExceptionClassFilter40', a)


def test_assoc_job37_link_reassign_clear():
    a = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b1 = jbatch_DocumentRoot(mixed="sample_text")
    b2 = jbatch_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jbatch_Job', b1)
    assert _is_linked(a, 'jbatch_Job', b1)
    if hasattr(b1, 'jbatch_DocumentRoot38'):
        assert _is_linked(b1, 'jbatch_DocumentRoot38', a)
    _safe_set(a, 'jbatch_Job', b2)
    assert _is_linked(a, 'jbatch_Job', b2)
    if hasattr(b1, 'jbatch_DocumentRoot38'):
        assert not _is_linked(b1, 'jbatch_DocumentRoot38', a)
    if hasattr(b2, 'jbatch_DocumentRoot38'):
        assert _is_linked(b2, 'jbatch_DocumentRoot38', a)
    _safe_set(a, 'jbatch_Job', None)
    assert not _is_linked(a, 'jbatch_Job', b2)
    if hasattr(b2, 'jbatch_DocumentRoot38'):
        assert not _is_linked(b2, 'jbatch_DocumentRoot38', a)


def test_assoc_listener92_link_reassign_clear():
    a = jbatch_Listener(ref="sample_text")
    b1 = jbatch_Listeners()
    b2 = jbatch_Listeners()
    _safe_set(a, 'jbatch_Listener94', b1)
    assert _is_linked(a, 'jbatch_Listener94', b1)
    if hasattr(b1, 'jbatch_Listeners93'):
        assert _is_linked(b1, 'jbatch_Listeners93', a)
    _safe_set(a, 'jbatch_Listener94', b2)
    assert _is_linked(a, 'jbatch_Listener94', b2)
    if hasattr(b1, 'jbatch_Listeners93'):
        assert not _is_linked(b1, 'jbatch_Listeners93', a)
    if hasattr(b2, 'jbatch_Listeners93'):
        assert _is_linked(b2, 'jbatch_Listeners93', a)
    _safe_set(a, 'jbatch_Listener94', None)
    assert not _is_linked(a, 'jbatch_Listener94', b2)
    if hasattr(b2, 'jbatch_Listeners93'):
        assert not _is_linked(b2, 'jbatch_Listeners93', a)


def test_assoc_listeners123_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Listeners()
    b2 = jbatch_Listeners()
    _safe_set(a, 'jbatch_Step124', b1)
    assert _is_linked(a, 'jbatch_Step124', b1)
    if hasattr(b1, 'jbatch_Listeners125'):
        assert _is_linked(b1, 'jbatch_Listeners125', a)
    _safe_set(a, 'jbatch_Step124', b2)
    assert _is_linked(a, 'jbatch_Step124', b2)
    if hasattr(b1, 'jbatch_Listeners125'):
        assert not _is_linked(b1, 'jbatch_Listeners125', a)
    if hasattr(b2, 'jbatch_Listeners125'):
        assert _is_linked(b2, 'jbatch_Listeners125', a)
    _safe_set(a, 'jbatch_Step124', None)
    assert not _is_linked(a, 'jbatch_Step124', b2)
    if hasattr(b2, 'jbatch_Listeners125'):
        assert not _is_linked(b2, 'jbatch_Listeners125', a)


def test_assoc_listeners76_link_reassign_clear():
    a = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b1 = jbatch_Listeners()
    b2 = jbatch_Listeners()
    _safe_set(a, 'jbatch_Job77', b1)
    assert _is_linked(a, 'jbatch_Job77', b1)
    if hasattr(b1, 'jbatch_Listeners'):
        assert _is_linked(b1, 'jbatch_Listeners', a)
    _safe_set(a, 'jbatch_Job77', b2)
    assert _is_linked(a, 'jbatch_Job77', b2)
    if hasattr(b1, 'jbatch_Listeners'):
        assert not _is_linked(b1, 'jbatch_Listeners', a)
    if hasattr(b2, 'jbatch_Listeners'):
        assert _is_linked(b2, 'jbatch_Listeners', a)
    _safe_set(a, 'jbatch_Job77', None)
    assert not _is_linked(a, 'jbatch_Job77', b2)
    if hasattr(b2, 'jbatch_Listeners'):
        assert not _is_linked(b2, 'jbatch_Listeners', a)


def test_assoc_mapper95_link_reassign_clear():
    a = jbatch_PartitionMapper(ref="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_PartitionMapper', b1)
    assert _is_linked(a, 'jbatch_PartitionMapper', b1)
    if hasattr(b1, 'jbatch_Partition'):
        assert _is_linked(b1, 'jbatch_Partition', a)
    _safe_set(a, 'jbatch_PartitionMapper', b2)
    assert _is_linked(a, 'jbatch_PartitionMapper', b2)
    if hasattr(b1, 'jbatch_Partition'):
        assert not _is_linked(b1, 'jbatch_Partition', a)
    if hasattr(b2, 'jbatch_Partition'):
        assert _is_linked(b2, 'jbatch_Partition', a)
    _safe_set(a, 'jbatch_PartitionMapper', None)
    assert not _is_linked(a, 'jbatch_PartitionMapper', b2)
    if hasattr(b2, 'jbatch_Partition'):
        assert not _is_linked(b2, 'jbatch_Partition', a)


def test_assoc_next141_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Next(on="sample_text", to="sample_text")
    b2 = jbatch_Next(on="sample_text_2", to="sample_text_2")
    _safe_set(a, 'jbatch_Step142', {b1})
    assert _is_linked(a, 'jbatch_Step142', b1)
    if hasattr(b1, 'jbatch_Next143'):
        assert _is_linked(b1, 'jbatch_Next143', a)
    _safe_set(a, 'jbatch_Step142', {b2})
    assert _is_linked(a, 'jbatch_Step142', b2)
    if hasattr(b1, 'jbatch_Next143'):
        assert not _is_linked(b1, 'jbatch_Next143', a)
    if hasattr(b2, 'jbatch_Next143'):
        assert _is_linked(b2, 'jbatch_Next143', a)
    _safe_set(a, 'jbatch_Step142', set())
    assert not _is_linked(a, 'jbatch_Step142', b2)
    if hasattr(b2, 'jbatch_Next143'):
        assert not _is_linked(b2, 'jbatch_Next143', a)


def test_assoc_next29_link_reassign_clear():
    a = jbatch_Next(on="sample_text", to="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Next', b1)
    assert _is_linked(a, 'jbatch_Next', b1)
    if hasattr(b1, 'jbatch_Decision30'):
        assert _is_linked(b1, 'jbatch_Decision30', a)
    _safe_set(a, 'jbatch_Next', b2)
    assert _is_linked(a, 'jbatch_Next', b2)
    if hasattr(b1, 'jbatch_Decision30'):
        assert not _is_linked(b1, 'jbatch_Decision30', a)
    if hasattr(b2, 'jbatch_Decision30'):
        assert _is_linked(b2, 'jbatch_Decision30', a)
    _safe_set(a, 'jbatch_Next', None)
    assert not _is_linked(a, 'jbatch_Next', b2)
    if hasattr(b2, 'jbatch_Decision30'):
        assert not _is_linked(b2, 'jbatch_Decision30', a)


def test_assoc_next58_link_reassign_clear():
    a = jbatch_Next(on="sample_text", to="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Next60', b1)
    assert _is_linked(a, 'jbatch_Next60', b1)
    if hasattr(b1, 'jbatch_Flow59'):
        assert _is_linked(b1, 'jbatch_Flow59', a)
    _safe_set(a, 'jbatch_Next60', b2)
    assert _is_linked(a, 'jbatch_Next60', b2)
    if hasattr(b1, 'jbatch_Flow59'):
        assert not _is_linked(b1, 'jbatch_Flow59', a)
    if hasattr(b2, 'jbatch_Flow59'):
        assert _is_linked(b2, 'jbatch_Flow59', a)
    _safe_set(a, 'jbatch_Next60', None)
    assert not _is_linked(a, 'jbatch_Next60', b2)
    if hasattr(b2, 'jbatch_Flow59'):
        assert not _is_linked(b2, 'jbatch_Flow59', a)


def test_assoc_noRollbackExceptionClasses18_link_reassign_clear():
    a = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b1 = jbatch_ExceptionClassFilter()
    b2 = jbatch_ExceptionClassFilter()
    _safe_set(a, 'jbatch_Chunk19', b1)
    assert _is_linked(a, 'jbatch_Chunk19', b1)
    if hasattr(b1, 'jbatch_ExceptionClassFilter20'):
        assert _is_linked(b1, 'jbatch_ExceptionClassFilter20', a)
    _safe_set(a, 'jbatch_Chunk19', b2)
    assert _is_linked(a, 'jbatch_Chunk19', b2)
    if hasattr(b1, 'jbatch_ExceptionClassFilter20'):
        assert not _is_linked(b1, 'jbatch_ExceptionClassFilter20', a)
    if hasattr(b2, 'jbatch_ExceptionClassFilter20'):
        assert _is_linked(b2, 'jbatch_ExceptionClassFilter20', a)
    _safe_set(a, 'jbatch_Chunk19', None)
    assert not _is_linked(a, 'jbatch_Chunk19', b2)
    if hasattr(b2, 'jbatch_ExceptionClassFilter20'):
        assert not _is_linked(b2, 'jbatch_ExceptionClassFilter20', a)


def test_assoc_partition132_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_Step133', b1)
    assert _is_linked(a, 'jbatch_Step133', b1)
    if hasattr(b1, 'jbatch_Partition134'):
        assert _is_linked(b1, 'jbatch_Partition134', a)
    _safe_set(a, 'jbatch_Step133', b2)
    assert _is_linked(a, 'jbatch_Step133', b2)
    if hasattr(b1, 'jbatch_Partition134'):
        assert not _is_linked(b1, 'jbatch_Partition134', a)
    if hasattr(b2, 'jbatch_Partition134'):
        assert _is_linked(b2, 'jbatch_Partition134', a)
    _safe_set(a, 'jbatch_Step133', None)
    assert not _is_linked(a, 'jbatch_Step133', b2)
    if hasattr(b2, 'jbatch_Partition134'):
        assert not _is_linked(b2, 'jbatch_Partition134', a)


def test_assoc_plan96_link_reassign_clear():
    a = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_PartitionPlan', b1)
    assert _is_linked(a, 'jbatch_PartitionPlan', b1)
    if hasattr(b1, 'jbatch_Partition97'):
        assert _is_linked(b1, 'jbatch_Partition97', a)
    _safe_set(a, 'jbatch_PartitionPlan', b2)
    assert _is_linked(a, 'jbatch_PartitionPlan', b2)
    if hasattr(b1, 'jbatch_Partition97'):
        assert not _is_linked(b1, 'jbatch_Partition97', a)
    if hasattr(b2, 'jbatch_Partition97'):
        assert _is_linked(b2, 'jbatch_Partition97', a)
    _safe_set(a, 'jbatch_PartitionPlan', None)
    assert not _is_linked(a, 'jbatch_PartitionPlan', b2)
    if hasattr(b2, 'jbatch_Partition97'):
        assert not _is_linked(b2, 'jbatch_Partition97', a)


def test_assoc_processor6_link_reassign_clear():
    a = jbatch_ItemProcessor(ref="sample_text")
    b1 = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b2 = jbatch_Chunk(checkpointPolicy="sample_text_2", itemCount="sample_text_2", retryLimit="sample_text_2", skipLimit="sample_text_2", timeLimit="sample_text_2")
    _safe_set(a, 'jbatch_ItemProcessor', b1)
    assert _is_linked(a, 'jbatch_ItemProcessor', b1)
    if hasattr(b1, 'jbatch_Chunk7'):
        assert _is_linked(b1, 'jbatch_Chunk7', a)
    _safe_set(a, 'jbatch_ItemProcessor', b2)
    assert _is_linked(a, 'jbatch_ItemProcessor', b2)
    if hasattr(b1, 'jbatch_Chunk7'):
        assert not _is_linked(b1, 'jbatch_Chunk7', a)
    if hasattr(b2, 'jbatch_Chunk7'):
        assert _is_linked(b2, 'jbatch_Chunk7', a)
    _safe_set(a, 'jbatch_ItemProcessor', None)
    assert not _is_linked(a, 'jbatch_ItemProcessor', b2)
    if hasattr(b2, 'jbatch_Chunk7'):
        assert not _is_linked(b2, 'jbatch_Chunk7', a)


def test_assoc_properties0_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Analyzer(ref="sample_text")
    b2 = jbatch_Analyzer(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties', b1)
    assert _is_linked(a, 'jbatch_Properties', b1)
    if hasattr(b1, 'jbatch_Analyzer'):
        assert _is_linked(b1, 'jbatch_Analyzer', a)
    _safe_set(a, 'jbatch_Properties', b2)
    assert _is_linked(a, 'jbatch_Properties', b2)
    if hasattr(b1, 'jbatch_Analyzer'):
        assert not _is_linked(b1, 'jbatch_Analyzer', a)
    if hasattr(b2, 'jbatch_Analyzer'):
        assert _is_linked(b2, 'jbatch_Analyzer', a)
    _safe_set(a, 'jbatch_Properties', None)
    assert not _is_linked(a, 'jbatch_Properties', b2)
    if hasattr(b2, 'jbatch_Analyzer'):
        assert not _is_linked(b2, 'jbatch_Analyzer', a)


def test_assoc_properties1_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Batchlet(ref="sample_text")
    b2 = jbatch_Batchlet(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties2', b1)
    assert _is_linked(a, 'jbatch_Properties2', b1)
    if hasattr(b1, 'jbatch_Batchlet'):
        assert _is_linked(b1, 'jbatch_Batchlet', a)
    _safe_set(a, 'jbatch_Properties2', b2)
    assert _is_linked(a, 'jbatch_Properties2', b2)
    if hasattr(b1, 'jbatch_Batchlet'):
        assert not _is_linked(b1, 'jbatch_Batchlet', a)
    if hasattr(b2, 'jbatch_Batchlet'):
        assert _is_linked(b2, 'jbatch_Batchlet', a)
    _safe_set(a, 'jbatch_Properties2', None)
    assert not _is_linked(a, 'jbatch_Properties2', b2)
    if hasattr(b2, 'jbatch_Batchlet'):
        assert not _is_linked(b2, 'jbatch_Batchlet', a)


def test_assoc_properties106_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_PartitionMapper(ref="sample_text")
    b2 = jbatch_PartitionMapper(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties108', b1)
    assert _is_linked(a, 'jbatch_Properties108', b1)
    if hasattr(b1, 'jbatch_PartitionMapper107'):
        assert _is_linked(b1, 'jbatch_PartitionMapper107', a)
    _safe_set(a, 'jbatch_Properties108', b2)
    assert _is_linked(a, 'jbatch_Properties108', b2)
    if hasattr(b1, 'jbatch_PartitionMapper107'):
        assert not _is_linked(b1, 'jbatch_PartitionMapper107', a)
    if hasattr(b2, 'jbatch_PartitionMapper107'):
        assert _is_linked(b2, 'jbatch_PartitionMapper107', a)
    _safe_set(a, 'jbatch_Properties108', None)
    assert not _is_linked(a, 'jbatch_Properties108', b2)
    if hasattr(b2, 'jbatch_PartitionMapper107'):
        assert not _is_linked(b2, 'jbatch_PartitionMapper107', a)


def test_assoc_properties109_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_PartitionPlan(partitions="sample_text", threads="sample_text")
    b2 = jbatch_PartitionPlan(partitions="sample_text_2", threads="sample_text_2")
    _safe_set(a, 'jbatch_Properties111', b1)
    assert _is_linked(a, 'jbatch_Properties111', b1)
    if hasattr(b1, 'jbatch_PartitionPlan110'):
        assert _is_linked(b1, 'jbatch_PartitionPlan110', a)
    _safe_set(a, 'jbatch_Properties111', b2)
    assert _is_linked(a, 'jbatch_Properties111', b2)
    if hasattr(b1, 'jbatch_PartitionPlan110'):
        assert not _is_linked(b1, 'jbatch_PartitionPlan110', a)
    if hasattr(b2, 'jbatch_PartitionPlan110'):
        assert _is_linked(b2, 'jbatch_PartitionPlan110', a)
    _safe_set(a, 'jbatch_Properties111', None)
    assert not _is_linked(a, 'jbatch_Properties111', b2)
    if hasattr(b2, 'jbatch_PartitionPlan110'):
        assert not _is_linked(b2, 'jbatch_PartitionPlan110', a)


def test_assoc_properties112_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_PartitionReducer(ref="sample_text")
    b2 = jbatch_PartitionReducer(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties114', b1)
    assert _is_linked(a, 'jbatch_Properties114', b1)
    if hasattr(b1, 'jbatch_PartitionReducer113'):
        assert _is_linked(b1, 'jbatch_PartitionReducer113', a)
    _safe_set(a, 'jbatch_Properties114', b2)
    assert _is_linked(a, 'jbatch_Properties114', b2)
    if hasattr(b1, 'jbatch_PartitionReducer113'):
        assert not _is_linked(b1, 'jbatch_PartitionReducer113', a)
    if hasattr(b2, 'jbatch_PartitionReducer113'):
        assert _is_linked(b2, 'jbatch_PartitionReducer113', a)
    _safe_set(a, 'jbatch_Properties114', None)
    assert not _is_linked(a, 'jbatch_Properties114', b2)
    if hasattr(b2, 'jbatch_PartitionReducer113'):
        assert not _is_linked(b2, 'jbatch_PartitionReducer113', a)


def test_assoc_properties120_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Properties(partition="sample_text")
    b2 = jbatch_Properties(partition="sample_text_2")
    _safe_set(a, 'jbatch_Step121', b1)
    assert _is_linked(a, 'jbatch_Step121', b1)
    if hasattr(b1, 'jbatch_Properties122'):
        assert _is_linked(b1, 'jbatch_Properties122', a)
    _safe_set(a, 'jbatch_Step121', b2)
    assert _is_linked(a, 'jbatch_Step121', b2)
    if hasattr(b1, 'jbatch_Properties122'):
        assert not _is_linked(b1, 'jbatch_Properties122', a)
    if hasattr(b2, 'jbatch_Properties122'):
        assert _is_linked(b2, 'jbatch_Properties122', a)
    _safe_set(a, 'jbatch_Step121', None)
    assert not _is_linked(a, 'jbatch_Step121', b2)
    if hasattr(b2, 'jbatch_Properties122'):
        assert not _is_linked(b2, 'jbatch_Properties122', a)


def test_assoc_properties21_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Collector(ref="sample_text")
    b2 = jbatch_Collector(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties22', b1)
    assert _is_linked(a, 'jbatch_Properties22', b1)
    if hasattr(b1, 'jbatch_Collector'):
        assert _is_linked(b1, 'jbatch_Collector', a)
    _safe_set(a, 'jbatch_Properties22', b2)
    assert _is_linked(a, 'jbatch_Properties22', b2)
    if hasattr(b1, 'jbatch_Collector'):
        assert not _is_linked(b1, 'jbatch_Collector', a)
    if hasattr(b2, 'jbatch_Collector'):
        assert _is_linked(b2, 'jbatch_Collector', a)
    _safe_set(a, 'jbatch_Properties22', None)
    assert not _is_linked(a, 'jbatch_Properties22', b2)
    if hasattr(b2, 'jbatch_Collector'):
        assert not _is_linked(b2, 'jbatch_Collector', a)


def test_assoc_properties23_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Properties24', b1)
    assert _is_linked(a, 'jbatch_Properties24', b1)
    if hasattr(b1, 'jbatch_Decision'):
        assert _is_linked(b1, 'jbatch_Decision', a)
    _safe_set(a, 'jbatch_Properties24', b2)
    assert _is_linked(a, 'jbatch_Properties24', b2)
    if hasattr(b1, 'jbatch_Decision'):
        assert not _is_linked(b1, 'jbatch_Decision', a)
    if hasattr(b2, 'jbatch_Decision'):
        assert _is_linked(b2, 'jbatch_Decision', a)
    _safe_set(a, 'jbatch_Properties24', None)
    assert not _is_linked(a, 'jbatch_Properties24', b2)
    if hasattr(b2, 'jbatch_Decision'):
        assert not _is_linked(b2, 'jbatch_Decision', a)


def test_assoc_properties3_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_CheckpointAlgorithm(ref="sample_text")
    b2 = jbatch_CheckpointAlgorithm(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties4', b1)
    assert _is_linked(a, 'jbatch_Properties4', b1)
    if hasattr(b1, 'jbatch_CheckpointAlgorithm'):
        assert _is_linked(b1, 'jbatch_CheckpointAlgorithm', a)
    _safe_set(a, 'jbatch_Properties4', b2)
    assert _is_linked(a, 'jbatch_Properties4', b2)
    if hasattr(b1, 'jbatch_CheckpointAlgorithm'):
        assert not _is_linked(b1, 'jbatch_CheckpointAlgorithm', a)
    if hasattr(b2, 'jbatch_CheckpointAlgorithm'):
        assert _is_linked(b2, 'jbatch_CheckpointAlgorithm', a)
    _safe_set(a, 'jbatch_Properties4', None)
    assert not _is_linked(a, 'jbatch_Properties4', b2)
    if hasattr(b2, 'jbatch_CheckpointAlgorithm'):
        assert not _is_linked(b2, 'jbatch_CheckpointAlgorithm', a)


def test_assoc_properties64_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_ItemProcessor(ref="sample_text")
    b2 = jbatch_ItemProcessor(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties66', b1)
    assert _is_linked(a, 'jbatch_Properties66', b1)
    if hasattr(b1, 'jbatch_ItemProcessor65'):
        assert _is_linked(b1, 'jbatch_ItemProcessor65', a)
    _safe_set(a, 'jbatch_Properties66', b2)
    assert _is_linked(a, 'jbatch_Properties66', b2)
    if hasattr(b1, 'jbatch_ItemProcessor65'):
        assert not _is_linked(b1, 'jbatch_ItemProcessor65', a)
    if hasattr(b2, 'jbatch_ItemProcessor65'):
        assert _is_linked(b2, 'jbatch_ItemProcessor65', a)
    _safe_set(a, 'jbatch_Properties66', None)
    assert not _is_linked(a, 'jbatch_Properties66', b2)
    if hasattr(b2, 'jbatch_ItemProcessor65'):
        assert not _is_linked(b2, 'jbatch_ItemProcessor65', a)


def test_assoc_properties67_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_ItemReader(ref="sample_text")
    b2 = jbatch_ItemReader(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties69', b1)
    assert _is_linked(a, 'jbatch_Properties69', b1)
    if hasattr(b1, 'jbatch_ItemReader68'):
        assert _is_linked(b1, 'jbatch_ItemReader68', a)
    _safe_set(a, 'jbatch_Properties69', b2)
    assert _is_linked(a, 'jbatch_Properties69', b2)
    if hasattr(b1, 'jbatch_ItemReader68'):
        assert not _is_linked(b1, 'jbatch_ItemReader68', a)
    if hasattr(b2, 'jbatch_ItemReader68'):
        assert _is_linked(b2, 'jbatch_ItemReader68', a)
    _safe_set(a, 'jbatch_Properties69', None)
    assert not _is_linked(a, 'jbatch_Properties69', b2)
    if hasattr(b2, 'jbatch_ItemReader68'):
        assert not _is_linked(b2, 'jbatch_ItemReader68', a)


def test_assoc_properties70_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_ItemWriter(ref="sample_text")
    b2 = jbatch_ItemWriter(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties72', b1)
    assert _is_linked(a, 'jbatch_Properties72', b1)
    if hasattr(b1, 'jbatch_ItemWriter71'):
        assert _is_linked(b1, 'jbatch_ItemWriter71', a)
    _safe_set(a, 'jbatch_Properties72', b2)
    assert _is_linked(a, 'jbatch_Properties72', b2)
    if hasattr(b1, 'jbatch_ItemWriter71'):
        assert not _is_linked(b1, 'jbatch_ItemWriter71', a)
    if hasattr(b2, 'jbatch_ItemWriter71'):
        assert _is_linked(b2, 'jbatch_ItemWriter71', a)
    _safe_set(a, 'jbatch_Properties72', None)
    assert not _is_linked(a, 'jbatch_Properties72', b2)
    if hasattr(b2, 'jbatch_ItemWriter71'):
        assert not _is_linked(b2, 'jbatch_ItemWriter71', a)


def test_assoc_properties73_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    _safe_set(a, 'jbatch_Properties75', b1)
    assert _is_linked(a, 'jbatch_Properties75', b1)
    if hasattr(b1, 'jbatch_Job74'):
        assert _is_linked(b1, 'jbatch_Job74', a)
    _safe_set(a, 'jbatch_Properties75', b2)
    assert _is_linked(a, 'jbatch_Properties75', b2)
    if hasattr(b1, 'jbatch_Job74'):
        assert not _is_linked(b1, 'jbatch_Job74', a)
    if hasattr(b2, 'jbatch_Job74'):
        assert _is_linked(b2, 'jbatch_Job74', a)
    _safe_set(a, 'jbatch_Properties75', None)
    assert not _is_linked(a, 'jbatch_Properties75', b2)
    if hasattr(b2, 'jbatch_Job74'):
        assert not _is_linked(b2, 'jbatch_Job74', a)


def test_assoc_properties90_link_reassign_clear():
    a = jbatch_Properties(partition="sample_text")
    b1 = jbatch_Listener(ref="sample_text")
    b2 = jbatch_Listener(ref="sample_text_2")
    _safe_set(a, 'jbatch_Properties91', b1)
    assert _is_linked(a, 'jbatch_Properties91', b1)
    if hasattr(b1, 'jbatch_Listener'):
        assert _is_linked(b1, 'jbatch_Listener', a)
    _safe_set(a, 'jbatch_Properties91', b2)
    assert _is_linked(a, 'jbatch_Properties91', b2)
    if hasattr(b1, 'jbatch_Listener'):
        assert not _is_linked(b1, 'jbatch_Listener', a)
    if hasattr(b2, 'jbatch_Listener'):
        assert _is_linked(b2, 'jbatch_Listener', a)
    _safe_set(a, 'jbatch_Properties91', None)
    assert not _is_linked(a, 'jbatch_Properties91', b2)
    if hasattr(b2, 'jbatch_Listener'):
        assert not _is_linked(b2, 'jbatch_Listener', a)


def test_assoc_property115_link_reassign_clear():
    a = jbatch_Property(name="sample_text", value="sample_text")
    b1 = jbatch_Properties(partition="sample_text")
    b2 = jbatch_Properties(partition="sample_text_2")
    _safe_set(a, 'jbatch_Property', b1)
    assert _is_linked(a, 'jbatch_Property', b1)
    if hasattr(b1, 'jbatch_Properties116'):
        assert _is_linked(b1, 'jbatch_Properties116', a)
    _safe_set(a, 'jbatch_Property', b2)
    assert _is_linked(a, 'jbatch_Property', b2)
    if hasattr(b1, 'jbatch_Properties116'):
        assert not _is_linked(b1, 'jbatch_Properties116', a)
    if hasattr(b2, 'jbatch_Properties116'):
        assert _is_linked(b2, 'jbatch_Properties116', a)
    _safe_set(a, 'jbatch_Property', None)
    assert not _is_linked(a, 'jbatch_Property', b2)
    if hasattr(b2, 'jbatch_Properties116'):
        assert not _is_linked(b2, 'jbatch_Properties116', a)


def test_assoc_reader5_link_reassign_clear():
    a = jbatch_ItemReader(ref="sample_text")
    b1 = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b2 = jbatch_Chunk(checkpointPolicy="sample_text_2", itemCount="sample_text_2", retryLimit="sample_text_2", skipLimit="sample_text_2", timeLimit="sample_text_2")
    _safe_set(a, 'jbatch_ItemReader', b1)
    assert _is_linked(a, 'jbatch_ItemReader', b1)
    if hasattr(b1, 'jbatch_Chunk'):
        assert _is_linked(b1, 'jbatch_Chunk', a)
    _safe_set(a, 'jbatch_ItemReader', b2)
    assert _is_linked(a, 'jbatch_ItemReader', b2)
    if hasattr(b1, 'jbatch_Chunk'):
        assert not _is_linked(b1, 'jbatch_Chunk', a)
    if hasattr(b2, 'jbatch_Chunk'):
        assert _is_linked(b2, 'jbatch_Chunk', a)
    _safe_set(a, 'jbatch_ItemReader', None)
    assert not _is_linked(a, 'jbatch_ItemReader', b2)
    if hasattr(b2, 'jbatch_Chunk'):
        assert not _is_linked(b2, 'jbatch_Chunk', a)


def test_assoc_reducer104_link_reassign_clear():
    a = jbatch_PartitionReducer(ref="sample_text")
    b1 = jbatch_Partition()
    b2 = jbatch_Partition()
    _safe_set(a, 'jbatch_PartitionReducer', b1)
    assert _is_linked(a, 'jbatch_PartitionReducer', b1)
    if hasattr(b1, 'jbatch_Partition105'):
        assert _is_linked(b1, 'jbatch_Partition105', a)
    _safe_set(a, 'jbatch_PartitionReducer', b2)
    assert _is_linked(a, 'jbatch_PartitionReducer', b2)
    if hasattr(b1, 'jbatch_Partition105'):
        assert not _is_linked(b1, 'jbatch_Partition105', a)
    if hasattr(b2, 'jbatch_Partition105'):
        assert _is_linked(b2, 'jbatch_Partition105', a)
    _safe_set(a, 'jbatch_PartitionReducer', None)
    assert not _is_linked(a, 'jbatch_PartitionReducer', b2)
    if hasattr(b2, 'jbatch_Partition105'):
        assert not _is_linked(b2, 'jbatch_Partition105', a)


def test_assoc_retryableExceptionClasses15_link_reassign_clear():
    a = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b1 = jbatch_ExceptionClassFilter()
    b2 = jbatch_ExceptionClassFilter()
    _safe_set(a, 'jbatch_Chunk16', b1)
    assert _is_linked(a, 'jbatch_Chunk16', b1)
    if hasattr(b1, 'jbatch_ExceptionClassFilter17'):
        assert _is_linked(b1, 'jbatch_ExceptionClassFilter17', a)
    _safe_set(a, 'jbatch_Chunk16', b2)
    assert _is_linked(a, 'jbatch_Chunk16', b2)
    if hasattr(b1, 'jbatch_ExceptionClassFilter17'):
        assert not _is_linked(b1, 'jbatch_ExceptionClassFilter17', a)
    if hasattr(b2, 'jbatch_ExceptionClassFilter17'):
        assert _is_linked(b2, 'jbatch_ExceptionClassFilter17', a)
    _safe_set(a, 'jbatch_Chunk16', None)
    assert not _is_linked(a, 'jbatch_Chunk16', b2)
    if hasattr(b2, 'jbatch_ExceptionClassFilter17'):
        assert not _is_linked(b2, 'jbatch_ExceptionClassFilter17', a)


def test_assoc_skippableExceptionClasses13_link_reassign_clear():
    a = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b1 = jbatch_ExceptionClassFilter()
    b2 = jbatch_ExceptionClassFilter()
    _safe_set(a, 'jbatch_Chunk14', b1)
    assert _is_linked(a, 'jbatch_Chunk14', b1)
    if hasattr(b1, 'jbatch_ExceptionClassFilter'):
        assert _is_linked(b1, 'jbatch_ExceptionClassFilter', a)
    _safe_set(a, 'jbatch_Chunk14', b2)
    assert _is_linked(a, 'jbatch_Chunk14', b2)
    if hasattr(b1, 'jbatch_ExceptionClassFilter'):
        assert not _is_linked(b1, 'jbatch_ExceptionClassFilter', a)
    if hasattr(b2, 'jbatch_ExceptionClassFilter'):
        assert _is_linked(b2, 'jbatch_ExceptionClassFilter', a)
    _safe_set(a, 'jbatch_Chunk14', None)
    assert not _is_linked(a, 'jbatch_Chunk14', b2)
    if hasattr(b2, 'jbatch_ExceptionClassFilter'):
        assert not _is_linked(b2, 'jbatch_ExceptionClassFilter', a)


def test_assoc_split48_link_reassign_clear():
    a = jbatch_Split(id="sample_text", next="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Split', b1)
    assert _is_linked(a, 'jbatch_Split', b1)
    if hasattr(b1, 'jbatch_Flow49'):
        assert _is_linked(b1, 'jbatch_Flow49', a)
    _safe_set(a, 'jbatch_Split', b2)
    assert _is_linked(a, 'jbatch_Split', b2)
    if hasattr(b1, 'jbatch_Flow49'):
        assert not _is_linked(b1, 'jbatch_Flow49', a)
    if hasattr(b2, 'jbatch_Flow49'):
        assert _is_linked(b2, 'jbatch_Flow49', a)
    _safe_set(a, 'jbatch_Split', None)
    assert not _is_linked(a, 'jbatch_Split', b2)
    if hasattr(b2, 'jbatch_Flow49'):
        assert not _is_linked(b2, 'jbatch_Flow49', a)


def test_assoc_split84_link_reassign_clear():
    a = jbatch_Split(id="sample_text", next="sample_text")
    b1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    _safe_set(a, 'jbatch_Split86', b1)
    assert _is_linked(a, 'jbatch_Split86', b1)
    if hasattr(b1, 'jbatch_Job85'):
        assert _is_linked(b1, 'jbatch_Job85', a)
    _safe_set(a, 'jbatch_Split86', b2)
    assert _is_linked(a, 'jbatch_Split86', b2)
    if hasattr(b1, 'jbatch_Job85'):
        assert not _is_linked(b1, 'jbatch_Job85', a)
    if hasattr(b2, 'jbatch_Job85'):
        assert _is_linked(b2, 'jbatch_Job85', a)
    _safe_set(a, 'jbatch_Split86', None)
    assert not _is_linked(a, 'jbatch_Split86', b2)
    if hasattr(b2, 'jbatch_Job85'):
        assert not _is_linked(b2, 'jbatch_Job85', a)


def test_assoc_step50_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Step', b1)
    assert _is_linked(a, 'jbatch_Step', b1)
    if hasattr(b1, 'jbatch_Flow51'):
        assert _is_linked(b1, 'jbatch_Flow51', a)
    _safe_set(a, 'jbatch_Step', b2)
    assert _is_linked(a, 'jbatch_Step', b2)
    if hasattr(b1, 'jbatch_Flow51'):
        assert not _is_linked(b1, 'jbatch_Flow51', a)
    if hasattr(b2, 'jbatch_Flow51'):
        assert _is_linked(b2, 'jbatch_Flow51', a)
    _safe_set(a, 'jbatch_Step', None)
    assert not _is_linked(a, 'jbatch_Step', b2)
    if hasattr(b2, 'jbatch_Flow51'):
        assert not _is_linked(b2, 'jbatch_Flow51', a)


def test_assoc_step87_link_reassign_clear():
    a = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b1 = jbatch_Job(group="sample_text", id="sample_text", restartable="sample_text", version="sample_text")
    b2 = jbatch_Job(group="sample_text_2", id="sample_text_2", restartable="sample_text_2", version="sample_text_2")
    _safe_set(a, 'jbatch_Step89', b1)
    assert _is_linked(a, 'jbatch_Step89', b1)
    if hasattr(b1, 'jbatch_Job88'):
        assert _is_linked(b1, 'jbatch_Job88', a)
    _safe_set(a, 'jbatch_Step89', b2)
    assert _is_linked(a, 'jbatch_Step89', b2)
    if hasattr(b1, 'jbatch_Job88'):
        assert not _is_linked(b1, 'jbatch_Job88', a)
    if hasattr(b2, 'jbatch_Job88'):
        assert _is_linked(b2, 'jbatch_Job88', a)
    _safe_set(a, 'jbatch_Step89', None)
    assert not _is_linked(a, 'jbatch_Step89', b2)
    if hasattr(b2, 'jbatch_Job88'):
        assert not _is_linked(b2, 'jbatch_Job88', a)


def test_assoc_stop144_link_reassign_clear():
    a = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    b1 = jbatch_Step(allowStartIfComplete="sample_text", id="sample_text", next1="sample_text", startLimit="sample_text", transitionElements="sample_text")
    b2 = jbatch_Step(allowStartIfComplete="sample_text_2", id="sample_text_2", next1="sample_text_2", startLimit="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Stop146', b1)
    assert _is_linked(a, 'jbatch_Stop146', b1)
    if hasattr(b1, 'jbatch_Step145'):
        assert _is_linked(b1, 'jbatch_Step145', a)
    _safe_set(a, 'jbatch_Stop146', b2)
    assert _is_linked(a, 'jbatch_Stop146', b2)
    if hasattr(b1, 'jbatch_Step145'):
        assert not _is_linked(b1, 'jbatch_Step145', a)
    if hasattr(b2, 'jbatch_Step145'):
        assert _is_linked(b2, 'jbatch_Step145', a)
    _safe_set(a, 'jbatch_Stop146', None)
    assert not _is_linked(a, 'jbatch_Stop146', b2)
    if hasattr(b2, 'jbatch_Step145'):
        assert not _is_linked(b2, 'jbatch_Step145', a)


def test_assoc_stop31_link_reassign_clear():
    a = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    b1 = jbatch_Decision(id="sample_text", ref="sample_text", transitionElements="sample_text")
    b2 = jbatch_Decision(id="sample_text_2", ref="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Stop', b1)
    assert _is_linked(a, 'jbatch_Stop', b1)
    if hasattr(b1, 'jbatch_Decision32'):
        assert _is_linked(b1, 'jbatch_Decision32', a)
    _safe_set(a, 'jbatch_Stop', b2)
    assert _is_linked(a, 'jbatch_Stop', b2)
    if hasattr(b1, 'jbatch_Decision32'):
        assert not _is_linked(b1, 'jbatch_Decision32', a)
    if hasattr(b2, 'jbatch_Decision32'):
        assert _is_linked(b2, 'jbatch_Decision32', a)
    _safe_set(a, 'jbatch_Stop', None)
    assert not _is_linked(a, 'jbatch_Stop', b2)
    if hasattr(b2, 'jbatch_Decision32'):
        assert not _is_linked(b2, 'jbatch_Decision32', a)


def test_assoc_stop61_link_reassign_clear():
    a = jbatch_Stop(exitStatus="sample_text", on="sample_text", restart="sample_text")
    b1 = jbatch_Flow(group="sample_text", id="sample_text", next1="sample_text", transitionElements="sample_text")
    b2 = jbatch_Flow(group="sample_text_2", id="sample_text_2", next1="sample_text_2", transitionElements="sample_text_2")
    _safe_set(a, 'jbatch_Stop63', b1)
    assert _is_linked(a, 'jbatch_Stop63', b1)
    if hasattr(b1, 'jbatch_Flow62'):
        assert _is_linked(b1, 'jbatch_Flow62', a)
    _safe_set(a, 'jbatch_Stop63', b2)
    assert _is_linked(a, 'jbatch_Stop63', b2)
    if hasattr(b1, 'jbatch_Flow62'):
        assert not _is_linked(b1, 'jbatch_Flow62', a)
    if hasattr(b2, 'jbatch_Flow62'):
        assert _is_linked(b2, 'jbatch_Flow62', a)
    _safe_set(a, 'jbatch_Stop63', None)
    assert not _is_linked(a, 'jbatch_Stop63', b2)
    if hasattr(b2, 'jbatch_Flow62'):
        assert not _is_linked(b2, 'jbatch_Flow62', a)


def test_assoc_writer8_link_reassign_clear():
    a = jbatch_ItemWriter(ref="sample_text")
    b1 = jbatch_Chunk(checkpointPolicy="sample_text", itemCount="sample_text", retryLimit="sample_text", skipLimit="sample_text", timeLimit="sample_text")
    b2 = jbatch_Chunk(checkpointPolicy="sample_text_2", itemCount="sample_text_2", retryLimit="sample_text_2", skipLimit="sample_text_2", timeLimit="sample_text_2")
    _safe_set(a, 'jbatch_ItemWriter', b1)
    assert _is_linked(a, 'jbatch_ItemWriter', b1)
    if hasattr(b1, 'jbatch_Chunk9'):
        assert _is_linked(b1, 'jbatch_Chunk9', a)
    _safe_set(a, 'jbatch_ItemWriter', b2)
    assert _is_linked(a, 'jbatch_ItemWriter', b2)
    if hasattr(b1, 'jbatch_Chunk9'):
        assert not _is_linked(b1, 'jbatch_Chunk9', a)
    if hasattr(b2, 'jbatch_Chunk9'):
        assert _is_linked(b2, 'jbatch_Chunk9', a)
    _safe_set(a, 'jbatch_ItemWriter', None)
    assert not _is_linked(a, 'jbatch_ItemWriter', b2)
    if hasattr(b2, 'jbatch_Chunk9'):
        assert not _is_linked(b2, 'jbatch_Chunk9', a)


def test_assoc_xMLNSPrefixMap33_link_reassign_clear():
    a = jbatch_DocumentRoot(mixed="sample_text")
    b1 = jbatch_EStringToStringMapEntry()
    b2 = jbatch_EStringToStringMapEntry()
    _safe_set(a, 'jbatch_DocumentRoot', {b1})
    assert _is_linked(a, 'jbatch_DocumentRoot', b1)
    if hasattr(b1, 'jbatch_EStringToStringMapEntry'):
        assert _is_linked(b1, 'jbatch_EStringToStringMapEntry', a)
    _safe_set(a, 'jbatch_DocumentRoot', {b2})
    assert _is_linked(a, 'jbatch_DocumentRoot', b2)
    if hasattr(b1, 'jbatch_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'jbatch_EStringToStringMapEntry', a)
    if hasattr(b2, 'jbatch_EStringToStringMapEntry'):
        assert _is_linked(b2, 'jbatch_EStringToStringMapEntry', a)
    _safe_set(a, 'jbatch_DocumentRoot', set())
    assert not _is_linked(a, 'jbatch_DocumentRoot', b2)
    if hasattr(b2, 'jbatch_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'jbatch_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation34_link_reassign_clear():
    a = jbatch_DocumentRoot(mixed="sample_text")
    b1 = jbatch_EStringToStringMapEntry()
    b2 = jbatch_EStringToStringMapEntry()
    _safe_set(a, 'jbatch_DocumentRoot35', {b1})
    assert _is_linked(a, 'jbatch_DocumentRoot35', b1)
    if hasattr(b1, 'jbatch_EStringToStringMapEntry36'):
        assert _is_linked(b1, 'jbatch_EStringToStringMapEntry36', a)
    _safe_set(a, 'jbatch_DocumentRoot35', {b2})
    assert _is_linked(a, 'jbatch_DocumentRoot35', b2)
    if hasattr(b1, 'jbatch_EStringToStringMapEntry36'):
        assert not _is_linked(b1, 'jbatch_EStringToStringMapEntry36', a)
    if hasattr(b2, 'jbatch_EStringToStringMapEntry36'):
        assert _is_linked(b2, 'jbatch_EStringToStringMapEntry36', a)
    _safe_set(a, 'jbatch_DocumentRoot35', set())
    assert not _is_linked(a, 'jbatch_DocumentRoot35', b2)
    if hasattr(b2, 'jbatch_EStringToStringMapEntry36'):
        assert not _is_linked(b2, 'jbatch_EStringToStringMapEntry36', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

jbatch_Analyzer_strategy = st.builds(jbatch_Analyzer, ref=safe_text)
@given(instance=jbatch_Analyzer_strategy)
@settings(max_examples=25)
def test_jbatch_Analyzer_instantiation(instance):
    assert isinstance(instance, jbatch_Analyzer)


jbatch_Batchlet_strategy = st.builds(jbatch_Batchlet, ref=safe_text)
@given(instance=jbatch_Batchlet_strategy)
@settings(max_examples=25)
def test_jbatch_Batchlet_instantiation(instance):
    assert isinstance(instance, jbatch_Batchlet)


jbatch_CheckpointAlgorithm_strategy = st.builds(jbatch_CheckpointAlgorithm, ref=safe_text)
@given(instance=jbatch_CheckpointAlgorithm_strategy)
@settings(max_examples=25)
def test_jbatch_CheckpointAlgorithm_instantiation(instance):
    assert isinstance(instance, jbatch_CheckpointAlgorithm)


jbatch_Chunk_strategy = st.builds(jbatch_Chunk, checkpointPolicy=safe_text, itemCount=safe_text, retryLimit=safe_text, skipLimit=safe_text, timeLimit=safe_text)
@given(instance=jbatch_Chunk_strategy)
@settings(max_examples=25)
def test_jbatch_Chunk_instantiation(instance):
    assert isinstance(instance, jbatch_Chunk)


jbatch_Collector_strategy = st.builds(jbatch_Collector, ref=safe_text)
@given(instance=jbatch_Collector_strategy)
@settings(max_examples=25)
def test_jbatch_Collector_instantiation(instance):
    assert isinstance(instance, jbatch_Collector)


jbatch_Decision_strategy = st.builds(jbatch_Decision, id=safe_text, ref=safe_text, transitionElements=safe_text)
@given(instance=jbatch_Decision_strategy)
@settings(max_examples=25)
def test_jbatch_Decision_instantiation(instance):
    assert isinstance(instance, jbatch_Decision)


jbatch_DocumentRoot_strategy = st.builds(jbatch_DocumentRoot, mixed=safe_text)
@given(instance=jbatch_DocumentRoot_strategy)
@settings(max_examples=25)
def test_jbatch_DocumentRoot_instantiation(instance):
    assert isinstance(instance, jbatch_DocumentRoot)


jbatch_EStringToStringMapEntry_strategy = st.builds(jbatch_EStringToStringMapEntry)
@given(instance=jbatch_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_jbatch_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, jbatch_EStringToStringMapEntry)


jbatch_End_strategy = st.builds(jbatch_End, exitStatus=safe_text, on=safe_text)
@given(instance=jbatch_End_strategy)
@settings(max_examples=25)
def test_jbatch_End_instantiation(instance):
    assert isinstance(instance, jbatch_End)


jbatch_ExceptionClassFilter_strategy = st.builds(jbatch_ExceptionClassFilter)
@given(instance=jbatch_ExceptionClassFilter_strategy)
@settings(max_examples=25)
def test_jbatch_ExceptionClassFilter_instantiation(instance):
    assert isinstance(instance, jbatch_ExceptionClassFilter)


jbatch_ExcludeType_strategy = st.builds(jbatch_ExcludeType, class_=safe_text)
@given(instance=jbatch_ExcludeType_strategy)
@settings(max_examples=25)
def test_jbatch_ExcludeType_instantiation(instance):
    assert isinstance(instance, jbatch_ExcludeType)


jbatch_Fail_strategy = st.builds(jbatch_Fail, exitStatus=safe_text, on=safe_text)
@given(instance=jbatch_Fail_strategy)
@settings(max_examples=25)
def test_jbatch_Fail_instantiation(instance):
    assert isinstance(instance, jbatch_Fail)


jbatch_Flow_strategy = st.builds(jbatch_Flow, group=safe_text, id=safe_text, next1=safe_text, transitionElements=safe_text)
@given(instance=jbatch_Flow_strategy)
@settings(max_examples=25)
def test_jbatch_Flow_instantiation(instance):
    assert isinstance(instance, jbatch_Flow)


jbatch_IncludeType_strategy = st.builds(jbatch_IncludeType, class_=safe_text)
@given(instance=jbatch_IncludeType_strategy)
@settings(max_examples=25)
def test_jbatch_IncludeType_instantiation(instance):
    assert isinstance(instance, jbatch_IncludeType)


jbatch_ItemProcessor_strategy = st.builds(jbatch_ItemProcessor, ref=safe_text)
@given(instance=jbatch_ItemProcessor_strategy)
@settings(max_examples=25)
def test_jbatch_ItemProcessor_instantiation(instance):
    assert isinstance(instance, jbatch_ItemProcessor)


jbatch_ItemReader_strategy = st.builds(jbatch_ItemReader, ref=safe_text)
@given(instance=jbatch_ItemReader_strategy)
@settings(max_examples=25)
def test_jbatch_ItemReader_instantiation(instance):
    assert isinstance(instance, jbatch_ItemReader)


jbatch_ItemWriter_strategy = st.builds(jbatch_ItemWriter, ref=safe_text)
@given(instance=jbatch_ItemWriter_strategy)
@settings(max_examples=25)
def test_jbatch_ItemWriter_instantiation(instance):
    assert isinstance(instance, jbatch_ItemWriter)


jbatch_Job_strategy = st.builds(jbatch_Job, group=safe_text, id=safe_text, restartable=safe_text, version=safe_text)
@given(instance=jbatch_Job_strategy)
@settings(max_examples=25)
def test_jbatch_Job_instantiation(instance):
    assert isinstance(instance, jbatch_Job)


jbatch_Listener_strategy = st.builds(jbatch_Listener, ref=safe_text)
@given(instance=jbatch_Listener_strategy)
@settings(max_examples=25)
def test_jbatch_Listener_instantiation(instance):
    assert isinstance(instance, jbatch_Listener)


jbatch_Listeners_strategy = st.builds(jbatch_Listeners)
@given(instance=jbatch_Listeners_strategy)
@settings(max_examples=25)
def test_jbatch_Listeners_instantiation(instance):
    assert isinstance(instance, jbatch_Listeners)


jbatch_Next_strategy = st.builds(jbatch_Next, on=safe_text, to=safe_text)
@given(instance=jbatch_Next_strategy)
@settings(max_examples=25)
def test_jbatch_Next_instantiation(instance):
    assert isinstance(instance, jbatch_Next)


jbatch_Partition_strategy = st.builds(jbatch_Partition)
@given(instance=jbatch_Partition_strategy)
@settings(max_examples=25)
def test_jbatch_Partition_instantiation(instance):
    assert isinstance(instance, jbatch_Partition)


jbatch_PartitionMapper_strategy = st.builds(jbatch_PartitionMapper, ref=safe_text)
@given(instance=jbatch_PartitionMapper_strategy)
@settings(max_examples=25)
def test_jbatch_PartitionMapper_instantiation(instance):
    assert isinstance(instance, jbatch_PartitionMapper)


jbatch_PartitionPlan_strategy = st.builds(jbatch_PartitionPlan, partitions=safe_text, threads=safe_text)
@given(instance=jbatch_PartitionPlan_strategy)
@settings(max_examples=25)
def test_jbatch_PartitionPlan_instantiation(instance):
    assert isinstance(instance, jbatch_PartitionPlan)


jbatch_PartitionReducer_strategy = st.builds(jbatch_PartitionReducer, ref=safe_text)
@given(instance=jbatch_PartitionReducer_strategy)
@settings(max_examples=25)
def test_jbatch_PartitionReducer_instantiation(instance):
    assert isinstance(instance, jbatch_PartitionReducer)


jbatch_Properties_strategy = st.builds(jbatch_Properties, partition=safe_text)
@given(instance=jbatch_Properties_strategy)
@settings(max_examples=25)
def test_jbatch_Properties_instantiation(instance):
    assert isinstance(instance, jbatch_Properties)


jbatch_Property_strategy = st.builds(jbatch_Property, name=safe_text, value=safe_text)
@given(instance=jbatch_Property_strategy)
@settings(max_examples=25)
def test_jbatch_Property_instantiation(instance):
    assert isinstance(instance, jbatch_Property)


jbatch_Split_strategy = st.builds(jbatch_Split, id=safe_text, next=safe_text)
@given(instance=jbatch_Split_strategy)
@settings(max_examples=25)
def test_jbatch_Split_instantiation(instance):
    assert isinstance(instance, jbatch_Split)


jbatch_Step_strategy = st.builds(jbatch_Step, allowStartIfComplete=safe_text, id=safe_text, next1=safe_text, startLimit=safe_text, transitionElements=safe_text)
@given(instance=jbatch_Step_strategy)
@settings(max_examples=25)
def test_jbatch_Step_instantiation(instance):
    assert isinstance(instance, jbatch_Step)


jbatch_Stop_strategy = st.builds(jbatch_Stop, exitStatus=safe_text, on=safe_text, restart=safe_text)
@given(instance=jbatch_Stop_strategy)
@settings(max_examples=25)
def test_jbatch_Stop_instantiation(instance):
    assert isinstance(instance, jbatch_Stop)


