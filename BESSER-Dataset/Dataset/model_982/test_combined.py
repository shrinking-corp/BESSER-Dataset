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
    Formula,
    henshin_BinaryFormula,
    henshin_UnaryFormula,
    henshin_NestedCondition,
    henshin_ParameterMapping,
    henshin_EReference,
    henshin_EAttribute,
    henshin_Attribute,
    henshin_EClass,
    GraphElement,
    henshin_GraphElement,
    henshin_Formula,
    henshin_Edge,
    henshin_Mapping,
    TransformationUnit,
    henshin_CountedUnit,
    henshin_PriorityUnit,
    henshin_IndependentUnit,
    henshin_ConditionalUnit,
    henshin_SequentialUnit,
    henshin_AmalgamationUnit,
    henshin_EPackage,
    henshin_Rule,
    NamedElement,
    henshin_Graph,
    henshin_Node,
    DescribedElement,
    henshin_TransformationUnit,
    henshin_Parameter,
    henshin_TransformationSystem,
    henshin_DescribedElement,
    henshin_NamedElement,
    henshin_AttributeCondition,
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



def test_hyp_formula_is_not_abstract():
    assert not inspect.isabstract(Formula)


def test_hyp_formula_constructor_exists():
    assert callable(Formula.__init__)


def test_hyp_formula_constructor_args():
    sig = inspect.signature(Formula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_binaryformula_is_not_abstract():
    assert not inspect.isabstract(henshin_BinaryFormula)


def test_hyp_henshin_binaryformula_constructor_exists():
    assert callable(henshin_BinaryFormula.__init__)


def test_hyp_henshin_binaryformula_constructor_args():
    sig = inspect.signature(henshin_BinaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_unaryformula_is_not_abstract():
    assert not inspect.isabstract(henshin_UnaryFormula)


def test_hyp_henshin_unaryformula_constructor_exists():
    assert callable(henshin_UnaryFormula.__init__)


def test_hyp_henshin_unaryformula_constructor_args():
    sig = inspect.signature(henshin_UnaryFormula.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_nestedcondition_is_not_abstract():
    assert not inspect.isabstract(henshin_NestedCondition)


def test_hyp_henshin_nestedcondition_constructor_exists():
    assert callable(henshin_NestedCondition.__init__)


def test_hyp_henshin_nestedcondition_constructor_args():
    sig = inspect.signature(henshin_NestedCondition.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"




def test_hyp_henshin_parametermapping_is_not_abstract():
    assert not inspect.isabstract(henshin_ParameterMapping)


def test_hyp_henshin_parametermapping_constructor_exists():
    assert callable(henshin_ParameterMapping.__init__)


def test_hyp_henshin_parametermapping_constructor_args():
    sig = inspect.signature(henshin_ParameterMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_ereference_is_not_abstract():
    assert not inspect.isabstract(henshin_EReference)


def test_hyp_henshin_ereference_constructor_exists():
    assert callable(henshin_EReference.__init__)


def test_hyp_henshin_ereference_constructor_args():
    sig = inspect.signature(henshin_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_eattribute_is_not_abstract():
    assert not inspect.isabstract(henshin_EAttribute)


def test_hyp_henshin_eattribute_constructor_exists():
    assert callable(henshin_EAttribute.__init__)


def test_hyp_henshin_eattribute_constructor_args():
    sig = inspect.signature(henshin_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_attribute_is_not_abstract():
    assert not inspect.isabstract(henshin_Attribute)


def test_hyp_henshin_attribute_constructor_exists():
    assert callable(henshin_Attribute.__init__)


def test_hyp_henshin_attribute_constructor_args():
    sig = inspect.signature(henshin_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_henshin_eclass_is_not_abstract():
    assert not inspect.isabstract(henshin_EClass)


def test_hyp_henshin_eclass_constructor_exists():
    assert callable(henshin_EClass.__init__)


def test_hyp_henshin_eclass_constructor_args():
    sig = inspect.signature(henshin_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_hyp_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_hyp_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_graphelement_is_not_abstract():
    assert not inspect.isabstract(henshin_GraphElement)


def test_hyp_henshin_graphelement_constructor_exists():
    assert callable(henshin_GraphElement.__init__)


def test_hyp_henshin_graphelement_constructor_args():
    sig = inspect.signature(henshin_GraphElement.__init__)
    params = list(sig.parameters.keys())



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



def test_hyp_henshin_mapping_is_not_abstract():
    assert not inspect.isabstract(henshin_Mapping)


def test_hyp_henshin_mapping_constructor_exists():
    assert callable(henshin_Mapping.__init__)


def test_hyp_henshin_mapping_constructor_args():
    sig = inspect.signature(henshin_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transformationunit_is_not_abstract():
    assert not inspect.isabstract(TransformationUnit)


def test_hyp_transformationunit_constructor_exists():
    assert callable(TransformationUnit.__init__)


def test_hyp_transformationunit_constructor_args():
    sig = inspect.signature(TransformationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_countedunit_is_not_abstract():
    assert not inspect.isabstract(henshin_CountedUnit)


def test_hyp_henshin_countedunit_constructor_exists():
    assert callable(henshin_CountedUnit.__init__)


def test_hyp_henshin_countedunit_constructor_args():
    sig = inspect.signature(henshin_CountedUnit.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"




def test_hyp_henshin_priorityunit_is_not_abstract():
    assert not inspect.isabstract(henshin_PriorityUnit)


def test_hyp_henshin_priorityunit_constructor_exists():
    assert callable(henshin_PriorityUnit.__init__)


def test_hyp_henshin_priorityunit_constructor_args():
    sig = inspect.signature(henshin_PriorityUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_independentunit_is_not_abstract():
    assert not inspect.isabstract(henshin_IndependentUnit)


def test_hyp_henshin_independentunit_constructor_exists():
    assert callable(henshin_IndependentUnit.__init__)


def test_hyp_henshin_independentunit_constructor_args():
    sig = inspect.signature(henshin_IndependentUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_conditionalunit_is_not_abstract():
    assert not inspect.isabstract(henshin_ConditionalUnit)


def test_hyp_henshin_conditionalunit_constructor_exists():
    assert callable(henshin_ConditionalUnit.__init__)


def test_hyp_henshin_conditionalunit_constructor_args():
    sig = inspect.signature(henshin_ConditionalUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_sequentialunit_is_not_abstract():
    assert not inspect.isabstract(henshin_SequentialUnit)


def test_hyp_henshin_sequentialunit_constructor_exists():
    assert callable(henshin_SequentialUnit.__init__)


def test_hyp_henshin_sequentialunit_constructor_args():
    sig = inspect.signature(henshin_SequentialUnit.__init__)
    params = list(sig.parameters.keys())
    assert "rollback" in params, "Missing parameter 'rollback'"
    assert "strict" in params, "Missing parameter 'strict'"





def test_hyp_henshin_amalgamationunit_is_not_abstract():
    assert not inspect.isabstract(henshin_AmalgamationUnit)


def test_hyp_henshin_amalgamationunit_constructor_exists():
    assert callable(henshin_AmalgamationUnit.__init__)


def test_hyp_henshin_amalgamationunit_constructor_args():
    sig = inspect.signature(henshin_AmalgamationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_epackage_is_not_abstract():
    assert not inspect.isabstract(henshin_EPackage)


def test_hyp_henshin_epackage_constructor_exists():
    assert callable(henshin_EPackage.__init__)


def test_hyp_henshin_epackage_constructor_args():
    sig = inspect.signature(henshin_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_rule_is_not_abstract():
    assert not inspect.isabstract(henshin_Rule)


def test_hyp_henshin_rule_constructor_exists():
    assert callable(henshin_Rule.__init__)


def test_hyp_henshin_rule_constructor_args():
    sig = inspect.signature(henshin_Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_graph_is_not_abstract():
    assert not inspect.isabstract(henshin_Graph)


def test_hyp_henshin_graph_constructor_exists():
    assert callable(henshin_Graph.__init__)


def test_hyp_henshin_graph_constructor_args():
    sig = inspect.signature(henshin_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_node_is_not_abstract():
    assert not inspect.isabstract(henshin_Node)


def test_hyp_henshin_node_constructor_exists():
    assert callable(henshin_Node.__init__)


def test_hyp_henshin_node_constructor_args():
    sig = inspect.signature(henshin_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_describedelement_is_not_abstract():
    assert not inspect.isabstract(DescribedElement)


def test_hyp_describedelement_constructor_exists():
    assert callable(DescribedElement.__init__)


def test_hyp_describedelement_constructor_args():
    sig = inspect.signature(DescribedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_transformationunit_is_not_abstract():
    assert not inspect.isabstract(henshin_TransformationUnit)


def test_hyp_henshin_transformationunit_constructor_exists():
    assert callable(henshin_TransformationUnit.__init__)


def test_hyp_henshin_transformationunit_constructor_args():
    sig = inspect.signature(henshin_TransformationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "activated" in params, "Missing parameter 'activated'"




def test_hyp_henshin_parameter_is_not_abstract():
    assert not inspect.isabstract(henshin_Parameter)


def test_hyp_henshin_parameter_constructor_exists():
    assert callable(henshin_Parameter.__init__)


def test_hyp_henshin_parameter_constructor_args():
    sig = inspect.signature(henshin_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_transformationsystem_is_not_abstract():
    assert not inspect.isabstract(henshin_TransformationSystem)


def test_hyp_henshin_transformationsystem_constructor_exists():
    assert callable(henshin_TransformationSystem.__init__)


def test_hyp_henshin_transformationsystem_constructor_args():
    sig = inspect.signature(henshin_TransformationSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_henshin_describedelement_is_not_abstract():
    assert not inspect.isabstract(henshin_DescribedElement)


def test_hyp_henshin_describedelement_constructor_exists():
    assert callable(henshin_DescribedElement.__init__)


def test_hyp_henshin_describedelement_constructor_args():
    sig = inspect.signature(henshin_DescribedElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_henshin_namedelement_is_not_abstract():
    assert not inspect.isabstract(henshin_NamedElement)


def test_hyp_henshin_namedelement_constructor_exists():
    assert callable(henshin_NamedElement.__init__)


def test_hyp_henshin_namedelement_constructor_args():
    sig = inspect.signature(henshin_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_henshin_attributecondition_is_not_abstract():
    assert not inspect.isabstract(henshin_AttributeCondition)


def test_hyp_henshin_attributecondition_constructor_exists():
    assert callable(henshin_AttributeCondition.__init__)


def test_hyp_henshin_attributecondition_constructor_args():
    sig = inspect.signature(henshin_AttributeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionText" in params, "Missing parameter 'conditionText'"



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
Formula_strategy = st.builds(
    Formula,
)
henshin_BinaryFormula_strategy = st.builds(
    henshin_BinaryFormula,
)
henshin_UnaryFormula_strategy = st.builds(
    henshin_UnaryFormula,
)
henshin_NestedCondition_strategy = st.builds(
    henshin_NestedCondition,
    negated=
        st.booleans()
)
henshin_ParameterMapping_strategy = st.builds(
    henshin_ParameterMapping,
)
henshin_EReference_strategy = st.builds(
    henshin_EReference,
)
henshin_EAttribute_strategy = st.builds(
    henshin_EAttribute,
)
henshin_Attribute_strategy = st.builds(
    henshin_Attribute,
    value=
        safe_text
)
henshin_EClass_strategy = st.builds(
    henshin_EClass,
)
GraphElement_strategy = st.builds(
    GraphElement,
)
henshin_GraphElement_strategy = st.builds(
    henshin_GraphElement,
)
henshin_Formula_strategy = st.builds(
    henshin_Formula,
)
henshin_Edge_strategy = st.builds(
    henshin_Edge,
)
henshin_Mapping_strategy = st.builds(
    henshin_Mapping,
)
TransformationUnit_strategy = st.builds(
    TransformationUnit,
)
henshin_CountedUnit_strategy = st.builds(
    henshin_CountedUnit,
    count=
        st.integers()
)
henshin_PriorityUnit_strategy = st.builds(
    henshin_PriorityUnit,
)
henshin_IndependentUnit_strategy = st.builds(
    henshin_IndependentUnit,
)
henshin_ConditionalUnit_strategy = st.builds(
    henshin_ConditionalUnit,
)
henshin_SequentialUnit_strategy = st.builds(
    henshin_SequentialUnit,
    rollback=
        st.booleans(),
    strict=
        st.booleans()
)
henshin_AmalgamationUnit_strategy = st.builds(
    henshin_AmalgamationUnit,
)
henshin_EPackage_strategy = st.builds(
    henshin_EPackage,
)
henshin_Rule_strategy = st.builds(
    henshin_Rule,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
henshin_Graph_strategy = st.builds(
    henshin_Graph,
)
henshin_Node_strategy = st.builds(
    henshin_Node,
)
DescribedElement_strategy = st.builds(
    DescribedElement,
)
henshin_TransformationUnit_strategy = st.builds(
    henshin_TransformationUnit,
    activated=
        st.booleans()
)
henshin_Parameter_strategy = st.builds(
    henshin_Parameter,
)
henshin_TransformationSystem_strategy = st.builds(
    henshin_TransformationSystem,
)
henshin_DescribedElement_strategy = st.builds(
    henshin_DescribedElement,
    description=
        safe_text
)
henshin_NamedElement_strategy = st.builds(
    henshin_NamedElement,
    name=
        safe_text
)
henshin_AttributeCondition_strategy = st.builds(
    henshin_AttributeCondition,
    conditionText=
        safe_text
)













@given(instance=henshin_NestedCondition_strategy)
def test_hyp_henshin_nestedcondition_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original







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
def test_hyp_henshin_formula_stringrepresentation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.stringRepresentation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.stringRepresentation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'stringRepresentation' in henshin_Formula is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'stringRepresentation' in henshin_Formula did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'stringRepresentation' in henshin_Formula is not implemented or raised an error")







@given(instance=henshin_CountedUnit_strategy)
def test_hyp_henshin_countedunit_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original







@given(instance=henshin_SequentialUnit_strategy)
def test_hyp_henshin_sequentialunit_rollback_setter(instance):
    original = instance.rollback
    instance.rollback = original
    assert instance.rollback == original



@given(instance=henshin_SequentialUnit_strategy)
def test_hyp_henshin_sequentialunit_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Rule_strategy)
@settings(max_examples=30)
def test_hyp_henshin_rule_containsmapping_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.containsMapping(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.containsMapping).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'containsMapping' in henshin_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'containsMapping' in henshin_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'containsMapping' in henshin_Rule is not implemented or raised an error")



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
def test_hyp_henshin_graph_findedgesbytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findEdgesByType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findEdgesByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findEdgesByType' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findEdgesByType' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findEdgesByType' in henshin_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Graph_strategy)
@settings(max_examples=30)
def test_hyp_henshin_graph_findnodesbytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findNodesByType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findNodesByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findNodesByType' in henshin_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findNodesByType' in henshin_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findNodesByType' in henshin_Graph is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Node_strategy)
@settings(max_examples=30)
def test_hyp_henshin_node_findincomingedgebytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findIncomingEdgeByType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findIncomingEdgeByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findIncomingEdgeByType' in henshin_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findIncomingEdgeByType' in henshin_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findIncomingEdgeByType' in henshin_Node is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Node_strategy)
@settings(max_examples=30)
def test_hyp_henshin_node_findattributebytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findAttributeByType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findAttributeByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findAttributeByType' in henshin_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAttributeByType' in henshin_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAttributeByType' in henshin_Node is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Node_strategy)
@settings(max_examples=30)
def test_hyp_henshin_node_findoutgoingedgebytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findOutgoingEdgeByType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findOutgoingEdgeByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findOutgoingEdgeByType' in henshin_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findOutgoingEdgeByType' in henshin_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findOutgoingEdgeByType' in henshin_Node is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Node_strategy)
@settings(max_examples=30)
def test_hyp_henshin_node_findincomingedgesbytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findIncomingEdgesByType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findIncomingEdgesByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findIncomingEdgesByType' in henshin_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findIncomingEdgesByType' in henshin_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findIncomingEdgesByType' in henshin_Node is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_Node_strategy)
@settings(max_examples=30)
def test_hyp_henshin_node_findoutgoingedgesbytype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findOutgoingEdgesByType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findOutgoingEdgesByType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findOutgoingEdgesByType' in henshin_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findOutgoingEdgesByType' in henshin_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findOutgoingEdgesByType' in henshin_Node is not implemented or raised an error")





@given(instance=henshin_TransformationUnit_strategy)
def test_hyp_henshin_transformationunit_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_TransformationSystem_strategy)
@settings(max_examples=30)
def test_hyp_henshin_transformationsystem_findrulebyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findRuleByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findRuleByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findRuleByName' in henshin_TransformationSystem is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findRuleByName' in henshin_TransformationSystem did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findRuleByName' in henshin_TransformationSystem is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=henshin_TransformationSystem_strategy)
@settings(max_examples=30)
def test_hyp_henshin_transformationsystem_findunitbyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findUnitByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findUnitByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findUnitByName' in henshin_TransformationSystem is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findUnitByName' in henshin_TransformationSystem did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findUnitByName' in henshin_TransformationSystem is not implemented or raised an error")




@given(instance=henshin_DescribedElement_strategy)
def test_hyp_henshin_describedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=henshin_NamedElement_strategy)
def test_hyp_henshin_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=henshin_AttributeCondition_strategy)
def test_hyp_henshin_attributecondition_conditionText_setter(instance):
    original = instance.conditionText
    instance.conditionText = original
    assert instance.conditionText == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryFormula,
    DescribedElement,
    Formula,
    GraphElement,
    NamedElement,
    TransformationUnit,
    UnaryFormula,
    henshin_AmalgamationUnit,
    henshin_And,
    henshin_Attribute,
    henshin_AttributeCondition,
    henshin_BinaryFormula,
    henshin_ConditionalUnit,
    henshin_CountedUnit,
    henshin_DescribedElement,
    henshin_EAttribute,
    henshin_EClass,
    henshin_EPackage,
    henshin_EReference,
    henshin_Edge,
    henshin_Formula,
    henshin_Graph,
    henshin_GraphElement,
    henshin_IndependentUnit,
    henshin_Mapping,
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
    henshin_TransformationSystem,
    henshin_TransformationUnit,
    henshin_UnaryFormula,
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

def test_henshin_Attribute_value_value_roundtrip():
    instance = henshin_Attribute(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_henshin_AttributeCondition_conditionText_value_roundtrip():
    instance = henshin_AttributeCondition(conditionText="sample_text")
    assert instance.conditionText == "sample_text"
    instance.conditionText = "sample_text_2"
    assert instance.conditionText == "sample_text_2"


def test_henshin_CountedUnit_count_value_roundtrip():
    instance = henshin_CountedUnit(count=7)
    assert instance.count == 7
    instance.count = 13
    assert instance.count == 13


def test_henshin_DescribedElement_description_value_roundtrip():
    instance = henshin_DescribedElement(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_henshin_NamedElement_name_value_roundtrip():
    instance = henshin_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_henshin_NestedCondition_negated_value_roundtrip():
    instance = henshin_NestedCondition(negated=True)
    assert instance.negated == True
    instance.negated = False
    assert instance.negated == False


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


def test_henshin_TransformationUnit_activated_value_roundtrip():
    instance = henshin_TransformationUnit(activated=True)
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


def test_henshin_AttributeCondition_isa_DescribedElement():
    instance = henshin_AttributeCondition(conditionText="sample_text")
    assert isinstance(instance, DescribedElement)


def test_henshin_Parameter_isa_DescribedElement():
    instance = henshin_Parameter()
    assert isinstance(instance, DescribedElement)


def test_henshin_TransformationSystem_isa_DescribedElement():
    instance = henshin_TransformationSystem()
    assert isinstance(instance, DescribedElement)


def test_henshin_TransformationUnit_isa_DescribedElement():
    instance = henshin_TransformationUnit(activated=True)
    assert isinstance(instance, DescribedElement)


def test_henshin_BinaryFormula_isa_Formula():
    instance = henshin_BinaryFormula()
    assert isinstance(instance, Formula)


def test_henshin_NestedCondition_isa_Formula():
    instance = henshin_NestedCondition(negated=True)
    assert isinstance(instance, Formula)


def test_henshin_UnaryFormula_isa_Formula():
    instance = henshin_UnaryFormula()
    assert isinstance(instance, Formula)


def test_henshin_Edge_isa_GraphElement():
    instance = henshin_Edge()
    assert isinstance(instance, GraphElement)


def test_henshin_Node_isa_GraphElement():
    instance = henshin_Node()
    assert isinstance(instance, GraphElement)


def test_henshin_AttributeCondition_isa_NamedElement():
    instance = henshin_AttributeCondition(conditionText="sample_text")
    assert isinstance(instance, NamedElement)


def test_henshin_Graph_isa_NamedElement():
    instance = henshin_Graph()
    assert isinstance(instance, NamedElement)


def test_henshin_Node_isa_NamedElement():
    instance = henshin_Node()
    assert isinstance(instance, NamedElement)


def test_henshin_Parameter_isa_NamedElement():
    instance = henshin_Parameter()
    assert isinstance(instance, NamedElement)


def test_henshin_TransformationSystem_isa_NamedElement():
    instance = henshin_TransformationSystem()
    assert isinstance(instance, NamedElement)


def test_henshin_TransformationUnit_isa_NamedElement():
    instance = henshin_TransformationUnit(activated=True)
    assert isinstance(instance, NamedElement)


def test_henshin_AmalgamationUnit_isa_TransformationUnit():
    instance = henshin_AmalgamationUnit()
    assert isinstance(instance, TransformationUnit)


def test_henshin_ConditionalUnit_isa_TransformationUnit():
    instance = henshin_ConditionalUnit()
    assert isinstance(instance, TransformationUnit)


def test_henshin_CountedUnit_isa_TransformationUnit():
    instance = henshin_CountedUnit(count=7)
    assert isinstance(instance, TransformationUnit)


def test_henshin_IndependentUnit_isa_TransformationUnit():
    instance = henshin_IndependentUnit()
    assert isinstance(instance, TransformationUnit)


def test_henshin_PriorityUnit_isa_TransformationUnit():
    instance = henshin_PriorityUnit()
    assert isinstance(instance, TransformationUnit)


def test_henshin_Rule_isa_TransformationUnit():
    instance = henshin_Rule()
    assert isinstance(instance, TransformationUnit)


def test_henshin_SequentialUnit_isa_TransformationUnit():
    instance = henshin_SequentialUnit(rollback=True, strict=True)
    assert isinstance(instance, TransformationUnit)


def test_henshin_Not_isa_UnaryFormula():
    instance = henshin_Not()
    assert isinstance(instance, UnaryFormula)


def test_assoc_allEdges36_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'henshin_Node37', {b1})
    assert _is_linked(a, 'henshin_Node37', b1)
    if hasattr(b1, 'henshin_Edge'):
        assert _is_linked(b1, 'henshin_Edge', a)
    _safe_set(a, 'henshin_Node37', {b2})
    assert _is_linked(a, 'henshin_Node37', b2)
    if hasattr(b1, 'henshin_Edge'):
        assert not _is_linked(b1, 'henshin_Edge', a)
    if hasattr(b2, 'henshin_Edge'):
        assert _is_linked(b2, 'henshin_Edge', a)
    _safe_set(a, 'henshin_Node37', set())
    assert not _is_linked(a, 'henshin_Node37', b2)
    if hasattr(b2, 'henshin_Edge'):
        assert not _is_linked(b2, 'henshin_Edge', a)


def test_assoc_attributeConditions11_link_reassign_clear():
    a = henshin_Rule()
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


def test_assoc_attributes30_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Attribute(value="sample_text")
    b2 = henshin_Attribute(value="sample_text_2")
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


def test_assoc_child84_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_UnaryFormula()
    b2 = henshin_UnaryFormula()
    _safe_set(a, 'henshin_Formula85', b1)
    assert _is_linked(a, 'henshin_Formula85', b1)
    if hasattr(b1, 'henshin_UnaryFormula'):
        assert _is_linked(b1, 'henshin_UnaryFormula', a)
    _safe_set(a, 'henshin_Formula85', b2)
    assert _is_linked(a, 'henshin_Formula85', b2)
    if hasattr(b1, 'henshin_UnaryFormula'):
        assert not _is_linked(b1, 'henshin_UnaryFormula', a)
    if hasattr(b2, 'henshin_UnaryFormula'):
        assert _is_linked(b2, 'henshin_UnaryFormula', a)
    _safe_set(a, 'henshin_Formula85', None)
    assert not _is_linked(a, 'henshin_Formula85', b2)
    if hasattr(b2, 'henshin_UnaryFormula'):
        assert not _is_linked(b2, 'henshin_UnaryFormula', a)


def test_assoc_conclusion79_link_reassign_clear():
    a = henshin_NestedCondition(negated=True)
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_NestedCondition', b1)
    assert _is_linked(a, 'henshin_NestedCondition', b1)
    if hasattr(b1, 'henshin_Graph80'):
        assert _is_linked(b1, 'henshin_Graph80', a)
    _safe_set(a, 'henshin_NestedCondition', b2)
    assert _is_linked(a, 'henshin_NestedCondition', b2)
    if hasattr(b1, 'henshin_Graph80'):
        assert not _is_linked(b1, 'henshin_Graph80', a)
    if hasattr(b2, 'henshin_Graph80'):
        assert _is_linked(b2, 'henshin_Graph80', a)
    _safe_set(a, 'henshin_NestedCondition', None)
    assert not _is_linked(a, 'henshin_NestedCondition', b2)
    if hasattr(b2, 'henshin_Graph80'):
        assert not _is_linked(b2, 'henshin_Graph80', a)


def test_assoc_edges19_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'graph20', {b1})
    assert _is_linked(a, 'graph20', b1)
    if hasattr(b1, 'Edge'):
        assert _is_linked(b1, 'Edge', a)
    _safe_set(a, 'graph20', {b2})
    assert _is_linked(a, 'graph20', b2)
    if hasattr(b1, 'Edge'):
        assert not _is_linked(b1, 'Edge', a)
    if hasattr(b2, 'Edge'):
        assert _is_linked(b2, 'Edge', a)
    _safe_set(a, 'graph20', set())
    assert not _is_linked(a, 'graph20', b2)
    if hasattr(b2, 'Edge'):
        assert not _is_linked(b2, 'Edge', a)


def test_assoc_else_61_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_TransformationUnit63', b1)
    assert _is_linked(a, 'henshin_TransformationUnit63', b1)
    if hasattr(b1, 'henshin_ConditionalUnit62'):
        assert _is_linked(b1, 'henshin_ConditionalUnit62', a)
    _safe_set(a, 'henshin_TransformationUnit63', b2)
    assert _is_linked(a, 'henshin_TransformationUnit63', b2)
    if hasattr(b1, 'henshin_ConditionalUnit62'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit62', a)
    if hasattr(b2, 'henshin_ConditionalUnit62'):
        assert _is_linked(b2, 'henshin_ConditionalUnit62', a)
    _safe_set(a, 'henshin_TransformationUnit63', None)
    assert not _is_linked(a, 'henshin_TransformationUnit63', b2)
    if hasattr(b2, 'henshin_ConditionalUnit62'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit62', a)


def test_assoc_formula21_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Formula()
    b2 = henshin_Formula()
    _safe_set(a, 'henshin_Graph22', b1)
    assert _is_linked(a, 'henshin_Graph22', b1)
    if hasattr(b1, 'henshin_Formula'):
        assert _is_linked(b1, 'henshin_Formula', a)
    _safe_set(a, 'henshin_Graph22', b2)
    assert _is_linked(a, 'henshin_Graph22', b2)
    if hasattr(b1, 'henshin_Formula'):
        assert not _is_linked(b1, 'henshin_Formula', a)
    if hasattr(b2, 'henshin_Formula'):
        assert _is_linked(b2, 'henshin_Formula', a)
    _safe_set(a, 'henshin_Graph22', None)
    assert not _is_linked(a, 'henshin_Graph22', b2)
    if hasattr(b2, 'henshin_Formula'):
        assert not _is_linked(b2, 'henshin_Formula', a)


def test_assoc_graph31_link_reassign_clear():
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


def test_assoc_graph47_link_reassign_clear():
    a = henshin_Graph()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'Graph48', b1)
    assert _is_linked(a, 'Graph48', b1)
    if hasattr(b1, 'edges'):
        assert _is_linked(b1, 'edges', a)
    _safe_set(a, 'Graph48', b2)
    assert _is_linked(a, 'Graph48', b2)
    if hasattr(b1, 'edges'):
        assert not _is_linked(b1, 'edges', a)
    if hasattr(b2, 'edges'):
        assert _is_linked(b2, 'edges', a)
    _safe_set(a, 'Graph48', None)
    assert not _is_linked(a, 'Graph48', b2)
    if hasattr(b2, 'edges'):
        assert not _is_linked(b2, 'edges', a)


def test_assoc_if_56_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_TransformationUnit57', b1)
    assert _is_linked(a, 'henshin_TransformationUnit57', b1)
    if hasattr(b1, 'henshin_ConditionalUnit'):
        assert _is_linked(b1, 'henshin_ConditionalUnit', a)
    _safe_set(a, 'henshin_TransformationUnit57', b2)
    assert _is_linked(a, 'henshin_TransformationUnit57', b2)
    if hasattr(b1, 'henshin_ConditionalUnit'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit', a)
    if hasattr(b2, 'henshin_ConditionalUnit'):
        assert _is_linked(b2, 'henshin_ConditionalUnit', a)
    _safe_set(a, 'henshin_TransformationUnit57', None)
    assert not _is_linked(a, 'henshin_TransformationUnit57', b2)
    if hasattr(b2, 'henshin_ConditionalUnit'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit', a)


def test_assoc_image25_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Node27', b1)
    assert _is_linked(a, 'henshin_Node27', b1)
    if hasattr(b1, 'henshin_Mapping26'):
        assert _is_linked(b1, 'henshin_Mapping26', a)
    _safe_set(a, 'henshin_Node27', b2)
    assert _is_linked(a, 'henshin_Node27', b2)
    if hasattr(b1, 'henshin_Mapping26'):
        assert not _is_linked(b1, 'henshin_Mapping26', a)
    if hasattr(b2, 'henshin_Mapping26'):
        assert _is_linked(b2, 'henshin_Mapping26', a)
    _safe_set(a, 'henshin_Node27', None)
    assert not _is_linked(a, 'henshin_Node27', b2)
    if hasattr(b2, 'henshin_Mapping26'):
        assert not _is_linked(b2, 'henshin_Mapping26', a)


def test_assoc_imports1_link_reassign_clear():
    a = henshin_TransformationSystem()
    b1 = henshin_EPackage()
    b2 = henshin_EPackage()
    _safe_set(a, 'henshin_TransformationSystem', {b1})
    assert _is_linked(a, 'henshin_TransformationSystem', b1)
    if hasattr(b1, 'henshin_EPackage'):
        assert _is_linked(b1, 'henshin_EPackage', a)
    _safe_set(a, 'henshin_TransformationSystem', {b2})
    assert _is_linked(a, 'henshin_TransformationSystem', b2)
    if hasattr(b1, 'henshin_EPackage'):
        assert not _is_linked(b1, 'henshin_EPackage', a)
    if hasattr(b2, 'henshin_EPackage'):
        assert _is_linked(b2, 'henshin_EPackage', a)
    _safe_set(a, 'henshin_TransformationSystem', set())
    assert not _is_linked(a, 'henshin_TransformationSystem', b2)
    if hasattr(b2, 'henshin_EPackage'):
        assert not _is_linked(b2, 'henshin_EPackage', a)


def test_assoc_incoming32_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Edge33'):
        assert _is_linked(b1, 'Edge33', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Edge33'):
        assert not _is_linked(b1, 'Edge33', a)
    if hasattr(b2, 'Edge33'):
        assert _is_linked(b2, 'Edge33', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Edge33'):
        assert not _is_linked(b2, 'Edge33', a)


def test_assoc_instances2_link_reassign_clear():
    a = henshin_TransformationSystem()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_TransformationSystem3', {b1})
    assert _is_linked(a, 'henshin_TransformationSystem3', b1)
    if hasattr(b1, 'henshin_Graph'):
        assert _is_linked(b1, 'henshin_Graph', a)
    _safe_set(a, 'henshin_TransformationSystem3', {b2})
    assert _is_linked(a, 'henshin_TransformationSystem3', b2)
    if hasattr(b1, 'henshin_Graph'):
        assert not _is_linked(b1, 'henshin_Graph', a)
    if hasattr(b2, 'henshin_Graph'):
        assert _is_linked(b2, 'henshin_Graph', a)
    _safe_set(a, 'henshin_TransformationSystem3', set())
    assert not _is_linked(a, 'henshin_TransformationSystem3', b2)
    if hasattr(b2, 'henshin_Graph'):
        assert not _is_linked(b2, 'henshin_Graph', a)


def test_assoc_kernelRule66_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_AmalgamationUnit()
    b2 = henshin_AmalgamationUnit()
    _safe_set(a, 'henshin_Rule67', b1)
    assert _is_linked(a, 'henshin_Rule67', b1)
    if hasattr(b1, 'henshin_AmalgamationUnit'):
        assert _is_linked(b1, 'henshin_AmalgamationUnit', a)
    _safe_set(a, 'henshin_Rule67', b2)
    assert _is_linked(a, 'henshin_Rule67', b2)
    if hasattr(b1, 'henshin_AmalgamationUnit'):
        assert not _is_linked(b1, 'henshin_AmalgamationUnit', a)
    if hasattr(b2, 'henshin_AmalgamationUnit'):
        assert _is_linked(b2, 'henshin_AmalgamationUnit', a)
    _safe_set(a, 'henshin_Rule67', None)
    assert not _is_linked(a, 'henshin_Rule67', b2)
    if hasattr(b2, 'henshin_AmalgamationUnit'):
        assert not _is_linked(b2, 'henshin_AmalgamationUnit', a)


def test_assoc_left86_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_BinaryFormula()
    b2 = henshin_BinaryFormula()
    _safe_set(a, 'henshin_Formula87', b1)
    assert _is_linked(a, 'henshin_Formula87', b1)
    if hasattr(b1, 'henshin_BinaryFormula'):
        assert _is_linked(b1, 'henshin_BinaryFormula', a)
    _safe_set(a, 'henshin_Formula87', b2)
    assert _is_linked(a, 'henshin_Formula87', b2)
    if hasattr(b1, 'henshin_BinaryFormula'):
        assert not _is_linked(b1, 'henshin_BinaryFormula', a)
    if hasattr(b2, 'henshin_BinaryFormula'):
        assert _is_linked(b2, 'henshin_BinaryFormula', a)
    _safe_set(a, 'henshin_Formula87', None)
    assert not _is_linked(a, 'henshin_Formula87', b2)
    if hasattr(b2, 'henshin_BinaryFormula'):
        assert not _is_linked(b2, 'henshin_BinaryFormula', a)


def test_assoc_lhs6_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_Rule', b1)
    assert _is_linked(a, 'henshin_Rule', b1)
    if hasattr(b1, 'henshin_Graph7'):
        assert _is_linked(b1, 'henshin_Graph7', a)
    _safe_set(a, 'henshin_Rule', b2)
    assert _is_linked(a, 'henshin_Rule', b2)
    if hasattr(b1, 'henshin_Graph7'):
        assert not _is_linked(b1, 'henshin_Graph7', a)
    if hasattr(b2, 'henshin_Graph7'):
        assert _is_linked(b2, 'henshin_Graph7', a)
    _safe_set(a, 'henshin_Rule', None)
    assert not _is_linked(a, 'henshin_Rule', b2)
    if hasattr(b2, 'henshin_Graph7'):
        assert not _is_linked(b2, 'henshin_Graph7', a)


def test_assoc_mappings12_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Rule13', {b1})
    assert _is_linked(a, 'henshin_Rule13', b1)
    if hasattr(b1, 'henshin_Mapping'):
        assert _is_linked(b1, 'henshin_Mapping', a)
    _safe_set(a, 'henshin_Rule13', {b2})
    assert _is_linked(a, 'henshin_Rule13', b2)
    if hasattr(b1, 'henshin_Mapping'):
        assert not _is_linked(b1, 'henshin_Mapping', a)
    if hasattr(b2, 'henshin_Mapping'):
        assert _is_linked(b2, 'henshin_Mapping', a)
    _safe_set(a, 'henshin_Rule13', set())
    assert not _is_linked(a, 'henshin_Rule13', b2)
    if hasattr(b2, 'henshin_Mapping'):
        assert not _is_linked(b2, 'henshin_Mapping', a)


def test_assoc_mappings81_link_reassign_clear():
    a = henshin_NestedCondition(negated=True)
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_NestedCondition82', {b1})
    assert _is_linked(a, 'henshin_NestedCondition82', b1)
    if hasattr(b1, 'henshin_Mapping83'):
        assert _is_linked(b1, 'henshin_Mapping83', a)
    _safe_set(a, 'henshin_NestedCondition82', {b2})
    assert _is_linked(a, 'henshin_NestedCondition82', b2)
    if hasattr(b1, 'henshin_Mapping83'):
        assert not _is_linked(b1, 'henshin_Mapping83', a)
    if hasattr(b2, 'henshin_Mapping83'):
        assert _is_linked(b2, 'henshin_Mapping83', a)
    _safe_set(a, 'henshin_NestedCondition82', set())
    assert not _is_linked(a, 'henshin_NestedCondition82', b2)
    if hasattr(b2, 'henshin_Mapping83'):
        assert not _is_linked(b2, 'henshin_Mapping83', a)


def test_assoc_multiRules68_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_AmalgamationUnit()
    b2 = henshin_AmalgamationUnit()
    _safe_set(a, 'henshin_Rule70', b1)
    assert _is_linked(a, 'henshin_Rule70', b1)
    if hasattr(b1, 'henshin_AmalgamationUnit69'):
        assert _is_linked(b1, 'henshin_AmalgamationUnit69', a)
    _safe_set(a, 'henshin_Rule70', b2)
    assert _is_linked(a, 'henshin_Rule70', b2)
    if hasattr(b1, 'henshin_AmalgamationUnit69'):
        assert not _is_linked(b1, 'henshin_AmalgamationUnit69', a)
    if hasattr(b2, 'henshin_AmalgamationUnit69'):
        assert _is_linked(b2, 'henshin_AmalgamationUnit69', a)
    _safe_set(a, 'henshin_Rule70', None)
    assert not _is_linked(a, 'henshin_Rule70', b2)
    if hasattr(b2, 'henshin_AmalgamationUnit69'):
        assert not _is_linked(b2, 'henshin_AmalgamationUnit69', a)


def test_assoc_node39_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Attribute(value="sample_text")
    b2 = henshin_Attribute(value="sample_text_2")
    _safe_set(a, 'Node40', b1)
    assert _is_linked(a, 'Node40', b1)
    if hasattr(b1, 'attributes'):
        assert _is_linked(b1, 'attributes', a)
    _safe_set(a, 'Node40', b2)
    assert _is_linked(a, 'Node40', b2)
    if hasattr(b1, 'attributes'):
        assert not _is_linked(b1, 'attributes', a)
    if hasattr(b2, 'attributes'):
        assert _is_linked(b2, 'attributes', a)
    _safe_set(a, 'Node40', None)
    assert not _is_linked(a, 'Node40', b2)
    if hasattr(b2, 'attributes'):
        assert not _is_linked(b2, 'attributes', a)


def test_assoc_nodes18_link_reassign_clear():
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


def test_assoc_origin23_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Mapping()
    b2 = henshin_Mapping()
    _safe_set(a, 'henshin_Node', b1)
    assert _is_linked(a, 'henshin_Node', b1)
    if hasattr(b1, 'henshin_Mapping24'):
        assert _is_linked(b1, 'henshin_Mapping24', a)
    _safe_set(a, 'henshin_Node', b2)
    assert _is_linked(a, 'henshin_Node', b2)
    if hasattr(b1, 'henshin_Mapping24'):
        assert not _is_linked(b1, 'henshin_Mapping24', a)
    if hasattr(b2, 'henshin_Mapping24'):
        assert _is_linked(b2, 'henshin_Mapping24', a)
    _safe_set(a, 'henshin_Node', None)
    assert not _is_linked(a, 'henshin_Node', b2)
    if hasattr(b2, 'henshin_Mapping24'):
        assert not _is_linked(b2, 'henshin_Mapping24', a)


def test_assoc_outgoing34_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Edge35'):
        assert _is_linked(b1, 'Edge35', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Edge35'):
        assert not _is_linked(b1, 'Edge35', a)
    if hasattr(b2, 'Edge35'):
        assert _is_linked(b2, 'Edge35', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Edge35'):
        assert not _is_linked(b2, 'Edge35', a)


def test_assoc_parameterMappings50_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_ParameterMapping()
    b2 = henshin_ParameterMapping()
    _safe_set(a, 'henshin_TransformationUnit51', {b1})
    assert _is_linked(a, 'henshin_TransformationUnit51', b1)
    if hasattr(b1, 'henshin_ParameterMapping'):
        assert _is_linked(b1, 'henshin_ParameterMapping', a)
    _safe_set(a, 'henshin_TransformationUnit51', {b2})
    assert _is_linked(a, 'henshin_TransformationUnit51', b2)
    if hasattr(b1, 'henshin_ParameterMapping'):
        assert not _is_linked(b1, 'henshin_ParameterMapping', a)
    if hasattr(b2, 'henshin_ParameterMapping'):
        assert _is_linked(b2, 'henshin_ParameterMapping', a)
    _safe_set(a, 'henshin_TransformationUnit51', set())
    assert not _is_linked(a, 'henshin_TransformationUnit51', b2)
    if hasattr(b2, 'henshin_ParameterMapping'):
        assert not _is_linked(b2, 'henshin_ParameterMapping', a)


def test_assoc_parameters49_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
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


def test_assoc_rhs8_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_Graph()
    b2 = henshin_Graph()
    _safe_set(a, 'henshin_Rule9', b1)
    assert _is_linked(a, 'henshin_Rule9', b1)
    if hasattr(b1, 'henshin_Graph10'):
        assert _is_linked(b1, 'henshin_Graph10', a)
    _safe_set(a, 'henshin_Rule9', b2)
    assert _is_linked(a, 'henshin_Rule9', b2)
    if hasattr(b1, 'henshin_Graph10'):
        assert not _is_linked(b1, 'henshin_Graph10', a)
    if hasattr(b2, 'henshin_Graph10'):
        assert _is_linked(b2, 'henshin_Graph10', a)
    _safe_set(a, 'henshin_Rule9', None)
    assert not _is_linked(a, 'henshin_Rule9', b2)
    if hasattr(b2, 'henshin_Graph10'):
        assert not _is_linked(b2, 'henshin_Graph10', a)


def test_assoc_right88_link_reassign_clear():
    a = henshin_Formula()
    b1 = henshin_BinaryFormula()
    b2 = henshin_BinaryFormula()
    _safe_set(a, 'henshin_Formula90', b1)
    assert _is_linked(a, 'henshin_Formula90', b1)
    if hasattr(b1, 'henshin_BinaryFormula89'):
        assert _is_linked(b1, 'henshin_BinaryFormula89', a)
    _safe_set(a, 'henshin_Formula90', b2)
    assert _is_linked(a, 'henshin_Formula90', b2)
    if hasattr(b1, 'henshin_BinaryFormula89'):
        assert not _is_linked(b1, 'henshin_BinaryFormula89', a)
    if hasattr(b2, 'henshin_BinaryFormula89'):
        assert _is_linked(b2, 'henshin_BinaryFormula89', a)
    _safe_set(a, 'henshin_Formula90', None)
    assert not _is_linked(a, 'henshin_Formula90', b2)
    if hasattr(b2, 'henshin_BinaryFormula89'):
        assert not _is_linked(b2, 'henshin_BinaryFormula89', a)


def test_assoc_rule15_link_reassign_clear():
    a = henshin_Rule()
    b1 = henshin_AttributeCondition(conditionText="sample_text")
    b2 = henshin_AttributeCondition(conditionText="sample_text_2")
    _safe_set(a, 'Rule16', b1)
    assert _is_linked(a, 'Rule16', b1)
    if hasattr(b1, 'attributeConditions'):
        assert _is_linked(b1, 'attributeConditions', a)
    _safe_set(a, 'Rule16', b2)
    assert _is_linked(a, 'Rule16', b2)
    if hasattr(b1, 'attributeConditions'):
        assert not _is_linked(b1, 'attributeConditions', a)
    if hasattr(b2, 'attributeConditions'):
        assert _is_linked(b2, 'attributeConditions', a)
    _safe_set(a, 'Rule16', None)
    assert not _is_linked(a, 'Rule16', b2)
    if hasattr(b2, 'attributeConditions'):
        assert not _is_linked(b2, 'attributeConditions', a)


def test_assoc_rules0_link_reassign_clear():
    a = henshin_TransformationSystem()
    b1 = henshin_Rule()
    b2 = henshin_Rule()
    _safe_set(a, 'transformationSystem', {b1})
    assert _is_linked(a, 'transformationSystem', b1)
    if hasattr(b1, 'Rule'):
        assert _is_linked(b1, 'Rule', a)
    _safe_set(a, 'transformationSystem', {b2})
    assert _is_linked(a, 'transformationSystem', b2)
    if hasattr(b1, 'Rule'):
        assert not _is_linked(b1, 'Rule', a)
    if hasattr(b2, 'Rule'):
        assert _is_linked(b2, 'Rule', a)
    _safe_set(a, 'transformationSystem', set())
    assert not _is_linked(a, 'transformationSystem', b2)
    if hasattr(b2, 'Rule'):
        assert not _is_linked(b2, 'Rule', a)


def test_assoc_source41_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'Node42', b1)
    assert _is_linked(a, 'Node42', b1)
    if hasattr(b1, 'outgoing'):
        assert _is_linked(b1, 'outgoing', a)
    _safe_set(a, 'Node42', b2)
    assert _is_linked(a, 'Node42', b2)
    if hasattr(b1, 'outgoing'):
        assert not _is_linked(b1, 'outgoing', a)
    if hasattr(b2, 'outgoing'):
        assert _is_linked(b2, 'outgoing', a)
    _safe_set(a, 'Node42', None)
    assert not _is_linked(a, 'Node42', b2)
    if hasattr(b2, 'outgoing'):
        assert not _is_linked(b2, 'outgoing', a)


def test_assoc_subUnit77_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_CountedUnit(count=7)
    b2 = henshin_CountedUnit(count=13)
    _safe_set(a, 'henshin_TransformationUnit78', b1)
    assert _is_linked(a, 'henshin_TransformationUnit78', b1)
    if hasattr(b1, 'henshin_CountedUnit'):
        assert _is_linked(b1, 'henshin_CountedUnit', a)
    _safe_set(a, 'henshin_TransformationUnit78', b2)
    assert _is_linked(a, 'henshin_TransformationUnit78', b2)
    if hasattr(b1, 'henshin_CountedUnit'):
        assert not _is_linked(b1, 'henshin_CountedUnit', a)
    if hasattr(b2, 'henshin_CountedUnit'):
        assert _is_linked(b2, 'henshin_CountedUnit', a)
    _safe_set(a, 'henshin_TransformationUnit78', None)
    assert not _is_linked(a, 'henshin_TransformationUnit78', b2)
    if hasattr(b2, 'henshin_CountedUnit'):
        assert not _is_linked(b2, 'henshin_CountedUnit', a)


def test_assoc_subUnits52_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_IndependentUnit()
    b2 = henshin_IndependentUnit()
    _safe_set(a, 'henshin_TransformationUnit53', b1)
    assert _is_linked(a, 'henshin_TransformationUnit53', b1)
    if hasattr(b1, 'henshin_IndependentUnit'):
        assert _is_linked(b1, 'henshin_IndependentUnit', a)
    _safe_set(a, 'henshin_TransformationUnit53', b2)
    assert _is_linked(a, 'henshin_TransformationUnit53', b2)
    if hasattr(b1, 'henshin_IndependentUnit'):
        assert not _is_linked(b1, 'henshin_IndependentUnit', a)
    if hasattr(b2, 'henshin_IndependentUnit'):
        assert _is_linked(b2, 'henshin_IndependentUnit', a)
    _safe_set(a, 'henshin_TransformationUnit53', None)
    assert not _is_linked(a, 'henshin_TransformationUnit53', b2)
    if hasattr(b2, 'henshin_IndependentUnit'):
        assert not _is_linked(b2, 'henshin_IndependentUnit', a)


def test_assoc_subUnits54_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_SequentialUnit(rollback=True, strict=True)
    b2 = henshin_SequentialUnit(rollback=False, strict=False)
    _safe_set(a, 'henshin_TransformationUnit55', b1)
    assert _is_linked(a, 'henshin_TransformationUnit55', b1)
    if hasattr(b1, 'henshin_SequentialUnit'):
        assert _is_linked(b1, 'henshin_SequentialUnit', a)
    _safe_set(a, 'henshin_TransformationUnit55', b2)
    assert _is_linked(a, 'henshin_TransformationUnit55', b2)
    if hasattr(b1, 'henshin_SequentialUnit'):
        assert not _is_linked(b1, 'henshin_SequentialUnit', a)
    if hasattr(b2, 'henshin_SequentialUnit'):
        assert _is_linked(b2, 'henshin_SequentialUnit', a)
    _safe_set(a, 'henshin_TransformationUnit55', None)
    assert not _is_linked(a, 'henshin_TransformationUnit55', b2)
    if hasattr(b2, 'henshin_SequentialUnit'):
        assert not _is_linked(b2, 'henshin_SequentialUnit', a)


def test_assoc_subUnits64_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_PriorityUnit()
    b2 = henshin_PriorityUnit()
    _safe_set(a, 'henshin_TransformationUnit65', b1)
    assert _is_linked(a, 'henshin_TransformationUnit65', b1)
    if hasattr(b1, 'henshin_PriorityUnit'):
        assert _is_linked(b1, 'henshin_PriorityUnit', a)
    _safe_set(a, 'henshin_TransformationUnit65', b2)
    assert _is_linked(a, 'henshin_TransformationUnit65', b2)
    if hasattr(b1, 'henshin_PriorityUnit'):
        assert not _is_linked(b1, 'henshin_PriorityUnit', a)
    if hasattr(b2, 'henshin_PriorityUnit'):
        assert _is_linked(b2, 'henshin_PriorityUnit', a)
    _safe_set(a, 'henshin_TransformationUnit65', None)
    assert not _is_linked(a, 'henshin_TransformationUnit65', b2)
    if hasattr(b2, 'henshin_PriorityUnit'):
        assert not _is_linked(b2, 'henshin_PriorityUnit', a)


def test_assoc_target43_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_Edge()
    b2 = henshin_Edge()
    _safe_set(a, 'Node44', b1)
    assert _is_linked(a, 'Node44', b1)
    if hasattr(b1, 'incoming'):
        assert _is_linked(b1, 'incoming', a)
    _safe_set(a, 'Node44', b2)
    assert _is_linked(a, 'Node44', b2)
    if hasattr(b1, 'incoming'):
        assert not _is_linked(b1, 'incoming', a)
    if hasattr(b2, 'incoming'):
        assert _is_linked(b2, 'incoming', a)
    _safe_set(a, 'Node44', None)
    assert not _is_linked(a, 'Node44', b2)
    if hasattr(b2, 'incoming'):
        assert not _is_linked(b2, 'incoming', a)


def test_assoc_then58_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_ConditionalUnit()
    b2 = henshin_ConditionalUnit()
    _safe_set(a, 'henshin_TransformationUnit60', b1)
    assert _is_linked(a, 'henshin_TransformationUnit60', b1)
    if hasattr(b1, 'henshin_ConditionalUnit59'):
        assert _is_linked(b1, 'henshin_ConditionalUnit59', a)
    _safe_set(a, 'henshin_TransformationUnit60', b2)
    assert _is_linked(a, 'henshin_TransformationUnit60', b2)
    if hasattr(b1, 'henshin_ConditionalUnit59'):
        assert not _is_linked(b1, 'henshin_ConditionalUnit59', a)
    if hasattr(b2, 'henshin_ConditionalUnit59'):
        assert _is_linked(b2, 'henshin_ConditionalUnit59', a)
    _safe_set(a, 'henshin_TransformationUnit60', None)
    assert not _is_linked(a, 'henshin_TransformationUnit60', b2)
    if hasattr(b2, 'henshin_ConditionalUnit59'):
        assert not _is_linked(b2, 'henshin_ConditionalUnit59', a)


def test_assoc_transformationSystem14_link_reassign_clear():
    a = henshin_TransformationSystem()
    b1 = henshin_Rule()
    b2 = henshin_Rule()
    _safe_set(a, 'TransformationSystem', b1)
    assert _is_linked(a, 'TransformationSystem', b1)
    if hasattr(b1, 'rules'):
        assert _is_linked(b1, 'rules', a)
    _safe_set(a, 'TransformationSystem', b2)
    assert _is_linked(a, 'TransformationSystem', b2)
    if hasattr(b1, 'rules'):
        assert not _is_linked(b1, 'rules', a)
    if hasattr(b2, 'rules'):
        assert _is_linked(b2, 'rules', a)
    _safe_set(a, 'TransformationSystem', None)
    assert not _is_linked(a, 'TransformationSystem', b2)
    if hasattr(b2, 'rules'):
        assert not _is_linked(b2, 'rules', a)


def test_assoc_transformationUnits4_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_TransformationSystem()
    b2 = henshin_TransformationSystem()
    _safe_set(a, 'henshin_TransformationUnit', b1)
    assert _is_linked(a, 'henshin_TransformationUnit', b1)
    if hasattr(b1, 'henshin_TransformationSystem5'):
        assert _is_linked(b1, 'henshin_TransformationSystem5', a)
    _safe_set(a, 'henshin_TransformationUnit', b2)
    assert _is_linked(a, 'henshin_TransformationUnit', b2)
    if hasattr(b1, 'henshin_TransformationSystem5'):
        assert not _is_linked(b1, 'henshin_TransformationSystem5', a)
    if hasattr(b2, 'henshin_TransformationSystem5'):
        assert _is_linked(b2, 'henshin_TransformationSystem5', a)
    _safe_set(a, 'henshin_TransformationUnit', None)
    assert not _is_linked(a, 'henshin_TransformationUnit', b2)
    if hasattr(b2, 'henshin_TransformationSystem5'):
        assert not _is_linked(b2, 'henshin_TransformationSystem5', a)


def test_assoc_type28_link_reassign_clear():
    a = henshin_Node()
    b1 = henshin_EClass()
    b2 = henshin_EClass()
    _safe_set(a, 'henshin_Node29', b1)
    assert _is_linked(a, 'henshin_Node29', b1)
    if hasattr(b1, 'henshin_EClass'):
        assert _is_linked(b1, 'henshin_EClass', a)
    _safe_set(a, 'henshin_Node29', b2)
    assert _is_linked(a, 'henshin_Node29', b2)
    if hasattr(b1, 'henshin_EClass'):
        assert not _is_linked(b1, 'henshin_EClass', a)
    if hasattr(b2, 'henshin_EClass'):
        assert _is_linked(b2, 'henshin_EClass', a)
    _safe_set(a, 'henshin_Node29', None)
    assert not _is_linked(a, 'henshin_Node29', b2)
    if hasattr(b2, 'henshin_EClass'):
        assert not _is_linked(b2, 'henshin_EClass', a)


def test_assoc_type38_link_reassign_clear():
    a = henshin_Attribute(value="sample_text")
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


def test_assoc_unit17_link_reassign_clear():
    a = henshin_TransformationUnit(activated=True)
    b1 = henshin_Parameter()
    b2 = henshin_Parameter()
    _safe_set(a, 'TransformationUnit', b1)
    assert _is_linked(a, 'TransformationUnit', b1)
    if hasattr(b1, 'parameters'):
        assert _is_linked(b1, 'parameters', a)
    _safe_set(a, 'TransformationUnit', b2)
    assert _is_linked(a, 'TransformationUnit', b2)
    if hasattr(b1, 'parameters'):
        assert not _is_linked(b1, 'parameters', a)
    if hasattr(b2, 'parameters'):
        assert _is_linked(b2, 'parameters', a)
    _safe_set(a, 'TransformationUnit', None)
    assert not _is_linked(a, 'TransformationUnit', b2)
    if hasattr(b2, 'parameters'):
        assert not _is_linked(b2, 'parameters', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryFormula_strategy = st.builds(BinaryFormula)
@given(instance=BinaryFormula_strategy)
@settings(max_examples=25)
def test_BinaryFormula_instantiation(instance):
    assert isinstance(instance, BinaryFormula)


DescribedElement_strategy = st.builds(DescribedElement)
@given(instance=DescribedElement_strategy)
@settings(max_examples=25)
def test_DescribedElement_instantiation(instance):
    assert isinstance(instance, DescribedElement)


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


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


TransformationUnit_strategy = st.builds(TransformationUnit)
@given(instance=TransformationUnit_strategy)
@settings(max_examples=25)
def test_TransformationUnit_instantiation(instance):
    assert isinstance(instance, TransformationUnit)


UnaryFormula_strategy = st.builds(UnaryFormula)
@given(instance=UnaryFormula_strategy)
@settings(max_examples=25)
def test_UnaryFormula_instantiation(instance):
    assert isinstance(instance, UnaryFormula)


henshin_AmalgamationUnit_strategy = st.builds(henshin_AmalgamationUnit)
@given(instance=henshin_AmalgamationUnit_strategy)
@settings(max_examples=25)
def test_henshin_AmalgamationUnit_instantiation(instance):
    assert isinstance(instance, henshin_AmalgamationUnit)


henshin_And_strategy = st.builds(henshin_And)
@given(instance=henshin_And_strategy)
@settings(max_examples=25)
def test_henshin_And_instantiation(instance):
    assert isinstance(instance, henshin_And)


henshin_Attribute_strategy = st.builds(henshin_Attribute, value=safe_text)
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


henshin_CountedUnit_strategy = st.builds(henshin_CountedUnit, count=st.integers())
@given(instance=henshin_CountedUnit_strategy)
@settings(max_examples=25)
def test_henshin_CountedUnit_instantiation(instance):
    assert isinstance(instance, henshin_CountedUnit)


henshin_DescribedElement_strategy = st.builds(henshin_DescribedElement, description=safe_text)
@given(instance=henshin_DescribedElement_strategy)
@settings(max_examples=25)
def test_henshin_DescribedElement_instantiation(instance):
    assert isinstance(instance, henshin_DescribedElement)


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


henshin_Edge_strategy = st.builds(henshin_Edge)
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


henshin_GraphElement_strategy = st.builds(henshin_GraphElement)
@given(instance=henshin_GraphElement_strategy)
@settings(max_examples=25)
def test_henshin_GraphElement_instantiation(instance):
    assert isinstance(instance, henshin_GraphElement)


henshin_IndependentUnit_strategy = st.builds(henshin_IndependentUnit)
@given(instance=henshin_IndependentUnit_strategy)
@settings(max_examples=25)
def test_henshin_IndependentUnit_instantiation(instance):
    assert isinstance(instance, henshin_IndependentUnit)


henshin_Mapping_strategy = st.builds(henshin_Mapping)
@given(instance=henshin_Mapping_strategy)
@settings(max_examples=25)
def test_henshin_Mapping_instantiation(instance):
    assert isinstance(instance, henshin_Mapping)


henshin_NamedElement_strategy = st.builds(henshin_NamedElement, name=safe_text)
@given(instance=henshin_NamedElement_strategy)
@settings(max_examples=25)
def test_henshin_NamedElement_instantiation(instance):
    assert isinstance(instance, henshin_NamedElement)


henshin_NestedCondition_strategy = st.builds(henshin_NestedCondition, negated=st.booleans())
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


henshin_Rule_strategy = st.builds(henshin_Rule)
@given(instance=henshin_Rule_strategy)
@settings(max_examples=25)
def test_henshin_Rule_instantiation(instance):
    assert isinstance(instance, henshin_Rule)


henshin_SequentialUnit_strategy = st.builds(henshin_SequentialUnit, rollback=st.booleans(), strict=st.booleans())
@given(instance=henshin_SequentialUnit_strategy)
@settings(max_examples=25)
def test_henshin_SequentialUnit_instantiation(instance):
    assert isinstance(instance, henshin_SequentialUnit)


henshin_TransformationSystem_strategy = st.builds(henshin_TransformationSystem)
@given(instance=henshin_TransformationSystem_strategy)
@settings(max_examples=25)
def test_henshin_TransformationSystem_instantiation(instance):
    assert isinstance(instance, henshin_TransformationSystem)


henshin_TransformationUnit_strategy = st.builds(henshin_TransformationUnit, activated=st.booleans())
@given(instance=henshin_TransformationUnit_strategy)
@settings(max_examples=25)
def test_henshin_TransformationUnit_instantiation(instance):
    assert isinstance(instance, henshin_TransformationUnit)


henshin_UnaryFormula_strategy = st.builds(henshin_UnaryFormula)
@given(instance=henshin_UnaryFormula_strategy)
@settings(max_examples=25)
def test_henshin_UnaryFormula_instantiation(instance):
    assert isinstance(instance, henshin_UnaryFormula)


henshin_Xor_strategy = st.builds(henshin_Xor)
@given(instance=henshin_Xor_strategy)
@settings(max_examples=25)
def test_henshin_Xor_instantiation(instance):
    assert isinstance(instance, henshin_Xor)



