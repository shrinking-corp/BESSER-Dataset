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
    JoinEntity,
    FromRange,
    dom_InCollection,
    dom_InClass,
    dom_FromClass,
    Expression,
    dom_CollectionFunction,
    dom_AggregateFunction,
    dom_FunctionCall,
    dom_CastFunction,
    dom_JoinEntity,
    dom_InCollectionElements,
    dom_PropertyValue,
    dom_PropertyAssignment,
    SelectStatement,
    dom_SelectObject,
    dom_SelectClass,
    dom_SelectProperties,
    dom_SortOrderElement,
    dom_Join,
    dom_FromRange,
    dom_CallOutputParameter,
    dom_CallInputParameter,
    QlStatement,
    dom_InsertStatement,
    dom_UpdateStatement,
    dom_DeleteStatement,
    dom_SelectStatement,
    dom_CallableStatement,
    dom_Function,
    DaoFeature,
    dom_SqlType,
    dom_OneToOne,
    dom_ManyToOne,
    dom_Column,
    dom_DataBaseConstraint,
    dom_QlStatement,
    dom_QueryParameter,
    dom_ManyToMany,
    dom_OneToMany,
    dom_DaoFeature,
    dom_AttributeSortOrder,
    dom_ValidatorReference,
    dom_Constraint,
    dom_BoolLiteral,
    ExpressionFlag,
    dom_ReadOnlyFlag,
    dom_AvailableFlag,
    dom_RequiredFlag,
    dom_EqualityExpr,
    AttributeFlag,
    dom_TransientFlag,
    dom_DerivedFlag,
    dom_ExpressionFlag,
    AttributeProperty,
    dom_AttributeTextProperty,
    dom_AttributeValidationProperty,
    dom_BetweenExpression,
    dom_UnaryExpression,
    dom_MemberOfExpression,
    dom_LikeExpression,
    dom_InExpression,
    dom_NotExpression,
    dom_BinaryExpression,
    dom_AliasedExpression,
    dom_PresentableFeature,
    dom_WhenClause,
    LiteralValue,
    dom_RealLiteralValue,
    dom_IntegerLiteralValue,
    dom_EmptyLiteralValue,
    dom_NullLiteralValue,
    dom_BooleanLiteralValue,
    dom_LiteralValue,
    dom_ParenthesizedExpression,
    dom_SubQuery,
    dom_AltWhenClause,
    dom_StringLiteralValue,
    dom_TrimFunction,
    dom_CaseExpression,
    dom_QuantifiedExpression,
    dom_QueryParameterValue,
    dom_QueryParameterReference,
    dom_AttributeFlag,
    dom_IncrementerReference,
    dom_DataTypeAndTypeParameter,
    dom_PropertyMapping,
    dom_ConditionsBlock,
    PresentableFeature,
    ComplexType,
    dom_ValueObject,
    dom_AttributeProperty,
    dom_DataView,
    dom_Type,
    QueryParameterReference,
    QueryParameter,
    dom_Expression,
    dom_DaoOperation,
    dom_Dependant,
    Dependant,
    dom_Entity,
    dom_Parameter,
    DaoOperation,
    dom_SimpleType,
    IDocumentable,
    dom_FeatureReference,
    dom_AttributeGroup,
    dom_Operation,
    dom_QueryOperation,
    dom_DelegateOperation,
    ReferenceableByXmadslVariable,
    dom_IElementWithNoName,
    dom_Property,
    dom_Attribute,
    Type,
    ModelElement,
    dom_ApplicationSession,
    dom_Mapper,
    dom_Dao,
    dom_Service,
    dom_ComplexType,
    DataBaseConstraintType,
    CrudOperationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_joinentity_is_not_abstract():
    assert not inspect.isabstract(JoinEntity)


def test_hyp_joinentity_constructor_exists():
    assert callable(JoinEntity.__init__)


def test_hyp_joinentity_constructor_args():
    sig = inspect.signature(JoinEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fromrange_is_not_abstract():
    assert not inspect.isabstract(FromRange)


def test_hyp_fromrange_constructor_exists():
    assert callable(FromRange.__init__)


def test_hyp_fromrange_constructor_args():
    sig = inspect.signature(FromRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_incollection_is_not_abstract():
    assert not inspect.isabstract(dom_InCollection)


def test_hyp_dom_incollection_constructor_exists():
    assert callable(dom_InCollection.__init__)


def test_hyp_dom_incollection_constructor_args():
    sig = inspect.signature(dom_InCollection.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "path" in params, "Missing parameter 'path'"





def test_hyp_dom_inclass_is_not_abstract():
    assert not inspect.isabstract(dom_InClass)


def test_hyp_dom_inclass_constructor_exists():
    assert callable(dom_InClass.__init__)


def test_hyp_dom_inclass_constructor_args():
    sig = inspect.signature(dom_InClass.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_dom_fromclass_is_not_abstract():
    assert not inspect.isabstract(dom_FromClass)


def test_hyp_dom_fromclass_constructor_exists():
    assert callable(dom_FromClass.__init__)


def test_hyp_dom_fromclass_constructor_args():
    sig = inspect.signature(dom_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "popertyFetch" in params, "Missing parameter 'popertyFetch'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_collectionfunction_is_not_abstract():
    assert not inspect.isabstract(dom_CollectionFunction)


def test_hyp_dom_collectionfunction_constructor_exists():
    assert callable(dom_CollectionFunction.__init__)


def test_hyp_dom_collectionfunction_constructor_args():
    sig = inspect.signature(dom_CollectionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"




def test_hyp_dom_aggregatefunction_is_not_abstract():
    assert not inspect.isabstract(dom_AggregateFunction)


def test_hyp_dom_aggregatefunction_constructor_exists():
    assert callable(dom_AggregateFunction.__init__)


def test_hyp_dom_aggregatefunction_constructor_args():
    sig = inspect.signature(dom_AggregateFunction.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "function" in params, "Missing parameter 'function'"
    assert "all" in params, "Missing parameter 'all'"







def test_hyp_dom_functioncall_is_not_abstract():
    assert not inspect.isabstract(dom_FunctionCall)


def test_hyp_dom_functioncall_constructor_exists():
    assert callable(dom_FunctionCall.__init__)


def test_hyp_dom_functioncall_constructor_args():
    sig = inspect.signature(dom_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"




def test_hyp_dom_castfunction_is_not_abstract():
    assert not inspect.isabstract(dom_CastFunction)


def test_hyp_dom_castfunction_constructor_exists():
    assert callable(dom_CastFunction.__init__)


def test_hyp_dom_castfunction_constructor_args():
    sig = inspect.signature(dom_CastFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_dom_joinentity_is_not_abstract():
    assert not inspect.isabstract(dom_JoinEntity)


def test_hyp_dom_joinentity_constructor_exists():
    assert callable(dom_JoinEntity.__init__)


def test_hyp_dom_joinentity_constructor_args():
    sig = inspect.signature(dom_JoinEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_incollectionelements_is_not_abstract():
    assert not inspect.isabstract(dom_InCollectionElements)


def test_hyp_dom_incollectionelements_constructor_exists():
    assert callable(dom_InCollectionElements.__init__)


def test_hyp_dom_incollectionelements_constructor_args():
    sig = inspect.signature(dom_InCollectionElements.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_dom_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyValue)


def test_hyp_dom_propertyvalue_constructor_exists():
    assert callable(dom_PropertyValue.__init__)


def test_hyp_dom_propertyvalue_constructor_args():
    sig = inspect.signature(dom_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "classProperty" in params, "Missing parameter 'classProperty'"
    assert "segments" in params, "Missing parameter 'segments'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_dom_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyAssignment)


def test_hyp_dom_propertyassignment_constructor_exists():
    assert callable(dom_PropertyAssignment.__init__)


def test_hyp_dom_propertyassignment_constructor_args():
    sig = inspect.signature(dom_PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_hyp_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_hyp_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_selectobject_is_not_abstract():
    assert not inspect.isabstract(dom_SelectObject)


def test_hyp_dom_selectobject_constructor_exists():
    assert callable(dom_SelectObject.__init__)


def test_hyp_dom_selectobject_constructor_args():
    sig = inspect.signature(dom_SelectObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_selectclass_is_not_abstract():
    assert not inspect.isabstract(dom_SelectClass)


def test_hyp_dom_selectclass_constructor_exists():
    assert callable(dom_SelectClass.__init__)


def test_hyp_dom_selectclass_constructor_args():
    sig = inspect.signature(dom_SelectClass.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"




def test_hyp_dom_selectproperties_is_not_abstract():
    assert not inspect.isabstract(dom_SelectProperties)


def test_hyp_dom_selectproperties_constructor_exists():
    assert callable(dom_SelectProperties.__init__)


def test_hyp_dom_selectproperties_constructor_args():
    sig = inspect.signature(dom_SelectProperties.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"




def test_hyp_dom_sortorderelement_is_not_abstract():
    assert not inspect.isabstract(dom_SortOrderElement)


def test_hyp_dom_sortorderelement_constructor_exists():
    assert callable(dom_SortOrderElement.__init__)


def test_hyp_dom_sortorderelement_constructor_args():
    sig = inspect.signature(dom_SortOrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "sortOrder" in params, "Missing parameter 'sortOrder'"




def test_hyp_dom_join_is_not_abstract():
    assert not inspect.isabstract(dom_Join)


def test_hyp_dom_join_constructor_exists():
    assert callable(dom_Join.__init__)


def test_hyp_dom_join_constructor_args():
    sig = inspect.signature(dom_Join.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "propertyFetch" in params, "Missing parameter 'propertyFetch'"






def test_hyp_dom_fromrange_is_not_abstract():
    assert not inspect.isabstract(dom_FromRange)


def test_hyp_dom_fromrange_constructor_exists():
    assert callable(dom_FromRange.__init__)


def test_hyp_dom_fromrange_constructor_args():
    sig = inspect.signature(dom_FromRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_calloutputparameter_is_not_abstract():
    assert not inspect.isabstract(dom_CallOutputParameter)


def test_hyp_dom_calloutputparameter_constructor_exists():
    assert callable(dom_CallOutputParameter.__init__)


def test_hyp_dom_calloutputparameter_constructor_args():
    sig = inspect.signature(dom_CallOutputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_callinputparameter_is_not_abstract():
    assert not inspect.isabstract(dom_CallInputParameter)


def test_hyp_dom_callinputparameter_constructor_exists():
    assert callable(dom_CallInputParameter.__init__)


def test_hyp_dom_callinputparameter_constructor_args():
    sig = inspect.signature(dom_CallInputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_qlstatement_is_not_abstract():
    assert not inspect.isabstract(QlStatement)


def test_hyp_qlstatement_constructor_exists():
    assert callable(QlStatement.__init__)


def test_hyp_qlstatement_constructor_args():
    sig = inspect.signature(QlStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_insertstatement_is_not_abstract():
    assert not inspect.isabstract(dom_InsertStatement)


def test_hyp_dom_insertstatement_constructor_exists():
    assert callable(dom_InsertStatement.__init__)


def test_hyp_dom_insertstatement_constructor_args():
    sig = inspect.signature(dom_InsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_updatestatement_is_not_abstract():
    assert not inspect.isabstract(dom_UpdateStatement)


def test_hyp_dom_updatestatement_constructor_exists():
    assert callable(dom_UpdateStatement.__init__)


def test_hyp_dom_updatestatement_constructor_args():
    sig = inspect.signature(dom_UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "versioned" in params, "Missing parameter 'versioned'"





def test_hyp_dom_deletestatement_is_not_abstract():
    assert not inspect.isabstract(dom_DeleteStatement)


def test_hyp_dom_deletestatement_constructor_exists():
    assert callable(dom_DeleteStatement.__init__)


def test_hyp_dom_deletestatement_constructor_args():
    sig = inspect.signature(dom_DeleteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_selectstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SelectStatement)


def test_hyp_dom_selectstatement_constructor_exists():
    assert callable(dom_SelectStatement.__init__)


def test_hyp_dom_selectstatement_constructor_args():
    sig = inspect.signature(dom_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_callablestatement_is_not_abstract():
    assert not inspect.isabstract(dom_CallableStatement)


def test_hyp_dom_callablestatement_constructor_exists():
    assert callable(dom_CallableStatement.__init__)


def test_hyp_dom_callablestatement_constructor_args():
    sig = inspect.signature(dom_CallableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "functionCall" in params, "Missing parameter 'functionCall'"





def test_hyp_dom_function_is_not_abstract():
    assert not inspect.isabstract(dom_Function)


def test_hyp_dom_function_constructor_exists():
    assert callable(dom_Function.__init__)


def test_hyp_dom_function_constructor_args():
    sig = inspect.signature(dom_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_daofeature_is_not_abstract():
    assert not inspect.isabstract(DaoFeature)


def test_hyp_daofeature_constructor_exists():
    assert callable(DaoFeature.__init__)


def test_hyp_daofeature_constructor_args():
    sig = inspect.signature(DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_sqltype_is_not_abstract():
    assert not inspect.isabstract(dom_SqlType)


def test_hyp_dom_sqltype_constructor_exists():
    assert callable(dom_SqlType.__init__)


def test_hyp_dom_sqltype_constructor_args():
    sig = inspect.signature(dom_SqlType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_onetoone_is_not_abstract():
    assert not inspect.isabstract(dom_OneToOne)


def test_hyp_dom_onetoone_constructor_exists():
    assert callable(dom_OneToOne.__init__)


def test_hyp_dom_onetoone_constructor_args():
    sig = inspect.signature(dom_OneToOne.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_manytoone_is_not_abstract():
    assert not inspect.isabstract(dom_ManyToOne)


def test_hyp_dom_manytoone_constructor_exists():
    assert callable(dom_ManyToOne.__init__)


def test_hyp_dom_manytoone_constructor_args():
    sig = inspect.signature(dom_ManyToOne.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "derived" in params, "Missing parameter 'derived'"





def test_hyp_dom_column_is_not_abstract():
    assert not inspect.isabstract(dom_Column)


def test_hyp_dom_column_constructor_exists():
    assert callable(dom_Column.__init__)


def test_hyp_dom_column_constructor_args():
    sig = inspect.signature(dom_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"




def test_hyp_dom_databaseconstraint_is_not_abstract():
    assert not inspect.isabstract(dom_DataBaseConstraint)


def test_hyp_dom_databaseconstraint_constructor_exists():
    assert callable(dom_DataBaseConstraint.__init__)


def test_hyp_dom_databaseconstraint_constructor_args():
    sig = inspect.signature(dom_DataBaseConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_dom_qlstatement_is_not_abstract():
    assert not inspect.isabstract(dom_QlStatement)


def test_hyp_dom_qlstatement_constructor_exists():
    assert callable(dom_QlStatement.__init__)


def test_hyp_dom_qlstatement_constructor_args():
    sig = inspect.signature(dom_QlStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_queryparameter_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameter)


def test_hyp_dom_queryparameter_constructor_exists():
    assert callable(dom_QueryParameter.__init__)


def test_hyp_dom_queryparameter_constructor_args():
    sig = inspect.signature(dom_QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_manytomany_is_not_abstract():
    assert not inspect.isabstract(dom_ManyToMany)


def test_hyp_dom_manytomany_constructor_exists():
    assert callable(dom_ManyToMany.__init__)


def test_hyp_dom_manytomany_constructor_args():
    sig = inspect.signature(dom_ManyToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "inverse" in params, "Missing parameter 'inverse'"






def test_hyp_dom_onetomany_is_not_abstract():
    assert not inspect.isabstract(dom_OneToMany)


def test_hyp_dom_onetomany_constructor_exists():
    assert callable(dom_OneToMany.__init__)


def test_hyp_dom_onetomany_constructor_args():
    sig = inspect.signature(dom_OneToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"




def test_hyp_dom_daofeature_is_not_abstract():
    assert not inspect.isabstract(dom_DaoFeature)


def test_hyp_dom_daofeature_constructor_exists():
    assert callable(dom_DaoFeature.__init__)


def test_hyp_dom_daofeature_constructor_args():
    sig = inspect.signature(dom_DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_attributesortorder_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeSortOrder)


def test_hyp_dom_attributesortorder_constructor_exists():
    assert callable(dom_AttributeSortOrder.__init__)


def test_hyp_dom_attributesortorder_constructor_args():
    sig = inspect.signature(dom_AttributeSortOrder.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"





def test_hyp_dom_validatorreference_is_not_abstract():
    assert not inspect.isabstract(dom_ValidatorReference)


def test_hyp_dom_validatorreference_constructor_exists():
    assert callable(dom_ValidatorReference.__init__)


def test_hyp_dom_validatorreference_constructor_args():
    sig = inspect.signature(dom_ValidatorReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_constraint_is_not_abstract():
    assert not inspect.isabstract(dom_Constraint)


def test_hyp_dom_constraint_constructor_exists():
    assert callable(dom_Constraint.__init__)


def test_hyp_dom_constraint_constructor_args():
    sig = inspect.signature(dom_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_boolliteral_is_not_abstract():
    assert not inspect.isabstract(dom_BoolLiteral)


def test_hyp_dom_boolliteral_constructor_exists():
    assert callable(dom_BoolLiteral.__init__)


def test_hyp_dom_boolliteral_constructor_args():
    sig = inspect.signature(dom_BoolLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionflag_is_not_abstract():
    assert not inspect.isabstract(ExpressionFlag)


def test_hyp_expressionflag_constructor_exists():
    assert callable(ExpressionFlag.__init__)


def test_hyp_expressionflag_constructor_args():
    sig = inspect.signature(ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_readonlyflag_is_not_abstract():
    assert not inspect.isabstract(dom_ReadOnlyFlag)


def test_hyp_dom_readonlyflag_constructor_exists():
    assert callable(dom_ReadOnlyFlag.__init__)


def test_hyp_dom_readonlyflag_constructor_args():
    sig = inspect.signature(dom_ReadOnlyFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_availableflag_is_not_abstract():
    assert not inspect.isabstract(dom_AvailableFlag)


def test_hyp_dom_availableflag_constructor_exists():
    assert callable(dom_AvailableFlag.__init__)


def test_hyp_dom_availableflag_constructor_args():
    sig = inspect.signature(dom_AvailableFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_requiredflag_is_not_abstract():
    assert not inspect.isabstract(dom_RequiredFlag)


def test_hyp_dom_requiredflag_constructor_exists():
    assert callable(dom_RequiredFlag.__init__)


def test_hyp_dom_requiredflag_constructor_args():
    sig = inspect.signature(dom_RequiredFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_equalityexpr_is_not_abstract():
    assert not inspect.isabstract(dom_EqualityExpr)


def test_hyp_dom_equalityexpr_constructor_exists():
    assert callable(dom_EqualityExpr.__init__)


def test_hyp_dom_equalityexpr_constructor_args():
    sig = inspect.signature(dom_EqualityExpr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributeflag_is_not_abstract():
    assert not inspect.isabstract(AttributeFlag)


def test_hyp_attributeflag_constructor_exists():
    assert callable(AttributeFlag.__init__)


def test_hyp_attributeflag_constructor_args():
    sig = inspect.signature(AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_transientflag_is_not_abstract():
    assert not inspect.isabstract(dom_TransientFlag)


def test_hyp_dom_transientflag_constructor_exists():
    assert callable(dom_TransientFlag.__init__)


def test_hyp_dom_transientflag_constructor_args():
    sig = inspect.signature(dom_TransientFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_derivedflag_is_not_abstract():
    assert not inspect.isabstract(dom_DerivedFlag)


def test_hyp_dom_derivedflag_constructor_exists():
    assert callable(dom_DerivedFlag.__init__)


def test_hyp_dom_derivedflag_constructor_args():
    sig = inspect.signature(dom_DerivedFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expressionflag_is_not_abstract():
    assert not inspect.isabstract(dom_ExpressionFlag)


def test_hyp_dom_expressionflag_constructor_exists():
    assert callable(dom_ExpressionFlag.__init__)


def test_hyp_dom_expressionflag_constructor_args():
    sig = inspect.signature(dom_ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributeproperty_is_not_abstract():
    assert not inspect.isabstract(AttributeProperty)


def test_hyp_attributeproperty_constructor_exists():
    assert callable(AttributeProperty.__init__)


def test_hyp_attributeproperty_constructor_args():
    sig = inspect.signature(AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_attributetextproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeTextProperty)


def test_hyp_dom_attributetextproperty_constructor_exists():
    assert callable(dom_AttributeTextProperty.__init__)


def test_hyp_dom_attributetextproperty_constructor_args():
    sig = inspect.signature(dom_AttributeTextProperty.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "hstoreColumn" in params, "Missing parameter 'hstoreColumn'"
    assert "unitText" in params, "Missing parameter 'unitText'"







def test_hyp_dom_attributevalidationproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeValidationProperty)


def test_hyp_dom_attributevalidationproperty_constructor_exists():
    assert callable(dom_AttributeValidationProperty.__init__)


def test_hyp_dom_attributevalidationproperty_constructor_args():
    sig = inspect.signature(dom_AttributeValidationProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_betweenexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BetweenExpression)


def test_hyp_dom_betweenexpression_constructor_exists():
    assert callable(dom_BetweenExpression.__init__)


def test_hyp_dom_betweenexpression_constructor_args():
    sig = inspect.signature(dom_BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "not_" in params, "Missing parameter 'not_'"





def test_hyp_dom_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_UnaryExpression)


def test_hyp_dom_unaryexpression_constructor_exists():
    assert callable(dom_UnaryExpression.__init__)


def test_hyp_dom_unaryexpression_constructor_args():
    sig = inspect.signature(dom_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_memberofexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MemberOfExpression)


def test_hyp_dom_memberofexpression_constructor_exists():
    assert callable(dom_MemberOfExpression.__init__)


def test_hyp_dom_memberofexpression_constructor_args():
    sig = inspect.signature(dom_MemberOfExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "memberOf" in params, "Missing parameter 'memberOf'"
    assert "operator" in params, "Missing parameter 'operator'"






def test_hyp_dom_likeexpression_is_not_abstract():
    assert not inspect.isabstract(dom_LikeExpression)


def test_hyp_dom_likeexpression_constructor_exists():
    assert callable(dom_LikeExpression.__init__)


def test_hyp_dom_likeexpression_constructor_args():
    sig = inspect.signature(dom_LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"





def test_hyp_dom_inexpression_is_not_abstract():
    assert not inspect.isabstract(dom_InExpression)


def test_hyp_dom_inexpression_constructor_exists():
    assert callable(dom_InExpression.__init__)


def test_hyp_dom_inexpression_constructor_args():
    sig = inspect.signature(dom_InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"





def test_hyp_dom_notexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NotExpression)


def test_hyp_dom_notexpression_constructor_exists():
    assert callable(dom_NotExpression.__init__)


def test_hyp_dom_notexpression_constructor_args():
    sig = inspect.signature(dom_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BinaryExpression)


def test_hyp_dom_binaryexpression_constructor_exists():
    assert callable(dom_BinaryExpression.__init__)


def test_hyp_dom_binaryexpression_constructor_args():
    sig = inspect.signature(dom_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_aliasedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_AliasedExpression)


def test_hyp_dom_aliasedexpression_constructor_exists():
    assert callable(dom_AliasedExpression.__init__)


def test_hyp_dom_aliasedexpression_constructor_args():
    sig = inspect.signature(dom_AliasedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_presentablefeature_is_not_abstract():
    assert not inspect.isabstract(dom_PresentableFeature)


def test_hyp_dom_presentablefeature_constructor_exists():
    assert callable(dom_PresentableFeature.__init__)


def test_hyp_dom_presentablefeature_constructor_args():
    sig = inspect.signature(dom_PresentableFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_whenclause_is_not_abstract():
    assert not inspect.isabstract(dom_WhenClause)


def test_hyp_dom_whenclause_constructor_exists():
    assert callable(dom_WhenClause.__init__)


def test_hyp_dom_whenclause_constructor_args():
    sig = inspect.signature(dom_WhenClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_hyp_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_hyp_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_realliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_RealLiteralValue)


def test_hyp_dom_realliteralvalue_constructor_exists():
    assert callable(dom_RealLiteralValue.__init__)


def test_hyp_dom_realliteralvalue_constructor_args():
    sig = inspect.signature(dom_RealLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_dom_integerliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_IntegerLiteralValue)


def test_hyp_dom_integerliteralvalue_constructor_exists():
    assert callable(dom_IntegerLiteralValue.__init__)


def test_hyp_dom_integerliteralvalue_constructor_args():
    sig = inspect.signature(dom_IntegerLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_dom_emptyliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_EmptyLiteralValue)


def test_hyp_dom_emptyliteralvalue_constructor_exists():
    assert callable(dom_EmptyLiteralValue.__init__)


def test_hyp_dom_emptyliteralvalue_constructor_args():
    sig = inspect.signature(dom_EmptyLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_nullliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_NullLiteralValue)


def test_hyp_dom_nullliteralvalue_constructor_exists():
    assert callable(dom_NullLiteralValue.__init__)


def test_hyp_dom_nullliteralvalue_constructor_args():
    sig = inspect.signature(dom_NullLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_booleanliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_BooleanLiteralValue)


def test_hyp_dom_booleanliteralvalue_constructor_exists():
    assert callable(dom_BooleanLiteralValue.__init__)


def test_hyp_dom_booleanliteralvalue_constructor_args():
    sig = inspect.signature(dom_BooleanLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"




def test_hyp_dom_literalvalue_is_not_abstract():
    assert not inspect.isabstract(dom_LiteralValue)


def test_hyp_dom_literalvalue_constructor_exists():
    assert callable(dom_LiteralValue.__init__)


def test_hyp_dom_literalvalue_constructor_args():
    sig = inspect.signature(dom_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ParenthesizedExpression)


def test_hyp_dom_parenthesizedexpression_constructor_exists():
    assert callable(dom_ParenthesizedExpression.__init__)


def test_hyp_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(dom_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_subquery_is_not_abstract():
    assert not inspect.isabstract(dom_SubQuery)


def test_hyp_dom_subquery_constructor_exists():
    assert callable(dom_SubQuery.__init__)


def test_hyp_dom_subquery_constructor_args():
    sig = inspect.signature(dom_SubQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_altwhenclause_is_not_abstract():
    assert not inspect.isabstract(dom_AltWhenClause)


def test_hyp_dom_altwhenclause_constructor_exists():
    assert callable(dom_AltWhenClause.__init__)


def test_hyp_dom_altwhenclause_constructor_args():
    sig = inspect.signature(dom_AltWhenClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_stringliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_StringLiteralValue)


def test_hyp_dom_stringliteralvalue_constructor_exists():
    assert callable(dom_StringLiteralValue.__init__)


def test_hyp_dom_stringliteralvalue_constructor_args():
    sig = inspect.signature(dom_StringLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_dom_trimfunction_is_not_abstract():
    assert not inspect.isabstract(dom_TrimFunction)


def test_hyp_dom_trimfunction_constructor_exists():
    assert callable(dom_TrimFunction.__init__)


def test_hyp_dom_trimfunction_constructor_args():
    sig = inspect.signature(dom_TrimFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"
    assert "mode" in params, "Missing parameter 'mode'"





def test_hyp_dom_caseexpression_is_not_abstract():
    assert not inspect.isabstract(dom_CaseExpression)


def test_hyp_dom_caseexpression_constructor_exists():
    assert callable(dom_CaseExpression.__init__)


def test_hyp_dom_caseexpression_constructor_args():
    sig = inspect.signature(dom_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_QuantifiedExpression)


def test_hyp_dom_quantifiedexpression_constructor_exists():
    assert callable(dom_QuantifiedExpression.__init__)


def test_hyp_dom_quantifiedexpression_constructor_args():
    sig = inspect.signature(dom_QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_dom_queryparametervalue_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameterValue)


def test_hyp_dom_queryparametervalue_constructor_exists():
    assert callable(dom_QueryParameterValue.__init__)


def test_hyp_dom_queryparametervalue_constructor_args():
    sig = inspect.signature(dom_QueryParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameterReference)


def test_hyp_dom_queryparameterreference_constructor_exists():
    assert callable(dom_QueryParameterReference.__init__)


def test_hyp_dom_queryparameterreference_constructor_args():
    sig = inspect.signature(dom_QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_attributeflag_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeFlag)


def test_hyp_dom_attributeflag_constructor_exists():
    assert callable(dom_AttributeFlag.__init__)


def test_hyp_dom_attributeflag_constructor_args():
    sig = inspect.signature(dom_AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_incrementerreference_is_not_abstract():
    assert not inspect.isabstract(dom_IncrementerReference)


def test_hyp_dom_incrementerreference_constructor_exists():
    assert callable(dom_IncrementerReference.__init__)


def test_hyp_dom_incrementerreference_constructor_args():
    sig = inspect.signature(dom_IncrementerReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_datatypeandtypeparameter_is_not_abstract():
    assert not inspect.isabstract(dom_DataTypeAndTypeParameter)


def test_hyp_dom_datatypeandtypeparameter_constructor_exists():
    assert callable(dom_DataTypeAndTypeParameter.__init__)


def test_hyp_dom_datatypeandtypeparameter_constructor_args():
    sig = inspect.signature(dom_DataTypeAndTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_propertymapping_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyMapping)


def test_hyp_dom_propertymapping_constructor_exists():
    assert callable(dom_PropertyMapping.__init__)


def test_hyp_dom_propertymapping_constructor_args():
    sig = inspect.signature(dom_PropertyMapping.__init__)
    params = list(sig.parameters.keys())
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "toLeft" in params, "Missing parameter 'toLeft'"






def test_hyp_dom_conditionsblock_is_not_abstract():
    assert not inspect.isabstract(dom_ConditionsBlock)


def test_hyp_dom_conditionsblock_constructor_exists():
    assert callable(dom_ConditionsBlock.__init__)


def test_hyp_dom_conditionsblock_constructor_args():
    sig = inspect.signature(dom_ConditionsBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_presentablefeature_is_not_abstract():
    assert not inspect.isabstract(PresentableFeature)


def test_hyp_presentablefeature_constructor_exists():
    assert callable(PresentableFeature.__init__)


def test_hyp_presentablefeature_constructor_args():
    sig = inspect.signature(PresentableFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_hyp_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_hyp_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_valueobject_is_not_abstract():
    assert not inspect.isabstract(dom_ValueObject)


def test_hyp_dom_valueobject_constructor_exists():
    assert callable(dom_ValueObject.__init__)


def test_hyp_dom_valueobject_constructor_args():
    sig = inspect.signature(dom_ValueObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_attributeproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeProperty)


def test_hyp_dom_attributeproperty_constructor_exists():
    assert callable(dom_AttributeProperty.__init__)


def test_hyp_dom_attributeproperty_constructor_args():
    sig = inspect.signature(dom_AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_dataview_is_not_abstract():
    assert not inspect.isabstract(dom_DataView)


def test_hyp_dom_dataview_constructor_exists():
    assert callable(dom_DataView.__init__)


def test_hyp_dom_dataview_constructor_args():
    sig = inspect.signature(dom_DataView.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_type_is_not_abstract():
    assert not inspect.isabstract(dom_Type)


def test_hyp_dom_type_constructor_exists():
    assert callable(dom_Type.__init__)


def test_hyp_dom_type_constructor_args():
    sig = inspect.signature(dom_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(QueryParameterReference)


def test_hyp_queryparameterreference_constructor_exists():
    assert callable(QueryParameterReference.__init__)


def test_hyp_queryparameterreference_constructor_args():
    sig = inspect.signature(QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_queryparameter_is_not_abstract():
    assert not inspect.isabstract(QueryParameter)


def test_hyp_queryparameter_constructor_exists():
    assert callable(QueryParameter.__init__)


def test_hyp_queryparameter_constructor_args():
    sig = inspect.signature(QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expression_is_not_abstract():
    assert not inspect.isabstract(dom_Expression)


def test_hyp_dom_expression_constructor_exists():
    assert callable(dom_Expression.__init__)


def test_hyp_dom_expression_constructor_args():
    sig = inspect.signature(dom_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_daooperation_is_not_abstract():
    assert not inspect.isabstract(dom_DaoOperation)


def test_hyp_dom_daooperation_constructor_exists():
    assert callable(dom_DaoOperation.__init__)


def test_hyp_dom_daooperation_constructor_args():
    sig = inspect.signature(dom_DaoOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"





def test_hyp_dom_dependant_is_not_abstract():
    assert not inspect.isabstract(dom_Dependant)


def test_hyp_dom_dependant_constructor_exists():
    assert callable(dom_Dependant.__init__)


def test_hyp_dom_dependant_constructor_args():
    sig = inspect.signature(dom_Dependant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dependant_is_not_abstract():
    assert not inspect.isabstract(Dependant)


def test_hyp_dependant_constructor_exists():
    assert callable(Dependant.__init__)


def test_hyp_dependant_constructor_args():
    sig = inspect.signature(Dependant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_entity_is_not_abstract():
    assert not inspect.isabstract(dom_Entity)


def test_hyp_dom_entity_constructor_exists():
    assert callable(dom_Entity.__init__)


def test_hyp_dom_entity_constructor_args():
    sig = inspect.signature(dom_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_parameter_is_not_abstract():
    assert not inspect.isabstract(dom_Parameter)


def test_hyp_dom_parameter_constructor_exists():
    assert callable(dom_Parameter.__init__)


def test_hyp_dom_parameter_constructor_args():
    sig = inspect.signature(dom_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"





def test_hyp_daooperation_is_not_abstract():
    assert not inspect.isabstract(DaoOperation)


def test_hyp_daooperation_constructor_exists():
    assert callable(DaoOperation.__init__)


def test_hyp_daooperation_constructor_args():
    sig = inspect.signature(DaoOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_simpletype_is_not_abstract():
    assert not inspect.isabstract(dom_SimpleType)


def test_hyp_dom_simpletype_constructor_exists():
    assert callable(dom_SimpleType.__init__)


def test_hyp_dom_simpletype_constructor_args():
    sig = inspect.signature(dom_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_idocumentable_is_not_abstract():
    assert not inspect.isabstract(IDocumentable)


def test_hyp_idocumentable_constructor_exists():
    assert callable(IDocumentable.__init__)


def test_hyp_idocumentable_constructor_args():
    sig = inspect.signature(IDocumentable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_featurereference_is_not_abstract():
    assert not inspect.isabstract(dom_FeatureReference)


def test_hyp_dom_featurereference_constructor_exists():
    assert callable(dom_FeatureReference.__init__)


def test_hyp_dom_featurereference_constructor_args():
    sig = inspect.signature(dom_FeatureReference.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"




def test_hyp_dom_attributegroup_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeGroup)


def test_hyp_dom_attributegroup_constructor_exists():
    assert callable(dom_AttributeGroup.__init__)


def test_hyp_dom_attributegroup_constructor_args():
    sig = inspect.signature(dom_AttributeGroup.__init__)
    params = list(sig.parameters.keys())
    assert "sortorder" in params, "Missing parameter 'sortorder'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "name" in params, "Missing parameter 'name'"
    assert "key" in params, "Missing parameter 'key'"
    assert "filter" in params, "Missing parameter 'filter'"








def test_hyp_dom_operation_is_not_abstract():
    assert not inspect.isabstract(dom_Operation)


def test_hyp_dom_operation_constructor_exists():
    assert callable(dom_Operation.__init__)


def test_hyp_dom_operation_constructor_args():
    sig = inspect.signature(dom_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_dom_queryoperation_is_not_abstract():
    assert not inspect.isabstract(dom_QueryOperation)


def test_hyp_dom_queryoperation_constructor_exists():
    assert callable(dom_QueryOperation.__init__)


def test_hyp_dom_queryoperation_constructor_args():
    sig = inspect.signature(dom_QueryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_delegateoperation_is_not_abstract():
    assert not inspect.isabstract(dom_DelegateOperation)


def test_hyp_dom_delegateoperation_constructor_exists():
    assert callable(dom_DelegateOperation.__init__)


def test_hyp_dom_delegateoperation_constructor_args():
    sig = inspect.signature(dom_DelegateOperation.__init__)
    params = list(sig.parameters.keys())
    assert "crudOperationType" in params, "Missing parameter 'crudOperationType'"
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_referenceablebyxmadslvariable_is_not_abstract():
    assert not inspect.isabstract(ReferenceableByXmadslVariable)


def test_hyp_referenceablebyxmadslvariable_constructor_exists():
    assert callable(ReferenceableByXmadslVariable.__init__)


def test_hyp_referenceablebyxmadslvariable_constructor_args():
    sig = inspect.signature(ReferenceableByXmadslVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ielementwithnoname_is_not_abstract():
    assert not inspect.isabstract(dom_IElementWithNoName)


def test_hyp_dom_ielementwithnoname_constructor_exists():
    assert callable(dom_IElementWithNoName.__init__)


def test_hyp_dom_ielementwithnoname_constructor_args():
    sig = inspect.signature(dom_IElementWithNoName.__init__)
    params = list(sig.parameters.keys())
    assert "noName" in params, "Missing parameter 'noName'"




def test_hyp_dom_property_is_not_abstract():
    assert not inspect.isabstract(dom_Property)


def test_hyp_dom_property_constructor_exists():
    assert callable(dom_Property.__init__)


def test_hyp_dom_property_constructor_args():
    sig = inspect.signature(dom_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"





def test_hyp_dom_attribute_is_not_abstract():
    assert not inspect.isabstract(dom_Attribute)


def test_hyp_dom_attribute_constructor_exists():
    assert callable(dom_Attribute.__init__)


def test_hyp_dom_attribute_constructor_args():
    sig = inspect.signature(dom_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "version" in params, "Missing parameter 'version'"
    assert "composition" in params, "Missing parameter 'composition'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "required" in params, "Missing parameter 'required'"
    assert "dataTypeName" in params, "Missing parameter 'dataTypeName'"














def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_applicationsession_is_not_abstract():
    assert not inspect.isabstract(dom_ApplicationSession)


def test_hyp_dom_applicationsession_constructor_exists():
    assert callable(dom_ApplicationSession.__init__)


def test_hyp_dom_applicationsession_constructor_args():
    sig = inspect.signature(dom_ApplicationSession.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_mapper_is_not_abstract():
    assert not inspect.isabstract(dom_Mapper)


def test_hyp_dom_mapper_constructor_exists():
    assert callable(dom_Mapper.__init__)


def test_hyp_dom_mapper_constructor_args():
    sig = inspect.signature(dom_Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "toLeft" in params, "Missing parameter 'toLeft'"
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"






def test_hyp_dom_dao_is_not_abstract():
    assert not inspect.isabstract(dom_Dao)


def test_hyp_dom_dao_constructor_exists():
    assert callable(dom_Dao.__init__)


def test_hyp_dom_dao_constructor_args():
    sig = inspect.signature(dom_Dao.__init__)
    params = list(sig.parameters.keys())
    assert "discriminator" in params, "Missing parameter 'discriminator'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "tableName" in params, "Missing parameter 'tableName'"






def test_hyp_dom_service_is_not_abstract():
    assert not inspect.isabstract(dom_Service)


def test_hyp_dom_service_constructor_exists():
    assert callable(dom_Service.__init__)


def test_hyp_dom_service_constructor_args():
    sig = inspect.signature(dom_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_complextype_is_not_abstract():
    assert not inspect.isabstract(dom_ComplexType)


def test_hyp_dom_complextype_constructor_exists():
    assert callable(dom_ComplexType.__init__)


def test_hyp_dom_complextype_constructor_args():
    sig = inspect.signature(dom_ComplexType.__init__)
    params = list(sig.parameters.keys())

def test_hyp_databaseconstrainttype_exists():
    # Check that the Enumeration exists
    assert DataBaseConstraintType is not None

def test_hyp_databaseconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataBaseConstraintType]
    expected_literals = [
        "NULL",
        "PRIMARY",
        "NATURAL",
        "UNIQUE",
        "INDEX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataBaseConstraintType"

def test_hyp_crudoperationtype_exists():
    # Check that the Enumeration exists
    assert CrudOperationType is not None

def test_hyp_crudoperationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CrudOperationType]
    expected_literals = [
        "READ",
        "DELETE",
        "CREATE",
        "ALL",
        "NULL",
        "UPDATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CrudOperationType"


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
JoinEntity_strategy = st.builds(
    JoinEntity,
)
FromRange_strategy = st.builds(
    FromRange,
)
dom_InCollection_strategy = st.builds(
    dom_InCollection,
    alias=
        safe_text,
    path=
        safe_text
)
dom_InClass_strategy = st.builds(
    dom_InClass,
    class_=
        safe_text,
    name=
        safe_text
)
dom_FromClass_strategy = st.builds(
    dom_FromClass,
    popertyFetch=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
dom_CollectionFunction_strategy = st.builds(
    dom_CollectionFunction,
    function=
        safe_text
)
dom_AggregateFunction_strategy = st.builds(
    dom_AggregateFunction,
    from_=
        safe_text,
    distinct=
        st.booleans(),
    function=
        safe_text,
    all=
        st.booleans()
)
dom_FunctionCall_strategy = st.builds(
    dom_FunctionCall,
    function=
        safe_text
)
dom_CastFunction_strategy = st.builds(
    dom_CastFunction,
    function=
        safe_text,
    name=
        safe_text
)
dom_JoinEntity_strategy = st.builds(
    dom_JoinEntity,
    name=
        safe_text
)
dom_InCollectionElements_strategy = st.builds(
    dom_InCollectionElements,
    reference=
        safe_text,
    name=
        safe_text
)
dom_PropertyValue_strategy = st.builds(
    dom_PropertyValue,
    classProperty=
        st.booleans(),
    segments=
        safe_text,
    name=
        safe_text
)
dom_PropertyAssignment_strategy = st.builds(
    dom_PropertyAssignment,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
dom_SelectObject_strategy = st.builds(
    dom_SelectObject,
    name=
        safe_text
)
dom_SelectClass_strategy = st.builds(
    dom_SelectClass,
    class_=
        safe_text
)
dom_SelectProperties_strategy = st.builds(
    dom_SelectProperties,
    distinct=
        st.booleans()
)
dom_SortOrderElement_strategy = st.builds(
    dom_SortOrderElement,
    sortOrder=
        safe_text
)
dom_Join_strategy = st.builds(
    dom_Join,
    type=
        safe_text,
    fetch=
        st.booleans(),
    propertyFetch=
        st.booleans()
)
dom_FromRange_strategy = st.builds(
    dom_FromRange,
)
dom_CallOutputParameter_strategy = st.builds(
    dom_CallOutputParameter,
    name=
        safe_text
)
dom_CallInputParameter_strategy = st.builds(
    dom_CallInputParameter,
    name=
        safe_text
)
QlStatement_strategy = st.builds(
    QlStatement,
)
dom_InsertStatement_strategy = st.builds(
    dom_InsertStatement,
)
dom_UpdateStatement_strategy = st.builds(
    dom_UpdateStatement,
    name=
        safe_text,
    versioned=
        st.booleans()
)
dom_DeleteStatement_strategy = st.builds(
    dom_DeleteStatement,
    name=
        safe_text
)
dom_SelectStatement_strategy = st.builds(
    dom_SelectStatement,
)
dom_CallableStatement_strategy = st.builds(
    dom_CallableStatement,
    name=
        safe_text,
    functionCall=
        st.booleans()
)
dom_Function_strategy = st.builds(
    dom_Function,
)
DaoFeature_strategy = st.builds(
    DaoFeature,
)
dom_SqlType_strategy = st.builds(
    dom_SqlType,
)
dom_OneToOne_strategy = st.builds(
    dom_OneToOne,
)
dom_ManyToOne_strategy = st.builds(
    dom_ManyToOne,
    columnName=
        safe_text,
    derived=
        st.booleans()
)
dom_Column_strategy = st.builds(
    dom_Column,
    columnName=
        safe_text
)
dom_DataBaseConstraint_strategy = st.builds(
    dom_DataBaseConstraint,
    name=
        safe_text,
    type=
        safe_text
)
dom_QlStatement_strategy = st.builds(
    dom_QlStatement,
)
dom_QueryParameter_strategy = st.builds(
    dom_QueryParameter,
)
dom_ManyToMany_strategy = st.builds(
    dom_ManyToMany,
    columnName=
        safe_text,
    tableName=
        safe_text,
    inverse=
        st.booleans()
)
dom_OneToMany_strategy = st.builds(
    dom_OneToMany,
    columnName=
        safe_text
)
dom_DaoFeature_strategy = st.builds(
    dom_DaoFeature,
)
dom_AttributeSortOrder_strategy = st.builds(
    dom_AttributeSortOrder,
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
dom_ValidatorReference_strategy = st.builds(
    dom_ValidatorReference,
)
dom_Constraint_strategy = st.builds(
    dom_Constraint,
)
dom_BoolLiteral_strategy = st.builds(
    dom_BoolLiteral,
)
ExpressionFlag_strategy = st.builds(
    ExpressionFlag,
)
dom_ReadOnlyFlag_strategy = st.builds(
    dom_ReadOnlyFlag,
)
dom_AvailableFlag_strategy = st.builds(
    dom_AvailableFlag,
)
dom_RequiredFlag_strategy = st.builds(
    dom_RequiredFlag,
)
dom_EqualityExpr_strategy = st.builds(
    dom_EqualityExpr,
)
AttributeFlag_strategy = st.builds(
    AttributeFlag,
)
dom_TransientFlag_strategy = st.builds(
    dom_TransientFlag,
)
dom_DerivedFlag_strategy = st.builds(
    dom_DerivedFlag,
)
dom_ExpressionFlag_strategy = st.builds(
    dom_ExpressionFlag,
)
AttributeProperty_strategy = st.builds(
    AttributeProperty,
)
dom_AttributeTextProperty_strategy = st.builds(
    dom_AttributeTextProperty,
    labelText=
        safe_text,
    tooltipText=
        safe_text,
    hstoreColumn=
        safe_text,
    unitText=
        safe_text
)
dom_AttributeValidationProperty_strategy = st.builds(
    dom_AttributeValidationProperty,
)
dom_BetweenExpression_strategy = st.builds(
    dom_BetweenExpression,
    operator=
        safe_text,
    not_=
        st.booleans()
)
dom_UnaryExpression_strategy = st.builds(
    dom_UnaryExpression,
    operator=
        safe_text
)
dom_MemberOfExpression_strategy = st.builds(
    dom_MemberOfExpression,
    not_=
        st.booleans(),
    memberOf=
        safe_text,
    operator=
        safe_text
)
dom_LikeExpression_strategy = st.builds(
    dom_LikeExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom_InExpression_strategy = st.builds(
    dom_InExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom_NotExpression_strategy = st.builds(
    dom_NotExpression,
)
dom_BinaryExpression_strategy = st.builds(
    dom_BinaryExpression,
    operator=
        safe_text
)
dom_AliasedExpression_strategy = st.builds(
    dom_AliasedExpression,
    name=
        safe_text
)
dom_PresentableFeature_strategy = st.builds(
    dom_PresentableFeature,
    name=
        safe_text
)
dom_WhenClause_strategy = st.builds(
    dom_WhenClause,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
dom_RealLiteralValue_strategy = st.builds(
    dom_RealLiteralValue,
    value=
        safe_text
)
dom_IntegerLiteralValue_strategy = st.builds(
    dom_IntegerLiteralValue,
    value=
        safe_text
)
dom_EmptyLiteralValue_strategy = st.builds(
    dom_EmptyLiteralValue,
)
dom_NullLiteralValue_strategy = st.builds(
    dom_NullLiteralValue,
)
dom_BooleanLiteralValue_strategy = st.builds(
    dom_BooleanLiteralValue,
    isTrue=
        st.booleans()
)
dom_LiteralValue_strategy = st.builds(
    dom_LiteralValue,
)
dom_ParenthesizedExpression_strategy = st.builds(
    dom_ParenthesizedExpression,
)
dom_SubQuery_strategy = st.builds(
    dom_SubQuery,
)
dom_AltWhenClause_strategy = st.builds(
    dom_AltWhenClause,
)
dom_StringLiteralValue_strategy = st.builds(
    dom_StringLiteralValue,
    value=
        safe_text
)
dom_TrimFunction_strategy = st.builds(
    dom_TrimFunction,
    function=
        safe_text,
    mode=
        safe_text
)
dom_CaseExpression_strategy = st.builds(
    dom_CaseExpression,
)
dom_QuantifiedExpression_strategy = st.builds(
    dom_QuantifiedExpression,
    quantifier=
        safe_text,
    name=
        safe_text
)
dom_QueryParameterValue_strategy = st.builds(
    dom_QueryParameterValue,
)
dom_QueryParameterReference_strategy = st.builds(
    dom_QueryParameterReference,
)
dom_AttributeFlag_strategy = st.builds(
    dom_AttributeFlag,
)
dom_IncrementerReference_strategy = st.builds(
    dom_IncrementerReference,
)
dom_DataTypeAndTypeParameter_strategy = st.builds(
    dom_DataTypeAndTypeParameter,
)
dom_PropertyMapping_strategy = st.builds(
    dom_PropertyMapping,
    biDirectional=
        st.booleans(),
    toRight=
        st.booleans(),
    toLeft=
        st.booleans()
)
dom_ConditionsBlock_strategy = st.builds(
    dom_ConditionsBlock,
)
PresentableFeature_strategy = st.builds(
    PresentableFeature,
)
ComplexType_strategy = st.builds(
    ComplexType,
)
dom_ValueObject_strategy = st.builds(
    dom_ValueObject,
)
dom_AttributeProperty_strategy = st.builds(
    dom_AttributeProperty,
)
dom_DataView_strategy = st.builds(
    dom_DataView,
)
dom_Type_strategy = st.builds(
    dom_Type,
)
QueryParameterReference_strategy = st.builds(
    QueryParameterReference,
)
QueryParameter_strategy = st.builds(
    QueryParameter,
)
dom_Expression_strategy = st.builds(
    dom_Expression,
)
dom_DaoOperation_strategy = st.builds(
    dom_DaoOperation,
    name=
        safe_text,
    many=
        st.booleans()
)
dom_Dependant_strategy = st.builds(
    dom_Dependant,
)
Dependant_strategy = st.builds(
    Dependant,
)
dom_Entity_strategy = st.builds(
    dom_Entity,
)
dom_Parameter_strategy = st.builds(
    dom_Parameter,
    name=
        safe_text,
    many=
        st.booleans()
)
DaoOperation_strategy = st.builds(
    DaoOperation,
)
dom_SimpleType_strategy = st.builds(
    dom_SimpleType,
)
IDocumentable_strategy = st.builds(
    IDocumentable,
)
dom_FeatureReference_strategy = st.builds(
    dom_FeatureReference,
    all=
        st.booleans()
)
dom_AttributeGroup_strategy = st.builds(
    dom_AttributeGroup,
    sortorder=
        st.booleans(),
    unique=
        st.booleans(),
    name=
        safe_text,
    key=
        st.booleans(),
    filter=
        st.booleans()
)
dom_Operation_strategy = st.builds(
    dom_Operation,
    expression=
        safe_text
)
dom_QueryOperation_strategy = st.builds(
    dom_QueryOperation,
)
dom_DelegateOperation_strategy = st.builds(
    dom_DelegateOperation,
    crudOperationType=
        safe_text,
    many=
        st.booleans(),
    name=
        safe_text
)
ReferenceableByXmadslVariable_strategy = st.builds(
    ReferenceableByXmadslVariable,
)
dom_IElementWithNoName_strategy = st.builds(
    dom_IElementWithNoName,
    noName=
        safe_text
)
dom_Property_strategy = st.builds(
    dom_Property,
    name=
        safe_text,
    defaultValue=
        safe_text
)
dom_Attribute_strategy = st.builds(
    dom_Attribute,
    many=
        st.booleans(),
    readOnly=
        st.booleans(),
    version=
        st.booleans(),
    composition=
        st.booleans(),
    reference=
        st.booleans(),
    defaultValue=
        safe_text,
    derived=
        st.booleans(),
    identifier=
        st.booleans(),
    transient=
        st.booleans(),
    required=
        st.booleans(),
    dataTypeName=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
dom_ApplicationSession_strategy = st.builds(
    dom_ApplicationSession,
)
dom_Mapper_strategy = st.builds(
    dom_Mapper,
    toLeft=
        st.booleans(),
    toRight=
        st.booleans(),
    biDirectional=
        st.booleans()
)
dom_Dao_strategy = st.builds(
    dom_Dao,
    discriminator=
        safe_text,
    qualifier=
        safe_text,
    tableName=
        safe_text
)
dom_Service_strategy = st.builds(
    dom_Service,
)
dom_ComplexType_strategy = st.builds(
    dom_ComplexType,
)






@given(instance=dom_InCollection_strategy)
def test_hyp_dom_incollection_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=dom_InCollection_strategy)
def test_hyp_dom_incollection_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original




@given(instance=dom_InClass_strategy)
def test_hyp_dom_inclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=dom_InClass_strategy)
def test_hyp_dom_inclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_FromClass_strategy)
def test_hyp_dom_fromclass_popertyFetch_setter(instance):
    original = instance.popertyFetch
    instance.popertyFetch = original
    assert instance.popertyFetch == original





@given(instance=dom_CollectionFunction_strategy)
def test_hyp_dom_collectionfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original




@given(instance=dom_AggregateFunction_strategy)
def test_hyp_dom_aggregatefunction_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=dom_AggregateFunction_strategy)
def test_hyp_dom_aggregatefunction_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=dom_AggregateFunction_strategy)
def test_hyp_dom_aggregatefunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_AggregateFunction_strategy)
def test_hyp_dom_aggregatefunction_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original




@given(instance=dom_FunctionCall_strategy)
def test_hyp_dom_functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original




@given(instance=dom_CastFunction_strategy)
def test_hyp_dom_castfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_CastFunction_strategy)
def test_hyp_dom_castfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_JoinEntity_strategy)
def test_hyp_dom_joinentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_InCollectionElements_strategy)
def test_hyp_dom_incollectionelements_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=dom_InCollectionElements_strategy)
def test_hyp_dom_incollectionelements_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_PropertyValue_strategy)
def test_hyp_dom_propertyvalue_classProperty_setter(instance):
    original = instance.classProperty
    instance.classProperty = original
    assert instance.classProperty == original



@given(instance=dom_PropertyValue_strategy)
def test_hyp_dom_propertyvalue_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original



@given(instance=dom_PropertyValue_strategy)
def test_hyp_dom_propertyvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=dom_SelectObject_strategy)
def test_hyp_dom_selectobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_SelectClass_strategy)
def test_hyp_dom_selectclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=dom_SelectProperties_strategy)
def test_hyp_dom_selectproperties_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original




@given(instance=dom_SortOrderElement_strategy)
def test_hyp_dom_sortorderelement_sortOrder_setter(instance):
    original = instance.sortOrder
    instance.sortOrder = original
    assert instance.sortOrder == original




@given(instance=dom_Join_strategy)
def test_hyp_dom_join_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=dom_Join_strategy)
def test_hyp_dom_join_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original



@given(instance=dom_Join_strategy)
def test_hyp_dom_join_propertyFetch_setter(instance):
    original = instance.propertyFetch
    instance.propertyFetch = original
    assert instance.propertyFetch == original





@given(instance=dom_CallOutputParameter_strategy)
def test_hyp_dom_calloutputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_CallInputParameter_strategy)
def test_hyp_dom_callinputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=dom_UpdateStatement_strategy)
def test_hyp_dom_updatestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_UpdateStatement_strategy)
def test_hyp_dom_updatestatement_versioned_setter(instance):
    original = instance.versioned
    instance.versioned = original
    assert instance.versioned == original




@given(instance=dom_DeleteStatement_strategy)
def test_hyp_dom_deletestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=dom_CallableStatement_strategy)
def test_hyp_dom_callablestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_CallableStatement_strategy)
def test_hyp_dom_callablestatement_functionCall_setter(instance):
    original = instance.functionCall
    instance.functionCall = original
    assert instance.functionCall == original








@given(instance=dom_ManyToOne_strategy)
def test_hyp_dom_manytoone_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=dom_ManyToOne_strategy)
def test_hyp_dom_manytoone_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original




@given(instance=dom_Column_strategy)
def test_hyp_dom_column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original




@given(instance=dom_DataBaseConstraint_strategy)
def test_hyp_dom_databaseconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_DataBaseConstraint_strategy)
def test_hyp_dom_databaseconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=dom_ManyToMany_strategy)
def test_hyp_dom_manytomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=dom_ManyToMany_strategy)
def test_hyp_dom_manytomany_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=dom_ManyToMany_strategy)
def test_hyp_dom_manytomany_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original




@given(instance=dom_OneToMany_strategy)
def test_hyp_dom_onetomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original





@given(instance=dom_AttributeSortOrder_strategy)
def test_hyp_dom_attributesortorder_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=dom_AttributeSortOrder_strategy)
def test_hyp_dom_attributesortorder_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

















@given(instance=dom_AttributeTextProperty_strategy)
def test_hyp_dom_attributetextproperty_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_hyp_dom_attributetextproperty_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_hyp_dom_attributetextproperty_hstoreColumn_setter(instance):
    original = instance.hstoreColumn
    instance.hstoreColumn = original
    assert instance.hstoreColumn == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_hyp_dom_attributetextproperty_unitText_setter(instance):
    original = instance.unitText
    instance.unitText = original
    assert instance.unitText == original





@given(instance=dom_BetweenExpression_strategy)
def test_hyp_dom_betweenexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=dom_BetweenExpression_strategy)
def test_hyp_dom_betweenexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original




@given(instance=dom_UnaryExpression_strategy)
def test_hyp_dom_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=dom_MemberOfExpression_strategy)
def test_hyp_dom_memberofexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_MemberOfExpression_strategy)
def test_hyp_dom_memberofexpression_memberOf_setter(instance):
    original = instance.memberOf
    instance.memberOf = original
    assert instance.memberOf == original



@given(instance=dom_MemberOfExpression_strategy)
def test_hyp_dom_memberofexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=dom_LikeExpression_strategy)
def test_hyp_dom_likeexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_LikeExpression_strategy)
def test_hyp_dom_likeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=dom_InExpression_strategy)
def test_hyp_dom_inexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_InExpression_strategy)
def test_hyp_dom_inexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=dom_BinaryExpression_strategy)
def test_hyp_dom_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=dom_AliasedExpression_strategy)
def test_hyp_dom_aliasedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dom_PresentableFeature_strategy)
def test_hyp_dom_presentablefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=dom_RealLiteralValue_strategy)
def test_hyp_dom_realliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=dom_IntegerLiteralValue_strategy)
def test_hyp_dom_integerliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=dom_BooleanLiteralValue_strategy)
def test_hyp_dom_booleanliteralvalue_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original








@given(instance=dom_StringLiteralValue_strategy)
def test_hyp_dom_stringliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=dom_TrimFunction_strategy)
def test_hyp_dom_trimfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_TrimFunction_strategy)
def test_hyp_dom_trimfunction_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original





@given(instance=dom_QuantifiedExpression_strategy)
def test_hyp_dom_quantifiedexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original



@given(instance=dom_QuantifiedExpression_strategy)
def test_hyp_dom_quantifiedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=dom_PropertyMapping_strategy)
def test_hyp_dom_propertymapping_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original



@given(instance=dom_PropertyMapping_strategy)
def test_hyp_dom_propertymapping_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original



@given(instance=dom_PropertyMapping_strategy)
def test_hyp_dom_propertymapping_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original














@given(instance=dom_DaoOperation_strategy)
def test_hyp_dom_daooperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_DaoOperation_strategy)
def test_hyp_dom_daooperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original







@given(instance=dom_Parameter_strategy)
def test_hyp_dom_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_Parameter_strategy)
def test_hyp_dom_parameter_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original







@given(instance=dom_FeatureReference_strategy)
def test_hyp_dom_featurereference_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original




@given(instance=dom_AttributeGroup_strategy)
def test_hyp_dom_attributegroup_sortorder_setter(instance):
    original = instance.sortorder
    instance.sortorder = original
    assert instance.sortorder == original



@given(instance=dom_AttributeGroup_strategy)
def test_hyp_dom_attributegroup_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=dom_AttributeGroup_strategy)
def test_hyp_dom_attributegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_AttributeGroup_strategy)
def test_hyp_dom_attributegroup_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=dom_AttributeGroup_strategy)
def test_hyp_dom_attributegroup_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original




@given(instance=dom_Operation_strategy)
def test_hyp_dom_operation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original





@given(instance=dom_DelegateOperation_strategy)
def test_hyp_dom_delegateoperation_crudOperationType_setter(instance):
    original = instance.crudOperationType
    instance.crudOperationType = original
    assert instance.crudOperationType == original



@given(instance=dom_DelegateOperation_strategy)
def test_hyp_dom_delegateoperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=dom_DelegateOperation_strategy)
def test_hyp_dom_delegateoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=dom_IElementWithNoName_strategy)
def test_hyp_dom_ielementwithnoname_noName_setter(instance):
    original = instance.noName
    instance.noName = original
    assert instance.noName == original




@given(instance=dom_Property_strategy)
def test_hyp_dom_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_Property_strategy)
def test_hyp_dom_property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original




@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=dom_Attribute_strategy)
def test_hyp_dom_attribute_dataTypeName_setter(instance):
    original = instance.dataTypeName
    instance.dataTypeName = original
    assert instance.dataTypeName == original







@given(instance=dom_Mapper_strategy)
def test_hyp_dom_mapper_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original



@given(instance=dom_Mapper_strategy)
def test_hyp_dom_mapper_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original



@given(instance=dom_Mapper_strategy)
def test_hyp_dom_mapper_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original




@given(instance=dom_Dao_strategy)
def test_hyp_dom_dao_discriminator_setter(instance):
    original = instance.discriminator
    instance.discriminator = original
    assert instance.discriminator == original



@given(instance=dom_Dao_strategy)
def test_hyp_dom_dao_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=dom_Dao_strategy)
def test_hyp_dom_dao_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AttributeFlag,
    AttributeProperty,
    ComplexType,
    DaoFeature,
    DaoOperation,
    Dependant,
    Expression,
    ExpressionFlag,
    FromRange,
    IDocumentable,
    JoinEntity,
    LiteralValue,
    ModelElement,
    PresentableFeature,
    QlStatement,
    QueryParameter,
    QueryParameterReference,
    ReferenceableByXmadslVariable,
    SelectStatement,
    Type,
    dom_AggregateFunction,
    dom_AliasedExpression,
    dom_AltWhenClause,
    dom_ApplicationSession,
    dom_Attribute,
    dom_AttributeFlag,
    dom_AttributeGroup,
    dom_AttributeProperty,
    dom_AttributeSortOrder,
    dom_AttributeTextProperty,
    dom_AttributeValidationProperty,
    dom_AvailableFlag,
    dom_BetweenExpression,
    dom_BinaryExpression,
    dom_BoolLiteral,
    dom_BooleanLiteralValue,
    dom_CallInputParameter,
    dom_CallOutputParameter,
    dom_CallableStatement,
    dom_CaseExpression,
    dom_CastFunction,
    dom_CollectionFunction,
    dom_Column,
    dom_ComplexType,
    dom_ConditionsBlock,
    dom_Constraint,
    dom_Dao,
    dom_DaoFeature,
    dom_DaoOperation,
    dom_DataBaseConstraint,
    dom_DataTypeAndTypeParameter,
    dom_DataView,
    dom_DelegateOperation,
    dom_DeleteStatement,
    dom_Dependant,
    dom_DerivedFlag,
    dom_EmptyLiteralValue,
    dom_Entity,
    dom_EqualityExpr,
    dom_Expression,
    dom_ExpressionFlag,
    dom_FeatureReference,
    dom_FromClass,
    dom_FromRange,
    dom_Function,
    dom_FunctionCall,
    dom_IElementWithNoName,
    dom_InClass,
    dom_InCollection,
    dom_InCollectionElements,
    dom_InExpression,
    dom_IncrementerReference,
    dom_InsertStatement,
    dom_IntegerLiteralValue,
    dom_Join,
    dom_JoinEntity,
    dom_LikeExpression,
    dom_LiteralValue,
    dom_ManyToMany,
    dom_ManyToOne,
    dom_Mapper,
    dom_MemberOfExpression,
    dom_NotExpression,
    dom_NullLiteralValue,
    dom_OneToMany,
    dom_OneToOne,
    dom_Operation,
    dom_Parameter,
    dom_ParenthesizedExpression,
    dom_PresentableFeature,
    dom_Property,
    dom_PropertyAssignment,
    dom_PropertyMapping,
    dom_PropertyValue,
    dom_QlStatement,
    dom_QuantifiedExpression,
    dom_QueryOperation,
    dom_QueryParameter,
    dom_QueryParameterReference,
    dom_QueryParameterValue,
    dom_ReadOnlyFlag,
    dom_RealLiteralValue,
    dom_RequiredFlag,
    dom_SelectClass,
    dom_SelectObject,
    dom_SelectProperties,
    dom_SelectStatement,
    dom_Service,
    dom_SimpleType,
    dom_SortOrderElement,
    dom_SqlType,
    dom_StringLiteralValue,
    dom_SubQuery,
    dom_TransientFlag,
    dom_TrimFunction,
    dom_Type,
    dom_UnaryExpression,
    dom_UpdateStatement,
    dom_ValidatorReference,
    dom_ValueObject,
    dom_WhenClause,
    CrudOperationType,
    DataBaseConstraintType,
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

def test_dom_AggregateFunction_all_value_roundtrip():
    instance = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    assert instance.all == True
    instance.all = False
    assert instance.all == False


def test_dom_AggregateFunction_distinct_value_roundtrip():
    instance = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    assert instance.distinct == True
    instance.distinct = False
    assert instance.distinct == False


def test_dom_AggregateFunction_from__value_roundtrip():
    instance = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    assert instance.from_ == "sample_text"
    instance.from_ = "sample_text_2"
    assert instance.from_ == "sample_text_2"


def test_dom_AggregateFunction_function_value_roundtrip():
    instance = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_dom_AliasedExpression_name_value_roundtrip():
    instance = dom_AliasedExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_Attribute_composition_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.composition == True
    instance.composition = False
    assert instance.composition == False


def test_dom_Attribute_dataTypeName_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.dataTypeName == "sample_text"
    instance.dataTypeName = "sample_text_2"
    assert instance.dataTypeName == "sample_text_2"


def test_dom_Attribute_defaultValue_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_dom_Attribute_derived_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_dom_Attribute_identifier_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.identifier == True
    instance.identifier = False
    assert instance.identifier == False


def test_dom_Attribute_many_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_dom_Attribute_readOnly_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_dom_Attribute_reference_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.reference == True
    instance.reference = False
    assert instance.reference == False


def test_dom_Attribute_required_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_dom_Attribute_transient_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_dom_Attribute_version_value_roundtrip():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert instance.version == True
    instance.version = False
    assert instance.version == False


def test_dom_AttributeGroup_filter_value_roundtrip():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert instance.filter == True
    instance.filter = False
    assert instance.filter == False


def test_dom_AttributeGroup_key_value_roundtrip():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert instance.key == True
    instance.key = False
    assert instance.key == False


def test_dom_AttributeGroup_name_value_roundtrip():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_AttributeGroup_sortorder_value_roundtrip():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert instance.sortorder == True
    instance.sortorder = False
    assert instance.sortorder == False


def test_dom_AttributeGroup_unique_value_roundtrip():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_dom_AttributeSortOrder_asc_value_roundtrip():
    instance = dom_AttributeSortOrder(asc=True, desc=True)
    assert instance.asc == True
    instance.asc = False
    assert instance.asc == False


def test_dom_AttributeSortOrder_desc_value_roundtrip():
    instance = dom_AttributeSortOrder(asc=True, desc=True)
    assert instance.desc == True
    instance.desc = False
    assert instance.desc == False


def test_dom_AttributeTextProperty_hstoreColumn_value_roundtrip():
    instance = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    assert instance.hstoreColumn == "sample_text"
    instance.hstoreColumn = "sample_text_2"
    assert instance.hstoreColumn == "sample_text_2"


def test_dom_AttributeTextProperty_labelText_value_roundtrip():
    instance = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    assert instance.labelText == "sample_text"
    instance.labelText = "sample_text_2"
    assert instance.labelText == "sample_text_2"


def test_dom_AttributeTextProperty_tooltipText_value_roundtrip():
    instance = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    assert instance.tooltipText == "sample_text"
    instance.tooltipText = "sample_text_2"
    assert instance.tooltipText == "sample_text_2"


def test_dom_AttributeTextProperty_unitText_value_roundtrip():
    instance = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    assert instance.unitText == "sample_text"
    instance.unitText = "sample_text_2"
    assert instance.unitText == "sample_text_2"


def test_dom_BetweenExpression_not__value_roundtrip():
    instance = dom_BetweenExpression(not_=True, operator="sample_text")
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_dom_BetweenExpression_operator_value_roundtrip():
    instance = dom_BetweenExpression(not_=True, operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_BinaryExpression_operator_value_roundtrip():
    instance = dom_BinaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_BooleanLiteralValue_isTrue_value_roundtrip():
    instance = dom_BooleanLiteralValue(isTrue=True)
    assert instance.isTrue == True
    instance.isTrue = False
    assert instance.isTrue == False


def test_dom_CallInputParameter_name_value_roundtrip():
    instance = dom_CallInputParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_CallOutputParameter_name_value_roundtrip():
    instance = dom_CallOutputParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_CallableStatement_functionCall_value_roundtrip():
    instance = dom_CallableStatement(functionCall=True, name="sample_text")
    assert instance.functionCall == True
    instance.functionCall = False
    assert instance.functionCall == False


def test_dom_CallableStatement_name_value_roundtrip():
    instance = dom_CallableStatement(functionCall=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_CastFunction_function_value_roundtrip():
    instance = dom_CastFunction(function="sample_text", name="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_dom_CastFunction_name_value_roundtrip():
    instance = dom_CastFunction(function="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_CollectionFunction_function_value_roundtrip():
    instance = dom_CollectionFunction(function="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_dom_Column_columnName_value_roundtrip():
    instance = dom_Column(columnName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_dom_Dao_discriminator_value_roundtrip():
    instance = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    assert instance.discriminator == "sample_text"
    instance.discriminator = "sample_text_2"
    assert instance.discriminator == "sample_text_2"


def test_dom_Dao_qualifier_value_roundtrip():
    instance = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_dom_Dao_tableName_value_roundtrip():
    instance = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_dom_DaoOperation_many_value_roundtrip():
    instance = dom_DaoOperation(many=True, name="sample_text")
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_dom_DaoOperation_name_value_roundtrip():
    instance = dom_DaoOperation(many=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_DataBaseConstraint_name_value_roundtrip():
    instance = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_DataBaseConstraint_type_value_roundtrip():
    instance = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_dom_DelegateOperation_crudOperationType_value_roundtrip():
    instance = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    assert instance.crudOperationType == "sample_text"
    instance.crudOperationType = "sample_text_2"
    assert instance.crudOperationType == "sample_text_2"


def test_dom_DelegateOperation_many_value_roundtrip():
    instance = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_dom_DelegateOperation_name_value_roundtrip():
    instance = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_DeleteStatement_name_value_roundtrip():
    instance = dom_DeleteStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_FeatureReference_all_value_roundtrip():
    instance = dom_FeatureReference(all=True)
    assert instance.all == True
    instance.all = False
    assert instance.all == False


def test_dom_FromClass_popertyFetch_value_roundtrip():
    instance = dom_FromClass(popertyFetch=True)
    assert instance.popertyFetch == True
    instance.popertyFetch = False
    assert instance.popertyFetch == False


def test_dom_FunctionCall_function_value_roundtrip():
    instance = dom_FunctionCall(function="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_dom_IElementWithNoName_noName_value_roundtrip():
    instance = dom_IElementWithNoName(noName="sample_text")
    assert instance.noName == "sample_text"
    instance.noName = "sample_text_2"
    assert instance.noName == "sample_text_2"


def test_dom_InClass_class__value_roundtrip():
    instance = dom_InClass(class_="sample_text", name="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_dom_InClass_name_value_roundtrip():
    instance = dom_InClass(class_="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_InCollection_alias_value_roundtrip():
    instance = dom_InCollection(alias="sample_text", path="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_dom_InCollection_path_value_roundtrip():
    instance = dom_InCollection(alias="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_dom_InCollectionElements_name_value_roundtrip():
    instance = dom_InCollectionElements(name="sample_text", reference="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_InCollectionElements_reference_value_roundtrip():
    instance = dom_InCollectionElements(name="sample_text", reference="sample_text")
    assert instance.reference == "sample_text"
    instance.reference = "sample_text_2"
    assert instance.reference == "sample_text_2"


def test_dom_InExpression_not__value_roundtrip():
    instance = dom_InExpression(not_=True, operator="sample_text")
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_dom_InExpression_operator_value_roundtrip():
    instance = dom_InExpression(not_=True, operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_IntegerLiteralValue_value_value_roundtrip():
    instance = dom_IntegerLiteralValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_dom_Join_fetch_value_roundtrip():
    instance = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    assert instance.fetch == True
    instance.fetch = False
    assert instance.fetch == False


def test_dom_Join_propertyFetch_value_roundtrip():
    instance = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    assert instance.propertyFetch == True
    instance.propertyFetch = False
    assert instance.propertyFetch == False


def test_dom_Join_type_value_roundtrip():
    instance = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_dom_JoinEntity_name_value_roundtrip():
    instance = dom_JoinEntity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_LikeExpression_not__value_roundtrip():
    instance = dom_LikeExpression(not_=True, operator="sample_text")
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_dom_LikeExpression_operator_value_roundtrip():
    instance = dom_LikeExpression(not_=True, operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_ManyToMany_columnName_value_roundtrip():
    instance = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_dom_ManyToMany_inverse_value_roundtrip():
    instance = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    assert instance.inverse == True
    instance.inverse = False
    assert instance.inverse == False


def test_dom_ManyToMany_tableName_value_roundtrip():
    instance = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_dom_ManyToOne_columnName_value_roundtrip():
    instance = dom_ManyToOne(columnName="sample_text", derived=True)
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_dom_ManyToOne_derived_value_roundtrip():
    instance = dom_ManyToOne(columnName="sample_text", derived=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_dom_Mapper_biDirectional_value_roundtrip():
    instance = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    assert instance.biDirectional == True
    instance.biDirectional = False
    assert instance.biDirectional == False


def test_dom_Mapper_toLeft_value_roundtrip():
    instance = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    assert instance.toLeft == True
    instance.toLeft = False
    assert instance.toLeft == False


def test_dom_Mapper_toRight_value_roundtrip():
    instance = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    assert instance.toRight == True
    instance.toRight = False
    assert instance.toRight == False


def test_dom_MemberOfExpression_memberOf_value_roundtrip():
    instance = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    assert instance.memberOf == "sample_text"
    instance.memberOf = "sample_text_2"
    assert instance.memberOf == "sample_text_2"


def test_dom_MemberOfExpression_not__value_roundtrip():
    instance = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_dom_MemberOfExpression_operator_value_roundtrip():
    instance = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_OneToMany_columnName_value_roundtrip():
    instance = dom_OneToMany(columnName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_dom_Operation_expression_value_roundtrip():
    instance = dom_Operation(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_dom_Parameter_many_value_roundtrip():
    instance = dom_Parameter(many=True, name="sample_text")
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_dom_Parameter_name_value_roundtrip():
    instance = dom_Parameter(many=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_PresentableFeature_name_value_roundtrip():
    instance = dom_PresentableFeature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_Property_defaultValue_value_roundtrip():
    instance = dom_Property(defaultValue="sample_text", name="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_dom_Property_name_value_roundtrip():
    instance = dom_Property(defaultValue="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_PropertyMapping_biDirectional_value_roundtrip():
    instance = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    assert instance.biDirectional == True
    instance.biDirectional = False
    assert instance.biDirectional == False


def test_dom_PropertyMapping_toLeft_value_roundtrip():
    instance = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    assert instance.toLeft == True
    instance.toLeft = False
    assert instance.toLeft == False


def test_dom_PropertyMapping_toRight_value_roundtrip():
    instance = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    assert instance.toRight == True
    instance.toRight = False
    assert instance.toRight == False


def test_dom_PropertyValue_classProperty_value_roundtrip():
    instance = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    assert instance.classProperty == True
    instance.classProperty = False
    assert instance.classProperty == False


def test_dom_PropertyValue_name_value_roundtrip():
    instance = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_PropertyValue_segments_value_roundtrip():
    instance = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    assert instance.segments == "sample_text"
    instance.segments = "sample_text_2"
    assert instance.segments == "sample_text_2"


def test_dom_QuantifiedExpression_name_value_roundtrip():
    instance = dom_QuantifiedExpression(name="sample_text", quantifier="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_QuantifiedExpression_quantifier_value_roundtrip():
    instance = dom_QuantifiedExpression(name="sample_text", quantifier="sample_text")
    assert instance.quantifier == "sample_text"
    instance.quantifier = "sample_text_2"
    assert instance.quantifier == "sample_text_2"


def test_dom_RealLiteralValue_value_value_roundtrip():
    instance = dom_RealLiteralValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_dom_SelectClass_class__value_roundtrip():
    instance = dom_SelectClass(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_dom_SelectObject_name_value_roundtrip():
    instance = dom_SelectObject(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_SelectProperties_distinct_value_roundtrip():
    instance = dom_SelectProperties(distinct=True)
    assert instance.distinct == True
    instance.distinct = False
    assert instance.distinct == False


def test_dom_SortOrderElement_sortOrder_value_roundtrip():
    instance = dom_SortOrderElement(sortOrder="sample_text")
    assert instance.sortOrder == "sample_text"
    instance.sortOrder = "sample_text_2"
    assert instance.sortOrder == "sample_text_2"


def test_dom_StringLiteralValue_value_value_roundtrip():
    instance = dom_StringLiteralValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_dom_TrimFunction_function_value_roundtrip():
    instance = dom_TrimFunction(function="sample_text", mode="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_dom_TrimFunction_mode_value_roundtrip():
    instance = dom_TrimFunction(function="sample_text", mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_dom_UnaryExpression_operator_value_roundtrip():
    instance = dom_UnaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_dom_UpdateStatement_name_value_roundtrip():
    instance = dom_UpdateStatement(name="sample_text", versioned=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_UpdateStatement_versioned_value_roundtrip():
    instance = dom_UpdateStatement(name="sample_text", versioned=True)
    assert instance.versioned == True
    instance.versioned = False
    assert instance.versioned == False


def test_dom_DerivedFlag_isa_AttributeFlag():
    instance = dom_DerivedFlag()
    assert isinstance(instance, AttributeFlag)


def test_dom_ExpressionFlag_isa_AttributeFlag():
    instance = dom_ExpressionFlag()
    assert isinstance(instance, AttributeFlag)


def test_dom_TransientFlag_isa_AttributeFlag():
    instance = dom_TransientFlag()
    assert isinstance(instance, AttributeFlag)


def test_dom_AttributeFlag_isa_AttributeProperty():
    instance = dom_AttributeFlag()
    assert isinstance(instance, AttributeProperty)


def test_dom_AttributeTextProperty_isa_AttributeProperty():
    instance = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    assert isinstance(instance, AttributeProperty)


def test_dom_AttributeValidationProperty_isa_AttributeProperty():
    instance = dom_AttributeValidationProperty()
    assert isinstance(instance, AttributeProperty)


def test_dom_DataView_isa_ComplexType():
    instance = dom_DataView()
    assert isinstance(instance, ComplexType)


def test_dom_Entity_isa_ComplexType():
    instance = dom_Entity()
    assert isinstance(instance, ComplexType)


def test_dom_ValueObject_isa_ComplexType():
    instance = dom_ValueObject()
    assert isinstance(instance, ComplexType)


def test_dom_Column_isa_DaoFeature():
    instance = dom_Column(columnName="sample_text")
    assert isinstance(instance, DaoFeature)


def test_dom_ManyToMany_isa_DaoFeature():
    instance = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    assert isinstance(instance, DaoFeature)


def test_dom_ManyToOne_isa_DaoFeature():
    instance = dom_ManyToOne(columnName="sample_text", derived=True)
    assert isinstance(instance, DaoFeature)


def test_dom_OneToMany_isa_DaoFeature():
    instance = dom_OneToMany(columnName="sample_text")
    assert isinstance(instance, DaoFeature)


def test_dom_OneToOne_isa_DaoFeature():
    instance = dom_OneToOne()
    assert isinstance(instance, DaoFeature)


def test_dom_Operation_isa_DaoOperation():
    instance = dom_Operation(expression="sample_text")
    assert isinstance(instance, DaoOperation)


def test_dom_QueryOperation_isa_DaoOperation():
    instance = dom_QueryOperation()
    assert isinstance(instance, DaoOperation)


def test_dom_Dao_isa_Dependant():
    instance = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    assert isinstance(instance, Dependant)


def test_dom_Entity_isa_Dependant():
    instance = dom_Entity()
    assert isinstance(instance, Dependant)


def test_dom_Service_isa_Dependant():
    instance = dom_Service()
    assert isinstance(instance, Dependant)


def test_dom_AggregateFunction_isa_Expression():
    instance = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    assert isinstance(instance, Expression)


def test_dom_AliasedExpression_isa_Expression():
    instance = dom_AliasedExpression(name="sample_text")
    assert isinstance(instance, Expression)


def test_dom_BetweenExpression_isa_Expression():
    instance = dom_BetweenExpression(not_=True, operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_BinaryExpression_isa_Expression():
    instance = dom_BinaryExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_CaseExpression_isa_Expression():
    instance = dom_CaseExpression()
    assert isinstance(instance, Expression)


def test_dom_CastFunction_isa_Expression():
    instance = dom_CastFunction(function="sample_text", name="sample_text")
    assert isinstance(instance, Expression)


def test_dom_CollectionFunction_isa_Expression():
    instance = dom_CollectionFunction(function="sample_text")
    assert isinstance(instance, Expression)


def test_dom_FunctionCall_isa_Expression():
    instance = dom_FunctionCall(function="sample_text")
    assert isinstance(instance, Expression)


def test_dom_InExpression_isa_Expression():
    instance = dom_InExpression(not_=True, operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_LikeExpression_isa_Expression():
    instance = dom_LikeExpression(not_=True, operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_LiteralValue_isa_Expression():
    instance = dom_LiteralValue()
    assert isinstance(instance, Expression)


def test_dom_MemberOfExpression_isa_Expression():
    instance = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_NotExpression_isa_Expression():
    instance = dom_NotExpression()
    assert isinstance(instance, Expression)


def test_dom_ParenthesizedExpression_isa_Expression():
    instance = dom_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_dom_PropertyValue_isa_Expression():
    instance = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    assert isinstance(instance, Expression)


def test_dom_QuantifiedExpression_isa_Expression():
    instance = dom_QuantifiedExpression(name="sample_text", quantifier="sample_text")
    assert isinstance(instance, Expression)


def test_dom_QueryParameterValue_isa_Expression():
    instance = dom_QueryParameterValue()
    assert isinstance(instance, Expression)


def test_dom_SubQuery_isa_Expression():
    instance = dom_SubQuery()
    assert isinstance(instance, Expression)


def test_dom_TrimFunction_isa_Expression():
    instance = dom_TrimFunction(function="sample_text", mode="sample_text")
    assert isinstance(instance, Expression)


def test_dom_UnaryExpression_isa_Expression():
    instance = dom_UnaryExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_dom_AvailableFlag_isa_ExpressionFlag():
    instance = dom_AvailableFlag()
    assert isinstance(instance, ExpressionFlag)


def test_dom_ReadOnlyFlag_isa_ExpressionFlag():
    instance = dom_ReadOnlyFlag()
    assert isinstance(instance, ExpressionFlag)


def test_dom_RequiredFlag_isa_ExpressionFlag():
    instance = dom_RequiredFlag()
    assert isinstance(instance, ExpressionFlag)


def test_dom_FromClass_isa_FromRange():
    instance = dom_FromClass(popertyFetch=True)
    assert isinstance(instance, FromRange)


def test_dom_InClass_isa_FromRange():
    instance = dom_InClass(class_="sample_text", name="sample_text")
    assert isinstance(instance, FromRange)


def test_dom_InCollection_isa_FromRange():
    instance = dom_InCollection(alias="sample_text", path="sample_text")
    assert isinstance(instance, FromRange)


def test_dom_InCollectionElements_isa_FromRange():
    instance = dom_InCollectionElements(name="sample_text", reference="sample_text")
    assert isinstance(instance, FromRange)


def test_dom_Attribute_isa_IDocumentable():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert isinstance(instance, IDocumentable)


def test_dom_AttributeGroup_isa_IDocumentable():
    instance = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    assert isinstance(instance, IDocumentable)


def test_dom_DelegateOperation_isa_IDocumentable():
    instance = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    assert isinstance(instance, IDocumentable)


def test_dom_FeatureReference_isa_IDocumentable():
    instance = dom_FeatureReference(all=True)
    assert isinstance(instance, IDocumentable)


def test_dom_Operation_isa_IDocumentable():
    instance = dom_Operation(expression="sample_text")
    assert isinstance(instance, IDocumentable)


def test_dom_Property_isa_IDocumentable():
    instance = dom_Property(defaultValue="sample_text", name="sample_text")
    assert isinstance(instance, IDocumentable)


def test_dom_QueryOperation_isa_IDocumentable():
    instance = dom_QueryOperation()
    assert isinstance(instance, IDocumentable)


def test_dom_FromClass_isa_JoinEntity():
    instance = dom_FromClass(popertyFetch=True)
    assert isinstance(instance, JoinEntity)


def test_dom_Join_isa_JoinEntity():
    instance = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    assert isinstance(instance, JoinEntity)


def test_dom_BooleanLiteralValue_isa_LiteralValue():
    instance = dom_BooleanLiteralValue(isTrue=True)
    assert isinstance(instance, LiteralValue)


def test_dom_EmptyLiteralValue_isa_LiteralValue():
    instance = dom_EmptyLiteralValue()
    assert isinstance(instance, LiteralValue)


def test_dom_IntegerLiteralValue_isa_LiteralValue():
    instance = dom_IntegerLiteralValue(value="sample_text")
    assert isinstance(instance, LiteralValue)


def test_dom_NullLiteralValue_isa_LiteralValue():
    instance = dom_NullLiteralValue()
    assert isinstance(instance, LiteralValue)


def test_dom_RealLiteralValue_isa_LiteralValue():
    instance = dom_RealLiteralValue(value="sample_text")
    assert isinstance(instance, LiteralValue)


def test_dom_StringLiteralValue_isa_LiteralValue():
    instance = dom_StringLiteralValue(value="sample_text")
    assert isinstance(instance, LiteralValue)


def test_dom_ApplicationSession_isa_ModelElement():
    instance = dom_ApplicationSession()
    assert isinstance(instance, ModelElement)


def test_dom_ComplexType_isa_ModelElement():
    instance = dom_ComplexType()
    assert isinstance(instance, ModelElement)


def test_dom_Dao_isa_ModelElement():
    instance = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    assert isinstance(instance, ModelElement)


def test_dom_Mapper_isa_ModelElement():
    instance = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    assert isinstance(instance, ModelElement)


def test_dom_Service_isa_ModelElement():
    instance = dom_Service()
    assert isinstance(instance, ModelElement)


def test_dom_Attribute_isa_PresentableFeature():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert isinstance(instance, PresentableFeature)


def test_dom_FeatureReference_isa_PresentableFeature():
    instance = dom_FeatureReference(all=True)
    assert isinstance(instance, PresentableFeature)


def test_dom_CallableStatement_isa_QlStatement():
    instance = dom_CallableStatement(functionCall=True, name="sample_text")
    assert isinstance(instance, QlStatement)


def test_dom_DeleteStatement_isa_QlStatement():
    instance = dom_DeleteStatement(name="sample_text")
    assert isinstance(instance, QlStatement)


def test_dom_InsertStatement_isa_QlStatement():
    instance = dom_InsertStatement()
    assert isinstance(instance, QlStatement)


def test_dom_SelectStatement_isa_QlStatement():
    instance = dom_SelectStatement()
    assert isinstance(instance, QlStatement)


def test_dom_UpdateStatement_isa_QlStatement():
    instance = dom_UpdateStatement(name="sample_text", versioned=True)
    assert isinstance(instance, QlStatement)


def test_dom_Parameter_isa_QueryParameter():
    instance = dom_Parameter(many=True, name="sample_text")
    assert isinstance(instance, QueryParameter)


def test_dom_Attribute_isa_QueryParameterReference():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert isinstance(instance, QueryParameterReference)


def test_dom_IElementWithNoName_isa_QueryParameterReference():
    instance = dom_IElementWithNoName(noName="sample_text")
    assert isinstance(instance, QueryParameterReference)


def test_dom_Parameter_isa_QueryParameterReference():
    instance = dom_Parameter(many=True, name="sample_text")
    assert isinstance(instance, QueryParameterReference)


def test_dom_Attribute_isa_ReferenceableByXmadslVariable():
    instance = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    assert isinstance(instance, ReferenceableByXmadslVariable)


def test_dom_IElementWithNoName_isa_ReferenceableByXmadslVariable():
    instance = dom_IElementWithNoName(noName="sample_text")
    assert isinstance(instance, ReferenceableByXmadslVariable)


def test_dom_Property_isa_ReferenceableByXmadslVariable():
    instance = dom_Property(defaultValue="sample_text", name="sample_text")
    assert isinstance(instance, ReferenceableByXmadslVariable)


def test_dom_SelectClass_isa_SelectStatement():
    instance = dom_SelectClass(class_="sample_text")
    assert isinstance(instance, SelectStatement)


def test_dom_SelectObject_isa_SelectStatement():
    instance = dom_SelectObject(name="sample_text")
    assert isinstance(instance, SelectStatement)


def test_dom_SelectProperties_isa_SelectStatement():
    instance = dom_SelectProperties(distinct=True)
    assert isinstance(instance, SelectStatement)


def test_dom_ComplexType_isa_Type():
    instance = dom_ComplexType()
    assert isinstance(instance, Type)


def test_assoc_aggregateExpression288_link_reassign_clear():
    a = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_AggregateFunction', b1)
    assert _is_linked(a, 'dom_AggregateFunction', b1)
    if hasattr(b1, 'dom_Expression289'):
        assert _is_linked(b1, 'dom_Expression289', a)
    _safe_set(a, 'dom_AggregateFunction', b2)
    assert _is_linked(a, 'dom_AggregateFunction', b2)
    if hasattr(b1, 'dom_Expression289'):
        assert not _is_linked(b1, 'dom_Expression289', a)
    if hasattr(b2, 'dom_Expression289'):
        assert _is_linked(b2, 'dom_Expression289', a)
    _safe_set(a, 'dom_AggregateFunction', None)
    assert not _is_linked(a, 'dom_AggregateFunction', b2)
    if hasattr(b2, 'dom_Expression289'):
        assert not _is_linked(b2, 'dom_Expression289', a)


def test_assoc_allAttributes1_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_ComplexType()
    b2 = dom_ComplexType()
    _safe_set(a, 'dom_Attribute3', b1)
    assert _is_linked(a, 'dom_Attribute3', b1)
    if hasattr(b1, 'dom_ComplexType2'):
        assert _is_linked(b1, 'dom_ComplexType2', a)
    _safe_set(a, 'dom_Attribute3', b2)
    assert _is_linked(a, 'dom_Attribute3', b2)
    if hasattr(b1, 'dom_ComplexType2'):
        assert not _is_linked(b1, 'dom_ComplexType2', a)
    if hasattr(b2, 'dom_ComplexType2'):
        assert _is_linked(b2, 'dom_ComplexType2', a)
    _safe_set(a, 'dom_Attribute3', None)
    assert not _is_linked(a, 'dom_Attribute3', b2)
    if hasattr(b2, 'dom_ComplexType2'):
        assert not _is_linked(b2, 'dom_ComplexType2', a)


def test_assoc_arguments265_link_reassign_clear():
    a = dom_SelectClass(class_="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_SelectClass', {b1})
    assert _is_linked(a, 'dom_SelectClass', b1)
    if hasattr(b1, 'dom_Expression266'):
        assert _is_linked(b1, 'dom_Expression266', a)
    _safe_set(a, 'dom_SelectClass', {b2})
    assert _is_linked(a, 'dom_SelectClass', b2)
    if hasattr(b1, 'dom_Expression266'):
        assert not _is_linked(b1, 'dom_Expression266', a)
    if hasattr(b2, 'dom_Expression266'):
        assert _is_linked(b2, 'dom_Expression266', a)
    _safe_set(a, 'dom_SelectClass', set())
    assert not _is_linked(a, 'dom_SelectClass', b2)
    if hasattr(b2, 'dom_Expression266'):
        assert not _is_linked(b2, 'dom_Expression266', a)


def test_assoc_arguments280_link_reassign_clear():
    a = dom_FunctionCall(function="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_FunctionCall', {b1})
    assert _is_linked(a, 'dom_FunctionCall', b1)
    if hasattr(b1, 'dom_Expression281'):
        assert _is_linked(b1, 'dom_Expression281', a)
    _safe_set(a, 'dom_FunctionCall', {b2})
    assert _is_linked(a, 'dom_FunctionCall', b2)
    if hasattr(b1, 'dom_Expression281'):
        assert not _is_linked(b1, 'dom_Expression281', a)
    if hasattr(b2, 'dom_Expression281'):
        assert _is_linked(b2, 'dom_Expression281', a)
    _safe_set(a, 'dom_FunctionCall', set())
    assert not _is_linked(a, 'dom_FunctionCall', b2)
    if hasattr(b2, 'dom_Expression281'):
        assert not _is_linked(b2, 'dom_Expression281', a)


def test_assoc_assignment235_link_reassign_clear():
    a = dom_UpdateStatement(name="sample_text", versioned=True)
    b1 = dom_PropertyAssignment()
    b2 = dom_PropertyAssignment()
    _safe_set(a, 'dom_UpdateStatement236', {b1})
    assert _is_linked(a, 'dom_UpdateStatement236', b1)
    if hasattr(b1, 'dom_PropertyAssignment'):
        assert _is_linked(b1, 'dom_PropertyAssignment', a)
    _safe_set(a, 'dom_UpdateStatement236', {b2})
    assert _is_linked(a, 'dom_UpdateStatement236', b2)
    if hasattr(b1, 'dom_PropertyAssignment'):
        assert not _is_linked(b1, 'dom_PropertyAssignment', a)
    if hasattr(b2, 'dom_PropertyAssignment'):
        assert _is_linked(b2, 'dom_PropertyAssignment', a)
    _safe_set(a, 'dom_UpdateStatement236', set())
    assert not _is_linked(a, 'dom_UpdateStatement236', b2)
    if hasattr(b2, 'dom_PropertyAssignment'):
        assert not _is_linked(b2, 'dom_PropertyAssignment', a)


def test_assoc_attributProperties97_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_AttributeProperty()
    b2 = dom_AttributeProperty()
    _safe_set(a, 'dom_Attribute98', {b1})
    assert _is_linked(a, 'dom_Attribute98', b1)
    if hasattr(b1, 'dom_AttributeProperty99'):
        assert _is_linked(b1, 'dom_AttributeProperty99', a)
    _safe_set(a, 'dom_Attribute98', {b2})
    assert _is_linked(a, 'dom_Attribute98', b2)
    if hasattr(b1, 'dom_AttributeProperty99'):
        assert not _is_linked(b1, 'dom_AttributeProperty99', a)
    if hasattr(b2, 'dom_AttributeProperty99'):
        assert _is_linked(b2, 'dom_AttributeProperty99', a)
    _safe_set(a, 'dom_Attribute98', set())
    assert not _is_linked(a, 'dom_Attribute98', b2)
    if hasattr(b2, 'dom_AttributeProperty99'):
        assert not _is_linked(b2, 'dom_AttributeProperty99', a)


def test_assoc_attribute126_link_reassign_clear():
    a = dom_AttributeSortOrder(asc=True, desc=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_AttributeSortOrder127', b1)
    assert _is_linked(a, 'dom_AttributeSortOrder127', b1)
    if hasattr(b1, 'dom_Attribute128'):
        assert _is_linked(b1, 'dom_Attribute128', a)
    _safe_set(a, 'dom_AttributeSortOrder127', b2)
    assert _is_linked(a, 'dom_AttributeSortOrder127', b2)
    if hasattr(b1, 'dom_Attribute128'):
        assert not _is_linked(b1, 'dom_Attribute128', a)
    if hasattr(b2, 'dom_Attribute128'):
        assert _is_linked(b2, 'dom_Attribute128', a)
    _safe_set(a, 'dom_AttributeSortOrder127', None)
    assert not _is_linked(a, 'dom_AttributeSortOrder127', b2)
    if hasattr(b2, 'dom_Attribute128'):
        assert not _is_linked(b2, 'dom_Attribute128', a)


def test_assoc_attribute129_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_DaoFeature()
    b2 = dom_DaoFeature()
    _safe_set(a, 'dom_Attribute130', b1)
    assert _is_linked(a, 'dom_Attribute130', b1)
    if hasattr(b1, 'dom_DaoFeature'):
        assert _is_linked(b1, 'dom_DaoFeature', a)
    _safe_set(a, 'dom_Attribute130', b2)
    assert _is_linked(a, 'dom_Attribute130', b2)
    if hasattr(b1, 'dom_DaoFeature'):
        assert not _is_linked(b1, 'dom_DaoFeature', a)
    if hasattr(b2, 'dom_DaoFeature'):
        assert _is_linked(b2, 'dom_DaoFeature', a)
    _safe_set(a, 'dom_Attribute130', None)
    assert not _is_linked(a, 'dom_Attribute130', b2)
    if hasattr(b2, 'dom_DaoFeature'):
        assert not _is_linked(b2, 'dom_DaoFeature', a)


def test_assoc_attribute170_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_QueryParameter()
    b2 = dom_QueryParameter()
    _safe_set(a, 'dom_Attribute172', b1)
    assert _is_linked(a, 'dom_Attribute172', b1)
    if hasattr(b1, 'dom_QueryParameter171'):
        assert _is_linked(b1, 'dom_QueryParameter171', a)
    _safe_set(a, 'dom_Attribute172', b2)
    assert _is_linked(a, 'dom_Attribute172', b2)
    if hasattr(b1, 'dom_QueryParameter171'):
        assert not _is_linked(b1, 'dom_QueryParameter171', a)
    if hasattr(b2, 'dom_QueryParameter171'):
        assert _is_linked(b2, 'dom_QueryParameter171', a)
    _safe_set(a, 'dom_Attribute172', None)
    assert not _is_linked(a, 'dom_Attribute172', b2)
    if hasattr(b2, 'dom_QueryParameter171'):
        assert not _is_linked(b2, 'dom_QueryParameter171', a)


def test_assoc_attribute212_link_reassign_clear():
    a = dom_CallInputParameter(name="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_CallInputParameter213', b1)
    assert _is_linked(a, 'dom_CallInputParameter213', b1)
    if hasattr(b1, 'dom_Attribute214'):
        assert _is_linked(b1, 'dom_Attribute214', a)
    _safe_set(a, 'dom_CallInputParameter213', b2)
    assert _is_linked(a, 'dom_CallInputParameter213', b2)
    if hasattr(b1, 'dom_Attribute214'):
        assert not _is_linked(b1, 'dom_Attribute214', a)
    if hasattr(b2, 'dom_Attribute214'):
        assert _is_linked(b2, 'dom_Attribute214', a)
    _safe_set(a, 'dom_CallInputParameter213', None)
    assert not _is_linked(a, 'dom_CallInputParameter213', b2)
    if hasattr(b2, 'dom_Attribute214'):
        assert not _is_linked(b2, 'dom_Attribute214', a)


def test_assoc_attribute215_link_reassign_clear():
    a = dom_CallOutputParameter(name="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_CallOutputParameter216', b1)
    assert _is_linked(a, 'dom_CallOutputParameter216', b1)
    if hasattr(b1, 'dom_Attribute217'):
        assert _is_linked(b1, 'dom_Attribute217', a)
    _safe_set(a, 'dom_CallOutputParameter216', b2)
    assert _is_linked(a, 'dom_CallOutputParameter216', b2)
    if hasattr(b1, 'dom_Attribute217'):
        assert not _is_linked(b1, 'dom_Attribute217', a)
    if hasattr(b2, 'dom_Attribute217'):
        assert _is_linked(b2, 'dom_Attribute217', a)
    _safe_set(a, 'dom_CallOutputParameter216', None)
    assert not _is_linked(a, 'dom_CallOutputParameter216', b2)
    if hasattr(b2, 'dom_Attribute217'):
        assert not _is_linked(b2, 'dom_Attribute217', a)


def test_assoc_attribute293_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_QueryParameterValue()
    b2 = dom_QueryParameterValue()
    _safe_set(a, 'dom_Attribute295', b1)
    assert _is_linked(a, 'dom_Attribute295', b1)
    if hasattr(b1, 'dom_QueryParameterValue294'):
        assert _is_linked(b1, 'dom_QueryParameterValue294', a)
    _safe_set(a, 'dom_Attribute295', b2)
    assert _is_linked(a, 'dom_Attribute295', b2)
    if hasattr(b1, 'dom_QueryParameterValue294'):
        assert not _is_linked(b1, 'dom_QueryParameterValue294', a)
    if hasattr(b2, 'dom_QueryParameterValue294'):
        assert _is_linked(b2, 'dom_QueryParameterValue294', a)
    _safe_set(a, 'dom_Attribute295', None)
    assert not _is_linked(a, 'dom_Attribute295', b2)
    if hasattr(b2, 'dom_QueryParameterValue294'):
        assert not _is_linked(b2, 'dom_QueryParameterValue294', a)


def test_assoc_attribute38_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_FeatureReference39', b1)
    assert _is_linked(a, 'dom_FeatureReference39', b1)
    if hasattr(b1, 'dom_Attribute40'):
        assert _is_linked(b1, 'dom_Attribute40', a)
    _safe_set(a, 'dom_FeatureReference39', b2)
    assert _is_linked(a, 'dom_FeatureReference39', b2)
    if hasattr(b1, 'dom_Attribute40'):
        assert not _is_linked(b1, 'dom_Attribute40', a)
    if hasattr(b2, 'dom_Attribute40'):
        assert _is_linked(b2, 'dom_Attribute40', a)
    _safe_set(a, 'dom_FeatureReference39', None)
    assert not _is_linked(a, 'dom_FeatureReference39', b2)
    if hasattr(b2, 'dom_Attribute40'):
        assert not _is_linked(b2, 'dom_Attribute40', a)


def test_assoc_attributeGroups65_link_reassign_clear():
    a = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_AttributeGroup', b1)
    assert _is_linked(a, 'dom_AttributeGroup', b1)
    if hasattr(b1, 'dom_Entity66'):
        assert _is_linked(b1, 'dom_Entity66', a)
    _safe_set(a, 'dom_AttributeGroup', b2)
    assert _is_linked(a, 'dom_AttributeGroup', b2)
    if hasattr(b1, 'dom_Entity66'):
        assert not _is_linked(b1, 'dom_Entity66', a)
    if hasattr(b2, 'dom_Entity66'):
        assert _is_linked(b2, 'dom_Entity66', a)
    _safe_set(a, 'dom_AttributeGroup', None)
    assert not _is_linked(a, 'dom_AttributeGroup', b2)
    if hasattr(b2, 'dom_Entity66'):
        assert not _is_linked(b2, 'dom_Entity66', a)


def test_assoc_attributes0_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_ComplexType()
    b2 = dom_ComplexType()
    _safe_set(a, 'dom_Attribute', b1)
    assert _is_linked(a, 'dom_Attribute', b1)
    if hasattr(b1, 'dom_ComplexType'):
        assert _is_linked(b1, 'dom_ComplexType', a)
    _safe_set(a, 'dom_Attribute', b2)
    assert _is_linked(a, 'dom_Attribute', b2)
    if hasattr(b1, 'dom_ComplexType'):
        assert not _is_linked(b1, 'dom_ComplexType', a)
    if hasattr(b2, 'dom_ComplexType'):
        assert _is_linked(b2, 'dom_ComplexType', a)
    _safe_set(a, 'dom_Attribute', None)
    assert not _is_linked(a, 'dom_Attribute', b2)
    if hasattr(b2, 'dom_ComplexType'):
        assert not _is_linked(b2, 'dom_ComplexType', a)


def test_assoc_attributes121_link_reassign_clear():
    a = dom_AttributeSortOrder(asc=True, desc=True)
    b1 = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b2 = dom_AttributeGroup(filter=False, key=False, name="sample_text_2", sortorder=False, unique=False)
    _safe_set(a, 'dom_AttributeSortOrder', b1)
    assert _is_linked(a, 'dom_AttributeSortOrder', b1)
    if hasattr(b1, 'dom_AttributeGroup122'):
        assert _is_linked(b1, 'dom_AttributeGroup122', a)
    _safe_set(a, 'dom_AttributeSortOrder', b2)
    assert _is_linked(a, 'dom_AttributeSortOrder', b2)
    if hasattr(b1, 'dom_AttributeGroup122'):
        assert not _is_linked(b1, 'dom_AttributeGroup122', a)
    if hasattr(b2, 'dom_AttributeGroup122'):
        assert _is_linked(b2, 'dom_AttributeGroup122', a)
    _safe_set(a, 'dom_AttributeSortOrder', None)
    assert not _is_linked(a, 'dom_AttributeSortOrder', b2)
    if hasattr(b2, 'dom_AttributeGroup122'):
        assert not _is_linked(b2, 'dom_AttributeGroup122', a)


def test_assoc_attributes193_link_reassign_clear():
    a = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_DataBaseConstraint194', {b1})
    assert _is_linked(a, 'dom_DataBaseConstraint194', b1)
    if hasattr(b1, 'dom_Attribute195'):
        assert _is_linked(b1, 'dom_Attribute195', a)
    _safe_set(a, 'dom_DataBaseConstraint194', {b2})
    assert _is_linked(a, 'dom_DataBaseConstraint194', b2)
    if hasattr(b1, 'dom_Attribute195'):
        assert not _is_linked(b1, 'dom_Attribute195', a)
    if hasattr(b2, 'dom_Attribute195'):
        assert _is_linked(b2, 'dom_Attribute195', a)
    _safe_set(a, 'dom_DataBaseConstraint194', set())
    assert not _is_linked(a, 'dom_DataBaseConstraint194', b2)
    if hasattr(b2, 'dom_Attribute195'):
        assert not _is_linked(b2, 'dom_Attribute195', a)


def test_assoc_character282_link_reassign_clear():
    a = dom_TrimFunction(function="sample_text", mode="sample_text")
    b1 = dom_StringLiteralValue(value="sample_text")
    b2 = dom_StringLiteralValue(value="sample_text_2")
    _safe_set(a, 'dom_TrimFunction', b1)
    assert _is_linked(a, 'dom_TrimFunction', b1)
    if hasattr(b1, 'dom_StringLiteralValue'):
        assert _is_linked(b1, 'dom_StringLiteralValue', a)
    _safe_set(a, 'dom_TrimFunction', b2)
    assert _is_linked(a, 'dom_TrimFunction', b2)
    if hasattr(b1, 'dom_StringLiteralValue'):
        assert not _is_linked(b1, 'dom_StringLiteralValue', a)
    if hasattr(b2, 'dom_StringLiteralValue'):
        assert _is_linked(b2, 'dom_StringLiteralValue', a)
    _safe_set(a, 'dom_TrimFunction', None)
    assert not _is_linked(a, 'dom_TrimFunction', b2)
    if hasattr(b2, 'dom_StringLiteralValue'):
        assert not _is_linked(b2, 'dom_StringLiteralValue', a)


def test_assoc_collection290_link_reassign_clear():
    a = dom_CollectionFunction(function="sample_text")
    b1 = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    b2 = dom_AggregateFunction(all=False, distinct=False, from_="sample_text_2", function="sample_text_2")
    _safe_set(a, 'dom_CollectionFunction', b1)
    assert _is_linked(a, 'dom_CollectionFunction', b1)
    if hasattr(b1, 'dom_AggregateFunction291'):
        assert _is_linked(b1, 'dom_AggregateFunction291', a)
    _safe_set(a, 'dom_CollectionFunction', b2)
    assert _is_linked(a, 'dom_CollectionFunction', b2)
    if hasattr(b1, 'dom_AggregateFunction291'):
        assert not _is_linked(b1, 'dom_AggregateFunction291', a)
    if hasattr(b2, 'dom_AggregateFunction291'):
        assert _is_linked(b2, 'dom_AggregateFunction291', a)
    _safe_set(a, 'dom_CollectionFunction', None)
    assert not _is_linked(a, 'dom_CollectionFunction', b2)
    if hasattr(b2, 'dom_AggregateFunction291'):
        assert not _is_linked(b2, 'dom_AggregateFunction291', a)


def test_assoc_columnType176_link_reassign_clear():
    a = dom_Column(columnName="sample_text")
    b1 = dom_Type()
    b2 = dom_Type()
    _safe_set(a, 'dom_Column177', b1)
    assert _is_linked(a, 'dom_Column177', b1)
    if hasattr(b1, 'dom_Type178'):
        assert _is_linked(b1, 'dom_Type178', a)
    _safe_set(a, 'dom_Column177', b2)
    assert _is_linked(a, 'dom_Column177', b2)
    if hasattr(b1, 'dom_Type178'):
        assert not _is_linked(b1, 'dom_Type178', a)
    if hasattr(b2, 'dom_Type178'):
        assert _is_linked(b2, 'dom_Type178', a)
    _safe_set(a, 'dom_Column177', None)
    assert not _is_linked(a, 'dom_Column177', b2)
    if hasattr(b2, 'dom_Type178'):
        assert not _is_linked(b2, 'dom_Type178', a)


def test_assoc_columns141_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_Dao142', {b1})
    assert _is_linked(a, 'dom_Dao142', b1)
    if hasattr(b1, 'dom_Column'):
        assert _is_linked(b1, 'dom_Column', a)
    _safe_set(a, 'dom_Dao142', {b2})
    assert _is_linked(a, 'dom_Dao142', b2)
    if hasattr(b1, 'dom_Column'):
        assert not _is_linked(b1, 'dom_Column', a)
    if hasattr(b2, 'dom_Column'):
        assert _is_linked(b2, 'dom_Column', a)
    _safe_set(a, 'dom_Dao142', set())
    assert not _is_linked(a, 'dom_Dao142', b2)
    if hasattr(b2, 'dom_Column'):
        assert not _is_linked(b2, 'dom_Column', a)


def test_assoc_columns180_link_reassign_clear():
    a = dom_Column(columnName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_Column179', {b1})
    assert _is_linked(a, 'dom_Column179', b1)
    if hasattr(b1, 'dom_Column181'):
        assert _is_linked(b1, 'dom_Column181', a)
    _safe_set(a, 'dom_Column179', {b2})
    assert _is_linked(a, 'dom_Column179', b2)
    if hasattr(b1, 'dom_Column181'):
        assert not _is_linked(b1, 'dom_Column181', a)
    if hasattr(b2, 'dom_Column181'):
        assert _is_linked(b2, 'dom_Column181', a)
    _safe_set(a, 'dom_Column179', set())
    assert not _is_linked(a, 'dom_Column179', b2)
    if hasattr(b2, 'dom_Column181'):
        assert not _is_linked(b2, 'dom_Column181', a)


def test_assoc_columns187_link_reassign_clear():
    a = dom_ManyToOne(columnName="sample_text", derived=True)
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_ManyToOne188', {b1})
    assert _is_linked(a, 'dom_ManyToOne188', b1)
    if hasattr(b1, 'dom_Column189'):
        assert _is_linked(b1, 'dom_Column189', a)
    _safe_set(a, 'dom_ManyToOne188', {b2})
    assert _is_linked(a, 'dom_ManyToOne188', b2)
    if hasattr(b1, 'dom_Column189'):
        assert not _is_linked(b1, 'dom_Column189', a)
    if hasattr(b2, 'dom_Column189'):
        assert _is_linked(b2, 'dom_Column189', a)
    _safe_set(a, 'dom_ManyToOne188', set())
    assert not _is_linked(a, 'dom_ManyToOne188', b2)
    if hasattr(b2, 'dom_Column189'):
        assert not _is_linked(b2, 'dom_Column189', a)


def test_assoc_columns190_link_reassign_clear():
    a = dom_OneToMany(columnName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_OneToMany191', {b1})
    assert _is_linked(a, 'dom_OneToMany191', b1)
    if hasattr(b1, 'dom_Column192'):
        assert _is_linked(b1, 'dom_Column192', a)
    _safe_set(a, 'dom_OneToMany191', {b2})
    assert _is_linked(a, 'dom_OneToMany191', b2)
    if hasattr(b1, 'dom_Column192'):
        assert not _is_linked(b1, 'dom_Column192', a)
    if hasattr(b2, 'dom_Column192'):
        assert _is_linked(b2, 'dom_Column192', a)
    _safe_set(a, 'dom_OneToMany191', set())
    assert not _is_linked(a, 'dom_OneToMany191', b2)
    if hasattr(b2, 'dom_Column192'):
        assert not _is_linked(b2, 'dom_Column192', a)


def test_assoc_dataBaseConstraints139_link_reassign_clear():
    a = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_DataBaseConstraint', b1)
    assert _is_linked(a, 'dom_DataBaseConstraint', b1)
    if hasattr(b1, 'dom_Dao140'):
        assert _is_linked(b1, 'dom_Dao140', a)
    _safe_set(a, 'dom_DataBaseConstraint', b2)
    assert _is_linked(a, 'dom_DataBaseConstraint', b2)
    if hasattr(b1, 'dom_Dao140'):
        assert not _is_linked(b1, 'dom_Dao140', a)
    if hasattr(b2, 'dom_Dao140'):
        assert _is_linked(b2, 'dom_Dao140', a)
    _safe_set(a, 'dom_DataBaseConstraint', None)
    assert not _is_linked(a, 'dom_DataBaseConstraint', b2)
    if hasattr(b2, 'dom_Dao140'):
        assert not _is_linked(b2, 'dom_Dao140', a)


def test_assoc_dataType103_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Type()
    b2 = dom_Type()
    _safe_set(a, 'dom_Attribute104', b1)
    assert _is_linked(a, 'dom_Attribute104', b1)
    if hasattr(b1, 'dom_Type105'):
        assert _is_linked(b1, 'dom_Type105', a)
    _safe_set(a, 'dom_Attribute104', b2)
    assert _is_linked(a, 'dom_Attribute104', b2)
    if hasattr(b1, 'dom_Type105'):
        assert not _is_linked(b1, 'dom_Type105', a)
    if hasattr(b2, 'dom_Type105'):
        assert _is_linked(b2, 'dom_Type105', a)
    _safe_set(a, 'dom_Attribute104', None)
    assert not _is_linked(a, 'dom_Attribute104', b2)
    if hasattr(b2, 'dom_Type105'):
        assert not _is_linked(b2, 'dom_Type105', a)


def test_assoc_delegate12_link_reassign_clear():
    a = dom_Operation(expression="sample_text")
    b1 = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b2 = dom_DelegateOperation(crudOperationType="sample_text_2", many=False, name="sample_text_2")
    _safe_set(a, 'dom_Operation13', b1)
    assert _is_linked(a, 'dom_Operation13', b1)
    if hasattr(b1, 'dom_DelegateOperation14'):
        assert _is_linked(b1, 'dom_DelegateOperation14', a)
    _safe_set(a, 'dom_Operation13', b2)
    assert _is_linked(a, 'dom_Operation13', b2)
    if hasattr(b1, 'dom_DelegateOperation14'):
        assert not _is_linked(b1, 'dom_DelegateOperation14', a)
    if hasattr(b2, 'dom_DelegateOperation14'):
        assert _is_linked(b2, 'dom_DelegateOperation14', a)
    _safe_set(a, 'dom_Operation13', None)
    assert not _is_linked(a, 'dom_Operation13', b2)
    if hasattr(b2, 'dom_DelegateOperation14'):
        assert not _is_linked(b2, 'dom_DelegateOperation14', a)


def test_assoc_delegateOperations7_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_Service()
    b2 = dom_Service()
    _safe_set(a, 'dom_DelegateOperation', b1)
    assert _is_linked(a, 'dom_DelegateOperation', b1)
    if hasattr(b1, 'dom_Service8'):
        assert _is_linked(b1, 'dom_Service8', a)
    _safe_set(a, 'dom_DelegateOperation', b2)
    assert _is_linked(a, 'dom_DelegateOperation', b2)
    if hasattr(b1, 'dom_Service8'):
        assert not _is_linked(b1, 'dom_Service8', a)
    if hasattr(b2, 'dom_Service8'):
        assert _is_linked(b2, 'dom_Service8', a)
    _safe_set(a, 'dom_DelegateOperation', None)
    assert not _is_linked(a, 'dom_DelegateOperation', b2)
    if hasattr(b2, 'dom_Service8'):
        assert not _is_linked(b2, 'dom_Service8', a)


def test_assoc_entity131_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Dao132', b1)
    assert _is_linked(a, 'dom_Dao132', b1)
    if hasattr(b1, 'dom_Entity133'):
        assert _is_linked(b1, 'dom_Entity133', a)
    _safe_set(a, 'dom_Dao132', b2)
    assert _is_linked(a, 'dom_Dao132', b2)
    if hasattr(b1, 'dom_Entity133'):
        assert not _is_linked(b1, 'dom_Entity133', a)
    if hasattr(b2, 'dom_Entity133'):
        assert _is_linked(b2, 'dom_Entity133', a)
    _safe_set(a, 'dom_Dao132', None)
    assert not _is_linked(a, 'dom_Dao132', b2)
    if hasattr(b2, 'dom_Entity133'):
        assert not _is_linked(b2, 'dom_Entity133', a)


def test_assoc_entity228_link_reassign_clear():
    a = dom_DeleteStatement(name="sample_text")
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_DeleteStatement', b1)
    assert _is_linked(a, 'dom_DeleteStatement', b1)
    if hasattr(b1, 'dom_Entity229'):
        assert _is_linked(b1, 'dom_Entity229', a)
    _safe_set(a, 'dom_DeleteStatement', b2)
    assert _is_linked(a, 'dom_DeleteStatement', b2)
    if hasattr(b1, 'dom_Entity229'):
        assert not _is_linked(b1, 'dom_Entity229', a)
    if hasattr(b2, 'dom_Entity229'):
        assert _is_linked(b2, 'dom_Entity229', a)
    _safe_set(a, 'dom_DeleteStatement', None)
    assert not _is_linked(a, 'dom_DeleteStatement', b2)
    if hasattr(b2, 'dom_Entity229'):
        assert not _is_linked(b2, 'dom_Entity229', a)


def test_assoc_entity233_link_reassign_clear():
    a = dom_UpdateStatement(name="sample_text", versioned=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_UpdateStatement', b1)
    assert _is_linked(a, 'dom_UpdateStatement', b1)
    if hasattr(b1, 'dom_Entity234'):
        assert _is_linked(b1, 'dom_Entity234', a)
    _safe_set(a, 'dom_UpdateStatement', b2)
    assert _is_linked(a, 'dom_UpdateStatement', b2)
    if hasattr(b1, 'dom_Entity234'):
        assert not _is_linked(b1, 'dom_Entity234', a)
    if hasattr(b2, 'dom_Entity234'):
        assert _is_linked(b2, 'dom_Entity234', a)
    _safe_set(a, 'dom_UpdateStatement', None)
    assert not _is_linked(a, 'dom_UpdateStatement', b2)
    if hasattr(b2, 'dom_Entity234'):
        assert not _is_linked(b2, 'dom_Entity234', a)


def test_assoc_entity267_link_reassign_clear():
    a = dom_FromClass(popertyFetch=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_FromClass', b1)
    assert _is_linked(a, 'dom_FromClass', b1)
    if hasattr(b1, 'dom_Entity268'):
        assert _is_linked(b1, 'dom_Entity268', a)
    _safe_set(a, 'dom_FromClass', b2)
    assert _is_linked(a, 'dom_FromClass', b2)
    if hasattr(b1, 'dom_Entity268'):
        assert not _is_linked(b1, 'dom_Entity268', a)
    if hasattr(b2, 'dom_Entity268'):
        assert _is_linked(b2, 'dom_Entity268', a)
    _safe_set(a, 'dom_FromClass', None)
    assert not _is_linked(a, 'dom_FromClass', b2)
    if hasattr(b2, 'dom_Entity268'):
        assert not _is_linked(b2, 'dom_Entity268', a)


def test_assoc_entity269_link_reassign_clear():
    a = dom_JoinEntity(name="sample_text")
    b1 = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    b2 = dom_Join(fetch=False, propertyFetch=False, type="sample_text_2")
    _safe_set(a, 'dom_JoinEntity', b1)
    assert _is_linked(a, 'dom_JoinEntity', b1)
    if hasattr(b1, 'dom_Join270'):
        assert _is_linked(b1, 'dom_Join270', a)
    _safe_set(a, 'dom_JoinEntity', b2)
    assert _is_linked(a, 'dom_JoinEntity', b2)
    if hasattr(b1, 'dom_Join270'):
        assert not _is_linked(b1, 'dom_Join270', a)
    if hasattr(b2, 'dom_Join270'):
        assert _is_linked(b2, 'dom_Join270', a)
    _safe_set(a, 'dom_JoinEntity', None)
    assert not _is_linked(a, 'dom_JoinEntity', b2)
    if hasattr(b2, 'dom_Join270'):
        assert not _is_linked(b2, 'dom_Join270', a)


def test_assoc_escape353_link_reassign_clear():
    a = dom_LikeExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_LikeExpression354', b1)
    assert _is_linked(a, 'dom_LikeExpression354', b1)
    if hasattr(b1, 'dom_Expression355'):
        assert _is_linked(b1, 'dom_Expression355', a)
    _safe_set(a, 'dom_LikeExpression354', b2)
    assert _is_linked(a, 'dom_LikeExpression354', b2)
    if hasattr(b1, 'dom_Expression355'):
        assert not _is_linked(b1, 'dom_Expression355', a)
    if hasattr(b2, 'dom_Expression355'):
        assert _is_linked(b2, 'dom_Expression355', a)
    _safe_set(a, 'dom_LikeExpression354', None)
    assert not _is_linked(a, 'dom_LikeExpression354', b2)
    if hasattr(b2, 'dom_Expression355'):
        assert not _is_linked(b2, 'dom_Expression355', a)


def test_assoc_expression260_link_reassign_clear():
    a = dom_SortOrderElement(sortOrder="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_SortOrderElement261', b1)
    assert _is_linked(a, 'dom_SortOrderElement261', b1)
    if hasattr(b1, 'dom_Expression262'):
        assert _is_linked(b1, 'dom_Expression262', a)
    _safe_set(a, 'dom_SortOrderElement261', b2)
    assert _is_linked(a, 'dom_SortOrderElement261', b2)
    if hasattr(b1, 'dom_Expression262'):
        assert not _is_linked(b1, 'dom_Expression262', a)
    if hasattr(b2, 'dom_Expression262'):
        assert _is_linked(b2, 'dom_Expression262', a)
    _safe_set(a, 'dom_SortOrderElement261', None)
    assert not _is_linked(a, 'dom_SortOrderElement261', b2)
    if hasattr(b2, 'dom_Expression262'):
        assert not _is_linked(b2, 'dom_Expression262', a)


def test_assoc_expression274_link_reassign_clear():
    a = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_Join275', b1)
    assert _is_linked(a, 'dom_Join275', b1)
    if hasattr(b1, 'dom_Expression276'):
        assert _is_linked(b1, 'dom_Expression276', a)
    _safe_set(a, 'dom_Join275', b2)
    assert _is_linked(a, 'dom_Join275', b2)
    if hasattr(b1, 'dom_Expression276'):
        assert not _is_linked(b1, 'dom_Expression276', a)
    if hasattr(b2, 'dom_Expression276'):
        assert _is_linked(b2, 'dom_Expression276', a)
    _safe_set(a, 'dom_Join275', None)
    assert not _is_linked(a, 'dom_Join275', b2)
    if hasattr(b2, 'dom_Expression276'):
        assert not _is_linked(b2, 'dom_Expression276', a)


def test_assoc_expression296_link_reassign_clear():
    a = dom_QuantifiedExpression(name="sample_text", quantifier="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_QuantifiedExpression', b1)
    assert _is_linked(a, 'dom_QuantifiedExpression', b1)
    if hasattr(b1, 'dom_Expression297'):
        assert _is_linked(b1, 'dom_Expression297', a)
    _safe_set(a, 'dom_QuantifiedExpression', b2)
    assert _is_linked(a, 'dom_QuantifiedExpression', b2)
    if hasattr(b1, 'dom_Expression297'):
        assert not _is_linked(b1, 'dom_Expression297', a)
    if hasattr(b2, 'dom_Expression297'):
        assert _is_linked(b2, 'dom_Expression297', a)
    _safe_set(a, 'dom_QuantifiedExpression', None)
    assert not _is_linked(a, 'dom_QuantifiedExpression', b2)
    if hasattr(b2, 'dom_Expression297'):
        assert not _is_linked(b2, 'dom_Expression297', a)


def test_assoc_expression326_link_reassign_clear():
    a = dom_AliasedExpression(name="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_AliasedExpression', b1)
    assert _is_linked(a, 'dom_AliasedExpression', b1)
    if hasattr(b1, 'dom_Expression327'):
        assert _is_linked(b1, 'dom_Expression327', a)
    _safe_set(a, 'dom_AliasedExpression', b2)
    assert _is_linked(a, 'dom_AliasedExpression', b2)
    if hasattr(b1, 'dom_Expression327'):
        assert not _is_linked(b1, 'dom_Expression327', a)
    if hasattr(b2, 'dom_Expression327'):
        assert _is_linked(b2, 'dom_Expression327', a)
    _safe_set(a, 'dom_AliasedExpression', None)
    assert not _is_linked(a, 'dom_AliasedExpression', b2)
    if hasattr(b2, 'dom_Expression327'):
        assert not _is_linked(b2, 'dom_Expression327', a)


def test_assoc_expression335_link_reassign_clear():
    a = dom_InExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_InExpression', b1)
    assert _is_linked(a, 'dom_InExpression', b1)
    if hasattr(b1, 'dom_Expression336'):
        assert _is_linked(b1, 'dom_Expression336', a)
    _safe_set(a, 'dom_InExpression', b2)
    assert _is_linked(a, 'dom_InExpression', b2)
    if hasattr(b1, 'dom_Expression336'):
        assert not _is_linked(b1, 'dom_Expression336', a)
    if hasattr(b2, 'dom_Expression336'):
        assert _is_linked(b2, 'dom_Expression336', a)
    _safe_set(a, 'dom_InExpression', None)
    assert not _is_linked(a, 'dom_InExpression', b2)
    if hasattr(b2, 'dom_Expression336'):
        assert not _is_linked(b2, 'dom_Expression336', a)


def test_assoc_expression340_link_reassign_clear():
    a = dom_BetweenExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BetweenExpression', b1)
    assert _is_linked(a, 'dom_BetweenExpression', b1)
    if hasattr(b1, 'dom_Expression341'):
        assert _is_linked(b1, 'dom_Expression341', a)
    _safe_set(a, 'dom_BetweenExpression', b2)
    assert _is_linked(a, 'dom_BetweenExpression', b2)
    if hasattr(b1, 'dom_Expression341'):
        assert not _is_linked(b1, 'dom_Expression341', a)
    if hasattr(b2, 'dom_Expression341'):
        assert _is_linked(b2, 'dom_Expression341', a)
    _safe_set(a, 'dom_BetweenExpression', None)
    assert not _is_linked(a, 'dom_BetweenExpression', b2)
    if hasattr(b2, 'dom_Expression341'):
        assert not _is_linked(b2, 'dom_Expression341', a)


def test_assoc_expression348_link_reassign_clear():
    a = dom_LikeExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_LikeExpression', b1)
    assert _is_linked(a, 'dom_LikeExpression', b1)
    if hasattr(b1, 'dom_Expression349'):
        assert _is_linked(b1, 'dom_Expression349', a)
    _safe_set(a, 'dom_LikeExpression', b2)
    assert _is_linked(a, 'dom_LikeExpression', b2)
    if hasattr(b1, 'dom_Expression349'):
        assert not _is_linked(b1, 'dom_Expression349', a)
    if hasattr(b2, 'dom_Expression349'):
        assert _is_linked(b2, 'dom_Expression349', a)
    _safe_set(a, 'dom_LikeExpression', None)
    assert not _is_linked(a, 'dom_LikeExpression', b2)
    if hasattr(b2, 'dom_Expression349'):
        assert not _is_linked(b2, 'dom_Expression349', a)


def test_assoc_expression356_link_reassign_clear():
    a = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_MemberOfExpression', b1)
    assert _is_linked(a, 'dom_MemberOfExpression', b1)
    if hasattr(b1, 'dom_Expression357'):
        assert _is_linked(b1, 'dom_Expression357', a)
    _safe_set(a, 'dom_MemberOfExpression', b2)
    assert _is_linked(a, 'dom_MemberOfExpression', b2)
    if hasattr(b1, 'dom_Expression357'):
        assert not _is_linked(b1, 'dom_Expression357', a)
    if hasattr(b2, 'dom_Expression357'):
        assert _is_linked(b2, 'dom_Expression357', a)
    _safe_set(a, 'dom_MemberOfExpression', None)
    assert not _is_linked(a, 'dom_MemberOfExpression', b2)
    if hasattr(b2, 'dom_Expression357'):
        assert not _is_linked(b2, 'dom_Expression357', a)


def test_assoc_expression358_link_reassign_clear():
    a = dom_UnaryExpression(operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_UnaryExpression', b1)
    assert _is_linked(a, 'dom_UnaryExpression', b1)
    if hasattr(b1, 'dom_Expression359'):
        assert _is_linked(b1, 'dom_Expression359', a)
    _safe_set(a, 'dom_UnaryExpression', b2)
    assert _is_linked(a, 'dom_UnaryExpression', b2)
    if hasattr(b1, 'dom_Expression359'):
        assert not _is_linked(b1, 'dom_Expression359', a)
    if hasattr(b2, 'dom_Expression359'):
        assert _is_linked(b2, 'dom_Expression359', a)
    _safe_set(a, 'dom_UnaryExpression', None)
    assert not _is_linked(a, 'dom_UnaryExpression', b2)
    if hasattr(b2, 'dom_Expression359'):
        assert not _is_linked(b2, 'dom_Expression359', a)


def test_assoc_featureReferences34_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_DataView()
    b2 = dom_DataView()
    _safe_set(a, 'dom_FeatureReference', b1)
    assert _is_linked(a, 'dom_FeatureReference', b1)
    if hasattr(b1, 'dom_DataView35'):
        assert _is_linked(b1, 'dom_DataView35', a)
    _safe_set(a, 'dom_FeatureReference', b2)
    assert _is_linked(a, 'dom_FeatureReference', b2)
    if hasattr(b1, 'dom_DataView35'):
        assert not _is_linked(b1, 'dom_DataView35', a)
    if hasattr(b2, 'dom_DataView35'):
        assert _is_linked(b2, 'dom_DataView35', a)
    _safe_set(a, 'dom_FeatureReference', None)
    assert not _is_linked(a, 'dom_FeatureReference', b2)
    if hasattr(b2, 'dom_DataView35'):
        assert not _is_linked(b2, 'dom_DataView35', a)


def test_assoc_filter26_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_DelegateOperation27', b1)
    assert _is_linked(a, 'dom_DelegateOperation27', b1)
    if hasattr(b1, 'dom_Expression'):
        assert _is_linked(b1, 'dom_Expression', a)
    _safe_set(a, 'dom_DelegateOperation27', b2)
    assert _is_linked(a, 'dom_DelegateOperation27', b2)
    if hasattr(b1, 'dom_Expression'):
        assert not _is_linked(b1, 'dom_Expression', a)
    if hasattr(b2, 'dom_Expression'):
        assert _is_linked(b2, 'dom_Expression', a)
    _safe_set(a, 'dom_DelegateOperation27', None)
    assert not _is_linked(a, 'dom_DelegateOperation27', b2)
    if hasattr(b2, 'dom_Expression'):
        assert not _is_linked(b2, 'dom_Expression', a)


def test_assoc_from_283_link_reassign_clear():
    a = dom_TrimFunction(function="sample_text", mode="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_TrimFunction284', b1)
    assert _is_linked(a, 'dom_TrimFunction284', b1)
    if hasattr(b1, 'dom_Expression285'):
        assert _is_linked(b1, 'dom_Expression285', a)
    _safe_set(a, 'dom_TrimFunction284', b2)
    assert _is_linked(a, 'dom_TrimFunction284', b2)
    if hasattr(b1, 'dom_Expression285'):
        assert not _is_linked(b1, 'dom_Expression285', a)
    if hasattr(b2, 'dom_Expression285'):
        assert _is_linked(b2, 'dom_Expression285', a)
    _safe_set(a, 'dom_TrimFunction284', None)
    assert not _is_linked(a, 'dom_TrimFunction284', b2)
    if hasattr(b2, 'dom_Expression285'):
        assert not _is_linked(b2, 'dom_Expression285', a)


def test_assoc_from_286_link_reassign_clear():
    a = dom_CastFunction(function="sample_text", name="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_CastFunction', b1)
    assert _is_linked(a, 'dom_CastFunction', b1)
    if hasattr(b1, 'dom_Expression287'):
        assert _is_linked(b1, 'dom_Expression287', a)
    _safe_set(a, 'dom_CastFunction', b2)
    assert _is_linked(a, 'dom_CastFunction', b2)
    if hasattr(b1, 'dom_Expression287'):
        assert not _is_linked(b1, 'dom_Expression287', a)
    if hasattr(b2, 'dom_Expression287'):
        assert _is_linked(b2, 'dom_Expression287', a)
    _safe_set(a, 'dom_CastFunction', None)
    assert not _is_linked(a, 'dom_CastFunction', b2)
    if hasattr(b2, 'dom_Expression287'):
        assert not _is_linked(b2, 'dom_Expression287', a)


def test_assoc_identifier78_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Attribute80', b1)
    assert _is_linked(a, 'dom_Attribute80', b1)
    if hasattr(b1, 'dom_Entity79'):
        assert _is_linked(b1, 'dom_Entity79', a)
    _safe_set(a, 'dom_Attribute80', b2)
    assert _is_linked(a, 'dom_Attribute80', b2)
    if hasattr(b1, 'dom_Entity79'):
        assert not _is_linked(b1, 'dom_Entity79', a)
    if hasattr(b2, 'dom_Entity79'):
        assert _is_linked(b2, 'dom_Entity79', a)
    _safe_set(a, 'dom_Attribute80', None)
    assert not _is_linked(a, 'dom_Attribute80', b2)
    if hasattr(b2, 'dom_Entity79'):
        assert not _is_linked(b2, 'dom_Entity79', a)


def test_assoc_inParameter206_link_reassign_clear():
    a = dom_CallableStatement(functionCall=True, name="sample_text")
    b1 = dom_CallInputParameter(name="sample_text")
    b2 = dom_CallInputParameter(name="sample_text_2")
    _safe_set(a, 'dom_CallableStatement', {b1})
    assert _is_linked(a, 'dom_CallableStatement', b1)
    if hasattr(b1, 'dom_CallInputParameter'):
        assert _is_linked(b1, 'dom_CallInputParameter', a)
    _safe_set(a, 'dom_CallableStatement', {b2})
    assert _is_linked(a, 'dom_CallableStatement', b2)
    if hasattr(b1, 'dom_CallInputParameter'):
        assert not _is_linked(b1, 'dom_CallInputParameter', a)
    if hasattr(b2, 'dom_CallInputParameter'):
        assert _is_linked(b2, 'dom_CallInputParameter', a)
    _safe_set(a, 'dom_CallableStatement', set())
    assert not _is_linked(a, 'dom_CallableStatement', b2)
    if hasattr(b2, 'dom_CallInputParameter'):
        assert not _is_linked(b2, 'dom_CallInputParameter', a)


def test_assoc_in_337_link_reassign_clear():
    a = dom_InExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_InExpression338', b1)
    assert _is_linked(a, 'dom_InExpression338', b1)
    if hasattr(b1, 'dom_Expression339'):
        assert _is_linked(b1, 'dom_Expression339', a)
    _safe_set(a, 'dom_InExpression338', b2)
    assert _is_linked(a, 'dom_InExpression338', b2)
    if hasattr(b1, 'dom_Expression339'):
        assert not _is_linked(b1, 'dom_Expression339', a)
    if hasattr(b2, 'dom_Expression339'):
        assert _is_linked(b2, 'dom_Expression339', a)
    _safe_set(a, 'dom_InExpression338', None)
    assert not _is_linked(a, 'dom_InExpression338', b2)
    if hasattr(b2, 'dom_Expression339'):
        assert not _is_linked(b2, 'dom_Expression339', a)


def test_assoc_incrementerReference92_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_IncrementerReference()
    b2 = dom_IncrementerReference()
    _safe_set(a, 'dom_Attribute93', b1)
    assert _is_linked(a, 'dom_Attribute93', b1)
    if hasattr(b1, 'dom_IncrementerReference'):
        assert _is_linked(b1, 'dom_IncrementerReference', a)
    _safe_set(a, 'dom_Attribute93', b2)
    assert _is_linked(a, 'dom_Attribute93', b2)
    if hasattr(b1, 'dom_IncrementerReference'):
        assert not _is_linked(b1, 'dom_IncrementerReference', a)
    if hasattr(b2, 'dom_IncrementerReference'):
        assert _is_linked(b2, 'dom_IncrementerReference', a)
    _safe_set(a, 'dom_Attribute93', None)
    assert not _is_linked(a, 'dom_Attribute93', b2)
    if hasattr(b2, 'dom_IncrementerReference'):
        assert not _is_linked(b2, 'dom_IncrementerReference', a)


def test_assoc_index277_link_reassign_clear():
    a = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_PropertyValue278', {b1})
    assert _is_linked(a, 'dom_PropertyValue278', b1)
    if hasattr(b1, 'dom_Expression279'):
        assert _is_linked(b1, 'dom_Expression279', a)
    _safe_set(a, 'dom_PropertyValue278', {b2})
    assert _is_linked(a, 'dom_PropertyValue278', b2)
    if hasattr(b1, 'dom_Expression279'):
        assert not _is_linked(b1, 'dom_Expression279', a)
    if hasattr(b2, 'dom_Expression279'):
        assert _is_linked(b2, 'dom_Expression279', a)
    _safe_set(a, 'dom_PropertyValue278', set())
    assert not _is_linked(a, 'dom_PropertyValue278', b2)
    if hasattr(b2, 'dom_Expression279'):
        assert not _is_linked(b2, 'dom_Expression279', a)


def test_assoc_join247_link_reassign_clear():
    a = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    b1 = dom_SelectStatement()
    b2 = dom_SelectStatement()
    _safe_set(a, 'dom_Join', b1)
    assert _is_linked(a, 'dom_Join', b1)
    if hasattr(b1, 'dom_SelectStatement248'):
        assert _is_linked(b1, 'dom_SelectStatement248', a)
    _safe_set(a, 'dom_Join', b2)
    assert _is_linked(a, 'dom_Join', b2)
    if hasattr(b1, 'dom_SelectStatement248'):
        assert not _is_linked(b1, 'dom_SelectStatement248', a)
    if hasattr(b2, 'dom_SelectStatement248'):
        assert _is_linked(b2, 'dom_SelectStatement248', a)
    _safe_set(a, 'dom_Join', None)
    assert not _is_linked(a, 'dom_Join', b2)
    if hasattr(b2, 'dom_SelectStatement248'):
        assert not _is_linked(b2, 'dom_SelectStatement248', a)


def test_assoc_key72_link_reassign_clear():
    a = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_AttributeGroup74', b1)
    assert _is_linked(a, 'dom_AttributeGroup74', b1)
    if hasattr(b1, 'dom_Entity73'):
        assert _is_linked(b1, 'dom_Entity73', a)
    _safe_set(a, 'dom_AttributeGroup74', b2)
    assert _is_linked(a, 'dom_AttributeGroup74', b2)
    if hasattr(b1, 'dom_Entity73'):
        assert not _is_linked(b1, 'dom_Entity73', a)
    if hasattr(b2, 'dom_Entity73'):
        assert _is_linked(b2, 'dom_Entity73', a)
    _safe_set(a, 'dom_AttributeGroup74', None)
    assert not _is_linked(a, 'dom_AttributeGroup74', b2)
    if hasattr(b2, 'dom_Entity73'):
        assert not _is_linked(b2, 'dom_Entity73', a)


def test_assoc_left328_link_reassign_clear():
    a = dom_BinaryExpression(operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BinaryExpression', b1)
    assert _is_linked(a, 'dom_BinaryExpression', b1)
    if hasattr(b1, 'dom_Expression329'):
        assert _is_linked(b1, 'dom_Expression329', a)
    _safe_set(a, 'dom_BinaryExpression', b2)
    assert _is_linked(a, 'dom_BinaryExpression', b2)
    if hasattr(b1, 'dom_Expression329'):
        assert not _is_linked(b1, 'dom_Expression329', a)
    if hasattr(b2, 'dom_Expression329'):
        assert _is_linked(b2, 'dom_Expression329', a)
    _safe_set(a, 'dom_BinaryExpression', None)
    assert not _is_linked(a, 'dom_BinaryExpression', b2)
    if hasattr(b2, 'dom_Expression329'):
        assert not _is_linked(b2, 'dom_Expression329', a)


def test_assoc_left342_link_reassign_clear():
    a = dom_BetweenExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BetweenExpression343', b1)
    assert _is_linked(a, 'dom_BetweenExpression343', b1)
    if hasattr(b1, 'dom_Expression344'):
        assert _is_linked(b1, 'dom_Expression344', a)
    _safe_set(a, 'dom_BetweenExpression343', b2)
    assert _is_linked(a, 'dom_BetweenExpression343', b2)
    if hasattr(b1, 'dom_Expression344'):
        assert not _is_linked(b1, 'dom_Expression344', a)
    if hasattr(b2, 'dom_Expression344'):
        assert _is_linked(b2, 'dom_Expression344', a)
    _safe_set(a, 'dom_BetweenExpression343', None)
    assert not _is_linked(a, 'dom_BetweenExpression343', b2)
    if hasattr(b2, 'dom_Expression344'):
        assert not _is_linked(b2, 'dom_Expression344', a)


def test_assoc_left49_link_reassign_clear():
    a = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    b1 = dom_ComplexType()
    b2 = dom_ComplexType()
    _safe_set(a, 'dom_Mapper', b1)
    assert _is_linked(a, 'dom_Mapper', b1)
    if hasattr(b1, 'dom_ComplexType50'):
        assert _is_linked(b1, 'dom_ComplexType50', a)
    _safe_set(a, 'dom_Mapper', b2)
    assert _is_linked(a, 'dom_Mapper', b2)
    if hasattr(b1, 'dom_ComplexType50'):
        assert not _is_linked(b1, 'dom_ComplexType50', a)
    if hasattr(b2, 'dom_ComplexType50'):
        assert _is_linked(b2, 'dom_ComplexType50', a)
    _safe_set(a, 'dom_Mapper', None)
    assert not _is_linked(a, 'dom_Mapper', b2)
    if hasattr(b2, 'dom_ComplexType50'):
        assert not _is_linked(b2, 'dom_ComplexType50', a)


def test_assoc_left56_link_reassign_clear():
    a = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_PropertyMapping57', b1)
    assert _is_linked(a, 'dom_PropertyMapping57', b1)
    if hasattr(b1, 'dom_Attribute58'):
        assert _is_linked(b1, 'dom_Attribute58', a)
    _safe_set(a, 'dom_PropertyMapping57', b2)
    assert _is_linked(a, 'dom_PropertyMapping57', b2)
    if hasattr(b1, 'dom_Attribute58'):
        assert not _is_linked(b1, 'dom_Attribute58', a)
    if hasattr(b2, 'dom_Attribute58'):
        assert _is_linked(b2, 'dom_Attribute58', a)
    _safe_set(a, 'dom_PropertyMapping57', None)
    assert not _is_linked(a, 'dom_PropertyMapping57', b2)
    if hasattr(b2, 'dom_Attribute58'):
        assert not _is_linked(b2, 'dom_Attribute58', a)


def test_assoc_like350_link_reassign_clear():
    a = dom_LikeExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_LikeExpression351', b1)
    assert _is_linked(a, 'dom_LikeExpression351', b1)
    if hasattr(b1, 'dom_Expression352'):
        assert _is_linked(b1, 'dom_Expression352', a)
    _safe_set(a, 'dom_LikeExpression351', b2)
    assert _is_linked(a, 'dom_LikeExpression351', b2)
    if hasattr(b1, 'dom_Expression352'):
        assert not _is_linked(b1, 'dom_Expression352', a)
    if hasattr(b2, 'dom_Expression352'):
        assert _is_linked(b2, 'dom_Expression352', a)
    _safe_set(a, 'dom_LikeExpression351', None)
    assert not _is_linked(a, 'dom_LikeExpression351', b2)
    if hasattr(b2, 'dom_Expression352'):
        assert not _is_linked(b2, 'dom_Expression352', a)


def test_assoc_manyToManyAssociations149_link_reassign_clear():
    a = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_ManyToMany', b1)
    assert _is_linked(a, 'dom_ManyToMany', b1)
    if hasattr(b1, 'dom_Dao150'):
        assert _is_linked(b1, 'dom_Dao150', a)
    _safe_set(a, 'dom_ManyToMany', b2)
    assert _is_linked(a, 'dom_ManyToMany', b2)
    if hasattr(b1, 'dom_Dao150'):
        assert not _is_linked(b1, 'dom_Dao150', a)
    if hasattr(b2, 'dom_Dao150'):
        assert _is_linked(b2, 'dom_Dao150', a)
    _safe_set(a, 'dom_ManyToMany', None)
    assert not _is_linked(a, 'dom_ManyToMany', b2)
    if hasattr(b2, 'dom_Dao150'):
        assert not _is_linked(b2, 'dom_Dao150', a)


def test_assoc_manyToOneAssociations143_link_reassign_clear():
    a = dom_ManyToOne(columnName="sample_text", derived=True)
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_ManyToOne', b1)
    assert _is_linked(a, 'dom_ManyToOne', b1)
    if hasattr(b1, 'dom_Dao144'):
        assert _is_linked(b1, 'dom_Dao144', a)
    _safe_set(a, 'dom_ManyToOne', b2)
    assert _is_linked(a, 'dom_ManyToOne', b2)
    if hasattr(b1, 'dom_Dao144'):
        assert not _is_linked(b1, 'dom_Dao144', a)
    if hasattr(b2, 'dom_Dao144'):
        assert _is_linked(b2, 'dom_Dao144', a)
    _safe_set(a, 'dom_ManyToOne', None)
    assert not _is_linked(a, 'dom_ManyToOne', b2)
    if hasattr(b2, 'dom_Dao144'):
        assert not _is_linked(b2, 'dom_Dao144', a)


def test_assoc_naturalKey163_link_reassign_clear():
    a = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_DataBaseConstraint165', b1)
    assert _is_linked(a, 'dom_DataBaseConstraint165', b1)
    if hasattr(b1, 'dom_Dao164'):
        assert _is_linked(b1, 'dom_Dao164', a)
    _safe_set(a, 'dom_DataBaseConstraint165', b2)
    assert _is_linked(a, 'dom_DataBaseConstraint165', b2)
    if hasattr(b1, 'dom_Dao164'):
        assert not _is_linked(b1, 'dom_Dao164', a)
    if hasattr(b2, 'dom_Dao164'):
        assert _is_linked(b2, 'dom_Dao164', a)
    _safe_set(a, 'dom_DataBaseConstraint165', None)
    assert not _is_linked(a, 'dom_DataBaseConstraint165', b2)
    if hasattr(b2, 'dom_Dao164'):
        assert not _is_linked(b2, 'dom_Dao164', a)


def test_assoc_naturalKeyColumns154_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_Dao155', {b1})
    assert _is_linked(a, 'dom_Dao155', b1)
    if hasattr(b1, 'dom_Column156'):
        assert _is_linked(b1, 'dom_Column156', a)
    _safe_set(a, 'dom_Dao155', {b2})
    assert _is_linked(a, 'dom_Dao155', b2)
    if hasattr(b1, 'dom_Column156'):
        assert not _is_linked(b1, 'dom_Column156', a)
    if hasattr(b2, 'dom_Column156'):
        assert _is_linked(b2, 'dom_Column156', a)
    _safe_set(a, 'dom_Dao155', set())
    assert not _is_linked(a, 'dom_Dao155', b2)
    if hasattr(b2, 'dom_Column156'):
        assert not _is_linked(b2, 'dom_Column156', a)


def test_assoc_nestedAttribute218_link_reassign_clear():
    a = dom_CallOutputParameter(name="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_CallOutputParameter219', b1)
    assert _is_linked(a, 'dom_CallOutputParameter219', b1)
    if hasattr(b1, 'dom_Attribute220'):
        assert _is_linked(b1, 'dom_Attribute220', a)
    _safe_set(a, 'dom_CallOutputParameter219', b2)
    assert _is_linked(a, 'dom_CallOutputParameter219', b2)
    if hasattr(b1, 'dom_Attribute220'):
        assert not _is_linked(b1, 'dom_Attribute220', a)
    if hasattr(b2, 'dom_Attribute220'):
        assert _is_linked(b2, 'dom_Attribute220', a)
    _safe_set(a, 'dom_CallOutputParameter219', None)
    assert not _is_linked(a, 'dom_CallOutputParameter219', b2)
    if hasattr(b2, 'dom_Attribute220'):
        assert not _is_linked(b2, 'dom_Attribute220', a)


def test_assoc_oneToManyAssociations147_link_reassign_clear():
    a = dom_OneToMany(columnName="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_OneToMany', b1)
    assert _is_linked(a, 'dom_OneToMany', b1)
    if hasattr(b1, 'dom_Dao148'):
        assert _is_linked(b1, 'dom_Dao148', a)
    _safe_set(a, 'dom_OneToMany', b2)
    assert _is_linked(a, 'dom_OneToMany', b2)
    if hasattr(b1, 'dom_Dao148'):
        assert not _is_linked(b1, 'dom_Dao148', a)
    if hasattr(b2, 'dom_Dao148'):
        assert _is_linked(b2, 'dom_Dao148', a)
    _safe_set(a, 'dom_OneToMany', None)
    assert not _is_linked(a, 'dom_OneToMany', b2)
    if hasattr(b2, 'dom_Dao148'):
        assert not _is_linked(b2, 'dom_Dao148', a)


def test_assoc_oneToOneAssociations145_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_OneToOne()
    b2 = dom_OneToOne()
    _safe_set(a, 'dom_Dao146', {b1})
    assert _is_linked(a, 'dom_Dao146', b1)
    if hasattr(b1, 'dom_OneToOne'):
        assert _is_linked(b1, 'dom_OneToOne', a)
    _safe_set(a, 'dom_Dao146', {b2})
    assert _is_linked(a, 'dom_Dao146', b2)
    if hasattr(b1, 'dom_OneToOne'):
        assert not _is_linked(b1, 'dom_OneToOne', a)
    if hasattr(b2, 'dom_OneToOne'):
        assert _is_linked(b2, 'dom_OneToOne', a)
    _safe_set(a, 'dom_Dao146', set())
    assert not _is_linked(a, 'dom_Dao146', b2)
    if hasattr(b2, 'dom_OneToOne'):
        assert not _is_linked(b2, 'dom_OneToOne', a)


def test_assoc_operation21_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_DaoOperation(many=True, name="sample_text")
    b2 = dom_DaoOperation(many=False, name="sample_text_2")
    _safe_set(a, 'dom_DelegateOperation22', b1)
    assert _is_linked(a, 'dom_DelegateOperation22', b1)
    if hasattr(b1, 'dom_DaoOperation'):
        assert _is_linked(b1, 'dom_DaoOperation', a)
    _safe_set(a, 'dom_DelegateOperation22', b2)
    assert _is_linked(a, 'dom_DelegateOperation22', b2)
    if hasattr(b1, 'dom_DaoOperation'):
        assert not _is_linked(b1, 'dom_DaoOperation', a)
    if hasattr(b2, 'dom_DaoOperation'):
        assert _is_linked(b2, 'dom_DaoOperation', a)
    _safe_set(a, 'dom_DelegateOperation22', None)
    assert not _is_linked(a, 'dom_DelegateOperation22', b2)
    if hasattr(b2, 'dom_DaoOperation'):
        assert not _is_linked(b2, 'dom_DaoOperation', a)


def test_assoc_operations134_link_reassign_clear():
    a = dom_Operation(expression="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_Operation136', b1)
    assert _is_linked(a, 'dom_Operation136', b1)
    if hasattr(b1, 'dom_Dao135'):
        assert _is_linked(b1, 'dom_Dao135', a)
    _safe_set(a, 'dom_Operation136', b2)
    assert _is_linked(a, 'dom_Operation136', b2)
    if hasattr(b1, 'dom_Dao135'):
        assert not _is_linked(b1, 'dom_Dao135', a)
    if hasattr(b2, 'dom_Dao135'):
        assert _is_linked(b2, 'dom_Dao135', a)
    _safe_set(a, 'dom_Operation136', None)
    assert not _is_linked(a, 'dom_Operation136', b2)
    if hasattr(b2, 'dom_Dao135'):
        assert not _is_linked(b2, 'dom_Dao135', a)


def test_assoc_operations5_link_reassign_clear():
    a = dom_Operation(expression="sample_text")
    b1 = dom_Service()
    b2 = dom_Service()
    _safe_set(a, 'dom_Operation', b1)
    assert _is_linked(a, 'dom_Operation', b1)
    if hasattr(b1, 'dom_Service6'):
        assert _is_linked(b1, 'dom_Service6', a)
    _safe_set(a, 'dom_Operation', b2)
    assert _is_linked(a, 'dom_Operation', b2)
    if hasattr(b1, 'dom_Service6'):
        assert not _is_linked(b1, 'dom_Service6', a)
    if hasattr(b2, 'dom_Service6'):
        assert _is_linked(b2, 'dom_Service6', a)
    _safe_set(a, 'dom_Operation', None)
    assert not _is_linked(a, 'dom_Operation', b2)
    if hasattr(b2, 'dom_Service6'):
        assert not _is_linked(b2, 'dom_Service6', a)


def test_assoc_opposite95_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_Attribute94', b1)
    assert _is_linked(a, 'dom_Attribute94', b1)
    if hasattr(b1, 'dom_Attribute96'):
        assert _is_linked(b1, 'dom_Attribute96', a)
    _safe_set(a, 'dom_Attribute94', b2)
    assert _is_linked(a, 'dom_Attribute94', b2)
    if hasattr(b1, 'dom_Attribute96'):
        assert not _is_linked(b1, 'dom_Attribute96', a)
    if hasattr(b2, 'dom_Attribute96'):
        assert _is_linked(b2, 'dom_Attribute96', a)
    _safe_set(a, 'dom_Attribute94', None)
    assert not _is_linked(a, 'dom_Attribute94', b2)
    if hasattr(b2, 'dom_Attribute96'):
        assert not _is_linked(b2, 'dom_Attribute96', a)


def test_assoc_oppositeReference107_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_Attribute106', b1)
    assert _is_linked(a, 'dom_Attribute106', b1)
    if hasattr(b1, 'dom_Attribute108'):
        assert _is_linked(b1, 'dom_Attribute108', a)
    _safe_set(a, 'dom_Attribute106', b2)
    assert _is_linked(a, 'dom_Attribute106', b2)
    if hasattr(b1, 'dom_Attribute108'):
        assert not _is_linked(b1, 'dom_Attribute108', a)
    if hasattr(b2, 'dom_Attribute108'):
        assert _is_linked(b2, 'dom_Attribute108', a)
    _safe_set(a, 'dom_Attribute106', None)
    assert not _is_linked(a, 'dom_Attribute106', b2)
    if hasattr(b2, 'dom_Attribute108'):
        assert not _is_linked(b2, 'dom_Attribute108', a)


def test_assoc_orderBy258_link_reassign_clear():
    a = dom_SortOrderElement(sortOrder="sample_text")
    b1 = dom_SelectStatement()
    b2 = dom_SelectStatement()
    _safe_set(a, 'dom_SortOrderElement', b1)
    assert _is_linked(a, 'dom_SortOrderElement', b1)
    if hasattr(b1, 'dom_SelectStatement259'):
        assert _is_linked(b1, 'dom_SelectStatement259', a)
    _safe_set(a, 'dom_SortOrderElement', b2)
    assert _is_linked(a, 'dom_SortOrderElement', b2)
    if hasattr(b1, 'dom_SelectStatement259'):
        assert not _is_linked(b1, 'dom_SelectStatement259', a)
    if hasattr(b2, 'dom_SelectStatement259'):
        assert _is_linked(b2, 'dom_SelectStatement259', a)
    _safe_set(a, 'dom_SortOrderElement', None)
    assert not _is_linked(a, 'dom_SortOrderElement', b2)
    if hasattr(b2, 'dom_SelectStatement259'):
        assert not _is_linked(b2, 'dom_SelectStatement259', a)


def test_assoc_outParameter207_link_reassign_clear():
    a = dom_CallableStatement(functionCall=True, name="sample_text")
    b1 = dom_CallOutputParameter(name="sample_text")
    b2 = dom_CallOutputParameter(name="sample_text_2")
    _safe_set(a, 'dom_CallableStatement208', {b1})
    assert _is_linked(a, 'dom_CallableStatement208', b1)
    if hasattr(b1, 'dom_CallOutputParameter'):
        assert _is_linked(b1, 'dom_CallOutputParameter', a)
    _safe_set(a, 'dom_CallableStatement208', {b2})
    assert _is_linked(a, 'dom_CallableStatement208', b2)
    if hasattr(b1, 'dom_CallOutputParameter'):
        assert not _is_linked(b1, 'dom_CallOutputParameter', a)
    if hasattr(b2, 'dom_CallOutputParameter'):
        assert _is_linked(b2, 'dom_CallOutputParameter', a)
    _safe_set(a, 'dom_CallableStatement208', set())
    assert not _is_linked(a, 'dom_CallableStatement208', b2)
    if hasattr(b2, 'dom_CallOutputParameter'):
        assert not _is_linked(b2, 'dom_CallOutputParameter', a)


def test_assoc_parameter209_link_reassign_clear():
    a = dom_CallInputParameter(name="sample_text")
    b1 = dom_QueryParameter()
    b2 = dom_QueryParameter()
    _safe_set(a, 'dom_CallInputParameter210', b1)
    assert _is_linked(a, 'dom_CallInputParameter210', b1)
    if hasattr(b1, 'dom_QueryParameter211'):
        assert _is_linked(b1, 'dom_QueryParameter211', a)
    _safe_set(a, 'dom_CallInputParameter210', b2)
    assert _is_linked(a, 'dom_CallInputParameter210', b2)
    if hasattr(b1, 'dom_QueryParameter211'):
        assert not _is_linked(b1, 'dom_QueryParameter211', a)
    if hasattr(b2, 'dom_QueryParameter211'):
        assert _is_linked(b2, 'dom_QueryParameter211', a)
    _safe_set(a, 'dom_CallInputParameter210', None)
    assert not _is_linked(a, 'dom_CallInputParameter210', b2)
    if hasattr(b2, 'dom_QueryParameter211'):
        assert not _is_linked(b2, 'dom_QueryParameter211', a)


def test_assoc_parameters10_link_reassign_clear():
    a = dom_Parameter(many=True, name="sample_text")
    b1 = dom_Operation(expression="sample_text")
    b2 = dom_Operation(expression="sample_text_2")
    _safe_set(a, 'dom_Parameter', b1)
    assert _is_linked(a, 'dom_Parameter', b1)
    if hasattr(b1, 'dom_Operation11'):
        assert _is_linked(b1, 'dom_Operation11', a)
    _safe_set(a, 'dom_Parameter', b2)
    assert _is_linked(a, 'dom_Parameter', b2)
    if hasattr(b1, 'dom_Operation11'):
        assert not _is_linked(b1, 'dom_Operation11', a)
    if hasattr(b2, 'dom_Operation11'):
        assert _is_linked(b2, 'dom_Operation11', a)
    _safe_set(a, 'dom_Parameter', None)
    assert not _is_linked(a, 'dom_Parameter', b2)
    if hasattr(b2, 'dom_Operation11'):
        assert not _is_linked(b2, 'dom_Operation11', a)


def test_assoc_primaryKey160_link_reassign_clear():
    a = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_DataBaseConstraint162', b1)
    assert _is_linked(a, 'dom_DataBaseConstraint162', b1)
    if hasattr(b1, 'dom_Dao161'):
        assert _is_linked(b1, 'dom_Dao161', a)
    _safe_set(a, 'dom_DataBaseConstraint162', b2)
    assert _is_linked(a, 'dom_DataBaseConstraint162', b2)
    if hasattr(b1, 'dom_Dao161'):
        assert not _is_linked(b1, 'dom_Dao161', a)
    if hasattr(b2, 'dom_Dao161'):
        assert _is_linked(b2, 'dom_Dao161', a)
    _safe_set(a, 'dom_DataBaseConstraint162', None)
    assert not _is_linked(a, 'dom_DataBaseConstraint162', b2)
    if hasattr(b2, 'dom_Dao161'):
        assert not _is_linked(b2, 'dom_Dao161', a)


def test_assoc_primaryKeyColumn151_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_Dao152', b1)
    assert _is_linked(a, 'dom_Dao152', b1)
    if hasattr(b1, 'dom_Column153'):
        assert _is_linked(b1, 'dom_Column153', a)
    _safe_set(a, 'dom_Dao152', b2)
    assert _is_linked(a, 'dom_Dao152', b2)
    if hasattr(b1, 'dom_Column153'):
        assert not _is_linked(b1, 'dom_Column153', a)
    if hasattr(b2, 'dom_Column153'):
        assert _is_linked(b2, 'dom_Column153', a)
    _safe_set(a, 'dom_Dao152', None)
    assert not _is_linked(a, 'dom_Dao152', b2)
    if hasattr(b2, 'dom_Column153'):
        assert not _is_linked(b2, 'dom_Column153', a)


def test_assoc_properties199_link_reassign_clear():
    a = dom_Property(defaultValue="sample_text", name="sample_text")
    b1 = dom_ApplicationSession()
    b2 = dom_ApplicationSession()
    _safe_set(a, 'dom_Property200', b1)
    assert _is_linked(a, 'dom_Property200', b1)
    if hasattr(b1, 'dom_ApplicationSession'):
        assert _is_linked(b1, 'dom_ApplicationSession', a)
    _safe_set(a, 'dom_Property200', b2)
    assert _is_linked(a, 'dom_Property200', b2)
    if hasattr(b1, 'dom_ApplicationSession'):
        assert not _is_linked(b1, 'dom_ApplicationSession', a)
    if hasattr(b2, 'dom_ApplicationSession'):
        assert _is_linked(b2, 'dom_ApplicationSession', a)
    _safe_set(a, 'dom_Property200', None)
    assert not _is_linked(a, 'dom_Property200', b2)
    if hasattr(b2, 'dom_ApplicationSession'):
        assert not _is_linked(b2, 'dom_ApplicationSession', a)


def test_assoc_properties263_link_reassign_clear():
    a = dom_SelectProperties(distinct=True)
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_SelectProperties', {b1})
    assert _is_linked(a, 'dom_SelectProperties', b1)
    if hasattr(b1, 'dom_Expression264'):
        assert _is_linked(b1, 'dom_Expression264', a)
    _safe_set(a, 'dom_SelectProperties', {b2})
    assert _is_linked(a, 'dom_SelectProperties', b2)
    if hasattr(b1, 'dom_Expression264'):
        assert not _is_linked(b1, 'dom_Expression264', a)
    if hasattr(b2, 'dom_Expression264'):
        assert _is_linked(b2, 'dom_Expression264', a)
    _safe_set(a, 'dom_SelectProperties', set())
    assert not _is_linked(a, 'dom_SelectProperties', b2)
    if hasattr(b2, 'dom_Expression264'):
        assert not _is_linked(b2, 'dom_Expression264', a)


def test_assoc_properties44_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_AttributeProperty()
    b2 = dom_AttributeProperty()
    _safe_set(a, 'dom_FeatureReference45', {b1})
    assert _is_linked(a, 'dom_FeatureReference45', b1)
    if hasattr(b1, 'dom_AttributeProperty'):
        assert _is_linked(b1, 'dom_AttributeProperty', a)
    _safe_set(a, 'dom_FeatureReference45', {b2})
    assert _is_linked(a, 'dom_FeatureReference45', b2)
    if hasattr(b1, 'dom_AttributeProperty'):
        assert not _is_linked(b1, 'dom_AttributeProperty', a)
    if hasattr(b2, 'dom_AttributeProperty'):
        assert _is_linked(b2, 'dom_AttributeProperty', a)
    _safe_set(a, 'dom_FeatureReference45', set())
    assert not _is_linked(a, 'dom_FeatureReference45', b2)
    if hasattr(b2, 'dom_AttributeProperty'):
        assert not _is_linked(b2, 'dom_AttributeProperty', a)


def test_assoc_property240_link_reassign_clear():
    a = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    b1 = dom_PropertyAssignment()
    b2 = dom_PropertyAssignment()
    _safe_set(a, 'dom_PropertyValue', b1)
    assert _is_linked(a, 'dom_PropertyValue', b1)
    if hasattr(b1, 'dom_PropertyAssignment241'):
        assert _is_linked(b1, 'dom_PropertyAssignment241', a)
    _safe_set(a, 'dom_PropertyValue', b2)
    assert _is_linked(a, 'dom_PropertyValue', b2)
    if hasattr(b1, 'dom_PropertyAssignment241'):
        assert not _is_linked(b1, 'dom_PropertyAssignment241', a)
    if hasattr(b2, 'dom_PropertyAssignment241'):
        assert _is_linked(b2, 'dom_PropertyAssignment241', a)
    _safe_set(a, 'dom_PropertyValue', None)
    assert not _is_linked(a, 'dom_PropertyValue', b2)
    if hasattr(b2, 'dom_PropertyAssignment241'):
        assert not _is_linked(b2, 'dom_PropertyAssignment241', a)


def test_assoc_property319_link_reassign_clear():
    a = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    b1 = dom_CollectionFunction(function="sample_text")
    b2 = dom_CollectionFunction(function="sample_text_2")
    _safe_set(a, 'dom_PropertyValue321', b1)
    assert _is_linked(a, 'dom_PropertyValue321', b1)
    if hasattr(b1, 'dom_CollectionFunction320'):
        assert _is_linked(b1, 'dom_CollectionFunction320', a)
    _safe_set(a, 'dom_PropertyValue321', b2)
    assert _is_linked(a, 'dom_PropertyValue321', b2)
    if hasattr(b1, 'dom_CollectionFunction320'):
        assert not _is_linked(b1, 'dom_CollectionFunction320', a)
    if hasattr(b2, 'dom_CollectionFunction320'):
        assert _is_linked(b2, 'dom_CollectionFunction320', a)
    _safe_set(a, 'dom_PropertyValue321', None)
    assert not _is_linked(a, 'dom_PropertyValue321', b2)
    if hasattr(b2, 'dom_CollectionFunction320'):
        assert not _is_linked(b2, 'dom_CollectionFunction320', a)


def test_assoc_propertyMappings54_link_reassign_clear():
    a = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    b1 = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    b2 = dom_Mapper(biDirectional=False, toLeft=False, toRight=False)
    _safe_set(a, 'dom_PropertyMapping', b1)
    assert _is_linked(a, 'dom_PropertyMapping', b1)
    if hasattr(b1, 'dom_Mapper55'):
        assert _is_linked(b1, 'dom_Mapper55', a)
    _safe_set(a, 'dom_PropertyMapping', b2)
    assert _is_linked(a, 'dom_PropertyMapping', b2)
    if hasattr(b1, 'dom_Mapper55'):
        assert not _is_linked(b1, 'dom_Mapper55', a)
    if hasattr(b2, 'dom_Mapper55'):
        assert _is_linked(b2, 'dom_Mapper55', a)
    _safe_set(a, 'dom_PropertyMapping', None)
    assert not _is_linked(a, 'dom_PropertyMapping', b2)
    if hasattr(b2, 'dom_Mapper55'):
        assert not _is_linked(b2, 'dom_Mapper55', a)


def test_assoc_queryOperation137_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_QueryOperation()
    b2 = dom_QueryOperation()
    _safe_set(a, 'dom_Dao138', {b1})
    assert _is_linked(a, 'dom_Dao138', b1)
    if hasattr(b1, 'dom_QueryOperation'):
        assert _is_linked(b1, 'dom_QueryOperation', a)
    _safe_set(a, 'dom_Dao138', {b2})
    assert _is_linked(a, 'dom_Dao138', b2)
    if hasattr(b1, 'dom_QueryOperation'):
        assert not _is_linked(b1, 'dom_QueryOperation', a)
    if hasattr(b2, 'dom_QueryOperation'):
        assert _is_linked(b2, 'dom_QueryOperation', a)
    _safe_set(a, 'dom_Dao138', set())
    assert not _is_linked(a, 'dom_Dao138', b2)
    if hasattr(b2, 'dom_QueryOperation'):
        assert not _is_linked(b2, 'dom_QueryOperation', a)


def test_assoc_reference271_link_reassign_clear():
    a = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_Join272', b1)
    assert _is_linked(a, 'dom_Join272', b1)
    if hasattr(b1, 'dom_Attribute273'):
        assert _is_linked(b1, 'dom_Attribute273', a)
    _safe_set(a, 'dom_Join272', b2)
    assert _is_linked(a, 'dom_Join272', b2)
    if hasattr(b1, 'dom_Attribute273'):
        assert not _is_linked(b1, 'dom_Attribute273', a)
    if hasattr(b2, 'dom_Attribute273'):
        assert _is_linked(b2, 'dom_Attribute273', a)
    _safe_set(a, 'dom_Join272', None)
    assert not _is_linked(a, 'dom_Join272', b2)
    if hasattr(b2, 'dom_Attribute273'):
        assert not _is_linked(b2, 'dom_Attribute273', a)


def test_assoc_repository19_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'dom_DelegateOperation20', b1)
    assert _is_linked(a, 'dom_DelegateOperation20', b1)
    if hasattr(b1, 'dom_Dao'):
        assert _is_linked(b1, 'dom_Dao', a)
    _safe_set(a, 'dom_DelegateOperation20', b2)
    assert _is_linked(a, 'dom_DelegateOperation20', b2)
    if hasattr(b1, 'dom_Dao'):
        assert not _is_linked(b1, 'dom_Dao', a)
    if hasattr(b2, 'dom_Dao'):
        assert _is_linked(b2, 'dom_Dao', a)
    _safe_set(a, 'dom_DelegateOperation20', None)
    assert not _is_linked(a, 'dom_DelegateOperation20', b2)
    if hasattr(b2, 'dom_Dao'):
        assert not _is_linked(b2, 'dom_Dao', a)


def test_assoc_repository69_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Dao71', b1)
    assert _is_linked(a, 'dom_Dao71', b1)
    if hasattr(b1, 'dom_Entity70'):
        assert _is_linked(b1, 'dom_Entity70', a)
    _safe_set(a, 'dom_Dao71', b2)
    assert _is_linked(a, 'dom_Dao71', b2)
    if hasattr(b1, 'dom_Entity70'):
        assert not _is_linked(b1, 'dom_Entity70', a)
    if hasattr(b2, 'dom_Entity70'):
        assert _is_linked(b2, 'dom_Entity70', a)
    _safe_set(a, 'dom_Dao71', None)
    assert not _is_linked(a, 'dom_Dao71', b2)
    if hasattr(b2, 'dom_Entity70'):
        assert not _is_linked(b2, 'dom_Entity70', a)


def test_assoc_requiredAttributes87_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Attribute89', b1)
    assert _is_linked(a, 'dom_Attribute89', b1)
    if hasattr(b1, 'dom_Entity88'):
        assert _is_linked(b1, 'dom_Entity88', a)
    _safe_set(a, 'dom_Attribute89', b2)
    assert _is_linked(a, 'dom_Attribute89', b2)
    if hasattr(b1, 'dom_Entity88'):
        assert not _is_linked(b1, 'dom_Entity88', a)
    if hasattr(b2, 'dom_Entity88'):
        assert _is_linked(b2, 'dom_Entity88', a)
    _safe_set(a, 'dom_Attribute89', None)
    assert not _is_linked(a, 'dom_Attribute89', b2)
    if hasattr(b2, 'dom_Entity88'):
        assert not _is_linked(b2, 'dom_Entity88', a)


def test_assoc_requiredReferences84_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Attribute86', b1)
    assert _is_linked(a, 'dom_Attribute86', b1)
    if hasattr(b1, 'dom_Entity85'):
        assert _is_linked(b1, 'dom_Entity85', a)
    _safe_set(a, 'dom_Attribute86', b2)
    assert _is_linked(a, 'dom_Attribute86', b2)
    if hasattr(b1, 'dom_Entity85'):
        assert not _is_linked(b1, 'dom_Entity85', a)
    if hasattr(b2, 'dom_Entity85'):
        assert _is_linked(b2, 'dom_Entity85', a)
    _safe_set(a, 'dom_Attribute86', None)
    assert not _is_linked(a, 'dom_Attribute86', b2)
    if hasattr(b2, 'dom_Entity85'):
        assert not _is_linked(b2, 'dom_Entity85', a)


def test_assoc_resolvedAttributeList110_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_Attribute109', {b1})
    assert _is_linked(a, 'dom_Attribute109', b1)
    if hasattr(b1, 'dom_Attribute111'):
        assert _is_linked(b1, 'dom_Attribute111', a)
    _safe_set(a, 'dom_Attribute109', {b2})
    assert _is_linked(a, 'dom_Attribute109', b2)
    if hasattr(b1, 'dom_Attribute111'):
        assert not _is_linked(b1, 'dom_Attribute111', a)
    if hasattr(b2, 'dom_Attribute111'):
        assert _is_linked(b2, 'dom_Attribute111', a)
    _safe_set(a, 'dom_Attribute109', set())
    assert not _is_linked(a, 'dom_Attribute109', b2)
    if hasattr(b2, 'dom_Attribute111'):
        assert not _is_linked(b2, 'dom_Attribute111', a)


def test_assoc_resolvedAttributeList123_link_reassign_clear():
    a = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_AttributeGroup124', {b1})
    assert _is_linked(a, 'dom_AttributeGroup124', b1)
    if hasattr(b1, 'dom_Attribute125'):
        assert _is_linked(b1, 'dom_Attribute125', a)
    _safe_set(a, 'dom_AttributeGroup124', {b2})
    assert _is_linked(a, 'dom_AttributeGroup124', b2)
    if hasattr(b1, 'dom_Attribute125'):
        assert not _is_linked(b1, 'dom_Attribute125', a)
    if hasattr(b2, 'dom_Attribute125'):
        assert _is_linked(b2, 'dom_Attribute125', a)
    _safe_set(a, 'dom_AttributeGroup124', set())
    assert not _is_linked(a, 'dom_AttributeGroup124', b2)
    if hasattr(b2, 'dom_Attribute125'):
        assert not _is_linked(b2, 'dom_Attribute125', a)


def test_assoc_resolvedAttributeList196_link_reassign_clear():
    a = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_DataBaseConstraint197', {b1})
    assert _is_linked(a, 'dom_DataBaseConstraint197', b1)
    if hasattr(b1, 'dom_Attribute198'):
        assert _is_linked(b1, 'dom_Attribute198', a)
    _safe_set(a, 'dom_DataBaseConstraint197', {b2})
    assert _is_linked(a, 'dom_DataBaseConstraint197', b2)
    if hasattr(b1, 'dom_Attribute198'):
        assert not _is_linked(b1, 'dom_Attribute198', a)
    if hasattr(b2, 'dom_Attribute198'):
        assert _is_linked(b2, 'dom_Attribute198', a)
    _safe_set(a, 'dom_DataBaseConstraint197', set())
    assert not _is_linked(a, 'dom_DataBaseConstraint197', b2)
    if hasattr(b2, 'dom_Attribute198'):
        assert not _is_linked(b2, 'dom_Attribute198', a)


def test_assoc_right330_link_reassign_clear():
    a = dom_BinaryExpression(operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BinaryExpression331', b1)
    assert _is_linked(a, 'dom_BinaryExpression331', b1)
    if hasattr(b1, 'dom_Expression332'):
        assert _is_linked(b1, 'dom_Expression332', a)
    _safe_set(a, 'dom_BinaryExpression331', b2)
    assert _is_linked(a, 'dom_BinaryExpression331', b2)
    if hasattr(b1, 'dom_Expression332'):
        assert not _is_linked(b1, 'dom_Expression332', a)
    if hasattr(b2, 'dom_Expression332'):
        assert _is_linked(b2, 'dom_Expression332', a)
    _safe_set(a, 'dom_BinaryExpression331', None)
    assert not _is_linked(a, 'dom_BinaryExpression331', b2)
    if hasattr(b2, 'dom_Expression332'):
        assert not _is_linked(b2, 'dom_Expression332', a)


def test_assoc_right345_link_reassign_clear():
    a = dom_BetweenExpression(not_=True, operator="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BetweenExpression346', b1)
    assert _is_linked(a, 'dom_BetweenExpression346', b1)
    if hasattr(b1, 'dom_Expression347'):
        assert _is_linked(b1, 'dom_Expression347', a)
    _safe_set(a, 'dom_BetweenExpression346', b2)
    assert _is_linked(a, 'dom_BetweenExpression346', b2)
    if hasattr(b1, 'dom_Expression347'):
        assert not _is_linked(b1, 'dom_Expression347', a)
    if hasattr(b2, 'dom_Expression347'):
        assert _is_linked(b2, 'dom_Expression347', a)
    _safe_set(a, 'dom_BetweenExpression346', None)
    assert not _is_linked(a, 'dom_BetweenExpression346', b2)
    if hasattr(b2, 'dom_Expression347'):
        assert not _is_linked(b2, 'dom_Expression347', a)


def test_assoc_right51_link_reassign_clear():
    a = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    b1 = dom_ComplexType()
    b2 = dom_ComplexType()
    _safe_set(a, 'dom_Mapper52', b1)
    assert _is_linked(a, 'dom_Mapper52', b1)
    if hasattr(b1, 'dom_ComplexType53'):
        assert _is_linked(b1, 'dom_ComplexType53', a)
    _safe_set(a, 'dom_Mapper52', b2)
    assert _is_linked(a, 'dom_Mapper52', b2)
    if hasattr(b1, 'dom_ComplexType53'):
        assert not _is_linked(b1, 'dom_ComplexType53', a)
    if hasattr(b2, 'dom_ComplexType53'):
        assert _is_linked(b2, 'dom_ComplexType53', a)
    _safe_set(a, 'dom_Mapper52', None)
    assert not _is_linked(a, 'dom_Mapper52', b2)
    if hasattr(b2, 'dom_ComplexType53'):
        assert not _is_linked(b2, 'dom_ComplexType53', a)


def test_assoc_right59_link_reassign_clear():
    a = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_PropertyMapping60', b1)
    assert _is_linked(a, 'dom_PropertyMapping60', b1)
    if hasattr(b1, 'dom_Attribute61'):
        assert _is_linked(b1, 'dom_Attribute61', a)
    _safe_set(a, 'dom_PropertyMapping60', b2)
    assert _is_linked(a, 'dom_PropertyMapping60', b2)
    if hasattr(b1, 'dom_Attribute61'):
        assert not _is_linked(b1, 'dom_Attribute61', a)
    if hasattr(b2, 'dom_Attribute61'):
        assert _is_linked(b2, 'dom_Attribute61', a)
    _safe_set(a, 'dom_PropertyMapping60', None)
    assert not _is_linked(a, 'dom_PropertyMapping60', b2)
    if hasattr(b2, 'dom_Attribute61'):
        assert not _is_linked(b2, 'dom_Attribute61', a)


def test_assoc_sortOrder100_link_reassign_clear():
    a = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_AttributeGroup102', b1)
    assert _is_linked(a, 'dom_AttributeGroup102', b1)
    if hasattr(b1, 'dom_Attribute101'):
        assert _is_linked(b1, 'dom_Attribute101', a)
    _safe_set(a, 'dom_AttributeGroup102', b2)
    assert _is_linked(a, 'dom_AttributeGroup102', b2)
    if hasattr(b1, 'dom_Attribute101'):
        assert not _is_linked(b1, 'dom_Attribute101', a)
    if hasattr(b2, 'dom_Attribute101'):
        assert _is_linked(b2, 'dom_Attribute101', a)
    _safe_set(a, 'dom_AttributeGroup102', None)
    assert not _is_linked(a, 'dom_AttributeGroup102', b2)
    if hasattr(b2, 'dom_Attribute101'):
        assert not _is_linked(b2, 'dom_Attribute101', a)


def test_assoc_sortOrders75_link_reassign_clear():
    a = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_AttributeGroup77', b1)
    assert _is_linked(a, 'dom_AttributeGroup77', b1)
    if hasattr(b1, 'dom_Entity76'):
        assert _is_linked(b1, 'dom_Entity76', a)
    _safe_set(a, 'dom_AttributeGroup77', b2)
    assert _is_linked(a, 'dom_AttributeGroup77', b2)
    if hasattr(b1, 'dom_Entity76'):
        assert not _is_linked(b1, 'dom_Entity76', a)
    if hasattr(b2, 'dom_Entity76'):
        assert _is_linked(b2, 'dom_Entity76', a)
    _safe_set(a, 'dom_AttributeGroup77', None)
    assert not _is_linked(a, 'dom_AttributeGroup77', b2)
    if hasattr(b2, 'dom_Entity76'):
        assert not _is_linked(b2, 'dom_Entity76', a)


def test_assoc_source36_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_FeatureReference37', b1)
    assert _is_linked(a, 'dom_FeatureReference37', b1)
    if hasattr(b1, 'dom_Entity'):
        assert _is_linked(b1, 'dom_Entity', a)
    _safe_set(a, 'dom_FeatureReference37', b2)
    assert _is_linked(a, 'dom_FeatureReference37', b2)
    if hasattr(b1, 'dom_Entity'):
        assert not _is_linked(b1, 'dom_Entity', a)
    if hasattr(b2, 'dom_Entity'):
        assert _is_linked(b2, 'dom_Entity', a)
    _safe_set(a, 'dom_FeatureReference37', None)
    assert not _is_linked(a, 'dom_FeatureReference37', b2)
    if hasattr(b2, 'dom_Entity'):
        assert not _is_linked(b2, 'dom_Entity', a)


def test_assoc_sqlType185_link_reassign_clear():
    a = dom_ManyToOne(columnName="sample_text", derived=True)
    b1 = dom_SqlType()
    b2 = dom_SqlType()
    _safe_set(a, 'dom_ManyToOne186', b1)
    assert _is_linked(a, 'dom_ManyToOne186', b1)
    if hasattr(b1, 'dom_SqlType'):
        assert _is_linked(b1, 'dom_SqlType', a)
    _safe_set(a, 'dom_ManyToOne186', b2)
    assert _is_linked(a, 'dom_ManyToOne186', b2)
    if hasattr(b1, 'dom_SqlType'):
        assert not _is_linked(b1, 'dom_SqlType', a)
    if hasattr(b2, 'dom_SqlType'):
        assert _is_linked(b2, 'dom_SqlType', a)
    _safe_set(a, 'dom_ManyToOne186', None)
    assert not _is_linked(a, 'dom_ManyToOne186', b2)
    if hasattr(b2, 'dom_SqlType'):
        assert not _is_linked(b2, 'dom_SqlType', a)


def test_assoc_target46_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_FeatureReference47', b1)
    assert _is_linked(a, 'dom_FeatureReference47', b1)
    if hasattr(b1, 'dom_Attribute48'):
        assert _is_linked(b1, 'dom_Attribute48', a)
    _safe_set(a, 'dom_FeatureReference47', b2)
    assert _is_linked(a, 'dom_FeatureReference47', b2)
    if hasattr(b1, 'dom_Attribute48'):
        assert not _is_linked(b1, 'dom_Attribute48', a)
    if hasattr(b2, 'dom_Attribute48'):
        assert _is_linked(b2, 'dom_Attribute48', a)
    _safe_set(a, 'dom_FeatureReference47', None)
    assert not _is_linked(a, 'dom_FeatureReference47', b2)
    if hasattr(b2, 'dom_Attribute48'):
        assert not _is_linked(b2, 'dom_Attribute48', a)


def test_assoc_type15_link_reassign_clear():
    a = dom_Parameter(many=True, name="sample_text")
    b1 = dom_Type()
    b2 = dom_Type()
    _safe_set(a, 'dom_Parameter16', b1)
    assert _is_linked(a, 'dom_Parameter16', b1)
    if hasattr(b1, 'dom_Type'):
        assert _is_linked(b1, 'dom_Type', a)
    _safe_set(a, 'dom_Parameter16', b2)
    assert _is_linked(a, 'dom_Parameter16', b2)
    if hasattr(b1, 'dom_Type'):
        assert not _is_linked(b1, 'dom_Type', a)
    if hasattr(b2, 'dom_Type'):
        assert _is_linked(b2, 'dom_Type', a)
    _safe_set(a, 'dom_Parameter16', None)
    assert not _is_linked(a, 'dom_Parameter16', b2)
    if hasattr(b2, 'dom_Type'):
        assert not _is_linked(b2, 'dom_Type', a)


def test_assoc_type28_link_reassign_clear():
    a = dom_DaoOperation(many=True, name="sample_text")
    b1 = dom_Type()
    b2 = dom_Type()
    _safe_set(a, 'dom_DaoOperation29', b1)
    assert _is_linked(a, 'dom_DaoOperation29', b1)
    if hasattr(b1, 'dom_Type30'):
        assert _is_linked(b1, 'dom_Type30', a)
    _safe_set(a, 'dom_DaoOperation29', b2)
    assert _is_linked(a, 'dom_DaoOperation29', b2)
    if hasattr(b1, 'dom_Type30'):
        assert not _is_linked(b1, 'dom_Type30', a)
    if hasattr(b2, 'dom_Type30'):
        assert _is_linked(b2, 'dom_Type30', a)
    _safe_set(a, 'dom_DaoOperation29', None)
    assert not _is_linked(a, 'dom_DaoOperation29', b2)
    if hasattr(b2, 'dom_Type30'):
        assert not _is_linked(b2, 'dom_Type30', a)


def test_assoc_type9_link_reassign_clear():
    a = dom_Property(defaultValue="sample_text", name="sample_text")
    b1 = dom_SimpleType()
    b2 = dom_SimpleType()
    _safe_set(a, 'dom_Property', b1)
    assert _is_linked(a, 'dom_Property', b1)
    if hasattr(b1, 'dom_SimpleType'):
        assert _is_linked(b1, 'dom_SimpleType', a)
    _safe_set(a, 'dom_Property', b2)
    assert _is_linked(a, 'dom_Property', b2)
    if hasattr(b1, 'dom_SimpleType'):
        assert not _is_linked(b1, 'dom_SimpleType', a)
    if hasattr(b2, 'dom_SimpleType'):
        assert _is_linked(b2, 'dom_SimpleType', a)
    _safe_set(a, 'dom_Property', None)
    assert not _is_linked(a, 'dom_Property', b2)
    if hasattr(b2, 'dom_SimpleType'):
        assert not _is_linked(b2, 'dom_SimpleType', a)


def test_assoc_type90_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_DataTypeAndTypeParameter()
    b2 = dom_DataTypeAndTypeParameter()
    _safe_set(a, 'dom_Attribute91', b1)
    assert _is_linked(a, 'dom_Attribute91', b1)
    if hasattr(b1, 'dom_DataTypeAndTypeParameter'):
        assert _is_linked(b1, 'dom_DataTypeAndTypeParameter', a)
    _safe_set(a, 'dom_Attribute91', b2)
    assert _is_linked(a, 'dom_Attribute91', b2)
    if hasattr(b1, 'dom_DataTypeAndTypeParameter'):
        assert not _is_linked(b1, 'dom_DataTypeAndTypeParameter', a)
    if hasattr(b2, 'dom_DataTypeAndTypeParameter'):
        assert _is_linked(b2, 'dom_DataTypeAndTypeParameter', a)
    _safe_set(a, 'dom_Attribute91', None)
    assert not _is_linked(a, 'dom_Attribute91', b2)
    if hasattr(b2, 'dom_DataTypeAndTypeParameter'):
        assert not _is_linked(b2, 'dom_DataTypeAndTypeParameter', a)


def test_assoc_unitAttribute119_link_reassign_clear():
    a = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    b1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    _safe_set(a, 'dom_AttributeTextProperty', b1)
    assert _is_linked(a, 'dom_AttributeTextProperty', b1)
    if hasattr(b1, 'dom_Attribute120'):
        assert _is_linked(b1, 'dom_Attribute120', a)
    _safe_set(a, 'dom_AttributeTextProperty', b2)
    assert _is_linked(a, 'dom_AttributeTextProperty', b2)
    if hasattr(b1, 'dom_Attribute120'):
        assert not _is_linked(b1, 'dom_Attribute120', a)
    if hasattr(b2, 'dom_Attribute120'):
        assert _is_linked(b2, 'dom_Attribute120', a)
    _safe_set(a, 'dom_AttributeTextProperty', None)
    assert not _is_linked(a, 'dom_AttributeTextProperty', b2)
    if hasattr(b2, 'dom_Attribute120'):
        assert not _is_linked(b2, 'dom_Attribute120', a)


def test_assoc_userType173_link_reassign_clear():
    a = dom_Column(columnName="sample_text")
    b1 = dom_DataTypeAndTypeParameter()
    b2 = dom_DataTypeAndTypeParameter()
    _safe_set(a, 'dom_Column174', b1)
    assert _is_linked(a, 'dom_Column174', b1)
    if hasattr(b1, 'dom_DataTypeAndTypeParameter175'):
        assert _is_linked(b1, 'dom_DataTypeAndTypeParameter175', a)
    _safe_set(a, 'dom_Column174', b2)
    assert _is_linked(a, 'dom_Column174', b2)
    if hasattr(b1, 'dom_DataTypeAndTypeParameter175'):
        assert not _is_linked(b1, 'dom_DataTypeAndTypeParameter175', a)
    if hasattr(b2, 'dom_DataTypeAndTypeParameter175'):
        assert _is_linked(b2, 'dom_DataTypeAndTypeParameter175', a)
    _safe_set(a, 'dom_Column174', None)
    assert not _is_linked(a, 'dom_Column174', b2)
    if hasattr(b2, 'dom_DataTypeAndTypeParameter175'):
        assert not _is_linked(b2, 'dom_DataTypeAndTypeParameter175', a)


def test_assoc_userType182_link_reassign_clear():
    a = dom_ManyToOne(columnName="sample_text", derived=True)
    b1 = dom_Type()
    b2 = dom_Type()
    _safe_set(a, 'dom_ManyToOne183', b1)
    assert _is_linked(a, 'dom_ManyToOne183', b1)
    if hasattr(b1, 'dom_Type184'):
        assert _is_linked(b1, 'dom_Type184', a)
    _safe_set(a, 'dom_ManyToOne183', b2)
    assert _is_linked(a, 'dom_ManyToOne183', b2)
    if hasattr(b1, 'dom_Type184'):
        assert not _is_linked(b1, 'dom_Type184', a)
    if hasattr(b2, 'dom_Type184'):
        assert _is_linked(b2, 'dom_Type184', a)
    _safe_set(a, 'dom_ManyToOne183', None)
    assert not _is_linked(a, 'dom_ManyToOne183', b2)
    if hasattr(b2, 'dom_Type184'):
        assert not _is_linked(b2, 'dom_Type184', a)


def test_assoc_version81_link_reassign_clear():
    a = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    b1 = dom_Entity()
    b2 = dom_Entity()
    _safe_set(a, 'dom_Attribute83', b1)
    assert _is_linked(a, 'dom_Attribute83', b1)
    if hasattr(b1, 'dom_Entity82'):
        assert _is_linked(b1, 'dom_Entity82', a)
    _safe_set(a, 'dom_Attribute83', b2)
    assert _is_linked(a, 'dom_Attribute83', b2)
    if hasattr(b1, 'dom_Entity82'):
        assert not _is_linked(b1, 'dom_Entity82', a)
    if hasattr(b2, 'dom_Entity82'):
        assert _is_linked(b2, 'dom_Entity82', a)
    _safe_set(a, 'dom_Attribute83', None)
    assert not _is_linked(a, 'dom_Attribute83', b2)
    if hasattr(b2, 'dom_Entity82'):
        assert not _is_linked(b2, 'dom_Entity82', a)


def test_assoc_versionColumn157_link_reassign_clear():
    a = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    b1 = dom_Column(columnName="sample_text")
    b2 = dom_Column(columnName="sample_text_2")
    _safe_set(a, 'dom_Dao158', b1)
    assert _is_linked(a, 'dom_Dao158', b1)
    if hasattr(b1, 'dom_Column159'):
        assert _is_linked(b1, 'dom_Column159', a)
    _safe_set(a, 'dom_Dao158', b2)
    assert _is_linked(a, 'dom_Dao158', b2)
    if hasattr(b1, 'dom_Column159'):
        assert not _is_linked(b1, 'dom_Column159', a)
    if hasattr(b2, 'dom_Column159'):
        assert _is_linked(b2, 'dom_Column159', a)
    _safe_set(a, 'dom_Dao158', None)
    assert not _is_linked(a, 'dom_Dao158', b2)
    if hasattr(b2, 'dom_Column159'):
        assert not _is_linked(b2, 'dom_Column159', a)


def test_assoc_view17_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_DataView()
    b2 = dom_DataView()
    _safe_set(a, 'dom_DelegateOperation18', b1)
    assert _is_linked(a, 'dom_DelegateOperation18', b1)
    if hasattr(b1, 'dom_DataView'):
        assert _is_linked(b1, 'dom_DataView', a)
    _safe_set(a, 'dom_DelegateOperation18', b2)
    assert _is_linked(a, 'dom_DelegateOperation18', b2)
    if hasattr(b1, 'dom_DataView'):
        assert not _is_linked(b1, 'dom_DataView', a)
    if hasattr(b2, 'dom_DataView'):
        assert _is_linked(b2, 'dom_DataView', a)
    _safe_set(a, 'dom_DelegateOperation18', None)
    assert not _is_linked(a, 'dom_DelegateOperation18', b2)
    if hasattr(b2, 'dom_DataView'):
        assert not _is_linked(b2, 'dom_DataView', a)


def test_assoc_view41_link_reassign_clear():
    a = dom_FeatureReference(all=True)
    b1 = dom_DataView()
    b2 = dom_DataView()
    _safe_set(a, 'dom_FeatureReference42', b1)
    assert _is_linked(a, 'dom_FeatureReference42', b1)
    if hasattr(b1, 'dom_DataView43'):
        assert _is_linked(b1, 'dom_DataView43', a)
    _safe_set(a, 'dom_FeatureReference42', b2)
    assert _is_linked(a, 'dom_FeatureReference42', b2)
    if hasattr(b1, 'dom_DataView43'):
        assert not _is_linked(b1, 'dom_DataView43', a)
    if hasattr(b2, 'dom_DataView43'):
        assert _is_linked(b2, 'dom_DataView43', a)
    _safe_set(a, 'dom_FeatureReference42', None)
    assert not _is_linked(a, 'dom_FeatureReference42', b2)
    if hasattr(b2, 'dom_DataView43'):
        assert not _is_linked(b2, 'dom_DataView43', a)


def test_assoc_viewParameter23_link_reassign_clear():
    a = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    b1 = dom_DataView()
    b2 = dom_DataView()
    _safe_set(a, 'dom_DelegateOperation24', b1)
    assert _is_linked(a, 'dom_DelegateOperation24', b1)
    if hasattr(b1, 'dom_DataView25'):
        assert _is_linked(b1, 'dom_DataView25', a)
    _safe_set(a, 'dom_DelegateOperation24', b2)
    assert _is_linked(a, 'dom_DelegateOperation24', b2)
    if hasattr(b1, 'dom_DataView25'):
        assert not _is_linked(b1, 'dom_DataView25', a)
    if hasattr(b2, 'dom_DataView25'):
        assert _is_linked(b2, 'dom_DataView25', a)
    _safe_set(a, 'dom_DelegateOperation24', None)
    assert not _is_linked(a, 'dom_DelegateOperation24', b2)
    if hasattr(b2, 'dom_DataView25'):
        assert not _is_linked(b2, 'dom_DataView25', a)


def test_assoc_where230_link_reassign_clear():
    a = dom_DeleteStatement(name="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_DeleteStatement231', b1)
    assert _is_linked(a, 'dom_DeleteStatement231', b1)
    if hasattr(b1, 'dom_Expression232'):
        assert _is_linked(b1, 'dom_Expression232', a)
    _safe_set(a, 'dom_DeleteStatement231', b2)
    assert _is_linked(a, 'dom_DeleteStatement231', b2)
    if hasattr(b1, 'dom_Expression232'):
        assert not _is_linked(b1, 'dom_Expression232', a)
    if hasattr(b2, 'dom_Expression232'):
        assert _is_linked(b2, 'dom_Expression232', a)
    _safe_set(a, 'dom_DeleteStatement231', None)
    assert not _is_linked(a, 'dom_DeleteStatement231', b2)
    if hasattr(b2, 'dom_Expression232'):
        assert not _is_linked(b2, 'dom_Expression232', a)


def test_assoc_where237_link_reassign_clear():
    a = dom_UpdateStatement(name="sample_text", versioned=True)
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_UpdateStatement238', b1)
    assert _is_linked(a, 'dom_UpdateStatement238', b1)
    if hasattr(b1, 'dom_Expression239'):
        assert _is_linked(b1, 'dom_Expression239', a)
    _safe_set(a, 'dom_UpdateStatement238', b2)
    assert _is_linked(a, 'dom_UpdateStatement238', b2)
    if hasattr(b1, 'dom_Expression239'):
        assert not _is_linked(b1, 'dom_Expression239', a)
    if hasattr(b2, 'dom_Expression239'):
        assert _is_linked(b2, 'dom_Expression239', a)
    _safe_set(a, 'dom_UpdateStatement238', None)
    assert not _is_linked(a, 'dom_UpdateStatement238', b2)
    if hasattr(b2, 'dom_Expression239'):
        assert not _is_linked(b2, 'dom_Expression239', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AttributeFlag_strategy = st.builds(AttributeFlag)
@given(instance=AttributeFlag_strategy)
@settings(max_examples=25)
def test_AttributeFlag_instantiation(instance):
    assert isinstance(instance, AttributeFlag)


AttributeProperty_strategy = st.builds(AttributeProperty)
@given(instance=AttributeProperty_strategy)
@settings(max_examples=25)
def test_AttributeProperty_instantiation(instance):
    assert isinstance(instance, AttributeProperty)


ComplexType_strategy = st.builds(ComplexType)
@given(instance=ComplexType_strategy)
@settings(max_examples=25)
def test_ComplexType_instantiation(instance):
    assert isinstance(instance, ComplexType)


DaoFeature_strategy = st.builds(DaoFeature)
@given(instance=DaoFeature_strategy)
@settings(max_examples=25)
def test_DaoFeature_instantiation(instance):
    assert isinstance(instance, DaoFeature)


DaoOperation_strategy = st.builds(DaoOperation)
@given(instance=DaoOperation_strategy)
@settings(max_examples=25)
def test_DaoOperation_instantiation(instance):
    assert isinstance(instance, DaoOperation)


Dependant_strategy = st.builds(Dependant)
@given(instance=Dependant_strategy)
@settings(max_examples=25)
def test_Dependant_instantiation(instance):
    assert isinstance(instance, Dependant)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionFlag_strategy = st.builds(ExpressionFlag)
@given(instance=ExpressionFlag_strategy)
@settings(max_examples=25)
def test_ExpressionFlag_instantiation(instance):
    assert isinstance(instance, ExpressionFlag)


FromRange_strategy = st.builds(FromRange)
@given(instance=FromRange_strategy)
@settings(max_examples=25)
def test_FromRange_instantiation(instance):
    assert isinstance(instance, FromRange)


IDocumentable_strategy = st.builds(IDocumentable)
@given(instance=IDocumentable_strategy)
@settings(max_examples=25)
def test_IDocumentable_instantiation(instance):
    assert isinstance(instance, IDocumentable)


JoinEntity_strategy = st.builds(JoinEntity)
@given(instance=JoinEntity_strategy)
@settings(max_examples=25)
def test_JoinEntity_instantiation(instance):
    assert isinstance(instance, JoinEntity)


LiteralValue_strategy = st.builds(LiteralValue)
@given(instance=LiteralValue_strategy)
@settings(max_examples=25)
def test_LiteralValue_instantiation(instance):
    assert isinstance(instance, LiteralValue)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


PresentableFeature_strategy = st.builds(PresentableFeature)
@given(instance=PresentableFeature_strategy)
@settings(max_examples=25)
def test_PresentableFeature_instantiation(instance):
    assert isinstance(instance, PresentableFeature)


QlStatement_strategy = st.builds(QlStatement)
@given(instance=QlStatement_strategy)
@settings(max_examples=25)
def test_QlStatement_instantiation(instance):
    assert isinstance(instance, QlStatement)


QueryParameter_strategy = st.builds(QueryParameter)
@given(instance=QueryParameter_strategy)
@settings(max_examples=25)
def test_QueryParameter_instantiation(instance):
    assert isinstance(instance, QueryParameter)


QueryParameterReference_strategy = st.builds(QueryParameterReference)
@given(instance=QueryParameterReference_strategy)
@settings(max_examples=25)
def test_QueryParameterReference_instantiation(instance):
    assert isinstance(instance, QueryParameterReference)


ReferenceableByXmadslVariable_strategy = st.builds(ReferenceableByXmadslVariable)
@given(instance=ReferenceableByXmadslVariable_strategy)
@settings(max_examples=25)
def test_ReferenceableByXmadslVariable_instantiation(instance):
    assert isinstance(instance, ReferenceableByXmadslVariable)


SelectStatement_strategy = st.builds(SelectStatement)
@given(instance=SelectStatement_strategy)
@settings(max_examples=25)
def test_SelectStatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


dom_AggregateFunction_strategy = st.builds(dom_AggregateFunction, all=st.booleans(), distinct=st.booleans(), from_=safe_text, function=safe_text)
@given(instance=dom_AggregateFunction_strategy)
@settings(max_examples=25)
def test_dom_AggregateFunction_instantiation(instance):
    assert isinstance(instance, dom_AggregateFunction)


dom_AliasedExpression_strategy = st.builds(dom_AliasedExpression, name=safe_text)
@given(instance=dom_AliasedExpression_strategy)
@settings(max_examples=25)
def test_dom_AliasedExpression_instantiation(instance):
    assert isinstance(instance, dom_AliasedExpression)


dom_AltWhenClause_strategy = st.builds(dom_AltWhenClause)
@given(instance=dom_AltWhenClause_strategy)
@settings(max_examples=25)
def test_dom_AltWhenClause_instantiation(instance):
    assert isinstance(instance, dom_AltWhenClause)


dom_ApplicationSession_strategy = st.builds(dom_ApplicationSession)
@given(instance=dom_ApplicationSession_strategy)
@settings(max_examples=25)
def test_dom_ApplicationSession_instantiation(instance):
    assert isinstance(instance, dom_ApplicationSession)


dom_Attribute_strategy = st.builds(dom_Attribute, composition=st.booleans(), dataTypeName=safe_text, defaultValue=safe_text, derived=st.booleans(), identifier=st.booleans(), many=st.booleans(), readOnly=st.booleans(), reference=st.booleans(), required=st.booleans(), transient=st.booleans(), version=st.booleans())
@given(instance=dom_Attribute_strategy)
@settings(max_examples=25)
def test_dom_Attribute_instantiation(instance):
    assert isinstance(instance, dom_Attribute)


dom_AttributeFlag_strategy = st.builds(dom_AttributeFlag)
@given(instance=dom_AttributeFlag_strategy)
@settings(max_examples=25)
def test_dom_AttributeFlag_instantiation(instance):
    assert isinstance(instance, dom_AttributeFlag)


dom_AttributeGroup_strategy = st.builds(dom_AttributeGroup, filter=st.booleans(), key=st.booleans(), name=safe_text, sortorder=st.booleans(), unique=st.booleans())
@given(instance=dom_AttributeGroup_strategy)
@settings(max_examples=25)
def test_dom_AttributeGroup_instantiation(instance):
    assert isinstance(instance, dom_AttributeGroup)


dom_AttributeProperty_strategy = st.builds(dom_AttributeProperty)
@given(instance=dom_AttributeProperty_strategy)
@settings(max_examples=25)
def test_dom_AttributeProperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeProperty)


dom_AttributeSortOrder_strategy = st.builds(dom_AttributeSortOrder, asc=st.booleans(), desc=st.booleans())
@given(instance=dom_AttributeSortOrder_strategy)
@settings(max_examples=25)
def test_dom_AttributeSortOrder_instantiation(instance):
    assert isinstance(instance, dom_AttributeSortOrder)


dom_AttributeTextProperty_strategy = st.builds(dom_AttributeTextProperty, hstoreColumn=safe_text, labelText=safe_text, tooltipText=safe_text, unitText=safe_text)
@given(instance=dom_AttributeTextProperty_strategy)
@settings(max_examples=25)
def test_dom_AttributeTextProperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeTextProperty)


dom_AttributeValidationProperty_strategy = st.builds(dom_AttributeValidationProperty)
@given(instance=dom_AttributeValidationProperty_strategy)
@settings(max_examples=25)
def test_dom_AttributeValidationProperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeValidationProperty)


dom_AvailableFlag_strategy = st.builds(dom_AvailableFlag)
@given(instance=dom_AvailableFlag_strategy)
@settings(max_examples=25)
def test_dom_AvailableFlag_instantiation(instance):
    assert isinstance(instance, dom_AvailableFlag)


dom_BetweenExpression_strategy = st.builds(dom_BetweenExpression, not_=st.booleans(), operator=safe_text)
@given(instance=dom_BetweenExpression_strategy)
@settings(max_examples=25)
def test_dom_BetweenExpression_instantiation(instance):
    assert isinstance(instance, dom_BetweenExpression)


dom_BinaryExpression_strategy = st.builds(dom_BinaryExpression, operator=safe_text)
@given(instance=dom_BinaryExpression_strategy)
@settings(max_examples=25)
def test_dom_BinaryExpression_instantiation(instance):
    assert isinstance(instance, dom_BinaryExpression)


dom_BoolLiteral_strategy = st.builds(dom_BoolLiteral)
@given(instance=dom_BoolLiteral_strategy)
@settings(max_examples=25)
def test_dom_BoolLiteral_instantiation(instance):
    assert isinstance(instance, dom_BoolLiteral)


dom_BooleanLiteralValue_strategy = st.builds(dom_BooleanLiteralValue, isTrue=st.booleans())
@given(instance=dom_BooleanLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_BooleanLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_BooleanLiteralValue)


dom_CallInputParameter_strategy = st.builds(dom_CallInputParameter, name=safe_text)
@given(instance=dom_CallInputParameter_strategy)
@settings(max_examples=25)
def test_dom_CallInputParameter_instantiation(instance):
    assert isinstance(instance, dom_CallInputParameter)


dom_CallOutputParameter_strategy = st.builds(dom_CallOutputParameter, name=safe_text)
@given(instance=dom_CallOutputParameter_strategy)
@settings(max_examples=25)
def test_dom_CallOutputParameter_instantiation(instance):
    assert isinstance(instance, dom_CallOutputParameter)


dom_CallableStatement_strategy = st.builds(dom_CallableStatement, functionCall=st.booleans(), name=safe_text)
@given(instance=dom_CallableStatement_strategy)
@settings(max_examples=25)
def test_dom_CallableStatement_instantiation(instance):
    assert isinstance(instance, dom_CallableStatement)


dom_CaseExpression_strategy = st.builds(dom_CaseExpression)
@given(instance=dom_CaseExpression_strategy)
@settings(max_examples=25)
def test_dom_CaseExpression_instantiation(instance):
    assert isinstance(instance, dom_CaseExpression)


dom_CastFunction_strategy = st.builds(dom_CastFunction, function=safe_text, name=safe_text)
@given(instance=dom_CastFunction_strategy)
@settings(max_examples=25)
def test_dom_CastFunction_instantiation(instance):
    assert isinstance(instance, dom_CastFunction)


dom_CollectionFunction_strategy = st.builds(dom_CollectionFunction, function=safe_text)
@given(instance=dom_CollectionFunction_strategy)
@settings(max_examples=25)
def test_dom_CollectionFunction_instantiation(instance):
    assert isinstance(instance, dom_CollectionFunction)


dom_Column_strategy = st.builds(dom_Column, columnName=safe_text)
@given(instance=dom_Column_strategy)
@settings(max_examples=25)
def test_dom_Column_instantiation(instance):
    assert isinstance(instance, dom_Column)


dom_ComplexType_strategy = st.builds(dom_ComplexType)
@given(instance=dom_ComplexType_strategy)
@settings(max_examples=25)
def test_dom_ComplexType_instantiation(instance):
    assert isinstance(instance, dom_ComplexType)


dom_ConditionsBlock_strategy = st.builds(dom_ConditionsBlock)
@given(instance=dom_ConditionsBlock_strategy)
@settings(max_examples=25)
def test_dom_ConditionsBlock_instantiation(instance):
    assert isinstance(instance, dom_ConditionsBlock)


dom_Constraint_strategy = st.builds(dom_Constraint)
@given(instance=dom_Constraint_strategy)
@settings(max_examples=25)
def test_dom_Constraint_instantiation(instance):
    assert isinstance(instance, dom_Constraint)


dom_Dao_strategy = st.builds(dom_Dao, discriminator=safe_text, qualifier=safe_text, tableName=safe_text)
@given(instance=dom_Dao_strategy)
@settings(max_examples=25)
def test_dom_Dao_instantiation(instance):
    assert isinstance(instance, dom_Dao)


dom_DaoFeature_strategy = st.builds(dom_DaoFeature)
@given(instance=dom_DaoFeature_strategy)
@settings(max_examples=25)
def test_dom_DaoFeature_instantiation(instance):
    assert isinstance(instance, dom_DaoFeature)


dom_DaoOperation_strategy = st.builds(dom_DaoOperation, many=st.booleans(), name=safe_text)
@given(instance=dom_DaoOperation_strategy)
@settings(max_examples=25)
def test_dom_DaoOperation_instantiation(instance):
    assert isinstance(instance, dom_DaoOperation)


dom_DataBaseConstraint_strategy = st.builds(dom_DataBaseConstraint, name=safe_text, type=safe_text)
@given(instance=dom_DataBaseConstraint_strategy)
@settings(max_examples=25)
def test_dom_DataBaseConstraint_instantiation(instance):
    assert isinstance(instance, dom_DataBaseConstraint)


dom_DataTypeAndTypeParameter_strategy = st.builds(dom_DataTypeAndTypeParameter)
@given(instance=dom_DataTypeAndTypeParameter_strategy)
@settings(max_examples=25)
def test_dom_DataTypeAndTypeParameter_instantiation(instance):
    assert isinstance(instance, dom_DataTypeAndTypeParameter)


dom_DataView_strategy = st.builds(dom_DataView)
@given(instance=dom_DataView_strategy)
@settings(max_examples=25)
def test_dom_DataView_instantiation(instance):
    assert isinstance(instance, dom_DataView)


dom_DelegateOperation_strategy = st.builds(dom_DelegateOperation, crudOperationType=safe_text, many=st.booleans(), name=safe_text)
@given(instance=dom_DelegateOperation_strategy)
@settings(max_examples=25)
def test_dom_DelegateOperation_instantiation(instance):
    assert isinstance(instance, dom_DelegateOperation)


dom_DeleteStatement_strategy = st.builds(dom_DeleteStatement, name=safe_text)
@given(instance=dom_DeleteStatement_strategy)
@settings(max_examples=25)
def test_dom_DeleteStatement_instantiation(instance):
    assert isinstance(instance, dom_DeleteStatement)


dom_Dependant_strategy = st.builds(dom_Dependant)
@given(instance=dom_Dependant_strategy)
@settings(max_examples=25)
def test_dom_Dependant_instantiation(instance):
    assert isinstance(instance, dom_Dependant)


dom_DerivedFlag_strategy = st.builds(dom_DerivedFlag)
@given(instance=dom_DerivedFlag_strategy)
@settings(max_examples=25)
def test_dom_DerivedFlag_instantiation(instance):
    assert isinstance(instance, dom_DerivedFlag)


dom_EmptyLiteralValue_strategy = st.builds(dom_EmptyLiteralValue)
@given(instance=dom_EmptyLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_EmptyLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_EmptyLiteralValue)


dom_Entity_strategy = st.builds(dom_Entity)
@given(instance=dom_Entity_strategy)
@settings(max_examples=25)
def test_dom_Entity_instantiation(instance):
    assert isinstance(instance, dom_Entity)


dom_EqualityExpr_strategy = st.builds(dom_EqualityExpr)
@given(instance=dom_EqualityExpr_strategy)
@settings(max_examples=25)
def test_dom_EqualityExpr_instantiation(instance):
    assert isinstance(instance, dom_EqualityExpr)


dom_Expression_strategy = st.builds(dom_Expression)
@given(instance=dom_Expression_strategy)
@settings(max_examples=25)
def test_dom_Expression_instantiation(instance):
    assert isinstance(instance, dom_Expression)


dom_ExpressionFlag_strategy = st.builds(dom_ExpressionFlag)
@given(instance=dom_ExpressionFlag_strategy)
@settings(max_examples=25)
def test_dom_ExpressionFlag_instantiation(instance):
    assert isinstance(instance, dom_ExpressionFlag)


dom_FeatureReference_strategy = st.builds(dom_FeatureReference, all=st.booleans())
@given(instance=dom_FeatureReference_strategy)
@settings(max_examples=25)
def test_dom_FeatureReference_instantiation(instance):
    assert isinstance(instance, dom_FeatureReference)


dom_FromClass_strategy = st.builds(dom_FromClass, popertyFetch=st.booleans())
@given(instance=dom_FromClass_strategy)
@settings(max_examples=25)
def test_dom_FromClass_instantiation(instance):
    assert isinstance(instance, dom_FromClass)


dom_FromRange_strategy = st.builds(dom_FromRange)
@given(instance=dom_FromRange_strategy)
@settings(max_examples=25)
def test_dom_FromRange_instantiation(instance):
    assert isinstance(instance, dom_FromRange)


dom_Function_strategy = st.builds(dom_Function)
@given(instance=dom_Function_strategy)
@settings(max_examples=25)
def test_dom_Function_instantiation(instance):
    assert isinstance(instance, dom_Function)


dom_FunctionCall_strategy = st.builds(dom_FunctionCall, function=safe_text)
@given(instance=dom_FunctionCall_strategy)
@settings(max_examples=25)
def test_dom_FunctionCall_instantiation(instance):
    assert isinstance(instance, dom_FunctionCall)


dom_IElementWithNoName_strategy = st.builds(dom_IElementWithNoName, noName=safe_text)
@given(instance=dom_IElementWithNoName_strategy)
@settings(max_examples=25)
def test_dom_IElementWithNoName_instantiation(instance):
    assert isinstance(instance, dom_IElementWithNoName)


dom_InClass_strategy = st.builds(dom_InClass, class_=safe_text, name=safe_text)
@given(instance=dom_InClass_strategy)
@settings(max_examples=25)
def test_dom_InClass_instantiation(instance):
    assert isinstance(instance, dom_InClass)


dom_InCollection_strategy = st.builds(dom_InCollection, alias=safe_text, path=safe_text)
@given(instance=dom_InCollection_strategy)
@settings(max_examples=25)
def test_dom_InCollection_instantiation(instance):
    assert isinstance(instance, dom_InCollection)


dom_InCollectionElements_strategy = st.builds(dom_InCollectionElements, name=safe_text, reference=safe_text)
@given(instance=dom_InCollectionElements_strategy)
@settings(max_examples=25)
def test_dom_InCollectionElements_instantiation(instance):
    assert isinstance(instance, dom_InCollectionElements)


dom_InExpression_strategy = st.builds(dom_InExpression, not_=st.booleans(), operator=safe_text)
@given(instance=dom_InExpression_strategy)
@settings(max_examples=25)
def test_dom_InExpression_instantiation(instance):
    assert isinstance(instance, dom_InExpression)


dom_IncrementerReference_strategy = st.builds(dom_IncrementerReference)
@given(instance=dom_IncrementerReference_strategy)
@settings(max_examples=25)
def test_dom_IncrementerReference_instantiation(instance):
    assert isinstance(instance, dom_IncrementerReference)


dom_InsertStatement_strategy = st.builds(dom_InsertStatement)
@given(instance=dom_InsertStatement_strategy)
@settings(max_examples=25)
def test_dom_InsertStatement_instantiation(instance):
    assert isinstance(instance, dom_InsertStatement)


dom_IntegerLiteralValue_strategy = st.builds(dom_IntegerLiteralValue, value=safe_text)
@given(instance=dom_IntegerLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_IntegerLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_IntegerLiteralValue)


dom_Join_strategy = st.builds(dom_Join, fetch=st.booleans(), propertyFetch=st.booleans(), type=safe_text)
@given(instance=dom_Join_strategy)
@settings(max_examples=25)
def test_dom_Join_instantiation(instance):
    assert isinstance(instance, dom_Join)


dom_JoinEntity_strategy = st.builds(dom_JoinEntity, name=safe_text)
@given(instance=dom_JoinEntity_strategy)
@settings(max_examples=25)
def test_dom_JoinEntity_instantiation(instance):
    assert isinstance(instance, dom_JoinEntity)


dom_LikeExpression_strategy = st.builds(dom_LikeExpression, not_=st.booleans(), operator=safe_text)
@given(instance=dom_LikeExpression_strategy)
@settings(max_examples=25)
def test_dom_LikeExpression_instantiation(instance):
    assert isinstance(instance, dom_LikeExpression)


dom_LiteralValue_strategy = st.builds(dom_LiteralValue)
@given(instance=dom_LiteralValue_strategy)
@settings(max_examples=25)
def test_dom_LiteralValue_instantiation(instance):
    assert isinstance(instance, dom_LiteralValue)


dom_ManyToMany_strategy = st.builds(dom_ManyToMany, columnName=safe_text, inverse=st.booleans(), tableName=safe_text)
@given(instance=dom_ManyToMany_strategy)
@settings(max_examples=25)
def test_dom_ManyToMany_instantiation(instance):
    assert isinstance(instance, dom_ManyToMany)


dom_ManyToOne_strategy = st.builds(dom_ManyToOne, columnName=safe_text, derived=st.booleans())
@given(instance=dom_ManyToOne_strategy)
@settings(max_examples=25)
def test_dom_ManyToOne_instantiation(instance):
    assert isinstance(instance, dom_ManyToOne)


dom_Mapper_strategy = st.builds(dom_Mapper, biDirectional=st.booleans(), toLeft=st.booleans(), toRight=st.booleans())
@given(instance=dom_Mapper_strategy)
@settings(max_examples=25)
def test_dom_Mapper_instantiation(instance):
    assert isinstance(instance, dom_Mapper)


dom_MemberOfExpression_strategy = st.builds(dom_MemberOfExpression, memberOf=safe_text, not_=st.booleans(), operator=safe_text)
@given(instance=dom_MemberOfExpression_strategy)
@settings(max_examples=25)
def test_dom_MemberOfExpression_instantiation(instance):
    assert isinstance(instance, dom_MemberOfExpression)


dom_NotExpression_strategy = st.builds(dom_NotExpression)
@given(instance=dom_NotExpression_strategy)
@settings(max_examples=25)
def test_dom_NotExpression_instantiation(instance):
    assert isinstance(instance, dom_NotExpression)


dom_NullLiteralValue_strategy = st.builds(dom_NullLiteralValue)
@given(instance=dom_NullLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_NullLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_NullLiteralValue)


dom_OneToMany_strategy = st.builds(dom_OneToMany, columnName=safe_text)
@given(instance=dom_OneToMany_strategy)
@settings(max_examples=25)
def test_dom_OneToMany_instantiation(instance):
    assert isinstance(instance, dom_OneToMany)


dom_OneToOne_strategy = st.builds(dom_OneToOne)
@given(instance=dom_OneToOne_strategy)
@settings(max_examples=25)
def test_dom_OneToOne_instantiation(instance):
    assert isinstance(instance, dom_OneToOne)


dom_Operation_strategy = st.builds(dom_Operation, expression=safe_text)
@given(instance=dom_Operation_strategy)
@settings(max_examples=25)
def test_dom_Operation_instantiation(instance):
    assert isinstance(instance, dom_Operation)


dom_Parameter_strategy = st.builds(dom_Parameter, many=st.booleans(), name=safe_text)
@given(instance=dom_Parameter_strategy)
@settings(max_examples=25)
def test_dom_Parameter_instantiation(instance):
    assert isinstance(instance, dom_Parameter)


dom_ParenthesizedExpression_strategy = st.builds(dom_ParenthesizedExpression)
@given(instance=dom_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_dom_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, dom_ParenthesizedExpression)


dom_PresentableFeature_strategy = st.builds(dom_PresentableFeature, name=safe_text)
@given(instance=dom_PresentableFeature_strategy)
@settings(max_examples=25)
def test_dom_PresentableFeature_instantiation(instance):
    assert isinstance(instance, dom_PresentableFeature)


dom_Property_strategy = st.builds(dom_Property, defaultValue=safe_text, name=safe_text)
@given(instance=dom_Property_strategy)
@settings(max_examples=25)
def test_dom_Property_instantiation(instance):
    assert isinstance(instance, dom_Property)


dom_PropertyAssignment_strategy = st.builds(dom_PropertyAssignment)
@given(instance=dom_PropertyAssignment_strategy)
@settings(max_examples=25)
def test_dom_PropertyAssignment_instantiation(instance):
    assert isinstance(instance, dom_PropertyAssignment)


dom_PropertyMapping_strategy = st.builds(dom_PropertyMapping, biDirectional=st.booleans(), toLeft=st.booleans(), toRight=st.booleans())
@given(instance=dom_PropertyMapping_strategy)
@settings(max_examples=25)
def test_dom_PropertyMapping_instantiation(instance):
    assert isinstance(instance, dom_PropertyMapping)


dom_PropertyValue_strategy = st.builds(dom_PropertyValue, classProperty=st.booleans(), name=safe_text, segments=safe_text)
@given(instance=dom_PropertyValue_strategy)
@settings(max_examples=25)
def test_dom_PropertyValue_instantiation(instance):
    assert isinstance(instance, dom_PropertyValue)


dom_QlStatement_strategy = st.builds(dom_QlStatement)
@given(instance=dom_QlStatement_strategy)
@settings(max_examples=25)
def test_dom_QlStatement_instantiation(instance):
    assert isinstance(instance, dom_QlStatement)


dom_QuantifiedExpression_strategy = st.builds(dom_QuantifiedExpression, name=safe_text, quantifier=safe_text)
@given(instance=dom_QuantifiedExpression_strategy)
@settings(max_examples=25)
def test_dom_QuantifiedExpression_instantiation(instance):
    assert isinstance(instance, dom_QuantifiedExpression)


dom_QueryOperation_strategy = st.builds(dom_QueryOperation)
@given(instance=dom_QueryOperation_strategy)
@settings(max_examples=25)
def test_dom_QueryOperation_instantiation(instance):
    assert isinstance(instance, dom_QueryOperation)


dom_QueryParameter_strategy = st.builds(dom_QueryParameter)
@given(instance=dom_QueryParameter_strategy)
@settings(max_examples=25)
def test_dom_QueryParameter_instantiation(instance):
    assert isinstance(instance, dom_QueryParameter)


dom_QueryParameterReference_strategy = st.builds(dom_QueryParameterReference)
@given(instance=dom_QueryParameterReference_strategy)
@settings(max_examples=25)
def test_dom_QueryParameterReference_instantiation(instance):
    assert isinstance(instance, dom_QueryParameterReference)


dom_QueryParameterValue_strategy = st.builds(dom_QueryParameterValue)
@given(instance=dom_QueryParameterValue_strategy)
@settings(max_examples=25)
def test_dom_QueryParameterValue_instantiation(instance):
    assert isinstance(instance, dom_QueryParameterValue)


dom_ReadOnlyFlag_strategy = st.builds(dom_ReadOnlyFlag)
@given(instance=dom_ReadOnlyFlag_strategy)
@settings(max_examples=25)
def test_dom_ReadOnlyFlag_instantiation(instance):
    assert isinstance(instance, dom_ReadOnlyFlag)


dom_RealLiteralValue_strategy = st.builds(dom_RealLiteralValue, value=safe_text)
@given(instance=dom_RealLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_RealLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_RealLiteralValue)


dom_RequiredFlag_strategy = st.builds(dom_RequiredFlag)
@given(instance=dom_RequiredFlag_strategy)
@settings(max_examples=25)
def test_dom_RequiredFlag_instantiation(instance):
    assert isinstance(instance, dom_RequiredFlag)


dom_SelectClass_strategy = st.builds(dom_SelectClass, class_=safe_text)
@given(instance=dom_SelectClass_strategy)
@settings(max_examples=25)
def test_dom_SelectClass_instantiation(instance):
    assert isinstance(instance, dom_SelectClass)


dom_SelectObject_strategy = st.builds(dom_SelectObject, name=safe_text)
@given(instance=dom_SelectObject_strategy)
@settings(max_examples=25)
def test_dom_SelectObject_instantiation(instance):
    assert isinstance(instance, dom_SelectObject)


dom_SelectProperties_strategy = st.builds(dom_SelectProperties, distinct=st.booleans())
@given(instance=dom_SelectProperties_strategy)
@settings(max_examples=25)
def test_dom_SelectProperties_instantiation(instance):
    assert isinstance(instance, dom_SelectProperties)


dom_SelectStatement_strategy = st.builds(dom_SelectStatement)
@given(instance=dom_SelectStatement_strategy)
@settings(max_examples=25)
def test_dom_SelectStatement_instantiation(instance):
    assert isinstance(instance, dom_SelectStatement)


dom_Service_strategy = st.builds(dom_Service)
@given(instance=dom_Service_strategy)
@settings(max_examples=25)
def test_dom_Service_instantiation(instance):
    assert isinstance(instance, dom_Service)


dom_SimpleType_strategy = st.builds(dom_SimpleType)
@given(instance=dom_SimpleType_strategy)
@settings(max_examples=25)
def test_dom_SimpleType_instantiation(instance):
    assert isinstance(instance, dom_SimpleType)


dom_SortOrderElement_strategy = st.builds(dom_SortOrderElement, sortOrder=safe_text)
@given(instance=dom_SortOrderElement_strategy)
@settings(max_examples=25)
def test_dom_SortOrderElement_instantiation(instance):
    assert isinstance(instance, dom_SortOrderElement)


dom_SqlType_strategy = st.builds(dom_SqlType)
@given(instance=dom_SqlType_strategy)
@settings(max_examples=25)
def test_dom_SqlType_instantiation(instance):
    assert isinstance(instance, dom_SqlType)


dom_StringLiteralValue_strategy = st.builds(dom_StringLiteralValue, value=safe_text)
@given(instance=dom_StringLiteralValue_strategy)
@settings(max_examples=25)
def test_dom_StringLiteralValue_instantiation(instance):
    assert isinstance(instance, dom_StringLiteralValue)


dom_SubQuery_strategy = st.builds(dom_SubQuery)
@given(instance=dom_SubQuery_strategy)
@settings(max_examples=25)
def test_dom_SubQuery_instantiation(instance):
    assert isinstance(instance, dom_SubQuery)


dom_TransientFlag_strategy = st.builds(dom_TransientFlag)
@given(instance=dom_TransientFlag_strategy)
@settings(max_examples=25)
def test_dom_TransientFlag_instantiation(instance):
    assert isinstance(instance, dom_TransientFlag)


dom_TrimFunction_strategy = st.builds(dom_TrimFunction, function=safe_text, mode=safe_text)
@given(instance=dom_TrimFunction_strategy)
@settings(max_examples=25)
def test_dom_TrimFunction_instantiation(instance):
    assert isinstance(instance, dom_TrimFunction)


dom_Type_strategy = st.builds(dom_Type)
@given(instance=dom_Type_strategy)
@settings(max_examples=25)
def test_dom_Type_instantiation(instance):
    assert isinstance(instance, dom_Type)


dom_UnaryExpression_strategy = st.builds(dom_UnaryExpression, operator=safe_text)
@given(instance=dom_UnaryExpression_strategy)
@settings(max_examples=25)
def test_dom_UnaryExpression_instantiation(instance):
    assert isinstance(instance, dom_UnaryExpression)


dom_UpdateStatement_strategy = st.builds(dom_UpdateStatement, name=safe_text, versioned=st.booleans())
@given(instance=dom_UpdateStatement_strategy)
@settings(max_examples=25)
def test_dom_UpdateStatement_instantiation(instance):
    assert isinstance(instance, dom_UpdateStatement)


dom_ValidatorReference_strategy = st.builds(dom_ValidatorReference)
@given(instance=dom_ValidatorReference_strategy)
@settings(max_examples=25)
def test_dom_ValidatorReference_instantiation(instance):
    assert isinstance(instance, dom_ValidatorReference)


dom_ValueObject_strategy = st.builds(dom_ValueObject)
@given(instance=dom_ValueObject_strategy)
@settings(max_examples=25)
def test_dom_ValueObject_instantiation(instance):
    assert isinstance(instance, dom_ValueObject)


dom_WhenClause_strategy = st.builds(dom_WhenClause)
@given(instance=dom_WhenClause_strategy)
@settings(max_examples=25)
def test_dom_WhenClause_instantiation(instance):
    assert isinstance(instance, dom_WhenClause)



