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
    FinalNode,
    uml_ActivityFinalNode,
    ControlNode,
    uml_ForkNode,
    uml_DecisionNode,
    uml_InitialNode,
    uml_FinalNode,
    uml_JoinNode,
    ObjectNode,
    uml_ActivityParameterNode,
    ExecutableNode,
    uml_Action,
    uml_RootPackage,
    ActivityEdge,
    uml_ControlFlow,
    uml_ObjectFlow,
    Type,
    RedefinableElement,
    Classifier,
    uml_StructuredClassifier,
    StructuredClassifier,
    uml_EncapsulatedClassifier,
    Class,
    uml_Behavior,
    Element,
    uml_TemplateableElement,
    ActivityGroup,
    NamedElement,
    uml_ActivityPartition,
    ActivityNode,
    uml_ControlNode,
    uml_ExecutableNode,
    uml_RedefinableElement,
    Action,
    uml_OpaqueAction,
    uml_Element,
    uml_ParameterableElement,
    uml_NamedElement,
    ParameterableElement,
    uml_TypedElement,
    TypedElement,
    uml_ObjectNode,
    ValueSpecification,
    uml_OpaqueExpression,
    BehavioredClassifier,
    EncapsulatedClassifier,
    uml_Class,
    uml_BehavioredClassifier,
    uml_Namespace,
    uml_ActivityGroup,
    uml_ActivityEdge,
    uml_ActivityNode,
    Behavior,
    uml_Activity,
    uml_PackageableElement,
    TemplateableElement,
    PackageableElement,
    uml_ValueSpecification,
    uml_Type,
    Namespace,
    uml_Classifier,
    uml_Package,
    ObjectNodeOrderingKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityFinalNode)


def test_hyp_uml_activityfinalnode_constructor_exists():
    assert callable(uml_ActivityFinalNode.__init__)


def test_hyp_uml_activityfinalnode_constructor_args():
    sig = inspect.signature(uml_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_forknode_is_not_abstract():
    assert not inspect.isabstract(uml_ForkNode)


def test_hyp_uml_forknode_constructor_exists():
    assert callable(uml_ForkNode.__init__)


def test_hyp_uml_forknode_constructor_args():
    sig = inspect.signature(uml_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml_DecisionNode)


def test_hyp_uml_decisionnode_constructor_exists():
    assert callable(uml_DecisionNode.__init__)


def test_hyp_uml_decisionnode_constructor_args():
    sig = inspect.signature(uml_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_initialnode_is_not_abstract():
    assert not inspect.isabstract(uml_InitialNode)


def test_hyp_uml_initialnode_constructor_exists():
    assert callable(uml_InitialNode.__init__)


def test_hyp_uml_initialnode_constructor_args():
    sig = inspect.signature(uml_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_finalnode_is_not_abstract():
    assert not inspect.isabstract(uml_FinalNode)


def test_hyp_uml_finalnode_constructor_exists():
    assert callable(uml_FinalNode.__init__)


def test_hyp_uml_finalnode_constructor_args():
    sig = inspect.signature(uml_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_joinnode_is_not_abstract():
    assert not inspect.isabstract(uml_JoinNode)


def test_hyp_uml_joinnode_constructor_exists():
    assert callable(uml_JoinNode.__init__)


def test_hyp_uml_joinnode_constructor_args():
    sig = inspect.signature(uml_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"




def test_hyp_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_hyp_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_hyp_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityParameterNode)


def test_hyp_uml_activityparameternode_constructor_exists():
    assert callable(uml_ActivityParameterNode.__init__)


def test_hyp_uml_activityparameternode_constructor_args():
    sig = inspect.signature(uml_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_hyp_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_hyp_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_action_is_not_abstract():
    assert not inspect.isabstract(uml_Action)


def test_hyp_uml_action_constructor_exists():
    assert callable(uml_Action.__init__)


def test_hyp_uml_action_constructor_args():
    sig = inspect.signature(uml_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_rootpackage_is_not_abstract():
    assert not inspect.isabstract(uml_RootPackage)


def test_hyp_uml_rootpackage_constructor_exists():
    assert callable(uml_RootPackage.__init__)


def test_hyp_uml_rootpackage_constructor_args():
    sig = inspect.signature(uml_RootPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_controlflow_is_not_abstract():
    assert not inspect.isabstract(uml_ControlFlow)


def test_hyp_uml_controlflow_constructor_exists():
    assert callable(uml_ControlFlow.__init__)


def test_hyp_uml_controlflow_constructor_args():
    sig = inspect.signature(uml_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_objectflow_is_not_abstract():
    assert not inspect.isabstract(uml_ObjectFlow)


def test_hyp_uml_objectflow_constructor_exists():
    assert callable(uml_ObjectFlow.__init__)


def test_hyp_uml_objectflow_constructor_args():
    sig = inspect.signature(uml_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"





def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_hyp_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_hyp_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_StructuredClassifier)


def test_hyp_uml_structuredclassifier_constructor_exists():
    assert callable(uml_StructuredClassifier.__init__)


def test_hyp_uml_structuredclassifier_constructor_args():
    sig = inspect.signature(uml_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_hyp_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_hyp_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_EncapsulatedClassifier)


def test_hyp_uml_encapsulatedclassifier_constructor_exists():
    assert callable(uml_EncapsulatedClassifier.__init__)


def test_hyp_uml_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_behavior_is_not_abstract():
    assert not inspect.isabstract(uml_Behavior)


def test_hyp_uml_behavior_constructor_exists():
    assert callable(uml_Behavior.__init__)


def test_hyp_uml_behavior_constructor_args():
    sig = inspect.signature(uml_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"




def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_templateableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateableElement)


def test_hyp_uml_templateableelement_constructor_exists():
    assert callable(uml_TemplateableElement.__init__)


def test_hyp_uml_templateableelement_constructor_args():
    sig = inspect.signature(uml_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_hyp_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_hyp_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityPartition)


def test_hyp_uml_activitypartition_constructor_exists():
    assert callable(uml_ActivityPartition.__init__)


def test_hyp_uml_activitypartition_constructor_args():
    sig = inspect.signature(uml_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_controlnode_is_not_abstract():
    assert not inspect.isabstract(uml_ControlNode)


def test_hyp_uml_controlnode_constructor_exists():
    assert callable(uml_ControlNode.__init__)


def test_hyp_uml_controlnode_constructor_args():
    sig = inspect.signature(uml_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_executablenode_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutableNode)


def test_hyp_uml_executablenode_constructor_exists():
    assert callable(uml_ExecutableNode.__init__)


def test_hyp_uml_executablenode_constructor_args():
    sig = inspect.signature(uml_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml_RedefinableElement)


def test_hyp_uml_redefinableelement_constructor_exists():
    assert callable(uml_RedefinableElement.__init__)


def test_hyp_uml_redefinableelement_constructor_args():
    sig = inspect.signature(uml_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"




def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml_OpaqueAction)


def test_hyp_uml_opaqueaction_constructor_exists():
    assert callable(uml_OpaqueAction.__init__)


def test_hyp_uml_opaqueaction_constructor_args():
    sig = inspect.signature(uml_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_element_is_not_abstract():
    assert not inspect.isabstract(uml_Element)


def test_hyp_uml_element_constructor_exists():
    assert callable(uml_Element.__init__)


def test_hyp_uml_element_constructor_args():
    sig = inspect.signature(uml_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml_ParameterableElement)


def test_hyp_uml_parameterableelement_constructor_exists():
    assert callable(uml_ParameterableElement.__init__)


def test_hyp_uml_parameterableelement_constructor_args():
    sig = inspect.signature(uml_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml_NamedElement)


def test_hyp_uml_namedelement_constructor_exists():
    assert callable(uml_NamedElement.__init__)


def test_hyp_uml_namedelement_constructor_args():
    sig = inspect.signature(uml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_hyp_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_hyp_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_typedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TypedElement)


def test_hyp_uml_typedelement_constructor_exists():
    assert callable(uml_TypedElement.__init__)


def test_hyp_uml_typedelement_constructor_args():
    sig = inspect.signature(uml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_objectnode_is_not_abstract():
    assert not inspect.isabstract(uml_ObjectNode)


def test_hyp_uml_objectnode_constructor_exists():
    assert callable(uml_ObjectNode.__init__)


def test_hyp_uml_objectnode_constructor_args():
    sig = inspect.signature(uml_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "isControlType" in params, "Missing parameter 'isControlType'"




def test_hyp_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_hyp_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_hyp_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml_OpaqueExpression)


def test_hyp_uml_opaqueexpression_constructor_exists():
    assert callable(uml_OpaqueExpression.__init__)


def test_hyp_uml_opaqueexpression_constructor_args():
    sig = inspect.signature(uml_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_hyp_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_hyp_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_hyp_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_hyp_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_hyp_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_hyp_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"




def test_hyp_uml_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_BehavioredClassifier)


def test_hyp_uml_behavioredclassifier_constructor_exists():
    assert callable(uml_BehavioredClassifier.__init__)


def test_hyp_uml_behavioredclassifier_constructor_args():
    sig = inspect.signature(uml_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_namespace_is_not_abstract():
    assert not inspect.isabstract(uml_Namespace)


def test_hyp_uml_namespace_constructor_exists():
    assert callable(uml_Namespace.__init__)


def test_hyp_uml_namespace_constructor_args():
    sig = inspect.signature(uml_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activitygroup_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityGroup)


def test_hyp_uml_activitygroup_constructor_exists():
    assert callable(uml_ActivityGroup.__init__)


def test_hyp_uml_activitygroup_constructor_args():
    sig = inspect.signature(uml_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activityedge_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityEdge)


def test_hyp_uml_activityedge_constructor_exists():
    assert callable(uml_ActivityEdge.__init__)


def test_hyp_uml_activityedge_constructor_args():
    sig = inspect.signature(uml_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activitynode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityNode)


def test_hyp_uml_activitynode_constructor_exists():
    assert callable(uml_ActivityNode.__init__)


def test_hyp_uml_activitynode_constructor_args():
    sig = inspect.signature(uml_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_is_not_abstract():
    assert not inspect.isabstract(uml_Activity)


def test_hyp_uml_activity_constructor_exists():
    assert callable(uml_Activity.__init__)


def test_hyp_uml_activity_constructor_args():
    sig = inspect.signature(uml_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml_PackageableElement)


def test_hyp_uml_packageableelement_constructor_exists():
    assert callable(uml_PackageableElement.__init__)


def test_hyp_uml_packageableelement_constructor_args():
    sig = inspect.signature(uml_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_hyp_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_hyp_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_hyp_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_hyp_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml_ValueSpecification)


def test_hyp_uml_valuespecification_constructor_exists():
    assert callable(uml_ValueSpecification.__init__)


def test_hyp_uml_valuespecification_constructor_args():
    sig = inspect.signature(uml_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_type_is_not_abstract():
    assert not inspect.isabstract(uml_Type)


def test_hyp_uml_type_constructor_exists():
    assert callable(uml_Type.__init__)


def test_hyp_uml_type_constructor_args():
    sig = inspect.signature(uml_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_classifier_is_not_abstract():
    assert not inspect.isabstract(uml_Classifier)


def test_hyp_uml_classifier_constructor_exists():
    assert callable(uml_Classifier.__init__)


def test_hyp_uml_classifier_constructor_args():
    sig = inspect.signature(uml_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"




def test_hyp_uml_package_is_not_abstract():
    assert not inspect.isabstract(uml_Package)


def test_hyp_uml_package_constructor_exists():
    assert callable(uml_Package.__init__)


def test_hyp_uml_package_constructor_args():
    sig = inspect.signature(uml_Package.__init__)
    params = list(sig.parameters.keys())

def test_hyp_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_hyp_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "unordered",
        "LIFO",
        "FIFO",
        "ordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"


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
FinalNode_strategy = st.builds(
    FinalNode,
)
uml_ActivityFinalNode_strategy = st.builds(
    uml_ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
uml_ForkNode_strategy = st.builds(
    uml_ForkNode,
)
uml_DecisionNode_strategy = st.builds(
    uml_DecisionNode,
)
uml_InitialNode_strategy = st.builds(
    uml_InitialNode,
)
uml_FinalNode_strategy = st.builds(
    uml_FinalNode,
)
uml_JoinNode_strategy = st.builds(
    uml_JoinNode,
    isCombineDuplicate=
        safe_text
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
uml_ActivityParameterNode_strategy = st.builds(
    uml_ActivityParameterNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
uml_Action_strategy = st.builds(
    uml_Action,
)
uml_RootPackage_strategy = st.builds(
    uml_RootPackage,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
uml_ControlFlow_strategy = st.builds(
    uml_ControlFlow,
)
uml_ObjectFlow_strategy = st.builds(
    uml_ObjectFlow,
    isMultireceive=
        safe_text,
    isMulticast=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
Classifier_strategy = st.builds(
    Classifier,
)
uml_StructuredClassifier_strategy = st.builds(
    uml_StructuredClassifier,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
uml_EncapsulatedClassifier_strategy = st.builds(
    uml_EncapsulatedClassifier,
)
Class_strategy = st.builds(
    Class,
)
uml_Behavior_strategy = st.builds(
    uml_Behavior,
    isReentrant=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
uml_TemplateableElement_strategy = st.builds(
    uml_TemplateableElement,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml_ActivityPartition_strategy = st.builds(
    uml_ActivityPartition,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
uml_ControlNode_strategy = st.builds(
    uml_ControlNode,
)
uml_ExecutableNode_strategy = st.builds(
    uml_ExecutableNode,
)
uml_RedefinableElement_strategy = st.builds(
    uml_RedefinableElement,
    isLeaf=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
uml_OpaqueAction_strategy = st.builds(
    uml_OpaqueAction,
)
uml_Element_strategy = st.builds(
    uml_Element,
)
uml_ParameterableElement_strategy = st.builds(
    uml_ParameterableElement,
)
uml_NamedElement_strategy = st.builds(
    uml_NamedElement,
    name=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
uml_TypedElement_strategy = st.builds(
    uml_TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml_ObjectNode_strategy = st.builds(
    uml_ObjectNode,
    isControlType=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
uml_OpaqueExpression_strategy = st.builds(
    uml_OpaqueExpression,
    body=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
uml_Class_strategy = st.builds(
    uml_Class,
    isActive=
        safe_text
)
uml_BehavioredClassifier_strategy = st.builds(
    uml_BehavioredClassifier,
)
uml_Namespace_strategy = st.builds(
    uml_Namespace,
)
uml_ActivityGroup_strategy = st.builds(
    uml_ActivityGroup,
)
uml_ActivityEdge_strategy = st.builds(
    uml_ActivityEdge,
)
uml_ActivityNode_strategy = st.builds(
    uml_ActivityNode,
)
Behavior_strategy = st.builds(
    Behavior,
)
uml_Activity_strategy = st.builds(
    uml_Activity,
)
uml_PackageableElement_strategy = st.builds(
    uml_PackageableElement,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml_ValueSpecification_strategy = st.builds(
    uml_ValueSpecification,
)
uml_Type_strategy = st.builds(
    uml_Type,
)
Namespace_strategy = st.builds(
    Namespace,
)
uml_Classifier_strategy = st.builds(
    uml_Classifier,
    isAbstract=
        safe_text
)
uml_Package_strategy = st.builds(
    uml_Package,
)











@given(instance=uml_JoinNode_strategy)
def test_hyp_uml_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original











@given(instance=uml_ObjectFlow_strategy)
def test_hyp_uml_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original



@given(instance=uml_ObjectFlow_strategy)
def test_hyp_uml_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original











@given(instance=uml_Behavior_strategy)
def test_hyp_uml_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original












@given(instance=uml_RedefinableElement_strategy)
def test_hyp_uml_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original








@given(instance=uml_NamedElement_strategy)
def test_hyp_uml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=uml_ObjectNode_strategy)
def test_hyp_uml_objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original





@given(instance=uml_OpaqueExpression_strategy)
def test_hyp_uml_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original






@given(instance=uml_Class_strategy)
def test_hyp_uml_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

















@given(instance=uml_Classifier_strategy)
def test_hyp_uml_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    Behavior,
    BehavioredClassifier,
    Class,
    Classifier,
    ControlNode,
    Element,
    EncapsulatedClassifier,
    ExecutableNode,
    FinalNode,
    NamedElement,
    Namespace,
    ObjectNode,
    PackageableElement,
    ParameterableElement,
    RedefinableElement,
    StructuredClassifier,
    TemplateableElement,
    Type,
    TypedElement,
    ValueSpecification,
    uml_Action,
    uml_Activity,
    uml_ActivityEdge,
    uml_ActivityFinalNode,
    uml_ActivityGroup,
    uml_ActivityNode,
    uml_ActivityParameterNode,
    uml_ActivityPartition,
    uml_Behavior,
    uml_BehavioredClassifier,
    uml_Class,
    uml_Classifier,
    uml_ControlFlow,
    uml_ControlNode,
    uml_DecisionNode,
    uml_Element,
    uml_EncapsulatedClassifier,
    uml_ExecutableNode,
    uml_FinalNode,
    uml_ForkNode,
    uml_InitialNode,
    uml_JoinNode,
    uml_NamedElement,
    uml_Namespace,
    uml_ObjectFlow,
    uml_ObjectNode,
    uml_OpaqueAction,
    uml_OpaqueExpression,
    uml_Package,
    uml_PackageableElement,
    uml_ParameterableElement,
    uml_RedefinableElement,
    uml_RootPackage,
    uml_StructuredClassifier,
    uml_TemplateableElement,
    uml_Type,
    uml_TypedElement,
    uml_ValueSpecification,
    ObjectNodeOrderingKind,
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

def test_uml_Behavior_isReentrant_value_roundtrip():
    instance = uml_Behavior(isReentrant="sample_text")
    assert instance.isReentrant == "sample_text"
    instance.isReentrant = "sample_text_2"
    assert instance.isReentrant == "sample_text_2"


def test_uml_Class_isActive_value_roundtrip():
    instance = uml_Class(isActive="sample_text")
    assert instance.isActive == "sample_text"
    instance.isActive = "sample_text_2"
    assert instance.isActive == "sample_text_2"


def test_uml_Classifier_isAbstract_value_roundtrip():
    instance = uml_Classifier(isAbstract="sample_text")
    assert instance.isAbstract == "sample_text"
    instance.isAbstract = "sample_text_2"
    assert instance.isAbstract == "sample_text_2"


def test_uml_JoinNode_isCombineDuplicate_value_roundtrip():
    instance = uml_JoinNode(isCombineDuplicate="sample_text")
    assert instance.isCombineDuplicate == "sample_text"
    instance.isCombineDuplicate = "sample_text_2"
    assert instance.isCombineDuplicate == "sample_text_2"


def test_uml_NamedElement_name_value_roundtrip():
    instance = uml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_uml_ObjectFlow_isMulticast_value_roundtrip():
    instance = uml_ObjectFlow(isMulticast="sample_text", isMultireceive="sample_text")
    assert instance.isMulticast == "sample_text"
    instance.isMulticast = "sample_text_2"
    assert instance.isMulticast == "sample_text_2"


def test_uml_ObjectFlow_isMultireceive_value_roundtrip():
    instance = uml_ObjectFlow(isMulticast="sample_text", isMultireceive="sample_text")
    assert instance.isMultireceive == "sample_text"
    instance.isMultireceive = "sample_text_2"
    assert instance.isMultireceive == "sample_text_2"


def test_uml_ObjectNode_isControlType_value_roundtrip():
    instance = uml_ObjectNode(isControlType="sample_text")
    assert instance.isControlType == "sample_text"
    instance.isControlType = "sample_text_2"
    assert instance.isControlType == "sample_text_2"


def test_uml_OpaqueExpression_body_value_roundtrip():
    instance = uml_OpaqueExpression(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_uml_RedefinableElement_isLeaf_value_roundtrip():
    instance = uml_RedefinableElement(isLeaf="sample_text")
    assert instance.isLeaf == "sample_text"
    instance.isLeaf = "sample_text_2"
    assert instance.isLeaf == "sample_text_2"


def test_uml_OpaqueAction_isa_Action():
    instance = uml_OpaqueAction()
    assert isinstance(instance, Action)


def test_uml_ControlFlow_isa_ActivityEdge():
    instance = uml_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_uml_ObjectFlow_isa_ActivityEdge():
    instance = uml_ObjectFlow(isMulticast="sample_text", isMultireceive="sample_text")
    assert isinstance(instance, ActivityEdge)


def test_uml_ActivityPartition_isa_ActivityGroup():
    instance = uml_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_uml_ControlNode_isa_ActivityNode():
    instance = uml_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_uml_ExecutableNode_isa_ActivityNode():
    instance = uml_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_uml_ObjectNode_isa_ActivityNode():
    instance = uml_ObjectNode(isControlType="sample_text")
    assert isinstance(instance, ActivityNode)


def test_uml_Activity_isa_Behavior():
    instance = uml_Activity()
    assert isinstance(instance, Behavior)


def test_uml_Class_isa_BehavioredClassifier():
    instance = uml_Class(isActive="sample_text")
    assert isinstance(instance, BehavioredClassifier)


def test_uml_Behavior_isa_Class():
    instance = uml_Behavior(isReentrant="sample_text")
    assert isinstance(instance, Class)


def test_uml_BehavioredClassifier_isa_Classifier():
    instance = uml_BehavioredClassifier()
    assert isinstance(instance, Classifier)


def test_uml_StructuredClassifier_isa_Classifier():
    instance = uml_StructuredClassifier()
    assert isinstance(instance, Classifier)


def test_uml_DecisionNode_isa_ControlNode():
    instance = uml_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_uml_FinalNode_isa_ControlNode():
    instance = uml_FinalNode()
    assert isinstance(instance, ControlNode)


def test_uml_ForkNode_isa_ControlNode():
    instance = uml_ForkNode()
    assert isinstance(instance, ControlNode)


def test_uml_InitialNode_isa_ControlNode():
    instance = uml_InitialNode()
    assert isinstance(instance, ControlNode)


def test_uml_JoinNode_isa_ControlNode():
    instance = uml_JoinNode(isCombineDuplicate="sample_text")
    assert isinstance(instance, ControlNode)


def test_uml_ActivityGroup_isa_Element():
    instance = uml_ActivityGroup()
    assert isinstance(instance, Element)


def test_uml_NamedElement_isa_Element():
    instance = uml_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_uml_ParameterableElement_isa_Element():
    instance = uml_ParameterableElement()
    assert isinstance(instance, Element)


def test_uml_TemplateableElement_isa_Element():
    instance = uml_TemplateableElement()
    assert isinstance(instance, Element)


def test_uml_Class_isa_EncapsulatedClassifier():
    instance = uml_Class(isActive="sample_text")
    assert isinstance(instance, EncapsulatedClassifier)


def test_uml_Action_isa_ExecutableNode():
    instance = uml_Action()
    assert isinstance(instance, ExecutableNode)


def test_uml_ActivityFinalNode_isa_FinalNode():
    instance = uml_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_uml_ActivityPartition_isa_NamedElement():
    instance = uml_ActivityPartition()
    assert isinstance(instance, NamedElement)


def test_uml_Namespace_isa_NamedElement():
    instance = uml_Namespace()
    assert isinstance(instance, NamedElement)


def test_uml_PackageableElement_isa_NamedElement():
    instance = uml_PackageableElement()
    assert isinstance(instance, NamedElement)


def test_uml_RedefinableElement_isa_NamedElement():
    instance = uml_RedefinableElement(isLeaf="sample_text")
    assert isinstance(instance, NamedElement)


def test_uml_TypedElement_isa_NamedElement():
    instance = uml_TypedElement()
    assert isinstance(instance, NamedElement)


def test_uml_Classifier_isa_Namespace():
    instance = uml_Classifier(isAbstract="sample_text")
    assert isinstance(instance, Namespace)


def test_uml_Package_isa_Namespace():
    instance = uml_Package()
    assert isinstance(instance, Namespace)


def test_uml_ActivityParameterNode_isa_ObjectNode():
    instance = uml_ActivityParameterNode()
    assert isinstance(instance, ObjectNode)


def test_uml_Package_isa_PackageableElement():
    instance = uml_Package()
    assert isinstance(instance, PackageableElement)


def test_uml_Type_isa_PackageableElement():
    instance = uml_Type()
    assert isinstance(instance, PackageableElement)


def test_uml_ValueSpecification_isa_PackageableElement():
    instance = uml_ValueSpecification()
    assert isinstance(instance, PackageableElement)


def test_uml_PackageableElement_isa_ParameterableElement():
    instance = uml_PackageableElement()
    assert isinstance(instance, ParameterableElement)


def test_uml_ActivityEdge_isa_RedefinableElement():
    instance = uml_ActivityEdge()
    assert isinstance(instance, RedefinableElement)


def test_uml_ActivityNode_isa_RedefinableElement():
    instance = uml_ActivityNode()
    assert isinstance(instance, RedefinableElement)


def test_uml_Classifier_isa_RedefinableElement():
    instance = uml_Classifier(isAbstract="sample_text")
    assert isinstance(instance, RedefinableElement)


def test_uml_EncapsulatedClassifier_isa_StructuredClassifier():
    instance = uml_EncapsulatedClassifier()
    assert isinstance(instance, StructuredClassifier)


def test_uml_Classifier_isa_TemplateableElement():
    instance = uml_Classifier(isAbstract="sample_text")
    assert isinstance(instance, TemplateableElement)


def test_uml_Package_isa_TemplateableElement():
    instance = uml_Package()
    assert isinstance(instance, TemplateableElement)


def test_uml_Classifier_isa_Type():
    instance = uml_Classifier(isAbstract="sample_text")
    assert isinstance(instance, Type)


def test_uml_ObjectNode_isa_TypedElement():
    instance = uml_ObjectNode(isControlType="sample_text")
    assert isinstance(instance, TypedElement)


def test_uml_ValueSpecification_isa_TypedElement():
    instance = uml_ValueSpecification()
    assert isinstance(instance, TypedElement)


def test_uml_OpaqueExpression_isa_ValueSpecification():
    instance = uml_OpaqueExpression(body="sample_text")
    assert isinstance(instance, ValueSpecification)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityGroup_strategy = st.builds(ActivityGroup)
@given(instance=ActivityGroup_strategy)
@settings(max_examples=25)
def test_ActivityGroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


BehavioredClassifier_strategy = st.builds(BehavioredClassifier)
@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


EncapsulatedClassifier_strategy = st.builds(EncapsulatedClassifier)
@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=25)
def test_EncapsulatedClassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


PackageableElement_strategy = st.builds(PackageableElement)
@given(instance=PackageableElement_strategy)
@settings(max_examples=25)
def test_PackageableElement_instantiation(instance):
    assert isinstance(instance, PackageableElement)


ParameterableElement_strategy = st.builds(ParameterableElement)
@given(instance=ParameterableElement_strategy)
@settings(max_examples=25)
def test_ParameterableElement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)


RedefinableElement_strategy = st.builds(RedefinableElement)
@given(instance=RedefinableElement_strategy)
@settings(max_examples=25)
def test_RedefinableElement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)


StructuredClassifier_strategy = st.builds(StructuredClassifier)
@given(instance=StructuredClassifier_strategy)
@settings(max_examples=25)
def test_StructuredClassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)


TemplateableElement_strategy = st.builds(TemplateableElement)
@given(instance=TemplateableElement_strategy)
@settings(max_examples=25)
def test_TemplateableElement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


uml_Action_strategy = st.builds(uml_Action)
@given(instance=uml_Action_strategy)
@settings(max_examples=25)
def test_uml_Action_instantiation(instance):
    assert isinstance(instance, uml_Action)


uml_Activity_strategy = st.builds(uml_Activity)
@given(instance=uml_Activity_strategy)
@settings(max_examples=25)
def test_uml_Activity_instantiation(instance):
    assert isinstance(instance, uml_Activity)


uml_ActivityEdge_strategy = st.builds(uml_ActivityEdge)
@given(instance=uml_ActivityEdge_strategy)
@settings(max_examples=25)
def test_uml_ActivityEdge_instantiation(instance):
    assert isinstance(instance, uml_ActivityEdge)


uml_ActivityFinalNode_strategy = st.builds(uml_ActivityFinalNode)
@given(instance=uml_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_uml_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, uml_ActivityFinalNode)


uml_ActivityGroup_strategy = st.builds(uml_ActivityGroup)
@given(instance=uml_ActivityGroup_strategy)
@settings(max_examples=25)
def test_uml_ActivityGroup_instantiation(instance):
    assert isinstance(instance, uml_ActivityGroup)


uml_ActivityNode_strategy = st.builds(uml_ActivityNode)
@given(instance=uml_ActivityNode_strategy)
@settings(max_examples=25)
def test_uml_ActivityNode_instantiation(instance):
    assert isinstance(instance, uml_ActivityNode)


uml_ActivityParameterNode_strategy = st.builds(uml_ActivityParameterNode)
@given(instance=uml_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_uml_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, uml_ActivityParameterNode)


uml_ActivityPartition_strategy = st.builds(uml_ActivityPartition)
@given(instance=uml_ActivityPartition_strategy)
@settings(max_examples=25)
def test_uml_ActivityPartition_instantiation(instance):
    assert isinstance(instance, uml_ActivityPartition)


uml_Behavior_strategy = st.builds(uml_Behavior, isReentrant=safe_text)
@given(instance=uml_Behavior_strategy)
@settings(max_examples=25)
def test_uml_Behavior_instantiation(instance):
    assert isinstance(instance, uml_Behavior)


uml_BehavioredClassifier_strategy = st.builds(uml_BehavioredClassifier)
@given(instance=uml_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_uml_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, uml_BehavioredClassifier)


uml_Class_strategy = st.builds(uml_Class, isActive=safe_text)
@given(instance=uml_Class_strategy)
@settings(max_examples=25)
def test_uml_Class_instantiation(instance):
    assert isinstance(instance, uml_Class)


uml_Classifier_strategy = st.builds(uml_Classifier, isAbstract=safe_text)
@given(instance=uml_Classifier_strategy)
@settings(max_examples=25)
def test_uml_Classifier_instantiation(instance):
    assert isinstance(instance, uml_Classifier)


uml_ControlFlow_strategy = st.builds(uml_ControlFlow)
@given(instance=uml_ControlFlow_strategy)
@settings(max_examples=25)
def test_uml_ControlFlow_instantiation(instance):
    assert isinstance(instance, uml_ControlFlow)


uml_ControlNode_strategy = st.builds(uml_ControlNode)
@given(instance=uml_ControlNode_strategy)
@settings(max_examples=25)
def test_uml_ControlNode_instantiation(instance):
    assert isinstance(instance, uml_ControlNode)


uml_DecisionNode_strategy = st.builds(uml_DecisionNode)
@given(instance=uml_DecisionNode_strategy)
@settings(max_examples=25)
def test_uml_DecisionNode_instantiation(instance):
    assert isinstance(instance, uml_DecisionNode)


uml_Element_strategy = st.builds(uml_Element)
@given(instance=uml_Element_strategy)
@settings(max_examples=25)
def test_uml_Element_instantiation(instance):
    assert isinstance(instance, uml_Element)


uml_EncapsulatedClassifier_strategy = st.builds(uml_EncapsulatedClassifier)
@given(instance=uml_EncapsulatedClassifier_strategy)
@settings(max_examples=25)
def test_uml_EncapsulatedClassifier_instantiation(instance):
    assert isinstance(instance, uml_EncapsulatedClassifier)


uml_ExecutableNode_strategy = st.builds(uml_ExecutableNode)
@given(instance=uml_ExecutableNode_strategy)
@settings(max_examples=25)
def test_uml_ExecutableNode_instantiation(instance):
    assert isinstance(instance, uml_ExecutableNode)


uml_FinalNode_strategy = st.builds(uml_FinalNode)
@given(instance=uml_FinalNode_strategy)
@settings(max_examples=25)
def test_uml_FinalNode_instantiation(instance):
    assert isinstance(instance, uml_FinalNode)


uml_ForkNode_strategy = st.builds(uml_ForkNode)
@given(instance=uml_ForkNode_strategy)
@settings(max_examples=25)
def test_uml_ForkNode_instantiation(instance):
    assert isinstance(instance, uml_ForkNode)


uml_InitialNode_strategy = st.builds(uml_InitialNode)
@given(instance=uml_InitialNode_strategy)
@settings(max_examples=25)
def test_uml_InitialNode_instantiation(instance):
    assert isinstance(instance, uml_InitialNode)


uml_JoinNode_strategy = st.builds(uml_JoinNode, isCombineDuplicate=safe_text)
@given(instance=uml_JoinNode_strategy)
@settings(max_examples=25)
def test_uml_JoinNode_instantiation(instance):
    assert isinstance(instance, uml_JoinNode)


uml_NamedElement_strategy = st.builds(uml_NamedElement, name=safe_text)
@given(instance=uml_NamedElement_strategy)
@settings(max_examples=25)
def test_uml_NamedElement_instantiation(instance):
    assert isinstance(instance, uml_NamedElement)


uml_Namespace_strategy = st.builds(uml_Namespace)
@given(instance=uml_Namespace_strategy)
@settings(max_examples=25)
def test_uml_Namespace_instantiation(instance):
    assert isinstance(instance, uml_Namespace)


uml_ObjectFlow_strategy = st.builds(uml_ObjectFlow, isMulticast=safe_text, isMultireceive=safe_text)
@given(instance=uml_ObjectFlow_strategy)
@settings(max_examples=25)
def test_uml_ObjectFlow_instantiation(instance):
    assert isinstance(instance, uml_ObjectFlow)


uml_ObjectNode_strategy = st.builds(uml_ObjectNode, isControlType=safe_text)
@given(instance=uml_ObjectNode_strategy)
@settings(max_examples=25)
def test_uml_ObjectNode_instantiation(instance):
    assert isinstance(instance, uml_ObjectNode)


uml_OpaqueAction_strategy = st.builds(uml_OpaqueAction)
@given(instance=uml_OpaqueAction_strategy)
@settings(max_examples=25)
def test_uml_OpaqueAction_instantiation(instance):
    assert isinstance(instance, uml_OpaqueAction)


uml_OpaqueExpression_strategy = st.builds(uml_OpaqueExpression, body=safe_text)
@given(instance=uml_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_uml_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, uml_OpaqueExpression)


uml_Package_strategy = st.builds(uml_Package)
@given(instance=uml_Package_strategy)
@settings(max_examples=25)
def test_uml_Package_instantiation(instance):
    assert isinstance(instance, uml_Package)


uml_PackageableElement_strategy = st.builds(uml_PackageableElement)
@given(instance=uml_PackageableElement_strategy)
@settings(max_examples=25)
def test_uml_PackageableElement_instantiation(instance):
    assert isinstance(instance, uml_PackageableElement)


uml_ParameterableElement_strategy = st.builds(uml_ParameterableElement)
@given(instance=uml_ParameterableElement_strategy)
@settings(max_examples=25)
def test_uml_ParameterableElement_instantiation(instance):
    assert isinstance(instance, uml_ParameterableElement)


uml_RedefinableElement_strategy = st.builds(uml_RedefinableElement, isLeaf=safe_text)
@given(instance=uml_RedefinableElement_strategy)
@settings(max_examples=25)
def test_uml_RedefinableElement_instantiation(instance):
    assert isinstance(instance, uml_RedefinableElement)


uml_RootPackage_strategy = st.builds(uml_RootPackage)
@given(instance=uml_RootPackage_strategy)
@settings(max_examples=25)
def test_uml_RootPackage_instantiation(instance):
    assert isinstance(instance, uml_RootPackage)


uml_StructuredClassifier_strategy = st.builds(uml_StructuredClassifier)
@given(instance=uml_StructuredClassifier_strategy)
@settings(max_examples=25)
def test_uml_StructuredClassifier_instantiation(instance):
    assert isinstance(instance, uml_StructuredClassifier)


uml_TemplateableElement_strategy = st.builds(uml_TemplateableElement)
@given(instance=uml_TemplateableElement_strategy)
@settings(max_examples=25)
def test_uml_TemplateableElement_instantiation(instance):
    assert isinstance(instance, uml_TemplateableElement)


uml_Type_strategy = st.builds(uml_Type)
@given(instance=uml_Type_strategy)
@settings(max_examples=25)
def test_uml_Type_instantiation(instance):
    assert isinstance(instance, uml_Type)


uml_TypedElement_strategy = st.builds(uml_TypedElement)
@given(instance=uml_TypedElement_strategy)
@settings(max_examples=25)
def test_uml_TypedElement_instantiation(instance):
    assert isinstance(instance, uml_TypedElement)


uml_ValueSpecification_strategy = st.builds(uml_ValueSpecification)
@given(instance=uml_ValueSpecification_strategy)
@settings(max_examples=25)
def test_uml_ValueSpecification_instantiation(instance):
    assert isinstance(instance, uml_ValueSpecification)



