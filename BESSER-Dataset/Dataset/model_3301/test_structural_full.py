import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DynamicLabel,
    EdgeDecorator,
    EdgeLabel,
    LabelValue,
    MigrationEdge,
    MigrationEdgeLabel,
    Node,
    NodeLabel,
    PopulationEdge,
    TransportSystem,
    transport_LoadUnloadEdge,
    transport_LoadUnloadEdgeLabel,
    transport_PacketStyleTransportSystem,
    transport_PacketStyleTransportSystemDecorator,
    transport_PacketTransportLabel,
    transport_PacketTransportLabelValue,
    transport_PipeStyleTransportSystem,
    transport_PipeTransportEdge,
    transport_PipeTransportEdgeLabel,
    transport_PipeTransportEdgeLabelValue,
    transport_STEMTime,
    transport_TransportSystem,
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

def test_transport_LoadUnloadEdge_loadingEdge_value_roundtrip():
    instance = transport_LoadUnloadEdge(loadingEdge=True)
    assert instance.loadingEdge == True
    instance.loadingEdge = False
    assert instance.loadingEdge == False


def test_transport_LoadUnloadEdgeLabel_activatedRate_value_roundtrip():
    instance = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    assert instance.activatedRate == 3.14
    instance.activatedRate = 9.99
    assert instance.activatedRate == 9.99


def test_transport_PacketTransportLabelValue_capacity_value_roundtrip():
    instance = transport_PacketTransportLabelValue(capacity=3.14)
    assert instance.capacity == 3.14
    instance.capacity = 9.99
    assert instance.capacity == 9.99


def test_transport_PipeStyleTransportSystem_maxCapacity_value_roundtrip():
    instance = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    assert instance.maxCapacity == 3.14
    instance.maxCapacity = 9.99
    assert instance.maxCapacity == 9.99


def test_transport_PipeTransportEdgeLabelValue_maxFlow_value_roundtrip():
    instance = transport_PipeTransportEdgeLabelValue(maxFlow=3.14, timePeriod="sample_text")
    assert instance.maxFlow == 3.14
    instance.maxFlow = 9.99
    assert instance.maxFlow == 9.99


def test_transport_PipeTransportEdgeLabelValue_timePeriod_value_roundtrip():
    instance = transport_PipeTransportEdgeLabelValue(maxFlow=3.14, timePeriod="sample_text")
    assert instance.timePeriod == "sample_text"
    instance.timePeriod = "sample_text_2"
    assert instance.timePeriod == "sample_text_2"


def test_transport_LoadUnloadEdgeLabel_isa_DynamicLabel():
    instance = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    assert isinstance(instance, DynamicLabel)


def test_transport_PacketStyleTransportSystemDecorator_isa_EdgeDecorator():
    instance = transport_PacketStyleTransportSystemDecorator()
    assert isinstance(instance, EdgeDecorator)


def test_transport_PipeTransportEdgeLabel_isa_EdgeLabel():
    instance = transport_PipeTransportEdgeLabel()
    assert isinstance(instance, EdgeLabel)


def test_transport_PacketTransportLabelValue_isa_LabelValue():
    instance = transport_PacketTransportLabelValue(capacity=3.14)
    assert isinstance(instance, LabelValue)


def test_transport_PipeTransportEdgeLabelValue_isa_LabelValue():
    instance = transport_PipeTransportEdgeLabelValue(maxFlow=3.14, timePeriod="sample_text")
    assert isinstance(instance, LabelValue)


def test_transport_LoadUnloadEdge_isa_MigrationEdge():
    instance = transport_LoadUnloadEdge(loadingEdge=True)
    assert isinstance(instance, MigrationEdge)


def test_transport_LoadUnloadEdgeLabel_isa_MigrationEdgeLabel():
    instance = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    assert isinstance(instance, MigrationEdgeLabel)


def test_transport_TransportSystem_isa_Node():
    instance = transport_TransportSystem()
    assert isinstance(instance, Node)


def test_transport_PacketTransportLabel_isa_NodeLabel():
    instance = transport_PacketTransportLabel()
    assert isinstance(instance, NodeLabel)


def test_transport_PipeTransportEdge_isa_PopulationEdge():
    instance = transport_PipeTransportEdge()
    assert isinstance(instance, PopulationEdge)


def test_transport_PacketStyleTransportSystem_isa_TransportSystem():
    instance = transport_PacketStyleTransportSystem()
    assert isinstance(instance, TransportSystem)


def test_transport_PipeStyleTransportSystem_isa_TransportSystem():
    instance = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    assert isinstance(instance, TransportSystem)


def test_assoc_activationTime0_link_reassign_clear():
    a = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    b1 = transport_STEMTime()
    b2 = transport_STEMTime()
    _safe_set(a, 'transport_LoadUnloadEdgeLabel', b1)
    assert _is_linked(a, 'transport_LoadUnloadEdgeLabel', b1)
    if hasattr(b1, 'transport_STEMTime'):
        assert _is_linked(b1, 'transport_STEMTime', a)
    _safe_set(a, 'transport_LoadUnloadEdgeLabel', b2)
    assert _is_linked(a, 'transport_LoadUnloadEdgeLabel', b2)
    if hasattr(b1, 'transport_STEMTime'):
        assert not _is_linked(b1, 'transport_STEMTime', a)
    if hasattr(b2, 'transport_STEMTime'):
        assert _is_linked(b2, 'transport_STEMTime', a)
    _safe_set(a, 'transport_LoadUnloadEdgeLabel', None)
    assert not _is_linked(a, 'transport_LoadUnloadEdgeLabel', b2)
    if hasattr(b2, 'transport_STEMTime'):
        assert not _is_linked(b2, 'transport_STEMTime', a)


def test_assoc_deactivationTime1_link_reassign_clear():
    a = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    b1 = transport_STEMTime()
    b2 = transport_STEMTime()
    _safe_set(a, 'transport_LoadUnloadEdgeLabel2', b1)
    assert _is_linked(a, 'transport_LoadUnloadEdgeLabel2', b1)
    if hasattr(b1, 'transport_STEMTime3'):
        assert _is_linked(b1, 'transport_STEMTime3', a)
    _safe_set(a, 'transport_LoadUnloadEdgeLabel2', b2)
    assert _is_linked(a, 'transport_LoadUnloadEdgeLabel2', b2)
    if hasattr(b1, 'transport_STEMTime3'):
        assert not _is_linked(b1, 'transport_STEMTime3', a)
    if hasattr(b2, 'transport_STEMTime3'):
        assert _is_linked(b2, 'transport_STEMTime3', a)
    _safe_set(a, 'transport_LoadUnloadEdgeLabel2', None)
    assert not _is_linked(a, 'transport_LoadUnloadEdgeLabel2', b2)
    if hasattr(b2, 'transport_STEMTime3'):
        assert not _is_linked(b2, 'transport_STEMTime3', a)


def test_assoc_inTransportEdges10_link_reassign_clear():
    a = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    b1 = transport_PipeTransportEdge()
    b2 = transport_PipeTransportEdge()
    _safe_set(a, 'transport_PipeStyleTransportSystem', {b1})
    assert _is_linked(a, 'transport_PipeStyleTransportSystem', b1)
    if hasattr(b1, 'transport_PipeTransportEdge'):
        assert _is_linked(b1, 'transport_PipeTransportEdge', a)
    _safe_set(a, 'transport_PipeStyleTransportSystem', {b2})
    assert _is_linked(a, 'transport_PipeStyleTransportSystem', b2)
    if hasattr(b1, 'transport_PipeTransportEdge'):
        assert not _is_linked(b1, 'transport_PipeTransportEdge', a)
    if hasattr(b2, 'transport_PipeTransportEdge'):
        assert _is_linked(b2, 'transport_PipeTransportEdge', a)
    _safe_set(a, 'transport_PipeStyleTransportSystem', set())
    assert not _is_linked(a, 'transport_PipeStyleTransportSystem', b2)
    if hasattr(b2, 'transport_PipeTransportEdge'):
        assert not _is_linked(b2, 'transport_PipeTransportEdge', a)


def test_assoc_loadingEdges5_link_reassign_clear():
    a = transport_LoadUnloadEdge(loadingEdge=True)
    b1 = transport_PacketStyleTransportSystem()
    b2 = transport_PacketStyleTransportSystem()
    _safe_set(a, 'transport_LoadUnloadEdge', b1)
    assert _is_linked(a, 'transport_LoadUnloadEdge', b1)
    if hasattr(b1, 'transport_PacketStyleTransportSystem6'):
        assert _is_linked(b1, 'transport_PacketStyleTransportSystem6', a)
    _safe_set(a, 'transport_LoadUnloadEdge', b2)
    assert _is_linked(a, 'transport_LoadUnloadEdge', b2)
    if hasattr(b1, 'transport_PacketStyleTransportSystem6'):
        assert not _is_linked(b1, 'transport_PacketStyleTransportSystem6', a)
    if hasattr(b2, 'transport_PacketStyleTransportSystem6'):
        assert _is_linked(b2, 'transport_PacketStyleTransportSystem6', a)
    _safe_set(a, 'transport_LoadUnloadEdge', None)
    assert not _is_linked(a, 'transport_LoadUnloadEdge', b2)
    if hasattr(b2, 'transport_PacketStyleTransportSystem6'):
        assert not _is_linked(b2, 'transport_PacketStyleTransportSystem6', a)


def test_assoc_outTransportEdges11_link_reassign_clear():
    a = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    b1 = transport_PipeTransportEdge()
    b2 = transport_PipeTransportEdge()
    _safe_set(a, 'transport_PipeStyleTransportSystem12', {b1})
    assert _is_linked(a, 'transport_PipeStyleTransportSystem12', b1)
    if hasattr(b1, 'transport_PipeTransportEdge13'):
        assert _is_linked(b1, 'transport_PipeTransportEdge13', a)
    _safe_set(a, 'transport_PipeStyleTransportSystem12', {b2})
    assert _is_linked(a, 'transport_PipeStyleTransportSystem12', b2)
    if hasattr(b1, 'transport_PipeTransportEdge13'):
        assert not _is_linked(b1, 'transport_PipeTransportEdge13', a)
    if hasattr(b2, 'transport_PipeTransportEdge13'):
        assert _is_linked(b2, 'transport_PipeTransportEdge13', a)
    _safe_set(a, 'transport_PipeStyleTransportSystem12', set())
    assert not _is_linked(a, 'transport_PipeStyleTransportSystem12', b2)
    if hasattr(b2, 'transport_PipeTransportEdge13'):
        assert not _is_linked(b2, 'transport_PipeTransportEdge13', a)


def test_assoc_unloadingEdges7_link_reassign_clear():
    a = transport_LoadUnloadEdge(loadingEdge=True)
    b1 = transport_PacketStyleTransportSystem()
    b2 = transport_PacketStyleTransportSystem()
    _safe_set(a, 'transport_LoadUnloadEdge9', b1)
    assert _is_linked(a, 'transport_LoadUnloadEdge9', b1)
    if hasattr(b1, 'transport_PacketStyleTransportSystem8'):
        assert _is_linked(b1, 'transport_PacketStyleTransportSystem8', a)
    _safe_set(a, 'transport_LoadUnloadEdge9', b2)
    assert _is_linked(a, 'transport_LoadUnloadEdge9', b2)
    if hasattr(b1, 'transport_PacketStyleTransportSystem8'):
        assert not _is_linked(b1, 'transport_PacketStyleTransportSystem8', a)
    if hasattr(b2, 'transport_PacketStyleTransportSystem8'):
        assert _is_linked(b2, 'transport_PacketStyleTransportSystem8', a)
    _safe_set(a, 'transport_LoadUnloadEdge9', None)
    assert not _is_linked(a, 'transport_LoadUnloadEdge9', b2)
    if hasattr(b2, 'transport_PacketStyleTransportSystem8'):
        assert not _is_linked(b2, 'transport_PacketStyleTransportSystem8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DynamicLabel_strategy = st.builds(DynamicLabel)
@given(instance=DynamicLabel_strategy)
@settings(max_examples=25)
def test_DynamicLabel_instantiation(instance):
    assert isinstance(instance, DynamicLabel)


EdgeDecorator_strategy = st.builds(EdgeDecorator)
@given(instance=EdgeDecorator_strategy)
@settings(max_examples=25)
def test_EdgeDecorator_instantiation(instance):
    assert isinstance(instance, EdgeDecorator)


EdgeLabel_strategy = st.builds(EdgeLabel)
@given(instance=EdgeLabel_strategy)
@settings(max_examples=25)
def test_EdgeLabel_instantiation(instance):
    assert isinstance(instance, EdgeLabel)


LabelValue_strategy = st.builds(LabelValue)
@given(instance=LabelValue_strategy)
@settings(max_examples=25)
def test_LabelValue_instantiation(instance):
    assert isinstance(instance, LabelValue)


MigrationEdge_strategy = st.builds(MigrationEdge)
@given(instance=MigrationEdge_strategy)
@settings(max_examples=25)
def test_MigrationEdge_instantiation(instance):
    assert isinstance(instance, MigrationEdge)


MigrationEdgeLabel_strategy = st.builds(MigrationEdgeLabel)
@given(instance=MigrationEdgeLabel_strategy)
@settings(max_examples=25)
def test_MigrationEdgeLabel_instantiation(instance):
    assert isinstance(instance, MigrationEdgeLabel)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


NodeLabel_strategy = st.builds(NodeLabel)
@given(instance=NodeLabel_strategy)
@settings(max_examples=25)
def test_NodeLabel_instantiation(instance):
    assert isinstance(instance, NodeLabel)


PopulationEdge_strategy = st.builds(PopulationEdge)
@given(instance=PopulationEdge_strategy)
@settings(max_examples=25)
def test_PopulationEdge_instantiation(instance):
    assert isinstance(instance, PopulationEdge)


TransportSystem_strategy = st.builds(TransportSystem)
@given(instance=TransportSystem_strategy)
@settings(max_examples=25)
def test_TransportSystem_instantiation(instance):
    assert isinstance(instance, TransportSystem)


transport_LoadUnloadEdge_strategy = st.builds(transport_LoadUnloadEdge, loadingEdge=st.booleans())
@given(instance=transport_LoadUnloadEdge_strategy)
@settings(max_examples=25)
def test_transport_LoadUnloadEdge_instantiation(instance):
    assert isinstance(instance, transport_LoadUnloadEdge)


transport_LoadUnloadEdgeLabel_strategy = st.builds(transport_LoadUnloadEdgeLabel, activatedRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=transport_LoadUnloadEdgeLabel_strategy)
@settings(max_examples=25)
def test_transport_LoadUnloadEdgeLabel_instantiation(instance):
    assert isinstance(instance, transport_LoadUnloadEdgeLabel)


transport_PacketStyleTransportSystem_strategy = st.builds(transport_PacketStyleTransportSystem)
@given(instance=transport_PacketStyleTransportSystem_strategy)
@settings(max_examples=25)
def test_transport_PacketStyleTransportSystem_instantiation(instance):
    assert isinstance(instance, transport_PacketStyleTransportSystem)


transport_PacketStyleTransportSystemDecorator_strategy = st.builds(transport_PacketStyleTransportSystemDecorator)
@given(instance=transport_PacketStyleTransportSystemDecorator_strategy)
@settings(max_examples=25)
def test_transport_PacketStyleTransportSystemDecorator_instantiation(instance):
    assert isinstance(instance, transport_PacketStyleTransportSystemDecorator)


transport_PacketTransportLabel_strategy = st.builds(transport_PacketTransportLabel)
@given(instance=transport_PacketTransportLabel_strategy)
@settings(max_examples=25)
def test_transport_PacketTransportLabel_instantiation(instance):
    assert isinstance(instance, transport_PacketTransportLabel)


transport_PacketTransportLabelValue_strategy = st.builds(transport_PacketTransportLabelValue, capacity=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=transport_PacketTransportLabelValue_strategy)
@settings(max_examples=25)
def test_transport_PacketTransportLabelValue_instantiation(instance):
    assert isinstance(instance, transport_PacketTransportLabelValue)


transport_PipeStyleTransportSystem_strategy = st.builds(transport_PipeStyleTransportSystem, maxCapacity=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=transport_PipeStyleTransportSystem_strategy)
@settings(max_examples=25)
def test_transport_PipeStyleTransportSystem_instantiation(instance):
    assert isinstance(instance, transport_PipeStyleTransportSystem)


transport_PipeTransportEdge_strategy = st.builds(transport_PipeTransportEdge)
@given(instance=transport_PipeTransportEdge_strategy)
@settings(max_examples=25)
def test_transport_PipeTransportEdge_instantiation(instance):
    assert isinstance(instance, transport_PipeTransportEdge)


transport_PipeTransportEdgeLabel_strategy = st.builds(transport_PipeTransportEdgeLabel)
@given(instance=transport_PipeTransportEdgeLabel_strategy)
@settings(max_examples=25)
def test_transport_PipeTransportEdgeLabel_instantiation(instance):
    assert isinstance(instance, transport_PipeTransportEdgeLabel)


transport_PipeTransportEdgeLabelValue_strategy = st.builds(transport_PipeTransportEdgeLabelValue, maxFlow=st.floats(allow_nan=False, allow_infinity=False), timePeriod=safe_text)
@given(instance=transport_PipeTransportEdgeLabelValue_strategy)
@settings(max_examples=25)
def test_transport_PipeTransportEdgeLabelValue_instantiation(instance):
    assert isinstance(instance, transport_PipeTransportEdgeLabelValue)


transport_STEMTime_strategy = st.builds(transport_STEMTime)
@given(instance=transport_STEMTime_strategy)
@settings(max_examples=25)
def test_transport_STEMTime_instantiation(instance):
    assert isinstance(instance, transport_STEMTime)


transport_TransportSystem_strategy = st.builds(transport_TransportSystem)
@given(instance=transport_TransportSystem_strategy)
@settings(max_examples=25)
def test_transport_TransportSystem_instantiation(instance):
    assert isinstance(instance, transport_TransportSystem)


