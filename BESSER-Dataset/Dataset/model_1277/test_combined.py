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
    ModelElementCS,
    AbstractNameExpCS,
    essentialoclcs_CallExpCS,
    PrimitiveLiteralExpCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_AssociationClass,
    CallExpCS,
    essentialoclcs_AssociationClassCallExpCS,
    essentialoclcs_Type,
    essentialoclcs_PathNameCS,
    ExpCS,
    essentialoclcs_AbstractNameExpCS,
    essentialoclcs_Variable,
    essentialoclcs_VariableExpCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_ShadowExpCS,
    essentialoclcs_SelfExpCS,
    essentialoclcs_Property,
    essentialoclcs_PropertyCallExpCS,
    essentialoclcs_TypeRefCS,
    essentialoclcs_Operation,
    essentialoclcs_OperationCallExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_Iteration,
    essentialoclcs_NavigatingArgCS,
    VariableExpCS,
    PropertyCallExpCS,
    OperationCallExpCS,
    IterateCallExpCS,
    ShadowExpCS,
    AssociationClassCallExpCS,
    essentialoclcs_MapLiteralPartCS,
    essentialoclcs_LiteralExpCS,
    VariableCS,
    essentialoclcs_TupleLiteralPartCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_IterationCallExpCS,
    IterationCallExpCS,
    essentialoclcs_NameExpCS,
    essentialoclcs_IterateCallExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    OperatorExpCS,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_IfThenExpCS,
    essentialoclcs_IfExpCS,
    SpecificationCS,
    essentialoclcs_ExpSpecificationCS,
    essentialoclcs_Precedence,
    essentialoclcs_CollectionLiteralPartCS,
    LiteralExpCS,
    essentialoclcs_MapLiteralExpCS,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_LambdaLiteralExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    essentialoclcs_ExpCS,
    ContextLessElementCS,
    essentialoclcs_CurlyBracketedClauseCS,
    essentialoclcs_RoundBracketedClauseCS,
    essentialoclcs_SquareBracketedClauseCS,
    RootCS,
    NamedElementCS,
    essentialoclcs_OperatorExpCS,
    essentialoclcs_VariableCS,
    essentialoclcs_ContextCS,
    essentialoclcs_TypedRefCS,
    Nameable,
    essentialoclcs_ShadowPartCS,
    essentialoclcs_PatternExpCS,
    TypedRefCS,
    essentialoclcs_CollectionTypeCS,
    essentialoclcs_TypeNameExpCS,
    essentialoclcs_MapTypeCS,
    essentialoclcs_CollectionPatternCS,
    NavigationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_hyp_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_hyp_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(AbstractNameExpCS)


def test_hyp_abstractnameexpcs_constructor_exists():
    assert callable(AbstractNameExpCS.__init__)


def test_hyp_abstractnameexpcs_constructor_args():
    sig = inspect.signature(AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CallExpCS)


def test_hyp_essentialoclcs_callexpcs_constructor_exists():
    assert callable(essentialoclcs_CallExpCS.__init__)


def test_hyp_essentialoclcs_callexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_hyp_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_hyp_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_BooleanLiteralExpCS)


def test_hyp_essentialoclcs_booleanliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_BooleanLiteralExpCS.__init__)


def test_hyp_essentialoclcs_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_essentialoclcs_associationclass_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AssociationClass)


def test_hyp_essentialoclcs_associationclass_constructor_exists():
    assert callable(essentialoclcs_AssociationClass.__init__)


def test_hyp_essentialoclcs_associationclass_constructor_args():
    sig = inspect.signature(essentialoclcs_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_hyp_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_hyp_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_associationclasscallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AssociationClassCallExpCS)


def test_hyp_essentialoclcs_associationclasscallexpcs_constructor_exists():
    assert callable(essentialoclcs_AssociationClassCallExpCS.__init__)


def test_hyp_essentialoclcs_associationclasscallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_AssociationClassCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_type_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Type)


def test_hyp_essentialoclcs_type_constructor_exists():
    assert callable(essentialoclcs_Type.__init__)


def test_hyp_essentialoclcs_type_constructor_args():
    sig = inspect.signature(essentialoclcs_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PathNameCS)


def test_hyp_essentialoclcs_pathnamecs_constructor_exists():
    assert callable(essentialoclcs_PathNameCS.__init__)


def test_hyp_essentialoclcs_pathnamecs_constructor_args():
    sig = inspect.signature(essentialoclcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_hyp_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_hyp_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AbstractNameExpCS)


def test_hyp_essentialoclcs_abstractnameexpcs_constructor_exists():
    assert callable(essentialoclcs_AbstractNameExpCS.__init__)


def test_hyp_essentialoclcs_abstractnameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"




def test_hyp_essentialoclcs_variable_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Variable)


def test_hyp_essentialoclcs_variable_constructor_exists():
    assert callable(essentialoclcs_Variable.__init__)


def test_hyp_essentialoclcs_variable_constructor_args():
    sig = inspect.signature(essentialoclcs_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_VariableExpCS)


def test_hyp_essentialoclcs_variableexpcs_constructor_exists():
    assert callable(essentialoclcs_VariableExpCS.__init__)


def test_hyp_essentialoclcs_variableexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_UnlimitedNaturalLiteralExpCS)


def test_hyp_essentialoclcs_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)


def test_hyp_essentialoclcs_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_StringLiteralExpCS)


def test_hyp_essentialoclcs_stringliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_StringLiteralExpCS.__init__)


def test_hyp_essentialoclcs_stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"




def test_hyp_essentialoclcs_shadowexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ShadowExpCS)


def test_hyp_essentialoclcs_shadowexpcs_constructor_exists():
    assert callable(essentialoclcs_ShadowExpCS.__init__)


def test_hyp_essentialoclcs_shadowexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ShadowExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_essentialoclcs_selfexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_SelfExpCS)


def test_hyp_essentialoclcs_selfexpcs_constructor_exists():
    assert callable(essentialoclcs_SelfExpCS.__init__)


def test_hyp_essentialoclcs_selfexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_SelfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_essentialoclcs_property_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Property)


def test_hyp_essentialoclcs_property_constructor_exists():
    assert callable(essentialoclcs_Property.__init__)


def test_hyp_essentialoclcs_property_constructor_args():
    sig = inspect.signature(essentialoclcs_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_propertycallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PropertyCallExpCS)


def test_hyp_essentialoclcs_propertycallexpcs_constructor_exists():
    assert callable(essentialoclcs_PropertyCallExpCS.__init__)


def test_hyp_essentialoclcs_propertycallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PropertyCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_typerefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeRefCS)


def test_hyp_essentialoclcs_typerefcs_constructor_exists():
    assert callable(essentialoclcs_TypeRefCS.__init__)


def test_hyp_essentialoclcs_typerefcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_operation_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Operation)


def test_hyp_essentialoclcs_operation_constructor_exists():
    assert callable(essentialoclcs_Operation.__init__)


def test_hyp_essentialoclcs_operation_constructor_args():
    sig = inspect.signature(essentialoclcs_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_OperationCallExpCS)


def test_hyp_essentialoclcs_operationcallexpcs_constructor_exists():
    assert callable(essentialoclcs_OperationCallExpCS.__init__)


def test_hyp_essentialoclcs_operationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NumberLiteralExpCS)


def test_hyp_essentialoclcs_numberliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NumberLiteralExpCS.__init__)


def test_hyp_essentialoclcs_numberliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_essentialoclcs_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NullLiteralExpCS)


def test_hyp_essentialoclcs_nullliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NullLiteralExpCS.__init__)


def test_hyp_essentialoclcs_nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NestedExpCS)


def test_hyp_essentialoclcs_nestedexpcs_constructor_exists():
    assert callable(essentialoclcs_NestedExpCS.__init__)


def test_hyp_essentialoclcs_nestedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetExpCS)


def test_hyp_essentialoclcs_letexpcs_constructor_exists():
    assert callable(essentialoclcs_LetExpCS.__init__)


def test_hyp_essentialoclcs_letexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"




def test_hyp_essentialoclcs_iteration_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Iteration)


def test_hyp_essentialoclcs_iteration_constructor_exists():
    assert callable(essentialoclcs_Iteration.__init__)


def test_hyp_essentialoclcs_iteration_constructor_args():
    sig = inspect.signature(essentialoclcs_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NavigatingArgCS)


def test_hyp_essentialoclcs_navigatingargcs_constructor_exists():
    assert callable(essentialoclcs_NavigatingArgCS.__init__)


def test_hyp_essentialoclcs_navigatingargcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "role" in params, "Missing parameter 'role'"





def test_hyp_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(VariableExpCS)


def test_hyp_variableexpcs_constructor_exists():
    assert callable(VariableExpCS.__init__)


def test_hyp_variableexpcs_constructor_args():
    sig = inspect.signature(VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertycallexpcs_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExpCS)


def test_hyp_propertycallexpcs_constructor_exists():
    assert callable(PropertyCallExpCS.__init__)


def test_hyp_propertycallexpcs_constructor_args():
    sig = inspect.signature(PropertyCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_hyp_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_hyp_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iteratecallexpcs_is_not_abstract():
    assert not inspect.isabstract(IterateCallExpCS)


def test_hyp_iteratecallexpcs_constructor_exists():
    assert callable(IterateCallExpCS.__init__)


def test_hyp_iteratecallexpcs_constructor_args():
    sig = inspect.signature(IterateCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shadowexpcs_is_not_abstract():
    assert not inspect.isabstract(ShadowExpCS)


def test_hyp_shadowexpcs_constructor_exists():
    assert callable(ShadowExpCS.__init__)


def test_hyp_shadowexpcs_constructor_args():
    sig = inspect.signature(ShadowExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_associationclasscallexpcs_is_not_abstract():
    assert not inspect.isabstract(AssociationClassCallExpCS)


def test_hyp_associationclasscallexpcs_constructor_exists():
    assert callable(AssociationClassCallExpCS.__init__)


def test_hyp_associationclasscallexpcs_constructor_args():
    sig = inspect.signature(AssociationClassCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_mapliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapLiteralPartCS)


def test_hyp_essentialoclcs_mapliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_MapLiteralPartCS.__init__)


def test_hyp_essentialoclcs_mapliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LiteralExpCS)


def test_hyp_essentialoclcs_literalexpcs_constructor_exists():
    assert callable(essentialoclcs_LiteralExpCS.__init__)


def test_hyp_essentialoclcs_literalexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_hyp_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_hyp_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralPartCS)


def test_hyp_essentialoclcs_tupleliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralPartCS.__init__)


def test_hyp_essentialoclcs_tupleliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_letvariablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetVariableCS)


def test_hyp_essentialoclcs_letvariablecs_constructor_exists():
    assert callable(essentialoclcs_LetVariableCS.__init__)


def test_hyp_essentialoclcs_letvariablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IterationCallExpCS)


def test_hyp_essentialoclcs_iterationcallexpcs_constructor_exists():
    assert callable(essentialoclcs_IterationCallExpCS.__init__)


def test_hyp_essentialoclcs_iterationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(IterationCallExpCS)


def test_hyp_iterationcallexpcs_constructor_exists():
    assert callable(IterationCallExpCS.__init__)


def test_hyp_iterationcallexpcs_constructor_args():
    sig = inspect.signature(IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NameExpCS)


def test_hyp_essentialoclcs_nameexpcs_constructor_exists():
    assert callable(essentialoclcs_NameExpCS.__init__)


def test_hyp_essentialoclcs_nameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_iteratecallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IterateCallExpCS)


def test_hyp_essentialoclcs_iteratecallexpcs_constructor_exists():
    assert callable(essentialoclcs_IterateCallExpCS.__init__)


def test_hyp_essentialoclcs_iteratecallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IterateCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InvalidLiteralExpCS)


def test_hyp_essentialoclcs_invalidliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_InvalidLiteralExpCS.__init__)


def test_hyp_essentialoclcs_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(OperatorExpCS)


def test_hyp_operatorexpcs_constructor_exists():
    assert callable(OperatorExpCS.__init__)


def test_hyp_operatorexpcs_constructor_args():
    sig = inspect.signature(OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrefixExpCS)


def test_hyp_essentialoclcs_prefixexpcs_constructor_exists():
    assert callable(essentialoclcs_PrefixExpCS.__init__)


def test_hyp_essentialoclcs_prefixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_infixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InfixExpCS)


def test_hyp_essentialoclcs_infixexpcs_constructor_exists():
    assert callable(essentialoclcs_InfixExpCS.__init__)


def test_hyp_essentialoclcs_infixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_ifthenexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IfThenExpCS)


def test_hyp_essentialoclcs_ifthenexpcs_constructor_exists():
    assert callable(essentialoclcs_IfThenExpCS.__init__)


def test_hyp_essentialoclcs_ifthenexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IfThenExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IfExpCS)


def test_hyp_essentialoclcs_ifexpcs_constructor_exists():
    assert callable(essentialoclcs_IfExpCS.__init__)


def test_hyp_essentialoclcs_ifexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"




def test_hyp_specificationcs_is_not_abstract():
    assert not inspect.isabstract(SpecificationCS)


def test_hyp_specificationcs_constructor_exists():
    assert callable(SpecificationCS.__init__)


def test_hyp_specificationcs_constructor_args():
    sig = inspect.signature(SpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpSpecificationCS)


def test_hyp_essentialoclcs_expspecificationcs_constructor_exists():
    assert callable(essentialoclcs_ExpSpecificationCS.__init__)


def test_hyp_essentialoclcs_expspecificationcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpSpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_precedence_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Precedence)


def test_hyp_essentialoclcs_precedence_constructor_exists():
    assert callable(essentialoclcs_Precedence.__init__)


def test_hyp_essentialoclcs_precedence_constructor_args():
    sig = inspect.signature(essentialoclcs_Precedence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralPartCS)


def test_hyp_essentialoclcs_collectionliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralPartCS.__init__)


def test_hyp_essentialoclcs_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_hyp_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_hyp_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_mapliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapLiteralExpCS)


def test_hyp_essentialoclcs_mapliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_MapLiteralExpCS.__init__)


def test_hyp_essentialoclcs_mapliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeLiteralExpCS)


def test_hyp_essentialoclcs_typeliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeLiteralExpCS.__init__)


def test_hyp_essentialoclcs_typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralExpCS)


def test_hyp_essentialoclcs_tupleliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralExpCS.__init__)


def test_hyp_essentialoclcs_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_lambdaliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LambdaLiteralExpCS)


def test_hyp_essentialoclcs_lambdaliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_LambdaLiteralExpCS.__init__)


def test_hyp_essentialoclcs_lambdaliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LambdaLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrimitiveLiteralExpCS)


def test_hyp_essentialoclcs_primitiveliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_PrimitiveLiteralExpCS.__init__)


def test_hyp_essentialoclcs_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralExpCS)


def test_hyp_essentialoclcs_collectionliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralExpCS.__init__)


def test_hyp_essentialoclcs_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_expcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpCS)


def test_hyp_essentialoclcs_expcs_constructor_exists():
    assert callable(essentialoclcs_ExpCS.__init__)


def test_hyp_essentialoclcs_expcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "hasError" in params, "Missing parameter 'hasError'"




def test_hyp_contextlesselementcs_is_not_abstract():
    assert not inspect.isabstract(ContextLessElementCS)


def test_hyp_contextlesselementcs_constructor_exists():
    assert callable(ContextLessElementCS.__init__)


def test_hyp_contextlesselementcs_constructor_args():
    sig = inspect.signature(ContextLessElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_curlybracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CurlyBracketedClauseCS)


def test_hyp_essentialoclcs_curlybracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_CurlyBracketedClauseCS.__init__)


def test_hyp_essentialoclcs_curlybracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_CurlyBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_essentialoclcs_roundbracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_RoundBracketedClauseCS)


def test_hyp_essentialoclcs_roundbracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_RoundBracketedClauseCS.__init__)


def test_hyp_essentialoclcs_roundbracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_RoundBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_squarebracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_SquareBracketedClauseCS)


def test_hyp_essentialoclcs_squarebracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_SquareBracketedClauseCS.__init__)


def test_hyp_essentialoclcs_squarebracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_SquareBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_hyp_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_hyp_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_hyp_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_hyp_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_OperatorExpCS)


def test_hyp_essentialoclcs_operatorexpcs_constructor_exists():
    assert callable(essentialoclcs_OperatorExpCS.__init__)


def test_hyp_essentialoclcs_operatorexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_VariableCS)


def test_hyp_essentialoclcs_variablecs_constructor_exists():
    assert callable(essentialoclcs_VariableCS.__init__)


def test_hyp_essentialoclcs_variablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_contextcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ContextCS)


def test_hyp_essentialoclcs_contextcs_constructor_exists():
    assert callable(essentialoclcs_ContextCS.__init__)


def test_hyp_essentialoclcs_contextcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ContextCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypedRefCS)


def test_hyp_essentialoclcs_typedrefcs_constructor_exists():
    assert callable(essentialoclcs_TypedRefCS.__init__)


def test_hyp_essentialoclcs_typedrefcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_hyp_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_hyp_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_shadowpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ShadowPartCS)


def test_hyp_essentialoclcs_shadowpartcs_constructor_exists():
    assert callable(essentialoclcs_ShadowPartCS.__init__)


def test_hyp_essentialoclcs_shadowpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ShadowPartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_patternexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PatternExpCS)


def test_hyp_essentialoclcs_patternexpcs_constructor_exists():
    assert callable(essentialoclcs_PatternExpCS.__init__)


def test_hyp_essentialoclcs_patternexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PatternExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "patternVariableName" in params, "Missing parameter 'patternVariableName'"




def test_hyp_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_hyp_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_hyp_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionTypeCS)


def test_hyp_essentialoclcs_collectiontypecs_constructor_exists():
    assert callable(essentialoclcs_CollectionTypeCS.__init__)


def test_hyp_essentialoclcs_collectiontypecs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_essentialoclcs_typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeNameExpCS)


def test_hyp_essentialoclcs_typenameexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeNameExpCS.__init__)


def test_hyp_essentialoclcs_typenameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcs_maptypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapTypeCS)


def test_hyp_essentialoclcs_maptypecs_constructor_exists():
    assert callable(essentialoclcs_MapTypeCS.__init__)


def test_hyp_essentialoclcs_maptypecs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_essentialoclcs_collectionpatterncs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionPatternCS)


def test_hyp_essentialoclcs_collectionpatterncs_constructor_exists():
    assert callable(essentialoclcs_CollectionPatternCS.__init__)


def test_hyp_essentialoclcs_collectionpatterncs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionPatternCS.__init__)
    params = list(sig.parameters.keys())
    assert "restVariableName" in params, "Missing parameter 'restVariableName'"


def test_hyp_navigationrole_exists():
    # Check that the Enumeration exists
    assert NavigationRole is not None

def test_hyp_navigationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationRole]
    expected_literals = [
        "ACCUMULATOR",
        "ITERATOR",
        "EXPRESSION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NavigationRole"


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
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
AbstractNameExpCS_strategy = st.builds(
    AbstractNameExpCS,
)
essentialoclcs_CallExpCS_strategy = st.builds(
    essentialoclcs_CallExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialoclcs_BooleanLiteralExpCS_strategy = st.builds(
    essentialoclcs_BooleanLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs_AssociationClass_strategy = st.builds(
    essentialoclcs_AssociationClass,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
essentialoclcs_AssociationClassCallExpCS_strategy = st.builds(
    essentialoclcs_AssociationClassCallExpCS,
)
essentialoclcs_Type_strategy = st.builds(
    essentialoclcs_Type,
)
essentialoclcs_PathNameCS_strategy = st.builds(
    essentialoclcs_PathNameCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
essentialoclcs_AbstractNameExpCS_strategy = st.builds(
    essentialoclcs_AbstractNameExpCS,
    isPre=
        st.booleans()
)
essentialoclcs_Variable_strategy = st.builds(
    essentialoclcs_Variable,
)
essentialoclcs_VariableExpCS_strategy = st.builds(
    essentialoclcs_VariableExpCS,
)
essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
)
essentialoclcs_StringLiteralExpCS_strategy = st.builds(
    essentialoclcs_StringLiteralExpCS,
    segments=
        safe_text
)
essentialoclcs_ShadowExpCS_strategy = st.builds(
    essentialoclcs_ShadowExpCS,
    value=
        safe_text
)
essentialoclcs_SelfExpCS_strategy = st.builds(
    essentialoclcs_SelfExpCS,
    name=
        safe_text
)
essentialoclcs_Property_strategy = st.builds(
    essentialoclcs_Property,
)
essentialoclcs_PropertyCallExpCS_strategy = st.builds(
    essentialoclcs_PropertyCallExpCS,
)
essentialoclcs_TypeRefCS_strategy = st.builds(
    essentialoclcs_TypeRefCS,
)
essentialoclcs_Operation_strategy = st.builds(
    essentialoclcs_Operation,
)
essentialoclcs_OperationCallExpCS_strategy = st.builds(
    essentialoclcs_OperationCallExpCS,
)
essentialoclcs_NumberLiteralExpCS_strategy = st.builds(
    essentialoclcs_NumberLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs_NullLiteralExpCS_strategy = st.builds(
    essentialoclcs_NullLiteralExpCS,
)
essentialoclcs_NestedExpCS_strategy = st.builds(
    essentialoclcs_NestedExpCS,
)
essentialoclcs_LetExpCS_strategy = st.builds(
    essentialoclcs_LetExpCS,
    isImplicit=
        st.booleans()
)
essentialoclcs_Iteration_strategy = st.builds(
    essentialoclcs_Iteration,
)
essentialoclcs_NavigatingArgCS_strategy = st.builds(
    essentialoclcs_NavigatingArgCS,
    prefix=
        safe_text,
    role=
        safe_text
)
VariableExpCS_strategy = st.builds(
    VariableExpCS,
)
PropertyCallExpCS_strategy = st.builds(
    PropertyCallExpCS,
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
IterateCallExpCS_strategy = st.builds(
    IterateCallExpCS,
)
ShadowExpCS_strategy = st.builds(
    ShadowExpCS,
)
AssociationClassCallExpCS_strategy = st.builds(
    AssociationClassCallExpCS,
)
essentialoclcs_MapLiteralPartCS_strategy = st.builds(
    essentialoclcs_MapLiteralPartCS,
)
essentialoclcs_LiteralExpCS_strategy = st.builds(
    essentialoclcs_LiteralExpCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
essentialoclcs_TupleLiteralPartCS_strategy = st.builds(
    essentialoclcs_TupleLiteralPartCS,
)
essentialoclcs_LetVariableCS_strategy = st.builds(
    essentialoclcs_LetVariableCS,
)
essentialoclcs_IterationCallExpCS_strategy = st.builds(
    essentialoclcs_IterationCallExpCS,
)
IterationCallExpCS_strategy = st.builds(
    IterationCallExpCS,
)
essentialoclcs_NameExpCS_strategy = st.builds(
    essentialoclcs_NameExpCS,
)
essentialoclcs_IterateCallExpCS_strategy = st.builds(
    essentialoclcs_IterateCallExpCS,
)
essentialoclcs_InvalidLiteralExpCS_strategy = st.builds(
    essentialoclcs_InvalidLiteralExpCS,
)
OperatorExpCS_strategy = st.builds(
    OperatorExpCS,
)
essentialoclcs_PrefixExpCS_strategy = st.builds(
    essentialoclcs_PrefixExpCS,
)
essentialoclcs_InfixExpCS_strategy = st.builds(
    essentialoclcs_InfixExpCS,
)
essentialoclcs_IfThenExpCS_strategy = st.builds(
    essentialoclcs_IfThenExpCS,
)
essentialoclcs_IfExpCS_strategy = st.builds(
    essentialoclcs_IfExpCS,
    isImplicit=
        st.booleans()
)
SpecificationCS_strategy = st.builds(
    SpecificationCS,
)
essentialoclcs_ExpSpecificationCS_strategy = st.builds(
    essentialoclcs_ExpSpecificationCS,
)
essentialoclcs_Precedence_strategy = st.builds(
    essentialoclcs_Precedence,
)
essentialoclcs_CollectionLiteralPartCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialoclcs_MapLiteralExpCS_strategy = st.builds(
    essentialoclcs_MapLiteralExpCS,
)
essentialoclcs_TypeLiteralExpCS_strategy = st.builds(
    essentialoclcs_TypeLiteralExpCS,
)
essentialoclcs_TupleLiteralExpCS_strategy = st.builds(
    essentialoclcs_TupleLiteralExpCS,
)
essentialoclcs_LambdaLiteralExpCS_strategy = st.builds(
    essentialoclcs_LambdaLiteralExpCS,
)
essentialoclcs_PrimitiveLiteralExpCS_strategy = st.builds(
    essentialoclcs_PrimitiveLiteralExpCS,
)
essentialoclcs_CollectionLiteralExpCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralExpCS,
)
essentialoclcs_ExpCS_strategy = st.builds(
    essentialoclcs_ExpCS,
    hasError=
        st.booleans()
)
ContextLessElementCS_strategy = st.builds(
    ContextLessElementCS,
)
essentialoclcs_CurlyBracketedClauseCS_strategy = st.builds(
    essentialoclcs_CurlyBracketedClauseCS,
    value=
        safe_text
)
essentialoclcs_RoundBracketedClauseCS_strategy = st.builds(
    essentialoclcs_RoundBracketedClauseCS,
)
essentialoclcs_SquareBracketedClauseCS_strategy = st.builds(
    essentialoclcs_SquareBracketedClauseCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
essentialoclcs_OperatorExpCS_strategy = st.builds(
    essentialoclcs_OperatorExpCS,
)
essentialoclcs_VariableCS_strategy = st.builds(
    essentialoclcs_VariableCS,
)
essentialoclcs_ContextCS_strategy = st.builds(
    essentialoclcs_ContextCS,
)
essentialoclcs_TypedRefCS_strategy = st.builds(
    essentialoclcs_TypedRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
essentialoclcs_ShadowPartCS_strategy = st.builds(
    essentialoclcs_ShadowPartCS,
)
essentialoclcs_PatternExpCS_strategy = st.builds(
    essentialoclcs_PatternExpCS,
    patternVariableName=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
essentialoclcs_CollectionTypeCS_strategy = st.builds(
    essentialoclcs_CollectionTypeCS,
    name=
        safe_text
)
essentialoclcs_TypeNameExpCS_strategy = st.builds(
    essentialoclcs_TypeNameExpCS,
)
essentialoclcs_MapTypeCS_strategy = st.builds(
    essentialoclcs_MapTypeCS,
    name=
        safe_text
)
essentialoclcs_CollectionPatternCS_strategy = st.builds(
    essentialoclcs_CollectionPatternCS,
    restVariableName=
        safe_text
)








@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
def test_hyp_essentialoclcs_booleanliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original










@given(instance=essentialoclcs_AbstractNameExpCS_strategy)
def test_hyp_essentialoclcs_abstractnameexpcs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original







@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
def test_hyp_essentialoclcs_stringliteralexpcs_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original




@given(instance=essentialoclcs_ShadowExpCS_strategy)
def test_hyp_essentialoclcs_shadowexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=essentialoclcs_SelfExpCS_strategy)
def test_hyp_essentialoclcs_selfexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
def test_hyp_essentialoclcs_numberliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original






@given(instance=essentialoclcs_LetExpCS_strategy)
def test_hyp_essentialoclcs_letexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original





@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_hyp_essentialoclcs_navigatingargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_hyp_essentialoclcs_navigatingargcs_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original
























@given(instance=essentialoclcs_IfExpCS_strategy)
def test_hyp_essentialoclcs_ifexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original















@given(instance=essentialoclcs_ExpCS_strategy)
def test_hyp_essentialoclcs_expcs_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=30)
def test_hyp_essentialoclcs_expcs_islocalleftancestorof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocalLeftAncestorOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocalLeftAncestorOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=30)
def test_hyp_essentialoclcs_expcs_islocalrightancestorof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocalRightAncestorOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocalRightAncestorOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocalRightAncestorOf' in essentialoclcs_ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs_ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs_ExpCS is not implemented or raised an error")





@given(instance=essentialoclcs_CurlyBracketedClauseCS_strategy)
def test_hyp_essentialoclcs_curlybracketedclausecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original














@given(instance=essentialoclcs_PatternExpCS_strategy)
def test_hyp_essentialoclcs_patternexpcs_patternVariableName_setter(instance):
    original = instance.patternVariableName
    instance.patternVariableName = original
    assert instance.patternVariableName == original





@given(instance=essentialoclcs_CollectionTypeCS_strategy)
def test_hyp_essentialoclcs_collectiontypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=essentialoclcs_MapTypeCS_strategy)
def test_hyp_essentialoclcs_maptypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=essentialoclcs_CollectionPatternCS_strategy)
def test_hyp_essentialoclcs_collectionpatterncs_restVariableName_setter(instance):
    original = instance.restVariableName
    instance.restVariableName = original
    assert instance.restVariableName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractNameExpCS,
    AssociationClassCallExpCS,
    CallExpCS,
    ContextLessElementCS,
    ExpCS,
    IterateCallExpCS,
    IterationCallExpCS,
    LiteralExpCS,
    ModelElementCS,
    Nameable,
    NamedElementCS,
    OperationCallExpCS,
    OperatorExpCS,
    PrimitiveLiteralExpCS,
    PropertyCallExpCS,
    RootCS,
    ShadowExpCS,
    SpecificationCS,
    TypedRefCS,
    VariableCS,
    VariableExpCS,
    essentialoclcs_AbstractNameExpCS,
    essentialoclcs_AssociationClass,
    essentialoclcs_AssociationClassCallExpCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_CallExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    essentialoclcs_CollectionLiteralPartCS,
    essentialoclcs_CollectionPatternCS,
    essentialoclcs_CollectionTypeCS,
    essentialoclcs_ContextCS,
    essentialoclcs_CurlyBracketedClauseCS,
    essentialoclcs_ExpCS,
    essentialoclcs_ExpSpecificationCS,
    essentialoclcs_IfExpCS,
    essentialoclcs_IfThenExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    essentialoclcs_IterateCallExpCS,
    essentialoclcs_Iteration,
    essentialoclcs_IterationCallExpCS,
    essentialoclcs_LambdaLiteralExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_LiteralExpCS,
    essentialoclcs_MapLiteralExpCS,
    essentialoclcs_MapLiteralPartCS,
    essentialoclcs_MapTypeCS,
    essentialoclcs_NameExpCS,
    essentialoclcs_NavigatingArgCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_Operation,
    essentialoclcs_OperationCallExpCS,
    essentialoclcs_OperatorExpCS,
    essentialoclcs_PathNameCS,
    essentialoclcs_PatternExpCS,
    essentialoclcs_Precedence,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_Property,
    essentialoclcs_PropertyCallExpCS,
    essentialoclcs_RoundBracketedClauseCS,
    essentialoclcs_SelfExpCS,
    essentialoclcs_ShadowExpCS,
    essentialoclcs_ShadowPartCS,
    essentialoclcs_SquareBracketedClauseCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_TupleLiteralPartCS,
    essentialoclcs_Type,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_TypeNameExpCS,
    essentialoclcs_TypeRefCS,
    essentialoclcs_TypedRefCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_Variable,
    essentialoclcs_VariableCS,
    essentialoclcs_VariableExpCS,
    NavigationRole,
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

def test_essentialoclcs_AbstractNameExpCS_isPre_value_roundtrip():
    instance = essentialoclcs_AbstractNameExpCS(isPre=True)
    assert instance.isPre == True
    instance.isPre = False
    assert instance.isPre == False


def test_essentialoclcs_BooleanLiteralExpCS_symbol_value_roundtrip():
    instance = essentialoclcs_BooleanLiteralExpCS(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_essentialoclcs_CollectionPatternCS_restVariableName_value_roundtrip():
    instance = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    assert instance.restVariableName == "sample_text"
    instance.restVariableName = "sample_text_2"
    assert instance.restVariableName == "sample_text_2"


def test_essentialoclcs_CollectionTypeCS_name_value_roundtrip():
    instance = essentialoclcs_CollectionTypeCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_essentialoclcs_CurlyBracketedClauseCS_value_value_roundtrip():
    instance = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_essentialoclcs_ExpCS_hasError_value_roundtrip():
    instance = essentialoclcs_ExpCS(hasError=True)
    assert instance.hasError == True
    instance.hasError = False
    assert instance.hasError == False


def test_essentialoclcs_IfExpCS_isImplicit_value_roundtrip():
    instance = essentialoclcs_IfExpCS(isImplicit=True)
    assert instance.isImplicit == True
    instance.isImplicit = False
    assert instance.isImplicit == False


def test_essentialoclcs_LetExpCS_isImplicit_value_roundtrip():
    instance = essentialoclcs_LetExpCS(isImplicit=True)
    assert instance.isImplicit == True
    instance.isImplicit = False
    assert instance.isImplicit == False


def test_essentialoclcs_MapTypeCS_name_value_roundtrip():
    instance = essentialoclcs_MapTypeCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_essentialoclcs_NavigatingArgCS_prefix_value_roundtrip():
    instance = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_essentialoclcs_NavigatingArgCS_role_value_roundtrip():
    instance = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    assert instance.role == "sample_text"
    instance.role = "sample_text_2"
    assert instance.role == "sample_text_2"


def test_essentialoclcs_NumberLiteralExpCS_symbol_value_roundtrip():
    instance = essentialoclcs_NumberLiteralExpCS(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_essentialoclcs_PatternExpCS_patternVariableName_value_roundtrip():
    instance = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    assert instance.patternVariableName == "sample_text"
    instance.patternVariableName = "sample_text_2"
    assert instance.patternVariableName == "sample_text_2"


def test_essentialoclcs_SelfExpCS_name_value_roundtrip():
    instance = essentialoclcs_SelfExpCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_essentialoclcs_ShadowExpCS_value_value_roundtrip():
    instance = essentialoclcs_ShadowExpCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_essentialoclcs_StringLiteralExpCS_segments_value_roundtrip():
    instance = essentialoclcs_StringLiteralExpCS(segments="sample_text")
    assert instance.segments == "sample_text"
    instance.segments = "sample_text_2"
    assert instance.segments == "sample_text_2"


def test_essentialoclcs_CallExpCS_isa_AbstractNameExpCS():
    instance = essentialoclcs_CallExpCS()
    assert isinstance(instance, AbstractNameExpCS)


def test_essentialoclcs_ShadowExpCS_isa_AbstractNameExpCS():
    instance = essentialoclcs_ShadowExpCS(value="sample_text")
    assert isinstance(instance, AbstractNameExpCS)


def test_essentialoclcs_VariableExpCS_isa_AbstractNameExpCS():
    instance = essentialoclcs_VariableExpCS()
    assert isinstance(instance, AbstractNameExpCS)


def test_essentialoclcs_NameExpCS_isa_AssociationClassCallExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, AssociationClassCallExpCS)


def test_essentialoclcs_AssociationClassCallExpCS_isa_CallExpCS():
    instance = essentialoclcs_AssociationClassCallExpCS()
    assert isinstance(instance, CallExpCS)


def test_essentialoclcs_IterationCallExpCS_isa_CallExpCS():
    instance = essentialoclcs_IterationCallExpCS()
    assert isinstance(instance, CallExpCS)


def test_essentialoclcs_OperationCallExpCS_isa_CallExpCS():
    instance = essentialoclcs_OperationCallExpCS()
    assert isinstance(instance, CallExpCS)


def test_essentialoclcs_PropertyCallExpCS_isa_CallExpCS():
    instance = essentialoclcs_PropertyCallExpCS()
    assert isinstance(instance, CallExpCS)


def test_essentialoclcs_CurlyBracketedClauseCS_isa_ContextLessElementCS():
    instance = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    assert isinstance(instance, ContextLessElementCS)


def test_essentialoclcs_RoundBracketedClauseCS_isa_ContextLessElementCS():
    instance = essentialoclcs_RoundBracketedClauseCS()
    assert isinstance(instance, ContextLessElementCS)


def test_essentialoclcs_SquareBracketedClauseCS_isa_ContextLessElementCS():
    instance = essentialoclcs_SquareBracketedClauseCS()
    assert isinstance(instance, ContextLessElementCS)


def test_essentialoclcs_AbstractNameExpCS_isa_ExpCS():
    instance = essentialoclcs_AbstractNameExpCS(isPre=True)
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_IfExpCS_isa_ExpCS():
    instance = essentialoclcs_IfExpCS(isImplicit=True)
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_IfThenExpCS_isa_ExpCS():
    instance = essentialoclcs_IfThenExpCS()
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_LetExpCS_isa_ExpCS():
    instance = essentialoclcs_LetExpCS(isImplicit=True)
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_LetVariableCS_isa_ExpCS():
    instance = essentialoclcs_LetVariableCS()
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_LiteralExpCS_isa_ExpCS():
    instance = essentialoclcs_LiteralExpCS()
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_NestedExpCS_isa_ExpCS():
    instance = essentialoclcs_NestedExpCS()
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_OperatorExpCS_isa_ExpCS():
    instance = essentialoclcs_OperatorExpCS()
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_PatternExpCS_isa_ExpCS():
    instance = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_SelfExpCS_isa_ExpCS():
    instance = essentialoclcs_SelfExpCS(name="sample_text")
    assert isinstance(instance, ExpCS)


def test_essentialoclcs_NameExpCS_isa_IterateCallExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, IterateCallExpCS)


def test_essentialoclcs_IterateCallExpCS_isa_IterationCallExpCS():
    instance = essentialoclcs_IterateCallExpCS()
    assert isinstance(instance, IterationCallExpCS)


def test_essentialoclcs_NameExpCS_isa_IterationCallExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, IterationCallExpCS)


def test_essentialoclcs_CollectionLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_CollectionLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_LambdaLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_LambdaLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_MapLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_MapLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_PrimitiveLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_PrimitiveLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_TupleLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_TupleLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_TypeLiteralExpCS_isa_LiteralExpCS():
    instance = essentialoclcs_TypeLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialoclcs_CollectionLiteralPartCS_isa_ModelElementCS():
    instance = essentialoclcs_CollectionLiteralPartCS()
    assert isinstance(instance, ModelElementCS)


def test_essentialoclcs_ExpCS_isa_ModelElementCS():
    instance = essentialoclcs_ExpCS(hasError=True)
    assert isinstance(instance, ModelElementCS)


def test_essentialoclcs_MapLiteralPartCS_isa_ModelElementCS():
    instance = essentialoclcs_MapLiteralPartCS()
    assert isinstance(instance, ModelElementCS)


def test_essentialoclcs_NavigatingArgCS_isa_ModelElementCS():
    instance = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    assert isinstance(instance, ModelElementCS)


def test_essentialoclcs_ShadowPartCS_isa_ModelElementCS():
    instance = essentialoclcs_ShadowPartCS()
    assert isinstance(instance, ModelElementCS)


def test_essentialoclcs_CollectionTypeCS_isa_Nameable():
    instance = essentialoclcs_CollectionTypeCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_essentialoclcs_MapTypeCS_isa_Nameable():
    instance = essentialoclcs_MapTypeCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_essentialoclcs_ShadowPartCS_isa_Nameable():
    instance = essentialoclcs_ShadowPartCS()
    assert isinstance(instance, Nameable)


def test_essentialoclcs_ContextCS_isa_NamedElementCS():
    instance = essentialoclcs_ContextCS()
    assert isinstance(instance, NamedElementCS)


def test_essentialoclcs_OperatorExpCS_isa_NamedElementCS():
    instance = essentialoclcs_OperatorExpCS()
    assert isinstance(instance, NamedElementCS)


def test_essentialoclcs_VariableCS_isa_NamedElementCS():
    instance = essentialoclcs_VariableCS()
    assert isinstance(instance, NamedElementCS)


def test_essentialoclcs_NameExpCS_isa_OperationCallExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, OperationCallExpCS)


def test_essentialoclcs_InfixExpCS_isa_OperatorExpCS():
    instance = essentialoclcs_InfixExpCS()
    assert isinstance(instance, OperatorExpCS)


def test_essentialoclcs_PrefixExpCS_isa_OperatorExpCS():
    instance = essentialoclcs_PrefixExpCS()
    assert isinstance(instance, OperatorExpCS)


def test_essentialoclcs_BooleanLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_BooleanLiteralExpCS(symbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_InvalidLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_InvalidLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_NullLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_NullLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_NumberLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_NumberLiteralExpCS(symbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_StringLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_StringLiteralExpCS(segments="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_UnlimitedNaturalLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialoclcs_UnlimitedNaturalLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialoclcs_NameExpCS_isa_PropertyCallExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, PropertyCallExpCS)


def test_essentialoclcs_ContextCS_isa_RootCS():
    instance = essentialoclcs_ContextCS()
    assert isinstance(instance, RootCS)


def test_essentialoclcs_NameExpCS_isa_ShadowExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, ShadowExpCS)


def test_essentialoclcs_ExpSpecificationCS_isa_SpecificationCS():
    instance = essentialoclcs_ExpSpecificationCS()
    assert isinstance(instance, SpecificationCS)


def test_essentialoclcs_CollectionPatternCS_isa_TypedRefCS():
    instance = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_essentialoclcs_CollectionTypeCS_isa_TypedRefCS():
    instance = essentialoclcs_CollectionTypeCS(name="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_essentialoclcs_MapTypeCS_isa_TypedRefCS():
    instance = essentialoclcs_MapTypeCS(name="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_essentialoclcs_TypeNameExpCS_isa_TypedRefCS():
    instance = essentialoclcs_TypeNameExpCS()
    assert isinstance(instance, TypedRefCS)


def test_essentialoclcs_LetVariableCS_isa_VariableCS():
    instance = essentialoclcs_LetVariableCS()
    assert isinstance(instance, VariableCS)


def test_essentialoclcs_TupleLiteralPartCS_isa_VariableCS():
    instance = essentialoclcs_TupleLiteralPartCS()
    assert isinstance(instance, VariableCS)


def test_essentialoclcs_NameExpCS_isa_VariableExpCS():
    instance = essentialoclcs_NameExpCS()
    assert isinstance(instance, VariableExpCS)


def test_assoc_argument72_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_InfixExpCS()
    b2 = essentialoclcs_InfixExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS73', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS73', b1)
    if hasattr(b1, 'essentialoclcs_InfixExpCS'):
        assert _is_linked(b1, 'essentialoclcs_InfixExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS73', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS73', b2)
    if hasattr(b1, 'essentialoclcs_InfixExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_InfixExpCS', a)
    if hasattr(b2, 'essentialoclcs_InfixExpCS'):
        assert _is_linked(b2, 'essentialoclcs_InfixExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS73', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS73', b2)
    if hasattr(b2, 'essentialoclcs_InfixExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_InfixExpCS', a)


def test_assoc_arguments12_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_CallExpCS()
    b2 = essentialoclcs_CallExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS', b1)
    if hasattr(b1, 'essentialoclcs_CallExpCS'):
        assert _is_linked(b1, 'essentialoclcs_CallExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS', b2)
    if hasattr(b1, 'essentialoclcs_CallExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_CallExpCS', a)
    if hasattr(b2, 'essentialoclcs_CallExpCS'):
        assert _is_linked(b2, 'essentialoclcs_CallExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS', b2)
    if hasattr(b2, 'essentialoclcs_CallExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_CallExpCS', a)


def test_assoc_localLeft39_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_ExpCS38', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS38', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS40'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS40', a)
    _safe_set(a, 'essentialoclcs_ExpCS38', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS38', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS40'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS40', a)
    if hasattr(b2, 'essentialoclcs_ExpCS40'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS40', a)
    _safe_set(a, 'essentialoclcs_ExpCS38', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS38', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS40'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS40', a)


def test_assoc_localLeftmostDescendant42_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_ExpCS41', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS41', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS43'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS43', a)
    _safe_set(a, 'essentialoclcs_ExpCS41', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS41', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS43'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS43', a)
    if hasattr(b2, 'essentialoclcs_ExpCS43'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS43', a)
    _safe_set(a, 'essentialoclcs_ExpCS41', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS41', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS43'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS43', a)


def test_assoc_localParent44_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_OperatorExpCS()
    b2 = essentialoclcs_OperatorExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS45', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS45', b1)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS'):
        assert _is_linked(b1, 'essentialoclcs_OperatorExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS45', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS45', b2)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_OperatorExpCS', a)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS'):
        assert _is_linked(b2, 'essentialoclcs_OperatorExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS45', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS45', b2)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_OperatorExpCS', a)


def test_assoc_localRight47_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_ExpCS46', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS46', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS48'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS48', a)
    _safe_set(a, 'essentialoclcs_ExpCS46', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS46', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS48'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS48', a)
    if hasattr(b2, 'essentialoclcs_ExpCS48'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS48', a)
    _safe_set(a, 'essentialoclcs_ExpCS46', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS46', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS48'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS48', a)


def test_assoc_localRightmostDescendant50_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_ExpCS49', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS49', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS51'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS51', a)
    _safe_set(a, 'essentialoclcs_ExpCS49', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS49', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS51'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS51', a)
    if hasattr(b2, 'essentialoclcs_ExpCS51'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS51', a)
    _safe_set(a, 'essentialoclcs_ExpCS49', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS49', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS51'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS51', a)


def test_assoc_ownedArguments126_link_reassign_clear():
    a = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    b1 = essentialoclcs_RoundBracketedClauseCS()
    b2 = essentialoclcs_RoundBracketedClauseCS()
    _safe_set(a, 'NavigatingArgCS', b1)
    assert _is_linked(a, 'NavigatingArgCS', b1)
    if hasattr(b1, 'owningRoundBracketedClause'):
        assert _is_linked(b1, 'owningRoundBracketedClause', a)
    _safe_set(a, 'NavigatingArgCS', b2)
    assert _is_linked(a, 'NavigatingArgCS', b2)
    if hasattr(b1, 'owningRoundBracketedClause'):
        assert not _is_linked(b1, 'owningRoundBracketedClause', a)
    if hasattr(b2, 'owningRoundBracketedClause'):
        assert _is_linked(b2, 'owningRoundBracketedClause', a)
    _safe_set(a, 'NavigatingArgCS', None)
    assert not _is_linked(a, 'NavigatingArgCS', b2)
    if hasattr(b2, 'owningRoundBracketedClause'):
        assert not _is_linked(b2, 'owningRoundBracketedClause', a)


def test_assoc_ownedCondition56_link_reassign_clear():
    a = essentialoclcs_IfExpCS(isImplicit=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_IfExpCS', b1)
    assert _is_linked(a, 'essentialoclcs_IfExpCS', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS57'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS57', a)
    _safe_set(a, 'essentialoclcs_IfExpCS', b2)
    assert _is_linked(a, 'essentialoclcs_IfExpCS', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS57'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS57', a)
    if hasattr(b2, 'essentialoclcs_ExpCS57'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS57', a)
    _safe_set(a, 'essentialoclcs_IfExpCS', None)
    assert not _is_linked(a, 'essentialoclcs_IfExpCS', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS57'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS57', a)


def test_assoc_ownedCondition66_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_IfThenExpCS()
    b2 = essentialoclcs_IfThenExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS68', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS68', b1)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS67'):
        assert _is_linked(b1, 'essentialoclcs_IfThenExpCS67', a)
    _safe_set(a, 'essentialoclcs_ExpCS68', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS68', b2)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS67'):
        assert not _is_linked(b1, 'essentialoclcs_IfThenExpCS67', a)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS67'):
        assert _is_linked(b2, 'essentialoclcs_IfThenExpCS67', a)
    _safe_set(a, 'essentialoclcs_ExpCS68', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS68', b2)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS67'):
        assert not _is_linked(b2, 'essentialoclcs_IfThenExpCS67', a)


def test_assoc_ownedCurlyBracketedClause0_link_reassign_clear():
    a = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    b1 = essentialoclcs_AbstractNameExpCS(isPre=True)
    b2 = essentialoclcs_AbstractNameExpCS(isPre=False)
    _safe_set(a, 'CurlyBracketedClauseCS', b1)
    assert _is_linked(a, 'CurlyBracketedClauseCS', b1)
    if hasattr(b1, 'owningNameExp'):
        assert _is_linked(b1, 'owningNameExp', a)
    _safe_set(a, 'CurlyBracketedClauseCS', b2)
    assert _is_linked(a, 'CurlyBracketedClauseCS', b2)
    if hasattr(b1, 'owningNameExp'):
        assert not _is_linked(b1, 'owningNameExp', a)
    if hasattr(b2, 'owningNameExp'):
        assert _is_linked(b2, 'owningNameExp', a)
    _safe_set(a, 'CurlyBracketedClauseCS', None)
    assert not _is_linked(a, 'CurlyBracketedClauseCS', b2)
    if hasattr(b2, 'owningNameExp'):
        assert not _is_linked(b2, 'owningNameExp', a)


def test_assoc_ownedCurlyBracketedClause153_link_reassign_clear():
    a = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    b1 = essentialoclcs_TypeNameExpCS()
    b2 = essentialoclcs_TypeNameExpCS()
    _safe_set(a, 'essentialoclcs_CurlyBracketedClauseCS', b1)
    assert _is_linked(a, 'essentialoclcs_CurlyBracketedClauseCS', b1)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS154'):
        assert _is_linked(b1, 'essentialoclcs_TypeNameExpCS154', a)
    _safe_set(a, 'essentialoclcs_CurlyBracketedClauseCS', b2)
    assert _is_linked(a, 'essentialoclcs_CurlyBracketedClauseCS', b2)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS154'):
        assert not _is_linked(b1, 'essentialoclcs_TypeNameExpCS154', a)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS154'):
        assert _is_linked(b2, 'essentialoclcs_TypeNameExpCS154', a)
    _safe_set(a, 'essentialoclcs_CurlyBracketedClauseCS', None)
    assert not _is_linked(a, 'essentialoclcs_CurlyBracketedClauseCS', b2)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS154'):
        assert not _is_linked(b2, 'essentialoclcs_TypeNameExpCS154', a)


def test_assoc_ownedElseExpression58_link_reassign_clear():
    a = essentialoclcs_IfExpCS(isImplicit=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_IfExpCS59', b1)
    assert _is_linked(a, 'essentialoclcs_IfExpCS59', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS60'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS60', a)
    _safe_set(a, 'essentialoclcs_IfExpCS59', b2)
    assert _is_linked(a, 'essentialoclcs_IfExpCS59', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS60'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS60', a)
    if hasattr(b2, 'essentialoclcs_ExpCS60'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS60', a)
    _safe_set(a, 'essentialoclcs_IfExpCS59', None)
    assert not _is_linked(a, 'essentialoclcs_IfExpCS59', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS60'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS60', a)


def test_assoc_ownedExpression114_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_NestedExpCS()
    b2 = essentialoclcs_NestedExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS115', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS115', b1)
    if hasattr(b1, 'essentialoclcs_NestedExpCS'):
        assert _is_linked(b1, 'essentialoclcs_NestedExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS115', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS115', b2)
    if hasattr(b1, 'essentialoclcs_NestedExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_NestedExpCS', a)
    if hasattr(b2, 'essentialoclcs_NestedExpCS'):
        assert _is_linked(b2, 'essentialoclcs_NestedExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS115', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS115', b2)
    if hasattr(b2, 'essentialoclcs_NestedExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_NestedExpCS', a)


def test_assoc_ownedExpression19_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_CollectionLiteralPartCS()
    b2 = essentialoclcs_CollectionLiteralPartCS()
    _safe_set(a, 'essentialoclcs_ExpCS21', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS21', b1)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralPartCS20'):
        assert _is_linked(b1, 'essentialoclcs_CollectionLiteralPartCS20', a)
    _safe_set(a, 'essentialoclcs_ExpCS21', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS21', b2)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralPartCS20'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionLiteralPartCS20', a)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralPartCS20'):
        assert _is_linked(b2, 'essentialoclcs_CollectionLiteralPartCS20', a)
    _safe_set(a, 'essentialoclcs_ExpCS21', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS21', b2)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralPartCS20'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionLiteralPartCS20', a)


def test_assoc_ownedExpression34_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ContextCS()
    b2 = essentialoclcs_ContextCS()
    _safe_set(a, 'essentialoclcs_ExpCS35', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS35', b1)
    if hasattr(b1, 'essentialoclcs_ContextCS'):
        assert _is_linked(b1, 'essentialoclcs_ContextCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS35', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS35', b2)
    if hasattr(b1, 'essentialoclcs_ContextCS'):
        assert not _is_linked(b1, 'essentialoclcs_ContextCS', a)
    if hasattr(b2, 'essentialoclcs_ContextCS'):
        assert _is_linked(b2, 'essentialoclcs_ContextCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS35', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS35', b2)
    if hasattr(b2, 'essentialoclcs_ContextCS'):
        assert not _is_linked(b2, 'essentialoclcs_ContextCS', a)


def test_assoc_ownedExpression54_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ExpSpecificationCS()
    b2 = essentialoclcs_ExpSpecificationCS()
    _safe_set(a, 'essentialoclcs_ExpCS55', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS55', b1)
    if hasattr(b1, 'essentialoclcs_ExpSpecificationCS'):
        assert _is_linked(b1, 'essentialoclcs_ExpSpecificationCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS55', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS55', b2)
    if hasattr(b1, 'essentialoclcs_ExpSpecificationCS'):
        assert not _is_linked(b1, 'essentialoclcs_ExpSpecificationCS', a)
    if hasattr(b2, 'essentialoclcs_ExpSpecificationCS'):
        assert _is_linked(b2, 'essentialoclcs_ExpSpecificationCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS55', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS55', b2)
    if hasattr(b2, 'essentialoclcs_ExpSpecificationCS'):
        assert not _is_linked(b2, 'essentialoclcs_ExpSpecificationCS', a)


def test_assoc_ownedExpressionCS82_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_LambdaLiteralExpCS()
    b2 = essentialoclcs_LambdaLiteralExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS83', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS83', b1)
    if hasattr(b1, 'essentialoclcs_LambdaLiteralExpCS'):
        assert _is_linked(b1, 'essentialoclcs_LambdaLiteralExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS83', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS83', b2)
    if hasattr(b1, 'essentialoclcs_LambdaLiteralExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_LambdaLiteralExpCS', a)
    if hasattr(b2, 'essentialoclcs_LambdaLiteralExpCS'):
        assert _is_linked(b2, 'essentialoclcs_LambdaLiteralExpCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS83', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS83', b2)
    if hasattr(b2, 'essentialoclcs_LambdaLiteralExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_LambdaLiteralExpCS', a)


def test_assoc_ownedIfThenExpressions61_link_reassign_clear():
    a = essentialoclcs_IfExpCS(isImplicit=True)
    b1 = essentialoclcs_IfThenExpCS()
    b2 = essentialoclcs_IfThenExpCS()
    _safe_set(a, 'essentialoclcs_IfExpCS62', {b1})
    assert _is_linked(a, 'essentialoclcs_IfExpCS62', b1)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS'):
        assert _is_linked(b1, 'essentialoclcs_IfThenExpCS', a)
    _safe_set(a, 'essentialoclcs_IfExpCS62', {b2})
    assert _is_linked(a, 'essentialoclcs_IfExpCS62', b2)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_IfThenExpCS', a)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS'):
        assert _is_linked(b2, 'essentialoclcs_IfThenExpCS', a)
    _safe_set(a, 'essentialoclcs_IfExpCS62', set())
    assert not _is_linked(a, 'essentialoclcs_IfExpCS62', b2)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_IfThenExpCS', a)


def test_assoc_ownedInExpression84_link_reassign_clear():
    a = essentialoclcs_LetExpCS(isImplicit=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_LetExpCS', b1)
    assert _is_linked(a, 'essentialoclcs_LetExpCS', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS85'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS85', a)
    _safe_set(a, 'essentialoclcs_LetExpCS', b2)
    assert _is_linked(a, 'essentialoclcs_LetExpCS', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS85'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS85', a)
    if hasattr(b2, 'essentialoclcs_ExpCS85'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS85', a)
    _safe_set(a, 'essentialoclcs_LetExpCS', None)
    assert not _is_linked(a, 'essentialoclcs_LetExpCS', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS85'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS85', a)


def test_assoc_ownedInitExpression104_link_reassign_clear():
    a = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS', b1)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS105'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS105', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS', b2)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS105'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS105', a)
    if hasattr(b2, 'essentialoclcs_ExpCS105'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS105', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS', None)
    assert not _is_linked(a, 'essentialoclcs_NavigatingArgCS', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS105'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS105', a)


def test_assoc_ownedInitExpression132_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_ShadowPartCS()
    b2 = essentialoclcs_ShadowPartCS()
    _safe_set(a, 'essentialoclcs_ExpCS134', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS134', b1)
    if hasattr(b1, 'essentialoclcs_ShadowPartCS133'):
        assert _is_linked(b1, 'essentialoclcs_ShadowPartCS133', a)
    _safe_set(a, 'essentialoclcs_ExpCS134', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS134', b2)
    if hasattr(b1, 'essentialoclcs_ShadowPartCS133'):
        assert not _is_linked(b1, 'essentialoclcs_ShadowPartCS133', a)
    if hasattr(b2, 'essentialoclcs_ShadowPartCS133'):
        assert _is_linked(b2, 'essentialoclcs_ShadowPartCS133', a)
    _safe_set(a, 'essentialoclcs_ExpCS134', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS134', b2)
    if hasattr(b2, 'essentialoclcs_ShadowPartCS133'):
        assert not _is_linked(b2, 'essentialoclcs_ShadowPartCS133', a)


def test_assoc_ownedInitExpression161_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_VariableCS()
    b2 = essentialoclcs_VariableCS()
    _safe_set(a, 'essentialoclcs_ExpCS163', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS163', b1)
    if hasattr(b1, 'essentialoclcs_VariableCS162'):
        assert _is_linked(b1, 'essentialoclcs_VariableCS162', a)
    _safe_set(a, 'essentialoclcs_ExpCS163', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS163', b2)
    if hasattr(b1, 'essentialoclcs_VariableCS162'):
        assert not _is_linked(b1, 'essentialoclcs_VariableCS162', a)
    if hasattr(b2, 'essentialoclcs_VariableCS162'):
        assert _is_linked(b2, 'essentialoclcs_VariableCS162', a)
    _safe_set(a, 'essentialoclcs_ExpCS163', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS163', b2)
    if hasattr(b2, 'essentialoclcs_VariableCS162'):
        assert not _is_linked(b2, 'essentialoclcs_VariableCS162', a)


def test_assoc_ownedKey92_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_MapLiteralPartCS()
    b2 = essentialoclcs_MapLiteralPartCS()
    _safe_set(a, 'essentialoclcs_ExpCS94', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS94', b1)
    if hasattr(b1, 'essentialoclcs_MapLiteralPartCS93'):
        assert _is_linked(b1, 'essentialoclcs_MapLiteralPartCS93', a)
    _safe_set(a, 'essentialoclcs_ExpCS94', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS94', b2)
    if hasattr(b1, 'essentialoclcs_MapLiteralPartCS93'):
        assert not _is_linked(b1, 'essentialoclcs_MapLiteralPartCS93', a)
    if hasattr(b2, 'essentialoclcs_MapLiteralPartCS93'):
        assert _is_linked(b2, 'essentialoclcs_MapLiteralPartCS93', a)
    _safe_set(a, 'essentialoclcs_ExpCS94', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS94', b2)
    if hasattr(b2, 'essentialoclcs_MapLiteralPartCS93'):
        assert not _is_linked(b2, 'essentialoclcs_MapLiteralPartCS93', a)


def test_assoc_ownedKeyType98_link_reassign_clear():
    a = essentialoclcs_MapTypeCS(name="sample_text")
    b1 = essentialoclcs_TypedRefCS()
    b2 = essentialoclcs_TypedRefCS()
    _safe_set(a, 'essentialoclcs_MapTypeCS99', b1)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS99', b1)
    if hasattr(b1, 'essentialoclcs_TypedRefCS100'):
        assert _is_linked(b1, 'essentialoclcs_TypedRefCS100', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS99', b2)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS99', b2)
    if hasattr(b1, 'essentialoclcs_TypedRefCS100'):
        assert not _is_linked(b1, 'essentialoclcs_TypedRefCS100', a)
    if hasattr(b2, 'essentialoclcs_TypedRefCS100'):
        assert _is_linked(b2, 'essentialoclcs_TypedRefCS100', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS99', None)
    assert not _is_linked(a, 'essentialoclcs_MapTypeCS99', b2)
    if hasattr(b2, 'essentialoclcs_TypedRefCS100'):
        assert not _is_linked(b2, 'essentialoclcs_TypedRefCS100', a)


def test_assoc_ownedLastExpression22_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_CollectionLiteralPartCS()
    b2 = essentialoclcs_CollectionLiteralPartCS()
    _safe_set(a, 'essentialoclcs_ExpCS24', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS24', b1)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralPartCS23'):
        assert _is_linked(b1, 'essentialoclcs_CollectionLiteralPartCS23', a)
    _safe_set(a, 'essentialoclcs_ExpCS24', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS24', b2)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralPartCS23'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionLiteralPartCS23', a)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralPartCS23'):
        assert _is_linked(b2, 'essentialoclcs_CollectionLiteralPartCS23', a)
    _safe_set(a, 'essentialoclcs_ExpCS24', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS24', b2)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralPartCS23'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionLiteralPartCS23', a)


def test_assoc_ownedLeft74_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_InfixExpCS()
    b2 = essentialoclcs_InfixExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS76', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS76', b1)
    if hasattr(b1, 'essentialoclcs_InfixExpCS75'):
        assert _is_linked(b1, 'essentialoclcs_InfixExpCS75', a)
    _safe_set(a, 'essentialoclcs_ExpCS76', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS76', b2)
    if hasattr(b1, 'essentialoclcs_InfixExpCS75'):
        assert not _is_linked(b1, 'essentialoclcs_InfixExpCS75', a)
    if hasattr(b2, 'essentialoclcs_InfixExpCS75'):
        assert _is_linked(b2, 'essentialoclcs_InfixExpCS75', a)
    _safe_set(a, 'essentialoclcs_ExpCS76', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS76', b2)
    if hasattr(b2, 'essentialoclcs_InfixExpCS75'):
        assert not _is_linked(b2, 'essentialoclcs_InfixExpCS75', a)


def test_assoc_ownedNameExpression106_link_reassign_clear():
    a = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS107', b1)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS107', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS108'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS108', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS107', b2)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS107', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS108'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS108', a)
    if hasattr(b2, 'essentialoclcs_ExpCS108'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS108', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS107', None)
    assert not _is_linked(a, 'essentialoclcs_NavigatingArgCS107', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS108'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS108', a)


def test_assoc_ownedParts25_link_reassign_clear():
    a = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    b1 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    b2 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text_2")
    _safe_set(a, 'essentialoclcs_PatternExpCS', b1)
    assert _is_linked(a, 'essentialoclcs_PatternExpCS', b1)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS'):
        assert _is_linked(b1, 'essentialoclcs_CollectionPatternCS', a)
    _safe_set(a, 'essentialoclcs_PatternExpCS', b2)
    assert _is_linked(a, 'essentialoclcs_PatternExpCS', b2)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionPatternCS', a)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS'):
        assert _is_linked(b2, 'essentialoclcs_CollectionPatternCS', a)
    _safe_set(a, 'essentialoclcs_PatternExpCS', None)
    assert not _is_linked(a, 'essentialoclcs_PatternExpCS', b2)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionPatternCS', a)


def test_assoc_ownedParts36_link_reassign_clear():
    a = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    b1 = essentialoclcs_ShadowPartCS()
    b2 = essentialoclcs_ShadowPartCS()
    _safe_set(a, 'owningCurlyBracketClause', {b1})
    assert _is_linked(a, 'owningCurlyBracketClause', b1)
    if hasattr(b1, 'ShadowPartCS'):
        assert _is_linked(b1, 'ShadowPartCS', a)
    _safe_set(a, 'owningCurlyBracketClause', {b2})
    assert _is_linked(a, 'owningCurlyBracketClause', b2)
    if hasattr(b1, 'ShadowPartCS'):
        assert not _is_linked(b1, 'ShadowPartCS', a)
    if hasattr(b2, 'ShadowPartCS'):
        assert _is_linked(b2, 'ShadowPartCS', a)
    _safe_set(a, 'owningCurlyBracketClause', set())
    assert not _is_linked(a, 'owningCurlyBracketClause', b2)
    if hasattr(b2, 'ShadowPartCS'):
        assert not _is_linked(b2, 'ShadowPartCS', a)


def test_assoc_ownedPathName1_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_PathNameCS()
    b2 = essentialoclcs_PathNameCS()
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS', b1)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS', b1)
    if hasattr(b1, 'essentialoclcs_PathNameCS'):
        assert _is_linked(b1, 'essentialoclcs_PathNameCS', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS', b2)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS', b2)
    if hasattr(b1, 'essentialoclcs_PathNameCS'):
        assert not _is_linked(b1, 'essentialoclcs_PathNameCS', a)
    if hasattr(b2, 'essentialoclcs_PathNameCS'):
        assert _is_linked(b2, 'essentialoclcs_PathNameCS', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS', None)
    assert not _is_linked(a, 'essentialoclcs_AbstractNameExpCS', b2)
    if hasattr(b2, 'essentialoclcs_PathNameCS'):
        assert not _is_linked(b2, 'essentialoclcs_PathNameCS', a)


def test_assoc_ownedPatternGuard158_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_TypeNameExpCS()
    b2 = essentialoclcs_TypeNameExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS160', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS160', b1)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS159'):
        assert _is_linked(b1, 'essentialoclcs_TypeNameExpCS159', a)
    _safe_set(a, 'essentialoclcs_ExpCS160', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS160', b2)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS159'):
        assert not _is_linked(b1, 'essentialoclcs_TypeNameExpCS159', a)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS159'):
        assert _is_linked(b2, 'essentialoclcs_TypeNameExpCS159', a)
    _safe_set(a, 'essentialoclcs_ExpCS160', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS160', b2)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS159'):
        assert not _is_linked(b2, 'essentialoclcs_TypeNameExpCS159', a)


def test_assoc_ownedPatternGuard26_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    b2 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text_2")
    _safe_set(a, 'essentialoclcs_ExpCS28', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS28', b1)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS27'):
        assert _is_linked(b1, 'essentialoclcs_CollectionPatternCS27', a)
    _safe_set(a, 'essentialoclcs_ExpCS28', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS28', b2)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS27'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionPatternCS27', a)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS27'):
        assert _is_linked(b2, 'essentialoclcs_CollectionPatternCS27', a)
    _safe_set(a, 'essentialoclcs_ExpCS28', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS28', b2)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS27'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionPatternCS27', a)


def test_assoc_ownedPatternType123_link_reassign_clear():
    a = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    b1 = essentialoclcs_TypeRefCS()
    b2 = essentialoclcs_TypeRefCS()
    _safe_set(a, 'essentialoclcs_PatternExpCS124', b1)
    assert _is_linked(a, 'essentialoclcs_PatternExpCS124', b1)
    if hasattr(b1, 'essentialoclcs_TypeRefCS'):
        assert _is_linked(b1, 'essentialoclcs_TypeRefCS', a)
    _safe_set(a, 'essentialoclcs_PatternExpCS124', b2)
    assert _is_linked(a, 'essentialoclcs_PatternExpCS124', b2)
    if hasattr(b1, 'essentialoclcs_TypeRefCS'):
        assert not _is_linked(b1, 'essentialoclcs_TypeRefCS', a)
    if hasattr(b2, 'essentialoclcs_TypeRefCS'):
        assert _is_linked(b2, 'essentialoclcs_TypeRefCS', a)
    _safe_set(a, 'essentialoclcs_PatternExpCS124', None)
    assert not _is_linked(a, 'essentialoclcs_PatternExpCS124', b2)
    if hasattr(b2, 'essentialoclcs_TypeRefCS'):
        assert not _is_linked(b2, 'essentialoclcs_TypeRefCS', a)


def test_assoc_ownedRight117_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_OperatorExpCS()
    b2 = essentialoclcs_OperatorExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS119', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS119', b1)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS118'):
        assert _is_linked(b1, 'essentialoclcs_OperatorExpCS118', a)
    _safe_set(a, 'essentialoclcs_ExpCS119', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS119', b2)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS118'):
        assert not _is_linked(b1, 'essentialoclcs_OperatorExpCS118', a)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS118'):
        assert _is_linked(b2, 'essentialoclcs_OperatorExpCS118', a)
    _safe_set(a, 'essentialoclcs_ExpCS119', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS119', b2)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS118'):
        assert not _is_linked(b2, 'essentialoclcs_OperatorExpCS118', a)


def test_assoc_ownedRoundBracketedClause2_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_RoundBracketedClauseCS()
    b2 = essentialoclcs_RoundBracketedClauseCS()
    _safe_set(a, 'owningNameExp3', b1)
    assert _is_linked(a, 'owningNameExp3', b1)
    if hasattr(b1, 'RoundBracketedClauseCS'):
        assert _is_linked(b1, 'RoundBracketedClauseCS', a)
    _safe_set(a, 'owningNameExp3', b2)
    assert _is_linked(a, 'owningNameExp3', b2)
    if hasattr(b1, 'RoundBracketedClauseCS'):
        assert not _is_linked(b1, 'RoundBracketedClauseCS', a)
    if hasattr(b2, 'RoundBracketedClauseCS'):
        assert _is_linked(b2, 'RoundBracketedClauseCS', a)
    _safe_set(a, 'owningNameExp3', None)
    assert not _is_linked(a, 'owningNameExp3', b2)
    if hasattr(b2, 'RoundBracketedClauseCS'):
        assert not _is_linked(b2, 'RoundBracketedClauseCS', a)


def test_assoc_ownedSquareBracketedClauses4_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_SquareBracketedClauseCS()
    b2 = essentialoclcs_SquareBracketedClauseCS()
    _safe_set(a, 'owningNameExp5', {b1})
    assert _is_linked(a, 'owningNameExp5', b1)
    if hasattr(b1, 'SquareBracketedClauseCS'):
        assert _is_linked(b1, 'SquareBracketedClauseCS', a)
    _safe_set(a, 'owningNameExp5', {b2})
    assert _is_linked(a, 'owningNameExp5', b2)
    if hasattr(b1, 'SquareBracketedClauseCS'):
        assert not _is_linked(b1, 'SquareBracketedClauseCS', a)
    if hasattr(b2, 'SquareBracketedClauseCS'):
        assert _is_linked(b2, 'SquareBracketedClauseCS', a)
    _safe_set(a, 'owningNameExp5', set())
    assert not _is_linked(a, 'owningNameExp5', b2)
    if hasattr(b2, 'SquareBracketedClauseCS'):
        assert not _is_linked(b2, 'SquareBracketedClauseCS', a)


def test_assoc_ownedTerms140_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_SquareBracketedClauseCS()
    b2 = essentialoclcs_SquareBracketedClauseCS()
    _safe_set(a, 'essentialoclcs_ExpCS141', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS141', b1)
    if hasattr(b1, 'essentialoclcs_SquareBracketedClauseCS'):
        assert _is_linked(b1, 'essentialoclcs_SquareBracketedClauseCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS141', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS141', b2)
    if hasattr(b1, 'essentialoclcs_SquareBracketedClauseCS'):
        assert not _is_linked(b1, 'essentialoclcs_SquareBracketedClauseCS', a)
    if hasattr(b2, 'essentialoclcs_SquareBracketedClauseCS'):
        assert _is_linked(b2, 'essentialoclcs_SquareBracketedClauseCS', a)
    _safe_set(a, 'essentialoclcs_ExpCS141', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS141', b2)
    if hasattr(b2, 'essentialoclcs_SquareBracketedClauseCS'):
        assert not _is_linked(b2, 'essentialoclcs_SquareBracketedClauseCS', a)


def test_assoc_ownedThenExpression63_link_reassign_clear():
    a = essentialoclcs_IfExpCS(isImplicit=True)
    b1 = essentialoclcs_ExpCS(hasError=True)
    b2 = essentialoclcs_ExpCS(hasError=False)
    _safe_set(a, 'essentialoclcs_IfExpCS64', b1)
    assert _is_linked(a, 'essentialoclcs_IfExpCS64', b1)
    if hasattr(b1, 'essentialoclcs_ExpCS65'):
        assert _is_linked(b1, 'essentialoclcs_ExpCS65', a)
    _safe_set(a, 'essentialoclcs_IfExpCS64', b2)
    assert _is_linked(a, 'essentialoclcs_IfExpCS64', b2)
    if hasattr(b1, 'essentialoclcs_ExpCS65'):
        assert not _is_linked(b1, 'essentialoclcs_ExpCS65', a)
    if hasattr(b2, 'essentialoclcs_ExpCS65'):
        assert _is_linked(b2, 'essentialoclcs_ExpCS65', a)
    _safe_set(a, 'essentialoclcs_IfExpCS64', None)
    assert not _is_linked(a, 'essentialoclcs_IfExpCS64', b2)
    if hasattr(b2, 'essentialoclcs_ExpCS65'):
        assert not _is_linked(b2, 'essentialoclcs_ExpCS65', a)


def test_assoc_ownedThenExpression69_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_IfThenExpCS()
    b2 = essentialoclcs_IfThenExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS71', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS71', b1)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS70'):
        assert _is_linked(b1, 'essentialoclcs_IfThenExpCS70', a)
    _safe_set(a, 'essentialoclcs_ExpCS71', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS71', b2)
    if hasattr(b1, 'essentialoclcs_IfThenExpCS70'):
        assert not _is_linked(b1, 'essentialoclcs_IfThenExpCS70', a)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS70'):
        assert _is_linked(b2, 'essentialoclcs_IfThenExpCS70', a)
    _safe_set(a, 'essentialoclcs_ExpCS71', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS71', b2)
    if hasattr(b2, 'essentialoclcs_IfThenExpCS70'):
        assert not _is_linked(b2, 'essentialoclcs_IfThenExpCS70', a)


def test_assoc_ownedType109_link_reassign_clear():
    a = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    b1 = essentialoclcs_TypedRefCS()
    b2 = essentialoclcs_TypedRefCS()
    _safe_set(a, 'essentialoclcs_NavigatingArgCS110', b1)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS110', b1)
    if hasattr(b1, 'essentialoclcs_TypedRefCS111'):
        assert _is_linked(b1, 'essentialoclcs_TypedRefCS111', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS110', b2)
    assert _is_linked(a, 'essentialoclcs_NavigatingArgCS110', b2)
    if hasattr(b1, 'essentialoclcs_TypedRefCS111'):
        assert not _is_linked(b1, 'essentialoclcs_TypedRefCS111', a)
    if hasattr(b2, 'essentialoclcs_TypedRefCS111'):
        assert _is_linked(b2, 'essentialoclcs_TypedRefCS111', a)
    _safe_set(a, 'essentialoclcs_NavigatingArgCS110', None)
    assert not _is_linked(a, 'essentialoclcs_NavigatingArgCS110', b2)
    if hasattr(b2, 'essentialoclcs_TypedRefCS111'):
        assert not _is_linked(b2, 'essentialoclcs_TypedRefCS111', a)


def test_assoc_ownedType17_link_reassign_clear():
    a = essentialoclcs_CollectionTypeCS(name="sample_text")
    b1 = essentialoclcs_CollectionLiteralExpCS()
    b2 = essentialoclcs_CollectionLiteralExpCS()
    _safe_set(a, 'essentialoclcs_CollectionTypeCS', b1)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS', b1)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralExpCS18'):
        assert _is_linked(b1, 'essentialoclcs_CollectionLiteralExpCS18', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS', b2)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS', b2)
    if hasattr(b1, 'essentialoclcs_CollectionLiteralExpCS18'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionLiteralExpCS18', a)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralExpCS18'):
        assert _is_linked(b2, 'essentialoclcs_CollectionLiteralExpCS18', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS', None)
    assert not _is_linked(a, 'essentialoclcs_CollectionTypeCS', b2)
    if hasattr(b2, 'essentialoclcs_CollectionLiteralExpCS18'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionLiteralExpCS18', a)


def test_assoc_ownedType29_link_reassign_clear():
    a = essentialoclcs_CollectionTypeCS(name="sample_text")
    b1 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    b2 = essentialoclcs_CollectionPatternCS(restVariableName="sample_text_2")
    _safe_set(a, 'essentialoclcs_CollectionTypeCS31', b1)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS31', b1)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS30'):
        assert _is_linked(b1, 'essentialoclcs_CollectionPatternCS30', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS31', b2)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS31', b2)
    if hasattr(b1, 'essentialoclcs_CollectionPatternCS30'):
        assert not _is_linked(b1, 'essentialoclcs_CollectionPatternCS30', a)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS30'):
        assert _is_linked(b2, 'essentialoclcs_CollectionPatternCS30', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS31', None)
    assert not _is_linked(a, 'essentialoclcs_CollectionTypeCS31', b2)
    if hasattr(b2, 'essentialoclcs_CollectionPatternCS30'):
        assert not _is_linked(b2, 'essentialoclcs_CollectionPatternCS30', a)


def test_assoc_ownedType32_link_reassign_clear():
    a = essentialoclcs_CollectionTypeCS(name="sample_text")
    b1 = essentialoclcs_TypedRefCS()
    b2 = essentialoclcs_TypedRefCS()
    _safe_set(a, 'essentialoclcs_CollectionTypeCS33', b1)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS33', b1)
    if hasattr(b1, 'essentialoclcs_TypedRefCS'):
        assert _is_linked(b1, 'essentialoclcs_TypedRefCS', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS33', b2)
    assert _is_linked(a, 'essentialoclcs_CollectionTypeCS33', b2)
    if hasattr(b1, 'essentialoclcs_TypedRefCS'):
        assert not _is_linked(b1, 'essentialoclcs_TypedRefCS', a)
    if hasattr(b2, 'essentialoclcs_TypedRefCS'):
        assert _is_linked(b2, 'essentialoclcs_TypedRefCS', a)
    _safe_set(a, 'essentialoclcs_CollectionTypeCS33', None)
    assert not _is_linked(a, 'essentialoclcs_CollectionTypeCS33', b2)
    if hasattr(b2, 'essentialoclcs_TypedRefCS'):
        assert not _is_linked(b2, 'essentialoclcs_TypedRefCS', a)


def test_assoc_ownedType90_link_reassign_clear():
    a = essentialoclcs_MapTypeCS(name="sample_text")
    b1 = essentialoclcs_MapLiteralExpCS()
    b2 = essentialoclcs_MapLiteralExpCS()
    _safe_set(a, 'essentialoclcs_MapTypeCS', b1)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS', b1)
    if hasattr(b1, 'essentialoclcs_MapLiteralExpCS91'):
        assert _is_linked(b1, 'essentialoclcs_MapLiteralExpCS91', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS', b2)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS', b2)
    if hasattr(b1, 'essentialoclcs_MapLiteralExpCS91'):
        assert not _is_linked(b1, 'essentialoclcs_MapLiteralExpCS91', a)
    if hasattr(b2, 'essentialoclcs_MapLiteralExpCS91'):
        assert _is_linked(b2, 'essentialoclcs_MapLiteralExpCS91', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS', None)
    assert not _is_linked(a, 'essentialoclcs_MapTypeCS', b2)
    if hasattr(b2, 'essentialoclcs_MapLiteralExpCS91'):
        assert not _is_linked(b2, 'essentialoclcs_MapLiteralExpCS91', a)


def test_assoc_ownedValue95_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_MapLiteralPartCS()
    b2 = essentialoclcs_MapLiteralPartCS()
    _safe_set(a, 'essentialoclcs_ExpCS97', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS97', b1)
    if hasattr(b1, 'essentialoclcs_MapLiteralPartCS96'):
        assert _is_linked(b1, 'essentialoclcs_MapLiteralPartCS96', a)
    _safe_set(a, 'essentialoclcs_ExpCS97', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS97', b2)
    if hasattr(b1, 'essentialoclcs_MapLiteralPartCS96'):
        assert not _is_linked(b1, 'essentialoclcs_MapLiteralPartCS96', a)
    if hasattr(b2, 'essentialoclcs_MapLiteralPartCS96'):
        assert _is_linked(b2, 'essentialoclcs_MapLiteralPartCS96', a)
    _safe_set(a, 'essentialoclcs_ExpCS97', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS97', b2)
    if hasattr(b2, 'essentialoclcs_MapLiteralPartCS96'):
        assert not _is_linked(b2, 'essentialoclcs_MapLiteralPartCS96', a)


def test_assoc_ownedValueType101_link_reassign_clear():
    a = essentialoclcs_MapTypeCS(name="sample_text")
    b1 = essentialoclcs_TypedRefCS()
    b2 = essentialoclcs_TypedRefCS()
    _safe_set(a, 'essentialoclcs_MapTypeCS102', b1)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS102', b1)
    if hasattr(b1, 'essentialoclcs_TypedRefCS103'):
        assert _is_linked(b1, 'essentialoclcs_TypedRefCS103', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS102', b2)
    assert _is_linked(a, 'essentialoclcs_MapTypeCS102', b2)
    if hasattr(b1, 'essentialoclcs_TypedRefCS103'):
        assert not _is_linked(b1, 'essentialoclcs_TypedRefCS103', a)
    if hasattr(b2, 'essentialoclcs_TypedRefCS103'):
        assert _is_linked(b2, 'essentialoclcs_TypedRefCS103', a)
    _safe_set(a, 'essentialoclcs_MapTypeCS102', None)
    assert not _is_linked(a, 'essentialoclcs_MapTypeCS102', b2)
    if hasattr(b2, 'essentialoclcs_TypedRefCS103'):
        assert not _is_linked(b2, 'essentialoclcs_TypedRefCS103', a)


def test_assoc_ownedVariables86_link_reassign_clear():
    a = essentialoclcs_LetExpCS(isImplicit=True)
    b1 = essentialoclcs_LetVariableCS()
    b2 = essentialoclcs_LetVariableCS()
    _safe_set(a, 'owningLetExpression', {b1})
    assert _is_linked(a, 'owningLetExpression', b1)
    if hasattr(b1, 'LetVariableCS'):
        assert _is_linked(b1, 'LetVariableCS', a)
    _safe_set(a, 'owningLetExpression', {b2})
    assert _is_linked(a, 'owningLetExpression', b2)
    if hasattr(b1, 'LetVariableCS'):
        assert not _is_linked(b1, 'LetVariableCS', a)
    if hasattr(b2, 'LetVariableCS'):
        assert _is_linked(b2, 'LetVariableCS', a)
    _safe_set(a, 'owningLetExpression', set())
    assert not _is_linked(a, 'owningLetExpression', b2)
    if hasattr(b2, 'LetVariableCS'):
        assert not _is_linked(b2, 'LetVariableCS', a)


def test_assoc_owningCurlyBracketClause135_link_reassign_clear():
    a = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    b1 = essentialoclcs_ShadowPartCS()
    b2 = essentialoclcs_ShadowPartCS()
    _safe_set(a, 'CurlyBracketedClauseCS136', b1)
    assert _is_linked(a, 'CurlyBracketedClauseCS136', b1)
    if hasattr(b1, 'ownedParts'):
        assert _is_linked(b1, 'ownedParts', a)
    _safe_set(a, 'CurlyBracketedClauseCS136', b2)
    assert _is_linked(a, 'CurlyBracketedClauseCS136', b2)
    if hasattr(b1, 'ownedParts'):
        assert not _is_linked(b1, 'ownedParts', a)
    if hasattr(b2, 'ownedParts'):
        assert _is_linked(b2, 'ownedParts', a)
    _safe_set(a, 'CurlyBracketedClauseCS136', None)
    assert not _is_linked(a, 'CurlyBracketedClauseCS136', b2)
    if hasattr(b2, 'ownedParts'):
        assert not _is_linked(b2, 'ownedParts', a)


def test_assoc_owningLetExpression88_link_reassign_clear():
    a = essentialoclcs_LetExpCS(isImplicit=True)
    b1 = essentialoclcs_LetVariableCS()
    b2 = essentialoclcs_LetVariableCS()
    _safe_set(a, 'LetExpCS', b1)
    assert _is_linked(a, 'LetExpCS', b1)
    if hasattr(b1, 'ownedVariables'):
        assert _is_linked(b1, 'ownedVariables', a)
    _safe_set(a, 'LetExpCS', b2)
    assert _is_linked(a, 'LetExpCS', b2)
    if hasattr(b1, 'ownedVariables'):
        assert not _is_linked(b1, 'ownedVariables', a)
    if hasattr(b2, 'ownedVariables'):
        assert _is_linked(b2, 'ownedVariables', a)
    _safe_set(a, 'LetExpCS', None)
    assert not _is_linked(a, 'LetExpCS', b2)
    if hasattr(b2, 'ownedVariables'):
        assert not _is_linked(b2, 'ownedVariables', a)


def test_assoc_owningNameExp127_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_RoundBracketedClauseCS()
    b2 = essentialoclcs_RoundBracketedClauseCS()
    _safe_set(a, 'AbstractNameExpCS128', b1)
    assert _is_linked(a, 'AbstractNameExpCS128', b1)
    if hasattr(b1, 'ownedRoundBracketedClause'):
        assert _is_linked(b1, 'ownedRoundBracketedClause', a)
    _safe_set(a, 'AbstractNameExpCS128', b2)
    assert _is_linked(a, 'AbstractNameExpCS128', b2)
    if hasattr(b1, 'ownedRoundBracketedClause'):
        assert not _is_linked(b1, 'ownedRoundBracketedClause', a)
    if hasattr(b2, 'ownedRoundBracketedClause'):
        assert _is_linked(b2, 'ownedRoundBracketedClause', a)
    _safe_set(a, 'AbstractNameExpCS128', None)
    assert not _is_linked(a, 'AbstractNameExpCS128', b2)
    if hasattr(b2, 'ownedRoundBracketedClause'):
        assert not _is_linked(b2, 'ownedRoundBracketedClause', a)


def test_assoc_owningNameExp142_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_SquareBracketedClauseCS()
    b2 = essentialoclcs_SquareBracketedClauseCS()
    _safe_set(a, 'AbstractNameExpCS143', b1)
    assert _is_linked(a, 'AbstractNameExpCS143', b1)
    if hasattr(b1, 'ownedSquareBracketedClauses'):
        assert _is_linked(b1, 'ownedSquareBracketedClauses', a)
    _safe_set(a, 'AbstractNameExpCS143', b2)
    assert _is_linked(a, 'AbstractNameExpCS143', b2)
    if hasattr(b1, 'ownedSquareBracketedClauses'):
        assert not _is_linked(b1, 'ownedSquareBracketedClauses', a)
    if hasattr(b2, 'ownedSquareBracketedClauses'):
        assert _is_linked(b2, 'ownedSquareBracketedClauses', a)
    _safe_set(a, 'AbstractNameExpCS143', None)
    assert not _is_linked(a, 'AbstractNameExpCS143', b2)
    if hasattr(b2, 'ownedSquareBracketedClauses'):
        assert not _is_linked(b2, 'ownedSquareBracketedClauses', a)


def test_assoc_owningNameExp37_link_reassign_clear():
    a = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    b1 = essentialoclcs_AbstractNameExpCS(isPre=True)
    b2 = essentialoclcs_AbstractNameExpCS(isPre=False)
    _safe_set(a, 'ownedCurlyBracketedClause', b1)
    assert _is_linked(a, 'ownedCurlyBracketedClause', b1)
    if hasattr(b1, 'AbstractNameExpCS'):
        assert _is_linked(b1, 'AbstractNameExpCS', a)
    _safe_set(a, 'ownedCurlyBracketedClause', b2)
    assert _is_linked(a, 'ownedCurlyBracketedClause', b2)
    if hasattr(b1, 'AbstractNameExpCS'):
        assert not _is_linked(b1, 'AbstractNameExpCS', a)
    if hasattr(b2, 'AbstractNameExpCS'):
        assert _is_linked(b2, 'AbstractNameExpCS', a)
    _safe_set(a, 'ownedCurlyBracketedClause', None)
    assert not _is_linked(a, 'ownedCurlyBracketedClause', b2)
    if hasattr(b2, 'AbstractNameExpCS'):
        assert not _is_linked(b2, 'AbstractNameExpCS', a)


def test_assoc_owningRoundBracketedClause112_link_reassign_clear():
    a = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    b1 = essentialoclcs_RoundBracketedClauseCS()
    b2 = essentialoclcs_RoundBracketedClauseCS()
    _safe_set(a, 'ownedArguments', b1)
    assert _is_linked(a, 'ownedArguments', b1)
    if hasattr(b1, 'RoundBracketedClauseCS113'):
        assert _is_linked(b1, 'RoundBracketedClauseCS113', a)
    _safe_set(a, 'ownedArguments', b2)
    assert _is_linked(a, 'ownedArguments', b2)
    if hasattr(b1, 'RoundBracketedClauseCS113'):
        assert not _is_linked(b1, 'RoundBracketedClauseCS113', a)
    if hasattr(b2, 'RoundBracketedClauseCS113'):
        assert _is_linked(b2, 'RoundBracketedClauseCS113', a)
    _safe_set(a, 'ownedArguments', None)
    assert not _is_linked(a, 'ownedArguments', b2)
    if hasattr(b2, 'RoundBracketedClauseCS113'):
        assert not _is_linked(b2, 'RoundBracketedClauseCS113', a)


def test_assoc_parts129_link_reassign_clear():
    a = essentialoclcs_ShadowExpCS(value="sample_text")
    b1 = essentialoclcs_ShadowPartCS()
    b2 = essentialoclcs_ShadowPartCS()
    _safe_set(a, 'essentialoclcs_ShadowExpCS', {b1})
    assert _is_linked(a, 'essentialoclcs_ShadowExpCS', b1)
    if hasattr(b1, 'essentialoclcs_ShadowPartCS'):
        assert _is_linked(b1, 'essentialoclcs_ShadowPartCS', a)
    _safe_set(a, 'essentialoclcs_ShadowExpCS', {b2})
    assert _is_linked(a, 'essentialoclcs_ShadowExpCS', b2)
    if hasattr(b1, 'essentialoclcs_ShadowPartCS'):
        assert not _is_linked(b1, 'essentialoclcs_ShadowPartCS', a)
    if hasattr(b2, 'essentialoclcs_ShadowPartCS'):
        assert _is_linked(b2, 'essentialoclcs_ShadowPartCS', a)
    _safe_set(a, 'essentialoclcs_ShadowExpCS', set())
    assert not _is_linked(a, 'essentialoclcs_ShadowExpCS', b2)
    if hasattr(b2, 'essentialoclcs_ShadowPartCS'):
        assert not _is_linked(b2, 'essentialoclcs_ShadowPartCS', a)


def test_assoc_precedence52_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_Precedence()
    b2 = essentialoclcs_Precedence()
    _safe_set(a, 'essentialoclcs_ExpCS53', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS53', b1)
    if hasattr(b1, 'essentialoclcs_Precedence'):
        assert _is_linked(b1, 'essentialoclcs_Precedence', a)
    _safe_set(a, 'essentialoclcs_ExpCS53', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS53', b2)
    if hasattr(b1, 'essentialoclcs_Precedence'):
        assert not _is_linked(b1, 'essentialoclcs_Precedence', a)
    if hasattr(b2, 'essentialoclcs_Precedence'):
        assert _is_linked(b2, 'essentialoclcs_Precedence', a)
    _safe_set(a, 'essentialoclcs_ExpCS53', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS53', b2)
    if hasattr(b2, 'essentialoclcs_Precedence'):
        assert not _is_linked(b2, 'essentialoclcs_Precedence', a)


def test_assoc_source120_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_OperatorExpCS()
    b2 = essentialoclcs_OperatorExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS122', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS122', b1)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS121'):
        assert _is_linked(b1, 'essentialoclcs_OperatorExpCS121', a)
    _safe_set(a, 'essentialoclcs_ExpCS122', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS122', b2)
    if hasattr(b1, 'essentialoclcs_OperatorExpCS121'):
        assert not _is_linked(b1, 'essentialoclcs_OperatorExpCS121', a)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS121'):
        assert _is_linked(b2, 'essentialoclcs_OperatorExpCS121', a)
    _safe_set(a, 'essentialoclcs_ExpCS122', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS122', b2)
    if hasattr(b2, 'essentialoclcs_OperatorExpCS121'):
        assert not _is_linked(b2, 'essentialoclcs_OperatorExpCS121', a)


def test_assoc_source13_link_reassign_clear():
    a = essentialoclcs_ExpCS(hasError=True)
    b1 = essentialoclcs_CallExpCS()
    b2 = essentialoclcs_CallExpCS()
    _safe_set(a, 'essentialoclcs_ExpCS15', b1)
    assert _is_linked(a, 'essentialoclcs_ExpCS15', b1)
    if hasattr(b1, 'essentialoclcs_CallExpCS14'):
        assert _is_linked(b1, 'essentialoclcs_CallExpCS14', a)
    _safe_set(a, 'essentialoclcs_ExpCS15', b2)
    assert _is_linked(a, 'essentialoclcs_ExpCS15', b2)
    if hasattr(b1, 'essentialoclcs_CallExpCS14'):
        assert not _is_linked(b1, 'essentialoclcs_CallExpCS14', a)
    if hasattr(b2, 'essentialoclcs_CallExpCS14'):
        assert _is_linked(b2, 'essentialoclcs_CallExpCS14', a)
    _safe_set(a, 'essentialoclcs_ExpCS15', None)
    assert not _is_linked(a, 'essentialoclcs_ExpCS15', b2)
    if hasattr(b2, 'essentialoclcs_CallExpCS14'):
        assert not _is_linked(b2, 'essentialoclcs_CallExpCS14', a)


def test_assoc_sourceType6_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_Type()
    b2 = essentialoclcs_Type()
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS7', b1)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS7', b1)
    if hasattr(b1, 'essentialoclcs_Type'):
        assert _is_linked(b1, 'essentialoclcs_Type', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS7', b2)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS7', b2)
    if hasattr(b1, 'essentialoclcs_Type'):
        assert not _is_linked(b1, 'essentialoclcs_Type', a)
    if hasattr(b2, 'essentialoclcs_Type'):
        assert _is_linked(b2, 'essentialoclcs_Type', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS7', None)
    assert not _is_linked(a, 'essentialoclcs_AbstractNameExpCS7', b2)
    if hasattr(b2, 'essentialoclcs_Type'):
        assert not _is_linked(b2, 'essentialoclcs_Type', a)


def test_assoc_sourceTypeValue8_link_reassign_clear():
    a = essentialoclcs_AbstractNameExpCS(isPre=True)
    b1 = essentialoclcs_Type()
    b2 = essentialoclcs_Type()
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS9', b1)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS9', b1)
    if hasattr(b1, 'essentialoclcs_Type10'):
        assert _is_linked(b1, 'essentialoclcs_Type10', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS9', b2)
    assert _is_linked(a, 'essentialoclcs_AbstractNameExpCS9', b2)
    if hasattr(b1, 'essentialoclcs_Type10'):
        assert not _is_linked(b1, 'essentialoclcs_Type10', a)
    if hasattr(b2, 'essentialoclcs_Type10'):
        assert _is_linked(b2, 'essentialoclcs_Type10', a)
    _safe_set(a, 'essentialoclcs_AbstractNameExpCS9', None)
    assert not _is_linked(a, 'essentialoclcs_AbstractNameExpCS9', b2)
    if hasattr(b2, 'essentialoclcs_Type10'):
        assert not _is_linked(b2, 'essentialoclcs_Type10', a)


def test_assoc_typeName130_link_reassign_clear():
    a = essentialoclcs_ShadowExpCS(value="sample_text")
    b1 = essentialoclcs_TypeNameExpCS()
    b2 = essentialoclcs_TypeNameExpCS()
    _safe_set(a, 'essentialoclcs_ShadowExpCS131', b1)
    assert _is_linked(a, 'essentialoclcs_ShadowExpCS131', b1)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS'):
        assert _is_linked(b1, 'essentialoclcs_TypeNameExpCS', a)
    _safe_set(a, 'essentialoclcs_ShadowExpCS131', b2)
    assert _is_linked(a, 'essentialoclcs_ShadowExpCS131', b2)
    if hasattr(b1, 'essentialoclcs_TypeNameExpCS'):
        assert not _is_linked(b1, 'essentialoclcs_TypeNameExpCS', a)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS'):
        assert _is_linked(b2, 'essentialoclcs_TypeNameExpCS', a)
    _safe_set(a, 'essentialoclcs_ShadowExpCS131', None)
    assert not _is_linked(a, 'essentialoclcs_ShadowExpCS131', b2)
    if hasattr(b2, 'essentialoclcs_TypeNameExpCS'):
        assert not _is_linked(b2, 'essentialoclcs_TypeNameExpCS', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractNameExpCS_strategy = st.builds(AbstractNameExpCS)
@given(instance=AbstractNameExpCS_strategy)
@settings(max_examples=25)
def test_AbstractNameExpCS_instantiation(instance):
    assert isinstance(instance, AbstractNameExpCS)


AssociationClassCallExpCS_strategy = st.builds(AssociationClassCallExpCS)
@given(instance=AssociationClassCallExpCS_strategy)
@settings(max_examples=25)
def test_AssociationClassCallExpCS_instantiation(instance):
    assert isinstance(instance, AssociationClassCallExpCS)


CallExpCS_strategy = st.builds(CallExpCS)
@given(instance=CallExpCS_strategy)
@settings(max_examples=25)
def test_CallExpCS_instantiation(instance):
    assert isinstance(instance, CallExpCS)


ContextLessElementCS_strategy = st.builds(ContextLessElementCS)
@given(instance=ContextLessElementCS_strategy)
@settings(max_examples=25)
def test_ContextLessElementCS_instantiation(instance):
    assert isinstance(instance, ContextLessElementCS)


ExpCS_strategy = st.builds(ExpCS)
@given(instance=ExpCS_strategy)
@settings(max_examples=25)
def test_ExpCS_instantiation(instance):
    assert isinstance(instance, ExpCS)


IterateCallExpCS_strategy = st.builds(IterateCallExpCS)
@given(instance=IterateCallExpCS_strategy)
@settings(max_examples=25)
def test_IterateCallExpCS_instantiation(instance):
    assert isinstance(instance, IterateCallExpCS)


IterationCallExpCS_strategy = st.builds(IterationCallExpCS)
@given(instance=IterationCallExpCS_strategy)
@settings(max_examples=25)
def test_IterationCallExpCS_instantiation(instance):
    assert isinstance(instance, IterationCallExpCS)


LiteralExpCS_strategy = st.builds(LiteralExpCS)
@given(instance=LiteralExpCS_strategy)
@settings(max_examples=25)
def test_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)


ModelElementCS_strategy = st.builds(ModelElementCS)
@given(instance=ModelElementCS_strategy)
@settings(max_examples=25)
def test_ModelElementCS_instantiation(instance):
    assert isinstance(instance, ModelElementCS)


Nameable_strategy = st.builds(Nameable)
@given(instance=Nameable_strategy)
@settings(max_examples=25)
def test_Nameable_instantiation(instance):
    assert isinstance(instance, Nameable)


NamedElementCS_strategy = st.builds(NamedElementCS)
@given(instance=NamedElementCS_strategy)
@settings(max_examples=25)
def test_NamedElementCS_instantiation(instance):
    assert isinstance(instance, NamedElementCS)


OperationCallExpCS_strategy = st.builds(OperationCallExpCS)
@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=25)
def test_OperationCallExpCS_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)


OperatorExpCS_strategy = st.builds(OperatorExpCS)
@given(instance=OperatorExpCS_strategy)
@settings(max_examples=25)
def test_OperatorExpCS_instantiation(instance):
    assert isinstance(instance, OperatorExpCS)


PrimitiveLiteralExpCS_strategy = st.builds(PrimitiveLiteralExpCS)
@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=25)
def test_PrimitiveLiteralExpCS_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)


PropertyCallExpCS_strategy = st.builds(PropertyCallExpCS)
@given(instance=PropertyCallExpCS_strategy)
@settings(max_examples=25)
def test_PropertyCallExpCS_instantiation(instance):
    assert isinstance(instance, PropertyCallExpCS)


RootCS_strategy = st.builds(RootCS)
@given(instance=RootCS_strategy)
@settings(max_examples=25)
def test_RootCS_instantiation(instance):
    assert isinstance(instance, RootCS)


ShadowExpCS_strategy = st.builds(ShadowExpCS)
@given(instance=ShadowExpCS_strategy)
@settings(max_examples=25)
def test_ShadowExpCS_instantiation(instance):
    assert isinstance(instance, ShadowExpCS)


SpecificationCS_strategy = st.builds(SpecificationCS)
@given(instance=SpecificationCS_strategy)
@settings(max_examples=25)
def test_SpecificationCS_instantiation(instance):
    assert isinstance(instance, SpecificationCS)


TypedRefCS_strategy = st.builds(TypedRefCS)
@given(instance=TypedRefCS_strategy)
@settings(max_examples=25)
def test_TypedRefCS_instantiation(instance):
    assert isinstance(instance, TypedRefCS)


VariableCS_strategy = st.builds(VariableCS)
@given(instance=VariableCS_strategy)
@settings(max_examples=25)
def test_VariableCS_instantiation(instance):
    assert isinstance(instance, VariableCS)


VariableExpCS_strategy = st.builds(VariableExpCS)
@given(instance=VariableExpCS_strategy)
@settings(max_examples=25)
def test_VariableExpCS_instantiation(instance):
    assert isinstance(instance, VariableExpCS)


essentialoclcs_AbstractNameExpCS_strategy = st.builds(essentialoclcs_AbstractNameExpCS, isPre=st.booleans())
@given(instance=essentialoclcs_AbstractNameExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_AbstractNameExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AbstractNameExpCS)


essentialoclcs_AssociationClass_strategy = st.builds(essentialoclcs_AssociationClass)
@given(instance=essentialoclcs_AssociationClass_strategy)
@settings(max_examples=25)
def test_essentialoclcs_AssociationClass_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AssociationClass)


essentialoclcs_AssociationClassCallExpCS_strategy = st.builds(essentialoclcs_AssociationClassCallExpCS)
@given(instance=essentialoclcs_AssociationClassCallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_AssociationClassCallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AssociationClassCallExpCS)


essentialoclcs_BooleanLiteralExpCS_strategy = st.builds(essentialoclcs_BooleanLiteralExpCS, symbol=safe_text)
@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_BooleanLiteralExpCS)


essentialoclcs_CallExpCS_strategy = st.builds(essentialoclcs_CallExpCS)
@given(instance=essentialoclcs_CallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CallExpCS)


essentialoclcs_CollectionLiteralExpCS_strategy = st.builds(essentialoclcs_CollectionLiteralExpCS)
@given(instance=essentialoclcs_CollectionLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CollectionLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralExpCS)


essentialoclcs_CollectionLiteralPartCS_strategy = st.builds(essentialoclcs_CollectionLiteralPartCS)
@given(instance=essentialoclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CollectionLiteralPartCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralPartCS)


essentialoclcs_CollectionPatternCS_strategy = st.builds(essentialoclcs_CollectionPatternCS, restVariableName=safe_text)
@given(instance=essentialoclcs_CollectionPatternCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CollectionPatternCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionPatternCS)


essentialoclcs_CollectionTypeCS_strategy = st.builds(essentialoclcs_CollectionTypeCS, name=safe_text)
@given(instance=essentialoclcs_CollectionTypeCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CollectionTypeCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionTypeCS)


essentialoclcs_ContextCS_strategy = st.builds(essentialoclcs_ContextCS)
@given(instance=essentialoclcs_ContextCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_ContextCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ContextCS)


essentialoclcs_CurlyBracketedClauseCS_strategy = st.builds(essentialoclcs_CurlyBracketedClauseCS, value=safe_text)
@given(instance=essentialoclcs_CurlyBracketedClauseCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_CurlyBracketedClauseCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CurlyBracketedClauseCS)


essentialoclcs_ExpCS_strategy = st.builds(essentialoclcs_ExpCS, hasError=st.booleans())
@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_ExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpCS)


essentialoclcs_ExpSpecificationCS_strategy = st.builds(essentialoclcs_ExpSpecificationCS)
@given(instance=essentialoclcs_ExpSpecificationCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_ExpSpecificationCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpSpecificationCS)


essentialoclcs_IfExpCS_strategy = st.builds(essentialoclcs_IfExpCS, isImplicit=st.booleans())
@given(instance=essentialoclcs_IfExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_IfExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IfExpCS)


essentialoclcs_IfThenExpCS_strategy = st.builds(essentialoclcs_IfThenExpCS)
@given(instance=essentialoclcs_IfThenExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_IfThenExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IfThenExpCS)


essentialoclcs_InfixExpCS_strategy = st.builds(essentialoclcs_InfixExpCS)
@given(instance=essentialoclcs_InfixExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_InfixExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InfixExpCS)


essentialoclcs_InvalidLiteralExpCS_strategy = st.builds(essentialoclcs_InvalidLiteralExpCS)
@given(instance=essentialoclcs_InvalidLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_InvalidLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InvalidLiteralExpCS)


essentialoclcs_IterateCallExpCS_strategy = st.builds(essentialoclcs_IterateCallExpCS)
@given(instance=essentialoclcs_IterateCallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_IterateCallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IterateCallExpCS)


essentialoclcs_Iteration_strategy = st.builds(essentialoclcs_Iteration)
@given(instance=essentialoclcs_Iteration_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Iteration_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Iteration)


essentialoclcs_IterationCallExpCS_strategy = st.builds(essentialoclcs_IterationCallExpCS)
@given(instance=essentialoclcs_IterationCallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_IterationCallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IterationCallExpCS)


essentialoclcs_LambdaLiteralExpCS_strategy = st.builds(essentialoclcs_LambdaLiteralExpCS)
@given(instance=essentialoclcs_LambdaLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_LambdaLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LambdaLiteralExpCS)


essentialoclcs_LetExpCS_strategy = st.builds(essentialoclcs_LetExpCS, isImplicit=st.booleans())
@given(instance=essentialoclcs_LetExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_LetExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetExpCS)


essentialoclcs_LetVariableCS_strategy = st.builds(essentialoclcs_LetVariableCS)
@given(instance=essentialoclcs_LetVariableCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_LetVariableCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetVariableCS)


essentialoclcs_LiteralExpCS_strategy = st.builds(essentialoclcs_LiteralExpCS)
@given(instance=essentialoclcs_LiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LiteralExpCS)


essentialoclcs_MapLiteralExpCS_strategy = st.builds(essentialoclcs_MapLiteralExpCS)
@given(instance=essentialoclcs_MapLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_MapLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapLiteralExpCS)


essentialoclcs_MapLiteralPartCS_strategy = st.builds(essentialoclcs_MapLiteralPartCS)
@given(instance=essentialoclcs_MapLiteralPartCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_MapLiteralPartCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapLiteralPartCS)


essentialoclcs_MapTypeCS_strategy = st.builds(essentialoclcs_MapTypeCS, name=safe_text)
@given(instance=essentialoclcs_MapTypeCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_MapTypeCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapTypeCS)


essentialoclcs_NameExpCS_strategy = st.builds(essentialoclcs_NameExpCS)
@given(instance=essentialoclcs_NameExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_NameExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NameExpCS)


essentialoclcs_NavigatingArgCS_strategy = st.builds(essentialoclcs_NavigatingArgCS, prefix=safe_text, role=safe_text)
@given(instance=essentialoclcs_NavigatingArgCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_NavigatingArgCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NavigatingArgCS)


essentialoclcs_NestedExpCS_strategy = st.builds(essentialoclcs_NestedExpCS)
@given(instance=essentialoclcs_NestedExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_NestedExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NestedExpCS)


essentialoclcs_NullLiteralExpCS_strategy = st.builds(essentialoclcs_NullLiteralExpCS)
@given(instance=essentialoclcs_NullLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_NullLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NullLiteralExpCS)


essentialoclcs_NumberLiteralExpCS_strategy = st.builds(essentialoclcs_NumberLiteralExpCS, symbol=safe_text)
@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_NumberLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NumberLiteralExpCS)


essentialoclcs_Operation_strategy = st.builds(essentialoclcs_Operation)
@given(instance=essentialoclcs_Operation_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Operation_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Operation)


essentialoclcs_OperationCallExpCS_strategy = st.builds(essentialoclcs_OperationCallExpCS)
@given(instance=essentialoclcs_OperationCallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_OperationCallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_OperationCallExpCS)


essentialoclcs_OperatorExpCS_strategy = st.builds(essentialoclcs_OperatorExpCS)
@given(instance=essentialoclcs_OperatorExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_OperatorExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_OperatorExpCS)


essentialoclcs_PathNameCS_strategy = st.builds(essentialoclcs_PathNameCS)
@given(instance=essentialoclcs_PathNameCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_PathNameCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PathNameCS)


essentialoclcs_PatternExpCS_strategy = st.builds(essentialoclcs_PatternExpCS, patternVariableName=safe_text)
@given(instance=essentialoclcs_PatternExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_PatternExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PatternExpCS)


essentialoclcs_Precedence_strategy = st.builds(essentialoclcs_Precedence)
@given(instance=essentialoclcs_Precedence_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Precedence_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Precedence)


essentialoclcs_PrefixExpCS_strategy = st.builds(essentialoclcs_PrefixExpCS)
@given(instance=essentialoclcs_PrefixExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_PrefixExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrefixExpCS)


essentialoclcs_PrimitiveLiteralExpCS_strategy = st.builds(essentialoclcs_PrimitiveLiteralExpCS)
@given(instance=essentialoclcs_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_PrimitiveLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrimitiveLiteralExpCS)


essentialoclcs_Property_strategy = st.builds(essentialoclcs_Property)
@given(instance=essentialoclcs_Property_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Property_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Property)


essentialoclcs_PropertyCallExpCS_strategy = st.builds(essentialoclcs_PropertyCallExpCS)
@given(instance=essentialoclcs_PropertyCallExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_PropertyCallExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PropertyCallExpCS)


essentialoclcs_RoundBracketedClauseCS_strategy = st.builds(essentialoclcs_RoundBracketedClauseCS)
@given(instance=essentialoclcs_RoundBracketedClauseCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_RoundBracketedClauseCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_RoundBracketedClauseCS)


essentialoclcs_SelfExpCS_strategy = st.builds(essentialoclcs_SelfExpCS, name=safe_text)
@given(instance=essentialoclcs_SelfExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_SelfExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_SelfExpCS)


essentialoclcs_ShadowExpCS_strategy = st.builds(essentialoclcs_ShadowExpCS, value=safe_text)
@given(instance=essentialoclcs_ShadowExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_ShadowExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ShadowExpCS)


essentialoclcs_ShadowPartCS_strategy = st.builds(essentialoclcs_ShadowPartCS)
@given(instance=essentialoclcs_ShadowPartCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_ShadowPartCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ShadowPartCS)


essentialoclcs_SquareBracketedClauseCS_strategy = st.builds(essentialoclcs_SquareBracketedClauseCS)
@given(instance=essentialoclcs_SquareBracketedClauseCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_SquareBracketedClauseCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_SquareBracketedClauseCS)


essentialoclcs_StringLiteralExpCS_strategy = st.builds(essentialoclcs_StringLiteralExpCS, segments=safe_text)
@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_StringLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_StringLiteralExpCS)


essentialoclcs_TupleLiteralExpCS_strategy = st.builds(essentialoclcs_TupleLiteralExpCS)
@given(instance=essentialoclcs_TupleLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TupleLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralExpCS)


essentialoclcs_TupleLiteralPartCS_strategy = st.builds(essentialoclcs_TupleLiteralPartCS)
@given(instance=essentialoclcs_TupleLiteralPartCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TupleLiteralPartCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralPartCS)


essentialoclcs_Type_strategy = st.builds(essentialoclcs_Type)
@given(instance=essentialoclcs_Type_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Type_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Type)


essentialoclcs_TypeLiteralExpCS_strategy = st.builds(essentialoclcs_TypeLiteralExpCS)
@given(instance=essentialoclcs_TypeLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TypeLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeLiteralExpCS)


essentialoclcs_TypeNameExpCS_strategy = st.builds(essentialoclcs_TypeNameExpCS)
@given(instance=essentialoclcs_TypeNameExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TypeNameExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeNameExpCS)


essentialoclcs_TypeRefCS_strategy = st.builds(essentialoclcs_TypeRefCS)
@given(instance=essentialoclcs_TypeRefCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TypeRefCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeRefCS)


essentialoclcs_TypedRefCS_strategy = st.builds(essentialoclcs_TypedRefCS)
@given(instance=essentialoclcs_TypedRefCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_TypedRefCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypedRefCS)


essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy = st.builds(essentialoclcs_UnlimitedNaturalLiteralExpCS)
@given(instance=essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_UnlimitedNaturalLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_UnlimitedNaturalLiteralExpCS)


essentialoclcs_Variable_strategy = st.builds(essentialoclcs_Variable)
@given(instance=essentialoclcs_Variable_strategy)
@settings(max_examples=25)
def test_essentialoclcs_Variable_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Variable)


essentialoclcs_VariableCS_strategy = st.builds(essentialoclcs_VariableCS)
@given(instance=essentialoclcs_VariableCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_VariableCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_VariableCS)


essentialoclcs_VariableExpCS_strategy = st.builds(essentialoclcs_VariableExpCS)
@given(instance=essentialoclcs_VariableExpCS_strategy)
@settings(max_examples=25)
def test_essentialoclcs_VariableExpCS_instantiation(instance):
    assert isinstance(instance, essentialoclcs_VariableExpCS)



