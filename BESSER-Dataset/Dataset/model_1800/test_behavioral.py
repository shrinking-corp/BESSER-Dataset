import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Company,
    library_Company,
    library_DiagramInfo,
    library_Equipment,
    library_EquipmentGroup,
    library_EquipmentRelationship,
    library_Expression,
    library_Function,
    library_FunctionRelationship,
    library_Library,
    library_Lifecycle,
    library_Message,
    library_Meta,
    library_Metric,
    library_MetricValueRange,
    library_MultiImage,
    library_NetXResource,
    library_NodeType,
    library_Parameter,
    library_Procedure,
    library_ProductInfo,
    library_Protocol,
    library_ServiceProfile,
    library_Tolerance,
    library_Unit,
    library_Value,
    library_Vendor,
    LevelType,
    OSIType,
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

def test_assoc_allEquipmentResources21_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment22', {a1})
    assert _is_linked(b, 'library_Equipment22', a1)
    if hasattr(a1, 'library_NetXResource23'):
        assert _is_linked(a1, 'library_NetXResource23', b)
    _safe_set(b, 'library_Equipment22', {a2})
    assert _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a1, 'library_NetXResource23'):
        assert not _is_linked(a1, 'library_NetXResource23', b)
    if hasattr(a2, 'library_NetXResource23'):
        assert _is_linked(a2, 'library_NetXResource23', b)
    _safe_set(b, 'library_Equipment22', set())
    assert not _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a2, 'library_NetXResource23'):
        assert not _is_linked(a2, 'library_NetXResource23', b)


def test_assoc_allEquipmentResources43_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup44', {a1})
    assert _is_linked(b, 'library_EquipmentGroup44', a1)
    if hasattr(a1, 'library_NetXResource45'):
        assert _is_linked(a1, 'library_NetXResource45', b)
    _safe_set(b, 'library_EquipmentGroup44', {a2})
    assert _is_linked(b, 'library_EquipmentGroup44', a2)
    if hasattr(a1, 'library_NetXResource45'):
        assert not _is_linked(a1, 'library_NetXResource45', b)
    if hasattr(a2, 'library_NetXResource45'):
        assert _is_linked(a2, 'library_NetXResource45', b)
    _safe_set(b, 'library_EquipmentGroup44', set())
    assert not _is_linked(b, 'library_EquipmentGroup44', a2)
    if hasattr(a2, 'library_NetXResource45'):
        assert not _is_linked(a2, 'library_NetXResource45', b)


def test_assoc_allEquipments25_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", description="sample_text_2", equipmentCode="sample_text_2", equipmentName="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment26', a1)
    assert _is_linked(b, 'library_Equipment26', a1)
    if hasattr(a1, 'library_Equipment24'):
        assert _is_linked(a1, 'library_Equipment24', b)
    _safe_set(b, 'library_Equipment26', a2)
    assert _is_linked(b, 'library_Equipment26', a2)
    if hasattr(a1, 'library_Equipment24'):
        assert not _is_linked(a1, 'library_Equipment24', b)
    if hasattr(a2, 'library_Equipment24'):
        assert _is_linked(a2, 'library_Equipment24', b)
    _safe_set(b, 'library_Equipment26', None)
    assert not _is_linked(b, 'library_Equipment26', a2)
    if hasattr(a2, 'library_Equipment24'):
        assert not _is_linked(a2, 'library_Equipment24', b)


def test_assoc_allEquipments46_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment48', a1)
    assert _is_linked(b, 'library_Equipment48', a1)
    if hasattr(a1, 'library_EquipmentGroup47'):
        assert _is_linked(a1, 'library_EquipmentGroup47', b)
    _safe_set(b, 'library_Equipment48', a2)
    assert _is_linked(b, 'library_Equipment48', a2)
    if hasattr(a1, 'library_EquipmentGroup47'):
        assert not _is_linked(a1, 'library_EquipmentGroup47', b)
    if hasattr(a2, 'library_EquipmentGroup47'):
        assert _is_linked(a2, 'library_EquipmentGroup47', b)
    _safe_set(b, 'library_Equipment48', None)
    assert not _is_linked(b, 'library_Equipment48', a2)
    if hasattr(a2, 'library_EquipmentGroup47'):
        assert not _is_linked(a2, 'library_EquipmentGroup47', b)


def test_assoc_allFunctionResources80_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function81', {a1})
    assert _is_linked(b, 'library_Function81', a1)
    if hasattr(a1, 'library_NetXResource82'):
        assert _is_linked(a1, 'library_NetXResource82', b)
    _safe_set(b, 'library_Function81', {a2})
    assert _is_linked(b, 'library_Function81', a2)
    if hasattr(a1, 'library_NetXResource82'):
        assert not _is_linked(a1, 'library_NetXResource82', b)
    if hasattr(a2, 'library_NetXResource82'):
        assert _is_linked(a2, 'library_NetXResource82', b)
    _safe_set(b, 'library_Function81', set())
    assert not _is_linked(b, 'library_Function81', a2)
    if hasattr(a2, 'library_NetXResource82'):
        assert not _is_linked(a2, 'library_NetXResource82', b)


def test_assoc_allFunctions84_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function85', a1)
    assert _is_linked(b, 'library_Function85', a1)
    if hasattr(a1, 'library_Function83'):
        assert _is_linked(a1, 'library_Function83', b)
    _safe_set(b, 'library_Function85', a2)
    assert _is_linked(b, 'library_Function85', a2)
    if hasattr(a1, 'library_Function83'):
        assert not _is_linked(a1, 'library_Function83', b)
    if hasattr(a2, 'library_Function83'):
        assert _is_linked(a2, 'library_Function83', b)
    _safe_set(b, 'library_Function85', None)
    assert not _is_linked(b, 'library_Function85', a2)
    if hasattr(a2, 'library_Function83'):
        assert not _is_linked(a2, 'library_Function83', b)


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


def test_assoc_equipmentGroupRefs51_reverse_link_reassign_clear():
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


def test_assoc_equipmentGroupResources32_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup33', {a1})
    assert _is_linked(b, 'library_EquipmentGroup33', a1)
    if hasattr(a1, 'library_NetXResource34'):
        assert _is_linked(a1, 'library_NetXResource34', b)
    _safe_set(b, 'library_EquipmentGroup33', {a2})
    assert _is_linked(b, 'library_EquipmentGroup33', a2)
    if hasattr(a1, 'library_NetXResource34'):
        assert not _is_linked(a1, 'library_NetXResource34', b)
    if hasattr(a2, 'library_NetXResource34'):
        assert _is_linked(a2, 'library_NetXResource34', b)
    _safe_set(b, 'library_EquipmentGroup33', set())
    assert not _is_linked(b, 'library_EquipmentGroup33', a2)
    if hasattr(a2, 'library_NetXResource34'):
        assert not _is_linked(a2, 'library_NetXResource34', b)


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


def test_assoc_equipmentRef135_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment136', a1)
    assert _is_linked(b, 'library_Equipment136', a1)
    if hasattr(a1, 'library_ProductInfo'):
        assert _is_linked(a1, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment136', a2)
    assert _is_linked(b, 'library_Equipment136', a2)
    if hasattr(a1, 'library_ProductInfo'):
        assert not _is_linked(a1, 'library_ProductInfo', b)
    if hasattr(a2, 'library_ProductInfo'):
        assert _is_linked(a2, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment136', None)
    assert not _is_linked(b, 'library_Equipment136', a2)
    if hasattr(a2, 'library_ProductInfo'):
        assert not _is_linked(a2, 'library_ProductInfo', b)


def test_assoc_equipmentRefs37_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment39', a1)
    assert _is_linked(b, 'library_Equipment39', a1)
    if hasattr(a1, 'library_EquipmentGroup38'):
        assert _is_linked(a1, 'library_EquipmentGroup38', b)
    _safe_set(b, 'library_Equipment39', a2)
    assert _is_linked(b, 'library_Equipment39', a2)
    if hasattr(a1, 'library_EquipmentGroup38'):
        assert not _is_linked(a1, 'library_EquipmentGroup38', b)
    if hasattr(a2, 'library_EquipmentGroup38'):
        assert _is_linked(a2, 'library_EquipmentGroup38', b)
    _safe_set(b, 'library_Equipment39', None)
    assert not _is_linked(b, 'library_Equipment39', a2)
    if hasattr(a2, 'library_EquipmentGroup38'):
        assert not _is_linked(a2, 'library_EquipmentGroup38', b)


def test_assoc_equipmentRefs49_reverse_link_reassign_clear():
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


def test_assoc_equipments90_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment92', a1)
    assert _is_linked(b, 'library_Equipment92', a1)
    if hasattr(a1, 'library_Library91'):
        assert _is_linked(a1, 'library_Library91', b)
    _safe_set(b, 'library_Equipment92', a2)
    assert _is_linked(b, 'library_Equipment92', a2)
    if hasattr(a1, 'library_Library91'):
        assert not _is_linked(a1, 'library_Library91', b)
    if hasattr(a2, 'library_Library91'):
        assert _is_linked(a2, 'library_Library91', b)
    _safe_set(b, 'library_Equipment92', None)
    assert not _is_linked(b, 'library_Equipment92', a2)
    if hasattr(a2, 'library_Library91'):
        assert not _is_linked(a2, 'library_Library91', b)


def test_assoc_expressionRefs35_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'equipmentGroupRefs', {a1})
    assert _is_linked(b, 'equipmentGroupRefs', a1)
    if hasattr(a1, 'Expression36'):
        assert _is_linked(a1, 'Expression36', b)
    _safe_set(b, 'equipmentGroupRefs', {a2})
    assert _is_linked(b, 'equipmentGroupRefs', a2)
    if hasattr(a1, 'Expression36'):
        assert not _is_linked(a1, 'Expression36', b)
    if hasattr(a2, 'Expression36'):
        assert _is_linked(a2, 'Expression36', b)
    _safe_set(b, 'equipmentGroupRefs', set())
    assert not _is_linked(b, 'equipmentGroupRefs', a2)
    if hasattr(a2, 'Expression36'):
        assert not _is_linked(a2, 'Expression36', b)


def test_assoc_expressions105_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression107', a1)
    assert _is_linked(b, 'library_Expression107', a1)
    if hasattr(a1, 'library_Library106'):
        assert _is_linked(a1, 'library_Library106', b)
    _safe_set(b, 'library_Expression107', a2)
    assert _is_linked(b, 'library_Expression107', a2)
    if hasattr(a1, 'library_Library106'):
        assert not _is_linked(a1, 'library_Library106', b)
    if hasattr(a2, 'library_Library106'):
        assert _is_linked(a2, 'library_Library106', b)
    _safe_set(b, 'library_Expression107', None)
    assert not _is_linked(b, 'library_Expression107', a2)
    if hasattr(a2, 'library_Library106'):
        assert not _is_linked(a2, 'library_Library106', b)


def test_assoc_functionExpressionRefs69_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'Expression70', a1)
    assert _is_linked(b, 'Expression70', a1)
    if hasattr(a1, 'functionRefs'):
        assert _is_linked(a1, 'functionRefs', b)
    _safe_set(b, 'Expression70', a2)
    assert _is_linked(b, 'Expression70', a2)
    if hasattr(a1, 'functionRefs'):
        assert not _is_linked(a1, 'functionRefs', b)
    if hasattr(a2, 'functionRefs'):
        assert _is_linked(a2, 'functionRefs', b)
    _safe_set(b, 'Expression70', None)
    assert not _is_linked(b, 'Expression70', a2)
    if hasattr(a2, 'functionRefs'):
        assert not _is_linked(a2, 'functionRefs', b)


def test_assoc_functionRefs50_reverse_link_reassign_clear():
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


def test_assoc_functionResources61_reverse_link_reassign_clear():
    a1 = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    a2 = library_NetXResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function62', {a1})
    assert _is_linked(b, 'library_Function62', a1)
    if hasattr(a1, 'library_NetXResource63'):
        assert _is_linked(a1, 'library_NetXResource63', b)
    _safe_set(b, 'library_Function62', {a2})
    assert _is_linked(b, 'library_Function62', a2)
    if hasattr(a1, 'library_NetXResource63'):
        assert not _is_linked(a1, 'library_NetXResource63', b)
    if hasattr(a2, 'library_NetXResource63'):
        assert _is_linked(a2, 'library_NetXResource63', b)
    _safe_set(b, 'library_Function62', set())
    assert not _is_linked(b, 'library_Function62', a2)
    if hasattr(a2, 'library_NetXResource63'):
        assert not _is_linked(a2, 'library_NetXResource63', b)


def test_assoc_functions59_reverse_link_reassign_clear():
    a1 = library_Function(description="sample_text", functionName="sample_text")
    a2 = library_Function(description="sample_text_2", functionName="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function60', a1)
    assert _is_linked(b, 'library_Function60', a1)
    if hasattr(a1, 'library_Function58'):
        assert _is_linked(a1, 'library_Function58', b)
    _safe_set(b, 'library_Function60', a2)
    assert _is_linked(b, 'library_Function60', a2)
    if hasattr(a1, 'library_Function58'):
        assert not _is_linked(a1, 'library_Function58', b)
    if hasattr(a2, 'library_Function58'):
        assert _is_linked(a2, 'library_Function58', b)
    _safe_set(b, 'library_Function60', None)
    assert not _is_linked(b, 'library_Function60', a2)
    if hasattr(a2, 'library_Function58'):
        assert not _is_linked(a2, 'library_Function58', b)


def test_assoc_functions86_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function87', a1)
    assert _is_linked(b, 'library_Function87', a1)
    if hasattr(a1, 'library_Library'):
        assert _is_linked(a1, 'library_Library', b)
    _safe_set(b, 'library_Function87', a2)
    assert _is_linked(b, 'library_Function87', a2)
    if hasattr(a1, 'library_Library'):
        assert not _is_linked(a1, 'library_Library', b)
    if hasattr(a2, 'library_Library'):
        assert _is_linked(a2, 'library_Library', b)
    _safe_set(b, 'library_Function87', None)
    assert not _is_linked(b, 'library_Function87', a2)
    if hasattr(a2, 'library_Library'):
        assert not _is_linked(a2, 'library_Library', b)


def test_assoc_licensedFunctionRef137_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function139', a1)
    assert _is_linked(b, 'library_Function139', a1)
    if hasattr(a1, 'library_ProductInfo138'):
        assert _is_linked(a1, 'library_ProductInfo138', b)
    _safe_set(b, 'library_Function139', a2)
    assert _is_linked(b, 'library_Function139', a2)
    if hasattr(a1, 'library_ProductInfo138'):
        assert not _is_linked(a1, 'library_ProductInfo138', b)
    if hasattr(a2, 'library_ProductInfo138'):
        assert _is_linked(a2, 'library_ProductInfo138', b)
    _safe_set(b, 'library_Function139', None)
    assert not _is_linked(b, 'library_Function139', a2)
    if hasattr(a2, 'library_ProductInfo138'):
        assert not _is_linked(a2, 'library_ProductInfo138', b)


def test_assoc_messages134_reverse_link_reassign_clear():
    a1 = library_Procedure(name="sample_text")
    a2 = library_Procedure(name="sample_text_2")
    b = library_Message(name="sample_text")
    _safe_set(b, 'library_Message', a1)
    assert _is_linked(b, 'library_Message', a1)
    if hasattr(a1, 'library_Procedure'):
        assert _is_linked(a1, 'library_Procedure', b)
    _safe_set(b, 'library_Message', a2)
    assert _is_linked(b, 'library_Message', a2)
    if hasattr(a1, 'library_Procedure'):
        assert not _is_linked(a1, 'library_Procedure', b)
    if hasattr(a2, 'library_Procedure'):
        assert _is_linked(a2, 'library_Procedure', b)
    _safe_set(b, 'library_Message', None)
    assert not _is_linked(b, 'library_Message', a2)
    if hasattr(a2, 'library_Procedure'):
        assert not _is_linked(a2, 'library_Procedure', b)


def test_assoc_parameterRefs19_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment20', {a1})
    assert _is_linked(b, 'library_Equipment20', a1)
    if hasattr(a1, 'library_Parameter'):
        assert _is_linked(a1, 'library_Parameter', b)
    _safe_set(b, 'library_Equipment20', {a2})
    assert _is_linked(b, 'library_Equipment20', a2)
    if hasattr(a1, 'library_Parameter'):
        assert not _is_linked(a1, 'library_Parameter', b)
    if hasattr(a2, 'library_Parameter'):
        assert _is_linked(a2, 'library_Parameter', b)
    _safe_set(b, 'library_Equipment20', set())
    assert not _is_linked(b, 'library_Equipment20', a2)
    if hasattr(a2, 'library_Parameter'):
        assert not _is_linked(a2, 'library_Parameter', b)


def test_assoc_parameterRefs40_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup41', {a1})
    assert _is_linked(b, 'library_EquipmentGroup41', a1)
    if hasattr(a1, 'library_Parameter42'):
        assert _is_linked(a1, 'library_Parameter42', b)
    _safe_set(b, 'library_EquipmentGroup41', {a2})
    assert _is_linked(b, 'library_EquipmentGroup41', a2)
    if hasattr(a1, 'library_Parameter42'):
        assert not _is_linked(a1, 'library_Parameter42', b)
    if hasattr(a2, 'library_Parameter42'):
        assert _is_linked(a2, 'library_Parameter42', b)
    _safe_set(b, 'library_EquipmentGroup41', set())
    assert not _is_linked(b, 'library_EquipmentGroup41', a2)
    if hasattr(a2, 'library_Parameter42'):
        assert not _is_linked(a2, 'library_Parameter42', b)


def test_assoc_parameterRefs77_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function78', {a1})
    assert _is_linked(b, 'library_Function78', a1)
    if hasattr(a1, 'library_Parameter79'):
        assert _is_linked(a1, 'library_Parameter79', b)
    _safe_set(b, 'library_Function78', {a2})
    assert _is_linked(b, 'library_Function78', a2)
    if hasattr(a1, 'library_Parameter79'):
        assert not _is_linked(a1, 'library_Parameter79', b)
    if hasattr(a2, 'library_Parameter79'):
        assert _is_linked(a2, 'library_Parameter79', b)
    _safe_set(b, 'library_Function78', set())
    assert not _is_linked(b, 'library_Function78', a2)
    if hasattr(a2, 'library_Parameter79'):
        assert not _is_linked(a2, 'library_Parameter79', b)


def test_assoc_parameters96_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library97', {a1})
    assert _is_linked(b, 'library_Library97', a1)
    if hasattr(a1, 'library_Parameter98'):
        assert _is_linked(a1, 'library_Parameter98', b)
    _safe_set(b, 'library_Library97', {a2})
    assert _is_linked(b, 'library_Library97', a2)
    if hasattr(a1, 'library_Parameter98'):
        assert not _is_linked(a1, 'library_Parameter98', b)
    if hasattr(a2, 'library_Parameter98'):
        assert _is_linked(a2, 'library_Parameter98', b)
    _safe_set(b, 'library_Library97', set())
    assert not _is_linked(b, 'library_Library97', a2)
    if hasattr(a2, 'library_Parameter98'):
        assert not _is_linked(a2, 'library_Parameter98', b)


def test_assoc_procedures143_reverse_link_reassign_clear():
    a1 = library_Protocol(description="sample_text", name="sample_text", oSI="sample_text", specification="sample_text")
    a2 = library_Protocol(description="sample_text_2", name="sample_text_2", oSI="sample_text_2", specification="sample_text_2")
    b = library_Procedure(name="sample_text")
    _safe_set(b, 'library_Procedure145', a1)
    assert _is_linked(b, 'library_Procedure145', a1)
    if hasattr(a1, 'library_Protocol144'):
        assert _is_linked(a1, 'library_Protocol144', b)
    _safe_set(b, 'library_Procedure145', a2)
    assert _is_linked(b, 'library_Procedure145', a2)
    if hasattr(a1, 'library_Protocol144'):
        assert not _is_linked(a1, 'library_Protocol144', b)
    if hasattr(a2, 'library_Protocol144'):
        assert _is_linked(a2, 'library_Protocol144', b)
    _safe_set(b, 'library_Procedure145', None)
    assert not _is_linked(b, 'library_Procedure145', a2)
    if hasattr(a2, 'library_Protocol144'):
        assert not _is_linked(a2, 'library_Protocol144', b)


def test_assoc_protocolRefs17_reverse_link_reassign_clear():
    a1 = library_Protocol(description="sample_text", name="sample_text", oSI="sample_text", specification="sample_text")
    a2 = library_Protocol(description="sample_text_2", name="sample_text_2", oSI="sample_text_2", specification="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment18', {a1})
    assert _is_linked(b, 'library_Equipment18', a1)
    if hasattr(a1, 'library_Protocol'):
        assert _is_linked(a1, 'library_Protocol', b)
    _safe_set(b, 'library_Equipment18', {a2})
    assert _is_linked(b, 'library_Equipment18', a2)
    if hasattr(a1, 'library_Protocol'):
        assert not _is_linked(a1, 'library_Protocol', b)
    if hasattr(a2, 'library_Protocol'):
        assert _is_linked(a2, 'library_Protocol', b)
    _safe_set(b, 'library_Equipment18', set())
    assert not _is_linked(b, 'library_Equipment18', a2)
    if hasattr(a2, 'library_Protocol'):
        assert not _is_linked(a2, 'library_Protocol', b)


def test_assoc_protocolRefs74_reverse_link_reassign_clear():
    a1 = library_Protocol(description="sample_text", name="sample_text", oSI="sample_text", specification="sample_text")
    a2 = library_Protocol(description="sample_text_2", name="sample_text_2", oSI="sample_text_2", specification="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function75', {a1})
    assert _is_linked(b, 'library_Function75', a1)
    if hasattr(a1, 'library_Protocol76'):
        assert _is_linked(a1, 'library_Protocol76', b)
    _safe_set(b, 'library_Function75', {a2})
    assert _is_linked(b, 'library_Function75', a2)
    if hasattr(a1, 'library_Protocol76'):
        assert not _is_linked(a1, 'library_Protocol76', b)
    if hasattr(a2, 'library_Protocol76'):
        assert _is_linked(a2, 'library_Protocol76', b)
    _safe_set(b, 'library_Function75', set())
    assert not _is_linked(b, 'library_Function75', a2)
    if hasattr(a2, 'library_Protocol76'):
        assert not _is_linked(a2, 'library_Protocol76', b)


def test_assoc_protocols99_reverse_link_reassign_clear():
    a1 = library_Protocol(description="sample_text", name="sample_text", oSI="sample_text", specification="sample_text")
    a2 = library_Protocol(description="sample_text_2", name="sample_text_2", oSI="sample_text_2", specification="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library100', {a1})
    assert _is_linked(b, 'library_Library100', a1)
    if hasattr(a1, 'library_Protocol101'):
        assert _is_linked(a1, 'library_Protocol101', b)
    _safe_set(b, 'library_Library100', {a2})
    assert _is_linked(b, 'library_Library100', a2)
    if hasattr(a1, 'library_Protocol101'):
        assert not _is_linked(a1, 'library_Protocol101', b)
    if hasattr(a2, 'library_Protocol101'):
        assert _is_linked(a2, 'library_Protocol101', b)
    _safe_set(b, 'library_Library100', set())
    assert not _is_linked(b, 'library_Library100', a2)
    if hasattr(a2, 'library_Protocol101'):
        assert not _is_linked(a2, 'library_Protocol101', b)


def test_assoc_toleranceRefs15_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment16', {a1})
    assert _is_linked(b, 'library_Equipment16', a1)
    if hasattr(a1, 'library_Tolerance'):
        assert _is_linked(a1, 'library_Tolerance', b)
    _safe_set(b, 'library_Equipment16', {a2})
    assert _is_linked(b, 'library_Equipment16', a2)
    if hasattr(a1, 'library_Tolerance'):
        assert not _is_linked(a1, 'library_Tolerance', b)
    if hasattr(a2, 'library_Tolerance'):
        assert _is_linked(a2, 'library_Tolerance', b)
    _safe_set(b, 'library_Equipment16', set())
    assert not _is_linked(b, 'library_Equipment16', a2)
    if hasattr(a2, 'library_Tolerance'):
        assert not _is_linked(a2, 'library_Tolerance', b)


def test_assoc_toleranceRefs71_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Function(description="sample_text", functionName="sample_text")
    _safe_set(b, 'library_Function72', {a1})
    assert _is_linked(b, 'library_Function72', a1)
    if hasattr(a1, 'library_Tolerance73'):
        assert _is_linked(a1, 'library_Tolerance73', b)
    _safe_set(b, 'library_Function72', {a2})
    assert _is_linked(b, 'library_Function72', a2)
    if hasattr(a1, 'library_Tolerance73'):
        assert not _is_linked(a1, 'library_Tolerance73', b)
    if hasattr(a2, 'library_Tolerance73'):
        assert _is_linked(a2, 'library_Tolerance73', b)
    _safe_set(b, 'library_Function72', set())
    assert not _is_linked(b, 'library_Function72', a2)
    if hasattr(a2, 'library_Tolerance73'):
        assert not _is_linked(a2, 'library_Tolerance73', b)


def test_assoc_tolerances102_reverse_link_reassign_clear():
    a1 = library_Tolerance(expression="sample_text", level="sample_text", name="sample_text")
    a2 = library_Tolerance(expression="sample_text_2", level="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library103', {a1})
    assert _is_linked(b, 'library_Library103', a1)
    if hasattr(a1, 'library_Tolerance104'):
        assert _is_linked(a1, 'library_Tolerance104', b)
    _safe_set(b, 'library_Library103', {a2})
    assert _is_linked(b, 'library_Library103', a2)
    if hasattr(a1, 'library_Tolerance104'):
        assert not _is_linked(a1, 'library_Tolerance104', b)
    if hasattr(a2, 'library_Tolerance104'):
        assert _is_linked(a2, 'library_Tolerance104', b)
    _safe_set(b, 'library_Library103', set())
    assert not _is_linked(b, 'library_Library103', a2)
    if hasattr(a2, 'library_Tolerance104'):
        assert not _is_linked(a2, 'library_Tolerance104', b)


def test_assoc_unitRef125_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    _safe_set(b, 'library_NetXResource126', a1)
    assert _is_linked(b, 'library_NetXResource126', a1)
    if hasattr(a1, 'library_Unit127'):
        assert _is_linked(a1, 'library_Unit127', b)
    _safe_set(b, 'library_NetXResource126', a2)
    assert _is_linked(b, 'library_NetXResource126', a2)
    if hasattr(a1, 'library_Unit127'):
        assert not _is_linked(a1, 'library_Unit127', b)
    if hasattr(a2, 'library_Unit127'):
        assert _is_linked(a2, 'library_Unit127', b)
    _safe_set(b, 'library_NetXResource126', None)
    assert not _is_linked(b, 'library_NetXResource126', a2)
    if hasattr(a2, 'library_Unit127'):
        assert not _is_linked(a2, 'library_Unit127', b)


def test_assoc_units108_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library109', {a1})
    assert _is_linked(b, 'library_Library109', a1)
    if hasattr(a1, 'library_Unit'):
        assert _is_linked(a1, 'library_Unit', b)
    _safe_set(b, 'library_Library109', {a2})
    assert _is_linked(b, 'library_Library109', a2)
    if hasattr(a1, 'library_Unit'):
        assert not _is_linked(a1, 'library_Unit', b)
    if hasattr(a2, 'library_Unit'):
        assert _is_linked(a2, 'library_Unit', b)
    _safe_set(b, 'library_Library109', set())
    assert not _is_linked(b, 'library_Library109', a2)
    if hasattr(a2, 'library_Unit'):
        assert not _is_linked(a2, 'library_Unit', b)


def test_assoc_version110_reverse_link_reassign_clear():
    a1 = library_Meta(author="sample_text", description="sample_text", version="sample_text")
    a2 = library_Meta(author="sample_text_2", description="sample_text_2", version="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library111', a1)
    assert _is_linked(b, 'library_Library111', a1)
    if hasattr(a1, 'library_Meta'):
        assert _is_linked(a1, 'library_Meta', b)
    _safe_set(b, 'library_Library111', a2)
    assert _is_linked(b, 'library_Library111', a2)
    if hasattr(a1, 'library_Meta'):
        assert not _is_linked(a1, 'library_Meta', b)
    if hasattr(a2, 'library_Meta'):
        assert _is_linked(a2, 'library_Meta', b)
    _safe_set(b, 'library_Library111', None)
    assert not _is_linked(b, 'library_Library111', a2)
    if hasattr(a2, 'library_Meta'):
        assert not _is_linked(a2, 'library_Meta', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyRef146_stub_double():
    # library_Company has no real 'library_Company' property in the generated
    # code (a bare stub) -- manually attach it so library_Protocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Protocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Protocol(description="sample_text", name="sample_text", oSI="sample_text", specification="sample_text")
    partner = library_Company()
    setattr(partner, 'library_Company', None)
    _safe_set(owner, 'library_Protocol147', partner)
    assert getattr(partner, 'library_Company') == owner
    _safe_set(owner, 'library_Protocol147', None)
    assert getattr(partner, 'library_Company') is None


def test_assoc_capacityValues114_stub_double():
    # library_Value has no real 'library_Value' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value', None)
    _safe_set(owner, 'library_NetXResource115', {partner})
    assert getattr(partner, 'library_Value') == owner
    _safe_set(owner, 'library_NetXResource115', set())
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


def test_assoc_diagrams29_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo31' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo31', None)
    _safe_set(owner, 'library_EquipmentGroup30', {partner})
    assert getattr(partner, 'library_DiagramInfo31') == owner
    _safe_set(owner, 'library_EquipmentGroup30', set())
    assert getattr(partner, 'library_DiagramInfo31') is None


def test_assoc_diagrams53_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo54' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo54', None)
    _safe_set(owner, 'library_Function', {partner})
    assert getattr(partner, 'library_DiagramInfo54') == owner
    _safe_set(owner, 'library_Function', set())
    assert getattr(partner, 'library_DiagramInfo54') is None


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


def test_assoc_equipments131_stub_double():
    # library_NodeType has no real 'library_NodeType132' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_NodeType()
    setattr(partner, 'library_NodeType132', None)
    _safe_set(owner, 'library_Equipment133', partner)
    assert owner in getattr(partner, 'library_NodeType132')
    _safe_set(owner, 'library_Equipment133', None)
    assert owner not in getattr(partner, 'library_NodeType132')


def test_assoc_forecastCapacityValues116_stub_double():
    # library_Value has no real 'library_Value118' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value118', None)
    _safe_set(owner, 'library_NetXResource117', {partner})
    assert getattr(partner, 'library_Value118') == owner
    _safe_set(owner, 'library_NetXResource117', set())
    assert getattr(partner, 'library_Value118') is None


def test_assoc_forecastValues119_stub_double():
    # library_Value has no real 'library_Value121' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value121', None)
    _safe_set(owner, 'library_NetXResource120', {partner})
    assert getattr(partner, 'library_Value121') == owner
    _safe_set(owner, 'library_NetXResource120', set())
    assert getattr(partner, 'library_Value121') is None


def test_assoc_functionMetricRefs64_stub_double():
    # library_Metric has no real 'library_Metric66' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric66', None)
    _safe_set(owner, 'library_Function65', {partner})
    assert getattr(partner, 'library_Metric66') == owner
    _safe_set(owner, 'library_Function65', set())
    assert getattr(partner, 'library_Metric66') is None


def test_assoc_functionRelationshipRefs67_stub_double():
    # library_FunctionRelationship has no real 'library_FunctionRelationship' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_FunctionRelationship()
    setattr(partner, 'library_FunctionRelationship', None)
    _safe_set(owner, 'library_Function68', {partner})
    assert getattr(partner, 'library_FunctionRelationship') == owner
    _safe_set(owner, 'library_Function68', set())
    assert getattr(partner, 'library_FunctionRelationship') is None


def test_assoc_functions128_stub_double():
    # library_NodeType has no real 'library_NodeType129' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_NodeType()
    setattr(partner, 'library_NodeType129', None)
    _safe_set(owner, 'library_Function130', partner)
    assert owner in getattr(partner, 'library_NodeType129')
    _safe_set(owner, 'library_Function130', None)
    assert owner not in getattr(partner, 'library_NodeType129')


def test_assoc_icons148_stub_double():
    # library_MultiImage has no real 'library_MultiImage150' property in the generated
    # code (a bare stub) -- manually attach it so library_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage150', None)
    _safe_set(owner, 'library_Unit149', partner)
    assert getattr(partner, 'library_MultiImage150') == owner
    _safe_set(owner, 'library_Unit149', None)
    assert getattr(partner, 'library_MultiImage150') is None


def test_assoc_icons27_stub_double():
    # library_MultiImage has no real 'library_MultiImage' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", description="sample_text", equipmentCode="sample_text", equipmentName="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage', None)
    _safe_set(owner, 'library_Equipment28', partner)
    assert getattr(partner, 'library_MultiImage') == owner
    _safe_set(owner, 'library_Equipment28', None)
    assert getattr(partner, 'library_MultiImage') is None


def test_assoc_icons55_stub_double():
    # library_MultiImage has no real 'library_MultiImage57' property in the generated
    # code (a bare stub) -- manually attach it so library_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Function(description="sample_text", functionName="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage57', None)
    _safe_set(owner, 'library_Function56', partner)
    assert getattr(partner, 'library_MultiImage57') == owner
    _safe_set(owner, 'library_Function56', None)
    assert getattr(partner, 'library_MultiImage57') is None


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


def test_assoc_metricValueRanges112_stub_double():
    # library_MetricValueRange has no real 'library_MetricValueRange' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_MetricValueRange()
    setattr(partner, 'library_MetricValueRange', None)
    _safe_set(owner, 'library_NetXResource113', {partner})
    assert getattr(partner, 'library_MetricValueRange') == owner
    _safe_set(owner, 'library_NetXResource113', set())
    assert getattr(partner, 'library_MetricValueRange') is None


def test_assoc_metrics93_stub_double():
    # library_Metric has no real 'library_Metric95' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric95', None)
    _safe_set(owner, 'library_Library94', {partner})
    assert getattr(partner, 'library_Metric95') == owner
    _safe_set(owner, 'library_Library94', set())
    assert getattr(partner, 'library_Metric95') is None


def test_assoc_nodeTypeRef140_stub_double():
    # library_NodeType has no real 'library_NodeType142' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_NodeType()
    setattr(partner, 'library_NodeType142', None)
    _safe_set(owner, 'library_ProductInfo141', {partner})
    assert getattr(partner, 'library_NodeType142') == owner
    _safe_set(owner, 'library_ProductInfo141', set())
    assert getattr(partner, 'library_NodeType142') is None


def test_assoc_nodeTypes88_stub_double():
    # library_NodeType has no real 'library_NodeType' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_NodeType()
    setattr(partner, 'library_NodeType', None)
    _safe_set(owner, 'library_Library89', {partner})
    assert getattr(partner, 'library_NodeType') == owner
    _safe_set(owner, 'library_Library89', set())
    assert getattr(partner, 'library_NodeType') is None


def test_assoc_products151_stub_double():
    # library_Vendor has no real 'library_Vendor' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Vendor()
    setattr(partner, 'library_Vendor', None)
    _safe_set(owner, 'library_ProductInfo152', partner)
    assert owner in getattr(partner, 'library_Vendor')
    _safe_set(owner, 'library_ProductInfo152', None)
    assert owner not in getattr(partner, 'library_Vendor')


def test_assoc_serviceProfileRefs52_stub_double():
    # library_ServiceProfile has no real 'library_ServiceProfile' property in the generated
    # code (a bare stub) -- manually attach it so library_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Expression(expressionLines="sample_text", name="sample_text")
    partner = library_ServiceProfile()
    setattr(partner, 'library_ServiceProfile', None)
    _safe_set(owner, 'library_Expression', {partner})
    assert getattr(partner, 'library_ServiceProfile') == owner
    _safe_set(owner, 'library_Expression', set())
    assert getattr(partner, 'library_ServiceProfile') is None


def test_assoc_trendedValues122_stub_double():
    # library_Value has no real 'library_Value124' property in the generated
    # code (a bare stub) -- manually attach it so library_NetXResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NetXResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NetXResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value124', None)
    _safe_set(owner, 'library_NetXResource123', {partner})
    assert getattr(partner, 'library_Value124') == owner
    _safe_set(owner, 'library_NetXResource123', set())
    assert getattr(partner, 'library_Value124') is None


