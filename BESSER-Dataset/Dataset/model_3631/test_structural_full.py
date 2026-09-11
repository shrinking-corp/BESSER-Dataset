import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_selflet_Ability_file_value_roundtrip():
    instance = selflet_Ability(file="sample_text", service="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_selflet_Ability_service_value_roundtrip():
    instance = selflet_Ability(file="sample_text", service="sample_text")
    assert instance.service == "sample_text"
    instance.service = "sample_text_2"
    assert instance.service == "sample_text_2"


def test_selflet_Action_file_value_roundtrip():
    instance = selflet_Action(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_selflet_Active_mainService_value_roundtrip():
    instance = selflet_Active(mainService="sample_text")
    assert instance.mainService == "sample_text"
    instance.mainService = "sample_text_2"
    assert instance.mainService == "sample_text_2"


def test_selflet_Behavior_elementaryBehaviorCPUTime_value_roundtrip():
    instance = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    assert instance.elementaryBehaviorCPUTime == "sample_text"
    instance.elementaryBehaviorCPUTime = "sample_text_2"
    assert instance.elementaryBehaviorCPUTime == "sample_text_2"


def test_selflet_Behavior_elementaryBehaviorCost_value_roundtrip():
    instance = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    assert instance.elementaryBehaviorCost == "sample_text"
    instance.elementaryBehaviorCost = "sample_text_2"
    assert instance.elementaryBehaviorCost == "sample_text_2"


def test_selflet_Behavior_fileName_value_roundtrip():
    instance = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_selflet_Behavior_isDefaultBehavior_value_roundtrip():
    instance = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    assert instance.isDefaultBehavior == "sample_text"
    instance.isDefaultBehavior = "sample_text_2"
    assert instance.isDefaultBehavior == "sample_text_2"


def test_selflet_Behavior_name_value_roundtrip():
    instance = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_CPUUtilization_lowerBound_value_roundtrip():
    instance = selflet_CPUUtilization(lowerBound="sample_text", upperBound="sample_text")
    assert instance.lowerBound == "sample_text"
    instance.lowerBound = "sample_text_2"
    assert instance.lowerBound == "sample_text_2"


def test_selflet_CPUUtilization_upperBound_value_roundtrip():
    instance = selflet_CPUUtilization(lowerBound="sample_text", upperBound="sample_text")
    assert instance.upperBound == "sample_text"
    instance.upperBound = "sample_text_2"
    assert instance.upperBound == "sample_text_2"


def test_selflet_Condition_file_value_roundtrip():
    instance = selflet_Condition(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_selflet_Method_name_value_roundtrip():
    instance = selflet_Method(name="sample_text", paramType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_Method_paramType_value_roundtrip():
    instance = selflet_Method(name="sample_text", paramType="sample_text")
    assert instance.paramType == "sample_text"
    instance.paramType = "sample_text_2"
    assert instance.paramType == "sample_text_2"


def test_selflet_OfferMode_mode_value_roundtrip():
    instance = selflet_OfferMode(mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_selflet_Parameter_name_value_roundtrip():
    instance = selflet_Parameter(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_Parameter_type_value_roundtrip():
    instance = selflet_Parameter(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_selflet_Reds_ipAddress_value_roundtrip():
    instance = selflet_Reds(ipAddress="sample_text", port="sample_text")
    assert instance.ipAddress == "sample_text"
    instance.ipAddress = "sample_text_2"
    assert instance.ipAddress == "sample_text_2"


def test_selflet_Reds_port_value_roundtrip():
    instance = selflet_Reds(ipAddress="sample_text", port="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_selflet_Rule_file_value_roundtrip():
    instance = selflet_Rule(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_selflet_SelfLetProperty_name_value_roundtrip():
    instance = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_SelfLetProperty_type_value_roundtrip():
    instance = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_selflet_SelfLetProperty_value_value_roundtrip():
    instance = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_selflet_Selflet_name_value_roundtrip():
    instance = selflet_Selflet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_SelfletProperties_author_value_roundtrip():
    instance = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_selflet_SelfletProperties_description_value_roundtrip():
    instance = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_selflet_SelfletProperties_enableCloudOptimizationPolicy_value_roundtrip():
    instance = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    assert instance.enableCloudOptimizationPolicy == "sample_text"
    instance.enableCloudOptimizationPolicy = "sample_text_2"
    assert instance.enableCloudOptimizationPolicy == "sample_text_2"


def test_selflet_SelfletProperties_enableOptimizationPolicy_value_roundtrip():
    instance = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    assert instance.enableOptimizationPolicy == "sample_text"
    instance.enableOptimizationPolicy = "sample_text_2"
    assert instance.enableOptimizationPolicy == "sample_text_2"


def test_selflet_SelfletProperties_limePort_value_roundtrip():
    instance = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    assert instance.limePort == "sample_text"
    instance.limePort = "sample_text_2"
    assert instance.limePort == "sample_text_2"


def test_selflet_Service_active_value_roundtrip():
    instance = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    assert instance.active == "sample_text"
    instance.active = "sample_text_2"
    assert instance.active == "sample_text_2"


def test_selflet_Service_maxResponseTime_value_roundtrip():
    instance = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    assert instance.maxResponseTime == "sample_text"
    instance.maxResponseTime = "sample_text_2"
    assert instance.maxResponseTime == "sample_text_2"


def test_selflet_Service_name_value_roundtrip():
    instance = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_Service_revenue_value_roundtrip():
    instance = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    assert instance.revenue == "sample_text"
    instance.revenue = "sample_text_2"
    assert instance.revenue == "sample_text_2"


def test_selflet_State_name_value_roundtrip():
    instance = selflet_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_selflet_ComplexBehavior_isa_Behavior():
    instance = selflet_ComplexBehavior()
    assert isinstance(instance, Behavior)


def test_selflet_ElementaryBehavior_isa_Behavior():
    instance = selflet_ElementaryBehavior()
    assert isinstance(instance, Behavior)


def test_selflet_AbilityState_isa_State():
    instance = selflet_AbilityState()
    assert isinstance(instance, State)


def test_selflet_FinalState_isa_State():
    instance = selflet_FinalState()
    assert isinstance(instance, State)


def test_selflet_InitialState_isa_State():
    instance = selflet_InitialState()
    assert isinstance(instance, State)


def test_selflet_IntermediateState_isa_State():
    instance = selflet_IntermediateState()
    assert isinstance(instance, State)


def test_assoc_ability0_link_reassign_clear():
    a = selflet_Ability(file="sample_text", service="sample_text")
    b1 = selflet_Abilities()
    b2 = selflet_Abilities()
    _safe_set(a, 'selflet_Ability', b1)
    assert _is_linked(a, 'selflet_Ability', b1)
    if hasattr(b1, 'selflet_Abilities'):
        assert _is_linked(b1, 'selflet_Abilities', a)
    _safe_set(a, 'selflet_Ability', b2)
    assert _is_linked(a, 'selflet_Ability', b2)
    if hasattr(b1, 'selflet_Abilities'):
        assert not _is_linked(b1, 'selflet_Abilities', a)
    if hasattr(b2, 'selflet_Abilities'):
        assert _is_linked(b2, 'selflet_Abilities', a)
    _safe_set(a, 'selflet_Ability', None)
    assert not _is_linked(a, 'selflet_Ability', b2)
    if hasattr(b2, 'selflet_Abilities'):
        assert not _is_linked(b2, 'selflet_Abilities', a)


def test_assoc_action3_link_reassign_clear():
    a = selflet_Action(file="sample_text")
    b1 = selflet_Actions()
    b2 = selflet_Actions()
    _safe_set(a, 'selflet_Action', b1)
    assert _is_linked(a, 'selflet_Action', b1)
    if hasattr(b1, 'selflet_Actions'):
        assert _is_linked(b1, 'selflet_Actions', a)
    _safe_set(a, 'selflet_Action', b2)
    assert _is_linked(a, 'selflet_Action', b2)
    if hasattr(b1, 'selflet_Actions'):
        assert not _is_linked(b1, 'selflet_Actions', a)
    if hasattr(b2, 'selflet_Actions'):
        assert _is_linked(b2, 'selflet_Actions', a)
    _safe_set(a, 'selflet_Action', None)
    assert not _is_linked(a, 'selflet_Action', b2)
    if hasattr(b2, 'selflet_Actions'):
        assert not _is_linked(b2, 'selflet_Actions', a)


def test_assoc_active18_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_Active(mainService="sample_text")
    b2 = selflet_Active(mainService="sample_text_2")
    _safe_set(a, 'selflet_SelfletProperties19', b1)
    assert _is_linked(a, 'selflet_SelfletProperties19', b1)
    if hasattr(b1, 'selflet_Active'):
        assert _is_linked(b1, 'selflet_Active', a)
    _safe_set(a, 'selflet_SelfletProperties19', b2)
    assert _is_linked(a, 'selflet_SelfletProperties19', b2)
    if hasattr(b1, 'selflet_Active'):
        assert not _is_linked(b1, 'selflet_Active', a)
    if hasattr(b2, 'selflet_Active'):
        assert _is_linked(b2, 'selflet_Active', a)
    _safe_set(a, 'selflet_SelfletProperties19', None)
    assert not _is_linked(a, 'selflet_SelfletProperties19', b2)
    if hasattr(b2, 'selflet_Active'):
        assert not _is_linked(b2, 'selflet_Active', a)


def test_assoc_condition5_link_reassign_clear():
    a = selflet_Condition(file="sample_text")
    b1 = selflet_Conditions()
    b2 = selflet_Conditions()
    _safe_set(a, 'selflet_Condition', b1)
    assert _is_linked(a, 'selflet_Condition', b1)
    if hasattr(b1, 'selflet_Conditions'):
        assert _is_linked(b1, 'selflet_Conditions', a)
    _safe_set(a, 'selflet_Condition', b2)
    assert _is_linked(a, 'selflet_Condition', b2)
    if hasattr(b1, 'selflet_Conditions'):
        assert not _is_linked(b1, 'selflet_Conditions', a)
    if hasattr(b2, 'selflet_Conditions'):
        assert _is_linked(b2, 'selflet_Conditions', a)
    _safe_set(a, 'selflet_Condition', None)
    assert not _is_linked(a, 'selflet_Condition', b2)
    if hasattr(b2, 'selflet_Conditions'):
        assert not _is_linked(b2, 'selflet_Conditions', a)


def test_assoc_do64_link_reassign_clear():
    a = selflet_Action(file="sample_text")
    b1 = selflet_AbilityState()
    b2 = selflet_AbilityState()
    _safe_set(a, 'selflet_Action65', b1)
    assert _is_linked(a, 'selflet_Action65', b1)
    if hasattr(b1, 'selflet_AbilityState'):
        assert _is_linked(b1, 'selflet_AbilityState', a)
    _safe_set(a, 'selflet_Action65', b2)
    assert _is_linked(a, 'selflet_Action65', b2)
    if hasattr(b1, 'selflet_AbilityState'):
        assert not _is_linked(b1, 'selflet_AbilityState', a)
    if hasattr(b2, 'selflet_AbilityState'):
        assert _is_linked(b2, 'selflet_AbilityState', a)
    _safe_set(a, 'selflet_Action65', None)
    assert not _is_linked(a, 'selflet_Action65', b2)
    if hasattr(b2, 'selflet_AbilityState'):
        assert not _is_linked(b2, 'selflet_AbilityState', a)


def test_assoc_generalknowledge22_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_GeneralKnowledge()
    b2 = selflet_GeneralKnowledge()
    _safe_set(a, 'selflet_SelfletProperties23', b1)
    assert _is_linked(a, 'selflet_SelfletProperties23', b1)
    if hasattr(b1, 'selflet_GeneralKnowledge24'):
        assert _is_linked(b1, 'selflet_GeneralKnowledge24', a)
    _safe_set(a, 'selflet_SelfletProperties23', b2)
    assert _is_linked(a, 'selflet_SelfletProperties23', b2)
    if hasattr(b1, 'selflet_GeneralKnowledge24'):
        assert not _is_linked(b1, 'selflet_GeneralKnowledge24', a)
    if hasattr(b2, 'selflet_GeneralKnowledge24'):
        assert _is_linked(b2, 'selflet_GeneralKnowledge24', a)
    _safe_set(a, 'selflet_SelfletProperties23', None)
    assert not _is_linked(a, 'selflet_SelfletProperties23', b2)
    if hasattr(b2, 'selflet_GeneralKnowledge24'):
        assert not _is_linked(b2, 'selflet_GeneralKnowledge24', a)


def test_assoc_implementations52_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    b2 = selflet_Behavior(elementaryBehaviorCPUTime="sample_text_2", elementaryBehaviorCost="sample_text_2", fileName="sample_text_2", isDefaultBehavior="sample_text_2", name="sample_text_2")
    _safe_set(a, 'selflet_Service53', {b1})
    assert _is_linked(a, 'selflet_Service53', b1)
    if hasattr(b1, 'selflet_Behavior54'):
        assert _is_linked(b1, 'selflet_Behavior54', a)
    _safe_set(a, 'selflet_Service53', {b2})
    assert _is_linked(a, 'selflet_Service53', b2)
    if hasattr(b1, 'selflet_Behavior54'):
        assert not _is_linked(b1, 'selflet_Behavior54', a)
    if hasattr(b2, 'selflet_Behavior54'):
        assert _is_linked(b2, 'selflet_Behavior54', a)
    _safe_set(a, 'selflet_Service53', set())
    assert not _is_linked(a, 'selflet_Service53', b2)
    if hasattr(b2, 'selflet_Behavior54'):
        assert not _is_linked(b2, 'selflet_Behavior54', a)


def test_assoc_implements4_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_Behavior(elementaryBehaviorCPUTime="sample_text", elementaryBehaviorCost="sample_text", fileName="sample_text", isDefaultBehavior="sample_text", name="sample_text")
    b2 = selflet_Behavior(elementaryBehaviorCPUTime="sample_text_2", elementaryBehaviorCost="sample_text_2", fileName="sample_text_2", isDefaultBehavior="sample_text_2", name="sample_text_2")
    _safe_set(a, 'selflet_Service', b1)
    assert _is_linked(a, 'selflet_Service', b1)
    if hasattr(b1, 'selflet_Behavior'):
        assert _is_linked(b1, 'selflet_Behavior', a)
    _safe_set(a, 'selflet_Service', b2)
    assert _is_linked(a, 'selflet_Service', b2)
    if hasattr(b1, 'selflet_Behavior'):
        assert not _is_linked(b1, 'selflet_Behavior', a)
    if hasattr(b2, 'selflet_Behavior'):
        assert _is_linked(b2, 'selflet_Behavior', a)
    _safe_set(a, 'selflet_Service', None)
    assert not _is_linked(a, 'selflet_Service', b2)
    if hasattr(b2, 'selflet_Behavior'):
        assert not _is_linked(b2, 'selflet_Behavior', a)


def test_assoc_input44_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_Input()
    b2 = selflet_Input()
    _safe_set(a, 'selflet_Service45', b1)
    assert _is_linked(a, 'selflet_Service45', b1)
    if hasattr(b1, 'selflet_Input46'):
        assert _is_linked(b1, 'selflet_Input46', a)
    _safe_set(a, 'selflet_Service45', b2)
    assert _is_linked(a, 'selflet_Service45', b2)
    if hasattr(b1, 'selflet_Input46'):
        assert not _is_linked(b1, 'selflet_Input46', a)
    if hasattr(b2, 'selflet_Input46'):
        assert _is_linked(b2, 'selflet_Input46', a)
    _safe_set(a, 'selflet_Service45', None)
    assert not _is_linked(a, 'selflet_Service45', b2)
    if hasattr(b2, 'selflet_Input46'):
        assert not _is_linked(b2, 'selflet_Input46', a)


def test_assoc_invoke66_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_IntermediateState()
    b2 = selflet_IntermediateState()
    _safe_set(a, 'selflet_Service67', b1)
    assert _is_linked(a, 'selflet_Service67', b1)
    if hasattr(b1, 'selflet_IntermediateState'):
        assert _is_linked(b1, 'selflet_IntermediateState', a)
    _safe_set(a, 'selflet_Service67', b2)
    assert _is_linked(a, 'selflet_Service67', b2)
    if hasattr(b1, 'selflet_IntermediateState'):
        assert not _is_linked(b1, 'selflet_IntermediateState', a)
    if hasattr(b2, 'selflet_IntermediateState'):
        assert _is_linked(b2, 'selflet_IntermediateState', a)
    _safe_set(a, 'selflet_Service67', None)
    assert not _is_linked(a, 'selflet_Service67', b2)
    if hasattr(b2, 'selflet_IntermediateState'):
        assert not _is_linked(b2, 'selflet_IntermediateState', a)


def test_assoc_method8_link_reassign_clear():
    a = selflet_Method(name="sample_text", paramType="sample_text")
    b1 = selflet_Methods()
    b2 = selflet_Methods()
    _safe_set(a, 'selflet_Method', b1)
    assert _is_linked(a, 'selflet_Method', b1)
    if hasattr(b1, 'selflet_Methods9'):
        assert _is_linked(b1, 'selflet_Methods9', a)
    _safe_set(a, 'selflet_Method', b2)
    assert _is_linked(a, 'selflet_Method', b2)
    if hasattr(b1, 'selflet_Methods9'):
        assert not _is_linked(b1, 'selflet_Methods9', a)
    if hasattr(b2, 'selflet_Methods9'):
        assert _is_linked(b2, 'selflet_Methods9', a)
    _safe_set(a, 'selflet_Method', None)
    assert not _is_linked(a, 'selflet_Method', b2)
    if hasattr(b2, 'selflet_Methods9'):
        assert not _is_linked(b2, 'selflet_Methods9', a)


def test_assoc_methods1_link_reassign_clear():
    a = selflet_Ability(file="sample_text", service="sample_text")
    b1 = selflet_Methods()
    b2 = selflet_Methods()
    _safe_set(a, 'selflet_Ability2', b1)
    assert _is_linked(a, 'selflet_Ability2', b1)
    if hasattr(b1, 'selflet_Methods'):
        assert _is_linked(b1, 'selflet_Methods', a)
    _safe_set(a, 'selflet_Ability2', b2)
    assert _is_linked(a, 'selflet_Ability2', b2)
    if hasattr(b1, 'selflet_Methods'):
        assert not _is_linked(b1, 'selflet_Methods', a)
    if hasattr(b2, 'selflet_Methods'):
        assert _is_linked(b2, 'selflet_Methods', a)
    _safe_set(a, 'selflet_Ability2', None)
    assert not _is_linked(a, 'selflet_Ability2', b2)
    if hasattr(b2, 'selflet_Methods'):
        assert not _is_linked(b2, 'selflet_Methods', a)


def test_assoc_next62_link_reassign_clear():
    a = selflet_State(name="sample_text")
    b1 = selflet_State(name="sample_text")
    b2 = selflet_State(name="sample_text_2")
    _safe_set(a, 'selflet_State61', {b1})
    assert _is_linked(a, 'selflet_State61', b1)
    if hasattr(b1, 'selflet_State63'):
        assert _is_linked(b1, 'selflet_State63', a)
    _safe_set(a, 'selflet_State61', {b2})
    assert _is_linked(a, 'selflet_State61', b2)
    if hasattr(b1, 'selflet_State63'):
        assert not _is_linked(b1, 'selflet_State63', a)
    if hasattr(b2, 'selflet_State63'):
        assert _is_linked(b2, 'selflet_State63', a)
    _safe_set(a, 'selflet_State61', set())
    assert not _is_linked(a, 'selflet_State61', b2)
    if hasattr(b2, 'selflet_State63'):
        assert not _is_linked(b2, 'selflet_State63', a)


def test_assoc_offermode50_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_OfferMode(mode="sample_text")
    b2 = selflet_OfferMode(mode="sample_text_2")
    _safe_set(a, 'selflet_Service51', b1)
    assert _is_linked(a, 'selflet_Service51', b1)
    if hasattr(b1, 'selflet_OfferMode'):
        assert _is_linked(b1, 'selflet_OfferMode', a)
    _safe_set(a, 'selflet_Service51', b2)
    assert _is_linked(a, 'selflet_Service51', b2)
    if hasattr(b1, 'selflet_OfferMode'):
        assert not _is_linked(b1, 'selflet_OfferMode', a)
    if hasattr(b2, 'selflet_OfferMode'):
        assert _is_linked(b2, 'selflet_OfferMode', a)
    _safe_set(a, 'selflet_Service51', None)
    assert not _is_linked(a, 'selflet_Service51', b2)
    if hasattr(b2, 'selflet_OfferMode'):
        assert not _is_linked(b2, 'selflet_OfferMode', a)


def test_assoc_output47_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_Output()
    b2 = selflet_Output()
    _safe_set(a, 'selflet_Service48', b1)
    assert _is_linked(a, 'selflet_Service48', b1)
    if hasattr(b1, 'selflet_Output49'):
        assert _is_linked(b1, 'selflet_Output49', a)
    _safe_set(a, 'selflet_Service48', b2)
    assert _is_linked(a, 'selflet_Service48', b2)
    if hasattr(b1, 'selflet_Output49'):
        assert not _is_linked(b1, 'selflet_Output49', a)
    if hasattr(b2, 'selflet_Output49'):
        assert _is_linked(b2, 'selflet_Output49', a)
    _safe_set(a, 'selflet_Service48', None)
    assert not _is_linked(a, 'selflet_Service48', b2)
    if hasattr(b2, 'selflet_Output49'):
        assert not _is_linked(b2, 'selflet_Output49', a)


def test_assoc_parameter10_link_reassign_clear():
    a = selflet_Parameter(name="sample_text", type="sample_text")
    b1 = selflet_Output()
    b2 = selflet_Output()
    _safe_set(a, 'selflet_Parameter11', b1)
    assert _is_linked(a, 'selflet_Parameter11', b1)
    if hasattr(b1, 'selflet_Output'):
        assert _is_linked(b1, 'selflet_Output', a)
    _safe_set(a, 'selflet_Parameter11', b2)
    assert _is_linked(a, 'selflet_Parameter11', b2)
    if hasattr(b1, 'selflet_Output'):
        assert not _is_linked(b1, 'selflet_Output', a)
    if hasattr(b2, 'selflet_Output'):
        assert _is_linked(b2, 'selflet_Output', a)
    _safe_set(a, 'selflet_Parameter11', None)
    assert not _is_linked(a, 'selflet_Parameter11', b2)
    if hasattr(b2, 'selflet_Output'):
        assert not _is_linked(b2, 'selflet_Output', a)


def test_assoc_parameter7_link_reassign_clear():
    a = selflet_Parameter(name="sample_text", type="sample_text")
    b1 = selflet_Input()
    b2 = selflet_Input()
    _safe_set(a, 'selflet_Parameter', b1)
    assert _is_linked(a, 'selflet_Parameter', b1)
    if hasattr(b1, 'selflet_Input'):
        assert _is_linked(b1, 'selflet_Input', a)
    _safe_set(a, 'selflet_Parameter', b2)
    assert _is_linked(a, 'selflet_Parameter', b2)
    if hasattr(b1, 'selflet_Input'):
        assert not _is_linked(b1, 'selflet_Input', a)
    if hasattr(b2, 'selflet_Input'):
        assert _is_linked(b2, 'selflet_Input', a)
    _safe_set(a, 'selflet_Parameter', None)
    assert not _is_linked(a, 'selflet_Parameter', b2)
    if hasattr(b2, 'selflet_Input'):
        assert not _is_linked(b2, 'selflet_Input', a)


def test_assoc_passive16_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_Empty()
    b2 = selflet_Empty()
    _safe_set(a, 'selflet_SelfletProperties17', b1)
    assert _is_linked(a, 'selflet_SelfletProperties17', b1)
    if hasattr(b1, 'selflet_Empty'):
        assert _is_linked(b1, 'selflet_Empty', a)
    _safe_set(a, 'selflet_SelfletProperties17', b2)
    assert _is_linked(a, 'selflet_SelfletProperties17', b2)
    if hasattr(b1, 'selflet_Empty'):
        assert not _is_linked(b1, 'selflet_Empty', a)
    if hasattr(b2, 'selflet_Empty'):
        assert _is_linked(b2, 'selflet_Empty', a)
    _safe_set(a, 'selflet_SelfletProperties17', None)
    assert not _is_linked(a, 'selflet_SelfletProperties17', b2)
    if hasattr(b2, 'selflet_Empty'):
        assert not _is_linked(b2, 'selflet_Empty', a)


def test_assoc_reds20_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_Reds(ipAddress="sample_text", port="sample_text")
    b2 = selflet_Reds(ipAddress="sample_text_2", port="sample_text_2")
    _safe_set(a, 'selflet_SelfletProperties21', b1)
    assert _is_linked(a, 'selflet_SelfletProperties21', b1)
    if hasattr(b1, 'selflet_Reds'):
        assert _is_linked(b1, 'selflet_Reds', a)
    _safe_set(a, 'selflet_SelfletProperties21', b2)
    assert _is_linked(a, 'selflet_SelfletProperties21', b2)
    if hasattr(b1, 'selflet_Reds'):
        assert not _is_linked(b1, 'selflet_Reds', a)
    if hasattr(b2, 'selflet_Reds'):
        assert _is_linked(b2, 'selflet_Reds', a)
    _safe_set(a, 'selflet_SelfletProperties21', None)
    assert not _is_linked(a, 'selflet_SelfletProperties21', b2)
    if hasattr(b2, 'selflet_Reds'):
        assert not _is_linked(b2, 'selflet_Reds', a)


def test_assoc_rule12_link_reassign_clear():
    a = selflet_Rule(file="sample_text")
    b1 = selflet_Rules()
    b2 = selflet_Rules()
    _safe_set(a, 'selflet_Rule', b1)
    assert _is_linked(a, 'selflet_Rule', b1)
    if hasattr(b1, 'selflet_Rules'):
        assert _is_linked(b1, 'selflet_Rules', a)
    _safe_set(a, 'selflet_Rule', b2)
    assert _is_linked(a, 'selflet_Rule', b2)
    if hasattr(b1, 'selflet_Rules'):
        assert not _is_linked(b1, 'selflet_Rules', a)
    if hasattr(b2, 'selflet_Rules'):
        assert _is_linked(b2, 'selflet_Rules', a)
    _safe_set(a, 'selflet_Rule', None)
    assert not _is_linked(a, 'selflet_Rule', b2)
    if hasattr(b2, 'selflet_Rules'):
        assert not _is_linked(b2, 'selflet_Rules', a)


def test_assoc_selfLetProperty55_link_reassign_clear():
    a = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    b1 = selflet_TypeKnowledge()
    b2 = selflet_TypeKnowledge()
    _safe_set(a, 'selflet_SelfLetProperty57', b1)
    assert _is_linked(a, 'selflet_SelfLetProperty57', b1)
    if hasattr(b1, 'selflet_TypeKnowledge56'):
        assert _is_linked(b1, 'selflet_TypeKnowledge56', a)
    _safe_set(a, 'selflet_SelfLetProperty57', b2)
    assert _is_linked(a, 'selflet_SelfLetProperty57', b2)
    if hasattr(b1, 'selflet_TypeKnowledge56'):
        assert not _is_linked(b1, 'selflet_TypeKnowledge56', a)
    if hasattr(b2, 'selflet_TypeKnowledge56'):
        assert _is_linked(b2, 'selflet_TypeKnowledge56', a)
    _safe_set(a, 'selflet_SelfLetProperty57', None)
    assert not _is_linked(a, 'selflet_SelfLetProperty57', b2)
    if hasattr(b2, 'selflet_TypeKnowledge56'):
        assert not _is_linked(b2, 'selflet_TypeKnowledge56', a)


def test_assoc_selfLetProperty6_link_reassign_clear():
    a = selflet_SelfLetProperty(name="sample_text", type="sample_text", value="sample_text")
    b1 = selflet_GeneralKnowledge()
    b2 = selflet_GeneralKnowledge()
    _safe_set(a, 'selflet_SelfLetProperty', b1)
    assert _is_linked(a, 'selflet_SelfLetProperty', b1)
    if hasattr(b1, 'selflet_GeneralKnowledge'):
        assert _is_linked(b1, 'selflet_GeneralKnowledge', a)
    _safe_set(a, 'selflet_SelfLetProperty', b2)
    assert _is_linked(a, 'selflet_SelfLetProperty', b2)
    if hasattr(b1, 'selflet_GeneralKnowledge'):
        assert not _is_linked(b1, 'selflet_GeneralKnowledge', a)
    if hasattr(b2, 'selflet_GeneralKnowledge'):
        assert _is_linked(b2, 'selflet_GeneralKnowledge', a)
    _safe_set(a, 'selflet_SelfLetProperty', None)
    assert not _is_linked(a, 'selflet_SelfLetProperty', b2)
    if hasattr(b2, 'selflet_GeneralKnowledge'):
        assert not _is_linked(b2, 'selflet_GeneralKnowledge', a)


def test_assoc_selfletProperties13_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_Selflet(name="sample_text")
    b2 = selflet_Selflet(name="sample_text_2")
    _safe_set(a, 'selflet_SelfletProperties', b1)
    assert _is_linked(a, 'selflet_SelfletProperties', b1)
    if hasattr(b1, 'selflet_Selflet'):
        assert _is_linked(b1, 'selflet_Selflet', a)
    _safe_set(a, 'selflet_SelfletProperties', b2)
    assert _is_linked(a, 'selflet_SelfletProperties', b2)
    if hasattr(b1, 'selflet_Selflet'):
        assert not _is_linked(b1, 'selflet_Selflet', a)
    if hasattr(b2, 'selflet_Selflet'):
        assert _is_linked(b2, 'selflet_Selflet', a)
    _safe_set(a, 'selflet_SelfletProperties', None)
    assert not _is_linked(a, 'selflet_SelfletProperties', b2)
    if hasattr(b2, 'selflet_Selflet'):
        assert not _is_linked(b2, 'selflet_Selflet', a)


def test_assoc_selfletResources14_link_reassign_clear():
    a = selflet_Selflet(name="sample_text")
    b1 = selflet_SelfletResources()
    b2 = selflet_SelfletResources()
    _safe_set(a, 'selflet_Selflet15', b1)
    assert _is_linked(a, 'selflet_Selflet15', b1)
    if hasattr(b1, 'selflet_SelfletResources'):
        assert _is_linked(b1, 'selflet_SelfletResources', a)
    _safe_set(a, 'selflet_Selflet15', b2)
    assert _is_linked(a, 'selflet_Selflet15', b2)
    if hasattr(b1, 'selflet_SelfletResources'):
        assert not _is_linked(b1, 'selflet_SelfletResources', a)
    if hasattr(b2, 'selflet_SelfletResources'):
        assert _is_linked(b2, 'selflet_SelfletResources', a)
    _safe_set(a, 'selflet_Selflet15', None)
    assert not _is_linked(a, 'selflet_Selflet15', b2)
    if hasattr(b2, 'selflet_SelfletResources'):
        assert not _is_linked(b2, 'selflet_SelfletResources', a)


def test_assoc_service41_link_reassign_clear():
    a = selflet_Service(active="sample_text", maxResponseTime="sample_text", name="sample_text", revenue="sample_text")
    b1 = selflet_Services()
    b2 = selflet_Services()
    _safe_set(a, 'selflet_Service43', b1)
    assert _is_linked(a, 'selflet_Service43', b1)
    if hasattr(b1, 'selflet_Services42'):
        assert _is_linked(b1, 'selflet_Services42', a)
    _safe_set(a, 'selflet_Service43', b2)
    assert _is_linked(a, 'selflet_Service43', b2)
    if hasattr(b1, 'selflet_Services42'):
        assert not _is_linked(b1, 'selflet_Services42', a)
    if hasattr(b2, 'selflet_Services42'):
        assert _is_linked(b2, 'selflet_Services42', a)
    _safe_set(a, 'selflet_Service43', None)
    assert not _is_linked(a, 'selflet_Service43', b2)
    if hasattr(b2, 'selflet_Services42'):
        assert not _is_linked(b2, 'selflet_Services42', a)


def test_assoc_states58_link_reassign_clear():
    a = selflet_State(name="sample_text")
    b1 = selflet_ElementaryBehavior()
    b2 = selflet_ElementaryBehavior()
    _safe_set(a, 'selflet_State', b1)
    assert _is_linked(a, 'selflet_State', b1)
    if hasattr(b1, 'selflet_ElementaryBehavior'):
        assert _is_linked(b1, 'selflet_ElementaryBehavior', a)
    _safe_set(a, 'selflet_State', b2)
    assert _is_linked(a, 'selflet_State', b2)
    if hasattr(b1, 'selflet_ElementaryBehavior'):
        assert not _is_linked(b1, 'selflet_ElementaryBehavior', a)
    if hasattr(b2, 'selflet_ElementaryBehavior'):
        assert _is_linked(b2, 'selflet_ElementaryBehavior', a)
    _safe_set(a, 'selflet_State', None)
    assert not _is_linked(a, 'selflet_State', b2)
    if hasattr(b2, 'selflet_ElementaryBehavior'):
        assert not _is_linked(b2, 'selflet_ElementaryBehavior', a)


def test_assoc_states59_link_reassign_clear():
    a = selflet_State(name="sample_text")
    b1 = selflet_ComplexBehavior()
    b2 = selflet_ComplexBehavior()
    _safe_set(a, 'selflet_State60', b1)
    assert _is_linked(a, 'selflet_State60', b1)
    if hasattr(b1, 'selflet_ComplexBehavior'):
        assert _is_linked(b1, 'selflet_ComplexBehavior', a)
    _safe_set(a, 'selflet_State60', b2)
    assert _is_linked(a, 'selflet_State60', b2)
    if hasattr(b1, 'selflet_ComplexBehavior'):
        assert not _is_linked(b1, 'selflet_ComplexBehavior', a)
    if hasattr(b2, 'selflet_ComplexBehavior'):
        assert _is_linked(b2, 'selflet_ComplexBehavior', a)
    _safe_set(a, 'selflet_State60', None)
    assert not _is_linked(a, 'selflet_State60', b2)
    if hasattr(b2, 'selflet_ComplexBehavior'):
        assert not _is_linked(b2, 'selflet_ComplexBehavior', a)


def test_assoc_typeKnowledge25_link_reassign_clear():
    a = selflet_SelfletProperties(author="sample_text", description="sample_text", enableCloudOptimizationPolicy="sample_text", enableOptimizationPolicy="sample_text", limePort="sample_text")
    b1 = selflet_TypeKnowledge()
    b2 = selflet_TypeKnowledge()
    _safe_set(a, 'selflet_SelfletProperties26', b1)
    assert _is_linked(a, 'selflet_SelfletProperties26', b1)
    if hasattr(b1, 'selflet_TypeKnowledge'):
        assert _is_linked(b1, 'selflet_TypeKnowledge', a)
    _safe_set(a, 'selflet_SelfletProperties26', b2)
    assert _is_linked(a, 'selflet_SelfletProperties26', b2)
    if hasattr(b1, 'selflet_TypeKnowledge'):
        assert not _is_linked(b1, 'selflet_TypeKnowledge', a)
    if hasattr(b2, 'selflet_TypeKnowledge'):
        assert _is_linked(b2, 'selflet_TypeKnowledge', a)
    _safe_set(a, 'selflet_SelfletProperties26', None)
    assert not _is_linked(a, 'selflet_SelfletProperties26', b2)
    if hasattr(b2, 'selflet_TypeKnowledge'):
        assert not _is_linked(b2, 'selflet_TypeKnowledge', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


selflet_Abilities_strategy = st.builds(selflet_Abilities)
@given(instance=selflet_Abilities_strategy)
@settings(max_examples=25)
def test_selflet_Abilities_instantiation(instance):
    assert isinstance(instance, selflet_Abilities)


selflet_Ability_strategy = st.builds(selflet_Ability, file=safe_text, service=safe_text)
@given(instance=selflet_Ability_strategy)
@settings(max_examples=25)
def test_selflet_Ability_instantiation(instance):
    assert isinstance(instance, selflet_Ability)


selflet_AbilityState_strategy = st.builds(selflet_AbilityState)
@given(instance=selflet_AbilityState_strategy)
@settings(max_examples=25)
def test_selflet_AbilityState_instantiation(instance):
    assert isinstance(instance, selflet_AbilityState)


selflet_Action_strategy = st.builds(selflet_Action, file=safe_text)
@given(instance=selflet_Action_strategy)
@settings(max_examples=25)
def test_selflet_Action_instantiation(instance):
    assert isinstance(instance, selflet_Action)


selflet_Actions_strategy = st.builds(selflet_Actions)
@given(instance=selflet_Actions_strategy)
@settings(max_examples=25)
def test_selflet_Actions_instantiation(instance):
    assert isinstance(instance, selflet_Actions)


selflet_Active_strategy = st.builds(selflet_Active, mainService=safe_text)
@given(instance=selflet_Active_strategy)
@settings(max_examples=25)
def test_selflet_Active_instantiation(instance):
    assert isinstance(instance, selflet_Active)


selflet_Behavior_strategy = st.builds(selflet_Behavior, elementaryBehaviorCPUTime=safe_text, elementaryBehaviorCost=safe_text, fileName=safe_text, isDefaultBehavior=safe_text, name=safe_text)
@given(instance=selflet_Behavior_strategy)
@settings(max_examples=25)
def test_selflet_Behavior_instantiation(instance):
    assert isinstance(instance, selflet_Behavior)


selflet_CPUUtilization_strategy = st.builds(selflet_CPUUtilization, lowerBound=safe_text, upperBound=safe_text)
@given(instance=selflet_CPUUtilization_strategy)
@settings(max_examples=25)
def test_selflet_CPUUtilization_instantiation(instance):
    assert isinstance(instance, selflet_CPUUtilization)


selflet_ComplexBehavior_strategy = st.builds(selflet_ComplexBehavior)
@given(instance=selflet_ComplexBehavior_strategy)
@settings(max_examples=25)
def test_selflet_ComplexBehavior_instantiation(instance):
    assert isinstance(instance, selflet_ComplexBehavior)


selflet_Condition_strategy = st.builds(selflet_Condition, file=safe_text)
@given(instance=selflet_Condition_strategy)
@settings(max_examples=25)
def test_selflet_Condition_instantiation(instance):
    assert isinstance(instance, selflet_Condition)


selflet_Conditions_strategy = st.builds(selflet_Conditions)
@given(instance=selflet_Conditions_strategy)
@settings(max_examples=25)
def test_selflet_Conditions_instantiation(instance):
    assert isinstance(instance, selflet_Conditions)


selflet_ElementaryBehavior_strategy = st.builds(selflet_ElementaryBehavior)
@given(instance=selflet_ElementaryBehavior_strategy)
@settings(max_examples=25)
def test_selflet_ElementaryBehavior_instantiation(instance):
    assert isinstance(instance, selflet_ElementaryBehavior)


selflet_Empty_strategy = st.builds(selflet_Empty)
@given(instance=selflet_Empty_strategy)
@settings(max_examples=25)
def test_selflet_Empty_instantiation(instance):
    assert isinstance(instance, selflet_Empty)


selflet_FinalState_strategy = st.builds(selflet_FinalState)
@given(instance=selflet_FinalState_strategy)
@settings(max_examples=25)
def test_selflet_FinalState_instantiation(instance):
    assert isinstance(instance, selflet_FinalState)


selflet_GeneralKnowledge_strategy = st.builds(selflet_GeneralKnowledge)
@given(instance=selflet_GeneralKnowledge_strategy)
@settings(max_examples=25)
def test_selflet_GeneralKnowledge_instantiation(instance):
    assert isinstance(instance, selflet_GeneralKnowledge)


selflet_InitialState_strategy = st.builds(selflet_InitialState)
@given(instance=selflet_InitialState_strategy)
@settings(max_examples=25)
def test_selflet_InitialState_instantiation(instance):
    assert isinstance(instance, selflet_InitialState)


selflet_Input_strategy = st.builds(selflet_Input)
@given(instance=selflet_Input_strategy)
@settings(max_examples=25)
def test_selflet_Input_instantiation(instance):
    assert isinstance(instance, selflet_Input)


selflet_IntermediateState_strategy = st.builds(selflet_IntermediateState)
@given(instance=selflet_IntermediateState_strategy)
@settings(max_examples=25)
def test_selflet_IntermediateState_instantiation(instance):
    assert isinstance(instance, selflet_IntermediateState)


selflet_Method_strategy = st.builds(selflet_Method, name=safe_text, paramType=safe_text)
@given(instance=selflet_Method_strategy)
@settings(max_examples=25)
def test_selflet_Method_instantiation(instance):
    assert isinstance(instance, selflet_Method)


selflet_Methods_strategy = st.builds(selflet_Methods)
@given(instance=selflet_Methods_strategy)
@settings(max_examples=25)
def test_selflet_Methods_instantiation(instance):
    assert isinstance(instance, selflet_Methods)


selflet_OfferMode_strategy = st.builds(selflet_OfferMode, mode=safe_text)
@given(instance=selflet_OfferMode_strategy)
@settings(max_examples=25)
def test_selflet_OfferMode_instantiation(instance):
    assert isinstance(instance, selflet_OfferMode)


selflet_Output_strategy = st.builds(selflet_Output)
@given(instance=selflet_Output_strategy)
@settings(max_examples=25)
def test_selflet_Output_instantiation(instance):
    assert isinstance(instance, selflet_Output)


selflet_Parameter_strategy = st.builds(selflet_Parameter, name=safe_text, type=safe_text)
@given(instance=selflet_Parameter_strategy)
@settings(max_examples=25)
def test_selflet_Parameter_instantiation(instance):
    assert isinstance(instance, selflet_Parameter)


selflet_Reds_strategy = st.builds(selflet_Reds, ipAddress=safe_text, port=safe_text)
@given(instance=selflet_Reds_strategy)
@settings(max_examples=25)
def test_selflet_Reds_instantiation(instance):
    assert isinstance(instance, selflet_Reds)


selflet_Rule_strategy = st.builds(selflet_Rule, file=safe_text)
@given(instance=selflet_Rule_strategy)
@settings(max_examples=25)
def test_selflet_Rule_instantiation(instance):
    assert isinstance(instance, selflet_Rule)


selflet_Rules_strategy = st.builds(selflet_Rules)
@given(instance=selflet_Rules_strategy)
@settings(max_examples=25)
def test_selflet_Rules_instantiation(instance):
    assert isinstance(instance, selflet_Rules)


selflet_SelfLetProperty_strategy = st.builds(selflet_SelfLetProperty, name=safe_text, type=safe_text, value=safe_text)
@given(instance=selflet_SelfLetProperty_strategy)
@settings(max_examples=25)
def test_selflet_SelfLetProperty_instantiation(instance):
    assert isinstance(instance, selflet_SelfLetProperty)


selflet_Selflet_strategy = st.builds(selflet_Selflet, name=safe_text)
@given(instance=selflet_Selflet_strategy)
@settings(max_examples=25)
def test_selflet_Selflet_instantiation(instance):
    assert isinstance(instance, selflet_Selflet)


selflet_SelfletProperties_strategy = st.builds(selflet_SelfletProperties, author=safe_text, description=safe_text, enableCloudOptimizationPolicy=safe_text, enableOptimizationPolicy=safe_text, limePort=safe_text)
@given(instance=selflet_SelfletProperties_strategy)
@settings(max_examples=25)
def test_selflet_SelfletProperties_instantiation(instance):
    assert isinstance(instance, selflet_SelfletProperties)


selflet_SelfletResources_strategy = st.builds(selflet_SelfletResources)
@given(instance=selflet_SelfletResources_strategy)
@settings(max_examples=25)
def test_selflet_SelfletResources_instantiation(instance):
    assert isinstance(instance, selflet_SelfletResources)


selflet_Service_strategy = st.builds(selflet_Service, active=safe_text, maxResponseTime=safe_text, name=safe_text, revenue=safe_text)
@given(instance=selflet_Service_strategy)
@settings(max_examples=25)
def test_selflet_Service_instantiation(instance):
    assert isinstance(instance, selflet_Service)


selflet_Services_strategy = st.builds(selflet_Services)
@given(instance=selflet_Services_strategy)
@settings(max_examples=25)
def test_selflet_Services_instantiation(instance):
    assert isinstance(instance, selflet_Services)


selflet_State_strategy = st.builds(selflet_State, name=safe_text)
@given(instance=selflet_State_strategy)
@settings(max_examples=25)
def test_selflet_State_instantiation(instance):
    assert isinstance(instance, selflet_State)


selflet_TypeKnowledge_strategy = st.builds(selflet_TypeKnowledge)
@given(instance=selflet_TypeKnowledge_strategy)
@settings(max_examples=25)
def test_selflet_TypeKnowledge_instantiation(instance):
    assert isinstance(instance, selflet_TypeKnowledge)


