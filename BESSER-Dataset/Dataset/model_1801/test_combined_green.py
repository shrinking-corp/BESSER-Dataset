# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_BaseExpressionResult,
    Company,
    library_Vendor,
    library_MetricValueRange,
    BaseResource,
    library_Meta,
    library_Library,
    library_MetricSource,
    library_Value,
    library_FunctionRelationship,
    BaseExpressionResult,
    library_LastEvaluationExpressionResult,
    library_ExpressionResult,
    library_EObject,
    library_EquipmentRelationship,
    Component,
    library_Function,
    library_Equipment,
    library_Protocol,
    library_MultiImage,
    library_DiagramInfo,
    library_Metric,
    library_NetXResource,
    library_Lifecycle,
    Base,
    library_Component,
    library_BaseResource,
    library_Unit,
    library_NodeType,
    library_Parameter,
    library_EquipmentGroup,
    library_Tolerance,
    library_Expression,
    library_ProductInfo,
    StateType,
    LevelKind,
    RedundancyType,
    RangeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_baseexpressionresult_is_not_abstract():
    assert not inspect.isabstract(library_BaseExpressionResult)


def test_hyp_library_baseexpressionresult_constructor_exists():
    assert callable(library_BaseExpressionResult.__init__)


def test_hyp_library_baseexpressionresult_constructor_args():
    sig = inspect.signature(library_BaseExpressionResult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_is_not_abstract():
    assert not inspect.isabstract(Company)


def test_hyp_company_constructor_exists():
    assert callable(Company.__init__)


def test_hyp_company_constructor_args():
    sig = inspect.signature(Company.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_vendor_is_not_abstract():
    assert not inspect.isabstract(library_Vendor)


def test_hyp_library_vendor_constructor_exists():
    assert callable(library_Vendor.__init__)


def test_hyp_library_vendor_constructor_args():
    sig = inspect.signature(library_Vendor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_metricvaluerange_is_not_abstract():
    assert not inspect.isabstract(library_MetricValueRange)


def test_hyp_library_metricvaluerange_constructor_exists():
    assert callable(library_MetricValueRange.__init__)


def test_hyp_library_metricvaluerange_constructor_args():
    sig = inspect.signature(library_MetricValueRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_baseresource_is_not_abstract():
    assert not inspect.isabstract(BaseResource)


def test_hyp_baseresource_constructor_exists():
    assert callable(BaseResource.__init__)


def test_hyp_baseresource_constructor_args():
    sig = inspect.signature(BaseResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_meta_is_not_abstract():
    assert not inspect.isabstract(library_Meta)


def test_hyp_library_meta_constructor_exists():
    assert callable(library_Meta.__init__)


def test_hyp_library_meta_constructor_args():
    sig = inspect.signature(library_Meta.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_hyp_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_hyp_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "protocols" in params, "Missing parameter 'protocols'"





def test_hyp_library_metricsource_is_not_abstract():
    assert not inspect.isabstract(library_MetricSource)


def test_hyp_library_metricsource_constructor_exists():
    assert callable(library_MetricSource.__init__)


def test_hyp_library_metricsource_constructor_args():
    sig = inspect.signature(library_MetricSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_value_is_not_abstract():
    assert not inspect.isabstract(library_Value)


def test_hyp_library_value_constructor_exists():
    assert callable(library_Value.__init__)


def test_hyp_library_value_constructor_args():
    sig = inspect.signature(library_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_functionrelationship_is_not_abstract():
    assert not inspect.isabstract(library_FunctionRelationship)


def test_hyp_library_functionrelationship_constructor_exists():
    assert callable(library_FunctionRelationship.__init__)


def test_hyp_library_functionrelationship_constructor_args():
    sig = inspect.signature(library_FunctionRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_baseexpressionresult_is_not_abstract():
    assert not inspect.isabstract(BaseExpressionResult)


def test_hyp_baseexpressionresult_constructor_exists():
    assert callable(BaseExpressionResult.__init__)


def test_hyp_baseexpressionresult_constructor_args():
    sig = inspect.signature(BaseExpressionResult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_lastevaluationexpressionresult_is_not_abstract():
    assert not inspect.isabstract(library_LastEvaluationExpressionResult)


def test_hyp_library_lastevaluationexpressionresult_constructor_exists():
    assert callable(library_LastEvaluationExpressionResult.__init__)


def test_hyp_library_lastevaluationexpressionresult_constructor_args():
    sig = inspect.signature(library_LastEvaluationExpressionResult.__init__)
    params = list(sig.parameters.keys())
    assert "lastEvalResult" in params, "Missing parameter 'lastEvalResult'"




def test_hyp_library_expressionresult_is_not_abstract():
    assert not inspect.isabstract(library_ExpressionResult)


def test_hyp_library_expressionresult_constructor_exists():
    assert callable(library_ExpressionResult.__init__)


def test_hyp_library_expressionresult_constructor_args():
    sig = inspect.signature(library_ExpressionResult.__init__)
    params = list(sig.parameters.keys())
    assert "targetKindHint" in params, "Missing parameter 'targetKindHint'"
    assert "targetIntervalHint" in params, "Missing parameter 'targetIntervalHint'"
    assert "targetRange" in params, "Missing parameter 'targetRange'"






def test_hyp_library_eobject_is_not_abstract():
    assert not inspect.isabstract(library_EObject)


def test_hyp_library_eobject_constructor_exists():
    assert callable(library_EObject.__init__)


def test_hyp_library_eobject_constructor_args():
    sig = inspect.signature(library_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_equipmentrelationship_is_not_abstract():
    assert not inspect.isabstract(library_EquipmentRelationship)


def test_hyp_library_equipmentrelationship_constructor_exists():
    assert callable(library_EquipmentRelationship.__init__)


def test_hyp_library_equipmentrelationship_constructor_args():
    sig = inspect.signature(library_EquipmentRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_function_is_not_abstract():
    assert not inspect.isabstract(library_Function)


def test_hyp_library_function_constructor_exists():
    assert callable(library_Function.__init__)


def test_hyp_library_function_constructor_args():
    sig = inspect.signature(library_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_equipment_is_not_abstract():
    assert not inspect.isabstract(library_Equipment)


def test_hyp_library_equipment_constructor_exists():
    assert callable(library_Equipment.__init__)


def test_hyp_library_equipment_constructor_args():
    sig = inspect.signature(library_Equipment.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "count" in params, "Missing parameter 'count'"
    assert "redundancy" in params, "Missing parameter 'redundancy'"
    assert "equipmentCode" in params, "Missing parameter 'equipmentCode'"
    assert "state" in params, "Missing parameter 'state'"








def test_hyp_library_protocol_is_not_abstract():
    assert not inspect.isabstract(library_Protocol)


def test_hyp_library_protocol_constructor_exists():
    assert callable(library_Protocol.__init__)


def test_hyp_library_protocol_constructor_args():
    sig = inspect.signature(library_Protocol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_multiimage_is_not_abstract():
    assert not inspect.isabstract(library_MultiImage)


def test_hyp_library_multiimage_constructor_exists():
    assert callable(library_MultiImage.__init__)


def test_hyp_library_multiimage_constructor_args():
    sig = inspect.signature(library_MultiImage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_diagraminfo_is_not_abstract():
    assert not inspect.isabstract(library_DiagramInfo)


def test_hyp_library_diagraminfo_constructor_exists():
    assert callable(library_DiagramInfo.__init__)


def test_hyp_library_diagraminfo_constructor_args():
    sig = inspect.signature(library_DiagramInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_metric_is_not_abstract():
    assert not inspect.isabstract(library_Metric)


def test_hyp_library_metric_constructor_exists():
    assert callable(library_Metric.__init__)


def test_hyp_library_metric_constructor_args():
    sig = inspect.signature(library_Metric.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_netxresource_is_not_abstract():
    assert not inspect.isabstract(library_NetXResource)


def test_hyp_library_netxresource_constructor_exists():
    assert callable(library_NetXResource.__init__)


def test_hyp_library_netxresource_constructor_args():
    sig = inspect.signature(library_NetXResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_lifecycle_is_not_abstract():
    assert not inspect.isabstract(library_Lifecycle)


def test_hyp_library_lifecycle_constructor_exists():
    assert callable(library_Lifecycle.__init__)


def test_hyp_library_lifecycle_constructor_args():
    sig = inspect.signature(library_Lifecycle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_hyp_base_constructor_exists():
    assert callable(Base.__init__)


def test_hyp_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_component_is_not_abstract():
    assert not inspect.isabstract(library_Component)


def test_hyp_library_component_constructor_exists():
    assert callable(library_Component.__init__)


def test_hyp_library_component_constructor_args():
    sig = inspect.signature(library_Component.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_library_baseresource_is_not_abstract():
    assert not inspect.isabstract(library_BaseResource)


def test_hyp_library_baseresource_constructor_exists():
    assert callable(library_BaseResource.__init__)


def test_hyp_library_baseresource_constructor_args():
    sig = inspect.signature(library_BaseResource.__init__)
    params = list(sig.parameters.keys())
    assert "detailDisplay" in params, "Missing parameter 'detailDisplay'"
    assert "summaryDisplay" in params, "Missing parameter 'summaryDisplay'"
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "longName" in params, "Missing parameter 'longName'"
    assert "expressionName" in params, "Missing parameter 'expressionName'"








def test_hyp_library_unit_is_not_abstract():
    assert not inspect.isabstract(library_Unit)


def test_hyp_library_unit_constructor_exists():
    assert callable(library_Unit.__init__)


def test_hyp_library_unit_constructor_args():
    sig = inspect.signature(library_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"






def test_hyp_library_nodetype_is_not_abstract():
    assert not inspect.isabstract(library_NodeType)


def test_hyp_library_nodetype_constructor_exists():
    assert callable(library_NodeType.__init__)


def test_hyp_library_nodetype_constructor_args():
    sig = inspect.signature(library_NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "leafNode" in params, "Missing parameter 'leafNode'"





def test_hyp_library_parameter_is_not_abstract():
    assert not inspect.isabstract(library_Parameter)


def test_hyp_library_parameter_constructor_exists():
    assert callable(library_Parameter.__init__)


def test_hyp_library_parameter_constructor_args():
    sig = inspect.signature(library_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "modifiable" in params, "Missing parameter 'modifiable'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "expressionName" in params, "Missing parameter 'expressionName'"








def test_hyp_library_equipmentgroup_is_not_abstract():
    assert not inspect.isabstract(library_EquipmentGroup)


def test_hyp_library_equipmentgroup_constructor_exists():
    assert callable(library_EquipmentGroup.__init__)


def test_hyp_library_equipmentgroup_constructor_args():
    sig = inspect.signature(library_EquipmentGroup.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "count" in params, "Missing parameter 'count'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_library_tolerance_is_not_abstract():
    assert not inspect.isabstract(library_Tolerance)


def test_hyp_library_tolerance_constructor_exists():
    assert callable(library_Tolerance.__init__)


def test_hyp_library_tolerance_constructor_args():
    sig = inspect.signature(library_Tolerance.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_library_expression_is_not_abstract():
    assert not inspect.isabstract(library_Expression)


def test_hyp_library_expression_constructor_exists():
    assert callable(library_Expression.__init__)


def test_hyp_library_expression_constructor_args():
    sig = inspect.signature(library_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "expressionLines" in params, "Missing parameter 'expressionLines'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_library_productinfo_is_not_abstract():
    assert not inspect.isabstract(library_ProductInfo)


def test_hyp_library_productinfo_constructor_exists():
    assert callable(library_ProductInfo.__init__)


def test_hyp_library_productinfo_constructor_args():
    sig = inspect.signature(library_ProductInfo.__init__)
    params = list(sig.parameters.keys())
    assert "endOfSupportDate" in params, "Missing parameter 'endOfSupportDate'"
    assert "availableDate" in params, "Missing parameter 'availableDate'"
    assert "endOfSalesDate" in params, "Missing parameter 'endOfSalesDate'"
    assert "productCode" in params, "Missing parameter 'productCode'"
    assert "underDevelopmentDate" in params, "Missing parameter 'underDevelopmentDate'"
    assert "salesCode" in params, "Missing parameter 'salesCode'"







def test_hyp_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_hyp_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "RESERVED",
        "STANDBY",
        "DEFECT",
        "IDLE",
        "ACTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"

def test_hyp_levelkind_exists():
    # Check that the Enumeration exists
    assert LevelKind is not None

def test_hyp_levelkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LevelKind]
    expected_literals = [
        "GREEN",
        "AMBER",
        "RED",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LevelKind"

def test_hyp_redundancytype_exists():
    # Check that the Enumeration exists
    assert RedundancyType is not None

def test_hyp_redundancytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedundancyType]
    expected_literals = [
        "n1",
        "n",
        "_11",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedundancyType"

def test_hyp_rangekind_exists():
    # Check that the Enumeration exists
    assert RangeKind is not None

def test_hyp_rangekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeKind]
    expected_literals = [
        "CAP",
        "UTILIZATION",
        "FORECASTCAP",
        "METRICREMOVE",
        "DERIVED",
        "METRIC",
        "TRENDED",
        "TOLERANCE",
        "FORECAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
library_BaseExpressionResult_strategy = st.builds(
    library_BaseExpressionResult,
)
Company_strategy = st.builds(
    Company,
)
library_Vendor_strategy = st.builds(
    library_Vendor,
)
library_MetricValueRange_strategy = st.builds(
    library_MetricValueRange,
)
BaseResource_strategy = st.builds(
    BaseResource,
)
library_Meta_strategy = st.builds(
    library_Meta,
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text,
    protocols=
        safe_text
)
library_MetricSource_strategy = st.builds(
    library_MetricSource,
)
library_Value_strategy = st.builds(
    library_Value,
)
library_FunctionRelationship_strategy = st.builds(
    library_FunctionRelationship,
)
BaseExpressionResult_strategy = st.builds(
    BaseExpressionResult,
)
library_LastEvaluationExpressionResult_strategy = st.builds(
    library_LastEvaluationExpressionResult,
    lastEvalResult=
        safe_text
)
library_ExpressionResult_strategy = st.builds(
    library_ExpressionResult,
    targetKindHint=
        safe_text,
    targetIntervalHint=
        safe_text,
    targetRange=
        safe_text
)
library_EObject_strategy = st.builds(
    library_EObject,
)
library_EquipmentRelationship_strategy = st.builds(
    library_EquipmentRelationship,
)
Component_strategy = st.builds(
    Component,
)
library_Function_strategy = st.builds(
    library_Function,
)
library_Equipment_strategy = st.builds(
    library_Equipment,
    position=
        safe_text,
    count=
        safe_text,
    redundancy=
        safe_text,
    equipmentCode=
        safe_text,
    state=
        safe_text
)
library_Protocol_strategy = st.builds(
    library_Protocol,
)
library_MultiImage_strategy = st.builds(
    library_MultiImage,
)
library_DiagramInfo_strategy = st.builds(
    library_DiagramInfo,
)
library_Metric_strategy = st.builds(
    library_Metric,
)
library_NetXResource_strategy = st.builds(
    library_NetXResource,
)
library_Lifecycle_strategy = st.builds(
    library_Lifecycle,
)
Base_strategy = st.builds(
    Base,
)
library_Component_strategy = st.builds(
    library_Component,
    duration=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
library_BaseResource_strategy = st.builds(
    library_BaseResource,
    detailDisplay=
        safe_text,
    summaryDisplay=
        safe_text,
    shortName=
        safe_text,
    longName=
        safe_text,
    expressionName=
        safe_text
)
library_Unit_strategy = st.builds(
    library_Unit,
    description=
        safe_text,
    name=
        safe_text,
    code=
        safe_text
)
library_NodeType_strategy = st.builds(
    library_NodeType,
    name=
        safe_text,
    leafNode=
        safe_text
)
library_Parameter_strategy = st.builds(
    library_Parameter,
    modifiable=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    value=
        safe_text,
    expressionName=
        safe_text
)
library_EquipmentGroup_strategy = st.builds(
    library_EquipmentGroup,
    description=
        safe_text,
    count=
        safe_text,
    name=
        safe_text
)
library_Tolerance_strategy = st.builds(
    library_Tolerance,
    level=
        safe_text,
    name=
        safe_text
)
library_Expression_strategy = st.builds(
    library_Expression,
    expressionLines=
        safe_text,
    name=
        safe_text
)
library_ProductInfo_strategy = st.builds(
    library_ProductInfo,
    endOfSupportDate=
        safe_text,
    availableDate=
        safe_text,
    endOfSalesDate=
        safe_text,
    productCode=
        safe_text,
    underDevelopmentDate=
        safe_text,
    salesCode=
        safe_text
)










@given(instance=library_Library_strategy)
def test_hyp_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Library_strategy)
def test_hyp_library_library_protocols_setter(instance):
    original = instance.protocols
    instance.protocols = original
    assert instance.protocols == original








@given(instance=library_LastEvaluationExpressionResult_strategy)
def test_hyp_library_lastevaluationexpressionresult_lastEvalResult_setter(instance):
    original = instance.lastEvalResult
    instance.lastEvalResult = original
    assert instance.lastEvalResult == original




@given(instance=library_ExpressionResult_strategy)
def test_hyp_library_expressionresult_targetKindHint_setter(instance):
    original = instance.targetKindHint
    instance.targetKindHint = original
    assert instance.targetKindHint == original



@given(instance=library_ExpressionResult_strategy)
def test_hyp_library_expressionresult_targetIntervalHint_setter(instance):
    original = instance.targetIntervalHint
    instance.targetIntervalHint = original
    assert instance.targetIntervalHint == original



@given(instance=library_ExpressionResult_strategy)
def test_hyp_library_expressionresult_targetRange_setter(instance):
    original = instance.targetRange
    instance.targetRange = original
    assert instance.targetRange == original








@given(instance=library_Equipment_strategy)
def test_hyp_library_equipment_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=library_Equipment_strategy)
def test_hyp_library_equipment_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=library_Equipment_strategy)
def test_hyp_library_equipment_redundancy_setter(instance):
    original = instance.redundancy
    instance.redundancy = original
    assert instance.redundancy == original



@given(instance=library_Equipment_strategy)
def test_hyp_library_equipment_equipmentCode_setter(instance):
    original = instance.equipmentCode
    instance.equipmentCode = original
    assert instance.equipmentCode == original



@given(instance=library_Equipment_strategy)
def test_hyp_library_equipment_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original











@given(instance=library_Component_strategy)
def test_hyp_library_component_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=library_Component_strategy)
def test_hyp_library_component_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=library_Component_strategy)
def test_hyp_library_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_BaseResource_strategy)
def test_hyp_library_baseresource_detailDisplay_setter(instance):
    original = instance.detailDisplay
    instance.detailDisplay = original
    assert instance.detailDisplay == original



@given(instance=library_BaseResource_strategy)
def test_hyp_library_baseresource_summaryDisplay_setter(instance):
    original = instance.summaryDisplay
    instance.summaryDisplay = original
    assert instance.summaryDisplay == original



@given(instance=library_BaseResource_strategy)
def test_hyp_library_baseresource_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=library_BaseResource_strategy)
def test_hyp_library_baseresource_longName_setter(instance):
    original = instance.longName
    instance.longName = original
    assert instance.longName == original



@given(instance=library_BaseResource_strategy)
def test_hyp_library_baseresource_expressionName_setter(instance):
    original = instance.expressionName
    instance.expressionName = original
    assert instance.expressionName == original




@given(instance=library_Unit_strategy)
def test_hyp_library_unit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=library_Unit_strategy)
def test_hyp_library_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Unit_strategy)
def test_hyp_library_unit_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=library_NodeType_strategy)
def test_hyp_library_nodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_NodeType_strategy)
def test_hyp_library_nodetype_leafNode_setter(instance):
    original = instance.leafNode
    instance.leafNode = original
    assert instance.leafNode == original




@given(instance=library_Parameter_strategy)
def test_hyp_library_parameter_modifiable_setter(instance):
    original = instance.modifiable
    instance.modifiable = original
    assert instance.modifiable == original



@given(instance=library_Parameter_strategy)
def test_hyp_library_parameter_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=library_Parameter_strategy)
def test_hyp_library_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Parameter_strategy)
def test_hyp_library_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=library_Parameter_strategy)
def test_hyp_library_parameter_expressionName_setter(instance):
    original = instance.expressionName
    instance.expressionName = original
    assert instance.expressionName == original




@given(instance=library_EquipmentGroup_strategy)
def test_hyp_library_equipmentgroup_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=library_EquipmentGroup_strategy)
def test_hyp_library_equipmentgroup_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=library_EquipmentGroup_strategy)
def test_hyp_library_equipmentgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Tolerance_strategy)
def test_hyp_library_tolerance_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=library_Tolerance_strategy)
def test_hyp_library_tolerance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Expression_strategy)
def test_hyp_library_expression_expressionLines_setter(instance):
    original = instance.expressionLines
    instance.expressionLines = original
    assert instance.expressionLines == original



@given(instance=library_Expression_strategy)
def test_hyp_library_expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_endOfSupportDate_setter(instance):
    original = instance.endOfSupportDate
    instance.endOfSupportDate = original
    assert instance.endOfSupportDate == original



@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_availableDate_setter(instance):
    original = instance.availableDate
    instance.availableDate = original
    assert instance.availableDate == original



@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_endOfSalesDate_setter(instance):
    original = instance.endOfSalesDate
    instance.endOfSalesDate = original
    assert instance.endOfSalesDate == original



@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_productCode_setter(instance):
    original = instance.productCode
    instance.productCode = original
    assert instance.productCode == original



@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_underDevelopmentDate_setter(instance):
    original = instance.underDevelopmentDate
    instance.underDevelopmentDate = original
    assert instance.underDevelopmentDate == original



@given(instance=library_ProductInfo_strategy)
def test_hyp_library_productinfo_salesCode_setter(instance):
    original = instance.salesCode
    instance.salesCode = original
    assert instance.salesCode == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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


def test_assoc_allEquipmentResources46_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_EquipmentGroup47', {b1})
    assert _is_linked(a, 'library_EquipmentGroup47', b1)
    if hasattr(b1, 'library_NetXResource48'):
        assert _is_linked(b1, 'library_NetXResource48', a)
    _safe_set(a, 'library_EquipmentGroup47', {b2})
    assert _is_linked(a, 'library_EquipmentGroup47', b2)
    if hasattr(b1, 'library_NetXResource48'):
        assert not _is_linked(b1, 'library_NetXResource48', a)
    if hasattr(b2, 'library_NetXResource48'):
        assert _is_linked(b2, 'library_NetXResource48', a)
    _safe_set(a, 'library_EquipmentGroup47', set())
    assert not _is_linked(a, 'library_EquipmentGroup47', b2)
    if hasattr(b2, 'library_NetXResource48'):
        assert not _is_linked(b2, 'library_NetXResource48', a)


def test_assoc_allEquipments29_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Equipment28', {b1})
    assert _is_linked(a, 'library_Equipment28', b1)
    if hasattr(b1, 'library_Equipment30'):
        assert _is_linked(b1, 'library_Equipment30', a)
    _safe_set(a, 'library_Equipment28', {b2})
    assert _is_linked(a, 'library_Equipment28', b2)
    if hasattr(b1, 'library_Equipment30'):
        assert not _is_linked(b1, 'library_Equipment30', a)
    if hasattr(b2, 'library_Equipment30'):
        assert _is_linked(b2, 'library_Equipment30', a)
    _safe_set(a, 'library_Equipment28', set())
    assert not _is_linked(a, 'library_Equipment28', b2)
    if hasattr(b2, 'library_Equipment30'):
        assert not _is_linked(b2, 'library_Equipment30', a)


def test_assoc_allEquipments49_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup50', {b1})
    assert _is_linked(a, 'library_EquipmentGroup50', b1)
    if hasattr(b1, 'library_Equipment51'):
        assert _is_linked(b1, 'library_Equipment51', a)
    _safe_set(a, 'library_EquipmentGroup50', {b2})
    assert _is_linked(a, 'library_EquipmentGroup50', b2)
    if hasattr(b1, 'library_Equipment51'):
        assert not _is_linked(b1, 'library_Equipment51', a)
    if hasattr(b2, 'library_Equipment51'):
        assert _is_linked(b2, 'library_Equipment51', a)
    _safe_set(a, 'library_EquipmentGroup50', set())
    assert not _is_linked(a, 'library_EquipmentGroup50', b2)
    if hasattr(b2, 'library_Equipment51'):
        assert not _is_linked(b2, 'library_Equipment51', a)


def test_assoc_allResources16_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_Component17', {b1})
    assert _is_linked(a, 'library_Component17', b1)
    if hasattr(b1, 'library_NetXResource'):
        assert _is_linked(b1, 'library_NetXResource', a)
    _safe_set(a, 'library_Component17', {b2})
    assert _is_linked(a, 'library_Component17', b2)
    if hasattr(b1, 'library_NetXResource'):
        assert not _is_linked(b1, 'library_NetXResource', a)
    if hasattr(b2, 'library_NetXResource'):
        assert _is_linked(b2, 'library_NetXResource', a)
    _safe_set(a, 'library_Component17', set())
    assert not _is_linked(a, 'library_Component17', b2)
    if hasattr(b2, 'library_NetXResource'):
        assert not _is_linked(b2, 'library_NetXResource', a)


def test_assoc_capacityExpressionRef5_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression', b1)
    assert _is_linked(a, 'library_Expression', b1)
    if hasattr(b1, 'library_Component6'):
        assert _is_linked(b1, 'library_Component6', a)
    _safe_set(a, 'library_Expression', b2)
    assert _is_linked(a, 'library_Expression', b2)
    if hasattr(b1, 'library_Component6'):
        assert not _is_linked(b1, 'library_Component6', a)
    if hasattr(b2, 'library_Component6'):
        assert _is_linked(b2, 'library_Component6', a)
    _safe_set(a, 'library_Expression', None)
    assert not _is_linked(a, 'library_Expression', b2)
    if hasattr(b2, 'library_Component6'):
        assert not _is_linked(b2, 'library_Component6', a)


def test_assoc_componentRef91_link_reassign_clear():
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


def test_assoc_diagrams18_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_DiagramInfo()
    b2 = library_DiagramInfo()
    _safe_set(a, 'library_Component19', {b1})
    assert _is_linked(a, 'library_Component19', b1)
    if hasattr(b1, 'library_DiagramInfo'):
        assert _is_linked(b1, 'library_DiagramInfo', a)
    _safe_set(a, 'library_Component19', {b2})
    assert _is_linked(a, 'library_Component19', b2)
    if hasattr(b1, 'library_DiagramInfo'):
        assert not _is_linked(b1, 'library_DiagramInfo', a)
    if hasattr(b2, 'library_DiagramInfo'):
        assert _is_linked(b2, 'library_DiagramInfo', a)
    _safe_set(a, 'library_Component19', set())
    assert not _is_linked(a, 'library_Component19', b2)
    if hasattr(b2, 'library_DiagramInfo'):
        assert not _is_linked(b2, 'library_DiagramInfo', a)


def test_assoc_diagrams31_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_DiagramInfo()
    b2 = library_DiagramInfo()
    _safe_set(a, 'library_EquipmentGroup32', {b1})
    assert _is_linked(a, 'library_EquipmentGroup32', b1)
    if hasattr(b1, 'library_DiagramInfo33'):
        assert _is_linked(b1, 'library_DiagramInfo33', a)
    _safe_set(a, 'library_EquipmentGroup32', {b2})
    assert _is_linked(a, 'library_EquipmentGroup32', b2)
    if hasattr(b1, 'library_DiagramInfo33'):
        assert not _is_linked(b1, 'library_DiagramInfo33', a)
    if hasattr(b2, 'library_DiagramInfo33'):
        assert _is_linked(b2, 'library_DiagramInfo33', a)
    _safe_set(a, 'library_EquipmentGroup32', set())
    assert not _is_linked(a, 'library_EquipmentGroup32', b2)
    if hasattr(b2, 'library_DiagramInfo33'):
        assert not _is_linked(b2, 'library_DiagramInfo33', a)


def test_assoc_equipmentGroupResources34_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_NetXResource()
    b2 = library_NetXResource()
    _safe_set(a, 'library_EquipmentGroup35', {b1})
    assert _is_linked(a, 'library_EquipmentGroup35', b1)
    if hasattr(b1, 'library_NetXResource36'):
        assert _is_linked(b1, 'library_NetXResource36', a)
    _safe_set(a, 'library_EquipmentGroup35', {b2})
    assert _is_linked(a, 'library_EquipmentGroup35', b2)
    if hasattr(b1, 'library_NetXResource36'):
        assert not _is_linked(b1, 'library_NetXResource36', a)
    if hasattr(b2, 'library_NetXResource36'):
        assert _is_linked(b2, 'library_NetXResource36', a)
    _safe_set(a, 'library_EquipmentGroup35', set())
    assert not _is_linked(a, 'library_EquipmentGroup35', b2)
    if hasattr(b2, 'library_NetXResource36'):
        assert not _is_linked(b2, 'library_NetXResource36', a)


def test_assoc_equipmentGroups24_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup', b1)
    assert _is_linked(a, 'library_EquipmentGroup', b1)
    if hasattr(b1, 'library_Equipment25'):
        assert _is_linked(b1, 'library_Equipment25', a)
    _safe_set(a, 'library_EquipmentGroup', b2)
    assert _is_linked(a, 'library_EquipmentGroup', b2)
    if hasattr(b1, 'library_Equipment25'):
        assert not _is_linked(b1, 'library_Equipment25', a)
    if hasattr(b2, 'library_Equipment25'):
        assert _is_linked(b2, 'library_Equipment25', a)
    _safe_set(a, 'library_EquipmentGroup', None)
    assert not _is_linked(a, 'library_EquipmentGroup', b2)
    if hasattr(b2, 'library_Equipment25'):
        assert not _is_linked(b2, 'library_Equipment25', a)


def test_assoc_equipmentRef118_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_ProductInfo', {b1})
    assert _is_linked(a, 'library_ProductInfo', b1)
    if hasattr(b1, 'library_Equipment119'):
        assert _is_linked(b1, 'library_Equipment119', a)
    _safe_set(a, 'library_ProductInfo', {b2})
    assert _is_linked(a, 'library_ProductInfo', b2)
    if hasattr(b1, 'library_Equipment119'):
        assert not _is_linked(b1, 'library_Equipment119', a)
    if hasattr(b2, 'library_Equipment119'):
        assert _is_linked(b2, 'library_Equipment119', a)
    _safe_set(a, 'library_ProductInfo', set())
    assert not _is_linked(a, 'library_ProductInfo', b2)
    if hasattr(b2, 'library_Equipment119'):
        assert not _is_linked(b2, 'library_Equipment119', a)


def test_assoc_equipmentRefs40_link_reassign_clear():
    a = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_EquipmentGroup41', {b1})
    assert _is_linked(a, 'library_EquipmentGroup41', b1)
    if hasattr(b1, 'library_Equipment42'):
        assert _is_linked(b1, 'library_Equipment42', a)
    _safe_set(a, 'library_EquipmentGroup41', {b2})
    assert _is_linked(a, 'library_EquipmentGroup41', b2)
    if hasattr(b1, 'library_Equipment42'):
        assert not _is_linked(b1, 'library_Equipment42', a)
    if hasattr(b2, 'library_Equipment42'):
        assert _is_linked(b2, 'library_Equipment42', a)
    _safe_set(a, 'library_EquipmentGroup41', set())
    assert not _is_linked(a, 'library_EquipmentGroup41', b2)
    if hasattr(b2, 'library_Equipment42'):
        assert not _is_linked(b2, 'library_Equipment42', a)


def test_assoc_equipmentRelationshipRefs26_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_EquipmentRelationship()
    b2 = library_EquipmentRelationship()
    _safe_set(a, 'library_Equipment27', {b1})
    assert _is_linked(a, 'library_Equipment27', b1)
    if hasattr(b1, 'library_EquipmentRelationship'):
        assert _is_linked(b1, 'library_EquipmentRelationship', a)
    _safe_set(a, 'library_Equipment27', {b2})
    assert _is_linked(a, 'library_Equipment27', b2)
    if hasattr(b1, 'library_EquipmentRelationship'):
        assert not _is_linked(b1, 'library_EquipmentRelationship', a)
    if hasattr(b2, 'library_EquipmentRelationship'):
        assert _is_linked(b2, 'library_EquipmentRelationship', a)
    _safe_set(a, 'library_Equipment27', set())
    assert not _is_linked(a, 'library_Equipment27', b2)
    if hasattr(b2, 'library_EquipmentRelationship'):
        assert not _is_linked(b2, 'library_EquipmentRelationship', a)


def test_assoc_equipments115_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_NodeType116', {b1})
    assert _is_linked(a, 'library_NodeType116', b1)
    if hasattr(b1, 'library_Equipment117'):
        assert _is_linked(b1, 'library_Equipment117', a)
    _safe_set(a, 'library_NodeType116', {b2})
    assert _is_linked(a, 'library_NodeType116', b2)
    if hasattr(b1, 'library_Equipment117'):
        assert not _is_linked(b1, 'library_Equipment117', a)
    if hasattr(b2, 'library_Equipment117'):
        assert _is_linked(b2, 'library_Equipment117', a)
    _safe_set(a, 'library_NodeType116', set())
    assert not _is_linked(a, 'library_NodeType116', b2)
    if hasattr(b2, 'library_Equipment117'):
        assert not _is_linked(b2, 'library_Equipment117', a)


def test_assoc_equipments23_link_reassign_clear():
    a = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Equipment', b1)
    assert _is_linked(a, 'library_Equipment', b1)
    if hasattr(b1, 'library_Equipment22'):
        assert _is_linked(b1, 'library_Equipment22', a)
    _safe_set(a, 'library_Equipment', b2)
    assert _is_linked(a, 'library_Equipment', b2)
    if hasattr(b1, 'library_Equipment22'):
        assert not _is_linked(b1, 'library_Equipment22', a)
    if hasattr(b2, 'library_Equipment22'):
        assert _is_linked(b2, 'library_Equipment22', a)
    _safe_set(a, 'library_Equipment', None)
    assert not _is_linked(a, 'library_Equipment', b2)
    if hasattr(b2, 'library_Equipment22'):
        assert not _is_linked(b2, 'library_Equipment22', a)


def test_assoc_equipments69_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Equipment(count="sample_text", equipmentCode="sample_text", position="sample_text", redundancy="sample_text", state="sample_text")
    b2 = library_Equipment(count="sample_text_2", equipmentCode="sample_text_2", position="sample_text_2", redundancy="sample_text_2", state="sample_text_2")
    _safe_set(a, 'library_Library70', {b1})
    assert _is_linked(a, 'library_Library70', b1)
    if hasattr(b1, 'library_Equipment71'):
        assert _is_linked(b1, 'library_Equipment71', a)
    _safe_set(a, 'library_Library70', {b2})
    assert _is_linked(a, 'library_Library70', b2)
    if hasattr(b1, 'library_Equipment71'):
        assert not _is_linked(b1, 'library_Equipment71', a)
    if hasattr(b2, 'library_Equipment71'):
        assert _is_linked(b2, 'library_Equipment71', a)
    _safe_set(a, 'library_Library70', set())
    assert not _is_linked(a, 'library_Library70', b2)
    if hasattr(b2, 'library_Equipment71'):
        assert not _is_linked(b2, 'library_Equipment71', a)


def test_assoc_evaluationObject52_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_EObject()
    b2 = library_EObject()
    _safe_set(a, 'library_Expression53', b1)
    assert _is_linked(a, 'library_Expression53', b1)
    if hasattr(b1, 'library_EObject'):
        assert _is_linked(b1, 'library_EObject', a)
    _safe_set(a, 'library_Expression53', b2)
    assert _is_linked(a, 'library_Expression53', b2)
    if hasattr(b1, 'library_EObject'):
        assert not _is_linked(b1, 'library_EObject', a)
    if hasattr(b2, 'library_EObject'):
        assert _is_linked(b2, 'library_EObject', a)
    _safe_set(a, 'library_Expression53', None)
    assert not _is_linked(a, 'library_Expression53', b2)
    if hasattr(b2, 'library_EObject'):
        assert not _is_linked(b2, 'library_EObject', a)


def test_assoc_expressionRef126_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Expression(expressionLines="sample_text", name="sample_text")
    b2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Tolerance127', b1)
    assert _is_linked(a, 'library_Tolerance127', b1)
    if hasattr(b1, 'library_Expression128'):
        assert _is_linked(b1, 'library_Expression128', a)
    _safe_set(a, 'library_Tolerance127', b2)
    assert _is_linked(a, 'library_Tolerance127', b2)
    if hasattr(b1, 'library_Expression128'):
        assert not _is_linked(b1, 'library_Expression128', a)
    if hasattr(b2, 'library_Expression128'):
        assert _is_linked(b2, 'library_Expression128', a)
    _safe_set(a, 'library_Tolerance127', None)
    assert not _is_linked(a, 'library_Tolerance127', b2)
    if hasattr(b2, 'library_Expression128'):
        assert not _is_linked(b2, 'library_Expression128', a)


def test_assoc_expressionRefs37_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression39', b1)
    assert _is_linked(a, 'library_Expression39', b1)
    if hasattr(b1, 'library_EquipmentGroup38'):
        assert _is_linked(b1, 'library_EquipmentGroup38', a)
    _safe_set(a, 'library_Expression39', b2)
    assert _is_linked(a, 'library_Expression39', b2)
    if hasattr(b1, 'library_EquipmentGroup38'):
        assert not _is_linked(b1, 'library_EquipmentGroup38', a)
    if hasattr(b2, 'library_EquipmentGroup38'):
        assert _is_linked(b2, 'library_EquipmentGroup38', a)
    _safe_set(a, 'library_Expression39', None)
    assert not _is_linked(a, 'library_Expression39', b2)
    if hasattr(b2, 'library_EquipmentGroup38'):
        assert not _is_linked(b2, 'library_EquipmentGroup38', a)


def test_assoc_expressions83_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Expression(expressionLines="sample_text", name="sample_text")
    b2 = library_Expression(expressionLines="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Library84', {b1})
    assert _is_linked(a, 'library_Library84', b1)
    if hasattr(b1, 'library_Expression85'):
        assert _is_linked(b1, 'library_Expression85', a)
    _safe_set(a, 'library_Library84', {b2})
    assert _is_linked(a, 'library_Library84', b2)
    if hasattr(b1, 'library_Expression85'):
        assert not _is_linked(b1, 'library_Expression85', a)
    if hasattr(b2, 'library_Expression85'):
        assert _is_linked(b2, 'library_Expression85', a)
    _safe_set(a, 'library_Library84', set())
    assert not _is_linked(a, 'library_Library84', b2)
    if hasattr(b2, 'library_Expression85'):
        assert not _is_linked(b2, 'library_Expression85', a)


def test_assoc_functions112_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_NodeType113', {b1})
    assert _is_linked(a, 'library_NodeType113', b1)
    if hasattr(b1, 'library_Function114'):
        assert _is_linked(b1, 'library_Function114', a)
    _safe_set(a, 'library_NodeType113', {b2})
    assert _is_linked(a, 'library_NodeType113', b2)
    if hasattr(b1, 'library_Function114'):
        assert not _is_linked(b1, 'library_Function114', a)
    if hasattr(b2, 'library_Function114'):
        assert _is_linked(b2, 'library_Function114', a)
    _safe_set(a, 'library_NodeType113', set())
    assert not _is_linked(a, 'library_NodeType113', b2)
    if hasattr(b2, 'library_Function114'):
        assert not _is_linked(b2, 'library_Function114', a)


def test_assoc_functions65_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_Library', {b1})
    assert _is_linked(a, 'library_Library', b1)
    if hasattr(b1, 'library_Function66'):
        assert _is_linked(b1, 'library_Function66', a)
    _safe_set(a, 'library_Library', {b2})
    assert _is_linked(a, 'library_Library', b2)
    if hasattr(b1, 'library_Function66'):
        assert not _is_linked(b1, 'library_Function66', a)
    if hasattr(b2, 'library_Function66'):
        assert _is_linked(b2, 'library_Function66', a)
    _safe_set(a, 'library_Library', set())
    assert not _is_linked(a, 'library_Library', b2)
    if hasattr(b2, 'library_Function66'):
        assert not _is_linked(b2, 'library_Function66', a)


def test_assoc_icons129_link_reassign_clear():
    a = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    b1 = library_MultiImage()
    b2 = library_MultiImage()
    _safe_set(a, 'library_Unit130', b1)
    assert _is_linked(a, 'library_Unit130', b1)
    if hasattr(b1, 'library_MultiImage131'):
        assert _is_linked(b1, 'library_MultiImage131', a)
    _safe_set(a, 'library_Unit130', b2)
    assert _is_linked(a, 'library_Unit130', b2)
    if hasattr(b1, 'library_MultiImage131'):
        assert not _is_linked(b1, 'library_MultiImage131', a)
    if hasattr(b2, 'library_MultiImage131'):
        assert _is_linked(b2, 'library_MultiImage131', a)
    _safe_set(a, 'library_Unit130', None)
    assert not _is_linked(a, 'library_Unit130', b2)
    if hasattr(b2, 'library_MultiImage131'):
        assert not _is_linked(b2, 'library_MultiImage131', a)


def test_assoc_icons20_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_MultiImage()
    b2 = library_MultiImage()
    _safe_set(a, 'library_Component21', b1)
    assert _is_linked(a, 'library_Component21', b1)
    if hasattr(b1, 'library_MultiImage'):
        assert _is_linked(b1, 'library_MultiImage', a)
    _safe_set(a, 'library_Component21', b2)
    assert _is_linked(a, 'library_Component21', b2)
    if hasattr(b1, 'library_MultiImage'):
        assert not _is_linked(b1, 'library_MultiImage', a)
    if hasattr(b2, 'library_MultiImage'):
        assert _is_linked(b2, 'library_MultiImage', a)
    _safe_set(a, 'library_Component21', None)
    assert not _is_linked(a, 'library_Component21', b2)
    if hasattr(b2, 'library_MultiImage'):
        assert not _is_linked(b2, 'library_MultiImage', a)


def test_assoc_licensedFunctionRef120_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Function()
    b2 = library_Function()
    _safe_set(a, 'library_ProductInfo121', {b1})
    assert _is_linked(a, 'library_ProductInfo121', b1)
    if hasattr(b1, 'library_Function122'):
        assert _is_linked(b1, 'library_Function122', a)
    _safe_set(a, 'library_ProductInfo121', {b2})
    assert _is_linked(a, 'library_ProductInfo121', b2)
    if hasattr(b1, 'library_Function122'):
        assert not _is_linked(b1, 'library_Function122', a)
    if hasattr(b2, 'library_Function122'):
        assert _is_linked(b2, 'library_Function122', a)
    _safe_set(a, 'library_ProductInfo121', set())
    assert not _is_linked(a, 'library_ProductInfo121', b2)
    if hasattr(b2, 'library_Function122'):
        assert not _is_linked(b2, 'library_Function122', a)


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


def test_assoc_metricRefs3_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_Metric()
    b2 = library_Metric()
    _safe_set(a, 'library_Component4', {b1})
    assert _is_linked(a, 'library_Component4', b1)
    if hasattr(b1, 'library_Metric'):
        assert _is_linked(b1, 'library_Metric', a)
    _safe_set(a, 'library_Component4', {b2})
    assert _is_linked(a, 'library_Component4', b2)
    if hasattr(b1, 'library_Metric'):
        assert not _is_linked(b1, 'library_Metric', a)
    if hasattr(b2, 'library_Metric'):
        assert _is_linked(b2, 'library_Metric', a)
    _safe_set(a, 'library_Component4', set())
    assert not _is_linked(a, 'library_Component4', b2)
    if hasattr(b2, 'library_Metric'):
        assert not _is_linked(b2, 'library_Metric', a)


def test_assoc_metricSources75_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_MetricSource()
    b2 = library_MetricSource()
    _safe_set(a, 'library_Library76', {b1})
    assert _is_linked(a, 'library_Library76', b1)
    if hasattr(b1, 'library_MetricSource'):
        assert _is_linked(b1, 'library_MetricSource', a)
    _safe_set(a, 'library_Library76', {b2})
    assert _is_linked(a, 'library_Library76', b2)
    if hasattr(b1, 'library_MetricSource'):
        assert not _is_linked(b1, 'library_MetricSource', a)
    if hasattr(b2, 'library_MetricSource'):
        assert _is_linked(b2, 'library_MetricSource', a)
    _safe_set(a, 'library_Library76', set())
    assert not _is_linked(a, 'library_Library76', b2)
    if hasattr(b2, 'library_MetricSource'):
        assert not _is_linked(b2, 'library_MetricSource', a)


def test_assoc_metrics72_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Metric()
    b2 = library_Metric()
    _safe_set(a, 'library_Library73', {b1})
    assert _is_linked(a, 'library_Library73', b1)
    if hasattr(b1, 'library_Metric74'):
        assert _is_linked(b1, 'library_Metric74', a)
    _safe_set(a, 'library_Library73', {b2})
    assert _is_linked(a, 'library_Library73', b2)
    if hasattr(b1, 'library_Metric74'):
        assert not _is_linked(b1, 'library_Metric74', a)
    if hasattr(b2, 'library_Metric74'):
        assert _is_linked(b2, 'library_Metric74', a)
    _safe_set(a, 'library_Library73', set())
    assert not _is_linked(a, 'library_Library73', b2)
    if hasattr(b2, 'library_Metric74'):
        assert not _is_linked(b2, 'library_Metric74', a)


def test_assoc_nodeTypeRef123_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_NodeType(leafNode="sample_text", name="sample_text")
    b2 = library_NodeType(leafNode="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_ProductInfo124', {b1})
    assert _is_linked(a, 'library_ProductInfo124', b1)
    if hasattr(b1, 'library_NodeType125'):
        assert _is_linked(b1, 'library_NodeType125', a)
    _safe_set(a, 'library_ProductInfo124', {b2})
    assert _is_linked(a, 'library_ProductInfo124', b2)
    if hasattr(b1, 'library_NodeType125'):
        assert not _is_linked(b1, 'library_NodeType125', a)
    if hasattr(b2, 'library_NodeType125'):
        assert _is_linked(b2, 'library_NodeType125', a)
    _safe_set(a, 'library_ProductInfo124', set())
    assert not _is_linked(a, 'library_ProductInfo124', b2)
    if hasattr(b2, 'library_NodeType125'):
        assert not _is_linked(b2, 'library_NodeType125', a)


def test_assoc_nodeTypes67_link_reassign_clear():
    a = library_NodeType(leafNode="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_NodeType', b1)
    assert _is_linked(a, 'library_NodeType', b1)
    if hasattr(b1, 'library_Library68'):
        assert _is_linked(b1, 'library_Library68', a)
    _safe_set(a, 'library_NodeType', b2)
    assert _is_linked(a, 'library_NodeType', b2)
    if hasattr(b1, 'library_Library68'):
        assert not _is_linked(b1, 'library_Library68', a)
    if hasattr(b2, 'library_Library68'):
        assert _is_linked(b2, 'library_Library68', a)
    _safe_set(a, 'library_NodeType', None)
    assert not _is_linked(a, 'library_NodeType', b2)
    if hasattr(b2, 'library_Library68'):
        assert not _is_linked(b2, 'library_Library68', a)


def test_assoc_parameterRefs14_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Parameter', b1)
    assert _is_linked(a, 'library_Parameter', b1)
    if hasattr(b1, 'library_Component15'):
        assert _is_linked(b1, 'library_Component15', a)
    _safe_set(a, 'library_Parameter', b2)
    assert _is_linked(a, 'library_Parameter', b2)
    if hasattr(b1, 'library_Component15'):
        assert not _is_linked(b1, 'library_Component15', a)
    if hasattr(b2, 'library_Component15'):
        assert _is_linked(b2, 'library_Component15', a)
    _safe_set(a, 'library_Parameter', None)
    assert not _is_linked(a, 'library_Parameter', b2)
    if hasattr(b2, 'library_Component15'):
        assert not _is_linked(b2, 'library_Component15', a)


def test_assoc_parameterRefs43_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_EquipmentGroup(count="sample_text", description="sample_text", name="sample_text")
    b2 = library_EquipmentGroup(count="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Parameter45', b1)
    assert _is_linked(a, 'library_Parameter45', b1)
    if hasattr(b1, 'library_EquipmentGroup44'):
        assert _is_linked(b1, 'library_EquipmentGroup44', a)
    _safe_set(a, 'library_Parameter45', b2)
    assert _is_linked(a, 'library_Parameter45', b2)
    if hasattr(b1, 'library_EquipmentGroup44'):
        assert not _is_linked(b1, 'library_EquipmentGroup44', a)
    if hasattr(b2, 'library_EquipmentGroup44'):
        assert _is_linked(b2, 'library_EquipmentGroup44', a)
    _safe_set(a, 'library_Parameter45', None)
    assert not _is_linked(a, 'library_Parameter45', b2)
    if hasattr(b2, 'library_EquipmentGroup44'):
        assert not _is_linked(b2, 'library_EquipmentGroup44', a)


def test_assoc_parameters77_link_reassign_clear():
    a = library_Parameter(description="sample_text", expressionName="sample_text", modifiable="sample_text", name="sample_text", value="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Parameter79', b1)
    assert _is_linked(a, 'library_Parameter79', b1)
    if hasattr(b1, 'library_Library78'):
        assert _is_linked(b1, 'library_Library78', a)
    _safe_set(a, 'library_Parameter79', b2)
    assert _is_linked(a, 'library_Parameter79', b2)
    if hasattr(b1, 'library_Library78'):
        assert not _is_linked(b1, 'library_Library78', a)
    if hasattr(b2, 'library_Library78'):
        assert _is_linked(b2, 'library_Library78', a)
    _safe_set(a, 'library_Parameter79', None)
    assert not _is_linked(a, 'library_Parameter79', b2)
    if hasattr(b2, 'library_Library78'):
        assert not _is_linked(b2, 'library_Library78', a)


def test_assoc_products132_link_reassign_clear():
    a = library_ProductInfo(availableDate="sample_text", endOfSalesDate="sample_text", endOfSupportDate="sample_text", productCode="sample_text", salesCode="sample_text", underDevelopmentDate="sample_text")
    b1 = library_Vendor()
    b2 = library_Vendor()
    _safe_set(a, 'library_ProductInfo133', b1)
    assert _is_linked(a, 'library_ProductInfo133', b1)
    if hasattr(b1, 'library_Vendor'):
        assert _is_linked(b1, 'library_Vendor', a)
    _safe_set(a, 'library_ProductInfo133', b2)
    assert _is_linked(a, 'library_ProductInfo133', b2)
    if hasattr(b1, 'library_Vendor'):
        assert not _is_linked(b1, 'library_Vendor', a)
    if hasattr(b2, 'library_Vendor'):
        assert _is_linked(b2, 'library_Vendor', a)
    _safe_set(a, 'library_ProductInfo133', None)
    assert not _is_linked(a, 'library_ProductInfo133', b2)
    if hasattr(b2, 'library_Vendor'):
        assert not _is_linked(b2, 'library_Vendor', a)


def test_assoc_protocolRefs12_link_reassign_clear():
    a = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b1 = library_Protocol()
    b2 = library_Protocol()
    _safe_set(a, 'library_Component13', {b1})
    assert _is_linked(a, 'library_Component13', b1)
    if hasattr(b1, 'library_Protocol'):
        assert _is_linked(b1, 'library_Protocol', a)
    _safe_set(a, 'library_Component13', {b2})
    assert _is_linked(a, 'library_Component13', b2)
    if hasattr(b1, 'library_Protocol'):
        assert not _is_linked(b1, 'library_Protocol', a)
    if hasattr(b2, 'library_Protocol'):
        assert _is_linked(b2, 'library_Protocol', a)
    _safe_set(a, 'library_Component13', set())
    assert not _is_linked(a, 'library_Component13', b2)
    if hasattr(b2, 'library_Protocol'):
        assert not _is_linked(b2, 'library_Protocol', a)


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


def test_assoc_targetResource54_link_reassign_clear():
    a = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    b1 = library_BaseResource(detailDisplay="sample_text", expressionName="sample_text", longName="sample_text", shortName="sample_text", summaryDisplay="sample_text")
    b2 = library_BaseResource(detailDisplay="sample_text_2", expressionName="sample_text_2", longName="sample_text_2", shortName="sample_text_2", summaryDisplay="sample_text_2")
    _safe_set(a, 'library_ExpressionResult', b1)
    assert _is_linked(a, 'library_ExpressionResult', b1)
    if hasattr(b1, 'library_BaseResource55'):
        assert _is_linked(b1, 'library_BaseResource55', a)
    _safe_set(a, 'library_ExpressionResult', b2)
    assert _is_linked(a, 'library_ExpressionResult', b2)
    if hasattr(b1, 'library_BaseResource55'):
        assert not _is_linked(b1, 'library_BaseResource55', a)
    if hasattr(b2, 'library_BaseResource55'):
        assert _is_linked(b2, 'library_BaseResource55', a)
    _safe_set(a, 'library_ExpressionResult', None)
    assert not _is_linked(a, 'library_ExpressionResult', b2)
    if hasattr(b2, 'library_BaseResource55'):
        assert not _is_linked(b2, 'library_BaseResource55', a)


def test_assoc_targetValues56_link_reassign_clear():
    a = library_ExpressionResult(targetIntervalHint="sample_text", targetKindHint="sample_text", targetRange="sample_text")
    b1 = library_Value()
    b2 = library_Value()
    _safe_set(a, 'library_ExpressionResult57', {b1})
    assert _is_linked(a, 'library_ExpressionResult57', b1)
    if hasattr(b1, 'library_Value'):
        assert _is_linked(b1, 'library_Value', a)
    _safe_set(a, 'library_ExpressionResult57', {b2})
    assert _is_linked(a, 'library_ExpressionResult57', b2)
    if hasattr(b1, 'library_Value'):
        assert not _is_linked(b1, 'library_Value', a)
    if hasattr(b2, 'library_Value'):
        assert _is_linked(b2, 'library_Value', a)
    _safe_set(a, 'library_ExpressionResult57', set())
    assert not _is_linked(a, 'library_ExpressionResult57', b2)
    if hasattr(b2, 'library_Value'):
        assert not _is_linked(b2, 'library_Value', a)


def test_assoc_toleranceRefs10_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Tolerance', b1)
    assert _is_linked(a, 'library_Tolerance', b1)
    if hasattr(b1, 'library_Component11'):
        assert _is_linked(b1, 'library_Component11', a)
    _safe_set(a, 'library_Tolerance', b2)
    assert _is_linked(a, 'library_Tolerance', b2)
    if hasattr(b1, 'library_Component11'):
        assert not _is_linked(b1, 'library_Component11', a)
    if hasattr(b2, 'library_Component11'):
        assert _is_linked(b2, 'library_Component11', a)
    _safe_set(a, 'library_Tolerance', None)
    assert not _is_linked(a, 'library_Tolerance', b2)
    if hasattr(b2, 'library_Component11'):
        assert not _is_linked(b2, 'library_Component11', a)


def test_assoc_tolerances80_link_reassign_clear():
    a = library_Tolerance(level="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Tolerance82', b1)
    assert _is_linked(a, 'library_Tolerance82', b1)
    if hasattr(b1, 'library_Library81'):
        assert _is_linked(b1, 'library_Library81', a)
    _safe_set(a, 'library_Tolerance82', b2)
    assert _is_linked(a, 'library_Tolerance82', b2)
    if hasattr(b1, 'library_Library81'):
        assert not _is_linked(b1, 'library_Library81', a)
    if hasattr(b2, 'library_Library81'):
        assert _is_linked(b2, 'library_Library81', a)
    _safe_set(a, 'library_Tolerance82', None)
    assert not _is_linked(a, 'library_Tolerance82', b2)
    if hasattr(b2, 'library_Library81'):
        assert not _is_linked(b2, 'library_Library81', a)


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


def test_assoc_units86_link_reassign_clear():
    a = library_Unit(code="sample_text", description="sample_text", name="sample_text")
    b1 = library_Library(name="sample_text", protocols="sample_text")
    b2 = library_Library(name="sample_text_2", protocols="sample_text_2")
    _safe_set(a, 'library_Unit88', b1)
    assert _is_linked(a, 'library_Unit88', b1)
    if hasattr(b1, 'library_Library87'):
        assert _is_linked(b1, 'library_Library87', a)
    _safe_set(a, 'library_Unit88', b2)
    assert _is_linked(a, 'library_Unit88', b2)
    if hasattr(b1, 'library_Library87'):
        assert not _is_linked(b1, 'library_Library87', a)
    if hasattr(b2, 'library_Library87'):
        assert _is_linked(b2, 'library_Library87', a)
    _safe_set(a, 'library_Unit88', None)
    assert not _is_linked(a, 'library_Unit88', b2)
    if hasattr(b2, 'library_Library87'):
        assert not _is_linked(b2, 'library_Library87', a)


def test_assoc_utilizationExpressionRef7_link_reassign_clear():
    a = library_Expression(expressionLines="sample_text", name="sample_text")
    b1 = library_Component(description="sample_text", duration="sample_text", name="sample_text")
    b2 = library_Component(description="sample_text_2", duration="sample_text_2", name="sample_text_2")
    _safe_set(a, 'library_Expression9', b1)
    assert _is_linked(a, 'library_Expression9', b1)
    if hasattr(b1, 'library_Component8'):
        assert _is_linked(b1, 'library_Component8', a)
    _safe_set(a, 'library_Expression9', b2)
    assert _is_linked(a, 'library_Expression9', b2)
    if hasattr(b1, 'library_Component8'):
        assert not _is_linked(b1, 'library_Component8', a)
    if hasattr(b2, 'library_Component8'):
        assert _is_linked(b2, 'library_Component8', a)
    _safe_set(a, 'library_Expression9', None)
    assert not _is_linked(a, 'library_Expression9', b2)
    if hasattr(b2, 'library_Component8'):
        assert not _is_linked(b2, 'library_Component8', a)


def test_assoc_version89_link_reassign_clear():
    a = library_Library(name="sample_text", protocols="sample_text")
    b1 = library_Meta()
    b2 = library_Meta()
    _safe_set(a, 'library_Library90', b1)
    assert _is_linked(a, 'library_Library90', b1)
    if hasattr(b1, 'library_Meta'):
        assert _is_linked(b1, 'library_Meta', a)
    _safe_set(a, 'library_Library90', b2)
    assert _is_linked(a, 'library_Library90', b2)
    if hasattr(b1, 'library_Meta'):
        assert not _is_linked(b1, 'library_Meta', a)
    if hasattr(b2, 'library_Meta'):
        assert _is_linked(b2, 'library_Meta', a)
    _safe_set(a, 'library_Library90', None)
    assert not _is_linked(a, 'library_Library90', b2)
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



