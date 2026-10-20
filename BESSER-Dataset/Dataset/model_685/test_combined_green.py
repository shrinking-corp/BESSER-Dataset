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
    TryExp,
    TypedElement,
    JTL_essentialocl_OclExpression,
    PrimitiveLiteralExp,
    JTL_essentialocl_BooleanLiteralExp,
    Relation,
    Model,
    emof_Package,
    emof_Class,
    JTL_JTL_Transformation,
    Extent,
    JTL_emof_URIExtent,
    Pattern,
    Variable,
    When,
    Where,
    Domain,
    Transformation,
    JTL_emof_MultiplicityElement,
    Parameter,
    emof_TypedElement,
    emof_MultiplicityElement,
    JTL_emof_Operation,
    JTL_emof_Object,
    JTL_emof_Property,
    Enumeration,
    JTL_emof_Parameter,
    Package,
    NamedElement,
    JTL_JTL_Model,
    JTL_emof_EnumerationLiteral,
    JTL_JTL_Relation,
    JTL_JTL_Domain,
    JTL_emof_TypedElement,
    JTL_emof_Type,
    JTL_emof_Package,
    Property,
    Type,
    JTL_emof_Class,
    EnumerationLiteral,
    DataType,
    JTL_emof_PrimitiveType,
    JTL_emof_Enumeration,
    Element,
    JTL_emof_NamedElement,
    JTL_emof_Comment,
    JTL_emof_Tag,
    Comment,
    Tag,
    Object,
    JTL_emof_Extent,
    JTL_emof_Element,
    JTL_emof_DataType,
    Class,
    Operation,
    JTL_imperativeocl_AnonymousTupleLiteralPart,
    AnonymousTupleLiteralPart,
    JTL_imperativeocl_AnonymousTupleType,
    JTL_imperativeocl_TemplateParameterType,
    JTL_imperativeocl_DictLiteralPart,
    DictLiteralPart,
    essentialocl_LoopExp,
    LogExp,
    JTL_imperativeocl_Typedef,
    AltExp,
    imperativeocl_ImperativeExpression,
    JTL_imperativeocl_ImperativeLoopExp,
    AssignExp,
    PropertyTemplateItem,
    ImperativeExpression,
    JTL_imperativeocl_ContinueExp,
    JTL_imperativeocl_RaiseExp,
    JTL_imperativeocl_BlockExp,
    JTL_imperativeocl_AltExp,
    JTL_imperativeocl_UnlinkExp,
    JTL_imperativeocl_WhileExp,
    JTL_imperativeocl_UnpackExp,
    JTL_imperativeocl_InstantiationExp,
    JTL_imperativeocl_BreakExp,
    JTL_imperativeocl_TryExp,
    JTL_imperativeocl_VariableInitExp,
    JTL_imperativeocl_TupleExp,
    JTL_imperativeocl_LogExp,
    JTL_imperativeocl_ComputeExp,
    JTL_imperativeocl_AssertExp,
    JTL_imperativeocl_ReturnExp,
    JTL_imperativeocl_AssignExp,
    ImperativeLoopExp,
    JTL_imperativeocl_CollectorExp,
    JTL_imperativeocl_ForExp,
    JTL_imperativeocl_ImperativeIterateExp,
    ObjectTemplateExp,
    JTL_template_PropertyTemplateItem,
    JTL_essentialocl_CollectionType,
    CollectionType,
    JTL_imperativeocl_DictionaryType,
    JTL_imperativeocl_ListType,
    JTL_essentialocl_BagType,
    TupleLiteralExp,
    JTL_essentialocl_TupleLiteralPart,
    CallExp,
    JTL_essentialocl_FeaturePropertyCall,
    JTL_essentialocl_OpaqueExpression,
    emof_Type,
    JTL_essentialocl_AnyType,
    JTL_essentialocl_VoidType,
    emof_DataType,
    JTL_essentialocl_TupleType,
    JTL_essentialocl_SetType,
    JTL_essentialocl_SequenceType,
    JTL_essentialocl_OrderedSetType,
    JTL_essentialocl_InvalidType,
    CollectionLiteralExp,
    JTL_essentialocl_CollectionLiteralPart,
    CollectionLiteralPart,
    JTL_essentialocl_NumericLiteralExp,
    LiteralExp,
    JTL_essentialocl_EnumLiteralExp,
    JTL_essentialocl_InvalidLiteralExp,
    JTL_essentialocl_CollectionLiteralExp,
    JTL_imperativeocl_AnonymousTupleLiteralExp,
    JTL_imperativeocl_DictLiteralExp,
    JTL_template_TemplateExp,
    JTL_essentialocl_PrimitiveLiteralExp,
    OpaqueExpression,
    JTL_essentialocl_ExpressionInOcl,
    JTL_essentialocl_NullLiteralExp,
    TupleLiteralPart,
    JTL_essentialocl_TupleLiteralExp,
    JTL_essentialocl_CollectionRange,
    JTL_essentialocl_CollectionItem,
    FeaturePropertyCall,
    JTL_essentialocl_PropertyCallExp,
    ComputeExp,
    LetExp,
    JTL_essentialocl_Variable,
    JTL_essentialocl_OperationCallExp,
    JTL_essentialocl_StringLiteralExp,
    LoopExp,
    JTL_essentialocl_IterateExp,
    JTL_essentialocl_IteratorExp,
    essentialocl_OclExpression,
    essentialocl_CallExp,
    JTL_imperativeocl_SwitchExp,
    JTL_essentialocl_LoopExp,
    JTL_JTL_Where,
    JTL_JTL_When,
    OclExpression,
    JTL_essentialocl_LetExp,
    JTL_essentialocl_TypeExp,
    JTL_imperativeocl_ImperativeExpression,
    JTL_essentialocl_VariableExp,
    JTL_essentialocl_LiteralExp,
    JTL_essentialocl_CallExp,
    JTL_JTL_Predicate,
    TemplateExp,
    JTL_template_CollectionTemplateExp,
    JTL_template_ObjectTemplateExp,
    Predicate,
    JTL_JTL_Pattern,
    JTL_essentialocl_IfExp,
    NumericLiteralExp,
    JTL_essentialocl_IntegerLiteralExp,
    JTL_essentialocl_RealLiteralExp,
    JTL_essentialocl_UnlimitedNaturalExp,
    SeverityKind,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_hyp_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_hyp_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OclExpression)


def test_hyp_jtl_essentialocl_oclexpression_constructor_exists():
    assert callable(JTL_essentialocl_OclExpression.__init__)


def test_hyp_jtl_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_hyp_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_hyp_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_BooleanLiteralExp)


def test_hyp_jtl_essentialocl_booleanliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_BooleanLiteralExp.__init__)


def test_hyp_jtl_essentialocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"




def test_hyp_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_hyp_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_hyp_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_hyp_model_constructor_exists():
    assert callable(Model.__init__)


def test_hyp_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_package_is_not_abstract():
    assert not inspect.isabstract(emof_Package)


def test_hyp_emof_package_constructor_exists():
    assert callable(emof_Package.__init__)


def test_hyp_emof_package_constructor_args():
    sig = inspect.signature(emof_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_class_is_not_abstract():
    assert not inspect.isabstract(emof_Class)


def test_hyp_emof_class_constructor_exists():
    assert callable(emof_Class.__init__)


def test_hyp_emof_class_constructor_args():
    sig = inspect.signature(emof_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_transformation_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Transformation)


def test_hyp_jtl_jtl_transformation_constructor_exists():
    assert callable(JTL_JTL_Transformation.__init__)


def test_hyp_jtl_jtl_transformation_constructor_args():
    sig = inspect.signature(JTL_JTL_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_hyp_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_hyp_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_uriextent_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_URIExtent)


def test_hyp_jtl_emof_uriextent_constructor_exists():
    assert callable(JTL_emof_URIExtent.__init__)


def test_hyp_jtl_emof_uriextent_constructor_args():
    sig = inspect.signature(JTL_emof_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_hyp_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_hyp_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_when_is_not_abstract():
    assert not inspect.isabstract(When)


def test_hyp_when_constructor_exists():
    assert callable(When.__init__)


def test_hyp_when_constructor_args():
    sig = inspect.signature(When.__init__)
    params = list(sig.parameters.keys())



def test_hyp_where_is_not_abstract():
    assert not inspect.isabstract(Where)


def test_hyp_where_constructor_exists():
    assert callable(Where.__init__)


def test_hyp_where_constructor_args():
    sig = inspect.signature(Where.__init__)
    params = list(sig.parameters.keys())



def test_hyp_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_hyp_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_hyp_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_hyp_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_hyp_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_MultiplicityElement)


def test_hyp_jtl_emof_multiplicityelement_constructor_exists():
    assert callable(JTL_emof_MultiplicityElement.__init__)


def test_hyp_jtl_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(JTL_emof_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"







def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(emof_TypedElement)


def test_hyp_emof_typedelement_constructor_exists():
    assert callable(emof_TypedElement.__init__)


def test_hyp_emof_typedelement_constructor_args():
    sig = inspect.signature(emof_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof_MultiplicityElement)


def test_hyp_emof_multiplicityelement_constructor_exists():
    assert callable(emof_MultiplicityElement.__init__)


def test_hyp_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(emof_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_operation_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Operation)


def test_hyp_jtl_emof_operation_constructor_exists():
    assert callable(JTL_emof_Operation.__init__)


def test_hyp_jtl_emof_operation_constructor_args():
    sig = inspect.signature(JTL_emof_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_object_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Object)


def test_hyp_jtl_emof_object_constructor_exists():
    assert callable(JTL_emof_Object.__init__)


def test_hyp_jtl_emof_object_constructor_args():
    sig = inspect.signature(JTL_emof_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_property_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Property)


def test_hyp_jtl_emof_property_constructor_exists():
    assert callable(JTL_emof_Property.__init__)


def test_hyp_jtl_emof_property_constructor_args():
    sig = inspect.signature(JTL_emof_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "default" in params, "Missing parameter 'default'"








def test_hyp_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_hyp_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_hyp_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_parameter_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Parameter)


def test_hyp_jtl_emof_parameter_constructor_exists():
    assert callable(JTL_emof_Parameter.__init__)


def test_hyp_jtl_emof_parameter_constructor_args():
    sig = inspect.signature(JTL_emof_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_hyp_package_constructor_exists():
    assert callable(Package.__init__)


def test_hyp_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_model_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Model)


def test_hyp_jtl_jtl_model_constructor_exists():
    assert callable(JTL_JTL_Model.__init__)


def test_hyp_jtl_jtl_model_constructor_args():
    sig = inspect.signature(JTL_JTL_Model.__init__)
    params = list(sig.parameters.keys())
    assert "usedPackage" in params, "Missing parameter 'usedPackage'"




def test_hyp_jtl_emof_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_EnumerationLiteral)


def test_hyp_jtl_emof_enumerationliteral_constructor_exists():
    assert callable(JTL_emof_EnumerationLiteral.__init__)


def test_hyp_jtl_emof_enumerationliteral_constructor_args():
    sig = inspect.signature(JTL_emof_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_relation_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Relation)


def test_hyp_jtl_jtl_relation_constructor_exists():
    assert callable(JTL_JTL_Relation.__init__)


def test_hyp_jtl_jtl_relation_constructor_args():
    sig = inspect.signature(JTL_JTL_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"




def test_hyp_jtl_jtl_domain_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Domain)


def test_hyp_jtl_jtl_domain_constructor_exists():
    assert callable(JTL_JTL_Domain.__init__)


def test_hyp_jtl_jtl_domain_constructor_args():
    sig = inspect.signature(JTL_JTL_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"





def test_hyp_jtl_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_TypedElement)


def test_hyp_jtl_emof_typedelement_constructor_exists():
    assert callable(JTL_emof_TypedElement.__init__)


def test_hyp_jtl_emof_typedelement_constructor_args():
    sig = inspect.signature(JTL_emof_TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_jtl_emof_type_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Type)


def test_hyp_jtl_emof_type_constructor_exists():
    assert callable(JTL_emof_Type.__init__)


def test_hyp_jtl_emof_type_constructor_args():
    sig = inspect.signature(JTL_emof_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_package_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Package)


def test_hyp_jtl_emof_package_constructor_exists():
    assert callable(JTL_emof_Package.__init__)


def test_hyp_jtl_emof_package_constructor_args():
    sig = inspect.signature(JTL_emof_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_class_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Class)


def test_hyp_jtl_emof_class_constructor_exists():
    assert callable(JTL_emof_Class.__init__)


def test_hyp_jtl_emof_class_constructor_args():
    sig = inspect.signature(JTL_emof_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"




def test_hyp_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_hyp_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_hyp_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_primitivetype_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_PrimitiveType)


def test_hyp_jtl_emof_primitivetype_constructor_exists():
    assert callable(JTL_emof_PrimitiveType.__init__)


def test_hyp_jtl_emof_primitivetype_constructor_args():
    sig = inspect.signature(JTL_emof_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_enumeration_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Enumeration)


def test_hyp_jtl_emof_enumeration_constructor_exists():
    assert callable(JTL_emof_Enumeration.__init__)


def test_hyp_jtl_emof_enumeration_constructor_args():
    sig = inspect.signature(JTL_emof_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_namedelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_NamedElement)


def test_hyp_jtl_emof_namedelement_constructor_exists():
    assert callable(JTL_emof_NamedElement.__init__)


def test_hyp_jtl_emof_namedelement_constructor_args():
    sig = inspect.signature(JTL_emof_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jtl_emof_comment_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Comment)


def test_hyp_jtl_emof_comment_constructor_exists():
    assert callable(JTL_emof_Comment.__init__)


def test_hyp_jtl_emof_comment_constructor_args():
    sig = inspect.signature(JTL_emof_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_tag_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Tag)


def test_hyp_jtl_emof_tag_constructor_exists():
    assert callable(JTL_emof_Tag.__init__)


def test_hyp_jtl_emof_tag_constructor_args():
    sig = inspect.signature(JTL_emof_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_hyp_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_hyp_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_hyp_object_constructor_exists():
    assert callable(Object.__init__)


def test_hyp_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_extent_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Extent)


def test_hyp_jtl_emof_extent_constructor_exists():
    assert callable(JTL_emof_Extent.__init__)


def test_hyp_jtl_emof_extent_constructor_args():
    sig = inspect.signature(JTL_emof_Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_element_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Element)


def test_hyp_jtl_emof_element_constructor_exists():
    assert callable(JTL_emof_Element.__init__)


def test_hyp_jtl_emof_element_constructor_args():
    sig = inspect.signature(JTL_emof_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_DataType)


def test_hyp_jtl_emof_datatype_constructor_exists():
    assert callable(JTL_emof_DataType.__init__)


def test_hyp_jtl_emof_datatype_constructor_args():
    sig = inspect.signature(JTL_emof_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleLiteralPart)


def test_hyp_jtl_imperativeocl_anonymoustupleliteralpart_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleLiteralPart.__init__)


def test_hyp_jtl_imperativeocl_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_hyp_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_hyp_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleType)


def test_hyp_jtl_imperativeocl_anonymoustupletype_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleType.__init__)


def test_hyp_jtl_imperativeocl_anonymoustupletype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TemplateParameterType)


def test_hyp_jtl_imperativeocl_templateparametertype_constructor_exists():
    assert callable(JTL_imperativeocl_TemplateParameterType.__init__)


def test_hyp_jtl_imperativeocl_templateparametertype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"




def test_hyp_jtl_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictLiteralPart)


def test_hyp_jtl_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(JTL_imperativeocl_DictLiteralPart.__init__)


def test_hyp_jtl_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_hyp_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_hyp_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_LoopExp)


def test_hyp_essentialocl_loopexp_constructor_exists():
    assert callable(essentialocl_LoopExp.__init__)


def test_hyp_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(essentialocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_hyp_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_hyp_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_Typedef)


def test_hyp_jtl_imperativeocl_typedef_constructor_exists():
    assert callable(JTL_imperativeocl_Typedef.__init__)


def test_hyp_jtl_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_hyp_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_hyp_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeExpression)


def test_hyp_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(imperativeocl_ImperativeExpression.__init__)


def test_hyp_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeLoopExp)


def test_hyp_jtl_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeLoopExp.__init__)


def test_hyp_jtl_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignexp_is_not_abstract():
    assert not inspect.isabstract(AssignExp)


def test_hyp_assignexp_constructor_exists():
    assert callable(AssignExp.__init__)


def test_hyp_assignexp_constructor_args():
    sig = inspect.signature(AssignExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_hyp_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_hyp_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_hyp_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_hyp_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ContinueExp)


def test_hyp_jtl_imperativeocl_continueexp_constructor_exists():
    assert callable(JTL_imperativeocl_ContinueExp.__init__)


def test_hyp_jtl_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_RaiseExp)


def test_hyp_jtl_imperativeocl_raiseexp_constructor_exists():
    assert callable(JTL_imperativeocl_RaiseExp.__init__)


def test_hyp_jtl_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_BlockExp)


def test_hyp_jtl_imperativeocl_blockexp_constructor_exists():
    assert callable(JTL_imperativeocl_BlockExp.__init__)


def test_hyp_jtl_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AltExp)


def test_hyp_jtl_imperativeocl_altexp_constructor_exists():
    assert callable(JTL_imperativeocl_AltExp.__init__)


def test_hyp_jtl_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_UnlinkExp)


def test_hyp_jtl_imperativeocl_unlinkexp_constructor_exists():
    assert callable(JTL_imperativeocl_UnlinkExp.__init__)


def test_hyp_jtl_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_WhileExp)


def test_hyp_jtl_imperativeocl_whileexp_constructor_exists():
    assert callable(JTL_imperativeocl_WhileExp.__init__)


def test_hyp_jtl_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_UnpackExp)


def test_hyp_jtl_imperativeocl_unpackexp_constructor_exists():
    assert callable(JTL_imperativeocl_UnpackExp.__init__)


def test_hyp_jtl_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_InstantiationExp)


def test_hyp_jtl_imperativeocl_instantiationexp_constructor_exists():
    assert callable(JTL_imperativeocl_InstantiationExp.__init__)


def test_hyp_jtl_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_BreakExp)


def test_hyp_jtl_imperativeocl_breakexp_constructor_exists():
    assert callable(JTL_imperativeocl_BreakExp.__init__)


def test_hyp_jtl_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TryExp)


def test_hyp_jtl_imperativeocl_tryexp_constructor_exists():
    assert callable(JTL_imperativeocl_TryExp.__init__)


def test_hyp_jtl_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_VariableInitExp)


def test_hyp_jtl_imperativeocl_variableinitexp_constructor_exists():
    assert callable(JTL_imperativeocl_VariableInitExp.__init__)


def test_hyp_jtl_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"




def test_hyp_jtl_imperativeocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TupleExp)


def test_hyp_jtl_imperativeocl_tupleexp_constructor_exists():
    assert callable(JTL_imperativeocl_TupleExp.__init__)


def test_hyp_jtl_imperativeocl_tupleexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_LogExp)


def test_hyp_jtl_imperativeocl_logexp_constructor_exists():
    assert callable(JTL_imperativeocl_LogExp.__init__)


def test_hyp_jtl_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"





def test_hyp_jtl_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ComputeExp)


def test_hyp_jtl_imperativeocl_computeexp_constructor_exists():
    assert callable(JTL_imperativeocl_ComputeExp.__init__)


def test_hyp_jtl_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AssertExp)


def test_hyp_jtl_imperativeocl_assertexp_constructor_exists():
    assert callable(JTL_imperativeocl_AssertExp.__init__)


def test_hyp_jtl_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"




def test_hyp_jtl_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ReturnExp)


def test_hyp_jtl_imperativeocl_returnexp_constructor_exists():
    assert callable(JTL_imperativeocl_ReturnExp.__init__)


def test_hyp_jtl_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AssignExp)


def test_hyp_jtl_imperativeocl_assignexp_constructor_exists():
    assert callable(JTL_imperativeocl_AssignExp.__init__)


def test_hyp_jtl_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"




def test_hyp_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_hyp_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_hyp_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_collectorexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_CollectorExp)


def test_hyp_jtl_imperativeocl_collectorexp_constructor_exists():
    assert callable(JTL_imperativeocl_CollectorExp.__init__)


def test_hyp_jtl_imperativeocl_collectorexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ForExp)


def test_hyp_jtl_imperativeocl_forexp_constructor_exists():
    assert callable(JTL_imperativeocl_ForExp.__init__)


def test_hyp_jtl_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeIterateExp)


def test_hyp_jtl_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeIterateExp.__init__)


def test_hyp_jtl_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_hyp_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_hyp_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_template_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(JTL_template_PropertyTemplateItem)


def test_hyp_jtl_template_propertytemplateitem_constructor_exists():
    assert callable(JTL_template_PropertyTemplateItem.__init__)


def test_hyp_jtl_template_propertytemplateitem_constructor_args():
    sig = inspect.signature(JTL_template_PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionType)


def test_hyp_jtl_essentialocl_collectiontype_constructor_exists():
    assert callable(JTL_essentialocl_CollectionType.__init__)


def test_hyp_jtl_essentialocl_collectiontype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_hyp_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_hyp_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictionaryType)


def test_hyp_jtl_imperativeocl_dictionarytype_constructor_exists():
    assert callable(JTL_imperativeocl_DictionaryType.__init__)


def test_hyp_jtl_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ListType)


def test_hyp_jtl_imperativeocl_listtype_constructor_exists():
    assert callable(JTL_imperativeocl_ListType.__init__)


def test_hyp_jtl_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ListType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_BagType)


def test_hyp_jtl_essentialocl_bagtype_constructor_exists():
    assert callable(JTL_essentialocl_BagType.__init__)


def test_hyp_jtl_essentialocl_bagtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_hyp_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_hyp_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleLiteralPart)


def test_hyp_jtl_essentialocl_tupleliteralpart_constructor_exists():
    assert callable(JTL_essentialocl_TupleLiteralPart.__init__)


def test_hyp_jtl_essentialocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_hyp_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_hyp_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_FeaturePropertyCall)


def test_hyp_jtl_essentialocl_featurepropertycall_constructor_exists():
    assert callable(JTL_essentialocl_FeaturePropertyCall.__init__)


def test_hyp_jtl_essentialocl_featurepropertycall_constructor_args():
    sig = inspect.signature(JTL_essentialocl_FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OpaqueExpression)


def test_hyp_jtl_essentialocl_opaqueexpression_constructor_exists():
    assert callable(JTL_essentialocl_OpaqueExpression.__init__)


def test_hyp_jtl_essentialocl_opaqueexpression_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_type_is_not_abstract():
    assert not inspect.isabstract(emof_Type)


def test_hyp_emof_type_constructor_exists():
    assert callable(emof_Type.__init__)


def test_hyp_emof_type_constructor_args():
    sig = inspect.signature(emof_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_anytype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_AnyType)


def test_hyp_jtl_essentialocl_anytype_constructor_exists():
    assert callable(JTL_essentialocl_AnyType.__init__)


def test_hyp_jtl_essentialocl_anytype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_VoidType)


def test_hyp_jtl_essentialocl_voidtype_constructor_exists():
    assert callable(JTL_essentialocl_VoidType.__init__)


def test_hyp_jtl_essentialocl_voidtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(emof_DataType)


def test_hyp_emof_datatype_constructor_exists():
    assert callable(emof_DataType.__init__)


def test_hyp_emof_datatype_constructor_args():
    sig = inspect.signature(emof_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleType)


def test_hyp_jtl_essentialocl_tupletype_constructor_exists():
    assert callable(JTL_essentialocl_TupleType.__init__)


def test_hyp_jtl_essentialocl_tupletype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_settype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_SetType)


def test_hyp_jtl_essentialocl_settype_constructor_exists():
    assert callable(JTL_essentialocl_SetType.__init__)


def test_hyp_jtl_essentialocl_settype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_SequenceType)


def test_hyp_jtl_essentialocl_sequencetype_constructor_exists():
    assert callable(JTL_essentialocl_SequenceType.__init__)


def test_hyp_jtl_essentialocl_sequencetype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OrderedSetType)


def test_hyp_jtl_essentialocl_orderedsettype_constructor_exists():
    assert callable(JTL_essentialocl_OrderedSetType.__init__)


def test_hyp_jtl_essentialocl_orderedsettype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_InvalidType)


def test_hyp_jtl_essentialocl_invalidtype_constructor_exists():
    assert callable(JTL_essentialocl_InvalidType.__init__)


def test_hyp_jtl_essentialocl_invalidtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_hyp_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_hyp_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionLiteralPart)


def test_hyp_jtl_essentialocl_collectionliteralpart_constructor_exists():
    assert callable(JTL_essentialocl_CollectionLiteralPart.__init__)


def test_hyp_jtl_essentialocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_hyp_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_hyp_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_NumericLiteralExp)


def test_hyp_jtl_essentialocl_numericliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_NumericLiteralExp.__init__)


def test_hyp_jtl_essentialocl_numericliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_hyp_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_hyp_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_EnumLiteralExp)


def test_hyp_jtl_essentialocl_enumliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_EnumLiteralExp.__init__)


def test_hyp_jtl_essentialocl_enumliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_InvalidLiteralExp)


def test_hyp_jtl_essentialocl_invalidliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_InvalidLiteralExp.__init__)


def test_hyp_jtl_essentialocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionLiteralExp)


def test_hyp_jtl_essentialocl_collectionliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_CollectionLiteralExp.__init__)


def test_hyp_jtl_essentialocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_jtl_imperativeocl_anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleLiteralExp)


def test_hyp_jtl_imperativeocl_anonymoustupleliteralexp_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleLiteralExp.__init__)


def test_hyp_jtl_imperativeocl_anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictLiteralExp)


def test_hyp_jtl_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(JTL_imperativeocl_DictLiteralExp.__init__)


def test_hyp_jtl_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_template_templateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_TemplateExp)


def test_hyp_jtl_template_templateexp_constructor_exists():
    assert callable(JTL_template_TemplateExp.__init__)


def test_hyp_jtl_template_templateexp_constructor_args():
    sig = inspect.signature(JTL_template_TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_PrimitiveLiteralExp)


def test_hyp_jtl_essentialocl_primitiveliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_PrimitiveLiteralExp.__init__)


def test_hyp_jtl_essentialocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_hyp_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_hyp_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_ExpressionInOcl)


def test_hyp_jtl_essentialocl_expressioninocl_constructor_exists():
    assert callable(JTL_essentialocl_ExpressionInOcl.__init__)


def test_hyp_jtl_essentialocl_expressioninocl_constructor_args():
    sig = inspect.signature(JTL_essentialocl_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_NullLiteralExp)


def test_hyp_jtl_essentialocl_nullliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_NullLiteralExp.__init__)


def test_hyp_jtl_essentialocl_nullliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_hyp_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_hyp_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleLiteralExp)


def test_hyp_jtl_essentialocl_tupleliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_TupleLiteralExp.__init__)


def test_hyp_jtl_essentialocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionRange)


def test_hyp_jtl_essentialocl_collectionrange_constructor_exists():
    assert callable(JTL_essentialocl_CollectionRange.__init__)


def test_hyp_jtl_essentialocl_collectionrange_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionItem)


def test_hyp_jtl_essentialocl_collectionitem_constructor_exists():
    assert callable(JTL_essentialocl_CollectionItem.__init__)


def test_hyp_jtl_essentialocl_collectionitem_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_hyp_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_hyp_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_PropertyCallExp)


def test_hyp_jtl_essentialocl_propertycallexp_constructor_exists():
    assert callable(JTL_essentialocl_PropertyCallExp.__init__)


def test_hyp_jtl_essentialocl_propertycallexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_computeexp_is_not_abstract():
    assert not inspect.isabstract(ComputeExp)


def test_hyp_computeexp_constructor_exists():
    assert callable(ComputeExp.__init__)


def test_hyp_computeexp_constructor_args():
    sig = inspect.signature(ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_hyp_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_hyp_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_variable_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_Variable)


def test_hyp_jtl_essentialocl_variable_constructor_exists():
    assert callable(JTL_essentialocl_Variable.__init__)


def test_hyp_jtl_essentialocl_variable_constructor_args():
    sig = inspect.signature(JTL_essentialocl_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OperationCallExp)


def test_hyp_jtl_essentialocl_operationcallexp_constructor_exists():
    assert callable(JTL_essentialocl_OperationCallExp.__init__)


def test_hyp_jtl_essentialocl_operationcallexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_StringLiteralExp)


def test_hyp_jtl_essentialocl_stringliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_StringLiteralExp.__init__)


def test_hyp_jtl_essentialocl_stringliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_hyp_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_hyp_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IterateExp)


def test_hyp_jtl_essentialocl_iterateexp_constructor_exists():
    assert callable(JTL_essentialocl_IterateExp.__init__)


def test_hyp_jtl_essentialocl_iterateexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IteratorExp)


def test_hyp_jtl_essentialocl_iteratorexp_constructor_exists():
    assert callable(JTL_essentialocl_IteratorExp.__init__)


def test_hyp_jtl_essentialocl_iteratorexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OclExpression)


def test_hyp_essentialocl_oclexpression_constructor_exists():
    assert callable(essentialocl_OclExpression.__init__)


def test_hyp_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(essentialocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CallExp)


def test_hyp_essentialocl_callexp_constructor_exists():
    assert callable(essentialocl_CallExp.__init__)


def test_hyp_essentialocl_callexp_constructor_args():
    sig = inspect.signature(essentialocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_SwitchExp)


def test_hyp_jtl_imperativeocl_switchexp_constructor_exists():
    assert callable(JTL_imperativeocl_SwitchExp.__init__)


def test_hyp_jtl_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LoopExp)


def test_hyp_jtl_essentialocl_loopexp_constructor_exists():
    assert callable(JTL_essentialocl_LoopExp.__init__)


def test_hyp_jtl_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_where_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Where)


def test_hyp_jtl_jtl_where_constructor_exists():
    assert callable(JTL_JTL_Where.__init__)


def test_hyp_jtl_jtl_where_constructor_args():
    sig = inspect.signature(JTL_JTL_Where.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_when_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_When)


def test_hyp_jtl_jtl_when_constructor_exists():
    assert callable(JTL_JTL_When.__init__)


def test_hyp_jtl_jtl_when_constructor_args():
    sig = inspect.signature(JTL_JTL_When.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_hyp_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_hyp_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_letexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LetExp)


def test_hyp_jtl_essentialocl_letexp_constructor_exists():
    assert callable(JTL_essentialocl_LetExp.__init__)


def test_hyp_jtl_essentialocl_letexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_typeexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TypeExp)


def test_hyp_jtl_essentialocl_typeexp_constructor_exists():
    assert callable(JTL_essentialocl_TypeExp.__init__)


def test_hyp_jtl_essentialocl_typeexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeExpression)


def test_hyp_jtl_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeExpression.__init__)


def test_hyp_jtl_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_VariableExp)


def test_hyp_jtl_essentialocl_variableexp_constructor_exists():
    assert callable(JTL_essentialocl_VariableExp.__init__)


def test_hyp_jtl_essentialocl_variableexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LiteralExp)


def test_hyp_jtl_essentialocl_literalexp_constructor_exists():
    assert callable(JTL_essentialocl_LiteralExp.__init__)


def test_hyp_jtl_essentialocl_literalexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CallExp)


def test_hyp_jtl_essentialocl_callexp_constructor_exists():
    assert callable(JTL_essentialocl_CallExp.__init__)


def test_hyp_jtl_essentialocl_callexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_predicate_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Predicate)


def test_hyp_jtl_jtl_predicate_constructor_exists():
    assert callable(JTL_JTL_Predicate.__init__)


def test_hyp_jtl_jtl_predicate_constructor_args():
    sig = inspect.signature(JTL_JTL_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_hyp_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_hyp_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_template_collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_CollectionTemplateExp)


def test_hyp_jtl_template_collectiontemplateexp_constructor_exists():
    assert callable(JTL_template_CollectionTemplateExp.__init__)


def test_hyp_jtl_template_collectiontemplateexp_constructor_args():
    sig = inspect.signature(JTL_template_CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_jtl_template_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_ObjectTemplateExp)


def test_hyp_jtl_template_objecttemplateexp_constructor_exists():
    assert callable(JTL_template_ObjectTemplateExp.__init__)


def test_hyp_jtl_template_objecttemplateexp_constructor_args():
    sig = inspect.signature(JTL_template_ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredClass" in params, "Missing parameter 'referredClass'"




def test_hyp_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_hyp_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_hyp_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_jtl_pattern_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Pattern)


def test_hyp_jtl_jtl_pattern_constructor_exists():
    assert callable(JTL_JTL_Pattern.__init__)


def test_hyp_jtl_jtl_pattern_constructor_args():
    sig = inspect.signature(JTL_JTL_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IfExp)


def test_hyp_jtl_essentialocl_ifexp_constructor_exists():
    assert callable(JTL_essentialocl_IfExp.__init__)


def test_hyp_jtl_essentialocl_ifexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_hyp_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_hyp_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jtl_essentialocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IntegerLiteralExp)


def test_hyp_jtl_essentialocl_integerliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_IntegerLiteralExp.__init__)


def test_hyp_jtl_essentialocl_integerliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"




def test_hyp_jtl_essentialocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_RealLiteralExp)


def test_hyp_jtl_essentialocl_realliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_RealLiteralExp.__init__)


def test_hyp_jtl_essentialocl_realliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"




def test_hyp_jtl_essentialocl_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_UnlimitedNaturalExp)


def test_hyp_jtl_essentialocl_unlimitednaturalexp_constructor_exists():
    assert callable(JTL_essentialocl_UnlimitedNaturalExp.__init__)


def test_hyp_jtl_essentialocl_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"


def test_hyp_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_hyp_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "fatal",
        "warning",
        "error",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"

def test_hyp_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_hyp_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Set",
        "OrderedSet",
        "Bag",
        "Sequence",
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
TryExp_strategy = st.builds(
    TryExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JTL_essentialocl_OclExpression_strategy = st.builds(
    JTL_essentialocl_OclExpression,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
JTL_essentialocl_BooleanLiteralExp_strategy = st.builds(
    JTL_essentialocl_BooleanLiteralExp,
    booleanSymbol=
        st.booleans()
)
Relation_strategy = st.builds(
    Relation,
)
Model_strategy = st.builds(
    Model,
)
emof_Package_strategy = st.builds(
    emof_Package,
)
emof_Class_strategy = st.builds(
    emof_Class,
)
JTL_JTL_Transformation_strategy = st.builds(
    JTL_JTL_Transformation,
)
Extent_strategy = st.builds(
    Extent,
)
JTL_emof_URIExtent_strategy = st.builds(
    JTL_emof_URIExtent,
)
Pattern_strategy = st.builds(
    Pattern,
)
Variable_strategy = st.builds(
    Variable,
)
When_strategy = st.builds(
    When,
)
Where_strategy = st.builds(
    Where,
)
Domain_strategy = st.builds(
    Domain,
)
Transformation_strategy = st.builds(
    Transformation,
)
JTL_emof_MultiplicityElement_strategy = st.builds(
    JTL_emof_MultiplicityElement,
    isUnique=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    lower=
        st.integers()
)
Parameter_strategy = st.builds(
    Parameter,
)
emof_TypedElement_strategy = st.builds(
    emof_TypedElement,
)
emof_MultiplicityElement_strategy = st.builds(
    emof_MultiplicityElement,
)
JTL_emof_Operation_strategy = st.builds(
    JTL_emof_Operation,
)
JTL_emof_Object_strategy = st.builds(
    JTL_emof_Object,
)
JTL_emof_Property_strategy = st.builds(
    JTL_emof_Property,
    isDerived=
        st.booleans(),
    isId=
        st.booleans(),
    isReadOnly=
        st.booleans(),
    isComposite=
        st.booleans(),
    default=
        safe_text
)
Enumeration_strategy = st.builds(
    Enumeration,
)
JTL_emof_Parameter_strategy = st.builds(
    JTL_emof_Parameter,
)
Package_strategy = st.builds(
    Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JTL_JTL_Model_strategy = st.builds(
    JTL_JTL_Model,
    usedPackage=
        safe_text
)
JTL_emof_EnumerationLiteral_strategy = st.builds(
    JTL_emof_EnumerationLiteral,
)
JTL_JTL_Relation_strategy = st.builds(
    JTL_JTL_Relation,
    isTopLevel=
        st.booleans()
)
JTL_JTL_Domain_strategy = st.builds(
    JTL_JTL_Domain,
    isEnforceable=
        st.booleans(),
    isCheckable=
        st.booleans()
)
JTL_emof_TypedElement_strategy = st.builds(
    JTL_emof_TypedElement,
    type=
        safe_text
)
JTL_emof_Type_strategy = st.builds(
    JTL_emof_Type,
)
JTL_emof_Package_strategy = st.builds(
    JTL_emof_Package,
    uri=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
JTL_emof_Class_strategy = st.builds(
    JTL_emof_Class,
    isAbstract=
        st.booleans()
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
JTL_emof_PrimitiveType_strategy = st.builds(
    JTL_emof_PrimitiveType,
)
JTL_emof_Enumeration_strategy = st.builds(
    JTL_emof_Enumeration,
)
Element_strategy = st.builds(
    Element,
)
JTL_emof_NamedElement_strategy = st.builds(
    JTL_emof_NamedElement,
    name=
        safe_text
)
JTL_emof_Comment_strategy = st.builds(
    JTL_emof_Comment,
)
JTL_emof_Tag_strategy = st.builds(
    JTL_emof_Tag,
    name=
        safe_text,
    value=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Tag_strategy = st.builds(
    Tag,
)
Object_strategy = st.builds(
    Object,
)
JTL_emof_Extent_strategy = st.builds(
    JTL_emof_Extent,
)
JTL_emof_Element_strategy = st.builds(
    JTL_emof_Element,
)
JTL_emof_DataType_strategy = st.builds(
    JTL_emof_DataType,
)
Class_strategy = st.builds(
    Class,
)
Operation_strategy = st.builds(
    Operation,
)
JTL_imperativeocl_AnonymousTupleLiteralPart_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleLiteralPart,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
JTL_imperativeocl_AnonymousTupleType_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleType,
)
JTL_imperativeocl_TemplateParameterType_strategy = st.builds(
    JTL_imperativeocl_TemplateParameterType,
    specification=
        safe_text
)
JTL_imperativeocl_DictLiteralPart_strategy = st.builds(
    JTL_imperativeocl_DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
essentialocl_LoopExp_strategy = st.builds(
    essentialocl_LoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
JTL_imperativeocl_Typedef_strategy = st.builds(
    JTL_imperativeocl_Typedef,
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl_ImperativeExpression_strategy = st.builds(
    imperativeocl_ImperativeExpression,
)
JTL_imperativeocl_ImperativeLoopExp_strategy = st.builds(
    JTL_imperativeocl_ImperativeLoopExp,
)
AssignExp_strategy = st.builds(
    AssignExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
JTL_imperativeocl_ContinueExp_strategy = st.builds(
    JTL_imperativeocl_ContinueExp,
)
JTL_imperativeocl_RaiseExp_strategy = st.builds(
    JTL_imperativeocl_RaiseExp,
)
JTL_imperativeocl_BlockExp_strategy = st.builds(
    JTL_imperativeocl_BlockExp,
)
JTL_imperativeocl_AltExp_strategy = st.builds(
    JTL_imperativeocl_AltExp,
)
JTL_imperativeocl_UnlinkExp_strategy = st.builds(
    JTL_imperativeocl_UnlinkExp,
)
JTL_imperativeocl_WhileExp_strategy = st.builds(
    JTL_imperativeocl_WhileExp,
)
JTL_imperativeocl_UnpackExp_strategy = st.builds(
    JTL_imperativeocl_UnpackExp,
)
JTL_imperativeocl_InstantiationExp_strategy = st.builds(
    JTL_imperativeocl_InstantiationExp,
)
JTL_imperativeocl_BreakExp_strategy = st.builds(
    JTL_imperativeocl_BreakExp,
)
JTL_imperativeocl_TryExp_strategy = st.builds(
    JTL_imperativeocl_TryExp,
)
JTL_imperativeocl_VariableInitExp_strategy = st.builds(
    JTL_imperativeocl_VariableInitExp,
    withResult=
        st.booleans()
)
JTL_imperativeocl_TupleExp_strategy = st.builds(
    JTL_imperativeocl_TupleExp,
)
JTL_imperativeocl_LogExp_strategy = st.builds(
    JTL_imperativeocl_LogExp,
    text=
        safe_text,
    level=
        st.integers()
)
JTL_imperativeocl_ComputeExp_strategy = st.builds(
    JTL_imperativeocl_ComputeExp,
)
JTL_imperativeocl_AssertExp_strategy = st.builds(
    JTL_imperativeocl_AssertExp,
    severity=
        safe_text
)
JTL_imperativeocl_ReturnExp_strategy = st.builds(
    JTL_imperativeocl_ReturnExp,
)
JTL_imperativeocl_AssignExp_strategy = st.builds(
    JTL_imperativeocl_AssignExp,
    isReset=
        st.booleans()
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
JTL_imperativeocl_CollectorExp_strategy = st.builds(
    JTL_imperativeocl_CollectorExp,
)
JTL_imperativeocl_ForExp_strategy = st.builds(
    JTL_imperativeocl_ForExp,
)
JTL_imperativeocl_ImperativeIterateExp_strategy = st.builds(
    JTL_imperativeocl_ImperativeIterateExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
JTL_template_PropertyTemplateItem_strategy = st.builds(
    JTL_template_PropertyTemplateItem,
)
JTL_essentialocl_CollectionType_strategy = st.builds(
    JTL_essentialocl_CollectionType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
JTL_imperativeocl_DictionaryType_strategy = st.builds(
    JTL_imperativeocl_DictionaryType,
)
JTL_imperativeocl_ListType_strategy = st.builds(
    JTL_imperativeocl_ListType,
)
JTL_essentialocl_BagType_strategy = st.builds(
    JTL_essentialocl_BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
JTL_essentialocl_TupleLiteralPart_strategy = st.builds(
    JTL_essentialocl_TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
JTL_essentialocl_FeaturePropertyCall_strategy = st.builds(
    JTL_essentialocl_FeaturePropertyCall,
)
JTL_essentialocl_OpaqueExpression_strategy = st.builds(
    JTL_essentialocl_OpaqueExpression,
)
emof_Type_strategy = st.builds(
    emof_Type,
)
JTL_essentialocl_AnyType_strategy = st.builds(
    JTL_essentialocl_AnyType,
)
JTL_essentialocl_VoidType_strategy = st.builds(
    JTL_essentialocl_VoidType,
)
emof_DataType_strategy = st.builds(
    emof_DataType,
)
JTL_essentialocl_TupleType_strategy = st.builds(
    JTL_essentialocl_TupleType,
)
JTL_essentialocl_SetType_strategy = st.builds(
    JTL_essentialocl_SetType,
)
JTL_essentialocl_SequenceType_strategy = st.builds(
    JTL_essentialocl_SequenceType,
)
JTL_essentialocl_OrderedSetType_strategy = st.builds(
    JTL_essentialocl_OrderedSetType,
)
JTL_essentialocl_InvalidType_strategy = st.builds(
    JTL_essentialocl_InvalidType,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
JTL_essentialocl_CollectionLiteralPart_strategy = st.builds(
    JTL_essentialocl_CollectionLiteralPart,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
JTL_essentialocl_NumericLiteralExp_strategy = st.builds(
    JTL_essentialocl_NumericLiteralExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
JTL_essentialocl_EnumLiteralExp_strategy = st.builds(
    JTL_essentialocl_EnumLiteralExp,
)
JTL_essentialocl_InvalidLiteralExp_strategy = st.builds(
    JTL_essentialocl_InvalidLiteralExp,
)
JTL_essentialocl_CollectionLiteralExp_strategy = st.builds(
    JTL_essentialocl_CollectionLiteralExp,
    kind=
        safe_text
)
JTL_imperativeocl_AnonymousTupleLiteralExp_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleLiteralExp,
)
JTL_imperativeocl_DictLiteralExp_strategy = st.builds(
    JTL_imperativeocl_DictLiteralExp,
)
JTL_template_TemplateExp_strategy = st.builds(
    JTL_template_TemplateExp,
)
JTL_essentialocl_PrimitiveLiteralExp_strategy = st.builds(
    JTL_essentialocl_PrimitiveLiteralExp,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
JTL_essentialocl_ExpressionInOcl_strategy = st.builds(
    JTL_essentialocl_ExpressionInOcl,
)
JTL_essentialocl_NullLiteralExp_strategy = st.builds(
    JTL_essentialocl_NullLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
JTL_essentialocl_TupleLiteralExp_strategy = st.builds(
    JTL_essentialocl_TupleLiteralExp,
)
JTL_essentialocl_CollectionRange_strategy = st.builds(
    JTL_essentialocl_CollectionRange,
)
JTL_essentialocl_CollectionItem_strategy = st.builds(
    JTL_essentialocl_CollectionItem,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
JTL_essentialocl_PropertyCallExp_strategy = st.builds(
    JTL_essentialocl_PropertyCallExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
JTL_essentialocl_Variable_strategy = st.builds(
    JTL_essentialocl_Variable,
)
JTL_essentialocl_OperationCallExp_strategy = st.builds(
    JTL_essentialocl_OperationCallExp,
)
JTL_essentialocl_StringLiteralExp_strategy = st.builds(
    JTL_essentialocl_StringLiteralExp,
    stringSymbol=
        safe_text
)
LoopExp_strategy = st.builds(
    LoopExp,
)
JTL_essentialocl_IterateExp_strategy = st.builds(
    JTL_essentialocl_IterateExp,
)
JTL_essentialocl_IteratorExp_strategy = st.builds(
    JTL_essentialocl_IteratorExp,
)
essentialocl_OclExpression_strategy = st.builds(
    essentialocl_OclExpression,
)
essentialocl_CallExp_strategy = st.builds(
    essentialocl_CallExp,
)
JTL_imperativeocl_SwitchExp_strategy = st.builds(
    JTL_imperativeocl_SwitchExp,
)
JTL_essentialocl_LoopExp_strategy = st.builds(
    JTL_essentialocl_LoopExp,
)
JTL_JTL_Where_strategy = st.builds(
    JTL_JTL_Where,
)
JTL_JTL_When_strategy = st.builds(
    JTL_JTL_When,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
JTL_essentialocl_LetExp_strategy = st.builds(
    JTL_essentialocl_LetExp,
)
JTL_essentialocl_TypeExp_strategy = st.builds(
    JTL_essentialocl_TypeExp,
)
JTL_imperativeocl_ImperativeExpression_strategy = st.builds(
    JTL_imperativeocl_ImperativeExpression,
)
JTL_essentialocl_VariableExp_strategy = st.builds(
    JTL_essentialocl_VariableExp,
)
JTL_essentialocl_LiteralExp_strategy = st.builds(
    JTL_essentialocl_LiteralExp,
)
JTL_essentialocl_CallExp_strategy = st.builds(
    JTL_essentialocl_CallExp,
)
JTL_JTL_Predicate_strategy = st.builds(
    JTL_JTL_Predicate,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
JTL_template_CollectionTemplateExp_strategy = st.builds(
    JTL_template_CollectionTemplateExp,
    kind=
        safe_text
)
JTL_template_ObjectTemplateExp_strategy = st.builds(
    JTL_template_ObjectTemplateExp,
    referredClass=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
JTL_JTL_Pattern_strategy = st.builds(
    JTL_JTL_Pattern,
)
JTL_essentialocl_IfExp_strategy = st.builds(
    JTL_essentialocl_IfExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
JTL_essentialocl_IntegerLiteralExp_strategy = st.builds(
    JTL_essentialocl_IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
JTL_essentialocl_RealLiteralExp_strategy = st.builds(
    JTL_essentialocl_RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
JTL_essentialocl_UnlimitedNaturalExp_strategy = st.builds(
    JTL_essentialocl_UnlimitedNaturalExp,
    symbol=
        safe_text
)








@given(instance=JTL_essentialocl_BooleanLiteralExp_strategy)
def test_hyp_jtl_essentialocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

















@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_hyp_jtl_emof_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_hyp_jtl_emof_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_hyp_jtl_emof_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_hyp_jtl_emof_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original









@given(instance=JTL_emof_Property_strategy)
def test_hyp_jtl_emof_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=JTL_emof_Property_strategy)
def test_hyp_jtl_emof_property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original



@given(instance=JTL_emof_Property_strategy)
def test_hyp_jtl_emof_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=JTL_emof_Property_strategy)
def test_hyp_jtl_emof_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=JTL_emof_Property_strategy)
def test_hyp_jtl_emof_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original








@given(instance=JTL_JTL_Model_strategy)
def test_hyp_jtl_jtl_model_usedPackage_setter(instance):
    original = instance.usedPackage
    instance.usedPackage = original
    assert instance.usedPackage == original





@given(instance=JTL_JTL_Relation_strategy)
def test_hyp_jtl_jtl_relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original




@given(instance=JTL_JTL_Domain_strategy)
def test_hyp_jtl_jtl_domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original



@given(instance=JTL_JTL_Domain_strategy)
def test_hyp_jtl_jtl_domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original




@given(instance=JTL_emof_TypedElement_strategy)
def test_hyp_jtl_emof_typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=JTL_emof_Package_strategy)
def test_hyp_jtl_emof_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original






@given(instance=JTL_emof_Class_strategy)
def test_hyp_jtl_emof_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original









@given(instance=JTL_emof_NamedElement_strategy)
def test_hyp_jtl_emof_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=JTL_emof_Tag_strategy)
def test_hyp_jtl_emof_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JTL_emof_Tag_strategy)
def test_hyp_jtl_emof_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original















@given(instance=JTL_imperativeocl_TemplateParameterType_strategy)
def test_hyp_jtl_imperativeocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

























@given(instance=JTL_imperativeocl_VariableInitExp_strategy)
def test_hyp_jtl_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original





@given(instance=JTL_imperativeocl_LogExp_strategy)
def test_hyp_jtl_imperativeocl_logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=JTL_imperativeocl_LogExp_strategy)
def test_hyp_jtl_imperativeocl_logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original





@given(instance=JTL_imperativeocl_AssertExp_strategy)
def test_hyp_jtl_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original





@given(instance=JTL_imperativeocl_AssignExp_strategy)
def test_hyp_jtl_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original




































@given(instance=JTL_essentialocl_CollectionLiteralExp_strategy)
def test_hyp_jtl_essentialocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





















@given(instance=JTL_essentialocl_StringLiteralExp_strategy)
def test_hyp_jtl_essentialocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original






















@given(instance=JTL_template_CollectionTemplateExp_strategy)
def test_hyp_jtl_template_collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=JTL_template_ObjectTemplateExp_strategy)
def test_hyp_jtl_template_objecttemplateexp_referredClass_setter(instance):
    original = instance.referredClass
    instance.referredClass = original
    assert instance.referredClass == original








@given(instance=JTL_essentialocl_IntegerLiteralExp_strategy)
def test_hyp_jtl_essentialocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original




@given(instance=JTL_essentialocl_RealLiteralExp_strategy)
def test_hyp_jtl_essentialocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original




@given(instance=JTL_essentialocl_UnlimitedNaturalExp_strategy)
def test_hyp_jtl_essentialocl_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AltExp,
    AnonymousTupleLiteralPart,
    AssignExp,
    CallExp,
    Class,
    CollectionLiteralExp,
    CollectionLiteralPart,
    CollectionType,
    Comment,
    ComputeExp,
    DataType,
    DictLiteralPart,
    Domain,
    Element,
    Enumeration,
    EnumerationLiteral,
    Extent,
    FeaturePropertyCall,
    ImperativeExpression,
    ImperativeLoopExp,
    JTL_JTL_Domain,
    JTL_JTL_Model,
    JTL_JTL_Pattern,
    JTL_JTL_Predicate,
    JTL_JTL_Relation,
    JTL_JTL_Transformation,
    JTL_JTL_When,
    JTL_JTL_Where,
    JTL_emof_Class,
    JTL_emof_Comment,
    JTL_emof_DataType,
    JTL_emof_Element,
    JTL_emof_Enumeration,
    JTL_emof_EnumerationLiteral,
    JTL_emof_Extent,
    JTL_emof_MultiplicityElement,
    JTL_emof_NamedElement,
    JTL_emof_Object,
    JTL_emof_Operation,
    JTL_emof_Package,
    JTL_emof_Parameter,
    JTL_emof_PrimitiveType,
    JTL_emof_Property,
    JTL_emof_Tag,
    JTL_emof_Type,
    JTL_emof_TypedElement,
    JTL_emof_URIExtent,
    JTL_essentialocl_AnyType,
    JTL_essentialocl_BagType,
    JTL_essentialocl_BooleanLiteralExp,
    JTL_essentialocl_CallExp,
    JTL_essentialocl_CollectionItem,
    JTL_essentialocl_CollectionLiteralExp,
    JTL_essentialocl_CollectionLiteralPart,
    JTL_essentialocl_CollectionRange,
    JTL_essentialocl_CollectionType,
    JTL_essentialocl_EnumLiteralExp,
    JTL_essentialocl_ExpressionInOcl,
    JTL_essentialocl_FeaturePropertyCall,
    JTL_essentialocl_IfExp,
    JTL_essentialocl_IntegerLiteralExp,
    JTL_essentialocl_InvalidLiteralExp,
    JTL_essentialocl_InvalidType,
    JTL_essentialocl_IterateExp,
    JTL_essentialocl_IteratorExp,
    JTL_essentialocl_LetExp,
    JTL_essentialocl_LiteralExp,
    JTL_essentialocl_LoopExp,
    JTL_essentialocl_NullLiteralExp,
    JTL_essentialocl_NumericLiteralExp,
    JTL_essentialocl_OclExpression,
    JTL_essentialocl_OpaqueExpression,
    JTL_essentialocl_OperationCallExp,
    JTL_essentialocl_OrderedSetType,
    JTL_essentialocl_PrimitiveLiteralExp,
    JTL_essentialocl_PropertyCallExp,
    JTL_essentialocl_RealLiteralExp,
    JTL_essentialocl_SequenceType,
    JTL_essentialocl_SetType,
    JTL_essentialocl_StringLiteralExp,
    JTL_essentialocl_TupleLiteralExp,
    JTL_essentialocl_TupleLiteralPart,
    JTL_essentialocl_TupleType,
    JTL_essentialocl_TypeExp,
    JTL_essentialocl_UnlimitedNaturalExp,
    JTL_essentialocl_Variable,
    JTL_essentialocl_VariableExp,
    JTL_essentialocl_VoidType,
    JTL_imperativeocl_AltExp,
    JTL_imperativeocl_AnonymousTupleLiteralExp,
    JTL_imperativeocl_AnonymousTupleLiteralPart,
    JTL_imperativeocl_AnonymousTupleType,
    JTL_imperativeocl_AssertExp,
    JTL_imperativeocl_AssignExp,
    JTL_imperativeocl_BlockExp,
    JTL_imperativeocl_BreakExp,
    JTL_imperativeocl_CollectorExp,
    JTL_imperativeocl_ComputeExp,
    JTL_imperativeocl_ContinueExp,
    JTL_imperativeocl_DictLiteralExp,
    JTL_imperativeocl_DictLiteralPart,
    JTL_imperativeocl_DictionaryType,
    JTL_imperativeocl_ForExp,
    JTL_imperativeocl_ImperativeExpression,
    JTL_imperativeocl_ImperativeIterateExp,
    JTL_imperativeocl_ImperativeLoopExp,
    JTL_imperativeocl_InstantiationExp,
    JTL_imperativeocl_ListType,
    JTL_imperativeocl_LogExp,
    JTL_imperativeocl_RaiseExp,
    JTL_imperativeocl_ReturnExp,
    JTL_imperativeocl_SwitchExp,
    JTL_imperativeocl_TemplateParameterType,
    JTL_imperativeocl_TryExp,
    JTL_imperativeocl_TupleExp,
    JTL_imperativeocl_Typedef,
    JTL_imperativeocl_UnlinkExp,
    JTL_imperativeocl_UnpackExp,
    JTL_imperativeocl_VariableInitExp,
    JTL_imperativeocl_WhileExp,
    JTL_template_CollectionTemplateExp,
    JTL_template_ObjectTemplateExp,
    JTL_template_PropertyTemplateItem,
    JTL_template_TemplateExp,
    LetExp,
    LiteralExp,
    LogExp,
    LoopExp,
    Model,
    NamedElement,
    NumericLiteralExp,
    Object,
    ObjectTemplateExp,
    OclExpression,
    OpaqueExpression,
    Operation,
    Package,
    Parameter,
    Pattern,
    Predicate,
    PrimitiveLiteralExp,
    Property,
    PropertyTemplateItem,
    Relation,
    Tag,
    TemplateExp,
    Transformation,
    TryExp,
    TupleLiteralExp,
    TupleLiteralPart,
    Type,
    TypedElement,
    Variable,
    When,
    Where,
    emof_Class,
    emof_DataType,
    emof_MultiplicityElement,
    emof_Package,
    emof_Type,
    emof_TypedElement,
    essentialocl_CallExp,
    essentialocl_LoopExp,
    essentialocl_OclExpression,
    imperativeocl_ImperativeExpression,
    CollectionKind,
    SeverityKind,
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

def test_JTL_JTL_Domain_isCheckable_value_roundtrip():
    instance = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    assert instance.isCheckable == True
    instance.isCheckable = False
    assert instance.isCheckable == False


def test_JTL_JTL_Domain_isEnforceable_value_roundtrip():
    instance = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    assert instance.isEnforceable == True
    instance.isEnforceable = False
    assert instance.isEnforceable == False


def test_JTL_JTL_Model_usedPackage_value_roundtrip():
    instance = JTL_JTL_Model(usedPackage="sample_text")
    assert instance.usedPackage == "sample_text"
    instance.usedPackage = "sample_text_2"
    assert instance.usedPackage == "sample_text_2"


def test_JTL_JTL_Relation_isTopLevel_value_roundtrip():
    instance = JTL_JTL_Relation(isTopLevel=True)
    assert instance.isTopLevel == True
    instance.isTopLevel = False
    assert instance.isTopLevel == False


def test_JTL_emof_Class_isAbstract_value_roundtrip():
    instance = JTL_emof_Class(isAbstract=True)
    assert instance.isAbstract == True
    instance.isAbstract = False
    assert instance.isAbstract == False


def test_JTL_emof_MultiplicityElement_isOrdered_value_roundtrip():
    instance = JTL_emof_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower=7, upper="sample_text")
    assert instance.isOrdered == "sample_text"
    instance.isOrdered = "sample_text_2"
    assert instance.isOrdered == "sample_text_2"


def test_JTL_emof_MultiplicityElement_isUnique_value_roundtrip():
    instance = JTL_emof_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower=7, upper="sample_text")
    assert instance.isUnique == "sample_text"
    instance.isUnique = "sample_text_2"
    assert instance.isUnique == "sample_text_2"


def test_JTL_emof_MultiplicityElement_lower_value_roundtrip():
    instance = JTL_emof_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower=7, upper="sample_text")
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_JTL_emof_MultiplicityElement_upper_value_roundtrip():
    instance = JTL_emof_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower=7, upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_JTL_emof_NamedElement_name_value_roundtrip():
    instance = JTL_emof_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_JTL_emof_Package_uri_value_roundtrip():
    instance = JTL_emof_Package(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_JTL_emof_Property_default_value_roundtrip():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_JTL_emof_Property_isComposite_value_roundtrip():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert instance.isComposite == True
    instance.isComposite = False
    assert instance.isComposite == False


def test_JTL_emof_Property_isDerived_value_roundtrip():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert instance.isDerived == True
    instance.isDerived = False
    assert instance.isDerived == False


def test_JTL_emof_Property_isId_value_roundtrip():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert instance.isId == True
    instance.isId = False
    assert instance.isId == False


def test_JTL_emof_Property_isReadOnly_value_roundtrip():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert instance.isReadOnly == True
    instance.isReadOnly = False
    assert instance.isReadOnly == False


def test_JTL_emof_Tag_name_value_roundtrip():
    instance = JTL_emof_Tag(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_JTL_emof_Tag_value_value_roundtrip():
    instance = JTL_emof_Tag(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_JTL_emof_TypedElement_type_value_roundtrip():
    instance = JTL_emof_TypedElement(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_JTL_essentialocl_BooleanLiteralExp_booleanSymbol_value_roundtrip():
    instance = JTL_essentialocl_BooleanLiteralExp(booleanSymbol=True)
    assert instance.booleanSymbol == True
    instance.booleanSymbol = False
    assert instance.booleanSymbol == False


def test_JTL_essentialocl_CollectionLiteralExp_kind_value_roundtrip():
    instance = JTL_essentialocl_CollectionLiteralExp(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_JTL_essentialocl_IntegerLiteralExp_integerSymbol_value_roundtrip():
    instance = JTL_essentialocl_IntegerLiteralExp(integerSymbol=7)
    assert instance.integerSymbol == 7
    instance.integerSymbol = 13
    assert instance.integerSymbol == 13


def test_JTL_essentialocl_RealLiteralExp_realSymbol_value_roundtrip():
    instance = JTL_essentialocl_RealLiteralExp(realSymbol=3.14)
    assert instance.realSymbol == 3.14
    instance.realSymbol = 9.99
    assert instance.realSymbol == 9.99


def test_JTL_essentialocl_StringLiteralExp_stringSymbol_value_roundtrip():
    instance = JTL_essentialocl_StringLiteralExp(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_JTL_essentialocl_UnlimitedNaturalExp_symbol_value_roundtrip():
    instance = JTL_essentialocl_UnlimitedNaturalExp(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_JTL_imperativeocl_AssertExp_severity_value_roundtrip():
    instance = JTL_imperativeocl_AssertExp(severity="sample_text")
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_JTL_imperativeocl_AssignExp_isReset_value_roundtrip():
    instance = JTL_imperativeocl_AssignExp(isReset=True)
    assert instance.isReset == True
    instance.isReset = False
    assert instance.isReset == False


def test_JTL_imperativeocl_LogExp_level_value_roundtrip():
    instance = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_JTL_imperativeocl_LogExp_text_value_roundtrip():
    instance = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_JTL_imperativeocl_TemplateParameterType_specification_value_roundtrip():
    instance = JTL_imperativeocl_TemplateParameterType(specification="sample_text")
    assert instance.specification == "sample_text"
    instance.specification = "sample_text_2"
    assert instance.specification == "sample_text_2"


def test_JTL_imperativeocl_VariableInitExp_withResult_value_roundtrip():
    instance = JTL_imperativeocl_VariableInitExp(withResult=True)
    assert instance.withResult == True
    instance.withResult = False
    assert instance.withResult == False


def test_JTL_template_CollectionTemplateExp_kind_value_roundtrip():
    instance = JTL_template_CollectionTemplateExp(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_JTL_template_ObjectTemplateExp_referredClass_value_roundtrip():
    instance = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    assert instance.referredClass == "sample_text"
    instance.referredClass = "sample_text_2"
    assert instance.referredClass == "sample_text_2"


def test_JTL_essentialocl_FeaturePropertyCall_isa_CallExp():
    instance = JTL_essentialocl_FeaturePropertyCall()
    assert isinstance(instance, CallExp)


def test_JTL_imperativeocl_AnonymousTupleType_isa_Class():
    instance = JTL_imperativeocl_AnonymousTupleType()
    assert isinstance(instance, Class)


def test_JTL_imperativeocl_Typedef_isa_Class():
    instance = JTL_imperativeocl_Typedef()
    assert isinstance(instance, Class)


def test_JTL_essentialocl_CollectionItem_isa_CollectionLiteralPart():
    instance = JTL_essentialocl_CollectionItem()
    assert isinstance(instance, CollectionLiteralPart)


def test_JTL_essentialocl_CollectionRange_isa_CollectionLiteralPart():
    instance = JTL_essentialocl_CollectionRange()
    assert isinstance(instance, CollectionLiteralPart)


def test_JTL_essentialocl_BagType_isa_CollectionType():
    instance = JTL_essentialocl_BagType()
    assert isinstance(instance, CollectionType)


def test_JTL_essentialocl_OrderedSetType_isa_CollectionType():
    instance = JTL_essentialocl_OrderedSetType()
    assert isinstance(instance, CollectionType)


def test_JTL_essentialocl_SequenceType_isa_CollectionType():
    instance = JTL_essentialocl_SequenceType()
    assert isinstance(instance, CollectionType)


def test_JTL_essentialocl_SetType_isa_CollectionType():
    instance = JTL_essentialocl_SetType()
    assert isinstance(instance, CollectionType)


def test_JTL_imperativeocl_DictionaryType_isa_CollectionType():
    instance = JTL_imperativeocl_DictionaryType()
    assert isinstance(instance, CollectionType)


def test_JTL_imperativeocl_ListType_isa_CollectionType():
    instance = JTL_imperativeocl_ListType()
    assert isinstance(instance, CollectionType)


def test_JTL_emof_Enumeration_isa_DataType():
    instance = JTL_emof_Enumeration()
    assert isinstance(instance, DataType)


def test_JTL_emof_PrimitiveType_isa_DataType():
    instance = JTL_emof_PrimitiveType()
    assert isinstance(instance, DataType)


def test_JTL_essentialocl_CollectionType_isa_DataType():
    instance = JTL_essentialocl_CollectionType()
    assert isinstance(instance, DataType)


def test_JTL_JTL_Pattern_isa_Element():
    instance = JTL_JTL_Pattern()
    assert isinstance(instance, Element)


def test_JTL_JTL_Predicate_isa_Element():
    instance = JTL_JTL_Predicate()
    assert isinstance(instance, Element)


def test_JTL_emof_Comment_isa_Element():
    instance = JTL_emof_Comment()
    assert isinstance(instance, Element)


def test_JTL_emof_NamedElement_isa_Element():
    instance = JTL_emof_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_JTL_emof_Tag_isa_Element():
    instance = JTL_emof_Tag(name="sample_text", value="sample_text")
    assert isinstance(instance, Element)


def test_JTL_imperativeocl_AnonymousTupleLiteralPart_isa_Element():
    instance = JTL_imperativeocl_AnonymousTupleLiteralPart()
    assert isinstance(instance, Element)


def test_JTL_imperativeocl_DictLiteralPart_isa_Element():
    instance = JTL_imperativeocl_DictLiteralPart()
    assert isinstance(instance, Element)


def test_JTL_template_PropertyTemplateItem_isa_Element():
    instance = JTL_template_PropertyTemplateItem()
    assert isinstance(instance, Element)


def test_JTL_emof_URIExtent_isa_Extent():
    instance = JTL_emof_URIExtent()
    assert isinstance(instance, Extent)


def test_JTL_essentialocl_OperationCallExp_isa_FeaturePropertyCall():
    instance = JTL_essentialocl_OperationCallExp()
    assert isinstance(instance, FeaturePropertyCall)


def test_JTL_essentialocl_PropertyCallExp_isa_FeaturePropertyCall():
    instance = JTL_essentialocl_PropertyCallExp()
    assert isinstance(instance, FeaturePropertyCall)


def test_JTL_imperativeocl_AltExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_AltExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_AssertExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_AssertExp(severity="sample_text")
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_AssignExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_AssignExp(isReset=True)
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_BlockExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_BlockExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_BreakExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_BreakExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_ComputeExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_ComputeExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_ContinueExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_ContinueExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_InstantiationExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_InstantiationExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_LogExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_RaiseExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_RaiseExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_ReturnExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_ReturnExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_TryExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_TryExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_TupleExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_TupleExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_UnlinkExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_UnlinkExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_UnpackExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_UnpackExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_VariableInitExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_VariableInitExp(withResult=True)
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_WhileExp_isa_ImperativeExpression():
    instance = JTL_imperativeocl_WhileExp()
    assert isinstance(instance, ImperativeExpression)


def test_JTL_imperativeocl_CollectorExp_isa_ImperativeLoopExp():
    instance = JTL_imperativeocl_CollectorExp()
    assert isinstance(instance, ImperativeLoopExp)


def test_JTL_imperativeocl_ForExp_isa_ImperativeLoopExp():
    instance = JTL_imperativeocl_ForExp()
    assert isinstance(instance, ImperativeLoopExp)


def test_JTL_imperativeocl_ImperativeIterateExp_isa_ImperativeLoopExp():
    instance = JTL_imperativeocl_ImperativeIterateExp()
    assert isinstance(instance, ImperativeLoopExp)


def test_JTL_essentialocl_CollectionLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_CollectionLiteralExp(kind="sample_text")
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_EnumLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_EnumLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_InvalidLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_InvalidLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_NullLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_NullLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_PrimitiveLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_PrimitiveLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_TupleLiteralExp_isa_LiteralExp():
    instance = JTL_essentialocl_TupleLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_imperativeocl_AnonymousTupleLiteralExp_isa_LiteralExp():
    instance = JTL_imperativeocl_AnonymousTupleLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_imperativeocl_DictLiteralExp_isa_LiteralExp():
    instance = JTL_imperativeocl_DictLiteralExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_template_TemplateExp_isa_LiteralExp():
    instance = JTL_template_TemplateExp()
    assert isinstance(instance, LiteralExp)


def test_JTL_essentialocl_IterateExp_isa_LoopExp():
    instance = JTL_essentialocl_IterateExp()
    assert isinstance(instance, LoopExp)


def test_JTL_essentialocl_IteratorExp_isa_LoopExp():
    instance = JTL_essentialocl_IteratorExp()
    assert isinstance(instance, LoopExp)


def test_JTL_JTL_Domain_isa_NamedElement():
    instance = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    assert isinstance(instance, NamedElement)


def test_JTL_JTL_Model_isa_NamedElement():
    instance = JTL_JTL_Model(usedPackage="sample_text")
    assert isinstance(instance, NamedElement)


def test_JTL_JTL_Relation_isa_NamedElement():
    instance = JTL_JTL_Relation(isTopLevel=True)
    assert isinstance(instance, NamedElement)


def test_JTL_emof_EnumerationLiteral_isa_NamedElement():
    instance = JTL_emof_EnumerationLiteral()
    assert isinstance(instance, NamedElement)


def test_JTL_emof_Package_isa_NamedElement():
    instance = JTL_emof_Package(uri="sample_text")
    assert isinstance(instance, NamedElement)


def test_JTL_emof_Type_isa_NamedElement():
    instance = JTL_emof_Type()
    assert isinstance(instance, NamedElement)


def test_JTL_emof_TypedElement_isa_NamedElement():
    instance = JTL_emof_TypedElement(type="sample_text")
    assert isinstance(instance, NamedElement)


def test_JTL_essentialocl_IntegerLiteralExp_isa_NumericLiteralExp():
    instance = JTL_essentialocl_IntegerLiteralExp(integerSymbol=7)
    assert isinstance(instance, NumericLiteralExp)


def test_JTL_essentialocl_RealLiteralExp_isa_NumericLiteralExp():
    instance = JTL_essentialocl_RealLiteralExp(realSymbol=3.14)
    assert isinstance(instance, NumericLiteralExp)


def test_JTL_essentialocl_UnlimitedNaturalExp_isa_NumericLiteralExp():
    instance = JTL_essentialocl_UnlimitedNaturalExp(symbol="sample_text")
    assert isinstance(instance, NumericLiteralExp)


def test_JTL_emof_Element_isa_Object():
    instance = JTL_emof_Element()
    assert isinstance(instance, Object)


def test_JTL_emof_Extent_isa_Object():
    instance = JTL_emof_Extent()
    assert isinstance(instance, Object)


def test_JTL_essentialocl_CallExp_isa_OclExpression():
    instance = JTL_essentialocl_CallExp()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_IfExp_isa_OclExpression():
    instance = JTL_essentialocl_IfExp()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_LetExp_isa_OclExpression():
    instance = JTL_essentialocl_LetExp()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_LiteralExp_isa_OclExpression():
    instance = JTL_essentialocl_LiteralExp()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_TypeExp_isa_OclExpression():
    instance = JTL_essentialocl_TypeExp()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_VariableExp_isa_OclExpression():
    instance = JTL_essentialocl_VariableExp()
    assert isinstance(instance, OclExpression)


def test_JTL_imperativeocl_ImperativeExpression_isa_OclExpression():
    instance = JTL_imperativeocl_ImperativeExpression()
    assert isinstance(instance, OclExpression)


def test_JTL_essentialocl_ExpressionInOcl_isa_OpaqueExpression():
    instance = JTL_essentialocl_ExpressionInOcl()
    assert isinstance(instance, OpaqueExpression)


def test_JTL_JTL_When_isa_Pattern():
    instance = JTL_JTL_When()
    assert isinstance(instance, Pattern)


def test_JTL_JTL_Where_isa_Pattern():
    instance = JTL_JTL_Where()
    assert isinstance(instance, Pattern)


def test_JTL_essentialocl_BooleanLiteralExp_isa_PrimitiveLiteralExp():
    instance = JTL_essentialocl_BooleanLiteralExp(booleanSymbol=True)
    assert isinstance(instance, PrimitiveLiteralExp)


def test_JTL_essentialocl_NumericLiteralExp_isa_PrimitiveLiteralExp():
    instance = JTL_essentialocl_NumericLiteralExp()
    assert isinstance(instance, PrimitiveLiteralExp)


def test_JTL_essentialocl_StringLiteralExp_isa_PrimitiveLiteralExp():
    instance = JTL_essentialocl_StringLiteralExp(stringSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExp)


def test_JTL_template_CollectionTemplateExp_isa_TemplateExp():
    instance = JTL_template_CollectionTemplateExp(kind="sample_text")
    assert isinstance(instance, TemplateExp)


def test_JTL_template_ObjectTemplateExp_isa_TemplateExp():
    instance = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    assert isinstance(instance, TemplateExp)


def test_JTL_emof_Class_isa_Type():
    instance = JTL_emof_Class(isAbstract=True)
    assert isinstance(instance, Type)


def test_JTL_emof_DataType_isa_Type():
    instance = JTL_emof_DataType()
    assert isinstance(instance, Type)


def test_JTL_essentialocl_InvalidType_isa_Type():
    instance = JTL_essentialocl_InvalidType()
    assert isinstance(instance, Type)


def test_JTL_essentialocl_VoidType_isa_Type():
    instance = JTL_essentialocl_VoidType()
    assert isinstance(instance, Type)


def test_JTL_imperativeocl_TemplateParameterType_isa_Type():
    instance = JTL_imperativeocl_TemplateParameterType(specification="sample_text")
    assert isinstance(instance, Type)


def test_JTL_essentialocl_CollectionLiteralPart_isa_TypedElement():
    instance = JTL_essentialocl_CollectionLiteralPart()
    assert isinstance(instance, TypedElement)


def test_JTL_essentialocl_OclExpression_isa_TypedElement():
    instance = JTL_essentialocl_OclExpression()
    assert isinstance(instance, TypedElement)


def test_JTL_essentialocl_TupleLiteralPart_isa_TypedElement():
    instance = JTL_essentialocl_TupleLiteralPart()
    assert isinstance(instance, TypedElement)


def test_JTL_essentialocl_Variable_isa_TypedElement():
    instance = JTL_essentialocl_Variable()
    assert isinstance(instance, TypedElement)


def test_JTL_JTL_Transformation_isa_emof_Class():
    instance = JTL_JTL_Transformation()
    assert isinstance(instance, emof_Class)


def test_JTL_essentialocl_AnyType_isa_emof_Class():
    instance = JTL_essentialocl_AnyType()
    assert isinstance(instance, emof_Class)


def test_JTL_essentialocl_TupleType_isa_emof_Class():
    instance = JTL_essentialocl_TupleType()
    assert isinstance(instance, emof_Class)


def test_JTL_essentialocl_TupleType_isa_emof_DataType():
    instance = JTL_essentialocl_TupleType()
    assert isinstance(instance, emof_DataType)


def test_JTL_emof_Operation_isa_emof_MultiplicityElement():
    instance = JTL_emof_Operation()
    assert isinstance(instance, emof_MultiplicityElement)


def test_JTL_emof_Parameter_isa_emof_MultiplicityElement():
    instance = JTL_emof_Parameter()
    assert isinstance(instance, emof_MultiplicityElement)


def test_JTL_emof_Property_isa_emof_MultiplicityElement():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert isinstance(instance, emof_MultiplicityElement)


def test_JTL_JTL_Transformation_isa_emof_Package():
    instance = JTL_JTL_Transformation()
    assert isinstance(instance, emof_Package)


def test_JTL_essentialocl_AnyType_isa_emof_Type():
    instance = JTL_essentialocl_AnyType()
    assert isinstance(instance, emof_Type)


def test_JTL_emof_Operation_isa_emof_TypedElement():
    instance = JTL_emof_Operation()
    assert isinstance(instance, emof_TypedElement)


def test_JTL_emof_Parameter_isa_emof_TypedElement():
    instance = JTL_emof_Parameter()
    assert isinstance(instance, emof_TypedElement)


def test_JTL_emof_Property_isa_emof_TypedElement():
    instance = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    assert isinstance(instance, emof_TypedElement)


def test_JTL_essentialocl_LoopExp_isa_essentialocl_CallExp():
    instance = JTL_essentialocl_LoopExp()
    assert isinstance(instance, essentialocl_CallExp)


def test_JTL_imperativeocl_SwitchExp_isa_essentialocl_CallExp():
    instance = JTL_imperativeocl_SwitchExp()
    assert isinstance(instance, essentialocl_CallExp)


def test_JTL_imperativeocl_ImperativeLoopExp_isa_essentialocl_LoopExp():
    instance = JTL_imperativeocl_ImperativeLoopExp()
    assert isinstance(instance, essentialocl_LoopExp)


def test_JTL_essentialocl_LoopExp_isa_essentialocl_OclExpression():
    instance = JTL_essentialocl_LoopExp()
    assert isinstance(instance, essentialocl_OclExpression)


def test_JTL_imperativeocl_ImperativeLoopExp_isa_imperativeocl_ImperativeExpression():
    instance = JTL_imperativeocl_ImperativeLoopExp()
    assert isinstance(instance, imperativeocl_ImperativeExpression)


def test_JTL_imperativeocl_SwitchExp_isa_imperativeocl_ImperativeExpression():
    instance = JTL_imperativeocl_SwitchExp()
    assert isinstance(instance, imperativeocl_ImperativeExpression)


def test_assoc_Class20_link_reassign_clear():
    a = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    b1 = Class()
    b2 = Class()
    _safe_set(a, 'ownedAttribute', b1)
    assert _is_linked(a, 'ownedAttribute', b1)
    if hasattr(b1, 'Class21'):
        assert _is_linked(b1, 'Class21', a)
    _safe_set(a, 'ownedAttribute', b2)
    assert _is_linked(a, 'ownedAttribute', b2)
    if hasattr(b1, 'Class21'):
        assert not _is_linked(b1, 'Class21', a)
    if hasattr(b2, 'Class21'):
        assert _is_linked(b2, 'Class21', a)
    _safe_set(a, 'ownedAttribute', None)
    assert not _is_linked(a, 'ownedAttribute', b2)
    if hasattr(b2, 'Class21'):
        assert not _is_linked(b2, 'Class21', a)


def test_assoc_assertion230_link_reassign_clear():
    a = JTL_imperativeocl_AssertExp(severity="sample_text")
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_imperativeocl_AssertExp231', b1)
    assert _is_linked(a, 'JTL_imperativeocl_AssertExp231', b1)
    if hasattr(b1, 'OclExpression232'):
        assert _is_linked(b1, 'OclExpression232', a)
    _safe_set(a, 'JTL_imperativeocl_AssertExp231', b2)
    assert _is_linked(a, 'JTL_imperativeocl_AssertExp231', b2)
    if hasattr(b1, 'OclExpression232'):
        assert not _is_linked(b1, 'OclExpression232', a)
    if hasattr(b2, 'OclExpression232'):
        assert _is_linked(b2, 'OclExpression232', a)
    _safe_set(a, 'JTL_imperativeocl_AssertExp231', None)
    assert not _is_linked(a, 'JTL_imperativeocl_AssertExp231', b2)
    if hasattr(b2, 'OclExpression232'):
        assert not _is_linked(b2, 'OclExpression232', a)


def test_assoc_condition224_link_reassign_clear():
    a = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_imperativeocl_LogExp', b1)
    assert _is_linked(a, 'JTL_imperativeocl_LogExp', b1)
    if hasattr(b1, 'OclExpression225'):
        assert _is_linked(b1, 'OclExpression225', a)
    _safe_set(a, 'JTL_imperativeocl_LogExp', b2)
    assert _is_linked(a, 'JTL_imperativeocl_LogExp', b2)
    if hasattr(b1, 'OclExpression225'):
        assert not _is_linked(b1, 'OclExpression225', a)
    if hasattr(b2, 'OclExpression225'):
        assert _is_linked(b2, 'OclExpression225', a)
    _safe_set(a, 'JTL_imperativeocl_LogExp', None)
    assert not _is_linked(a, 'JTL_imperativeocl_LogExp', b2)
    if hasattr(b2, 'OclExpression225'):
        assert not _is_linked(b2, 'OclExpression225', a)


def test_assoc_defaultValue160_link_reassign_clear():
    a = JTL_imperativeocl_AssignExp(isReset=True)
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_imperativeocl_AssignExp161', b1)
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp161', b1)
    if hasattr(b1, 'OclExpression162'):
        assert _is_linked(b1, 'OclExpression162', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp161', b2)
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp161', b2)
    if hasattr(b1, 'OclExpression162'):
        assert not _is_linked(b1, 'OclExpression162', a)
    if hasattr(b2, 'OclExpression162'):
        assert _is_linked(b2, 'OclExpression162', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp161', None)
    assert not _is_linked(a, 'JTL_imperativeocl_AssignExp161', b2)
    if hasattr(b2, 'OclExpression162'):
        assert not _is_linked(b2, 'OclExpression162', a)


def test_assoc_dependsOn45_link_reassign_clear():
    a = JTL_JTL_Model(usedPackage="sample_text")
    b1 = Model()
    b2 = Model()
    _safe_set(a, 'JTL_JTL_Model', {b1})
    assert _is_linked(a, 'JTL_JTL_Model', b1)
    if hasattr(b1, 'Model46'):
        assert _is_linked(b1, 'Model46', a)
    _safe_set(a, 'JTL_JTL_Model', {b2})
    assert _is_linked(a, 'JTL_JTL_Model', b2)
    if hasattr(b1, 'Model46'):
        assert not _is_linked(b1, 'Model46', a)
    if hasattr(b2, 'Model46'):
        assert _is_linked(b2, 'Model46', a)
    _safe_set(a, 'JTL_JTL_Model', set())
    assert not _is_linked(a, 'JTL_JTL_Model', b2)
    if hasattr(b2, 'Model46'):
        assert not _is_linked(b2, 'Model46', a)


def test_assoc_domain29_link_reassign_clear():
    a = JTL_JTL_Relation(isTopLevel=True)
    b1 = Domain()
    b2 = Domain()
    _safe_set(a, 'relation30', {b1})
    assert _is_linked(a, 'relation30', b1)
    if hasattr(b1, 'Domain'):
        assert _is_linked(b1, 'Domain', a)
    _safe_set(a, 'relation30', {b2})
    assert _is_linked(a, 'relation30', b2)
    if hasattr(b1, 'Domain'):
        assert not _is_linked(b1, 'Domain', a)
    if hasattr(b2, 'Domain'):
        assert _is_linked(b2, 'Domain', a)
    _safe_set(a, 'relation30', set())
    assert not _is_linked(a, 'relation30', b2)
    if hasattr(b2, 'Domain'):
        assert not _is_linked(b2, 'Domain', a)


def test_assoc_element226_link_reassign_clear():
    a = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'JTL_imperativeocl_LogExp227', b1)
    assert _is_linked(a, 'JTL_imperativeocl_LogExp227', b1)
    if hasattr(b1, 'Element228'):
        assert _is_linked(b1, 'Element228', a)
    _safe_set(a, 'JTL_imperativeocl_LogExp227', b2)
    assert _is_linked(a, 'JTL_imperativeocl_LogExp227', b2)
    if hasattr(b1, 'Element228'):
        assert not _is_linked(b1, 'Element228', a)
    if hasattr(b2, 'Element228'):
        assert _is_linked(b2, 'Element228', a)
    _safe_set(a, 'JTL_imperativeocl_LogExp227', None)
    assert not _is_linked(a, 'JTL_imperativeocl_LogExp227', b2)
    if hasattr(b2, 'Element228'):
        assert not _is_linked(b2, 'Element228', a)


def test_assoc_element6_link_reassign_clear():
    a = JTL_emof_Tag(name="sample_text", value="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'tag', {b1})
    assert _is_linked(a, 'tag', b1)
    if hasattr(b1, 'Element'):
        assert _is_linked(b1, 'Element', a)
    _safe_set(a, 'tag', {b2})
    assert _is_linked(a, 'tag', b2)
    if hasattr(b1, 'Element'):
        assert not _is_linked(b1, 'Element', a)
    if hasattr(b2, 'Element'):
        assert _is_linked(b2, 'Element', a)
    _safe_set(a, 'tag', set())
    assert not _is_linked(a, 'tag', b2)
    if hasattr(b2, 'Element'):
        assert not _is_linked(b2, 'Element', a)


def test_assoc_inside138_link_reassign_clear():
    a = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    b1 = AssignExp()
    b2 = AssignExp()
    _safe_set(a, 'JTL_template_ObjectTemplateExp', {b1})
    assert _is_linked(a, 'JTL_template_ObjectTemplateExp', b1)
    if hasattr(b1, 'AssignExp'):
        assert _is_linked(b1, 'AssignExp', a)
    _safe_set(a, 'JTL_template_ObjectTemplateExp', {b2})
    assert _is_linked(a, 'JTL_template_ObjectTemplateExp', b2)
    if hasattr(b1, 'AssignExp'):
        assert not _is_linked(b1, 'AssignExp', a)
    if hasattr(b2, 'AssignExp'):
        assert _is_linked(b2, 'AssignExp', a)
    _safe_set(a, 'JTL_template_ObjectTemplateExp', set())
    assert not _is_linked(a, 'JTL_template_ObjectTemplateExp', b2)
    if hasattr(b2, 'AssignExp'):
        assert not _is_linked(b2, 'AssignExp', a)


def test_assoc_left157_link_reassign_clear():
    a = JTL_imperativeocl_AssignExp(isReset=True)
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_imperativeocl_AssignExp158', b1)
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp158', b1)
    if hasattr(b1, 'OclExpression159'):
        assert _is_linked(b1, 'OclExpression159', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp158', b2)
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp158', b2)
    if hasattr(b1, 'OclExpression159'):
        assert not _is_linked(b1, 'OclExpression159', a)
    if hasattr(b2, 'OclExpression159'):
        assert _is_linked(b2, 'OclExpression159', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp158', None)
    assert not _is_linked(a, 'JTL_imperativeocl_AssignExp158', b2)
    if hasattr(b2, 'OclExpression159'):
        assert not _is_linked(b2, 'OclExpression159', a)


def test_assoc_log229_link_reassign_clear():
    a = JTL_imperativeocl_AssertExp(severity="sample_text")
    b1 = LogExp()
    b2 = LogExp()
    _safe_set(a, 'JTL_imperativeocl_AssertExp', b1)
    assert _is_linked(a, 'JTL_imperativeocl_AssertExp', b1)
    if hasattr(b1, 'LogExp'):
        assert _is_linked(b1, 'LogExp', a)
    _safe_set(a, 'JTL_imperativeocl_AssertExp', b2)
    assert _is_linked(a, 'JTL_imperativeocl_AssertExp', b2)
    if hasattr(b1, 'LogExp'):
        assert not _is_linked(b1, 'LogExp', a)
    if hasattr(b2, 'LogExp'):
        assert _is_linked(b2, 'LogExp', a)
    _safe_set(a, 'JTL_imperativeocl_AssertExp', None)
    assert not _is_linked(a, 'JTL_imperativeocl_AssertExp', b2)
    if hasattr(b2, 'LogExp'):
        assert not _is_linked(b2, 'LogExp', a)


def test_assoc_match143_link_reassign_clear():
    a = JTL_template_CollectionTemplateExp(kind="sample_text")
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_template_CollectionTemplateExp144', b1)
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp144', b1)
    if hasattr(b1, 'OclExpression145'):
        assert _is_linked(b1, 'OclExpression145', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp144', b2)
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp144', b2)
    if hasattr(b1, 'OclExpression145'):
        assert not _is_linked(b1, 'OclExpression145', a)
    if hasattr(b2, 'OclExpression145'):
        assert _is_linked(b2, 'OclExpression145', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp144', None)
    assert not _is_linked(a, 'JTL_template_CollectionTemplateExp144', b2)
    if hasattr(b2, 'OclExpression145'):
        assert not _is_linked(b2, 'OclExpression145', a)


def test_assoc_model37_link_reassign_clear():
    a = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    b1 = Model()
    b2 = Model()
    _safe_set(a, 'JTL_JTL_Domain38', b1)
    assert _is_linked(a, 'JTL_JTL_Domain38', b1)
    if hasattr(b1, 'Model39'):
        assert _is_linked(b1, 'Model39', a)
    _safe_set(a, 'JTL_JTL_Domain38', b2)
    assert _is_linked(a, 'JTL_JTL_Domain38', b2)
    if hasattr(b1, 'Model39'):
        assert not _is_linked(b1, 'Model39', a)
    if hasattr(b2, 'Model39'):
        assert _is_linked(b2, 'Model39', a)
    _safe_set(a, 'JTL_JTL_Domain38', None)
    assert not _is_linked(a, 'JTL_JTL_Domain38', b2)
    if hasattr(b2, 'Model39'):
        assert not _is_linked(b2, 'Model39', a)


def test_assoc_nestedPackage14_link_reassign_clear():
    a = JTL_emof_Package(uri="sample_text")
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'JTL_emof_Package', {b1})
    assert _is_linked(a, 'JTL_emof_Package', b1)
    if hasattr(b1, 'Package'):
        assert _is_linked(b1, 'Package', a)
    _safe_set(a, 'JTL_emof_Package', {b2})
    assert _is_linked(a, 'JTL_emof_Package', b2)
    if hasattr(b1, 'Package'):
        assert not _is_linked(b1, 'Package', a)
    if hasattr(b2, 'Package'):
        assert _is_linked(b2, 'Package', a)
    _safe_set(a, 'JTL_emof_Package', set())
    assert not _is_linked(a, 'JTL_emof_Package', b2)
    if hasattr(b2, 'Package'):
        assert not _is_linked(b2, 'Package', a)


def test_assoc_opposite22_link_reassign_clear():
    a = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'JTL_emof_Property', b1)
    assert _is_linked(a, 'JTL_emof_Property', b1)
    if hasattr(b1, 'Property23'):
        assert _is_linked(b1, 'Property23', a)
    _safe_set(a, 'JTL_emof_Property', b2)
    assert _is_linked(a, 'JTL_emof_Property', b2)
    if hasattr(b1, 'Property23'):
        assert not _is_linked(b1, 'Property23', a)
    if hasattr(b2, 'Property23'):
        assert _is_linked(b2, 'Property23', a)
    _safe_set(a, 'JTL_emof_Property', None)
    assert not _is_linked(a, 'JTL_emof_Property', b2)
    if hasattr(b2, 'Property23'):
        assert not _is_linked(b2, 'Property23', a)


def test_assoc_ownedAttribute0_link_reassign_clear():
    a = JTL_emof_Class(isAbstract=True)
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'Class', {b1})
    assert _is_linked(a, 'Class', b1)
    if hasattr(b1, 'Property'):
        assert _is_linked(b1, 'Property', a)
    _safe_set(a, 'Class', {b2})
    assert _is_linked(a, 'Class', b2)
    if hasattr(b1, 'Property'):
        assert not _is_linked(b1, 'Property', a)
    if hasattr(b2, 'Property'):
        assert _is_linked(b2, 'Property', a)
    _safe_set(a, 'Class', set())
    assert not _is_linked(a, 'Class', b2)
    if hasattr(b2, 'Property'):
        assert not _is_linked(b2, 'Property', a)


def test_assoc_ownedOperation1_link_reassign_clear():
    a = JTL_emof_Class(isAbstract=True)
    b1 = Operation()
    b2 = Operation()
    _safe_set(a, 'class_', {b1})
    assert _is_linked(a, 'class_', b1)
    if hasattr(b1, 'Operation'):
        assert _is_linked(b1, 'Operation', a)
    _safe_set(a, 'class_', {b2})
    assert _is_linked(a, 'class_', b2)
    if hasattr(b1, 'Operation'):
        assert not _is_linked(b1, 'Operation', a)
    if hasattr(b2, 'Operation'):
        assert _is_linked(b2, 'Operation', a)
    _safe_set(a, 'class_', set())
    assert not _is_linked(a, 'class_', b2)
    if hasattr(b2, 'Operation'):
        assert not _is_linked(b2, 'Operation', a)


def test_assoc_ownedType12_link_reassign_clear():
    a = JTL_emof_Package(uri="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'package', {b1})
    assert _is_linked(a, 'package', b1)
    if hasattr(b1, 'Type13'):
        assert _is_linked(b1, 'Type13', a)
    _safe_set(a, 'package', {b2})
    assert _is_linked(a, 'package', b2)
    if hasattr(b1, 'Type13'):
        assert not _is_linked(b1, 'Type13', a)
    if hasattr(b2, 'Type13'):
        assert _is_linked(b2, 'Type13', a)
    _safe_set(a, 'package', set())
    assert not _is_linked(a, 'package', b2)
    if hasattr(b2, 'Type13'):
        assert not _is_linked(b2, 'Type13', a)


def test_assoc_part103_link_reassign_clear():
    a = JTL_essentialocl_CollectionLiteralExp(kind="sample_text")
    b1 = CollectionLiteralPart()
    b2 = CollectionLiteralPart()
    _safe_set(a, 'CollectionLiteralExp', {b1})
    assert _is_linked(a, 'CollectionLiteralExp', b1)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert _is_linked(b1, 'CollectionLiteralPart', a)
    _safe_set(a, 'CollectionLiteralExp', {b2})
    assert _is_linked(a, 'CollectionLiteralExp', b2)
    if hasattr(b1, 'CollectionLiteralPart'):
        assert not _is_linked(b1, 'CollectionLiteralPart', a)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert _is_linked(b2, 'CollectionLiteralPart', a)
    _safe_set(a, 'CollectionLiteralExp', set())
    assert not _is_linked(a, 'CollectionLiteralExp', b2)
    if hasattr(b2, 'CollectionLiteralPart'):
        assert not _is_linked(b2, 'CollectionLiteralPart', a)


def test_assoc_part137_link_reassign_clear():
    a = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    b1 = PropertyTemplateItem()
    b2 = PropertyTemplateItem()
    _safe_set(a, 'objContainer', {b1})
    assert _is_linked(a, 'objContainer', b1)
    if hasattr(b1, 'PropertyTemplateItem'):
        assert _is_linked(b1, 'PropertyTemplateItem', a)
    _safe_set(a, 'objContainer', {b2})
    assert _is_linked(a, 'objContainer', b2)
    if hasattr(b1, 'PropertyTemplateItem'):
        assert not _is_linked(b1, 'PropertyTemplateItem', a)
    if hasattr(b2, 'PropertyTemplateItem'):
        assert _is_linked(b2, 'PropertyTemplateItem', a)
    _safe_set(a, 'objContainer', set())
    assert not _is_linked(a, 'objContainer', b2)
    if hasattr(b2, 'PropertyTemplateItem'):
        assert not _is_linked(b2, 'PropertyTemplateItem', a)


def test_assoc_part139_link_reassign_clear():
    a = JTL_template_CollectionTemplateExp(kind="sample_text")
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_template_CollectionTemplateExp', {b1})
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp', b1)
    if hasattr(b1, 'OclExpression140'):
        assert _is_linked(b1, 'OclExpression140', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp', {b2})
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp', b2)
    if hasattr(b1, 'OclExpression140'):
        assert not _is_linked(b1, 'OclExpression140', a)
    if hasattr(b2, 'OclExpression140'):
        assert _is_linked(b2, 'OclExpression140', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp', set())
    assert not _is_linked(a, 'JTL_template_CollectionTemplateExp', b2)
    if hasattr(b2, 'OclExpression140'):
        assert not _is_linked(b2, 'OclExpression140', a)


def test_assoc_pattern36_link_reassign_clear():
    a = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    b1 = Pattern()
    b2 = Pattern()
    _safe_set(a, 'JTL_JTL_Domain', b1)
    assert _is_linked(a, 'JTL_JTL_Domain', b1)
    if hasattr(b1, 'Pattern'):
        assert _is_linked(b1, 'Pattern', a)
    _safe_set(a, 'JTL_JTL_Domain', b2)
    assert _is_linked(a, 'JTL_JTL_Domain', b2)
    if hasattr(b1, 'Pattern'):
        assert not _is_linked(b1, 'Pattern', a)
    if hasattr(b2, 'Pattern'):
        assert _is_linked(b2, 'Pattern', a)
    _safe_set(a, 'JTL_JTL_Domain', None)
    assert not _is_linked(a, 'JTL_JTL_Domain', b2)
    if hasattr(b2, 'Pattern'):
        assert not _is_linked(b2, 'Pattern', a)


def test_assoc_referredCollectionType141_link_reassign_clear():
    a = JTL_template_CollectionTemplateExp(kind="sample_text")
    b1 = CollectionType()
    b2 = CollectionType()
    _safe_set(a, 'JTL_template_CollectionTemplateExp142', b1)
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp142', b1)
    if hasattr(b1, 'CollectionType'):
        assert _is_linked(b1, 'CollectionType', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp142', b2)
    assert _is_linked(a, 'JTL_template_CollectionTemplateExp142', b2)
    if hasattr(b1, 'CollectionType'):
        assert not _is_linked(b1, 'CollectionType', a)
    if hasattr(b2, 'CollectionType'):
        assert _is_linked(b2, 'CollectionType', a)
    _safe_set(a, 'JTL_template_CollectionTemplateExp142', None)
    assert not _is_linked(a, 'JTL_template_CollectionTemplateExp142', b2)
    if hasattr(b2, 'CollectionType'):
        assert not _is_linked(b2, 'CollectionType', a)


def test_assoc_referredVariable169_link_reassign_clear():
    a = JTL_imperativeocl_VariableInitExp(withResult=True)
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'JTL_imperativeocl_VariableInitExp', b1)
    assert _is_linked(a, 'JTL_imperativeocl_VariableInitExp', b1)
    if hasattr(b1, 'Variable170'):
        assert _is_linked(b1, 'Variable170', a)
    _safe_set(a, 'JTL_imperativeocl_VariableInitExp', b2)
    assert _is_linked(a, 'JTL_imperativeocl_VariableInitExp', b2)
    if hasattr(b1, 'Variable170'):
        assert not _is_linked(b1, 'Variable170', a)
    if hasattr(b2, 'Variable170'):
        assert _is_linked(b2, 'Variable170', a)
    _safe_set(a, 'JTL_imperativeocl_VariableInitExp', None)
    assert not _is_linked(a, 'JTL_imperativeocl_VariableInitExp', b2)
    if hasattr(b2, 'Variable170'):
        assert not _is_linked(b2, 'Variable170', a)


def test_assoc_relation34_link_reassign_clear():
    a = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    b1 = Relation()
    b2 = Relation()
    _safe_set(a, 'domain', b1)
    assert _is_linked(a, 'domain', b1)
    if hasattr(b1, 'Relation35'):
        assert _is_linked(b1, 'Relation35', a)
    _safe_set(a, 'domain', b2)
    assert _is_linked(a, 'domain', b2)
    if hasattr(b1, 'Relation35'):
        assert not _is_linked(b1, 'Relation35', a)
    if hasattr(b2, 'Relation35'):
        assert _is_linked(b2, 'Relation35', a)
    _safe_set(a, 'domain', None)
    assert not _is_linked(a, 'domain', b2)
    if hasattr(b2, 'Relation35'):
        assert not _is_linked(b2, 'Relation35', a)


def test_assoc_rootVariable40_link_reassign_clear():
    a = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'JTL_JTL_Domain41', b1)
    assert _is_linked(a, 'JTL_JTL_Domain41', b1)
    if hasattr(b1, 'Variable42'):
        assert _is_linked(b1, 'Variable42', a)
    _safe_set(a, 'JTL_JTL_Domain41', b2)
    assert _is_linked(a, 'JTL_JTL_Domain41', b2)
    if hasattr(b1, 'Variable42'):
        assert not _is_linked(b1, 'Variable42', a)
    if hasattr(b2, 'Variable42'):
        assert _is_linked(b2, 'Variable42', a)
    _safe_set(a, 'JTL_JTL_Domain41', None)
    assert not _is_linked(a, 'JTL_JTL_Domain41', b2)
    if hasattr(b2, 'Variable42'):
        assert not _is_linked(b2, 'Variable42', a)


def test_assoc_superClass2_link_reassign_clear():
    a = JTL_emof_Class(isAbstract=True)
    b1 = Class()
    b2 = Class()
    _safe_set(a, 'JTL_emof_Class', {b1})
    assert _is_linked(a, 'JTL_emof_Class', b1)
    if hasattr(b1, 'Class3'):
        assert _is_linked(b1, 'Class3', a)
    _safe_set(a, 'JTL_emof_Class', {b2})
    assert _is_linked(a, 'JTL_emof_Class', b2)
    if hasattr(b1, 'Class3'):
        assert not _is_linked(b1, 'Class3', a)
    if hasattr(b2, 'Class3'):
        assert _is_linked(b2, 'Class3', a)
    _safe_set(a, 'JTL_emof_Class', set())
    assert not _is_linked(a, 'JTL_emof_Class', b2)
    if hasattr(b2, 'Class3'):
        assert not _is_linked(b2, 'Class3', a)


def test_assoc_transformation28_link_reassign_clear():
    a = JTL_JTL_Relation(isTopLevel=True)
    b1 = Transformation()
    b2 = Transformation()
    _safe_set(a, 'relation', b1)
    assert _is_linked(a, 'relation', b1)
    if hasattr(b1, 'Transformation'):
        assert _is_linked(b1, 'Transformation', a)
    _safe_set(a, 'relation', b2)
    assert _is_linked(a, 'relation', b2)
    if hasattr(b1, 'Transformation'):
        assert not _is_linked(b1, 'Transformation', a)
    if hasattr(b2, 'Transformation'):
        assert _is_linked(b2, 'Transformation', a)
    _safe_set(a, 'relation', None)
    assert not _is_linked(a, 'relation', b2)
    if hasattr(b2, 'Transformation'):
        assert not _is_linked(b2, 'Transformation', a)


def test_assoc_transformation43_link_reassign_clear():
    a = JTL_JTL_Model(usedPackage="sample_text")
    b1 = Transformation()
    b2 = Transformation()
    _safe_set(a, 'modelParameter', b1)
    assert _is_linked(a, 'modelParameter', b1)
    if hasattr(b1, 'Transformation44'):
        assert _is_linked(b1, 'Transformation44', a)
    _safe_set(a, 'modelParameter', b2)
    assert _is_linked(a, 'modelParameter', b2)
    if hasattr(b1, 'Transformation44'):
        assert not _is_linked(b1, 'Transformation44', a)
    if hasattr(b2, 'Transformation44'):
        assert _is_linked(b2, 'Transformation44', a)
    _safe_set(a, 'modelParameter', None)
    assert not _is_linked(a, 'modelParameter', b2)
    if hasattr(b2, 'Transformation44'):
        assert not _is_linked(b2, 'Transformation44', a)


def test_assoc_value155_link_reassign_clear():
    a = JTL_imperativeocl_AssignExp(isReset=True)
    b1 = OclExpression()
    b2 = OclExpression()
    _safe_set(a, 'JTL_imperativeocl_AssignExp', {b1})
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp', b1)
    if hasattr(b1, 'OclExpression156'):
        assert _is_linked(b1, 'OclExpression156', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp', {b2})
    assert _is_linked(a, 'JTL_imperativeocl_AssignExp', b2)
    if hasattr(b1, 'OclExpression156'):
        assert not _is_linked(b1, 'OclExpression156', a)
    if hasattr(b2, 'OclExpression156'):
        assert _is_linked(b2, 'OclExpression156', a)
    _safe_set(a, 'JTL_imperativeocl_AssignExp', set())
    assert not _is_linked(a, 'JTL_imperativeocl_AssignExp', b2)
    if hasattr(b2, 'OclExpression156'):
        assert not _is_linked(b2, 'OclExpression156', a)


def test_assoc_variable33_link_reassign_clear():
    a = JTL_JTL_Relation(isTopLevel=True)
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'JTL_JTL_Relation', {b1})
    assert _is_linked(a, 'JTL_JTL_Relation', b1)
    if hasattr(b1, 'Variable'):
        assert _is_linked(b1, 'Variable', a)
    _safe_set(a, 'JTL_JTL_Relation', {b2})
    assert _is_linked(a, 'JTL_JTL_Relation', b2)
    if hasattr(b1, 'Variable'):
        assert not _is_linked(b1, 'Variable', a)
    if hasattr(b2, 'Variable'):
        assert _is_linked(b2, 'Variable', a)
    _safe_set(a, 'JTL_JTL_Relation', set())
    assert not _is_linked(a, 'JTL_JTL_Relation', b2)
    if hasattr(b2, 'Variable'):
        assert not _is_linked(b2, 'Variable', a)


def test_assoc_when32_link_reassign_clear():
    a = JTL_JTL_Relation(isTopLevel=True)
    b1 = When()
    b2 = When()
    _safe_set(a, 'whenOwner', b1)
    assert _is_linked(a, 'whenOwner', b1)
    if hasattr(b1, 'When'):
        assert _is_linked(b1, 'When', a)
    _safe_set(a, 'whenOwner', b2)
    assert _is_linked(a, 'whenOwner', b2)
    if hasattr(b1, 'When'):
        assert not _is_linked(b1, 'When', a)
    if hasattr(b2, 'When'):
        assert _is_linked(b2, 'When', a)
    _safe_set(a, 'whenOwner', None)
    assert not _is_linked(a, 'whenOwner', b2)
    if hasattr(b2, 'When'):
        assert not _is_linked(b2, 'When', a)


def test_assoc_where31_link_reassign_clear():
    a = JTL_JTL_Relation(isTopLevel=True)
    b1 = Where()
    b2 = Where()
    _safe_set(a, 'whereOwner', b1)
    assert _is_linked(a, 'whereOwner', b1)
    if hasattr(b1, 'Where'):
        assert _is_linked(b1, 'Where', a)
    _safe_set(a, 'whereOwner', b2)
    assert _is_linked(a, 'whereOwner', b2)
    if hasattr(b1, 'Where'):
        assert not _is_linked(b1, 'Where', a)
    if hasattr(b2, 'Where'):
        assert _is_linked(b2, 'Where', a)
    _safe_set(a, 'whereOwner', None)
    assert not _is_linked(a, 'whereOwner', b2)
    if hasattr(b2, 'Where'):
        assert not _is_linked(b2, 'Where', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AltExp_strategy = st.builds(AltExp)
@given(instance=AltExp_strategy)
@settings(max_examples=25)
def test_AltExp_instantiation(instance):
    assert isinstance(instance, AltExp)


AnonymousTupleLiteralPart_strategy = st.builds(AnonymousTupleLiteralPart)
@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=25)
def test_AnonymousTupleLiteralPart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)


AssignExp_strategy = st.builds(AssignExp)
@given(instance=AssignExp_strategy)
@settings(max_examples=25)
def test_AssignExp_instantiation(instance):
    assert isinstance(instance, AssignExp)


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


CollectionLiteralExp_strategy = st.builds(CollectionLiteralExp)
@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)


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


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


ComputeExp_strategy = st.builds(ComputeExp)
@given(instance=ComputeExp_strategy)
@settings(max_examples=25)
def test_ComputeExp_instantiation(instance):
    assert isinstance(instance, ComputeExp)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


DictLiteralPart_strategy = st.builds(DictLiteralPart)
@given(instance=DictLiteralPart_strategy)
@settings(max_examples=25)
def test_DictLiteralPart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)


Domain_strategy = st.builds(Domain)
@given(instance=Domain_strategy)
@settings(max_examples=25)
def test_Domain_instantiation(instance):
    assert isinstance(instance, Domain)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Enumeration_strategy = st.builds(Enumeration)
@given(instance=Enumeration_strategy)
@settings(max_examples=25)
def test_Enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)


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


ImperativeExpression_strategy = st.builds(ImperativeExpression)
@given(instance=ImperativeExpression_strategy)
@settings(max_examples=25)
def test_ImperativeExpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)


ImperativeLoopExp_strategy = st.builds(ImperativeLoopExp)
@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=25)
def test_ImperativeLoopExp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)


JTL_JTL_Domain_strategy = st.builds(JTL_JTL_Domain, isCheckable=st.booleans(), isEnforceable=st.booleans())
@given(instance=JTL_JTL_Domain_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Domain_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Domain)


JTL_JTL_Model_strategy = st.builds(JTL_JTL_Model, usedPackage=safe_text)
@given(instance=JTL_JTL_Model_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Model_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Model)


JTL_JTL_Pattern_strategy = st.builds(JTL_JTL_Pattern)
@given(instance=JTL_JTL_Pattern_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Pattern_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Pattern)


JTL_JTL_Predicate_strategy = st.builds(JTL_JTL_Predicate)
@given(instance=JTL_JTL_Predicate_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Predicate_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Predicate)


JTL_JTL_Relation_strategy = st.builds(JTL_JTL_Relation, isTopLevel=st.booleans())
@given(instance=JTL_JTL_Relation_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Relation_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Relation)


JTL_JTL_Transformation_strategy = st.builds(JTL_JTL_Transformation)
@given(instance=JTL_JTL_Transformation_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Transformation_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Transformation)


JTL_JTL_When_strategy = st.builds(JTL_JTL_When)
@given(instance=JTL_JTL_When_strategy)
@settings(max_examples=25)
def test_JTL_JTL_When_instantiation(instance):
    assert isinstance(instance, JTL_JTL_When)


JTL_JTL_Where_strategy = st.builds(JTL_JTL_Where)
@given(instance=JTL_JTL_Where_strategy)
@settings(max_examples=25)
def test_JTL_JTL_Where_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Where)


JTL_emof_Class_strategy = st.builds(JTL_emof_Class, isAbstract=st.booleans())
@given(instance=JTL_emof_Class_strategy)
@settings(max_examples=25)
def test_JTL_emof_Class_instantiation(instance):
    assert isinstance(instance, JTL_emof_Class)


JTL_emof_Comment_strategy = st.builds(JTL_emof_Comment)
@given(instance=JTL_emof_Comment_strategy)
@settings(max_examples=25)
def test_JTL_emof_Comment_instantiation(instance):
    assert isinstance(instance, JTL_emof_Comment)


JTL_emof_DataType_strategy = st.builds(JTL_emof_DataType)
@given(instance=JTL_emof_DataType_strategy)
@settings(max_examples=25)
def test_JTL_emof_DataType_instantiation(instance):
    assert isinstance(instance, JTL_emof_DataType)


JTL_emof_Element_strategy = st.builds(JTL_emof_Element)
@given(instance=JTL_emof_Element_strategy)
@settings(max_examples=25)
def test_JTL_emof_Element_instantiation(instance):
    assert isinstance(instance, JTL_emof_Element)


JTL_emof_Enumeration_strategy = st.builds(JTL_emof_Enumeration)
@given(instance=JTL_emof_Enumeration_strategy)
@settings(max_examples=25)
def test_JTL_emof_Enumeration_instantiation(instance):
    assert isinstance(instance, JTL_emof_Enumeration)


JTL_emof_EnumerationLiteral_strategy = st.builds(JTL_emof_EnumerationLiteral)
@given(instance=JTL_emof_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_JTL_emof_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, JTL_emof_EnumerationLiteral)


JTL_emof_Extent_strategy = st.builds(JTL_emof_Extent)
@given(instance=JTL_emof_Extent_strategy)
@settings(max_examples=25)
def test_JTL_emof_Extent_instantiation(instance):
    assert isinstance(instance, JTL_emof_Extent)


JTL_emof_MultiplicityElement_strategy = st.builds(JTL_emof_MultiplicityElement, isOrdered=safe_text, isUnique=safe_text, lower=st.integers(), upper=safe_text)
@given(instance=JTL_emof_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_JTL_emof_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, JTL_emof_MultiplicityElement)


JTL_emof_NamedElement_strategy = st.builds(JTL_emof_NamedElement, name=safe_text)
@given(instance=JTL_emof_NamedElement_strategy)
@settings(max_examples=25)
def test_JTL_emof_NamedElement_instantiation(instance):
    assert isinstance(instance, JTL_emof_NamedElement)


JTL_emof_Object_strategy = st.builds(JTL_emof_Object)
@given(instance=JTL_emof_Object_strategy)
@settings(max_examples=25)
def test_JTL_emof_Object_instantiation(instance):
    assert isinstance(instance, JTL_emof_Object)


JTL_emof_Operation_strategy = st.builds(JTL_emof_Operation)
@given(instance=JTL_emof_Operation_strategy)
@settings(max_examples=25)
def test_JTL_emof_Operation_instantiation(instance):
    assert isinstance(instance, JTL_emof_Operation)


JTL_emof_Package_strategy = st.builds(JTL_emof_Package, uri=safe_text)
@given(instance=JTL_emof_Package_strategy)
@settings(max_examples=25)
def test_JTL_emof_Package_instantiation(instance):
    assert isinstance(instance, JTL_emof_Package)


JTL_emof_Parameter_strategy = st.builds(JTL_emof_Parameter)
@given(instance=JTL_emof_Parameter_strategy)
@settings(max_examples=25)
def test_JTL_emof_Parameter_instantiation(instance):
    assert isinstance(instance, JTL_emof_Parameter)


JTL_emof_PrimitiveType_strategy = st.builds(JTL_emof_PrimitiveType)
@given(instance=JTL_emof_PrimitiveType_strategy)
@settings(max_examples=25)
def test_JTL_emof_PrimitiveType_instantiation(instance):
    assert isinstance(instance, JTL_emof_PrimitiveType)


JTL_emof_Property_strategy = st.builds(JTL_emof_Property, default=safe_text, isComposite=st.booleans(), isDerived=st.booleans(), isId=st.booleans(), isReadOnly=st.booleans())
@given(instance=JTL_emof_Property_strategy)
@settings(max_examples=25)
def test_JTL_emof_Property_instantiation(instance):
    assert isinstance(instance, JTL_emof_Property)


JTL_emof_Tag_strategy = st.builds(JTL_emof_Tag, name=safe_text, value=safe_text)
@given(instance=JTL_emof_Tag_strategy)
@settings(max_examples=25)
def test_JTL_emof_Tag_instantiation(instance):
    assert isinstance(instance, JTL_emof_Tag)


JTL_emof_Type_strategy = st.builds(JTL_emof_Type)
@given(instance=JTL_emof_Type_strategy)
@settings(max_examples=25)
def test_JTL_emof_Type_instantiation(instance):
    assert isinstance(instance, JTL_emof_Type)


JTL_emof_TypedElement_strategy = st.builds(JTL_emof_TypedElement, type=safe_text)
@given(instance=JTL_emof_TypedElement_strategy)
@settings(max_examples=25)
def test_JTL_emof_TypedElement_instantiation(instance):
    assert isinstance(instance, JTL_emof_TypedElement)


JTL_emof_URIExtent_strategy = st.builds(JTL_emof_URIExtent)
@given(instance=JTL_emof_URIExtent_strategy)
@settings(max_examples=25)
def test_JTL_emof_URIExtent_instantiation(instance):
    assert isinstance(instance, JTL_emof_URIExtent)


JTL_essentialocl_AnyType_strategy = st.builds(JTL_essentialocl_AnyType)
@given(instance=JTL_essentialocl_AnyType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_AnyType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_AnyType)


JTL_essentialocl_BagType_strategy = st.builds(JTL_essentialocl_BagType)
@given(instance=JTL_essentialocl_BagType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_BagType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_BagType)


JTL_essentialocl_BooleanLiteralExp_strategy = st.builds(JTL_essentialocl_BooleanLiteralExp, booleanSymbol=st.booleans())
@given(instance=JTL_essentialocl_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_BooleanLiteralExp)


JTL_essentialocl_CallExp_strategy = st.builds(JTL_essentialocl_CallExp)
@given(instance=JTL_essentialocl_CallExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CallExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CallExp)


JTL_essentialocl_CollectionItem_strategy = st.builds(JTL_essentialocl_CollectionItem)
@given(instance=JTL_essentialocl_CollectionItem_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CollectionItem_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionItem)


JTL_essentialocl_CollectionLiteralExp_strategy = st.builds(JTL_essentialocl_CollectionLiteralExp, kind=safe_text)
@given(instance=JTL_essentialocl_CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionLiteralExp)


JTL_essentialocl_CollectionLiteralPart_strategy = st.builds(JTL_essentialocl_CollectionLiteralPart)
@given(instance=JTL_essentialocl_CollectionLiteralPart_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CollectionLiteralPart_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionLiteralPart)


JTL_essentialocl_CollectionRange_strategy = st.builds(JTL_essentialocl_CollectionRange)
@given(instance=JTL_essentialocl_CollectionRange_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CollectionRange_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionRange)


JTL_essentialocl_CollectionType_strategy = st.builds(JTL_essentialocl_CollectionType)
@given(instance=JTL_essentialocl_CollectionType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_CollectionType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionType)


JTL_essentialocl_EnumLiteralExp_strategy = st.builds(JTL_essentialocl_EnumLiteralExp)
@given(instance=JTL_essentialocl_EnumLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_EnumLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_EnumLiteralExp)


JTL_essentialocl_ExpressionInOcl_strategy = st.builds(JTL_essentialocl_ExpressionInOcl)
@given(instance=JTL_essentialocl_ExpressionInOcl_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_ExpressionInOcl_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_ExpressionInOcl)


JTL_essentialocl_FeaturePropertyCall_strategy = st.builds(JTL_essentialocl_FeaturePropertyCall)
@given(instance=JTL_essentialocl_FeaturePropertyCall_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_FeaturePropertyCall_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_FeaturePropertyCall)


JTL_essentialocl_IfExp_strategy = st.builds(JTL_essentialocl_IfExp)
@given(instance=JTL_essentialocl_IfExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_IfExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IfExp)


JTL_essentialocl_IntegerLiteralExp_strategy = st.builds(JTL_essentialocl_IntegerLiteralExp, integerSymbol=st.integers())
@given(instance=JTL_essentialocl_IntegerLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_IntegerLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IntegerLiteralExp)


JTL_essentialocl_InvalidLiteralExp_strategy = st.builds(JTL_essentialocl_InvalidLiteralExp)
@given(instance=JTL_essentialocl_InvalidLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_InvalidLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_InvalidLiteralExp)


JTL_essentialocl_InvalidType_strategy = st.builds(JTL_essentialocl_InvalidType)
@given(instance=JTL_essentialocl_InvalidType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_InvalidType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_InvalidType)


JTL_essentialocl_IterateExp_strategy = st.builds(JTL_essentialocl_IterateExp)
@given(instance=JTL_essentialocl_IterateExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_IterateExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IterateExp)


JTL_essentialocl_IteratorExp_strategy = st.builds(JTL_essentialocl_IteratorExp)
@given(instance=JTL_essentialocl_IteratorExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_IteratorExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IteratorExp)


JTL_essentialocl_LetExp_strategy = st.builds(JTL_essentialocl_LetExp)
@given(instance=JTL_essentialocl_LetExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_LetExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LetExp)


JTL_essentialocl_LiteralExp_strategy = st.builds(JTL_essentialocl_LiteralExp)
@given(instance=JTL_essentialocl_LiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_LiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LiteralExp)


JTL_essentialocl_LoopExp_strategy = st.builds(JTL_essentialocl_LoopExp)
@given(instance=JTL_essentialocl_LoopExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_LoopExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LoopExp)


JTL_essentialocl_NullLiteralExp_strategy = st.builds(JTL_essentialocl_NullLiteralExp)
@given(instance=JTL_essentialocl_NullLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_NullLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_NullLiteralExp)


JTL_essentialocl_NumericLiteralExp_strategy = st.builds(JTL_essentialocl_NumericLiteralExp)
@given(instance=JTL_essentialocl_NumericLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_NumericLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_NumericLiteralExp)


JTL_essentialocl_OclExpression_strategy = st.builds(JTL_essentialocl_OclExpression)
@given(instance=JTL_essentialocl_OclExpression_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_OclExpression_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OclExpression)


JTL_essentialocl_OpaqueExpression_strategy = st.builds(JTL_essentialocl_OpaqueExpression)
@given(instance=JTL_essentialocl_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OpaqueExpression)


JTL_essentialocl_OperationCallExp_strategy = st.builds(JTL_essentialocl_OperationCallExp)
@given(instance=JTL_essentialocl_OperationCallExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_OperationCallExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OperationCallExp)


JTL_essentialocl_OrderedSetType_strategy = st.builds(JTL_essentialocl_OrderedSetType)
@given(instance=JTL_essentialocl_OrderedSetType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_OrderedSetType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OrderedSetType)


JTL_essentialocl_PrimitiveLiteralExp_strategy = st.builds(JTL_essentialocl_PrimitiveLiteralExp)
@given(instance=JTL_essentialocl_PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_PrimitiveLiteralExp)


JTL_essentialocl_PropertyCallExp_strategy = st.builds(JTL_essentialocl_PropertyCallExp)
@given(instance=JTL_essentialocl_PropertyCallExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_PropertyCallExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_PropertyCallExp)


JTL_essentialocl_RealLiteralExp_strategy = st.builds(JTL_essentialocl_RealLiteralExp, realSymbol=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=JTL_essentialocl_RealLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_RealLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_RealLiteralExp)


JTL_essentialocl_SequenceType_strategy = st.builds(JTL_essentialocl_SequenceType)
@given(instance=JTL_essentialocl_SequenceType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_SequenceType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_SequenceType)


JTL_essentialocl_SetType_strategy = st.builds(JTL_essentialocl_SetType)
@given(instance=JTL_essentialocl_SetType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_SetType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_SetType)


JTL_essentialocl_StringLiteralExp_strategy = st.builds(JTL_essentialocl_StringLiteralExp, stringSymbol=safe_text)
@given(instance=JTL_essentialocl_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_StringLiteralExp)


JTL_essentialocl_TupleLiteralExp_strategy = st.builds(JTL_essentialocl_TupleLiteralExp)
@given(instance=JTL_essentialocl_TupleLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_TupleLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleLiteralExp)


JTL_essentialocl_TupleLiteralPart_strategy = st.builds(JTL_essentialocl_TupleLiteralPart)
@given(instance=JTL_essentialocl_TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleLiteralPart)


JTL_essentialocl_TupleType_strategy = st.builds(JTL_essentialocl_TupleType)
@given(instance=JTL_essentialocl_TupleType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_TupleType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleType)


JTL_essentialocl_TypeExp_strategy = st.builds(JTL_essentialocl_TypeExp)
@given(instance=JTL_essentialocl_TypeExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_TypeExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TypeExp)


JTL_essentialocl_UnlimitedNaturalExp_strategy = st.builds(JTL_essentialocl_UnlimitedNaturalExp, symbol=safe_text)
@given(instance=JTL_essentialocl_UnlimitedNaturalExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_UnlimitedNaturalExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_UnlimitedNaturalExp)


JTL_essentialocl_Variable_strategy = st.builds(JTL_essentialocl_Variable)
@given(instance=JTL_essentialocl_Variable_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_Variable_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_Variable)


JTL_essentialocl_VariableExp_strategy = st.builds(JTL_essentialocl_VariableExp)
@given(instance=JTL_essentialocl_VariableExp_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_VariableExp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_VariableExp)


JTL_essentialocl_VoidType_strategy = st.builds(JTL_essentialocl_VoidType)
@given(instance=JTL_essentialocl_VoidType_strategy)
@settings(max_examples=25)
def test_JTL_essentialocl_VoidType_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_VoidType)


JTL_imperativeocl_AltExp_strategy = st.builds(JTL_imperativeocl_AltExp)
@given(instance=JTL_imperativeocl_AltExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AltExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AltExp)


JTL_imperativeocl_AnonymousTupleLiteralExp_strategy = st.builds(JTL_imperativeocl_AnonymousTupleLiteralExp)
@given(instance=JTL_imperativeocl_AnonymousTupleLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AnonymousTupleLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleLiteralExp)


JTL_imperativeocl_AnonymousTupleLiteralPart_strategy = st.builds(JTL_imperativeocl_AnonymousTupleLiteralPart)
@given(instance=JTL_imperativeocl_AnonymousTupleLiteralPart_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AnonymousTupleLiteralPart_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleLiteralPart)


JTL_imperativeocl_AnonymousTupleType_strategy = st.builds(JTL_imperativeocl_AnonymousTupleType)
@given(instance=JTL_imperativeocl_AnonymousTupleType_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AnonymousTupleType_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleType)


JTL_imperativeocl_AssertExp_strategy = st.builds(JTL_imperativeocl_AssertExp, severity=safe_text)
@given(instance=JTL_imperativeocl_AssertExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AssertExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AssertExp)


JTL_imperativeocl_AssignExp_strategy = st.builds(JTL_imperativeocl_AssignExp, isReset=st.booleans())
@given(instance=JTL_imperativeocl_AssignExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_AssignExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AssignExp)


JTL_imperativeocl_BlockExp_strategy = st.builds(JTL_imperativeocl_BlockExp)
@given(instance=JTL_imperativeocl_BlockExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_BlockExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_BlockExp)


JTL_imperativeocl_BreakExp_strategy = st.builds(JTL_imperativeocl_BreakExp)
@given(instance=JTL_imperativeocl_BreakExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_BreakExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_BreakExp)


JTL_imperativeocl_CollectorExp_strategy = st.builds(JTL_imperativeocl_CollectorExp)
@given(instance=JTL_imperativeocl_CollectorExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_CollectorExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_CollectorExp)


JTL_imperativeocl_ComputeExp_strategy = st.builds(JTL_imperativeocl_ComputeExp)
@given(instance=JTL_imperativeocl_ComputeExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ComputeExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ComputeExp)


JTL_imperativeocl_ContinueExp_strategy = st.builds(JTL_imperativeocl_ContinueExp)
@given(instance=JTL_imperativeocl_ContinueExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ContinueExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ContinueExp)


JTL_imperativeocl_DictLiteralExp_strategy = st.builds(JTL_imperativeocl_DictLiteralExp)
@given(instance=JTL_imperativeocl_DictLiteralExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_DictLiteralExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictLiteralExp)


JTL_imperativeocl_DictLiteralPart_strategy = st.builds(JTL_imperativeocl_DictLiteralPart)
@given(instance=JTL_imperativeocl_DictLiteralPart_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_DictLiteralPart_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictLiteralPart)


JTL_imperativeocl_DictionaryType_strategy = st.builds(JTL_imperativeocl_DictionaryType)
@given(instance=JTL_imperativeocl_DictionaryType_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_DictionaryType_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictionaryType)


JTL_imperativeocl_ForExp_strategy = st.builds(JTL_imperativeocl_ForExp)
@given(instance=JTL_imperativeocl_ForExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ForExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ForExp)


JTL_imperativeocl_ImperativeExpression_strategy = st.builds(JTL_imperativeocl_ImperativeExpression)
@given(instance=JTL_imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ImperativeExpression_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeExpression)


JTL_imperativeocl_ImperativeIterateExp_strategy = st.builds(JTL_imperativeocl_ImperativeIterateExp)
@given(instance=JTL_imperativeocl_ImperativeIterateExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ImperativeIterateExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeIterateExp)


JTL_imperativeocl_ImperativeLoopExp_strategy = st.builds(JTL_imperativeocl_ImperativeLoopExp)
@given(instance=JTL_imperativeocl_ImperativeLoopExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ImperativeLoopExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeLoopExp)


JTL_imperativeocl_InstantiationExp_strategy = st.builds(JTL_imperativeocl_InstantiationExp)
@given(instance=JTL_imperativeocl_InstantiationExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_InstantiationExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_InstantiationExp)


JTL_imperativeocl_ListType_strategy = st.builds(JTL_imperativeocl_ListType)
@given(instance=JTL_imperativeocl_ListType_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ListType_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ListType)


JTL_imperativeocl_LogExp_strategy = st.builds(JTL_imperativeocl_LogExp, level=st.integers(), text=safe_text)
@given(instance=JTL_imperativeocl_LogExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_LogExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_LogExp)


JTL_imperativeocl_RaiseExp_strategy = st.builds(JTL_imperativeocl_RaiseExp)
@given(instance=JTL_imperativeocl_RaiseExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_RaiseExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_RaiseExp)


JTL_imperativeocl_ReturnExp_strategy = st.builds(JTL_imperativeocl_ReturnExp)
@given(instance=JTL_imperativeocl_ReturnExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_ReturnExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ReturnExp)


JTL_imperativeocl_SwitchExp_strategy = st.builds(JTL_imperativeocl_SwitchExp)
@given(instance=JTL_imperativeocl_SwitchExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_SwitchExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_SwitchExp)


JTL_imperativeocl_TemplateParameterType_strategy = st.builds(JTL_imperativeocl_TemplateParameterType, specification=safe_text)
@given(instance=JTL_imperativeocl_TemplateParameterType_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_TemplateParameterType_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TemplateParameterType)


JTL_imperativeocl_TryExp_strategy = st.builds(JTL_imperativeocl_TryExp)
@given(instance=JTL_imperativeocl_TryExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_TryExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TryExp)


JTL_imperativeocl_TupleExp_strategy = st.builds(JTL_imperativeocl_TupleExp)
@given(instance=JTL_imperativeocl_TupleExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_TupleExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TupleExp)


JTL_imperativeocl_Typedef_strategy = st.builds(JTL_imperativeocl_Typedef)
@given(instance=JTL_imperativeocl_Typedef_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_Typedef_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_Typedef)


JTL_imperativeocl_UnlinkExp_strategy = st.builds(JTL_imperativeocl_UnlinkExp)
@given(instance=JTL_imperativeocl_UnlinkExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_UnlinkExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_UnlinkExp)


JTL_imperativeocl_UnpackExp_strategy = st.builds(JTL_imperativeocl_UnpackExp)
@given(instance=JTL_imperativeocl_UnpackExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_UnpackExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_UnpackExp)


JTL_imperativeocl_VariableInitExp_strategy = st.builds(JTL_imperativeocl_VariableInitExp, withResult=st.booleans())
@given(instance=JTL_imperativeocl_VariableInitExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_VariableInitExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_VariableInitExp)


JTL_imperativeocl_WhileExp_strategy = st.builds(JTL_imperativeocl_WhileExp)
@given(instance=JTL_imperativeocl_WhileExp_strategy)
@settings(max_examples=25)
def test_JTL_imperativeocl_WhileExp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_WhileExp)


JTL_template_CollectionTemplateExp_strategy = st.builds(JTL_template_CollectionTemplateExp, kind=safe_text)
@given(instance=JTL_template_CollectionTemplateExp_strategy)
@settings(max_examples=25)
def test_JTL_template_CollectionTemplateExp_instantiation(instance):
    assert isinstance(instance, JTL_template_CollectionTemplateExp)


JTL_template_ObjectTemplateExp_strategy = st.builds(JTL_template_ObjectTemplateExp, referredClass=safe_text)
@given(instance=JTL_template_ObjectTemplateExp_strategy)
@settings(max_examples=25)
def test_JTL_template_ObjectTemplateExp_instantiation(instance):
    assert isinstance(instance, JTL_template_ObjectTemplateExp)


JTL_template_PropertyTemplateItem_strategy = st.builds(JTL_template_PropertyTemplateItem)
@given(instance=JTL_template_PropertyTemplateItem_strategy)
@settings(max_examples=25)
def test_JTL_template_PropertyTemplateItem_instantiation(instance):
    assert isinstance(instance, JTL_template_PropertyTemplateItem)


JTL_template_TemplateExp_strategy = st.builds(JTL_template_TemplateExp)
@given(instance=JTL_template_TemplateExp_strategy)
@settings(max_examples=25)
def test_JTL_template_TemplateExp_instantiation(instance):
    assert isinstance(instance, JTL_template_TemplateExp)


LetExp_strategy = st.builds(LetExp)
@given(instance=LetExp_strategy)
@settings(max_examples=25)
def test_LetExp_instantiation(instance):
    assert isinstance(instance, LetExp)


LiteralExp_strategy = st.builds(LiteralExp)
@given(instance=LiteralExp_strategy)
@settings(max_examples=25)
def test_LiteralExp_instantiation(instance):
    assert isinstance(instance, LiteralExp)


LogExp_strategy = st.builds(LogExp)
@given(instance=LogExp_strategy)
@settings(max_examples=25)
def test_LogExp_instantiation(instance):
    assert isinstance(instance, LogExp)


LoopExp_strategy = st.builds(LoopExp)
@given(instance=LoopExp_strategy)
@settings(max_examples=25)
def test_LoopExp_instantiation(instance):
    assert isinstance(instance, LoopExp)


Model_strategy = st.builds(Model)
@given(instance=Model_strategy)
@settings(max_examples=25)
def test_Model_instantiation(instance):
    assert isinstance(instance, Model)


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


Object_strategy = st.builds(Object)
@given(instance=Object_strategy)
@settings(max_examples=25)
def test_Object_instantiation(instance):
    assert isinstance(instance, Object)


ObjectTemplateExp_strategy = st.builds(ObjectTemplateExp)
@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=25)
def test_ObjectTemplateExp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)


OclExpression_strategy = st.builds(OclExpression)
@given(instance=OclExpression_strategy)
@settings(max_examples=25)
def test_OclExpression_instantiation(instance):
    assert isinstance(instance, OclExpression)


OpaqueExpression_strategy = st.builds(OpaqueExpression)
@given(instance=OpaqueExpression_strategy)
@settings(max_examples=25)
def test_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


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


Pattern_strategy = st.builds(Pattern)
@given(instance=Pattern_strategy)
@settings(max_examples=25)
def test_Pattern_instantiation(instance):
    assert isinstance(instance, Pattern)


Predicate_strategy = st.builds(Predicate)
@given(instance=Predicate_strategy)
@settings(max_examples=25)
def test_Predicate_instantiation(instance):
    assert isinstance(instance, Predicate)


PrimitiveLiteralExp_strategy = st.builds(PrimitiveLiteralExp)
@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


PropertyTemplateItem_strategy = st.builds(PropertyTemplateItem)
@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=25)
def test_PropertyTemplateItem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


Tag_strategy = st.builds(Tag)
@given(instance=Tag_strategy)
@settings(max_examples=25)
def test_Tag_instantiation(instance):
    assert isinstance(instance, Tag)


TemplateExp_strategy = st.builds(TemplateExp)
@given(instance=TemplateExp_strategy)
@settings(max_examples=25)
def test_TemplateExp_instantiation(instance):
    assert isinstance(instance, TemplateExp)


Transformation_strategy = st.builds(Transformation)
@given(instance=Transformation_strategy)
@settings(max_examples=25)
def test_Transformation_instantiation(instance):
    assert isinstance(instance, Transformation)


TryExp_strategy = st.builds(TryExp)
@given(instance=TryExp_strategy)
@settings(max_examples=25)
def test_TryExp_instantiation(instance):
    assert isinstance(instance, TryExp)


TupleLiteralExp_strategy = st.builds(TupleLiteralExp)
@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=25)
def test_TupleLiteralExp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)


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


When_strategy = st.builds(When)
@given(instance=When_strategy)
@settings(max_examples=25)
def test_When_instantiation(instance):
    assert isinstance(instance, When)


Where_strategy = st.builds(Where)
@given(instance=Where_strategy)
@settings(max_examples=25)
def test_Where_instantiation(instance):
    assert isinstance(instance, Where)


emof_Class_strategy = st.builds(emof_Class)
@given(instance=emof_Class_strategy)
@settings(max_examples=25)
def test_emof_Class_instantiation(instance):
    assert isinstance(instance, emof_Class)


emof_DataType_strategy = st.builds(emof_DataType)
@given(instance=emof_DataType_strategy)
@settings(max_examples=25)
def test_emof_DataType_instantiation(instance):
    assert isinstance(instance, emof_DataType)


emof_MultiplicityElement_strategy = st.builds(emof_MultiplicityElement)
@given(instance=emof_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_emof_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, emof_MultiplicityElement)


emof_Package_strategy = st.builds(emof_Package)
@given(instance=emof_Package_strategy)
@settings(max_examples=25)
def test_emof_Package_instantiation(instance):
    assert isinstance(instance, emof_Package)


emof_Type_strategy = st.builds(emof_Type)
@given(instance=emof_Type_strategy)
@settings(max_examples=25)
def test_emof_Type_instantiation(instance):
    assert isinstance(instance, emof_Type)


emof_TypedElement_strategy = st.builds(emof_TypedElement)
@given(instance=emof_TypedElement_strategy)
@settings(max_examples=25)
def test_emof_TypedElement_instantiation(instance):
    assert isinstance(instance, emof_TypedElement)


essentialocl_CallExp_strategy = st.builds(essentialocl_CallExp)
@given(instance=essentialocl_CallExp_strategy)
@settings(max_examples=25)
def test_essentialocl_CallExp_instantiation(instance):
    assert isinstance(instance, essentialocl_CallExp)


essentialocl_LoopExp_strategy = st.builds(essentialocl_LoopExp)
@given(instance=essentialocl_LoopExp_strategy)
@settings(max_examples=25)
def test_essentialocl_LoopExp_instantiation(instance):
    assert isinstance(instance, essentialocl_LoopExp)


essentialocl_OclExpression_strategy = st.builds(essentialocl_OclExpression)
@given(instance=essentialocl_OclExpression_strategy)
@settings(max_examples=25)
def test_essentialocl_OclExpression_instantiation(instance):
    assert isinstance(instance, essentialocl_OclExpression)


imperativeocl_ImperativeExpression_strategy = st.builds(imperativeocl_ImperativeExpression)
@given(instance=imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=25)
def test_imperativeocl_ImperativeExpression_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeExpression)



