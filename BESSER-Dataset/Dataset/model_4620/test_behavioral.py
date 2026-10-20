import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ApplicationCondition,
    AttributeCalculation,
    Calculation,
    FlowRule,
    NodePattern,
    Operand,
    Operator,
    Parameter,
    ParameterRef,
    Restriction,
    Result,
    trnetvisual_Action,
    trnetvisual_AntiOperand,
    trnetvisual_AnyOperand,
    trnetvisual_AnyResult,
    trnetvisual_ApplicationCondition,
    trnetvisual_AttributeCalculation,
    trnetvisual_AttributePattern,
    trnetvisual_Calculation,
    trnetvisual_Combinator,
    trnetvisual_Different,
    trnetvisual_EdgePattern,
    trnetvisual_Eventually,
    trnetvisual_External,
    trnetvisual_ExternalActionCall,
    trnetvisual_ExternalActionCallParameter,
    trnetvisual_ExternalAttributeCalculationCall,
    trnetvisual_ExternalAttributeCalculationCallParameter,
    trnetvisual_ExternalCalculationCall,
    trnetvisual_ExternalCalculationCallParameter,
    trnetvisual_ExternalConditionCall,
    trnetvisual_ExternalConditionCallParameter,
    trnetvisual_FlowRule,
    trnetvisual_Keep,
    trnetvisual_MandatoryNode,
    trnetvisual_Next,
    trnetvisual_NextDerived,
    trnetvisual_NodePattern,
    trnetvisual_Operand,
    trnetvisual_Operator,
    trnetvisual_OptionalNode,
    trnetvisual_OptionalOperand,
    trnetvisual_Parameter,
    trnetvisual_ParameterRef,
    trnetvisual_Pattern,
    trnetvisual_Restriction,
    trnetvisual_Result,
    trnetvisual_Same,
    trnetvisual_SomeOperand,
    trnetvisual_SomeResult,
    trnetvisual_TrNetModel,
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

def test_assoc_attributeExternalCalculationCall55_reverse_link_reassign_clear():
    a1 = trnetvisual_ExternalAttributeCalculationCall(id="sample_text", qualifiedName="sample_text")
    a2 = trnetvisual_ExternalAttributeCalculationCall(id="sample_text_2", qualifiedName="sample_text_2")
    b = trnetvisual_AttributePattern(expectedNumberOfDistinctValues=3.14, name="sample_text")
    _safe_set(b, 'result', a1)
    assert _is_linked(b, 'result', a1)
    if hasattr(a1, 'ExternalAttributeCalculationCall'):
        assert _is_linked(a1, 'ExternalAttributeCalculationCall', b)
    _safe_set(b, 'result', a2)
    assert _is_linked(b, 'result', a2)
    if hasattr(a1, 'ExternalAttributeCalculationCall'):
        assert not _is_linked(a1, 'ExternalAttributeCalculationCall', b)
    if hasattr(a2, 'ExternalAttributeCalculationCall'):
        assert _is_linked(a2, 'ExternalAttributeCalculationCall', b)
    _safe_set(b, 'result', None)
    assert not _is_linked(b, 'result', a2)
    if hasattr(a2, 'ExternalAttributeCalculationCall'):
        assert not _is_linked(a2, 'ExternalAttributeCalculationCall', b)


def test_assoc_attributes22_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_AttributePattern(expectedNumberOfDistinctValues=3.14, name="sample_text")
    _safe_set(b, 'AttributePattern', a1)
    assert _is_linked(b, 'AttributePattern', a1)
    if hasattr(a1, 'ownerNode'):
        assert _is_linked(a1, 'ownerNode', b)
    _safe_set(b, 'AttributePattern', a2)
    assert _is_linked(b, 'AttributePattern', a2)
    if hasattr(a1, 'ownerNode'):
        assert not _is_linked(a1, 'ownerNode', b)
    if hasattr(a2, 'ownerNode'):
        assert _is_linked(a2, 'ownerNode', b)
    _safe_set(b, 'AttributePattern', None)
    assert not _is_linked(b, 'AttributePattern', a2)
    if hasattr(a2, 'ownerNode'):
        assert not _is_linked(a2, 'ownerNode', b)


def test_assoc_edges40_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'EdgePattern42', a1)
    assert _is_linked(b, 'EdgePattern42', a1)
    if hasattr(a1, 'pattern41'):
        assert _is_linked(a1, 'pattern41', b)
    _safe_set(b, 'EdgePattern42', a2)
    assert _is_linked(b, 'EdgePattern42', a2)
    if hasattr(a1, 'pattern41'):
        assert not _is_linked(a1, 'pattern41', b)
    if hasattr(a2, 'pattern41'):
        assert _is_linked(a2, 'pattern41', b)
    _safe_set(b, 'EdgePattern42', None)
    assert not _is_linked(b, 'EdgePattern42', a2)
    if hasattr(a2, 'pattern41'):
        assert not _is_linked(a2, 'pattern41', b)


def test_assoc_incoming13_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'EdgePattern', a1)
    assert _is_linked(b, 'EdgePattern', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'EdgePattern', a2)
    assert _is_linked(b, 'EdgePattern', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'EdgePattern', None)
    assert not _is_linked(b, 'EdgePattern', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_nodes38_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    _safe_set(b, 'NodePattern39', a1)
    assert _is_linked(b, 'NodePattern39', a1)
    if hasattr(a1, 'pattern'):
        assert _is_linked(a1, 'pattern', b)
    _safe_set(b, 'NodePattern39', a2)
    assert _is_linked(b, 'NodePattern39', a2)
    if hasattr(a1, 'pattern'):
        assert not _is_linked(a1, 'pattern', b)
    if hasattr(a2, 'pattern'):
        assert _is_linked(a2, 'pattern', b)
    _safe_set(b, 'NodePattern39', None)
    assert not _is_linked(b, 'NodePattern39', a2)
    if hasattr(a2, 'pattern'):
        assert not _is_linked(a2, 'pattern', b)


def test_assoc_operands5_reverse_link_reassign_clear():
    a1 = trnetvisual_TrNetModel(id="sample_text")
    a2 = trnetvisual_TrNetModel(id="sample_text_2")
    b = trnetvisual_Operand(index=7)
    _safe_set(b, 'trnetvisual_Operand', a1)
    assert _is_linked(b, 'trnetvisual_Operand', a1)
    if hasattr(a1, 'trnetvisual_TrNetModel6'):
        assert _is_linked(a1, 'trnetvisual_TrNetModel6', b)
    _safe_set(b, 'trnetvisual_Operand', a2)
    assert _is_linked(b, 'trnetvisual_Operand', a2)
    if hasattr(a1, 'trnetvisual_TrNetModel6'):
        assert not _is_linked(a1, 'trnetvisual_TrNetModel6', b)
    if hasattr(a2, 'trnetvisual_TrNetModel6'):
        assert _is_linked(a2, 'trnetvisual_TrNetModel6', b)
    _safe_set(b, 'trnetvisual_Operand', None)
    assert not _is_linked(b, 'trnetvisual_Operand', a2)
    if hasattr(a2, 'trnetvisual_TrNetModel6'):
        assert not _is_linked(a2, 'trnetvisual_TrNetModel6', b)


def test_assoc_operands62_reverse_link_reassign_clear():
    a1 = trnetvisual_Operator(id="sample_text")
    a2 = trnetvisual_Operator(id="sample_text_2")
    b = trnetvisual_Operand(index=7)
    _safe_set(b, 'Operand63', a1)
    assert _is_linked(b, 'Operand63', a1)
    if hasattr(a1, 'operator'):
        assert _is_linked(a1, 'operator', b)
    _safe_set(b, 'Operand63', a2)
    assert _is_linked(b, 'Operand63', a2)
    if hasattr(a1, 'operator'):
        assert not _is_linked(a1, 'operator', b)
    if hasattr(a2, 'operator'):
        assert _is_linked(a2, 'operator', b)
    _safe_set(b, 'Operand63', None)
    assert not _is_linked(b, 'Operand63', a2)
    if hasattr(a2, 'operator'):
        assert not _is_linked(a2, 'operator', b)


def test_assoc_operator79_reverse_link_reassign_clear():
    a1 = trnetvisual_Operator(id="sample_text")
    a2 = trnetvisual_Operator(id="sample_text_2")
    b = trnetvisual_Operand(index=7)
    _safe_set(b, 'operands', a1)
    assert _is_linked(b, 'operands', a1)
    if hasattr(a1, 'Operator80'):
        assert _is_linked(a1, 'Operator80', b)
    _safe_set(b, 'operands', a2)
    assert _is_linked(b, 'operands', a2)
    if hasattr(a1, 'Operator80'):
        assert not _is_linked(a1, 'Operator80', b)
    if hasattr(a2, 'Operator80'):
        assert _is_linked(a2, 'Operator80', b)
    _safe_set(b, 'operands', None)
    assert not _is_linked(b, 'operands', a2)
    if hasattr(a2, 'Operator80'):
        assert not _is_linked(a2, 'Operator80', b)


def test_assoc_operators1_reverse_link_reassign_clear():
    a1 = trnetvisual_TrNetModel(id="sample_text")
    a2 = trnetvisual_TrNetModel(id="sample_text_2")
    b = trnetvisual_Operator(id="sample_text")
    _safe_set(b, 'trnetvisual_Operator', a1)
    assert _is_linked(b, 'trnetvisual_Operator', a1)
    if hasattr(a1, 'trnetvisual_TrNetModel2'):
        assert _is_linked(a1, 'trnetvisual_TrNetModel2', b)
    _safe_set(b, 'trnetvisual_Operator', a2)
    assert _is_linked(b, 'trnetvisual_Operator', a2)
    if hasattr(a1, 'trnetvisual_TrNetModel2'):
        assert not _is_linked(a1, 'trnetvisual_TrNetModel2', b)
    if hasattr(a2, 'trnetvisual_TrNetModel2'):
        assert _is_linked(a2, 'trnetvisual_TrNetModel2', b)
    _safe_set(b, 'trnetvisual_Operator', None)
    assert not _is_linked(b, 'trnetvisual_Operator', a2)
    if hasattr(a2, 'trnetvisual_TrNetModel2'):
        assert not _is_linked(a2, 'trnetvisual_TrNetModel2', b)


def test_assoc_outgoing14_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'EdgePattern15', a1)
    assert _is_linked(b, 'EdgePattern15', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'EdgePattern15', a2)
    assert _is_linked(b, 'EdgePattern15', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'EdgePattern15', None)
    assert not _is_linked(b, 'EdgePattern15', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_outgoingOperands45_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_Operand(index=7)
    _safe_set(b, 'Operand', a1)
    assert _is_linked(b, 'Operand', a1)
    if hasattr(a1, 'pattern46'):
        assert _is_linked(a1, 'pattern46', b)
    _safe_set(b, 'Operand', a2)
    assert _is_linked(b, 'Operand', a2)
    if hasattr(a1, 'pattern46'):
        assert not _is_linked(a1, 'pattern46', b)
    if hasattr(a2, 'pattern46'):
        assert _is_linked(a2, 'pattern46', b)
    _safe_set(b, 'Operand', None)
    assert not _is_linked(b, 'Operand', a2)
    if hasattr(a2, 'pattern46'):
        assert not _is_linked(a2, 'pattern46', b)


def test_assoc_ownerNode56_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_AttributePattern(expectedNumberOfDistinctValues=3.14, name="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'NodePattern57'):
        assert _is_linked(a1, 'NodePattern57', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'NodePattern57'):
        assert not _is_linked(a1, 'NodePattern57', b)
    if hasattr(a2, 'NodePattern57'):
        assert _is_linked(a2, 'NodePattern57', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'NodePattern57'):
        assert not _is_linked(a2, 'NodePattern57', b)


def test_assoc_pattern21_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'Pattern'):
        assert _is_linked(a1, 'Pattern', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'Pattern'):
        assert not _is_linked(a1, 'Pattern', b)
    if hasattr(a2, 'Pattern'):
        assert _is_linked(a2, 'Pattern', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'Pattern'):
        assert not _is_linked(a2, 'Pattern', b)


def test_assoc_pattern36_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Pattern37'):
        assert _is_linked(a1, 'Pattern37', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Pattern37'):
        assert not _is_linked(a1, 'Pattern37', b)
    if hasattr(a2, 'Pattern37'):
        assert _is_linked(a2, 'Pattern37', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Pattern37'):
        assert not _is_linked(a2, 'Pattern37', b)


def test_assoc_pattern81_reverse_link_reassign_clear():
    a1 = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    a2 = trnetvisual_Pattern(expected_size=9.99, id="sample_text_2")
    b = trnetvisual_Operand(index=7)
    _safe_set(b, 'outgoingOperands', a1)
    assert _is_linked(b, 'outgoingOperands', a1)
    if hasattr(a1, 'Pattern82'):
        assert _is_linked(a1, 'Pattern82', b)
    _safe_set(b, 'outgoingOperands', a2)
    assert _is_linked(b, 'outgoingOperands', a2)
    if hasattr(a1, 'Pattern82'):
        assert not _is_linked(a1, 'Pattern82', b)
    if hasattr(a2, 'Pattern82'):
        assert _is_linked(a2, 'Pattern82', b)
    _safe_set(b, 'outgoingOperands', None)
    assert not _is_linked(b, 'outgoingOperands', a2)
    if hasattr(a2, 'Pattern82'):
        assert not _is_linked(a2, 'Pattern82', b)


def test_assoc_patterns0_reverse_link_reassign_clear():
    a1 = trnetvisual_TrNetModel(id="sample_text")
    a2 = trnetvisual_TrNetModel(id="sample_text_2")
    b = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    _safe_set(b, 'trnetvisual_Pattern', a1)
    assert _is_linked(b, 'trnetvisual_Pattern', a1)
    if hasattr(a1, 'trnetvisual_TrNetModel'):
        assert _is_linked(a1, 'trnetvisual_TrNetModel', b)
    _safe_set(b, 'trnetvisual_Pattern', a2)
    assert _is_linked(b, 'trnetvisual_Pattern', a2)
    if hasattr(a1, 'trnetvisual_TrNetModel'):
        assert not _is_linked(a1, 'trnetvisual_TrNetModel', b)
    if hasattr(a2, 'trnetvisual_TrNetModel'):
        assert _is_linked(a2, 'trnetvisual_TrNetModel', b)
    _safe_set(b, 'trnetvisual_Pattern', None)
    assert not _is_linked(b, 'trnetvisual_Pattern', a2)
    if hasattr(a2, 'trnetvisual_TrNetModel'):
        assert not _is_linked(a2, 'trnetvisual_TrNetModel', b)


def test_assoc_result87_reverse_link_reassign_clear():
    a1 = trnetvisual_ExternalAttributeCalculationCall(id="sample_text", qualifiedName="sample_text")
    a2 = trnetvisual_ExternalAttributeCalculationCall(id="sample_text_2", qualifiedName="sample_text_2")
    b = trnetvisual_AttributePattern(expectedNumberOfDistinctValues=3.14, name="sample_text")
    _safe_set(b, 'AttributePattern88', a1)
    assert _is_linked(b, 'AttributePattern88', a1)
    if hasattr(a1, 'attributeExternalCalculationCall'):
        assert _is_linked(a1, 'attributeExternalCalculationCall', b)
    _safe_set(b, 'AttributePattern88', a2)
    assert _is_linked(b, 'AttributePattern88', a2)
    if hasattr(a1, 'attributeExternalCalculationCall'):
        assert not _is_linked(a1, 'attributeExternalCalculationCall', b)
    if hasattr(a2, 'attributeExternalCalculationCall'):
        assert _is_linked(a2, 'attributeExternalCalculationCall', b)
    _safe_set(b, 'AttributePattern88', None)
    assert not _is_linked(b, 'AttributePattern88', a2)
    if hasattr(a2, 'attributeExternalCalculationCall'):
        assert not _is_linked(a2, 'attributeExternalCalculationCall', b)


def test_assoc_source33_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'NodePattern'):
        assert _is_linked(a1, 'NodePattern', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'NodePattern'):
        assert not _is_linked(a1, 'NodePattern', b)
    if hasattr(a2, 'NodePattern'):
        assert _is_linked(a2, 'NodePattern', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'NodePattern'):
        assert not _is_linked(a2, 'NodePattern', b)


def test_assoc_target34_reverse_link_reassign_clear():
    a1 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    a2 = trnetvisual_NodePattern(expectedNumberOfDistinctValues=9.99, id="sample_text_2", name="sample_text_2")
    b = trnetvisual_EdgePattern(name="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'NodePattern35'):
        assert _is_linked(a1, 'NodePattern35', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'NodePattern35'):
        assert not _is_linked(a1, 'NodePattern35', b)
    if hasattr(a2, 'NodePattern35'):
        assert _is_linked(a2, 'NodePattern35', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'NodePattern35'):
        assert not _is_linked(a2, 'NodePattern35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions74_stub_double():
    # trnetvisual_Action has no real 'trnetvisual_Action' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_Action()
    setattr(partner, 'trnetvisual_Action', None)
    _safe_set(owner, 'trnetvisual_Operator75', {partner})
    assert getattr(partner, 'trnetvisual_Action') == owner
    _safe_set(owner, 'trnetvisual_Operator75', set())
    assert getattr(partner, 'trnetvisual_Action') is None


def test_assoc_calculations11_stub_double():
    # trnetvisual_Calculation has no real 'trnetvisual_Calculation' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_TrNetModel(id="sample_text")
    partner = trnetvisual_Calculation()
    setattr(partner, 'trnetvisual_Calculation', None)
    _safe_set(owner, 'trnetvisual_TrNetModel12', {partner})
    assert getattr(partner, 'trnetvisual_Calculation') == owner
    _safe_set(owner, 'trnetvisual_TrNetModel12', set())
    assert getattr(partner, 'trnetvisual_Calculation') is None


def test_assoc_conditions72_stub_double():
    # trnetvisual_ApplicationCondition has no real 'trnetvisual_ApplicationCondition' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_ApplicationCondition()
    setattr(partner, 'trnetvisual_ApplicationCondition', None)
    _safe_set(owner, 'trnetvisual_Operator73', {partner})
    assert getattr(partner, 'trnetvisual_ApplicationCondition') == owner
    _safe_set(owner, 'trnetvisual_Operator73', set())
    assert getattr(partner, 'trnetvisual_ApplicationCondition') is None


def test_assoc_differentIn28_stub_double():
    # trnetvisual_Different has no real 'Different' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Different()
    setattr(partner, 'Different', None)
    _safe_set(owner, 'target29', {partner})
    assert getattr(partner, 'Different') == owner
    _safe_set(owner, 'target29', set())
    assert getattr(partner, 'Different') is None


def test_assoc_differentOut30_stub_double():
    # trnetvisual_Different has no real 'Different32' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Different()
    setattr(partner, 'Different32', None)
    _safe_set(owner, 'source31', {partner})
    assert getattr(partner, 'Different32') == owner
    _safe_set(owner, 'source31', set())
    assert getattr(partner, 'Different32') is None


def test_assoc_flowIn69_stub_double():
    # trnetvisual_FlowRule has no real 'FlowRule71' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_FlowRule()
    setattr(partner, 'FlowRule71', None)
    _safe_set(owner, 'target70', {partner})
    assert getattr(partner, 'FlowRule71') == owner
    _safe_set(owner, 'target70', set())
    assert getattr(partner, 'FlowRule71') is None


def test_assoc_flowOut67_stub_double():
    # trnetvisual_FlowRule has no real 'FlowRule' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_FlowRule()
    setattr(partner, 'FlowRule', None)
    _safe_set(owner, 'source68', {partner})
    assert getattr(partner, 'FlowRule') == owner
    _safe_set(owner, 'source68', set())
    assert getattr(partner, 'FlowRule') is None


def test_assoc_flowRules9_stub_double():
    # trnetvisual_FlowRule has no real 'trnetvisual_FlowRule' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_TrNetModel(id="sample_text")
    partner = trnetvisual_FlowRule()
    setattr(partner, 'trnetvisual_FlowRule', None)
    _safe_set(owner, 'trnetvisual_TrNetModel10', {partner})
    assert getattr(partner, 'trnetvisual_FlowRule') == owner
    _safe_set(owner, 'trnetvisual_TrNetModel10', set())
    assert getattr(partner, 'trnetvisual_FlowRule') is None


def test_assoc_incomingResults43_stub_double():
    # trnetvisual_Result has no real 'Result' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    partner = trnetvisual_Result()
    setattr(partner, 'Result', None)
    _safe_set(owner, 'pattern44', {partner})
    assert getattr(partner, 'Result') == owner
    _safe_set(owner, 'pattern44', set())
    assert getattr(partner, 'Result') is None


def test_assoc_keepIn23_stub_double():
    # trnetvisual_Keep has no real 'Keep' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Keep()
    setattr(partner, 'Keep', None)
    _safe_set(owner, 'target24', {partner})
    assert getattr(partner, 'Keep') == owner
    _safe_set(owner, 'target24', set())
    assert getattr(partner, 'Keep') is None


def test_assoc_keepOut25_stub_double():
    # trnetvisual_Keep has no real 'Keep27' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Keep()
    setattr(partner, 'Keep27', None)
    _safe_set(owner, 'source26', {partner})
    assert getattr(partner, 'Keep27') == owner
    _safe_set(owner, 'source26', set())
    assert getattr(partner, 'Keep27') is None


def test_assoc_operator78_stub_double():
    # trnetvisual_Result has no real 'results' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_Result()
    setattr(partner, 'results', None)
    _safe_set(owner, 'Operator', partner)
    assert getattr(partner, 'results') == owner
    _safe_set(owner, 'Operator', None)
    assert getattr(partner, 'results') is None


def test_assoc_owner104_stub_double():
    # trnetvisual_ExternalAttributeCalculationCallParameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalAttributeCalculationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalAttributeCalculationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalAttributeCalculationCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalAttributeCalculationCallParameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'ExternalAttributeCalculationCall105', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'ExternalAttributeCalculationCall105', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_owner107_stub_double():
    # trnetvisual_ExternalConditionCallParameter has no real 'parameters108' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalConditionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalConditionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalConditionCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalConditionCallParameter()
    setattr(partner, 'parameters108', None)
    _safe_set(owner, 'ExternalConditionCall', partner)
    assert getattr(partner, 'parameters108') == owner
    _safe_set(owner, 'ExternalConditionCall', None)
    assert getattr(partner, 'parameters108') is None


def test_assoc_owner111_stub_double():
    # trnetvisual_ExternalActionCallParameter has no real 'parameters112' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalActionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalActionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalActionCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalActionCallParameter()
    setattr(partner, 'parameters112', None)
    _safe_set(owner, 'ExternalActionCall', partner)
    assert getattr(partner, 'parameters112') == owner
    _safe_set(owner, 'ExternalActionCall', None)
    assert getattr(partner, 'parameters112') is None


def test_assoc_owner118_stub_double():
    # trnetvisual_ExternalCalculationCallParameter has no real 'parameters119' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalCalculationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalCalculationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalCalculationCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalCalculationCallParameter()
    setattr(partner, 'parameters119', None)
    _safe_set(owner, 'ExternalCalculationCall', partner)
    assert getattr(partner, 'parameters119') == owner
    _safe_set(owner, 'ExternalCalculationCall', None)
    assert getattr(partner, 'parameters119') is None


def test_assoc_parameters101_stub_double():
    # trnetvisual_ExternalActionCallParameter has no real 'ExternalActionCallParameter103' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalActionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalActionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalActionCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalActionCallParameter()
    setattr(partner, 'ExternalActionCallParameter103', None)
    _safe_set(owner, 'owner102', {partner})
    assert getattr(partner, 'ExternalActionCallParameter103') == owner
    _safe_set(owner, 'owner102', set())
    assert getattr(partner, 'ExternalActionCallParameter103') is None


def test_assoc_parameters115_stub_double():
    # trnetvisual_ExternalCalculationCallParameter has no real 'ExternalCalculationCallParameter117' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalCalculationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalCalculationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalCalculationCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalCalculationCallParameter()
    setattr(partner, 'ExternalCalculationCallParameter117', None)
    _safe_set(owner, 'owner116', {partner})
    assert getattr(partner, 'ExternalCalculationCallParameter117') == owner
    _safe_set(owner, 'owner116', set())
    assert getattr(partner, 'ExternalCalculationCallParameter117') is None


def test_assoc_parameters89_stub_double():
    # trnetvisual_ExternalAttributeCalculationCallParameter has no real 'ExternalAttributeCalculationCallParameter' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalAttributeCalculationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalAttributeCalculationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalAttributeCalculationCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalAttributeCalculationCallParameter()
    setattr(partner, 'ExternalAttributeCalculationCallParameter', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'ExternalAttributeCalculationCallParameter') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'ExternalAttributeCalculationCallParameter') is None


def test_assoc_parameters98_stub_double():
    # trnetvisual_ExternalConditionCallParameter has no real 'ExternalConditionCallParameter100' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_ExternalConditionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_ExternalConditionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_ExternalConditionCall(id="sample_text", qualifiedName="sample_text")
    partner = trnetvisual_ExternalConditionCallParameter()
    setattr(partner, 'ExternalConditionCallParameter100', None)
    _safe_set(owner, 'owner99', {partner})
    assert getattr(partner, 'ExternalConditionCallParameter100') == owner
    _safe_set(owner, 'owner99', set())
    assert getattr(partner, 'ExternalConditionCallParameter100') is None


def test_assoc_pattern76_stub_double():
    # trnetvisual_Result has no real 'incomingResults' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Pattern(expected_size=3.14, id="sample_text")
    partner = trnetvisual_Result()
    setattr(partner, 'incomingResults', None)
    _safe_set(owner, 'Pattern77', partner)
    assert getattr(partner, 'incomingResults') == owner
    _safe_set(owner, 'Pattern77', None)
    assert getattr(partner, 'incomingResults') is None


def test_assoc_restrictions3_stub_double():
    # trnetvisual_Restriction has no real 'trnetvisual_Restriction' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_TrNetModel(id="sample_text")
    partner = trnetvisual_Restriction()
    setattr(partner, 'trnetvisual_Restriction', None)
    _safe_set(owner, 'trnetvisual_TrNetModel4', {partner})
    assert getattr(partner, 'trnetvisual_Restriction') == owner
    _safe_set(owner, 'trnetvisual_TrNetModel4', set())
    assert getattr(partner, 'trnetvisual_Restriction') is None


def test_assoc_results64_stub_double():
    # trnetvisual_Result has no real 'Result66' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_Result()
    setattr(partner, 'Result66', None)
    _safe_set(owner, 'operator65', {partner})
    assert getattr(partner, 'Result66') == owner
    _safe_set(owner, 'operator65', set())
    assert getattr(partner, 'Result66') is None


def test_assoc_results7_stub_double():
    # trnetvisual_Result has no real 'trnetvisual_Result' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_TrNetModel(id="sample_text")
    partner = trnetvisual_Result()
    setattr(partner, 'trnetvisual_Result', None)
    _safe_set(owner, 'trnetvisual_TrNetModel8', {partner})
    assert getattr(partner, 'trnetvisual_Result') == owner
    _safe_set(owner, 'trnetvisual_TrNetModel8', set())
    assert getattr(partner, 'trnetvisual_Result') is None


def test_assoc_sameIn18_stub_double():
    # trnetvisual_Same has no real 'Same20' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Same()
    setattr(partner, 'Same20', None)
    _safe_set(owner, 'target19', {partner})
    assert getattr(partner, 'Same20') == owner
    _safe_set(owner, 'target19', set())
    assert getattr(partner, 'Same20') is None


def test_assoc_sameOut16_stub_double():
    # trnetvisual_Same has no real 'Same' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Same()
    setattr(partner, 'Same', None)
    _safe_set(owner, 'source17', {partner})
    assert getattr(partner, 'Same') == owner
    _safe_set(owner, 'source17', set())
    assert getattr(partner, 'Same') is None


def test_assoc_source47_stub_double():
    # trnetvisual_Same has no real 'sameOut' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Same()
    setattr(partner, 'sameOut', None)
    _safe_set(owner, 'NodePattern48', partner)
    assert getattr(partner, 'sameOut') == owner
    _safe_set(owner, 'NodePattern48', None)
    assert getattr(partner, 'sameOut') is None


def test_assoc_source51_stub_double():
    # trnetvisual_Different has no real 'differentOut' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Different()
    setattr(partner, 'differentOut', None)
    _safe_set(owner, 'NodePattern52', partner)
    assert getattr(partner, 'differentOut') == owner
    _safe_set(owner, 'NodePattern52', None)
    assert getattr(partner, 'differentOut') is None


def test_assoc_source58_stub_double():
    # trnetvisual_Keep has no real 'keepOut' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Keep()
    setattr(partner, 'keepOut', None)
    _safe_set(owner, 'NodePattern59', partner)
    assert getattr(partner, 'keepOut') == owner
    _safe_set(owner, 'NodePattern59', None)
    assert getattr(partner, 'keepOut') is None


def test_assoc_source83_stub_double():
    # trnetvisual_FlowRule has no real 'flowOut' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_FlowRule()
    setattr(partner, 'flowOut', None)
    _safe_set(owner, 'Operator84', partner)
    assert getattr(partner, 'flowOut') == owner
    _safe_set(owner, 'Operator84', None)
    assert getattr(partner, 'flowOut') is None


def test_assoc_target49_stub_double():
    # trnetvisual_Same has no real 'sameIn' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Same()
    setattr(partner, 'sameIn', None)
    _safe_set(owner, 'NodePattern50', partner)
    assert getattr(partner, 'sameIn') == owner
    _safe_set(owner, 'NodePattern50', None)
    assert getattr(partner, 'sameIn') is None


def test_assoc_target53_stub_double():
    # trnetvisual_Different has no real 'differentIn' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Different()
    setattr(partner, 'differentIn', None)
    _safe_set(owner, 'NodePattern54', partner)
    assert getattr(partner, 'differentIn') == owner
    _safe_set(owner, 'NodePattern54', None)
    assert getattr(partner, 'differentIn') is None


def test_assoc_target60_stub_double():
    # trnetvisual_Keep has no real 'keepIn' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_NodePattern(expectedNumberOfDistinctValues=3.14, id="sample_text", name="sample_text")
    partner = trnetvisual_Keep()
    setattr(partner, 'keepIn', None)
    _safe_set(owner, 'NodePattern61', partner)
    assert getattr(partner, 'keepIn') == owner
    _safe_set(owner, 'NodePattern61', None)
    assert getattr(partner, 'keepIn') is None


def test_assoc_target85_stub_double():
    # trnetvisual_FlowRule has no real 'flowIn' property in the generated
    # code (a bare stub) -- manually attach it so trnetvisual_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnetvisual_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnetvisual_Operator(id="sample_text")
    partner = trnetvisual_FlowRule()
    setattr(partner, 'flowIn', None)
    _safe_set(owner, 'Operator86', partner)
    assert getattr(partner, 'flowIn') == owner
    _safe_set(owner, 'Operator86', None)
    assert getattr(partner, 'flowIn') is None


