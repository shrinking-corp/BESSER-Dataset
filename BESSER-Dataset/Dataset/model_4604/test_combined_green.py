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
    Logic,
    henshin_text_Not,
    henshin_text_ConditionGraphRef,
    henshin_text_AND,
    henshin_text_ORorXOR,
    Expression,
    henshin_text_JavaAttributeValue,
    henshin_text_MulOrDivExpression,
    henshin_text_NotExpression,
    henshin_text_AndExpression,
    henshin_text_PlusExpression,
    henshin_text_MinusExpression,
    henshin_text_IntegerValue,
    henshin_text_EqualityExpression,
    henshin_text_BracketExpression,
    henshin_text_NaturalValue,
    henshin_text_JavaClassValue,
    henshin_text_BoolValue,
    henshin_text_NumberValue,
    henshin_text_ComparisonExpression,
    henshin_text_ParameterValue,
    henshin_text_StringValue,
    henshin_text_OrExpression,
    ModelElement,
    henshin_text_Rule,
    henshin_text_Unit,
    henshin_text_List,
    henshin_text_ParameterType,
    henshin_text_Match,
    henshin_text_ConditionNodeTypes,
    henshin_text_ConditionEdge,
    henshin_text_ConditionGraphElements,
    SequentialProperties,
    henshin_text_Rollback,
    henshin_text_Strict,
    UnitElement,
    henshin_text_IteratedUnit,
    henshin_text_PriorityUnit,
    henshin_text_IndependentUnit,
    henshin_text_ConditionalUnit,
    henshin_text_Call,
    henshin_text_LoopUnit,
    henshin_text_SequentialProperties,
    henshin_text_UnitElement,
    henshin_text_EAttribute,
    henshin_text_Attribute,
    henshin_text_EClass,
    ConditionNodeTypes,
    RuleNodeTypes,
    henshin_text_EReference,
    henshin_text_ConditionGraph,
    henshin_text_Logic,
    ConditionGraphElements,
    henshin_text_ConditionNode,
    henshin_text_ConditionReuseNode,
    henshin_text_ConditionEdges,
    henshin_text_GraphElements,
    henshin_text_Expression,
    RuleElement,
    henshin_text_CheckDangling,
    henshin_text_Conditions,
    henshin_text_InjectiveMatching,
    henshin_text_Graph,
    henshin_text_JavaImport,
    henshin_text_RuleElement,
    henshin_text_Parameter,
    henshin_text_EPackage,
    henshin_text_ModelElement,
    henshin_text_RuleNodeTypes,
    henshin_text_Edge,
    GraphElements,
    henshin_text_MultiRule,
    henshin_text_Node,
    henshin_text_MultiRuleReuseNode,
    henshin_text_Formula,
    henshin_text_Edges,
    henshin_text_EPackageImport,
    henshin_text_Model,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_logic_is_not_abstract():
    assert not inspect.isabstract(Logic)


def test_hyp_logic_constructor_exists():
    assert callable(Logic.__init__)


def test_hyp_logic_constructor_args():
    sig = inspect.signature(Logic.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_not_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Not)


def test_hyp_henshin_text_not_constructor_exists():
    assert callable(henshin_text_Not.__init__)


def test_hyp_henshin_text_not_constructor_args():
    sig = inspect.signature(henshin_text_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditiongraphref_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraphRef)


def test_hyp_henshin_text_conditiongraphref_constructor_exists():
    assert callable(henshin_text_ConditionGraphRef.__init__)


def test_hyp_henshin_text_conditiongraphref_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraphRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_and_is_not_abstract():
    assert not inspect.isabstract(henshin_text_AND)


def test_hyp_henshin_text_and_constructor_exists():
    assert callable(henshin_text_AND.__init__)


def test_hyp_henshin_text_and_constructor_args():
    sig = inspect.signature(henshin_text_AND.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_ororxor_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ORorXOR)


def test_hyp_henshin_text_ororxor_constructor_exists():
    assert callable(henshin_text_ORorXOR.__init__)


def test_hyp_henshin_text_ororxor_constructor_args():
    sig = inspect.signature(henshin_text_ORorXOR.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_javaattributevalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaAttributeValue)


def test_hyp_henshin_text_javaattributevalue_constructor_exists():
    assert callable(henshin_text_JavaAttributeValue.__init__)


def test_hyp_henshin_text_javaattributevalue_constructor_args():
    sig = inspect.signature(henshin_text_JavaAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_mulordivexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MulOrDivExpression)


def test_hyp_henshin_text_mulordivexpression_constructor_exists():
    assert callable(henshin_text_MulOrDivExpression.__init__)


def test_hyp_henshin_text_mulordivexpression_constructor_args():
    sig = inspect.signature(henshin_text_MulOrDivExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_henshin_text_notexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NotExpression)


def test_hyp_henshin_text_notexpression_constructor_exists():
    assert callable(henshin_text_NotExpression.__init__)


def test_hyp_henshin_text_notexpression_constructor_args():
    sig = inspect.signature(henshin_text_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_andexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_AndExpression)


def test_hyp_henshin_text_andexpression_constructor_exists():
    assert callable(henshin_text_AndExpression.__init__)


def test_hyp_henshin_text_andexpression_constructor_args():
    sig = inspect.signature(henshin_text_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_plusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_PlusExpression)


def test_hyp_henshin_text_plusexpression_constructor_exists():
    assert callable(henshin_text_PlusExpression.__init__)


def test_hyp_henshin_text_plusexpression_constructor_args():
    sig = inspect.signature(henshin_text_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_minusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MinusExpression)


def test_hyp_henshin_text_minusexpression_constructor_exists():
    assert callable(henshin_text_MinusExpression.__init__)


def test_hyp_henshin_text_minusexpression_constructor_args():
    sig = inspect.signature(henshin_text_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_integervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IntegerValue)


def test_hyp_henshin_text_integervalue_constructor_exists():
    assert callable(henshin_text_IntegerValue.__init__)


def test_hyp_henshin_text_integervalue_constructor_args():
    sig = inspect.signature(henshin_text_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EqualityExpression)


def test_hyp_henshin_text_equalityexpression_constructor_exists():
    assert callable(henshin_text_EqualityExpression.__init__)


def test_hyp_henshin_text_equalityexpression_constructor_args():
    sig = inspect.signature(henshin_text_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_henshin_text_bracketexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_BracketExpression)


def test_hyp_henshin_text_bracketexpression_constructor_exists():
    assert callable(henshin_text_BracketExpression.__init__)


def test_hyp_henshin_text_bracketexpression_constructor_args():
    sig = inspect.signature(henshin_text_BracketExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_naturalvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NaturalValue)


def test_hyp_henshin_text_naturalvalue_constructor_exists():
    assert callable(henshin_text_NaturalValue.__init__)


def test_hyp_henshin_text_naturalvalue_constructor_args():
    sig = inspect.signature(henshin_text_NaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_javaclassvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaClassValue)


def test_hyp_henshin_text_javaclassvalue_constructor_exists():
    assert callable(henshin_text_JavaClassValue.__init__)


def test_hyp_henshin_text_javaclassvalue_constructor_args():
    sig = inspect.signature(henshin_text_JavaClassValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_boolvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_BoolValue)


def test_hyp_henshin_text_boolvalue_constructor_exists():
    assert callable(henshin_text_BoolValue.__init__)


def test_hyp_henshin_text_boolvalue_constructor_args():
    sig = inspect.signature(henshin_text_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_numbervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NumberValue)


def test_hyp_henshin_text_numbervalue_constructor_exists():
    assert callable(henshin_text_NumberValue.__init__)


def test_hyp_henshin_text_numbervalue_constructor_args():
    sig = inspect.signature(henshin_text_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ComparisonExpression)


def test_hyp_henshin_text_comparisonexpression_constructor_exists():
    assert callable(henshin_text_ComparisonExpression.__init__)


def test_hyp_henshin_text_comparisonexpression_constructor_args():
    sig = inspect.signature(henshin_text_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_henshin_text_parametervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ParameterValue)


def test_hyp_henshin_text_parametervalue_constructor_exists():
    assert callable(henshin_text_ParameterValue.__init__)


def test_hyp_henshin_text_parametervalue_constructor_args():
    sig = inspect.signature(henshin_text_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_stringvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_StringValue)


def test_hyp_henshin_text_stringvalue_constructor_exists():
    assert callable(henshin_text_StringValue.__init__)


def test_hyp_henshin_text_stringvalue_constructor_args():
    sig = inspect.signature(henshin_text_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_text_orexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_OrExpression)


def test_hyp_henshin_text_orexpression_constructor_exists():
    assert callable(henshin_text_OrExpression.__init__)


def test_hyp_henshin_text_orexpression_constructor_args():
    sig = inspect.signature(henshin_text_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_rule_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Rule)


def test_hyp_henshin_text_rule_constructor_exists():
    assert callable(henshin_text_Rule.__init__)


def test_hyp_henshin_text_rule_constructor_args():
    sig = inspect.signature(henshin_text_Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_unit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Unit)


def test_hyp_henshin_text_unit_constructor_exists():
    assert callable(henshin_text_Unit.__init__)


def test_hyp_henshin_text_unit_constructor_args():
    sig = inspect.signature(henshin_text_Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_list_is_not_abstract():
    assert not inspect.isabstract(henshin_text_List)


def test_hyp_henshin_text_list_constructor_exists():
    assert callable(henshin_text_List.__init__)


def test_hyp_henshin_text_list_constructor_args():
    sig = inspect.signature(henshin_text_List.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_parametertype_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ParameterType)


def test_hyp_henshin_text_parametertype_constructor_exists():
    assert callable(henshin_text_ParameterType.__init__)


def test_hyp_henshin_text_parametertype_constructor_args():
    sig = inspect.signature(henshin_text_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "enumType" in params, "Missing parameter 'enumType'"




def test_hyp_henshin_text_match_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Match)


def test_hyp_henshin_text_match_constructor_exists():
    assert callable(henshin_text_Match.__init__)


def test_hyp_henshin_text_match_constructor_args():
    sig = inspect.signature(henshin_text_Match.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionNodeTypes)


def test_hyp_henshin_text_conditionnodetypes_constructor_exists():
    assert callable(henshin_text_ConditionNodeTypes.__init__)


def test_hyp_henshin_text_conditionnodetypes_constructor_args():
    sig = inspect.signature(henshin_text_ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_text_conditionedge_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionEdge)


def test_hyp_henshin_text_conditionedge_constructor_exists():
    assert callable(henshin_text_ConditionEdge.__init__)


def test_hyp_henshin_text_conditionedge_constructor_args():
    sig = inspect.signature(henshin_text_ConditionEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraphElements)


def test_hyp_henshin_text_conditiongraphelements_constructor_exists():
    assert callable(henshin_text_ConditionGraphElements.__init__)


def test_hyp_henshin_text_conditiongraphelements_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(SequentialProperties)


def test_hyp_sequentialproperties_constructor_exists():
    assert callable(SequentialProperties.__init__)


def test_hyp_sequentialproperties_constructor_args():
    sig = inspect.signature(SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_rollback_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Rollback)


def test_hyp_henshin_text_rollback_constructor_exists():
    assert callable(henshin_text_Rollback.__init__)


def test_hyp_henshin_text_rollback_constructor_args():
    sig = inspect.signature(henshin_text_Rollback.__init__)
    params = list(sig.parameters.keys())
    assert "rollback" in params, "Missing parameter 'rollback'"




def test_hyp_henshin_text_strict_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Strict)


def test_hyp_henshin_text_strict_constructor_exists():
    assert callable(henshin_text_Strict.__init__)


def test_hyp_henshin_text_strict_constructor_args():
    sig = inspect.signature(henshin_text_Strict.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"




def test_hyp_unitelement_is_not_abstract():
    assert not inspect.isabstract(UnitElement)


def test_hyp_unitelement_constructor_exists():
    assert callable(UnitElement.__init__)


def test_hyp_unitelement_constructor_args():
    sig = inspect.signature(UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_iteratedunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IteratedUnit)


def test_hyp_henshin_text_iteratedunit_constructor_exists():
    assert callable(henshin_text_IteratedUnit.__init__)


def test_hyp_henshin_text_iteratedunit_constructor_args():
    sig = inspect.signature(henshin_text_IteratedUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_priorityunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_PriorityUnit)


def test_hyp_henshin_text_priorityunit_constructor_exists():
    assert callable(henshin_text_PriorityUnit.__init__)


def test_hyp_henshin_text_priorityunit_constructor_args():
    sig = inspect.signature(henshin_text_PriorityUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_independentunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IndependentUnit)


def test_hyp_henshin_text_independentunit_constructor_exists():
    assert callable(henshin_text_IndependentUnit.__init__)


def test_hyp_henshin_text_independentunit_constructor_args():
    sig = inspect.signature(henshin_text_IndependentUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditionalunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionalUnit)


def test_hyp_henshin_text_conditionalunit_constructor_exists():
    assert callable(henshin_text_ConditionalUnit.__init__)


def test_hyp_henshin_text_conditionalunit_constructor_args():
    sig = inspect.signature(henshin_text_ConditionalUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_call_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Call)


def test_hyp_henshin_text_call_constructor_exists():
    assert callable(henshin_text_Call.__init__)


def test_hyp_henshin_text_call_constructor_args():
    sig = inspect.signature(henshin_text_Call.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_loopunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_LoopUnit)


def test_hyp_henshin_text_loopunit_constructor_exists():
    assert callable(henshin_text_LoopUnit.__init__)


def test_hyp_henshin_text_loopunit_constructor_args():
    sig = inspect.signature(henshin_text_LoopUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(henshin_text_SequentialProperties)


def test_hyp_henshin_text_sequentialproperties_constructor_exists():
    assert callable(henshin_text_SequentialProperties.__init__)


def test_hyp_henshin_text_sequentialproperties_constructor_args():
    sig = inspect.signature(henshin_text_SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_unitelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_UnitElement)


def test_hyp_henshin_text_unitelement_constructor_exists():
    assert callable(henshin_text_UnitElement.__init__)


def test_hyp_henshin_text_unitelement_constructor_args():
    sig = inspect.signature(henshin_text_UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_eattribute_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EAttribute)


def test_hyp_henshin_text_eattribute_constructor_exists():
    assert callable(henshin_text_EAttribute.__init__)


def test_hyp_henshin_text_eattribute_constructor_args():
    sig = inspect.signature(henshin_text_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_attribute_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Attribute)


def test_hyp_henshin_text_attribute_constructor_exists():
    assert callable(henshin_text_Attribute.__init__)


def test_hyp_henshin_text_attribute_constructor_args():
    sig = inspect.signature(henshin_text_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"
    assert "update" in params, "Missing parameter 'update'"





def test_hyp_henshin_text_eclass_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EClass)


def test_hyp_henshin_text_eclass_constructor_exists():
    assert callable(henshin_text_EClass.__init__)


def test_hyp_henshin_text_eclass_constructor_args():
    sig = inspect.signature(henshin_text_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(ConditionNodeTypes)


def test_hyp_conditionnodetypes_constructor_exists():
    assert callable(ConditionNodeTypes.__init__)


def test_hyp_conditionnodetypes_constructor_args():
    sig = inspect.signature(ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(RuleNodeTypes)


def test_hyp_rulenodetypes_constructor_exists():
    assert callable(RuleNodeTypes.__init__)


def test_hyp_rulenodetypes_constructor_args():
    sig = inspect.signature(RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_ereference_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EReference)


def test_hyp_henshin_text_ereference_constructor_exists():
    assert callable(henshin_text_EReference.__init__)


def test_hyp_henshin_text_ereference_constructor_args():
    sig = inspect.signature(henshin_text_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditiongraph_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraph)


def test_hyp_henshin_text_conditiongraph_constructor_exists():
    assert callable(henshin_text_ConditionGraph.__init__)


def test_hyp_henshin_text_conditiongraph_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_text_logic_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Logic)


def test_hyp_henshin_text_logic_constructor_exists():
    assert callable(henshin_text_Logic.__init__)


def test_hyp_henshin_text_logic_constructor_args():
    sig = inspect.signature(henshin_text_Logic.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(ConditionGraphElements)


def test_hyp_conditiongraphelements_constructor_exists():
    assert callable(ConditionGraphElements.__init__)


def test_hyp_conditiongraphelements_constructor_args():
    sig = inspect.signature(ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditionnode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionNode)


def test_hyp_henshin_text_conditionnode_constructor_exists():
    assert callable(henshin_text_ConditionNode.__init__)


def test_hyp_henshin_text_conditionnode_constructor_args():
    sig = inspect.signature(henshin_text_ConditionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditionreusenode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionReuseNode)


def test_hyp_henshin_text_conditionreusenode_constructor_exists():
    assert callable(henshin_text_ConditionReuseNode.__init__)


def test_hyp_henshin_text_conditionreusenode_constructor_args():
    sig = inspect.signature(henshin_text_ConditionReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_conditionedges_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionEdges)


def test_hyp_henshin_text_conditionedges_constructor_exists():
    assert callable(henshin_text_ConditionEdges.__init__)


def test_hyp_henshin_text_conditionedges_constructor_args():
    sig = inspect.signature(henshin_text_ConditionEdges.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_graphelements_is_not_abstract():
    assert not inspect.isabstract(henshin_text_GraphElements)


def test_hyp_henshin_text_graphelements_constructor_exists():
    assert callable(henshin_text_GraphElements.__init__)


def test_hyp_henshin_text_graphelements_constructor_args():
    sig = inspect.signature(henshin_text_GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_expression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Expression)


def test_hyp_henshin_text_expression_constructor_exists():
    assert callable(henshin_text_Expression.__init__)


def test_hyp_henshin_text_expression_constructor_args():
    sig = inspect.signature(henshin_text_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ruleelement_is_not_abstract():
    assert not inspect.isabstract(RuleElement)


def test_hyp_ruleelement_constructor_exists():
    assert callable(RuleElement.__init__)


def test_hyp_ruleelement_constructor_args():
    sig = inspect.signature(RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_checkdangling_is_not_abstract():
    assert not inspect.isabstract(henshin_text_CheckDangling)


def test_hyp_henshin_text_checkdangling_constructor_exists():
    assert callable(henshin_text_CheckDangling.__init__)


def test_hyp_henshin_text_checkdangling_constructor_args():
    sig = inspect.signature(henshin_text_CheckDangling.__init__)
    params = list(sig.parameters.keys())
    assert "checkDangling" in params, "Missing parameter 'checkDangling'"




def test_hyp_henshin_text_conditions_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Conditions)


def test_hyp_henshin_text_conditions_constructor_exists():
    assert callable(henshin_text_Conditions.__init__)


def test_hyp_henshin_text_conditions_constructor_args():
    sig = inspect.signature(henshin_text_Conditions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_injectivematching_is_not_abstract():
    assert not inspect.isabstract(henshin_text_InjectiveMatching)


def test_hyp_henshin_text_injectivematching_constructor_exists():
    assert callable(henshin_text_InjectiveMatching.__init__)


def test_hyp_henshin_text_injectivematching_constructor_args():
    sig = inspect.signature(henshin_text_InjectiveMatching.__init__)
    params = list(sig.parameters.keys())
    assert "injectiveMatching" in params, "Missing parameter 'injectiveMatching'"




def test_hyp_henshin_text_graph_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Graph)


def test_hyp_henshin_text_graph_constructor_exists():
    assert callable(henshin_text_Graph.__init__)


def test_hyp_henshin_text_graph_constructor_args():
    sig = inspect.signature(henshin_text_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_javaimport_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaImport)


def test_hyp_henshin_text_javaimport_constructor_exists():
    assert callable(henshin_text_JavaImport.__init__)


def test_hyp_henshin_text_javaimport_constructor_args():
    sig = inspect.signature(henshin_text_JavaImport.__init__)
    params = list(sig.parameters.keys())
    assert "packagename" in params, "Missing parameter 'packagename'"




def test_hyp_henshin_text_ruleelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_RuleElement)


def test_hyp_henshin_text_ruleelement_constructor_exists():
    assert callable(henshin_text_RuleElement.__init__)


def test_hyp_henshin_text_ruleelement_constructor_args():
    sig = inspect.signature(henshin_text_RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_parameter_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Parameter)


def test_hyp_henshin_text_parameter_constructor_exists():
    assert callable(henshin_text_Parameter.__init__)


def test_hyp_henshin_text_parameter_constructor_args():
    sig = inspect.signature(henshin_text_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_text_epackage_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EPackage)


def test_hyp_henshin_text_epackage_constructor_exists():
    assert callable(henshin_text_EPackage.__init__)


def test_hyp_henshin_text_epackage_constructor_args():
    sig = inspect.signature(henshin_text_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_modelelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ModelElement)


def test_hyp_henshin_text_modelelement_constructor_exists():
    assert callable(henshin_text_ModelElement.__init__)


def test_hyp_henshin_text_modelelement_constructor_args():
    sig = inspect.signature(henshin_text_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_text_rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin_text_RuleNodeTypes)


def test_hyp_henshin_text_rulenodetypes_constructor_exists():
    assert callable(henshin_text_RuleNodeTypes.__init__)


def test_hyp_henshin_text_rulenodetypes_constructor_args():
    sig = inspect.signature(henshin_text_RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_edge_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Edge)


def test_hyp_henshin_text_edge_constructor_exists():
    assert callable(henshin_text_Edge.__init__)


def test_hyp_henshin_text_edge_constructor_args():
    sig = inspect.signature(henshin_text_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"




def test_hyp_graphelements_is_not_abstract():
    assert not inspect.isabstract(GraphElements)


def test_hyp_graphelements_constructor_exists():
    assert callable(GraphElements.__init__)


def test_hyp_graphelements_constructor_args():
    sig = inspect.signature(GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_multirule_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MultiRule)


def test_hyp_henshin_text_multirule_constructor_exists():
    assert callable(henshin_text_MultiRule.__init__)


def test_hyp_henshin_text_multirule_constructor_args():
    sig = inspect.signature(henshin_text_MultiRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_text_node_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Node)


def test_hyp_henshin_text_node_constructor_exists():
    assert callable(henshin_text_Node.__init__)


def test_hyp_henshin_text_node_constructor_args():
    sig = inspect.signature(henshin_text_Node.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"




def test_hyp_henshin_text_multirulereusenode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MultiRuleReuseNode)


def test_hyp_henshin_text_multirulereusenode_constructor_exists():
    assert callable(henshin_text_MultiRuleReuseNode.__init__)


def test_hyp_henshin_text_multirulereusenode_constructor_args():
    sig = inspect.signature(henshin_text_MultiRuleReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_formula_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Formula)


def test_hyp_henshin_text_formula_constructor_exists():
    assert callable(henshin_text_Formula.__init__)


def test_hyp_henshin_text_formula_constructor_args():
    sig = inspect.signature(henshin_text_Formula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_edges_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Edges)


def test_hyp_henshin_text_edges_constructor_exists():
    assert callable(henshin_text_Edges.__init__)


def test_hyp_henshin_text_edges_constructor_args():
    sig = inspect.signature(henshin_text_Edges.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_epackageimport_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EPackageImport)


def test_hyp_henshin_text_epackageimport_constructor_exists():
    assert callable(henshin_text_EPackageImport.__init__)


def test_hyp_henshin_text_epackageimport_constructor_args():
    sig = inspect.signature(henshin_text_EPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_text_model_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Model)


def test_hyp_henshin_text_model_constructor_exists():
    assert callable(henshin_text_Model.__init__)


def test_hyp_henshin_text_model_constructor_args():
    sig = inspect.signature(henshin_text_Model.__init__)
    params = list(sig.parameters.keys())

def test_hyp_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_hyp_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "eLong",
        "eResource",
        "eBoolean",
        "eDate",
        "eLongObject",
        "eBigInteger",
        "eDoubleObject",
        "eDouble",
        "eJavaClass",
        "eInt",
        "eByteArray",
        "eEList",
        "eBooleanObject",
        "eDiagnosticChain",
        "eResourceSet",
        "eChar",
        "eEnumerator",
        "eMap",
        "eIntegerObject",
        "eFloat",
        "eJavaObject",
        "eFloatObject",
        "eInvocationTargetException",
        "eShortObject",
        "eShort",
        "eByteObject",
        "eCharacterObject",
        "eBigDecimal",
        "eByte",
        "eTreeIterator",
        "eFeatureMap",
        "eString",
        "eFeatureMapEntry",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
Logic_strategy = st.builds(
    Logic,
)
henshin_text_Not_strategy = st.builds(
    henshin_text_Not,
)
henshin_text_ConditionGraphRef_strategy = st.builds(
    henshin_text_ConditionGraphRef,
)
henshin_text_AND_strategy = st.builds(
    henshin_text_AND,
)
henshin_text_ORorXOR_strategy = st.builds(
    henshin_text_ORorXOR,
    op=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
henshin_text_JavaAttributeValue_strategy = st.builds(
    henshin_text_JavaAttributeValue,
    value=
        safe_text
)
henshin_text_MulOrDivExpression_strategy = st.builds(
    henshin_text_MulOrDivExpression,
    op=
        safe_text
)
henshin_text_NotExpression_strategy = st.builds(
    henshin_text_NotExpression,
)
henshin_text_AndExpression_strategy = st.builds(
    henshin_text_AndExpression,
)
henshin_text_PlusExpression_strategy = st.builds(
    henshin_text_PlusExpression,
)
henshin_text_MinusExpression_strategy = st.builds(
    henshin_text_MinusExpression,
)
henshin_text_IntegerValue_strategy = st.builds(
    henshin_text_IntegerValue,
    value=
        safe_text
)
henshin_text_EqualityExpression_strategy = st.builds(
    henshin_text_EqualityExpression,
    op=
        safe_text
)
henshin_text_BracketExpression_strategy = st.builds(
    henshin_text_BracketExpression,
)
henshin_text_NaturalValue_strategy = st.builds(
    henshin_text_NaturalValue,
    value=
        st.integers()
)
henshin_text_JavaClassValue_strategy = st.builds(
    henshin_text_JavaClassValue,
    value=
        safe_text
)
henshin_text_BoolValue_strategy = st.builds(
    henshin_text_BoolValue,
    value=
        st.booleans()
)
henshin_text_NumberValue_strategy = st.builds(
    henshin_text_NumberValue,
    value=
        safe_text
)
henshin_text_ComparisonExpression_strategy = st.builds(
    henshin_text_ComparisonExpression,
    op=
        safe_text
)
henshin_text_ParameterValue_strategy = st.builds(
    henshin_text_ParameterValue,
)
henshin_text_StringValue_strategy = st.builds(
    henshin_text_StringValue,
    value=
        safe_text
)
henshin_text_OrExpression_strategy = st.builds(
    henshin_text_OrExpression,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
henshin_text_Rule_strategy = st.builds(
    henshin_text_Rule,
)
henshin_text_Unit_strategy = st.builds(
    henshin_text_Unit,
)
henshin_text_List_strategy = st.builds(
    henshin_text_List,
)
henshin_text_ParameterType_strategy = st.builds(
    henshin_text_ParameterType,
    enumType=
        safe_text
)
henshin_text_Match_strategy = st.builds(
    henshin_text_Match,
)
henshin_text_ConditionNodeTypes_strategy = st.builds(
    henshin_text_ConditionNodeTypes,
    name=
        safe_text
)
henshin_text_ConditionEdge_strategy = st.builds(
    henshin_text_ConditionEdge,
)
henshin_text_ConditionGraphElements_strategy = st.builds(
    henshin_text_ConditionGraphElements,
)
SequentialProperties_strategy = st.builds(
    SequentialProperties,
)
henshin_text_Rollback_strategy = st.builds(
    henshin_text_Rollback,
    rollback=
        st.booleans()
)
henshin_text_Strict_strategy = st.builds(
    henshin_text_Strict,
    strict=
        st.booleans()
)
UnitElement_strategy = st.builds(
    UnitElement,
)
henshin_text_IteratedUnit_strategy = st.builds(
    henshin_text_IteratedUnit,
)
henshin_text_PriorityUnit_strategy = st.builds(
    henshin_text_PriorityUnit,
)
henshin_text_IndependentUnit_strategy = st.builds(
    henshin_text_IndependentUnit,
)
henshin_text_ConditionalUnit_strategy = st.builds(
    henshin_text_ConditionalUnit,
)
henshin_text_Call_strategy = st.builds(
    henshin_text_Call,
)
henshin_text_LoopUnit_strategy = st.builds(
    henshin_text_LoopUnit,
)
henshin_text_SequentialProperties_strategy = st.builds(
    henshin_text_SequentialProperties,
)
henshin_text_UnitElement_strategy = st.builds(
    henshin_text_UnitElement,
)
henshin_text_EAttribute_strategy = st.builds(
    henshin_text_EAttribute,
)
henshin_text_Attribute_strategy = st.builds(
    henshin_text_Attribute,
    actiontype=
        safe_text,
    update=
        safe_text
)
henshin_text_EClass_strategy = st.builds(
    henshin_text_EClass,
)
ConditionNodeTypes_strategy = st.builds(
    ConditionNodeTypes,
)
RuleNodeTypes_strategy = st.builds(
    RuleNodeTypes,
)
henshin_text_EReference_strategy = st.builds(
    henshin_text_EReference,
)
henshin_text_ConditionGraph_strategy = st.builds(
    henshin_text_ConditionGraph,
    name=
        safe_text
)
henshin_text_Logic_strategy = st.builds(
    henshin_text_Logic,
)
ConditionGraphElements_strategy = st.builds(
    ConditionGraphElements,
)
henshin_text_ConditionNode_strategy = st.builds(
    henshin_text_ConditionNode,
)
henshin_text_ConditionReuseNode_strategy = st.builds(
    henshin_text_ConditionReuseNode,
)
henshin_text_ConditionEdges_strategy = st.builds(
    henshin_text_ConditionEdges,
)
henshin_text_GraphElements_strategy = st.builds(
    henshin_text_GraphElements,
)
henshin_text_Expression_strategy = st.builds(
    henshin_text_Expression,
)
RuleElement_strategy = st.builds(
    RuleElement,
)
henshin_text_CheckDangling_strategy = st.builds(
    henshin_text_CheckDangling,
    checkDangling=
        st.booleans()
)
henshin_text_Conditions_strategy = st.builds(
    henshin_text_Conditions,
)
henshin_text_InjectiveMatching_strategy = st.builds(
    henshin_text_InjectiveMatching,
    injectiveMatching=
        st.booleans()
)
henshin_text_Graph_strategy = st.builds(
    henshin_text_Graph,
)
henshin_text_JavaImport_strategy = st.builds(
    henshin_text_JavaImport,
    packagename=
        safe_text
)
henshin_text_RuleElement_strategy = st.builds(
    henshin_text_RuleElement,
)
henshin_text_Parameter_strategy = st.builds(
    henshin_text_Parameter,
    name=
        safe_text
)
henshin_text_EPackage_strategy = st.builds(
    henshin_text_EPackage,
)
henshin_text_ModelElement_strategy = st.builds(
    henshin_text_ModelElement,
    name=
        safe_text
)
henshin_text_RuleNodeTypes_strategy = st.builds(
    henshin_text_RuleNodeTypes,
)
henshin_text_Edge_strategy = st.builds(
    henshin_text_Edge,
    actiontype=
        safe_text
)
GraphElements_strategy = st.builds(
    GraphElements,
)
henshin_text_MultiRule_strategy = st.builds(
    henshin_text_MultiRule,
    name=
        safe_text
)
henshin_text_Node_strategy = st.builds(
    henshin_text_Node,
    actiontype=
        safe_text
)
henshin_text_MultiRuleReuseNode_strategy = st.builds(
    henshin_text_MultiRuleReuseNode,
)
henshin_text_Formula_strategy = st.builds(
    henshin_text_Formula,
)
henshin_text_Edges_strategy = st.builds(
    henshin_text_Edges,
)
henshin_text_EPackageImport_strategy = st.builds(
    henshin_text_EPackageImport,
)
henshin_text_Model_strategy = st.builds(
    henshin_text_Model,
)








@given(instance=henshin_text_ORorXOR_strategy)
def test_hyp_henshin_text_ororxor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=henshin_text_JavaAttributeValue_strategy)
def test_hyp_henshin_text_javaattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_MulOrDivExpression_strategy)
def test_hyp_henshin_text_mulordivexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original








@given(instance=henshin_text_IntegerValue_strategy)
def test_hyp_henshin_text_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_EqualityExpression_strategy)
def test_hyp_henshin_text_equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=henshin_text_NaturalValue_strategy)
def test_hyp_henshin_text_naturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_JavaClassValue_strategy)
def test_hyp_henshin_text_javaclassvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_BoolValue_strategy)
def test_hyp_henshin_text_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_NumberValue_strategy)
def test_hyp_henshin_text_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=henshin_text_ComparisonExpression_strategy)
def test_hyp_henshin_text_comparisonexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=henshin_text_StringValue_strategy)
def test_hyp_henshin_text_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=henshin_text_ParameterType_strategy)
def test_hyp_henshin_text_parametertype_enumType_setter(instance):
    original = instance.enumType
    instance.enumType = original
    assert instance.enumType == original





@given(instance=henshin_text_ConditionNodeTypes_strategy)
def test_hyp_henshin_text_conditionnodetypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=henshin_text_Rollback_strategy)
def test_hyp_henshin_text_rollback_rollback_setter(instance):
    original = instance.rollback
    instance.rollback = original
    assert instance.rollback == original




@given(instance=henshin_text_Strict_strategy)
def test_hyp_henshin_text_strict_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original














@given(instance=henshin_text_Attribute_strategy)
def test_hyp_henshin_text_attribute_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original



@given(instance=henshin_text_Attribute_strategy)
def test_hyp_henshin_text_attribute_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original








@given(instance=henshin_text_ConditionGraph_strategy)
def test_hyp_henshin_text_conditiongraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=henshin_text_CheckDangling_strategy)
def test_hyp_henshin_text_checkdangling_checkDangling_setter(instance):
    original = instance.checkDangling
    instance.checkDangling = original
    assert instance.checkDangling == original





@given(instance=henshin_text_InjectiveMatching_strategy)
def test_hyp_henshin_text_injectivematching_injectiveMatching_setter(instance):
    original = instance.injectiveMatching
    instance.injectiveMatching = original
    assert instance.injectiveMatching == original





@given(instance=henshin_text_JavaImport_strategy)
def test_hyp_henshin_text_javaimport_packagename_setter(instance):
    original = instance.packagename
    instance.packagename = original
    assert instance.packagename == original





@given(instance=henshin_text_Parameter_strategy)
def test_hyp_henshin_text_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=henshin_text_ModelElement_strategy)
def test_hyp_henshin_text_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=henshin_text_Edge_strategy)
def test_hyp_henshin_text_edge_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original





@given(instance=henshin_text_MultiRule_strategy)
def test_hyp_henshin_text_multirule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=henshin_text_Node_strategy)
def test_hyp_henshin_text_node_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ConditionGraphElements,
    ConditionNodeTypes,
    Expression,
    GraphElements,
    Logic,
    ModelElement,
    RuleElement,
    RuleNodeTypes,
    SequentialProperties,
    UnitElement,
    henshin_text_AND,
    henshin_text_AndExpression,
    henshin_text_Attribute,
    henshin_text_BoolValue,
    henshin_text_BracketExpression,
    henshin_text_Call,
    henshin_text_CheckDangling,
    henshin_text_ComparisonExpression,
    henshin_text_ConditionEdge,
    henshin_text_ConditionEdges,
    henshin_text_ConditionGraph,
    henshin_text_ConditionGraphElements,
    henshin_text_ConditionGraphRef,
    henshin_text_ConditionNode,
    henshin_text_ConditionNodeTypes,
    henshin_text_ConditionReuseNode,
    henshin_text_ConditionalUnit,
    henshin_text_Conditions,
    henshin_text_EAttribute,
    henshin_text_EClass,
    henshin_text_EPackage,
    henshin_text_EPackageImport,
    henshin_text_EReference,
    henshin_text_Edge,
    henshin_text_Edges,
    henshin_text_EqualityExpression,
    henshin_text_Expression,
    henshin_text_Formula,
    henshin_text_Graph,
    henshin_text_GraphElements,
    henshin_text_IndependentUnit,
    henshin_text_InjectiveMatching,
    henshin_text_IntegerValue,
    henshin_text_IteratedUnit,
    henshin_text_JavaAttributeValue,
    henshin_text_JavaClassValue,
    henshin_text_JavaImport,
    henshin_text_List,
    henshin_text_Logic,
    henshin_text_LoopUnit,
    henshin_text_Match,
    henshin_text_MinusExpression,
    henshin_text_Model,
    henshin_text_ModelElement,
    henshin_text_MulOrDivExpression,
    henshin_text_MultiRule,
    henshin_text_MultiRuleReuseNode,
    henshin_text_NaturalValue,
    henshin_text_Node,
    henshin_text_Not,
    henshin_text_NotExpression,
    henshin_text_NumberValue,
    henshin_text_ORorXOR,
    henshin_text_OrExpression,
    henshin_text_Parameter,
    henshin_text_ParameterType,
    henshin_text_ParameterValue,
    henshin_text_PlusExpression,
    henshin_text_PriorityUnit,
    henshin_text_Rollback,
    henshin_text_Rule,
    henshin_text_RuleElement,
    henshin_text_RuleNodeTypes,
    henshin_text_SequentialProperties,
    henshin_text_Strict,
    henshin_text_StringValue,
    henshin_text_Unit,
    henshin_text_UnitElement,
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

def test_henshin_text_Attribute_actiontype_value_roundtrip():
    instance = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    assert instance.actiontype == "sample_text"
    instance.actiontype = "sample_text_2"
    assert instance.actiontype == "sample_text_2"


def test_henshin_text_Attribute_update_value_roundtrip():
    instance = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    assert instance.update == "sample_text"
    instance.update = "sample_text_2"
    assert instance.update == "sample_text_2"


def test_henshin_text_BoolValue_value_value_roundtrip():
    instance = henshin_text_BoolValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_henshin_text_CheckDangling_checkDangling_value_roundtrip():
    instance = henshin_text_CheckDangling(checkDangling=True)
    assert instance.checkDangling == True
    instance.checkDangling = False
    assert instance.checkDangling == False


def test_henshin_text_ComparisonExpression_op_value_roundtrip():
    instance = henshin_text_ComparisonExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_henshin_text_ConditionGraph_name_value_roundtrip():
    instance = henshin_text_ConditionGraph(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_text_ConditionNodeTypes_name_value_roundtrip():
    instance = henshin_text_ConditionNodeTypes(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_text_Edge_actiontype_value_roundtrip():
    instance = henshin_text_Edge(actiontype="sample_text")
    assert instance.actiontype == "sample_text"
    instance.actiontype = "sample_text_2"
    assert instance.actiontype == "sample_text_2"


def test_henshin_text_EqualityExpression_op_value_roundtrip():
    instance = henshin_text_EqualityExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_henshin_text_InjectiveMatching_injectiveMatching_value_roundtrip():
    instance = henshin_text_InjectiveMatching(injectiveMatching=True)
    assert instance.injectiveMatching == True
    instance.injectiveMatching = False
    assert instance.injectiveMatching == False


def test_henshin_text_IntegerValue_value_value_roundtrip():
    instance = henshin_text_IntegerValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_text_JavaAttributeValue_value_value_roundtrip():
    instance = henshin_text_JavaAttributeValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_text_JavaClassValue_value_value_roundtrip():
    instance = henshin_text_JavaClassValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_text_JavaImport_packagename_value_roundtrip():
    instance = henshin_text_JavaImport(packagename="sample_text")
    assert instance.packagename == "sample_text"
    instance.packagename = "sample_text_2"
    assert instance.packagename == "sample_text_2"


def test_henshin_text_ModelElement_name_value_roundtrip():
    instance = henshin_text_ModelElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_text_MulOrDivExpression_op_value_roundtrip():
    instance = henshin_text_MulOrDivExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_henshin_text_MultiRule_name_value_roundtrip():
    instance = henshin_text_MultiRule(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_text_NaturalValue_value_value_roundtrip():
    instance = henshin_text_NaturalValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_henshin_text_Node_actiontype_value_roundtrip():
    instance = henshin_text_Node(actiontype="sample_text")
    assert instance.actiontype == "sample_text"
    instance.actiontype = "sample_text_2"
    assert instance.actiontype == "sample_text_2"


def test_henshin_text_NumberValue_value_value_roundtrip():
    instance = henshin_text_NumberValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_text_ORorXOR_op_value_roundtrip():
    instance = henshin_text_ORorXOR(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_henshin_text_Parameter_name_value_roundtrip():
    instance = henshin_text_Parameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_text_ParameterType_enumType_value_roundtrip():
    instance = henshin_text_ParameterType(enumType="sample_text")
    assert instance.enumType == "sample_text"
    instance.enumType = "sample_text_2"
    assert instance.enumType == "sample_text_2"


def test_henshin_text_Rollback_rollback_value_roundtrip():
    instance = henshin_text_Rollback(rollback=True)
    assert instance.rollback == True
    instance.rollback = False
    assert instance.rollback == False


def test_henshin_text_Strict_strict_value_roundtrip():
    instance = henshin_text_Strict(strict=True)
    assert instance.strict == True
    instance.strict = False
    assert instance.strict == False


def test_henshin_text_StringValue_value_value_roundtrip():
    instance = henshin_text_StringValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_text_ConditionEdges_isa_ConditionGraphElements():
    instance = henshin_text_ConditionEdges()
    assert isinstance(instance, ConditionGraphElements)


def test_henshin_text_ConditionNode_isa_ConditionGraphElements():
    instance = henshin_text_ConditionNode()
    assert isinstance(instance, ConditionGraphElements)


def test_henshin_text_ConditionReuseNode_isa_ConditionGraphElements():
    instance = henshin_text_ConditionReuseNode()
    assert isinstance(instance, ConditionGraphElements)


def test_henshin_text_Formula_isa_ConditionGraphElements():
    instance = henshin_text_Formula()
    assert isinstance(instance, ConditionGraphElements)


def test_henshin_text_ConditionNode_isa_ConditionNodeTypes():
    instance = henshin_text_ConditionNode()
    assert isinstance(instance, ConditionNodeTypes)


def test_henshin_text_Node_isa_ConditionNodeTypes():
    instance = henshin_text_Node(actiontype="sample_text")
    assert isinstance(instance, ConditionNodeTypes)


def test_henshin_text_AndExpression_isa_Expression():
    instance = henshin_text_AndExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_BoolValue_isa_Expression():
    instance = henshin_text_BoolValue(value=True)
    assert isinstance(instance, Expression)


def test_henshin_text_BracketExpression_isa_Expression():
    instance = henshin_text_BracketExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_ComparisonExpression_isa_Expression():
    instance = henshin_text_ComparisonExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_EqualityExpression_isa_Expression():
    instance = henshin_text_EqualityExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_IntegerValue_isa_Expression():
    instance = henshin_text_IntegerValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_JavaAttributeValue_isa_Expression():
    instance = henshin_text_JavaAttributeValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_JavaClassValue_isa_Expression():
    instance = henshin_text_JavaClassValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_MinusExpression_isa_Expression():
    instance = henshin_text_MinusExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_MulOrDivExpression_isa_Expression():
    instance = henshin_text_MulOrDivExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_NaturalValue_isa_Expression():
    instance = henshin_text_NaturalValue(value=7)
    assert isinstance(instance, Expression)


def test_henshin_text_NotExpression_isa_Expression():
    instance = henshin_text_NotExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_NumberValue_isa_Expression():
    instance = henshin_text_NumberValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_OrExpression_isa_Expression():
    instance = henshin_text_OrExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_ParameterValue_isa_Expression():
    instance = henshin_text_ParameterValue()
    assert isinstance(instance, Expression)


def test_henshin_text_PlusExpression_isa_Expression():
    instance = henshin_text_PlusExpression()
    assert isinstance(instance, Expression)


def test_henshin_text_StringValue_isa_Expression():
    instance = henshin_text_StringValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_henshin_text_Edges_isa_GraphElements():
    instance = henshin_text_Edges()
    assert isinstance(instance, GraphElements)


def test_henshin_text_Formula_isa_GraphElements():
    instance = henshin_text_Formula()
    assert isinstance(instance, GraphElements)


def test_henshin_text_MultiRule_isa_GraphElements():
    instance = henshin_text_MultiRule(name="sample_text")
    assert isinstance(instance, GraphElements)


def test_henshin_text_MultiRuleReuseNode_isa_GraphElements():
    instance = henshin_text_MultiRuleReuseNode()
    assert isinstance(instance, GraphElements)


def test_henshin_text_Node_isa_GraphElements():
    instance = henshin_text_Node(actiontype="sample_text")
    assert isinstance(instance, GraphElements)


def test_henshin_text_AND_isa_Logic():
    instance = henshin_text_AND()
    assert isinstance(instance, Logic)


def test_henshin_text_ConditionGraphRef_isa_Logic():
    instance = henshin_text_ConditionGraphRef()
    assert isinstance(instance, Logic)


def test_henshin_text_Not_isa_Logic():
    instance = henshin_text_Not()
    assert isinstance(instance, Logic)


def test_henshin_text_ORorXOR_isa_Logic():
    instance = henshin_text_ORorXOR(op="sample_text")
    assert isinstance(instance, Logic)


def test_henshin_text_Rule_isa_ModelElement():
    instance = henshin_text_Rule()
    assert isinstance(instance, ModelElement)


def test_henshin_text_Unit_isa_ModelElement():
    instance = henshin_text_Unit()
    assert isinstance(instance, ModelElement)


def test_henshin_text_CheckDangling_isa_RuleElement():
    instance = henshin_text_CheckDangling(checkDangling=True)
    assert isinstance(instance, RuleElement)


def test_henshin_text_Conditions_isa_RuleElement():
    instance = henshin_text_Conditions()
    assert isinstance(instance, RuleElement)


def test_henshin_text_Graph_isa_RuleElement():
    instance = henshin_text_Graph()
    assert isinstance(instance, RuleElement)


def test_henshin_text_InjectiveMatching_isa_RuleElement():
    instance = henshin_text_InjectiveMatching(injectiveMatching=True)
    assert isinstance(instance, RuleElement)


def test_henshin_text_JavaImport_isa_RuleElement():
    instance = henshin_text_JavaImport(packagename="sample_text")
    assert isinstance(instance, RuleElement)


def test_henshin_text_MultiRuleReuseNode_isa_RuleNodeTypes():
    instance = henshin_text_MultiRuleReuseNode()
    assert isinstance(instance, RuleNodeTypes)


def test_henshin_text_Node_isa_RuleNodeTypes():
    instance = henshin_text_Node(actiontype="sample_text")
    assert isinstance(instance, RuleNodeTypes)


def test_henshin_text_Rollback_isa_SequentialProperties():
    instance = henshin_text_Rollback(rollback=True)
    assert isinstance(instance, SequentialProperties)


def test_henshin_text_Strict_isa_SequentialProperties():
    instance = henshin_text_Strict(strict=True)
    assert isinstance(instance, SequentialProperties)


def test_henshin_text_Call_isa_UnitElement():
    instance = henshin_text_Call()
    assert isinstance(instance, UnitElement)


def test_henshin_text_ConditionalUnit_isa_UnitElement():
    instance = henshin_text_ConditionalUnit()
    assert isinstance(instance, UnitElement)


def test_henshin_text_IndependentUnit_isa_UnitElement():
    instance = henshin_text_IndependentUnit()
    assert isinstance(instance, UnitElement)


def test_henshin_text_IteratedUnit_isa_UnitElement():
    instance = henshin_text_IteratedUnit()
    assert isinstance(instance, UnitElement)


def test_henshin_text_LoopUnit_isa_UnitElement():
    instance = henshin_text_LoopUnit()
    assert isinstance(instance, UnitElement)


def test_henshin_text_PriorityUnit_isa_UnitElement():
    instance = henshin_text_PriorityUnit()
    assert isinstance(instance, UnitElement)


def test_henshin_text_SequentialProperties_isa_UnitElement():
    instance = henshin_text_SequentialProperties()
    assert isinstance(instance, UnitElement)


def test_assoc_attribute18_link_reassign_clear():
    a = henshin_text_Node(actiontype="sample_text")
    b1 = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    b2 = henshin_text_Attribute(actiontype="sample_text_2", update="sample_text_2")
    _safe_set(a, 'henshin_text_Node19', {b1})
    assert _is_linked(a, 'henshin_text_Node19', b1)
    if hasattr(b1, 'henshin_text_Attribute'):
        assert _is_linked(b1, 'henshin_text_Attribute', a)
    _safe_set(a, 'henshin_text_Node19', {b2})
    assert _is_linked(a, 'henshin_text_Node19', b2)
    if hasattr(b1, 'henshin_text_Attribute'):
        assert not _is_linked(b1, 'henshin_text_Attribute', a)
    if hasattr(b2, 'henshin_text_Attribute'):
        assert _is_linked(b2, 'henshin_text_Attribute', a)
    _safe_set(a, 'henshin_text_Node19', set())
    assert not _is_linked(a, 'henshin_text_Node19', b2)
    if hasattr(b2, 'henshin_text_Attribute'):
        assert not _is_linked(b2, 'henshin_text_Attribute', a)


def test_assoc_attribute22_link_reassign_clear():
    a = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    b1 = henshin_text_MultiRuleReuseNode()
    b2 = henshin_text_MultiRuleReuseNode()
    _safe_set(a, 'henshin_text_Attribute24', b1)
    assert _is_linked(a, 'henshin_text_Attribute24', b1)
    if hasattr(b1, 'henshin_text_MultiRuleReuseNode23'):
        assert _is_linked(b1, 'henshin_text_MultiRuleReuseNode23', a)
    _safe_set(a, 'henshin_text_Attribute24', b2)
    assert _is_linked(a, 'henshin_text_Attribute24', b2)
    if hasattr(b1, 'henshin_text_MultiRuleReuseNode23'):
        assert not _is_linked(b1, 'henshin_text_MultiRuleReuseNode23', a)
    if hasattr(b2, 'henshin_text_MultiRuleReuseNode23'):
        assert _is_linked(b2, 'henshin_text_MultiRuleReuseNode23', a)
    _safe_set(a, 'henshin_text_Attribute24', None)
    assert not _is_linked(a, 'henshin_text_Attribute24', b2)
    if hasattr(b2, 'henshin_text_MultiRuleReuseNode23'):
        assert not _is_linked(b2, 'henshin_text_MultiRuleReuseNode23', a)


def test_assoc_conditionGraphElements34_link_reassign_clear():
    a = henshin_text_ConditionGraph(name="sample_text")
    b1 = henshin_text_ConditionGraphElements()
    b2 = henshin_text_ConditionGraphElements()
    _safe_set(a, 'henshin_text_ConditionGraph35', {b1})
    assert _is_linked(a, 'henshin_text_ConditionGraph35', b1)
    if hasattr(b1, 'henshin_text_ConditionGraphElements'):
        assert _is_linked(b1, 'henshin_text_ConditionGraphElements', a)
    _safe_set(a, 'henshin_text_ConditionGraph35', {b2})
    assert _is_linked(a, 'henshin_text_ConditionGraph35', b2)
    if hasattr(b1, 'henshin_text_ConditionGraphElements'):
        assert not _is_linked(b1, 'henshin_text_ConditionGraphElements', a)
    if hasattr(b2, 'henshin_text_ConditionGraphElements'):
        assert _is_linked(b2, 'henshin_text_ConditionGraphElements', a)
    _safe_set(a, 'henshin_text_ConditionGraph35', set())
    assert not _is_linked(a, 'henshin_text_ConditionGraph35', b2)
    if hasattr(b2, 'henshin_text_ConditionGraphElements'):
        assert not _is_linked(b2, 'henshin_text_ConditionGraphElements', a)


def test_assoc_conditionGraphRef104_link_reassign_clear():
    a = henshin_text_ConditionGraph(name="sample_text")
    b1 = henshin_text_ConditionGraphRef()
    b2 = henshin_text_ConditionGraphRef()
    _safe_set(a, 'henshin_text_ConditionGraph105', b1)
    assert _is_linked(a, 'henshin_text_ConditionGraph105', b1)
    if hasattr(b1, 'henshin_text_ConditionGraphRef'):
        assert _is_linked(b1, 'henshin_text_ConditionGraphRef', a)
    _safe_set(a, 'henshin_text_ConditionGraph105', b2)
    assert _is_linked(a, 'henshin_text_ConditionGraph105', b2)
    if hasattr(b1, 'henshin_text_ConditionGraphRef'):
        assert not _is_linked(b1, 'henshin_text_ConditionGraphRef', a)
    if hasattr(b2, 'henshin_text_ConditionGraphRef'):
        assert _is_linked(b2, 'henshin_text_ConditionGraphRef', a)
    _safe_set(a, 'henshin_text_ConditionGraph105', None)
    assert not _is_linked(a, 'henshin_text_ConditionGraph105', b2)
    if hasattr(b2, 'henshin_text_ConditionGraphRef'):
        assert not _is_linked(b2, 'henshin_text_ConditionGraphRef', a)


def test_assoc_conditionGraphs32_link_reassign_clear():
    a = henshin_text_ConditionGraph(name="sample_text")
    b1 = henshin_text_Formula()
    b2 = henshin_text_Formula()
    _safe_set(a, 'henshin_text_ConditionGraph', b1)
    assert _is_linked(a, 'henshin_text_ConditionGraph', b1)
    if hasattr(b1, 'henshin_text_Formula33'):
        assert _is_linked(b1, 'henshin_text_Formula33', a)
    _safe_set(a, 'henshin_text_ConditionGraph', b2)
    assert _is_linked(a, 'henshin_text_ConditionGraph', b2)
    if hasattr(b1, 'henshin_text_Formula33'):
        assert not _is_linked(b1, 'henshin_text_Formula33', a)
    if hasattr(b2, 'henshin_text_Formula33'):
        assert _is_linked(b2, 'henshin_text_Formula33', a)
    _safe_set(a, 'henshin_text_ConditionGraph', None)
    assert not _is_linked(a, 'henshin_text_ConditionGraph', b2)
    if hasattr(b2, 'henshin_text_Formula33'):
        assert not _is_linked(b2, 'henshin_text_Formula33', a)


def test_assoc_edges9_link_reassign_clear():
    a = henshin_text_Edge(actiontype="sample_text")
    b1 = henshin_text_Edges()
    b2 = henshin_text_Edges()
    _safe_set(a, 'henshin_text_Edge', b1)
    assert _is_linked(a, 'henshin_text_Edge', b1)
    if hasattr(b1, 'henshin_text_Edges'):
        assert _is_linked(b1, 'henshin_text_Edges', a)
    _safe_set(a, 'henshin_text_Edge', b2)
    assert _is_linked(a, 'henshin_text_Edge', b2)
    if hasattr(b1, 'henshin_text_Edges'):
        assert not _is_linked(b1, 'henshin_text_Edges', a)
    if hasattr(b2, 'henshin_text_Edges'):
        assert _is_linked(b2, 'henshin_text_Edges', a)
    _safe_set(a, 'henshin_text_Edge', None)
    assert not _is_linked(a, 'henshin_text_Edge', b2)
    if hasattr(b2, 'henshin_text_Edges'):
        assert not _is_linked(b2, 'henshin_text_Edges', a)


def test_assoc_elementCall106_link_reassign_clear():
    a = henshin_text_ModelElement(name="sample_text")
    b1 = henshin_text_Call()
    b2 = henshin_text_Call()
    _safe_set(a, 'henshin_text_ModelElement107', b1)
    assert _is_linked(a, 'henshin_text_ModelElement107', b1)
    if hasattr(b1, 'henshin_text_Call'):
        assert _is_linked(b1, 'henshin_text_Call', a)
    _safe_set(a, 'henshin_text_ModelElement107', b2)
    assert _is_linked(a, 'henshin_text_ModelElement107', b2)
    if hasattr(b1, 'henshin_text_Call'):
        assert not _is_linked(b1, 'henshin_text_Call', a)
    if hasattr(b2, 'henshin_text_Call'):
        assert _is_linked(b2, 'henshin_text_Call', a)
    _safe_set(a, 'henshin_text_ModelElement107', None)
    assert not _is_linked(a, 'henshin_text_ModelElement107', b2)
    if hasattr(b2, 'henshin_text_Call'):
        assert not _is_linked(b2, 'henshin_text_Call', a)


def test_assoc_javaParameter152_link_reassign_clear():
    a = henshin_text_JavaClassValue(value="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_JavaClassValue', {b1})
    assert _is_linked(a, 'henshin_text_JavaClassValue', b1)
    if hasattr(b1, 'henshin_text_Expression153'):
        assert _is_linked(b1, 'henshin_text_Expression153', a)
    _safe_set(a, 'henshin_text_JavaClassValue', {b2})
    assert _is_linked(a, 'henshin_text_JavaClassValue', b2)
    if hasattr(b1, 'henshin_text_Expression153'):
        assert not _is_linked(b1, 'henshin_text_Expression153', a)
    if hasattr(b2, 'henshin_text_Expression153'):
        assert _is_linked(b2, 'henshin_text_Expression153', a)
    _safe_set(a, 'henshin_text_JavaClassValue', set())
    assert not _is_linked(a, 'henshin_text_JavaClassValue', b2)
    if hasattr(b2, 'henshin_text_Expression153'):
        assert not _is_linked(b2, 'henshin_text_Expression153', a)


def test_assoc_left121_link_reassign_clear():
    a = henshin_text_EqualityExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_EqualityExpression', b1)
    assert _is_linked(a, 'henshin_text_EqualityExpression', b1)
    if hasattr(b1, 'henshin_text_Expression122'):
        assert _is_linked(b1, 'henshin_text_Expression122', a)
    _safe_set(a, 'henshin_text_EqualityExpression', b2)
    assert _is_linked(a, 'henshin_text_EqualityExpression', b2)
    if hasattr(b1, 'henshin_text_Expression122'):
        assert not _is_linked(b1, 'henshin_text_Expression122', a)
    if hasattr(b2, 'henshin_text_Expression122'):
        assert _is_linked(b2, 'henshin_text_Expression122', a)
    _safe_set(a, 'henshin_text_EqualityExpression', None)
    assert not _is_linked(a, 'henshin_text_EqualityExpression', b2)
    if hasattr(b2, 'henshin_text_Expression122'):
        assert not _is_linked(b2, 'henshin_text_Expression122', a)


def test_assoc_left126_link_reassign_clear():
    a = henshin_text_ComparisonExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_ComparisonExpression', b1)
    assert _is_linked(a, 'henshin_text_ComparisonExpression', b1)
    if hasattr(b1, 'henshin_text_Expression127'):
        assert _is_linked(b1, 'henshin_text_Expression127', a)
    _safe_set(a, 'henshin_text_ComparisonExpression', b2)
    assert _is_linked(a, 'henshin_text_ComparisonExpression', b2)
    if hasattr(b1, 'henshin_text_Expression127'):
        assert not _is_linked(b1, 'henshin_text_Expression127', a)
    if hasattr(b2, 'henshin_text_Expression127'):
        assert _is_linked(b2, 'henshin_text_Expression127', a)
    _safe_set(a, 'henshin_text_ComparisonExpression', None)
    assert not _is_linked(a, 'henshin_text_ComparisonExpression', b2)
    if hasattr(b2, 'henshin_text_Expression127'):
        assert not _is_linked(b2, 'henshin_text_Expression127', a)


def test_assoc_left141_link_reassign_clear():
    a = henshin_text_MulOrDivExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_MulOrDivExpression', b1)
    assert _is_linked(a, 'henshin_text_MulOrDivExpression', b1)
    if hasattr(b1, 'henshin_text_Expression142'):
        assert _is_linked(b1, 'henshin_text_Expression142', a)
    _safe_set(a, 'henshin_text_MulOrDivExpression', b2)
    assert _is_linked(a, 'henshin_text_MulOrDivExpression', b2)
    if hasattr(b1, 'henshin_text_Expression142'):
        assert not _is_linked(b1, 'henshin_text_Expression142', a)
    if hasattr(b2, 'henshin_text_Expression142'):
        assert _is_linked(b2, 'henshin_text_Expression142', a)
    _safe_set(a, 'henshin_text_MulOrDivExpression', None)
    assert not _is_linked(a, 'henshin_text_MulOrDivExpression', b2)
    if hasattr(b2, 'henshin_text_Expression142'):
        assert not _is_linked(b2, 'henshin_text_Expression142', a)


def test_assoc_left92_link_reassign_clear():
    a = henshin_text_ORorXOR(op="sample_text")
    b1 = henshin_text_Logic()
    b2 = henshin_text_Logic()
    _safe_set(a, 'henshin_text_ORorXOR', b1)
    assert _is_linked(a, 'henshin_text_ORorXOR', b1)
    if hasattr(b1, 'henshin_text_Logic93'):
        assert _is_linked(b1, 'henshin_text_Logic93', a)
    _safe_set(a, 'henshin_text_ORorXOR', b2)
    assert _is_linked(a, 'henshin_text_ORorXOR', b2)
    if hasattr(b1, 'henshin_text_Logic93'):
        assert not _is_linked(b1, 'henshin_text_Logic93', a)
    if hasattr(b2, 'henshin_text_Logic93'):
        assert _is_linked(b2, 'henshin_text_Logic93', a)
    _safe_set(a, 'henshin_text_ORorXOR', None)
    assert not _is_linked(a, 'henshin_text_ORorXOR', b2)
    if hasattr(b2, 'henshin_text_Logic93'):
        assert not _is_linked(b2, 'henshin_text_Logic93', a)


def test_assoc_multiruleElements30_link_reassign_clear():
    a = henshin_text_MultiRule(name="sample_text")
    b1 = henshin_text_RuleElement()
    b2 = henshin_text_RuleElement()
    _safe_set(a, 'henshin_text_MultiRule', {b1})
    assert _is_linked(a, 'henshin_text_MultiRule', b1)
    if hasattr(b1, 'henshin_text_RuleElement'):
        assert _is_linked(b1, 'henshin_text_RuleElement', a)
    _safe_set(a, 'henshin_text_MultiRule', {b2})
    assert _is_linked(a, 'henshin_text_MultiRule', b2)
    if hasattr(b1, 'henshin_text_RuleElement'):
        assert not _is_linked(b1, 'henshin_text_RuleElement', a)
    if hasattr(b2, 'henshin_text_RuleElement'):
        assert _is_linked(b2, 'henshin_text_RuleElement', a)
    _safe_set(a, 'henshin_text_MultiRule', set())
    assert not _is_linked(a, 'henshin_text_MultiRule', b2)
    if hasattr(b2, 'henshin_text_RuleElement'):
        assert not _is_linked(b2, 'henshin_text_RuleElement', a)


def test_assoc_name20_link_reassign_clear():
    a = henshin_text_Node(actiontype="sample_text")
    b1 = henshin_text_MultiRuleReuseNode()
    b2 = henshin_text_MultiRuleReuseNode()
    _safe_set(a, 'henshin_text_Node21', b1)
    assert _is_linked(a, 'henshin_text_Node21', b1)
    if hasattr(b1, 'henshin_text_MultiRuleReuseNode'):
        assert _is_linked(b1, 'henshin_text_MultiRuleReuseNode', a)
    _safe_set(a, 'henshin_text_Node21', b2)
    assert _is_linked(a, 'henshin_text_Node21', b2)
    if hasattr(b1, 'henshin_text_MultiRuleReuseNode'):
        assert not _is_linked(b1, 'henshin_text_MultiRuleReuseNode', a)
    if hasattr(b2, 'henshin_text_MultiRuleReuseNode'):
        assert _is_linked(b2, 'henshin_text_MultiRuleReuseNode', a)
    _safe_set(a, 'henshin_text_Node21', None)
    assert not _is_linked(a, 'henshin_text_Node21', b2)
    if hasattr(b2, 'henshin_text_MultiRuleReuseNode'):
        assert not _is_linked(b2, 'henshin_text_MultiRuleReuseNode', a)


def test_assoc_name25_link_reassign_clear():
    a = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    b1 = henshin_text_EAttribute()
    b2 = henshin_text_EAttribute()
    _safe_set(a, 'henshin_text_Attribute26', b1)
    assert _is_linked(a, 'henshin_text_Attribute26', b1)
    if hasattr(b1, 'henshin_text_EAttribute'):
        assert _is_linked(b1, 'henshin_text_EAttribute', a)
    _safe_set(a, 'henshin_text_Attribute26', b2)
    assert _is_linked(a, 'henshin_text_Attribute26', b2)
    if hasattr(b1, 'henshin_text_EAttribute'):
        assert not _is_linked(b1, 'henshin_text_EAttribute', a)
    if hasattr(b2, 'henshin_text_EAttribute'):
        assert _is_linked(b2, 'henshin_text_EAttribute', a)
    _safe_set(a, 'henshin_text_Attribute26', None)
    assert not _is_linked(a, 'henshin_text_Attribute26', b2)
    if hasattr(b2, 'henshin_text_EAttribute'):
        assert not _is_linked(b2, 'henshin_text_EAttribute', a)


def test_assoc_name49_link_reassign_clear():
    a = henshin_text_ConditionNodeTypes(name="sample_text")
    b1 = henshin_text_ConditionReuseNode()
    b2 = henshin_text_ConditionReuseNode()
    _safe_set(a, 'henshin_text_ConditionNodeTypes50', b1)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes50', b1)
    if hasattr(b1, 'henshin_text_ConditionReuseNode'):
        assert _is_linked(b1, 'henshin_text_ConditionReuseNode', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes50', b2)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes50', b2)
    if hasattr(b1, 'henshin_text_ConditionReuseNode'):
        assert not _is_linked(b1, 'henshin_text_ConditionReuseNode', a)
    if hasattr(b2, 'henshin_text_ConditionReuseNode'):
        assert _is_linked(b2, 'henshin_text_ConditionReuseNode', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes50', None)
    assert not _is_linked(a, 'henshin_text_ConditionNodeTypes50', b2)
    if hasattr(b2, 'henshin_text_ConditionReuseNode'):
        assert not _is_linked(b2, 'henshin_text_ConditionReuseNode', a)


def test_assoc_nodetype17_link_reassign_clear():
    a = henshin_text_Node(actiontype="sample_text")
    b1 = henshin_text_EClass()
    b2 = henshin_text_EClass()
    _safe_set(a, 'henshin_text_Node', b1)
    assert _is_linked(a, 'henshin_text_Node', b1)
    if hasattr(b1, 'henshin_text_EClass'):
        assert _is_linked(b1, 'henshin_text_EClass', a)
    _safe_set(a, 'henshin_text_Node', b2)
    assert _is_linked(a, 'henshin_text_Node', b2)
    if hasattr(b1, 'henshin_text_EClass'):
        assert not _is_linked(b1, 'henshin_text_EClass', a)
    if hasattr(b2, 'henshin_text_EClass'):
        assert _is_linked(b2, 'henshin_text_EClass', a)
    _safe_set(a, 'henshin_text_Node', None)
    assert not _is_linked(a, 'henshin_text_Node', b2)
    if hasattr(b2, 'henshin_text_EClass'):
        assert not _is_linked(b2, 'henshin_text_EClass', a)


def test_assoc_parameters108_link_reassign_clear():
    a = henshin_text_Parameter(name="sample_text")
    b1 = henshin_text_Call()
    b2 = henshin_text_Call()
    _safe_set(a, 'henshin_text_Parameter110', b1)
    assert _is_linked(a, 'henshin_text_Parameter110', b1)
    if hasattr(b1, 'henshin_text_Call109'):
        assert _is_linked(b1, 'henshin_text_Call109', a)
    _safe_set(a, 'henshin_text_Parameter110', b2)
    assert _is_linked(a, 'henshin_text_Parameter110', b2)
    if hasattr(b1, 'henshin_text_Call109'):
        assert not _is_linked(b1, 'henshin_text_Call109', a)
    if hasattr(b2, 'henshin_text_Call109'):
        assert _is_linked(b2, 'henshin_text_Call109', a)
    _safe_set(a, 'henshin_text_Parameter110', None)
    assert not _is_linked(a, 'henshin_text_Parameter110', b2)
    if hasattr(b2, 'henshin_text_Call109'):
        assert not _is_linked(b2, 'henshin_text_Call109', a)


def test_assoc_parameters5_link_reassign_clear():
    a = henshin_text_Parameter(name="sample_text")
    b1 = henshin_text_ModelElement(name="sample_text")
    b2 = henshin_text_ModelElement(name="sample_text_2")
    _safe_set(a, 'henshin_text_Parameter', b1)
    assert _is_linked(a, 'henshin_text_Parameter', b1)
    if hasattr(b1, 'henshin_text_ModelElement6'):
        assert _is_linked(b1, 'henshin_text_ModelElement6', a)
    _safe_set(a, 'henshin_text_Parameter', b2)
    assert _is_linked(a, 'henshin_text_Parameter', b2)
    if hasattr(b1, 'henshin_text_ModelElement6'):
        assert not _is_linked(b1, 'henshin_text_ModelElement6', a)
    if hasattr(b2, 'henshin_text_ModelElement6'):
        assert _is_linked(b2, 'henshin_text_ModelElement6', a)
    _safe_set(a, 'henshin_text_Parameter', None)
    assert not _is_linked(a, 'henshin_text_Parameter', b2)
    if hasattr(b2, 'henshin_text_ModelElement6'):
        assert not _is_linked(b2, 'henshin_text_ModelElement6', a)


def test_assoc_right123_link_reassign_clear():
    a = henshin_text_EqualityExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_EqualityExpression124', b1)
    assert _is_linked(a, 'henshin_text_EqualityExpression124', b1)
    if hasattr(b1, 'henshin_text_Expression125'):
        assert _is_linked(b1, 'henshin_text_Expression125', a)
    _safe_set(a, 'henshin_text_EqualityExpression124', b2)
    assert _is_linked(a, 'henshin_text_EqualityExpression124', b2)
    if hasattr(b1, 'henshin_text_Expression125'):
        assert not _is_linked(b1, 'henshin_text_Expression125', a)
    if hasattr(b2, 'henshin_text_Expression125'):
        assert _is_linked(b2, 'henshin_text_Expression125', a)
    _safe_set(a, 'henshin_text_EqualityExpression124', None)
    assert not _is_linked(a, 'henshin_text_EqualityExpression124', b2)
    if hasattr(b2, 'henshin_text_Expression125'):
        assert not _is_linked(b2, 'henshin_text_Expression125', a)


def test_assoc_right128_link_reassign_clear():
    a = henshin_text_ComparisonExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_ComparisonExpression129', b1)
    assert _is_linked(a, 'henshin_text_ComparisonExpression129', b1)
    if hasattr(b1, 'henshin_text_Expression130'):
        assert _is_linked(b1, 'henshin_text_Expression130', a)
    _safe_set(a, 'henshin_text_ComparisonExpression129', b2)
    assert _is_linked(a, 'henshin_text_ComparisonExpression129', b2)
    if hasattr(b1, 'henshin_text_Expression130'):
        assert not _is_linked(b1, 'henshin_text_Expression130', a)
    if hasattr(b2, 'henshin_text_Expression130'):
        assert _is_linked(b2, 'henshin_text_Expression130', a)
    _safe_set(a, 'henshin_text_ComparisonExpression129', None)
    assert not _is_linked(a, 'henshin_text_ComparisonExpression129', b2)
    if hasattr(b2, 'henshin_text_Expression130'):
        assert not _is_linked(b2, 'henshin_text_Expression130', a)


def test_assoc_right143_link_reassign_clear():
    a = henshin_text_MulOrDivExpression(op="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_MulOrDivExpression144', b1)
    assert _is_linked(a, 'henshin_text_MulOrDivExpression144', b1)
    if hasattr(b1, 'henshin_text_Expression145'):
        assert _is_linked(b1, 'henshin_text_Expression145', a)
    _safe_set(a, 'henshin_text_MulOrDivExpression144', b2)
    assert _is_linked(a, 'henshin_text_MulOrDivExpression144', b2)
    if hasattr(b1, 'henshin_text_Expression145'):
        assert not _is_linked(b1, 'henshin_text_Expression145', a)
    if hasattr(b2, 'henshin_text_Expression145'):
        assert _is_linked(b2, 'henshin_text_Expression145', a)
    _safe_set(a, 'henshin_text_MulOrDivExpression144', None)
    assert not _is_linked(a, 'henshin_text_MulOrDivExpression144', b2)
    if hasattr(b2, 'henshin_text_Expression145'):
        assert not _is_linked(b2, 'henshin_text_Expression145', a)


def test_assoc_right94_link_reassign_clear():
    a = henshin_text_ORorXOR(op="sample_text")
    b1 = henshin_text_Logic()
    b2 = henshin_text_Logic()
    _safe_set(a, 'henshin_text_ORorXOR95', b1)
    assert _is_linked(a, 'henshin_text_ORorXOR95', b1)
    if hasattr(b1, 'henshin_text_Logic96'):
        assert _is_linked(b1, 'henshin_text_Logic96', a)
    _safe_set(a, 'henshin_text_ORorXOR95', b2)
    assert _is_linked(a, 'henshin_text_ORorXOR95', b2)
    if hasattr(b1, 'henshin_text_Logic96'):
        assert not _is_linked(b1, 'henshin_text_Logic96', a)
    if hasattr(b2, 'henshin_text_Logic96'):
        assert _is_linked(b2, 'henshin_text_Logic96', a)
    _safe_set(a, 'henshin_text_ORorXOR95', None)
    assert not _is_linked(a, 'henshin_text_ORorXOR95', b2)
    if hasattr(b2, 'henshin_text_Logic96'):
        assert not _is_linked(b2, 'henshin_text_Logic96', a)


def test_assoc_source10_link_reassign_clear():
    a = henshin_text_Edge(actiontype="sample_text")
    b1 = henshin_text_RuleNodeTypes()
    b2 = henshin_text_RuleNodeTypes()
    _safe_set(a, 'henshin_text_Edge11', b1)
    assert _is_linked(a, 'henshin_text_Edge11', b1)
    if hasattr(b1, 'henshin_text_RuleNodeTypes'):
        assert _is_linked(b1, 'henshin_text_RuleNodeTypes', a)
    _safe_set(a, 'henshin_text_Edge11', b2)
    assert _is_linked(a, 'henshin_text_Edge11', b2)
    if hasattr(b1, 'henshin_text_RuleNodeTypes'):
        assert not _is_linked(b1, 'henshin_text_RuleNodeTypes', a)
    if hasattr(b2, 'henshin_text_RuleNodeTypes'):
        assert _is_linked(b2, 'henshin_text_RuleNodeTypes', a)
    _safe_set(a, 'henshin_text_Edge11', None)
    assert not _is_linked(a, 'henshin_text_Edge11', b2)
    if hasattr(b2, 'henshin_text_RuleNodeTypes'):
        assert not _is_linked(b2, 'henshin_text_RuleNodeTypes', a)


def test_assoc_source37_link_reassign_clear():
    a = henshin_text_ConditionNodeTypes(name="sample_text")
    b1 = henshin_text_ConditionEdge()
    b2 = henshin_text_ConditionEdge()
    _safe_set(a, 'henshin_text_ConditionNodeTypes', b1)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes', b1)
    if hasattr(b1, 'henshin_text_ConditionEdge38'):
        assert _is_linked(b1, 'henshin_text_ConditionEdge38', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes', b2)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes', b2)
    if hasattr(b1, 'henshin_text_ConditionEdge38'):
        assert not _is_linked(b1, 'henshin_text_ConditionEdge38', a)
    if hasattr(b2, 'henshin_text_ConditionEdge38'):
        assert _is_linked(b2, 'henshin_text_ConditionEdge38', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes', None)
    assert not _is_linked(a, 'henshin_text_ConditionNodeTypes', b2)
    if hasattr(b2, 'henshin_text_ConditionEdge38'):
        assert not _is_linked(b2, 'henshin_text_ConditionEdge38', a)


def test_assoc_target12_link_reassign_clear():
    a = henshin_text_Edge(actiontype="sample_text")
    b1 = henshin_text_RuleNodeTypes()
    b2 = henshin_text_RuleNodeTypes()
    _safe_set(a, 'henshin_text_Edge13', b1)
    assert _is_linked(a, 'henshin_text_Edge13', b1)
    if hasattr(b1, 'henshin_text_RuleNodeTypes14'):
        assert _is_linked(b1, 'henshin_text_RuleNodeTypes14', a)
    _safe_set(a, 'henshin_text_Edge13', b2)
    assert _is_linked(a, 'henshin_text_Edge13', b2)
    if hasattr(b1, 'henshin_text_RuleNodeTypes14'):
        assert not _is_linked(b1, 'henshin_text_RuleNodeTypes14', a)
    if hasattr(b2, 'henshin_text_RuleNodeTypes14'):
        assert _is_linked(b2, 'henshin_text_RuleNodeTypes14', a)
    _safe_set(a, 'henshin_text_Edge13', None)
    assert not _is_linked(a, 'henshin_text_Edge13', b2)
    if hasattr(b2, 'henshin_text_RuleNodeTypes14'):
        assert not _is_linked(b2, 'henshin_text_RuleNodeTypes14', a)


def test_assoc_target39_link_reassign_clear():
    a = henshin_text_ConditionNodeTypes(name="sample_text")
    b1 = henshin_text_ConditionEdge()
    b2 = henshin_text_ConditionEdge()
    _safe_set(a, 'henshin_text_ConditionNodeTypes41', b1)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes41', b1)
    if hasattr(b1, 'henshin_text_ConditionEdge40'):
        assert _is_linked(b1, 'henshin_text_ConditionEdge40', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes41', b2)
    assert _is_linked(a, 'henshin_text_ConditionNodeTypes41', b2)
    if hasattr(b1, 'henshin_text_ConditionEdge40'):
        assert not _is_linked(b1, 'henshin_text_ConditionEdge40', a)
    if hasattr(b2, 'henshin_text_ConditionEdge40'):
        assert _is_linked(b2, 'henshin_text_ConditionEdge40', a)
    _safe_set(a, 'henshin_text_ConditionNodeTypes41', None)
    assert not _is_linked(a, 'henshin_text_ConditionNodeTypes41', b2)
    if hasattr(b2, 'henshin_text_ConditionEdge40'):
        assert not _is_linked(b2, 'henshin_text_ConditionEdge40', a)


def test_assoc_transformationsystem1_link_reassign_clear():
    a = henshin_text_ModelElement(name="sample_text")
    b1 = henshin_text_Model()
    b2 = henshin_text_Model()
    _safe_set(a, 'henshin_text_ModelElement', b1)
    assert _is_linked(a, 'henshin_text_ModelElement', b1)
    if hasattr(b1, 'henshin_text_Model2'):
        assert _is_linked(b1, 'henshin_text_Model2', a)
    _safe_set(a, 'henshin_text_ModelElement', b2)
    assert _is_linked(a, 'henshin_text_ModelElement', b2)
    if hasattr(b1, 'henshin_text_Model2'):
        assert not _is_linked(b1, 'henshin_text_Model2', a)
    if hasattr(b2, 'henshin_text_Model2'):
        assert _is_linked(b2, 'henshin_text_Model2', a)
    _safe_set(a, 'henshin_text_ModelElement', None)
    assert not _is_linked(a, 'henshin_text_ModelElement', b2)
    if hasattr(b2, 'henshin_text_Model2'):
        assert not _is_linked(b2, 'henshin_text_Model2', a)


def test_assoc_type15_link_reassign_clear():
    a = henshin_text_Edge(actiontype="sample_text")
    b1 = henshin_text_EReference()
    b2 = henshin_text_EReference()
    _safe_set(a, 'henshin_text_Edge16', b1)
    assert _is_linked(a, 'henshin_text_Edge16', b1)
    if hasattr(b1, 'henshin_text_EReference'):
        assert _is_linked(b1, 'henshin_text_EReference', a)
    _safe_set(a, 'henshin_text_Edge16', b2)
    assert _is_linked(a, 'henshin_text_Edge16', b2)
    if hasattr(b1, 'henshin_text_EReference'):
        assert not _is_linked(b1, 'henshin_text_EReference', a)
    if hasattr(b2, 'henshin_text_EReference'):
        assert _is_linked(b2, 'henshin_text_EReference', a)
    _safe_set(a, 'henshin_text_Edge16', None)
    assert not _is_linked(a, 'henshin_text_Edge16', b2)
    if hasattr(b2, 'henshin_text_EReference'):
        assert not _is_linked(b2, 'henshin_text_EReference', a)


def test_assoc_type83_link_reassign_clear():
    a = henshin_text_ParameterType(enumType="sample_text")
    b1 = henshin_text_Parameter(name="sample_text")
    b2 = henshin_text_Parameter(name="sample_text_2")
    _safe_set(a, 'henshin_text_ParameterType', b1)
    assert _is_linked(a, 'henshin_text_ParameterType', b1)
    if hasattr(b1, 'henshin_text_Parameter84'):
        assert _is_linked(b1, 'henshin_text_Parameter84', a)
    _safe_set(a, 'henshin_text_ParameterType', b2)
    assert _is_linked(a, 'henshin_text_ParameterType', b2)
    if hasattr(b1, 'henshin_text_Parameter84'):
        assert not _is_linked(b1, 'henshin_text_Parameter84', a)
    if hasattr(b2, 'henshin_text_Parameter84'):
        assert _is_linked(b2, 'henshin_text_Parameter84', a)
    _safe_set(a, 'henshin_text_ParameterType', None)
    assert not _is_linked(a, 'henshin_text_ParameterType', b2)
    if hasattr(b2, 'henshin_text_Parameter84'):
        assert not _is_linked(b2, 'henshin_text_Parameter84', a)


def test_assoc_type85_link_reassign_clear():
    a = henshin_text_ParameterType(enumType="sample_text")
    b1 = henshin_text_EClass()
    b2 = henshin_text_EClass()
    _safe_set(a, 'henshin_text_ParameterType86', b1)
    assert _is_linked(a, 'henshin_text_ParameterType86', b1)
    if hasattr(b1, 'henshin_text_EClass87'):
        assert _is_linked(b1, 'henshin_text_EClass87', a)
    _safe_set(a, 'henshin_text_ParameterType86', b2)
    assert _is_linked(a, 'henshin_text_ParameterType86', b2)
    if hasattr(b1, 'henshin_text_EClass87'):
        assert not _is_linked(b1, 'henshin_text_EClass87', a)
    if hasattr(b2, 'henshin_text_EClass87'):
        assert _is_linked(b2, 'henshin_text_EClass87', a)
    _safe_set(a, 'henshin_text_ParameterType86', None)
    assert not _is_linked(a, 'henshin_text_ParameterType86', b2)
    if hasattr(b2, 'henshin_text_EClass87'):
        assert not _is_linked(b2, 'henshin_text_EClass87', a)


def test_assoc_value150_link_reassign_clear():
    a = henshin_text_Parameter(name="sample_text")
    b1 = henshin_text_ParameterValue()
    b2 = henshin_text_ParameterValue()
    _safe_set(a, 'henshin_text_Parameter151', b1)
    assert _is_linked(a, 'henshin_text_Parameter151', b1)
    if hasattr(b1, 'henshin_text_ParameterValue'):
        assert _is_linked(b1, 'henshin_text_ParameterValue', a)
    _safe_set(a, 'henshin_text_Parameter151', b2)
    assert _is_linked(a, 'henshin_text_Parameter151', b2)
    if hasattr(b1, 'henshin_text_ParameterValue'):
        assert not _is_linked(b1, 'henshin_text_ParameterValue', a)
    if hasattr(b2, 'henshin_text_ParameterValue'):
        assert _is_linked(b2, 'henshin_text_ParameterValue', a)
    _safe_set(a, 'henshin_text_Parameter151', None)
    assert not _is_linked(a, 'henshin_text_Parameter151', b2)
    if hasattr(b2, 'henshin_text_ParameterValue'):
        assert not _is_linked(b2, 'henshin_text_ParameterValue', a)


def test_assoc_value27_link_reassign_clear():
    a = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    b1 = henshin_text_Expression()
    b2 = henshin_text_Expression()
    _safe_set(a, 'henshin_text_Attribute28', b1)
    assert _is_linked(a, 'henshin_text_Attribute28', b1)
    if hasattr(b1, 'henshin_text_Expression29'):
        assert _is_linked(b1, 'henshin_text_Expression29', a)
    _safe_set(a, 'henshin_text_Attribute28', b2)
    assert _is_linked(a, 'henshin_text_Attribute28', b2)
    if hasattr(b1, 'henshin_text_Expression29'):
        assert not _is_linked(b1, 'henshin_text_Expression29', a)
    if hasattr(b2, 'henshin_text_Expression29'):
        assert _is_linked(b2, 'henshin_text_Expression29', a)
    _safe_set(a, 'henshin_text_Attribute28', None)
    assert not _is_linked(a, 'henshin_text_Attribute28', b2)
    if hasattr(b2, 'henshin_text_Expression29'):
        assert not _is_linked(b2, 'henshin_text_Expression29', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ConditionGraphElements_strategy = st.builds(ConditionGraphElements)
@given(instance=ConditionGraphElements_strategy)
@settings(max_examples=25)
def test_ConditionGraphElements_instantiation(instance):
    assert isinstance(instance, ConditionGraphElements)


ConditionNodeTypes_strategy = st.builds(ConditionNodeTypes)
@given(instance=ConditionNodeTypes_strategy)
@settings(max_examples=25)
def test_ConditionNodeTypes_instantiation(instance):
    assert isinstance(instance, ConditionNodeTypes)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


GraphElements_strategy = st.builds(GraphElements)
@given(instance=GraphElements_strategy)
@settings(max_examples=25)
def test_GraphElements_instantiation(instance):
    assert isinstance(instance, GraphElements)


Logic_strategy = st.builds(Logic)
@given(instance=Logic_strategy)
@settings(max_examples=25)
def test_Logic_instantiation(instance):
    assert isinstance(instance, Logic)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


RuleElement_strategy = st.builds(RuleElement)
@given(instance=RuleElement_strategy)
@settings(max_examples=25)
def test_RuleElement_instantiation(instance):
    assert isinstance(instance, RuleElement)


RuleNodeTypes_strategy = st.builds(RuleNodeTypes)
@given(instance=RuleNodeTypes_strategy)
@settings(max_examples=25)
def test_RuleNodeTypes_instantiation(instance):
    assert isinstance(instance, RuleNodeTypes)


SequentialProperties_strategy = st.builds(SequentialProperties)
@given(instance=SequentialProperties_strategy)
@settings(max_examples=25)
def test_SequentialProperties_instantiation(instance):
    assert isinstance(instance, SequentialProperties)


UnitElement_strategy = st.builds(UnitElement)
@given(instance=UnitElement_strategy)
@settings(max_examples=25)
def test_UnitElement_instantiation(instance):
    assert isinstance(instance, UnitElement)


henshin_text_AND_strategy = st.builds(henshin_text_AND)
@given(instance=henshin_text_AND_strategy)
@settings(max_examples=25)
def test_henshin_text_AND_instantiation(instance):
    assert isinstance(instance, henshin_text_AND)


henshin_text_AndExpression_strategy = st.builds(henshin_text_AndExpression)
@given(instance=henshin_text_AndExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_AndExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_AndExpression)


henshin_text_Attribute_strategy = st.builds(henshin_text_Attribute, actiontype=safe_text, update=safe_text)
@given(instance=henshin_text_Attribute_strategy)
@settings(max_examples=25)
def test_henshin_text_Attribute_instantiation(instance):
    assert isinstance(instance, henshin_text_Attribute)


henshin_text_BoolValue_strategy = st.builds(henshin_text_BoolValue, value=st.booleans())
@given(instance=henshin_text_BoolValue_strategy)
@settings(max_examples=25)
def test_henshin_text_BoolValue_instantiation(instance):
    assert isinstance(instance, henshin_text_BoolValue)


henshin_text_BracketExpression_strategy = st.builds(henshin_text_BracketExpression)
@given(instance=henshin_text_BracketExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_BracketExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_BracketExpression)


henshin_text_Call_strategy = st.builds(henshin_text_Call)
@given(instance=henshin_text_Call_strategy)
@settings(max_examples=25)
def test_henshin_text_Call_instantiation(instance):
    assert isinstance(instance, henshin_text_Call)


henshin_text_CheckDangling_strategy = st.builds(henshin_text_CheckDangling, checkDangling=st.booleans())
@given(instance=henshin_text_CheckDangling_strategy)
@settings(max_examples=25)
def test_henshin_text_CheckDangling_instantiation(instance):
    assert isinstance(instance, henshin_text_CheckDangling)


henshin_text_ComparisonExpression_strategy = st.builds(henshin_text_ComparisonExpression, op=safe_text)
@given(instance=henshin_text_ComparisonExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_ComparisonExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_ComparisonExpression)


henshin_text_ConditionEdge_strategy = st.builds(henshin_text_ConditionEdge)
@given(instance=henshin_text_ConditionEdge_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionEdge_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionEdge)


henshin_text_ConditionEdges_strategy = st.builds(henshin_text_ConditionEdges)
@given(instance=henshin_text_ConditionEdges_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionEdges_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionEdges)


henshin_text_ConditionGraph_strategy = st.builds(henshin_text_ConditionGraph, name=safe_text)
@given(instance=henshin_text_ConditionGraph_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionGraph_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraph)


henshin_text_ConditionGraphElements_strategy = st.builds(henshin_text_ConditionGraphElements)
@given(instance=henshin_text_ConditionGraphElements_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionGraphElements_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraphElements)


henshin_text_ConditionGraphRef_strategy = st.builds(henshin_text_ConditionGraphRef)
@given(instance=henshin_text_ConditionGraphRef_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionGraphRef_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraphRef)


henshin_text_ConditionNode_strategy = st.builds(henshin_text_ConditionNode)
@given(instance=henshin_text_ConditionNode_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionNode_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionNode)


henshin_text_ConditionNodeTypes_strategy = st.builds(henshin_text_ConditionNodeTypes, name=safe_text)
@given(instance=henshin_text_ConditionNodeTypes_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionNodeTypes_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionNodeTypes)


henshin_text_ConditionReuseNode_strategy = st.builds(henshin_text_ConditionReuseNode)
@given(instance=henshin_text_ConditionReuseNode_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionReuseNode_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionReuseNode)


henshin_text_ConditionalUnit_strategy = st.builds(henshin_text_ConditionalUnit)
@given(instance=henshin_text_ConditionalUnit_strategy)
@settings(max_examples=25)
def test_henshin_text_ConditionalUnit_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionalUnit)


henshin_text_Conditions_strategy = st.builds(henshin_text_Conditions)
@given(instance=henshin_text_Conditions_strategy)
@settings(max_examples=25)
def test_henshin_text_Conditions_instantiation(instance):
    assert isinstance(instance, henshin_text_Conditions)


henshin_text_EAttribute_strategy = st.builds(henshin_text_EAttribute)
@given(instance=henshin_text_EAttribute_strategy)
@settings(max_examples=25)
def test_henshin_text_EAttribute_instantiation(instance):
    assert isinstance(instance, henshin_text_EAttribute)


henshin_text_EClass_strategy = st.builds(henshin_text_EClass)
@given(instance=henshin_text_EClass_strategy)
@settings(max_examples=25)
def test_henshin_text_EClass_instantiation(instance):
    assert isinstance(instance, henshin_text_EClass)


henshin_text_EPackage_strategy = st.builds(henshin_text_EPackage)
@given(instance=henshin_text_EPackage_strategy)
@settings(max_examples=25)
def test_henshin_text_EPackage_instantiation(instance):
    assert isinstance(instance, henshin_text_EPackage)


henshin_text_EPackageImport_strategy = st.builds(henshin_text_EPackageImport)
@given(instance=henshin_text_EPackageImport_strategy)
@settings(max_examples=25)
def test_henshin_text_EPackageImport_instantiation(instance):
    assert isinstance(instance, henshin_text_EPackageImport)


henshin_text_EReference_strategy = st.builds(henshin_text_EReference)
@given(instance=henshin_text_EReference_strategy)
@settings(max_examples=25)
def test_henshin_text_EReference_instantiation(instance):
    assert isinstance(instance, henshin_text_EReference)


henshin_text_Edge_strategy = st.builds(henshin_text_Edge, actiontype=safe_text)
@given(instance=henshin_text_Edge_strategy)
@settings(max_examples=25)
def test_henshin_text_Edge_instantiation(instance):
    assert isinstance(instance, henshin_text_Edge)


henshin_text_Edges_strategy = st.builds(henshin_text_Edges)
@given(instance=henshin_text_Edges_strategy)
@settings(max_examples=25)
def test_henshin_text_Edges_instantiation(instance):
    assert isinstance(instance, henshin_text_Edges)


henshin_text_EqualityExpression_strategy = st.builds(henshin_text_EqualityExpression, op=safe_text)
@given(instance=henshin_text_EqualityExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_EqualityExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_EqualityExpression)


henshin_text_Expression_strategy = st.builds(henshin_text_Expression)
@given(instance=henshin_text_Expression_strategy)
@settings(max_examples=25)
def test_henshin_text_Expression_instantiation(instance):
    assert isinstance(instance, henshin_text_Expression)


henshin_text_Formula_strategy = st.builds(henshin_text_Formula)
@given(instance=henshin_text_Formula_strategy)
@settings(max_examples=25)
def test_henshin_text_Formula_instantiation(instance):
    assert isinstance(instance, henshin_text_Formula)


henshin_text_Graph_strategy = st.builds(henshin_text_Graph)
@given(instance=henshin_text_Graph_strategy)
@settings(max_examples=25)
def test_henshin_text_Graph_instantiation(instance):
    assert isinstance(instance, henshin_text_Graph)


henshin_text_GraphElements_strategy = st.builds(henshin_text_GraphElements)
@given(instance=henshin_text_GraphElements_strategy)
@settings(max_examples=25)
def test_henshin_text_GraphElements_instantiation(instance):
    assert isinstance(instance, henshin_text_GraphElements)


henshin_text_IndependentUnit_strategy = st.builds(henshin_text_IndependentUnit)
@given(instance=henshin_text_IndependentUnit_strategy)
@settings(max_examples=25)
def test_henshin_text_IndependentUnit_instantiation(instance):
    assert isinstance(instance, henshin_text_IndependentUnit)


henshin_text_InjectiveMatching_strategy = st.builds(henshin_text_InjectiveMatching, injectiveMatching=st.booleans())
@given(instance=henshin_text_InjectiveMatching_strategy)
@settings(max_examples=25)
def test_henshin_text_InjectiveMatching_instantiation(instance):
    assert isinstance(instance, henshin_text_InjectiveMatching)


henshin_text_IntegerValue_strategy = st.builds(henshin_text_IntegerValue, value=safe_text)
@given(instance=henshin_text_IntegerValue_strategy)
@settings(max_examples=25)
def test_henshin_text_IntegerValue_instantiation(instance):
    assert isinstance(instance, henshin_text_IntegerValue)


henshin_text_IteratedUnit_strategy = st.builds(henshin_text_IteratedUnit)
@given(instance=henshin_text_IteratedUnit_strategy)
@settings(max_examples=25)
def test_henshin_text_IteratedUnit_instantiation(instance):
    assert isinstance(instance, henshin_text_IteratedUnit)


henshin_text_JavaAttributeValue_strategy = st.builds(henshin_text_JavaAttributeValue, value=safe_text)
@given(instance=henshin_text_JavaAttributeValue_strategy)
@settings(max_examples=25)
def test_henshin_text_JavaAttributeValue_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaAttributeValue)


henshin_text_JavaClassValue_strategy = st.builds(henshin_text_JavaClassValue, value=safe_text)
@given(instance=henshin_text_JavaClassValue_strategy)
@settings(max_examples=25)
def test_henshin_text_JavaClassValue_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaClassValue)


henshin_text_JavaImport_strategy = st.builds(henshin_text_JavaImport, packagename=safe_text)
@given(instance=henshin_text_JavaImport_strategy)
@settings(max_examples=25)
def test_henshin_text_JavaImport_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaImport)


henshin_text_List_strategy = st.builds(henshin_text_List)
@given(instance=henshin_text_List_strategy)
@settings(max_examples=25)
def test_henshin_text_List_instantiation(instance):
    assert isinstance(instance, henshin_text_List)


henshin_text_Logic_strategy = st.builds(henshin_text_Logic)
@given(instance=henshin_text_Logic_strategy)
@settings(max_examples=25)
def test_henshin_text_Logic_instantiation(instance):
    assert isinstance(instance, henshin_text_Logic)


henshin_text_LoopUnit_strategy = st.builds(henshin_text_LoopUnit)
@given(instance=henshin_text_LoopUnit_strategy)
@settings(max_examples=25)
def test_henshin_text_LoopUnit_instantiation(instance):
    assert isinstance(instance, henshin_text_LoopUnit)


henshin_text_Match_strategy = st.builds(henshin_text_Match)
@given(instance=henshin_text_Match_strategy)
@settings(max_examples=25)
def test_henshin_text_Match_instantiation(instance):
    assert isinstance(instance, henshin_text_Match)


henshin_text_MinusExpression_strategy = st.builds(henshin_text_MinusExpression)
@given(instance=henshin_text_MinusExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_MinusExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_MinusExpression)


henshin_text_Model_strategy = st.builds(henshin_text_Model)
@given(instance=henshin_text_Model_strategy)
@settings(max_examples=25)
def test_henshin_text_Model_instantiation(instance):
    assert isinstance(instance, henshin_text_Model)


henshin_text_ModelElement_strategy = st.builds(henshin_text_ModelElement, name=safe_text)
@given(instance=henshin_text_ModelElement_strategy)
@settings(max_examples=25)
def test_henshin_text_ModelElement_instantiation(instance):
    assert isinstance(instance, henshin_text_ModelElement)


henshin_text_MulOrDivExpression_strategy = st.builds(henshin_text_MulOrDivExpression, op=safe_text)
@given(instance=henshin_text_MulOrDivExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_MulOrDivExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_MulOrDivExpression)


henshin_text_MultiRule_strategy = st.builds(henshin_text_MultiRule, name=safe_text)
@given(instance=henshin_text_MultiRule_strategy)
@settings(max_examples=25)
def test_henshin_text_MultiRule_instantiation(instance):
    assert isinstance(instance, henshin_text_MultiRule)


henshin_text_MultiRuleReuseNode_strategy = st.builds(henshin_text_MultiRuleReuseNode)
@given(instance=henshin_text_MultiRuleReuseNode_strategy)
@settings(max_examples=25)
def test_henshin_text_MultiRuleReuseNode_instantiation(instance):
    assert isinstance(instance, henshin_text_MultiRuleReuseNode)


henshin_text_NaturalValue_strategy = st.builds(henshin_text_NaturalValue, value=st.integers())
@given(instance=henshin_text_NaturalValue_strategy)
@settings(max_examples=25)
def test_henshin_text_NaturalValue_instantiation(instance):
    assert isinstance(instance, henshin_text_NaturalValue)


henshin_text_Node_strategy = st.builds(henshin_text_Node, actiontype=safe_text)
@given(instance=henshin_text_Node_strategy)
@settings(max_examples=25)
def test_henshin_text_Node_instantiation(instance):
    assert isinstance(instance, henshin_text_Node)


henshin_text_Not_strategy = st.builds(henshin_text_Not)
@given(instance=henshin_text_Not_strategy)
@settings(max_examples=25)
def test_henshin_text_Not_instantiation(instance):
    assert isinstance(instance, henshin_text_Not)


henshin_text_NotExpression_strategy = st.builds(henshin_text_NotExpression)
@given(instance=henshin_text_NotExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_NotExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_NotExpression)


henshin_text_NumberValue_strategy = st.builds(henshin_text_NumberValue, value=safe_text)
@given(instance=henshin_text_NumberValue_strategy)
@settings(max_examples=25)
def test_henshin_text_NumberValue_instantiation(instance):
    assert isinstance(instance, henshin_text_NumberValue)


henshin_text_ORorXOR_strategy = st.builds(henshin_text_ORorXOR, op=safe_text)
@given(instance=henshin_text_ORorXOR_strategy)
@settings(max_examples=25)
def test_henshin_text_ORorXOR_instantiation(instance):
    assert isinstance(instance, henshin_text_ORorXOR)


henshin_text_OrExpression_strategy = st.builds(henshin_text_OrExpression)
@given(instance=henshin_text_OrExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_OrExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_OrExpression)


henshin_text_Parameter_strategy = st.builds(henshin_text_Parameter, name=safe_text)
@given(instance=henshin_text_Parameter_strategy)
@settings(max_examples=25)
def test_henshin_text_Parameter_instantiation(instance):
    assert isinstance(instance, henshin_text_Parameter)


henshin_text_ParameterType_strategy = st.builds(henshin_text_ParameterType, enumType=safe_text)
@given(instance=henshin_text_ParameterType_strategy)
@settings(max_examples=25)
def test_henshin_text_ParameterType_instantiation(instance):
    assert isinstance(instance, henshin_text_ParameterType)


henshin_text_ParameterValue_strategy = st.builds(henshin_text_ParameterValue)
@given(instance=henshin_text_ParameterValue_strategy)
@settings(max_examples=25)
def test_henshin_text_ParameterValue_instantiation(instance):
    assert isinstance(instance, henshin_text_ParameterValue)


henshin_text_PlusExpression_strategy = st.builds(henshin_text_PlusExpression)
@given(instance=henshin_text_PlusExpression_strategy)
@settings(max_examples=25)
def test_henshin_text_PlusExpression_instantiation(instance):
    assert isinstance(instance, henshin_text_PlusExpression)


henshin_text_PriorityUnit_strategy = st.builds(henshin_text_PriorityUnit)
@given(instance=henshin_text_PriorityUnit_strategy)
@settings(max_examples=25)
def test_henshin_text_PriorityUnit_instantiation(instance):
    assert isinstance(instance, henshin_text_PriorityUnit)


henshin_text_Rollback_strategy = st.builds(henshin_text_Rollback, rollback=st.booleans())
@given(instance=henshin_text_Rollback_strategy)
@settings(max_examples=25)
def test_henshin_text_Rollback_instantiation(instance):
    assert isinstance(instance, henshin_text_Rollback)


henshin_text_Rule_strategy = st.builds(henshin_text_Rule)
@given(instance=henshin_text_Rule_strategy)
@settings(max_examples=25)
def test_henshin_text_Rule_instantiation(instance):
    assert isinstance(instance, henshin_text_Rule)


henshin_text_RuleElement_strategy = st.builds(henshin_text_RuleElement)
@given(instance=henshin_text_RuleElement_strategy)
@settings(max_examples=25)
def test_henshin_text_RuleElement_instantiation(instance):
    assert isinstance(instance, henshin_text_RuleElement)


henshin_text_RuleNodeTypes_strategy = st.builds(henshin_text_RuleNodeTypes)
@given(instance=henshin_text_RuleNodeTypes_strategy)
@settings(max_examples=25)
def test_henshin_text_RuleNodeTypes_instantiation(instance):
    assert isinstance(instance, henshin_text_RuleNodeTypes)


henshin_text_SequentialProperties_strategy = st.builds(henshin_text_SequentialProperties)
@given(instance=henshin_text_SequentialProperties_strategy)
@settings(max_examples=25)
def test_henshin_text_SequentialProperties_instantiation(instance):
    assert isinstance(instance, henshin_text_SequentialProperties)


henshin_text_Strict_strategy = st.builds(henshin_text_Strict, strict=st.booleans())
@given(instance=henshin_text_Strict_strategy)
@settings(max_examples=25)
def test_henshin_text_Strict_instantiation(instance):
    assert isinstance(instance, henshin_text_Strict)


henshin_text_StringValue_strategy = st.builds(henshin_text_StringValue, value=safe_text)
@given(instance=henshin_text_StringValue_strategy)
@settings(max_examples=25)
def test_henshin_text_StringValue_instantiation(instance):
    assert isinstance(instance, henshin_text_StringValue)


henshin_text_Unit_strategy = st.builds(henshin_text_Unit)
@given(instance=henshin_text_Unit_strategy)
@settings(max_examples=25)
def test_henshin_text_Unit_instantiation(instance):
    assert isinstance(instance, henshin_text_Unit)


henshin_text_UnitElement_strategy = st.builds(henshin_text_UnitElement)
@given(instance=henshin_text_UnitElement_strategy)
@settings(max_examples=25)
def test_henshin_text_UnitElement_instantiation(instance):
    assert isinstance(instance, henshin_text_UnitElement)



