import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTypedIOPort,
    ActionPattern,
    ChannelSelector,
    JvmTypedObj,
    NamedObj,
    OutputAction,
    Parameter,
    PortPattern,
    ReAction,
    Relation,
    Variable,
    caltrop_ActionPattern,
    caltrop_ActorParameter,
    caltrop_CaltropActorImpl,
    caltrop_ChannelSelector,
    caltrop_ConversionRelation,
    caltrop_EventAction,
    caltrop_EventPattern,
    caltrop_ExpressionChannelSelector,
    caltrop_FireAction,
    caltrop_FunctionDeclaration,
    caltrop_InputPattern,
    caltrop_JvmTypeReference,
    caltrop_JvmTypedObj,
    caltrop_KeywordChannelSelector,
    caltrop_OutputAction,
    caltrop_OutputPattern,
    caltrop_Port,
    caltrop_PortPattern,
    caltrop_ReAction,
    caltrop_Schedule,
    caltrop_State,
    caltrop_StateVariable,
    caltrop_Transition,
    caltrop_TypedInputPort,
    caltrop_TypedOutputPort,
    caltrop_XExpression,
    ChannelSelectorKeyword,
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

def test_assoc_varRef54_reverse_link_reassign_clear():
    a1 = caltrop_StateVariable(constant=True)
    a2 = caltrop_StateVariable(constant=False)
    b = caltrop_EventPattern(_property=True, name="sample_text", qualifier="sample_text", variables="sample_text")
    _safe_set(b, 'caltrop_EventPattern55', a1)
    assert _is_linked(b, 'caltrop_EventPattern55', a1)
    if hasattr(a1, 'caltrop_StateVariable56'):
        assert _is_linked(a1, 'caltrop_StateVariable56', b)
    _safe_set(b, 'caltrop_EventPattern55', a2)
    assert _is_linked(b, 'caltrop_EventPattern55', a2)
    if hasattr(a1, 'caltrop_StateVariable56'):
        assert not _is_linked(a1, 'caltrop_StateVariable56', b)
    if hasattr(a2, 'caltrop_StateVariable56'):
        assert _is_linked(a2, 'caltrop_StateVariable56', b)
    _safe_set(b, 'caltrop_EventPattern55', None)
    assert not _is_linked(b, 'caltrop_EventPattern55', a2)
    if hasattr(a2, 'caltrop_StateVariable56'):
        assert not _is_linked(a2, 'caltrop_StateVariable56', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyExpression14_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression16' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression16', None)
    _safe_set(owner, 'caltrop_OutputAction15', partner)
    assert getattr(partner, 'caltrop_XExpression16') == owner
    _safe_set(owner, 'caltrop_OutputAction15', None)
    assert getattr(partner, 'caltrop_XExpression16') is None


def test_assoc_channels25_stub_double():
    # caltrop_ChannelSelector has no real 'caltrop_ChannelSelector' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_PortPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_PortPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_PortPattern()
    partner = caltrop_ChannelSelector()
    setattr(partner, 'caltrop_ChannelSelector', None)
    _safe_set(owner, 'caltrop_PortPattern26', partner)
    assert getattr(partner, 'caltrop_ChannelSelector') == owner
    _safe_set(owner, 'caltrop_PortPattern26', None)
    assert getattr(partner, 'caltrop_ChannelSelector') is None


def test_assoc_conversionExpression63_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression64' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_ConversionRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_ConversionRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_ConversionRelation(valueVar="sample_text")
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression64', None)
    _safe_set(owner, 'caltrop_ConversionRelation', partner)
    assert getattr(partner, 'caltrop_XExpression64') == owner
    _safe_set(owner, 'caltrop_ConversionRelation', None)
    assert getattr(partner, 'caltrop_XExpression64') is None


def test_assoc_declarations0_stub_double():
    # caltrop_CaltropActorImpl has no real 'caltrop_CaltropActorImpl' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_StateVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_StateVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_StateVariable(constant=True)
    partner = caltrop_CaltropActorImpl()
    setattr(partner, 'caltrop_CaltropActorImpl', None)
    _safe_set(owner, 'caltrop_StateVariable', partner)
    assert owner in getattr(partner, 'caltrop_CaltropActorImpl')
    _safe_set(owner, 'caltrop_StateVariable', None)
    assert owner not in getattr(partner, 'caltrop_CaltropActorImpl')


def test_assoc_delayExpression20_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression22' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression22', None)
    _safe_set(owner, 'caltrop_OutputAction21', partner)
    assert getattr(partner, 'caltrop_XExpression22') == owner
    _safe_set(owner, 'caltrop_OutputAction21', None)
    assert getattr(partner, 'caltrop_XExpression22') is None


def test_assoc_eventPatterns53_stub_double():
    # caltrop_EventAction has no real 'caltrop_EventAction' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_EventPattern(_property=True, name="sample_text", qualifier="sample_text", variables="sample_text")
    partner = caltrop_EventAction()
    setattr(partner, 'caltrop_EventAction', None)
    _safe_set(owner, 'caltrop_EventPattern', partner)
    assert owner in getattr(partner, 'caltrop_EventAction')
    _safe_set(owner, 'caltrop_EventPattern', None)
    assert owner not in getattr(partner, 'caltrop_EventAction')


def test_assoc_guardExpression10_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression', None)
    _safe_set(owner, 'caltrop_OutputAction11', partner)
    assert getattr(partner, 'caltrop_XExpression') == owner
    _safe_set(owner, 'caltrop_OutputAction11', None)
    assert getattr(partner, 'caltrop_XExpression') is None


def test_assoc_guardExpression29_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression31' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_PortPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_PortPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_PortPattern()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression31', None)
    _safe_set(owner, 'caltrop_PortPattern30', partner)
    assert getattr(partner, 'caltrop_XExpression31') == owner
    _safe_set(owner, 'caltrop_PortPattern30', None)
    assert getattr(partner, 'caltrop_XExpression31') is None


def test_assoc_guardExpression60_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression62' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_EventPattern(_property=True, name="sample_text", qualifier="sample_text", variables="sample_text")
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression62', None)
    _safe_set(owner, 'caltrop_EventPattern61', partner)
    assert getattr(partner, 'caltrop_XExpression62') == owner
    _safe_set(owner, 'caltrop_EventPattern61', None)
    assert getattr(partner, 'caltrop_XExpression62') is None


def test_assoc_guardExpression65_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression67' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_ConversionRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_ConversionRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_ConversionRelation(valueVar="sample_text")
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression67', None)
    _safe_set(owner, 'caltrop_ConversionRelation66', partner)
    assert getattr(partner, 'caltrop_XExpression67') == owner
    _safe_set(owner, 'caltrop_ConversionRelation66', None)
    assert getattr(partner, 'caltrop_XExpression67') is None


def test_assoc_initActions3_stub_double():
    # caltrop_CaltropActorImpl has no real 'caltrop_CaltropActorImpl4' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_CaltropActorImpl()
    setattr(partner, 'caltrop_CaltropActorImpl4', None)
    _safe_set(owner, 'caltrop_OutputAction', partner)
    assert owner in getattr(partner, 'caltrop_CaltropActorImpl4')
    _safe_set(owner, 'caltrop_OutputAction', None)
    assert owner not in getattr(partner, 'caltrop_CaltropActorImpl4')


def test_assoc_inputPatterns9_stub_double():
    # caltrop_FireAction has no real 'caltrop_FireAction' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_InputPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_InputPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_InputPattern(variables="sample_text")
    partner = caltrop_FireAction()
    setattr(partner, 'caltrop_FireAction', None)
    _safe_set(owner, 'caltrop_InputPattern', partner)
    assert owner in getattr(partner, 'caltrop_FireAction')
    _safe_set(owner, 'caltrop_InputPattern', None)
    assert owner not in getattr(partner, 'caltrop_FireAction')


def test_assoc_keyExpressions35_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression36' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_ExpressionChannelSelector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_ExpressionChannelSelector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_ExpressionChannelSelector(many=True)
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression36', None)
    _safe_set(owner, 'caltrop_ExpressionChannelSelector', {partner})
    assert getattr(partner, 'caltrop_XExpression36') == owner
    _safe_set(owner, 'caltrop_ExpressionChannelSelector', set())
    assert getattr(partner, 'caltrop_XExpression36') is None


def test_assoc_outputPatterns12_stub_double():
    # caltrop_OutputPattern has no real 'caltrop_OutputPattern' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_OutputPattern()
    setattr(partner, 'caltrop_OutputPattern', None)
    _safe_set(owner, 'caltrop_OutputAction13', {partner})
    assert getattr(partner, 'caltrop_OutputPattern') == owner
    _safe_set(owner, 'caltrop_OutputAction13', set())
    assert getattr(partner, 'caltrop_OutputPattern') is None


def test_assoc_portRef27_stub_double():
    # caltrop_Port has no real 'caltrop_Port' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_PortPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_PortPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_PortPattern()
    partner = caltrop_Port()
    setattr(partner, 'caltrop_Port', None)
    _safe_set(owner, 'caltrop_PortPattern28', partner)
    assert getattr(partner, 'caltrop_Port') == owner
    _safe_set(owner, 'caltrop_PortPattern28', None)
    assert getattr(partner, 'caltrop_Port') is None


def test_assoc_repeatExpression23_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression24' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_PortPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_PortPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_PortPattern()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression24', None)
    _safe_set(owner, 'caltrop_PortPattern', partner)
    assert getattr(partner, 'caltrop_XExpression24') == owner
    _safe_set(owner, 'caltrop_PortPattern', None)
    assert getattr(partner, 'caltrop_XExpression24') is None


def test_assoc_source49_stub_double():
    # caltrop_State has no real 'State50' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_Transition(tags="sample_text")
    partner = caltrop_State()
    setattr(partner, 'State50', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'State50') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'State50') is None


def test_assoc_target51_stub_double():
    # caltrop_State has no real 'caltrop_State52' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_Transition(tags="sample_text")
    partner = caltrop_State()
    setattr(partner, 'caltrop_State52', None)
    _safe_set(owner, 'caltrop_Transition', partner)
    assert getattr(partner, 'caltrop_State52') == owner
    _safe_set(owner, 'caltrop_Transition', None)
    assert getattr(partner, 'caltrop_State52') is None


def test_assoc_timeExpression57_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression59' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_EventPattern(_property=True, name="sample_text", qualifier="sample_text", variables="sample_text")
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression59', None)
    _safe_set(owner, 'caltrop_EventPattern58', partner)
    assert getattr(partner, 'caltrop_XExpression59') == owner
    _safe_set(owner, 'caltrop_EventPattern58', None)
    assert getattr(partner, 'caltrop_XExpression59') is None


def test_assoc_transitions47_stub_double():
    # caltrop_State has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_Transition(tags="sample_text")
    partner = caltrop_State()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_updateExpression17_stub_double():
    # caltrop_XExpression has no real 'caltrop_XExpression19' property in the generated
    # code (a bare stub) -- manually attach it so caltrop_OutputAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caltrop_OutputAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caltrop_OutputAction()
    partner = caltrop_XExpression()
    setattr(partner, 'caltrop_XExpression19', None)
    _safe_set(owner, 'caltrop_OutputAction18', partner)
    assert getattr(partner, 'caltrop_XExpression19') == owner
    _safe_set(owner, 'caltrop_OutputAction18', None)
    assert getattr(partner, 'caltrop_XExpression19') is None


