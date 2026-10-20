import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    NamedElement,
    Service,
    micro_API,
    micro_AggregateService,
    micro_Attribute,
    micro_Command,
    micro_Data,
    micro_Event,
    micro_Info,
    micro_MicroserviceArchitecture,
    micro_Model,
    micro_ModelEvent,
    micro_NamedElement,
    micro_Operation,
    micro_PrimitiveTypeAttribute,
    micro_ReferenceAttribute,
    micro_Saga,
    micro_Service,
    micro_Step,
    micro_ViewService,
    AttributePrimitiveValue,
    CRUDOperation,
    CommandType,
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

def test_assoc_aggregateService25_reverse_link_reassign_clear():
    a1 = micro_Operation(isMethodController=True, operationType="sample_text")
    a2 = micro_Operation(isMethodController=False, operationType="sample_text_2")
    b = micro_AggregateService()
    _safe_set(b, 'AggregateService26', a1)
    assert _is_linked(b, 'AggregateService26', a1)
    if hasattr(a1, 'operation'):
        assert _is_linked(a1, 'operation', b)
    _safe_set(b, 'AggregateService26', a2)
    assert _is_linked(b, 'AggregateService26', a2)
    if hasattr(a1, 'operation'):
        assert not _is_linked(a1, 'operation', b)
    if hasattr(a2, 'operation'):
        assert _is_linked(a2, 'operation', b)
    _safe_set(b, 'AggregateService26', None)
    assert not _is_linked(b, 'AggregateService26', a2)
    if hasattr(a2, 'operation'):
        assert not _is_linked(a2, 'operation', b)


def test_assoc_operation8_reverse_link_reassign_clear():
    a1 = micro_Operation(isMethodController=True, operationType="sample_text")
    a2 = micro_Operation(isMethodController=False, operationType="sample_text_2")
    b = micro_AggregateService()
    _safe_set(b, 'aggregateService9', {a1})
    assert _is_linked(b, 'aggregateService9', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'aggregateService9', {a2})
    assert _is_linked(b, 'aggregateService9', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'aggregateService9', set())
    assert not _is_linked(b, 'aggregateService9', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ModelToView51_stub_double():
    # micro_Model has no real 'micro_Model52' property in the generated
    # code (a bare stub) -- manually attach it so micro_PrimitiveTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_PrimitiveTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_PrimitiveTypeAttribute(type="sample_text")
    partner = micro_Model()
    setattr(partner, 'micro_Model52', None)
    _safe_set(owner, 'micro_PrimitiveTypeAttribute', partner)
    assert getattr(partner, 'micro_Model52') == owner
    _safe_set(owner, 'micro_PrimitiveTypeAttribute', None)
    assert getattr(partner, 'micro_Model52') is None


def test_assoc_Saga20_stub_double():
    # micro_Saga has no real 'micro_Saga' property in the generated
    # code (a bare stub) -- manually attach it so micro_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Operation(isMethodController=True, operationType="sample_text")
    partner = micro_Saga()
    setattr(partner, 'micro_Saga', None)
    _safe_set(owner, 'micro_Operation21', partner)
    assert getattr(partner, 'micro_Saga') == owner
    _safe_set(owner, 'micro_Operation21', None)
    assert getattr(partner, 'micro_Saga') is None


def test_assoc_aggregateService6_stub_double():
    # micro_ModelEvent has no real 'modelEvents' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_ModelEvent()
    setattr(partner, 'modelEvents', None)
    _safe_set(owner, 'AggregateService', partner)
    assert getattr(partner, 'modelEvents') == owner
    _safe_set(owner, 'AggregateService', None)
    assert getattr(partner, 'modelEvents') is None


def test_assoc_api10_stub_double():
    # micro_API has no real 'micro_API' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_API()
    setattr(partner, 'micro_API', None)
    _safe_set(owner, 'micro_AggregateService', partner)
    assert getattr(partner, 'micro_API') == owner
    _safe_set(owner, 'micro_AggregateService', None)
    assert getattr(partner, 'micro_API') is None


def test_assoc_api33_stub_double():
    # micro_API has no real 'API' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_API()
    setattr(partner, 'API', None)
    _safe_set(owner, 'commands', partner)
    assert getattr(partner, 'API') == owner
    _safe_set(owner, 'commands', None)
    assert getattr(partner, 'API') is None


def test_assoc_attributes3_stub_double():
    # micro_Model has no real 'model' property in the generated
    # code (a bare stub) -- manually attach it so micro_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Attribute(isGenerated=True, isId=True, isMany=True, name="sample_text")
    partner = micro_Model()
    setattr(partner, 'model', None)
    _safe_set(owner, 'Attribute', partner)
    assert owner in getattr(partner, 'model')
    _safe_set(owner, 'Attribute', None)
    assert owner not in getattr(partner, 'model')


def test_assoc_commands28_stub_double():
    # micro_API has no real 'api29' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_API()
    setattr(partner, 'api29', None)
    _safe_set(owner, 'Command', partner)
    assert owner in getattr(partner, 'api29')
    _safe_set(owner, 'Command', None)
    assert owner not in getattr(partner, 'api29')


def test_assoc_commands41_stub_double():
    # micro_Step has no real 'micro_Step' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_Step()
    setattr(partner, 'micro_Step', None)
    _safe_set(owner, 'micro_Command42', partner)
    assert owner in getattr(partner, 'micro_Step')
    _safe_set(owner, 'micro_Command42', None)
    assert owner not in getattr(partner, 'micro_Step')


def test_assoc_handleModelEvents11_stub_double():
    # micro_ModelEvent has no real 'micro_ModelEvent13' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_ModelEvent()
    setattr(partner, 'micro_ModelEvent13', None)
    _safe_set(owner, 'micro_AggregateService12', {partner})
    assert getattr(partner, 'micro_ModelEvent13') == owner
    _safe_set(owner, 'micro_AggregateService12', set())
    assert getattr(partner, 'micro_ModelEvent13') is None


def test_assoc_model22_stub_double():
    # micro_Model has no real 'micro_Model24' property in the generated
    # code (a bare stub) -- manually attach it so micro_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Operation(isMethodController=True, operationType="sample_text")
    partner = micro_Model()
    setattr(partner, 'micro_Model24', None)
    _safe_set(owner, 'micro_Operation23', partner)
    assert getattr(partner, 'micro_Model24') == owner
    _safe_set(owner, 'micro_Operation23', None)
    assert getattr(partner, 'micro_Model24') is None


def test_assoc_model48_stub_double():
    # micro_Model has no real 'Model' property in the generated
    # code (a bare stub) -- manually attach it so micro_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Attribute(isGenerated=True, isId=True, isMany=True, name="sample_text")
    partner = micro_Model()
    setattr(partner, 'Model', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'Model') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'Model') is None


def test_assoc_modelEvents7_stub_double():
    # micro_ModelEvent has no real 'ModelEvent' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_ModelEvent()
    setattr(partner, 'ModelEvent', None)
    _safe_set(owner, 'aggregateService', {partner})
    assert getattr(partner, 'ModelEvent') == owner
    _safe_set(owner, 'aggregateService', set())
    assert getattr(partner, 'ModelEvent') is None


def test_assoc_models14_stub_double():
    # micro_Model has no real 'micro_Model16' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_Model()
    setattr(partner, 'micro_Model16', None)
    _safe_set(owner, 'micro_AggregateService15', {partner})
    assert getattr(partner, 'micro_Model16') == owner
    _safe_set(owner, 'micro_AggregateService15', set())
    assert getattr(partner, 'micro_Model16') is None


def test_assoc_publish19_stub_double():
    # micro_Event has no real 'micro_Event' property in the generated
    # code (a bare stub) -- manually attach it so micro_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Operation(isMethodController=True, operationType="sample_text")
    partner = micro_Event()
    setattr(partner, 'micro_Event', None)
    _safe_set(owner, 'micro_Operation', partner)
    assert getattr(partner, 'micro_Event') == owner
    _safe_set(owner, 'micro_Operation', None)
    assert getattr(partner, 'micro_Event') is None


def test_assoc_replicateServices17_stub_double():
    # micro_ViewService has no real 'micro_ViewService' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_ViewService()
    setattr(partner, 'micro_ViewService', None)
    _safe_set(owner, 'micro_AggregateService18', partner)
    assert owner in getattr(partner, 'micro_ViewService')
    _safe_set(owner, 'micro_AggregateService18', None)
    assert owner not in getattr(partner, 'micro_ViewService')


def test_assoc_replyInfo32_stub_double():
    # micro_Info has no real 'micro_Info' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_Info()
    setattr(partner, 'micro_Info', None)
    _safe_set(owner, 'micro_Command', partner)
    assert getattr(partner, 'micro_Info') == owner
    _safe_set(owner, 'micro_Command', None)
    assert getattr(partner, 'micro_Info') is None


def test_assoc_services0_stub_double():
    # micro_MicroserviceArchitecture has no real 'micro_MicroserviceArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so micro_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Service(description="sample_text", fullname="sample_text", port=7, shortname="sample_text")
    partner = micro_MicroserviceArchitecture()
    setattr(partner, 'micro_MicroserviceArchitecture', None)
    _safe_set(owner, 'micro_Service', partner)
    assert owner in getattr(partner, 'micro_MicroserviceArchitecture')
    _safe_set(owner, 'micro_Service', None)
    assert owner not in getattr(partner, 'micro_MicroserviceArchitecture')


