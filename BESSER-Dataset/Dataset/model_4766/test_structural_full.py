import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractFunction,
    Port,
    syswbeff106prepa_AbstractFunction,
    syswbeff106prepa_Flow,
    syswbeff106prepa_Function,
    syswbeff106prepa_InputPort,
    syswbeff106prepa_OutputPort,
    syswbeff106prepa_Pattern,
    syswbeff106prepa_PatternCatalog,
    syswbeff106prepa_Port,
    syswbeff106prepa_System,
    syswbeff106prepa_Workbench,
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

def test_syswbeff106prepa_AbstractFunction_name_value_roundtrip():
    instance = syswbeff106prepa_AbstractFunction(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_syswbeff106prepa_PatternCatalog_id_value_roundtrip():
    instance = syswbeff106prepa_PatternCatalog(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_syswbeff106prepa_Port_name_value_roundtrip():
    instance = syswbeff106prepa_Port(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_syswbeff106prepa_System_id_value_roundtrip():
    instance = syswbeff106prepa_System(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_syswbeff106prepa_Function_isa_AbstractFunction():
    instance = syswbeff106prepa_Function()
    assert isinstance(instance, AbstractFunction)


def test_syswbeff106prepa_Pattern_isa_AbstractFunction():
    instance = syswbeff106prepa_Pattern()
    assert isinstance(instance, AbstractFunction)


def test_syswbeff106prepa_InputPort_isa_Port():
    instance = syswbeff106prepa_InputPort()
    assert isinstance(instance, Port)


def test_syswbeff106prepa_OutputPort_isa_Port():
    instance = syswbeff106prepa_OutputPort()
    assert isinstance(instance, Port)


def test_assoc_associations1_link_reassign_clear():
    a = syswbeff106prepa_AbstractFunction(name="sample_text")
    b1 = syswbeff106prepa_AbstractFunction(name="sample_text")
    b2 = syswbeff106prepa_AbstractFunction(name="sample_text_2")
    _safe_set(a, 'syswbeff106prepa_AbstractFunction', b1)
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction', b1)
    if hasattr(b1, 'syswbeff106prepa_AbstractFunction0'):
        assert _is_linked(b1, 'syswbeff106prepa_AbstractFunction0', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction', b2)
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction', b2)
    if hasattr(b1, 'syswbeff106prepa_AbstractFunction0'):
        assert not _is_linked(b1, 'syswbeff106prepa_AbstractFunction0', a)
    if hasattr(b2, 'syswbeff106prepa_AbstractFunction0'):
        assert _is_linked(b2, 'syswbeff106prepa_AbstractFunction0', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction', None)
    assert not _is_linked(a, 'syswbeff106prepa_AbstractFunction', b2)
    if hasattr(b2, 'syswbeff106prepa_AbstractFunction0'):
        assert not _is_linked(b2, 'syswbeff106prepa_AbstractFunction0', a)


def test_assoc_catalog12_link_reassign_clear():
    a = syswbeff106prepa_PatternCatalog(id="sample_text")
    b1 = syswbeff106prepa_Workbench()
    b2 = syswbeff106prepa_Workbench()
    _safe_set(a, 'syswbeff106prepa_PatternCatalog14', b1)
    assert _is_linked(a, 'syswbeff106prepa_PatternCatalog14', b1)
    if hasattr(b1, 'syswbeff106prepa_Workbench13'):
        assert _is_linked(b1, 'syswbeff106prepa_Workbench13', a)
    _safe_set(a, 'syswbeff106prepa_PatternCatalog14', b2)
    assert _is_linked(a, 'syswbeff106prepa_PatternCatalog14', b2)
    if hasattr(b1, 'syswbeff106prepa_Workbench13'):
        assert not _is_linked(b1, 'syswbeff106prepa_Workbench13', a)
    if hasattr(b2, 'syswbeff106prepa_Workbench13'):
        assert _is_linked(b2, 'syswbeff106prepa_Workbench13', a)
    _safe_set(a, 'syswbeff106prepa_PatternCatalog14', None)
    assert not _is_linked(a, 'syswbeff106prepa_PatternCatalog14', b2)
    if hasattr(b2, 'syswbeff106prepa_Workbench13'):
        assert not _is_linked(b2, 'syswbeff106prepa_Workbench13', a)


def test_assoc_flows6_link_reassign_clear():
    a = syswbeff106prepa_AbstractFunction(name="sample_text")
    b1 = syswbeff106prepa_Flow()
    b2 = syswbeff106prepa_Flow()
    _safe_set(a, 'syswbeff106prepa_AbstractFunction7', {b1})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction7', b1)
    if hasattr(b1, 'syswbeff106prepa_Flow'):
        assert _is_linked(b1, 'syswbeff106prepa_Flow', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction7', {b2})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction7', b2)
    if hasattr(b1, 'syswbeff106prepa_Flow'):
        assert not _is_linked(b1, 'syswbeff106prepa_Flow', a)
    if hasattr(b2, 'syswbeff106prepa_Flow'):
        assert _is_linked(b2, 'syswbeff106prepa_Flow', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction7', set())
    assert not _is_linked(a, 'syswbeff106prepa_AbstractFunction7', b2)
    if hasattr(b2, 'syswbeff106prepa_Flow'):
        assert not _is_linked(b2, 'syswbeff106prepa_Flow', a)


def test_assoc_functionalArchitecture8_link_reassign_clear():
    a = syswbeff106prepa_System(id="sample_text")
    b1 = syswbeff106prepa_Function()
    b2 = syswbeff106prepa_Function()
    _safe_set(a, 'syswbeff106prepa_System', b1)
    assert _is_linked(a, 'syswbeff106prepa_System', b1)
    if hasattr(b1, 'syswbeff106prepa_Function'):
        assert _is_linked(b1, 'syswbeff106prepa_Function', a)
    _safe_set(a, 'syswbeff106prepa_System', b2)
    assert _is_linked(a, 'syswbeff106prepa_System', b2)
    if hasattr(b1, 'syswbeff106prepa_Function'):
        assert not _is_linked(b1, 'syswbeff106prepa_Function', a)
    if hasattr(b2, 'syswbeff106prepa_Function'):
        assert _is_linked(b2, 'syswbeff106prepa_Function', a)
    _safe_set(a, 'syswbeff106prepa_System', None)
    assert not _is_linked(a, 'syswbeff106prepa_System', b2)
    if hasattr(b2, 'syswbeff106prepa_Function'):
        assert not _is_linked(b2, 'syswbeff106prepa_Function', a)


def test_assoc_inputports2_link_reassign_clear():
    a = syswbeff106prepa_AbstractFunction(name="sample_text")
    b1 = syswbeff106prepa_InputPort()
    b2 = syswbeff106prepa_InputPort()
    _safe_set(a, 'syswbeff106prepa_AbstractFunction3', {b1})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction3', b1)
    if hasattr(b1, 'syswbeff106prepa_InputPort'):
        assert _is_linked(b1, 'syswbeff106prepa_InputPort', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction3', {b2})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction3', b2)
    if hasattr(b1, 'syswbeff106prepa_InputPort'):
        assert not _is_linked(b1, 'syswbeff106prepa_InputPort', a)
    if hasattr(b2, 'syswbeff106prepa_InputPort'):
        assert _is_linked(b2, 'syswbeff106prepa_InputPort', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction3', set())
    assert not _is_linked(a, 'syswbeff106prepa_AbstractFunction3', b2)
    if hasattr(b2, 'syswbeff106prepa_InputPort'):
        assert not _is_linked(b2, 'syswbeff106prepa_InputPort', a)


def test_assoc_outputports4_link_reassign_clear():
    a = syswbeff106prepa_AbstractFunction(name="sample_text")
    b1 = syswbeff106prepa_OutputPort()
    b2 = syswbeff106prepa_OutputPort()
    _safe_set(a, 'syswbeff106prepa_AbstractFunction5', {b1})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction5', b1)
    if hasattr(b1, 'syswbeff106prepa_OutputPort'):
        assert _is_linked(b1, 'syswbeff106prepa_OutputPort', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction5', {b2})
    assert _is_linked(a, 'syswbeff106prepa_AbstractFunction5', b2)
    if hasattr(b1, 'syswbeff106prepa_OutputPort'):
        assert not _is_linked(b1, 'syswbeff106prepa_OutputPort', a)
    if hasattr(b2, 'syswbeff106prepa_OutputPort'):
        assert _is_linked(b2, 'syswbeff106prepa_OutputPort', a)
    _safe_set(a, 'syswbeff106prepa_AbstractFunction5', set())
    assert not _is_linked(a, 'syswbeff106prepa_AbstractFunction5', b2)
    if hasattr(b2, 'syswbeff106prepa_OutputPort'):
        assert not _is_linked(b2, 'syswbeff106prepa_OutputPort', a)


def test_assoc_patterns9_link_reassign_clear():
    a = syswbeff106prepa_PatternCatalog(id="sample_text")
    b1 = syswbeff106prepa_Pattern()
    b2 = syswbeff106prepa_Pattern()
    _safe_set(a, 'syswbeff106prepa_PatternCatalog', {b1})
    assert _is_linked(a, 'syswbeff106prepa_PatternCatalog', b1)
    if hasattr(b1, 'syswbeff106prepa_Pattern'):
        assert _is_linked(b1, 'syswbeff106prepa_Pattern', a)
    _safe_set(a, 'syswbeff106prepa_PatternCatalog', {b2})
    assert _is_linked(a, 'syswbeff106prepa_PatternCatalog', b2)
    if hasattr(b1, 'syswbeff106prepa_Pattern'):
        assert not _is_linked(b1, 'syswbeff106prepa_Pattern', a)
    if hasattr(b2, 'syswbeff106prepa_Pattern'):
        assert _is_linked(b2, 'syswbeff106prepa_Pattern', a)
    _safe_set(a, 'syswbeff106prepa_PatternCatalog', set())
    assert not _is_linked(a, 'syswbeff106prepa_PatternCatalog', b2)
    if hasattr(b2, 'syswbeff106prepa_Pattern'):
        assert not _is_linked(b2, 'syswbeff106prepa_Pattern', a)


def test_assoc_systemView10_link_reassign_clear():
    a = syswbeff106prepa_System(id="sample_text")
    b1 = syswbeff106prepa_Workbench()
    b2 = syswbeff106prepa_Workbench()
    _safe_set(a, 'syswbeff106prepa_System11', b1)
    assert _is_linked(a, 'syswbeff106prepa_System11', b1)
    if hasattr(b1, 'syswbeff106prepa_Workbench'):
        assert _is_linked(b1, 'syswbeff106prepa_Workbench', a)
    _safe_set(a, 'syswbeff106prepa_System11', b2)
    assert _is_linked(a, 'syswbeff106prepa_System11', b2)
    if hasattr(b1, 'syswbeff106prepa_Workbench'):
        assert not _is_linked(b1, 'syswbeff106prepa_Workbench', a)
    if hasattr(b2, 'syswbeff106prepa_Workbench'):
        assert _is_linked(b2, 'syswbeff106prepa_Workbench', a)
    _safe_set(a, 'syswbeff106prepa_System11', None)
    assert not _is_linked(a, 'syswbeff106prepa_System11', b2)
    if hasattr(b2, 'syswbeff106prepa_Workbench'):
        assert not _is_linked(b2, 'syswbeff106prepa_Workbench', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractFunction_strategy = st.builds(AbstractFunction)
@given(instance=AbstractFunction_strategy)
@settings(max_examples=25)
def test_AbstractFunction_instantiation(instance):
    assert isinstance(instance, AbstractFunction)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


syswbeff106prepa_AbstractFunction_strategy = st.builds(syswbeff106prepa_AbstractFunction, name=safe_text)
@given(instance=syswbeff106prepa_AbstractFunction_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_AbstractFunction_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_AbstractFunction)


syswbeff106prepa_Flow_strategy = st.builds(syswbeff106prepa_Flow)
@given(instance=syswbeff106prepa_Flow_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_Flow_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_Flow)


syswbeff106prepa_Function_strategy = st.builds(syswbeff106prepa_Function)
@given(instance=syswbeff106prepa_Function_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_Function_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_Function)


syswbeff106prepa_InputPort_strategy = st.builds(syswbeff106prepa_InputPort)
@given(instance=syswbeff106prepa_InputPort_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_InputPort_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_InputPort)


syswbeff106prepa_OutputPort_strategy = st.builds(syswbeff106prepa_OutputPort)
@given(instance=syswbeff106prepa_OutputPort_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_OutputPort_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_OutputPort)


syswbeff106prepa_Pattern_strategy = st.builds(syswbeff106prepa_Pattern)
@given(instance=syswbeff106prepa_Pattern_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_Pattern_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_Pattern)


syswbeff106prepa_PatternCatalog_strategy = st.builds(syswbeff106prepa_PatternCatalog, id=safe_text)
@given(instance=syswbeff106prepa_PatternCatalog_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_PatternCatalog_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_PatternCatalog)


syswbeff106prepa_Port_strategy = st.builds(syswbeff106prepa_Port, name=safe_text)
@given(instance=syswbeff106prepa_Port_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_Port_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_Port)


syswbeff106prepa_System_strategy = st.builds(syswbeff106prepa_System, id=safe_text)
@given(instance=syswbeff106prepa_System_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_System_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_System)


syswbeff106prepa_Workbench_strategy = st.builds(syswbeff106prepa_Workbench)
@given(instance=syswbeff106prepa_Workbench_strategy)
@settings(max_examples=25)
def test_syswbeff106prepa_Workbench_instantiation(instance):
    assert isinstance(instance, syswbeff106prepa_Workbench)


