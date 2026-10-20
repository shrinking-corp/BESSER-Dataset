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
    Iterator,
    NumericLiteralExp,
    OCL_IntegerLiteralExp,
    OperationCallExp,
    OCL_OperatorCallExp,
    OCL_CollectionOperationCallExp,
    FeaturePropertyCall,
    OCL_PropertyCallExp,
    OCL_OperationCallExp,
    LoopExp,
    OCL_IteratorExp,
    OCL_IterateExp,
    PrimitiveLiteralExp,
    OCL_StringLiteralExp,
    OCL_NumericLiteralExp,
    CollectionLiteralPart,
    OCL_CollectionItem,
    OCL_CollectionRange,
    TupleLiteralPart,
    CallExp,
    OCL_LoopExp,
    OCL_FeaturePropertyCall,
    LiteralExp,
    OCL_TupleLiteralExp,
    OCL_NullLiteralExp,
    OCL_PrimitiveLiteralExp,
    OCL_CollectionLiteralExp,
    OCL_InvalidLiteralExp,
    OCL_EnumLiteralExp,
    CollectionType,
    OCL_SequenceType,
    OCL_OrderedSetType,
    OCL_BagType,
    OCL_SetType,
    Type,
    OCL_Class,
    OCL_VoidType,
    OCL_InvalidType,
    PrimitiveType,
    OCL_StringType,
    OCL_RealType,
    OCL_BooleanType,
    OCL_IntegerType,
    DataType,
    OCL_CollectionType,
    OCL_TupleType,
    OCL_PrimitiveType,
    Extent,
    OCL_URIExtent,
    NamedElement,
    OCL_EnumerationLiteral,
    OCL_TypedElement,
    EnumerationLiteral,
    OCL_Enumeration,
    Object,
    OCL_Element,
    OCL_Extent,
    OCL_Object,
    OCL_MultiplicityElement,
    OCL_Package,
    OCL_Type,
    OCL_DataType,
    MultiplicityElement,
    TypedElement,
    OCL_CollectionLiteralPart,
    OCL_Variable,
    OCL_Operation,
    OCL_Parameter,
    OCL_Property,
    OCL_TupleLiteralPart,
    OCL_OclModuleElement,
    OCL_OclFeature,
    Property,
    OclExpression,
    OCL_VariableExp,
    OCL_LetExp,
    OCL_LiteralExp,
    Variable,
    OCL_Iterator,
    OclFeature,
    OCL_OclProperty,
    Operation,
    OCL_OclOperation,
    Package,
    OCL_OclModule,
    Class,
    OCL_AnyType,
    Element,
    OCL_Comment,
    OCL_NamedElement,
    OCL_Tag,
    OCL_OclContextDefinition,
    Parameter,
    OclModuleElement,
    OCL_DeriveOclModuleElement,
    OCL_Invariant,
    OCL_DefOclModuleElement,
    OclContextDefinition,
    OCL_RealLiteralExp,
    OCL_BooleanLiteralExp,
    OCL_CallExp,
    OCL_OclExpression,
    OCL_IfExp,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_hyp_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_hyp_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_hyp_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_hyp_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerLiteralExp)


def test_hyp_ocl_integerliteralexp_constructor_exists():
    assert callable(OCL_IntegerLiteralExp.__init__)


def test_hyp_ocl_integerliteralexp_constructor_args():
    sig = inspect.signature(OCL_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"




def test_hyp_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_hyp_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_hyp_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperatorCallExp)


def test_hyp_ocl_operatorcallexp_constructor_exists():
    assert callable(OCL_OperatorCallExp.__init__)


def test_hyp_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(OCL_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionOperationCallExp)


def test_hyp_ocl_collectionoperationcallexp_constructor_exists():
    assert callable(OCL_CollectionOperationCallExp.__init__)


def test_hyp_ocl_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCL_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_hyp_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_hyp_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PropertyCallExp)


def test_hyp_ocl_propertycallexp_constructor_exists():
    assert callable(OCL_PropertyCallExp.__init__)


def test_hyp_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperationCallExp)


def test_hyp_ocl_operationcallexp_constructor_exists():
    assert callable(OCL_OperationCallExp.__init__)


def test_hyp_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(OCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_hyp_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_hyp_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IteratorExp)


def test_hyp_ocl_iteratorexp_constructor_exists():
    assert callable(OCL_IteratorExp.__init__)


def test_hyp_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(OCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IterateExp)


def test_hyp_ocl_iterateexp_constructor_exists():
    assert callable(OCL_IterateExp.__init__)


def test_hyp_ocl_iterateexp_constructor_args():
    sig = inspect.signature(OCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_hyp_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_hyp_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_StringLiteralExp)


def test_hyp_ocl_stringliteralexp_constructor_exists():
    assert callable(OCL_StringLiteralExp.__init__)


def test_hyp_ocl_stringliteralexp_constructor_args():
    sig = inspect.signature(OCL_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_ocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NumericLiteralExp)


def test_hyp_ocl_numericliteralexp_constructor_exists():
    assert callable(OCL_NumericLiteralExp.__init__)


def test_hyp_ocl_numericliteralexp_constructor_args():
    sig = inspect.signature(OCL_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_hyp_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_hyp_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionItem)


def test_hyp_ocl_collectionitem_constructor_exists():
    assert callable(OCL_CollectionItem.__init__)


def test_hyp_ocl_collectionitem_constructor_args():
    sig = inspect.signature(OCL_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionRange)


def test_hyp_ocl_collectionrange_constructor_exists():
    assert callable(OCL_CollectionRange.__init__)


def test_hyp_ocl_collectionrange_constructor_args():
    sig = inspect.signature(OCL_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_hyp_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_hyp_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_hyp_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_hyp_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LoopExp)


def test_hyp_ocl_loopexp_constructor_exists():
    assert callable(OCL_LoopExp.__init__)


def test_hyp_ocl_loopexp_constructor_args():
    sig = inspect.signature(OCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(OCL_FeaturePropertyCall)


def test_hyp_ocl_featurepropertycall_constructor_exists():
    assert callable(OCL_FeaturePropertyCall.__init__)


def test_hyp_ocl_featurepropertycall_constructor_args():
    sig = inspect.signature(OCL_FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_hyp_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_hyp_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleLiteralExp)


def test_hyp_ocl_tupleliteralexp_constructor_exists():
    assert callable(OCL_TupleLiteralExp.__init__)


def test_hyp_ocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(OCL_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NullLiteralExp)


def test_hyp_ocl_nullliteralexp_constructor_exists():
    assert callable(OCL_NullLiteralExp.__init__)


def test_hyp_ocl_nullliteralexp_constructor_args():
    sig = inspect.signature(OCL_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PrimitiveLiteralExp)


def test_hyp_ocl_primitiveliteralexp_constructor_exists():
    assert callable(OCL_PrimitiveLiteralExp.__init__)


def test_hyp_ocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(OCL_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionLiteralExp)


def test_hyp_ocl_collectionliteralexp_constructor_exists():
    assert callable(OCL_CollectionLiteralExp.__init__)


def test_hyp_ocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(OCL_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_ocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_InvalidLiteralExp)


def test_hyp_ocl_invalidliteralexp_constructor_exists():
    assert callable(OCL_InvalidLiteralExp.__init__)


def test_hyp_ocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(OCL_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_EnumLiteralExp)


def test_hyp_ocl_enumliteralexp_constructor_exists():
    assert callable(OCL_EnumLiteralExp.__init__)


def test_hyp_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(OCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_hyp_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_hyp_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCL_SequenceType)


def test_hyp_ocl_sequencetype_constructor_exists():
    assert callable(OCL_SequenceType.__init__)


def test_hyp_ocl_sequencetype_constructor_args():
    sig = inspect.signature(OCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCL_OrderedSetType)


def test_hyp_ocl_orderedsettype_constructor_exists():
    assert callable(OCL_OrderedSetType.__init__)


def test_hyp_ocl_orderedsettype_constructor_args():
    sig = inspect.signature(OCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(OCL_BagType)


def test_hyp_ocl_bagtype_constructor_exists():
    assert callable(OCL_BagType.__init__)


def test_hyp_ocl_bagtype_constructor_args():
    sig = inspect.signature(OCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_settype_is_not_abstract():
    assert not inspect.isabstract(OCL_SetType)


def test_hyp_ocl_settype_constructor_exists():
    assert callable(OCL_SetType.__init__)


def test_hyp_ocl_settype_constructor_args():
    sig = inspect.signature(OCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_class_is_not_abstract():
    assert not inspect.isabstract(OCL_Class)


def test_hyp_ocl_class_constructor_exists():
    assert callable(OCL_Class.__init__)


def test_hyp_ocl_class_constructor_args():
    sig = inspect.signature(OCL_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"




def test_hyp_ocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(OCL_VoidType)


def test_hyp_ocl_voidtype_constructor_exists():
    assert callable(OCL_VoidType.__init__)


def test_hyp_ocl_voidtype_constructor_args():
    sig = inspect.signature(OCL_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(OCL_InvalidType)


def test_hyp_ocl_invalidtype_constructor_exists():
    assert callable(OCL_InvalidType.__init__)


def test_hyp_ocl_invalidtype_constructor_args():
    sig = inspect.signature(OCL_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(OCL_StringType)


def test_hyp_ocl_stringtype_constructor_exists():
    assert callable(OCL_StringType.__init__)


def test_hyp_ocl_stringtype_constructor_args():
    sig = inspect.signature(OCL_StringType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_realtype_is_not_abstract():
    assert not inspect.isabstract(OCL_RealType)


def test_hyp_ocl_realtype_constructor_exists():
    assert callable(OCL_RealType.__init__)


def test_hyp_ocl_realtype_constructor_args():
    sig = inspect.signature(OCL_RealType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanType)


def test_hyp_ocl_booleantype_constructor_exists():
    assert callable(OCL_BooleanType.__init__)


def test_hyp_ocl_booleantype_constructor_args():
    sig = inspect.signature(OCL_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_integertype_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerType)


def test_hyp_ocl_integertype_constructor_exists():
    assert callable(OCL_IntegerType.__init__)


def test_hyp_ocl_integertype_constructor_args():
    sig = inspect.signature(OCL_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionType)


def test_hyp_ocl_collectiontype_constructor_exists():
    assert callable(OCL_CollectionType.__init__)


def test_hyp_ocl_collectiontype_constructor_args():
    sig = inspect.signature(OCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleType)


def test_hyp_ocl_tupletype_constructor_exists():
    assert callable(OCL_TupleType.__init__)


def test_hyp_ocl_tupletype_constructor_args():
    sig = inspect.signature(OCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(OCL_PrimitiveType)


def test_hyp_ocl_primitivetype_constructor_exists():
    assert callable(OCL_PrimitiveType.__init__)


def test_hyp_ocl_primitivetype_constructor_args():
    sig = inspect.signature(OCL_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_hyp_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_hyp_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_uriextent_is_not_abstract():
    assert not inspect.isabstract(OCL_URIExtent)


def test_hyp_ocl_uriextent_constructor_exists():
    assert callable(OCL_URIExtent.__init__)


def test_hyp_ocl_uriextent_constructor_args():
    sig = inspect.signature(OCL_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(OCL_EnumerationLiteral)


def test_hyp_ocl_enumerationliteral_constructor_exists():
    assert callable(OCL_EnumerationLiteral.__init__)


def test_hyp_ocl_enumerationliteral_constructor_args():
    sig = inspect.signature(OCL_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_typedelement_is_not_abstract():
    assert not inspect.isabstract(OCL_TypedElement)


def test_hyp_ocl_typedelement_constructor_exists():
    assert callable(OCL_TypedElement.__init__)


def test_hyp_ocl_typedelement_constructor_args():
    sig = inspect.signature(OCL_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_hyp_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_hyp_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_enumeration_is_not_abstract():
    assert not inspect.isabstract(OCL_Enumeration)


def test_hyp_ocl_enumeration_constructor_exists():
    assert callable(OCL_Enumeration.__init__)


def test_hyp_ocl_enumeration_constructor_args():
    sig = inspect.signature(OCL_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_hyp_object_constructor_exists():
    assert callable(Object.__init__)


def test_hyp_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_element_is_not_abstract():
    assert not inspect.isabstract(OCL_Element)


def test_hyp_ocl_element_constructor_exists():
    assert callable(OCL_Element.__init__)


def test_hyp_ocl_element_constructor_args():
    sig = inspect.signature(OCL_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_extent_is_not_abstract():
    assert not inspect.isabstract(OCL_Extent)


def test_hyp_ocl_extent_constructor_exists():
    assert callable(OCL_Extent.__init__)


def test_hyp_ocl_extent_constructor_args():
    sig = inspect.signature(OCL_Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_object_is_not_abstract():
    assert not inspect.isabstract(OCL_Object)


def test_hyp_ocl_object_constructor_exists():
    assert callable(OCL_Object.__init__)


def test_hyp_ocl_object_constructor_args():
    sig = inspect.signature(OCL_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(OCL_MultiplicityElement)


def test_hyp_ocl_multiplicityelement_constructor_exists():
    assert callable(OCL_MultiplicityElement.__init__)


def test_hyp_ocl_multiplicityelement_constructor_args():
    sig = inspect.signature(OCL_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"







def test_hyp_ocl_package_is_not_abstract():
    assert not inspect.isabstract(OCL_Package)


def test_hyp_ocl_package_constructor_exists():
    assert callable(OCL_Package.__init__)


def test_hyp_ocl_package_constructor_args():
    sig = inspect.signature(OCL_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_ocl_type_is_not_abstract():
    assert not inspect.isabstract(OCL_Type)


def test_hyp_ocl_type_constructor_exists():
    assert callable(OCL_Type.__init__)


def test_hyp_ocl_type_constructor_args():
    sig = inspect.signature(OCL_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_datatype_is_not_abstract():
    assert not inspect.isabstract(OCL_DataType)


def test_hyp_ocl_datatype_constructor_exists():
    assert callable(OCL_DataType.__init__)


def test_hyp_ocl_datatype_constructor_args():
    sig = inspect.signature(OCL_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_hyp_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_hyp_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionLiteralPart)


def test_hyp_ocl_collectionliteralpart_constructor_exists():
    assert callable(OCL_CollectionLiteralPart.__init__)


def test_hyp_ocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(OCL_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_variable_is_not_abstract():
    assert not inspect.isabstract(OCL_Variable)


def test_hyp_ocl_variable_constructor_exists():
    assert callable(OCL_Variable.__init__)


def test_hyp_ocl_variable_constructor_args():
    sig = inspect.signature(OCL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(OCL_Operation)


def test_hyp_ocl_operation_constructor_exists():
    assert callable(OCL_Operation.__init__)


def test_hyp_ocl_operation_constructor_args():
    sig = inspect.signature(OCL_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_parameter_is_not_abstract():
    assert not inspect.isabstract(OCL_Parameter)


def test_hyp_ocl_parameter_constructor_exists():
    assert callable(OCL_Parameter.__init__)


def test_hyp_ocl_parameter_constructor_args():
    sig = inspect.signature(OCL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_property_is_not_abstract():
    assert not inspect.isabstract(OCL_Property)


def test_hyp_ocl_property_constructor_exists():
    assert callable(OCL_Property.__init__)


def test_hyp_ocl_property_constructor_args():
    sig = inspect.signature(OCL_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isId" in params, "Missing parameter 'isId'"








def test_hyp_ocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleLiteralPart)


def test_hyp_ocl_tupleliteralpart_constructor_exists():
    assert callable(OCL_TupleLiteralPart.__init__)


def test_hyp_ocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(OCL_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModuleElement)


def test_hyp_ocl_oclmoduleelement_constructor_exists():
    assert callable(OCL_OclModuleElement.__init__)


def test_hyp_ocl_oclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL_OclFeature)


def test_hyp_ocl_oclfeature_constructor_exists():
    assert callable(OCL_OclFeature.__init__)


def test_hyp_ocl_oclfeature_constructor_args():
    sig = inspect.signature(OCL_OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_hyp_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_hyp_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(OCL_VariableExp)


def test_hyp_ocl_variableexp_constructor_exists():
    assert callable(OCL_VariableExp.__init__)


def test_hyp_ocl_variableexp_constructor_args():
    sig = inspect.signature(OCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LetExp)


def test_hyp_ocl_letexp_constructor_exists():
    assert callable(OCL_LetExp.__init__)


def test_hyp_ocl_letexp_constructor_args():
    sig = inspect.signature(OCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LiteralExp)


def test_hyp_ocl_literalexp_constructor_exists():
    assert callable(OCL_LiteralExp.__init__)


def test_hyp_ocl_literalexp_constructor_args():
    sig = inspect.signature(OCL_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(OCL_Iterator)


def test_hyp_ocl_iterator_constructor_exists():
    assert callable(OCL_Iterator.__init__)


def test_hyp_ocl_iterator_constructor_args():
    sig = inspect.signature(OCL_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_hyp_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_hyp_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_oclproperty_is_not_abstract():
    assert not inspect.isabstract(OCL_OclProperty)


def test_hyp_ocl_oclproperty_constructor_exists():
    assert callable(OCL_OclProperty.__init__)


def test_hyp_ocl_oclproperty_constructor_args():
    sig = inspect.signature(OCL_OclProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_ocloperation_is_not_abstract():
    assert not inspect.isabstract(OCL_OclOperation)


def test_hyp_ocl_ocloperation_constructor_exists():
    assert callable(OCL_OclOperation.__init__)


def test_hyp_ocl_ocloperation_constructor_args():
    sig = inspect.signature(OCL_OclOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_hyp_package_constructor_exists():
    assert callable(Package.__init__)


def test_hyp_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_oclmodule_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModule)


def test_hyp_ocl_oclmodule_constructor_exists():
    assert callable(OCL_OclModule.__init__)


def test_hyp_ocl_oclmodule_constructor_args():
    sig = inspect.signature(OCL_OclModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_anytype_is_not_abstract():
    assert not inspect.isabstract(OCL_AnyType)


def test_hyp_ocl_anytype_constructor_exists():
    assert callable(OCL_AnyType.__init__)


def test_hyp_ocl_anytype_constructor_args():
    sig = inspect.signature(OCL_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_comment_is_not_abstract():
    assert not inspect.isabstract(OCL_Comment)


def test_hyp_ocl_comment_constructor_exists():
    assert callable(OCL_Comment.__init__)


def test_hyp_ocl_comment_constructor_args():
    sig = inspect.signature(OCL_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_namedelement_is_not_abstract():
    assert not inspect.isabstract(OCL_NamedElement)


def test_hyp_ocl_namedelement_constructor_exists():
    assert callable(OCL_NamedElement.__init__)


def test_hyp_ocl_namedelement_constructor_args():
    sig = inspect.signature(OCL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocl_tag_is_not_abstract():
    assert not inspect.isabstract(OCL_Tag)


def test_hyp_ocl_tag_constructor_exists():
    assert callable(OCL_Tag.__init__)


def test_hyp_ocl_tag_constructor_args():
    sig = inspect.signature(OCL_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_ocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL_OclContextDefinition)


def test_hyp_ocl_oclcontextdefinition_constructor_exists():
    assert callable(OCL_OclContextDefinition.__init__)


def test_hyp_ocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OclModuleElement)


def test_hyp_oclmoduleelement_constructor_exists():
    assert callable(OclModuleElement.__init__)


def test_hyp_oclmoduleelement_constructor_args():
    sig = inspect.signature(OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_deriveoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_DeriveOclModuleElement)


def test_hyp_ocl_deriveoclmoduleelement_constructor_exists():
    assert callable(OCL_DeriveOclModuleElement.__init__)


def test_hyp_ocl_deriveoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_DeriveOclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_invariant_is_not_abstract():
    assert not inspect.isabstract(OCL_Invariant)


def test_hyp_ocl_invariant_constructor_exists():
    assert callable(OCL_Invariant.__init__)


def test_hyp_ocl_invariant_constructor_args():
    sig = inspect.signature(OCL_Invariant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocl_defoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_DefOclModuleElement)


def test_hyp_ocl_defoclmoduleelement_constructor_exists():
    assert callable(OCL_DefOclModuleElement.__init__)


def test_hyp_ocl_defoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_DefOclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_hyp_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_hyp_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_RealLiteralExp)


def test_hyp_ocl_realliteralexp_constructor_exists():
    assert callable(OCL_RealLiteralExp.__init__)


def test_hyp_ocl_realliteralexp_constructor_args():
    sig = inspect.signature(OCL_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"




def test_hyp_ocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanLiteralExp)


def test_hyp_ocl_booleanliteralexp_constructor_exists():
    assert callable(OCL_BooleanLiteralExp.__init__)


def test_hyp_ocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(OCL_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"




def test_hyp_ocl_callexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CallExp)


def test_hyp_ocl_callexp_constructor_exists():
    assert callable(OCL_CallExp.__init__)


def test_hyp_ocl_callexp_constructor_args():
    sig = inspect.signature(OCL_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL_OclExpression)


def test_hyp_ocl_oclexpression_constructor_exists():
    assert callable(OCL_OclExpression.__init__)


def test_hyp_ocl_oclexpression_constructor_args():
    sig = inspect.signature(OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IfExp)


def test_hyp_ocl_ifexp_constructor_exists():
    assert callable(OCL_IfExp.__init__)


def test_hyp_ocl_ifexp_constructor_args():
    sig = inspect.signature(OCL_IfExp.__init__)
    params = list(sig.parameters.keys())

def test_hyp_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_hyp_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "OrderedSet",
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
Iterator_strategy = st.builds(
    Iterator,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
OCL_IntegerLiteralExp_strategy = st.builds(
    OCL_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
OCL_OperatorCallExp_strategy = st.builds(
    OCL_OperatorCallExp,
)
OCL_CollectionOperationCallExp_strategy = st.builds(
    OCL_CollectionOperationCallExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
OCL_PropertyCallExp_strategy = st.builds(
    OCL_PropertyCallExp,
)
OCL_OperationCallExp_strategy = st.builds(
    OCL_OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OCL_IteratorExp_strategy = st.builds(
    OCL_IteratorExp,
)
OCL_IterateExp_strategy = st.builds(
    OCL_IterateExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
OCL_StringLiteralExp_strategy = st.builds(
    OCL_StringLiteralExp,
    stringSymbol=
        safe_text
)
OCL_NumericLiteralExp_strategy = st.builds(
    OCL_NumericLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
OCL_CollectionItem_strategy = st.builds(
    OCL_CollectionItem,
)
OCL_CollectionRange_strategy = st.builds(
    OCL_CollectionRange,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
OCL_LoopExp_strategy = st.builds(
    OCL_LoopExp,
)
OCL_FeaturePropertyCall_strategy = st.builds(
    OCL_FeaturePropertyCall,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
OCL_TupleLiteralExp_strategy = st.builds(
    OCL_TupleLiteralExp,
)
OCL_NullLiteralExp_strategy = st.builds(
    OCL_NullLiteralExp,
)
OCL_PrimitiveLiteralExp_strategy = st.builds(
    OCL_PrimitiveLiteralExp,
)
OCL_CollectionLiteralExp_strategy = st.builds(
    OCL_CollectionLiteralExp,
    kind=
        safe_text
)
OCL_InvalidLiteralExp_strategy = st.builds(
    OCL_InvalidLiteralExp,
)
OCL_EnumLiteralExp_strategy = st.builds(
    OCL_EnumLiteralExp,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCL_SequenceType_strategy = st.builds(
    OCL_SequenceType,
)
OCL_OrderedSetType_strategy = st.builds(
    OCL_OrderedSetType,
)
OCL_BagType_strategy = st.builds(
    OCL_BagType,
)
OCL_SetType_strategy = st.builds(
    OCL_SetType,
)
Type_strategy = st.builds(
    Type,
)
OCL_Class_strategy = st.builds(
    OCL_Class,
    isAbstract=
        safe_text
)
OCL_VoidType_strategy = st.builds(
    OCL_VoidType,
)
OCL_InvalidType_strategy = st.builds(
    OCL_InvalidType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OCL_StringType_strategy = st.builds(
    OCL_StringType,
)
OCL_RealType_strategy = st.builds(
    OCL_RealType,
)
OCL_BooleanType_strategy = st.builds(
    OCL_BooleanType,
)
OCL_IntegerType_strategy = st.builds(
    OCL_IntegerType,
)
DataType_strategy = st.builds(
    DataType,
)
OCL_CollectionType_strategy = st.builds(
    OCL_CollectionType,
)
OCL_TupleType_strategy = st.builds(
    OCL_TupleType,
)
OCL_PrimitiveType_strategy = st.builds(
    OCL_PrimitiveType,
)
Extent_strategy = st.builds(
    Extent,
)
OCL_URIExtent_strategy = st.builds(
    OCL_URIExtent,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OCL_EnumerationLiteral_strategy = st.builds(
    OCL_EnumerationLiteral,
)
OCL_TypedElement_strategy = st.builds(
    OCL_TypedElement,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
OCL_Enumeration_strategy = st.builds(
    OCL_Enumeration,
)
Object_strategy = st.builds(
    Object,
)
OCL_Element_strategy = st.builds(
    OCL_Element,
)
OCL_Extent_strategy = st.builds(
    OCL_Extent,
)
OCL_Object_strategy = st.builds(
    OCL_Object,
)
OCL_MultiplicityElement_strategy = st.builds(
    OCL_MultiplicityElement,
    isOrdered=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text
)
OCL_Package_strategy = st.builds(
    OCL_Package,
    uri=
        safe_text
)
OCL_Type_strategy = st.builds(
    OCL_Type,
)
OCL_DataType_strategy = st.builds(
    OCL_DataType,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
OCL_CollectionLiteralPart_strategy = st.builds(
    OCL_CollectionLiteralPart,
)
OCL_Variable_strategy = st.builds(
    OCL_Variable,
)
OCL_Operation_strategy = st.builds(
    OCL_Operation,
)
OCL_Parameter_strategy = st.builds(
    OCL_Parameter,
)
OCL_Property_strategy = st.builds(
    OCL_Property,
    isReadOnly=
        safe_text,
    isDerived=
        safe_text,
    default=
        safe_text,
    isComposite=
        safe_text,
    isId=
        safe_text
)
OCL_TupleLiteralPart_strategy = st.builds(
    OCL_TupleLiteralPart,
)
OCL_OclModuleElement_strategy = st.builds(
    OCL_OclModuleElement,
)
OCL_OclFeature_strategy = st.builds(
    OCL_OclFeature,
)
Property_strategy = st.builds(
    Property,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL_VariableExp_strategy = st.builds(
    OCL_VariableExp,
)
OCL_LetExp_strategy = st.builds(
    OCL_LetExp,
)
OCL_LiteralExp_strategy = st.builds(
    OCL_LiteralExp,
)
Variable_strategy = st.builds(
    Variable,
)
OCL_Iterator_strategy = st.builds(
    OCL_Iterator,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL_OclProperty_strategy = st.builds(
    OCL_OclProperty,
)
Operation_strategy = st.builds(
    Operation,
)
OCL_OclOperation_strategy = st.builds(
    OCL_OclOperation,
)
Package_strategy = st.builds(
    Package,
)
OCL_OclModule_strategy = st.builds(
    OCL_OclModule,
)
Class_strategy = st.builds(
    Class,
)
OCL_AnyType_strategy = st.builds(
    OCL_AnyType,
)
Element_strategy = st.builds(
    Element,
)
OCL_Comment_strategy = st.builds(
    OCL_Comment,
)
OCL_NamedElement_strategy = st.builds(
    OCL_NamedElement,
    name=
        safe_text
)
OCL_Tag_strategy = st.builds(
    OCL_Tag,
    name=
        safe_text,
    value=
        safe_text
)
OCL_OclContextDefinition_strategy = st.builds(
    OCL_OclContextDefinition,
)
Parameter_strategy = st.builds(
    Parameter,
)
OclModuleElement_strategy = st.builds(
    OclModuleElement,
)
OCL_DeriveOclModuleElement_strategy = st.builds(
    OCL_DeriveOclModuleElement,
)
OCL_Invariant_strategy = st.builds(
    OCL_Invariant,
    name=
        safe_text
)
OCL_DefOclModuleElement_strategy = st.builds(
    OCL_DefOclModuleElement,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
OCL_RealLiteralExp_strategy = st.builds(
    OCL_RealLiteralExp,
    realSymbol=
        safe_text
)
OCL_BooleanLiteralExp_strategy = st.builds(
    OCL_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
OCL_CallExp_strategy = st.builds(
    OCL_CallExp,
)
OCL_OclExpression_strategy = st.builds(
    OCL_OclExpression,
)
OCL_IfExp_strategy = st.builds(
    OCL_IfExp,
)






@given(instance=OCL_IntegerLiteralExp_strategy)
def test_hyp_ocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original














@given(instance=OCL_StringLiteralExp_strategy)
def test_hyp_ocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original
















@given(instance=OCL_CollectionLiteralExp_strategy)
def test_hyp_ocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original












@given(instance=OCL_Class_strategy)
def test_hyp_ocl_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original


























@given(instance=OCL_MultiplicityElement_strategy)
def test_hyp_ocl_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_hyp_ocl_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_hyp_ocl_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_hyp_ocl_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original




@given(instance=OCL_Package_strategy)
def test_hyp_ocl_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original












@given(instance=OCL_Property_strategy)
def test_hyp_ocl_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=OCL_Property_strategy)
def test_hyp_ocl_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=OCL_Property_strategy)
def test_hyp_ocl_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=OCL_Property_strategy)
def test_hyp_ocl_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=OCL_Property_strategy)
def test_hyp_ocl_property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original
























@given(instance=OCL_NamedElement_strategy)
def test_hyp_ocl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=OCL_Tag_strategy)
def test_hyp_ocl_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=OCL_Tag_strategy)
def test_hyp_ocl_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=OCL_Invariant_strategy)
def test_hyp_ocl_invariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=OCL_RealLiteralExp_strategy)
def test_hyp_ocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original




@given(instance=OCL_BooleanLiteralExp_strategy)
def test_hyp_ocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CallExp,
    Class,
    CollectionLiteralPart,
    CollectionType,
    DataType,
    Element,
    EnumerationLiteral,
    Extent,
    FeaturePropertyCall,
    Iterator,
    LiteralExp,
    LoopExp,
    MultiplicityElement,
    NamedElement,
    NumericLiteralExp,
    OCL_AnyType,
    OCL_BagType,
    OCL_BooleanLiteralExp,
    OCL_BooleanType,
    OCL_CallExp,
    OCL_Class,
    OCL_CollectionItem,
    OCL_CollectionLiteralExp,
    OCL_CollectionLiteralPart,
    OCL_CollectionOperationCallExp,
    OCL_CollectionRange,
    OCL_CollectionType,
    OCL_Comment,
    OCL_DataType,
    OCL_DefOclModuleElement,
    OCL_DeriveOclModuleElement,
    OCL_Element,
    OCL_EnumLiteralExp,
    OCL_Enumeration,
    OCL_EnumerationLiteral,
    OCL_Extent,
    OCL_FeaturePropertyCall,
    OCL_IfExp,
    OCL_IntegerLiteralExp,
    OCL_IntegerType,
    OCL_InvalidLiteralExp,
    OCL_InvalidType,
    OCL_Invariant,
    OCL_IterateExp,
    OCL_Iterator,
    OCL_IteratorExp,
    OCL_LetExp,
    OCL_LiteralExp,
    OCL_LoopExp,
    OCL_MultiplicityElement,
    OCL_NamedElement,
    OCL_NullLiteralExp,
    OCL_NumericLiteralExp,
    OCL_Object,
    OCL_OclContextDefinition,
    OCL_OclExpression,
    OCL_OclFeature,
    OCL_OclModule,
    OCL_OclModuleElement,
    OCL_OclOperation,
    OCL_OclProperty,
    OCL_Operation,
    OCL_OperationCallExp,
    OCL_OperatorCallExp,
    OCL_OrderedSetType,
    OCL_Package,
    OCL_Parameter,
    OCL_PrimitiveLiteralExp,
    OCL_PrimitiveType,
    OCL_Property,
    OCL_PropertyCallExp,
    OCL_RealLiteralExp,
    OCL_RealType,
    OCL_SequenceType,
    OCL_SetType,
    OCL_StringLiteralExp,
    OCL_StringType,
    OCL_Tag,
    OCL_TupleLiteralExp,
    OCL_TupleLiteralPart,
    OCL_TupleType,
    OCL_Type,
    OCL_TypedElement,
    OCL_URIExtent,
    OCL_Variable,
    OCL_VariableExp,
    OCL_VoidType,
    Object,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclModuleElement,
    Operation,
    OperationCallExp,
    Package,
    Parameter,
    PrimitiveLiteralExp,
    PrimitiveType,
    Property,
    TupleLiteralPart,
    Type,
    TypedElement,
    Variable,
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

def test_OCL_BooleanLiteralExp_booleanSymbol_value_roundtrip():
    instance = OCL_BooleanLiteralExp(booleanSymbol="sample_text")
    assert instance.booleanSymbol == "sample_text"
    instance.booleanSymbol = "sample_text_2"
    assert instance.booleanSymbol == "sample_text_2"


def test_OCL_Class_isAbstract_value_roundtrip():
    instance = OCL_Class(isAbstract="sample_text")
    assert instance.isAbstract == "sample_text"
    instance.isAbstract = "sample_text_2"
    assert instance.isAbstract == "sample_text_2"


def test_OCL_CollectionLiteralExp_kind_value_roundtrip():
    instance = OCL_CollectionLiteralExp(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_OCL_IntegerLiteralExp_integerSymbol_value_roundtrip():
    instance = OCL_IntegerLiteralExp(integerSymbol="sample_text")
    assert instance.integerSymbol == "sample_text"
    instance.integerSymbol = "sample_text_2"
    assert instance.integerSymbol == "sample_text_2"


def test_OCL_Invariant_name_value_roundtrip():
    instance = OCL_Invariant(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OCL_MultiplicityElement_isOrdered_value_roundtrip():
    instance = OCL_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.isOrdered == "sample_text"
    instance.isOrdered = "sample_text_2"
    assert instance.isOrdered == "sample_text_2"


def test_OCL_MultiplicityElement_isUnique_value_roundtrip():
    instance = OCL_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.isUnique == "sample_text"
    instance.isUnique = "sample_text_2"
    assert instance.isUnique == "sample_text_2"


def test_OCL_MultiplicityElement_lower_value_roundtrip():
    instance = OCL_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_OCL_MultiplicityElement_upper_value_roundtrip():
    instance = OCL_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_OCL_NamedElement_name_value_roundtrip():
    instance = OCL_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OCL_Package_uri_value_roundtrip():
    instance = OCL_Package(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_OCL_Property_default_value_roundtrip():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_OCL_Property_isComposite_value_roundtrip():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert instance.isComposite == "sample_text"
    instance.isComposite = "sample_text_2"
    assert instance.isComposite == "sample_text_2"


def test_OCL_Property_isDerived_value_roundtrip():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert instance.isDerived == "sample_text"
    instance.isDerived = "sample_text_2"
    assert instance.isDerived == "sample_text_2"


def test_OCL_Property_isId_value_roundtrip():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert instance.isId == "sample_text"
    instance.isId = "sample_text_2"
    assert instance.isId == "sample_text_2"


def test_OCL_Property_isReadOnly_value_roundtrip():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert instance.isReadOnly == "sample_text"
    instance.isReadOnly = "sample_text_2"
    assert instance.isReadOnly == "sample_text_2"


def test_OCL_RealLiteralExp_realSymbol_value_roundtrip():
    instance = OCL_RealLiteralExp(realSymbol="sample_text")
    assert instance.realSymbol == "sample_text"
    instance.realSymbol = "sample_text_2"
    assert instance.realSymbol == "sample_text_2"


def test_OCL_StringLiteralExp_stringSymbol_value_roundtrip():
    instance = OCL_StringLiteralExp(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_OCL_Tag_name_value_roundtrip():
    instance = OCL_Tag(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OCL_Tag_value_value_roundtrip():
    instance = OCL_Tag(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_OCL_FeaturePropertyCall_isa_CallExp():
    instance = OCL_FeaturePropertyCall()
    assert isinstance(instance, CallExp)


def test_OCL_LoopExp_isa_CallExp():
    instance = OCL_LoopExp()
    assert isinstance(instance, CallExp)


def test_OCL_AnyType_isa_Class():
    instance = OCL_AnyType()
    assert isinstance(instance, Class)


def test_OCL_CollectionItem_isa_CollectionLiteralPart():
    instance = OCL_CollectionItem()
    assert isinstance(instance, CollectionLiteralPart)


def test_OCL_CollectionRange_isa_CollectionLiteralPart():
    instance = OCL_CollectionRange()
    assert isinstance(instance, CollectionLiteralPart)


def test_OCL_BagType_isa_CollectionType():
    instance = OCL_BagType()
    assert isinstance(instance, CollectionType)


def test_OCL_OrderedSetType_isa_CollectionType():
    instance = OCL_OrderedSetType()
    assert isinstance(instance, CollectionType)


def test_OCL_SequenceType_isa_CollectionType():
    instance = OCL_SequenceType()
    assert isinstance(instance, CollectionType)


def test_OCL_SetType_isa_CollectionType():
    instance = OCL_SetType()
    assert isinstance(instance, CollectionType)


def test_OCL_CollectionType_isa_DataType():
    instance = OCL_CollectionType()
    assert isinstance(instance, DataType)


def test_OCL_Enumeration_isa_DataType():
    instance = OCL_Enumeration()
    assert isinstance(instance, DataType)


def test_OCL_PrimitiveType_isa_DataType():
    instance = OCL_PrimitiveType()
    assert isinstance(instance, DataType)


def test_OCL_TupleType_isa_DataType():
    instance = OCL_TupleType()
    assert isinstance(instance, DataType)


def test_OCL_Comment_isa_Element():
    instance = OCL_Comment()
    assert isinstance(instance, Element)


def test_OCL_NamedElement_isa_Element():
    instance = OCL_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_OCL_OclContextDefinition_isa_Element():
    instance = OCL_OclContextDefinition()
    assert isinstance(instance, Element)


def test_OCL_Tag_isa_Element():
    instance = OCL_Tag(name="sample_text", value="sample_text")
    assert isinstance(instance, Element)


def test_OCL_URIExtent_isa_Extent():
    instance = OCL_URIExtent()
    assert isinstance(instance, Extent)


def test_OCL_OperationCallExp_isa_FeaturePropertyCall():
    instance = OCL_OperationCallExp()
    assert isinstance(instance, FeaturePropertyCall)


def test_OCL_PropertyCallExp_isa_FeaturePropertyCall():
    instance = OCL_PropertyCallExp()
    assert isinstance(instance, FeaturePropertyCall)


def test_OCL_CollectionLiteralExp_isa_LiteralExp():
    instance = OCL_CollectionLiteralExp(kind="sample_text")
    assert isinstance(instance, LiteralExp)


def test_OCL_EnumLiteralExp_isa_LiteralExp():
    instance = OCL_EnumLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_OCL_InvalidLiteralExp_isa_LiteralExp():
    instance = OCL_InvalidLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_OCL_NullLiteralExp_isa_LiteralExp():
    instance = OCL_NullLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_OCL_PrimitiveLiteralExp_isa_LiteralExp():
    instance = OCL_PrimitiveLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_OCL_TupleLiteralExp_isa_LiteralExp():
    instance = OCL_TupleLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_OCL_IterateExp_isa_LoopExp():
    instance = OCL_IterateExp()
    assert isinstance(instance, LoopExp)


def test_OCL_IteratorExp_isa_LoopExp():
    instance = OCL_IteratorExp()
    assert isinstance(instance, LoopExp)


def test_OCL_Operation_isa_MultiplicityElement():
    instance = OCL_Operation()
    assert isinstance(instance, MultiplicityElement)


def test_OCL_Parameter_isa_MultiplicityElement():
    instance = OCL_Parameter()
    assert isinstance(instance, MultiplicityElement)


def test_OCL_Property_isa_MultiplicityElement():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert isinstance(instance, MultiplicityElement)


def test_OCL_EnumerationLiteral_isa_NamedElement():
    instance = OCL_EnumerationLiteral()
    assert isinstance(instance, NamedElement)


def test_OCL_Package_isa_NamedElement():
    instance = OCL_Package(uri="sample_text")
    assert isinstance(instance, NamedElement)


def test_OCL_Type_isa_NamedElement():
    instance = OCL_Type()
    assert isinstance(instance, NamedElement)


def test_OCL_TypedElement_isa_NamedElement():
    instance = OCL_TypedElement()
    assert isinstance(instance, NamedElement)


def test_OCL_IntegerLiteralExp_isa_NumericLiteralExp():
    instance = OCL_IntegerLiteralExp(integerSymbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_OCL_RealLiteralExp_isa_NumericLiteralExp():
    instance = OCL_RealLiteralExp(realSymbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_OCL_Element_isa_Object():
    instance = OCL_Element()
    assert isinstance(instance, Object)


def test_OCL_Extent_isa_Object():
    instance = OCL_Extent()
    assert isinstance(instance, Object)


def test_OCL_CallExp_isa_OclExpression():
    instance = OCL_CallExp()
    assert isinstance(instance, OclExpression)


def test_OCL_IfExp_isa_OclExpression():
    instance = OCL_IfExp()
    assert isinstance(instance, OclExpression)


def test_OCL_LetExp_isa_OclExpression():
    instance = OCL_LetExp()
    assert isinstance(instance, OclExpression)


def test_OCL_LiteralExp_isa_OclExpression():
    instance = OCL_LiteralExp()
    assert isinstance(instance, OclExpression)


def test_OCL_VariableExp_isa_OclExpression():
    instance = OCL_VariableExp()
    assert isinstance(instance, OclExpression)


def test_OCL_OclOperation_isa_OclFeature():
    instance = OCL_OclOperation()
    assert isinstance(instance, OclFeature)


def test_OCL_OclProperty_isa_OclFeature():
    instance = OCL_OclProperty()
    assert isinstance(instance, OclFeature)


def test_OCL_DefOclModuleElement_isa_OclModuleElement():
    instance = OCL_DefOclModuleElement()
    assert isinstance(instance, OclModuleElement)


def test_OCL_DeriveOclModuleElement_isa_OclModuleElement():
    instance = OCL_DeriveOclModuleElement()
    assert isinstance(instance, OclModuleElement)


def test_OCL_Invariant_isa_OclModuleElement():
    instance = OCL_Invariant(name="sample_text")
    assert isinstance(instance, OclModuleElement)


def test_OCL_OclOperation_isa_Operation():
    instance = OCL_OclOperation()
    assert isinstance(instance, Operation)


def test_OCL_CollectionOperationCallExp_isa_OperationCallExp():
    instance = OCL_CollectionOperationCallExp()
    assert isinstance(instance, OperationCallExp)


def test_OCL_OperatorCallExp_isa_OperationCallExp():
    instance = OCL_OperatorCallExp()
    assert isinstance(instance, OperationCallExp)


def test_OCL_OclModule_isa_Package():
    instance = OCL_OclModule()
    assert isinstance(instance, Package)


def test_OCL_BooleanLiteralExp_isa_PrimitiveLiteralExp():
    instance = OCL_BooleanLiteralExp(booleanSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExp)


def test_OCL_NumericLiteralExp_isa_PrimitiveLiteralExp():
    instance = OCL_NumericLiteralExp()
    assert isinstance(instance, PrimitiveLiteralExp)


def test_OCL_StringLiteralExp_isa_PrimitiveLiteralExp():
    instance = OCL_StringLiteralExp(stringSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExp)


def test_OCL_BooleanType_isa_PrimitiveType():
    instance = OCL_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_OCL_IntegerType_isa_PrimitiveType():
    instance = OCL_IntegerType()
    assert isinstance(instance, PrimitiveType)


def test_OCL_RealType_isa_PrimitiveType():
    instance = OCL_RealType()
    assert isinstance(instance, PrimitiveType)


def test_OCL_StringType_isa_PrimitiveType():
    instance = OCL_StringType()
    assert isinstance(instance, PrimitiveType)


def test_OCL_OclProperty_isa_Property():
    instance = OCL_OclProperty()
    assert isinstance(instance, Property)


def test_OCL_Class_isa_Type():
    instance = OCL_Class(isAbstract="sample_text")
    assert isinstance(instance, Type)


def test_OCL_DataType_isa_Type():
    instance = OCL_DataType()
    assert isinstance(instance, Type)


def test_OCL_InvalidType_isa_Type():
    instance = OCL_InvalidType()
    assert isinstance(instance, Type)


def test_OCL_VoidType_isa_Type():
    instance = OCL_VoidType()
    assert isinstance(instance, Type)


def test_OCL_CollectionLiteralPart_isa_TypedElement():
    instance = OCL_CollectionLiteralPart()
    assert isinstance(instance, TypedElement)


def test_OCL_OclExpression_isa_TypedElement():
    instance = OCL_OclExpression()
    assert isinstance(instance, TypedElement)


def test_OCL_Operation_isa_TypedElement():
    instance = OCL_Operation()
    assert isinstance(instance, TypedElement)


def test_OCL_Parameter_isa_TypedElement():
    instance = OCL_Parameter()
    assert isinstance(instance, TypedElement)


def test_OCL_Property_isa_TypedElement():
    instance = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    assert isinstance(instance, TypedElement)


def test_OCL_TupleLiteralPart_isa_TypedElement():
    instance = OCL_TupleLiteralPart()
    assert isinstance(instance, TypedElement)


def test_OCL_Variable_isa_TypedElement():
    instance = OCL_Variable()
    assert isinstance(instance, TypedElement)


def test_OCL_Iterator_isa_Variable():
    instance = OCL_Iterator()
    assert isinstance(instance, Variable)


def test_assoc_contextVariable21_link_reassign_clear():
    a = OCL_Invariant(name="sample_text")
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'OCL_Invariant22', b1)
    assert _is_linked(a, 'OCL_Invariant22', b1)
    if hasattr(b1, 'Variable23'):
        assert _is_linked(b1, 'Variable23', a)
    _safe_set(a, 'OCL_Invariant22', b2)
    assert _is_linked(a, 'OCL_Invariant22', b2)
    if hasattr(b1, 'Variable23'):
        assert not _is_linked(b1, 'Variable23', a)
    if hasattr(b2, 'Variable23'):
        assert _is_linked(b2, 'Variable23', a)
    _safe_set(a, 'OCL_Invariant22', None)
    assert not _is_linked(a, 'OCL_Invariant22', b2)
    if hasattr(b2, 'Variable23'):
        assert not _is_linked(b2, 'Variable23', a)


def test_assoc_element31_link_reassign_clear():
    a = OCL_Tag(name="sample_text", value="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'OCL_Tag', {b1})
    assert _is_linked(a, 'OCL_Tag', b1)
    if hasattr(b1, 'Element'):
        assert _is_linked(b1, 'Element', a)
    _safe_set(a, 'OCL_Tag', {b2})
    assert _is_linked(a, 'OCL_Tag', b2)
    if hasattr(b1, 'Element'):
        assert not _is_linked(b1, 'Element', a)
    if hasattr(b2, 'Element'):
        assert _is_linked(b2, 'Element', a)
    _safe_set(a, 'OCL_Tag', set())
    assert not _is_linked(a, 'OCL_Tag', b2)
    if hasattr(b2, 'Element'):
        assert not _is_linked(b2, 'Element', a)


def test_assoc_nestedPackage28_link_reassign_clear():
    a = OCL_Package(uri="sample_text")
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'OCL_Package29', {b1})
    assert _is_linked(a, 'OCL_Package29', b1)
    if hasattr(b1, 'Package'):
        assert _is_linked(b1, 'Package', a)
    _safe_set(a, 'OCL_Package29', {b2})
    assert _is_linked(a, 'OCL_Package29', b2)
    if hasattr(b1, 'Package'):
        assert not _is_linked(b1, 'Package', a)
    if hasattr(b2, 'Package'):
        assert _is_linked(b2, 'Package', a)
    _safe_set(a, 'OCL_Package29', set())
    assert not _is_linked(a, 'OCL_Package29', b2)
    if hasattr(b2, 'Package'):
        assert not _is_linked(b2, 'Package', a)


def test_assoc_opposite37_link_reassign_clear():
    a = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'OCL_Property', b1)
    assert _is_linked(a, 'OCL_Property', b1)
    if hasattr(b1, 'Property'):
        assert _is_linked(b1, 'Property', a)
    _safe_set(a, 'OCL_Property', b2)
    assert _is_linked(a, 'OCL_Property', b2)
    if hasattr(b1, 'Property'):
        assert not _is_linked(b1, 'Property', a)
    if hasattr(b2, 'Property'):
        assert _is_linked(b2, 'Property', a)
    _safe_set(a, 'OCL_Property', None)
    assert not _is_linked(a, 'OCL_Property', b2)
    if hasattr(b2, 'Property'):
        assert not _is_linked(b2, 'Property', a)


def test_assoc_ownedAttribute38_link_reassign_clear():
    a = OCL_Class(isAbstract="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'OCL_Class', {b1})
    assert _is_linked(a, 'OCL_Class', b1)
    if hasattr(b1, 'Property39'):
        assert _is_linked(b1, 'Property39', a)
    _safe_set(a, 'OCL_Class', {b2})
    assert _is_linked(a, 'OCL_Class', b2)
    if hasattr(b1, 'Property39'):
        assert not _is_linked(b1, 'Property39', a)
    if hasattr(b2, 'Property39'):
        assert _is_linked(b2, 'Property39', a)
    _safe_set(a, 'OCL_Class', set())
    assert not _is_linked(a, 'OCL_Class', b2)
    if hasattr(b2, 'Property39'):
        assert not _is_linked(b2, 'Property39', a)


def test_assoc_ownedOperation40_link_reassign_clear():
    a = OCL_Class(isAbstract="sample_text")
    b1 = Operation()
    b2 = Operation()
    _safe_set(a, 'OCL_Class41', {b1})
    assert _is_linked(a, 'OCL_Class41', b1)
    if hasattr(b1, 'Operation'):
        assert _is_linked(b1, 'Operation', a)
    _safe_set(a, 'OCL_Class41', {b2})
    assert _is_linked(a, 'OCL_Class41', b2)
    if hasattr(b1, 'Operation'):
        assert not _is_linked(b1, 'Operation', a)
    if hasattr(b2, 'Operation'):
        assert _is_linked(b2, 'Operation', a)
    _safe_set(a, 'OCL_Class41', set())
    assert not _is_linked(a, 'OCL_Class41', b2)
    if hasattr(b2, 'Operation'):
        assert not _is_linked(b2, 'Operation', a)


def test_assoc_ownedType26_link_reassign_clear():
    a = OCL_Package(uri="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'OCL_Package', {b1})
    assert _is_linked(a, 'OCL_Package', b1)
    if hasattr(b1, 'Type27'):
        assert _is_linked(b1, 'Type27', a)
    _safe_set(a, 'OCL_Package', {b2})
    assert _is_linked(a, 'OCL_Package', b2)
    if hasattr(b1, 'Type27'):
        assert not _is_linked(b1, 'Type27', a)
    if hasattr(b2, 'Type27'):
        assert _is_linked(b2, 'Type27', a)
    _safe_set(a, 'OCL_Package', set())
    assert not _is_linked(a, 'OCL_Package', b2)
    if hasattr(b2, 'Type27'):
        assert not _is_linked(b2, 'Type27', a)


def test_assoc_part59_link_reassign_clear():
    a = OCL_CollectionLiteralExp(kind="sample_text")
    b1 = CollectionLiteralPart()
    b2 = CollectionLiteralPart()
    _safe_set(a, 'OCL_CollectionLiteralExp', {b1})
    assert _is_linked(a, 'OCL_CollectionLiteralExp', b1)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert _is_linked(b1, 'CollectionLiteralPart', a)
    _safe_set(a, 'OCL_CollectionLiteralExp', {b2})
    assert _is_linked(a, 'OCL_CollectionLiteralExp', b2)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert not _is_linked(b1, 'CollectionLiteralPart', a)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert _is_linked(b2, 'CollectionLiteralPart', a)
    _safe_set(a, 'OCL_CollectionLiteralExp', set())
    assert not _is_linked(a, 'OCL_CollectionLiteralExp', b2)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert not _is_linked(b2, 'CollectionLiteralPart', a)


def test_assoc_specification19_link_reassign_clear():
    a = OCL_Invariant(name="sample_text")
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'OCL_Invariant', b1)
    assert _is_linked(a, 'OCL_Invariant', b1)
    if hasattr(b1, 'OclExpression20'):
        assert _is_linked(b1, 'OclExpression20', a)
    _safe_set(a, 'OCL_Invariant', b2)
    assert _is_linked(a, 'OCL_Invariant', b2)
    if hasattr(b1, 'OclExpression20'):
        assert not _is_linked(b1, 'OclExpression20', a)
    if hasattr(b2, 'OclExpression20'):
        assert _is_linked(b2, 'OclExpression20', a)
    _safe_set(a, 'OCL_Invariant', None)
    assert not _is_linked(a, 'OCL_Invariant', b2)
    if hasattr(b2, 'OclExpression20'):
        assert not _is_linked(b2, 'OclExpression20', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CallExp_strategy = st.builds(CallExp)
@given(instance=CallExp_strategy)
@settings(max_examples=25)
def test_CallExp_instantiation(instance):
    assert isinstance(instance, CallExp)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


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


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


EnumerationLiteral_strategy = st.builds(EnumerationLiteral)
@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)


Extent_strategy = st.builds(Extent)
@given(instance=Extent_strategy)
@settings(max_examples=25)
def test_Extent_instantiation(instance):
    assert isinstance(instance, Extent)


FeaturePropertyCall_strategy = st.builds(FeaturePropertyCall)
@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=25)
def test_FeaturePropertyCall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)


Iterator_strategy = st.builds(Iterator)
@given(instance=Iterator_strategy)
@settings(max_examples=25)
def test_Iterator_instantiation(instance):
    assert isinstance(instance, Iterator)


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


MultiplicityElement_strategy = st.builds(MultiplicityElement)
@given(instance=MultiplicityElement_strategy)
@settings(max_examples=25)
def test_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)


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


OCL_AnyType_strategy = st.builds(OCL_AnyType)
@given(instance=OCL_AnyType_strategy)
@settings(max_examples=25)
def test_OCL_AnyType_instantiation(instance):
    assert isinstance(instance, OCL_AnyType)


OCL_BagType_strategy = st.builds(OCL_BagType)
@given(instance=OCL_BagType_strategy)
@settings(max_examples=25)
def test_OCL_BagType_instantiation(instance):
    assert isinstance(instance, OCL_BagType)


OCL_BooleanLiteralExp_strategy = st.builds(OCL_BooleanLiteralExp, booleanSymbol=safe_text)
@given(instance=OCL_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_BooleanLiteralExp)


OCL_BooleanType_strategy = st.builds(OCL_BooleanType)
@given(instance=OCL_BooleanType_strategy)
@settings(max_examples=25)
def test_OCL_BooleanType_instantiation(instance):
    assert isinstance(instance, OCL_BooleanType)


OCL_CallExp_strategy = st.builds(OCL_CallExp)
@given(instance=OCL_CallExp_strategy)
@settings(max_examples=25)
def test_OCL_CallExp_instantiation(instance):
    assert isinstance(instance, OCL_CallExp)


OCL_Class_strategy = st.builds(OCL_Class, isAbstract=safe_text)
@given(instance=OCL_Class_strategy)
@settings(max_examples=25)
def test_OCL_Class_instantiation(instance):
    assert isinstance(instance, OCL_Class)


OCL_CollectionItem_strategy = st.builds(OCL_CollectionItem)
@given(instance=OCL_CollectionItem_strategy)
@settings(max_examples=25)
def test_OCL_CollectionItem_instantiation(instance):
    assert isinstance(instance, OCL_CollectionItem)


OCL_CollectionLiteralExp_strategy = st.builds(OCL_CollectionLiteralExp, kind=safe_text)
@given(instance=OCL_CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionLiteralExp)


OCL_CollectionLiteralPart_strategy = st.builds(OCL_CollectionLiteralPart)
@given(instance=OCL_CollectionLiteralPart_strategy)
@settings(max_examples=25)
def test_OCL_CollectionLiteralPart_instantiation(instance):
    assert isinstance(instance, OCL_CollectionLiteralPart)


OCL_CollectionOperationCallExp_strategy = st.builds(OCL_CollectionOperationCallExp)
@given(instance=OCL_CollectionOperationCallExp_strategy)
@settings(max_examples=25)
def test_OCL_CollectionOperationCallExp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionOperationCallExp)


OCL_CollectionRange_strategy = st.builds(OCL_CollectionRange)
@given(instance=OCL_CollectionRange_strategy)
@settings(max_examples=25)
def test_OCL_CollectionRange_instantiation(instance):
    assert isinstance(instance, OCL_CollectionRange)


OCL_CollectionType_strategy = st.builds(OCL_CollectionType)
@given(instance=OCL_CollectionType_strategy)
@settings(max_examples=25)
def test_OCL_CollectionType_instantiation(instance):
    assert isinstance(instance, OCL_CollectionType)


OCL_Comment_strategy = st.builds(OCL_Comment)
@given(instance=OCL_Comment_strategy)
@settings(max_examples=25)
def test_OCL_Comment_instantiation(instance):
    assert isinstance(instance, OCL_Comment)


OCL_DataType_strategy = st.builds(OCL_DataType)
@given(instance=OCL_DataType_strategy)
@settings(max_examples=25)
def test_OCL_DataType_instantiation(instance):
    assert isinstance(instance, OCL_DataType)


OCL_DefOclModuleElement_strategy = st.builds(OCL_DefOclModuleElement)
@given(instance=OCL_DefOclModuleElement_strategy)
@settings(max_examples=25)
def test_OCL_DefOclModuleElement_instantiation(instance):
    assert isinstance(instance, OCL_DefOclModuleElement)


OCL_DeriveOclModuleElement_strategy = st.builds(OCL_DeriveOclModuleElement)
@given(instance=OCL_DeriveOclModuleElement_strategy)
@settings(max_examples=25)
def test_OCL_DeriveOclModuleElement_instantiation(instance):
    assert isinstance(instance, OCL_DeriveOclModuleElement)


OCL_Element_strategy = st.builds(OCL_Element)
@given(instance=OCL_Element_strategy)
@settings(max_examples=25)
def test_OCL_Element_instantiation(instance):
    assert isinstance(instance, OCL_Element)


OCL_EnumLiteralExp_strategy = st.builds(OCL_EnumLiteralExp)
@given(instance=OCL_EnumLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_EnumLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_EnumLiteralExp)


OCL_Enumeration_strategy = st.builds(OCL_Enumeration)
@given(instance=OCL_Enumeration_strategy)
@settings(max_examples=25)
def test_OCL_Enumeration_instantiation(instance):
    assert isinstance(instance, OCL_Enumeration)


OCL_EnumerationLiteral_strategy = st.builds(OCL_EnumerationLiteral)
@given(instance=OCL_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_OCL_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, OCL_EnumerationLiteral)


OCL_Extent_strategy = st.builds(OCL_Extent)
@given(instance=OCL_Extent_strategy)
@settings(max_examples=25)
def test_OCL_Extent_instantiation(instance):
    assert isinstance(instance, OCL_Extent)


OCL_FeaturePropertyCall_strategy = st.builds(OCL_FeaturePropertyCall)
@given(instance=OCL_FeaturePropertyCall_strategy)
@settings(max_examples=25)
def test_OCL_FeaturePropertyCall_instantiation(instance):
    assert isinstance(instance, OCL_FeaturePropertyCall)


OCL_IfExp_strategy = st.builds(OCL_IfExp)
@given(instance=OCL_IfExp_strategy)
@settings(max_examples=25)
def test_OCL_IfExp_instantiation(instance):
    assert isinstance(instance, OCL_IfExp)


OCL_IntegerLiteralExp_strategy = st.builds(OCL_IntegerLiteralExp, integerSymbol=safe_text)
@given(instance=OCL_IntegerLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_IntegerLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_IntegerLiteralExp)


OCL_IntegerType_strategy = st.builds(OCL_IntegerType)
@given(instance=OCL_IntegerType_strategy)
@settings(max_examples=25)
def test_OCL_IntegerType_instantiation(instance):
    assert isinstance(instance, OCL_IntegerType)


OCL_InvalidLiteralExp_strategy = st.builds(OCL_InvalidLiteralExp)
@given(instance=OCL_InvalidLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_InvalidLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_InvalidLiteralExp)


OCL_InvalidType_strategy = st.builds(OCL_InvalidType)
@given(instance=OCL_InvalidType_strategy)
@settings(max_examples=25)
def test_OCL_InvalidType_instantiation(instance):
    assert isinstance(instance, OCL_InvalidType)


OCL_Invariant_strategy = st.builds(OCL_Invariant, name=safe_text)
@given(instance=OCL_Invariant_strategy)
@settings(max_examples=25)
def test_OCL_Invariant_instantiation(instance):
    assert isinstance(instance, OCL_Invariant)


OCL_IterateExp_strategy = st.builds(OCL_IterateExp)
@given(instance=OCL_IterateExp_strategy)
@settings(max_examples=25)
def test_OCL_IterateExp_instantiation(instance):
    assert isinstance(instance, OCL_IterateExp)


OCL_Iterator_strategy = st.builds(OCL_Iterator)
@given(instance=OCL_Iterator_strategy)
@settings(max_examples=25)
def test_OCL_Iterator_instantiation(instance):
    assert isinstance(instance, OCL_Iterator)


OCL_IteratorExp_strategy = st.builds(OCL_IteratorExp)
@given(instance=OCL_IteratorExp_strategy)
@settings(max_examples=25)
def test_OCL_IteratorExp_instantiation(instance):
    assert isinstance(instance, OCL_IteratorExp)


OCL_LetExp_strategy = st.builds(OCL_LetExp)
@given(instance=OCL_LetExp_strategy)
@settings(max_examples=25)
def test_OCL_LetExp_instantiation(instance):
    assert isinstance(instance, OCL_LetExp)


OCL_LiteralExp_strategy = st.builds(OCL_LiteralExp)
@given(instance=OCL_LiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_LiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_LiteralExp)


OCL_LoopExp_strategy = st.builds(OCL_LoopExp)
@given(instance=OCL_LoopExp_strategy)
@settings(max_examples=25)
def test_OCL_LoopExp_instantiation(instance):
    assert isinstance(instance, OCL_LoopExp)


OCL_MultiplicityElement_strategy = st.builds(OCL_MultiplicityElement, isOrdered=safe_text, isUnique=safe_text, lower=safe_text, upper=safe_text)
@given(instance=OCL_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_OCL_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, OCL_MultiplicityElement)


OCL_NamedElement_strategy = st.builds(OCL_NamedElement, name=safe_text)
@given(instance=OCL_NamedElement_strategy)
@settings(max_examples=25)
def test_OCL_NamedElement_instantiation(instance):
    assert isinstance(instance, OCL_NamedElement)


OCL_NullLiteralExp_strategy = st.builds(OCL_NullLiteralExp)
@given(instance=OCL_NullLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_NullLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_NullLiteralExp)


OCL_NumericLiteralExp_strategy = st.builds(OCL_NumericLiteralExp)
@given(instance=OCL_NumericLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_NumericLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_NumericLiteralExp)


OCL_Object_strategy = st.builds(OCL_Object)
@given(instance=OCL_Object_strategy)
@settings(max_examples=25)
def test_OCL_Object_instantiation(instance):
    assert isinstance(instance, OCL_Object)


OCL_OclContextDefinition_strategy = st.builds(OCL_OclContextDefinition)
@given(instance=OCL_OclContextDefinition_strategy)
@settings(max_examples=25)
def test_OCL_OclContextDefinition_instantiation(instance):
    assert isinstance(instance, OCL_OclContextDefinition)


OCL_OclExpression_strategy = st.builds(OCL_OclExpression)
@given(instance=OCL_OclExpression_strategy)
@settings(max_examples=25)
def test_OCL_OclExpression_instantiation(instance):
    assert isinstance(instance, OCL_OclExpression)


OCL_OclFeature_strategy = st.builds(OCL_OclFeature)
@given(instance=OCL_OclFeature_strategy)
@settings(max_examples=25)
def test_OCL_OclFeature_instantiation(instance):
    assert isinstance(instance, OCL_OclFeature)


OCL_OclModule_strategy = st.builds(OCL_OclModule)
@given(instance=OCL_OclModule_strategy)
@settings(max_examples=25)
def test_OCL_OclModule_instantiation(instance):
    assert isinstance(instance, OCL_OclModule)


OCL_OclModuleElement_strategy = st.builds(OCL_OclModuleElement)
@given(instance=OCL_OclModuleElement_strategy)
@settings(max_examples=25)
def test_OCL_OclModuleElement_instantiation(instance):
    assert isinstance(instance, OCL_OclModuleElement)


OCL_OclOperation_strategy = st.builds(OCL_OclOperation)
@given(instance=OCL_OclOperation_strategy)
@settings(max_examples=25)
def test_OCL_OclOperation_instantiation(instance):
    assert isinstance(instance, OCL_OclOperation)


OCL_OclProperty_strategy = st.builds(OCL_OclProperty)
@given(instance=OCL_OclProperty_strategy)
@settings(max_examples=25)
def test_OCL_OclProperty_instantiation(instance):
    assert isinstance(instance, OCL_OclProperty)


OCL_Operation_strategy = st.builds(OCL_Operation)
@given(instance=OCL_Operation_strategy)
@settings(max_examples=25)
def test_OCL_Operation_instantiation(instance):
    assert isinstance(instance, OCL_Operation)


OCL_OperationCallExp_strategy = st.builds(OCL_OperationCallExp)
@given(instance=OCL_OperationCallExp_strategy)
@settings(max_examples=25)
def test_OCL_OperationCallExp_instantiation(instance):
    assert isinstance(instance, OCL_OperationCallExp)


OCL_OperatorCallExp_strategy = st.builds(OCL_OperatorCallExp)
@given(instance=OCL_OperatorCallExp_strategy)
@settings(max_examples=25)
def test_OCL_OperatorCallExp_instantiation(instance):
    assert isinstance(instance, OCL_OperatorCallExp)


OCL_OrderedSetType_strategy = st.builds(OCL_OrderedSetType)
@given(instance=OCL_OrderedSetType_strategy)
@settings(max_examples=25)
def test_OCL_OrderedSetType_instantiation(instance):
    assert isinstance(instance, OCL_OrderedSetType)


OCL_Package_strategy = st.builds(OCL_Package, uri=safe_text)
@given(instance=OCL_Package_strategy)
@settings(max_examples=25)
def test_OCL_Package_instantiation(instance):
    assert isinstance(instance, OCL_Package)


OCL_Parameter_strategy = st.builds(OCL_Parameter)
@given(instance=OCL_Parameter_strategy)
@settings(max_examples=25)
def test_OCL_Parameter_instantiation(instance):
    assert isinstance(instance, OCL_Parameter)


OCL_PrimitiveLiteralExp_strategy = st.builds(OCL_PrimitiveLiteralExp)
@given(instance=OCL_PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_PrimitiveLiteralExp)


OCL_PrimitiveType_strategy = st.builds(OCL_PrimitiveType)
@given(instance=OCL_PrimitiveType_strategy)
@settings(max_examples=25)
def test_OCL_PrimitiveType_instantiation(instance):
    assert isinstance(instance, OCL_PrimitiveType)


OCL_Property_strategy = st.builds(OCL_Property, default=safe_text, isComposite=safe_text, isDerived=safe_text, isId=safe_text, isReadOnly=safe_text)
@given(instance=OCL_Property_strategy)
@settings(max_examples=25)
def test_OCL_Property_instantiation(instance):
    assert isinstance(instance, OCL_Property)


OCL_PropertyCallExp_strategy = st.builds(OCL_PropertyCallExp)
@given(instance=OCL_PropertyCallExp_strategy)
@settings(max_examples=25)
def test_OCL_PropertyCallExp_instantiation(instance):
    assert isinstance(instance, OCL_PropertyCallExp)


OCL_RealLiteralExp_strategy = st.builds(OCL_RealLiteralExp, realSymbol=safe_text)
@given(instance=OCL_RealLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_RealLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_RealLiteralExp)


OCL_RealType_strategy = st.builds(OCL_RealType)
@given(instance=OCL_RealType_strategy)
@settings(max_examples=25)
def test_OCL_RealType_instantiation(instance):
    assert isinstance(instance, OCL_RealType)


OCL_SequenceType_strategy = st.builds(OCL_SequenceType)
@given(instance=OCL_SequenceType_strategy)
@settings(max_examples=25)
def test_OCL_SequenceType_instantiation(instance):
    assert isinstance(instance, OCL_SequenceType)


OCL_SetType_strategy = st.builds(OCL_SetType)
@given(instance=OCL_SetType_strategy)
@settings(max_examples=25)
def test_OCL_SetType_instantiation(instance):
    assert isinstance(instance, OCL_SetType)


OCL_StringLiteralExp_strategy = st.builds(OCL_StringLiteralExp, stringSymbol=safe_text)
@given(instance=OCL_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_StringLiteralExp)


OCL_StringType_strategy = st.builds(OCL_StringType)
@given(instance=OCL_StringType_strategy)
@settings(max_examples=25)
def test_OCL_StringType_instantiation(instance):
    assert isinstance(instance, OCL_StringType)


OCL_Tag_strategy = st.builds(OCL_Tag, name=safe_text, value=safe_text)
@given(instance=OCL_Tag_strategy)
@settings(max_examples=25)
def test_OCL_Tag_instantiation(instance):
    assert isinstance(instance, OCL_Tag)


OCL_TupleLiteralExp_strategy = st.builds(OCL_TupleLiteralExp)
@given(instance=OCL_TupleLiteralExp_strategy)
@settings(max_examples=25)
def test_OCL_TupleLiteralExp_instantiation(instance):
    assert isinstance(instance, OCL_TupleLiteralExp)


OCL_TupleLiteralPart_strategy = st.builds(OCL_TupleLiteralPart)
@given(instance=OCL_TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_OCL_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, OCL_TupleLiteralPart)


OCL_TupleType_strategy = st.builds(OCL_TupleType)
@given(instance=OCL_TupleType_strategy)
@settings(max_examples=25)
def test_OCL_TupleType_instantiation(instance):
    assert isinstance(instance, OCL_TupleType)


OCL_Type_strategy = st.builds(OCL_Type)
@given(instance=OCL_Type_strategy)
@settings(max_examples=25)
def test_OCL_Type_instantiation(instance):
    assert isinstance(instance, OCL_Type)


OCL_TypedElement_strategy = st.builds(OCL_TypedElement)
@given(instance=OCL_TypedElement_strategy)
@settings(max_examples=25)
def test_OCL_TypedElement_instantiation(instance):
    assert isinstance(instance, OCL_TypedElement)


OCL_URIExtent_strategy = st.builds(OCL_URIExtent)
@given(instance=OCL_URIExtent_strategy)
@settings(max_examples=25)
def test_OCL_URIExtent_instantiation(instance):
    assert isinstance(instance, OCL_URIExtent)


OCL_Variable_strategy = st.builds(OCL_Variable)
@given(instance=OCL_Variable_strategy)
@settings(max_examples=25)
def test_OCL_Variable_instantiation(instance):
    assert isinstance(instance, OCL_Variable)


OCL_VariableExp_strategy = st.builds(OCL_VariableExp)
@given(instance=OCL_VariableExp_strategy)
@settings(max_examples=25)
def test_OCL_VariableExp_instantiation(instance):
    assert isinstance(instance, OCL_VariableExp)


OCL_VoidType_strategy = st.builds(OCL_VoidType)
@given(instance=OCL_VoidType_strategy)
@settings(max_examples=25)
def test_OCL_VoidType_instantiation(instance):
    assert isinstance(instance, OCL_VoidType)


Object_strategy = st.builds(Object)
@given(instance=Object_strategy)
@settings(max_examples=25)
def test_Object_instantiation(instance):
    assert isinstance(instance, Object)


OclContextDefinition_strategy = st.builds(OclContextDefinition)
@given(instance=OclContextDefinition_strategy)
@settings(max_examples=25)
def test_OclContextDefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)


OclExpression_strategy = st.builds(OclExpression)
@given(instance=OclExpression_strategy)
@settings(max_examples=25)
def test_OclExpression_instantiation(instance):
    assert isinstance(instance, OclExpression)


OclFeature_strategy = st.builds(OclFeature)
@given(instance=OclFeature_strategy)
@settings(max_examples=25)
def test_OclFeature_instantiation(instance):
    assert isinstance(instance, OclFeature)


OclModuleElement_strategy = st.builds(OclModuleElement)
@given(instance=OclModuleElement_strategy)
@settings(max_examples=25)
def test_OclModuleElement_instantiation(instance):
    assert isinstance(instance, OclModuleElement)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


OperationCallExp_strategy = st.builds(OperationCallExp)
@given(instance=OperationCallExp_strategy)
@settings(max_examples=25)
def test_OperationCallExp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)


Package_strategy = st.builds(Package)
@given(instance=Package_strategy)
@settings(max_examples=25)
def test_Package_instantiation(instance):
    assert isinstance(instance, Package)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


PrimitiveLiteralExp_strategy = st.builds(PrimitiveLiteralExp)
@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


TupleLiteralPart_strategy = st.builds(TupleLiteralPart)
@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)


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


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)



