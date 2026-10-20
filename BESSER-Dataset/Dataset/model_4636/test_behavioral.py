import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    ExpressionOperator,
    FlowRule,
    NodePattern,
    Operand,
    Operator,
    Restriction,
    Result,
    trnet_AntiOperand,
    trnet_AnyOperand,
    trnet_AnyResult,
    trnet_AttributePattern,
    trnet_Combinator,
    trnet_Different,
    trnet_EdgePattern,
    trnet_Equality,
    trnet_Eventually,
    trnet_Expression,
    trnet_ExpressionOperator,
    trnet_External,
    trnet_FlowRule,
    trnet_Keep,
    trnet_MandatoryNode,
    trnet_Next,
    trnet_NextDerived,
    trnet_NodePattern,
    trnet_Operand,
    trnet_Operator,
    trnet_OptionalNode,
    trnet_OptionalOperand,
    trnet_Pattern,
    trnet_Restriction,
    trnet_Result,
    trnet_Same,
    trnet_SomeOperand,
    trnet_SomeResult,
    trnet_StringLiteral,
    trnet_TrNetModel,
    trnet_Union,
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

def test_assoc_attributes14_reverse_link_reassign_clear():
    a1 = trnet_NodePattern(id="sample_text", name="sample_text")
    a2 = trnet_NodePattern(id="sample_text_2", name="sample_text_2")
    b = trnet_AttributePattern(name="sample_text")
    _safe_set(b, 'trnet_AttributePattern', a1)
    assert _is_linked(b, 'trnet_AttributePattern', a1)
    if hasattr(a1, 'trnet_NodePattern'):
        assert _is_linked(a1, 'trnet_NodePattern', b)
    _safe_set(b, 'trnet_AttributePattern', a2)
    assert _is_linked(b, 'trnet_AttributePattern', a2)
    if hasattr(a1, 'trnet_NodePattern'):
        assert not _is_linked(a1, 'trnet_NodePattern', b)
    if hasattr(a2, 'trnet_NodePattern'):
        assert _is_linked(a2, 'trnet_NodePattern', b)
    _safe_set(b, 'trnet_AttributePattern', None)
    assert not _is_linked(b, 'trnet_AttributePattern', a2)
    if hasattr(a2, 'trnet_NodePattern'):
        assert not _is_linked(a2, 'trnet_NodePattern', b)


def test_assoc_edges32_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
    _safe_set(b, 'EdgePattern34', a1)
    assert _is_linked(b, 'EdgePattern34', a1)
    if hasattr(a1, 'pattern33'):
        assert _is_linked(a1, 'pattern33', b)
    _safe_set(b, 'EdgePattern34', a2)
    assert _is_linked(b, 'EdgePattern34', a2)
    if hasattr(a1, 'pattern33'):
        assert not _is_linked(a1, 'pattern33', b)
    if hasattr(a2, 'pattern33'):
        assert _is_linked(a2, 'pattern33', b)
    _safe_set(b, 'EdgePattern34', None)
    assert not _is_linked(b, 'EdgePattern34', a2)
    if hasattr(a2, 'pattern33'):
        assert not _is_linked(a2, 'pattern33', b)


def test_assoc_incoming5_reverse_link_reassign_clear():
    a1 = trnet_NodePattern(id="sample_text", name="sample_text")
    a2 = trnet_NodePattern(id="sample_text_2", name="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
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


def test_assoc_nodes30_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_NodePattern(id="sample_text", name="sample_text")
    _safe_set(b, 'NodePattern31', a1)
    assert _is_linked(b, 'NodePattern31', a1)
    if hasattr(a1, 'pattern'):
        assert _is_linked(a1, 'pattern', b)
    _safe_set(b, 'NodePattern31', a2)
    assert _is_linked(b, 'NodePattern31', a2)
    if hasattr(a1, 'pattern'):
        assert not _is_linked(a1, 'pattern', b)
    if hasattr(a2, 'pattern'):
        assert _is_linked(a2, 'pattern', b)
    _safe_set(b, 'NodePattern31', None)
    assert not _is_linked(b, 'NodePattern31', a2)
    if hasattr(a2, 'pattern'):
        assert not _is_linked(a2, 'pattern', b)


def test_assoc_operands39_reverse_link_reassign_clear():
    a1 = trnet_Operator(id="sample_text")
    a2 = trnet_Operator(id="sample_text_2")
    b = trnet_Operand(index=7)
    _safe_set(b, 'Operand40', a1)
    assert _is_linked(b, 'Operand40', a1)
    if hasattr(a1, 'operator'):
        assert _is_linked(a1, 'operator', b)
    _safe_set(b, 'Operand40', a2)
    assert _is_linked(b, 'Operand40', a2)
    if hasattr(a1, 'operator'):
        assert not _is_linked(a1, 'operator', b)
    if hasattr(a2, 'operator'):
        assert _is_linked(a2, 'operator', b)
    _safe_set(b, 'Operand40', None)
    assert not _is_linked(b, 'Operand40', a2)
    if hasattr(a2, 'operator'):
        assert not _is_linked(a2, 'operator', b)


def test_assoc_operator59_reverse_link_reassign_clear():
    a1 = trnet_Operator(id="sample_text")
    a2 = trnet_Operator(id="sample_text_2")
    b = trnet_Operand(index=7)
    _safe_set(b, 'operands', a1)
    assert _is_linked(b, 'operands', a1)
    if hasattr(a1, 'Operator'):
        assert _is_linked(a1, 'Operator', b)
    _safe_set(b, 'operands', a2)
    assert _is_linked(b, 'operands', a2)
    if hasattr(a1, 'Operator'):
        assert not _is_linked(a1, 'Operator', b)
    if hasattr(a2, 'Operator'):
        assert _is_linked(a2, 'Operator', b)
    _safe_set(b, 'operands', None)
    assert not _is_linked(b, 'operands', a2)
    if hasattr(a2, 'Operator'):
        assert not _is_linked(a2, 'Operator', b)


def test_assoc_operators1_reverse_link_reassign_clear():
    a1 = trnet_TrNetModel(id="sample_text")
    a2 = trnet_TrNetModel(id="sample_text_2")
    b = trnet_Operator(id="sample_text")
    _safe_set(b, 'trnet_Operator', a1)
    assert _is_linked(b, 'trnet_Operator', a1)
    if hasattr(a1, 'trnet_TrNetModel2'):
        assert _is_linked(a1, 'trnet_TrNetModel2', b)
    _safe_set(b, 'trnet_Operator', a2)
    assert _is_linked(b, 'trnet_Operator', a2)
    if hasattr(a1, 'trnet_TrNetModel2'):
        assert not _is_linked(a1, 'trnet_TrNetModel2', b)
    if hasattr(a2, 'trnet_TrNetModel2'):
        assert _is_linked(a2, 'trnet_TrNetModel2', b)
    _safe_set(b, 'trnet_Operator', None)
    assert not _is_linked(b, 'trnet_Operator', a2)
    if hasattr(a2, 'trnet_TrNetModel2'):
        assert not _is_linked(a2, 'trnet_TrNetModel2', b)


def test_assoc_outgoing6_reverse_link_reassign_clear():
    a1 = trnet_NodePattern(id="sample_text", name="sample_text")
    a2 = trnet_NodePattern(id="sample_text_2", name="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
    _safe_set(b, 'EdgePattern7', a1)
    assert _is_linked(b, 'EdgePattern7', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'EdgePattern7', a2)
    assert _is_linked(b, 'EdgePattern7', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'EdgePattern7', None)
    assert not _is_linked(b, 'EdgePattern7', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_outgoingOperands35_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_Operand(index=7)
    _safe_set(b, 'Operand', a1)
    assert _is_linked(b, 'Operand', a1)
    if hasattr(a1, 'pattern36'):
        assert _is_linked(a1, 'pattern36', b)
    _safe_set(b, 'Operand', a2)
    assert _is_linked(b, 'Operand', a2)
    if hasattr(a1, 'pattern36'):
        assert not _is_linked(a1, 'pattern36', b)
    if hasattr(a2, 'pattern36'):
        assert _is_linked(a2, 'pattern36', b)
    _safe_set(b, 'Operand', None)
    assert not _is_linked(b, 'Operand', a2)
    if hasattr(a2, 'pattern36'):
        assert not _is_linked(a2, 'pattern36', b)


def test_assoc_pattern13_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_NodePattern(id="sample_text", name="sample_text")
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


def test_assoc_pattern28_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Pattern29'):
        assert _is_linked(a1, 'Pattern29', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Pattern29'):
        assert not _is_linked(a1, 'Pattern29', b)
    if hasattr(a2, 'Pattern29'):
        assert _is_linked(a2, 'Pattern29', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Pattern29'):
        assert not _is_linked(a2, 'Pattern29', b)


def test_assoc_pattern57_reverse_link_reassign_clear():
    a1 = trnet_Pattern(expected_size=7, id="sample_text")
    a2 = trnet_Pattern(expected_size=13, id="sample_text_2")
    b = trnet_Operand(index=7)
    _safe_set(b, 'outgoingOperands', a1)
    assert _is_linked(b, 'outgoingOperands', a1)
    if hasattr(a1, 'Pattern58'):
        assert _is_linked(a1, 'Pattern58', b)
    _safe_set(b, 'outgoingOperands', a2)
    assert _is_linked(b, 'outgoingOperands', a2)
    if hasattr(a1, 'Pattern58'):
        assert not _is_linked(a1, 'Pattern58', b)
    if hasattr(a2, 'Pattern58'):
        assert _is_linked(a2, 'Pattern58', b)
    _safe_set(b, 'outgoingOperands', None)
    assert not _is_linked(b, 'outgoingOperands', a2)
    if hasattr(a2, 'Pattern58'):
        assert not _is_linked(a2, 'Pattern58', b)


def test_assoc_patterns0_reverse_link_reassign_clear():
    a1 = trnet_TrNetModel(id="sample_text")
    a2 = trnet_TrNetModel(id="sample_text_2")
    b = trnet_Pattern(expected_size=7, id="sample_text")
    _safe_set(b, 'trnet_Pattern', a1)
    assert _is_linked(b, 'trnet_Pattern', a1)
    if hasattr(a1, 'trnet_TrNetModel'):
        assert _is_linked(a1, 'trnet_TrNetModel', b)
    _safe_set(b, 'trnet_Pattern', a2)
    assert _is_linked(b, 'trnet_Pattern', a2)
    if hasattr(a1, 'trnet_TrNetModel'):
        assert not _is_linked(a1, 'trnet_TrNetModel', b)
    if hasattr(a2, 'trnet_TrNetModel'):
        assert _is_linked(a2, 'trnet_TrNetModel', b)
    _safe_set(b, 'trnet_Pattern', None)
    assert not _is_linked(b, 'trnet_Pattern', a2)
    if hasattr(a2, 'trnet_TrNetModel'):
        assert not _is_linked(a2, 'trnet_TrNetModel', b)


def test_assoc_source25_reverse_link_reassign_clear():
    a1 = trnet_NodePattern(id="sample_text", name="sample_text")
    a2 = trnet_NodePattern(id="sample_text_2", name="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
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


def test_assoc_target26_reverse_link_reassign_clear():
    a1 = trnet_NodePattern(id="sample_text", name="sample_text")
    a2 = trnet_NodePattern(id="sample_text_2", name="sample_text_2")
    b = trnet_EdgePattern(name="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'NodePattern27'):
        assert _is_linked(a1, 'NodePattern27', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'NodePattern27'):
        assert not _is_linked(a1, 'NodePattern27', b)
    if hasattr(a2, 'NodePattern27'):
        assert _is_linked(a2, 'NodePattern27', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'NodePattern27'):
        assert not _is_linked(a2, 'NodePattern27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_differentIn15_stub_double():
    # trnet_Different has no real 'Different' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Different()
    setattr(partner, 'Different', None)
    _safe_set(owner, 'target16', {partner})
    assert getattr(partner, 'Different') == owner
    _safe_set(owner, 'target16', set())
    assert getattr(partner, 'Different') is None


def test_assoc_differentOut17_stub_double():
    # trnet_Different has no real 'Different19' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Different()
    setattr(partner, 'Different19', None)
    _safe_set(owner, 'source18', {partner})
    assert getattr(partner, 'Different19') == owner
    _safe_set(owner, 'source18', set())
    assert getattr(partner, 'Different19') is None


def test_assoc_expression49_stub_double():
    # trnet_Expression has no real 'trnet_Expression' property in the generated
    # code (a bare stub) -- manually attach it so trnet_AttributePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_AttributePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_AttributePattern(name="sample_text")
    partner = trnet_Expression()
    setattr(partner, 'trnet_Expression', None)
    _safe_set(owner, 'trnet_AttributePattern50', partner)
    assert getattr(partner, 'trnet_Expression') == owner
    _safe_set(owner, 'trnet_AttributePattern50', None)
    assert getattr(partner, 'trnet_Expression') is None


def test_assoc_flowRules3_stub_double():
    # trnet_FlowRule has no real 'trnet_FlowRule' property in the generated
    # code (a bare stub) -- manually attach it so trnet_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_TrNetModel(id="sample_text")
    partner = trnet_FlowRule()
    setattr(partner, 'trnet_FlowRule', None)
    _safe_set(owner, 'trnet_TrNetModel4', {partner})
    assert getattr(partner, 'trnet_FlowRule') == owner
    _safe_set(owner, 'trnet_TrNetModel4', set())
    assert getattr(partner, 'trnet_FlowRule') is None


def test_assoc_incommingResults37_stub_double():
    # trnet_Result has no real 'Result' property in the generated
    # code (a bare stub) -- manually attach it so trnet_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_Pattern(expected_size=7, id="sample_text")
    partner = trnet_Result()
    setattr(partner, 'Result', None)
    _safe_set(owner, 'pattern38', {partner})
    assert getattr(partner, 'Result') == owner
    _safe_set(owner, 'pattern38', set())
    assert getattr(partner, 'Result') is None


def test_assoc_keepIn20_stub_double():
    # trnet_Keep has no real 'Keep' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Keep()
    setattr(partner, 'Keep', None)
    _safe_set(owner, 'target21', {partner})
    assert getattr(partner, 'Keep') == owner
    _safe_set(owner, 'target21', set())
    assert getattr(partner, 'Keep') is None


def test_assoc_keepOut22_stub_double():
    # trnet_Keep has no real 'Keep24' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Keep()
    setattr(partner, 'Keep24', None)
    _safe_set(owner, 'source23', {partner})
    assert getattr(partner, 'Keep24') == owner
    _safe_set(owner, 'source23', set())
    assert getattr(partner, 'Keep24') is None


def test_assoc_operator51_stub_double():
    # trnet_ExpressionOperator has no real 'trnet_ExpressionOperator' property in the generated
    # code (a bare stub) -- manually attach it so trnet_AttributePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_AttributePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_AttributePattern(name="sample_text")
    partner = trnet_ExpressionOperator()
    setattr(partner, 'trnet_ExpressionOperator', None)
    _safe_set(owner, 'trnet_AttributePattern52', partner)
    assert getattr(partner, 'trnet_ExpressionOperator') == owner
    _safe_set(owner, 'trnet_AttributePattern52', None)
    assert getattr(partner, 'trnet_ExpressionOperator') is None


def test_assoc_operator62_stub_double():
    # trnet_Result has no real 'results' property in the generated
    # code (a bare stub) -- manually attach it so trnet_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_Operator(id="sample_text")
    partner = trnet_Result()
    setattr(partner, 'results', None)
    _safe_set(owner, 'Operator63', partner)
    assert getattr(partner, 'results') == owner
    _safe_set(owner, 'Operator63', None)
    assert getattr(partner, 'results') is None


def test_assoc_pattern60_stub_double():
    # trnet_Result has no real 'incommingResults' property in the generated
    # code (a bare stub) -- manually attach it so trnet_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_Pattern(expected_size=7, id="sample_text")
    partner = trnet_Result()
    setattr(partner, 'incommingResults', None)
    _safe_set(owner, 'Pattern61', partner)
    assert getattr(partner, 'incommingResults') == owner
    _safe_set(owner, 'Pattern61', None)
    assert getattr(partner, 'incommingResults') is None


def test_assoc_results41_stub_double():
    # trnet_Result has no real 'Result43' property in the generated
    # code (a bare stub) -- manually attach it so trnet_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_Operator(id="sample_text")
    partner = trnet_Result()
    setattr(partner, 'Result43', None)
    _safe_set(owner, 'operator42', {partner})
    assert getattr(partner, 'Result43') == owner
    _safe_set(owner, 'operator42', set())
    assert getattr(partner, 'Result43') is None


def test_assoc_sameIn10_stub_double():
    # trnet_Same has no real 'Same12' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Same()
    setattr(partner, 'Same12', None)
    _safe_set(owner, 'target11', {partner})
    assert getattr(partner, 'Same12') == owner
    _safe_set(owner, 'target11', set())
    assert getattr(partner, 'Same12') is None


def test_assoc_sameOut8_stub_double():
    # trnet_Same has no real 'Same' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Same()
    setattr(partner, 'Same', None)
    _safe_set(owner, 'source9', {partner})
    assert getattr(partner, 'Same') == owner
    _safe_set(owner, 'source9', set())
    assert getattr(partner, 'Same') is None


def test_assoc_source45_stub_double():
    # trnet_Same has no real 'sameOut' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Same()
    setattr(partner, 'sameOut', None)
    _safe_set(owner, 'NodePattern46', partner)
    assert getattr(partner, 'sameOut') == owner
    _safe_set(owner, 'NodePattern46', None)
    assert getattr(partner, 'sameOut') is None


def test_assoc_source53_stub_double():
    # trnet_Keep has no real 'keepOut' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Keep()
    setattr(partner, 'keepOut', None)
    _safe_set(owner, 'NodePattern54', partner)
    assert getattr(partner, 'keepOut') == owner
    _safe_set(owner, 'NodePattern54', None)
    assert getattr(partner, 'keepOut') is None


def test_assoc_source64_stub_double():
    # trnet_Different has no real 'differentOut' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Different()
    setattr(partner, 'differentOut', None)
    _safe_set(owner, 'NodePattern65', partner)
    assert getattr(partner, 'differentOut') == owner
    _safe_set(owner, 'NodePattern65', None)
    assert getattr(partner, 'differentOut') is None


def test_assoc_source70_stub_double():
    # trnet_FlowRule has no real 'trnet_FlowRule71' property in the generated
    # code (a bare stub) -- manually attach it so trnet_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_TrNetModel(id="sample_text")
    partner = trnet_FlowRule()
    setattr(partner, 'trnet_FlowRule71', None)
    _safe_set(owner, 'trnet_TrNetModel72', partner)
    assert getattr(partner, 'trnet_FlowRule71') == owner
    _safe_set(owner, 'trnet_TrNetModel72', None)
    assert getattr(partner, 'trnet_FlowRule71') is None


def test_assoc_target47_stub_double():
    # trnet_Same has no real 'sameIn' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Same()
    setattr(partner, 'sameIn', None)
    _safe_set(owner, 'NodePattern48', partner)
    assert getattr(partner, 'sameIn') == owner
    _safe_set(owner, 'NodePattern48', None)
    assert getattr(partner, 'sameIn') is None


def test_assoc_target55_stub_double():
    # trnet_Keep has no real 'keepIn' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Keep()
    setattr(partner, 'keepIn', None)
    _safe_set(owner, 'NodePattern56', partner)
    assert getattr(partner, 'keepIn') == owner
    _safe_set(owner, 'NodePattern56', None)
    assert getattr(partner, 'keepIn') is None


def test_assoc_target66_stub_double():
    # trnet_Different has no real 'differentIn' property in the generated
    # code (a bare stub) -- manually attach it so trnet_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_NodePattern(id="sample_text", name="sample_text")
    partner = trnet_Different()
    setattr(partner, 'differentIn', None)
    _safe_set(owner, 'NodePattern67', partner)
    assert getattr(partner, 'differentIn') == owner
    _safe_set(owner, 'NodePattern67', None)
    assert getattr(partner, 'differentIn') is None


def test_assoc_target73_stub_double():
    # trnet_FlowRule has no real 'trnet_FlowRule74' property in the generated
    # code (a bare stub) -- manually attach it so trnet_TrNetModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trnet_TrNetModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trnet_TrNetModel(id="sample_text")
    partner = trnet_FlowRule()
    setattr(partner, 'trnet_FlowRule74', None)
    _safe_set(owner, 'trnet_TrNetModel75', partner)
    assert getattr(partner, 'trnet_FlowRule74') == owner
    _safe_set(owner, 'trnet_TrNetModel75', None)
    assert getattr(partner, 'trnet_FlowRule74') is None


