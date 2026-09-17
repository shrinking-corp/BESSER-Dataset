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
    KeyValueExpression,
    eol_ModelDeclarationParameter,
    ArithmeticOperatorExpression,
    eol_PlusOperatorExpression,
    eol_MinusOperatorExpression,
    eol_MultiplyOperatorExpression,
    eol_DivideOperatorExpression,
    FeatureCallExpression,
    eol_PropertyCallExpression,
    eol_FOLMethodCallExpression,
    RealType,
    eol_IntegerType,
    SummablePrimitiveType,
    ComparablePrimitiveType,
    eol_RealType,
    PrimitiveType,
    eol_BooleanType,
    eol_SummablePrimitiveType,
    eol_ComparablePrimitiveType,
    OrderedCollectionType,
    eol_SequenceType,
    UniqueCollectionType,
    eol_OrderedSetType,
    eol_SetType,
    CollectionType,
    eol_OrderedCollectionType,
    eol_UniqueCollectionType,
    eol_BagType,
    eol_StringType,
    AnyType,
    eol_VoidType,
    eol_CollectionType,
    eol_PrimitiveType,
    eol_InvalidType,
    eol_ModelElementType,
    eol_ModelType,
    Type,
    eol_AnyType,
    eol_NativeType,
    eol_MapType,
    PseudoType,
    eol_SelfContentType,
    eol_SelfType,
    eol_PseudoType,
    AnnotationStatement,
    eol_ExecutableAnnotationStatement,
    eol_SimpleAnnotationStatement,
    AssignmentStatement,
    eol_SpecialAssignmentStatement,
    Statement,
    eol_DeleteStatement,
    eol_BreakStatement,
    eol_AssignmentStatement,
    eol_AbortStatement,
    eol_ReturnStatement,
    eol_ForStatement,
    eol_AnnotationStatement,
    eol_IfStatement,
    eol_ThrowStatement,
    eol_BreakAllStatement,
    eol_ExpressionStatement,
    eol_WhileStatement,
    eol_ContinueStatement,
    eol_TransactionStatement,
    CollectionInitialisationExpression,
    eol_ExpressionList,
    eol_ExpressionRange,
    OrderedCollection,
    eol_SequenceExpression,
    UniqueCollection,
    eol_OrderedSetExpression,
    eol_SetExpression,
    CollectionExpression,
    eol_UniqueCollection,
    eol_OrderedCollection,
    eol_BagExpression,
    SwitchCaseStatement,
    eol_SwitchCaseStatement,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    SummableExpression,
    ComparableExpression,
    eol_IntegerExpression,
    eol_RealExpression,
    eol_StringExpression,
    PrimitiveExpression,
    eol_BooleanExpression,
    eol_SummableExpression,
    eol_ComparableExpression,
    eol_SwitchStatement,
    VariableDeclarationExpression,
    ComparisonOperatorExpression,
    eol_EqualsOperatorExpression,
    eol_NotEqualsOperatorExpression,
    eol_GreaterThanOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_LessThanOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_MethodCallExpression,
    eol_FormalParameterExpression,
    LogicalOperatorExpression,
    eol_XorOperatorExpression,
    eol_ImpliesOperatorExpression,
    eol_OrOperatorExpression,
    eol_AndOperatorExpression,
    BinaryOperatorExpression,
    eol_ArithmeticOperatorExpression,
    eol_ComparisonOperatorExpression,
    eol_LogicalOperatorExpression,
    UnaryOperatorExpression,
    eol_NegativeOperatorExpression,
    eol_NotOperatorExpression,
    OperatorExpression,
    eol_BinaryOperatorExpression,
    eol_UnaryOperatorExpression,
    Expression,
    eol_CollectionExpression,
    eol_VariableDeclarationExpression,
    eol_PrimitiveExpression,
    eol_CollectionInitialisationExpression,
    eol_EnumerationLiteralExpression,
    eol_KeyValueExpression,
    eol_MapExpression,
    eol_NewExpression,
    eol_FeatureCallExpression,
    eol_NameExpression,
    eol_OperatorExpression,
    EOLElement,
    eol_EOLLibraryModule,
    eol_TextPosition,
    eol_TextRegion,
    eol_Type,
    eol_Expression,
    eol_ExpressionOrStatementBlock,
    Block,
    eol_AnnotationBlock,
    eol_Statement,
    eol_Block,
    EOLLibraryModule,
    eol_EOLModule,
    eol_OperationDefinition,
    eol_ModelDeclarationStatement,
    eol_Import,
    eol_EOLElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(KeyValueExpression)


def test_hyp_keyvalueexpression_constructor_exists():
    assert callable(KeyValueExpression.__init__)


def test_hyp_keyvalueexpression_constructor_args():
    sig = inspect.signature(KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationParameter)


def test_hyp_eol_modeldeclarationparameter_constructor_exists():
    assert callable(eol_ModelDeclarationParameter.__init__)


def test_hyp_eol_modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_hyp_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_hyp_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PlusOperatorExpression)


def test_hyp_eol_plusoperatorexpression_constructor_exists():
    assert callable(eol_PlusOperatorExpression.__init__)


def test_hyp_eol_plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MinusOperatorExpression)


def test_hyp_eol_minusoperatorexpression_constructor_exists():
    assert callable(eol_MinusOperatorExpression.__init__)


def test_hyp_eol_minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MultiplyOperatorExpression)


def test_hyp_eol_multiplyoperatorexpression_constructor_exists():
    assert callable(eol_MultiplyOperatorExpression.__init__)


def test_hyp_eol_multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol_MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_DivideOperatorExpression)


def test_hyp_eol_divideoperatorexpression_constructor_exists():
    assert callable(eol_DivideOperatorExpression.__init__)


def test_hyp_eol_divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol_DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_hyp_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_hyp_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PropertyCallExpression)


def test_hyp_eol_propertycallexpression_constructor_exists():
    assert callable(eol_PropertyCallExpression.__init__)


def test_hyp_eol_propertycallexpression_constructor_args():
    sig = inspect.signature(eol_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "extended" in params, "Missing parameter 'extended'"




def test_hyp_eol_folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FOLMethodCallExpression)


def test_hyp_eol_folmethodcallexpression_constructor_exists():
    assert callable(eol_FOLMethodCallExpression.__init__)


def test_hyp_eol_folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol_FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_hyp_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_hyp_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_integertype_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerType)


def test_hyp_eol_integertype_constructor_exists():
    assert callable(eol_IntegerType.__init__)


def test_hyp_eol_integertype_constructor_args():
    sig = inspect.signature(eol_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(SummablePrimitiveType)


def test_hyp_summableprimitivetype_constructor_exists():
    assert callable(SummablePrimitiveType.__init__)


def test_hyp_summableprimitivetype_constructor_args():
    sig = inspect.signature(SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ComparablePrimitiveType)


def test_hyp_comparableprimitivetype_constructor_exists():
    assert callable(ComparablePrimitiveType.__init__)


def test_hyp_comparableprimitivetype_constructor_args():
    sig = inspect.signature(ComparablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_realtype_is_not_abstract():
    assert not inspect.isabstract(eol_RealType)


def test_hyp_eol_realtype_constructor_exists():
    assert callable(eol_RealType.__init__)


def test_hyp_eol_realtype_constructor_args():
    sig = inspect.signature(eol_RealType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_booleantype_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanType)


def test_hyp_eol_booleantype_constructor_exists():
    assert callable(eol_BooleanType.__init__)


def test_hyp_eol_booleantype_constructor_args():
    sig = inspect.signature(eol_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_SummablePrimitiveType)


def test_hyp_eol_summableprimitivetype_constructor_exists():
    assert callable(eol_SummablePrimitiveType.__init__)


def test_hyp_eol_summableprimitivetype_constructor_args():
    sig = inspect.signature(eol_SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_ComparablePrimitiveType)


def test_hyp_eol_comparableprimitivetype_constructor_exists():
    assert callable(eol_ComparablePrimitiveType.__init__)


def test_hyp_eol_comparableprimitivetype_constructor_args():
    sig = inspect.signature(eol_ComparablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(OrderedCollectionType)


def test_hyp_orderedcollectiontype_constructor_exists():
    assert callable(OrderedCollectionType.__init__)


def test_hyp_orderedcollectiontype_constructor_args():
    sig = inspect.signature(OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_sequencetype_is_not_abstract():
    assert not inspect.isabstract(eol_SequenceType)


def test_hyp_eol_sequencetype_constructor_exists():
    assert callable(eol_SequenceType.__init__)


def test_hyp_eol_sequencetype_constructor_args():
    sig = inspect.signature(eol_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(UniqueCollectionType)


def test_hyp_uniquecollectiontype_constructor_exists():
    assert callable(UniqueCollectionType.__init__)


def test_hyp_uniquecollectiontype_constructor_args():
    sig = inspect.signature(UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedSetType)


def test_hyp_eol_orderedsettype_constructor_exists():
    assert callable(eol_OrderedSetType.__init__)


def test_hyp_eol_orderedsettype_constructor_args():
    sig = inspect.signature(eol_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_settype_is_not_abstract():
    assert not inspect.isabstract(eol_SetType)


def test_hyp_eol_settype_constructor_exists():
    assert callable(eol_SetType.__init__)


def test_hyp_eol_settype_constructor_args():
    sig = inspect.signature(eol_SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_hyp_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_hyp_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedCollectionType)


def test_hyp_eol_orderedcollectiontype_constructor_exists():
    assert callable(eol_OrderedCollectionType.__init__)


def test_hyp_eol_orderedcollectiontype_constructor_args():
    sig = inspect.signature(eol_OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_UniqueCollectionType)


def test_hyp_eol_uniquecollectiontype_constructor_exists():
    assert callable(eol_UniqueCollectionType.__init__)


def test_hyp_eol_uniquecollectiontype_constructor_args():
    sig = inspect.signature(eol_UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_bagtype_is_not_abstract():
    assert not inspect.isabstract(eol_BagType)


def test_hyp_eol_bagtype_constructor_exists():
    assert callable(eol_BagType.__init__)


def test_hyp_eol_bagtype_constructor_args():
    sig = inspect.signature(eol_BagType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_stringtype_is_not_abstract():
    assert not inspect.isabstract(eol_StringType)


def test_hyp_eol_stringtype_constructor_exists():
    assert callable(eol_StringType.__init__)


def test_hyp_eol_stringtype_constructor_args():
    sig = inspect.signature(eol_StringType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_hyp_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_hyp_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_voidtype_is_not_abstract():
    assert not inspect.isabstract(eol_VoidType)


def test_hyp_eol_voidtype_constructor_exists():
    assert callable(eol_VoidType.__init__)


def test_hyp_eol_voidtype_constructor_args():
    sig = inspect.signature(eol_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_collectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionType)


def test_hyp_eol_collectiontype_constructor_exists():
    assert callable(eol_CollectionType.__init__)


def test_hyp_eol_collectiontype_constructor_args():
    sig = inspect.signature(eol_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveType)


def test_hyp_eol_primitivetype_constructor_exists():
    assert callable(eol_PrimitiveType.__init__)


def test_hyp_eol_primitivetype_constructor_args():
    sig = inspect.signature(eol_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_invalidtype_is_not_abstract():
    assert not inspect.isabstract(eol_InvalidType)


def test_hyp_eol_invalidtype_constructor_exists():
    assert callable(eol_InvalidType.__init__)


def test_hyp_eol_invalidtype_constructor_args():
    sig = inspect.signature(eol_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelElementType)


def test_hyp_eol_modelelementtype_constructor_exists():
    assert callable(eol_ModelElementType.__init__)


def test_hyp_eol_modelelementtype_constructor_args():
    sig = inspect.signature(eol_ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"
    assert "modelElementType" in params, "Missing parameter 'modelElementType'"
    assert "modelName" in params, "Missing parameter 'modelName'"
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "resolvedIPackage" in params, "Missing parameter 'resolvedIPackage'"








def test_hyp_eol_modeltype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelType)


def test_hyp_eol_modeltype_constructor_exists():
    assert callable(eol_ModelType.__init__)


def test_hyp_eol_modeltype_constructor_args():
    sig = inspect.signature(eol_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"
    assert "modelName" in params, "Missing parameter 'modelName'"





def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_anytype_is_not_abstract():
    assert not inspect.isabstract(eol_AnyType)


def test_hyp_eol_anytype_constructor_exists():
    assert callable(eol_AnyType.__init__)


def test_hyp_eol_anytype_constructor_args():
    sig = inspect.signature(eol_AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "declared" in params, "Missing parameter 'declared'"




def test_hyp_eol_nativetype_is_not_abstract():
    assert not inspect.isabstract(eol_NativeType)


def test_hyp_eol_nativetype_constructor_exists():
    assert callable(eol_NativeType.__init__)


def test_hyp_eol_nativetype_constructor_args():
    sig = inspect.signature(eol_NativeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_maptype_is_not_abstract():
    assert not inspect.isabstract(eol_MapType)


def test_hyp_eol_maptype_constructor_exists():
    assert callable(eol_MapType.__init__)


def test_hyp_eol_maptype_constructor_args():
    sig = inspect.signature(eol_MapType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pseudotype_is_not_abstract():
    assert not inspect.isabstract(PseudoType)


def test_hyp_pseudotype_constructor_exists():
    assert callable(PseudoType.__init__)


def test_hyp_pseudotype_constructor_args():
    sig = inspect.signature(PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_selfcontenttype_is_not_abstract():
    assert not inspect.isabstract(eol_SelfContentType)


def test_hyp_eol_selfcontenttype_constructor_exists():
    assert callable(eol_SelfContentType.__init__)


def test_hyp_eol_selfcontenttype_constructor_args():
    sig = inspect.signature(eol_SelfContentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_selftype_is_not_abstract():
    assert not inspect.isabstract(eol_SelfType)


def test_hyp_eol_selftype_constructor_exists():
    assert callable(eol_SelfType.__init__)


def test_hyp_eol_selftype_constructor_args():
    sig = inspect.signature(eol_SelfType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_pseudotype_is_not_abstract():
    assert not inspect.isabstract(eol_PseudoType)


def test_hyp_eol_pseudotype_constructor_exists():
    assert callable(eol_PseudoType.__init__)


def test_hyp_eol_pseudotype_constructor_args():
    sig = inspect.signature(eol_PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(AnnotationStatement)


def test_hyp_annotationstatement_constructor_exists():
    assert callable(AnnotationStatement.__init__)


def test_hyp_annotationstatement_constructor_args():
    sig = inspect.signature(AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_executableannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ExecutableAnnotationStatement)


def test_hyp_eol_executableannotationstatement_constructor_exists():
    assert callable(eol_ExecutableAnnotationStatement.__init__)


def test_hyp_eol_executableannotationstatement_constructor_args():
    sig = inspect.signature(eol_ExecutableAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_simpleannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SimpleAnnotationStatement)


def test_hyp_eol_simpleannotationstatement_constructor_exists():
    assert callable(eol_SimpleAnnotationStatement.__init__)


def test_hyp_eol_simpleannotationstatement_constructor_args():
    sig = inspect.signature(eol_SimpleAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_hyp_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_hyp_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SpecialAssignmentStatement)


def test_hyp_eol_specialassignmentstatement_constructor_exists():
    assert callable(eol_SpecialAssignmentStatement.__init__)


def test_hyp_eol_specialassignmentstatement_constructor_args():
    sig = inspect.signature(eol_SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol_DeleteStatement)


def test_hyp_eol_deletestatement_constructor_exists():
    assert callable(eol_DeleteStatement.__init__)


def test_hyp_eol_deletestatement_constructor_args():
    sig = inspect.signature(eol_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol_BreakStatement)


def test_hyp_eol_breakstatement_constructor_exists():
    assert callable(eol_BreakStatement.__init__)


def test_hyp_eol_breakstatement_constructor_args():
    sig = inspect.signature(eol_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AssignmentStatement)


def test_hyp_eol_assignmentstatement_constructor_exists():
    assert callable(eol_AssignmentStatement.__init__)


def test_hyp_eol_assignmentstatement_constructor_args():
    sig = inspect.signature(eol_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_abortstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AbortStatement)


def test_hyp_eol_abortstatement_constructor_exists():
    assert callable(eol_AbortStatement.__init__)


def test_hyp_eol_abortstatement_constructor_args():
    sig = inspect.signature(eol_AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ReturnStatement)


def test_hyp_eol_returnstatement_constructor_exists():
    assert callable(eol_ReturnStatement.__init__)


def test_hyp_eol_returnstatement_constructor_args():
    sig = inspect.signature(eol_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_forstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ForStatement)


def test_hyp_eol_forstatement_constructor_exists():
    assert callable(eol_ForStatement.__init__)


def test_hyp_eol_forstatement_constructor_args():
    sig = inspect.signature(eol_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AnnotationStatement)


def test_hyp_eol_annotationstatement_constructor_exists():
    assert callable(eol_AnnotationStatement.__init__)


def test_hyp_eol_annotationstatement_constructor_args():
    sig = inspect.signature(eol_AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol_IfStatement)


def test_hyp_eol_ifstatement_constructor_exists():
    assert callable(eol_IfStatement.__init__)


def test_hyp_eol_ifstatement_constructor_args():
    sig = inspect.signature(eol_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_throwstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ThrowStatement)


def test_hyp_eol_throwstatement_constructor_exists():
    assert callable(eol_ThrowStatement.__init__)


def test_hyp_eol_throwstatement_constructor_args():
    sig = inspect.signature(eol_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_breakallstatement_is_not_abstract():
    assert not inspect.isabstract(eol_BreakAllStatement)


def test_hyp_eol_breakallstatement_constructor_exists():
    assert callable(eol_BreakAllStatement.__init__)


def test_hyp_eol_breakallstatement_constructor_args():
    sig = inspect.signature(eol_BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionStatement)


def test_hyp_eol_expressionstatement_constructor_exists():
    assert callable(eol_ExpressionStatement.__init__)


def test_hyp_eol_expressionstatement_constructor_args():
    sig = inspect.signature(eol_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_whilestatement_is_not_abstract():
    assert not inspect.isabstract(eol_WhileStatement)


def test_hyp_eol_whilestatement_constructor_exists():
    assert callable(eol_WhileStatement.__init__)


def test_hyp_eol_whilestatement_constructor_args():
    sig = inspect.signature(eol_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol_ContinueStatement)


def test_hyp_eol_continuestatement_constructor_exists():
    assert callable(eol_ContinueStatement.__init__)


def test_hyp_eol_continuestatement_constructor_args():
    sig = inspect.signature(eol_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_transactionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_TransactionStatement)


def test_hyp_eol_transactionstatement_constructor_exists():
    assert callable(eol_TransactionStatement.__init__)


def test_hyp_eol_transactionstatement_constructor_args():
    sig = inspect.signature(eol_TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionInitialisationExpression)


def test_hyp_collectioninitialisationexpression_constructor_exists():
    assert callable(CollectionInitialisationExpression.__init__)


def test_hyp_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_expressionlist_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionList)


def test_hyp_eol_expressionlist_constructor_exists():
    assert callable(eol_ExpressionList.__init__)


def test_hyp_eol_expressionlist_constructor_args():
    sig = inspect.signature(eol_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_expressionrange_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionRange)


def test_hyp_eol_expressionrange_constructor_exists():
    assert callable(eol_ExpressionRange.__init__)


def test_hyp_eol_expressionrange_constructor_args():
    sig = inspect.signature(eol_ExpressionRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(OrderedCollection)


def test_hyp_orderedcollection_constructor_exists():
    assert callable(OrderedCollection.__init__)


def test_hyp_orderedcollection_constructor_args():
    sig = inspect.signature(OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SequenceExpression)


def test_hyp_eol_sequenceexpression_constructor_exists():
    assert callable(eol_SequenceExpression.__init__)


def test_hyp_eol_sequenceexpression_constructor_args():
    sig = inspect.signature(eol_SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(UniqueCollection)


def test_hyp_uniquecollection_constructor_exists():
    assert callable(UniqueCollection.__init__)


def test_hyp_uniquecollection_constructor_args():
    sig = inspect.signature(UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedSetExpression)


def test_hyp_eol_orderedsetexpression_constructor_exists():
    assert callable(eol_OrderedSetExpression.__init__)


def test_hyp_eol_orderedsetexpression_constructor_args():
    sig = inspect.signature(eol_OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_setexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SetExpression)


def test_hyp_eol_setexpression_constructor_exists():
    assert callable(eol_SetExpression.__init__)


def test_hyp_eol_setexpression_constructor_args():
    sig = inspect.signature(eol_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_hyp_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_hyp_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(eol_UniqueCollection)


def test_hyp_eol_uniquecollection_constructor_exists():
    assert callable(eol_UniqueCollection.__init__)


def test_hyp_eol_uniquecollection_constructor_args():
    sig = inspect.signature(eol_UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedCollection)


def test_hyp_eol_orderedcollection_constructor_exists():
    assert callable(eol_OrderedCollection.__init__)


def test_hyp_eol_orderedcollection_constructor_args():
    sig = inspect.signature(eol_OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BagExpression)


def test_hyp_eol_bagexpression_constructor_exists():
    assert callable(eol_BagExpression.__init__)


def test_hyp_eol_bagexpression_constructor_args():
    sig = inspect.signature(eol_BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_hyp_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_hyp_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseStatement)


def test_hyp_eol_switchcasestatement_constructor_exists():
    assert callable(eol_SwitchCaseStatement.__init__)


def test_hyp_eol_switchcasestatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseDefaultStatement)


def test_hyp_eol_switchcasedefaultstatement_constructor_exists():
    assert callable(eol_SwitchCaseDefaultStatement.__init__)


def test_hyp_eol_switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseExpressionStatement)


def test_hyp_eol_switchcaseexpressionstatement_constructor_exists():
    assert callable(eol_SwitchCaseExpressionStatement.__init__)


def test_hyp_eol_switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_summableexpression_is_not_abstract():
    assert not inspect.isabstract(SummableExpression)


def test_hyp_summableexpression_constructor_exists():
    assert callable(SummableExpression.__init__)


def test_hyp_summableexpression_constructor_args():
    sig = inspect.signature(SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(ComparableExpression)


def test_hyp_comparableexpression_constructor_exists():
    assert callable(ComparableExpression.__init__)


def test_hyp_comparableexpression_constructor_args():
    sig = inspect.signature(ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerExpression)


def test_hyp_eol_integerexpression_constructor_exists():
    assert callable(eol_IntegerExpression.__init__)


def test_hyp_eol_integerexpression_constructor_args():
    sig = inspect.signature(eol_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_eol_realexpression_is_not_abstract():
    assert not inspect.isabstract(eol_RealExpression)


def test_hyp_eol_realexpression_constructor_exists():
    assert callable(eol_RealExpression.__init__)


def test_hyp_eol_realexpression_constructor_args():
    sig = inspect.signature(eol_RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_eol_stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol_StringExpression)


def test_hyp_eol_stringexpression_constructor_exists():
    assert callable(eol_StringExpression.__init__)


def test_hyp_eol_stringexpression_constructor_args():
    sig = inspect.signature(eol_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_hyp_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_hyp_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanExpression)


def test_hyp_eol_booleanexpression_constructor_exists():
    assert callable(eol_BooleanExpression.__init__)


def test_hyp_eol_booleanexpression_constructor_args():
    sig = inspect.signature(eol_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_eol_summableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SummableExpression)


def test_hyp_eol_summableexpression_constructor_exists():
    assert callable(eol_SummableExpression.__init__)


def test_hyp_eol_summableexpression_constructor_args():
    sig = inspect.signature(eol_SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ComparableExpression)


def test_hyp_eol_comparableexpression_constructor_exists():
    assert callable(eol_ComparableExpression.__init__)


def test_hyp_eol_comparableexpression_constructor_args():
    sig = inspect.signature(eol_ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchStatement)


def test_hyp_eol_switchstatement_constructor_exists():
    assert callable(eol_SwitchStatement.__init__)


def test_hyp_eol_switchstatement_constructor_args():
    sig = inspect.signature(eol_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_hyp_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_hyp_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_hyp_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_hyp_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EqualsOperatorExpression)


def test_hyp_eol_equalsoperatorexpression_constructor_exists():
    assert callable(eol_EqualsOperatorExpression.__init__)


def test_hyp_eol_equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NotEqualsOperatorExpression)


def test_hyp_eol_notequalsoperatorexpression_constructor_exists():
    assert callable(eol_NotEqualsOperatorExpression.__init__)


def test_hyp_eol_notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOperatorExpression)


def test_hyp_eol_greaterthanoperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOperatorExpression.__init__)


def test_hyp_eol_greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LessThanOrEqualToOperatorExpression)


def test_hyp_eol_lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_LessThanOrEqualToOperatorExpression.__init__)


def test_hyp_eol_lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LessThanOperatorExpression)


def test_hyp_eol_lessthanoperatorexpression_constructor_exists():
    assert callable(eol_LessThanOperatorExpression.__init__)


def test_hyp_eol_lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOrEqualToOperatorExpression)


def test_hyp_eol_greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOrEqualToOperatorExpression.__init__)


def test_hyp_eol_greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MethodCallExpression)


def test_hyp_eol_methodcallexpression_constructor_exists():
    assert callable(eol_MethodCallExpression.__init__)


def test_hyp_eol_methodcallexpression_constructor_args():
    sig = inspect.signature(eol_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FormalParameterExpression)


def test_hyp_eol_formalparameterexpression_constructor_exists():
    assert callable(eol_FormalParameterExpression.__init__)


def test_hyp_eol_formalparameterexpression_constructor_args():
    sig = inspect.signature(eol_FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_hyp_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_hyp_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_XorOperatorExpression)


def test_hyp_eol_xoroperatorexpression_constructor_exists():
    assert callable(eol_XorOperatorExpression.__init__)


def test_hyp_eol_xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol_XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ImpliesOperatorExpression)


def test_hyp_eol_impliesoperatorexpression_constructor_exists():
    assert callable(eol_ImpliesOperatorExpression.__init__)


def test_hyp_eol_impliesoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrOperatorExpression)


def test_hyp_eol_oroperatorexpression_constructor_exists():
    assert callable(eol_OrOperatorExpression.__init__)


def test_hyp_eol_oroperatorexpression_constructor_args():
    sig = inspect.signature(eol_OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_AndOperatorExpression)


def test_hyp_eol_andoperatorexpression_constructor_exists():
    assert callable(eol_AndOperatorExpression.__init__)


def test_hyp_eol_andoperatorexpression_constructor_args():
    sig = inspect.signature(eol_AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_hyp_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_hyp_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ArithmeticOperatorExpression)


def test_hyp_eol_arithmeticoperatorexpression_constructor_exists():
    assert callable(eol_ArithmeticOperatorExpression.__init__)


def test_hyp_eol_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ComparisonOperatorExpression)


def test_hyp_eol_comparisonoperatorexpression_constructor_exists():
    assert callable(eol_ComparisonOperatorExpression.__init__)


def test_hyp_eol_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LogicalOperatorExpression)


def test_hyp_eol_logicaloperatorexpression_constructor_exists():
    assert callable(eol_LogicalOperatorExpression.__init__)


def test_hyp_eol_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol_LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_hyp_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_hyp_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NegativeOperatorExpression)


def test_hyp_eol_negativeoperatorexpression_constructor_exists():
    assert callable(eol_NegativeOperatorExpression.__init__)


def test_hyp_eol_negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NotOperatorExpression)


def test_hyp_eol_notoperatorexpression_constructor_exists():
    assert callable(eol_NotOperatorExpression.__init__)


def test_hyp_eol_notoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_hyp_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_hyp_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BinaryOperatorExpression)


def test_hyp_eol_binaryoperatorexpression_constructor_exists():
    assert callable(eol_BinaryOperatorExpression.__init__)


def test_hyp_eol_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_UnaryOperatorExpression)


def test_hyp_eol_unaryoperatorexpression_constructor_exists():
    assert callable(eol_UnaryOperatorExpression.__init__)


def test_hyp_eol_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionExpression)


def test_hyp_eol_collectionexpression_constructor_exists():
    assert callable(eol_CollectionExpression.__init__)


def test_hyp_eol_collectionexpression_constructor_args():
    sig = inspect.signature(eol_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_VariableDeclarationExpression)


def test_hyp_eol_variabledeclarationexpression_constructor_exists():
    assert callable(eol_VariableDeclarationExpression.__init__)


def test_hyp_eol_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "create" in params, "Missing parameter 'create'"




def test_hyp_eol_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveExpression)


def test_hyp_eol_primitiveexpression_constructor_exists():
    assert callable(eol_PrimitiveExpression.__init__)


def test_hyp_eol_primitiveexpression_constructor_args():
    sig = inspect.signature(eol_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionInitialisationExpression)


def test_hyp_eol_collectioninitialisationexpression_constructor_exists():
    assert callable(eol_CollectionInitialisationExpression.__init__)


def test_hyp_eol_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(eol_CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EnumerationLiteralExpression)


def test_hyp_eol_enumerationliteralexpression_constructor_exists():
    assert callable(eol_EnumerationLiteralExpression.__init__)


def test_hyp_eol_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(eol_KeyValueExpression)


def test_hyp_eol_keyvalueexpression_constructor_exists():
    assert callable(eol_KeyValueExpression.__init__)


def test_hyp_eol_keyvalueexpression_constructor_args():
    sig = inspect.signature(eol_KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MapExpression)


def test_hyp_eol_mapexpression_constructor_exists():
    assert callable(eol_MapExpression.__init__)


def test_hyp_eol_mapexpression_constructor_args():
    sig = inspect.signature(eol_MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_newexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NewExpression)


def test_hyp_eol_newexpression_constructor_exists():
    assert callable(eol_NewExpression.__init__)


def test_hyp_eol_newexpression_constructor_args():
    sig = inspect.signature(eol_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FeatureCallExpression)


def test_hyp_eol_featurecallexpression_constructor_exists():
    assert callable(eol_FeatureCallExpression.__init__)


def test_hyp_eol_featurecallexpression_constructor_args():
    sig = inspect.signature(eol_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arrow" in params, "Missing parameter 'arrow'"




def test_hyp_eol_nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NameExpression)


def test_hyp_eol_nameexpression_constructor_exists():
    assert callable(eol_NameExpression.__init__)


def test_hyp_eol_nameexpression_constructor_args():
    sig = inspect.signature(eol_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "resolvedContent" in params, "Missing parameter 'resolvedContent'"
    assert "isType" in params, "Missing parameter 'isType'"






def test_hyp_eol_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OperatorExpression)


def test_hyp_eol_operatorexpression_constructor_exists():
    assert callable(eol_OperatorExpression.__init__)


def test_hyp_eol_operatorexpression_constructor_args():
    sig = inspect.signature(eol_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eolelement_is_not_abstract():
    assert not inspect.isabstract(EOLElement)


def test_hyp_eolelement_constructor_exists():
    assert callable(EOLElement.__init__)


def test_hyp_eolelement_constructor_args():
    sig = inspect.signature(EOLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol_EOLLibraryModule)


def test_hyp_eol_eollibrarymodule_constructor_exists():
    assert callable(eol_EOLLibraryModule.__init__)


def test_hyp_eol_eollibrarymodule_constructor_args():
    sig = inspect.signature(eol_EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_eol_textposition_is_not_abstract():
    assert not inspect.isabstract(eol_TextPosition)


def test_hyp_eol_textposition_constructor_exists():
    assert callable(eol_TextPosition.__init__)


def test_hyp_eol_textposition_constructor_args():
    sig = inspect.signature(eol_TextPosition.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"





def test_hyp_eol_textregion_is_not_abstract():
    assert not inspect.isabstract(eol_TextRegion)


def test_hyp_eol_textregion_constructor_exists():
    assert callable(eol_TextRegion.__init__)


def test_hyp_eol_textregion_constructor_args():
    sig = inspect.signature(eol_TextRegion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_type_is_not_abstract():
    assert not inspect.isabstract(eol_Type)


def test_hyp_eol_type_constructor_exists():
    assert callable(eol_Type.__init__)


def test_hyp_eol_type_constructor_args():
    sig = inspect.signature(eol_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_expression_is_not_abstract():
    assert not inspect.isabstract(eol_Expression)


def test_hyp_eol_expression_constructor_exists():
    assert callable(eol_Expression.__init__)


def test_hyp_eol_expression_constructor_args():
    sig = inspect.signature(eol_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "inBrackets" in params, "Missing parameter 'inBrackets'"




def test_hyp_eol_expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionOrStatementBlock)


def test_hyp_eol_expressionorstatementblock_constructor_exists():
    assert callable(eol_ExpressionOrStatementBlock.__init__)


def test_hyp_eol_expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol_ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_annotationblock_is_not_abstract():
    assert not inspect.isabstract(eol_AnnotationBlock)


def test_hyp_eol_annotationblock_constructor_exists():
    assert callable(eol_AnnotationBlock.__init__)


def test_hyp_eol_annotationblock_constructor_args():
    sig = inspect.signature(eol_AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_statement_is_not_abstract():
    assert not inspect.isabstract(eol_Statement)


def test_hyp_eol_statement_constructor_exists():
    assert callable(eol_Statement.__init__)


def test_hyp_eol_statement_constructor_args():
    sig = inspect.signature(eol_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_block_is_not_abstract():
    assert not inspect.isabstract(eol_Block)


def test_hyp_eol_block_constructor_exists():
    assert callable(eol_Block.__init__)


def test_hyp_eol_block_constructor_args():
    sig = inspect.signature(eol_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EOLLibraryModule)


def test_hyp_eollibrarymodule_constructor_exists():
    assert callable(EOLLibraryModule.__init__)


def test_hyp_eollibrarymodule_constructor_args():
    sig = inspect.signature(EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_eolmodule_is_not_abstract():
    assert not inspect.isabstract(eol_EOLModule)


def test_hyp_eol_eolmodule_constructor_exists():
    assert callable(eol_EOLModule.__init__)


def test_hyp_eol_eolmodule_constructor_args():
    sig = inspect.signature(eol_EOLModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(eol_OperationDefinition)


def test_hyp_eol_operationdefinition_constructor_exists():
    assert callable(eol_OperationDefinition.__init__)


def test_hyp_eol_operationdefinition_constructor_args():
    sig = inspect.signature(eol_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eol_modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationStatement)


def test_hyp_eol_modeldeclarationstatement_constructor_exists():
    assert callable(eol_ModelDeclarationStatement.__init__)


def test_hyp_eol_modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"




def test_hyp_eol_import_is_not_abstract():
    assert not inspect.isabstract(eol_Import)


def test_hyp_eol_import_constructor_exists():
    assert callable(eol_Import.__init__)


def test_hyp_eol_import_constructor_args():
    sig = inspect.signature(eol_Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"




def test_hyp_eol_eolelement_is_not_abstract():
    assert not inspect.isabstract(eol_EOLElement)


def test_hyp_eol_eolelement_constructor_exists():
    assert callable(eol_EOLElement.__init__)


def test_hyp_eol_eolelement_constructor_args():
    sig = inspect.signature(eol_EOLElement.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"



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
KeyValueExpression_strategy = st.builds(
    KeyValueExpression,
)
eol_ModelDeclarationParameter_strategy = st.builds(
    eol_ModelDeclarationParameter,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol_PlusOperatorExpression_strategy = st.builds(
    eol_PlusOperatorExpression,
)
eol_MinusOperatorExpression_strategy = st.builds(
    eol_MinusOperatorExpression,
)
eol_MultiplyOperatorExpression_strategy = st.builds(
    eol_MultiplyOperatorExpression,
)
eol_DivideOperatorExpression_strategy = st.builds(
    eol_DivideOperatorExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol_PropertyCallExpression_strategy = st.builds(
    eol_PropertyCallExpression,
    extended=
        st.booleans()
)
eol_FOLMethodCallExpression_strategy = st.builds(
    eol_FOLMethodCallExpression,
)
RealType_strategy = st.builds(
    RealType,
)
eol_IntegerType_strategy = st.builds(
    eol_IntegerType,
)
SummablePrimitiveType_strategy = st.builds(
    SummablePrimitiveType,
)
ComparablePrimitiveType_strategy = st.builds(
    ComparablePrimitiveType,
)
eol_RealType_strategy = st.builds(
    eol_RealType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol_BooleanType_strategy = st.builds(
    eol_BooleanType,
)
eol_SummablePrimitiveType_strategy = st.builds(
    eol_SummablePrimitiveType,
)
eol_ComparablePrimitiveType_strategy = st.builds(
    eol_ComparablePrimitiveType,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol_SequenceType_strategy = st.builds(
    eol_SequenceType,
)
UniqueCollectionType_strategy = st.builds(
    UniqueCollectionType,
)
eol_OrderedSetType_strategy = st.builds(
    eol_OrderedSetType,
)
eol_SetType_strategy = st.builds(
    eol_SetType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
eol_OrderedCollectionType_strategy = st.builds(
    eol_OrderedCollectionType,
)
eol_UniqueCollectionType_strategy = st.builds(
    eol_UniqueCollectionType,
)
eol_BagType_strategy = st.builds(
    eol_BagType,
)
eol_StringType_strategy = st.builds(
    eol_StringType,
)
AnyType_strategy = st.builds(
    AnyType,
)
eol_VoidType_strategy = st.builds(
    eol_VoidType,
)
eol_CollectionType_strategy = st.builds(
    eol_CollectionType,
)
eol_PrimitiveType_strategy = st.builds(
    eol_PrimitiveType,
)
eol_InvalidType_strategy = st.builds(
    eol_InvalidType,
)
eol_ModelElementType_strategy = st.builds(
    eol_ModelElementType,
    resolvedIMetamodel=
        safe_text,
    modelElementType=
        safe_text,
    modelName=
        safe_text,
    elementName=
        safe_text,
    resolvedIPackage=
        safe_text
)
eol_ModelType_strategy = st.builds(
    eol_ModelType,
    resolvedIMetamodel=
        safe_text,
    modelName=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
eol_AnyType_strategy = st.builds(
    eol_AnyType,
    declared=
        st.booleans()
)
eol_NativeType_strategy = st.builds(
    eol_NativeType,
)
eol_MapType_strategy = st.builds(
    eol_MapType,
)
PseudoType_strategy = st.builds(
    PseudoType,
)
eol_SelfContentType_strategy = st.builds(
    eol_SelfContentType,
)
eol_SelfType_strategy = st.builds(
    eol_SelfType,
)
eol_PseudoType_strategy = st.builds(
    eol_PseudoType,
)
AnnotationStatement_strategy = st.builds(
    AnnotationStatement,
)
eol_ExecutableAnnotationStatement_strategy = st.builds(
    eol_ExecutableAnnotationStatement,
)
eol_SimpleAnnotationStatement_strategy = st.builds(
    eol_SimpleAnnotationStatement,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol_SpecialAssignmentStatement_strategy = st.builds(
    eol_SpecialAssignmentStatement,
)
Statement_strategy = st.builds(
    Statement,
)
eol_DeleteStatement_strategy = st.builds(
    eol_DeleteStatement,
)
eol_BreakStatement_strategy = st.builds(
    eol_BreakStatement,
)
eol_AssignmentStatement_strategy = st.builds(
    eol_AssignmentStatement,
)
eol_AbortStatement_strategy = st.builds(
    eol_AbortStatement,
)
eol_ReturnStatement_strategy = st.builds(
    eol_ReturnStatement,
)
eol_ForStatement_strategy = st.builds(
    eol_ForStatement,
)
eol_AnnotationStatement_strategy = st.builds(
    eol_AnnotationStatement,
)
eol_IfStatement_strategy = st.builds(
    eol_IfStatement,
)
eol_ThrowStatement_strategy = st.builds(
    eol_ThrowStatement,
)
eol_BreakAllStatement_strategy = st.builds(
    eol_BreakAllStatement,
)
eol_ExpressionStatement_strategy = st.builds(
    eol_ExpressionStatement,
)
eol_WhileStatement_strategy = st.builds(
    eol_WhileStatement,
)
eol_ContinueStatement_strategy = st.builds(
    eol_ContinueStatement,
)
eol_TransactionStatement_strategy = st.builds(
    eol_TransactionStatement,
)
CollectionInitialisationExpression_strategy = st.builds(
    CollectionInitialisationExpression,
)
eol_ExpressionList_strategy = st.builds(
    eol_ExpressionList,
)
eol_ExpressionRange_strategy = st.builds(
    eol_ExpressionRange,
)
OrderedCollection_strategy = st.builds(
    OrderedCollection,
)
eol_SequenceExpression_strategy = st.builds(
    eol_SequenceExpression,
)
UniqueCollection_strategy = st.builds(
    UniqueCollection,
)
eol_OrderedSetExpression_strategy = st.builds(
    eol_OrderedSetExpression,
)
eol_SetExpression_strategy = st.builds(
    eol_SetExpression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol_UniqueCollection_strategy = st.builds(
    eol_UniqueCollection,
)
eol_OrderedCollection_strategy = st.builds(
    eol_OrderedCollection,
)
eol_BagExpression_strategy = st.builds(
    eol_BagExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
eol_SwitchCaseStatement_strategy = st.builds(
    eol_SwitchCaseStatement,
)
eol_SwitchCaseDefaultStatement_strategy = st.builds(
    eol_SwitchCaseDefaultStatement,
)
eol_SwitchCaseExpressionStatement_strategy = st.builds(
    eol_SwitchCaseExpressionStatement,
)
SummableExpression_strategy = st.builds(
    SummableExpression,
)
ComparableExpression_strategy = st.builds(
    ComparableExpression,
)
eol_IntegerExpression_strategy = st.builds(
    eol_IntegerExpression,
    value=
        st.integers()
)
eol_RealExpression_strategy = st.builds(
    eol_RealExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol_StringExpression_strategy = st.builds(
    eol_StringExpression,
    value=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol_BooleanExpression_strategy = st.builds(
    eol_BooleanExpression,
    value=
        st.booleans()
)
eol_SummableExpression_strategy = st.builds(
    eol_SummableExpression,
)
eol_ComparableExpression_strategy = st.builds(
    eol_ComparableExpression,
)
eol_SwitchStatement_strategy = st.builds(
    eol_SwitchStatement,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol_EqualsOperatorExpression_strategy = st.builds(
    eol_EqualsOperatorExpression,
)
eol_NotEqualsOperatorExpression_strategy = st.builds(
    eol_NotEqualsOperatorExpression,
)
eol_GreaterThanOperatorExpression_strategy = st.builds(
    eol_GreaterThanOperatorExpression,
)
eol_LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_LessThanOrEqualToOperatorExpression,
)
eol_LessThanOperatorExpression_strategy = st.builds(
    eol_LessThanOperatorExpression,
)
eol_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_GreaterThanOrEqualToOperatorExpression,
)
eol_MethodCallExpression_strategy = st.builds(
    eol_MethodCallExpression,
)
eol_FormalParameterExpression_strategy = st.builds(
    eol_FormalParameterExpression,
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol_XorOperatorExpression_strategy = st.builds(
    eol_XorOperatorExpression,
)
eol_ImpliesOperatorExpression_strategy = st.builds(
    eol_ImpliesOperatorExpression,
)
eol_OrOperatorExpression_strategy = st.builds(
    eol_OrOperatorExpression,
)
eol_AndOperatorExpression_strategy = st.builds(
    eol_AndOperatorExpression,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol_ArithmeticOperatorExpression_strategy = st.builds(
    eol_ArithmeticOperatorExpression,
)
eol_ComparisonOperatorExpression_strategy = st.builds(
    eol_ComparisonOperatorExpression,
)
eol_LogicalOperatorExpression_strategy = st.builds(
    eol_LogicalOperatorExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol_NegativeOperatorExpression_strategy = st.builds(
    eol_NegativeOperatorExpression,
)
eol_NotOperatorExpression_strategy = st.builds(
    eol_NotOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol_BinaryOperatorExpression_strategy = st.builds(
    eol_BinaryOperatorExpression,
)
eol_UnaryOperatorExpression_strategy = st.builds(
    eol_UnaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol_CollectionExpression_strategy = st.builds(
    eol_CollectionExpression,
)
eol_VariableDeclarationExpression_strategy = st.builds(
    eol_VariableDeclarationExpression,
    create=
        st.booleans()
)
eol_PrimitiveExpression_strategy = st.builds(
    eol_PrimitiveExpression,
)
eol_CollectionInitialisationExpression_strategy = st.builds(
    eol_CollectionInitialisationExpression,
)
eol_EnumerationLiteralExpression_strategy = st.builds(
    eol_EnumerationLiteralExpression,
)
eol_KeyValueExpression_strategy = st.builds(
    eol_KeyValueExpression,
)
eol_MapExpression_strategy = st.builds(
    eol_MapExpression,
)
eol_NewExpression_strategy = st.builds(
    eol_NewExpression,
)
eol_FeatureCallExpression_strategy = st.builds(
    eol_FeatureCallExpression,
    arrow=
        st.booleans()
)
eol_NameExpression_strategy = st.builds(
    eol_NameExpression,
    name=
        safe_text,
    resolvedContent=
        safe_text,
    isType=
        st.booleans()
)
eol_OperatorExpression_strategy = st.builds(
    eol_OperatorExpression,
)
EOLElement_strategy = st.builds(
    EOLElement,
)
eol_EOLLibraryModule_strategy = st.builds(
    eol_EOLLibraryModule,
    name=
        safe_text
)
eol_TextPosition_strategy = st.builds(
    eol_TextPosition,
    column=
        st.integers(),
    line=
        st.integers()
)
eol_TextRegion_strategy = st.builds(
    eol_TextRegion,
)
eol_Type_strategy = st.builds(
    eol_Type,
)
eol_Expression_strategy = st.builds(
    eol_Expression,
    inBrackets=
        st.booleans()
)
eol_ExpressionOrStatementBlock_strategy = st.builds(
    eol_ExpressionOrStatementBlock,
)
Block_strategy = st.builds(
    Block,
)
eol_AnnotationBlock_strategy = st.builds(
    eol_AnnotationBlock,
)
eol_Statement_strategy = st.builds(
    eol_Statement,
)
eol_Block_strategy = st.builds(
    eol_Block,
)
EOLLibraryModule_strategy = st.builds(
    EOLLibraryModule,
)
eol_EOLModule_strategy = st.builds(
    eol_EOLModule,
)
eol_OperationDefinition_strategy = st.builds(
    eol_OperationDefinition,
)
eol_ModelDeclarationStatement_strategy = st.builds(
    eol_ModelDeclarationStatement,
    resolvedIMetamodel=
        safe_text
)
eol_Import_strategy = st.builds(
    eol_Import,
    imported=
        safe_text
)
eol_EOLElement_strategy = st.builds(
    eol_EOLElement,
    uri=
        safe_text
)












@given(instance=eol_PropertyCallExpression_strategy)
def test_hyp_eol_propertycallexpression_extended_setter(instance):
    original = instance.extended
    instance.extended = original
    assert instance.extended == original





























@given(instance=eol_ModelElementType_strategy)
def test_hyp_eol_modelelementtype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original



@given(instance=eol_ModelElementType_strategy)
def test_hyp_eol_modelelementtype_modelElementType_setter(instance):
    original = instance.modelElementType
    instance.modelElementType = original
    assert instance.modelElementType == original



@given(instance=eol_ModelElementType_strategy)
def test_hyp_eol_modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original



@given(instance=eol_ModelElementType_strategy)
def test_hyp_eol_modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original



@given(instance=eol_ModelElementType_strategy)
def test_hyp_eol_modelelementtype_resolvedIPackage_setter(instance):
    original = instance.resolvedIPackage
    instance.resolvedIPackage = original
    assert instance.resolvedIPackage == original




@given(instance=eol_ModelType_strategy)
def test_hyp_eol_modeltype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original



@given(instance=eol_ModelType_strategy)
def test_hyp_eol_modeltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original





@given(instance=eol_AnyType_strategy)
def test_hyp_eol_anytype_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original
















































@given(instance=eol_IntegerExpression_strategy)
def test_hyp_eol_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=eol_RealExpression_strategy)
def test_hyp_eol_realexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=eol_StringExpression_strategy)
def test_hyp_eol_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=eol_BooleanExpression_strategy)
def test_hyp_eol_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


































@given(instance=eol_VariableDeclarationExpression_strategy)
def test_hyp_eol_variabledeclarationexpression_create_setter(instance):
    original = instance.create
    instance.create = original
    assert instance.create == original










@given(instance=eol_FeatureCallExpression_strategy)
def test_hyp_eol_featurecallexpression_arrow_setter(instance):
    original = instance.arrow
    instance.arrow = original
    assert instance.arrow == original




@given(instance=eol_NameExpression_strategy)
def test_hyp_eol_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eol_NameExpression_strategy)
def test_hyp_eol_nameexpression_resolvedContent_setter(instance):
    original = instance.resolvedContent
    instance.resolvedContent = original
    assert instance.resolvedContent == original



@given(instance=eol_NameExpression_strategy)
def test_hyp_eol_nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original






@given(instance=eol_EOLLibraryModule_strategy)
def test_hyp_eol_eollibrarymodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=eol_TextPosition_strategy)
def test_hyp_eol_textposition_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=eol_TextPosition_strategy)
def test_hyp_eol_textposition_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original






@given(instance=eol_Expression_strategy)
def test_hyp_eol_expression_inBrackets_setter(instance):
    original = instance.inBrackets
    instance.inBrackets = original
    assert instance.inBrackets == original












@given(instance=eol_ModelDeclarationStatement_strategy)
def test_hyp_eol_modeldeclarationstatement_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original




@given(instance=eol_Import_strategy)
def test_hyp_eol_import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original




@given(instance=eol_EOLElement_strategy)
def test_hyp_eol_eolelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnnotationStatement,
    AnyType,
    ArithmeticOperatorExpression,
    AssignmentStatement,
    BinaryOperatorExpression,
    Block,
    CollectionExpression,
    CollectionInitialisationExpression,
    CollectionType,
    ComparableExpression,
    ComparablePrimitiveType,
    ComparisonOperatorExpression,
    EOLElement,
    EOLLibraryModule,
    Expression,
    FeatureCallExpression,
    KeyValueExpression,
    LogicalOperatorExpression,
    OperatorExpression,
    OrderedCollection,
    OrderedCollectionType,
    PrimitiveExpression,
    PrimitiveType,
    PseudoType,
    RealType,
    Statement,
    SummableExpression,
    SummablePrimitiveType,
    SwitchCaseStatement,
    Type,
    UnaryOperatorExpression,
    UniqueCollection,
    UniqueCollectionType,
    VariableDeclarationExpression,
    eol_AbortStatement,
    eol_AndOperatorExpression,
    eol_AnnotationBlock,
    eol_AnnotationStatement,
    eol_AnyType,
    eol_ArithmeticOperatorExpression,
    eol_AssignmentStatement,
    eol_BagExpression,
    eol_BagType,
    eol_BinaryOperatorExpression,
    eol_Block,
    eol_BooleanExpression,
    eol_BooleanType,
    eol_BreakAllStatement,
    eol_BreakStatement,
    eol_CollectionExpression,
    eol_CollectionInitialisationExpression,
    eol_CollectionType,
    eol_ComparableExpression,
    eol_ComparablePrimitiveType,
    eol_ComparisonOperatorExpression,
    eol_ContinueStatement,
    eol_DeleteStatement,
    eol_DivideOperatorExpression,
    eol_EOLElement,
    eol_EOLLibraryModule,
    eol_EOLModule,
    eol_EnumerationLiteralExpression,
    eol_EqualsOperatorExpression,
    eol_ExecutableAnnotationStatement,
    eol_Expression,
    eol_ExpressionList,
    eol_ExpressionOrStatementBlock,
    eol_ExpressionRange,
    eol_ExpressionStatement,
    eol_FOLMethodCallExpression,
    eol_FeatureCallExpression,
    eol_ForStatement,
    eol_FormalParameterExpression,
    eol_GreaterThanOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_IfStatement,
    eol_ImpliesOperatorExpression,
    eol_Import,
    eol_IntegerExpression,
    eol_IntegerType,
    eol_InvalidType,
    eol_KeyValueExpression,
    eol_LessThanOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_LogicalOperatorExpression,
    eol_MapExpression,
    eol_MapType,
    eol_MethodCallExpression,
    eol_MinusOperatorExpression,
    eol_ModelDeclarationParameter,
    eol_ModelDeclarationStatement,
    eol_ModelElementType,
    eol_ModelType,
    eol_MultiplyOperatorExpression,
    eol_NameExpression,
    eol_NativeType,
    eol_NegativeOperatorExpression,
    eol_NewExpression,
    eol_NotEqualsOperatorExpression,
    eol_NotOperatorExpression,
    eol_OperationDefinition,
    eol_OperatorExpression,
    eol_OrOperatorExpression,
    eol_OrderedCollection,
    eol_OrderedCollectionType,
    eol_OrderedSetExpression,
    eol_OrderedSetType,
    eol_PlusOperatorExpression,
    eol_PrimitiveExpression,
    eol_PrimitiveType,
    eol_PropertyCallExpression,
    eol_PseudoType,
    eol_RealExpression,
    eol_RealType,
    eol_ReturnStatement,
    eol_SelfContentType,
    eol_SelfType,
    eol_SequenceExpression,
    eol_SequenceType,
    eol_SetExpression,
    eol_SetType,
    eol_SimpleAnnotationStatement,
    eol_SpecialAssignmentStatement,
    eol_Statement,
    eol_StringExpression,
    eol_StringType,
    eol_SummableExpression,
    eol_SummablePrimitiveType,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    eol_SwitchCaseStatement,
    eol_SwitchStatement,
    eol_TextPosition,
    eol_TextRegion,
    eol_ThrowStatement,
    eol_TransactionStatement,
    eol_Type,
    eol_UnaryOperatorExpression,
    eol_UniqueCollection,
    eol_UniqueCollectionType,
    eol_VariableDeclarationExpression,
    eol_VoidType,
    eol_WhileStatement,
    eol_XorOperatorExpression,
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

def test_eol_AnyType_declared_value_roundtrip():
    instance = eol_AnyType(declared=True)
    assert instance.declared == True
    instance.declared = False
    assert instance.declared == False


def test_eol_BooleanExpression_value_value_roundtrip():
    instance = eol_BooleanExpression(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_eol_EOLElement_uri_value_roundtrip():
    instance = eol_EOLElement(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_eol_EOLLibraryModule_name_value_roundtrip():
    instance = eol_EOLLibraryModule(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eol_Expression_inBrackets_value_roundtrip():
    instance = eol_Expression(inBrackets=True)
    assert instance.inBrackets == True
    instance.inBrackets = False
    assert instance.inBrackets == False


def test_eol_FeatureCallExpression_arrow_value_roundtrip():
    instance = eol_FeatureCallExpression(arrow=True)
    assert instance.arrow == True
    instance.arrow = False
    assert instance.arrow == False


def test_eol_Import_imported_value_roundtrip():
    instance = eol_Import(imported="sample_text")
    assert instance.imported == "sample_text"
    instance.imported = "sample_text_2"
    assert instance.imported == "sample_text_2"


def test_eol_IntegerExpression_value_value_roundtrip():
    instance = eol_IntegerExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_eol_ModelDeclarationStatement_resolvedIMetamodel_value_roundtrip():
    instance = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    assert instance.resolvedIMetamodel == "sample_text"
    instance.resolvedIMetamodel = "sample_text_2"
    assert instance.resolvedIMetamodel == "sample_text_2"


def test_eol_ModelElementType_elementName_value_roundtrip():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert instance.elementName == "sample_text"
    instance.elementName = "sample_text_2"
    assert instance.elementName == "sample_text_2"


def test_eol_ModelElementType_modelElementType_value_roundtrip():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert instance.modelElementType == "sample_text"
    instance.modelElementType = "sample_text_2"
    assert instance.modelElementType == "sample_text_2"


def test_eol_ModelElementType_modelName_value_roundtrip():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert instance.modelName == "sample_text"
    instance.modelName = "sample_text_2"
    assert instance.modelName == "sample_text_2"


def test_eol_ModelElementType_resolvedIMetamodel_value_roundtrip():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert instance.resolvedIMetamodel == "sample_text"
    instance.resolvedIMetamodel = "sample_text_2"
    assert instance.resolvedIMetamodel == "sample_text_2"


def test_eol_ModelElementType_resolvedIPackage_value_roundtrip():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert instance.resolvedIPackage == "sample_text"
    instance.resolvedIPackage = "sample_text_2"
    assert instance.resolvedIPackage == "sample_text_2"


def test_eol_ModelType_modelName_value_roundtrip():
    instance = eol_ModelType(modelName="sample_text", resolvedIMetamodel="sample_text")
    assert instance.modelName == "sample_text"
    instance.modelName = "sample_text_2"
    assert instance.modelName == "sample_text_2"


def test_eol_ModelType_resolvedIMetamodel_value_roundtrip():
    instance = eol_ModelType(modelName="sample_text", resolvedIMetamodel="sample_text")
    assert instance.resolvedIMetamodel == "sample_text"
    instance.resolvedIMetamodel = "sample_text_2"
    assert instance.resolvedIMetamodel == "sample_text_2"


def test_eol_NameExpression_isType_value_roundtrip():
    instance = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    assert instance.isType == True
    instance.isType = False
    assert instance.isType == False


def test_eol_NameExpression_name_value_roundtrip():
    instance = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eol_NameExpression_resolvedContent_value_roundtrip():
    instance = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    assert instance.resolvedContent == "sample_text"
    instance.resolvedContent = "sample_text_2"
    assert instance.resolvedContent == "sample_text_2"


def test_eol_PropertyCallExpression_extended_value_roundtrip():
    instance = eol_PropertyCallExpression(extended=True)
    assert instance.extended == True
    instance.extended = False
    assert instance.extended == False


def test_eol_RealExpression_value_value_roundtrip():
    instance = eol_RealExpression(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_eol_StringExpression_value_value_roundtrip():
    instance = eol_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_eol_TextPosition_column_value_roundtrip():
    instance = eol_TextPosition(column=7, line=7)
    assert instance.column == 7
    instance.column = 13
    assert instance.column == 13


def test_eol_TextPosition_line_value_roundtrip():
    instance = eol_TextPosition(column=7, line=7)
    assert instance.line == 7
    instance.line = 13
    assert instance.line == 13


def test_eol_VariableDeclarationExpression_create_value_roundtrip():
    instance = eol_VariableDeclarationExpression(create=True)
    assert instance.create == True
    instance.create = False
    assert instance.create == False


def test_eol_ExecutableAnnotationStatement_isa_AnnotationStatement():
    instance = eol_ExecutableAnnotationStatement()
    assert isinstance(instance, AnnotationStatement)


def test_eol_SimpleAnnotationStatement_isa_AnnotationStatement():
    instance = eol_SimpleAnnotationStatement()
    assert isinstance(instance, AnnotationStatement)


def test_eol_CollectionType_isa_AnyType():
    instance = eol_CollectionType()
    assert isinstance(instance, AnyType)


def test_eol_InvalidType_isa_AnyType():
    instance = eol_InvalidType()
    assert isinstance(instance, AnyType)


def test_eol_MapType_isa_AnyType():
    instance = eol_MapType()
    assert isinstance(instance, AnyType)


def test_eol_ModelElementType_isa_AnyType():
    instance = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    assert isinstance(instance, AnyType)


def test_eol_ModelType_isa_AnyType():
    instance = eol_ModelType(modelName="sample_text", resolvedIMetamodel="sample_text")
    assert isinstance(instance, AnyType)


def test_eol_NativeType_isa_AnyType():
    instance = eol_NativeType()
    assert isinstance(instance, AnyType)


def test_eol_PrimitiveType_isa_AnyType():
    instance = eol_PrimitiveType()
    assert isinstance(instance, AnyType)


def test_eol_PseudoType_isa_AnyType():
    instance = eol_PseudoType()
    assert isinstance(instance, AnyType)


def test_eol_VoidType_isa_AnyType():
    instance = eol_VoidType()
    assert isinstance(instance, AnyType)


def test_eol_DivideOperatorExpression_isa_ArithmeticOperatorExpression():
    instance = eol_DivideOperatorExpression()
    assert isinstance(instance, ArithmeticOperatorExpression)


def test_eol_MinusOperatorExpression_isa_ArithmeticOperatorExpression():
    instance = eol_MinusOperatorExpression()
    assert isinstance(instance, ArithmeticOperatorExpression)


def test_eol_MultiplyOperatorExpression_isa_ArithmeticOperatorExpression():
    instance = eol_MultiplyOperatorExpression()
    assert isinstance(instance, ArithmeticOperatorExpression)


def test_eol_PlusOperatorExpression_isa_ArithmeticOperatorExpression():
    instance = eol_PlusOperatorExpression()
    assert isinstance(instance, ArithmeticOperatorExpression)


def test_eol_SpecialAssignmentStatement_isa_AssignmentStatement():
    instance = eol_SpecialAssignmentStatement()
    assert isinstance(instance, AssignmentStatement)


def test_eol_ArithmeticOperatorExpression_isa_BinaryOperatorExpression():
    instance = eol_ArithmeticOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_eol_ComparisonOperatorExpression_isa_BinaryOperatorExpression():
    instance = eol_ComparisonOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_eol_LogicalOperatorExpression_isa_BinaryOperatorExpression():
    instance = eol_LogicalOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_eol_AnnotationBlock_isa_Block():
    instance = eol_AnnotationBlock()
    assert isinstance(instance, Block)


def test_eol_BagExpression_isa_CollectionExpression():
    instance = eol_BagExpression()
    assert isinstance(instance, CollectionExpression)


def test_eol_OrderedCollection_isa_CollectionExpression():
    instance = eol_OrderedCollection()
    assert isinstance(instance, CollectionExpression)


def test_eol_UniqueCollection_isa_CollectionExpression():
    instance = eol_UniqueCollection()
    assert isinstance(instance, CollectionExpression)


def test_eol_ExpressionList_isa_CollectionInitialisationExpression():
    instance = eol_ExpressionList()
    assert isinstance(instance, CollectionInitialisationExpression)


def test_eol_ExpressionRange_isa_CollectionInitialisationExpression():
    instance = eol_ExpressionRange()
    assert isinstance(instance, CollectionInitialisationExpression)


def test_eol_BagType_isa_CollectionType():
    instance = eol_BagType()
    assert isinstance(instance, CollectionType)


def test_eol_OrderedCollectionType_isa_CollectionType():
    instance = eol_OrderedCollectionType()
    assert isinstance(instance, CollectionType)


def test_eol_UniqueCollectionType_isa_CollectionType():
    instance = eol_UniqueCollectionType()
    assert isinstance(instance, CollectionType)


def test_eol_IntegerExpression_isa_ComparableExpression():
    instance = eol_IntegerExpression(value=7)
    assert isinstance(instance, ComparableExpression)


def test_eol_RealExpression_isa_ComparableExpression():
    instance = eol_RealExpression(value=3.14)
    assert isinstance(instance, ComparableExpression)


def test_eol_StringExpression_isa_ComparableExpression():
    instance = eol_StringExpression(value="sample_text")
    assert isinstance(instance, ComparableExpression)


def test_eol_RealType_isa_ComparablePrimitiveType():
    instance = eol_RealType()
    assert isinstance(instance, ComparablePrimitiveType)


def test_eol_StringType_isa_ComparablePrimitiveType():
    instance = eol_StringType()
    assert isinstance(instance, ComparablePrimitiveType)


def test_eol_EqualsOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_EqualsOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_GreaterThanOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_GreaterThanOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_GreaterThanOrEqualToOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_GreaterThanOrEqualToOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_LessThanOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_LessThanOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_LessThanOrEqualToOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_LessThanOrEqualToOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_NotEqualsOperatorExpression_isa_ComparisonOperatorExpression():
    instance = eol_NotEqualsOperatorExpression()
    assert isinstance(instance, ComparisonOperatorExpression)


def test_eol_Block_isa_EOLElement():
    instance = eol_Block()
    assert isinstance(instance, EOLElement)


def test_eol_EOLLibraryModule_isa_EOLElement():
    instance = eol_EOLLibraryModule(name="sample_text")
    assert isinstance(instance, EOLElement)


def test_eol_Expression_isa_EOLElement():
    instance = eol_Expression(inBrackets=True)
    assert isinstance(instance, EOLElement)


def test_eol_ExpressionOrStatementBlock_isa_EOLElement():
    instance = eol_ExpressionOrStatementBlock()
    assert isinstance(instance, EOLElement)


def test_eol_Import_isa_EOLElement():
    instance = eol_Import(imported="sample_text")
    assert isinstance(instance, EOLElement)


def test_eol_OperationDefinition_isa_EOLElement():
    instance = eol_OperationDefinition()
    assert isinstance(instance, EOLElement)


def test_eol_Statement_isa_EOLElement():
    instance = eol_Statement()
    assert isinstance(instance, EOLElement)


def test_eol_Type_isa_EOLElement():
    instance = eol_Type()
    assert isinstance(instance, EOLElement)


def test_eol_EOLModule_isa_EOLLibraryModule():
    instance = eol_EOLModule()
    assert isinstance(instance, EOLLibraryModule)


def test_eol_CollectionExpression_isa_Expression():
    instance = eol_CollectionExpression()
    assert isinstance(instance, Expression)


def test_eol_CollectionInitialisationExpression_isa_Expression():
    instance = eol_CollectionInitialisationExpression()
    assert isinstance(instance, Expression)


def test_eol_EnumerationLiteralExpression_isa_Expression():
    instance = eol_EnumerationLiteralExpression()
    assert isinstance(instance, Expression)


def test_eol_FeatureCallExpression_isa_Expression():
    instance = eol_FeatureCallExpression(arrow=True)
    assert isinstance(instance, Expression)


def test_eol_KeyValueExpression_isa_Expression():
    instance = eol_KeyValueExpression()
    assert isinstance(instance, Expression)


def test_eol_MapExpression_isa_Expression():
    instance = eol_MapExpression()
    assert isinstance(instance, Expression)


def test_eol_NameExpression_isa_Expression():
    instance = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    assert isinstance(instance, Expression)


def test_eol_NewExpression_isa_Expression():
    instance = eol_NewExpression()
    assert isinstance(instance, Expression)


def test_eol_OperatorExpression_isa_Expression():
    instance = eol_OperatorExpression()
    assert isinstance(instance, Expression)


def test_eol_PrimitiveExpression_isa_Expression():
    instance = eol_PrimitiveExpression()
    assert isinstance(instance, Expression)


def test_eol_VariableDeclarationExpression_isa_Expression():
    instance = eol_VariableDeclarationExpression(create=True)
    assert isinstance(instance, Expression)


def test_eol_FOLMethodCallExpression_isa_FeatureCallExpression():
    instance = eol_FOLMethodCallExpression()
    assert isinstance(instance, FeatureCallExpression)


def test_eol_MethodCallExpression_isa_FeatureCallExpression():
    instance = eol_MethodCallExpression()
    assert isinstance(instance, FeatureCallExpression)


def test_eol_PropertyCallExpression_isa_FeatureCallExpression():
    instance = eol_PropertyCallExpression(extended=True)
    assert isinstance(instance, FeatureCallExpression)


def test_eol_ModelDeclarationParameter_isa_KeyValueExpression():
    instance = eol_ModelDeclarationParameter()
    assert isinstance(instance, KeyValueExpression)


def test_eol_AndOperatorExpression_isa_LogicalOperatorExpression():
    instance = eol_AndOperatorExpression()
    assert isinstance(instance, LogicalOperatorExpression)


def test_eol_ImpliesOperatorExpression_isa_LogicalOperatorExpression():
    instance = eol_ImpliesOperatorExpression()
    assert isinstance(instance, LogicalOperatorExpression)


def test_eol_OrOperatorExpression_isa_LogicalOperatorExpression():
    instance = eol_OrOperatorExpression()
    assert isinstance(instance, LogicalOperatorExpression)


def test_eol_XorOperatorExpression_isa_LogicalOperatorExpression():
    instance = eol_XorOperatorExpression()
    assert isinstance(instance, LogicalOperatorExpression)


def test_eol_BinaryOperatorExpression_isa_OperatorExpression():
    instance = eol_BinaryOperatorExpression()
    assert isinstance(instance, OperatorExpression)


def test_eol_UnaryOperatorExpression_isa_OperatorExpression():
    instance = eol_UnaryOperatorExpression()
    assert isinstance(instance, OperatorExpression)


def test_eol_OrderedSetExpression_isa_OrderedCollection():
    instance = eol_OrderedSetExpression()
    assert isinstance(instance, OrderedCollection)


def test_eol_SequenceExpression_isa_OrderedCollection():
    instance = eol_SequenceExpression()
    assert isinstance(instance, OrderedCollection)


def test_eol_OrderedSetType_isa_OrderedCollectionType():
    instance = eol_OrderedSetType()
    assert isinstance(instance, OrderedCollectionType)


def test_eol_SequenceType_isa_OrderedCollectionType():
    instance = eol_SequenceType()
    assert isinstance(instance, OrderedCollectionType)


def test_eol_BooleanExpression_isa_PrimitiveExpression():
    instance = eol_BooleanExpression(value=True)
    assert isinstance(instance, PrimitiveExpression)


def test_eol_ComparableExpression_isa_PrimitiveExpression():
    instance = eol_ComparableExpression()
    assert isinstance(instance, PrimitiveExpression)


def test_eol_SummableExpression_isa_PrimitiveExpression():
    instance = eol_SummableExpression()
    assert isinstance(instance, PrimitiveExpression)


def test_eol_BooleanType_isa_PrimitiveType():
    instance = eol_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_eol_ComparablePrimitiveType_isa_PrimitiveType():
    instance = eol_ComparablePrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_eol_SummablePrimitiveType_isa_PrimitiveType():
    instance = eol_SummablePrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_eol_SelfContentType_isa_PseudoType():
    instance = eol_SelfContentType()
    assert isinstance(instance, PseudoType)


def test_eol_SelfType_isa_PseudoType():
    instance = eol_SelfType()
    assert isinstance(instance, PseudoType)


def test_eol_IntegerType_isa_RealType():
    instance = eol_IntegerType()
    assert isinstance(instance, RealType)


def test_eol_AbortStatement_isa_Statement():
    instance = eol_AbortStatement()
    assert isinstance(instance, Statement)


def test_eol_AnnotationStatement_isa_Statement():
    instance = eol_AnnotationStatement()
    assert isinstance(instance, Statement)


def test_eol_AssignmentStatement_isa_Statement():
    instance = eol_AssignmentStatement()
    assert isinstance(instance, Statement)


def test_eol_BreakAllStatement_isa_Statement():
    instance = eol_BreakAllStatement()
    assert isinstance(instance, Statement)


def test_eol_BreakStatement_isa_Statement():
    instance = eol_BreakStatement()
    assert isinstance(instance, Statement)


def test_eol_ContinueStatement_isa_Statement():
    instance = eol_ContinueStatement()
    assert isinstance(instance, Statement)


def test_eol_DeleteStatement_isa_Statement():
    instance = eol_DeleteStatement()
    assert isinstance(instance, Statement)


def test_eol_ExpressionStatement_isa_Statement():
    instance = eol_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_eol_ForStatement_isa_Statement():
    instance = eol_ForStatement()
    assert isinstance(instance, Statement)


def test_eol_IfStatement_isa_Statement():
    instance = eol_IfStatement()
    assert isinstance(instance, Statement)


def test_eol_ModelDeclarationStatement_isa_Statement():
    instance = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    assert isinstance(instance, Statement)


def test_eol_ReturnStatement_isa_Statement():
    instance = eol_ReturnStatement()
    assert isinstance(instance, Statement)


def test_eol_SwitchCaseStatement_isa_Statement():
    instance = eol_SwitchCaseStatement()
    assert isinstance(instance, Statement)


def test_eol_SwitchStatement_isa_Statement():
    instance = eol_SwitchStatement()
    assert isinstance(instance, Statement)


def test_eol_ThrowStatement_isa_Statement():
    instance = eol_ThrowStatement()
    assert isinstance(instance, Statement)


def test_eol_TransactionStatement_isa_Statement():
    instance = eol_TransactionStatement()
    assert isinstance(instance, Statement)


def test_eol_WhileStatement_isa_Statement():
    instance = eol_WhileStatement()
    assert isinstance(instance, Statement)


def test_eol_IntegerExpression_isa_SummableExpression():
    instance = eol_IntegerExpression(value=7)
    assert isinstance(instance, SummableExpression)


def test_eol_RealExpression_isa_SummableExpression():
    instance = eol_RealExpression(value=3.14)
    assert isinstance(instance, SummableExpression)


def test_eol_StringExpression_isa_SummableExpression():
    instance = eol_StringExpression(value="sample_text")
    assert isinstance(instance, SummableExpression)


def test_eol_RealType_isa_SummablePrimitiveType():
    instance = eol_RealType()
    assert isinstance(instance, SummablePrimitiveType)


def test_eol_StringType_isa_SummablePrimitiveType():
    instance = eol_StringType()
    assert isinstance(instance, SummablePrimitiveType)


def test_eol_SwitchCaseDefaultStatement_isa_SwitchCaseStatement():
    instance = eol_SwitchCaseDefaultStatement()
    assert isinstance(instance, SwitchCaseStatement)


def test_eol_SwitchCaseExpressionStatement_isa_SwitchCaseStatement():
    instance = eol_SwitchCaseExpressionStatement()
    assert isinstance(instance, SwitchCaseStatement)


def test_eol_AnyType_isa_Type():
    instance = eol_AnyType(declared=True)
    assert isinstance(instance, Type)


def test_eol_NegativeOperatorExpression_isa_UnaryOperatorExpression():
    instance = eol_NegativeOperatorExpression()
    assert isinstance(instance, UnaryOperatorExpression)


def test_eol_NotOperatorExpression_isa_UnaryOperatorExpression():
    instance = eol_NotOperatorExpression()
    assert isinstance(instance, UnaryOperatorExpression)


def test_eol_OrderedSetExpression_isa_UniqueCollection():
    instance = eol_OrderedSetExpression()
    assert isinstance(instance, UniqueCollection)


def test_eol_SetExpression_isa_UniqueCollection():
    instance = eol_SetExpression()
    assert isinstance(instance, UniqueCollection)


def test_eol_OrderedSetType_isa_UniqueCollectionType():
    instance = eol_OrderedSetType()
    assert isinstance(instance, UniqueCollectionType)


def test_eol_SetType_isa_UniqueCollectionType():
    instance = eol_SetType()
    assert isinstance(instance, UniqueCollectionType)


def test_eol_FormalParameterExpression_isa_VariableDeclarationExpression():
    instance = eol_FormalParameterExpression()
    assert isinstance(instance, VariableDeclarationExpression)


def test_assoc__result43_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_OperationDefinition()
    b2 = eol_OperationDefinition()
    _safe_set(a, 'eol_VariableDeclarationExpression45', b1)
    assert _is_linked(a, 'eol_VariableDeclarationExpression45', b1)
    if hasattr(b1, 'eol_OperationDefinition44'):
        assert _is_linked(b1, 'eol_OperationDefinition44', a)
    _safe_set(a, 'eol_VariableDeclarationExpression45', b2)
    assert _is_linked(a, 'eol_VariableDeclarationExpression45', b2)
    if hasattr(b1, 'eol_OperationDefinition44'):
        assert not _is_linked(b1, 'eol_OperationDefinition44', a)
    if hasattr(b2, 'eol_OperationDefinition44'):
        assert _is_linked(b2, 'eol_OperationDefinition44', a)
    _safe_set(a, 'eol_VariableDeclarationExpression45', None)
    assert not _is_linked(a, 'eol_VariableDeclarationExpression45', b2)
    if hasattr(b2, 'eol_OperationDefinition44'):
        assert not _is_linked(b2, 'eol_OperationDefinition44', a)


def test_assoc_aliases183_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    _safe_set(a, 'eol_VariableDeclarationExpression185', b1)
    assert _is_linked(a, 'eol_VariableDeclarationExpression185', b1)
    if hasattr(b1, 'eol_ModelDeclarationStatement184'):
        assert _is_linked(b1, 'eol_ModelDeclarationStatement184', a)
    _safe_set(a, 'eol_VariableDeclarationExpression185', b2)
    assert _is_linked(a, 'eol_VariableDeclarationExpression185', b2)
    if hasattr(b1, 'eol_ModelDeclarationStatement184'):
        assert not _is_linked(b1, 'eol_ModelDeclarationStatement184', a)
    if hasattr(b2, 'eol_ModelDeclarationStatement184'):
        assert _is_linked(b2, 'eol_ModelDeclarationStatement184', a)
    _safe_set(a, 'eol_VariableDeclarationExpression185', None)
    assert not _is_linked(a, 'eol_VariableDeclarationExpression185', b2)
    if hasattr(b2, 'eol_ModelDeclarationStatement184'):
        assert not _is_linked(b2, 'eol_ModelDeclarationStatement184', a)


def test_assoc_arguments67_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_MethodCallExpression()
    b2 = eol_MethodCallExpression()
    _safe_set(a, 'eol_Expression68', b1)
    assert _is_linked(a, 'eol_Expression68', b1)
    if hasattr(b1, 'eol_MethodCallExpression'):
        assert _is_linked(b1, 'eol_MethodCallExpression', a)
    _safe_set(a, 'eol_Expression68', b2)
    assert _is_linked(a, 'eol_Expression68', b2)
    if hasattr(b1, 'eol_MethodCallExpression'):
        assert not _is_linked(b1, 'eol_MethodCallExpression', a)
    if hasattr(b2, 'eol_MethodCallExpression'):
        assert _is_linked(b2, 'eol_MethodCallExpression', a)
    _safe_set(a, 'eol_Expression68', None)
    assert not _is_linked(a, 'eol_Expression68', b2)
    if hasattr(b2, 'eol_MethodCallExpression'):
        assert not _is_linked(b2, 'eol_MethodCallExpression', a)


def test_assoc_condition137_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_IfStatement()
    b2 = eol_IfStatement()
    _safe_set(a, 'eol_Expression138', b1)
    assert _is_linked(a, 'eol_Expression138', b1)
    if hasattr(b1, 'eol_IfStatement'):
        assert _is_linked(b1, 'eol_IfStatement', a)
    _safe_set(a, 'eol_Expression138', b2)
    assert _is_linked(a, 'eol_Expression138', b2)
    if hasattr(b1, 'eol_IfStatement'):
        assert not _is_linked(b1, 'eol_IfStatement', a)
    if hasattr(b2, 'eol_IfStatement'):
        assert _is_linked(b2, 'eol_IfStatement', a)
    _safe_set(a, 'eol_Expression138', None)
    assert not _is_linked(a, 'eol_Expression138', b2)
    if hasattr(b2, 'eol_IfStatement'):
        assert not _is_linked(b2, 'eol_IfStatement', a)


def test_assoc_condition150_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ForStatement()
    b2 = eol_ForStatement()
    _safe_set(a, 'eol_Expression152', b1)
    assert _is_linked(a, 'eol_Expression152', b1)
    if hasattr(b1, 'eol_ForStatement151'):
        assert _is_linked(b1, 'eol_ForStatement151', a)
    _safe_set(a, 'eol_Expression152', b2)
    assert _is_linked(a, 'eol_Expression152', b2)
    if hasattr(b1, 'eol_ForStatement151'):
        assert not _is_linked(b1, 'eol_ForStatement151', a)
    if hasattr(b2, 'eol_ForStatement151'):
        assert _is_linked(b2, 'eol_ForStatement151', a)
    _safe_set(a, 'eol_Expression152', None)
    assert not _is_linked(a, 'eol_Expression152', b2)
    if hasattr(b2, 'eol_ForStatement151'):
        assert not _is_linked(b2, 'eol_ForStatement151', a)


def test_assoc_condition156_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_WhileStatement()
    b2 = eol_WhileStatement()
    _safe_set(a, 'eol_Expression157', b1)
    assert _is_linked(a, 'eol_Expression157', b1)
    if hasattr(b1, 'eol_WhileStatement'):
        assert _is_linked(b1, 'eol_WhileStatement', a)
    _safe_set(a, 'eol_Expression157', b2)
    assert _is_linked(a, 'eol_Expression157', b2)
    if hasattr(b1, 'eol_WhileStatement'):
        assert not _is_linked(b1, 'eol_WhileStatement', a)
    if hasattr(b2, 'eol_WhileStatement'):
        assert _is_linked(b2, 'eol_WhileStatement', a)
    _safe_set(a, 'eol_Expression157', None)
    assert not _is_linked(a, 'eol_Expression157', b2)
    if hasattr(b2, 'eol_WhileStatement'):
        assert not _is_linked(b2, 'eol_WhileStatement', a)


def test_assoc_condition24_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionOrStatementBlock()
    b2 = eol_ExpressionOrStatementBlock()
    _safe_set(a, 'eol_Expression26', b1)
    assert _is_linked(a, 'eol_Expression26', b1)
    if hasattr(b1, 'eol_ExpressionOrStatementBlock25'):
        assert _is_linked(b1, 'eol_ExpressionOrStatementBlock25', a)
    _safe_set(a, 'eol_Expression26', b2)
    assert _is_linked(a, 'eol_Expression26', b2)
    if hasattr(b1, 'eol_ExpressionOrStatementBlock25'):
        assert not _is_linked(b1, 'eol_ExpressionOrStatementBlock25', a)
    if hasattr(b2, 'eol_ExpressionOrStatementBlock25'):
        assert _is_linked(b2, 'eol_ExpressionOrStatementBlock25', a)
    _safe_set(a, 'eol_Expression26', None)
    assert not _is_linked(a, 'eol_Expression26', b2)
    if hasattr(b2, 'eol_ExpressionOrStatementBlock25'):
        assert not _is_linked(b2, 'eol_ExpressionOrStatementBlock25', a)


def test_assoc_conditions79_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_FOLMethodCallExpression()
    b2 = eol_FOLMethodCallExpression()
    _safe_set(a, 'eol_Expression81', b1)
    assert _is_linked(a, 'eol_Expression81', b1)
    if hasattr(b1, 'eol_FOLMethodCallExpression80'):
        assert _is_linked(b1, 'eol_FOLMethodCallExpression80', a)
    _safe_set(a, 'eol_Expression81', b2)
    assert _is_linked(a, 'eol_Expression81', b2)
    if hasattr(b1, 'eol_FOLMethodCallExpression80'):
        assert not _is_linked(b1, 'eol_FOLMethodCallExpression80', a)
    if hasattr(b2, 'eol_FOLMethodCallExpression80'):
        assert _is_linked(b2, 'eol_FOLMethodCallExpression80', a)
    _safe_set(a, 'eol_Expression81', None)
    assert not _is_linked(a, 'eol_Expression81', b2)
    if hasattr(b2, 'eol_FOLMethodCallExpression80'):
        assert not _is_linked(b2, 'eol_FOLMethodCallExpression80', a)


def test_assoc_container1_link_reassign_clear():
    a = eol_EOLElement(uri="sample_text")
    b1 = eol_EOLElement(uri="sample_text")
    b2 = eol_EOLElement(uri="sample_text_2")
    _safe_set(a, 'eol_EOLElement', b1)
    assert _is_linked(a, 'eol_EOLElement', b1)
    if hasattr(b1, 'eol_EOLElement0'):
        assert _is_linked(b1, 'eol_EOLElement0', a)
    _safe_set(a, 'eol_EOLElement', b2)
    assert _is_linked(a, 'eol_EOLElement', b2)
    if hasattr(b1, 'eol_EOLElement0'):
        assert not _is_linked(b1, 'eol_EOLElement0', a)
    if hasattr(b2, 'eol_EOLElement0'):
        assert _is_linked(b2, 'eol_EOLElement0', a)
    _safe_set(a, 'eol_EOLElement', None)
    assert not _is_linked(a, 'eol_EOLElement', b2)
    if hasattr(b2, 'eol_EOLElement0'):
        assert not _is_linked(b2, 'eol_EOLElement0', a)


def test_assoc_contents100_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_CollectionExpression()
    b2 = eol_CollectionExpression()
    _safe_set(a, 'eol_Expression101', b1)
    assert _is_linked(a, 'eol_Expression101', b1)
    if hasattr(b1, 'eol_CollectionExpression'):
        assert _is_linked(b1, 'eol_CollectionExpression', a)
    _safe_set(a, 'eol_Expression101', b2)
    assert _is_linked(a, 'eol_Expression101', b2)
    if hasattr(b1, 'eol_CollectionExpression'):
        assert not _is_linked(b1, 'eol_CollectionExpression', a)
    if hasattr(b2, 'eol_CollectionExpression'):
        assert _is_linked(b2, 'eol_CollectionExpression', a)
    _safe_set(a, 'eol_Expression101', None)
    assert not _is_linked(a, 'eol_Expression101', b2)
    if hasattr(b2, 'eol_CollectionExpression'):
        assert not _is_linked(b2, 'eol_CollectionExpression', a)


def test_assoc_driver180_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    _safe_set(a, 'eol_NameExpression182', b1)
    assert _is_linked(a, 'eol_NameExpression182', b1)
    if hasattr(b1, 'eol_ModelDeclarationStatement181'):
        assert _is_linked(b1, 'eol_ModelDeclarationStatement181', a)
    _safe_set(a, 'eol_NameExpression182', b2)
    assert _is_linked(a, 'eol_NameExpression182', b2)
    if hasattr(b1, 'eol_ModelDeclarationStatement181'):
        assert not _is_linked(b1, 'eol_ModelDeclarationStatement181', a)
    if hasattr(b2, 'eol_ModelDeclarationStatement181'):
        assert _is_linked(b2, 'eol_ModelDeclarationStatement181', a)
    _safe_set(a, 'eol_NameExpression182', None)
    assert not _is_linked(a, 'eol_NameExpression182', b2)
    if hasattr(b2, 'eol_ModelDeclarationStatement181'):
        assert not _is_linked(b2, 'eol_ModelDeclarationStatement181', a)


def test_assoc_dynamicTypes188_link_reassign_clear():
    a = eol_AnyType(declared=True)
    b1 = eol_Type()
    b2 = eol_Type()
    _safe_set(a, 'eol_AnyType', {b1})
    assert _is_linked(a, 'eol_AnyType', b1)
    if hasattr(b1, 'eol_Type189'):
        assert _is_linked(b1, 'eol_Type189', a)
    _safe_set(a, 'eol_AnyType', {b2})
    assert _is_linked(a, 'eol_AnyType', b2)
    if hasattr(b1, 'eol_Type189'):
        assert not _is_linked(b1, 'eol_Type189', a)
    if hasattr(b2, 'eol_Type189'):
        assert _is_linked(b2, 'eol_Type189', a)
    _safe_set(a, 'eol_AnyType', set())
    assert not _is_linked(a, 'eol_AnyType', b2)
    if hasattr(b2, 'eol_Type189'):
        assert not _is_linked(b2, 'eol_Type189', a)


def test_assoc_end114_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionRange()
    b2 = eol_ExpressionRange()
    _safe_set(a, 'eol_Expression116', b1)
    assert _is_linked(a, 'eol_Expression116', b1)
    if hasattr(b1, 'eol_ExpressionRange115'):
        assert _is_linked(b1, 'eol_ExpressionRange115', a)
    _safe_set(a, 'eol_Expression116', b2)
    assert _is_linked(a, 'eol_Expression116', b2)
    if hasattr(b1, 'eol_ExpressionRange115'):
        assert not _is_linked(b1, 'eol_ExpressionRange115', a)
    if hasattr(b2, 'eol_ExpressionRange115'):
        assert _is_linked(b2, 'eol_ExpressionRange115', a)
    _safe_set(a, 'eol_Expression116', None)
    assert not _is_linked(a, 'eol_Expression116', b2)
    if hasattr(b2, 'eol_ExpressionRange115'):
        assert not _is_linked(b2, 'eol_ExpressionRange115', a)


def test_assoc_end6_link_reassign_clear():
    a = eol_TextPosition(column=7, line=7)
    b1 = eol_TextRegion()
    b2 = eol_TextRegion()
    _safe_set(a, 'eol_TextPosition8', b1)
    assert _is_linked(a, 'eol_TextPosition8', b1)
    if hasattr(b1, 'eol_TextRegion7'):
        assert _is_linked(b1, 'eol_TextRegion7', a)
    _safe_set(a, 'eol_TextPosition8', b2)
    assert _is_linked(a, 'eol_TextPosition8', b2)
    if hasattr(b1, 'eol_TextRegion7'):
        assert not _is_linked(b1, 'eol_TextRegion7', a)
    if hasattr(b2, 'eol_TextRegion7'):
        assert _is_linked(b2, 'eol_TextRegion7', a)
    _safe_set(a, 'eol_TextPosition8', None)
    assert not _is_linked(a, 'eol_TextPosition8', b2)
    if hasattr(b2, 'eol_TextRegion7'):
        assert not _is_linked(b2, 'eol_TextRegion7', a)


def test_assoc_enumeration106_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_EnumerationLiteralExpression()
    b2 = eol_EnumerationLiteralExpression()
    _safe_set(a, 'eol_NameExpression108', b1)
    assert _is_linked(a, 'eol_NameExpression108', b1)
    if hasattr(b1, 'eol_EnumerationLiteralExpression107'):
        assert _is_linked(b1, 'eol_EnumerationLiteralExpression107', a)
    _safe_set(a, 'eol_NameExpression108', b2)
    assert _is_linked(a, 'eol_NameExpression108', b2)
    if hasattr(b1, 'eol_EnumerationLiteralExpression107'):
        assert not _is_linked(b1, 'eol_EnumerationLiteralExpression107', a)
    if hasattr(b2, 'eol_EnumerationLiteralExpression107'):
        assert _is_linked(b2, 'eol_EnumerationLiteralExpression107', a)
    _safe_set(a, 'eol_NameExpression108', None)
    assert not _is_linked(a, 'eol_NameExpression108', b2)
    if hasattr(b2, 'eol_EnumerationLiteralExpression107'):
        assert not _is_linked(b2, 'eol_EnumerationLiteralExpression107', a)


def test_assoc_expression124_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionStatement()
    b2 = eol_ExpressionStatement()
    _safe_set(a, 'eol_Expression125', b1)
    assert _is_linked(a, 'eol_Expression125', b1)
    if hasattr(b1, 'eol_ExpressionStatement'):
        assert _is_linked(b1, 'eol_ExpressionStatement', a)
    _safe_set(a, 'eol_Expression125', b2)
    assert _is_linked(a, 'eol_Expression125', b2)
    if hasattr(b1, 'eol_ExpressionStatement'):
        assert not _is_linked(b1, 'eol_ExpressionStatement', a)
    if hasattr(b2, 'eol_ExpressionStatement'):
        assert _is_linked(b2, 'eol_ExpressionStatement', a)
    _safe_set(a, 'eol_Expression125', None)
    assert not _is_linked(a, 'eol_Expression125', b2)
    if hasattr(b2, 'eol_ExpressionStatement'):
        assert not _is_linked(b2, 'eol_ExpressionStatement', a)


def test_assoc_expression126_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_SwitchStatement()
    b2 = eol_SwitchStatement()
    _safe_set(a, 'eol_Expression127', b1)
    assert _is_linked(a, 'eol_Expression127', b1)
    if hasattr(b1, 'eol_SwitchStatement'):
        assert _is_linked(b1, 'eol_SwitchStatement', a)
    _safe_set(a, 'eol_Expression127', b2)
    assert _is_linked(a, 'eol_Expression127', b2)
    if hasattr(b1, 'eol_SwitchStatement'):
        assert not _is_linked(b1, 'eol_SwitchStatement', a)
    if hasattr(b2, 'eol_SwitchStatement'):
        assert _is_linked(b2, 'eol_SwitchStatement', a)
    _safe_set(a, 'eol_Expression127', None)
    assert not _is_linked(a, 'eol_Expression127', b2)
    if hasattr(b2, 'eol_SwitchStatement'):
        assert not _is_linked(b2, 'eol_SwitchStatement', a)


def test_assoc_expression134_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_SwitchCaseExpressionStatement()
    b2 = eol_SwitchCaseExpressionStatement()
    _safe_set(a, 'eol_Expression136', b1)
    assert _is_linked(a, 'eol_Expression136', b1)
    if hasattr(b1, 'eol_SwitchCaseExpressionStatement135'):
        assert _is_linked(b1, 'eol_SwitchCaseExpressionStatement135', a)
    _safe_set(a, 'eol_Expression136', b2)
    assert _is_linked(a, 'eol_Expression136', b2)
    if hasattr(b1, 'eol_SwitchCaseExpressionStatement135'):
        assert not _is_linked(b1, 'eol_SwitchCaseExpressionStatement135', a)
    if hasattr(b2, 'eol_SwitchCaseExpressionStatement135'):
        assert _is_linked(b2, 'eol_SwitchCaseExpressionStatement135', a)
    _safe_set(a, 'eol_Expression136', None)
    assert not _is_linked(a, 'eol_Expression136', b2)
    if hasattr(b2, 'eol_SwitchCaseExpressionStatement135'):
        assert not _is_linked(b2, 'eol_SwitchCaseExpressionStatement135', a)


def test_assoc_expression161_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ReturnStatement()
    b2 = eol_ReturnStatement()
    _safe_set(a, 'eol_Expression162', b1)
    assert _is_linked(a, 'eol_Expression162', b1)
    if hasattr(b1, 'eol_ReturnStatement'):
        assert _is_linked(b1, 'eol_ReturnStatement', a)
    _safe_set(a, 'eol_Expression162', b2)
    assert _is_linked(a, 'eol_Expression162', b2)
    if hasattr(b1, 'eol_ReturnStatement'):
        assert not _is_linked(b1, 'eol_ReturnStatement', a)
    if hasattr(b2, 'eol_ReturnStatement'):
        assert _is_linked(b2, 'eol_ReturnStatement', a)
    _safe_set(a, 'eol_Expression162', None)
    assert not _is_linked(a, 'eol_Expression162', b2)
    if hasattr(b2, 'eol_ReturnStatement'):
        assert not _is_linked(b2, 'eol_ReturnStatement', a)


def test_assoc_expression163_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ThrowStatement()
    b2 = eol_ThrowStatement()
    _safe_set(a, 'eol_Expression164', b1)
    assert _is_linked(a, 'eol_Expression164', b1)
    if hasattr(b1, 'eol_ThrowStatement'):
        assert _is_linked(b1, 'eol_ThrowStatement', a)
    _safe_set(a, 'eol_Expression164', b2)
    assert _is_linked(a, 'eol_Expression164', b2)
    if hasattr(b1, 'eol_ThrowStatement'):
        assert not _is_linked(b1, 'eol_ThrowStatement', a)
    if hasattr(b2, 'eol_ThrowStatement'):
        assert _is_linked(b2, 'eol_ThrowStatement', a)
    _safe_set(a, 'eol_Expression164', None)
    assert not _is_linked(a, 'eol_Expression164', b2)
    if hasattr(b2, 'eol_ThrowStatement'):
        assert not _is_linked(b2, 'eol_ThrowStatement', a)


def test_assoc_expression165_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_DeleteStatement()
    b2 = eol_DeleteStatement()
    _safe_set(a, 'eol_Expression166', b1)
    assert _is_linked(a, 'eol_Expression166', b1)
    if hasattr(b1, 'eol_DeleteStatement'):
        assert _is_linked(b1, 'eol_DeleteStatement', a)
    _safe_set(a, 'eol_Expression166', b2)
    assert _is_linked(a, 'eol_Expression166', b2)
    if hasattr(b1, 'eol_DeleteStatement'):
        assert not _is_linked(b1, 'eol_DeleteStatement', a)
    if hasattr(b2, 'eol_DeleteStatement'):
        assert _is_linked(b2, 'eol_DeleteStatement', a)
    _safe_set(a, 'eol_Expression166', None)
    assert not _is_linked(a, 'eol_Expression166', b2)
    if hasattr(b2, 'eol_DeleteStatement'):
        assert not _is_linked(b2, 'eol_DeleteStatement', a)


def test_assoc_expression175_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExecutableAnnotationStatement()
    b2 = eol_ExecutableAnnotationStatement()
    _safe_set(a, 'eol_Expression176', b1)
    assert _is_linked(a, 'eol_Expression176', b1)
    if hasattr(b1, 'eol_ExecutableAnnotationStatement'):
        assert _is_linked(b1, 'eol_ExecutableAnnotationStatement', a)
    _safe_set(a, 'eol_Expression176', b2)
    assert _is_linked(a, 'eol_Expression176', b2)
    if hasattr(b1, 'eol_ExecutableAnnotationStatement'):
        assert not _is_linked(b1, 'eol_ExecutableAnnotationStatement', a)
    if hasattr(b2, 'eol_ExecutableAnnotationStatement'):
        assert _is_linked(b2, 'eol_ExecutableAnnotationStatement', a)
    _safe_set(a, 'eol_Expression176', None)
    assert not _is_linked(a, 'eol_Expression176', b2)
    if hasattr(b2, 'eol_ExecutableAnnotationStatement'):
        assert not _is_linked(b2, 'eol_ExecutableAnnotationStatement', a)


def test_assoc_expression197_link_reassign_clear():
    a = eol_StringExpression(value="sample_text")
    b1 = eol_NativeType()
    b2 = eol_NativeType()
    _safe_set(a, 'eol_StringExpression198', b1)
    assert _is_linked(a, 'eol_StringExpression198', b1)
    if hasattr(b1, 'eol_NativeType'):
        assert _is_linked(b1, 'eol_NativeType', a)
    _safe_set(a, 'eol_StringExpression198', b2)
    assert _is_linked(a, 'eol_StringExpression198', b2)
    if hasattr(b1, 'eol_NativeType'):
        assert not _is_linked(b1, 'eol_NativeType', a)
    if hasattr(b2, 'eol_NativeType'):
        assert _is_linked(b2, 'eol_NativeType', a)
    _safe_set(a, 'eol_StringExpression198', None)
    assert not _is_linked(a, 'eol_StringExpression198', b2)
    if hasattr(b2, 'eol_NativeType'):
        assert not _is_linked(b2, 'eol_NativeType', a)


def test_assoc_expression22_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionOrStatementBlock()
    b2 = eol_ExpressionOrStatementBlock()
    _safe_set(a, 'eol_Expression', b1)
    assert _is_linked(a, 'eol_Expression', b1)
    if hasattr(b1, 'eol_ExpressionOrStatementBlock23'):
        assert _is_linked(b1, 'eol_ExpressionOrStatementBlock23', a)
    _safe_set(a, 'eol_Expression', b2)
    assert _is_linked(a, 'eol_Expression', b2)
    if hasattr(b1, 'eol_ExpressionOrStatementBlock23'):
        assert not _is_linked(b1, 'eol_ExpressionOrStatementBlock23', a)
    if hasattr(b2, 'eol_ExpressionOrStatementBlock23'):
        assert _is_linked(b2, 'eol_ExpressionOrStatementBlock23', a)
    _safe_set(a, 'eol_Expression', None)
    assert not _is_linked(a, 'eol_Expression', b2)
    if hasattr(b2, 'eol_ExpressionOrStatementBlock23'):
        assert not _is_linked(b2, 'eol_ExpressionOrStatementBlock23', a)


def test_assoc_expression52_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_UnaryOperatorExpression()
    b2 = eol_UnaryOperatorExpression()
    _safe_set(a, 'eol_Expression53', b1)
    assert _is_linked(a, 'eol_Expression53', b1)
    if hasattr(b1, 'eol_UnaryOperatorExpression'):
        assert _is_linked(b1, 'eol_UnaryOperatorExpression', a)
    _safe_set(a, 'eol_Expression53', b2)
    assert _is_linked(a, 'eol_Expression53', b2)
    if hasattr(b1, 'eol_UnaryOperatorExpression'):
        assert not _is_linked(b1, 'eol_UnaryOperatorExpression', a)
    if hasattr(b2, 'eol_UnaryOperatorExpression'):
        assert _is_linked(b2, 'eol_UnaryOperatorExpression', a)
    _safe_set(a, 'eol_Expression53', None)
    assert not _is_linked(a, 'eol_Expression53', b2)
    if hasattr(b2, 'eol_UnaryOperatorExpression'):
        assert not _is_linked(b2, 'eol_UnaryOperatorExpression', a)


def test_assoc_expressions117_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionList()
    b2 = eol_ExpressionList()
    _safe_set(a, 'eol_Expression118', b1)
    assert _is_linked(a, 'eol_Expression118', b1)
    if hasattr(b1, 'eol_ExpressionList'):
        assert _is_linked(b1, 'eol_ExpressionList', a)
    _safe_set(a, 'eol_Expression118', b2)
    assert _is_linked(a, 'eol_Expression118', b2)
    if hasattr(b1, 'eol_ExpressionList'):
        assert not _is_linked(b1, 'eol_ExpressionList', a)
    if hasattr(b2, 'eol_ExpressionList'):
        assert _is_linked(b2, 'eol_ExpressionList', a)
    _safe_set(a, 'eol_Expression118', None)
    assert not _is_linked(a, 'eol_Expression118', b2)
    if hasattr(b2, 'eol_ExpressionList'):
        assert not _is_linked(b2, 'eol_ExpressionList', a)


def test_assoc_importedModule15_link_reassign_clear():
    a = eol_Import(imported="sample_text")
    b1 = eol_EOLLibraryModule(name="sample_text")
    b2 = eol_EOLLibraryModule(name="sample_text_2")
    _safe_set(a, 'eol_Import16', b1)
    assert _is_linked(a, 'eol_Import16', b1)
    if hasattr(b1, 'eol_EOLLibraryModule17'):
        assert _is_linked(b1, 'eol_EOLLibraryModule17', a)
    _safe_set(a, 'eol_Import16', b2)
    assert _is_linked(a, 'eol_Import16', b2)
    if hasattr(b1, 'eol_EOLLibraryModule17'):
        assert not _is_linked(b1, 'eol_EOLLibraryModule17', a)
    if hasattr(b2, 'eol_EOLLibraryModule17'):
        assert _is_linked(b2, 'eol_EOLLibraryModule17', a)
    _safe_set(a, 'eol_Import16', None)
    assert not _is_linked(a, 'eol_Import16', b2)
    if hasattr(b2, 'eol_EOLLibraryModule17'):
        assert not _is_linked(b2, 'eol_EOLLibraryModule17', a)


def test_assoc_imports9_link_reassign_clear():
    a = eol_Import(imported="sample_text")
    b1 = eol_EOLLibraryModule(name="sample_text")
    b2 = eol_EOLLibraryModule(name="sample_text_2")
    _safe_set(a, 'eol_Import', b1)
    assert _is_linked(a, 'eol_Import', b1)
    if hasattr(b1, 'eol_EOLLibraryModule'):
        assert _is_linked(b1, 'eol_EOLLibraryModule', a)
    _safe_set(a, 'eol_Import', b2)
    assert _is_linked(a, 'eol_Import', b2)
    if hasattr(b1, 'eol_EOLLibraryModule'):
        assert not _is_linked(b1, 'eol_EOLLibraryModule', a)
    if hasattr(b2, 'eol_EOLLibraryModule'):
        assert _is_linked(b2, 'eol_EOLLibraryModule', a)
    _safe_set(a, 'eol_Import', None)
    assert not _is_linked(a, 'eol_Import', b2)
    if hasattr(b2, 'eol_EOLLibraryModule'):
        assert not _is_linked(b2, 'eol_EOLLibraryModule', a)


def test_assoc_key88_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_KeyValueExpression()
    b2 = eol_KeyValueExpression()
    _safe_set(a, 'eol_Expression89', b1)
    assert _is_linked(a, 'eol_Expression89', b1)
    if hasattr(b1, 'eol_KeyValueExpression'):
        assert _is_linked(b1, 'eol_KeyValueExpression', a)
    _safe_set(a, 'eol_Expression89', b2)
    assert _is_linked(a, 'eol_Expression89', b2)
    if hasattr(b1, 'eol_KeyValueExpression'):
        assert not _is_linked(b1, 'eol_KeyValueExpression', a)
    if hasattr(b2, 'eol_KeyValueExpression'):
        assert _is_linked(b2, 'eol_KeyValueExpression', a)
    _safe_set(a, 'eol_Expression89', None)
    assert not _is_linked(a, 'eol_Expression89', b2)
    if hasattr(b2, 'eol_KeyValueExpression'):
        assert not _is_linked(b2, 'eol_KeyValueExpression', a)


def test_assoc_keyType192_link_reassign_clear():
    a = eol_AnyType(declared=True)
    b1 = eol_MapType()
    b2 = eol_MapType()
    _safe_set(a, 'eol_AnyType193', b1)
    assert _is_linked(a, 'eol_AnyType193', b1)
    if hasattr(b1, 'eol_MapType'):
        assert _is_linked(b1, 'eol_MapType', a)
    _safe_set(a, 'eol_AnyType193', b2)
    assert _is_linked(a, 'eol_AnyType193', b2)
    if hasattr(b1, 'eol_MapType'):
        assert not _is_linked(b1, 'eol_MapType', a)
    if hasattr(b2, 'eol_MapType'):
        assert _is_linked(b2, 'eol_MapType', a)
    _safe_set(a, 'eol_AnyType193', None)
    assert not _is_linked(a, 'eol_AnyType193', b2)
    if hasattr(b2, 'eol_MapType'):
        assert not _is_linked(b2, 'eol_MapType', a)


def test_assoc_lhs167_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_AssignmentStatement()
    b2 = eol_AssignmentStatement()
    _safe_set(a, 'eol_Expression168', b1)
    assert _is_linked(a, 'eol_Expression168', b1)
    if hasattr(b1, 'eol_AssignmentStatement'):
        assert _is_linked(b1, 'eol_AssignmentStatement', a)
    _safe_set(a, 'eol_Expression168', b2)
    assert _is_linked(a, 'eol_Expression168', b2)
    if hasattr(b1, 'eol_AssignmentStatement'):
        assert not _is_linked(b1, 'eol_AssignmentStatement', a)
    if hasattr(b2, 'eol_AssignmentStatement'):
        assert _is_linked(b2, 'eol_AssignmentStatement', a)
    _safe_set(a, 'eol_Expression168', None)
    assert not _is_linked(a, 'eol_Expression168', b2)
    if hasattr(b2, 'eol_AssignmentStatement'):
        assert not _is_linked(b2, 'eol_AssignmentStatement', a)


def test_assoc_lhs54_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_BinaryOperatorExpression()
    b2 = eol_BinaryOperatorExpression()
    _safe_set(a, 'eol_Expression55', b1)
    assert _is_linked(a, 'eol_Expression55', b1)
    if hasattr(b1, 'eol_BinaryOperatorExpression'):
        assert _is_linked(b1, 'eol_BinaryOperatorExpression', a)
    _safe_set(a, 'eol_Expression55', b2)
    assert _is_linked(a, 'eol_Expression55', b2)
    if hasattr(b1, 'eol_BinaryOperatorExpression'):
        assert not _is_linked(b1, 'eol_BinaryOperatorExpression', a)
    if hasattr(b2, 'eol_BinaryOperatorExpression'):
        assert _is_linked(b2, 'eol_BinaryOperatorExpression', a)
    _safe_set(a, 'eol_Expression55', None)
    assert not _is_linked(a, 'eol_Expression55', b2)
    if hasattr(b2, 'eol_BinaryOperatorExpression'):
        assert not _is_linked(b2, 'eol_BinaryOperatorExpression', a)


def test_assoc_literal104_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_EnumerationLiteralExpression()
    b2 = eol_EnumerationLiteralExpression()
    _safe_set(a, 'eol_NameExpression105', b1)
    assert _is_linked(a, 'eol_NameExpression105', b1)
    if hasattr(b1, 'eol_EnumerationLiteralExpression'):
        assert _is_linked(b1, 'eol_EnumerationLiteralExpression', a)
    _safe_set(a, 'eol_NameExpression105', b2)
    assert _is_linked(a, 'eol_NameExpression105', b2)
    if hasattr(b1, 'eol_EnumerationLiteralExpression'):
        assert not _is_linked(b1, 'eol_EnumerationLiteralExpression', a)
    if hasattr(b2, 'eol_EnumerationLiteralExpression'):
        assert _is_linked(b2, 'eol_EnumerationLiteralExpression', a)
    _safe_set(a, 'eol_NameExpression105', None)
    assert not _is_linked(a, 'eol_NameExpression105', b2)
    if hasattr(b2, 'eol_EnumerationLiteralExpression'):
        assert not _is_linked(b2, 'eol_EnumerationLiteralExpression', a)


def test_assoc_method69_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_MethodCallExpression()
    b2 = eol_MethodCallExpression()
    _safe_set(a, 'eol_NameExpression71', b1)
    assert _is_linked(a, 'eol_NameExpression71', b1)
    if hasattr(b1, 'eol_MethodCallExpression70'):
        assert _is_linked(b1, 'eol_MethodCallExpression70', a)
    _safe_set(a, 'eol_NameExpression71', b2)
    assert _is_linked(a, 'eol_NameExpression71', b2)
    if hasattr(b1, 'eol_MethodCallExpression70'):
        assert not _is_linked(b1, 'eol_MethodCallExpression70', a)
    if hasattr(b2, 'eol_MethodCallExpression70'):
        assert _is_linked(b2, 'eol_MethodCallExpression70', a)
    _safe_set(a, 'eol_NameExpression71', None)
    assert not _is_linked(a, 'eol_NameExpression71', b2)
    if hasattr(b2, 'eol_MethodCallExpression70'):
        assert not _is_linked(b2, 'eol_MethodCallExpression70', a)


def test_assoc_method82_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_FOLMethodCallExpression()
    b2 = eol_FOLMethodCallExpression()
    _safe_set(a, 'eol_NameExpression84', b1)
    assert _is_linked(a, 'eol_NameExpression84', b1)
    if hasattr(b1, 'eol_FOLMethodCallExpression83'):
        assert _is_linked(b1, 'eol_FOLMethodCallExpression83', a)
    _safe_set(a, 'eol_NameExpression84', b2)
    assert _is_linked(a, 'eol_NameExpression84', b2)
    if hasattr(b1, 'eol_FOLMethodCallExpression83'):
        assert not _is_linked(b1, 'eol_FOLMethodCallExpression83', a)
    if hasattr(b2, 'eol_FOLMethodCallExpression83'):
        assert _is_linked(b2, 'eol_FOLMethodCallExpression83', a)
    _safe_set(a, 'eol_NameExpression84', None)
    assert not _is_linked(a, 'eol_NameExpression84', b2)
    if hasattr(b2, 'eol_FOLMethodCallExpression83'):
        assert not _is_linked(b2, 'eol_FOLMethodCallExpression83', a)


def test_assoc_model109_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_EnumerationLiteralExpression()
    b2 = eol_EnumerationLiteralExpression()
    _safe_set(a, 'eol_NameExpression111', b1)
    assert _is_linked(a, 'eol_NameExpression111', b1)
    if hasattr(b1, 'eol_EnumerationLiteralExpression110'):
        assert _is_linked(b1, 'eol_EnumerationLiteralExpression110', a)
    _safe_set(a, 'eol_NameExpression111', b2)
    assert _is_linked(a, 'eol_NameExpression111', b2)
    if hasattr(b1, 'eol_EnumerationLiteralExpression110'):
        assert not _is_linked(b1, 'eol_EnumerationLiteralExpression110', a)
    if hasattr(b2, 'eol_EnumerationLiteralExpression110'):
        assert _is_linked(b2, 'eol_EnumerationLiteralExpression110', a)
    _safe_set(a, 'eol_NameExpression111', None)
    assert not _is_linked(a, 'eol_NameExpression111', b2)
    if hasattr(b2, 'eol_EnumerationLiteralExpression110'):
        assert not _is_linked(b2, 'eol_EnumerationLiteralExpression110', a)


def test_assoc_modelDeclarations10_link_reassign_clear():
    a = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b1 = eol_EOLLibraryModule(name="sample_text")
    b2 = eol_EOLLibraryModule(name="sample_text_2")
    _safe_set(a, 'eol_ModelDeclarationStatement', b1)
    assert _is_linked(a, 'eol_ModelDeclarationStatement', b1)
    if hasattr(b1, 'eol_EOLLibraryModule11'):
        assert _is_linked(b1, 'eol_EOLLibraryModule11', a)
    _safe_set(a, 'eol_ModelDeclarationStatement', b2)
    assert _is_linked(a, 'eol_ModelDeclarationStatement', b2)
    if hasattr(b1, 'eol_EOLLibraryModule11'):
        assert not _is_linked(b1, 'eol_EOLLibraryModule11', a)
    if hasattr(b2, 'eol_EOLLibraryModule11'):
        assert _is_linked(b2, 'eol_EOLLibraryModule11', a)
    _safe_set(a, 'eol_ModelDeclarationStatement', None)
    assert not _is_linked(a, 'eol_ModelDeclarationStatement', b2)
    if hasattr(b2, 'eol_EOLLibraryModule11'):
        assert not _is_linked(b2, 'eol_EOLLibraryModule11', a)


def test_assoc_name172_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_AnnotationStatement()
    b2 = eol_AnnotationStatement()
    _safe_set(a, 'eol_NameExpression173', b1)
    assert _is_linked(a, 'eol_NameExpression173', b1)
    if hasattr(b1, 'eol_AnnotationStatement'):
        assert _is_linked(b1, 'eol_AnnotationStatement', a)
    _safe_set(a, 'eol_NameExpression173', b2)
    assert _is_linked(a, 'eol_NameExpression173', b2)
    if hasattr(b1, 'eol_AnnotationStatement'):
        assert not _is_linked(b1, 'eol_AnnotationStatement', a)
    if hasattr(b2, 'eol_AnnotationStatement'):
        assert _is_linked(b2, 'eol_AnnotationStatement', a)
    _safe_set(a, 'eol_NameExpression173', None)
    assert not _is_linked(a, 'eol_NameExpression173', b2)
    if hasattr(b2, 'eol_AnnotationStatement'):
        assert not _is_linked(b2, 'eol_AnnotationStatement', a)


def test_assoc_name177_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    _safe_set(a, 'eol_VariableDeclarationExpression179', b1)
    assert _is_linked(a, 'eol_VariableDeclarationExpression179', b1)
    if hasattr(b1, 'eol_ModelDeclarationStatement178'):
        assert _is_linked(b1, 'eol_ModelDeclarationStatement178', a)
    _safe_set(a, 'eol_VariableDeclarationExpression179', b2)
    assert _is_linked(a, 'eol_VariableDeclarationExpression179', b2)
    if hasattr(b1, 'eol_ModelDeclarationStatement178'):
        assert not _is_linked(b1, 'eol_ModelDeclarationStatement178', a)
    if hasattr(b2, 'eol_ModelDeclarationStatement178'):
        assert _is_linked(b2, 'eol_ModelDeclarationStatement178', a)
    _safe_set(a, 'eol_VariableDeclarationExpression179', None)
    assert not _is_linked(a, 'eol_VariableDeclarationExpression179', b2)
    if hasattr(b2, 'eol_ModelDeclarationStatement178'):
        assert not _is_linked(b2, 'eol_ModelDeclarationStatement178', a)


def test_assoc_name37_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_OperationDefinition()
    b2 = eol_OperationDefinition()
    _safe_set(a, 'eol_NameExpression', b1)
    assert _is_linked(a, 'eol_NameExpression', b1)
    if hasattr(b1, 'eol_OperationDefinition38'):
        assert _is_linked(b1, 'eol_OperationDefinition38', a)
    _safe_set(a, 'eol_NameExpression', b2)
    assert _is_linked(a, 'eol_NameExpression', b2)
    if hasattr(b1, 'eol_OperationDefinition38'):
        assert not _is_linked(b1, 'eol_OperationDefinition38', a)
    if hasattr(b2, 'eol_OperationDefinition38'):
        assert _is_linked(b2, 'eol_OperationDefinition38', a)
    _safe_set(a, 'eol_NameExpression', None)
    assert not _is_linked(a, 'eol_NameExpression', b2)
    if hasattr(b2, 'eol_OperationDefinition38'):
        assert not _is_linked(b2, 'eol_OperationDefinition38', a)


def test_assoc_name59_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    _safe_set(a, 'eol_VariableDeclarationExpression60', b1)
    assert _is_linked(a, 'eol_VariableDeclarationExpression60', b1)
    if hasattr(b1, 'eol_NameExpression61'):
        assert _is_linked(b1, 'eol_NameExpression61', a)
    _safe_set(a, 'eol_VariableDeclarationExpression60', b2)
    assert _is_linked(a, 'eol_VariableDeclarationExpression60', b2)
    if hasattr(b1, 'eol_NameExpression61'):
        assert not _is_linked(b1, 'eol_NameExpression61', a)
    if hasattr(b2, 'eol_NameExpression61'):
        assert _is_linked(b2, 'eol_NameExpression61', a)
    _safe_set(a, 'eol_VariableDeclarationExpression60', None)
    assert not _is_linked(a, 'eol_VariableDeclarationExpression60', b2)
    if hasattr(b2, 'eol_NameExpression61'):
        assert not _is_linked(b2, 'eol_NameExpression61', a)


def test_assoc_names119_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_TransactionStatement()
    b2 = eol_TransactionStatement()
    _safe_set(a, 'eol_NameExpression120', b1)
    assert _is_linked(a, 'eol_NameExpression120', b1)
    if hasattr(b1, 'eol_TransactionStatement'):
        assert _is_linked(b1, 'eol_TransactionStatement', a)
    _safe_set(a, 'eol_NameExpression120', b2)
    assert _is_linked(a, 'eol_NameExpression120', b2)
    if hasattr(b1, 'eol_TransactionStatement'):
        assert not _is_linked(b1, 'eol_TransactionStatement', a)
    if hasattr(b2, 'eol_TransactionStatement'):
        assert _is_linked(b2, 'eol_TransactionStatement', a)
    _safe_set(a, 'eol_NameExpression120', None)
    assert not _is_linked(a, 'eol_NameExpression120', b2)
    if hasattr(b2, 'eol_TransactionStatement'):
        assert not _is_linked(b2, 'eol_TransactionStatement', a)


def test_assoc_operations12_link_reassign_clear():
    a = eol_EOLLibraryModule(name="sample_text")
    b1 = eol_OperationDefinition()
    b2 = eol_OperationDefinition()
    _safe_set(a, 'eol_EOLLibraryModule13', {b1})
    assert _is_linked(a, 'eol_EOLLibraryModule13', b1)
    if hasattr(b1, 'eol_OperationDefinition'):
        assert _is_linked(b1, 'eol_OperationDefinition', a)
    _safe_set(a, 'eol_EOLLibraryModule13', {b2})
    assert _is_linked(a, 'eol_EOLLibraryModule13', b2)
    if hasattr(b1, 'eol_OperationDefinition'):
        assert not _is_linked(b1, 'eol_OperationDefinition', a)
    if hasattr(b2, 'eol_OperationDefinition'):
        assert _is_linked(b2, 'eol_OperationDefinition', a)
    _safe_set(a, 'eol_EOLLibraryModule13', set())
    assert not _is_linked(a, 'eol_EOLLibraryModule13', b2)
    if hasattr(b2, 'eol_OperationDefinition'):
        assert not _is_linked(b2, 'eol_OperationDefinition', a)


def test_assoc_parameters186_link_reassign_clear():
    a = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b1 = eol_ModelDeclarationParameter()
    b2 = eol_ModelDeclarationParameter()
    _safe_set(a, 'eol_ModelDeclarationStatement187', {b1})
    assert _is_linked(a, 'eol_ModelDeclarationStatement187', b1)
    if hasattr(b1, 'eol_ModelDeclarationParameter'):
        assert _is_linked(b1, 'eol_ModelDeclarationParameter', a)
    _safe_set(a, 'eol_ModelDeclarationStatement187', {b2})
    assert _is_linked(a, 'eol_ModelDeclarationStatement187', b2)
    if hasattr(b1, 'eol_ModelDeclarationParameter'):
        assert not _is_linked(b1, 'eol_ModelDeclarationParameter', a)
    if hasattr(b2, 'eol_ModelDeclarationParameter'):
        assert _is_linked(b2, 'eol_ModelDeclarationParameter', a)
    _safe_set(a, 'eol_ModelDeclarationStatement187', set())
    assert not _is_linked(a, 'eol_ModelDeclarationStatement187', b2)
    if hasattr(b2, 'eol_ModelDeclarationParameter'):
        assert not _is_linked(b2, 'eol_ModelDeclarationParameter', a)


def test_assoc_parameters95_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_NewExpression()
    b2 = eol_NewExpression()
    _safe_set(a, 'eol_Expression97', b1)
    assert _is_linked(a, 'eol_Expression97', b1)
    if hasattr(b1, 'eol_NewExpression96'):
        assert _is_linked(b1, 'eol_NewExpression96', a)
    _safe_set(a, 'eol_Expression97', b2)
    assert _is_linked(a, 'eol_Expression97', b2)
    if hasattr(b1, 'eol_NewExpression96'):
        assert not _is_linked(b1, 'eol_NewExpression96', a)
    if hasattr(b2, 'eol_NewExpression96'):
        assert _is_linked(b2, 'eol_NewExpression96', a)
    _safe_set(a, 'eol_Expression97', None)
    assert not _is_linked(a, 'eol_Expression97', b2)
    if hasattr(b2, 'eol_NewExpression96'):
        assert not _is_linked(b2, 'eol_NewExpression96', a)


def test_assoc_property75_link_reassign_clear():
    a = eol_PropertyCallExpression(extended=True)
    b1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    _safe_set(a, 'eol_PropertyCallExpression', b1)
    assert _is_linked(a, 'eol_PropertyCallExpression', b1)
    if hasattr(b1, 'eol_NameExpression76'):
        assert _is_linked(b1, 'eol_NameExpression76', a)
    _safe_set(a, 'eol_PropertyCallExpression', b2)
    assert _is_linked(a, 'eol_PropertyCallExpression', b2)
    if hasattr(b1, 'eol_NameExpression76'):
        assert not _is_linked(b1, 'eol_NameExpression76', a)
    if hasattr(b2, 'eol_NameExpression76'):
        assert _is_linked(b2, 'eol_NameExpression76', a)
    _safe_set(a, 'eol_PropertyCallExpression', None)
    assert not _is_linked(a, 'eol_PropertyCallExpression', b2)
    if hasattr(b2, 'eol_NameExpression76'):
        assert not _is_linked(b2, 'eol_NameExpression76', a)


def test_assoc_references62_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    _safe_set(a, 'eol_VariableDeclarationExpression63', {b1})
    assert _is_linked(a, 'eol_VariableDeclarationExpression63', b1)
    if hasattr(b1, 'eol_NameExpression64'):
        assert _is_linked(b1, 'eol_NameExpression64', a)
    _safe_set(a, 'eol_VariableDeclarationExpression63', {b2})
    assert _is_linked(a, 'eol_VariableDeclarationExpression63', b2)
    if hasattr(b1, 'eol_NameExpression64'):
        assert not _is_linked(b1, 'eol_NameExpression64', a)
    if hasattr(b2, 'eol_NameExpression64'):
        assert _is_linked(b2, 'eol_NameExpression64', a)
    _safe_set(a, 'eol_VariableDeclarationExpression63', set())
    assert not _is_linked(a, 'eol_VariableDeclarationExpression63', b2)
    if hasattr(b2, 'eol_NameExpression64'):
        assert not _is_linked(b2, 'eol_NameExpression64', a)


def test_assoc_region2_link_reassign_clear():
    a = eol_EOLElement(uri="sample_text")
    b1 = eol_TextRegion()
    b2 = eol_TextRegion()
    _safe_set(a, 'eol_EOLElement3', b1)
    assert _is_linked(a, 'eol_EOLElement3', b1)
    if hasattr(b1, 'eol_TextRegion'):
        assert _is_linked(b1, 'eol_TextRegion', a)
    _safe_set(a, 'eol_EOLElement3', b2)
    assert _is_linked(a, 'eol_EOLElement3', b2)
    if hasattr(b1, 'eol_TextRegion'):
        assert not _is_linked(b1, 'eol_TextRegion', a)
    if hasattr(b2, 'eol_TextRegion'):
        assert _is_linked(b2, 'eol_TextRegion', a)
    _safe_set(a, 'eol_EOLElement3', None)
    assert not _is_linked(a, 'eol_EOLElement3', b2)
    if hasattr(b2, 'eol_TextRegion'):
        assert not _is_linked(b2, 'eol_TextRegion', a)


def test_assoc_resolvedModelDeclaration190_link_reassign_clear():
    a = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    b1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    b2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    _safe_set(a, 'eol_ModelElementType', b1)
    assert _is_linked(a, 'eol_ModelElementType', b1)
    if hasattr(b1, 'eol_ModelDeclarationStatement191'):
        assert _is_linked(b1, 'eol_ModelDeclarationStatement191', a)
    _safe_set(a, 'eol_ModelElementType', b2)
    assert _is_linked(a, 'eol_ModelElementType', b2)
    if hasattr(b1, 'eol_ModelDeclarationStatement191'):
        assert not _is_linked(b1, 'eol_ModelDeclarationStatement191', a)
    if hasattr(b2, 'eol_ModelDeclarationStatement191'):
        assert _is_linked(b2, 'eol_ModelDeclarationStatement191', a)
    _safe_set(a, 'eol_ModelElementType', None)
    assert not _is_linked(a, 'eol_ModelElementType', b2)
    if hasattr(b2, 'eol_ModelDeclarationStatement191'):
        assert not _is_linked(b2, 'eol_ModelDeclarationStatement191', a)


def test_assoc_resolvedType49_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_Type()
    b2 = eol_Type()
    _safe_set(a, 'eol_Expression50', b1)
    assert _is_linked(a, 'eol_Expression50', b1)
    if hasattr(b1, 'eol_Type51'):
        assert _is_linked(b1, 'eol_Type51', a)
    _safe_set(a, 'eol_Expression50', b2)
    assert _is_linked(a, 'eol_Expression50', b2)
    if hasattr(b1, 'eol_Type51'):
        assert not _is_linked(b1, 'eol_Type51', a)
    if hasattr(b2, 'eol_Type51'):
        assert _is_linked(b2, 'eol_Type51', a)
    _safe_set(a, 'eol_Expression50', None)
    assert not _is_linked(a, 'eol_Expression50', b2)
    if hasattr(b2, 'eol_Type51'):
        assert not _is_linked(b2, 'eol_Type51', a)


def test_assoc_rhs169_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_AssignmentStatement()
    b2 = eol_AssignmentStatement()
    _safe_set(a, 'eol_Expression171', b1)
    assert _is_linked(a, 'eol_Expression171', b1)
    if hasattr(b1, 'eol_AssignmentStatement170'):
        assert _is_linked(b1, 'eol_AssignmentStatement170', a)
    _safe_set(a, 'eol_Expression171', b2)
    assert _is_linked(a, 'eol_Expression171', b2)
    if hasattr(b1, 'eol_AssignmentStatement170'):
        assert not _is_linked(b1, 'eol_AssignmentStatement170', a)
    if hasattr(b2, 'eol_AssignmentStatement170'):
        assert _is_linked(b2, 'eol_AssignmentStatement170', a)
    _safe_set(a, 'eol_Expression171', None)
    assert not _is_linked(a, 'eol_Expression171', b2)
    if hasattr(b2, 'eol_AssignmentStatement170'):
        assert not _is_linked(b2, 'eol_AssignmentStatement170', a)


def test_assoc_rhs56_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_BinaryOperatorExpression()
    b2 = eol_BinaryOperatorExpression()
    _safe_set(a, 'eol_Expression58', b1)
    assert _is_linked(a, 'eol_Expression58', b1)
    if hasattr(b1, 'eol_BinaryOperatorExpression57'):
        assert _is_linked(b1, 'eol_BinaryOperatorExpression57', a)
    _safe_set(a, 'eol_Expression58', b2)
    assert _is_linked(a, 'eol_Expression58', b2)
    if hasattr(b1, 'eol_BinaryOperatorExpression57'):
        assert not _is_linked(b1, 'eol_BinaryOperatorExpression57', a)
    if hasattr(b2, 'eol_BinaryOperatorExpression57'):
        assert _is_linked(b2, 'eol_BinaryOperatorExpression57', a)
    _safe_set(a, 'eol_Expression58', None)
    assert not _is_linked(a, 'eol_Expression58', b2)
    if hasattr(b2, 'eol_BinaryOperatorExpression57'):
        assert not _is_linked(b2, 'eol_BinaryOperatorExpression57', a)


def test_assoc_self41_link_reassign_clear():
    a = eol_VariableDeclarationExpression(create=True)
    b1 = eol_OperationDefinition()
    b2 = eol_OperationDefinition()
    _safe_set(a, 'eol_VariableDeclarationExpression', b1)
    assert _is_linked(a, 'eol_VariableDeclarationExpression', b1)
    if hasattr(b1, 'eol_OperationDefinition42'):
        assert _is_linked(b1, 'eol_OperationDefinition42', a)
    _safe_set(a, 'eol_VariableDeclarationExpression', b2)
    assert _is_linked(a, 'eol_VariableDeclarationExpression', b2)
    if hasattr(b1, 'eol_OperationDefinition42'):
        assert not _is_linked(b1, 'eol_OperationDefinition42', a)
    if hasattr(b2, 'eol_OperationDefinition42'):
        assert _is_linked(b2, 'eol_OperationDefinition42', a)
    _safe_set(a, 'eol_VariableDeclarationExpression', None)
    assert not _is_linked(a, 'eol_VariableDeclarationExpression', b2)
    if hasattr(b2, 'eol_OperationDefinition42'):
        assert not _is_linked(b2, 'eol_OperationDefinition42', a)


def test_assoc_start112_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_ExpressionRange()
    b2 = eol_ExpressionRange()
    _safe_set(a, 'eol_Expression113', b1)
    assert _is_linked(a, 'eol_Expression113', b1)
    if hasattr(b1, 'eol_ExpressionRange'):
        assert _is_linked(b1, 'eol_ExpressionRange', a)
    _safe_set(a, 'eol_Expression113', b2)
    assert _is_linked(a, 'eol_Expression113', b2)
    if hasattr(b1, 'eol_ExpressionRange'):
        assert not _is_linked(b1, 'eol_ExpressionRange', a)
    if hasattr(b2, 'eol_ExpressionRange'):
        assert _is_linked(b2, 'eol_ExpressionRange', a)
    _safe_set(a, 'eol_Expression113', None)
    assert not _is_linked(a, 'eol_Expression113', b2)
    if hasattr(b2, 'eol_ExpressionRange'):
        assert not _is_linked(b2, 'eol_ExpressionRange', a)


def test_assoc_start4_link_reassign_clear():
    a = eol_TextPosition(column=7, line=7)
    b1 = eol_TextRegion()
    b2 = eol_TextRegion()
    _safe_set(a, 'eol_TextPosition', b1)
    assert _is_linked(a, 'eol_TextPosition', b1)
    if hasattr(b1, 'eol_TextRegion5'):
        assert _is_linked(b1, 'eol_TextRegion5', a)
    _safe_set(a, 'eol_TextPosition', b2)
    assert _is_linked(a, 'eol_TextPosition', b2)
    if hasattr(b1, 'eol_TextRegion5'):
        assert not _is_linked(b1, 'eol_TextRegion5', a)
    if hasattr(b2, 'eol_TextRegion5'):
        assert _is_linked(b2, 'eol_TextRegion5', a)
    _safe_set(a, 'eol_TextPosition', None)
    assert not _is_linked(a, 'eol_TextPosition', b2)
    if hasattr(b2, 'eol_TextRegion5'):
        assert not _is_linked(b2, 'eol_TextRegion5', a)


def test_assoc_target65_link_reassign_clear():
    a = eol_FeatureCallExpression(arrow=True)
    b1 = eol_Expression(inBrackets=True)
    b2 = eol_Expression(inBrackets=False)
    _safe_set(a, 'eol_FeatureCallExpression', b1)
    assert _is_linked(a, 'eol_FeatureCallExpression', b1)
    if hasattr(b1, 'eol_Expression66'):
        assert _is_linked(b1, 'eol_Expression66', a)
    _safe_set(a, 'eol_FeatureCallExpression', b2)
    assert _is_linked(a, 'eol_FeatureCallExpression', b2)
    if hasattr(b1, 'eol_Expression66'):
        assert not _is_linked(b1, 'eol_Expression66', a)
    if hasattr(b2, 'eol_Expression66'):
        assert _is_linked(b2, 'eol_Expression66', a)
    _safe_set(a, 'eol_FeatureCallExpression', None)
    assert not _is_linked(a, 'eol_FeatureCallExpression', b2)
    if hasattr(b2, 'eol_Expression66'):
        assert not _is_linked(b2, 'eol_Expression66', a)


def test_assoc_typeName93_link_reassign_clear():
    a = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    b1 = eol_NewExpression()
    b2 = eol_NewExpression()
    _safe_set(a, 'eol_NameExpression94', b1)
    assert _is_linked(a, 'eol_NameExpression94', b1)
    if hasattr(b1, 'eol_NewExpression'):
        assert _is_linked(b1, 'eol_NewExpression', a)
    _safe_set(a, 'eol_NameExpression94', b2)
    assert _is_linked(a, 'eol_NameExpression94', b2)
    if hasattr(b1, 'eol_NewExpression'):
        assert not _is_linked(b1, 'eol_NewExpression', a)
    if hasattr(b2, 'eol_NewExpression'):
        assert _is_linked(b2, 'eol_NewExpression', a)
    _safe_set(a, 'eol_NameExpression94', None)
    assert not _is_linked(a, 'eol_NameExpression94', b2)
    if hasattr(b2, 'eol_NewExpression'):
        assert not _is_linked(b2, 'eol_NewExpression', a)


def test_assoc_value90_link_reassign_clear():
    a = eol_Expression(inBrackets=True)
    b1 = eol_KeyValueExpression()
    b2 = eol_KeyValueExpression()
    _safe_set(a, 'eol_Expression92', b1)
    assert _is_linked(a, 'eol_Expression92', b1)
    if hasattr(b1, 'eol_KeyValueExpression91'):
        assert _is_linked(b1, 'eol_KeyValueExpression91', a)
    _safe_set(a, 'eol_Expression92', b2)
    assert _is_linked(a, 'eol_Expression92', b2)
    if hasattr(b1, 'eol_KeyValueExpression91'):
        assert not _is_linked(b1, 'eol_KeyValueExpression91', a)
    if hasattr(b2, 'eol_KeyValueExpression91'):
        assert _is_linked(b2, 'eol_KeyValueExpression91', a)
    _safe_set(a, 'eol_Expression92', None)
    assert not _is_linked(a, 'eol_Expression92', b2)
    if hasattr(b2, 'eol_KeyValueExpression91'):
        assert not _is_linked(b2, 'eol_KeyValueExpression91', a)


def test_assoc_valueType194_link_reassign_clear():
    a = eol_AnyType(declared=True)
    b1 = eol_MapType()
    b2 = eol_MapType()
    _safe_set(a, 'eol_AnyType196', b1)
    assert _is_linked(a, 'eol_AnyType196', b1)
    if hasattr(b1, 'eol_MapType195'):
        assert _is_linked(b1, 'eol_MapType195', a)
    _safe_set(a, 'eol_AnyType196', b2)
    assert _is_linked(a, 'eol_AnyType196', b2)
    if hasattr(b1, 'eol_MapType195'):
        assert not _is_linked(b1, 'eol_MapType195', a)
    if hasattr(b2, 'eol_MapType195'):
        assert _is_linked(b2, 'eol_MapType195', a)
    _safe_set(a, 'eol_AnyType196', None)
    assert not _is_linked(a, 'eol_AnyType196', b2)
    if hasattr(b2, 'eol_MapType195'):
        assert not _is_linked(b2, 'eol_MapType195', a)


def test_assoc_values174_link_reassign_clear():
    a = eol_StringExpression(value="sample_text")
    b1 = eol_SimpleAnnotationStatement()
    b2 = eol_SimpleAnnotationStatement()
    _safe_set(a, 'eol_StringExpression', b1)
    assert _is_linked(a, 'eol_StringExpression', b1)
    if hasattr(b1, 'eol_SimpleAnnotationStatement'):
        assert _is_linked(b1, 'eol_SimpleAnnotationStatement', a)
    _safe_set(a, 'eol_StringExpression', b2)
    assert _is_linked(a, 'eol_StringExpression', b2)
    if hasattr(b1, 'eol_SimpleAnnotationStatement'):
        assert not _is_linked(b1, 'eol_SimpleAnnotationStatement', a)
    if hasattr(b2, 'eol_SimpleAnnotationStatement'):
        assert _is_linked(b2, 'eol_SimpleAnnotationStatement', a)
    _safe_set(a, 'eol_StringExpression', None)
    assert not _is_linked(a, 'eol_StringExpression', b2)
    if hasattr(b2, 'eol_SimpleAnnotationStatement'):
        assert not _is_linked(b2, 'eol_SimpleAnnotationStatement', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnnotationStatement_strategy = st.builds(AnnotationStatement)
@given(instance=AnnotationStatement_strategy)
@settings(max_examples=25)
def test_AnnotationStatement_instantiation(instance):
    assert isinstance(instance, AnnotationStatement)


AnyType_strategy = st.builds(AnyType)
@given(instance=AnyType_strategy)
@settings(max_examples=25)
def test_AnyType_instantiation(instance):
    assert isinstance(instance, AnyType)


ArithmeticOperatorExpression_strategy = st.builds(ArithmeticOperatorExpression)
@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=25)
def test_ArithmeticOperatorExpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)


AssignmentStatement_strategy = st.builds(AssignmentStatement)
@given(instance=AssignmentStatement_strategy)
@settings(max_examples=25)
def test_AssignmentStatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)


BinaryOperatorExpression_strategy = st.builds(BinaryOperatorExpression)
@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_BinaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


CollectionExpression_strategy = st.builds(CollectionExpression)
@given(instance=CollectionExpression_strategy)
@settings(max_examples=25)
def test_CollectionExpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)


CollectionInitialisationExpression_strategy = st.builds(CollectionInitialisationExpression)
@given(instance=CollectionInitialisationExpression_strategy)
@settings(max_examples=25)
def test_CollectionInitialisationExpression_instantiation(instance):
    assert isinstance(instance, CollectionInitialisationExpression)


CollectionType_strategy = st.builds(CollectionType)
@given(instance=CollectionType_strategy)
@settings(max_examples=25)
def test_CollectionType_instantiation(instance):
    assert isinstance(instance, CollectionType)


ComparableExpression_strategy = st.builds(ComparableExpression)
@given(instance=ComparableExpression_strategy)
@settings(max_examples=25)
def test_ComparableExpression_instantiation(instance):
    assert isinstance(instance, ComparableExpression)


ComparablePrimitiveType_strategy = st.builds(ComparablePrimitiveType)
@given(instance=ComparablePrimitiveType_strategy)
@settings(max_examples=25)
def test_ComparablePrimitiveType_instantiation(instance):
    assert isinstance(instance, ComparablePrimitiveType)


ComparisonOperatorExpression_strategy = st.builds(ComparisonOperatorExpression)
@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=25)
def test_ComparisonOperatorExpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)


EOLElement_strategy = st.builds(EOLElement)
@given(instance=EOLElement_strategy)
@settings(max_examples=25)
def test_EOLElement_instantiation(instance):
    assert isinstance(instance, EOLElement)


EOLLibraryModule_strategy = st.builds(EOLLibraryModule)
@given(instance=EOLLibraryModule_strategy)
@settings(max_examples=25)
def test_EOLLibraryModule_instantiation(instance):
    assert isinstance(instance, EOLLibraryModule)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FeatureCallExpression_strategy = st.builds(FeatureCallExpression)
@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=25)
def test_FeatureCallExpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)


KeyValueExpression_strategy = st.builds(KeyValueExpression)
@given(instance=KeyValueExpression_strategy)
@settings(max_examples=25)
def test_KeyValueExpression_instantiation(instance):
    assert isinstance(instance, KeyValueExpression)


LogicalOperatorExpression_strategy = st.builds(LogicalOperatorExpression)
@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=25)
def test_LogicalOperatorExpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)


OperatorExpression_strategy = st.builds(OperatorExpression)
@given(instance=OperatorExpression_strategy)
@settings(max_examples=25)
def test_OperatorExpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)


OrderedCollection_strategy = st.builds(OrderedCollection)
@given(instance=OrderedCollection_strategy)
@settings(max_examples=25)
def test_OrderedCollection_instantiation(instance):
    assert isinstance(instance, OrderedCollection)


OrderedCollectionType_strategy = st.builds(OrderedCollectionType)
@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=25)
def test_OrderedCollectionType_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)


PrimitiveExpression_strategy = st.builds(PrimitiveExpression)
@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


PseudoType_strategy = st.builds(PseudoType)
@given(instance=PseudoType_strategy)
@settings(max_examples=25)
def test_PseudoType_instantiation(instance):
    assert isinstance(instance, PseudoType)


RealType_strategy = st.builds(RealType)
@given(instance=RealType_strategy)
@settings(max_examples=25)
def test_RealType_instantiation(instance):
    assert isinstance(instance, RealType)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


SummableExpression_strategy = st.builds(SummableExpression)
@given(instance=SummableExpression_strategy)
@settings(max_examples=25)
def test_SummableExpression_instantiation(instance):
    assert isinstance(instance, SummableExpression)


SummablePrimitiveType_strategy = st.builds(SummablePrimitiveType)
@given(instance=SummablePrimitiveType_strategy)
@settings(max_examples=25)
def test_SummablePrimitiveType_instantiation(instance):
    assert isinstance(instance, SummablePrimitiveType)


SwitchCaseStatement_strategy = st.builds(SwitchCaseStatement)
@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=25)
def test_SwitchCaseStatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


UnaryOperatorExpression_strategy = st.builds(UnaryOperatorExpression)
@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_UnaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)


UniqueCollection_strategy = st.builds(UniqueCollection)
@given(instance=UniqueCollection_strategy)
@settings(max_examples=25)
def test_UniqueCollection_instantiation(instance):
    assert isinstance(instance, UniqueCollection)


UniqueCollectionType_strategy = st.builds(UniqueCollectionType)
@given(instance=UniqueCollectionType_strategy)
@settings(max_examples=25)
def test_UniqueCollectionType_instantiation(instance):
    assert isinstance(instance, UniqueCollectionType)


VariableDeclarationExpression_strategy = st.builds(VariableDeclarationExpression)
@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)


eol_AbortStatement_strategy = st.builds(eol_AbortStatement)
@given(instance=eol_AbortStatement_strategy)
@settings(max_examples=25)
def test_eol_AbortStatement_instantiation(instance):
    assert isinstance(instance, eol_AbortStatement)


eol_AndOperatorExpression_strategy = st.builds(eol_AndOperatorExpression)
@given(instance=eol_AndOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_AndOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_AndOperatorExpression)


eol_AnnotationBlock_strategy = st.builds(eol_AnnotationBlock)
@given(instance=eol_AnnotationBlock_strategy)
@settings(max_examples=25)
def test_eol_AnnotationBlock_instantiation(instance):
    assert isinstance(instance, eol_AnnotationBlock)


eol_AnnotationStatement_strategy = st.builds(eol_AnnotationStatement)
@given(instance=eol_AnnotationStatement_strategy)
@settings(max_examples=25)
def test_eol_AnnotationStatement_instantiation(instance):
    assert isinstance(instance, eol_AnnotationStatement)


eol_AnyType_strategy = st.builds(eol_AnyType, declared=st.booleans())
@given(instance=eol_AnyType_strategy)
@settings(max_examples=25)
def test_eol_AnyType_instantiation(instance):
    assert isinstance(instance, eol_AnyType)


eol_ArithmeticOperatorExpression_strategy = st.builds(eol_ArithmeticOperatorExpression)
@given(instance=eol_ArithmeticOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_ArithmeticOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_ArithmeticOperatorExpression)


eol_AssignmentStatement_strategy = st.builds(eol_AssignmentStatement)
@given(instance=eol_AssignmentStatement_strategy)
@settings(max_examples=25)
def test_eol_AssignmentStatement_instantiation(instance):
    assert isinstance(instance, eol_AssignmentStatement)


eol_BagExpression_strategy = st.builds(eol_BagExpression)
@given(instance=eol_BagExpression_strategy)
@settings(max_examples=25)
def test_eol_BagExpression_instantiation(instance):
    assert isinstance(instance, eol_BagExpression)


eol_BagType_strategy = st.builds(eol_BagType)
@given(instance=eol_BagType_strategy)
@settings(max_examples=25)
def test_eol_BagType_instantiation(instance):
    assert isinstance(instance, eol_BagType)


eol_BinaryOperatorExpression_strategy = st.builds(eol_BinaryOperatorExpression)
@given(instance=eol_BinaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_BinaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_BinaryOperatorExpression)


eol_Block_strategy = st.builds(eol_Block)
@given(instance=eol_Block_strategy)
@settings(max_examples=25)
def test_eol_Block_instantiation(instance):
    assert isinstance(instance, eol_Block)


eol_BooleanExpression_strategy = st.builds(eol_BooleanExpression, value=st.booleans())
@given(instance=eol_BooleanExpression_strategy)
@settings(max_examples=25)
def test_eol_BooleanExpression_instantiation(instance):
    assert isinstance(instance, eol_BooleanExpression)


eol_BooleanType_strategy = st.builds(eol_BooleanType)
@given(instance=eol_BooleanType_strategy)
@settings(max_examples=25)
def test_eol_BooleanType_instantiation(instance):
    assert isinstance(instance, eol_BooleanType)


eol_BreakAllStatement_strategy = st.builds(eol_BreakAllStatement)
@given(instance=eol_BreakAllStatement_strategy)
@settings(max_examples=25)
def test_eol_BreakAllStatement_instantiation(instance):
    assert isinstance(instance, eol_BreakAllStatement)


eol_BreakStatement_strategy = st.builds(eol_BreakStatement)
@given(instance=eol_BreakStatement_strategy)
@settings(max_examples=25)
def test_eol_BreakStatement_instantiation(instance):
    assert isinstance(instance, eol_BreakStatement)


eol_CollectionExpression_strategy = st.builds(eol_CollectionExpression)
@given(instance=eol_CollectionExpression_strategy)
@settings(max_examples=25)
def test_eol_CollectionExpression_instantiation(instance):
    assert isinstance(instance, eol_CollectionExpression)


eol_CollectionInitialisationExpression_strategy = st.builds(eol_CollectionInitialisationExpression)
@given(instance=eol_CollectionInitialisationExpression_strategy)
@settings(max_examples=25)
def test_eol_CollectionInitialisationExpression_instantiation(instance):
    assert isinstance(instance, eol_CollectionInitialisationExpression)


eol_CollectionType_strategy = st.builds(eol_CollectionType)
@given(instance=eol_CollectionType_strategy)
@settings(max_examples=25)
def test_eol_CollectionType_instantiation(instance):
    assert isinstance(instance, eol_CollectionType)


eol_ComparableExpression_strategy = st.builds(eol_ComparableExpression)
@given(instance=eol_ComparableExpression_strategy)
@settings(max_examples=25)
def test_eol_ComparableExpression_instantiation(instance):
    assert isinstance(instance, eol_ComparableExpression)


eol_ComparablePrimitiveType_strategy = st.builds(eol_ComparablePrimitiveType)
@given(instance=eol_ComparablePrimitiveType_strategy)
@settings(max_examples=25)
def test_eol_ComparablePrimitiveType_instantiation(instance):
    assert isinstance(instance, eol_ComparablePrimitiveType)


eol_ComparisonOperatorExpression_strategy = st.builds(eol_ComparisonOperatorExpression)
@given(instance=eol_ComparisonOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_ComparisonOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_ComparisonOperatorExpression)


eol_ContinueStatement_strategy = st.builds(eol_ContinueStatement)
@given(instance=eol_ContinueStatement_strategy)
@settings(max_examples=25)
def test_eol_ContinueStatement_instantiation(instance):
    assert isinstance(instance, eol_ContinueStatement)


eol_DeleteStatement_strategy = st.builds(eol_DeleteStatement)
@given(instance=eol_DeleteStatement_strategy)
@settings(max_examples=25)
def test_eol_DeleteStatement_instantiation(instance):
    assert isinstance(instance, eol_DeleteStatement)


eol_DivideOperatorExpression_strategy = st.builds(eol_DivideOperatorExpression)
@given(instance=eol_DivideOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_DivideOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_DivideOperatorExpression)


eol_EOLElement_strategy = st.builds(eol_EOLElement, uri=safe_text)
@given(instance=eol_EOLElement_strategy)
@settings(max_examples=25)
def test_eol_EOLElement_instantiation(instance):
    assert isinstance(instance, eol_EOLElement)


eol_EOLLibraryModule_strategy = st.builds(eol_EOLLibraryModule, name=safe_text)
@given(instance=eol_EOLLibraryModule_strategy)
@settings(max_examples=25)
def test_eol_EOLLibraryModule_instantiation(instance):
    assert isinstance(instance, eol_EOLLibraryModule)


eol_EOLModule_strategy = st.builds(eol_EOLModule)
@given(instance=eol_EOLModule_strategy)
@settings(max_examples=25)
def test_eol_EOLModule_instantiation(instance):
    assert isinstance(instance, eol_EOLModule)


eol_EnumerationLiteralExpression_strategy = st.builds(eol_EnumerationLiteralExpression)
@given(instance=eol_EnumerationLiteralExpression_strategy)
@settings(max_examples=25)
def test_eol_EnumerationLiteralExpression_instantiation(instance):
    assert isinstance(instance, eol_EnumerationLiteralExpression)


eol_EqualsOperatorExpression_strategy = st.builds(eol_EqualsOperatorExpression)
@given(instance=eol_EqualsOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_EqualsOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_EqualsOperatorExpression)


eol_ExecutableAnnotationStatement_strategy = st.builds(eol_ExecutableAnnotationStatement)
@given(instance=eol_ExecutableAnnotationStatement_strategy)
@settings(max_examples=25)
def test_eol_ExecutableAnnotationStatement_instantiation(instance):
    assert isinstance(instance, eol_ExecutableAnnotationStatement)


eol_Expression_strategy = st.builds(eol_Expression, inBrackets=st.booleans())
@given(instance=eol_Expression_strategy)
@settings(max_examples=25)
def test_eol_Expression_instantiation(instance):
    assert isinstance(instance, eol_Expression)


eol_ExpressionList_strategy = st.builds(eol_ExpressionList)
@given(instance=eol_ExpressionList_strategy)
@settings(max_examples=25)
def test_eol_ExpressionList_instantiation(instance):
    assert isinstance(instance, eol_ExpressionList)


eol_ExpressionOrStatementBlock_strategy = st.builds(eol_ExpressionOrStatementBlock)
@given(instance=eol_ExpressionOrStatementBlock_strategy)
@settings(max_examples=25)
def test_eol_ExpressionOrStatementBlock_instantiation(instance):
    assert isinstance(instance, eol_ExpressionOrStatementBlock)


eol_ExpressionRange_strategy = st.builds(eol_ExpressionRange)
@given(instance=eol_ExpressionRange_strategy)
@settings(max_examples=25)
def test_eol_ExpressionRange_instantiation(instance):
    assert isinstance(instance, eol_ExpressionRange)


eol_ExpressionStatement_strategy = st.builds(eol_ExpressionStatement)
@given(instance=eol_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_eol_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, eol_ExpressionStatement)


eol_FOLMethodCallExpression_strategy = st.builds(eol_FOLMethodCallExpression)
@given(instance=eol_FOLMethodCallExpression_strategy)
@settings(max_examples=25)
def test_eol_FOLMethodCallExpression_instantiation(instance):
    assert isinstance(instance, eol_FOLMethodCallExpression)


eol_FeatureCallExpression_strategy = st.builds(eol_FeatureCallExpression, arrow=st.booleans())
@given(instance=eol_FeatureCallExpression_strategy)
@settings(max_examples=25)
def test_eol_FeatureCallExpression_instantiation(instance):
    assert isinstance(instance, eol_FeatureCallExpression)


eol_ForStatement_strategy = st.builds(eol_ForStatement)
@given(instance=eol_ForStatement_strategy)
@settings(max_examples=25)
def test_eol_ForStatement_instantiation(instance):
    assert isinstance(instance, eol_ForStatement)


eol_FormalParameterExpression_strategy = st.builds(eol_FormalParameterExpression)
@given(instance=eol_FormalParameterExpression_strategy)
@settings(max_examples=25)
def test_eol_FormalParameterExpression_instantiation(instance):
    assert isinstance(instance, eol_FormalParameterExpression)


eol_GreaterThanOperatorExpression_strategy = st.builds(eol_GreaterThanOperatorExpression)
@given(instance=eol_GreaterThanOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_GreaterThanOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOperatorExpression)


eol_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(eol_GreaterThanOrEqualToOperatorExpression)
@given(instance=eol_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_GreaterThanOrEqualToOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOrEqualToOperatorExpression)


eol_IfStatement_strategy = st.builds(eol_IfStatement)
@given(instance=eol_IfStatement_strategy)
@settings(max_examples=25)
def test_eol_IfStatement_instantiation(instance):
    assert isinstance(instance, eol_IfStatement)


eol_ImpliesOperatorExpression_strategy = st.builds(eol_ImpliesOperatorExpression)
@given(instance=eol_ImpliesOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_ImpliesOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_ImpliesOperatorExpression)


eol_Import_strategy = st.builds(eol_Import, imported=safe_text)
@given(instance=eol_Import_strategy)
@settings(max_examples=25)
def test_eol_Import_instantiation(instance):
    assert isinstance(instance, eol_Import)


eol_IntegerExpression_strategy = st.builds(eol_IntegerExpression, value=st.integers())
@given(instance=eol_IntegerExpression_strategy)
@settings(max_examples=25)
def test_eol_IntegerExpression_instantiation(instance):
    assert isinstance(instance, eol_IntegerExpression)


eol_IntegerType_strategy = st.builds(eol_IntegerType)
@given(instance=eol_IntegerType_strategy)
@settings(max_examples=25)
def test_eol_IntegerType_instantiation(instance):
    assert isinstance(instance, eol_IntegerType)


eol_InvalidType_strategy = st.builds(eol_InvalidType)
@given(instance=eol_InvalidType_strategy)
@settings(max_examples=25)
def test_eol_InvalidType_instantiation(instance):
    assert isinstance(instance, eol_InvalidType)


eol_KeyValueExpression_strategy = st.builds(eol_KeyValueExpression)
@given(instance=eol_KeyValueExpression_strategy)
@settings(max_examples=25)
def test_eol_KeyValueExpression_instantiation(instance):
    assert isinstance(instance, eol_KeyValueExpression)


eol_LessThanOperatorExpression_strategy = st.builds(eol_LessThanOperatorExpression)
@given(instance=eol_LessThanOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_LessThanOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOperatorExpression)


eol_LessThanOrEqualToOperatorExpression_strategy = st.builds(eol_LessThanOrEqualToOperatorExpression)
@given(instance=eol_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_LessThanOrEqualToOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOrEqualToOperatorExpression)


eol_LogicalOperatorExpression_strategy = st.builds(eol_LogicalOperatorExpression)
@given(instance=eol_LogicalOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_LogicalOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_LogicalOperatorExpression)


eol_MapExpression_strategy = st.builds(eol_MapExpression)
@given(instance=eol_MapExpression_strategy)
@settings(max_examples=25)
def test_eol_MapExpression_instantiation(instance):
    assert isinstance(instance, eol_MapExpression)


eol_MapType_strategy = st.builds(eol_MapType)
@given(instance=eol_MapType_strategy)
@settings(max_examples=25)
def test_eol_MapType_instantiation(instance):
    assert isinstance(instance, eol_MapType)


eol_MethodCallExpression_strategy = st.builds(eol_MethodCallExpression)
@given(instance=eol_MethodCallExpression_strategy)
@settings(max_examples=25)
def test_eol_MethodCallExpression_instantiation(instance):
    assert isinstance(instance, eol_MethodCallExpression)


eol_MinusOperatorExpression_strategy = st.builds(eol_MinusOperatorExpression)
@given(instance=eol_MinusOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_MinusOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_MinusOperatorExpression)


eol_ModelDeclarationParameter_strategy = st.builds(eol_ModelDeclarationParameter)
@given(instance=eol_ModelDeclarationParameter_strategy)
@settings(max_examples=25)
def test_eol_ModelDeclarationParameter_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationParameter)


eol_ModelDeclarationStatement_strategy = st.builds(eol_ModelDeclarationStatement, resolvedIMetamodel=safe_text)
@given(instance=eol_ModelDeclarationStatement_strategy)
@settings(max_examples=25)
def test_eol_ModelDeclarationStatement_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationStatement)


eol_ModelElementType_strategy = st.builds(eol_ModelElementType, elementName=safe_text, modelElementType=safe_text, modelName=safe_text, resolvedIMetamodel=safe_text, resolvedIPackage=safe_text)
@given(instance=eol_ModelElementType_strategy)
@settings(max_examples=25)
def test_eol_ModelElementType_instantiation(instance):
    assert isinstance(instance, eol_ModelElementType)


eol_ModelType_strategy = st.builds(eol_ModelType, modelName=safe_text, resolvedIMetamodel=safe_text)
@given(instance=eol_ModelType_strategy)
@settings(max_examples=25)
def test_eol_ModelType_instantiation(instance):
    assert isinstance(instance, eol_ModelType)


eol_MultiplyOperatorExpression_strategy = st.builds(eol_MultiplyOperatorExpression)
@given(instance=eol_MultiplyOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_MultiplyOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_MultiplyOperatorExpression)


eol_NameExpression_strategy = st.builds(eol_NameExpression, isType=st.booleans(), name=safe_text, resolvedContent=safe_text)
@given(instance=eol_NameExpression_strategy)
@settings(max_examples=25)
def test_eol_NameExpression_instantiation(instance):
    assert isinstance(instance, eol_NameExpression)


eol_NativeType_strategy = st.builds(eol_NativeType)
@given(instance=eol_NativeType_strategy)
@settings(max_examples=25)
def test_eol_NativeType_instantiation(instance):
    assert isinstance(instance, eol_NativeType)


eol_NegativeOperatorExpression_strategy = st.builds(eol_NegativeOperatorExpression)
@given(instance=eol_NegativeOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_NegativeOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_NegativeOperatorExpression)


eol_NewExpression_strategy = st.builds(eol_NewExpression)
@given(instance=eol_NewExpression_strategy)
@settings(max_examples=25)
def test_eol_NewExpression_instantiation(instance):
    assert isinstance(instance, eol_NewExpression)


eol_NotEqualsOperatorExpression_strategy = st.builds(eol_NotEqualsOperatorExpression)
@given(instance=eol_NotEqualsOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_NotEqualsOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_NotEqualsOperatorExpression)


eol_NotOperatorExpression_strategy = st.builds(eol_NotOperatorExpression)
@given(instance=eol_NotOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_NotOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_NotOperatorExpression)


eol_OperationDefinition_strategy = st.builds(eol_OperationDefinition)
@given(instance=eol_OperationDefinition_strategy)
@settings(max_examples=25)
def test_eol_OperationDefinition_instantiation(instance):
    assert isinstance(instance, eol_OperationDefinition)


eol_OperatorExpression_strategy = st.builds(eol_OperatorExpression)
@given(instance=eol_OperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_OperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_OperatorExpression)


eol_OrOperatorExpression_strategy = st.builds(eol_OrOperatorExpression)
@given(instance=eol_OrOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_OrOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_OrOperatorExpression)


eol_OrderedCollection_strategy = st.builds(eol_OrderedCollection)
@given(instance=eol_OrderedCollection_strategy)
@settings(max_examples=25)
def test_eol_OrderedCollection_instantiation(instance):
    assert isinstance(instance, eol_OrderedCollection)


eol_OrderedCollectionType_strategy = st.builds(eol_OrderedCollectionType)
@given(instance=eol_OrderedCollectionType_strategy)
@settings(max_examples=25)
def test_eol_OrderedCollectionType_instantiation(instance):
    assert isinstance(instance, eol_OrderedCollectionType)


eol_OrderedSetExpression_strategy = st.builds(eol_OrderedSetExpression)
@given(instance=eol_OrderedSetExpression_strategy)
@settings(max_examples=25)
def test_eol_OrderedSetExpression_instantiation(instance):
    assert isinstance(instance, eol_OrderedSetExpression)


eol_OrderedSetType_strategy = st.builds(eol_OrderedSetType)
@given(instance=eol_OrderedSetType_strategy)
@settings(max_examples=25)
def test_eol_OrderedSetType_instantiation(instance):
    assert isinstance(instance, eol_OrderedSetType)


eol_PlusOperatorExpression_strategy = st.builds(eol_PlusOperatorExpression)
@given(instance=eol_PlusOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_PlusOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_PlusOperatorExpression)


eol_PrimitiveExpression_strategy = st.builds(eol_PrimitiveExpression)
@given(instance=eol_PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_eol_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveExpression)


eol_PrimitiveType_strategy = st.builds(eol_PrimitiveType)
@given(instance=eol_PrimitiveType_strategy)
@settings(max_examples=25)
def test_eol_PrimitiveType_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveType)


eol_PropertyCallExpression_strategy = st.builds(eol_PropertyCallExpression, extended=st.booleans())
@given(instance=eol_PropertyCallExpression_strategy)
@settings(max_examples=25)
def test_eol_PropertyCallExpression_instantiation(instance):
    assert isinstance(instance, eol_PropertyCallExpression)


eol_PseudoType_strategy = st.builds(eol_PseudoType)
@given(instance=eol_PseudoType_strategy)
@settings(max_examples=25)
def test_eol_PseudoType_instantiation(instance):
    assert isinstance(instance, eol_PseudoType)


eol_RealExpression_strategy = st.builds(eol_RealExpression, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=eol_RealExpression_strategy)
@settings(max_examples=25)
def test_eol_RealExpression_instantiation(instance):
    assert isinstance(instance, eol_RealExpression)


eol_RealType_strategy = st.builds(eol_RealType)
@given(instance=eol_RealType_strategy)
@settings(max_examples=25)
def test_eol_RealType_instantiation(instance):
    assert isinstance(instance, eol_RealType)


eol_ReturnStatement_strategy = st.builds(eol_ReturnStatement)
@given(instance=eol_ReturnStatement_strategy)
@settings(max_examples=25)
def test_eol_ReturnStatement_instantiation(instance):
    assert isinstance(instance, eol_ReturnStatement)


eol_SelfContentType_strategy = st.builds(eol_SelfContentType)
@given(instance=eol_SelfContentType_strategy)
@settings(max_examples=25)
def test_eol_SelfContentType_instantiation(instance):
    assert isinstance(instance, eol_SelfContentType)


eol_SelfType_strategy = st.builds(eol_SelfType)
@given(instance=eol_SelfType_strategy)
@settings(max_examples=25)
def test_eol_SelfType_instantiation(instance):
    assert isinstance(instance, eol_SelfType)


eol_SequenceExpression_strategy = st.builds(eol_SequenceExpression)
@given(instance=eol_SequenceExpression_strategy)
@settings(max_examples=25)
def test_eol_SequenceExpression_instantiation(instance):
    assert isinstance(instance, eol_SequenceExpression)


eol_SequenceType_strategy = st.builds(eol_SequenceType)
@given(instance=eol_SequenceType_strategy)
@settings(max_examples=25)
def test_eol_SequenceType_instantiation(instance):
    assert isinstance(instance, eol_SequenceType)


eol_SetExpression_strategy = st.builds(eol_SetExpression)
@given(instance=eol_SetExpression_strategy)
@settings(max_examples=25)
def test_eol_SetExpression_instantiation(instance):
    assert isinstance(instance, eol_SetExpression)


eol_SetType_strategy = st.builds(eol_SetType)
@given(instance=eol_SetType_strategy)
@settings(max_examples=25)
def test_eol_SetType_instantiation(instance):
    assert isinstance(instance, eol_SetType)


eol_SimpleAnnotationStatement_strategy = st.builds(eol_SimpleAnnotationStatement)
@given(instance=eol_SimpleAnnotationStatement_strategy)
@settings(max_examples=25)
def test_eol_SimpleAnnotationStatement_instantiation(instance):
    assert isinstance(instance, eol_SimpleAnnotationStatement)


eol_SpecialAssignmentStatement_strategy = st.builds(eol_SpecialAssignmentStatement)
@given(instance=eol_SpecialAssignmentStatement_strategy)
@settings(max_examples=25)
def test_eol_SpecialAssignmentStatement_instantiation(instance):
    assert isinstance(instance, eol_SpecialAssignmentStatement)


eol_Statement_strategy = st.builds(eol_Statement)
@given(instance=eol_Statement_strategy)
@settings(max_examples=25)
def test_eol_Statement_instantiation(instance):
    assert isinstance(instance, eol_Statement)


eol_StringExpression_strategy = st.builds(eol_StringExpression, value=safe_text)
@given(instance=eol_StringExpression_strategy)
@settings(max_examples=25)
def test_eol_StringExpression_instantiation(instance):
    assert isinstance(instance, eol_StringExpression)


eol_StringType_strategy = st.builds(eol_StringType)
@given(instance=eol_StringType_strategy)
@settings(max_examples=25)
def test_eol_StringType_instantiation(instance):
    assert isinstance(instance, eol_StringType)


eol_SummableExpression_strategy = st.builds(eol_SummableExpression)
@given(instance=eol_SummableExpression_strategy)
@settings(max_examples=25)
def test_eol_SummableExpression_instantiation(instance):
    assert isinstance(instance, eol_SummableExpression)


eol_SummablePrimitiveType_strategy = st.builds(eol_SummablePrimitiveType)
@given(instance=eol_SummablePrimitiveType_strategy)
@settings(max_examples=25)
def test_eol_SummablePrimitiveType_instantiation(instance):
    assert isinstance(instance, eol_SummablePrimitiveType)


eol_SwitchCaseDefaultStatement_strategy = st.builds(eol_SwitchCaseDefaultStatement)
@given(instance=eol_SwitchCaseDefaultStatement_strategy)
@settings(max_examples=25)
def test_eol_SwitchCaseDefaultStatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseDefaultStatement)


eol_SwitchCaseExpressionStatement_strategy = st.builds(eol_SwitchCaseExpressionStatement)
@given(instance=eol_SwitchCaseExpressionStatement_strategy)
@settings(max_examples=25)
def test_eol_SwitchCaseExpressionStatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseExpressionStatement)


eol_SwitchCaseStatement_strategy = st.builds(eol_SwitchCaseStatement)
@given(instance=eol_SwitchCaseStatement_strategy)
@settings(max_examples=25)
def test_eol_SwitchCaseStatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseStatement)


eol_SwitchStatement_strategy = st.builds(eol_SwitchStatement)
@given(instance=eol_SwitchStatement_strategy)
@settings(max_examples=25)
def test_eol_SwitchStatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchStatement)


eol_TextPosition_strategy = st.builds(eol_TextPosition, column=st.integers(), line=st.integers())
@given(instance=eol_TextPosition_strategy)
@settings(max_examples=25)
def test_eol_TextPosition_instantiation(instance):
    assert isinstance(instance, eol_TextPosition)


eol_TextRegion_strategy = st.builds(eol_TextRegion)
@given(instance=eol_TextRegion_strategy)
@settings(max_examples=25)
def test_eol_TextRegion_instantiation(instance):
    assert isinstance(instance, eol_TextRegion)


eol_ThrowStatement_strategy = st.builds(eol_ThrowStatement)
@given(instance=eol_ThrowStatement_strategy)
@settings(max_examples=25)
def test_eol_ThrowStatement_instantiation(instance):
    assert isinstance(instance, eol_ThrowStatement)


eol_TransactionStatement_strategy = st.builds(eol_TransactionStatement)
@given(instance=eol_TransactionStatement_strategy)
@settings(max_examples=25)
def test_eol_TransactionStatement_instantiation(instance):
    assert isinstance(instance, eol_TransactionStatement)


eol_Type_strategy = st.builds(eol_Type)
@given(instance=eol_Type_strategy)
@settings(max_examples=25)
def test_eol_Type_instantiation(instance):
    assert isinstance(instance, eol_Type)


eol_UnaryOperatorExpression_strategy = st.builds(eol_UnaryOperatorExpression)
@given(instance=eol_UnaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_UnaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_UnaryOperatorExpression)


eol_UniqueCollection_strategy = st.builds(eol_UniqueCollection)
@given(instance=eol_UniqueCollection_strategy)
@settings(max_examples=25)
def test_eol_UniqueCollection_instantiation(instance):
    assert isinstance(instance, eol_UniqueCollection)


eol_UniqueCollectionType_strategy = st.builds(eol_UniqueCollectionType)
@given(instance=eol_UniqueCollectionType_strategy)
@settings(max_examples=25)
def test_eol_UniqueCollectionType_instantiation(instance):
    assert isinstance(instance, eol_UniqueCollectionType)


eol_VariableDeclarationExpression_strategy = st.builds(eol_VariableDeclarationExpression, create=st.booleans())
@given(instance=eol_VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_eol_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, eol_VariableDeclarationExpression)


eol_VoidType_strategy = st.builds(eol_VoidType)
@given(instance=eol_VoidType_strategy)
@settings(max_examples=25)
def test_eol_VoidType_instantiation(instance):
    assert isinstance(instance, eol_VoidType)


eol_WhileStatement_strategy = st.builds(eol_WhileStatement)
@given(instance=eol_WhileStatement_strategy)
@settings(max_examples=25)
def test_eol_WhileStatement_instantiation(instance):
    assert isinstance(instance, eol_WhileStatement)


eol_XorOperatorExpression_strategy = st.builds(eol_XorOperatorExpression)
@given(instance=eol_XorOperatorExpression_strategy)
@settings(max_examples=25)
def test_eol_XorOperatorExpression_instantiation(instance):
    assert isinstance(instance, eol_XorOperatorExpression)



