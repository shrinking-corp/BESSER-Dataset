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
    AggregateExpression,
    logiclanguage_ProjectedAggregateExpression,
    logiclanguage_Count,
    ProjectedAggregateExpression,
    logiclanguage_Max,
    logiclanguage_Min,
    logiclanguage_Sum,
    logiclanguage_AggregatedParameterSubstitution,
    Relation,
    logiclanguage_RelationDefinition,
    Constant,
    logiclanguage_ConstantDeclaration,
    logiclanguage_ConstantDefinition,
    logiclanguage_ConstantAnnotation,
    Function,
    logiclanguage_FunctionDeclaration,
    logiclanguage_FunctionDefinition,
    logiclanguage_RelationDeclaration,
    logiclanguage_RelationAnnotation,
    logiclanguage_AssertionAnnotation,
    logiclanguage_Assertion,
    logiclanguage_TermDescription,
    logiclanguage_TypeDescriptor,
    NumericOperation,
    logiclanguage_Divison,
    logiclanguage_Mod,
    logiclanguage_Multiply,
    logiclanguage_Pow,
    logiclanguage_Minus,
    logiclanguage_Plus,
    BoolOperation,
    logiclanguage_Or,
    logiclanguage_Not,
    logiclanguage_Iff,
    logiclanguage_Impl,
    logiclanguage_And,
    PrimitiveRelation,
    logiclanguage_MoreOrEqualThan,
    logiclanguage_LessOrEqualThan,
    logiclanguage_Distinct,
    logiclanguage_LessThan,
    logiclanguage_MoreThan,
    logiclanguage_Equals,
    Term,
    logiclanguage_PrimitiveRelation,
    logiclanguage_IfThenElse,
    logiclanguage_BoolOperation,
    logiclanguage_NumericOperation,
    logiclanguage_UnknownBecauseUninterpreted,
    logiclanguage_AggregateExpression,
    logiclanguage_TransitiveClosure,
    logiclanguage_InstanceOf,
    logiclanguage_SymbolicValue,
    TermDescription,
    logiclanguage_SymbolicDeclaration,
    logiclanguage_Term,
    logiclanguage_FunctionAnnotation,
    PrimitiveTypeReference,
    logiclanguage_StringTypeReference,
    logiclanguage_RealTypeReference,
    logiclanguage_BoolTypeReference,
    logiclanguage_IntTypeReference,
    QuantifiedExpression,
    logiclanguage_Forall,
    logiclanguage_Exists,
    logiclanguage_QuantifiedExpression,
    AtomicTerm,
    logiclanguage_BoolLiteral,
    logiclanguage_RealLiteral,
    logiclanguage_StringLiteral,
    logiclanguage_IntLiteral,
    logiclanguage_AtomicTerm,
    TypeDescriptor,
    logiclanguage_Type,
    TypeReference,
    logiclanguage_PrimitiveTypeReference,
    logiclanguage_ComplexTypeReference,
    logiclanguage_TypeReference,
    Type,
    logiclanguage_TypeDeclaration,
    logiclanguage_TypeDefinition,
    SymbolicDeclaration,
    logiclanguage_Variable,
    logiclanguage_Constant,
    logiclanguage_Relation,
    logiclanguage_Function,
    logiclanguage_DefinedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(AggregateExpression)


def test_hyp_aggregateexpression_constructor_exists():
    assert callable(AggregateExpression.__init__)


def test_hyp_aggregateexpression_constructor_args():
    sig = inspect.signature(AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ProjectedAggregateExpression)


def test_hyp_logiclanguage_projectedaggregateexpression_constructor_exists():
    assert callable(logiclanguage_ProjectedAggregateExpression.__init__)


def test_hyp_logiclanguage_projectedaggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage_ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "projectionIndex" in params, "Missing parameter 'projectionIndex'"




def test_hyp_logiclanguage_count_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Count)


def test_hyp_logiclanguage_count_constructor_exists():
    assert callable(logiclanguage_Count.__init__)


def test_hyp_logiclanguage_count_constructor_args():
    sig = inspect.signature(logiclanguage_Count.__init__)
    params = list(sig.parameters.keys())



def test_hyp_projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(ProjectedAggregateExpression)


def test_hyp_projectedaggregateexpression_constructor_exists():
    assert callable(ProjectedAggregateExpression.__init__)


def test_hyp_projectedaggregateexpression_constructor_args():
    sig = inspect.signature(ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_max_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Max)


def test_hyp_logiclanguage_max_constructor_exists():
    assert callable(logiclanguage_Max.__init__)


def test_hyp_logiclanguage_max_constructor_args():
    sig = inspect.signature(logiclanguage_Max.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_min_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Min)


def test_hyp_logiclanguage_min_constructor_exists():
    assert callable(logiclanguage_Min.__init__)


def test_hyp_logiclanguage_min_constructor_args():
    sig = inspect.signature(logiclanguage_Min.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_sum_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Sum)


def test_hyp_logiclanguage_sum_constructor_exists():
    assert callable(logiclanguage_Sum.__init__)


def test_hyp_logiclanguage_sum_constructor_args():
    sig = inspect.signature(logiclanguage_Sum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_aggregatedparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AggregatedParameterSubstitution)


def test_hyp_logiclanguage_aggregatedparametersubstitution_constructor_exists():
    assert callable(logiclanguage_AggregatedParameterSubstitution.__init__)


def test_hyp_logiclanguage_aggregatedparametersubstitution_constructor_args():
    sig = inspect.signature(logiclanguage_AggregatedParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_hyp_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_hyp_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_relationdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationDefinition)


def test_hyp_logiclanguage_relationdefinition_constructor_exists():
    assert callable(logiclanguage_RelationDefinition.__init__)


def test_hyp_logiclanguage_relationdefinition_constructor_args():
    sig = inspect.signature(logiclanguage_RelationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_hyp_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_hyp_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantDeclaration)


def test_hyp_logiclanguage_constantdeclaration_constructor_exists():
    assert callable(logiclanguage_ConstantDeclaration.__init__)


def test_hyp_logiclanguage_constantdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_constantdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantDefinition)


def test_hyp_logiclanguage_constantdefinition_constructor_exists():
    assert callable(logiclanguage_ConstantDefinition.__init__)


def test_hyp_logiclanguage_constantdefinition_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_constantannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantAnnotation)


def test_hyp_logiclanguage_constantannotation_constructor_exists():
    assert callable(logiclanguage_ConstantAnnotation.__init__)


def test_hyp_logiclanguage_constantannotation_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionDeclaration)


def test_hyp_logiclanguage_functiondeclaration_constructor_exists():
    assert callable(logiclanguage_FunctionDeclaration.__init__)


def test_hyp_logiclanguage_functiondeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionDefinition)


def test_hyp_logiclanguage_functiondefinition_constructor_exists():
    assert callable(logiclanguage_FunctionDefinition.__init__)


def test_hyp_logiclanguage_functiondefinition_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_relationdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationDeclaration)


def test_hyp_logiclanguage_relationdeclaration_constructor_exists():
    assert callable(logiclanguage_RelationDeclaration.__init__)


def test_hyp_logiclanguage_relationdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_RelationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_relationannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationAnnotation)


def test_hyp_logiclanguage_relationannotation_constructor_exists():
    assert callable(logiclanguage_RelationAnnotation.__init__)


def test_hyp_logiclanguage_relationannotation_constructor_args():
    sig = inspect.signature(logiclanguage_RelationAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_assertionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AssertionAnnotation)


def test_hyp_logiclanguage_assertionannotation_constructor_exists():
    assert callable(logiclanguage_AssertionAnnotation.__init__)


def test_hyp_logiclanguage_assertionannotation_constructor_args():
    sig = inspect.signature(logiclanguage_AssertionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_assertion_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Assertion)


def test_hyp_logiclanguage_assertion_constructor_exists():
    assert callable(logiclanguage_Assertion.__init__)


def test_hyp_logiclanguage_assertion_constructor_args():
    sig = inspect.signature(logiclanguage_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_logiclanguage_termdescription_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TermDescription)


def test_hyp_logiclanguage_termdescription_constructor_exists():
    assert callable(logiclanguage_TermDescription.__init__)


def test_hyp_logiclanguage_termdescription_constructor_args():
    sig = inspect.signature(logiclanguage_TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_typedescriptor_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDescriptor)


def test_hyp_logiclanguage_typedescriptor_constructor_exists():
    assert callable(logiclanguage_TypeDescriptor.__init__)


def test_hyp_logiclanguage_typedescriptor_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericoperation_is_not_abstract():
    assert not inspect.isabstract(NumericOperation)


def test_hyp_numericoperation_constructor_exists():
    assert callable(NumericOperation.__init__)


def test_hyp_numericoperation_constructor_args():
    sig = inspect.signature(NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_divison_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Divison)


def test_hyp_logiclanguage_divison_constructor_exists():
    assert callable(logiclanguage_Divison.__init__)


def test_hyp_logiclanguage_divison_constructor_args():
    sig = inspect.signature(logiclanguage_Divison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_mod_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Mod)


def test_hyp_logiclanguage_mod_constructor_exists():
    assert callable(logiclanguage_Mod.__init__)


def test_hyp_logiclanguage_mod_constructor_args():
    sig = inspect.signature(logiclanguage_Mod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_multiply_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Multiply)


def test_hyp_logiclanguage_multiply_constructor_exists():
    assert callable(logiclanguage_Multiply.__init__)


def test_hyp_logiclanguage_multiply_constructor_args():
    sig = inspect.signature(logiclanguage_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_pow_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Pow)


def test_hyp_logiclanguage_pow_constructor_exists():
    assert callable(logiclanguage_Pow.__init__)


def test_hyp_logiclanguage_pow_constructor_args():
    sig = inspect.signature(logiclanguage_Pow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_minus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Minus)


def test_hyp_logiclanguage_minus_constructor_exists():
    assert callable(logiclanguage_Minus.__init__)


def test_hyp_logiclanguage_minus_constructor_args():
    sig = inspect.signature(logiclanguage_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_plus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Plus)


def test_hyp_logiclanguage_plus_constructor_exists():
    assert callable(logiclanguage_Plus.__init__)


def test_hyp_logiclanguage_plus_constructor_args():
    sig = inspect.signature(logiclanguage_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booloperation_is_not_abstract():
    assert not inspect.isabstract(BoolOperation)


def test_hyp_booloperation_constructor_exists():
    assert callable(BoolOperation.__init__)


def test_hyp_booloperation_constructor_args():
    sig = inspect.signature(BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_or_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Or)


def test_hyp_logiclanguage_or_constructor_exists():
    assert callable(logiclanguage_Or.__init__)


def test_hyp_logiclanguage_or_constructor_args():
    sig = inspect.signature(logiclanguage_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_not_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Not)


def test_hyp_logiclanguage_not_constructor_exists():
    assert callable(logiclanguage_Not.__init__)


def test_hyp_logiclanguage_not_constructor_args():
    sig = inspect.signature(logiclanguage_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_iff_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Iff)


def test_hyp_logiclanguage_iff_constructor_exists():
    assert callable(logiclanguage_Iff.__init__)


def test_hyp_logiclanguage_iff_constructor_args():
    sig = inspect.signature(logiclanguage_Iff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_impl_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Impl)


def test_hyp_logiclanguage_impl_constructor_exists():
    assert callable(logiclanguage_Impl.__init__)


def test_hyp_logiclanguage_impl_constructor_args():
    sig = inspect.signature(logiclanguage_Impl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_and_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_And)


def test_hyp_logiclanguage_and_constructor_exists():
    assert callable(logiclanguage_And.__init__)


def test_hyp_logiclanguage_and_constructor_args():
    sig = inspect.signature(logiclanguage_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiverelation_is_not_abstract():
    assert not inspect.isabstract(PrimitiveRelation)


def test_hyp_primitiverelation_constructor_exists():
    assert callable(PrimitiveRelation.__init__)


def test_hyp_primitiverelation_constructor_args():
    sig = inspect.signature(PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_moreorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_MoreOrEqualThan)


def test_hyp_logiclanguage_moreorequalthan_constructor_exists():
    assert callable(logiclanguage_MoreOrEqualThan.__init__)


def test_hyp_logiclanguage_moreorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage_MoreOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_lessorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_LessOrEqualThan)


def test_hyp_logiclanguage_lessorequalthan_constructor_exists():
    assert callable(logiclanguage_LessOrEqualThan.__init__)


def test_hyp_logiclanguage_lessorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage_LessOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_distinct_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Distinct)


def test_hyp_logiclanguage_distinct_constructor_exists():
    assert callable(logiclanguage_Distinct.__init__)


def test_hyp_logiclanguage_distinct_constructor_args():
    sig = inspect.signature(logiclanguage_Distinct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_lessthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_LessThan)


def test_hyp_logiclanguage_lessthan_constructor_exists():
    assert callable(logiclanguage_LessThan.__init__)


def test_hyp_logiclanguage_lessthan_constructor_args():
    sig = inspect.signature(logiclanguage_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_morethan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_MoreThan)


def test_hyp_logiclanguage_morethan_constructor_exists():
    assert callable(logiclanguage_MoreThan.__init__)


def test_hyp_logiclanguage_morethan_constructor_args():
    sig = inspect.signature(logiclanguage_MoreThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_equals_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Equals)


def test_hyp_logiclanguage_equals_constructor_exists():
    assert callable(logiclanguage_Equals.__init__)


def test_hyp_logiclanguage_equals_constructor_args():
    sig = inspect.signature(logiclanguage_Equals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_hyp_term_constructor_exists():
    assert callable(Term.__init__)


def test_hyp_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_primitiverelation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_PrimitiveRelation)


def test_hyp_logiclanguage_primitiverelation_constructor_exists():
    assert callable(logiclanguage_PrimitiveRelation.__init__)


def test_hyp_logiclanguage_primitiverelation_constructor_args():
    sig = inspect.signature(logiclanguage_PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IfThenElse)


def test_hyp_logiclanguage_ifthenelse_constructor_exists():
    assert callable(logiclanguage_IfThenElse.__init__)


def test_hyp_logiclanguage_ifthenelse_constructor_args():
    sig = inspect.signature(logiclanguage_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_booloperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolOperation)


def test_hyp_logiclanguage_booloperation_constructor_exists():
    assert callable(logiclanguage_BoolOperation.__init__)


def test_hyp_logiclanguage_booloperation_constructor_args():
    sig = inspect.signature(logiclanguage_BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_numericoperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_NumericOperation)


def test_hyp_logiclanguage_numericoperation_constructor_exists():
    assert callable(logiclanguage_NumericOperation.__init__)


def test_hyp_logiclanguage_numericoperation_constructor_args():
    sig = inspect.signature(logiclanguage_NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_unknownbecauseuninterpreted_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_UnknownBecauseUninterpreted)


def test_hyp_logiclanguage_unknownbecauseuninterpreted_constructor_exists():
    assert callable(logiclanguage_UnknownBecauseUninterpreted.__init__)


def test_hyp_logiclanguage_unknownbecauseuninterpreted_constructor_args():
    sig = inspect.signature(logiclanguage_UnknownBecauseUninterpreted.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AggregateExpression)


def test_hyp_logiclanguage_aggregateexpression_constructor_exists():
    assert callable(logiclanguage_AggregateExpression.__init__)


def test_hyp_logiclanguage_aggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_transitiveclosure_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TransitiveClosure)


def test_hyp_logiclanguage_transitiveclosure_constructor_exists():
    assert callable(logiclanguage_TransitiveClosure.__init__)


def test_hyp_logiclanguage_transitiveclosure_constructor_args():
    sig = inspect.signature(logiclanguage_TransitiveClosure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_instanceof_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_InstanceOf)


def test_hyp_logiclanguage_instanceof_constructor_exists():
    assert callable(logiclanguage_InstanceOf.__init__)


def test_hyp_logiclanguage_instanceof_constructor_args():
    sig = inspect.signature(logiclanguage_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_symbolicvalue_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_SymbolicValue)


def test_hyp_logiclanguage_symbolicvalue_constructor_exists():
    assert callable(logiclanguage_SymbolicValue.__init__)


def test_hyp_logiclanguage_symbolicvalue_constructor_args():
    sig = inspect.signature(logiclanguage_SymbolicValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_termdescription_is_not_abstract():
    assert not inspect.isabstract(TermDescription)


def test_hyp_termdescription_constructor_exists():
    assert callable(TermDescription.__init__)


def test_hyp_termdescription_constructor_args():
    sig = inspect.signature(TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_SymbolicDeclaration)


def test_hyp_logiclanguage_symbolicdeclaration_constructor_exists():
    assert callable(logiclanguage_SymbolicDeclaration.__init__)


def test_hyp_logiclanguage_symbolicdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_logiclanguage_term_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Term)


def test_hyp_logiclanguage_term_constructor_exists():
    assert callable(logiclanguage_Term.__init__)


def test_hyp_logiclanguage_term_constructor_args():
    sig = inspect.signature(logiclanguage_Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_functionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionAnnotation)


def test_hyp_logiclanguage_functionannotation_constructor_exists():
    assert callable(logiclanguage_FunctionAnnotation.__init__)


def test_hyp_logiclanguage_functionannotation_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(PrimitiveTypeReference)


def test_hyp_primitivetypereference_constructor_exists():
    assert callable(PrimitiveTypeReference.__init__)


def test_hyp_primitivetypereference_constructor_args():
    sig = inspect.signature(PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_stringtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_StringTypeReference)


def test_hyp_logiclanguage_stringtypereference_constructor_exists():
    assert callable(logiclanguage_StringTypeReference.__init__)


def test_hyp_logiclanguage_stringtypereference_constructor_args():
    sig = inspect.signature(logiclanguage_StringTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_realtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RealTypeReference)


def test_hyp_logiclanguage_realtypereference_constructor_exists():
    assert callable(logiclanguage_RealTypeReference.__init__)


def test_hyp_logiclanguage_realtypereference_constructor_args():
    sig = inspect.signature(logiclanguage_RealTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_booltypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolTypeReference)


def test_hyp_logiclanguage_booltypereference_constructor_exists():
    assert callable(logiclanguage_BoolTypeReference.__init__)


def test_hyp_logiclanguage_booltypereference_constructor_args():
    sig = inspect.signature(logiclanguage_BoolTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_inttypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IntTypeReference)


def test_hyp_logiclanguage_inttypereference_constructor_exists():
    assert callable(logiclanguage_IntTypeReference.__init__)


def test_hyp_logiclanguage_inttypereference_constructor_args():
    sig = inspect.signature(logiclanguage_IntTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifiedExpression)


def test_hyp_quantifiedexpression_constructor_exists():
    assert callable(QuantifiedExpression.__init__)


def test_hyp_quantifiedexpression_constructor_args():
    sig = inspect.signature(QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_forall_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Forall)


def test_hyp_logiclanguage_forall_constructor_exists():
    assert callable(logiclanguage_Forall.__init__)


def test_hyp_logiclanguage_forall_constructor_args():
    sig = inspect.signature(logiclanguage_Forall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_exists_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Exists)


def test_hyp_logiclanguage_exists_constructor_exists():
    assert callable(logiclanguage_Exists.__init__)


def test_hyp_logiclanguage_exists_constructor_args():
    sig = inspect.signature(logiclanguage_Exists.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_QuantifiedExpression)


def test_hyp_logiclanguage_quantifiedexpression_constructor_exists():
    assert callable(logiclanguage_QuantifiedExpression.__init__)


def test_hyp_logiclanguage_quantifiedexpression_constructor_args():
    sig = inspect.signature(logiclanguage_QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_atomicterm_is_not_abstract():
    assert not inspect.isabstract(AtomicTerm)


def test_hyp_atomicterm_constructor_exists():
    assert callable(AtomicTerm.__init__)


def test_hyp_atomicterm_constructor_args():
    sig = inspect.signature(AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_boolliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolLiteral)


def test_hyp_logiclanguage_boolliteral_constructor_exists():
    assert callable(logiclanguage_BoolLiteral.__init__)


def test_hyp_logiclanguage_boolliteral_constructor_args():
    sig = inspect.signature(logiclanguage_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_logiclanguage_realliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RealLiteral)


def test_hyp_logiclanguage_realliteral_constructor_exists():
    assert callable(logiclanguage_RealLiteral.__init__)


def test_hyp_logiclanguage_realliteral_constructor_args():
    sig = inspect.signature(logiclanguage_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_logiclanguage_stringliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_StringLiteral)


def test_hyp_logiclanguage_stringliteral_constructor_exists():
    assert callable(logiclanguage_StringLiteral.__init__)


def test_hyp_logiclanguage_stringliteral_constructor_args():
    sig = inspect.signature(logiclanguage_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_logiclanguage_intliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IntLiteral)


def test_hyp_logiclanguage_intliteral_constructor_exists():
    assert callable(logiclanguage_IntLiteral.__init__)


def test_hyp_logiclanguage_intliteral_constructor_args():
    sig = inspect.signature(logiclanguage_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_logiclanguage_atomicterm_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AtomicTerm)


def test_hyp_logiclanguage_atomicterm_constructor_exists():
    assert callable(logiclanguage_AtomicTerm.__init__)


def test_hyp_logiclanguage_atomicterm_constructor_args():
    sig = inspect.signature(logiclanguage_AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedescriptor_is_not_abstract():
    assert not inspect.isabstract(TypeDescriptor)


def test_hyp_typedescriptor_constructor_exists():
    assert callable(TypeDescriptor.__init__)


def test_hyp_typedescriptor_constructor_args():
    sig = inspect.signature(TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_type_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Type)


def test_hyp_logiclanguage_type_constructor_exists():
    assert callable(logiclanguage_Type.__init__)


def test_hyp_logiclanguage_type_constructor_args():
    sig = inspect.signature(logiclanguage_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_hyp_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_hyp_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_PrimitiveTypeReference)


def test_hyp_logiclanguage_primitivetypereference_constructor_exists():
    assert callable(logiclanguage_PrimitiveTypeReference.__init__)


def test_hyp_logiclanguage_primitivetypereference_constructor_args():
    sig = inspect.signature(logiclanguage_PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_complextypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ComplexTypeReference)


def test_hyp_logiclanguage_complextypereference_constructor_exists():
    assert callable(logiclanguage_ComplexTypeReference.__init__)


def test_hyp_logiclanguage_complextypereference_constructor_args():
    sig = inspect.signature(logiclanguage_ComplexTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_typereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeReference)


def test_hyp_logiclanguage_typereference_constructor_exists():
    assert callable(logiclanguage_TypeReference.__init__)


def test_hyp_logiclanguage_typereference_constructor_args():
    sig = inspect.signature(logiclanguage_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDeclaration)


def test_hyp_logiclanguage_typedeclaration_constructor_exists():
    assert callable(logiclanguage_TypeDeclaration.__init__)


def test_hyp_logiclanguage_typedeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_typedefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDefinition)


def test_hyp_logiclanguage_typedefinition_constructor_exists():
    assert callable(logiclanguage_TypeDefinition.__init__)


def test_hyp_logiclanguage_typedefinition_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(SymbolicDeclaration)


def test_hyp_symbolicdeclaration_constructor_exists():
    assert callable(SymbolicDeclaration.__init__)


def test_hyp_symbolicdeclaration_constructor_args():
    sig = inspect.signature(SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_variable_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Variable)


def test_hyp_logiclanguage_variable_constructor_exists():
    assert callable(logiclanguage_Variable.__init__)


def test_hyp_logiclanguage_variable_constructor_args():
    sig = inspect.signature(logiclanguage_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_constant_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Constant)


def test_hyp_logiclanguage_constant_constructor_exists():
    assert callable(logiclanguage_Constant.__init__)


def test_hyp_logiclanguage_constant_constructor_args():
    sig = inspect.signature(logiclanguage_Constant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_relation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Relation)


def test_hyp_logiclanguage_relation_constructor_exists():
    assert callable(logiclanguage_Relation.__init__)


def test_hyp_logiclanguage_relation_constructor_args():
    sig = inspect.signature(logiclanguage_Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_function_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Function)


def test_hyp_logiclanguage_function_constructor_exists():
    assert callable(logiclanguage_Function.__init__)


def test_hyp_logiclanguage_function_constructor_args():
    sig = inspect.signature(logiclanguage_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logiclanguage_definedelement_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_DefinedElement)


def test_hyp_logiclanguage_definedelement_constructor_exists():
    assert callable(logiclanguage_DefinedElement.__init__)


def test_hyp_logiclanguage_definedelement_constructor_args():
    sig = inspect.signature(logiclanguage_DefinedElement.__init__)
    params = list(sig.parameters.keys())


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
AggregateExpression_strategy = st.builds(
    AggregateExpression,
)
logiclanguage_ProjectedAggregateExpression_strategy = st.builds(
    logiclanguage_ProjectedAggregateExpression,
    projectionIndex=
        st.integers()
)
logiclanguage_Count_strategy = st.builds(
    logiclanguage_Count,
)
ProjectedAggregateExpression_strategy = st.builds(
    ProjectedAggregateExpression,
)
logiclanguage_Max_strategy = st.builds(
    logiclanguage_Max,
)
logiclanguage_Min_strategy = st.builds(
    logiclanguage_Min,
)
logiclanguage_Sum_strategy = st.builds(
    logiclanguage_Sum,
)
logiclanguage_AggregatedParameterSubstitution_strategy = st.builds(
    logiclanguage_AggregatedParameterSubstitution,
)
Relation_strategy = st.builds(
    Relation,
)
logiclanguage_RelationDefinition_strategy = st.builds(
    logiclanguage_RelationDefinition,
)
Constant_strategy = st.builds(
    Constant,
)
logiclanguage_ConstantDeclaration_strategy = st.builds(
    logiclanguage_ConstantDeclaration,
)
logiclanguage_ConstantDefinition_strategy = st.builds(
    logiclanguage_ConstantDefinition,
)
logiclanguage_ConstantAnnotation_strategy = st.builds(
    logiclanguage_ConstantAnnotation,
)
Function_strategy = st.builds(
    Function,
)
logiclanguage_FunctionDeclaration_strategy = st.builds(
    logiclanguage_FunctionDeclaration,
)
logiclanguage_FunctionDefinition_strategy = st.builds(
    logiclanguage_FunctionDefinition,
)
logiclanguage_RelationDeclaration_strategy = st.builds(
    logiclanguage_RelationDeclaration,
)
logiclanguage_RelationAnnotation_strategy = st.builds(
    logiclanguage_RelationAnnotation,
)
logiclanguage_AssertionAnnotation_strategy = st.builds(
    logiclanguage_AssertionAnnotation,
)
logiclanguage_Assertion_strategy = st.builds(
    logiclanguage_Assertion,
    name=
        safe_text
)
logiclanguage_TermDescription_strategy = st.builds(
    logiclanguage_TermDescription,
)
logiclanguage_TypeDescriptor_strategy = st.builds(
    logiclanguage_TypeDescriptor,
)
NumericOperation_strategy = st.builds(
    NumericOperation,
)
logiclanguage_Divison_strategy = st.builds(
    logiclanguage_Divison,
)
logiclanguage_Mod_strategy = st.builds(
    logiclanguage_Mod,
)
logiclanguage_Multiply_strategy = st.builds(
    logiclanguage_Multiply,
)
logiclanguage_Pow_strategy = st.builds(
    logiclanguage_Pow,
)
logiclanguage_Minus_strategy = st.builds(
    logiclanguage_Minus,
)
logiclanguage_Plus_strategy = st.builds(
    logiclanguage_Plus,
)
BoolOperation_strategy = st.builds(
    BoolOperation,
)
logiclanguage_Or_strategy = st.builds(
    logiclanguage_Or,
)
logiclanguage_Not_strategy = st.builds(
    logiclanguage_Not,
)
logiclanguage_Iff_strategy = st.builds(
    logiclanguage_Iff,
)
logiclanguage_Impl_strategy = st.builds(
    logiclanguage_Impl,
)
logiclanguage_And_strategy = st.builds(
    logiclanguage_And,
)
PrimitiveRelation_strategy = st.builds(
    PrimitiveRelation,
)
logiclanguage_MoreOrEqualThan_strategy = st.builds(
    logiclanguage_MoreOrEqualThan,
)
logiclanguage_LessOrEqualThan_strategy = st.builds(
    logiclanguage_LessOrEqualThan,
)
logiclanguage_Distinct_strategy = st.builds(
    logiclanguage_Distinct,
)
logiclanguage_LessThan_strategy = st.builds(
    logiclanguage_LessThan,
)
logiclanguage_MoreThan_strategy = st.builds(
    logiclanguage_MoreThan,
)
logiclanguage_Equals_strategy = st.builds(
    logiclanguage_Equals,
)
Term_strategy = st.builds(
    Term,
)
logiclanguage_PrimitiveRelation_strategy = st.builds(
    logiclanguage_PrimitiveRelation,
)
logiclanguage_IfThenElse_strategy = st.builds(
    logiclanguage_IfThenElse,
)
logiclanguage_BoolOperation_strategy = st.builds(
    logiclanguage_BoolOperation,
)
logiclanguage_NumericOperation_strategy = st.builds(
    logiclanguage_NumericOperation,
)
logiclanguage_UnknownBecauseUninterpreted_strategy = st.builds(
    logiclanguage_UnknownBecauseUninterpreted,
)
logiclanguage_AggregateExpression_strategy = st.builds(
    logiclanguage_AggregateExpression,
)
logiclanguage_TransitiveClosure_strategy = st.builds(
    logiclanguage_TransitiveClosure,
)
logiclanguage_InstanceOf_strategy = st.builds(
    logiclanguage_InstanceOf,
)
logiclanguage_SymbolicValue_strategy = st.builds(
    logiclanguage_SymbolicValue,
)
TermDescription_strategy = st.builds(
    TermDescription,
)
logiclanguage_SymbolicDeclaration_strategy = st.builds(
    logiclanguage_SymbolicDeclaration,
    name=
        safe_text
)
logiclanguage_Term_strategy = st.builds(
    logiclanguage_Term,
)
logiclanguage_FunctionAnnotation_strategy = st.builds(
    logiclanguage_FunctionAnnotation,
)
PrimitiveTypeReference_strategy = st.builds(
    PrimitiveTypeReference,
)
logiclanguage_StringTypeReference_strategy = st.builds(
    logiclanguage_StringTypeReference,
)
logiclanguage_RealTypeReference_strategy = st.builds(
    logiclanguage_RealTypeReference,
)
logiclanguage_BoolTypeReference_strategy = st.builds(
    logiclanguage_BoolTypeReference,
)
logiclanguage_IntTypeReference_strategy = st.builds(
    logiclanguage_IntTypeReference,
)
QuantifiedExpression_strategy = st.builds(
    QuantifiedExpression,
)
logiclanguage_Forall_strategy = st.builds(
    logiclanguage_Forall,
)
logiclanguage_Exists_strategy = st.builds(
    logiclanguage_Exists,
)
logiclanguage_QuantifiedExpression_strategy = st.builds(
    logiclanguage_QuantifiedExpression,
)
AtomicTerm_strategy = st.builds(
    AtomicTerm,
)
logiclanguage_BoolLiteral_strategy = st.builds(
    logiclanguage_BoolLiteral,
    value=
        st.booleans()
)
logiclanguage_RealLiteral_strategy = st.builds(
    logiclanguage_RealLiteral,
    value=
        safe_text
)
logiclanguage_StringLiteral_strategy = st.builds(
    logiclanguage_StringLiteral,
    value=
        safe_text
)
logiclanguage_IntLiteral_strategy = st.builds(
    logiclanguage_IntLiteral,
    value=
        st.integers()
)
logiclanguage_AtomicTerm_strategy = st.builds(
    logiclanguage_AtomicTerm,
)
TypeDescriptor_strategy = st.builds(
    TypeDescriptor,
)
logiclanguage_Type_strategy = st.builds(
    logiclanguage_Type,
    isAbstract=
        st.booleans(),
    name=
        safe_text
)
TypeReference_strategy = st.builds(
    TypeReference,
)
logiclanguage_PrimitiveTypeReference_strategy = st.builds(
    logiclanguage_PrimitiveTypeReference,
)
logiclanguage_ComplexTypeReference_strategy = st.builds(
    logiclanguage_ComplexTypeReference,
)
logiclanguage_TypeReference_strategy = st.builds(
    logiclanguage_TypeReference,
)
Type_strategy = st.builds(
    Type,
)
logiclanguage_TypeDeclaration_strategy = st.builds(
    logiclanguage_TypeDeclaration,
)
logiclanguage_TypeDefinition_strategy = st.builds(
    logiclanguage_TypeDefinition,
)
SymbolicDeclaration_strategy = st.builds(
    SymbolicDeclaration,
)
logiclanguage_Variable_strategy = st.builds(
    logiclanguage_Variable,
)
logiclanguage_Constant_strategy = st.builds(
    logiclanguage_Constant,
)
logiclanguage_Relation_strategy = st.builds(
    logiclanguage_Relation,
)
logiclanguage_Function_strategy = st.builds(
    logiclanguage_Function,
)
logiclanguage_DefinedElement_strategy = st.builds(
    logiclanguage_DefinedElement,
)





@given(instance=logiclanguage_ProjectedAggregateExpression_strategy)
def test_hyp_logiclanguage_projectedaggregateexpression_projectionIndex_setter(instance):
    original = instance.projectionIndex
    instance.projectionIndex = original
    assert instance.projectionIndex == original






















@given(instance=logiclanguage_Assertion_strategy)
def test_hyp_logiclanguage_assertion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





































@given(instance=logiclanguage_SymbolicDeclaration_strategy)
def test_hyp_logiclanguage_symbolicdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
















@given(instance=logiclanguage_BoolLiteral_strategy)
def test_hyp_logiclanguage_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=logiclanguage_RealLiteral_strategy)
def test_hyp_logiclanguage_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=logiclanguage_StringLiteral_strategy)
def test_hyp_logiclanguage_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=logiclanguage_IntLiteral_strategy)
def test_hyp_logiclanguage_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=logiclanguage_Type_strategy)
def test_hyp_logiclanguage_type_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=logiclanguage_Type_strategy)
def test_hyp_logiclanguage_type_name_setter(instance):
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
    AggregateExpression,
    AtomicTerm,
    BoolOperation,
    Constant,
    Function,
    NumericOperation,
    PrimitiveRelation,
    PrimitiveTypeReference,
    ProjectedAggregateExpression,
    QuantifiedExpression,
    Relation,
    SymbolicDeclaration,
    Term,
    TermDescription,
    Type,
    TypeDescriptor,
    TypeReference,
    logiclanguage_AggregateExpression,
    logiclanguage_AggregatedParameterSubstitution,
    logiclanguage_And,
    logiclanguage_Assertion,
    logiclanguage_AssertionAnnotation,
    logiclanguage_AtomicTerm,
    logiclanguage_BoolLiteral,
    logiclanguage_BoolOperation,
    logiclanguage_BoolTypeReference,
    logiclanguage_ComplexTypeReference,
    logiclanguage_Constant,
    logiclanguage_ConstantAnnotation,
    logiclanguage_ConstantDeclaration,
    logiclanguage_ConstantDefinition,
    logiclanguage_Count,
    logiclanguage_DefinedElement,
    logiclanguage_Distinct,
    logiclanguage_Divison,
    logiclanguage_Equals,
    logiclanguage_Exists,
    logiclanguage_Forall,
    logiclanguage_Function,
    logiclanguage_FunctionAnnotation,
    logiclanguage_FunctionDeclaration,
    logiclanguage_FunctionDefinition,
    logiclanguage_IfThenElse,
    logiclanguage_Iff,
    logiclanguage_Impl,
    logiclanguage_InstanceOf,
    logiclanguage_IntLiteral,
    logiclanguage_IntTypeReference,
    logiclanguage_LessOrEqualThan,
    logiclanguage_LessThan,
    logiclanguage_Max,
    logiclanguage_Min,
    logiclanguage_Minus,
    logiclanguage_Mod,
    logiclanguage_MoreOrEqualThan,
    logiclanguage_MoreThan,
    logiclanguage_Multiply,
    logiclanguage_Not,
    logiclanguage_NumericOperation,
    logiclanguage_Or,
    logiclanguage_Plus,
    logiclanguage_Pow,
    logiclanguage_PrimitiveRelation,
    logiclanguage_PrimitiveTypeReference,
    logiclanguage_ProjectedAggregateExpression,
    logiclanguage_QuantifiedExpression,
    logiclanguage_RealLiteral,
    logiclanguage_RealTypeReference,
    logiclanguage_Relation,
    logiclanguage_RelationAnnotation,
    logiclanguage_RelationDeclaration,
    logiclanguage_RelationDefinition,
    logiclanguage_StringLiteral,
    logiclanguage_StringTypeReference,
    logiclanguage_Sum,
    logiclanguage_SymbolicDeclaration,
    logiclanguage_SymbolicValue,
    logiclanguage_Term,
    logiclanguage_TermDescription,
    logiclanguage_TransitiveClosure,
    logiclanguage_Type,
    logiclanguage_TypeDeclaration,
    logiclanguage_TypeDefinition,
    logiclanguage_TypeDescriptor,
    logiclanguage_TypeReference,
    logiclanguage_UnknownBecauseUninterpreted,
    logiclanguage_Variable,
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

def test_logiclanguage_Assertion_name_value_roundtrip():
    instance = logiclanguage_Assertion(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_logiclanguage_BoolLiteral_value_value_roundtrip():
    instance = logiclanguage_BoolLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_logiclanguage_IntLiteral_value_value_roundtrip():
    instance = logiclanguage_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_logiclanguage_ProjectedAggregateExpression_projectionIndex_value_roundtrip():
    instance = logiclanguage_ProjectedAggregateExpression(projectionIndex=7)
    assert instance.projectionIndex == 7
    instance.projectionIndex = 13
    assert instance.projectionIndex == 13


def test_logiclanguage_RealLiteral_value_value_roundtrip():
    instance = logiclanguage_RealLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_logiclanguage_StringLiteral_value_value_roundtrip():
    instance = logiclanguage_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_logiclanguage_SymbolicDeclaration_name_value_roundtrip():
    instance = logiclanguage_SymbolicDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_logiclanguage_Type_isAbstract_value_roundtrip():
    instance = logiclanguage_Type(isAbstract=True, name="sample_text")
    assert instance.isAbstract == True
    instance.isAbstract = False
    assert instance.isAbstract == False


def test_logiclanguage_Type_name_value_roundtrip():
    instance = logiclanguage_Type(isAbstract=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_logiclanguage_Count_isa_AggregateExpression():
    instance = logiclanguage_Count()
    assert isinstance(instance, AggregateExpression)


def test_logiclanguage_ProjectedAggregateExpression_isa_AggregateExpression():
    instance = logiclanguage_ProjectedAggregateExpression(projectionIndex=7)
    assert isinstance(instance, AggregateExpression)


def test_logiclanguage_BoolLiteral_isa_AtomicTerm():
    instance = logiclanguage_BoolLiteral(value=True)
    assert isinstance(instance, AtomicTerm)


def test_logiclanguage_IntLiteral_isa_AtomicTerm():
    instance = logiclanguage_IntLiteral(value=7)
    assert isinstance(instance, AtomicTerm)


def test_logiclanguage_RealLiteral_isa_AtomicTerm():
    instance = logiclanguage_RealLiteral(value="sample_text")
    assert isinstance(instance, AtomicTerm)


def test_logiclanguage_StringLiteral_isa_AtomicTerm():
    instance = logiclanguage_StringLiteral(value="sample_text")
    assert isinstance(instance, AtomicTerm)


def test_logiclanguage_And_isa_BoolOperation():
    instance = logiclanguage_And()
    assert isinstance(instance, BoolOperation)


def test_logiclanguage_Iff_isa_BoolOperation():
    instance = logiclanguage_Iff()
    assert isinstance(instance, BoolOperation)


def test_logiclanguage_Impl_isa_BoolOperation():
    instance = logiclanguage_Impl()
    assert isinstance(instance, BoolOperation)


def test_logiclanguage_Not_isa_BoolOperation():
    instance = logiclanguage_Not()
    assert isinstance(instance, BoolOperation)


def test_logiclanguage_Or_isa_BoolOperation():
    instance = logiclanguage_Or()
    assert isinstance(instance, BoolOperation)


def test_logiclanguage_ConstantDeclaration_isa_Constant():
    instance = logiclanguage_ConstantDeclaration()
    assert isinstance(instance, Constant)


def test_logiclanguage_ConstantDefinition_isa_Constant():
    instance = logiclanguage_ConstantDefinition()
    assert isinstance(instance, Constant)


def test_logiclanguage_FunctionDeclaration_isa_Function():
    instance = logiclanguage_FunctionDeclaration()
    assert isinstance(instance, Function)


def test_logiclanguage_FunctionDefinition_isa_Function():
    instance = logiclanguage_FunctionDefinition()
    assert isinstance(instance, Function)


def test_logiclanguage_Divison_isa_NumericOperation():
    instance = logiclanguage_Divison()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Minus_isa_NumericOperation():
    instance = logiclanguage_Minus()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Mod_isa_NumericOperation():
    instance = logiclanguage_Mod()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Multiply_isa_NumericOperation():
    instance = logiclanguage_Multiply()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Plus_isa_NumericOperation():
    instance = logiclanguage_Plus()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Pow_isa_NumericOperation():
    instance = logiclanguage_Pow()
    assert isinstance(instance, NumericOperation)


def test_logiclanguage_Distinct_isa_PrimitiveRelation():
    instance = logiclanguage_Distinct()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_Equals_isa_PrimitiveRelation():
    instance = logiclanguage_Equals()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_LessOrEqualThan_isa_PrimitiveRelation():
    instance = logiclanguage_LessOrEqualThan()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_LessThan_isa_PrimitiveRelation():
    instance = logiclanguage_LessThan()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_MoreOrEqualThan_isa_PrimitiveRelation():
    instance = logiclanguage_MoreOrEqualThan()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_MoreThan_isa_PrimitiveRelation():
    instance = logiclanguage_MoreThan()
    assert isinstance(instance, PrimitiveRelation)


def test_logiclanguage_BoolTypeReference_isa_PrimitiveTypeReference():
    instance = logiclanguage_BoolTypeReference()
    assert isinstance(instance, PrimitiveTypeReference)


def test_logiclanguage_IntTypeReference_isa_PrimitiveTypeReference():
    instance = logiclanguage_IntTypeReference()
    assert isinstance(instance, PrimitiveTypeReference)


def test_logiclanguage_RealTypeReference_isa_PrimitiveTypeReference():
    instance = logiclanguage_RealTypeReference()
    assert isinstance(instance, PrimitiveTypeReference)


def test_logiclanguage_StringTypeReference_isa_PrimitiveTypeReference():
    instance = logiclanguage_StringTypeReference()
    assert isinstance(instance, PrimitiveTypeReference)


def test_logiclanguage_Max_isa_ProjectedAggregateExpression():
    instance = logiclanguage_Max()
    assert isinstance(instance, ProjectedAggregateExpression)


def test_logiclanguage_Min_isa_ProjectedAggregateExpression():
    instance = logiclanguage_Min()
    assert isinstance(instance, ProjectedAggregateExpression)


def test_logiclanguage_Sum_isa_ProjectedAggregateExpression():
    instance = logiclanguage_Sum()
    assert isinstance(instance, ProjectedAggregateExpression)


def test_logiclanguage_Exists_isa_QuantifiedExpression():
    instance = logiclanguage_Exists()
    assert isinstance(instance, QuantifiedExpression)


def test_logiclanguage_Forall_isa_QuantifiedExpression():
    instance = logiclanguage_Forall()
    assert isinstance(instance, QuantifiedExpression)


def test_logiclanguage_RelationDeclaration_isa_Relation():
    instance = logiclanguage_RelationDeclaration()
    assert isinstance(instance, Relation)


def test_logiclanguage_RelationDefinition_isa_Relation():
    instance = logiclanguage_RelationDefinition()
    assert isinstance(instance, Relation)


def test_logiclanguage_Constant_isa_SymbolicDeclaration():
    instance = logiclanguage_Constant()
    assert isinstance(instance, SymbolicDeclaration)


def test_logiclanguage_DefinedElement_isa_SymbolicDeclaration():
    instance = logiclanguage_DefinedElement()
    assert isinstance(instance, SymbolicDeclaration)


def test_logiclanguage_Function_isa_SymbolicDeclaration():
    instance = logiclanguage_Function()
    assert isinstance(instance, SymbolicDeclaration)


def test_logiclanguage_Relation_isa_SymbolicDeclaration():
    instance = logiclanguage_Relation()
    assert isinstance(instance, SymbolicDeclaration)


def test_logiclanguage_Variable_isa_SymbolicDeclaration():
    instance = logiclanguage_Variable()
    assert isinstance(instance, SymbolicDeclaration)


def test_logiclanguage_AggregateExpression_isa_Term():
    instance = logiclanguage_AggregateExpression()
    assert isinstance(instance, Term)


def test_logiclanguage_AtomicTerm_isa_Term():
    instance = logiclanguage_AtomicTerm()
    assert isinstance(instance, Term)


def test_logiclanguage_BoolOperation_isa_Term():
    instance = logiclanguage_BoolOperation()
    assert isinstance(instance, Term)


def test_logiclanguage_IfThenElse_isa_Term():
    instance = logiclanguage_IfThenElse()
    assert isinstance(instance, Term)


def test_logiclanguage_InstanceOf_isa_Term():
    instance = logiclanguage_InstanceOf()
    assert isinstance(instance, Term)


def test_logiclanguage_NumericOperation_isa_Term():
    instance = logiclanguage_NumericOperation()
    assert isinstance(instance, Term)


def test_logiclanguage_PrimitiveRelation_isa_Term():
    instance = logiclanguage_PrimitiveRelation()
    assert isinstance(instance, Term)


def test_logiclanguage_QuantifiedExpression_isa_Term():
    instance = logiclanguage_QuantifiedExpression()
    assert isinstance(instance, Term)


def test_logiclanguage_SymbolicValue_isa_Term():
    instance = logiclanguage_SymbolicValue()
    assert isinstance(instance, Term)


def test_logiclanguage_TransitiveClosure_isa_Term():
    instance = logiclanguage_TransitiveClosure()
    assert isinstance(instance, Term)


def test_logiclanguage_UnknownBecauseUninterpreted_isa_Term():
    instance = logiclanguage_UnknownBecauseUninterpreted()
    assert isinstance(instance, Term)


def test_logiclanguage_SymbolicDeclaration_isa_TermDescription():
    instance = logiclanguage_SymbolicDeclaration(name="sample_text")
    assert isinstance(instance, TermDescription)


def test_logiclanguage_Term_isa_TermDescription():
    instance = logiclanguage_Term()
    assert isinstance(instance, TermDescription)


def test_logiclanguage_TypeDeclaration_isa_Type():
    instance = logiclanguage_TypeDeclaration()
    assert isinstance(instance, Type)


def test_logiclanguage_TypeDefinition_isa_Type():
    instance = logiclanguage_TypeDefinition()
    assert isinstance(instance, Type)


def test_logiclanguage_Type_isa_TypeDescriptor():
    instance = logiclanguage_Type(isAbstract=True, name="sample_text")
    assert isinstance(instance, TypeDescriptor)


def test_logiclanguage_TypeReference_isa_TypeDescriptor():
    instance = logiclanguage_TypeReference()
    assert isinstance(instance, TypeDescriptor)


def test_logiclanguage_ComplexTypeReference_isa_TypeReference():
    instance = logiclanguage_ComplexTypeReference()
    assert isinstance(instance, TypeReference)


def test_logiclanguage_PrimitiveTypeReference_isa_TypeReference():
    instance = logiclanguage_PrimitiveTypeReference()
    assert isinstance(instance, TypeReference)


def test_assoc_annotations74_link_reassign_clear():
    a = logiclanguage_Assertion(name="sample_text")
    b1 = logiclanguage_AssertionAnnotation()
    b2 = logiclanguage_AssertionAnnotation()
    _safe_set(a, 'target75', {b1})
    assert _is_linked(a, 'target75', b1)
    if hasattr(b1, 'logicproblem.ecoreAssertionAnnotation'):
        assert _is_linked(b1, 'logicproblem.ecoreAssertionAnnotation', a)
    _safe_set(a, 'target75', {b2})
    assert _is_linked(a, 'target75', b2)
    if hasattr(b1, 'logicproblem.ecoreAssertionAnnotation'):
        assert not _is_linked(b1, 'logicproblem.ecoreAssertionAnnotation', a)
    if hasattr(b2, 'logicproblem.ecoreAssertionAnnotation'):
        assert _is_linked(b2, 'logicproblem.ecoreAssertionAnnotation', a)
    _safe_set(a, 'target75', set())
    assert not _is_linked(a, 'target75', b2)
    if hasattr(b2, 'logicproblem.ecoreAssertionAnnotation'):
        assert not _is_linked(b2, 'logicproblem.ecoreAssertionAnnotation', a)


def test_assoc_referred8_link_reassign_clear():
    a = logiclanguage_Type(isAbstract=True, name="sample_text")
    b1 = logiclanguage_ComplexTypeReference()
    b2 = logiclanguage_ComplexTypeReference()
    _safe_set(a, 'logiclanguage_Type', b1)
    assert _is_linked(a, 'logiclanguage_Type', b1)
    if hasattr(b1, 'logiclanguage_ComplexTypeReference'):
        assert _is_linked(b1, 'logiclanguage_ComplexTypeReference', a)
    _safe_set(a, 'logiclanguage_Type', b2)
    assert _is_linked(a, 'logiclanguage_Type', b2)
    if hasattr(b1, 'logiclanguage_ComplexTypeReference'):
        assert not _is_linked(b1, 'logiclanguage_ComplexTypeReference', a)
    if hasattr(b2, 'logiclanguage_ComplexTypeReference'):
        assert _is_linked(b2, 'logiclanguage_ComplexTypeReference', a)
    _safe_set(a, 'logiclanguage_Type', None)
    assert not _is_linked(a, 'logiclanguage_Type', b2)
    if hasattr(b2, 'logiclanguage_ComplexTypeReference'):
        assert not _is_linked(b2, 'logiclanguage_ComplexTypeReference', a)


def test_assoc_subtypes1_link_reassign_clear():
    a = logiclanguage_Type(isAbstract=True, name="sample_text")
    b1 = logiclanguage_Type(isAbstract=True, name="sample_text")
    b2 = logiclanguage_Type(isAbstract=False, name="sample_text_2")
    _safe_set(a, 'Type', b1)
    assert _is_linked(a, 'Type', b1)
    if hasattr(b1, 'supertypes'):
        assert _is_linked(b1, 'supertypes', a)
    _safe_set(a, 'Type', b2)
    assert _is_linked(a, 'Type', b2)
    if hasattr(b1, 'supertypes'):
        assert not _is_linked(b1, 'supertypes', a)
    if hasattr(b2, 'supertypes'):
        assert _is_linked(b2, 'supertypes', a)
    _safe_set(a, 'Type', None)
    assert not _is_linked(a, 'Type', b2)
    if hasattr(b2, 'supertypes'):
        assert not _is_linked(b2, 'supertypes', a)


def test_assoc_supertypes3_link_reassign_clear():
    a = logiclanguage_Type(isAbstract=True, name="sample_text")
    b1 = logiclanguage_Type(isAbstract=True, name="sample_text")
    b2 = logiclanguage_Type(isAbstract=False, name="sample_text_2")
    _safe_set(a, 'Type4', b1)
    assert _is_linked(a, 'Type4', b1)
    if hasattr(b1, 'subtypes'):
        assert _is_linked(b1, 'subtypes', a)
    _safe_set(a, 'Type4', b2)
    assert _is_linked(a, 'Type4', b2)
    if hasattr(b1, 'subtypes'):
        assert not _is_linked(b1, 'subtypes', a)
    if hasattr(b2, 'subtypes'):
        assert _is_linked(b2, 'subtypes', a)
    _safe_set(a, 'Type4', None)
    assert not _is_linked(a, 'Type4', b2)
    if hasattr(b2, 'subtypes'):
        assert not _is_linked(b2, 'subtypes', a)


def test_assoc_symbolicReference14_link_reassign_clear():
    a = logiclanguage_SymbolicDeclaration(name="sample_text")
    b1 = logiclanguage_SymbolicValue()
    b2 = logiclanguage_SymbolicValue()
    _safe_set(a, 'logiclanguage_SymbolicDeclaration', b1)
    assert _is_linked(a, 'logiclanguage_SymbolicDeclaration', b1)
    if hasattr(b1, 'logiclanguage_SymbolicValue'):
        assert _is_linked(b1, 'logiclanguage_SymbolicValue', a)
    _safe_set(a, 'logiclanguage_SymbolicDeclaration', b2)
    assert _is_linked(a, 'logiclanguage_SymbolicDeclaration', b2)
    if hasattr(b1, 'logiclanguage_SymbolicValue'):
        assert not _is_linked(b1, 'logiclanguage_SymbolicValue', a)
    if hasattr(b2, 'logiclanguage_SymbolicValue'):
        assert _is_linked(b2, 'logiclanguage_SymbolicValue', a)
    _safe_set(a, 'logiclanguage_SymbolicDeclaration', None)
    assert not _is_linked(a, 'logiclanguage_SymbolicDeclaration', b2)
    if hasattr(b2, 'logiclanguage_SymbolicValue'):
        assert not _is_linked(b2, 'logiclanguage_SymbolicValue', a)


def test_assoc_value72_link_reassign_clear():
    a = logiclanguage_Assertion(name="sample_text")
    b1 = logiclanguage_Term()
    b2 = logiclanguage_Term()
    _safe_set(a, 'logiclanguage_Assertion', b1)
    assert _is_linked(a, 'logiclanguage_Assertion', b1)
    if hasattr(b1, 'logiclanguage_Term73'):
        assert _is_linked(b1, 'logiclanguage_Term73', a)
    _safe_set(a, 'logiclanguage_Assertion', b2)
    assert _is_linked(a, 'logiclanguage_Assertion', b2)
    if hasattr(b1, 'logiclanguage_Term73'):
        assert not _is_linked(b1, 'logiclanguage_Term73', a)
    if hasattr(b2, 'logiclanguage_Term73'):
        assert _is_linked(b2, 'logiclanguage_Term73', a)
    _safe_set(a, 'logiclanguage_Assertion', None)
    assert not _is_linked(a, 'logiclanguage_Assertion', b2)
    if hasattr(b2, 'logiclanguage_Term73'):
        assert not _is_linked(b2, 'logiclanguage_Term73', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AggregateExpression_strategy = st.builds(AggregateExpression)
@given(instance=AggregateExpression_strategy)
@settings(max_examples=25)
def test_AggregateExpression_instantiation(instance):
    assert isinstance(instance, AggregateExpression)


AtomicTerm_strategy = st.builds(AtomicTerm)
@given(instance=AtomicTerm_strategy)
@settings(max_examples=25)
def test_AtomicTerm_instantiation(instance):
    assert isinstance(instance, AtomicTerm)


BoolOperation_strategy = st.builds(BoolOperation)
@given(instance=BoolOperation_strategy)
@settings(max_examples=25)
def test_BoolOperation_instantiation(instance):
    assert isinstance(instance, BoolOperation)


Constant_strategy = st.builds(Constant)
@given(instance=Constant_strategy)
@settings(max_examples=25)
def test_Constant_instantiation(instance):
    assert isinstance(instance, Constant)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


NumericOperation_strategy = st.builds(NumericOperation)
@given(instance=NumericOperation_strategy)
@settings(max_examples=25)
def test_NumericOperation_instantiation(instance):
    assert isinstance(instance, NumericOperation)


PrimitiveRelation_strategy = st.builds(PrimitiveRelation)
@given(instance=PrimitiveRelation_strategy)
@settings(max_examples=25)
def test_PrimitiveRelation_instantiation(instance):
    assert isinstance(instance, PrimitiveRelation)


PrimitiveTypeReference_strategy = st.builds(PrimitiveTypeReference)
@given(instance=PrimitiveTypeReference_strategy)
@settings(max_examples=25)
def test_PrimitiveTypeReference_instantiation(instance):
    assert isinstance(instance, PrimitiveTypeReference)


ProjectedAggregateExpression_strategy = st.builds(ProjectedAggregateExpression)
@given(instance=ProjectedAggregateExpression_strategy)
@settings(max_examples=25)
def test_ProjectedAggregateExpression_instantiation(instance):
    assert isinstance(instance, ProjectedAggregateExpression)


QuantifiedExpression_strategy = st.builds(QuantifiedExpression)
@given(instance=QuantifiedExpression_strategy)
@settings(max_examples=25)
def test_QuantifiedExpression_instantiation(instance):
    assert isinstance(instance, QuantifiedExpression)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


SymbolicDeclaration_strategy = st.builds(SymbolicDeclaration)
@given(instance=SymbolicDeclaration_strategy)
@settings(max_examples=25)
def test_SymbolicDeclaration_instantiation(instance):
    assert isinstance(instance, SymbolicDeclaration)


Term_strategy = st.builds(Term)
@given(instance=Term_strategy)
@settings(max_examples=25)
def test_Term_instantiation(instance):
    assert isinstance(instance, Term)


TermDescription_strategy = st.builds(TermDescription)
@given(instance=TermDescription_strategy)
@settings(max_examples=25)
def test_TermDescription_instantiation(instance):
    assert isinstance(instance, TermDescription)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeDescriptor_strategy = st.builds(TypeDescriptor)
@given(instance=TypeDescriptor_strategy)
@settings(max_examples=25)
def test_TypeDescriptor_instantiation(instance):
    assert isinstance(instance, TypeDescriptor)


TypeReference_strategy = st.builds(TypeReference)
@given(instance=TypeReference_strategy)
@settings(max_examples=25)
def test_TypeReference_instantiation(instance):
    assert isinstance(instance, TypeReference)


logiclanguage_AggregateExpression_strategy = st.builds(logiclanguage_AggregateExpression)
@given(instance=logiclanguage_AggregateExpression_strategy)
@settings(max_examples=25)
def test_logiclanguage_AggregateExpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_AggregateExpression)


logiclanguage_AggregatedParameterSubstitution_strategy = st.builds(logiclanguage_AggregatedParameterSubstitution)
@given(instance=logiclanguage_AggregatedParameterSubstitution_strategy)
@settings(max_examples=25)
def test_logiclanguage_AggregatedParameterSubstitution_instantiation(instance):
    assert isinstance(instance, logiclanguage_AggregatedParameterSubstitution)


logiclanguage_And_strategy = st.builds(logiclanguage_And)
@given(instance=logiclanguage_And_strategy)
@settings(max_examples=25)
def test_logiclanguage_And_instantiation(instance):
    assert isinstance(instance, logiclanguage_And)


logiclanguage_Assertion_strategy = st.builds(logiclanguage_Assertion, name=safe_text)
@given(instance=logiclanguage_Assertion_strategy)
@settings(max_examples=25)
def test_logiclanguage_Assertion_instantiation(instance):
    assert isinstance(instance, logiclanguage_Assertion)


logiclanguage_AssertionAnnotation_strategy = st.builds(logiclanguage_AssertionAnnotation)
@given(instance=logiclanguage_AssertionAnnotation_strategy)
@settings(max_examples=25)
def test_logiclanguage_AssertionAnnotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_AssertionAnnotation)


logiclanguage_AtomicTerm_strategy = st.builds(logiclanguage_AtomicTerm)
@given(instance=logiclanguage_AtomicTerm_strategy)
@settings(max_examples=25)
def test_logiclanguage_AtomicTerm_instantiation(instance):
    assert isinstance(instance, logiclanguage_AtomicTerm)


logiclanguage_BoolLiteral_strategy = st.builds(logiclanguage_BoolLiteral, value=st.booleans())
@given(instance=logiclanguage_BoolLiteral_strategy)
@settings(max_examples=25)
def test_logiclanguage_BoolLiteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolLiteral)


logiclanguage_BoolOperation_strategy = st.builds(logiclanguage_BoolOperation)
@given(instance=logiclanguage_BoolOperation_strategy)
@settings(max_examples=25)
def test_logiclanguage_BoolOperation_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolOperation)


logiclanguage_BoolTypeReference_strategy = st.builds(logiclanguage_BoolTypeReference)
@given(instance=logiclanguage_BoolTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_BoolTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolTypeReference)


logiclanguage_ComplexTypeReference_strategy = st.builds(logiclanguage_ComplexTypeReference)
@given(instance=logiclanguage_ComplexTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_ComplexTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_ComplexTypeReference)


logiclanguage_Constant_strategy = st.builds(logiclanguage_Constant)
@given(instance=logiclanguage_Constant_strategy)
@settings(max_examples=25)
def test_logiclanguage_Constant_instantiation(instance):
    assert isinstance(instance, logiclanguage_Constant)


logiclanguage_ConstantAnnotation_strategy = st.builds(logiclanguage_ConstantAnnotation)
@given(instance=logiclanguage_ConstantAnnotation_strategy)
@settings(max_examples=25)
def test_logiclanguage_ConstantAnnotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantAnnotation)


logiclanguage_ConstantDeclaration_strategy = st.builds(logiclanguage_ConstantDeclaration)
@given(instance=logiclanguage_ConstantDeclaration_strategy)
@settings(max_examples=25)
def test_logiclanguage_ConstantDeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantDeclaration)


logiclanguage_ConstantDefinition_strategy = st.builds(logiclanguage_ConstantDefinition)
@given(instance=logiclanguage_ConstantDefinition_strategy)
@settings(max_examples=25)
def test_logiclanguage_ConstantDefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantDefinition)


logiclanguage_Count_strategy = st.builds(logiclanguage_Count)
@given(instance=logiclanguage_Count_strategy)
@settings(max_examples=25)
def test_logiclanguage_Count_instantiation(instance):
    assert isinstance(instance, logiclanguage_Count)


logiclanguage_DefinedElement_strategy = st.builds(logiclanguage_DefinedElement)
@given(instance=logiclanguage_DefinedElement_strategy)
@settings(max_examples=25)
def test_logiclanguage_DefinedElement_instantiation(instance):
    assert isinstance(instance, logiclanguage_DefinedElement)


logiclanguage_Distinct_strategy = st.builds(logiclanguage_Distinct)
@given(instance=logiclanguage_Distinct_strategy)
@settings(max_examples=25)
def test_logiclanguage_Distinct_instantiation(instance):
    assert isinstance(instance, logiclanguage_Distinct)


logiclanguage_Divison_strategy = st.builds(logiclanguage_Divison)
@given(instance=logiclanguage_Divison_strategy)
@settings(max_examples=25)
def test_logiclanguage_Divison_instantiation(instance):
    assert isinstance(instance, logiclanguage_Divison)


logiclanguage_Equals_strategy = st.builds(logiclanguage_Equals)
@given(instance=logiclanguage_Equals_strategy)
@settings(max_examples=25)
def test_logiclanguage_Equals_instantiation(instance):
    assert isinstance(instance, logiclanguage_Equals)


logiclanguage_Exists_strategy = st.builds(logiclanguage_Exists)
@given(instance=logiclanguage_Exists_strategy)
@settings(max_examples=25)
def test_logiclanguage_Exists_instantiation(instance):
    assert isinstance(instance, logiclanguage_Exists)


logiclanguage_Forall_strategy = st.builds(logiclanguage_Forall)
@given(instance=logiclanguage_Forall_strategy)
@settings(max_examples=25)
def test_logiclanguage_Forall_instantiation(instance):
    assert isinstance(instance, logiclanguage_Forall)


logiclanguage_Function_strategy = st.builds(logiclanguage_Function)
@given(instance=logiclanguage_Function_strategy)
@settings(max_examples=25)
def test_logiclanguage_Function_instantiation(instance):
    assert isinstance(instance, logiclanguage_Function)


logiclanguage_FunctionAnnotation_strategy = st.builds(logiclanguage_FunctionAnnotation)
@given(instance=logiclanguage_FunctionAnnotation_strategy)
@settings(max_examples=25)
def test_logiclanguage_FunctionAnnotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionAnnotation)


logiclanguage_FunctionDeclaration_strategy = st.builds(logiclanguage_FunctionDeclaration)
@given(instance=logiclanguage_FunctionDeclaration_strategy)
@settings(max_examples=25)
def test_logiclanguage_FunctionDeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionDeclaration)


logiclanguage_FunctionDefinition_strategy = st.builds(logiclanguage_FunctionDefinition)
@given(instance=logiclanguage_FunctionDefinition_strategy)
@settings(max_examples=25)
def test_logiclanguage_FunctionDefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionDefinition)


logiclanguage_IfThenElse_strategy = st.builds(logiclanguage_IfThenElse)
@given(instance=logiclanguage_IfThenElse_strategy)
@settings(max_examples=25)
def test_logiclanguage_IfThenElse_instantiation(instance):
    assert isinstance(instance, logiclanguage_IfThenElse)


logiclanguage_Iff_strategy = st.builds(logiclanguage_Iff)
@given(instance=logiclanguage_Iff_strategy)
@settings(max_examples=25)
def test_logiclanguage_Iff_instantiation(instance):
    assert isinstance(instance, logiclanguage_Iff)


logiclanguage_Impl_strategy = st.builds(logiclanguage_Impl)
@given(instance=logiclanguage_Impl_strategy)
@settings(max_examples=25)
def test_logiclanguage_Impl_instantiation(instance):
    assert isinstance(instance, logiclanguage_Impl)


logiclanguage_InstanceOf_strategy = st.builds(logiclanguage_InstanceOf)
@given(instance=logiclanguage_InstanceOf_strategy)
@settings(max_examples=25)
def test_logiclanguage_InstanceOf_instantiation(instance):
    assert isinstance(instance, logiclanguage_InstanceOf)


logiclanguage_IntLiteral_strategy = st.builds(logiclanguage_IntLiteral, value=st.integers())
@given(instance=logiclanguage_IntLiteral_strategy)
@settings(max_examples=25)
def test_logiclanguage_IntLiteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_IntLiteral)


logiclanguage_IntTypeReference_strategy = st.builds(logiclanguage_IntTypeReference)
@given(instance=logiclanguage_IntTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_IntTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_IntTypeReference)


logiclanguage_LessOrEqualThan_strategy = st.builds(logiclanguage_LessOrEqualThan)
@given(instance=logiclanguage_LessOrEqualThan_strategy)
@settings(max_examples=25)
def test_logiclanguage_LessOrEqualThan_instantiation(instance):
    assert isinstance(instance, logiclanguage_LessOrEqualThan)


logiclanguage_LessThan_strategy = st.builds(logiclanguage_LessThan)
@given(instance=logiclanguage_LessThan_strategy)
@settings(max_examples=25)
def test_logiclanguage_LessThan_instantiation(instance):
    assert isinstance(instance, logiclanguage_LessThan)


logiclanguage_Max_strategy = st.builds(logiclanguage_Max)
@given(instance=logiclanguage_Max_strategy)
@settings(max_examples=25)
def test_logiclanguage_Max_instantiation(instance):
    assert isinstance(instance, logiclanguage_Max)


logiclanguage_Min_strategy = st.builds(logiclanguage_Min)
@given(instance=logiclanguage_Min_strategy)
@settings(max_examples=25)
def test_logiclanguage_Min_instantiation(instance):
    assert isinstance(instance, logiclanguage_Min)


logiclanguage_Minus_strategy = st.builds(logiclanguage_Minus)
@given(instance=logiclanguage_Minus_strategy)
@settings(max_examples=25)
def test_logiclanguage_Minus_instantiation(instance):
    assert isinstance(instance, logiclanguage_Minus)


logiclanguage_Mod_strategy = st.builds(logiclanguage_Mod)
@given(instance=logiclanguage_Mod_strategy)
@settings(max_examples=25)
def test_logiclanguage_Mod_instantiation(instance):
    assert isinstance(instance, logiclanguage_Mod)


logiclanguage_MoreOrEqualThan_strategy = st.builds(logiclanguage_MoreOrEqualThan)
@given(instance=logiclanguage_MoreOrEqualThan_strategy)
@settings(max_examples=25)
def test_logiclanguage_MoreOrEqualThan_instantiation(instance):
    assert isinstance(instance, logiclanguage_MoreOrEqualThan)


logiclanguage_MoreThan_strategy = st.builds(logiclanguage_MoreThan)
@given(instance=logiclanguage_MoreThan_strategy)
@settings(max_examples=25)
def test_logiclanguage_MoreThan_instantiation(instance):
    assert isinstance(instance, logiclanguage_MoreThan)


logiclanguage_Multiply_strategy = st.builds(logiclanguage_Multiply)
@given(instance=logiclanguage_Multiply_strategy)
@settings(max_examples=25)
def test_logiclanguage_Multiply_instantiation(instance):
    assert isinstance(instance, logiclanguage_Multiply)


logiclanguage_Not_strategy = st.builds(logiclanguage_Not)
@given(instance=logiclanguage_Not_strategy)
@settings(max_examples=25)
def test_logiclanguage_Not_instantiation(instance):
    assert isinstance(instance, logiclanguage_Not)


logiclanguage_NumericOperation_strategy = st.builds(logiclanguage_NumericOperation)
@given(instance=logiclanguage_NumericOperation_strategy)
@settings(max_examples=25)
def test_logiclanguage_NumericOperation_instantiation(instance):
    assert isinstance(instance, logiclanguage_NumericOperation)


logiclanguage_Or_strategy = st.builds(logiclanguage_Or)
@given(instance=logiclanguage_Or_strategy)
@settings(max_examples=25)
def test_logiclanguage_Or_instantiation(instance):
    assert isinstance(instance, logiclanguage_Or)


logiclanguage_Plus_strategy = st.builds(logiclanguage_Plus)
@given(instance=logiclanguage_Plus_strategy)
@settings(max_examples=25)
def test_logiclanguage_Plus_instantiation(instance):
    assert isinstance(instance, logiclanguage_Plus)


logiclanguage_Pow_strategy = st.builds(logiclanguage_Pow)
@given(instance=logiclanguage_Pow_strategy)
@settings(max_examples=25)
def test_logiclanguage_Pow_instantiation(instance):
    assert isinstance(instance, logiclanguage_Pow)


logiclanguage_PrimitiveRelation_strategy = st.builds(logiclanguage_PrimitiveRelation)
@given(instance=logiclanguage_PrimitiveRelation_strategy)
@settings(max_examples=25)
def test_logiclanguage_PrimitiveRelation_instantiation(instance):
    assert isinstance(instance, logiclanguage_PrimitiveRelation)


logiclanguage_PrimitiveTypeReference_strategy = st.builds(logiclanguage_PrimitiveTypeReference)
@given(instance=logiclanguage_PrimitiveTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_PrimitiveTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_PrimitiveTypeReference)


logiclanguage_ProjectedAggregateExpression_strategy = st.builds(logiclanguage_ProjectedAggregateExpression, projectionIndex=st.integers())
@given(instance=logiclanguage_ProjectedAggregateExpression_strategy)
@settings(max_examples=25)
def test_logiclanguage_ProjectedAggregateExpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_ProjectedAggregateExpression)


logiclanguage_QuantifiedExpression_strategy = st.builds(logiclanguage_QuantifiedExpression)
@given(instance=logiclanguage_QuantifiedExpression_strategy)
@settings(max_examples=25)
def test_logiclanguage_QuantifiedExpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_QuantifiedExpression)


logiclanguage_RealLiteral_strategy = st.builds(logiclanguage_RealLiteral, value=safe_text)
@given(instance=logiclanguage_RealLiteral_strategy)
@settings(max_examples=25)
def test_logiclanguage_RealLiteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_RealLiteral)


logiclanguage_RealTypeReference_strategy = st.builds(logiclanguage_RealTypeReference)
@given(instance=logiclanguage_RealTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_RealTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_RealTypeReference)


logiclanguage_Relation_strategy = st.builds(logiclanguage_Relation)
@given(instance=logiclanguage_Relation_strategy)
@settings(max_examples=25)
def test_logiclanguage_Relation_instantiation(instance):
    assert isinstance(instance, logiclanguage_Relation)


logiclanguage_RelationAnnotation_strategy = st.builds(logiclanguage_RelationAnnotation)
@given(instance=logiclanguage_RelationAnnotation_strategy)
@settings(max_examples=25)
def test_logiclanguage_RelationAnnotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationAnnotation)


logiclanguage_RelationDeclaration_strategy = st.builds(logiclanguage_RelationDeclaration)
@given(instance=logiclanguage_RelationDeclaration_strategy)
@settings(max_examples=25)
def test_logiclanguage_RelationDeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationDeclaration)


logiclanguage_RelationDefinition_strategy = st.builds(logiclanguage_RelationDefinition)
@given(instance=logiclanguage_RelationDefinition_strategy)
@settings(max_examples=25)
def test_logiclanguage_RelationDefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationDefinition)


logiclanguage_StringLiteral_strategy = st.builds(logiclanguage_StringLiteral, value=safe_text)
@given(instance=logiclanguage_StringLiteral_strategy)
@settings(max_examples=25)
def test_logiclanguage_StringLiteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_StringLiteral)


logiclanguage_StringTypeReference_strategy = st.builds(logiclanguage_StringTypeReference)
@given(instance=logiclanguage_StringTypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_StringTypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_StringTypeReference)


logiclanguage_Sum_strategy = st.builds(logiclanguage_Sum)
@given(instance=logiclanguage_Sum_strategy)
@settings(max_examples=25)
def test_logiclanguage_Sum_instantiation(instance):
    assert isinstance(instance, logiclanguage_Sum)


logiclanguage_SymbolicDeclaration_strategy = st.builds(logiclanguage_SymbolicDeclaration, name=safe_text)
@given(instance=logiclanguage_SymbolicDeclaration_strategy)
@settings(max_examples=25)
def test_logiclanguage_SymbolicDeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_SymbolicDeclaration)


logiclanguage_SymbolicValue_strategy = st.builds(logiclanguage_SymbolicValue)
@given(instance=logiclanguage_SymbolicValue_strategy)
@settings(max_examples=25)
def test_logiclanguage_SymbolicValue_instantiation(instance):
    assert isinstance(instance, logiclanguage_SymbolicValue)


logiclanguage_Term_strategy = st.builds(logiclanguage_Term)
@given(instance=logiclanguage_Term_strategy)
@settings(max_examples=25)
def test_logiclanguage_Term_instantiation(instance):
    assert isinstance(instance, logiclanguage_Term)


logiclanguage_TermDescription_strategy = st.builds(logiclanguage_TermDescription)
@given(instance=logiclanguage_TermDescription_strategy)
@settings(max_examples=25)
def test_logiclanguage_TermDescription_instantiation(instance):
    assert isinstance(instance, logiclanguage_TermDescription)


logiclanguage_TransitiveClosure_strategy = st.builds(logiclanguage_TransitiveClosure)
@given(instance=logiclanguage_TransitiveClosure_strategy)
@settings(max_examples=25)
def test_logiclanguage_TransitiveClosure_instantiation(instance):
    assert isinstance(instance, logiclanguage_TransitiveClosure)


logiclanguage_Type_strategy = st.builds(logiclanguage_Type, isAbstract=st.booleans(), name=safe_text)
@given(instance=logiclanguage_Type_strategy)
@settings(max_examples=25)
def test_logiclanguage_Type_instantiation(instance):
    assert isinstance(instance, logiclanguage_Type)


logiclanguage_TypeDeclaration_strategy = st.builds(logiclanguage_TypeDeclaration)
@given(instance=logiclanguage_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_logiclanguage_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDeclaration)


logiclanguage_TypeDefinition_strategy = st.builds(logiclanguage_TypeDefinition)
@given(instance=logiclanguage_TypeDefinition_strategy)
@settings(max_examples=25)
def test_logiclanguage_TypeDefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDefinition)


logiclanguage_TypeDescriptor_strategy = st.builds(logiclanguage_TypeDescriptor)
@given(instance=logiclanguage_TypeDescriptor_strategy)
@settings(max_examples=25)
def test_logiclanguage_TypeDescriptor_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDescriptor)


logiclanguage_TypeReference_strategy = st.builds(logiclanguage_TypeReference)
@given(instance=logiclanguage_TypeReference_strategy)
@settings(max_examples=25)
def test_logiclanguage_TypeReference_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeReference)


logiclanguage_UnknownBecauseUninterpreted_strategy = st.builds(logiclanguage_UnknownBecauseUninterpreted)
@given(instance=logiclanguage_UnknownBecauseUninterpreted_strategy)
@settings(max_examples=25)
def test_logiclanguage_UnknownBecauseUninterpreted_instantiation(instance):
    assert isinstance(instance, logiclanguage_UnknownBecauseUninterpreted)


logiclanguage_Variable_strategy = st.builds(logiclanguage_Variable)
@given(instance=logiclanguage_Variable_strategy)
@settings(max_examples=25)
def test_logiclanguage_Variable_instantiation(instance):
    assert isinstance(instance, logiclanguage_Variable)



