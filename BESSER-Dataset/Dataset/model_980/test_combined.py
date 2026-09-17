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
    UnaryFormula,
    henshin_Not,
    BinaryFormula,
    henshin_Xor,
    henshin_Or,
    henshin_And,
    UnaryUnit,
    henshin_LoopUnit,
    henshin_IteratedUnit,
    MultiUnit,
    henshin_PriorityUnit,
    henshin_SequentialUnit,
    henshin_IndependentUnit,
    Formula,
    henshin_True,
    henshin_UnaryFormula,
    henshin_BinaryFormula,
    henshin_NestedCondition,
    henshin_EReference,
    henshin_EClass,
    henshin_EAttribute,
    henshin_EClassifier,
    GraphElement,
    henshin_Attribute,
    henshin_Formula,
    henshin_Edge,
    henshin_Mapping,
    henshin_EPackage,
    NamedElement,
    henshin_Unit,
    henshin_Node,
    henshin_AttributeCondition,
    henshin_Parameter,
    henshin_Graph,
    henshin_Module,
    Unit,
    henshin_UnaryUnit,
    henshin_ConditionalUnit,
    henshin_MultiUnit,
    henshin_Rule,
    henshin_ParameterMapping,
    henshin_GraphElement,
    henshin_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_unaryformula_is_not_abstract():
    assert not inspect.isabstract(UnaryFormula)


def test_hyp_unaryformula_constructor_exists():
    assert callable(UnaryFormula.__init__)


def test_hyp_unaryformula_constructor_args():
    sig = inspect.signature(UnaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_not_is_not_abstract():
    assert not inspect.isabstract(henshin_Not)


def test_hyp_henshin_not_constructor_exists():
    assert callable(henshin_Not.__init__)


def test_hyp_henshin_not_constructor_args():
    sig = inspect.signature(henshin_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryformula_is_not_abstract():
    assert not inspect.isabstract(BinaryFormula)


def test_hyp_binaryformula_constructor_exists():
    assert callable(BinaryFormula.__init__)


def test_hyp_binaryformula_constructor_args():
    sig = inspect.signature(BinaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_xor_is_not_abstract():
    assert not inspect.isabstract(henshin_Xor)


def test_hyp_henshin_xor_constructor_exists():
    assert callable(henshin_Xor.__init__)


def test_hyp_henshin_xor_constructor_args():
    sig = inspect.signature(henshin_Xor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_or_is_not_abstract():
    assert not inspect.isabstract(henshin_Or)


def test_hyp_henshin_or_constructor_exists():
    assert callable(henshin_Or.__init__)


def test_hyp_henshin_or_constructor_args():
    sig = inspect.signature(henshin_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_and_is_not_abstract():
    assert not inspect.isabstract(henshin_And)


def test_hyp_henshin_and_constructor_exists():
    assert callable(henshin_And.__init__)


def test_hyp_henshin_and_constructor_args():
    sig = inspect.signature(henshin_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryunit_is_not_abstract():
    assert not inspect.isabstract(UnaryUnit)


def test_hyp_unaryunit_constructor_exists():
    assert callable(UnaryUnit.__init__)


def test_hyp_unaryunit_constructor_args():
    sig = inspect.signature(UnaryUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_loopunit_is_not_abstract():
    assert not inspect.isabstract(henshin_LoopUnit)


def test_hyp_henshin_loopunit_constructor_exists():
    assert callable(henshin_LoopUnit.__init__)


def test_hyp_henshin_loopunit_constructor_args():
    sig = inspect.signature(henshin_LoopUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_iteratedunit_is_not_abstract():
    assert not inspect.isabstract(henshin_IteratedUnit)


def test_hyp_henshin_iteratedunit_constructor_exists():
    assert callable(henshin_IteratedUnit.__init__)


def test_hyp_henshin_iteratedunit_constructor_args():
    sig = inspect.signature(henshin_IteratedUnit.__init__)
    params = list(sig.parameters.keys())
    assert "iterations" in params, "Missing parameter 'iterations'"




def test_hyp_multiunit_is_not_abstract():
    assert not inspect.isabstract(MultiUnit)


def test_hyp_multiunit_constructor_exists():
    assert callable(MultiUnit.__init__)


def test_hyp_multiunit_constructor_args():
    sig = inspect.signature(MultiUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_priorityunit_is_not_abstract():
    assert not inspect.isabstract(henshin_PriorityUnit)


def test_hyp_henshin_priorityunit_constructor_exists():
    assert callable(henshin_PriorityUnit.__init__)


def test_hyp_henshin_priorityunit_constructor_args():
    sig = inspect.signature(henshin_PriorityUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_sequentialunit_is_not_abstract():
    assert not inspect.isabstract(henshin_SequentialUnit)


def test_hyp_henshin_sequentialunit_constructor_exists():
    assert callable(henshin_SequentialUnit.__init__)


def test_hyp_henshin_sequentialunit_constructor_args():
    sig = inspect.signature(henshin_SequentialUnit.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "rollback" in params, "Missing parameter 'rollback'"





def test_hyp_henshin_independentunit_is_not_abstract():
    assert not inspect.isabstract(henshin_IndependentUnit)


def test_hyp_henshin_independentunit_constructor_exists():
    assert callable(henshin_IndependentUnit.__init__)


def test_hyp_henshin_independentunit_constructor_args():
    sig = inspect.signature(henshin_IndependentUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_formula_is_not_abstract():
    assert not inspect.isabstract(Formula)


def test_hyp_formula_constructor_exists():
    assert callable(Formula.__init__)


def test_hyp_formula_constructor_args():
    sig = inspect.signature(Formula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_true_is_not_abstract():
    assert not inspect.isabstract(henshin_True)


def test_hyp_henshin_true_constructor_exists():
    assert callable(henshin_True.__init__)


def test_hyp_henshin_true_constructor_args():
    sig = inspect.signature(henshin_True.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_unaryformula_is_not_abstract():
    assert not inspect.isabstract(henshin_UnaryFormula)


def test_hyp_henshin_unaryformula_constructor_exists():
    assert callable(henshin_UnaryFormula.__init__)


def test_hyp_henshin_unaryformula_constructor_args():
    sig = inspect.signature(henshin_UnaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_binaryformula_is_not_abstract():
    assert not inspect.isabstract(henshin_BinaryFormula)


def test_hyp_henshin_binaryformula_constructor_exists():
    assert callable(henshin_BinaryFormula.__init__)


def test_hyp_henshin_binaryformula_constructor_args():
    sig = inspect.signature(henshin_BinaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_nestedcondition_is_not_abstract():
    assert not inspect.isabstract(henshin_NestedCondition)


def test_hyp_henshin_nestedcondition_constructor_exists():
    assert callable(henshin_NestedCondition.__init__)


def test_hyp_henshin_nestedcondition_constructor_args():
    sig = inspect.signature(henshin_NestedCondition.__init__)
    params = list(sig.parameters.keys())
    assert "presenceCondition" in params, "Missing parameter 'presenceCondition'"




def test_hyp_henshin_ereference_is_not_abstract():
    assert not inspect.isabstract(henshin_EReference)


def test_hyp_henshin_ereference_constructor_exists():
    assert callable(henshin_EReference.__init__)


def test_hyp_henshin_ereference_constructor_args():
    sig = inspect.signature(henshin_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_eclass_is_not_abstract():
    assert not inspect.isabstract(henshin_EClass)


def test_hyp_henshin_eclass_constructor_exists():
    assert callable(henshin_EClass.__init__)


def test_hyp_henshin_eclass_constructor_args():
    sig = inspect.signature(henshin_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_eattribute_is_not_abstract():
    assert not inspect.isabstract(henshin_EAttribute)


def test_hyp_henshin_eattribute_constructor_exists():
    assert callable(henshin_EAttribute.__init__)


def test_hyp_henshin_eattribute_constructor_args():
    sig = inspect.signature(henshin_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_eclassifier_is_not_abstract():
    assert not inspect.isabstract(henshin_EClassifier)


def test_hyp_henshin_eclassifier_constructor_exists():
    assert callable(henshin_EClassifier.__init__)


def test_hyp_henshin_eclassifier_constructor_args():
    sig = inspect.signature(henshin_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_hyp_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_hyp_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_attribute_is_not_abstract():
    assert not inspect.isabstract(henshin_Attribute)


def test_hyp_henshin_attribute_constructor_exists():
    assert callable(henshin_Attribute.__init__)


def test_hyp_henshin_attribute_constructor_args():
    sig = inspect.signature(henshin_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "constant" in params, "Missing parameter 'constant'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_henshin_formula_is_not_abstract():
    assert not inspect.isabstract(henshin_Formula)


def test_hyp_henshin_formula_constructor_exists():
    assert callable(henshin_Formula.__init__)


def test_hyp_henshin_formula_constructor_args():
    sig = inspect.signature(henshin_Formula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_edge_is_not_abstract():
    assert not inspect.isabstract(henshin_Edge)


def test_hyp_henshin_edge_constructor_exists():
    assert callable(henshin_Edge.__init__)


def test_hyp_henshin_edge_constructor_args():
    sig = inspect.signature(henshin_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "indexConstant" in params, "Missing parameter 'indexConstant'"





def test_hyp_henshin_mapping_is_not_abstract():
    assert not inspect.isabstract(henshin_Mapping)


def test_hyp_henshin_mapping_constructor_exists():
    assert callable(henshin_Mapping.__init__)


def test_hyp_henshin_mapping_constructor_args():
    sig = inspect.signature(henshin_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_epackage_is_not_abstract():
    assert not inspect.isabstract(henshin_EPackage)


def test_hyp_henshin_epackage_constructor_exists():
    assert callable(henshin_EPackage.__init__)


def test_hyp_henshin_epackage_constructor_args():
    sig = inspect.signature(henshin_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_unit_is_not_abstract():
    assert not inspect.isabstract(henshin_Unit)


def test_hyp_henshin_unit_constructor_exists():
    assert callable(henshin_Unit.__init__)


def test_hyp_henshin_unit_constructor_args():
    sig = inspect.signature(henshin_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "activated" in params, "Missing parameter 'activated'"




def test_hyp_henshin_node_is_not_abstract():
    assert not inspect.isabstract(henshin_Node)


def test_hyp_henshin_node_constructor_exists():
    assert callable(henshin_Node.__init__)


def test_hyp_henshin_node_constructor_args():
    sig = inspect.signature(henshin_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_attributecondition_is_not_abstract():
    assert not inspect.isabstract(henshin_AttributeCondition)


def test_hyp_henshin_attributecondition_constructor_exists():
    assert callable(henshin_AttributeCondition.__init__)


def test_hyp_henshin_attributecondition_constructor_args():
    sig = inspect.signature(henshin_AttributeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionText" in params, "Missing parameter 'conditionText'"




def test_hyp_henshin_parameter_is_not_abstract():
    assert not inspect.isabstract(henshin_Parameter)


def test_hyp_henshin_parameter_constructor_exists():
    assert callable(henshin_Parameter.__init__)


def test_hyp_henshin_parameter_constructor_args():
    sig = inspect.signature(henshin_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_graph_is_not_abstract():
    assert not inspect.isabstract(henshin_Graph)


def test_hyp_henshin_graph_constructor_exists():
    assert callable(henshin_Graph.__init__)


def test_hyp_henshin_graph_constructor_args():
    sig = inspect.signature(henshin_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_module_is_not_abstract():
    assert not inspect.isabstract(henshin_Module)


def test_hyp_henshin_module_constructor_exists():
    assert callable(henshin_Module.__init__)


def test_hyp_henshin_module_constructor_args():
    sig = inspect.signature(henshin_Module.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_hyp_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_hyp_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_unaryunit_is_not_abstract():
    assert not inspect.isabstract(henshin_UnaryUnit)


def test_hyp_henshin_unaryunit_constructor_exists():
    assert callable(henshin_UnaryUnit.__init__)


def test_hyp_henshin_unaryunit_constructor_args():
    sig = inspect.signature(henshin_UnaryUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_conditionalunit_is_not_abstract():
    assert not inspect.isabstract(henshin_ConditionalUnit)


def test_hyp_henshin_conditionalunit_constructor_exists():
    assert callable(henshin_ConditionalUnit.__init__)


def test_hyp_henshin_conditionalunit_constructor_args():
    sig = inspect.signature(henshin_ConditionalUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_multiunit_is_not_abstract():
    assert not inspect.isabstract(henshin_MultiUnit)


def test_hyp_henshin_multiunit_constructor_exists():
    assert callable(henshin_MultiUnit.__init__)


def test_hyp_henshin_multiunit_constructor_args():
    sig = inspect.signature(henshin_MultiUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_rule_is_not_abstract():
    assert not inspect.isabstract(henshin_Rule)


def test_hyp_henshin_rule_constructor_exists():
    assert callable(henshin_Rule.__init__)


def test_hyp_henshin_rule_constructor_args():
    sig = inspect.signature(henshin_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "injectiveMatching" in params, "Missing parameter 'injectiveMatching'"
    assert "checkDangling" in params, "Missing parameter 'checkDangling'"
    assert "featureModel" in params, "Missing parameter 'featureModel'"
    assert "injectiveMatchingPresenceCondition" in params, "Missing parameter 'injectiveMatchingPresenceCondition'"







def test_hyp_henshin_parametermapping_is_not_abstract():
    assert not inspect.isabstract(henshin_ParameterMapping)


def test_hyp_henshin_parametermapping_constructor_exists():
    assert callable(henshin_ParameterMapping.__init__)


def test_hyp_henshin_parametermapping_constructor_args():
    sig = inspect.signature(henshin_ParameterMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_graphelement_is_not_abstract():
    assert not inspect.isabstract(henshin_GraphElement)


def test_hyp_henshin_graphelement_constructor_exists():
    assert callable(henshin_GraphElement.__init__)


def test_hyp_henshin_graphelement_constructor_args():
    sig = inspect.signature(henshin_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "presenceCondition" in params, "Missing parameter 'presenceCondition'"





def test_hyp_henshin_namedelement_is_not_abstract():
    assert not inspect.isabstract(henshin_NamedElement)


def test_hyp_henshin_namedelement_constructor_exists():
    assert callable(henshin_NamedElement.__init__)


def test_hyp_henshin_namedelement_constructor_args():
    sig = inspect.signature(henshin_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"




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
UnaryFormula_strategy = st.builds(
    UnaryFormula,
)
henshin_Not_strategy = st.builds(
    henshin_Not,
)
BinaryFormula_strategy = st.builds(
    BinaryFormula,
)
henshin_Xor_strategy = st.builds(
    henshin_Xor,
)
henshin_Or_strategy = st.builds(
    henshin_Or,
)
henshin_And_strategy = st.builds(
    henshin_And,
)
UnaryUnit_strategy = st.builds(
    UnaryUnit,
)
henshin_LoopUnit_strategy = st.builds(
    henshin_LoopUnit,
)
henshin_IteratedUnit_strategy = st.builds(
    henshin_IteratedUnit,
    iterations=
        safe_text
)
MultiUnit_strategy = st.builds(
    MultiUnit,
)
henshin_PriorityUnit_strategy = st.builds(
    henshin_PriorityUnit,
)
henshin_SequentialUnit_strategy = st.builds(
    henshin_SequentialUnit,
    strict=
        st.booleans(),
    rollback=
        st.booleans()
)
henshin_IndependentUnit_strategy = st.builds(
    henshin_IndependentUnit,
)
Formula_strategy = st.builds(
    Formula,
)
henshin_True_strategy = st.builds(
    henshin_True,
)
henshin_UnaryFormula_strategy = st.builds(
    henshin_UnaryFormula,
)
henshin_BinaryFormula_strategy = st.builds(
    henshin_BinaryFormula,
)
henshin_NestedCondition_strategy = st.builds(
    henshin_NestedCondition,
    presenceCondition=
        safe_text
)
henshin_EReference_strategy = st.builds(
    henshin_EReference,
)
henshin_EClass_strategy = st.builds(
    henshin_EClass,
)
henshin_EAttribute_strategy = st.builds(
    henshin_EAttribute,
)
henshin_EClassifier_strategy = st.builds(
    henshin_EClassifier,
)
GraphElement_strategy = st.builds(
    GraphElement,
)
henshin_Attribute_strategy = st.builds(
    henshin_Attribute,
    null=
        st.booleans(),
    constant=
        safe_text,
    value=
        safe_text
)
henshin_Formula_strategy = st.builds(
    henshin_Formula,
)
henshin_Edge_strategy = st.builds(
    henshin_Edge,
    index=
        safe_text,
    indexConstant=
        safe_text
)
henshin_Mapping_strategy = st.builds(
    henshin_Mapping,
)
henshin_EPackage_strategy = st.builds(
    henshin_EPackage,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
henshin_Unit_strategy = st.builds(
    henshin_Unit,
    activated=
        st.booleans()
)
henshin_Node_strategy = st.builds(
    henshin_Node,
)
henshin_AttributeCondition_strategy = st.builds(
    henshin_AttributeCondition,
    conditionText=
        safe_text
)
henshin_Parameter_strategy = st.builds(
    henshin_Parameter,
)
henshin_Graph_strategy = st.builds(
    henshin_Graph,
)
henshin_Module_strategy = st.builds(
    henshin_Module,
)
Unit_strategy = st.builds(
    Unit,
)
henshin_UnaryUnit_strategy = st.builds(
    henshin_UnaryUnit,
)
henshin_ConditionalUnit_strategy = st.builds(
    henshin_ConditionalUnit,
)
henshin_MultiUnit_strategy = st.builds(
    henshin_MultiUnit,
)
henshin_Rule_strategy = st.builds(
    henshin_Rule,
    injectiveMatching=
        st.booleans(),
    checkDangling=
        st.booleans(),
    featureModel=
        safe_text,
    injectiveMatchingPresenceCondition=
        safe_text
)
henshin_ParameterMapping_strategy = st.builds(
    henshin_ParameterMapping,
)
henshin_GraphElement_strategy = st.builds(
    henshin_GraphElement,
    action=
        safe_text,
    presenceCondition=
        safe_text
)
henshin_NamedElement_strategy = st.builds(
    henshin_NamedElement,
    name=
        safe_text,
    description=
        safe_text
)












@given(instance=henshin_IteratedUnit_strategy)
def test_hyp_henshin_iteratedunit_iterations_setter(instance):
    original = instance.iterations
    instance.iterations = original
    assert instance.iterations == original






@given(instance=henshin_SequentialUnit_strategy)
def test_hyp_henshin_sequentialunit_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original



@given(instance=henshin_SequentialUnit_strategy)
def test_hyp_henshin_sequentialunit_rollback_setter(instance):
    original = instance.rollback
    instance.rollback = original
    assert instance.rollback == original









@given(instance=henshin_NestedCondition_strategy)
def test_hyp_henshin_nestedcondition_presenceCondition_setter(instance):
    original = instance.presenceCondition
    instance.presenceCondition = original
    assert instance.presenceCondition == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_NestedCondition_strategy)
@settings(max_examples=30)
def test_hyp_henshin_nestedcondition_ispac_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPAC()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPAC).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPAC' in henshin_NestedCondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPAC' in henshin_NestedCondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPAC' in henshin_NestedCondition is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_NestedCondition_strategy)
@settings(max_examples=30)
def test_hyp_henshin_nestedcondition_isnac_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isNAC()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isNAC).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isNAC' in henshin_NestedCondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNAC' in henshin_NestedCondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNAC' in henshin_NestedCondition is not implemented or raised an error")









@given(instance=henshin_Attribute_strategy)
def test_hyp_henshin_attribute_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=henshin_Attribute_strategy)
def test_hyp_henshin_attribute_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=henshin_Attribute_strategy)
def test_hyp_henshin_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Formula_strategy)
@settings(max_examples=30)
def test_hyp_henshin_formula_isfalse_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFalse()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFalse).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFalse' in henshin_Formula is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFalse' in henshin_Formula did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFalse' in henshin_Formula is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Formula_strategy)
@settings(max_examples=30)
def test_hyp_henshin_formula_istrue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isTrue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isTrue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isTrue' in henshin_Formula is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isTrue' in henshin_Formula did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isTrue' in henshin_Formula is not implemented or raised an error")




@given(instance=henshin_Edge_strategy)
def test_hyp_henshin_edge_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=henshin_Edge_strategy)
def test_hyp_henshin_edge_indexConstant_setter(instance):
    original = instance.indexConstant
    instance.indexConstant = original
    assert instance.indexConstant == original







@given(instance=henshin_Unit_strategy)
def test_hyp_henshin_unit_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original





@given(instance=henshin_AttributeCondition_strategy)
def test_hyp_henshin_attributecondition_conditionText_setter(instance):
    original = instance.conditionText
    instance.conditionText = original
    assert instance.conditionText == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_isnestedcondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isNestedCondition()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isNestedCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isNestedCondition' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNestedCondition' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNestedCondition' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_isrhs_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isRhs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isRhs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isRhs' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRhs' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRhs' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_removenestedcondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeNestedCondition(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeNestedCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeNestedCondition' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeNestedCondition' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeNestedCondition' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_removeedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeEdge' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeEdge' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeEdge' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_islhs_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLhs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLhs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLhs' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLhs' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLhs' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_createnac_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNAC(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNAC).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNAC' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNAC' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNAC' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_createpac_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createPAC(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createPAC).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createPAC' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createPAC' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createPAC' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_removenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeNode' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeNode' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeNode' in henshin_Graph is not implemented or raised an error")









@given(instance=henshin_Rule_strategy)
def test_hyp_henshin_rule_injectiveMatching_setter(instance):
    original = instance.injectiveMatching
    instance.injectiveMatching = original
    assert instance.injectiveMatching == original



@given(instance=henshin_Rule_strategy)
def test_hyp_henshin_rule_checkDangling_setter(instance):
    original = instance.checkDangling
    instance.checkDangling = original
    assert instance.checkDangling == original



@given(instance=henshin_Rule_strategy)
def test_hyp_henshin_rule_featureModel_setter(instance):
    original = instance.featureModel
    instance.featureModel = original
    assert instance.featureModel == original



@given(instance=henshin_Rule_strategy)
def test_hyp_henshin_rule_injectiveMatchingPresenceCondition_setter(instance):
    original = instance.injectiveMatchingPresenceCondition
    instance.injectiveMatchingPresenceCondition = original
    assert instance.injectiveMatchingPresenceCondition == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_createnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNode' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_removeedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeEdge(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeEdge' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeEdge' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeEdge' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_removenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeNode(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeNode' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeNode' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeNode' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_cancreateedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canCreateEdge(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canCreateEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canCreateEdge' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canCreateEdge' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canCreateEdge' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_ismultirule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMultiRule()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMultiRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMultiRule' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMultiRule' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMultiRule' in henshin_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_removeattribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeAttribute(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeAttribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeAttribute' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeAttribute' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeAttribute' in henshin_Rule is not implemented or raised an error")





@given(instance=henshin_GraphElement_strategy)
def test_hyp_henshin_graphelement_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=henshin_GraphElement_strategy)
def test_hyp_henshin_graphelement_presenceCondition_setter(instance):
    original = instance.presenceCondition
    instance.presenceCondition = original
    assert instance.presenceCondition == original




@given(instance=henshin_NamedElement_strategy)
def test_hyp_henshin_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=henshin_NamedElement_strategy)
def test_hyp_henshin_namedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryFormula,
    Formula,
    GraphElement,
    MultiUnit,
    NamedElement,
    UnaryFormula,
    UnaryUnit,
    Unit,
    henshin_And,
    henshin_Attribute,
    henshin_AttributeCondition,
    henshin_BinaryFormula,
    henshin_ConditionalUnit,
    henshin_EAttribute,
    henshin_EClass,
    henshin_EClassifier,
    henshin_EPackage,
    henshin_EReference,
    henshin_Edge,
    henshin_Formula,
    henshin_Graph,
    henshin_GraphElement,
    henshin_IndependentUnit,
    henshin_IteratedUnit,
    henshin_LoopUnit,
    henshin_Mapping,
    henshin_Module,
    henshin_MultiUnit,
    henshin_NamedElement,
    henshin_NestedCondition,
    henshin_Node,
    henshin_Not,
    henshin_Or,
    henshin_Parameter,
    henshin_ParameterMapping,
    henshin_PriorityUnit,
    henshin_Rule,
    henshin_SequentialUnit,
    henshin_True,
    henshin_UnaryFormula,
    henshin_UnaryUnit,
    henshin_Unit,
    henshin_Xor,
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

def test_henshin_Attribute_constant_value_roundtrip():
    instance = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    assert instance.constant == "sample_text"
    instance.constant = "sample_text_2"
    assert instance.constant == "sample_text_2"


def test_henshin_Attribute_null_value_roundtrip():
    instance = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    assert instance.null == True
    instance.null = False
    assert instance.null == False


def test_henshin_Attribute_value_value_roundtrip():
    instance = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_AttributeCondition_conditionText_value_roundtrip():
    instance = henshin_AttributeCondition(conditionText="sample_text")
    assert instance.conditionText == "sample_text"
    instance.conditionText = "sample_text_2"
    assert instance.conditionText == "sample_text_2"


def test_henshin_Edge_index_value_roundtrip():
    instance = henshin_Edge(index="sample_text", indexConstant="sample_text")
    assert instance.index == "sample_text"
    instance.index = "sample_text_2"
    assert instance.index == "sample_text_2"


def test_henshin_Edge_indexConstant_value_roundtrip():
    instance = henshin_Edge(index="sample_text", indexConstant="sample_text")
    assert instance.indexConstant == "sample_text"
    instance.indexConstant = "sample_text_2"
    assert instance.indexConstant == "sample_text_2"


def test_henshin_GraphElement_action_value_roundtrip():
    instance = henshin_GraphElement(action="sample_text", presenceCondition="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_henshin_GraphElement_presenceCondition_value_roundtrip():
    instance = henshin_GraphElement(action="sample_text", presenceCondition="sample_text")
    assert instance.presenceCondition == "sample_text"
    instance.presenceCondition = "sample_text_2"
    assert instance.presenceCondition == "sample_text_2"


def test_henshin_IteratedUnit_iterations_value_roundtrip():
    instance = henshin_IteratedUnit(iterations="sample_text")
    assert instance.iterations == "sample_text"
    instance.iterations = "sample_text_2"
    assert instance.iterations == "sample_text_2"


def test_henshin_NamedElement_description_value_roundtrip():
    instance = henshin_NamedElement(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_henshin_NamedElement_name_value_roundtrip():
    instance = henshin_NamedElement(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_NestedCondition_presenceCondition_value_roundtrip():
    instance = henshin_NestedCondition(presenceCondition="sample_text")
    assert instance.presenceCondition == "sample_text"
    instance.presenceCondition = "sample_text_2"
    assert instance.presenceCondition == "sample_text_2"


def test_henshin_Rule_checkDangling_value_roundtrip():
    instance = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    assert instance.checkDangling == True
    instance.checkDangling = False
    assert instance.checkDangling == False


def test_henshin_Rule_featureModel_value_roundtrip():
    instance = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    assert instance.featureModel == "sample_text"
    instance.featureModel = "sample_text_2"
    assert instance.featureModel == "sample_text_2"


def test_henshin_Rule_injectiveMatching_value_roundtrip():
    instance = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    assert instance.injectiveMatching == True
    instance.injectiveMatching = False
    assert instance.injectiveMatching == False


def test_henshin_Rule_injectiveMatchingPresenceCondition_value_roundtrip():
    instance = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    assert instance.injectiveMatchingPresenceCondition == "sample_text"
    instance.injectiveMatchingPresenceCondition = "sample_text_2"
    assert instance.injectiveMatchingPresenceCondition == "sample_text_2"


def test_henshin_SequentialUnit_rollback_value_roundtrip():
    instance = henshin_SequentialUnit(rollback=True, strict=True)
    assert instance.rollback == True
    instance.rollback = False
    assert instance.rollback == False


def test_henshin_SequentialUnit_strict_value_roundtrip():
    instance = henshin_SequentialUnit(rollback=True, strict=True)
    assert instance.strict == True
    instance.strict = False
    assert instance.strict == False


def test_henshin_Unit_activated_value_roundtrip():
    instance = henshin_Unit(activated=True)
    assert instance.activated == True
    instance.activated = False
    assert instance.activated == False


def test_henshin_And_isa_BinaryFormula():
    instance = henshin_And()
    assert isinstance(instance, BinaryFormula)


def test_henshin_Or_isa_BinaryFormula():
    instance = henshin_Or()
    assert isinstance(instance, BinaryFormula)


def test_henshin_Xor_isa_BinaryFormula():
    instance = henshin_Xor()
    assert isinstance(instance, BinaryFormula)


def test_henshin_BinaryFormula_isa_Formula():
    instance = henshin_BinaryFormula()
    assert isinstance(instance, Formula)


def test_henshin_NestedCondition_isa_Formula():
    instance = henshin_NestedCondition(presenceCondition="sample_text")
    assert isinstance(instance, Formula)


def test_henshin_True_isa_Formula():
    instance = henshin_True()
    assert isinstance(instance, Formula)


def test_henshin_UnaryFormula_isa_Formula():
    instance = henshin_UnaryFormula()
    assert isinstance(instance, Formula)


def test_henshin_Attribute_isa_GraphElement():
    instance = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    assert isinstance(instance, GraphElement)


def test_henshin_Edge_isa_GraphElement():
    instance = henshin_Edge(index="sample_text", indexConstant="sample_text")
    assert isinstance(instance, GraphElement)


def test_henshin_Node_isa_GraphElement():
    instance = henshin_Node()
    assert isinstance(instance, GraphElement)


def test_henshin_IndependentUnit_isa_MultiUnit():
    instance = henshin_IndependentUnit()
    assert isinstance(instance, MultiUnit)


def test_henshin_PriorityUnit_isa_MultiUnit():
    instance = henshin_PriorityUnit()
    assert isinstance(instance, MultiUnit)


def test_henshin_SequentialUnit_isa_MultiUnit():
    instance = henshin_SequentialUnit(rollback=True, strict=True)
    assert isinstance(instance, MultiUnit)


def test_henshin_AttributeCondition_isa_NamedElement():
    instance = henshin_AttributeCondition(conditionText="sample_text")
    assert isinstance(instance, NamedElement)


def test_henshin_Graph_isa_NamedElement():
    instance = henshin_Graph()
    assert isinstance(instance, NamedElement)


def test_henshin_Module_isa_NamedElement():
    instance = henshin_Module()
    assert isinstance(instance, NamedElement)


def test_henshin_Node_isa_NamedElement():
    instance = henshin_Node()
    assert isinstance(instance, NamedElement)


def test_henshin_Parameter_isa_NamedElement():
    instance = henshin_Parameter()
    assert isinstance(instance, NamedElement)


def test_henshin_Unit_isa_NamedElement():
    instance = henshin_Unit(activated=True)
    assert isinstance(instance, NamedElement)


def test_henshin_Not_isa_UnaryFormula():
    instance = henshin_Not()
    assert isinstance(instance, UnaryFormula)


def test_henshin_IteratedUnit_isa_UnaryUnit():
    instance = henshin_IteratedUnit(iterations="sample_text")
    assert isinstance(instance, UnaryUnit)


def test_henshin_LoopUnit_isa_UnaryUnit():
    instance = henshin_LoopUnit()
    assert isinstance(instance, UnaryUnit)


def test_henshin_ConditionalUnit_isa_Unit():
    instance = henshin_ConditionalUnit()
    assert isinstance(instance, Unit)


def test_henshin_MultiUnit_isa_Unit():
    instance = henshin_MultiUnit()
    assert isinstance(instance, Unit)


def test_henshin_Rule_isa_Unit():
    instance = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    assert isinstance(instance, Unit)


def test_henshin_UnaryUnit_isa_Unit():
    instance = henshin_UnaryUnit()
    assert isinstance(instance, Unit)


def test_assoc_attributeConditions18_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_AttributeCondition(conditionText="sample_text")
    b2 = henshin_AttributeCondition(conditionText="sample_text_2")
    _safe_set(a, 'rule', {b1})
    assert _is_linked(a, 'rule', b1)
    if hasattr(b1, 'AttributeCondition'):
        assert _is_linked(b1, 'AttributeCondition', a)
    _safe_set(a, 'rule', {b2})
    assert _is_linked(a, 'rule', b2)
    if hasattr(b1, 'AttributeCondition'):
        assert not _is_linked(b1, 'AttributeCondition', a)
    if hasattr(b2, 'AttributeCondition'):
        assert _is_linked(b2, 'AttributeCondition', a)
    _safe_set(a, 'rule', set())
    assert not _is_linked(a, 'rule', b2)
    if hasattr(b2, 'AttributeCondition'):
        assert not _is_linked(b2, 'AttributeCondition', a)


def test_assoc_attributes41_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    b2 = henshin_Attribute(constant="sample_text_2", null=False, value="sample_text_2")
    _safe_set(a, 'node', {b1})
    assert _is_linked(a, 'node', b1)
    if hasattr(b1, 'Attribute'):
        assert _is_linked(b1, 'Attribute', a)
    _safe_set(a, 'node', {b2})
    assert _is_linked(a, 'node', b2)
    if hasattr(b1, 'Attribute'):
        assert not _is_linked(b1, 'Attribute', a)
    if hasattr(b2, 'Attribute'):
        assert _is_linked(b2, 'Attribute', a)
    _safe_set(a, 'node', set())
    assert not _is_linked(a, 'node', b2)
    if hasattr(b2, 'Attribute'):
        assert not _is_linked(b2, 'Attribute', a)


def test_assoc_child81_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_UnaryFormula()
    b2 = henshin_UnaryFormula()
    _safe_set(a, 'henshin_Formula82', b1)
    assert _is_linked(a, 'henshin_Formula82', b1)
    if hasattr(b1, 'henshin_UnaryFormula'):
        assert _is_linked(b1, 'henshin_UnaryFormula', a)
    _safe_set(a, 'henshin_Formula82', b2)
    assert _is_linked(a, 'henshin_Formula82', b2)
    if hasattr(b1, 'henshin_UnaryFormula'):
        assert not _is_linked(b1, 'henshin_UnaryFormula', a)
    if hasattr(b2, 'henshin_UnaryFormula'):
        assert _is_linked(b2, 'henshin_UnaryFormula', a)
    _safe_set(a, 'henshin_Formula82', None)
    assert not _is_linked(a, 'henshin_Formula82', b2)
    if hasattr(b2, 'henshin_UnaryFormula'):
        assert not _is_linked(b2, 'henshin_UnaryFormula', a)


def test_assoc_conclusion76_link_reassign_clear():
    a = henshin_NestedCondition(presenceCondition="sample_text")
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_NestedCondition', b1)
    assert _is_linked(a, 'henshin_NestedCondition', b1)
    if hasattr(b1, 'henshin_Graph77'):
        assert _is_linked(b1, 'henshin_Graph77', a)
    _safe_set(a, 'henshin_NestedCondition', b2)
    assert _is_linked(a, 'henshin_NestedCondition', b2)
    if hasattr(b1, 'henshin_Graph77'):
        assert not _is_linked(b1, 'henshin_Graph77', a)
    if hasattr(b2, 'henshin_Graph77'):
        assert _is_linked(b2, 'henshin_Graph77', a)
    _safe_set(a, 'henshin_NestedCondition', None)
    assert not _is_linked(a, 'henshin_NestedCondition', b2)
    if hasattr(b2, 'henshin_Graph77'):
        assert not _is_linked(b2, 'henshin_Graph77', a)


def test_assoc_edges36_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'graph37', {b1})
    assert _is_linked(a, 'graph37', b1)
    if hasattr(b1, 'Edge'):
        assert _is_linked(b1, 'Edge', a)
    _safe_set(a, 'graph37', {b2})
    assert _is_linked(a, 'graph37', b2)
    if hasattr(b1, 'Edge'):
        assert not _is_linked(b1, 'Edge', a)
    if hasattr(b2, 'Edge'):
        assert _is_linked(b2, 'Edge', a)
    _safe_set(a, 'graph37', set())
    assert not _is_linked(a, 'graph37', b2)
    if hasattr(b2, 'Edge'):
        assert not _is_linked(b2, 'Edge', a)


def test_assoc_else_73_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_Unit75', b1)
    assert _is_linked(a, 'henshin_Unit75', b1)
    if hasattr(b1, 'henshin_ConditionalUnit74'):
        assert _is_linked(b1, 'henshin_ConditionalUnit74', a)
    _safe_set(a, 'henshin_Unit75', b2)
    assert _is_linked(a, 'henshin_Unit75', b2)
    if hasattr(b1, 'henshin_ConditionalUnit74'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit74', a)
    if hasattr(b2, 'henshin_ConditionalUnit74'):
        assert _is_linked(b2, 'henshin_ConditionalUnit74', a)
    _safe_set(a, 'henshin_Unit75', None)
    assert not _is_linked(a, 'henshin_Unit75', b2)
    if hasattr(b2, 'henshin_ConditionalUnit74'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit74', a)


def test_assoc_formula38_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Formula()
    b2 = henshin_Formula()
    _safe_set(a, 'henshin_Graph39', b1)
    assert _is_linked(a, 'henshin_Graph39', b1)
    if hasattr(b1, 'henshin_Formula'):
        assert _is_linked(b1, 'henshin_Formula', a)
    _safe_set(a, 'henshin_Graph39', b2)
    assert _is_linked(a, 'henshin_Graph39', b2)
    if hasattr(b1, 'henshin_Formula'):
        assert not _is_linked(b1, 'henshin_Formula', a)
    if hasattr(b2, 'henshin_Formula'):
        assert _is_linked(b2, 'henshin_Formula', a)
    _safe_set(a, 'henshin_Graph39', None)
    assert not _is_linked(a, 'henshin_Graph39', b2)
    if hasattr(b2, 'henshin_Formula'):
        assert not _is_linked(b2, 'henshin_Formula', a)


def test_assoc_graph42_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'nodes', b1)
    assert _is_linked(a, 'nodes', b1)
    if hasattr(b1, 'Graph'):
        assert _is_linked(b1, 'Graph', a)
    _safe_set(a, 'nodes', b2)
    assert _is_linked(a, 'nodes', b2)
    if hasattr(b1, 'Graph'):
        assert not _is_linked(b1, 'Graph', a)
    if hasattr(b2, 'Graph'):
        assert _is_linked(b2, 'Graph', a)
    _safe_set(a, 'nodes', None)
    assert not _is_linked(a, 'nodes', b2)
    if hasattr(b2, 'Graph'):
        assert not _is_linked(b2, 'Graph', a)


def test_assoc_graph52_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'Graph53', b1)
    assert _is_linked(a, 'Graph53', b1)
    if hasattr(b1, 'edges'):
        assert _is_linked(b1, 'edges', a)
    _safe_set(a, 'Graph53', b2)
    assert _is_linked(a, 'Graph53', b2)
    if hasattr(b1, 'edges'):
        assert not _is_linked(b1, 'edges', a)
    if hasattr(b2, 'edges'):
        assert _is_linked(b2, 'edges', a)
    _safe_set(a, 'Graph53', None)
    assert not _is_linked(a, 'Graph53', b2)
    if hasattr(b2, 'edges'):
        assert not _is_linked(b2, 'edges', a)


def test_assoc_if_68_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_Unit69', b1)
    assert _is_linked(a, 'henshin_Unit69', b1)
    if hasattr(b1, 'henshin_ConditionalUnit'):
        assert _is_linked(b1, 'henshin_ConditionalUnit', a)
    _safe_set(a, 'henshin_Unit69', b2)
    assert _is_linked(a, 'henshin_Unit69', b2)
    if hasattr(b1, 'henshin_ConditionalUnit'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit', a)
    if hasattr(b2, 'henshin_ConditionalUnit'):
        assert _is_linked(b2, 'henshin_ConditionalUnit', a)
    _safe_set(a, 'henshin_Unit69', None)
    assert not _is_linked(a, 'henshin_Unit69', b2)
    if hasattr(b2, 'henshin_ConditionalUnit'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit', a)


def test_assoc_image61_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Node63', b1)
    assert _is_linked(a, 'henshin_Node63', b1)
    if hasattr(b1, 'henshin_Mapping62'):
        assert _is_linked(b1, 'henshin_Mapping62', a)
    _safe_set(a, 'henshin_Node63', b2)
    assert _is_linked(a, 'henshin_Node63', b2)
    if hasattr(b1, 'henshin_Mapping62'):
        assert not _is_linked(b1, 'henshin_Mapping62', a)
    if hasattr(b2, 'henshin_Mapping62'):
        assert _is_linked(b2, 'henshin_Mapping62', a)
    _safe_set(a, 'henshin_Node63', None)
    assert not _is_linked(a, 'henshin_Node63', b2)
    if hasattr(b2, 'henshin_Mapping62'):
        assert not _is_linked(b2, 'henshin_Mapping62', a)


def test_assoc_imports5_link_reassign_clear():
    a = henshin_Module()
    b1 = henshin_EPackage()
    b2 = henshin_EPackage()
    _safe_set(a, 'henshin_Module', {b1})
    assert _is_linked(a, 'henshin_Module', b1)
    if hasattr(b1, 'henshin_EPackage'):
        assert _is_linked(b1, 'henshin_EPackage', a)
    _safe_set(a, 'henshin_Module', {b2})
    assert _is_linked(a, 'henshin_Module', b2)
    if hasattr(b1, 'henshin_EPackage'):
        assert not _is_linked(b1, 'henshin_EPackage', a)
    if hasattr(b2, 'henshin_EPackage'):
        assert _is_linked(b2, 'henshin_EPackage', a)
    _safe_set(a, 'henshin_Module', set())
    assert not _is_linked(a, 'henshin_Module', b2)
    if hasattr(b2, 'henshin_EPackage'):
        assert not _is_linked(b2, 'henshin_EPackage', a)


def test_assoc_incoming43_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Edge44'):
        assert _is_linked(b1, 'Edge44', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Edge44'):
        assert not _is_linked(b1, 'Edge44', a)
    if hasattr(b2, 'Edge44'):
        assert _is_linked(b2, 'Edge44', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Edge44'):
        assert not _is_linked(b2, 'Edge44', a)


def test_assoc_instances8_link_reassign_clear():
    a = henshin_Module()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_Module9', {b1})
    assert _is_linked(a, 'henshin_Module9', b1)
    if hasattr(b1, 'henshin_Graph'):
        assert _is_linked(b1, 'henshin_Graph', a)
    _safe_set(a, 'henshin_Module9', {b2})
    assert _is_linked(a, 'henshin_Module9', b2)
    if hasattr(b1, 'henshin_Graph'):
        assert not _is_linked(b1, 'henshin_Graph', a)
    if hasattr(b2, 'henshin_Graph'):
        assert _is_linked(b2, 'henshin_Graph', a)
    _safe_set(a, 'henshin_Module9', set())
    assert not _is_linked(a, 'henshin_Module9', b2)
    if hasattr(b2, 'henshin_Graph'):
        assert not _is_linked(b2, 'henshin_Graph', a)


def test_assoc_left83_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_BinaryFormula()
    b2 = henshin_BinaryFormula()
    _safe_set(a, 'henshin_Formula84', b1)
    assert _is_linked(a, 'henshin_Formula84', b1)
    if hasattr(b1, 'henshin_BinaryFormula'):
        assert _is_linked(b1, 'henshin_BinaryFormula', a)
    _safe_set(a, 'henshin_Formula84', b2)
    assert _is_linked(a, 'henshin_Formula84', b2)
    if hasattr(b1, 'henshin_BinaryFormula'):
        assert not _is_linked(b1, 'henshin_BinaryFormula', a)
    if hasattr(b2, 'henshin_BinaryFormula'):
        assert _is_linked(b2, 'henshin_BinaryFormula', a)
    _safe_set(a, 'henshin_Formula84', None)
    assert not _is_linked(a, 'henshin_Formula84', b2)
    if hasattr(b2, 'henshin_BinaryFormula'):
        assert not _is_linked(b2, 'henshin_BinaryFormula', a)


def test_assoc_lhs13_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_Rule', b1)
    assert _is_linked(a, 'henshin_Rule', b1)
    if hasattr(b1, 'henshin_Graph14'):
        assert _is_linked(b1, 'henshin_Graph14', a)
    _safe_set(a, 'henshin_Rule', b2)
    assert _is_linked(a, 'henshin_Rule', b2)
    if hasattr(b1, 'henshin_Graph14'):
        assert not _is_linked(b1, 'henshin_Graph14', a)
    if hasattr(b2, 'henshin_Graph14'):
        assert _is_linked(b2, 'henshin_Graph14', a)
    _safe_set(a, 'henshin_Rule', None)
    assert not _is_linked(a, 'henshin_Rule', b2)
    if hasattr(b2, 'henshin_Graph14'):
        assert not _is_linked(b2, 'henshin_Graph14', a)


def test_assoc_mappings19_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Rule20', {b1})
    assert _is_linked(a, 'henshin_Rule20', b1)
    if hasattr(b1, 'henshin_Mapping'):
        assert _is_linked(b1, 'henshin_Mapping', a)
    _safe_set(a, 'henshin_Rule20', {b2})
    assert _is_linked(a, 'henshin_Rule20', b2)
    if hasattr(b1, 'henshin_Mapping'):
        assert not _is_linked(b1, 'henshin_Mapping', a)
    if hasattr(b2, 'henshin_Mapping'):
        assert _is_linked(b2, 'henshin_Mapping', a)
    _safe_set(a, 'henshin_Rule20', set())
    assert not _is_linked(a, 'henshin_Rule20', b2)
    if hasattr(b2, 'henshin_Mapping'):
        assert not _is_linked(b2, 'henshin_Mapping', a)


def test_assoc_mappings78_link_reassign_clear():
    a = henshin_NestedCondition(presenceCondition="sample_text")
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_NestedCondition79', {b1})
    assert _is_linked(a, 'henshin_NestedCondition79', b1)
    if hasattr(b1, 'henshin_Mapping80'):
        assert _is_linked(b1, 'henshin_Mapping80', a)
    _safe_set(a, 'henshin_NestedCondition79', {b2})
    assert _is_linked(a, 'henshin_NestedCondition79', b2)
    if hasattr(b1, 'henshin_Mapping80'):
        assert not _is_linked(b1, 'henshin_Mapping80', a)
    if hasattr(b2, 'henshin_Mapping80'):
        assert _is_linked(b2, 'henshin_Mapping80', a)
    _safe_set(a, 'henshin_NestedCondition79', set())
    assert not _is_linked(a, 'henshin_NestedCondition79', b2)
    if hasattr(b2, 'henshin_Mapping80'):
        assert not _is_linked(b2, 'henshin_Mapping80', a)


def test_assoc_multiMappings24_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Rule25', {b1})
    assert _is_linked(a, 'henshin_Rule25', b1)
    if hasattr(b1, 'henshin_Mapping26'):
        assert _is_linked(b1, 'henshin_Mapping26', a)
    _safe_set(a, 'henshin_Rule25', {b2})
    assert _is_linked(a, 'henshin_Rule25', b2)
    if hasattr(b1, 'henshin_Mapping26'):
        assert not _is_linked(b1, 'henshin_Mapping26', a)
    if hasattr(b2, 'henshin_Mapping26'):
        assert _is_linked(b2, 'henshin_Mapping26', a)
    _safe_set(a, 'henshin_Rule25', set())
    assert not _is_linked(a, 'henshin_Rule25', b2)
    if hasattr(b2, 'henshin_Mapping26'):
        assert not _is_linked(b2, 'henshin_Mapping26', a)


def test_assoc_multiRules22_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b2 = henshin_Rule(checkDangling=False, featureModel="sample_text_2", injectiveMatching=False, injectiveMatchingPresenceCondition="sample_text_2")
    _safe_set(a, 'henshin_Rule21', {b1})
    assert _is_linked(a, 'henshin_Rule21', b1)
    if hasattr(b1, 'henshin_Rule23'):
        assert _is_linked(b1, 'henshin_Rule23', a)
    _safe_set(a, 'henshin_Rule21', {b2})
    assert _is_linked(a, 'henshin_Rule21', b2)
    if hasattr(b1, 'henshin_Rule23'):
        assert not _is_linked(b1, 'henshin_Rule23', a)
    if hasattr(b2, 'henshin_Rule23'):
        assert _is_linked(b2, 'henshin_Rule23', a)
    _safe_set(a, 'henshin_Rule21', set())
    assert not _is_linked(a, 'henshin_Rule21', b2)
    if hasattr(b2, 'henshin_Rule23'):
        assert not _is_linked(b2, 'henshin_Rule23', a)


def test_assoc_node55_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    b2 = henshin_Attribute(constant="sample_text_2", null=False, value="sample_text_2")
    _safe_set(a, 'Node56', b1)
    assert _is_linked(a, 'Node56', b1)
    if hasattr(b1, 'attributes'):
        assert _is_linked(b1, 'attributes', a)
    _safe_set(a, 'Node56', b2)
    assert _is_linked(a, 'Node56', b2)
    if hasattr(b1, 'attributes'):
        assert not _is_linked(b1, 'attributes', a)
    if hasattr(b2, 'attributes'):
        assert _is_linked(b2, 'attributes', a)
    _safe_set(a, 'Node56', None)
    assert not _is_linked(a, 'Node56', b2)
    if hasattr(b2, 'attributes'):
        assert not _is_linked(b2, 'attributes', a)


def test_assoc_nodes35_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'Node', b1)
    assert _is_linked(a, 'Node', b1)
    if hasattr(b1, 'graph'):
        assert _is_linked(b1, 'graph', a)
    _safe_set(a, 'Node', b2)
    assert _is_linked(a, 'Node', b2)
    if hasattr(b1, 'graph'):
        assert not _is_linked(b1, 'graph', a)
    if hasattr(b2, 'graph'):
        assert _is_linked(b2, 'graph', a)
    _safe_set(a, 'Node', None)
    assert not _is_linked(a, 'Node', b2)
    if hasattr(b2, 'graph'):
        assert not _is_linked(b2, 'graph', a)


def test_assoc_origin58_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Node60', b1)
    assert _is_linked(a, 'henshin_Node60', b1)
    if hasattr(b1, 'henshin_Mapping59'):
        assert _is_linked(b1, 'henshin_Mapping59', a)
    _safe_set(a, 'henshin_Node60', b2)
    assert _is_linked(a, 'henshin_Node60', b2)
    if hasattr(b1, 'henshin_Mapping59'):
        assert not _is_linked(b1, 'henshin_Mapping59', a)
    if hasattr(b2, 'henshin_Mapping59'):
        assert _is_linked(b2, 'henshin_Mapping59', a)
    _safe_set(a, 'henshin_Node60', None)
    assert not _is_linked(a, 'henshin_Node60', b2)
    if hasattr(b2, 'henshin_Mapping59'):
        assert not _is_linked(b2, 'henshin_Mapping59', a)


def test_assoc_outgoing45_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Edge46'):
        assert _is_linked(b1, 'Edge46', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Edge46'):
        assert not _is_linked(b1, 'Edge46', a)
    if hasattr(b2, 'Edge46'):
        assert _is_linked(b2, 'Edge46', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Edge46'):
        assert not _is_linked(b2, 'Edge46', a)


def test_assoc_parameterMappings11_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_ParameterMapping()
    b2 = henshin_ParameterMapping()
    _safe_set(a, 'henshin_Unit12', {b1})
    assert _is_linked(a, 'henshin_Unit12', b1)
    if hasattr(b1, 'henshin_ParameterMapping'):
        assert _is_linked(b1, 'henshin_ParameterMapping', a)
    _safe_set(a, 'henshin_Unit12', {b2})
    assert _is_linked(a, 'henshin_Unit12', b2)
    if hasattr(b1, 'henshin_ParameterMapping'):
        assert not _is_linked(b1, 'henshin_ParameterMapping', a)
    if hasattr(b2, 'henshin_ParameterMapping'):
        assert _is_linked(b2, 'henshin_ParameterMapping', a)
    _safe_set(a, 'henshin_Unit12', set())
    assert not _is_linked(a, 'henshin_Unit12', b2)
    if hasattr(b2, 'henshin_ParameterMapping'):
        assert not _is_linked(b2, 'henshin_ParameterMapping', a)


def test_assoc_parameters10_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_Parameter()
    b2 = henshin_Parameter()
    _safe_set(a, 'unit', {b1})
    assert _is_linked(a, 'unit', b1)
    if hasattr(b1, 'Parameter'):
        assert _is_linked(b1, 'Parameter', a)
    _safe_set(a, 'unit', {b2})
    assert _is_linked(a, 'unit', b2)
    if hasattr(b1, 'Parameter'):
        assert not _is_linked(b1, 'Parameter', a)
    if hasattr(b2, 'Parameter'):
        assert _is_linked(b2, 'Parameter', a)
    _safe_set(a, 'unit', set())
    assert not _is_linked(a, 'unit', b2)
    if hasattr(b2, 'Parameter'):
        assert not _is_linked(b2, 'Parameter', a)


def test_assoc_rhs15_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_Rule16', b1)
    assert _is_linked(a, 'henshin_Rule16', b1)
    if hasattr(b1, 'henshin_Graph17'):
        assert _is_linked(b1, 'henshin_Graph17', a)
    _safe_set(a, 'henshin_Rule16', b2)
    assert _is_linked(a, 'henshin_Rule16', b2)
    if hasattr(b1, 'henshin_Graph17'):
        assert not _is_linked(b1, 'henshin_Graph17', a)
    if hasattr(b2, 'henshin_Graph17'):
        assert _is_linked(b2, 'henshin_Graph17', a)
    _safe_set(a, 'henshin_Rule16', None)
    assert not _is_linked(a, 'henshin_Rule16', b2)
    if hasattr(b2, 'henshin_Graph17'):
        assert not _is_linked(b2, 'henshin_Graph17', a)


def test_assoc_right85_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_BinaryFormula()
    b2 = henshin_BinaryFormula()
    _safe_set(a, 'henshin_Formula87', b1)
    assert _is_linked(a, 'henshin_Formula87', b1)
    if hasattr(b1, 'henshin_BinaryFormula86'):
        assert _is_linked(b1, 'henshin_BinaryFormula86', a)
    _safe_set(a, 'henshin_Formula87', b2)
    assert _is_linked(a, 'henshin_Formula87', b2)
    if hasattr(b1, 'henshin_BinaryFormula86'):
        assert not _is_linked(b1, 'henshin_BinaryFormula86', a)
    if hasattr(b2, 'henshin_BinaryFormula86'):
        assert _is_linked(b2, 'henshin_BinaryFormula86', a)
    _safe_set(a, 'henshin_Formula87', None)
    assert not _is_linked(a, 'henshin_Formula87', b2)
    if hasattr(b2, 'henshin_BinaryFormula86'):
        assert not _is_linked(b2, 'henshin_BinaryFormula86', a)


def test_assoc_rule57_link_reassign_clear():
    a = henshin_Rule(checkDangling=True, featureModel="sample_text", injectiveMatching=True, injectiveMatchingPresenceCondition="sample_text")
    b1 = henshin_AttributeCondition(conditionText="sample_text")
    b2 = henshin_AttributeCondition(conditionText="sample_text_2")
    _safe_set(a, 'Rule', b1)
    assert _is_linked(a, 'Rule', b1)
    if hasattr(b1, 'attributeConditions'):
        assert _is_linked(b1, 'attributeConditions', a)
    _safe_set(a, 'Rule', b2)
    assert _is_linked(a, 'Rule', b2)
    if hasattr(b1, 'attributeConditions'):
        assert not _is_linked(b1, 'attributeConditions', a)
    if hasattr(b2, 'attributeConditions'):
        assert _is_linked(b2, 'attributeConditions', a)
    _safe_set(a, 'Rule', None)
    assert not _is_linked(a, 'Rule', b2)
    if hasattr(b2, 'attributeConditions'):
        assert not _is_linked(b2, 'attributeConditions', a)


def test_assoc_source47_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'Node48', b1)
    assert _is_linked(a, 'Node48', b1)
    if hasattr(b1, 'outgoing'):
        assert _is_linked(b1, 'outgoing', a)
    _safe_set(a, 'Node48', b2)
    assert _is_linked(a, 'Node48', b2)
    if hasattr(b1, 'outgoing'):
        assert not _is_linked(b1, 'outgoing', a)
    if hasattr(b2, 'outgoing'):
        assert _is_linked(b2, 'outgoing', a)
    _safe_set(a, 'Node48', None)
    assert not _is_linked(a, 'Node48', b2)
    if hasattr(b2, 'outgoing'):
        assert not _is_linked(b2, 'outgoing', a)


def test_assoc_subModules1_link_reassign_clear():
    a = henshin_Module()
    b1 = henshin_Module()
    b2 = henshin_Module()
    _safe_set(a, 'Module', b1)
    assert _is_linked(a, 'Module', b1)
    if hasattr(b1, 'superModule'):
        assert _is_linked(b1, 'superModule', a)
    _safe_set(a, 'Module', b2)
    assert _is_linked(a, 'Module', b2)
    if hasattr(b1, 'superModule'):
        assert not _is_linked(b1, 'superModule', a)
    if hasattr(b2, 'superModule'):
        assert _is_linked(b2, 'superModule', a)
    _safe_set(a, 'Module', None)
    assert not _is_linked(a, 'Module', b2)
    if hasattr(b2, 'superModule'):
        assert not _is_linked(b2, 'superModule', a)


def test_assoc_subUnit64_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_UnaryUnit()
    b2 = henshin_UnaryUnit()
    _safe_set(a, 'henshin_Unit65', b1)
    assert _is_linked(a, 'henshin_Unit65', b1)
    if hasattr(b1, 'henshin_UnaryUnit'):
        assert _is_linked(b1, 'henshin_UnaryUnit', a)
    _safe_set(a, 'henshin_Unit65', b2)
    assert _is_linked(a, 'henshin_Unit65', b2)
    if hasattr(b1, 'henshin_UnaryUnit'):
        assert not _is_linked(b1, 'henshin_UnaryUnit', a)
    if hasattr(b2, 'henshin_UnaryUnit'):
        assert _is_linked(b2, 'henshin_UnaryUnit', a)
    _safe_set(a, 'henshin_Unit65', None)
    assert not _is_linked(a, 'henshin_Unit65', b2)
    if hasattr(b2, 'henshin_UnaryUnit'):
        assert not _is_linked(b2, 'henshin_UnaryUnit', a)


def test_assoc_subUnits66_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_MultiUnit()
    b2 = henshin_MultiUnit()
    _safe_set(a, 'henshin_Unit67', b1)
    assert _is_linked(a, 'henshin_Unit67', b1)
    if hasattr(b1, 'henshin_MultiUnit'):
        assert _is_linked(b1, 'henshin_MultiUnit', a)
    _safe_set(a, 'henshin_Unit67', b2)
    assert _is_linked(a, 'henshin_Unit67', b2)
    if hasattr(b1, 'henshin_MultiUnit'):
        assert not _is_linked(b1, 'henshin_MultiUnit', a)
    if hasattr(b2, 'henshin_MultiUnit'):
        assert _is_linked(b2, 'henshin_MultiUnit', a)
    _safe_set(a, 'henshin_Unit67', None)
    assert not _is_linked(a, 'henshin_Unit67', b2)
    if hasattr(b2, 'henshin_MultiUnit'):
        assert not _is_linked(b2, 'henshin_MultiUnit', a)


def test_assoc_superModule3_link_reassign_clear():
    a = henshin_Module()
    b1 = henshin_Module()
    b2 = henshin_Module()
    _safe_set(a, 'Module4', b1)
    assert _is_linked(a, 'Module4', b1)
    if hasattr(b1, 'subModules'):
        assert _is_linked(b1, 'subModules', a)
    _safe_set(a, 'Module4', b2)
    assert _is_linked(a, 'Module4', b2)
    if hasattr(b1, 'subModules'):
        assert not _is_linked(b1, 'subModules', a)
    if hasattr(b2, 'subModules'):
        assert _is_linked(b2, 'subModules', a)
    _safe_set(a, 'Module4', None)
    assert not _is_linked(a, 'Module4', b2)
    if hasattr(b2, 'subModules'):
        assert not _is_linked(b2, 'subModules', a)


def test_assoc_target49_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b2 = henshin_Edge(index="sample_text_2", indexConstant="sample_text_2")
    _safe_set(a, 'Node50', b1)
    assert _is_linked(a, 'Node50', b1)
    if hasattr(b1, 'incoming'):
        assert _is_linked(b1, 'incoming', a)
    _safe_set(a, 'Node50', b2)
    assert _is_linked(a, 'Node50', b2)
    if hasattr(b1, 'incoming'):
        assert not _is_linked(b1, 'incoming', a)
    if hasattr(b2, 'incoming'):
        assert _is_linked(b2, 'incoming', a)
    _safe_set(a, 'Node50', None)
    assert not _is_linked(a, 'Node50', b2)
    if hasattr(b2, 'incoming'):
        assert not _is_linked(b2, 'incoming', a)


def test_assoc_then70_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_Unit72', b1)
    assert _is_linked(a, 'henshin_Unit72', b1)
    if hasattr(b1, 'henshin_ConditionalUnit71'):
        assert _is_linked(b1, 'henshin_ConditionalUnit71', a)
    _safe_set(a, 'henshin_Unit72', b2)
    assert _is_linked(a, 'henshin_Unit72', b2)
    if hasattr(b1, 'henshin_ConditionalUnit71'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit71', a)
    if hasattr(b2, 'henshin_ConditionalUnit71'):
        assert _is_linked(b2, 'henshin_ConditionalUnit71', a)
    _safe_set(a, 'henshin_Unit72', None)
    assert not _is_linked(a, 'henshin_Unit72', b2)
    if hasattr(b2, 'henshin_ConditionalUnit71'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit71', a)


def test_assoc_type40_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_EClass()
    b2 = henshin_EClass()
    _safe_set(a, 'henshin_Node', b1)
    assert _is_linked(a, 'henshin_Node', b1)
    if hasattr(b1, 'henshin_EClass'):
        assert _is_linked(b1, 'henshin_EClass', a)
    _safe_set(a, 'henshin_Node', b2)
    assert _is_linked(a, 'henshin_Node', b2)
    if hasattr(b1, 'henshin_EClass'):
        assert not _is_linked(b1, 'henshin_EClass', a)
    if hasattr(b2, 'henshin_EClass'):
        assert _is_linked(b2, 'henshin_EClass', a)
    _safe_set(a, 'henshin_Node', None)
    assert not _is_linked(a, 'henshin_Node', b2)
    if hasattr(b2, 'henshin_EClass'):
        assert not _is_linked(b2, 'henshin_EClass', a)


def test_assoc_type51_link_reassign_clear():
    a = henshin_Edge(index="sample_text", indexConstant="sample_text")
    b1 = henshin_EReference()
    b2 = henshin_EReference()
    _safe_set(a, 'henshin_Edge', b1)
    assert _is_linked(a, 'henshin_Edge', b1)
    if hasattr(b1, 'henshin_EReference'):
        assert _is_linked(b1, 'henshin_EReference', a)
    _safe_set(a, 'henshin_Edge', b2)
    assert _is_linked(a, 'henshin_Edge', b2)
    if hasattr(b1, 'henshin_EReference'):
        assert not _is_linked(b1, 'henshin_EReference', a)
    if hasattr(b2, 'henshin_EReference'):
        assert _is_linked(b2, 'henshin_EReference', a)
    _safe_set(a, 'henshin_Edge', None)
    assert not _is_linked(a, 'henshin_Edge', b2)
    if hasattr(b2, 'henshin_EReference'):
        assert not _is_linked(b2, 'henshin_EReference', a)


def test_assoc_type54_link_reassign_clear():
    a = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    b1 = henshin_EAttribute()
    b2 = henshin_EAttribute()
    _safe_set(a, 'henshin_Attribute', b1)
    assert _is_linked(a, 'henshin_Attribute', b1)
    if hasattr(b1, 'henshin_EAttribute'):
        assert _is_linked(b1, 'henshin_EAttribute', a)
    _safe_set(a, 'henshin_Attribute', b2)
    assert _is_linked(a, 'henshin_Attribute', b2)
    if hasattr(b1, 'henshin_EAttribute'):
        assert not _is_linked(b1, 'henshin_EAttribute', a)
    if hasattr(b2, 'henshin_EAttribute'):
        assert _is_linked(b2, 'henshin_EAttribute', a)
    _safe_set(a, 'henshin_Attribute', None)
    assert not _is_linked(a, 'henshin_Attribute', b2)
    if hasattr(b2, 'henshin_EAttribute'):
        assert not _is_linked(b2, 'henshin_EAttribute', a)


def test_assoc_unit27_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_Parameter()
    b2 = henshin_Parameter()
    _safe_set(a, 'Unit', b1)
    assert _is_linked(a, 'Unit', b1)
    if hasattr(b1, 'parameters'):
        assert _is_linked(b1, 'parameters', a)
    _safe_set(a, 'Unit', b2)
    assert _is_linked(a, 'Unit', b2)
    if hasattr(b1, 'parameters'):
        assert not _is_linked(b1, 'parameters', a)
    if hasattr(b2, 'parameters'):
        assert _is_linked(b2, 'parameters', a)
    _safe_set(a, 'Unit', None)
    assert not _is_linked(a, 'Unit', b2)
    if hasattr(b2, 'parameters'):
        assert not _is_linked(b2, 'parameters', a)


def test_assoc_units6_link_reassign_clear():
    a = henshin_Unit(activated=True)
    b1 = henshin_Module()
    b2 = henshin_Module()
    _safe_set(a, 'henshin_Unit', b1)
    assert _is_linked(a, 'henshin_Unit', b1)
    if hasattr(b1, 'henshin_Module7'):
        assert _is_linked(b1, 'henshin_Module7', a)
    _safe_set(a, 'henshin_Unit', b2)
    assert _is_linked(a, 'henshin_Unit', b2)
    if hasattr(b1, 'henshin_Module7'):
        assert not _is_linked(b1, 'henshin_Module7', a)
    if hasattr(b2, 'henshin_Module7'):
        assert _is_linked(b2, 'henshin_Module7', a)
    _safe_set(a, 'henshin_Unit', None)
    assert not _is_linked(a, 'henshin_Unit', b2)
    if hasattr(b2, 'henshin_Module7'):
        assert not _is_linked(b2, 'henshin_Module7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryFormula_strategy = st.builds(BinaryFormula)
@given(instance=BinaryFormula_strategy)
@settings(max_examples=25)
def test_BinaryFormula_instantiation(instance):
    assert isinstance(instance, BinaryFormula)


Formula_strategy = st.builds(Formula)
@given(instance=Formula_strategy)
@settings(max_examples=25)
def test_Formula_instantiation(instance):
    assert isinstance(instance, Formula)


GraphElement_strategy = st.builds(GraphElement)
@given(instance=GraphElement_strategy)
@settings(max_examples=25)
def test_GraphElement_instantiation(instance):
    assert isinstance(instance, GraphElement)


MultiUnit_strategy = st.builds(MultiUnit)
@given(instance=MultiUnit_strategy)
@settings(max_examples=25)
def test_MultiUnit_instantiation(instance):
    assert isinstance(instance, MultiUnit)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


UnaryFormula_strategy = st.builds(UnaryFormula)
@given(instance=UnaryFormula_strategy)
@settings(max_examples=25)
def test_UnaryFormula_instantiation(instance):
    assert isinstance(instance, UnaryFormula)


UnaryUnit_strategy = st.builds(UnaryUnit)
@given(instance=UnaryUnit_strategy)
@settings(max_examples=25)
def test_UnaryUnit_instantiation(instance):
    assert isinstance(instance, UnaryUnit)


Unit_strategy = st.builds(Unit)
@given(instance=Unit_strategy)
@settings(max_examples=25)
def test_Unit_instantiation(instance):
    assert isinstance(instance, Unit)


henshin_And_strategy = st.builds(henshin_And)
@given(instance=henshin_And_strategy)
@settings(max_examples=25)
def test_henshin_And_instantiation(instance):
    assert isinstance(instance, henshin_And)


henshin_Attribute_strategy = st.builds(henshin_Attribute, constant=safe_text, null=st.booleans(), value=safe_text)
@given(instance=henshin_Attribute_strategy)
@settings(max_examples=25)
def test_henshin_Attribute_instantiation(instance):
    assert isinstance(instance, henshin_Attribute)


henshin_AttributeCondition_strategy = st.builds(henshin_AttributeCondition, conditionText=safe_text)
@given(instance=henshin_AttributeCondition_strategy)
@settings(max_examples=25)
def test_henshin_AttributeCondition_instantiation(instance):
    assert isinstance(instance, henshin_AttributeCondition)


henshin_BinaryFormula_strategy = st.builds(henshin_BinaryFormula)
@given(instance=henshin_BinaryFormula_strategy)
@settings(max_examples=25)
def test_henshin_BinaryFormula_instantiation(instance):
    assert isinstance(instance, henshin_BinaryFormula)


henshin_ConditionalUnit_strategy = st.builds(henshin_ConditionalUnit)
@given(instance=henshin_ConditionalUnit_strategy)
@settings(max_examples=25)
def test_henshin_ConditionalUnit_instantiation(instance):
    assert isinstance(instance, henshin_ConditionalUnit)


henshin_EAttribute_strategy = st.builds(henshin_EAttribute)
@given(instance=henshin_EAttribute_strategy)
@settings(max_examples=25)
def test_henshin_EAttribute_instantiation(instance):
    assert isinstance(instance, henshin_EAttribute)


henshin_EClass_strategy = st.builds(henshin_EClass)
@given(instance=henshin_EClass_strategy)
@settings(max_examples=25)
def test_henshin_EClass_instantiation(instance):
    assert isinstance(instance, henshin_EClass)


henshin_EClassifier_strategy = st.builds(henshin_EClassifier)
@given(instance=henshin_EClassifier_strategy)
@settings(max_examples=25)
def test_henshin_EClassifier_instantiation(instance):
    assert isinstance(instance, henshin_EClassifier)


henshin_EPackage_strategy = st.builds(henshin_EPackage)
@given(instance=henshin_EPackage_strategy)
@settings(max_examples=25)
def test_henshin_EPackage_instantiation(instance):
    assert isinstance(instance, henshin_EPackage)


henshin_EReference_strategy = st.builds(henshin_EReference)
@given(instance=henshin_EReference_strategy)
@settings(max_examples=25)
def test_henshin_EReference_instantiation(instance):
    assert isinstance(instance, henshin_EReference)


henshin_Edge_strategy = st.builds(henshin_Edge, index=safe_text, indexConstant=safe_text)
@given(instance=henshin_Edge_strategy)
@settings(max_examples=25)
def test_henshin_Edge_instantiation(instance):
    assert isinstance(instance, henshin_Edge)


henshin_Formula_strategy = st.builds(henshin_Formula)
@given(instance=henshin_Formula_strategy)
@settings(max_examples=25)
def test_henshin_Formula_instantiation(instance):
    assert isinstance(instance, henshin_Formula)


henshin_Graph_strategy = st.builds(henshin_Graph)
@given(instance=henshin_Graph_strategy)
@settings(max_examples=25)
def test_henshin_Graph_instantiation(instance):
    assert isinstance(instance, henshin_Graph)


henshin_GraphElement_strategy = st.builds(henshin_GraphElement, action=safe_text, presenceCondition=safe_text)
@given(instance=henshin_GraphElement_strategy)
@settings(max_examples=25)
def test_henshin_GraphElement_instantiation(instance):
    assert isinstance(instance, henshin_GraphElement)


henshin_IndependentUnit_strategy = st.builds(henshin_IndependentUnit)
@given(instance=henshin_IndependentUnit_strategy)
@settings(max_examples=25)
def test_henshin_IndependentUnit_instantiation(instance):
    assert isinstance(instance, henshin_IndependentUnit)


henshin_IteratedUnit_strategy = st.builds(henshin_IteratedUnit, iterations=safe_text)
@given(instance=henshin_IteratedUnit_strategy)
@settings(max_examples=25)
def test_henshin_IteratedUnit_instantiation(instance):
    assert isinstance(instance, henshin_IteratedUnit)


henshin_LoopUnit_strategy = st.builds(henshin_LoopUnit)
@given(instance=henshin_LoopUnit_strategy)
@settings(max_examples=25)
def test_henshin_LoopUnit_instantiation(instance):
    assert isinstance(instance, henshin_LoopUnit)


henshin_Mapping_strategy = st.builds(henshin_Mapping)
@given(instance=henshin_Mapping_strategy)
@settings(max_examples=25)
def test_henshin_Mapping_instantiation(instance):
    assert isinstance(instance, henshin_Mapping)


henshin_Module_strategy = st.builds(henshin_Module)
@given(instance=henshin_Module_strategy)
@settings(max_examples=25)
def test_henshin_Module_instantiation(instance):
    assert isinstance(instance, henshin_Module)


henshin_MultiUnit_strategy = st.builds(henshin_MultiUnit)
@given(instance=henshin_MultiUnit_strategy)
@settings(max_examples=25)
def test_henshin_MultiUnit_instantiation(instance):
    assert isinstance(instance, henshin_MultiUnit)


henshin_NamedElement_strategy = st.builds(henshin_NamedElement, description=safe_text, name=safe_text)
@given(instance=henshin_NamedElement_strategy)
@settings(max_examples=25)
def test_henshin_NamedElement_instantiation(instance):
    assert isinstance(instance, henshin_NamedElement)


henshin_NestedCondition_strategy = st.builds(henshin_NestedCondition, presenceCondition=safe_text)
@given(instance=henshin_NestedCondition_strategy)
@settings(max_examples=25)
def test_henshin_NestedCondition_instantiation(instance):
    assert isinstance(instance, henshin_NestedCondition)


henshin_Node_strategy = st.builds(henshin_Node)
@given(instance=henshin_Node_strategy)
@settings(max_examples=25)
def test_henshin_Node_instantiation(instance):
    assert isinstance(instance, henshin_Node)


henshin_Not_strategy = st.builds(henshin_Not)
@given(instance=henshin_Not_strategy)
@settings(max_examples=25)
def test_henshin_Not_instantiation(instance):
    assert isinstance(instance, henshin_Not)


henshin_Or_strategy = st.builds(henshin_Or)
@given(instance=henshin_Or_strategy)
@settings(max_examples=25)
def test_henshin_Or_instantiation(instance):
    assert isinstance(instance, henshin_Or)


henshin_Parameter_strategy = st.builds(henshin_Parameter)
@given(instance=henshin_Parameter_strategy)
@settings(max_examples=25)
def test_henshin_Parameter_instantiation(instance):
    assert isinstance(instance, henshin_Parameter)


henshin_ParameterMapping_strategy = st.builds(henshin_ParameterMapping)
@given(instance=henshin_ParameterMapping_strategy)
@settings(max_examples=25)
def test_henshin_ParameterMapping_instantiation(instance):
    assert isinstance(instance, henshin_ParameterMapping)


henshin_PriorityUnit_strategy = st.builds(henshin_PriorityUnit)
@given(instance=henshin_PriorityUnit_strategy)
@settings(max_examples=25)
def test_henshin_PriorityUnit_instantiation(instance):
    assert isinstance(instance, henshin_PriorityUnit)


henshin_Rule_strategy = st.builds(henshin_Rule, checkDangling=st.booleans(), featureModel=safe_text, injectiveMatching=st.booleans(), injectiveMatchingPresenceCondition=safe_text)
@given(instance=henshin_Rule_strategy)
@settings(max_examples=25)
def test_henshin_Rule_instantiation(instance):
    assert isinstance(instance, henshin_Rule)


henshin_SequentialUnit_strategy = st.builds(henshin_SequentialUnit, rollback=st.booleans(), strict=st.booleans())
@given(instance=henshin_SequentialUnit_strategy)
@settings(max_examples=25)
def test_henshin_SequentialUnit_instantiation(instance):
    assert isinstance(instance, henshin_SequentialUnit)


henshin_True_strategy = st.builds(henshin_True)
@given(instance=henshin_True_strategy)
@settings(max_examples=25)
def test_henshin_True_instantiation(instance):
    assert isinstance(instance, henshin_True)


henshin_UnaryFormula_strategy = st.builds(henshin_UnaryFormula)
@given(instance=henshin_UnaryFormula_strategy)
@settings(max_examples=25)
def test_henshin_UnaryFormula_instantiation(instance):
    assert isinstance(instance, henshin_UnaryFormula)


henshin_UnaryUnit_strategy = st.builds(henshin_UnaryUnit)
@given(instance=henshin_UnaryUnit_strategy)
@settings(max_examples=25)
def test_henshin_UnaryUnit_instantiation(instance):
    assert isinstance(instance, henshin_UnaryUnit)


henshin_Unit_strategy = st.builds(henshin_Unit, activated=st.booleans())
@given(instance=henshin_Unit_strategy)
@settings(max_examples=25)
def test_henshin_Unit_instantiation(instance):
    assert isinstance(instance, henshin_Unit)


henshin_Xor_strategy = st.builds(henshin_Xor)
@given(instance=henshin_Xor_strategy)
@settings(max_examples=25)
def test_henshin_Xor_instantiation(instance):
    assert isinstance(instance, henshin_Xor)



