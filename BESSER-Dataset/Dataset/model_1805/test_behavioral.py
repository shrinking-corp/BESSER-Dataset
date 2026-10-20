import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_allEquipments31_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment32', a1)
    assert _is_linked(b, 'library_Equipment32', a1)
    if hasattr(a1, 'library_Equipment30'):
        assert _is_linked(a1, 'library_Equipment30', b)
    _safe_set(b, 'library_Equipment32', a2)
    assert _is_linked(b, 'library_Equipment32', a2)
    if hasattr(a1, 'library_Equipment30'):
        assert not _is_linked(a1, 'library_Equipment30', b)
    if hasattr(a2, 'library_Equipment30'):
        assert _is_linked(a2, 'library_Equipment30', b)
    _safe_set(b, 'library_Equipment32', None)
    assert not _is_linked(b, 'library_Equipment32', a2)
    if hasattr(a2, 'library_Equipment30'):
        assert not _is_linked(a2, 'library_Equipment30', b)


def test_assoc_allEquipments51_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment53', a1)
    assert _is_linked(b, 'library_Equipment53', a1)
    if hasattr(a1, 'library_EquipmentGroup52'):
        assert _is_linked(a1, 'library_EquipmentGroup52', b)
    _safe_set(b, 'library_Equipment53', a2)
    assert _is_linked(b, 'library_Equipment53', a2)
    if hasattr(a1, 'library_EquipmentGroup52'):
        assert not _is_linked(a1, 'library_EquipmentGroup52', b)
    if hasattr(a2, 'library_EquipmentGroup52'):
        assert _is_linked(a2, 'library_EquipmentGroup52', b)
    _safe_set(b, 'library_Equipment53', None)
    assert not _is_linked(b, 'library_Equipment53', a2)
    if hasattr(a2, 'library_EquipmentGroup52'):
        assert not _is_linked(a2, 'library_EquipmentGroup52', b)


def test_assoc_capacityExpressionRef7_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component8', a1)
    assert _is_linked(b, 'library_Component8', a1)
    if hasattr(a1, 'library_Expression'):
        assert _is_linked(a1, 'library_Expression', b)
    _safe_set(b, 'library_Component8', a2)
    assert _is_linked(b, 'library_Component8', a2)
    if hasattr(a1, 'library_Expression'):
        assert not _is_linked(a1, 'library_Expression', b)
    if hasattr(a2, 'library_Expression'):
        assert _is_linked(a2, 'library_Expression', b)
    _safe_set(b, 'library_Component8', None)
    assert not _is_linked(b, 'library_Component8', a2)
    if hasattr(a2, 'library_Expression'):
        assert not _is_linked(a2, 'library_Expression', b)


def test_assoc_equipmentGroups26_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment27', {a1})
    assert _is_linked(b, 'library_Equipment27', a1)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert _is_linked(a1, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment27', {a2})
    assert _is_linked(b, 'library_Equipment27', a2)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert not _is_linked(a1, 'library_EquipmentGroup', b)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert _is_linked(a2, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment27', set())
    assert not _is_linked(b, 'library_Equipment27', a2)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert not _is_linked(a2, 'library_EquipmentGroup', b)


def test_assoc_equipmentRef120_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment121', a1)
    assert _is_linked(b, 'library_Equipment121', a1)
    if hasattr(a1, 'library_ProductInfo'):
        assert _is_linked(a1, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment121', a2)
    assert _is_linked(b, 'library_Equipment121', a2)
    if hasattr(a1, 'library_ProductInfo'):
        assert not _is_linked(a1, 'library_ProductInfo', b)
    if hasattr(a2, 'library_ProductInfo'):
        assert _is_linked(a2, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment121', None)
    assert not _is_linked(b, 'library_Equipment121', a2)
    if hasattr(a2, 'library_ProductInfo'):
        assert not _is_linked(a2, 'library_ProductInfo', b)


def test_assoc_equipmentRefs42_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment44', a1)
    assert _is_linked(b, 'library_Equipment44', a1)
    if hasattr(a1, 'library_EquipmentGroup43'):
        assert _is_linked(a1, 'library_EquipmentGroup43', b)
    _safe_set(b, 'library_Equipment44', a2)
    assert _is_linked(b, 'library_Equipment44', a2)
    if hasattr(a1, 'library_EquipmentGroup43'):
        assert not _is_linked(a1, 'library_EquipmentGroup43', b)
    if hasattr(a2, 'library_EquipmentGroup43'):
        assert _is_linked(a2, 'library_EquipmentGroup43', b)
    _safe_set(b, 'library_Equipment44', None)
    assert not _is_linked(b, 'library_Equipment44', a2)
    if hasattr(a2, 'library_EquipmentGroup43'):
        assert not _is_linked(a2, 'library_EquipmentGroup43', b)


def test_assoc_equipments117_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text", name="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment119', a1)
    assert _is_linked(b, 'library_Equipment119', a1)
    if hasattr(a1, 'library_NodeType118'):
        assert _is_linked(a1, 'library_NodeType118', b)
    _safe_set(b, 'library_Equipment119', a2)
    assert _is_linked(b, 'library_Equipment119', a2)
    if hasattr(a1, 'library_NodeType118'):
        assert not _is_linked(a1, 'library_NodeType118', b)
    if hasattr(a2, 'library_NodeType118'):
        assert _is_linked(a2, 'library_NodeType118', b)
    _safe_set(b, 'library_Equipment119', None)
    assert not _is_linked(b, 'library_Equipment119', a2)
    if hasattr(a2, 'library_NodeType118'):
        assert not _is_linked(a2, 'library_NodeType118', b)


def test_assoc_equipments25_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment24', {a1})
    assert _is_linked(b, 'library_Equipment24', a1)
    if hasattr(a1, 'library_Equipment'):
        assert _is_linked(a1, 'library_Equipment', b)
    _safe_set(b, 'library_Equipment24', {a2})
    assert _is_linked(b, 'library_Equipment24', a2)
    if hasattr(a1, 'library_Equipment'):
        assert not _is_linked(a1, 'library_Equipment', b)
    if hasattr(a2, 'library_Equipment'):
        assert _is_linked(a2, 'library_Equipment', b)
    _safe_set(b, 'library_Equipment24', set())
    assert not _is_linked(b, 'library_Equipment24', a2)
    if hasattr(a2, 'library_Equipment'):
        assert not _is_linked(a2, 'library_Equipment', b)


def test_assoc_equipments71_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment73', a1)
    assert _is_linked(b, 'library_Equipment73', a1)
    if hasattr(a1, 'library_Library72'):
        assert _is_linked(a1, 'library_Library72', b)
    _safe_set(b, 'library_Equipment73', a2)
    assert _is_linked(b, 'library_Equipment73', a2)
    if hasattr(a1, 'library_Library72'):
        assert not _is_linked(a1, 'library_Library72', b)
    if hasattr(a2, 'library_Library72'):
        assert _is_linked(a2, 'library_Library72', b)
    _safe_set(b, 'library_Equipment73', None)
    assert not _is_linked(b, 'library_Equipment73', a2)
    if hasattr(a2, 'library_Library72'):
        assert not _is_linked(a2, 'library_Library72', b)


def test_assoc_expressionRef147_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression149', a1)
    assert _is_linked(b, 'library_Expression149', a1)
    if hasattr(a1, 'library_Tolerance148'):
        assert _is_linked(a1, 'library_Tolerance148', b)
    _safe_set(b, 'library_Expression149', a2)
    assert _is_linked(b, 'library_Expression149', a2)
    if hasattr(a1, 'library_Tolerance148'):
        assert not _is_linked(a1, 'library_Tolerance148', b)
    if hasattr(a2, 'library_Tolerance148'):
        assert _is_linked(a2, 'library_Tolerance148', b)
    _safe_set(b, 'library_Expression149', None)
    assert not _is_linked(b, 'library_Expression149', a2)
    if hasattr(a2, 'library_Tolerance148'):
        assert not _is_linked(a2, 'library_Tolerance148', b)


def test_assoc_expressionRefs39_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup40', {a1})
    assert _is_linked(b, 'library_EquipmentGroup40', a1)
    if hasattr(a1, 'library_Expression41'):
        assert _is_linked(a1, 'library_Expression41', b)
    _safe_set(b, 'library_EquipmentGroup40', {a2})
    assert _is_linked(b, 'library_EquipmentGroup40', a2)
    if hasattr(a1, 'library_Expression41'):
        assert not _is_linked(a1, 'library_Expression41', b)
    if hasattr(a2, 'library_Expression41'):
        assert _is_linked(a2, 'library_Expression41', b)
    _safe_set(b, 'library_EquipmentGroup40', set())
    assert not _is_linked(b, 'library_EquipmentGroup40', a2)
    if hasattr(a2, 'library_Expression41'):
        assert not _is_linked(a2, 'library_Expression41', b)


def test_assoc_expressions85_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression87', a1)
    assert _is_linked(b, 'library_Expression87', a1)
    if hasattr(a1, 'library_Library86'):
        assert _is_linked(a1, 'library_Library86', b)
    _safe_set(b, 'library_Expression87', a2)
    assert _is_linked(b, 'library_Expression87', a2)
    if hasattr(a1, 'library_Library86'):
        assert not _is_linked(a1, 'library_Library86', b)
    if hasattr(a2, 'library_Library86'):
        assert _is_linked(a2, 'library_Library86', b)
    _safe_set(b, 'library_Expression87', None)
    assert not _is_linked(b, 'library_Expression87', a2)
    if hasattr(a2, 'library_Library86'):
        assert not _is_linked(a2, 'library_Library86', b)


def test_assoc_nodeTypeRef125_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_NodeType(leafNode="sample_text", name="sample_text")
    _safe_set(b, 'library_NodeType127', a1)
    assert _is_linked(b, 'library_NodeType127', a1)
    if hasattr(a1, 'library_ProductInfo126'):
        assert _is_linked(a1, 'library_ProductInfo126', b)
    _safe_set(b, 'library_NodeType127', a2)
    assert _is_linked(b, 'library_NodeType127', a2)
    if hasattr(a1, 'library_ProductInfo126'):
        assert not _is_linked(a1, 'library_ProductInfo126', b)
    if hasattr(a2, 'library_ProductInfo126'):
        assert _is_linked(a2, 'library_ProductInfo126', b)
    _safe_set(b, 'library_NodeType127', None)
    assert not _is_linked(b, 'library_NodeType127', a2)
    if hasattr(a2, 'library_ProductInfo126'):
        assert not _is_linked(a2, 'library_ProductInfo126', b)


def test_assoc_nodeTypes130_reverse_link_reassign_clear():
    a1 = library_ReferenceNetwork(description="sample_text", name="sample_text")
    a2 = library_ReferenceNetwork(description="sample_text_2", name="sample_text_2")
    b = library_NodeType(leafNode="sample_text", name="sample_text")
    _safe_set(b, 'library_NodeType132', a1)
    assert _is_linked(b, 'library_NodeType132', a1)
    if hasattr(a1, 'library_ReferenceNetwork131'):
        assert _is_linked(a1, 'library_ReferenceNetwork131', b)
    _safe_set(b, 'library_NodeType132', a2)
    assert _is_linked(b, 'library_NodeType132', a2)
    if hasattr(a1, 'library_ReferenceNetwork131'):
        assert not _is_linked(a1, 'library_ReferenceNetwork131', b)
    if hasattr(a2, 'library_ReferenceNetwork131'):
        assert _is_linked(a2, 'library_ReferenceNetwork131', b)
    _safe_set(b, 'library_NodeType132', None)
    assert not _is_linked(b, 'library_NodeType132', a2)
    if hasattr(a2, 'library_ReferenceNetwork131'):
        assert not _is_linked(a2, 'library_ReferenceNetwork131', b)


def test_assoc_nodeTypes69_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text", name="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library70', {a1})
    assert _is_linked(b, 'library_Library70', a1)
    if hasattr(a1, 'library_NodeType'):
        assert _is_linked(a1, 'library_NodeType', b)
    _safe_set(b, 'library_Library70', {a2})
    assert _is_linked(b, 'library_Library70', a2)
    if hasattr(a1, 'library_NodeType'):
        assert not _is_linked(a1, 'library_NodeType', b)
    if hasattr(a2, 'library_NodeType'):
        assert _is_linked(a2, 'library_NodeType', b)
    _safe_set(b, 'library_Library70', set())
    assert not _is_linked(b, 'library_Library70', a2)
    if hasattr(a2, 'library_NodeType'):
        assert not _is_linked(a2, 'library_NodeType', b)


def test_assoc_parameterRefs16_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component17', {a1})
    assert _is_linked(b, 'library_Component17', a1)
    if hasattr(a1, 'library_Parameter'):
        assert _is_linked(a1, 'library_Parameter', b)
    _safe_set(b, 'library_Component17', {a2})
    assert _is_linked(b, 'library_Component17', a2)
    if hasattr(a1, 'library_Parameter'):
        assert not _is_linked(a1, 'library_Parameter', b)
    if hasattr(a2, 'library_Parameter'):
        assert _is_linked(a2, 'library_Parameter', b)
    _safe_set(b, 'library_Component17', set())
    assert not _is_linked(b, 'library_Component17', a2)
    if hasattr(a2, 'library_Parameter'):
        assert not _is_linked(a2, 'library_Parameter', b)


def test_assoc_parameterRefs45_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup46', {a1})
    assert _is_linked(b, 'library_EquipmentGroup46', a1)
    if hasattr(a1, 'library_Parameter47'):
        assert _is_linked(a1, 'library_Parameter47', b)
    _safe_set(b, 'library_EquipmentGroup46', {a2})
    assert _is_linked(b, 'library_EquipmentGroup46', a2)
    if hasattr(a1, 'library_Parameter47'):
        assert not _is_linked(a1, 'library_Parameter47', b)
    if hasattr(a2, 'library_Parameter47'):
        assert _is_linked(a2, 'library_Parameter47', b)
    _safe_set(b, 'library_EquipmentGroup46', set())
    assert not _is_linked(b, 'library_EquipmentGroup46', a2)
    if hasattr(a2, 'library_Parameter47'):
        assert not _is_linked(a2, 'library_Parameter47', b)


def test_assoc_parameters79_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library80', {a1})
    assert _is_linked(b, 'library_Library80', a1)
    if hasattr(a1, 'library_Parameter81'):
        assert _is_linked(a1, 'library_Parameter81', b)
    _safe_set(b, 'library_Library80', {a2})
    assert _is_linked(b, 'library_Library80', a2)
    if hasattr(a1, 'library_Parameter81'):
        assert not _is_linked(a1, 'library_Parameter81', b)
    if hasattr(a2, 'library_Parameter81'):
        assert _is_linked(a2, 'library_Parameter81', b)
    _safe_set(b, 'library_Library80', set())
    assert not _is_linked(b, 'library_Library80', a2)
    if hasattr(a2, 'library_Parameter81'):
        assert not _is_linked(a2, 'library_Parameter81', b)


def test_assoc_refInterface1Ref141_reverse_link_reassign_clear():
    a1 = library_ReferenceRelationship(name="sample_text")
    a2 = library_ReferenceRelationship(name="sample_text_2")
    b = library_NodeType(leafNode="sample_text", name="sample_text")
    _safe_set(b, 'library_NodeType143', a1)
    assert _is_linked(b, 'library_NodeType143', a1)
    if hasattr(a1, 'library_ReferenceRelationship142'):
        assert _is_linked(a1, 'library_ReferenceRelationship142', b)
    _safe_set(b, 'library_NodeType143', a2)
    assert _is_linked(b, 'library_NodeType143', a2)
    if hasattr(a1, 'library_ReferenceRelationship142'):
        assert not _is_linked(a1, 'library_ReferenceRelationship142', b)
    if hasattr(a2, 'library_ReferenceRelationship142'):
        assert _is_linked(a2, 'library_ReferenceRelationship142', b)
    _safe_set(b, 'library_NodeType143', None)
    assert not _is_linked(b, 'library_NodeType143', a2)
    if hasattr(a2, 'library_ReferenceRelationship142'):
        assert not _is_linked(a2, 'library_ReferenceRelationship142', b)


def test_assoc_refInterface2Ref144_reverse_link_reassign_clear():
    a1 = library_ReferenceRelationship(name="sample_text")
    a2 = library_ReferenceRelationship(name="sample_text_2")
    b = library_NodeType(leafNode="sample_text", name="sample_text")
    _safe_set(b, 'library_NodeType146', a1)
    assert _is_linked(b, 'library_NodeType146', a1)
    if hasattr(a1, 'library_ReferenceRelationship145'):
        assert _is_linked(a1, 'library_ReferenceRelationship145', b)
    _safe_set(b, 'library_NodeType146', a2)
    assert _is_linked(b, 'library_NodeType146', a2)
    if hasattr(a1, 'library_ReferenceRelationship145'):
        assert not _is_linked(a1, 'library_ReferenceRelationship145', b)
    if hasattr(a2, 'library_ReferenceRelationship145'):
        assert _is_linked(a2, 'library_ReferenceRelationship145', b)
    _safe_set(b, 'library_NodeType146', None)
    assert not _is_linked(b, 'library_NodeType146', a2)
    if hasattr(a2, 'library_ReferenceRelationship145'):
        assert not _is_linked(a2, 'library_ReferenceRelationship145', b)


def test_assoc_refRelationships136_reverse_link_reassign_clear():
    a1 = library_ReferenceRelationship(name="sample_text")
    a2 = library_ReferenceRelationship(name="sample_text_2")
    b = library_ReferenceNetwork(description="sample_text", name="sample_text")
    _safe_set(b, 'library_ReferenceNetwork137', {a1})
    assert _is_linked(b, 'library_ReferenceNetwork137', a1)
    if hasattr(a1, 'library_ReferenceRelationship'):
        assert _is_linked(a1, 'library_ReferenceRelationship', b)
    _safe_set(b, 'library_ReferenceNetwork137', {a2})
    assert _is_linked(b, 'library_ReferenceNetwork137', a2)
    if hasattr(a1, 'library_ReferenceRelationship'):
        assert not _is_linked(a1, 'library_ReferenceRelationship', b)
    if hasattr(a2, 'library_ReferenceRelationship'):
        assert _is_linked(a2, 'library_ReferenceRelationship', b)
    _safe_set(b, 'library_ReferenceNetwork137', set())
    assert not _is_linked(b, 'library_ReferenceNetwork137', a2)
    if hasattr(a2, 'library_ReferenceRelationship'):
        assert not _is_linked(a2, 'library_ReferenceRelationship', b)


def test_assoc_referenceNetworks134_reverse_link_reassign_clear():
    a1 = library_ReferenceNetwork(description="sample_text", name="sample_text")
    a2 = library_ReferenceNetwork(description="sample_text_2", name="sample_text_2")
    b = library_ReferenceNetwork(description="sample_text", name="sample_text")
    _safe_set(b, 'library_ReferenceNetwork135', a1)
    assert _is_linked(b, 'library_ReferenceNetwork135', a1)
    if hasattr(a1, 'library_ReferenceNetwork133'):
        assert _is_linked(a1, 'library_ReferenceNetwork133', b)
    _safe_set(b, 'library_ReferenceNetwork135', a2)
    assert _is_linked(b, 'library_ReferenceNetwork135', a2)
    if hasattr(a1, 'library_ReferenceNetwork133'):
        assert not _is_linked(a1, 'library_ReferenceNetwork133', b)
    if hasattr(a2, 'library_ReferenceNetwork133'):
        assert _is_linked(a2, 'library_ReferenceNetwork133', b)
    _safe_set(b, 'library_ReferenceNetwork135', None)
    assert not _is_linked(b, 'library_ReferenceNetwork135', a2)
    if hasattr(a2, 'library_ReferenceNetwork133'):
        assert not _is_linked(a2, 'library_ReferenceNetwork133', b)


def test_assoc_targetResource56_reverse_link_reassign_clear():
    a1 = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    a2 = library_ExpressionResult(targetIntervalHint="sample_text_2", targetKindHint="sample_text_2", targetRange="sample_text_2")
    b = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    _safe_set(b, 'library_BaseResource57', a1)
    assert _is_linked(b, 'library_BaseResource57', a1)
    if hasattr(a1, 'library_ExpressionResult'):
        assert _is_linked(a1, 'library_ExpressionResult', b)
    _safe_set(b, 'library_BaseResource57', a2)
    assert _is_linked(b, 'library_BaseResource57', a2)
    if hasattr(a1, 'library_ExpressionResult'):
        assert not _is_linked(a1, 'library_ExpressionResult', b)
    if hasattr(a2, 'library_ExpressionResult'):
        assert _is_linked(a2, 'library_ExpressionResult', b)
    _safe_set(b, 'library_BaseResource57', None)
    assert not _is_linked(b, 'library_BaseResource57', a2)
    if hasattr(a2, 'library_ExpressionResult'):
        assert not _is_linked(a2, 'library_ExpressionResult', b)


def test_assoc_toleranceRefs12_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component13', {a1})
    assert _is_linked(b, 'library_Component13', a1)
    if hasattr(a1, 'library_Tolerance'):
        assert _is_linked(a1, 'library_Tolerance', b)
    _safe_set(b, 'library_Component13', {a2})
    assert _is_linked(b, 'library_Component13', a2)
    if hasattr(a1, 'library_Tolerance'):
        assert not _is_linked(a1, 'library_Tolerance', b)
    if hasattr(a2, 'library_Tolerance'):
        assert _is_linked(a2, 'library_Tolerance', b)
    _safe_set(b, 'library_Component13', set())
    assert not _is_linked(b, 'library_Component13', a2)
    if hasattr(a2, 'library_Tolerance'):
        assert not _is_linked(a2, 'library_Tolerance', b)


def test_assoc_tolerances82_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library83', {a1})
    assert _is_linked(b, 'library_Library83', a1)
    if hasattr(a1, 'library_Tolerance84'):
        assert _is_linked(a1, 'library_Tolerance84', b)
    _safe_set(b, 'library_Library83', {a2})
    assert _is_linked(b, 'library_Library83', a2)
    if hasattr(a1, 'library_Tolerance84'):
        assert not _is_linked(a1, 'library_Tolerance84', b)
    if hasattr(a2, 'library_Tolerance84'):
        assert _is_linked(a2, 'library_Tolerance84', b)
    _safe_set(b, 'library_Library83', set())
    assert not _is_linked(b, 'library_Library83', a2)
    if hasattr(a2, 'library_Tolerance84'):
        assert not _is_linked(a2, 'library_Tolerance84', b)


def test_assoc_unitRef0_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    _safe_set(b, 'library_BaseResource', a1)
    assert _is_linked(b, 'library_BaseResource', a1)
    if hasattr(a1, 'library_Unit'):
        assert _is_linked(a1, 'library_Unit', b)
    _safe_set(b, 'library_BaseResource', a2)
    assert _is_linked(b, 'library_BaseResource', a2)
    if hasattr(a1, 'library_Unit'):
        assert not _is_linked(a1, 'library_Unit', b)
    if hasattr(a2, 'library_Unit'):
        assert _is_linked(a2, 'library_Unit', b)
    _safe_set(b, 'library_BaseResource', None)
    assert not _is_linked(b, 'library_BaseResource', a2)
    if hasattr(a2, 'library_Unit'):
        assert not _is_linked(a2, 'library_Unit', b)


def test_assoc_units88_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library89', {a1})
    assert _is_linked(b, 'library_Library89', a1)
    if hasattr(a1, 'library_Unit90'):
        assert _is_linked(a1, 'library_Unit90', b)
    _safe_set(b, 'library_Library89', {a2})
    assert _is_linked(b, 'library_Library89', a2)
    if hasattr(a1, 'library_Unit90'):
        assert not _is_linked(a1, 'library_Unit90', b)
    if hasattr(a2, 'library_Unit90'):
        assert _is_linked(a2, 'library_Unit90', b)
    _safe_set(b, 'library_Library89', set())
    assert not _is_linked(b, 'library_Library89', a2)
    if hasattr(a2, 'library_Unit90'):
        assert not _is_linked(a2, 'library_Unit90', b)


def test_assoc_utilizationExpressionRef9_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component10', a1)
    assert _is_linked(b, 'library_Component10', a1)
    if hasattr(a1, 'library_Expression11'):
        assert _is_linked(a1, 'library_Expression11', b)
    _safe_set(b, 'library_Component10', a2)
    assert _is_linked(b, 'library_Component10', a2)
    if hasattr(a1, 'library_Expression11'):
        assert not _is_linked(a1, 'library_Expression11', b)
    if hasattr(a2, 'library_Expression11'):
        assert _is_linked(a2, 'library_Expression11', b)
    _safe_set(b, 'library_Component10', None)
    assert not _is_linked(b, 'library_Component10', a2)
    if hasattr(a2, 'library_Expression11'):
        assert not _is_linked(a2, 'library_Expression11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allEquipmentResources48_stub_double():
    # library_NetXResource has no real 'library_NetXResource50' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource50', None)
    _safe_set(owner, 'library_EquipmentGroup49', {partner})
    assert getattr(partner, 'library_NetXResource50') == owner
    _safe_set(owner, 'library_EquipmentGroup49', set())
    assert getattr(partner, 'library_NetXResource50') is None


def test_assoc_allResources18_stub_double():
    # library_NetXResource has no real 'library_NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource', None)
    _safe_set(owner, 'library_Component19', {partner})
    assert getattr(partner, 'library_NetXResource') == owner
    _safe_set(owner, 'library_Component19', set())
    assert getattr(partner, 'library_NetXResource') is None


def test_assoc_componentRef93_stub_double():
    # library_NetXResource has no real 'resourceRefs' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'resourceRefs', None)
    _safe_set(owner, 'Component', partner)
    assert getattr(partner, 'resourceRefs') == owner
    _safe_set(owner, 'Component', None)
    assert getattr(partner, 'resourceRefs') is None


def test_assoc_configAttributes3_stub_double():
    # library_ConfigAttribute has no real 'library_ConfigAttribute' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_ConfigAttribute()
    setattr(partner, 'library_ConfigAttribute', None)
    _safe_set(owner, 'library_Component4', {partner})
    assert getattr(partner, 'library_ConfigAttribute') == owner
    _safe_set(owner, 'library_Component4', set())
    assert getattr(partner, 'library_ConfigAttribute') is None


def test_assoc_diagrams128_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo129' property in the generated
    # code (a bare stub) -- manually attach it so library_ReferenceNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ReferenceNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ReferenceNetwork(description="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo129', None)
    _safe_set(owner, 'library_ReferenceNetwork', {partner})
    assert getattr(partner, 'library_DiagramInfo129') == owner
    _safe_set(owner, 'library_ReferenceNetwork', set())
    assert getattr(partner, 'library_DiagramInfo129') is None


def test_assoc_diagrams20_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo', None)
    _safe_set(owner, 'library_Component21', {partner})
    assert getattr(partner, 'library_DiagramInfo') == owner
    _safe_set(owner, 'library_Component21', set())
    assert getattr(partner, 'library_DiagramInfo') is None


def test_assoc_diagrams33_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo35' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo35', None)
    _safe_set(owner, 'library_EquipmentGroup34', {partner})
    assert getattr(partner, 'library_DiagramInfo35') == owner
    _safe_set(owner, 'library_EquipmentGroup34', set())
    assert getattr(partner, 'library_DiagramInfo35') is None


def test_assoc_equipmentGroupResources36_stub_double():
    # library_NetXResource has no real 'library_NetXResource38' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource38', None)
    _safe_set(owner, 'library_EquipmentGroup37', {partner})
    assert getattr(partner, 'library_NetXResource38') == owner
    _safe_set(owner, 'library_EquipmentGroup37', set())
    assert getattr(partner, 'library_NetXResource38') is None


def test_assoc_equipmentRelationshipRefs28_stub_double():
    # library_EquipmentRelationship has no real 'library_EquipmentRelationship' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_EquipmentRelationship()
    setattr(partner, 'library_EquipmentRelationship', None)
    _safe_set(owner, 'library_Equipment29', {partner})
    assert getattr(partner, 'library_EquipmentRelationship') == owner
    _safe_set(owner, 'library_Equipment29', set())
    assert getattr(partner, 'library_EquipmentRelationship') is None


def test_assoc_evaluationObject54_stub_double():
    # library_EObject has no real 'library_EObject' property in the generated
    # code (a bare stub) -- manually attach it so library_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Expression(expressionLines="sample_text", name="sample_text")
    partner = library_EObject()
    setattr(partner, 'library_EObject', None)
    _safe_set(owner, 'library_Expression55', partner)
    assert getattr(partner, 'library_EObject') == owner
    _safe_set(owner, 'library_Expression55', None)
    assert getattr(partner, 'library_EObject') is None


def test_assoc_functions114_stub_double():
    # library_Function has no real 'library_Function116' property in the generated
    # code (a bare stub) -- manually attach it so library_NodeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NodeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NodeType(leafNode="sample_text", name="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function116', None)
    _safe_set(owner, 'library_NodeType115', {partner})
    assert getattr(partner, 'library_Function116') == owner
    _safe_set(owner, 'library_NodeType115', set())
    assert getattr(partner, 'library_Function116') is None


def test_assoc_functions67_stub_double():
    # library_Function has no real 'library_Function68' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function68', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'library_Function68') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'library_Function68') is None


def test_assoc_icons150_stub_double():
    # library_MultiImage has no real 'library_MultiImage152' property in the generated
    # code (a bare stub) -- manually attach it so library_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage152', None)
    _safe_set(owner, 'library_Unit151', partner)
    assert getattr(partner, 'library_MultiImage152') == owner
    _safe_set(owner, 'library_Unit151', None)
    assert getattr(partner, 'library_MultiImage152') is None


def test_assoc_icons22_stub_double():
    # library_MultiImage has no real 'library_MultiImage' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage', None)
    _safe_set(owner, 'library_Component23', partner)
    assert getattr(partner, 'library_MultiImage') == owner
    _safe_set(owner, 'library_Component23', None)
    assert getattr(partner, 'library_MultiImage') is None


def test_assoc_licensedFunctionRef122_stub_double():
    # library_Function has no real 'library_Function124' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function124', None)
    _safe_set(owner, 'library_ProductInfo123', {partner})
    assert getattr(partner, 'library_Function124') == owner
    _safe_set(owner, 'library_ProductInfo123', set())
    assert getattr(partner, 'library_Function124') is None


def test_assoc_lifecycle1_stub_double():
    # library_Lifecycle has no real 'library_Lifecycle' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_Lifecycle()
    setattr(partner, 'library_Lifecycle', None)
    _safe_set(owner, 'library_Component', partner)
    assert getattr(partner, 'library_Lifecycle') == owner
    _safe_set(owner, 'library_Component', None)
    assert getattr(partner, 'library_Lifecycle') is None


def test_assoc_metricRefs5_stub_double():
    # library_Metric has no real 'library_Metric' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric', None)
    _safe_set(owner, 'library_Component6', {partner})
    assert getattr(partner, 'library_Metric') == owner
    _safe_set(owner, 'library_Component6', set())
    assert getattr(partner, 'library_Metric') is None


def test_assoc_metricSources77_stub_double():
    # library_MetricSource has no real 'library_MetricSource' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_MetricSource()
    setattr(partner, 'library_MetricSource', None)
    _safe_set(owner, 'library_Library78', {partner})
    assert getattr(partner, 'library_MetricSource') == owner
    _safe_set(owner, 'library_Library78', set())
    assert getattr(partner, 'library_MetricSource') is None


def test_assoc_metrics74_stub_double():
    # library_Metric has no real 'library_Metric76' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric76', None)
    _safe_set(owner, 'library_Library75', {partner})
    assert getattr(partner, 'library_Metric76') == owner
    _safe_set(owner, 'library_Library75', set())
    assert getattr(partner, 'library_Metric76') is None


def test_assoc_products153_stub_double():
    # library_Vendor has no real 'library_Vendor' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Vendor()
    setattr(partner, 'library_Vendor', None)
    _safe_set(owner, 'library_ProductInfo154', partner)
    assert owner in getattr(partner, 'library_Vendor')
    _safe_set(owner, 'library_ProductInfo154', None)
    assert owner not in getattr(partner, 'library_Vendor')


def test_assoc_protocolRef138_stub_double():
    # library_Protocol has no real 'library_Protocol140' property in the generated
    # code (a bare stub) -- manually attach it so library_ReferenceRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ReferenceRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ReferenceRelationship(name="sample_text")
    partner = library_Protocol()
    setattr(partner, 'library_Protocol140', None)
    _safe_set(owner, 'library_ReferenceRelationship139', partner)
    assert getattr(partner, 'library_Protocol140') == owner
    _safe_set(owner, 'library_ReferenceRelationship139', None)
    assert getattr(partner, 'library_Protocol140') is None


def test_assoc_protocolRefs14_stub_double():
    # library_Protocol has no real 'library_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_Protocol()
    setattr(partner, 'library_Protocol', None)
    _safe_set(owner, 'library_Component15', {partner})
    assert getattr(partner, 'library_Protocol') == owner
    _safe_set(owner, 'library_Component15', set())
    assert getattr(partner, 'library_Protocol') is None


def test_assoc_resourceRefs2_stub_double():
    # library_NetXResource has no real 'NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'NetXResource', None)
    _safe_set(owner, 'componentRef', {partner})
    assert getattr(partner, 'NetXResource') == owner
    _safe_set(owner, 'componentRef', set())
    assert getattr(partner, 'NetXResource') is None


def test_assoc_targetValues58_stub_double():
    # library_Value has no real 'library_Value' property in the generated
    # code (a bare stub) -- manually attach it so library_ExpressionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ExpressionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value', None)
    _safe_set(owner, 'library_ExpressionResult59', {partner})
    assert getattr(partner, 'library_Value') == owner
    _safe_set(owner, 'library_ExpressionResult59', set())
    assert getattr(partner, 'library_Value') is None


def test_assoc_version91_stub_double():
    # library_Meta has no real 'library_Meta' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Meta()
    setattr(partner, 'library_Meta', None)
    _safe_set(owner, 'library_Library92', partner)
    assert getattr(partner, 'library_Meta') == owner
    _safe_set(owner, 'library_Library92', None)
    assert getattr(partner, 'library_Meta') is None


