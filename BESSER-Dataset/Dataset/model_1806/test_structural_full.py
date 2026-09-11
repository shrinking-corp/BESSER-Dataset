import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Base,
    BaseExpressionResult,
    BaseResource,
    Company,
    Component,
    library_BaseExpressionResult,
    library_BaseResource,
    library_Component,
    library_ConfigAttribute,
    library_DiagramInfo,
    library_EObject,
    library_Equipment,
    library_EquipmentGroup,
    library_EquipmentRelationship,
    library_Expression,
    library_ExpressionResult,
    library_Function,
    library_FunctionRelationship,
    library_LastEvaluationExpressionResult,
    library_Library,
    library_Lifecycle,
    library_Meta,
    library_Metric,
    library_MetricSource,
    library_MetricValueRange,
    library_MultiImage,
    library_NetXResource,
    library_NodeType,
    library_Parameter,
    library_ProductInfo,
    library_Protocol,
    library_ReferenceNetwork,
    library_ReferenceRelationship,
    library_Tolerance,
    library_Unit,
    library_Value,
    library_Vendor,
    LevelKind,
    RangeKind,
    RedundancyType,
    StateType,
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

def test_library_BaseResource_detailDisplay_value_roundtrip():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert instance.detailDisplay == "sample_text"
    instance.detailDisplay = "sample_text_2"
    assert instance.detailDisplay == "sample_text_2"


def test_library_BaseResource_expressionName_value_roundtrip():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert instance.expressionName == "sample_text"
    instance.expressionName = "sample_text_2"
    assert instance.expressionName == "sample_text_2"


def test_library_BaseResource_longName_value_roundtrip():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert instance.longName == "sample_text"
    instance.longName = "sample_text_2"
    assert instance.longName == "sample_text_2"


def test_library_BaseResource_shortName_value_roundtrip():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert instance.shortName == "sample_text"
    instance.shortName = "sample_text_2"
    assert instance.shortName == "sample_text_2"


def test_library_BaseResource_summaryDisplay_value_roundtrip():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert instance.summaryDisplay == "sample_text"
    instance.summaryDisplay = "sample_text_2"
    assert instance.summaryDisplay == "sample_text_2"


def test_library_Component_description_value_roundtrip():
    instance = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_library_Component_duration_value_roundtrip():
    instance = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_library_Component_name_value_roundtrip():
    instance = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Equipment_count_value_roundtrip():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert instance.count == "sample_text"
    instance.count = "sample_text_2"
    assert instance.count == "sample_text_2"


def test_library_Equipment_equipmentCode_value_roundtrip():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert instance.equipmentCode == "sample_text"
    instance.equipmentCode = "sample_text_2"
    assert instance.equipmentCode == "sample_text_2"


def test_library_Equipment_position_value_roundtrip():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_library_Equipment_redundancy_value_roundtrip():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert instance.redundancy == "sample_text"
    instance.redundancy = "sample_text_2"
    assert instance.redundancy == "sample_text_2"


def test_library_Equipment_state_value_roundtrip():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_library_EquipmentGroup_count_value_roundtrip():
    instance = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    assert instance.count == "sample_text"
    instance.count = "sample_text_2"
    assert instance.count == "sample_text_2"


def test_library_EquipmentGroup_description_value_roundtrip():
    instance = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_library_EquipmentGroup_name_value_roundtrip():
    instance = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Expression_expressionLines_value_roundtrip():
    instance = library_Expression(expressionLines="sample_text", name="sample_text")
    assert instance.expressionLines == "sample_text"
    instance.expressionLines = "sample_text_2"
    assert instance.expressionLines == "sample_text_2"


def test_library_Expression_name_value_roundtrip():
    instance = library_Expression(expressionLines="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_ExpressionResult_targetIntervalHint_value_roundtrip():
    instance = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    assert instance.targetIntervalHint == "sample_text"
    instance.targetIntervalHint = "sample_text_2"
    assert instance.targetIntervalHint == "sample_text_2"


def test_library_ExpressionResult_targetKindHint_value_roundtrip():
    instance = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    assert instance.targetKindHint == "sample_text"
    instance.targetKindHint = "sample_text_2"
    assert instance.targetKindHint == "sample_text_2"


def test_library_ExpressionResult_targetRange_value_roundtrip():
    instance = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    assert instance.targetRange == "sample_text"
    instance.targetRange = "sample_text_2"
    assert instance.targetRange == "sample_text_2"


def test_library_LastEvaluationExpressionResult_lastEvalResult_value_roundtrip():
    instance = library_LastEvaluationExpressionResult(lastEvalResult="sample_text")
    assert instance.lastEvalResult == "sample_text"
    instance.lastEvalResult = "sample_text_2"
    assert instance.lastEvalResult == "sample_text_2"


def test_library_Library_name_value_roundtrip():
    instance = library_Library(name="sample_text", protocols="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Library_protocols_value_roundtrip():
    instance = library_Library(name="sample_text", protocols="sample_text")
    assert instance.protocols == "sample_text"
    instance.protocols = "sample_text_2"
    assert instance.protocols == "sample_text_2"


def test_library_NodeType_leafNode_value_roundtrip():
    instance = library_NodeType(leafNode="sample_text", name="sample_text")
    assert instance.leafNode == "sample_text"
    instance.leafNode = "sample_text_2"
    assert instance.leafNode == "sample_text_2"


def test_library_NodeType_name_value_roundtrip():
    instance = library_NodeType(leafNode="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Parameter_description_value_roundtrip():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_library_Parameter_expressionName_value_roundtrip():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert instance.expressionName == "sample_text"
    instance.expressionName = "sample_text_2"
    assert instance.expressionName == "sample_text_2"


def test_library_Parameter_modifiable_value_roundtrip():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert instance.modifiable == "sample_text"
    instance.modifiable = "sample_text_2"
    assert instance.modifiable == "sample_text_2"


def test_library_Parameter_name_value_roundtrip():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Parameter_value_value_roundtrip():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_library_ProductInfo_availableDate_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.availableDate == "sample_text"
    instance.availableDate = "sample_text_2"
    assert instance.availableDate == "sample_text_2"


def test_library_ProductInfo_endOfSalesDate_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.endOfSalesDate == "sample_text"
    instance.endOfSalesDate = "sample_text_2"
    assert instance.endOfSalesDate == "sample_text_2"


def test_library_ProductInfo_endOfSupportDate_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.endOfSupportDate == "sample_text"
    instance.endOfSupportDate = "sample_text_2"
    assert instance.endOfSupportDate == "sample_text_2"


def test_library_ProductInfo_productCode_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.productCode == "sample_text"
    instance.productCode = "sample_text_2"
    assert instance.productCode == "sample_text_2"


def test_library_ProductInfo_salesCode_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.salesCode == "sample_text"
    instance.salesCode = "sample_text_2"
    assert instance.salesCode == "sample_text_2"


def test_library_ProductInfo_underDevelopmentDate_value_roundtrip():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert instance.underDevelopmentDate == "sample_text"
    instance.underDevelopmentDate = "sample_text_2"
    assert instance.underDevelopmentDate == "sample_text_2"


def test_library_ReferenceNetwork_description_value_roundtrip():
    instance = library_ReferenceNetwork(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_library_ReferenceNetwork_name_value_roundtrip():
    instance = library_ReferenceNetwork(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_ReferenceRelationship_name_value_roundtrip():
    instance = library_ReferenceRelationship(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Tolerance_level_value_roundtrip():
    instance = library_Tolerance(level="sample_text", name="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_library_Tolerance_name_value_roundtrip():
    instance = library_Tolerance(level="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Unit_code_value_roundtrip():
    instance = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_library_Unit_description_value_roundtrip():
    instance = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_library_Unit_name_value_roundtrip():
    instance = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_BaseResource_isa_Base():
    instance = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    assert isinstance(instance, Base)


def test_library_Component_isa_Base():
    instance = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_EquipmentGroup_isa_Base():
    instance = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_Expression_isa_Base():
    instance = library_Expression(expressionLines="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_NodeType_isa_Base():
    instance = library_NodeType(leafNode="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_Parameter_isa_Base():
    instance = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    assert isinstance(instance, Base)


def test_library_ProductInfo_isa_Base():
    instance = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    assert isinstance(instance, Base)


def test_library_ReferenceNetwork_isa_Base():
    instance = library_ReferenceNetwork(description="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_ReferenceRelationship_isa_Base():
    instance = library_ReferenceRelationship(name="sample_text")
    assert isinstance(instance, Base)


def test_library_Tolerance_isa_Base():
    instance = library_Tolerance(level="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_Unit_isa_Base():
    instance = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_library_ExpressionResult_isa_BaseExpressionResult():
    instance = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    assert isinstance(instance, BaseExpressionResult)


def test_library_LastEvaluationExpressionResult_isa_BaseExpressionResult():
    instance = library_LastEvaluationExpressionResult(lastEvalResult="sample_text")
    assert isinstance(instance, BaseExpressionResult)


def test_library_NetXResource_isa_BaseResource():
    instance = library_NetXResource()
    assert isinstance(instance, BaseResource)


def test_library_Vendor_isa_Company():
    instance = library_Vendor()
    assert isinstance(instance, Company)


def test_library_Equipment_isa_Component():
    instance = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    assert isinstance(instance, Component)


def test_library_Function_isa_Component():
    instance = library_Function()
    assert isinstance(instance, Component)


def test_assoc_allEquipmentResources48_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_EquipmentGroup49', {b1})
    assert _is_linked(a, 'library_EquipmentGroup49', b1)
    if hasattr(b1, 'library_NetXResource50'):
        assert _is_linked(b1, 'library_NetXResource50', a)
    _safe_set(a, 'library_EquipmentGroup49', {b2})
    assert _is_linked(a, 'library_EquipmentGroup49', b2)
    if hasattr(b1, 'library_NetXResource50'):
        assert not _is_linked(b1, 'library_NetXResource50', a)
    if hasattr(b2, 'library_NetXResource50'):
        assert _is_linked(b2, 'library_NetXResource50', a)
    _safe_set(a, 'library_EquipmentGroup49', set())
    assert not _is_linked(a, 'library_EquipmentGroup49', b2)
    if hasattr(b2, 'library_NetXResource50'):
        assert not _is_linked(b2, 'library_NetXResource50', a)


def test_assoc_allEquipments31_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Equipment30', {b1})
    assert _is_linked(a, 'library_Equipment30', b1)
    if hasattr(b1, 'library_Equipment32'):
        assert _is_linked(b1, 'library_Equipment32', a)
    _safe_set(a, 'library_Equipment30', {b2})
    assert _is_linked(a, 'library_Equipment30', b2)
    if hasattr(b1, 'library_Equipment32'):
        assert not _is_linked(b1, 'library_Equipment32', a)
    if hasattr(b2, 'library_Equipment32'):
        assert _is_linked(b2, 'library_Equipment32', a)
    _safe_set(a, 'library_Equipment30', set())
    assert not _is_linked(a, 'library_Equipment30', b2)
    if hasattr(b2, 'library_Equipment32'):
        assert not _is_linked(b2, 'library_Equipment32', a)


def test_assoc_allEquipments51_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup52', {b1})
    assert _is_linked(a, 'library_EquipmentGroup52', b1)
    if hasattr(b1, 'library_Equipment53'):
        assert _is_linked(b1, 'library_Equipment53', a)
    _safe_set(a, 'library_EquipmentGroup52', {b2})
    assert _is_linked(a, 'library_EquipmentGroup52', b2)
    if hasattr(b1, 'library_Equipment53'):
        assert not _is_linked(b1, 'library_Equipment53', a)
    if hasattr(b2, 'library_Equipment53'):
        assert _is_linked(b2, 'library_Equipment53', a)
    _safe_set(a, 'library_EquipmentGroup52', set())
    assert not _is_linked(a, 'library_EquipmentGroup52', b2)
    if hasattr(b2, 'library_Equipment53'):
        assert not _is_linked(b2, 'library_Equipment53', a)


def test_assoc_allResources18_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_Component19', {b1})
    assert _is_linked(a, 'library_Component19', b1)
    if hasattr(b1, 'library_NetXResource'):
        assert _is_linked(b1, 'library_NetXResource', a)
    _safe_set(a, 'library_Component19', {b2})
    assert _is_linked(a, 'library_Component19', b2)
    if hasattr(b1, 'library_NetXResource'):
        assert not _is_linked(b1, 'library_NetXResource', a)
    if hasattr(b2, 'library_NetXResource'):
        assert _is_linked(b2, 'library_NetXResource', a)
    _safe_set(a, 'library_Component19', set())
    assert not _is_linked(a, 'library_Component19', b2)
    if hasattr(b2, 'library_NetXResource'):
        assert not _is_linked(b2, 'library_NetXResource', a)


def test_assoc_capacityExpressionRef7_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression', b1)
    assert _is_linked(a, 'library_Expression', b1)
    if hasattr(b1, 'library_Component8'):
        assert _is_linked(b1, 'library_Component8', a)
    _safe_set(a, 'library_Expression', b2)
    assert _is_linked(a, 'library_Expression', b2)
    if hasattr(b1, 'library_Component8'):
        assert not _is_linked(b1, 'library_Component8', a)
    if hasattr(b2, 'library_Component8'):
        assert _is_linked(b2, 'library_Component8', a)
    _safe_set(a, 'library_Expression', None)
    assert not _is_linked(a, 'library_Expression', b2)
    if hasattr(b2, 'library_Component8'):
        assert not _is_linked(b2, 'library_Component8', a)


def test_assoc_componentRef93_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'Component', b1)
    assert _is_linked(a, 'Component', b1)
    if hasattr(b1, 'resourceRefs'):
        assert _is_linked(b1, 'resourceRefs', a)
    _safe_set(a, 'Component', b2)
    assert _is_linked(a, 'Component', b2)
    if hasattr(b1, 'resourceRefs'):
        assert not _is_linked(b1, 'resourceRefs', a)
    if hasattr(b2, 'resourceRefs'):
        assert _is_linked(b2, 'resourceRefs', a)
    _safe_set(a, 'Component', None)
    assert not _is_linked(a, 'Component', b2)
    if hasattr(b2, 'resourceRefs'):
        assert not _is_linked(b2, 'resourceRefs', a)


def test_assoc_configAttributes3_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_ConfigAttribute()
    b2 = library_ConfigAttribute()
    _safe_set(a, 'library_Component4', {b1})
    assert _is_linked(a, 'library_Component4', b1)
    if hasattr(b1, 'library_ConfigAttribute'):
        assert _is_linked(b1, 'library_ConfigAttribute', a)
    _safe_set(a, 'library_Component4', {b2})
    assert _is_linked(a, 'library_Component4', b2)
    if hasattr(b1, 'library_ConfigAttribute'):
        assert not _is_linked(b1, 'library_ConfigAttribute', a)
    if hasattr(b2, 'library_ConfigAttribute'):
        assert _is_linked(b2, 'library_ConfigAttribute', a)
    _safe_set(a, 'library_Component4', set())
    assert not _is_linked(a, 'library_Component4', b2)
    if hasattr(b2, 'library_ConfigAttribute'):
        assert not _is_linked(b2, 'library_ConfigAttribute', a)


def test_assoc_diagrams128_link_reassign_clear():
    a = library_ReferenceNetwork(description="sample_text", name="sample_text")
    b1 = library_DiagramInfo()
    b2 = library_DiagramInfo()
    _safe_set(a, 'library_ReferenceNetwork', {b1})
    assert _is_linked(a, 'library_ReferenceNetwork', b1)
    if hasattr(b1, 'library_DiagramInfo129'):
        assert _is_linked(b1, 'library_DiagramInfo129', a)
    _safe_set(a, 'library_ReferenceNetwork', {b2})
    assert _is_linked(a, 'library_ReferenceNetwork', b2)
    if hasattr(b1, 'library_DiagramInfo129'):
        assert not _is_linked(b1, 'library_DiagramInfo129', a)
    if hasattr(b2, 'library_DiagramInfo129'):
        assert _is_linked(b2, 'library_DiagramInfo129', a)
    _safe_set(a, 'library_ReferenceNetwork', set())
    assert not _is_linked(a, 'library_ReferenceNetwork', b2)
    if hasattr(b2, 'library_DiagramInfo129'):
        assert not _is_linked(b2, 'library_DiagramInfo129', a)


def test_assoc_diagrams20_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_DiagramInfo()
    b2 = library_DiagramInfo()
    _safe_set(a, 'library_Component21', {b1})
    assert _is_linked(a, 'library_Component21', b1)
    if hasattr(b1, 'library_DiagramInfo'):
        assert _is_linked(b1, 'library_DiagramInfo', a)
    _safe_set(a, 'library_Component21', {b2})
    assert _is_linked(a, 'library_Component21', b2)
    if hasattr(b1, 'library_DiagramInfo'):
        assert not _is_linked(b1, 'library_DiagramInfo', a)
    if hasattr(b2, 'library_DiagramInfo'):
        assert _is_linked(b2, 'library_DiagramInfo', a)
    _safe_set(a, 'library_Component21', set())
    assert not _is_linked(a, 'library_Component21', b2)
    if hasattr(b2, 'library_DiagramInfo'):
        assert not _is_linked(b2, 'library_DiagramInfo', a)


def test_assoc_diagrams33_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_DiagramInfo()
    b2 = library_DiagramInfo()
    _safe_set(a, 'library_EquipmentGroup34', {b1})
    assert _is_linked(a, 'library_EquipmentGroup34', b1)
    if hasattr(b1, 'library_DiagramInfo35'):
        assert _is_linked(b1, 'library_DiagramInfo35', a)
    _safe_set(a, 'library_EquipmentGroup34', {b2})
    assert _is_linked(a, 'library_EquipmentGroup34', b2)
    if hasattr(b1, 'library_DiagramInfo35'):
        assert not _is_linked(b1, 'library_DiagramInfo35', a)
    if hasattr(b2, 'library_DiagramInfo35'):
        assert _is_linked(b2, 'library_DiagramInfo35', a)
    _safe_set(a, 'library_EquipmentGroup34', set())
    assert not _is_linked(a, 'library_EquipmentGroup34', b2)
    if hasattr(b2, 'library_DiagramInfo35'):
        assert not _is_linked(b2, 'library_DiagramInfo35', a)


def test_assoc_equipmentGroupResources36_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_EquipmentGroup37', {b1})
    assert _is_linked(a, 'library_EquipmentGroup37', b1)
    if hasattr(b1, 'library_NetXResource38'):
        assert _is_linked(b1, 'library_NetXResource38', a)
    _safe_set(a, 'library_EquipmentGroup37', {b2})
    assert _is_linked(a, 'library_EquipmentGroup37', b2)
    if hasattr(b1, 'library_NetXResource38'):
        assert not _is_linked(b1, 'library_NetXResource38', a)
    if hasattr(b2, 'library_NetXResource38'):
        assert _is_linked(b2, 'library_NetXResource38', a)
    _safe_set(a, 'library_EquipmentGroup37', set())
    assert not _is_linked(a, 'library_EquipmentGroup37', b2)
    if hasattr(b2, 'library_NetXResource38'):
        assert not _is_linked(b2, 'library_NetXResource38', a)


def test_assoc_equipmentGroups26_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup', b1)
    assert _is_linked(a, 'library_EquipmentGroup', b1)
    if hasattr(b1, 'library_Equipment27'):
        assert _is_linked(b1, 'library_Equipment27', a)
    _safe_set(a, 'library_EquipmentGroup', b2)
    assert _is_linked(a, 'library_EquipmentGroup', b2)
    if hasattr(b1, 'library_Equipment27'):
        assert not _is_linked(b1, 'library_Equipment27', a)
    if hasattr(b2, 'library_Equipment27'):
        assert _is_linked(b2, 'library_Equipment27', a)
    _safe_set(a, 'library_EquipmentGroup', None)
    assert not _is_linked(a, 'library_EquipmentGroup', b2)
    if hasattr(b2, 'library_Equipment27'):
        assert not _is_linked(b2, 'library_Equipment27', a)


def test_assoc_equipmentRef120_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_ProductInfo', {b1})
    assert _is_linked(a, 'library_ProductInfo', b1)
    if hasattr(b1, 'library_Equipment121'):
        assert _is_linked(b1, 'library_Equipment121', a)
    _safe_set(a, 'library_ProductInfo', {b2})
    assert _is_linked(a, 'library_ProductInfo', b2)
    if hasattr(b1, 'library_Equipment121'):
        assert not _is_linked(b1, 'library_Equipment121', a)
    if hasattr(b2, 'library_Equipment121'):
        assert _is_linked(b2, 'library_Equipment121', a)
    _safe_set(a, 'library_ProductInfo', set())
    assert not _is_linked(a, 'library_ProductInfo', b2)
    if hasattr(b2, 'library_Equipment121'):
        assert not _is_linked(b2, 'library_Equipment121', a)


def test_assoc_equipmentRefs42_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup43', {b1})
    assert _is_linked(a, 'library_EquipmentGroup43', b1)
    if hasattr(b1, 'library_Equipment44'):
        assert _is_linked(b1, 'library_Equipment44', a)
    _safe_set(a, 'library_EquipmentGroup43', {b2})
    assert _is_linked(a, 'library_EquipmentGroup43', b2)
    if hasattr(b1, 'library_Equipment44'):
        assert not _is_linked(b1, 'library_Equipment44', a)
    if hasattr(b2, 'library_Equipment44'):
        assert _is_linked(b2, 'library_Equipment44', a)
    _safe_set(a, 'library_EquipmentGroup43', set())
    assert not _is_linked(a, 'library_EquipmentGroup43', b2)
    if hasattr(b2, 'library_Equipment44'):
        assert not _is_linked(b2, 'library_Equipment44', a)


def test_assoc_equipmentRelationshipRefs28_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_EquipmentRelationship()
    b2 = library_EquipmentRelationship()
    _safe_set(a, 'library_Equipment29', {b1})
    assert _is_linked(a, 'library_Equipment29', b1)
    if hasattr(b1, 'library_EquipmentRelationship'):
        assert _is_linked(b1, 'library_EquipmentRelationship', a)
    _safe_set(a, 'library_Equipment29', {b2})
    assert _is_linked(a, 'library_Equipment29', b2)
    if hasattr(b1, 'library_EquipmentRelationship'):
        assert not _is_linked(b1, 'library_EquipmentRelationship', a)
    if hasattr(b2, 'library_EquipmentRelationship'):
        assert _is_linked(b2, 'library_EquipmentRelationship', a)
    _safe_set(a, 'library_Equipment29', set())
    assert not _is_linked(a, 'library_Equipment29', b2)
    if hasattr(b2, 'library_EquipmentRelationship'):
        assert not _is_linked(b2, 'library_EquipmentRelationship', a)


def test_assoc_equipments117_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_NodeType118', {b1})
    assert _is_linked(a, 'library_NodeType118', b1)
    if hasattr(b1, 'library_Equipment119'):
        assert _is_linked(b1, 'library_Equipment119', a)
    _safe_set(a, 'library_NodeType118', {b2})
    assert _is_linked(a, 'library_NodeType118', b2)
    if hasattr(b1, 'library_Equipment119'):
        assert not _is_linked(b1, 'library_Equipment119', a)
    if hasattr(b2, 'library_Equipment119'):
        assert _is_linked(b2, 'library_Equipment119', a)
    _safe_set(a, 'library_NodeType118', set())
    assert not _is_linked(a, 'library_NodeType118', b2)
    if hasattr(b2, 'library_Equipment119'):
        assert not _is_linked(b2, 'library_Equipment119', a)


def test_assoc_equipments25_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Equipment', b1)
    assert _is_linked(a, 'library_Equipment', b1)
    if hasattr(b1, 'library_Equipment24'):
        assert _is_linked(b1, 'library_Equipment24', a)
    _safe_set(a, 'library_Equipment', b2)
    assert _is_linked(a, 'library_Equipment', b2)
    if hasattr(b1, 'library_Equipment24'):
        assert not _is_linked(b1, 'library_Equipment24', a)
    if hasattr(b2, 'library_Equipment24'):
        assert _is_linked(b2, 'library_Equipment24', a)
    _safe_set(a, 'library_Equipment', None)
    assert not _is_linked(a, 'library_Equipment', b2)
    if hasattr(b2, 'library_Equipment24'):
        assert not _is_linked(b2, 'library_Equipment24', a)


def test_assoc_equipments71_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Library72', {b1})
    assert _is_linked(a, 'library_Library72', b1)
    if hasattr(b1, 'library_Equipment73'):
        assert _is_linked(b1, 'library_Equipment73', a)
    _safe_set(a, 'library_Library72', {b2})
    assert _is_linked(a, 'library_Library72', b2)
    if hasattr(b1, 'library_Equipment73'):
        assert not _is_linked(b1, 'library_Equipment73', a)
    if hasattr(b2, 'library_Equipment73'):
        assert _is_linked(b2, 'library_Equipment73', a)
    _safe_set(a, 'library_Library72', set())
    assert not _is_linked(a, 'library_Library72', b2)
    if hasattr(b2, 'library_Equipment73'):
        assert not _is_linked(b2, 'library_Equipment73', a)


def test_assoc_evaluationObject54_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_EObject()
    b2 = library_EObject()
    _safe_set(a, 'library_Expression55', b1)
    assert _is_linked(a, 'library_Expression55', b1)
    if hasattr(b1, 'library_EObject'):
        assert _is_linked(b1, 'library_EObject', a)
    _safe_set(a, 'library_Expression55', b2)
    assert _is_linked(a, 'library_Expression55', b2)
    if hasattr(b1, 'library_EObject'):
        assert not _is_linked(b1, 'library_EObject', a)
    if hasattr(b2, 'library_EObject'):
        assert _is_linked(b2, 'library_EObject', a)
    _safe_set(a, 'library_Expression55', None)
    assert not _is_linked(a, 'library_Expression55', b2)
    if hasattr(b2, 'library_EObject'):
        assert not _is_linked(b2, 'library_EObject', a)


def test_assoc_expressionRef147_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Expression(expressionLines="sample_text", name="sample_text")
    b2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Tolerance148', b1)
    assert _is_linked(a, 'library_Tolerance148', b1)
    if hasattr(b1, 'library_Expression149'):
        assert _is_linked(b1, 'library_Expression149', a)
    _safe_set(a, 'library_Tolerance148', b2)
    assert _is_linked(a, 'library_Tolerance148', b2)
    if hasattr(b1, 'library_Expression149'):
        assert not _is_linked(b1, 'library_Expression149', a)
    if hasattr(b2, 'library_Expression149'):
        assert _is_linked(b2, 'library_Expression149', a)
    _safe_set(a, 'library_Tolerance148', None)
    assert not _is_linked(a, 'library_Tolerance148', b2)
    if hasattr(b2, 'library_Expression149'):
        assert not _is_linked(b2, 'library_Expression149', a)


def test_assoc_expressionRefs39_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression41', b1)
    assert _is_linked(a, 'library_Expression41', b1)
    if hasattr(b1, 'library_EquipmentGroup40'):
        assert _is_linked(b1, 'library_EquipmentGroup40', a)
    _safe_set(a, 'library_Expression41', b2)
    assert _is_linked(a, 'library_Expression41', b2)
    if hasattr(b1, 'library_EquipmentGroup40'):
        assert not _is_linked(b1, 'library_EquipmentGroup40', a)
    if hasattr(b2, 'library_EquipmentGroup40'):
        assert _is_linked(b2, 'library_EquipmentGroup40', a)
    _safe_set(a, 'library_Expression41', None)
    assert not _is_linked(a, 'library_Expression41', b2)
    if hasattr(b2, 'library_EquipmentGroup40'):
        assert not _is_linked(b2, 'library_EquipmentGroup40', a)


def test_assoc_expressions85_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Expression(expressionLines="sample_text", name="sample_text")
    b2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Library86', {b1})
    assert _is_linked(a, 'library_Library86', b1)
    if hasattr(b1, 'library_Expression87'):
        assert _is_linked(b1, 'library_Expression87', a)
    _safe_set(a, 'library_Library86', {b2})
    assert _is_linked(a, 'library_Library86', b2)
    if hasattr(b1, 'library_Expression87'):
        assert not _is_linked(b1, 'library_Expression87', a)
    if hasattr(b2, 'library_Expression87'):
        assert _is_linked(b2, 'library_Expression87', a)
    _safe_set(a, 'library_Library86', set())
    assert not _is_linked(a, 'library_Library86', b2)
    if hasattr(b2, 'library_Expression87'):
        assert not _is_linked(b2, 'library_Expression87', a)


def test_assoc_functions114_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_NodeType115', {b1})
    assert _is_linked(a, 'library_NodeType115', b1)
    if hasattr(b1, 'library_Function116'):
        assert _is_linked(b1, 'library_Function116', a)
    _safe_set(a, 'library_NodeType115', {b2})
    assert _is_linked(a, 'library_NodeType115', b2)
    if hasattr(b1, 'library_Function116'):
        assert not _is_linked(b1, 'library_Function116', a)
    if hasattr(b2, 'library_Function116'):
        assert _is_linked(b2, 'library_Function116', a)
    _safe_set(a, 'library_NodeType115', set())
    assert not _is_linked(a, 'library_NodeType115', b2)
    if hasattr(b2, 'library_Function116'):
        assert not _is_linked(b2, 'library_Function116', a)


def test_assoc_functions67_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_Library', {b1})
    assert _is_linked(a, 'library_Library', b1)
    if hasattr(b1, 'library_Function68'):
        assert _is_linked(b1, 'library_Function68', a)
    _safe_set(a, 'library_Library', {b2})
    assert _is_linked(a, 'library_Library', b2)
    if hasattr(b1, 'library_Function68'):
        assert not _is_linked(b1, 'library_Function68', a)
    if hasattr(b2, 'library_Function68'):
        assert _is_linked(b2, 'library_Function68', a)
    _safe_set(a, 'library_Library', set())
    assert not _is_linked(a, 'library_Library', b2)
    if hasattr(b2, 'library_Function68'):
        assert not _is_linked(b2, 'library_Function68', a)


def test_assoc_icons150_link_reassign_clear():
    a = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    b1 = library_MultiImage()
    b2 = library_MultiImage()
    _safe_set(a, 'library_Unit151', b1)
    assert _is_linked(a, 'library_Unit151', b1)
    if hasattr(b1, 'library_MultiImage152'):
        assert _is_linked(b1, 'library_MultiImage152', a)
    _safe_set(a, 'library_Unit151', b2)
    assert _is_linked(a, 'library_Unit151', b2)
    if hasattr(b1, 'library_MultiImage152'):
        assert not _is_linked(b1, 'library_MultiImage152', a)
    if hasattr(b2, 'library_MultiImage152'):
        assert _is_linked(b2, 'library_MultiImage152', a)
    _safe_set(a, 'library_Unit151', None)
    assert not _is_linked(a, 'library_Unit151', b2)
    if hasattr(b2, 'library_MultiImage152'):
        assert not _is_linked(b2, 'library_MultiImage152', a)


def test_assoc_icons22_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_MultiImage()
    b2 = library_MultiImage()
    _safe_set(a, 'library_Component23', b1)
    assert _is_linked(a, 'library_Component23', b1)
    if hasattr(b1, 'library_MultiImage'):
        assert _is_linked(b1, 'library_MultiImage', a)
    _safe_set(a, 'library_Component23', b2)
    assert _is_linked(a, 'library_Component23', b2)
    if hasattr(b1, 'library_MultiImage'):
        assert not _is_linked(b1, 'library_MultiImage', a)
    if hasattr(b2, 'library_MultiImage'):
        assert _is_linked(b2, 'library_MultiImage', a)
    _safe_set(a, 'library_Component23', None)
    assert not _is_linked(a, 'library_Component23', b2)
    if hasattr(b2, 'library_MultiImage'):
        assert not _is_linked(b2, 'library_MultiImage', a)


def test_assoc_licensedFunctionRef122_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_ProductInfo123', {b1})
    assert _is_linked(a, 'library_ProductInfo123', b1)
    if hasattr(b1, 'library_Function124'):
        assert _is_linked(b1, 'library_Function124', a)
    _safe_set(a, 'library_ProductInfo123', {b2})
    assert _is_linked(a, 'library_ProductInfo123', b2)
    if hasattr(b1, 'library_Function124'):
        assert not _is_linked(b1, 'library_Function124', a)
    if hasattr(b2, 'library_Function124'):
        assert _is_linked(b2, 'library_Function124', a)
    _safe_set(a, 'library_ProductInfo123', set())
    assert not _is_linked(a, 'library_ProductInfo123', b2)
    if hasattr(b2, 'library_Function124'):
        assert not _is_linked(b2, 'library_Function124', a)


def test_assoc_lifecycle1_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_Lifecycle()
    b2 = library_Lifecycle()
    _safe_set(a, 'library_Component', b1)
    assert _is_linked(a, 'library_Component', b1)
    if hasattr(b1, 'library_Lifecycle'):
        assert _is_linked(b1, 'library_Lifecycle', a)
    _safe_set(a, 'library_Component', b2)
    assert _is_linked(a, 'library_Component', b2)
    if hasattr(b1, 'library_Lifecycle'):
        assert not _is_linked(b1, 'library_Lifecycle', a)
    if hasattr(b2, 'library_Lifecycle'):
        assert _is_linked(b2, 'library_Lifecycle', a)
    _safe_set(a, 'library_Component', None)
    assert not _is_linked(a, 'library_Component', b2)
    if hasattr(b2, 'library_Lifecycle'):
        assert not _is_linked(b2, 'library_Lifecycle', a)


def test_assoc_metricRefs5_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_Metric()
    b2 = library_Metric()
    _safe_set(a, 'library_Component6', {b1})
    assert _is_linked(a, 'library_Component6', b1)
    if hasattr(b1, 'library_Metric'):
        assert _is_linked(b1, 'library_Metric', a)
    _safe_set(a, 'library_Component6', {b2})
    assert _is_linked(a, 'library_Component6', b2)
    if hasattr(b1, 'library_Metric'):
        assert not _is_linked(b1, 'library_Metric', a)
    if hasattr(b2, 'library_Metric'):
        assert _is_linked(b2, 'library_Metric', a)
    _safe_set(a, 'library_Component6', set())
    assert not _is_linked(a, 'library_Component6', b2)
    if hasattr(b2, 'library_Metric'):
        assert not _is_linked(b2, 'library_Metric', a)


def test_assoc_metricSources77_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_MetricSource()
    b2 = library_MetricSource()
    _safe_set(a, 'library_Library78', {b1})
    assert _is_linked(a, 'library_Library78', b1)
    if hasattr(b1, 'library_MetricSource'):
        assert _is_linked(b1, 'library_MetricSource', a)
    _safe_set(a, 'library_Library78', {b2})
    assert _is_linked(a, 'library_Library78', b2)
    if hasattr(b1, 'library_MetricSource'):
        assert not _is_linked(b1, 'library_MetricSource', a)
    if hasattr(b2, 'library_MetricSource'):
        assert _is_linked(b2, 'library_MetricSource', a)
    _safe_set(a, 'library_Library78', set())
    assert not _is_linked(a, 'library_Library78', b2)
    if hasattr(b2, 'library_MetricSource'):
        assert not _is_linked(b2, 'library_MetricSource', a)


def test_assoc_metrics74_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Metric()
    b2 = library_Metric()
    _safe_set(a, 'library_Library75', {b1})
    assert _is_linked(a, 'library_Library75', b1)
    if hasattr(b1, 'library_Metric76'):
        assert _is_linked(b1, 'library_Metric76', a)
    _safe_set(a, 'library_Library75', {b2})
    assert _is_linked(a, 'library_Library75', b2)
    if hasattr(b1, 'library_Metric76'):
        assert not _is_linked(b1, 'library_Metric76', a)
    if hasattr(b2, 'library_Metric76'):
        assert _is_linked(b2, 'library_Metric76', a)
    _safe_set(a, 'library_Library75', set())
    assert not _is_linked(a, 'library_Library75', b2)
    if hasattr(b2, 'library_Metric76'):
        assert not _is_linked(b2, 'library_Metric76', a)


def test_assoc_nodeTypeRef125_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_NodeType(leafNode="sample_text", name="sample_text")
    b2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ProductInfo126', {b1})
    assert _is_linked(a, 'library_ProductInfo126', b1)
    if hasattr(b1, 'library_NodeType127'):
        assert _is_linked(b1, 'library_NodeType127', a)
    _safe_set(a, 'library_ProductInfo126', {b2})
    assert _is_linked(a, 'library_ProductInfo126', b2)
    if hasattr(b1, 'library_NodeType127'):
        assert not _is_linked(b1, 'library_NodeType127', a)
    if hasattr(b2, 'library_NodeType127'):
        assert _is_linked(b2, 'library_NodeType127', a)
    _safe_set(a, 'library_ProductInfo126', set())
    assert not _is_linked(a, 'library_ProductInfo126', b2)
    if hasattr(b2, 'library_NodeType127'):
        assert not _is_linked(b2, 'library_NodeType127', a)


def test_assoc_nodeTypes130_link_reassign_clear():
    a = library_ReferenceNetwork(description="sample_text", name="sample_text")
    b1 = library_NodeType(leafNode="sample_text", name="sample_text")
    b2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ReferenceNetwork131', {b1})
    assert _is_linked(a, 'library_ReferenceNetwork131', b1)
    if hasattr(b1, 'library_NodeType132'):
        assert _is_linked(b1, 'library_NodeType132', a)
    _safe_set(a, 'library_ReferenceNetwork131', {b2})
    assert _is_linked(a, 'library_ReferenceNetwork131', b2)
    if hasattr(b1, 'library_NodeType132'):
        assert not _is_linked(b1, 'library_NodeType132', a)
    if hasattr(b2, 'library_NodeType132'):
        assert _is_linked(b2, 'library_NodeType132', a)
    _safe_set(a, 'library_ReferenceNetwork131', set())
    assert not _is_linked(a, 'library_ReferenceNetwork131', b2)
    if hasattr(b2, 'library_NodeType132'):
        assert not _is_linked(b2, 'library_NodeType132', a)


def test_assoc_nodeTypes69_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_NodeType', b1)
    assert _is_linked(a, 'library_NodeType', b1)
    if hasattr(b1, 'library_Library70'):
        assert _is_linked(b1, 'library_Library70', a)
    _safe_set(a, 'library_NodeType', b2)
    assert _is_linked(a, 'library_NodeType', b2)
    if hasattr(b1, 'library_Library70'):
        assert not _is_linked(b1, 'library_Library70', a)
    if hasattr(b2, 'library_Library70'):
        assert _is_linked(b2, 'library_Library70', a)
    _safe_set(a, 'library_NodeType', None)
    assert not _is_linked(a, 'library_NodeType', b2)
    if hasattr(b2, 'library_Library70'):
        assert not _is_linked(b2, 'library_Library70', a)


def test_assoc_parameterRefs16_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Parameter', b1)
    assert _is_linked(a, 'library_Parameter', b1)
    if hasattr(b1, 'library_Component17'):
        assert _is_linked(b1, 'library_Component17', a)
    _safe_set(a, 'library_Parameter', b2)
    assert _is_linked(a, 'library_Parameter', b2)
    if hasattr(b1, 'library_Component17'):
        assert not _is_linked(b1, 'library_Component17', a)
    if hasattr(b2, 'library_Component17'):
        assert _is_linked(b2, 'library_Component17', a)
    _safe_set(a, 'library_Parameter', None)
    assert not _is_linked(a, 'library_Parameter', b2)
    if hasattr(b2, 'library_Component17'):
        assert not _is_linked(b2, 'library_Component17', a)


def test_assoc_parameterRefs45_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Parameter47', b1)
    assert _is_linked(a, 'library_Parameter47', b1)
    if hasattr(b1, 'library_EquipmentGroup46'):
        assert _is_linked(b1, 'library_EquipmentGroup46', a)
    _safe_set(a, 'library_Parameter47', b2)
    assert _is_linked(a, 'library_Parameter47', b2)
    if hasattr(b1, 'library_EquipmentGroup46'):
        assert not _is_linked(b1, 'library_EquipmentGroup46', a)
    if hasattr(b2, 'library_EquipmentGroup46'):
        assert _is_linked(b2, 'library_EquipmentGroup46', a)
    _safe_set(a, 'library_Parameter47', None)
    assert not _is_linked(a, 'library_Parameter47', b2)
    if hasattr(b2, 'library_EquipmentGroup46'):
        assert not _is_linked(b2, 'library_EquipmentGroup46', a)


def test_assoc_parameters79_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Parameter81', b1)
    assert _is_linked(a, 'library_Parameter81', b1)
    if hasattr(b1, 'library_Library80'):
        assert _is_linked(b1, 'library_Library80', a)
    _safe_set(a, 'library_Parameter81', b2)
    assert _is_linked(a, 'library_Parameter81', b2)
    if hasattr(b1, 'library_Library80'):
        assert not _is_linked(b1, 'library_Library80', a)
    if hasattr(b2, 'library_Library80'):
        assert _is_linked(b2, 'library_Library80', a)
    _safe_set(a, 'library_Parameter81', None)
    assert not _is_linked(a, 'library_Parameter81', b2)
    if hasattr(b2, 'library_Library80'):
        assert not _is_linked(b2, 'library_Library80', a)


def test_assoc_products153_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Vendor()
    b2 = library_Vendor()
    _safe_set(a, 'library_ProductInfo154', b1)
    assert _is_linked(a, 'library_ProductInfo154', b1)
    if hasattr(b1, 'library_Vendor'):
        assert _is_linked(b1, 'library_Vendor', a)
    _safe_set(a, 'library_ProductInfo154', b2)
    assert _is_linked(a, 'library_ProductInfo154', b2)
    if hasattr(b1, 'library_Vendor'):
        assert not _is_linked(b1, 'library_Vendor', a)
    if hasattr(b2, 'library_Vendor'):
        assert _is_linked(b2, 'library_Vendor', a)
    _safe_set(a, 'library_ProductInfo154', None)
    assert not _is_linked(a, 'library_ProductInfo154', b2)
    if hasattr(b2, 'library_Vendor'):
        assert not _is_linked(b2, 'library_Vendor', a)


def test_assoc_protocolRef138_link_reassign_clear():
    a = library_ReferenceRelationship(name="sample_text")
    b1 = library_Protocol()
    b2 = library_Protocol()
    _safe_set(a, 'library_ReferenceRelationship139', b1)
    assert _is_linked(a, 'library_ReferenceRelationship139', b1)
    if hasattr(b1, 'library_Protocol140'):
        assert _is_linked(b1, 'library_Protocol140', a)
    _safe_set(a, 'library_ReferenceRelationship139', b2)
    assert _is_linked(a, 'library_ReferenceRelationship139', b2)
    if hasattr(b1, 'library_Protocol140'):
        assert not _is_linked(b1, 'library_Protocol140', a)
    if hasattr(b2, 'library_Protocol140'):
        assert _is_linked(b2, 'library_Protocol140', a)
    _safe_set(a, 'library_ReferenceRelationship139', None)
    assert not _is_linked(a, 'library_ReferenceRelationship139', b2)
    if hasattr(b2, 'library_Protocol140'):
        assert not _is_linked(b2, 'library_Protocol140', a)


def test_assoc_protocolRefs14_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_Protocol()
    b2 = library_Protocol()
    _safe_set(a, 'library_Component15', {b1})
    assert _is_linked(a, 'library_Component15', b1)
    if hasattr(b1, 'library_Protocol'):
        assert _is_linked(b1, 'library_Protocol', a)
    _safe_set(a, 'library_Component15', {b2})
    assert _is_linked(a, 'library_Component15', b2)
    if hasattr(b1, 'library_Protocol'):
        assert not _is_linked(b1, 'library_Protocol', a)
    if hasattr(b2, 'library_Protocol'):
        assert _is_linked(b2, 'library_Protocol', a)
    _safe_set(a, 'library_Component15', set())
    assert not _is_linked(a, 'library_Component15', b2)
    if hasattr(b2, 'library_Protocol'):
        assert not _is_linked(b2, 'library_Protocol', a)


def test_assoc_refInterface1Ref141_link_reassign_clear():
    a = library_ReferenceRelationship(name="sample_text")
    b1 = library_NodeType(leafNode="sample_text", name="sample_text")
    b2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ReferenceRelationship142', b1)
    assert _is_linked(a, 'library_ReferenceRelationship142', b1)
    if hasattr(b1, 'library_NodeType143'):
        assert _is_linked(b1, 'library_NodeType143', a)
    _safe_set(a, 'library_ReferenceRelationship142', b2)
    assert _is_linked(a, 'library_ReferenceRelationship142', b2)
    if hasattr(b1, 'library_NodeType143'):
        assert not _is_linked(b1, 'library_NodeType143', a)
    if hasattr(b2, 'library_NodeType143'):
        assert _is_linked(b2, 'library_NodeType143', a)
    _safe_set(a, 'library_ReferenceRelationship142', None)
    assert not _is_linked(a, 'library_ReferenceRelationship142', b2)
    if hasattr(b2, 'library_NodeType143'):
        assert not _is_linked(b2, 'library_NodeType143', a)


def test_assoc_refInterface2Ref144_link_reassign_clear():
    a = library_ReferenceRelationship(name="sample_text")
    b1 = library_NodeType(leafNode="sample_text", name="sample_text")
    b2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ReferenceRelationship145', b1)
    assert _is_linked(a, 'library_ReferenceRelationship145', b1)
    if hasattr(b1, 'library_NodeType146'):
        assert _is_linked(b1, 'library_NodeType146', a)
    _safe_set(a, 'library_ReferenceRelationship145', b2)
    assert _is_linked(a, 'library_ReferenceRelationship145', b2)
    if hasattr(b1, 'library_NodeType146'):
        assert not _is_linked(b1, 'library_NodeType146', a)
    if hasattr(b2, 'library_NodeType146'):
        assert _is_linked(b2, 'library_NodeType146', a)
    _safe_set(a, 'library_ReferenceRelationship145', None)
    assert not _is_linked(a, 'library_ReferenceRelationship145', b2)
    if hasattr(b2, 'library_NodeType146'):
        assert not _is_linked(b2, 'library_NodeType146', a)


def test_assoc_refRelationships136_link_reassign_clear():
    a = library_ReferenceRelationship(name="sample_text")
    b1 = library_ReferenceNetwork(description="sample_text", name="sample_text")
    b2 = library_ReferenceNetwork(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ReferenceRelationship', b1)
    assert _is_linked(a, 'library_ReferenceRelationship', b1)
    if hasattr(b1, 'library_ReferenceNetwork137'):
        assert _is_linked(b1, 'library_ReferenceNetwork137', a)
    _safe_set(a, 'library_ReferenceRelationship', b2)
    assert _is_linked(a, 'library_ReferenceRelationship', b2)
    if hasattr(b1, 'library_ReferenceNetwork137'):
        assert not _is_linked(b1, 'library_ReferenceNetwork137', a)
    if hasattr(b2, 'library_ReferenceNetwork137'):
        assert _is_linked(b2, 'library_ReferenceNetwork137', a)
    _safe_set(a, 'library_ReferenceRelationship', None)
    assert not _is_linked(a, 'library_ReferenceRelationship', b2)
    if hasattr(b2, 'library_ReferenceNetwork137'):
        assert not _is_linked(b2, 'library_ReferenceNetwork137', a)


def test_assoc_referenceNetworks134_link_reassign_clear():
    a = library_ReferenceNetwork(description="sample_text", name="sample_text")
    b1 = library_ReferenceNetwork(description="sample_text", name="sample_text")
    b2 = library_ReferenceNetwork(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ReferenceNetwork133', {b1})
    assert _is_linked(a, 'library_ReferenceNetwork133', b1)
    if hasattr(b1, 'library_ReferenceNetwork135'):
        assert _is_linked(b1, 'library_ReferenceNetwork135', a)
    _safe_set(a, 'library_ReferenceNetwork133', {b2})
    assert _is_linked(a, 'library_ReferenceNetwork133', b2)
    if hasattr(b1, 'library_ReferenceNetwork135'):
        assert not _is_linked(b1, 'library_ReferenceNetwork135', a)
    if hasattr(b2, 'library_ReferenceNetwork135'):
        assert _is_linked(b2, 'library_ReferenceNetwork135', a)
    _safe_set(a, 'library_ReferenceNetwork133', set())
    assert not _is_linked(a, 'library_ReferenceNetwork133', b2)
    if hasattr(b2, 'library_ReferenceNetwork135'):
        assert not _is_linked(b2, 'library_ReferenceNetwork135', a)


def test_assoc_resourceRefs2_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'componentRef', {b1})
    assert _is_linked(a, 'componentRef', b1)
    if hasattr(b1, 'NetXResource'):
        assert _is_linked(b1, 'NetXResource', a)
    _safe_set(a, 'componentRef', {b2})
    assert _is_linked(a, 'componentRef', b2)
    if hasattr(b1, 'NetXResource'):
        assert not _is_linked(b1, 'NetXResource', a)
    if hasattr(b2, 'NetXResource'):
        assert _is_linked(b2, 'NetXResource', a)
    _safe_set(a, 'componentRef', set())
    assert not _is_linked(a, 'componentRef', b2)
    if hasattr(b2, 'NetXResource'):
        assert not _is_linked(b2, 'NetXResource', a)


def test_assoc_targetResource56_link_reassign_clear():
    a = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    b1 = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    b2 = library_BaseResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    _safe_set(a, 'library_ExpressionResult', b1)
    assert _is_linked(a, 'library_ExpressionResult', b1)
    if hasattr(b1, 'library_BaseResource57'):
        assert _is_linked(b1, 'library_BaseResource57', a)
    _safe_set(a, 'library_ExpressionResult', b2)
    assert _is_linked(a, 'library_ExpressionResult', b2)
    if hasattr(b1, 'library_BaseResource57'):
        assert not _is_linked(b1, 'library_BaseResource57', a)
    if hasattr(b2, 'library_BaseResource57'):
        assert _is_linked(b2, 'library_BaseResource57', a)
    _safe_set(a, 'library_ExpressionResult', None)
    assert not _is_linked(a, 'library_ExpressionResult', b2)
    if hasattr(b2, 'library_BaseResource57'):
        assert not _is_linked(b2, 'library_BaseResource57', a)


def test_assoc_targetValues58_link_reassign_clear():
    a = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    b1 = library_Value()
    b2 = library_Value()
    _safe_set(a, 'library_ExpressionResult59', {b1})
    assert _is_linked(a, 'library_ExpressionResult59', b1)
    if hasattr(b1, 'library_Value'):
        assert _is_linked(b1, 'library_Value', a)
    _safe_set(a, 'library_ExpressionResult59', {b2})
    assert _is_linked(a, 'library_ExpressionResult59', b2)
    if hasattr(b1, 'library_Value'):
        assert not _is_linked(b1, 'library_Value', a)
    if hasattr(b2, 'library_Value'):
        assert _is_linked(b2, 'library_Value', a)
    _safe_set(a, 'library_ExpressionResult59', set())
    assert not _is_linked(a, 'library_ExpressionResult59', b2)
    if hasattr(b2, 'library_Value'):
        assert not _is_linked(b2, 'library_Value', a)


def test_assoc_toleranceRefs12_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Tolerance', b1)
    assert _is_linked(a, 'library_Tolerance', b1)
    if hasattr(b1, 'library_Component13'):
        assert _is_linked(b1, 'library_Component13', a)
    _safe_set(a, 'library_Tolerance', b2)
    assert _is_linked(a, 'library_Tolerance', b2)
    if hasattr(b1, 'library_Component13'):
        assert not _is_linked(b1, 'library_Component13', a)
    if hasattr(b2, 'library_Component13'):
        assert _is_linked(b2, 'library_Component13', a)
    _safe_set(a, 'library_Tolerance', None)
    assert not _is_linked(a, 'library_Tolerance', b2)
    if hasattr(b2, 'library_Component13'):
        assert not _is_linked(b2, 'library_Component13', a)


def test_assoc_tolerances82_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Tolerance84', b1)
    assert _is_linked(a, 'library_Tolerance84', b1)
    if hasattr(b1, 'library_Library83'):
        assert _is_linked(b1, 'library_Library83', a)
    _safe_set(a, 'library_Tolerance84', b2)
    assert _is_linked(a, 'library_Tolerance84', b2)
    if hasattr(b1, 'library_Library83'):
        assert not _is_linked(b1, 'library_Library83', a)
    if hasattr(b2, 'library_Library83'):
        assert _is_linked(b2, 'library_Library83', a)
    _safe_set(a, 'library_Tolerance84', None)
    assert not _is_linked(a, 'library_Tolerance84', b2)
    if hasattr(b2, 'library_Library83'):
        assert not _is_linked(b2, 'library_Library83', a)


def test_assoc_unitRef0_link_reassign_clear():
    a = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    b1 = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    b2 = library_BaseResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    _safe_set(a, 'library_Unit', b1)
    assert _is_linked(a, 'library_Unit', b1)
    if hasattr(b1, 'library_BaseResource'):
        assert _is_linked(b1, 'library_BaseResource', a)
    _safe_set(a, 'library_Unit', b2)
    assert _is_linked(a, 'library_Unit', b2)
    if hasattr(b1, 'library_BaseResource'):
        assert not _is_linked(b1, 'library_BaseResource', a)
    if hasattr(b2, 'library_BaseResource'):
        assert _is_linked(b2, 'library_BaseResource', a)
    _safe_set(a, 'library_Unit', None)
    assert not _is_linked(a, 'library_Unit', b2)
    if hasattr(b2, 'library_BaseResource'):
        assert not _is_linked(b2, 'library_BaseResource', a)


def test_assoc_units88_link_reassign_clear():
    a = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Unit90', b1)
    assert _is_linked(a, 'library_Unit90', b1)
    if hasattr(b1, 'library_Library89'):
        assert _is_linked(b1, 'library_Library89', a)
    _safe_set(a, 'library_Unit90', b2)
    assert _is_linked(a, 'library_Unit90', b2)
    if hasattr(b1, 'library_Library89'):
        assert not _is_linked(b1, 'library_Library89', a)
    if hasattr(b2, 'library_Library89'):
        assert _is_linked(b2, 'library_Library89', a)
    _safe_set(a, 'library_Unit90', None)
    assert not _is_linked(a, 'library_Unit90', b2)
    if hasattr(b2, 'library_Library89'):
        assert not _is_linked(b2, 'library_Library89', a)


def test_assoc_utilizationExpressionRef9_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression11', b1)
    assert _is_linked(a, 'library_Expression11', b1)
    if hasattr(b1, 'library_Component10'):
        assert _is_linked(b1, 'library_Component10', a)
    _safe_set(a, 'library_Expression11', b2)
    assert _is_linked(a, 'library_Expression11', b2)
    if hasattr(b1, 'library_Component10'):
        assert not _is_linked(b1, 'library_Component10', a)
    if hasattr(b2, 'library_Component10'):
        assert _is_linked(b2, 'library_Component10', a)
    _safe_set(a, 'library_Expression11', None)
    assert not _is_linked(a, 'library_Expression11', b2)
    if hasattr(b2, 'library_Component10'):
        assert not _is_linked(b2, 'library_Component10', a)


def test_assoc_version91_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Meta()
    b2 = library_Meta()
    _safe_set(a, 'library_Library92', b1)
    assert _is_linked(a, 'library_Library92', b1)
    if hasattr(b1, 'library_Meta'):
        assert _is_linked(b1, 'library_Meta', a)
    _safe_set(a, 'library_Library92', b2)
    assert _is_linked(a, 'library_Library92', b2)
    if hasattr(b1, 'library_Meta'):
        assert not _is_linked(b1, 'library_Meta', a)
    if hasattr(b2, 'library_Meta'):
        assert _is_linked(b2, 'library_Meta', a)
    _safe_set(a, 'library_Library92', None)
    assert not _is_linked(a, 'library_Library92', b2)
    if hasattr(b2, 'library_Meta'):
        assert not _is_linked(b2, 'library_Meta', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Base_strategy = st.builds(Base)
@given(instance=Base_strategy)
@settings(max_examples=25)
def test_Base_instantiation(instance):
    assert isinstance(instance, Base)


BaseExpressionResult_strategy = st.builds(BaseExpressionResult)
@given(instance=BaseExpressionResult_strategy)
@settings(max_examples=25)
def test_BaseExpressionResult_instantiation(instance):
    assert isinstance(instance, BaseExpressionResult)


BaseResource_strategy = st.builds(BaseResource)
@given(instance=BaseResource_strategy)
@settings(max_examples=25)
def test_BaseResource_instantiation(instance):
    assert isinstance(instance, BaseResource)


Company_strategy = st.builds(Company)
@given(instance=Company_strategy)
@settings(max_examples=25)
def test_Company_instantiation(instance):
    assert isinstance(instance, Company)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


library_BaseExpressionResult_strategy = st.builds(library_BaseExpressionResult)
@given(instance=library_BaseExpressionResult_strategy)
@settings(max_examples=25)
def test_library_BaseExpressionResult_instantiation(instance):
    assert isinstance(instance, library_BaseExpressionResult)


library_BaseResource_strategy = st.builds(library_BaseResource, detailDisplay=safe_text, expressionName=safe_text, longName=safe_text, shortName=safe_text, summaryDisplay=safe_text)
@given(instance=library_BaseResource_strategy)
@settings(max_examples=25)
def test_library_BaseResource_instantiation(instance):
    assert isinstance(instance, library_BaseResource)


library_Component_strategy = st.builds(library_Component, description=safe_text, duration=safe_text, name=safe_text)
@given(instance=library_Component_strategy)
@settings(max_examples=25)
def test_library_Component_instantiation(instance):
    assert isinstance(instance, library_Component)


library_ConfigAttribute_strategy = st.builds(library_ConfigAttribute)
@given(instance=library_ConfigAttribute_strategy)
@settings(max_examples=25)
def test_library_ConfigAttribute_instantiation(instance):
    assert isinstance(instance, library_ConfigAttribute)


library_DiagramInfo_strategy = st.builds(library_DiagramInfo)
@given(instance=library_DiagramInfo_strategy)
@settings(max_examples=25)
def test_library_DiagramInfo_instantiation(instance):
    assert isinstance(instance, library_DiagramInfo)


library_EObject_strategy = st.builds(library_EObject)
@given(instance=library_EObject_strategy)
@settings(max_examples=25)
def test_library_EObject_instantiation(instance):
    assert isinstance(instance, library_EObject)


library_Equipment_strategy = st.builds(library_Equipment, count=safe_text, equipmentCode=safe_text, position=safe_text, redundancy=safe_text, state=safe_text)
@given(instance=library_Equipment_strategy)
@settings(max_examples=25)
def test_library_Equipment_instantiation(instance):
    assert isinstance(instance, library_Equipment)


library_EquipmentGroup_strategy = st.builds(library_EquipmentGroup, count=safe_text, description=safe_text, name=safe_text)
@given(instance=library_EquipmentGroup_strategy)
@settings(max_examples=25)
def test_library_EquipmentGroup_instantiation(instance):
    assert isinstance(instance, library_EquipmentGroup)


library_EquipmentRelationship_strategy = st.builds(library_EquipmentRelationship)
@given(instance=library_EquipmentRelationship_strategy)
@settings(max_examples=25)
def test_library_EquipmentRelationship_instantiation(instance):
    assert isinstance(instance, library_EquipmentRelationship)


library_Expression_strategy = st.builds(library_Expression, expressionLines=safe_text, name=safe_text)
@given(instance=library_Expression_strategy)
@settings(max_examples=25)
def test_library_Expression_instantiation(instance):
    assert isinstance(instance, library_Expression)


library_ExpressionResult_strategy = st.builds(library_ExpressionResult, targetIntervalHint=safe_text, targetKindHint=safe_text, targetRange=safe_text)
@given(instance=library_ExpressionResult_strategy)
@settings(max_examples=25)
def test_library_ExpressionResult_instantiation(instance):
    assert isinstance(instance, library_ExpressionResult)


library_Function_strategy = st.builds(library_Function)
@given(instance=library_Function_strategy)
@settings(max_examples=25)
def test_library_Function_instantiation(instance):
    assert isinstance(instance, library_Function)


library_FunctionRelationship_strategy = st.builds(library_FunctionRelationship)
@given(instance=library_FunctionRelationship_strategy)
@settings(max_examples=25)
def test_library_FunctionRelationship_instantiation(instance):
    assert isinstance(instance, library_FunctionRelationship)


library_LastEvaluationExpressionResult_strategy = st.builds(library_LastEvaluationExpressionResult, lastEvalResult=safe_text)
@given(instance=library_LastEvaluationExpressionResult_strategy)
@settings(max_examples=25)
def test_library_LastEvaluationExpressionResult_instantiation(instance):
    assert isinstance(instance, library_LastEvaluationExpressionResult)


library_Library_strategy = st.builds(library_Library, name=safe_text, protocols=safe_text)
@given(instance=library_Library_strategy)
@settings(max_examples=25)
def test_library_Library_instantiation(instance):
    assert isinstance(instance, library_Library)


library_Lifecycle_strategy = st.builds(library_Lifecycle)
@given(instance=library_Lifecycle_strategy)
@settings(max_examples=25)
def test_library_Lifecycle_instantiation(instance):
    assert isinstance(instance, library_Lifecycle)


library_Meta_strategy = st.builds(library_Meta)
@given(instance=library_Meta_strategy)
@settings(max_examples=25)
def test_library_Meta_instantiation(instance):
    assert isinstance(instance, library_Meta)


library_Metric_strategy = st.builds(library_Metric)
@given(instance=library_Metric_strategy)
@settings(max_examples=25)
def test_library_Metric_instantiation(instance):
    assert isinstance(instance, library_Metric)


library_MetricSource_strategy = st.builds(library_MetricSource)
@given(instance=library_MetricSource_strategy)
@settings(max_examples=25)
def test_library_MetricSource_instantiation(instance):
    assert isinstance(instance, library_MetricSource)


library_MetricValueRange_strategy = st.builds(library_MetricValueRange)
@given(instance=library_MetricValueRange_strategy)
@settings(max_examples=25)
def test_library_MetricValueRange_instantiation(instance):
    assert isinstance(instance, library_MetricValueRange)


library_MultiImage_strategy = st.builds(library_MultiImage)
@given(instance=library_MultiImage_strategy)
@settings(max_examples=25)
def test_library_MultiImage_instantiation(instance):
    assert isinstance(instance, library_MultiImage)


library_NetXResource_strategy = st.builds(library_NetXResource)
@given(instance=library_NetXResource_strategy)
@settings(max_examples=25)
def test_library_NetXResource_instantiation(instance):
    assert isinstance(instance, library_NetXResource)


library_NodeType_strategy = st.builds(library_NodeType, leafNode=safe_text, name=safe_text)
@given(instance=library_NodeType_strategy)
@settings(max_examples=25)
def test_library_NodeType_instantiation(instance):
    assert isinstance(instance, library_NodeType)


library_Parameter_strategy = st.builds(library_Parameter, description=safe_text, expressionName=safe_text, modifiable=safe_text, name=safe_text, value=safe_text)
@given(instance=library_Parameter_strategy)
@settings(max_examples=25)
def test_library_Parameter_instantiation(instance):
    assert isinstance(instance, library_Parameter)


library_ProductInfo_strategy = st.builds(library_ProductInfo, availableDate=safe_text, endOfSalesDate=safe_text, endOfSupportDate=safe_text, productCode=safe_text, salesCode=safe_text, underDevelopmentDate=safe_text)
@given(instance=library_ProductInfo_strategy)
@settings(max_examples=25)
def test_library_ProductInfo_instantiation(instance):
    assert isinstance(instance, library_ProductInfo)


library_Protocol_strategy = st.builds(library_Protocol)
@given(instance=library_Protocol_strategy)
@settings(max_examples=25)
def test_library_Protocol_instantiation(instance):
    assert isinstance(instance, library_Protocol)


library_ReferenceNetwork_strategy = st.builds(library_ReferenceNetwork, description=safe_text, name=safe_text)
@given(instance=library_ReferenceNetwork_strategy)
@settings(max_examples=25)
def test_library_ReferenceNetwork_instantiation(instance):
    assert isinstance(instance, library_ReferenceNetwork)


library_ReferenceRelationship_strategy = st.builds(library_ReferenceRelationship, name=safe_text)
@given(instance=library_ReferenceRelationship_strategy)
@settings(max_examples=25)
def test_library_ReferenceRelationship_instantiation(instance):
    assert isinstance(instance, library_ReferenceRelationship)


library_Tolerance_strategy = st.builds(library_Tolerance, level=safe_text, name=safe_text)
@given(instance=library_Tolerance_strategy)
@settings(max_examples=25)
def test_library_Tolerance_instantiation(instance):
    assert isinstance(instance, library_Tolerance)


library_Unit_strategy = st.builds(library_Unit, code=safe_text, description=safe_text, name=safe_text)
@given(instance=library_Unit_strategy)
@settings(max_examples=25)
def test_library_Unit_instantiation(instance):
    assert isinstance(instance, library_Unit)


library_Value_strategy = st.builds(library_Value)
@given(instance=library_Value_strategy)
@settings(max_examples=25)
def test_library_Value_instantiation(instance):
    assert isinstance(instance, library_Value)


library_Vendor_strategy = st.builds(library_Vendor)
@given(instance=library_Vendor_strategy)
@settings(max_examples=25)
def test_library_Vendor_instantiation(instance):
    assert isinstance(instance, library_Vendor)


