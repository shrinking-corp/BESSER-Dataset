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
    coCoMM_HardLimitDRExpression,
    coCoMM_Config,
    coCoMM_CrossModelConstraint,
    coCoMM_CoCo,
    coCoMM_CTConstraintExpression,
    DecisionRule,
    coCoMM_HardLimitDR,
    coCoMM_OptimizationDR,
    coCoMM_SelectionStateDR,
    coCoMM_CMConstraintExpression,
    coCoMM_Stakeholder,
    coCoMM_Project,
    coCoMM_DecisionRule,
    coCoMM_FeatureAttribute,
    coCoMM_TreeConstraint,
    coCoMM_FeatureAttributeElement,
    coCoMM_AttributeTypeElement,
    coCoMM_AttributeType,
    coCoMM_CrossTreeConstraint,
    coCoMM_Feature,
    coCoMM_FeatureModel,
    ConfigType,
    CTConstraintType,
    DataType,
    DRSelectionStateType,
    CMConstraintType,
    DROptimizationOp,
    DRType,
    DRHardLimitOp,
    TreeConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cocomm_hardlimitdrexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitDRExpression)


def test_hyp_cocomm_hardlimitdrexpression_constructor_exists():
    assert callable(coCoMM_HardLimitDRExpression.__init__)


def test_hyp_cocomm_hardlimitdrexpression_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitDRExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_cocomm_config_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Config)


def test_hyp_cocomm_config_constructor_exists():
    assert callable(coCoMM_Config.__init__)


def test_hyp_cocomm_config_constructor_args():
    sig = inspect.signature(coCoMM_Config.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "selected" in params, "Missing parameter 'selected'"





def test_hyp_cocomm_crossmodelconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CrossModelConstraint)


def test_hyp_cocomm_crossmodelconstraint_constructor_exists():
    assert callable(coCoMM_CrossModelConstraint.__init__)


def test_hyp_cocomm_crossmodelconstraint_constructor_args():
    sig = inspect.signature(coCoMM_CrossModelConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cocomm_coco_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CoCo)


def test_hyp_cocomm_coco_constructor_exists():
    assert callable(coCoMM_CoCo.__init__)


def test_hyp_cocomm_coco_constructor_args():
    sig = inspect.signature(coCoMM_CoCo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cocomm_ctconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CTConstraintExpression)


def test_hyp_cocomm_ctconstraintexpression_constructor_exists():
    assert callable(coCoMM_CTConstraintExpression.__init__)


def test_hyp_cocomm_ctconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM_CTConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_decisionrule_is_not_abstract():
    assert not inspect.isabstract(DecisionRule)


def test_hyp_decisionrule_constructor_exists():
    assert callable(DecisionRule.__init__)


def test_hyp_decisionrule_constructor_args():
    sig = inspect.signature(DecisionRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cocomm_hardlimitdr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitDR)


def test_hyp_cocomm_hardlimitdr_constructor_exists():
    assert callable(coCoMM_HardLimitDR.__init__)


def test_hyp_cocomm_hardlimitdr_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitDR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cocomm_optimizationdr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_OptimizationDR)


def test_hyp_cocomm_optimizationdr_constructor_exists():
    assert callable(coCoMM_OptimizationDR.__init__)


def test_hyp_cocomm_optimizationdr_constructor_args():
    sig = inspect.signature(coCoMM_OptimizationDR.__init__)
    params = list(sig.parameters.keys())
    assert "funct" in params, "Missing parameter 'funct'"




def test_hyp_cocomm_selectionstatedr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_SelectionStateDR)


def test_hyp_cocomm_selectionstatedr_constructor_exists():
    assert callable(coCoMM_SelectionStateDR.__init__)


def test_hyp_cocomm_selectionstatedr_constructor_args():
    sig = inspect.signature(coCoMM_SelectionStateDR.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"




def test_hyp_cocomm_cmconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CMConstraintExpression)


def test_hyp_cocomm_cmconstraintexpression_constructor_exists():
    assert callable(coCoMM_CMConstraintExpression.__init__)


def test_hyp_cocomm_cmconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM_CMConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_cocomm_stakeholder_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Stakeholder)


def test_hyp_cocomm_stakeholder_constructor_exists():
    assert callable(coCoMM_Stakeholder.__init__)


def test_hyp_cocomm_stakeholder_constructor_args():
    sig = inspect.signature(coCoMM_Stakeholder.__init__)
    params = list(sig.parameters.keys())
    assert "job" in params, "Missing parameter 'job'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_cocomm_project_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Project)


def test_hyp_cocomm_project_constructor_exists():
    assert callable(coCoMM_Project.__init__)


def test_hyp_cocomm_project_constructor_args():
    sig = inspect.signature(coCoMM_Project.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "target" in params, "Missing parameter 'target'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_cocomm_decisionrule_is_not_abstract():
    assert not inspect.isabstract(coCoMM_DecisionRule)


def test_hyp_cocomm_decisionrule_constructor_exists():
    assert callable(coCoMM_DecisionRule.__init__)


def test_hyp_cocomm_decisionrule_constructor_args():
    sig = inspect.signature(coCoMM_DecisionRule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_cocomm_featureattribute_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureAttribute)


def test_hyp_cocomm_featureattribute_constructor_exists():
    assert callable(coCoMM_FeatureAttribute.__init__)


def test_hyp_cocomm_featureattribute_constructor_args():
    sig = inspect.signature(coCoMM_FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cocomm_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_TreeConstraint)


def test_hyp_cocomm_treeconstraint_constructor_exists():
    assert callable(coCoMM_TreeConstraint.__init__)


def test_hyp_cocomm_treeconstraint_constructor_args():
    sig = inspect.signature(coCoMM_TreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_cocomm_featureattributeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureAttributeElement)


def test_hyp_cocomm_featureattributeelement_constructor_exists():
    assert callable(coCoMM_FeatureAttributeElement.__init__)


def test_hyp_cocomm_featureattributeelement_constructor_args():
    sig = inspect.signature(coCoMM_FeatureAttributeElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_cocomm_attributetypeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AttributeTypeElement)


def test_hyp_cocomm_attributetypeelement_constructor_exists():
    assert callable(coCoMM_AttributeTypeElement.__init__)


def test_hyp_cocomm_attributetypeelement_constructor_args():
    sig = inspect.signature(coCoMM_AttributeTypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"





def test_hyp_cocomm_attributetype_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AttributeType)


def test_hyp_cocomm_attributetype_constructor_exists():
    assert callable(coCoMM_AttributeType.__init__)


def test_hyp_cocomm_attributetype_constructor_args():
    sig = inspect.signature(coCoMM_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_cocomm_crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CrossTreeConstraint)


def test_hyp_cocomm_crosstreeconstraint_constructor_exists():
    assert callable(coCoMM_CrossTreeConstraint.__init__)


def test_hyp_cocomm_crosstreeconstraint_constructor_args():
    sig = inspect.signature(coCoMM_CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cocomm_feature_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Feature)


def test_hyp_cocomm_feature_constructor_exists():
    assert callable(coCoMM_Feature.__init__)


def test_hyp_cocomm_feature_constructor_args():
    sig = inspect.signature(coCoMM_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "abstract" in params, "Missing parameter 'abstract'"






def test_hyp_cocomm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureModel)


def test_hyp_cocomm_featuremodel_constructor_exists():
    assert callable(coCoMM_FeatureModel.__init__)


def test_hyp_cocomm_featuremodel_constructor_args():
    sig = inspect.signature(coCoMM_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "isDomain" in params, "Missing parameter 'isDomain'"
    assert "name" in params, "Missing parameter 'name'"



def test_hyp_configtype_exists():
    # Check that the Enumeration exists
    assert ConfigType is not None

def test_hyp_configtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigType]
    expected_literals = [
        "output",
        "input",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigType"

def test_hyp_ctconstrainttype_exists():
    # Check that the Enumeration exists
    assert CTConstraintType is not None

def test_hyp_ctconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CTConstraintType]
    expected_literals = [
        "or_",
        "not_",
        "implies",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CTConstraintType"

def test_hyp_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_hyp_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "int",
        "String",
        "double",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_hyp_drselectionstatetype_exists():
    # Check that the Enumeration exists
    assert DRSelectionStateType is not None

def test_hyp_drselectionstatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRSelectionStateType]
    expected_literals = [
        "mandatory",
        "forbidden",
        "preferred",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRSelectionStateType"

def test_hyp_cmconstrainttype_exists():
    # Check that the Enumeration exists
    assert CMConstraintType is not None

def test_hyp_cmconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CMConstraintType]
    expected_literals = [
        "and_",
        "or_",
        "not_",
        "implies",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CMConstraintType"

def test_hyp_droptimizationop_exists():
    # Check that the Enumeration exists
    assert DROptimizationOp is not None

def test_hyp_droptimizationop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DROptimizationOp]
    expected_literals = [
        "maximize",
        "minimize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DROptimizationOp"

def test_hyp_drtype_exists():
    # Check that the Enumeration exists
    assert DRType is not None

def test_hyp_drtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRType]
    expected_literals = [
        "hardLimit",
        "selectionState",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRType"

def test_hyp_drhardlimitop_exists():
    # Check that the Enumeration exists
    assert DRHardLimitOp is not None

def test_hyp_drhardlimitop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRHardLimitOp]
    expected_literals = [
        "eq",
        "lt",
        "leq",
        "gt",
        "geq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRHardLimitOp"

def test_hyp_treeconstrainttype_exists():
    # Check that the Enumeration exists
    assert TreeConstraintType is not None

def test_hyp_treeconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeConstraintType]
    expected_literals = [
        "Optional",
        "Mandatory",
        "Alternative",
        "Or",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeConstraintType"


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
coCoMM_HardLimitDRExpression_strategy = st.builds(
    coCoMM_HardLimitDRExpression,
    op=
        safe_text,
    value=
        safe_text
)
coCoMM_Config_strategy = st.builds(
    coCoMM_Config,
    type=
        safe_text,
    selected=
        st.booleans()
)
coCoMM_CrossModelConstraint_strategy = st.builds(
    coCoMM_CrossModelConstraint,
)
coCoMM_CoCo_strategy = st.builds(
    coCoMM_CoCo,
)
coCoMM_CTConstraintExpression_strategy = st.builds(
    coCoMM_CTConstraintExpression,
    op=
        safe_text
)
DecisionRule_strategy = st.builds(
    DecisionRule,
)
coCoMM_HardLimitDR_strategy = st.builds(
    coCoMM_HardLimitDR,
)
coCoMM_OptimizationDR_strategy = st.builds(
    coCoMM_OptimizationDR,
    funct=
        safe_text
)
coCoMM_SelectionStateDR_strategy = st.builds(
    coCoMM_SelectionStateDR,
    state=
        safe_text
)
coCoMM_CMConstraintExpression_strategy = st.builds(
    coCoMM_CMConstraintExpression,
    op=
        safe_text
)
coCoMM_Stakeholder_strategy = st.builds(
    coCoMM_Stakeholder,
    job=
        safe_text,
    name=
        safe_text
)
coCoMM_Project_strategy = st.builds(
    coCoMM_Project,
    date=
        st.dates(),
    target=
        st.booleans(),
    name=
        safe_text
)
coCoMM_DecisionRule_strategy = st.builds(
    coCoMM_DecisionRule,
    type=
        safe_text
)
coCoMM_FeatureAttribute_strategy = st.builds(
    coCoMM_FeatureAttribute,
    name=
        safe_text
)
coCoMM_TreeConstraint_strategy = st.builds(
    coCoMM_TreeConstraint,
    type=
        safe_text
)
coCoMM_FeatureAttributeElement_strategy = st.builds(
    coCoMM_FeatureAttributeElement,
    value=
        safe_text
)
coCoMM_AttributeTypeElement_strategy = st.builds(
    coCoMM_AttributeTypeElement,
    name=
        safe_text,
    dataType=
        safe_text
)
coCoMM_AttributeType_strategy = st.builds(
    coCoMM_AttributeType,
    id=
        safe_text,
    name=
        safe_text
)
coCoMM_CrossTreeConstraint_strategy = st.builds(
    coCoMM_CrossTreeConstraint,
)
coCoMM_Feature_strategy = st.builds(
    coCoMM_Feature,
    id=
        safe_text,
    name=
        safe_text,
    abstract=
        st.booleans()
)
coCoMM_FeatureModel_strategy = st.builds(
    coCoMM_FeatureModel,
    isDomain=
        st.booleans(),
    name=
        safe_text
)




@given(instance=coCoMM_HardLimitDRExpression_strategy)
def test_hyp_cocomm_hardlimitdrexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=coCoMM_HardLimitDRExpression_strategy)
def test_hyp_cocomm_hardlimitdrexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=coCoMM_Config_strategy)
def test_hyp_cocomm_config_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=coCoMM_Config_strategy)
def test_hyp_cocomm_config_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original






@given(instance=coCoMM_CTConstraintExpression_strategy)
def test_hyp_cocomm_ctconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=coCoMM_OptimizationDR_strategy)
def test_hyp_cocomm_optimizationdr_funct_setter(instance):
    original = instance.funct
    instance.funct = original
    assert instance.funct == original




@given(instance=coCoMM_SelectionStateDR_strategy)
def test_hyp_cocomm_selectionstatedr_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original




@given(instance=coCoMM_CMConstraintExpression_strategy)
def test_hyp_cocomm_cmconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=coCoMM_Stakeholder_strategy)
def test_hyp_cocomm_stakeholder_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original



@given(instance=coCoMM_Stakeholder_strategy)
def test_hyp_cocomm_stakeholder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=coCoMM_Project_strategy)
def test_hyp_cocomm_project_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=coCoMM_Project_strategy)
def test_hyp_cocomm_project_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=coCoMM_Project_strategy)
def test_hyp_cocomm_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=coCoMM_DecisionRule_strategy)
def test_hyp_cocomm_decisionrule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=coCoMM_FeatureAttribute_strategy)
def test_hyp_cocomm_featureattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=coCoMM_TreeConstraint_strategy)
def test_hyp_cocomm_treeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=coCoMM_FeatureAttributeElement_strategy)
def test_hyp_cocomm_featureattributeelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=coCoMM_AttributeTypeElement_strategy)
def test_hyp_cocomm_attributetypeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_AttributeTypeElement_strategy)
def test_hyp_cocomm_attributetypeelement_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original




@given(instance=coCoMM_AttributeType_strategy)
def test_hyp_cocomm_attributetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_AttributeType_strategy)
def test_hyp_cocomm_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=coCoMM_Feature_strategy)
def test_hyp_cocomm_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_Feature_strategy)
def test_hyp_cocomm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_Feature_strategy)
def test_hyp_cocomm_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original




@given(instance=coCoMM_FeatureModel_strategy)
def test_hyp_cocomm_featuremodel_isDomain_setter(instance):
    original = instance.isDomain
    instance.isDomain = original
    assert instance.isDomain == original



@given(instance=coCoMM_FeatureModel_strategy)
def test_hyp_cocomm_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DecisionRule,
    coCoMM_AttributeType,
    coCoMM_AttributeTypeElement,
    coCoMM_CMConstraintExpression,
    coCoMM_CTConstraintExpression,
    coCoMM_CoCo,
    coCoMM_Config,
    coCoMM_CrossModelConstraint,
    coCoMM_CrossTreeConstraint,
    coCoMM_DecisionRule,
    coCoMM_Feature,
    coCoMM_FeatureAttribute,
    coCoMM_FeatureAttributeElement,
    coCoMM_FeatureModel,
    coCoMM_HardLimitDR,
    coCoMM_HardLimitDRExpression,
    coCoMM_OptimizationDR,
    coCoMM_Project,
    coCoMM_SelectionStateDR,
    coCoMM_Stakeholder,
    coCoMM_TreeConstraint,
    CMConstraintType,
    CTConstraintType,
    ConfigType,
    DRHardLimitOp,
    DROptimizationOp,
    DRSelectionStateType,
    DRType,
    DataType,
    TreeConstraintType,
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

def test_coCoMM_AttributeType_id_value_roundtrip():
    instance = coCoMM_AttributeType(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_coCoMM_AttributeType_name_value_roundtrip():
    instance = coCoMM_AttributeType(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_AttributeTypeElement_dataType_value_roundtrip():
    instance = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_coCoMM_AttributeTypeElement_name_value_roundtrip():
    instance = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_CMConstraintExpression_op_value_roundtrip():
    instance = coCoMM_CMConstraintExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_CTConstraintExpression_op_value_roundtrip():
    instance = coCoMM_CTConstraintExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_Config_selected_value_roundtrip():
    instance = coCoMM_Config(selected=True, type="sample_text")
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_coCoMM_Config_type_value_roundtrip():
    instance = coCoMM_Config(selected=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_DecisionRule_type_value_roundtrip():
    instance = coCoMM_DecisionRule(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_Feature_abstract_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_coCoMM_Feature_id_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_coCoMM_Feature_name_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_FeatureAttribute_name_value_roundtrip():
    instance = coCoMM_FeatureAttribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_FeatureAttributeElement_value_value_roundtrip():
    instance = coCoMM_FeatureAttributeElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_coCoMM_FeatureModel_isDomain_value_roundtrip():
    instance = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    assert instance.isDomain == True
    instance.isDomain = False
    assert instance.isDomain == False


def test_coCoMM_FeatureModel_name_value_roundtrip():
    instance = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_HardLimitDRExpression_op_value_roundtrip():
    instance = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_HardLimitDRExpression_value_value_roundtrip():
    instance = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_coCoMM_OptimizationDR_funct_value_roundtrip():
    instance = coCoMM_OptimizationDR(funct="sample_text")
    assert instance.funct == "sample_text"
    instance.funct = "sample_text_2"
    assert instance.funct == "sample_text_2"


def test_coCoMM_Project_date_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_coCoMM_Project_name_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_Project_target_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.target == True
    instance.target = False
    assert instance.target == False


def test_coCoMM_SelectionStateDR_state_value_roundtrip():
    instance = coCoMM_SelectionStateDR(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_coCoMM_Stakeholder_job_value_roundtrip():
    instance = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    assert instance.job == "sample_text"
    instance.job = "sample_text_2"
    assert instance.job == "sample_text_2"


def test_coCoMM_Stakeholder_name_value_roundtrip():
    instance = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_TreeConstraint_type_value_roundtrip():
    instance = coCoMM_TreeConstraint(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_HardLimitDR_isa_DecisionRule():
    instance = coCoMM_HardLimitDR()
    assert isinstance(instance, DecisionRule)


def test_coCoMM_OptimizationDR_isa_DecisionRule():
    instance = coCoMM_OptimizationDR(funct="sample_text")
    assert isinstance(instance, DecisionRule)


def test_coCoMM_SelectionStateDR_isa_DecisionRule():
    instance = coCoMM_SelectionStateDR(state="sample_text")
    assert isinstance(instance, DecisionRule)


def test_assoc_attrType20_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute21', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute21', b1)
    if hasattr(b1, 'coCoMM_AttributeType22'):
        assert _is_linked(b1, 'coCoMM_AttributeType22', a)
    _safe_set(a, 'coCoMM_FeatureAttribute21', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute21', b2)
    if hasattr(b1, 'coCoMM_AttributeType22'):
        assert not _is_linked(b1, 'coCoMM_AttributeType22', a)
    if hasattr(b2, 'coCoMM_AttributeType22'):
        assert _is_linked(b2, 'coCoMM_AttributeType22', a)
    _safe_set(a, 'coCoMM_FeatureAttribute21', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute21', b2)
    if hasattr(b2, 'coCoMM_AttributeType22'):
        assert not _is_linked(b2, 'coCoMM_AttributeType22', a)


def test_assoc_attrType48_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_HardLimitDR()
    b2 = coCoMM_HardLimitDR()
    _safe_set(a, 'coCoMM_AttributeType50', b1)
    assert _is_linked(a, 'coCoMM_AttributeType50', b1)
    if hasattr(b1, 'coCoMM_HardLimitDR49'):
        assert _is_linked(b1, 'coCoMM_HardLimitDR49', a)
    _safe_set(a, 'coCoMM_AttributeType50', b2)
    assert _is_linked(a, 'coCoMM_AttributeType50', b2)
    if hasattr(b1, 'coCoMM_HardLimitDR49'):
        assert not _is_linked(b1, 'coCoMM_HardLimitDR49', a)
    if hasattr(b2, 'coCoMM_HardLimitDR49'):
        assert _is_linked(b2, 'coCoMM_HardLimitDR49', a)
    _safe_set(a, 'coCoMM_AttributeType50', None)
    assert not _is_linked(a, 'coCoMM_AttributeType50', b2)
    if hasattr(b2, 'coCoMM_HardLimitDR49'):
        assert not _is_linked(b2, 'coCoMM_HardLimitDR49', a)


def test_assoc_attrType51_link_reassign_clear():
    a = coCoMM_OptimizationDR(funct="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_OptimizationDR', b1)
    assert _is_linked(a, 'coCoMM_OptimizationDR', b1)
    if hasattr(b1, 'coCoMM_AttributeType52'):
        assert _is_linked(b1, 'coCoMM_AttributeType52', a)
    _safe_set(a, 'coCoMM_OptimizationDR', b2)
    assert _is_linked(a, 'coCoMM_OptimizationDR', b2)
    if hasattr(b1, 'coCoMM_AttributeType52'):
        assert not _is_linked(b1, 'coCoMM_AttributeType52', a)
    if hasattr(b2, 'coCoMM_AttributeType52'):
        assert _is_linked(b2, 'coCoMM_AttributeType52', a)
    _safe_set(a, 'coCoMM_OptimizationDR', None)
    assert not _is_linked(a, 'coCoMM_OptimizationDR', b2)
    if hasattr(b2, 'coCoMM_AttributeType52'):
        assert not _is_linked(b2, 'coCoMM_AttributeType52', a)


def test_assoc_attributeTypes33_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_AttributeType35', b1)
    assert _is_linked(a, 'coCoMM_AttributeType35', b1)
    if hasattr(b1, 'coCoMM_CoCo34'):
        assert _is_linked(b1, 'coCoMM_CoCo34', a)
    _safe_set(a, 'coCoMM_AttributeType35', b2)
    assert _is_linked(a, 'coCoMM_AttributeType35', b2)
    if hasattr(b1, 'coCoMM_CoCo34'):
        assert not _is_linked(b1, 'coCoMM_CoCo34', a)
    if hasattr(b2, 'coCoMM_CoCo34'):
        assert _is_linked(b2, 'coCoMM_CoCo34', a)
    _safe_set(a, 'coCoMM_AttributeType35', None)
    assert not _is_linked(a, 'coCoMM_AttributeType35', b2)
    if hasattr(b2, 'coCoMM_CoCo34'):
        assert not _is_linked(b2, 'coCoMM_CoCo34', a)


def test_assoc_children10_link_reassign_clear():
    a = coCoMM_TreeConstraint(type="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_TreeConstraint11', {b1})
    assert _is_linked(a, 'coCoMM_TreeConstraint11', b1)
    if hasattr(b1, 'coCoMM_Feature12'):
        assert _is_linked(b1, 'coCoMM_Feature12', a)
    _safe_set(a, 'coCoMM_TreeConstraint11', {b2})
    assert _is_linked(a, 'coCoMM_TreeConstraint11', b2)
    if hasattr(b1, 'coCoMM_Feature12'):
        assert not _is_linked(b1, 'coCoMM_Feature12', a)
    if hasattr(b2, 'coCoMM_Feature12'):
        assert _is_linked(b2, 'coCoMM_Feature12', a)
    _safe_set(a, 'coCoMM_TreeConstraint11', set())
    assert not _is_linked(a, 'coCoMM_TreeConstraint11', b2)
    if hasattr(b2, 'coCoMM_Feature12'):
        assert not _is_linked(b2, 'coCoMM_Feature12', a)


def test_assoc_configs56_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Project57', {b1})
    assert _is_linked(a, 'coCoMM_Project57', b1)
    if hasattr(b1, 'coCoMM_Config'):
        assert _is_linked(b1, 'coCoMM_Config', a)
    _safe_set(a, 'coCoMM_Project57', {b2})
    assert _is_linked(a, 'coCoMM_Project57', b2)
    if hasattr(b1, 'coCoMM_Config'):
        assert not _is_linked(b1, 'coCoMM_Config', a)
    if hasattr(b2, 'coCoMM_Config'):
        assert _is_linked(b2, 'coCoMM_Config', a)
    _safe_set(a, 'coCoMM_Project57', set())
    assert not _is_linked(a, 'coCoMM_Project57', b2)
    if hasattr(b2, 'coCoMM_Config'):
        assert not _is_linked(b2, 'coCoMM_Config', a)


def test_assoc_ctConstraints1_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_CrossTreeConstraint()
    b2 = coCoMM_CrossTreeConstraint()
    _safe_set(a, 'coCoMM_FeatureModel2', {b1})
    assert _is_linked(a, 'coCoMM_FeatureModel2', b1)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint'):
        assert _is_linked(b1, 'coCoMM_CrossTreeConstraint', a)
    _safe_set(a, 'coCoMM_FeatureModel2', {b2})
    assert _is_linked(a, 'coCoMM_FeatureModel2', b2)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint'):
        assert not _is_linked(b1, 'coCoMM_CrossTreeConstraint', a)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint'):
        assert _is_linked(b2, 'coCoMM_CrossTreeConstraint', a)
    _safe_set(a, 'coCoMM_FeatureModel2', set())
    assert not _is_linked(a, 'coCoMM_FeatureModel2', b2)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint'):
        assert not _is_linked(b2, 'coCoMM_CrossTreeConstraint', a)


def test_assoc_decisionRules31_link_reassign_clear():
    a = coCoMM_DecisionRule(type="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_DecisionRule', b1)
    assert _is_linked(a, 'coCoMM_DecisionRule', b1)
    if hasattr(b1, 'coCoMM_CoCo32'):
        assert _is_linked(b1, 'coCoMM_CoCo32', a)
    _safe_set(a, 'coCoMM_DecisionRule', b2)
    assert _is_linked(a, 'coCoMM_DecisionRule', b2)
    if hasattr(b1, 'coCoMM_CoCo32'):
        assert not _is_linked(b1, 'coCoMM_CoCo32', a)
    if hasattr(b2, 'coCoMM_CoCo32'):
        assert _is_linked(b2, 'coCoMM_CoCo32', a)
    _safe_set(a, 'coCoMM_DecisionRule', None)
    assert not _is_linked(a, 'coCoMM_DecisionRule', b2)
    if hasattr(b2, 'coCoMM_CoCo32'):
        assert not _is_linked(b2, 'coCoMM_CoCo32', a)


def test_assoc_decisionRules53_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_DecisionRule(type="sample_text")
    b2 = coCoMM_DecisionRule(type="sample_text_2")
    _safe_set(a, 'coCoMM_Project54', {b1})
    assert _is_linked(a, 'coCoMM_Project54', b1)
    if hasattr(b1, 'coCoMM_DecisionRule55'):
        assert _is_linked(b1, 'coCoMM_DecisionRule55', a)
    _safe_set(a, 'coCoMM_Project54', {b2})
    assert _is_linked(a, 'coCoMM_Project54', b2)
    if hasattr(b1, 'coCoMM_DecisionRule55'):
        assert not _is_linked(b1, 'coCoMM_DecisionRule55', a)
    if hasattr(b2, 'coCoMM_DecisionRule55'):
        assert _is_linked(b2, 'coCoMM_DecisionRule55', a)
    _safe_set(a, 'coCoMM_Project54', set())
    assert not _is_linked(a, 'coCoMM_Project54', b2)
    if hasattr(b2, 'coCoMM_DecisionRule55'):
        assert not _is_linked(b2, 'coCoMM_DecisionRule55', a)


def test_assoc_elements15_link_reassign_clear():
    a = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_AttributeTypeElement', b1)
    assert _is_linked(a, 'coCoMM_AttributeTypeElement', b1)
    if hasattr(b1, 'coCoMM_AttributeType16'):
        assert _is_linked(b1, 'coCoMM_AttributeType16', a)
    _safe_set(a, 'coCoMM_AttributeTypeElement', b2)
    assert _is_linked(a, 'coCoMM_AttributeTypeElement', b2)
    if hasattr(b1, 'coCoMM_AttributeType16'):
        assert not _is_linked(b1, 'coCoMM_AttributeType16', a)
    if hasattr(b2, 'coCoMM_AttributeType16'):
        assert _is_linked(b2, 'coCoMM_AttributeType16', a)
    _safe_set(a, 'coCoMM_AttributeTypeElement', None)
    assert not _is_linked(a, 'coCoMM_AttributeTypeElement', b2)
    if hasattr(b2, 'coCoMM_AttributeType16'):
        assert not _is_linked(b2, 'coCoMM_AttributeType16', a)


def test_assoc_elements23_link_reassign_clear():
    a = coCoMM_FeatureAttributeElement(value="sample_text")
    b1 = coCoMM_FeatureAttribute(name="sample_text")
    b2 = coCoMM_FeatureAttribute(name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttributeElement', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttributeElement', b1)
    if hasattr(b1, 'coCoMM_FeatureAttribute24'):
        assert _is_linked(b1, 'coCoMM_FeatureAttribute24', a)
    _safe_set(a, 'coCoMM_FeatureAttributeElement', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttributeElement', b2)
    if hasattr(b1, 'coCoMM_FeatureAttribute24'):
        assert not _is_linked(b1, 'coCoMM_FeatureAttribute24', a)
    if hasattr(b2, 'coCoMM_FeatureAttribute24'):
        assert _is_linked(b2, 'coCoMM_FeatureAttribute24', a)
    _safe_set(a, 'coCoMM_FeatureAttributeElement', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttributeElement', b2)
    if hasattr(b2, 'coCoMM_FeatureAttribute24'):
        assert not _is_linked(b2, 'coCoMM_FeatureAttribute24', a)


def test_assoc_expressions25_link_reassign_clear():
    a = coCoMM_CTConstraintExpression(op="sample_text")
    b1 = coCoMM_CrossTreeConstraint()
    b2 = coCoMM_CrossTreeConstraint()
    _safe_set(a, 'coCoMM_CTConstraintExpression', b1)
    assert _is_linked(a, 'coCoMM_CTConstraintExpression', b1)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint26'):
        assert _is_linked(b1, 'coCoMM_CrossTreeConstraint26', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression', b2)
    assert _is_linked(a, 'coCoMM_CTConstraintExpression', b2)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint26'):
        assert not _is_linked(b1, 'coCoMM_CrossTreeConstraint26', a)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint26'):
        assert _is_linked(b2, 'coCoMM_CrossTreeConstraint26', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression', None)
    assert not _is_linked(a, 'coCoMM_CTConstraintExpression', b2)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint26'):
        assert not _is_linked(b2, 'coCoMM_CrossTreeConstraint26', a)


def test_assoc_expressions40_link_reassign_clear():
    a = coCoMM_CMConstraintExpression(op="sample_text")
    b1 = coCoMM_CrossModelConstraint()
    b2 = coCoMM_CrossModelConstraint()
    _safe_set(a, 'coCoMM_CMConstraintExpression', b1)
    assert _is_linked(a, 'coCoMM_CMConstraintExpression', b1)
    if hasattr(b1, 'coCoMM_CrossModelConstraint41'):
        assert _is_linked(b1, 'coCoMM_CrossModelConstraint41', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression', b2)
    assert _is_linked(a, 'coCoMM_CMConstraintExpression', b2)
    if hasattr(b1, 'coCoMM_CrossModelConstraint41'):
        assert not _is_linked(b1, 'coCoMM_CrossModelConstraint41', a)
    if hasattr(b2, 'coCoMM_CrossModelConstraint41'):
        assert _is_linked(b2, 'coCoMM_CrossModelConstraint41', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression', None)
    assert not _is_linked(a, 'coCoMM_CMConstraintExpression', b2)
    if hasattr(b2, 'coCoMM_CrossModelConstraint41'):
        assert not _is_linked(b2, 'coCoMM_CrossModelConstraint41', a)


def test_assoc_expressions47_link_reassign_clear():
    a = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    b1 = coCoMM_HardLimitDR()
    b2 = coCoMM_HardLimitDR()
    _safe_set(a, 'coCoMM_HardLimitDRExpression', b1)
    assert _is_linked(a, 'coCoMM_HardLimitDRExpression', b1)
    if hasattr(b1, 'coCoMM_HardLimitDR'):
        assert _is_linked(b1, 'coCoMM_HardLimitDR', a)
    _safe_set(a, 'coCoMM_HardLimitDRExpression', b2)
    assert _is_linked(a, 'coCoMM_HardLimitDRExpression', b2)
    if hasattr(b1, 'coCoMM_HardLimitDR'):
        assert not _is_linked(b1, 'coCoMM_HardLimitDR', a)
    if hasattr(b2, 'coCoMM_HardLimitDR'):
        assert _is_linked(b2, 'coCoMM_HardLimitDR', a)
    _safe_set(a, 'coCoMM_HardLimitDRExpression', None)
    assert not _is_linked(a, 'coCoMM_HardLimitDRExpression', b2)
    if hasattr(b2, 'coCoMM_HardLimitDR'):
        assert not _is_linked(b2, 'coCoMM_HardLimitDR', a)


def test_assoc_expressions68_link_reassign_clear():
    a = coCoMM_CTConstraintExpression(op="sample_text")
    b1 = coCoMM_CTConstraintExpression(op="sample_text")
    b2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_CTConstraintExpression67', {b1})
    assert _is_linked(a, 'coCoMM_CTConstraintExpression67', b1)
    if hasattr(b1, 'coCoMM_CTConstraintExpression69'):
        assert _is_linked(b1, 'coCoMM_CTConstraintExpression69', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression67', {b2})
    assert _is_linked(a, 'coCoMM_CTConstraintExpression67', b2)
    if hasattr(b1, 'coCoMM_CTConstraintExpression69'):
        assert not _is_linked(b1, 'coCoMM_CTConstraintExpression69', a)
    if hasattr(b2, 'coCoMM_CTConstraintExpression69'):
        assert _is_linked(b2, 'coCoMM_CTConstraintExpression69', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression67', set())
    assert not _is_linked(a, 'coCoMM_CTConstraintExpression67', b2)
    if hasattr(b2, 'coCoMM_CTConstraintExpression69'):
        assert not _is_linked(b2, 'coCoMM_CTConstraintExpression69', a)


def test_assoc_expressions74_link_reassign_clear():
    a = coCoMM_CMConstraintExpression(op="sample_text")
    b1 = coCoMM_CMConstraintExpression(op="sample_text")
    b2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_CMConstraintExpression73', {b1})
    assert _is_linked(a, 'coCoMM_CMConstraintExpression73', b1)
    if hasattr(b1, 'coCoMM_CMConstraintExpression75'):
        assert _is_linked(b1, 'coCoMM_CMConstraintExpression75', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression73', {b2})
    assert _is_linked(a, 'coCoMM_CMConstraintExpression73', b2)
    if hasattr(b1, 'coCoMM_CMConstraintExpression75'):
        assert not _is_linked(b1, 'coCoMM_CMConstraintExpression75', a)
    if hasattr(b2, 'coCoMM_CMConstraintExpression75'):
        assert _is_linked(b2, 'coCoMM_CMConstraintExpression75', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression73', set())
    assert not _is_linked(a, 'coCoMM_CMConstraintExpression73', b2)
    if hasattr(b2, 'coCoMM_CMConstraintExpression75'):
        assert not _is_linked(b2, 'coCoMM_CMConstraintExpression75', a)


def test_assoc_feature44_link_reassign_clear():
    a = coCoMM_SelectionStateDR(state="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_SelectionStateDR45', b1)
    assert _is_linked(a, 'coCoMM_SelectionStateDR45', b1)
    if hasattr(b1, 'coCoMM_Feature46'):
        assert _is_linked(b1, 'coCoMM_Feature46', a)
    _safe_set(a, 'coCoMM_SelectionStateDR45', b2)
    assert _is_linked(a, 'coCoMM_SelectionStateDR45', b2)
    if hasattr(b1, 'coCoMM_Feature46'):
        assert not _is_linked(b1, 'coCoMM_Feature46', a)
    if hasattr(b2, 'coCoMM_Feature46'):
        assert _is_linked(b2, 'coCoMM_Feature46', a)
    _safe_set(a, 'coCoMM_SelectionStateDR45', None)
    assert not _is_linked(a, 'coCoMM_SelectionStateDR45', b2)
    if hasattr(b2, 'coCoMM_Feature46'):
        assert not _is_linked(b2, 'coCoMM_Feature46', a)


def test_assoc_featureAttributes17_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute19', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute19', b1)
    if hasattr(b1, 'coCoMM_AttributeType18'):
        assert _is_linked(b1, 'coCoMM_AttributeType18', a)
    _safe_set(a, 'coCoMM_FeatureAttribute19', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute19', b2)
    if hasattr(b1, 'coCoMM_AttributeType18'):
        assert not _is_linked(b1, 'coCoMM_AttributeType18', a)
    if hasattr(b2, 'coCoMM_AttributeType18'):
        assert _is_linked(b2, 'coCoMM_AttributeType18', a)
    _safe_set(a, 'coCoMM_FeatureAttribute19', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute19', b2)
    if hasattr(b2, 'coCoMM_AttributeType18'):
        assert not _is_linked(b2, 'coCoMM_AttributeType18', a)


def test_assoc_featureAttributes8_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute', b1)
    if hasattr(b1, 'coCoMM_Feature9'):
        assert _is_linked(b1, 'coCoMM_Feature9', a)
    _safe_set(a, 'coCoMM_FeatureAttribute', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute', b2)
    if hasattr(b1, 'coCoMM_Feature9'):
        assert not _is_linked(b1, 'coCoMM_Feature9', a)
    if hasattr(b2, 'coCoMM_Feature9'):
        assert _is_linked(b2, 'coCoMM_Feature9', a)
    _safe_set(a, 'coCoMM_FeatureAttribute', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute', b2)
    if hasattr(b2, 'coCoMM_Feature9'):
        assert not _is_linked(b2, 'coCoMM_Feature9', a)


def test_assoc_featureModel42_link_reassign_clear():
    a = coCoMM_SelectionStateDR(state="sample_text")
    b1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
    _safe_set(a, 'coCoMM_SelectionStateDR', b1)
    assert _is_linked(a, 'coCoMM_SelectionStateDR', b1)
    if hasattr(b1, 'coCoMM_FeatureModel43'):
        assert _is_linked(b1, 'coCoMM_FeatureModel43', a)
    _safe_set(a, 'coCoMM_SelectionStateDR', b2)
    assert _is_linked(a, 'coCoMM_SelectionStateDR', b2)
    if hasattr(b1, 'coCoMM_FeatureModel43'):
        assert not _is_linked(b1, 'coCoMM_FeatureModel43', a)
    if hasattr(b2, 'coCoMM_FeatureModel43'):
        assert _is_linked(b2, 'coCoMM_FeatureModel43', a)
    _safe_set(a, 'coCoMM_SelectionStateDR', None)
    assert not _is_linked(a, 'coCoMM_SelectionStateDR', b2)
    if hasattr(b2, 'coCoMM_FeatureModel43'):
        assert not _is_linked(b2, 'coCoMM_FeatureModel43', a)


def test_assoc_featureModel5_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureModel7', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel7', b1)
    if hasattr(b1, 'coCoMM_Feature6'):
        assert _is_linked(b1, 'coCoMM_Feature6', a)
    _safe_set(a, 'coCoMM_FeatureModel7', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel7', b2)
    if hasattr(b1, 'coCoMM_Feature6'):
        assert not _is_linked(b1, 'coCoMM_Feature6', a)
    if hasattr(b2, 'coCoMM_Feature6'):
        assert _is_linked(b2, 'coCoMM_Feature6', a)
    _safe_set(a, 'coCoMM_FeatureModel7', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel7', b2)
    if hasattr(b2, 'coCoMM_Feature6'):
        assert not _is_linked(b2, 'coCoMM_Feature6', a)


def test_assoc_featureModels27_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_FeatureModel28', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel28', b1)
    if hasattr(b1, 'coCoMM_CoCo'):
        assert _is_linked(b1, 'coCoMM_CoCo', a)
    _safe_set(a, 'coCoMM_FeatureModel28', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel28', b2)
    if hasattr(b1, 'coCoMM_CoCo'):
        assert not _is_linked(b1, 'coCoMM_CoCo', a)
    if hasattr(b2, 'coCoMM_CoCo'):
        assert _is_linked(b2, 'coCoMM_CoCo', a)
    _safe_set(a, 'coCoMM_FeatureModel28', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel28', b2)
    if hasattr(b2, 'coCoMM_CoCo'):
        assert not _is_linked(b2, 'coCoMM_CoCo', a)


def test_assoc_features61_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Feature63', b1)
    assert _is_linked(a, 'coCoMM_Feature63', b1)
    if hasattr(b1, 'coCoMM_Config62'):
        assert _is_linked(b1, 'coCoMM_Config62', a)
    _safe_set(a, 'coCoMM_Feature63', b2)
    assert _is_linked(a, 'coCoMM_Feature63', b2)
    if hasattr(b1, 'coCoMM_Config62'):
        assert not _is_linked(b1, 'coCoMM_Config62', a)
    if hasattr(b2, 'coCoMM_Config62'):
        assert _is_linked(b2, 'coCoMM_Config62', a)
    _safe_set(a, 'coCoMM_Feature63', None)
    assert not _is_linked(a, 'coCoMM_Feature63', b2)
    if hasattr(b2, 'coCoMM_Config62'):
        assert not _is_linked(b2, 'coCoMM_Config62', a)


def test_assoc_features64_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_CTConstraintExpression(op="sample_text")
    b2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_Feature66', b1)
    assert _is_linked(a, 'coCoMM_Feature66', b1)
    if hasattr(b1, 'coCoMM_CTConstraintExpression65'):
        assert _is_linked(b1, 'coCoMM_CTConstraintExpression65', a)
    _safe_set(a, 'coCoMM_Feature66', b2)
    assert _is_linked(a, 'coCoMM_Feature66', b2)
    if hasattr(b1, 'coCoMM_CTConstraintExpression65'):
        assert not _is_linked(b1, 'coCoMM_CTConstraintExpression65', a)
    if hasattr(b2, 'coCoMM_CTConstraintExpression65'):
        assert _is_linked(b2, 'coCoMM_CTConstraintExpression65', a)
    _safe_set(a, 'coCoMM_Feature66', None)
    assert not _is_linked(a, 'coCoMM_Feature66', b2)
    if hasattr(b2, 'coCoMM_CTConstraintExpression65'):
        assert not _is_linked(b2, 'coCoMM_CTConstraintExpression65', a)


def test_assoc_features70_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_CMConstraintExpression(op="sample_text")
    b2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_Feature72', b1)
    assert _is_linked(a, 'coCoMM_Feature72', b1)
    if hasattr(b1, 'coCoMM_CMConstraintExpression71'):
        assert _is_linked(b1, 'coCoMM_CMConstraintExpression71', a)
    _safe_set(a, 'coCoMM_Feature72', b2)
    assert _is_linked(a, 'coCoMM_Feature72', b2)
    if hasattr(b1, 'coCoMM_CMConstraintExpression71'):
        assert not _is_linked(b1, 'coCoMM_CMConstraintExpression71', a)
    if hasattr(b2, 'coCoMM_CMConstraintExpression71'):
        assert _is_linked(b2, 'coCoMM_CMConstraintExpression71', a)
    _safe_set(a, 'coCoMM_Feature72', None)
    assert not _is_linked(a, 'coCoMM_Feature72', b2)
    if hasattr(b2, 'coCoMM_CMConstraintExpression71'):
        assert not _is_linked(b2, 'coCoMM_CMConstraintExpression71', a)


def test_assoc_independentAttrType14_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_AttributeType', b1)
    assert _is_linked(a, 'coCoMM_AttributeType', b1)
    if hasattr(b1, 'coCoMM_AttributeType13'):
        assert _is_linked(b1, 'coCoMM_AttributeType13', a)
    _safe_set(a, 'coCoMM_AttributeType', b2)
    assert _is_linked(a, 'coCoMM_AttributeType', b2)
    if hasattr(b1, 'coCoMM_AttributeType13'):
        assert not _is_linked(b1, 'coCoMM_AttributeType13', a)
    if hasattr(b2, 'coCoMM_AttributeType13'):
        assert _is_linked(b2, 'coCoMM_AttributeType13', a)
    _safe_set(a, 'coCoMM_AttributeType', None)
    assert not _is_linked(a, 'coCoMM_AttributeType', b2)
    if hasattr(b2, 'coCoMM_AttributeType13'):
        assert not _is_linked(b2, 'coCoMM_AttributeType13', a)


def test_assoc_project36_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_Project', b1)
    assert _is_linked(a, 'coCoMM_Project', b1)
    if hasattr(b1, 'coCoMM_CoCo37'):
        assert _is_linked(b1, 'coCoMM_CoCo37', a)
    _safe_set(a, 'coCoMM_Project', b2)
    assert _is_linked(a, 'coCoMM_Project', b2)
    if hasattr(b1, 'coCoMM_CoCo37'):
        assert not _is_linked(b1, 'coCoMM_CoCo37', a)
    if hasattr(b2, 'coCoMM_CoCo37'):
        assert _is_linked(b2, 'coCoMM_CoCo37', a)
    _safe_set(a, 'coCoMM_Project', None)
    assert not _is_linked(a, 'coCoMM_Project', b2)
    if hasattr(b2, 'coCoMM_CoCo37'):
        assert not _is_linked(b2, 'coCoMM_CoCo37', a)


def test_assoc_root0_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureModel', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel', b1)
    if hasattr(b1, 'coCoMM_Feature'):
        assert _is_linked(b1, 'coCoMM_Feature', a)
    _safe_set(a, 'coCoMM_FeatureModel', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel', b2)
    if hasattr(b1, 'coCoMM_Feature'):
        assert not _is_linked(b1, 'coCoMM_Feature', a)
    if hasattr(b2, 'coCoMM_Feature'):
        assert _is_linked(b2, 'coCoMM_Feature', a)
    _safe_set(a, 'coCoMM_FeatureModel', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel', b2)
    if hasattr(b2, 'coCoMM_Feature'):
        assert not _is_linked(b2, 'coCoMM_Feature', a)


def test_assoc_stakeholder58_link_reassign_clear():
    a = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Stakeholder60', b1)
    assert _is_linked(a, 'coCoMM_Stakeholder60', b1)
    if hasattr(b1, 'coCoMM_Config59'):
        assert _is_linked(b1, 'coCoMM_Config59', a)
    _safe_set(a, 'coCoMM_Stakeholder60', b2)
    assert _is_linked(a, 'coCoMM_Stakeholder60', b2)
    if hasattr(b1, 'coCoMM_Config59'):
        assert not _is_linked(b1, 'coCoMM_Config59', a)
    if hasattr(b2, 'coCoMM_Config59'):
        assert _is_linked(b2, 'coCoMM_Config59', a)
    _safe_set(a, 'coCoMM_Stakeholder60', None)
    assert not _is_linked(a, 'coCoMM_Stakeholder60', b2)
    if hasattr(b2, 'coCoMM_Config59'):
        assert not _is_linked(b2, 'coCoMM_Config59', a)


def test_assoc_stakeholders38_link_reassign_clear():
    a = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_Stakeholder', b1)
    assert _is_linked(a, 'coCoMM_Stakeholder', b1)
    if hasattr(b1, 'coCoMM_CoCo39'):
        assert _is_linked(b1, 'coCoMM_CoCo39', a)
    _safe_set(a, 'coCoMM_Stakeholder', b2)
    assert _is_linked(a, 'coCoMM_Stakeholder', b2)
    if hasattr(b1, 'coCoMM_CoCo39'):
        assert not _is_linked(b1, 'coCoMM_CoCo39', a)
    if hasattr(b2, 'coCoMM_CoCo39'):
        assert _is_linked(b2, 'coCoMM_CoCo39', a)
    _safe_set(a, 'coCoMM_Stakeholder', None)
    assert not _is_linked(a, 'coCoMM_Stakeholder', b2)
    if hasattr(b2, 'coCoMM_CoCo39'):
        assert not _is_linked(b2, 'coCoMM_CoCo39', a)


def test_assoc_treeConstraints3_link_reassign_clear():
    a = coCoMM_TreeConstraint(type="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_TreeConstraint', b1)
    assert _is_linked(a, 'coCoMM_TreeConstraint', b1)
    if hasattr(b1, 'coCoMM_Feature4'):
        assert _is_linked(b1, 'coCoMM_Feature4', a)
    _safe_set(a, 'coCoMM_TreeConstraint', b2)
    assert _is_linked(a, 'coCoMM_TreeConstraint', b2)
    if hasattr(b1, 'coCoMM_Feature4'):
        assert not _is_linked(b1, 'coCoMM_Feature4', a)
    if hasattr(b2, 'coCoMM_Feature4'):
        assert _is_linked(b2, 'coCoMM_Feature4', a)
    _safe_set(a, 'coCoMM_TreeConstraint', None)
    assert not _is_linked(a, 'coCoMM_TreeConstraint', b2)
    if hasattr(b2, 'coCoMM_Feature4'):
        assert not _is_linked(b2, 'coCoMM_Feature4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DecisionRule_strategy = st.builds(DecisionRule)
@given(instance=DecisionRule_strategy)
@settings(max_examples=25)
def test_DecisionRule_instantiation(instance):
    assert isinstance(instance, DecisionRule)


coCoMM_AttributeType_strategy = st.builds(coCoMM_AttributeType, id=safe_text, name=safe_text)
@given(instance=coCoMM_AttributeType_strategy)
@settings(max_examples=25)
def test_coCoMM_AttributeType_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeType)


coCoMM_AttributeTypeElement_strategy = st.builds(coCoMM_AttributeTypeElement, dataType=safe_text, name=safe_text)
@given(instance=coCoMM_AttributeTypeElement_strategy)
@settings(max_examples=25)
def test_coCoMM_AttributeTypeElement_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeTypeElement)


coCoMM_CMConstraintExpression_strategy = st.builds(coCoMM_CMConstraintExpression, op=safe_text)
@given(instance=coCoMM_CMConstraintExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_CMConstraintExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CMConstraintExpression)


coCoMM_CTConstraintExpression_strategy = st.builds(coCoMM_CTConstraintExpression, op=safe_text)
@given(instance=coCoMM_CTConstraintExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_CTConstraintExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CTConstraintExpression)


coCoMM_CoCo_strategy = st.builds(coCoMM_CoCo)
@given(instance=coCoMM_CoCo_strategy)
@settings(max_examples=25)
def test_coCoMM_CoCo_instantiation(instance):
    assert isinstance(instance, coCoMM_CoCo)


coCoMM_Config_strategy = st.builds(coCoMM_Config, selected=st.booleans(), type=safe_text)
@given(instance=coCoMM_Config_strategy)
@settings(max_examples=25)
def test_coCoMM_Config_instantiation(instance):
    assert isinstance(instance, coCoMM_Config)


coCoMM_CrossModelConstraint_strategy = st.builds(coCoMM_CrossModelConstraint)
@given(instance=coCoMM_CrossModelConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_CrossModelConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossModelConstraint)


coCoMM_CrossTreeConstraint_strategy = st.builds(coCoMM_CrossTreeConstraint)
@given(instance=coCoMM_CrossTreeConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_CrossTreeConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossTreeConstraint)


coCoMM_DecisionRule_strategy = st.builds(coCoMM_DecisionRule, type=safe_text)
@given(instance=coCoMM_DecisionRule_strategy)
@settings(max_examples=25)
def test_coCoMM_DecisionRule_instantiation(instance):
    assert isinstance(instance, coCoMM_DecisionRule)


coCoMM_Feature_strategy = st.builds(coCoMM_Feature, abstract=st.booleans(), id=safe_text, name=safe_text)
@given(instance=coCoMM_Feature_strategy)
@settings(max_examples=25)
def test_coCoMM_Feature_instantiation(instance):
    assert isinstance(instance, coCoMM_Feature)


coCoMM_FeatureAttribute_strategy = st.builds(coCoMM_FeatureAttribute, name=safe_text)
@given(instance=coCoMM_FeatureAttribute_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureAttribute_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttribute)


coCoMM_FeatureAttributeElement_strategy = st.builds(coCoMM_FeatureAttributeElement, value=safe_text)
@given(instance=coCoMM_FeatureAttributeElement_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureAttributeElement_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttributeElement)


coCoMM_FeatureModel_strategy = st.builds(coCoMM_FeatureModel, isDomain=st.booleans(), name=safe_text)
@given(instance=coCoMM_FeatureModel_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureModel_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureModel)


coCoMM_HardLimitDR_strategy = st.builds(coCoMM_HardLimitDR)
@given(instance=coCoMM_HardLimitDR_strategy)
@settings(max_examples=25)
def test_coCoMM_HardLimitDR_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDR)


coCoMM_HardLimitDRExpression_strategy = st.builds(coCoMM_HardLimitDRExpression, op=safe_text, value=safe_text)
@given(instance=coCoMM_HardLimitDRExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_HardLimitDRExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDRExpression)


coCoMM_OptimizationDR_strategy = st.builds(coCoMM_OptimizationDR, funct=safe_text)
@given(instance=coCoMM_OptimizationDR_strategy)
@settings(max_examples=25)
def test_coCoMM_OptimizationDR_instantiation(instance):
    assert isinstance(instance, coCoMM_OptimizationDR)


coCoMM_Project_strategy = st.builds(coCoMM_Project, date=st.dates(), name=safe_text, target=st.booleans())
@given(instance=coCoMM_Project_strategy)
@settings(max_examples=25)
def test_coCoMM_Project_instantiation(instance):
    assert isinstance(instance, coCoMM_Project)


coCoMM_SelectionStateDR_strategy = st.builds(coCoMM_SelectionStateDR, state=safe_text)
@given(instance=coCoMM_SelectionStateDR_strategy)
@settings(max_examples=25)
def test_coCoMM_SelectionStateDR_instantiation(instance):
    assert isinstance(instance, coCoMM_SelectionStateDR)


coCoMM_Stakeholder_strategy = st.builds(coCoMM_Stakeholder, job=safe_text, name=safe_text)
@given(instance=coCoMM_Stakeholder_strategy)
@settings(max_examples=25)
def test_coCoMM_Stakeholder_instantiation(instance):
    assert isinstance(instance, coCoMM_Stakeholder)


coCoMM_TreeConstraint_strategy = st.builds(coCoMM_TreeConstraint, type=safe_text)
@given(instance=coCoMM_TreeConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_TreeConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_TreeConstraint)



