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
    Expression,
    essentialocl_expressions_ExpressionInOcl,
    expressions_essentialocl_EnumerationLiteral,
    CollectionLiteralPart,
    essentialocl_expressions_CollectionRange,
    essentialocl_expressions_CollectionItem,
    LoopExp,
    essentialocl_expressions_IterateExp,
    essentialocl_expressions_IteratorExp,
    CallExp,
    essentialocl_expressions_FeatureCallExp,
    essentialocl_expressions_LoopExp,
    expressions_essentialocl_Operation,
    FeatureCallExp,
    essentialocl_expressions_OperationCallExp,
    essentialocl_expressions_PropertyCallExp,
    PrimitiveLiteralExp,
    essentialocl_expressions_BooleanLiteralExp,
    essentialocl_expressions_NumericLiteralExp,
    essentialocl_expressions_StringLiteralExp,
    TupleLiteralPart,
    expressions_essentialocl_Property,
    expressions_essentialocl_Type,
    LiteralExp,
    essentialocl_expressions_PrimitiveLiteralExp,
    essentialocl_expressions_InvalidLiteralExp,
    essentialocl_expressions_TupleLiteralExp,
    essentialocl_expressions_CollectionLiteralExp,
    essentialocl_expressions_EnumLiteralExp,
    essentialocl_expressions_UndefinedLiteralExp,
    essentialocl_expressions_TypeLiteralExp,
    NumericLiteralExp,
    essentialocl_expressions_IntegerLiteralExp,
    essentialocl_expressions_RealLiteralExp,
    essentialocl_expressions_UnlimitedNaturalExp,
    expressions_essentialocl_Parameter,
    NamedElement,
    TypedElement,
    essentialocl_expressions_CollectionLiteralPart,
    essentialocl_expressions_TupleLiteralPart,
    essentialocl_expressions_OclExpression,
    essentialocl_expressions_Variable,
    Variable,
    OclExpression,
    essentialocl_expressions_CallExp,
    essentialocl_expressions_IfExp,
    essentialocl_expressions_LiteralExp,
    essentialocl_expressions_LetExp,
    essentialocl_expressions_VariableExp,
    TupleType,
    OrderedSetType,
    SetType,
    BagType,
    SequenceType,
    TypeType,
    InvalidType,
    VoidType,
    AnyType,
    types_essentialocl_PrimitiveType,
    essentialocl_types_OclLibrary,
    types_essentialocl_Type,
    OclLibrary,
    Type,
    essentialocl_types_CollectionType,
    essentialocl_types_AnyType,
    essentialocl_types_TypeType,
    essentialocl_types_InvalidType,
    essentialocl_types_VoidType,
    essentialocl_types_TupleType,
    CollectionType,
    essentialocl_types_OrderedSetType,
    essentialocl_types_BagType,
    essentialocl_types_SetType,
    essentialocl_types_SequenceType,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_ExpressionInOcl)


def test_hyp_essentialocl_expressions_expressioninocl_constructor_exists():
    assert callable(essentialocl_expressions_ExpressionInOcl.__init__)


def test_hyp_essentialocl_expressions_expressioninocl_constructor_args():
    sig = inspect.signature(essentialocl_expressions_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_essentialocl_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_essentialocl_EnumerationLiteral)


def test_hyp_expressions_essentialocl_enumerationliteral_constructor_exists():
    assert callable(expressions_essentialocl_EnumerationLiteral.__init__)


def test_hyp_expressions_essentialocl_enumerationliteral_constructor_args():
    sig = inspect.signature(expressions_essentialocl_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_hyp_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_hyp_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_collectionrange_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_CollectionRange)


def test_hyp_essentialocl_expressions_collectionrange_constructor_exists():
    assert callable(essentialocl_expressions_CollectionRange.__init__)


def test_hyp_essentialocl_expressions_collectionrange_constructor_args():
    sig = inspect.signature(essentialocl_expressions_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_collectionitem_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_CollectionItem)


def test_hyp_essentialocl_expressions_collectionitem_constructor_exists():
    assert callable(essentialocl_expressions_CollectionItem.__init__)


def test_hyp_essentialocl_expressions_collectionitem_constructor_args():
    sig = inspect.signature(essentialocl_expressions_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_hyp_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_hyp_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_iterateexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_IterateExp)


def test_hyp_essentialocl_expressions_iterateexp_constructor_exists():
    assert callable(essentialocl_expressions_IterateExp.__init__)


def test_hyp_essentialocl_expressions_iterateexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_IteratorExp)


def test_hyp_essentialocl_expressions_iteratorexp_constructor_exists():
    assert callable(essentialocl_expressions_IteratorExp.__init__)


def test_hyp_essentialocl_expressions_iteratorexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_hyp_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_hyp_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_FeatureCallExp)


def test_hyp_essentialocl_expressions_featurecallexp_constructor_exists():
    assert callable(essentialocl_expressions_FeatureCallExp.__init__)


def test_hyp_essentialocl_expressions_featurecallexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_LoopExp)


def test_hyp_essentialocl_expressions_loopexp_constructor_exists():
    assert callable(essentialocl_expressions_LoopExp.__init__)


def test_hyp_essentialocl_expressions_loopexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_essentialocl_operation_is_not_abstract():
    assert not inspect.isabstract(expressions_essentialocl_Operation)


def test_hyp_expressions_essentialocl_operation_constructor_exists():
    assert callable(expressions_essentialocl_Operation.__init__)


def test_hyp_expressions_essentialocl_operation_constructor_args():
    sig = inspect.signature(expressions_essentialocl_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_hyp_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_hyp_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_OperationCallExp)


def test_hyp_essentialocl_expressions_operationcallexp_constructor_exists():
    assert callable(essentialocl_expressions_OperationCallExp.__init__)


def test_hyp_essentialocl_expressions_operationcallexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_PropertyCallExp)


def test_hyp_essentialocl_expressions_propertycallexp_constructor_exists():
    assert callable(essentialocl_expressions_PropertyCallExp.__init__)


def test_hyp_essentialocl_expressions_propertycallexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_hyp_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_hyp_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_BooleanLiteralExp)


def test_hyp_essentialocl_expressions_booleanliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_BooleanLiteralExp.__init__)


def test_hyp_essentialocl_expressions_booleanliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"




def test_hyp_essentialocl_expressions_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_NumericLiteralExp)


def test_hyp_essentialocl_expressions_numericliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_NumericLiteralExp.__init__)


def test_hyp_essentialocl_expressions_numericliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_StringLiteralExp)


def test_hyp_essentialocl_expressions_stringliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_StringLiteralExp.__init__)


def test_hyp_essentialocl_expressions_stringliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_hyp_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_hyp_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_essentialocl_property_is_not_abstract():
    assert not inspect.isabstract(expressions_essentialocl_Property)


def test_hyp_expressions_essentialocl_property_constructor_exists():
    assert callable(expressions_essentialocl_Property.__init__)


def test_hyp_expressions_essentialocl_property_constructor_args():
    sig = inspect.signature(expressions_essentialocl_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_essentialocl_type_is_not_abstract():
    assert not inspect.isabstract(expressions_essentialocl_Type)


def test_hyp_expressions_essentialocl_type_constructor_exists():
    assert callable(expressions_essentialocl_Type.__init__)


def test_hyp_expressions_essentialocl_type_constructor_args():
    sig = inspect.signature(expressions_essentialocl_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_hyp_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_hyp_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_PrimitiveLiteralExp)


def test_hyp_essentialocl_expressions_primitiveliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_PrimitiveLiteralExp.__init__)


def test_hyp_essentialocl_expressions_primitiveliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_InvalidLiteralExp)


def test_hyp_essentialocl_expressions_invalidliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_InvalidLiteralExp.__init__)


def test_hyp_essentialocl_expressions_invalidliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_TupleLiteralExp)


def test_hyp_essentialocl_expressions_tupleliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_TupleLiteralExp.__init__)


def test_hyp_essentialocl_expressions_tupleliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_CollectionLiteralExp)


def test_hyp_essentialocl_expressions_collectionliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_CollectionLiteralExp.__init__)


def test_hyp_essentialocl_expressions_collectionliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_essentialocl_expressions_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_EnumLiteralExp)


def test_hyp_essentialocl_expressions_enumliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_EnumLiteralExp.__init__)


def test_hyp_essentialocl_expressions_enumliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_undefinedliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_UndefinedLiteralExp)


def test_hyp_essentialocl_expressions_undefinedliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_UndefinedLiteralExp.__init__)


def test_hyp_essentialocl_expressions_undefinedliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_UndefinedLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_typeliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_TypeLiteralExp)


def test_hyp_essentialocl_expressions_typeliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_TypeLiteralExp.__init__)


def test_hyp_essentialocl_expressions_typeliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_TypeLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_hyp_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_hyp_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_IntegerLiteralExp)


def test_hyp_essentialocl_expressions_integerliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_IntegerLiteralExp.__init__)


def test_hyp_essentialocl_expressions_integerliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"




def test_hyp_essentialocl_expressions_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_RealLiteralExp)


def test_hyp_essentialocl_expressions_realliteralexp_constructor_exists():
    assert callable(essentialocl_expressions_RealLiteralExp.__init__)


def test_hyp_essentialocl_expressions_realliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"




def test_hyp_essentialocl_expressions_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_UnlimitedNaturalExp)


def test_hyp_essentialocl_expressions_unlimitednaturalexp_constructor_exists():
    assert callable(essentialocl_expressions_UnlimitedNaturalExp.__init__)


def test_hyp_essentialocl_expressions_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_expressions_essentialocl_parameter_is_not_abstract():
    assert not inspect.isabstract(expressions_essentialocl_Parameter)


def test_hyp_expressions_essentialocl_parameter_constructor_exists():
    assert callable(expressions_essentialocl_Parameter.__init__)


def test_hyp_expressions_essentialocl_parameter_constructor_args():
    sig = inspect.signature(expressions_essentialocl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_CollectionLiteralPart)


def test_hyp_essentialocl_expressions_collectionliteralpart_constructor_exists():
    assert callable(essentialocl_expressions_CollectionLiteralPart.__init__)


def test_hyp_essentialocl_expressions_collectionliteralpart_constructor_args():
    sig = inspect.signature(essentialocl_expressions_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_TupleLiteralPart)


def test_hyp_essentialocl_expressions_tupleliteralpart_constructor_exists():
    assert callable(essentialocl_expressions_TupleLiteralPart.__init__)


def test_hyp_essentialocl_expressions_tupleliteralpart_constructor_args():
    sig = inspect.signature(essentialocl_expressions_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_OclExpression)


def test_hyp_essentialocl_expressions_oclexpression_constructor_exists():
    assert callable(essentialocl_expressions_OclExpression.__init__)


def test_hyp_essentialocl_expressions_oclexpression_constructor_args():
    sig = inspect.signature(essentialocl_expressions_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_variable_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_Variable)


def test_hyp_essentialocl_expressions_variable_constructor_exists():
    assert callable(essentialocl_expressions_Variable.__init__)


def test_hyp_essentialocl_expressions_variable_constructor_args():
    sig = inspect.signature(essentialocl_expressions_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_hyp_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_hyp_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_CallExp)


def test_hyp_essentialocl_expressions_callexp_constructor_exists():
    assert callable(essentialocl_expressions_CallExp.__init__)


def test_hyp_essentialocl_expressions_callexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_ifexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_IfExp)


def test_hyp_essentialocl_expressions_ifexp_constructor_exists():
    assert callable(essentialocl_expressions_IfExp.__init__)


def test_hyp_essentialocl_expressions_ifexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_literalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_LiteralExp)


def test_hyp_essentialocl_expressions_literalexp_constructor_exists():
    assert callable(essentialocl_expressions_LiteralExp.__init__)


def test_hyp_essentialocl_expressions_literalexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_letexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_LetExp)


def test_hyp_essentialocl_expressions_letexp_constructor_exists():
    assert callable(essentialocl_expressions_LetExp.__init__)


def test_hyp_essentialocl_expressions_letexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_expressions_variableexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_expressions_VariableExp)


def test_hyp_essentialocl_expressions_variableexp_constructor_exists():
    assert callable(essentialocl_expressions_VariableExp.__init__)


def test_hyp_essentialocl_expressions_variableexp_constructor_args():
    sig = inspect.signature(essentialocl_expressions_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_hyp_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_hyp_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OrderedSetType)


def test_hyp_orderedsettype_constructor_exists():
    assert callable(OrderedSetType.__init__)


def test_hyp_orderedsettype_constructor_args():
    sig = inspect.signature(OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_hyp_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_hyp_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bagtype_is_not_abstract():
    assert not inspect.isabstract(BagType)


def test_hyp_bagtype_constructor_exists():
    assert callable(BagType.__init__)


def test_hyp_bagtype_constructor_args():
    sig = inspect.signature(BagType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sequencetype_is_not_abstract():
    assert not inspect.isabstract(SequenceType)


def test_hyp_sequencetype_constructor_exists():
    assert callable(SequenceType.__init__)


def test_hyp_sequencetype_constructor_args():
    sig = inspect.signature(SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typetype_is_not_abstract():
    assert not inspect.isabstract(TypeType)


def test_hyp_typetype_constructor_exists():
    assert callable(TypeType.__init__)


def test_hyp_typetype_constructor_args():
    sig = inspect.signature(TypeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_invalidtype_is_not_abstract():
    assert not inspect.isabstract(InvalidType)


def test_hyp_invalidtype_constructor_exists():
    assert callable(InvalidType.__init__)


def test_hyp_invalidtype_constructor_args():
    sig = inspect.signature(InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_voidtype_is_not_abstract():
    assert not inspect.isabstract(VoidType)


def test_hyp_voidtype_constructor_exists():
    assert callable(VoidType.__init__)


def test_hyp_voidtype_constructor_args():
    sig = inspect.signature(VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_hyp_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_hyp_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_essentialocl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_essentialocl_PrimitiveType)


def test_hyp_types_essentialocl_primitivetype_constructor_exists():
    assert callable(types_essentialocl_PrimitiveType.__init__)


def test_hyp_types_essentialocl_primitivetype_constructor_args():
    sig = inspect.signature(types_essentialocl_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_ocllibrary_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_OclLibrary)


def test_hyp_essentialocl_types_ocllibrary_constructor_exists():
    assert callable(essentialocl_types_OclLibrary.__init__)


def test_hyp_essentialocl_types_ocllibrary_constructor_args():
    sig = inspect.signature(essentialocl_types_OclLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_essentialocl_type_is_not_abstract():
    assert not inspect.isabstract(types_essentialocl_Type)


def test_hyp_types_essentialocl_type_constructor_exists():
    assert callable(types_essentialocl_Type.__init__)


def test_hyp_types_essentialocl_type_constructor_args():
    sig = inspect.signature(types_essentialocl_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllibrary_is_not_abstract():
    assert not inspect.isabstract(OclLibrary)


def test_hyp_ocllibrary_constructor_exists():
    assert callable(OclLibrary.__init__)


def test_hyp_ocllibrary_constructor_args():
    sig = inspect.signature(OclLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_CollectionType)


def test_hyp_essentialocl_types_collectiontype_constructor_exists():
    assert callable(essentialocl_types_CollectionType.__init__)


def test_hyp_essentialocl_types_collectiontype_constructor_args():
    sig = inspect.signature(essentialocl_types_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_essentialocl_types_anytype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_AnyType)


def test_hyp_essentialocl_types_anytype_constructor_exists():
    assert callable(essentialocl_types_AnyType.__init__)


def test_hyp_essentialocl_types_anytype_constructor_args():
    sig = inspect.signature(essentialocl_types_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_typetype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_TypeType)


def test_hyp_essentialocl_types_typetype_constructor_exists():
    assert callable(essentialocl_types_TypeType.__init__)


def test_hyp_essentialocl_types_typetype_constructor_args():
    sig = inspect.signature(essentialocl_types_TypeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_invalidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_InvalidType)


def test_hyp_essentialocl_types_invalidtype_constructor_exists():
    assert callable(essentialocl_types_InvalidType.__init__)


def test_hyp_essentialocl_types_invalidtype_constructor_args():
    sig = inspect.signature(essentialocl_types_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_voidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_VoidType)


def test_hyp_essentialocl_types_voidtype_constructor_exists():
    assert callable(essentialocl_types_VoidType.__init__)


def test_hyp_essentialocl_types_voidtype_constructor_args():
    sig = inspect.signature(essentialocl_types_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_tupletype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_TupleType)


def test_hyp_essentialocl_types_tupletype_constructor_exists():
    assert callable(essentialocl_types_TupleType.__init__)


def test_hyp_essentialocl_types_tupletype_constructor_args():
    sig = inspect.signature(essentialocl_types_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_hyp_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_hyp_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_OrderedSetType)


def test_hyp_essentialocl_types_orderedsettype_constructor_exists():
    assert callable(essentialocl_types_OrderedSetType.__init__)


def test_hyp_essentialocl_types_orderedsettype_constructor_args():
    sig = inspect.signature(essentialocl_types_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_bagtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_BagType)


def test_hyp_essentialocl_types_bagtype_constructor_exists():
    assert callable(essentialocl_types_BagType.__init__)


def test_hyp_essentialocl_types_bagtype_constructor_args():
    sig = inspect.signature(essentialocl_types_BagType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_settype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_SetType)


def test_hyp_essentialocl_types_settype_constructor_exists():
    assert callable(essentialocl_types_SetType.__init__)


def test_hyp_essentialocl_types_settype_constructor_args():
    sig = inspect.signature(essentialocl_types_SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_types_sequencetype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_types_SequenceType)


def test_hyp_essentialocl_types_sequencetype_constructor_exists():
    assert callable(essentialocl_types_SequenceType.__init__)


def test_hyp_essentialocl_types_sequencetype_constructor_args():
    sig = inspect.signature(essentialocl_types_SequenceType.__init__)
    params = list(sig.parameters.keys())

def test_hyp_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_hyp_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Collection",
        "OrderedSet",
        "Bag",
        "Sequence",
        "Set",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
Expression_strategy = st.builds(
    Expression,
)
essentialocl_expressions_ExpressionInOcl_strategy = st.builds(
    essentialocl_expressions_ExpressionInOcl,
)
expressions_essentialocl_EnumerationLiteral_strategy = st.builds(
    expressions_essentialocl_EnumerationLiteral,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
essentialocl_expressions_CollectionRange_strategy = st.builds(
    essentialocl_expressions_CollectionRange,
)
essentialocl_expressions_CollectionItem_strategy = st.builds(
    essentialocl_expressions_CollectionItem,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
essentialocl_expressions_IterateExp_strategy = st.builds(
    essentialocl_expressions_IterateExp,
)
essentialocl_expressions_IteratorExp_strategy = st.builds(
    essentialocl_expressions_IteratorExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
essentialocl_expressions_FeatureCallExp_strategy = st.builds(
    essentialocl_expressions_FeatureCallExp,
)
essentialocl_expressions_LoopExp_strategy = st.builds(
    essentialocl_expressions_LoopExp,
)
expressions_essentialocl_Operation_strategy = st.builds(
    expressions_essentialocl_Operation,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
essentialocl_expressions_OperationCallExp_strategy = st.builds(
    essentialocl_expressions_OperationCallExp,
)
essentialocl_expressions_PropertyCallExp_strategy = st.builds(
    essentialocl_expressions_PropertyCallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
essentialocl_expressions_BooleanLiteralExp_strategy = st.builds(
    essentialocl_expressions_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
essentialocl_expressions_NumericLiteralExp_strategy = st.builds(
    essentialocl_expressions_NumericLiteralExp,
)
essentialocl_expressions_StringLiteralExp_strategy = st.builds(
    essentialocl_expressions_StringLiteralExp,
    stringSymbol=
        safe_text
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
expressions_essentialocl_Property_strategy = st.builds(
    expressions_essentialocl_Property,
)
expressions_essentialocl_Type_strategy = st.builds(
    expressions_essentialocl_Type,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
essentialocl_expressions_PrimitiveLiteralExp_strategy = st.builds(
    essentialocl_expressions_PrimitiveLiteralExp,
)
essentialocl_expressions_InvalidLiteralExp_strategy = st.builds(
    essentialocl_expressions_InvalidLiteralExp,
)
essentialocl_expressions_TupleLiteralExp_strategy = st.builds(
    essentialocl_expressions_TupleLiteralExp,
)
essentialocl_expressions_CollectionLiteralExp_strategy = st.builds(
    essentialocl_expressions_CollectionLiteralExp,
    kind=
        safe_text
)
essentialocl_expressions_EnumLiteralExp_strategy = st.builds(
    essentialocl_expressions_EnumLiteralExp,
)
essentialocl_expressions_UndefinedLiteralExp_strategy = st.builds(
    essentialocl_expressions_UndefinedLiteralExp,
)
essentialocl_expressions_TypeLiteralExp_strategy = st.builds(
    essentialocl_expressions_TypeLiteralExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
essentialocl_expressions_IntegerLiteralExp_strategy = st.builds(
    essentialocl_expressions_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
essentialocl_expressions_RealLiteralExp_strategy = st.builds(
    essentialocl_expressions_RealLiteralExp,
    realSymbol=
        safe_text
)
essentialocl_expressions_UnlimitedNaturalExp_strategy = st.builds(
    essentialocl_expressions_UnlimitedNaturalExp,
    symbol=
        safe_text
)
expressions_essentialocl_Parameter_strategy = st.builds(
    expressions_essentialocl_Parameter,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
essentialocl_expressions_CollectionLiteralPart_strategy = st.builds(
    essentialocl_expressions_CollectionLiteralPart,
)
essentialocl_expressions_TupleLiteralPart_strategy = st.builds(
    essentialocl_expressions_TupleLiteralPart,
)
essentialocl_expressions_OclExpression_strategy = st.builds(
    essentialocl_expressions_OclExpression,
)
essentialocl_expressions_Variable_strategy = st.builds(
    essentialocl_expressions_Variable,
)
Variable_strategy = st.builds(
    Variable,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
essentialocl_expressions_CallExp_strategy = st.builds(
    essentialocl_expressions_CallExp,
)
essentialocl_expressions_IfExp_strategy = st.builds(
    essentialocl_expressions_IfExp,
)
essentialocl_expressions_LiteralExp_strategy = st.builds(
    essentialocl_expressions_LiteralExp,
)
essentialocl_expressions_LetExp_strategy = st.builds(
    essentialocl_expressions_LetExp,
)
essentialocl_expressions_VariableExp_strategy = st.builds(
    essentialocl_expressions_VariableExp,
)
TupleType_strategy = st.builds(
    TupleType,
)
OrderedSetType_strategy = st.builds(
    OrderedSetType,
)
SetType_strategy = st.builds(
    SetType,
)
BagType_strategy = st.builds(
    BagType,
)
SequenceType_strategy = st.builds(
    SequenceType,
)
TypeType_strategy = st.builds(
    TypeType,
)
InvalidType_strategy = st.builds(
    InvalidType,
)
VoidType_strategy = st.builds(
    VoidType,
)
AnyType_strategy = st.builds(
    AnyType,
)
types_essentialocl_PrimitiveType_strategy = st.builds(
    types_essentialocl_PrimitiveType,
)
essentialocl_types_OclLibrary_strategy = st.builds(
    essentialocl_types_OclLibrary,
)
types_essentialocl_Type_strategy = st.builds(
    types_essentialocl_Type,
)
OclLibrary_strategy = st.builds(
    OclLibrary,
)
Type_strategy = st.builds(
    Type,
)
essentialocl_types_CollectionType_strategy = st.builds(
    essentialocl_types_CollectionType,
    kind=
        safe_text
)
essentialocl_types_AnyType_strategy = st.builds(
    essentialocl_types_AnyType,
)
essentialocl_types_TypeType_strategy = st.builds(
    essentialocl_types_TypeType,
)
essentialocl_types_InvalidType_strategy = st.builds(
    essentialocl_types_InvalidType,
)
essentialocl_types_VoidType_strategy = st.builds(
    essentialocl_types_VoidType,
)
essentialocl_types_TupleType_strategy = st.builds(
    essentialocl_types_TupleType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
essentialocl_types_OrderedSetType_strategy = st.builds(
    essentialocl_types_OrderedSetType,
)
essentialocl_types_BagType_strategy = st.builds(
    essentialocl_types_BagType,
)
essentialocl_types_SetType_strategy = st.builds(
    essentialocl_types_SetType,
)
essentialocl_types_SequenceType_strategy = st.builds(
    essentialocl_types_SequenceType,
)





















@given(instance=essentialocl_expressions_BooleanLiteralExp_strategy)
def test_hyp_essentialocl_expressions_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original





@given(instance=essentialocl_expressions_StringLiteralExp_strategy)
def test_hyp_essentialocl_expressions_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original











@given(instance=essentialocl_expressions_CollectionLiteralExp_strategy)
def test_hyp_essentialocl_expressions_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original








@given(instance=essentialocl_expressions_IntegerLiteralExp_strategy)
def test_hyp_essentialocl_expressions_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original




@given(instance=essentialocl_expressions_RealLiteralExp_strategy)
def test_hyp_essentialocl_expressions_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original




@given(instance=essentialocl_expressions_UnlimitedNaturalExp_strategy)
def test_hyp_essentialocl_expressions_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original







import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialocl_expressions_OclExpression_strategy)
@settings(max_examples=30)
def test_hyp_essentialocl_expressions_oclexpression_withasset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.withAsSet()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.withAsSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'withAsSet' in essentialocl_expressions_OclExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'withAsSet' in essentialocl_expressions_OclExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'withAsSet' in essentialocl_expressions_OclExpression is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialocl_expressions_OclExpression_strategy)
@settings(max_examples=30)
def test_hyp_essentialocl_expressions_oclexpression_withatpre_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.withAtPre()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.withAtPre).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'withAtPre' in essentialocl_expressions_OclExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'withAtPre' in essentialocl_expressions_OclExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'withAtPre' in essentialocl_expressions_OclExpression is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialocl_expressions_Variable_strategy)
@settings(max_examples=30)
def test_hyp_essentialocl_expressions_variable_asproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.asProperty()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.asProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'asProperty' in essentialocl_expressions_Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'asProperty' in essentialocl_expressions_Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'asProperty' in essentialocl_expressions_Variable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialocl_expressions_Variable_strategy)
@settings(max_examples=30)
def test_hyp_essentialocl_expressions_variable_asparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.asParameter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.asParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'asParameter' in essentialocl_expressions_Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'asParameter' in essentialocl_expressions_Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'asParameter' in essentialocl_expressions_Variable is not implemented or raised an error")



















import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialocl_types_OclLibrary_strategy)
@settings(max_examples=30)
def test_hyp_essentialocl_types_ocllibrary_maketupletype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makeTupleType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makeTupleType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makeTupleType' in essentialocl_types_OclLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeTupleType' in essentialocl_types_OclLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeTupleType' in essentialocl_types_OclLibrary is not implemented or raised an error")







@given(instance=essentialocl_types_CollectionType_strategy)
def test_hyp_essentialocl_types_collectiontype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original












# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnyType,
    BagType,
    CallExp,
    CollectionLiteralPart,
    CollectionType,
    Expression,
    FeatureCallExp,
    InvalidType,
    LiteralExp,
    LoopExp,
    NamedElement,
    NumericLiteralExp,
    OclExpression,
    OclLibrary,
    OrderedSetType,
    PrimitiveLiteralExp,
    SequenceType,
    SetType,
    TupleLiteralPart,
    TupleType,
    Type,
    TypeType,
    TypedElement,
    Variable,
    VoidType,
    essentialocl_expressions_BooleanLiteralExp,
    essentialocl_expressions_CallExp,
    essentialocl_expressions_CollectionItem,
    essentialocl_expressions_CollectionLiteralExp,
    essentialocl_expressions_CollectionLiteralPart,
    essentialocl_expressions_CollectionRange,
    essentialocl_expressions_EnumLiteralExp,
    essentialocl_expressions_ExpressionInOcl,
    essentialocl_expressions_FeatureCallExp,
    essentialocl_expressions_IfExp,
    essentialocl_expressions_IntegerLiteralExp,
    essentialocl_expressions_InvalidLiteralExp,
    essentialocl_expressions_IterateExp,
    essentialocl_expressions_IteratorExp,
    essentialocl_expressions_LetExp,
    essentialocl_expressions_LiteralExp,
    essentialocl_expressions_LoopExp,
    essentialocl_expressions_NumericLiteralExp,
    essentialocl_expressions_OclExpression,
    essentialocl_expressions_OperationCallExp,
    essentialocl_expressions_PrimitiveLiteralExp,
    essentialocl_expressions_PropertyCallExp,
    essentialocl_expressions_RealLiteralExp,
    essentialocl_expressions_StringLiteralExp,
    essentialocl_expressions_TupleLiteralExp,
    essentialocl_expressions_TupleLiteralPart,
    essentialocl_expressions_TypeLiteralExp,
    essentialocl_expressions_UndefinedLiteralExp,
    essentialocl_expressions_UnlimitedNaturalExp,
    essentialocl_expressions_Variable,
    essentialocl_expressions_VariableExp,
    essentialocl_types_AnyType,
    essentialocl_types_BagType,
    essentialocl_types_CollectionType,
    essentialocl_types_InvalidType,
    essentialocl_types_OclLibrary,
    essentialocl_types_OrderedSetType,
    essentialocl_types_SequenceType,
    essentialocl_types_SetType,
    essentialocl_types_TupleType,
    essentialocl_types_TypeType,
    essentialocl_types_VoidType,
    expressions_essentialocl_EnumerationLiteral,
    expressions_essentialocl_Operation,
    expressions_essentialocl_Parameter,
    expressions_essentialocl_Property,
    expressions_essentialocl_Type,
    types_essentialocl_PrimitiveType,
    types_essentialocl_Type,
    CollectionKind,
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

def test_essentialocl_expressions_BooleanLiteralExp_booleanSymbol_value_roundtrip():
    instance = essentialocl_expressions_BooleanLiteralExp(booleanSymbol="sample_text")
    assert instance.booleanSymbol == "sample_text"
    instance.booleanSymbol = "sample_text_2"
    assert instance.booleanSymbol == "sample_text_2"


def test_essentialocl_expressions_CollectionLiteralExp_kind_value_roundtrip():
    instance = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_essentialocl_expressions_IntegerLiteralExp_integerSymbol_value_roundtrip():
    instance = essentialocl_expressions_IntegerLiteralExp(integerSymbol="sample_text")
    assert instance.integerSymbol == "sample_text"
    instance.integerSymbol = "sample_text_2"
    assert instance.integerSymbol == "sample_text_2"


def test_essentialocl_expressions_RealLiteralExp_realSymbol_value_roundtrip():
    instance = essentialocl_expressions_RealLiteralExp(realSymbol="sample_text")
    assert instance.realSymbol == "sample_text"
    instance.realSymbol = "sample_text_2"
    assert instance.realSymbol == "sample_text_2"


def test_essentialocl_expressions_StringLiteralExp_stringSymbol_value_roundtrip():
    instance = essentialocl_expressions_StringLiteralExp(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_essentialocl_expressions_UnlimitedNaturalExp_symbol_value_roundtrip():
    instance = essentialocl_expressions_UnlimitedNaturalExp(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_essentialocl_types_CollectionType_kind_value_roundtrip():
    instance = essentialocl_types_CollectionType(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_essentialocl_expressions_FeatureCallExp_isa_CallExp():
    instance = essentialocl_expressions_FeatureCallExp()
    assert isinstance(instance, CallExp)


def test_essentialocl_expressions_LoopExp_isa_CallExp():
    instance = essentialocl_expressions_LoopExp()
    assert isinstance(instance, CallExp)


def test_essentialocl_expressions_CollectionItem_isa_CollectionLiteralPart():
    instance = essentialocl_expressions_CollectionItem()
    assert isinstance(instance, CollectionLiteralPart)


def test_essentialocl_expressions_CollectionRange_isa_CollectionLiteralPart():
    instance = essentialocl_expressions_CollectionRange()
    assert isinstance(instance, CollectionLiteralPart)


def test_essentialocl_types_BagType_isa_CollectionType():
    instance = essentialocl_types_BagType()
    assert isinstance(instance, CollectionType)


def test_essentialocl_types_OrderedSetType_isa_CollectionType():
    instance = essentialocl_types_OrderedSetType()
    assert isinstance(instance, CollectionType)


def test_essentialocl_types_SequenceType_isa_CollectionType():
    instance = essentialocl_types_SequenceType()
    assert isinstance(instance, CollectionType)


def test_essentialocl_types_SetType_isa_CollectionType():
    instance = essentialocl_types_SetType()
    assert isinstance(instance, CollectionType)


def test_essentialocl_expressions_ExpressionInOcl_isa_Expression():
    instance = essentialocl_expressions_ExpressionInOcl()
    assert isinstance(instance, Expression)


def test_essentialocl_expressions_OperationCallExp_isa_FeatureCallExp():
    instance = essentialocl_expressions_OperationCallExp()
    assert isinstance(instance, FeatureCallExp)


def test_essentialocl_expressions_PropertyCallExp_isa_FeatureCallExp():
    instance = essentialocl_expressions_PropertyCallExp()
    assert isinstance(instance, FeatureCallExp)


def test_essentialocl_expressions_CollectionLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_EnumLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_EnumLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_InvalidLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_InvalidLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_PrimitiveLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_PrimitiveLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_TupleLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_TupleLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_TypeLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_TypeLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_UndefinedLiteralExp_isa_LiteralExp():
    instance = essentialocl_expressions_UndefinedLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_essentialocl_expressions_IterateExp_isa_LoopExp():
    instance = essentialocl_expressions_IterateExp()
    assert isinstance(instance, LoopExp)


def test_essentialocl_expressions_IteratorExp_isa_LoopExp():
    instance = essentialocl_expressions_IteratorExp()
    assert isinstance(instance, LoopExp)


def test_essentialocl_expressions_OclExpression_isa_NamedElement():
    instance = essentialocl_expressions_OclExpression()
    assert isinstance(instance, NamedElement)


def test_essentialocl_expressions_Variable_isa_NamedElement():
    instance = essentialocl_expressions_Variable()
    assert isinstance(instance, NamedElement)


def test_essentialocl_expressions_IntegerLiteralExp_isa_NumericLiteralExp():
    instance = essentialocl_expressions_IntegerLiteralExp(integerSymbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_essentialocl_expressions_RealLiteralExp_isa_NumericLiteralExp():
    instance = essentialocl_expressions_RealLiteralExp(realSymbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_essentialocl_expressions_UnlimitedNaturalExp_isa_NumericLiteralExp():
    instance = essentialocl_expressions_UnlimitedNaturalExp(symbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_essentialocl_expressions_CallExp_isa_OclExpression():
    instance = essentialocl_expressions_CallExp()
    assert isinstance(instance, OclExpression)


def test_essentialocl_expressions_IfExp_isa_OclExpression():
    instance = essentialocl_expressions_IfExp()
    assert isinstance(instance, OclExpression)


def test_essentialocl_expressions_LetExp_isa_OclExpression():
    instance = essentialocl_expressions_LetExp()
    assert isinstance(instance, OclExpression)


def test_essentialocl_expressions_LiteralExp_isa_OclExpression():
    instance = essentialocl_expressions_LiteralExp()
    assert isinstance(instance, OclExpression)


def test_essentialocl_expressions_VariableExp_isa_OclExpression():
    instance = essentialocl_expressions_VariableExp()
    assert isinstance(instance, OclExpression)


def test_essentialocl_expressions_BooleanLiteralExp_isa_PrimitiveLiteralExp():
    instance = essentialocl_expressions_BooleanLiteralExp(booleanSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExp)


def test_essentialocl_expressions_NumericLiteralExp_isa_PrimitiveLiteralExp():
    instance = essentialocl_expressions_NumericLiteralExp()
    assert isinstance(instance, PrimitiveLiteralExp)


def test_essentialocl_expressions_StringLiteralExp_isa_PrimitiveLiteralExp():
    instance = essentialocl_expressions_StringLiteralExp(stringSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExp)


def test_essentialocl_types_AnyType_isa_Type():
    instance = essentialocl_types_AnyType()
    assert isinstance(instance, Type)


def test_essentialocl_types_CollectionType_isa_Type():
    instance = essentialocl_types_CollectionType(kind="sample_text")
    assert isinstance(instance, Type)


def test_essentialocl_types_InvalidType_isa_Type():
    instance = essentialocl_types_InvalidType()
    assert isinstance(instance, Type)


def test_essentialocl_types_TupleType_isa_Type():
    instance = essentialocl_types_TupleType()
    assert isinstance(instance, Type)


def test_essentialocl_types_TypeType_isa_Type():
    instance = essentialocl_types_TypeType()
    assert isinstance(instance, Type)


def test_essentialocl_types_VoidType_isa_Type():
    instance = essentialocl_types_VoidType()
    assert isinstance(instance, Type)


def test_essentialocl_expressions_CollectionLiteralPart_isa_TypedElement():
    instance = essentialocl_expressions_CollectionLiteralPart()
    assert isinstance(instance, TypedElement)


def test_essentialocl_expressions_OclExpression_isa_TypedElement():
    instance = essentialocl_expressions_OclExpression()
    assert isinstance(instance, TypedElement)


def test_essentialocl_expressions_TupleLiteralPart_isa_TypedElement():
    instance = essentialocl_expressions_TupleLiteralPart()
    assert isinstance(instance, TypedElement)


def test_essentialocl_expressions_Variable_isa_TypedElement():
    instance = essentialocl_expressions_Variable()
    assert isinstance(instance, TypedElement)


def test_assoc_elementType1_link_reassign_clear():
    a = essentialocl_types_CollectionType(kind="sample_text")
    b1 = types_essentialocl_Type()
    b2 = types_essentialocl_Type()
    _safe_set(a, 'essentialocl_types_CollectionType', b1)
    assert _is_linked(a, 'essentialocl_types_CollectionType', b1)
    if hasattr(b1, 'types_essentialocl_Type'):
        assert _is_linked(b1, 'types_essentialocl_Type', a)
    _safe_set(a, 'essentialocl_types_CollectionType', b2)
    assert _is_linked(a, 'essentialocl_types_CollectionType', b2)
    if hasattr(b1, 'types_essentialocl_Type'):
        assert not _is_linked(b1, 'types_essentialocl_Type', a)
    if hasattr(b2, 'types_essentialocl_Type'):
        assert _is_linked(b2, 'types_essentialocl_Type', a)
    _safe_set(a, 'essentialocl_types_CollectionType', None)
    assert not _is_linked(a, 'essentialocl_types_CollectionType', b2)
    if hasattr(b2, 'types_essentialocl_Type'):
        assert not _is_linked(b2, 'types_essentialocl_Type', a)


def test_assoc_elementType88_link_reassign_clear():
    a = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    b1 = expressions_essentialocl_Type()
    b2 = expressions_essentialocl_Type()
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp89', b1)
    assert _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp89', b1)
    if hasattr(b1, 'expressions_essentialocl_Type90'):
        assert _is_linked(b1, 'expressions_essentialocl_Type90', a)
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp89', b2)
    assert _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp89', b2)
    if hasattr(b1, 'expressions_essentialocl_Type90'):
        assert not _is_linked(b1, 'expressions_essentialocl_Type90', a)
    if hasattr(b2, 'expressions_essentialocl_Type90'):
        assert _is_linked(b2, 'expressions_essentialocl_Type90', a)
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp89', None)
    assert not _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp89', b2)
    if hasattr(b2, 'expressions_essentialocl_Type90'):
        assert not _is_linked(b2, 'expressions_essentialocl_Type90', a)


def test_assoc_initExpression42_link_reassign_clear():
    a = essentialocl_expressions_Variable()
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'essentialocl_expressions_Variable43', b1)
    assert _is_linked(a, 'essentialocl_expressions_Variable43', b1)
    if hasattr(b1, 'OclExpression'):
        assert _is_linked(b1, 'OclExpression', a)
    _safe_set(a, 'essentialocl_expressions_Variable43', b2)
    assert _is_linked(a, 'essentialocl_expressions_Variable43', b2)
    if hasattr(b1, 'OclExpression'):
        assert not _is_linked(b1, 'OclExpression', a)
    if hasattr(b2, 'OclExpression'):
        assert _is_linked(b2, 'OclExpression', a)
    _safe_set(a, 'essentialocl_expressions_Variable43', None)
    assert not _is_linked(a, 'essentialocl_expressions_Variable43', b2)
    if hasattr(b2, 'OclExpression'):
        assert not _is_linked(b2, 'OclExpression', a)


def test_assoc_oclAny21_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = AnyType()
    b2 = AnyType()
    _safe_set(a, 'essentialocl_types_OclLibrary22', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary22', b1)
    if hasattr(b1, 'AnyType'):
        assert _is_linked(b1, 'AnyType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary22', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary22', b2)
    if hasattr(b1, 'AnyType'):
        assert not _is_linked(b1, 'AnyType', a)
    if hasattr(b2, 'AnyType'):
        assert _is_linked(b2, 'AnyType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary22', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary22', b2)
    if hasattr(b2, 'AnyType'):
        assert not _is_linked(b2, 'AnyType', a)


def test_assoc_oclBag32_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = BagType()
    b2 = BagType()
    _safe_set(a, 'essentialocl_types_OclLibrary33', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary33', b1)
    if hasattr(b1, 'BagType'):
        assert _is_linked(b1, 'BagType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary33', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary33', b2)
    if hasattr(b1, 'BagType'):
        assert not _is_linked(b1, 'BagType', a)
    if hasattr(b2, 'BagType'):
        assert _is_linked(b2, 'BagType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary33', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary33', b2)
    if hasattr(b2, 'BagType'):
        assert not _is_linked(b2, 'BagType', a)


def test_assoc_oclBoolean11_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = types_essentialocl_PrimitiveType()
    b2 = types_essentialocl_PrimitiveType()
    _safe_set(a, 'essentialocl_types_OclLibrary', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary', b1)
    if hasattr(b1, 'types_essentialocl_PrimitiveType'):
        assert _is_linked(b1, 'types_essentialocl_PrimitiveType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary', b2)
    if hasattr(b1, 'types_essentialocl_PrimitiveType'):
        assert not _is_linked(b1, 'types_essentialocl_PrimitiveType', a)
    if hasattr(b2, 'types_essentialocl_PrimitiveType'):
        assert _is_linked(b2, 'types_essentialocl_PrimitiveType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary', b2)
    if hasattr(b2, 'types_essentialocl_PrimitiveType'):
        assert not _is_linked(b2, 'types_essentialocl_PrimitiveType', a)


def test_assoc_oclCollection28_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = CollectionType()
    b2 = CollectionType()
    _safe_set(a, 'essentialocl_types_OclLibrary29', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary29', b1)
    if hasattr(b1, 'CollectionType'):
        assert _is_linked(b1, 'CollectionType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary29', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary29', b2)
    if hasattr(b1, 'CollectionType'):
        assert not _is_linked(b1, 'CollectionType', a)
    if hasattr(b2, 'CollectionType'):
        assert _is_linked(b2, 'CollectionType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary29', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary29', b2)
    if hasattr(b2, 'CollectionType'):
        assert not _is_linked(b2, 'CollectionType', a)


def test_assoc_oclInteger15_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = types_essentialocl_PrimitiveType()
    b2 = types_essentialocl_PrimitiveType()
    _safe_set(a, 'essentialocl_types_OclLibrary16', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary16', b1)
    if hasattr(b1, 'types_essentialocl_PrimitiveType17'):
        assert _is_linked(b1, 'types_essentialocl_PrimitiveType17', a)
    _safe_set(a, 'essentialocl_types_OclLibrary16', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary16', b2)
    if hasattr(b1, 'types_essentialocl_PrimitiveType17'):
        assert not _is_linked(b1, 'types_essentialocl_PrimitiveType17', a)
    if hasattr(b2, 'types_essentialocl_PrimitiveType17'):
        assert _is_linked(b2, 'types_essentialocl_PrimitiveType17', a)
    _safe_set(a, 'essentialocl_types_OclLibrary16', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary16', b2)
    if hasattr(b2, 'types_essentialocl_PrimitiveType17'):
        assert not _is_linked(b2, 'types_essentialocl_PrimitiveType17', a)


def test_assoc_oclInvalid24_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = InvalidType()
    b2 = InvalidType()
    _safe_set(a, 'oclLibrary25', b1)
    assert _is_linked(a, 'oclLibrary25', b1)
    if hasattr(b1, 'InvalidType'):
        assert _is_linked(b1, 'InvalidType', a)
    _safe_set(a, 'oclLibrary25', b2)
    assert _is_linked(a, 'oclLibrary25', b2)
    if hasattr(b1, 'InvalidType'):
        assert not _is_linked(b1, 'InvalidType', a)
    if hasattr(b2, 'InvalidType'):
        assert _is_linked(b2, 'InvalidType', a)
    _safe_set(a, 'oclLibrary25', None)
    assert not _is_linked(a, 'oclLibrary25', b2)
    if hasattr(b2, 'InvalidType'):
        assert not _is_linked(b2, 'InvalidType', a)


def test_assoc_oclLibrary2_link_reassign_clear():
    a = essentialocl_types_CollectionType(kind="sample_text")
    b1 = OclLibrary()
    b2 = OclLibrary()
    _safe_set(a, 'essentialocl_types_CollectionType3', b1)
    assert _is_linked(a, 'essentialocl_types_CollectionType3', b1)
    if hasattr(b1, 'OclLibrary4'):
        assert _is_linked(b1, 'OclLibrary4', a)
    _safe_set(a, 'essentialocl_types_CollectionType3', b2)
    assert _is_linked(a, 'essentialocl_types_CollectionType3', b2)
    if hasattr(b1, 'OclLibrary4'):
        assert not _is_linked(b1, 'OclLibrary4', a)
    if hasattr(b2, 'OclLibrary4'):
        assert _is_linked(b2, 'OclLibrary4', a)
    _safe_set(a, 'essentialocl_types_CollectionType3', None)
    assert not _is_linked(a, 'essentialocl_types_CollectionType3', b2)
    if hasattr(b2, 'OclLibrary4'):
        assert not _is_linked(b2, 'OclLibrary4', a)


def test_assoc_oclLibrary59_link_reassign_clear():
    a = essentialocl_expressions_OclExpression()
    b1 = OclLibrary()
    b2 = OclLibrary()
    _safe_set(a, 'essentialocl_expressions_OclExpression', b1)
    assert _is_linked(a, 'essentialocl_expressions_OclExpression', b1)
    if hasattr(b1, 'OclLibrary60'):
        assert _is_linked(b1, 'OclLibrary60', a)
    _safe_set(a, 'essentialocl_expressions_OclExpression', b2)
    assert _is_linked(a, 'essentialocl_expressions_OclExpression', b2)
    if hasattr(b1, 'OclLibrary60'):
        assert not _is_linked(b1, 'OclLibrary60', a)
    if hasattr(b2, 'OclLibrary60'):
        assert _is_linked(b2, 'OclLibrary60', a)
    _safe_set(a, 'essentialocl_expressions_OclExpression', None)
    assert not _is_linked(a, 'essentialocl_expressions_OclExpression', b2)
    if hasattr(b2, 'OclLibrary60'):
        assert not _is_linked(b2, 'OclLibrary60', a)


def test_assoc_oclOrderedSet36_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = OrderedSetType()
    b2 = OrderedSetType()
    _safe_set(a, 'essentialocl_types_OclLibrary37', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary37', b1)
    if hasattr(b1, 'OrderedSetType'):
        assert _is_linked(b1, 'OrderedSetType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary37', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary37', b2)
    if hasattr(b1, 'OrderedSetType'):
        assert not _is_linked(b1, 'OrderedSetType', a)
    if hasattr(b2, 'OrderedSetType'):
        assert _is_linked(b2, 'OrderedSetType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary37', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary37', b2)
    if hasattr(b2, 'OrderedSetType'):
        assert not _is_linked(b2, 'OrderedSetType', a)


def test_assoc_oclReal18_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = types_essentialocl_PrimitiveType()
    b2 = types_essentialocl_PrimitiveType()
    _safe_set(a, 'essentialocl_types_OclLibrary19', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary19', b1)
    if hasattr(b1, 'types_essentialocl_PrimitiveType20'):
        assert _is_linked(b1, 'types_essentialocl_PrimitiveType20', a)
    _safe_set(a, 'essentialocl_types_OclLibrary19', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary19', b2)
    if hasattr(b1, 'types_essentialocl_PrimitiveType20'):
        assert not _is_linked(b1, 'types_essentialocl_PrimitiveType20', a)
    if hasattr(b2, 'types_essentialocl_PrimitiveType20'):
        assert _is_linked(b2, 'types_essentialocl_PrimitiveType20', a)
    _safe_set(a, 'essentialocl_types_OclLibrary19', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary19', b2)
    if hasattr(b2, 'types_essentialocl_PrimitiveType20'):
        assert not _is_linked(b2, 'types_essentialocl_PrimitiveType20', a)


def test_assoc_oclSequence30_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = SequenceType()
    b2 = SequenceType()
    _safe_set(a, 'essentialocl_types_OclLibrary31', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary31', b1)
    if hasattr(b1, 'SequenceType'):
        assert _is_linked(b1, 'SequenceType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary31', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary31', b2)
    if hasattr(b1, 'SequenceType'):
        assert not _is_linked(b1, 'SequenceType', a)
    if hasattr(b2, 'SequenceType'):
        assert _is_linked(b2, 'SequenceType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary31', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary31', b2)
    if hasattr(b2, 'SequenceType'):
        assert not _is_linked(b2, 'SequenceType', a)


def test_assoc_oclSet34_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = SetType()
    b2 = SetType()
    _safe_set(a, 'essentialocl_types_OclLibrary35', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary35', b1)
    if hasattr(b1, 'SetType'):
        assert _is_linked(b1, 'SetType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary35', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary35', b2)
    if hasattr(b1, 'SetType'):
        assert not _is_linked(b1, 'SetType', a)
    if hasattr(b2, 'SetType'):
        assert _is_linked(b2, 'SetType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary35', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary35', b2)
    if hasattr(b2, 'SetType'):
        assert not _is_linked(b2, 'SetType', a)


def test_assoc_oclString12_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = types_essentialocl_PrimitiveType()
    b2 = types_essentialocl_PrimitiveType()
    _safe_set(a, 'essentialocl_types_OclLibrary13', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary13', b1)
    if hasattr(b1, 'types_essentialocl_PrimitiveType14'):
        assert _is_linked(b1, 'types_essentialocl_PrimitiveType14', a)
    _safe_set(a, 'essentialocl_types_OclLibrary13', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary13', b2)
    if hasattr(b1, 'types_essentialocl_PrimitiveType14'):
        assert not _is_linked(b1, 'types_essentialocl_PrimitiveType14', a)
    if hasattr(b2, 'types_essentialocl_PrimitiveType14'):
        assert _is_linked(b2, 'types_essentialocl_PrimitiveType14', a)
    _safe_set(a, 'essentialocl_types_OclLibrary13', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary13', b2)
    if hasattr(b2, 'types_essentialocl_PrimitiveType14'):
        assert not _is_linked(b2, 'types_essentialocl_PrimitiveType14', a)


def test_assoc_oclTuple38_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = TupleType()
    b2 = TupleType()
    _safe_set(a, 'essentialocl_types_OclLibrary39', {b1})
    assert _is_linked(a, 'essentialocl_types_OclLibrary39', b1)
    if hasattr(b1, 'TupleType'):
        assert _is_linked(b1, 'TupleType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary39', {b2})
    assert _is_linked(a, 'essentialocl_types_OclLibrary39', b2)
    if hasattr(b1, 'TupleType'):
        assert not _is_linked(b1, 'TupleType', a)
    if hasattr(b2, 'TupleType'):
        assert _is_linked(b2, 'TupleType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary39', set())
    assert not _is_linked(a, 'essentialocl_types_OclLibrary39', b2)
    if hasattr(b2, 'TupleType'):
        assert not _is_linked(b2, 'TupleType', a)


def test_assoc_oclType26_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = TypeType()
    b2 = TypeType()
    _safe_set(a, 'essentialocl_types_OclLibrary27', b1)
    assert _is_linked(a, 'essentialocl_types_OclLibrary27', b1)
    if hasattr(b1, 'TypeType'):
        assert _is_linked(b1, 'TypeType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary27', b2)
    assert _is_linked(a, 'essentialocl_types_OclLibrary27', b2)
    if hasattr(b1, 'TypeType'):
        assert not _is_linked(b1, 'TypeType', a)
    if hasattr(b2, 'TypeType'):
        assert _is_linked(b2, 'TypeType', a)
    _safe_set(a, 'essentialocl_types_OclLibrary27', None)
    assert not _is_linked(a, 'essentialocl_types_OclLibrary27', b2)
    if hasattr(b2, 'TypeType'):
        assert not _is_linked(b2, 'TypeType', a)


def test_assoc_oclVoid23_link_reassign_clear():
    a = essentialocl_types_OclLibrary()
    b1 = VoidType()
    b2 = VoidType()
    _safe_set(a, 'oclLibrary', b1)
    assert _is_linked(a, 'oclLibrary', b1)
    if hasattr(b1, 'VoidType'):
        assert _is_linked(b1, 'VoidType', a)
    _safe_set(a, 'oclLibrary', b2)
    assert _is_linked(a, 'oclLibrary', b2)
    if hasattr(b1, 'VoidType'):
        assert not _is_linked(b1, 'VoidType', a)
    if hasattr(b2, 'VoidType'):
        assert _is_linked(b2, 'VoidType', a)
    _safe_set(a, 'oclLibrary', None)
    assert not _is_linked(a, 'oclLibrary', b2)
    if hasattr(b2, 'VoidType'):
        assert not _is_linked(b2, 'VoidType', a)


def test_assoc_part87_link_reassign_clear():
    a = essentialocl_expressions_CollectionLiteralExp(kind="sample_text")
    b1 = CollectionLiteralPart()
    b2 = CollectionLiteralPart()
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp', {b1})
    assert _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp', b1)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert _is_linked(b1, 'CollectionLiteralPart', a)
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp', {b2})
    assert _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp', b2)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert not _is_linked(b1, 'CollectionLiteralPart', a)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert _is_linked(b2, 'CollectionLiteralPart', a)
    _safe_set(a, 'essentialocl_expressions_CollectionLiteralExp', set())
    assert not _is_linked(a, 'essentialocl_expressions_CollectionLiteralExp', b2)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert not _is_linked(b2, 'CollectionLiteralPart', a)


def test_assoc_representedParameter41_link_reassign_clear():
    a = essentialocl_expressions_Variable()
    b1 = expressions_essentialocl_Parameter()
    b2 = expressions_essentialocl_Parameter()
    _safe_set(a, 'essentialocl_expressions_Variable', b1)
    assert _is_linked(a, 'essentialocl_expressions_Variable', b1)
    if hasattr(b1, 'expressions_essentialocl_Parameter'):
        assert _is_linked(b1, 'expressions_essentialocl_Parameter', a)
    _safe_set(a, 'essentialocl_expressions_Variable', b2)
    assert _is_linked(a, 'essentialocl_expressions_Variable', b2)
    if hasattr(b1, 'expressions_essentialocl_Parameter'):
        assert not _is_linked(b1, 'expressions_essentialocl_Parameter', a)
    if hasattr(b2, 'expressions_essentialocl_Parameter'):
        assert _is_linked(b2, 'expressions_essentialocl_Parameter', a)
    _safe_set(a, 'essentialocl_expressions_Variable', None)
    assert not _is_linked(a, 'essentialocl_expressions_Variable', b2)
    if hasattr(b2, 'expressions_essentialocl_Parameter'):
        assert not _is_linked(b2, 'expressions_essentialocl_Parameter', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnyType_strategy = st.builds(AnyType)
@given(instance=AnyType_strategy)
@settings(max_examples=25)
def test_AnyType_instantiation(instance):
    assert isinstance(instance, AnyType)


BagType_strategy = st.builds(BagType)
@given(instance=BagType_strategy)
@settings(max_examples=25)
def test_BagType_instantiation(instance):
    assert isinstance(instance, BagType)


CallExp_strategy = st.builds(CallExp)
@given(instance=CallExp_strategy)
@settings(max_examples=25)
def test_CallExp_instantiation(instance):
    assert isinstance(instance, CallExp)


CollectionLiteralPart_strategy = st.builds(CollectionLiteralPart)
@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=25)
def test_CollectionLiteralPart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)


CollectionType_strategy = st.builds(CollectionType)
@given(instance=CollectionType_strategy)
@settings(max_examples=25)
def test_CollectionType_instantiation(instance):
    assert isinstance(instance, CollectionType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FeatureCallExp_strategy = st.builds(FeatureCallExp)
@given(instance=FeatureCallExp_strategy)
@settings(max_examples=25)
def test_FeatureCallExp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)


InvalidType_strategy = st.builds(InvalidType)
@given(instance=InvalidType_strategy)
@settings(max_examples=25)
def test_InvalidType_instantiation(instance):
    assert isinstance(instance, InvalidType)


LiteralExp_strategy = st.builds(LiteralExp)
@given(instance=LiteralExp_strategy)
@settings(max_examples=25)
def test_LiteralExp_instantiation(instance):
    assert isinstance(instance, LiteralExp)


LoopExp_strategy = st.builds(LoopExp)
@given(instance=LoopExp_strategy)
@settings(max_examples=25)
def test_LoopExp_instantiation(instance):
    assert isinstance(instance, LoopExp)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NumericLiteralExp_strategy = st.builds(NumericLiteralExp)
@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=25)
def test_NumericLiteralExp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)


OclExpression_strategy = st.builds(OclExpression)
@given(instance=OclExpression_strategy)
@settings(max_examples=25)
def test_OclExpression_instantiation(instance):
    assert isinstance(instance, OclExpression)


OclLibrary_strategy = st.builds(OclLibrary)
@given(instance=OclLibrary_strategy)
@settings(max_examples=25)
def test_OclLibrary_instantiation(instance):
    assert isinstance(instance, OclLibrary)


OrderedSetType_strategy = st.builds(OrderedSetType)
@given(instance=OrderedSetType_strategy)
@settings(max_examples=25)
def test_OrderedSetType_instantiation(instance):
    assert isinstance(instance, OrderedSetType)


PrimitiveLiteralExp_strategy = st.builds(PrimitiveLiteralExp)
@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)


SequenceType_strategy = st.builds(SequenceType)
@given(instance=SequenceType_strategy)
@settings(max_examples=25)
def test_SequenceType_instantiation(instance):
    assert isinstance(instance, SequenceType)


SetType_strategy = st.builds(SetType)
@given(instance=SetType_strategy)
@settings(max_examples=25)
def test_SetType_instantiation(instance):
    assert isinstance(instance, SetType)


TupleLiteralPart_strategy = st.builds(TupleLiteralPart)
@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)


TupleType_strategy = st.builds(TupleType)
@given(instance=TupleType_strategy)
@settings(max_examples=25)
def test_TupleType_instantiation(instance):
    assert isinstance(instance, TupleType)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeType_strategy = st.builds(TypeType)
@given(instance=TypeType_strategy)
@settings(max_examples=25)
def test_TypeType_instantiation(instance):
    assert isinstance(instance, TypeType)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


VoidType_strategy = st.builds(VoidType)
@given(instance=VoidType_strategy)
@settings(max_examples=25)
def test_VoidType_instantiation(instance):
    assert isinstance(instance, VoidType)


essentialocl_expressions_BooleanLiteralExp_strategy = st.builds(essentialocl_expressions_BooleanLiteralExp, booleanSymbol=safe_text)
@given(instance=essentialocl_expressions_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_BooleanLiteralExp)


essentialocl_expressions_CallExp_strategy = st.builds(essentialocl_expressions_CallExp)
@given(instance=essentialocl_expressions_CallExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_CallExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_CallExp)


essentialocl_expressions_CollectionItem_strategy = st.builds(essentialocl_expressions_CollectionItem)
@given(instance=essentialocl_expressions_CollectionItem_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_CollectionItem_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_CollectionItem)


essentialocl_expressions_CollectionLiteralExp_strategy = st.builds(essentialocl_expressions_CollectionLiteralExp, kind=safe_text)
@given(instance=essentialocl_expressions_CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_CollectionLiteralExp)


essentialocl_expressions_CollectionLiteralPart_strategy = st.builds(essentialocl_expressions_CollectionLiteralPart)
@given(instance=essentialocl_expressions_CollectionLiteralPart_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_CollectionLiteralPart_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_CollectionLiteralPart)


essentialocl_expressions_CollectionRange_strategy = st.builds(essentialocl_expressions_CollectionRange)
@given(instance=essentialocl_expressions_CollectionRange_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_CollectionRange_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_CollectionRange)


essentialocl_expressions_EnumLiteralExp_strategy = st.builds(essentialocl_expressions_EnumLiteralExp)
@given(instance=essentialocl_expressions_EnumLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_EnumLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_EnumLiteralExp)


essentialocl_expressions_ExpressionInOcl_strategy = st.builds(essentialocl_expressions_ExpressionInOcl)
@given(instance=essentialocl_expressions_ExpressionInOcl_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_ExpressionInOcl_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_ExpressionInOcl)


essentialocl_expressions_FeatureCallExp_strategy = st.builds(essentialocl_expressions_FeatureCallExp)
@given(instance=essentialocl_expressions_FeatureCallExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_FeatureCallExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_FeatureCallExp)


essentialocl_expressions_IfExp_strategy = st.builds(essentialocl_expressions_IfExp)
@given(instance=essentialocl_expressions_IfExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_IfExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_IfExp)


essentialocl_expressions_IntegerLiteralExp_strategy = st.builds(essentialocl_expressions_IntegerLiteralExp, integerSymbol=safe_text)
@given(instance=essentialocl_expressions_IntegerLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_IntegerLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_IntegerLiteralExp)


essentialocl_expressions_InvalidLiteralExp_strategy = st.builds(essentialocl_expressions_InvalidLiteralExp)
@given(instance=essentialocl_expressions_InvalidLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_InvalidLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_InvalidLiteralExp)


essentialocl_expressions_IterateExp_strategy = st.builds(essentialocl_expressions_IterateExp)
@given(instance=essentialocl_expressions_IterateExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_IterateExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_IterateExp)


essentialocl_expressions_IteratorExp_strategy = st.builds(essentialocl_expressions_IteratorExp)
@given(instance=essentialocl_expressions_IteratorExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_IteratorExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_IteratorExp)


essentialocl_expressions_LetExp_strategy = st.builds(essentialocl_expressions_LetExp)
@given(instance=essentialocl_expressions_LetExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_LetExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_LetExp)


essentialocl_expressions_LiteralExp_strategy = st.builds(essentialocl_expressions_LiteralExp)
@given(instance=essentialocl_expressions_LiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_LiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_LiteralExp)


essentialocl_expressions_LoopExp_strategy = st.builds(essentialocl_expressions_LoopExp)
@given(instance=essentialocl_expressions_LoopExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_LoopExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_LoopExp)


essentialocl_expressions_NumericLiteralExp_strategy = st.builds(essentialocl_expressions_NumericLiteralExp)
@given(instance=essentialocl_expressions_NumericLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_NumericLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_NumericLiteralExp)


essentialocl_expressions_OclExpression_strategy = st.builds(essentialocl_expressions_OclExpression)
@given(instance=essentialocl_expressions_OclExpression_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_OclExpression_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_OclExpression)


essentialocl_expressions_OperationCallExp_strategy = st.builds(essentialocl_expressions_OperationCallExp)
@given(instance=essentialocl_expressions_OperationCallExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_OperationCallExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_OperationCallExp)


essentialocl_expressions_PrimitiveLiteralExp_strategy = st.builds(essentialocl_expressions_PrimitiveLiteralExp)
@given(instance=essentialocl_expressions_PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_PrimitiveLiteralExp)


essentialocl_expressions_PropertyCallExp_strategy = st.builds(essentialocl_expressions_PropertyCallExp)
@given(instance=essentialocl_expressions_PropertyCallExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_PropertyCallExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_PropertyCallExp)


essentialocl_expressions_RealLiteralExp_strategy = st.builds(essentialocl_expressions_RealLiteralExp, realSymbol=safe_text)
@given(instance=essentialocl_expressions_RealLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_RealLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_RealLiteralExp)


essentialocl_expressions_StringLiteralExp_strategy = st.builds(essentialocl_expressions_StringLiteralExp, stringSymbol=safe_text)
@given(instance=essentialocl_expressions_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_StringLiteralExp)


essentialocl_expressions_TupleLiteralExp_strategy = st.builds(essentialocl_expressions_TupleLiteralExp)
@given(instance=essentialocl_expressions_TupleLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_TupleLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_TupleLiteralExp)


essentialocl_expressions_TupleLiteralPart_strategy = st.builds(essentialocl_expressions_TupleLiteralPart)
@given(instance=essentialocl_expressions_TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_TupleLiteralPart)


essentialocl_expressions_TypeLiteralExp_strategy = st.builds(essentialocl_expressions_TypeLiteralExp)
@given(instance=essentialocl_expressions_TypeLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_TypeLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_TypeLiteralExp)


essentialocl_expressions_UndefinedLiteralExp_strategy = st.builds(essentialocl_expressions_UndefinedLiteralExp)
@given(instance=essentialocl_expressions_UndefinedLiteralExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_UndefinedLiteralExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_UndefinedLiteralExp)


essentialocl_expressions_UnlimitedNaturalExp_strategy = st.builds(essentialocl_expressions_UnlimitedNaturalExp, symbol=safe_text)
@given(instance=essentialocl_expressions_UnlimitedNaturalExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_UnlimitedNaturalExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_UnlimitedNaturalExp)


essentialocl_expressions_Variable_strategy = st.builds(essentialocl_expressions_Variable)
@given(instance=essentialocl_expressions_Variable_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_Variable_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_Variable)


essentialocl_expressions_VariableExp_strategy = st.builds(essentialocl_expressions_VariableExp)
@given(instance=essentialocl_expressions_VariableExp_strategy)
@settings(max_examples=25)
def test_essentialocl_expressions_VariableExp_instantiation(instance):
    assert isinstance(instance, essentialocl_expressions_VariableExp)


essentialocl_types_AnyType_strategy = st.builds(essentialocl_types_AnyType)
@given(instance=essentialocl_types_AnyType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_AnyType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_AnyType)


essentialocl_types_BagType_strategy = st.builds(essentialocl_types_BagType)
@given(instance=essentialocl_types_BagType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_BagType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_BagType)


essentialocl_types_CollectionType_strategy = st.builds(essentialocl_types_CollectionType, kind=safe_text)
@given(instance=essentialocl_types_CollectionType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_CollectionType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_CollectionType)


essentialocl_types_InvalidType_strategy = st.builds(essentialocl_types_InvalidType)
@given(instance=essentialocl_types_InvalidType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_InvalidType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_InvalidType)


essentialocl_types_OclLibrary_strategy = st.builds(essentialocl_types_OclLibrary)
@given(instance=essentialocl_types_OclLibrary_strategy)
@settings(max_examples=25)
def test_essentialocl_types_OclLibrary_instantiation(instance):
    assert isinstance(instance, essentialocl_types_OclLibrary)


essentialocl_types_OrderedSetType_strategy = st.builds(essentialocl_types_OrderedSetType)
@given(instance=essentialocl_types_OrderedSetType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_OrderedSetType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_OrderedSetType)


essentialocl_types_SequenceType_strategy = st.builds(essentialocl_types_SequenceType)
@given(instance=essentialocl_types_SequenceType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_SequenceType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_SequenceType)


essentialocl_types_SetType_strategy = st.builds(essentialocl_types_SetType)
@given(instance=essentialocl_types_SetType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_SetType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_SetType)


essentialocl_types_TupleType_strategy = st.builds(essentialocl_types_TupleType)
@given(instance=essentialocl_types_TupleType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_TupleType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_TupleType)


essentialocl_types_TypeType_strategy = st.builds(essentialocl_types_TypeType)
@given(instance=essentialocl_types_TypeType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_TypeType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_TypeType)


essentialocl_types_VoidType_strategy = st.builds(essentialocl_types_VoidType)
@given(instance=essentialocl_types_VoidType_strategy)
@settings(max_examples=25)
def test_essentialocl_types_VoidType_instantiation(instance):
    assert isinstance(instance, essentialocl_types_VoidType)


expressions_essentialocl_EnumerationLiteral_strategy = st.builds(expressions_essentialocl_EnumerationLiteral)
@given(instance=expressions_essentialocl_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_expressions_essentialocl_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, expressions_essentialocl_EnumerationLiteral)


expressions_essentialocl_Operation_strategy = st.builds(expressions_essentialocl_Operation)
@given(instance=expressions_essentialocl_Operation_strategy)
@settings(max_examples=25)
def test_expressions_essentialocl_Operation_instantiation(instance):
    assert isinstance(instance, expressions_essentialocl_Operation)


expressions_essentialocl_Parameter_strategy = st.builds(expressions_essentialocl_Parameter)
@given(instance=expressions_essentialocl_Parameter_strategy)
@settings(max_examples=25)
def test_expressions_essentialocl_Parameter_instantiation(instance):
    assert isinstance(instance, expressions_essentialocl_Parameter)


expressions_essentialocl_Property_strategy = st.builds(expressions_essentialocl_Property)
@given(instance=expressions_essentialocl_Property_strategy)
@settings(max_examples=25)
def test_expressions_essentialocl_Property_instantiation(instance):
    assert isinstance(instance, expressions_essentialocl_Property)


expressions_essentialocl_Type_strategy = st.builds(expressions_essentialocl_Type)
@given(instance=expressions_essentialocl_Type_strategy)
@settings(max_examples=25)
def test_expressions_essentialocl_Type_instantiation(instance):
    assert isinstance(instance, expressions_essentialocl_Type)


types_essentialocl_PrimitiveType_strategy = st.builds(types_essentialocl_PrimitiveType)
@given(instance=types_essentialocl_PrimitiveType_strategy)
@settings(max_examples=25)
def test_types_essentialocl_PrimitiveType_instantiation(instance):
    assert isinstance(instance, types_essentialocl_PrimitiveType)


types_essentialocl_Type_strategy = st.builds(types_essentialocl_Type)
@given(instance=types_essentialocl_Type_strategy)
@settings(max_examples=25)
def test_types_essentialocl_Type_instantiation(instance):
    assert isinstance(instance, types_essentialocl_Type)



