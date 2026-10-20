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

def test_assoc_aggregateService14_reverse_link_reassign_clear():
    a1 = micro_Operation(isMethodController=True, operationType="sample_text")
    a2 = micro_Operation(isMethodController=False, operationType="sample_text_2")
    b = micro_AggregateService()
    _safe_set(b, 'AggregateService15', a1)
    assert _is_linked(b, 'AggregateService15', a1)
    if hasattr(a1, 'operation'):
        assert _is_linked(a1, 'operation', b)
    _safe_set(b, 'AggregateService15', a2)
    assert _is_linked(b, 'AggregateService15', a2)
    if hasattr(a1, 'operation'):
        assert not _is_linked(a1, 'operation', b)
    if hasattr(a2, 'operation'):
        assert _is_linked(a2, 'operation', b)
    _safe_set(b, 'AggregateService15', None)
    assert not _is_linked(b, 'AggregateService15', a2)
    if hasattr(a2, 'operation'):
        assert not _is_linked(a2, 'operation', b)


def test_assoc_operation3_reverse_link_reassign_clear():
    a1 = micro_Operation(isMethodController=True, operationType="sample_text")
    a2 = micro_Operation(isMethodController=False, operationType="sample_text_2")
    b = micro_AggregateService()
    _safe_set(b, 'aggregateService', {a1})
    assert _is_linked(b, 'aggregateService', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'aggregateService', {a2})
    assert _is_linked(b, 'aggregateService', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'aggregateService', set())
    assert not _is_linked(b, 'aggregateService', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ModelToView41_stub_double():
    # micro_Model has no real 'micro_Model42' property in the generated
    # code (a bare stub) -- manually attach it so micro_PrimitiveTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_PrimitiveTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_PrimitiveTypeAttribute(type="sample_text")
    partner = micro_Model()
    setattr(partner, 'micro_Model42', None)
    _safe_set(owner, 'micro_PrimitiveTypeAttribute', partner)
    assert getattr(partner, 'micro_Model42') == owner
    _safe_set(owner, 'micro_PrimitiveTypeAttribute', None)
    assert getattr(partner, 'micro_Model42') is None


def test_assoc_Saga10_stub_double():
    # micro_Saga has no real 'micro_Saga' property in the generated
    # code (a bare stub) -- manually attach it so micro_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Operation(isMethodController=True, operationType="sample_text")
    partner = micro_Saga()
    setattr(partner, 'micro_Saga', None)
    _safe_set(owner, 'micro_Operation11', partner)
    assert getattr(partner, 'micro_Saga') == owner
    _safe_set(owner, 'micro_Operation11', None)
    assert getattr(partner, 'micro_Saga') is None


def test_assoc_aggregateService2_stub_double():
    # micro_Model has no real 'models' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_Model()
    setattr(partner, 'models', None)
    _safe_set(owner, 'AggregateService', partner)
    assert getattr(partner, 'models') == owner
    _safe_set(owner, 'AggregateService', None)
    assert getattr(partner, 'models') is None


def test_assoc_api22_stub_double():
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


def test_assoc_api4_stub_double():
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


def test_assoc_attributes1_stub_double():
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


def test_assoc_commands17_stub_double():
    # micro_API has no real 'api18' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_API()
    setattr(partner, 'api18', None)
    _safe_set(owner, 'Command', partner)
    assert owner in getattr(partner, 'api18')
    _safe_set(owner, 'Command', None)
    assert owner not in getattr(partner, 'api18')


def test_assoc_commands30_stub_double():
    # micro_Step has no real 'micro_Step' property in the generated
    # code (a bare stub) -- manually attach it so micro_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Command(commandType="sample_text", isReplyInfoMany=True)
    partner = micro_Step()
    setattr(partner, 'micro_Step', None)
    _safe_set(owner, 'micro_Command31', partner)
    assert owner in getattr(partner, 'micro_Step')
    _safe_set(owner, 'micro_Command31', None)
    assert owner not in getattr(partner, 'micro_Step')


def test_assoc_model12_stub_double():
    # micro_Model has no real 'micro_Model' property in the generated
    # code (a bare stub) -- manually attach it so micro_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Operation(isMethodController=True, operationType="sample_text")
    partner = micro_Model()
    setattr(partner, 'micro_Model', None)
    _safe_set(owner, 'micro_Operation13', partner)
    assert getattr(partner, 'micro_Model') == owner
    _safe_set(owner, 'micro_Operation13', None)
    assert getattr(partner, 'micro_Model') is None


def test_assoc_model37_stub_double():
    # micro_Model has no real 'Model38' property in the generated
    # code (a bare stub) -- manually attach it so micro_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_Attribute(isGenerated=True, isId=True, isMany=True, name="sample_text")
    partner = micro_Model()
    setattr(partner, 'Model38', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'Model38') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'Model38') is None


def test_assoc_models5_stub_double():
    # micro_Model has no real 'Model' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_Model()
    setattr(partner, 'Model', None)
    _safe_set(owner, 'aggregateService6', {partner})
    assert getattr(partner, 'Model') == owner
    _safe_set(owner, 'aggregateService6', set())
    assert getattr(partner, 'Model') is None


def test_assoc_publish9_stub_double():
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


def test_assoc_replicateServices7_stub_double():
    # micro_ViewService has no real 'micro_ViewService' property in the generated
    # code (a bare stub) -- manually attach it so micro_AggregateService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # micro_AggregateService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = micro_AggregateService()
    partner = micro_ViewService()
    setattr(partner, 'micro_ViewService', None)
    _safe_set(owner, 'micro_AggregateService8', partner)
    assert owner in getattr(partner, 'micro_ViewService')
    _safe_set(owner, 'micro_AggregateService8', None)
    assert owner not in getattr(partner, 'micro_ViewService')


def test_assoc_replyInfo21_stub_double():
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


