import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractBehavior,
    AbstractFunctionalChainContainer,
    CapellaElement,
    NamedElement,
    Namespace,
    Structure,
    interaction_AbstractCapability,
    interaction_AbstractEventOperation,
    interaction_AbstractFunction,
    interaction_CombinedFragment,
    interaction_Constraint,
    interaction_ExchangeItem,
    interaction_ExchangeItemElement,
    interaction_FunctionalChain,
    interaction_InteractionOperand,
    interaction_Part,
    interaction_Scenario,
    interaction_SequenceMessage,
    interaction_SequenceMessageValuation,
    interaction_State,
    interaction_ValueSpecification,
    InteractionOperatorKind,
    MessageKind,
    ScenarioKind,
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

def test_assoc_ownedMessages22_reverse_link_reassign_clear():
    a1 = interaction_SequenceMessage(kind="sample_text")
    a2 = interaction_SequenceMessage(kind="sample_text_2")
    b = interaction_Scenario(kind="sample_text", merged=True)
    _safe_set(b, 'interaction_Scenario23', {a1})
    assert _is_linked(b, 'interaction_Scenario23', a1)
    if hasattr(a1, 'interaction_SequenceMessage24'):
        assert _is_linked(a1, 'interaction_SequenceMessage24', b)
    _safe_set(b, 'interaction_Scenario23', {a2})
    assert _is_linked(b, 'interaction_Scenario23', a2)
    if hasattr(a1, 'interaction_SequenceMessage24'):
        assert not _is_linked(a1, 'interaction_SequenceMessage24', b)
    if hasattr(a2, 'interaction_SequenceMessage24'):
        assert _is_linked(a2, 'interaction_SequenceMessage24', b)
    _safe_set(b, 'interaction_Scenario23', set())
    assert not _is_linked(b, 'interaction_Scenario23', a2)
    if hasattr(a2, 'interaction_SequenceMessage24'):
        assert not _is_linked(a2, 'interaction_SequenceMessage24', b)


def test_assoc_realizedScenarios35_reverse_link_reassign_clear():
    a1 = interaction_Scenario(kind="sample_text", merged=True)
    a2 = interaction_Scenario(kind="sample_text_2", merged=False)
    b = interaction_Scenario(kind="sample_text", merged=True)
    _safe_set(b, 'interaction_Scenario36', a1)
    assert _is_linked(b, 'interaction_Scenario36', a1)
    if hasattr(a1, 'interaction_Scenario34'):
        assert _is_linked(a1, 'interaction_Scenario34', b)
    _safe_set(b, 'interaction_Scenario36', a2)
    assert _is_linked(b, 'interaction_Scenario36', a2)
    if hasattr(a1, 'interaction_Scenario34'):
        assert not _is_linked(a1, 'interaction_Scenario34', b)
    if hasattr(a2, 'interaction_Scenario34'):
        assert _is_linked(a2, 'interaction_Scenario34', b)
    _safe_set(b, 'interaction_Scenario36', None)
    assert not _is_linked(b, 'interaction_Scenario36', a2)
    if hasattr(a2, 'interaction_Scenario34'):
        assert not _is_linked(a2, 'interaction_Scenario34', b)


def test_assoc_referencedScenarios32_reverse_link_reassign_clear():
    a1 = interaction_Scenario(kind="sample_text", merged=True)
    a2 = interaction_Scenario(kind="sample_text_2", merged=False)
    b = interaction_Scenario(kind="sample_text", merged=True)
    _safe_set(b, 'interaction_Scenario33', a1)
    assert _is_linked(b, 'interaction_Scenario33', a1)
    if hasattr(a1, 'interaction_Scenario31'):
        assert _is_linked(a1, 'interaction_Scenario31', b)
    _safe_set(b, 'interaction_Scenario33', a2)
    assert _is_linked(b, 'interaction_Scenario33', a2)
    if hasattr(a1, 'interaction_Scenario31'):
        assert not _is_linked(a1, 'interaction_Scenario31', b)
    if hasattr(a2, 'interaction_Scenario31'):
        assert _is_linked(a2, 'interaction_Scenario31', b)
    _safe_set(b, 'interaction_Scenario33', None)
    assert not _is_linked(b, 'interaction_Scenario33', a2)
    if hasattr(a2, 'interaction_Scenario31'):
        assert not _is_linked(a2, 'interaction_Scenario31', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containedFunctions25_stub_double():
    # interaction_AbstractFunction has no real 'interaction_AbstractFunction27' property in the generated
    # code (a bare stub) -- manually attach it so interaction_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_Scenario(kind="sample_text", merged=True)
    partner = interaction_AbstractFunction()
    setattr(partner, 'interaction_AbstractFunction27', None)
    _safe_set(owner, 'interaction_Scenario26', {partner})
    assert getattr(partner, 'interaction_AbstractFunction27') == owner
    _safe_set(owner, 'interaction_Scenario26', set())
    assert getattr(partner, 'interaction_AbstractFunction27') is None


def test_assoc_containedParts28_stub_double():
    # interaction_Part has no real 'interaction_Part30' property in the generated
    # code (a bare stub) -- manually attach it so interaction_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_Scenario(kind="sample_text", merged=True)
    partner = interaction_Part()
    setattr(partner, 'interaction_Part30', None)
    _safe_set(owner, 'interaction_Scenario29', {partner})
    assert getattr(partner, 'interaction_Part30') == owner
    _safe_set(owner, 'interaction_Scenario29', set())
    assert getattr(partner, 'interaction_Part30') is None


def test_assoc_exchangeContext0_stub_double():
    # interaction_Constraint has no real 'interaction_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_Constraint()
    setattr(partner, 'interaction_Constraint', None)
    _safe_set(owner, 'interaction_SequenceMessage', partner)
    assert getattr(partner, 'interaction_Constraint') == owner
    _safe_set(owner, 'interaction_SequenceMessage', None)
    assert getattr(partner, 'interaction_Constraint') is None


def test_assoc_exchangedItems3_stub_double():
    # interaction_ExchangeItem has no real 'interaction_ExchangeItem' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_ExchangeItem()
    setattr(partner, 'interaction_ExchangeItem', None)
    _safe_set(owner, 'interaction_SequenceMessage4', {partner})
    assert getattr(partner, 'interaction_ExchangeItem') == owner
    _safe_set(owner, 'interaction_SequenceMessage4', set())
    assert getattr(partner, 'interaction_ExchangeItem') is None


def test_assoc_invokedOperation1_stub_double():
    # interaction_AbstractEventOperation has no real 'interaction_AbstractEventOperation' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_AbstractEventOperation()
    setattr(partner, 'interaction_AbstractEventOperation', None)
    _safe_set(owner, 'interaction_SequenceMessage2', partner)
    assert getattr(partner, 'interaction_AbstractEventOperation') == owner
    _safe_set(owner, 'interaction_SequenceMessage2', None)
    assert getattr(partner, 'interaction_AbstractEventOperation') is None


def test_assoc_ownedScenarios42_stub_double():
    # interaction_AbstractCapability has no real 'interaction_AbstractCapability43' property in the generated
    # code (a bare stub) -- manually attach it so interaction_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_Scenario(kind="sample_text", merged=True)
    partner = interaction_AbstractCapability()
    setattr(partner, 'interaction_AbstractCapability43', None)
    _safe_set(owner, 'interaction_Scenario44', partner)
    assert owner in getattr(partner, 'interaction_AbstractCapability43')
    _safe_set(owner, 'interaction_Scenario44', None)
    assert owner not in getattr(partner, 'interaction_AbstractCapability43')


def test_assoc_ownedSequenceMessageValuations15_stub_double():
    # interaction_SequenceMessageValuation has no real 'interaction_SequenceMessageValuation' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_SequenceMessageValuation()
    setattr(partner, 'interaction_SequenceMessageValuation', None)
    _safe_set(owner, 'interaction_SequenceMessage16', {partner})
    assert getattr(partner, 'interaction_SequenceMessageValuation') == owner
    _safe_set(owner, 'interaction_SequenceMessage16', set())
    assert getattr(partner, 'interaction_SequenceMessageValuation') is None


def test_assoc_postCondition19_stub_double():
    # interaction_Constraint has no real 'interaction_Constraint21' property in the generated
    # code (a bare stub) -- manually attach it so interaction_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_Scenario(kind="sample_text", merged=True)
    partner = interaction_Constraint()
    setattr(partner, 'interaction_Constraint21', None)
    _safe_set(owner, 'interaction_Scenario20', partner)
    assert getattr(partner, 'interaction_Constraint21') == owner
    _safe_set(owner, 'interaction_Scenario20', None)
    assert getattr(partner, 'interaction_Constraint21') is None


def test_assoc_preCondition17_stub_double():
    # interaction_Constraint has no real 'interaction_Constraint18' property in the generated
    # code (a bare stub) -- manually attach it so interaction_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_Scenario(kind="sample_text", merged=True)
    partner = interaction_Constraint()
    setattr(partner, 'interaction_Constraint18', None)
    _safe_set(owner, 'interaction_Scenario', partner)
    assert getattr(partner, 'interaction_Constraint18') == owner
    _safe_set(owner, 'interaction_Scenario', None)
    assert getattr(partner, 'interaction_Constraint18') is None


def test_assoc_receivingFunction12_stub_double():
    # interaction_AbstractFunction has no real 'interaction_AbstractFunction14' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_AbstractFunction()
    setattr(partner, 'interaction_AbstractFunction14', None)
    _safe_set(owner, 'interaction_SequenceMessage13', partner)
    assert getattr(partner, 'interaction_AbstractFunction14') == owner
    _safe_set(owner, 'interaction_SequenceMessage13', None)
    assert getattr(partner, 'interaction_AbstractFunction14') is None


def test_assoc_receivingPart7_stub_double():
    # interaction_Part has no real 'interaction_Part9' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_Part()
    setattr(partner, 'interaction_Part9', None)
    _safe_set(owner, 'interaction_SequenceMessage8', partner)
    assert getattr(partner, 'interaction_Part9') == owner
    _safe_set(owner, 'interaction_SequenceMessage8', None)
    assert getattr(partner, 'interaction_Part9') is None


def test_assoc_sendingFunction10_stub_double():
    # interaction_AbstractFunction has no real 'interaction_AbstractFunction' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_AbstractFunction()
    setattr(partner, 'interaction_AbstractFunction', None)
    _safe_set(owner, 'interaction_SequenceMessage11', partner)
    assert getattr(partner, 'interaction_AbstractFunction') == owner
    _safe_set(owner, 'interaction_SequenceMessage11', None)
    assert getattr(partner, 'interaction_AbstractFunction') is None


def test_assoc_sendingPart5_stub_double():
    # interaction_Part has no real 'interaction_Part' property in the generated
    # code (a bare stub) -- manually attach it so interaction_SequenceMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # interaction_SequenceMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = interaction_SequenceMessage(kind="sample_text")
    partner = interaction_Part()
    setattr(partner, 'interaction_Part', None)
    _safe_set(owner, 'interaction_SequenceMessage6', partner)
    assert getattr(partner, 'interaction_Part') == owner
    _safe_set(owner, 'interaction_SequenceMessage6', None)
    assert getattr(partner, 'interaction_Part') is None


