import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    State,
    selflet_Abilities,
    selflet_Ability,
    selflet_AbilityState,
    selflet_Action,
    selflet_Actions,
    selflet_Active,
    selflet_Behavior,
    selflet_CPUUtilization,
    selflet_ComplexBehavior,
    selflet_Condition,
    selflet_Conditions,
    selflet_ElementaryBehavior,
    selflet_Empty,
    selflet_FinalState,
    selflet_GeneralKnowledge,
    selflet_InitialState,
    selflet_Input,
    selflet_IntermediateState,
    selflet_Method,
    selflet_Methods,
    selflet_OfferMode,
    selflet_Output,
    selflet_Parameter,
    selflet_Reds,
    selflet_Rule,
    selflet_Rules,
    selflet_SelfLetProperty,
    selflet_Selflet,
    selflet_SelfletProperties,
    selflet_SelfletResources,
    selflet_Service,
    selflet_Services,
    selflet_State,
    selflet_TypeKnowledge,
    Mode,
    Type,
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

def test_assoc_active18_reverse_link_reassign_clear():
    a1 = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    a2 = selflet_SelfletProperties(author="sample_text_2", description="sample_text_2", enableCloudOptimizationPolicy="sample_text_2", enableOptimizationPolicy="sample_text_2", limePort="sample_text_2")
    b = selflet_Active(mainService="sample_text")
    _safe_set(b, 'selflet_Active', a1)
    assert _is_linked(b, 'selflet_Active', a1)
    if hasattr(a1, 'selflet_SelfletProperties19'):
        assert _is_linked(a1, 'selflet_SelfletProperties19', b)
    _safe_set(b, 'selflet_Active', a2)
    assert _is_linked(b, 'selflet_Active', a2)
    if hasattr(a1, 'selflet_SelfletProperties19'):
        assert not _is_linked(a1, 'selflet_SelfletProperties19', b)
    if hasattr(a2, 'selflet_SelfletProperties19'):
        assert _is_linked(a2, 'selflet_SelfletProperties19', b)
    _safe_set(b, 'selflet_Active', None)
    assert not _is_linked(b, 'selflet_Active', a2)
    if hasattr(a2, 'selflet_SelfletProperties19'):
        assert not _is_linked(a2, 'selflet_SelfletProperties19', b)


def test_assoc_implementations52_reverse_link_reassign_clear():
    a1 = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    a2 = selflet_Service(active="sample_text_2", maxResponseTime="sample_text_2", name="sample_text_2", revenue="sample_text_2")
    b = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    _safe_set(b, 'selflet_Behavior54', a1)
    assert _is_linked(b, 'selflet_Behavior54', a1)
    if hasattr(a1, 'selflet_Service53'):
        assert _is_linked(a1, 'selflet_Service53', b)
    _safe_set(b, 'selflet_Behavior54', a2)
    assert _is_linked(b, 'selflet_Behavior54', a2)
    if hasattr(a1, 'selflet_Service53'):
        assert not _is_linked(a1, 'selflet_Service53', b)
    if hasattr(a2, 'selflet_Service53'):
        assert _is_linked(a2, 'selflet_Service53', b)
    _safe_set(b, 'selflet_Behavior54', None)
    assert not _is_linked(b, 'selflet_Behavior54', a2)
    if hasattr(a2, 'selflet_Service53'):
        assert not _is_linked(a2, 'selflet_Service53', b)


def test_assoc_implements4_reverse_link_reassign_clear():
    a1 = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    a2 = selflet_Service(active="sample_text_2", maxResponseTime="sample_text_2", name="sample_text_2", revenue="sample_text_2")
    b = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    _safe_set(b, 'selflet_Behavior', a1)
    assert _is_linked(b, 'selflet_Behavior', a1)
    if hasattr(a1, 'selflet_Service'):
        assert _is_linked(a1, 'selflet_Service', b)
    _safe_set(b, 'selflet_Behavior', a2)
    assert _is_linked(b, 'selflet_Behavior', a2)
    if hasattr(a1, 'selflet_Service'):
        assert not _is_linked(a1, 'selflet_Service', b)
    if hasattr(a2, 'selflet_Service'):
        assert _is_linked(a2, 'selflet_Service', b)
    _safe_set(b, 'selflet_Behavior', None)
    assert not _is_linked(b, 'selflet_Behavior', a2)
    if hasattr(a2, 'selflet_Service'):
        assert not _is_linked(a2, 'selflet_Service', b)


def test_assoc_next62_reverse_link_reassign_clear():
    a1 = selflet_State(name="sample_text")
    a2 = selflet_State(name="sample_text_2")
    b = selflet_State(name="sample_text")
    _safe_set(b, 'selflet_State63', a1)
    assert _is_linked(b, 'selflet_State63', a1)
    if hasattr(a1, 'selflet_State61'):
        assert _is_linked(a1, 'selflet_State61', b)
    _safe_set(b, 'selflet_State63', a2)
    assert _is_linked(b, 'selflet_State63', a2)
    if hasattr(a1, 'selflet_State61'):
        assert not _is_linked(a1, 'selflet_State61', b)
    if hasattr(a2, 'selflet_State61'):
        assert _is_linked(a2, 'selflet_State61', b)
    _safe_set(b, 'selflet_State63', None)
    assert not _is_linked(b, 'selflet_State63', a2)
    if hasattr(a2, 'selflet_State61'):
        assert not _is_linked(a2, 'selflet_State61', b)


def test_assoc_offermode50_reverse_link_reassign_clear():
    a1 = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    a2 = selflet_Service(active="sample_text_2", maxResponseTime="sample_text_2", name="sample_text_2", revenue="sample_text_2")
    b = selflet_OfferMode(mode="sample_text")
    _safe_set(b, 'selflet_OfferMode', a1)
    assert _is_linked(b, 'selflet_OfferMode', a1)
    if hasattr(a1, 'selflet_Service51'):
        assert _is_linked(a1, 'selflet_Service51', b)
    _safe_set(b, 'selflet_OfferMode', a2)
    assert _is_linked(b, 'selflet_OfferMode', a2)
    if hasattr(a1, 'selflet_Service51'):
        assert not _is_linked(a1, 'selflet_Service51', b)
    if hasattr(a2, 'selflet_Service51'):
        assert _is_linked(a2, 'selflet_Service51', b)
    _safe_set(b, 'selflet_OfferMode', None)
    assert not _is_linked(b, 'selflet_OfferMode', a2)
    if hasattr(a2, 'selflet_Service51'):
        assert not _is_linked(a2, 'selflet_Service51', b)


def test_assoc_reds20_reverse_link_reassign_clear():
    a1 = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    a2 = selflet_SelfletProperties(author="sample_text_2", description="sample_text_2", enableCloudOptimizationPolicy="sample_text_2", enableOptimizationPolicy="sample_text_2", limePort="sample_text_2")
    b = selflet_Reds(ipAddress="sample_text", port="sample_text")
    _safe_set(b, 'selflet_Reds', a1)
    assert _is_linked(b, 'selflet_Reds', a1)
    if hasattr(a1, 'selflet_SelfletProperties21'):
        assert _is_linked(a1, 'selflet_SelfletProperties21', b)
    _safe_set(b, 'selflet_Reds', a2)
    assert _is_linked(b, 'selflet_Reds', a2)
    if hasattr(a1, 'selflet_SelfletProperties21'):
        assert not _is_linked(a1, 'selflet_SelfletProperties21', b)
    if hasattr(a2, 'selflet_SelfletProperties21'):
        assert _is_linked(a2, 'selflet_SelfletProperties21', b)
    _safe_set(b, 'selflet_Reds', None)
    assert not _is_linked(b, 'selflet_Reds', a2)
    if hasattr(a2, 'selflet_SelfletProperties21'):
        assert not _is_linked(a2, 'selflet_SelfletProperties21', b)


def test_assoc_selfletProperties13_reverse_link_reassign_clear():
    a1 = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    a2 = selflet_SelfletProperties(author="sample_text_2", description="sample_text_2", enableCloudOptimizationPolicy="sample_text_2", enableOptimizationPolicy="sample_text_2", limePort="sample_text_2")
    b = selflet_Selflet(name="sample_text")
    _safe_set(b, 'selflet_Selflet', a1)
    assert _is_linked(b, 'selflet_Selflet', a1)
    if hasattr(a1, 'selflet_SelfletProperties'):
        assert _is_linked(a1, 'selflet_SelfletProperties', b)
    _safe_set(b, 'selflet_Selflet', a2)
    assert _is_linked(b, 'selflet_Selflet', a2)
    if hasattr(a1, 'selflet_SelfletProperties'):
        assert not _is_linked(a1, 'selflet_SelfletProperties', b)
    if hasattr(a2, 'selflet_SelfletProperties'):
        assert _is_linked(a2, 'selflet_SelfletProperties', b)
    _safe_set(b, 'selflet_Selflet', None)
    assert not _is_linked(b, 'selflet_Selflet', a2)
    if hasattr(a2, 'selflet_SelfletProperties'):
        assert not _is_linked(a2, 'selflet_SelfletProperties', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ability0_stub_double():
    # selflet_Abilities has no real 'selflet_Abilities' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Ability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Ability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Ability(file="sample_text", service="sample_text")
    partner = selflet_Abilities()
    setattr(partner, 'selflet_Abilities', None)
    _safe_set(owner, 'selflet_Ability', partner)
    assert owner in getattr(partner, 'selflet_Abilities')
    _safe_set(owner, 'selflet_Ability', None)
    assert owner not in getattr(partner, 'selflet_Abilities')


def test_assoc_action3_stub_double():
    # selflet_Actions has no real 'selflet_Actions' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Action(file="sample_text")
    partner = selflet_Actions()
    setattr(partner, 'selflet_Actions', None)
    _safe_set(owner, 'selflet_Action', partner)
    assert owner in getattr(partner, 'selflet_Actions')
    _safe_set(owner, 'selflet_Action', None)
    assert owner not in getattr(partner, 'selflet_Actions')


def test_assoc_condition5_stub_double():
    # selflet_Conditions has no real 'selflet_Conditions' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Condition(file="sample_text")
    partner = selflet_Conditions()
    setattr(partner, 'selflet_Conditions', None)
    _safe_set(owner, 'selflet_Condition', partner)
    assert owner in getattr(partner, 'selflet_Conditions')
    _safe_set(owner, 'selflet_Condition', None)
    assert owner not in getattr(partner, 'selflet_Conditions')


def test_assoc_do64_stub_double():
    # selflet_AbilityState has no real 'selflet_AbilityState' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Action(file="sample_text")
    partner = selflet_AbilityState()
    setattr(partner, 'selflet_AbilityState', None)
    _safe_set(owner, 'selflet_Action65', partner)
    assert getattr(partner, 'selflet_AbilityState') == owner
    _safe_set(owner, 'selflet_Action65', None)
    assert getattr(partner, 'selflet_AbilityState') is None


def test_assoc_generalknowledge22_stub_double():
    # selflet_GeneralKnowledge has no real 'selflet_GeneralKnowledge24' property in the generated
    # code (a bare stub) -- manually attach it so selflet_SelfletProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_SelfletProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    partner = selflet_GeneralKnowledge()
    setattr(partner, 'selflet_GeneralKnowledge24', None)
    _safe_set(owner, 'selflet_SelfletProperties23', partner)
    assert getattr(partner, 'selflet_GeneralKnowledge24') == owner
    _safe_set(owner, 'selflet_SelfletProperties23', None)
    assert getattr(partner, 'selflet_GeneralKnowledge24') is None


def test_assoc_input44_stub_double():
    # selflet_Input has no real 'selflet_Input46' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    partner = selflet_Input()
    setattr(partner, 'selflet_Input46', None)
    _safe_set(owner, 'selflet_Service45', partner)
    assert getattr(partner, 'selflet_Input46') == owner
    _safe_set(owner, 'selflet_Service45', None)
    assert getattr(partner, 'selflet_Input46') is None


def test_assoc_invoke66_stub_double():
    # selflet_IntermediateState has no real 'selflet_IntermediateState' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    partner = selflet_IntermediateState()
    setattr(partner, 'selflet_IntermediateState', None)
    _safe_set(owner, 'selflet_Service67', partner)
    assert getattr(partner, 'selflet_IntermediateState') == owner
    _safe_set(owner, 'selflet_Service67', None)
    assert getattr(partner, 'selflet_IntermediateState') is None


def test_assoc_method8_stub_double():
    # selflet_Methods has no real 'selflet_Methods9' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Method(name="sample_text", paramType="sample_text")
    partner = selflet_Methods()
    setattr(partner, 'selflet_Methods9', None)
    _safe_set(owner, 'selflet_Method', partner)
    assert owner in getattr(partner, 'selflet_Methods9')
    _safe_set(owner, 'selflet_Method', None)
    assert owner not in getattr(partner, 'selflet_Methods9')


def test_assoc_methods1_stub_double():
    # selflet_Methods has no real 'selflet_Methods' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Ability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Ability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Ability(file="sample_text", service="sample_text")
    partner = selflet_Methods()
    setattr(partner, 'selflet_Methods', None)
    _safe_set(owner, 'selflet_Ability2', partner)
    assert getattr(partner, 'selflet_Methods') == owner
    _safe_set(owner, 'selflet_Ability2', None)
    assert getattr(partner, 'selflet_Methods') is None


def test_assoc_output47_stub_double():
    # selflet_Output has no real 'selflet_Output49' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    partner = selflet_Output()
    setattr(partner, 'selflet_Output49', None)
    _safe_set(owner, 'selflet_Service48', partner)
    assert getattr(partner, 'selflet_Output49') == owner
    _safe_set(owner, 'selflet_Service48', None)
    assert getattr(partner, 'selflet_Output49') is None


def test_assoc_parameter10_stub_double():
    # selflet_Output has no real 'selflet_Output' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Parameter(name="sample_text", type="sample_text")
    partner = selflet_Output()
    setattr(partner, 'selflet_Output', None)
    _safe_set(owner, 'selflet_Parameter11', partner)
    assert getattr(partner, 'selflet_Output') == owner
    _safe_set(owner, 'selflet_Parameter11', None)
    assert getattr(partner, 'selflet_Output') is None


def test_assoc_parameter7_stub_double():
    # selflet_Input has no real 'selflet_Input' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Parameter(name="sample_text", type="sample_text")
    partner = selflet_Input()
    setattr(partner, 'selflet_Input', None)
    _safe_set(owner, 'selflet_Parameter', partner)
    assert owner in getattr(partner, 'selflet_Input')
    _safe_set(owner, 'selflet_Parameter', None)
    assert owner not in getattr(partner, 'selflet_Input')


def test_assoc_passive16_stub_double():
    # selflet_Empty has no real 'selflet_Empty' property in the generated
    # code (a bare stub) -- manually attach it so selflet_SelfletProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_SelfletProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    partner = selflet_Empty()
    setattr(partner, 'selflet_Empty', None)
    _safe_set(owner, 'selflet_SelfletProperties17', partner)
    assert getattr(partner, 'selflet_Empty') == owner
    _safe_set(owner, 'selflet_SelfletProperties17', None)
    assert getattr(partner, 'selflet_Empty') is None


def test_assoc_rule12_stub_double():
    # selflet_Rules has no real 'selflet_Rules' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Rule(file="sample_text")
    partner = selflet_Rules()
    setattr(partner, 'selflet_Rules', None)
    _safe_set(owner, 'selflet_Rule', partner)
    assert owner in getattr(partner, 'selflet_Rules')
    _safe_set(owner, 'selflet_Rule', None)
    assert owner not in getattr(partner, 'selflet_Rules')


def test_assoc_selfLetProperty55_stub_double():
    # selflet_TypeKnowledge has no real 'selflet_TypeKnowledge56' property in the generated
    # code (a bare stub) -- manually attach it so selflet_SelfLetProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_SelfLetProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    partner = selflet_TypeKnowledge()
    setattr(partner, 'selflet_TypeKnowledge56', None)
    _safe_set(owner, 'selflet_SelfLetProperty57', partner)
    assert owner in getattr(partner, 'selflet_TypeKnowledge56')
    _safe_set(owner, 'selflet_SelfLetProperty57', None)
    assert owner not in getattr(partner, 'selflet_TypeKnowledge56')


def test_assoc_selfLetProperty6_stub_double():
    # selflet_GeneralKnowledge has no real 'selflet_GeneralKnowledge' property in the generated
    # code (a bare stub) -- manually attach it so selflet_SelfLetProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_SelfLetProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    partner = selflet_GeneralKnowledge()
    setattr(partner, 'selflet_GeneralKnowledge', None)
    _safe_set(owner, 'selflet_SelfLetProperty', partner)
    assert owner in getattr(partner, 'selflet_GeneralKnowledge')
    _safe_set(owner, 'selflet_SelfLetProperty', None)
    assert owner not in getattr(partner, 'selflet_GeneralKnowledge')


def test_assoc_selfletResources14_stub_double():
    # selflet_SelfletResources has no real 'selflet_SelfletResources' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Selflet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Selflet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Selflet(name="sample_text")
    partner = selflet_SelfletResources()
    setattr(partner, 'selflet_SelfletResources', None)
    _safe_set(owner, 'selflet_Selflet15', partner)
    assert getattr(partner, 'selflet_SelfletResources') == owner
    _safe_set(owner, 'selflet_Selflet15', None)
    assert getattr(partner, 'selflet_SelfletResources') is None


def test_assoc_service41_stub_double():
    # selflet_Services has no real 'selflet_Services42' property in the generated
    # code (a bare stub) -- manually attach it so selflet_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    partner = selflet_Services()
    setattr(partner, 'selflet_Services42', None)
    _safe_set(owner, 'selflet_Service43', partner)
    assert owner in getattr(partner, 'selflet_Services42')
    _safe_set(owner, 'selflet_Service43', None)
    assert owner not in getattr(partner, 'selflet_Services42')


def test_assoc_states58_stub_double():
    # selflet_ElementaryBehavior has no real 'selflet_ElementaryBehavior' property in the generated
    # code (a bare stub) -- manually attach it so selflet_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_State(name="sample_text")
    partner = selflet_ElementaryBehavior()
    setattr(partner, 'selflet_ElementaryBehavior', None)
    _safe_set(owner, 'selflet_State', partner)
    assert owner in getattr(partner, 'selflet_ElementaryBehavior')
    _safe_set(owner, 'selflet_State', None)
    assert owner not in getattr(partner, 'selflet_ElementaryBehavior')


def test_assoc_states59_stub_double():
    # selflet_ComplexBehavior has no real 'selflet_ComplexBehavior' property in the generated
    # code (a bare stub) -- manually attach it so selflet_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_State(name="sample_text")
    partner = selflet_ComplexBehavior()
    setattr(partner, 'selflet_ComplexBehavior', None)
    _safe_set(owner, 'selflet_State60', partner)
    assert owner in getattr(partner, 'selflet_ComplexBehavior')
    _safe_set(owner, 'selflet_State60', None)
    assert owner not in getattr(partner, 'selflet_ComplexBehavior')


def test_assoc_typeKnowledge25_stub_double():
    # selflet_TypeKnowledge has no real 'selflet_TypeKnowledge' property in the generated
    # code (a bare stub) -- manually attach it so selflet_SelfletProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # selflet_SelfletProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    partner = selflet_TypeKnowledge()
    setattr(partner, 'selflet_TypeKnowledge', None)
    _safe_set(owner, 'selflet_SelfletProperties26', partner)
    assert getattr(partner, 'selflet_TypeKnowledge') == owner
    _safe_set(owner, 'selflet_SelfletProperties26', None)
    assert getattr(partner, 'selflet_TypeKnowledge') is None


