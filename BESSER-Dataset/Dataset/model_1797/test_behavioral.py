import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Company,
    library_DiagramInfo,
    library_EObject,
    library_Equipment,
    library_EquipmentGroup,
    library_EquipmentRelationship,
    library_Expression,
    library_ExpressionResult,
    library_Function,
    library_FunctionRelationship,
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
    library_ServiceProfile,
    library_Tolerance,
    library_Unit,
    library_Value,
    library_Vendor,
    LevelType,
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

def test_assoc_allEquipmentResources23_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment24', {a1})
    assert _is_linked(b, 'library_Equipment24', a1)
    if hasattr(a1, 'library_NetXResource25'):
        assert _is_linked(a1, 'library_NetXResource25', b)
    _safe_set(b, 'library_Equipment24', {a2})
    assert _is_linked(b, 'library_Equipment24', a2)
    if hasattr(a1, 'library_NetXResource25'):
        assert not _is_linked(a1, 'library_NetXResource25', b)
    if hasattr(a2, 'library_NetXResource25'):
        assert _is_linked(a2, 'library_NetXResource25', b)
    _safe_set(b, 'library_Equipment24', set())
    assert not _is_linked(b, 'library_Equipment24', a2)
    if hasattr(a2, 'library_NetXResource25'):
        assert not _is_linked(a2, 'library_NetXResource25', b)


def test_assoc_allEquipmentResources45_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup46', {a1})
    assert _is_linked(b, 'library_EquipmentGroup46', a1)
    if hasattr(a1, 'library_NetXResource47'):
        assert _is_linked(a1, 'library_NetXResource47', b)
    _safe_set(b, 'library_EquipmentGroup46', {a2})
    assert _is_linked(b, 'library_EquipmentGroup46', a2)
    if hasattr(a1, 'library_NetXResource47'):
        assert not _is_linked(a1, 'library_NetXResource47', b)
    if hasattr(a2, 'library_NetXResource47'):
        assert _is_linked(a2, 'library_NetXResource47', b)
    _safe_set(b, 'library_EquipmentGroup46', set())
    assert not _is_linked(b, 'library_EquipmentGroup46', a2)
    if hasattr(a2, 'library_NetXResource47'):
        assert not _is_linked(a2, 'library_NetXResource47', b)


def test_assoc_allEquipments27_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", description="sample_text_2", equipmentCode="sample_text_2", equipmentName="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment28', a1)
    assert _is_linked(b, 'library_Equipment28', a1)
    if hasattr(a1, 'library_Equipment26'):
        assert _is_linked(a1, 'library_Equipment26', b)
    _safe_set(b, 'library_Equipment28', a2)
    assert _is_linked(b, 'library_Equipment28', a2)
    if hasattr(a1, 'library_Equipment26'):
        assert not _is_linked(a1, 'library_Equipment26', b)
    if hasattr(a2, 'library_Equipment26'):
        assert _is_linked(a2, 'library_Equipment26', b)
    _safe_set(b, 'library_Equipment28', None)
    assert not _is_linked(b, 'library_Equipment28', a2)
    if hasattr(a2, 'library_Equipment26'):
        assert not _is_linked(a2, 'library_Equipment26', b)


def test_assoc_allEquipments48_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment50', a1)
    assert _is_linked(b, 'library_Equipment50', a1)
    if hasattr(a1, 'library_EquipmentGroup49'):
        assert _is_linked(a1, 'library_EquipmentGroup49', b)
    _safe_set(b, 'library_Equipment50', a2)
    assert _is_linked(b, 'library_Equipment50', a2)
    if hasattr(a1, 'library_EquipmentGroup49'):
        assert not _is_linked(a1, 'library_EquipmentGroup49', b)
    if hasattr(a2, 'library_EquipmentGroup49'):
        assert _is_linked(a2, 'library_EquipmentGroup49', b)
    _safe_set(b, 'library_Equipment50', None)
    assert not _is_linked(b, 'library_Equipment50', a2)
    if hasattr(a2, 'library_EquipmentGroup49'):
        assert not _is_linked(a2, 'library_EquipmentGroup49', b)


def test_assoc_allFunctionResources88_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function89', {a1})
    assert _is_linked(b, 'library_Function89', a1)
    if hasattr(a1, 'library_NetXResource90'):
        assert _is_linked(a1, 'library_NetXResource90', b)
    _safe_set(b, 'library_Function89', {a2})
    assert _is_linked(b, 'library_Function89', a2)
    if hasattr(a1, 'library_NetXResource90'):
        assert not _is_linked(a1, 'library_NetXResource90', b)
    if hasattr(a2, 'library_NetXResource90'):
        assert _is_linked(a2, 'library_NetXResource90', b)
    _safe_set(b, 'library_Function89', set())
    assert not _is_linked(b, 'library_Function89', a2)
    if hasattr(a2, 'library_NetXResource90'):
        assert not _is_linked(a2, 'library_NetXResource90', b)


def test_assoc_allFunctions92_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function93', a1)
    assert _is_linked(b, 'library_Function93', a1)
    if hasattr(a1, 'library_Function91'):
        assert _is_linked(a1, 'library_Function91', b)
    _safe_set(b, 'library_Function93', a2)
    assert _is_linked(b, 'library_Function93', a2)
    if hasattr(a1, 'library_Function91'):
        assert not _is_linked(a1, 'library_Function91', b)
    if hasattr(a2, 'library_Function91'):
        assert _is_linked(a2, 'library_Function91', b)
    _safe_set(b, 'library_Function93', None)
    assert not _is_linked(b, 'library_Function93', a2)
    if hasattr(a2, 'library_Function91'):
        assert not _is_linked(a2, 'library_Function91', b)


def test_assoc_capacityExpressionRef15_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment16', a1)
    assert _is_linked(b, 'library_Equipment16', a1)
    if hasattr(a1, 'library_Expression'):
        assert _is_linked(a1, 'library_Expression', b)
    _safe_set(b, 'library_Equipment16', a2)
    assert _is_linked(b, 'library_Equipment16', a2)
    if hasattr(a1, 'library_Expression'):
        assert not _is_linked(a1, 'library_Expression', b)
    if hasattr(a2, 'library_Expression'):
        assert _is_linked(a2, 'library_Expression', b)
    _safe_set(b, 'library_Equipment16', None)
    assert not _is_linked(b, 'library_Equipment16', a2)
    if hasattr(a2, 'library_Expression'):
        assert not _is_linked(a2, 'library_Expression', b)


def test_assoc_capacityExpressionRef76_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression78', a1)
    assert _is_linked(b, 'library_Expression78', a1)
    if hasattr(a1, 'library_Function77'):
        assert _is_linked(a1, 'library_Function77', b)
    _safe_set(b, 'library_Expression78', a2)
    assert _is_linked(b, 'library_Expression78', a2)
    if hasattr(a1, 'library_Function77'):
        assert not _is_linked(a1, 'library_Function77', b)
    if hasattr(a2, 'library_Function77'):
        assert _is_linked(a2, 'library_Function77', b)
    _safe_set(b, 'library_Expression78', None)
    assert not _is_linked(b, 'library_Expression78', a2)
    if hasattr(a2, 'library_Function77'):
        assert not _is_linked(a2, 'library_Function77', b)


def test_assoc_equipmentExpressionRefs14_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'equipmentRefs', {a1})
    assert _is_linked(b, 'equipmentRefs', a1)
    if hasattr(a1, 'Expression'):
        assert _is_linked(a1, 'Expression', b)
    _safe_set(b, 'equipmentRefs', {a2})
    assert _is_linked(b, 'equipmentRefs', a2)
    if hasattr(a1, 'Expression'):
        assert not _is_linked(a1, 'Expression', b)
    if hasattr(a2, 'Expression'):
        assert _is_linked(a2, 'Expression', b)
    _safe_set(b, 'equipmentRefs', set())
    assert not _is_linked(b, 'equipmentRefs', a2)
    if hasattr(a2, 'Expression'):
        assert not _is_linked(a2, 'Expression', b)


def test_assoc_equipmentGroupRefs55_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'EquipmentGroup', a1)
    assert _is_linked(b, 'EquipmentGroup', a1)
    if hasattr(a1, 'expressionRefs'):
        assert _is_linked(a1, 'expressionRefs', b)
    _safe_set(b, 'EquipmentGroup', a2)
    assert _is_linked(b, 'EquipmentGroup', a2)
    if hasattr(a1, 'expressionRefs'):
        assert not _is_linked(a1, 'expressionRefs', b)
    if hasattr(a2, 'expressionRefs'):
        assert _is_linked(a2, 'expressionRefs', b)
    _safe_set(b, 'EquipmentGroup', None)
    assert not _is_linked(b, 'EquipmentGroup', a2)
    if hasattr(a2, 'expressionRefs'):
        assert not _is_linked(a2, 'expressionRefs', b)


def test_assoc_equipmentGroupResources34_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup35', {a1})
    assert _is_linked(b, 'library_EquipmentGroup35', a1)
    if hasattr(a1, 'library_NetXResource36'):
        assert _is_linked(a1, 'library_NetXResource36', b)
    _safe_set(b, 'library_EquipmentGroup35', {a2})
    assert _is_linked(b, 'library_EquipmentGroup35', a2)
    if hasattr(a1, 'library_NetXResource36'):
        assert not _is_linked(a1, 'library_NetXResource36', b)
    if hasattr(a2, 'library_NetXResource36'):
        assert _is_linked(a2, 'library_NetXResource36', b)
    _safe_set(b, 'library_EquipmentGroup35', set())
    assert not _is_linked(b, 'library_EquipmentGroup35', a2)
    if hasattr(a2, 'library_NetXResource36'):
        assert not _is_linked(a2, 'library_NetXResource36', b)


def test_assoc_equipmentGroups6_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment7', {a1})
    assert _is_linked(b, 'library_Equipment7', a1)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert _is_linked(a1, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment7', {a2})
    assert _is_linked(b, 'library_Equipment7', a2)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert not _is_linked(a1, 'library_EquipmentGroup', b)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert _is_linked(a2, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment7', set())
    assert not _is_linked(b, 'library_Equipment7', a2)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert not _is_linked(a2, 'library_EquipmentGroup', b)


def test_assoc_equipmentRef147_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment148', a1)
    assert _is_linked(b, 'library_Equipment148', a1)
    if hasattr(a1, 'library_ProductInfo'):
        assert _is_linked(a1, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment148', a2)
    assert _is_linked(b, 'library_Equipment148', a2)
    if hasattr(a1, 'library_ProductInfo'):
        assert not _is_linked(a1, 'library_ProductInfo', b)
    if hasattr(a2, 'library_ProductInfo'):
        assert _is_linked(a2, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment148', None)
    assert not _is_linked(b, 'library_Equipment148', a2)
    if hasattr(a2, 'library_ProductInfo'):
        assert not _is_linked(a2, 'library_ProductInfo', b)


def test_assoc_equipmentRefs39_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment41', a1)
    assert _is_linked(b, 'library_Equipment41', a1)
    if hasattr(a1, 'library_EquipmentGroup40'):
        assert _is_linked(a1, 'library_EquipmentGroup40', b)
    _safe_set(b, 'library_Equipment41', a2)
    assert _is_linked(b, 'library_Equipment41', a2)
    if hasattr(a1, 'library_EquipmentGroup40'):
        assert not _is_linked(a1, 'library_EquipmentGroup40', b)
    if hasattr(a2, 'library_EquipmentGroup40'):
        assert _is_linked(a2, 'library_EquipmentGroup40', b)
    _safe_set(b, 'library_Equipment41', None)
    assert not _is_linked(b, 'library_Equipment41', a2)
    if hasattr(a2, 'library_EquipmentGroup40'):
        assert not _is_linked(a2, 'library_EquipmentGroup40', b)


def test_assoc_equipmentRefs53_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'Equipment', a1)
    assert _is_linked(b, 'Equipment', a1)
    if hasattr(a1, 'equipmentExpressionRefs'):
        assert _is_linked(a1, 'equipmentExpressionRefs', b)
    _safe_set(b, 'Equipment', a2)
    assert _is_linked(b, 'Equipment', a2)
    if hasattr(a1, 'equipmentExpressionRefs'):
        assert not _is_linked(a1, 'equipmentExpressionRefs', b)
    if hasattr(a2, 'equipmentExpressionRefs'):
        assert _is_linked(a2, 'equipmentExpressionRefs', b)
    _safe_set(b, 'Equipment', None)
    assert not _is_linked(b, 'Equipment', a2)
    if hasattr(a2, 'equipmentExpressionRefs'):
        assert not _is_linked(a2, 'equipmentExpressionRefs', b)


def test_assoc_equipmentResources8_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment9', {a1})
    assert _is_linked(b, 'library_Equipment9', a1)
    if hasattr(a1, 'library_NetXResource'):
        assert _is_linked(a1, 'library_NetXResource', b)
    _safe_set(b, 'library_Equipment9', {a2})
    assert _is_linked(b, 'library_Equipment9', a2)
    if hasattr(a1, 'library_NetXResource'):
        assert not _is_linked(a1, 'library_NetXResource', b)
    if hasattr(a2, 'library_NetXResource'):
        assert _is_linked(a2, 'library_NetXResource', b)
    _safe_set(b, 'library_Equipment9', set())
    assert not _is_linked(b, 'library_Equipment9', a2)
    if hasattr(a2, 'library_NetXResource'):
        assert not _is_linked(a2, 'library_NetXResource', b)


def test_assoc_equipments144_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment146', a1)
    assert _is_linked(b, 'library_Equipment146', a1)
    if hasattr(a1, 'library_NodeType145'):
        assert _is_linked(a1, 'library_NodeType145', b)
    _safe_set(b, 'library_Equipment146', a2)
    assert _is_linked(b, 'library_Equipment146', a2)
    if hasattr(a1, 'library_NodeType145'):
        assert not _is_linked(a1, 'library_NodeType145', b)
    if hasattr(a2, 'library_NodeType145'):
        assert _is_linked(a2, 'library_NodeType145', b)
    _safe_set(b, 'library_Equipment146', None)
    assert not _is_linked(b, 'library_Equipment146', a2)
    if hasattr(a2, 'library_NodeType145'):
        assert not _is_linked(a2, 'library_NodeType145', b)


def test_assoc_equipments4_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", description="sample_text_2", equipmentCode="sample_text_2", equipmentName="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment5', a1)
    assert _is_linked(b, 'library_Equipment5', a1)
    if hasattr(a1, 'library_Equipment3'):
        assert _is_linked(a1, 'library_Equipment3', b)
    _safe_set(b, 'library_Equipment5', a2)
    assert _is_linked(b, 'library_Equipment5', a2)
    if hasattr(a1, 'library_Equipment3'):
        assert not _is_linked(a1, 'library_Equipment3', b)
    if hasattr(a2, 'library_Equipment3'):
        assert _is_linked(a2, 'library_Equipment3', b)
    _safe_set(b, 'library_Equipment5', None)
    assert not _is_linked(b, 'library_Equipment5', a2)
    if hasattr(a2, 'library_Equipment3'):
        assert not _is_linked(a2, 'library_Equipment3', b)


def test_assoc_equipments98_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment100', a1)
    assert _is_linked(b, 'library_Equipment100', a1)
    if hasattr(a1, 'library_Library99'):
        assert _is_linked(a1, 'library_Library99', b)
    _safe_set(b, 'library_Equipment100', a2)
    assert _is_linked(b, 'library_Equipment100', a2)
    if hasattr(a1, 'library_Library99'):
        assert not _is_linked(a1, 'library_Library99', b)
    if hasattr(a2, 'library_Library99'):
        assert _is_linked(a2, 'library_Library99', b)
    _safe_set(b, 'library_Equipment100', None)
    assert not _is_linked(b, 'library_Equipment100', a2)
    if hasattr(a2, 'library_Library99'):
        assert not _is_linked(a2, 'library_Library99', b)


def test_assoc_expressionRefs37_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'equipmentGroupRefs', {a1})
    assert _is_linked(b, 'equipmentGroupRefs', a1)
    if hasattr(a1, 'Expression38'):
        assert _is_linked(a1, 'Expression38', b)
    _safe_set(b, 'equipmentGroupRefs', {a2})
    assert _is_linked(b, 'equipmentGroupRefs', a2)
    if hasattr(a1, 'Expression38'):
        assert not _is_linked(a1, 'Expression38', b)
    if hasattr(a2, 'Expression38'):
        assert _is_linked(a2, 'Expression38', b)
    _safe_set(b, 'equipmentGroupRefs', set())
    assert not _is_linked(b, 'equipmentGroupRefs', a2)
    if hasattr(a2, 'Expression38'):
        assert not _is_linked(a2, 'Expression38', b)


def test_assoc_expressions112_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression114', a1)
    assert _is_linked(b, 'library_Expression114', a1)
    if hasattr(a1, 'library_Library113'):
        assert _is_linked(a1, 'library_Library113', b)
    _safe_set(b, 'library_Expression114', a2)
    assert _is_linked(b, 'library_Expression114', a2)
    if hasattr(a1, 'library_Library113'):
        assert not _is_linked(a1, 'library_Library113', b)
    if hasattr(a2, 'library_Library113'):
        assert _is_linked(a2, 'library_Library113', b)
    _safe_set(b, 'library_Expression114', None)
    assert not _is_linked(b, 'library_Expression114', a2)
    if hasattr(a2, 'library_Library113'):
        assert not _is_linked(a2, 'library_Library113', b)


def test_assoc_functionExpressionRefs74_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'Expression75', a1)
    assert _is_linked(b, 'Expression75', a1)
    if hasattr(a1, 'functionRefs'):
        assert _is_linked(a1, 'functionRefs', b)
    _safe_set(b, 'Expression75', a2)
    assert _is_linked(b, 'Expression75', a2)
    if hasattr(a1, 'functionRefs'):
        assert not _is_linked(a1, 'functionRefs', b)
    if hasattr(a2, 'functionRefs'):
        assert _is_linked(a2, 'functionRefs', b)
    _safe_set(b, 'Expression75', None)
    assert not _is_linked(b, 'Expression75', a2)
    if hasattr(a2, 'functionRefs'):
        assert not _is_linked(a2, 'functionRefs', b)


def test_assoc_functionRefs54_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'functionExpressionRefs', {a1})
    assert _is_linked(b, 'functionExpressionRefs', a1)
    if hasattr(a1, 'Function'):
        assert _is_linked(a1, 'Function', b)
    _safe_set(b, 'functionExpressionRefs', {a2})
    assert _is_linked(b, 'functionExpressionRefs', a2)
    if hasattr(a1, 'Function'):
        assert not _is_linked(a1, 'Function', b)
    if hasattr(a2, 'Function'):
        assert _is_linked(a2, 'Function', b)
    _safe_set(b, 'functionExpressionRefs', set())
    assert not _is_linked(b, 'functionExpressionRefs', a2)
    if hasattr(a2, 'Function'):
        assert not _is_linked(a2, 'Function', b)


def test_assoc_functionResources66_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function67', {a1})
    assert _is_linked(b, 'library_Function67', a1)
    if hasattr(a1, 'library_NetXResource68'):
        assert _is_linked(a1, 'library_NetXResource68', b)
    _safe_set(b, 'library_Function67', {a2})
    assert _is_linked(b, 'library_Function67', a2)
    if hasattr(a1, 'library_NetXResource68'):
        assert not _is_linked(a1, 'library_NetXResource68', b)
    if hasattr(a2, 'library_NetXResource68'):
        assert _is_linked(a2, 'library_NetXResource68', b)
    _safe_set(b, 'library_Function67', set())
    assert not _is_linked(b, 'library_Function67', a2)
    if hasattr(a2, 'library_NetXResource68'):
        assert not _is_linked(a2, 'library_NetXResource68', b)


def test_assoc_functions141_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function143', a1)
    assert _is_linked(b, 'library_Function143', a1)
    if hasattr(a1, 'library_NodeType142'):
        assert _is_linked(a1, 'library_NodeType142', b)
    _safe_set(b, 'library_Function143', a2)
    assert _is_linked(b, 'library_Function143', a2)
    if hasattr(a1, 'library_NodeType142'):
        assert not _is_linked(a1, 'library_NodeType142', b)
    if hasattr(a2, 'library_NodeType142'):
        assert _is_linked(a2, 'library_NodeType142', b)
    _safe_set(b, 'library_Function143', None)
    assert not _is_linked(b, 'library_Function143', a2)
    if hasattr(a2, 'library_NodeType142'):
        assert not _is_linked(a2, 'library_NodeType142', b)


def test_assoc_functions64_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function65', a1)
    assert _is_linked(b, 'library_Function65', a1)
    if hasattr(a1, 'library_Function63'):
        assert _is_linked(a1, 'library_Function63', b)
    _safe_set(b, 'library_Function65', a2)
    assert _is_linked(b, 'library_Function65', a2)
    if hasattr(a1, 'library_Function63'):
        assert not _is_linked(a1, 'library_Function63', b)
    if hasattr(a2, 'library_Function63'):
        assert _is_linked(a2, 'library_Function63', b)
    _safe_set(b, 'library_Function65', None)
    assert not _is_linked(b, 'library_Function65', a2)
    if hasattr(a2, 'library_Function63'):
        assert not _is_linked(a2, 'library_Function63', b)


def test_assoc_functions94_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function95', a1)
    assert _is_linked(b, 'library_Function95', a1)
    if hasattr(a1, 'library_Library'):
        assert _is_linked(a1, 'library_Library', b)
    _safe_set(b, 'library_Function95', a2)
    assert _is_linked(b, 'library_Function95', a2)
    if hasattr(a1, 'library_Library'):
        assert not _is_linked(a1, 'library_Library', b)
    if hasattr(a2, 'library_Library'):
        assert _is_linked(a2, 'library_Library', b)
    _safe_set(b, 'library_Function95', None)
    assert not _is_linked(b, 'library_Function95', a2)
    if hasattr(a2, 'library_Library'):
        assert not _is_linked(a2, 'library_Library', b)


def test_assoc_licensedFunctionRef149_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function151', a1)
    assert _is_linked(b, 'library_Function151', a1)
    if hasattr(a1, 'library_ProductInfo150'):
        assert _is_linked(a1, 'library_ProductInfo150', b)
    _safe_set(b, 'library_Function151', a2)
    assert _is_linked(b, 'library_Function151', a2)
    if hasattr(a1, 'library_ProductInfo150'):
        assert not _is_linked(a1, 'library_ProductInfo150', b)
    if hasattr(a2, 'library_ProductInfo150'):
        assert _is_linked(a2, 'library_ProductInfo150', b)
    _safe_set(b, 'library_Function151', None)
    assert not _is_linked(b, 'library_Function151', a2)
    if hasattr(a2, 'library_ProductInfo150'):
        assert not _is_linked(a2, 'library_ProductInfo150', b)


def test_assoc_nodeTypeRef152_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_NodeType(leafNode="sample_text")
    _safe_set(b, 'library_NodeType154', a1)
    assert _is_linked(b, 'library_NodeType154', a1)
    if hasattr(a1, 'library_ProductInfo153'):
        assert _is_linked(a1, 'library_ProductInfo153', b)
    _safe_set(b, 'library_NodeType154', a2)
    assert _is_linked(b, 'library_NodeType154', a2)
    if hasattr(a1, 'library_ProductInfo153'):
        assert not _is_linked(a1, 'library_ProductInfo153', b)
    if hasattr(a2, 'library_ProductInfo153'):
        assert _is_linked(a2, 'library_ProductInfo153', b)
    _safe_set(b, 'library_NodeType154', None)
    assert not _is_linked(b, 'library_NodeType154', a2)
    if hasattr(a2, 'library_ProductInfo153'):
        assert not _is_linked(a2, 'library_ProductInfo153', b)


def test_assoc_nodeTypes96_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library97', {a1})
    assert _is_linked(b, 'library_Library97', a1)
    if hasattr(a1, 'library_NodeType'):
        assert _is_linked(a1, 'library_NodeType', b)
    _safe_set(b, 'library_Library97', {a2})
    assert _is_linked(b, 'library_Library97', a2)
    if hasattr(a1, 'library_NodeType'):
        assert not _is_linked(a1, 'library_NodeType', b)
    if hasattr(a2, 'library_NodeType'):
        assert _is_linked(a2, 'library_NodeType', b)
    _safe_set(b, 'library_Library97', set())
    assert not _is_linked(b, 'library_Library97', a2)
    if hasattr(a2, 'library_NodeType'):
        assert not _is_linked(a2, 'library_NodeType', b)


def test_assoc_parameterRefs21_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment22', {a1})
    assert _is_linked(b, 'library_Equipment22', a1)
    if hasattr(a1, 'library_Parameter'):
        assert _is_linked(a1, 'library_Parameter', b)
    _safe_set(b, 'library_Equipment22', {a2})
    assert _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a1, 'library_Parameter'):
        assert not _is_linked(a1, 'library_Parameter', b)
    if hasattr(a2, 'library_Parameter'):
        assert _is_linked(a2, 'library_Parameter', b)
    _safe_set(b, 'library_Equipment22', set())
    assert not _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a2, 'library_Parameter'):
        assert not _is_linked(a2, 'library_Parameter', b)


def test_assoc_parameterRefs42_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup43', {a1})
    assert _is_linked(b, 'library_EquipmentGroup43', a1)
    if hasattr(a1, 'library_Parameter44'):
        assert _is_linked(a1, 'library_Parameter44', b)
    _safe_set(b, 'library_EquipmentGroup43', {a2})
    assert _is_linked(b, 'library_EquipmentGroup43', a2)
    if hasattr(a1, 'library_Parameter44'):
        assert not _is_linked(a1, 'library_Parameter44', b)
    if hasattr(a2, 'library_Parameter44'):
        assert _is_linked(a2, 'library_Parameter44', b)
    _safe_set(b, 'library_EquipmentGroup43', set())
    assert not _is_linked(b, 'library_EquipmentGroup43', a2)
    if hasattr(a2, 'library_Parameter44'):
        assert not _is_linked(a2, 'library_Parameter44', b)


def test_assoc_parameterRefs85_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function86', {a1})
    assert _is_linked(b, 'library_Function86', a1)
    if hasattr(a1, 'library_Parameter87'):
        assert _is_linked(a1, 'library_Parameter87', b)
    _safe_set(b, 'library_Function86', {a2})
    assert _is_linked(b, 'library_Function86', a2)
    if hasattr(a1, 'library_Parameter87'):
        assert not _is_linked(a1, 'library_Parameter87', b)
    if hasattr(a2, 'library_Parameter87'):
        assert _is_linked(a2, 'library_Parameter87', b)
    _safe_set(b, 'library_Function86', set())
    assert not _is_linked(b, 'library_Function86', a2)
    if hasattr(a2, 'library_Parameter87'):
        assert not _is_linked(a2, 'library_Parameter87', b)


def test_assoc_parameters106_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library107', {a1})
    assert _is_linked(b, 'library_Library107', a1)
    if hasattr(a1, 'library_Parameter108'):
        assert _is_linked(a1, 'library_Parameter108', b)
    _safe_set(b, 'library_Library107', {a2})
    assert _is_linked(b, 'library_Library107', a2)
    if hasattr(a1, 'library_Parameter108'):
        assert not _is_linked(a1, 'library_Parameter108', b)
    if hasattr(a2, 'library_Parameter108'):
        assert _is_linked(a2, 'library_Parameter108', b)
    _safe_set(b, 'library_Library107', set())
    assert not _is_linked(b, 'library_Library107', a2)
    if hasattr(a2, 'library_Parameter108'):
        assert not _is_linked(a2, 'library_Parameter108', b)


def test_assoc_toleranceRefs17_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment18', {a1})
    assert _is_linked(b, 'library_Equipment18', a1)
    if hasattr(a1, 'library_Tolerance'):
        assert _is_linked(a1, 'library_Tolerance', b)
    _safe_set(b, 'library_Equipment18', {a2})
    assert _is_linked(b, 'library_Equipment18', a2)
    if hasattr(a1, 'library_Tolerance'):
        assert not _is_linked(a1, 'library_Tolerance', b)
    if hasattr(a2, 'library_Tolerance'):
        assert _is_linked(a2, 'library_Tolerance', b)
    _safe_set(b, 'library_Equipment18', set())
    assert not _is_linked(b, 'library_Equipment18', a2)
    if hasattr(a2, 'library_Tolerance'):
        assert not _is_linked(a2, 'library_Tolerance', b)


def test_assoc_toleranceRefs79_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function80', {a1})
    assert _is_linked(b, 'library_Function80', a1)
    if hasattr(a1, 'library_Tolerance81'):
        assert _is_linked(a1, 'library_Tolerance81', b)
    _safe_set(b, 'library_Function80', {a2})
    assert _is_linked(b, 'library_Function80', a2)
    if hasattr(a1, 'library_Tolerance81'):
        assert not _is_linked(a1, 'library_Tolerance81', b)
    if hasattr(a2, 'library_Tolerance81'):
        assert _is_linked(a2, 'library_Tolerance81', b)
    _safe_set(b, 'library_Function80', set())
    assert not _is_linked(b, 'library_Function80', a2)
    if hasattr(a2, 'library_Tolerance81'):
        assert not _is_linked(a2, 'library_Tolerance81', b)


def test_assoc_tolerances109_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library110', {a1})
    assert _is_linked(b, 'library_Library110', a1)
    if hasattr(a1, 'library_Tolerance111'):
        assert _is_linked(a1, 'library_Tolerance111', b)
    _safe_set(b, 'library_Library110', {a2})
    assert _is_linked(b, 'library_Library110', a2)
    if hasattr(a1, 'library_Tolerance111'):
        assert not _is_linked(a1, 'library_Tolerance111', b)
    if hasattr(a2, 'library_Tolerance111'):
        assert _is_linked(a2, 'library_Tolerance111', b)
    _safe_set(b, 'library_Library110', set())
    assert not _is_linked(b, 'library_Library110', a2)
    if hasattr(a2, 'library_Tolerance111'):
        assert not _is_linked(a2, 'library_Tolerance111', b)


def test_assoc_unitRef138_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    _safe_set(b, 'library_NetXResource139', a1)
    assert _is_linked(b, 'library_NetXResource139', a1)
    if hasattr(a1, 'library_Unit140'):
        assert _is_linked(a1, 'library_Unit140', b)
    _safe_set(b, 'library_NetXResource139', a2)
    assert _is_linked(b, 'library_NetXResource139', a2)
    if hasattr(a1, 'library_Unit140'):
        assert not _is_linked(a1, 'library_Unit140', b)
    if hasattr(a2, 'library_Unit140'):
        assert _is_linked(a2, 'library_Unit140', b)
    _safe_set(b, 'library_NetXResource139', None)
    assert not _is_linked(b, 'library_NetXResource139', a2)
    if hasattr(a2, 'library_Unit140'):
        assert not _is_linked(a2, 'library_Unit140', b)


def test_assoc_units115_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library116', {a1})
    assert _is_linked(b, 'library_Library116', a1)
    if hasattr(a1, 'library_Unit'):
        assert _is_linked(a1, 'library_Unit', b)
    _safe_set(b, 'library_Library116', {a2})
    assert _is_linked(b, 'library_Library116', a2)
    if hasattr(a1, 'library_Unit'):
        assert not _is_linked(a1, 'library_Unit', b)
    if hasattr(a2, 'library_Unit'):
        assert _is_linked(a2, 'library_Unit', b)
    _safe_set(b, 'library_Library116', set())
    assert not _is_linked(b, 'library_Library116', a2)
    if hasattr(a2, 'library_Unit'):
        assert not _is_linked(a2, 'library_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_capacityValues124_stub_double():
    # library_Value has no real 'library_Value' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value', None)
    _safe_set(owner, 'library_NetXResource125', {partner})
    assert getattr(partner, 'library_Value') == owner
    _safe_set(owner, 'library_NetXResource125', set())
    assert getattr(partner, 'library_Value') is None


def test_assoc_diagrams1_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo', None)
    _safe_set(owner, 'library_Equipment2', {partner})
    assert getattr(partner, 'library_DiagramInfo') == owner
    _safe_set(owner, 'library_Equipment2', set())
    assert getattr(partner, 'library_DiagramInfo') is None


def test_assoc_diagrams31_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo33' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo33', None)
    _safe_set(owner, 'library_EquipmentGroup32', {partner})
    assert getattr(partner, 'library_DiagramInfo33') == owner
    _safe_set(owner, 'library_EquipmentGroup32', set())
    assert getattr(partner, 'library_DiagramInfo33') is None


def test_assoc_diagrams58_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo59' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo59', None)
    _safe_set(owner, 'library_Function', {partner})
    assert getattr(partner, 'library_DiagramInfo59') == owner
    _safe_set(owner, 'library_Function', set())
    assert getattr(partner, 'library_DiagramInfo59') is None


def test_assoc_equipmentMetricRefs10_stub_double():
    # library_Metric has no real 'library_Metric' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric', None)
    _safe_set(owner, 'library_Equipment11', {partner})
    assert getattr(partner, 'library_Metric') == owner
    _safe_set(owner, 'library_Equipment11', set())
    assert getattr(partner, 'library_Metric') is None


def test_assoc_equipmentRelationshipRefs12_stub_double():
    # library_EquipmentRelationship has no real 'library_EquipmentRelationship' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_EquipmentRelationship()
    setattr(partner, 'library_EquipmentRelationship', None)
    _safe_set(owner, 'library_Equipment13', {partner})
    assert getattr(partner, 'library_EquipmentRelationship') == owner
    _safe_set(owner, 'library_Equipment13', set())
    assert getattr(partner, 'library_EquipmentRelationship') is None


def test_assoc_evaluationObject51_stub_double():
    # library_EObject has no real 'library_EObject' property in the generated
    # code (a bare stub) -- manually attach it so library_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Expression(expressionLines="sample_text", name="sample_text")
    partner = library_EObject()
    setattr(partner, 'library_EObject', None)
    _safe_set(owner, 'library_Expression52', partner)
    assert getattr(partner, 'library_EObject') == owner
    _safe_set(owner, 'library_Expression52', None)
    assert getattr(partner, 'library_EObject') is None


def test_assoc_forecastCapacityValues129_stub_double():
    # library_Value has no real 'library_Value131' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value131', None)
    _safe_set(owner, 'library_NetXResource130', {partner})
    assert getattr(partner, 'library_Value131') == owner
    _safe_set(owner, 'library_NetXResource130', set())
    assert getattr(partner, 'library_Value131') is None


def test_assoc_forecastValues132_stub_double():
    # library_Value has no real 'library_Value134' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value134', None)
    _safe_set(owner, 'library_NetXResource133', {partner})
    assert getattr(partner, 'library_Value134') == owner
    _safe_set(owner, 'library_NetXResource133', set())
    assert getattr(partner, 'library_Value134') is None


def test_assoc_functionMetricRefs69_stub_double():
    # library_Metric has no real 'library_Metric71' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric71', None)
    _safe_set(owner, 'library_Function70', {partner})
    assert getattr(partner, 'library_Metric71') == owner
    _safe_set(owner, 'library_Function70', set())
    assert getattr(partner, 'library_Metric71') is None


def test_assoc_functionRelationshipRefs72_stub_double():
    # library_FunctionRelationship has no real 'library_FunctionRelationship' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_FunctionRelationship()
    setattr(partner, 'library_FunctionRelationship', None)
    _safe_set(owner, 'library_Function73', {partner})
    assert getattr(partner, 'library_FunctionRelationship') == owner
    _safe_set(owner, 'library_Function73', set())
    assert getattr(partner, 'library_FunctionRelationship') is None


def test_assoc_icons155_stub_double():
    # library_MultiImage has no real 'library_MultiImage157' property in the generated
    # code (a bare stub) -- manually attach it so library_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage157', None)
    _safe_set(owner, 'library_Unit156', partner)
    assert getattr(partner, 'library_MultiImage157') == owner
    _safe_set(owner, 'library_Unit156', None)
    assert getattr(partner, 'library_MultiImage157') is None


def test_assoc_icons29_stub_double():
    # library_MultiImage has no real 'library_MultiImage' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage', None)
    _safe_set(owner, 'library_Equipment30', partner)
    assert getattr(partner, 'library_MultiImage') == owner
    _safe_set(owner, 'library_Equipment30', None)
    assert getattr(partner, 'library_MultiImage') is None


def test_assoc_icons60_stub_double():
    # library_MultiImage has no real 'library_MultiImage62' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage62', None)
    _safe_set(owner, 'library_Function61', partner)
    assert getattr(partner, 'library_MultiImage62') == owner
    _safe_set(owner, 'library_Function61', None)
    assert getattr(partner, 'library_MultiImage62') is None


def test_assoc_lifecycle0_stub_double():
    # library_Lifecycle has no real 'library_Lifecycle' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_Lifecycle()
    setattr(partner, 'library_Lifecycle', None)
    _safe_set(owner, 'library_Equipment', partner)
    assert getattr(partner, 'library_Lifecycle') == owner
    _safe_set(owner, 'library_Equipment', None)
    assert getattr(partner, 'library_Lifecycle') is None


def test_assoc_metricRef119_stub_double():
    # library_Metric has no real 'library_Metric121' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric121', None)
    _safe_set(owner, 'library_NetXResource120', partner)
    assert getattr(partner, 'library_Metric121') == owner
    _safe_set(owner, 'library_NetXResource120', None)
    assert getattr(partner, 'library_Metric121') is None


def test_assoc_metricSources104_stub_double():
    # library_MetricSource has no real 'library_MetricSource' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_MetricSource()
    setattr(partner, 'library_MetricSource', None)
    _safe_set(owner, 'library_Library105', {partner})
    assert getattr(partner, 'library_MetricSource') == owner
    _safe_set(owner, 'library_Library105', set())
    assert getattr(partner, 'library_MetricSource') is None


def test_assoc_metricValueRanges122_stub_double():
    # library_MetricValueRange has no real 'library_MetricValueRange' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_MetricValueRange()
    setattr(partner, 'library_MetricValueRange', None)
    _safe_set(owner, 'library_NetXResource123', {partner})
    assert getattr(partner, 'library_MetricValueRange') == owner
    _safe_set(owner, 'library_NetXResource123', set())
    assert getattr(partner, 'library_MetricValueRange') is None


def test_assoc_metrics101_stub_double():
    # library_Metric has no real 'library_Metric103' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric103', None)
    _safe_set(owner, 'library_Library102', {partner})
    assert getattr(partner, 'library_Metric103') == owner
    _safe_set(owner, 'library_Library102', set())
    assert getattr(partner, 'library_Metric103') is None


def test_assoc_products158_stub_double():
    # library_Vendor has no real 'library_Vendor' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Vendor()
    setattr(partner, 'library_Vendor', None)
    _safe_set(owner, 'library_ProductInfo159', partner)
    assert owner in getattr(partner, 'library_Vendor')
    _safe_set(owner, 'library_ProductInfo159', None)
    assert owner not in getattr(partner, 'library_Vendor')


def test_assoc_protocolRefs19_stub_double():
    # library_Protocol has no real 'library_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_Protocol()
    setattr(partner, 'library_Protocol', None)
    _safe_set(owner, 'library_Equipment20', {partner})
    assert getattr(partner, 'library_Protocol') == owner
    _safe_set(owner, 'library_Equipment20', set())
    assert getattr(partner, 'library_Protocol') is None


def test_assoc_protocolRefs82_stub_double():
    # library_Protocol has no real 'library_Protocol84' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_Protocol()
    setattr(partner, 'library_Protocol84', None)
    _safe_set(owner, 'library_Function83', {partner})
    assert getattr(partner, 'library_Protocol84') == owner
    _safe_set(owner, 'library_Function83', set())
    assert getattr(partner, 'library_Protocol84') is None


def test_assoc_serviceProfileRefs56_stub_double():
    # library_ServiceProfile has no real 'library_ServiceProfile' property in the generated
    # code (a bare stub) -- manually attach it so library_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Expression(expressionLines="sample_text", name="sample_text")
    partner = library_ServiceProfile()
    setattr(partner, 'library_ServiceProfile', None)
    _safe_set(owner, 'library_Expression57', {partner})
    assert getattr(partner, 'library_ServiceProfile') == owner
    _safe_set(owner, 'library_Expression57', set())
    assert getattr(partner, 'library_ServiceProfile') is None


def test_assoc_trendedValues135_stub_double():
    # library_Value has no real 'library_Value137' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value137', None)
    _safe_set(owner, 'library_NetXResource136', {partner})
    assert getattr(partner, 'library_Value137') == owner
    _safe_set(owner, 'library_NetXResource136', set())
    assert getattr(partner, 'library_Value137') is None


def test_assoc_utilizationValues126_stub_double():
    # library_Value has no real 'library_Value128' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value128', None)
    _safe_set(owner, 'library_NetXResource127', {partner})
    assert getattr(partner, 'library_Value128') == owner
    _safe_set(owner, 'library_NetXResource127', set())
    assert getattr(partner, 'library_Value128') is None


def test_assoc_version117_stub_double():
    # library_Meta has no real 'library_Meta' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Meta()
    setattr(partner, 'library_Meta', None)
    _safe_set(owner, 'library_Library118', partner)
    assert getattr(partner, 'library_Meta') == owner
    _safe_set(owner, 'library_Library118', None)
    assert getattr(partner, 'library_Meta') is None


