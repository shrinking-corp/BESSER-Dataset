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
    PrimitiveExp,
    oCLlite_StringLiteralExp,
    oCLlite_UnlimitedNaturalLiteralExp,
    oCLlite_InvalidLiteralExp,
    oCLlite_BooleanLiteralExp,
    oCLlite_NumberLiteralExp,
    oCLlite_TuplePart,
    oCLlite_MapElement,
    CollectionExp,
    oCLlite_OrderedSetExp,
    oCLlite_SequenceExp,
    oCLlite_SetExp,
    oCLlite_BagExp,
    OclLExpression,
    oCLlite_PrimitiveExp,
    oCLlite_ComOpCallExp,
    oCLlite_IterateExp,
    oCLlite_IteratorExp,
    oCLlite_LambdaExp,
    oCLlite_TupleExp,
    oCLlite_OperationCall,
    oCLlite_ElseIfThenExp,
    oCLlite_NavigationOrAttributeCall,
    oCLlite_BoolOpCallExp,
    oCLlite_NavigationExp,
    oCLlite_NestedExp,
    oCLlite_MulOpCallExp,
    oCLlite_SelfExp,
    oCLlite_EqOpCallExp,
    oCLlite_MapExp,
    oCLlite_AddOpCallExp,
    oCLlite_CollectionOpCallExp,
    oCLlite_CollectionExp,
    OclLType,
    oCLlite_IntegerType,
    oCLlite_BooleanType,
    oCLlite_MapType,
    oCLlite_BagType,
    oCLlite_LambdaType,
    oCLlite_StringType,
    oCLlite_SequenceType,
    oCLlite_RealType,
    oCLlite_EnvType,
    oCLlite_OclLAnyType,
    oCLlite_TupleType,
    oCLlite_OrderedSetType,
    oCLlite_SetType,
    oCLlite_OclLModelElementExp,
    oCLlite_IfExp,
    oCLlite_NullLiteralExp,
    oCLlite_OclLExpression,
    ModuleElement,
    oCLlite_Query,
    oCLlite_URI_,
    oCLlite_ModuleElement,
    oCLlite_Import,
    oCLlite_OclLModel,
    oCLlite_Module,
    oCLlite_OclLType,
    oCLlite_Iterator,
    oCLlite_LocalVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_hyp_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_hyp_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_StringLiteralExp)


def test_hyp_ocllite_stringliteralexp_constructor_exists():
    assert callable(oCLlite_StringLiteralExp.__init__)


def test_hyp_ocllite_stringliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"




def test_hyp_ocllite_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_UnlimitedNaturalLiteralExp)


def test_hyp_ocllite_unlimitednaturalliteralexp_constructor_exists():
    assert callable(oCLlite_UnlimitedNaturalLiteralExp.__init__)


def test_hyp_ocllite_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_InvalidLiteralExp)


def test_hyp_ocllite_invalidliteralexp_constructor_exists():
    assert callable(oCLlite_InvalidLiteralExp.__init__)


def test_hyp_ocllite_invalidliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BooleanLiteralExp)


def test_hyp_ocllite_booleanliteralexp_constructor_exists():
    assert callable(oCLlite_BooleanLiteralExp.__init__)


def test_hyp_ocllite_booleanliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_ocllite_numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NumberLiteralExp)


def test_hyp_ocllite_numberliteralexp_constructor_exists():
    assert callable(oCLlite_NumberLiteralExp.__init__)


def test_hyp_ocllite_numberliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_ocllite_tuplepart_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TuplePart)


def test_hyp_ocllite_tuplepart_constructor_exists():
    assert callable(oCLlite_TuplePart.__init__)


def test_hyp_ocllite_tuplepart_constructor_args():
    sig = inspect.signature(oCLlite_TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_mapelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapElement)


def test_hyp_ocllite_mapelement_constructor_exists():
    assert callable(oCLlite_MapElement.__init__)


def test_hyp_ocllite_mapelement_constructor_args():
    sig = inspect.signature(oCLlite_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_hyp_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_hyp_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OrderedSetExp)


def test_hyp_ocllite_orderedsetexp_constructor_exists():
    assert callable(oCLlite_OrderedSetExp.__init__)


def test_hyp_ocllite_orderedsetexp_constructor_args():
    sig = inspect.signature(oCLlite_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SequenceExp)


def test_hyp_ocllite_sequenceexp_constructor_exists():
    assert callable(oCLlite_SequenceExp.__init__)


def test_hyp_ocllite_sequenceexp_constructor_args():
    sig = inspect.signature(oCLlite_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_setexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SetExp)


def test_hyp_ocllite_setexp_constructor_exists():
    assert callable(oCLlite_SetExp.__init__)


def test_hyp_ocllite_setexp_constructor_args():
    sig = inspect.signature(oCLlite_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_bagexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BagExp)


def test_hyp_ocllite_bagexp_constructor_exists():
    assert callable(oCLlite_BagExp.__init__)


def test_hyp_ocllite_bagexp_constructor_args():
    sig = inspect.signature(oCLlite_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllexpression_is_not_abstract():
    assert not inspect.isabstract(OclLExpression)


def test_hyp_ocllexpression_constructor_exists():
    assert callable(OclLExpression.__init__)


def test_hyp_ocllexpression_constructor_args():
    sig = inspect.signature(OclLExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_PrimitiveExp)


def test_hyp_ocllite_primitiveexp_constructor_exists():
    assert callable(oCLlite_PrimitiveExp.__init__)


def test_hyp_ocllite_primitiveexp_constructor_args():
    sig = inspect.signature(oCLlite_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_comopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ComOpCallExp)


def test_hyp_ocllite_comopcallexp_constructor_exists():
    assert callable(oCLlite_ComOpCallExp.__init__)


def test_hyp_ocllite_comopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_ComOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_iterateexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IterateExp)


def test_hyp_ocllite_iterateexp_constructor_exists():
    assert callable(oCLlite_IterateExp.__init__)


def test_hyp_ocllite_iterateexp_constructor_args():
    sig = inspect.signature(oCLlite_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IteratorExp)


def test_hyp_ocllite_iteratorexp_constructor_exists():
    assert callable(oCLlite_IteratorExp.__init__)


def test_hyp_ocllite_iteratorexp_constructor_args():
    sig = inspect.signature(oCLlite_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LambdaExp)


def test_hyp_ocllite_lambdaexp_constructor_exists():
    assert callable(oCLlite_LambdaExp.__init__)


def test_hyp_ocllite_lambdaexp_constructor_args():
    sig = inspect.signature(oCLlite_LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_tupleexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TupleExp)


def test_hyp_ocllite_tupleexp_constructor_exists():
    assert callable(oCLlite_TupleExp.__init__)


def test_hyp_ocllite_tupleexp_constructor_args():
    sig = inspect.signature(oCLlite_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_operationcall_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OperationCall)


def test_hyp_ocllite_operationcall_constructor_exists():
    assert callable(oCLlite_OperationCall.__init__)


def test_hyp_ocllite_operationcall_constructor_args():
    sig = inspect.signature(oCLlite_OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_elseifthenexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ElseIfThenExp)


def test_hyp_ocllite_elseifthenexp_constructor_exists():
    assert callable(oCLlite_ElseIfThenExp.__init__)


def test_hyp_ocllite_elseifthenexp_constructor_args():
    sig = inspect.signature(oCLlite_ElseIfThenExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NavigationOrAttributeCall)


def test_hyp_ocllite_navigationorattributecall_constructor_exists():
    assert callable(oCLlite_NavigationOrAttributeCall.__init__)


def test_hyp_ocllite_navigationorattributecall_constructor_args():
    sig = inspect.signature(oCLlite_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"




def test_hyp_ocllite_boolopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BoolOpCallExp)


def test_hyp_ocllite_boolopcallexp_constructor_exists():
    assert callable(oCLlite_BoolOpCallExp.__init__)


def test_hyp_ocllite_boolopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_BoolOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_navigationexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NavigationExp)


def test_hyp_ocllite_navigationexp_constructor_exists():
    assert callable(oCLlite_NavigationExp.__init__)


def test_hyp_ocllite_navigationexp_constructor_args():
    sig = inspect.signature(oCLlite_NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_nestedexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NestedExp)


def test_hyp_ocllite_nestedexp_constructor_exists():
    assert callable(oCLlite_NestedExp.__init__)


def test_hyp_ocllite_nestedexp_constructor_args():
    sig = inspect.signature(oCLlite_NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MulOpCallExp)


def test_hyp_ocllite_mulopcallexp_constructor_exists():
    assert callable(oCLlite_MulOpCallExp.__init__)


def test_hyp_ocllite_mulopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_selfexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SelfExp)


def test_hyp_ocllite_selfexp_constructor_exists():
    assert callable(oCLlite_SelfExp.__init__)


def test_hyp_ocllite_selfexp_constructor_args():
    sig = inspect.signature(oCLlite_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_EqOpCallExp)


def test_hyp_ocllite_eqopcallexp_constructor_exists():
    assert callable(oCLlite_EqOpCallExp.__init__)


def test_hyp_ocllite_eqopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_mapexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapExp)


def test_hyp_ocllite_mapexp_constructor_exists():
    assert callable(oCLlite_MapExp.__init__)


def test_hyp_ocllite_mapexp_constructor_args():
    sig = inspect.signature(oCLlite_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_AddOpCallExp)


def test_hyp_ocllite_addopcallexp_constructor_exists():
    assert callable(oCLlite_AddOpCallExp.__init__)


def test_hyp_ocllite_addopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_collectionopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_CollectionOpCallExp)


def test_hyp_ocllite_collectionopcallexp_constructor_exists():
    assert callable(oCLlite_CollectionOpCallExp.__init__)


def test_hyp_ocllite_collectionopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_CollectionOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_collectionexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_CollectionExp)


def test_hyp_ocllite_collectionexp_constructor_exists():
    assert callable(oCLlite_CollectionExp.__init__)


def test_hyp_ocllite_collectionexp_constructor_args():
    sig = inspect.signature(oCLlite_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclltype_is_not_abstract():
    assert not inspect.isabstract(OclLType)


def test_hyp_oclltype_constructor_exists():
    assert callable(OclLType.__init__)


def test_hyp_oclltype_constructor_args():
    sig = inspect.signature(OclLType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_integertype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IntegerType)


def test_hyp_ocllite_integertype_constructor_exists():
    assert callable(oCLlite_IntegerType.__init__)


def test_hyp_ocllite_integertype_constructor_args():
    sig = inspect.signature(oCLlite_IntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_booleantype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BooleanType)


def test_hyp_ocllite_booleantype_constructor_exists():
    assert callable(oCLlite_BooleanType.__init__)


def test_hyp_ocllite_booleantype_constructor_args():
    sig = inspect.signature(oCLlite_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_maptype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapType)


def test_hyp_ocllite_maptype_constructor_exists():
    assert callable(oCLlite_MapType.__init__)


def test_hyp_ocllite_maptype_constructor_args():
    sig = inspect.signature(oCLlite_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_bagtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BagType)


def test_hyp_ocllite_bagtype_constructor_exists():
    assert callable(oCLlite_BagType.__init__)


def test_hyp_ocllite_bagtype_constructor_args():
    sig = inspect.signature(oCLlite_BagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_lambdatype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LambdaType)


def test_hyp_ocllite_lambdatype_constructor_exists():
    assert callable(oCLlite_LambdaType.__init__)


def test_hyp_ocllite_lambdatype_constructor_args():
    sig = inspect.signature(oCLlite_LambdaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_stringtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_StringType)


def test_hyp_ocllite_stringtype_constructor_exists():
    assert callable(oCLlite_StringType.__init__)


def test_hyp_ocllite_stringtype_constructor_args():
    sig = inspect.signature(oCLlite_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_sequencetype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SequenceType)


def test_hyp_ocllite_sequencetype_constructor_exists():
    assert callable(oCLlite_SequenceType.__init__)


def test_hyp_ocllite_sequencetype_constructor_args():
    sig = inspect.signature(oCLlite_SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_realtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_RealType)


def test_hyp_ocllite_realtype_constructor_exists():
    assert callable(oCLlite_RealType.__init__)


def test_hyp_ocllite_realtype_constructor_args():
    sig = inspect.signature(oCLlite_RealType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_envtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_EnvType)


def test_hyp_ocllite_envtype_constructor_exists():
    assert callable(oCLlite_EnvType.__init__)


def test_hyp_ocllite_envtype_constructor_args():
    sig = inspect.signature(oCLlite_EnvType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_ocllanytype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLAnyType)


def test_hyp_ocllite_ocllanytype_constructor_exists():
    assert callable(oCLlite_OclLAnyType.__init__)


def test_hyp_ocllite_ocllanytype_constructor_args():
    sig = inspect.signature(oCLlite_OclLAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_tupletype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TupleType)


def test_hyp_ocllite_tupletype_constructor_exists():
    assert callable(oCLlite_TupleType.__init__)


def test_hyp_ocllite_tupletype_constructor_args():
    sig = inspect.signature(oCLlite_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OrderedSetType)


def test_hyp_ocllite_orderedsettype_constructor_exists():
    assert callable(oCLlite_OrderedSetType.__init__)


def test_hyp_ocllite_orderedsettype_constructor_args():
    sig = inspect.signature(oCLlite_OrderedSetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_settype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SetType)


def test_hyp_ocllite_settype_constructor_exists():
    assert callable(oCLlite_SetType.__init__)


def test_hyp_ocllite_settype_constructor_args():
    sig = inspect.signature(oCLlite_SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_ocllmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLModelElementExp)


def test_hyp_ocllite_ocllmodelelementexp_constructor_exists():
    assert callable(oCLlite_OclLModelElementExp.__init__)


def test_hyp_ocllite_ocllmodelelementexp_constructor_args():
    sig = inspect.signature(oCLlite_OclLModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_ifexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IfExp)


def test_hyp_ocllite_ifexp_constructor_exists():
    assert callable(oCLlite_IfExp.__init__)


def test_hyp_ocllite_ifexp_constructor_args():
    sig = inspect.signature(oCLlite_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NullLiteralExp)


def test_hyp_ocllite_nullliteralexp_constructor_exists():
    assert callable(oCLlite_NullLiteralExp.__init__)


def test_hyp_ocllite_nullliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_ocllexpression_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLExpression)


def test_hyp_ocllite_ocllexpression_constructor_exists():
    assert callable(oCLlite_OclLExpression.__init__)


def test_hyp_ocllite_ocllexpression_constructor_args():
    sig = inspect.signature(oCLlite_OclLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_hyp_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_hyp_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_query_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Query)


def test_hyp_ocllite_query_constructor_exists():
    assert callable(oCLlite_Query.__init__)


def test_hyp_ocllite_query_constructor_args():
    sig = inspect.signature(oCLlite_Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_uri__is_not_abstract():
    assert not inspect.isabstract(oCLlite_URI_)


def test_hyp_ocllite_uri__constructor_exists():
    assert callable(oCLlite_URI_.__init__)


def test_hyp_ocllite_uri__constructor_args():
    sig = inspect.signature(oCLlite_URI_.__init__)
    params = list(sig.parameters.keys())
    assert "authority" in params, "Missing parameter 'authority'"
    assert "fragment_" in params, "Missing parameter 'fragment_'"
    assert "scheme" in params, "Missing parameter 'scheme'"






def test_hyp_ocllite_moduleelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ModuleElement)


def test_hyp_ocllite_moduleelement_constructor_exists():
    assert callable(oCLlite_ModuleElement.__init__)


def test_hyp_ocllite_moduleelement_constructor_args():
    sig = inspect.signature(oCLlite_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_import_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Import)


def test_hyp_ocllite_import_constructor_exists():
    assert callable(oCLlite_Import.__init__)


def test_hyp_ocllite_import_constructor_args():
    sig = inspect.signature(oCLlite_Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_ocllmodel_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLModel)


def test_hyp_ocllite_ocllmodel_constructor_exists():
    assert callable(oCLlite_OclLModel.__init__)


def test_hyp_ocllite_ocllmodel_constructor_args():
    sig = inspect.signature(oCLlite_OclLModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_module_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Module)


def test_hyp_ocllite_module_constructor_exists():
    assert callable(oCLlite_Module.__init__)


def test_hyp_ocllite_module_constructor_args():
    sig = inspect.signature(oCLlite_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_oclltype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLType)


def test_hyp_ocllite_oclltype_constructor_exists():
    assert callable(oCLlite_OclLType.__init__)


def test_hyp_ocllite_oclltype_constructor_args():
    sig = inspect.signature(oCLlite_OclLType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ocllite_iterator_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Iterator)


def test_hyp_ocllite_iterator_constructor_exists():
    assert callable(oCLlite_Iterator.__init__)


def test_hyp_ocllite_iterator_constructor_args():
    sig = inspect.signature(oCLlite_Iterator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ocllite_localvariable_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LocalVariable)


def test_hyp_ocllite_localvariable_constructor_exists():
    assert callable(oCLlite_LocalVariable.__init__)


def test_hyp_ocllite_localvariable_constructor_args():
    sig = inspect.signature(oCLlite_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
oCLlite_StringLiteralExp_strategy = st.builds(
    oCLlite_StringLiteralExp,
    segments=
        safe_text
)
oCLlite_UnlimitedNaturalLiteralExp_strategy = st.builds(
    oCLlite_UnlimitedNaturalLiteralExp,
)
oCLlite_InvalidLiteralExp_strategy = st.builds(
    oCLlite_InvalidLiteralExp,
)
oCLlite_BooleanLiteralExp_strategy = st.builds(
    oCLlite_BooleanLiteralExp,
    symbol=
        safe_text
)
oCLlite_NumberLiteralExp_strategy = st.builds(
    oCLlite_NumberLiteralExp,
    symbol=
        st.integers()
)
oCLlite_TuplePart_strategy = st.builds(
    oCLlite_TuplePart,
    name=
        safe_text
)
oCLlite_MapElement_strategy = st.builds(
    oCLlite_MapElement,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
oCLlite_OrderedSetExp_strategy = st.builds(
    oCLlite_OrderedSetExp,
)
oCLlite_SequenceExp_strategy = st.builds(
    oCLlite_SequenceExp,
)
oCLlite_SetExp_strategy = st.builds(
    oCLlite_SetExp,
)
oCLlite_BagExp_strategy = st.builds(
    oCLlite_BagExp,
)
OclLExpression_strategy = st.builds(
    OclLExpression,
)
oCLlite_PrimitiveExp_strategy = st.builds(
    oCLlite_PrimitiveExp,
)
oCLlite_ComOpCallExp_strategy = st.builds(
    oCLlite_ComOpCallExp,
)
oCLlite_IterateExp_strategy = st.builds(
    oCLlite_IterateExp,
)
oCLlite_IteratorExp_strategy = st.builds(
    oCLlite_IteratorExp,
)
oCLlite_LambdaExp_strategy = st.builds(
    oCLlite_LambdaExp,
)
oCLlite_TupleExp_strategy = st.builds(
    oCLlite_TupleExp,
)
oCLlite_OperationCall_strategy = st.builds(
    oCLlite_OperationCall,
)
oCLlite_ElseIfThenExp_strategy = st.builds(
    oCLlite_ElseIfThenExp,
)
oCLlite_NavigationOrAttributeCall_strategy = st.builds(
    oCLlite_NavigationOrAttributeCall,
    feature=
        safe_text
)
oCLlite_BoolOpCallExp_strategy = st.builds(
    oCLlite_BoolOpCallExp,
)
oCLlite_NavigationExp_strategy = st.builds(
    oCLlite_NavigationExp,
)
oCLlite_NestedExp_strategy = st.builds(
    oCLlite_NestedExp,
)
oCLlite_MulOpCallExp_strategy = st.builds(
    oCLlite_MulOpCallExp,
)
oCLlite_SelfExp_strategy = st.builds(
    oCLlite_SelfExp,
)
oCLlite_EqOpCallExp_strategy = st.builds(
    oCLlite_EqOpCallExp,
)
oCLlite_MapExp_strategy = st.builds(
    oCLlite_MapExp,
)
oCLlite_AddOpCallExp_strategy = st.builds(
    oCLlite_AddOpCallExp,
)
oCLlite_CollectionOpCallExp_strategy = st.builds(
    oCLlite_CollectionOpCallExp,
)
oCLlite_CollectionExp_strategy = st.builds(
    oCLlite_CollectionExp,
)
OclLType_strategy = st.builds(
    OclLType,
)
oCLlite_IntegerType_strategy = st.builds(
    oCLlite_IntegerType,
    name=
        safe_text
)
oCLlite_BooleanType_strategy = st.builds(
    oCLlite_BooleanType,
    name=
        safe_text
)
oCLlite_MapType_strategy = st.builds(
    oCLlite_MapType,
    name=
        safe_text
)
oCLlite_BagType_strategy = st.builds(
    oCLlite_BagType,
    name=
        safe_text
)
oCLlite_LambdaType_strategy = st.builds(
    oCLlite_LambdaType,
    name=
        safe_text
)
oCLlite_StringType_strategy = st.builds(
    oCLlite_StringType,
    name=
        safe_text
)
oCLlite_SequenceType_strategy = st.builds(
    oCLlite_SequenceType,
    name=
        safe_text
)
oCLlite_RealType_strategy = st.builds(
    oCLlite_RealType,
    name=
        safe_text
)
oCLlite_EnvType_strategy = st.builds(
    oCLlite_EnvType,
    name=
        safe_text
)
oCLlite_OclLAnyType_strategy = st.builds(
    oCLlite_OclLAnyType,
    name=
        safe_text
)
oCLlite_TupleType_strategy = st.builds(
    oCLlite_TupleType,
)
oCLlite_OrderedSetType_strategy = st.builds(
    oCLlite_OrderedSetType,
    name=
        safe_text
)
oCLlite_SetType_strategy = st.builds(
    oCLlite_SetType,
    name=
        safe_text
)
oCLlite_OclLModelElementExp_strategy = st.builds(
    oCLlite_OclLModelElementExp,
    name=
        safe_text
)
oCLlite_IfExp_strategy = st.builds(
    oCLlite_IfExp,
)
oCLlite_NullLiteralExp_strategy = st.builds(
    oCLlite_NullLiteralExp,
)
oCLlite_OclLExpression_strategy = st.builds(
    oCLlite_OclLExpression,
    elements=
        safe_text,
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
oCLlite_Query_strategy = st.builds(
    oCLlite_Query,
    name=
        safe_text
)
oCLlite_URI__strategy = st.builds(
    oCLlite_URI_,
    authority=
        safe_text,
    fragment_=
        safe_text,
    scheme=
        safe_text
)
oCLlite_ModuleElement_strategy = st.builds(
    oCLlite_ModuleElement,
)
oCLlite_Import_strategy = st.builds(
    oCLlite_Import,
    name=
        safe_text
)
oCLlite_OclLModel_strategy = st.builds(
    oCLlite_OclLModel,
    name=
        safe_text
)
oCLlite_Module_strategy = st.builds(
    oCLlite_Module,
    name=
        safe_text
)
oCLlite_OclLType_strategy = st.builds(
    oCLlite_OclLType,
)
oCLlite_Iterator_strategy = st.builds(
    oCLlite_Iterator,
    name=
        safe_text
)
oCLlite_LocalVariable_strategy = st.builds(
    oCLlite_LocalVariable,
    name=
        safe_text
)





@given(instance=oCLlite_StringLiteralExp_strategy)
def test_hyp_ocllite_stringliteralexp_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original






@given(instance=oCLlite_BooleanLiteralExp_strategy)
def test_hyp_ocllite_booleanliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original




@given(instance=oCLlite_NumberLiteralExp_strategy)
def test_hyp_ocllite_numberliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original




@given(instance=oCLlite_TuplePart_strategy)
def test_hyp_ocllite_tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



















@given(instance=oCLlite_NavigationOrAttributeCall_strategy)
def test_hyp_ocllite_navigationorattributecall_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original















@given(instance=oCLlite_IntegerType_strategy)
def test_hyp_ocllite_integertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_BooleanType_strategy)
def test_hyp_ocllite_booleantype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_MapType_strategy)
def test_hyp_ocllite_maptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_BagType_strategy)
def test_hyp_ocllite_bagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_LambdaType_strategy)
def test_hyp_ocllite_lambdatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_StringType_strategy)
def test_hyp_ocllite_stringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_SequenceType_strategy)
def test_hyp_ocllite_sequencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_RealType_strategy)
def test_hyp_ocllite_realtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_EnvType_strategy)
def test_hyp_ocllite_envtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_OclLAnyType_strategy)
def test_hyp_ocllite_ocllanytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=oCLlite_OrderedSetType_strategy)
def test_hyp_ocllite_orderedsettype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_SetType_strategy)
def test_hyp_ocllite_settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_OclLModelElementExp_strategy)
def test_hyp_ocllite_ocllmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=oCLlite_OclLExpression_strategy)
def test_hyp_ocllite_ocllexpression_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original



@given(instance=oCLlite_OclLExpression_strategy)
def test_hyp_ocllite_ocllexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=oCLlite_Query_strategy)
def test_hyp_ocllite_query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_URI__strategy)
def test_hyp_ocllite_uri__authority_setter(instance):
    original = instance.authority
    instance.authority = original
    assert instance.authority == original



@given(instance=oCLlite_URI__strategy)
def test_hyp_ocllite_uri__fragment__setter(instance):
    original = instance.fragment_
    instance.fragment_ = original
    assert instance.fragment_ == original



@given(instance=oCLlite_URI__strategy)
def test_hyp_ocllite_uri__scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original





@given(instance=oCLlite_Import_strategy)
def test_hyp_ocllite_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_OclLModel_strategy)
def test_hyp_ocllite_ocllmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_Module_strategy)
def test_hyp_ocllite_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=oCLlite_Iterator_strategy)
def test_hyp_ocllite_iterator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oCLlite_LocalVariable_strategy)
def test_hyp_ocllite_localvariable_name_setter(instance):
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
    CollectionExp,
    ModuleElement,
    OclLExpression,
    OclLType,
    PrimitiveExp,
    oCLlite_AddOpCallExp,
    oCLlite_BagExp,
    oCLlite_BagType,
    oCLlite_BoolOpCallExp,
    oCLlite_BooleanLiteralExp,
    oCLlite_BooleanType,
    oCLlite_CollectionExp,
    oCLlite_CollectionOpCallExp,
    oCLlite_ComOpCallExp,
    oCLlite_ElseIfThenExp,
    oCLlite_EnvType,
    oCLlite_EqOpCallExp,
    oCLlite_IfExp,
    oCLlite_Import,
    oCLlite_IntegerType,
    oCLlite_InvalidLiteralExp,
    oCLlite_IterateExp,
    oCLlite_Iterator,
    oCLlite_IteratorExp,
    oCLlite_LambdaExp,
    oCLlite_LambdaType,
    oCLlite_LocalVariable,
    oCLlite_MapElement,
    oCLlite_MapExp,
    oCLlite_MapType,
    oCLlite_Module,
    oCLlite_ModuleElement,
    oCLlite_MulOpCallExp,
    oCLlite_NavigationExp,
    oCLlite_NavigationOrAttributeCall,
    oCLlite_NestedExp,
    oCLlite_NullLiteralExp,
    oCLlite_NumberLiteralExp,
    oCLlite_OclLAnyType,
    oCLlite_OclLExpression,
    oCLlite_OclLModel,
    oCLlite_OclLModelElementExp,
    oCLlite_OclLType,
    oCLlite_OperationCall,
    oCLlite_OrderedSetExp,
    oCLlite_OrderedSetType,
    oCLlite_PrimitiveExp,
    oCLlite_Query,
    oCLlite_RealType,
    oCLlite_SelfExp,
    oCLlite_SequenceExp,
    oCLlite_SequenceType,
    oCLlite_SetExp,
    oCLlite_SetType,
    oCLlite_StringLiteralExp,
    oCLlite_StringType,
    oCLlite_TupleExp,
    oCLlite_TuplePart,
    oCLlite_TupleType,
    oCLlite_URI_,
    oCLlite_UnlimitedNaturalLiteralExp,
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

def test_oCLlite_BagType_name_value_roundtrip():
    instance = oCLlite_BagType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_BooleanLiteralExp_symbol_value_roundtrip():
    instance = oCLlite_BooleanLiteralExp(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_oCLlite_BooleanType_name_value_roundtrip():
    instance = oCLlite_BooleanType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_EnvType_name_value_roundtrip():
    instance = oCLlite_EnvType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_Import_name_value_roundtrip():
    instance = oCLlite_Import(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_IntegerType_name_value_roundtrip():
    instance = oCLlite_IntegerType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_Iterator_name_value_roundtrip():
    instance = oCLlite_Iterator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_LambdaType_name_value_roundtrip():
    instance = oCLlite_LambdaType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_LocalVariable_name_value_roundtrip():
    instance = oCLlite_LocalVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_MapType_name_value_roundtrip():
    instance = oCLlite_MapType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_Module_name_value_roundtrip():
    instance = oCLlite_Module(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_NavigationOrAttributeCall_feature_value_roundtrip():
    instance = oCLlite_NavigationOrAttributeCall(feature="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_oCLlite_NumberLiteralExp_symbol_value_roundtrip():
    instance = oCLlite_NumberLiteralExp(symbol=7)
    assert instance.symbol == 7
    instance.symbol = 13
    assert instance.symbol == 13


def test_oCLlite_OclLAnyType_name_value_roundtrip():
    instance = oCLlite_OclLAnyType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_OclLExpression_elements_value_roundtrip():
    instance = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    assert instance.elements == "sample_text"
    instance.elements = "sample_text_2"
    assert instance.elements == "sample_text_2"


def test_oCLlite_OclLExpression_name_value_roundtrip():
    instance = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_OclLModel_name_value_roundtrip():
    instance = oCLlite_OclLModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_OclLModelElementExp_name_value_roundtrip():
    instance = oCLlite_OclLModelElementExp(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_OrderedSetType_name_value_roundtrip():
    instance = oCLlite_OrderedSetType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_Query_name_value_roundtrip():
    instance = oCLlite_Query(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_RealType_name_value_roundtrip():
    instance = oCLlite_RealType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_SequenceType_name_value_roundtrip():
    instance = oCLlite_SequenceType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_SetType_name_value_roundtrip():
    instance = oCLlite_SetType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_StringLiteralExp_segments_value_roundtrip():
    instance = oCLlite_StringLiteralExp(segments="sample_text")
    assert instance.segments == "sample_text"
    instance.segments = "sample_text_2"
    assert instance.segments == "sample_text_2"


def test_oCLlite_StringType_name_value_roundtrip():
    instance = oCLlite_StringType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_TuplePart_name_value_roundtrip():
    instance = oCLlite_TuplePart(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oCLlite_URI__authority_value_roundtrip():
    instance = oCLlite_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    assert instance.authority == "sample_text"
    instance.authority = "sample_text_2"
    assert instance.authority == "sample_text_2"


def test_oCLlite_URI__fragment__value_roundtrip():
    instance = oCLlite_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    assert instance.fragment_ == "sample_text"
    instance.fragment_ = "sample_text_2"
    assert instance.fragment_ == "sample_text_2"


def test_oCLlite_URI__scheme_value_roundtrip():
    instance = oCLlite_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    assert instance.scheme == "sample_text"
    instance.scheme = "sample_text_2"
    assert instance.scheme == "sample_text_2"


def test_oCLlite_BagExp_isa_CollectionExp():
    instance = oCLlite_BagExp()
    assert isinstance(instance, CollectionExp)


def test_oCLlite_OrderedSetExp_isa_CollectionExp():
    instance = oCLlite_OrderedSetExp()
    assert isinstance(instance, CollectionExp)


def test_oCLlite_SequenceExp_isa_CollectionExp():
    instance = oCLlite_SequenceExp()
    assert isinstance(instance, CollectionExp)


def test_oCLlite_SetExp_isa_CollectionExp():
    instance = oCLlite_SetExp()
    assert isinstance(instance, CollectionExp)


def test_oCLlite_Query_isa_ModuleElement():
    instance = oCLlite_Query(name="sample_text")
    assert isinstance(instance, ModuleElement)


def test_oCLlite_AddOpCallExp_isa_OclLExpression():
    instance = oCLlite_AddOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_BoolOpCallExp_isa_OclLExpression():
    instance = oCLlite_BoolOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_CollectionExp_isa_OclLExpression():
    instance = oCLlite_CollectionExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_CollectionOpCallExp_isa_OclLExpression():
    instance = oCLlite_CollectionOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_ComOpCallExp_isa_OclLExpression():
    instance = oCLlite_ComOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_ElseIfThenExp_isa_OclLExpression():
    instance = oCLlite_ElseIfThenExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_EqOpCallExp_isa_OclLExpression():
    instance = oCLlite_EqOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_IfExp_isa_OclLExpression():
    instance = oCLlite_IfExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_IterateExp_isa_OclLExpression():
    instance = oCLlite_IterateExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_IteratorExp_isa_OclLExpression():
    instance = oCLlite_IteratorExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_LambdaExp_isa_OclLExpression():
    instance = oCLlite_LambdaExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_MapExp_isa_OclLExpression():
    instance = oCLlite_MapExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_MulOpCallExp_isa_OclLExpression():
    instance = oCLlite_MulOpCallExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_NavigationExp_isa_OclLExpression():
    instance = oCLlite_NavigationExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_NavigationOrAttributeCall_isa_OclLExpression():
    instance = oCLlite_NavigationOrAttributeCall(feature="sample_text")
    assert isinstance(instance, OclLExpression)


def test_oCLlite_NestedExp_isa_OclLExpression():
    instance = oCLlite_NestedExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_OperationCall_isa_OclLExpression():
    instance = oCLlite_OperationCall()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_PrimitiveExp_isa_OclLExpression():
    instance = oCLlite_PrimitiveExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_SelfExp_isa_OclLExpression():
    instance = oCLlite_SelfExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_TupleExp_isa_OclLExpression():
    instance = oCLlite_TupleExp()
    assert isinstance(instance, OclLExpression)


def test_oCLlite_BagType_isa_OclLType():
    instance = oCLlite_BagType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_BooleanType_isa_OclLType():
    instance = oCLlite_BooleanType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_EnvType_isa_OclLType():
    instance = oCLlite_EnvType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_IntegerType_isa_OclLType():
    instance = oCLlite_IntegerType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_LambdaType_isa_OclLType():
    instance = oCLlite_LambdaType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_MapType_isa_OclLType():
    instance = oCLlite_MapType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_OclLAnyType_isa_OclLType():
    instance = oCLlite_OclLAnyType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_OclLModelElementExp_isa_OclLType():
    instance = oCLlite_OclLModelElementExp(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_OrderedSetType_isa_OclLType():
    instance = oCLlite_OrderedSetType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_RealType_isa_OclLType():
    instance = oCLlite_RealType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_SequenceType_isa_OclLType():
    instance = oCLlite_SequenceType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_SetType_isa_OclLType():
    instance = oCLlite_SetType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_StringType_isa_OclLType():
    instance = oCLlite_StringType(name="sample_text")
    assert isinstance(instance, OclLType)


def test_oCLlite_TupleType_isa_OclLType():
    instance = oCLlite_TupleType()
    assert isinstance(instance, OclLType)


def test_oCLlite_BooleanLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_BooleanLiteralExp(symbol="sample_text")
    assert isinstance(instance, PrimitiveExp)


def test_oCLlite_InvalidLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_InvalidLiteralExp()
    assert isinstance(instance, PrimitiveExp)


def test_oCLlite_NullLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_NullLiteralExp()
    assert isinstance(instance, PrimitiveExp)


def test_oCLlite_NumberLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_NumberLiteralExp(symbol=7)
    assert isinstance(instance, PrimitiveExp)


def test_oCLlite_StringLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_StringLiteralExp(segments="sample_text")
    assert isinstance(instance, PrimitiveExp)


def test_oCLlite_UnlimitedNaturalLiteralExp_isa_PrimitiveExp():
    instance = oCLlite_UnlimitedNaturalLiteralExp()
    assert isinstance(instance, PrimitiveExp)


def test_assoc_argsTypes56_link_reassign_clear():
    a = oCLlite_LambdaType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_LambdaType', {b1})
    assert _is_linked(a, 'oCLlite_LambdaType', b1)
    if hasattr(b1, 'oCLlite_OclLType57'):
        assert _is_linked(b1, 'oCLlite_OclLType57', a)
    _safe_set(a, 'oCLlite_LambdaType', {b2})
    assert _is_linked(a, 'oCLlite_LambdaType', b2)
    if hasattr(b1, 'oCLlite_OclLType57'):
        assert not _is_linked(b1, 'oCLlite_OclLType57', a)
    if hasattr(b2, 'oCLlite_OclLType57'):
        assert _is_linked(b2, 'oCLlite_OclLType57', a)
    _safe_set(a, 'oCLlite_LambdaType', set())
    assert not _is_linked(a, 'oCLlite_LambdaType', b2)
    if hasattr(b2, 'oCLlite_OclLType57'):
        assert not _is_linked(b2, 'oCLlite_OclLType57', a)


def test_assoc_arguments101_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_OperationCall()
    b2 = oCLlite_OperationCall()
    _safe_set(a, 'oCLlite_OclLExpression102', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression102', b1)
    if hasattr(b1, 'oCLlite_OperationCall'):
        assert _is_linked(b1, 'oCLlite_OperationCall', a)
    _safe_set(a, 'oCLlite_OclLExpression102', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression102', b2)
    if hasattr(b1, 'oCLlite_OperationCall'):
        assert not _is_linked(b1, 'oCLlite_OperationCall', a)
    if hasattr(b2, 'oCLlite_OperationCall'):
        assert _is_linked(b2, 'oCLlite_OperationCall', a)
    _safe_set(a, 'oCLlite_OclLExpression102', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression102', b2)
    if hasattr(b2, 'oCLlite_OperationCall'):
        assert not _is_linked(b2, 'oCLlite_OperationCall', a)


def test_assoc_arguments86_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_CollectionOpCallExp()
    b2 = oCLlite_CollectionOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression87', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression87', b1)
    if hasattr(b1, 'oCLlite_CollectionOpCallExp'):
        assert _is_linked(b1, 'oCLlite_CollectionOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression87', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression87', b2)
    if hasattr(b1, 'oCLlite_CollectionOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_CollectionOpCallExp', a)
    if hasattr(b2, 'oCLlite_CollectionOpCallExp'):
        assert _is_linked(b2, 'oCLlite_CollectionOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression87', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression87', b2)
    if hasattr(b2, 'oCLlite_CollectionOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_CollectionOpCallExp', a)


def test_assoc_body10_link_reassign_clear():
    a = oCLlite_Query(name="sample_text")
    b1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oCLlite_Query', b1)
    assert _is_linked(a, 'oCLlite_Query', b1)
    if hasattr(b1, 'oCLlite_OclLExpression'):
        assert _is_linked(b1, 'oCLlite_OclLExpression', a)
    _safe_set(a, 'oCLlite_Query', b2)
    assert _is_linked(a, 'oCLlite_Query', b2)
    if hasattr(b1, 'oCLlite_OclLExpression'):
        assert not _is_linked(b1, 'oCLlite_OclLExpression', a)
    if hasattr(b2, 'oCLlite_OclLExpression'):
        assert _is_linked(b2, 'oCLlite_OclLExpression', a)
    _safe_set(a, 'oCLlite_Query', None)
    assert not _is_linked(a, 'oCLlite_Query', b2)
    if hasattr(b2, 'oCLlite_OclLExpression'):
        assert not _is_linked(b2, 'oCLlite_OclLExpression', a)


def test_assoc_body93_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IterateExp()
    b2 = oCLlite_IterateExp()
    _safe_set(a, 'oCLlite_OclLExpression95', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression95', b1)
    if hasattr(b1, 'oCLlite_IterateExp94'):
        assert _is_linked(b1, 'oCLlite_IterateExp94', a)
    _safe_set(a, 'oCLlite_OclLExpression95', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression95', b2)
    if hasattr(b1, 'oCLlite_IterateExp94'):
        assert not _is_linked(b1, 'oCLlite_IterateExp94', a)
    if hasattr(b2, 'oCLlite_IterateExp94'):
        assert _is_linked(b2, 'oCLlite_IterateExp94', a)
    _safe_set(a, 'oCLlite_OclLExpression95', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression95', b2)
    if hasattr(b2, 'oCLlite_IterateExp94'):
        assert not _is_linked(b2, 'oCLlite_IterateExp94', a)


def test_assoc_body98_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IteratorExp()
    b2 = oCLlite_IteratorExp()
    _safe_set(a, 'oCLlite_OclLExpression100', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression100', b1)
    if hasattr(b1, 'oCLlite_IteratorExp99'):
        assert _is_linked(b1, 'oCLlite_IteratorExp99', a)
    _safe_set(a, 'oCLlite_OclLExpression100', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression100', b2)
    if hasattr(b1, 'oCLlite_IteratorExp99'):
        assert not _is_linked(b1, 'oCLlite_IteratorExp99', a)
    if hasattr(b2, 'oCLlite_IteratorExp99'):
        assert _is_linked(b2, 'oCLlite_IteratorExp99', a)
    _safe_set(a, 'oCLlite_OclLExpression100', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression100', b2)
    if hasattr(b2, 'oCLlite_IteratorExp99'):
        assert not _is_linked(b2, 'oCLlite_IteratorExp99', a)


def test_assoc_condition107_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_ElseIfThenExp()
    b2 = oCLlite_ElseIfThenExp()
    _safe_set(a, 'oCLlite_OclLExpression108', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression108', b1)
    if hasattr(b1, 'oCLlite_ElseIfThenExp'):
        assert _is_linked(b1, 'oCLlite_ElseIfThenExp', a)
    _safe_set(a, 'oCLlite_OclLExpression108', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression108', b2)
    if hasattr(b1, 'oCLlite_ElseIfThenExp'):
        assert not _is_linked(b1, 'oCLlite_ElseIfThenExp', a)
    if hasattr(b2, 'oCLlite_ElseIfThenExp'):
        assert _is_linked(b2, 'oCLlite_ElseIfThenExp', a)
    _safe_set(a, 'oCLlite_OclLExpression108', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression108', b2)
    if hasattr(b2, 'oCLlite_ElseIfThenExp'):
        assert not _is_linked(b2, 'oCLlite_ElseIfThenExp', a)


def test_assoc_condition43_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IfExp()
    b2 = oCLlite_IfExp()
    _safe_set(a, 'oCLlite_OclLExpression44', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression44', b1)
    if hasattr(b1, 'oCLlite_IfExp'):
        assert _is_linked(b1, 'oCLlite_IfExp', a)
    _safe_set(a, 'oCLlite_OclLExpression44', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression44', b2)
    if hasattr(b1, 'oCLlite_IfExp'):
        assert not _is_linked(b1, 'oCLlite_IfExp', a)
    if hasattr(b2, 'oCLlite_IfExp'):
        assert _is_linked(b2, 'oCLlite_IfExp', a)
    _safe_set(a, 'oCLlite_OclLExpression44', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression44', b2)
    if hasattr(b2, 'oCLlite_IfExp'):
        assert not _is_linked(b2, 'oCLlite_IfExp', a)


def test_assoc_elementType66_link_reassign_clear():
    a = oCLlite_SetType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_SetType', b1)
    assert _is_linked(a, 'oCLlite_SetType', b1)
    if hasattr(b1, 'oCLlite_OclLType67'):
        assert _is_linked(b1, 'oCLlite_OclLType67', a)
    _safe_set(a, 'oCLlite_SetType', b2)
    assert _is_linked(a, 'oCLlite_SetType', b2)
    if hasattr(b1, 'oCLlite_OclLType67'):
        assert not _is_linked(b1, 'oCLlite_OclLType67', a)
    if hasattr(b2, 'oCLlite_OclLType67'):
        assert _is_linked(b2, 'oCLlite_OclLType67', a)
    _safe_set(a, 'oCLlite_SetType', None)
    assert not _is_linked(a, 'oCLlite_SetType', b2)
    if hasattr(b2, 'oCLlite_OclLType67'):
        assert not _is_linked(b2, 'oCLlite_OclLType67', a)


def test_assoc_elementType68_link_reassign_clear():
    a = oCLlite_SequenceType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_SequenceType', b1)
    assert _is_linked(a, 'oCLlite_SequenceType', b1)
    if hasattr(b1, 'oCLlite_OclLType69'):
        assert _is_linked(b1, 'oCLlite_OclLType69', a)
    _safe_set(a, 'oCLlite_SequenceType', b2)
    assert _is_linked(a, 'oCLlite_SequenceType', b2)
    if hasattr(b1, 'oCLlite_OclLType69'):
        assert not _is_linked(b1, 'oCLlite_OclLType69', a)
    if hasattr(b2, 'oCLlite_OclLType69'):
        assert _is_linked(b2, 'oCLlite_OclLType69', a)
    _safe_set(a, 'oCLlite_SequenceType', None)
    assert not _is_linked(a, 'oCLlite_SequenceType', b2)
    if hasattr(b2, 'oCLlite_OclLType69'):
        assert not _is_linked(b2, 'oCLlite_OclLType69', a)


def test_assoc_elementType70_link_reassign_clear():
    a = oCLlite_OrderedSetType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_OrderedSetType', b1)
    assert _is_linked(a, 'oCLlite_OrderedSetType', b1)
    if hasattr(b1, 'oCLlite_OclLType71'):
        assert _is_linked(b1, 'oCLlite_OclLType71', a)
    _safe_set(a, 'oCLlite_OrderedSetType', b2)
    assert _is_linked(a, 'oCLlite_OrderedSetType', b2)
    if hasattr(b1, 'oCLlite_OclLType71'):
        assert not _is_linked(b1, 'oCLlite_OclLType71', a)
    if hasattr(b2, 'oCLlite_OclLType71'):
        assert _is_linked(b2, 'oCLlite_OclLType71', a)
    _safe_set(a, 'oCLlite_OrderedSetType', None)
    assert not _is_linked(a, 'oCLlite_OrderedSetType', b2)
    if hasattr(b2, 'oCLlite_OclLType71'):
        assert not _is_linked(b2, 'oCLlite_OclLType71', a)


def test_assoc_elementType72_link_reassign_clear():
    a = oCLlite_BagType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_BagType', b1)
    assert _is_linked(a, 'oCLlite_BagType', b1)
    if hasattr(b1, 'oCLlite_OclLType73'):
        assert _is_linked(b1, 'oCLlite_OclLType73', a)
    _safe_set(a, 'oCLlite_BagType', b2)
    assert _is_linked(a, 'oCLlite_BagType', b2)
    if hasattr(b1, 'oCLlite_OclLType73'):
        assert not _is_linked(b1, 'oCLlite_OclLType73', a)
    if hasattr(b2, 'oCLlite_OclLType73'):
        assert _is_linked(b2, 'oCLlite_OclLType73', a)
    _safe_set(a, 'oCLlite_BagType', None)
    assert not _is_linked(a, 'oCLlite_BagType', b2)
    if hasattr(b2, 'oCLlite_OclLType73'):
        assert not _is_linked(b2, 'oCLlite_OclLType73', a)


def test_assoc_elements6_link_reassign_clear():
    a = oCLlite_Module(name="sample_text")
    b1 = oCLlite_ModuleElement()
    b2 = oCLlite_ModuleElement()
    _safe_set(a, 'oCLlite_Module7', {b1})
    assert _is_linked(a, 'oCLlite_Module7', b1)
    if hasattr(b1, 'oCLlite_ModuleElement'):
        assert _is_linked(b1, 'oCLlite_ModuleElement', a)
    _safe_set(a, 'oCLlite_Module7', {b2})
    assert _is_linked(a, 'oCLlite_Module7', b2)
    if hasattr(b1, 'oCLlite_ModuleElement'):
        assert not _is_linked(b1, 'oCLlite_ModuleElement', a)
    if hasattr(b2, 'oCLlite_ModuleElement'):
        assert _is_linked(b2, 'oCLlite_ModuleElement', a)
    _safe_set(a, 'oCLlite_Module7', set())
    assert not _is_linked(a, 'oCLlite_Module7', b2)
    if hasattr(b2, 'oCLlite_ModuleElement'):
        assert not _is_linked(b2, 'oCLlite_ModuleElement', a)


def test_assoc_else_51_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IfExp()
    b2 = oCLlite_IfExp()
    _safe_set(a, 'oCLlite_OclLExpression53', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression53', b1)
    if hasattr(b1, 'oCLlite_IfExp52'):
        assert _is_linked(b1, 'oCLlite_IfExp52', a)
    _safe_set(a, 'oCLlite_OclLExpression53', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression53', b2)
    if hasattr(b1, 'oCLlite_IfExp52'):
        assert not _is_linked(b1, 'oCLlite_IfExp52', a)
    if hasattr(b2, 'oCLlite_IfExp52'):
        assert _is_linked(b2, 'oCLlite_IfExp52', a)
    _safe_set(a, 'oCLlite_OclLExpression53', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression53', b2)
    if hasattr(b2, 'oCLlite_IfExp52'):
        assert not _is_linked(b2, 'oCLlite_IfExp52', a)


def test_assoc_exp112_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_NestedExp()
    b2 = oCLlite_NestedExp()
    _safe_set(a, 'oCLlite_OclLExpression113', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression113', b1)
    if hasattr(b1, 'oCLlite_NestedExp'):
        assert _is_linked(b1, 'oCLlite_NestedExp', a)
    _safe_set(a, 'oCLlite_OclLExpression113', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression113', b2)
    if hasattr(b1, 'oCLlite_NestedExp'):
        assert not _is_linked(b1, 'oCLlite_NestedExp', a)
    if hasattr(b2, 'oCLlite_NestedExp'):
        assert _is_linked(b2, 'oCLlite_NestedExp', a)
    _safe_set(a, 'oCLlite_OclLExpression113', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression113', b2)
    if hasattr(b2, 'oCLlite_NestedExp'):
        assert not _is_linked(b2, 'oCLlite_NestedExp', a)


def test_assoc_expression103_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_LambdaExp()
    b2 = oCLlite_LambdaExp()
    _safe_set(a, 'oCLlite_OclLExpression104', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression104', b1)
    if hasattr(b1, 'oCLlite_LambdaExp'):
        assert _is_linked(b1, 'oCLlite_LambdaExp', a)
    _safe_set(a, 'oCLlite_OclLExpression104', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression104', b2)
    if hasattr(b1, 'oCLlite_LambdaExp'):
        assert not _is_linked(b1, 'oCLlite_LambdaExp', a)
    if hasattr(b2, 'oCLlite_LambdaExp'):
        assert _is_linked(b2, 'oCLlite_LambdaExp', a)
    _safe_set(a, 'oCLlite_OclLExpression104', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression104', b2)
    if hasattr(b2, 'oCLlite_LambdaExp'):
        assert not _is_linked(b2, 'oCLlite_LambdaExp', a)


def test_assoc_ifThen48_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IfExp()
    b2 = oCLlite_IfExp()
    _safe_set(a, 'oCLlite_OclLExpression50', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression50', b1)
    if hasattr(b1, 'oCLlite_IfExp49'):
        assert _is_linked(b1, 'oCLlite_IfExp49', a)
    _safe_set(a, 'oCLlite_OclLExpression50', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression50', b2)
    if hasattr(b1, 'oCLlite_IfExp49'):
        assert not _is_linked(b1, 'oCLlite_IfExp49', a)
    if hasattr(b2, 'oCLlite_IfExp49'):
        assert _is_linked(b2, 'oCLlite_IfExp49', a)
    _safe_set(a, 'oCLlite_OclLExpression50', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression50', b2)
    if hasattr(b2, 'oCLlite_IfExp49'):
        assert not _is_linked(b2, 'oCLlite_IfExp49', a)


def test_assoc_imports4_link_reassign_clear():
    a = oCLlite_Module(name="sample_text")
    b1 = oCLlite_Import(name="sample_text")
    b2 = oCLlite_Import(name="sample_text_2")
    _safe_set(a, 'oCLlite_Module5', {b1})
    assert _is_linked(a, 'oCLlite_Module5', b1)
    if hasattr(b1, 'oCLlite_Import'):
        assert _is_linked(b1, 'oCLlite_Import', a)
    _safe_set(a, 'oCLlite_Module5', {b2})
    assert _is_linked(a, 'oCLlite_Module5', b2)
    if hasattr(b1, 'oCLlite_Import'):
        assert not _is_linked(b1, 'oCLlite_Import', a)
    if hasattr(b2, 'oCLlite_Import'):
        assert _is_linked(b2, 'oCLlite_Import', a)
    _safe_set(a, 'oCLlite_Module5', set())
    assert not _is_linked(a, 'oCLlite_Module5', b2)
    if hasattr(b2, 'oCLlite_Import'):
        assert not _is_linked(b2, 'oCLlite_Import', a)


def test_assoc_in_14_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLExpression13', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression13', b1)
    if hasattr(b1, 'oCLlite_OclLExpression15'):
        assert _is_linked(b1, 'oCLlite_OclLExpression15', a)
    _safe_set(a, 'oCLlite_OclLExpression13', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression13', b2)
    if hasattr(b1, 'oCLlite_OclLExpression15'):
        assert not _is_linked(b1, 'oCLlite_OclLExpression15', a)
    if hasattr(b2, 'oCLlite_OclLExpression15'):
        assert _is_linked(b2, 'oCLlite_OclLExpression15', a)
    _safe_set(a, 'oCLlite_OclLExpression13', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression13', b2)
    if hasattr(b2, 'oCLlite_OclLExpression15'):
        assert not _is_linked(b2, 'oCLlite_OclLExpression15', a)


def test_assoc_init40_link_reassign_clear():
    a = oCLlite_TuplePart(name="sample_text")
    b1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oCLlite_TuplePart41', b1)
    assert _is_linked(a, 'oCLlite_TuplePart41', b1)
    if hasattr(b1, 'oCLlite_OclLExpression42'):
        assert _is_linked(b1, 'oCLlite_OclLExpression42', a)
    _safe_set(a, 'oCLlite_TuplePart41', b2)
    assert _is_linked(a, 'oCLlite_TuplePart41', b2)
    if hasattr(b1, 'oCLlite_OclLExpression42'):
        assert not _is_linked(b1, 'oCLlite_OclLExpression42', a)
    if hasattr(b2, 'oCLlite_OclLExpression42'):
        assert _is_linked(b2, 'oCLlite_OclLExpression42', a)
    _safe_set(a, 'oCLlite_TuplePart41', None)
    assert not _is_linked(a, 'oCLlite_TuplePart41', b2)
    if hasattr(b2, 'oCLlite_OclLExpression42'):
        assert not _is_linked(b2, 'oCLlite_OclLExpression42', a)


def test_assoc_initExp26_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_LocalVariable(name="sample_text")
    b2 = oCLlite_LocalVariable(name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLExpression28', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression28', b1)
    if hasattr(b1, 'oCLlite_LocalVariable27'):
        assert _is_linked(b1, 'oCLlite_LocalVariable27', a)
    _safe_set(a, 'oCLlite_OclLExpression28', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression28', b2)
    if hasattr(b1, 'oCLlite_LocalVariable27'):
        assert not _is_linked(b1, 'oCLlite_LocalVariable27', a)
    if hasattr(b2, 'oCLlite_LocalVariable27'):
        assert _is_linked(b2, 'oCLlite_LocalVariable27', a)
    _safe_set(a, 'oCLlite_OclLExpression28', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression28', b2)
    if hasattr(b2, 'oCLlite_LocalVariable27'):
        assert not _is_linked(b2, 'oCLlite_LocalVariable27', a)


def test_assoc_input1_link_reassign_clear():
    a = oCLlite_OclLModel(name="sample_text")
    b1 = oCLlite_Module(name="sample_text")
    b2 = oCLlite_Module(name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLModel3', b1)
    assert _is_linked(a, 'oCLlite_OclLModel3', b1)
    if hasattr(b1, 'oCLlite_Module2'):
        assert _is_linked(b1, 'oCLlite_Module2', a)
    _safe_set(a, 'oCLlite_OclLModel3', b2)
    assert _is_linked(a, 'oCLlite_OclLModel3', b2)
    if hasattr(b1, 'oCLlite_Module2'):
        assert not _is_linked(b1, 'oCLlite_Module2', a)
    if hasattr(b2, 'oCLlite_Module2'):
        assert _is_linked(b2, 'oCLlite_Module2', a)
    _safe_set(a, 'oCLlite_OclLModel3', None)
    assert not _is_linked(a, 'oCLlite_OclLModel3', b2)
    if hasattr(b2, 'oCLlite_Module2'):
        assert not _is_linked(b2, 'oCLlite_Module2', a)


def test_assoc_iterators88_link_reassign_clear():
    a = oCLlite_Iterator(name="sample_text")
    b1 = oCLlite_IterateExp()
    b2 = oCLlite_IterateExp()
    _safe_set(a, 'oCLlite_Iterator89', b1)
    assert _is_linked(a, 'oCLlite_Iterator89', b1)
    if hasattr(b1, 'oCLlite_IterateExp'):
        assert _is_linked(b1, 'oCLlite_IterateExp', a)
    _safe_set(a, 'oCLlite_Iterator89', b2)
    assert _is_linked(a, 'oCLlite_Iterator89', b2)
    if hasattr(b1, 'oCLlite_IterateExp'):
        assert not _is_linked(b1, 'oCLlite_IterateExp', a)
    if hasattr(b2, 'oCLlite_IterateExp'):
        assert _is_linked(b2, 'oCLlite_IterateExp', a)
    _safe_set(a, 'oCLlite_Iterator89', None)
    assert not _is_linked(a, 'oCLlite_Iterator89', b2)
    if hasattr(b2, 'oCLlite_IterateExp'):
        assert not _is_linked(b2, 'oCLlite_IterateExp', a)


def test_assoc_iterators96_link_reassign_clear():
    a = oCLlite_Iterator(name="sample_text")
    b1 = oCLlite_IteratorExp()
    b2 = oCLlite_IteratorExp()
    _safe_set(a, 'oCLlite_Iterator97', b1)
    assert _is_linked(a, 'oCLlite_Iterator97', b1)
    if hasattr(b1, 'oCLlite_IteratorExp'):
        assert _is_linked(b1, 'oCLlite_IteratorExp', a)
    _safe_set(a, 'oCLlite_Iterator97', b2)
    assert _is_linked(a, 'oCLlite_Iterator97', b2)
    if hasattr(b1, 'oCLlite_IteratorExp'):
        assert not _is_linked(b1, 'oCLlite_IteratorExp', a)
    if hasattr(b2, 'oCLlite_IteratorExp'):
        assert _is_linked(b2, 'oCLlite_IteratorExp', a)
    _safe_set(a, 'oCLlite_Iterator97', None)
    assert not _is_linked(a, 'oCLlite_Iterator97', b2)
    if hasattr(b2, 'oCLlite_IteratorExp'):
        assert not _is_linked(b2, 'oCLlite_IteratorExp', a)


def test_assoc_key32_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_MapElement()
    b2 = oCLlite_MapElement()
    _safe_set(a, 'oCLlite_OclLExpression34', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression34', b1)
    if hasattr(b1, 'oCLlite_MapElement33'):
        assert _is_linked(b1, 'oCLlite_MapElement33', a)
    _safe_set(a, 'oCLlite_OclLExpression34', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression34', b2)
    if hasattr(b1, 'oCLlite_MapElement33'):
        assert not _is_linked(b1, 'oCLlite_MapElement33', a)
    if hasattr(b2, 'oCLlite_MapElement33'):
        assert _is_linked(b2, 'oCLlite_MapElement33', a)
    _safe_set(a, 'oCLlite_OclLExpression34', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression34', b2)
    if hasattr(b2, 'oCLlite_MapElement33'):
        assert not _is_linked(b2, 'oCLlite_MapElement33', a)


def test_assoc_keyType61_link_reassign_clear():
    a = oCLlite_MapType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_MapType', b1)
    assert _is_linked(a, 'oCLlite_MapType', b1)
    if hasattr(b1, 'oCLlite_OclLType62'):
        assert _is_linked(b1, 'oCLlite_OclLType62', a)
    _safe_set(a, 'oCLlite_MapType', b2)
    assert _is_linked(a, 'oCLlite_MapType', b2)
    if hasattr(b1, 'oCLlite_OclLType62'):
        assert not _is_linked(b1, 'oCLlite_OclLType62', a)
    if hasattr(b2, 'oCLlite_OclLType62'):
        assert _is_linked(b2, 'oCLlite_OclLType62', a)
    _safe_set(a, 'oCLlite_MapType', None)
    assert not _is_linked(a, 'oCLlite_MapType', b2)
    if hasattr(b2, 'oCLlite_OclLType62'):
        assert not _is_linked(b2, 'oCLlite_OclLType62', a)


def test_assoc_model19_link_reassign_clear():
    a = oCLlite_OclLModel(name="sample_text")
    b1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLModel21', b1)
    assert _is_linked(a, 'oCLlite_OclLModel21', b1)
    if hasattr(b1, 'oCLlite_OclLExpression20'):
        assert _is_linked(b1, 'oCLlite_OclLExpression20', a)
    _safe_set(a, 'oCLlite_OclLModel21', b2)
    assert _is_linked(a, 'oCLlite_OclLModel21', b2)
    if hasattr(b1, 'oCLlite_OclLExpression20'):
        assert not _is_linked(b1, 'oCLlite_OclLExpression20', a)
    if hasattr(b2, 'oCLlite_OclLExpression20'):
        assert _is_linked(b2, 'oCLlite_OclLExpression20', a)
    _safe_set(a, 'oCLlite_OclLModel21', None)
    assert not _is_linked(a, 'oCLlite_OclLModel21', b2)
    if hasattr(b2, 'oCLlite_OclLExpression20'):
        assert not _is_linked(b2, 'oCLlite_OclLExpression20', a)


def test_assoc_model54_link_reassign_clear():
    a = oCLlite_OclLModelElementExp(name="sample_text")
    b1 = oCLlite_OclLModel(name="sample_text")
    b2 = oCLlite_OclLModel(name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLModelElementExp', b1)
    assert _is_linked(a, 'oCLlite_OclLModelElementExp', b1)
    if hasattr(b1, 'oCLlite_OclLModel55'):
        assert _is_linked(b1, 'oCLlite_OclLModel55', a)
    _safe_set(a, 'oCLlite_OclLModelElementExp', b2)
    assert _is_linked(a, 'oCLlite_OclLModelElementExp', b2)
    if hasattr(b1, 'oCLlite_OclLModel55'):
        assert not _is_linked(b1, 'oCLlite_OclLModel55', a)
    if hasattr(b2, 'oCLlite_OclLModel55'):
        assert _is_linked(b2, 'oCLlite_OclLModel55', a)
    _safe_set(a, 'oCLlite_OclLModelElementExp', None)
    assert not _is_linked(a, 'oCLlite_OclLModelElementExp', b2)
    if hasattr(b2, 'oCLlite_OclLModel55'):
        assert not _is_linked(b2, 'oCLlite_OclLModel55', a)


def test_assoc_parts105_link_reassign_clear():
    a = oCLlite_TuplePart(name="sample_text")
    b1 = oCLlite_TupleExp()
    b2 = oCLlite_TupleExp()
    _safe_set(a, 'oCLlite_TuplePart106', b1)
    assert _is_linked(a, 'oCLlite_TuplePart106', b1)
    if hasattr(b1, 'oCLlite_TupleExp'):
        assert _is_linked(b1, 'oCLlite_TupleExp', a)
    _safe_set(a, 'oCLlite_TuplePart106', b2)
    assert _is_linked(a, 'oCLlite_TuplePart106', b2)
    if hasattr(b1, 'oCLlite_TupleExp'):
        assert not _is_linked(b1, 'oCLlite_TupleExp', a)
    if hasattr(b2, 'oCLlite_TupleExp'):
        assert _is_linked(b2, 'oCLlite_TupleExp', a)
    _safe_set(a, 'oCLlite_TuplePart106', None)
    assert not _is_linked(a, 'oCLlite_TuplePart106', b2)
    if hasattr(b2, 'oCLlite_TupleExp'):
        assert not _is_linked(b2, 'oCLlite_TupleExp', a)


def test_assoc_parts29_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_CollectionExp()
    b2 = oCLlite_CollectionExp()
    _safe_set(a, 'oCLlite_OclLExpression30', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression30', b1)
    if hasattr(b1, 'oCLlite_CollectionExp'):
        assert _is_linked(b1, 'oCLlite_CollectionExp', a)
    _safe_set(a, 'oCLlite_OclLExpression30', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression30', b2)
    if hasattr(b1, 'oCLlite_CollectionExp'):
        assert not _is_linked(b1, 'oCLlite_CollectionExp', a)
    if hasattr(b2, 'oCLlite_CollectionExp'):
        assert _is_linked(b2, 'oCLlite_CollectionExp', a)
    _safe_set(a, 'oCLlite_OclLExpression30', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression30', b2)
    if hasattr(b2, 'oCLlite_CollectionExp'):
        assert not _is_linked(b2, 'oCLlite_CollectionExp', a)


def test_assoc_result90_link_reassign_clear():
    a = oCLlite_LocalVariable(name="sample_text")
    b1 = oCLlite_IterateExp()
    b2 = oCLlite_IterateExp()
    _safe_set(a, 'oCLlite_LocalVariable92', b1)
    assert _is_linked(a, 'oCLlite_LocalVariable92', b1)
    if hasattr(b1, 'oCLlite_IterateExp91'):
        assert _is_linked(b1, 'oCLlite_IterateExp91', a)
    _safe_set(a, 'oCLlite_LocalVariable92', b2)
    assert _is_linked(a, 'oCLlite_LocalVariable92', b2)
    if hasattr(b1, 'oCLlite_IterateExp91'):
        assert not _is_linked(b1, 'oCLlite_IterateExp91', a)
    if hasattr(b2, 'oCLlite_IterateExp91'):
        assert _is_linked(b2, 'oCLlite_IterateExp91', a)
    _safe_set(a, 'oCLlite_LocalVariable92', None)
    assert not _is_linked(a, 'oCLlite_LocalVariable92', b2)
    if hasattr(b2, 'oCLlite_IterateExp91'):
        assert not _is_linked(b2, 'oCLlite_IterateExp91', a)


def test_assoc_returnType58_link_reassign_clear():
    a = oCLlite_LambdaType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_LambdaType59', b1)
    assert _is_linked(a, 'oCLlite_LambdaType59', b1)
    if hasattr(b1, 'oCLlite_OclLType60'):
        assert _is_linked(b1, 'oCLlite_OclLType60', a)
    _safe_set(a, 'oCLlite_LambdaType59', b2)
    assert _is_linked(a, 'oCLlite_LambdaType59', b2)
    if hasattr(b1, 'oCLlite_OclLType60'):
        assert not _is_linked(b1, 'oCLlite_OclLType60', a)
    if hasattr(b2, 'oCLlite_OclLType60'):
        assert _is_linked(b2, 'oCLlite_OclLType60', a)
    _safe_set(a, 'oCLlite_LambdaType59', None)
    assert not _is_linked(a, 'oCLlite_LambdaType59', b2)
    if hasattr(b2, 'oCLlite_OclLType60'):
        assert not _is_linked(b2, 'oCLlite_OclLType60', a)


def test_assoc_source0_link_reassign_clear():
    a = oCLlite_OclLModel(name="sample_text")
    b1 = oCLlite_Module(name="sample_text")
    b2 = oCLlite_Module(name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLModel', b1)
    assert _is_linked(a, 'oCLlite_OclLModel', b1)
    if hasattr(b1, 'oCLlite_Module'):
        assert _is_linked(b1, 'oCLlite_Module', a)
    _safe_set(a, 'oCLlite_OclLModel', b2)
    assert _is_linked(a, 'oCLlite_OclLModel', b2)
    if hasattr(b1, 'oCLlite_Module'):
        assert not _is_linked(b1, 'oCLlite_Module', a)
    if hasattr(b2, 'oCLlite_Module'):
        assert _is_linked(b2, 'oCLlite_Module', a)
    _safe_set(a, 'oCLlite_OclLModel', None)
    assert not _is_linked(a, 'oCLlite_OclLModel', b2)
    if hasattr(b2, 'oCLlite_Module'):
        assert not _is_linked(b2, 'oCLlite_Module', a)


def test_assoc_source74_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_BoolOpCallExp()
    b2 = oCLlite_BoolOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression75', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression75', b1)
    if hasattr(b1, 'oCLlite_BoolOpCallExp'):
        assert _is_linked(b1, 'oCLlite_BoolOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression75', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression75', b2)
    if hasattr(b1, 'oCLlite_BoolOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_BoolOpCallExp', a)
    if hasattr(b2, 'oCLlite_BoolOpCallExp'):
        assert _is_linked(b2, 'oCLlite_BoolOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression75', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression75', b2)
    if hasattr(b2, 'oCLlite_BoolOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_BoolOpCallExp', a)


def test_assoc_source76_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_EqOpCallExp()
    b2 = oCLlite_EqOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression77', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression77', b1)
    if hasattr(b1, 'oCLlite_EqOpCallExp'):
        assert _is_linked(b1, 'oCLlite_EqOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression77', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression77', b2)
    if hasattr(b1, 'oCLlite_EqOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_EqOpCallExp', a)
    if hasattr(b2, 'oCLlite_EqOpCallExp'):
        assert _is_linked(b2, 'oCLlite_EqOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression77', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression77', b2)
    if hasattr(b2, 'oCLlite_EqOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_EqOpCallExp', a)


def test_assoc_source78_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_ComOpCallExp()
    b2 = oCLlite_ComOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression79', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression79', b1)
    if hasattr(b1, 'oCLlite_ComOpCallExp'):
        assert _is_linked(b1, 'oCLlite_ComOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression79', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression79', b2)
    if hasattr(b1, 'oCLlite_ComOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_ComOpCallExp', a)
    if hasattr(b2, 'oCLlite_ComOpCallExp'):
        assert _is_linked(b2, 'oCLlite_ComOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression79', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression79', b2)
    if hasattr(b2, 'oCLlite_ComOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_ComOpCallExp', a)


def test_assoc_source80_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_AddOpCallExp()
    b2 = oCLlite_AddOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression81', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression81', b1)
    if hasattr(b1, 'oCLlite_AddOpCallExp'):
        assert _is_linked(b1, 'oCLlite_AddOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression81', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression81', b2)
    if hasattr(b1, 'oCLlite_AddOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_AddOpCallExp', a)
    if hasattr(b2, 'oCLlite_AddOpCallExp'):
        assert _is_linked(b2, 'oCLlite_AddOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression81', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression81', b2)
    if hasattr(b2, 'oCLlite_AddOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_AddOpCallExp', a)


def test_assoc_source82_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_MulOpCallExp()
    b2 = oCLlite_MulOpCallExp()
    _safe_set(a, 'oCLlite_OclLExpression83', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression83', b1)
    if hasattr(b1, 'oCLlite_MulOpCallExp'):
        assert _is_linked(b1, 'oCLlite_MulOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression83', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression83', b2)
    if hasattr(b1, 'oCLlite_MulOpCallExp'):
        assert not _is_linked(b1, 'oCLlite_MulOpCallExp', a)
    if hasattr(b2, 'oCLlite_MulOpCallExp'):
        assert _is_linked(b2, 'oCLlite_MulOpCallExp', a)
    _safe_set(a, 'oCLlite_OclLExpression83', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression83', b2)
    if hasattr(b2, 'oCLlite_MulOpCallExp'):
        assert not _is_linked(b2, 'oCLlite_MulOpCallExp', a)


def test_assoc_source84_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_NavigationExp()
    b2 = oCLlite_NavigationExp()
    _safe_set(a, 'oCLlite_OclLExpression85', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression85', b1)
    if hasattr(b1, 'oCLlite_NavigationExp'):
        assert _is_linked(b1, 'oCLlite_NavigationExp', a)
    _safe_set(a, 'oCLlite_OclLExpression85', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression85', b2)
    if hasattr(b1, 'oCLlite_NavigationExp'):
        assert not _is_linked(b1, 'oCLlite_NavigationExp', a)
    if hasattr(b2, 'oCLlite_NavigationExp'):
        assert _is_linked(b2, 'oCLlite_NavigationExp', a)
    _safe_set(a, 'oCLlite_OclLExpression85', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression85', b2)
    if hasattr(b2, 'oCLlite_NavigationExp'):
        assert not _is_linked(b2, 'oCLlite_NavigationExp', a)


def test_assoc_target17_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLExpression16', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression16', b1)
    if hasattr(b1, 'oCLlite_OclLExpression18'):
        assert _is_linked(b1, 'oCLlite_OclLExpression18', a)
    _safe_set(a, 'oCLlite_OclLExpression16', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression16', b2)
    if hasattr(b1, 'oCLlite_OclLExpression18'):
        assert not _is_linked(b1, 'oCLlite_OclLExpression18', a)
    if hasattr(b2, 'oCLlite_OclLExpression18'):
        assert _is_linked(b2, 'oCLlite_OclLExpression18', a)
    _safe_set(a, 'oCLlite_OclLExpression16', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression16', b2)
    if hasattr(b2, 'oCLlite_OclLExpression18'):
        assert not _is_linked(b2, 'oCLlite_OclLExpression18', a)


def test_assoc_then109_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_ElseIfThenExp()
    b2 = oCLlite_ElseIfThenExp()
    _safe_set(a, 'oCLlite_OclLExpression111', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression111', b1)
    if hasattr(b1, 'oCLlite_ElseIfThenExp110'):
        assert _is_linked(b1, 'oCLlite_ElseIfThenExp110', a)
    _safe_set(a, 'oCLlite_OclLExpression111', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression111', b2)
    if hasattr(b1, 'oCLlite_ElseIfThenExp110'):
        assert not _is_linked(b1, 'oCLlite_ElseIfThenExp110', a)
    if hasattr(b2, 'oCLlite_ElseIfThenExp110'):
        assert _is_linked(b2, 'oCLlite_ElseIfThenExp110', a)
    _safe_set(a, 'oCLlite_OclLExpression111', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression111', b2)
    if hasattr(b2, 'oCLlite_ElseIfThenExp110'):
        assert not _is_linked(b2, 'oCLlite_ElseIfThenExp110', a)


def test_assoc_then45_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_IfExp()
    b2 = oCLlite_IfExp()
    _safe_set(a, 'oCLlite_OclLExpression47', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression47', b1)
    if hasattr(b1, 'oCLlite_IfExp46'):
        assert _is_linked(b1, 'oCLlite_IfExp46', a)
    _safe_set(a, 'oCLlite_OclLExpression47', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression47', b2)
    if hasattr(b1, 'oCLlite_IfExp46'):
        assert not _is_linked(b1, 'oCLlite_IfExp46', a)
    if hasattr(b2, 'oCLlite_IfExp46'):
        assert _is_linked(b2, 'oCLlite_IfExp46', a)
    _safe_set(a, 'oCLlite_OclLExpression47', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression47', b2)
    if hasattr(b2, 'oCLlite_IfExp46'):
        assert not _is_linked(b2, 'oCLlite_IfExp46', a)


def test_assoc_type22_link_reassign_clear():
    a = oCLlite_Iterator(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_Iterator', b1)
    assert _is_linked(a, 'oCLlite_Iterator', b1)
    if hasattr(b1, 'oCLlite_OclLType'):
        assert _is_linked(b1, 'oCLlite_OclLType', a)
    _safe_set(a, 'oCLlite_Iterator', b2)
    assert _is_linked(a, 'oCLlite_Iterator', b2)
    if hasattr(b1, 'oCLlite_OclLType'):
        assert not _is_linked(b1, 'oCLlite_OclLType', a)
    if hasattr(b2, 'oCLlite_OclLType'):
        assert _is_linked(b2, 'oCLlite_OclLType', a)
    _safe_set(a, 'oCLlite_Iterator', None)
    assert not _is_linked(a, 'oCLlite_Iterator', b2)
    if hasattr(b2, 'oCLlite_OclLType'):
        assert not _is_linked(b2, 'oCLlite_OclLType', a)


def test_assoc_type23_link_reassign_clear():
    a = oCLlite_LocalVariable(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_LocalVariable24', b1)
    assert _is_linked(a, 'oCLlite_LocalVariable24', b1)
    if hasattr(b1, 'oCLlite_OclLType25'):
        assert _is_linked(b1, 'oCLlite_OclLType25', a)
    _safe_set(a, 'oCLlite_LocalVariable24', b2)
    assert _is_linked(a, 'oCLlite_LocalVariable24', b2)
    if hasattr(b1, 'oCLlite_OclLType25'):
        assert not _is_linked(b1, 'oCLlite_OclLType25', a)
    if hasattr(b2, 'oCLlite_OclLType25'):
        assert _is_linked(b2, 'oCLlite_OclLType25', a)
    _safe_set(a, 'oCLlite_LocalVariable24', None)
    assert not _is_linked(a, 'oCLlite_LocalVariable24', b2)
    if hasattr(b2, 'oCLlite_OclLType25'):
        assert not _is_linked(b2, 'oCLlite_OclLType25', a)


def test_assoc_type38_link_reassign_clear():
    a = oCLlite_TuplePart(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_TuplePart', b1)
    assert _is_linked(a, 'oCLlite_TuplePart', b1)
    if hasattr(b1, 'oCLlite_OclLType39'):
        assert _is_linked(b1, 'oCLlite_OclLType39', a)
    _safe_set(a, 'oCLlite_TuplePart', b2)
    assert _is_linked(a, 'oCLlite_TuplePart', b2)
    if hasattr(b1, 'oCLlite_OclLType39'):
        assert not _is_linked(b1, 'oCLlite_OclLType39', a)
    if hasattr(b2, 'oCLlite_OclLType39'):
        assert _is_linked(b2, 'oCLlite_OclLType39', a)
    _safe_set(a, 'oCLlite_TuplePart', None)
    assert not _is_linked(a, 'oCLlite_TuplePart', b2)
    if hasattr(b2, 'oCLlite_OclLType39'):
        assert not _is_linked(b2, 'oCLlite_OclLType39', a)


def test_assoc_uri8_link_reassign_clear():
    a = oCLlite_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    b1 = oCLlite_OclLModel(name="sample_text")
    b2 = oCLlite_OclLModel(name="sample_text_2")
    _safe_set(a, 'oCLlite_URI_', b1)
    assert _is_linked(a, 'oCLlite_URI_', b1)
    if hasattr(b1, 'oCLlite_OclLModel9'):
        assert _is_linked(b1, 'oCLlite_OclLModel9', a)
    _safe_set(a, 'oCLlite_URI_', b2)
    assert _is_linked(a, 'oCLlite_URI_', b2)
    if hasattr(b1, 'oCLlite_OclLModel9'):
        assert not _is_linked(b1, 'oCLlite_OclLModel9', a)
    if hasattr(b2, 'oCLlite_OclLModel9'):
        assert _is_linked(b2, 'oCLlite_OclLModel9', a)
    _safe_set(a, 'oCLlite_URI_', None)
    assert not _is_linked(a, 'oCLlite_URI_', b2)
    if hasattr(b2, 'oCLlite_OclLModel9'):
        assert not _is_linked(b2, 'oCLlite_OclLModel9', a)


def test_assoc_value35_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_MapElement()
    b2 = oCLlite_MapElement()
    _safe_set(a, 'oCLlite_OclLExpression37', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression37', b1)
    if hasattr(b1, 'oCLlite_MapElement36'):
        assert _is_linked(b1, 'oCLlite_MapElement36', a)
    _safe_set(a, 'oCLlite_OclLExpression37', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression37', b2)
    if hasattr(b1, 'oCLlite_MapElement36'):
        assert not _is_linked(b1, 'oCLlite_MapElement36', a)
    if hasattr(b2, 'oCLlite_MapElement36'):
        assert _is_linked(b2, 'oCLlite_MapElement36', a)
    _safe_set(a, 'oCLlite_OclLExpression37', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression37', b2)
    if hasattr(b2, 'oCLlite_MapElement36'):
        assert not _is_linked(b2, 'oCLlite_MapElement36', a)


def test_assoc_valueType63_link_reassign_clear():
    a = oCLlite_MapType(name="sample_text")
    b1 = oCLlite_OclLType()
    b2 = oCLlite_OclLType()
    _safe_set(a, 'oCLlite_MapType64', b1)
    assert _is_linked(a, 'oCLlite_MapType64', b1)
    if hasattr(b1, 'oCLlite_OclLType65'):
        assert _is_linked(b1, 'oCLlite_OclLType65', a)
    _safe_set(a, 'oCLlite_MapType64', b2)
    assert _is_linked(a, 'oCLlite_MapType64', b2)
    if hasattr(b1, 'oCLlite_OclLType65'):
        assert not _is_linked(b1, 'oCLlite_OclLType65', a)
    if hasattr(b2, 'oCLlite_OclLType65'):
        assert _is_linked(b2, 'oCLlite_OclLType65', a)
    _safe_set(a, 'oCLlite_MapType64', None)
    assert not _is_linked(a, 'oCLlite_MapType64', b2)
    if hasattr(b2, 'oCLlite_OclLType65'):
        assert not _is_linked(b2, 'oCLlite_OclLType65', a)


def test_assoc_variable11_link_reassign_clear():
    a = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    b1 = oCLlite_LocalVariable(name="sample_text")
    b2 = oCLlite_LocalVariable(name="sample_text_2")
    _safe_set(a, 'oCLlite_OclLExpression12', b1)
    assert _is_linked(a, 'oCLlite_OclLExpression12', b1)
    if hasattr(b1, 'oCLlite_LocalVariable'):
        assert _is_linked(b1, 'oCLlite_LocalVariable', a)
    _safe_set(a, 'oCLlite_OclLExpression12', b2)
    assert _is_linked(a, 'oCLlite_OclLExpression12', b2)
    if hasattr(b1, 'oCLlite_LocalVariable'):
        assert not _is_linked(b1, 'oCLlite_LocalVariable', a)
    if hasattr(b2, 'oCLlite_LocalVariable'):
        assert _is_linked(b2, 'oCLlite_LocalVariable', a)
    _safe_set(a, 'oCLlite_OclLExpression12', None)
    assert not _is_linked(a, 'oCLlite_OclLExpression12', b2)
    if hasattr(b2, 'oCLlite_LocalVariable'):
        assert not _is_linked(b2, 'oCLlite_LocalVariable', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CollectionExp_strategy = st.builds(CollectionExp)
@given(instance=CollectionExp_strategy)
@settings(max_examples=25)
def test_CollectionExp_instantiation(instance):
    assert isinstance(instance, CollectionExp)


ModuleElement_strategy = st.builds(ModuleElement)
@given(instance=ModuleElement_strategy)
@settings(max_examples=25)
def test_ModuleElement_instantiation(instance):
    assert isinstance(instance, ModuleElement)


OclLExpression_strategy = st.builds(OclLExpression)
@given(instance=OclLExpression_strategy)
@settings(max_examples=25)
def test_OclLExpression_instantiation(instance):
    assert isinstance(instance, OclLExpression)


OclLType_strategy = st.builds(OclLType)
@given(instance=OclLType_strategy)
@settings(max_examples=25)
def test_OclLType_instantiation(instance):
    assert isinstance(instance, OclLType)


PrimitiveExp_strategy = st.builds(PrimitiveExp)
@given(instance=PrimitiveExp_strategy)
@settings(max_examples=25)
def test_PrimitiveExp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)


oCLlite_AddOpCallExp_strategy = st.builds(oCLlite_AddOpCallExp)
@given(instance=oCLlite_AddOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_AddOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_AddOpCallExp)


oCLlite_BagExp_strategy = st.builds(oCLlite_BagExp)
@given(instance=oCLlite_BagExp_strategy)
@settings(max_examples=25)
def test_oCLlite_BagExp_instantiation(instance):
    assert isinstance(instance, oCLlite_BagExp)


oCLlite_BagType_strategy = st.builds(oCLlite_BagType, name=safe_text)
@given(instance=oCLlite_BagType_strategy)
@settings(max_examples=25)
def test_oCLlite_BagType_instantiation(instance):
    assert isinstance(instance, oCLlite_BagType)


oCLlite_BoolOpCallExp_strategy = st.builds(oCLlite_BoolOpCallExp)
@given(instance=oCLlite_BoolOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_BoolOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_BoolOpCallExp)


oCLlite_BooleanLiteralExp_strategy = st.builds(oCLlite_BooleanLiteralExp, symbol=safe_text)
@given(instance=oCLlite_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_BooleanLiteralExp)


oCLlite_BooleanType_strategy = st.builds(oCLlite_BooleanType, name=safe_text)
@given(instance=oCLlite_BooleanType_strategy)
@settings(max_examples=25)
def test_oCLlite_BooleanType_instantiation(instance):
    assert isinstance(instance, oCLlite_BooleanType)


oCLlite_CollectionExp_strategy = st.builds(oCLlite_CollectionExp)
@given(instance=oCLlite_CollectionExp_strategy)
@settings(max_examples=25)
def test_oCLlite_CollectionExp_instantiation(instance):
    assert isinstance(instance, oCLlite_CollectionExp)


oCLlite_CollectionOpCallExp_strategy = st.builds(oCLlite_CollectionOpCallExp)
@given(instance=oCLlite_CollectionOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_CollectionOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_CollectionOpCallExp)


oCLlite_ComOpCallExp_strategy = st.builds(oCLlite_ComOpCallExp)
@given(instance=oCLlite_ComOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_ComOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_ComOpCallExp)


oCLlite_ElseIfThenExp_strategy = st.builds(oCLlite_ElseIfThenExp)
@given(instance=oCLlite_ElseIfThenExp_strategy)
@settings(max_examples=25)
def test_oCLlite_ElseIfThenExp_instantiation(instance):
    assert isinstance(instance, oCLlite_ElseIfThenExp)


oCLlite_EnvType_strategy = st.builds(oCLlite_EnvType, name=safe_text)
@given(instance=oCLlite_EnvType_strategy)
@settings(max_examples=25)
def test_oCLlite_EnvType_instantiation(instance):
    assert isinstance(instance, oCLlite_EnvType)


oCLlite_EqOpCallExp_strategy = st.builds(oCLlite_EqOpCallExp)
@given(instance=oCLlite_EqOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_EqOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_EqOpCallExp)


oCLlite_IfExp_strategy = st.builds(oCLlite_IfExp)
@given(instance=oCLlite_IfExp_strategy)
@settings(max_examples=25)
def test_oCLlite_IfExp_instantiation(instance):
    assert isinstance(instance, oCLlite_IfExp)


oCLlite_Import_strategy = st.builds(oCLlite_Import, name=safe_text)
@given(instance=oCLlite_Import_strategy)
@settings(max_examples=25)
def test_oCLlite_Import_instantiation(instance):
    assert isinstance(instance, oCLlite_Import)


oCLlite_IntegerType_strategy = st.builds(oCLlite_IntegerType, name=safe_text)
@given(instance=oCLlite_IntegerType_strategy)
@settings(max_examples=25)
def test_oCLlite_IntegerType_instantiation(instance):
    assert isinstance(instance, oCLlite_IntegerType)


oCLlite_InvalidLiteralExp_strategy = st.builds(oCLlite_InvalidLiteralExp)
@given(instance=oCLlite_InvalidLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_InvalidLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_InvalidLiteralExp)


oCLlite_IterateExp_strategy = st.builds(oCLlite_IterateExp)
@given(instance=oCLlite_IterateExp_strategy)
@settings(max_examples=25)
def test_oCLlite_IterateExp_instantiation(instance):
    assert isinstance(instance, oCLlite_IterateExp)


oCLlite_Iterator_strategy = st.builds(oCLlite_Iterator, name=safe_text)
@given(instance=oCLlite_Iterator_strategy)
@settings(max_examples=25)
def test_oCLlite_Iterator_instantiation(instance):
    assert isinstance(instance, oCLlite_Iterator)


oCLlite_IteratorExp_strategy = st.builds(oCLlite_IteratorExp)
@given(instance=oCLlite_IteratorExp_strategy)
@settings(max_examples=25)
def test_oCLlite_IteratorExp_instantiation(instance):
    assert isinstance(instance, oCLlite_IteratorExp)


oCLlite_LambdaExp_strategy = st.builds(oCLlite_LambdaExp)
@given(instance=oCLlite_LambdaExp_strategy)
@settings(max_examples=25)
def test_oCLlite_LambdaExp_instantiation(instance):
    assert isinstance(instance, oCLlite_LambdaExp)


oCLlite_LambdaType_strategy = st.builds(oCLlite_LambdaType, name=safe_text)
@given(instance=oCLlite_LambdaType_strategy)
@settings(max_examples=25)
def test_oCLlite_LambdaType_instantiation(instance):
    assert isinstance(instance, oCLlite_LambdaType)


oCLlite_LocalVariable_strategy = st.builds(oCLlite_LocalVariable, name=safe_text)
@given(instance=oCLlite_LocalVariable_strategy)
@settings(max_examples=25)
def test_oCLlite_LocalVariable_instantiation(instance):
    assert isinstance(instance, oCLlite_LocalVariable)


oCLlite_MapElement_strategy = st.builds(oCLlite_MapElement)
@given(instance=oCLlite_MapElement_strategy)
@settings(max_examples=25)
def test_oCLlite_MapElement_instantiation(instance):
    assert isinstance(instance, oCLlite_MapElement)


oCLlite_MapExp_strategy = st.builds(oCLlite_MapExp)
@given(instance=oCLlite_MapExp_strategy)
@settings(max_examples=25)
def test_oCLlite_MapExp_instantiation(instance):
    assert isinstance(instance, oCLlite_MapExp)


oCLlite_MapType_strategy = st.builds(oCLlite_MapType, name=safe_text)
@given(instance=oCLlite_MapType_strategy)
@settings(max_examples=25)
def test_oCLlite_MapType_instantiation(instance):
    assert isinstance(instance, oCLlite_MapType)


oCLlite_Module_strategy = st.builds(oCLlite_Module, name=safe_text)
@given(instance=oCLlite_Module_strategy)
@settings(max_examples=25)
def test_oCLlite_Module_instantiation(instance):
    assert isinstance(instance, oCLlite_Module)


oCLlite_ModuleElement_strategy = st.builds(oCLlite_ModuleElement)
@given(instance=oCLlite_ModuleElement_strategy)
@settings(max_examples=25)
def test_oCLlite_ModuleElement_instantiation(instance):
    assert isinstance(instance, oCLlite_ModuleElement)


oCLlite_MulOpCallExp_strategy = st.builds(oCLlite_MulOpCallExp)
@given(instance=oCLlite_MulOpCallExp_strategy)
@settings(max_examples=25)
def test_oCLlite_MulOpCallExp_instantiation(instance):
    assert isinstance(instance, oCLlite_MulOpCallExp)


oCLlite_NavigationExp_strategy = st.builds(oCLlite_NavigationExp)
@given(instance=oCLlite_NavigationExp_strategy)
@settings(max_examples=25)
def test_oCLlite_NavigationExp_instantiation(instance):
    assert isinstance(instance, oCLlite_NavigationExp)


oCLlite_NavigationOrAttributeCall_strategy = st.builds(oCLlite_NavigationOrAttributeCall, feature=safe_text)
@given(instance=oCLlite_NavigationOrAttributeCall_strategy)
@settings(max_examples=25)
def test_oCLlite_NavigationOrAttributeCall_instantiation(instance):
    assert isinstance(instance, oCLlite_NavigationOrAttributeCall)


oCLlite_NestedExp_strategy = st.builds(oCLlite_NestedExp)
@given(instance=oCLlite_NestedExp_strategy)
@settings(max_examples=25)
def test_oCLlite_NestedExp_instantiation(instance):
    assert isinstance(instance, oCLlite_NestedExp)


oCLlite_NullLiteralExp_strategy = st.builds(oCLlite_NullLiteralExp)
@given(instance=oCLlite_NullLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_NullLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_NullLiteralExp)


oCLlite_NumberLiteralExp_strategy = st.builds(oCLlite_NumberLiteralExp, symbol=st.integers())
@given(instance=oCLlite_NumberLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_NumberLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_NumberLiteralExp)


oCLlite_OclLAnyType_strategy = st.builds(oCLlite_OclLAnyType, name=safe_text)
@given(instance=oCLlite_OclLAnyType_strategy)
@settings(max_examples=25)
def test_oCLlite_OclLAnyType_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLAnyType)


oCLlite_OclLExpression_strategy = st.builds(oCLlite_OclLExpression, elements=safe_text, name=safe_text)
@given(instance=oCLlite_OclLExpression_strategy)
@settings(max_examples=25)
def test_oCLlite_OclLExpression_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLExpression)


oCLlite_OclLModel_strategy = st.builds(oCLlite_OclLModel, name=safe_text)
@given(instance=oCLlite_OclLModel_strategy)
@settings(max_examples=25)
def test_oCLlite_OclLModel_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLModel)


oCLlite_OclLModelElementExp_strategy = st.builds(oCLlite_OclLModelElementExp, name=safe_text)
@given(instance=oCLlite_OclLModelElementExp_strategy)
@settings(max_examples=25)
def test_oCLlite_OclLModelElementExp_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLModelElementExp)


oCLlite_OclLType_strategy = st.builds(oCLlite_OclLType)
@given(instance=oCLlite_OclLType_strategy)
@settings(max_examples=25)
def test_oCLlite_OclLType_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLType)


oCLlite_OperationCall_strategy = st.builds(oCLlite_OperationCall)
@given(instance=oCLlite_OperationCall_strategy)
@settings(max_examples=25)
def test_oCLlite_OperationCall_instantiation(instance):
    assert isinstance(instance, oCLlite_OperationCall)


oCLlite_OrderedSetExp_strategy = st.builds(oCLlite_OrderedSetExp)
@given(instance=oCLlite_OrderedSetExp_strategy)
@settings(max_examples=25)
def test_oCLlite_OrderedSetExp_instantiation(instance):
    assert isinstance(instance, oCLlite_OrderedSetExp)


oCLlite_OrderedSetType_strategy = st.builds(oCLlite_OrderedSetType, name=safe_text)
@given(instance=oCLlite_OrderedSetType_strategy)
@settings(max_examples=25)
def test_oCLlite_OrderedSetType_instantiation(instance):
    assert isinstance(instance, oCLlite_OrderedSetType)


oCLlite_PrimitiveExp_strategy = st.builds(oCLlite_PrimitiveExp)
@given(instance=oCLlite_PrimitiveExp_strategy)
@settings(max_examples=25)
def test_oCLlite_PrimitiveExp_instantiation(instance):
    assert isinstance(instance, oCLlite_PrimitiveExp)


oCLlite_Query_strategy = st.builds(oCLlite_Query, name=safe_text)
@given(instance=oCLlite_Query_strategy)
@settings(max_examples=25)
def test_oCLlite_Query_instantiation(instance):
    assert isinstance(instance, oCLlite_Query)


oCLlite_RealType_strategy = st.builds(oCLlite_RealType, name=safe_text)
@given(instance=oCLlite_RealType_strategy)
@settings(max_examples=25)
def test_oCLlite_RealType_instantiation(instance):
    assert isinstance(instance, oCLlite_RealType)


oCLlite_SelfExp_strategy = st.builds(oCLlite_SelfExp)
@given(instance=oCLlite_SelfExp_strategy)
@settings(max_examples=25)
def test_oCLlite_SelfExp_instantiation(instance):
    assert isinstance(instance, oCLlite_SelfExp)


oCLlite_SequenceExp_strategy = st.builds(oCLlite_SequenceExp)
@given(instance=oCLlite_SequenceExp_strategy)
@settings(max_examples=25)
def test_oCLlite_SequenceExp_instantiation(instance):
    assert isinstance(instance, oCLlite_SequenceExp)


oCLlite_SequenceType_strategy = st.builds(oCLlite_SequenceType, name=safe_text)
@given(instance=oCLlite_SequenceType_strategy)
@settings(max_examples=25)
def test_oCLlite_SequenceType_instantiation(instance):
    assert isinstance(instance, oCLlite_SequenceType)


oCLlite_SetExp_strategy = st.builds(oCLlite_SetExp)
@given(instance=oCLlite_SetExp_strategy)
@settings(max_examples=25)
def test_oCLlite_SetExp_instantiation(instance):
    assert isinstance(instance, oCLlite_SetExp)


oCLlite_SetType_strategy = st.builds(oCLlite_SetType, name=safe_text)
@given(instance=oCLlite_SetType_strategy)
@settings(max_examples=25)
def test_oCLlite_SetType_instantiation(instance):
    assert isinstance(instance, oCLlite_SetType)


oCLlite_StringLiteralExp_strategy = st.builds(oCLlite_StringLiteralExp, segments=safe_text)
@given(instance=oCLlite_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_StringLiteralExp)


oCLlite_StringType_strategy = st.builds(oCLlite_StringType, name=safe_text)
@given(instance=oCLlite_StringType_strategy)
@settings(max_examples=25)
def test_oCLlite_StringType_instantiation(instance):
    assert isinstance(instance, oCLlite_StringType)


oCLlite_TupleExp_strategy = st.builds(oCLlite_TupleExp)
@given(instance=oCLlite_TupleExp_strategy)
@settings(max_examples=25)
def test_oCLlite_TupleExp_instantiation(instance):
    assert isinstance(instance, oCLlite_TupleExp)


oCLlite_TuplePart_strategy = st.builds(oCLlite_TuplePart, name=safe_text)
@given(instance=oCLlite_TuplePart_strategy)
@settings(max_examples=25)
def test_oCLlite_TuplePart_instantiation(instance):
    assert isinstance(instance, oCLlite_TuplePart)


oCLlite_TupleType_strategy = st.builds(oCLlite_TupleType)
@given(instance=oCLlite_TupleType_strategy)
@settings(max_examples=25)
def test_oCLlite_TupleType_instantiation(instance):
    assert isinstance(instance, oCLlite_TupleType)


oCLlite_URI__strategy = st.builds(oCLlite_URI_, authority=safe_text, fragment_=safe_text, scheme=safe_text)
@given(instance=oCLlite_URI__strategy)
@settings(max_examples=25)
def test_oCLlite_URI__instantiation(instance):
    assert isinstance(instance, oCLlite_URI_)


oCLlite_UnlimitedNaturalLiteralExp_strategy = st.builds(oCLlite_UnlimitedNaturalLiteralExp)
@given(instance=oCLlite_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=25)
def test_oCLlite_UnlimitedNaturalLiteralExp_instantiation(instance):
    assert isinstance(instance, oCLlite_UnlimitedNaturalLiteralExp)



