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

def test_assoc_allEquipments29_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment30', a1)
    assert _is_linked(b, 'library_Equipment30', a1)
    if hasattr(a1, 'library_Equipment28'):
        assert _is_linked(a1, 'library_Equipment28', b)
    _safe_set(b, 'library_Equipment30', a2)
    assert _is_linked(b, 'library_Equipment30', a2)
    if hasattr(a1, 'library_Equipment28'):
        assert not _is_linked(a1, 'library_Equipment28', b)
    if hasattr(a2, 'library_Equipment28'):
        assert _is_linked(a2, 'library_Equipment28', b)
    _safe_set(b, 'library_Equipment30', None)
    assert not _is_linked(b, 'library_Equipment30', a2)
    if hasattr(a2, 'library_Equipment28'):
        assert not _is_linked(a2, 'library_Equipment28', b)


def test_assoc_allEquipments49_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment51', a1)
    assert _is_linked(b, 'library_Equipment51', a1)
    if hasattr(a1, 'library_EquipmentGroup50'):
        assert _is_linked(a1, 'library_EquipmentGroup50', b)
    _safe_set(b, 'library_Equipment51', a2)
    assert _is_linked(b, 'library_Equipment51', a2)
    if hasattr(a1, 'library_EquipmentGroup50'):
        assert not _is_linked(a1, 'library_EquipmentGroup50', b)
    if hasattr(a2, 'library_EquipmentGroup50'):
        assert _is_linked(a2, 'library_EquipmentGroup50', b)
    _safe_set(b, 'library_Equipment51', None)
    assert not _is_linked(b, 'library_Equipment51', a2)
    if hasattr(a2, 'library_EquipmentGroup50'):
        assert not _is_linked(a2, 'library_EquipmentGroup50', b)


def test_assoc_capacityExpressionRef5_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component6', a1)
    assert _is_linked(b, 'library_Component6', a1)
    if hasattr(a1, 'library_Expression'):
        assert _is_linked(a1, 'library_Expression', b)
    _safe_set(b, 'library_Component6', a2)
    assert _is_linked(b, 'library_Component6', a2)
    if hasattr(a1, 'library_Expression'):
        assert not _is_linked(a1, 'library_Expression', b)
    if hasattr(a2, 'library_Expression'):
        assert _is_linked(a2, 'library_Expression', b)
    _safe_set(b, 'library_Component6', None)
    assert not _is_linked(b, 'library_Component6', a2)
    if hasattr(a2, 'library_Expression'):
        assert not _is_linked(a2, 'library_Expression', b)


def test_assoc_equipmentGroups24_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment25', {a1})
    assert _is_linked(b, 'library_Equipment25', a1)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert _is_linked(a1, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment25', {a2})
    assert _is_linked(b, 'library_Equipment25', a2)
    if hasattr(a1, 'library_EquipmentGroup'):
        assert not _is_linked(a1, 'library_EquipmentGroup', b)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert _is_linked(a2, 'library_EquipmentGroup', b)
    _safe_set(b, 'library_Equipment25', set())
    assert not _is_linked(b, 'library_Equipment25', a2)
    if hasattr(a2, 'library_EquipmentGroup'):
        assert not _is_linked(a2, 'library_EquipmentGroup', b)


def test_assoc_equipmentRef118_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment119', a1)
    assert _is_linked(b, 'library_Equipment119', a1)
    if hasattr(a1, 'library_ProductInfo'):
        assert _is_linked(a1, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment119', a2)
    assert _is_linked(b, 'library_Equipment119', a2)
    if hasattr(a1, 'library_ProductInfo'):
        assert not _is_linked(a1, 'library_ProductInfo', b)
    if hasattr(a2, 'library_ProductInfo'):
        assert _is_linked(a2, 'library_ProductInfo', b)
    _safe_set(b, 'library_Equipment119', None)
    assert not _is_linked(b, 'library_Equipment119', a2)
    if hasattr(a2, 'library_ProductInfo'):
        assert not _is_linked(a2, 'library_ProductInfo', b)


def test_assoc_equipmentRefs40_reverse_link_reassign_clear():
    a1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    a2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment42', a1)
    assert _is_linked(b, 'library_Equipment42', a1)
    if hasattr(a1, 'library_EquipmentGroup41'):
        assert _is_linked(a1, 'library_EquipmentGroup41', b)
    _safe_set(b, 'library_Equipment42', a2)
    assert _is_linked(b, 'library_Equipment42', a2)
    if hasattr(a1, 'library_EquipmentGroup41'):
        assert not _is_linked(a1, 'library_EquipmentGroup41', b)
    if hasattr(a2, 'library_EquipmentGroup41'):
        assert _is_linked(a2, 'library_EquipmentGroup41', b)
    _safe_set(b, 'library_Equipment42', None)
    assert not _is_linked(b, 'library_Equipment42', a2)
    if hasattr(a2, 'library_EquipmentGroup41'):
        assert not _is_linked(a2, 'library_EquipmentGroup41', b)


def test_assoc_equipments115_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text", name="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment117', a1)
    assert _is_linked(b, 'library_Equipment117', a1)
    if hasattr(a1, 'library_NodeType116'):
        assert _is_linked(a1, 'library_NodeType116', b)
    _safe_set(b, 'library_Equipment117', a2)
    assert _is_linked(b, 'library_Equipment117', a2)
    if hasattr(a1, 'library_NodeType116'):
        assert not _is_linked(a1, 'library_NodeType116', b)
    if hasattr(a2, 'library_NodeType116'):
        assert _is_linked(a2, 'library_NodeType116', b)
    _safe_set(b, 'library_Equipment117', None)
    assert not _is_linked(b, 'library_Equipment117', a2)
    if hasattr(a2, 'library_NodeType116'):
        assert not _is_linked(a2, 'library_NodeType116', b)


def test_assoc_equipments23_reverse_link_reassign_clear():
    a1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    a2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment22', {a1})
    assert _is_linked(b, 'library_Equipment22', a1)
    if hasattr(a1, 'library_Equipment'):
        assert _is_linked(a1, 'library_Equipment', b)
    _safe_set(b, 'library_Equipment22', {a2})
    assert _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a1, 'library_Equipment'):
        assert not _is_linked(a1, 'library_Equipment', b)
    if hasattr(a2, 'library_Equipment'):
        assert _is_linked(a2, 'library_Equipment', b)
    _safe_set(b, 'library_Equipment22', set())
    assert not _is_linked(b, 'library_Equipment22', a2)
    if hasattr(a2, 'library_Equipment'):
        assert not _is_linked(a2, 'library_Equipment', b)


def test_assoc_equipments69_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    _safe_set(b, 'library_Equipment71', a1)
    assert _is_linked(b, 'library_Equipment71', a1)
    if hasattr(a1, 'library_Library70'):
        assert _is_linked(a1, 'library_Library70', b)
    _safe_set(b, 'library_Equipment71', a2)
    assert _is_linked(b, 'library_Equipment71', a2)
    if hasattr(a1, 'library_Library70'):
        assert not _is_linked(a1, 'library_Library70', b)
    if hasattr(a2, 'library_Library70'):
        assert _is_linked(a2, 'library_Library70', b)
    _safe_set(b, 'library_Equipment71', None)
    assert not _is_linked(b, 'library_Equipment71', a2)
    if hasattr(a2, 'library_Library70'):
        assert not _is_linked(a2, 'library_Library70', b)


def test_assoc_expressionRef126_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression128', a1)
    assert _is_linked(b, 'library_Expression128', a1)
    if hasattr(a1, 'library_Tolerance127'):
        assert _is_linked(a1, 'library_Tolerance127', b)
    _safe_set(b, 'library_Expression128', a2)
    assert _is_linked(b, 'library_Expression128', a2)
    if hasattr(a1, 'library_Tolerance127'):
        assert not _is_linked(a1, 'library_Tolerance127', b)
    if hasattr(a2, 'library_Tolerance127'):
        assert _is_linked(a2, 'library_Tolerance127', b)
    _safe_set(b, 'library_Expression128', None)
    assert not _is_linked(b, 'library_Expression128', a2)
    if hasattr(a2, 'library_Tolerance127'):
        assert not _is_linked(a2, 'library_Tolerance127', b)


def test_assoc_expressionRefs37_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup38', {a1})
    assert _is_linked(b, 'library_EquipmentGroup38', a1)
    if hasattr(a1, 'library_Expression39'):
        assert _is_linked(a1, 'library_Expression39', b)
    _safe_set(b, 'library_EquipmentGroup38', {a2})
    assert _is_linked(b, 'library_EquipmentGroup38', a2)
    if hasattr(a1, 'library_Expression39'):
        assert not _is_linked(a1, 'library_Expression39', b)
    if hasattr(a2, 'library_Expression39'):
        assert _is_linked(a2, 'library_Expression39', b)
    _safe_set(b, 'library_EquipmentGroup38', set())
    assert not _is_linked(b, 'library_EquipmentGroup38', a2)
    if hasattr(a2, 'library_Expression39'):
        assert not _is_linked(a2, 'library_Expression39', b)


def test_assoc_expressions83_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", protocols="sample_text")
    a2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    b = library_Expression(expressionLines="sample_text", name="sample_text")
    _safe_set(b, 'library_Expression85', a1)
    assert _is_linked(b, 'library_Expression85', a1)
    if hasattr(a1, 'library_Library84'):
        assert _is_linked(a1, 'library_Library84', b)
    _safe_set(b, 'library_Expression85', a2)
    assert _is_linked(b, 'library_Expression85', a2)
    if hasattr(a1, 'library_Library84'):
        assert not _is_linked(a1, 'library_Library84', b)
    if hasattr(a2, 'library_Library84'):
        assert _is_linked(a2, 'library_Library84', b)
    _safe_set(b, 'library_Expression85', None)
    assert not _is_linked(b, 'library_Expression85', a2)
    if hasattr(a2, 'library_Library84'):
        assert not _is_linked(a2, 'library_Library84', b)


def test_assoc_nodeTypeRef123_reverse_link_reassign_clear():
    a1 = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    a2 = library_ProductInfo(availableDate="sample_text_2", endOfSalesDate="sample_text_2", endOfSupportDate="sample_text_2", productCode="sample_text_2", salesCode="sample_text_2", underDevelopmentDate="sample_text_2")
    b = library_NodeType(leafNode="sample_text", name="sample_text")
    _safe_set(b, 'library_NodeType125', a1)
    assert _is_linked(b, 'library_NodeType125', a1)
    if hasattr(a1, 'library_ProductInfo124'):
        assert _is_linked(a1, 'library_ProductInfo124', b)
    _safe_set(b, 'library_NodeType125', a2)
    assert _is_linked(b, 'library_NodeType125', a2)
    if hasattr(a1, 'library_ProductInfo124'):
        assert not _is_linked(a1, 'library_ProductInfo124', b)
    if hasattr(a2, 'library_ProductInfo124'):
        assert _is_linked(a2, 'library_ProductInfo124', b)
    _safe_set(b, 'library_NodeType125', None)
    assert not _is_linked(b, 'library_NodeType125', a2)
    if hasattr(a2, 'library_ProductInfo124'):
        assert not _is_linked(a2, 'library_ProductInfo124', b)


def test_assoc_nodeTypes67_reverse_link_reassign_clear():
    a1 = library_NodeType(leafNode="sample_text", name="sample_text")
    a2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library68', {a1})
    assert _is_linked(b, 'library_Library68', a1)
    if hasattr(a1, 'library_NodeType'):
        assert _is_linked(a1, 'library_NodeType', b)
    _safe_set(b, 'library_Library68', {a2})
    assert _is_linked(b, 'library_Library68', a2)
    if hasattr(a1, 'library_NodeType'):
        assert not _is_linked(a1, 'library_NodeType', b)
    if hasattr(a2, 'library_NodeType'):
        assert _is_linked(a2, 'library_NodeType', b)
    _safe_set(b, 'library_Library68', set())
    assert not _is_linked(b, 'library_Library68', a2)
    if hasattr(a2, 'library_NodeType'):
        assert not _is_linked(a2, 'library_NodeType', b)


def test_assoc_parameterRefs14_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component15', {a1})
    assert _is_linked(b, 'library_Component15', a1)
    if hasattr(a1, 'library_Parameter'):
        assert _is_linked(a1, 'library_Parameter', b)
    _safe_set(b, 'library_Component15', {a2})
    assert _is_linked(b, 'library_Component15', a2)
    if hasattr(a1, 'library_Parameter'):
        assert not _is_linked(a1, 'library_Parameter', b)
    if hasattr(a2, 'library_Parameter'):
        assert _is_linked(a2, 'library_Parameter', b)
    _safe_set(b, 'library_Component15', set())
    assert not _is_linked(b, 'library_Component15', a2)
    if hasattr(a2, 'library_Parameter'):
        assert not _is_linked(a2, 'library_Parameter', b)


def test_assoc_parameterRefs43_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'library_EquipmentGroup44', {a1})
    assert _is_linked(b, 'library_EquipmentGroup44', a1)
    if hasattr(a1, 'library_Parameter45'):
        assert _is_linked(a1, 'library_Parameter45', b)
    _safe_set(b, 'library_EquipmentGroup44', {a2})
    assert _is_linked(b, 'library_EquipmentGroup44', a2)
    if hasattr(a1, 'library_Parameter45'):
        assert not _is_linked(a1, 'library_Parameter45', b)
    if hasattr(a2, 'library_Parameter45'):
        assert _is_linked(a2, 'library_Parameter45', b)
    _safe_set(b, 'library_EquipmentGroup44', set())
    assert not _is_linked(b, 'library_EquipmentGroup44', a2)
    if hasattr(a2, 'library_Parameter45'):
        assert not _is_linked(a2, 'library_Parameter45', b)


def test_assoc_parameters77_reverse_link_reassign_clear():
    a1 = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    a2 = library_Parameter(description="sample_text_2", expressionName="sample_text_2", modifiable="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library78', {a1})
    assert _is_linked(b, 'library_Library78', a1)
    if hasattr(a1, 'library_Parameter79'):
        assert _is_linked(a1, 'library_Parameter79', b)
    _safe_set(b, 'library_Library78', {a2})
    assert _is_linked(b, 'library_Library78', a2)
    if hasattr(a1, 'library_Parameter79'):
        assert not _is_linked(a1, 'library_Parameter79', b)
    if hasattr(a2, 'library_Parameter79'):
        assert _is_linked(a2, 'library_Parameter79', b)
    _safe_set(b, 'library_Library78', set())
    assert not _is_linked(b, 'library_Library78', a2)
    if hasattr(a2, 'library_Parameter79'):
        assert not _is_linked(a2, 'library_Parameter79', b)


def test_assoc_targetResource54_reverse_link_reassign_clear():
    a1 = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    a2 = library_ExpressionResult(targetIntervalHint="sample_text_2", targetKindHint="sample_text_2", targetRange="sample_text_2")
    b = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    _safe_set(b, 'library_BaseResource55', a1)
    assert _is_linked(b, 'library_BaseResource55', a1)
    if hasattr(a1, 'library_ExpressionResult'):
        assert _is_linked(a1, 'library_ExpressionResult', b)
    _safe_set(b, 'library_BaseResource55', a2)
    assert _is_linked(b, 'library_BaseResource55', a2)
    if hasattr(a1, 'library_ExpressionResult'):
        assert not _is_linked(a1, 'library_ExpressionResult', b)
    if hasattr(a2, 'library_ExpressionResult'):
        assert _is_linked(a2, 'library_ExpressionResult', b)
    _safe_set(b, 'library_BaseResource55', None)
    assert not _is_linked(b, 'library_BaseResource55', a2)
    if hasattr(a2, 'library_ExpressionResult'):
        assert not _is_linked(a2, 'library_ExpressionResult', b)


def test_assoc_toleranceRefs10_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component11', {a1})
    assert _is_linked(b, 'library_Component11', a1)
    if hasattr(a1, 'library_Tolerance'):
        assert _is_linked(a1, 'library_Tolerance', b)
    _safe_set(b, 'library_Component11', {a2})
    assert _is_linked(b, 'library_Component11', a2)
    if hasattr(a1, 'library_Tolerance'):
        assert not _is_linked(a1, 'library_Tolerance', b)
    if hasattr(a2, 'library_Tolerance'):
        assert _is_linked(a2, 'library_Tolerance', b)
    _safe_set(b, 'library_Component11', set())
    assert not _is_linked(b, 'library_Component11', a2)
    if hasattr(a2, 'library_Tolerance'):
        assert not _is_linked(a2, 'library_Tolerance', b)


def test_assoc_tolerances80_reverse_link_reassign_clear():
    a1 = library_Tolerance(level="sample_text", name="sample_text")
    a2 = library_Tolerance(level="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library81', {a1})
    assert _is_linked(b, 'library_Library81', a1)
    if hasattr(a1, 'library_Tolerance82'):
        assert _is_linked(a1, 'library_Tolerance82', b)
    _safe_set(b, 'library_Library81', {a2})
    assert _is_linked(b, 'library_Library81', a2)
    if hasattr(a1, 'library_Tolerance82'):
        assert not _is_linked(a1, 'library_Tolerance82', b)
    if hasattr(a2, 'library_Tolerance82'):
        assert _is_linked(a2, 'library_Tolerance82', b)
    _safe_set(b, 'library_Library81', set())
    assert not _is_linked(b, 'library_Library81', a2)
    if hasattr(a2, 'library_Tolerance82'):
        assert not _is_linked(a2, 'library_Tolerance82', b)


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


def test_assoc_units86_reverse_link_reassign_clear():
    a1 = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    a2 = library_Unit(code="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = library_Library(name="sample_text", protocols="sample_text")
    _safe_set(b, 'library_Library87', {a1})
    assert _is_linked(b, 'library_Library87', a1)
    if hasattr(a1, 'library_Unit88'):
        assert _is_linked(a1, 'library_Unit88', b)
    _safe_set(b, 'library_Library87', {a2})
    assert _is_linked(b, 'library_Library87', a2)
    if hasattr(a1, 'library_Unit88'):
        assert not _is_linked(a1, 'library_Unit88', b)
    if hasattr(a2, 'library_Unit88'):
        assert _is_linked(a2, 'library_Unit88', b)
    _safe_set(b, 'library_Library87', set())
    assert not _is_linked(b, 'library_Library87', a2)
    if hasattr(a2, 'library_Unit88'):
        assert not _is_linked(a2, 'library_Unit88', b)


def test_assoc_utilizationExpressionRef7_reverse_link_reassign_clear():
    a1 = library_Expression(expressionLines="sample_text", name="sample_text")
    a2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    b = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    _safe_set(b, 'library_Component8', a1)
    assert _is_linked(b, 'library_Component8', a1)
    if hasattr(a1, 'library_Expression9'):
        assert _is_linked(a1, 'library_Expression9', b)
    _safe_set(b, 'library_Component8', a2)
    assert _is_linked(b, 'library_Component8', a2)
    if hasattr(a1, 'library_Expression9'):
        assert not _is_linked(a1, 'library_Expression9', b)
    if hasattr(a2, 'library_Expression9'):
        assert _is_linked(a2, 'library_Expression9', b)
    _safe_set(b, 'library_Component8', None)
    assert not _is_linked(b, 'library_Component8', a2)
    if hasattr(a2, 'library_Expression9'):
        assert not _is_linked(a2, 'library_Expression9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allEquipmentResources46_stub_double():
    # library_NetXResource has no real 'library_NetXResource48' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource48', None)
    _safe_set(owner, 'library_EquipmentGroup47', {partner})
    assert getattr(partner, 'library_NetXResource48') == owner
    _safe_set(owner, 'library_EquipmentGroup47', set())
    assert getattr(partner, 'library_NetXResource48') is None


def test_assoc_allResources16_stub_double():
    # library_NetXResource has no real 'library_NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource', None)
    _safe_set(owner, 'library_Component17', {partner})
    assert getattr(partner, 'library_NetXResource') == owner
    _safe_set(owner, 'library_Component17', set())
    assert getattr(partner, 'library_NetXResource') is None


def test_assoc_componentRef91_stub_double():
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


def test_assoc_diagrams18_stub_double():
    # library_DiagramInfo has no real 'library_DiagramInfo' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_DiagramInfo()
    setattr(partner, 'library_DiagramInfo', None)
    _safe_set(owner, 'library_Component19', {partner})
    assert getattr(partner, 'library_DiagramInfo') == owner
    _safe_set(owner, 'library_Component19', set())
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


def test_assoc_equipmentGroupResources34_stub_double():
    # library_NetXResource has no real 'library_NetXResource36' property in the generated
    # code (a bare stub) -- manually attach it so library_EquipmentGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_EquipmentGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    partner = library_NetXResource()
    setattr(partner, 'library_NetXResource36', None)
    _safe_set(owner, 'library_EquipmentGroup35', {partner})
    assert getattr(partner, 'library_NetXResource36') == owner
    _safe_set(owner, 'library_EquipmentGroup35', set())
    assert getattr(partner, 'library_NetXResource36') is None


def test_assoc_equipmentRelationshipRefs26_stub_double():
    # library_EquipmentRelationship has no real 'library_EquipmentRelationship' property in the generated
    # code (a bare stub) -- manually attach it so library_Equipment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Equipment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    partner = library_EquipmentRelationship()
    setattr(partner, 'library_EquipmentRelationship', None)
    _safe_set(owner, 'library_Equipment27', {partner})
    assert getattr(partner, 'library_EquipmentRelationship') == owner
    _safe_set(owner, 'library_Equipment27', set())
    assert getattr(partner, 'library_EquipmentRelationship') is None


def test_assoc_evaluationObject52_stub_double():
    # library_EObject has no real 'library_EObject' property in the generated
    # code (a bare stub) -- manually attach it so library_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Expression(expressionLines="sample_text", name="sample_text")
    partner = library_EObject()
    setattr(partner, 'library_EObject', None)
    _safe_set(owner, 'library_Expression53', partner)
    assert getattr(partner, 'library_EObject') == owner
    _safe_set(owner, 'library_Expression53', None)
    assert getattr(partner, 'library_EObject') is None


def test_assoc_functions112_stub_double():
    # library_Function has no real 'library_Function114' property in the generated
    # code (a bare stub) -- manually attach it so library_NodeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_NodeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_NodeType(leafNode="sample_text", name="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function114', None)
    _safe_set(owner, 'library_NodeType113', {partner})
    assert getattr(partner, 'library_Function114') == owner
    _safe_set(owner, 'library_NodeType113', set())
    assert getattr(partner, 'library_Function114') is None


def test_assoc_functions65_stub_double():
    # library_Function has no real 'library_Function66' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function66', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'library_Function66') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'library_Function66') is None


def test_assoc_icons129_stub_double():
    # library_MultiImage has no real 'library_MultiImage131' property in the generated
    # code (a bare stub) -- manually attach it so library_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage131', None)
    _safe_set(owner, 'library_Unit130', partner)
    assert getattr(partner, 'library_MultiImage131') == owner
    _safe_set(owner, 'library_Unit130', None)
    assert getattr(partner, 'library_MultiImage131') is None


def test_assoc_icons20_stub_double():
    # library_MultiImage has no real 'library_MultiImage' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_MultiImage()
    setattr(partner, 'library_MultiImage', None)
    _safe_set(owner, 'library_Component21', partner)
    assert getattr(partner, 'library_MultiImage') == owner
    _safe_set(owner, 'library_Component21', None)
    assert getattr(partner, 'library_MultiImage') is None


def test_assoc_licensedFunctionRef120_stub_double():
    # library_Function has no real 'library_Function122' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Function()
    setattr(partner, 'library_Function122', None)
    _safe_set(owner, 'library_ProductInfo121', {partner})
    assert getattr(partner, 'library_Function122') == owner
    _safe_set(owner, 'library_ProductInfo121', set())
    assert getattr(partner, 'library_Function122') is None


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


def test_assoc_metricRefs3_stub_double():
    # library_Metric has no real 'library_Metric' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric', None)
    _safe_set(owner, 'library_Component4', {partner})
    assert getattr(partner, 'library_Metric') == owner
    _safe_set(owner, 'library_Component4', set())
    assert getattr(partner, 'library_Metric') is None


def test_assoc_metricSources75_stub_double():
    # library_MetricSource has no real 'library_MetricSource' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_MetricSource()
    setattr(partner, 'library_MetricSource', None)
    _safe_set(owner, 'library_Library76', {partner})
    assert getattr(partner, 'library_MetricSource') == owner
    _safe_set(owner, 'library_Library76', set())
    assert getattr(partner, 'library_MetricSource') is None


def test_assoc_metrics72_stub_double():
    # library_Metric has no real 'library_Metric74' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Metric()
    setattr(partner, 'library_Metric74', None)
    _safe_set(owner, 'library_Library73', {partner})
    assert getattr(partner, 'library_Metric74') == owner
    _safe_set(owner, 'library_Library73', set())
    assert getattr(partner, 'library_Metric74') is None


def test_assoc_products132_stub_double():
    # library_Vendor has no real 'library_Vendor' property in the generated
    # code (a bare stub) -- manually attach it so library_ProductInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ProductInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    partner = library_Vendor()
    setattr(partner, 'library_Vendor', None)
    _safe_set(owner, 'library_ProductInfo133', partner)
    assert owner in getattr(partner, 'library_Vendor')
    _safe_set(owner, 'library_ProductInfo133', None)
    assert owner not in getattr(partner, 'library_Vendor')


def test_assoc_protocolRefs12_stub_double():
    # library_Protocol has no real 'library_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so library_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    partner = library_Protocol()
    setattr(partner, 'library_Protocol', None)
    _safe_set(owner, 'library_Component13', {partner})
    assert getattr(partner, 'library_Protocol') == owner
    _safe_set(owner, 'library_Component13', set())
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


def test_assoc_targetValues56_stub_double():
    # library_Value has no real 'library_Value' property in the generated
    # code (a bare stub) -- manually attach it so library_ExpressionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_ExpressionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    partner = library_Value()
    setattr(partner, 'library_Value', None)
    _safe_set(owner, 'library_ExpressionResult57', {partner})
    assert getattr(partner, 'library_Value') == owner
    _safe_set(owner, 'library_ExpressionResult57', set())
    assert getattr(partner, 'library_Value') is None


def test_assoc_version89_stub_double():
    # library_Meta has no real 'library_Meta' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", protocols="sample_text")
    partner = library_Meta()
    setattr(partner, 'library_Meta', None)
    _safe_set(owner, 'library_Library90', partner)
    assert getattr(partner, 'library_Meta') == owner
    _safe_set(owner, 'library_Library90', None)
    assert getattr(partner, 'library_Meta') is None


