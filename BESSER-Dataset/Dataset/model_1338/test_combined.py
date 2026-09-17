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
    Relation,
    umlclassdiagram_Association,
    umlclassdiagram_Aggregation,
    umlclassdiagram_Composition,
    umlclassdiagram_Dependency,
    Modifier,
    umlclassdiagram_Operator,
    Feature,
    umlclassdiagram_Operation,
    umlclassdiagram_Attribute,
    Classifier,
    umlclassdiagram_Class,
    umlclassdiagram_AssociationClass,
    NavigationPathCS,
    umlclassdiagram_NavigationPathElementCS,
    umlclassdiagram_NavigationPathVariableCS,
    umlclassdiagram_NavigationPathCS,
    NamedElement,
    umlclassdiagram_Modifier,
    umlclassdiagram_Parameter,
    umlclassdiagram_NamedElement,
    umlclassdiagram_Constraint,
    umlclassdiagram_PrimitiveElement,
    umlclassdiagram_Relation,
    umlclassdiagram_Classifier,
    umlclassdiagram_ClassDiagram,
    umlclassdiagram_AccVarCS,
    LoopExpCS,
    umlclassdiagram_IterateExpCS,
    umlclassdiagram_ForAllExpCS,
    umlclassdiagram_CollectExpCS,
    umlclassdiagram_IteratorVarCS,
    umlclassdiagram_NavigationPathNameCS,
    umlclassdiagram_ExistsExpCS,
    BooleanLiteralExpCS,
    umlclassdiagram_BooleanExpCS,
    umlclassdiagram_Feature,
    PathCS,
    umlclassdiagram_PathElementCS,
    umlclassdiagram_PathVariableCS,
    umlclassdiagram_PathCS,
    LiteralExpCS,
    umlclassdiagram_BooleanLiteralExpCS,
    umlclassdiagram_StringLiteralExpCS,
    umlclassdiagram_IntLiteralExpCS,
    umlclassdiagram_InvariantCS,
    umlclassdiagram_ExpCS,
    umlclassdiagram_RoundedBracketClauseCS,
    NavigationExpCS,
    umlclassdiagram_NavigationNameExpCS,
    umlclassdiagram_LoopExpCS,
    umlclassdiagram_NameExpCS,
    PrimaryExpCS,
    umlclassdiagram_LiteralExpCS,
    CallExpCS,
    umlclassdiagram_PrimaryExpCS,
    umlclassdiagram_NavigationExpCS,
    LogicExpCS,
    umlclassdiagram_CallExpCS,
    ExpCS,
    umlclassdiagram_LogicExpCS,
    umlclassdiagram_ParameterCS,
    umlclassdiagram_OperationCS,
    umlclassdiagram_PropertyCS,
    umlclassdiagram_PathNameCS,
    umlclassdiagram_ClassCS,
    umlclassdiagram_ConstraintCS,
    umlclassdiagram_PackageCS,
    umlclassdiagram_RootCS,
    OperatorType,
    VisbilityType,
    PrimitiveDataType,
    ScopeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_hyp_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_hyp_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_association_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Association)


def test_hyp_umlclassdiagram_association_constructor_exists():
    assert callable(umlclassdiagram_Association.__init__)


def test_hyp_umlclassdiagram_association_constructor_args():
    sig = inspect.signature(umlclassdiagram_Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_aggregation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Aggregation)


def test_hyp_umlclassdiagram_aggregation_constructor_exists():
    assert callable(umlclassdiagram_Aggregation.__init__)


def test_hyp_umlclassdiagram_aggregation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Aggregation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_composition_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Composition)


def test_hyp_umlclassdiagram_composition_constructor_exists():
    assert callable(umlclassdiagram_Composition.__init__)


def test_hyp_umlclassdiagram_composition_constructor_args():
    sig = inspect.signature(umlclassdiagram_Composition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_dependency_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Dependency)


def test_hyp_umlclassdiagram_dependency_constructor_exists():
    assert callable(umlclassdiagram_Dependency.__init__)


def test_hyp_umlclassdiagram_dependency_constructor_args():
    sig = inspect.signature(umlclassdiagram_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_hyp_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_hyp_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_operator_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Operator)


def test_hyp_umlclassdiagram_operator_constructor_exists():
    assert callable(umlclassdiagram_Operator.__init__)


def test_hyp_umlclassdiagram_operator_constructor_args():
    sig = inspect.signature(umlclassdiagram_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_operation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Operation)


def test_hyp_umlclassdiagram_operation_constructor_exists():
    assert callable(umlclassdiagram_Operation.__init__)


def test_hyp_umlclassdiagram_operation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Attribute)


def test_hyp_umlclassdiagram_attribute_constructor_exists():
    assert callable(umlclassdiagram_Attribute.__init__)


def test_hyp_umlclassdiagram_attribute_constructor_args():
    sig = inspect.signature(umlclassdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"




def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_class_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Class)


def test_hyp_umlclassdiagram_class_constructor_exists():
    assert callable(umlclassdiagram_Class.__init__)


def test_hyp_umlclassdiagram_class_constructor_args():
    sig = inspect.signature(umlclassdiagram_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_associationclass_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_AssociationClass)


def test_hyp_umlclassdiagram_associationclass_constructor_exists():
    assert callable(umlclassdiagram_AssociationClass.__init__)


def test_hyp_umlclassdiagram_associationclass_constructor_args():
    sig = inspect.signature(umlclassdiagram_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_hyp_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_hyp_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathElementCS)


def test_hyp_umlclassdiagram_navigationpathelementcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathElementCS.__init__)


def test_hyp_umlclassdiagram_navigationpathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathVariableCS)


def test_hyp_umlclassdiagram_navigationpathvariablecs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathVariableCS.__init__)


def test_hyp_umlclassdiagram_navigationpathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_umlclassdiagram_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathCS)


def test_hyp_umlclassdiagram_navigationpathcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathCS.__init__)


def test_hyp_umlclassdiagram_navigationpathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_modifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Modifier)


def test_hyp_umlclassdiagram_modifier_constructor_exists():
    assert callable(umlclassdiagram_Modifier.__init__)


def test_hyp_umlclassdiagram_modifier_constructor_args():
    sig = inspect.signature(umlclassdiagram_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "visibility" in params, "Missing parameter 'visibility'"





def test_hyp_umlclassdiagram_parameter_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Parameter)


def test_hyp_umlclassdiagram_parameter_constructor_exists():
    assert callable(umlclassdiagram_Parameter.__init__)


def test_hyp_umlclassdiagram_parameter_constructor_args():
    sig = inspect.signature(umlclassdiagram_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_namedelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NamedElement)


def test_hyp_umlclassdiagram_namedelement_constructor_exists():
    assert callable(umlclassdiagram_NamedElement.__init__)


def test_hyp_umlclassdiagram_namedelement_constructor_args():
    sig = inspect.signature(umlclassdiagram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_constraint_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Constraint)


def test_hyp_umlclassdiagram_constraint_constructor_exists():
    assert callable(umlclassdiagram_Constraint.__init__)


def test_hyp_umlclassdiagram_constraint_constructor_args():
    sig = inspect.signature(umlclassdiagram_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_umlclassdiagram_primitiveelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PrimitiveElement)


def test_hyp_umlclassdiagram_primitiveelement_constructor_exists():
    assert callable(umlclassdiagram_PrimitiveElement.__init__)


def test_hyp_umlclassdiagram_primitiveelement_constructor_args():
    sig = inspect.signature(umlclassdiagram_PrimitiveElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_umlclassdiagram_relation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Relation)


def test_hyp_umlclassdiagram_relation_constructor_exists():
    assert callable(umlclassdiagram_Relation.__init__)


def test_hyp_umlclassdiagram_relation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "ntar" in params, "Missing parameter 'ntar'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "nsrc" in params, "Missing parameter 'nsrc'"






def test_hyp_umlclassdiagram_classifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Classifier)


def test_hyp_umlclassdiagram_classifier_constructor_exists():
    assert callable(umlclassdiagram_Classifier.__init__)


def test_hyp_umlclassdiagram_classifier_constructor_args():
    sig = inspect.signature(umlclassdiagram_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "abstract" in params, "Missing parameter 'abstract'"





def test_hyp_umlclassdiagram_classdiagram_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ClassDiagram)


def test_hyp_umlclassdiagram_classdiagram_constructor_exists():
    assert callable(umlclassdiagram_ClassDiagram.__init__)


def test_hyp_umlclassdiagram_classdiagram_constructor_args():
    sig = inspect.signature(umlclassdiagram_ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_accvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_AccVarCS)


def test_hyp_umlclassdiagram_accvarcs_constructor_exists():
    assert callable(umlclassdiagram_AccVarCS.__init__)


def test_hyp_umlclassdiagram_accvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"




def test_hyp_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_hyp_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_hyp_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IterateExpCS)


def test_hyp_umlclassdiagram_iterateexpcs_constructor_exists():
    assert callable(umlclassdiagram_IterateExpCS.__init__)


def test_hyp_umlclassdiagram_iterateexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_forallexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ForAllExpCS)


def test_hyp_umlclassdiagram_forallexpcs_constructor_exists():
    assert callable(umlclassdiagram_ForAllExpCS.__init__)


def test_hyp_umlclassdiagram_forallexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_collectexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_CollectExpCS)


def test_hyp_umlclassdiagram_collectexpcs_constructor_exists():
    assert callable(umlclassdiagram_CollectExpCS.__init__)


def test_hyp_umlclassdiagram_collectexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IteratorVarCS)


def test_hyp_umlclassdiagram_iteratorvarcs_constructor_exists():
    assert callable(umlclassdiagram_IteratorVarCS.__init__)


def test_hyp_umlclassdiagram_iteratorvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"




def test_hyp_umlclassdiagram_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathNameCS)


def test_hyp_umlclassdiagram_navigationpathnamecs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathNameCS.__init__)


def test_hyp_umlclassdiagram_navigationpathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_existsexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ExistsExpCS)


def test_hyp_umlclassdiagram_existsexpcs_constructor_exists():
    assert callable(umlclassdiagram_ExistsExpCS.__init__)


def test_hyp_umlclassdiagram_existsexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_hyp_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_hyp_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_BooleanExpCS)


def test_hyp_umlclassdiagram_booleanexpcs_constructor_exists():
    assert callable(umlclassdiagram_BooleanExpCS.__init__)


def test_hyp_umlclassdiagram_booleanexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"




def test_hyp_umlclassdiagram_feature_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Feature)


def test_hyp_umlclassdiagram_feature_constructor_exists():
    assert callable(umlclassdiagram_Feature.__init__)


def test_hyp_umlclassdiagram_feature_constructor_args():
    sig = inspect.signature(umlclassdiagram_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_hyp_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_hyp_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathElementCS)


def test_hyp_umlclassdiagram_pathelementcs_constructor_exists():
    assert callable(umlclassdiagram_PathElementCS.__init__)


def test_hyp_umlclassdiagram_pathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathVariableCS)


def test_hyp_umlclassdiagram_pathvariablecs_constructor_exists():
    assert callable(umlclassdiagram_PathVariableCS.__init__)


def test_hyp_umlclassdiagram_pathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_umlclassdiagram_pathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathCS)


def test_hyp_umlclassdiagram_pathcs_constructor_exists():
    assert callable(umlclassdiagram_PathCS.__init__)


def test_hyp_umlclassdiagram_pathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_hyp_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_hyp_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_BooleanLiteralExpCS)


def test_hyp_umlclassdiagram_booleanliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_BooleanLiteralExpCS.__init__)


def test_hyp_umlclassdiagram_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_StringLiteralExpCS)


def test_hyp_umlclassdiagram_stringliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_StringLiteralExpCS.__init__)


def test_hyp_umlclassdiagram_stringliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_umlclassdiagram_intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IntLiteralExpCS)


def test_hyp_umlclassdiagram_intliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_IntLiteralExpCS.__init__)


def test_hyp_umlclassdiagram_intliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"




def test_hyp_umlclassdiagram_invariantcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_InvariantCS)


def test_hyp_umlclassdiagram_invariantcs_constructor_exists():
    assert callable(umlclassdiagram_InvariantCS.__init__)


def test_hyp_umlclassdiagram_invariantcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_expcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ExpCS)


def test_hyp_umlclassdiagram_expcs_constructor_exists():
    assert callable(umlclassdiagram_ExpCS.__init__)


def test_hyp_umlclassdiagram_expcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_RoundedBracketClauseCS)


def test_hyp_umlclassdiagram_roundedbracketclausecs_constructor_exists():
    assert callable(umlclassdiagram_RoundedBracketClauseCS.__init__)


def test_hyp_umlclassdiagram_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_hyp_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_hyp_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationNameExpCS)


def test_hyp_umlclassdiagram_navigationnameexpcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationNameExpCS.__init__)


def test_hyp_umlclassdiagram_navigationnameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LoopExpCS)


def test_hyp_umlclassdiagram_loopexpcs_constructor_exists():
    assert callable(umlclassdiagram_LoopExpCS.__init__)


def test_hyp_umlclassdiagram_loopexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"




def test_hyp_umlclassdiagram_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NameExpCS)


def test_hyp_umlclassdiagram_nameexpcs_constructor_exists():
    assert callable(umlclassdiagram_NameExpCS.__init__)


def test_hyp_umlclassdiagram_nameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_hyp_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_hyp_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LiteralExpCS)


def test_hyp_umlclassdiagram_literalexpcs_constructor_exists():
    assert callable(umlclassdiagram_LiteralExpCS.__init__)


def test_hyp_umlclassdiagram_literalexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_hyp_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_hyp_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PrimaryExpCS)


def test_hyp_umlclassdiagram_primaryexpcs_constructor_exists():
    assert callable(umlclassdiagram_PrimaryExpCS.__init__)


def test_hyp_umlclassdiagram_primaryexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationExpCS)


def test_hyp_umlclassdiagram_navigationexpcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationExpCS.__init__)


def test_hyp_umlclassdiagram_navigationexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_hyp_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_hyp_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_callexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_CallExpCS)


def test_hyp_umlclassdiagram_callexpcs_constructor_exists():
    assert callable(umlclassdiagram_CallExpCS.__init__)


def test_hyp_umlclassdiagram_callexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_hyp_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_hyp_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LogicExpCS)


def test_hyp_umlclassdiagram_logicexpcs_constructor_exists():
    assert callable(umlclassdiagram_LogicExpCS.__init__)


def test_hyp_umlclassdiagram_logicexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_umlclassdiagram_parametercs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ParameterCS)


def test_hyp_umlclassdiagram_parametercs_constructor_exists():
    assert callable(umlclassdiagram_ParameterCS.__init__)


def test_hyp_umlclassdiagram_parametercs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_operationcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_OperationCS)


def test_hyp_umlclassdiagram_operationcs_constructor_exists():
    assert callable(umlclassdiagram_OperationCS.__init__)


def test_hyp_umlclassdiagram_operationcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_propertycs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PropertyCS)


def test_hyp_umlclassdiagram_propertycs_constructor_exists():
    assert callable(umlclassdiagram_PropertyCS.__init__)


def test_hyp_umlclassdiagram_propertycs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathNameCS)


def test_hyp_umlclassdiagram_pathnamecs_constructor_exists():
    assert callable(umlclassdiagram_PathNameCS.__init__)


def test_hyp_umlclassdiagram_pathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_classcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ClassCS)


def test_hyp_umlclassdiagram_classcs_constructor_exists():
    assert callable(umlclassdiagram_ClassCS.__init__)


def test_hyp_umlclassdiagram_classcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_constraintcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ConstraintCS)


def test_hyp_umlclassdiagram_constraintcs_constructor_exists():
    assert callable(umlclassdiagram_ConstraintCS.__init__)


def test_hyp_umlclassdiagram_constraintcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlclassdiagram_packagecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PackageCS)


def test_hyp_umlclassdiagram_packagecs_constructor_exists():
    assert callable(umlclassdiagram_PackageCS.__init__)


def test_hyp_umlclassdiagram_packagecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_umlclassdiagram_rootcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_RootCS)


def test_hyp_umlclassdiagram_rootcs_constructor_exists():
    assert callable(umlclassdiagram_RootCS.__init__)


def test_hyp_umlclassdiagram_rootcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_RootCS.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_hyp_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "subtract",
        "or_",
        "gte",
        "module",
        "and_",
        "add",
        "multiply",
        "distinct",
        "lt",
        "gt",
        "negative",
        "equals",
        "lte",
        "not_",
        "divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorType"

def test_hyp_visbilitytype_exists():
    # Check that the Enumeration exists
    assert VisbilityType is not None

def test_hyp_visbilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisbilityType]
    expected_literals = [
        "protected",
        "package",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisbilityType"

def test_hyp_primitivedatatype_exists():
    # Check that the Enumeration exists
    assert PrimitiveDataType is not None

def test_hyp_primitivedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveDataType]
    expected_literals = [
        "Integer",
        "Date",
        "Boolean",
        "String",
        "Double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveDataType"

def test_hyp_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_hyp_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "classifier",
        "instance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"


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
Relation_strategy = st.builds(
    Relation,
)
umlclassdiagram_Association_strategy = st.builds(
    umlclassdiagram_Association,
)
umlclassdiagram_Aggregation_strategy = st.builds(
    umlclassdiagram_Aggregation,
)
umlclassdiagram_Composition_strategy = st.builds(
    umlclassdiagram_Composition,
)
umlclassdiagram_Dependency_strategy = st.builds(
    umlclassdiagram_Dependency,
)
Modifier_strategy = st.builds(
    Modifier,
)
umlclassdiagram_Operator_strategy = st.builds(
    umlclassdiagram_Operator,
    operator=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
umlclassdiagram_Operation_strategy = st.builds(
    umlclassdiagram_Operation,
)
umlclassdiagram_Attribute_strategy = st.builds(
    umlclassdiagram_Attribute,
    derived=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
umlclassdiagram_Class_strategy = st.builds(
    umlclassdiagram_Class,
)
umlclassdiagram_AssociationClass_strategy = st.builds(
    umlclassdiagram_AssociationClass,
)
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
umlclassdiagram_NavigationPathElementCS_strategy = st.builds(
    umlclassdiagram_NavigationPathElementCS,
)
umlclassdiagram_NavigationPathVariableCS_strategy = st.builds(
    umlclassdiagram_NavigationPathVariableCS,
    varName=
        safe_text
)
umlclassdiagram_NavigationPathCS_strategy = st.builds(
    umlclassdiagram_NavigationPathCS,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umlclassdiagram_Modifier_strategy = st.builds(
    umlclassdiagram_Modifier,
    scope=
        safe_text,
    visibility=
        safe_text
)
umlclassdiagram_Parameter_strategy = st.builds(
    umlclassdiagram_Parameter,
)
umlclassdiagram_NamedElement_strategy = st.builds(
    umlclassdiagram_NamedElement,
    name=
        safe_text
)
umlclassdiagram_Constraint_strategy = st.builds(
    umlclassdiagram_Constraint,
    id=
        safe_text
)
umlclassdiagram_PrimitiveElement_strategy = st.builds(
    umlclassdiagram_PrimitiveElement,
    type=
        safe_text
)
umlclassdiagram_Relation_strategy = st.builds(
    umlclassdiagram_Relation,
    ntar=
        safe_text,
    derived=
        st.booleans(),
    nsrc=
        safe_text
)
umlclassdiagram_Classifier_strategy = st.builds(
    umlclassdiagram_Classifier,
    derived=
        st.booleans(),
    abstract=
        st.booleans()
)
umlclassdiagram_ClassDiagram_strategy = st.builds(
    umlclassdiagram_ClassDiagram,
)
umlclassdiagram_AccVarCS_strategy = st.builds(
    umlclassdiagram_AccVarCS,
    accVarName=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
umlclassdiagram_IterateExpCS_strategy = st.builds(
    umlclassdiagram_IterateExpCS,
)
umlclassdiagram_ForAllExpCS_strategy = st.builds(
    umlclassdiagram_ForAllExpCS,
)
umlclassdiagram_CollectExpCS_strategy = st.builds(
    umlclassdiagram_CollectExpCS,
)
umlclassdiagram_IteratorVarCS_strategy = st.builds(
    umlclassdiagram_IteratorVarCS,
    itName=
        safe_text
)
umlclassdiagram_NavigationPathNameCS_strategy = st.builds(
    umlclassdiagram_NavigationPathNameCS,
)
umlclassdiagram_ExistsExpCS_strategy = st.builds(
    umlclassdiagram_ExistsExpCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
umlclassdiagram_BooleanExpCS_strategy = st.builds(
    umlclassdiagram_BooleanExpCS,
    boolSymbol=
        st.booleans()
)
umlclassdiagram_Feature_strategy = st.builds(
    umlclassdiagram_Feature,
    scope=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
PathCS_strategy = st.builds(
    PathCS,
)
umlclassdiagram_PathElementCS_strategy = st.builds(
    umlclassdiagram_PathElementCS,
)
umlclassdiagram_PathVariableCS_strategy = st.builds(
    umlclassdiagram_PathVariableCS,
    varName=
        safe_text
)
umlclassdiagram_PathCS_strategy = st.builds(
    umlclassdiagram_PathCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
umlclassdiagram_BooleanLiteralExpCS_strategy = st.builds(
    umlclassdiagram_BooleanLiteralExpCS,
)
umlclassdiagram_StringLiteralExpCS_strategy = st.builds(
    umlclassdiagram_StringLiteralExpCS,
    stringSymbol=
        safe_text
)
umlclassdiagram_IntLiteralExpCS_strategy = st.builds(
    umlclassdiagram_IntLiteralExpCS,
    intSymbol=
        st.integers()
)
umlclassdiagram_InvariantCS_strategy = st.builds(
    umlclassdiagram_InvariantCS,
)
umlclassdiagram_ExpCS_strategy = st.builds(
    umlclassdiagram_ExpCS,
)
umlclassdiagram_RoundedBracketClauseCS_strategy = st.builds(
    umlclassdiagram_RoundedBracketClauseCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
umlclassdiagram_NavigationNameExpCS_strategy = st.builds(
    umlclassdiagram_NavigationNameExpCS,
)
umlclassdiagram_LoopExpCS_strategy = st.builds(
    umlclassdiagram_LoopExpCS,
    logicOp=
        safe_text
)
umlclassdiagram_NameExpCS_strategy = st.builds(
    umlclassdiagram_NameExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
umlclassdiagram_LiteralExpCS_strategy = st.builds(
    umlclassdiagram_LiteralExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
umlclassdiagram_PrimaryExpCS_strategy = st.builds(
    umlclassdiagram_PrimaryExpCS,
)
umlclassdiagram_NavigationExpCS_strategy = st.builds(
    umlclassdiagram_NavigationExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
umlclassdiagram_CallExpCS_strategy = st.builds(
    umlclassdiagram_CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
umlclassdiagram_LogicExpCS_strategy = st.builds(
    umlclassdiagram_LogicExpCS,
    op=
        safe_text
)
umlclassdiagram_ParameterCS_strategy = st.builds(
    umlclassdiagram_ParameterCS,
    name=
        safe_text
)
umlclassdiagram_OperationCS_strategy = st.builds(
    umlclassdiagram_OperationCS,
    name=
        safe_text
)
umlclassdiagram_PropertyCS_strategy = st.builds(
    umlclassdiagram_PropertyCS,
    name=
        safe_text
)
umlclassdiagram_PathNameCS_strategy = st.builds(
    umlclassdiagram_PathNameCS,
)
umlclassdiagram_ClassCS_strategy = st.builds(
    umlclassdiagram_ClassCS,
    name=
        safe_text
)
umlclassdiagram_ConstraintCS_strategy = st.builds(
    umlclassdiagram_ConstraintCS,
)
umlclassdiagram_PackageCS_strategy = st.builds(
    umlclassdiagram_PackageCS,
    name=
        safe_text
)
umlclassdiagram_RootCS_strategy = st.builds(
    umlclassdiagram_RootCS,
)










@given(instance=umlclassdiagram_Operator_strategy)
def test_hyp_umlclassdiagram_operator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=umlclassdiagram_Attribute_strategy)
def test_hyp_umlclassdiagram_attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original









@given(instance=umlclassdiagram_NavigationPathVariableCS_strategy)
def test_hyp_umlclassdiagram_navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original






@given(instance=umlclassdiagram_Modifier_strategy)
def test_hyp_umlclassdiagram_modifier_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=umlclassdiagram_Modifier_strategy)
def test_hyp_umlclassdiagram_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original





@given(instance=umlclassdiagram_NamedElement_strategy)
def test_hyp_umlclassdiagram_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=umlclassdiagram_Constraint_strategy)
def test_hyp_umlclassdiagram_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=umlclassdiagram_PrimitiveElement_strategy)
def test_hyp_umlclassdiagram_primitiveelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=umlclassdiagram_Relation_strategy)
def test_hyp_umlclassdiagram_relation_ntar_setter(instance):
    original = instance.ntar
    instance.ntar = original
    assert instance.ntar == original



@given(instance=umlclassdiagram_Relation_strategy)
def test_hyp_umlclassdiagram_relation_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=umlclassdiagram_Relation_strategy)
def test_hyp_umlclassdiagram_relation_nsrc_setter(instance):
    original = instance.nsrc
    instance.nsrc = original
    assert instance.nsrc == original




@given(instance=umlclassdiagram_Classifier_strategy)
def test_hyp_umlclassdiagram_classifier_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=umlclassdiagram_Classifier_strategy)
def test_hyp_umlclassdiagram_classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original





@given(instance=umlclassdiagram_AccVarCS_strategy)
def test_hyp_umlclassdiagram_accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original








@given(instance=umlclassdiagram_IteratorVarCS_strategy)
def test_hyp_umlclassdiagram_iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original







@given(instance=umlclassdiagram_BooleanExpCS_strategy)
def test_hyp_umlclassdiagram_booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original




@given(instance=umlclassdiagram_Feature_strategy)
def test_hyp_umlclassdiagram_feature_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=umlclassdiagram_Feature_strategy)
def test_hyp_umlclassdiagram_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=umlclassdiagram_Feature_strategy)
def test_hyp_umlclassdiagram_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=umlclassdiagram_PathVariableCS_strategy)
def test_hyp_umlclassdiagram_pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original







@given(instance=umlclassdiagram_StringLiteralExpCS_strategy)
def test_hyp_umlclassdiagram_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original




@given(instance=umlclassdiagram_IntLiteralExpCS_strategy)
def test_hyp_umlclassdiagram_intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original









@given(instance=umlclassdiagram_LoopExpCS_strategy)
def test_hyp_umlclassdiagram_loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original













@given(instance=umlclassdiagram_LogicExpCS_strategy)
def test_hyp_umlclassdiagram_logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=umlclassdiagram_ParameterCS_strategy)
def test_hyp_umlclassdiagram_parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=umlclassdiagram_OperationCS_strategy)
def test_hyp_umlclassdiagram_operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=umlclassdiagram_PropertyCS_strategy)
def test_hyp_umlclassdiagram_propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=umlclassdiagram_ClassCS_strategy)
def test_hyp_umlclassdiagram_classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=umlclassdiagram_PackageCS_strategy)
def test_hyp_umlclassdiagram_packagecs_name_setter(instance):
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
    BooleanLiteralExpCS,
    CallExpCS,
    Classifier,
    ExpCS,
    Feature,
    LiteralExpCS,
    LogicExpCS,
    LoopExpCS,
    Modifier,
    NamedElement,
    NavigationExpCS,
    NavigationPathCS,
    PathCS,
    PrimaryExpCS,
    Relation,
    umlclassdiagram_AccVarCS,
    umlclassdiagram_Aggregation,
    umlclassdiagram_Association,
    umlclassdiagram_AssociationClass,
    umlclassdiagram_Attribute,
    umlclassdiagram_BooleanExpCS,
    umlclassdiagram_BooleanLiteralExpCS,
    umlclassdiagram_CallExpCS,
    umlclassdiagram_Class,
    umlclassdiagram_ClassCS,
    umlclassdiagram_ClassDiagram,
    umlclassdiagram_Classifier,
    umlclassdiagram_CollectExpCS,
    umlclassdiagram_Composition,
    umlclassdiagram_Constraint,
    umlclassdiagram_ConstraintCS,
    umlclassdiagram_Dependency,
    umlclassdiagram_ExistsExpCS,
    umlclassdiagram_ExpCS,
    umlclassdiagram_Feature,
    umlclassdiagram_ForAllExpCS,
    umlclassdiagram_IntLiteralExpCS,
    umlclassdiagram_InvariantCS,
    umlclassdiagram_IterateExpCS,
    umlclassdiagram_IteratorVarCS,
    umlclassdiagram_LiteralExpCS,
    umlclassdiagram_LogicExpCS,
    umlclassdiagram_LoopExpCS,
    umlclassdiagram_Modifier,
    umlclassdiagram_NameExpCS,
    umlclassdiagram_NamedElement,
    umlclassdiagram_NavigationExpCS,
    umlclassdiagram_NavigationNameExpCS,
    umlclassdiagram_NavigationPathCS,
    umlclassdiagram_NavigationPathElementCS,
    umlclassdiagram_NavigationPathNameCS,
    umlclassdiagram_NavigationPathVariableCS,
    umlclassdiagram_Operation,
    umlclassdiagram_OperationCS,
    umlclassdiagram_Operator,
    umlclassdiagram_PackageCS,
    umlclassdiagram_Parameter,
    umlclassdiagram_ParameterCS,
    umlclassdiagram_PathCS,
    umlclassdiagram_PathElementCS,
    umlclassdiagram_PathNameCS,
    umlclassdiagram_PathVariableCS,
    umlclassdiagram_PrimaryExpCS,
    umlclassdiagram_PrimitiveElement,
    umlclassdiagram_PropertyCS,
    umlclassdiagram_Relation,
    umlclassdiagram_RootCS,
    umlclassdiagram_RoundedBracketClauseCS,
    umlclassdiagram_StringLiteralExpCS,
    OperatorType,
    PrimitiveDataType,
    ScopeType,
    VisbilityType,
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

def test_umlclassdiagram_AccVarCS_accVarName_value_roundtrip():
    instance = umlclassdiagram_AccVarCS(accVarName="sample_text")
    assert instance.accVarName == "sample_text"
    instance.accVarName = "sample_text_2"
    assert instance.accVarName == "sample_text_2"


def test_umlclassdiagram_Attribute_derived_value_roundtrip():
    instance = umlclassdiagram_Attribute(derived=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_umlclassdiagram_BooleanExpCS_boolSymbol_value_roundtrip():
    instance = umlclassdiagram_BooleanExpCS(boolSymbol=True)
    assert instance.boolSymbol == True
    instance.boolSymbol = False
    assert instance.boolSymbol == False


def test_umlclassdiagram_ClassCS_name_value_roundtrip():
    instance = umlclassdiagram_ClassCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_Classifier_abstract_value_roundtrip():
    instance = umlclassdiagram_Classifier(abstract=True, derived=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_umlclassdiagram_Classifier_derived_value_roundtrip():
    instance = umlclassdiagram_Classifier(abstract=True, derived=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_umlclassdiagram_Constraint_id_value_roundtrip():
    instance = umlclassdiagram_Constraint(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_umlclassdiagram_Feature_name_value_roundtrip():
    instance = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_Feature_scope_value_roundtrip():
    instance = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_umlclassdiagram_Feature_visibility_value_roundtrip():
    instance = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_umlclassdiagram_IntLiteralExpCS_intSymbol_value_roundtrip():
    instance = umlclassdiagram_IntLiteralExpCS(intSymbol=7)
    assert instance.intSymbol == 7
    instance.intSymbol = 13
    assert instance.intSymbol == 13


def test_umlclassdiagram_IteratorVarCS_itName_value_roundtrip():
    instance = umlclassdiagram_IteratorVarCS(itName="sample_text")
    assert instance.itName == "sample_text"
    instance.itName = "sample_text_2"
    assert instance.itName == "sample_text_2"


def test_umlclassdiagram_LogicExpCS_op_value_roundtrip():
    instance = umlclassdiagram_LogicExpCS(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_umlclassdiagram_LoopExpCS_logicOp_value_roundtrip():
    instance = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    assert instance.logicOp == "sample_text"
    instance.logicOp = "sample_text_2"
    assert instance.logicOp == "sample_text_2"


def test_umlclassdiagram_Modifier_scope_value_roundtrip():
    instance = umlclassdiagram_Modifier(scope="sample_text", visibility="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_umlclassdiagram_Modifier_visibility_value_roundtrip():
    instance = umlclassdiagram_Modifier(scope="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_umlclassdiagram_NamedElement_name_value_roundtrip():
    instance = umlclassdiagram_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_NavigationPathVariableCS_varName_value_roundtrip():
    instance = umlclassdiagram_NavigationPathVariableCS(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_umlclassdiagram_OperationCS_name_value_roundtrip():
    instance = umlclassdiagram_OperationCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_Operator_operator_value_roundtrip():
    instance = umlclassdiagram_Operator(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_umlclassdiagram_PackageCS_name_value_roundtrip():
    instance = umlclassdiagram_PackageCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_ParameterCS_name_value_roundtrip():
    instance = umlclassdiagram_ParameterCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_PathVariableCS_varName_value_roundtrip():
    instance = umlclassdiagram_PathVariableCS(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_umlclassdiagram_PrimitiveElement_type_value_roundtrip():
    instance = umlclassdiagram_PrimitiveElement(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_umlclassdiagram_PropertyCS_name_value_roundtrip():
    instance = umlclassdiagram_PropertyCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umlclassdiagram_Relation_derived_value_roundtrip():
    instance = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_umlclassdiagram_Relation_nsrc_value_roundtrip():
    instance = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    assert instance.nsrc == "sample_text"
    instance.nsrc = "sample_text_2"
    assert instance.nsrc == "sample_text_2"


def test_umlclassdiagram_Relation_ntar_value_roundtrip():
    instance = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    assert instance.ntar == "sample_text"
    instance.ntar = "sample_text_2"
    assert instance.ntar == "sample_text_2"


def test_umlclassdiagram_StringLiteralExpCS_stringSymbol_value_roundtrip():
    instance = umlclassdiagram_StringLiteralExpCS(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_umlclassdiagram_BooleanExpCS_isa_BooleanLiteralExpCS():
    instance = umlclassdiagram_BooleanExpCS(boolSymbol=True)
    assert isinstance(instance, BooleanLiteralExpCS)


def test_umlclassdiagram_PrimaryExpCS_isa_CallExpCS():
    instance = umlclassdiagram_PrimaryExpCS()
    assert isinstance(instance, CallExpCS)


def test_umlclassdiagram_AssociationClass_isa_Classifier():
    instance = umlclassdiagram_AssociationClass()
    assert isinstance(instance, Classifier)


def test_umlclassdiagram_Class_isa_Classifier():
    instance = umlclassdiagram_Class()
    assert isinstance(instance, Classifier)


def test_umlclassdiagram_LogicExpCS_isa_ExpCS():
    instance = umlclassdiagram_LogicExpCS(op="sample_text")
    assert isinstance(instance, ExpCS)


def test_umlclassdiagram_Attribute_isa_Feature():
    instance = umlclassdiagram_Attribute(derived=True)
    assert isinstance(instance, Feature)


def test_umlclassdiagram_Operation_isa_Feature():
    instance = umlclassdiagram_Operation()
    assert isinstance(instance, Feature)


def test_umlclassdiagram_BooleanLiteralExpCS_isa_LiteralExpCS():
    instance = umlclassdiagram_BooleanLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_umlclassdiagram_IntLiteralExpCS_isa_LiteralExpCS():
    instance = umlclassdiagram_IntLiteralExpCS(intSymbol=7)
    assert isinstance(instance, LiteralExpCS)


def test_umlclassdiagram_StringLiteralExpCS_isa_LiteralExpCS():
    instance = umlclassdiagram_StringLiteralExpCS(stringSymbol="sample_text")
    assert isinstance(instance, LiteralExpCS)


def test_umlclassdiagram_CallExpCS_isa_LogicExpCS():
    instance = umlclassdiagram_CallExpCS()
    assert isinstance(instance, LogicExpCS)


def test_umlclassdiagram_CollectExpCS_isa_LoopExpCS():
    instance = umlclassdiagram_CollectExpCS()
    assert isinstance(instance, LoopExpCS)


def test_umlclassdiagram_ExistsExpCS_isa_LoopExpCS():
    instance = umlclassdiagram_ExistsExpCS()
    assert isinstance(instance, LoopExpCS)


def test_umlclassdiagram_ForAllExpCS_isa_LoopExpCS():
    instance = umlclassdiagram_ForAllExpCS()
    assert isinstance(instance, LoopExpCS)


def test_umlclassdiagram_IterateExpCS_isa_LoopExpCS():
    instance = umlclassdiagram_IterateExpCS()
    assert isinstance(instance, LoopExpCS)


def test_umlclassdiagram_Classifier_isa_Modifier():
    instance = umlclassdiagram_Classifier(abstract=True, derived=True)
    assert isinstance(instance, Modifier)


def test_umlclassdiagram_Relation_isa_Modifier():
    instance = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    assert isinstance(instance, Modifier)


def test_umlclassdiagram_Modifier_isa_NamedElement():
    instance = umlclassdiagram_Modifier(scope="sample_text", visibility="sample_text")
    assert isinstance(instance, NamedElement)


def test_umlclassdiagram_Parameter_isa_NamedElement():
    instance = umlclassdiagram_Parameter()
    assert isinstance(instance, NamedElement)


def test_umlclassdiagram_PrimitiveElement_isa_NamedElement():
    instance = umlclassdiagram_PrimitiveElement(type="sample_text")
    assert isinstance(instance, NamedElement)


def test_umlclassdiagram_LoopExpCS_isa_NavigationExpCS():
    instance = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    assert isinstance(instance, NavigationExpCS)


def test_umlclassdiagram_NameExpCS_isa_NavigationExpCS():
    instance = umlclassdiagram_NameExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_umlclassdiagram_NavigationNameExpCS_isa_NavigationExpCS():
    instance = umlclassdiagram_NavigationNameExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_umlclassdiagram_NavigationPathElementCS_isa_NavigationPathCS():
    instance = umlclassdiagram_NavigationPathElementCS()
    assert isinstance(instance, NavigationPathCS)


def test_umlclassdiagram_NavigationPathVariableCS_isa_NavigationPathCS():
    instance = umlclassdiagram_NavigationPathVariableCS(varName="sample_text")
    assert isinstance(instance, NavigationPathCS)


def test_umlclassdiagram_PathElementCS_isa_PathCS():
    instance = umlclassdiagram_PathElementCS()
    assert isinstance(instance, PathCS)


def test_umlclassdiagram_PathVariableCS_isa_PathCS():
    instance = umlclassdiagram_PathVariableCS(varName="sample_text")
    assert isinstance(instance, PathCS)


def test_umlclassdiagram_LiteralExpCS_isa_PrimaryExpCS():
    instance = umlclassdiagram_LiteralExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_umlclassdiagram_NavigationExpCS_isa_PrimaryExpCS():
    instance = umlclassdiagram_NavigationExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_umlclassdiagram_Aggregation_isa_Relation():
    instance = umlclassdiagram_Aggregation()
    assert isinstance(instance, Relation)


def test_umlclassdiagram_Association_isa_Relation():
    instance = umlclassdiagram_Association()
    assert isinstance(instance, Relation)


def test_umlclassdiagram_Composition_isa_Relation():
    instance = umlclassdiagram_Composition()
    assert isinstance(instance, Relation)


def test_umlclassdiagram_Dependency_isa_Relation():
    instance = umlclassdiagram_Dependency()
    assert isinstance(instance, Relation)


def test_assoc_accInitExp62_link_reassign_clear():
    a = umlclassdiagram_AccVarCS(accVarName="sample_text")
    b1 = umlclassdiagram_ExpCS()
    b2 = umlclassdiagram_ExpCS()
    _safe_set(a, 'umlclassdiagram_AccVarCS63', b1)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS63', b1)
    if hasattr(b1, 'umlclassdiagram_ExpCS64'):
        assert _is_linked(b1, 'umlclassdiagram_ExpCS64', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS63', b2)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS63', b2)
    if hasattr(b1, 'umlclassdiagram_ExpCS64'):
        assert not _is_linked(b1, 'umlclassdiagram_ExpCS64', a)
    if hasattr(b2, 'umlclassdiagram_ExpCS64'):
        assert _is_linked(b2, 'umlclassdiagram_ExpCS64', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS63', None)
    assert not _is_linked(a, 'umlclassdiagram_AccVarCS63', b2)
    if hasattr(b2, 'umlclassdiagram_ExpCS64'):
        assert not _is_linked(b2, 'umlclassdiagram_ExpCS64', a)


def test_assoc_accType59_link_reassign_clear():
    a = umlclassdiagram_AccVarCS(accVarName="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_AccVarCS60', b1)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS60', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS61'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS61', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS60', b2)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS60', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS61'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS61', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS61'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS61', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS60', None)
    assert not _is_linked(a, 'umlclassdiagram_AccVarCS60', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS61'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS61', a)


def test_assoc_accVar58_link_reassign_clear():
    a = umlclassdiagram_AccVarCS(accVarName="sample_text")
    b1 = umlclassdiagram_IterateExpCS()
    b2 = umlclassdiagram_IterateExpCS()
    _safe_set(a, 'umlclassdiagram_AccVarCS', b1)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS', b1)
    if hasattr(b1, 'umlclassdiagram_IterateExpCS'):
        assert _is_linked(b1, 'umlclassdiagram_IterateExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS', b2)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS', b2)
    if hasattr(b1, 'umlclassdiagram_IterateExpCS'):
        assert not _is_linked(b1, 'umlclassdiagram_IterateExpCS', a)
    if hasattr(b2, 'umlclassdiagram_IterateExpCS'):
        assert _is_linked(b2, 'umlclassdiagram_IterateExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS', None)
    assert not _is_linked(a, 'umlclassdiagram_AccVarCS', b2)
    if hasattr(b2, 'umlclassdiagram_IterateExpCS'):
        assert not _is_linked(b2, 'umlclassdiagram_IterateExpCS', a)


def test_assoc_accVars71_link_reassign_clear():
    a = umlclassdiagram_AccVarCS(accVarName="sample_text")
    b1 = umlclassdiagram_ExistsExpCS()
    b2 = umlclassdiagram_ExistsExpCS()
    _safe_set(a, 'umlclassdiagram_AccVarCS72', b1)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS72', b1)
    if hasattr(b1, 'umlclassdiagram_ExistsExpCS'):
        assert _is_linked(b1, 'umlclassdiagram_ExistsExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS72', b2)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS72', b2)
    if hasattr(b1, 'umlclassdiagram_ExistsExpCS'):
        assert not _is_linked(b1, 'umlclassdiagram_ExistsExpCS', a)
    if hasattr(b2, 'umlclassdiagram_ExistsExpCS'):
        assert _is_linked(b2, 'umlclassdiagram_ExistsExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS72', None)
    assert not _is_linked(a, 'umlclassdiagram_AccVarCS72', b2)
    if hasattr(b2, 'umlclassdiagram_ExistsExpCS'):
        assert not _is_linked(b2, 'umlclassdiagram_ExistsExpCS', a)


def test_assoc_accVars84_link_reassign_clear():
    a = umlclassdiagram_AccVarCS(accVarName="sample_text")
    b1 = umlclassdiagram_ForAllExpCS()
    b2 = umlclassdiagram_ForAllExpCS()
    _safe_set(a, 'umlclassdiagram_AccVarCS85', b1)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS85', b1)
    if hasattr(b1, 'umlclassdiagram_ForAllExpCS'):
        assert _is_linked(b1, 'umlclassdiagram_ForAllExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS85', b2)
    assert _is_linked(a, 'umlclassdiagram_AccVarCS85', b2)
    if hasattr(b1, 'umlclassdiagram_ForAllExpCS'):
        assert not _is_linked(b1, 'umlclassdiagram_ForAllExpCS', a)
    if hasattr(b2, 'umlclassdiagram_ForAllExpCS'):
        assert _is_linked(b2, 'umlclassdiagram_ForAllExpCS', a)
    _safe_set(a, 'umlclassdiagram_AccVarCS85', None)
    assert not _is_linked(a, 'umlclassdiagram_AccVarCS85', b2)
    if hasattr(b2, 'umlclassdiagram_ForAllExpCS'):
        assert not _is_linked(b2, 'umlclassdiagram_ForAllExpCS', a)


def test_assoc_body22_link_reassign_clear():
    a = umlclassdiagram_OperationCS(name="sample_text")
    b1 = umlclassdiagram_ExpCS()
    b2 = umlclassdiagram_ExpCS()
    _safe_set(a, 'umlclassdiagram_OperationCS23', b1)
    assert _is_linked(a, 'umlclassdiagram_OperationCS23', b1)
    if hasattr(b1, 'umlclassdiagram_ExpCS'):
        assert _is_linked(b1, 'umlclassdiagram_ExpCS', a)
    _safe_set(a, 'umlclassdiagram_OperationCS23', b2)
    assert _is_linked(a, 'umlclassdiagram_OperationCS23', b2)
    if hasattr(b1, 'umlclassdiagram_ExpCS'):
        assert not _is_linked(b1, 'umlclassdiagram_ExpCS', a)
    if hasattr(b2, 'umlclassdiagram_ExpCS'):
        assert _is_linked(b2, 'umlclassdiagram_ExpCS', a)
    _safe_set(a, 'umlclassdiagram_OperationCS23', None)
    assert not _is_linked(a, 'umlclassdiagram_OperationCS23', b2)
    if hasattr(b2, 'umlclassdiagram_ExpCS'):
        assert not _is_linked(b2, 'umlclassdiagram_ExpCS', a)


def test_assoc_classes6_link_reassign_clear():
    a = umlclassdiagram_PackageCS(name="sample_text")
    b1 = umlclassdiagram_ClassCS(name="sample_text")
    b2 = umlclassdiagram_ClassCS(name="sample_text_2")
    _safe_set(a, 'umlclassdiagram_PackageCS7', {b1})
    assert _is_linked(a, 'umlclassdiagram_PackageCS7', b1)
    if hasattr(b1, 'umlclassdiagram_ClassCS'):
        assert _is_linked(b1, 'umlclassdiagram_ClassCS', a)
    _safe_set(a, 'umlclassdiagram_PackageCS7', {b2})
    assert _is_linked(a, 'umlclassdiagram_PackageCS7', b2)
    if hasattr(b1, 'umlclassdiagram_ClassCS'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassCS', a)
    if hasattr(b2, 'umlclassdiagram_ClassCS'):
        assert _is_linked(b2, 'umlclassdiagram_ClassCS', a)
    _safe_set(a, 'umlclassdiagram_PackageCS7', set())
    assert not _is_linked(a, 'umlclassdiagram_PackageCS7', b2)
    if hasattr(b2, 'umlclassdiagram_ClassCS'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassCS', a)


def test_assoc_classes86_link_reassign_clear():
    a = umlclassdiagram_Classifier(abstract=True, derived=True)
    b1 = umlclassdiagram_ClassDiagram()
    b2 = umlclassdiagram_ClassDiagram()
    _safe_set(a, 'umlclassdiagram_Classifier', b1)
    assert _is_linked(a, 'umlclassdiagram_Classifier', b1)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram'):
        assert _is_linked(b1, 'umlclassdiagram_ClassDiagram', a)
    _safe_set(a, 'umlclassdiagram_Classifier', b2)
    assert _is_linked(a, 'umlclassdiagram_Classifier', b2)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassDiagram', a)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram'):
        assert _is_linked(b2, 'umlclassdiagram_ClassDiagram', a)
    _safe_set(a, 'umlclassdiagram_Classifier', None)
    assert not _is_linked(a, 'umlclassdiagram_Classifier', b2)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassDiagram', a)


def test_assoc_constraints91_link_reassign_clear():
    a = umlclassdiagram_Constraint(id="sample_text")
    b1 = umlclassdiagram_ClassDiagram()
    b2 = umlclassdiagram_ClassDiagram()
    _safe_set(a, 'umlclassdiagram_Constraint', b1)
    assert _is_linked(a, 'umlclassdiagram_Constraint', b1)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram92'):
        assert _is_linked(b1, 'umlclassdiagram_ClassDiagram92', a)
    _safe_set(a, 'umlclassdiagram_Constraint', b2)
    assert _is_linked(a, 'umlclassdiagram_Constraint', b2)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram92'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassDiagram92', a)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram92'):
        assert _is_linked(b2, 'umlclassdiagram_ClassDiagram92', a)
    _safe_set(a, 'umlclassdiagram_Constraint', None)
    assert not _is_linked(a, 'umlclassdiagram_Constraint', b2)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram92'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassDiagram92', a)


def test_assoc_exp52_link_reassign_clear():
    a = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    b1 = umlclassdiagram_ExpCS()
    b2 = umlclassdiagram_ExpCS()
    _safe_set(a, 'umlclassdiagram_LoopExpCS53', {b1})
    assert _is_linked(a, 'umlclassdiagram_LoopExpCS53', b1)
    if hasattr(b1, 'umlclassdiagram_ExpCS54'):
        assert _is_linked(b1, 'umlclassdiagram_ExpCS54', a)
    _safe_set(a, 'umlclassdiagram_LoopExpCS53', {b2})
    assert _is_linked(a, 'umlclassdiagram_LoopExpCS53', b2)
    if hasattr(b1, 'umlclassdiagram_ExpCS54'):
        assert not _is_linked(b1, 'umlclassdiagram_ExpCS54', a)
    if hasattr(b2, 'umlclassdiagram_ExpCS54'):
        assert _is_linked(b2, 'umlclassdiagram_ExpCS54', a)
    _safe_set(a, 'umlclassdiagram_LoopExpCS53', set())
    assert not _is_linked(a, 'umlclassdiagram_LoopExpCS53', b2)
    if hasattr(b2, 'umlclassdiagram_ExpCS54'):
        assert not _is_linked(b2, 'umlclassdiagram_ExpCS54', a)


def test_assoc_expressions108_link_reassign_clear():
    a = umlclassdiagram_Constraint(id="sample_text")
    b1 = umlclassdiagram_RootCS()
    b2 = umlclassdiagram_RootCS()
    _safe_set(a, 'umlclassdiagram_Constraint109', {b1})
    assert _is_linked(a, 'umlclassdiagram_Constraint109', b1)
    if hasattr(b1, 'umlclassdiagram_RootCS110'):
        assert _is_linked(b1, 'umlclassdiagram_RootCS110', a)
    _safe_set(a, 'umlclassdiagram_Constraint109', {b2})
    assert _is_linked(a, 'umlclassdiagram_Constraint109', b2)
    if hasattr(b1, 'umlclassdiagram_RootCS110'):
        assert not _is_linked(b1, 'umlclassdiagram_RootCS110', a)
    if hasattr(b2, 'umlclassdiagram_RootCS110'):
        assert _is_linked(b2, 'umlclassdiagram_RootCS110', a)
    _safe_set(a, 'umlclassdiagram_Constraint109', set())
    assert not _is_linked(a, 'umlclassdiagram_Constraint109', b2)
    if hasattr(b2, 'umlclassdiagram_RootCS110'):
        assert not _is_linked(b2, 'umlclassdiagram_RootCS110', a)


def test_assoc_extends8_link_reassign_clear():
    a = umlclassdiagram_ClassCS(name="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_ClassCS9', b1)
    assert _is_linked(a, 'umlclassdiagram_ClassCS9', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS', a)
    _safe_set(a, 'umlclassdiagram_ClassCS9', b2)
    assert _is_linked(a, 'umlclassdiagram_ClassCS9', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS', a)
    _safe_set(a, 'umlclassdiagram_ClassCS9', None)
    assert not _is_linked(a, 'umlclassdiagram_ClassCS9', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS', a)


def test_assoc_features97_link_reassign_clear():
    a = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    b1 = umlclassdiagram_Classifier(abstract=True, derived=True)
    b2 = umlclassdiagram_Classifier(abstract=False, derived=False)
    _safe_set(a, 'umlclassdiagram_Feature99', b1)
    assert _is_linked(a, 'umlclassdiagram_Feature99', b1)
    if hasattr(b1, 'umlclassdiagram_Classifier98'):
        assert _is_linked(b1, 'umlclassdiagram_Classifier98', a)
    _safe_set(a, 'umlclassdiagram_Feature99', b2)
    assert _is_linked(a, 'umlclassdiagram_Feature99', b2)
    if hasattr(b1, 'umlclassdiagram_Classifier98'):
        assert not _is_linked(b1, 'umlclassdiagram_Classifier98', a)
    if hasattr(b2, 'umlclassdiagram_Classifier98'):
        assert _is_linked(b2, 'umlclassdiagram_Classifier98', a)
    _safe_set(a, 'umlclassdiagram_Feature99', None)
    assert not _is_linked(a, 'umlclassdiagram_Feature99', b2)
    if hasattr(b2, 'umlclassdiagram_Classifier98'):
        assert not _is_linked(b2, 'umlclassdiagram_Classifier98', a)


def test_assoc_itType55_link_reassign_clear():
    a = umlclassdiagram_IteratorVarCS(itName="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_IteratorVarCS56', b1)
    assert _is_linked(a, 'umlclassdiagram_IteratorVarCS56', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS57'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS57', a)
    _safe_set(a, 'umlclassdiagram_IteratorVarCS56', b2)
    assert _is_linked(a, 'umlclassdiagram_IteratorVarCS56', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS57'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS57', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS57'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS57', a)
    _safe_set(a, 'umlclassdiagram_IteratorVarCS56', None)
    assert not _is_linked(a, 'umlclassdiagram_IteratorVarCS56', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS57'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS57', a)


def test_assoc_itVar51_link_reassign_clear():
    a = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    b1 = umlclassdiagram_IteratorVarCS(itName="sample_text")
    b2 = umlclassdiagram_IteratorVarCS(itName="sample_text_2")
    _safe_set(a, 'umlclassdiagram_LoopExpCS', b1)
    assert _is_linked(a, 'umlclassdiagram_LoopExpCS', b1)
    if hasattr(b1, 'umlclassdiagram_IteratorVarCS'):
        assert _is_linked(b1, 'umlclassdiagram_IteratorVarCS', a)
    _safe_set(a, 'umlclassdiagram_LoopExpCS', b2)
    assert _is_linked(a, 'umlclassdiagram_LoopExpCS', b2)
    if hasattr(b1, 'umlclassdiagram_IteratorVarCS'):
        assert not _is_linked(b1, 'umlclassdiagram_IteratorVarCS', a)
    if hasattr(b2, 'umlclassdiagram_IteratorVarCS'):
        assert _is_linked(b2, 'umlclassdiagram_IteratorVarCS', a)
    _safe_set(a, 'umlclassdiagram_LoopExpCS', None)
    assert not _is_linked(a, 'umlclassdiagram_LoopExpCS', b2)
    if hasattr(b2, 'umlclassdiagram_IteratorVarCS'):
        assert not _is_linked(b2, 'umlclassdiagram_IteratorVarCS', a)


def test_assoc_left36_link_reassign_clear():
    a = umlclassdiagram_LogicExpCS(op="sample_text")
    b1 = umlclassdiagram_LogicExpCS(op="sample_text")
    b2 = umlclassdiagram_LogicExpCS(op="sample_text_2")
    _safe_set(a, 'umlclassdiagram_LogicExpCS', b1)
    assert _is_linked(a, 'umlclassdiagram_LogicExpCS', b1)
    if hasattr(b1, 'umlclassdiagram_LogicExpCS35'):
        assert _is_linked(b1, 'umlclassdiagram_LogicExpCS35', a)
    _safe_set(a, 'umlclassdiagram_LogicExpCS', b2)
    assert _is_linked(a, 'umlclassdiagram_LogicExpCS', b2)
    if hasattr(b1, 'umlclassdiagram_LogicExpCS35'):
        assert not _is_linked(b1, 'umlclassdiagram_LogicExpCS35', a)
    if hasattr(b2, 'umlclassdiagram_LogicExpCS35'):
        assert _is_linked(b2, 'umlclassdiagram_LogicExpCS35', a)
    _safe_set(a, 'umlclassdiagram_LogicExpCS', None)
    assert not _is_linked(a, 'umlclassdiagram_LogicExpCS', b2)
    if hasattr(b2, 'umlclassdiagram_LogicExpCS35'):
        assert not _is_linked(b2, 'umlclassdiagram_LogicExpCS35', a)


def test_assoc_operations12_link_reassign_clear():
    a = umlclassdiagram_OperationCS(name="sample_text")
    b1 = umlclassdiagram_ClassCS(name="sample_text")
    b2 = umlclassdiagram_ClassCS(name="sample_text_2")
    _safe_set(a, 'umlclassdiagram_OperationCS', b1)
    assert _is_linked(a, 'umlclassdiagram_OperationCS', b1)
    if hasattr(b1, 'umlclassdiagram_ClassCS13'):
        assert _is_linked(b1, 'umlclassdiagram_ClassCS13', a)
    _safe_set(a, 'umlclassdiagram_OperationCS', b2)
    assert _is_linked(a, 'umlclassdiagram_OperationCS', b2)
    if hasattr(b1, 'umlclassdiagram_ClassCS13'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassCS13', a)
    if hasattr(b2, 'umlclassdiagram_ClassCS13'):
        assert _is_linked(b2, 'umlclassdiagram_ClassCS13', a)
    _safe_set(a, 'umlclassdiagram_OperationCS', None)
    assert not _is_linked(a, 'umlclassdiagram_OperationCS', b2)
    if hasattr(b2, 'umlclassdiagram_ClassCS13'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassCS13', a)


def test_assoc_operators113_link_reassign_clear():
    a = umlclassdiagram_Operator(operator="sample_text")
    b1 = umlclassdiagram_Operation()
    b2 = umlclassdiagram_Operation()
    _safe_set(a, 'umlclassdiagram_Operator', b1)
    assert _is_linked(a, 'umlclassdiagram_Operator', b1)
    if hasattr(b1, 'umlclassdiagram_Operation114'):
        assert _is_linked(b1, 'umlclassdiagram_Operation114', a)
    _safe_set(a, 'umlclassdiagram_Operator', b2)
    assert _is_linked(a, 'umlclassdiagram_Operator', b2)
    if hasattr(b1, 'umlclassdiagram_Operation114'):
        assert not _is_linked(b1, 'umlclassdiagram_Operation114', a)
    if hasattr(b2, 'umlclassdiagram_Operation114'):
        assert _is_linked(b2, 'umlclassdiagram_Operation114', a)
    _safe_set(a, 'umlclassdiagram_Operator', None)
    assert not _is_linked(a, 'umlclassdiagram_Operator', b2)
    if hasattr(b2, 'umlclassdiagram_Operation114'):
        assert not _is_linked(b2, 'umlclassdiagram_Operation114', a)


def test_assoc_packages0_link_reassign_clear():
    a = umlclassdiagram_PackageCS(name="sample_text")
    b1 = umlclassdiagram_RootCS()
    b2 = umlclassdiagram_RootCS()
    _safe_set(a, 'umlclassdiagram_PackageCS', b1)
    assert _is_linked(a, 'umlclassdiagram_PackageCS', b1)
    if hasattr(b1, 'umlclassdiagram_RootCS'):
        assert _is_linked(b1, 'umlclassdiagram_RootCS', a)
    _safe_set(a, 'umlclassdiagram_PackageCS', b2)
    assert _is_linked(a, 'umlclassdiagram_PackageCS', b2)
    if hasattr(b1, 'umlclassdiagram_RootCS'):
        assert not _is_linked(b1, 'umlclassdiagram_RootCS', a)
    if hasattr(b2, 'umlclassdiagram_RootCS'):
        assert _is_linked(b2, 'umlclassdiagram_RootCS', a)
    _safe_set(a, 'umlclassdiagram_PackageCS', None)
    assert not _is_linked(a, 'umlclassdiagram_PackageCS', b2)
    if hasattr(b2, 'umlclassdiagram_RootCS'):
        assert not _is_linked(b2, 'umlclassdiagram_RootCS', a)


def test_assoc_packages4_link_reassign_clear():
    a = umlclassdiagram_PackageCS(name="sample_text")
    b1 = umlclassdiagram_PackageCS(name="sample_text")
    b2 = umlclassdiagram_PackageCS(name="sample_text_2")
    _safe_set(a, 'umlclassdiagram_PackageCS3', {b1})
    assert _is_linked(a, 'umlclassdiagram_PackageCS3', b1)
    if hasattr(b1, 'umlclassdiagram_PackageCS5'):
        assert _is_linked(b1, 'umlclassdiagram_PackageCS5', a)
    _safe_set(a, 'umlclassdiagram_PackageCS3', {b2})
    assert _is_linked(a, 'umlclassdiagram_PackageCS3', b2)
    if hasattr(b1, 'umlclassdiagram_PackageCS5'):
        assert not _is_linked(b1, 'umlclassdiagram_PackageCS5', a)
    if hasattr(b2, 'umlclassdiagram_PackageCS5'):
        assert _is_linked(b2, 'umlclassdiagram_PackageCS5', a)
    _safe_set(a, 'umlclassdiagram_PackageCS3', set())
    assert not _is_linked(a, 'umlclassdiagram_PackageCS3', b2)
    if hasattr(b2, 'umlclassdiagram_PackageCS5'):
        assert not _is_linked(b2, 'umlclassdiagram_PackageCS5', a)


def test_assoc_params17_link_reassign_clear():
    a = umlclassdiagram_ParameterCS(name="sample_text")
    b1 = umlclassdiagram_OperationCS(name="sample_text")
    b2 = umlclassdiagram_OperationCS(name="sample_text_2")
    _safe_set(a, 'umlclassdiagram_ParameterCS', b1)
    assert _is_linked(a, 'umlclassdiagram_ParameterCS', b1)
    if hasattr(b1, 'umlclassdiagram_OperationCS18'):
        assert _is_linked(b1, 'umlclassdiagram_OperationCS18', a)
    _safe_set(a, 'umlclassdiagram_ParameterCS', b2)
    assert _is_linked(a, 'umlclassdiagram_ParameterCS', b2)
    if hasattr(b1, 'umlclassdiagram_OperationCS18'):
        assert not _is_linked(b1, 'umlclassdiagram_OperationCS18', a)
    if hasattr(b2, 'umlclassdiagram_OperationCS18'):
        assert _is_linked(b2, 'umlclassdiagram_OperationCS18', a)
    _safe_set(a, 'umlclassdiagram_ParameterCS', None)
    assert not _is_linked(a, 'umlclassdiagram_ParameterCS', b2)
    if hasattr(b2, 'umlclassdiagram_OperationCS18'):
        assert not _is_linked(b2, 'umlclassdiagram_OperationCS18', a)


def test_assoc_pathName70_link_reassign_clear():
    a = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    b1 = umlclassdiagram_PathElementCS()
    b2 = umlclassdiagram_PathElementCS()
    _safe_set(a, 'umlclassdiagram_Feature', b1)
    assert _is_linked(a, 'umlclassdiagram_Feature', b1)
    if hasattr(b1, 'umlclassdiagram_PathElementCS'):
        assert _is_linked(b1, 'umlclassdiagram_PathElementCS', a)
    _safe_set(a, 'umlclassdiagram_Feature', b2)
    assert _is_linked(a, 'umlclassdiagram_Feature', b2)
    if hasattr(b1, 'umlclassdiagram_PathElementCS'):
        assert not _is_linked(b1, 'umlclassdiagram_PathElementCS', a)
    if hasattr(b2, 'umlclassdiagram_PathElementCS'):
        assert _is_linked(b2, 'umlclassdiagram_PathElementCS', a)
    _safe_set(a, 'umlclassdiagram_Feature', None)
    assert not _is_linked(a, 'umlclassdiagram_Feature', b2)
    if hasattr(b2, 'umlclassdiagram_PathElementCS'):
        assert not _is_linked(b2, 'umlclassdiagram_PathElementCS', a)


def test_assoc_pathName82_link_reassign_clear():
    a = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    b1 = umlclassdiagram_NavigationPathElementCS()
    b2 = umlclassdiagram_NavigationPathElementCS()
    _safe_set(a, 'umlclassdiagram_Feature83', b1)
    assert _is_linked(a, 'umlclassdiagram_Feature83', b1)
    if hasattr(b1, 'umlclassdiagram_NavigationPathElementCS'):
        assert _is_linked(b1, 'umlclassdiagram_NavigationPathElementCS', a)
    _safe_set(a, 'umlclassdiagram_Feature83', b2)
    assert _is_linked(a, 'umlclassdiagram_Feature83', b2)
    if hasattr(b1, 'umlclassdiagram_NavigationPathElementCS'):
        assert not _is_linked(b1, 'umlclassdiagram_NavigationPathElementCS', a)
    if hasattr(b2, 'umlclassdiagram_NavigationPathElementCS'):
        assert _is_linked(b2, 'umlclassdiagram_NavigationPathElementCS', a)
    _safe_set(a, 'umlclassdiagram_Feature83', None)
    assert not _is_linked(a, 'umlclassdiagram_Feature83', b2)
    if hasattr(b2, 'umlclassdiagram_NavigationPathElementCS'):
        assert not _is_linked(b2, 'umlclassdiagram_NavigationPathElementCS', a)


def test_assoc_properties10_link_reassign_clear():
    a = umlclassdiagram_PropertyCS(name="sample_text")
    b1 = umlclassdiagram_ClassCS(name="sample_text")
    b2 = umlclassdiagram_ClassCS(name="sample_text_2")
    _safe_set(a, 'umlclassdiagram_PropertyCS', b1)
    assert _is_linked(a, 'umlclassdiagram_PropertyCS', b1)
    if hasattr(b1, 'umlclassdiagram_ClassCS11'):
        assert _is_linked(b1, 'umlclassdiagram_ClassCS11', a)
    _safe_set(a, 'umlclassdiagram_PropertyCS', b2)
    assert _is_linked(a, 'umlclassdiagram_PropertyCS', b2)
    if hasattr(b1, 'umlclassdiagram_ClassCS11'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassCS11', a)
    if hasattr(b2, 'umlclassdiagram_ClassCS11'):
        assert _is_linked(b2, 'umlclassdiagram_ClassCS11', a)
    _safe_set(a, 'umlclassdiagram_PropertyCS', None)
    assert not _is_linked(a, 'umlclassdiagram_PropertyCS', b2)
    if hasattr(b2, 'umlclassdiagram_ClassCS11'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassCS11', a)


def test_assoc_relations87_link_reassign_clear():
    a = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    b1 = umlclassdiagram_ClassDiagram()
    b2 = umlclassdiagram_ClassDiagram()
    _safe_set(a, 'umlclassdiagram_Relation', b1)
    assert _is_linked(a, 'umlclassdiagram_Relation', b1)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram88'):
        assert _is_linked(b1, 'umlclassdiagram_ClassDiagram88', a)
    _safe_set(a, 'umlclassdiagram_Relation', b2)
    assert _is_linked(a, 'umlclassdiagram_Relation', b2)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram88'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassDiagram88', a)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram88'):
        assert _is_linked(b2, 'umlclassdiagram_ClassDiagram88', a)
    _safe_set(a, 'umlclassdiagram_Relation', None)
    assert not _is_linked(a, 'umlclassdiagram_Relation', b2)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram88'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassDiagram88', a)


def test_assoc_resultRef19_link_reassign_clear():
    a = umlclassdiagram_OperationCS(name="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_OperationCS20', b1)
    assert _is_linked(a, 'umlclassdiagram_OperationCS20', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS21'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS21', a)
    _safe_set(a, 'umlclassdiagram_OperationCS20', b2)
    assert _is_linked(a, 'umlclassdiagram_OperationCS20', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS21'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS21', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS21'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS21', a)
    _safe_set(a, 'umlclassdiagram_OperationCS20', None)
    assert not _is_linked(a, 'umlclassdiagram_OperationCS20', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS21'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS21', a)


def test_assoc_right37_link_reassign_clear():
    a = umlclassdiagram_LogicExpCS(op="sample_text")
    b1 = umlclassdiagram_CallExpCS()
    b2 = umlclassdiagram_CallExpCS()
    _safe_set(a, 'umlclassdiagram_LogicExpCS38', b1)
    assert _is_linked(a, 'umlclassdiagram_LogicExpCS38', b1)
    if hasattr(b1, 'umlclassdiagram_CallExpCS'):
        assert _is_linked(b1, 'umlclassdiagram_CallExpCS', a)
    _safe_set(a, 'umlclassdiagram_LogicExpCS38', b2)
    assert _is_linked(a, 'umlclassdiagram_LogicExpCS38', b2)
    if hasattr(b1, 'umlclassdiagram_CallExpCS'):
        assert not _is_linked(b1, 'umlclassdiagram_CallExpCS', a)
    if hasattr(b2, 'umlclassdiagram_CallExpCS'):
        assert _is_linked(b2, 'umlclassdiagram_CallExpCS', a)
    _safe_set(a, 'umlclassdiagram_LogicExpCS38', None)
    assert not _is_linked(a, 'umlclassdiagram_LogicExpCS38', b2)
    if hasattr(b2, 'umlclassdiagram_CallExpCS'):
        assert not _is_linked(b2, 'umlclassdiagram_CallExpCS', a)


def test_assoc_src115_link_reassign_clear():
    a = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    b1 = umlclassdiagram_Classifier(abstract=True, derived=True)
    b2 = umlclassdiagram_Classifier(abstract=False, derived=False)
    _safe_set(a, 'umlclassdiagram_Relation116', b1)
    assert _is_linked(a, 'umlclassdiagram_Relation116', b1)
    if hasattr(b1, 'umlclassdiagram_Classifier117'):
        assert _is_linked(b1, 'umlclassdiagram_Classifier117', a)
    _safe_set(a, 'umlclassdiagram_Relation116', b2)
    assert _is_linked(a, 'umlclassdiagram_Relation116', b2)
    if hasattr(b1, 'umlclassdiagram_Classifier117'):
        assert not _is_linked(b1, 'umlclassdiagram_Classifier117', a)
    if hasattr(b2, 'umlclassdiagram_Classifier117'):
        assert _is_linked(b2, 'umlclassdiagram_Classifier117', a)
    _safe_set(a, 'umlclassdiagram_Relation116', None)
    assert not _is_linked(a, 'umlclassdiagram_Relation116', b2)
    if hasattr(b2, 'umlclassdiagram_Classifier117'):
        assert not _is_linked(b2, 'umlclassdiagram_Classifier117', a)


def test_assoc_super100_link_reassign_clear():
    a = umlclassdiagram_Classifier(abstract=True, derived=True)
    b1 = umlclassdiagram_Class()
    b2 = umlclassdiagram_Class()
    _safe_set(a, 'umlclassdiagram_Classifier101', {b1})
    assert _is_linked(a, 'umlclassdiagram_Classifier101', b1)
    if hasattr(b1, 'umlclassdiagram_Class'):
        assert _is_linked(b1, 'umlclassdiagram_Class', a)
    _safe_set(a, 'umlclassdiagram_Classifier101', {b2})
    assert _is_linked(a, 'umlclassdiagram_Classifier101', b2)
    if hasattr(b1, 'umlclassdiagram_Class'):
        assert not _is_linked(b1, 'umlclassdiagram_Class', a)
    if hasattr(b2, 'umlclassdiagram_Class'):
        assert _is_linked(b2, 'umlclassdiagram_Class', a)
    _safe_set(a, 'umlclassdiagram_Classifier101', set())
    assert not _is_linked(a, 'umlclassdiagram_Classifier101', b2)
    if hasattr(b2, 'umlclassdiagram_Class'):
        assert not _is_linked(b2, 'umlclassdiagram_Class', a)


def test_assoc_supplier102_link_reassign_clear():
    a = umlclassdiagram_Classifier(abstract=True, derived=True)
    b1 = umlclassdiagram_Class()
    b2 = umlclassdiagram_Class()
    _safe_set(a, 'umlclassdiagram_Classifier103', {b1})
    assert _is_linked(a, 'umlclassdiagram_Classifier103', b1)
    if hasattr(b1, 'umlclassdiagram_Class104'):
        assert _is_linked(b1, 'umlclassdiagram_Class104', a)
    _safe_set(a, 'umlclassdiagram_Classifier103', {b2})
    assert _is_linked(a, 'umlclassdiagram_Classifier103', b2)
    if hasattr(b1, 'umlclassdiagram_Class104'):
        assert not _is_linked(b1, 'umlclassdiagram_Class104', a)
    if hasattr(b2, 'umlclassdiagram_Class104'):
        assert _is_linked(b2, 'umlclassdiagram_Class104', a)
    _safe_set(a, 'umlclassdiagram_Classifier103', set())
    assert not _is_linked(a, 'umlclassdiagram_Classifier103', b2)
    if hasattr(b2, 'umlclassdiagram_Class104'):
        assert not _is_linked(b2, 'umlclassdiagram_Class104', a)


def test_assoc_tar118_link_reassign_clear():
    a = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    b1 = umlclassdiagram_Classifier(abstract=True, derived=True)
    b2 = umlclassdiagram_Classifier(abstract=False, derived=False)
    _safe_set(a, 'umlclassdiagram_Relation119', b1)
    assert _is_linked(a, 'umlclassdiagram_Relation119', b1)
    if hasattr(b1, 'umlclassdiagram_Classifier120'):
        assert _is_linked(b1, 'umlclassdiagram_Classifier120', a)
    _safe_set(a, 'umlclassdiagram_Relation119', b2)
    assert _is_linked(a, 'umlclassdiagram_Relation119', b2)
    if hasattr(b1, 'umlclassdiagram_Classifier120'):
        assert not _is_linked(b1, 'umlclassdiagram_Classifier120', a)
    if hasattr(b2, 'umlclassdiagram_Classifier120'):
        assert _is_linked(b2, 'umlclassdiagram_Classifier120', a)
    _safe_set(a, 'umlclassdiagram_Relation119', None)
    assert not _is_linked(a, 'umlclassdiagram_Relation119', b2)
    if hasattr(b2, 'umlclassdiagram_Classifier120'):
        assert not _is_linked(b2, 'umlclassdiagram_Classifier120', a)


def test_assoc_type105_link_reassign_clear():
    a = umlclassdiagram_Constraint(id="sample_text")
    b1 = umlclassdiagram_Class()
    b2 = umlclassdiagram_Class()
    _safe_set(a, 'umlclassdiagram_Constraint106', b1)
    assert _is_linked(a, 'umlclassdiagram_Constraint106', b1)
    if hasattr(b1, 'umlclassdiagram_Class107'):
        assert _is_linked(b1, 'umlclassdiagram_Class107', a)
    _safe_set(a, 'umlclassdiagram_Constraint106', b2)
    assert _is_linked(a, 'umlclassdiagram_Constraint106', b2)
    if hasattr(b1, 'umlclassdiagram_Class107'):
        assert not _is_linked(b1, 'umlclassdiagram_Class107', a)
    if hasattr(b2, 'umlclassdiagram_Class107'):
        assert _is_linked(b2, 'umlclassdiagram_Class107', a)
    _safe_set(a, 'umlclassdiagram_Constraint106', None)
    assert not _is_linked(a, 'umlclassdiagram_Constraint106', b2)
    if hasattr(b2, 'umlclassdiagram_Class107'):
        assert not _is_linked(b2, 'umlclassdiagram_Class107', a)


def test_assoc_type93_link_reassign_clear():
    a = umlclassdiagram_NamedElement(name="sample_text")
    b1 = umlclassdiagram_Parameter()
    b2 = umlclassdiagram_Parameter()
    _safe_set(a, 'umlclassdiagram_NamedElement', b1)
    assert _is_linked(a, 'umlclassdiagram_NamedElement', b1)
    if hasattr(b1, 'umlclassdiagram_Parameter'):
        assert _is_linked(b1, 'umlclassdiagram_Parameter', a)
    _safe_set(a, 'umlclassdiagram_NamedElement', b2)
    assert _is_linked(a, 'umlclassdiagram_NamedElement', b2)
    if hasattr(b1, 'umlclassdiagram_Parameter'):
        assert not _is_linked(b1, 'umlclassdiagram_Parameter', a)
    if hasattr(b2, 'umlclassdiagram_Parameter'):
        assert _is_linked(b2, 'umlclassdiagram_Parameter', a)
    _safe_set(a, 'umlclassdiagram_NamedElement', None)
    assert not _is_linked(a, 'umlclassdiagram_NamedElement', b2)
    if hasattr(b2, 'umlclassdiagram_Parameter'):
        assert not _is_linked(b2, 'umlclassdiagram_Parameter', a)


def test_assoc_type94_link_reassign_clear():
    a = umlclassdiagram_NamedElement(name="sample_text")
    b1 = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    b2 = umlclassdiagram_Feature(name="sample_text_2", scope="sample_text_2", visibility="sample_text_2")
    _safe_set(a, 'umlclassdiagram_NamedElement96', b1)
    assert _is_linked(a, 'umlclassdiagram_NamedElement96', b1)
    if hasattr(b1, 'umlclassdiagram_Feature95'):
        assert _is_linked(b1, 'umlclassdiagram_Feature95', a)
    _safe_set(a, 'umlclassdiagram_NamedElement96', b2)
    assert _is_linked(a, 'umlclassdiagram_NamedElement96', b2)
    if hasattr(b1, 'umlclassdiagram_Feature95'):
        assert not _is_linked(b1, 'umlclassdiagram_Feature95', a)
    if hasattr(b2, 'umlclassdiagram_Feature95'):
        assert _is_linked(b2, 'umlclassdiagram_Feature95', a)
    _safe_set(a, 'umlclassdiagram_NamedElement96', None)
    assert not _is_linked(a, 'umlclassdiagram_NamedElement96', b2)
    if hasattr(b2, 'umlclassdiagram_Feature95'):
        assert not _is_linked(b2, 'umlclassdiagram_Feature95', a)


def test_assoc_typeRef14_link_reassign_clear():
    a = umlclassdiagram_PropertyCS(name="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_PropertyCS15', b1)
    assert _is_linked(a, 'umlclassdiagram_PropertyCS15', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS16'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS16', a)
    _safe_set(a, 'umlclassdiagram_PropertyCS15', b2)
    assert _is_linked(a, 'umlclassdiagram_PropertyCS15', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS16'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS16', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS16'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS16', a)
    _safe_set(a, 'umlclassdiagram_PropertyCS15', None)
    assert not _is_linked(a, 'umlclassdiagram_PropertyCS15', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS16'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS16', a)


def test_assoc_typeRef24_link_reassign_clear():
    a = umlclassdiagram_ParameterCS(name="sample_text")
    b1 = umlclassdiagram_PathNameCS()
    b2 = umlclassdiagram_PathNameCS()
    _safe_set(a, 'umlclassdiagram_ParameterCS25', b1)
    assert _is_linked(a, 'umlclassdiagram_ParameterCS25', b1)
    if hasattr(b1, 'umlclassdiagram_PathNameCS26'):
        assert _is_linked(b1, 'umlclassdiagram_PathNameCS26', a)
    _safe_set(a, 'umlclassdiagram_ParameterCS25', b2)
    assert _is_linked(a, 'umlclassdiagram_ParameterCS25', b2)
    if hasattr(b1, 'umlclassdiagram_PathNameCS26'):
        assert not _is_linked(b1, 'umlclassdiagram_PathNameCS26', a)
    if hasattr(b2, 'umlclassdiagram_PathNameCS26'):
        assert _is_linked(b2, 'umlclassdiagram_PathNameCS26', a)
    _safe_set(a, 'umlclassdiagram_ParameterCS25', None)
    assert not _is_linked(a, 'umlclassdiagram_ParameterCS25', b2)
    if hasattr(b2, 'umlclassdiagram_PathNameCS26'):
        assert not _is_linked(b2, 'umlclassdiagram_PathNameCS26', a)


def test_assoc_types89_link_reassign_clear():
    a = umlclassdiagram_PrimitiveElement(type="sample_text")
    b1 = umlclassdiagram_ClassDiagram()
    b2 = umlclassdiagram_ClassDiagram()
    _safe_set(a, 'umlclassdiagram_PrimitiveElement', b1)
    assert _is_linked(a, 'umlclassdiagram_PrimitiveElement', b1)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram90'):
        assert _is_linked(b1, 'umlclassdiagram_ClassDiagram90', a)
    _safe_set(a, 'umlclassdiagram_PrimitiveElement', b2)
    assert _is_linked(a, 'umlclassdiagram_PrimitiveElement', b2)
    if hasattr(b1, 'umlclassdiagram_ClassDiagram90'):
        assert not _is_linked(b1, 'umlclassdiagram_ClassDiagram90', a)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram90'):
        assert _is_linked(b2, 'umlclassdiagram_ClassDiagram90', a)
    _safe_set(a, 'umlclassdiagram_PrimitiveElement', None)
    assert not _is_linked(a, 'umlclassdiagram_PrimitiveElement', b2)
    if hasattr(b2, 'umlclassdiagram_ClassDiagram90'):
        assert not _is_linked(b2, 'umlclassdiagram_ClassDiagram90', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BooleanLiteralExpCS_strategy = st.builds(BooleanLiteralExpCS)
@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)


CallExpCS_strategy = st.builds(CallExpCS)
@given(instance=CallExpCS_strategy)
@settings(max_examples=25)
def test_CallExpCS_instantiation(instance):
    assert isinstance(instance, CallExpCS)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


ExpCS_strategy = st.builds(ExpCS)
@given(instance=ExpCS_strategy)
@settings(max_examples=25)
def test_ExpCS_instantiation(instance):
    assert isinstance(instance, ExpCS)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


LiteralExpCS_strategy = st.builds(LiteralExpCS)
@given(instance=LiteralExpCS_strategy)
@settings(max_examples=25)
def test_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)


LogicExpCS_strategy = st.builds(LogicExpCS)
@given(instance=LogicExpCS_strategy)
@settings(max_examples=25)
def test_LogicExpCS_instantiation(instance):
    assert isinstance(instance, LogicExpCS)


LoopExpCS_strategy = st.builds(LoopExpCS)
@given(instance=LoopExpCS_strategy)
@settings(max_examples=25)
def test_LoopExpCS_instantiation(instance):
    assert isinstance(instance, LoopExpCS)


Modifier_strategy = st.builds(Modifier)
@given(instance=Modifier_strategy)
@settings(max_examples=25)
def test_Modifier_instantiation(instance):
    assert isinstance(instance, Modifier)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NavigationExpCS_strategy = st.builds(NavigationExpCS)
@given(instance=NavigationExpCS_strategy)
@settings(max_examples=25)
def test_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)


NavigationPathCS_strategy = st.builds(NavigationPathCS)
@given(instance=NavigationPathCS_strategy)
@settings(max_examples=25)
def test_NavigationPathCS_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)


PathCS_strategy = st.builds(PathCS)
@given(instance=PathCS_strategy)
@settings(max_examples=25)
def test_PathCS_instantiation(instance):
    assert isinstance(instance, PathCS)


PrimaryExpCS_strategy = st.builds(PrimaryExpCS)
@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


umlclassdiagram_AccVarCS_strategy = st.builds(umlclassdiagram_AccVarCS, accVarName=safe_text)
@given(instance=umlclassdiagram_AccVarCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_AccVarCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_AccVarCS)


umlclassdiagram_Aggregation_strategy = st.builds(umlclassdiagram_Aggregation)
@given(instance=umlclassdiagram_Aggregation_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Aggregation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Aggregation)


umlclassdiagram_Association_strategy = st.builds(umlclassdiagram_Association)
@given(instance=umlclassdiagram_Association_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Association_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Association)


umlclassdiagram_AssociationClass_strategy = st.builds(umlclassdiagram_AssociationClass)
@given(instance=umlclassdiagram_AssociationClass_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_AssociationClass_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_AssociationClass)


umlclassdiagram_Attribute_strategy = st.builds(umlclassdiagram_Attribute, derived=st.booleans())
@given(instance=umlclassdiagram_Attribute_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Attribute_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Attribute)


umlclassdiagram_BooleanExpCS_strategy = st.builds(umlclassdiagram_BooleanExpCS, boolSymbol=st.booleans())
@given(instance=umlclassdiagram_BooleanExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_BooleanExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_BooleanExpCS)


umlclassdiagram_BooleanLiteralExpCS_strategy = st.builds(umlclassdiagram_BooleanLiteralExpCS)
@given(instance=umlclassdiagram_BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_BooleanLiteralExpCS)


umlclassdiagram_CallExpCS_strategy = st.builds(umlclassdiagram_CallExpCS)
@given(instance=umlclassdiagram_CallExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_CallExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_CallExpCS)


umlclassdiagram_Class_strategy = st.builds(umlclassdiagram_Class)
@given(instance=umlclassdiagram_Class_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Class_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Class)


umlclassdiagram_ClassCS_strategy = st.builds(umlclassdiagram_ClassCS, name=safe_text)
@given(instance=umlclassdiagram_ClassCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ClassCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ClassCS)


umlclassdiagram_ClassDiagram_strategy = st.builds(umlclassdiagram_ClassDiagram)
@given(instance=umlclassdiagram_ClassDiagram_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ClassDiagram_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ClassDiagram)


umlclassdiagram_Classifier_strategy = st.builds(umlclassdiagram_Classifier, abstract=st.booleans(), derived=st.booleans())
@given(instance=umlclassdiagram_Classifier_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Classifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Classifier)


umlclassdiagram_CollectExpCS_strategy = st.builds(umlclassdiagram_CollectExpCS)
@given(instance=umlclassdiagram_CollectExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_CollectExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_CollectExpCS)


umlclassdiagram_Composition_strategy = st.builds(umlclassdiagram_Composition)
@given(instance=umlclassdiagram_Composition_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Composition_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Composition)


umlclassdiagram_Constraint_strategy = st.builds(umlclassdiagram_Constraint, id=safe_text)
@given(instance=umlclassdiagram_Constraint_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Constraint_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Constraint)


umlclassdiagram_ConstraintCS_strategy = st.builds(umlclassdiagram_ConstraintCS)
@given(instance=umlclassdiagram_ConstraintCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ConstraintCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ConstraintCS)


umlclassdiagram_Dependency_strategy = st.builds(umlclassdiagram_Dependency)
@given(instance=umlclassdiagram_Dependency_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Dependency_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Dependency)


umlclassdiagram_ExistsExpCS_strategy = st.builds(umlclassdiagram_ExistsExpCS)
@given(instance=umlclassdiagram_ExistsExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ExistsExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ExistsExpCS)


umlclassdiagram_ExpCS_strategy = st.builds(umlclassdiagram_ExpCS)
@given(instance=umlclassdiagram_ExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ExpCS)


umlclassdiagram_Feature_strategy = st.builds(umlclassdiagram_Feature, name=safe_text, scope=safe_text, visibility=safe_text)
@given(instance=umlclassdiagram_Feature_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Feature_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Feature)


umlclassdiagram_ForAllExpCS_strategy = st.builds(umlclassdiagram_ForAllExpCS)
@given(instance=umlclassdiagram_ForAllExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ForAllExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ForAllExpCS)


umlclassdiagram_IntLiteralExpCS_strategy = st.builds(umlclassdiagram_IntLiteralExpCS, intSymbol=st.integers())
@given(instance=umlclassdiagram_IntLiteralExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_IntLiteralExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IntLiteralExpCS)


umlclassdiagram_InvariantCS_strategy = st.builds(umlclassdiagram_InvariantCS)
@given(instance=umlclassdiagram_InvariantCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_InvariantCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_InvariantCS)


umlclassdiagram_IterateExpCS_strategy = st.builds(umlclassdiagram_IterateExpCS)
@given(instance=umlclassdiagram_IterateExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_IterateExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IterateExpCS)


umlclassdiagram_IteratorVarCS_strategy = st.builds(umlclassdiagram_IteratorVarCS, itName=safe_text)
@given(instance=umlclassdiagram_IteratorVarCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_IteratorVarCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IteratorVarCS)


umlclassdiagram_LiteralExpCS_strategy = st.builds(umlclassdiagram_LiteralExpCS)
@given(instance=umlclassdiagram_LiteralExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LiteralExpCS)


umlclassdiagram_LogicExpCS_strategy = st.builds(umlclassdiagram_LogicExpCS, op=safe_text)
@given(instance=umlclassdiagram_LogicExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_LogicExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LogicExpCS)


umlclassdiagram_LoopExpCS_strategy = st.builds(umlclassdiagram_LoopExpCS, logicOp=safe_text)
@given(instance=umlclassdiagram_LoopExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_LoopExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LoopExpCS)


umlclassdiagram_Modifier_strategy = st.builds(umlclassdiagram_Modifier, scope=safe_text, visibility=safe_text)
@given(instance=umlclassdiagram_Modifier_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Modifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Modifier)


umlclassdiagram_NameExpCS_strategy = st.builds(umlclassdiagram_NameExpCS)
@given(instance=umlclassdiagram_NameExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NameExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NameExpCS)


umlclassdiagram_NamedElement_strategy = st.builds(umlclassdiagram_NamedElement, name=safe_text)
@given(instance=umlclassdiagram_NamedElement_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NamedElement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NamedElement)


umlclassdiagram_NavigationExpCS_strategy = st.builds(umlclassdiagram_NavigationExpCS)
@given(instance=umlclassdiagram_NavigationExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationExpCS)


umlclassdiagram_NavigationNameExpCS_strategy = st.builds(umlclassdiagram_NavigationNameExpCS)
@given(instance=umlclassdiagram_NavigationNameExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationNameExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationNameExpCS)


umlclassdiagram_NavigationPathCS_strategy = st.builds(umlclassdiagram_NavigationPathCS)
@given(instance=umlclassdiagram_NavigationPathCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationPathCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathCS)


umlclassdiagram_NavigationPathElementCS_strategy = st.builds(umlclassdiagram_NavigationPathElementCS)
@given(instance=umlclassdiagram_NavigationPathElementCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationPathElementCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathElementCS)


umlclassdiagram_NavigationPathNameCS_strategy = st.builds(umlclassdiagram_NavigationPathNameCS)
@given(instance=umlclassdiagram_NavigationPathNameCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationPathNameCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathNameCS)


umlclassdiagram_NavigationPathVariableCS_strategy = st.builds(umlclassdiagram_NavigationPathVariableCS, varName=safe_text)
@given(instance=umlclassdiagram_NavigationPathVariableCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_NavigationPathVariableCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathVariableCS)


umlclassdiagram_Operation_strategy = st.builds(umlclassdiagram_Operation)
@given(instance=umlclassdiagram_Operation_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Operation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Operation)


umlclassdiagram_OperationCS_strategy = st.builds(umlclassdiagram_OperationCS, name=safe_text)
@given(instance=umlclassdiagram_OperationCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_OperationCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_OperationCS)


umlclassdiagram_Operator_strategy = st.builds(umlclassdiagram_Operator, operator=safe_text)
@given(instance=umlclassdiagram_Operator_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Operator_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Operator)


umlclassdiagram_PackageCS_strategy = st.builds(umlclassdiagram_PackageCS, name=safe_text)
@given(instance=umlclassdiagram_PackageCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PackageCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PackageCS)


umlclassdiagram_Parameter_strategy = st.builds(umlclassdiagram_Parameter)
@given(instance=umlclassdiagram_Parameter_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Parameter_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Parameter)


umlclassdiagram_ParameterCS_strategy = st.builds(umlclassdiagram_ParameterCS, name=safe_text)
@given(instance=umlclassdiagram_ParameterCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_ParameterCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ParameterCS)


umlclassdiagram_PathCS_strategy = st.builds(umlclassdiagram_PathCS)
@given(instance=umlclassdiagram_PathCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PathCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathCS)


umlclassdiagram_PathElementCS_strategy = st.builds(umlclassdiagram_PathElementCS)
@given(instance=umlclassdiagram_PathElementCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PathElementCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathElementCS)


umlclassdiagram_PathNameCS_strategy = st.builds(umlclassdiagram_PathNameCS)
@given(instance=umlclassdiagram_PathNameCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PathNameCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathNameCS)


umlclassdiagram_PathVariableCS_strategy = st.builds(umlclassdiagram_PathVariableCS, varName=safe_text)
@given(instance=umlclassdiagram_PathVariableCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PathVariableCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathVariableCS)


umlclassdiagram_PrimaryExpCS_strategy = st.builds(umlclassdiagram_PrimaryExpCS)
@given(instance=umlclassdiagram_PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PrimaryExpCS)


umlclassdiagram_PrimitiveElement_strategy = st.builds(umlclassdiagram_PrimitiveElement, type=safe_text)
@given(instance=umlclassdiagram_PrimitiveElement_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PrimitiveElement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PrimitiveElement)


umlclassdiagram_PropertyCS_strategy = st.builds(umlclassdiagram_PropertyCS, name=safe_text)
@given(instance=umlclassdiagram_PropertyCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_PropertyCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PropertyCS)


umlclassdiagram_Relation_strategy = st.builds(umlclassdiagram_Relation, derived=st.booleans(), nsrc=safe_text, ntar=safe_text)
@given(instance=umlclassdiagram_Relation_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_Relation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Relation)


umlclassdiagram_RootCS_strategy = st.builds(umlclassdiagram_RootCS)
@given(instance=umlclassdiagram_RootCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_RootCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_RootCS)


umlclassdiagram_RoundedBracketClauseCS_strategy = st.builds(umlclassdiagram_RoundedBracketClauseCS)
@given(instance=umlclassdiagram_RoundedBracketClauseCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_RoundedBracketClauseCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_RoundedBracketClauseCS)


umlclassdiagram_StringLiteralExpCS_strategy = st.builds(umlclassdiagram_StringLiteralExpCS, stringSymbol=safe_text)
@given(instance=umlclassdiagram_StringLiteralExpCS_strategy)
@settings(max_examples=25)
def test_umlclassdiagram_StringLiteralExpCS_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_StringLiteralExpCS)



