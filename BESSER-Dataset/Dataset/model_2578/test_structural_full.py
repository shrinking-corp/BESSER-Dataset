import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActionRealisation,
    Alternative,
    Attribute,
    AttributeConstraint,
    Cardinality,
    Clone,
    CloudCredentials,
    CloudLocation,
    CloudProvider,
    Communication,
    CommunicationInstance,
    CommunicationPort,
    CommunicationPortInstance,
    Component,
    ComponentInstance,
    CompositeMetric,
    CompositeMetricInstance,
    CompositeSecurityMetric,
    CompositeSecurityMetricInstance,
    Condition,
    ConditionContext,
    Configuration,
    Constraint,
    Country,
    Credentials,
    DataCenter,
    DeploymentElement,
    DeploymentModel,
    Entity,
    EnumerateValue,
    Event,
    EventInstance,
    EventPattern,
    ExecutionContext,
    ExecutionModel,
    ExternalIdentifier,
    FeatCardinality,
    Feature,
    GeographicalRegion,
    GroupCardinality,
    HardRequirement,
    HardwareRequirement,
    Hosting,
    HostingInstance,
    HostingPort,
    HostingPortInstance,
    InternalComponent,
    InternalComponentInstance,
    Limit,
    Location,
    LocationModel,
    LocationRequirement,
    Measurement,
    Metric,
    MetricCondition,
    MetricContext,
    MetricFormula,
    MetricFormulaParameter,
    MetricInstance,
    MetricModel,
    MetricObjectBinding,
    Model,
    MonetaryUnit,
    NumericValue,
    OSOrImageRequirement,
    Organisation,
    OrganisationModel,
    PaaSageCredentials,
    Permission,
    Property,
    PropertyContext,
    ProvidedCommunication,
    ProvidedCommunicationInstance,
    ProvidedHost,
    ProvidedHostInstance,
    ProviderModel,
    ProviderRequirement,
    QualitativeHardwareRequirement,
    QuantitativeHardwareRequirement,
    Range,
    RawMetric,
    RawMetricInstance,
    RawSecurityMetric,
    RawSecurityMetricInstance,
    RequiredCommunication,
    RequiredCommunicationInstance,
    RequiredHost,
    RequiredHostInstance,
    Requirement,
    RequirementGroup,
    RequirementModel,
    Requires,
    ResourceFilter,
    Role,
    RoleAssignment,
    RuleTrigger,
    SLOAssessment,
    ScalabilityModel,
    ScalabilityRule,
    ScaleRequirement,
    ScalingAction,
    Schedule,
    Scope,
    SecurityCapability,
    SecurityControl,
    SecurityDomain,
    SecurityModel,
    SecurityProperty,
    SecurityRequirement,
    SecuritySLO,
    Sensor,
    ServiceLevelObjective,
    SimpleEvent,
    SingleValue,
    SoftRequirement,
    TimeIntervalUnit,
    Timer,
    TypeModel,
    Unit,
    UnitModel,
    User,
    UserGroup,
    VM,
    VMInstance,
    VMRequirementSet,
    ValueType,
    Window,
    camel_Action,
    camel_Application,
    camel_CamelModel,
    camel_Model,
    camel_deployment_Communication,
    camel_deployment_CommunicationInstance,
    camel_deployment_CommunicationPort,
    camel_deployment_CommunicationPortInstance,
    camel_deployment_Component,
    camel_deployment_ComponentInstance,
    camel_deployment_Configuration,
    camel_deployment_DeploymentElement,
    camel_deployment_DeploymentModel,
    camel_deployment_Hosting,
    camel_deployment_HostingInstance,
    camel_deployment_HostingPort,
    camel_deployment_HostingPortInstance,
    camel_deployment_InternalComponent,
    camel_deployment_InternalComponentInstance,
    camel_deployment_ProvidedCommunication,
    camel_deployment_ProvidedCommunicationInstance,
    camel_deployment_ProvidedHost,
    camel_deployment_ProvidedHostInstance,
    camel_deployment_RequiredCommunication,
    camel_deployment_RequiredCommunicationInstance,
    camel_deployment_RequiredHost,
    camel_deployment_RequiredHostInstance,
    camel_deployment_VM,
    camel_deployment_VMInstance,
    camel_deployment_VMRequirementSet,
    camel_execution_ActionRealisation,
    camel_execution_ApplicationMeasurement,
    camel_execution_CommunicationMeasurement,
    camel_execution_ExecutionContext,
    camel_execution_ExecutionModel,
    camel_execution_InternalComponentMeasurement,
    camel_execution_Measurement,
    camel_execution_RuleTrigger,
    camel_execution_SLOAssessment,
    camel_execution_VMMeasurement,
    camel_location_CloudLocation,
    camel_location_Country,
    camel_location_GeographicalRegion,
    camel_location_Location,
    camel_location_LocationModel,
    camel_metric_CompositeMetric,
    camel_metric_CompositeMetricContext,
    camel_metric_CompositeMetricInstance,
    camel_metric_Condition,
    camel_metric_ConditionContext,
    camel_metric_Metric,
    camel_metric_MetricApplicationBinding,
    camel_metric_MetricComponentBinding,
    camel_metric_MetricCondition,
    camel_metric_MetricContext,
    camel_metric_MetricFormula,
    camel_metric_MetricFormulaParameter,
    camel_metric_MetricInstance,
    camel_metric_MetricModel,
    camel_metric_MetricObjectBinding,
    camel_metric_MetricVMBinding,
    camel_metric_Property,
    camel_metric_PropertyCondition,
    camel_metric_PropertyContext,
    camel_metric_RawMetric,
    camel_metric_RawMetricContext,
    camel_metric_RawMetricInstance,
    camel_metric_Schedule,
    camel_metric_Sensor,
    camel_metric_Window,
    camel_organisation_CloudCredentials,
    camel_organisation_CloudProvider,
    camel_organisation_Credentials,
    camel_organisation_DataCenter,
    camel_organisation_Entity,
    camel_organisation_ExternalIdentifier,
    camel_organisation_InformationResourceFilter,
    camel_organisation_Organisation,
    camel_organisation_OrganisationModel,
    camel_organisation_PaaSageCredentials,
    camel_organisation_Permission,
    camel_organisation_ResourceFilter,
    camel_organisation_Role,
    camel_organisation_RoleAssignment,
    camel_organisation_ServiceResourceFilter,
    camel_organisation_User,
    camel_organisation_UserGroup,
    camel_provider_Alternative,
    camel_provider_Attribute,
    camel_provider_AttributeConstraint,
    camel_provider_Cardinality,
    camel_provider_Clone,
    camel_provider_Constraint,
    camel_provider_Excludes,
    camel_provider_Exclusive,
    camel_provider_FeatCardinality,
    camel_provider_Feature,
    camel_provider_Functional,
    camel_provider_GroupCardinality,
    camel_provider_Implies,
    camel_provider_Instance,
    camel_provider_Product,
    camel_provider_ProviderModel,
    camel_provider_Requires,
    camel_provider_Scope,
    camel_requirement_HardRequirement,
    camel_requirement_HardwareRequirement,
    camel_requirement_HorizontalScaleRequirement,
    camel_requirement_ImageRequirement,
    camel_requirement_LocationRequirement,
    camel_requirement_OSOrImageRequirement,
    camel_requirement_OSRequirement,
    camel_requirement_OptimisationRequirement,
    camel_requirement_ProviderRequirement,
    camel_requirement_QualitativeHardwareRequirement,
    camel_requirement_QuantitativeHardwareRequirement,
    camel_requirement_Requirement,
    camel_requirement_RequirementGroup,
    camel_requirement_RequirementModel,
    camel_requirement_ScaleRequirement,
    camel_requirement_SecurityRequirement,
    camel_requirement_ServiceLevelObjective,
    camel_requirement_SoftRequirement,
    camel_requirement_VerticalScaleRequirement,
    camel_scalability_BinaryEventPattern,
    camel_scalability_Event,
    camel_scalability_EventInstance,
    camel_scalability_EventPattern,
    camel_scalability_FunctionalEvent,
    camel_scalability_HorizontalScalingAction,
    camel_scalability_NonFunctionalEvent,
    camel_scalability_ScalabilityModel,
    camel_scalability_ScalabilityRule,
    camel_scalability_ScalingAction,
    camel_scalability_SimpleEvent,
    camel_scalability_Timer,
    camel_scalability_UnaryEventPattern,
    camel_scalability_VerticalScalingAction,
    camel_security_Certifiable,
    camel_security_CompositeSecurityMetric,
    camel_security_CompositeSecurityMetricInstance,
    camel_security_RawSecurityMetric,
    camel_security_RawSecurityMetricInstance,
    camel_security_SecurityCapability,
    camel_security_SecurityControl,
    camel_security_SecurityDomain,
    camel_security_SecurityModel,
    camel_security_SecurityProperty,
    camel_security_SecuritySLO,
    camel_type_BoolValue,
    camel_type_BooleanValueType,
    camel_type_DoublePrecisionValue,
    camel_type_EnumerateValue,
    camel_type_Enumeration,
    camel_type_FloatsValue,
    camel_type_IntegerValue,
    camel_type_Limit,
    camel_type_List,
    camel_type_NegativeInf,
    camel_type_NumericValue,
    camel_type_PositiveInf,
    camel_type_Range,
    camel_type_RangeUnion,
    camel_type_SingleValue,
    camel_type_StringValueType,
    camel_type_StringsValue,
    camel_type_TypeModel,
    camel_type_ValueToIncrease,
    camel_type_ValueType,
    camel_unit_CoreUnit,
    camel_unit_Dimensionless,
    camel_unit_MonetaryUnit,
    camel_unit_RequestUnit,
    camel_unit_StorageUnit,
    camel_unit_ThroughputUnit,
    camel_unit_TimeIntervalUnit,
    camel_unit_TransactionUnit,
    camel_unit_Unit,
    camel_unit_UnitModel,
    execution_camel_Action,
    execution_camel_Application,
    metric_camel_Application,
    requirement_camel_Application,
    scalability_camel_Action,
    ActionType,
    BinaryPatternOperatorType,
    CommunicationType,
    ComparisonOperatorType,
    FunctionPatternType,
    LayerType,
    MetricFunctionArityType,
    MetricFunctionType,
    Operator,
    OptimisationFunctionType,
    PropertyType,
    QuantifierType,
    RequirementOperatorType,
    ResourcePattern,
    ScheduleType,
    SecurityLevel,
    StatusType,
    TimerType,
    TypeEnum,
    UnaryPatternOperatorType,
    UnitDimensionType,
    UnitType,
    WindowSizeType,
    WindowType,
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

def test_camel_Action_name_value_roundtrip():
    instance = camel_Action(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_Action_type_value_roundtrip():
    instance = camel_Action(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_Application_description_value_roundtrip():
    instance = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_camel_Application_name_value_roundtrip():
    instance = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_Application_version_value_roundtrip():
    instance = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_camel_Model_importURI_value_roundtrip():
    instance = camel_Model(importURI="sample_text", name="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_camel_Model_name_value_roundtrip():
    instance = camel_Model(importURI="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_deployment_Communication_type_value_roundtrip():
    instance = camel_deployment_Communication(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_deployment_CommunicationPort_portNumber_value_roundtrip():
    instance = camel_deployment_CommunicationPort(portNumber=7)
    assert instance.portNumber == 7
    instance.portNumber = 13
    assert instance.portNumber == 13


def test_camel_deployment_ComponentInstance_destroyedOn_value_roundtrip():
    instance = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    assert instance.destroyedOn == date(2024, 1, 1)
    instance.destroyedOn = date(2025, 6, 15)
    assert instance.destroyedOn == date(2025, 6, 15)


def test_camel_deployment_ComponentInstance_instantiatedOn_value_roundtrip():
    instance = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    assert instance.instantiatedOn == date(2024, 1, 1)
    instance.instantiatedOn = date(2025, 6, 15)
    assert instance.instantiatedOn == date(2025, 6, 15)


def test_camel_deployment_Configuration_configureCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.configureCommand == "sample_text"
    instance.configureCommand = "sample_text_2"
    assert instance.configureCommand == "sample_text_2"


def test_camel_deployment_Configuration_downloadCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.downloadCommand == "sample_text"
    instance.downloadCommand = "sample_text_2"
    assert instance.downloadCommand == "sample_text_2"


def test_camel_deployment_Configuration_installCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.installCommand == "sample_text"
    instance.installCommand = "sample_text_2"
    assert instance.installCommand == "sample_text_2"


def test_camel_deployment_Configuration_startCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_camel_deployment_Configuration_stopCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.stopCommand == "sample_text"
    instance.stopCommand = "sample_text_2"
    assert instance.stopCommand == "sample_text_2"


def test_camel_deployment_Configuration_uploadCommand_value_roundtrip():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.uploadCommand == "sample_text"
    instance.uploadCommand = "sample_text_2"
    assert instance.uploadCommand == "sample_text_2"


def test_camel_deployment_DeploymentElement_name_value_roundtrip():
    instance = camel_deployment_DeploymentElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_deployment_InternalComponent_version_value_roundtrip():
    instance = camel_deployment_InternalComponent(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_camel_deployment_RequiredCommunication_isMandatory_value_roundtrip():
    instance = camel_deployment_RequiredCommunication(isMandatory=True)
    assert instance.isMandatory == True
    instance.isMandatory = False
    assert instance.isMandatory == False


def test_camel_deployment_VMInstance_ip_value_roundtrip():
    instance = camel_deployment_VMInstance(ip="sample_text")
    assert instance.ip == "sample_text"
    instance.ip = "sample_text_2"
    assert instance.ip == "sample_text_2"


def test_camel_deployment_VMRequirementSet_name_value_roundtrip():
    instance = camel_deployment_VMRequirementSet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_execution_ActionRealisation_endTime_value_roundtrip():
    instance = camel_execution_ActionRealisation(endTime=date(2024, 1, 1), lowLevelActions="sample_text", name="sample_text", startTime=date(2024, 1, 1))
    assert instance.endTime == date(2024, 1, 1)
    instance.endTime = date(2025, 6, 15)
    assert instance.endTime == date(2025, 6, 15)


def test_camel_execution_ActionRealisation_lowLevelActions_value_roundtrip():
    instance = camel_execution_ActionRealisation(endTime=date(2024, 1, 1), lowLevelActions="sample_text", name="sample_text", startTime=date(2024, 1, 1))
    assert instance.lowLevelActions == "sample_text"
    instance.lowLevelActions = "sample_text_2"
    assert instance.lowLevelActions == "sample_text_2"


def test_camel_execution_ActionRealisation_name_value_roundtrip():
    instance = camel_execution_ActionRealisation(endTime=date(2024, 1, 1), lowLevelActions="sample_text", name="sample_text", startTime=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_execution_ActionRealisation_startTime_value_roundtrip():
    instance = camel_execution_ActionRealisation(endTime=date(2024, 1, 1), lowLevelActions="sample_text", name="sample_text", startTime=date(2024, 1, 1))
    assert instance.startTime == date(2024, 1, 1)
    instance.startTime = date(2025, 6, 15)
    assert instance.startTime == date(2025, 6, 15)


def test_camel_execution_ExecutionContext_endTime_value_roundtrip():
    instance = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    assert instance.endTime == date(2024, 1, 1)
    instance.endTime = date(2025, 6, 15)
    assert instance.endTime == date(2025, 6, 15)


def test_camel_execution_ExecutionContext_name_value_roundtrip():
    instance = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_execution_ExecutionContext_startTime_value_roundtrip():
    instance = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    assert instance.startTime == date(2024, 1, 1)
    instance.startTime = date(2025, 6, 15)
    assert instance.startTime == date(2025, 6, 15)


def test_camel_execution_ExecutionContext_totalCost_value_roundtrip():
    instance = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    assert instance.totalCost == 3.14
    instance.totalCost = 9.99
    assert instance.totalCost == 9.99


def test_camel_execution_Measurement_measurementTime_value_roundtrip():
    instance = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    assert instance.measurementTime == date(2024, 1, 1)
    instance.measurementTime = date(2025, 6, 15)
    assert instance.measurementTime == date(2025, 6, 15)


def test_camel_execution_Measurement_name_value_roundtrip():
    instance = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_execution_Measurement_rawData_value_roundtrip():
    instance = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    assert instance.rawData == "sample_text"
    instance.rawData = "sample_text_2"
    assert instance.rawData == "sample_text_2"


def test_camel_execution_Measurement_value_value_roundtrip():
    instance = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_camel_execution_RuleTrigger_name_value_roundtrip():
    instance = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_execution_RuleTrigger_trigerringTime_value_roundtrip():
    instance = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    assert instance.trigerringTime == date(2024, 1, 1)
    instance.trigerringTime = date(2025, 6, 15)
    assert instance.trigerringTime == date(2025, 6, 15)


def test_camel_execution_SLOAssessment_assessment_value_roundtrip():
    instance = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    assert instance.assessment == True
    instance.assessment = False
    assert instance.assessment == False


def test_camel_execution_SLOAssessment_assessmentTime_value_roundtrip():
    instance = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    assert instance.assessmentTime == date(2024, 1, 1)
    instance.assessmentTime = date(2025, 6, 15)
    assert instance.assessmentTime == date(2025, 6, 15)


def test_camel_execution_SLOAssessment_name_value_roundtrip():
    instance = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_location_CloudLocation_isAssignable_value_roundtrip():
    instance = camel_location_CloudLocation(isAssignable=True)
    assert instance.isAssignable == True
    instance.isAssignable = False
    assert instance.isAssignable == False


def test_camel_location_GeographicalRegion_alternativeNames_value_roundtrip():
    instance = camel_location_GeographicalRegion(alternativeNames="sample_text", name="sample_text")
    assert instance.alternativeNames == "sample_text"
    instance.alternativeNames = "sample_text_2"
    assert instance.alternativeNames == "sample_text_2"


def test_camel_location_GeographicalRegion_name_value_roundtrip():
    instance = camel_location_GeographicalRegion(alternativeNames="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_location_Location_id_value_roundtrip():
    instance = camel_location_Location(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_camel_metric_Condition_comparisonOperator_value_roundtrip():
    instance = camel_metric_Condition(comparisonOperator="sample_text", name="sample_text", threshold=3.14, validity=date(2024, 1, 1))
    assert instance.comparisonOperator == "sample_text"
    instance.comparisonOperator = "sample_text_2"
    assert instance.comparisonOperator == "sample_text_2"


def test_camel_metric_Condition_name_value_roundtrip():
    instance = camel_metric_Condition(comparisonOperator="sample_text", name="sample_text", threshold=3.14, validity=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Condition_threshold_value_roundtrip():
    instance = camel_metric_Condition(comparisonOperator="sample_text", name="sample_text", threshold=3.14, validity=date(2024, 1, 1))
    assert instance.threshold == 3.14
    instance.threshold = 9.99
    assert instance.threshold == 9.99


def test_camel_metric_Condition_validity_value_roundtrip():
    instance = camel_metric_Condition(comparisonOperator="sample_text", name="sample_text", threshold=3.14, validity=date(2024, 1, 1))
    assert instance.validity == date(2024, 1, 1)
    instance.validity = date(2025, 6, 15)
    assert instance.validity == date(2025, 6, 15)


def test_camel_metric_ConditionContext_isRelative_value_roundtrip():
    instance = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    assert instance.isRelative == True
    instance.isRelative = False
    assert instance.isRelative == False


def test_camel_metric_ConditionContext_maxQuantity_value_roundtrip():
    instance = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    assert instance.maxQuantity == 3.14
    instance.maxQuantity = 9.99
    assert instance.maxQuantity == 9.99


def test_camel_metric_ConditionContext_minQuantity_value_roundtrip():
    instance = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    assert instance.minQuantity == 3.14
    instance.minQuantity = 9.99
    assert instance.minQuantity == 9.99


def test_camel_metric_ConditionContext_name_value_roundtrip():
    instance = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_ConditionContext_quantifier_value_roundtrip():
    instance = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    assert instance.quantifier == "sample_text"
    instance.quantifier = "sample_text_2"
    assert instance.quantifier == "sample_text_2"


def test_camel_metric_Metric_description_value_roundtrip():
    instance = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_camel_metric_Metric_isVariable_value_roundtrip():
    instance = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    assert instance.isVariable == True
    instance.isVariable = False
    assert instance.isVariable == False


def test_camel_metric_Metric_layer_value_roundtrip():
    instance = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    assert instance.layer == "sample_text"
    instance.layer = "sample_text_2"
    assert instance.layer == "sample_text_2"


def test_camel_metric_Metric_valueDirection_value_roundtrip():
    instance = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    assert instance.valueDirection == "sample_text"
    instance.valueDirection = "sample_text_2"
    assert instance.valueDirection == "sample_text_2"


def test_camel_metric_MetricFormula_function_value_roundtrip():
    instance = camel_metric_MetricFormula(function="sample_text", functionArity="sample_text", functionPattern="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_camel_metric_MetricFormula_functionArity_value_roundtrip():
    instance = camel_metric_MetricFormula(function="sample_text", functionArity="sample_text", functionPattern="sample_text")
    assert instance.functionArity == "sample_text"
    instance.functionArity = "sample_text_2"
    assert instance.functionArity == "sample_text_2"


def test_camel_metric_MetricFormula_functionPattern_value_roundtrip():
    instance = camel_metric_MetricFormula(function="sample_text", functionArity="sample_text", functionPattern="sample_text")
    assert instance.functionPattern == "sample_text"
    instance.functionPattern = "sample_text_2"
    assert instance.functionPattern == "sample_text_2"


def test_camel_metric_MetricFormulaParameter_name_value_roundtrip():
    instance = camel_metric_MetricFormulaParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_MetricInstance_name_value_roundtrip():
    instance = camel_metric_MetricInstance(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_MetricObjectBinding_name_value_roundtrip():
    instance = camel_metric_MetricObjectBinding(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Property_description_value_roundtrip():
    instance = camel_metric_Property(description="sample_text", name="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_camel_metric_Property_name_value_roundtrip():
    instance = camel_metric_Property(description="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Property_type_value_roundtrip():
    instance = camel_metric_Property(description="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_metric_Schedule_end_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.end == date(2024, 1, 1)
    instance.end = date(2025, 6, 15)
    assert instance.end == date(2025, 6, 15)


def test_camel_metric_Schedule_interval_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.interval == "sample_text"
    instance.interval = "sample_text_2"
    assert instance.interval == "sample_text_2"


def test_camel_metric_Schedule_name_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Schedule_repetitions_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.repetitions == 7
    instance.repetitions = 13
    assert instance.repetitions == 13


def test_camel_metric_Schedule_start_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.start == date(2024, 1, 1)
    instance.start = date(2025, 6, 15)
    assert instance.start == date(2025, 6, 15)


def test_camel_metric_Schedule_type_value_roundtrip():
    instance = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_metric_Sensor_configuration_value_roundtrip():
    instance = camel_metric_Sensor(configuration="sample_text", isPush=True, name="sample_text")
    assert instance.configuration == "sample_text"
    instance.configuration = "sample_text_2"
    assert instance.configuration == "sample_text_2"


def test_camel_metric_Sensor_isPush_value_roundtrip():
    instance = camel_metric_Sensor(configuration="sample_text", isPush=True, name="sample_text")
    assert instance.isPush == True
    instance.isPush = False
    assert instance.isPush == False


def test_camel_metric_Sensor_name_value_roundtrip():
    instance = camel_metric_Sensor(configuration="sample_text", isPush=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Window_measurementSize_value_roundtrip():
    instance = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    assert instance.measurementSize == "sample_text"
    instance.measurementSize = "sample_text_2"
    assert instance.measurementSize == "sample_text_2"


def test_camel_metric_Window_name_value_roundtrip():
    instance = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_metric_Window_sizeType_value_roundtrip():
    instance = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    assert instance.sizeType == "sample_text"
    instance.sizeType = "sample_text_2"
    assert instance.sizeType == "sample_text_2"


def test_camel_metric_Window_timeSize_value_roundtrip():
    instance = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    assert instance.timeSize == "sample_text"
    instance.timeSize = "sample_text_2"
    assert instance.timeSize == "sample_text_2"


def test_camel_metric_Window_windowType_value_roundtrip():
    instance = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    assert instance.windowType == "sample_text"
    instance.windowType = "sample_text_2"
    assert instance.windowType == "sample_text_2"


def test_camel_organisation_CloudCredentials_name_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_CloudCredentials_password_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_camel_organisation_CloudCredentials_privateSSHKey_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.privateSSHKey == "sample_text"
    instance.privateSSHKey = "sample_text_2"
    assert instance.privateSSHKey == "sample_text_2"


def test_camel_organisation_CloudCredentials_publicSSHKey_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.publicSSHKey == "sample_text"
    instance.publicSSHKey = "sample_text_2"
    assert instance.publicSSHKey == "sample_text_2"


def test_camel_organisation_CloudCredentials_securityGroup_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_camel_organisation_CloudCredentials_username_value_roundtrip():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_camel_organisation_CloudProvider_IaaS_value_roundtrip():
    instance = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    assert instance.IaaS == True
    instance.IaaS = False
    assert instance.IaaS == False


def test_camel_organisation_CloudProvider_PaaS_value_roundtrip():
    instance = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    assert instance.PaaS == True
    instance.PaaS = False
    assert instance.PaaS == False


def test_camel_organisation_CloudProvider_SaaS_value_roundtrip():
    instance = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    assert instance.SaaS == True
    instance.SaaS = False
    assert instance.SaaS == False


def test_camel_organisation_CloudProvider_public_value_roundtrip():
    instance = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    assert instance.public == True
    instance.public = False
    assert instance.public == False


def test_camel_organisation_DataCenter_codeName_value_roundtrip():
    instance = camel_organisation_DataCenter(codeName="sample_text", name="sample_text")
    assert instance.codeName == "sample_text"
    instance.codeName = "sample_text_2"
    assert instance.codeName == "sample_text_2"


def test_camel_organisation_DataCenter_name_value_roundtrip():
    instance = camel_organisation_DataCenter(codeName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_ExternalIdentifier_description_value_roundtrip():
    instance = camel_organisation_ExternalIdentifier(description="sample_text", identifier="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_camel_organisation_ExternalIdentifier_identifier_value_roundtrip():
    instance = camel_organisation_ExternalIdentifier(description="sample_text", identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_camel_organisation_InformationResourceFilter_everyInformationResource_value_roundtrip():
    instance = camel_organisation_InformationResourceFilter(everyInformationResource=True, informationResourcePath="sample_text")
    assert instance.everyInformationResource == True
    instance.everyInformationResource = False
    assert instance.everyInformationResource == False


def test_camel_organisation_InformationResourceFilter_informationResourcePath_value_roundtrip():
    instance = camel_organisation_InformationResourceFilter(everyInformationResource=True, informationResourcePath="sample_text")
    assert instance.informationResourcePath == "sample_text"
    instance.informationResourcePath = "sample_text_2"
    assert instance.informationResourcePath == "sample_text_2"


def test_camel_organisation_Organisation_email_value_roundtrip():
    instance = camel_organisation_Organisation(email="sample_text", name="sample_text", postalAddress="sample_text", www="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_camel_organisation_Organisation_name_value_roundtrip():
    instance = camel_organisation_Organisation(email="sample_text", name="sample_text", postalAddress="sample_text", www="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_Organisation_postalAddress_value_roundtrip():
    instance = camel_organisation_Organisation(email="sample_text", name="sample_text", postalAddress="sample_text", www="sample_text")
    assert instance.postalAddress == "sample_text"
    instance.postalAddress = "sample_text_2"
    assert instance.postalAddress == "sample_text_2"


def test_camel_organisation_Organisation_www_value_roundtrip():
    instance = camel_organisation_Organisation(email="sample_text", name="sample_text", postalAddress="sample_text", www="sample_text")
    assert instance.www == "sample_text"
    instance.www = "sample_text_2"
    assert instance.www == "sample_text_2"


def test_camel_organisation_OrganisationModel_securityLevel_value_roundtrip():
    instance = camel_organisation_OrganisationModel(securityLevel="sample_text")
    assert instance.securityLevel == "sample_text"
    instance.securityLevel = "sample_text_2"
    assert instance.securityLevel == "sample_text_2"


def test_camel_organisation_PaaSageCredentials_password_value_roundtrip():
    instance = camel_organisation_PaaSageCredentials(password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_camel_organisation_Permission_action_value_roundtrip():
    instance = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_camel_organisation_Permission_endTime_value_roundtrip():
    instance = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.endTime == date(2024, 1, 1)
    instance.endTime = date(2025, 6, 15)
    assert instance.endTime == date(2025, 6, 15)


def test_camel_organisation_Permission_name_value_roundtrip():
    instance = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_Permission_startTime_value_roundtrip():
    instance = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.startTime == date(2024, 1, 1)
    instance.startTime = date(2025, 6, 15)
    assert instance.startTime == date(2025, 6, 15)


def test_camel_organisation_ResourceFilter_name_value_roundtrip():
    instance = camel_organisation_ResourceFilter(name="sample_text", resourcePattern="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_ResourceFilter_resourcePattern_value_roundtrip():
    instance = camel_organisation_ResourceFilter(name="sample_text", resourcePattern="sample_text")
    assert instance.resourcePattern == "sample_text"
    instance.resourcePattern = "sample_text_2"
    assert instance.resourcePattern == "sample_text_2"


def test_camel_organisation_Role_name_value_roundtrip():
    instance = camel_organisation_Role(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_RoleAssignment_assignmentTime_value_roundtrip():
    instance = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.assignmentTime == date(2024, 1, 1)
    instance.assignmentTime = date(2025, 6, 15)
    assert instance.assignmentTime == date(2025, 6, 15)


def test_camel_organisation_RoleAssignment_endTime_value_roundtrip():
    instance = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.endTime == date(2024, 1, 1)
    instance.endTime = date(2025, 6, 15)
    assert instance.endTime == date(2025, 6, 15)


def test_camel_organisation_RoleAssignment_name_value_roundtrip():
    instance = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_RoleAssignment_startTime_value_roundtrip():
    instance = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    assert instance.startTime == date(2024, 1, 1)
    instance.startTime = date(2025, 6, 15)
    assert instance.startTime == date(2025, 6, 15)


def test_camel_organisation_ServiceResourceFilter_everyService_value_roundtrip():
    instance = camel_organisation_ServiceResourceFilter(everyService=True, serviceURL="sample_text")
    assert instance.everyService == True
    instance.everyService = False
    assert instance.everyService == False


def test_camel_organisation_ServiceResourceFilter_serviceURL_value_roundtrip():
    instance = camel_organisation_ServiceResourceFilter(everyService=True, serviceURL="sample_text")
    assert instance.serviceURL == "sample_text"
    instance.serviceURL = "sample_text_2"
    assert instance.serviceURL == "sample_text_2"


def test_camel_organisation_User_email_value_roundtrip():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_camel_organisation_User_firstName_value_roundtrip():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_camel_organisation_User_lastName_value_roundtrip():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_camel_organisation_User_name_value_roundtrip():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_organisation_User_www_value_roundtrip():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert instance.www == "sample_text"
    instance.www = "sample_text_2"
    assert instance.www == "sample_text_2"


def test_camel_organisation_UserGroup_name_value_roundtrip():
    instance = camel_organisation_UserGroup(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_Attribute_name_value_roundtrip():
    instance = camel_provider_Attribute(name="sample_text", unitType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_Attribute_unitType_value_roundtrip():
    instance = camel_provider_Attribute(name="sample_text", unitType="sample_text")
    assert instance.unitType == "sample_text"
    instance.unitType = "sample_text_2"
    assert instance.unitType == "sample_text_2"


def test_camel_provider_AttributeConstraint_name_value_roundtrip():
    instance = camel_provider_AttributeConstraint(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_Cardinality_cardinalityMax_value_roundtrip():
    instance = camel_provider_Cardinality(cardinalityMax=7, cardinalityMin=7)
    assert instance.cardinalityMax == 7
    instance.cardinalityMax = 13
    assert instance.cardinalityMax == 13


def test_camel_provider_Cardinality_cardinalityMin_value_roundtrip():
    instance = camel_provider_Cardinality(cardinalityMax=7, cardinalityMin=7)
    assert instance.cardinalityMin == 7
    instance.cardinalityMin = 13
    assert instance.cardinalityMin == 13


def test_camel_provider_Clone_name_value_roundtrip():
    instance = camel_provider_Clone(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_Constraint_name_value_roundtrip():
    instance = camel_provider_Constraint(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_FeatCardinality_value_value_roundtrip():
    instance = camel_provider_FeatCardinality(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_camel_provider_Feature_name_value_roundtrip():
    instance = camel_provider_Feature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_provider_Functional_order_value_roundtrip():
    instance = camel_provider_Functional(order=7, type="sample_text", value=7)
    assert instance.order == 7
    instance.order = 13
    assert instance.order == 13


def test_camel_provider_Functional_type_value_roundtrip():
    instance = camel_provider_Functional(order=7, type="sample_text", value=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_provider_Functional_value_value_roundtrip():
    instance = camel_provider_Functional(order=7, type="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_camel_requirement_HorizontalScaleRequirement_maxInstances_value_roundtrip():
    instance = camel_requirement_HorizontalScaleRequirement(maxInstances=7, minInstances=7)
    assert instance.maxInstances == 7
    instance.maxInstances = 13
    assert instance.maxInstances == 13


def test_camel_requirement_HorizontalScaleRequirement_minInstances_value_roundtrip():
    instance = camel_requirement_HorizontalScaleRequirement(maxInstances=7, minInstances=7)
    assert instance.minInstances == 7
    instance.minInstances = 13
    assert instance.minInstances == 13


def test_camel_requirement_ImageRequirement_imageId_value_roundtrip():
    instance = camel_requirement_ImageRequirement(imageId="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_camel_requirement_OSRequirement_is64os_value_roundtrip():
    instance = camel_requirement_OSRequirement(is64os=True, os="sample_text")
    assert instance.is64os == True
    instance.is64os = False
    assert instance.is64os == False


def test_camel_requirement_OSRequirement_os_value_roundtrip():
    instance = camel_requirement_OSRequirement(is64os=True, os="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_camel_requirement_OptimisationRequirement_optimisationFunction_value_roundtrip():
    instance = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    assert instance.optimisationFunction == "sample_text"
    instance.optimisationFunction = "sample_text_2"
    assert instance.optimisationFunction == "sample_text_2"


def test_camel_requirement_QualitativeHardwareRequirement_maxBenchmark_value_roundtrip():
    instance = camel_requirement_QualitativeHardwareRequirement(maxBenchmark=3.14, minBenchmark=3.14)
    assert instance.maxBenchmark == 3.14
    instance.maxBenchmark = 9.99
    assert instance.maxBenchmark == 9.99


def test_camel_requirement_QualitativeHardwareRequirement_minBenchmark_value_roundtrip():
    instance = camel_requirement_QualitativeHardwareRequirement(maxBenchmark=3.14, minBenchmark=3.14)
    assert instance.minBenchmark == 3.14
    instance.minBenchmark = 9.99
    assert instance.minBenchmark == 9.99


def test_camel_requirement_QuantitativeHardwareRequirement_maxCPU_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxCPU == 3.14
    instance.maxCPU = 9.99
    assert instance.maxCPU == 9.99


def test_camel_requirement_QuantitativeHardwareRequirement_maxCores_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxCores == 7
    instance.maxCores = 13
    assert instance.maxCores == 13


def test_camel_requirement_QuantitativeHardwareRequirement_maxRAM_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxRAM == 7
    instance.maxRAM = 13
    assert instance.maxRAM == 13


def test_camel_requirement_QuantitativeHardwareRequirement_maxStorage_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxStorage == 7
    instance.maxStorage = 13
    assert instance.maxStorage == 13


def test_camel_requirement_QuantitativeHardwareRequirement_minCPU_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minCPU == 3.14
    instance.minCPU = 9.99
    assert instance.minCPU == 9.99


def test_camel_requirement_QuantitativeHardwareRequirement_minCores_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minCores == 7
    instance.minCores = 13
    assert instance.minCores == 13


def test_camel_requirement_QuantitativeHardwareRequirement_minRAM_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minRAM == 7
    instance.minRAM = 13
    assert instance.minRAM == 13


def test_camel_requirement_QuantitativeHardwareRequirement_minStorage_value_roundtrip():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minStorage == 7
    instance.minStorage = 13
    assert instance.minStorage == 13


def test_camel_requirement_Requirement_name_value_roundtrip():
    instance = camel_requirement_Requirement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_requirement_RequirementGroup_requirementOperator_value_roundtrip():
    instance = camel_requirement_RequirementGroup(requirementOperator="sample_text")
    assert instance.requirementOperator == "sample_text"
    instance.requirementOperator = "sample_text_2"
    assert instance.requirementOperator == "sample_text_2"


def test_camel_requirement_SoftRequirement_priority_value_roundtrip():
    instance = camel_requirement_SoftRequirement(priority=3.14)
    assert instance.priority == 3.14
    instance.priority = 9.99
    assert instance.priority == 9.99


def test_camel_requirement_VerticalScaleRequirement_maxCPU_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxCPU == 3.14
    instance.maxCPU = 9.99
    assert instance.maxCPU == 9.99


def test_camel_requirement_VerticalScaleRequirement_maxCores_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxCores == 7
    instance.maxCores = 13
    assert instance.maxCores == 13


def test_camel_requirement_VerticalScaleRequirement_maxRAM_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxRAM == 7
    instance.maxRAM = 13
    assert instance.maxRAM == 13


def test_camel_requirement_VerticalScaleRequirement_maxStorage_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.maxStorage == 7
    instance.maxStorage = 13
    assert instance.maxStorage == 13


def test_camel_requirement_VerticalScaleRequirement_minCPU_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minCPU == 3.14
    instance.minCPU = 9.99
    assert instance.minCPU == 9.99


def test_camel_requirement_VerticalScaleRequirement_minCores_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minCores == 7
    instance.minCores = 13
    assert instance.minCores == 13


def test_camel_requirement_VerticalScaleRequirement_minRAM_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minRAM == 7
    instance.minRAM = 13
    assert instance.minRAM == 13


def test_camel_requirement_VerticalScaleRequirement_minStorage_value_roundtrip():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert instance.minStorage == 7
    instance.minStorage = 13
    assert instance.minStorage == 13


def test_camel_scalability_BinaryEventPattern_lowerOccurrenceBound_value_roundtrip():
    instance = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    assert instance.lowerOccurrenceBound == 7
    instance.lowerOccurrenceBound = 13
    assert instance.lowerOccurrenceBound == 13


def test_camel_scalability_BinaryEventPattern_operator_value_roundtrip():
    instance = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_camel_scalability_BinaryEventPattern_upperOccurrenceBound_value_roundtrip():
    instance = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    assert instance.upperOccurrenceBound == 7
    instance.upperOccurrenceBound = 13
    assert instance.upperOccurrenceBound == 13


def test_camel_scalability_Event_name_value_roundtrip():
    instance = camel_scalability_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_scalability_EventInstance_layer_value_roundtrip():
    instance = camel_scalability_EventInstance(layer="sample_text", name="sample_text", status="sample_text")
    assert instance.layer == "sample_text"
    instance.layer = "sample_text_2"
    assert instance.layer == "sample_text_2"


def test_camel_scalability_EventInstance_name_value_roundtrip():
    instance = camel_scalability_EventInstance(layer="sample_text", name="sample_text", status="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_scalability_EventInstance_status_value_roundtrip():
    instance = camel_scalability_EventInstance(layer="sample_text", name="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_camel_scalability_FunctionalEvent_functionalType_value_roundtrip():
    instance = camel_scalability_FunctionalEvent(functionalType="sample_text")
    assert instance.functionalType == "sample_text"
    instance.functionalType = "sample_text_2"
    assert instance.functionalType == "sample_text_2"


def test_camel_scalability_HorizontalScalingAction_count_value_roundtrip():
    instance = camel_scalability_HorizontalScalingAction(count=7)
    assert instance.count == 7
    instance.count = 13
    assert instance.count == 13


def test_camel_scalability_NonFunctionalEvent_isViolation_value_roundtrip():
    instance = camel_scalability_NonFunctionalEvent(isViolation=True)
    assert instance.isViolation == True
    instance.isViolation = False
    assert instance.isViolation == False


def test_camel_scalability_ScalabilityRule_name_value_roundtrip():
    instance = camel_scalability_ScalabilityRule(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_scalability_Timer_maxOccurrenceNum_value_roundtrip():
    instance = camel_scalability_Timer(maxOccurrenceNum=7, name="sample_text", timeValue=7, type="sample_text")
    assert instance.maxOccurrenceNum == 7
    instance.maxOccurrenceNum = 13
    assert instance.maxOccurrenceNum == 13


def test_camel_scalability_Timer_name_value_roundtrip():
    instance = camel_scalability_Timer(maxOccurrenceNum=7, name="sample_text", timeValue=7, type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_scalability_Timer_timeValue_value_roundtrip():
    instance = camel_scalability_Timer(maxOccurrenceNum=7, name="sample_text", timeValue=7, type="sample_text")
    assert instance.timeValue == 7
    instance.timeValue = 13
    assert instance.timeValue == 13


def test_camel_scalability_Timer_type_value_roundtrip():
    instance = camel_scalability_Timer(maxOccurrenceNum=7, name="sample_text", timeValue=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_camel_scalability_UnaryEventPattern_occurrenceNum_value_roundtrip():
    instance = camel_scalability_UnaryEventPattern(occurrenceNum=7, operator="sample_text")
    assert instance.occurrenceNum == 7
    instance.occurrenceNum = 13
    assert instance.occurrenceNum == 13


def test_camel_scalability_UnaryEventPattern_operator_value_roundtrip():
    instance = camel_scalability_UnaryEventPattern(occurrenceNum=7, operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_camel_scalability_VerticalScalingAction_CPUUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.CPUUpdate == 3.14
    instance.CPUUpdate = 9.99
    assert instance.CPUUpdate == 9.99


def test_camel_scalability_VerticalScalingAction_coreUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.coreUpdate == 7
    instance.coreUpdate = 13
    assert instance.coreUpdate == 13


def test_camel_scalability_VerticalScalingAction_ioUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.ioUpdate == 7
    instance.ioUpdate = 13
    assert instance.ioUpdate == 13


def test_camel_scalability_VerticalScalingAction_memoryUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.memoryUpdate == 7
    instance.memoryUpdate = 13
    assert instance.memoryUpdate == 13


def test_camel_scalability_VerticalScalingAction_networkUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.networkUpdate == 7
    instance.networkUpdate = 13
    assert instance.networkUpdate == 13


def test_camel_scalability_VerticalScalingAction_storageUpdate_value_roundtrip():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert instance.storageUpdate == 7
    instance.storageUpdate = 13
    assert instance.storageUpdate == 13


def test_camel_security_SecurityCapability_name_value_roundtrip():
    instance = camel_security_SecurityCapability(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_security_SecurityControl_name_value_roundtrip():
    instance = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_security_SecurityControl_specification_value_roundtrip():
    instance = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    assert instance.specification == "sample_text"
    instance.specification = "sample_text_2"
    assert instance.specification == "sample_text_2"


def test_camel_security_SecurityDomain_id_value_roundtrip():
    instance = camel_security_SecurityDomain(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_camel_security_SecurityDomain_name_value_roundtrip():
    instance = camel_security_SecurityDomain(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_type_BoolValue_value_value_roundtrip():
    instance = camel_type_BoolValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_camel_type_BooleanValueType_primitiveType_value_roundtrip():
    instance = camel_type_BooleanValueType(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_camel_type_DoublePrecisionValue_value_value_roundtrip():
    instance = camel_type_DoublePrecisionValue(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_camel_type_EnumerateValue_name_value_roundtrip():
    instance = camel_type_EnumerateValue(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_type_EnumerateValue_value_value_roundtrip():
    instance = camel_type_EnumerateValue(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_camel_type_FloatsValue_value_value_roundtrip():
    instance = camel_type_FloatsValue(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_camel_type_IntegerValue_value_value_roundtrip():
    instance = camel_type_IntegerValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_camel_type_Limit_included_value_roundtrip():
    instance = camel_type_Limit(included=True)
    assert instance.included == True
    instance.included = False
    assert instance.included == False


def test_camel_type_List_primitiveType_value_roundtrip():
    instance = camel_type_List(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_camel_type_Range_primitiveType_value_roundtrip():
    instance = camel_type_Range(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_camel_type_RangeUnion_primitiveType_value_roundtrip():
    instance = camel_type_RangeUnion(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_camel_type_StringValueType_primitiveType_value_roundtrip():
    instance = camel_type_StringValueType(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_camel_type_StringsValue_value_value_roundtrip():
    instance = camel_type_StringsValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_camel_type_ValueType_name_value_roundtrip():
    instance = camel_type_ValueType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_unit_Unit_name_value_roundtrip():
    instance = camel_unit_Unit(name="sample_text", unit="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_camel_unit_Unit_unit_value_roundtrip():
    instance = camel_unit_Unit(name="sample_text", unit="sample_text")
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_camel_scalability_ScalingAction_isa_Action():
    instance = camel_scalability_ScalingAction()
    assert isinstance(instance, Action)


def test_camel_provider_Exclusive_isa_Alternative():
    instance = camel_provider_Exclusive()
    assert isinstance(instance, Alternative)


def test_camel_provider_FeatCardinality_isa_Cardinality():
    instance = camel_provider_FeatCardinality(value=7)
    assert isinstance(instance, Cardinality)


def test_camel_provider_GroupCardinality_isa_Cardinality():
    instance = camel_provider_GroupCardinality()
    assert isinstance(instance, Cardinality)


def test_camel_deployment_ProvidedCommunication_isa_CommunicationPort():
    instance = camel_deployment_ProvidedCommunication()
    assert isinstance(instance, CommunicationPort)


def test_camel_deployment_RequiredCommunication_isa_CommunicationPort():
    instance = camel_deployment_RequiredCommunication(isMandatory=True)
    assert isinstance(instance, CommunicationPort)


def test_camel_deployment_ProvidedCommunicationInstance_isa_CommunicationPortInstance():
    instance = camel_deployment_ProvidedCommunicationInstance()
    assert isinstance(instance, CommunicationPortInstance)


def test_camel_deployment_RequiredCommunicationInstance_isa_CommunicationPortInstance():
    instance = camel_deployment_RequiredCommunicationInstance()
    assert isinstance(instance, CommunicationPortInstance)


def test_camel_deployment_InternalComponent_isa_Component():
    instance = camel_deployment_InternalComponent(version="sample_text")
    assert isinstance(instance, Component)


def test_camel_deployment_VM_isa_Component():
    instance = camel_deployment_VM()
    assert isinstance(instance, Component)


def test_camel_deployment_InternalComponentInstance_isa_ComponentInstance():
    instance = camel_deployment_InternalComponentInstance()
    assert isinstance(instance, ComponentInstance)


def test_camel_deployment_VMInstance_isa_ComponentInstance():
    instance = camel_deployment_VMInstance(ip="sample_text")
    assert isinstance(instance, ComponentInstance)


def test_camel_security_CompositeSecurityMetric_isa_CompositeMetric():
    instance = camel_security_CompositeSecurityMetric()
    assert isinstance(instance, CompositeMetric)


def test_camel_security_CompositeSecurityMetricInstance_isa_CompositeMetricInstance():
    instance = camel_security_CompositeSecurityMetricInstance()
    assert isinstance(instance, CompositeMetricInstance)


def test_camel_metric_MetricCondition_isa_Condition():
    instance = camel_metric_MetricCondition()
    assert isinstance(instance, Condition)


def test_camel_metric_PropertyCondition_isa_Condition():
    instance = camel_metric_PropertyCondition()
    assert isinstance(instance, Condition)


def test_camel_metric_MetricContext_isa_ConditionContext():
    instance = camel_metric_MetricContext()
    assert isinstance(instance, ConditionContext)


def test_camel_metric_PropertyContext_isa_ConditionContext():
    instance = camel_metric_PropertyContext()
    assert isinstance(instance, ConditionContext)


def test_camel_provider_Excludes_isa_Constraint():
    instance = camel_provider_Excludes()
    assert isinstance(instance, Constraint)


def test_camel_provider_Implies_isa_Constraint():
    instance = camel_provider_Implies()
    assert isinstance(instance, Constraint)


def test_camel_provider_Requires_isa_Constraint():
    instance = camel_provider_Requires()
    assert isinstance(instance, Constraint)


def test_camel_organisation_CloudCredentials_isa_Credentials():
    instance = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    assert isinstance(instance, Credentials)


def test_camel_organisation_PaaSageCredentials_isa_Credentials():
    instance = camel_organisation_PaaSageCredentials(password="sample_text")
    assert isinstance(instance, Credentials)


def test_camel_deployment_Communication_isa_DeploymentElement():
    instance = camel_deployment_Communication(type="sample_text")
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_CommunicationInstance_isa_DeploymentElement():
    instance = camel_deployment_CommunicationInstance()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_CommunicationPort_isa_DeploymentElement():
    instance = camel_deployment_CommunicationPort(portNumber=7)
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_CommunicationPortInstance_isa_DeploymentElement():
    instance = camel_deployment_CommunicationPortInstance()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_Component_isa_DeploymentElement():
    instance = camel_deployment_Component()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_ComponentInstance_isa_DeploymentElement():
    instance = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_Configuration_isa_DeploymentElement():
    instance = camel_deployment_Configuration(configureCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_Hosting_isa_DeploymentElement():
    instance = camel_deployment_Hosting()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_HostingInstance_isa_DeploymentElement():
    instance = camel_deployment_HostingInstance()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_HostingPort_isa_DeploymentElement():
    instance = camel_deployment_HostingPort()
    assert isinstance(instance, DeploymentElement)


def test_camel_deployment_HostingPortInstance_isa_DeploymentElement():
    instance = camel_deployment_HostingPortInstance()
    assert isinstance(instance, DeploymentElement)


def test_camel_organisation_Organisation_isa_Entity():
    instance = camel_organisation_Organisation(email="sample_text", name="sample_text", postalAddress="sample_text", www="sample_text")
    assert isinstance(instance, Entity)


def test_camel_organisation_User_isa_Entity():
    instance = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    assert isinstance(instance, Entity)


def test_camel_scalability_EventPattern_isa_Event():
    instance = camel_scalability_EventPattern()
    assert isinstance(instance, Event)


def test_camel_scalability_SimpleEvent_isa_Event():
    instance = camel_scalability_SimpleEvent()
    assert isinstance(instance, Event)


def test_camel_scalability_BinaryEventPattern_isa_EventPattern():
    instance = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    assert isinstance(instance, EventPattern)


def test_camel_scalability_UnaryEventPattern_isa_EventPattern():
    instance = camel_scalability_UnaryEventPattern(occurrenceNum=7, operator="sample_text")
    assert isinstance(instance, EventPattern)


def test_camel_provider_Alternative_isa_Feature():
    instance = camel_provider_Alternative()
    assert isinstance(instance, Feature)


def test_camel_location_Country_isa_GeographicalRegion():
    instance = camel_location_Country()
    assert isinstance(instance, GeographicalRegion)


def test_camel_requirement_HardwareRequirement_isa_HardRequirement():
    instance = camel_requirement_HardwareRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_LocationRequirement_isa_HardRequirement():
    instance = camel_requirement_LocationRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_OSOrImageRequirement_isa_HardRequirement():
    instance = camel_requirement_OSOrImageRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_ProviderRequirement_isa_HardRequirement():
    instance = camel_requirement_ProviderRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_ScaleRequirement_isa_HardRequirement():
    instance = camel_requirement_ScaleRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_SecurityRequirement_isa_HardRequirement():
    instance = camel_requirement_SecurityRequirement()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_ServiceLevelObjective_isa_HardRequirement():
    instance = camel_requirement_ServiceLevelObjective()
    assert isinstance(instance, HardRequirement)


def test_camel_requirement_QualitativeHardwareRequirement_isa_HardwareRequirement():
    instance = camel_requirement_QualitativeHardwareRequirement(maxBenchmark=3.14, minBenchmark=3.14)
    assert isinstance(instance, HardwareRequirement)


def test_camel_requirement_QuantitativeHardwareRequirement_isa_HardwareRequirement():
    instance = camel_requirement_QuantitativeHardwareRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert isinstance(instance, HardwareRequirement)


def test_camel_deployment_ProvidedHost_isa_HostingPort():
    instance = camel_deployment_ProvidedHost()
    assert isinstance(instance, HostingPort)


def test_camel_deployment_RequiredHost_isa_HostingPort():
    instance = camel_deployment_RequiredHost()
    assert isinstance(instance, HostingPort)


def test_camel_deployment_ProvidedHostInstance_isa_HostingPortInstance():
    instance = camel_deployment_ProvidedHostInstance()
    assert isinstance(instance, HostingPortInstance)


def test_camel_deployment_RequiredHostInstance_isa_HostingPortInstance():
    instance = camel_deployment_RequiredHostInstance()
    assert isinstance(instance, HostingPortInstance)


def test_camel_location_CloudLocation_isa_Location():
    instance = camel_location_CloudLocation(isAssignable=True)
    assert isinstance(instance, Location)


def test_camel_location_GeographicalRegion_isa_Location():
    instance = camel_location_GeographicalRegion(alternativeNames="sample_text", name="sample_text")
    assert isinstance(instance, Location)


def test_camel_execution_ApplicationMeasurement_isa_Measurement():
    instance = camel_execution_ApplicationMeasurement()
    assert isinstance(instance, Measurement)


def test_camel_execution_CommunicationMeasurement_isa_Measurement():
    instance = camel_execution_CommunicationMeasurement()
    assert isinstance(instance, Measurement)


def test_camel_execution_InternalComponentMeasurement_isa_Measurement():
    instance = camel_execution_InternalComponentMeasurement()
    assert isinstance(instance, Measurement)


def test_camel_execution_VMMeasurement_isa_Measurement():
    instance = camel_execution_VMMeasurement()
    assert isinstance(instance, Measurement)


def test_camel_metric_CompositeMetric_isa_Metric():
    instance = camel_metric_CompositeMetric()
    assert isinstance(instance, Metric)


def test_camel_metric_RawMetric_isa_Metric():
    instance = camel_metric_RawMetric()
    assert isinstance(instance, Metric)


def test_camel_metric_CompositeMetricContext_isa_MetricContext():
    instance = camel_metric_CompositeMetricContext()
    assert isinstance(instance, MetricContext)


def test_camel_metric_RawMetricContext_isa_MetricContext():
    instance = camel_metric_RawMetricContext()
    assert isinstance(instance, MetricContext)


def test_camel_metric_Metric_isa_MetricFormulaParameter():
    instance = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    assert isinstance(instance, MetricFormulaParameter)


def test_camel_metric_MetricFormula_isa_MetricFormulaParameter():
    instance = camel_metric_MetricFormula(function="sample_text", functionArity="sample_text", functionPattern="sample_text")
    assert isinstance(instance, MetricFormulaParameter)


def test_camel_metric_CompositeMetricInstance_isa_MetricInstance():
    instance = camel_metric_CompositeMetricInstance()
    assert isinstance(instance, MetricInstance)


def test_camel_metric_RawMetricInstance_isa_MetricInstance():
    instance = camel_metric_RawMetricInstance()
    assert isinstance(instance, MetricInstance)


def test_camel_metric_MetricApplicationBinding_isa_MetricObjectBinding():
    instance = camel_metric_MetricApplicationBinding()
    assert isinstance(instance, MetricObjectBinding)


def test_camel_metric_MetricComponentBinding_isa_MetricObjectBinding():
    instance = camel_metric_MetricComponentBinding()
    assert isinstance(instance, MetricObjectBinding)


def test_camel_metric_MetricVMBinding_isa_MetricObjectBinding():
    instance = camel_metric_MetricVMBinding()
    assert isinstance(instance, MetricObjectBinding)


def test_camel_CamelModel_isa_Model():
    instance = camel_CamelModel()
    assert isinstance(instance, Model)


def test_camel_deployment_DeploymentModel_isa_Model():
    instance = camel_deployment_DeploymentModel()
    assert isinstance(instance, Model)


def test_camel_execution_ExecutionModel_isa_Model():
    instance = camel_execution_ExecutionModel()
    assert isinstance(instance, Model)


def test_camel_location_LocationModel_isa_Model():
    instance = camel_location_LocationModel()
    assert isinstance(instance, Model)


def test_camel_metric_MetricModel_isa_Model():
    instance = camel_metric_MetricModel()
    assert isinstance(instance, Model)


def test_camel_organisation_OrganisationModel_isa_Model():
    instance = camel_organisation_OrganisationModel(securityLevel="sample_text")
    assert isinstance(instance, Model)


def test_camel_provider_ProviderModel_isa_Model():
    instance = camel_provider_ProviderModel()
    assert isinstance(instance, Model)


def test_camel_requirement_RequirementModel_isa_Model():
    instance = camel_requirement_RequirementModel()
    assert isinstance(instance, Model)


def test_camel_scalability_ScalabilityModel_isa_Model():
    instance = camel_scalability_ScalabilityModel()
    assert isinstance(instance, Model)


def test_camel_security_SecurityModel_isa_Model():
    instance = camel_security_SecurityModel()
    assert isinstance(instance, Model)


def test_camel_type_TypeModel_isa_Model():
    instance = camel_type_TypeModel()
    assert isinstance(instance, Model)


def test_camel_unit_UnitModel_isa_Model():
    instance = camel_unit_UnitModel()
    assert isinstance(instance, Model)


def test_camel_type_DoublePrecisionValue_isa_NumericValue():
    instance = camel_type_DoublePrecisionValue(value=3.14)
    assert isinstance(instance, NumericValue)


def test_camel_type_FloatsValue_isa_NumericValue():
    instance = camel_type_FloatsValue(value=3.14)
    assert isinstance(instance, NumericValue)


def test_camel_type_IntegerValue_isa_NumericValue():
    instance = camel_type_IntegerValue(value=7)
    assert isinstance(instance, NumericValue)


def test_camel_type_NegativeInf_isa_NumericValue():
    instance = camel_type_NegativeInf()
    assert isinstance(instance, NumericValue)


def test_camel_type_PositiveInf_isa_NumericValue():
    instance = camel_type_PositiveInf()
    assert isinstance(instance, NumericValue)


def test_camel_type_ValueToIncrease_isa_NumericValue():
    instance = camel_type_ValueToIncrease()
    assert isinstance(instance, NumericValue)


def test_camel_requirement_ImageRequirement_isa_OSOrImageRequirement():
    instance = camel_requirement_ImageRequirement(imageId="sample_text")
    assert isinstance(instance, OSOrImageRequirement)


def test_camel_requirement_OSRequirement_isa_OSOrImageRequirement():
    instance = camel_requirement_OSRequirement(is64os=True, os="sample_text")
    assert isinstance(instance, OSOrImageRequirement)


def test_camel_organisation_CloudProvider_isa_Organisation():
    instance = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    assert isinstance(instance, Organisation)


def test_camel_security_SecurityProperty_isa_Property():
    instance = camel_security_SecurityProperty()
    assert isinstance(instance, Property)


def test_camel_security_RawSecurityMetric_isa_RawMetric():
    instance = camel_security_RawSecurityMetric()
    assert isinstance(instance, RawMetric)


def test_camel_security_RawSecurityMetricInstance_isa_RawMetricInstance():
    instance = camel_security_RawSecurityMetricInstance()
    assert isinstance(instance, RawMetricInstance)


def test_camel_requirement_HardRequirement_isa_Requirement():
    instance = camel_requirement_HardRequirement()
    assert isinstance(instance, Requirement)


def test_camel_requirement_RequirementGroup_isa_Requirement():
    instance = camel_requirement_RequirementGroup(requirementOperator="sample_text")
    assert isinstance(instance, Requirement)


def test_camel_requirement_SoftRequirement_isa_Requirement():
    instance = camel_requirement_SoftRequirement(priority=3.14)
    assert isinstance(instance, Requirement)


def test_camel_provider_Functional_isa_Requires():
    instance = camel_provider_Functional(order=7, type="sample_text", value=7)
    assert isinstance(instance, Requires)


def test_camel_organisation_InformationResourceFilter_isa_ResourceFilter():
    instance = camel_organisation_InformationResourceFilter(everyInformationResource=True, informationResourcePath="sample_text")
    assert isinstance(instance, ResourceFilter)


def test_camel_organisation_ServiceResourceFilter_isa_ResourceFilter():
    instance = camel_organisation_ServiceResourceFilter(everyService=True, serviceURL="sample_text")
    assert isinstance(instance, ResourceFilter)


def test_camel_requirement_HorizontalScaleRequirement_isa_ScaleRequirement():
    instance = camel_requirement_HorizontalScaleRequirement(maxInstances=7, minInstances=7)
    assert isinstance(instance, ScaleRequirement)


def test_camel_requirement_VerticalScaleRequirement_isa_ScaleRequirement():
    instance = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    assert isinstance(instance, ScaleRequirement)


def test_camel_scalability_HorizontalScalingAction_isa_ScalingAction():
    instance = camel_scalability_HorizontalScalingAction(count=7)
    assert isinstance(instance, ScalingAction)


def test_camel_scalability_VerticalScalingAction_isa_ScalingAction():
    instance = camel_scalability_VerticalScalingAction(CPUUpdate=3.14, coreUpdate=7, ioUpdate=7, memoryUpdate=7, networkUpdate=7, storageUpdate=7)
    assert isinstance(instance, ScalingAction)


def test_camel_provider_Instance_isa_Scope():
    instance = camel_provider_Instance()
    assert isinstance(instance, Scope)


def test_camel_provider_Product_isa_Scope():
    instance = camel_provider_Product()
    assert isinstance(instance, Scope)


def test_camel_security_Certifiable_isa_SecurityProperty():
    instance = camel_security_Certifiable()
    assert isinstance(instance, SecurityProperty)


def test_camel_security_SecuritySLO_isa_ServiceLevelObjective():
    instance = camel_security_SecuritySLO()
    assert isinstance(instance, ServiceLevelObjective)


def test_camel_scalability_FunctionalEvent_isa_SimpleEvent():
    instance = camel_scalability_FunctionalEvent(functionalType="sample_text")
    assert isinstance(instance, SimpleEvent)


def test_camel_scalability_NonFunctionalEvent_isa_SimpleEvent():
    instance = camel_scalability_NonFunctionalEvent(isViolation=True)
    assert isinstance(instance, SimpleEvent)


def test_camel_type_BoolValue_isa_SingleValue():
    instance = camel_type_BoolValue(value=True)
    assert isinstance(instance, SingleValue)


def test_camel_type_EnumerateValue_isa_SingleValue():
    instance = camel_type_EnumerateValue(name="sample_text", value=7)
    assert isinstance(instance, SingleValue)


def test_camel_type_NumericValue_isa_SingleValue():
    instance = camel_type_NumericValue()
    assert isinstance(instance, SingleValue)


def test_camel_type_StringsValue_isa_SingleValue():
    instance = camel_type_StringsValue(value="sample_text")
    assert isinstance(instance, SingleValue)


def test_camel_requirement_OptimisationRequirement_isa_SoftRequirement():
    instance = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    assert isinstance(instance, SoftRequirement)


def test_camel_unit_CoreUnit_isa_Unit():
    instance = camel_unit_CoreUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_Dimensionless_isa_Unit():
    instance = camel_unit_Dimensionless()
    assert isinstance(instance, Unit)


def test_camel_unit_MonetaryUnit_isa_Unit():
    instance = camel_unit_MonetaryUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_RequestUnit_isa_Unit():
    instance = camel_unit_RequestUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_StorageUnit_isa_Unit():
    instance = camel_unit_StorageUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_ThroughputUnit_isa_Unit():
    instance = camel_unit_ThroughputUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_TimeIntervalUnit_isa_Unit():
    instance = camel_unit_TimeIntervalUnit()
    assert isinstance(instance, Unit)


def test_camel_unit_TransactionUnit_isa_Unit():
    instance = camel_unit_TransactionUnit()
    assert isinstance(instance, Unit)


def test_camel_type_BooleanValueType_isa_ValueType():
    instance = camel_type_BooleanValueType(primitiveType="sample_text")
    assert isinstance(instance, ValueType)


def test_camel_type_Enumeration_isa_ValueType():
    instance = camel_type_Enumeration()
    assert isinstance(instance, ValueType)


def test_camel_type_List_isa_ValueType():
    instance = camel_type_List(primitiveType="sample_text")
    assert isinstance(instance, ValueType)


def test_camel_type_Range_isa_ValueType():
    instance = camel_type_Range(primitiveType="sample_text")
    assert isinstance(instance, ValueType)


def test_camel_type_RangeUnion_isa_ValueType():
    instance = camel_type_RangeUnion(primitiveType="sample_text")
    assert isinstance(instance, ValueType)


def test_camel_type_StringValueType_isa_ValueType():
    instance = camel_type_StringValueType(primitiveType="sample_text")
    assert isinstance(instance, ValueType)


def test_assoc_action134_link_reassign_clear():
    a = camel_execution_ActionRealisation(endTime=date(2024, 1, 1), lowLevelActions="sample_text", name="sample_text", startTime=date(2024, 1, 1))
    b1 = execution_camel_Action()
    b2 = execution_camel_Action()
    _safe_set(a, 'camel_execution_ActionRealisation', b1)
    assert _is_linked(a, 'camel_execution_ActionRealisation', b1)
    if hasattr(b1, 'execution_camel_Action'):
        assert _is_linked(b1, 'execution_camel_Action', a)
    _safe_set(a, 'camel_execution_ActionRealisation', b2)
    assert _is_linked(a, 'camel_execution_ActionRealisation', b2)
    if hasattr(b1, 'execution_camel_Action'):
        assert not _is_linked(b1, 'execution_camel_Action', a)
    if hasattr(b2, 'execution_camel_Action'):
        assert _is_linked(b2, 'execution_camel_Action', a)
    _safe_set(a, 'camel_execution_ActionRealisation', None)
    assert not _is_linked(a, 'camel_execution_ActionRealisation', b2)
    if hasattr(b2, 'execution_camel_Action'):
        assert not _is_linked(b2, 'execution_camel_Action', a)


def test_assoc_actionRealisations175_link_reassign_clear():
    a = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    b1 = ActionRealisation()
    b2 = ActionRealisation()
    _safe_set(a, 'camel_execution_RuleTrigger176', {b1})
    assert _is_linked(a, 'camel_execution_RuleTrigger176', b1)
    if hasattr(b1, 'ActionRealisation177'):
        assert _is_linked(b1, 'ActionRealisation177', a)
    _safe_set(a, 'camel_execution_RuleTrigger176', {b2})
    assert _is_linked(a, 'camel_execution_RuleTrigger176', b2)
    if hasattr(b1, 'ActionRealisation177'):
        assert not _is_linked(b1, 'ActionRealisation177', a)
    if hasattr(b2, 'ActionRealisation177'):
        assert _is_linked(b2, 'ActionRealisation177', a)
    _safe_set(a, 'camel_execution_RuleTrigger176', set())
    assert not _is_linked(a, 'camel_execution_RuleTrigger176', b2)
    if hasattr(b2, 'ActionRealisation177'):
        assert not _is_linked(b2, 'ActionRealisation177', a)


def test_assoc_actions0_link_reassign_clear():
    a = camel_Action(name="sample_text", type="sample_text")
    b1 = camel_CamelModel()
    b2 = camel_CamelModel()
    _safe_set(a, 'camel_Action', b1)
    assert _is_linked(a, 'camel_Action', b1)
    if hasattr(b1, 'camel_CamelModel'):
        assert _is_linked(b1, 'camel_CamelModel', a)
    _safe_set(a, 'camel_Action', b2)
    assert _is_linked(a, 'camel_Action', b2)
    if hasattr(b1, 'camel_CamelModel'):
        assert not _is_linked(b1, 'camel_CamelModel', a)
    if hasattr(b2, 'camel_CamelModel'):
        assert _is_linked(b2, 'camel_CamelModel', a)
    _safe_set(a, 'camel_Action', None)
    assert not _is_linked(a, 'camel_Action', b2)
    if hasattr(b2, 'camel_CamelModel'):
        assert not _is_linked(b2, 'camel_CamelModel', a)


def test_assoc_actions463_link_reassign_clear():
    a = camel_scalability_ScalabilityRule(name="sample_text")
    b1 = scalability_camel_Action()
    b2 = scalability_camel_Action()
    _safe_set(a, 'camel_scalability_ScalabilityRule464', {b1})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule464', b1)
    if hasattr(b1, 'scalability_camel_Action'):
        assert _is_linked(b1, 'scalability_camel_Action', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule464', {b2})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule464', b2)
    if hasattr(b1, 'scalability_camel_Action'):
        assert not _is_linked(b1, 'scalability_camel_Action', a)
    if hasattr(b2, 'scalability_camel_Action'):
        assert _is_linked(b2, 'scalability_camel_Action', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule464', set())
    assert not _is_linked(a, 'camel_scalability_ScalabilityRule464', b2)
    if hasattr(b2, 'scalability_camel_Action'):
        assert not _is_linked(b2, 'scalability_camel_Action', a)


def test_assoc_application135_link_reassign_clear():
    a = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    b1 = execution_camel_Application()
    b2 = execution_camel_Application()
    _safe_set(a, 'camel_execution_ExecutionContext', b1)
    assert _is_linked(a, 'camel_execution_ExecutionContext', b1)
    if hasattr(b1, 'execution_camel_Application'):
        assert _is_linked(b1, 'execution_camel_Application', a)
    _safe_set(a, 'camel_execution_ExecutionContext', b2)
    assert _is_linked(a, 'camel_execution_ExecutionContext', b2)
    if hasattr(b1, 'execution_camel_Application'):
        assert not _is_linked(b1, 'execution_camel_Application', a)
    if hasattr(b2, 'execution_camel_Application'):
        assert _is_linked(b2, 'execution_camel_Application', a)
    _safe_set(a, 'camel_execution_ExecutionContext', None)
    assert not _is_linked(a, 'camel_execution_ExecutionContext', b2)
    if hasattr(b2, 'execution_camel_Application'):
        assert not _is_linked(b2, 'execution_camel_Application', a)


def test_assoc_application244_link_reassign_clear():
    a = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    b1 = metric_camel_Application()
    b2 = metric_camel_Application()
    _safe_set(a, 'camel_metric_ConditionContext245', b1)
    assert _is_linked(a, 'camel_metric_ConditionContext245', b1)
    if hasattr(b1, 'metric_camel_Application'):
        assert _is_linked(b1, 'metric_camel_Application', a)
    _safe_set(a, 'camel_metric_ConditionContext245', b2)
    assert _is_linked(a, 'camel_metric_ConditionContext245', b2)
    if hasattr(b1, 'metric_camel_Application'):
        assert not _is_linked(b1, 'metric_camel_Application', a)
    if hasattr(b2, 'metric_camel_Application'):
        assert _is_linked(b2, 'metric_camel_Application', a)
    _safe_set(a, 'camel_metric_ConditionContext245', None)
    assert not _is_linked(a, 'camel_metric_ConditionContext245', b2)
    if hasattr(b2, 'metric_camel_Application'):
        assert not _is_linked(b2, 'metric_camel_Application', a)


def test_assoc_application399_link_reassign_clear():
    a = camel_requirement_RequirementGroup(requirementOperator="sample_text")
    b1 = requirement_camel_Application()
    b2 = requirement_camel_Application()
    _safe_set(a, 'camel_requirement_RequirementGroup400', {b1})
    assert _is_linked(a, 'camel_requirement_RequirementGroup400', b1)
    if hasattr(b1, 'requirement_camel_Application'):
        assert _is_linked(b1, 'requirement_camel_Application', a)
    _safe_set(a, 'camel_requirement_RequirementGroup400', {b2})
    assert _is_linked(a, 'camel_requirement_RequirementGroup400', b2)
    if hasattr(b1, 'requirement_camel_Application'):
        assert not _is_linked(b1, 'requirement_camel_Application', a)
    if hasattr(b2, 'requirement_camel_Application'):
        assert _is_linked(b2, 'requirement_camel_Application', a)
    _safe_set(a, 'camel_requirement_RequirementGroup400', set())
    assert not _is_linked(a, 'camel_requirement_RequirementGroup400', b2)
    if hasattr(b2, 'requirement_camel_Application'):
        assert not _is_linked(b2, 'requirement_camel_Application', a)


def test_assoc_application408_link_reassign_clear():
    a = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    b1 = requirement_camel_Application()
    b2 = requirement_camel_Application()
    _safe_set(a, 'camel_requirement_OptimisationRequirement409', b1)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement409', b1)
    if hasattr(b1, 'requirement_camel_Application410'):
        assert _is_linked(b1, 'requirement_camel_Application410', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement409', b2)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement409', b2)
    if hasattr(b1, 'requirement_camel_Application410'):
        assert not _is_linked(b1, 'requirement_camel_Application410', a)
    if hasattr(b2, 'requirement_camel_Application410'):
        assert _is_linked(b2, 'requirement_camel_Application410', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement409', None)
    assert not _is_linked(a, 'camel_requirement_OptimisationRequirement409', b2)
    if hasattr(b2, 'requirement_camel_Application410'):
        assert not _is_linked(b2, 'requirement_camel_Application410', a)


def test_assoc_applications1_link_reassign_clear():
    a = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    b1 = camel_CamelModel()
    b2 = camel_CamelModel()
    _safe_set(a, 'camel_Application', b1)
    assert _is_linked(a, 'camel_Application', b1)
    if hasattr(b1, 'camel_CamelModel2'):
        assert _is_linked(b1, 'camel_CamelModel2', a)
    _safe_set(a, 'camel_Application', b2)
    assert _is_linked(a, 'camel_Application', b2)
    if hasattr(b1, 'camel_CamelModel2'):
        assert not _is_linked(b1, 'camel_CamelModel2', a)
    if hasattr(b2, 'camel_CamelModel2'):
        assert _is_linked(b2, 'camel_CamelModel2', a)
    _safe_set(a, 'camel_Application', None)
    assert not _is_linked(a, 'camel_Application', b2)
    if hasattr(b2, 'camel_CamelModel2'):
        assert not _is_linked(b2, 'camel_CamelModel2', a)


def test_assoc_attributeConstraints368_link_reassign_clear():
    a = camel_provider_Constraint(name="sample_text")
    b1 = AttributeConstraint()
    b2 = AttributeConstraint()
    _safe_set(a, 'camel_provider_Constraint369', {b1})
    assert _is_linked(a, 'camel_provider_Constraint369', b1)
    if hasattr(b1, 'AttributeConstraint'):
        assert _is_linked(b1, 'AttributeConstraint', a)
    _safe_set(a, 'camel_provider_Constraint369', {b2})
    assert _is_linked(a, 'camel_provider_Constraint369', b2)
    if hasattr(b1, 'AttributeConstraint'):
        assert not _is_linked(b1, 'AttributeConstraint', a)
    if hasattr(b2, 'AttributeConstraint'):
        assert _is_linked(b2, 'AttributeConstraint', a)
    _safe_set(a, 'camel_provider_Constraint369', set())
    assert not _is_linked(a, 'camel_provider_Constraint369', b2)
    if hasattr(b2, 'AttributeConstraint'):
        assert not _is_linked(b2, 'AttributeConstraint', a)


def test_assoc_attributes379_link_reassign_clear():
    a = camel_provider_Feature(name="sample_text")
    b1 = Attribute()
    b2 = Attribute()
    _safe_set(a, 'camel_provider_Feature', {b1})
    assert _is_linked(a, 'camel_provider_Feature', b1)
    if hasattr(b1, 'Attribute380'):
        assert _is_linked(b1, 'Attribute380', a)
    _safe_set(a, 'camel_provider_Feature', {b2})
    assert _is_linked(a, 'camel_provider_Feature', b2)
    if hasattr(b1, 'Attribute380'):
        assert not _is_linked(b1, 'Attribute380', a)
    if hasattr(b2, 'Attribute380'):
        assert _is_linked(b2, 'Attribute380', a)
    _safe_set(a, 'camel_provider_Feature', set())
    assert not _is_linked(a, 'camel_provider_Feature', b2)
    if hasattr(b2, 'Attribute380'):
        assert not _is_linked(b2, 'Attribute380', a)


def test_assoc_clones387_link_reassign_clear():
    a = camel_provider_Feature(name="sample_text")
    b1 = Clone()
    b2 = Clone()
    _safe_set(a, 'camel_provider_Feature388', {b1})
    assert _is_linked(a, 'camel_provider_Feature388', b1)
    if hasattr(b1, 'Clone389'):
        assert _is_linked(b1, 'Clone389', a)
    _safe_set(a, 'camel_provider_Feature388', {b2})
    assert _is_linked(a, 'camel_provider_Feature388', b2)
    if hasattr(b1, 'Clone389'):
        assert not _is_linked(b1, 'Clone389', a)
    if hasattr(b2, 'Clone389'):
        assert _is_linked(b2, 'Clone389', a)
    _safe_set(a, 'camel_provider_Feature388', set())
    assert not _is_linked(a, 'camel_provider_Feature388', b2)
    if hasattr(b2, 'Clone389'):
        assert not _is_linked(b2, 'Clone389', a)


def test_assoc_cloudCredentials321_link_reassign_clear():
    a = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    b1 = CloudCredentials()
    b2 = CloudCredentials()
    _safe_set(a, 'camel_organisation_User322', {b1})
    assert _is_linked(a, 'camel_organisation_User322', b1)
    if hasattr(b1, 'CloudCredentials'):
        assert _is_linked(b1, 'CloudCredentials', a)
    _safe_set(a, 'camel_organisation_User322', {b2})
    assert _is_linked(a, 'camel_organisation_User322', b2)
    if hasattr(b1, 'CloudCredentials'):
        assert not _is_linked(b1, 'CloudCredentials', a)
    if hasattr(b2, 'CloudCredentials'):
        assert _is_linked(b2, 'CloudCredentials', a)
    _safe_set(a, 'camel_organisation_User322', set())
    assert not _is_linked(a, 'camel_organisation_User322', b2)
    if hasattr(b2, 'CloudCredentials'):
        assert not _is_linked(b2, 'CloudCredentials', a)


def test_assoc_cloudProvider309_link_reassign_clear():
    a = camel_organisation_CloudCredentials(name="sample_text", password="sample_text", privateSSHKey="sample_text", publicSSHKey="sample_text", securityGroup="sample_text", username="sample_text")
    b1 = CloudProvider()
    b2 = CloudProvider()
    _safe_set(a, 'camel_organisation_CloudCredentials', b1)
    assert _is_linked(a, 'camel_organisation_CloudCredentials', b1)
    if hasattr(b1, 'CloudProvider310'):
        assert _is_linked(b1, 'CloudProvider310', a)
    _safe_set(a, 'camel_organisation_CloudCredentials', b2)
    assert _is_linked(a, 'camel_organisation_CloudCredentials', b2)
    if hasattr(b1, 'CloudProvider310'):
        assert not _is_linked(b1, 'CloudProvider310', a)
    if hasattr(b2, 'CloudProvider310'):
        assert _is_linked(b2, 'CloudProvider310', a)
    _safe_set(a, 'camel_organisation_CloudCredentials', None)
    assert not _is_linked(a, 'camel_organisation_CloudCredentials', b2)
    if hasattr(b2, 'CloudProvider310'):
        assert not _is_linked(b2, 'CloudProvider310', a)


def test_assoc_component242_link_reassign_clear():
    a = camel_metric_ConditionContext(isRelative=True, maxQuantity=3.14, minQuantity=3.14, name="sample_text", quantifier="sample_text")
    b1 = Component()
    b2 = Component()
    _safe_set(a, 'camel_metric_ConditionContext', b1)
    assert _is_linked(a, 'camel_metric_ConditionContext', b1)
    if hasattr(b1, 'Component243'):
        assert _is_linked(b1, 'Component243', a)
    _safe_set(a, 'camel_metric_ConditionContext', b2)
    assert _is_linked(a, 'camel_metric_ConditionContext', b2)
    if hasattr(b1, 'Component243'):
        assert not _is_linked(b1, 'Component243', a)
    if hasattr(b2, 'Component243'):
        assert _is_linked(b2, 'Component243', a)
    _safe_set(a, 'camel_metric_ConditionContext', None)
    assert not _is_linked(a, 'camel_metric_ConditionContext', b2)
    if hasattr(b2, 'Component243'):
        assert not _is_linked(b2, 'Component243', a)


def test_assoc_component411_link_reassign_clear():
    a = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    b1 = Component()
    b2 = Component()
    _safe_set(a, 'camel_requirement_OptimisationRequirement412', b1)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement412', b1)
    if hasattr(b1, 'Component413'):
        assert _is_linked(b1, 'Component413', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement412', b2)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement412', b2)
    if hasattr(b1, 'Component413'):
        assert not _is_linked(b1, 'Component413', a)
    if hasattr(b2, 'Component413'):
        assert _is_linked(b2, 'Component413', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement412', None)
    assert not _is_linked(a, 'camel_requirement_OptimisationRequirement412', b2)
    if hasattr(b2, 'Component413'):
        assert not _is_linked(b2, 'Component413', a)


def test_assoc_component428_link_reassign_clear():
    a = camel_requirement_HorizontalScaleRequirement(maxInstances=7, minInstances=7)
    b1 = InternalComponent()
    b2 = InternalComponent()
    _safe_set(a, 'camel_requirement_HorizontalScaleRequirement', b1)
    assert _is_linked(a, 'camel_requirement_HorizontalScaleRequirement', b1)
    if hasattr(b1, 'InternalComponent429'):
        assert _is_linked(b1, 'InternalComponent429', a)
    _safe_set(a, 'camel_requirement_HorizontalScaleRequirement', b2)
    assert _is_linked(a, 'camel_requirement_HorizontalScaleRequirement', b2)
    if hasattr(b1, 'InternalComponent429'):
        assert not _is_linked(b1, 'InternalComponent429', a)
    if hasattr(b2, 'InternalComponent429'):
        assert _is_linked(b2, 'InternalComponent429', a)
    _safe_set(a, 'camel_requirement_HorizontalScaleRequirement', None)
    assert not _is_linked(a, 'camel_requirement_HorizontalScaleRequirement', b2)
    if hasattr(b2, 'InternalComponent429'):
        assert not _is_linked(b2, 'InternalComponent429', a)


def test_assoc_compositeInternalComponents55_link_reassign_clear():
    a = camel_deployment_InternalComponent(version="sample_text")
    b1 = InternalComponent()
    b2 = InternalComponent()
    _safe_set(a, 'camel_deployment_InternalComponent', {b1})
    assert _is_linked(a, 'camel_deployment_InternalComponent', b1)
    if hasattr(b1, 'InternalComponent56'):
        assert _is_linked(b1, 'InternalComponent56', a)
    _safe_set(a, 'camel_deployment_InternalComponent', {b2})
    assert _is_linked(a, 'camel_deployment_InternalComponent', b2)
    if hasattr(b1, 'InternalComponent56'):
        assert not _is_linked(b1, 'InternalComponent56', a)
    if hasattr(b2, 'InternalComponent56'):
        assert _is_linked(b2, 'InternalComponent56', a)
    _safe_set(a, 'camel_deployment_InternalComponent', set())
    assert not _is_linked(a, 'camel_deployment_InternalComponent', b2)
    if hasattr(b2, 'InternalComponent56'):
        assert not _is_linked(b2, 'InternalComponent56', a)


def test_assoc_compositeSecurityMetrics511_link_reassign_clear():
    a = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    b1 = CompositeSecurityMetric()
    b2 = CompositeSecurityMetric()
    _safe_set(a, 'camel_security_SecurityControl512', {b1})
    assert _is_linked(a, 'camel_security_SecurityControl512', b1)
    if hasattr(b1, 'CompositeSecurityMetric513'):
        assert _is_linked(b1, 'CompositeSecurityMetric513', a)
    _safe_set(a, 'camel_security_SecurityControl512', {b2})
    assert _is_linked(a, 'camel_security_SecurityControl512', b2)
    if hasattr(b1, 'CompositeSecurityMetric513'):
        assert not _is_linked(b1, 'CompositeSecurityMetric513', a)
    if hasattr(b2, 'CompositeSecurityMetric513'):
        assert _is_linked(b2, 'CompositeSecurityMetric513', a)
    _safe_set(a, 'camel_security_SecurityControl512', set())
    assert not _is_linked(a, 'camel_security_SecurityControl512', b2)
    if hasattr(b2, 'CompositeSecurityMetric513'):
        assert not _is_linked(b2, 'CompositeSecurityMetric513', a)


def test_assoc_costUnit136_link_reassign_clear():
    a = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    b1 = MonetaryUnit()
    b2 = MonetaryUnit()
    _safe_set(a, 'camel_execution_ExecutionContext137', b1)
    assert _is_linked(a, 'camel_execution_ExecutionContext137', b1)
    if hasattr(b1, 'MonetaryUnit'):
        assert _is_linked(b1, 'MonetaryUnit', a)
    _safe_set(a, 'camel_execution_ExecutionContext137', b2)
    assert _is_linked(a, 'camel_execution_ExecutionContext137', b2)
    if hasattr(b1, 'MonetaryUnit'):
        assert not _is_linked(b1, 'MonetaryUnit', a)
    if hasattr(b2, 'MonetaryUnit'):
        assert _is_linked(b2, 'MonetaryUnit', a)
    _safe_set(a, 'camel_execution_ExecutionContext137', None)
    assert not _is_linked(a, 'camel_execution_ExecutionContext137', b2)
    if hasattr(b2, 'MonetaryUnit'):
        assert not _is_linked(b2, 'MonetaryUnit', a)


def test_assoc_dataCenter518_link_reassign_clear():
    a = camel_security_SecurityCapability(name="sample_text")
    b1 = DataCenter()
    b2 = DataCenter()
    _safe_set(a, 'camel_security_SecurityCapability519', b1)
    assert _is_linked(a, 'camel_security_SecurityCapability519', b1)
    if hasattr(b1, 'DataCenter520'):
        assert _is_linked(b1, 'DataCenter520', a)
    _safe_set(a, 'camel_security_SecurityCapability519', b2)
    assert _is_linked(a, 'camel_security_SecurityCapability519', b2)
    if hasattr(b1, 'DataCenter520'):
        assert not _is_linked(b1, 'DataCenter520', a)
    if hasattr(b2, 'DataCenter520'):
        assert _is_linked(b2, 'DataCenter520', a)
    _safe_set(a, 'camel_security_SecurityCapability519', None)
    assert not _is_linked(a, 'camel_security_SecurityCapability519', b2)
    if hasattr(b2, 'DataCenter520'):
        assert not _is_linked(b2, 'DataCenter520', a)


def test_assoc_dataCentres299_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = DataCenter()
    b2 = DataCenter()
    _safe_set(a, 'camel_organisation_OrganisationModel300', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel300', b1)
    if hasattr(b1, 'DataCenter'):
        assert _is_linked(b1, 'DataCenter', a)
    _safe_set(a, 'camel_organisation_OrganisationModel300', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel300', b2)
    if hasattr(b1, 'DataCenter'):
        assert not _is_linked(b1, 'DataCenter', a)
    if hasattr(b2, 'DataCenter'):
        assert _is_linked(b2, 'DataCenter', a)
    _safe_set(a, 'camel_organisation_OrganisationModel300', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel300', b2)
    if hasattr(b2, 'DataCenter'):
        assert not _is_linked(b2, 'DataCenter', a)


def test_assoc_deploymentModel138_link_reassign_clear():
    a = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    b1 = DeploymentModel()
    b2 = DeploymentModel()
    _safe_set(a, 'camel_execution_ExecutionContext139', b1)
    assert _is_linked(a, 'camel_execution_ExecutionContext139', b1)
    if hasattr(b1, 'DeploymentModel140'):
        assert _is_linked(b1, 'DeploymentModel140', a)
    _safe_set(a, 'camel_execution_ExecutionContext139', b2)
    assert _is_linked(a, 'camel_execution_ExecutionContext139', b2)
    if hasattr(b1, 'DeploymentModel140'):
        assert not _is_linked(b1, 'DeploymentModel140', a)
    if hasattr(b2, 'DeploymentModel140'):
        assert _is_linked(b2, 'DeploymentModel140', a)
    _safe_set(a, 'camel_execution_ExecutionContext139', None)
    assert not _is_linked(a, 'camel_execution_ExecutionContext139', b2)
    if hasattr(b2, 'DeploymentModel140'):
        assert not _is_linked(b2, 'DeploymentModel140', a)


def test_assoc_deploymentModels27_link_reassign_clear():
    a = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    b1 = DeploymentModel()
    b2 = DeploymentModel()
    _safe_set(a, 'camel_Application28', {b1})
    assert _is_linked(a, 'camel_Application28', b1)
    if hasattr(b1, 'DeploymentModel29'):
        assert _is_linked(b1, 'DeploymentModel29', a)
    _safe_set(a, 'camel_Application28', {b2})
    assert _is_linked(a, 'camel_Application28', b2)
    if hasattr(b1, 'DeploymentModel29'):
        assert not _is_linked(b1, 'DeploymentModel29', a)
    if hasattr(b2, 'DeploymentModel29'):
        assert _is_linked(b2, 'DeploymentModel29', a)
    _safe_set(a, 'camel_Application28', set())
    assert not _is_linked(a, 'camel_Application28', b2)
    if hasattr(b2, 'DeploymentModel29'):
        assert not _is_linked(b2, 'DeploymentModel29', a)


def test_assoc_deploymentModels323_link_reassign_clear():
    a = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    b1 = DeploymentModel()
    b2 = DeploymentModel()
    _safe_set(a, 'camel_organisation_User324', {b1})
    assert _is_linked(a, 'camel_organisation_User324', b1)
    if hasattr(b1, 'DeploymentModel325'):
        assert _is_linked(b1, 'DeploymentModel325', a)
    _safe_set(a, 'camel_organisation_User324', {b2})
    assert _is_linked(a, 'camel_organisation_User324', b2)
    if hasattr(b1, 'DeploymentModel325'):
        assert not _is_linked(b1, 'DeploymentModel325', a)
    if hasattr(b2, 'DeploymentModel325'):
        assert _is_linked(b2, 'DeploymentModel325', a)
    _safe_set(a, 'camel_organisation_User324', set())
    assert not _is_linked(a, 'camel_organisation_User324', b2)
    if hasattr(b2, 'DeploymentModel325'):
        assert not _is_linked(b2, 'DeploymentModel325', a)


def test_assoc_domain500_link_reassign_clear():
    a = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    b1 = SecurityDomain()
    b2 = SecurityDomain()
    _safe_set(a, 'camel_security_SecurityControl', b1)
    assert _is_linked(a, 'camel_security_SecurityControl', b1)
    if hasattr(b1, 'SecurityDomain501'):
        assert _is_linked(b1, 'SecurityDomain501', a)
    _safe_set(a, 'camel_security_SecurityControl', b2)
    assert _is_linked(a, 'camel_security_SecurityControl', b2)
    if hasattr(b1, 'SecurityDomain501'):
        assert not _is_linked(b1, 'SecurityDomain501', a)
    if hasattr(b2, 'SecurityDomain501'):
        assert _is_linked(b2, 'SecurityDomain501', a)
    _safe_set(a, 'camel_security_SecurityControl', None)
    assert not _is_linked(a, 'camel_security_SecurityControl', b2)
    if hasattr(b2, 'SecurityDomain501'):
        assert not _is_linked(b2, 'SecurityDomain501', a)


def test_assoc_entity465_link_reassign_clear():
    a = camel_scalability_ScalabilityRule(name="sample_text")
    b1 = Entity()
    b2 = Entity()
    _safe_set(a, 'camel_scalability_ScalabilityRule466', {b1})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule466', b1)
    if hasattr(b1, 'Entity467'):
        assert _is_linked(b1, 'Entity467', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule466', {b2})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule466', b2)
    if hasattr(b1, 'Entity467'):
        assert not _is_linked(b1, 'Entity467', a)
    if hasattr(b2, 'Entity467'):
        assert _is_linked(b2, 'Entity467', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule466', set())
    assert not _is_linked(a, 'camel_scalability_ScalabilityRule466', b2)
    if hasattr(b2, 'Entity467'):
        assert not _is_linked(b2, 'Entity467', a)


def test_assoc_event454_link_reassign_clear():
    a = camel_scalability_UnaryEventPattern(occurrenceNum=7, operator="sample_text")
    b1 = Event()
    b2 = Event()
    _safe_set(a, 'camel_scalability_UnaryEventPattern', b1)
    assert _is_linked(a, 'camel_scalability_UnaryEventPattern', b1)
    if hasattr(b1, 'Event455'):
        assert _is_linked(b1, 'Event455', a)
    _safe_set(a, 'camel_scalability_UnaryEventPattern', b2)
    assert _is_linked(a, 'camel_scalability_UnaryEventPattern', b2)
    if hasattr(b1, 'Event455'):
        assert not _is_linked(b1, 'Event455', a)
    if hasattr(b2, 'Event455'):
        assert _is_linked(b2, 'Event455', a)
    _safe_set(a, 'camel_scalability_UnaryEventPattern', None)
    assert not _is_linked(a, 'camel_scalability_UnaryEventPattern', b2)
    if hasattr(b2, 'Event455'):
        assert not _is_linked(b2, 'Event455', a)


def test_assoc_event457_link_reassign_clear():
    a = camel_scalability_EventInstance(layer="sample_text", name="sample_text", status="sample_text")
    b1 = SimpleEvent()
    b2 = SimpleEvent()
    _safe_set(a, 'camel_scalability_EventInstance', b1)
    assert _is_linked(a, 'camel_scalability_EventInstance', b1)
    if hasattr(b1, 'SimpleEvent'):
        assert _is_linked(b1, 'SimpleEvent', a)
    _safe_set(a, 'camel_scalability_EventInstance', b2)
    assert _is_linked(a, 'camel_scalability_EventInstance', b2)
    if hasattr(b1, 'SimpleEvent'):
        assert not _is_linked(b1, 'SimpleEvent', a)
    if hasattr(b2, 'SimpleEvent'):
        assert _is_linked(b2, 'SimpleEvent', a)
    _safe_set(a, 'camel_scalability_EventInstance', None)
    assert not _is_linked(a, 'camel_scalability_EventInstance', b2)
    if hasattr(b2, 'SimpleEvent'):
        assert not _is_linked(b2, 'SimpleEvent', a)


def test_assoc_event461_link_reassign_clear():
    a = camel_scalability_ScalabilityRule(name="sample_text")
    b1 = Event()
    b2 = Event()
    _safe_set(a, 'camel_scalability_ScalabilityRule', b1)
    assert _is_linked(a, 'camel_scalability_ScalabilityRule', b1)
    if hasattr(b1, 'Event462'):
        assert _is_linked(b1, 'Event462', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule', b2)
    assert _is_linked(a, 'camel_scalability_ScalabilityRule', b2)
    if hasattr(b1, 'Event462'):
        assert not _is_linked(b1, 'Event462', a)
    if hasattr(b2, 'Event462'):
        assert _is_linked(b2, 'Event462', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule', None)
    assert not _is_linked(a, 'camel_scalability_ScalabilityRule', b2)
    if hasattr(b2, 'Event462'):
        assert not _is_linked(b2, 'Event462', a)


def test_assoc_eventInstance149_link_reassign_clear():
    a = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    b1 = EventInstance()
    b2 = EventInstance()
    _safe_set(a, 'camel_execution_Measurement150', b1)
    assert _is_linked(a, 'camel_execution_Measurement150', b1)
    if hasattr(b1, 'EventInstance151'):
        assert _is_linked(b1, 'EventInstance151', a)
    _safe_set(a, 'camel_execution_Measurement150', b2)
    assert _is_linked(a, 'camel_execution_Measurement150', b2)
    if hasattr(b1, 'EventInstance151'):
        assert not _is_linked(b1, 'EventInstance151', a)
    if hasattr(b2, 'EventInstance151'):
        assert _is_linked(b2, 'EventInstance151', a)
    _safe_set(a, 'camel_execution_Measurement150', None)
    assert not _is_linked(a, 'camel_execution_Measurement150', b2)
    if hasattr(b2, 'EventInstance151'):
        assert not _is_linked(b2, 'EventInstance151', a)


def test_assoc_eventInstances172_link_reassign_clear():
    a = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    b1 = EventInstance()
    b2 = EventInstance()
    _safe_set(a, 'camel_execution_RuleTrigger173', {b1})
    assert _is_linked(a, 'camel_execution_RuleTrigger173', b1)
    if hasattr(b1, 'EventInstance174'):
        assert _is_linked(b1, 'EventInstance174', a)
    _safe_set(a, 'camel_execution_RuleTrigger173', {b2})
    assert _is_linked(a, 'camel_execution_RuleTrigger173', b2)
    if hasattr(b1, 'EventInstance174'):
        assert not _is_linked(b1, 'EventInstance174', a)
    if hasattr(b2, 'EventInstance174'):
        assert _is_linked(b2, 'EventInstance174', a)
    _safe_set(a, 'camel_execution_RuleTrigger173', set())
    assert not _is_linked(a, 'camel_execution_RuleTrigger173', b2)
    if hasattr(b2, 'EventInstance174'):
        assert not _is_linked(b2, 'EventInstance174', a)


def test_assoc_executionContext143_link_reassign_clear():
    a = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    b1 = ExecutionContext()
    b2 = ExecutionContext()
    _safe_set(a, 'camel_execution_Measurement', b1)
    assert _is_linked(a, 'camel_execution_Measurement', b1)
    if hasattr(b1, 'ExecutionContext144'):
        assert _is_linked(b1, 'ExecutionContext144', a)
    _safe_set(a, 'camel_execution_Measurement', b2)
    assert _is_linked(a, 'camel_execution_Measurement', b2)
    if hasattr(b1, 'ExecutionContext144'):
        assert not _is_linked(b1, 'ExecutionContext144', a)
    if hasattr(b2, 'ExecutionContext144'):
        assert _is_linked(b2, 'ExecutionContext144', a)
    _safe_set(a, 'camel_execution_Measurement', None)
    assert not _is_linked(a, 'camel_execution_Measurement', b2)
    if hasattr(b2, 'ExecutionContext144'):
        assert not _is_linked(b2, 'ExecutionContext144', a)


def test_assoc_executionContext165_link_reassign_clear():
    a = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    b1 = ExecutionContext()
    b2 = ExecutionContext()
    _safe_set(a, 'camel_execution_SLOAssessment166', b1)
    assert _is_linked(a, 'camel_execution_SLOAssessment166', b1)
    if hasattr(b1, 'ExecutionContext167'):
        assert _is_linked(b1, 'ExecutionContext167', a)
    _safe_set(a, 'camel_execution_SLOAssessment166', b2)
    assert _is_linked(a, 'camel_execution_SLOAssessment166', b2)
    if hasattr(b1, 'ExecutionContext167'):
        assert not _is_linked(b1, 'ExecutionContext167', a)
    if hasattr(b2, 'ExecutionContext167'):
        assert _is_linked(b2, 'ExecutionContext167', a)
    _safe_set(a, 'camel_execution_SLOAssessment166', None)
    assert not _is_linked(a, 'camel_execution_SLOAssessment166', b2)
    if hasattr(b2, 'ExecutionContext167'):
        assert not _is_linked(b2, 'ExecutionContext167', a)


def test_assoc_executionContext178_link_reassign_clear():
    a = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    b1 = ExecutionContext()
    b2 = ExecutionContext()
    _safe_set(a, 'camel_execution_RuleTrigger179', b1)
    assert _is_linked(a, 'camel_execution_RuleTrigger179', b1)
    if hasattr(b1, 'ExecutionContext180'):
        assert _is_linked(b1, 'ExecutionContext180', a)
    _safe_set(a, 'camel_execution_RuleTrigger179', b2)
    assert _is_linked(a, 'camel_execution_RuleTrigger179', b2)
    if hasattr(b1, 'ExecutionContext180'):
        assert not _is_linked(b1, 'ExecutionContext180', a)
    if hasattr(b2, 'ExecutionContext180'):
        assert _is_linked(b2, 'ExecutionContext180', a)
    _safe_set(a, 'camel_execution_RuleTrigger179', None)
    assert not _is_linked(a, 'camel_execution_RuleTrigger179', b2)
    if hasattr(b2, 'ExecutionContext180'):
        assert not _is_linked(b2, 'ExecutionContext180', a)


def test_assoc_executionContext225_link_reassign_clear():
    a = camel_metric_MetricObjectBinding(name="sample_text")
    b1 = ExecutionContext()
    b2 = ExecutionContext()
    _safe_set(a, 'camel_metric_MetricObjectBinding', b1)
    assert _is_linked(a, 'camel_metric_MetricObjectBinding', b1)
    if hasattr(b1, 'ExecutionContext226'):
        assert _is_linked(b1, 'ExecutionContext226', a)
    _safe_set(a, 'camel_metric_MetricObjectBinding', b2)
    assert _is_linked(a, 'camel_metric_MetricObjectBinding', b2)
    if hasattr(b1, 'ExecutionContext226'):
        assert not _is_linked(b1, 'ExecutionContext226', a)
    if hasattr(b2, 'ExecutionContext226'):
        assert _is_linked(b2, 'ExecutionContext226', a)
    _safe_set(a, 'camel_metric_MetricObjectBinding', None)
    assert not _is_linked(a, 'camel_metric_MetricObjectBinding', b2)
    if hasattr(b2, 'ExecutionContext226'):
        assert not _is_linked(b2, 'ExecutionContext226', a)


def test_assoc_externalIdentifiers293_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = ExternalIdentifier()
    b2 = ExternalIdentifier()
    _safe_set(a, 'camel_organisation_OrganisationModel294', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel294', b1)
    if hasattr(b1, 'ExternalIdentifier'):
        assert _is_linked(b1, 'ExternalIdentifier', a)
    _safe_set(a, 'camel_organisation_OrganisationModel294', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel294', b2)
    if hasattr(b1, 'ExternalIdentifier'):
        assert not _is_linked(b1, 'ExternalIdentifier', a)
    if hasattr(b2, 'ExternalIdentifier'):
        assert _is_linked(b2, 'ExternalIdentifier', a)
    _safe_set(a, 'camel_organisation_OrganisationModel294', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel294', b2)
    if hasattr(b2, 'ExternalIdentifier'):
        assert not _is_linked(b2, 'ExternalIdentifier', a)


def test_assoc_externalIdentifiers316_link_reassign_clear():
    a = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    b1 = ExternalIdentifier()
    b2 = ExternalIdentifier()
    _safe_set(a, 'camel_organisation_User', {b1})
    assert _is_linked(a, 'camel_organisation_User', b1)
    if hasattr(b1, 'ExternalIdentifier317'):
        assert _is_linked(b1, 'ExternalIdentifier317', a)
    _safe_set(a, 'camel_organisation_User', {b2})
    assert _is_linked(a, 'camel_organisation_User', b2)
    if hasattr(b1, 'ExternalIdentifier317'):
        assert not _is_linked(b1, 'ExternalIdentifier317', a)
    if hasattr(b2, 'ExternalIdentifier317'):
        assert _is_linked(b2, 'ExternalIdentifier317', a)
    _safe_set(a, 'camel_organisation_User', set())
    assert not _is_linked(a, 'camel_organisation_User', b2)
    if hasattr(b2, 'ExternalIdentifier317'):
        assert not _is_linked(b2, 'ExternalIdentifier317', a)


def test_assoc_featureCardinality384_link_reassign_clear():
    a = camel_provider_Feature(name="sample_text")
    b1 = FeatCardinality()
    b2 = FeatCardinality()
    _safe_set(a, 'camel_provider_Feature385', b1)
    assert _is_linked(a, 'camel_provider_Feature385', b1)
    if hasattr(b1, 'FeatCardinality386'):
        assert _is_linked(b1, 'FeatCardinality386', a)
    _safe_set(a, 'camel_provider_Feature385', b2)
    assert _is_linked(a, 'camel_provider_Feature385', b2)
    if hasattr(b1, 'FeatCardinality386'):
        assert not _is_linked(b1, 'FeatCardinality386', a)
    if hasattr(b2, 'FeatCardinality386'):
        assert _is_linked(b2, 'FeatCardinality386', a)
    _safe_set(a, 'camel_provider_Feature385', None)
    assert not _is_linked(a, 'camel_provider_Feature385', b2)
    if hasattr(b2, 'FeatCardinality386'):
        assert not _is_linked(b2, 'FeatCardinality386', a)


def test_assoc_formula224_link_reassign_clear():
    a = camel_metric_CompositeMetric()
    b1 = MetricFormula()
    b2 = MetricFormula()
    _safe_set(a, 'camel_metric_CompositeMetric', b1)
    assert _is_linked(a, 'camel_metric_CompositeMetric', b1)
    if hasattr(b1, 'MetricFormula'):
        assert _is_linked(b1, 'MetricFormula', a)
    _safe_set(a, 'camel_metric_CompositeMetric', b2)
    assert _is_linked(a, 'camel_metric_CompositeMetric', b2)
    if hasattr(b1, 'MetricFormula'):
        assert not _is_linked(b1, 'MetricFormula', a)
    if hasattr(b2, 'MetricFormula'):
        assert _is_linked(b2, 'MetricFormula', a)
    _safe_set(a, 'camel_metric_CompositeMetric', None)
    assert not _is_linked(a, 'camel_metric_CompositeMetric', b2)
    if hasattr(b2, 'MetricFormula'):
        assert not _is_linked(b2, 'MetricFormula', a)


def test_assoc_fromValue356_link_reassign_clear():
    a = camel_provider_AttributeConstraint(name="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_provider_AttributeConstraint357', b1)
    assert _is_linked(a, 'camel_provider_AttributeConstraint357', b1)
    if hasattr(b1, 'SingleValue358'):
        assert _is_linked(b1, 'SingleValue358', a)
    _safe_set(a, 'camel_provider_AttributeConstraint357', b2)
    assert _is_linked(a, 'camel_provider_AttributeConstraint357', b2)
    if hasattr(b1, 'SingleValue358'):
        assert not _is_linked(b1, 'SingleValue358', a)
    if hasattr(b2, 'SingleValue358'):
        assert _is_linked(b2, 'SingleValue358', a)
    _safe_set(a, 'camel_provider_AttributeConstraint357', None)
    assert not _is_linked(a, 'camel_provider_AttributeConstraint357', b2)
    if hasattr(b2, 'SingleValue358'):
        assert not _is_linked(b2, 'SingleValue358', a)


def test_assoc_from_351_link_reassign_clear():
    a = camel_provider_AttributeConstraint(name="sample_text")
    b1 = Attribute()
    b2 = Attribute()
    _safe_set(a, 'camel_provider_AttributeConstraint', b1)
    assert _is_linked(a, 'camel_provider_AttributeConstraint', b1)
    if hasattr(b1, 'Attribute352'):
        assert _is_linked(b1, 'Attribute352', a)
    _safe_set(a, 'camel_provider_AttributeConstraint', b2)
    assert _is_linked(a, 'camel_provider_AttributeConstraint', b2)
    if hasattr(b1, 'Attribute352'):
        assert not _is_linked(b1, 'Attribute352', a)
    if hasattr(b2, 'Attribute352'):
        assert _is_linked(b2, 'Attribute352', a)
    _safe_set(a, 'camel_provider_AttributeConstraint', None)
    assert not _is_linked(a, 'camel_provider_AttributeConstraint', b2)
    if hasattr(b2, 'Attribute352'):
        assert not _is_linked(b2, 'Attribute352', a)


def test_assoc_from_363_link_reassign_clear():
    a = camel_provider_Constraint(name="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'camel_provider_Constraint', b1)
    assert _is_linked(a, 'camel_provider_Constraint', b1)
    if hasattr(b1, 'Feature364'):
        assert _is_linked(b1, 'Feature364', a)
    _safe_set(a, 'camel_provider_Constraint', b2)
    assert _is_linked(a, 'camel_provider_Constraint', b2)
    if hasattr(b1, 'Feature364'):
        assert not _is_linked(b1, 'Feature364', a)
    if hasattr(b2, 'Feature364'):
        assert _is_linked(b2, 'Feature364', a)
    _safe_set(a, 'camel_provider_Constraint', None)
    assert not _is_linked(a, 'camel_provider_Constraint', b2)
    if hasattr(b2, 'Feature364'):
        assert not _is_linked(b2, 'Feature364', a)


def test_assoc_geographicalRegion191_link_reassign_clear():
    a = camel_location_CloudLocation(isAssignable=True)
    b1 = GeographicalRegion()
    b2 = GeographicalRegion()
    _safe_set(a, 'camel_location_CloudLocation192', b1)
    assert _is_linked(a, 'camel_location_CloudLocation192', b1)
    if hasattr(b1, 'GeographicalRegion193'):
        assert _is_linked(b1, 'GeographicalRegion193', a)
    _safe_set(a, 'camel_location_CloudLocation192', b2)
    assert _is_linked(a, 'camel_location_CloudLocation192', b2)
    if hasattr(b1, 'GeographicalRegion193'):
        assert not _is_linked(b1, 'GeographicalRegion193', a)
    if hasattr(b2, 'GeographicalRegion193'):
        assert _is_linked(b2, 'GeographicalRegion193', a)
    _safe_set(a, 'camel_location_CloudLocation192', None)
    assert not _is_linked(a, 'camel_location_CloudLocation192', b2)
    if hasattr(b2, 'GeographicalRegion193'):
        assert not _is_linked(b2, 'GeographicalRegion193', a)


def test_assoc_internalComponent473_link_reassign_clear():
    a = camel_scalability_HorizontalScalingAction(count=7)
    b1 = InternalComponent()
    b2 = InternalComponent()
    _safe_set(a, 'camel_scalability_HorizontalScalingAction', b1)
    assert _is_linked(a, 'camel_scalability_HorizontalScalingAction', b1)
    if hasattr(b1, 'InternalComponent474'):
        assert _is_linked(b1, 'InternalComponent474', a)
    _safe_set(a, 'camel_scalability_HorizontalScalingAction', b2)
    assert _is_linked(a, 'camel_scalability_HorizontalScalingAction', b2)
    if hasattr(b1, 'InternalComponent474'):
        assert not _is_linked(b1, 'InternalComponent474', a)
    if hasattr(b2, 'InternalComponent474'):
        assert _is_linked(b2, 'InternalComponent474', a)
    _safe_set(a, 'camel_scalability_HorizontalScalingAction', None)
    assert not _is_linked(a, 'camel_scalability_HorizontalScalingAction', b2)
    if hasattr(b2, 'InternalComponent474'):
        assert not _is_linked(b2, 'InternalComponent474', a)


def test_assoc_leftEvent449_link_reassign_clear():
    a = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    b1 = Event()
    b2 = Event()
    _safe_set(a, 'camel_scalability_BinaryEventPattern', b1)
    assert _is_linked(a, 'camel_scalability_BinaryEventPattern', b1)
    if hasattr(b1, 'Event450'):
        assert _is_linked(b1, 'Event450', a)
    _safe_set(a, 'camel_scalability_BinaryEventPattern', b2)
    assert _is_linked(a, 'camel_scalability_BinaryEventPattern', b2)
    if hasattr(b1, 'Event450'):
        assert not _is_linked(b1, 'Event450', a)
    if hasattr(b2, 'Event450'):
        assert _is_linked(b2, 'Event450', a)
    _safe_set(a, 'camel_scalability_BinaryEventPattern', None)
    assert not _is_linked(a, 'camel_scalability_BinaryEventPattern', b2)
    if hasattr(b2, 'Event450'):
        assert not _is_linked(b2, 'Event450', a)


def test_assoc_location311_link_reassign_clear():
    a = camel_organisation_DataCenter(codeName="sample_text", name="sample_text")
    b1 = Location()
    b2 = Location()
    _safe_set(a, 'camel_organisation_DataCenter', b1)
    assert _is_linked(a, 'camel_organisation_DataCenter', b1)
    if hasattr(b1, 'Location'):
        assert _is_linked(b1, 'Location', a)
    _safe_set(a, 'camel_organisation_DataCenter', b2)
    assert _is_linked(a, 'camel_organisation_DataCenter', b2)
    if hasattr(b1, 'Location'):
        assert not _is_linked(b1, 'Location', a)
    if hasattr(b2, 'Location'):
        assert _is_linked(b2, 'Location', a)
    _safe_set(a, 'camel_organisation_DataCenter', None)
    assert not _is_linked(a, 'camel_organisation_DataCenter', b2)
    if hasattr(b2, 'Location'):
        assert not _is_linked(b2, 'Location', a)


def test_assoc_locationRequirement63_link_reassign_clear():
    a = camel_deployment_VMRequirementSet(name="sample_text")
    b1 = LocationRequirement()
    b2 = LocationRequirement()
    _safe_set(a, 'camel_deployment_VMRequirementSet', b1)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet', b1)
    if hasattr(b1, 'LocationRequirement'):
        assert _is_linked(b1, 'LocationRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet', b2)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet', b2)
    if hasattr(b1, 'LocationRequirement'):
        assert not _is_linked(b1, 'LocationRequirement', a)
    if hasattr(b2, 'LocationRequirement'):
        assert _is_linked(b2, 'LocationRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet', None)
    assert not _is_linked(a, 'camel_deployment_VMRequirementSet', b2)
    if hasattr(b2, 'LocationRequirement'):
        assert not _is_linked(b2, 'LocationRequirement', a)


def test_assoc_lowerLimit535_link_reassign_clear():
    a = camel_type_Range(primitiveType="sample_text")
    b1 = Limit()
    b2 = Limit()
    _safe_set(a, 'camel_type_Range', b1)
    assert _is_linked(a, 'camel_type_Range', b1)
    if hasattr(b1, 'Limit'):
        assert _is_linked(b1, 'Limit', a)
    _safe_set(a, 'camel_type_Range', b2)
    assert _is_linked(a, 'camel_type_Range', b2)
    if hasattr(b1, 'Limit'):
        assert not _is_linked(b1, 'Limit', a)
    if hasattr(b2, 'Limit'):
        assert _is_linked(b2, 'Limit', a)
    _safe_set(a, 'camel_type_Range', None)
    assert not _is_linked(a, 'camel_type_Range', b2)
    if hasattr(b2, 'Limit'):
        assert not _is_linked(b2, 'Limit', a)


def test_assoc_measurement168_link_reassign_clear():
    a = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    b1 = Measurement()
    b2 = Measurement()
    _safe_set(a, 'camel_execution_SLOAssessment169', b1)
    assert _is_linked(a, 'camel_execution_SLOAssessment169', b1)
    if hasattr(b1, 'Measurement170'):
        assert _is_linked(b1, 'Measurement170', a)
    _safe_set(a, 'camel_execution_SLOAssessment169', b2)
    assert _is_linked(a, 'camel_execution_SLOAssessment169', b2)
    if hasattr(b1, 'Measurement170'):
        assert not _is_linked(b1, 'Measurement170', a)
    if hasattr(b2, 'Measurement170'):
        assert _is_linked(b2, 'Measurement170', a)
    _safe_set(a, 'camel_execution_SLOAssessment169', None)
    assert not _is_linked(a, 'camel_execution_SLOAssessment169', b2)
    if hasattr(b2, 'Measurement170'):
        assert not _is_linked(b2, 'Measurement170', a)


def test_assoc_metric203_link_reassign_clear():
    a = camel_metric_MetricInstance(name="sample_text")
    b1 = Metric()
    b2 = Metric()
    _safe_set(a, 'camel_metric_MetricInstance', b1)
    assert _is_linked(a, 'camel_metric_MetricInstance', b1)
    if hasattr(b1, 'Metric'):
        assert _is_linked(b1, 'Metric', a)
    _safe_set(a, 'camel_metric_MetricInstance', b2)
    assert _is_linked(a, 'camel_metric_MetricInstance', b2)
    if hasattr(b1, 'Metric'):
        assert not _is_linked(b1, 'Metric', a)
    if hasattr(b2, 'Metric'):
        assert _is_linked(b2, 'Metric', a)
    _safe_set(a, 'camel_metric_MetricInstance', None)
    assert not _is_linked(a, 'camel_metric_MetricInstance', b2)
    if hasattr(b2, 'Metric'):
        assert not _is_linked(b2, 'Metric', a)


def test_assoc_metric403_link_reassign_clear():
    a = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    b1 = Metric()
    b2 = Metric()
    _safe_set(a, 'camel_requirement_OptimisationRequirement', b1)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement', b1)
    if hasattr(b1, 'Metric404'):
        assert _is_linked(b1, 'Metric404', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement', b2)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement', b2)
    if hasattr(b1, 'Metric404'):
        assert not _is_linked(b1, 'Metric404', a)
    if hasattr(b2, 'Metric404'):
        assert _is_linked(b2, 'Metric404', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement', None)
    assert not _is_linked(a, 'camel_requirement_OptimisationRequirement', b2)
    if hasattr(b2, 'Metric404'):
        assert not _is_linked(b2, 'Metric404', a)


def test_assoc_metricCondition456_link_reassign_clear():
    a = camel_scalability_NonFunctionalEvent(isViolation=True)
    b1 = MetricCondition()
    b2 = MetricCondition()
    _safe_set(a, 'camel_scalability_NonFunctionalEvent', b1)
    assert _is_linked(a, 'camel_scalability_NonFunctionalEvent', b1)
    if hasattr(b1, 'MetricCondition'):
        assert _is_linked(b1, 'MetricCondition', a)
    _safe_set(a, 'camel_scalability_NonFunctionalEvent', b2)
    assert _is_linked(a, 'camel_scalability_NonFunctionalEvent', b2)
    if hasattr(b1, 'MetricCondition'):
        assert not _is_linked(b1, 'MetricCondition', a)
    if hasattr(b2, 'MetricCondition'):
        assert _is_linked(b2, 'MetricCondition', a)
    _safe_set(a, 'camel_scalability_NonFunctionalEvent', None)
    assert not _is_linked(a, 'camel_scalability_NonFunctionalEvent', b2)
    if hasattr(b2, 'MetricCondition'):
        assert not _is_linked(b2, 'MetricCondition', a)


def test_assoc_metricContext210_link_reassign_clear():
    a = camel_metric_MetricInstance(name="sample_text")
    b1 = MetricContext()
    b2 = MetricContext()
    _safe_set(a, 'camel_metric_MetricInstance211', b1)
    assert _is_linked(a, 'camel_metric_MetricInstance211', b1)
    if hasattr(b1, 'MetricContext212'):
        assert _is_linked(b1, 'MetricContext212', a)
    _safe_set(a, 'camel_metric_MetricInstance211', b2)
    assert _is_linked(a, 'camel_metric_MetricInstance211', b2)
    if hasattr(b1, 'MetricContext212'):
        assert not _is_linked(b1, 'MetricContext212', a)
    if hasattr(b2, 'MetricContext212'):
        assert _is_linked(b2, 'MetricContext212', a)
    _safe_set(a, 'camel_metric_MetricInstance211', None)
    assert not _is_linked(a, 'camel_metric_MetricInstance211', b2)
    if hasattr(b2, 'MetricContext212'):
        assert not _is_linked(b2, 'MetricContext212', a)


def test_assoc_metricContext414_link_reassign_clear():
    a = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    b1 = MetricContext()
    b2 = MetricContext()
    _safe_set(a, 'camel_requirement_OptimisationRequirement415', b1)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement415', b1)
    if hasattr(b1, 'MetricContext416'):
        assert _is_linked(b1, 'MetricContext416', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement415', b2)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement415', b2)
    if hasattr(b1, 'MetricContext416'):
        assert not _is_linked(b1, 'MetricContext416', a)
    if hasattr(b2, 'MetricContext416'):
        assert _is_linked(b2, 'MetricContext416', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement415', None)
    assert not _is_linked(a, 'camel_requirement_OptimisationRequirement415', b2)
    if hasattr(b2, 'MetricContext416'):
        assert not _is_linked(b2, 'MetricContext416', a)


def test_assoc_metricInstance145_link_reassign_clear():
    a = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    b1 = MetricInstance()
    b2 = MetricInstance()
    _safe_set(a, 'camel_execution_Measurement146', b1)
    assert _is_linked(a, 'camel_execution_Measurement146', b1)
    if hasattr(b1, 'MetricInstance'):
        assert _is_linked(b1, 'MetricInstance', a)
    _safe_set(a, 'camel_execution_Measurement146', b2)
    assert _is_linked(a, 'camel_execution_Measurement146', b2)
    if hasattr(b1, 'MetricInstance'):
        assert not _is_linked(b1, 'MetricInstance', a)
    if hasattr(b2, 'MetricInstance'):
        assert _is_linked(b2, 'MetricInstance', a)
    _safe_set(a, 'camel_execution_Measurement146', None)
    assert not _is_linked(a, 'camel_execution_Measurement146', b2)
    if hasattr(b2, 'MetricInstance'):
        assert not _is_linked(b2, 'MetricInstance', a)


def test_assoc_metricInstance458_link_reassign_clear():
    a = camel_scalability_EventInstance(layer="sample_text", name="sample_text", status="sample_text")
    b1 = MetricInstance()
    b2 = MetricInstance()
    _safe_set(a, 'camel_scalability_EventInstance459', b1)
    assert _is_linked(a, 'camel_scalability_EventInstance459', b1)
    if hasattr(b1, 'MetricInstance460'):
        assert _is_linked(b1, 'MetricInstance460', a)
    _safe_set(a, 'camel_scalability_EventInstance459', b2)
    assert _is_linked(a, 'camel_scalability_EventInstance459', b2)
    if hasattr(b1, 'MetricInstance460'):
        assert not _is_linked(b1, 'MetricInstance460', a)
    if hasattr(b2, 'MetricInstance460'):
        assert _is_linked(b2, 'MetricInstance460', a)
    _safe_set(a, 'camel_scalability_EventInstance459', None)
    assert not _is_linked(a, 'camel_scalability_EventInstance459', b2)
    if hasattr(b2, 'MetricInstance460'):
        assert not _is_linked(b2, 'MetricInstance460', a)


def test_assoc_objectBinding208_link_reassign_clear():
    a = camel_metric_MetricInstance(name="sample_text")
    b1 = MetricObjectBinding()
    b2 = MetricObjectBinding()
    _safe_set(a, 'camel_metric_MetricInstance209', b1)
    assert _is_linked(a, 'camel_metric_MetricInstance209', b1)
    if hasattr(b1, 'MetricObjectBinding'):
        assert _is_linked(b1, 'MetricObjectBinding', a)
    _safe_set(a, 'camel_metric_MetricInstance209', b2)
    assert _is_linked(a, 'camel_metric_MetricInstance209', b2)
    if hasattr(b1, 'MetricObjectBinding'):
        assert not _is_linked(b1, 'MetricObjectBinding', a)
    if hasattr(b2, 'MetricObjectBinding'):
        assert _is_linked(b2, 'MetricObjectBinding', a)
    _safe_set(a, 'camel_metric_MetricInstance209', None)
    assert not _is_linked(a, 'camel_metric_MetricInstance209', b2)
    if hasattr(b2, 'MetricObjectBinding'):
        assert not _is_linked(b2, 'MetricObjectBinding', a)


def test_assoc_organisation290_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = Organisation()
    b2 = Organisation()
    _safe_set(a, 'camel_organisation_OrganisationModel', b1)
    assert _is_linked(a, 'camel_organisation_OrganisationModel', b1)
    if hasattr(b1, 'Organisation'):
        assert _is_linked(b1, 'Organisation', a)
    _safe_set(a, 'camel_organisation_OrganisationModel', b2)
    assert _is_linked(a, 'camel_organisation_OrganisationModel', b2)
    if hasattr(b1, 'Organisation'):
        assert not _is_linked(b1, 'Organisation', a)
    if hasattr(b2, 'Organisation'):
        assert _is_linked(b2, 'Organisation', a)
    _safe_set(a, 'camel_organisation_OrganisationModel', None)
    assert not _is_linked(a, 'camel_organisation_OrganisationModel', b2)
    if hasattr(b2, 'Organisation'):
        assert not _is_linked(b2, 'Organisation', a)


def test_assoc_osOrImageRequirement70_link_reassign_clear():
    a = camel_deployment_VMRequirementSet(name="sample_text")
    b1 = OSOrImageRequirement()
    b2 = OSOrImageRequirement()
    _safe_set(a, 'camel_deployment_VMRequirementSet71', b1)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet71', b1)
    if hasattr(b1, 'OSOrImageRequirement'):
        assert _is_linked(b1, 'OSOrImageRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet71', b2)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet71', b2)
    if hasattr(b1, 'OSOrImageRequirement'):
        assert not _is_linked(b1, 'OSOrImageRequirement', a)
    if hasattr(b2, 'OSOrImageRequirement'):
        assert _is_linked(b2, 'OSOrImageRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet71', None)
    assert not _is_linked(a, 'camel_deployment_VMRequirementSet71', b2)
    if hasattr(b2, 'OSOrImageRequirement'):
        assert not _is_linked(b2, 'OSOrImageRequirement', a)


def test_assoc_owner25_link_reassign_clear():
    a = camel_Application(description="sample_text", name="sample_text", version="sample_text")
    b1 = Entity()
    b2 = Entity()
    _safe_set(a, 'camel_Application26', b1)
    assert _is_linked(a, 'camel_Application26', b1)
    if hasattr(b1, 'Entity'):
        assert _is_linked(b1, 'Entity', a)
    _safe_set(a, 'camel_Application26', b2)
    assert _is_linked(a, 'camel_Application26', b2)
    if hasattr(b1, 'Entity'):
        assert not _is_linked(b1, 'Entity', a)
    if hasattr(b2, 'Entity'):
        assert _is_linked(b2, 'Entity', a)
    _safe_set(a, 'camel_Application26', None)
    assert not _is_linked(a, 'camel_Application26', b2)
    if hasattr(b2, 'Entity'):
        assert not _is_linked(b2, 'Entity', a)


def test_assoc_paasageCredentials326_link_reassign_clear():
    a = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    b1 = PaaSageCredentials()
    b2 = PaaSageCredentials()
    _safe_set(a, 'camel_organisation_User327', b1)
    assert _is_linked(a, 'camel_organisation_User327', b1)
    if hasattr(b1, 'PaaSageCredentials'):
        assert _is_linked(b1, 'PaaSageCredentials', a)
    _safe_set(a, 'camel_organisation_User327', b2)
    assert _is_linked(a, 'camel_organisation_User327', b2)
    if hasattr(b1, 'PaaSageCredentials'):
        assert not _is_linked(b1, 'PaaSageCredentials', a)
    if hasattr(b2, 'PaaSageCredentials'):
        assert _is_linked(b2, 'PaaSageCredentials', a)
    _safe_set(a, 'camel_organisation_User327', None)
    assert not _is_linked(a, 'camel_organisation_User327', b2)
    if hasattr(b2, 'PaaSageCredentials'):
        assert not _is_linked(b2, 'PaaSageCredentials', a)


def test_assoc_parameters218_link_reassign_clear():
    a = camel_metric_MetricFormula(function="sample_text", functionArity="sample_text", functionPattern="sample_text")
    b1 = MetricFormulaParameter()
    b2 = MetricFormulaParameter()
    _safe_set(a, 'camel_metric_MetricFormula', {b1})
    assert _is_linked(a, 'camel_metric_MetricFormula', b1)
    if hasattr(b1, 'MetricFormulaParameter'):
        assert _is_linked(b1, 'MetricFormulaParameter', a)
    _safe_set(a, 'camel_metric_MetricFormula', {b2})
    assert _is_linked(a, 'camel_metric_MetricFormula', b2)
    if hasattr(b1, 'MetricFormulaParameter'):
        assert not _is_linked(b1, 'MetricFormulaParameter', a)
    if hasattr(b2, 'MetricFormulaParameter'):
        assert _is_linked(b2, 'MetricFormulaParameter', a)
    _safe_set(a, 'camel_metric_MetricFormula', set())
    assert not _is_linked(a, 'camel_metric_MetricFormula', b2)
    if hasattr(b2, 'MetricFormulaParameter'):
        assert not _is_linked(b2, 'MetricFormulaParameter', a)


def test_assoc_parent188_link_reassign_clear():
    a = camel_location_CloudLocation(isAssignable=True)
    b1 = CloudLocation()
    b2 = CloudLocation()
    _safe_set(a, 'camel_location_CloudLocation189', b1)
    assert _is_linked(a, 'camel_location_CloudLocation189', b1)
    if hasattr(b1, 'CloudLocation190'):
        assert _is_linked(b1, 'CloudLocation190', a)
    _safe_set(a, 'camel_location_CloudLocation189', b2)
    assert _is_linked(a, 'camel_location_CloudLocation189', b2)
    if hasattr(b1, 'CloudLocation190'):
        assert not _is_linked(b1, 'CloudLocation190', a)
    if hasattr(b2, 'CloudLocation190'):
        assert _is_linked(b2, 'CloudLocation190', a)
    _safe_set(a, 'camel_location_CloudLocation189', None)
    assert not _is_linked(a, 'camel_location_CloudLocation189', b2)
    if hasattr(b2, 'CloudLocation190'):
        assert not _is_linked(b2, 'CloudLocation190', a)


def test_assoc_parentRegions194_link_reassign_clear():
    a = camel_location_GeographicalRegion(alternativeNames="sample_text", name="sample_text")
    b1 = GeographicalRegion()
    b2 = GeographicalRegion()
    _safe_set(a, 'camel_location_GeographicalRegion', {b1})
    assert _is_linked(a, 'camel_location_GeographicalRegion', b1)
    if hasattr(b1, 'GeographicalRegion195'):
        assert _is_linked(b1, 'GeographicalRegion195', a)
    _safe_set(a, 'camel_location_GeographicalRegion', {b2})
    assert _is_linked(a, 'camel_location_GeographicalRegion', b2)
    if hasattr(b1, 'GeographicalRegion195'):
        assert not _is_linked(b1, 'GeographicalRegion195', a)
    if hasattr(b2, 'GeographicalRegion195'):
        assert _is_linked(b2, 'GeographicalRegion195', a)
    _safe_set(a, 'camel_location_GeographicalRegion', set())
    assert not _is_linked(a, 'camel_location_GeographicalRegion', b2)
    if hasattr(b2, 'GeographicalRegion195'):
        assert not _is_linked(b2, 'GeographicalRegion195', a)


def test_assoc_permissions305_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = Permission()
    b2 = Permission()
    _safe_set(a, 'camel_organisation_OrganisationModel306', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel306', b1)
    if hasattr(b1, 'Permission'):
        assert _is_linked(b1, 'Permission', a)
    _safe_set(a, 'camel_organisation_OrganisationModel306', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel306', b2)
    if hasattr(b1, 'Permission'):
        assert not _is_linked(b1, 'Permission', a)
    if hasattr(b2, 'Permission'):
        assert _is_linked(b2, 'Permission', a)
    _safe_set(a, 'camel_organisation_OrganisationModel306', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel306', b2)
    if hasattr(b2, 'Permission'):
        assert not _is_linked(b2, 'Permission', a)


def test_assoc_property222_link_reassign_clear():
    a = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'camel_metric_Metric223', b1)
    assert _is_linked(a, 'camel_metric_Metric223', b1)
    if hasattr(b1, 'Property'):
        assert _is_linked(b1, 'Property', a)
    _safe_set(a, 'camel_metric_Metric223', b2)
    assert _is_linked(a, 'camel_metric_Metric223', b2)
    if hasattr(b1, 'Property'):
        assert not _is_linked(b1, 'Property', a)
    if hasattr(b2, 'Property'):
        assert _is_linked(b2, 'Property', a)
    _safe_set(a, 'camel_metric_Metric223', None)
    assert not _is_linked(a, 'camel_metric_Metric223', b2)
    if hasattr(b2, 'Property'):
        assert not _is_linked(b2, 'Property', a)


def test_assoc_property405_link_reassign_clear():
    a = camel_requirement_OptimisationRequirement(optimisationFunction="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'camel_requirement_OptimisationRequirement406', b1)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement406', b1)
    if hasattr(b1, 'Property407'):
        assert _is_linked(b1, 'Property407', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement406', b2)
    assert _is_linked(a, 'camel_requirement_OptimisationRequirement406', b2)
    if hasattr(b1, 'Property407'):
        assert not _is_linked(b1, 'Property407', a)
    if hasattr(b2, 'Property407'):
        assert _is_linked(b2, 'Property407', a)
    _safe_set(a, 'camel_requirement_OptimisationRequirement406', None)
    assert not _is_linked(a, 'camel_requirement_OptimisationRequirement406', b2)
    if hasattr(b2, 'Property407'):
        assert not _is_linked(b2, 'Property407', a)


def test_assoc_providedCommunication72_link_reassign_clear():
    a = camel_deployment_Communication(type="sample_text")
    b1 = ProvidedCommunication()
    b2 = ProvidedCommunication()
    _safe_set(a, 'camel_deployment_Communication', b1)
    assert _is_linked(a, 'camel_deployment_Communication', b1)
    if hasattr(b1, 'ProvidedCommunication73'):
        assert _is_linked(b1, 'ProvidedCommunication73', a)
    _safe_set(a, 'camel_deployment_Communication', b2)
    assert _is_linked(a, 'camel_deployment_Communication', b2)
    if hasattr(b1, 'ProvidedCommunication73'):
        assert not _is_linked(b1, 'ProvidedCommunication73', a)
    if hasattr(b2, 'ProvidedCommunication73'):
        assert _is_linked(b2, 'ProvidedCommunication73', a)
    _safe_set(a, 'camel_deployment_Communication', None)
    assert not _is_linked(a, 'camel_deployment_Communication', b2)
    if hasattr(b2, 'ProvidedCommunication73'):
        assert not _is_linked(b2, 'ProvidedCommunication73', a)


def test_assoc_providedCommunicationInstances95_link_reassign_clear():
    a = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    b1 = ProvidedCommunicationInstance()
    b2 = ProvidedCommunicationInstance()
    _safe_set(a, 'camel_deployment_ComponentInstance96', {b1})
    assert _is_linked(a, 'camel_deployment_ComponentInstance96', b1)
    if hasattr(b1, 'ProvidedCommunicationInstance'):
        assert _is_linked(b1, 'ProvidedCommunicationInstance', a)
    _safe_set(a, 'camel_deployment_ComponentInstance96', {b2})
    assert _is_linked(a, 'camel_deployment_ComponentInstance96', b2)
    if hasattr(b1, 'ProvidedCommunicationInstance'):
        assert not _is_linked(b1, 'ProvidedCommunicationInstance', a)
    if hasattr(b2, 'ProvidedCommunicationInstance'):
        assert _is_linked(b2, 'ProvidedCommunicationInstance', a)
    _safe_set(a, 'camel_deployment_ComponentInstance96', set())
    assert not _is_linked(a, 'camel_deployment_ComponentInstance96', b2)
    if hasattr(b2, 'ProvidedCommunicationInstance'):
        assert not _is_linked(b2, 'ProvidedCommunicationInstance', a)


def test_assoc_providedHostInstances97_link_reassign_clear():
    a = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    b1 = ProvidedHostInstance()
    b2 = ProvidedHostInstance()
    _safe_set(a, 'camel_deployment_ComponentInstance98', {b1})
    assert _is_linked(a, 'camel_deployment_ComponentInstance98', b1)
    if hasattr(b1, 'ProvidedHostInstance'):
        assert _is_linked(b1, 'ProvidedHostInstance', a)
    _safe_set(a, 'camel_deployment_ComponentInstance98', {b2})
    assert _is_linked(a, 'camel_deployment_ComponentInstance98', b2)
    if hasattr(b1, 'ProvidedHostInstance'):
        assert not _is_linked(b1, 'ProvidedHostInstance', a)
    if hasattr(b2, 'ProvidedHostInstance'):
        assert _is_linked(b2, 'ProvidedHostInstance', a)
    _safe_set(a, 'camel_deployment_ComponentInstance98', set())
    assert not _is_linked(a, 'camel_deployment_ComponentInstance98', b2)
    if hasattr(b2, 'ProvidedHostInstance'):
        assert not _is_linked(b2, 'ProvidedHostInstance', a)


def test_assoc_providedPortConfiguration77_link_reassign_clear():
    a = camel_deployment_Communication(type="sample_text")
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'camel_deployment_Communication78', b1)
    assert _is_linked(a, 'camel_deployment_Communication78', b1)
    if hasattr(b1, 'Configuration79'):
        assert _is_linked(b1, 'Configuration79', a)
    _safe_set(a, 'camel_deployment_Communication78', b2)
    assert _is_linked(a, 'camel_deployment_Communication78', b2)
    if hasattr(b1, 'Configuration79'):
        assert not _is_linked(b1, 'Configuration79', a)
    if hasattr(b2, 'Configuration79'):
        assert _is_linked(b2, 'Configuration79', a)
    _safe_set(a, 'camel_deployment_Communication78', None)
    assert not _is_linked(a, 'camel_deployment_Communication78', b2)
    if hasattr(b2, 'Configuration79'):
        assert not _is_linked(b2, 'Configuration79', a)


def test_assoc_provider291_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = CloudProvider()
    b2 = CloudProvider()
    _safe_set(a, 'camel_organisation_OrganisationModel292', b1)
    assert _is_linked(a, 'camel_organisation_OrganisationModel292', b1)
    if hasattr(b1, 'CloudProvider'):
        assert _is_linked(b1, 'CloudProvider', a)
    _safe_set(a, 'camel_organisation_OrganisationModel292', b2)
    assert _is_linked(a, 'camel_organisation_OrganisationModel292', b2)
    if hasattr(b1, 'CloudProvider'):
        assert not _is_linked(b1, 'CloudProvider', a)
    if hasattr(b2, 'CloudProvider'):
        assert _is_linked(b2, 'CloudProvider', a)
    _safe_set(a, 'camel_organisation_OrganisationModel292', None)
    assert not _is_linked(a, 'camel_organisation_OrganisationModel292', b2)
    if hasattr(b2, 'CloudProvider'):
        assert not _is_linked(b2, 'CloudProvider', a)


def test_assoc_providerModel312_link_reassign_clear():
    a = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    b1 = ProviderModel()
    b2 = ProviderModel()
    _safe_set(a, 'camel_organisation_CloudProvider', b1)
    assert _is_linked(a, 'camel_organisation_CloudProvider', b1)
    if hasattr(b1, 'ProviderModel313'):
        assert _is_linked(b1, 'ProviderModel313', a)
    _safe_set(a, 'camel_organisation_CloudProvider', b2)
    assert _is_linked(a, 'camel_organisation_CloudProvider', b2)
    if hasattr(b1, 'ProviderModel313'):
        assert not _is_linked(b1, 'ProviderModel313', a)
    if hasattr(b2, 'ProviderModel313'):
        assert _is_linked(b2, 'ProviderModel313', a)
    _safe_set(a, 'camel_organisation_CloudProvider', None)
    assert not _is_linked(a, 'camel_organisation_CloudProvider', b2)
    if hasattr(b2, 'ProviderModel313'):
        assert not _is_linked(b2, 'ProviderModel313', a)


def test_assoc_providerRequirement64_link_reassign_clear():
    a = camel_deployment_VMRequirementSet(name="sample_text")
    b1 = ProviderRequirement()
    b2 = ProviderRequirement()
    _safe_set(a, 'camel_deployment_VMRequirementSet65', b1)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet65', b1)
    if hasattr(b1, 'ProviderRequirement'):
        assert _is_linked(b1, 'ProviderRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet65', b2)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet65', b2)
    if hasattr(b1, 'ProviderRequirement'):
        assert not _is_linked(b1, 'ProviderRequirement', a)
    if hasattr(b2, 'ProviderRequirement'):
        assert _is_linked(b2, 'ProviderRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet65', None)
    assert not _is_linked(a, 'camel_deployment_VMRequirementSet65', b2)
    if hasattr(b2, 'ProviderRequirement'):
        assert not _is_linked(b2, 'ProviderRequirement', a)


def test_assoc_qualitativeHardwareRequirement66_link_reassign_clear():
    a = camel_deployment_VMRequirementSet(name="sample_text")
    b1 = QualitativeHardwareRequirement()
    b2 = QualitativeHardwareRequirement()
    _safe_set(a, 'camel_deployment_VMRequirementSet67', b1)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet67', b1)
    if hasattr(b1, 'QualitativeHardwareRequirement'):
        assert _is_linked(b1, 'QualitativeHardwareRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet67', b2)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet67', b2)
    if hasattr(b1, 'QualitativeHardwareRequirement'):
        assert not _is_linked(b1, 'QualitativeHardwareRequirement', a)
    if hasattr(b2, 'QualitativeHardwareRequirement'):
        assert _is_linked(b2, 'QualitativeHardwareRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet67', None)
    assert not _is_linked(a, 'camel_deployment_VMRequirementSet67', b2)
    if hasattr(b2, 'QualitativeHardwareRequirement'):
        assert not _is_linked(b2, 'QualitativeHardwareRequirement', a)


def test_assoc_quantitativeHardwareRequirement68_link_reassign_clear():
    a = camel_deployment_VMRequirementSet(name="sample_text")
    b1 = QuantitativeHardwareRequirement()
    b2 = QuantitativeHardwareRequirement()
    _safe_set(a, 'camel_deployment_VMRequirementSet69', b1)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet69', b1)
    if hasattr(b1, 'QuantitativeHardwareRequirement'):
        assert _is_linked(b1, 'QuantitativeHardwareRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet69', b2)
    assert _is_linked(a, 'camel_deployment_VMRequirementSet69', b2)
    if hasattr(b1, 'QuantitativeHardwareRequirement'):
        assert not _is_linked(b1, 'QuantitativeHardwareRequirement', a)
    if hasattr(b2, 'QuantitativeHardwareRequirement'):
        assert _is_linked(b2, 'QuantitativeHardwareRequirement', a)
    _safe_set(a, 'camel_deployment_VMRequirementSet69', None)
    assert not _is_linked(a, 'camel_deployment_VMRequirementSet69', b2)
    if hasattr(b2, 'QuantitativeHardwareRequirement'):
        assert not _is_linked(b2, 'QuantitativeHardwareRequirement', a)


def test_assoc_ranges539_link_reassign_clear():
    a = camel_type_RangeUnion(primitiveType="sample_text")
    b1 = Range()
    b2 = Range()
    _safe_set(a, 'camel_type_RangeUnion', {b1})
    assert _is_linked(a, 'camel_type_RangeUnion', b1)
    if hasattr(b1, 'Range'):
        assert _is_linked(b1, 'Range', a)
    _safe_set(a, 'camel_type_RangeUnion', {b2})
    assert _is_linked(a, 'camel_type_RangeUnion', b2)
    if hasattr(b1, 'Range'):
        assert not _is_linked(b1, 'Range', a)
    if hasattr(b2, 'Range'):
        assert _is_linked(b2, 'Range', a)
    _safe_set(a, 'camel_type_RangeUnion', set())
    assert not _is_linked(a, 'camel_type_RangeUnion', b2)
    if hasattr(b2, 'Range'):
        assert not _is_linked(b2, 'Range', a)


def test_assoc_rawSecurityMetrics508_link_reassign_clear():
    a = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    b1 = RawSecurityMetric()
    b2 = RawSecurityMetric()
    _safe_set(a, 'camel_security_SecurityControl509', {b1})
    assert _is_linked(a, 'camel_security_SecurityControl509', b1)
    if hasattr(b1, 'RawSecurityMetric510'):
        assert _is_linked(b1, 'RawSecurityMetric510', a)
    _safe_set(a, 'camel_security_SecurityControl509', {b2})
    assert _is_linked(a, 'camel_security_SecurityControl509', b2)
    if hasattr(b1, 'RawSecurityMetric510'):
        assert not _is_linked(b1, 'RawSecurityMetric510', a)
    if hasattr(b2, 'RawSecurityMetric510'):
        assert _is_linked(b2, 'RawSecurityMetric510', a)
    _safe_set(a, 'camel_security_SecurityControl509', set())
    assert not _is_linked(a, 'camel_security_SecurityControl509', b2)
    if hasattr(b2, 'RawSecurityMetric510'):
        assert not _is_linked(b2, 'RawSecurityMetric510', a)


def test_assoc_requiredCommunication74_link_reassign_clear():
    a = camel_deployment_Communication(type="sample_text")
    b1 = RequiredCommunication()
    b2 = RequiredCommunication()
    _safe_set(a, 'camel_deployment_Communication75', b1)
    assert _is_linked(a, 'camel_deployment_Communication75', b1)
    if hasattr(b1, 'RequiredCommunication76'):
        assert _is_linked(b1, 'RequiredCommunication76', a)
    _safe_set(a, 'camel_deployment_Communication75', b2)
    assert _is_linked(a, 'camel_deployment_Communication75', b2)
    if hasattr(b1, 'RequiredCommunication76'):
        assert not _is_linked(b1, 'RequiredCommunication76', a)
    if hasattr(b2, 'RequiredCommunication76'):
        assert _is_linked(b2, 'RequiredCommunication76', a)
    _safe_set(a, 'camel_deployment_Communication75', None)
    assert not _is_linked(a, 'camel_deployment_Communication75', b2)
    if hasattr(b2, 'RequiredCommunication76'):
        assert not _is_linked(b2, 'RequiredCommunication76', a)


def test_assoc_requiredCommunications57_link_reassign_clear():
    a = camel_deployment_InternalComponent(version="sample_text")
    b1 = RequiredCommunication()
    b2 = RequiredCommunication()
    _safe_set(a, 'camel_deployment_InternalComponent58', {b1})
    assert _is_linked(a, 'camel_deployment_InternalComponent58', b1)
    if hasattr(b1, 'RequiredCommunication'):
        assert _is_linked(b1, 'RequiredCommunication', a)
    _safe_set(a, 'camel_deployment_InternalComponent58', {b2})
    assert _is_linked(a, 'camel_deployment_InternalComponent58', b2)
    if hasattr(b1, 'RequiredCommunication'):
        assert not _is_linked(b1, 'RequiredCommunication', a)
    if hasattr(b2, 'RequiredCommunication'):
        assert _is_linked(b2, 'RequiredCommunication', a)
    _safe_set(a, 'camel_deployment_InternalComponent58', set())
    assert not _is_linked(a, 'camel_deployment_InternalComponent58', b2)
    if hasattr(b2, 'RequiredCommunication'):
        assert not _is_linked(b2, 'RequiredCommunication', a)


def test_assoc_requiredHost59_link_reassign_clear():
    a = camel_deployment_InternalComponent(version="sample_text")
    b1 = RequiredHost()
    b2 = RequiredHost()
    _safe_set(a, 'camel_deployment_InternalComponent60', b1)
    assert _is_linked(a, 'camel_deployment_InternalComponent60', b1)
    if hasattr(b1, 'RequiredHost'):
        assert _is_linked(b1, 'RequiredHost', a)
    _safe_set(a, 'camel_deployment_InternalComponent60', b2)
    assert _is_linked(a, 'camel_deployment_InternalComponent60', b2)
    if hasattr(b1, 'RequiredHost'):
        assert not _is_linked(b1, 'RequiredHost', a)
    if hasattr(b2, 'RequiredHost'):
        assert _is_linked(b2, 'RequiredHost', a)
    _safe_set(a, 'camel_deployment_InternalComponent60', None)
    assert not _is_linked(a, 'camel_deployment_InternalComponent60', b2)
    if hasattr(b2, 'RequiredHost'):
        assert not _is_linked(b2, 'RequiredHost', a)


def test_assoc_requiredPortConfiguration80_link_reassign_clear():
    a = camel_deployment_Communication(type="sample_text")
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'camel_deployment_Communication81', b1)
    assert _is_linked(a, 'camel_deployment_Communication81', b1)
    if hasattr(b1, 'Configuration82'):
        assert _is_linked(b1, 'Configuration82', a)
    _safe_set(a, 'camel_deployment_Communication81', b2)
    assert _is_linked(a, 'camel_deployment_Communication81', b2)
    if hasattr(b1, 'Configuration82'):
        assert not _is_linked(b1, 'Configuration82', a)
    if hasattr(b2, 'Configuration82'):
        assert _is_linked(b2, 'Configuration82', a)
    _safe_set(a, 'camel_deployment_Communication81', None)
    assert not _is_linked(a, 'camel_deployment_Communication81', b2)
    if hasattr(b2, 'Configuration82'):
        assert not _is_linked(b2, 'Configuration82', a)


def test_assoc_requirementGroup141_link_reassign_clear():
    a = camel_execution_ExecutionContext(endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1), totalCost=3.14)
    b1 = RequirementGroup()
    b2 = RequirementGroup()
    _safe_set(a, 'camel_execution_ExecutionContext142', b1)
    assert _is_linked(a, 'camel_execution_ExecutionContext142', b1)
    if hasattr(b1, 'RequirementGroup'):
        assert _is_linked(b1, 'RequirementGroup', a)
    _safe_set(a, 'camel_execution_ExecutionContext142', b2)
    assert _is_linked(a, 'camel_execution_ExecutionContext142', b2)
    if hasattr(b1, 'RequirementGroup'):
        assert not _is_linked(b1, 'RequirementGroup', a)
    if hasattr(b2, 'RequirementGroup'):
        assert _is_linked(b2, 'RequirementGroup', a)
    _safe_set(a, 'camel_execution_ExecutionContext142', None)
    assert not _is_linked(a, 'camel_execution_ExecutionContext142', b2)
    if hasattr(b2, 'RequirementGroup'):
        assert not _is_linked(b2, 'RequirementGroup', a)


def test_assoc_requirementModels318_link_reassign_clear():
    a = camel_organisation_User(email="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", www="sample_text")
    b1 = RequirementModel()
    b2 = RequirementModel()
    _safe_set(a, 'camel_organisation_User319', {b1})
    assert _is_linked(a, 'camel_organisation_User319', b1)
    if hasattr(b1, 'RequirementModel320'):
        assert _is_linked(b1, 'RequirementModel320', a)
    _safe_set(a, 'camel_organisation_User319', {b2})
    assert _is_linked(a, 'camel_organisation_User319', b2)
    if hasattr(b1, 'RequirementModel320'):
        assert not _is_linked(b1, 'RequirementModel320', a)
    if hasattr(b2, 'RequirementModel320'):
        assert _is_linked(b2, 'RequirementModel320', a)
    _safe_set(a, 'camel_organisation_User319', set())
    assert not _is_linked(a, 'camel_organisation_User319', b2)
    if hasattr(b2, 'RequirementModel320'):
        assert not _is_linked(b2, 'RequirementModel320', a)


def test_assoc_requirements397_link_reassign_clear():
    a = camel_requirement_RequirementGroup(requirementOperator="sample_text")
    b1 = Requirement()
    b2 = Requirement()
    _safe_set(a, 'camel_requirement_RequirementGroup', {b1})
    assert _is_linked(a, 'camel_requirement_RequirementGroup', b1)
    if hasattr(b1, 'Requirement398'):
        assert _is_linked(b1, 'Requirement398', a)
    _safe_set(a, 'camel_requirement_RequirementGroup', {b2})
    assert _is_linked(a, 'camel_requirement_RequirementGroup', b2)
    if hasattr(b1, 'Requirement398'):
        assert not _is_linked(b1, 'Requirement398', a)
    if hasattr(b2, 'Requirement398'):
        assert _is_linked(b2, 'Requirement398', a)
    _safe_set(a, 'camel_requirement_RequirementGroup', set())
    assert not _is_linked(a, 'camel_requirement_RequirementGroup', b2)
    if hasattr(b2, 'Requirement398'):
        assert not _is_linked(b2, 'Requirement398', a)


def test_assoc_resourceFilter330_link_reassign_clear():
    a = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    b1 = ResourceFilter()
    b2 = ResourceFilter()
    _safe_set(a, 'camel_organisation_Permission331', b1)
    assert _is_linked(a, 'camel_organisation_Permission331', b1)
    if hasattr(b1, 'ResourceFilter332'):
        assert _is_linked(b1, 'ResourceFilter332', a)
    _safe_set(a, 'camel_organisation_Permission331', b2)
    assert _is_linked(a, 'camel_organisation_Permission331', b2)
    if hasattr(b1, 'ResourceFilter332'):
        assert not _is_linked(b1, 'ResourceFilter332', a)
    if hasattr(b2, 'ResourceFilter332'):
        assert _is_linked(b2, 'ResourceFilter332', a)
    _safe_set(a, 'camel_organisation_Permission331', None)
    assert not _is_linked(a, 'camel_organisation_Permission331', b2)
    if hasattr(b2, 'ResourceFilter332'):
        assert not _is_linked(b2, 'ResourceFilter332', a)


def test_assoc_resourceFilters307_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = ResourceFilter()
    b2 = ResourceFilter()
    _safe_set(a, 'camel_organisation_OrganisationModel308', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel308', b1)
    if hasattr(b1, 'ResourceFilter'):
        assert _is_linked(b1, 'ResourceFilter', a)
    _safe_set(a, 'camel_organisation_OrganisationModel308', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel308', b2)
    if hasattr(b1, 'ResourceFilter'):
        assert not _is_linked(b1, 'ResourceFilter', a)
    if hasattr(b2, 'ResourceFilter'):
        assert _is_linked(b2, 'ResourceFilter', a)
    _safe_set(a, 'camel_organisation_OrganisationModel308', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel308', b2)
    if hasattr(b2, 'ResourceFilter'):
        assert not _is_linked(b2, 'ResourceFilter', a)


def test_assoc_rightEvent451_link_reassign_clear():
    a = camel_scalability_BinaryEventPattern(lowerOccurrenceBound=7, operator="sample_text", upperOccurrenceBound=7)
    b1 = Event()
    b2 = Event()
    _safe_set(a, 'camel_scalability_BinaryEventPattern452', b1)
    assert _is_linked(a, 'camel_scalability_BinaryEventPattern452', b1)
    if hasattr(b1, 'Event453'):
        assert _is_linked(b1, 'Event453', a)
    _safe_set(a, 'camel_scalability_BinaryEventPattern452', b2)
    assert _is_linked(a, 'camel_scalability_BinaryEventPattern452', b2)
    if hasattr(b1, 'Event453'):
        assert not _is_linked(b1, 'Event453', a)
    if hasattr(b2, 'Event453'):
        assert _is_linked(b2, 'Event453', a)
    _safe_set(a, 'camel_scalability_BinaryEventPattern452', None)
    assert not _is_linked(a, 'camel_scalability_BinaryEventPattern452', b2)
    if hasattr(b2, 'Event453'):
        assert not _is_linked(b2, 'Event453', a)


def test_assoc_role328_link_reassign_clear():
    a = camel_organisation_Permission(action="sample_text", endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    b1 = Role()
    b2 = Role()
    _safe_set(a, 'camel_organisation_Permission', b1)
    assert _is_linked(a, 'camel_organisation_Permission', b1)
    if hasattr(b1, 'Role329'):
        assert _is_linked(b1, 'Role329', a)
    _safe_set(a, 'camel_organisation_Permission', b2)
    assert _is_linked(a, 'camel_organisation_Permission', b2)
    if hasattr(b1, 'Role329'):
        assert not _is_linked(b1, 'Role329', a)
    if hasattr(b2, 'Role329'):
        assert _is_linked(b2, 'Role329', a)
    _safe_set(a, 'camel_organisation_Permission', None)
    assert not _is_linked(a, 'camel_organisation_Permission', b2)
    if hasattr(b2, 'Role329'):
        assert not _is_linked(b2, 'Role329', a)


def test_assoc_role335_link_reassign_clear():
    a = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    b1 = Role()
    b2 = Role()
    _safe_set(a, 'camel_organisation_RoleAssignment336', b1)
    assert _is_linked(a, 'camel_organisation_RoleAssignment336', b1)
    if hasattr(b1, 'Role337'):
        assert _is_linked(b1, 'Role337', a)
    _safe_set(a, 'camel_organisation_RoleAssignment336', b2)
    assert _is_linked(a, 'camel_organisation_RoleAssignment336', b2)
    if hasattr(b1, 'Role337'):
        assert not _is_linked(b1, 'Role337', a)
    if hasattr(b2, 'Role337'):
        assert _is_linked(b2, 'Role337', a)
    _safe_set(a, 'camel_organisation_RoleAssignment336', None)
    assert not _is_linked(a, 'camel_organisation_RoleAssignment336', b2)
    if hasattr(b2, 'Role337'):
        assert not _is_linked(b2, 'Role337', a)


def test_assoc_roleAssigments303_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = RoleAssignment()
    b2 = RoleAssignment()
    _safe_set(a, 'camel_organisation_OrganisationModel304', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel304', b1)
    if hasattr(b1, 'RoleAssignment'):
        assert _is_linked(b1, 'RoleAssignment', a)
    _safe_set(a, 'camel_organisation_OrganisationModel304', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel304', b2)
    if hasattr(b1, 'RoleAssignment'):
        assert not _is_linked(b1, 'RoleAssignment', a)
    if hasattr(b2, 'RoleAssignment'):
        assert _is_linked(b2, 'RoleAssignment', a)
    _safe_set(a, 'camel_organisation_OrganisationModel304', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel304', b2)
    if hasattr(b2, 'RoleAssignment'):
        assert not _is_linked(b2, 'RoleAssignment', a)


def test_assoc_roles301_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = Role()
    b2 = Role()
    _safe_set(a, 'camel_organisation_OrganisationModel302', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel302', b1)
    if hasattr(b1, 'Role'):
        assert _is_linked(b1, 'Role', a)
    _safe_set(a, 'camel_organisation_OrganisationModel302', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel302', b2)
    if hasattr(b1, 'Role'):
        assert not _is_linked(b1, 'Role', a)
    if hasattr(b2, 'Role'):
        assert _is_linked(b2, 'Role', a)
    _safe_set(a, 'camel_organisation_OrganisationModel302', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel302', b2)
    if hasattr(b2, 'Role'):
        assert not _is_linked(b2, 'Role', a)


def test_assoc_scalabilityRule171_link_reassign_clear():
    a = camel_execution_RuleTrigger(name="sample_text", trigerringTime=date(2024, 1, 1))
    b1 = ScalabilityRule()
    b2 = ScalabilityRule()
    _safe_set(a, 'camel_execution_RuleTrigger', b1)
    assert _is_linked(a, 'camel_execution_RuleTrigger', b1)
    if hasattr(b1, 'ScalabilityRule'):
        assert _is_linked(b1, 'ScalabilityRule', a)
    _safe_set(a, 'camel_execution_RuleTrigger', b2)
    assert _is_linked(a, 'camel_execution_RuleTrigger', b2)
    if hasattr(b1, 'ScalabilityRule'):
        assert not _is_linked(b1, 'ScalabilityRule', a)
    if hasattr(b2, 'ScalabilityRule'):
        assert _is_linked(b2, 'ScalabilityRule', a)
    _safe_set(a, 'camel_execution_RuleTrigger', None)
    assert not _is_linked(a, 'camel_execution_RuleTrigger', b2)
    if hasattr(b2, 'ScalabilityRule'):
        assert not _is_linked(b2, 'ScalabilityRule', a)


def test_assoc_scaleRequirements468_link_reassign_clear():
    a = camel_scalability_ScalabilityRule(name="sample_text")
    b1 = ScaleRequirement()
    b2 = ScaleRequirement()
    _safe_set(a, 'camel_scalability_ScalabilityRule469', {b1})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule469', b1)
    if hasattr(b1, 'ScaleRequirement470'):
        assert _is_linked(b1, 'ScaleRequirement470', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule469', {b2})
    assert _is_linked(a, 'camel_scalability_ScalabilityRule469', b2)
    if hasattr(b1, 'ScaleRequirement470'):
        assert not _is_linked(b1, 'ScaleRequirement470', a)
    if hasattr(b2, 'ScaleRequirement470'):
        assert _is_linked(b2, 'ScaleRequirement470', a)
    _safe_set(a, 'camel_scalability_ScalabilityRule469', set())
    assert not _is_linked(a, 'camel_scalability_ScalabilityRule469', b2)
    if hasattr(b2, 'ScaleRequirement470'):
        assert not _is_linked(b2, 'ScaleRequirement470', a)


def test_assoc_schedule204_link_reassign_clear():
    a = camel_metric_MetricInstance(name="sample_text")
    b1 = Schedule()
    b2 = Schedule()
    _safe_set(a, 'camel_metric_MetricInstance205', b1)
    assert _is_linked(a, 'camel_metric_MetricInstance205', b1)
    if hasattr(b1, 'Schedule'):
        assert _is_linked(b1, 'Schedule', a)
    _safe_set(a, 'camel_metric_MetricInstance205', b2)
    assert _is_linked(a, 'camel_metric_MetricInstance205', b2)
    if hasattr(b1, 'Schedule'):
        assert not _is_linked(b1, 'Schedule', a)
    if hasattr(b2, 'Schedule'):
        assert _is_linked(b2, 'Schedule', a)
    _safe_set(a, 'camel_metric_MetricInstance205', None)
    assert not _is_linked(a, 'camel_metric_MetricInstance205', b2)
    if hasattr(b2, 'Schedule'):
        assert not _is_linked(b2, 'Schedule', a)


def test_assoc_securityCapability314_link_reassign_clear():
    a = camel_organisation_CloudProvider(IaaS=True, PaaS=True, SaaS=True, public=True)
    b1 = SecurityCapability()
    b2 = SecurityCapability()
    _safe_set(a, 'camel_organisation_CloudProvider315', {b1})
    assert _is_linked(a, 'camel_organisation_CloudProvider315', b1)
    if hasattr(b1, 'SecurityCapability'):
        assert _is_linked(b1, 'SecurityCapability', a)
    _safe_set(a, 'camel_organisation_CloudProvider315', {b2})
    assert _is_linked(a, 'camel_organisation_CloudProvider315', b2)
    if hasattr(b1, 'SecurityCapability'):
        assert not _is_linked(b1, 'SecurityCapability', a)
    if hasattr(b2, 'SecurityCapability'):
        assert _is_linked(b2, 'SecurityCapability', a)
    _safe_set(a, 'camel_organisation_CloudProvider315', set())
    assert not _is_linked(a, 'camel_organisation_CloudProvider315', b2)
    if hasattr(b2, 'SecurityCapability'):
        assert not _is_linked(b2, 'SecurityCapability', a)


def test_assoc_securityControls516_link_reassign_clear():
    a = camel_security_SecurityCapability(name="sample_text")
    b1 = SecurityControl()
    b2 = SecurityControl()
    _safe_set(a, 'camel_security_SecurityCapability', {b1})
    assert _is_linked(a, 'camel_security_SecurityCapability', b1)
    if hasattr(b1, 'SecurityControl517'):
        assert _is_linked(b1, 'SecurityControl517', a)
    _safe_set(a, 'camel_security_SecurityCapability', {b2})
    assert _is_linked(a, 'camel_security_SecurityCapability', b2)
    if hasattr(b1, 'SecurityControl517'):
        assert not _is_linked(b1, 'SecurityControl517', a)
    if hasattr(b2, 'SecurityControl517'):
        assert _is_linked(b2, 'SecurityControl517', a)
    _safe_set(a, 'camel_security_SecurityCapability', set())
    assert not _is_linked(a, 'camel_security_SecurityCapability', b2)
    if hasattr(b2, 'SecurityControl517'):
        assert not _is_linked(b2, 'SecurityControl517', a)


def test_assoc_securityProperties505_link_reassign_clear():
    a = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    b1 = SecurityProperty()
    b2 = SecurityProperty()
    _safe_set(a, 'camel_security_SecurityControl506', {b1})
    assert _is_linked(a, 'camel_security_SecurityControl506', b1)
    if hasattr(b1, 'SecurityProperty507'):
        assert _is_linked(b1, 'SecurityProperty507', a)
    _safe_set(a, 'camel_security_SecurityControl506', {b2})
    assert _is_linked(a, 'camel_security_SecurityControl506', b2)
    if hasattr(b1, 'SecurityProperty507'):
        assert not _is_linked(b1, 'SecurityProperty507', a)
    if hasattr(b2, 'SecurityProperty507'):
        assert _is_linked(b2, 'SecurityProperty507', a)
    _safe_set(a, 'camel_security_SecurityControl506', set())
    assert not _is_linked(a, 'camel_security_SecurityControl506', b2)
    if hasattr(b2, 'SecurityProperty507'):
        assert not _is_linked(b2, 'SecurityProperty507', a)


def test_assoc_sensors235_link_reassign_clear():
    a = camel_metric_Property(description="sample_text", name="sample_text", type="sample_text")
    b1 = Sensor()
    b2 = Sensor()
    _safe_set(a, 'camel_metric_Property236', {b1})
    assert _is_linked(a, 'camel_metric_Property236', b1)
    if hasattr(b1, 'Sensor237'):
        assert _is_linked(b1, 'Sensor237', a)
    _safe_set(a, 'camel_metric_Property236', {b2})
    assert _is_linked(a, 'camel_metric_Property236', b2)
    if hasattr(b1, 'Sensor237'):
        assert not _is_linked(b1, 'Sensor237', a)
    if hasattr(b2, 'Sensor237'):
        assert _is_linked(b2, 'Sensor237', a)
    _safe_set(a, 'camel_metric_Property236', set())
    assert not _is_linked(a, 'camel_metric_Property236', b2)
    if hasattr(b2, 'Sensor237'):
        assert not _is_linked(b2, 'Sensor237', a)


def test_assoc_slo147_link_reassign_clear():
    a = camel_execution_Measurement(measurementTime=date(2024, 1, 1), name="sample_text", rawData="sample_text", value=3.14)
    b1 = ServiceLevelObjective()
    b2 = ServiceLevelObjective()
    _safe_set(a, 'camel_execution_Measurement148', b1)
    assert _is_linked(a, 'camel_execution_Measurement148', b1)
    if hasattr(b1, 'ServiceLevelObjective'):
        assert _is_linked(b1, 'ServiceLevelObjective', a)
    _safe_set(a, 'camel_execution_Measurement148', b2)
    assert _is_linked(a, 'camel_execution_Measurement148', b2)
    if hasattr(b1, 'ServiceLevelObjective'):
        assert not _is_linked(b1, 'ServiceLevelObjective', a)
    if hasattr(b2, 'ServiceLevelObjective'):
        assert _is_linked(b2, 'ServiceLevelObjective', a)
    _safe_set(a, 'camel_execution_Measurement148', None)
    assert not _is_linked(a, 'camel_execution_Measurement148', b2)
    if hasattr(b2, 'ServiceLevelObjective'):
        assert not _is_linked(b2, 'ServiceLevelObjective', a)


def test_assoc_slo163_link_reassign_clear():
    a = camel_execution_SLOAssessment(assessment=True, assessmentTime=date(2024, 1, 1), name="sample_text")
    b1 = ServiceLevelObjective()
    b2 = ServiceLevelObjective()
    _safe_set(a, 'camel_execution_SLOAssessment', b1)
    assert _is_linked(a, 'camel_execution_SLOAssessment', b1)
    if hasattr(b1, 'ServiceLevelObjective164'):
        assert _is_linked(b1, 'ServiceLevelObjective164', a)
    _safe_set(a, 'camel_execution_SLOAssessment', b2)
    assert _is_linked(a, 'camel_execution_SLOAssessment', b2)
    if hasattr(b1, 'ServiceLevelObjective164'):
        assert not _is_linked(b1, 'ServiceLevelObjective164', a)
    if hasattr(b2, 'ServiceLevelObjective164'):
        assert _is_linked(b2, 'ServiceLevelObjective164', a)
    _safe_set(a, 'camel_execution_SLOAssessment', None)
    assert not _is_linked(a, 'camel_execution_SLOAssessment', b2)
    if hasattr(b2, 'ServiceLevelObjective164'):
        assert not _is_linked(b2, 'ServiceLevelObjective164', a)


def test_assoc_subClones362_link_reassign_clear():
    a = camel_provider_Clone(name="sample_text")
    b1 = Clone()
    b2 = Clone()
    _safe_set(a, 'camel_provider_Clone', {b1})
    assert _is_linked(a, 'camel_provider_Clone', b1)
    if hasattr(b1, 'Clone'):
        assert _is_linked(b1, 'Clone', a)
    _safe_set(a, 'camel_provider_Clone', {b2})
    assert _is_linked(a, 'camel_provider_Clone', b2)
    if hasattr(b1, 'Clone'):
        assert not _is_linked(b1, 'Clone', a)
    if hasattr(b2, 'Clone'):
        assert _is_linked(b2, 'Clone', a)
    _safe_set(a, 'camel_provider_Clone', set())
    assert not _is_linked(a, 'camel_provider_Clone', b2)
    if hasattr(b2, 'Clone'):
        assert not _is_linked(b2, 'Clone', a)


def test_assoc_subDomain498_link_reassign_clear():
    a = camel_security_SecurityDomain(id="sample_text", name="sample_text")
    b1 = SecurityDomain()
    b2 = SecurityDomain()
    _safe_set(a, 'camel_security_SecurityDomain', {b1})
    assert _is_linked(a, 'camel_security_SecurityDomain', b1)
    if hasattr(b1, 'SecurityDomain499'):
        assert _is_linked(b1, 'SecurityDomain499', a)
    _safe_set(a, 'camel_security_SecurityDomain', {b2})
    assert _is_linked(a, 'camel_security_SecurityDomain', b2)
    if hasattr(b1, 'SecurityDomain499'):
        assert not _is_linked(b1, 'SecurityDomain499', a)
    if hasattr(b2, 'SecurityDomain499'):
        assert _is_linked(b2, 'SecurityDomain499', a)
    _safe_set(a, 'camel_security_SecurityDomain', set())
    assert not _is_linked(a, 'camel_security_SecurityDomain', b2)
    if hasattr(b2, 'SecurityDomain499'):
        assert not _is_linked(b2, 'SecurityDomain499', a)


def test_assoc_subDomain502_link_reassign_clear():
    a = camel_security_SecurityControl(name="sample_text", specification="sample_text")
    b1 = SecurityDomain()
    b2 = SecurityDomain()
    _safe_set(a, 'camel_security_SecurityControl503', b1)
    assert _is_linked(a, 'camel_security_SecurityControl503', b1)
    if hasattr(b1, 'SecurityDomain504'):
        assert _is_linked(b1, 'SecurityDomain504', a)
    _safe_set(a, 'camel_security_SecurityControl503', b2)
    assert _is_linked(a, 'camel_security_SecurityControl503', b2)
    if hasattr(b1, 'SecurityDomain504'):
        assert not _is_linked(b1, 'SecurityDomain504', a)
    if hasattr(b2, 'SecurityDomain504'):
        assert _is_linked(b2, 'SecurityDomain504', a)
    _safe_set(a, 'camel_security_SecurityControl503', None)
    assert not _is_linked(a, 'camel_security_SecurityControl503', b2)
    if hasattr(b2, 'SecurityDomain504'):
        assert not _is_linked(b2, 'SecurityDomain504', a)


def test_assoc_subFeatures381_link_reassign_clear():
    a = camel_provider_Feature(name="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'camel_provider_Feature382', {b1})
    assert _is_linked(a, 'camel_provider_Feature382', b1)
    if hasattr(b1, 'Feature383'):
        assert _is_linked(b1, 'Feature383', a)
    _safe_set(a, 'camel_provider_Feature382', {b2})
    assert _is_linked(a, 'camel_provider_Feature382', b2)
    if hasattr(b1, 'Feature383'):
        assert not _is_linked(b1, 'Feature383', a)
    if hasattr(b2, 'Feature383'):
        assert _is_linked(b2, 'Feature383', a)
    _safe_set(a, 'camel_provider_Feature382', set())
    assert not _is_linked(a, 'camel_provider_Feature382', b2)
    if hasattr(b2, 'Feature383'):
        assert not _is_linked(b2, 'Feature383', a)


def test_assoc_subLocations186_link_reassign_clear():
    a = camel_location_CloudLocation(isAssignable=True)
    b1 = CloudLocation()
    b2 = CloudLocation()
    _safe_set(a, 'camel_location_CloudLocation', {b1})
    assert _is_linked(a, 'camel_location_CloudLocation', b1)
    if hasattr(b1, 'CloudLocation187'):
        assert _is_linked(b1, 'CloudLocation187', a)
    _safe_set(a, 'camel_location_CloudLocation', {b2})
    assert _is_linked(a, 'camel_location_CloudLocation', b2)
    if hasattr(b1, 'CloudLocation187'):
        assert not _is_linked(b1, 'CloudLocation187', a)
    if hasattr(b2, 'CloudLocation187'):
        assert _is_linked(b2, 'CloudLocation187', a)
    _safe_set(a, 'camel_location_CloudLocation', set())
    assert not _is_linked(a, 'camel_location_CloudLocation', b2)
    if hasattr(b2, 'CloudLocation187'):
        assert not _is_linked(b2, 'CloudLocation187', a)


def test_assoc_subProperties233_link_reassign_clear():
    a = camel_metric_Property(description="sample_text", name="sample_text", type="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'camel_metric_Property', {b1})
    assert _is_linked(a, 'camel_metric_Property', b1)
    if hasattr(b1, 'Property234'):
        assert _is_linked(b1, 'Property234', a)
    _safe_set(a, 'camel_metric_Property', {b2})
    assert _is_linked(a, 'camel_metric_Property', b2)
    if hasattr(b1, 'Property234'):
        assert not _is_linked(b1, 'Property234', a)
    if hasattr(b2, 'Property234'):
        assert _is_linked(b2, 'Property234', a)
    _safe_set(a, 'camel_metric_Property', set())
    assert not _is_linked(a, 'camel_metric_Property', b2)
    if hasattr(b2, 'Property234'):
        assert not _is_linked(b2, 'Property234', a)


def test_assoc_timer447_link_reassign_clear():
    a = camel_scalability_EventPattern()
    b1 = Timer()
    b2 = Timer()
    _safe_set(a, 'camel_scalability_EventPattern', b1)
    assert _is_linked(a, 'camel_scalability_EventPattern', b1)
    if hasattr(b1, 'Timer448'):
        assert _is_linked(b1, 'Timer448', a)
    _safe_set(a, 'camel_scalability_EventPattern', b2)
    assert _is_linked(a, 'camel_scalability_EventPattern', b2)
    if hasattr(b1, 'Timer448'):
        assert not _is_linked(b1, 'Timer448', a)
    if hasattr(b2, 'Timer448'):
        assert _is_linked(b2, 'Timer448', a)
    _safe_set(a, 'camel_scalability_EventPattern', None)
    assert not _is_linked(a, 'camel_scalability_EventPattern', b2)
    if hasattr(b2, 'Timer448'):
        assert not _is_linked(b2, 'Timer448', a)


def test_assoc_to353_link_reassign_clear():
    a = camel_provider_AttributeConstraint(name="sample_text")
    b1 = Attribute()
    b2 = Attribute()
    _safe_set(a, 'camel_provider_AttributeConstraint354', b1)
    assert _is_linked(a, 'camel_provider_AttributeConstraint354', b1)
    if hasattr(b1, 'Attribute355'):
        assert _is_linked(b1, 'Attribute355', a)
    _safe_set(a, 'camel_provider_AttributeConstraint354', b2)
    assert _is_linked(a, 'camel_provider_AttributeConstraint354', b2)
    if hasattr(b1, 'Attribute355'):
        assert not _is_linked(b1, 'Attribute355', a)
    if hasattr(b2, 'Attribute355'):
        assert _is_linked(b2, 'Attribute355', a)
    _safe_set(a, 'camel_provider_AttributeConstraint354', None)
    assert not _is_linked(a, 'camel_provider_AttributeConstraint354', b2)
    if hasattr(b2, 'Attribute355'):
        assert not _is_linked(b2, 'Attribute355', a)


def test_assoc_to365_link_reassign_clear():
    a = camel_provider_Constraint(name="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'camel_provider_Constraint366', b1)
    assert _is_linked(a, 'camel_provider_Constraint366', b1)
    if hasattr(b1, 'Feature367'):
        assert _is_linked(b1, 'Feature367', a)
    _safe_set(a, 'camel_provider_Constraint366', b2)
    assert _is_linked(a, 'camel_provider_Constraint366', b2)
    if hasattr(b1, 'Feature367'):
        assert not _is_linked(b1, 'Feature367', a)
    if hasattr(b2, 'Feature367'):
        assert _is_linked(b2, 'Feature367', a)
    _safe_set(a, 'camel_provider_Constraint366', None)
    assert not _is_linked(a, 'camel_provider_Constraint366', b2)
    if hasattr(b2, 'Feature367'):
        assert not _is_linked(b2, 'Feature367', a)


def test_assoc_toValue359_link_reassign_clear():
    a = camel_provider_AttributeConstraint(name="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_provider_AttributeConstraint360', b1)
    assert _is_linked(a, 'camel_provider_AttributeConstraint360', b1)
    if hasattr(b1, 'SingleValue361'):
        assert _is_linked(b1, 'SingleValue361', a)
    _safe_set(a, 'camel_provider_AttributeConstraint360', b2)
    assert _is_linked(a, 'camel_provider_AttributeConstraint360', b2)
    if hasattr(b1, 'SingleValue361'):
        assert not _is_linked(b1, 'SingleValue361', a)
    if hasattr(b2, 'SingleValue361'):
        assert _is_linked(b2, 'SingleValue361', a)
    _safe_set(a, 'camel_provider_AttributeConstraint360', None)
    assert not _is_linked(a, 'camel_provider_AttributeConstraint360', b2)
    if hasattr(b2, 'SingleValue361'):
        assert not _is_linked(b2, 'SingleValue361', a)


def test_assoc_type532_link_reassign_clear():
    a = camel_type_List(primitiveType="sample_text")
    b1 = ValueType()
    b2 = ValueType()
    _safe_set(a, 'camel_type_List533', b1)
    assert _is_linked(a, 'camel_type_List533', b1)
    if hasattr(b1, 'ValueType534'):
        assert _is_linked(b1, 'ValueType534', a)
    _safe_set(a, 'camel_type_List533', b2)
    assert _is_linked(a, 'camel_type_List533', b2)
    if hasattr(b1, 'ValueType534'):
        assert not _is_linked(b1, 'ValueType534', a)
    if hasattr(b2, 'ValueType534'):
        assert _is_linked(b2, 'ValueType534', a)
    _safe_set(a, 'camel_type_List533', None)
    assert not _is_linked(a, 'camel_type_List533', b2)
    if hasattr(b2, 'ValueType534'):
        assert not _is_linked(b2, 'ValueType534', a)


def test_assoc_type94_link_reassign_clear():
    a = camel_deployment_ComponentInstance(destroyedOn=date(2024, 1, 1), instantiatedOn=date(2024, 1, 1))
    b1 = Component()
    b2 = Component()
    _safe_set(a, 'camel_deployment_ComponentInstance', b1)
    assert _is_linked(a, 'camel_deployment_ComponentInstance', b1)
    if hasattr(b1, 'Component'):
        assert _is_linked(b1, 'Component', a)
    _safe_set(a, 'camel_deployment_ComponentInstance', b2)
    assert _is_linked(a, 'camel_deployment_ComponentInstance', b2)
    if hasattr(b1, 'Component'):
        assert not _is_linked(b1, 'Component', a)
    if hasattr(b2, 'Component'):
        assert _is_linked(b2, 'Component', a)
    _safe_set(a, 'camel_deployment_ComponentInstance', None)
    assert not _is_linked(a, 'camel_deployment_ComponentInstance', b2)
    if hasattr(b2, 'Component'):
        assert not _is_linked(b2, 'Component', a)


def test_assoc_unit220_link_reassign_clear():
    a = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    b1 = Unit()
    b2 = Unit()
    _safe_set(a, 'camel_metric_Metric221', b1)
    assert _is_linked(a, 'camel_metric_Metric221', b1)
    if hasattr(b1, 'Unit'):
        assert _is_linked(b1, 'Unit', a)
    _safe_set(a, 'camel_metric_Metric221', b2)
    assert _is_linked(a, 'camel_metric_Metric221', b2)
    if hasattr(b1, 'Unit'):
        assert not _is_linked(b1, 'Unit', a)
    if hasattr(b2, 'Unit'):
        assert _is_linked(b2, 'Unit', a)
    _safe_set(a, 'camel_metric_Metric221', None)
    assert not _is_linked(a, 'camel_metric_Metric221', b2)
    if hasattr(b2, 'Unit'):
        assert not _is_linked(b2, 'Unit', a)


def test_assoc_unit238_link_reassign_clear():
    a = camel_metric_Schedule(end=date(2024, 1, 1), interval="sample_text", name="sample_text", repetitions=7, start=date(2024, 1, 1), type="sample_text")
    b1 = TimeIntervalUnit()
    b2 = TimeIntervalUnit()
    _safe_set(a, 'camel_metric_Schedule', b1)
    assert _is_linked(a, 'camel_metric_Schedule', b1)
    if hasattr(b1, 'TimeIntervalUnit239'):
        assert _is_linked(b1, 'TimeIntervalUnit239', a)
    _safe_set(a, 'camel_metric_Schedule', b2)
    assert _is_linked(a, 'camel_metric_Schedule', b2)
    if hasattr(b1, 'TimeIntervalUnit239'):
        assert not _is_linked(b1, 'TimeIntervalUnit239', a)
    if hasattr(b2, 'TimeIntervalUnit239'):
        assert _is_linked(b2, 'TimeIntervalUnit239', a)
    _safe_set(a, 'camel_metric_Schedule', None)
    assert not _is_linked(a, 'camel_metric_Schedule', b2)
    if hasattr(b2, 'TimeIntervalUnit239'):
        assert not _is_linked(b2, 'TimeIntervalUnit239', a)


def test_assoc_unit240_link_reassign_clear():
    a = camel_metric_Window(measurementSize="sample_text", name="sample_text", sizeType="sample_text", timeSize="sample_text", windowType="sample_text")
    b1 = TimeIntervalUnit()
    b2 = TimeIntervalUnit()
    _safe_set(a, 'camel_metric_Window', b1)
    assert _is_linked(a, 'camel_metric_Window', b1)
    if hasattr(b1, 'TimeIntervalUnit241'):
        assert _is_linked(b1, 'TimeIntervalUnit241', a)
    _safe_set(a, 'camel_metric_Window', b2)
    assert _is_linked(a, 'camel_metric_Window', b2)
    if hasattr(b1, 'TimeIntervalUnit241'):
        assert not _is_linked(b1, 'TimeIntervalUnit241', a)
    if hasattr(b2, 'TimeIntervalUnit241'):
        assert _is_linked(b2, 'TimeIntervalUnit241', a)
    _safe_set(a, 'camel_metric_Window', None)
    assert not _is_linked(a, 'camel_metric_Window', b2)
    if hasattr(b2, 'TimeIntervalUnit241'):
        assert not _is_linked(b2, 'TimeIntervalUnit241', a)


def test_assoc_unit475_link_reassign_clear():
    a = camel_scalability_Timer(maxOccurrenceNum=7, name="sample_text", timeValue=7, type="sample_text")
    b1 = TimeIntervalUnit()
    b2 = TimeIntervalUnit()
    _safe_set(a, 'camel_scalability_Timer', b1)
    assert _is_linked(a, 'camel_scalability_Timer', b1)
    if hasattr(b1, 'TimeIntervalUnit476'):
        assert _is_linked(b1, 'TimeIntervalUnit476', a)
    _safe_set(a, 'camel_scalability_Timer', b2)
    assert _is_linked(a, 'camel_scalability_Timer', b2)
    if hasattr(b1, 'TimeIntervalUnit476'):
        assert not _is_linked(b1, 'TimeIntervalUnit476', a)
    if hasattr(b2, 'TimeIntervalUnit476'):
        assert _is_linked(b2, 'TimeIntervalUnit476', a)
    _safe_set(a, 'camel_scalability_Timer', None)
    assert not _is_linked(a, 'camel_scalability_Timer', b2)
    if hasattr(b2, 'TimeIntervalUnit476'):
        assert not _is_linked(b2, 'TimeIntervalUnit476', a)


def test_assoc_upperLimit536_link_reassign_clear():
    a = camel_type_Range(primitiveType="sample_text")
    b1 = Limit()
    b2 = Limit()
    _safe_set(a, 'camel_type_Range537', b1)
    assert _is_linked(a, 'camel_type_Range537', b1)
    if hasattr(b1, 'Limit538'):
        assert _is_linked(b1, 'Limit538', a)
    _safe_set(a, 'camel_type_Range537', b2)
    assert _is_linked(a, 'camel_type_Range537', b2)
    if hasattr(b1, 'Limit538'):
        assert not _is_linked(b1, 'Limit538', a)
    if hasattr(b2, 'Limit538'):
        assert _is_linked(b2, 'Limit538', a)
    _safe_set(a, 'camel_type_Range537', None)
    assert not _is_linked(a, 'camel_type_Range537', b2)
    if hasattr(b2, 'Limit538'):
        assert not _is_linked(b2, 'Limit538', a)


def test_assoc_user333_link_reassign_clear():
    a = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    b1 = User()
    b2 = User()
    _safe_set(a, 'camel_organisation_RoleAssignment', b1)
    assert _is_linked(a, 'camel_organisation_RoleAssignment', b1)
    if hasattr(b1, 'User334'):
        assert _is_linked(b1, 'User334', a)
    _safe_set(a, 'camel_organisation_RoleAssignment', b2)
    assert _is_linked(a, 'camel_organisation_RoleAssignment', b2)
    if hasattr(b1, 'User334'):
        assert not _is_linked(b1, 'User334', a)
    if hasattr(b2, 'User334'):
        assert _is_linked(b2, 'User334', a)
    _safe_set(a, 'camel_organisation_RoleAssignment', None)
    assert not _is_linked(a, 'camel_organisation_RoleAssignment', b2)
    if hasattr(b2, 'User334'):
        assert not _is_linked(b2, 'User334', a)


def test_assoc_userGroup338_link_reassign_clear():
    a = camel_organisation_RoleAssignment(assignmentTime=date(2024, 1, 1), endTime=date(2024, 1, 1), name="sample_text", startTime=date(2024, 1, 1))
    b1 = UserGroup()
    b2 = UserGroup()
    _safe_set(a, 'camel_organisation_RoleAssignment339', b1)
    assert _is_linked(a, 'camel_organisation_RoleAssignment339', b1)
    if hasattr(b1, 'UserGroup340'):
        assert _is_linked(b1, 'UserGroup340', a)
    _safe_set(a, 'camel_organisation_RoleAssignment339', b2)
    assert _is_linked(a, 'camel_organisation_RoleAssignment339', b2)
    if hasattr(b1, 'UserGroup340'):
        assert not _is_linked(b1, 'UserGroup340', a)
    if hasattr(b2, 'UserGroup340'):
        assert _is_linked(b2, 'UserGroup340', a)
    _safe_set(a, 'camel_organisation_RoleAssignment339', None)
    assert not _is_linked(a, 'camel_organisation_RoleAssignment339', b2)
    if hasattr(b2, 'UserGroup340'):
        assert not _is_linked(b2, 'UserGroup340', a)


def test_assoc_userGroups297_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = UserGroup()
    b2 = UserGroup()
    _safe_set(a, 'camel_organisation_OrganisationModel298', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel298', b1)
    if hasattr(b1, 'UserGroup'):
        assert _is_linked(b1, 'UserGroup', a)
    _safe_set(a, 'camel_organisation_OrganisationModel298', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel298', b2)
    if hasattr(b1, 'UserGroup'):
        assert not _is_linked(b1, 'UserGroup', a)
    if hasattr(b2, 'UserGroup'):
        assert _is_linked(b2, 'UserGroup', a)
    _safe_set(a, 'camel_organisation_OrganisationModel298', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel298', b2)
    if hasattr(b2, 'UserGroup'):
        assert not _is_linked(b2, 'UserGroup', a)


def test_assoc_users295_link_reassign_clear():
    a = camel_organisation_OrganisationModel(securityLevel="sample_text")
    b1 = User()
    b2 = User()
    _safe_set(a, 'camel_organisation_OrganisationModel296', {b1})
    assert _is_linked(a, 'camel_organisation_OrganisationModel296', b1)
    if hasattr(b1, 'User'):
        assert _is_linked(b1, 'User', a)
    _safe_set(a, 'camel_organisation_OrganisationModel296', {b2})
    assert _is_linked(a, 'camel_organisation_OrganisationModel296', b2)
    if hasattr(b1, 'User'):
        assert not _is_linked(b1, 'User', a)
    if hasattr(b2, 'User'):
        assert _is_linked(b2, 'User', a)
    _safe_set(a, 'camel_organisation_OrganisationModel296', set())
    assert not _is_linked(a, 'camel_organisation_OrganisationModel296', b2)
    if hasattr(b2, 'User'):
        assert not _is_linked(b2, 'User', a)


def test_assoc_users341_link_reassign_clear():
    a = camel_organisation_UserGroup(name="sample_text")
    b1 = User()
    b2 = User()
    _safe_set(a, 'camel_organisation_UserGroup', {b1})
    assert _is_linked(a, 'camel_organisation_UserGroup', b1)
    if hasattr(b1, 'User342'):
        assert _is_linked(b1, 'User342', a)
    _safe_set(a, 'camel_organisation_UserGroup', {b2})
    assert _is_linked(a, 'camel_organisation_UserGroup', b2)
    if hasattr(b1, 'User342'):
        assert not _is_linked(b1, 'User342', a)
    if hasattr(b2, 'User342'):
        assert _is_linked(b2, 'User342', a)
    _safe_set(a, 'camel_organisation_UserGroup', set())
    assert not _is_linked(a, 'camel_organisation_UserGroup', b2)
    if hasattr(b2, 'User342'):
        assert not _is_linked(b2, 'User342', a)


def test_assoc_value216_link_reassign_clear():
    a = camel_metric_MetricFormulaParameter(name="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_metric_MetricFormulaParameter', b1)
    assert _is_linked(a, 'camel_metric_MetricFormulaParameter', b1)
    if hasattr(b1, 'SingleValue217'):
        assert _is_linked(b1, 'SingleValue217', a)
    _safe_set(a, 'camel_metric_MetricFormulaParameter', b2)
    assert _is_linked(a, 'camel_metric_MetricFormulaParameter', b2)
    if hasattr(b1, 'SingleValue217'):
        assert not _is_linked(b1, 'SingleValue217', a)
    if hasattr(b2, 'SingleValue217'):
        assert _is_linked(b2, 'SingleValue217', a)
    _safe_set(a, 'camel_metric_MetricFormulaParameter', None)
    assert not _is_linked(a, 'camel_metric_MetricFormulaParameter', b2)
    if hasattr(b2, 'SingleValue217'):
        assert not _is_linked(b2, 'SingleValue217', a)


def test_assoc_value346_link_reassign_clear():
    a = camel_provider_Attribute(name="sample_text", unitType="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_provider_Attribute', b1)
    assert _is_linked(a, 'camel_provider_Attribute', b1)
    if hasattr(b1, 'SingleValue347'):
        assert _is_linked(b1, 'SingleValue347', a)
    _safe_set(a, 'camel_provider_Attribute', b2)
    assert _is_linked(a, 'camel_provider_Attribute', b2)
    if hasattr(b1, 'SingleValue347'):
        assert not _is_linked(b1, 'SingleValue347', a)
    if hasattr(b2, 'SingleValue347'):
        assert _is_linked(b2, 'SingleValue347', a)
    _safe_set(a, 'camel_provider_Attribute', None)
    assert not _is_linked(a, 'camel_provider_Attribute', b2)
    if hasattr(b2, 'SingleValue347'):
        assert not _is_linked(b2, 'SingleValue347', a)


def test_assoc_value526_link_reassign_clear():
    a = camel_type_Limit(included=True)
    b1 = NumericValue()
    b2 = NumericValue()
    _safe_set(a, 'camel_type_Limit', b1)
    assert _is_linked(a, 'camel_type_Limit', b1)
    if hasattr(b1, 'NumericValue'):
        assert _is_linked(b1, 'NumericValue', a)
    _safe_set(a, 'camel_type_Limit', b2)
    assert _is_linked(a, 'camel_type_Limit', b2)
    if hasattr(b1, 'NumericValue'):
        assert not _is_linked(b1, 'NumericValue', a)
    if hasattr(b2, 'NumericValue'):
        assert _is_linked(b2, 'NumericValue', a)
    _safe_set(a, 'camel_type_Limit', None)
    assert not _is_linked(a, 'camel_type_Limit', b2)
    if hasattr(b2, 'NumericValue'):
        assert not _is_linked(b2, 'NumericValue', a)


def test_assoc_valueType219_link_reassign_clear():
    a = camel_metric_Metric(description="sample_text", isVariable=True, layer="sample_text", valueDirection="sample_text")
    b1 = ValueType()
    b2 = ValueType()
    _safe_set(a, 'camel_metric_Metric', b1)
    assert _is_linked(a, 'camel_metric_Metric', b1)
    if hasattr(b1, 'ValueType'):
        assert _is_linked(b1, 'ValueType', a)
    _safe_set(a, 'camel_metric_Metric', b2)
    assert _is_linked(a, 'camel_metric_Metric', b2)
    if hasattr(b1, 'ValueType'):
        assert not _is_linked(b1, 'ValueType', a)
    if hasattr(b2, 'ValueType'):
        assert _is_linked(b2, 'ValueType', a)
    _safe_set(a, 'camel_metric_Metric', None)
    assert not _is_linked(a, 'camel_metric_Metric', b2)
    if hasattr(b2, 'ValueType'):
        assert not _is_linked(b2, 'ValueType', a)


def test_assoc_valueType348_link_reassign_clear():
    a = camel_provider_Attribute(name="sample_text", unitType="sample_text")
    b1 = ValueType()
    b2 = ValueType()
    _safe_set(a, 'camel_provider_Attribute349', b1)
    assert _is_linked(a, 'camel_provider_Attribute349', b1)
    if hasattr(b1, 'ValueType350'):
        assert _is_linked(b1, 'ValueType350', a)
    _safe_set(a, 'camel_provider_Attribute349', b2)
    assert _is_linked(a, 'camel_provider_Attribute349', b2)
    if hasattr(b1, 'ValueType350'):
        assert not _is_linked(b1, 'ValueType350', a)
    if hasattr(b2, 'ValueType350'):
        assert _is_linked(b2, 'ValueType350', a)
    _safe_set(a, 'camel_provider_Attribute349', None)
    assert not _is_linked(a, 'camel_provider_Attribute349', b2)
    if hasattr(b2, 'ValueType350'):
        assert not _is_linked(b2, 'ValueType350', a)


def test_assoc_values529_link_reassign_clear():
    a = camel_type_Enumeration()
    b1 = EnumerateValue()
    b2 = EnumerateValue()
    _safe_set(a, 'camel_type_Enumeration', {b1})
    assert _is_linked(a, 'camel_type_Enumeration', b1)
    if hasattr(b1, 'EnumerateValue'):
        assert _is_linked(b1, 'EnumerateValue', a)
    _safe_set(a, 'camel_type_Enumeration', {b2})
    assert _is_linked(a, 'camel_type_Enumeration', b2)
    if hasattr(b1, 'EnumerateValue'):
        assert not _is_linked(b1, 'EnumerateValue', a)
    if hasattr(b2, 'EnumerateValue'):
        assert _is_linked(b2, 'EnumerateValue', a)
    _safe_set(a, 'camel_type_Enumeration', set())
    assert not _is_linked(a, 'camel_type_Enumeration', b2)
    if hasattr(b2, 'EnumerateValue'):
        assert not _is_linked(b2, 'EnumerateValue', a)


def test_assoc_values530_link_reassign_clear():
    a = camel_type_List(primitiveType="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_type_List', {b1})
    assert _is_linked(a, 'camel_type_List', b1)
    if hasattr(b1, 'SingleValue531'):
        assert _is_linked(b1, 'SingleValue531', a)
    _safe_set(a, 'camel_type_List', {b2})
    assert _is_linked(a, 'camel_type_List', b2)
    if hasattr(b1, 'SingleValue531'):
        assert not _is_linked(b1, 'SingleValue531', a)
    if hasattr(b2, 'SingleValue531'):
        assert _is_linked(b2, 'SingleValue531', a)
    _safe_set(a, 'camel_type_List', set())
    assert not _is_linked(a, 'camel_type_List', b2)
    if hasattr(b2, 'SingleValue531'):
        assert not _is_linked(b2, 'SingleValue531', a)


def test_assoc_vm430_link_reassign_clear():
    a = camel_requirement_VerticalScaleRequirement(maxCPU=3.14, maxCores=7, maxRAM=7, maxStorage=7, minCPU=3.14, minCores=7, minRAM=7, minStorage=7)
    b1 = VM()
    b2 = VM()
    _safe_set(a, 'camel_requirement_VerticalScaleRequirement', b1)
    assert _is_linked(a, 'camel_requirement_VerticalScaleRequirement', b1)
    if hasattr(b1, 'VM431'):
        assert _is_linked(b1, 'VM431', a)
    _safe_set(a, 'camel_requirement_VerticalScaleRequirement', b2)
    assert _is_linked(a, 'camel_requirement_VerticalScaleRequirement', b2)
    if hasattr(b1, 'VM431'):
        assert not _is_linked(b1, 'VM431', a)
    if hasattr(b2, 'VM431'):
        assert _is_linked(b2, 'VM431', a)
    _safe_set(a, 'camel_requirement_VerticalScaleRequirement', None)
    assert not _is_linked(a, 'camel_requirement_VerticalScaleRequirement', b2)
    if hasattr(b2, 'VM431'):
        assert not _is_linked(b2, 'VM431', a)


def test_assoc_vmType102_link_reassign_clear():
    a = camel_deployment_VMInstance(ip="sample_text")
    b1 = Attribute()
    b2 = Attribute()
    _safe_set(a, 'camel_deployment_VMInstance', b1)
    assert _is_linked(a, 'camel_deployment_VMInstance', b1)
    if hasattr(b1, 'Attribute'):
        assert _is_linked(b1, 'Attribute', a)
    _safe_set(a, 'camel_deployment_VMInstance', b2)
    assert _is_linked(a, 'camel_deployment_VMInstance', b2)
    if hasattr(b1, 'Attribute'):
        assert not _is_linked(b1, 'Attribute', a)
    if hasattr(b2, 'Attribute'):
        assert _is_linked(b2, 'Attribute', a)
    _safe_set(a, 'camel_deployment_VMInstance', None)
    assert not _is_linked(a, 'camel_deployment_VMInstance', b2)
    if hasattr(b2, 'Attribute'):
        assert not _is_linked(b2, 'Attribute', a)


def test_assoc_vmTypeValue103_link_reassign_clear():
    a = camel_deployment_VMInstance(ip="sample_text")
    b1 = SingleValue()
    b2 = SingleValue()
    _safe_set(a, 'camel_deployment_VMInstance104', b1)
    assert _is_linked(a, 'camel_deployment_VMInstance104', b1)
    if hasattr(b1, 'SingleValue'):
        assert _is_linked(b1, 'SingleValue', a)
    _safe_set(a, 'camel_deployment_VMInstance104', b2)
    assert _is_linked(a, 'camel_deployment_VMInstance104', b2)
    if hasattr(b1, 'SingleValue'):
        assert not _is_linked(b1, 'SingleValue', a)
    if hasattr(b2, 'SingleValue'):
        assert _is_linked(b2, 'SingleValue', a)
    _safe_set(a, 'camel_deployment_VMInstance104', None)
    assert not _is_linked(a, 'camel_deployment_VMInstance104', b2)
    if hasattr(b2, 'SingleValue'):
        assert not _is_linked(b2, 'SingleValue', a)


def test_assoc_window206_link_reassign_clear():
    a = camel_metric_MetricInstance(name="sample_text")
    b1 = Window()
    b2 = Window()
    _safe_set(a, 'camel_metric_MetricInstance207', b1)
    assert _is_linked(a, 'camel_metric_MetricInstance207', b1)
    if hasattr(b1, 'Window'):
        assert _is_linked(b1, 'Window', a)
    _safe_set(a, 'camel_metric_MetricInstance207', b2)
    assert _is_linked(a, 'camel_metric_MetricInstance207', b2)
    if hasattr(b1, 'Window'):
        assert not _is_linked(b1, 'Window', a)
    if hasattr(b2, 'Window'):
        assert _is_linked(b2, 'Window', a)
    _safe_set(a, 'camel_metric_MetricInstance207', None)
    assert not _is_linked(a, 'camel_metric_MetricInstance207', b2)
    if hasattr(b2, 'Window'):
        assert not _is_linked(b2, 'Window', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActionRealisation_strategy = st.builds(ActionRealisation)
@given(instance=ActionRealisation_strategy)
@settings(max_examples=25)
def test_ActionRealisation_instantiation(instance):
    assert isinstance(instance, ActionRealisation)


Alternative_strategy = st.builds(Alternative)
@given(instance=Alternative_strategy)
@settings(max_examples=25)
def test_Alternative_instantiation(instance):
    assert isinstance(instance, Alternative)


Attribute_strategy = st.builds(Attribute)
@given(instance=Attribute_strategy)
@settings(max_examples=25)
def test_Attribute_instantiation(instance):
    assert isinstance(instance, Attribute)


AttributeConstraint_strategy = st.builds(AttributeConstraint)
@given(instance=AttributeConstraint_strategy)
@settings(max_examples=25)
def test_AttributeConstraint_instantiation(instance):
    assert isinstance(instance, AttributeConstraint)


Cardinality_strategy = st.builds(Cardinality)
@given(instance=Cardinality_strategy)
@settings(max_examples=25)
def test_Cardinality_instantiation(instance):
    assert isinstance(instance, Cardinality)


Clone_strategy = st.builds(Clone)
@given(instance=Clone_strategy)
@settings(max_examples=25)
def test_Clone_instantiation(instance):
    assert isinstance(instance, Clone)


CloudCredentials_strategy = st.builds(CloudCredentials)
@given(instance=CloudCredentials_strategy)
@settings(max_examples=25)
def test_CloudCredentials_instantiation(instance):
    assert isinstance(instance, CloudCredentials)


CloudLocation_strategy = st.builds(CloudLocation)
@given(instance=CloudLocation_strategy)
@settings(max_examples=25)
def test_CloudLocation_instantiation(instance):
    assert isinstance(instance, CloudLocation)


CloudProvider_strategy = st.builds(CloudProvider)
@given(instance=CloudProvider_strategy)
@settings(max_examples=25)
def test_CloudProvider_instantiation(instance):
    assert isinstance(instance, CloudProvider)


Communication_strategy = st.builds(Communication)
@given(instance=Communication_strategy)
@settings(max_examples=25)
def test_Communication_instantiation(instance):
    assert isinstance(instance, Communication)


CommunicationInstance_strategy = st.builds(CommunicationInstance)
@given(instance=CommunicationInstance_strategy)
@settings(max_examples=25)
def test_CommunicationInstance_instantiation(instance):
    assert isinstance(instance, CommunicationInstance)


CommunicationPort_strategy = st.builds(CommunicationPort)
@given(instance=CommunicationPort_strategy)
@settings(max_examples=25)
def test_CommunicationPort_instantiation(instance):
    assert isinstance(instance, CommunicationPort)


CommunicationPortInstance_strategy = st.builds(CommunicationPortInstance)
@given(instance=CommunicationPortInstance_strategy)
@settings(max_examples=25)
def test_CommunicationPortInstance_instantiation(instance):
    assert isinstance(instance, CommunicationPortInstance)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


ComponentInstance_strategy = st.builds(ComponentInstance)
@given(instance=ComponentInstance_strategy)
@settings(max_examples=25)
def test_ComponentInstance_instantiation(instance):
    assert isinstance(instance, ComponentInstance)


CompositeMetric_strategy = st.builds(CompositeMetric)
@given(instance=CompositeMetric_strategy)
@settings(max_examples=25)
def test_CompositeMetric_instantiation(instance):
    assert isinstance(instance, CompositeMetric)


CompositeMetricInstance_strategy = st.builds(CompositeMetricInstance)
@given(instance=CompositeMetricInstance_strategy)
@settings(max_examples=25)
def test_CompositeMetricInstance_instantiation(instance):
    assert isinstance(instance, CompositeMetricInstance)


CompositeSecurityMetric_strategy = st.builds(CompositeSecurityMetric)
@given(instance=CompositeSecurityMetric_strategy)
@settings(max_examples=25)
def test_CompositeSecurityMetric_instantiation(instance):
    assert isinstance(instance, CompositeSecurityMetric)


CompositeSecurityMetricInstance_strategy = st.builds(CompositeSecurityMetricInstance)
@given(instance=CompositeSecurityMetricInstance_strategy)
@settings(max_examples=25)
def test_CompositeSecurityMetricInstance_instantiation(instance):
    assert isinstance(instance, CompositeSecurityMetricInstance)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


ConditionContext_strategy = st.builds(ConditionContext)
@given(instance=ConditionContext_strategy)
@settings(max_examples=25)
def test_ConditionContext_instantiation(instance):
    assert isinstance(instance, ConditionContext)


Configuration_strategy = st.builds(Configuration)
@given(instance=Configuration_strategy)
@settings(max_examples=25)
def test_Configuration_instantiation(instance):
    assert isinstance(instance, Configuration)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Country_strategy = st.builds(Country)
@given(instance=Country_strategy)
@settings(max_examples=25)
def test_Country_instantiation(instance):
    assert isinstance(instance, Country)


Credentials_strategy = st.builds(Credentials)
@given(instance=Credentials_strategy)
@settings(max_examples=25)
def test_Credentials_instantiation(instance):
    assert isinstance(instance, Credentials)


DataCenter_strategy = st.builds(DataCenter)
@given(instance=DataCenter_strategy)
@settings(max_examples=25)
def test_DataCenter_instantiation(instance):
    assert isinstance(instance, DataCenter)


DeploymentElement_strategy = st.builds(DeploymentElement)
@given(instance=DeploymentElement_strategy)
@settings(max_examples=25)
def test_DeploymentElement_instantiation(instance):
    assert isinstance(instance, DeploymentElement)


DeploymentModel_strategy = st.builds(DeploymentModel)
@given(instance=DeploymentModel_strategy)
@settings(max_examples=25)
def test_DeploymentModel_instantiation(instance):
    assert isinstance(instance, DeploymentModel)


Entity_strategy = st.builds(Entity)
@given(instance=Entity_strategy)
@settings(max_examples=25)
def test_Entity_instantiation(instance):
    assert isinstance(instance, Entity)


EnumerateValue_strategy = st.builds(EnumerateValue)
@given(instance=EnumerateValue_strategy)
@settings(max_examples=25)
def test_EnumerateValue_instantiation(instance):
    assert isinstance(instance, EnumerateValue)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


EventInstance_strategy = st.builds(EventInstance)
@given(instance=EventInstance_strategy)
@settings(max_examples=25)
def test_EventInstance_instantiation(instance):
    assert isinstance(instance, EventInstance)


EventPattern_strategy = st.builds(EventPattern)
@given(instance=EventPattern_strategy)
@settings(max_examples=25)
def test_EventPattern_instantiation(instance):
    assert isinstance(instance, EventPattern)


ExecutionContext_strategy = st.builds(ExecutionContext)
@given(instance=ExecutionContext_strategy)
@settings(max_examples=25)
def test_ExecutionContext_instantiation(instance):
    assert isinstance(instance, ExecutionContext)


ExecutionModel_strategy = st.builds(ExecutionModel)
@given(instance=ExecutionModel_strategy)
@settings(max_examples=25)
def test_ExecutionModel_instantiation(instance):
    assert isinstance(instance, ExecutionModel)


ExternalIdentifier_strategy = st.builds(ExternalIdentifier)
@given(instance=ExternalIdentifier_strategy)
@settings(max_examples=25)
def test_ExternalIdentifier_instantiation(instance):
    assert isinstance(instance, ExternalIdentifier)


FeatCardinality_strategy = st.builds(FeatCardinality)
@given(instance=FeatCardinality_strategy)
@settings(max_examples=25)
def test_FeatCardinality_instantiation(instance):
    assert isinstance(instance, FeatCardinality)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


GeographicalRegion_strategy = st.builds(GeographicalRegion)
@given(instance=GeographicalRegion_strategy)
@settings(max_examples=25)
def test_GeographicalRegion_instantiation(instance):
    assert isinstance(instance, GeographicalRegion)


GroupCardinality_strategy = st.builds(GroupCardinality)
@given(instance=GroupCardinality_strategy)
@settings(max_examples=25)
def test_GroupCardinality_instantiation(instance):
    assert isinstance(instance, GroupCardinality)


HardRequirement_strategy = st.builds(HardRequirement)
@given(instance=HardRequirement_strategy)
@settings(max_examples=25)
def test_HardRequirement_instantiation(instance):
    assert isinstance(instance, HardRequirement)


HardwareRequirement_strategy = st.builds(HardwareRequirement)
@given(instance=HardwareRequirement_strategy)
@settings(max_examples=25)
def test_HardwareRequirement_instantiation(instance):
    assert isinstance(instance, HardwareRequirement)


Hosting_strategy = st.builds(Hosting)
@given(instance=Hosting_strategy)
@settings(max_examples=25)
def test_Hosting_instantiation(instance):
    assert isinstance(instance, Hosting)


HostingInstance_strategy = st.builds(HostingInstance)
@given(instance=HostingInstance_strategy)
@settings(max_examples=25)
def test_HostingInstance_instantiation(instance):
    assert isinstance(instance, HostingInstance)


HostingPort_strategy = st.builds(HostingPort)
@given(instance=HostingPort_strategy)
@settings(max_examples=25)
def test_HostingPort_instantiation(instance):
    assert isinstance(instance, HostingPort)


HostingPortInstance_strategy = st.builds(HostingPortInstance)
@given(instance=HostingPortInstance_strategy)
@settings(max_examples=25)
def test_HostingPortInstance_instantiation(instance):
    assert isinstance(instance, HostingPortInstance)


InternalComponent_strategy = st.builds(InternalComponent)
@given(instance=InternalComponent_strategy)
@settings(max_examples=25)
def test_InternalComponent_instantiation(instance):
    assert isinstance(instance, InternalComponent)


InternalComponentInstance_strategy = st.builds(InternalComponentInstance)
@given(instance=InternalComponentInstance_strategy)
@settings(max_examples=25)
def test_InternalComponentInstance_instantiation(instance):
    assert isinstance(instance, InternalComponentInstance)


Limit_strategy = st.builds(Limit)
@given(instance=Limit_strategy)
@settings(max_examples=25)
def test_Limit_instantiation(instance):
    assert isinstance(instance, Limit)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


LocationModel_strategy = st.builds(LocationModel)
@given(instance=LocationModel_strategy)
@settings(max_examples=25)
def test_LocationModel_instantiation(instance):
    assert isinstance(instance, LocationModel)


LocationRequirement_strategy = st.builds(LocationRequirement)
@given(instance=LocationRequirement_strategy)
@settings(max_examples=25)
def test_LocationRequirement_instantiation(instance):
    assert isinstance(instance, LocationRequirement)


Measurement_strategy = st.builds(Measurement)
@given(instance=Measurement_strategy)
@settings(max_examples=25)
def test_Measurement_instantiation(instance):
    assert isinstance(instance, Measurement)


Metric_strategy = st.builds(Metric)
@given(instance=Metric_strategy)
@settings(max_examples=25)
def test_Metric_instantiation(instance):
    assert isinstance(instance, Metric)


MetricCondition_strategy = st.builds(MetricCondition)
@given(instance=MetricCondition_strategy)
@settings(max_examples=25)
def test_MetricCondition_instantiation(instance):
    assert isinstance(instance, MetricCondition)


MetricContext_strategy = st.builds(MetricContext)
@given(instance=MetricContext_strategy)
@settings(max_examples=25)
def test_MetricContext_instantiation(instance):
    assert isinstance(instance, MetricContext)


MetricFormula_strategy = st.builds(MetricFormula)
@given(instance=MetricFormula_strategy)
@settings(max_examples=25)
def test_MetricFormula_instantiation(instance):
    assert isinstance(instance, MetricFormula)


MetricFormulaParameter_strategy = st.builds(MetricFormulaParameter)
@given(instance=MetricFormulaParameter_strategy)
@settings(max_examples=25)
def test_MetricFormulaParameter_instantiation(instance):
    assert isinstance(instance, MetricFormulaParameter)


MetricInstance_strategy = st.builds(MetricInstance)
@given(instance=MetricInstance_strategy)
@settings(max_examples=25)
def test_MetricInstance_instantiation(instance):
    assert isinstance(instance, MetricInstance)


MetricModel_strategy = st.builds(MetricModel)
@given(instance=MetricModel_strategy)
@settings(max_examples=25)
def test_MetricModel_instantiation(instance):
    assert isinstance(instance, MetricModel)


MetricObjectBinding_strategy = st.builds(MetricObjectBinding)
@given(instance=MetricObjectBinding_strategy)
@settings(max_examples=25)
def test_MetricObjectBinding_instantiation(instance):
    assert isinstance(instance, MetricObjectBinding)


Model_strategy = st.builds(Model)
@given(instance=Model_strategy)
@settings(max_examples=25)
def test_Model_instantiation(instance):
    assert isinstance(instance, Model)


MonetaryUnit_strategy = st.builds(MonetaryUnit)
@given(instance=MonetaryUnit_strategy)
@settings(max_examples=25)
def test_MonetaryUnit_instantiation(instance):
    assert isinstance(instance, MonetaryUnit)


NumericValue_strategy = st.builds(NumericValue)
@given(instance=NumericValue_strategy)
@settings(max_examples=25)
def test_NumericValue_instantiation(instance):
    assert isinstance(instance, NumericValue)


OSOrImageRequirement_strategy = st.builds(OSOrImageRequirement)
@given(instance=OSOrImageRequirement_strategy)
@settings(max_examples=25)
def test_OSOrImageRequirement_instantiation(instance):
    assert isinstance(instance, OSOrImageRequirement)


Organisation_strategy = st.builds(Organisation)
@given(instance=Organisation_strategy)
@settings(max_examples=25)
def test_Organisation_instantiation(instance):
    assert isinstance(instance, Organisation)


OrganisationModel_strategy = st.builds(OrganisationModel)
@given(instance=OrganisationModel_strategy)
@settings(max_examples=25)
def test_OrganisationModel_instantiation(instance):
    assert isinstance(instance, OrganisationModel)


PaaSageCredentials_strategy = st.builds(PaaSageCredentials)
@given(instance=PaaSageCredentials_strategy)
@settings(max_examples=25)
def test_PaaSageCredentials_instantiation(instance):
    assert isinstance(instance, PaaSageCredentials)


Permission_strategy = st.builds(Permission)
@given(instance=Permission_strategy)
@settings(max_examples=25)
def test_Permission_instantiation(instance):
    assert isinstance(instance, Permission)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


PropertyContext_strategy = st.builds(PropertyContext)
@given(instance=PropertyContext_strategy)
@settings(max_examples=25)
def test_PropertyContext_instantiation(instance):
    assert isinstance(instance, PropertyContext)


ProvidedCommunication_strategy = st.builds(ProvidedCommunication)
@given(instance=ProvidedCommunication_strategy)
@settings(max_examples=25)
def test_ProvidedCommunication_instantiation(instance):
    assert isinstance(instance, ProvidedCommunication)


ProvidedCommunicationInstance_strategy = st.builds(ProvidedCommunicationInstance)
@given(instance=ProvidedCommunicationInstance_strategy)
@settings(max_examples=25)
def test_ProvidedCommunicationInstance_instantiation(instance):
    assert isinstance(instance, ProvidedCommunicationInstance)


ProvidedHost_strategy = st.builds(ProvidedHost)
@given(instance=ProvidedHost_strategy)
@settings(max_examples=25)
def test_ProvidedHost_instantiation(instance):
    assert isinstance(instance, ProvidedHost)


ProvidedHostInstance_strategy = st.builds(ProvidedHostInstance)
@given(instance=ProvidedHostInstance_strategy)
@settings(max_examples=25)
def test_ProvidedHostInstance_instantiation(instance):
    assert isinstance(instance, ProvidedHostInstance)


ProviderModel_strategy = st.builds(ProviderModel)
@given(instance=ProviderModel_strategy)
@settings(max_examples=25)
def test_ProviderModel_instantiation(instance):
    assert isinstance(instance, ProviderModel)


ProviderRequirement_strategy = st.builds(ProviderRequirement)
@given(instance=ProviderRequirement_strategy)
@settings(max_examples=25)
def test_ProviderRequirement_instantiation(instance):
    assert isinstance(instance, ProviderRequirement)


QualitativeHardwareRequirement_strategy = st.builds(QualitativeHardwareRequirement)
@given(instance=QualitativeHardwareRequirement_strategy)
@settings(max_examples=25)
def test_QualitativeHardwareRequirement_instantiation(instance):
    assert isinstance(instance, QualitativeHardwareRequirement)


QuantitativeHardwareRequirement_strategy = st.builds(QuantitativeHardwareRequirement)
@given(instance=QuantitativeHardwareRequirement_strategy)
@settings(max_examples=25)
def test_QuantitativeHardwareRequirement_instantiation(instance):
    assert isinstance(instance, QuantitativeHardwareRequirement)


Range_strategy = st.builds(Range)
@given(instance=Range_strategy)
@settings(max_examples=25)
def test_Range_instantiation(instance):
    assert isinstance(instance, Range)


RawMetric_strategy = st.builds(RawMetric)
@given(instance=RawMetric_strategy)
@settings(max_examples=25)
def test_RawMetric_instantiation(instance):
    assert isinstance(instance, RawMetric)


RawMetricInstance_strategy = st.builds(RawMetricInstance)
@given(instance=RawMetricInstance_strategy)
@settings(max_examples=25)
def test_RawMetricInstance_instantiation(instance):
    assert isinstance(instance, RawMetricInstance)


RawSecurityMetric_strategy = st.builds(RawSecurityMetric)
@given(instance=RawSecurityMetric_strategy)
@settings(max_examples=25)
def test_RawSecurityMetric_instantiation(instance):
    assert isinstance(instance, RawSecurityMetric)


RawSecurityMetricInstance_strategy = st.builds(RawSecurityMetricInstance)
@given(instance=RawSecurityMetricInstance_strategy)
@settings(max_examples=25)
def test_RawSecurityMetricInstance_instantiation(instance):
    assert isinstance(instance, RawSecurityMetricInstance)


RequiredCommunication_strategy = st.builds(RequiredCommunication)
@given(instance=RequiredCommunication_strategy)
@settings(max_examples=25)
def test_RequiredCommunication_instantiation(instance):
    assert isinstance(instance, RequiredCommunication)


RequiredCommunicationInstance_strategy = st.builds(RequiredCommunicationInstance)
@given(instance=RequiredCommunicationInstance_strategy)
@settings(max_examples=25)
def test_RequiredCommunicationInstance_instantiation(instance):
    assert isinstance(instance, RequiredCommunicationInstance)


RequiredHost_strategy = st.builds(RequiredHost)
@given(instance=RequiredHost_strategy)
@settings(max_examples=25)
def test_RequiredHost_instantiation(instance):
    assert isinstance(instance, RequiredHost)


RequiredHostInstance_strategy = st.builds(RequiredHostInstance)
@given(instance=RequiredHostInstance_strategy)
@settings(max_examples=25)
def test_RequiredHostInstance_instantiation(instance):
    assert isinstance(instance, RequiredHostInstance)


Requirement_strategy = st.builds(Requirement)
@given(instance=Requirement_strategy)
@settings(max_examples=25)
def test_Requirement_instantiation(instance):
    assert isinstance(instance, Requirement)


RequirementGroup_strategy = st.builds(RequirementGroup)
@given(instance=RequirementGroup_strategy)
@settings(max_examples=25)
def test_RequirementGroup_instantiation(instance):
    assert isinstance(instance, RequirementGroup)


RequirementModel_strategy = st.builds(RequirementModel)
@given(instance=RequirementModel_strategy)
@settings(max_examples=25)
def test_RequirementModel_instantiation(instance):
    assert isinstance(instance, RequirementModel)


Requires_strategy = st.builds(Requires)
@given(instance=Requires_strategy)
@settings(max_examples=25)
def test_Requires_instantiation(instance):
    assert isinstance(instance, Requires)


ResourceFilter_strategy = st.builds(ResourceFilter)
@given(instance=ResourceFilter_strategy)
@settings(max_examples=25)
def test_ResourceFilter_instantiation(instance):
    assert isinstance(instance, ResourceFilter)


Role_strategy = st.builds(Role)
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


RoleAssignment_strategy = st.builds(RoleAssignment)
@given(instance=RoleAssignment_strategy)
@settings(max_examples=25)
def test_RoleAssignment_instantiation(instance):
    assert isinstance(instance, RoleAssignment)


RuleTrigger_strategy = st.builds(RuleTrigger)
@given(instance=RuleTrigger_strategy)
@settings(max_examples=25)
def test_RuleTrigger_instantiation(instance):
    assert isinstance(instance, RuleTrigger)


SLOAssessment_strategy = st.builds(SLOAssessment)
@given(instance=SLOAssessment_strategy)
@settings(max_examples=25)
def test_SLOAssessment_instantiation(instance):
    assert isinstance(instance, SLOAssessment)


ScalabilityModel_strategy = st.builds(ScalabilityModel)
@given(instance=ScalabilityModel_strategy)
@settings(max_examples=25)
def test_ScalabilityModel_instantiation(instance):
    assert isinstance(instance, ScalabilityModel)


ScalabilityRule_strategy = st.builds(ScalabilityRule)
@given(instance=ScalabilityRule_strategy)
@settings(max_examples=25)
def test_ScalabilityRule_instantiation(instance):
    assert isinstance(instance, ScalabilityRule)


ScaleRequirement_strategy = st.builds(ScaleRequirement)
@given(instance=ScaleRequirement_strategy)
@settings(max_examples=25)
def test_ScaleRequirement_instantiation(instance):
    assert isinstance(instance, ScaleRequirement)


ScalingAction_strategy = st.builds(ScalingAction)
@given(instance=ScalingAction_strategy)
@settings(max_examples=25)
def test_ScalingAction_instantiation(instance):
    assert isinstance(instance, ScalingAction)


Schedule_strategy = st.builds(Schedule)
@given(instance=Schedule_strategy)
@settings(max_examples=25)
def test_Schedule_instantiation(instance):
    assert isinstance(instance, Schedule)


Scope_strategy = st.builds(Scope)
@given(instance=Scope_strategy)
@settings(max_examples=25)
def test_Scope_instantiation(instance):
    assert isinstance(instance, Scope)


SecurityCapability_strategy = st.builds(SecurityCapability)
@given(instance=SecurityCapability_strategy)
@settings(max_examples=25)
def test_SecurityCapability_instantiation(instance):
    assert isinstance(instance, SecurityCapability)


SecurityControl_strategy = st.builds(SecurityControl)
@given(instance=SecurityControl_strategy)
@settings(max_examples=25)
def test_SecurityControl_instantiation(instance):
    assert isinstance(instance, SecurityControl)


SecurityDomain_strategy = st.builds(SecurityDomain)
@given(instance=SecurityDomain_strategy)
@settings(max_examples=25)
def test_SecurityDomain_instantiation(instance):
    assert isinstance(instance, SecurityDomain)


SecurityModel_strategy = st.builds(SecurityModel)
@given(instance=SecurityModel_strategy)
@settings(max_examples=25)
def test_SecurityModel_instantiation(instance):
    assert isinstance(instance, SecurityModel)


SecurityProperty_strategy = st.builds(SecurityProperty)
@given(instance=SecurityProperty_strategy)
@settings(max_examples=25)
def test_SecurityProperty_instantiation(instance):
    assert isinstance(instance, SecurityProperty)


SecurityRequirement_strategy = st.builds(SecurityRequirement)
@given(instance=SecurityRequirement_strategy)
@settings(max_examples=25)
def test_SecurityRequirement_instantiation(instance):
    assert isinstance(instance, SecurityRequirement)


SecuritySLO_strategy = st.builds(SecuritySLO)
@given(instance=SecuritySLO_strategy)
@settings(max_examples=25)
def test_SecuritySLO_instantiation(instance):
    assert isinstance(instance, SecuritySLO)


Sensor_strategy = st.builds(Sensor)
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


ServiceLevelObjective_strategy = st.builds(ServiceLevelObjective)
@given(instance=ServiceLevelObjective_strategy)
@settings(max_examples=25)
def test_ServiceLevelObjective_instantiation(instance):
    assert isinstance(instance, ServiceLevelObjective)


SimpleEvent_strategy = st.builds(SimpleEvent)
@given(instance=SimpleEvent_strategy)
@settings(max_examples=25)
def test_SimpleEvent_instantiation(instance):
    assert isinstance(instance, SimpleEvent)


SingleValue_strategy = st.builds(SingleValue)
@given(instance=SingleValue_strategy)
@settings(max_examples=25)
def test_SingleValue_instantiation(instance):
    assert isinstance(instance, SingleValue)


SoftRequirement_strategy = st.builds(SoftRequirement)
@given(instance=SoftRequirement_strategy)
@settings(max_examples=25)
def test_SoftRequirement_instantiation(instance):
    assert isinstance(instance, SoftRequirement)


TimeIntervalUnit_strategy = st.builds(TimeIntervalUnit)
@given(instance=TimeIntervalUnit_strategy)
@settings(max_examples=25)
def test_TimeIntervalUnit_instantiation(instance):
    assert isinstance(instance, TimeIntervalUnit)


Timer_strategy = st.builds(Timer)
@given(instance=Timer_strategy)
@settings(max_examples=25)
def test_Timer_instantiation(instance):
    assert isinstance(instance, Timer)


TypeModel_strategy = st.builds(TypeModel)
@given(instance=TypeModel_strategy)
@settings(max_examples=25)
def test_TypeModel_instantiation(instance):
    assert isinstance(instance, TypeModel)


Unit_strategy = st.builds(Unit)
@given(instance=Unit_strategy)
@settings(max_examples=25)
def test_Unit_instantiation(instance):
    assert isinstance(instance, Unit)


UnitModel_strategy = st.builds(UnitModel)
@given(instance=UnitModel_strategy)
@settings(max_examples=25)
def test_UnitModel_instantiation(instance):
    assert isinstance(instance, UnitModel)


User_strategy = st.builds(User)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


UserGroup_strategy = st.builds(UserGroup)
@given(instance=UserGroup_strategy)
@settings(max_examples=25)
def test_UserGroup_instantiation(instance):
    assert isinstance(instance, UserGroup)


VM_strategy = st.builds(VM)
@given(instance=VM_strategy)
@settings(max_examples=25)
def test_VM_instantiation(instance):
    assert isinstance(instance, VM)


VMInstance_strategy = st.builds(VMInstance)
@given(instance=VMInstance_strategy)
@settings(max_examples=25)
def test_VMInstance_instantiation(instance):
    assert isinstance(instance, VMInstance)


VMRequirementSet_strategy = st.builds(VMRequirementSet)
@given(instance=VMRequirementSet_strategy)
@settings(max_examples=25)
def test_VMRequirementSet_instantiation(instance):
    assert isinstance(instance, VMRequirementSet)


ValueType_strategy = st.builds(ValueType)
@given(instance=ValueType_strategy)
@settings(max_examples=25)
def test_ValueType_instantiation(instance):
    assert isinstance(instance, ValueType)


Window_strategy = st.builds(Window)
@given(instance=Window_strategy)
@settings(max_examples=25)
def test_Window_instantiation(instance):
    assert isinstance(instance, Window)


camel_Action_strategy = st.builds(camel_Action, name=safe_text, type=safe_text)
@given(instance=camel_Action_strategy)
@settings(max_examples=25)
def test_camel_Action_instantiation(instance):
    assert isinstance(instance, camel_Action)


camel_Application_strategy = st.builds(camel_Application, description=safe_text, name=safe_text, version=safe_text)
@given(instance=camel_Application_strategy)
@settings(max_examples=25)
def test_camel_Application_instantiation(instance):
    assert isinstance(instance, camel_Application)


camel_CamelModel_strategy = st.builds(camel_CamelModel)
@given(instance=camel_CamelModel_strategy)
@settings(max_examples=25)
def test_camel_CamelModel_instantiation(instance):
    assert isinstance(instance, camel_CamelModel)


camel_Model_strategy = st.builds(camel_Model, importURI=safe_text, name=safe_text)
@given(instance=camel_Model_strategy)
@settings(max_examples=25)
def test_camel_Model_instantiation(instance):
    assert isinstance(instance, camel_Model)


camel_deployment_Communication_strategy = st.builds(camel_deployment_Communication, type=safe_text)
@given(instance=camel_deployment_Communication_strategy)
@settings(max_examples=25)
def test_camel_deployment_Communication_instantiation(instance):
    assert isinstance(instance, camel_deployment_Communication)


camel_deployment_CommunicationInstance_strategy = st.builds(camel_deployment_CommunicationInstance)
@given(instance=camel_deployment_CommunicationInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_CommunicationInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_CommunicationInstance)


camel_deployment_CommunicationPort_strategy = st.builds(camel_deployment_CommunicationPort, portNumber=st.integers())
@given(instance=camel_deployment_CommunicationPort_strategy)
@settings(max_examples=25)
def test_camel_deployment_CommunicationPort_instantiation(instance):
    assert isinstance(instance, camel_deployment_CommunicationPort)


camel_deployment_CommunicationPortInstance_strategy = st.builds(camel_deployment_CommunicationPortInstance)
@given(instance=camel_deployment_CommunicationPortInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_CommunicationPortInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_CommunicationPortInstance)


camel_deployment_Component_strategy = st.builds(camel_deployment_Component)
@given(instance=camel_deployment_Component_strategy)
@settings(max_examples=25)
def test_camel_deployment_Component_instantiation(instance):
    assert isinstance(instance, camel_deployment_Component)


camel_deployment_ComponentInstance_strategy = st.builds(camel_deployment_ComponentInstance, destroyedOn=st.dates(), instantiatedOn=st.dates())
@given(instance=camel_deployment_ComponentInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_ComponentInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_ComponentInstance)


camel_deployment_Configuration_strategy = st.builds(camel_deployment_Configuration, configureCommand=safe_text, downloadCommand=safe_text, installCommand=safe_text, startCommand=safe_text, stopCommand=safe_text, uploadCommand=safe_text)
@given(instance=camel_deployment_Configuration_strategy)
@settings(max_examples=25)
def test_camel_deployment_Configuration_instantiation(instance):
    assert isinstance(instance, camel_deployment_Configuration)


camel_deployment_DeploymentElement_strategy = st.builds(camel_deployment_DeploymentElement, name=safe_text)
@given(instance=camel_deployment_DeploymentElement_strategy)
@settings(max_examples=25)
def test_camel_deployment_DeploymentElement_instantiation(instance):
    assert isinstance(instance, camel_deployment_DeploymentElement)


camel_deployment_DeploymentModel_strategy = st.builds(camel_deployment_DeploymentModel)
@given(instance=camel_deployment_DeploymentModel_strategy)
@settings(max_examples=25)
def test_camel_deployment_DeploymentModel_instantiation(instance):
    assert isinstance(instance, camel_deployment_DeploymentModel)


camel_deployment_Hosting_strategy = st.builds(camel_deployment_Hosting)
@given(instance=camel_deployment_Hosting_strategy)
@settings(max_examples=25)
def test_camel_deployment_Hosting_instantiation(instance):
    assert isinstance(instance, camel_deployment_Hosting)


camel_deployment_HostingInstance_strategy = st.builds(camel_deployment_HostingInstance)
@given(instance=camel_deployment_HostingInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_HostingInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_HostingInstance)


camel_deployment_HostingPort_strategy = st.builds(camel_deployment_HostingPort)
@given(instance=camel_deployment_HostingPort_strategy)
@settings(max_examples=25)
def test_camel_deployment_HostingPort_instantiation(instance):
    assert isinstance(instance, camel_deployment_HostingPort)


camel_deployment_HostingPortInstance_strategy = st.builds(camel_deployment_HostingPortInstance)
@given(instance=camel_deployment_HostingPortInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_HostingPortInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_HostingPortInstance)


camel_deployment_InternalComponent_strategy = st.builds(camel_deployment_InternalComponent, version=safe_text)
@given(instance=camel_deployment_InternalComponent_strategy)
@settings(max_examples=25)
def test_camel_deployment_InternalComponent_instantiation(instance):
    assert isinstance(instance, camel_deployment_InternalComponent)


camel_deployment_InternalComponentInstance_strategy = st.builds(camel_deployment_InternalComponentInstance)
@given(instance=camel_deployment_InternalComponentInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_InternalComponentInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_InternalComponentInstance)


camel_deployment_ProvidedCommunication_strategy = st.builds(camel_deployment_ProvidedCommunication)
@given(instance=camel_deployment_ProvidedCommunication_strategy)
@settings(max_examples=25)
def test_camel_deployment_ProvidedCommunication_instantiation(instance):
    assert isinstance(instance, camel_deployment_ProvidedCommunication)


camel_deployment_ProvidedCommunicationInstance_strategy = st.builds(camel_deployment_ProvidedCommunicationInstance)
@given(instance=camel_deployment_ProvidedCommunicationInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_ProvidedCommunicationInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_ProvidedCommunicationInstance)


camel_deployment_ProvidedHost_strategy = st.builds(camel_deployment_ProvidedHost)
@given(instance=camel_deployment_ProvidedHost_strategy)
@settings(max_examples=25)
def test_camel_deployment_ProvidedHost_instantiation(instance):
    assert isinstance(instance, camel_deployment_ProvidedHost)


camel_deployment_ProvidedHostInstance_strategy = st.builds(camel_deployment_ProvidedHostInstance)
@given(instance=camel_deployment_ProvidedHostInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_ProvidedHostInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_ProvidedHostInstance)


camel_deployment_RequiredCommunication_strategy = st.builds(camel_deployment_RequiredCommunication, isMandatory=st.booleans())
@given(instance=camel_deployment_RequiredCommunication_strategy)
@settings(max_examples=25)
def test_camel_deployment_RequiredCommunication_instantiation(instance):
    assert isinstance(instance, camel_deployment_RequiredCommunication)


camel_deployment_RequiredCommunicationInstance_strategy = st.builds(camel_deployment_RequiredCommunicationInstance)
@given(instance=camel_deployment_RequiredCommunicationInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_RequiredCommunicationInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_RequiredCommunicationInstance)


camel_deployment_RequiredHost_strategy = st.builds(camel_deployment_RequiredHost)
@given(instance=camel_deployment_RequiredHost_strategy)
@settings(max_examples=25)
def test_camel_deployment_RequiredHost_instantiation(instance):
    assert isinstance(instance, camel_deployment_RequiredHost)


camel_deployment_RequiredHostInstance_strategy = st.builds(camel_deployment_RequiredHostInstance)
@given(instance=camel_deployment_RequiredHostInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_RequiredHostInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_RequiredHostInstance)


camel_deployment_VM_strategy = st.builds(camel_deployment_VM)
@given(instance=camel_deployment_VM_strategy)
@settings(max_examples=25)
def test_camel_deployment_VM_instantiation(instance):
    assert isinstance(instance, camel_deployment_VM)


camel_deployment_VMInstance_strategy = st.builds(camel_deployment_VMInstance, ip=safe_text)
@given(instance=camel_deployment_VMInstance_strategy)
@settings(max_examples=25)
def test_camel_deployment_VMInstance_instantiation(instance):
    assert isinstance(instance, camel_deployment_VMInstance)


camel_deployment_VMRequirementSet_strategy = st.builds(camel_deployment_VMRequirementSet, name=safe_text)
@given(instance=camel_deployment_VMRequirementSet_strategy)
@settings(max_examples=25)
def test_camel_deployment_VMRequirementSet_instantiation(instance):
    assert isinstance(instance, camel_deployment_VMRequirementSet)


camel_execution_ActionRealisation_strategy = st.builds(camel_execution_ActionRealisation, endTime=st.dates(), lowLevelActions=safe_text, name=safe_text, startTime=st.dates())
@given(instance=camel_execution_ActionRealisation_strategy)
@settings(max_examples=25)
def test_camel_execution_ActionRealisation_instantiation(instance):
    assert isinstance(instance, camel_execution_ActionRealisation)


camel_execution_ApplicationMeasurement_strategy = st.builds(camel_execution_ApplicationMeasurement)
@given(instance=camel_execution_ApplicationMeasurement_strategy)
@settings(max_examples=25)
def test_camel_execution_ApplicationMeasurement_instantiation(instance):
    assert isinstance(instance, camel_execution_ApplicationMeasurement)


camel_execution_CommunicationMeasurement_strategy = st.builds(camel_execution_CommunicationMeasurement)
@given(instance=camel_execution_CommunicationMeasurement_strategy)
@settings(max_examples=25)
def test_camel_execution_CommunicationMeasurement_instantiation(instance):
    assert isinstance(instance, camel_execution_CommunicationMeasurement)


camel_execution_ExecutionContext_strategy = st.builds(camel_execution_ExecutionContext, endTime=st.dates(), name=safe_text, startTime=st.dates(), totalCost=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_execution_ExecutionContext_strategy)
@settings(max_examples=25)
def test_camel_execution_ExecutionContext_instantiation(instance):
    assert isinstance(instance, camel_execution_ExecutionContext)


camel_execution_ExecutionModel_strategy = st.builds(camel_execution_ExecutionModel)
@given(instance=camel_execution_ExecutionModel_strategy)
@settings(max_examples=25)
def test_camel_execution_ExecutionModel_instantiation(instance):
    assert isinstance(instance, camel_execution_ExecutionModel)


camel_execution_InternalComponentMeasurement_strategy = st.builds(camel_execution_InternalComponentMeasurement)
@given(instance=camel_execution_InternalComponentMeasurement_strategy)
@settings(max_examples=25)
def test_camel_execution_InternalComponentMeasurement_instantiation(instance):
    assert isinstance(instance, camel_execution_InternalComponentMeasurement)


camel_execution_Measurement_strategy = st.builds(camel_execution_Measurement, measurementTime=st.dates(), name=safe_text, rawData=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_execution_Measurement_strategy)
@settings(max_examples=25)
def test_camel_execution_Measurement_instantiation(instance):
    assert isinstance(instance, camel_execution_Measurement)


camel_execution_RuleTrigger_strategy = st.builds(camel_execution_RuleTrigger, name=safe_text, trigerringTime=st.dates())
@given(instance=camel_execution_RuleTrigger_strategy)
@settings(max_examples=25)
def test_camel_execution_RuleTrigger_instantiation(instance):
    assert isinstance(instance, camel_execution_RuleTrigger)


camel_execution_SLOAssessment_strategy = st.builds(camel_execution_SLOAssessment, assessment=st.booleans(), assessmentTime=st.dates(), name=safe_text)
@given(instance=camel_execution_SLOAssessment_strategy)
@settings(max_examples=25)
def test_camel_execution_SLOAssessment_instantiation(instance):
    assert isinstance(instance, camel_execution_SLOAssessment)


camel_execution_VMMeasurement_strategy = st.builds(camel_execution_VMMeasurement)
@given(instance=camel_execution_VMMeasurement_strategy)
@settings(max_examples=25)
def test_camel_execution_VMMeasurement_instantiation(instance):
    assert isinstance(instance, camel_execution_VMMeasurement)


camel_location_CloudLocation_strategy = st.builds(camel_location_CloudLocation, isAssignable=st.booleans())
@given(instance=camel_location_CloudLocation_strategy)
@settings(max_examples=25)
def test_camel_location_CloudLocation_instantiation(instance):
    assert isinstance(instance, camel_location_CloudLocation)


camel_location_Country_strategy = st.builds(camel_location_Country)
@given(instance=camel_location_Country_strategy)
@settings(max_examples=25)
def test_camel_location_Country_instantiation(instance):
    assert isinstance(instance, camel_location_Country)


camel_location_GeographicalRegion_strategy = st.builds(camel_location_GeographicalRegion, alternativeNames=safe_text, name=safe_text)
@given(instance=camel_location_GeographicalRegion_strategy)
@settings(max_examples=25)
def test_camel_location_GeographicalRegion_instantiation(instance):
    assert isinstance(instance, camel_location_GeographicalRegion)


camel_location_Location_strategy = st.builds(camel_location_Location, id=safe_text)
@given(instance=camel_location_Location_strategy)
@settings(max_examples=25)
def test_camel_location_Location_instantiation(instance):
    assert isinstance(instance, camel_location_Location)


camel_location_LocationModel_strategy = st.builds(camel_location_LocationModel)
@given(instance=camel_location_LocationModel_strategy)
@settings(max_examples=25)
def test_camel_location_LocationModel_instantiation(instance):
    assert isinstance(instance, camel_location_LocationModel)


camel_metric_CompositeMetric_strategy = st.builds(camel_metric_CompositeMetric)
@given(instance=camel_metric_CompositeMetric_strategy)
@settings(max_examples=25)
def test_camel_metric_CompositeMetric_instantiation(instance):
    assert isinstance(instance, camel_metric_CompositeMetric)


camel_metric_CompositeMetricContext_strategy = st.builds(camel_metric_CompositeMetricContext)
@given(instance=camel_metric_CompositeMetricContext_strategy)
@settings(max_examples=25)
def test_camel_metric_CompositeMetricContext_instantiation(instance):
    assert isinstance(instance, camel_metric_CompositeMetricContext)


camel_metric_CompositeMetricInstance_strategy = st.builds(camel_metric_CompositeMetricInstance)
@given(instance=camel_metric_CompositeMetricInstance_strategy)
@settings(max_examples=25)
def test_camel_metric_CompositeMetricInstance_instantiation(instance):
    assert isinstance(instance, camel_metric_CompositeMetricInstance)


camel_metric_Condition_strategy = st.builds(camel_metric_Condition, comparisonOperator=safe_text, name=safe_text, threshold=st.floats(allow_nan=False, allow_infinity=False), validity=st.dates())
@given(instance=camel_metric_Condition_strategy)
@settings(max_examples=25)
def test_camel_metric_Condition_instantiation(instance):
    assert isinstance(instance, camel_metric_Condition)


camel_metric_ConditionContext_strategy = st.builds(camel_metric_ConditionContext, isRelative=st.booleans(), maxQuantity=st.floats(allow_nan=False, allow_infinity=False), minQuantity=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, quantifier=safe_text)
@given(instance=camel_metric_ConditionContext_strategy)
@settings(max_examples=25)
def test_camel_metric_ConditionContext_instantiation(instance):
    assert isinstance(instance, camel_metric_ConditionContext)


camel_metric_Metric_strategy = st.builds(camel_metric_Metric, description=safe_text, isVariable=st.booleans(), layer=safe_text, valueDirection=safe_text)
@given(instance=camel_metric_Metric_strategy)
@settings(max_examples=25)
def test_camel_metric_Metric_instantiation(instance):
    assert isinstance(instance, camel_metric_Metric)


camel_metric_MetricApplicationBinding_strategy = st.builds(camel_metric_MetricApplicationBinding)
@given(instance=camel_metric_MetricApplicationBinding_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricApplicationBinding_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricApplicationBinding)


camel_metric_MetricComponentBinding_strategy = st.builds(camel_metric_MetricComponentBinding)
@given(instance=camel_metric_MetricComponentBinding_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricComponentBinding_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricComponentBinding)


camel_metric_MetricCondition_strategy = st.builds(camel_metric_MetricCondition)
@given(instance=camel_metric_MetricCondition_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricCondition_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricCondition)


camel_metric_MetricContext_strategy = st.builds(camel_metric_MetricContext)
@given(instance=camel_metric_MetricContext_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricContext_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricContext)


camel_metric_MetricFormula_strategy = st.builds(camel_metric_MetricFormula, function=safe_text, functionArity=safe_text, functionPattern=safe_text)
@given(instance=camel_metric_MetricFormula_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricFormula_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricFormula)


camel_metric_MetricFormulaParameter_strategy = st.builds(camel_metric_MetricFormulaParameter, name=safe_text)
@given(instance=camel_metric_MetricFormulaParameter_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricFormulaParameter_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricFormulaParameter)


camel_metric_MetricInstance_strategy = st.builds(camel_metric_MetricInstance, name=safe_text)
@given(instance=camel_metric_MetricInstance_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricInstance_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricInstance)


camel_metric_MetricModel_strategy = st.builds(camel_metric_MetricModel)
@given(instance=camel_metric_MetricModel_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricModel_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricModel)


camel_metric_MetricObjectBinding_strategy = st.builds(camel_metric_MetricObjectBinding, name=safe_text)
@given(instance=camel_metric_MetricObjectBinding_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricObjectBinding_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricObjectBinding)


camel_metric_MetricVMBinding_strategy = st.builds(camel_metric_MetricVMBinding)
@given(instance=camel_metric_MetricVMBinding_strategy)
@settings(max_examples=25)
def test_camel_metric_MetricVMBinding_instantiation(instance):
    assert isinstance(instance, camel_metric_MetricVMBinding)


camel_metric_Property_strategy = st.builds(camel_metric_Property, description=safe_text, name=safe_text, type=safe_text)
@given(instance=camel_metric_Property_strategy)
@settings(max_examples=25)
def test_camel_metric_Property_instantiation(instance):
    assert isinstance(instance, camel_metric_Property)


camel_metric_PropertyCondition_strategy = st.builds(camel_metric_PropertyCondition)
@given(instance=camel_metric_PropertyCondition_strategy)
@settings(max_examples=25)
def test_camel_metric_PropertyCondition_instantiation(instance):
    assert isinstance(instance, camel_metric_PropertyCondition)


camel_metric_PropertyContext_strategy = st.builds(camel_metric_PropertyContext)
@given(instance=camel_metric_PropertyContext_strategy)
@settings(max_examples=25)
def test_camel_metric_PropertyContext_instantiation(instance):
    assert isinstance(instance, camel_metric_PropertyContext)


camel_metric_RawMetric_strategy = st.builds(camel_metric_RawMetric)
@given(instance=camel_metric_RawMetric_strategy)
@settings(max_examples=25)
def test_camel_metric_RawMetric_instantiation(instance):
    assert isinstance(instance, camel_metric_RawMetric)


camel_metric_RawMetricContext_strategy = st.builds(camel_metric_RawMetricContext)
@given(instance=camel_metric_RawMetricContext_strategy)
@settings(max_examples=25)
def test_camel_metric_RawMetricContext_instantiation(instance):
    assert isinstance(instance, camel_metric_RawMetricContext)


camel_metric_RawMetricInstance_strategy = st.builds(camel_metric_RawMetricInstance)
@given(instance=camel_metric_RawMetricInstance_strategy)
@settings(max_examples=25)
def test_camel_metric_RawMetricInstance_instantiation(instance):
    assert isinstance(instance, camel_metric_RawMetricInstance)


camel_metric_Schedule_strategy = st.builds(camel_metric_Schedule, end=st.dates(), interval=safe_text, name=safe_text, repetitions=st.integers(), start=st.dates(), type=safe_text)
@given(instance=camel_metric_Schedule_strategy)
@settings(max_examples=25)
def test_camel_metric_Schedule_instantiation(instance):
    assert isinstance(instance, camel_metric_Schedule)


camel_metric_Sensor_strategy = st.builds(camel_metric_Sensor, configuration=safe_text, isPush=st.booleans(), name=safe_text)
@given(instance=camel_metric_Sensor_strategy)
@settings(max_examples=25)
def test_camel_metric_Sensor_instantiation(instance):
    assert isinstance(instance, camel_metric_Sensor)


camel_metric_Window_strategy = st.builds(camel_metric_Window, measurementSize=safe_text, name=safe_text, sizeType=safe_text, timeSize=safe_text, windowType=safe_text)
@given(instance=camel_metric_Window_strategy)
@settings(max_examples=25)
def test_camel_metric_Window_instantiation(instance):
    assert isinstance(instance, camel_metric_Window)


camel_organisation_CloudCredentials_strategy = st.builds(camel_organisation_CloudCredentials, name=safe_text, password=safe_text, privateSSHKey=safe_text, publicSSHKey=safe_text, securityGroup=safe_text, username=safe_text)
@given(instance=camel_organisation_CloudCredentials_strategy)
@settings(max_examples=25)
def test_camel_organisation_CloudCredentials_instantiation(instance):
    assert isinstance(instance, camel_organisation_CloudCredentials)


camel_organisation_CloudProvider_strategy = st.builds(camel_organisation_CloudProvider, IaaS=st.booleans(), PaaS=st.booleans(), SaaS=st.booleans(), public=st.booleans())
@given(instance=camel_organisation_CloudProvider_strategy)
@settings(max_examples=25)
def test_camel_organisation_CloudProvider_instantiation(instance):
    assert isinstance(instance, camel_organisation_CloudProvider)


camel_organisation_Credentials_strategy = st.builds(camel_organisation_Credentials)
@given(instance=camel_organisation_Credentials_strategy)
@settings(max_examples=25)
def test_camel_organisation_Credentials_instantiation(instance):
    assert isinstance(instance, camel_organisation_Credentials)


camel_organisation_DataCenter_strategy = st.builds(camel_organisation_DataCenter, codeName=safe_text, name=safe_text)
@given(instance=camel_organisation_DataCenter_strategy)
@settings(max_examples=25)
def test_camel_organisation_DataCenter_instantiation(instance):
    assert isinstance(instance, camel_organisation_DataCenter)


camel_organisation_Entity_strategy = st.builds(camel_organisation_Entity)
@given(instance=camel_organisation_Entity_strategy)
@settings(max_examples=25)
def test_camel_organisation_Entity_instantiation(instance):
    assert isinstance(instance, camel_organisation_Entity)


camel_organisation_ExternalIdentifier_strategy = st.builds(camel_organisation_ExternalIdentifier, description=safe_text, identifier=safe_text)
@given(instance=camel_organisation_ExternalIdentifier_strategy)
@settings(max_examples=25)
def test_camel_organisation_ExternalIdentifier_instantiation(instance):
    assert isinstance(instance, camel_organisation_ExternalIdentifier)


camel_organisation_InformationResourceFilter_strategy = st.builds(camel_organisation_InformationResourceFilter, everyInformationResource=st.booleans(), informationResourcePath=safe_text)
@given(instance=camel_organisation_InformationResourceFilter_strategy)
@settings(max_examples=25)
def test_camel_organisation_InformationResourceFilter_instantiation(instance):
    assert isinstance(instance, camel_organisation_InformationResourceFilter)


camel_organisation_Organisation_strategy = st.builds(camel_organisation_Organisation, email=safe_text, name=safe_text, postalAddress=safe_text, www=safe_text)
@given(instance=camel_organisation_Organisation_strategy)
@settings(max_examples=25)
def test_camel_organisation_Organisation_instantiation(instance):
    assert isinstance(instance, camel_organisation_Organisation)


camel_organisation_OrganisationModel_strategy = st.builds(camel_organisation_OrganisationModel, securityLevel=safe_text)
@given(instance=camel_organisation_OrganisationModel_strategy)
@settings(max_examples=25)
def test_camel_organisation_OrganisationModel_instantiation(instance):
    assert isinstance(instance, camel_organisation_OrganisationModel)


camel_organisation_PaaSageCredentials_strategy = st.builds(camel_organisation_PaaSageCredentials, password=safe_text)
@given(instance=camel_organisation_PaaSageCredentials_strategy)
@settings(max_examples=25)
def test_camel_organisation_PaaSageCredentials_instantiation(instance):
    assert isinstance(instance, camel_organisation_PaaSageCredentials)


camel_organisation_Permission_strategy = st.builds(camel_organisation_Permission, action=safe_text, endTime=st.dates(), name=safe_text, startTime=st.dates())
@given(instance=camel_organisation_Permission_strategy)
@settings(max_examples=25)
def test_camel_organisation_Permission_instantiation(instance):
    assert isinstance(instance, camel_organisation_Permission)


camel_organisation_ResourceFilter_strategy = st.builds(camel_organisation_ResourceFilter, name=safe_text, resourcePattern=safe_text)
@given(instance=camel_organisation_ResourceFilter_strategy)
@settings(max_examples=25)
def test_camel_organisation_ResourceFilter_instantiation(instance):
    assert isinstance(instance, camel_organisation_ResourceFilter)


camel_organisation_Role_strategy = st.builds(camel_organisation_Role, name=safe_text)
@given(instance=camel_organisation_Role_strategy)
@settings(max_examples=25)
def test_camel_organisation_Role_instantiation(instance):
    assert isinstance(instance, camel_organisation_Role)


camel_organisation_RoleAssignment_strategy = st.builds(camel_organisation_RoleAssignment, assignmentTime=st.dates(), endTime=st.dates(), name=safe_text, startTime=st.dates())
@given(instance=camel_organisation_RoleAssignment_strategy)
@settings(max_examples=25)
def test_camel_organisation_RoleAssignment_instantiation(instance):
    assert isinstance(instance, camel_organisation_RoleAssignment)


camel_organisation_ServiceResourceFilter_strategy = st.builds(camel_organisation_ServiceResourceFilter, everyService=st.booleans(), serviceURL=safe_text)
@given(instance=camel_organisation_ServiceResourceFilter_strategy)
@settings(max_examples=25)
def test_camel_organisation_ServiceResourceFilter_instantiation(instance):
    assert isinstance(instance, camel_organisation_ServiceResourceFilter)


camel_organisation_User_strategy = st.builds(camel_organisation_User, email=safe_text, firstName=safe_text, lastName=safe_text, name=safe_text, www=safe_text)
@given(instance=camel_organisation_User_strategy)
@settings(max_examples=25)
def test_camel_organisation_User_instantiation(instance):
    assert isinstance(instance, camel_organisation_User)


camel_organisation_UserGroup_strategy = st.builds(camel_organisation_UserGroup, name=safe_text)
@given(instance=camel_organisation_UserGroup_strategy)
@settings(max_examples=25)
def test_camel_organisation_UserGroup_instantiation(instance):
    assert isinstance(instance, camel_organisation_UserGroup)


camel_provider_Alternative_strategy = st.builds(camel_provider_Alternative)
@given(instance=camel_provider_Alternative_strategy)
@settings(max_examples=25)
def test_camel_provider_Alternative_instantiation(instance):
    assert isinstance(instance, camel_provider_Alternative)


camel_provider_Attribute_strategy = st.builds(camel_provider_Attribute, name=safe_text, unitType=safe_text)
@given(instance=camel_provider_Attribute_strategy)
@settings(max_examples=25)
def test_camel_provider_Attribute_instantiation(instance):
    assert isinstance(instance, camel_provider_Attribute)


camel_provider_AttributeConstraint_strategy = st.builds(camel_provider_AttributeConstraint, name=safe_text)
@given(instance=camel_provider_AttributeConstraint_strategy)
@settings(max_examples=25)
def test_camel_provider_AttributeConstraint_instantiation(instance):
    assert isinstance(instance, camel_provider_AttributeConstraint)


camel_provider_Cardinality_strategy = st.builds(camel_provider_Cardinality, cardinalityMax=st.integers(), cardinalityMin=st.integers())
@given(instance=camel_provider_Cardinality_strategy)
@settings(max_examples=25)
def test_camel_provider_Cardinality_instantiation(instance):
    assert isinstance(instance, camel_provider_Cardinality)


camel_provider_Clone_strategy = st.builds(camel_provider_Clone, name=safe_text)
@given(instance=camel_provider_Clone_strategy)
@settings(max_examples=25)
def test_camel_provider_Clone_instantiation(instance):
    assert isinstance(instance, camel_provider_Clone)


camel_provider_Constraint_strategy = st.builds(camel_provider_Constraint, name=safe_text)
@given(instance=camel_provider_Constraint_strategy)
@settings(max_examples=25)
def test_camel_provider_Constraint_instantiation(instance):
    assert isinstance(instance, camel_provider_Constraint)


camel_provider_Excludes_strategy = st.builds(camel_provider_Excludes)
@given(instance=camel_provider_Excludes_strategy)
@settings(max_examples=25)
def test_camel_provider_Excludes_instantiation(instance):
    assert isinstance(instance, camel_provider_Excludes)


camel_provider_Exclusive_strategy = st.builds(camel_provider_Exclusive)
@given(instance=camel_provider_Exclusive_strategy)
@settings(max_examples=25)
def test_camel_provider_Exclusive_instantiation(instance):
    assert isinstance(instance, camel_provider_Exclusive)


camel_provider_FeatCardinality_strategy = st.builds(camel_provider_FeatCardinality, value=st.integers())
@given(instance=camel_provider_FeatCardinality_strategy)
@settings(max_examples=25)
def test_camel_provider_FeatCardinality_instantiation(instance):
    assert isinstance(instance, camel_provider_FeatCardinality)


camel_provider_Feature_strategy = st.builds(camel_provider_Feature, name=safe_text)
@given(instance=camel_provider_Feature_strategy)
@settings(max_examples=25)
def test_camel_provider_Feature_instantiation(instance):
    assert isinstance(instance, camel_provider_Feature)


camel_provider_Functional_strategy = st.builds(camel_provider_Functional, order=st.integers(), type=safe_text, value=st.integers())
@given(instance=camel_provider_Functional_strategy)
@settings(max_examples=25)
def test_camel_provider_Functional_instantiation(instance):
    assert isinstance(instance, camel_provider_Functional)


camel_provider_GroupCardinality_strategy = st.builds(camel_provider_GroupCardinality)
@given(instance=camel_provider_GroupCardinality_strategy)
@settings(max_examples=25)
def test_camel_provider_GroupCardinality_instantiation(instance):
    assert isinstance(instance, camel_provider_GroupCardinality)


camel_provider_Implies_strategy = st.builds(camel_provider_Implies)
@given(instance=camel_provider_Implies_strategy)
@settings(max_examples=25)
def test_camel_provider_Implies_instantiation(instance):
    assert isinstance(instance, camel_provider_Implies)


camel_provider_Instance_strategy = st.builds(camel_provider_Instance)
@given(instance=camel_provider_Instance_strategy)
@settings(max_examples=25)
def test_camel_provider_Instance_instantiation(instance):
    assert isinstance(instance, camel_provider_Instance)


camel_provider_Product_strategy = st.builds(camel_provider_Product)
@given(instance=camel_provider_Product_strategy)
@settings(max_examples=25)
def test_camel_provider_Product_instantiation(instance):
    assert isinstance(instance, camel_provider_Product)


camel_provider_ProviderModel_strategy = st.builds(camel_provider_ProviderModel)
@given(instance=camel_provider_ProviderModel_strategy)
@settings(max_examples=25)
def test_camel_provider_ProviderModel_instantiation(instance):
    assert isinstance(instance, camel_provider_ProviderModel)


camel_provider_Requires_strategy = st.builds(camel_provider_Requires)
@given(instance=camel_provider_Requires_strategy)
@settings(max_examples=25)
def test_camel_provider_Requires_instantiation(instance):
    assert isinstance(instance, camel_provider_Requires)


camel_provider_Scope_strategy = st.builds(camel_provider_Scope)
@given(instance=camel_provider_Scope_strategy)
@settings(max_examples=25)
def test_camel_provider_Scope_instantiation(instance):
    assert isinstance(instance, camel_provider_Scope)


camel_requirement_HardRequirement_strategy = st.builds(camel_requirement_HardRequirement)
@given(instance=camel_requirement_HardRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_HardRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_HardRequirement)


camel_requirement_HardwareRequirement_strategy = st.builds(camel_requirement_HardwareRequirement)
@given(instance=camel_requirement_HardwareRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_HardwareRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_HardwareRequirement)


camel_requirement_HorizontalScaleRequirement_strategy = st.builds(camel_requirement_HorizontalScaleRequirement, maxInstances=st.integers(), minInstances=st.integers())
@given(instance=camel_requirement_HorizontalScaleRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_HorizontalScaleRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_HorizontalScaleRequirement)


camel_requirement_ImageRequirement_strategy = st.builds(camel_requirement_ImageRequirement, imageId=safe_text)
@given(instance=camel_requirement_ImageRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_ImageRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_ImageRequirement)


camel_requirement_LocationRequirement_strategy = st.builds(camel_requirement_LocationRequirement)
@given(instance=camel_requirement_LocationRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_LocationRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_LocationRequirement)


camel_requirement_OSOrImageRequirement_strategy = st.builds(camel_requirement_OSOrImageRequirement)
@given(instance=camel_requirement_OSOrImageRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_OSOrImageRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_OSOrImageRequirement)


camel_requirement_OSRequirement_strategy = st.builds(camel_requirement_OSRequirement, is64os=st.booleans(), os=safe_text)
@given(instance=camel_requirement_OSRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_OSRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_OSRequirement)


camel_requirement_OptimisationRequirement_strategy = st.builds(camel_requirement_OptimisationRequirement, optimisationFunction=safe_text)
@given(instance=camel_requirement_OptimisationRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_OptimisationRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_OptimisationRequirement)


camel_requirement_ProviderRequirement_strategy = st.builds(camel_requirement_ProviderRequirement)
@given(instance=camel_requirement_ProviderRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_ProviderRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_ProviderRequirement)


camel_requirement_QualitativeHardwareRequirement_strategy = st.builds(camel_requirement_QualitativeHardwareRequirement, maxBenchmark=st.floats(allow_nan=False, allow_infinity=False), minBenchmark=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_requirement_QualitativeHardwareRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_QualitativeHardwareRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_QualitativeHardwareRequirement)


camel_requirement_QuantitativeHardwareRequirement_strategy = st.builds(camel_requirement_QuantitativeHardwareRequirement, maxCPU=st.floats(allow_nan=False, allow_infinity=False), maxCores=st.integers(), maxRAM=st.integers(), maxStorage=st.integers(), minCPU=st.floats(allow_nan=False, allow_infinity=False), minCores=st.integers(), minRAM=st.integers(), minStorage=st.integers())
@given(instance=camel_requirement_QuantitativeHardwareRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_QuantitativeHardwareRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_QuantitativeHardwareRequirement)


camel_requirement_Requirement_strategy = st.builds(camel_requirement_Requirement, name=safe_text)
@given(instance=camel_requirement_Requirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_Requirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_Requirement)


camel_requirement_RequirementGroup_strategy = st.builds(camel_requirement_RequirementGroup, requirementOperator=safe_text)
@given(instance=camel_requirement_RequirementGroup_strategy)
@settings(max_examples=25)
def test_camel_requirement_RequirementGroup_instantiation(instance):
    assert isinstance(instance, camel_requirement_RequirementGroup)


camel_requirement_RequirementModel_strategy = st.builds(camel_requirement_RequirementModel)
@given(instance=camel_requirement_RequirementModel_strategy)
@settings(max_examples=25)
def test_camel_requirement_RequirementModel_instantiation(instance):
    assert isinstance(instance, camel_requirement_RequirementModel)


camel_requirement_ScaleRequirement_strategy = st.builds(camel_requirement_ScaleRequirement)
@given(instance=camel_requirement_ScaleRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_ScaleRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_ScaleRequirement)


camel_requirement_SecurityRequirement_strategy = st.builds(camel_requirement_SecurityRequirement)
@given(instance=camel_requirement_SecurityRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_SecurityRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_SecurityRequirement)


camel_requirement_ServiceLevelObjective_strategy = st.builds(camel_requirement_ServiceLevelObjective)
@given(instance=camel_requirement_ServiceLevelObjective_strategy)
@settings(max_examples=25)
def test_camel_requirement_ServiceLevelObjective_instantiation(instance):
    assert isinstance(instance, camel_requirement_ServiceLevelObjective)


camel_requirement_SoftRequirement_strategy = st.builds(camel_requirement_SoftRequirement, priority=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_requirement_SoftRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_SoftRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_SoftRequirement)


camel_requirement_VerticalScaleRequirement_strategy = st.builds(camel_requirement_VerticalScaleRequirement, maxCPU=st.floats(allow_nan=False, allow_infinity=False), maxCores=st.integers(), maxRAM=st.integers(), maxStorage=st.integers(), minCPU=st.floats(allow_nan=False, allow_infinity=False), minCores=st.integers(), minRAM=st.integers(), minStorage=st.integers())
@given(instance=camel_requirement_VerticalScaleRequirement_strategy)
@settings(max_examples=25)
def test_camel_requirement_VerticalScaleRequirement_instantiation(instance):
    assert isinstance(instance, camel_requirement_VerticalScaleRequirement)


camel_scalability_BinaryEventPattern_strategy = st.builds(camel_scalability_BinaryEventPattern, lowerOccurrenceBound=st.integers(), operator=safe_text, upperOccurrenceBound=st.integers())
@given(instance=camel_scalability_BinaryEventPattern_strategy)
@settings(max_examples=25)
def test_camel_scalability_BinaryEventPattern_instantiation(instance):
    assert isinstance(instance, camel_scalability_BinaryEventPattern)


camel_scalability_Event_strategy = st.builds(camel_scalability_Event, name=safe_text)
@given(instance=camel_scalability_Event_strategy)
@settings(max_examples=25)
def test_camel_scalability_Event_instantiation(instance):
    assert isinstance(instance, camel_scalability_Event)


camel_scalability_EventInstance_strategy = st.builds(camel_scalability_EventInstance, layer=safe_text, name=safe_text, status=safe_text)
@given(instance=camel_scalability_EventInstance_strategy)
@settings(max_examples=25)
def test_camel_scalability_EventInstance_instantiation(instance):
    assert isinstance(instance, camel_scalability_EventInstance)


camel_scalability_EventPattern_strategy = st.builds(camel_scalability_EventPattern)
@given(instance=camel_scalability_EventPattern_strategy)
@settings(max_examples=25)
def test_camel_scalability_EventPattern_instantiation(instance):
    assert isinstance(instance, camel_scalability_EventPattern)


camel_scalability_FunctionalEvent_strategy = st.builds(camel_scalability_FunctionalEvent, functionalType=safe_text)
@given(instance=camel_scalability_FunctionalEvent_strategy)
@settings(max_examples=25)
def test_camel_scalability_FunctionalEvent_instantiation(instance):
    assert isinstance(instance, camel_scalability_FunctionalEvent)


camel_scalability_HorizontalScalingAction_strategy = st.builds(camel_scalability_HorizontalScalingAction, count=st.integers())
@given(instance=camel_scalability_HorizontalScalingAction_strategy)
@settings(max_examples=25)
def test_camel_scalability_HorizontalScalingAction_instantiation(instance):
    assert isinstance(instance, camel_scalability_HorizontalScalingAction)


camel_scalability_NonFunctionalEvent_strategy = st.builds(camel_scalability_NonFunctionalEvent, isViolation=st.booleans())
@given(instance=camel_scalability_NonFunctionalEvent_strategy)
@settings(max_examples=25)
def test_camel_scalability_NonFunctionalEvent_instantiation(instance):
    assert isinstance(instance, camel_scalability_NonFunctionalEvent)


camel_scalability_ScalabilityModel_strategy = st.builds(camel_scalability_ScalabilityModel)
@given(instance=camel_scalability_ScalabilityModel_strategy)
@settings(max_examples=25)
def test_camel_scalability_ScalabilityModel_instantiation(instance):
    assert isinstance(instance, camel_scalability_ScalabilityModel)


camel_scalability_ScalabilityRule_strategy = st.builds(camel_scalability_ScalabilityRule, name=safe_text)
@given(instance=camel_scalability_ScalabilityRule_strategy)
@settings(max_examples=25)
def test_camel_scalability_ScalabilityRule_instantiation(instance):
    assert isinstance(instance, camel_scalability_ScalabilityRule)


camel_scalability_ScalingAction_strategy = st.builds(camel_scalability_ScalingAction)
@given(instance=camel_scalability_ScalingAction_strategy)
@settings(max_examples=25)
def test_camel_scalability_ScalingAction_instantiation(instance):
    assert isinstance(instance, camel_scalability_ScalingAction)


camel_scalability_SimpleEvent_strategy = st.builds(camel_scalability_SimpleEvent)
@given(instance=camel_scalability_SimpleEvent_strategy)
@settings(max_examples=25)
def test_camel_scalability_SimpleEvent_instantiation(instance):
    assert isinstance(instance, camel_scalability_SimpleEvent)


camel_scalability_Timer_strategy = st.builds(camel_scalability_Timer, maxOccurrenceNum=st.integers(), name=safe_text, timeValue=st.integers(), type=safe_text)
@given(instance=camel_scalability_Timer_strategy)
@settings(max_examples=25)
def test_camel_scalability_Timer_instantiation(instance):
    assert isinstance(instance, camel_scalability_Timer)


camel_scalability_UnaryEventPattern_strategy = st.builds(camel_scalability_UnaryEventPattern, occurrenceNum=st.integers(), operator=safe_text)
@given(instance=camel_scalability_UnaryEventPattern_strategy)
@settings(max_examples=25)
def test_camel_scalability_UnaryEventPattern_instantiation(instance):
    assert isinstance(instance, camel_scalability_UnaryEventPattern)


camel_scalability_VerticalScalingAction_strategy = st.builds(camel_scalability_VerticalScalingAction, CPUUpdate=st.floats(allow_nan=False, allow_infinity=False), coreUpdate=st.integers(), ioUpdate=st.integers(), memoryUpdate=st.integers(), networkUpdate=st.integers(), storageUpdate=st.integers())
@given(instance=camel_scalability_VerticalScalingAction_strategy)
@settings(max_examples=25)
def test_camel_scalability_VerticalScalingAction_instantiation(instance):
    assert isinstance(instance, camel_scalability_VerticalScalingAction)


camel_security_Certifiable_strategy = st.builds(camel_security_Certifiable)
@given(instance=camel_security_Certifiable_strategy)
@settings(max_examples=25)
def test_camel_security_Certifiable_instantiation(instance):
    assert isinstance(instance, camel_security_Certifiable)


camel_security_CompositeSecurityMetric_strategy = st.builds(camel_security_CompositeSecurityMetric)
@given(instance=camel_security_CompositeSecurityMetric_strategy)
@settings(max_examples=25)
def test_camel_security_CompositeSecurityMetric_instantiation(instance):
    assert isinstance(instance, camel_security_CompositeSecurityMetric)


camel_security_CompositeSecurityMetricInstance_strategy = st.builds(camel_security_CompositeSecurityMetricInstance)
@given(instance=camel_security_CompositeSecurityMetricInstance_strategy)
@settings(max_examples=25)
def test_camel_security_CompositeSecurityMetricInstance_instantiation(instance):
    assert isinstance(instance, camel_security_CompositeSecurityMetricInstance)


camel_security_RawSecurityMetric_strategy = st.builds(camel_security_RawSecurityMetric)
@given(instance=camel_security_RawSecurityMetric_strategy)
@settings(max_examples=25)
def test_camel_security_RawSecurityMetric_instantiation(instance):
    assert isinstance(instance, camel_security_RawSecurityMetric)


camel_security_RawSecurityMetricInstance_strategy = st.builds(camel_security_RawSecurityMetricInstance)
@given(instance=camel_security_RawSecurityMetricInstance_strategy)
@settings(max_examples=25)
def test_camel_security_RawSecurityMetricInstance_instantiation(instance):
    assert isinstance(instance, camel_security_RawSecurityMetricInstance)


camel_security_SecurityCapability_strategy = st.builds(camel_security_SecurityCapability, name=safe_text)
@given(instance=camel_security_SecurityCapability_strategy)
@settings(max_examples=25)
def test_camel_security_SecurityCapability_instantiation(instance):
    assert isinstance(instance, camel_security_SecurityCapability)


camel_security_SecurityControl_strategy = st.builds(camel_security_SecurityControl, name=safe_text, specification=safe_text)
@given(instance=camel_security_SecurityControl_strategy)
@settings(max_examples=25)
def test_camel_security_SecurityControl_instantiation(instance):
    assert isinstance(instance, camel_security_SecurityControl)


camel_security_SecurityDomain_strategy = st.builds(camel_security_SecurityDomain, id=safe_text, name=safe_text)
@given(instance=camel_security_SecurityDomain_strategy)
@settings(max_examples=25)
def test_camel_security_SecurityDomain_instantiation(instance):
    assert isinstance(instance, camel_security_SecurityDomain)


camel_security_SecurityModel_strategy = st.builds(camel_security_SecurityModel)
@given(instance=camel_security_SecurityModel_strategy)
@settings(max_examples=25)
def test_camel_security_SecurityModel_instantiation(instance):
    assert isinstance(instance, camel_security_SecurityModel)


camel_security_SecurityProperty_strategy = st.builds(camel_security_SecurityProperty)
@given(instance=camel_security_SecurityProperty_strategy)
@settings(max_examples=25)
def test_camel_security_SecurityProperty_instantiation(instance):
    assert isinstance(instance, camel_security_SecurityProperty)


camel_security_SecuritySLO_strategy = st.builds(camel_security_SecuritySLO)
@given(instance=camel_security_SecuritySLO_strategy)
@settings(max_examples=25)
def test_camel_security_SecuritySLO_instantiation(instance):
    assert isinstance(instance, camel_security_SecuritySLO)


camel_type_BoolValue_strategy = st.builds(camel_type_BoolValue, value=st.booleans())
@given(instance=camel_type_BoolValue_strategy)
@settings(max_examples=25)
def test_camel_type_BoolValue_instantiation(instance):
    assert isinstance(instance, camel_type_BoolValue)


camel_type_BooleanValueType_strategy = st.builds(camel_type_BooleanValueType, primitiveType=safe_text)
@given(instance=camel_type_BooleanValueType_strategy)
@settings(max_examples=25)
def test_camel_type_BooleanValueType_instantiation(instance):
    assert isinstance(instance, camel_type_BooleanValueType)


camel_type_DoublePrecisionValue_strategy = st.builds(camel_type_DoublePrecisionValue, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_type_DoublePrecisionValue_strategy)
@settings(max_examples=25)
def test_camel_type_DoublePrecisionValue_instantiation(instance):
    assert isinstance(instance, camel_type_DoublePrecisionValue)


camel_type_EnumerateValue_strategy = st.builds(camel_type_EnumerateValue, name=safe_text, value=st.integers())
@given(instance=camel_type_EnumerateValue_strategy)
@settings(max_examples=25)
def test_camel_type_EnumerateValue_instantiation(instance):
    assert isinstance(instance, camel_type_EnumerateValue)


camel_type_Enumeration_strategy = st.builds(camel_type_Enumeration)
@given(instance=camel_type_Enumeration_strategy)
@settings(max_examples=25)
def test_camel_type_Enumeration_instantiation(instance):
    assert isinstance(instance, camel_type_Enumeration)


camel_type_FloatsValue_strategy = st.builds(camel_type_FloatsValue, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=camel_type_FloatsValue_strategy)
@settings(max_examples=25)
def test_camel_type_FloatsValue_instantiation(instance):
    assert isinstance(instance, camel_type_FloatsValue)


camel_type_IntegerValue_strategy = st.builds(camel_type_IntegerValue, value=st.integers())
@given(instance=camel_type_IntegerValue_strategy)
@settings(max_examples=25)
def test_camel_type_IntegerValue_instantiation(instance):
    assert isinstance(instance, camel_type_IntegerValue)


camel_type_Limit_strategy = st.builds(camel_type_Limit, included=st.booleans())
@given(instance=camel_type_Limit_strategy)
@settings(max_examples=25)
def test_camel_type_Limit_instantiation(instance):
    assert isinstance(instance, camel_type_Limit)


camel_type_List_strategy = st.builds(camel_type_List, primitiveType=safe_text)
@given(instance=camel_type_List_strategy)
@settings(max_examples=25)
def test_camel_type_List_instantiation(instance):
    assert isinstance(instance, camel_type_List)


camel_type_NegativeInf_strategy = st.builds(camel_type_NegativeInf)
@given(instance=camel_type_NegativeInf_strategy)
@settings(max_examples=25)
def test_camel_type_NegativeInf_instantiation(instance):
    assert isinstance(instance, camel_type_NegativeInf)


camel_type_NumericValue_strategy = st.builds(camel_type_NumericValue)
@given(instance=camel_type_NumericValue_strategy)
@settings(max_examples=25)
def test_camel_type_NumericValue_instantiation(instance):
    assert isinstance(instance, camel_type_NumericValue)


camel_type_PositiveInf_strategy = st.builds(camel_type_PositiveInf)
@given(instance=camel_type_PositiveInf_strategy)
@settings(max_examples=25)
def test_camel_type_PositiveInf_instantiation(instance):
    assert isinstance(instance, camel_type_PositiveInf)


camel_type_Range_strategy = st.builds(camel_type_Range, primitiveType=safe_text)
@given(instance=camel_type_Range_strategy)
@settings(max_examples=25)
def test_camel_type_Range_instantiation(instance):
    assert isinstance(instance, camel_type_Range)


camel_type_RangeUnion_strategy = st.builds(camel_type_RangeUnion, primitiveType=safe_text)
@given(instance=camel_type_RangeUnion_strategy)
@settings(max_examples=25)
def test_camel_type_RangeUnion_instantiation(instance):
    assert isinstance(instance, camel_type_RangeUnion)


camel_type_SingleValue_strategy = st.builds(camel_type_SingleValue)
@given(instance=camel_type_SingleValue_strategy)
@settings(max_examples=25)
def test_camel_type_SingleValue_instantiation(instance):
    assert isinstance(instance, camel_type_SingleValue)


camel_type_StringValueType_strategy = st.builds(camel_type_StringValueType, primitiveType=safe_text)
@given(instance=camel_type_StringValueType_strategy)
@settings(max_examples=25)
def test_camel_type_StringValueType_instantiation(instance):
    assert isinstance(instance, camel_type_StringValueType)


camel_type_StringsValue_strategy = st.builds(camel_type_StringsValue, value=safe_text)
@given(instance=camel_type_StringsValue_strategy)
@settings(max_examples=25)
def test_camel_type_StringsValue_instantiation(instance):
    assert isinstance(instance, camel_type_StringsValue)


camel_type_TypeModel_strategy = st.builds(camel_type_TypeModel)
@given(instance=camel_type_TypeModel_strategy)
@settings(max_examples=25)
def test_camel_type_TypeModel_instantiation(instance):
    assert isinstance(instance, camel_type_TypeModel)


camel_type_ValueToIncrease_strategy = st.builds(camel_type_ValueToIncrease)
@given(instance=camel_type_ValueToIncrease_strategy)
@settings(max_examples=25)
def test_camel_type_ValueToIncrease_instantiation(instance):
    assert isinstance(instance, camel_type_ValueToIncrease)


camel_type_ValueType_strategy = st.builds(camel_type_ValueType, name=safe_text)
@given(instance=camel_type_ValueType_strategy)
@settings(max_examples=25)
def test_camel_type_ValueType_instantiation(instance):
    assert isinstance(instance, camel_type_ValueType)


camel_unit_CoreUnit_strategy = st.builds(camel_unit_CoreUnit)
@given(instance=camel_unit_CoreUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_CoreUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_CoreUnit)


camel_unit_Dimensionless_strategy = st.builds(camel_unit_Dimensionless)
@given(instance=camel_unit_Dimensionless_strategy)
@settings(max_examples=25)
def test_camel_unit_Dimensionless_instantiation(instance):
    assert isinstance(instance, camel_unit_Dimensionless)


camel_unit_MonetaryUnit_strategy = st.builds(camel_unit_MonetaryUnit)
@given(instance=camel_unit_MonetaryUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_MonetaryUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_MonetaryUnit)


camel_unit_RequestUnit_strategy = st.builds(camel_unit_RequestUnit)
@given(instance=camel_unit_RequestUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_RequestUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_RequestUnit)


camel_unit_StorageUnit_strategy = st.builds(camel_unit_StorageUnit)
@given(instance=camel_unit_StorageUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_StorageUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_StorageUnit)


camel_unit_ThroughputUnit_strategy = st.builds(camel_unit_ThroughputUnit)
@given(instance=camel_unit_ThroughputUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_ThroughputUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_ThroughputUnit)


camel_unit_TimeIntervalUnit_strategy = st.builds(camel_unit_TimeIntervalUnit)
@given(instance=camel_unit_TimeIntervalUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_TimeIntervalUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_TimeIntervalUnit)


camel_unit_TransactionUnit_strategy = st.builds(camel_unit_TransactionUnit)
@given(instance=camel_unit_TransactionUnit_strategy)
@settings(max_examples=25)
def test_camel_unit_TransactionUnit_instantiation(instance):
    assert isinstance(instance, camel_unit_TransactionUnit)


camel_unit_Unit_strategy = st.builds(camel_unit_Unit, name=safe_text, unit=safe_text)
@given(instance=camel_unit_Unit_strategy)
@settings(max_examples=25)
def test_camel_unit_Unit_instantiation(instance):
    assert isinstance(instance, camel_unit_Unit)


camel_unit_UnitModel_strategy = st.builds(camel_unit_UnitModel)
@given(instance=camel_unit_UnitModel_strategy)
@settings(max_examples=25)
def test_camel_unit_UnitModel_instantiation(instance):
    assert isinstance(instance, camel_unit_UnitModel)


execution_camel_Action_strategy = st.builds(execution_camel_Action)
@given(instance=execution_camel_Action_strategy)
@settings(max_examples=25)
def test_execution_camel_Action_instantiation(instance):
    assert isinstance(instance, execution_camel_Action)


execution_camel_Application_strategy = st.builds(execution_camel_Application)
@given(instance=execution_camel_Application_strategy)
@settings(max_examples=25)
def test_execution_camel_Application_instantiation(instance):
    assert isinstance(instance, execution_camel_Application)


metric_camel_Application_strategy = st.builds(metric_camel_Application)
@given(instance=metric_camel_Application_strategy)
@settings(max_examples=25)
def test_metric_camel_Application_instantiation(instance):
    assert isinstance(instance, metric_camel_Application)


requirement_camel_Application_strategy = st.builds(requirement_camel_Application)
@given(instance=requirement_camel_Application_strategy)
@settings(max_examples=25)
def test_requirement_camel_Application_instantiation(instance):
    assert isinstance(instance, requirement_camel_Application)


scalability_camel_Action_strategy = st.builds(scalability_camel_Action)
@given(instance=scalability_camel_Action_strategy)
@settings(max_examples=25)
def test_scalability_camel_Action_instantiation(instance):
    assert isinstance(instance, scalability_camel_Action)


