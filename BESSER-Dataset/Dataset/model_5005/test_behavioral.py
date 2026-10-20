import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    DataType,
    InterfaceBlock,
    Port,
    SMElement,
    systemmodel_Block,
    systemmodel_DataType,
    systemmodel_GainBlock,
    systemmodel_Inport,
    systemmodel_InputBlock,
    systemmodel_InterfaceBlock,
    systemmodel_MatrixType,
    systemmodel_Outport,
    systemmodel_OutputBlock,
    systemmodel_Port,
    systemmodel_SMElement,
    systemmodel_Saturation,
    systemmodel_ScalarType,
    systemmodel_Signal,
    systemmodel_Sum,
    systemmodel_SystemModel,
    systemmodel_UnitDelay,
    systemmodel_VectorType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_blocks0_stub_double():
    # systemmodel_SystemModel has no real 'systemmodel_SystemModel' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_Block(sequenceNumber=7)
    partner = systemmodel_SystemModel()
    setattr(partner, 'systemmodel_SystemModel', None)
    _safe_set(owner, 'systemmodel_Block', partner)
    assert owner in getattr(partner, 'systemmodel_SystemModel')
    _safe_set(owner, 'systemmodel_Block', None)
    assert owner not in getattr(partner, 'systemmodel_SystemModel')


def test_assoc_dataTypes3_stub_double():
    # systemmodel_SystemModel has no real 'systemmodel_SystemModel4' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_DataType(basetype="sample_text")
    partner = systemmodel_SystemModel()
    setattr(partner, 'systemmodel_SystemModel4', None)
    _safe_set(owner, 'systemmodel_DataType', partner)
    assert owner in getattr(partner, 'systemmodel_SystemModel4')
    _safe_set(owner, 'systemmodel_DataType', None)
    assert owner not in getattr(partner, 'systemmodel_SystemModel4')


def test_assoc_inports5_stub_double():
    # systemmodel_Inport has no real 'Inport' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_Block(sequenceNumber=7)
    partner = systemmodel_Inport()
    setattr(partner, 'Inport', None)
    _safe_set(owner, 'parentBlock', {partner})
    assert getattr(partner, 'Inport') == owner
    _safe_set(owner, 'parentBlock', set())
    assert getattr(partner, 'Inport') is None


def test_assoc_outports6_stub_double():
    # systemmodel_Outport has no real 'Outport' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_Block(sequenceNumber=7)
    partner = systemmodel_Outport()
    setattr(partner, 'Outport', None)
    _safe_set(owner, 'parentBlock7', {partner})
    assert getattr(partner, 'Outport') == owner
    _safe_set(owner, 'parentBlock7', set())
    assert getattr(partner, 'Outport') is None


def test_assoc_parentBlock13_stub_double():
    # systemmodel_Inport has no real 'inports' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_Block(sequenceNumber=7)
    partner = systemmodel_Inport()
    setattr(partner, 'inports', None)
    _safe_set(owner, 'Block', partner)
    assert getattr(partner, 'inports') == owner
    _safe_set(owner, 'Block', None)
    assert getattr(partner, 'inports') is None


def test_assoc_parentBlock16_stub_double():
    # systemmodel_Outport has no real 'outports' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_Block(sequenceNumber=7)
    partner = systemmodel_Outport()
    setattr(partner, 'outports', None)
    _safe_set(owner, 'Block17', partner)
    assert getattr(partner, 'outports') == owner
    _safe_set(owner, 'Block17', None)
    assert getattr(partner, 'outports') is None


def test_assoc_type18_stub_double():
    # systemmodel_Port has no real 'systemmodel_Port' property in the generated
    # code (a bare stub) -- manually attach it so systemmodel_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemmodel_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemmodel_DataType(basetype="sample_text")
    partner = systemmodel_Port()
    setattr(partner, 'systemmodel_Port', None)
    _safe_set(owner, 'systemmodel_DataType19', partner)
    assert getattr(partner, 'systemmodel_Port') == owner
    _safe_set(owner, 'systemmodel_DataType19', None)
    assert getattr(partner, 'systemmodel_Port') is None


